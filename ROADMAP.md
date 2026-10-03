# UI/UX Skill Roadmap

This is the repository's durable roadmap and stage-progress reference. It preserves the completed capability-building history and defines the agreed correction workstream for design discovery, a living product design handbook, visual approval, and configurable appearance.

The correction workstream is planned, not implemented. Publishing this document does not start implementation, lift the stabilization policy, change installed Skill behavior, or authorize a merge or release.

## Current state

- Last updated: **2026-10-04**.
- Reviewed source baseline: **v3.1.1** at `d2420e9c60230fb2a667dff971f60a8bbbaaa1de`.
- Planning: **Complete**; the agreed requirements, stage outputs, dependencies, and acceptance gates are documented below.
- Implementation: **Not started**; **0 of 9 correction stages completed**.
- Active implementation stage: **None**.
- Next implementation stage: **R0 — Controlled kickoff**, after an explicit instruction to start corrections.
- Current authorized delivery: the English roadmap documentation only.
- Product handbook filename: **`DESIGN.md`**, with this exact capitalization.
- Additional external specialists: **None planned**. The existing conditional `persian-writing` route remains.
- Historical Stages 1–6: **Completed as recorded**, with the Stage 6 source-based evaluation limitations preserved below.

The source baseline is an evidence snapshot, not a permanent version pin. Recheck the actual branch, source changes, and instructions at implementation kickoff.

### Correction stage tracker

This table is the canonical stage status. Task checkboxes below describe progress within a stage; checking tasks does not by itself establish stage acceptance.

| Stage | Deliverable | Status | Dependencies | Accountable role | Completed on | Acceptance evidence / PR |
| --- | --- | --- | --- | --- | --- | --- |
| R0 | Controlled kickoff, policy consistency, and ownership | Not started | Explicit implementation authorization; valid working checkout | Engineering lead / maintainer | Not completed | Not recorded |
| R1 | Adaptive discovery and professional recommendations | Not started | R0 | Design role; engineering lead accepts | Not completed | Not recorded |
| R2 | Living `DESIGN.md` contract and profile migration | Not started | R1 | Design role; one handbook writer | Not completed | Not recorded |
| R3 | Comparable visual directions and versioned approval | Not started | R1, R2 | Design role; product owner approves | Not completed | Not recorded |
| R4 | Incremental decisions and bounded agent handoffs | Not started | R2, R3 | Engineering lead | Not completed | Not recorded |
| R5 | Parametric appearance governance with real consumers | Not started | R2, R4 | Engineering lead with design input | Not completed | Not recorded |
| R6 | Editable semantic icons and icon families | Not started | R5 | Engineering lead with design input | Not completed | Not recorded |
| R7 | Integrated language, direction, theme, and visual quality | Not started | Contracts begin in R1/R3; final gate after R6 | Design role; engineering lead accepts | Not completed | Not recorded |
| R8 | Behavioral evaluation, package verification, release readiness | Not started | R0–R7 | Engineering lead / maintainer | Not completed | Not recorded |

Language, direction, accessibility, and dark mode start with discovery and the first samples. R7 is their integration gate, not permission to postpone them. Define and run stage-relevant checks during each stage; R8 is the final gate, not the first testing stage.

### Mandatory progress-update protocol

1. Before starting an authorized stage, read this roadmap, the actual repository state, the applicable instructions, and the preceding stage's evidence. Update the active stage, owner, scope, date, and stage status to `In progress`.
2. During the stage, check only tasks actually performed. Record meaningful partial delivery, unresolved decisions, and concrete blockers. Do not mark the entire stage complete because its documents exist or a PR was opened.
3. At stage completion, record the changed paths, implementation commit or PR, relevant check commands and actual results, required visual/behavioral evidence, limitations, and the engineering lead's acceptance. Record product-owner approval only when it was really given.
4. Change the stage to `Completed` only when its exit criteria are satisfied. Set the completion date and evidence links, update the completed-stage count, and name the next executable stage or explicit approval gate.
5. Commit the meaningful roadmap update with the stage's authorized delivery. Keep it on the working branch until any required merge approval. A proposed PR must not be presented as already integrated into `main`.
6. If work cannot proceed, use `Blocked` with the concrete dependency, recovery action, and required decision. If a completed stage is invalidated by new evidence, use `Reopened` and explain the affected acceptance criteria. Preserve prior evidence rather than silently rewriting history.
7. Keep operational caches, temporary screenshots, tool state, and generated scan/test reports outside product source. Link durable test results or review artifacts that the project actually retains; never fabricate Issues, PRs, milestones, or checks.

Allowed stage states: `Not started`, `In progress`, `Blocked`, `Completed`, `Reopened`. A future stage is not blocked merely because its predecessor has not started. The active stage, tracker, checked tasks, completion evidence, and next action must agree before handoff.

There are currently no completed correction-stage records. When a stage is accepted, retain a concise dated completion entry here or in its linked PR; the tracker must link to that real record. Do not require a second competing status document solely for this workstream.

## Principles

- Product design knowledge stays local to this repository.
- `persian-writing` remains the only external specialist unless explicitly changed later.
- Product Packs contain product-specific methodology.
- Shared rules should be extracted only when repetition becomes real and stable.
- Behavioral evals and release validation protect existing capabilities.
- Product routing should minimize context and keep inactive Product Packs unloaded.
- Prefer evidence-backed rules and current platform guidance over stylistic opinion.
- During the feature freeze, changes are limited to deduplication, context isolation, correctness, validation, documentation, and release maintenance.

## Correction objective and boundaries

The Skill should guide a coherent process:

`Inspect product evidence -> Discover needs and preferences -> Recommend -> Build representative samples -> Approve a revision -> Maintain DESIGN.md -> Implement and validate configurable design`

