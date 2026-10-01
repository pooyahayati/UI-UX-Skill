#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "ui-ux-skill"
REGISTRY = SKILL / "product-types.json"

REQUIRED_PRODUCT_IDS = {
    "website",
    "dashboard",
    "web-application",
    "mobile-application",
    "wordpress-plugin",
    "generic-product-ui",
}

PRIMARY_PACKS = {
    "website": "references/products/website.md",
    "dashboard": "references/products/dashboard.md",
    "web-application": "references/products/web-application.md",
    "mobile-application": "references/products/mobile-application.md",
    "wordpress-plugin": "references/products/wordpress-plugin.md",
    "generic-product-ui": "references/product-routing.md",
}

LOCAL_MODULES = {
    "website": [
        "references/products/website/structure-navigation.md",
        "references/products/website/conversion-trust.md",
        "references/products/website/content-seo.md",
        "references/products/website/media-performance.md",
        "references/products/website/accessibility-localization-qa.md",
    ],
    "dashboard": [
        "references/products/dashboard/executive.md",
        "references/products/dashboard/analytical.md",
        "references/products/dashboard/operational.md",
        "references/products/dashboard/monitoring-noc.md",
        "references/products/dashboard/crm-pipeline.md",
        "references/products/dashboard/admin-management.md",
    ],
    "web-application": [
        "references/products/web-application/navigation-state.md",
        "references/products/web-application/workflows-data.md",
        "references/products/web-application/interaction-access.md",
    ],
    "mobile-application": [
        "references/products/mobile/ios.md",
        "references/products/mobile/android.md",
        "references/products/mobile/cross-platform.md",
    ],
    "wordpress-plugin": [
        "references/products/wordpress/settings.md",
        "references/products/wordpress/onboarding-integrations.md",
        "references/products/wordpress/diagnostics-operations.md",
        "references/products/wordpress/multisite-admin.md",
    ],
}

errors: list[str] = []


def error(message: str) -> None:
    errors.append(message)


def read(rel: str) -> str:
    path = SKILL / rel
    if not path.is_file():
        error(f"missing required file: {rel}")
        return ""
    return path.read_text(encoding="utf-8")


try:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
except Exception as exc:
    print(f"ERROR: cannot parse product-types.json: {exc}", file=sys.stderr)
    raise SystemExit(1)

if data.get("schema_version") != 1:
    error("product-types.json schema_version must be 1")

policy = data.get("policy", {})
for key in [
    "classification_required",
    "require_primary_route",
    "product_rules_are_mandatory",
    "load_only_active_product_packs",
    "internal_product_modules_are_parent_routed",
]:
    if policy.get(key) is not True:
        error(f"product routing policy must require {key}")

if policy.get("preload_inactive_product_knowledge") is not False:
    error("inactive product knowledge must not be preloaded")

if policy.get("fallback_route") != "generic-product-ui":
    error("generic-product-ui must remain the fallback route")

products = data.get("products")
if not isinstance(products, list) or not products:
    error("product-types.json must contain products")
    products = []

seen: set[str] = set()
fallback_count = 0

for item in products:
    if not isinstance(item, dict):
        error("each product route must be an object")
        continue

    product_id = item.get("id")
    if not product_id:
        error("product route missing id")
        continue
    if product_id in seen:
        error(f"duplicate product route id: {product_id}")
    seen.add(product_id)

    if item.get("fallback_only"):
        fallback_count += 1
        if product_id != "generic-product-ui":
            error(f"{product_id}: only generic-product-ui may be fallback_only")

    triggers = item.get("triggers")
    if not isinstance(triggers, list) or not triggers:
        error(f"{product_id}: missing triggers")

    refs = item.get("required_references")
    expected = [PRIMARY_PACKS.get(product_id)]
    if refs != expected:
        error(
            f"{product_id}: required_references must contain only its top-level Product Pack; "
            f"expected={expected!r}, found={refs!r}"
        )

    for key in item:
        if key != "required_references" and "reference" in key.casefold():
            error(
                f"{product_id}: global registry leaks internal product routing via {key}; "
                "internal modules must be parent-routed"
            )

    for ref in refs or []:
        read(ref)

