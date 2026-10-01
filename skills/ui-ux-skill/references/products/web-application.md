# Web Application Product Pack

Use only when the active product route includes `web-application`.

This Product Pack applies to browser-based products whose primary purpose is doing work inside an application rather than consuming marketing content.

All web-application design rules are maintained locally in this repository. Do not depend on an external design Skill for product UX.

## Shared rule loading

After this Product Pack is active, read `../shared-product-rules.md` and `../../shared-rules.json`.

For broad web-application work normally load:

- `../shared/navigation-wayfinding.md`
- `../shared/feedback-status.md`
- `../shared/state-recovery.md`
- `../shared/accessibility-interaction.md`
- `../shared/responsive-adaptation.md`
- `../shared/content-hierarchy-progressive-disclosure.md`

Load `../shared/forms-data-entry.md`, `../shared/destructive-high-impact-actions.md`, and `../shared/motion.md` when those concerns are materially in scope.

This Product Pack retains browser history/URL state, application-shell, draft/autosave, concurrency, session/auth, custom-workflow, and application-specific interaction semantics.

## Product model

Establish:

- primary user roles;
- core jobs and workflows;
- route/page structure;
- authenticated vs public surfaces;
- primary objects/resources;
- application shell;
- navigation depth;
- persistent vs transient state;
- save/submit behavior;
- background/long-running work;
- failure and recovery paths;
- concurrency or collaborative state when relevant.

Do not design a web application as a collection of unrelated landing pages.

## Application shell and information architecture

Choose navigation based on destination count, hierarchy, frequency, role, and the primary object model.

Preserve stable orientation across routes.

Clarify the relationship between:

- global navigation;
- workspace/project/account scope;
- local section navigation;
- tabs;
- breadcrumbs;
- contextual actions;
- current object/detail context.

Avoid:

- duplicate global navigation;
- deep nested navigation without strong information architecture;
- hiding important destinations behind icon-only controls;
- changing navigation patterns page by page;
- using tabs as a substitute for a broken route hierarchy.

## Browser navigation and URL state

Treat browser history and deep links as part of the product contract.

For meaningful application state, decide whether it belongs in:

- URL/path;
- query parameters;
- browser history entry;
- local/session state;
- server-side user preferences.

Prefer URL-addressable state when users need to:

- refresh without losing context;
- share a view;
- bookmark a view;
- use Back/Forward predictably;
- open a deep link in a new tab.

Examples may include:

- selected object;
- active tab when semantically meaningful;
- search/filter/sort;
- pagination;
- date range;
- workspace/project context.

Do not put sensitive or excessively large state in the URL.

Back/Forward must not produce surprising destructive transitions.

When a route cannot be restored exactly, recover to the closest valid state and explain the difference if material.

## Routed workflows

For multi-step tasks, make current position, next action, validation, and recovery understandable.

Preserve deep links and browser navigation semantics unless the product deliberately uses another model.

Do not create artificial wizard steps when a single screen with clear structure is easier.

For interrupted workflows, define:

- what is preserved;
- what is lost;
- whether the user can resume;
- how stale input is handled.

## Drafts, autosave, and unsaved changes

For meaningful editable work, explicitly choose one model:

- explicit save;
- autosave;
- local draft;
- server draft;
- staged changes;
- immediate update.

Do not mix models without clear feedback.

When unsaved work can be lost:

- warn on destructive navigation when appropriate;
- preserve valid entered data where possible;
- make save/saved/saving/failed state understandable;
- avoid false "saved" feedback before authoritative confirmation;
- define recovery after refresh/session interruption when feasible.

Autosave must communicate failure and conflict states.

## State model

Read `../shared/state-recovery.md` and `../shared/feedback-status.md`.

The Web Application Product Pack additionally owns:

- route-specific unavailable/deleted resource state;
- permission/session effects;
- stale server state;
- syncing/reconnecting;
- conflict;
- background processing tied to application objects.

Preserve enough prior application context during recoverable loading/error transitions to prevent unnecessary disorientation.

## Long-running and background work

For imports, exports, generation, uploads, reports, indexing, processing, or other jobs:

Design explicit states for:

- queued;
- running;
- progress when measurable;
- completed;
- partially completed;
- failed;
- cancelled;
- retrying.

Where relevant:

- prevent duplicate submission;
- allow the user to continue other work;
- preserve access to job status after navigation;
- make completion discoverable;
- provide retry/resume/cancel only when supported by the system;
- distinguish optimistic acknowledgement from confirmed completion.

Never present a job as complete before authoritative state confirms it.

## Concurrency, stale data, and conflicting edits

For collaborative, multi-tab, or frequently updated products, define behavior when another actor changes the same resource.

Consider:

- stale record warning;
- version conflict;
- refresh/reload;
- merge/reapply;
- discard local changes;
- read-only takeover;
- optimistic update rollback;
- presence/locking only when the product truly supports it.

Do not silently overwrite meaningful user work.

Do not invent collaboration semantics that the backend does not implement.

## Forms and data entry

Read `../shared/forms-data-entry.md`.

Web-application specialization must additionally define:

- explicit save vs autosave vs staged changes;
- async/server validation;
- remote uniqueness/existence checks;
- draft persistence;
- cross-field/business validation;
- application permission effects;
- form state across route changes.

Do not use a generic form contract to erase application-specific save/concurrency semantics.

## Search, filtering, sorting, and saved state

For repeated information-finding tasks, define:

- what scope search covers;
- whether search is instant or submitted;
- filter semantics;
- active filter visibility;
- clear/reset behavior;
- sorting precedence;
- no-result state;
- persistence across navigation/refresh;
- shareable URL behavior when useful;
- saved views/preferences when repeated work justifies them.

Avoid hidden active filters that make data appear missing.

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

## Destructive and reversible actions

Read `../shared/destructive-high-impact-actions.md`.

Web-application specialization should distinguish object deletion from:

- removing a relationship;
- revoking access;
- cancelling a job;
- archiving;
- disabling;
- changing shared state.

Use the actual domain consequence and authorization model.

Do not invent Undo, approval, or recovery semantics that the backend cannot support.

## File upload, import, export, and download

When relevant, design:

- accepted formats/limits;
- upload progress;
- cancel/retry;
- partial failure;
- validation errors;
- duplicate/conflict handling;
- background continuation;
- final output/download availability.

Drag-and-drop must not be the only input path.

## Feedback and notifications

Read `../shared/feedback-status.md`.

Web-application specialization:

- use inline feedback for field/task-local issues;
- persistent application notices for unresolved product state;
- transient feedback for low-risk acknowledgement;
- durable job/history surfaces when results may arrive after navigation.

Do not let a toast become the only record of a critical application failure.

## Responsive web behavior

Read `../shared/responsive-adaptation.md` and `../shared/navigation-wayfinding.md`.

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

Read `../shared/motion.md`.

For repeated-use web applications, keep motion subordinate to task speed, focus continuity, and state clarity.

Avoid motion that delays frequent commands or creates false progress.

## Accessibility interaction contracts

Read `../shared/accessibility-interaction.md` for the design contract and `../accessibility.md` for QA/evidence.

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
