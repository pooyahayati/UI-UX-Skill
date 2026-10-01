#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "ui-ux-skill"
SKILL = ROOT / "skills" / SKILL_NAME
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
ERRORS: list[str] = []

def error(msg: str) -> None:
    ERRORS.append(msg)

def require(path: str) -> Path:
    p = ROOT / path
    if not p.exists():
        error(f"Missing required path: {path}")
    return p

required = [
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
    f"skills/{SKILL_NAME}/product-types.json",
    f"skills/{SKILL_NAME}/specialists.json",
    f"skills/{SKILL_NAME}/shared-rules.json",
    f"skills/{SKILL_NAME}/design-system.json",
    f"skills/{SKILL_NAME}/agents/openai.yaml",
    f"skills/{SKILL_NAME}/references/design-system/tokens-foundations.md",
    f"skills/{SKILL_NAME}/references/design-system/typography.md",
    f"skills/{SKILL_NAME}/references/design-system/color-theme.md",
    f"skills/{SKILL_NAME}/references/design-system/spacing-density-layout.md",
    f"skills/{SKILL_NAME}/references/design-system/component-states.md",
    f"skills/{SKILL_NAME}/references/design-system/responsive-variants.md",
    f"skills/{SKILL_NAME}/references/design-system/governance-migration.md",
    f"skills/{SKILL_NAME}/references/shared-product-rules.md",
    f"skills/{SKILL_NAME}/references/shared/navigation-wayfinding.md",
    f"skills/{SKILL_NAME}/references/shared/forms-data-entry.md",
    f"skills/{SKILL_NAME}/references/shared/feedback-status.md",
    f"skills/{SKILL_NAME}/references/shared/state-recovery.md",
    f"skills/{SKILL_NAME}/references/shared/destructive-high-impact-actions.md",
    f"skills/{SKILL_NAME}/references/shared/accessibility-interaction.md",
    f"skills/{SKILL_NAME}/references/shared/responsive-adaptation.md",
    f"skills/{SKILL_NAME}/references/shared/motion.md",
    f"skills/{SKILL_NAME}/references/shared/content-hierarchy-progressive-disclosure.md",
    f"skills/{SKILL_NAME}/references/product-routing.md",
    f"skills/{SKILL_NAME}/references/products/website.md",
    f"skills/{SKILL_NAME}/references/products/website/structure-navigation.md",
    f"skills/{SKILL_NAME}/references/products/website/conversion-trust.md",
    f"skills/{SKILL_NAME}/references/products/website/content-seo.md",
    f"skills/{SKILL_NAME}/references/products/website/media-performance.md",
    f"skills/{SKILL_NAME}/references/products/website/accessibility-localization-qa.md",
    f"skills/{SKILL_NAME}/references/products/dashboard.md",
    f"skills/{SKILL_NAME}/references/products/dashboard/executive.md",
    f"skills/{SKILL_NAME}/references/products/dashboard/analytical.md",
    f"skills/{SKILL_NAME}/references/products/dashboard/operational.md",
    f"skills/{SKILL_NAME}/references/products/dashboard/monitoring-noc.md",
    f"skills/{SKILL_NAME}/references/products/dashboard/crm-pipeline.md",
    f"skills/{SKILL_NAME}/references/products/dashboard/admin-management.md",
    f"skills/{SKILL_NAME}/references/products/web-application.md",
    f"skills/{SKILL_NAME}/references/products/web-application/navigation-state.md",
    f"skills/{SKILL_NAME}/references/products/web-application/workflows-data.md",
    f"skills/{SKILL_NAME}/references/products/web-application/interaction-access.md",
    f"skills/{SKILL_NAME}/references/products/mobile-application.md",
    f"skills/{SKILL_NAME}/references/products/mobile/ios.md",
    f"skills/{SKILL_NAME}/references/products/mobile/android.md",
    f"skills/{SKILL_NAME}/references/products/mobile/cross-platform.md",
    f"skills/{SKILL_NAME}/references/products/wordpress-plugin.md",
    f"skills/{SKILL_NAME}/references/products/wordpress/settings.md",
    f"skills/{SKILL_NAME}/references/products/wordpress/onboarding-integrations.md",
    f"skills/{SKILL_NAME}/references/products/wordpress/diagnostics-operations.md",
    f"skills/{SKILL_NAME}/references/products/wordpress/multisite-admin.md",
    f"skills/{SKILL_NAME}/references/specialist-routing.md",
    f"skills/{SKILL_NAME}/references/discovery-and-profile.md",
    f"skills/{SKILL_NAME}/references/existing-product-audit.md",
    f"skills/{SKILL_NAME}/references/execution-safety.md",
    f"skills/{SKILL_NAME}/references/design-system-architecture.md",
    f"skills/{SKILL_NAME}/references/implementation-strategies.md",
    f"skills/{SKILL_NAME}/references/visual-regression.md",
    f"skills/{SKILL_NAME}/references/ux-evidence-and-metrics.md",
    f"skills/{SKILL_NAME}/references/runtime-ui-governance.md",
    f"skills/{SKILL_NAME}/references/personalization-and-data-ux.md",
    f"skills/{SKILL_NAME}/references/preference-reconciliation.md",
    f"skills/{SKILL_NAME}/references/operational-interaction-patterns.md",
    f"skills/{SKILL_NAME}/references/domain-patterns.md",
    f"skills/{SKILL_NAME}/references/accessibility.md",
    f"skills/{SKILL_NAME}/references/performance.md",
    f"skills/{SKILL_NAME}/references/qa-checklist.md",
    "submission/TEST_CASES.md",
    "submission/SUBMISSION_CHECKLIST.md",
    "evals/README.md",
    "evals/cases.json",
    "evals/result.schema.json",
    "evals/RESULT_TEMPLATE.md",
    "evals/real-world/README.md",
    "evals/real-world/manifest.json",
    "evals/real-world/result.json",
    "evals/real-world/RESULTS.md",
    "scripts/prepare_eval_run.py",
    "scripts/validate_product_routes.py",
    "scripts/validate_shared_rules.py",
    "scripts/validate_design_system.py",
    "scripts/validate_specialists.py",
    "scripts/validate_real_world_evaluation.py",
    "scripts/validate_eval_fixtures.py",
    "scripts/validate_eval_result.py",
]
for path in required:
    require(path)