missing = REQUIRED_PRODUCT_IDS - seen
if missing:
    error(f"missing required product routes: {sorted(missing)}")
if seen - REQUIRED_PRODUCT_IDS:
    error(f"unexpected product routes: {sorted(seen - REQUIRED_PRODUCT_IDS)}")
if fallback_count != 1:
    error(f"exactly one fallback_only route is required; found {fallback_count}")

for product_id, refs in LOCAL_MODULES.items():
    parent_ref = PRIMARY_PACKS[product_id]
    parent_text = read(parent_ref)
    parent_folded = parent_text.casefold()

    if "shared-product-rules.md" not in parent_text:
        error(f"{parent_ref}: must route shared behavior through shared-product-rules.md")
    if "shared-rule boundary" not in parent_folded and "routing contract" not in parent_folded:
        error(f"{parent_ref}: missing compact routing/shared boundary")

    for ref in refs:
        module_text = read(ref)
        short = ref.removeprefix("references/products/")
        if short.casefold() not in parent_folded:
            error(f"{parent_ref}: does not route to local module {short}")

        if "load only" not in module_text.casefold():
            error(f"{ref}: local module must explicitly require scope-based loading")

for product_id, parent_ref in PRIMARY_PACKS.items():
    if product_id == "generic-product-ui":
        continue
    text = read(parent_ref).casefold()
    for other_id, other_refs in LOCAL_MODULES.items():
        if other_id == product_id:
            continue
        for ref in other_refs:
            short = ref.removeprefix("references/products/").casefold()
            if short in text:
                error(
                    f"{parent_ref}: routes to inactive product module {short}; "
                    "cross-product modules must stay isolated"
                )

coverage_terms = {
    "website": [
        "website subtype and visitor job",
        "website decision brief",
        "structure-navigation.md",
        "conversion-trust.md",
        "content-seo.md",
        "media-performance.md",
        "accessibility-localization-qa.md",
    ],
    "dashboard": [
        "required dashboard mode routing",
        "dashboard/executive.md",
        "dashboard/analytical.md",
        "dashboard/operational.md",
        "dashboard/monitoring-noc.md",
        "dashboard/crm-pipeline.md",
        "dashboard/admin-management.md",
    ],
    "web-application": [
        "navigation-state.md",
        "workflows-data.md",
        "interaction-access.md",
        "browser history",
        "autosave",
        "concurrency",
    ],
    "mobile-application": [
        "required mobile routing",
        "mobile/ios.md",
        "mobile/android.md",
        "mobile/cross-platform.md",
    ],
    "wordpress-plugin": [
        "required wordpress routing",
        "wordpress/settings.md",
        "wordpress/onboarding-integrations.md",
        "wordpress/diagnostics-operations.md",
        "wordpress/multisite-admin.md",
    ],
}

for product_id, terms in coverage_terms.items():
    text = read(PRIMARY_PACKS[product_id]).casefold()
    for term in terms:
        if term.casefold() not in text:
            error(f"{PRIMARY_PACKS[product_id]} missing routing/coverage term: {term}")

routing = read("references/product-routing.md").casefold()
for term in [
    "product isolation",
    "inactive product knowledge is out of scope",
    "load only the `required_references` for active routes",
    "internal dashboard modes",
    "generic-product-ui",
]:
    if term.casefold() not in routing:
        error(f"product-routing.md missing required isolation policy: {term}")

skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8").casefold()
for term in [
    "product isolation",
    "product-types.json",
    "references/product-routing.md",
    "do not load another product pack",
    "product-specific references are discovered through the active product pack",
]:
    if term.casefold() not in skill_text:
        error(f"SKILL.md missing thin-head/product-isolation contract: {term}")

if errors:
    print("Product route validation failed:")
    for item in errors:
        print(f"- {item}")
    raise SystemExit(1)

print("Product route validation passed: active-pack isolation and parent-routed local modules enforced.")
