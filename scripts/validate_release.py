#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

from roadmap_policy import validate_policy

ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "ui-ux-skill"
SKILL = ROOT / "skills" / SKILL_NAME
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
ERRORS: list[str] = []


def error(message: str) -> None:
    ERRORS.append(message)


def require(path: str) -> Path:
    target = ROOT / path
    if not target.exists():
        error(f"Missing required release path: {path}")
    return target


def require_text(text: str, terms: list[str], label: str) -> None:
    folded = text.casefold()
    for term in terms:
        if term.casefold() not in folded:
            error(f"{label} missing required term: {term}")


# Release/package surface only. Product-specific structure is owned by dedicated validators.
for path in [
    "README.md",
    "CHANGELOG.md",
    "ROADMAP.md",
    "INSTALL.md",
    "LICENSE",
    "VERSION",
    "plugin.json",
    "assets/logo.svg",
    "assets/composer-icon.svg",
    f"skills/{SKILL_NAME}/SKILL.md",
    f"skills/{SKILL_NAME}/VERSION",
    f"skills/{SKILL_NAME}/product-types.json",
    f"skills/{SKILL_NAME}/shared-rules.json",
    f"skills/{SKILL_NAME}/design-system.json",
    f"skills/{SKILL_NAME}/specialists.json",
    f"skills/{SKILL_NAME}/agents/openai.yaml",
    f"skills/{SKILL_NAME}/references/design-handbook.md",
    f"skills/{SKILL_NAME}/assets/templates/DESIGN.md",
    "submission/TEST_CASES.md",
    "submission/SUBMISSION_CHECKLIST.md",
    "evals/cases.json",
    "evals/result.schema.json",
    "evals/real-world/manifest.json",
    "evals/real-world/result.json",
    "scripts/package_release.py",
    "scripts/validate_product_routes.py",
    "scripts/validate_shared_rules.py",
    "scripts/validate_design_system.py",
    "scripts/validate_specialists.py",
    "scripts/validate_eval_fixtures.py",
    "scripts/validate_real_world_evaluation.py",
    "scripts/validate_eval_result.py",
    "scripts/roadmap_policy.py",
    "scripts/test_roadmap_policy.py",
    "scripts/test_handbook_migration.py",
]:
    require(path)

if not re.fullmatch(r"\d+\.\d+\.\d+", VERSION):
    error(f"VERSION must use x.y.z semantic versioning; got {VERSION!r}")

skill_version_path = SKILL / "VERSION"
if skill_version_path.is_file():
    skill_version = skill_version_path.read_text(encoding="utf-8").strip()
    if skill_version != VERSION:
        error(
            "Installed Skill VERSION does not match repository VERSION; "
            f"skill={skill_version!r}, repository={VERSION!r}"
        )
    if not re.fullmatch(r"\d+\.\d+\.\d+", skill_version):
        error(f"Installed Skill VERSION must use x.y.z semantic versioning; got {skill_version!r}")
else:
    error("Installed Skill must contain VERSION at its Skill root")

# Canonical source must remain singular.
for old in ["SKILL.md", "agents", "references"]:
    if (ROOT / old).exists():
        error(f"Duplicate root Skill source still exists: {old}")
if (ROOT / "skills" / "production-dashboard-ui-ux-skill").exists():
    error("Legacy Skill path still exists")

# Thin Head/frontmatter release contract.
skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
if not skill_text.startswith("---\n"):
    error("SKILL.md must start with YAML frontmatter")
else:
    parts = skill_text.split("---", 2)
    if len(parts) != 3:
        error("SKILL.md frontmatter is not closed")
    else:
        fm = parts[1].strip().splitlines()
        keys = [line.split(":", 1)[0].strip() for line in fm if ":" in line]
        if keys != ["name", "description"]:
            error(f"SKILL.md frontmatter must contain only name and description; got {keys}")
        name = next((line.split(":", 1)[1].strip() for line in fm if line.startswith("name:")), "")
        description = next((line.split(":", 1)[1].strip() for line in fm if line.startswith("description:")), "")
        if name != SKILL_NAME:
            error(f"Unexpected Skill name: {name}")
        if not description or len(description) > 1024:
            error("Skill description must be 1..1024 characters")
        if "Use " not in description or "Do not use" not in description:
            error("Skill description must say when to use and when not to use it")

