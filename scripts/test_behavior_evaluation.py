"""Synthetic validator tests, never substitutes for the retained model outputs."""
from copy import deepcopy
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

from behavior_evaluation import (ROOT, SUITE, COMMON_PATHS, canonical, digest, manifest,
                                 prepare, preparation_errors, run_bytes, run_record,
                                 snapshot, tree_digest, validate_record)
from release_version_binding import (content_digest, release_predecessor, version_digest)


UI_RECORD = "evals/ui-foundations/r12-result.json"
WPS_RECORD = "evals/wordpress-settings/r12-behavior-results.json"


def release_binding_for(ui, wps, previous):
    """Synthetic release transition only; never writes model evidence."""
    return {
        "schema_version": 1, "normalization": "git-lf", "scope": "r12-release-version-only",
        "decision": "docs/releases/3.6.0.md#authority", "recorded_version": "3.5.1",
        "release_version": "3.6.0", "version_change": {
            "path": "VERSION", "previous_sha256": version_digest("3.5.1"),
            "sha256": version_digest("3.6.0")},
        "candidate_before_sha256": tree_digest(previous),
        "candidate_after_sha256": tree_digest({**previous, "VERSION": version_digest("3.6.0")}),
        "records": {UI_RECORD: content_digest(ui), WPS_RECORD: content_digest(wps)},
        "notes": "Synthetic metadata-only compatibility, not execution evidence.",
    }


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

    def refreshed_case(self):
        """Synthetic partial rerun; preserve the old snapshot and actual output."""
        name = "references/products/wordpress/settings.md"
        old = next(case for case in self.result["cases"] if case["id"] == "S04")
        old["sourcePaths"].append(name)
        with (self.root / "skills/ui-ux-skill" / name).open("ab") as stream:
            stream.write(b"\nChanged settings guidance for a synthetic unit test.\n")
        value = deepcopy(self.result)
        fresh = next(case for case in value["cases"] if case["id"] == "S04")
        files = snapshot(self.root / "skills/ui-ux-skill")
        fresh["candidate"] = {"files": files, "sha256": tree_digest(files)}
        preparation = prepare("S04", self.base / "fresh-S04", self.root)
        fresh["preparationSha256"] = digest(canonical(preparation / "RUN.json"))
        fresh["outputFile"] = "S04-r12.md"
        output = b"Fresh synthetic output for validator tests, not model evidence.\n"
        (self.record_dir / "outputs" / fresh["outputFile"]).write_bytes(output)
        fresh["outputSha256"] = digest(output)
        fresh["evaluatorId"] = "fresh-unit-only-S04"
        return value, fresh

    def test_partial_rerun_preserves_unchanged_cases_and_historical_candidate(self):
        value, fresh = self.refreshed_case()
        self.assertEqual(self.errors(value, accept=True), [])
        self.assertEqual(value["candidate"], self.result["candidate"])
        self.assertEqual([c for c in value["cases"] if c["id"] != "S04"],
                         [c for c in self.result["cases"] if c["id"] != "S04"])
        self.assertTrue((self.record_dir / "outputs/S04.md").is_file())
        self.assertNotEqual(fresh["candidate"], value["candidate"])
        self.assertEqual(self.errors(accept=True),
                         ["S04: stale/missing consumed source references/products/wordpress/settings.md"])

    def test_override_requires_full_valid_snapshot_and_new_output_name(self):
        value, fresh = self.refreshed_case()
        for candidate in (None, [], {}, {"files": [], "sha256": "bad"},
                          {**fresh["candidate"], "sha256": "0" * 64}):
            changed = deepcopy(value)
            next(c for c in changed["cases"] if c["id"] == "S04")["candidate"] = candidate
            self.assertTrue(any("candidate override" in e for e in self.errors(changed)), candidate)
        changed = deepcopy(value)
        override = next(c for c in changed["cases"] if c["id"] == "S04")["candidate"]
        override["files"].pop("LICENSE")
        override["sha256"] = tree_digest(override["files"])
        self.assertTrue(any("changed resource inventory" in e for e in self.errors(changed)))
        for field in ("candidate", "outputFile"):
            changed = deepcopy(value)
            next(c for c in changed["cases"] if c["id"] == "S04").pop(field)
            self.assertTrue(any("must be paired" in e for e in self.errors(changed)), field)

    def test_override_preparation_and_consumed_sources_are_independently_bound(self):
        value, fresh = self.refreshed_case()
        fresh["preparationSha256"] = next(c for c in self.result["cases"] if c["id"] == "S04")["preparationSha256"]
        self.assertTrue(any("S04: stale preparation/rubric" in e for e in self.errors(value)))
        # Even a coherent preparation cannot make a stale consumed source current.
        fresh["candidate"] = deepcopy(self.result["candidate"])
        self.assertTrue(any("S04: stale/missing consumed source" in e for e in self.errors(value)))
        with (self.root / "skills/ui-ux-skill/SKILL.md").open("ab") as stream:
            stream.write(b"\nChanged shared guidance invalidates all consumers.\n")
        self.assertEqual(sum("stale/missing consumed source SKILL.md" in e for e in self.errors(value)), 13)

    def test_output_override_rejects_paths_wrong_case_and_historical_filename(self):
        value, fresh = self.refreshed_case()
        for filename in (None, [], "", "S04.md", "S01-r12.md", "../S04-r12.md",
                         "subdir/S04-r12.md", r"..\S04-r12.md", "C:/S04-r12.md", "/S04-r12.md"):
            fresh["outputFile"] = filename
            self.assertTrue(any("invalid or escaping outputFile" in e for e in self.errors(value)), filename)

    def test_fresh_output_is_required_and_content_bound(self):
        value, fresh = self.refreshed_case()
        output = self.record_dir / "outputs" / fresh["outputFile"]
        output.unlink()
        self.assertTrue(any("S04: missing actual output" in e for e in self.errors(value)))
        for content in (b"", b"Changed fresh output"):
            output.write_bytes(content)
            self.assertTrue(any("S04: missing/changed actual output" in e for e in self.errors(value)))

    def test_resolved_output_escape_is_rejected(self):
        value, fresh = self.refreshed_case()
        output = self.record_dir / "outputs" / fresh["outputFile"]
        outside = self.base / "outside-output.md"
        outside.write_bytes(output.read_bytes())
        # Exercise the resolved containment boundary independently of whether
        # the host permits creating symlinks (Windows may require privileges).
        resolve = Path.resolve
        def redirected(path, *args, **kwargs):
            return outside if path == output else resolve(path, *args, **kwargs)
        with patch.object(Path, "resolve", redirected):
            self.assertTrue(any("invalid or escaping outputFile" in e for e in self.errors(value)))

    def released_case(self):
        for path in (self.root / "VERSION", self.root / "skills/ui-ux-skill/VERSION"):
            path.write_text("3.5.1\n", encoding="utf-8")
        self.manifest = manifest(self.root)
        files = snapshot(self.root / "skills/ui-ux-skill")
        self.result["skillVersion"] = "3.5.1"
        self.result["candidate"] = {"files": files, "sha256": tree_digest(files)}
        for row, case in zip(self.result["cases"], self.manifest["cases"]):
            row["preparationSha256"] = digest(run_bytes(run_record(case, files)))
        result, fresh = self.refreshed_case()
        binding = release_binding_for(result, {"candidate": fresh["candidate"]}, fresh["candidate"]["files"])
        for path in (self.root / "VERSION", self.root / "skills/ui-ux-skill/VERSION"):
            path.write_text("3.6.0\n", encoding="utf-8")
        return result, binding

    def test_release_metadata_bridge_preserves_original_records_and_per_case_candidates(self):
        result, binding = self.released_case()
        before = deepcopy(result)
        self.assertTrue(self.errors(result, accept=True))
        self.assertEqual(self.errors(result, accept=True, release_binding=binding), [])
        self.assertEqual(result, before)
        self.assertNotEqual(result["candidate"], next(row for row in result["cases"] if row["id"] == "S04")["candidate"])
        self.assertTrue((self.record_dir / "outputs/S04.md").is_file())

    def test_release_bridge_does_not_relax_output_preparation_or_override_checks(self):
        result, binding = self.released_case()
        for field, item in (("preparationSha256", "0" * 64), ("outputFile", "S04.md"),
                            ("candidate", {"files": {}, "sha256": "0" * 64})):
            changed = deepcopy(result)
            next(row for row in changed["cases"] if row["id"] == "S04")[field] = item
            # Even a deliberately rebound synthetic record must retain the
            # independent preparation/output/complete-candidate checks.
            rebound = deepcopy(binding)
            rebound["records"][UI_RECORD] = content_digest(changed)
            self.assertTrue(self.errors(changed, accept=True, release_binding=rebound), field)
        (self.record_dir / "outputs/S04-r12.md").write_bytes(b"replacement\n")
        self.assertTrue(any("actual output" in e for e in self.errors(result, release_binding=binding)))


