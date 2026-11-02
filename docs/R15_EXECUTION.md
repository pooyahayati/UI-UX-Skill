# R15 Execution

## Authority

On 2026-11-02 the owner instructed: implement R15.1 through R15.3 in order.
This supersedes the planning-only checkpoint for the three corrections in the
[R15 plan](R15_AUDIT_REMEDIATION.md), including their regression tests and synthetic
local browser verification. At that checkpoint, commit/push/merge, publication
and updating the installed Skill were outside scope; version 3.7.0 was unchanged.

A subsequent owner instruction on 2026-11-02 explicitly authorized merge, release
and local installation as well. [Delivery authority and evidence](releases/3.7.1.md#authority)
supersedes that earlier boundary for this repository and its managed installation.
[ROADMAP.md](../ROADMAP.md#r15-post-r14-audit-remediation) is the sole progress ledger.

## Baseline and boundaries

- Base commit: `feb4bf199f567be6f2e86e1663c8c3da44a31d24` on `codex/r15-roadmap`.
  The two uncommitted planning documents from the preceding task are retained.
- One implementation writer. No new dependencies or portable Skill guidance edits.
  Existing historical evidence, approved designs/fonts, owner policy and product
  routing remain protected.
- The read-only Context Router selected the browser scope; PHP/WordPress matches
  are adjacent evaluation fixtures, not changed runtime boundaries. Direct source,
  test and evidence inspection covers the affected paths; no graph or installed
  specialist update is needed for these bounded corrections.

<a id="r151"></a>
## R15.1

Accepted 2026-11-02 against JSON-1 through JSON-4.

- Moved the unchanged duplicate-field rule into import-safe `evidence_json.py`.
  R14 evaluation, source and release readers, their retained R13 release path,
  and the accepted-result CLI now use a path-labelled strict reader. The primary
  R14 evidence test loads raw records through that reader, not permissive parsing.
- Raw temporary-file regressions reproduced the original acceptance bug before
  correction (including identical and contradictory duplicates); the CLI already
  rejected duplicates but lacked the record name. The final six regressions pass,
  including nested status, companion records and unchanged canonical formatting.
- Checks passed: `test_eval_result.py` (16), `test_r14_evaluation.py` (3),
  `test_r14_source_binding.py` (3), `test_r14_release_binding.py` (5),
  `test_r13_release_binding.py` (7), `test_behavior_evaluation.py` (28),
  `test_roadmap_policy.py` (54), `test_r15_evidence.py` (6), release metadata,
  and the explicit R14 accepted-result CLI (13 retained cases).
- Reader inventory: `r14_evaluation.errors`, `r14_predecessor`,
  `retained_r13_version_case`, `r14_release_predecessor`, their traversed
  `r13_release_predecessor`, and the five CLI file arguments. Historical report
  bytes/digests, portable Skill files and version are unchanged. CI includes the
  new raw-file regression suite. No fresh model evaluation is claimed.

<a id="r152"></a>
## R15.2

Accepted 2026-11-02 against LIFE-1 through LIFE-4.

- The new real-HTTP browser check failed on the original adapter immediately after
  an observed persisted restoration: clicking left `aria-expanded=false` instead
  of opening the panel. After the fix, four real BFCache cycles passed (open/closed,
  static/selected provider), including pointer, Enter/Space, focus, one activation,
  geometry and OS reduction changed while away. Normal reloads cannot satisfy it.
- Suspension cancels the driver and invalidates pending imports without removing
  the view's listeners/state. Resume re-resolves effective policy; permanent
  teardown remains final. Page lifecycle cancels stale configuration reads.
- Existing plus new browser observations: 16 passed in Edge 156.0.4314.58 at
  390x844. Provider payload remained 9,611 gzip bytes against the existing 16,000
  ceiling. Local raw report: workspace `r15-local/stage2/runtime.json`; R15.3 must
  re-run these checks because it changes the same producer inputs.
- Controlled DOM regressions passed for late provider success after suspension
  and destruction, repeated resume, owner/user/OS off policy, active-driver cleanup
  and settings arriving while suspended. These supplement, not replace, BFCache.
- Preserved seven exact R14 runtime inputs under `evals/r15/r14-runtime-source/`.
  The historical R14 gate explicitly uses that root and its original hashes;
  producer/artifact mutation tests pass. It no longer pretends the old runtime
  report verifies the changed specimen. The current gate is completed in R15.3.

<a id="r153"></a>
## R15.3

Accepted 2026-11-02 against FALL-1 through FALL-4.

- The new cold-start browser regression failed before correction: an open panel
  still had closed path `M7 5L14 12L7 19`. The adapter now starts with the prepared
  outline/plain pair and zero effective motion until configuration is available.
  A catalog-equality test prevents the local default from drifting from the trusted
  `runtime_icons.asset` output; no arbitrary artwork/configuration is introduced.
- HTTP 503 and network failure both passed while initially delayed and after
  failure, including open/close geometry, accessible state, directional RTL and
  zero provider requests. Real BFCache return after failure remained usable.
  Recovery applied solid/badge selection without resetting open state or focus;
  reduced policy and later last-valid retention passed. Status text distinguishes
  the static default, retained appearance and successful loading.
- The final [runtime report](../evals/r15/evidence/runtime.json) records 17 passing
  observation groups, including all four R15.2 cached-navigation cycles. Browser:
  Edge 156.0.4314.58, 390x844 emulation. Payload remains 9,611 gzip bytes under the
  unchanged 16,000-byte budget. The [capture](../evals/r15/evidence/mobile.png) was
  inspected: the open-state icon, visible content and status agree; no clipping.
- The R15 gate requires the complete new observation inventory and details, exact
  current source/provider/artifact identities and strict raw JSON. Its five negative
  regression tests cover missing/duplicate/failed rows, missing or contradictory
  recovery details, producer/archive/artifact changes and duplicate JSON fields.
  Historical R14 report bytes, images and identities remain unchanged.

## Combined review

Accepted 2026-11-02. All twelve numbered plan criteria have scoped evidence above.

| Check | Result |
| --- | --- |
| Combined Python checks | 17 commands succeeded; 186 unittest cases discovered, 183 passed and 3 native file-link cases skipped by the Windows host. Suites include the R15 readers/runtime gate, R14/R13 bindings, behavior/result validation, runtime appearance, resource routes, package safety, roadmap and release metadata. |
| Browser and controlled DOM | 17 real-browser observation groups passed; controlled late-provider, suspension/destruction, owner/user/OS and initial-default regressions passed. |
| Current and historical evidence | New runtime canonical SHA-256 `def8b604d23d7c3c944bec0dcb5317985bef4aa97fc25fdeab573f56fb71d81e`; seven current inputs and mobile capture checked. Seven preserved R14 inputs still match the original report. The old report correctly fails if asserted against changed live producer files. |
| Actual local test packages | Claude ZIP: 92 entries; plugin ZIP: 99 entries. Both exclude evaluation fixtures, archived runtime sources and scripts. Built in disposable scratch space, not published or installed. |
| Final documentation and scope check | All 133 local links/anchors resolved; `git diff --check`, the completed three-stage roadmap and release metadata passed. Protected original inputs were checked unchanged after closeout. |
| Scope | Portable Skill tree, VERSION 3.7.0, provider pin, runtime appearance storage/API and original R14 evidence unchanged. CI adds focused regression/integrity checks; no new dependency or design workflow. |

Historical model evaluations are not new R15 browser evidence. Browser evidence is
limited to the named local Edge emulation, not Firefox/Safari, physical devices,
assistive-technology certification, production or real WordPress acceptance.
The three skipped file-link tests remain recorded limitations, not passes.

At the implementation checkpoint, work was complete locally on `codex/r15-roadmap`, based on
`feb4bf199f567be6f2e86e1663c8c3da44a31d24`. Changes were then uncommitted and unpushed,
with no PR, remote CI, merge, release or installed update. The subsequently
authorized [3.7.1 delivery](releases/3.7.1.md) records those separate gates.
The checks above retain their original pre-release 3.7.0 identity.
