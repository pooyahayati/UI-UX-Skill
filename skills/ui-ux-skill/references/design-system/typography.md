# Design System Typography

Use when defining or auditing product typography.

Typography is a semantic system, not a collection of font sizes.

## Typography roles

Define explicit roles appropriate to the product.

A practical role set may include:

- display
- heading
- title
- body
- label
- caption
- code / mono
- data / numeric

Not every product requires every role.

Do not create one token per page heading.

## Role contract

Each role should define or inherit:

- font family
- font size
- font weight
- line height
- letter spacing where applicable
- text transform only when semantically justified
- script compatibility
- responsive behavior
- density behavior where applicable

Typography roles should resolve consistently across themes.

## Scale

Use a deliberate type scale.

The scale may be:

- modular;
- custom;
- platform-native;
- inherited from an existing framework.

Do not force a mathematical scale if it damages product hierarchy.

Avoid excessive steps that differ by only trivial amounts.

## Body text

Body typography should optimize sustained reading or task scanning according to product context.

Validate:

- line length;
- line height;
- zoom/text scaling;
- localized expansion;
- high-density UI constraints.

Do not shrink body text merely to preserve a screenshot layout.

## Labels and controls

Control labels must remain legible at all supported densities.

Density may change padding or control height, but should not create an inaccessible micro-type system.

## Numeric/data typography

For dense data, consider:

- tabular numerals;
- consistent decimal alignment;
- unit/currency treatment;
- predictable negative-value treatment.

Do not introduce a separate numeric font unless it improves real data work and remains compatible with the product language.

## Code / technical identifiers

Use a monospace role only when technical identity benefits from it.

Examples:

- code;
- token IDs;
- hashes;
- paths;
- version strings.

Do not render ordinary labels in monospace merely for visual novelty.

## Persian and Latin

For bilingual Persian/English products, deliberately choose:

- one family with strong support for both scripts; or
- a compatible Persian + Latin pairing.

Test mixed-script lines.

Validate:

- Persian shaping;
- Latin glyph quality;
- digits;
- punctuation;
- baseline alignment;
- weight equivalence;
- x-height/visual scale;
- line height.

Do not assume matching numeric font sizes produce matching visual size across scripts.

## Font loading

Prefer supplied, licensed, or approved project fonts.

Load only required weights/styles.

Use variable fonts when they materially simplify the system and browser/platform support is appropriate.

Do not ship font files that are not licensed for the product.

## Responsive typography

Responsive typography should preserve hierarchy and reading quality.

Do not scale every role proportionally with viewport width.

Use product-aware changes where necessary.

## Accessibility

Typography must tolerate:

- browser zoom;
- platform text scaling;
- translated string expansion;
- RTL/LTR;
- user contrast/theme preferences.

Do not use weight or color alone to convey essential state.

## Validation

Test representative:

- body copy;
- dense control labels;
- headings;
- tables/data;
- Persian-only;
- English-only;
- mixed-script;
- Light/Dark;
- high contrast/forced colors where applicable;
- large text/zoom;
- compact and comfortable density.
