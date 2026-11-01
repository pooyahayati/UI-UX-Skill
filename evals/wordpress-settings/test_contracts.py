"""Dedicated WPS source/isolation and evidence-integrity checks, not model evaluation."""
from __future__ import annotations

import argparse
import copy
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
EXPECTED = {f"WP-{i:02d}" for i in range(1, 15)} | {f"ISO-{i:02d}" for i in range(1, 6)}
BEHAVIOR = {
    "references/products/wordpress-plugin.md", "references/products/wordpress/settings.md",
    "references/products/wordpress/components.md",
}
R12_FIXTURE_CHANGES = {"app.js", "style.css", "wps-specimen.php", "discovery.js", "workspace.js"}
R12_PARENT_HASHES = {
    "baseline.json": "7f9c912937e0bc65487d98194b6f3c10593daf530c9eaea3f8e1971da88dc570",
    "RESULTS.json": "7946519749a5f7c2677b47671666fab09b73a58efd0b1e855dbe52fa4ce2b2ac",
    "r11-fixture-delta.json": "5da598e8b69efc00653f0596c207ccf833577980041a73a3379fdbef6a85cec7",
    "r11-license-delta.json": "dad8e38265e8997f5195ac6732193a045414d0c016597c77c005252b3cb5cea2",
    "evidence/r11-browser-results.json": "8f7f8cec1079bf9320543248ff249e67c39450169bfa68c9f5077a5260023ed4",
}
R12_DISCOVERY_IDS = {f"D{i:02d}" for i in range(1, 12)}
R13_VALIDATION_IDS = {f"ERR-{case}-{service}-{lang}" for case in ("retained", "delayed-corrected", "delayed-unchanged")
                      for service, lang in (("current", "en"), ("minimum", "en"), ("current", "fa"))}
R12_REGRESSION_IDS = ({f"WP-{i:02d}" for i in range(1, 15)} - {"WP-10"}) | {
    "R11-CONFLICT-current", "R11-CONFLICT-minimum", "R11-CONFLICT-RTL",
}


def canonical_bytes(path):
    return path.read_bytes().replace(b"\r\n", b"\n")


def isolation_errors(skill_root, baseline):
    errors = []
    protected = baseline.get("protected_skill_hashes", {})
    if baseline.get("normalization") != "git-lf" or not protected:
        return ["Missing canonical protected baseline"]
    prefix = "skills/ui-ux-skill/"
    actual = {p.relative_to(skill_root).as_posix() for p in skill_root.rglob("*") if p.is_file()}
    expected_protected = actual - BEHAVIOR - {"VERSION"}
    recorded = {p[len(prefix):] for p in protected if p.startswith(prefix)}
    if recorded != expected_protected or len(recorded) != len(protected):
        errors.append("Protected baseline coverage or unexpected Skill resources changed")
    for name, digest in protected.items():
        rel = name[len(prefix):] if name.startswith(prefix) else ""
        if not rel or ".." in Path(rel).parts or not re.fullmatch(r"[a-f0-9]{64}", str(digest)):
            errors.append("Malformed protected path/hash")
            continue
        path = skill_root / rel
        if not path.is_file() or hashlib.sha256(canonical_bytes(path)).hexdigest() != digest:
            errors.append(f"Protected resource changed: {rel}")
    return errors


def current_source_baseline(baseline, delta):
    """Keep the WPS checkpoint intact; bind the separately authorized successor.

    Exact hashes still protect every resource. This is source integrity, not
    a rerun or transfer of the historical WPS behavioral acceptance.
    """
    allowed = {
        "skills/ui-ux-skill/references/products/dashboard.md",
        "skills/ui-ux-skill/references/implementation-strategies.md",
        "skills/ui-ux-skill/references/shadcn-ui.md",
    }
    if (delta.get("schema_version") != 1 or delta.get("normalization") != "git-lf"
            or delta.get("decision") != "ROADMAP.md#shadcnui-dashboard-default"
            or delta.get("authorized_on") != "2026-10-16"
            or set(delta.get("changes", {})) != allowed):
        raise ValueError("Invalid shadcn source delta or authorization scope")
    updated = copy.deepcopy(baseline)
    for name, binding in delta["changes"].items():
        if (binding.get("previous_sha256") != baseline["protected_skill_hashes"].get(name)
                or not re.fullmatch(r"[a-f0-9]{64}", str(binding.get("sha256", "")))):
            raise ValueError("Source delta does not bind the retained baseline: " + name)
        updated["protected_skill_hashes"][name] = binding["sha256"]
    return updated


def motion_source_baseline(baseline, delta):
    """Bind the authorized motion successor without rewriting earlier evidence."""
    allowed = {
        "skills/ui-ux-skill/references/shared/motion.md",
        "skills/ui-ux-skill/references/implementation-strategies.md",
        "skills/ui-ux-skill/references/shadcn-ui.md",
        "skills/ui-ux-skill/references/runtime-ui-governance.md",
        "skills/ui-ux-skill/assets/templates/DESIGN.md",
        "skills/ui-ux-skill/references/interactive-motion.md",
    }
    if (delta.get("schema_version") != 1 or delta.get("normalization") != "git-lf"
            or delta.get("decision") != "ROADMAP.md#interactive-motion"
            or delta.get("authorized_on") != "2026-10-16"
            or set(delta.get("changes", {})) != allowed):
        raise ValueError("Invalid motion source delta or authorization scope")
    updated = copy.deepcopy(baseline)
    for name, binding in delta["changes"].items():
        if (binding.get("previous_sha256") != baseline["protected_skill_hashes"].get(name)
                or not re.fullmatch(r"[a-f0-9]{64}", str(binding.get("sha256", "")))):
            raise ValueError("Motion delta does not bind the retained baseline: " + name)
        updated["protected_skill_hashes"][name] = binding["sha256"]
    return updated