for old in ["SKILL.md", "agents", "references"]:
    if (ROOT / old).exists():
        error(f"Duplicate root Skill source still exists: {old}")

legacy_skill = ROOT / "skills" / "production-dashboard-ui-ux-skill"
if legacy_skill.exists():
    error("Legacy Skill path still exists; v2 canonical source must be skills/ui-ux-skill/")

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
        for term in ["personalization", "runtime design governance", "visual QA"]:
            if term.casefold() not in description.casefold():
                error(f"Skill description should cover {term}")

for term in ["persian-writing", "Head-delegated", "Higher-level Engineering Head", "product-types.json", "product-routing.md", "shared-rules.json", "shared-product-rules.md", "design-system.json", "design-system-architecture.md"]:
    if term.casefold() not in skill_text.casefold():
        error(f"SKILL.md missing v3.0 routing contract term: {term}")

# v2.0 thin-head specialist routing:
# the Head should contain routing/governance, not copied specialist methodology.
product_registry_path = SKILL / "product-types.json"
try:
    product_registry = json.loads(product_registry_path.read_text(encoding="utf-8"))
except Exception as exc:
    product_registry = {}
    error(f"Cannot parse product-types.json: {exc}")

product_ids = {
    item.get("id")
    for item in product_registry.get("products", [])
    if isinstance(item, dict)
}
for product_id in [
    "website",
    "dashboard",
    "web-application",
    "mobile-application",
    "wordpress-plugin",
    "generic-product-ui",
]:
    if product_id not in product_ids:
        error(f"Product route registry missing {product_id}")

registry_path = SKILL / "specialists.json"
try:
    specialist_registry = json.loads(registry_path.read_text(encoding="utf-8"))
except Exception as exc:
    specialist_registry = {}
    error(f"Cannot parse specialists.json: {exc}")

registry_items = {
    item.get("id"): item
    for item in specialist_registry.get("specialists", [])
    if isinstance(item, dict)
}

