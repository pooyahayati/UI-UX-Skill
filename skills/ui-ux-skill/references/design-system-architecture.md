# Design System Architecture and Changeability

Use this reference when implementing, auditing, or migrating a reusable product UI design system.

The goal is controlled, testable changeability—not unlimited theming.

Machine-readable registry:

`../design-system.json`

## Architecture

Use this conceptual flow:

`Design Profile -> Primitive Tokens -> Semantic Tokens -> Component Tokens -> Product Variants -> Resolved Runtime Tokens -> Components -> Product Surfaces`

When runtime customization exists:

`Persisted Config -> Validation/Migration -> Policy Resolution -> Preference Reconciliation -> Resolved Runtime Tokens`

Pages and product surfaces should consume stable component/token contracts rather than raw owner settings or repeated visual values.

## Required module routing

Load only the modules relevant to the task.

### Tokens and foundations

`design-system/tokens-foundations.md`

Owns:

- primitive / semantic / component token hierarchy;
- product variants;
- token naming/types;
- aliases/references;
- source vs resolved tokens;
- DTCG-compatible interchange;
- logical-direction token principles.

### Typography

`design-system/typography.md`

Owns:

- semantic typography roles;
- type scales;
- label/body/data/code roles;
- Persian/Latin pairing;
- font loading;
- responsive typography.

### Color and theme

`design-system/color-theme.md`

Owns:

- semantic color roles;
- Light/Dark;
- High Contrast / Forced Colors;
- contrast;
- status color;
- chart palette roles;
- owner-configurable palette boundaries.

### Spacing, density, and layout

`design-system/spacing-density-layout.md`

Owns:

- spacing scale and semantic spacing;
- density presets;
- control sizing;
- layout foundations;
- radius;
- elevation.

### Component states

`design-system/component-states.md`

Owns:

- interactive state inventory;
- state semantics;
- focus/selected/disabled/read-only distinctions;
- loading/validation state;
- state tokens;
- state/theme matrix.

### Responsive tokens and product variants

`design-system/responsive-variants.md`

Owns:

- reusable responsive-token architecture;
- breakpoint/range strategy;
- component variants;
- product variants;
- variant precedence;
- variant-explosion control.

### Governance and migration

`design-system/governance-migration.md`

Owns:

- lifecycle;
- deprecation;
- alias migration;
- breaking-change classification;
- impact analysis;
- runtime configuration boundary;
- visual-regression compatibility;
- ownership.

## Stable token interchange

When machine-readable design-token interchange is useful, prefer compatibility with the stable DTCG 2025.10 specification.

This does not require migrating a stable existing token format solely for standardization.

Use DTCG concepts such as:

- `$value`;
- `$type`;
- groups;
- references/aliases;
- composite values;
- extensions.

Do not implement against a newer unstable draft merely because it is newer.

## Authority and precedence

Use:

`Product Pack -> Shared Product UI Rule -> Design System Contract -> Product Variant -> Runtime Configuration -> Allowed User Preference -> Component Implementation`

Interpret this carefully:

- Product Packs own product/host/platform semantics.
- Shared Rules own cross-product behavioral contracts.
- Design System owns reusable visual/interaction primitives and component contracts.
- Product variants specialize approved token/component behavior.
- Runtime configuration selects only approved design-system values/presets.
- User preferences affect only explicitly permitted fields.
- Component implementation must preserve all higher-level semantics.

No lower layer may weaken:

- accessibility;
- security;
- authorization;
- truthful state;
- user-data integrity.

## Design-system defaults vs runtime settings

Design-system source is not the same as runtime owner configuration.

Design-system source defines:

- token structure;
- semantic roles;
- component states;
- variant capabilities;
- safe ranges/presets;
- theme resolution;
- migration rules.

Runtime configuration may choose from approved values.

Runtime configuration must not redefine:

- token aliases;
- component state model;
- breakpoint logic;
- arbitrary component CSS;
- security/permission rules;
- workflow/business logic.

Read `runtime-ui-governance.md` for owner controls.

## Existing systems

Reuse the project's current architecture where it can support the required contracts.

Do not migrate frameworks, styling libraries, or token formats solely for architectural purity.

Read `implementation-strategies.md` to map the design-system contract into:

- CSS variables;
- utility-first CSS;
- theme objects/providers;
- CSS-in-JS;
- preprocessors;
- existing component libraries;
- framework-native theming.

## Avoid hard-coded presentation

Audit repeated raw values in:

- components;
- pages;
- inline styles;
- chart configs;
- theme branches;
- runtime configuration adapters.

Centralize values that represent a real repeated design decision.

Do not abstract one-off values merely to increase indirection.

## Component contracts

Components should expose purposeful variants.

Prefer:

`<Button intent="primary" size="md" />`

over raw style fragments passed throughout product code.

Do not make every component infinitely configurable.

Every reusable interactive component should define its relevant states through `design-system/component-states.md`.

## Product variants

Do not create separate design systems for Website, Dashboard, Web App, Mobile, and WordPress.

Use product variants only where reusable system behavior genuinely differs.

Examples:

- dashboard compact data density;
- website editorial reading measure;
- WordPress host-compatible admin controls;
- mobile platform-adapted control metrics.

The active Product Pack remains authoritative for whether a variant is appropriate.

## RTL/LTR

Use one coherent design system for RTL and LTR.

Prefer logical direction concepts and CSS logical properties where applicable.

Read `rtl-ltr-typography.md` for direction/localization architecture and `design-system/typography.md` for typography-system integration.

Do not create a duplicated RTL token system merely to mirror left/right.

## Testing changeability

A hardened design system should pass practical change tests such as:

- changing a semantic color updates expected components without page edits;
- Light/Dark/High Contrast preserve meaning;
- changing supported density updates controls/tables consistently;
- typography changes do not break representative layouts;
- component state semantics survive theme/product variants;
- responsive tokens resolve without page-level override sprawl;
- product variants preserve base contracts;
- invalid runtime configuration falls back safely;
- user preferences override only allowed fields;
- deprecated token aliases migrate without silently changing meaning.

## Visual regression

Read `visual-regression.md` for rendered evidence.

Design-system changes should identify affected baseline dimensions:

- themes;
- component states;
- density;
- typography;
- responsive contexts;
- RTL/LTR;
- product variants.

A screenshot difference is not automatically a regression; expected token-driven changes should be documented.

## Developer handoff

Document:

- token source;
- token format/interchange;
- semantic roles;
- component-state contract;
- theme contexts;
- density/layout roles;
- responsive/product variants;
- runtime configuration boundary;
- user preference boundary;
- migration/deprecation process;
- fallback behavior;
- ownership;
- relevant tests and visual baselines.

Changeability should be understandable without reverse-engineering every page.

## Current canonical references

When standards details may have changed, verify current sources.

Relevant references include:

- Design Tokens Community Group stable specification;
- WCAG 2.2;
- CSS Color Adjustment / Forced Colors;
- CSS Logical Properties and Values.

These external specifications inform the local design-system contract; they are not external design Skill dependencies.
