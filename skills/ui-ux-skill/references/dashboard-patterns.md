# Dashboard UI Patterns

Read `operational-interaction-patterns.md` for search, real-time updates, concurrency, bulk operations, and long-running jobs.

Read `domain-patterns.md` when domain-specific workflow context materially affects the design.

## Dashboard philosophy

A dashboard should answer:

- what needs attention
- what changed
- what is abnormal
- what should happen next
- what can wait

Do not start with cards and charts. Start with user decisions.

## Role-aware home

Different roles may need different emphasis, not necessarily different products.

Consider role-specific:

- landing summary
- primary action
- alerts
- shortcuts
- table defaults
- terminology/context

Presentation must follow authorization. It must never grant capabilities.

## Shell and navigation

Use a stable shell appropriate to destination count, hierarchy, frequency, roles, and viewport.

Avoid:

- duplicate navigation
- excessive nesting
- icon-only critical destinations
- oversized sidebars
- decorative separators

Persian navigation normally originates from the right; English normally from the left.

Preserve spatial consistency. Do not let runtime appearance settings freely reorder critical destinations.

## Page headers

Keep operational headers compact.

Communicate:

- location and context
- purpose
- primary action

Normally one action should be visually dominant.

## Metric cards and summary numbers

A metric card is appropriate when the value itself is a decision-relevant summary.

A useful metric card should usually communicate enough context to answer:

- what the metric is;
- current value;
- relevant unit;
- relevant time period;
- target/baseline/previous value when comparison matters;
- direction/variance when meaningful;
- freshness if the value may be stale.

Do not show percentage change without a meaningful denominator/baseline.

Do not use red/green direction arrows until it is clear whether up/down is actually good or bad.

Avoid a wall of equally prominent metric cards.

## Metrics and Data Trust

Do not default to four KPI cards.

A prominent metric should be important, interpretable, and contextualized with time or comparison where useful.

For important data, expose relevant trust context such as:

- time range
- timezone
- last updated
- freshness/stale state
- source when useful
- comparison baseline
- active filter scope
- partial-data state
- concise metric definition when ambiguity is likely

Read `personalization-and-data-ux.md` for detailed Data Trust UX.

## Number formatting

Format values according to the decision task.

Use:

- consistent unit/currency;
- appropriate precision;
- compact notation only when it remains interpretable;
- localized number/date formatting where appropriate;
- explicit negative values;
- consistent sign conventions.

Avoid false precision.

Do not mix currencies/units in one comparison without clear labeling or normalization.

## Tables

Treat tables as working tools.

Define:

- identifier
- operational columns
- status and numeric fields
- search scope
- filters
- sort
- pagination
- selection and bulk actions
- row actions
- column priority
- density
- sticky behavior
- responsive strategy

Do not expose every database field.

Keep frequent row actions discoverable; move rare actions to overflow.

Show active filters and a clear-filter action.

For repeated operational use, consider:

- remembered visible columns
- remembered column order/width
- user density preference
- saved views
- shared team views
- default owner-published views

Clarify permission for shared views.

For large datasets read `performance.md`.

## Table accessibility

When a dashboard table is semantically tabular data:

- preserve row/column header relationships;
- use meaningful column labels;
- expose sort state;
- keep row identity clear;
- ensure row actions are keyboard reachable;
- do not rely on color-only status;
- keep focus visible during horizontal/virtualized navigation;
- provide accessible context when sticky headers/columns are used.

Do not replace semantic tabular relationships with layout-only div grids unless the implementation reproduces the required semantics and keyboard behavior.

## Forms

Treat forms as workflows.

Use:

- meaningful grouping
- visible labels
- explicit save behavior
- clear validation
- preserved valid values after errors
- unsaved-change protection for meaningful work

Prefer one column for complex or long-label forms.

Use multiple columns only when relationships and available width justify it.

## Filters

Design around user decisions, not database schema.

Make filter scope explicit when one filter affects multiple widgets or pages.

For frequent workflows consider:

- saved filters
- named views
- recent filters
- clear all
- shared views where permission allows

On mobile, adapt to a drawer, bottom sheet, or dedicated view when appropriate.

## Charts

Before adding a chart answer:

`What question does this chart answer?`

Common mappings:

- trend -> line
- category comparison -> bar
- distribution -> histogram
- relationship -> scatter
- goal progress -> progress indicator
- single value -> metric

Avoid decorative or 3D charts and excessive series or colors.

Always clarify:

- unit
- time range and timezone where relevant
- missing or partial data
- comparison baseline
- data freshness when material

For accessibility:

- do not rely on color alone
- provide meaningful labels and summary
- provide a data/table alternative when exact values matter

