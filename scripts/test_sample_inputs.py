"""Raw sample/continuation preparation regressions, not model or rendered UI checks."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

# Include exact positive binding regressions in the existing CI test entrypoint.
from test_executable_baseline import ExecutableBaselineTests

ROOT = Path(__file__).resolve().parents[1]
PREPARE = ROOT / "scripts/prepare_eval_run.py"
RAW_ROOT = ROOT / "evals/fixtures"
RAW_FILES = {
    "material-activation": {"README.md", "BRIEF.md"},
    "real-world-wordpress": {"README.md", "plugin.php", "admin.css"},
    "runtime-appearance-brief": {"README.md", "ADMIN.md", "ICONS.md", "NARROW.md",
                                 "NO_ADMIN.md", "PERSIAN_FONT.md", "FONT_EXISTING.md"},
    "sample-review": {"README.md", "BRIEF.md", "OWNER_NOTES.md", "FOUNDATION.json",
                      "variants/bilingual.md", "variants/revision-change.md"},
    "incremental-design": {"README.md", "BRIEF.md", "DESIGN.md", "OWNER_NOTES.md", "ui-tokens.json"},
    "executable-baseline": {".gitattributes", "README.md", "BRIEF.md", "DESIGN.md",
                            "OWNER_NOTES.md", "BASELINE.json", "index.html"},
}
MANIFEST = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
CASES = [c for c in MANIFEST["cases"]
         if c["id"].startswith(("samples-", "incremental-", "runtime-appearance-", "material-"))]


def files(root: Path) -> dict[str, bytes]:
    return {p.relative_to(root).as_posix(): p.read_bytes()
            for p in root.rglob("*") if p.is_file()}


class SampleInputPreparation(unittest.TestCase):
    def test_each_case_receives_only_exact_raw_inputs_and_prompt(self):
        raw_snapshots = {name: files(RAW_ROOT / name) for name in RAW_FILES}
        for name, expected_files in RAW_FILES.items():
            self.assertEqual(set(raw_snapshots[name]), expected_files)
        self.assertTrue(CASES)
        with tempfile.TemporaryDirectory() as temporary:
            for case in CASES:
                with self.subTest(case=case["id"]):
                    expected = raw_snapshots[case["fixture"]]
                    output = Path(temporary) / case["id"]
                    result = subprocess.run(
                        [sys.executable, "-B", str(PREPARE), case["id"], "--output", str(output)],
                        capture_output=True, text=True, encoding="utf-8", timeout=30,
                    )
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(files(output / "fixture"), expected)
                    self.assertEqual((output / "PROMPT.txt").read_text(encoding="utf-8"),
                                     case["prompt"] + "\n")
                    run = json.loads((output / "RUN.json").read_text(encoding="utf-8"))
                    self.assertEqual(run["caseId"], case["id"])
                    self.assertEqual(run["prompt"], case["prompt"])
                    self.assertEqual(run["fixture"], case["fixture"])
                    self.assertEqual(run["skillVersion"], MANIFEST["version"])
                    self.assertEqual(set(files(output)),
                                     {"RUN.json", "PROMPT.txt"} | {"fixture/" + p for p in expected})
        for name, expected in raw_snapshots.items():
            self.assertEqual(files(RAW_ROOT / name), expected)

    def test_preparation_refuses_existing_run_without_overwriting(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "existing-run"
            output.mkdir()
            sentinel = output / "review.txt"
            sentinel.write_text("Existing reviewer evidence must survive.", encoding="utf-8")
            before = files(output)
            result = subprocess.run(
                [sys.executable, "-B", str(PREPARE), CASES[0]["id"], "--output", str(output)],
                capture_output=True, text=True, encoding="utf-8", timeout=30,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("Output already exists", result.stderr)
            self.assertEqual(files(output), before)


if __name__ == "__main__":
    unittest.main()
