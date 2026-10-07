"""Recorded outcomes must be coherent, not necessarily successful."""
from copy import deepcopy
from contextlib import redirect_stdout
import io
import itertools
import json
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
VERDICTS = ("pass", "partial", "fail", "not-testable")


def report(all_cases=False):
    return {
        "skillVersion": MANIFEST["version"], "host": "test", "model": "synthetic",
        "date": "2026-10-07", "cases": [
            {"id": case["id"], "triggerMode": "explicit", "result": "pass",
             "invariants": [{"text": text, "result": "pass"} for text in case["invariants"]]}
            for case in (MANIFEST["cases"] if all_cases else MANIFEST["cases"][:1])
        ],
    }


class EvalResultTests(unittest.TestCase):
    def cli(self, value, *args):
        with tempfile.TemporaryDirectory(prefix="uiux-eval-verdict-") as temp:
            path = Path(temp) / "result.json"
            path.write_text(json.dumps(value), encoding="utf-8")
            return subprocess.run(
                [sys.executable, "-B", str(ROOT / "scripts/validate_eval_result.py"), str(path), *args],
                capture_output=True, text=True, encoding="utf-8", check=False,
            )

    def errors(self, value, **kwargs):
        from validate_eval_result import validate_result
        return validate_result(value, **kwargs)

    def test_full_manifest_false_clean_regression(self):
        value = report(all_cases=True)
        value["cases"][0]["invariants"][0]["result"] = "fail"
        result = self.cli(value, "--require-all")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("inconsistent", result.stdout)
        self.assertNotIn("structurally valid", result.stdout)

    def test_verdict_matrix(self):
        # Two distinct required criteria suffice for every pair of outcome classes.
        manifest = {"version": "test", "cases": [{"id": "case", "invariants": ["a", "b"]}]}
        for overall, first, second in itertools.product(VERDICTS, repeat=3):
            with self.subTest(overall=overall, first=first, second=second):
                value = report()
                value["skillVersion"] = "test"
                value["cases"] = [{"id": "case", "triggerMode": "implicit", "result": overall,
                                   "invariants": [{"text": "a", "result": first}, {"text": "b", "result": second}]}]
                outcomes = {first, second}
                accepted = (
                    (overall == "pass" and outcomes == {"pass"})
                    or (overall == "fail" and "fail" in outcomes)
                    or (overall == "not-testable" and outcomes == {"not-testable"})
                    or (overall == "partial" and "fail" not in outcomes
                        and outcomes not in ({"pass"}, {"not-testable"}))
                )
                self.assertEqual(not self.errors(value, manifest=manifest), accepted)

    def test_conservative_fail_and_partial_need_reason(self):
        for verdict in ("fail", "partial"):
            value = report()
            value["cases"][0]["result"] = verdict
            self.assertTrue(self.errors(value))
            value["cases"][0]["notes"] = "Additional observed case-level limitation."
            self.assertEqual(self.errors(value), [])

    def test_notes_cannot_excuse_contradictions(self):
        for overall, outcome in (("pass", "partial"), ("pass", "not-testable"),
                                 ("partial", "fail"), ("not-testable", "pass"),
                                 ("partial", "not-testable")):
            value = report()
            value["cases"][0].update(result=overall, notes="An explanation is not a waiver.")
            for invariant in value["cases"][0]["invariants"]:
                invariant["result"] = outcome
            self.assertTrue(self.errors(value))

    def test_missing_duplicate_unknown_cases_and_invariants(self):
        base = report()
        variants = []
        value = deepcopy(base)
        value["cases"].append(deepcopy(value["cases"][0]))
        variants.append((value, "Duplicate result case"))
        value = deepcopy(base)
        value["cases"][0]["id"] = "unknown-case"
        variants.append((value, "Unknown case id"))
        value = deepcopy(base)
        value["cases"][0]["invariants"].pop()
        variants.append((value, "missing invariant"))
        for verdict in ("pass", "fail"):
            value = deepcopy(base)
            duplicate = deepcopy(value["cases"][0]["invariants"][0])
            duplicate["result"] = verdict
            value["cases"][0]["invariants"].append(duplicate)
            variants.append((value, "duplicate invariant"))
        value = deepcopy(base)
        value["cases"][0]["invariants"].append({"text": "invented", "result": "pass"})
        variants.append((value, "unknown invariant"))
        for value, diagnostic in variants:
            with self.subTest(diagnostic=diagnostic):
                self.assertTrue(any(diagnostic in error for error in self.errors(value)))

    def test_completeness_is_opt_in(self):
        self.assertEqual(self.errors(report()), [])
        self.assertTrue(any("Missing case results" in e for e in self.errors(report(), require_all=True)))
        self.assertEqual(self.errors(report(all_cases=True), require_all=True), [])
        result = self.cli(report(all_cases=True), "--require-all")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn(f"Cases={len(MANIFEST['cases'])}/{len(MANIFEST['cases'])}", result.stdout)

    def test_valid_failure_is_recordable_and_all_counts_visible(self):
        value = report(all_cases=True)
        value["cases"] = value["cases"][:4]
        for case, verdict in zip(value["cases"], VERDICTS):
            case["result"] = verdict
            for invariant in case["invariants"]:
                invariant["result"] = verdict
        result = self.cli(value)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        for label in ("Pass=1", "Partial=1", "Fail=1", "Not-testable=1"):
            self.assertIn(label, result.stdout)
        self.assertIn("not acceptance", result.stdout)

    def test_malformed_shapes_and_enums_are_diagnostics(self):
        for value in (None, [], "report", {}, {**report(), "cases": {}}, {**report(), "cases": []},
                      {**report(), "cases": [None]}, {**report(), "host": []}):
            with self.subTest(value=value):
                self.assertTrue(self.errors(value))
        for field, bad in (("id", []), ("triggerMode", {}), ("result", []),
                           ("invariants", None), ("invariants", [None]),
                           ("invariants", [{"text": [], "result": "pass"}]),
                           ("invariants", [{"text": "x", "result": {}}]),
                           ("notes", []), ("evidence", "not an array")):
            value = report()
            value["cases"][0][field] = bad
            with self.subTest(field=field, bad=bad):
                self.assertTrue(self.errors(value))

    def test_required_fields_and_optional_evidence_types(self):
        for field in ("skillVersion", "host", "model", "date", "cases"):
            value = report()
            del value[field]
            self.assertTrue(self.errors(value), field)
        for field in ("id", "triggerMode", "result", "invariants"):
            value = report()
            del value["cases"][0][field]
            self.assertTrue(self.errors(value), field)
        for field in ("text", "result"):
            value = report()
            del value["cases"][0]["invariants"][0][field]
            self.assertTrue(self.errors(value), field)
        for field in ("host", "model", "date"):
            value = report()
            value[field] = " \n\t"
            self.assertTrue(self.errors(value), field)
        value = report()
        value["cases"][0]["invariants"][0]["evidence"] = []
        self.assertTrue(self.errors(value))

    def test_validating_does_not_mutate_records(self):
        for all_cases in (False, True):
            value = report(all_cases)
            before = deepcopy(value)
            self.errors(value, require_all=True)
            self.assertEqual(value, before)

    def test_real_world_gate_reuses_consistency_and_remains_stricter(self):
        path = ROOT / "evals/real-world/result.json"
        original_read = Path.read_text
        original = json.loads(original_read(path, encoding="utf-8"))
        for variant in ("contradiction", "duplicate-case", "duplicate-invariant", "duplicate-json", "valid-failure"):
            value = deepcopy(original)
            case = value["cases"][0]
            if variant == "contradiction":
                case["invariants"][0]["result"] = "partial"
            elif variant == "duplicate-case":
                value["cases"].append(deepcopy(case))
            elif variant == "duplicate-invariant":
                case["invariants"].append(deepcopy(case["invariants"][0]))
            elif variant == "valid-failure":
                case["result"] = case["invariants"][0]["result"] = "fail"
                self.assertEqual(self.errors(value), [])

            raw = json.dumps(value)
            if variant == "duplicate-json":
                raw = raw[:-1] + ', "cases": []}'

            def read(candidate, *args, **kwargs):
                return raw if candidate == path else original_read(candidate, *args, **kwargs)

            with self.subTest(variant=variant), patch.object(Path, "read_text", read):
                with redirect_stdout(io.StringIO()) as output, self.assertRaises(SystemExit) as exit_result:
                    runpy.run_path(str(ROOT / "scripts/validate_real_world_evaluation.py"), run_name="__main__")
                self.assertEqual(exit_result.exception.code, 1)
                self.assertIn("validation failed", output.getvalue())
    def test_read_parse_and_duplicate_key_errors(self):
        with tempfile.TemporaryDirectory(prefix="uiux-eval-invalid-") as temp:
            path = Path(temp) / "result.json"
            for raw in (None, b"{", b"\xff", b'{"cases":[],"cases":[]}'):
                if raw is not None:
                    path.write_bytes(raw)
                result = subprocess.run([sys.executable, "-B", str(ROOT / "scripts/validate_eval_result.py"), str(path)],
                                        capture_output=True, text=True, encoding="utf-8", check=False)
                self.assertEqual(result.returncode, 1)
                self.assertNotIn("Traceback", result.stderr)
                self.assertIn("validation failed", result.stdout)

    def test_unchanged_historical_subset(self):
        path = ROOT / "evals/real-world/result.json"
        before = path.read_bytes()
        value = json.loads(before)
        self.assertEqual(self.errors(value), [])
        self.assertTrue(self.errors(value, require_all=True))
        self.assertEqual(self.cli(value).returncode, 0)
        self.assertEqual(path.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
