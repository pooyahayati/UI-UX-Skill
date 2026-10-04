# Behavioral Evals

Structural validation cannot prove that a model follows this Skill well.

The [authored Dispatch Notes comparison](samples/dispatch-notes/README.md) is historical executable R3 output from the superseded simultaneous/multiple-direction workflow. Its draft handbook and bounded rendered evidence do not demonstrate the revised sequential gates. It is not a raw fixture, independent model outcome or approved design; choosing its style is not a maintainer prerequisite. Do not use it as an answer key/input for fresh evaluations.

Version 3.0 provides fixture projects plus scripts that make forward testing repeatable without pretending the model itself ran in CI.

## Validate fixtures

```bash
python3 scripts/validate_eval_fixtures.py
```

## Prepare one run

```bash
python3 scripts/prepare_eval_run.py existing-safe-improvement --output /tmp/uiux-eval
```

The output contains:

- a disposable copy of the fixture when the case uses one
- `RUN.json`
- `PROMPT.txt`

Run the prompt in a fresh Codex/Claude session against the prepared fixture.

## Record results

Record:

- host
- model
- date
- explicit vs implicit trigger
- case result
- every invariant result
- concrete evidence
- regressions/limitations

Use `RESULT_TEMPLATE.md` as the human-readable checklist.

For machine validation, produce JSON matching `result.schema.json`.

## Validate a recorded result

```bash
python3 scripts/validate_eval_result.py result.json
```

For a full candidate run:

```bash
python3 scripts/validate_eval_result.py result.json --require-all
```

This validates completeness/structure. It does not decide whether evidence is truthful.

## Fixture policy

Fixtures intentionally contain known UI/UX and architecture problems.

Do not edit the source fixtures during a run. Use `prepare_eval_run.py` to create a disposable copy.

Current fixtures:

- `existing-dashboard`
- `owner-config`
- `rtl-table`
- `analytics-dashboard`
- `realtime-ops`

## Scoring

Use:

- Pass
- Partial
- Fail
- Not testable

Score observable behavior and evidence, not exact wording.

## Release gate

A candidate should not ship with an unexplained Fail in:

- product-type classification
- required Product Pack loading
- primary/secondary route separation
- local mobile platform-pack routing
- web-application browser/state continuity
- website IA/trust/conversion behavior
- website content/accessibility/performance behavior
- wordpress settings/capability behavior
- wordpress onboarding/integration behavior
- wordpress diagnostics/background-operation behavior
- wordpress multisite/network-admin behavior
- dashboard executive/analytical/operational/monitoring/CRM/admin mode behavior
- shared-rule scope selection after product routing
- shared-rule/product-pack specialization precedence
- shared accessibility/security/data-integrity floors
- design-system token hierarchy and aliases
- component-state completeness and theme matrices
- Light/Dark/High Contrast theme resolution
- Persian/RTL typography-system behavior
- density/responsive/product-variant behavior
- runtime configuration boundary safety

- business-logic preservation
- working-tree safety
- authorization/security boundaries
- arbitrary-code customization boundary
- owner/user config precedence
- invalid-config fallback
- identity-redesign boundary
- trigger boundary
- claims of visual/UX validation without evidence


## R1 adaptive discovery cases

The `discovery-*` cases use raw synthetic inputs in `fixtures/discovery-brief/`. Prepare each with `prepare_eval_run.py`; give future independent evaluators only the case prompt, candidate Skill and raw fixture, not the illustrative responses in `discovery/WALKTHROUGHS.md`.

That walkthrough is a current-session implementation-agent source review, not a fresh model run or customer interview. It is not machine-recorded conformance evidence. Old Stage 6 results do not cover these added cases; full candidate evaluation remains pending. Do not pass `--require-all` on the old five-case result and call that a full candidate run.

## R2 handbook cases and compatibility example

R2's historical local-only limitations below are supplemented by PR #20 CI and the roadmap's integration checkpoint; model/rendered limitations remain.