external_ids = set(registry_items)
if external_ids != {"persian-writing"}:
    error(
        "Only persian-writing may remain as an external specialist; "
        f"found: {sorted(external_ids)}"
    )
persian_route = registry_items.get("persian-writing", {})
if persian_route.get("requirement") != "required":
    error("Specialist registry missing required persian-writing route")
if persian_route.get("canonical_repository") != "ali2000hos/persian-writing":
    error("persian-writing must use its canonical upstream repository")
if any(key in persian_route for key in ["version", "tag", "commit", "sha", "pinned_ref"]):
    error("persian-writing registry entry must not pin a version/ref")

routing_path = SKILL / "references" / "specialist-routing.md"
routing_text = routing_path.read_text(encoding="utf-8") if routing_path.exists() else ""
for term in [
    "Non-duplication rule",
    "Skill freshness and update policy",
    "Do not pin a specialist version",
    "latest available stable version",
]:
    if term.casefold() not in routing_text.casefold():
        error(f"Specialist routing guidance missing: {term}")

# Specialist references must stay version-agnostic unless an explicit compatibility exception is documented.
for pattern in [
    r"persian-writing[^\n]{0,120}\bv?\d+\.\d+(?:\.\d+)?\b",
    r"/releases/tag/",
    r"/commit/[0-9a-f]{7,40}",
]:
    if re.search(pattern, routing_text, re.I):
        error("Specialist routing must not pin a specialist version/tag/commit without an explicit compatibility exception")

body_lines = skill_text.split("---", 2)[-1].splitlines()
if len(body_lines) >= 500:
    error(f"SKILL.md body should stay under 500 lines; got {len(body_lines)}")

for ref in sorted(set(re.findall(r"references/[a-z0-9-]+\.md", skill_text))):
    if not (SKILL / ref).exists():
        error(f"Referenced file missing: {ref}")

for ref in [
    "references/specialist-routing.md",
    "references/design-system-architecture.md",
    "references/runtime-ui-governance.md",
    "references/personalization-and-data-ux.md",
    "references/preference-reconciliation.md",
    "references/visual-regression.md",
    "references/ux-evidence-and-metrics.md",
    "references/implementation-strategies.md",
    "references/operational-interaction-patterns.md",
    "references/domain-patterns.md",
]:
    if ref not in skill_text:
        error(f"SKILL.md does not route to required v3.0 reference: {ref}")

manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
if manifest.get("version") != VERSION:
    error("plugin.json version does not match VERSION")

if manifest.get("name") != "ui-ux":
    error("plugin.json name must be ui-ux for v2")

plugin_name = manifest.get("name", "")
if len(f"{plugin_name}:{SKILL_NAME}") > 64:
    error("plugin-name:skill-name identity exceeds 64 characters")

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

author_name = manifest.get("author", {}).get("name", "")
if author_name and developer and author_name != developer:
    error("plugin author.name and interface.developerName should match")

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

caps = interface.get("capabilities", [])
if len(caps) > 20 or any(
    not isinstance(x, str) or not x.strip() or len(x) > 120 or "\n" in x
    for x in caps
):
    error("Plugin capabilities violate directory limits")

prompts = interface.get("defaultPrompt", [])
if not isinstance(prompts, list) or len(prompts) > 3:
    error("Plugin defaultPrompt must be a list of at most 3 prompts")
else:
    normalized = set()
    for prompt in prompts:
        if (
            not isinstance(prompt, str)
            or not prompt.strip()
            or len(prompt) > 128
            or "\n" in prompt
            or "@" in prompt
        ):
            error(f"Invalid starter prompt: {prompt!r}")
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
        vals = [float(x) for x in viewbox.split()]
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

readme = (ROOT / "README.md").read_text(encoding="utf-8")
install = (ROOT / "INSTALL.md").read_text(encoding="utf-8")

# README should remain a concise entrypoint and link to detailed docs.
if len(readme.splitlines()) > 120:
    error(f"README should stay concise (<=120 lines); got {len(readme.splitlines())}")

