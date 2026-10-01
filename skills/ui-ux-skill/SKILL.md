---
name: ui-ux-skill
description: Product-aware UI/UX Head Skill for designing, auditing, improving, and validating websites, dashboards, web applications, mobile applications, WordPress plugin/admin UI, and other production product interfaces. Works standalone or as a specialist under a higher-level engineering Head. It MUST classify the product type and load the required Product Pack before product-specific design decisions, then route narrow concerns to specialist Skills. Use for product UI/UX, existing-product reviews, responsive or RTL/LTR work, themes, branding, navigation, forms, data UI, accessibility, performance, personalization, runtime design governance, or visual QA. Persian-facing UI requires the persian-writing specialist. Do not use for backend-only work, marketing-only websites, or unrelated graphic design.
---

# UI/UX Skill

Build and improve production interfaces for real work, not screenshot-first demos.

Core principle:

> Design for the task, not for the screenshot.

## Operating role and delegation

This Skill can run in two modes:

- **Standalone UI/UX Head** — invoked directly and responsible for UI/UX routing, design decisions, and UI validation.
- **Head-delegated UI/UX Specialist** — invoked by a higher-level engineering Head with objective, scope, constraints, risk/approval requirements, or acceptance criteria already established.

Read `references/specialist-routing.md` whenever another Skill delegates work to this Skill or when a lower-level specialist may be required.

In Head-delegated mode:

- preserve the higher-level Head's approved scope, risk floor, architecture/security boundaries, and acceptance criteria;
- do not repeat discovery or reopen decisions already settled upstream;
- own UI/UX decisions only inside the delegated boundary;
- return a structured UI/UX handoff rather than declaring the entire software objective complete.

Authority order:

`Higher-level Engineering Head -> UI/UX Head -> Lower-level Specialist`

## Route the product first

Before choosing a work mode, read:

- `product-types.json`
- `references/product-routing.md`

Determine the primary product route and load every required Product Pack for that route.

Product classification is mandatory for product UI work.

For major/new work, do not make product-specific design decisions until the product route is resolved.

For narrow existing-product changes, infer the route from repository/product evidence when confidence is high.

A task may activate multiple Product Packs, but one primary route must be identified for the current deliverable.

Current registered routes include:

- `website`
- `dashboard`
- `web-application`
- `mobile-application`
- `wordpress-plugin`
- `generic-product-ui` as fallback only

## Route the task mode

Choose the smallest mode that fits the request.

### New product

Use when there is no established interface.

Read:
- `references/discovery-and-profile.md`
- the relevant domain references
- `references/design-system-architecture.md` when implementing a reusable product UI
- `references/qa-checklist.md` before completion

Typical flow:

`Inspect -> Discover -> Recommend -> Approve or Delegate -> Foundation -> Representative Screen -> Roll Out -> QA`

### Existing product — audit only

Use when the user asks to review, critique, assess, or report problems.

Read:
- `references/existing-product-audit.md`
- `references/qa-checklist.md`

Do not modify code or assets unless requested.

### Existing product — audit and improve

Use when the user asks to fix, modernize, improve, polish, or redesign an existing product.

Read:
- `references/existing-product-audit.md`
- `references/execution-safety.md`
- `references/design-system-architecture.md` when maintainability or configurability matters
- relevant visual/domain references
- `references/qa-checklist.md`

Typical flow:

`Baseline -> Audit -> Prioritize -> Fix -> Validate -> Compare -> Refine`

If no approved `design-profile.md` exists, infer an Observed Baseline first. Do not force a full discovery interview for local corrective work.

### Targeted UI change

Use when the request is narrow, such as a table, form, palette, mobile issue, RTL defect, theme issue, typography problem, logo treatment, personalization feature, or appearance setting.

Inspect the affected surface and read only the relevant references.

Do not expand the assignment unnecessarily.

## Autonomy and approvals

Respect the user's working style.

When a higher-level Head supplied approval or autonomy constraints, those constraints take precedence over this Skill's standalone autonomy defaults.

### Collaborative mode

Use when the user wants to review major design decisions.

Pause before broad changes to:
- primary navigation
- information architecture
- core workflows
- global palette or typography
- design-system foundation
- actual logo artwork or brand identity
- UI framework or component-library migration
- runtime configuration capabilities that change product-wide behavior

### Delegated mode

Use when the user explicitly asks the agent to make reasonable design decisions and complete the work without repeated approvals.

Proceed within the requested scope, but still do not silently:
- weaken permissions or security
- change business rules or data meaning
- remove product capabilities
- replace the actual brand identity unless that was requested
- introduce a major framework migration without a clear need
- expose arbitrary CSS, JavaScript, HTML, or unsafe runtime customization