The goal is a final interface that stays close to the product owner's intent and avoids avoidable redesign. It is not a guarantee of zero revisions, complete discovery of unknown future needs, or usability without testing.

This work improves the Skill's contracts, routing, reusable assets, and evaluations. It does not turn the Skill repository into a universal application/theme builder. Small representative executable fixtures may prove the contracts; production implementations must follow their own approved software scope and stack.

### Planned limited exception to stabilization

The agreed correction package is limited to **design foundation, the living handbook, visual approval, and safe parametric appearance management**. R0 must reconcile the roadmap, README, and release-validation policy before capability implementation starts. The current stabilization contract remains in place for this documentation-only update.

Do not add new Product Types, external design specialists, mandatory cloud services, a mandatory frontend framework, or a general-purpose page builder. Avada Theme was an illustration of owner-editable appearance, not an architectural dependency or a request to reproduce WordPress everywhere.

The installed Skill and source capability version remain unchanged by roadmap publication. Choose the correction release version later: a compatible capability addition normally calls for a minor version; incompatible behavior requires an explicit major-version decision. Do not disguise this work as a patch release.

### Scope-sensitive activation

- **New product or broad redesign:** establish design foundations and representative samples before broad UI rollout. For products with an admin surface, Design and Appearance settings are part of delivery, not an optional omission merely because the product is small.
- **Existing product, narrow correction:** reuse the approved handbook or observed baseline. A button/form/RTL fix must not trigger a full interview, global redesign, new admin panel, or infrastructure expansion. Record an absent appearance panel as follow-up scope; implement it only when authorized.
- **Product without an admin surface:** raise the appearance-management need to the engineering lead. Do not invent accounts, a backend, or an admin application merely to provide theme settings. Choose a host-appropriate management surface only within approved product scope.
- **Native/mobile and hosted products:** account for asset packaging, distribution, and host restrictions. WordPress work changes only the owned plugin/product surfaces; it does not restyle all of `wp-admin` without permission.
- **Audit-only or backend-only request:** do not mutate the product or activate unrelated design implementation.

## Agreed correction requirements

| ID | Requirement | Responsible stages | Observable acceptance |
| --- | --- | --- | --- |
| F01 | Adaptive discovery based on product subject, audience, breadth, approved features, and sections | R1 | Relevant questions; known information is reused |
| F02 | Mandatory professional recommendation, rationale, and a small alternative set | R1 | A novice can choose or explicitly delegate a choice |
| F03 | Image/reference intake, including likes and dislikes | R1 | Provenance and inference confidence are recorded |
| F04 | Early designs before full feature/backend implementation | R3 | Representative screens identify synthetic data and hypothetical capabilities |
| F05 | Usually two or three coherent, comparable directions | R3 | Equivalent content and scenarios make meaningful differences visible |
| F06 | Approval of a specific design revision | R3 | The selected sample, decision, and approval source are traceable |
| F07 | An initial and living product handbook named `DESIGN.md` | R2 | Another agent can use the canonical document without chat history |
| F08 | Incremental questions and recorded decisions during development | R4 | Only genuinely new or conflicting decisions are reopened |
| F09 | Strong recommendation to delegate substantial early design work to a bounded subagent | R0, R1, R4 | Lead ownership, limited handoff, and honest fallback are retained |
| F10 | No additional external design specialists | All | Existing specialist inventory is not expanded |
| F11 | Appearance settings belong in delivery for in-scope products with admin | R5 | The panel is an explicit product plan and acceptance item |
| F12 | Editable colors, fonts, sizes, spacing, borders, shadows, and component style | R5 | Valid changes reach their consumers and persist |
| F13 | Editable icon family and individual semantic icon assignments | R6 | Gallery, shared mapping, preview, and rollback work |
| F14 | Separate the handbook from active runtime configuration | R2, R5 | Routine admin changes need no manual handbook or code edit |
| F15 | Use the default and supported product languages | R1, R7 | Product language is not inferred from the conversation language |
| F16 | Support the product's LTR, RTL, and multilingual directions | R7 | Directional behavior and mixed-script content are verified |
| F17 | Light and dark mode from the first samples through delivery | R3, R7 | Samples, handbook, settings, and checks cover both |
| F18 | Draft, preview, validation, publish, history, and rollback | R5 | Drafts stay private and active revisions are identifiable/reversible |
| F19 | Preserve behavior, authorization, data, and the existing stack | All | Relevant protection checks and change boundaries are recorded |
| F20 | Rendered and behavioral evidence, not source-text checks alone | R8 | Real representative execution and honest limitations are recorded |
| F21 | Do not impose Avada, WordPress, or a replacement stack | R0, R5 | Implementation fits the existing product and host |
| F22 | Compatible migration from the prior design profile | R2 | One canonical approved handbook; decision provenance survives |

## Agent responsibility and delegation contract

The primary programming/engineering lead owns software scope, architecture, risk, integration, user communication, final acceptance, and release decisions. A design role recommends and proves design within that boundary; it does not invent features or change backend/security architecture.

Strongly recommend a subagent using this same UI/UX Skill for substantial foundation work in new products or broad redesigns. This is a recommendation to the future programming lead, not a request to launch an agent during roadmap publication or to install a new external specialist. It does not grant permission to create a new user-owned chat.

When delegation is unavailable or unauthorized, the lead performs the same bounded work and states that no subagent was used. Avoid making delegation a blocker to otherwise permitted work.

The handoff input includes approved product goals, type, audience/roles, features, stack, languages/directions, existing assets and decisions, constraints, file-write ownership, acceptance criteria, and handbook path. The return includes recommendations and rationale, genuinely open questions, displayable samples, proposed handbook changes, assumptions, evidence/limitations, conflicts, and approvals still needed.