for term in [
    "[Roadmap](ROADMAP.md)",
    "[How to Install / Update](INSTALL.md)",
    "[Updates & Changelog](CHANGELOG.md)",
    "[Skill Specification](skills/ui-ux-skill/SKILL.md)",
    "[Shared UI Registry](skills/ui-ux-skill/shared-rules.json)",
    "[Shared UI Routing](skills/ui-ux-skill/references/shared-product-rules.md)",
    "[Design System Registry](skills/ui-ux-skill/design-system.json)",
    "[Design System Architecture](skills/ui-ux-skill/references/design-system-architecture.md)",
    "[Specialist Routing](skills/ui-ux-skill/references/specialist-routing.md)",
]:
    if term not in readme:
        error(f"README missing required documentation link: {term}")

if f"**v{VERSION}**" not in readme:
    error("README current-source version does not match VERSION")

for term in ["persian-writing", "UI/UX Head", "Shared UI Rules", "Design System", "Specialist routing", "websites", "web applications", "mobile applications", "WordPress plugin"]:
    if term.casefold() not in readme.casefold():
        error(f"README missing essential architecture term: {term}")

canonical_url = "https://github.com/pooyahayati/UI-UX-Skill/tree/main/skills/ui-ux-skill"
if canonical_url not in install:
    error("INSTALL.md is missing the canonical installer URL")

for term in [
    "$ui-ux-skill",
    "/ui-ux-skill",
    "production-dashboard-ui-ux-skill",
    "ui-ux-skill",
    "persian-writing",
]:
    if term not in install:
        error(f"INSTALL.md missing required installation/migration term: {term}")

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
if "Public-facing business website" not in tests:
    error("Submission tests do not cover the website Product Pack")
if "Unsafe owner customization" not in tests:
    error("Submission tests do not cover unsafe runtime customization")
if tests.count("Shared Product UI Rules") < 5:
    error("Submission tests do not cover Shared Product UI Rules across all five positive product cases")

submission_checklist = (ROOT / "submission/SUBMISSION_CHECKLIST.md").read_text(encoding="utf-8")
for term in [
    "Machine-readable Shared Product UI Rule registry",
    "Shared Product UI Rule router",
    "Nine local shared UI contract modules",
    "Shared-rule structural validator",
    "Machine-readable Design System registry",
    "Design-system structural validator",
    "Five-product real-world evaluation",
]:
    if term not in submission_checklist:
        error(f"Submission checklist missing v2.7 shared-rule item: {term}")

roadmap = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
for term in [
    "Stage 1 — Website Product Pack",
    "Stage 2 — WordPress Plugin Product Pack",
    "Stage 3 — Dashboard Product Pack",
    "Stage 4 — Shared Product UI Rules",
    "Stage 5 — Design System Hardening",
    "Stage 6 — Real-World Product Evaluation",
]:
    if term not in roadmap:
        error(f"ROADMAP missing required stage: {term}")

stage2_start = roadmap.find("## Stage 2 — WordPress Plugin Product Pack")
stage3_start = roadmap.find("## Stage 3 — Dashboard Product Pack")
stage4_start = roadmap.find("## Stage 4 — Shared Product UI Rules")
stage2_block = roadmap[stage2_start:stage3_start] if stage2_start >= 0 and stage3_start > stage2_start else ""
if "**Status:** Completed" not in stage2_block:
    error("Stage 2 — WordPress Plugin Product Pack must be Completed")

stage3_block = roadmap[stage3_start:stage4_start] if stage3_start >= 0 and stage4_start > stage3_start else ""
if "**Status:** Completed" not in stage3_block:
    error("Stage 3 — Dashboard Product Pack must be Completed")

stage5_start = roadmap.find("## Stage 5 — Design System Hardening")
stage6_start = roadmap.find("## Stage 6 — Real-World Product Evaluation")
stage4_block = roadmap[stage4_start:stage5_start] if stage4_start >= 0 and stage5_start > stage4_start else ""
if "**Status:** Completed" not in stage4_block:
    error("Stage 4 — Shared Product UI Rules must be Completed")

stage5_block = roadmap[stage5_start:stage6_start] if stage5_start >= 0 and stage6_start > stage5_start else ""
if "**Status:** Completed" not in stage5_block:
    error("Stage 5 — Design System Hardening must be Completed")

