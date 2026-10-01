# Monitoring / NOC Dashboard Rules

Use this local rule pack when the active product route includes `dashboard` and the dashboard supports real-time or near-real-time monitoring, observability, incident response, operations centers, NOC/SOC-like situational awareness, or wallboard use.

This is an internal Dashboard mode, not a separate Product Type.

## Primary job

A monitoring dashboard should help users answer:

- Is the system healthy?
- What is failing or degrading?
- How severe is it?
- When did it start?
- What scope is affected?
- Is it getting worse?
- What should I investigate or acknowledge next?

Optimize for situational awareness under pressure.

## Monitoring strategy

Do not monitor everything simply because data exists.

Each panel should have a purpose tied to:

- symptom;
- cause;
- capacity;
- dependency;
- service objective;
- incident diagnosis.

Avoid dashboard sprawl.

Related dashboards should have clear ownership, naming, and navigation.

## Attention hierarchy

Severity must be meaningful.

Differentiate:

- normal;
- informational;
- warning;
- critical;
- unknown/no signal;
- stale/disconnected.

Do not use red merely to make a chart visually interesting.

Reserve the strongest attention treatment for conditions that require action.

## Alert vs visualization

A monitoring chart and an alert are not the same product.

Use alerts for conditions that justify interruption.

Use dashboards for:

- situation assessment;
- diagnosis;
- trend/context;
- correlation;
- ongoing observation.

Do not create alert fatigue by turning every threshold line into an interruptive alert.

## Real-time updates

Incoming data must not destroy operator context.

Avoid:

- continuous disruptive resorting;
- shifting rows under the pointer/focus;
- animation on every update;
- replacing selected records unexpectedly.

Consider:

- subtle changed-state indication;
- new-items banner;
- pause/freeze/live control;
- stable ordering during active inspection;
- explicit refresh cadence.

## Refresh cadence

Refresh according to the data and decision requirement.

Do not refresh every few seconds when the underlying data changes hourly.

Excessive refresh can:

- increase backend load;
- make visuals unstable;
- create false urgency;
- waste network/device resources.

## Connection and freshness

Make connection state explicit:

- live;
- delayed;
- reconnecting;
- stale;
- disconnected;
- failed;
- partial source failure.

A dashboard must not look healthy merely because the last successful data is still on screen.

## Time-series monitoring

For time series:

- show clear units;
- preserve scale consistency where comparison matters;
- mark significant incidents/deployments when useful;
- avoid misleading stacked series;
- distinguish gaps from zero;
- make current time/window clear.

When multiple units/ranges are shown, avoid visual relationships that can be misread.

## Thresholds and baselines

Thresholds should come from meaningful operational policy, SLO/SLA, capacity, or validated baseline.

Avoid arbitrary red/yellow/green bands.

When thresholds vary by entity/time, make the rule discoverable.

## Incident context

For incident-oriented views, support:

- start time;
- duration;
- affected service/entity;
- severity;
- current status;
- owner/commander if applicable;
- related alerts/events;
- change/deployment context;
- runbook/help link;
- drill-down.

Do not make the operator hunt across unrelated dashboards for the first diagnostic step.

## Acknowledgement and ownership

If alerts/incidents can be acknowledged:

- distinguish acknowledged from resolved;
- show owner;
- show time;
- preserve audit/history;
- avoid hiding active impact merely because someone acknowledged it.

## Wallboard vs workstation

A wallboard is not the same as an interactive operator dashboard.

For wallboards:

- minimize interaction dependency;
- use large readable labels;
- avoid hover-only details;
- show current time/freshness;
- keep critical status interpretable at distance.

For workstations:

- support drill-down;
- filtering;
- details;
- investigation context;
- keyboard/mouse workflows.

## Accessibility under pressure

Do not rely on color alone.

Use:

- text/status labels;
- icons/shapes;
- clear severity wording;
- readable contrast.

Avoid flashing/pulsing patterns that can harm accessibility or create alarm fatigue.

## Validation checklist

Validate:

- healthy state;
- warning;
- critical;
- unknown/no-data;
- stale/disconnected;
- partial source failure;
- active incident;
- acknowledged vs resolved;
- live-update stability;
- pause/freeze behavior when available;
- wallboard readability when applicable;
- drill-down/runbook path;
- accessible severity meaning;
- RTL/LTR time-series semantics.
