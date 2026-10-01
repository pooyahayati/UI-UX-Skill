# Navigation and Wayfinding

Use when navigation, routing, menus, tabs, hierarchy, or location awareness is materially in scope.

This Shared Rule defines cross-product navigation contracts. Product Packs own product-specific navigation models.

## Orientation

A user should be able to answer:

- Where am I?
- What is the current scope/context?
- What are the main destinations?
- How do I go back or up?
- What happens if I leave this place?

Do not require users to infer location only from page content.

## Destination hierarchy

Separate:

- global destinations;
- local section destinations;
- contextual actions;
- temporary tasks;
- history/back behavior.

Do not represent unrelated hierarchy levels with the same navigation pattern.

Avoid duplicate navigation that exposes the same destination in multiple equally prominent systems without a clear reason.

## Labels

Navigation labels should predict destination or action.

Prefer user/domain language over internal implementation names.

Avoid:

- unexplained abbreviations;
- icon-only critical destinations;
- generic labels when a more specific label is available;
- changing labels for the same destination across contexts.

## Current location and selected state

Make the current destination understandable without relying on color alone.

Selection and focus are different states.

Do not style keyboard focus as if it were current navigation selection.

## Back, close, and up

Back, Close, Cancel, and Up are not interchangeable.

Define them according to the product's navigation model.

A user should not lose meaningful work because an ambiguous control behaved differently than expected.

## Temporary navigation surfaces

For drawers, sheets, popovers, menus, and temporary navigation:

- provide a clear open/close model;
- preserve focus/return context;
- avoid trapping users in hidden layers;
- do not hide the only path to a critical destination in a transient surface without reason.

## Navigation continuity

When navigation changes layout across widths or platforms, preserve the underlying information architecture.

A desktop sidebar can become a drawer or another platform-native structure without changing what destinations mean.

Do not reorder critical destinations merely because the viewport changed.

## Deep location

For products with deep hierarchy, provide enough context to understand parent relationships.

Possible mechanisms include:

- breadcrumbs;
- section navigation;
- parent labels;
- route hierarchy;
- split navigation/content.

Product Packs decide which mechanism is appropriate.

## Navigation and permissions

Navigation visibility follows actual authorization.

Do not expose a destination solely because a role-based layout configuration says it should appear.

Do not use navigation hiding as the security boundary.

## Keyboard and assistive interaction

Navigation must remain usable without a pointer.

For custom composite navigation widgets:

- use established keyboard conventions;
- keep visible focus;
- distinguish focus from selection;
- preserve semantic names/states;
- avoid overriding browser/OS shortcuts without reason.

Prefer native semantic navigation patterns before custom ARIA-heavy behavior.

## Responsive and platform adaptation

Preserve:

- destination identity;
- hierarchy;
- current location;
- return behavior.

Allow presentation to adapt by product/platform.

Do not clone one platform's navigation chrome onto another merely for visual consistency.

## Validation

Verify:

- primary navigation;
- local/contextual navigation;
- current-location state;
- Back/Close/Cancel meaning;
- keyboard path;
- focus visibility;
- narrow/wide adaptation;
- RTL/LTR ordering when supported;
- capability-limited visibility when relevant.
