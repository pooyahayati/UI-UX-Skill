# Updates & Changelog

All notable user-facing and technical changes to this project are documented here.

## [Unreleased] — target 3.1.0

### Stabilization, Product Isolation, and Feature Freeze

- Declared a feature freeze: no new Product Types or major capability families are planned for the 3.1.0 stabilization release.
- Reduced the canonical Head so product-specific references are discovered through the active Product Pack instead of being enumerated globally.
- Changed the product registry to classify products and map only top-level Product Packs; internal product modules are parent-routed after activation.
- Added explicit active-product isolation policy so inactive Product Packs and their local modules are not preloaded.
- Split the Website Product Pack into scope-routed modules for structure/navigation, conversion/trust, content/SEO, media/performance, and accessibility/localization/QA while preserving existing coverage.
- Split the Web Application Product Pack into scope-routed navigation/state, workflows/data, and interaction/access modules while preserving existing coverage.
- Centralized Shared Product UI Rule loading to remove repeated pack-level loading instructions.
- Updated product and Shared Rule validators to enforce scope-based loading, parent-routed local modules, and cross-product isolation.
- Replaced the README capability list with a product-by-product coverage table and documented the frozen capability scope.
- Simplified plugin metadata so it describes the stable architecture without version-specific marketing language.
- Added five explicit behavioral Product Isolation cases, one for each primary Product Type, requiring unrelated Product Packs to remain unloaded.
- Added machine-readable forbidden inactive routes to the real-world evaluation manifest and validation that fails on cross-product reference leakage.
- Reduced `validate_release.py` to release/package/documentation responsibilities and removed duplicated Product/Shared/Design/Specialist/Eval validation logic.
- Made `validate-skill.yml` the single reusable validation gate and made release publication depend on that exact gate before packaging/publishing.

## [3.0.0] - 2026-10-02

### Real-World Product Evaluation

- Completed Roadmap Stage 6 with one dedicated production-like evaluation fixture for each primary Product Type: Dashboard, Website, Web Application, Mobile Application, and WordPress Plugin.
- Added five real-world behavioral cases to the main eval manifest, bringing total behavioral coverage to 50 cases.
- Added `evals/real-world/manifest.json` with machine-readable Product Pack, Shared Rule, and Design System expectations per product.
- Added a recorded ChatGPT / GPT-5.6 Sol source-based behavioral evaluation in `evals/real-world/result.json`.
- Added a human-readable Stage 6 result summary with explicit browser/device/fresh-session limitations.
- Added `scripts/validate_real_world_evaluation.py` to require exact five-product coverage, fixture integrity, routing/module expectations, evidence for every invariant, and zero blocking failures.
- Wired real-world evaluation validation into PR and Release workflows.
- Updated the behavioral result template and removed the legacy Dashboard-only schema title.
- Updated fixture validation to require all five Stage 6 fixtures.
- Marked Roadmap Stage 6 complete.
- The recorded run explicitly does not claim independent fresh Codex/Claude/browser/device validation that was not performed.

## [2.8.0] - 2026-10-02

### Design System Hardening

- Added machine-readable `design-system.json` registry and seven local Design System modules.
- Rebuilt `design-system-architecture.md` as a modular router with explicit authority and runtime boundaries.
- Added token foundations covering primitive, semantic, component, product-variant, and resolved-runtime layers.
- Added stable token typing, aliases/references, source-vs-resolved separation, logical-direction guidance, and DTCG 2025.10-compatible interchange guidance.
- Added semantic typography roles including Persian/Latin mixed-script behavior, numeric/data typography, responsive type, and font-loading guidance.
- Added color/theme contracts for Light, Dark, High Contrast / Forced Colors, semantic status roles, chart palette roles, and owner palette constraints.
- Added spacing/density/layout contracts covering semantic spacing, control sizing, density presets, radius, elevation, and logical layout foundations.
- Added reusable component-state contracts covering focus-visible, disabled, read-only, loading, validation, selection, and theme/state matrices.
- Added responsive token and product-variant architecture with deterministic precedence and variant-explosion control.
- Added design-system governance for lifecycle, deprecation, aliases, migration, impact analysis, runtime configuration boundaries, and visual-regression compatibility.
- Added `scripts/validate_design_system.py` and wired it into PR and Release workflows.
- Added six behavioral evals for token hierarchy, component states, theme resolution, bilingual typography, density/responsive behavior, and runtime boundary safety.
- Extended Design Profile, runtime governance, RTL/typography, theme/brand, and visual-regression references for the hardened Design System.
- Marked Roadmap Stage 5 complete.

