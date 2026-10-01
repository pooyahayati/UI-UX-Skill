# How to Install

This document contains installation, update, migration, and verification instructions for **UI/UX Skill**.

## Canonical source

Repository:

`https://github.com/pooyahayati/UI-UX-Skill`

Canonical Skill path:

`skills/ui-ux-skill/`

Machine-readable Skill name:

`ui-ux-skill`

## OpenAI Codex

Install with `$skill-installer` from:

```text
https://github.com/pooyahayati/UI-UX-Skill/tree/main/skills/ui-ux-skill
```

Then invoke:

```text
$ui-ux-skill
```

Example:

```text
Use $ui-ux-skill to classify this product and improve its UI/UX using the required Product Pack.
```

If Codex does not detect the Skill immediately, restart Codex or start a new session.

## Claude.ai / Claude Desktop

1. Open the latest published GitHub Release.
2. Download the Claude-ready Skill ZIP.
3. Upload it from **Customize → Skills**.
4. Enable the Skill.

## Claude Code

Extract the Claude-ready ZIP into either:

```text
~/.claude/skills/
```

or a project-local directory:

```text
<project>/.claude/skills/
```

Then invoke:

```text
/ui-ux-skill
```

## Updating

Always prefer the latest stable version from the canonical repository.

For Codex:

1. Remove the currently installed `ui-ux-skill` if the installer cannot overwrite it.
2. Reinstall from the canonical path above.
3. Restart Codex or open a new session if needed.

For Claude.ai / Claude Desktop, replace the uploaded Skill with the ZIP from the newest published Release.

For Claude Code, replace the installed Skill directory with the newest Claude-ready package.

## Migrating from the legacy slug

Version 2.0 changed the technical Skill slug:

```text
production-dashboard-ui-ux-skill
→
ui-ux-skill
```

If an older installation still uses `production-dashboard-ui-ux-skill`:

1. remove the legacy installed Skill;
2. install from `skills/ui-ux-skill/`;
3. invoke it as `$ui-ux-skill` in Codex or `/ui-ux-skill` in Claude Code.

Do not keep both legacy and current copies installed unless you are intentionally testing migration behavior.

## Verifying the repository

Repository validation:

```bash
python3 scripts/validate_release.py
python3 scripts/validate_eval_fixtures.py
python3 scripts/package_release.py --output dist
```

CI also runs OpenAI's current Skill validator and a real Codex installer smoke test on pushes to `main`.

## Specialist dependencies

This Skill uses modular specialist routing. The machine-readable registry is:

`skills/ui-ux-skill/specialists.json`

For Persian-facing UI, `persian-writing` is REQUIRED and remains an independent Skill:

`https://github.com/ali2000hos/persian-writing`

Do not copy it into this repository. Install or update it from its canonical repository so upstream improvements remain available.

### Codex: install Persian specialist

The current `persian-writing` Skill lives at the repository root. Ask `$skill-installer` to install:

```text
Repository: ali2000hos/persian-writing
Path: .
Install name: persian-writing
```

Codex installs Skills under `$CODEX_HOME/skills` (default `~/.codex/skills`).

### Check specialist sources

Validate the registry only:

```bash
python3 scripts/validate_specialists.py
```

Resolve every specialist against its current canonical upstream source:

```bash
python3 scripts/validate_specialists.py --check-upstream
```

Check a Codex installation against current upstream:

```bash
python3 scripts/validate_specialists.py --check-codex --require-current
```

To require all REQUIRED specialists to be installed as well:

```bash
python3 scripts/validate_specialists.py \
  --check-codex \
  --require-required-installed \
  --require-current
```

You can inspect another Skill installation root with repeated `--installed-root <path>`.

Specialists are never version-pinned in the Head. The checker resolves the latest stable GitHub Release when one exists; otherwise it uses the source repository's current default branch.
