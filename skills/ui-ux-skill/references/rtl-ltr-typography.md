# RTL, LTR, Localization, and Typography

Treat Persian RTL and English LTR as first-class modes.

## Persian language routing

When Persian-facing language work is in scope, route it to the REQUIRED `persian-writing` specialist defined in `specialist-routing.md`.

This reference does not duplicate Persian-language rules. It remains responsible only for UI/UX direction architecture, mixed-direction layout behavior, responsive behavior, and typography-system integration.

Head-level UI/UX constraints take precedence over any overlapping lower-level specialist guidance.

## Direction architecture

Use correct document `lang` and `dir`.

Prefer CSS logical properties over hard-coded left and right rules.

Do not create separate duplicated design systems for RTL and LTR.

## Mixed-direction content

Inside RTL UI, isolate technical LTR values such as:

- email
- URL or domain
- version
- token or ID
- code
- phone numbers where appropriate

Use semantic isolation such as `dir="ltr"`, `bdi`, or `unicode-bidi: isolate` when needed.

## Directional icons

Mirror only icons whose meaning is directional.

Do not mirror neutral symbols simply because the document is RTL.

## Tables, forms, and navigation

Audit independently:

- alignment
- sticky columns
- selection controls
- row actions
- pagination
- breadcrumbs
- drawers
- input adornments
- error and help placement
- mobile behavior

## Charts

Do not blindly mirror analytical axes.

Preserve chronology, magnitude, and domain conventions.

## Localization beyond direction

Review:

- locale-aware number formatting
- currency
- date and time
- timezone
- calendar system when applicable
- digit style when required
- pluralization
- text expansion and contraction
- truncation
- long localized labels
- sorting and search behavior
- string concatenation that breaks translation

Avoid constructing sentences from fragments when localization will make grammar unstable.

## Typography

Read `design-system/typography.md` for the canonical typography-role and design-system contract.

This file owns direction/localization integration and mixed-script behavior.

For user-supplied local fonts inspect:

- family
- weights and styles
- WOFF2 availability
- variable-font support
- Persian and Arabic shaping
- Latin glyph quality
- digits
- punctuation
- UI legibility at small sizes

Prefer local or self-hosted font loading when requested.

Load only needed weights.

Use framework-native loading when practical.

After a font change re-evaluate:

- line height
- type scale
- weight mapping
- button and input height
- table density
- truncation
- vertical rhythm

## Bilingual font strategy

Choose deliberately between:

- one family supporting both scripts
- Persian family plus compatible Latin companion

Test mixed-script lines rather than judging each script separately.

## Accessibility

Visual mirroring must not break DOM reading order.

Keyboard order, focus order, and screen-reader structure should remain logical in both directions.

Test representative mobile RTL separately from desktop RTL.
