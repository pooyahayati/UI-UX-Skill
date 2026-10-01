# Dashboard Product Pack

Use only when the active product route includes `dashboard`.

This Product Pack owns shared dashboard UX and routes the current dashboard to one or more local Dashboard modes.

Dashboard design knowledge is maintained locally in this repository. Do not depend on an external design Skill for dashboard design.

Read the shared detailed component/pattern reference when dashboard components or workflows are in scope:

`../dashboard-patterns.md`

## Shared rule loading

After the Dashboard Product Pack is active, read `../shared-product-rules.md` and `../../shared-rules.json`.

For broad dashboard work normally load:

- `../shared/navigation-wayfinding.md`
- `../shared/feedback-status.md`
- `../shared/state-recovery.md`
- `../shared/accessibility-interaction.md`
- `../shared/responsive-adaptation.md`
- `../shared/content-hierarchy-progressive-disclosure.md`

Load `../shared/forms-data-entry.md`, `../shared/destructive-high-impact-actions.md`, and `../shared/motion.md` when materially in scope.

Dashboard specialization retains Data Trust UX, metrics, targets/baselines, filters, drill-down, tables/work queues, charts, cross-filtering, alerts, live-update behavior, personalization, role-aware presentation, and mode-specific decision semantics.

## Required Dashboard mode routing

Before broad dashboard design decisions, identify the primary Dashboard mode.

### Executive

Load:

`dashboard/executive.md`

Use when the primary job is strategic oversight, target/variance review, portfolio comparison, risk/opportunity review, or executive decision support.

### Analytical

Load:

`dashboard/analytical.md`

Use when the primary job is exploration, comparison, segmentation, diagnosis, drill-down, hypothesis testing, or understanding patterns.

### Operational

Load:

`dashboard/operational.md`

Use when users repeatedly prioritize queues, process records, manage SLA/time-sensitive work, perform bulk actions, or run daily operations.

### Monitoring / NOC

Load:

`dashboard/monitoring-noc.md`

Use for real-time/near-real-time monitoring, observability, NOC/SOC-like situational awareness, incident response, wallboards, or system/service health.

### CRM / Pipeline

Load:

`dashboard/crm-pipeline.md`

Use for leads, deals, opportunities, account/customer lifecycle, pipeline stages, forecasting, ownership, and next-action work.

### Admin / Management

Load:

`dashboard/admin-management.md`

Use when the dashboard primarily manages users, organizations, permissions, policies, configuration, governance, or administrative operations.

A dashboard can combine modes.

Examples:

- executive overview with a drill-down analytical page -> primary `executive`, secondary `analytical`;
- support operations dashboard with live incident health -> primary `operational`, secondary `monitoring-noc`;
- sales manager dashboard -> primary `crm-pipeline`, secondary `executive`;
- system admin dashboard with live health -> primary `admin-management`, secondary `monitoring-noc`.

Always identify one primary Dashboard mode for the current deliverable.

Do not load every mode by default.

## Dashboard decision brief

Before broad visual design, establish:

- primary Dashboard mode;
- secondary modes, if any;
- primary users/roles;
- primary decision or job;
- decision cadence;
- critical metrics/entities;
- attention/exception model;
- default time horizon;
- filter scope;
- data freshness expectations;
- source/provenance needs;
- primary actions;
- drill-down path;
- live-update behavior if applicable;
- personalization/saved-view needs;
- responsive priorities;
- representative states for validation.

Do not begin from a fixed collection of KPI cards and charts.

## Primary objective

A dashboard exists to reduce the time and uncertainty required to understand state, detect meaningful change, make a decision, and act.

Before selecting components, answer:

- What requires attention?
- What changed?
- What is abnormal?
- What decision is being made?
- What action follows?
- What can safely wait?
- How trustworthy/current is the data?

Different Dashboard modes answer these questions differently.

## Decision hierarchy

Read `../shared/content-hierarchy-progressive-disclosure.md`.

Dashboard specialization prioritizes content by decision consequence, frequency, and required attention.

A prominent dashboard element may be an exception, work queue, alert, trend, target variance, pipeline, critical table, or single metric.

Do not default to equally weighted KPI cards simply because dashboard space exists.