The `handbook-*` cases use raw `discovery-brief` or `legacy-handbook` inputs. The authored after-artifacts in `handbook/example/` are separate from raw fixtures and must not be given to forward evaluators. `scripts/test_handbook_migration.py` exercises actual fixture parser compatibility (including the broken pointer-only replacement), unchanged token/owner bytes and local after-document links. It does not execute a model or prove an arbitrary product migration.

Prepare new cases in isolated copies. Full candidate conformance, real visual approval and runtime behavior remain pending; revalidating old Stage 6 records does not test these new cases. The example is a current-session source-based mapping with explicit gaps, not an independent agent outcome.

## R3 sequential samples and approval cases

The nine `samples-*` cases use only raw `fixtures/sample-review/` inputs, including previously settled foundation values. The base is English/LTR; the conditional bilingual variant declares Persian/RTL need. Cases activate only named fictional phase records: initial primary, correction, approved-primary dark derivation, post-dark authorized secondary, premature secondary refusal, monolingual skip, stale approval, unavailable rendering and narrow correction. These scoped scenario notes are not current artifacts or approval of newly generated samples. No authored comparison or expected response is part of the fixture.

Prepare each case separately. Observe one professional proposal applying settled palette/font/spacing, product-specific responsive priority, focused corrections and revision linkage; inspect dark-after-primary and owner-authorized secondary-after-dark boundaries, monolingual omissions and stale approval refusal. Inspect executable actions and actual current-phase fonts/layout evidence or missing checks. Score behavior/evidence, not instruction headings. Keep source checks, prepared inputs, fresh model results, rendered proof and real product-owner approval distinct. Preparing cases does not run a model or complete R3; old Stage 6 results do not cover them.

## R4 incremental decisions and handoff cases

Five `incremental-*` cases use raw `fixtures/incremental-design/` inputs: supplied hypothetical h7 handbook, separate token-value authority, scoped owner records and stale contributor feedback. They cover a newly needed treatment of an approved job, reuse without duplicate questioning, strategic appearance preference, stale conflicting return and direct fallback when agent use is unavailable/unauthorized.

The existing preparation regression copies both sample and continuation fixtures byte-exactly, keeps prompts isolated and refuses overwriting existing evidence. It does not execute a model or verify a generated handbook/UI. Observe actual baseline reuse, delta-only changes, necessary questions, authority, stale-return handling and performed versus missing checks in future candidate runs. The [authored continuation source review](incremental/WALKTHROUGH.md) is separate illustrative output, never a raw input/answer key or independent conformance claim.

## Positive executable continuation input

`incremental-executable-baseline` uses the separate frozen `fixtures/executable-baseline/` source/handbook pair and its exact byte binding. The supplied approval/delegation records are explicitly fictional and scoped to these actual inputs, not missing historical artifacts. Preserve the originals and work in an output copy. Generated feedback, revised handbooks, current renders and actual model outcomes are not bundled as answers. Existing missing-original/stale cases are unchanged.

`scripts/test_executable_baseline.py` checks the real pair and rejects changed/missing artifacts, absent scoped identity and untrusted manifest paths. Exact-input preparation includes this new fixture. Those deterministic checks prove only binding/preparation; a fresh continuation response, rendered inspection and lead review remain separate.

## Stage 6 real-world evaluation

The v3 candidate includes five dedicated production-like fixtures and cases:

- Dashboard
- Website
- Web Application
- Mobile Application
- WordPress Plugin

Machine-readable plan:

`real-world/manifest.json`

Recorded result:

`real-world/result.json`

Human-readable summary:

`real-world/RESULTS.md`

Validate with:

```bash
python3 scripts/validate_real_world_evaluation.py
python3 scripts/validate_eval_result.py evals/real-world/result.json
```

The recorded 2026-10-02 run is an in-session source-based ChatGPT / GPT-5.6 Sol evaluation, not an independent fresh Codex/Claude/browser/device run. Do not infer rendered or device validation from that record.
