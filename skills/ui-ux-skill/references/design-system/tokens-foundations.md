# Design System Tokens and Foundations

Use when defining, implementing, auditing, or migrating design tokens.

This module owns the token model. Product Packs and Shared Rules consume tokens but should not redefine the token architecture.

## Token architecture

Use this conceptual flow:

`Design Handbook -> Primitive Tokens -> Semantic Tokens -> Component Tokens -> Product Variants -> Resolved Runtime Tokens -> Components -> Product Surfaces`

The handbook records accepted intent and links to real token sources; it is not a parallel editable token-value database. See [handbook authority and migration](../design-handbook.md).

Do not let pages consume raw design configuration directly.

## Primitive tokens

Primitive tokens are raw reusable scales.

Examples:

- color ramps
- spacing scale
- type size scale
- font weight scale
- radius scale
- elevation values
- motion durations
- opacity levels
- control-size scale

Primitive tokens do not carry product intent.

Avoid using primitive names directly in product UI when a semantic role exists.

## Semantic tokens

Semantic tokens express stable UI meaning.

Examples:

- surface.canvas
- surface.default
- surface.raised
- text.primary
- text.secondary
- text.disabled
- border.default
- border.strong
- action.primary
- focus.ring
- status.success
- status.warning
- status.danger
- status.info

Semantic meaning should survive theme changes.

Do not name semantic tokens after a current color such as `blue-500-button`.

## Component tokens

Use component tokens only when a component needs a stable role that cannot be expressed safely by global semantic tokens.

Examples:

- button.primary.background
- input.border.focus
- table.row.height
- dialog.elevation
- sidebar.width

Do not create a component token for every CSS property.

## Product variants

A Product Pack may specialize design-system decisions without creating a separate design system.

Examples:

- Dashboard may use compact table density.
- Website may use wider editorial spacing.
- WordPress Plugin may preserve host-compatible control sizing.
- Mobile may adapt platform typography/control metrics.

Product variants must resolve back to the same semantic/component contracts.

Do not fork token namespaces by product unless semantics genuinely differ.

## Token naming

Token names should describe role before implementation.

Prefer stable dot-paths or equivalent structured names.

Avoid:

- current raw value in the name;
- page-specific names that cannot be reused;
- arbitrary abbreviations;
- direction-specific left/right names when a logical start/end meaning exists.

## Token type

Every machine-readable token should have a known type.

Examples:

- color
- dimension
- number
- fontFamily
- fontWeight
- duration
- cubicBezier
- shadow
- border
- gradient
- typography

Do not infer type only from a token name when the interchange format supports explicit typing.

## Values and references

Prefer references/aliases when one token intentionally inherits another token's value.

Examples:

`text.secondary -> color.neutral.700`

`button.primary.background -> action.primary`

Aliases should represent intentional dependency.

Avoid circular references.

Do not use aliases to conceal unrelated semantics that merely share today's value.

## DTCG interchange

When a machine-readable token interchange format is needed, prefer compatibility with the stable DTCG 2025.10 format.

Relevant concepts include:

- `$value`
- `$type`
- groups
- aliases/references
- composite token values
- extensions

DTCG compatibility is an interchange recommendation, not a requirement to rewrite an existing design system that already has a stable typed token format.

Do not implement against an unstable future draft merely because it is newer.

## Source vs resolved tokens

Keep source tokens distinct from resolved runtime values.

A source token may reference:

- another token;
- a theme context;
- a product variant.

Resolved runtime tokens should contain the effective values consumed by the implementation.

Do not persist calculated runtime output as the canonical source when the source model can be preserved.

## Logical direction tokens

Prefer logical concepts where direction is semantic:

- inline-start
- inline-end
- block-start
- block-end

Do not convert every physical asset/property into a logical token; physical direction may still be correct for maps, media, physical controls, charts, or domain-specific meaning.

## Ownership

Each important token family should have an owner or governance path.

Document:

- source of truth;
- who can change it;
- expected consumers;
- whether runtime configuration can influence it;
- migration/deprecation requirements.

## Validation

Validate:

- stable hierarchy;
- token types;
- no circular aliases;
- no unintended primitive consumption by pages;
- semantic names independent of current values;
- product variants preserve base meaning;
- RTL/LTR logical meaning;
- machine-readable format parses;
- runtime resolution produces valid effective tokens.
