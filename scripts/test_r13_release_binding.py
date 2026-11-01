"""R13 release compatibility rejects drift; original evaluations stay immutable."""
import copy
import json
import subprocess
import sys
import unittest
from unittest.mock import patch
from pathlib import Path
from behavior_evaluation import ROOT, snapshot, validate_record
from release_version_binding import content_digest, tree_digest
from r13_release_binding import r13_release_predecessor


class R13Release(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = snapshot(ROOT / "skills/ui-ux-skill")
        cls.binding = json.loads((ROOT / "evals/r13-release-version.json").read_text())
        cls.ui = json.loads((ROOT / "evals/ui-foundations/r13-result.json").read_text(encoding="utf-8"))

    def test_exact_candidate_and_both_retained_results(self):
        previous = r13_release_predecessor(self.files)
        from r14_source_binding import r14_predecessor
        released = r14_predecessor(self.files)
        self.assertEqual([p for p in previous if previous[p] != released[p]], ["VERSION"])
        for name in ("evals/ui-foundations/r13-result.json", "evals/wordpress-settings/r13-stage4-behavior.json"):
            result = json.loads((ROOT / name).read_text(encoding="utf-8"))
            before = copy.deepcopy(result)
            self.assertEqual(r13_release_predecessor(self.files, result=result, record=name), previous)
            self.assertEqual(result, before)

    def test_guidance_inventory_and_version_drift_rejected_even_if_rebound(self):
        for files in ({**self.files, "SKILL.md": "0" * 64},
                      {**self.files, "extra.md": "0" * 64},
                      {k: v for k, v in self.files.items() if k != "LICENSE"},
                      {**self.files, "VERSION": "0" * 64}):
            binding = {**self.binding, "candidate_after_sha256": tree_digest(files)}
            with self.assertRaises(ValueError): r13_release_predecessor(files, binding)

    def test_missing_malformed_and_other_scope_rejected(self):
        mutations = [[], {}, {**self.binding, "scope": "arbitrary"},
                     {**self.binding, "decision": "other"}, {**self.binding, "extra": True}]
        for key in self.binding:
            bad = copy.deepcopy(self.binding); bad.pop(key); mutations.append(bad)
        for key in ("path", "previous_sha256", "sha256"):
            bad = copy.deepcopy(self.binding); bad["version_change"][key] = "wrong"; mutations.append(bad)
        for bad in mutations:
            with self.assertRaises(ValueError): r13_release_predecessor(self.files, bad)

    def test_changed_records_or_evaluator_context_rejected(self):
        for name in self.binding["records"]:
            bad = copy.deepcopy(self.binding); bad["records"][name] = "0" * 64
            with self.assertRaises(ValueError): r13_release_predecessor(self.files, bad)
        bad = copy.deepcopy(self.ui); bad["cases"][0]["evaluatorId"] = "relabelled"
        for record, result in (("evals/ui-foundations/r13-result.json", bad), ("other", self.ui)):
            with self.assertRaises(ValueError):
                r13_release_predecessor(self.files, result=result, record=record)

    def test_explicit_ui_acceptance_and_default_rejection(self):
        directory = ROOT / "evals/ui-foundations"
        self.assertTrue(validate_record(self.ui, directory, accept=True))
        self.assertEqual(validate_record(self.ui, directory, accept=True, r13_release_binding=self.binding), [])
        bad = copy.deepcopy(self.ui); bad["cases"][0]["invariants"][0]["result"] = "fail"
        self.assertTrue(validate_record(bad, directory, accept=True, r13_release_binding=self.binding))

    def test_report_and_sidecar_cannot_be_jointly_relabelled(self):
        name = "evals/ui-foundations/r13-result.json"
        changed = copy.deepcopy(self.ui); changed["cases"][0]["evaluatorId"] = "relabelled-context"
        binding = copy.deepcopy(self.binding); binding["records"][name] = content_digest(changed)
        original_read = Path.read_text
        def read(path, *args, **kwargs):
            return json.dumps(changed) if path == ROOT / name else original_read(path, *args, **kwargs)
        with patch.object(Path, "read_text", read):
            with self.assertRaises(ValueError):
                r13_release_predecessor(self.files, binding, result=changed, record=name)
            self.assertTrue(validate_record(changed, ROOT / "evals/ui-foundations", accept=True,
                                            r13_release_binding=binding))

    def test_cli_requires_explicit_correct_bridge(self):
        base = [sys.executable, "-B", str(ROOT / "scripts/validate_eval_result.py"),
                str(ROOT / "evals/ui-foundations/r13-result.json"), "--suite", "ui-foundations", "--accept"]
        for extra, code in (([], 1), (["--r13-release-binding", str(ROOT / "evals/r13-release-version.json")], 0),
                            (["--r13-release-binding", str(ROOT / "evals/r12-release-version.json")], 1)):
            result = subprocess.run(base + extra, cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(result.returncode, code, result.stdout + result.stderr)
            if code == 0: self.assertIn("not a fresh 3.6.1 model evaluation", result.stdout)


if __name__ == "__main__": unittest.main()
