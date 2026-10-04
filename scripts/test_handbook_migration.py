"""Concrete synthetic artifact compatibility tests, not model conformance."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import re
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "evals/fixtures/legacy-handbook"
EXAMPLE = ROOT / "evals/handbook/example"
spec = importlib.util.spec_from_file_location("legacy_reader", RAW / "tools/profile_reader.py")
reader = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reader)


class HandbookMigrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.product = Path(self.temp.name) / "product"
        shutil.copytree(RAW, self.product)
        self.before = reader.read_profile(self.product)
        self.tokens = (self.product / "ui-tokens.json").read_bytes()
        self.owner = (self.product / "OWNER.md").read_bytes()
        for name in ("DESIGN.md", "design-profile.md", "PROJECT.md"):
            shutil.copyfile(EXAMPLE / name, self.product / name)

    def test_existing_parser_keeps_accepted_payload(self):
        self.assertEqual(reader.read_profile(self.product), self.before)
        self.assertEqual(self.before, {"status": "approved", "density": "balanced"})

    def test_pointer_alone_cannot_replace_parser_input(self):
        (self.product / "design-profile.md").write_text("See DESIGN.md\n", encoding="utf-8")
        with self.assertRaises(ValueError):
            reader.read_profile(self.product)

    def test_value_and_owner_sources_are_preserved(self):
        self.assertEqual((self.product / "ui-tokens.json").read_bytes(), self.tokens)
        self.assertEqual((self.product / "OWNER.md").read_bytes(), self.owner)
        self.assertNotIn(b"#2563eb", (self.product / "DESIGN.md").read_bytes())

    def test_migrated_documentation_links_resolve(self):
        for name in ("DESIGN.md", "design-profile.md", "PROJECT.md"):
            text = (self.product / name).read_text(encoding="utf-8")
            links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
            self.assertTrue(links, name)
            for link in links:
                self.assertTrue((self.product / link).is_file(), f"{name}: {link}")


if __name__ == "__main__":
    unittest.main()