Document significant decisions at the end.

### Audit-only mode

Never modify code, configuration, or assets.

## Non-negotiable invariants

1. Inspect before changing.
2. Preserve user intent and scope.
3. Preserve business logic, permissions, validation, routing, API contracts, and data semantics unless explicitly authorized.
4. Treat working-tree safety and user-authored changes as protected; read `references/execution-safety.md` for implementation work.
5. Reuse the existing stack before adding dependencies.
6. Existing visual design is not sacred. Improve weak hierarchy, palette, typography, component styling, brand treatment, and responsive behavior when justified.
7. Treat Persian RTL and English LTR as native modes, not post-processing.
8. Treat responsive behavior as product architecture, not a final CSS patch.
9. Use supplied/local fonts and brand assets responsibly; check licensing before adding third-party assets.
10. Prefer semantic design tokens and configuration boundaries over hard-coded presentation when building reusable product UI.
11. Runtime customization must be constrained, validated, permissioned, previewable, and reversible.
12. User preferences must not override locked product constraints or security-sensitive behavior.
13. Do not call a major UI task complete without QA of the rendered result when rendering/browser access is available.
14. Report what was actually inspected and what was not.
15. Do not claim improvement merely because the interface looks newer.
16. Base significant UX findings on evidence and confidence; do not fabricate metrics or research.
17. For broad visual changes, capture or report the absence of a rendered baseline when screenshot/browser tooling is available.
18. Preserve valid user preferences across schema/config changes and reconcile invalid preferences safely.
19. Use required specialist Skills when their triggers are active; never claim specialist-dependent validation when a required specialist was unavailable or not run.
20. Keep specialist knowledge out of the Head: store only routing, precedence, constraints, handoff, and fallback rules; do not duplicate specialist methodology.
21. Use the latest available stable Head/Specialist installations when freshness can be verified; never pin specialist versions in Head routing without an explicit compatibility requirement.
22. Classify every product UI task through `product-types.json` and load all required Product Packs before product-specific design decisions.
23. Product-specific rules belong in Product Packs; do not bloat the Head with duplicated dashboard, web-app, mobile-app, or WordPress-specific methodology.

## Reference routing

Read references only when relevant.

- `product-types.json` — machine-readable product routes and required Product Packs; product classification is mandatory
- `references/product-routing.md` — product classification, precedence, multi-route behavior, and fallback policy
- `specialists.json` — machine-readable specialist identities, requirement levels, triggers, canonical sources, and install paths; contains no specialist methodology or pinned versions
- `references/specialist-routing.md` — standalone vs Head-delegated operation, authority hierarchy, specialist policy, and handoff contract

- `references/discovery-and-profile.md` — discovery, design-profile lifecycle, partial rediscovery, provenance
- `references/existing-product-audit.md` — existing-product baseline, audit matrix, severity, safe vs strategic fixes
- `references/execution-safety.md` — git/working-tree safety, data/privacy boundaries, scoped implementation
- `references/design-system-architecture.md` — token layers, configuration boundaries, maintainability, implementation architecture
- `references/implementation-strategies.md` — mapping the architecture into existing CSS/framework/theme systems
- `references/runtime-ui-governance.md` — owner-only appearance controls, preview/publish/version/rollback/audit
- `references/personalization-and-data-ux.md` — user preferences, saved views, role-aware UX, data trust/freshness
- `references/preference-reconciliation.md` — migration/conflict rules for stored preferences and saved views
- `references/ux-evidence-and-metrics.md` — evidence chain, confidence, UX metrics, validation
- `references/visual-regression.md` — screenshot baselines, rendered evidence, visual regression protocol
- `references/operational-interaction-patterns.md` — search, real-time updates, concurrency, bulk/long-running operations
- `references/domain-patterns.md` — domain-aware prompts for CRM, support, ERP, finance, operations, security, and more
- `references/design-presets.md` — style vocabulary and visual-direction options
- `references/dashboard-patterns.md` — detailed dashboard patterns; load through the dashboard Product Pack rather than as a generic default
- `references/rtl-ltr-typography.md` — RTL/LTR, bilingual UI, localization, fonts, mixed-direction content
- `references/theme-responsive-brand.md` — theme, responsive behavior, palette, logo/brand, icons, motion
- `references/accessibility.md` — WCAG-oriented implementation and verification
- `references/performance.md` — frontend performance and perceived-performance review
- `references/qa-checklist.md` — final validation and coverage reporting

## Existing product baseline