## [2.7.0] - 2026-10-01

### Shared Product UI Rules

- Added a machine-readable `shared-rules.json` registry for stable cross-product UI contracts.
- Added `references/shared-product-rules.md` with scope-based loading, authority/precedence, specialization rules, and a strict non-duplication policy.
- Added nine local Shared UI modules: navigation/wayfinding, forms/data entry, feedback/status, state/recovery, destructive/high-impact actions, accessibility interaction, responsive adaptation, motion, and content hierarchy/progressive disclosure.
- Established the architecture `Product Route -> Product Pack -> scope-relevant Shared Product UI Rules`; Product Packs retain product/platform/host/domain specialization.
- Added an explicit floor preventing product specialization from weakening accessibility, security, authorization, truthful-state, or user-data-integrity requirements.
- Deduplicated generic navigation/forms/feedback/state/destructive/responsive/accessibility/motion/hierarchy contracts from Website, Web Application, Mobile Application, WordPress Plugin, and Dashboard Product Packs while preserving product-specific behavior.
- Split accessibility responsibility into the Shared accessibility interaction contract plus `accessibility.md` for QA/evidence.
- Removed generic responsive/navigation/motion duplication from the theme/brand reference.
- Added Shared Rule routing to Design Profile and final QA coverage.
- Added `scripts/validate_shared_rules.py` and made Shared Rule validation mandatory in PR and Release workflows.
- Added four behavioral evals for broad Shared Rule loading, narrow scope selection, product specialization precedence, and accessibility-floor preservation.
- Marked Roadmap Stage 4 complete.

## [2.6.0] - 2026-10-01

### Dashboard Product Pack Hardening

- Rebuilt `dashboard.md` as a shared Dashboard foundation plus local mode router while keeping `dashboard` as one Product Type.
- Added local Dashboard mode packs for Executive, Analytical, Operational, Monitoring/NOC, CRM/Pipeline, and Admin/Management use cases.
- Added a Dashboard decision brief covering primary mode, users, decision cadence, metrics/entities, attention model, time horizon, filter scope, freshness, actions, drill-down, personalization, responsive priorities, and validation states.
- Expanded shared Dashboard rules for decision hierarchy, Data Trust UX, metric contracts, targets/baselines, filter context, drill-down/traceability, tables/work queues, visualizations, cross-filtering, alerts, live updates, personalization, role-aware UX, failure/loading states, responsive behavior, accessibility, and RTL.
- Deepened `dashboard-patterns.md` with metric-card context, number formatting, semantic table accessibility, chart scale/baseline rules, time-series semantics, annotations, cross-filtering, legends/labels, and refresh/performance behavior.
- Added machine-readable Dashboard `local_references` for all six modes.
- Added six Dashboard behavioral evals and release/product-route validation for mode-specific routing and required rule contracts.
- Marked Roadmap Stage 3 complete.
- Kept Dashboard design knowledge local; `persian-writing` remains the only external specialist.

## [2.5.0] - 2026-10-01

### WordPress Plugin Product Pack Hardening

- Rebuilt `wordpress-plugin.md` as a local modular Product Pack and router for WordPress admin UI.
- Added local `wordpress/settings.md` rules for settings architecture, save/validation behavior, notices, advanced settings, import/export, licenses/accounts, credentials, reset/default actions, accessibility, and responsive `wp-admin`.
- Added local `wordpress/onboarding-integrations.md` rules for first-run setup, setup wizards, prerequisites, OAuth/API connections, integration states, background initial sync, resume/skip behavior, and completion.
- Added local `wordpress/diagnostics-operations.md` rules for Site Health, plugin-local diagnostics, support exports, logs, background/scheduled jobs, repair/maintenance, destructive data cleanup, and operational notices.
- Added local `wordpress/multisite-admin.md` rules for Network Admin, site-vs-network scope, capabilities, network defaults, site overrides, locked settings, bulk operations, network activation, and destructive network actions.
- Expanded the shared WordPress Product Pack with menu-placement rules, native-vs-application UI classification, capability-aware UX, Settings API awareness, privacy/data lifecycle, updates/migrations, dependencies, responsive admin, accessibility, localization, and a WordPress-specific QA matrix.
- Added machine-readable `local_references` for the WordPress product route.
- Added behavioral evals for settings/capabilities, onboarding/integrations, diagnostics/operations, and Multisite.
- Added release/product-route validation that requires all local WordPress packs and critical WordPress UX contracts.
- Kept `persian-writing` as the only external specialist; WordPress product design remains local.