## Audience and use context

Consider:

- who uses the dashboard;
- how often;
- for how long;
- on what screen;
- under what time pressure;
- with what level of domain expertise;
- whether interaction is expected;
- whether the dashboard is used in meetings/wallboards/exports.

A monthly executive review and an all-day operator workstation should not share the same density and interaction model merely because they use the same data.

## Data Trust UX

A dashboard must communicate enough context to interpret its data correctly.

Where relevant expose:

- active time range;
- timezone;
- last updated;
- source;
- refresh cadence;
- live/stale/delayed/partial state;
- comparison baseline;
- active filter scope;
- metric definition;
- unit/currency;
- missing-data meaning;
- forecast/model status;
- drill-down path.

Do not present stale, partial, modeled, forecast, or sampled data as current observed truth.

Read `../personalization-and-data-ux.md` for deeper Data Trust UX.

## Metric contracts

Important metrics should have a stable contract.

For each important metric, know:

- business definition;
- numerator/denominator when relevant;
- aggregation rule;
- inclusion/exclusion;
- unit/currency;
- time window;
- timezone;
- source;
- update cadence;
- target/baseline;
- owner.

Do not let the same metric label mean different things across pages without explicit context.

## Targets, baselines, and variance

When a metric is evaluated against something, show the relevant basis:

- target;
- prior period;
- forecast;
- benchmark;
- budget;
- threshold;
- control range.

Avoid red/green variance without explaining what "good" means.

Do not assume higher is always better.

## Filters and analytical context

For global filters:

- make active state visible;
- communicate scope;
- identify widgets that are excluded;
- support clear/reset;
- preserve/share state intentionally;
- avoid hidden inherited filters.

For repeated-use workflows, consider:

- saved views;
- owner/team-published views;
- recent views;
- URL/shareable state where useful.

A user should be able to answer:

`What exact slice of data am I looking at?`

## Drill-down and traceability

For important summaries, provide a path toward explanation when the domain supports it.

A typical path may be:

`overview -> segment -> entity/record -> source/activity/context`

Preserve the user's filter/time context during drill-down.

Do not use drill-down merely to hide information that belongs in the primary view.

## Tables and work queues

Treat tables as working surfaces.

Resolve:

- row identity;
- operational columns;
- status;
- numeric/metric fields;
- search scope;
- filters;
- sorting;
- grouping;
- selection;
- bulk operations;
- row actions;
- column priority;
- density;
- sticky behavior;
- pagination/virtualization;
- responsive strategy;
- saved/published views.

Do not expose database schema just because fields exist.

For semantic/accessibility behavior, preserve real row/column relationships and headers when the table is a data table.

## Charts and visualizations

Every chart must answer a question.

Prefer the simplest visual that supports the comparison.

Use visual encoding deliberately:

- position/length for precise comparison;
- color for limited semantic/category meaning;
- shape/marker/text when color alone is insufficient;
- area/size only when users can interpret it reliably.

Avoid:

- 3D charts;
- decorative gauges;
- unnecessary series;
- rainbow palettes;
- misleading truncation/scales;
- stacking that hides important values;
- dual axes that imply unsupported relationships.

When exact values matter, provide a table/data alternative or accessible equivalent.

## Cross-filtering and linked views

When selecting one visual changes others:

- show selection clearly;
- distinguish highlight from filter;
- communicate scope;
- provide reset;
- preserve sufficient context.

Do not create invisible cross-filter behavior.

## Alerts and attention

An alert should earn interruption.

Define:

- severity;
- trigger/baseline;
- affected scope;
- owner;
- required action;
- acknowledgement semantics;
- resolved semantics.

Do not use alarm colors for ordinary variation.

Read `../operational-interaction-patterns.md` for real-time, concurrency, alert, bulk-action, and long-running patterns.

## Live and near-real-time dashboards

For live products:

- preserve operator focus/selection;
- avoid disruptive resorting;
- expose connection/freshness;
- distinguish new vs changed data where useful;
- consider pause/freeze/live controls;
- choose refresh cadence according to the source and decision.

Do not refresh more frequently than the decision/data requires.

Do not show a "live" indicator when the current data is stale or disconnected.

## Personalization

