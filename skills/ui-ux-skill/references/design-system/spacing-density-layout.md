# Design System Spacing, Density, and Layout

Use when defining spacing scales, control sizing, density modes, radius, elevation, or reusable layout foundations.

## Spacing scale

Define a limited, deliberate spacing scale.

Use the scale for repeated relationships such as:

- inline gaps;
- control padding;
- stack spacing;
- section spacing;
- container gutters.

Do not create a token for every historical pixel value.

## Semantic spacing

Where useful, map primitives to semantic roles such as:

- gap.control
- gap.inline
- gap.stack
- space.section
- space.page-gutter

Semantic spacing should describe relationship, not current numeric value.

## Density

Density is a coordinated system, not a single row-height toggle.

A product may support:

- compact
- balanced
- comfortable

A density preset may affect:

- control height;
- control padding;
- table row height;
- list spacing;
- toolbar spacing;
- content gaps.

Density should not silently reduce:

- readable text;
- accessible target size;
- focus visibility;
- essential hit areas.

## Density ownership

Define whether density is:

- fixed by product;
- chosen by owner;
- chosen by user;
- adapted by platform.

Do not expose density controls when the product cannot maintain valid layouts across presets.

## Control sizing

Establish coherent size roles such as:

- small
- medium
- large

Map component variants to those roles.

Avoid ad hoc component heights.

## Layout foundations

Define reusable layout constraints where they improve consistency:

- content max width;
- page gutter;
- pane minimum/maximum width;
- sidebar width;
- modal/dialog widths;
- readable text measure.

Do not turn layout foundations into rigid global dimensions that conflict with product-specific surfaces.

## Radius hierarchy

Use a limited hierarchy.

Example roles:

- radius.control
- radius.surface
- radius.overlay

Do not increase radius on every element to create visual personality.

Radius should remain coherent with component density and product brand.

## Elevation

Use elevation only when hierarchy genuinely represents layering/floating.

Potential roles:

- base
- raised
- overlay
- modal

Prefer borders/surface contrast when sufficient.

Do not use shadow as decoration on every card.

## RTL/LTR

Spacing and layout tokens should prefer logical relationships where direction affects placement.

Do not encode `left-gap` / `right-padding` as global semantics when `inline-start/end` expresses the intent.

## Responsive behavior

Load `responsive-variants.md` and the Shared Responsive rule.

Spacing may adapt by responsive context, but avoid uncontrolled interpolation that creates arbitrary values.

## Validation

Test:

- compact/balanced/comfortable if supported;
- touch/pointer practicality;
- zoom/text scaling;
- dense data;
- long translations;
- RTL/LTR;
- narrow/wide layouts;
- radius/elevation consistency;
- owner/user density precedence if configurable.
