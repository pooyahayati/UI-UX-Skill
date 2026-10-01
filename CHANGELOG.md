# Updates & Changelog

All notable user-facing and technical changes to this project are documented here.

## [2.0.0] - 2026-10-01

### Canonical Skill Identity Migration

- Renamed the technical Skill slug from `production-dashboard-ui-ux-skill` to `ui-ux-skill`.
- Moved the canonical Skill source to `skills/ui-ux-skill/`.
- Updated Codex and Claude invocation examples to `$ui-ux-skill` and `/ui-ux-skill`.
- Renamed the portable Plugin package identity from `production-dashboard-ui-ux` to `ui-ux`.
- Updated release artifacts, OpenAI validation, installer smoke tests, contribution docs, eval metadata, and submission metadata to the new identity.
- Added an explicit migration path for legacy installations. Version 1.x installations using the old slug should be removed and reinstalled from the new canonical path.
- Kept the public repository slug `UI-UX-Skill` and the machine-readable Skill slug `ui-ux-skill` aligned while preserving lowercase Agent Skill naming conventions.
- Added a machine-readable `specialists.json` registry so specialist identity, trigger, requirement level, source, and install path are separated from domain methodology.
- Added `scripts/validate_specialists.py` to validate specialist sources and compare installed copies with current canonical upstream without pinning versions.
- Added periodic upstream specialist freshness validation in GitHub Actions.
- Confirmed `persian-writing` as a REQUIRED independent specialist for Persian-facing UI; it is referenced and installable from its canonical repository rather than vendored into this Head.

## [1.5.0] - 2026-10-01

### Head Skill and Specialist Routing

- Added explicit standalone and Head-delegated operating modes so the Skill can act as a UI/UX Head or as a bounded specialist under a higher-level engineering Head.
- Added a formal authority hierarchy: higher-level engineering Head → Production Dashboard UI/UX Head → lower-level specialists.
- Added `references/specialist-routing.md` with required/recommended specialist classes, delegation contracts, fallback behavior, conflict handling, repository-state ownership, and structured handoff rules.
- Added REQUIRED `persian-writing` routing for Persian-facing UI and mixed Persian/English user-facing copy.
- Kept UI layout, responsive behavior, RTL/LTR architecture, design-system decisions, typography architecture, interaction design, accessibility, and visual hierarchy under the UI/UX Head while delegating Persian linguistic correctness to `persian-writing`.
- Added explicit fail-safe behavior when the required Persian specialist is unavailable: safe non-language UI work may continue, but Persian language QA remains Unverified and Persian-facing copy cannot be declared final.
- Added RECOMMENDED `browser-testing-with-devtools` routing for live browser evidence when available.
- Added specialist-routing QA coverage and Head-delegation/Persian-routing behavioral evals.
- Updated documentation and release validation to treat specialist routing as a first-class capability.
- Refined the architecture to a thin Head: specialist methodology is not duplicated in the Head; only triggers, precedence, constraints, handoff, fallback, and source metadata remain.
- Added version-agnostic specialist routing and a freshness policy that prefers the latest stable installed Head/Specialists, updates known-stale copies when supported, and never pins specialist versions without an explicit compatibility reason.

## [1.4.0] - 2026-09-20

### Quality, Evidence, and Operational UX

- Added an executable behavioral-eval harness with reusable fixture projects, run preparation, result schema, and result validation.
- Added fixtures for existing-dashboard safety, Owner runtime configuration, Persian RTL tables, analytics/Data Trust, and real-time operations.
- Added a formal visual-regression protocol with representative baselines, stable screenshot matrices, dynamic-noise handling, semantic review, and explicit coverage reporting.
- Added an evidence-driven UX framework: Observation → Evidence → User Impact → Hypothesis → Change → Validation.
- Added confidence guidance and UX metrics without inventing uplift or false precision.
- Expanded Design Presets into a practical multi-dimension heuristic matrix while keeping presets non-template-based.
- Added implementation strategies for CSS variables, utility-first CSS, shadcn-style stacks, theme-object libraries, CSS-in-JS, preprocessors, and component frameworks.
- Added Preference Reconciliation for owner/user settings, Saved Views, removed options, migrations, permission changes, and multi-device conflicts.
- Added operational interaction patterns for duplicate actions, stale/concurrent edits, bulk operations, long-running jobs, search, live updates, and connection state.
- Added domain-aware dashboard prompts for CRM, support, ERP/inventory, finance, DevOps/NOC, security operations, healthcare administration, HR, and executive dashboards.
- Added project-relative performance-budget guidance and stronger accessibility evidence requirements.
- Connected visual regression, UX evidence, implementation strategies, and preference reconciliation to SKILL routing and final QA.
- Reduced README specification duplication and moved detailed guidance into references.

