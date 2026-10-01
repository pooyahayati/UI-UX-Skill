# Design Discovery and Design Profile

Use for new products, major redesigns, or strategic changes to an existing visual system.

Do not run full discovery when a narrow existing-product fix can be resolved from the current baseline.

## Modes

### Full Discovery

Use for new products or substantial system replacement.

### Partial Rediscovery

Use when only selected strategic fields need reconsideration, such as:

- palette
- typography
- logo or brand direction
- density
- navigation
- theme strategy
- responsive priority
- visual personality
- runtime appearance governance
- user personalization

### Reuse Existing Profile

Use when an approved `design-profile.md` exists and remains appropriate.

## Recommendation-first discovery

For unresolved strategic decisions:

1. recommend the strongest option
2. give a short product-specific reason
3. offer a small number of alternatives
4. offer Custom
5. accept "use your recommendation" as delegated approval where appropriate

Inspect repository and assets before asking questions.

## Product route first

Before full or partial discovery, read `../product-types.json` and `product-routing.md`.

Record one primary product route and any genuinely applicable secondary routes.

The active Product Pack constrains product-specific discovery questions. Do not ask dashboard-specific questions for a mobile app, mobile-specific questions for a web application, or WordPress-admin questions for an unrelated product.

## Decisions to resolve when relevant

- primary product route
- secondary product routes when applicable
- product and domain
- user roles
- high-frequency workflows
- operational vs analytical usage
- language and direction
- visual style
- personality
- density
- design freedom
- brand and logo scope
- font and font source
- bilingual font strategy
- palette
- Light/Dark
- surface and radius
- icon system
- responsive priority
- navigation
- date, time, digits, currency, timezone, and calendar
- motion
- auth and system-page scope
- accessibility target
- role-aware UX needs
- saved views and recurring preference needs
- data freshness/metric-trust requirements
- whether runtime owner customization is justified
- which fields are owner-configurable
- which fields are user-configurable
- which fields must remain code-only or locked
- validation/evidence expectations for major redesigns
- whether visual-regression capture is available
- domain-specific risk/workflow constraints when they materially affect UI

## Runtime governance decision

Do not assume every project needs an Owner UI/UX Control Center.

Recommend it only when product value justifies the complexity.

Useful triggers include:

- white-label or multi-tenant product
- frequent brand/theme changes
- non-developer owner needs safe presentation controls
- multiple environments or deployments share design configuration
- operational defaults need runtime adjustment
- users need meaningful personalization

If enabled, read:

- `design-system-architecture.md`
- `runtime-ui-governance.md`
- `personalization-and-data-ux.md`

Resolve the configuration hierarchy:

`Locked Constraints -> Design System Defaults -> Published Owner Config -> User Preferences`

## Brand change scope

Explicitly distinguish:

- preserve identity and improve treatment
- refresh palette, typography, or visual language
- redesign actual logo or identity
- use supplied new brand assets

Actual identity replacement requires explicit user intent.

## Design Profile schema

Use a concise Markdown or YAML-like structure. Include provenance so future work can tell what was observed vs approved.

Example:

```yaml
profile_version: 4
skill_version: 2.5.0
status: approved
updated_at: 2026-09-20

product:
  primary_route: dashboard
  secondary_routes: []
  route_source: user-provided
  type: operational-dashboard
  users: [admin, operator]
  primary_workflows:
    - review queue
    - update record

direction:
  languages: [fa, en]
  rtl: true
  ltr: true

visual:
  style: professional
  personality: calm
  density: high
  freedom: balanced

brand:
  change_scope: treatment-only
  logo_source: existing
  palette: approved-semantic-tokens
  typography: local-font

theme:
  modes: [light, dark]
  default: system

responsive:
  priority: desktop-first
  supported: [large-desktop, desktop, laptop, tablet, mobile]

runtime_governance:
  enabled: true
  owner_role: system-owner
  owner_configurable:
    - theme.default
    - brand.primary
    - visual.density
    - tables.default_page_size
  user_configurable:
    - theme.preference
    - visual.density
    - tables.visible_columns
    - saved_views
  code_only:
    - navigation.destinations
    - authentication
    - permissions
  preview_publish_rollback: true

data_ux:
  show_last_updated: true
  show_filter_scope: true
  timezone: product-locale
  saved_views: true

validation:
  visual_regression: representative
  ux_evidence: use-when-available
  performance_budget: existing-or-baseline-delta

decisions:
  - field: visual.density
    value: high
    source: user-approved
  - field: brand.logo_source
    value: existing
    source: observed-baseline
  - field: runtime_governance.enabled
    value: true
    source: delegated-recommendation

locked_constraints:
  - preserve authentication flow
  - do not change brand mark
  - owner config cannot alter permissions

open_questions: []
```

## Status

Use:

- `draft` while strategic choices remain unresolved
- `approved` after user approval or explicit delegated authority

## Decision source

Useful values:

- user-provided
- user-approved
- delegated-recommendation
- observed-baseline
- existing-profile

Do not represent an inferred decision as user-approved.

## Configurability classification

For products with runtime or user configuration, classify design decisions as:

- `locked` — cannot be changed through runtime presentation settings
- `owner-configurable` — controlled product-wide or tenant-wide setting
- `user-configurable` — personal preference within allowed bounds
- `code-only` — requires implementation/deployment

Avoid unclear ownership of configuration.

## Updates

Before major UI work:

- read the profile
- respect locked constraints
- avoid re-asking resolved questions
- update only affected strategic fields
- preserve provenance
- update `skill_version` when materially revising the profile with a newer Skill
- re-evaluate `primary_route` and `secondary_routes` when the product surface materially changes
- migrate runtime-governance fields carefully when the schema changes
- reconcile stored preferences/saved views when owner or schema constraints change
- update validation/evidence expectations when the redesign scope changes