Keep detailed investigation in the design work and present concise decisions in the main conversation. Do not promise invisible activity, transfer the user automatically to another chat, or ask duplicate competing questions. Assign one writer to the canonical handbook and shared contracts; parallel agents may propose changes but must not concurrently overwrite approved decisions.

## Correction stages and exit criteria

All actions below are planned and unchecked. They are not evidence that the requested capabilities already exist. Stage order describes dependencies, not separate mandatory approvals for every routine task. Reuse settled approvals; obtain fresh direction only for material new decisions or actions requiring additional authority.

### R0 — Controlled kickoff and consistent policy

Owner: engineering lead / maintainer. Prerequisites: explicit implementation-start instruction and a valid working checkout.

Tasks:

- [ ] Recheck upstream source, applicable instructions, branch, local/upstream SHAs, dirty state, and protected user changes; record the implementation baseline.
- [ ] Work on an authorized branch with the `codex/` prefix; preserve `main` and unrelated work.
- [ ] Reconcile the limited correction exception with the roadmap and README while preserving completed historical stages and evaluation limitations.
- [ ] Update the release validator's active-freeze contract to recognize the explicit limited exception without weakening Product Type isolation, historical-stage preservation, or the no-new-specialists boundary. The current validator requires the legacy freeze to remain active; this dependency must not be overlooked.
- [ ] Define full-foundation versus narrow-change routing, the admin-panel activation boundary, and audit/backend exclusions with distinguishable examples.
- [ ] Define lead/subagent authority, a bounded early-design handoff, unavailable-tool fallback, and one-writer ownership.
- [ ] Record acceptance criteria, stage-update responsibilities, and a later versioning decision; do not bump the version just to start the workstream.

Output: accepted implementation scope, consistent development policy, ownership/handoff contract, and actual baseline check results.

Exit: the implementation scope is authorized; policy documents and validators no longer contradict the correction exception; mandatory admin delivery and narrow-task non-expansion are distinguishable; no new specialist, stack, or agent permission is invented. Attach the reviewed diff, baseline results, and accepting lead decision before marking R0 complete.

### R1 — Adaptive discovery and designer recommendations

Owner: design role within the lead's boundary. Prerequisite: R0.

Tasks:

- [ ] Inspect existing product documents, assets, interfaces, decisions, and stack before asking the user.
- [ ] Extract product type, audience/roles, principal jobs and workflows, breadth, approved sections/features, and practical constraints; separate UX needs from visual preferences.
- [ ] Record the default language, supported languages, direction per language, and localization requirements explicitly. A Persian conversation can describe an English product.
- [ ] Use a short, product-relevant question sequence rather than a fixed exhaustive questionnaire. Let the user answer, attach references, select a proposal, or explicitly delegate a choice.
- [ ] For key decisions, always give a primary professional recommendation, product/audience rationale, and limited alternatives, with room for a custom preference.
- [ ] Cover relevant palette, typography roles/sizes, style, spacing/density, borders, controls, charts/diagrams, icons, effects/motion, responsive behavior, accessibility, and light/dark preferences; do not ask about irrelevant features.
- [ ] Accept screenshots/images and verbal references; record what the user likes and dislikes, provenance, confidence, and observed versus inferred properties. Do not claim exact font, motion, spacing, or interaction from an ambiguous static image.
- [ ] Treat silence as unresolved, not approval. Distinguish user choice, explicit delegation, an agent proposal, and protected product constraints.
- [ ] Resolve most foundation decisions early and leave genuinely unknown details open for the appropriate development stage; do not invent capabilities or roles to fill a form.

Output: initial design brief, evidence-backed recommendations, preferences/constraints, assumptions, and a focused open-question list.

Exit: both a design novice and an experienced owner can make progress; known information is not reasked; recommendations fit the actual product; reference images are not treated as permission to copy identity/assets or expand functionality. Attach representative discovery transcripts/evaluation results before acceptance.

### R2 — Living `DESIGN.md` and compatible migration

Owner: one assigned handbook writer. Prerequisite: R1.

Tasks:

- [ ] Define the canonical product handbook as `DESIGN.md`, with this exact capitalization, and record its location in the product's working contract.
- [ ] Provide a usable initial template early, not only a document written after implementation is finished.
- [ ] Link requirements to workflows, screens, components, states, and verification methods; cover UX structure as well as visual styling.
- [ ] Track proposed, approved, and open decisions with their real approval/delegation source, revision, and relevant sample.
- [ ] Define one canonical handbook and one writer; preserve enough context for another agent to continue without chat history.
- [ ] Migrate valid `design-profile.md` or other established design documentation into the canonical handbook compatibly. Inspect consumers before renaming/removing anything; preserve provenance and references.
- [ ] Avoid two independent approved documents or duplicated canonical token values. Preserve an old document as an explicit compatibility reference only when required, with the new authority clear.
- [ ] Keep runtime token values/configuration in their real implementation sources. The handbook defines approved roles, initial defaults, policies, allowed controls, and links to those sources.
- [ ] Do not require manual handbook edits for every routine admin setting change. Active configuration comes from product storage and version history.

Minimum handbook content:

