"""Integrity of reviewed raw R12 outputs; does not run or grade an evaluator."""
from pathlib import Path
import copy
import json
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "scripts"))
from behavior_evaluation import canonical, digest, snapshot, tree_digest
from release_version_binding import release_predecessor

CRITERIA = {
    "B01": {"short-form-restraint", "native-preserve"},
    "B02": {"task-discovery", "hybrid-drafts"},
    "B03": {"audit-boundary", "library-boundary"},
    "B04": {"version-fit", "data-fit"},
    "B05": {"primary-foundations", "approval-evidence"},
}


def errors(report, files, prompts, outputs, *, release_binding=None, current_version=None):
    failures = []
    if release_binding is not None:
        try:
            files = release_predecessor(report, files, release_binding,
                                        record="evals/wordpress-settings/r12-behavior-results.json",
                                        current_version=current_version)
        except ValueError as error:
            return [str(error)]
    if (report.get("schema_version") != 1 or report.get("recorded_on") != "2026-11-01"
            or report.get("candidate") != {"sha256": tree_digest(files), "files": files}):
        failures.append("Candidate or execution identity mismatch")
    rows = report.get("cases", [])
    if (not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows)
            or len(rows) != len(CRITERIA) or {row.get("id") for row in rows} != set(CRITERIA)):
        return failures + ["Case inventory mismatch"]
    evaluators = set()
    for row in rows:
        ident = row["id"]
        reads = row.get("read_paths", [])
        reviews = row.get("review", [])
        if (row.get("method") != "independent-model-response" or row.get("status") != "passed"
                or not isinstance(row.get("evaluator"), str) or not row["evaluator"].strip()
                or row["evaluator"] in evaluators):
            failures.append(ident + ": unresolved or non-independent observation")
        evaluators.add(row.get("evaluator"))
        if row.get("input_sha256") != digest(prompts[ident].encode()):
            failures.append(ident + ": changed raw input")
        if (row.get("output") != f"r12-outputs/{ident}.md" or not outputs[ident].strip()
                or row.get("output_sha256") != digest(outputs[ident])):
            failures.append(ident + ": missing or changed actual output")
        if (not isinstance(reads, list) or not reads or len(reads) != len(set(reads))
                or not all(isinstance(p, str) and p in files for p in reads)):
            failures.append(ident + ": invalid consumed resources")
        if (not isinstance(reviews, list) or any(not isinstance(r, dict) for r in reviews)
                or len(reviews) != len(CRITERIA[ident])
                or {r.get("id") for r in reviews} != CRITERIA[ident]
                or any(r.get("status") != "passed" or not isinstance(r.get("evidence"), str)
                       or not r["evidence"].strip() for r in reviews)):
            failures.append(ident + ": missing or unresolved reviewed criteria")
    return failures


class R12Behavior(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = json.loads((HERE / "r12-behavior-results.json").read_text(encoding="utf-8"))
        cls.files = snapshot(ROOT / "skills/ui-ux-skill")
        cls.release_binding = json.loads((ROOT / "evals/r12-release-version.json").read_text(encoding="utf-8"))
        cls.current_version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        cls.prompts = {m[1]: m[2].strip() + "\n" for m in re.finditer(
            r"^## (B\d{2})[^\n]*\n(.*?)(?=^## |\Z)",
            (HERE / "R12_CASES.md").read_text(encoding="utf-8"), re.M | re.S)}
        cls.outputs = {ident: canonical(HERE / "r12-outputs" / (ident + ".md")) for ident in CRITERIA}

    def check(self, report, files=None, prompts=None, outputs=None):
        return errors(report, files or self.files, prompts or self.prompts, outputs or self.outputs,
                      release_binding=self.release_binding, current_version=self.current_version)

    def test_retained_actual_responses(self):
        self.assertEqual(self.check(self.report), [])
        self.assertEqual(errors(self.report, self.report["candidate"]["files"], self.prompts, self.outputs), [])

    def test_release_bridge_is_explicit_and_preserves_recorded_candidate(self):
        before = copy.deepcopy(self.report)
        self.assertTrue(errors(self.report, self.files, self.prompts, self.outputs))
        self.assertEqual(self.check(self.report), [])
        self.assertEqual(self.report, before)
        self.assertNotEqual(self.report["candidate"]["files"]["VERSION"], self.files["VERSION"])

    def test_final_independent_task_evidence(self):
        record = json.loads((HERE / "r12-task-result.json").read_text(encoding="utf-8"))
        runtime = json.loads((HERE / "evidence/r12-browser-results.json").read_text(encoding="utf-8"))
        self.assertEqual(record["method"], "independent-rendered-ui-task")
        self.assertEqual(record["raw_input_sha256"], digest(canonical(HERE / "R12_TASK.md")))
        self.assertEqual(record["fixture_hashes"], runtime["fixture_hashes"])
        self.assertEqual(record["behavior_hashes"], runtime["behavior_hashes"])
        self.assertEqual(record["facilitator_hints"], 0)
        self.assertEqual(record["evaluator"], "/root/r12_final_tasks")
        self.assertTrue({"r12-task/trace.json", "r12-task/report.md"}.issubset(record["artifacts"]))
        for name, expected in record["artifacts"].items():
            self.assertRegex(name, r"^r12-task/(?:report\.md|trace\.json|[0-9]{2}-[a-z-]+\.png)$")
            self.assertEqual(expected, digest(canonical(HERE / name)))
        outcomes = record["outcomes"]
        self.assertEqual(len(outcomes), 5)
        self.assertEqual({row["id"] for row in outcomes}, {"alias-discovery", "error-recovery", "draft-retention", "section-save", "reload-verification"})
        for row in outcomes:
            self.assertEqual(row["status"], "passed")
            self.assertTrue(row["evidence"].strip())

    def test_candidate_input_and_output_drift(self):
        changed = {**self.files, "SKILL.md": "0" * 64}
        self.assertTrue(self.check(self.report, files=changed))
        self.assertTrue(self.check(self.report, prompts={**self.prompts, "B01": "Changed request"}))
        for text in (b"", b"Fabricated replacement"):
            self.assertTrue(self.check(self.report, outputs={**self.outputs, "B01": text}))

    def test_inventory_and_independence(self):
        for mutate in (lambda r: r["cases"].pop(),
                       lambda r: r["cases"].append(copy.deepcopy(r["cases"][0])),
                       lambda r: r["cases"][1].update(evaluator=r["cases"][0]["evaluator"])):
            bad = copy.deepcopy(self.report); mutate(bad)
            # Exercise the original review contract as well as the release
            # record digest, so the metadata bridge cannot mask regressions.
            self.assertTrue(errors(bad, self.report["candidate"]["files"], self.prompts, self.outputs))
            self.assertTrue(self.check(bad))

    def test_unresolved_or_missing_review(self):
        for mutate in (lambda r: r.update(status="failed"), lambda r: r.update(review=[]),
                       lambda r: r["review"][0].update(status="fail"),
                       lambda r: r["review"][0].update(evidence=" "),
                       lambda r: r.update(output="../escaped.md"),
                       lambda r: r.update(read_paths=["missing.md"])):
            bad = copy.deepcopy(self.report); mutate(bad["cases"][0])
            self.assertTrue(errors(bad, self.report["candidate"]["files"], self.prompts, self.outputs))
            self.assertTrue(self.check(bad))


if __name__ == "__main__":
    unittest.main()