future_start = roadmap.find("## Future Product Types")
stage6_block = roadmap[stage6_start:future_start] if stage6_start >= 0 and future_start > stage6_start else ""
if "**Status:** Completed" not in stage6_block:
    error("Stage 6 — Real-World Product Evaluation must be Completed for v3.0")

website_paths = [
    "references/products/website.md",
    "references/products/website/structure-navigation.md",
    "references/products/website/conversion-trust.md",
    "references/products/website/content-seo.md",
    "references/products/website/media-performance.md",
    "references/products/website/accessibility-localization-qa.md",
]
website_pack = "\n".join((SKILL / rel).read_text(encoding="utf-8") for rel in website_paths)
for term in [
    "Website subtype and visitor job",
    "Website decision brief",
    "Navigation",
    "Homepage architecture",
    "First viewport / hero",
    "Conversion UX",
    "Trust and credibility",
    "SEO-aware information architecture",
    "Responsive media and art direction",
    "Performance UX",
    "Accessibility",
    "Privacy, consent, and preference UX",
    "Localization, Persian, and RTL websites",
    "Website QA matrix",
]:
    if term.casefold() not in website_pack.casefold():
        error(f"Website Product Pack coverage missing after modularization: {term}")

web_app_paths = [
    "references/products/web-application.md",
    "references/products/web-application/navigation-state.md",
    "references/products/web-application/workflows-data.md",
    "references/products/web-application/interaction-access.md",
]
web_app_pack = "\n".join((SKILL / rel).read_text(encoding="utf-8") for rel in web_app_paths)
for term in [
    "Browser navigation and URL state",
    "Drafts, autosave, and unsaved changes",
    "Long-running and background work",
    "Concurrency, stale data, and conflicting edits",
    "Dialogs, drawers, popovers, and overlays",
    "Accessibility interaction contracts",
]:
    if term.casefold() not in web_app_pack.casefold():
        error(f"Web Application Product Pack coverage missing after modularization: {term}")

wordpress_pack = (SKILL / "references/products/wordpress-plugin.md").read_text(encoding="utf-8")
for term in [
    "Required WordPress routing",
    "Menu placement and entry point",
    "Capability boundaries",
    "WordPress-native vs custom application UI",
    "Settings API awareness",
    "Diagnostics and Site Health",
    "Privacy and personal data",
    "Multisite / Network Admin",
    "Plugin QA matrix",
]:
    if term.casefold() not in wordpress_pack.casefold():
        error(f"WordPress Plugin Product Pack Hardening missing: {term}")

for ref, terms in {
    "settings.md": [
        "Settings information architecture",
        "Save model",
        "Admin notices",
        "Import / export",
        "License and account surfaces",
    ],
    "onboarding-integrations.md": [
        "First successful outcome",
        "Integration state model",
        "OAuth / external authorization",
        "Data sync onboarding",
    ],
    "diagnostics-operations.md": [
        "Site Health integration",
        "Background jobs",
        "Support information",
        "Data deletion and uninstall cleanup",
    ],
    "multisite-admin.md": [
        "Network Admin vs site admin",
        "Network defaults and site overrides",
        "Bulk / selected-site operations",
        "Destructive network actions",
    ],
}.items():
    wp_ref = (SKILL / "references/products/wordpress" / ref).read_text(encoding="utf-8")
    for term in terms:
        if term.casefold() not in wp_ref.casefold():
            error(f"WordPress local pack {ref} missing: {term}")

dashboard_pack = (SKILL / "references/products/dashboard.md").read_text(encoding="utf-8")
for term in [
    "Required Dashboard mode routing",
    "Dashboard decision brief",
    "Decision hierarchy",
    "Data Trust UX",
    "Metric contracts",
    "Filters and analytical context",
    "Drill-down and traceability",
    "Charts and visualizations",
    "Alerts and attention",
    "Live and near-real-time dashboards",
    "Dashboard QA matrix",
]:
    if term.casefold() not in dashboard_pack.casefold():
        error(f"Dashboard Product Pack Hardening missing: {term}")

