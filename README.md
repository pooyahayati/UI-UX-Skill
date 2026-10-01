# UI/UX Skill

[![Validate](https://github.com/pooyahayati/UI-UX-Skill/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/pooyahayati/UI-UX-Skill/actions/workflows/validate-skill.yml)
![Version](https://img.shields.io/badge/version-2.8.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A production-oriented **Product-Aware UI/UX Head Skill** for designing, auditing, improving, and validating websites, dashboards, web applications, mobile applications, WordPress plugin/admin UI, and other production interfaces.

It can work independently or as a UI/UX specialist under a higher-level engineering Head.

## Core capabilities

- mandatory product routing before product-specific design decisions
- shared cross-product UI contracts for navigation, forms, feedback, state/recovery, destructive actions, accessibility, responsive adaptation, motion, and content hierarchy
- hardened local design system for tokens, typography, themes, density, component states, responsive/product variants, and migration governance
- websites with deep local rules for IA, trust, conversion, content/SEO UX, accessibility, responsive media, and performance
- dashboards with local executive, analytical, operational, monitoring/NOC, CRM/pipeline, and admin-management modes
- web applications with local browser/state/workflow UX rules
- mobile applications with local iOS, Android, and cross-platform mobile rules
- WordPress plugin/admin UI with local settings, onboarding/integration, diagnostics/operations, and Multisite rules
- new product and existing-product UI/UX work
- responsive design, Light/Dark themes, RTL/LTR, branding, and local typography
- design systems, personalization, operational UX, and Data Trust UX
- accessibility, performance, visual regression, and evidence-based QA
- safe preservation of business logic, permissions, data meaning, and existing user changes
- modular specialist routing instead of duplicating specialist knowledge

For Persian-facing UI, the external **`persian-writing`** Skill is required for Persian-language validation.

## Architecture

```text
Higher-level Engineering Head
            ↓
        UI/UX Skill
        (UI/UX Head)
            ↓
       Product Router
            ↓
      Required Product Pack
            ↓
  Scope-relevant Shared UI Rules

Specialist routing (for example persian-writing) is evaluated independently within its delegated domain.
```

Head-level scope, security, architecture, approvals, and UI/UX constraints always take precedence over lower-level specialists.

External specialist use is intentionally minimal: `persian-writing` is the only external specialist and is used for Persian-language validation.

## Quick use

Codex:

```text
$ui-ux-skill
```

Claude Code:

```text
/ui-ux-skill
```

## Documentation

- **[Roadmap](ROADMAP.md)** — ordered development plan and upcoming hardening stages
- **[How to Install / Update](INSTALL.md)** — installation, updates, migration from the old slug, and verification
- **[Updates & Changelog](CHANGELOG.md)** — release-by-release changes
- **[Skill Specification](skills/ui-ux-skill/SKILL.md)** — canonical Skill behavior and routing
- **[Product Registry](skills/ui-ux-skill/product-types.json)** — machine-readable product routes and required Product Packs
- **[Product Routing](skills/ui-ux-skill/references/product-routing.md)** — product classification and multi-route rules
- **[Shared UI Registry](skills/ui-ux-skill/shared-rules.json)** — machine-readable cross-product UI rule modules
- **[Shared UI Routing](skills/ui-ux-skill/references/shared-product-rules.md)** — scope loading, precedence, and non-duplication policy
- **[Design System Registry](skills/ui-ux-skill/design-system.json)** — machine-readable local design-system modules
- **[Design System Architecture](skills/ui-ux-skill/references/design-system-architecture.md)** — token hierarchy, themes, states, variants, governance, and runtime boundaries
- **[Specialist Registry](skills/ui-ux-skill/specialists.json)** — machine-readable Specialist sources and triggers
- **[Specialist Routing](skills/ui-ux-skill/references/specialist-routing.md)** — Head/Specialist authority, fallback, and freshness rules
- **[Contributing](CONTRIBUTING.md)** — contribution workflow
- **[Security](SECURITY.md)** — supported versions and security reporting

## Current source

**v2.8.0**

Canonical repository: **pooyahayati/UI-UX-Skill**  
Canonical Skill slug: **`ui-ux-skill`**

GitHub Releases are published automatically from the current `VERSION` after validated changes reach `main`.

## Author

**Pooya Hayati | پویا حیاتی**  
https://pooyahayati.com

## License

MIT
