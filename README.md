# UI/UX Skill

[![Validate](https://github.com/pooyahayati/UI-UX-Skill/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/pooyahayati/UI-UX-Skill/actions/workflows/validate-skill.yml)
![Version](https://img.shields.io/badge/version-3.1.1-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A production-oriented **Product-Aware UI/UX Head Skill** for designing, auditing, improving, and validating websites, dashboards, web applications, mobile applications, WordPress plugin/admin UI, and other production interfaces.

It can work independently or as a UI/UX specialist under a higher-level engineering Head.

## Product coverage

| Product | What this Skill accounts for |
| --- | --- |
| **Website** | Corporate/organization, service-business, product/brand, personal-brand/portfolio, publication/content, campaign/landing surfaces; information architecture, navigation, homepage/hero, landing/detail/editorial composition, content hierarchy, CTA/conversion, forms and lead generation, contact/support, trust/proof, pricing, site search, SEO-aware structure, structured data/breadcrumbs, internal linking, responsive media, performance, progressive enhancement, accessibility, privacy/consent, localization, Persian/RTL, edge pages, and Website QA. |
| **Dashboard** | Executive, analytical, operational, monitoring/NOC, CRM/pipeline, and admin/management modes; decision hierarchy, Data Trust UX, metric contracts, targets/baselines, filters, drill-down/traceability, tables/work queues, charts, cross-filtering, alerts, live updates, saved views/personalization, role-aware presentation, responsive dashboard architecture, accessibility, and RTL/mixed-direction data. |
| **Web Application** | Application shell and information architecture, browser history, URL/deep-link state, routed workflows, drafts/autosave/unsaved changes, state and recovery, long-running jobs, concurrency/conflicts, forms, search/filter/sort/saved state, overlays, keyboard/focus, custom interactions, destructive/reversible actions, file operations, feedback, responsive behavior, authentication/session/permissions, onboarding, motion, accessibility, and Persian/mixed-language behavior. |
| **Mobile Application** | Shared mobile UX plus local iOS/iPadOS, Android, and cross-platform rules; navigation intent, touch/reachability, safe areas/system UI, keyboard/IME, permissions, connectivity/offline/sync, lifecycle/state restoration, long-running work, deep links, notifications, dense-data adaptation, motion/haptics, VoiceOver/TalkBack, text scaling, large-screen/resizable behavior, and platform adaptation. |
| **WordPress Plugin / Admin UI** | Native settings extensions, plugin workspaces, and hybrid surfaces; wp-admin integration, menu/entry-point decisions, settings/configuration, onboarding/integrations, diagnostics/Site Health, background work, capabilities and permission-facing UX, Settings API semantics, notices, privacy/data lifecycle, reset/delete/uninstall behavior, updates/migrations, compatibility/dependencies, import/export, Multisite/Network Admin, responsive wp-admin, accessibility, localization, Persian/RTL, and appearance behavior. |
| **Shared foundation** | Product routing, scope-relevant Shared UI Rules for navigation/forms/feedback/state/destructive actions/accessibility/responsive adaptation/motion/content hierarchy, modular Design System foundations for tokens/typography/themes/density/component states/responsive variants/governance, new and existing-product workflows, personalization, runtime UI governance, visual regression, evidence-based QA, and preservation of business logic, permissions, data meaning, and user-authored changes. |

For Persian-facing UI, the external **`persian-writing`** Skill is required for Persian-language validation. It is the only external specialist; product design knowledge remains local.

## Architecture

```text
Higher-level Engineering Head
            ↓
        UI/UX Skill
        (UI/UX Head)
            ↓
       Product Router
            ↓
   Active Product Pack only
            ↓
 Scope-relevant local modules
            ↓
 Scope-relevant Shared UI Rules
            ↓
 Relevant Design System modules
```

Inactive Product Packs are not preloaded. Specialist routing is evaluated independently only when its trigger is active.

## Feature freeze

The current product model is feature-frozen for the `3.1.x` stabilization line. No new Product Types or major capability areas are planned. Work is limited to deduplication, context isolation, quality hardening, validation, documentation, and release maintenance unless the freeze is explicitly lifted.

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

- **[Roadmap](ROADMAP.md)** — completed capability roadmap and current feature-freeze policy
- **[How to Install / Update](INSTALL.md)** — installation, updates, migration from the old slug, and verification
- **[Updates & Changelog](CHANGELOG.md)** — release-by-release changes
- **[Skill Specification](skills/ui-ux-skill/SKILL.md)** — canonical Skill behavior and routing
- **[Product Registry](skills/ui-ux-skill/product-types.json)** — machine-readable product routes and required Product Packs
- **[Product Routing](skills/ui-ux-skill/references/product-routing.md)** — product classification, isolation, and multi-route rules
- **[Shared UI Registry](skills/ui-ux-skill/shared-rules.json)** — machine-readable cross-product UI rule modules
- **[Shared UI Routing](skills/ui-ux-skill/references/shared-product-rules.md)** — scope loading, precedence, and non-duplication policy
- **[Design System Registry](skills/ui-ux-skill/design-system.json)** — machine-readable local design-system modules
- **[Design System Architecture](skills/ui-ux-skill/references/design-system-architecture.md)** — token hierarchy, themes, states, variants, governance, and runtime boundaries
- **[Real-World Evaluation](evals/real-world/RESULTS.md)** — five-product evaluation results and limitations
- **[Specialist Registry](skills/ui-ux-skill/specialists.json)** — machine-readable specialist sources and triggers
- **[Specialist Routing](skills/ui-ux-skill/references/specialist-routing.md)** — Head/Specialist authority, fallback, and freshness rules
- **[Contributing](CONTRIBUTING.md)** — contribution workflow
- **[Security](SECURITY.md)** — supported versions and security reporting

## Current source

**v3.1.1**

Canonical repository: **pooyahayati/UI-UX-Skill**  
Canonical Skill slug: **`ui-ux-skill`**

GitHub Releases are published automatically from the current `VERSION` after validated changes reach `main`.

## Author

**Pooya Hayati | پویا حیاتی**  
https://pooyahayati.com

## License

MIT