def active_source_baseline():
    baseline = json.loads((HERE / "baseline.json").read_text(encoding="utf-8"))
    shadcn = json.loads((ROOT / "evals/shadcn/source-delta.json").read_text(encoding="utf-8"))
    motion = json.loads((ROOT / "evals/motion/source-delta.json").read_text(encoding="utf-8"))
    license_delta = json.loads((HERE / "r11-license-delta.json").read_text(encoding="utf-8"))
    updated = license_source_baseline(motion_source_baseline(current_source_baseline(baseline, shadcn), motion), license_delta)
    sys.path.insert(0, str(ROOT / "scripts"))
    from r13_source_binding import r13_predecessor
    r13_predecessor()  # Verify exact full source scope before updating protected expectations.
    delta = json.loads((ROOT / "evals/r13-source.json").read_text(encoding="utf-8"))
    for name, binding in delta["changes"].items():
        key = "skills/ui-ux-skill/" + name
        if key in updated["protected_skill_hashes"]:
            if updated["protected_skill_hashes"][key] != binding["previous_sha256"]:
                raise ValueError("R13 protected-source predecessor mismatch: " + name)
            updated["protected_skill_hashes"][key] = binding["sha256"]
    return updated


def license_source_baseline(baseline, delta):
    name = "skills/ui-ux-skill/LICENSE"
    if (delta.get("schema_version") != 1 or delta.get("normalization") != "git-lf"
            or delta.get("decision") != "ROADMAP.md#r11-audit-remediation"
            or delta.get("authorized_on") != "2026-10-16" or set(delta.get("changes", {})) != {name}):
        raise ValueError("Invalid R11 license successor scope")
    binding = delta["changes"][name]
    if (name in baseline["protected_skill_hashes"] or binding.get("previous_sha256") is not None
            or "previous_sha256" not in binding
            or binding.get("sha256") != "62c149a3a65bbd3b2f545e7279838b76ede79d3aac3ac786a5eaff21e7e583b7"):
        raise ValueError("Invalid R11 license addition or content")
    updated = copy.deepcopy(baseline)
    updated["protected_skill_hashes"][name] = binding["sha256"]
    return updated


def report_errors(report):
    errors = []
    if report.get("schema_version") != 1 or report.get("fresh_model_evaluation") is not False:
        errors.append("Report must distinguish same-session/source/runtime evidence from fresh model evaluation")
    rows = report.get("outcomes")
    if not isinstance(rows, list):
        return errors + ["Missing outcome inventory"]
    ids = [row.get("id") for row in rows if isinstance(row, dict)]
    if len(ids) != len(EXPECTED) or set(ids) != EXPECTED:
        errors.append("Missing/duplicate/unexpected WPS outcomes")
    for row in rows:
        if not isinstance(row, dict) or row.get("status") != "passed" or row.get("accepted") is not True:
            errors.append("Unresolved or contradictory outcome")
            continue
        if not row.get("evidence") or not row.get("detail"):
            errors.append("Outcome lacks concrete evidence")
        expected_method = "source-trace" if row["id"] in {"WP-10", "ISO-01", "ISO-02", "ISO-03", "ISO-04"} else "package-diff" if row["id"] == "ISO-05" else "real-admin-browser"
        if row.get("method") != expected_method:
            errors.append("Outcome method does not meet its required evidence boundary")
    return errors


def fixture_successor(historical, delta):
    """Only the two R11.1 fixture changes may succeed the immutable WPS record."""
    if (delta.get("schema_version") != 1 or delta.get("normalization") != "git-lf"
            or delta.get("decision") != "ROADMAP.md#r11-audit-remediation"
            or delta.get("authorized_on") != "2026-10-16"
            or set(delta.get("changes", {})) != {"app.js", "model.js"}):
        raise ValueError("Invalid R11 fixture successor scope")
    current = dict(historical)
    for name, binding in delta["changes"].items():
        if (binding.get("previous_sha256") != historical.get(name)
                or not re.fullmatch(r"[a-f0-9]{64}", str(binding.get("sha256", "")))):
            raise ValueError("R11 fixture successor does not bind its parent")
        current[name] = binding["sha256"]
    return current


def r12_successor(behavior_parent, fixture_parent, delta):
    """Bind only the authorized R12 changes to the retained WPS/R11 parents.

    This produces expected source identities; acceptance still requires fresh
    runtime records and their independent source/runner checks below.
    """
    if (delta.get("schema_version") != 1 or delta.get("normalization") != "git-lf"
            or delta.get("decision") != "docs/R12_EXECUTION.md#authority"
            or delta.get("authorized_on") != "2026-11-01"
            or delta.get("parents") != R12_PARENT_HASHES
            or set(delta.get("skill_changes", {})) != BEHAVIOR
            or set(delta.get("fixture_changes", {})) != R12_FIXTURE_CHANGES
            or set(behavior_parent) != BEHAVIOR):
        raise ValueError("Invalid R12 successor scope or retained-parent binding")
    updated = []
    for parent, changes, additions in (
        (behavior_parent, delta["skill_changes"], set()),
        (fixture_parent, delta["fixture_changes"], {"discovery.js", "workspace.js"}),
    ):
        current = dict(parent)
        for name, binding in changes.items():
            if (not isinstance(binding, dict) or "previous_sha256" not in binding
                    or (name not in parent) != (name in additions)
                    or binding["previous_sha256"] != parent.get(name)
                    or not re.fullmatch(r"[a-f0-9]{64}", str(binding.get("sha256", "")))
                    or binding["sha256"] == parent.get(name)):
                raise ValueError("R12 successor does not bind its exact parent: " + name)
            current[name] = binding["sha256"]
        updated.append(current)
    return tuple(updated)