| Section | Required content |
| --- | --- |
| Identity and governance | Revision, status, date, owner, scope, and canonical path |
| Product and audience | Product type, roles, principal jobs, approved features, constraints |
| UX foundation | Information architecture, workflows, interaction/state/recovery expectations |
| Preferences and evidence | Likes/dislikes, references, provenance, inference confidence |
| Languages and directions | Default/supported languages, LTR/RTL, fonts and localization |
| Visual foundation | Color/typography roles, sizes, spacing, borders, shadows, light/dark rules |
| Components and icons | Approved variants/states and semantic icon assignments |
| Samples and approval | Sample revision, language/theme coverage, feedback, selected direction |
| Configurability | Parameters, scope, limits, dependencies, permissions and storage boundary |
| Implementation links | Real value sources, consumers, and verification methods |
| Incremental decisions | Open questions, meaningful decisions, impact and change history |
| Acceptance | Requirement coverage, actual evidence, limitations and outstanding decisions |

Output: handbook contract, a reusable template, and a migration scenario.

Exit: another agent can identify approved/open decisions without the chat; migration preserves meaning and authority; admin changes are not tied to manually editing the document. Attach template/fixture results and the migration evidence.

### R3 — Visual directions, representative prototype, and approval

Owner: design role; product owner approves the design revision. Prerequisites: R1, R2.

Tasks:

- [ ] Select representative screens from important audience workflows and explain the choice; do not always choose login/dashboard screens regardless of product.
- [ ] Usually present two or three coherent directions with comparable content and scenarios. A different count needs a proportionate scope-based reason.
- [ ] Use the default product language, real text and fonts, and both light and dark mode from the first samples.
- [ ] Provide representative samples for other supported languages and their real directions, including bilingual/multilingual products.
- [ ] Build early samples without waiting for the full backend or all features. Clearly mark synthetic data and hypothetical capabilities; approving their appearance does not add them to software scope.
- [ ] Use conceptual images when useful for selecting direction, but prove real typography, direction, layout, and behavior with an executable sample before claiming those qualities validated.
- [ ] Inspect the selected direction on desktop and mobile with relevant normal, loading, empty, error, success, disabled/access, and recovery states.
- [ ] Ask for feedback about specific parts, revise deliberately, and record approval of a specific sample/handbook revision before broad rollout.
- [ ] Do not interpret approval of a few screens as approval of unbuilt pages, new features, or all future decisions.

Output: comparable visible directions, an executable selected sample, an approved handbook baseline, and actual coverage/limitations.

Exit: the sample and handbook agree on revision; both themes and relevant languages are visible; approval is real and scoped. Source inspection or a passing build cannot substitute for rendered evidence. Attach sample locations, observations/screenshots, revision, and approval source.

### R4 — Incremental development and bounded handoffs

Owner: engineering lead. Prerequisites: R2, R3.

Tasks:

- [ ] Require the current handbook and affected constraints to be read before each meaningful UI development slice.
- [ ] Reuse approved decisions; resolve compatible details within authority rather than interviewing the user again.
- [ ] Identify genuinely new needs, conflicts, or strategic changes and their impact on screens, components, runtime settings, and existing approvals.
- [ ] Keep preference changes separate from changed user needs or software feature scope; obtain required approval before expanding a strategic change.
- [ ] Update only affected handbook/sample sections and retain meaningful decision provenance.
- [ ] Require agent handoffs to identify the baseline revision, proposed/accepted decisions, evidence, unchecked areas, conflicts, and remaining approvals.
- [ ] Demonstrate continuation with one new design need without uncontrolled style drift or duplicate questioning.

Output: incremental decision/handoff contract and a continuation evaluation.

Exit: a new slice follows the approved foundation, only necessary new questions are asked, and conflicting feedback is resolved as one product decision rather than parallel values. Attach the continuation/handoff evidence and lead acceptance.

### R5 — Parametric appearance management with real consumers

Owner: engineering lead with design input. Prerequisites: R2, R4.

Tasks:

- [ ] Make admin appearance management mandatory for in-scope new/broad work on products with admin, while retaining the narrow-change and no-admin boundaries.
- [ ] Define each setting's ownership and effect: product surface, owned admin surface, organization/tenant, or user. Preserve isolation and protected precedence.
- [ ] Reuse the product's current technology and native/host controls. Do not migrate frameworks to resemble the example theme.
- [ ] Define validated configuration, resolution, persistence, and component-consumption boundaries; do not scatter raw settings or hard-coded configurable values through pages.
- [ ] Offer coherent presets/simple controls plus bounded advanced settings, with human-readable names, defaults, allowed values, dependencies, permissions, consumers, and reset behavior.
- [ ] Cover colors/brand, available fonts and typography sizes, line height, spacing/density, borders/radii/shadows, component style, light/dark modes, motion, and supported chart/diagram styles.
- [ ] Connect charts, overlays, icons, error screens, and independent assets through appropriate adapters; changing CSS variables alone is not proof of complete consumption.
- [ ] Define isolated draft, preview, validation, publish, active-version identity, history, rollback, reset, and safe defaults; keep public rendering on the published version.
- [ ] Enforce authorization and input constraints at the trusted boundary, not only by hiding a menu.
- [ ] Verify persistence, refresh behavior, cache invalidation, partial/failing loads, and coherent publication.
- [ ] Restrict choices to prepared/legal assets and variants. Adding a new font/library or unbundled asset may require preparation/build; routine supported setting changes must not require editing a page.
- [ ] Do not substitute arbitrary CSS, JavaScript, HTML, or executable asset input for safe parametric controls. Optional import/export must validate schema, show differences, and never publish silently.

Output: implementation-neutral panel contract and a small stack-appropriate executable fixture proving color, font, density, and component-shape changes.

Exit: valid published changes visibly affect relevant consumers and survive refresh; invalid/unauthorized writes are rejected; drafts remain private; fallback and rollback really work. Attach runtime, persistence, denial/isolation, and rollback evidence. A settings form or JSON file alone does not satisfy this gate.

### R6 — Editable semantic icons

