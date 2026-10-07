# UI/UX Skill

[![Validate](https://github.com/pooyahayati/UI-UX-Skill/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/pooyahayati/UI-UX-Skill/actions/workflows/validate-skill.yml)
![Version](https://img.shields.io/badge/version-3.2.1-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A product-aware **UI/UX Head** for designing, auditing and improving real interfaces. Works standalone or as a bounded specialist under an engineering Head.

Current source: **v3.2.1** · Skill slug: `ui-ux-skill` · [Latest published release](https://github.com/pooyahayati/UI-UX-Skill/releases/latest)

The 3.2.1 maintenance update repairs packaging safety, packaged resource routes, stale-draft recovery, evaluation verdict consistency and whole-package specialist verification. See [release notes](CHANGELOG.md) and [delivery status](ROADMAP.md).

## Product coverage

| Product | Focus |
| --- | --- |
| **Website** | Navigation, content hierarchy, conversion/trust, SEO-aware structure and accessible responsive pages. |
| **Dashboard** | Decision hierarchy, trustworthy metrics, tables/charts, filters, live states and role-aware work queues. |
| **Web Application** | Routed workflows, URL/state continuity, drafts, forms, recovery, keyboard/focus and permission-facing UX. |
| **Mobile Application** | iOS/Android/cross-platform adaptation, touch, lifecycle/offline behavior and accessible adaptive layouts. |
| **WordPress Plugin / Admin UI** | Native admin integration, settings, onboarding, diagnostics, capabilities and Multisite. |
| **Shared foundation** | Shared UI Rules, Design System tokens/themes/states, responsive/RTL behavior and bounded appearance governance. |

Inactive Product Packs are not preloaded. Only the active product's modules and scope-relevant shared rules are loaded. For Persian-facing UI, `persian-writing` is required; it is the only external specialist.

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

## Feature freeze

Limited correction exception: R0–R8 only. The design-foundation, living-handbook, visual-approval and safe appearance work is completed.

Separate R9 exception: optional Material Design only. All six packages are completed within their documented engineering scope.

Outside this exception, stabilization maintenance is the default: no new Product Types, additional external design specialists or general-purpose page builder. Completion is not fresh delivery authority. See [Roadmap](ROADMAP.md) for scope and evidence.

## Author and license

Pooya Hayati · [Website](https://pooyahayati.com) · MIT