def supported_host_errors(report, expected_surfaces):
    errors = []
    compose = (ROOT / "evals/fixtures/wordpress-settings/compose.yaml").read_text(encoding="utf-8")
    hosts = {}
    for service in ("current", "minimum"):
        block = re.search(rf"^  {service}:\n(.*?)(?=^  [a-z]|^volumes:)", compose, re.M | re.S).group(1)
        hosts[service] = (re.search(r'WPS_CORE_VERSION: "([^"]+)"', block).group(1),
                          re.search(r'WPS_SITE_URL: "([^"]+)"', block).group(1),
                          re.search(r'image: wordpress:php([0-9.]+)-', block).group(1))
    compatibility = report.get("compatibility")
    if (not isinstance(compatibility, list) or len(compatibility) != len(expected_surfaces)
            or any(not isinstance(row, dict) for row in compatibility)
            or {(row.get("service"), row.get("actualOwnedLanguage")) for row in compatibility
                if isinstance(row, dict) and isinstance(row.get("service"), str) and isinstance(row.get("actualOwnedLanguage"), str)} != set(expected_surfaces)):
        errors.append("Discovery compatibility must identify each required supported host/language surface exactly once")
    else:
        controls = {"TextControl", "ToggleControl", "SelectControl", "Button", "Notice", "Modal", "Spinner", "PanelBody", "SearchControl"}
        for row in compatibility:
            core, base, php = hosts[row["service"]]
            exports, asset = row.get("exports"), row.get("asset_metadata")
            if (row.get("actualRootDirection") != ("rtl" if row["actualOwnedLanguage"] == "fa" else "ltr")
                    or row.get("core") != core or row.get("base") != base
                    or not isinstance(row.get("php"), str) or not row["php"].startswith(php + ".")
                    or row.get("plugins") != ["wps-specimen/wps-specimen.php"]
                    or not isinstance(exports, dict) or set(exports) != controls or any(v is not True for v in exports.values())
                    or not isinstance(asset, dict) or asset.get("dependencies") != ["wp-components", "wp-element"]):
                errors.append("Discovery compatibility disagrees with declared host or verified public controls")

    return errors


def discovery_metadata_errors(report):
    """Full discovery producer contract, not a requirement on legacy runners."""
    errors = []
    if (report.get("complete") is not True or report.get("scope") != "full R12 discovery and workspace"
            or report.get("omitted_observations") != []):
        errors.append("Full discovery needs complete scope and no omitted observations")
    errors.extend(supported_host_errors(report, {("current", "en"), ("minimum", "en")}))
    # State names are tied to actual producer capture destinations. General
    # ready-state alone cannot distinguish default, recipient and detail views.
    matrix = {}
    for width, height in ((1440, 1100), (390, 844)):
        for name in ("current", "recipient"):
            matrix[f"discovery-{name}-fa-{width}.png"] = ("current", "fa", width, height, "discovery", "ready")
        matrix[f"workspace-current-fa-{width}.png"] = ("current", "fa", width, height, "workspace", "ready")
    matrix["discovery-minimum-en-390.png"] = ("minimum", "en", 390, 844, "discovery", "saved")
    matrix["workspace-minimum-en-390.png"] = ("minimum", "en", 390, 844, "workspace", "ready")
    for name, variant in (("detail", "modal"), ("connection", "connection"), ("failed", "failed")):
        matrix[f"workspace-{name}-current-fa-390.png"] = ("current", "fa", 390, 844, "workspace-" + variant, "ready")
    captures = report.get("captures")
    if not isinstance(captures, list) or any(not isinstance(row, dict) or not isinstance(row.get("file"), str) for row in captures):
        return errors + ["Discovery capture matrix missing or malformed"]
    names = [row["file"].removeprefix("r12-") for row in captures]
    if len(names) != len(matrix) or set(names) != set(matrix):
        errors.append("Discovery capture matrix is missing, duplicate or out of scope")
    for name, row in zip(names, captures):
        if name not in matrix: continue
        service, language, width, height, variant, state = matrix[name]
        if (row.get("service") != service or row.get("language") != language or row.get("variant") != variant
                or row.get("viewport") != {"width": width, "height": height} or row.get("state") != state
                or row.get("theme") != "light" or row.get("direction") != ("rtl" if language == "fa" else "ltr")
                or row.get("overflow") is not False or row.get("toolbar") is not True or row.get("menu") is not True):
            errors.append("Discovery capture metadata disagrees with its required host/locale/viewport/state cell: " + name)
    return errors


def validation_metadata_errors(report):
    errors = []
    if (report.get("complete") is not True or report.get("scope") != "R13 section and submitted-value error ownership"
            or report.get("omitted_observations") != []):
        errors.append("Full R13 validation needs complete scope and no omitted observations")
    cells = {("current", "en", 1440), ("minimum", "en", 390), ("current", "fa", 390)}
    errors.extend(supported_host_errors(report, {(s, l) for s, l, _ in cells}))
    captures = report.get("captures")
    if not isinstance(captures, list) or len(captures) != 3 or any(not isinstance(row, dict) for row in captures):
        return errors + ["R13 validation capture matrix missing or malformed"]
    expected = {f"r13-errors-{s}-{l}-{w}.png": (s, l, w) for s, l, w in cells}
    names = [row.get("file") for row in captures]
    if any(not isinstance(name, str) for name in names) or set(names) != set(expected):
        return errors + ["R13 validation capture matrix missing, duplicate or out of scope"]
    for row in captures:
        service, language, width = expected[row["file"]]
        if (row.get("service") != service or row.get("language") != language
                or row.get("viewport") != {"width": width, "height": 1000}
                or row.get("variant") != "discovery" or row.get("state") != "saved"
                or row.get("theme") != "light" or row.get("direction") != ("rtl" if language == "fa" else "ltr")
                or row.get("overflow") is not False or row.get("toolbar") is not True or row.get("menu") is not True):
            errors.append("R13 validation capture disagrees with required host/locale/viewport/state cell")
    return errors


