"""Exercise rejection/acceptance of release policy and progress inconsistencies."""
from pathlib import Path
import re
import unittest

from roadmap_policy import validate_policy

ROOT = Path(__file__).resolve().parents[1]


class RoadmapPolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.readme = (ROOT / "README.md").read_text(encoding="utf-8")
        cls.current_roadmap = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
        # Stable kickoff fixture: later stage updates must not change these scenarios.
        cls.roadmap = cls.current_roadmap
        for row in re.findall(r"^\| R\d+ \|.*$", cls.roadmap, re.M):
            fields = row.split("|")
            stage = fields[1].strip()
            fields[3] = " In progress " if stage == "R0" else " Not started "
            fields[6] = " Not completed "
            fields[7] = " [R0 execution record](#r0-execution-record) " if stage == "R0" else " Not recorded "
            cls.roadmap = cls.roadmap.replace(row, "|".join(fields))
        cls.roadmap = re.sub(r"^- Implementation:.*$", "- Implementation: **In progress**; **0 of 9 correction stages completed**.", cls.roadmap, flags=re.M)
        cls.roadmap = re.sub(r"^- Active implementation stage:.*$", "- Active implementation stage: **R0**.", cls.roadmap, flags=re.M)
        cls.roadmap = re.sub(r"^- Next implementation stage:.*$", "- Next implementation stage: **R1 — Adaptive discovery**.", cls.roadmap, flags=re.M)
        for row in re.findall(r"^\| R9\.\d+ \|.*$", cls.roadmap, re.M):
            fields = row.split("|")
            fields[3], fields[5] = " Not started ", " Not recorded "
            cls.roadmap = cls.roadmap.replace(row, "|".join(fields))

    def rejected(self, text, expected, readme=None):
        errors = validate_policy(self.readme if readme is None else readme, text)
        self.assertTrue(any(expected in error for error in errors), errors)

    def test_current_policy_passes(self):
        self.assertEqual(validate_policy(self.readme, self.current_roadmap), [])
        self.assertEqual(validate_policy(self.readme, self.roadmap), [])

    def test_exception_cannot_be_removed_or_expanded(self):
        for before, after in (
            ("Authorized for R0–R8 only.", "Authorized for all development."),
            ("- visual approval;", "- payment processing;"),
            ("- safe parametric appearance management.", "- safe parametric appearance management.\n- new Product Types;"),
        ):
            with self.subTest(after=after):
                text = self.roadmap.replace(before, after)
                self.assertTrue(text != self.roadmap, "Scope mutation did not change the fixture")
                self.assertTrue(validate_policy(self.readme, text))

    def test_historical_completion_is_preserved(self):
        text = self.roadmap.replace("**Status:** Completed", "**Status:** Planned", 1)
        self.rejected(text, "must remain Completed")

    def test_readme_cannot_keep_unqualified_legacy_freeze(self):
        text = self.readme.replace("Limited correction exception: R0–R8 only.", "All capabilities frozen.")
        self.rejected(self.roadmap, "README stabilization policy missing", readme=text)

    def test_tracker_rejects_missing_duplicate_and_invalid_stages(self):
        row = next(line for line in self.roadmap.splitlines() if line.startswith("| R1 |"))
        fields = row.split("|")
        fields[3] = " Almost done "
        for text in (
            self.roadmap.replace("| R8 |", "| R9 |", 1),
            self.roadmap.replace("| R8 |", "| R7 |", 1),
            self.roadmap.replace(row, "|".join(fields)),
        ):
            self.assertTrue(text != self.roadmap, "Tracker mutation did not change the fixture")
            self.assertTrue(validate_policy(self.readme, text))

    def test_counter_and_active_stage_must_match_tracker(self):
        for pattern, replacement, expected in (
            (r"\*\*\d+ of 9 correction stages completed\*\*", "**8 of 9 correction stages completed**", "completed count"),
            (r"Active implementation stage: \*\*(?:None|R\d+)\*\*", "Active implementation stage: **R8**", "Active implementation stage"),
        ):
            text = re.sub(pattern, replacement, self.roadmap, count=1)
            self.rejected(text, expected)

    def test_completion_requires_date_and_evidence(self):
        row = next(line for line in self.roadmap.splitlines() if line.startswith("| R1 |"))
        fields = row.split("|")
        fields[3], fields[6], fields[7] = " Completed ", " Not completed ", " Not recorded "
        text = self.roadmap.replace(row, "|".join(fields))
        count = sum("| Completed |" in line for line in text.splitlines() if re.match(r"\| R\d+ \|", line))
        text = re.sub(r"\*\*\d+ of 9 correction stages completed\*\*", f"**{count} of 9 correction stages completed**", text, count=1)
        self.rejected(text, "R1: completion needs a dated evidence link")

    def test_completion_with_date_and_evidence_is_accepted(self):
        row = next(line for line in self.roadmap.splitlines() if line.startswith("| R0 |"))
        fields = row.split("|")
        fields[3], fields[6], fields[7] = " Completed ", " 2026-10-04 ", " [R0 execution record](#r0-execution-record) "
        text = self.roadmap.replace(row, "|".join(fields))
        text = re.sub(r"Active implementation stage: \*\*(?:None|R\d+)\*\*", "Active implementation stage: **None**", text, count=1)
        text = re.sub(r"\*\*\d+ of 9 correction stages completed\*\*", "**1 of 9 correction stages completed**", text, count=1)
        self.assertEqual(validate_policy(self.readme, text), [])

    def test_out_of_order_completion_is_rejected(self):
        row = next(line for line in self.roadmap.splitlines() if line.startswith("| R8 |"))
        fields = row.split("|")
        fields[3], fields[6], fields[7] = " Completed ", " 2026-10-04 ", " [Evidence](#r0-execution-record) "
        text = self.roadmap.replace(row, "|".join(fields))
        self.rejected(text, "R8: prerequisites must be Completed")

    def test_next_stage_must_match_tracker(self):
        text = re.sub(r"Next implementation stage: \*\*R\d+", "Next implementation stage: **R8", self.roadmap, count=1)
        self.rejected(text, "Next implementation stage")

    def test_history_limitations_and_frozen_product_boundary_are_preserved(self):
        self.rejected(self.roadmap.replace("did not independently execute", "independently executed"), "Historical evaluation limitations")
        self.rejected(self.roadmap + "\n## Future Product Types\n", "must not advertise future Product Types")

    def test_r9_exception_is_separate_and_bounded(self):
        for before, after, expected in (
            ("**Separate R9 exception:** Optional Material Design only.",
             "**Separate R9 exception:** All styles and libraries.", "Separate R9 stabilization"),
            ("- optional Material activation and routing;", "- framework migration;", "Separate R9 scope"),
            ("- bounded behavioral/rendered evaluation and candidate readiness.",
             "- bounded behavioral/rendered evaluation and candidate readiness.\n- any capability;", "Separate R9 scope"),
            ("**R9 kickoff:** Authorized local R9.1 implementation on 2026-10-06 after accepted R7/R8.",
             "**R9 kickoff:** Inherited old merge permission.", "Separate R9 stabilization"),
        ):
            self.rejected(self.current_roadmap.replace(before, after), expected)
        self.rejected(self.current_roadmap, "README stabilization policy missing",
                      self.readme.replace("Separate R9 exception: optional Material Design only.", "Unlimited expansion."))

    def test_r9_cannot_start_before_accepted_corrections(self):
        row = next(line for line in self.current_roadmap.splitlines() if line.startswith("| R8 |"))
        fields = row.split("|")
        fields[3] = " Not started "
        self.rejected(self.current_roadmap.replace(row, "|".join(fields)), "accepted R7/R8")

    def test_r9_package_identity_status_order_and_evidence(self):
        row = next(line for line in self.current_roadmap.splitlines() if line.startswith("| R9.1 |"))
        fields = row.split("|")
        fields[3], fields[5] = " Completed ", " [Undated evidence](#r91-execution-record--2026-10-06) "
        for text, expected in (
            (self.current_roadmap.replace("| R9.6 |", "| R9.5 |", 1), "R9 package tracker"),
            (self.current_roadmap.replace(row, "|".join(fields)), "completion needs valid dated"),
        ):
            self.rejected(text, expected)
        row = next(line for line in self.current_roadmap.splitlines() if line.startswith("| R9.6 |"))
        fields = row.split("|")
        fields[3], fields[5] = " In progress ", " [Execution](#record) "
        self.rejected(self.current_roadmap.replace(row, "|".join(fields)), "prerequisite packages")

    def test_r9_overall_cannot_complete_early(self):
        row = next(line for line in self.current_roadmap.splitlines() if line.startswith("| R9 |"))
        fields = row.split("|")
        fields[3], fields[6] = " Completed ", " 2026-10-06 "
        self.rejected(self.current_roadmap.replace(row, "|".join(fields)), "R9 overall status")

    def test_dated_first_package_acceptance_does_not_complete_extension(self):
        row = next(line for line in self.current_roadmap.splitlines() if line.startswith("| R9.1 |"))
        fields = row.split("|")
        fields[3] = " Completed "
        fields[5] = " [2026-10-06 scoped acceptance](#record) "
        self.assertEqual(validate_policy(self.readme,
                                        self.current_roadmap.replace(row, "|".join(fields))), [])

    def test_r9_invalid_status_and_parallel_active_packages_are_rejected(self):
        row = next(line for line in self.current_roadmap.splitlines() if line.startswith("| R9.1 |"))
        fields = row.split("|")
        fields[3] = " Almost done "
        self.rejected(self.current_roadmap.replace(row, "|".join(fields)), "invalid package status")
        # Both-active scenario is invalid independently of prerequisite failures.
        first_fields = row.split("|")
        first_fields[3] = " In progress "
        first = self.current_roadmap.replace(row, "|".join(first_fields))
        second = next(line for line in first.splitlines() if line.startswith("| R9.2 |"))
        second_fields = second.split("|")
        second_fields[3], second_fields[5] = " In progress ", " [Execution](#record) "
        self.rejected(first.replace(second, "|".join(second_fields)), "at most one active")


if __name__ == "__main__":
    unittest.main()
