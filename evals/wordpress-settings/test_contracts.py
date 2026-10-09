"""Dedicated WPS source/isolation and evidence-integrity checks, not model evaluation."""
from __future__ import annotations

import argparse
import copy
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
        baseline = json.loads((HERE / "baseline.json").read_text(encoding="utf-8"))
        self.assertEqual(isolation_errors(ROOT / "skills/ui-ux-skill", baseline), [])

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
        for rel, digest in result["candidate_skill_hashes"].items():
            self.assertEqual(hashlib.sha256(canonical_bytes(ROOT / "skills/ui-ux-skill" / rel)).hexdigest(), digest)
        fixture = ROOT / "evals/fixtures/wordpress-settings/plugin"
        actual = {p.relative_to(fixture).as_posix(): hashlib.sha256(p.read_bytes() if p.suffix == ".ttf" else canonical_bytes(p)).hexdigest() for p in fixture.rglob("*") if p.is_file()}
        self.assertEqual(result["fixture_hashes"], actual)

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
                            file.write_text("test\n", encoding="utf-8")
                            zipped.write(file, "ui-ux/" + rel)
                sums.append(hashlib.sha256((root / name).read_bytes()).hexdigest() + "  " + name)
            manifest = root / "SHA256SUMS.txt"
            manifest.write_text("\n".join(sums), encoding="utf-8")
            with patch.object(verify_packages, "ROOT", root):
                self.assertEqual(len(verify_packages.verify(root)["checks"]), 2)
                manifest.write_text("\n".join(sums).replace(sums[0][:64], "0" * 64), encoding="utf-8")
                with self.assertRaises(ValueError):
                    verify_packages.verify(root)
                manifest.write_text("\n".join(sums), encoding="utf-8")
                (skill / "SKILL.md").write_text("changed\n", encoding="utf-8")
                with self.assertRaises(ValueError):
                    verify_packages.verify(root)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill-root", type=Path)
    parser.add_argument("--check-report", type=Path)
    args, rest = parser.parse_known_args()
    if args.skill_root or args.check_report:
        failures = isolation_errors(args.skill_root, json.loads((HERE / "baseline.json").read_text(encoding="utf-8"))) if args.skill_root else report_errors(json.loads(args.check_report.read_text(encoding="utf-8")))
        for failure in failures:
            print(failure, file=sys.stderr)
        raise SystemExit(bool(failures))
    unittest.main(argv=[sys.argv[0], *rest])