## [2.4.0] - 2026-10-01

### Website Product Pack Hardening

- Added a root `ROADMAP.md` with an ordered product-design hardening plan through real-world evaluation.
- Deepened `website.md` from a general public-site guide into a full local Product Pack.
- Added website subtype and visitor-job classification for corporate, service, product/brand, personal-brand, publication/content, and campaign/landing surfaces.
- Expanded website information architecture, navigation, mega-menu, breadcrumb, homepage, first-viewport, landing-page, service/detail, and editorial-content rules.
- Added local conversion, CTA, forms/lead-generation, contact/support, trust, testimonials, case-study, pricing, and non-manipulative interaction rules.
- Expanded SEO-aware UX with semantic content structure, title/page-title alignment, internal linking, breadcrumbs, visible-content/structured-data alignment, and search-result presentation considerations.
- Expanded responsive behavior, responsive media/art direction, video, progressive enhancement, third-party script, and performance UX guidance.
- Added WCAG-aware website interaction rules covering focus, target size, forms, menus, zoom/text scaling, reduced motion, consistent help, and recovery states.
- Added privacy/consent, legal/footer, multilingual, Persian/RTL, and website edge-page guidance.
- Added a comprehensive website QA matrix and explicit evidence boundaries for conversion, SEO, accessibility, trust, and performance claims.
- Added behavioral evals and validators that enforce critical Website Product Pack sections.

## [2.3.0] - 2026-10-01

### Local Web and Mobile Design Expansion

- Expanded `web-application.md` with local browser-navigation/URL-state, drafts/autosave, long-running jobs, concurrency/conflict, forms, search/filter state, overlays/focus, destructive actions, file operations, session expiry, onboarding, motion, and accessibility interaction rules.
- Rebuilt the Mobile Product Pack as a shared mobile UX foundation with mandatory local platform routing.
- Added local `mobile/ios.md` rules for Apple navigation/presentation, safe areas, Dynamic Type, iPad/resizable layouts, VoiceOver, keyboard, gestures, and system capabilities.
- Added local `mobile/android.md` rules for edge-to-edge/system bars, predictive back, adaptive layouts, navigation adaptation, large screens/foldables, TalkBack, and IME behavior.
- Added local `mobile/cross-platform.md` rules based on preserving product/UX invariants while translating platform idiom rather than cloning pixels.
- Added machine-readable mobile platform references in `product-types.json`.
- Renamed the WordPress product route from `wordpress-plugin-settings` to `wordpress-plugin` and broadened its Product Pack beyond settings-only screens.
- Reduced external specialists to `persian-writing` only; product design knowledge remains local.
- Added behavioral evals and release validation for Web App state continuity and local iOS/Android/Cross-platform routing.

## [2.2.0] - 2026-10-01

### Website Product Pack and Final Release Automation

- Added `website` as a first-class Product Type separate from `web-application`.
- Added a required Website Product Pack for public-facing company, service, marketing, content, blog, portfolio, landing-page, and SEO-driven websites.
- Added explicit website-vs-web-application routing so public marketing/content surfaces and signed-in application surfaces use different product rules.
- Added website-specific guidance for information architecture, homepage/landing-page hierarchy, conversion/forms, trust signals, semantic/SEO structure, responsive behavior, accessibility, performance, branding, multilingual/RTL handling, and evidence-based validation.
- Added website behavioral eval coverage and release validation.
- Updated public metadata and prompts to advertise website support.
- Updated release automation so a new VERSION merged to `main` can publish the matching GitHub Release automatically when the tag/release does not yet exist.

## [2.1.0] - 2026-10-01

### Product-Aware UI/UX Routing

- Expanded the Skill from dashboard-first UI/UX into a product-aware UI/UX Head.
- Added mandatory product classification before product-specific design decisions.
- Added machine-readable `product-types.json` routing with required Product Packs.
- Added Product Packs for dashboards, web applications, mobile applications, and WordPress plugin settings/admin UI.
- Added multi-route support for products that span surfaces, such as a web application containing an analytics dashboard.
- Added `generic-product-ui` as a fallback only when no registered product type fits.
- Added product route precedence and handoff rules without duplicating product-specific methodology in the Head.
- Added product route fields to Design Discovery / Design Profile.
- Added product-aware QA coverage and behavioral evals.
- Added CI/release validation that fails when required Product Packs or registered routes are missing.

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