for ref, terms in {
    "executive.md": [
        "Primary job",
        "Executive summary layer",
        "Targets and baselines",
        "Forecast and uncertainty",
    ],
    "analytical.md": [
        "Exploration model",
        "Comparison",
        "Distribution and variation",
        "Missing, sparse, and partial data",
    ],
    "operational.md": [
        "Work queue first",
        "Prioritization",
        "SLA and time sensitivity",
        "Row and bulk actions",
    ],
    "monitoring-noc.md": [
        "Monitoring strategy",
        "Attention hierarchy",
        "Real-time updates",
        "Connection and freshness",
    ],
    "crm-pipeline.md": [
        "Stage semantics",
        "Pipeline value",
        "Funnel/conversion",
        "Aging and stagnation",
    ],
    "admin-management.md": [
        "Scope and authority",
        "Permission-aware presentation",
        "Audit and traceability",
        "High-impact actions",
    ],
}.items():
    dashboard_ref = (SKILL / "references/products/dashboard" / ref).read_text(encoding="utf-8")
    for term in terms:
        if term.casefold() not in dashboard_ref.casefold():
            error(f"Dashboard local mode pack {ref} missing: {term}")

shared_registry = json.loads((SKILL / "shared-rules.json").read_text(encoding="utf-8"))
expected_shared_ids = {
    "navigation-wayfinding",
    "forms-data-entry",
    "feedback-status",
    "state-recovery",
    "destructive-high-impact-actions",
    "accessibility-interaction",
    "responsive-adaptation",
    "motion",
    "content-hierarchy-progressive-disclosure",
}
shared_ids = {
    item.get("id")
    for item in shared_registry.get("modules", [])
    if isinstance(item, dict)
}
if shared_registry.get("schema_version") != 1 or shared_ids != expected_shared_ids:
    error("Shared Product UI Rule registry missing or inconsistent")

shared_router = (SKILL / "references/shared-product-rules.md").read_text(encoding="utf-8")
for term in [
    "Authority and precedence",
    "Load strategy",
    "Non-duplication rule",
    "Product Pack may specialize",
    "must not weaken",
]:
    if term.casefold() not in shared_router.casefold():
        error(f"Shared Product UI Rule routing missing: {term}")

for product_ref in [
    "website.md",
    "dashboard.md",
    "web-application.md",
    "mobile-application.md",
    "wordpress-plugin.md",
]:
    product_text = (SKILL / "references/products" / product_ref).read_text(encoding="utf-8")
    if "shared-product-rules.md" not in product_text:
        error(f"{product_ref} missing Shared Product UI Rule routing")
    if "Shared rule loading".casefold() in product_text.casefold():
        error(f"{product_ref} still contains the duplicated Shared rule loading block")

profile = (SKILL / "references/discovery-and-profile.md").read_text(encoding="utf-8")
for term in [
    "profile_version",
    "skill_version",
    "status:",
    "source:",
    "locked_constraints",
    "runtime_governance",
    "owner_configurable",
    "user_configurable",
    "code_only",
    "data_ux",
    "routing:",
    "product_packs_loaded",
    "shared_rules_loaded",
    "design_system:",
    "modules_loaded",
    "token_interchange",
    "runtime_boundary",
]:
    if term not in profile:
        error(f"Design Profile v3.0 field missing: {term}")

design_registry = json.loads((SKILL / "design-system.json").read_text(encoding="utf-8"))
expected_design_modules = {
    "tokens-foundations",
    "typography",
    "color-theme",
    "spacing-density-layout",
    "component-states",
    "responsive-variants",
    "governance-migration",
}
design_module_ids = {
    item.get("id")
    for item in design_registry.get("modules", [])
    if isinstance(item, dict)
}
if design_registry.get("schema_version") != 1 or design_module_ids != expected_design_modules:
    error("Design System registry missing or inconsistent")
if design_registry.get("stable_token_interchange") != "DTCG 2025.10":
    error("Design System stable token interchange must be DTCG 2025.10")

architecture = (SKILL / "references/design-system-architecture.md").read_text(encoding="utf-8")
for term in [
    "Primitive Tokens -> Semantic Tokens -> Component Tokens -> Product Variants",
    "Required module routing",
    "DTCG 2025.10",
    "Authority and precedence",
    "Design-system defaults vs runtime settings",
    "Testing changeability",
]:
    if term.casefold() not in architecture.casefold():
        error(f"Design-system architecture guidance missing: {term}")

