# CRM / Pipeline Dashboard Rules

Use this local rule pack when the active product route includes `dashboard` and the dashboard is primarily about leads, deals, opportunities, accounts, sales pipeline, customer lifecycle, or similar stage-based commercial workflows.

This is an internal Dashboard mode, not a separate Product Type.

## Primary job

A CRM/pipeline dashboard should help users answer:

- What should I follow up on?
- Which opportunities are progressing or stuck?
- What is the pipeline value/quality?
- What is likely to close and when?
- Where are we losing momentum?
- Who owns the next action?

Do not optimize only for a visually impressive funnel.

## Stage semantics

Pipeline stages must have clear business meaning.

For each stage, understand:

- entry criteria;
- exit criteria;
- owner;
- expected next action;
- typical time;
- probability/forecast meaning if used.

Do not use arbitrary stage probabilities merely because a CRM convention does.

## Pipeline value

When showing pipeline totals, clarify:

- gross vs weighted;
- currency;
- time horizon;
- included stages;
- owner/team scope;
- open vs closed;
- forecast category.

Do not compare gross pipeline to booked revenue as if they are equivalent.

## Funnel/conversion

If a funnel is used:

- define the population;
- define the time period;
- define whether it is cohort-based or current-state;
- distinguish stage inventory from stage conversion;
- surface drop-off meaning.

A snapshot of current records in each stage is not automatically a conversion funnel.

## Aging and stagnation

For active opportunities, consider:

- time in stage;
- days since last activity;
- overdue next action;
- expected close date drift;
- repeated reschedule;
- missing contact/decision context.

Highlight stagnation based on meaningful business rules.

## Next action

A high-value CRM dashboard should make the next action visible.

Examples:

- call;
- email;
- schedule;
- prepare proposal;
- review legal;
- follow up;
- update close date;
- reassign.

Do not require opening every record merely to discover the next task.

## Ownership

Make ownership clear for:

- lead/deal;
- account;
- next action;
- escalation.

When team views are used, support relevant owner/team filtering.

Do not use dashboard visibility to grant access to records the user cannot open.

## Forecast

Forecasting views should distinguish:

- actual closed;
- committed;
- best case;
- pipeline;
- model estimate;
- manual forecast.

Make uncertainty and category semantics understandable.

Do not present weighted pipeline as guaranteed revenue.

## Activity and recency

Activity volume is not automatically quality.

Useful recency/context may include:

- last meaningful contact;
- next scheduled activity;
- unanswered contact;
- stage change;
- decision milestone.

Avoid vanity activity counts that do not support a decision.

## Data quality

CRM dashboards are sensitive to stale/incomplete data.

Surface material quality issues such as:

- missing owner;
- missing next action;
- overdue close date;
- duplicate record;
- invalid stage;
- stale contact data.

Do not hide poor data quality behind polished aggregate charts.

## Pipeline drill-down

Every material pipeline number should support a path to contributing records when authorized.

Preserve:

- stage;
- owner;
- date range;
- segment;
- forecast context.

## Validation checklist

Validate:

- owner/team scope;
- stage definition;
- gross vs weighted value;
- funnel population/time logic;
- stagnant opportunity state;
- overdue next action;
- forecast categories;
- stale/incomplete CRM data;
- drill-down to records;
- permissions;
- responsive queue/table behavior;
- RTL/LTR.
