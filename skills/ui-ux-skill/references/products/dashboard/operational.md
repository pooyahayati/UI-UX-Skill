# Operational Dashboard Rules

Use this local rule pack when the active product route includes `dashboard` and users repeatedly monitor queues, prioritize work, make routine decisions, and take action throughout the day.

This is an internal Dashboard mode, not a separate Product Type.

## Primary job

An operational dashboard should help users answer:

- What needs action now?
- What is due soon?
- What is blocked?
- What changed since I last looked?
- What can I process in batch?
- What should I do next?

Optimize for repeated work, not presentation.

## Work queue first

When the primary job is processing records, the work queue may be the dashboard.

Prioritize:

- identity;
- status;
- owner;
- age/time;
- priority/risk;
- next action;
- SLA/due state;
- critical context.

Do not force a row-processing workflow through KPI cards and charts.

## Prioritization

Make prioritization rules understandable.

Potential factors:

- SLA breach/risk;
- severity;
- due time;
- business value;
- customer impact;
- age;
- dependency;
- manual priority.

Avoid arbitrary visual emphasis that does not reflect actual work priority.

## SLA and time sensitivity

For time-sensitive work, distinguish:

- on time;
- approaching threshold;
- breached;
- paused;
- not applicable.

Clarify whether timers use:

- business hours;
- calendar time;
- timezone;
- paused states.

Do not show a countdown without explaining the rule it represents.

## Throughput and workload

When useful, show operational health such as:

- incoming rate;
- completed rate;
- backlog;
- work in progress;
- aging;
- cycle/response time;
- capacity by team/owner.

Do not optimize a team around a metric that can encourage harmful gaming without context.

## Row and bulk actions

Frequent actions should be discoverable.

For bulk actions:

- show selected count;
- clarify all-visible vs all-filtered;
- preview high-impact scope;
- handle partial success;
- preserve failed items/context;
- define retry behavior.

Do not hide every action in overflow if users perform it constantly.

## State transitions

If records move through states, users should understand:

- current state;
- valid next states;
- required information;
- consequence;
- who/what changed it;
- whether transition is reversible.

Do not present impossible transitions and rely on backend errors as the UX.

## Ownership and handoff

Where work is assigned:

- show owner/team;
- distinguish unassigned;
- support reassignment if authorized;
- surface handoff notes/context where needed;
- avoid hiding ownership behind secondary detail.

For collaborative queues, define how refresh/concurrency affects ownership.

## Saved views and personal defaults

Repeated users benefit from:

- saved filters/views;
- visible columns;
- sort;
- grouping;
- density;
- page size;
- date range;
- default landing queue.

Shared views require permission and ownership semantics.

## Keyboard/power-user behavior

For high-volume workflows, consider:

- keyboard row navigation;
- shortcuts;
- command palette;
- quick filters;
- inline edit when safe;
- batch selection;
- predictable focus after actions.

Do not add shortcuts without discoverability or collision handling.

## Feedback and continuity

After an action:

- keep the user oriented;
- show success/failure at the correct scope;
- avoid unexpected resorting while the user is acting;
- preserve selection/context on recoverable failure;
- explain partial completion.

## Responsive behavior

On narrow widths:

- preserve priority/identity/status/action;
- collapse secondary detail;
- use drill-down for complex records;
- keep bulk scope understandable;
- avoid converting every row to a giant card if a compact list remains clearer.

## Validation checklist

Validate:

- default work queue;
- priority/SLA states;
- aging;
- frequent row action;
- bulk action with partial failure;
- saved view/default behavior;
- ownership/reassignment when present;
- stale/concurrent state when relevant;
- keyboard high-frequency flow;
- narrow viewport;
- RTL/LTR.