Before broad changes, first determine the active product route(s), then determine enough of the current product to understand:
- shell and navigation
- high-frequency workflows
- representative pages
- components and tokens
- typography and palette
- themes
- responsive behavior
- RTL/LTR/localization
- auth and permission-sensitive surfaces
- loading, empty, error, partial, disabled, and success states
- personalization and saved-view behavior where present
- whether presentation values are centralized or hard-coded
- tests and available visual/browser tooling
- available UX evidence such as support issues, analytics, user feedback, or task data
- existing visual-regression tooling/baselines
- supported product languages and whether Persian-facing UI triggers the required `persian-writing` specialist
- real-time, concurrency, search, and bulk-operation behavior where relevant

For large products, sample representative surfaces first. Record audit coverage rather than implying the whole application was inspected.

## Design profile

For new products or strategic redesigns, create or update `design-profile.md` using `references/discovery-and-profile.md`.

For existing products:
- keep an approved profile authoritative unless the user approves a revision
- use an Observed Baseline for corrective work when no profile exists
- use Partial Rediscovery when only selected strategic fields need to change

When runtime customization is appropriate, record which fields are:
- locked
- owner-configurable
- user-configurable
- code-only

## Runtime configurability decision

Do not add an Owner UI/UX Control Center to every project.

Assess whether runtime design governance is justified by:
- white-label or multi-tenant needs
- frequent brand/theme changes
- non-developer owners who need safe appearance controls
- operational need for density/table/default adjustments
- multiple deployments that should share/import design configuration
- meaningful user personalization needs

If justified, read:
- `references/design-system-architecture.md`
- `references/runtime-ui-governance.md`
- `references/personalization-and-data-ux.md`
- `references/preference-reconciliation.md` when persisted settings can become invalid
- `references/implementation-strategies.md` when mapping the design architecture into the existing stack

Prefer:

`Locked Constraints -> Design System Defaults -> Published Owner Config -> User Preferences`

Do not allow lower layers to override protected constraints.

## Product-first decisions

Before designing a screen, establish:
- who uses it
- why they open it
- what they must know
- what they must do
- what happens next
- which decisions repeat often enough to deserve saved state or personalization

Prefer hierarchy, typography, spacing, grouping, and alignment before adding containers.

Do not default to:
- four KPI cards
- nested cards
- excessive pills
- excessive radius or shadow
- decorative gradients or glass
- huge operational headings
- random accent colors
- charts without a question
- icon-only critical navigation
- animation without informational value

## Brand changes

Differentiate:
- treatment fix: logo size, spacing, contrast, placement, correct variants
- brand refresh: palette, typography, iconography, surface language, visual personality
- identity redesign: actual logo/mark replacement or redraw

Treatment fixes can proceed when UI improvement was requested.

Broad brand refresh follows the selected autonomy mode.

Actual identity replacement requires explicit user intent.

## UI implementation boundaries

Prefer:

`Reuse -> Extend -> Refactor -> Add dependency`

Do not migrate frameworks solely for aesthetics.

Keep changes scoped and reviewable.

For existing products, preserve functional contracts while improving the presentation layer.

For configurable products, prefer a token/configuration architecture over scattered page-level values.

When implementing that architecture, read `references/implementation-strategies.md` and adapt to the existing framework rather than forcing a migration.

## Final validation

Before completion:
1. read `product-types.json` and `references/product-routing.md`; confirm the correct Product Pack(s) were loaded
2. read `specialists.json` and `references/specialist-routing.md`; confirm required specialist routes were satisfied and verify installation/freshness when tooling allows
3. read `references/qa-checklist.md`
4. inspect the rendered UI when possible
5. test representative viewports, themes, directions, and states
6. run available tests, lint, type checks, accessibility checks, and relevant performance checks
7. compare meaningful redesigns against the baseline; read `references/visual-regression.md` for broad visual changes
8. if runtime UI governance exists, test preview, validation, publish, permission, rollback, fallback, and user-preference precedence
9. validate significant UX claims with `references/ux-evidence-and-metrics.md` when evidence is available
10. report coverage, limitations, changes made, preserved behavior, and remaining approval items

If rendered inspection or a required check cannot be performed, say so explicitly.


## Head-delegated result format

When this Skill was invoked by a higher-level engineering Head, finish with:

### UI/UX Specialist Result
- UI/UX decisions made
- affected surfaces/files
- upstream constraints preserved
- required/recommended specialists used or unavailable
- rendered, accessibility, localization, and UX evidence
- checks performed / not performed
- unresolved UI/UX risks
- remaining approvals
- next action required from the higher-level Head

The higher-level Head owns cross-domain integration, release decisions, and final software completion.
