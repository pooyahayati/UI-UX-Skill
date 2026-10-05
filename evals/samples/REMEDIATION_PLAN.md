# Design evidence remediation plan

Prepared: 2026-10-04. Current checkpoint: 2026-10-06. QF01–QF03 and QF06/QF07 are Verified for the bounded outcomes recorded below; QF04 is Owner accepted, with technical metadata limitations preserved. QF05 has owner-reported manual evidence as recorded in the current checkpoint.

## Purpose and authority

Address the observed prototype findings and evidence gaps in the [R3 sequential forward review](SEQUENTIAL_FORWARD_REVIEW.md) without confusing Skill workflow acceptance with finished product quality. The initial request authorized planning only; that slice changed this document and its [roadmap entry](../../ROADMAP.md#design-evidence-remediation-follow-up). The owner subsequently authorized continuing execution on 2026-10-04. New independent agents, publication, installation and a real product redesign still require their separate authority.

Planning baseline: local `codex/r4-incremental-design-handoffs` at `c0a2ac273d800db451ee7eaf9e981483c5f26e75`, with R4 preparation and the review retained locally. The independently evaluated R3 source was merge `ddb4b1b5fb7fc06644a450b738359cf04db6616c`, Skill version `3.1.1`. These are different evidence scopes. Refresh the checkout and instructions before implementation.

R0–R4 are now locally completed for their documented scope; R4 acceptance is recorded in the latest checkpoint below, not inferred from this plan. QF task IDs are quality follow-ups, not extra canonical stages or proof that R7/R8 have started. Historical checkpoints retain their then-current states.

## Preserved decisions and exclusions

- Keep one professional proposal grounded in the product's settled palette, actual font, scale, spacing, platform and usage. Review the primary language/direction/theme first; derive dark after primary approval; derive secondary language/layout only after the preceding gates, confirmed need and named owner authority. Do not infer Persian or bilingual scope from this conversation.
- Keep the canonical product handbook named `DESIGN.md`; preserve one writer, real value-source ownership, approved baselines and scoped decision provenance. It is not a live settings database.
- Explain a detected design/accessibility conflict and recommend the smallest suitable correction. Do not silently overwrite approved foundations, and do not present a known blocker as accepted simply because an owner chose it.
- Add no external design specialist, framework, font installation, paid capture service, Product Pack, general-purpose page builder, feature, role, calendar conversion or backend to repair an evidence gap.
- R5's bounded admin appearance controls and R6's semantic icon controls remain planned. This review does not implement or verify them; their actual consumer, validation, permission, preview, publication and rollback checks belong to their authorized stages.
- Preserve raw evaluation inputs, execution logs, original screenshots and historical conclusions. Corrected evidence gets a new identity; it must not overwrite or retroactively approve the old run. Historical authored examples must not become answer keys for fresh evaluation.

## Evidence inventory and classification

The source review records one fresh agent with nine case-local scenarios and 46 scoped invariants, not nine reset sessions or a complete 81-case candidate evaluation. Four previews were rendered; additional direct root observations covered only their stated contexts. Workflow passes do not establish product approval or accessibility certification.

| ID | Observation or missing evidence | Classification | Consequence |
| --- | --- | --- | --- |
| F01 | Light input border `#8a9e99` against `#ffffff` computes about 2.826:1 | Observed conditional accessibility finding | Below the 3:1 floor where this boundary is needed to identify the enabled field; fix the affected semantic role, not every decorative border |
| F02 | In a Persian free-text note, `HVAC-A2` wrapped at its hyphen; structured list identifiers had LTR isolation | Observed readability risk; wrapping alone is not a confirmed defect | Reproduce and inspect ordering, completeness and copying before selecting any presentation correction |
| F03 | Some retained Persian light narrow/intermediate rasters were clipped or inconsistent; fresh direct root layouts reflowed normally | Observed capture-integrity finding; cause unproven | Those rasters cannot prove complete RTL readability; investigate capture versus actual layout before changing CSS |
| G01 | CSS `system-ui` and joined glyphs, without actual glyph-font identity | Unverified typography evidence | Do not claim the intended font was rendered merely from CSS or visual shaping |
| G02 | Completion was seen after a timed-out interaction, without independently established confirmation acceptance | Unverified interaction evidence | Explicitly distinguish cancel and confirm results; do not infer acceptance from the final screen alone |
| G03 | Exact previously accepted primary/dark source artifacts were absent | Missing baseline evidence | Reconstruction remains proposed; it cannot authenticate or inherit the original sample's approval |
| G04 | Native phone/keyboard, screen reader, zoom, forced colors and the full keyboard path were not all checked | Coverage gaps | Select risk-relevant checks and report actual omissions; do not require every device for every narrow task |
| G05 | Real backend persistence, concurrency and authenticated permissions were not exercised | Outside the simulated preview's scope | Defer actual implementation checks; do not add a backend to make the demonstration look complete |
| G06 | Official local Skill quick validation lacks PyYAML; prior remote CI covers an older merged source | Tooling/evidence gap | Do not install a dependency or reuse old CI as current evidence; obtain relevant CI only with separate publication authority |
| G07 | R4's five raw continuation scenarios have not been executed | Open existing stage obligation | Source walkthrough and preparation tests cannot close R4 behavioral acceptance |

For F01, use the current [W3C non-text contrast explanation](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html), checked on 2026-10-04, alongside the project's existing accessibility contract. Essential identification cues are the relevant boundary; decorative borders and text-identifiable buttons do not automatically need a contrasting hit-area outline. Disabled controls have a different applicability boundary. Calculate against the relevant adjacent resolved colors without rounding a below-threshold result into a pass; inspect actual usability separately.

Operational evidence remains in the existing external evaluation workspace `.roadmap-ops/r3-independent-20261004/` beside the repository. The portable review retains original input/log/result digests. Host-specific reports, runner receipts and screenshots stay outside the Skill package and Git; this project plan is durable repository documentation, not an evaluation result.

## Task tracker and execution sequence

All tasks started as **Not started**; current progress is recorded below. Engineering lead/maintainer is accountable and the single repository writer. A design role may recommend scoped changes; a real product owner decides material product design choices. Independent review is a separate role only when explicitly authorized. Priority orders the work, not a universal severity label for every product.

| Task | Priority | Deliverable | Dependency | Existing stage relationship | Status |
| --- | --- | --- | --- | --- | --- |
| QF01 | First | Trustworthy capture protocol and reproduced affected contexts | Implementation authority and preserved evidence | R3 evidence follow-up; R7 integrated QA | Verified |
| QF02 | High | Bounded essential-control contrast correction and conflict handling | Reliable rendered evidence from QF01 for acceptance | R3 foundation review; R4 scoped decisions | Verified |
| QF03 | High | Mixed-script free-text readability/data-preservation review | QF01 | R3 localized sample; R7 direction QA | Verified |
| QF04 | Medium | Actual font evidence or explicit bounded limitation | QF01; real assets/environment access where needed | R3 sample evidence; R7 typography QA | Owner accepted; metadata limitations retained |
| QF05 | High | Observable completion cancel/confirm checks | QF01; documented supported interaction tooling | R3 executable slice; R7 interaction QA | Unverified |
| QF06 | High | Usable exact baseline fixture and missing-baseline boundary | Existing fixture coverage review; approval-source availability | R3 approval; R4 continuation inputs | Verified |
| QF07 | Final | Affected regressions, continuation observations and lead reconciliation | Required outcomes from QF01–QF06 for the selected scope | R4 acceptance; later R8 candidate gate | Verified |

QF02–QF06 can be investigated once the shared evidence method is reliable; no additional agents are implied. Each change stays reviewable, with no calendar estimate until tooling and authorized implementation scope are known.

### QF01 — Repair capture evidence before diagnosing layout

1. Preserve the 42 original JPEGs and their review classification. Identify which affected captures actually support a required claim; screenshot count is not coverage quality.
2. Reproduce the affected Persian light normal layout at 390 and 768 CSS pixels; include 320 and a relevant wide size as focused reflow controls. These are this sample's regression contexts, not universal product defaults. Retain supported themes/locales only when their sequential authority exists.
3. Record real surface/source and sample/handbook revisions, language/direction, theme, state, actual viewport, screenshot mode, scale when available, document/client/scroll dimensions and tool/environment. Distinguish source metadata from what the browser actually applied.
4. Wait for a stable relevant layout and font readiness, capture through documented tools, then inspect the returned image. Compare visible geometry to actual viewport/scroll observations. A hash or matching metadata cannot by itself establish compositor correctness.
5. If raster capture and direct layout disagree, isolate timing, viewport application, full-page/viewport capture or tool behavior. Classify the cause as reproduced application defect, capture defect or still unknown. Use a documented independent capture method when available; never claim a cause from inference alone.

Acceptance: a reviewer can open the new capture and verify the claimed context, essential visible content and relevant reflow without misleading clipping. A demonstrated capture failure is labeled and excluded from positive layout evidence. If tooling cannot provide reliable evidence, affected visual acceptance remains unverified, with a recovery action; do not patch RTL CSS speculatively.

Likely future instruction location: [visual-regression.md](../../skills/ui-ux-skill/references/visual-regression.md), with a short QA pointer only if needed. Existing stable-capture guidance already covers fonts, viewport and states; add only the missing capture-to-observation validity check. No new screenshot framework is the default solution.

### QF02 — Correct only the relevant contrast conflict

1. Reproduce F01 on the enabled field and identify whether its boundary is the required identifying cue. Inspect existing token ownership and adjacent colors, not only a generic palette swatch.
2. Recommend a minimally adjusted semantic control-border treatment while retaining brand colors, text, font, spacing, density, workflow and decorative separators. No universal replacement hex value is prescribed by this plan.
3. Record the conflict, rationale, affected consumers and pending decision in the sample's existing `DESIGN.md`. If explicit scoped delegation covers this correction, retain it; otherwise obtain the owning decision before treating the change as active. Keep the last approved baseline intact.
4. After authorized correction, measure the relevant resolved colors and inspect enabled/default/focus and relevant validation states. Inspect affected dark consumers only if the same role/source changed; do not invalidate unrelated approved choices or create premature variants.

Acceptance: essential identifying boundary meets at least 3:1 in its applicable state, actual field remains discoverable, unaffected foundations are preserved and evidence matches the new revision. A decorative-border/text-identifiable-control case prevents blanket application of the rule. Approval cannot waive an applicable accessibility blocker, and a passing color calculation is not full-page conformance.

Likely future location: a small pre-acceptance conflict check in [design-foundation-workflow.md](../../skills/ui-ux-skill/references/design-foundation-workflow.md), linking existing [accessibility evidence](../../skills/ui-ux-skill/references/accessibility.md) and [shared interaction floor](../../skills/ui-ux-skill/references/shared/accessibility-interaction.md). The original evaluator already disclosed this conflict correctly; do not describe it as a proven refusal/approval-contract failure or duplicate the accessibility manual.

### QF03 — Verify mixed-script notes without changing stored data

1. Reproduce the supplied Persian note with `HVAC-A2`, adjacent punctuation and a relevant longer identifier at narrow/intermediate sizes. Inspect free-text entry and saved/read-only presentation separately from structured identifier fields.
2. Verify full character order, legibility, editing and copy round-trip. Wrapping at a hyphen is acceptable if it remains unambiguous and usable; diagnose only an actual failure.
3. If a defect is reproduced, select the smallest display/layout correction consistent with existing mixed-direction isolation guidance. Preserve user input and the field's editing semantics; do not inject hidden directional controls into stored text, globally force nowrap or create horizontal overflow to conceal wrapping.

Acceptance: identifiers remain complete and correctly ordered, copying preserves the original value, ordinary text reflows, essential actions remain reachable and no regression changes the data. Retain a no-change disposition if wrapping is valid; the exact sample identifier is regression data, not a product-wide naming rule.

Likely future location: [rtl-ltr-typography.md](../../skills/ui-ux-skill/references/rtl-ltr-typography.md), only if existing guidance needs a free-text-specific clarification. Use the existing conditional Persian writing route for Persian-facing work, without copying its language rules into the Head.

### QF04 — Prove font resolution, or retain the gap

1. Inspect the product's actual approved typography source and assets. A deliberate system-font strategy is not itself a defect. Do not universally replace it with a Persian font or install one on the host.
2. Where supported, inspect actual rendered glyph-font resolution or equivalent platform evidence for Persian/Latin/digits and important punctuation, together with font asset/load failures. CSS family, computed style, `document.fonts.ready` or a readiness check alone does not identify the font used for every glyph.
3. Record actual environment resolution when a system stack is intended; inspect shaping, relevant weights, line height, wrapping and controls at real sizes. If actual identity cannot be exposed, state the limit and do not claim intended-font validation.
4. For future fresh Persian evaluation, verify required specialist compatibility/currency within the authorized host/tool boundary. Historical isolated-agent currency remains unverified; later verification cannot retroactively change it. No implicit specialist update is authorized here.

Acceptance: the claimed typography evidence names its actual method and environment, and layout checks match that source. A required but unavailable asset/resolution check keeps typography acceptance pending. Any licensed asset addition or foundation change needs its own scoped authority.

Likely locations: existing [typography integration](../../skills/ui-ux-skill/references/rtl-ltr-typography.md) and [QA checklist](../../skills/ui-ux-skill/references/qa-checklist.md); reuse the existing handbook evidence fields. Change its template only if a concrete missing field is demonstrated.

### QF05 — Exercise completion cancellation and confirmation

1. Reproduce the actual completion action in an isolated copy of the executable primary refinement. Inspect whether the interaction is a browser-native confirmation or an application dialog; use documented controls for that type.
2. Cancel: observe that completion status and relevant draft values remain unchanged. Confirm: explicitly observe acceptance followed by the intended current-visit simulated status update, scoped to the selected record.
3. Inspect relevant keyboard activation and focus continuation/return. Apply application-modal focus containment only to a real application modal; do not impose custom-dialog behavior on browser-native confirmation.
4. A timeout, missing dialog API or final screen alone cannot prove the branch taken. Use a supported alternative or report unverified. Do not replace the UI framework/dialog just to accommodate an unsupported automation method.

Acceptance: explicit cancel and confirm observations prove their distinct expected local effects, with a clear simulated-data limit. This does not verify backend writes, real authorization, multi-user behavior or persistence across sessions. Escalate to implementation change only if a product defect is reproduced.

Likely future location: the existing executable-sample action/evidence boundary plus accessibility QA pointers. Prefer better execution evidence over adding another duplicated interaction rule.

### QF06 — Make positive baseline evidence executable

1. Inspect current raw fixtures and continuation preparation coverage before adding anything. Keep missing-original/stale-approval scenarios unchanged as negative evidence-honesty cases.
2. For a positive derivation/continuation scenario that needs exact originals, supply a frozen real sample source/viewing artifact, its matching `DESIGN.md` baseline and named scoped approval/delegation input. Fictional test authority must be explicitly identified as such; it is not a real customer approval.
3. Bind the actual sample/handbook identities and scope. Verify the inspected baseline corresponds to the record, and ensure changed choices cannot inherit unrelated approval. Do not make reconstructed proposals into evidence of missing historical originals.
4. Create only the minimal uncovered positive fixture/case, separate from authored outputs. The fresh evaluator receives the candidate and raw product inputs, not expected answers, previous findings or a prescribed layout. If exact originals remain unavailable, retain proposal/pending status and test that boundary honestly.

Acceptance: a future authorized evaluation can inspect the named baseline bytes and derive only the permitted change while preserving unaffected foundations. A mismatch/missing artifact is disclosed and does not authenticate an approval. Preparation remains deterministic and does not overwrite raw inputs or earlier results.

Likely future locations: [case definitions](../cases.json), the existing sample/incremental raw fixture directories and their preparation tests, only for demonstrated coverage gaps. Existing [handbook authority](../../skills/ui-ux-skill/references/design-handbook.md) remains canonical; no second approval document or mandatory parser is introduced.

### QF07 — Reconcile regressions and the open R4 gate

1. Review the affected contract diff, preserved decisions and evidence ledger. Separate an instruction change, an illustrative sample correction and a capture/tool correction; each has a different verification obligation.
2. Run affected structural/route/fixture/preparation tests plus the release-document policy checks. Add only uncovered behavioral boundaries that detect a meaningful failure. A full candidate suite remains required where release policy calls for it, not after each small edit.
3. When separately authorized, perform a bounded fresh forward evaluation of changed behavior using the relevant existing nine sequential scenarios and any justified new cases. Independently review actual returns and exact revised captures; record candidate revision, inputs, environment, actual model identity if exposed and explicit unknowns. No independent agent is spawned by this plan.
4. Evaluate the five existing R4 raw continuation cases when their stage execution is authorized. Require current handbook/baseline reuse, only necessary questions, bounded deltas, no style drift, stale-return handling, single-writer reconciliation and separate lead acceptance. Preparation tests and authored walkthrough are not those results.
5. Select supplementary accessibility/device checks for the real platform and affected risk. Full keyboard, zoom/reflow or screen-reader checks remain required when selected acceptance depends on them; unavailable required checks stay unmet. Backend permission/persistence checks wait for actual implementation, not fabricated demo infrastructure.
6. Record official quick validation as locally unavailable until tooling permits it. After separate push/PR authority, use actual candidate-bound CI rather than older merged-source success. Release/package/install/security gates remain at their relevant stage; no release is implied by local regression success.

Acceptance: each required outcome has relevant current evidence; failures/unknowns cannot be closed by structural validation or agent assertion. The lead records what is accepted, what remains pending and why. R4 completes only after its actual continuation/handoff gate is met. If new evidence falsifies an accepted R3 core contract, reconcile the canonical prerequisite/stage tracker explicitly rather than silently waiving it or marking multiple stages active.

## Batches, recording and stopping rules

Execution batches:

1. Establish QF01 capture validity and the exact reproduced findings. Retain no-change conclusions when evidence does not demonstrate a product defect.
2. Implement only necessary instruction clarifications and authorized scoped sample corrections from QF02–QF06. Keep independent diffs small, reuse existing references, and document decision impact before changing active foundations.
3. Complete QF07 affected verification and lead review; then reconcile R4's gate and the authorized next stage. Publication is a separate decision.

For every task, update its status here as `Not started`, `In progress`, `Verified`, `Failed`, `Unverified` or `Not applicable`. A non-applicable disposition needs a scope reason. Record the writer, tested source/sample/handbook revision, actual check/observation, external evidence identity/location, accepted changes and remaining owner/lead decision. `Verified` means the task's stated outcome, not whole-product certification. Do not mark all tasks verified to express that planning is done.

Keep unresolved required outcomes open. Resolve task dependencies by affected acceptance scope: an unrelated optional native-device check does not block a source-only instruction correction; an unreliable screenshot does block a claim dependent on that screenshot. Any deferral records its owner, reason, required future trigger and owning stage. No silent waivers, broad redesign or duplicate foundation interview.

Recovery: preserve original raw fixtures and prior approved sources, work in new scoped artifact copies, and retain before/after provenance. If a small correction fails, restore only task-owned changed values from the retained baseline within existing authority; never reset the user's worktree or overwrite old evaluation results. Tool failure stops the affected evidence claim, not unrelated work.

## Planning-only verification record

The lead inspected the preserved review and the existing foundation, handbook, accessibility, mixed-direction and visual QA references before choosing the proposed change locations. Available local checks for this documentation slice:

- `scripts/test_roadmap_policy.py`: 11 tests passed; canonical single-active-stage, prerequisite and historical-policy behavior remains intact.
- `scripts/validate_release.py`: release metadata/document validation passed for unchanged version `3.1.1`. This is not the unavailable official Skill quick validator, package verification or release acceptance.
- Local path/heading checks: all 37 local links in the two touched documents resolved.
- Git whitespace/scope review: only `ROADMAP.md` and this plan are intended changes; original review, raw inputs, Skill source and scripts are unchanged.
- Installed engineering Head preflight: version `1.4.0` reported current after a bounded retry; no specialist selected and no installation/update performed. This host check does not establish the historical isolated evaluator's specialist currency.

These historical planning results verify planning/tracker consistency, not remediation execution, a new model run, product visuals or candidate CI. At that planning checkpoint the checkout remained local and unpublished; no new commit, PR, issue, milestone, merge, release or installed-Skill change was made by the planning slice.

## QF01 execution checkpoint — 2026-10-04

The lead reused the unchanged independent-run Persian sample `A-fa-forward-r1` / draft handbook `hf-fa-1`. Existing fictional locale scope permits this review; no new locale or design approval is created. Original 390 normal and 768 open captures were visibly cropped. In a fresh Codex in-app browser, `fullPage: true` reproduced the same geometry mismatch at both widths while document measurements still reported the intended viewport/reflow. `fullPage: false` returned correctly reflowed viewport images at 320, 390, 768 and 1280. The open form at 768 was also inspected through a separately captured lower viewport after scrolling 276 CSS pixels.

This localizes the reproduced failure to the full-page capture path under viewport override in this environment, not a demonstrated application RTL defect. The internal backend cause and exact historical call parameters are unverified. Full-page rasters are retained as failed evidence; viewport replacements substantiate only their named visible contexts. No CSS, foundation value, original source/handbook or historical finding is rewritten.

Added a bounded capture-validity contract to `visual-regression.md` and one QA pointer. External `TASK.md`, `REVIEW.md` and eight new capture files are retained in `.roadmap-ops/qf01-capture-review-20261004/` beside the repository. Source, original-image and replacement hashes plus measured dimensions belong to that operational review; the reproduced 390 full-page raster is byte-identical to the failed original, while its valid viewport replacement is a separately identified 390x843 raster for a reported 390x844 viewport. No rescaling or pixel-parity claim is made.

Lead acceptance: **QF01 Verified**, scoped to the capture-validity contract and affected-context recovery. Eleven roadmap-policy tests plus release metadata, product-route, shared-rule, design-system and eval-fixture validators passed; Git whitespace review passed after normalizing only touched files. Fixture validation checks 81 definitions/14 fixtures, not model outcomes. Official quick validation was attempted and remains unavailable because PyYAML is missing; no dependency installed. This is not a fresh independent agent evaluation, actual font validation, accessibility certification or R4 continuation acceptance.

## Planning completion and then-current next action — 2026-10-04

- [x] Findings classified separately from unverified/out-of-scope checks.
- [x] Task owners, priorities, dependencies, proposed locations and observable acceptance criteria defined.
- [x] Original evidence, settled foundations, sequential approval and no-new-specialist boundaries preserved.
- [x] Work linked into the canonical roadmap without changing stage acceptance or claiming execution.
- [ ] QF01–QF07 implemented/verified according to their actual authorized scope.
- [ ] Fresh R4 continuation/handoff acceptance obtained.
- [ ] Any separately authorized integration/publication checks completed.

Next action: recover QF04's actual glyph-font/weight evidence and QF05's native-confirmation control before claiming those outcomes verified; see the recovery checkpoint below. QF01–QF03's bounded lead acceptance is complete. Execution of QF04/QF05 has been authorized; do not repeat that question. The separately authorized required Persian specialist update is verified; other installations are not authorized. A different browser must comply with the selected-browser control policy. No new taste selection from the maintainer is needed. QF06/QF07 remain Not started.

## QF02 execution checkpoint — 2026-10-04

Writer/lead: engineering lead, no additional agent. Owner explicitly authorized QF02 after the QF01 handoff. Added two scoped conflict-handling paragraphs to [the existing foundation workflow](../../skills/ui-ux-skill/references/design-foundation-workflow.md), linked to existing accessibility contracts. The original evaluator had already disclosed the conflict; no proven earlier approval-contract failure is alleged.

Reproduced the enabled note-area cue from `samples-approved-secondary-language`: fill alone contrasts only 1.0990:1 with its surrounding article; the essential original border is 2.5711843295398586:1 against its inside and 2.825854615521382:1 against its outside. Created an isolated corrected **proposal**, `A-fa-qf02-r1 / hf-fa-qf02-1`, in the external workspace `.roadmap-ops/qf02-control-contrast-20261004/` beside the repository. Only textarea consumes a new semantic control-border role, measuring 3.1946396051863704:1 and 3.5110617972920264:1 respectively. Values live in its HTML source; its `DESIGN.md` records rationale, consumers, parent draft, authority and pending approval. The darker border is sample-specific, not a universal value prescribed by this Skill.

Decorative border/separator roles, brand/action/text/fills, fonts, spacing/density, layout and JavaScript stayed unchanged. Existing dark aliases the old border role and resolves identically (5.367869685458795:1 inside / 4.3255857295255:1 outside); no new theme/language phase is authorized. Owner approval of the revised fictional product remains pending, not required from the Skill maintainer to accept this maintenance task. Actual prior approved artifacts remain unavailable (QF06); historical sample/handbook and all raw inputs/renders were preserved.

Rendered/manual observations: phone 390x844 default/keyboard focus, empty enabled field and actual simulated save failure with unchanged draft; intermediate 768x844 focus and an incidental default 1280x720 inspection. Existing dark focus was inspected. Nine viewport captures are retained with actual context, scroll positions, dimensions and hashes in external evidence; no full-page claim. Raster sizes differ from CSS viewport sizes, with coherent scaled geometry; the report retains that limitation and the initial new-tab viewport reset, not a false phone label. No invalid-field styling exists, so that state is not applicable for this delta. These checks do not prove actual glyph/font identity, full keyboard/screen-reader/accessibility conformance, real persistence/permissions or completion cancel/confirm.

Lead acceptance: **QF02 Verified** for the clarified conflict contract and bounded proposed sample correction. The external `verify-scope.ps1` passed exact allowed-delta/unchanged-script and contrast checks. Eleven roadmap-policy tests and release metadata, product-route, shared-rule, design-system and eval-fixture validators passed; fixture validity covers 81 definitions/14 fixtures, not agent behavior. Official quick validation is unavailable without PyYAML; no dependency installed. Fresh independent conformance remains QF07; R4 continuation acceptance is not closed. Changes remain local/uncommitted, not pushed/merged or installed. Next: QF03.

## QF03 execution checkpoint — 2026-10-04

Writer/lead: engineering lead under the owner's next-step authority; no additional agent. Reviewed unchanged QF02 proposal `A-fa-qf02-r1 / hf-fa-qf02-1` in an isolated external clone, `.roadmap-ops/qf03-mixed-script-20261004/` beside the repository. HTML and handbook remain byte-identical to QF02; no new visual revision, customer approval or prior accepted baseline is asserted. The short note transcribes historical visible content and the recorded identifier case; authenticated historical keystrokes/codepoints are unavailable. Declared punctuation and long-token strings are synthetic regression inputs, not product naming rules.

Fresh viewport inspections: Persian RTL light at 320/390/768 CSS pixels, plus the already-present dark at 390. The short `HVAC-A2` split at its hyphen at 390; longer identifiers wrapped at narrow sizes, and the reference identifier wrapped at 768. All inspected parts and adjacent punctuation remained complete, ordered and readable. Fourteen retained observations and eight manually inspected viewport rasters record actual geometry/scroll; document and field measurements showed no horizontal overflow, and Save remained visible/reachable. Returned images are scaled relative to CSS viewports, not pixel-parity or full-page evidence.

Actual keyboard copy/clear/paste round-trips preserved the exact short, long and punctuation strings; the previous clipboard was restored after each test. Backspace and retyping restored the exact editable identifier. Actual simulated save success at 320 and failure/retry at dark 390 retained the long note unchanged. There is no separate saved/read-only note view in this source: that presentation is **Not applicable**, not fabricated or certified. Real server persistence/permissions, full keyboard navigation, screen readers/native phones and actual glyph-font identity remain unverified or outside this slice.

Disposition: **no sample UI/data change needed for the inspected cases**. Added two compact free-text-specific paragraphs to [the existing direction reference](../../skills/ui-ux-skill/references/rtl-ltr-typography.md), distinguishing structured isolation from editable-text verification and rejecting speculative stored directional controls/global nowrap. No Persian language methodology was duplicated. This clarification is not evidence of a prior general workflow failure or universal mixed-script conformance.

Lead acceptance: **QF03 Verified** for the bounded readability/data-preservation assessment and instruction clarification. Recorded-value/clipboard-result/keyboard/action/overflow checks and unchanged-source hashes passed; visual judgment is separate manual evidence. Eleven roadmap-policy tests plus release metadata, product-route, shared-rule and eval-fixture validators passed; 81 definitions/14 fixtures are structural validity, not fresh model outcomes. Official quick validation was attempted and remains unavailable without PyYAML; no dependency installed. Source diff/whitespace and local link checks passed. R4's actual continuation gate remains open. No commit, push, merge, new PR/issue/milestone, release or installed-Skill change. Next: QF04.

## QF04 and QF05 execution checkpoint — 2026-10-04

Owner explicitly requested both tasks. Engineering lead remains the single writer; no agent. Operational source copies, four inspected rasters and nine concrete observations are retained in `.roadmap-ops/qf04-qf05-evidence-20261004/` beside the repo. Primary English source is byte-unchanged `A-refined-forward-r1 / hf-refined-1`; Persian source is byte-unchanged QF02 proposal `A-fa-qf02-r1 / hf-fa-qf02-1`. Their handbooks/approval states are unchanged. No new locale/theme, real product approval, backend, font asset or UI rewrite.

QF04: inspected current proposed system-stack source, Persian/Latin identifiers/digits/punctuation at 390/768, title/body/label/control roles and existing dark at 390. The selected browser exposes CSS/layout and FontFaceSet metadata, not actual per-glyph font resolution. FontFaceSet reports loaded/zero web faces, source has no font-face/assets/external stylesheet; this is not a rendered-font identity or real-weight proof. Returned rasters show legible joined Persian and mixed-script text in these contexts, with no measured horizontal overflow; actual identity and synthesized-weight status remain **Unverified**. Added one compact typography evidence-boundary paragraph plus QA pointer; no font replacement or install.

Current required-specialist check: installed `persian-writing` is 1.3.6; canonical latest stable release resolves to v1.4.0/version 1.4.0. Existing `validate_specialists.py --check-upstream --check-codex --require-required-installed --require-current` failed the current-version condition after a narrow read-only network retry. The installed instructions were read, but known-stale specialist-dependent validation cannot be accepted. No update authorized/performed. QF04 remains **Unverified**, not whole-font or Persian acceptance. Historical evaluator currency is unchanged/unverified. Vibe preflight passed after the temporary-lock access retry with no --apply; installed UI metadata was reported current by that elevated manager, but direct sandbox read was denied, so current candidate repo instructions were used rather than claiming installed candidate changes.

QF05: saved an exact synthetic draft on the unchanged primary English/LTR/light refinement. Actual eventual in-memory-save status and enabled completion were observed. Keyboard Tab reached the visible completion action. Enter then timed out in the browser control path; documented getJsDialog returned undefined. Subsequent DOM/AX observations, native Escape and close were unavailable through the same focus-emulation timeout. No explicit dismiss or accept was observed, and no post-choice state was established. The affected tab remains in handoff; closing/reset is not claimed. Visibility set was attempted but get reported false. This is an interaction-tooling/evidence gap, not a proven product defect. QF05 remains **Unverified**; neither cancellation nor confirmation can be counted as passed. Application-modal focus containment is N/A to this source's native confirm. No framework/dialog replacement was made to accommodate automation.

Added one bounded QA evidence pointer, not another confirmation implementation or product rule. Required recovery: dismiss any pending native preview confirmation through an accessible user surface, then run explicit cancel/preserved-state and accept/current-record-result checks with working documented dialog controls. Actual glyph-font resolution requires a capable inspector; updating the known-stale required Persian specialist needs explicit host-change authority before dependent acceptance. Do not waive those checks, infer a branch from a final screen, or use old CI/fixtures to fill them. QF06/QF07 and R4 continuation remain open.

Final checks: eleven roadmap-policy tests and release metadata, product-route, shared-rule, design-system and eval-fixture validators passed; fixture structure is 81 definitions/14 fixtures, not fresh behavior. All 39 local paths/anchors resolved, whitespace/scope review and four unchanged-copy hashes passed. Pre-confirm exact draft/keyboard focus and recorded geometry checks passed only their named assertions. Official quick validation remains unavailable without PyYAML, no dependency installed. Own loopback server stopped and port 8768 is clear. Final viewport-reset attempt timed out and reset the automation session; tab/dialog cleanup remains unverified after that reset. Re-observe the user/browser state before any resumed UI action. These structural successes do not close QF04/QF05. Source changes remain local/uncommitted; no push/merge/install or new PR/issue/milestone/CI claimed.

## Required Persian specialist recovery checkpoint — 2026-10-04

The owner separately authorized updating the installed `persian-writing`, not other Skills, host dependencies or system fonts. The lead used the bundled `skill-installer` helper to download the canonical `ali2000hos/persian-writing` release `v1.4.0` into an external staging directory, checked its instructions/version consistency, then preserved the entire installed 1.3.6 directory before installing the staged candidate. No additional agent, product font change or source vendoring.

Operational receipt and full per-file SHA-256 manifests are retained in `.roadmap-ops/persian-writing-update-20261004/` beside the repository. All 43 old files match the recoverable backup; all 49 installed files match the staged download. The backup is outside the Skill discovery directory. Existing `check_version.py` reports 1.4.0 in all four version locations; the repository's live `validate_specialists.py --check-upstream --check-codex --require-required-installed --require-current` now passes against canonical latest stable `v1.4.0`. That validator compares the main Skill bytes; the separate tree comparison proves installation fidelity to the downloaded candidate, not independent upstream per-file attestation.

Read the new main instructions and the selected writing, orthography, fonts and HTML references before further use. Product-approved aesthetics retain precedence; brand-neutral examples/defaults do not authorize replacing settled fonts or colors. The specialist is available to normal Skill discovery on the next user turn. This resolves the current-host stale-specialist blocker only; it neither certifies actual rendered glyphs/weights nor repairs missing historical evaluator evidence.

Fresh browser inventory after the previous automation reset lists no tabs in the selected Codex in-app browser. The cause of tab removal, prior dialog choice and viewport-reset outcome are not inferred. No new native-confirm interaction or screenshot was produced; no previously observed state is recounted as a new branch result. QF04 and QF05 remain **Unverified**, QF06/QF07 remain **Not started**, and R4 remains the sole active stage. Required next evidence: a capable actual font inspector and a documented working native-confirm interaction path, or an explicit scoped decision about the unmet checks. No implicit browser switch, dialog replacement or acceptance waiver.

This is a host installation/tracker checkpoint, not a new product approval, source release or integration. Historical checkpoints above remain unchanged. Repository changes remain local; publication and other installations keep their separate authorization gates.

## QF06/QF07 and scoped R4 acceptance checkpoint — 2026-10-05

The owner's remaining-work goal authorizes passing merges and practical defaults but prohibits a new release. Bounded independent evaluation under skill-creator used raw prompts/inputs and isolated outputs, not another implementation writer or external design specialist. See [the lead's six-case review](INCREMENTAL_FORWARD_REVIEW.md) for 31 assessed invariants, actual reads/changes, shared-session limitations, rendered/action observations and exact output identities.

