# UI/UX Skill Roadmap

This is the repository's durable roadmap and stage-progress reference. It preserves the completed capability-building history and defines the agreed correction workstream for design discovery, a living product design handbook, visual approval, and configurable appearance.

Implementation was explicitly authorized after roadmap publication. The tracker distinguishes completed R0–R4 and planned R5–R8. R3/R4 completion covers their scoped fresh workflow observations, not customer approval or production readiness of a fictional demo. The owner's remaining-work goal separately authorizes passing merges and practical choices, but expressly prohibits a new release. Editing this document alone does not grant delivery authority.

## Current state

- Last updated: **2026-10-05**.
- Implementation baseline: **v3.1.1** at `16cfced8a166ab59eadfd7b38b899b046ba334f6`; local and live upstream `main` matched with a clean working tree at kickoff.
- Planning: **Complete**; the agreed requirements, stage outputs, dependencies, and acceptance gates are documented below.
- Implementation: **In progress**; **6 of 9 correction stages completed**.
- Active implementation stage: **R6**. R5 is accepted and integrated; R6 contract/preparation work has begun under one writer. Its runtime gallery, semantic selection, compatibility and rendered/lifecycle acceptance remain pending.
- Next implementation stage: **R7 — Language, direction, theme, and integrated quality**. Not started; final integrated gate follows R6. No maintainer taste choice for a fictional product is requested.
- Current authorized delivery: the owner requested remaining corrections, passing merges and practical defaults, with no new release. R0/R1 are integrated through PR #19; R2 through PR #20; earlier R3 contract through PR #21; corrected R3 through PR #22; R4 through PR #23; R5 through PR #24 at `61eacadece92e187434d72c5c58a9c44e55e2007`. R6 starts on local `codex/r6-editable-semantic-icons` from that clean matching main; its preparation is not pushed/merged. Version/tag/release assets stay unchanged; deployment and further installed-Skill changes remain separate.
- Dependency disposition: the [six-case R4 review](evals/samples/INCREMENTAL_FORWARD_REVIEW.md) records actual bounded forward execution, separate lead acceptance and shared-session limitations. No specialist was added or policy/test gate weakened; one writer and completed prerequisites remain enforced.
- Quality follow-up: [QF01–QF07](evals/samples/REMEDIATION_PLAN.md) preserve all historical evidence. QF01–QF03 and QF06/QF07 have bounded Verified outcomes; QF04/QF05 remain Unverified required R7 typography/native-confirmation obligations with explicit owner/reason/trigger, not waivers. The separately authorized installed Persian specialist update to 1.4.0 remains verified with its full prior backup. Source review, rendered save/refresh checks and current installation do not prove actual glyph-font/weight or completion-dialog branches. No additional external design specialist or other installation was performed.
- Product handbook filename: **`DESIGN.md`**, with this exact capitalization.
- Additional external specialists: **None planned**. The existing conditional `persian-writing` route remains.
- Historical Stages 1–6: **Completed as recorded**, with the Stage 6 source-based evaluation limitations preserved below.

The source baseline is an evidence snapshot, not a permanent version pin. Recheck the actual branch, source changes, and instructions at implementation kickoff.

### Correction stage tracker

This table is the canonical stage status. Task checkboxes below describe progress within a stage; checking tasks does not by itself establish stage acceptance.

