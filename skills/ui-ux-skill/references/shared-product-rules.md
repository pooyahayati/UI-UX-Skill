# Shared Product UI Rules

Use this router only after the primary Product Route and required Product Pack are resolved.

Shared Product UI Rules define stable behavioral contracts that recur across product types. They never replace Product Packs.

## Authority and precedence

`Higher-level Engineering Head -> UI/UX Head invariants -> Active Product Pack -> Shared Product UI Rule -> Design-system defaults -> implementation details`

The Product Pack owns product purpose, platform/host behavior, domain semantics, and exceptions. Shared Rules own reusable cross-product behavior.

A Product Pack may specialize a Shared Rule, but must not weaken accessibility, security, authorization, truthful-state, or user-data-integrity requirements.

## Load strategy

Read `../shared-rules.json` and load only modules materially required by the current task.

Do not load the full shared set by default.

Typical mapping:

- navigation structure or wayfinding -> `shared/navigation-wayfinding.md`
- forms, validation, save/submit -> `shared/forms-data-entry.md`
- notices, feedback, progress, status -> `shared/feedback-status.md`
- loading, empty, error, stale, retry, resume -> `shared/state-recovery.md`
- delete/reset/revoke/bulk high-impact work -> `shared/destructive-high-impact-actions.md`
- keyboard/focus/screen-reader/zoom/custom widgets -> `shared/accessibility-interaction.md`
- responsive/reflow/input-mode/resizing -> `shared/responsive-adaptation.md`
- animation/transition/haptics/reduced motion -> `shared/motion.md`
- information priority/grouping/progressive disclosure -> `shared/content-hierarchy-progressive-disclosure.md`

For broad work, select the modules needed by the actual surfaces and interactions. "Broad" is not permission to load every shared module.

## Non-duplication rule

Keep a rule in Shared Rules when it means the same thing across multiple product types.

Keep it in a Product Pack when product/platform/host/domain context materially changes its meaning.

Product Packs should contain only specialization, exceptions, consequences, examples, and product-specific validation—not copied Shared Rule methodology.

## Product specialization examples

- destructive action contract is shared; WordPress distinguishes reset, plugin-data deletion, and uninstall cleanup;
- state/recovery contract is shared; Mobile adds offline/sync/lifecycle behavior;
- navigation contract is shared; Web Applications add browser history and URL-addressable state;
- responsive contract is shared; Dashboards add decision-priority transformations for dense data;
- content hierarchy is shared; Websites add visitor discovery, trust, and conversion priorities.

## Validation

For every Shared Rule loaded, validate representative behavior that actually exercises it.

Report:

- modules loaded;
- modules intentionally not loaded;
- Product Pack specializations applied;
- checks performed;
- checks unavailable.

Do not claim Shared Rule compliance merely because a file was read.
