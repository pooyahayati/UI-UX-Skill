"""Synthetic validator tests, never substitutes for the retained model outputs."""
from copy import deepcopy
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from behavior_evaluation import (ROOT, SUITE, COMMON_PATHS, canonical, digest, manifest,
                                 prepare, preparation_errors, run_bytes, run_record,
                                 snapshot, tree_digest, validate_record)


class BehaviorEvaluationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="uiux-behavior-unit-")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / "source"
        for relative in ("skills/ui-ux-skill", "evals/ui-foundations", "evals/shadcn", "evals/motion"):
            shutil.copytree(ROOT / relative, self.root / relative)
        shutil.copyfile(ROOT / "VERSION", self.root / "VERSION")
        self.record_dir = self.base / "record"
        (self.record_dir / "outputs").mkdir(parents=True)
        self.manifest = manifest(self.root)
        files = snapshot(self.root / "skills/ui-ux-skill")
        self.result = {"skillVersion": self.manifest["version"], "host": "unit-test",
                       "model": "synthetic-not-model-evidence", "date": "2026-10-16",
                       "suite": SUITE, "candidate": {"files": files, "sha256": tree_digest(files)},
                       "unexecuted": self.manifest["unexecuted"], "cases": []}
        for case in self.manifest["cases"]:
            output = b"Synthetic unit-test output. Not evaluation evidence.\n"
            (self.record_dir / "outputs" / (case["id"] + ".md")).write_bytes(output)
            self.result["cases"].append({
                "id": case["id"], "triggerMode": "explicit", "result": "pass",
                "inputSha256": digest(case["prompt"].encode()),
                "preparationSha256": digest(run_bytes(run_record(case, files))),
                "outputSha256": digest(output), "sourcePaths": sorted(COMMON_PATHS),
                "evaluatorId": "unit-only-" + case["id"], "evidence": ["synthetic"],
                "invariants": [{"text": text, "result": "pass", "evidence": "synthetic"}
                               for text in case["invariants"]]})

    def errors(self, result=None, **kwargs):
        return validate_record(self.result if result is None else result, self.record_dir, root=self.root, **kwargs)

    def test_inventory_and_recorded_acceptance_are_bounded(self):
        self.assertEqual(len(self.manifest["cases"]), 13)
        self.assertEqual(sum(len(c["invariants"]) for c in self.manifest["cases"]), 27)
        self.assertEqual(len(self.manifest["unexecuted"]), 5)
        self.assertEqual(self.errors(accept=True), [])

    def test_preparation_has_only_raw_prompt_and_exact_candidate(self):
        output = prepare("S01", self.base / "run", self.root)
        self.assertEqual(preparation_errors(output, self.root), [])
        self.assertEqual(canonical(output / "evaluator/PROMPT.txt"), self.manifest["cases"][0]["prompt"].encode())
        self.assertFalse((output / "evaluator/RUN.json").exists())
        self.assertFalse((output / "evaluator/manifest.json").exists())
        before = (output / "RUN.json").read_bytes()
        with self.assertRaises(ValueError):
            prepare("S01", output, self.root)
        self.assertEqual((output / "RUN.json").read_bytes(), before)

    def test_preparation_rejects_answer_leakage_and_stale_inputs(self):
        for index, path in enumerate(("evaluator/ANSWERS.md", "evaluator/PROMPT.txt", "evaluator/skill/SKILL.md", "RUN.json")):
            output = prepare("S01", self.base / ("run" + str(index)), self.root)
            with (output / path).open("ab") as stream:
                stream.write(b"\nreviewer answer key / changed input\n")
            self.assertTrue(preparation_errors(output, self.root), path)

    def test_rejects_unknown_case_and_output_inside_source(self):
        for case_id, target in (("S03", self.base / "run"), ("S01", self.root / "skills/unsafe")):
            with self.assertRaises(ValueError):
                prepare(case_id, target, self.root)
            self.assertFalse(target.exists())

    def test_preparation_rejects_duplicate_reviewer_fields(self):
        output = prepare("S01", self.base / "run", self.root)
        path = output / "RUN.json"
        path.write_text(path.read_text(encoding="utf-8").rstrip()[:-1] + ', "caseId": "S01"}', encoding="utf-8")
        self.assertTrue(preparation_errors(output, self.root))

    def test_missing_changed_or_empty_actual_output_rejected(self):
        output = self.record_dir / "outputs/S01.md"
        output.unlink()
        self.assertTrue(self.errors(accept=True))
        for content in (b"", b"altered"):
            output.write_bytes(content)
            self.assertTrue(self.errors(accept=True))

    def test_case_identity_and_evidence_fields_required(self):
        for key in ("inputSha256", "preparationSha256", "outputSha256", "sourcePaths", "evaluatorId", "evidence"):
            value = deepcopy(self.result)
            del value["cases"][0][key]
            self.assertTrue(self.errors(value, accept=True), key)
        value = deepcopy(self.result)
        value["cases"][0]["invariants"][0]["evidence"] = " "
        self.assertTrue(self.errors(value))

    def test_duplicate_contradictory_and_incomplete_records_rejected(self):
        value = deepcopy(self.result)
        value["cases"].append(deepcopy(value["cases"][0]))
        self.assertTrue(self.errors(value))
        value = deepcopy(self.result)
        value["cases"][0]["invariants"][0]["result"] = "fail"
        self.assertTrue(self.errors(value))
        value = deepcopy(self.result)
        value["cases"].pop()
        self.assertEqual(self.errors(value), [])
        self.assertTrue(self.errors(value, accept=True))

    def test_coherent_failure_is_recordable_but_not_accepted(self):
        self.result["cases"][0]["result"] = "fail"
        self.result["cases"][0]["invariants"][0]["result"] = "fail"
        self.assertEqual(self.errors(), [])
        self.assertTrue(self.errors(accept=True))

    def test_one_fresh_evaluator_context_per_case(self):
        self.result["cases"][1]["evaluatorId"] = self.result["cases"][0]["evaluatorId"]
        self.assertTrue(any("reused evaluator context" in error for error in self.errors()))

    def test_bad_candidate_identity_and_coverage_rejected(self):
        for candidate in (None, [], {}, {"files": [], "sha256": "bad"}, {**self.result["candidate"], "sha256": "bad"}):
            value = deepcopy(self.result)
            value["candidate"] = candidate
            self.assertTrue(self.errors(value))
        value = deepcopy(self.result)
        value["unexecuted"] = {}
        self.assertTrue(self.errors(value))

    def test_stale_raw_and_rubric_rejected(self):
        raw = self.root / "evals/shadcn/CASES.md"
        raw.write_text(raw.read_text(encoding="utf-8").replace("## S01", "## S01 altered heading\nchanged input", 1), encoding="utf-8")
        self.assertTrue(any("stale raw input" in e for e in self.errors()))
        path = self.root / "evals/ui-foundations/manifest.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["cases"][0]["invariants"][0] += " revised"
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertTrue(any("preparation/rubric" in e for e in self.errors()))

    def test_dependency_mapping_invalidates_affected_case_only(self):
        name = "references/interactive-motion.md"
        self.assertIn(name, self.result["candidate"]["files"])
        self.result["cases"][0]["sourcePaths"].append(name)
        with (self.root / "skills/ui-ux-skill" / name).open("ab") as stream:
            stream.write(b"\nchanged relevant guidance\n")
        errors = self.errors(accept=True)
        self.assertEqual(errors, ["S01: stale/missing consumed source " + name])
        with (self.root / "skills/ui-ux-skill/SKILL.md").open("ab") as stream:
            stream.write(b"\nshared guidance changed\n")
        self.assertEqual(sum("SKILL.md" in e for e in self.errors()), 13)

    def test_malformed_dependency_sets_rejected(self):
        for paths in (None, [], [None], sorted(COMMON_PATHS) + ["SKILL.md"], sorted(COMMON_PATHS) + ["../outside"]):
            value = deepcopy(self.result)
            value["cases"][0]["sourcePaths"] = paths
            self.assertTrue(self.errors(value), paths)

    def test_malformed_case_identity_and_blank_evidence_rejected(self):
        for field, item in (("id", []), ("id", {}), ("evidence", [" "]), ("evidence", [])):
            value = deepcopy(self.result)
            value["cases"][0][field] = item
            self.assertTrue(self.errors(value))


if __name__ == "__main__":
    unittest.main()
