# Shared Product UI Rules

Use this router after the primary Product Route and required Product Pack have been resolved.

Shared Product UI Rules define stable behavioral contracts that recur across multiple product types.

They do **not** replace Product Packs.

## Authority and precedence

Use this order:

`Higher-level Engineering Head -> UI/UX Head invariants -> Active Product Pack -> Shared Product UI Rule -> Design-system defaults -> implementation details`

Interpret precedence carefully:

- the Product Pack owns product-specific purpose, host/platform behavior, domain semantics, and exceptions;
- a Shared Rule owns the cross-product behavioral contract;
- a Product Pack may specialize how the contract is expressed;
- a Product Pack must not weaken accessibility, security, authorization, user-data integrity, or truthful-state requirements;
- a Shared Rule must not override platform-native or host-native behavior without a cross-product reason.

Example:

- Shared rule: destructive actions require consequence clarity and recovery/confirmation proportional to risk.
- WordPress specialization: distinguish reset, delete plugin data, and uninstall cleanup.
- Mobile specialization: respect OS/system confirmation and interruption behavior.
- Dashboard specialization: bulk destructive scope must distinguish selected vs filtered/all.

## Load strategy

Read `../shared-rules.json`.

Do not load every Shared Rule for every narrow task.

### Broad new product or broad redesign

Normally consider:

- navigation and wayfinding;
- feedback/status;
- state/recovery;
- accessibility interaction;
- responsive adaptation;
- content hierarchy/progressive disclosure.

Load forms, destructive actions, or motion when those concerns are materially in scope.

### Narrow change

Load only the matching Shared Rule modules plus the active Product Pack.

Examples:

- fix a validation-heavy form -> `forms-data-entry.md` + product-specific form rules;
- redesign navigation -> `navigation-wayfinding.md` + product navigation rules;
- improve deletion/reset -> `destructive-high-impact-actions.md` + product-specific consequence rules;
- fix loading/error/retry -> `state-recovery.md` + product-specific lifecycle/state rules;
- accessibility review -> `accessibility-interaction.md` plus applicable product/platform rules.

## Non-duplication rule

Product Packs should not restate the full Shared Rule.

Keep in Product Packs only:

- product-specific extension;
- host/platform exception;
- domain-specific consequence;
- product-specific examples;
- additional validation states.

If a sentence can be moved between Website, Web App, Dashboard, Mobile, and WordPress without changing its meaning, it probably belongs in Shared Rules.

If moving the rule would remove essential product meaning, keep it in the Product Pack.

## Shared modules

### Navigation and wayfinding

`shared/navigation-wayfinding.md`

Owns:

- orientation;
- destination hierarchy;
- current location;
- back/return predictability;
- labels;
- navigation-state continuity;
- avoiding duplicate/ambiguous navigation.

Product Packs still own:

- website mega menus/breadcrumb use;
- web-app route/deep-link behavior;
- mobile platform navigation;
- WordPress admin/menu placement;
- dashboard mode navigation.

### Forms and data entry

`shared/forms-data-entry.md`

Owns:

- labels;
- required/optional clarity;
- input semantics;
- validation;
- error recovery;
- preserving valid values;
- redundant-entry avoidance;
- save/submit state.

Product Packs still own:

- lead-generation commitment;
- web-app draft/autosave semantics;
- mobile keyboard/OTP/autofill behavior;
- WordPress Settings API/save model.

### Feedback and status

`shared/feedback-status.md`

Owns:

- choosing inline/transient/persistent feedback;
- status wording;
- progress truthfulness;
- success/failure scope;
- live-region/announcement intent;
- avoiding toast-only critical errors.

Product Packs own their host-specific notice/notification models.

### State and recovery

`shared/state-recovery.md`

Owns:

- loading;
- empty;
- no-result;
- partial;
- error;
- stale;
- disconnected/offline;
- retry;
- resume;
- preserving context;
- long-running state truthfulness.

Product Packs own platform/host lifecycle semantics.

### Destructive and high-impact actions

`shared/destructive-high-impact-actions.md`

Owns:

- consequence classification;
- scope clarity;
- confirmation/undo/recovery;
- partial failure;
- irreversible action safeguards.

Product Packs define domain-specific destructive meaning.

### Accessibility interaction

`shared/accessibility-interaction.md`

Owns the cross-product accessibility floor.

Product Packs/platform packs may strengthen it but must not weaken it.

### Responsive adaptation

`shared/responsive-adaptation.md`

Owns reflow, prioritization, input-mode and resizing principles.

Product Packs define product-specific transformations.

### Motion

`shared/motion.md`

Owns purpose, interruption cost, continuity, reduced-motion behavior, and avoiding decorative overload.

Product/platform packs define native transition/haptic behavior.

### Content hierarchy and progressive disclosure

`shared/content-hierarchy-progressive-disclosure.md`

Owns:

- information priority;
- grouping;
- scanning;
- progressive disclosure;
- label/help-text restraint;
- avoiding card-everything layouts.

Product Packs define what content is important.

## Validation

For every Shared Rule loaded, report whether the representative behavior was actually exercised.

Do not claim "shared-rule compliance" merely because the file was loaded.

When a Product Pack intentionally specializes a Shared Rule, validation should verify both:

1. the shared behavioral contract remains intact;
2. the product-specific specialization works in its real environment.