governance = (SKILL / "references/runtime-ui-governance.md").read_text(encoding="utf-8")
for term in [
    "server-side",
    "arbitrary CSS",
    "Preview",
    "Validate",
    "Publish",
    "Version history",
    "Rollback",
    "Audit log",
    "Import and export",
    "safe fallbacks",
]:
    if term.casefold() not in governance.casefold():
        error(f"Runtime governance guidance missing: {term}")

personalization = (SKILL / "references/personalization-and-data-ux.md").read_text(encoding="utf-8")
for term in [
    "Saved views",
    "Role-aware UX",
    "Data Trust UX",
    "last updated",
    "timezone",
    "stale",
    "partial",
]:
    if term.casefold() not in personalization.casefold():
        error(f"Personalization/Data UX guidance missing: {term}")

evals = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
cases = evals.get("cases", [])
if evals.get("version") != VERSION:
    error("Behavioral eval manifest version does not match VERSION")
if len(cases) < 50:
    error("Behavioral eval manifest should contain at least 50 cases for v3.0")
ids = {case.get("id") for case in cases}
for required_id in [
    "owner-runtime-governance",
    "personalization-precedence",
    "data-trust",
    "arbitrary-code-config",
    "visual-regression-redesign",
    "realtime-operations",
    "head-delegated-ui",
    "persian-specialist-routing",
    "specialist-freshness",
    "website-product-routing",
    "website-ia-trust-conversion",
    "website-content-accessibility-performance",
    "dashboard-product-routing",
    "dashboard-executive-mode",
    "dashboard-analytical-mode",
    "dashboard-operational-mode",
    "dashboard-monitoring-noc-mode",
    "dashboard-crm-pipeline-mode",
    "dashboard-admin-management-mode",
    "web-application-product-routing",
    "mobile-application-product-routing",
    "web-application-state-continuity",
    "mobile-ios-local-rules",
    "mobile-android-local-rules",
    "mobile-cross-platform-local-rules",
    "wordpress-plugin-product-routing",
    "wordpress-settings-capabilities",
    "wordpress-onboarding-integrations",
    "wordpress-diagnostics-operations",
    "wordpress-multisite-admin",
    "multi-product-routing",
    "shared-rules-broad-redesign",
    "shared-rules-narrow-scope",
    "shared-rules-product-specialization",
    "shared-rules-accessibility-floor",
    "design-system-token-hierarchy",
    "design-system-component-states",
    "design-system-theme-resolution",
    "design-system-typography-rtl",
    "design-system-density-responsive",
    "design-system-runtime-boundary",
    "real-world-dashboard-evaluation",
    "real-world-website-evaluation",
    "real-world-web-app-evaluation",
    "real-world-mobile-evaluation",
    "real-world-wordpress-evaluation",
]:
    if required_id not in ids:
        error(f"Behavioral eval missing v3.0 case: {required_id}")
if not any(case.get("type") == "positive" for case in cases):
    error("Behavioral evals need positive cases")
if not any(case.get("type") == "negative" for case in cases):
    error("Behavioral evals need negative cases")

real_world_result = json.loads((ROOT / "evals/real-world/result.json").read_text(encoding="utf-8"))
real_world_cases = real_world_result.get("cases", [])
if len(real_world_cases) != 5:
    error("Stage 6 real-world result must be recorded for exactly five products")
if any(item.get("result") == "fail" for item in real_world_cases):
    error("Stage 6 real-world result contains a blocking fail")
if "not an independent fresh Codex/Claude session" not in (real_world_result.get("independence") or ""):
    error("Stage 6 real-world result must disclose evaluation independence limitation")

for case in cases:
    fixture = case.get("fixture")
    if fixture:
        fixture_dir = ROOT / "evals" / "fixtures" / fixture
        if not fixture_dir.is_dir() or not (fixture_dir / "README.md").is_file():
            error(f"Missing or invalid eval fixture: {fixture}")

if ERRORS:
    print("Release validation failed:")
    for item in ERRORS:
        print(f"- {item}")
    sys.exit(1)

print(f"Release validation passed for v{VERSION}.")