Owner: engineering lead with design input. Prerequisite: R5.

Tasks:

- [ ] Define central semantic assignments for designed uses such as search, add, edit, delete, and settings.
- [ ] Provide a visible gallery for choosing an available family and replacing the icon assigned to an individual semantic use.
- [ ] Route all applicable component/page uses through the assignments, not isolated page-level imports beyond admin control.
- [ ] Define valid per-family mappings and safe meaningful fallbacks for missing icons; incomplete families must not break the interface.
- [ ] Offer size, color, and stroke controls only when supported; do not show ineffective stroke controls for incompatible solid assets.
- [ ] Preserve accessible names, operation meaning, directional behavior, and meaningful open/closed state pairs.
- [ ] Do not execute unknown uploaded vector/code assets directly. Arbitrary uploads require a separately scoped safe asset pipeline.
- [ ] Include family/per-use changes in preview, publication, refresh, rollback, and both themes.

Output: icon contract and an executable family/per-use replacement fixture.

Exit: changing the search assignment updates all relevant uses; a missing icon has a safe fallback; meaning/accessibility/direction remain intact; selection persists and rollback restores it. Attach actual rendered and state evidence.

### R7 — Language, direction, theme, and integrated quality

Owner: design role; engineering lead accepts. Contracts start in R1/R3; final integration follows R6.

Tasks:

- [ ] Validate the default and supported product languages independently from the conversation language; cover only actual supported directions for monolingual products and all relevant directions for multilingual products.
- [ ] Use real fonts/text, number/currency/time/calendar conventions, longer translations, and mixed-script identifiers appropriate to the product.
- [ ] Activate existing `persian-writing` when the product supports Persian; do not copy its methodology into the UI/UX Head or force it into English-only products.
- [ ] Keep one coherent design system across directions, using logical relationships rather than a separate conflicting RTL theme.
- [ ] Mirror only icons/interactions whose meaning is directional; do not blindly mirror logos or every chart.
- [ ] Use semantic dark-mode roles and component states rather than mechanical color inversion; verify brand assets and chart readability.
- [ ] Inspect forms, tables, menus, messages, overlays, charts, focus, selection, disabled/access states, and recovery in relevant themes, languages, and viewports.
- [ ] Ensure configurable typography/spacing does not violate readability, touch targets, keyboard/focus behavior, reduced-motion preferences, or host accessibility capabilities.
- [ ] Select a justified representative coverage matrix; do not demand a blind Cartesian product of every state, but do not omit critical combinations.

Output: representative coverage matrix and rendered/behavioral evidence for relevant languages, directions, themes, sizes, and states.

Exit: English-only samples are not unintentionally Persianized; bilingual samples preserve both directions; dark mode covers more than the page background; unchecked areas are explicit. Attach concrete coverage and findings, not a blanket QA claim.

### R8 — Behavioral evaluation, packaging, and release readiness

Owner: engineering lead / maintainer. Prerequisites: R0–R7.

Tasks:

- [ ] Preserve and run existing structural/regression validators; record actual results and new failure cases.
- [ ] Add evaluations for professional recommendation, references, `DESIGN.md`, approval, incremental decisions, delegation/fallback, settings, icons, languages, and themes.
- [ ] Verify observable behavior and real data, not merely the presence of headings/phrases; keep structural evidence distinct from agent execution quality.
- [ ] Execute small representative fixtures only in authorized isolated environments; do not test against production data/systems without permission.
- [ ] Perform a fresh independent evaluation when the required tooling and authorization are available; give realistic requests and raw inputs without supplying the intended answer.
- [ ] Record missing independent-agent, browser, or device evidence honestly; do not relabel source inspection as those checks.
- [ ] Recheck existing Website, Dashboard, Web Application, Mobile Application, and WordPress Plugin routes and context isolation.
- [ ] Verify the handbook template, routed references, and matching version metadata inside the exact candidate installable packages.
- [ ] Review the actual diff, requirements coverage, evidence, compatibility, outstanding risks, and permitted delivery actions.
- [ ] Separate candidate readiness from merge, release, deployment, and local installation; perform those only with appropriate authorization.

Output: fresh behavioral results, representative executable evidence, exact validated candidate packages, and an accurate readiness report.

Exit: no unexplained required failure remains in protected behavior, approval, settings, icons, language, or themes; mandatory claims have appropriate evidence. Record outstanding external authority rather than treating preparation as publication.

## Planned destination-file impact

This is an impact map, not permission to change every listed file now. New files are justified only when they separate a meaningful responsibility. Keep the entrypoint short and route conditional detail; retain product-specific rules inside the active Product Pack.

