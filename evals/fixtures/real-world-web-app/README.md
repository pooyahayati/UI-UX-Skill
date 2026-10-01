# Real-World Web Application Fixture

Representative product: authenticated SaaS customer-management application.

Primary route: `web-application`

Intentional issues:

- filter and selected workspace state are not URL-addressable
- unsaved edits are lost on route change
- optimistic save reports success before server confirmation
- session expiry drops intended destination
- modal has no focus return contract
- destructive delete is a generic confirm
- loading replaces the whole shell
- repeated component styles bypass semantic tokens
- narrow layout hides essential actions

Expected evaluation:

- route Web Application, not Website
- preserve browser/history/deep-link behavior
- define draft/save/concurrency/session semantics
- use relevant Shared forms/state/destructive/accessibility/responsive rules
- apply reusable component-state and token contracts
- preserve permissions/data semantics
