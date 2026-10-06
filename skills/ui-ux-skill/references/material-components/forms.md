# Material forms and selection

Apply the [shared overlay contract](../material-components.md#shared-overlay-contract)
to each row. Reuse the affected Product/Shared forms and recovery rules rather
than inventing a Material validation system. Suggested examples are hypothetical,
not additional product features or approved labels.

| Component | Purpose / anatomy / suitable variants | Example / Material Web baseline observation |
| --- | --- | --- |
| Text field | Labeled input: container, label, value, optional prefix/suffix or icon, supporting/error text. Filled/outlined appearance must remain recognizably editable; multiline only for genuine prose. | Visit note uses a multiline field; record ID remains isolated within RTL. Text field documented; verify textarea, input type and form API in actual provider. |
| Checkbox | Independent choices or grouped multiple selection: target, checked/mixed indicator and associated label. Mixed state means partial group selection, not uncertain server truth. | Pick several visit categories. Documented. |
| Radio | One choice from a labeled group: option targets, indicators and labels; explicit group/value identity. | Select one contact method; no silent clearing of the required answer. Documented. |
| Switch | A clearly labeled on/off setting: track, thumb and semantic state. Prefer it for an immediate setting only when product behavior actually supports that; not an accept-terms replacement. | Existing notification setting with pending/failure feedback. Documented. |
| Chips | Compact assist/filter/input/suggestion roles: container, meaningful label, optional selected/removal icon. Choose role before appearance; not every chip is a checkbox. | Selected visit filters, removable by a named action. Chips documented; verify the exact role/export. |
| Slider | Numeric range: track, thumb, label/value, optional steps/range handles. Use only when range adjustment is easier than exact entry; retain an accessible precision path. | Existing display-size preview within prepared limits. Documented; verify chosen range/step support. |
| Segmented buttons | Small related selection set: labeled segments, container and selected state. Distinguish one-choice from multiple-choice behavior; avoid long crowded labels. | Day/week view choice, if already a product feature. Listed unbuilt in roadmap; do not invent an export. |
| Date / time pickers | Valid date/time entry: label/input, calendar or clock/list surface, selection, confirmation/dismissal and errors. Pick a provider/locale-compatible presentation, not a decorative calendar. | Existing scheduled visit field with timezone/calendar contract. Both listed unbuilt in Material Web; native/host pickers may be better. |

## Component-specific states and recovery

Text fields retain input on error/retry and distinct disabled/read-only modes;
associate errors with the field, not placeholders in place of labels. Checkbox
and radio values/state are programmatic and group keyboard behavior is preserved.
Switches distinguish pending from confirmed values and show reversal/retry if
the actual save fails; do not fabricate a saved value. Chips keep selected versus
focused/removable states distinct and announce resulting filter scope where needed.
Sliders convey min/max/current/step through the control and support keyboard
increment/precision without drag-only interaction. Segments preserve group
selection semantics and unavailable-choice explanation. Picker cancel retains
the previous value; invalid/unavailable dates, loading and parse errors stay
actionable, with accessible manual entry when appropriate.

## Responsive, language, theme and controls

Fields and supporting text reflow without losing labels/errors; software keyboard
and zoom must not cover the active field or submission. Long option groups stack;
chips may wrap with predictable reading order. Sliders need adequate usable track
and targets; precision should not depend on pixel-perfect touch. Picker overlays
inherit [overlay](overlays.md) rules only when used.

Actual locale controls numerals, date/calendar/timezone and input formatting;
the chat language does not choose them. Isolate identifiers/phone numbers and
do not blindly reverse numeric ranges or time order in RTL. Both themes preserve
field boundaries, selection, invalid text and focus. Icon changes cannot alter
clear/reveal-password meaning; motion must not imply server confirmation.

Prepared owner controls may affect field/font/spacing/shape/icon appearance and
supported component presentation, never requiredness, valid range, calendar,
selection multiplicity, password security or save semantics. Unprepared picker,
segmented or combobox behavior requires authorized implementation, not a setting.

Official component links: [forms row in index](../material-components.md#navigable-official-catalog).
Text-field overview read live 2026-10-06; other links catalog-observed. Provider
availability: [roadmap](https://github.com/material-components/material-web/blob/main/docs/roadmap.md).
Web select/combobox is a provider-specific primitive, not an inferred M3 catalog
component. Recheck [stack fit](../material-stack-fit.md) for actual APIs/support.
