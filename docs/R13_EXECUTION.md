# R13 execution evidence

This is the accepted implementation checkpoint. The subsequent owner instruction
authorizes [3.6.1 delivery](releases/3.6.1.md#authority); its separate record
supersedes the publication/installation restriction below without rewriting the
original execution evidence.

## Authority

On 2026-11-01 the owner requested R13.1 through R13.4 in order, with the
corrections and tests reported after each stage. This supersedes the planning-only
decision in [the R13 plan](R13_AUDIT_REMEDIATION.md#objective-and-authority).
Scope includes the planned source/test/documentation corrections and existing
synthetic local WordPress hosts. No commit, push, merge, publication or active
Skill installation is included. VERSION remains 3.6.0.

The [roadmap](../ROADMAP.md#r13-audit-remediation) is the sole live ledger.
One implementation writer; independent read-only review and blind behavioral
evaluators support verification. Preserve all original WPS/R11/R12 evidence.

Baseline: `faad3b126e323e566706f6f5dd288cc1e2781c3b`, branch
`codex/r13-audit-plan`. The pre-existing working changes were the approved R13
plan and roadmap. Current Head 1.7.1 and installed UI specialist 3.6.0 verified;
accepted compatibility retained. The unrelated security specialist inventory
warning was preserved; no installed specialist changed. Explicit source/test
tracing supplies the impact map; no dependency graph is claimed.

## R13.1

Actual App-handler regressions reproduced both defects before the correction:
section-error replacement failed (one error instead of two), and a delayed HTTP
endpoint rejection marked the subsequently corrected HTTPS value invalid.
The unchanged-value delayed rejection control already passed.

The correction preserves errors belonging to independent section drafts and
accepts late field errors only for keys/values in the failed submitted section.
Successful acknowledgement clears that section's errors. No server contract,
storage, credential behavior or framework changed.

Independent review reproduced two related paths: a nonce rejection must not
erase a prior field error, and adopting a changed peer value must clear its
obsolete error. Both are corrected and covered by actual-handler regressions.
The reviewer also exercised uncertain reset recovery: default delivery values
clear their obsolete error while an unchanged invalid endpoint retains its own.

Accepted 2026-11-01, ERR-1–ERR-5:

- Five actual-handler validation scenarios pass, together with existing model,
  conflict and discovery checks. Before/after failures are described above.
- [Nine actual-host observations](../evals/wordpress-settings/evidence/r13/validation/r13-validation-results.json)
  cover current English desktop, minimum English narrow and current Persian RTL
  narrow; stored/draft values, associated help, hidden errors, browser back and
  late-response focus are asserted. Persian narrow capture visually reviewed.
- Unchanged runners passed [21 regression observations](../evals/wordpress-settings/evidence/r13/regression/r13-regression-results.json)
  and [11 discovery/workspace observations](../evals/wordpress-settings/evidence/r13/discovery/r12-browser-results.json)
  against the final App bytes. The legacy runner's exact raw report remains next
  to its explicitly labelled execution wrapper; no observations were rewritten.
- 22 WordPress contracts, two R13 evidence tests, 47 roadmap tests and release
  metadata checks pass. Historical fixture records remain unchanged; the
  [R13 successor](../evals/wordpress-settings/r13-fixture-delta.json) allows only
  `app.js` against exact R12 parents. R13 ledger tests cover counts, sequence,
  authority, single active stage and dated acceptance without weakening R12/WPS.
- A discovery run interrupted by an in-flight source correction correctly failed
  its source-stability assertion; it is not acceptance evidence. The final three
  browser runs used fixed source and passed. Initial Temp-permission failures
  were rerun with normal host access; no check was removed.

R13-F02 remains open at this checkpoint. Runtime observation plus independent
review establish this behavior; the old metadata guard alone does not.

## R13.2

Started after R13.1 acceptance. Strengthen producer-specific completion, method
and supported-host/capture checks while retaining valid legacy report contracts.

Accepted 2026-11-01, EVD-1–EVD-5. Before correction, separate in-memory mutations
of completion, partial scope, D10 omission, missing compatibility and source-only
methods all passed. They now fail for the relevant reason. The dedicated R13
error runner also has its own completion and three-cell capture contract;
independent review caught and verified closure of an initial exemption there.

The discovery contract requires its eleven named destinations with their actual
host/language/viewport/view-state identity, direction, theme, host shell and no
overflow. Compatibility versions come from the declared Compose targets, not a
claim about the latest external release. Missing/duplicate/malformed cells,
relabelling, invalid controls, methods, stale hashes and omitted observations are
negative tests. Existing screenshot-byte checks remain active.

22 WordPress contracts, five R13 evidence tests, six historical R12 behavior tests
and 47 roadmap tests pass. Both valid historical and current full reports pass;
the legacy regression producer is explicitly exempt from discovery-only fields
and cannot be promoted to full discovery. CI invokes the new tests. This stage
reused unchanged source-bound browser evidence; validator tests are not a new
browser run. Independent read-only review found no remaining scoped defect.

## R13.3

Started after R13.2 acceptance. The operational component selection paragraph is
moving to the WordPress parent, preserving the settings-only control mandate.

Accepted 2026-11-01, ROUTE-1–ROUTE-4. The parent now owns conditional
DataViews/DataForm selection for real collection/detail/edit work; short settings
keep the existing public-control requirement, and adequate native lists remain
valid. No library, dependency, host or storage contract changed.

Before editing, consumed-resource mapping identified S04 and B01–B05. Each was
rerun independently, plus operational-only O01, using raw requests and frozen
candidate copies with no plans/rubrics/old answers. Full responses were reviewed:
[WordPress cases](../evals/wordpress-settings/r13-stage3-behavior.json) and
[S04 with twelve unchanged retained cases](../evals/ui-foundations/r13-stage3-result.json).
O01 reached the conditional advice without reading either settings module;
B01 retained a compact native-control form, B02/B04 separated hybrid surfaces,
B03 remained audit-only and B05 preserved primary/monolingual approval limits.

23 WordPress contracts, two R13 behavior integrity tests, three source-bridge
tests, 28 foundation harness tests, 16 verdict tests, six historical R12 behavior
tests, 47 roadmap tests and resource/product routing pass. The current 13-case
foundation gate passes. Original R12 records/outputs/release bridge remain exact;
only exact unchanged historical rows may reuse their prior VERSION-only bridge.
Independent review found no broad source waiver. [Stage-three source identity](../evals/r13-stage3-source.json)
binds the full candidate and only the two authorized guide changes.

## R13.4

Started after R13.3 acceptance. In addition to the planned guidance/template
correction, source tracing found the same unconditional dark prerequisite in
`validate_material_sample.py`. Its gate and focused tests are included as necessary
support for this transition; the existing authored sample stays unchanged. This
does not expand Material activation, product scope or runtime implementation.


The same sequence was also repeated in discovery, interactive motion, shadcn,
Material activation and Material component guidance. Only those transition
summaries were reconciled with the canonical gate before freezing the candidate;
no style/provider default changed. The exact source successor includes those
five additional consumed paths.

The R13.4 impact map includes all thirteen selected foundation cases and all six
R13.3 WordPress cases through their shared entrypoint. Each is refreshed from raw
input, plus three new requests for light-only bilingual, required-dark pending
and approved primary-dark behavior. No old response is relabelled as fresh.

The general verification run passed 31 commands, including all existing relevant
contract, package, resource, handbook, sample, runtime, routing and historical
checks. The Material gate suite has eight tests, including missing/contradictory
applicability, stale parents and missing authority; the existing sample remains
unchanged. Both candidate ZIP consumers matched all source files and passed
resource routing. Official local Skill validation passed. These are unpublished
3.6.0-labelled candidate archives, not new published assets or active installs.
The four owned WordPress containers were restored to their original stopped
state after runtime verification; volumes and synthetic data were preserved.

Accepted 2026-11-01, THEME-1–THEME-5. All 22 complete fresh responses were read
and reviewed: [thirteen foundation cases](../evals/ui-foundations/r13-result.json)
and [nine WordPress/theme cases](../evals/wordpress-settings/r13-stage4-behavior.json).
Their exact raw inputs, preparations where applicable, actual response bytes,
independent evaluator identities and consumed-resource lists are retained. The
final foundation record has no retained historical rows or VERSION-only waiver.

- T01 uses the recorded light-only host decision and approved Persian primary
  parent to prepare the already authorized English handoff, without dark work or
  repeated approval questions.
- T02 keeps required, unavailable/unreviewed dark open; later Persian authority
  remains recorded but cannot bypass the theme gate.
- T03 reuses the approved primary-dark treatment and proceeds to the authorized
  Spanish review without a duplicate dark or new light/admin scope.
- B05 keeps its Persian-only primary deliverable and pending actual-host/owner
  review; dark consideration is not silently converted into either an obligation
  or an exemption. O01 reaches operational advice without reading either
  settings-only guide. B01–B04 and the thirteen foundation cases preserve
  component, stack, permission, draft, accessibility, motion and owner controls.

Independent read-only review found no scoped Material-gate blocker. All eight
sample tests passed; seven further invalid-record checks rejected stale decision
or secondary parents, invalid product source/theme and fabricated derived dark
artifacts or approval. Existing approval/authorization checks were retained.
The final two WordPress response-integrity tests, four source-succession tests,
13-case acceptance CLI, 47 roadmap tests, release metadata and resource-routing
checks passed. Local project-document links/anchors and tracked diff whitespace
also passed. These checks validate recorded evidence; they do not run a model or
approve a customer's design.

## Final handoff

All nineteen planned criteria are accepted within the stated scope. No required
R13 implementation or verification item remains open. The sole status ledger is
the [roadmap](../ROADMAP.md#r13-audit-remediation); original WPS/R11/R12 artifacts
and the intermediate R13.3 records remain unchanged.

| Evidence layer | Completed verification and boundary |
| --- | --- |
| Runtime | Five actual-handler validation cases and 41 real-admin observations: nine new error-ownership, 21 existing regression and eleven discovery/workspace observations. Original runner reports remain separate from later guidance changes. |
| Evidence contracts | Positive historical/current records and negative completion, scope, omission, method, host/capture, source and output mutations pass their intended accept/reject checks. |
| Model behavior | Seven independent responses accepted at R13.3, then all affected cases refreshed at R13.4: thirteen selected foundation and nine WordPress/theme responses. Five other foundation requests remain explicitly unexecuted; the 114-case inventory is not claimed as 114 executed evaluations. |
| General checks | 31 local verification commands covered the relevant CI test families; final affected-record, source, roadmap, release and resource checks passed after consolidation. Official local Skill validation also passed. Remote GitHub CI was not run. |
| Packaging | Both unpublished candidate ZIPs passed checksum/CRC/version/content checks; extracted Skill and plugin consumers matched source and passed resource routing. No installed Skill or published asset was replaced. |

The [exact current source](../evals/r13-source.json) is bound by tree SHA-256
`c88607b8b2eccc7a93fdfb17a51905897adbcc8acb269486e8a996ceee724692`.
Unpublished plugin ZIP SHA-256:
`f1698da1a97a39a4914a46981d4488d8c150c72648f827e386a748d822d508af`;
unpublished standalone Skill ZIP SHA-256:
`bdecb0c70e51efe521243b4cd329c54a5bbf01d022c919c5c234fb328cfb78fc`.
These version-3.6.0-labelled archives are local verification candidates only.

Branch `codex/r13-audit-plan` remains uncommitted at
`faad3b126e323e566706f6f5dd288cc1e2781c3b`, with no configured upstream. Its
commit is zero ahead/behind the cached `origin/main` at that same SHA; this is
not a new remote synchronization claim. No R13 PR, commit, merge, release or
active installation occurred. VERSION stays 3.6.0. All four owned synthetic
WordPress/database containers were rechecked as stopped; volumes were preserved.

Evidence remains bounded engineering verification, not new owner visual/font
approval, a human usability study, exhaustive device/assistive-technology testing
or production deployment. Any later authorized delivery must use the existing
exact-head CI, merge/tag, published-download and managed-install checks.
