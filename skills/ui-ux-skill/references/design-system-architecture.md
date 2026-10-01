# Design System Architecture and Changeability

Use this reference when implementing or auditing a product UI that must remain easy to change after initial delivery.

The goal is controlled changeability, not unlimited theming.

Read `implementation-strategies.md` when mapping this architecture into an existing framework or styling stack.

## Architecture principle

Prefer this flow:

`Design Profile -> Design System Defaults -> Semantic Tokens -> Component Tokens -> Components -> Pages`

When runtime customization is justified:

`Locked Constraints -> Design System Defaults -> Published Owner Config -> User Preferences -> Resolved Runtime Tokens`

Pages should consume stable components/tokens rather than repeat visual values.

## Token layers

### Primitive tokens

Raw scales such as:
- color ramps
- spacing scale
- typography scale
- radius scale
- elevation values
- motion durations

Primitive tokens are implementation building blocks. They are usually not directly editable by non-developers.

### Semantic tokens

Product meanings such as:
- background
- surface
- surface-muted
- text-primary
- text-secondary
- border
- primary
- focus
- success
- warning
- danger
- info

Owner-facing configuration should normally map to semantic tokens, not arbitrary primitives.

### Component tokens

Component-level meanings such as:
- button-primary-bg
- input-border
- table-row-height
- sidebar-width
- chart-grid
- dialog-elevation

Use them only where a global semantic token is too broad.

## Avoid hard-coded presentation

Audit for repeated raw values in:
- components
- pages
- inline styles
- chart configs
- conditional classes
- theme-specific branches

Prefer central variables/tokens for values expected to change.

Do not abstract one-off values merely to increase indirection.

## Configuration schema

When runtime design configuration is needed, define a typed/versioned schema.

Example:

```json
{
  "schemaVersion": 1,
  "theme": {
    "defaultMode": "system",
    "allowedModes": ["light", "dark", "system"]
  },
  "brand": {
    "primary": "#0F766E",
    "accent": "#2563EB",
    "logoLight": "/brand/logo-light.svg",
    "logoDark": "/brand/logo-dark.svg"
  },
  "density": "balanced",
  "radius": "medium",
  "motion": "standard",
  "navigation": {
    "defaultState": "expanded"
  },
  "tables": {
    "defaultPageSize": 25
  }
}
```

Do not store executable code inside design configuration.

## Validation boundaries

Each configurable field should define:

- type
- allowed values or range
- fallback/default
- role allowed to change it
- whether it requires preview
- whether it is user-overridable
- accessibility constraints
- compatibility/migration behavior

Examples:

- page size: integer from approved set
- density: enum
- radius: preset enum rather than arbitrary CSS
- color: valid color plus contrast validation
- logo: approved asset type/size/path
- font: allowlisted project font family/preset

## Precedence

Resolve configuration deterministically.

Recommended precedence:

1. locked product constraints
2. design-system defaults
3. published owner configuration
4. user preferences for explicitly user-configurable fields
5. safe runtime fallback when a value is missing or invalid

A user preference must never override a locked or non-user-configurable field.

## Storage

Choose storage based on product architecture.

Possible locations:
- database configuration record
- tenant settings
- server-side configuration service
- versioned JSON/YAML for build-time-only products
- local user preference storage for non-sensitive personal preferences

Do not put authorization decisions solely in browser storage.

For multi-tenant products, scope owner configuration to the correct tenant/account.

## Server/client behavior

Avoid theme/config flashes and hydration mismatch.

Where relevant:
- resolve critical theme/config values before first meaningful render
- cache safely
- invalidate cache after publish
- provide deterministic server/client fallbacks
- avoid blocking the whole application on non-critical appearance settings

## Schema evolution

Runtime configuration needs migrations.

When changing schema:
- increment `schemaVersion`
- provide defaults for new fields
- migrate or safely ignore removed fields
- preserve rollback compatibility when practical
- test older published configs

## Component contracts

Components should expose purposeful variants rather than raw styling escape hatches.

Prefer:

`<Button intent="primary" size="md" />`

over passing arbitrary style fragments throughout the product.

Do not make every component infinitely configurable.

## Testing changeability

A maintainable design system should pass practical change tests, for example:

- changing primary semantic color updates expected components without editing pages
- changing density updates tables/forms consistently
- Light/Dark logo variants switch correctly
- changing approved typography does not break common layouts
- user preference overrides only permitted fields
- invalid owner config falls back safely

## Developer handoff

Document:
- token source
- config schema
- precedence
- owner-configurable fields
- user-configurable fields
- code-only fields
- migration process
- fallback behavior
- relevant tests

Changeability is a product capability and should be understandable without reverse-engineering every component.
