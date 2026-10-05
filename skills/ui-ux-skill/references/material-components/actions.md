# Material actions

Apply the [shared overlay contract](../material-components.md#shared-overlay-contract)
to each row. Load only for affected actions; retain Shared destructive-action,
state/recovery and accessibility semantics when relevant. These are local
product recommendations, not new business rules or a verbatim Material manual.

| Component | Purpose / anatomy / suitable presentation | Representative example / implementation observation |
| --- | --- | --- |
| Button | Explicit action: container, visible verb label, optional semantic icon, state layer/focus. Use supported filled/tonal/outlined/text/elevated emphasis to reflect importance. Current official overview also distinguishes default/toggle and configurable size/shape; do not equate those with installed support. | Field work: visible “Save note” paired with a quieter cancel action, not two competing primaries. Material Web baseline button documented; Expressive size/shape/toggle behavior requires separate API proof. |
| Icon button | Compact familiar action: target, icon, accessible name, focus/state. Use supported visual/selection variants only; prefer visible text when meaning is not obvious or consequence matters. | “Open filters” with an accessible name and expanded-state relationship; do not use an unexplained destructive glyph. Baseline icon button documented in Material Web. |
| FAB / extended FAB | Prominent recurring creation action: floating container, semantic icon and, for extended presentation, visible label. Use only when the workflow needs that prominence, not as compulsory screen decoration or a second Save. | “New visit” on an authorized visit list; extended label helpful for unfamiliar users. Material Web FAB documented; verify the selected extended variant's exact API. |

## Per-component behavior and recovery

- **Button:** retain action identity while busy, block duplicate submission using
  actual task state, show truthful outcome and actionable failure without losing
  draft data. A toggle is selection (`aria-pressed` when appropriate), not a
  disguised irreversible operation. Link destinations retain link semantics.
- **Icon button:** communicate on/off or expanded state programmatically, distinct
  from focus. Selection changes the icon's treatment, not its accessible meaning;
  paired icon variants resolve through the semantic map. A tooltip supplements
  rather than supplies the only name or necessary instruction.
- **FAB / extended FAB:** remain reachable without covering data or other actions.
  Disabled/hidden behavior follows actual authorization and workflow context;
  never claim creation succeeded because an animation finished.

## Responsive, language, theme and controls

Buttons wrap or stack at content-driven transitions; retain action order and
full meaningful labels under approved font/zoom boundaries. Icon targets keep
their touch area even when glyphs are visually small. Floating actions account
for navigation, safe areas and on-screen keyboard; do not resize them into tiny
controls to fit. Placement uses logical edges, while action meaning survives RTL.

Use semantic action/foreground pairs for emphasis, with independently visible
focus/disabled/busy states in primary and later dark review. Supported owner
choices may alter prepared emphasis, font roles, size, radius and icon family;
they cannot relabel Save as Complete, toggle authorization, change submission,
or select a not-yet-implemented morph/FAB menu. Reduced motion keeps state cues
without requiring bounce or shape transformation.

Official sources: [buttons](https://m3.material.io/components/buttons/overview),
[icon buttons](https://m3.material.io/components/icon-buttons/overview),
[FAB](https://m3.material.io/components/floating-action-button/overview),
[extended FAB](https://m3.material.io/components/extended-fab/overview).
Button overview read live 2026-10-06; other links observed in the live catalog.
Baseline availability: [provider roadmap](https://github.com/material-components/material-web/blob/main/docs/roadmap.md).
Use [stack fit](../material-stack-fit.md) for provider-specific limitations.
