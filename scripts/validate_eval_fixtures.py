#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from xml.etree import ElementTree as ET
from baseline_binding import validate_baseline

ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals"
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
manifest = json.loads((EVALS / "cases.json").read_text(encoding="utf-8"))
errors: list[str] = []

if manifest.get("version") != VERSION:
    errors.append("evals/cases.json version must match VERSION")

seen: set[str] = set()
for case in manifest.get("cases", []):
    case_id = case.get("id")
    if not case_id or case_id in seen:
        errors.append(f"Invalid or duplicate case id: {case_id!r}")
    seen.add(case_id)

    if case.get("type") not in {"positive", "negative"}:
        errors.append(f"{case_id}: invalid type")

    if not case.get("prompt"):
        errors.append(f"{case_id}: missing prompt")

    invariants = case.get("invariants")
    if not isinstance(invariants, list) or not invariants:
        errors.append(f"{case_id}: missing invariants")

    fixture = case.get("fixture")
    if fixture:
        fixture_dir = EVALS / "fixtures" / fixture
        if not fixture_dir.is_dir():
            errors.append(f"{case_id}: missing fixture {fixture}")
        elif not (fixture_dir / "README.md").is_file():
            errors.append(f"{case_id}: fixture {fixture} is missing README.md")

required_fixtures = {
    "existing-dashboard",
    "owner-config",
    "rtl-table",
    "analytics-dashboard",
    "realtime-ops",
    "real-world-dashboard",
    "real-world-website",
    "real-world-web-app",
    "real-world-mobile",
    "real-world-wordpress",
    "discovery-brief",
    "legacy-handbook",
    "sample-review",
    "incremental-design",
    "executable-baseline",
    "runtime-appearance-brief",
}
existing = {p.name for p in (EVALS / "fixtures").iterdir() if p.is_dir()}
for case_id, raw in (("runtime-appearance-admin-planning", "ADMIN.md"),
                     ("runtime-appearance-icon-planning", "ICONS.md"),
                     ("runtime-appearance-narrow-boundary", "NARROW.md"),
                     ("runtime-appearance-no-admin-boundary", "NO_ADMIN.md"),
                     ("runtime-appearance-persian-font-upload", "PERSIAN_FONT.md"),
                     ("runtime-appearance-preserve-approved-font", "FONT_EXISTING.md")):
    case = next((c for c in manifest.get("cases", []) if c.get("id") == case_id), None)
    if not case or case.get("fixture") != "runtime-appearance-brief":
        errors.append(f"Missing raw appearance planning case: {case_id}")
    if not (EVALS / "fixtures/runtime-appearance-brief" / raw).is_file():
        errors.append(f"Appearance planning fixture missing {raw}")
missing = sorted(required_fixtures - existing)
if missing:
    errors.append(f"Missing required fixtures: {', '.join(missing)}")

if len(manifest.get("cases", [])) < 10:
    errors.append("Expected at least 10 behavioral eval cases")

required_isolation_cases = {
    "product-isolation-website",
    "product-isolation-dashboard",
    "product-isolation-web-application",
    "product-isolation-mobile-application",
    "product-isolation-wordpress-plugin",
}
missing_isolation = sorted(required_isolation_cases - seen)
if missing_isolation:
    errors.append(
        "Missing explicit product-isolation eval cases: " + ", ".join(missing_isolation)
    )

# Resource/manifest coverage only; this does not execute a model or score discovery.
required_discovery_cases = {
    "discovery-novice-recommendations", "discovery-known-decisions",
    "discovery-reference-uncertainty", "discovery-missing-reference",
    "discovery-language-not-conversation", "discovery-bilingual-foundation",
    "discovery-scoped-choice-authority", "discovery-narrow-scope",
}
missing_discovery = sorted(required_discovery_cases - seen)
if missing_discovery:
    errors.append("Missing discovery eval cases: " + ", ".join(missing_discovery))
for case in manifest.get("cases", []):
    if case.get("id") in required_discovery_cases and case.get("fixture") != "discovery-brief":
        errors.append(f"{case['id']}: must use the raw discovery-brief fixture")
discovery = EVALS / "fixtures" / "discovery-brief"
if not (discovery / "BRIEF.md").is_file():
    errors.append("Discovery fixture missing BRIEF.md")
try:
    reference = ET.parse(discovery / "reference.svg").getroot()
    if reference.tag != "{http://www.w3.org/2000/svg}svg":
        errors.append("Discovery reference must be SVG")
except (OSError, ET.ParseError) as exc:
    errors.append(f"Discovery reference missing or invalid: {exc}")
