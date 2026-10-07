"""Offline package-integrity regressions; never mutate a real Skill install."""
import base64
from contextlib import redirect_stdout, redirect_stderr
from copy import deepcopy
import hashlib
import io
import json
from pathlib import Path
import tempfile
import unittest
import urllib.error
from unittest.mock import patch

import validate_specialists as checker
import specialist_integrity as integrity

ITEM = {"id": "demo", "skill_name": "demo", "requirement": "required", "trigger": "test",
        "canonical_repository": "owner/repo", "skill_path": ".", "install_name": "demo"}
FILES = {"SKILL.md": b"---\nname: demo\ndescription: fixture\n---\nRead references/rule.md\n",
         "references/rule.md": b"Required rule\n", "scripts/check.py": b"raise SystemExit(0)\n",
         "assets/font.bin": b"\x00\xff\x01"}
COMMIT = "a" * 40
TREE = "b" * 40


def blob(data):
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


class SpecialistsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="uiux-specialist-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.files = dict(FILES)
        self.urls = []

    def install(self, root=None):
        package = (root or self.root) / "demo"
        for name, data in self.files.items():
            path = package / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        return package

    def api(self, url):
        self.urls.append(url)
        if url.endswith("/releases/latest"):
            return {"tag_name": "v1", "draft": False, "prerelease": False}
        if "/commits/" in url:
            return {"sha": COMMIT, "commit": {"tree": {"sha": TREE}}}
        if "/git/trees/" in url:
            return {"sha": TREE, "truncated": False, "tree": [
                {"path": name, "type": "blob", "mode": "100644", "sha": blob(data), "size": len(data)}
                for name, data in self.files.items()]}
        if "/git/blobs/" in url:
            data = next(data for data in self.files.values() if url.endswith(blob(data)))
            return {"encoding": "base64", "content": base64.b64encode(data).decode(),
                    "sha": blob(data), "size": len(data)}
        if "/contents/SKILL.md" in url:  # Pre-fix CLI reproduction uses this endpoint.
            return {"encoding": "base64", "content": base64.b64encode(self.files["SKILL.md"]).decode()}
        raise AssertionError(f"Unexpected API call: {url}")

    def run_check(self, *args, api=None):
        out, err = io.StringIO(), io.StringIO()
        with patch.object(checker, "load_registry", return_value={"specialists": [ITEM]}), \
             patch.object(checker, "github_json", side_effect=api or self.api), \
             patch("sys.argv", ["validate_specialists.py", *args]), redirect_stdout(out), redirect_stderr(err):
            code = checker.main()
        return code, out.getvalue() + err.getvalue()

    def strict(self, **kwargs):
        return self.run_check("--installed-root", str(self.root), "--require-current", **kwargs)

    def test_matching_entrypoint_missing_resource_is_not_current(self):
        package = self.install()
        (package / "references/rule.md").unlink()
        code, output = self.strict()
        self.assertEqual(code, 1, output)
        self.assertNotIn(": CURRENT ", output)
        self.assertIn("references/rule.md", output)

    def test_intact_package_and_binary_resource_match(self):
        self.install()
        code, output = self.strict()
        self.assertEqual(code, 0, output)
        self.assertIn(": CURRENT entrypoint=MATCH", output)
        self.assertIn(f"commit={COMMIT}", output)

    def test_missing_or_modified_reference_script_and_asset(self):
        for name in FILES:
            for missing in (True, False):
                with self.subTest(name=name, missing=missing):
                    package = self.install()
                    if missing:
                        (package / name).unlink()
                    else:
                        (package / name).write_bytes(b"modified")
                    code, output = self.strict()
                    self.assertEqual(code, 1, output)
                    self.assertNotIn(": CURRENT ", output)
                    self.assertIn(name, output)

    def test_upstream_resource_only_change_is_detected(self):
        self.install()
        self.files["references/rule.md"] = b"New upstream rule; unchanged SKILL.md"
        code, output = self.strict()
        self.assertEqual(code, 1, output)
        self.assertIn("entrypoint=MATCH", output)
        self.assertIn("MODIFIED_FILE references/rule.md", output)

    def test_default_branch_fallback_only_for_404(self):
        self.install()
        def api(url):
            if url.endswith("/releases/latest"):
                raise checker.CheckError("no release", status=404)
            if url.endswith("/repos/owner/repo"):
                return {"default_branch": "main"}
            return self.api(url)
        code, output = self.strict(api=api)
        self.assertEqual(code, 0, output)
        self.assertIn("channel=default-branch", output)
        self.assertTrue(any(url.endswith("/commits/main") for url in self.urls))
        for status in (403, 429, 500):
            with self.subTest(status=status):
                def denied(url):
                    raise checker.CheckError("denied", status=status)
                code, output = self.strict(api=denied)
                self.assertEqual(code, 1)
                self.assertIn("UPSTREAM_UNVERIFIED", output)
                self.assertNotIn(": CURRENT ", output)

    def test_single_resolution_and_no_moving_refs_in_resource_requests(self):
        self.install()
        code, output = self.strict()
        self.assertEqual(code, 0, output)
        self.assertEqual(sum("/commits/" in url for url in self.urls), 1)
        self.assertEqual(sum("/releases/latest" in url for url in self.urls), 1)
        resources = [url for url in self.urls if "/git/" in url]
        self.assertTrue(resources)
        self.assertTrue(all("v1" not in url and "ref=" not in url for url in resources))
        self.assertFalse(any("/contents/" in url for url in self.urls))

    def test_nested_package_ignores_unrelated_repository_siblings(self):
        self.install()
        child = "c" * 40
        package_tree = "d" * 40
        def api(url):
            if url.endswith(f"/git/trees/{TREE}"):
                return {"sha": TREE, "truncated": False, "tree": [
                    {"path": "skills", "type": "tree", "mode": "040000", "sha": child},
                    {"path": "aux", "type": "commit", "mode": "160000", "sha": "e" * 40}]}
            if url.endswith(f"/git/trees/{child}"):
                return {"sha": child, "truncated": False, "tree": [
                    {"path": "demo", "type": "tree", "mode": "040000", "sha": package_tree}]}
            if url.endswith(f"/git/trees/{package_tree}?recursive=1"):
                payload = self.api(f"https://api.github.com/repos/owner/repo/git/trees/{TREE}?recursive=1")
                payload["sha"] = package_tree
                return payload
            return self.api(url)
        with patch.dict(ITEM, {"skill_path": "skills/demo"}):
            code, output = self.strict(api=api)
        self.assertEqual(code, 0, output)

    def test_strict_flags_need_explicit_target_and_each_root(self):
        for flag in ("--require-current", "--require-required-installed"):
            code, output = self.run_check(flag)
            self.assertEqual(code, 1)
            self.assertIn("require --check-codex or --installed-root", output)
            self.assertFalse(self.urls)
        self.install()
        second = self.root / "second"
        self.install(second)
        (second / "demo/assets/font.bin").unlink()
        args = ("--installed-root", str(self.root), "--installed-root", str(second))
        code, output = self.run_check(*args, "--require-current")
        self.assertEqual(code, 1, output)
        self.assertIn(": CURRENT ", output)
        self.assertIn(": DIFFERS ", output)
        code, output = self.run_check(*args, "--require-required-installed")
        self.assertEqual(code, 0, output)  # Presence is intentionally distinct from integrity.
        code, output = self.run_check("--installed-root", str(self.root / "absent"), "--require-current")
        self.assertEqual(code, 1, output)
        self.assertIn(": MISSING ", output)
        for flag in ("--require-current", "--require-required-installed"):
            code, output = self.run_check("--installed-root", str(self.root), "--installed-root",
                                          str(self.root / "absent"), flag)
            self.assertEqual(code, 1, output)

    def test_additions_and_head_modifications_are_preserved_not_certified(self):
        package = self.install()
        extra = package / "vibe-head-contract.md"
        extra.write_bytes(b"owner integration")
        code, output = self.strict()
        self.assertEqual(code, 1, output)
        self.assertIn("UPSTREAM_MATCH_WITH_ADDITIONS", output)
        self.assertEqual(extra.read_bytes(), b"owner integration")
        (package / "SKILL.md").write_bytes(FILES["SKILL.md"] + b"\nHead-controlled policy\n")
        code, output = self.strict()
        self.assertEqual(code, 1, output)
        self.assertIn("MODIFIED_FILE SKILL.md", output)
        self.assertEqual(extra.read_bytes(), b"owner integration")

    def test_runtime_caches_do_not_hide_required_files(self):
        package = self.install()
        (package / "__pycache__").mkdir()
        (package / "__pycache__/cache.pyc").write_bytes(b"generated")
        self.assertEqual(self.strict()[0], 0)
        self.files["__pycache__/required.pyc"] = b"tracked upstream"
        self.assertEqual(self.strict()[0], 1)

    def test_permissions_and_local_links_are_unverified(self):
        package = self.install()
        original = Path.open
        def denied(path, *args, **kwargs):
            if path == package / "references/rule.md":
                raise PermissionError("fixture denied")
            return original(path, *args, **kwargs)
        with patch.object(Path, "open", denied):
            code, output = self.strict()
        self.assertEqual(code, 1, output)
        self.assertIn("UNVERIFIED", output)
        original_stat = integrity.regular_stat
        def linked(path):
            if path == package / "assets":
                raise checker.CheckError("Unsupported local link/reparse point")
            return original_stat(path)
        with patch.object(integrity, "regular_stat", linked):
            code, output = self.strict()
        self.assertEqual(code, 1, output)
        self.assertIn("link/reparse", output)

    def test_real_symlink_is_not_followed(self):
        package = self.install()
        target = package / "references/rule.md"
        target.unlink()
        outside = self.root / "outside.md"
        outside.write_bytes(FILES["references/rule.md"])
        try:
            target.symlink_to(outside)
        except OSError as exc:
            self.skipTest(f"Native symlink creation unavailable: {exc}")
        code, output = self.strict()
        self.assertEqual(code, 1, output)
        self.assertIn("link/reparse", output)
        self.assertEqual(outside.read_bytes(), FILES["references/rule.md"])

    def test_upstream_unsafe_paths_modes_collisions_and_bounds(self):
        self.install()
        for change in ("../outside", "C:/x", "a\\b", "/root", "con.txt", "rule. ",
                       "symlink", "submodule", "duplicate", "case-collision", "ancestor-collision",
                       "truncated", "bad-size", "oversize", "bad-sha", "wrong-tree", "file-directory"):
            def api(url):
                payload = self.api(url)
                if "/git/trees/" not in url:
                    return payload
                record = payload["tree"][1]
                if change == "symlink":
                    record["mode"] = "120000"
                elif change == "submodule":
                    record.update(type="commit", mode="160000")
                elif change == "duplicate":
                    payload["tree"].append(dict(record))
                elif change == "case-collision":
                    payload["tree"].append({**record, "path": record["path"].upper()})
                elif change == "ancestor-collision":
                    payload["tree"].append({**record, "path": "REFERENCES/other.md"})
                elif change == "file-directory":
                    payload["tree"].append({**record, "path": "SKILL.md/child"})
                elif change == "truncated":
                    payload["truncated"] = True
                elif change == "bad-size":
                    record["size"] = True
                elif change == "oversize":
                    record["size"] = integrity.MAX_FILE_BYTES + 1
                elif change == "bad-sha":
                    record["sha"] = "../bad"
                elif change == "wrong-tree":
                    payload["sha"] = "f" * 40
                else:
                    record["path"] = change
                return payload
            with self.subTest(change=change):
                code, output = self.strict(api=api)
                self.assertEqual(code, 1, output)
                self.assertIn("UPSTREAM_UNVERIFIED", output)

    def test_entrypoint_blob_mismatch_and_malformed_remote_metadata(self):
        self.install()
        for change in ("blob", "commit", "release", "missing-entrypoint"):
            def api(url):
                payload = self.api(url)
                if change == "blob" and "/git/blobs/" in url:
                    payload["content"] = base64.b64encode(b"tampered").decode()
                if change == "commit" and "/commits/" in url:
                    payload = {"sha": COMMIT}
                if change == "release" and url.endswith("/releases/latest"):
                    payload = {"tag_name": "v1", "draft": True, "prerelease": False}
                if change == "missing-entrypoint" and "/git/trees/" in url:
                    payload["tree"] = payload["tree"][1:]
                return payload
            with self.subTest(change=change):
                self.assertEqual(self.strict(api=api)[0], 1)

    def test_request_and_json_fail_closed_without_leaking_body(self):
        with patch.object(checker.urllib.request, "build_opener") as factory:
            for exc in (TimeoutError(), urllib.error.URLError("offline"), checker.http.client.IncompleteRead(b"partial"),
                        urllib.error.HTTPError("url", 429, "rate limited", {}, io.BytesIO(b"sensitive body"))):
                factory.return_value.open.side_effect = exc
                with self.assertRaises(checker.CheckError) as failure:
                    checker.github_request("https://api.github.com/repos/owner/repo")
                self.assertNotIn("sensitive body", str(failure.exception))
            factory.return_value.open.side_effect = None
            factory.return_value.open.return_value.__enter__.return_value.read.return_value = b"x" * 9
            with patch.object(checker, "MAX_RESPONSE_BYTES", 8), self.assertRaises(checker.CheckError):
                checker.github_request("https://api.github.com/repos/owner/repo")
            for url in ("http://api.github.com/repos/a/b", "https://evil.test/repos/a/b",
                        "https://api.github.com@evil.test/repos/a/b"):
                with self.assertRaises(checker.CheckError):
                    checker.github_request(url)
        self.assertIsNone(checker.NoRedirect().redirect_request(None, None, 302, "", {}, "https://evil.test"))
        for raw in (b"[]", b"{", b"\xff"):
            with patch.object(checker, "github_request", return_value=raw), self.assertRaises(checker.CheckError):
                checker.github_json("https://api.github.com/repos/a/b")

    def test_package_and_scan_limits_fail_closed(self):
        self.install()
        for field, limit in (("MAX_ENTRIES", 2), ("MAX_PACKAGE_BYTES", 2), ("MAX_ENTRYPOINT_BYTES", 2)):
            with self.subTest(field=field), patch.object(integrity, field, limit):
                code, output = self.strict()
                self.assertEqual(code, 1, output)
                self.assertIn("UPSTREAM_UNVERIFIED", output)
        upstream = integrity.remote_package(ITEM, "v1", "test", self.api)
        for field in ("MAX_ENTRIES", "MAX_FILE_BYTES", "MAX_PACKAGE_BYTES", "MAX_ENTRYPOINT_BYTES"):
            with self.subTest(field=field), patch.object(integrity, field, 2):
                result = integrity.inspect_package(self.root / "demo", upstream)
                self.assertEqual(result["state"], "UNVERIFIED", result)

    def test_registry_only_never_uses_network(self):
        def denied(url):
            self.fail(f"Unexpected request: {url}")
        code, output = self.run_check(api=denied)
        self.assertEqual(code, 0, output)
        self.assertIn("No network/install freshness check requested", output)

    def test_registry_path_and_type_validation(self):
        base = {"schema_version": 1, "policy": {"allow_version_pins": False,
                "vendor_specialists": False, "head_precedence": True}, "specialists": [ITEM]}
        for key, bad in (("install_name", "../outside"), ("install_name", "nested/demo"),
                         ("skill_path", "/absolute"), ("skill_path", "a/../b"),
                         ("canonical_repository", "owner/.."), ("id", [])):
            value = deepcopy(base)
            value["specialists"][0][key] = bad
            with patch.object(Path, "read_text", return_value=json.dumps(value)), self.assertRaises(checker.CheckError):
                checker.load_registry()

    def test_read_only_snapshots_and_non_strict_reporting(self):
        package = self.install()
        (package / "scripts/check.py").write_bytes(b"locally edited")
        before = {p.relative_to(package).as_posix(): p.read_bytes() for p in package.rglob("*") if p.is_file()}
        code, output = self.run_check("--installed-root", str(self.root))
        self.assertEqual(code, 0, output)
        self.assertIn(": DIFFERS ", output)
        after = {p.relative_to(package).as_posix(): p.read_bytes() for p in package.rglob("*") if p.is_file()}
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
