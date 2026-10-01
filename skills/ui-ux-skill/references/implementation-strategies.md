# Implementation Strategies for Design Systems

Use this reference after choosing the architecture. Adapt to the project's existing stack.

The objective is stable semantic contracts, not framework migration.

## General rule

Prefer:

`existing theme mechanism -> semantic tokens -> component contracts -> pages`

Do not introduce a new styling system when the current one can support the required architecture.

## CSS variables

CSS custom properties are a strong runtime-token boundary when the product needs dynamic theme or owner configuration.

Example:

```css
:root {
  --color-bg: ...;
  --color-surface: ...;
  --color-text: ...;
  --color-primary: ...;
  --radius-control: ...;
  --table-row-height: ...;
}
```

Components consume semantic variables rather than owner-config values directly.

Validate and resolve runtime configuration before mapping it to variables.

## Utility-first CSS

For utility-based systems:

- keep semantic values in theme variables/tokens
- let utilities reference the semantic layer
- avoid scattering arbitrary hex/spacing values across markup
- use variants/components for repeated interactive patterns

If runtime theming is required, prefer variables under the utility layer rather than regenerating every class at runtime.

## shadcn-style component stacks

When a project already uses CSS-variable-based component foundations:

- preserve the existing component primitives
- map brand/semantic tokens into the shared variable layer
- normalize component variants instead of editing each screen
- treat generated/default styling as a starting point, not final product design

Do not migrate solely to use a specific component kit.

## Theme-object libraries

For systems built around a theme/provider object:

- map primitive and semantic tokens into the existing theme shape
- centralize component overrides
- use supported theme extension points
- avoid local overrides that bypass the theme without a documented reason

Runtime owner configuration should produce a validated theme input, not arbitrary style objects.

## CSS-in-JS

If the project uses CSS-in-JS:

- keep semantic tokens centralized
- avoid computing expensive theme objects on every render
- memoize/rescope only where necessary
- keep server/client theme resolution deterministic when SSR is involved

## SCSS or preprocessor tokens

For build-time-only products:

- use variables/maps for stable scales
- generate semantic classes/tokens where useful
- do not pretend build-time SCSS variables provide runtime owner customization

If runtime configuration becomes a requirement, introduce a runtime-safe layer such as CSS variables without rewriting unrelated styling.

## Vue/Nuxt, Angular, and other component frameworks

The same principles apply:

- use the framework's existing provider/injection/theme mechanism
- keep semantic tokens independent of page implementation
- centralize reusable component variants
- resolve critical theme state early in SSR/hydration flows
- preserve existing component conventions

Do not force React-specific patterns into a non-React project.

## Charts

Chart libraries often bypass application tokens.

Create a chart-theme adapter for:

- semantic series palette
- grid
- text
- tooltip
- status/reference lines
- Light/Dark

Do not duplicate chart color arrays in every screen.

## Icons

Prefer an existing coherent icon family.

Centralize semantic icon choices where product meaning matters.

Do not make arbitrary owner-uploaded SVG code executable inside the application.

## Runtime configuration adapter

Keep raw persisted owner configuration separate from resolved UI tokens.

Prefer:

```text
Persisted Config
      ↓
Schema Validation
      ↓
Migration
      ↓
Policy/Permission Resolution
      ↓
Preference Reconciliation
      ↓
Resolved Theme/Tokens
      ↓
UI
```

This boundary makes rollback and schema evolution safer.

## Tests

Useful implementation-level tests:

- token contract unit tests
- config schema tests
- migration tests
- theme resolution tests
- component visual tests
- Light/Dark/RTL/LTR screenshots
- invalid-config fallback
- user-preference precedence
- no flash/hydration regression where relevant

## Migration strategy

When converting hard-coded UI to tokens:

1. inventory repeated values
2. identify semantic roles
3. create a minimal token layer
4. migrate representative/high-value components
5. validate rendered output
6. expand incrementally
7. remove obsolete raw values only when safe

Avoid a single huge rewrite unless the existing architecture makes incremental migration impossible.
