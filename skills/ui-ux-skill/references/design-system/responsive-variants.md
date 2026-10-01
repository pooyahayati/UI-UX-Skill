# Design System Responsive Tokens and Product Variants

Use when the design system must adapt across viewport/window size, platform, product type, or density contexts.

Read the Shared Responsive rule for product behavior. This module owns design-system resolution and reusable variants.

## Responsive architecture

Responsive design-system values should exist only when repeated component/foundation behavior benefits from them.

Potential responsive token domains:

- container width;
- page gutter;
- typography role size;
- spacing role;
- pane width;
- navigation presentation;
- component layout mode.

Do not tokenize every media query.

## Breakpoints

Treat breakpoints as layout transition points, not device model labels.

A design system may expose named ranges such as:

- compact
- medium
- expanded

or use the project's existing framework breakpoints.

Do not migrate a stable breakpoint system merely for naming consistency.

## Responsive token resolution

A responsive token may resolve differently by context while keeping semantic identity.

Example:

`space.page-gutter`

may resolve to different values for compact and expanded layouts.

Avoid cascading arbitrary overrides across many files.

## Component variants

Components may expose purposeful responsive variants.

Examples:

- navigation: full -> compact -> temporary
- table: full columns -> priority columns + detail
- toolbar: inline -> wrapped -> overflow
- split pane: dual -> single pane

The Product Pack decides whether a transformation is appropriate.

The Design System defines how the supported variant is represented consistently.

## Product variants

Product variants allow one design system to adapt to product semantics.

Examples:

- dashboard.compact-density
- website.editorial-measure
- wordpress.host-compatible-controls
- mobile.platform-adapted-navigation

Product variants should specialize approved tokens/components, not fork the entire system.

## Variant precedence

Use deterministic resolution:

1. locked foundation
2. theme context
3. responsive context
4. product variant
5. validated owner setting
6. allowed user preference
7. safe fallback

When two contexts conflict, document which one owns the affected token.

## Variant explosion

Avoid creating every possible cross-product combination.

Prefer orthogonal contexts with clear ownership.

Do not maintain separate full token sets for:

- Light desktop dashboard
- Dark desktop dashboard
- Light mobile dashboard
- Dark mobile dashboard

when theme + responsive + product contexts can resolve independently.

## RTL/LTR

Direction should normally be an orthogonal context.

Use logical tokens/implementation where possible.

Do not duplicate a complete RTL token set solely to mirror physical values.

## Validation

Test supported matrices intentionally:

- Light/Dark;
- high contrast where applicable;
- compact/medium/expanded;
- RTL/LTR;
- product variants;
- density variants;
- representative component states.

Use pairwise/risk-based coverage when the full Cartesian matrix would be excessive.
