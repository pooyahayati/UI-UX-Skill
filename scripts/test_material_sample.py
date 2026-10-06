"""Meaningful phase/asset regressions; hypothetical records are not owner approval."""
from copy import deepcopy
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import unittest
from urllib.parse import urlsplit

from validate_material_sample import ROOT, SAMPLE, validate_metadata


class References(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []; self.ids = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        self.ids += [values["id"]] if "id" in values else []
        self.links += [values[k] for k in ("src", "href") if k in values]


class MaterialSampleTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((SAMPLE / "sample.json").read_text(encoding="utf-8"))
        self.identity = {k: self.data[k] for k in
                         ("sample_revision", "handbook_revision", "default_language", "direction", "theme")}

    def test_actual_primary_has_no_fabricated_approval_or_future_artifacts(self):
        self.assertEqual(validate_metadata(self.data), [])
        self.assertIsNone(self.data["approval"])
        self.assertIsNone(self.data["last_approved_baseline"])
        self.assertEqual(self.data["secondary"]["status"], "not-applicable")
        self.assertEqual({p.name for p in SAMPLE.glob("*.html")}, {"index.html"})
        self.assertFalse(self.data["admin"] or self.data["backend"])

    def hypothetical_approval(self, identity):
        return {"actor": "Synthetic test actor", "source": "Test only", "date": "unknown",
                "scope": "Test fixture, not real consent", "identity": deepcopy(identity)}

    def proposed_dark(self):
        self.data["approval"] = self.hypothetical_approval(self.identity)
        self.data["dark"] = {"status": "proposed", "parent": deepcopy(self.identity),
                             "entry": "index.html", "approval": None,
                             "identity": dict(self.identity, theme="dark", sample_revision="dark-test-r1")}

    def test_dark_without_primary_or_with_stale_parent_is_rejected(self):
        self.data["dark"]["entry"] = "index.html"
        self.assertTrue(validate_metadata(self.data))
        self.proposed_dark()
        self.assertEqual(validate_metadata(self.data), [])
        self.data["approval"] = None
        self.assertTrue(validate_metadata(self.data))
        self.proposed_dark()
        self.data["dark"]["parent"]["sample_revision"] = "older-r0"
        self.assertTrue(validate_metadata(self.data))

    def test_style_selection_boolean_and_incomplete_source_cannot_approve(self):
        for value in (True, "selected", {"identity": self.identity},
                      dict(self.hypothetical_approval(self.identity), source="")):
            with self.subTest(value=value):
                self.data["approval"] = value
                self.assertTrue(validate_metadata(self.data))

    def test_secondary_requires_dark_and_named_need_authority(self):
        self.proposed_dark()
        self.data["secondary"] = {"status": "proposed", "entry": "index.html",
                                  "parent": deepcopy(self.data["dark"]["identity"]),
                                  "authorization": {"actor": "Test", "source": "Test", "scope": "Test",
                                                    "date": "unknown", "language": "en", "direction": "ltr", "need": "Test only"}}
        self.assertTrue(validate_metadata(self.data))
        self.data["dark"]["status"] = "approved"
        self.data["dark"]["approval"] = self.hypothetical_approval(self.data["dark"]["identity"])
        self.assertEqual(validate_metadata(self.data), [])
        self.data["secondary"]["authorization"] = None
        self.assertTrue(validate_metadata(self.data))

    def test_revision_artifact_and_derived_identity_drift_is_rejected(self):
        self.data["handbook_revision"] = "h2"
        self.assertTrue(validate_metadata(self.data))
        self.setUp(); self.proposed_dark()
        self.data["dark"]["identity"]["default_language"] = "en"
        self.assertTrue(validate_metadata(self.data))
        self.setUp(); self.data["entry"] = "../../../../missing.html"
        self.assertTrue(validate_metadata(self.data))

    def test_native_assets_foundation_consumption_and_ids_resolve(self):
        parser = References(); parser.feed((SAMPLE / "index.html").read_text(encoding="utf-8"))
        self.assertEqual(len(parser.ids), len(set(parser.ids)))
        for raw in parser.links:
            parsed = urlsplit(raw)
            self.assertFalse(parsed.scheme or parsed.netloc)
            if not parsed.path:
                self.assertIn(parsed.fragment, parser.ids)
            else:
                self.assertTrue((SAMPLE / parsed.path).resolve().is_relative_to(ROOT / "evals"))
                self.assertTrue((SAMPLE / parsed.path).is_file())
        for raw in re.findall(r'url\("([^"]+)"\)', (SAMPLE / "styles.css").read_text(encoding="utf-8")):
            self.assertTrue((SAMPLE / raw).is_file())
        self.assertIn(self.data["foundations"], parser.links)
        css = (SAMPLE / "styles.css").read_text(encoding="utf-8")
        defined = set(re.findall(r'(--[\w-]+)\s*:', (SAMPLE / self.data["foundations"]).read_text(encoding="utf-8")))
        self.assertTrue(set(re.findall(r'var\((--[\w-]+)\)', css)).issubset(defined))


if __name__ == "__main__":
    unittest.main()
