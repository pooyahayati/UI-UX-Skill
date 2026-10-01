# Design System Governance and Migration

Use when changing token architecture, component contracts, runtime design configuration, or long-lived design-system APIs.

## Lifecycle

Use an explicit lifecycle for durable design-system contracts:

`Proposed -> Active -> Deprecated -> Migration/Alias -> Removed`

Do not delete widely consumed tokens/components without a migration path unless the change is intentionally breaking and approved.

## Deprecation

A deprecated token/component should document:

- replacement;
- reason;
- deprecation version/date;
- affected consumers;
- planned removal condition;
- migration guidance.

Deprecation is not permission to keep dead APIs forever.

## Aliases during migration

Aliases may preserve compatibility for renamed semantics.

Example:

`color.text.muted -> color.text.secondary`

Use aliases only when semantics are truly equivalent.

Do not alias a removed concept to a different meaning simply to avoid migration work.

## Breaking change

A breaking design-system change includes, where consumers depend on it:

- removed token;
- changed token type;
- changed semantic meaning;
- removed component variant;
- incompatible component-state behavior;
- changed runtime configuration schema.

Treat visual-only raw value changes separately when semantic meaning remains stable.

## Token impact analysis

Before changing a high-reuse token, identify:

- direct references;
- alias chain;
- component consumers;
- product surfaces;
- theme contexts;
- product variants;
- runtime owner/user configuration;
- screenshots/visual baselines likely to change.

Do not approve a broad semantic-token change based on one representative component.

## Versioning

Use repository/project versioning appropriate to the product.

At minimum, record changes to:

- token schema;
- runtime configuration schema;
- component API;
- migration logic.

Do not imply semantic-version guarantees if the project does not follow semantic versioning.

## Runtime configuration boundary

Keep persisted configuration separate from design-system source.

Use:

`Persisted Config -> Schema Validation -> Migration -> Policy Resolution -> Preference Reconciliation -> Resolved Runtime Tokens -> Components`

Owner/user configuration may select approved semantic presets or values.

It must not redefine:

- token alias graph;
- component state model;
- breakpoint logic;
- arbitrary CSS/JS;
- permissions/security;
- validation/business rules.

## Rollback

A design-system/runtime migration should define fallback/rollback when practical.

For runtime configuration, old published versions should remain reconstructable when rollback is a supported feature.

## Visual regression compatibility

Token/component changes should identify expected visual impact.

Use visual-regression coverage for:

- semantic color changes;
- typography changes;
- density changes;
- component-state changes;
- theme changes;
- RTL/LTR changes;
- responsive/layout token changes;
- product variants.

A changed screenshot is evidence of difference, not proof of regression.

## Ownership

Document ownership for:

- token source;
- component library;
- theme resolution;
- runtime configuration schema;
- migration code;
- visual baseline approval.

## Validation

Before removal or migration verify:

- no unintended consumers remain;
- alias graph resolves;
- old config migrates;
- invalid config falls back;
- themes still resolve;
- component states remain complete;
- visual changes are expected/approved;
- RTL/LTR and responsive contexts remain valid.
