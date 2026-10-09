![UI/UX Skill: responsive interfaces, design tokens and a living design handbook. Created by Pooya Hayati.](docs/images/ui-ux-skill-hero.png)

# UI/UX Skill

[![Validate](https://github.com/pooyahayati/UI-UX-Skill/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/pooyahayati/UI-UX-Skill/actions/workflows/validate-skill.yml)
![Version](https://img.shields.io/badge/version-3.4.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A product-aware **UI/UX Head** for designing, auditing and improving real interfaces. Works standalone or as a bounded specialist under an engineering Head.

Current source: **v3.4.0** · Skill slug: `ui-ux-skill` · [Latest published release](https://github.com/pooyahayati/UI-UX-Skill/releases/latest)

## Product coverage

| Product | Focus |
| --- | --- |
| **Website** | Navigation, content hierarchy, conversion/trust, SEO-aware structure and accessible responsive pages. |
| **Dashboard** | Decision hierarchy, trustworthy metrics, tables/charts, filters, live states and role-aware work queues. |
| **Web Application** | Routed workflows, URL/state continuity, drafts, forms, recovery, keyboard/focus and permission-facing UX. |
| **Mobile Application** | iOS/Android/cross-platform adaptation, touch, lifecycle/offline behavior and accessible adaptive layouts. |
| **WordPress Plugin / Admin UI** | Native admin integration, task-based settings, reliable saving, onboarding, diagnostics, capabilities and Multisite. |
| **Shared foundation** | Shared UI Rules, Design System tokens/themes/states, responsive/RTL behavior and bounded appearance governance. |

Inactive Product Packs are not preloaded. Only the active product's modules and scope-relevant shared rules are loaded. For Persian-facing UI, `persian-writing` is required; it is the only external specialist.

New or explicitly redesigned plugin-owned WordPress settings use stable public `@wordpress/components`, including short forms. The [scoped component guide](skills/ui-ux-skill/references/products/wordpress/components.md) preserves existing storage, permissions and other surfaces; an audit or narrow fix does not authorize migration. [Real-admin examples and evidence](evals/wordpress-settings/README.md) show the bounded behavior.

## Design workflow

1. Inspect the product, audience and settled decisions; ask focused questions and recommend suitable defaults.
2. Maintain one living `DESIGN.md`. Review one responsive primary-language/direction sample using approved foundations.
3. Refine and approve that revision, then review dark mode. Add a second language/layout only when needed and authorized.
4. Implement and validate the affected workflow. In-scope products with admin can use prepared, permissioned appearance/font/icon controls.

Material Design is [optional and product-personalized](skills/ui-ux-skill/references/material-design.md), not a universal default or automatic library choice. Existing stack, permissions, business logic and user data remain protected. Guidance and synthetic fixtures are not a turnkey production theme/admin engine.

## Quick use

Codex: `$ui-ux-skill` · Claude Code: `/ui-ux-skill`

Example: “Use this Skill to inspect our web app and improve the mobile visit form without changing its workflow or permissions.”

## Documentation

- [How to Install / Update](INSTALL.md)
- [Roadmap](ROADMAP.md) — current status, completed stages, evidence and next action
- [Updates & Changelog](CHANGELOG.md) — concise releases and linked history
- [Skill Specification](skills/ui-ux-skill/SKILL.md) — canonical behavior and conditional routing
- [Product Registry](skills/ui-ux-skill/product-types.json) · [Shared UI Registry](skills/ui-ux-skill/shared-rules.json) · [Design System Registry](skills/ui-ux-skill/design-system.json)
- [Specialist Routing](skills/ui-ux-skill/references/specialist-routing.md)
- [Evaluation guide](evals/README.md) — raw inputs, checks, results and limitations
- [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md) · [Support](SUPPORT.md)

## Project status

The current focus is stability, bug fixes and usability improvements. See the [Roadmap](ROADMAP.md) for development status and scope, or [Contributing](CONTRIBUTING.md) to propose a change.

## Author and license

Pooya Hayati · [Website](https://pooyahayati.com) · MIT
