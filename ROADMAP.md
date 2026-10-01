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
**Status:** Planned

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
**Status:** Planned

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
**Status:** Planned

Extract stable rules repeated across Product Packs.

Potential shared modules:

- navigation principles
- forms
- feedback
- loading / empty / error states
- destructive actions
- accessibility interaction contracts
- responsive principles
- motion
- content hierarchy
- state/recovery patterns

Do not extract rules merely because two files use similar wording. Extract only when the behavioral contract is genuinely shared.

## Stage 5 — Design System Hardening

**Target:** v2.8.x  
**Status:** Planned

Strengthen the design-system layer:

- foundations
- semantic tokens
- typography roles
- spacing
- color roles
- radius
- elevation
- component states
- density
- themes
- RTL/LTR
- responsive tokens
- product-specific variants
- runtime configuration boundaries
- visual regression compatibility

## Stage 6 — Real-World Product Evaluation

**Target:** v3.0.0 candidate  
**Status:** Planned

Test the Skill against representative real projects:

1. Dashboard
2. Website
3. Web Application
4. Mobile Application
5. WordPress Plugin

Evaluate:

- product-route classification accuracy
- correct Product Pack loading
- unnecessary questions
- rule relevance
- rule conflicts
- missed states
- rendered quality
- accessibility behavior
- responsive behavior
- Persian/RTL behavior
- regression safety
- completion/reporting quality

Use failures to refine existing rules before adding new ones.

## Future Product Types

Only consider new Product Types after the current roadmap is validated.

Candidates may include:

- ecommerce
- desktop application
- documentation / knowledge platform

A candidate should become a dedicated Product Type only when its behavior cannot be represented cleanly by an existing Product Pack plus shared rules.
