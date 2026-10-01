# Contributing

Contributions to **UI/UX Skill** are welcome.

## Canonical source

The Skill has one source of truth:

```text
skills/production-dashboard-ui-ux-skill/
```

Do not add duplicate root copies of `SKILL.md`, `agents/`, or `references/`.

Release packages are generated from the canonical folder by `scripts/package_release.py`.

## Good contribution areas

- production dashboard UX patterns
- existing-product audit and regression behavior
- design-system architecture and changeability
- runtime design governance
- safe owner-only appearance controls
- user personalization and saved views
- Data Trust UX
- role-aware operational UX
- Persian RTL and bilingual localization edge cases
- accessibility
- frontend performance
- responsive dashboard behavior
- tables, forms, filters, navigation, and charts
- design-system consistency
- Light/Dark edge cases
- local typography and Persian/Latin pairing
- safe working-tree behavior
- removal of generic AI-generated UI patterns

## Contribution principles

Changes should improve agent decisions without making the Skill unnecessarily rigid.

Prefer:

- reusable principles over one-off fixes
- product outcomes over visual trends
- a concise `SKILL.md`
- conditional detail in `skills/production-dashboard-ui-ux-skill/references/`
- preserving user intent and functional contracts
- observable QA criteria
- explicit trigger boundaries
- bounded configuration over arbitrary runtime code
- clear separation of owner defaults, user preferences, and protected constraints

Avoid:

- adding a rule for every isolated example
- turning one visual preference into a universal requirement
- duplicating instructions across multiple files
- large generic UI tutorials
- framework-specific requirements unless genuinely necessary
- runtime appearance controls that can bypass authorization or execute arbitrary code

## Before opening a pull request

Run:

```bash
python3 scripts/validate_release.py
python3 scripts/validate_eval_fixtures.py
python3 scripts/package_release.py --output dist
```

CI also runs OpenAI's current Skill quick validator.

For material behavior changes, prepare and run forward tests from `evals/` using `scripts/prepare_eval_run.py`, then validate recorded JSON results with `scripts/validate_eval_result.py`.

## Pull requests

Explain:

1. the problem or failure mode
2. the proposed change
3. why it belongs in the entrypoint or a specific reference
4. compatibility implications
5. relevant behavioral eval results

Keep unrelated changes separate.