QF06 Verified: supplied separate frozen executable HTML/handbook input with exact byte binding and explicitly fictional scoped approval/delegation. Existing missing-original/stale cases stayed unchanged. Added actual mismatched/missing/malformed/path boundary regressions and preparation preservation checks. Fresh continuation changed only delegated save disclosure and revision metadata; the lead independently checked exact source differences and phone/desktop rendering/actions. This does not authenticate absent historical originals or actual customer approval.

QF07 Verified for affected R4 regressions and lead reconciliation: all five original continuation cases plus the executable follow-up were fulfilled, actual returns reviewed separately, and current affected validators passed. R4's bounded workflow exit is accepted. Whole-candidate behavior, packages, CI, integration and security are not closed by this status; they remain explicit R8/publication obligations.

QF04/QF05 remain Unverified and required at R7. Responsible: engineering lead. Reason for scoped deferral: actual font identity and native completion branches are unchanged and do not determine the accepted local feedback/proposal/handoff contract; current controls cannot establish their required evidence. Trigger: before accepting the affected typography/completion surfaces, obtain actual glyph-font/weight inspection and distinct explicit cancel/accept observations on their exact source. No optional relabeling, tool substitution, silent waiver or claim that the old failed interaction recovered. Browser preview work here exercised save/failure/refresh only; viewport reset and tab close succeeded. Required final candidate acceptance cannot claim these checks passed without new evidence.