## [1.3.0] - 2026-09-20

### Product Design and Runtime Governance

- Added a dedicated Design System Architecture reference for token layering, configuration schemas, precedence, migrations, and maintainable changeability.
- Added Runtime UI Governance with an optional Owner-only UI/UX Control Center.
- Defined safe owner configuration through allowlisted semantic tokens rather than arbitrary CSS, JavaScript, or HTML.
- Added Draft → Preview → Validate → Publish lifecycle, version history, rollback, audit log, reset, import/export, tenant isolation, and failure fallback guidance.
- Added explicit server-side authorization requirements for privileged appearance controls.
- Added deterministic precedence: Locked Constraints → Design System Defaults → Published Owner Config → User Preferences.
- Added user personalization guidance for density, theme, sidebar state, table preferences, saved filters, saved views, and optional dashboard layouts.
- Added role-aware UX and power-user patterns.
- Added Data Trust UX for last-updated time, freshness, source, timezone, active filter scope, stale/partial/sync states, metric definitions, and drill-down traceability.
- Expanded dashboard patterns for saved views, shared-view permissions, role-aware landing experiences, onboarding, and recurring user preferences.
- Expanded existing-product audits to cover maintainability, hard-coded presentation, token architecture, runtime governance, personalization, and data trust.
- Expanded QA to cover configuration authorization, preview/publish/rollback, migrations, cache invalidation, preference precedence, stale data, and runtime fallback.
- Extended Design Profile schema with runtime governance, owner/user/code-only classification, and Data UX fields.
- Added behavioral eval definitions and public submission coverage for runtime governance and personalization.

## [1.2.0] - 2026-09-20

### Hardening

- Reduced the canonical `SKILL.md` to a route-based entrypoint with progressive disclosure.
- Removed duplicate root Skill/reference copies; `skills/production-dashboard-ui-ux-skill/` is now the single source of truth.
- Rewrote the trigger description to state both when to use and when not to use the Skill.
- Added Collaborative, Delegated, and Audit-only autonomy modes.
- Added explicit working-tree, privacy, production-data, dependency, and asset-license safety.
- Added dedicated performance and accessibility references.
- Added audit coverage reporting and stronger before/after regression criteria.
- Expanded localization beyond RTL/LTR to numbers, currency, dates, timezone, pluralization, text expansion, truncation, and translation-safe strings.
- Added chart accessibility and data-alternative guidance.
- Added Design Profile provenance, status, skill-version, decision-source, and locked-constraint fields.
- Corrected Codex skill-installer URLs to include the required repository path.
- Added validated public Plugin metadata, supported category/capabilities, publisher website/support links, brand colors, logo, and composer icon.
- Shortened Plugin listing fields and starter prompts to public-directory limits.
- Shortened the plugin package name so `plugin-name:skill-name` stays within the public identity limit.
- Reworked submission tests to exactly five positive and three negative cases with expected result format and fixture requirements.
- Added deterministic release packaging, checksums, permanent release workflow, official OpenAI skill validation, and Codex installer smoke testing.
- Added machine-readable behavioral eval cases and forward-testing instructions.

## [1.1.0] - 2026-09-19

### Added

- Dedicated existing-product audit and improvement workflow.
- Observed Baseline for completed/live products without a Design Profile.
- Safe-fix vs strategic-change rules.
- Brand, palette, and logo-treatment audit with controlled refresh support.
- Regression-aware before/after QA.

## [1.0.0] - 2026-09-19

### Added

- Initial public release.
- Design Discovery and Design Profile workflow.
- Dashboard and product UI patterns.
- Persian RTL, English LTR, local fonts, responsive behavior, Light/Dark themes, branding, and visual QA.
- Codex and Claude distribution guidance.