def r12_runtime_errors(report, behavior, fixture, runner_sha256, expected_ids):
    """Check fresh runtime evidence against the exact successor and runner."""
    errors = []
    try:
        recorded = report.get("recorded_on", "")
        dated = bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", recorded)) and date.fromisoformat(recorded) >= date(2026, 11, 1)
    except (ValueError, TypeError):
        dated = False
    if report.get("schema_version") != 1 or not dated:
        errors.append("R12 runtime record needs its schema and a valid post-authorization date")
    if report.get("behavior_hashes") != behavior or report.get("fixture_hashes") != fixture:
        errors.append("R12 runtime record does not bind the successor source")
    if report.get("runner_sha256") != runner_sha256:
        errors.append("R12 runtime record does not bind its actual runner")
    if report.get("javascript_errors") != [] or report.get("console_warnings") != []:
        errors.append("R12 runtime errors or warnings are unresolved or missing")
    rows = report.get("observations")
    if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
        return errors + ["R12 runtime observation inventory is missing or malformed"]
    ids = [row.get("id") for row in rows]
    if (any(not isinstance(name, str) for name in ids)
            or len(ids) != len(set(ids))
            or {name for name in ids if not name.startswith("VIEW-")} != expected_ids):
        errors.append("R12 runtime observations are missing, duplicate or out of scope")
    def has_detail(row):
        detail = row.get("detail")
        # The legacy runner records viewport geometry as an object. Required
        # behavioral observations still need an actual explanatory string.
        if isinstance(row.get("id"), str) and row["id"].startswith("VIEW-") and isinstance(detail, dict):
            return bool(detail)
        return isinstance(detail, str) and bool(detail.strip())

    if any(row.get("status") != "passed" or not has_detail(row) for row in rows):
        errors.append("R12 runtime observation is failed or lacks actual detail")
    if any(row.get("method") != "real-admin-browser" for row in rows):
        errors.append("Runtime observation method must be real-admin-browser")
    if expected_ids == R12_DISCOVERY_IDS:
        errors.extend(discovery_metadata_errors(report))
    elif expected_ids == R13_VALIDATION_IDS:
        errors.extend(validation_metadata_errors(report))
    return errors


def r13_fixture_successor(parent, delta):
    """R13.1 changes only App error ownership; older runtime records stay intact."""
    parents = {name: hashlib.sha256(canonical_bytes(HERE / name)).hexdigest() for name in
               ("r12-source-fixture-delta.json", "evidence/r12-browser-results.json", "evidence/r12-regression-results.json")}
    if (delta.get("schema_version") != 1 or delta.get("normalization") != "git-lf"
            or delta.get("decision") != "docs/R13_EXECUTION.md#authority"
            or delta.get("authorized_on") != "2026-11-01"
            or delta.get("parents") != parents or set(delta.get("changes", {})) != {"app.js"}):
        raise ValueError("Invalid R13 fixture successor scope/parent")
    binding = delta["changes"]["app.js"]
    if (binding.get("previous_sha256") != parent["app.js"]
            or not re.fullmatch(r"[a-f0-9]{64}", str(binding.get("sha256", "")))
            or binding["sha256"] == parent["app.js"]):
        raise ValueError("R13 fixture successor does not bind its exact parent")
    return {**parent, "app.js": binding["sha256"]}


