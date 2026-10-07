# Web Application Navigation and State

Load only after the active product route includes `web-application` and application structure, routing, URL/browser state, drafts, save semantics, or recovery state is in scope.

This module contains existing Web Application Product Pack guidance extracted for progressive disclosure. Load it only when the listed concerns are materially in scope.

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

Read `../../shared/state-recovery.md` and `../../shared/feedback-status.md`.

The Web Application Product Pack additionally owns:

- route-specific unavailable/deleted resource state;
- permission/session effects;
- stale server state;
- syncing/reconnecting;
- conflict;
- background processing tied to application objects.

Preserve enough prior application context during recoverable loading/error transitions to prevent unnecessary disorientation.
