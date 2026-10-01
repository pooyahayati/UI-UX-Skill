# Dashboard Product Pack

Use only when the active product route includes `dashboard`.

This Product Pack specializes the UI/UX Head for operational, analytical, monitoring, CRM, and data-heavy dashboards.

Read the detailed dashboard reference when dashboard components or workflows are in scope:

`../dashboard-patterns.md`

## Primary objective

A dashboard exists to help a user understand state, notice change, make decisions, and act.

Before selecting components, establish:

- what requires attention;
- what changed;
- what is abnormal;
- what decision the user is making;
- what action follows;
- what can safely wait.

Do not begin from a fixed card/chart template.

## Information hierarchy

Prioritize by operational consequence and decision frequency.

Use summary metrics only when they answer a real question.

Avoid equal visual weight for unrelated information.

A dashboard homepage should not become a decorative report when users primarily need a work queue, alert stream, table, or next action.

## Data trust

Where relevant, make clear:

- active time range;
- timezone;
- filter scope;
- last updated / freshness;
- stale, partial, delayed, or disconnected state;
- comparison baseline;
- metric definition;
- drill-down path to underlying records.

## Tables and work queues

Treat operational tables as working surfaces.

Resolve when relevant:

- identifier and key context;
- search scope;
- filter model;
- sorting;
- selection and bulk operations;
- row actions;
- column priority;
- density;
- sticky behavior;
- pagination or virtualization;
- responsive strategy;
- saved/published views.

Do not expose database structure merely because fields exist.

## Charts

Every chart must have a question.

Prefer the simplest representation that answers it.

Preserve analytical meaning in RTL; do not mirror chronological or quantitative semantics blindly.

Provide accessible alternatives when exact values or non-visual access matter.

## Live dashboards

For live or near-real-time products, read `../operational-interaction-patterns.md`.

Protect operator context during incoming updates.

Make connection, stale-data, reconnecting, and synchronization states visible when material.

## Roles and authorization

Role-aware presentation may change emphasis, defaults, shortcuts, or visible summaries.

Presentation must follow authorization and must not create capabilities.

## Responsive behavior

On smaller screens, preserve decision priority rather than shrinking the desktop dashboard.

Choose intentionally between:

- reduced summary;
- prioritized columns;
- expandable rows;
- dedicated record view;
- deferred secondary analytics;
- horizontal comparison when cross-column context is essential.

## Validation

For dashboard work, validate representative:

- overview/landing state;
- work queue or core table;
- filters/search;
- detail/drill-down;
- empty/error/stale states;
- relevant roles;
- responsive widths;
- active themes/directions;
- live-update states when applicable.

Read shared references only when relevant:
- `../personalization-and-data-ux.md`
- `../operational-interaction-patterns.md`
- `../domain-patterns.md`
- `../performance.md`
