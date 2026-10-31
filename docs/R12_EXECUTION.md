# R12 execution and acceptance

## Authority

The implementation boundary below is historical. The owner's subsequent
[3.6.0 delivery instruction](releases/3.6.0.md#authority) separately authorizes
commit/push/merge, release and the managed local update; this does not change the
six stages' accepted evidence or authorize production-site changes.

On 2026-11-01 the owner instructed execution of R12.1 through R12.6. This
supersedes the [planning-only decision](R12_WORDPRESS_ADMIN_DESIGN.md#objective-and-authority)
for the six bounded packages, including code/guidance edits, relevant tests and
reuse of the owned synthetic WordPress hosts. No push/merge, release, active Skill
installation or production-site change is included. The [roadmap](../ROADMAP.md)
is the only live status ledger.

Baseline: `0f708db4a2eb77f1524903bad1cf8ec1c1e91b15`, released 3.5.1. Branch
`codex/r12-wordpress-admin-plan` began with only the approved roadmap/plan edits.
No unrelated changes were present. One lead owns integration; isolated roadmap
and evidence validators have separately assigned writers. Read-only research and
independent evaluation do not carry delivery authority.

## R12.1

### Inventory and protected behavior

| Task / destination | Intent aliases | Frequency / consequence | Dependency / capability | Default and save scope |
| --- | --- | --- | --- | --- |
| Report identity / `#wps-title` | name, heading; نام گزارش | Occasional / report identity | `manage_options`; nonempty, max 80 characters | `Weekly report`; general section |
| Email delivery / `#wps-enabled` | notification, alerts; اعلان، ارسال | Occasional / changes delivery configuration | `manage_options`; boolean | Disabled; delivery section |
| Recipient / `#wps-email` | recipient, inbox; گیرنده، دریافت‌کننده | Occasional / wrong recipient risk | Delivery enabled; `manage_options` | `reports@example.test`; delivery section; disabling retains value |
| Technical connection / `#wps-endpoint` | webhook, callback; وب‌هوک، وب هوک | Rare / integration address | HTTPS; `manage_options`; secondary disclosure | `https://example.test/hooks/WPS-A2`; advanced section; never fetched |
| Credential action / `#wps-credentialAction` | API key, token; کلید اتصال | Rare / sensitive replacement/removal | `manage_options`; explicit keep/replace/remove | No stored secret; advanced section; stored secret never returned |
| Review a report / workspace list → detail | review, inspect | Repeated / operational reading | Synthetic local records only | No new persistence or customer data |
| Inspect connection / workspace status → configuration | connection health | Recovery / do not equate configured with connected | Existing configuration link; no external request | Demonstration state labelled synthetic |
| Inspect background work / workspace jobs | queued, retry | Recovery / acceptance is not completion | Synthetic local transitions only | No job engine or production action |

Routing examples: a two-field settings form loads settings/components without
search/tabs; multi-topic configuration may add discovery; a jobs workspace loads
operations rules without inheriting the settings-only library mandate; a hybrid
routes each surface separately. An audit makes findings only; a clipped label
repair does not authorize a redesign; public pages and unrelated dashboards keep
their existing product routes.

### Impact and evidence maintenance

The only changed portable Skill resources are the existing WordPress Product
Pack, settings guide and components guide. No new resource inventory/global
registry, other Product Pack or shared policy change is planned. Preserve the
WPS baseline/results, shadcn/motion deltas and R11 records. R12 gets an exact-parent
successor for changed WordPress guides and fixture files, plus fresh real-host
observations. UI-foundations case S04 consumes those guides and must be rerun;
other consumed-source bindings will be checked before deciding reuse.

Keep `wps_specimen_state`, AJAX payloads/option keys, nonces/capabilities, revision
comparison, request identity, secret handling and three-way conflict recovery.
New navigation shares the existing draft; no remount, reload or browser-storage
copy is used to preserve edits. Existing simple/multi fixtures remain available.

The context router reported truncated discovery of `evals/cases.json`; affected
evaluation entries are inspected explicitly rather than inferring no invariants.
Freshness checks found installed Head 1.7.1 and UI Skill 3.5.1 current and compatible;
an unrelated security-specialist inventory warning does not change this scope.

### Checks

Accepted 2026-11-01 for A1.1–A1.4: scoped source tracing of the routing examples
above preserves the settings-only mandate and narrow/audit boundary. Independent
source review corroborated the separate simple/multi/workspace routing and shared
draft contract. `scripts/test_roadmap_policy.py` passes 37 tests, including ten new
R12 cases and all 27 historical cases; an initially changed prerequisite label
was corrected to the declared kickoff contract before acceptance. Explicit JSON
inspection of `evals/cases.json` retained the three WordPress-sensitive scenarios;
consumed-source analysis confirms S04 alone is affected in UI-foundations.

Owned stopped containers were inspected for exact checkout bind mounts, existing
volumes and free loopback ports before restart. Bootstrap observed WordPress 6.8
and 7.1.3, both PHP 8.3.35. These are the fixture's supported hosts, not a claim
that 7.1.3 is today's latest stable WordPress. No customer database/service is used.

## R12.2

Accepted 2026-11-01 for A2.1–A2.4. The discovery variant retains the existing
short/multi specimens and reuses their server/draft model. Curated label/help/alias
search filters capabilities before matching and never indexes saved/draft values.
`test_discovery.cjs`, `test_model.cjs` and `test_conflict.cjs` pass. Real-host
`run_discovery.cjs --settings-only` passed D01–D09 and D11, zero JavaScript errors
or warnings, including alias→field focus, disabled dependency focus, no-result/
clear, browser-back draft retention, edits during delayed save, hidden-group
error focus, denied subscriber mutation with unchanged state, keyboard and both
supported hosts. Initial SearchControl margin deprecation was fixed using its
verified styling-transition flag and rerun successfully.

Partial raw evidence lives in external `r12-local/discovery-run`; its first
`recorded_on` uses UTC 2026-10-31, corresponding to the authorized 2026-11-01
Tehran session. The runner now records both actual UTC instant and Tehran date.
D10 was explicitly omitted, so this was settings-stage acceptance, not complete
R12 runtime acceptance. Final current-source evidence will replace neither this
history nor the old WPS/R11 records.

The Head inspected actual desktop/narrow Persian captures: no clipping/overflow;
the disabled recipient explanation was duplicated and body paragraphs inherited
WordPress's smaller default. These are R12.3 visual refinements, not concealed
runtime failures. No human findability timing or product-owner approval claimed.

## R12.3

Design-source review `r12-design-source-v1` was separately accepted by the Head
with preserved section-save contract; its local S2 gate passed with no unresolved
findings. It covers design analysis only, not rendering or runtime acceptance.
Actual source inspection replaces unavailable local graph evidence (the provider
reported no local graph); no fresh Graphify claim is made.

Accepted 2026-11-01 for A3.1–A3.4: fixture [design decisions](../evals/fixtures/wordpress-settings/DESIGN.md#r12-discovery-and-workspace-extension)
and the component guide now distinguish tested basic controls from conditional
DataViews/DataForm/theme/experimental UI choices. Official sources refreshed;
actual exports, maintained asset metadata, styles and loaded scripts checked on
6.8/7.1.3. No new dependency or runtime migration. The new discovery layout uses
native section composition rather than recommending inspector PanelBody universally.

After fixing duplicate help and paragraph sizing, the ten settings observations
passed again, zero JS errors/warnings, in external `r12-local/stage3-run`.
Head inspected desktop Persian and narrow recipient captures: persistent search
label, clear selected navigation, single focused dependency explanation, local
Vazirmatn, reflow and host chrome preserved. The original simple form remains
without search/tabs. No dark mode, full English host translation, screen-reader
certification or owner visual approval is claimed.

## R12.4

Accepted 2026-11-01 for A4.1–A4.4. The primary Persian discovery page was
rendered/reviewed before extending its scoped foundation to the synthetic
workspace list/detail, connection and job states. The full discovery runner
passed D01–D11 on the exact source, with zero JavaScript errors or warnings.
The Head inspected the actual desktop/narrow pages and stable narrow detail
dialog; its capture waits for finite animations and stable geometry. An initial
workspace configuration initialization error was fixed and the full run repeated.

The report records actual WordPress 6.8/7.1.3 hosts, local Vazirmatn weights,
assets, runner/source hashes and viewport evidence. Operational examples are
explicitly synthetic: configured is not connected, queued is not completed, and
no server job, external service or customer data is introduced. The example
does not claim a production dashboard, owner approval, dark-theme acceptance or
a translated English host. Earlier failed/partial captures remain external
diagnostics. During R12.5, the unchanged legacy suite exposed an explicit
ToggleControl input ID breaking its generated label association. The ID was moved
to a destination wrapper and focus resolves its native input. Both suites were
rerun with named-checkbox, visible-label click and alias-focus checks on both hosts.
Final consolidated discovery attempt-07 is retained in
[the runtime record](../evals/wordpress-settings/evidence/r12-browser-results.json).
Its eleven captures bind actual files and have been visually inspected.

## R12.5

Accepted 2026-11-01 for A5.1–A5.5. The final independent task's
[raw request](../evals/wordpress-settings/R12_TASK.md),
[actual report and captures](../evals/wordpress-settings/r12-task/report.md),
[22-step trace](../evals/wordpress-settings/r12-task/trace.json) and
[reviewed bindings](../evals/wordpress-settings/r12-task-result.json) are retained.
The evaluator received no destination/correction hints and inspected only the
rendered interface. It used the UI's HTTPS guidance, saved sections separately,
retained the title draft and verified all four final values after reload.
One incorrect automation assumption about reload's visible section caused a
timeout; the URL correctly retained delivery and ordinary navigation recovered.
No wrong search destination or lost edit was observed. Continuous visibility of
the report view during a pending request was not proven by that task's captures;
controlled D02/D05 cover the delayed transition separately. These observations
do not claim human usability, improvement over baseline or a timing threshold.

The [five raw behavioral requests](../evals/wordpress-settings/R12_CASES.md) were
given separately to fresh-context evaluators without the plan, criteria or old
outputs. The lead read the actual responses and accepted all ten recorded
criteria in [the bound result](../evals/wordpress-settings/r12-behavior-results.json):

| Coverage | Actual reviewed evidence |
| --- | --- |
| Short form | B01 retains two native controls, existing Settings API/encodings and no unnecessary navigation/search. |
| Hybrid discovery | B02 separates settings/report/operations, maps webhook aliases to field/dependency focus, preserves section drafts and uncertain-save boundaries. |
| Audit scope | B03 proposes bounded investigation, no implemented redesign or forced legacy-control/table migration. |
| Component compatibility | B04 rejects blanket new-package imports and separates the short form from a large paginated collection. |
| Visual sequence | B05 reuses settled Persian foundations, one primary responsive proposal, later conditional dark review and no unsolicited English variant or claimed rendering. |

Fresh [S04 output](../evals/ui-foundations/outputs/S04-r12.md) satisfies both
original criteria. Its [successor suite](../evals/ui-foundations/r12-result.json)
keeps twelve unchanged historical cases and the old top-level candidate intact;
only S04 has a fresh full snapshot, preparation/output bindings and distinct
output file. The old results remain untouched. This is six new model responses
across the two evaluations, not thirteen freshly rerun foundation cases.

The first independent browser task completed with retained drafts and saved
values but exposed generic validation text replacing the useful HTTPS help.
The fixture now retains that help and provides persistent error links after
navigation. A separate code review found automatic error reveal leaving the old
URL section, and keyboard activation losing focus when workspace buttons were
removed. Both were reproduced/corrected; final D05/D10 verify URL, help, links
and stable focus. The doubled search accessible name was also corrected.
The lead retained earlier observations outside source and requested a new
fresh-context raw task on the final source, without supplying its solution.
A final conditional-field review also found a replacement-credential error
surviving a later keep/remove choice. The fixture clears that obsolete field
error, including a delayed response, while preserving the user's current choice;
the browser regression checks the actual rendered error destination.

Protected regression evidence: [21 fresh legacy observations](../evals/wordpress-settings/evidence/r12-regression-results.json)
and [11 discovery/workspace observations](../evals/wordpress-settings/evidence/r12-browser-results.json)
pass with zero JS errors/warnings. The legacy runner is unchanged. Historical
parents and the exact three-guide/five-fixture-path successor remain bound;
22 contract tests include actual screenshot identity. Five behavior-integrity
tests reject changed candidates/requests/outputs, reused contexts and missing
reviews, and bind the independent task/report/images to current source. All 21 foundation-harness regressions pass without skips, including
the per-case successor's stale-source/output and path-containment negatives.

### Combined verification inventory

The delegated local workflow check ran 32 effective commands successfully:
release metadata; source/product/shared/design/specialist routes; handbook,
sample, Material, runtime appearance, package, evaluation and recovery checks;
real-world historical compatibility; raw-run preparation; and both extracted
consumers. Those Python suites reported 130 passes and four explicit skips;
the DOM suites separately passed eleven dialog assertions and eleven recovery
scenarios. The lead additionally runs the current R12 roadmap, evidence and
behavior checks. This is local Windows verification, not remote GitHub CI.

The four skipped existing tests require native symlink creation unavailable to
this Windows token: one resource-route case, two packaging cases and one
specialist case. They remain enabled and unmodified for supported hosts/CI;
no pass is claimed for them. The changed foundation-harness containment tests
all ran. Earlier temporary-directory permission errors were rerun successfully
with the required access. Official quick validation initially lacked PyYAML;
unchanged source and both consumers passed using already installed PyYAML 6.0.2
through a per-process path, without installing or modifying a validator.

Both locally built candidate archives pass checksum, CRC, exact canonical
source/license identity, version and extracted resource routes. The installed
official quick validator passes all three roots (source, standalone, plugin).
These are unreleased validation builds carrying the unchanged 3.5.1 metadata,
not the published 3.5.1 assets or an installation:

| Candidate archive | SHA-256 |
| --- | --- |
| Standalone, 92 members | `03a81b20336c700bf14e3e24761a8e8a7010f2ea63e125ee3b6533ddb493e6bf` |
| Plugin, 99 members | `6cb3c8164e7c7497304b4f4c094f579402e1ca18c42581a43cb10d6ba21064dd` |

Raw machine-specific command logs, initial failures, source-stage review receipts,
package extractions and temporary credentials stay outside the repository in the
local R12 work area. Selected portable evidence is linked above. No external
service, new production dependency, latest-core certification, physical-device,
screen-reader, dark-mode or human usability claim is made.

## R12.6

Accepted 2026-11-01 for A6.1–A6.4. Each A1–A5 group has dated acceptance above;
the current roadmap remains the only live completion ledger. README, changelog,
fixture/evaluation instructions and CI point to the actual R12 behavior and
successor evidence. Existing historical WPS/R11 records remain immutable.

The 32-command inventory and candidate archives above were checked locally;
the lead's final checks cover 37 roadmap cases, 22 WordPress evidence contracts,
five R12 behavior/task integrity cases, the current 13-case foundation successor,
model/conflict/discovery regressions, release metadata and changed-document local
links. The full browser checks cover both supported synthetic hosts. All required
R12 outcomes have evidence; the four unchanged Windows symlink cases remain
explicitly unexecuted locally and enabled for a capable CI host.

At the implementation handoff: branch `codex/r12-wordpress-admin-plan`, HEAD
`0f708db4a2eb77f1524903bad1cf8ec1c1e91b15`; recorded `origin/main` is the same
revision (0 ahead / 0 behind against that local ref, not a live remote freshness
claim). Changes are uncommitted and unpushed. No new PR, CI run, merge commit,
tag, release, installation or production change was created. The released and
installed baseline remains 3.5.1. No local graph existed; explicit source/test
tracing supplied the impact review rather than a Graphify-freshness claim.

No additional R12 implementation remains after the passing final ledger validation.
The four owned fixture containers were returned to their initially stopped state
after the final evaluator closed its browser; volumes/data were retained. The
fixture README documents restart and preview entrypoints. No unrelated container
was changed. Authored source and documentation pass Git-normalized whitespace
checks; the delivery review retains final blank lines in three immutable raw
model outputs to preserve their recorded identities.
The subsequent [delivery record](releases/3.6.0.md) owns current integration,
publication and installation evidence under the owner's separate authorization.
