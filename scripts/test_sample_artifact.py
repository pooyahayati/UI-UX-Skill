"""Authored sample artifact integrity; not browser/model conformance tests."""
from __future__ import annotations

import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import unittest
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "evals/samples/dispatch-notes"


class LocalReferences(HTMLParser):
    def __init__(self):
        super().__init__()
        self.references = []
        self.ids = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if "id" in values:
            self.ids.append(values["id"])
        for key in ("src", "href"):
            if key in values:
                self.references.append(values[key])


class SampleArtifactIntegrity(unittest.TestCase):
    def test_local_html_and_css_assets_resolve(self):
        metadata = json.loads((SAMPLE / "sample.json").read_text(encoding="utf-8"))
        for document in SAMPLE.glob("*.html"):
            parser = LocalReferences()
            parser.feed(document.read_text(encoding="utf-8"))
            self.assertEqual(len(parser.ids), len(set(parser.ids)), document.name)
            for raw in parser.references:
                reference = urlsplit(raw)
                self.assertFalse(reference.scheme or reference.netloc, raw)
                path = (document.parent / reference.path).resolve()
                self.assertTrue(path.is_relative_to(SAMPLE.resolve()), raw)
                self.assertTrue(path.exists(), raw)
                if reference.fragment and not reference.path and not reference.query:
                    # The entry uses intentional application routes, not scroll anchors.
                    routes = metadata["hash_routes"] if document.name == metadata["entry"] else []
                    self.assertIn(reference.fragment, parser.ids + routes, raw)
        for css in SAMPLE.glob("*.css"):
            for reference in re.findall(r'url\("([^"]+)"\)', css.read_text(encoding="utf-8")):
                self.assertTrue((SAMPLE / reference).is_file(), reference)

    def test_actual_font_bytes_keep_matching_license(self):
        expected = {
            "Vazirmatn-Regular.ttf": "b69fd4c680b8f3f225feabcc655a2c585d97627b8f5f5c0f9985e894069f3a56",
            "Vazirmatn-Bold.ttf": "f635fdbea28f265de395ba83b4b1570dcf2f58d13c65469e61903b1c2d2ae723",
        }
        for name, digest in expected.items():
            self.assertEqual(hashlib.sha256((SAMPLE / "fonts" / name).read_bytes()).hexdigest(), digest)
        license_text = (SAMPLE / "fonts/OFL.txt").read_text(encoding="utf-8")
        self.assertIn("Copyright 2015 The Vazirmatn Project Authors", license_text)
        self.assertIn("SIL OPEN FONT LICENSE Version 1.1", license_text)
        self.assertIn("OTHER DEALINGS IN THE FONT SOFTWARE", license_text)

    def test_revision_and_raw_input_boundary(self):
        metadata = json.loads((SAMPLE / "sample.json").read_text(encoding="utf-8"))
        handbook = (SAMPLE / metadata["handbook"]).read_text(encoding="utf-8")
        self.assertIn("Sample revision: " + metadata["sample_revision"], handbook)
        self.assertIn("Handbook revision: " + metadata["handbook_revision"], handbook)
        self.assertEqual(metadata["default_language"], "en")
        self.assertEqual(metadata["supported_languages"], {"en": "ltr", "fa": "rtl"})
        self.assertTrue((SAMPLE / metadata["language_source"]).is_file())
        for field in ("entry", "comparison", "supported_language_comparison", "rendered_review"):
            self.assertTrue((SAMPLE / metadata[field]).is_file(), field)
        self.assertFalse(SAMPLE.is_relative_to(ROOT / "evals/fixtures"))
        cases = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))["cases"]
        self.assertTrue(all("samples/dispatch-notes" not in str(case) for case in cases))


if __name__ == "__main__":
    unittest.main()
