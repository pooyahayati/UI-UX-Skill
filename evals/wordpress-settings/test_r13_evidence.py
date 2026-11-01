"""Current R13 runtime successor; historical R12 acceptance remains separate."""
import copy
import hashlib
import json
import unittest
from test_contracts import HERE, ROOT, canonical_bytes, r13_fixture_successor, r12_runtime_errors, discovery_metadata_errors, R12_DISCOVERY_IDS, R12_REGRESSION_IDS


def read(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


class R13Evidence(unittest.TestCase):
    def test_error_ownership_producer_metadata_mutations(self):
        from test_contracts import R13_VALIDATION_IDS
        original = read("evidence/r13/validation/r13-validation-results.json")
        def check(r): return r12_runtime_errors(r, original["behavior_hashes"], original["fixture_hashes"], original["runner_sha256"], R13_VALIDATION_IDS)
        self.assertEqual(check(original), [])
        for key, value in (("complete", False), ("scope", "partial"), ("omitted_observations", ["ERR-retained-current-fa"]),
                           ("compatibility", []), ("captures", []), ("captures", [None]), ("compatibility", [None])):
            self.assertTrue(check({**original, key: value}), key)
        for key in ("complete", "scope", "omitted_observations", "compatibility", "captures"):
            broken = copy.deepcopy(original); broken.pop(key); self.assertTrue(check(broken), key)
        for key, value in (("service", "minimum"), ("language", "fa"), ("variant", "workspace"),
                           ("viewport", {"width": 390, "height": 1000}), ("state", "ready"), ("overflow", True)):
            broken = copy.deepcopy(original); broken["captures"][0][key] = value
            self.assertTrue(check(broken), key)
        broken = copy.deepcopy(original); broken["observations"][0]["method"] = "source-trace"
        self.assertTrue(check(broken))

    def test_full_discovery_metadata_mutations(self):
        for name in ("evidence/r12-browser-results.json", "evidence/r13/discovery/r12-browser-results.json"):
            original = read(name)
            def check(report):
                return r12_runtime_errors(report, original["behavior_hashes"], original["fixture_hashes"], original["runner_sha256"], R12_DISCOVERY_IDS)
            self.assertEqual(check(original), [])
            for field, value, reason in (
                ("complete", False, "complete scope"), ("complete", 1, "complete scope"),
                ("scope", "settings-only partial; D10 workspace not executed", "complete scope"),
                ("omitted_observations", ["D10"], "omitted"), ("omitted_observations", {}, "omitted"),
                ("compatibility", None, "supported host"), ("compatibility", [], "supported host"),
                ("captures", None, "capture matrix"), ("captures", [None], "capture matrix"),
            ):
                self.assertTrue(any(reason in e for e in check({**original, field: value})), field)
            for field in ("complete", "scope", "omitted_observations", "compatibility", "captures"):
                broken = copy.deepcopy(original); broken.pop(field)
                self.assertTrue(check(broken), field)
            mutations = [
                (lambda r: r["observations"][0].update(method="source-trace"), "method"),
                (lambda r: r["observations"][0].pop("method"), "method"),
                (lambda r: r["observations"].pop(9), "observations"),
                (lambda r: r["compatibility"].pop(), "supported host"),
                (lambda r: r["compatibility"][0].update(core="0.0"), "declared host"),
                (lambda r: r["compatibility"][0].update(exports={}), "public controls"),
                (lambda r: r["captures"].pop(), "capture matrix"),
                (lambda r: r["captures"].append(copy.deepcopy(r["captures"][0])), "capture matrix"),
            ]
            for mutate, reason in mutations:
                broken = copy.deepcopy(original); mutate(broken)
                self.assertTrue(any(reason in e for e in check(broken)), reason)
            for key, value in (("service", "minimum"), ("language", "en"), ("variant", "workspace"),
                               ("viewport", {"width": 390, "height": 844}), ("state", "saved"),
                               ("theme", "dark"), ("direction", "ltr"), ("overflow", True)):
                broken = copy.deepcopy(original); broken["captures"][0][key] = value
                self.assertTrue(any("required host/locale/viewport/state" in e for e in check(broken)), key)

    def test_legacy_contract_does_not_require_discovery_fields(self):
        for name in ("evidence/r12-regression-results.json", "evidence/r13/regression/r13-regression-results.json"):
            report = read(name)
            self.assertNotIn("complete", report)
            self.assertNotIn("compatibility", report)
            self.assertEqual(r12_runtime_errors(report, report["behavior_hashes"], report["fixture_hashes"],
                report["runner_sha256"], R12_REGRESSION_IDS), [])
            self.assertTrue(discovery_metadata_errors(report), "Legacy evidence cannot be promoted to full discovery")

    def test_bounded_fixture_successor(self):
        parent = read("evidence/r12-browser-results.json")["fixture_hashes"]
        delta = read("r13-fixture-delta.json")
        current = r13_fixture_successor(parent, delta)
        self.assertNotEqual(current["app.js"], parent["app.js"])
        for name in set(parent) - {"app.js"}: self.assertEqual(current[name], parent[name])
        missing = copy.deepcopy(delta); missing["changes"] = {}
        extra = copy.deepcopy(delta); extra["changes"]["model.js"] = delta["changes"]["app.js"]
        wrong = copy.deepcopy(delta); wrong["changes"]["app.js"]["previous_sha256"] = "0" * 64
        for bad in (missing, extra, wrong, {**delta, "parents": {}}, {**delta, "decision": "unrelated"}):
            with self.assertRaises(ValueError): r13_fixture_successor(parent, bad)

    def test_current_runtime_and_images(self):
        prior = read("evidence/r12-browser-results.json")
        fixture = r13_fixture_successor(prior["fixture_hashes"], read("r13-fixture-delta.json"))
        ids = {f"ERR-{case}-{service}-{lang}" for case in ("retained", "delayed-corrected", "delayed-unchanged")
               for service, lang in (("current", "en"), ("minimum", "en"), ("current", "fa"))}
        for folder, filename, runner, expected in (
            ("validation", "r13-validation-results.json", "run_validation.cjs", ids),
            ("discovery", "r12-browser-results.json", "run_discovery.cjs", R12_DISCOVERY_IDS),
            ("regression", "r13-regression-results.json", "run_browser.cjs", R12_REGRESSION_IDS),
        ):
            report = read(f"evidence/r13/{folder}/{filename}")
            self.assertEqual(r12_runtime_errors(report, prior["behavior_hashes"], fixture,
                hashlib.sha256(canonical_bytes(HERE / runner)).hexdigest(), expected), [])
            if folder == "regression":
                raw = HERE / "evidence/r13/regression/browser-results.json"
                self.assertEqual(report["provenance"]["raw_sha256"], hashlib.sha256(canonical_bytes(raw)).hexdigest())
                for key, value in json.loads(raw.read_text(encoding="utf-8")).items(): self.assertEqual(report[key], value)
            for capture in report.get("captures", []):
                self.assertEqual(hashlib.sha256((HERE / "evidence/r13" / folder / capture["file"]).read_bytes()).hexdigest(), capture["sha256"])
                self.assertFalse(capture["overflow"])


if __name__ == "__main__": unittest.main()