| Stage | Deliverable | Status | Dependencies | Accountable role | Completed on | Acceptance evidence / PR |
| --- | --- | --- | --- | --- | --- | --- |
| R0 | Controlled kickoff, policy consistency, and ownership | Completed | Owner authorized kickoff; valid working checkout | Engineering lead / maintainer (single implementation writer) | 2026-10-04 | [R0 execution record](#r0-execution-record) |
| R1 | Adaptive discovery and professional recommendations | Completed | Locally accepted R0 | Current design role; engineering lead accepts; single writer | 2026-10-04 | [R1 execution record](#r1-execution-record) |
| R2 | Living `DESIGN.md` contract and profile migration | Completed | Integrated R1 | Current design role; one handbook writer | 2026-10-04 | [R2 execution record](#r2-execution-record) |
| R3 | Sequential product-aware samples and versioned approval | Completed | R1, R2 | Design role; product owner approves actual product designs | 2026-10-04 | [R3 independent forward review](evals/samples/SEQUENTIAL_FORWARD_REVIEW.md) |
| R4 | Incremental decisions and bounded agent handoffs | Completed | R2, R3; scoped continuation and separate lead review accepted | Engineering lead (single writer) | 2026-10-05 | [R4 forward review](evals/samples/INCREMENTAL_FORWARD_REVIEW.md) |
| R5 | Parametric appearance governance with real consumers | Completed | R2, integrated R4 | Engineering lead with design input | 2026-10-05 | [R5 delivery acceptance](#r5-delivery-acceptance--2026-10-05) |
| R6 | Editable semantic icons and icon families | In progress | Integrated R5 | Engineering lead with design input | Not completed | [R6 preparation](#r6-preparation--2026-10-05) |
| R7 | Integrated language, direction, theme, and visual quality | Not started | Contracts begin in R1/R3; final gate after R6 | Design role; engineering lead accepts | Not completed | Not recorded |
| R8 | Behavioral evaluation, package verification, release readiness | Not started | R0–R7 | Engineering lead / maintainer | Not completed | Not recorded |

Identify language, direction, accessibility and theme needs during discovery. Review one responsive primary-language/direction design first, using settled foundations; derive dark mode after primary approval; review secondary language/layout only after dark approval, confirmed need and owner authorization. Monolingual products need no extra locale sample. R7 integrates required approved contexts; define stage-relevant checks throughout, not only at R8.

### Mandatory progress-update protocol

1. Before starting an authorized stage, read this roadmap, the actual repository state, the applicable instructions, and the preceding stage's evidence. Update the active stage, owner, scope, date, and stage status to `In progress`.
2. During the stage, check only tasks actually performed. Record meaningful partial delivery, unresolved decisions, and concrete blockers. Do not mark the entire stage complete because its documents exist or a PR was opened.
3. At stage completion, record the changed paths, implementation commit or PR, relevant check commands and actual results, required visual/behavioral evidence, limitations, and the engineering lead's acceptance. Record product-owner approval only when it was really given.
4. Change the stage to `Completed` only when its exit criteria are satisfied. Set the completion date and evidence links, update the completed-stage count, and name the next executable stage or explicit approval gate.
5. Commit the meaningful roadmap update with the stage's authorized delivery. Keep it on the working branch until any required merge approval. A proposed PR must not be presented as already integrated into `main`.
6. If work cannot proceed, use `Blocked` with the concrete dependency, recovery action, and required decision. If a completed stage is invalidated by new evidence, use `Reopened` and explain the affected acceptance criteria. Preserve prior evidence rather than silently rewriting history.
7. Keep operational caches, temporary screenshots, tool state, and generated scan/test reports outside product source. Link durable test results or review artifacts that the project actually retains; never fabricate Issues, PRs, milestones, or checks.

Allowed stage states: `Not started`, `In progress`, `Blocked`, `Completed`, `Reopened`. A future stage is not blocked merely because its predecessor has not started. The active stage, tracker, checked tasks, completion evidence, and next action must agree before handoff.

At stage acceptance, retain a concise dated completion entry here or in its linked PR; the tracker must link to that real record. Do not require a second competing status document solely for this workstream.

## Principles

- Product design knowledge stays local to this repository.
- `persian-writing` remains the only external specialist unless explicitly changed later.
- Product Packs contain product-specific methodology.
- Shared rules should be extracted only when repetition becomes real and stable.
- Behavioral evals and release validation protect existing capabilities.
- Product routing should minimize context and keep inactive Product Packs unloaded.
- Prefer evidence-backed rules and current platform guidance over stylistic opinion.
- Outside the explicitly authorized R0–R8 correction exception, the feature freeze limits changes to deduplication, context isolation, correctness, validation, documentation, and release maintenance.

## Correction objective and boundaries

The Skill should guide a coherent process:

`Inspect product evidence -> Discover needs and preferences -> Recommend -> Build representative samples -> Approve a revision -> Maintain DESIGN.md -> Implement and validate configurable design`

The goal is a final interface that stays close to the product owner's intent and avoids avoidable redesign. It is not a guarantee of zero revisions, complete discovery of unknown future needs, or usability without testing.

This work improves the Skill's contracts, routing, reusable assets, and evaluations. It does not turn the Skill repository into a universal application/theme builder. Small representative executable fixtures may prove the contracts; production implementations must follow their own approved software scope and stack.

### Authorized limited exception to stabilization

The owner has explicitly authorized starting corrections. The exception is limited to **design foundation, the living handbook, visual approval, and safe parametric appearance management**. R0 reconciles the roadmap, README, and release-validation policy before later capability stages; this is not a general lifting of stabilization.

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
| F02 | One professional recommendation, rationale and focused corrections | R1 | A novice can accept, correct or explicitly delegate; alternatives are not mandatory |
| F03 | Image/reference intake, including likes and dislikes | R1 | Provenance and inference confidence are recorded |
| F04 | Early designs before full feature/backend implementation | R3 | Representative screens identify synthetic data and hypothetical capabilities |
| F05 | One foundation-aligned responsive primary proposal | R3 | Actual primary language/direction, settled palette/font/spacing and product-specific viewport priorities are applied before feedback and approval |
| F06 | Approval of a specific design revision | R3 | The selected sample, decision, and approval source are traceable |
| F07 | An initial and living product handbook named `DESIGN.md` | R2 | Another agent can use the canonical document without chat history |
| F08 | Incremental questions and recorded decisions during development | R4 | Only genuinely new or conflicting decisions are reopened |
| F09 | Strong recommendation to delegate substantial early design work to a bounded subagent | R0, R1, R4 | Lead ownership, limited handoff, and honest fallback are retained |
| F10 | No additional external design specialists | All | Existing specialist inventory is not expanded |
| F11 | Appearance settings belong in delivery for in-scope products with admin | R5 | The panel is an explicit product plan and acceptance item |
| F12 | Editable colors, fonts, sizes, spacing, borders, shadows, and component style | R5 | Valid changes reach their consumers and persist |
| F13 | Editable icon family and individual semantic icon assignments | R6 | Gallery, shared mapping, preview, and rollback work |
| F14 | Separate the handbook from active runtime configuration | R2, R5 | Routine admin changes need no manual handbook or code edit |
| F15 | Primary product language first; secondary language only when needed and authorized | R1, R3, R7 | Product language is not inferred from conversation; monolingual products avoid extra layouts |
| F16 | Support the product's LTR, RTL, and multilingual directions | R7 | Directional behavior and mixed-script content are verified |
| F17 | Dark review follows corrected primary approval | R3, R7 | Derive dark from the accepted baseline, receive corrections and scoped approval before any needed owner-authorized secondary review |
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

Task checkboxes record actual execution; unchecked tasks remain planned. They are not evidence that the requested capabilities already exist. Stage order describes dependencies, not separate mandatory approvals for every routine task. Reuse settled approvals; obtain fresh direction only for material new decisions or actions requiring additional authority.

### R0 — Controlled kickoff and consistent policy

Owner: engineering lead / maintainer. Prerequisites: explicit implementation-start instruction and a valid working checkout.

Tasks:

- [x] Recheck upstream source, applicable instructions, branch, local/upstream SHAs, dirty state, and protected user changes; record the implementation baseline.
- [x] Work on an authorized branch with the `codex/` prefix; preserve `main` and unrelated work.
- [x] Reconcile the limited correction exception with the roadmap and README while preserving completed historical stages and evaluation limitations.
- [x] Update the release validator's active-freeze contract to recognize the explicit limited exception without weakening Product Type isolation, historical-stage preservation, or the no-new-specialists boundary. The legacy freeze remains active outside the bounded exception.
- [x] Define full-foundation versus narrow-change routing, the admin-panel activation boundary, and audit/backend exclusions with distinguishable examples.
- [x] Define lead/subagent authority, a bounded early-design handoff, unavailable-tool fallback, and one-writer ownership.
- [x] Record acceptance criteria, stage-update responsibilities, and a later versioning decision; do not bump the version just to start the workstream.

Output: accepted implementation scope, consistent development policy, ownership/handoff contract, and actual baseline check results.

Exit: the implementation scope is authorized; policy documents and validators no longer contradict the correction exception; mandatory admin delivery and narrow-task non-expansion are distinguishable; no new specialist, stack, or agent permission is invented. Attach the reviewed diff, baseline results, and accepting lead decision before marking R0 complete.

### R0 execution record

- Started: 2026-10-04, after the owner's explicit "start" instruction.
- Engineering lead and sole implementation writer: the current coding agent. No subagent was started.
- Branch: `codex/r0-controlled-kickoff`; baseline `16cfced8a166ab59eadfd7b38b899b046ba334f6`.
- Plan: reconcile repository policy and validation first; align the existing activation/handoff references without implementing later stages; add focused policy regressions; run protected baseline checks; review the diff and record acceptance.
- Scope: `README.md`, `ROADMAP.md`, `CHANGELOG.md`, the existing Head/discovery/runtime/audit/specialist references, release-policy validation and its regression tests, and the shared CI validation step. No product UI, registries, dependencies, versions, or release automation changes.
- Acceptance: the limited exception is explicit and bounded; full/narrow/no-admin/audit/backend examples are distinguishable; lead authority and one-writer handoff are clear; inconsistent policy/progress is rejected; protected validators pass and the reviewed diff remains inside this scope.
- Baseline: all eight repository validators passed before edits; existing evaluation results are structural/source-based evidence only. Live upstream still points to the baseline above.
- Accepted locally: 2026-10-04 by the current engineering lead, after reviewing the scoped diff against the acceptance criteria. This is engineering acceptance of R0, not owner approval of a visual design or release.
- Implementation commit: `805a1d50e2e541764435bd1d054c7e2d691cecb9`. The subsequent roadmap-only commit records acceptance; its identity is retained in Git history rather than invented before commit creation.
- Changed paths: `README.md`, `ROADMAP.md`, `CHANGELOG.md`, `skills/ui-ux-skill/SKILL.md`, `references/discovery-and-profile.md`, `references/runtime-ui-governance.md`, `references/existing-product-audit.md`, `references/specialist-routing.md`, `scripts/validate_release.py`, `scripts/roadmap_policy.py`, `scripts/test_roadmap_policy.py`, `.github/workflows/validate-skill.yml`. Short reference paths are relative to the canonical Skill folder.
- Checks: `python -B -X utf8 scripts/test_roadmap_policy.py` passed 11 tests, including bounded-scope rejection, preserved history/limitations, valid completion, missing evidence, invalid/missing/duplicate stages, out-of-order completion, counter/active/next-stage mismatch. The eight commands under Existing verification to preserve all exited zero; eval checks validate recorded structure, not fresh model/browser behavior.
- Package evidence: isolated local archives passed CRC and SHA256 checks; all 71 canonical Skill files matched source bytes in both packages and version metadata remained `3.1.1`. Operational outputs stay outside the repository; these are unreleased verification artifacts, not a new public release or installation.
- Review: one activation contract is routed by the Head/runtime/audit references; the same-Skill handoff preserves lead acceptance and one writer. Historical stages/limitations and product/specialist registries are unchanged. Impact was checked directly through source, references, validators, and packaging; no generated Graphify evidence is claimed.
- Limitations: the official local quick validator could not import `yaml` (`PyYAML` unavailable); no dependency was installed. The existing release validator checked the unchanged frontmatter schema/Thin Head contract. Official CI validation remains pending a separately authorized push/PR; R0 acceptance does not waive the later candidate/release gate. No independent agent, rendered UI, or device evaluation is claimed or required for this policy-only stage.
- Repository purity: no forbidden tracked/staged artifacts; the tool reported a warning for an unconfigured optional local Git-exclude block. No repository/host exclusion settings were changed.
- Delivery: local only. No new PR, Issue, milestone, release, deployment, or installation has been created; no merge is authorized.

### R1 — Adaptive discovery and designer recommendations

Owner: design role within the lead's boundary. Prerequisite: R0.

Tasks:

- [x] Inspect existing product documents, assets, interfaces, decisions, and stack before asking the user.
- [x] Extract product type, audience/roles, principal jobs and workflows, breadth, approved sections/features, and practical constraints; separate UX needs from visual preferences.
- [x] Record the default language, supported languages, direction per language, and localization requirements explicitly. A Persian conversation can describe an English product.
- [x] Use a short, product-relevant question sequence rather than a fixed exhaustive questionnaire. Let the user answer, attach references, select a proposal, or explicitly delegate a choice.
- [x] For key decisions, always give a primary professional recommendation, product/audience rationale, and limited alternatives, with room for a custom preference.
- [x] Cover relevant palette, typography roles/sizes, style, spacing/density, borders, controls, charts/diagrams, icons, effects/motion, responsive behavior, accessibility, and light/dark preferences; do not ask about irrelevant features.
- [x] Accept screenshots/images and verbal references; record what the user likes and dislikes, provenance, confidence, and observed versus inferred properties. Do not claim exact font, motion, spacing, or interaction from an ambiguous static image.
- [x] Treat silence as unresolved, not approval. Distinguish user choice, explicit delegation, an agent proposal, and protected product constraints.
- [x] Resolve most foundation decisions early and leave genuinely unknown details open for the appropriate development stage; do not invent capabilities or roles to fill a form.

Output: initial design brief, evidence-backed recommendations, preferences/constraints, assumptions, and a focused open-question list.

Exit: both a design novice and an experienced owner can make progress; known information is not reasked; recommendations fit the actual product; reference images are not treated as permission to copy identity/assets or expand functionality. Attach representative discovery transcripts/evaluation results before acceptance.

### R1 execution record

- Started: 2026-10-04 after the owner's instruction to proceed to the next stage; accepted R0 baseline `228d9fa8de5db3ea31b24df590db8eba1645c951` on `codex/r0-controlled-kickoff`. The working tree was clean; live upstream `main` remained `16cfced8a166ab59eadfd7b38b899b046ba334f6`.
- Owner/writer: current coding agent acting as the bounded design role; the same agent retains engineering acceptance. No subagent or new external specialist is authorized or used.
- Plan/scope: extend the existing discovery reference and its thin Head entry; add raw synthetic discovery inputs, focused eval cases, and explicitly labeled source-based walkthroughs; run fixture/preparation/policy/protected validation and inspect package consumption; repair a progress-test assumption exposed by the R1 dependency wording; review and record acceptance. No product build, handbook migration/template, visual directions, runtime panel, dependency, registry, or version changes.
- Acceptance: inspect before asking; reuse settled/protected decisions; adapt to product jobs, breadth and sections; record actual product languages/directions; give understandable recommendation/rationale/alternatives/custom/delegation; distinguish proposals, approval and silence; bound image inference; stop when enough is known for representative samples and retain focused unknowns.
- Accepted locally: 2026-10-04 by the current engineering lead after reviewing the instruction changes and illustrative brief/choice records against this stage's criteria. Task completion describes the delivered discovery workflow, not an actual customer's design approval or independently measured model compliance.
- Implementation commit: `e7aabc4def83af8dce14b65d816ed64150fd2d4c`. The subsequent roadmap-only commit records acceptance; its identity is retained in Git history.
- Changed paths: the existing Head and `references/discovery-and-profile.md`; `evals/cases.json`, `evals/README.md`, the raw `evals/fixtures/discovery-brief/` inputs, and `evals/discovery/WALKTHROUGHS.md`; `scripts/validate_eval_fixtures.py`, `scripts/test_roadmap_policy.py`, `CHANGELOG.md`, and this roadmap. Short reference paths are relative to the canonical Skill folder. No competing discovery module was created.
- Discovery evidence: [eight synthetic walkthroughs](evals/discovery/WALKTHROUGHS.md) cover novice/experienced owners, reference uncertainty, a missing image, Persian conversation with an English product, explicit bilingual scope, partial delegation, and a narrow assessment. They are current-session authored and source-reviewed examples, not real owner interviews, fresh-agent tests, rendered inspections, usability findings, or preference-fit proof. Raw inputs remain separate from those illustrative responses. Independent conformance remains pending for later authorized evaluation/R8.
- Checks: all eight existing validation commands exited zero; 11 roadmap-policy regression tests passed. Fixture validation covers 63 cases and 11 fixture directories structurally. All eight new discovery cases were prepared in isolated copies with exact manifest prompts and byte-matching raw artifacts; the copies exclude the walkthrough responses. Preparation is not model execution. Existing five-product Stage 6 records were revalidated structurally, not rerun as fresh R1 behavior tests.
- Regression repair: the invalid-status test had depended on R1's human-readable dependency wording. It now mutates the actual status cell, retaining the same policy rejection and avoiding a whole-document assertion dump. The production roadmap-policy validator was not relaxed.
- Package evidence: both isolated archives passed CRC and SHA256 checks, with all 71 canonical Skill files matching current source bytes and embedded versions unchanged at `3.1.1`. These are unreleased verification artifacts outside the repository; no release or installed-Skill update occurred.
- Review: the Head still routes to the existing discovery reference; known decisions, approval provenance, product-language independence, light/dark planning, bounded reference inference, and focused stopping conditions are explicit. Later handbook/template, visual-approval and runtime capabilities remain unimplemented. Impact was checked directly through source, references, validators, and packaging; no generated Graphify evidence is claimed. The Persian illustrative prose passed local lint with zero issues; mechanical cleanup was inspected on an external copy and did not substitute product-language/rendered validation.
- Limitations: the official local quick validator still cannot import `yaml` because `PyYAML` is unavailable; no dependency was installed. Official CI for this branch remains pending a separately authorized push/PR. Source review and fixture preparation do not waive independent behavioral, rendered-language, font, preference-fit, or final candidate gates.
- Repository purity: no forbidden tracked/staged artifacts; only the existing optional local Git-exclude configuration warning. No host or exclusion settings were changed.
- Delivery: local branch only; no push, PR, Issue, milestone, merge, release, deployment, or installation.

### R2 — Living `DESIGN.md` and compatible migration

Owner: one assigned handbook writer. Prerequisite: R1.

Tasks:

- [x] Define the canonical product handbook as `DESIGN.md`, with this exact capitalization, and record its location in the product's working contract.
- [x] Provide a usable initial template early, not only a document written after implementation is finished.
- [x] Link requirements to workflows, screens, components, states, and verification methods; cover UX structure as well as visual styling.
- [x] Track proposed, approved, and open decisions with their real approval/delegation source, revision, and relevant sample.
- [x] Define one canonical handbook and one writer; preserve enough context for another agent to continue without chat history.
- [x] Migrate valid `design-profile.md` or other established design documentation into the canonical handbook compatibly. Inspect consumers before renaming/removing anything; preserve provenance and references.
- [x] Avoid two independent approved documents or duplicated canonical token values. Preserve an old document as an explicit compatibility reference only when required, with the new authority clear.
- [x] Keep runtime token values/configuration in their real implementation sources. The handbook defines approved roles, initial defaults, policies, allowed controls, and links to those sources.
- [x] Do not require manual handbook edits for every routine admin setting change. Active configuration comes from product storage and version history.

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

### R0/R1 integration checkpoint

- Owner authorization: merge and proceed to the next stage, 2026-10-04. Earlier local-only notes above are historical checkpoints, not the current integration state.
- [PR #19](https://github.com/pooyahayati/UI-UX-Skill/pull/19) merged with exact reviewed head `94d09795e603154331518e8de5711339465f39cc`; merge commit `336a50ba3db54e2c8b05d82e4cf087098ae1c0a7`. Local `main` was fast-forwarded to the same live `origin/main` before the R2 branch was created.
- [CI run](https://github.com/pooyahayati/UI-UX-Skill/actions/runs/37194969743) succeeded for that PR head, including official quick validation and package checks. The installer smoke step was skipped by the existing event condition; no host installation or release occurred. This closes the R0/R1 CI gap, not their independent behavioral/rendered evidence limitations.
- [Post-merge workflow](https://github.com/pooyahayati/UI-UX-Skill/actions/runs/37195042407) also succeeded at the exact merge commit, including official quick validation and the CI installer smoke test. The publication step was skipped because `v3.1.1` already exists; that public release still targets `d2420e9c60230fb2a667dff971f60a8bbbaaa1de`. No new release or local host installation was made.

### R2 execution record

- Started: 2026-10-04 from the verified merge commit above, with a clean working tree on `codex/r2-living-design-handbook`. One implementation/handbook writer; no subagent or external specialist added.
- Plan/spec: add one routed lifecycle/migration reference and a reusable draft template; replace the competing legacy schema instructions with that route; reconcile existing audit, specialist, design-system and privacy consumers; supply raw legacy/conflict inputs and an inspectable before/after migration example; validate links, fixture preparation, regressions and exact packages; review and record acceptance. No actual product migration, runtime configuration, visual samples, dependencies, registries or version changes.
- Acceptance: exact canonical `DESIGN.md` path and single writer; early draft with product/UX/foundation/language/theme coverage; scoped decision/sample/evidence provenance; resumable without chat history; compatible migration preserving valid decisions and inspected consumers without silent overwrite or deletion; actual token/storage authorities remain outside the handbook. The roadmap is the retained stage plan, not a duplicate operational plan.
- Impact/risk: instruction/output-document compatibility across routed resources and packaging; no customer data, application schema or production configuration is migrated. Source/reference/fixture/package impact is inspected directly instead of claiming a generated Graphify graph. Independent model behavior remains unverified unless actually evaluated.
- Accepted locally: 2026-10-04 by the current engineering lead after source/template/example review and the checks below. Task completion means the instruction/template/migration contract is delivered, not that a real product was migrated or its owner approved a design. A fresh independent agent was not run; resumability was assessed from the self-contained example's path, states, sources, constraints and next actions, not measured as model conformance.
- Implementation commit: `f98cef40a089339f35db7c65de336aeb90942669`. The following roadmap-only commit records acceptance; its identity is retained in Git history.
- Delivered resources: [handbook contract](skills/ui-ux-skill/references/design-handbook.md), [early draft template](skills/ui-ux-skill/assets/templates/DESIGN.md), [raw legacy inputs](evals/fixtures/legacy-handbook/README.md) and [after-handbook example](evals/handbook/example/DESIGN.md). The Head and existing discovery/audit/specialist/token-foundation consumers route to the same contract; the old duplicate profile schema instructions were removed. `PRIVACY.md` describes the local filename/scope without changing application data ownership. Registry identifiers and versions remain unchanged.
- Migration evidence: four concrete `scripts/test_handbook_migration.py` tests passed: the supplied legacy parser keeps its accepted payload; a pointer-only replacement is correctly rejected; token/owner-source bytes remain unchanged; after-document links resolve. Only isolated copies of the synthetic fixture are transformed. The retained old file is an explicit read-only projection tied to revision 1/D1, not a second editable authority. The conflicted variant and missing visual/runtime proof remain explicit.
- Forward inputs: four `handbook-*` cases were added, structurally validated and prepared with exact prompts and byte-matching raw inputs (67 total cases, 12 fixture directories). The after-example is excluded from those raw inputs; no model ran. Existing five-product Stage 6 records were only revalidated structurally, not rerun as correction behavior.
- Checks: 11 roadmap-policy regressions and all eight existing validators passed; routed handbook/template links resolve inside the portable Skill. CI now includes the synthetic consumer regression, but R2 has not been pushed, so its remote CI is pending. Windows restricted execution denied access inside temporary directories; the unchanged four-test suite passed with authorized elevated execution in an external workspace temp directory. This is an environment limitation, not a suppressed test failure.
- Package evidence: two isolated archives passed CRC/SHA256, exact membership and byte matching for all 73 canonical Skill files, including the routed contract/template. Embedded versions remain `3.1.1`; these external verification artifacts do not replace the public release or installed Skill.
- Limitations: no independent model, real owner approval, product UI/rendered languages/themes/fonts, runtime panel or arbitrary product-parser migration is claimed. The local official quick validator remains unavailable without `PyYAML`; R0/R1 CI success does not validate unpublished R2. Required candidate behavioral/visual/runtime gates remain pending for their authorized stages.
- Repository purity: no forbidden tracked/staged artifacts; the existing optional local Git-exclude warning remains. No dependencies, host tools, local exclusion policy or installed skills were changed. No R2 PR, Issue or milestone was created; delivery is local only.

### R2 integration checkpoint

- Owner authorization: merge and proceed to R3, 2026-10-04. Earlier R2 local-only notes are historical checkpoints.
- [PR #20](https://github.com/pooyahayati/UI-UX-Skill/pull/20) merged at exact reviewed head `63d5f43cfdd17d9bc4cba6948ff792917ef0ed1d`; merge commit `b487880a18e095d4e01569c975393b685fad433e`. Local `main` was fast-forwarded to matching `origin/main` before the R3 branch was created.
- [PR validation](https://github.com/pooyahayati/UI-UX-Skill/actions/runs/37196913773) passed for that head, including official quick validation and synthetic migration tests. The event-conditioned installer smoke step was skipped. This closes R2's remote validation gap, not its independent model/rendered/customer-approval limitations.
- [Post-merge workflow](https://github.com/pooyahayati/UI-UX-Skill/actions/runs/37196971332) succeeded for the merge commit, including official quick validation and ephemeral CI installer smoke. Publication was skipped because the existing `v3.1.1` release still targets `d2420e9c60230fb2a667dff971f60a8bbbaaa1de`; no new release or local host installation occurred.

### R3 execution record

- Started: 2026-10-04 from R2 merge `b487880a18e095d4e01569c975393b685fad433e`, clean branch `codex/r3-visual-directions-approval`. The current coding agent remains the sole implementation writer; no subagent was started.
- Initial plan (historical, superseded by the owner-corrected checkpoint below): implement comparable samples, simultaneous theme/locale coverage and revision-scoped approval, with raw forward inputs and an authored executable example.
- Protected scope: no new Product Types/specialists, stack/framework mandate, runtime panel, feature expansion, version bump, release or host installation. Sample selection, scoped visual approval and broad implementation authorization must remain distinct.
- Current acceptance: R3's exit below evaluates sequential gates and evidence separation. Actual products require executable responsive evidence, revision-matched handbook and real scoped approvals; Skill maintenance does not require this maintainer to approve a fictional product's style. Instruction/fixture completion alone is not independent conformance.
- Preflight: engineering Skill `v1.3.1` verified current without installation/update. Instruction-maintenance selection is empty; the source Skill is the artifact being maintained, not an installed candidate execution. Router signals from unrelated existing browser/PHP/WordPress evaluation fixtures do not establish a product/platform for this work. The active correction requirements and relevant roadmap sections were inspected directly; no Graphify output is claimed.
- Initial contract checkpoint (historical): the conditional [sample/approval workflow](skills/ui-ux-skill/references/design-foundation-workflow.md), Head/discovery/handbook routes and existing `DESIGN.md` output template were implemented. Six `samples-*` forward cases use [raw sample-review inputs](evals/fixtures/sample-review/README.md), with initial-comparison notes inactive and the bilingual variant explicitly opt-in. No authored after-answer or rendered sample is supplied as input.
- Accepted partial slice (historical): the current engineering lead reviewed instruction routing, scope, selection/approval/rollout separation, pending-revision handling, actual-language/theme obligations and raw-input isolation. This accepted the contract/preparation change, not the R3 stage exit or a product design. Executable sample, fresh model evaluation and owner design approval were absent at that checkpoint; the subsequent evidence below does not fabricate the latter two.
- Checks: eight protected repository validators and 11 roadmap-policy regressions passed. Two new preparation tests passed (all six cases receive exact raw files and prompts; an existing run's review evidence is preserved on refusal), plus all four prior synthetic migration tests. The temporary-directory tests ran with authorized elevated Windows access; no production data or host installation was touched. All eight local links across the conditional references/template resolve inside the portable Skill.
- Fixture coverage: 73 total cases across 13 raw fixture directories. These are structurally validated and prepared input definitions, not 73 executed model outcomes. Historical Stage 6 results were revalidated structurally, not rerun. CI includes the preparation regression but has not run for this unpublished R3 branch. Official quick validation is separately unavailable locally without `PyYAML`; R2 CI does not validate R3.
- Candidate packages: after LF normalization of touched text, both external verification archives passed CRC/SHA256, exact membership and byte matching for 74 portable Skill files, including the new conditional workflow. Versions remain `3.1.1`; these are test packages, not a publication or installed-Skill update. Raw bilingual input passed the Persian prose lint with zero findings.
- Repository purity: no forbidden tracked/staged artifacts; the pre-existing optional local-exclude warning remains and no exclude configuration was changed. R3 is a local partial delivery, not pushed/merged; no R3 PR, Issue or milestone was created. Generated archives and test/preflight state stay outside source control.
- Initial next slice (historical): generate comparable visible directions, then exercise a selected executable sample and revision-matched handbook. Any sample selection/approval needs a real scoped source; fictional fixture records cannot stand in for approval by this repository's owner.

### R3 contract integration checkpoint

- Owner authorization: merge the existing partial slice and continue, 2026-10-04. The earlier unpublished/local-only observations above are historical, not current integration status.
- [PR #21](https://github.com/pooyahayati/UI-UX-Skill/pull/21) merged at exact reviewed head `02d728d80909fa94b04c9e572308ba9206549375`; merge commit `b069bd16e1170028fd987af804197d2d3732f752`. Local `main` fast-forwarded to matching `origin/main` before `codex/r3-executable-samples` was created.
- [PR validation](https://github.com/pooyahayati/UI-UX-Skill/actions/runs/37198262273) succeeded at that head. [Post-merge workflow](https://github.com/pooyahayati/UI-UX-Skill/actions/runs/37198320035) succeeded at the merge commit, including official quick validation and ephemeral CI installer smoke. Publication was skipped because `v3.1.1` already exists at `d2420e9c60230fb2a667dff971f60a8bbbaaa1de`; no new release or host installation occurred.

### R3 authored executable checkpoint

- Built [Dispatch Notes](evals/samples/dispatch-notes/README.md), an explicitly authored output outside raw fixtures and the portable Skill package. The original raw inputs remain unchanged; this is not a fresh independent model result or fictional product-owner approval.
- Two equivalent workflow directions (A structured / B field notebook), real local licensed Regular/Bold font files, actual English/LTR default and explicitly supported Persian/RTL, both themes, long instructions and mixed IDs. List/detail/note/result were chosen for the technician's actual brief job rather than inventing a login/dashboard. Synthetic saves/completion are tab-only simulations; no backend, new role, admin panel or framework was added.
- Draft sample/handbook identity: **r1/h1**. [DESIGN.md](evals/samples/dispatch-notes/DESIGN.md), allowlisted review metadata and [QA.md](evals/samples/dispatch-notes/QA.md) record proposals, evidence, limitations and unresolved approvals. Review controls and code tokens do not establish admin runtime configurability.
- Current installed UI `3.1.1` compatibility assessment passed after direct whole-guidance review by the head; it does not mean the candidate was installed. Active product guidance is web-application only; unrelated Product Packs stayed inactive. Existing Persian/input-safety guidance was used without adding specialists or spawning agents.
- Actual isolated browser evidence: 28 assertions passed for busy/failure/retry, exact note preservation, language/theme changes, list/detail navigation, loading/empty/access simulations, validation, keyboard completion, literal markup and reload reset. Narrow/intermediate RTL and four semantic text palettes were checked. Native comparison boards were displayed; top-level RTL full-page captures exhibited a capture-tool clipping limitation, explicitly recorded rather than passed off as trustworthy full-page evidence.
- Local checks: 20 regression/integrity tests (11 policy, four migration, two raw-preparation, three authored-assets) and all eight protected validators passed. JavaScript syntax and extracted Persian copy lint passed. Static CI tests protect assets/revisions/input isolation only; this unpublished slice has no remote CI result and does not replay browser or model actions. Historical eval results were only structurally revalidated.
- Both candidate archives passed CRC/SHA256, exact membership and source-byte matching: 74 portable Skill files, 74 standalone entries / 81 plugin entries. Version remains `3.1.1`; authored sample/font/evidence output is excluded. All 28 local roadmap/sample document links and external source-binding hashes resolved/matched. No Issue, milestone, new PR, release, deployment, host update or Graphify result is claimed for this local slice.
- Historical proposed gate (superseded): maintainer benchmark direction selection was requested. The owner corrected this workflow below; selecting the fictional example is not a prerequisite for Skill development. No product approval or broad rollout authority is inferred from this correction.

### R3 owner-corrected sequential checkpoint — 2026-10-04

- Owner correction: one professional responsive proposal in the primary product language/direction, applying already settled palette, font, spacing and related foundations. Receive corrections and scoped primary approval; then derive/review/approve dark mode; only then confirm need and obtain named authorization for secondary language/layout. No unnecessary variants for a monolingual product.
- Updated canonical workflow, thin Head routes, discovery, handbook, template and phase-relevant QA. Recorded phase prerequisites, foundation sources, feedback/revisions, dependent baselines and separate approvals. Existing admin appearance/icon requirements, production themes/locales, permissions and software feature scope are unchanged.
- Revised raw sample inputs with explicit settled foundations and nine sequential sample scenarios (76 total cases, 13 fixture directories). Fictional phase records activate only in their named cases; they are neither current renders nor real customer approval. Raw preparation must preserve exact inputs and refuse overwriting prior run evidence.
- The earlier authored A/B bilingual/two-theme example remains historical output, not evidence of the revised sequence or an answer key. No new product UI or browser rendering is claimed by this instruction-only correction. Independent model evaluation remains outstanding; R3 stays `In progress`, 3 of 9 stages completed, and R4 is not started.
- Verification: all 20 local regression/integrity tests and eight protected validators passed. Nine prepared sample cases preserve exact raw files/prompts and prior run evidence; 76 cases across 13 fixtures are definitions, not executed model outcomes. All 27 local links in touched documents resolve; LF/source diff checks pass. Both test archives match all 74 portable Skill files by bytes, CRC/SHA256 and version `3.1.1`; authored samples/raw fixtures are excluded.
- Local delivery only on `codex/r3-executable-samples`; no branch upstream or associated PR. Live GitHub main remains `b069bd16e1170028fd987af804197d2d3732f752`. Older PR #21 CI results do not validate this correction; official quick validation is unavailable locally because `PyYAML` is absent. No dependency was installed. No push, merge, new Issue/milestone, release, deployment, installed-Skill change, independent review/model run or Graphify result is claimed.

### R3 — Sequential proposal, representative prototype, and approval

Owner: design role; product owner approves the design revision. Prerequisites: R1, R2.

Tasks:

- [x] Select representative screens from important audience workflows and explain the choice; do not always choose login/dashboard screens regardless of product.
- [x] Define one primary professional proposal using settled palette/font/spacing and other foundation sources; no mandatory competing designs.
- [x] Define primary-language/direction/theme review with product-specific responsive viewport priorities, focused corrections and exact revision approval.
- [x] Define derived dark review after primary approval, retaining accepted foundations and receiving its own corrections/approval.
- [x] Define secondary review only after dark approval, confirmed product need and named owner authorization; monolingual extra layouts are not required.
- [x] Build early samples without waiting for the full backend or all features. Clearly mark synthetic data and hypothetical capabilities; approving their appearance does not add them to software scope.
- [x] Use conceptual images when useful for selecting direction, but prove real typography, direction, layout, and behavior with an executable sample before claiming those qualities validated.
- [x] Observe candidate agent behavior on fresh raw sequential scenarios, including refusing premature dark/localized work and preserving settled foundation values.
- [x] Inspect generated executable samples at relevant responsive sizes/states; record actual evidence or unavailable checks without substituting old authored rendering.
- [x] Exercise feedback, exact sample/handbook approval and dependent-revision invalidation without inventing customer approvals or extending scope.

Output: sequential review instructions and honest evaluation evidence; in a real product, corrected primary sample, derived dark sample, any authorized secondary sample, scoped handbook baselines and actual coverage/limitations.

Checked contract items have source evidence plus the targeted [independent forward review](evals/samples/SEQUENTIAL_FORWARD_REVIEW.md). The older authored example remains historical only. R3 acceptance concerns observed Skill behavior; new demo revisions remain draft with scoped visual corrections and unverified checks. A maintainer accepting Skill changes need not approve an unrelated demonstration design.

Exit: fresh candidate observations demonstrate the sequential boundaries, settled-foundation reuse, responsive product-fit and honest missing checks. Actual product handoffs require matching sample/handbook revisions and real scoped approvals for each applicable phase; primary approval does not approve dark or secondary samples. Attach concrete evidence and limits. Structural/source checks alone cannot substitute for model/rendered observations; fictional notes are scenario inputs, not customer approval.

### R3 corrected-slice integration checkpoint

- Owner authorization: merge and proceed, 2026-10-04. Earlier unpublished/local-only notes describe their historical checkpoints, not current R3 integration status.
- [PR #22](https://github.com/pooyahayati/UI-UX-Skill/pull/22) merged at reviewed head `fd0bbc59557a94327e023c8938be7cf696b0383f`; merge commit `ddb4b1b5fb7fc06644a450b738359cf04db6616c`. Local main fast-forwarded to matching origin/main before the R4 branch was created.
- [PR CI](https://github.com/pooyahayati/UI-UX-Skill/actions/runs/37204221329) succeeded at the exact head. [Post-merge workflow](https://github.com/pooyahayati/UI-UX-Skill/actions/runs/37204282987) succeeded at the merge, including official quick validation and ephemeral CI installer smoke. Publish release was skipped; no new release, version bump or host installation.
- Direct OAuth push lacked workflow-file scope; the already configured GitHub connection published the exact uploaded reviewed commit and merged after green checks. No workflow step, approval gate or token permission was removed/weakened. No new connection or credential scope was requested.
- Merge accepts this source slice, not fresh candidate conformance or a fictional customer design. R3 remains In progress with its recorded evaluation gap.

### R4 execution record

Formal advancement checkpoint — 2026-10-04: after explicitly authorized independent R3 observations and root review, R3's workflow prerequisite is accepted and R4 is In progress. Nine raw scenarios/46 scoped invariants were reviewed; four generated previews were rendered with additional root responsive/action observations. All raw inputs stayed unchanged. Prototype border contrast, free-text identifier wrapping, some clipped RTL captures, actual fonts and other unverified product checks remain explicit, not synthetic success. See [the portable review](evals/samples/SEQUENTIAL_FORWARD_REVIEW.md). The preparation bullets below describe the earlier checkpoint; fresh R4 continuation behavior is still outstanding. No additional specialist, R4 agent/model outcome, push, merge or release is claimed.

- Preparation started 2026-10-04 from R3 merge `ddb4b1b5fb7fc06644a450b738359cf04db6616c`, clean `codex/r4-incremental-design-handoffs`, one implementation writer. Formal R4 is Not started pending the open R3 behavioral gate; this requested preparation does not fabricate acceptance of that prerequisite.
- Scope: one [incremental decision reference](skills/ui-ux-skill/references/incremental-design-decisions.md), thin Head/handbook/handoff/template routes, five raw continuation cases, extended exact-input preparation coverage and a separate [authored continuation source review](evals/incremental/WALKTHROUGH.md). No Product Pack, registry, runtime panel, product UI, feature/role, dependency, version or installed-Skill change.
- Preflight: current engineering Skill 1.3.1, no selected specialists or installation; first freshness connection failed transiently, bounded retry passed. Tier 1 instruction/input maintenance crosses skills/evals, with an external retained plan. Unrelated fixture PHP/WordPress/browser markers do not establish this task's platform; relevant roadmap regions inspected directly despite scanner truncation. No agent/independent review or Graphify output is claimed.
- Source-review acceptance: new near-limit character feedback uses an approved job and scoped fictional delegation, retains h7 foundations/token authority and requests no duplicate palette/font/density interview. It proposes only the affected h8 delta, planned checks and remaining approval; no current render or actual customer authority is fabricated. This illustrative source review is not a fresh agent outcome or full R4 acceptance.
- Verification/local delivery: initial policy runs rejected premature R4 advancement and multiple active statuses; the single-active-stage tracker is corrected without changing policy/tests. Final 20 local tests and eight protected validators pass. Exact-input tests cover nine sample/five continuation cases, preserve both raw directories byte-for-byte and refuse overwriting run evidence. 81 case definitions/14 fixtures are structurally valid, not fresh executed model outcomes. All 25 local links in touched documents resolve; normalized LF/diff checks pass. Both external test archives match all 75 portable Skill files by bytes, CRC/SHA256 and unchanged version 3.1.1.
- Delivery limits: local R4 preparation is not pushed/merged and has no PR, Issue or milestone. R3's remote CI does not validate it; official quick validation is locally unavailable without PyYAML, no dependency installed. No fresh candidate/rendered/product-runtime evidence, independent agent or Graphify result claimed. Recovery: obtain fresh candidate sequential observations for R3, then formally enter R4 and evaluate continuation behavior; independent delegation still requires authorization. Completed-stage count unchanged.

### Design evidence remediation follow-up

Current checkpoint — 2026-10-05: QF06 exact positive input and QF07 affected regressions/continuation reconciliation are Verified within their stated scope; see [the latest remediation checkpoint](evals/samples/REMEDIATION_PLAN.md#qf06qf07-and-scoped-r4-acceptance-checkpoint--2026-10-05). R4 is locally accepted by the engineering lead after six actual forward cases. QF04/QF05 remain required R7 evidence obligations, not passes; full-candidate R8 and integration remain pending. The paragraphs below preserve earlier checkpoint scope and do not override the current tracker.

Owner: engineering lead / maintainer, single writer. Planning completed 2026-10-04 at local source `c0a2ac273d800db451ee7eaf9e981483c5f26e75`; the owner's subsequent continuation request authorized execution. QF01 is Verified by lead review of reproduced full-page capture mismatches, inspected viewport/scrolled replacements and affected local checks. Its [execution checkpoint](evals/samples/REMEDIATION_PLAN.md#qf01-execution-checkpoint--2026-10-04) preserves unknown internal/historical causes and validation limits. See the [detailed plan and task tracker](evals/samples/REMEDIATION_PLAN.md), derived from the preserved [R3 forward review](evals/samples/SEQUENTIAL_FORWARD_REVIEW.md).

- QF01 establishes reliable capture evidence before assigning a layout cause to clipped RTL rasters.
- QF02 addresses the applicable essential-field border contrast with the smallest authorized semantic correction; QF03 assesses mixed-script free-text readability without rewriting user data or treating all wrapping as a defect.
- QF04–QF06 cover actual font resolution, explicit completion cancel/confirm observations and executable exact prior baselines. QF04/QF05 have a [current attempted-execution checkpoint](evals/samples/REMEDIATION_PLAN.md#qf04-and-qf05-execution-checkpoint--2026-10-04) with unmet evidence retained, not passes. Missing real-device, backend and local validator evidence remains classified by scope/tooling, not mislabeled as a confirmed product bug.
- QF07 runs affected regressions and reconciles fresh forward/continuation evidence when authorized. Existing R3 workflow acceptance remains scoped; R4 continuation/handoff acceptance is still outstanding. These follow-ups do not start R5, R7 or R8, and their plan is not a new evaluation result.

The earlier planning slice changed only this roadmap and the remediation plan. QF01 adds a bounded capture-validity check to the existing visual-regression reference and a QA pointer; unchanged sample sources and historical rasters are reviewed, not edited. QF02 adds a linked foundation-conflict check and an external isolated proposed note-border correction; resolved-color measurements, phone/intermediate captures and unchanged-script/source checks support its [bounded execution acceptance](evals/samples/REMEDIATION_PLAN.md#qf02-execution-checkpoint--2026-10-04), not actual customer approval or fresh model conformance. QF03 adds a free-text-specific direction clarification; fresh renders, actual copy/paste/editing and simulated save preservation support its [no-sample-change assessment](evals/samples/REMEDIATION_PLAN.md#qf03-execution-checkpoint--2026-10-04), not real persistence or actual font identity. Raw fixtures, repository scripts, dependencies, installed version and historical results are unchanged. Keep the agreed primary → dark → authorized secondary review order and the no-new-specialists boundary. Before R4 completion, reconcile relevant required follow-ups or explicitly retain justified later-stage/out-of-scope obligations; do not waive a required acceptance check or demand a backend for the fictional preview.

### R4 — Incremental development and bounded handoffs

Owner: engineering lead. Prerequisites: R2, R3.

Tasks:

- [x] Define reading the current handbook and affected constraints before each meaningful UI development slice.
- [x] Define reuse of approved decisions and compatible delegated details without duplicate interviews.
- [x] Define new-need/conflict/strategic impact on screens, components, runtime contracts and dependent approvals.
- [x] Separate preferences from changed user needs/feature scope; preserve owning approval before strategic expansion.
- [x] Define delta-only handbook/sample updates with meaningful provenance and retained accepted baseline.
- [x] Define revision-aware handoff inputs/returns, one writer, stale-return reconciliation and explicit lead acceptance.
- [x] Demonstrate continuation with one new design need without uncontrolled style drift or duplicate questioning; six bounded cases and separate lead review are recorded in [the R4 forward review](evals/samples/INCREMENTAL_FORWARD_REVIEW.md).

Output: incremental decision/handoff contract and a continuation evaluation.

The original source-review/preparation checkpoint did not establish agent behavior. The subsequent dated forward review records actual case execution and separate lead acceptance; its shared-session, fictional-authority and unperformed product-check limitations remain explicit.

Exit: a new slice follows the approved foundation, only necessary new questions are asked, and conflicting feedback is resolved as one product decision rather than parallel values. Attach the continuation/handoff evidence and lead acceptance.

### R5 — Parametric appearance management with real consumers

Owner: engineering lead with design input. Prerequisites: R2, R4.

Tasks:

- [x] Make admin appearance management mandatory for in-scope new/broad work on products with admin, while retaining the narrow-change and no-admin boundaries.
- [x] Define each setting's ownership and effect: product surface, owned admin surface, organization/tenant, or user. Preserve isolation and protected precedence.
- [x] Reuse the product's current technology and native/host controls. Do not migrate frameworks to resemble the example theme.
- [x] Define validated configuration, resolution, persistence, and component-consumption boundaries; do not scatter raw settings or hard-coded configurable values through pages.
- [x] Offer coherent presets/simple controls plus bounded advanced settings, with human-readable names, defaults, allowed values, dependencies, permissions, consumers, and reset behavior.
- [x] Cover colors/brand, available fonts and typography sizes, line height, spacing/density, borders/radii/shadows, component style, light/dark modes, motion, and supported chart/diagram styles.
- [x] Connect charts, overlays, icons, error screens, and independent assets through appropriate adapters; changing CSS variables alone is not proof of complete consumption.
- [x] Define isolated draft, preview, validation, publish, active-version identity, history, rollback, reset, and safe defaults; keep public rendering on the published version.
- [x] Enforce authorization and input constraints at the trusted boundary, not only by hiding a menu.
- [x] Verify persistence, refresh behavior, cache invalidation, partial/failing loads, and coherent publication.
- [x] Restrict choices to prepared/legal assets and variants. Adding a new font/library or unbundled asset may require preparation/build; routine supported setting changes must not require editing a page.
- [x] Do not substitute arbitrary CSS, JavaScript, HTML, or executable asset input for safe parametric controls. Optional import/export must validate schema, show differences, and never publish silently.

Output: implementation-neutral panel contract and a small stack-appropriate executable fixture proving color, font, density, and component-shape changes.

Exit: valid published changes visibly affect relevant consumers and survive refresh; invalid/unauthorized writes are rejected; drafts remain private; fallback and rollback really work. Attach runtime, persistence, denial/isolation, and rollback evidence. A settings form or JSON file alone does not satisfy this gate.

### R4 integration and R5 preparation record

R4 integrated 2026-10-05 local date through [PR #23](https://github.com/pooyahayati/UI-UX-Skill/pull/23), reviewed head `59c49fd4209899a5da9df17f0db6213116f224a4`, merge `265e9c360c279b637bd8987e16e1f90fb39c0d86`. PR validation run `37234302646` and merge run `37234373674` succeeded, including official quick validation and the merge-bound installer smoke. Publish release was explicitly skipped; latest release remains v3.1.1 published 2026-10-01, its assets retain that date, and tag still points to `d2420e9c60230fb2a667dff971f60a8bbbaaa1de`. No new release, version bump, installation or deployment.

Before publication, native Trivy 0.75.0 (freshly verified stable) actually scanned the exact git-archive delivery tree bound to the reviewed head: zero findings, no warnings and helper PASS. The direct Git-checkout diagnostic had zero secrets but was rejected because its native report type was repository rather than filesystem; an unchanged-helper scan on the exact delivery tree without Git metadata resolved this without weakening validation. Private report/manifest/package hashes are retained outside source. Candidate 3.1.1 ZIP CRC checks passed; these were not uploaded as release assets. No Graphify was required for the bounded input/caller source analysis.

### R5 preparation record

Started 2026-10-05 from the clean matching local/live main merge above; one writer, no new specialist/framework or installed package. Inspected existing runtime governance, handbook/value ownership, design-system migration and stack adapters before editing. Added per-setting ownership/allowed-value/consumer/reset evidence and complete snapshot/base-revision conflict/fallback boundaries to the existing canonical runtime reference, not another control-center methodology.

Engineering risk floor is Tier 2 for the future trusted configuration/storage fixture even though wording-only classification may be lower. The external execution plan retains all R5 tasks and exit criteria. Use a small isolated synthetic browser fixture with real local persistence and trusted validation/permission boundaries, not a production auth/backend project or a settings-only mock. Reuse current Python stdlib/SQLite and browser-native HTML/CSS/JavaScript where adequate; these fixture choices do not mandate a stack in products using this Skill. Generated databases/reports remain outside source. Actual implementation, panel rendering, consumers, denial/isolation, publish/history/rollback/restart/fallback and independent outcome evidence are still pending. No R5 task or stage is marked complete from this preparation.

### R5 executable checkpoint — 2026-10-05

This supersedes the preparation-only description above, not outstanding delivery gates. One implementation writer remains; R5 stays In progress, the completed count stays 5 of 9 and R6–R8 remain required.

- Implemented `scripts/runtime_appearance.py`, its SQLite/HTTP tests and the [isolated runtime fixture](evals/fixtures/runtime-appearance/README.md). The handbook records intent, one catalog/resolver owns 18 prepared controls and external SQLite holds complete tenant publications and actor-private drafts. No dependency/framework/host installation, production data/account or new external design specialist.
- `python -B -X utf8 scripts/test_runtime_appearance.py` passed 17 tests: catalog effects/contrast/target floors, privacy/isolation, stale draft/base conflicts, concurrent publication with one winner, persisted restart/reopen, append-only history/rollback/reset/discard, malformed/unsafe/oversized/duplicate inputs, one-use access/expiry, generic storage failure and whole-snapshot history/default fallback. The lead read existing contract/security guidance; no independent security-specialist return or production certification is claimed.
- Actual red-to-green fixes include huge numeric conversion, non-ASCII CSRF comparison, missing history differences/audit events, Windows early-refusal delivery, deeply nested corrupt stored JSON, duplicate security/framing headers, malformed/absolute request targets and blank/excess history queries. Persisted configuration now uses a bounded strict snapshot decoder. Required rejection/protected-state assertions were not relaxed to obtain success.
- [Three fresh planning evaluations](evals/samples/RUNTIME_FORWARD_REVIEW.md) passed 11 scoped invariants with separate lead review; all canonical raw briefs match evaluated-input SHA256 values. Authored runtime output was not an answer key. Admin output kept icons code-only; R6 must correct that, not claim icon configurability accepted.
- Actual panel observations: 17 non-theme controls changed typography, spacing/density, shapes, colors, component style, motion and SVG chart/diagram presentation in a private preview; public version 2 stayed unchanged until publication, then version 3 survived refresh and a real process restart. Overlay/error/brand/decorative-icon roles share resolution. All five source/default/handbook files remained byte-identical during runtime changes.
- Current-code dark preview stayed private against light version 3; cancel preserved version 3/draft 8, confirmation created version 4 and survived refresh. Measured 400×900 CSS viewport had document width 381; targets exceeded 44 px, table content fit its wrapper, dark chart labels and a 368 px overlay consumed semantic roles. Browser scale 0.8 required a nominal 320×720 request; coverage uses actual DOM geometry, not nominal request or raster size. Temporary override was reset.
- Reset cancel preserved public/history state; confirmation saved private defaults draft 10, leaving version 4 and five history entries unchanged. Discard removed only the draft. Rollback cancel preserved version 4; confirmation appended light version 5 copied from version 3 and retained all six historical entries. Backend/frontend/handbook hashes were unchanged before/after these operations.
- A separate read-only fixture with inaccessible storage rendered identifiable safe defaults/degraded provenance, never a private draft or false success. This capture predates the latest input hardening; current store/HTTP tests cover that corrected source. Inspected old `history-after-restart.jpg` showed loading and is not history proof; inspected new `rollback-history-current.jpg` shows version 5/4/3 entries in a scrolled viewport, not a full-page claim. Screenshots/database/session material stay outside Git. Localhost fixture cookies ignore port; use serial personas, not weaker cookies.
- All eight protected validators passed; 85 cases/17 fixtures are structural validity, not 85 executed model cases. JavaScript syntax/diff whitespace passed. Official local quick validation remains unavailable without PyYAML; no installation to bypass it.
- Pending R5 acceptance: final source/diff review, exact-source native security scan, package integrity, current CI and authorized passing integration. QF04/QF05 stay required R7 obligations; generic font declarations/new HTML dialogs do not prove old glyph identity/native-confirm branches. Version stays 3.1.1; no release/tag/asset upload/deployment/installed-Skill change.

### R5 delivery acceptance — 2026-10-05

Engineering lead accepts the scoped R5 setting/consumer/lifecycle contract at reviewed implementation `6e072c43264ab51b4c3460f180dc6e07f8ddde61`, delivered through [PR #24](https://github.com/pooyahayati/UI-UX-Skill/pull/24). The earlier executable checkpoint's pending gates were subsequently checked; it remains historical evidence, not the current status. R5 is Completed for its stated fixture/Skill scope, not production certification, editable-icon completion or full R7/R8 acceptance. Integration of this acceptance update is still pending and must pass current CI before merge.

- Final source/diff review checked all R5 plan rows, catalog/resolver, trusted store/HTTP boundaries and actual component/SVG consumers. One implementation writer; existing security/interface guidance informed lead review, not an independent specialist return. All 47 tests across six local suites and eight protected validators passed after the final handbook evidence update; JavaScript syntax/whitespace passed. Purity found no forbidden tracked/staged files; its optional local-exclude setup warning is retained.
- [Candidate CI](https://github.com/pooyahayati/UI-UX-Skill/actions/runs/37241534531) passed at that exact implementation, including runtime regressions, protected validators, packaging and official quick validation. PR-event installer smoke was skipped by the existing condition; exact merge-bound installation is a subsequent CI check, not a claimed local installation.
- Native Trivy 0.75.0, freshly resolved stable, scanned the complete exact git-archive delivery tree without Git metadata: helper PASS, zero findings, no warnings. Secret-only scope matches text/stdlib resources with no shipped third-party dependency or changed infrastructure; executable authorization/integrity checks remain separate. Private scan reports and delivery manifest stay outside source. The direct-checkout report-type limitation is preserved rather than weakening the helper.
- Both candidate ZIPs passed CRC and exact byte comparison of all 75 canonical Skill files, including `assets/templates/DESIGN.md` and runtime governance. Portable SHA256 `50b0c59833e6b104cb86b4f08aa0c6b00c2cf6c823224167ba1d2d4b6c2ce209`; plugin SHA256 `417f44b9847a9ed13465511a71ca76ce4717c15615db37c9af4d625c78ffcc49`. Source archive SHA256 `dc46263f8661f803fc46487add015c043e47738f8cc5f500e68b3c72307d67c7`. These are candidate verification artifacts, not uploaded release assets.
- Representative rendered settings, private/public state, publication, refresh/process restart, dark, reset/discard/rollback and source-preservation evidence remain as recorded above. The later handbook evidence update is not runtime synchronization. The verified own loopback server was stopped. Exact OS glyph/font weight and the original native-confirmation branches remain required QF04/QF05 at R7, not waived by this acceptance.
- Owner authorized passing merges and prohibited a new release. Root/Skill/plugin versions remain 3.1.1; public release/tag/assets were rechecked unchanged before integration. No version bump, release dispatch, upload, deployment, host installation, dependency/framework or external design-specialist addition. R6 is next after passing integration; R7/R8 remain required.

### R5 integration checkpoint — 2026-10-05

[PR #24](https://github.com/pooyahayati/UI-UX-Skill/pull/24) merged at exact reviewed head `9f1b0f96dae5b55cdd3819ad90e0e0bef6fb1273`, merge `61eacadece92e187434d72c5c58a9c44e55e2007`. [Final PR CI](https://github.com/pooyahayati/UI-UX-Skill/actions/runs/37241750915) and [merge CI](https://github.com/pooyahayati/UI-UX-Skill/actions/runs/37241799616) succeeded; the latter includes official quick validation and exact merge-bound ephemeral installer smoke. Publish release was skipped. Before the R6 branch, local main/live origin/main matched, clean and 0 ahead/behind. Public v3.1.1 release/tag/assets retain the original identities/dates; no new release, local host installation or deployment. This closes the integration pending at the preceding acceptance-time checkpoint.

The final acceptance-document commit was separately archived/scanned with the unchanged helper: native Trivy PASS, zero findings/no warnings. Rebuilt packages remained byte-identical to the accepted hashes above. Earlier implementation scans were not relabeled final scans; private final manifest/reports remain outside source.

### R6 preparation — 2026-10-05

One writer started R6 from integrated R5. The existing implementation reference now specifies visible family/per-use galleries, central semantic consumers, meaningful incomplete-family fallback, supported size/color/stroke controls, accessibility/direction/state preservation and reuse of the real R5 lifecycle. This is a contract addition, not actual editable icons. All R6 checkboxes remain open pending implementation/evidence.

The retained external Tier 2 plan maps every R6 task to an observable check and preserves existing trusted-write/tenant/draft/history contracts. Extend the existing isolated runtime fixture with prepared local assets, not a new application/framework/library or raw SVG pipeline. Valid pre-icon stored values/history must remain usable through bounded schema compatibility; a silent reset is not migration. Product route is web-application only; inactive PHP/WordPress fixture evidence does not activate their product rules. Required current domain preparation is distinct from the manager's unrelated cached compatibility reasoning; no independent security return is claimed. QF04/QF05 and full R7/R8 remain required.

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
| `PRIVACY.md` | Reconcile the old profile filename during R2 migration without changing data ownership | Documentation compatibility |
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

This is the correction acceptance catalog, not a blanket execution result. Stage records identify actual scoped checks and limitations. Full-candidate scenario reconciliation remains an R8 obligation; previous fixture/schema results alone do not prove the new capabilities.

| ID | Scenario | Observable expected result |
| --- | --- | --- |
| E01 | Owner unfamiliar with design | Clear primary recommendation, rationale, and choice/delegation path without a long technical interview |
| E02 | Owner supplies visual references | Likes/dislikes and confidence are recorded; inference is not relabeled approval |
| E03 | English product discussed in Persian | Samples and handbook use English/LTR, not the conversation language |
| E04 | Persian product | Real Persian text/fonts and correct RTL behavior |
| E05 | Authorized Persian/English secondary review | Primary and dark approvals precede confirmed need/owner authorization; coherent real RTL/mixed-script adaptation follows |
| E06 | Single professional primary proposal | Settled foundations, product-specific responsive priority, meaningful rationale, corrections and revision-scoped approval; no upfront variants |
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

For the initial documentation-only publication (PR #18), baseline validators/package checks concerned the unchanged Skill and roadmap compatibility. They do not count as executed correction scenarios or completed R0–R8 work. New implementation evidence belongs to the relevant correction-stage record, not that historical PR/check run.

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
| Dark mode forgotten or incomplete | Track need early; derive and approve after primary acceptance, then integrated component/chart QA; R3/R7 |
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

- [x] Explicit authorization to start Skill capability corrections; the owner instructed the coding agent to start on 2026-10-04.
- [x] Execution and local evidenced acceptance of R0.
- [x] Execution and local evidenced acceptance of R1, with synthetic/source-review limitations explicitly recorded.
- [x] Execution and local evidenced acceptance of R2, with synthetic consumer checks and independent-behavior limitations recorded.
- [x] Targeted fresh sequential behavior and evidenced stage acceptance of R3, retaining demo/evidence limitations.
- [x] Targeted fresh continuation/handoff behavior and separate lead acceptance of R4, with required later typography/interaction evidence retained.
- [x] Execution and evidenced scoped acceptance of R5, with final candidate checks and passing implementation CI; integration is recorded separately.
- [ ] Execution and evidenced acceptance of R6–R8.
- [ ] Fresh correction behavior/rendered/runtime evidence and exact candidate package verification.
- [ ] Any separately required integration, release, deployment, or installation authority.

**Next implementation action:** implement and verify R6's central semantic icon catalog, visible family/per-use gallery, actual consumers and compatible persisted lifecycle under its retained Tier 2 plan; use the existing runtime reference, not a decorative settings mock or mandated product framework. The owner authorized passing merges but prohibited a new release; retain 3.1.1 and recheck publication skip at each merge. [QF04/QF05](evals/samples/REMEDIATION_PLAN.md#qf06qf07-and-scoped-r4-acceptance-checkpoint--2026-10-05) remain Unverified, owned by the engineering lead and required before dependent R7 typography/completion acceptance. Do not repeat unsupported font/dialog paths, change foundations merely to accommodate tooling, or infer a prior dialog branch. R4's integrated workflow acceptance does not certify those unchanged surfaces or finish R8. Actual persistence/trusted write checks belong to the separate R5 runtime fixture, not fabricated claims about the fictional R3/R4 previews.

No calendar duration or cost is promised. This roadmap defines the execution sequence and acceptance conditions; estimate schedule after the authorized scope and available tooling are confirmed.

## Completed capability history

Stages 1–6 are complete as recorded below. These historical statuses, version targets, and limitations are retained independently from the R0–R8 correction tracker. The historical Stage 6 result is not fresh execution evidence for the correction workstream.

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

**Status:** Active with limited correction exception

**Correction exception:** Authorized for R0–R8 only.

**Outside this exception:** Stabilization maintenance only.

Allowed correction scope:

- design foundation;
- the living handbook;
- visual approval;
- safe parametric appearance management.

The owner authorized kickoff on 2026-10-04. The tracker records what has actually been executed. No new Product Types or additional external design specialists are authorized. Existing Product Pack isolation, historical acceptance limitations, protected product behavior, and separate publication gates remain in force.

The historical capability roadmap is complete; its recorded `3.1.0` stabilization baseline is preserved. R0–R8 are a distinct correction workstream, not retroactively completed history.

Allowed work:

- deduplication of repeated or parallel instructions;
- context isolation and context reduction without removing product knowledge;
- improve Product Pack and local-module isolation;
- strengthen validation that prevents irrelevant knowledge loading;
- correct contradictions, stale documentation, or release metadata;
- improve tests, packaging, and release reliability.

Not authorized outside the named correction scope:

- new Product Types;
- new major capability families;
- additional external design specialists;
- speculative feature expansion.

`persian-writing` remains the only external specialist.

Any capability expansion beyond the named correction scope requires a separate explicit decision; it must not be added implicitly through maintenance or this exception.
