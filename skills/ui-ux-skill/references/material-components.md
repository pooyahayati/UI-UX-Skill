# Material component index — selective workflow overlay

Read only after [Material selection](material-design.md) is evidenced for the
affected scope. Product Pack and relevant Shared Rules decide behavior; existing
[component states](design-system/component-states.md) and approved token sources
remain authoritative. A catalog entry is not a feature request, installed API,
or permission to redesign. For one field repair, read forms only, not all files.

## Shared overlay contract

The family guidance below inherits these constraints for **every authored
component**; component rows add only meaningful differences:

- Use the approved color/foreground pairs, font roles, spacing, density, shape
  and elevation through [foundations](material-foundations.md), not page-local
  values or a second token namespace. An unresolved design conflict is a scoped
  recommendation, not authority to replace approved foundations.
- Preserve labels, meaning, permissions, validation, task state and recovery
  from the active Product Pack/Shared Rules. Appearance never changes the action.
  Relevant default, focus, pressed, selected, disabled, busy and error states
  must remain distinct; omit genuinely irrelevant states.
- Adapt to actual content and existing layout transitions, not native `dp`
  numbers copied as web pixels. Protect touch targets, keyboard behavior,
  zoom/reflow, non-color cues and visible focus under existing accessibility
  rules. Read only the affected responsive/interaction modules.
- Use the product's actual language/direction, real approved font assets/weights,
  logical placement and isolated identifiers. Mirror directional meaning only,
  not logos, checkmarks, media playback or time/data semantics by blanket rule.
- Primary proposal/corrections/approval precede derived dark review, then any
  needed owner-authorized secondary language/layout. Both themes use semantic
  surface/text/boundary/state pairs; no automatic inversion or simultaneous gallery.
- Icons resolve through the existing semantic mapping and accessible labels.
  Motion indicates cause/state only, follows approved levels and reduced motion,
  and must not delay completion or become the sole cue.
- When admin is in scope, expose only already prepared effective choices through
  [runtime governance](runtime-ui-governance.md). Typical color/font/spacing/
  shape/icon choices are bounded by supported consumers. A guide does not create
  controls, change interaction models, allow arbitrary CSS or promise persistence.
- For implementation, use [stack fit](material-stack-fit.md). Material Web
  availability labels below are a dated documentation observation, not a
  universal provider matrix or a browser/runtime pass. Recheck exact APIs and
  installed revision; previews are not stable exports. Do not infer Expressive
  coverage from baseline components.

## Navigable official catalog

Catalog links observed in the live official browser on **2026-10-06**. This is
an index, not a copied specification or a frozen future inventory. Each linked
family is local product-adaptation guidance; **source-only** entries deliberately
have no bespoke local manual. Follow the official page only when actually needed,
including its current guidelines/accessibility/API evidence. Recheck changed names
or variants rather than assuming all old or new variants exist in a provider.

| Workflow / local guide | Official entries |
| --- | --- |
| [Actions](material-components/actions.md) | [Buttons](https://m3.material.io/components/buttons/overview), [icon buttons](https://m3.material.io/components/icon-buttons/overview), [FAB](https://m3.material.io/components/floating-action-button/overview), [extended FAB](https://m3.material.io/components/extended-fab/overview) |
| Action extensions — source-only | [Button groups](https://m3.material.io/components/button-groups/overview), [FAB menu](https://m3.material.io/components/fab-menu/overview), [split buttons](https://m3.material.io/components/split-button) |
| [Navigation](material-components/navigation.md) | [App bars](https://m3.material.io/components/app-bars/overview), [navigation bar](https://m3.material.io/components/navigation-bar/overview), [rail](https://m3.material.io/components/navigation-rail/overview), [drawer](https://m3.material.io/components/navigation-drawer/overview), [tabs](https://m3.material.io/components/tabs/overview) |
| Navigation extensions — source-only | [Search](https://m3.material.io/components/search/overview), [toolbars](https://m3.material.io/components/toolbars/overview) |
| [Forms / selection](material-components/forms.md) | [Text fields](https://m3.material.io/components/text-fields/overview), [checkbox](https://m3.material.io/components/checkbox/overview), [radio](https://m3.material.io/components/radio-button/overview), [switch](https://m3.material.io/components/switch/overview), [chips](https://m3.material.io/components/chips/overview), [sliders](https://m3.material.io/components/sliders/overview), [segmented buttons](https://m3.material.io/components/segmented-buttons/overview), [date](https://m3.material.io/components/date-pickers/overview) / [time pickers](https://m3.material.io/components/time-pickers/overview) |
| [Feedback](material-components/feedback.md) | [Progress indicators](https://m3.material.io/components/progress-indicators/overview), [snackbar](https://m3.material.io/components/snackbar/overview), [badges](https://m3.material.io/components/badges/overview) |
| Feedback extension — source-only | [Loading indicator](https://m3.material.io/components/loading-indicator/overview) |
| [Overlays](material-components/overlays.md) | [Dialogs](https://m3.material.io/components/dialogs/overview), [menus](https://m3.material.io/components/menus/overview), [bottom](https://m3.material.io/components/bottom-sheets/overview) / [side sheets](https://m3.material.io/components/side-sheets/overview), [tooltips](https://m3.material.io/components/tooltips/overview) |
| [Content](material-components/content.md) | [Cards](https://m3.material.io/components/cards/overview), [lists](https://m3.material.io/components/lists/overview), [divider](https://m3.material.io/components/divider/overview) |
| Content extension — source-only | [Carousel](https://m3.material.io/components/carousel/overview) |

Tables, charts, diagrams, command palettes, skeletons, steppers and web select/
combobox primitives are not inferred members of this observed M3 catalog. A
provider may supply them; use product/host semantics, label them custom or
provider-specific, and theme through existing tokens. Do not invent Material
specs for them or read every family because a screen has a chart.

## Handoff / validation

Record only relevant component choices, rationale, source/date, provider/version,
custom exceptions and actual token/config links in existing `DESIGN.md` when
authorized. In narrow/audit work reuse the baseline and report only the delta.
For significant implementation, verify real compact/wider consumers and affected
states using [existing QA](qa-checklist.md). A local guide, source reading or
provider accessibility claim is not rendered/user approval. Samples and connected
appearance implementation are separate R9.4/R9.5 work; full evaluation is R9.6.