class WPSContracts(unittest.TestCase):
    def test_historical_evaluation_content_unchanged(self):
        baseline = json.loads((HERE / "baseline.json").read_text(encoding="utf-8"))
        for rel, binding in baseline["protected_evaluation_content"].items():
            content = json.loads((ROOT / rel).read_text(encoding="utf-8"))
            for field in binding["exclude_release_fields"]:
                content.pop(field)
            data = json.dumps(content, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()
            self.assertEqual(hashlib.sha256(data).hexdigest(), binding["sha256"], rel)

    def test_protected_source_identity(self):
        self.assertEqual(isolation_errors(ROOT / "skills/ui-ux-skill", active_source_baseline()), [])

    def test_successor_scope_rejects_wrong_parent_extra_paths_and_missing_changes(self):
        baseline = json.loads((HERE / "baseline.json").read_text(encoding="utf-8"))
        before = copy.deepcopy(baseline)
        delta = json.loads((ROOT / "evals/shadcn/source-delta.json").read_text(encoding="utf-8"))
        current = current_source_baseline(baseline, delta)
        self.assertEqual(baseline, before)
        for name, digest in before["protected_skill_hashes"].items():
            if name not in delta["changes"]:
                self.assertEqual(current["protected_skill_hashes"][name], digest)
        bad_parent = copy.deepcopy(delta)
        next(iter(bad_parent["changes"].values()))["previous_sha256"] = "0" * 64
        extra = copy.deepcopy(delta)
        extra["changes"]["skills/ui-ux-skill/SKILL.md"] = {"sha256": "0" * 64}
        missing = copy.deepcopy(delta)
        missing["changes"].pop(next(iter(missing["changes"])))
        for bad in [bad_parent, extra, missing, {**delta, "decision": "unrelated"}]:
            with self.assertRaises(ValueError):
                current_source_baseline(baseline, bad)

    def test_successor_content_mismatch_is_not_exempted(self):
        baseline = active_source_baseline()
        self.assertEqual(isolation_errors(ROOT / "skills/ui-ux-skill", baseline), [])
        changed = set()
        for rel in ["evals/shadcn/source-delta.json", "evals/motion/source-delta.json", "evals/wordpress-settings/r11-license-delta.json"]:
            changed.update(json.loads((ROOT / rel).read_text(encoding="utf-8"))["changes"])
        for name in changed:
            mismatched = copy.deepcopy(baseline)
            mismatched["protected_skill_hashes"][name] = "0" * 64
            errors = isolation_errors(ROOT / "skills/ui-ux-skill", mismatched)
            self.assertEqual(errors, ["Protected resource changed: " + name.removeprefix("skills/ui-ux-skill/")])

    def test_motion_successor_preserves_parent_and_rejects_scope_or_chain_changes(self):
        original = json.loads((HERE / "baseline.json").read_text(encoding="utf-8"))
        shadcn = json.loads((ROOT / "evals/shadcn/source-delta.json").read_text(encoding="utf-8"))
        baseline = current_source_baseline(original, shadcn)
        before = copy.deepcopy(baseline)
        delta = json.loads((ROOT / "evals/motion/source-delta.json").read_text(encoding="utf-8"))
        updated = motion_source_baseline(baseline, delta)
        self.assertEqual(baseline, before)
        for name, digest in before["protected_skill_hashes"].items():
            if name not in delta["changes"]:
                self.assertEqual(updated["protected_skill_hashes"][name], digest)
        with self.assertRaises(ValueError):
            motion_source_baseline(original, delta)  # Cannot skip the shadcn parent.
        wrong_parent = copy.deepcopy(delta)
        next(iter(wrong_parent["changes"].values()))["previous_sha256"] = "0" * 64
        extra = copy.deepcopy(delta)
        extra["changes"]["skills/ui-ux-skill/SKILL.md"] = {"sha256": "0" * 64}
        missing = copy.deepcopy(delta)
        missing["changes"].pop(next(iter(missing["changes"])))
        malformed = copy.deepcopy(delta)
        next(iter(malformed["changes"].values()))["sha256"] = "not-a-hash"
        for bad in [wrong_parent, extra, missing, malformed, {**delta, "decision": "unrelated"},
                    {**delta, "authorized_on": "unknown"}, {**delta, "normalization": "none"}]:
            with self.assertRaises(ValueError):
                motion_source_baseline(baseline, bad)

    def test_license_successor_rejects_extra_missing_content_and_reapplication(self):
        baseline = active_source_baseline()
        baseline["protected_skill_hashes"].pop("skills/ui-ux-skill/LICENSE")
        delta = json.loads((HERE / "r11-license-delta.json").read_text(encoding="utf-8"))
        before = copy.deepcopy(baseline)
        updated = license_source_baseline(baseline, delta)
        self.assertEqual(baseline, before)
        self.assertEqual(len(updated["protected_skill_hashes"]), len(before["protected_skill_hashes"]) + 1)
        with self.assertRaises(ValueError):
            license_source_baseline(updated, delta)
        wrong = copy.deepcopy(delta); wrong["changes"]["skills/ui-ux-skill/LICENSE"]["sha256"] = "0" * 64
        parent = copy.deepcopy(delta); parent["changes"]["skills/ui-ux-skill/LICENSE"]["previous_sha256"] = "0" * 64
        extra = copy.deepcopy(delta); extra["changes"]["skills/ui-ux-skill/SKILL.md"] = {"sha256": "0" * 64}
        for bad in [wrong, parent, extra, {**delta, "changes": {}}, {**delta, "decision": "unrelated"}]:
            with self.assertRaises(ValueError):
                license_source_baseline(baseline, bad)

    def test_isolation_detects_modified_missing_and_extra_resources(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            p = root / "SKILL.md"
            p.write_bytes(b"protected\n")
            baseline = {"normalization": "git-lf", "protected_skill_hashes": {
                "skills/ui-ux-skill/SKILL.md": hashlib.sha256(b"protected\n").hexdigest()}}
            self.assertEqual(isolation_errors(root, baseline), [])
            p.write_bytes(b"changed\n")
            self.assertTrue(isolation_errors(root, baseline))
            p.unlink()
            self.assertTrue(isolation_errors(root, baseline))
            p.write_bytes(b"protected\r\n")
            self.assertEqual(isolation_errors(root, baseline), [])
            (root / "unexpected.md").write_bytes(b"extra")
            self.assertTrue(isolation_errors(root, baseline))

    def test_raw_inputs_cover_required_scenarios(self):
        inputs = json.loads((ROOT / "evals/fixtures/wordpress-settings/briefs.json").read_text(encoding="utf-8"))["briefs"]
        self.assertEqual({row["id"] for row in inputs}, EXPECTED)
        self.assertEqual(len(inputs), len(EXPECTED))
        self.assertTrue(all(row.get("request") for row in inputs))

    def test_local_guide_has_only_settings_callers(self):
        skill = ROOT / "skills/ui-ux-skill"
        callers = []
        for path in skill.rglob("*.md"):
            if path.name == "components.md":
                continue
            text = path.read_text(encoding="utf-8")
            if "wordpress/components.md" in text or re.search(r"\]\(components\.md\)", text):
                callers.append(path.relative_to(skill).as_posix())
        self.assertEqual(callers, ["references/products/wordpress/settings.md"])
        # Registry must not expose the nested guide as a global/preloaded resource.
        registry = json.loads((skill / "product-types.json").read_text(encoding="utf-8"))
        wordpress = next(p for p in registry["products"] if p["id"] == "wordpress-plugin")
        self.assertEqual(wordpress["required_references"], ["references/products/wordpress-plugin.md"])

    def test_operational_selection_is_reachable_without_settings_guide(self):
        skill = ROOT / "skills/ui-ux-skill/references/products"
        parent = (skill / "wordpress-plugin.md").read_text(encoding="utf-8")
        settings = (skill / "wordpress/settings.md").read_text(encoding="utf-8")
        controls = (skill / "wordpress/components.md").read_text(encoding="utf-8")
        operational = parent.split("### Operational collections and detail views", 1)[1].split("### Diagnostics", 1)[0]
        operational = " ".join(operational.split())
        for term in ("DataViews", "DataForm", "conditional dataset tools", "existing build strategy", "existing native list"):
            self.assertIn(term, operational)
        # Historical source citations are not operational selection instructions.
        self.assertNotIn("For data-heavy operational collections", controls)
        self.assertNotIn("They are conditional dataset tools", controls)
        self.assertIn("components.md", settings)
        self.assertIn("including simple forms", parent)
        self.assertIn("not to settings merely because this shared parent was read", operational)
        self.assertIn("Audit-only work recommends without migration", operational)

    def test_report_rejects_contradiction_missing_method_and_evidence(self):
        report = {"schema_version": 1, "fresh_model_evaluation": False, "outcomes": []}
        for name in sorted(EXPECTED):
            method = "source-trace" if name in {"WP-10", "ISO-01", "ISO-02", "ISO-03", "ISO-04"} else "package-diff" if name == "ISO-05" else "real-admin-browser"
            report["outcomes"].append({"id": name, "status": "passed", "accepted": True, "method": method, "evidence": "actual-record", "detail": "observed outcome"})
        self.assertEqual(report_errors(report), [])
        for field, value in [("status", "failed"), ("accepted", False), ("evidence", ""), ("method", "source-trace")]:
            broken = copy.deepcopy(report)
            row = next(row for row in broken["outcomes"] if row["id"] == "WP-12")
            row[field] = value
            self.assertTrue(report_errors(broken))
        for rows in (report["outcomes"][:-1], report["outcomes"] + [report["outcomes"][0]]):
            self.assertTrue(report_errors({**report, "outcomes": rows}))
        self.assertTrue(report_errors({**report, "fresh_model_evaluation": True}))

    def test_recorded_outcomes(self):
        report = HERE / "RESULTS.json"
        self.assertTrue(report.is_file(), "Required WPS acceptance report is missing")
        result = json.loads(report.read_text(encoding="utf-8"))
        self.assertEqual(report_errors(result), [])
        self.assertEqual(set(result["candidate_skill_hashes"]), BEHAVIOR)
        r11 = json.loads((HERE / "r11-fixture-delta.json").read_text(encoding="utf-8"))
        r12 = json.loads((HERE / "r12-source-fixture-delta.json").read_text(encoding="utf-8"))
        behavior, expected_fixture = r12_successor(
            result["candidate_skill_hashes"], fixture_successor(result["fixture_hashes"], r11), r12)
        expected_fixture = r13_fixture_successor(expected_fixture, json.loads((HERE / "r13-fixture-delta.json").read_text(encoding="utf-8")))
        sys.path.insert(0, str(ROOT / "scripts"))
        from r13_source_binding import r13_predecessor
        released = r13_predecessor()
        for rel, digest in behavior.items():
            self.assertEqual(released[rel], digest)
        fixture = ROOT / "evals/fixtures/wordpress-settings/plugin"
        actual = {p.relative_to(fixture).as_posix(): hashlib.sha256(p.read_bytes() if p.suffix == ".ttf" else canonical_bytes(p)).hexdigest() for p in fixture.rglob("*") if p.is_file()}
        self.assertEqual(expected_fixture, actual)

    def test_r11_fixture_successor_rejects_missing_extra_and_wrong_parent(self):
        historical = json.loads((HERE / "RESULTS.json").read_text(encoding="utf-8"))["fixture_hashes"]
        delta = json.loads((HERE / "r11-fixture-delta.json").read_text(encoding="utf-8"))
        before = copy.deepcopy(historical)
        current = fixture_successor(historical, delta)
        self.assertEqual(before, historical)
        for name in set(historical) - {"app.js", "model.js"}:
            self.assertEqual(current[name], historical[name])
        missing = copy.deepcopy(delta); missing["changes"].pop("model.js")
        extra = copy.deepcopy(delta); extra["changes"]["style.css"] = delta["changes"]["app.js"]
        parent = copy.deepcopy(delta); parent["changes"]["app.js"]["previous_sha256"] = "0" * 64
        malformed = copy.deepcopy(delta); malformed["changes"]["app.js"]["sha256"] = "invalid"
        for bad in [missing, extra, parent, malformed, {**delta, "decision": "unrelated"}]:
            with self.assertRaises(ValueError):
                fixture_successor(historical, bad)

    def test_r11_runtime_evidence_remains_bound_to_its_historical_fixture(self):
        historical = json.loads((HERE / "RESULTS.json").read_text(encoding="utf-8"))["fixture_hashes"]
        delta = json.loads((HERE / "r11-fixture-delta.json").read_text(encoding="utf-8"))
        browser = json.loads((HERE / "evidence/r11-browser-results.json").read_text(encoding="utf-8"))
        self.assertEqual(browser["recorded_on"], "2026-10-16")
        self.assertEqual(browser["runner_sha256"], hashlib.sha256(canonical_bytes(HERE / "run_browser.cjs")).hexdigest())
        self.assertEqual(browser["fixture_hashes"], fixture_successor(historical, delta))
        self.assertEqual(browser["javascript_errors"], [])
        self.assertEqual(browser["console_warnings"], [])
        expected = {f"WP-{i:02d}" for i in range(1, 15)} - {"WP-10"}
        expected |= {"R11-CONFLICT-current", "R11-CONFLICT-minimum", "R11-CONFLICT-RTL"}
        rows = [r for r in browser["observations"] if not r["id"].startswith("VIEW-")]
        self.assertEqual(len(rows), len(expected))
        self.assertEqual({r["id"] for r in rows}, expected)
        self.assertTrue(all(r["status"] == "passed" and r["method"] == "real-admin-browser" and r["detail"] for r in rows))
        for name in ["current-en", "current-en-390", "minimum-en", "minimum-en-390", "current-fa-390"]:
            self.assertTrue((HERE / "evidence" / ("r11-conflict-" + name + ".png")).read_bytes().startswith(b"\x89PNG\r\n\x1a\n"))

    def test_r12_retains_immutable_parent_records(self):
        for name, digest in R12_PARENT_HASHES.items():
            self.assertEqual(hashlib.sha256(canonical_bytes(HERE / name)).hexdigest(), digest, name)

    def test_r12_captures_bind_actual_images(self):
        report = json.loads((HERE / "evidence/r12-browser-results.json").read_text(encoding="utf-8"))
        captures = report["captures"]
        self.assertEqual(len(captures), 11)
        names = [capture["file"] for capture in captures]
        self.assertEqual(len(set(names)), len(names))
        for capture in captures:
            name = capture["file"]
            self.assertRegex(name, r"^r12-[a-z0-9-]+\.png$")
            self.assertEqual(hashlib.sha256((HERE / "evidence" / name).read_bytes()).hexdigest(), capture["sha256"])
            self.assertFalse(capture["overflow"])

    def test_r12_runtime_records_bind_the_actual_successor_and_runners(self):
        historical = json.loads((HERE / "RESULTS.json").read_text(encoding="utf-8"))
        r11 = json.loads((HERE / "r11-fixture-delta.json").read_text(encoding="utf-8"))
        delta = json.loads((HERE / "r12-source-fixture-delta.json").read_text(encoding="utf-8"))
        behavior, fixture = r12_successor(historical["candidate_skill_hashes"],
                                          fixture_successor(historical["fixture_hashes"], r11), delta)
        for record, runner, ids in (
            ("r12-browser-results.json", "run_discovery.cjs", R12_DISCOVERY_IDS),
            ("r12-regression-results.json", "run_browser.cjs", R12_REGRESSION_IDS),
        ):
            report = json.loads((HERE / "evidence" / record).read_text(encoding="utf-8"))
            self.assertEqual(r12_runtime_errors(report, behavior, fixture,
                                               hashlib.sha256(canonical_bytes(HERE / runner)).hexdigest(), ids), [], record)

    def test_runtime_record_matches_accepted_outcomes(self):
        result = json.loads((HERE / "RESULTS.json").read_text(encoding="utf-8"))
        browser = json.loads((HERE / "evidence/browser-results.json").read_text(encoding="utf-8"))
        self.assertEqual(browser["javascript_errors"], [])
        self.assertEqual(browser["console_warnings"], [])
        self.assertEqual(browser["fixture_hashes"], result["fixture_hashes"])
        observed = {row["id"]: row for row in browser["observations"] if row["id"].startswith("WP-")}
        self.assertEqual(set(observed), {f"WP-{i:02d}" for i in range(1, 15)} - {"WP-10"})
        for row in result["outcomes"]:
            if row["method"] == "real-admin-browser":
                self.assertEqual(row["detail"], observed[row["id"]]["detail"])
        for name in ["persian-simple-1440.png", "persian-simple-390.png", "persian-multi-1440.png", "persian-multi-390.png", "persian-reset-dialog-390.png", "persian-zoom-200.png"]:
            self.assertTrue((HERE / "evidence" / name).read_bytes().startswith(b"\x89PNG\r\n\x1a\n"))

    def test_consumer_verification_rejects_bad_checksum_and_changed_source(self):
        import verify_packages
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill = root / "skills/ui-ux-skill"
            skill.mkdir(parents=True)
            (root / "VERSION").write_text("3.4.0\n", encoding="utf-8")
            (skill / "VERSION").write_text("3.4.0\n", encoding="utf-8")
            (skill / "SKILL.md").write_text("protected\n", encoding="utf-8")
            notice = canonical_bytes(ROOT / "LICENSE")
            (skill / "LICENSE").write_bytes(notice)
            (root / "LICENSE").write_bytes(notice)
            sums = []
            for plugin in [False, True]:
                name = "ui-ux-plugin-v3.4.0.zip" if plugin else "ui-ux-skill-claude-v3.4.0.zip"
                prefix = "ui-ux/skills/ui-ux-skill/" if plugin else "ui-ux-skill/"
                with zipfile.ZipFile(root / name, "w") as zipped:
                    for file in skill.iterdir():
                        zipped.write(file, prefix + file.name)
                    if plugin:
                        for rel in ["plugin.json", "assets/logo.svg", "assets/composer-icon.svg", "LICENSE", "PRIVACY.md", "TERMS.md", "SUPPORT.md"]:
                            file = root / rel
                            file.parent.mkdir(parents=True, exist_ok=True)
                            file.write_bytes(notice if rel == "LICENSE" else b"test\n")
                            zipped.write(file, "ui-ux/" + rel)
                sums.append(hashlib.sha256((root / name).read_bytes()).hexdigest() + "  " + name)
            manifest = root / "SHA256SUMS.txt"
            manifest.write_text("\n".join(sums), encoding="utf-8")
            with patch.object(verify_packages, "ROOT", root):
                self.assertEqual(len(verify_packages.verify(root)["checks"]), 2)
                standalone = root / "ui-ux-skill-claude-v3.4.0.zip"
                good_archive = standalone.read_bytes()
                for replacement in (None, b"", notice[:80], notice.replace(b"Pooya Hayati", b"Wrong owner")):
                    with zipfile.ZipFile(standalone, "w") as zipped:
                        for file in skill.iterdir():
                            if file.name == "LICENSE":
                                if replacement is not None:
                                    zipped.writestr("ui-ux-skill/LICENSE", replacement)
                            else:
                                zipped.write(file, "ui-ux-skill/" + file.name)
                    corrected = [hashlib.sha256(standalone.read_bytes()).hexdigest() + "  " + standalone.name, sums[1]]
                    manifest.write_text("\n".join(corrected), encoding="utf-8")
                    with self.assertRaisesRegex(ValueError, "license"):
                        verify_packages.verify(root)
                standalone.write_bytes(good_archive)
                manifest.write_text("\n".join(sums), encoding="utf-8")
                manifest.write_text("\n".join(sums).replace(sums[0][:64], "0" * 64), encoding="utf-8")
                with self.assertRaises(ValueError):
                    verify_packages.verify(root)
                manifest.write_text("\n".join(sums), encoding="utf-8")
                (skill / "SKILL.md").write_text("changed\n", encoding="utf-8")
                with self.assertRaises(ValueError):
                    verify_packages.verify(root)


class R12SuccessorContracts(unittest.TestCase):
    def setUp(self):
        historical = json.loads((HERE / "RESULTS.json").read_text(encoding="utf-8"))
        r11 = json.loads((HERE / "r11-fixture-delta.json").read_text(encoding="utf-8"))
        self.behavior = historical["candidate_skill_hashes"]
        self.wps_fixture = historical["fixture_hashes"]
        self.fixture = fixture_successor(self.wps_fixture, r11)
        # Synthetic hashes exercise the contract only. They are never written
        # as candidate evidence or accepted runtime results.
        self.delta = {
            "schema_version": 1, "normalization": "git-lf",
            "decision": "docs/R12_EXECUTION.md#authority", "authorized_on": "2026-11-01",
            "parents": dict(R12_PARENT_HASHES),
            "skill_changes": {name: {"previous_sha256": self.behavior[name], "sha256": "a" * 64}
                              for name in BEHAVIOR},
            "fixture_changes": {name: {"previous_sha256": self.fixture.get(name), "sha256": "b" * 64}
                                for name in R12_FIXTURE_CHANGES},
        }

    def test_successor_preserves_parents_and_unchanged_fixture(self):
        before = copy.deepcopy((self.behavior, self.fixture, self.delta))
        behavior, fixture = r12_successor(self.behavior, self.fixture, self.delta)
        self.assertEqual(before, (self.behavior, self.fixture, self.delta))
        self.assertEqual(set(behavior), BEHAVIOR)
        self.assertEqual(set(fixture) - set(self.fixture), {"discovery.js", "workspace.js"})
        for name in set(self.fixture) - R12_FIXTURE_CHANGES:
            self.assertEqual(fixture[name], self.fixture[name])
        with self.assertRaises(ValueError):
            r12_successor(behavior, fixture, self.delta)  # Not a replayable blanket exemption.

    def test_rejects_missing_extra_wrong_parent_and_malformed_changes(self):
        for group in ("skill_changes", "fixture_changes"):
            name = next(iter(self.delta[group]))
            mutations = []
            missing = copy.deepcopy(self.delta); missing[group].pop(name); mutations.append(missing)
            extra = copy.deepcopy(self.delta); extra[group]["unexpected.js"] = {"sha256": "a" * 64}; mutations.append(extra)
            parent = copy.deepcopy(self.delta); parent[group][name]["previous_sha256"] = "0" * 64; mutations.append(parent)
            no_parent = copy.deepcopy(self.delta); no_parent[group][name].pop("previous_sha256"); mutations.append(no_parent)
            malformed = copy.deepcopy(self.delta); malformed[group][name]["sha256"] = "not-a-hash"; mutations.append(malformed)
            unchanged = copy.deepcopy(self.delta); unchanged[group][name]["sha256"] = unchanged[group][name]["previous_sha256"]; mutations.append(unchanged)
            for bad in mutations:
                with self.subTest(group=group, delta=bad):
                    with self.assertRaises(ValueError):
                        r12_successor(self.behavior, self.fixture, bad)
        with self.assertRaises(ValueError):
            r12_successor(self.behavior, self.wps_fixture, self.delta)  # Cannot bypass the R11 parent.

    def test_rejects_changed_authority_or_parent_records(self):
        for field, value in (("schema_version", 2), ("normalization", "none"),
                             ("decision", "inherited permission"), ("authorized_on", "2026-10-16"),
                             ("parents", {}), ("parents", {**R12_PARENT_HASHES, "RESULTS.json": "0" * 64})):
            with self.subTest(field=field):
                with self.assertRaises(ValueError):
                    r12_successor(self.behavior, self.fixture, {**self.delta, field: value})

    def test_runtime_rejects_stale_sources_runners_missing_or_failed_observations(self):
        behavior, fixture = r12_successor(self.behavior, self.fixture, self.delta)
        runner_hash = "c" * 64
        for ids in (R12_DISCOVERY_IDS, R12_REGRESSION_IDS):
            report = {
                **json.loads((HERE / "evidence/r12-browser-results.json").read_text(encoding="utf-8")),
                "schema_version": 1, "recorded_on": "2026-11-01", "runner_sha256": runner_hash,
                "behavior_hashes": behavior, "fixture_hashes": fixture,
                "javascript_errors": [], "console_warnings": [],
                "observations": [{"id": name, "status": "passed", "method": "real-admin-browser", "detail": "Synthetic contract-test observation"}
                                 for name in sorted(ids)],
            }
            self.assertEqual(r12_runtime_errors(report, behavior, fixture, runner_hash, ids), [])
            for field, value in (
                ("schema_version", 0), ("recorded_on", "2026-10-16"), ("recorded_on", "2026-02-30"),
                ("behavior_hashes", self.behavior), ("fixture_hashes", self.fixture),
                ("runner_sha256", "0" * 64), ("javascript_errors", ["error"]), ("console_warnings", None),
                ("observations", None), ("observations", [None]),
                ("observations", report["observations"][:-1]),
                ("observations", report["observations"] + [report["observations"][0]]),
            ):
                self.assertTrue(r12_runtime_errors({**report, field: value}, behavior, fixture, runner_hash, ids), field)
            for field, value in (("id", "unexpected"), ("id", {}), ("status", "failed"), ("detail", " ")):
                broken = copy.deepcopy(report)
                broken["observations"][0][field] = value
                self.assertTrue(r12_runtime_errors(broken, behavior, fixture, runner_hash, ids), field)
            with_view = copy.deepcopy(report)
            with_view["observations"].append({"id": "VIEW-primary", "status": "passed", "method": "real-admin-browser", "detail": "View checked"})
            self.assertEqual(r12_runtime_errors(with_view, behavior, fixture, runner_hash, ids), [])
            with_view["observations"][-1]["detail"] = {"viewport": 390, "scrollWidth": 390}
            self.assertEqual(r12_runtime_errors(with_view, behavior, fixture, runner_hash, ids), [])
            with_view["observations"][-1]["detail"] = {}
            self.assertTrue(r12_runtime_errors(with_view, behavior, fixture, runner_hash, ids))
            with_view["observations"][-1]["detail"] = "View checked"
            malformed_detail = copy.deepcopy(report)
            malformed_detail["observations"][0]["detail"] = {"claim": "passed"}
            self.assertTrue(r12_runtime_errors(malformed_detail, behavior, fixture, runner_hash, ids))
            with_view["observations"][-1]["status"] = "failed"
            self.assertTrue(r12_runtime_errors(with_view, behavior, fixture, runner_hash, ids))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-root", type=Path)
    parser.add_argument("--check-report", type=Path)
    parser.add_argument("--current-source", action="store_true", help="Include the authorized post-WPS source deltas; default checks the original WPS checkpoint")
    args, rest = parser.parse_known_args()
    if args.skill_root or args.check_report:
        baseline = json.loads((HERE / "baseline.json").read_text(encoding="utf-8"))
        if args.current_source:
            baseline = active_source_baseline()
        failures = isolation_errors(args.skill_root, baseline) if args.skill_root else report_errors(json.loads(args.check_report.read_text(encoding="utf-8")))
        for failure in failures:
            print(failure, file=sys.stderr)
        raise SystemExit(bool(failures))
    unittest.main(argv=[sys.argv[0], *rest])
