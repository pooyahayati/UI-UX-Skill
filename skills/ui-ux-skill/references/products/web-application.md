# Web Application Product Pack

Use only when the active product route includes `web-application`.

This Product Pack applies to browser-based products whose primary purpose is doing work inside an application rather than consuming marketing content.

All web-application design rules are maintained locally in this repository. Do not depend on an external design Skill for product UX.

## Routing contract

After the `web-application` route is active:

1. read `../shared-product-rules.md` and select only Shared UI Rules required by the task;
2. load only the Web Application modules below that match the current scope;
3. load Design System modules only when reusable foundations, themes, tokens, states, or migration are materially involved;
4. do not load Website, Dashboard, Mobile, or WordPress Product Packs unless the deliverable genuinely spans those product surfaces.

The Web Application Product Pack is the only source of Web Application-specific routing. The global product registry must not expose these internal modules.

## Local module routing

- `web-application/navigation-state.md` — application shell and information architecture, browser history, URL/deep-link state, routed workflows, drafts/autosave, save/recovery semantics.
- `web-application/workflows-data.md` — long-running jobs, concurrency/conflicts, forms, search/filter/sort/saved state, destructive/reversible actions, file operations.
- `web-application/interaction-access.md` — overlays, keyboard/focus, custom components, feedback, responsive behavior, auth/session/permissions, onboarding, motion, accessibility, Persian/mixed-language behavior, final validation.

For a narrow task, load the minimum matching module set. For a broad application design or redesign, load all modules that materially affect the requested deliverable.

## Product-specific ownership

This Product Pack and its local modules own browser/application semantics that Shared Rules cannot determine, including:

- browser history, URL-addressable state, refresh and deep-link restoration;
- explicit save, autosave, draft, staged-change, and unsaved-change models;
- background jobs tied to application objects;
- stale/concurrent edits and conflict handling;
- authenticated-session and permission-facing UX;
- application-specific search/filter/saved-view behavior;
- route-aware recovery and workflow continuity.

Do not design a web application as a collection of unrelated landing pages.

## Shared-rule boundary

Cross-product navigation, form, feedback, state/recovery, destructive-action, accessibility, responsive, motion, and content-hierarchy contracts live in Shared Product UI Rules.

Web Application modules specialize those contracts only where browser, route, session, persistence, concurrency, or application workflow semantics require it.

## Specialist boundary

Persian linguistic correctness remains owned by the required `persian-writing` specialist when Persian-facing UI is in scope. Application layout, RTL/LTR architecture, component behavior, and workflow semantics remain owned by this Skill.
