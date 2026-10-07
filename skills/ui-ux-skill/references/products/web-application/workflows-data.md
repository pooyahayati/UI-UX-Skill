# Web Application Workflows and Data Operations

Load only after the active product route includes `web-application` and background work, concurrency, forms, search/filter state, destructive actions, or file operations is in scope.

This module contains existing Web Application Product Pack guidance extracted for progressive disclosure. Load it only when the listed concerns are materially in scope.

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

Read `../../shared/forms-data-entry.md`.

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

## Destructive and reversible actions

Read `../../shared/destructive-high-impact-actions.md`.

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
