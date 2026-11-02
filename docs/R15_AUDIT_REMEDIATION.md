# R15: Evidence Loading and Icon Specimen Recovery

Prepared 2026-11-02. This is a plan, not implementation or acceptance evidence.
[ROADMAP.md](../ROADMAP.md#r15-post-r14-audit-remediation) is the only live progress
ledger. Execute R15.1, R15.2 and R15.3 in that priority order when authorized.

Historical planning checkpoint: all three stages were subsequently implemented
under the [execution authority and acceptance](R15_EXECUTION.md), then delivered
under the separately authorized [3.7.1 release](releases/3.7.1.md). The original
criteria and planning boundary below remain preserved.

## Objective and authority

Repair the three reproduced post-R14 defects without changing the Skill's purpose,
design workflow, provider-selection rules or settled product decisions.

**Owner decision, 2026-11-02:** update the roadmap with prioritized corrections and
explicit acceptance criteria; do not implement yet. This checkpoint changes only
`ROADMAP.md` and this plan. Code, tests, Skill guidance, fixtures, historical
evidence, dependencies, version metadata and the installed Skill remain unchanged.
Commit/push/merge, release and local installation are not part of this instruction.
Previous R14 delivery authority remains attached to its completed scope.

A later implementation instruction must be recorded in the roadmap and a single
R15 execution record before starting the first package. Use that record for dated
commands, checked revisions, actual observations, limitations and acceptance;
do not create another progress ledger or request settled design/font approvals.

**Superseding instruction, 2026-11-02:** the owner requested R15.1 through R15.3
in order. The [execution record](R15_EXECUTION.md#authority) now owns implementation
and verification authority. The planning checkpoint below remains historical;
delivery and local installation are not included in this instruction.

## Audit baseline and evidence

- Audited release: **3.7.0**, checked local commit
  `feb4bf199f567be6f2e86e1663c8c3da44a31d24` on a clean worktree.
- All three findings are confirmed, **Medium** severity. The two UI defects affect
  the [synthetic icon specimen](../evals/fixtures/icon-morph/README.md), which is
  excluded from the portable Skill. They are not evidence of a deployed-product
  failure. The first finding is a validator rejection gap, not proof of tampered
  current evidence.
- The audit ran 39 existing check-command groups successfully; four platform file-link
  cases were skipped. Strict parsing of 60 current JSON files found no duplicate
  keys. Browser reproductions served unchanged specimen sources with synthetic
  configuration responses; no repository report was rewritten. These observations
  are a defect baseline, not acceptance of the future fixes or a fresh full CI run.

| Finding | Repository evidence and reproduction | Impact / missing coverage |
| --- | --- | --- |
| F15-1: duplicate object fields survive evidence checks | [R14 evaluation tests](../scripts/test_r14_evaluation.py) and [release binding](../scripts/r14_release_binding.py) use ordinary `json.loads`; the existing [result validator](../scripts/validate_eval_result.py) has `unique_object`. In an in-memory copy of `icon-runtime.json`, replace the first `"status": "passed"` with `"status": "failed", "status": "passed"`. R14 `errors(...)` returns no errors and release binding accepts the parsed record; strict parsing rejects it. | Parsing discards the contradictory field before the canonical digest. Dictionary-only mutations cannot test duplicate raw keys. |
| F15-2: cached navigation leaves a dead disclosure | [fixture.mjs](../evals/fixtures/icon-morph/fixture.mjs) destroys the view on `pagehide`; [adapter.mjs](../evals/fixtures/icon-morph/adapter.mjs) removes listeners and permanently marks it disposed. In Edge 156.0.4314.58, open the static specimen, expand, navigate away and go back with BFCache enabled: `pageshow.persisted` is true, only one document request occurred, and the restored control ignores clicks. | No restoration path. The [browser runner](../scripts/test_icon_morph_browser.mjs) checks final cleanup only; a normal reload is not a BFCache regression test. |
| F15-3: cold-start failure leaves a stale state icon | The initial fetch catch in [fixture.mjs](../evals/fixtures/icon-morph/fixture.mjs) changes the status text only; `paint()` in [adapter.mjs](../evals/fixtures/icon-morph/adapter.mjs) returns without an asset. With the first appearance request returning 503, opening the panel changes `aria-expanded` and visibility, but the path stays `M7 5L14 12L7 19` instead of the open state `M5 8L12 15L19 8`. | The state cue contradicts the open panel, while the control and accessible state remain usable. Existing `CONFIG-FAILURE` coverage starts after a successful load and tests last-valid retention only. |

## Protected scope and file boundaries

- Preserve R14 and earlier reports, screenshots, evaluator outputs, acceptance and
  release bindings as historical records. Do not change expected digests, exempt
  source paths or relabel old results simply to make a changed candidate pass.
- Prefer the existing strict parsing rule, prepared icon catalog and lifecycle
  adapter. No new validation framework, appearance engine, UI panel, remote icon
  lookup, arbitrary SVG importer, provider upgrade or dependency is planned.
- Preserve semantic icon assignments, approved families, static unsupported-pair
  handling, RTL directional mirroring, keyboard/focus behavior and truthful state.
  Owner/user/OS motion reduction continues to override decorative motion.
- Preserve runtime appearance storage, permissions, preview/publish/reset/rollback
  contracts, WordPress-native boundaries, dashboard defaults and optional Material,
  Motion, Animate UI, Aria Icons and morphicons selection. Product `DESIGN.md` and
  primary/theme/secondary approval sequencing remain unchanged.

| Package | Permitted implementation area after authorization |
| --- | --- |
| R15.1 | R14 evidence readers and directly traversed companion/source/release loaders in `scripts/`; the existing strict-loader definition or a minimal import-safe shared helper; affected validator tests; narrowly additive R15 ledger validation/tests in `scripts/roadmap_policy.py` and `scripts/test_roadmap_policy.py`. No unrelated parser rewrite. |
| R15.2 | `evals/fixtures/icon-morph/fixture.mjs`, `adapter.mjs`, the existing browser runner and focused lifecycle regression support; bounded specimen documentation and new source-bound evidence. |
| R15.3 | The same specimen/runner, and trusted default artwork initialization in that specimen if required; cold-start/recovery coverage and new combined evidence. No runtime appearance API or persistence change is planned. |

If a changed test entrypoint requires CI wiring, update only the applicable existing
validation step. Keep portable guidance unchanged unless a concrete contradiction
is discovered; record any necessary scope extension before changing it.

<a id="r151"></a>
## R15.1 — Reject ambiguous raw evidence

**Entry:** owner instruction to implement R15.1. **Priority:** first, because later
acceptance depends on trustworthy report loading.

Use one strict duplicate-key rule at file-read boundaries, before semantic checks
or canonical hashing. Reuse the existing `unique_object` behavior through an
import-safe location if sharing it would otherwise execute a CLI or cause a cycle.
Inventory the actual read paths, including companion/source/release records and
test entrypoints; a strict top-level CLI with permissive nested reads is insufficient.

| ID | Observable acceptance |
| --- | --- |
| JSON-1 | Raw duplicate fields, whether equal or contradictory, are rejected at top level and inside nested observations/cases before a successful verdict or digest comparison. The reported failed/passed duplicate reproduction fails. Distinct keys in distinct objects remain valid. |
| JSON-2 | Each R14 evidence-loading entrypoint and its traversed companion/source/release records uses the same rejection rule. File-based regression inputs exercise those real paths, including the release check and accepted-result CLI; passing an already parsed dictionary cannot substitute for this coverage. Failures identify the offending record and key without falsely reporting acceptance. |
| JSON-3 | Unchanged accepted reports remain valid, with the same canonical identities. Existing schema, missing-row, contradictory-value, altered-artifact and source/version checks remain effective. Permitted formatting/key-order differences do not become a new raw-byte hash requirement. No historical report or expected digest is rewritten for this repair. |
| JSON-4 | The existing roadmap validator includes R15's three ordered rows, counts, one-active rule, prerequisites, dated acceptance and separate execution authority. Negative tests reject premature completion or inherited R14 authority. This tracking wiring is not evidence that an R15 package has been implemented. |

**Checks / exit:** add raw-input regressions to the affected existing suites; run
`test_eval_result.py`, R14 evaluation/source/release tests, affected shared-loading
tests, roadmap-policy tests and the accepted R14 result command from current CI.
Record failures on the audited baseline and passes on the corrected candidate.
Keep historical accepted inputs unchanged and review the reader inventory for
remaining permissive paths. Report this package's outcome before starting R15.2.

<a id="r152"></a>
## R15.2 — Restore interaction after cached navigation

**Entry:** accepted R15.1. **Priority:** second, because the reproduced navigation
sequence makes an otherwise visible control unusable.

Distinguish permanent teardown from a persisted page suspension. Stop active motion
and invalidate stale asynchronous work during suspension; restore one working view
on return, preserving the disclosure's actual open/closed state and last valid
appearance. Choose the smallest lifecycle change consistent with existing cleanup.

| ID | Observable acceptance |
| --- | --- |
| LIFE-1 | A real browser navigation away and back restores from BFCache, evidenced by `pageshow.persisted === true`. The control then opens/closes using pointer and keyboard; accessible name, `aria-expanded`, panel visibility, icon geometry and focus behavior remain consistent. A reload or synthetic event alone does not satisfy this criterion. |
| LIFE-2 | Both initially open and closed states survive restoration. Repeated cache-restoration cycles do not add duplicate listeners: one activation causes one state change. The last valid approved appearance remains applied. |
| LIFE-3 | Motion stops during suspension; pending provider work cannot mutate a disposed/suspended view. On restoration, resolve current owner/user/OS policy before any resumed motion. An OS reduction changed while away, and existing owner/user off settings, produce the truthful static/immediate state without an animation flash. |
| LIFE-4 | Non-persisted departure and explicit final destruction still remove listeners and settle/cancel animation. No late import, timer or preference event revives a destroyed view. Existing normal, rapid-interruption, live-reduction and provider-failure behavior continues to pass. |

**Checks / exit:** extend the existing browser runner with actual navigation and
bounded lifecycle checks. Enable BFCache in the test launch (the automation default
may disable it), retain the observed browser version and persisted-event evidence,
and use a navigation wait suitable for cache restoration. If the page is not
restored from cache, diagnose eligibility and leave LIFE-1 unverified; do not count
an ordinary reload as a pass. Record static and selected-provider results against
the corrected specimen source; report acceptance before starting R15.3.

<a id="r153"></a>
## R15.3 — Make the initial static fallback truthful

**Entry:** accepted R15.2. **Priority:** third; the defect affects the visual state
cue while the panel and accessible state continue to work.

Initialize a trusted prepared closed/open pair before configuration resolves.
Use zero motion while effective settings are unknown. Retain last-valid appearance
after later failures and apply recovered configuration to the existing state;
do not reset the user's disclosure or imply that unavailable settings were loaded.

| ID | Observable acceptance |
| --- | --- |
| FALL-1 | In a fresh context with no valid prior configuration, delay the first request and then fail it with 503 or a network error. Opening and closing before and after failure yields matching static geometry, `aria-expanded` and panel visibility. The fallback performs no provider download/animation and uses approved local artwork, with correct directional RTL mirroring. |
| FALL-2 | A later successful reload applies the selected valid family/state pair and effective motion policy to the current open/closed state without resetting it, losing focus, duplicating listeners or briefly showing the opposite icon. Reduced/off policy remains effective during recovery. |
| FALL-3 | Failure after a successful load keeps the last valid approved appearance and state instead of replacing it with defaults. Unsupported pairs and provider failure still use the correct static state. Status text accurately distinguishes unavailable/default, retained and loaded appearance without claiming a save or publication. |
| FALL-4 | Cold failure followed by a real BFCache round trip remains interactive; recovery after return succeeds. Existing appearance, naming, keyboard, motion and bounded mobile checks pass on the final candidate. Record new source-bound runtime evidence and the combined acceptance below; do not reuse an old report as proof of these new scenarios. |

**Checks / exit:** extend the same browser runner for fresh-context failure, delayed
load, recovery, retained-valid behavior and the lifecycle interaction. Use real
DOM/geometry assertions, not status text alone. Run the applicable existing runtime
appearance and icon tests, then the combined checks. Preserve the provider version
and existing payload budget; no new performance target or fresh product approval
is required for this repair.

## Combined acceptance and evidence integrity

- Accept each stage only with its named regression and protected-behavior checks.
  Distinguish unit/source checks, browser observations and historical model outputs;
  unavailable checks stay open. New runtime cases must be required by their evidence
  validator, not optional detail fields that can disappear without failing a gate.
- Record a new R15 runtime result for changed specimen/runner inputs. Bind source,
  runner, provider identity, environment and actual observation inventory; validate
  missing/duplicate/contradictory observations and altered inputs/artifacts. Keep
  the original R14 report and snapshots intact. Use exact-parent successor records
  only where the existing evidence contract requires them, without broad exemptions.
- Verify R15.1 rejection tests and the final icon runner together, plus applicable
  existing validator, roadmap, resource-routing and package-exclusion checks. Run
  the release metadata validator with **3.7.0 unchanged**. Reuse unchanged scoped
  evidence; do not rerun unrelated product designs or model evaluations merely to
  increase test counts. If consumed guidance changes, re-evaluate its affected cases.
- Maintain one execution record and update the roadmap row, completed count,
  active/next package and authority together. The final review must confirm that
  all three original reproductions now pass their expected behavior, historical
  evidence is preserved, and no dependency or workflow expansion occurred.
- Completing R15 is not publication authority. A later applicable delivery
  instruction owns version choice, final source/artifact and security checks,
  commit/push/merge, release and recoverable local installation. None occurs at
  this planning checkpoint.

## Planning checkpoint verification

Validate the two planning documents' links, R15 order/counts/prerequisites/authority
and protected historical ledgers. Run existing roadmap-policy tests and release
metadata validation; inspect the diff for documentation-only changes. These checks
validate the plan, not JSON/LIFE/FALL implementation acceptance.

At the planning checkpoint, the automatic roadmap entrypoint checked through R14. For that checkpoint,
exercise its existing shared ordered-ledger validator against R15 in memory;
JSON-4 schedules permanent wiring after implementation is authorized. No code or
test change is needed to declare the plan ready.

That wiring and all three corrections are now accepted in the
[execution record](R15_EXECUTION.md#combined-review); the checkpoint results below
describe the earlier documentation-only state.

Verified 2026-11-02: all 50 existing roadmap-policy tests and release metadata
validation passed with version 3.7.0 unchanged. The existing shared ledger validator
accepted R15's order, counts, prerequisites and authority in memory. All 117 local
links/anchors across the two planning documents resolved; the 12 numbered criteria
were unique and ordered, and whitespace/scope checks passed. Changes are local on
`codex/r15-roadmap`; only these two planning documents changed. No implementation,
commit, remote delivery or local installation was performed.