body_lines = skill_text.split("---", 2)[-1].splitlines()
if len(body_lines) >= 500:
    error(f"SKILL.md body should stay under 500 lines; got {len(body_lines)}")

require_text(
    skill_text,
    [
        "## Installed version",
        "`VERSION` at the Skill root",
        "read that local `VERSION` file",
        "Do not infer the installed version",
    ],
    "SKILL.md installed-version contract",
)

# Plugin manifest and directory-facing metadata.
try:
    manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
except Exception as exc:
    manifest = {}
    error(f"Cannot parse plugin.json: {exc}")

if manifest.get("version") != VERSION:
    error("plugin.json version does not match VERSION")
if manifest.get("name") != "ui-ux":
    error("plugin.json name must be ui-ux")

interface = manifest.get("extensions", {}).get("com.openai", {}).get("interface", {})
display_name = interface.get("displayName", "")
short = interface.get("shortDescription", "")
long_desc = interface.get("longDescription", "")
developer = interface.get("developerName", "")

if not display_name or len(display_name) > 30:
    error("Plugin displayName must be 1..30 characters")
if not short or len(short) > 30 or "\n" in short:
    error("Plugin shortDescription must be one line and <=30 characters")
if not long_desc or len(long_desc) > 4000:
    error("Plugin longDescription must be 1..4000 characters")
if not developer or len(developer) > 80 or "\n" in developer:
    error("Plugin developerName must be one line and <=80 characters")
if manifest.get("author", {}).get("name") not in {"", developer}:
    error("plugin author.name and interface.developerName should match")

require_text(
    long_desc,
    ["active local Product Pack", "scope-relevant local modules", "Shared Product UI Rules", "Design System"],
    "Plugin longDescription",
)
if re.search(r"\bVersion\s+\d+", long_desc, re.I):
    error("Plugin longDescription must remain version-agnostic")

allowed_categories = {
    "Productivity",
    "Creativity",
    "Developer Tools",
    "Business & Operations",
    "Data & Analytics",
    "Communication",
    "Education & Research",
    "Security",
    "Finance",
    "Healthcare",
    "Travel",
    "Entertainment",
    "Other",
}
if interface.get("category") not in allowed_categories:
    error("Plugin category is missing or unsupported")

capabilities = interface.get("capabilities", [])
if not isinstance(capabilities, list) or len(capabilities) > 20:
    error("Plugin capabilities must be a list of at most 20 entries")
elif any(not isinstance(x, str) or not x.strip() or len(x) > 120 or "\n" in x for x in capabilities):
    error("Plugin capabilities violate directory limits")

prompts = interface.get("defaultPrompt", [])
if not isinstance(prompts, list) or len(prompts) > 3:
    error("Plugin defaultPrompt must be a list of at most 3 prompts")
else:
    normalized: set[str] = set()
    for prompt in prompts:
        if (
            not isinstance(prompt, str)
            or not prompt.strip()
            or len(prompt) > 128
            or "\n" in prompt
            or "@" in prompt
        ):
            error(f"Invalid starter prompt: {prompt!r}")
            continue
        key = " ".join(prompt.split()).casefold()
        if key in normalized:
            error("Duplicate starter prompt")
        normalized.add(key)

for field in ["websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"]:
    value = interface.get(field, "")
    if value and not value.startswith("https://"):
        error(f"{field} must use HTTPS")


def validate_svg(field: str) -> None:
    rel = interface.get(field)
    if not rel or not rel.startswith("./"):
        error(f"{field} must be a ./ relative asset path")
        return
    path = ROOT / rel[2:]
    if not path.is_file():
        error(f"{field} asset missing: {rel}")
        return
    try:
        root = ET.fromstring(path.read_text(encoding="utf-8"))
    except Exception as exc:
        error(f"{field} SVG cannot be parsed: {exc}")
        return
    if not root.tag.endswith("svg"):
        error(f"{field} root must be svg")
    viewbox = root.attrib.get("viewBox")
    width = root.attrib.get("width")
    height = root.attrib.get("height")
    if viewbox:
        try:
            vals = [float(x) for x in viewbox.split()]
        except ValueError:
            vals = []
        if len(vals) != 4 or vals[2] != vals[3] or vals[2] < 48:
            error(f"{field} viewBox must be square and >=48")
    elif width and height:
        try:
            w, h = float(width), float(height)
            if w != h or w < 48:
                error(f"{field} dimensions must be square and >=48")
        except ValueError:
            error(f"{field} dimensions must be numeric")
    else:
        error(f"{field} SVG needs numeric viewBox or dimensions")


