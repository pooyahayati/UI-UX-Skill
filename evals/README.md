# Behavioral Evals

Structural validation does not prove model behavior, rendered quality or owner approval. See [current stage status](../ROADMAP.md); superseded pending notes remain in the [dated evaluation-guide archive](../docs/archive/EVALS-2026-10-06.md).

## Run and record a scoped evaluation

From the repository root:

```bash
python3 scripts/validate_eval_fixtures.py
python3 scripts/prepare_eval_run.py existing-safe-improvement --output <new-external-run-directory>
```

Preparation produces an isolated fixture copy, `RUN.json` and `PROMPT.txt`. It does not run a model. Use a fresh permitted session with only the case prompt, candidate Skill and named raw inputs; never supply authored walkthroughs, prior findings or expected invariants as an answer key.

Record host/model/date, actual candidate revision, explicit/implicit trigger, per-case/per-invariant outcomes, concrete evidence and limitations. Use [RESULT_TEMPLATE.md](RESULT_TEMPLATE.md) and [result.schema.json](result.schema.json).

```bash
python3 scripts/validate_eval_result.py <recorded-result.json>
python3 scripts/validate_eval_result.py <recorded-result.json> --require-all
```

Use `--require-all` only for a genuinely complete current-manifest run. The historical five-case record is not a full current-candidate run. Validation checks structure, completeness and internal consistency, not truthful evidence or release acceptance. Exit code 0 permits a coherent recorded failure; exit code 1 means malformed, contradictory or (with `--require-all`) incomplete input. Summaries include all four verdict counts and recorded/current case coverage.

### Verdict consistency

Each recorded case must contain every manifest invariant exactly once, using its exact text. Unknown/duplicate cases, unknown/duplicate invariants and duplicate JSON fields are rejected; omitted cases are allowed only without `--require-all`. Empty reports are not evaluations. The schema describes the JSON shape; `validate_eval_result.py` additionally enforces manifest identity and these cross-record rules:

| Case result | Required invariant outcomes |
| --- | --- |
| `pass` | All `pass`; notes cannot excuse a failed, partial or untested requirement. |
| `fail` | Any `fail` requires this case result. A conservative case-level failure without a failed invariant is allowed only with nonblank case `notes` explaining the additional failure. |
| `partial` | No `fail`, with at least one `partial`, or a mixture of `pass` and `not-testable`. If every invariant passed, nonblank case `notes` must explain the additional limitation. All-untested requirements cannot be called partial. |
| `not-testable` | Every required invariant is `not-testable`; do not hide tested outcomes. |

Notes are recorded explanations, not machine-verified proof. A reviewer still assesses their justification and evidence. The real-world validator retains its stricter historical evidence/no-failure gate and the shared consistency check. Its original result/version stays unchanged; [compatibility.json](real-world/compatibility.json) separately binds the exact historical JSON and current case inventory. The generic validator requires `--binding evals/real-world/compatibility.json` for that record; unbound version mismatches still fail. This does not promote the historical subset to a current run.

### Selected independent UI-foundation suite

The [selection manifest](ui-foundations/manifest.json) freezes 13 of the 18 existing shadcn/motion requests and 27 reviewer criteria, covering all six R11 decision families. Five exact prompts remain explicitly unexecuted. This is separate from the 114-case general inventory, not 114 passing executions.

```bash
python3 scripts/prepare_eval_run.py S01 --suite ui-foundations --output <fresh-external-case-directory>
python3 scripts/test_behavior_evaluation.py
python3 scripts/test_r13_source_binding.py
python3 scripts/validate_eval_result.py evals/ui-foundations/r13-result.json --suite ui-foundations --accept --r13-release-binding evals/r13-release-version.json
```

Provide a fresh evaluator only `evaluator/PROMPT.txt` and `evaluator/skill/`, plus required routed external specialization. `RUN.json`, the selection manifest, prior outputs and review notes stay outside its allowed inputs. Preparation checks exact prompt/candidate bytes and rejects extra files in the input tree; it is an integrity check, not a sandbox preventing an agent from reading elsewhere.

Retain the actual response and a consumed-resource list. Review decisions against the withheld criteria, recording concrete evidence for every outcome. The [result record](ui-foundations/result.json) binds raw inputs, preparation/rubric, actual output, candidate tree and declared per-case source dependencies; changes to consumed sources invalidate affected cases. Shared entrypoint/version/routing changes invalidate all selected cases; resource inventory changes also require review. Review the mapping if an unread resource becomes relevant: hashes cannot determine semantic impact or prove read history.

