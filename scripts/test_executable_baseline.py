"""Exact positive input binding and preparation, not agent or visual approval."""
from __future__ import annotations

import json
from pathlib import Path
import shutil
import tempfile
import unittest
from baseline_binding import validate_baseline

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "evals/fixtures/executable-baseline"


class ExecutableBaselineTests(unittest.TestCase):
    def test_real_input_pair_and_fictional_binding_match(self):
        self.assertEqual(validate_baseline(FIXTURE), [])

    def test_changed_source_handbook_or_approval_is_rejected(self):
        for name in ("index.html", "DESIGN.md", "OWNER_NOTES.md"):
            with self.subTest(name=name), tempfile.TemporaryDirectory() as temporary:
                copy = Path(temporary) / "fixture"
                shutil.copytree(FIXTURE, copy)
                path = copy / name
                if name == "OWNER_NOTES.md":
                    path.write_bytes(path.read_bytes().replace(b"fixture-owner-1", b"unrelated-owner"))
                else:
                    path.write_bytes(path.read_bytes() + b"\nChanged input.\n")
                self.assertTrue(validate_baseline(copy))

    def test_missing_original_is_not_authenticated(self):
        with tempfile.TemporaryDirectory() as temporary:
            copy = Path(temporary) / "fixture"
            shutil.copytree(FIXTURE, copy)
            (copy / "index.html").unlink()
            self.assertTrue(validate_baseline(copy))

    def test_untrusted_manifest_path_is_not_followed(self):
        with tempfile.TemporaryDirectory() as temporary:
            copy = Path(temporary) / "fixture"
            shutil.copytree(FIXTURE, copy)
            record = json.loads((copy / "BASELINE.json").read_text(encoding="utf-8"))
            record["files"]["../outside-secret"] = "a" * 64
            (copy / "BASELINE.json").write_text(json.dumps(record), encoding="utf-8")
            errors = validate_baseline(copy)
            self.assertTrue(errors)
            self.assertFalse(any("outside-secret" in error for error in errors))

    def test_malformed_record_or_files_is_rejected_without_crashing(self):
        for record in ([], {"files": []}, {"files": None}, {"files": "index.html"}):
            with self.subTest(record=record), tempfile.TemporaryDirectory() as temporary:
                copy = Path(temporary) / "fixture"
                shutil.copytree(FIXTURE, copy)
                (copy / "BASELINE.json").write_text(json.dumps(record), encoding="utf-8")
                self.assertTrue(validate_baseline(copy))


if __name__ == "__main__":
    unittest.main()
