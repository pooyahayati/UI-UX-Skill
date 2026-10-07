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

Use repeated `--installed-root <path>` to inspect other roots. This is a read-only checker: it never installs, overwrites, deletes or executes specialist files.

### Specialist package integrity

The checker resolves the latest stable release (or default branch only when no stable release exists) **once to an immutable commit**. It reads that commit's Git tree under the registry's `skill_path`, including every tracked file in that package subtree. Sibling packages are excluded. A registry path of `.` explicitly declares the repository root as the package, so its tracked supporting files are included. No archive extraction or resource-code execution is involved.

Local raw bytes are compared using Git blob identities, including binary assets and line endings; matching only `SKILL.md` is insufficient. File executable permissions are not compared across hosts. The result separately reports entrypoint match, package state and observed upstream commit:

- `CURRENT`: all declared package paths/bytes match, with no uncertified additions.
- `DIFFERS`: missing or modified upstream-owned files; this does not infer whether the cause is age, deliberate customization or corruption.
- `UPSTREAM_MATCH_WITH_ADDITIONS`: upstream-owned files match, but local additions (including a Head contract) are not certified.
- `MISSING` / `UNVERIFIED`: absent installation, unsupported links/types, unreadable files or unavailable upstream evidence. Neither means current.

Both strict flags require an explicit target via `--check-codex` or `--installed-root`. `--require-required-installed` requires a valid named entrypoint in **each** inspected root; it does not certify the other resources. `--require-current` additionally requires exact package identity/presence in **each** root for required specialists. One valid copy never certifies a different broken copy. Without strict flags, known differences/missing copies are reported without failing the registry check; unavailable/malformed checks still exit nonzero.

Local additions are retained and listed. Modified upstream files, including Head-edited `SKILL.md`, are never silently normalized or waived. Use the engineering Head's own integration-aware verification when applicable; a failed exact-match check does not authorize overwriting customization. Only untracked Git metadata and Python runtime caches are excluded from comparison, never missing required upstream files.

Limits per package: 10,000 tree/scan entries, depth 32, 32 MiB per file, 128 MiB total local/upstream file bytes, 1 MiB entrypoint and 8 MiB per API response; requests have a 20-second timeout, no redirects or automatic retries. Traversal/Windows aliases, case collisions, symlinks/junctions and submodules are unsupported, not accepted as current. Inspect trusted stable local directories: this is a point-in-time check, not a filesystem snapshot or protection against hostile concurrent ancestor/file replacement. An upstream update after commit resolution requires a new check; no persistent version pin is added.

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