validate_svg("logo")
validate_svg("composerIcon")

# README is the concise public entrypoint.
readme = (ROOT / "README.md").read_text(encoding="utf-8")
if len(readme.splitlines()) > 120:
    error(f"README should stay concise (<=120 lines); got {len(readme.splitlines())}")

require_text(
    readme,
    [
        "## Product coverage",
        "| **Website** |",
        "| **Dashboard** |",
        "| **Web Application** |",
        "| **Mobile Application** |",
        "| **WordPress Plugin / Admin UI** |",
        "| **Shared foundation** |",
        "Inactive Product Packs are not preloaded",
        "## Feature freeze",
        "persian-writing",
        "UI/UX Head",
        "Shared UI Rules",
        "Design System",
        "[Roadmap](ROADMAP.md)",
        "[How to Install / Update](INSTALL.md)",
        "[Updates & Changelog](CHANGELOG.md)",
        "[Skill Specification](skills/ui-ux-skill/SKILL.md)",
        "[Product Registry](skills/ui-ux-skill/product-types.json)",
        "[Shared UI Registry](skills/ui-ux-skill/shared-rules.json)",
        "[Design System Registry](skills/ui-ux-skill/design-system.json)",
        "[Specialist Routing](skills/ui-ux-skill/references/specialist-routing.md)",
    ],
    "README",
)
if "## Core capabilities" in readme:
    error("README must not contain the legacy Core capabilities list")
if f"**v{VERSION}**" not in readme:
    error("README current-source version does not match VERSION")
if f"version-{VERSION}-blue" not in readme:
    error("README version badge does not match VERSION")

# Installation/migration entrypoint.
install = (ROOT / "INSTALL.md").read_text(encoding="utf-8")
require_text(
    install,
    [
        "https://github.com/pooyahayati/UI-UX-Skill/tree/main/skills/ui-ux-skill",
        "$ui-ux-skill",
        "/ui-ux-skill",
        "production-dashboard-ui-ux-skill",
        "ui-ux-skill",
        "skills/ui-ux-skill/VERSION",
        "installed Skill root",
        "persian-writing",
    ],
    "INSTALL.md",
)

# Submission shape remains stable.
tests = (ROOT / "submission/TEST_CASES.md").read_text(encoding="utf-8")
positive_section, _, negative_section = tests.partition("## Negative test cases")
positive_count = len(re.findall(r"^### \d+\.", positive_section, re.M))
negative_count = len(re.findall(r"^### \d+\.", negative_section, re.M))
if positive_count != 5 or negative_count != 3:
    error(f"Submission tests must be exactly 5 positive and 3 negative; got {positive_count}+{negative_count}")
if tests.count("**Expected result format**") != 8:
    error("Every submission test needs Expected result format")
if tests.count("**Fixtures / test data**") != 8:
    error("Every submission test needs Fixtures / test data")
require_text(tests, ["Public-facing business website", "Unsafe owner customization"], "submission/TEST_CASES.md")

submission_checklist = (ROOT / "submission/SUBMISSION_CHECKLIST.md").read_text(encoding="utf-8")
require_text(
    submission_checklist,
    [
        "Machine-readable Shared Product UI Rule registry",
        "Machine-readable Design System registry",
        "Five-product real-world evaluation",
        "Persian-writing is the only external specialist",
    ],
    "submission/SUBMISSION_CHECKLIST.md",
)

# Preserved history, bounded correction exception, and canonical progress.
roadmap = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
ERRORS.extend(validate_policy(readme, roadmap))

# Current version must have a changelog entry. During development, newer work may remain Unreleased.
changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
if f"## [{VERSION}]" not in changelog:
    error(f"CHANGELOG missing current VERSION entry: {VERSION}")

if ERRORS:
    print("Release metadata validation failed:")
    for item in ERRORS:
        print(f"- {item}")
    sys.exit(1)

print(f"Release metadata validation passed for v{VERSION}.")
