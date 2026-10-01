# Behavioral Evals

Structural validation cannot prove that a model follows this Skill well.

Version 2.1 provides fixture projects plus scripts that make forward testing repeatable without pretending the model itself ran in CI.

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

- business-logic preservation
- working-tree safety
- authorization/security boundaries
- arbitrary-code customization boundary
- owner/user config precedence
- invalid-config fallback
- identity-redesign boundary
- trigger boundary
- claims of visual/UX validation without evidence
