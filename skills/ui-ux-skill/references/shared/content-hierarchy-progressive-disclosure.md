# Content Hierarchy and Progressive Disclosure

Use when information density, page composition, sectioning, visual hierarchy, help text, cards, summaries, or progressive disclosure is materially in scope.

## Start from decisions and questions

Organize content according to what the user needs to understand or do.

Prioritize by:

- consequence;
- frequency;
- sequence;
- dependency;
- uncertainty;
- user intent.

Do not organize only by internal system/module structure.

## Visual hierarchy

Use a limited set of consistent signals:

- position;
- size;
- typography;
- spacing;
- grouping;
- contrast;
- emphasis.

Do not make every section equally prominent.

## Sectioning

A section should represent a meaningful conceptual or task boundary.

Use headings that describe content, not generic labels such as:

- Overview
- Details
- More information

when a more specific heading is available.

## Progressive disclosure

Hide complexity only when:

- the information is secondary;
- the user can predict how to reveal it;
- concealment does not block informed decisions;
- accessibility/keyboard behavior remains sound.

Do not hide critical terms, consequence, pricing, permission, or risk behind "Advanced" or tooltip-only disclosure.

## Summary vs detail

Use summaries to support quick understanding while preserving a path to detail.

A summary should not distort the underlying state.

Examples:

- metric -> definition/drill-down;
- status -> diagnostics;
- record row -> detail;
- setting group -> advanced detail.

## Cards

Use cards when grouping benefits from a distinct container.

Do not turn every section, metric, paragraph, and action into a card.

Excessive card boundaries weaken hierarchy and waste space.

## Labels, badges, and metadata

Use labels/badges when they convey:

- status;
- classification;
- scope;
- ownership;
- meaningful metadata.

Do not badge ordinary values merely for decoration.

## Help text

Help should be placed where uncertainty occurs.

Prefer concise inline guidance for:

- unfamiliar concepts;
- unusual constraints;
- high-risk actions.

Use deeper documentation for detailed explanation.

Do not clutter routine interfaces with permanent tutorial text.

## Tooltips

Tooltips are supplementary.

Do not put:

- critical instructions;
- required legal/consequence information;
- essential metric context;
- form errors;

only in hover/focus tooltips.

## Density

Density should reflect task frequency and expertise.

High-frequency expert tools may justify compact presentation.

Low-frequency/high-risk workflows often benefit from more explanation and spacing.

Do not treat "modern" as synonymous with excessive whitespace.

## Content order and responsive behavior

When layout changes, preserve semantic/task order.

Avoid visual reordering that produces a confusing keyboard/screen-reader sequence.

## Validation

Verify:

- primary purpose visible;
- first/highest-priority content;
- section labels;
- summary/detail relationship;
- hidden/advanced content discoverability;
- card/container necessity;
- help/tooltip placement;
- dense vs spacious mode appropriateness;
- semantic/keyboard order across responsive widths;
- RTL/LTR hierarchy.
