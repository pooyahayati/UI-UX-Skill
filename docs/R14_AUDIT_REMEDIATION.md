# R14: Bounded Quality Gap Corrections

Prepared 2026-11-02. This is an implementation plan, not an implementation result.
[ROADMAP.md](../ROADMAP.md#r14-bounded-quality-gap-corrections) is the only live
progress ledger. Execute R14.1, R14.2 and R14.3 in that order when authorized.

## Objective and authority

Close the evidenced viewport-validation gap, make existing visual critique more
useful, and introduce optional icon discovery/state morphs where a product needs
them. The owner's explicit constraint is to fill deficiencies **without changing
the Skill's purpose, operating workflow or settled product decisions**.

The 2026-11-02 instruction authorizes roadmap/planning edits only. This checkpoint
changes `ROADMAP.md` and this plan; it does not implement guidance, code or tests,
install resources, change dependencies, alter fixtures, commit/push/merge, publish
or update the installed Skill. Previous delivery permissions remain attached to
their completed scope. Record a later implementation instruction here and in the
roadmap; do not ask again about already settled design/font choices.

**Superseding instruction, 2026-11-02:** the owner authorized R14.1 through R14.3
in order, then merge, a new release and a managed local update. The planning-only
boundary above records the earlier checkpoint; the [execution record](R14_EXECUTION.md#authority)
now owns this bounded implementation and delivery authority.

## Baseline and confirmed finding

- Audited release: 3.6.1; local and remote `main` were verified at
  `94c445dfa4980e5c5d44d875deeebabcff18df98` during planning.
- **Confirmed, Medium:** `r12_runtime_errors` in
  [test_contracts.py](../evals/wordpress-settings/test_contracts.py) excludes
  `VIEW-*` rows from its required observation inventory and accepts any nonempty
  detail object. The R13 legacy-report tests do not reject missing/contradictory
  viewport details.
- Reproduction used an in-memory copy of
  [the current regression report](../evals/wordpress-settings/evidence/r13/regression/r13-regression-results.json).
  Removing all five `VIEW-*` rows reduced 21 observations to 16 and returned no
  validation errors. Keeping the rows but setting `overflow=true`, `direction=ltr`,
  `regular=false`, `bold=false` and empty `rendered_fonts` also returned no errors.
  No report or screenshot was changed. This proves a validator gap, not that
  the current screenshots or the owner's prior approval are invalid.
- The prior audit's 32 existing command groups passed. That did not cover these
  negative scenarios. No fresh browser run or new model evaluation was claimed.
- R14.2 and R14.3 are targeted improvement proposals, not additional confirmed
  defects or evidence that external Skills outperform this Skill.

## Protected decisions and source-adoption rule

1. Keep the existing product discovery, focused recommendations, one responsive
   primary sample, refinement, applicable-theme gate and authorized secondary
   language sequence. No forced extra designs, translations or dark variants.
2. Keep one `DESIGN.md`, approved palette/fonts/spacing/density, semantic tokens,
   existing Product Packs and conditional resource loading. Preserve Vazirmatn
   as the Persian default unless the product owner chooses otherwise.
3. Preserve the dashboard shadcn/ui default and its existing-stack exceptions,
   optional Material selection, WordPress settings-only component policy and
   separate operational-surface routing. Native, quiet interfaces are valid.
4. Reuse existing appearance/icon/motion ownership, authorization, draft, preview,
   publish, history and rollback contracts. Do not create another settings engine
   or add an admin panel to a product/task that does not have one in scope.
5. No wholesale external Skill import, new external specialist, mandatory agent,
   detector, MCP service, CLI, network call or new design workflow. No automatic
   library migration, installation or replacement of owner-selected icon families.
6. For every retained external idea, identify the current gap, relevant product
   task, existing canonical destination and observable benefit. Rephrase only
   the useful criterion; retain attribution/license obligations for adapted
   material. Omit duplicates, house-style bans and conflicting instructions.
   An external source is research material, never authority over this Skill.

## Selected sources and bounded use

These revisions identify the researched material, not permanent dependency pins.
Recheck the exact file/API/license at adoption and record the chosen revision.

| Source / reviewed revision | Eligible contribution | Explicit exclusions |
| --- | --- | --- |
| [Impeccable](https://github.com/pbakaus/impeccable/tree/e89e3ada3e875a89ac2c5d33d11e65ebef6fe285), especially `skill/reference/operate.md` and `critique.md` | Task-sensitive hierarchy, density and evidence-backed refinement of a rendered surface | Its orchestration, required agents/tools, whole command suite and mandatory follow-up questions |
| [Interface Design](https://github.com/Dammyjay93/interface-design/tree/2f9be3206855bcb2d1d0af262c8bae25cba6658d), `.claude/skills/interface-design/SKILL.md` | Dashboard/settings hierarchy, consistent interaction patterns and restrained surface treatment | A second design-memory file, universal aesthetic prescriptions or changes to native host behavior |
| [Aria Icons](https://github.com/LeulAria/Aria-Icons/tree/c1d22bdca5a83921f435a52f2832320538236a62) / [catalog](https://icons.leularia.com/) | Optional development-time icon discovery, comparison and selected asset export | Whole-catalog imports, mixed-family defaults, automatic MCP/CLI setup or a runtime network dependency |
| [morphicons](https://github.com/guillermolg00/morphicons/tree/8c3e3c7cd717b2381f8f35cf6c245afd80d8d7df) | Optional, meaningful icon state transitions when existing primitives are insufficient | Mandatory animation, decorative motion everywhere, a competing motion policy or an owner-facing library switch |

Aria's code license does not license every icon uniformly; upstream icon-set
terms remain applicable. Its inspected web package uses `morphicons ^1.7.0`,
while the inspected upstream is 2.0.2. The Aria converter rejects some inputs,
including filled icons; do not transfer newer engine capabilities to the older
exporter by assumption. Its generated examples need accessible control names
and an explicit motion policy. See the [exporter](https://github.com/LeulAria/Aria-Icons/blob/c1d22bdca5a83921f435a52f2832320538236a62/apps/web/src/lib/icon-morph.ts)
and [1.7.0 reduced-motion contract](https://github.com/guillermolg00/morphicons/tree/v1.7.0#reduced-motion-all-five-bindings).

UI UX Pro Max, Vercel's Skills, Taste Skill and Anthropic's frontend-design were
research alternatives, not additional R14 workstreams. Do not expand this plan
to include them without a concrete gap and a separate scope decision.

## Planned file boundaries

Paths below are relative to the repository unless stated otherwise. They are
future implementation targets, not permission to edit them in this checkpoint.

| Package | Expected targets and limits |
| --- | --- |
| R14.1 | `evals/wordpress-settings/test_contracts.py`, relevant evidence tests and existing CI entrypoints; `scripts/roadmap_policy.py` and its tests for the new ledger. Preserve actual producers/reports unless the validated contract requires a documented successor. |
| R14.2 | Under `skills/ui-ux-skill/`: existing `references/qa-checklist.md`, `visual-regression.md`, `ux-evidence-and-metrics.md` and relevant product sections only where a named gap exists. Prefer these canonical locations over a parallel critique guide. Extend existing evaluation scenarios and their affected source bindings. |
| R14.3 | Under the same Skill root: the icon section of `references/implementation-strategies.md`, `interactive-motion.md`, and only necessary links in `runtime-ui-governance.md` / handbook guidance. A small conditional provider reference is acceptable only if needed for context isolation, with packaged reachability checks. Extend existing icon/motion scenarios and bounded specimens only as needed to verify claims. |

Central `SKILL.md`, registries and templates change only for a demonstrated
routing/consistency requirement, with affected-input analysis. No blanket rewrite,
product-default change, production application or new package ecosystem is planned.

## R14.1 — Validate legacy viewport evidence

**Entry:** owner instruction to implement R14.1. Fix the confirmed defect first.

| ID | Observable acceptance |
| --- | --- |
| VIEW-1 | Both in-memory reproductions above first demonstrate the current acceptance bug, then fail for the intended inventory/detail reason after correction. A valid unchanged report continues to pass. |
| VIEW-2 | The legacy producer requires exactly `VIEW-multi-1440`, `VIEW-multi-390`, `VIEW-simple-1440`, `VIEW-simple-390`, and `VIEW-zoom-200`, in addition to its existing behavioral IDs. Removing one/all, duplicating, renaming or substituting an unknown viewport ID fails. Do not apply this producer-specific inventory to discovery/validation reports or to all products. |
| VIEW-3 | Each regular viewport row requires the producer's RTL/no-overflow/regular-and-bold font results and actual custom Vazirmatn records for its captured heading/label selectors. Missing, malformed or contradictory data fails, even with `status=passed`. The zoom row validates its own recorded zoom/no-overflow/finite positive width contract; it does not inherit unrelated font fields. Retain the explicit CSS-zoom limitation. |
| VIEW-4 | Historical valid R12/R13 regression records pass under their own explicit contract without discovery-only fields. Raw/normalized provenance, source/runner hashes, observation methods and existing rejection cases remain effective. Do not change old evidence or expected hashes merely to make a check green. |
| VIEW-5 | Existing CI runs the negative cases. The R14 ledger gains ordered-prerequisite, count, active/next and dated-evidence checks through the existing roadmap validator, while historical ledger tests continue to pass. |

**Verification:** focused evidence/unit tests, the WordPress contract suite,
roadmap-policy checks and relevant release validation. A validator-only change
does not require another owner font test or an invented browser run. Rerun the
browser only if executed producer/fixture inputs or required coverage change;
preserve the old evidence and bind any fresh successor explicitly.

## R14.2 — Strengthen existing visual critique

**Entry:** accepted R14.1. Improve the usefulness of the existing QA/refinement
step; do not insert another lifecycle stage or approval gate.

| ID | Observable acceptance |
| --- | --- |
| CRIT-1 | Each adopted criterion maps a demonstrated omission in current guidance to a relevant product task and one canonical destination. Duplicate or unsupported external prescriptions are omitted. No external Skill/tool is installed or made mandatory. |
| CRIT-2 | A critique identifies the actual surface/state, observed hierarchy or interaction problem, task impact, smallest compatible correction and verification method. It distinguishes observed defects from proposals; personal taste alone does not create a defect or redesign requirement. Unavailable rendered evidence is stated honestly. |
| CRIT-3 | Compare the existing and candidate critique on two bounded existing examples: Persian WordPress settings and a mobile web-app/dashboard task. Hold content, approved foundations, state and viewport constant. Retained additions must detect a concrete previously missed issue or make its correction/verifiability materially clearer; remove additions with no demonstrated benefit. A baseline that already meets a criterion needs no artificial redesign. |
| CRIT-4 | Cases for a simple native settings form, an operational admin page, an existing approved design and a narrow audit preserve their scope. No forced cards/search, framework change, extra design directions, repeated approval, second handbook or new language/theme requirement appears. Applicable R13 routing/theme/error-ownership behavior remains intact. |
| CRIT-5 | Where a bounded correction is rendered, before/after evidence shows the claimed result with relevant responsive/keyboard/state checks. Task success, setting findability or user speed is called measured only when actually measured. Source review or agent opinion alone cannot establish user-performance improvement. |

**Verification:** source review plus affected behavioral evaluations using raw
requests, not rubric-fed expected answers. Reuse existing synthetic examples and
valid rendered evidence where their inputs still match. Keep comparison artifacts
and actual limitations in the existing evaluation structure; do not create a new
benchmark platform, score quota or owner questionnaire.

## R14.3 — Optional icon discovery and state morphs

**Entry:** accepted R14.2. Aria is an optional source; morphicons is an optional
implementation choice for a specific interaction. Neither becomes a product style.

| ID | Observable acceptance |
| --- | --- |
| ICON-1 | Guidance selects the existing/static icon solution when it meets the need. Aria can help discover/export a coherent, approved family without replacing existing assignments. A meaningful state pair may justify morphicons only after checking stack/host compatibility and the smallest sufficient alternative. No automatic install, migration or remote runtime dependency follows from mentioning the provider. |
| ICON-2 | A selected asset records upstream family/name, source revision and applicable icon license/attribution separately from Aria's code license. Unknown terms or unvalidated/unsafe SVG input do not enter the approved asset set. Preserve the existing trusted asset boundary; no arbitrary SVG/script/URL upload path is introduced. |
| ICON-3 | Record the actually selected engine/exporter version and supported shapes. Exercise an accepted pair and an unsupported shape/export case; the latter falls back to a truthful static icon or explains the limitation. Do not claim every catalog icon morphs or infer exporter support from a newer engine release. |
| ICON-4 | An interactive icon has an accessible control name, truthful state, keyboard/focus behavior and a useful static fallback. Only directional meaning is mirrored in RTL. A save/check or success transition waits for the actual confirmed result; animation does not imply persistence or completion. |
| ICON-5 | Existing owner/user/OS precedence is honored at startup and when preferences change during motion. Owner/user off removes all claimed transitions; system reduction cannot be overridden by branding. Verify normal/reduced/off, rapid interruption and cleanup. The inspected default `reducedMotion=never` must not leak into a product's effective policy; `user` and `always` are mapped to the chosen version's documented behavior. |
| ICON-6 | If appearance management is in scope, use its existing semantic assignments, approved family/state-pair choices and bounded motion presets. Preview, save/reopen, publish, reset and rollback affect the actual claimed consumers. Reject unknown identifiers/invalid presets at write time; configuration/provider loading failure retains a safe last-valid/default/static fallback. No new panel, raw spring/code controls or runtime library selector is created. |
| ICON-7 | Verify one bounded representative mobile interaction using the selected version, including accessible naming, off/reduced behavior and interruptions. Record actual added route payload and observed performance against the existing baseline/budget; do not invent frame-rate claims. Keep WordPress host controls and unrelated products unchanged. Passing guidance tests alone cannot establish runtime support. |

**Verification:** extend existing icon/motion selection and negative scenarios;
check representative rendered/runtime behavior in a bounded synthetic fixture,
not a production migration. Exercise protected WordPress/narrow-fix/no-admin
cases. If required runtime verification is unavailable, keep that acceptance open
rather than presenting a documented provider as a tested adapter.

## Evidence, integration and completion

- Before guidance edits, map changed paths to consumed evaluation inputs. Preserve
  WPS/R11/R12/R13 baselines and original outputs. Use explicit, exact-parent R14
  successors where needed; no broad hash exclusions, version waiver or relabelled
  historical answer. Re-evaluate affected outputs independently under the existing
  evaluation contract, without exposing expected answers or earlier responses.
- Use focused checks for each package. Combined acceptance verifies affected
  resource routes, packaging, behavior, accessibility/owner-motion contracts and
  historical integrity; unrelated passing checks cannot replace missing evidence.
- `DESIGN.md` remains the product handbook. R14 does not invent another product
  questionnaire, decision store, design language, mandatory tool or workflow.
- Keep one execution record when implementation starts, linked from the roadmap,
  with checked revisions, actual commands/results, source/rendered/user evidence
  distinctions, remaining limitations and stage acceptance. Local tools/caches
  stay outside the repository. Do not mark a package complete because its plan exists.
- R14 is complete only when all three packages satisfy their criteria and the
  combined checks. Release numbering, commit/push/merge, publication and managed
  installation are separate delivery work within a later applicable instruction.

## Planning checkpoint verification

Check the new ledger order/count/authority, all local links/anchors, the existing
roadmap-policy tests and release validator. Review the diff to confirm that only
the two planning documents changed. These checks validate the plan's consistency,
not VIEW/CRIT/ICON implementation acceptance. The current automatic roadmap
entrypoint does not yet select R14; VIEW-5 plans that wiring without implementing
it in this documentation-only checkpoint.

Verified 2026-11-02: all 47 existing roadmap-policy tests passed; release metadata
validation passed with version 3.6.1 unchanged. An in-memory call to the existing
shared ledger validator accepted the new R14 order, counts, prerequisites and
authority. All 93 local links/anchors across the two planning documents resolved;
`git diff --check` passed. Only these two documents changed on local branch
`codex/r14-roadmap`; no implementation, commit or remote delivery was performed.