Personalization should reduce repeated work without making shared dashboards unpredictable.

Possible preferences:

- visible columns;
- column width/order;
- density;
- saved filter/sort/view;
- default date range;
- landing dashboard;
- optional widgets;
- theme/reduced motion.

Separate:

- personal views;
- shared/team views;
- owner/admin-published defaults.

Read `../personalization-and-data-ux.md`.

## Role-aware presentation

Different roles may need different:

- default dashboard;
- visible summaries;
- alerts;
- shortcuts;
- default filters;
- table columns;
- actions.

Presentation must follow authorization.

Do not expose a privileged action because a dashboard layout says the user should see it.

## Empty, partial, stale, and failure states

Read `../shared/state-recovery.md` and `../shared/feedback-status.md`.

Dashboard specialization must distinguish data semantics such as:

- genuine zero;
- no records;
- filtered/no-result;
- not configured;
- permission denied;
- partial source failure;
- stale/delayed data;
- source unavailable;
- syncing.

For every degraded state, communicate what remains trustworthy and current.

## Loading and refresh

Read `../shared/state-recovery.md`.

Dashboard specialization should preserve stable context during local panel refresh.

Do not replace an entire dashboard with skeletons when only one panel is refreshing or failed.

Refresh cadence remains a Dashboard/data-source decision, not a generic loading rule.

## Responsive dashboard architecture

Read `../shared/responsive-adaptation.md`.

Dashboard specialization preserves decision priority across widths using, as appropriate:

- prioritized columns;
- expandable rows;
- summary + detail;
- filter drawer/sheet;
- deferred secondary analysis;
- split-to-single-pane transition;
- horizontal comparison where semantically necessary.

Do not convert every data table to cards or preserve an arbitrary desktop tile grid.

## Accessibility

Read `../shared/accessibility-interaction.md` for the cross-product interaction floor and `../accessibility.md` for QA/evidence.

Dashboard specialization additionally requires:

- semantic data-table relationships;
- non-color status/trend meaning;
- accessible current-data summaries/alternatives for charts;
- exact-value alternatives when needed;
- restrained live announcements;
- keyboard access through filters, tables, and linked views.

Static alt text must not make claims that become false as dashboard data changes.

## RTL and mixed-direction data

Persian dashboard language requires the external `persian-writing` specialist for linguistic validation.

Dashboard design remains local.

For RTL:

- navigation/layout may originate from the right;
- preserve chronological direction and quantitative semantics according to the data/visualization;
- do not blindly mirror charts, timelines, axes, or numeric meaning;
- isolate mixed technical identifiers when needed.

## Dashboard QA matrix

For significant dashboard work, validate representative:

### Shared

- primary decision/job;
- active Dashboard mode(s);
- default time range/timezone;
- filter scope;
- data freshness;
- metric definitions;
- drill-down;
- empty/no-result;
- stale/partial/failure;
- responsive layout;
- keyboard/focus;
- RTL/LTR when supported.

### Tables

- sorting/filtering;
- selection;
- bulk operations;
- row actions;
- column priority;
- semantic headers;
- narrow-width behavior.

### Charts

- question/visual fit;
- scale/baseline;
- missing data;
- exact-value alternative;
- color-independent meaning;
- cross-filter selection/reset.

### Live data

- connection;
- reconnecting;
- stale/disconnected;
- incoming updates;
- context stability;
- refresh cadence.

### Personalization

- saved/private/shared views;
- permissions;
- persistence/reset;
- schema fallback.

### Mode-specific

Run the validation checklist from every loaded Dashboard mode pack.

Do not claim dashboard-wide validation when the relevant mode/state was not exercised.

## Current canonical references

When details may have changed, prefer current authoritative guidance.

Useful references include:

- Grafana dashboard best practices for purpose, cognitive load, monitoring strategy, refresh cadence, documentation, and dashboard sprawl;
- Microsoft Power BI accessibility guidance for keyboard navigation, focus order, high contrast, labels, and accessible data alternatives;
- W3C/WAI data-table guidance for semantic header/data relationships;
- current WCAG guidance for non-color meaning, focus, contrast, and keyboard access.

These sources refresh implementation/context details; this local Dashboard Product Pack remains the design authority.
