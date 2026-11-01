"""Integrity of actually reviewed R13 responses; does not execute or grade models."""
import copy
import json
import re
import unittest
from test_r12_behavior import HERE, ROOT, CRITERIA, errors
from behavior_evaluation import canonical, snapshot
from r13_release_binding import r13_release_predecessor


def prompts():
    result = {}
    for name in ("R12_CASES.md", "R13_CASES.md"):
        for match in re.finditer(r"^## ([BOT]\d{2})[^\n]*\n(.*?)(?=^## |\Z)", (HERE / name).read_text(encoding="utf-8"), re.M | re.S):
            result[match[1]] = match[2].strip() + "\n"
    return result


class R13Behavior(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.stage = json.loads((ROOT / "evals/r13-source.json").read_text())["stage"].replace("R13.", "stage")
        cls.report = json.loads((HERE / f"r13-{cls.stage}-behavior.json").read_text(encoding="utf-8"))
        cls.criteria = {**CRITERIA, "O01": {"operational-reachability", "bounded-adoption"}}
        if cls.stage == "stage4":
            cls.criteria.update({"T01": {"light-only-transition", "parent-provenance"},
                                 "T02": {"required-dark-gate", "preserved-authorization"},
                                 "T03": {"primary-dark-reuse", "secondary-not-approval"}})
        cls.prompts = prompts()
        cls.outputs = {name: canonical(HERE / "r13-outputs" / cls.stage / (name + ".md")) for name in cls.criteria}
        cls.files = snapshot(ROOT / "skills/ui-ux-skill")
        cls.files = r13_release_predecessor(cls.files, result=cls.report,
                    record="evals/wordpress-settings/r13-stage4-behavior.json")

    def check(self, report, files=None):
        return errors(report, files or self.files, self.prompts, self.outputs,
                      criteria=self.criteria, output_prefix="r13-outputs/" + self.stage)

    def test_actual_responses_bind_current_source(self):
        self.assertEqual(self.check(self.report), [])
        operation = next(row for row in self.report["cases"] if row["id"] == "O01")
        self.assertIn("references/products/wordpress-plugin.md", operation["read_paths"])
        self.assertNotIn("references/products/wordpress/components.md", operation["read_paths"])
        self.assertNotIn("references/products/wordpress/settings.md", operation["read_paths"])

    def test_changed_source_and_unresolved_review_rejected(self):
        self.assertTrue(self.check(self.report, {**self.files, "SKILL.md": "0" * 64}))
        for mutate in (lambda r: r["cases"].pop(),
                       lambda r: r["cases"][0].update(method="source-trace"),
                       lambda r: r["cases"][0].update(output_sha256="0" * 64),
                       lambda r: r["cases"][0]["review"][0].update(status="unresolved"),
                       lambda r: r["cases"][1].update(evaluator=r["cases"][0]["evaluator"])):
            broken = copy.deepcopy(self.report); mutate(broken); self.assertTrue(self.check(broken))


if __name__ == "__main__": unittest.main()