class ReleaseVersionBindingTests(unittest.TestCase):
    def setUp(self):
        self.previous = {"VERSION": version_digest("3.5.1"), "SKILL.md": "a" * 64}
        candidate = {"files": self.previous, "sha256": tree_digest(self.previous)}
        self.ui = {"skillVersion": "3.5.1", "cases": [{"id": "S04", "candidate": candidate}]}
        self.wps = {"candidate": candidate}
        self.actual = {**self.previous, "VERSION": version_digest("3.6.0")}
        self.binding = release_binding_for(self.ui, self.wps, self.previous)

    def check(self, result=None, actual=None, binding=None, record=UI_RECORD, current_version="3.6.0"):
        return release_predecessor(self.ui if result is None else result,
                                   self.actual if actual is None else actual,
                                   self.binding if binding is None else binding,
                                   record=record, current_version=current_version)

    def test_exact_transition_is_non_mutating_and_covers_both_records(self):
        before = deepcopy((self.ui, self.wps, self.actual, self.binding))
        self.assertEqual(self.check(), self.previous)
        self.assertEqual(self.check(result=self.wps, record=WPS_RECORD), self.previous)
        self.assertEqual((self.ui, self.wps, self.actual, self.binding), before)

    def test_non_version_changes_and_inventory_changes_are_rejected(self):
        for actual in ({**self.actual, "SKILL.md": "b" * 64},
                       {**self.actual, "new.md": "b" * 64}, {"VERSION": self.actual["VERSION"]}):
            with self.assertRaises(ValueError):
                self.check(actual=actual)
            rebound = deepcopy(self.binding)
            rebound["candidate_after_sha256"] = tree_digest(actual)
            rebound["candidate_before_sha256"] = tree_digest({**actual, "VERSION": version_digest("3.5.1")})
            with self.assertRaises(ValueError):
                self.check(actual=actual, binding=rebound)

    def test_wrong_identity_parent_target_scope_and_record_are_rejected(self):
        for key, value in (("schema_version", 2), ("normalization", "none"),
                           ("scope", "general-compatibility"), ("decision", "elsewhere"),
                           ("recorded_version", "3.5.0"), ("release_version", "3.6.1"),
                           ("candidate_before_sha256", "0" * 64),
                           ("candidate_after_sha256", "0" * 64), ("notes", "")):
            with self.assertRaises(ValueError, msg=key):
                self.check(binding={**self.binding, key: value})
        for current in ("3.5.1", "3.6.1", None):
            with self.assertRaises(ValueError):
                self.check(current_version=current)
        for record in ("evals/ui-foundations/result.json", "../r12-result.json", WPS_RECORD):
            with self.assertRaises(ValueError):
                self.check(record=record)
        for changed in ({**self.ui, "skillVersion": "3.6.0"}, {**self.ui, "cases": []}):
            with self.assertRaises(ValueError):
                self.check(result=changed)

    def test_missing_extra_malformed_and_changed_bindings_are_rejected(self):
        mutations = [None, [], {}, {**self.binding, "extra": True}]
        for key in self.binding:
            changed = deepcopy(self.binding); changed.pop(key); mutations.append(changed)
        for key in ("path", "previous_sha256", "sha256"):
            changed = deepcopy(self.binding); changed["version_change"][key] = "wrong"; mutations.append(changed)
        for records in ({UI_RECORD: content_digest(self.ui)}, {**self.binding["records"], "other": "a" * 64},
                        {**self.binding["records"], UI_RECORD: "0" * 64}, []):
            mutations.append({**self.binding, "records": records})
        for changed in mutations:
            with self.assertRaises(ValueError):
                release_predecessor(self.ui, self.actual, changed, record=UI_RECORD, current_version="3.6.0")
        with self.assertRaises(ValueError):
            self.check(actual={**self.actual, "VERSION": version_digest("3.6.0")[:-1] + "x"})

    def test_actual_release_tree_and_retained_r12_records(self):
        binding = json.loads((ROOT / "evals/r12-release-version.json").read_text(encoding="utf-8"))
        from r13_source_binding import r13_predecessor
        actual = r13_predecessor(snapshot(ROOT / "skills/ui-ux-skill"))
        version = "3.6.0"  # Verified released predecessor, not the current metadata version.
        for record in (UI_RECORD, WPS_RECORD):
            result = json.loads((ROOT / record).read_text(encoding="utf-8"))
            previous = release_predecessor(result, actual, binding, record=record, current_version=version)
            self.assertEqual(set(previous), set(actual))
            self.assertEqual([name for name in previous if previous[name] != actual[name]], ["VERSION"])


if __name__ == "__main__":
    unittest.main()