The ordinary validator permits coherent failed/partial/untested records. `--accept` additionally requires all selected cases and passing required outcomes with matching output/source evidence. CI checks these saved records and focused negatives; it does not rerun a model, make paid calls, certify application runtime behavior or approve a visual design. Lead acceptance still requires reading the actual responses. See the [execution record](../docs/R11_EXECUTION.md#r113) for invocation, environment and limits.

R12's [successor record](ui-foundations/r12-result.json) contains one fresh S04
response and twelve unchanged historical case records. A paired per-case
`candidate` snapshot and distinct `outputFile` bind the new response without
rewriting the historical top-level candidate or output. All current consumed
resources must still match; an override is not a stale-source exemption.
The [original result](ui-foundations/result.json) remains historical. Separate
[R12 raw requests and reviewed outputs](wordpress-settings/README.md#historical-r12-evidence)
cover five WordPress design decisions; neither suite claims customer implementation.

The [3.6.0 release binding](r12-release-version.json) preserves those original
outputs and candidate identities across the canonical `VERSION`-only bump.
It binds the exact prior/current full trees and retained result contents;
changed guidance, inventory, raw requests, outputs or preparation still fail.
This is explicit metadata compatibility, not a new model or browser run.

The current [R13 record](ui-foundations/r13-result.json) is separate from those
historical records. R13.3 refreshed S04; its [intermediate record](ui-foundations/r13-stage3-result.json)
retains twelve exact older rows under their narrow VERSION-only compatibility.
R13.4 changes the shared entrypoint and therefore refreshes all thirteen selected
responses. [R13 source succession](r13-source.json) checks the entire current tree
and explicitly allowed changes against the exact released predecessor; historical
checks remain separate. The [execution record](../docs/R13_EXECUTION.md) owns
semantic acceptance, commands and limitations. Read lists are self-reported;
neither source hashes nor structural validation establish model truth.

The [3.6.1 metadata bridge](r13-release-version.json) verifies the complete
VERSION-only successor and the exact retained final R13 reports. Current CI
supplies it explicitly; the ordinary CLI still rejects a version/source mismatch.
This is release compatibility, not a new model or browser evaluation.

## Inputs versus examples

[cases.json](cases.json) is the current case/fixture inventory. Raw fixtures intentionally contain problems; do not alter them during evaluation. Prepare a disposable copy and obey each case's named input/phase records.

| Workstream | Raw inputs | Separate examples / evidence |
| --- | --- | --- |
| Discovery / handbook | [discovery brief](fixtures/discovery-brief/README.md), [legacy handbook](fixtures/legacy-handbook/README.md) | [Discovery walkthroughs](discovery/WALKTHROUGHS.md), [handbook example](handbook/example/DESIGN.md): authored, not interview/model/approval proof |
| Sequential samples | [sample review](fixtures/sample-review/README.md) | [Sequential forward review](samples/SEQUENTIAL_FORWARD_REVIEW.md); historical [Dispatch Notes](samples/dispatch-notes/README.md) comparison is superseded, not an approved design or raw input |
| Incremental handoffs | [incremental design](fixtures/incremental-design/README.md), [frozen executable baseline](fixtures/executable-baseline/README.md) | [Authored walkthrough](incremental/WALKTHROUGH.md), [forward review](samples/INCREMENTAL_FORWARD_REVIEW.md): keep provenance distinct |
| Runtime appearance / icons / fonts | [raw appearance requests](fixtures/runtime-appearance-brief/README.md) | [Executable fixture](fixtures/runtime-appearance/README.md), [runtime planning review](samples/RUNTIME_FORWARD_REVIEW.md), [icon review](samples/ICON_FORWARD_REVIEW.md), [font review](samples/FONT_FORWARD_REVIEW.md) |
| Integrated R7 / R8 | Named raw inputs above | [Integrated quality](samples/INTEGRATED_QUALITY_REVIEW.md), [five-route review](samples/ROUTE_FORWARD_REVIEW.md), [candidate readiness](samples/CANDIDATE_READINESS.md) |
| Optional Material | [activation](fixtures/material-activation/README.md), [foundations](fixtures/material-foundations/README.md), [components](fixtures/material-components/README.md), [samples](fixtures/material-samples/README.md) | [R9 acceptance](material/R9_6_ACCEPTANCE.md), [six-case review](material/R9_6_FORWARD_REVIEW.md), [proposed specimen](material/ham-amooz/DESIGN.md) |
| shadcn/ui and interactive motion | [shadcn requests](shadcn/CASES.md), [motion requests](motion/CASES.md) | [shadcn source review](shadcn/REVIEW.md), [motion source review](motion/REVIEW.md): source/scenario and package checks, not fresh model/browser runs |
| Historical five-product evaluation | [manifest](real-world/manifest.json) | [Method/limits](real-world/README.md), [results](real-world/RESULTS.md), [recorded JSON](real-world/result.json) |

Fictional approval records authorize only their named fixture phase; they do not approve a newly generated sample or real product. Preserve original inputs, byte bindings and earlier failed/unavailable evidence.

The authored handbook files are replacement snippets for a prepared legacy fixture, not a standalone product folder. Their `OWNER.md` and `ui-tokens.json` links resolve after combining them with the [raw legacy inputs](fixtures/legacy-handbook/README.md), as exercised by `scripts/test_handbook_migration.py`; do not duplicate those value/provenance files into the example folder.

## Scoring and protected gates

Score observable behavior/evidence as Pass, Partial, Fail or Not testable, not exact wording. Do not ship unexplained failures in:

- product classification, required/forbidden pack/module scope and genuine multi-route/platform behavior;
- relevant website, dashboard, browser-workflow and WordPress capability/data-lifecycle behavior;
- Shared Rule specialization and accessibility/security/data-integrity floors;
- token hierarchy, aliases, component states, themes, typography/direction and responsive density;
- safe owner/user precedence, invalid-config recovery and arbitrary-code boundaries;
- business logic, permissions, user-authored changes, scope/trigger authority and honest evidence reporting.

## Retained evidence limits

- Historical 2026-10-02 five-product results are source-based, in-session observations, not fresh independent browser/device runs. Later structural rebinding (including 3.3.0) does not rerun the model.
- Later scoped forward/manual/browser/runtime results have their own candidate bindings and methods. Five routes or six Material cases do not imply all current cases ran.
- R9 preserves F01 reference-order and shared-session/device/assistive-technology limits. The Material specimen remains proposed, dark unstarted, secondary N/A.
- Engineering stage acceptance does not approve customer taste, certify every production parser/runtime, implement arbitrary font uploads or prove real-device accessibility. Preserve accepted owner/font evidence; do not reopen it without a concrete defect.
