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

Notes are recorded explanations, not machine-verified proof. A reviewer still assesses their justification and evidence. No new acceptance CLI is needed: the existing real-world validator retains its stricter historical evidence/no-failure gate and also uses the shared consistency check. CI runs both checks without promoting the historical subset to a current full run.

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
