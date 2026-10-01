#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "ui-ux-skill"
REGISTRY = SKILL / "design-system.json"
ROUTER = SKILL / "references" / "design-system-architecture.md"

EXPECTED = {
    "tokens-foundations": "references/design-system/tokens-foundations.md",
    "typography": "references/design-system/typography.md",
    "color-theme": "references/design-system/color-theme.md",
    "spacing-density-layout": "references/design-system/spacing-density-layout.md",
    "component-states": "references/design-system/component-states.md",
    "responsive-variants": "references/design-system/responsive-variants.md",
    "governance-migration": "references/design-system/governance-migration.md",
}

errors: list[str] = []

def error(message: str) -> None:
    errors.append(message)

try:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
except Exception as exc:
    print(f"ERROR: cannot parse design-system.json: {exc}", file=sys.stderr)
    raise SystemExit(1)

if data.get("schema_version") != 1:
    error("design-system.json schema_version must be 1")

if data.get("stable_token_interchange") != "DTCG 2025.10":
    error("design-system.json must record DTCG 2025.10 as the stable token interchange baseline")

modules = data.get("modules", [])
if not isinstance(modules, list):
    error("design-system.json modules must be a list")
    modules = []

by_id = {
    item.get("id"): item
    for item in modules
    if isinstance(item, dict) and item.get("id")
}

if set(by_id) != set(EXPECTED):
    error(f"design-system.json module set mismatch: {sorted(by_id)}")

for module_id, ref in EXPECTED.items():
    item = by_id.get(module_id, {})
    if item.get("reference") != ref:
        error(f"{module_id}: expected reference {ref}")
    if not (SKILL / ref).is_file():
        error(f"{module_id}: module file missing: {ref}")

architecture = data.get("architecture", {})
required_order = [
    "design-profile",
    "primitive-tokens",
    "semantic-tokens",
    "component-tokens",
    "product-variants",
    "resolved-runtime-tokens",
    "components",
    "product-surfaces",
]
if architecture.get("order") != required_order:
    error("design-system architecture order is missing or inconsistent")

required_floors = {
    "accessibility",
    "security",
    "authorization",
    "truthful-state",
    "data-integrity",
}
if set(architecture.get("protected_floors", [])) != required_floors:
    error("design-system protected floors are missing or inconsistent")

router = ROUTER.read_text(encoding="utf-8") if ROUTER.is_file() else ""
for term in [
    "../design-system.json",
    "Primitive Tokens -> Semantic Tokens -> Component Tokens -> Product Variants",
    "Required module routing",
    "DTCG 2025.10",
    "Authority and precedence",
    "Design-system defaults vs runtime settings",
    "RTL/LTR",
    "Testing changeability",
    "Visual regression",
]:
    if term.casefold() not in router.casefold():
        error(f"design-system-architecture.md missing required term: {term}")

for ref in EXPECTED.values():
    short = ref.replace("references/", "")
    if short.casefold() not in router.casefold():
        error(f"design-system-architecture.md does not route to {short}")

checks = {
    "tokens-foundations.md": [
        "Primitive tokens",
        "Semantic tokens",
        "Component tokens",
        "Product variants",
        "$value",
        "$type",
        "Aliases",
        "DTCG 2025.10",
        "Source vs resolved tokens",
    ],
    "typography.md": [
        "Typography roles",
        "Role contract",
        "Numeric/data typography",
        "Persian and Latin",
        "Responsive typography",
    ],
    "color-theme.md": [
        "Primitive Palette -> Semantic Color Roles -> Component/State Roles",
        "Light",
        "Dark",
        "High Contrast / Forced Colors",
        "Forced colors",
        "Owner-configurable palettes",
    ],
    "spacing-density-layout.md": [
        "Spacing scale",
        "Semantic spacing",
        "Density",
        "Control sizing",
        "Radius hierarchy",
        "Elevation",
    ],
    "component-states.md": [
        "default",
        "hover",
        "focus-visible",
        "disabled",
        "read-only",
        "loading / busy",
        "State token model",
        "Theme matrix",
    ],
    "responsive-variants.md": [
        "Responsive architecture",
        "Breakpoints",
        "Responsive token resolution",
        "Product variants",
        "Variant precedence",
        "Variant explosion",
    ],
    "governance-migration.md": [
        "Proposed -> Active -> Deprecated -> Migration/Alias -> Removed",
        "Deprecation",
        "Aliases during migration",
        "Breaking change",
        "Token impact analysis",
        "Runtime configuration boundary",
        "Visual regression compatibility",
    ],
}

for filename, terms in checks.items():
    path = SKILL / "references" / "design-system" / filename
    text = path.read_text(encoding="utf-8") if path.is_file() else ""
    for term in terms:
        if term.casefold() not in text.casefold():
            error(f"{filename} missing design-system contract term: {term}")

skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
for term in [
    "design-system.json",
    "references/design-system-architecture.md",
]:
    if term not in skill_text:
        error(f"SKILL.md missing design-system routing: {term}")

runtime = (SKILL / "references/runtime-ui-governance.md").read_text(encoding="utf-8")
for term in [
    "semantic tokens",
    "arbitrary CSS",
    "Preview",
    "Validate",
    "Publish",
]:
    if term.casefold() not in runtime.casefold():
        error(f"runtime-ui-governance.md missing boundary term: {term}")

rtl = (SKILL / "references/rtl-ltr-typography.md").read_text(encoding="utf-8")
if "design-system/typography.md" not in rtl:
    error("rtl-ltr-typography.md must route typography-system work to design-system/typography.md")
if "CSS logical" not in rtl and "logical properties" not in rtl.casefold():
    error("rtl-ltr-typography.md must retain logical-direction guidance")

visual = (SKILL / "references/visual-regression.md").read_text(encoding="utf-8")
for term in [
    "semantic color",
    "typography",
    "density",
    "component state",
    "product variant",
]:
    if term.casefold() not in visual.casefold():
        error(f"visual-regression.md missing design-system impact dimension: {term}")

if errors:
    print("Design-system validation failed:")
    for item in errors:
        print(f"- {item}")
    raise SystemExit(1)

print("Design-system validation passed.")
