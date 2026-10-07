"""Packager preservation regressions; destructive reproductions use owned fixtures only."""
from __future__ import annotations

import contextlib
import io
import json
import hashlib
import os
from pathlib import Path
import subprocess
import stat
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import zipfile

import package_release as packager


class PackageReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="uiux-package-test-")
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name).resolve()
        self.root = self.base / "repo"
        self.skill = self.root / "skills" / "ui-ux-skill"
        files = {
            "VERSION": "3.2.0\n",
            "plugin.json": json.dumps({"name": "ui-ux", "version": "3.2.0"}),
            "skills/ui-ux-skill/VERSION": "3.2.0\n",
            "skills/ui-ux-skill/SKILL.md": "# Fixture skill\n",
            "skills/ui-ux-skill/references/example.md": "Fixture reference\n",
            "assets/logo.svg": "<svg/>\n",
            "assets/composer-icon.svg": "<svg/>\n",
            **{name: "Fixture legal text\n" for name in
               ("LICENSE", "PRIVACY.md", "TERMS.md", "SUPPORT.md")},
        }
        for name, text in files.items():
            target = self.root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text, encoding="utf-8")

    def test_existing_output_is_rejected_before_any_recursive_delete(self):
        out = self.base / "existing-output"
        out.mkdir()
        sentinel = out / "owner-data.txt"
        sentinel.write_bytes(b"preserve me")
        # On the audited implementation this intercepts the dangerous call;
        # no actual recursive deletion of an output directory is allowed.
        with patch.object(packager, "ROOT", self.root), \
             patch("sys.argv", ["package_release.py", "--output", str(out)]), \
             patch.object(packager.shutil, "rmtree", side_effect=AssertionError("unsafe delete")), \
             contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as caught:
                packager.main()
        self.assertEqual(caught.exception.code, 1)
        self.assertEqual(sentinel.read_bytes(), b"preserve me")

    def snapshot(self):
        return {str(p.relative_to(self.base)): p.read_bytes() if p.is_file() else None
                for p in self.base.rglob("*")}

    def assert_refused_without_writes(self, output):
        before = self.snapshot()
        with patch.object(packager.tempfile, "TemporaryDirectory", side_effect=AssertionError("staging before validation")) as staging:
            with self.assertRaises((ValueError, OSError)):
                packager.package_release(output, root=self.root)
            staging.assert_not_called()
        self.assertEqual(self.snapshot(), before)

    def test_repository_ancestors_and_source_paths_are_rejected(self):
        for output in (".", "..", "skills", "skills/new-output", ".git/new-output",
                       "assets/new-output", "scripts/new-output", "new-source-dir",
                       "dist/child", self.root, self.base, self.skill, self.skill / "new"):
            with self.subTest(output=str(output)):
                self.assert_refused_without_writes(output)

    def test_existing_empty_nonempty_directory_and_file_are_preserved(self):
        for kind in ("empty", "nonempty", "file"):
            output = self.base / kind
            if kind == "file":
                output.write_bytes(b"owner data")
            else:
                output.mkdir()
                if kind == "nonempty":
                    (output / "sentinel").write_bytes(b"owner data")
            with self.subTest(kind=kind):
                self.assert_refused_without_writes(output)

    def test_empty_argument_missing_parent_and_file_parent_are_rejected(self):
        for output in ("", "   ", self.base / "missing-parent" / "output",
                       self.root / "VERSION" / "output"):
            with self.subTest(output=str(output)):
                self.assert_refused_without_writes(output)

    def test_missing_required_inputs_are_rejected_before_staging(self):
        for name in ("VERSION", "plugin.json", "skills/ui-ux-skill/VERSION",
                     "skills/ui-ux-skill/SKILL.md", "assets/logo.svg",
                     "assets/composer-icon.svg", *packager.LEGAL_FILES):
            path = self.root / name
            original = path.read_bytes()
            path.unlink()
            with self.subTest(name=name):
                self.assert_refused_without_writes(self.base / "output")
            path.write_bytes(original)

    def test_invalid_versions_plugin_names_and_json_are_rejected(self):
        cases = [("VERSION", "../../escape"), ("VERSION", ""),
                 ("skills/ui-ux-skill/VERSION", "9.0.0"),
                 ("plugin.json", "not json"), ("plugin.json", "[]")]
        cases += [("plugin.json", json.dumps(value)) for value in (
            {"name": "ui-ux", "version": "0.0.0"},
            {"name": "../escape", "version": "3.2.0"},
            {"name": "/escape", "version": "3.2.0"},
            {"name": "C:\\escape", "version": "3.2.0"},
            {"name": None, "version": "3.2.0"})]
        for name, value in cases:
            path = self.root / name
            original = path.read_bytes()
            path.write_text(value, encoding="utf-8")
            with self.subTest(name=name, value=value):
                self.assert_refused_without_writes(self.base / "output")
            path.write_bytes(original)

    def test_fresh_external_output_has_exact_members_crc_versions_and_checksums(self):
        source_before = self.snapshot()
        out = self.base / "new output"
        results = packager.package_release(out, root=self.root)
        self.assertEqual([p.name for p in results], [
            "ui-ux-skill-claude-v3.2.0.zip", "ui-ux-plugin-v3.2.0.zip", "SHA256SUMS.txt"])
        skill_members = {"ui-ux-skill/" + p.relative_to(self.skill).as_posix(): p.read_bytes()
                         for p in self.skill.rglob("*") if p.is_file()}
        plugin_members = {"ui-ux/skills/" + name: data for name, data in skill_members.items()}
        for name in ("plugin.json", *packager.LEGAL_FILES, "assets/logo.svg", "assets/composer-icon.svg"):
            plugin_members["ui-ux/" + name] = (self.root / name).read_bytes()
        for archive, expected in zip(results[:2], (skill_members, plugin_members)):
            with zipfile.ZipFile(archive) as opened:
                self.assertIsNone(opened.testzip())
                self.assertEqual(set(opened.namelist()), set(expected))
                for member, data in expected.items():
                    self.assertEqual(opened.read(member), data)
                    self.assertEqual(opened.getinfo(member).date_time, (2026, 1, 1, 0, 0, 0))
        for line in results[2].read_text(encoding="utf-8").splitlines():
            digest, name = line.split("  ")
            self.assertEqual(hashlib.sha256((out / name).read_bytes()).hexdigest(), digest)
        after = self.snapshot()
        self.assertEqual({k: after[k] for k in source_before}, source_before)
        self.assertFalse(list(self.base.glob(".uiux-package-*")))

    def test_default_dist_and_relative_external_output_succeed_but_repeat_is_refused(self):
        for output, resolved in (("dist", self.root / "dist"), ("../relative-output", self.base / "relative-output")):
            with self.subTest(output=output):
                paths = packager.package_release(output, root=self.root)
                self.assertTrue(all(p.parent == resolved for p in paths))
                self.assert_refused_without_writes(output)

    def test_copy_zip_checksum_and_publish_failures_preserve_source_and_prior_output(self):
        prior = self.base / "prior-output"
        packager.package_release(prior, root=self.root)
        before = self.snapshot()
        out = self.base / "candidate"
        real_write = Path.write_text

        def fail_checksums(path, *args, **kwargs):
            if path.name == "SHA256SUMS.txt":
                raise OSError("injected checksum write failure")
            return real_write(path, *args, **kwargs)

        failures = [patch.object(packager.shutil, "copy2", side_effect=OSError("copy failed")),
                    patch.object(packager.zipfile.ZipFile, "writestr", side_effect=OSError("archive failed")),
                    patch.object(Path, "write_text", fail_checksums),
                    patch.object(Path, "rename", side_effect=PermissionError("publish denied")),
                    patch.object(packager.tempfile, "TemporaryDirectory", side_effect=PermissionError("stage denied"))]
        for index, failure in enumerate(failures):
            with self.subTest(failure=index), failure:
                with self.assertRaises(OSError):
                    packager.package_release(out, root=self.root)
            self.assertFalse(out.exists())
            self.assertEqual(self.snapshot(), before)

    def test_destination_created_during_build_is_preserved(self):
        real_build = packager.build_artifacts
        for nonempty in (False, True):
            out = self.base / f"collision-{nonempty}"

            def collide(*args):
                results = real_build(*args)
                out.mkdir()
                if nonempty:
                    (out / "sentinel").write_bytes(b"other writer")
                return results

            with self.subTest(nonempty=nonempty), patch.object(packager, "build_artifacts", collide):
                with self.assertRaisesRegex(ValueError, "already exists"):
                    packager.package_release(out, root=self.root)
            self.assertTrue(out.is_dir())
            if nonempty:
                self.assertEqual((out / "sentinel").read_bytes(), b"other writer")
            self.assertFalse(list(self.base.glob(".uiux-package-*")))

    def create_symlink(self, link, target, directory=False):
        try:
            link.symlink_to(target, target_is_directory=directory)
        except OSError as error:
            self.skipTest(f"Host cannot create test symlinks: {error}")
        self.addCleanup(link.unlink)

    def test_output_symlink_ancestor_and_dangling_symlink_are_rejected(self):
        alias = self.base / "alias"
        self.create_symlink(alias, self.root, directory=True)
        dangling = self.base / "dangling"
        self.create_symlink(dangling, self.base / "absent", directory=True)
        for output in (alias, alias / "dist", dangling):
            with self.subTest(output=output), patch.object(packager.tempfile, "TemporaryDirectory", side_effect=AssertionError("staging before validation")) as stage:
                with self.assertRaisesRegex(ValueError, "symlink/reparse"):
                    packager.package_release(output, root=self.root)
                stage.assert_not_called()
        self.assertFalse((self.root / "dist").exists())

    def test_source_symlinks_are_rejected_even_when_directory_or_dangling(self):
        target = self.base / "unrelated"
        target.mkdir()
        (target / "sentinel").write_bytes(b"do not package")
        for name, dest, is_dir in (("directory", target, True),
                                   ("file", target / "sentinel", False),
                                   ("dangling", target / "missing", False)):
            link = self.skill / name
            try:
                link.symlink_to(dest, target_is_directory=is_dir)
            except OSError as error:
                self.skipTest(f"Host cannot create test symlinks: {error}")
            try:
                with self.subTest(name=name), patch.object(packager.tempfile, "TemporaryDirectory", side_effect=AssertionError("staging before validation")) as stage:
                    with self.assertRaisesRegex(ValueError, "symlink/reparse"):
                        packager.package_release(self.base / "output", root=self.root)
                    stage.assert_not_called()
            finally:
                link.unlink()
        self.assertEqual((target / "sentinel").read_bytes(), b"do not package")

    def test_reported_symlink_and_reparse_types_are_denied_before_staging(self):
        # Deterministic boundary coverage even on hosts lacking symlink privileges.
        # This is mocked filesystem evidence, not a native symlink capability claim.
        real_lstat = Path.lstat
        for target in (self.base / "output", self.skill / "SKILL.md"):
            for mode, attributes in ((stat.S_IFLNK, 0), (stat.S_IFDIR, 0x400)):
                def report_link(path, *args, **kwargs):
                    if path == target:
                        return SimpleNamespace(st_mode=mode, st_file_attributes=attributes)
                    return real_lstat(path, *args, **kwargs)
                with self.subTest(target=target, mode=mode), \
                     patch.object(Path, "lstat", report_link), \
                     patch.object(packager.tempfile, "TemporaryDirectory", side_effect=AssertionError("staging before validation")) as stage:
                    with self.assertRaisesRegex(ValueError, "symlink/reparse"):
                        packager.package_release(self.base / "output", root=self.root)
                    stage.assert_not_called()

    @unittest.skipUnless(os.name == "nt", "Windows path aliases")
    def test_windows_device_drive_relative_case_and_spelling_aliases(self):
        for output in (str(self.root).upper(), "C:relative", "\\rooted", "\\\\?\\" + str(self.root),
                       "//?/" + str(self.skill / "new-output").replace("\\", "/"),
                       "//./" + str(self.skill / "new-output").replace("\\", "/"),
                       str(self.skill / "new-output").upper(),
                       "\\\\.\\C:\\output", "dist.", "dist ", "dist:stream", "NUL", "COM1.zip"):
            with self.subTest(output=output):
                self.assert_refused_without_writes(output)

    @unittest.skipUnless(os.name == "nt", "Windows junctions")
    def test_windows_junction_source_and_output_ancestor_are_rejected(self):
        target = self.base / "unrelated"
        target.mkdir()
        sentinel = target / "sentinel"
        sentinel.write_bytes(b"unchanged")
        for link in (self.base / "output-alias", self.skill / "linked-source"):
            result = subprocess.run(["cmd.exe", "/d", "/c", "mklink", "/J", str(link), str(target)],
                                    capture_output=True, text=True)
            if result.returncode:
                self.skipTest(f"Host cannot create test junction: {result.stderr}")
            self.addCleanup(link.rmdir)
        with self.assertRaisesRegex(ValueError, "symlink/reparse"):
            packager.package_release(self.base / "output-alias" / "output", root=self.root)
        with self.assertRaisesRegex(ValueError, "symlink/reparse"):
            packager.package_release(self.base / "output", root=self.root)
        self.assertEqual(sentinel.read_bytes(), b"unchanged")

    def test_cli_success_prints_only_completed_artifacts(self):
        out = self.base / "cli-output"
        stdout = io.StringIO()
        with patch.object(packager, "ROOT", self.root), \
             patch("sys.argv", ["package_release.py", "--output", str(out)]), \
             contextlib.redirect_stdout(stdout):
            packager.main()
        paths = [Path(line) for line in stdout.getvalue().splitlines()]
        self.assertEqual(len(paths), 3)
        self.assertTrue(all(p.is_file() and p.parent == out for p in paths))


if __name__ == "__main__":
    unittest.main()
