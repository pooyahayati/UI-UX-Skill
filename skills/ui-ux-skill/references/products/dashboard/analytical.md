# Analytical Dashboard Rules

Use this local rule pack when the active product route includes `dashboard` and the primary job is analysis, exploration, comparison, diagnosis, or understanding patterns in data.

This is an internal Dashboard mode, not a separate Product Type.

## Primary job

An analytical dashboard should help the user answer:

- What happened?
- Where did it happen?
- For whom?
- How does it compare?
- What explains the change?
- What hypothesis should I investigate next?

Do not optimize an analytical dashboard only for at-a-glance consumption.

## Exploration model

Support exploration through deliberate combinations of:

- filters;
- date ranges;
- segments;
- breakdowns;
- comparison groups;
- drill-down;
- drill-through;
- cross-filtering;
- saved analytical views.

Make the active analytical context visible.

Do not let users forget which filters or cohort definitions produced the current view.

## Comparison

When comparison is central, define the comparison explicitly.

Potential comparisons:

- current vs prior period;
- actual vs target;
- cohort A vs cohort B;
- segment vs total;
- before vs after;
- region/team/product;
- observed vs benchmark.

Do not compare incompatible populations, time windows, or units without warning.

## Filter scope and state

Global filters should clearly indicate:

- scope;
- active values;
- exceptions;
- inherited context;
- which visuals are affected.

For complex analysis, consider:

- pinned filters;
- named/saved views;
- URL/shareable state;
- reset to known baseline.

Avoid hidden filtering that changes metric meaning.

## Drill-down and traceability

Users should be able to move from aggregate to explanation.

Where the data model allows, support:

`summary -> segment -> record/sample -> source/context`

Preserve analytical context during drill-down.

Do not force the user to reconstruct filters manually after returning.

## Distribution and variation

Do not rely only on averages.

Where variation matters, consider:

- distribution;
- percentile;
- range;
- spread;
- histogram;
- box/quantile view;
- outlier identification.

Averages can hide operationally important variation.

## Relationships and correlation

When showing relationships:

- distinguish correlation from causation;
- reveal sample size/context where relevant;
- avoid dual-axis or scaled visuals that imply relationships not supported by the data;
- support inspection of outliers.

Do not present a visual pattern as proof of causal effect.

## Missing, sparse, and partial data

Analytical dashboards must make missingness visible when it can change interpretation.

Distinguish:

- zero;
- null/missing;
- not applicable;
- not yet reported;
- suppressed;
- filtered out;
- delayed/partial.

Do not silently convert missing data to zero.

## Statistical/derived metrics

For calculated metrics, provide enough context to understand:

- formula or definition;
- inclusion/exclusion;
- aggregation;
- unit;
- denominator;
- time window;
- sampling/model assumptions where material.

Do not use sophisticated metric names as a substitute for explanation.

## Chart choice

Choose the visual based on the analytical question.

Examples:

- time trend -> line/area with care;
- category comparison -> bar;
- rank -> sorted bar/table;
- distribution -> histogram/box/quantile;
- relationship -> scatter;
- composition -> stacked/part-to-whole only when comparisons remain readable;
- exact value lookup -> table.

Avoid chart variety for visual interest.

Avoid 3D charts.

Use stacking only when it helps the intended comparison.

## Cross-highlighting and linked views

When one selection changes multiple visuals:

- make the selected state obvious;
- distinguish filter from highlight;
- provide clear reset;
- preserve enough context to understand what changed.

Do not create invisible cross-filtering.

## Notes, definitions, and provenance

Analytical users often need to know:

- source;
- refresh/freshness;
- metric definition;
- data owner;
- transformation;
- exclusions;
- known quality issue.

Critical interpretation context should not depend on hover only.

## Export and handoff

When analysis commonly continues elsewhere, define appropriate handoff:

- CSV/data export;
- shareable filtered URL;
- saved view;
- report export;
- underlying record access.

Respect permissions and privacy.

Do not export data that the current user is not authorized to access.

## Validation checklist

Validate:

- active filter/context visibility;
- comparison validity;
- drill-down preservation;
- missing/partial states;
- derived metric interpretation;
- chart-question fit;
- exact-value alternative;
- cross-filter reset behavior;
- export/share behavior when present;
- keyboard/screen-reader access to key insights;
- RTL analytical semantics.
