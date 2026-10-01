# UX Evidence and Metrics

Use this reference when evaluating an existing product, validating a redesign, or when analytics/research evidence is available.

Visual preference is weak evidence. Prefer observable product/user evidence where available.

## Evidence chain

For meaningful findings, use:

`Observation -> Evidence -> User Impact -> Hypothesis -> Change -> Validation`

Example:

```text
Observation:
Users repeatedly reopen the filter drawer after navigation.

Evidence:
Session review and support reports show filters are lost between list/detail transitions.

User impact:
Repeated work and slower triage.

Hypothesis:
Persisting the current saved view/filter state will reduce repeated interaction.

Change:
Preserve list state and support a named saved view.

Validation:
Measure repeated filter setup, task time, and support feedback.
```

Do not fabricate analytics or research evidence.

## Evidence sources

Useful sources include:

- direct user request
- observed workflow
- usability test
- support tickets
- product analytics
- search/filter logs
- task completion data
- form validation errors
- abandoned flows
- accessibility testing
- performance traces
- user interviews
- domain expert feedback
- existing product requirements
- rendered UI inspection
- source-code evidence

State whether evidence is observed, measured, user-provided, or inferred.

## Confidence

Confidence should reflect evidence strength.

### High

Examples:
- reproducible defect
- repeated measured failure
- explicit product requirement
- clear accessibility violation
- consistent evidence across multiple sources

### Medium

Examples:
- strong heuristic issue
- plausible workflow problem with partial evidence
- representative sample but incomplete coverage

### Low

Examples:
- aesthetic preference
- speculative future concern
- inference from one ambiguous screen

Do not overstate low-confidence findings.

## UX metrics

Choose metrics that match the workflow.

Possible measures:

- task completion rate
- time on task
- steps/actions per task
- error rate
- correction/retry rate
- form abandonment
- validation-error frequency
- navigation depth
- repeated filter setup
- search success/no-result rate
- bulk-action failure/recovery
- support issue frequency
- stale-data incidents
- saved-view adoption
- preference reset/failure rate

Do not optimize a proxy metric that harms the real task.

## Baseline and delta

When measurable evidence exists:

1. establish baseline
2. define intended outcome
3. make the change
4. compare after
5. account for scope/sample limitations

Prefer relative project evidence over generic industry benchmarks.

## Qualitative validation

Not all UX work needs telemetry.

Useful qualitative validation:

- user can explain page purpose
- primary action is discoverable
- user can recover from error
- status meaning is understandable
- user can trace a metric to records
- keyboard workflow remains usable
- role-specific tasks are not buried

Record the scenario tested.

## Finding format

For significant audit findings, a useful format is:

```text
Finding:
Evidence:
Impact:
Severity:
Confidence:
Scope:
Hypothesis:
Recommended change:
Validation:
```

This is especially useful for High/Critical findings.

## Avoid false precision

Do not invent:

- conversion uplift
- time savings
- accessibility compliance percentage
- productivity percentage
- performance gain

without measurement.

If evidence is unavailable, say what should be measured.

## Research-driven prioritization

Prioritize with a combination of:

- user impact
- frequency
- risk
- business criticality
- accessibility/security impact
- confidence
- implementation cost
- reversibility

Do not use a single numeric score as false objectivity unless the product team already uses a defined prioritization model.
