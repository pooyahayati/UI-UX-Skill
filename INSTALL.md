# How to Install / Update

Canonical source: [pooyahayati/UI-UX-Skill](https://github.com/pooyahayati/UI-UX-Skill), directory `skills/ui-ux-skill/`, Skill name `ui-ux-skill`.

Prefer the [latest stable release](https://github.com/pooyahayati/UI-UX-Skill/releases/latest) for routine installation. Use a named commit only when intentionally testing development source.

## Codex

Ask `$skill-installer` to install `skills/ui-ux-skill` from the canonical repository at the latest stable release tag.

Repository path for discovery:
https://github.com/pooyahayati/UI-UX-Skill/tree/main/skills/ui-ux-skill

Invoke with `$ui-ux-skill`, for example: “Use $ui-ux-skill to inspect this product and improve the affected form without changing its workflow.”

Skills normally live under `$CODEX_HOME/skills` (default `~/.codex/skills`). The installed Skill root must contain `SKILL.md` and `VERSION`; the source version file is `skills/ui-ux-skill/VERSION`. Read the local file for installed-version questions, not the repository branch or latest-release label. The Skill is available on the next turn.

## Claude

- **Claude.ai / Claude Desktop:** download the Claude-ready Skill ZIP from the stable release, upload under **Customize → Skills**, then enable it.
- **Claude Code:** extract the ZIP into `~/.claude/skills/` or `<project>/.claude/skills/`; invoke `/ui-ux-skill`.

## Safe updates and legacy migration

1. Resolve the current stable tag and download/install into a separate staging directory. Verify version, source identity, archive integrity/checksums and required resources before touching the active copy.
2. Preserve any local customization or engineering-Head integration. If the Skill is managed by a Head, use its authorized update path rather than discarding its contract.
3. Move the existing directory to a clearly named backup **outside auto-discovered Skill directories**, then place the verified replacement at the canonical path. On failure, restore the backup. Retain it until the new copy is verified.
4. Verify the installed `VERSION`, manifest and resources. Replace the uploaded package similarly for Claude.ai/Desktop; replace the verified directory for Claude Code.

Do not delete a working installation before its replacement is verified.

Version 2.0 renamed `production-dashboard-ui-ux-skill` to `ui-ux-skill`. For a legacy installation, verify the new nested Skill first, back up the old copy outside discovery paths, and use the new invocation. Avoid two active copies unless intentionally testing migration.

## Persian specialist

For Persian-facing UI, `persian-writing` is REQUIRED and remains independent; do not vendor it into this repository.

Ask `$skill-installer` to install from [ali2000hos/persian-writing](https://github.com/ali2000hos/persian-writing), path `.`, install name `persian-writing`. Sources/triggers are in [specialists.json](skills/ui-ux-skill/specialists.json); specialist versions are not pinned.

From the repository root:

```bash
python3 scripts/validate_specialists.py
python3 scripts/validate_specialists.py --check-upstream
python3 scripts/validate_specialists.py --check-codex --require-required-installed --require-current
```

Use repeated `--installed-root <path>` to inspect another root. The checker resolves stable release or current default branch; an unavailable check is not proof of freshness.

## Repository checks and publication

```bash
python3 scripts/validate_release.py
python3 scripts/validate_eval_fixtures.py
python3 scripts/package_release.py --output <new-external-output-directory>
```

The packager requires a **nonexistent destination with an existing parent**. It refuses existing files/directories (even empty ones), repository/ancestor/source paths and symlink/junction paths. Choose a new output name for each run; there is no overwrite/force option. CI also runs the official quick validator and a temporary Codex installer smoke test on main pushes; this does not update the owner's installed copy.

### Packaging safety and limits

- Prefer an absolute external destination. Relative paths resolve from the repository root; only a fresh top-level `dist` is permitted inside it for existing CI consumers. The parent must already exist; the command does not create missing ancestor directories.
- Required package inputs, repository/Skill/plugin version agreement and copied source trees are checked before staging. Source symlinks and Windows reparse points, including junctions, are refused rather than followed.
- Archives and checksums are built in an invocation-owned temporary sibling. Only the complete staged directory is renamed to the requested destination. Detected copy/archive/checksum/publication failures preserve earlier outputs and source files; cleanup targets only the owned staging directory, never the requested output.
- Use trusted local source and destination-parent directories that cannot be changed by another actor during the command. Path validation and a final existence check do **not** provide descriptor-based protection against hostile concurrent ancestor swaps; on POSIX a rename can also race with another process creating an empty destination. Shared/untrusted mutable hierarchies are unsupported. An interrupted process may leave its temporary staging folder; inspect it before any manual cleanup.

### Publication

After authorized, validated changes reach `main`, the release workflow reads `VERSION`, builds Skill/plugin ZIPs and `SHA256SUMS.txt`, and creates `v<version>` only if its release does not exist. Existing releases are skipped, not overwritten. Do not create a competing tag for the same version. See [current status](ROADMAP.md).
