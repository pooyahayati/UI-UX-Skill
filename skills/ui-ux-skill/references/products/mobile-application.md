# Mobile Application Product Pack

Use only when the active product route includes `mobile-application`.

This Product Pack applies to native and hybrid mobile product interfaces.

## Platform context

Before major design decisions, identify:

- target platform: iOS, Android, both, or a cross-platform framework;
- existing native/component conventions;
- device classes materially supported;
- orientation requirements;
- offline/network assumptions;
- notification, permission, camera, location, file, or other OS integrations in scope.

Respect established platform and application conventions unless there is a deliberate reason to diverge.

## Navigation

Choose navigation based on task frequency, hierarchy, and platform context.

Keep back behavior predictable.

Do not transplant desktop sidebars, hover-dependent interactions, or dense desktop tables into mobile unchanged.

## Touch and reachability

Primary actions and frequent controls should be practical for touch and repeated use.

Avoid tightly packed controls and interactions that depend on hover.

Consider one-handed use when it materially affects the workflow.

## Safe areas and system UI

Account for:

- status/system bars;
- cutouts/notches;
- home indicators;
- keyboards;
- bottom navigation;
- sheets/dialogs;
- device rotation when supported.

Do not place critical controls where system UI or the on-screen keyboard can obscure them.

## Mobile forms

Use appropriate input types and platform capabilities.

Reduce unnecessary typing.

Preserve user input across validation errors and interruptions.

Make keyboard transitions and submit behavior intentional.

## Permissions

Request OS permissions in context, not merely at first launch.

Explain why a permission is needed before or when the user must decide.

The UI may communicate permission state but must not misrepresent actual OS/security capability.

## Connectivity and lifecycle

When relevant, design for:

- offline state;
- weak/interrupted connectivity;
- retry/recovery;
- background/foreground transitions;
- stale local data;
- synchronization conflicts;
- long-running uploads/downloads.

## Notifications and interruption

Use notifications and badges to support meaningful return paths.

Do not use interruption patterns merely to increase engagement.

## Dense data

For complex data, prioritize task and hierarchy.

Prefer dedicated detail screens, summaries, progressive disclosure, or purpose-built comparison patterns over shrinking a desktop grid.

## Accessibility

Validate touch, text scaling, screen-reader semantics, focus order, reduced motion, contrast, and platform accessibility behavior where applicable.

## Validation

For mobile application work, validate representative:

- primary navigation;
- core workflow;
- keyboard/input flow;
- permission state when relevant;
- offline/error/retry state when relevant;
- small and large supported devices;
- orientation if supported;
- system theme modes;
- RTL/LTR where supported;
- lifecycle/resume behavior where relevant.
