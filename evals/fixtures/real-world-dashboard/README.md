# Real-World Dashboard Fixture

Representative product: all-day support operations dashboard.

Primary route: `dashboard`
Primary mode: `operational`
Secondary mode: `monitoring-noc`

Intentional issues:

- KPI cards dominate the page while the actual queue is below the fold
- SLA status uses color only
- live refresh reorders rows and loses selection
- no stale/disconnected state
- table uses fixed widths and overflows badly
- bulk action scope is ambiguous
- hard-coded raw colors/spacing bypass the design system
- compact density reduces focus/target clarity

Expected evaluation:

- route Dashboard before selecting Shared/Design System modules
- load operational + monitoring/NOC local packs
- preserve queue/SLA/business semantics
- improve data trust, live-update stability, bulk-action scope
- load relevant Shared Rules only
- use design-system density/state/theme contracts
- validate responsive/accessibility behavior or report render limitations
