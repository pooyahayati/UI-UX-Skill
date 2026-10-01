# Admin / Management Dashboard Rules

Use this local rule pack when the active product route includes `dashboard` and the dashboard primarily manages users, organizations, permissions, configuration, governance, system entities, policies, or administrative operations.

This is an internal Dashboard mode, not a separate Product Type.

## Primary job

An admin/management dashboard should help authorized users answer:

- What requires administrative attention?
- Which entities/users are affected?
- What changed?
- What can I safely modify?
- What is the scope and consequence?
- How can I verify or reverse the change?

Do not make an admin dashboard look like a generic KPI report when its real job is governance and control.

## Scope and authority

Every administrative action should make scope understandable.

Potential scopes:

- current user;
- one user;
- team;
- organization;
- tenant;
- environment;
- selected records;
- all records.

Do not rely on page location alone to communicate scope.

## Permission-aware presentation

Presentation follows authorization.

Distinguish:

- can view;
- can edit;
- can assign;
- can approve;
- can configure;
- can delete;
- can manage permissions;
- can perform bulk/global actions.

Do not expose a disabled dangerous control without explaining why it is unavailable when the user legitimately needs that context.

UI restrictions are not security boundaries.

## User/entity lifecycle

For managed entities, make lifecycle state explicit.

Examples:

- invited;
- active;
- suspended;
- locked;
- pending;
- archived;
- deleted;
- deprovisioning.

Do not collapse materially different lifecycle states into "inactive."

## Governance and policy

For policy/configuration changes:

- show current/effective value;
- source/inheritance;
- impact scope;
- staged vs published state when applicable;
- validation;
- conflict;
- audit/change history where important.

Do not make irreversible global policy changes feel like ordinary form saves.

## Audit and traceability

For high-impact admin actions, provide appropriate traceability:

- actor;
- action;
- target;
- time;
- previous/current value when feasible;
- reason/context when required.

Audit history should be readable, filterable when large, and protected by authorization.

Do not expose sensitive audit details to unauthorized users.

## Bulk administration

Bulk actions need explicit scope.

Show:

- selected count;
- all-visible vs all-filtered;
- consequence;
- partial success/failure;
- failed items;
- recovery/retry where supported.

Do not use a generic success toast for a partially failed bulk permission update.

## High-impact actions

Separate ordinary actions from:

- delete;
- revoke;
- suspend;
- reset credentials;
- rotate keys;
- transfer ownership;
- change role/permission;
- global configuration;
- destructive migration.

Use confirmation/reauthentication/approval according to actual product security rules.

The UI/UX layer must not invent or bypass security requirements.

## System health vs administration

If the admin dashboard includes health/operations:

- separate governance/configuration from live operational monitoring;
- load Monitoring/NOC rules when the monitoring job is substantial.

Do not mix critical incident status with routine user-management metrics without hierarchy.

## Search and findability

Administrative products often need fast entity lookup.

Support:

- exact identity search;
- filters by status/scope;
- permission-safe results;
- no-result recovery;
- stable deep links when appropriate.

## Responsive behavior

On narrow screens, prioritize:

- identity;
- status;
- scope;
- high-value action.

Move complex configuration/detail into dedicated pages or drawers where appropriate.

Do not squeeze large permissions matrices into unreadable cards.

## Validation checklist

Validate:

- full-access administrator;
- limited administrator;
- denied action;
- entity lifecycle transitions;
- permission/role change;
- bulk action with partial failure;
- global vs local scope;
- audit/history;
- destructive/high-impact action;
- responsive layout;
- accessibility;
- RTL/LTR.