if (discovery / "unavailable-reference.png").exists():
    errors.append("Missing-reference scenario must retain its absent attachment")

# Handbook artifacts/forward inputs only; no model or product migration is run.
handbook_cases = {
    "handbook-initial-draft": "discovery-brief",
    "handbook-legacy-compatible": "legacy-handbook",
    "handbook-conflicting-authority": "legacy-handbook",
    "handbook-runtime-separation": "legacy-handbook",
}
for case_id, fixture in handbook_cases.items():
    case = next((c for c in manifest["cases"] if c.get("id") == case_id), None)
    if case is None or case.get("fixture") != fixture:
        errors.append(f"{case_id}: missing handbook case or wrong raw fixture")
legacy = EVALS / "fixtures/legacy-handbook"
for name in ("PROJECT.md", "OWNER.md", "design-profile.md", "ui-tokens.json",
             "tools/profile_reader.py", "variants/conflicting-design.md"):
    if not (legacy / name).is_file():
        errors.append(f"Handbook fixture missing {name}")
try:
    json.loads((legacy / "ui-tokens.json").read_text(encoding="utf-8"))
except (OSError, ValueError) as exc:
    errors.append(f"Handbook token source missing or invalid: {exc}")

# Forward-input availability only, not model conformance or visual approval.
sample_cases = {
    "samples-primary-foundation-proposal", "samples-approved-secondary-language",
    "samples-primary-executable-refinement", "samples-stale-scoped-approval",
    "samples-rendering-unavailable", "samples-narrow-change-no-redesign",
    "samples-dark-after-primary-approval", "samples-secondary-needs-approval",
    "samples-monolingual-no-extra-layout",
}
for case_id in sample_cases:
    case = next((c for c in manifest["cases"] if c.get("id") == case_id), None)
    if case is None or case.get("fixture") != "sample-review":
        errors.append(f"{case_id}: missing sample case or wrong raw fixture")
for name in ("README.md", "BRIEF.md", "OWNER_NOTES.md", "FOUNDATION.json", "variants/bilingual.md",
             "variants/revision-change.md"):
    if not (EVALS / "fixtures/sample-review" / name).is_file():
        errors.append(f"Sample-review fixture missing {name}")

try:
    foundation = json.loads((EVALS / "fixtures/sample-review/FOUNDATION.json").read_text(encoding="utf-8"))
    if not isinstance(foundation, dict):
        errors.append("Sample-review foundation must be a JSON object")
except (OSError, ValueError) as exc:
    errors.append(f"Sample-review foundation missing or invalid: {exc}")

# Continuation input availability only; no agent behavior is executed here.
incremental_cases = {
    "incremental-new-design-need", "incremental-reuse-settled-foundation",
    "incremental-strategic-preference", "incremental-stale-conflicting-return",
    "incremental-agent-unavailable",
}
for case_id in incremental_cases:
    case = next((c for c in manifest["cases"] if c.get("id") == case_id), None)
    if case is None or case.get("fixture") != "incremental-design":
        errors.append(f"{case_id}: missing continuation case or wrong raw fixture")
continuation = EVALS / "fixtures/incremental-design"
for name in ("README.md", "BRIEF.md", "DESIGN.md", "OWNER_NOTES.md", "ui-tokens.json"):
    if not (continuation / name).is_file():
        errors.append(f"Continuation fixture missing {name}")
try:
    if not isinstance(json.loads((continuation / "ui-tokens.json").read_text(encoding="utf-8")), dict):
        errors.append("Continuation token source must be a JSON object")
except (OSError, ValueError) as exc:
    errors.append(f"Continuation token source missing or invalid: {exc}")

for case in manifest.get("cases", []):
    if case.get("id") not in required_isolation_cases:
        continue
    invariants = " ".join(case.get("invariants", [])).casefold()
    for term in ["does not load", "shared rules", "design system", "intentionally not loaded"]:
        if term not in invariants:
            errors.append(f"{case.get('id')}: isolation eval missing invariant term: {term}")

# Exact positive source/handbook input availability, never agent conformance.
positive_baseline = next((c for c in manifest["cases"] if c.get("id") == "incremental-executable-baseline"), None)
if positive_baseline is None or positive_baseline.get("fixture") != "executable-baseline":
    errors.append("Missing exact executable continuation baseline case")
errors.extend(validate_baseline(EVALS / "fixtures/executable-baseline"))

if errors:
    print("Behavioral eval fixture validation failed:")
    for item in errors:
        print(f"- {item}")
    sys.exit(1)

print(f"Behavioral eval fixtures valid: {len(manifest['cases'])} cases, {len(existing)} fixtures.")
