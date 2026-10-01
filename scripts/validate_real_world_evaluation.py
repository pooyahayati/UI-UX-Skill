#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "ui-ux-skill"
EVALS = ROOT / "evals"
REAL = EVALS / "real-world"

errors: list[str] = []

def error(message: str) -> None:
    errors.append(message)

def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        error(f"Cannot parse {path.relative_to(ROOT)}: {exc}")
        return {}

manifest = load_json(REAL / "manifest.json")
result = load_json(REAL / "result.json")
cases_manifest = load_json(EVALS / "cases.json")
product_registry = load_json(SKILL / "product-types.json")
shared_registry = load_json(SKILL / "shared-rules.json")
design_registry = load_json(SKILL / "design-system.json")

if manifest.get("schema_version") != 1:
    error("real-world manifest schema_version must be 1")

cases = manifest.get("cases", [])
if len(cases) != 5:
    error(f"real-world evaluation must contain exactly 5 cases; got {len(cases)}")

expected_routes = {
    "dashboard",
    "website",
    "web-application",
    "mobile-application",
    "wordpress-plugin",
}
routes = {x.get("product_route") for x in cases if isinstance(x, dict)}
if routes != expected_routes:
    error(f"real-world product coverage mismatch: {sorted(routes)}")

case_defs = {
    item.get("id"): item
    for item in cases_manifest.get("cases", [])
    if isinstance(item, dict) and item.get("id")
}
registered_products = {
    item.get("id")
    for item in product_registry.get("products", [])
    if isinstance(item, dict)
}
shared_ids = {
    item.get("id")
    for item in shared_registry.get("modules", [])
    if isinstance(item, dict)
}
design_ids = {
    item.get("id")
    for item in design_registry.get("modules", [])
    if isinstance(item, dict)
}

for item in cases:
    case_id = item.get("id")
    route = item.get("product_route")
    fixture = item.get("fixture")

    if case_id not in case_defs:
        error(f"real-world case missing from evals/cases.json: {case_id}")
        continue
    if case_defs[case_id].get("fixture") != fixture:
        error(f"{case_id}: fixture mismatch between manifests")

    fixture_dir = EVALS / "fixtures" / str(fixture)
    if not fixture_dir.is_dir() or not (fixture_dir / "README.md").is_file():
        error(f"{case_id}: missing fixture or README: {fixture}")

    if route not in registered_products:
        error(f"{case_id}: unregistered product route: {route}")

    refs = item.get("product_refs", [])
    if not refs:
        error(f"{case_id}: product_refs must not be empty")
    for ref in refs:
        if not (SKILL / ref).is_file():
            error(f"{case_id}: missing product reference: {ref}")

    rule_ids = item.get("shared_rules", [])
    if not rule_ids:
        error(f"{case_id}: shared_rules must not be empty")
    for rule_id in rule_ids:
        if rule_id not in shared_ids:
            error(f"{case_id}: unknown shared rule: {rule_id}")

    design_modules = item.get("design_system", [])
    if not design_modules:
        error(f"{case_id}: design_system must not be empty")
    for module_id in design_modules:
        if module_id not in design_ids:
            error(f"{case_id}: unknown design-system module: {module_id}")

if result.get("skillVersion") != cases_manifest.get("version"):
    error("real-world result skillVersion must match eval manifest version")
if result.get("host") != "ChatGPT":
    error("recorded Stage 6 result must identify the actual host")
if result.get("model") != "GPT-5.6 Sol":
    error("recorded Stage 6 result must identify the actual model")
if result.get("evaluationMode") != "in-session source-based behavioral evaluation":
    error("recorded Stage 6 evaluation mode is missing or inconsistent")

notes = (result.get("notes") or "").casefold()
for term in ["not an independent", "browser", "render"]:
    if term not in notes:
        error(f"real-world result notes must disclose limitation term: {term}")

recorded = {
    item.get("id"): item
    for item in result.get("cases", [])
    if isinstance(item, dict) and item.get("id")
}
expected_ids = {x.get("id") for x in cases}
if set(recorded) != expected_ids:
    error("real-world result must record exactly the five manifest cases")

for case_id in sorted(expected_ids):
    item = recorded.get(case_id, {})
    if item.get("result") == "fail":
        error(f"{case_id}: blocking fail is not allowed")
    if item.get("result") not in {"pass", "partial", "not-testable"}:
        error(f"{case_id}: invalid overall result")

    expected_invariants = case_defs[case_id].get("invariants", [])
    rec_invariants = item.get("invariants", [])
    rec_by_text = {x.get("text"): x for x in rec_invariants if isinstance(x, dict)}

    for inv in expected_invariants:
        rec = rec_by_text.get(inv)
        if not rec:
            error(f"{case_id}: missing invariant record: {inv}")
            continue
        if rec.get("result") == "fail":
            error(f"{case_id}: invariant failed: {inv}")
        if rec.get("result") not in {"pass", "partial", "not-testable"}:
            error(f"{case_id}: invalid invariant result: {inv}")
        if not (rec.get("evidence") or "").strip():
            error(f"{case_id}: invariant missing evidence: {inv}")

results_md = (REAL / "RESULTS.md").read_text(encoding="utf-8") if (REAL / "RESULTS.md").is_file() else ""
for term in [
    "Dashboard",
    "Website",
    "Web Application",
    "Mobile Application",
    "WordPress Plugin",
    "Rendered/browser/device validation was not available",
    "Blocking failures: **0**",
]:
    if term.casefold() not in results_md.casefold():
        error(f"RESULTS.md missing Stage 6 evidence term: {term}")

if errors:
    print("Real-world evaluation validation failed:")
    for item in errors:
        print(f"- {item}")
    raise SystemExit(1)

print("Real-world evaluation validation passed: 5 products, 0 blocking failures.")
