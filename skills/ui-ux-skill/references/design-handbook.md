# Living Product Design Handbook

Use when establishing or materially evolving a product's design foundation. Discovery belongs to `discovery-and-profile.md`; this reference owns durable documentation, authority and compatible migration, not runtime implementation or sample generation.

## Location and ownership

The canonical filename is exactly `DESIGN.md`. Default to the product root; use an established product documentation directory when appropriate. Record the exact product-relative path and assigned writer in the existing project working contract. In a multi-product repository, name each product's boundary and canonical path rather than inventing one global approved design.

Inspect an existing `DESIGN.md` and other design documents first, including case-only filename collisions. Never overwrite user-authored content or create a second approved authority. Assign one writer for a revision; other agents propose changes. A narrow correction reuses the approved handbook or observed baseline; audit-only work does not create or migrate documents without permission.

## Early draft and usable scope

Start from [the output template](../assets/templates/DESIGN.md) during initial discovery, before broad UI implementation. The template is an output asset, not an approved product profile. Adapt it to supplied product evidence: preserve useful sections, omit irrelevant features and mark unknowns with a next action/owner/trigger rather than fabricating values or approval. A missing admin backend is not a reason to invent one.

Record enough for the next developer to identify the product, approved scope, UX structure, protected constraints, foundation proposals, actual languages/directions, light/dark expectations, implementation sources and remaining approvals without relying on chat history. Link requirements to workflows/screens, relevant component states/recovery and a verification method. Use existing requirement IDs when available; do not introduce a numbering system merely for ceremony.

Capture color/typography roles and scales, spacing/density, surfaces/borders/shadows, controls, semantic icons, responsive priorities and motion only where relevant. Record charts/diagrams when approved workflows require them. Inspect actual font assets and language formats; do not infer product language from conversation or claim rendered proof from this document. The first responsive proposal applies settled foundations in the primary language/direction/theme. Record dark needs early but derive/review dark only after primary approval; secondary language/layout follows dark approval only when needed and owner-authorized. Record monolingual secondary review as not applicable, not missing work.

## Authority, revision and evidence

Separate document lifecycle (`draft`, `approved`, `superseded`) from each decision's state (`proposed`, `approved`, `delegated`, `observed`, `unresolved`, `superseded`). An early draft may contain valid inherited approvals; an approved baseline may coexist with clearly labeled pending changes, which do not silently replace it. Mark a baseline approved only from actual scoped approval/delegation evidence; a revision bump alone never approves new changes.

For a meaningful decision retain its subject/value or real source, state, rationale, source/actor, date or explicit unknown, affected scope, and applicable document/sample revision. Inherited decisions retain their original provenance, not a fabricated new approval. Observation and inference are not approval; record reference location, supplied likes/dislikes and confidence separately. Keep private customer data, secrets and unnecessary conversation transcripts out of the handbook.

Explicit delegation applies only to its named decision/scope. Silence, preselection, image upload, implementation acceptance and a general agent recommendation do not approve the visual design. Record actual owner approval/delegation evidence and exact sample revision when it exists; a decision delegated without a sample is not proof of rendered fit. Never invent an approver, timestamp, sample or evidence URL to fill the template.

Increment the handbook revision for meaningful contract changes; preserve the last approved baseline and show which proposed changes are not yet active. Link the inspected Skill version when known, but do not invent it or couple document revisions to software releases. Track samples by phase, real path/identifier/revision, applied foundation sources, parent approved baseline, feedback/corrections and language/theme/viewport coverage; `planned`, `not run`, `unavailable` and `observed` must remain distinguishable. Use [the sequential sample/approval workflow](design-foundation-workflow.md) for phase gates, executable coverage and the approval/rollout boundary. Approval is not a claim that every test, permission or software feature is verified.

## Contract versus values

The handbook describes design intent, accepted defaults/policies, allowed controls and protected floors. Executable token values belong to the actual token/theme/component sources; published owner configuration, personal preferences and history belong to product storage. Link those authorities and actual consumers. If absent, say so; a proposed path or control is not an implemented source or panel.

Before code exists, numeric proposals may be documented as proposals. When implemented, link the actual source and reconcile drift rather than maintaining independently editable canonical copies of its values here. Classify applicable controls as `locked`, `owner-configurable`, `user-configurable` or `code-only`, with existing permission/scope, bounds/dependencies and implementation status. Icon families and semantic assignments follow the same boundary; this does not implement their picker or consumer.

Routine validated admin value changes use product configuration/version history; they do not require manual edits to `DESIGN.md`. Reopen the handbook when meaning, supported capabilities, protected limits or the approved design contract change. It is never a live settings database. Use `runtime-ui-governance.md` for actual resolution, persistence, preview, publication and reversal.

## Compatible migration

Migration is scoped product work, not an automatic rename on every UI task:

1. Inspect `DESIGN.md`, `design-profile.md` and established documentation, decisions/provenance, unresolved fields, token sources and their consumers. Search paths in project instructions, links, scripts/parsers, tests, generators and packaging. Check permissions and user edits before changes.
2. Choose the canonical target and writer. If documents conflict, retain the last demonstrably approved baseline, record the conflict and ask only the owning material decision. A newer date or filename does not establish authority. Do not merge inconsistent approvals silently.
3. Map valid legacy product/routing, audience/jobs, constraints, language/theme, visual and runtime-boundary fields to the template. Preserve values/meaning, source, dates, decision scope and open questions; do not turn a legacy document's global `approved` label into evidence that every unsupported field was approved. Keep legacy version identifiers as migration provenance, not the new document revision.
4. Work on a scoped copy/diff; add missing UX/state/coverage fields as observed, proposed or unresolved. Record the before/after path and baseline identity. Update actual consumers within authority; a text pointer cannot replace data expected by a parser. If necessary, retain a read-only/generated compatibility projection tied to the canonical revision, or defer conversion until the consumer has a safe compatibility path. Never create a second independently editable approved handbook.
5. Verify links/consumers, decisions, languages, themes, protected constraints and value-source ownership. Preserve an old path as an explicit non-authoritative compatibility pointer only when consumers need it. Removal/renaming requires verified dependencies, recovery and authority; do not delete the old file merely because the template exists. On failure preserve the previous usable baseline, report the blocking consumer and stop the affected migration.

Record actual migration checks and retained compatibility needs. Instruction examples and synthetic fixture transformations are not proof of an arbitrary application's parser/runtime compatibility. No blanket automatic migration script is required.

## Incremental handoff

Read the canonical path and approved baseline before a meaningful UI slice. Update only affected decisions, requirement coverage and material evidence; retain open questions with their trigger. Return baseline/revision, accepted versus proposed changes, protected invariants, real sample/source links, checks and limitations, unresolved conflicts and remaining approval. Do not duplicate raw chat or rebuild the entire document for a small correction.

Use [incremental decisions and handoffs](incremental-design-decisions.md) when a later slice introduces a new design need, preference/conflict or delegated contribution. It defines delta classification, necessary questions, dependent approval impact and lead acceptance without creating another design authority.