## Chart scale and baseline

Choose scales to preserve truthful interpretation.

For bars, a zero baseline is generally important for length comparison unless a specialized analytical context justifies otherwise.

For lines, a non-zero axis may be appropriate, but the scale should not exaggerate ordinary variation.

When comparing panels, consistent scales can materially improve interpretation.

Do not truncate axes merely to make change look dramatic.

## Time series

For time-based visuals:

- clarify timezone;
- keep intervals consistent;
- distinguish missing intervals from zero;
- expose comparison periods clearly;
- avoid connecting data across gaps when that implies observation;
- mark "now" or incomplete current buckets when useful.

Preserve chronological meaning in RTL.

For analytical traceability, provide drill-down to underlying records when the product domain benefits from answering:

`Why is this number here?`

Preserve chronological and analytical semantics in RTL rather than blindly mirroring.

## Cross-filtering and linked interactions

When selecting a chart/table item filters or highlights other panels:

- make the selected source visible;
- show the resulting filter/highlight state;
- communicate which panels changed;
- provide a clear reset path;
- preserve keyboard/focus context;
- avoid chaining hidden filters that users cannot reconstruct.

Cross-filtering should accelerate analysis, not create invisible dashboard state.

## Annotations and events

Use annotations when events materially explain a metric or incident.

Examples:

- deployment;
- campaign start;
- pricing change;
- outage;
- policy change;
- release;
- data-source interruption.

Annotations should be concise and inspectable.

Do not annotate every ordinary event.

## Legends, labels, and exact values

Legends and labels should support interpretation.

Prefer direct labeling when it reduces eye travel and clutter.

Avoid:

- truncated legend labels that destroy meaning;
- labels on every point when they obscure the pattern;
- relying on hover as the only way to retrieve critical exact values.

When exact values matter, provide a table/data alternative or accessible detail view.

## Status

Use a limited semantic palette:

- success
- warning
- danger
- info
- neutral

Do not use color alone.

Badges are for status or classification, not every ordinary value.

## Detail and CRM pages

Establish:

- identity
- status
- primary actions
- key properties
- related data
- activity and history
- secondary detail

Do not make every section an equal-weight card.

## Settings

Separate settings by scope:

- personal preferences
- team/shared settings
- owner/system settings

Group by user mental model, not backend modules.

Separate high-impact operations.

Avoid nested tabs inside tabs.

## Personal preferences

For repeated-use products, consider:

- theme
- density
- sidebar state
- landing page
- table page size
- visible columns
- saved views
- date-range default
- reduced motion

Do not turn every token into a user setting.

## Power users

For high-frequency operational work, consider:

- keyboard shortcuts
- command/search palette
- bulk actions
- quick filters
- recent items
- inline editing where safe
- dense mode
- predictable focus behavior

Shortcuts require discoverability and conflict handling.

## Onboarding and help

For complex products, consider:

- contextual empty states
- progressive first-use guidance
- metric definitions
- contextual help for complex/high-risk actions
- dismissible guidance

Avoid permanent tutorial clutter.

## States

Differentiate:

- no data
- no search result
- no filtered result
- permission denied
- not configured
- missing connection
- load error
- partial data
- stale data
- syncing/delayed data

Loading should preserve context.

Errors should explain:

- what happened
- what was affected
- what the user can do
- whether data was preserved

## High-impact actions

Use consequence text, confirmation, undo, or reversible removal based on risk.

Avoid confirmation fatigue.

## Authentication and system pages

Keep auth, 403, 404, 500, maintenance, offline, connection error, permission denied, and session expired inside the same design system.

Do not leave dead ends.

## Mobile

Do not automatically convert tables to cards.

Choose among:

- priority columns
- expandable rows
- summary and detail
- horizontal scroll
- dedicated detail view

Large dialogs may become full-screen views, sheets, or pages.

Keep primary actions discoverable.


## Refresh and performance

Dashboard performance is part of usability.

Review:

- query/data volume;
- number of panels;
- refresh cadence;
- virtualization/pagination;
- interaction latency;
- cross-filter cost;
- heavy chart rendering;
- background polling;
- unnecessary hidden panels.

Do not refresh more frequently than the user decision or source data requires.

For slow panels:

- preserve the rest of the dashboard;
- show local loading/failure;
- avoid blocking unrelated interactions.

## Dashboard-mode boundary

Mode-specific behavior belongs in local packs under `references/products/dashboard/`.

Use this shared file for reusable components and interaction patterns.

Do not copy executive, analytical, operational, monitoring/NOC, CRM/pipeline, or admin-management methodology back into this shared reference.
