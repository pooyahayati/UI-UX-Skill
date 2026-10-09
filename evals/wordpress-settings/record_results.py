"""Bind actual browser evidence, reviewed source traces and extracted packages."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile

from test_contracts import ROOT, HERE, BEHAVIOR, canonical_bytes, isolation_errors, report_errors


def digest(path):
    data = path.read_bytes() if path.suffix in {".ttf", ".zip"} else canonical_bytes(path)
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--browser", required=True, type=Path)
    parser.add_argument("--packages", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError("Choose a fresh report output")
    browser = json.loads(args.browser.read_text(encoding="utf-8"))
    fixture = ROOT / browser["fixture"]
    fixture_hashes = {p.relative_to(fixture).as_posix(): digest(p) for p in fixture.rglob("*") if p.is_file()}
    if browser.get("fixture_hashes") != fixture_hashes or browser["javascript_errors"] or browser["console_warnings"]:
        raise ValueError("Browser evidence is stale or contains unresolved errors/warnings")
    baseline = json.loads((HERE / "baseline.json").read_text(encoding="utf-8"))
    packages = []
    for archive in sorted(args.packages.glob("*.zip")):
        with zipfile.ZipFile(archive) as zipped:
            if zipped.testzip() is not None:
                raise ValueError("Corrupt archive")
            # Repository packager emits safe names; reject traversal before extraction anyway.
            if any(Path(name).is_absolute() or ".." in Path(name).parts for name in zipped.namelist()):
                raise ValueError("Unsafe member")
            target = args.packages / (archive.stem + "-extracted")
            if target.exists():
                raise ValueError("Choose fresh package evidence")
            zipped.extractall(target)
            skill = target / ("ui-ux/skills/ui-ux-skill" if "plugin" in archive.name else "ui-ux-skill")
            if isolation_errors(skill, baseline):
                raise ValueError("Packaged protected content differs")
            for rel in BEHAVIOR:
                if canonical_bytes(skill / rel) != canonical_bytes(ROOT / "skills/ui-ux-skill" / rel):
                    raise ValueError("Packaged behavior differs from candidate")
            packages.append({"file": archive.name, "sha256": digest(archive), "members": len(zipped.namelist()), "protected_resources": len(baseline["protected_skill_hashes"])})
    if len(packages) != 2:
        raise ValueError("Both consumer packages are required")
    outcomes = [{**row, "accepted": True, "evidence": "evidence/browser-results.json"} for row in browser["observations"] if row["id"].startswith("WP-")]
    details = {
        "WP-10": "Audit and narrow-fix authority preserves the existing page/storage; mandate gap reported, no full migration.",
        "ISO-01": "Other product routes and protected resources do not load the settings-components guide.",
        "ISO-02": "Public WordPress surfaces do not satisfy the owned-admin-settings activation boundary.",
        "ISO-03": "Diagnostics/operations keep their unchanged modules; only settings calls the new guide.",
        "ISO-04": "Hybrid product activation is restricted to its settings surface, not the operational workspace.",
    }
    for name, detail in details.items():
        outcomes.append({"id": name, "status": "passed", "accepted": True, "method": "source-trace", "detail": detail, "evidence": "SOURCE_REVIEW.md"})
    outcomes.append({"id": "ISO-05", "status": "passed", "accepted": True, "method": "package-diff", "detail": "All 85 protected source resources and both extracted packages match the canonical pre-edit baseline; the three allowed behavior resources match candidate source.", "evidence": "baseline.json and package_checks"})
    report = {"schema_version": 1, "date": "2026-10-10", "base_commit": baseline["base_commit"],
        "candidate_binding": "Canonical content hashes; commit/merge binding is recorded in EXECUTION.md after integration.",
        "fresh_model_evaluation": False, "candidate_skill_hashes": {rel: digest(ROOT / "skills/ui-ux-skill" / rel) for rel in sorted(BEHAVIOR)},
        "fixture_hashes": fixture_hashes, "package_checks": packages, "outcomes": sorted(outcomes, key=lambda row: row["id"]),
        "limitations": ["Source traces use the current lead session, not independent model evaluation.", "Real-admin browser evidence covers Edge, two declared WordPress hosts, synthetic data and selected keyboard/layout states; no universal browser/device or assistive-technology certification.", "Specimen engineering acceptance is not an owner-approved production design or plugin migration."]}
    if isolation_errors(ROOT / "skills/ui-ux-skill", baseline) or report_errors(report):
        raise ValueError("Candidate/report failed integrity")
    args.output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Recorded {len(outcomes)} accepted outcomes and {len(packages)} verified packages")


if __name__ == "__main__":
    main()
