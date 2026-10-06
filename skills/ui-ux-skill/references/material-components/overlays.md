# Material overlays

Apply the [shared overlay contract](../material-components.md#shared-overlay-contract)
to every row. Reuse established accessibility, state/recovery and destructive
action contracts; these recommendations do not create another modal framework.

| Component | Purpose / anatomy / variants | Representative example / Material Web baseline observation |
| --- | --- | --- |
| Dialog | Focused interruption: container, accessible title, task content and explicit actions. Basic/full-screen presentation serves one task; avoid confirmation for every harmless click. | Confirm a genuinely consequential existing operation, with its actual consequence and cancel route. Baseline dialog documented; exact full-screen variant requires API/viewport proof. |
| Menu | Contextual action/choice: anchor, popup, labeled items and optional groups/icons. Suitable supported selection/submenu variants depend on the task; not a substitute for primary navigation or form labels. | Existing visit actions with unavailable-item explanation. Baseline menu documented. |
| Bottom / side sheet | Secondary task/content: surface, title/content, dismissal/action and optional drag affordance. Modal/persistent choices depend on the workflow, not screen width alone. | Existing visit filters in a secondary surface, preserving active task state. Bottom sheet unbuilt in roadmap; stable side-sheet API not evidenced. |
| Tooltip | Brief supplementary clarification: trigger, concise text and optional rich content only when behavior is supported. Do not hide required labels, errors, instructions or essential actions in it. | Clarify a familiar icon's secondary meaning while its accessible name remains independently present. Listed unbuilt in Material Web roadmap. |

## Component-specific interaction / recovery

Dialogs establish accessible naming, initial focus appropriate to task, modal
containment when modal, keyboard dismissal policy, explicit cancel/close and
focus restoration. Cancellation preserves prior data; accepting still needs the
actual result/failure check. Busy/error states retain recoverable content. No
animation can act as confirmation and no nested stack of dialogs is the default.

Menus anchor predictably, distinguish current/selected/disabled from focus and
honor keyboard traversal/dismissal. Choosing an item does not authorize its action.
Restore focus logically when dismissed; do not implement a menu merely by painting
a generic div over the page. Sheets use containment only when modal and remain
operable without a swipe/drag gesture; unsaved edits follow existing policy.
Tooltips appear for keyboard focus as well as pointer when appropriate, dismiss
without obscuring required content, and meet hover/focus content rules; touch
users still need all necessary information without hover.

## Responsive, language, themes and controls

Fit within the actual viewport and software keyboard; scroll content while title,
essential action and dismissal stay reachable. Inspect portaled/teleported
content, stacking and background scroll; a page's `dir`/theme may not propagate
through every provider overlay. Use logical anchoring and actual label expansion
without reversing action meaning/order automatically. Full-screen treatment is
a supported presentation choice, not automatic permission to navigate elsewhere.

Apply paired surface/text/boundary/focus tokens to both primary and dark overlays.
Scrims separate layers without erasing focus or information. Semantic icons and
reduced motion preserve open/close relationships. Prepared owner controls may
affect effective appearance, never modality, focus containment, data loss policy,
Escape/security rules or trigger semantics. Missing APIs require bounded authorized
work; do not expose an ineffective “sheet variant” setting.

Official sources: [dialog](https://m3.material.io/components/dialogs/overview),
[menus](https://m3.material.io/components/menus/overview),
[bottom](https://m3.material.io/components/bottom-sheets/overview) /
[side sheets](https://m3.material.io/components/side-sheets/overview),
[tooltips](https://m3.material.io/components/tooltips/overview).
Dialog overview read live 2026-10-06; remaining links catalog-observed.
Availability: [provider roadmap](https://github.com/material-components/material-web/blob/main/docs/roadmap.md).
Use [stack fit](../material-stack-fit.md), not a native screenshot, as the web decision route.
