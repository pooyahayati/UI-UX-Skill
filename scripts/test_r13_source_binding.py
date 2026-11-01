"""Exact source succession and immutable R12 acceptance, distinct from R13 reruns."""
import copy
import json
import unittest
from unittest.mock import patch
import behavior_evaluation as behavior
from r13_source_binding import r13_predecessor, retained_r12_version_case

ROOT = behavior.ROOT


class R13Source(unittest.TestCase):
    def test_exact_source_scope_and_parent(self):
        actual = behavior.snapshot(ROOT / "skills/ui-ux-skill")
        binding = json.loads((ROOT / "evals/r13-source.json").read_text())
        released = r13_predecessor(actual, binding)
        self.assertNotEqual(actual, released)
        for changed in ({**actual, "references/accessibility.md": "0" * 64}, {**actual, "new.md": "0" * 64}):
            with self.assertRaises(ValueError): r13_predecessor(changed, binding)
        for key, value in (("parents", {}), ("changes", {}), ("stage", "unbounded"), ("decision", "unrelated")):
            with self.assertRaises(ValueError): r13_predecessor(actual, {**binding, key: value})
        wrong = copy.deepcopy(binding); next(iter(wrong["changes"].values()))["previous_sha256"] = "0" * 64
        with self.assertRaises(ValueError): r13_predecessor(actual, wrong)

    def test_preserved_full_r12_acceptance(self):
        result = json.loads((ROOT / "evals/ui-foundations/r12-result.json").read_text())
        bridge = json.loads((ROOT / "evals/r12-release-version.json").read_text())
        released = r13_predecessor()
        historical = {**behavior.manifest(), "version": "3.6.0"}
        with patch.object(behavior, "snapshot", return_value=released), patch.object(behavior, "manifest", return_value=historical):
            self.assertEqual(behavior.validate_record(result, ROOT / "evals/ui-foundations", accept=True, release_binding=bridge), [])

    def test_retained_version_permission_cannot_relabel_a_run(self):
        old = json.loads((ROOT / "evals/ui-foundations/r12-result.json").read_text())
        result = {**old, "skillVersion": "3.6.0", "retainedR12VersionOnly": {
            "record": "evals/ui-foundations/r12-result.json", "sha256": behavior.digest(behavior.canonical(ROOT / "evals/ui-foundations/r12-result.json"))}}
        case = old["cases"][0]
        self.assertTrue(retained_r12_version_case(result, case))
        self.assertFalse(retained_r12_version_case(result, {**case, "evaluatorId": "different"}))
        self.assertFalse(retained_r12_version_case({**result, "retainedR12VersionOnly": {}}, case))

    def test_stage_three_acceptance_remains_bound_to_its_own_candidate(self):
        result = json.loads((ROOT / "evals/ui-foundations/r13-stage3-result.json").read_text())
        candidate = next(c for c in result["cases"] if c["id"] == "S04")["candidate"]["files"]
        binding = json.loads((ROOT / "evals/r13-stage3-source.json").read_text())
        r13_predecessor(candidate, binding)
        historical = {**behavior.manifest(), "version": "3.6.0"}
        with patch.object(behavior, "snapshot", return_value=candidate), patch.object(behavior, "manifest", return_value=historical):
            self.assertEqual(behavior.validate_record(result, ROOT / "evals/ui-foundations", accept=True), [])


if __name__ == "__main__": unittest.main()
