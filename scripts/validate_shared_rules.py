#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "ui-ux-skill"
REGISTRY = SKILL / "shared-rules.json"
ROUTER = SKILL / "references" / "shared-product-rules.md"

EXPECTED = {
    "navigation-wayfinding": "references/shared/navigation-wayfinding.md",
    "forms-data-entry": "references/shared/forms-data-entry.md",
    "feedback-status": "references/shared/feedback-status.md",
    "state-recovery": "references/shared/state-recovery.md",
    "destructive-high-impact-actions": "references/shared/destructive-high-impact-actions.md",
    "accessibility-interaction": "references/shared/accessibility-interaction.md",
    "responsive-adaptation": "references/shared/responsive-adaptation.md",
    "motion": "references/shared/motion.md",
    "content-hierarchy-progressive-disclosure": "references/shared/content-hierarchy-progressive-disclosure.md",
}

PRODUCT_PACKS = [
    "references/products/website.md",
    "references/products/dashboard.md",
    "references/products/web-application.md",
    "references/products/mobile-application.md",
    "references/products/wordpress-plugin.md",
]

errors: list[str] = []


def error(message: str) -> None:
    errors.append(message)


try:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
except Exception as exc:
    print(f"ERROR: cannot parse shared-rules.json: {exc}", file=sys.stderr)
    raise SystemExit(1)

if data.get("schema_version") != 1:
    error("shared-rules.json schema_version must be 1")

policy = data.get("policy", {})
for key in [
    "local_rules_only",
    "load_after_product_route",
    "require_scope_based_loading",
    "product_pack_specializes_shared_rules",
    "shared_rules_define_cross_product_contracts",
    "product_pack_must_not_weaken_accessibility_security_or_data_integrity",
]:
    if policy.get(key) is not True:
        error(f"shared-rules policy must require {key}")

modules = data.get("modules", [])
if not isinstance(modules, list):
    error("shared-rules.json modules must be a list")
    modules = []

by_id = {
    item.get("id"): item
    for item in modules
    if isinstance(item, dict) and item.get("id")
}

if set(by_id) != set(EXPECTED):
    error(
        "shared-rules.json must contain exactly the expected shared modules; "
        f"found={sorted(by_id)}"
    )

for module_id, ref in EXPECTED.items():
    item = by_id.get(module_id, {})
    if item.get("reference") != ref:
        error(f"{module_id}: expected reference {ref}")
    triggers = item.get("triggers")
    if (
        not isinstance(triggers, list)
        or not triggers
        or any(not isinstance(x, str) or not x.strip() for x in triggers)
    ):
        error(f"{module_id}: triggers must be a non-empty list of strings")
    if not (SKILL / ref).is_file():
        error(f"{module_id}: shared rule file missing: {ref}")

router_text = ROUTER.read_text(encoding="utf-8") if ROUTER.is_file() else ""
for term in [
    "Authority and precedence",
    "Load strategy",
    "Non-duplication rule",
    "Product Pack may specialize",
    "Do not load the full shared set by default",
    "must not weaken",
]:
    if term.casefold() not in router_text.casefold():
        error(f"shared-product-rules.md missing required term: {term}")

for ref in EXPECTED.values():
    short = ref.replace("references/", "")
    if short.casefold() not in router_text.casefold():
        error(f"shared-product-rules.md does not route to {short}")

skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
for term in ["shared-rules.json", "references/shared-product-rules.md", "do not load every Shared Rule"]:
    if term.casefold() not in skill_text.casefold():
        error(f"SKILL.md missing scope-based Shared Rule routing: {term}")

routing_text = (SKILL / "references/product-routing.md").read_text(encoding="utf-8")
for term in ["shared-rules.json", "shared-product-rules.md", "load only scope-relevant Shared Rules"]:
    if term.casefold() not in routing_text.casefold():
        error(f"product-routing.md missing shared-rule contract: {term}")

for rel in PRODUCT_PACKS:
    text = (SKILL / rel).read_text(encoding="utf-8")
    folded = text.casefold()

    if "shared-product-rules.md" not in text:
        error(f"{rel} must route to shared-product-rules.md")

    if "## shared rule loading" in folded:
        error(f"{rel} still contains the duplicated Shared rule loading block")

    if "shared-rule boundary" not in folded and "routing contract" not in folded:
        error(f"{rel} must contain a compact Shared Rule boundary/routing contract")

accessibility = (SKILL / "references/accessibility.md").read_text(encoding="utf-8")
if "shared/accessibility-interaction.md" not in accessibility:
    error("accessibility.md must distinguish QA/evidence from the shared interaction contract")

theme = (SKILL / "references/theme-responsive-brand.md").read_text(encoding="utf-8")
for term in [
    "shared/responsive-adaptation.md",
    "shared/motion.md",
    "shared/navigation-wayfinding.md",
]:
    if term not in theme:
        error(f"theme-responsive-brand.md must route to {term}")

if errors:
    print("Shared rule validation failed:")
    for item in errors:
        print(f"- {item}")
    raise SystemExit(1)

print("Shared rule validation passed: one canonical router, scope-based loading, no duplicated pack-level loading blocks.")
