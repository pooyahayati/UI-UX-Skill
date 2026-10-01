#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals"
manifest = json.loads((EVALS / "cases.json").read_text(encoding="utf-8"))
errors: list[str] = []

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
}
existing = {p.name for p in (EVALS / "fixtures").iterdir() if p.is_dir()}
missing = sorted(required_fixtures - existing)
if missing:
    errors.append(f"Missing required fixtures: {', '.join(missing)}")

if len(manifest.get("cases", [])) < 10:
    errors.append("Expected at least 10 behavioral eval cases")

if errors:
    print("Behavioral eval fixture validation failed:")
    for item in errors:
        print(f"- {item}")
    sys.exit(1)

print(f"Behavioral eval fixtures valid: {len(manifest['cases'])} cases, {len(existing)} fixtures.")
