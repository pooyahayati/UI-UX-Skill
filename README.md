# Production Dashboard UI/UX Skill

[![Validate](https://github.com/pooyahayati/production-dashboard-ui-ux-skill/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/pooyahayati/production-dashboard-ui-ux-skill/actions/workflows/validate-skill.yml)
![Version](https://img.shields.io/badge/version-1.5.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A production-oriented Agent Skill for designing, auditing, improving, and redesigning dashboards, admin panels, CRM, analytics, and operational product interfaces.

It supports standalone or Head-delegated UI/UX work, specialist routing, existing-product audits, evidence-driven UX improvement, visual regression, responsive UI, Persian RTL / English LTR, Light/Dark themes, reusable design systems, runtime design governance, personalization, Data Trust UX, accessibility, and performance.

## Quick start

### OpenAI Codex

```text
Use $skill-installer to install this skill from:
https://github.com/pooyahayati/production-dashboard-ui-ux-skill/tree/main/skills/production-dashboard-ui-ux-skill
```

Then:

```text
Use $production-dashboard-ui-ux-skill to audit and improve this dashboard.
```

### Claude.ai / Claude Desktop

Download the Claude-ready ZIP from the latest Release, then upload it from **Customize → Skills** and enable it.

### Claude Code

Extract the Claude-ready ZIP into:

```text
~/.claude/skills/
```

or project-local:

```text
<project>/.claude/skills/
```

Then invoke:

```text
/production-dashboard-ui-ux-skill
```

## What the Skill covers

- new dashboard/product UI design
- existing-product UI/UX audit and improvement
- evidence/confidence-based findings instead of taste-only critique
- representative before/after visual-regression evidence
- tables, forms, filters, charts, search, bulk actions, and long-running jobs
- real-time operational dashboards and stale/disconnected states
- domain-aware reasoning for CRM, support, ERP, finance, operations, security, and similar products
- Persian RTL, English LTR, bilingual typography/localization
- responsive/mobile product behavior
- Light/Dark themes, branding, logo treatment, local fonts
- accessibility and frontend performance
- reusable semantic design tokens and component contracts
- safe Owner UI/UX Control Center when runtime customization is justified
- user preferences, Saved Views, role-aware UX, and preference reconciliation
- Data Trust UX: freshness, timezone, filter scope, metric definitions, partial/stale data
- working-tree, permissions, business-logic, and regression safety

## Existing product workflow

```text
Baseline
→ Audit
→ Prioritize
→ Fix
→ Validate
→ Compare
→ Refine
```

The Skill preserves functional contracts and user-authored changes unless changes are explicitly authorized.

For broad visual changes it records actual visual QA coverage and, when screenshot/browser tooling is available, uses a representative baseline and before/after comparison.

## Head and specialist routing

The Skill can work as:

```text
Standalone UI/UX Head
or
UI/UX Specialist under a higher-level engineering Head
```

It preserves upstream scope, risk, architecture, security, and acceptance criteria when delegated.

For Persian-facing interfaces, the external `persian-writing` Skill is REQUIRED:

```text
https://github.com/ali2000hos/persian-writing
```

The Head intentionally does not copy that specialist's language methodology. It keeps only trigger, authority, fallback, and handoff rules. Head-level product, security, scope, architecture, and UI/UX constraints always take precedence.

Specialists are referenced by canonical source, not by pinned version. When tooling allows, the Head verifies that itself and required specialists are installed and current, updates known-stale copies before relying on them, and reports freshness as unverified when it cannot be checked.

Browser runtime validation can optionally use `browser-testing-with-devtools` when installed and current.

See `specialist-routing.md` for the full authority, freshness, fallback, and handoff contract.

## Runtime design governance

The optional configuration hierarchy is:

```text
Locked Product Constraints
        ↓
Design System Defaults
        ↓
Published Owner Config
        ↓
User Preferences
```

Owner runtime settings use typed/allowlisted configuration and should support, where appropriate:

```text
Draft → Preview → Validate → Publish → Version History / Rollback
```

Arbitrary CSS, JavaScript, HTML, permissions, authentication, security controls, and business logic are not treated as appearance settings.

## Updating

For a Codex installation made with `$skill-installer`:

```text
Update $production-dashboard-ui-ux-skill to the latest version from:
https://github.com/pooyahayati/production-dashboard-ui-ux-skill/tree/main/skills/production-dashboard-ui-ux-skill

Remove the currently installed copy if necessary, then reinstall it with $skill-installer.
```

The installer does not overwrite an existing destination. If the updated Skill is not detected immediately, restart Codex or start a new session.

For Claude.ai / Claude Desktop, replace the uploaded Skill with the ZIP from the newest Release.

For Claude Code, replace the installed Skill folder with the folder from the newest Claude-ready ZIP.

## Behavioral evals

Version 1.5 includes executable eval preparation and result-validation tooling plus reusable fixture projects.

```bash
python3 scripts/validate_eval_fixtures.py
python3 scripts/prepare_eval_run.py existing-safe-improvement --output /tmp/uiux-eval
python3 scripts/validate_eval_result.py eval-result.json --require-all
```

Fixtures cover:

- existing dashboard safety/changeability
- Owner runtime configuration
- Persian RTL table behavior
- analytics/Data Trust UX
- real-time operations
- Head-delegated UI/UX routing
- required Persian language specialist routing

The harness makes behavioral testing repeatable, but it does not claim to test a model unless the prepared case is actually run in Codex/Claude and the result is recorded.

## Validation

```bash
python3 scripts/validate_release.py
python3 scripts/validate_eval_fixtures.py
python3 scripts/package_release.py --output dist
```

CI additionally runs OpenAI's current Skill validator and a real Codex `$skill-installer` smoke test.

## Structure

The canonical Skill source is:

```text
skills/production-dashboard-ui-ux-skill/
```

Key references include:

- `specialist-routing.md`

- `existing-product-audit.md`
- `ux-evidence-and-metrics.md`
- `visual-regression.md`
- `design-system-architecture.md`
- `implementation-strategies.md`
- `runtime-ui-governance.md`
- `preference-reconciliation.md`
- `personalization-and-data-ux.md`
- `operational-interaction-patterns.md`
- `domain-patterns.md`
- `rtl-ltr-typography.md`
- `accessibility.md`
- `performance.md`
- `qa-checklist.md`

## Releases

Latest release: **v1.5.0**

Release assets include:

- Claude-ready Skill ZIP
- OpenAI portable Plugin ZIP
- SHA-256 checksums

## Community and security

- [CONTRIBUTING.md](CONTRIBUTING.md)
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- [SECURITY.md](SECURITY.md)
- [PRIVACY.md](PRIVACY.md)
- [TERMS.md](TERMS.md)
- [SUPPORT.md](SUPPORT.md)

## Author

**Pooya Hayati | پویا حیاتی**

[Pooyahayati.com](https://pooyahayati.com)

## License

MIT