| Destination | Planned change | Responsibility |
| --- | --- | --- |
| `ROADMAP.md` | Current stage, tasks, dependencies, acceptance evidence, and preserved history | Durable execution tracking |
| `README.md` | Consistent limited-exception and deliverable summary in R0 | Concise project introduction |
| `skills/ui-ux-skill/SKILL.md` | Entry triggers, key gates, handbook routing, bounded delegation | Thin Head |
| `references/discovery-and-profile.md` | Adaptive recommendations, image evidence, and profile migration | Discovery |
| `references/design-foundation-workflow.md` | Add only if the substantial sample/approval workflow warrants a separate reference | Proposed conditional workflow |
| `references/design-handbook.md` | Add only if handbook lifecycle needs a distinct routed responsibility | Proposed handbook contract |
| `assets/templates/DESIGN.md` | Usable initial product-handbook template | Proposed output asset |
| `references/specialist-routing.md` | Bounded input/return, authority, fallback, and updated document references | Agent handoff |
| `references/existing-product-audit.md` | Reuse baseline and preserve narrow/audit scope | Existing products |
| `references/runtime-ui-governance.md` | Scoped admin requirement, safe controls, lifecycle | Runtime owner configuration |
| `references/design-system-architecture.md` | Handbook/value-source/configuration links without competing authorities | Shared architecture |
| `references/implementation-strategies.md` | Real stack-native consumption, chart and semantic-icon adapters | Implementation strategy |
| `references/theme-responsive-brand.md` | Available assets, themes, and editable presentation | Brand and appearance |
| `references/rtl-ltr-typography.md` | Default/supported-language policy and direction coverage | Language and typography |
| `references/qa-checklist.md`, `references/visual-regression.md` | Handbook, settings, language, theme, and rendered acceptance | QA |
| `references/design-system/governance-migration.md` | Compatible document/configuration migration and ownership | Compatibility |
| `evals/cases.json` and related fixtures | New meaningful behavior and protected regression scenarios | Evaluation |
| `scripts/validate_design_system.py`, `scripts/validate_eval_fixtures.py` | Structural contract/fixture checks when relevant | Validation |
| `scripts/validate_release.py` | R0 policy consistency; required package-resource checks when needed | Release invariants |
| `scripts/package_release.py` | Change only if new resources are not already packaged correctly | Packaging |
| `.github/workflows/validate-skill.yml` | Add justified real checks without dropping existing protection | CI |
| `CHANGELOG.md`, root/Skill `VERSION`, `plugin.json` | Synchronize only at the candidate-version gate | Versioned delivery |

Short `references/` and `assets/` paths above are relative to `skills/ui-ux-skill/`. They are destination plans, not files created by this documentation update. Update `product-types.json`, `shared-rules.json`, or `design-system.json` only if their routing contracts actually change. Do not add new entries to `specialists.json`.

## Appearance parameter contract

For each supported parameter, define its human-readable label, effect scope, type, approved default, allowed values/range, dependencies, validation, consumers, permissions, storage, theme/language applicability, reset, and rollback behavior.

| Group | Expected supported controls | Protected limits |
| --- | --- | --- |
| Brand and color | Palette/semantic colors, backgrounds, text, borders, approved assets | Contrast, status meaning, asset rights |
| Typography | Available families, roles, sizes, weights, line height | Language coverage, readability, real asset availability |
| Spacing and density | Section/component spacing, control and row sizing | Touch targets, content fit, mobile behavior |
| Shape and component style | Radius, elevation, borders, existing component variants | Focus/selected/disabled states and interaction meaning |
| Icons | Available family, per-use semantic assignment, supported visual properties | Meaning, direction, accessibility, missing-icon fallback |
| Themes | Light/dark defaults; system preference when supported | Coherent consumers, valid state colors, theme-flash prevention |
| Motion | Approved motion level and prepared behaviors | Reduced motion, performance, unchanged workflow |
| Charts and diagrams | Colors, text, lines, and existing presentation variants | Data meaning and relationship structure |
| Layout | Approved layout variants and bounded dimensions | Routes, workflow, authorization, host constraints |

The no-code promise applies to prepared, connected parameters/assets/variants, not every imaginable design change. A new library, feature, unbundled font, or asset may require code/build preparation, especially on native platforms.

The handbook describes the approved contract and links to real default/value sources. The active owner configuration lives in product configuration/storage and is resolved at runtime under protected constraints. Routine admin changes must not require manually editing `DESIGN.md` or component source. A setting is accepted only when actual consumers visibly use it and persistence/reversal are proven.

## Planned acceptance scenarios

All correction scenarios below are **planned, not run**. Previous fixture/schema results do not prove the new capabilities.

| ID | Scenario | Observable expected result |
| --- | --- | --- |
| E01 | Owner unfamiliar with design | Clear primary recommendation, rationale, and choice/delegation path without a long technical interview |
| E02 | Owner supplies visual references | Likes/dislikes and confidence are recorded; inference is not relabeled approval |
| E03 | English product discussed in Persian | Samples and handbook use English/LTR, not the conversation language |
| E04 | Persian product | Real Persian text/fonts and correct RTL behavior |
| E05 | Persian/English bilingual product | Representative samples cover both directions and mixed-script content |
| E06 | Comparable design directions | Equivalent content, meaningful differences, light/dark samples, selected revision |
| E07 | Features/backend incomplete | Early samples are shown; hypothetical data/features are marked; scope stays protected |
| E08 | Initial sample approval | Handbook and samples refer to the same actually approved revision |
| E09 | Prior design profile exists | Compatible migration preserves provenance and one canonical authority |
| E10 | A new need appears during development | Only relevant decisions reopen; impact and handbook changes are recorded |
| E11 | Delegation is authorized and available | Bounded assignment and concise return; lead retains acceptance |
| E12 | Delegation unavailable or unauthorized | Permitted work continues without falsely claiming a subagent |
| E13 | In-scope product has admin | Appearance management is explicitly included in plan and delivery |
| E14 | Change color, font, and density | Relevant pages change, refresh preserves settings, no component/page edit is needed |
| E15 | Change family and search-icon assignment | Shared uses update and incomplete-family fallback remains meaningful |
| E16 | Draft versus published settings | Draft remains nonpublic; the active published revision is identifiable |
| E17 | Invalid setting or unauthorized actor | Trusted boundary rejects it and stored values/permissions remain unchanged |
| E18 | Rollback or configuration-load failure | Valid prior configuration or safe defaults are actually applied |
| E19 | Settings import, if offered | Schema/differences are validated and publication is not automatic |
| E20 | Dark mode on mobile and supported languages | Forms, tables, menus, charts, messages, and component states remain usable |
| E21 | Narrow existing-product change | No forced full discovery, new admin panel, or global redesign |
| E22 | Backend-only request | Unrelated UI foundation work is not activated |
| E23 | Role/user/tenant protection | Appearance changes do not alter permissions or another owner's data |
| E24 | Exact installable candidate | Template, references, routing, and consistent versions are really packaged |

