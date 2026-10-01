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

errors: list[str] = []


def error(message: str) -> None:
    errors.append(message)


try:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
except Exception as exc:
    print(f"ERROR: cannot parse product-types.json: {exc}", file=sys.stderr)
    raise SystemExit(1)

if data.get("schema_version") != 1:
    error("product-types.json schema_version must be 1")

policy = data.get("policy", {})
if policy.get("classification_required") is not True:
    error("product classification must be required")
if policy.get("require_primary_route") is not True:
    error("a primary product route must be required")
if policy.get("product_rules_are_mandatory") is not True:
    error("Product Pack rules must be mandatory")
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

    label = item.get("label")
    triggers = item.get("triggers")
    refs = item.get("required_references")

    if not isinstance(label, str) or not label.strip():
        error(f"{product_id}: missing label")
    if not isinstance(triggers, list) or not triggers:
        error(f"{product_id}: missing triggers")
    if not isinstance(refs, list) or not refs:
        error(f"{product_id}: missing required_references")

    if item.get("fallback_only"):
        fallback_count += 1
        if product_id != policy.get("fallback_route"):
            error(f"{product_id}: only configured fallback may use fallback_only")

    for ref in refs or []:
        if not isinstance(ref, str) or not ref.startswith("references/") or not ref.endswith(".md"):
            error(f"{product_id}: invalid Product Pack reference: {ref!r}")
            continue
        path = SKILL / ref
        if not path.is_file():
            error(f"{product_id}: missing Product Pack: {ref}")
            continue

        text = path.read_text(encoding="utf-8")
        if product_id != "generic-product-ui":
            activation = f"active product route includes `{product_id}`"
            if activation.casefold() not in text.casefold():
                error(
                    f"{product_id}: Product Pack must state that it applies only when "
                    f"the active route includes {product_id}"
                )

missing = REQUIRED_PRODUCT_IDS - seen
if missing:
    error(f"missing required product routes: {sorted(missing)}")

if fallback_count != 1:
    error(f"exactly one fallback_only route is required; found {fallback_count}")

skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
for required_term in [
    "product-types.json",
    "references/product-routing.md",
    "dashboard",
    "web-application",
    "mobile-application",
    "wordpress-plugin",
]:
    if required_term.casefold() not in skill_text.casefold():
        error(f"SKILL.md missing product-routing term: {required_term}")

routing = (SKILL / "references" / "product-routing.md").read_text(encoding="utf-8")
for required_term in [
    "MUST be classified by product type",
    "required_references",
    "primary product route",
    "Multiple product routes",
    "generic-product-ui",
]:
    if required_term.casefold() not in routing.casefold():
        error(f"product-routing.md missing required policy: {required_term}")

if errors:
    print("Product route validation failed:")
    for item in errors:
        print(f"- {item}")
    raise SystemExit(1)

print("Product route validation passed.")
