# Material feedback and progress

Apply the [shared overlay contract](../material-components.md#shared-overlay-contract)
to each row; Shared feedback/status and state/recovery own truthful outcomes.

| Component | Purpose / anatomy / variants | Representative example / Material Web baseline observation |
| --- | --- | --- |
| Progress indicator | Ongoing process: track/active indication, optional determinate value and meaningful process label. Linear/circular choice reflects placement; determinate only with actual measurable progress, otherwise indeterminate. | Saving a note shows busy status without a fabricated percentage. Baseline progress documented; newer wavy/expressive configuration is not inferred support. |
| Snackbar | Nonblocking brief feedback: container, concise message, optional meaningful action. Not the sole location of a critical error, required decision or record of completion. | Confirm the server-acknowledged save; offer undo only if actual reversal exists. Listed unbuilt in Material Web roadmap. |
| Badge | Supplementary count/attention: indicator attached to a labeled destination/item. Dot/count choice does not replace the base label or convey status by color alone. | Unread visit updates, backed by actual data and accessible meaning. Listed unbuilt in Material Web roadmap. |

## States / recovery / accessibility

Progress starts/stops with actual work, distinguishes retry/failure/completion
and preserves relevant old data. Use suitable busy/progress semantics, with
indeterminate values omitted; never announce every animation frame. Stop useless
spinners after failure and provide a real retry/cancel path only when supported.

Snackbar appearance cannot prove persistence. Preserve errors where the task
can be recovered; use appropriate status announcements without stealing focus.
If a timed action is offered, honor accessibility timing/interaction needs and
provide a durable alternative when losing it would matter. Undo failure needs
honest recovery, not a second fabricated success message.

Badges distinguish unavailable/stale data from zero, and counts must not disclose
unauthorized data. Focus stays on the destination, not a decorative badge. Announce
meaningful changes sparingly and avoid reading an unchanged count twice.

## Responsive, language, themes and controls

Keep progress labels readable, snackbars away from keyboard/navigation/primary
actions, and badges from obscuring labels under zoom. Align by logical placement;
format counts with actual locale and isolate mixed-script messages. Both themes
use approved process/status and foreground roles; inverse snackbar roles require
their paired foregrounds rather than copying one light-mode color into dark.

Meaningful icons supplement text; reduced motion retains process/status meaning.
Waves/bounce are optional product-fit choices, not evidence of speed. Prepared
admin controls may alter approved color/font/density/icon and supported motion
appearance, never process truth, percentages, announcements, timeout rules or undo
capability. A loading-indicator catalog link does not add a new library component.

Official sources: [progress](https://m3.material.io/components/progress-indicators/overview),
[snackbar](https://m3.material.io/components/snackbar/overview),
[badges](https://m3.material.io/components/badges/overview).
Progress overview read live 2026-10-06; remaining links catalog-observed.
Availability: [provider roadmap](https://github.com/material-components/material-web/blob/main/docs/roadmap.md).
Recheck exact [implementation fit](../material-stack-fit.md) before dependency use.
