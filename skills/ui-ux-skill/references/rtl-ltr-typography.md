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

Distinguish structured technical values from editable mixed-script free text. Inspect representative identifiers and adjacent punctuation in the actual consumer at relevant widths; verify complete ordering, legibility, keyboard editing and an actual copy/paste round-trip. A soft wrap at a hyphen is not itself a defect if the value remains unambiguous and usable. Inspect an existing saved/read-only presentation separately; if none exists, record that boundary rather than inventing a view.

Preserve the exact input and editing semantics. If a failure is reproduced, choose the smallest presentation/layout correction; do not inject hidden directional controls into stored text, force global nowrap or create horizontal overflow to hide wrapping. Keep ordinary text reflow and essential actions usable. Route Persian language rules through the existing required specialist instead of duplicating them here.

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

Separate the requested font/stack, asset loading/readiness and actual rendered glyph-font identity. Computed CSS or a loaded FontFaceSet alone does not prove which face rendered Persian, Latin, digits or punctuation, nor whether a requested weight was synthesized. Use supported rendered-font inspection when available, naming the environment and method; otherwise retain identity/weight validation as unverified while reporting scoped visual observations separately. A deliberate system stack is not itself a defect or permission to replace/install a font.

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