For initial executable proof, include an RTL Persian, an LTR English, and a bilingual representative product profile. At least one must have actual admin controls to prove change, persistence, denial, and rollback. Reuse/extend existing small fixtures where appropriate; three large new applications are not required.

Rendered checks, authorization checks, and persistence checks are distinct evidence. Source inspection/build success proves only those observations. Preference fit needs owner feedback; safety and configuration contracts need relevant executable assertions.

## Existing verification to preserve

Run applicable checks from a valid repository checkout with an approved runtime. Preserve the existing validation workflow; future implementation must not weaken it to fit the new roadmap.

```bash
python3 scripts/validate_release.py
python3 scripts/validate_product_routes.py
python3 scripts/validate_shared_rules.py
python3 scripts/validate_design_system.py
python3 scripts/validate_specialists.py
python3 scripts/validate_eval_fixtures.py
python3 scripts/validate_real_world_evaluation.py
python3 scripts/validate_eval_result.py evals/real-world/result.json
```

Follow [the eval harness](evals/README.md) for fresh meaningful runs and result validation. Require all applicable candidate cases when they have actually been executed; never substitute a valid old JSON schema for fresh behavior evidence.

For this documentation-only publication, any baseline validators/package checks concern the unchanged Skill and roadmap compatibility. They do not count as executed correction scenarios or completed R0–R8 work. The associated PR/check runs record the actual publication-validation outcome.

The package script removes an existing output directory before building. Inspect its actual behavior and use an explicit isolated output directory whose target has been validated and contains no user data. Archive/package checks do not authorize installation or release.

Reference workflows: [validation](.github/workflows/validate-skill.yml) and [release](.github/workflows/release.yml). A push to `main` or a version tag can invoke release automation. A documentation update does not justify bypassing merge/release authorization, altering that workflow, or bumping the version.

## Acceptance and publication gates

| Gate | Required evidence / condition |
| --- | --- |
| Kickoff | Authorized scope, valid source, protected user work, consistent policy |
| Design foundation | Product-relevant discovery, justified recommendations, initial handbook, explicit open questions |
| Sample approval | Visible revision, real product languages/fonts, light/dark coverage, actual approval or explicit delegated choice |
| Runtime configurability | Connected consumers, persistence, private drafts, trusted permissions/validation, real rollback |
| Integrated QA | Relevant rendered/behavioral evidence, protected previous contracts, no unresolved required failures |
| Candidate package | Consistent version/resources, exact archive checks and installation check in an authorized environment |
| Publication | Required final acceptance and separate authorized push/merge/release actions under project policy |

Use the approved scope and real evidence at each gate. Missing tools/data leave dependent results unverified; no synthetic pass or blanket design-quality claim is allowed.

## Risks and mitigations

| Risk | Mitigation / responsible stage |
| --- | --- |
| Bloated entrypoint or repeated method | Thin Head, scope-based references, no duplicate canonical contract; R0/R8 |
| Legacy active-freeze validator conflicts with correction policy | Explicit compatible policy/validator change before implementation; R0 |
| Prototype implies new product capabilities | Mark hypothetical content; separate visual approval from feature scope; R3 |
| Competing handbook/value authorities | Compatible migration, one canonical handbook, links to real sources; R2 |
| Repetitive/excessive questions | Inspect first and reopen only new/conflicting decisions; R1/R4 |
| Decorative settings panel with no real effect | Verify consumers, persistence, draft isolation, failure, and rollback; R5 |
| Incomplete or misleading icon families | Semantic mappings, visible approved gallery, fallback and accessibility; R6 |
| Persian chat incorrectly determines product language | Explicit default/supported-language contract; R1/R7 |
| Dark mode deferred or incomplete | Both themes from first samples through actual component/chart QA; R3/R7 |
| Small fix becomes global redesign/admin project | Full versus narrow scope contract and authorized follow-up only; R0 |
| Agent races or hidden approval assumptions | Bounded handoff, one writer, lead acceptance, actual owner approval; R4 |
| Structural checks mistaken for real-agent/rendered success | Separate evidence types and record limitations; R8 |
| Unintended merge/release | Separate branch/PR, version unchanged, explicit delivery authority |

## Readiness and next action

Planning readiness:

- [x] The agreed requirements, exact `DESIGN.md` name, language/direction correction, and dark-mode requirement are captured.
- [x] The source baseline, historical roadmap, validation/release workflows, and applicable contribution rules have been inspected.
- [x] Stages have outputs, dependencies, owners, tasks, and exit criteria.
- [x] Handbook migration, runtime-storage separation, scoped admin delivery, and editable icons have distinct acceptance criteria.
- [x] The stage-status update protocol and evidence discipline are defined.
- [x] Existing narrow/audit/backend boundaries and the no-new-specialists decision are preserved.

Still pending:

- [ ] Explicit authorization to start Skill capability corrections.
- [ ] Execution and evidenced acceptance of R0–R8.
- [ ] Fresh correction behavior/rendered/runtime evidence and exact candidate package verification.
- [ ] Any separately required integration, release, deployment, or installation authority.

**Next implementation action:** start R0 only after an explicit implementation-start instruction, reusing this roadmap and rechecking current source. The first visible capability result is the initial handbook and representative light/dark samples in real product languages by R3; a large admin application or all backend features are not prerequisites for that design proof.

