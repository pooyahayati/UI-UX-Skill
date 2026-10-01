# Domain-Aware Dashboard Patterns

Use these patterns as prompts for domain-specific reasoning, not as fixed templates.

Always prefer actual product requirements and user workflows over generic domain assumptions.

## CRM and sales

Common questions:

- what needs follow-up
- which deals/leads are aging
- what changed stage
- who owns the next action
- where pipeline risk is concentrated

Useful concepts:

- stage
- owner
- next action
- lead/deal age
- value
- probability when the product uses it
- activity history
- stale opportunities
- source
- forecast context

Avoid making revenue/pipeline cards the whole experience when users spend most time working records.

## Customer support

Common questions:

- what breaches or approaches SLA
- what is unassigned
- what needs escalation
- what is waiting on customer/team
- where volume or backlog is changing

Useful concepts:

- priority
- SLA
- age
- assignee
- channel
- queue
- escalation
- customer status
- first response/resolution metrics

Make queue work efficient; do not over-prioritize decorative analytics.

## Inventory and ERP operations

Common questions:

- what is low/out of stock
- what is blocked/delayed
- which orders require intervention
- what changed in supply or demand
- where exceptions are concentrated

Useful concepts:

- stock state
- reorder point
- incoming/outgoing
- location
- supplier
- order state
- exception reason
- age
- fulfillment status

Traceability and bulk operations are often critical.

## Finance and billing operations

Common questions:

- what is overdue
- what failed
- what is unreconciled
- what changed vs period/budget
- what needs approval

Useful concepts:

- amount/currency
- due date
- payment/reconciliation state
- account/entity
- exception reason
- approval state
- period
- variance
- audit trail

Be explicit about currency, period, timezone, source, and partial data.

Do not imply accounting correctness from visual presentation alone.

## DevOps, NOC, and observability

Common questions:

- what is currently unhealthy
- what changed recently
- what needs acknowledgement
- what is stale/disconnected
- where impact is concentrated

Useful concepts:

- severity
- service/system
- incident age
- acknowledgement
- owner
- status
- change/deploy correlation
- freshness
- latency/error/resource signals

Real-time stability, alert fatigue, and drill-down are central UX concerns.

## Security operations

Common questions:

- which alerts need triage
- what is confirmed vs suspected
- what is escalating
- what is the evidence/context
- what was already investigated

Useful concepts:

- severity
- confidence
- source
- asset/user
- age
- owner
- status
- evidence
- related events
- false-positive/benign state where applicable

Do not let visual severity styling substitute for underlying security policy.

## Healthcare administration

Common questions:

- what requires operational attention
- what is delayed/incomplete
- what appointments/tasks need action
- what records are missing

Prioritize:

- privacy-aware presentation
- role/permission clarity
- clear status and ownership
- error prevention
- auditability
- accessible forms/tables

Do not make clinical recommendations from dashboard UI heuristics.

## HR and people operations

Common questions:

- what approvals/tasks are pending
- where onboarding/offboarding is incomplete
- which records require action
- what deadlines are approaching

Prioritize:

- privacy
- role-sensitive visibility
- clear workflow status
- explainable metrics
- careful bulk actions

## Executive dashboards

Optimize for:

- exceptions
- change
- trend
- comparison
- risk
- decisions

Do not overload executives with operational controls unless the role actually uses them.

## Domain discovery questions

When domain context is unclear, inspect or ask only what materially changes design:

- primary role
- frequency of use
- highest-risk action
- most important exception
- key entity
- data freshness expectation
- whether traceability/audit is required
- whether work is monitoring, triage, entry, approval, or analysis

## Domain safety

Do not infer legal, clinical, financial, security, or compliance rules merely from UI patterns.

When such requirements affect design, use the product's documented rules or clearly state the uncertainty.
