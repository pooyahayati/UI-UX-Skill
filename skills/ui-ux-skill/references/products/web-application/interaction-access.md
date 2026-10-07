# Web Application Interaction, Access, and Validation

Load only after the active product route includes `web-application` and overlays, focus/keyboard, custom interaction, feedback, responsive behavior, auth/session, onboarding, motion, accessibility, localization, or final validation is in scope.

This module contains existing Web Application Product Pack guidance extracted for progressive disclosure. Load it only when the listed concerns are materially in scope.

## Dialogs, drawers, popovers, and overlays

Use overlays for contained contextual tasks, not as a replacement for information architecture.

For every significant overlay, define:

- initial focus;
- keyboard focus containment when modal;
- Escape/cancel behavior;
- focus return after close;
- destructive-action safeguards;
- unsaved-change behavior;
- backdrop/dismiss behavior;
- mobile/narrow-width adaptation.

Avoid deeply nested modals.

Do not place a complex multi-screen workflow inside stacked dialogs when a route or dedicated page is clearer.

## Keyboard and focus behavior

For productivity-oriented applications, keyboard UX is part of the interaction model.

Ensure:

- every essential function is keyboard reachable;
- focus is visible;
- focused elements are not hidden behind sticky content;
- focus order follows task order;
- overlays restore focus meaningfully;
- custom controls implement expected keyboard semantics;
- shortcuts do not override common browser/OS shortcuts without strong reason;
- shortcut discovery exists for important power-user actions.

Do not break standard browser expectations without a product reason.

## Custom interactive components

When creating custom:

- comboboxes;
- menus;
- tabs;
- trees;
- grids;
- listboxes;
- dialogs;
- disclosure controls;

prefer established semantic/keyboard patterns.

Do not create visually novel controls whose interaction model is ambiguous.

Use native HTML behavior when it adequately solves the task.

## Feedback and notifications

Read `../../shared/feedback-status.md`.

Web-application specialization:

- use inline feedback for field/task-local issues;
- persistent application notices for unresolved product state;
- transient feedback for low-risk acknowledgement;
- durable job/history surfaces when results may arrive after navigation.

Do not let a toast become the only record of a critical application failure.

## Responsive web behavior

Read `../../shared/responsive-adaptation.md` and `../../shared/navigation-wayfinding.md`.

Web-application specialization must decide how:

- app shell/navigation transforms;
- multi-pane workflows collapse;
- data grids preserve working context;
- filters/actions move into temporary surfaces;
- pointer/keyboard productivity remains viable on narrow windows.

Do not emulate a native mobile app merely because the browser viewport is narrow.

## Authentication, session, and permission-facing UX

Keep authentication, account, billing, and security-sensitive screens visually coherent with the product while preserving engineering/security boundaries.

Design understandable states for:

- session expired;
- re-authentication required;
- permission changed while the page is open;
- account disabled/restricted;
- resource access revoked;
- logged out from another context when the system exposes it.

Preserve the user's intended destination after successful re-authentication when safe.

The UI/UX Head may improve presentation but must not redefine authentication or permission semantics.

## First-run, onboarding, and empty-to-useful transition

When a product begins empty or unconfigured:

- identify the first meaningful outcome;
- distinguish required setup from optional education;
- provide a clear next action;
- avoid blocking experienced users with unnecessary tours;
- allow resume when setup spans multiple steps;
- make empty states actionable without turning every empty screen into marketing copy.

## Motion and transition feedback

Read `../../shared/motion.md`.

For repeated-use web applications, keep motion subordinate to task speed, focus continuity, and state clarity.

Avoid motion that delays frequent commands or creates false progress.

## Accessibility interaction contracts

Read `../../shared/accessibility-interaction.md` for the design contract and `../../accessibility.md` for QA/evidence.

Web-application specialization must additionally validate:

- routed page/app-shell focus behavior;
- custom widgets used by productivity workflows;
- overlays/drawers/dialog focus return;
- keyboard power-user paths;
- sticky application chrome;
- dynamic status/error announcements.

Do not claim WCAG compliance without sufficient evidence and defined scope.

## Persian and mixed-language web applications

When Persian-facing language is in scope, the REQUIRED external `persian-writing` specialist owns Persian linguistic validation.

The Web Application Product Pack retains ownership of interaction architecture, responsive behavior, browser semantics, direction architecture, components, and accessibility.

## Validation

For web applications, validate representative:

- application shell/navigation;
- primary workflow;
- secondary route;
- URL/deep-link/refresh behavior;
- Back/Forward behavior;
- form/data-entry flow;
- unsaved/draft behavior when relevant;
- long-running/background work when relevant;
- stale/conflict state when relevant;
- search/filter/sort state when relevant;
- dialog/overlay focus behavior;
- permission/session-expiry/error state;
- responsive widths and zoom;
- keyboard-only use;
- active theme/direction;
- browser-rendered output;
- accessibility interaction contracts.

Do not claim product-aware validation for a state or workflow that was not actually exercised.

## Current web-platform references

When verification is needed, prefer current platform and accessibility standards rather than copying framework-specific implementation recipes.

Relevant canonical guidance includes:

- MDN History API / Navigation API for browser navigation semantics;
- W3C WCAG 2.2 and WAI guidance for keyboard/focus/accessibility;
- native HTML semantics before custom widgets.

This local Product Pack remains the design authority; current platform guidance should refresh details when browser standards materially change.
