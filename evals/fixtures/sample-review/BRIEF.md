# Dispatch Notes

An early browser web application for a small maintenance team. The principal job is to open an assigned visit, read instructions and record a completion note. Technicians often use phones; a coordinator reviews notes on desktop. Existing roles are technician and coordinator. Approved features are assigned-visit list, visit details and draft/completion notes. No billing, analytics, GPS tracking, chat, AI assistant or new roles are approved.

Default and sole supported language: English, LTR. Both light and dark mode are required. No brand font is supplied: use a legally available actual font and identify its asset/environment or report the gap. Browser/system fonts are allowed when actual resolution can be inspected. Preserve the product name; no identity replacement is requested. There is no backend or admin surface yet; do not create one to make a sample.

Use the same synthetic scenario across alternatives:

- Assigned visit: `VIS-204`, North Workshop, Tuesday at 09:30; assignee Sam Lee.
- Instruction: "Inspect the intake filter and record the reading before restarting the unit."
- Draft: "Filter replaced. Reading stable after restart."
- Long next task: "Inspect the north ventilation unit after the replacement filter arrives."
- Actions: open visit, edit note, save draft, mark complete. Label simulated save/error behavior; no real server guarantees are established.

The stakeholder has no design vocabulary and requests a professional recommendation plus comparable visible options. Balanced density and text labels for primary actions are protected baseline choices. Direction details remain open. Representative screens should explain this workflow, not add generic dashboard metrics or login to fill the sample set.