No calendar duration or cost is promised. This roadmap defines the execution sequence and acceptance conditions; estimate schedule after the authorized scope and available tooling are confirmed.

## Completed capability history

Stages 1–6 are complete as recorded below. These historical statuses, version targets, and limitations are retained independently from the not-started R0–R8 correction tracker. The historical Stage 6 result is not fresh execution evidence for the correction workstream.

## Stage 1 — Website Product Pack

**Target:** v2.4.x  
**Status:** Completed

Deepen `references/products/website.md` for public-facing websites.

Scope:

- website subtype and visitor-job classification
- information architecture and navigation
- homepage and landing-page composition
- service/content/detail page patterns
- conversion and CTA hierarchy
- trust, proof, credibility, and contact UX
- forms and lead-generation UX
- content hierarchy and editorial scanning
- semantic HTML / SEO-aware information architecture
- breadcrumbs and internal linking
- responsive content behavior
- image/media behavior
- accessibility and WCAG-aware interaction
- performance UX and Core Web Vitals awareness
- motion and progressive enhancement
- multilingual / RTL website behavior
- privacy/consent and non-manipulative interaction
- website-specific QA matrix

Completion gate:

- Product Pack expanded
- website behavioral evals expanded
- release/product-route validators enforce critical website sections
- README/metadata remain concise

## Stage 2 — WordPress Plugin Product Pack

**Target:** v2.5.x  
**Status:** Completed

Deepen `references/products/wordpress-plugin.md`.

Scope:

- settings information architecture
- onboarding/setup wizard
- license/account surfaces
- API/integration connection UX
- diagnostics and site-health UX
- import/export
- background jobs
- destructive/reset/data-cleanup actions
- WordPress notices
- capability/role boundaries
- multisite/network-admin behavior
- native `wp-admin` vs application-like plugin UI
- Persian/RTL WordPress admin behavior
- plugin-specific QA matrix

## Stage 3 — Dashboard Product Pack

**Target:** v2.6.x  
**Status:** Completed

Re-audit and deepen dashboard rules while keeping one Dashboard Product Pack.

Internal dashboard modes to cover:

- executive
- analytical
- operational
- monitoring / NOC
- CRM / pipeline
- admin / management

Focus:

- decision hierarchy
- alerts/attention
- data trust
- table/work-queue behavior
- chart/question matching
- drill-down
- live-update behavior
- role-aware presentation
- saved views / personalization
- responsive dashboard architecture

## Stage 4 — Shared Product UI Rules

**Target:** v2.7.x  
**Status:** Completed

Extracted stable cross-product contracts into local Shared UI modules:

- navigation and wayfinding
- forms and data entry
- feedback and status
- state and recovery
- destructive and high-impact actions
- accessibility interaction
- responsive adaptation
- motion and transitions
- content hierarchy and progressive disclosure

The Product Pack remains authoritative for product/platform/host/domain specialization.

Shared Rules are loaded only when relevant to the task and cannot weaken accessibility, security, authorization, truthful-state, or user-data-integrity requirements.

## Stage 5 — Design System Hardening

**Target:** v2.8.x  
**Status:** Completed

Hardened the local Design System into a modular, machine-readable architecture:

- token foundations: primitive, semantic, component, product-variant, and resolved-runtime layers
- stable token naming/types, aliases/references, and DTCG 2025.10-compatible interchange
- semantic typography roles with Persian/Latin and mixed-script behavior
- semantic color roles with Light, Dark, High Contrast / Forced Colors contexts
- spacing, density, control sizing, radius, elevation, and layout foundations
- reusable component-state contracts
- responsive tokens and product variants without variant explosion
- design-system lifecycle, deprecation, migration, impact analysis, and visual-regression compatibility
- explicit runtime-configuration boundary

Design-system specialization remains subordinate to Product Pack semantics and Shared Product UI Rules.

## Stage 6 — Real-World Product Evaluation

**Target:** v3.0.0  
**Status:** Completed

Evaluated one representative production-like fixture for each primary Product Type:

1. Dashboard
2. Website
3. Web Application
4. Mobile Application
5. WordPress Plugin

Evaluation covered:

- product-route classification accuracy
- correct Product Pack/local-pack loading
- Shared Rule scope
- Design System module scope
- unnecessary-rule avoidance
- product-specific issue detection
- safety/authorization/data-integrity boundaries
- accessibility/responsive risk coverage
- evidence discipline and explicit validation limitations

Recorded result:

`evals/real-world/result.json`

Summary:

`evals/real-world/RESULTS.md`

The 2026-10-02 run was an in-session source-based behavioral evaluation using ChatGPT / GPT-5.6 Sol.

It did not independently execute a fresh Codex/Claude/browser/device run. Rendered/device validation limitations are explicitly recorded and are not represented as completed checks.

## Feature Freeze — 3.1.0 Stabilization

**Status:** Active

This is the baseline stabilization policy retained for the documentation-only roadmap publication. The agreed limited correction workstream above is planned but not executing. R0 must reconcile this policy, the README, and its validator when implementation is explicitly authorized; no new Product Types or external specialists are part of that exception.

The capability roadmap is complete and frozen for `3.1.0`.

Allowed work:

- deduplication of repeated or parallel instructions;
- context isolation and context reduction without removing product knowledge;
- improve Product Pack and local-module isolation;
- strengthen validation that prevents irrelevant knowledge loading;
- correct contradictions, stale documentation, or release metadata;
- improve tests, packaging, and release reliability.

Not planned during the freeze:

- new Product Types;
- new major capability families;
- additional external design specialists;
- speculative feature expansion.

`persian-writing` remains the only external specialist.

Any future capability expansion requires an explicit decision to lift the feature freeze rather than being added implicitly through maintenance work.
