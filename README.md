# UI/UX Skill

[![Validate](https://github.com/pooyahayati/UI-UX-Skill/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/pooyahayati/UI-UX-Skill/actions/workflows/validate-skill.yml)
![Version](https://img.shields.io/badge/version-2.1.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A production-oriented **Product-Aware UI/UX Head Skill** for designing, auditing, improving, and validating dashboards, web applications, mobile applications, WordPress plugin settings/admin UI, and other production interfaces.

It can work independently or as a UI/UX specialist under a higher-level engineering Head.

## Core capabilities

- mandatory product routing before product-specific design decisions
- dashboards and operational data interfaces
- web applications and mobile applications
- WordPress plugin settings/admin UI
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
      Specialist Skills
```

Head-level scope, security, architecture, approvals, and UI/UX constraints always take precedence over lower-level specialists.

Specialists are referenced by canonical source and should use the latest stable available version rather than a version pinned inside this Skill.

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

- **[How to Install / Update](INSTALL.md)** — installation, updates, migration from the old slug, and verification
- **[Updates & Changelog](CHANGELOG.md)** — release-by-release changes
- **[Skill Specification](skills/ui-ux-skill/SKILL.md)** — canonical Skill behavior and routing
- **[Product Registry](skills/ui-ux-skill/product-types.json)** — machine-readable product routes and required Product Packs
- **[Product Routing](skills/ui-ux-skill/references/product-routing.md)** — product classification and multi-route rules
- **[Specialist Registry](skills/ui-ux-skill/specialists.json)** — machine-readable Specialist sources and triggers
- **[Specialist Routing](skills/ui-ux-skill/references/specialist-routing.md)** — Head/Specialist authority, fallback, and freshness rules
- **[Contributing](CONTRIBUTING.md)** — contribution workflow
- **[Security](SECURITY.md)** — supported versions and security reporting

## Current source

**v2.1.0**

Canonical repository: **pooyahayati/UI-UX-Skill**  
Canonical Skill slug: **`ui-ux-skill`**

GitHub Releases are tag-driven, so the latest published Release can temporarily lag behind the current source version.

## Author

**Pooya Hayati | پویا حیاتی**  
https://pooyahayati.com

## License

MIT
