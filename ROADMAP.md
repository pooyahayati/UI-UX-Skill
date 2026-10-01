# UI/UX Skill Roadmap

This roadmap defines the planned sequence for deepening the local design knowledge of `UI/UX Skill`.

The roadmap is intentionally ordered. Finish and validate each stage before expanding the next one.

## Principles

- Product design knowledge stays local to this repository.
- `persian-writing` remains the only external specialist unless explicitly changed later.
- Product Packs contain product-specific methodology.
- Shared rules should be extracted only when repetition becomes real and stable.
- Every major stage should add behavioral eval coverage and release validation.
- Do not add a new Product Type merely to avoid improving an existing Product Pack.
- Prefer evidence-backed rules and current platform guidance over stylistic opinion.

## Stage 1 — Website Product Pack

**Target:** v2.4.x  
**Status:** Completed

Deepen `references/products/website.md` for public-facing websites.

Scope:

- website subtype and visitor-job classification
- information architecture and navigation
- homepage and landing-page composition
- service/content/detail page patterns
- conversion and CTA hierarchy
- trust, proof, credibility, and contact UX
- forms and lead-generation UX
- content hierarchy and editorial scanning
- semantic HTML / SEO-aware information architecture
- breadcrumbs and internal linking
- responsive content behavior
- image/media behavior
- accessibility and WCAG-aware interaction
- performance UX and Core Web Vitals awareness
- motion and progressive enhancement
- multilingual / RTL website behavior
- privacy/consent and non-manipulative interaction
- website-specific QA matrix

Completion gate:

- Product Pack expanded
- website behavioral evals expanded
- release/product-route validators enforce critical website sections
- README/metadata remain concise

## Stage 2 — WordPress Plugin Product Pack

**Target:** v2.5.x  
**Status:** Completed

Deepen `references/products/wordpress-plugin.md`.

Scope:

- settings information architecture
- onboarding/setup wizard
- license/account surfaces
- API/integration connection UX
- diagnostics and site-health UX
- import/export
- background jobs
- destructive/reset/data-cleanup actions
- WordPress notices
- capability/role boundaries
- multisite/network-admin behavior
- native `wp-admin` vs application-like plugin UI
- Persian/RTL WordPress admin behavior
- plugin-specific QA matrix

## Stage 3 — Dashboard Product Pack

**Target:** v2.6.x  
**Status:** Completed

Re-audit and deepen dashboard rules while keeping one Dashboard Product Pack.

Internal dashboard modes to cover:

- executive
- analytical
- operational
- monitoring / NOC
- CRM / pipeline
- admin / management

Focus:

- decision hierarchy
- alerts/attention
- data trust
- table/work-queue behavior
- chart/question matching
- drill-down
- live-update behavior
- role-aware presentation
- saved views / personalization
- responsive dashboard architecture

## Stage 4 — Shared Product UI Rules

**Target:** v2.7.x  
**Status:** Completed

Extracted stable cross-product contracts into local Shared UI modules:

- navigation and wayfinding
- forms and data entry
- feedback and status
- state and recovery
- destructive and high-impact actions
- accessibility interaction
- responsive adaptation
- motion and transitions
- content hierarchy and progressive disclosure

The Product Pack remains authoritative for product/platform/host/domain specialization.

Shared Rules are loaded only when relevant to the task and cannot weaken accessibility, security, authorization, truthful-state, or user-data-integrity requirements.

## Stage 5 — Design System Hardening

**Target:** v2.8.x  
**Status:** Completed

Hardened the local Design System into a modular, machine-readable architecture:

- token foundations: primitive, semantic, component, product-variant, and resolved-runtime layers
- stable token naming/types, aliases/references, and DTCG 2025.10-compatible interchange
- semantic typography roles with Persian/Latin and mixed-script behavior
- semantic color roles with Light, Dark, High Contrast / Forced Colors contexts
- spacing, density, control sizing, radius, elevation, and layout foundations
- reusable component-state contracts
- responsive tokens and product variants without variant explosion
- design-system lifecycle, deprecation, migration, impact analysis, and visual-regression compatibility
- explicit runtime-configuration boundary

Design-system specialization remains subordinate to Product Pack semantics and Shared Product UI Rules.

## Stage 6 — Real-World Product Evaluation

**Target:** v3.0.0  
**Status:** Completed

Evaluated one representative production-like fixture for each primary Product Type:

1. Dashboard
2. Website
3. Web Application
4. Mobile Application
5. WordPress Plugin

Evaluation covered:

- product-route classification accuracy
- correct Product Pack/local-pack loading
- Shared Rule scope
- Design System module scope
- unnecessary-rule avoidance
- product-specific issue detection
- safety/authorization/data-integrity boundaries
- accessibility/responsive risk coverage
- evidence discipline and explicit validation limitations

Recorded result:

`evals/real-world/result.json`

Summary:

`evals/real-world/RESULTS.md`

The 2026-10-02 run was an in-session source-based behavioral evaluation using ChatGPT / GPT-5.6 Sol.

It did not independently execute a fresh Codex/Claude/browser/device run. Rendered/device validation limitations are explicitly recorded and are not represented as completed checks.

## Future Product Types

Only consider new Product Types after the current roadmap is validated.

Candidates may include:

- ecommerce
- desktop application
- documentation / knowledge platform

A candidate should become a dedicated Product Type only when its behavior cannot be represented cleanly by an existing Product Pack plus shared rules.
