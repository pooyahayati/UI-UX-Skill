# RTL, LTR, Localization, and Typography

Treat Persian RTL and English LTR as first-class modes.

## Persian language specialist

When Persian-facing UI is in scope, `persian-writing` is a REQUIRED specialist.

Canonical source:

`https://github.com/ali2000hos/persian-writing`

Use it for Persian wording, register, orthography, نیم‌فاصله/ZWNJ, Persian ی/ک, punctuation, digit conventions, mixed Persian/English text, and user-facing copy QA.

This reference remains authoritative for UI direction architecture, layout behavior, responsive RTL/LTR behavior, component structure, and typography-system integration. If language guidance and layout guidance overlap, keep ownership separate:

- Persian linguistic correctness -> `persian-writing`
- UI/UX layout and direction architecture -> this Skill

If `persian-writing` is unavailable, do not claim Persian language QA passed. Report:

`Persian language QA: Unverified — required specialist unavailable.`

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
