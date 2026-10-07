"""Resource routing must be checked inside the selected source/consumer root."""
from __future__ import annotations

import contextlib
import io
import json
from pathlib import Path
import shutil
import tempfile
import unittest
import zipfile
from unittest.mock import patch

import package_release
import validate_resource_routes as routes


class ResourceRouteTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="uiux-resource-test-")
        self.addCleanup(temporary.cleanup)
        self.base = Path(temporary.name).resolve()
        self.root = self.base / "skill"
        self.write("SKILL.md", "Read `references/products/web/page.md`.\nRead `product-types.json`.\n")
        self.write("references/products/web/page.md", "Read `../../shared/rule.md`.\n")
        self.write("references/shared/rule.md", "# Shared rule\n")
        for name in ("product-types.json", "shared-rules.json", "design-system.json"):
            self.write(name, json.dumps({"modules": [{"reference": "references/shared/rule.md"}]}))

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def test_real_source_routes_resolve(self):
        self.assertEqual(routes.validate_resources(routes.DEFAULT_SKILL), [])

    def test_nested_owner_relative_and_explicit_skill_root_routes(self):
        self.write("references/products/web/page.md", "Read `../../shared/rule.md` and `references/shared/rule.md`.\n")
        self.assertEqual(routes.validate_resources(self.root), [])

    def test_wrong_depth_has_file_line_target_diagnostic(self):
        self.write("references/products/web/page.md", "# Page\nRead `../shared/rule.md`.\n")
        errors = routes.validate_resources(self.root)
        self.assertEqual(len(errors), 1)
        self.assertIn("references/products/web/page.md:2: '../shared/rule.md'", errors[0])

    def test_no_repo_or_skill_root_fallback_for_owner_relative_link(self):
        self.write("references/products/web/page.md", "[Rule](shared/rule.md)\n")
        self.write("shared/rule.md", "Must not satisfy the nested link")
        self.assertTrue(routes.validate_resources(self.root))

    def test_links_encoded_spaces_titles_and_fragment_paths(self):
        self.write("references/shared/with space.md", "# Anchor")
        self.write("references/products/web/page.md", '[rule](../../shared/rule.md#anchor "Title")\n'
                   '[space](<../../shared/with space.md>)\n[encoded](../../shared/with%20space.md)\n')
        self.assertEqual(routes.validate_resources(self.root), [])

    def test_external_generated_and_fenced_examples_are_not_dependencies(self):
        self.write("references/products/web/page.md", '`DESIGN.md` and `design-profile.md` are product output.\n'
                   '[external](https://example.test/missing.md) [anchor](#local)\n'
                   '```markdown\nRead `../missing.md`.\n[example](missing.md)\n```\n'
                   'Example: ``[link](missing.md)`` and `python scripts/example.py`.\n')
        self.assertEqual(routes.validate_resources(self.root), [])
        self.write("references/products/web/page.md", "Read `missing.md`.\n")
        self.assertTrue(routes.validate_resources(self.root))

    def test_repository_exclusions_are_exact_and_never_apply_to_markdown_links(self):
        self.write("references/material-runtime.md", "Repository helper: `scripts/runtime_appearance.py`.\n")
        self.assertEqual(routes.validate_resources(self.root), [])
        self.write("references/material-runtime.md", "[Required helper](scripts/runtime_appearance.py)\n")
        self.assertTrue(routes.validate_resources(self.root))

    def test_missing_registry_or_registry_resource_and_bad_shapes_fail(self):
        for content in ('[]', '{broken', '{"modules":[{"reference":7}]}',
                        '{"required_references":"references/shared/rule.md"}'):
            self.write("shared-rules.json", content)
            self.assertTrue(routes.validate_resources(self.root))
        self.write("shared-rules.json", '{"modules":[{"reference":"references/missing.md"}]}')
        self.assertTrue(any("references/missing.md" in e for e in routes.validate_resources(self.root)))
        (self.root / "shared-rules.json").unlink()
        self.assertTrue(any("missing required resource registry" in e for e in routes.validate_resources(self.root)))

    def test_outside_paths_cannot_satisfy_a_route(self):
        outside = self.base / "outside.md"
        outside.write_text("Do not use outside package", encoding="utf-8")
        for value in ("../outside.md", "../%6futside.md", outside.as_posix(), "file:///outside.md"):
            with self.subTest(value=value):
                self.write("SKILL.md", f"[Untrusted]({value})\n")
                self.assertTrue(routes.validate_resources(self.root))

    def test_external_registry_reference_cannot_pass_as_local(self):
        for value in ("https://example.test/rule.md", "", "#anchor", "?query"):
            with self.subTest(value=value):
                self.write("shared-rules.json", json.dumps({"modules": [{"reference": value}]}))
                self.assertTrue(any("local resource" in e for e in routes.validate_resources(self.root)))

    def test_permission_and_scan_errors_are_failures_not_empty_success(self):
        real_read = Path.read_text
        def denied_read(path, *args, **kwargs):
            if path == self.root / "references/shared/rule.md":
                raise PermissionError("test denial")
            return real_read(path, *args, **kwargs)
        with patch.object(Path, "read_text", denied_read):
            self.assertTrue(any("cannot read Markdown" in e for e in routes.validate_resources(self.root)))
        def denied_walk(*args, **kwargs):
            kwargs["onerror"](PermissionError("test scan denial"))
            return iter(())
        with patch.object(routes.os, "walk", denied_walk):
            self.assertTrue(any("cannot inspect" in e for e in routes.validate_resources(self.root)))

    def test_actual_symlink_cannot_hide_missing_consumer_resource(self):
        outside = self.base / "outside.md"
        outside.write_text("outside", encoding="utf-8")
        link = self.root / "references/shared/alias.md"
        try:
            link.symlink_to(outside)
        except OSError as error:
            self.skipTest(f"Host cannot create test symlink: {error}")
        self.write("references/products/web/page.md", "Read `../../shared/alias.md`.\n")
        self.assertTrue(any("escapes" in e for e in routes.validate_resources(self.root)))

    def test_empty_root_or_valid_first_root_cannot_hide_invalid_second_root(self):
        self.assertTrue(routes.validate_resources(self.base / "absent"))
        with patch("sys.argv", ["validate_resource_routes.py", "--skill-root", str(self.root),
                                "--skill-root", str(self.base / "absent")]), contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(SystemExit) as caught:
                routes.main()
        self.assertEqual(caught.exception.code, 1)

    def test_both_real_package_formats_are_checked_without_source_fallback(self):
        repo = self.base / "repo"
        shutil.copytree(self.root, repo / "skills/ui-ux-skill")
        for relative, value in {"VERSION":"3.2.0", "skills/ui-ux-skill/VERSION":"3.2.0",
                                "plugin.json":'{"name":"ui-ux","version":"3.2.0"}',
                                "assets/logo.svg":"<svg/>", "assets/composer-icon.svg":"<svg/>",
                                **{name:"Legal" for name in package_release.LEGAL_FILES}}.items():
            path = repo / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(value, encoding="utf-8")
        out = self.base / "packages"
        artifacts = package_release.package_release(out, root=repo)
        unpacked = self.base / "unpacked"
        for artifact in artifacts[:2]:
            with zipfile.ZipFile(artifact) as archive:
                archive.extractall(unpacked)  # trusted archives authored by this fixture
        for consumer in (unpacked / "ui-ux-skill", unpacked / "ui-ux/skills/ui-ux-skill"):
            with self.subTest(consumer=consumer):
                self.assertEqual(routes.validate_resources(consumer), [])
                (consumer / "references/shared/rule.md").unlink()
                self.assertTrue(routes.validate_resources(consumer))
        self.assertTrue((repo / "skills/ui-ux-skill/references/shared/rule.md").is_file())


if __name__ == "__main__":
    unittest.main()
