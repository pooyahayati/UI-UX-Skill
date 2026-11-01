"""Whole-tree successor identity and narrowly retained metadata, not model grading."""
import copy
import json
import unittest
from unittest.mock import patch
from pathlib import Path

from behavior_evaluation import ROOT, snapshot, tree_digest
from r14_source_binding import r14_predecessor, retained_r13_version_case, PARENT


class R14Source(unittest.TestCase):
    def test_exact_parent_scope_and_current_tree(self):
        files = snapshot(ROOT / "skills/ui-ux-skill")
        binding = json.loads((ROOT / "evals/r14-source.json").read_text())
        self.assertEqual(tree_digest(r14_predecessor(files, binding)), PARENT)
        for changed in ({**files, "SKILL.md": "0" * 64}, {**files, "extra.md": "0" * 64},
                        {p: h for p, h in files.items() if p != "LICENSE"}):
            with self.assertRaises(ValueError): r14_predecessor(changed, binding)
        for key, value in (("stage", "unbounded"), ("changes", {}), ("parents", {}),
                           ("decision", "unrelated"), ("candidate_sha256", "0" * 64)):
            with self.assertRaises(ValueError): r14_predecessor(files, {**binding, key: value})
        wrong = copy.deepcopy(binding)
        next(iter(wrong["changes"].values()))["previous_sha256"] = "0" * 64
        with self.assertRaises(ValueError): r14_predecessor(files, wrong)

    def test_parent_report_and_binding_cannot_be_jointly_relabelled(self):
        files = snapshot(ROOT / "skills/ui-ux-skill")
        binding = json.loads((ROOT / "evals/r14-source.json").read_text())
        name = "evals/ui-foundations/r13-result.json"
        original = json.loads((ROOT / name).read_text())
        changed = copy.deepcopy(original); changed["cases"][0]["evaluatorId"] = "relabeled"
        from behavior_evaluation import digest
        body = json.dumps(changed)
        binding["parents"][name] = digest(body.encode())
        read = Path.read_text; read_bytes = Path.read_bytes
        with patch.object(Path, "read_text", lambda p,*a,**k: body if p == ROOT/name else read(p,*a,**k)), \
             patch.object(Path, "read_bytes", lambda p: body.encode() if p == ROOT/name else read_bytes(p)):
            with self.assertRaises(ValueError): r14_predecessor(files, binding)

    def test_retained_row_keeps_its_original_identity(self):
        from behavior_evaluation import canonical, digest
        name = "evals/ui-foundations/r13-result.json"
        report = json.loads((ROOT/name).read_text())
        successor = {"retainedR13VersionOnly": {"record": name, "sha256": digest(canonical(ROOT/name))}}
        row = report["cases"][0]
        self.assertTrue(retained_r13_version_case(successor, row))
        for changed in ({**row, "evaluatorId": "fresh"}, {**row, "outputSha256": "0" * 64}):
            self.assertFalse(retained_r13_version_case(successor, changed))
        self.assertFalse(retained_r13_version_case({"retainedR13VersionOnly": {}}, row))


if __name__ == "__main__": unittest.main()