Current next action: publish/review/merge the accepted R4 slice with unchanged version and real candidate-bound checks, then enter R5. No new release, font installation, additional specialist or production action is authorized by this checkpoint.

## R7 recovery checkpoint — 2026-10-05

R4–R6 have subsequently integrated with passing CI; those stage outcomes do not
retroactively prove QF04/QF05. See [R7 partial execution](INTEGRATED_QUALITY_REVIEW.md).
Original primary/Persian HTML hashes still match preserved QF evidence. Current
browser capability inspection exposes no actual glyph-font/weight inspector;
no new working original-native-confirm path was established or retried merely
to repeat the prior timeout. New runtime HTML overlay observations are separate.
Both required outcomes remain Unverified, engineering-lead-owned, triggered
before dependent R7 acceptance. No font substitution, installation or silent
waiver; unaffected scoped checks continue without declaring R7/R8 complete.

After the separately authorized roadmap-only PR #26 merge, the
[R7 continuation](INTEGRATED_QUALITY_REVIEW.md#post-roadmap-continuation--2026-10-05)
rechecked the preserved source hashes and currently available browser/tool
capabilities. No new actual-font inspector or working original-confirm path
became available. These are still required Unverified outcomes, not accepted
because 31 unrelated contract/progress tests pass. An alternate capable
browser/developer surface or equivalent concrete manual/platform evidence is
needed; do not repeat the same unsupported timeout or replace the source.

## Owner evidence reconciliation — 2026-10-06

The owner reports the three offered manual tests OK. The exact screenshots and
their scoped observations are recorded in the [integrated review](INTEGRATED_QUALITY_REVIEW.md#owner-manual-review--2026-10-06).
QF05 now has attributed owner save/cancel/accept evidence and a visibly matching
final completion state; this is not a new automated native-dialog branch result.
QF04 gains separate new-Vazirmatn wide/narrow visual observations, not original
per-glyph/control face metadata. Do not repeat the same owner tests or erase
historical limitations. Original required metadata and remaining integrated
coverage still block whole R7/R8 acceptance; unrelated validators do not waive it.

### Subsequent explicit owner acceptance

The owner stopped further font testing, explicitly instructed that this test be
treated as approved, and will report any later problem for correction. QF04 is
therefore **Owner accepted** for this bounded review. Missing technical metadata
remains an evidence limitation, not a reason to request more font screenshots or
block this review. This explicit reconciliation supersedes the earlier QF04
blocking disposition without rewriting historical observations or claiming a
technical pass. Reopen only for a concrete newly reported/observed font defect;
other R7/R8 obligations are not accepted by this decision.
