#!/usr/bin/env python3
"""Offline, package-local resource checks; not a full Markdown or behavior evaluator."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path, PureWindowsPath
import re
import stat
from urllib.parse import unquote, urlsplit

DEFAULT_SKILL = Path(__file__).resolve().parents[1] / "skills/ui-ux-skill"
ROOT_NAMESPACES = ("references/", "assets/", "agents/")
PRODUCT_OUTPUTS = {"DESIGN.md", "design-profile.md"}
# Exact explanatory repository-tool mentions, not portable Skill dependencies.
REPOSITORY_MENTIONS = {
    ("references/material-runtime.md", "scripts/runtime_appearance.py"),
    ("references/specialist-routing.md", "scripts/validate_specialists.py"),
}
INLINE_CODE = re.compile(r"(?P<ticks>`+)(?P<value>.*?)(?P=ticks)")
INLINE_LINK = re.compile(r'''!?\[[^\]\n]*\]\(\s*(?:<([^>\n]+)>|([^\s)]+))(?:\s+["'][^\n]*?["'])?\s*\)''')
FILE_TOKEN = re.compile(r"(?:[^\s`<>*{}]+\.(?:md|json|ya?ml|svg|py|png|jpg|woff2?|ttf)(?:#[^\s]*)?|VERSION)")


def markdown_routes(text: str, source: str):
    """Yield (line, target, root_relative); skip fenced examples and product outputs."""
    fence = None
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not line[marker.end():].strip():
                fence = None
            continue
        if fence is not None:
            continue
        for match in INLINE_CODE.finditer(line):
            target = match.group("value")
            if not FILE_TOKEN.fullmatch(target) or target in PRODUCT_OUTPUTS:
                continue
            if (source, target) in REPOSITORY_MENTIONS:
                continue
            yield number, target, target == "VERSION" or target.startswith(ROOT_NAMESPACES)
        # Literal Markdown inside code spans is an example, not a second route.
        prose = INLINE_CODE.sub("", line)
        for match in INLINE_LINK.finditer(prose):
            yield number, match.group(1) or match.group(2), False


def checked_file(root: Path, source: Path, target: str, root_relative: bool) -> str | None:
    try:
        parts = urlsplit(target)
        if parts.scheme in ("https", "http", "mailto", "tel") or target.startswith("//"):
            return "package-root routes must reference a local resource" if root_relative else None
        if parts.scheme:
            return "unsupported local URI/path"
        name = unquote(parts.path)
        if not name:  # same-document anchor
            return "package-root routes must name a local resource" if root_relative else None
        if "\\" in name or Path(name).is_absolute() or PureWindowsPath(name).drive:
            return "resource paths must be portable and package-relative"
        base = root if root_relative else source.parent
        path = base / name
        resolved = path.resolve()
        if not resolved.is_relative_to(root):
            return "resource escapes the supplied Skill root"
        # Do not let an alias certify bytes outside the consumer package.
        for component in (path, *path.parents):
            info = component.lstat()
            if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
                return "symlink/reparse resource is not a packaged regular file"
            if component == root:
                break
        if not resolved.is_file():
            return "resource is not a file"
    except (OSError, ValueError, RuntimeError) as error:
        return f"missing or unreadable resource ({type(error).__name__})"
    return None


def registry_routes(value):
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "reference":
                if not isinstance(child, str):
                    raise ValueError("reference must be a path string")
                yield child
            elif key == "required_references":
                if not isinstance(child, list) or not all(isinstance(x, str) for x in child):
                    raise ValueError("required_references must be a list of path strings")
                yield from child
            else:
                yield from registry_routes(child)
    elif isinstance(value, list):
        for child in value:
            yield from registry_routes(child)


def validate_resources(skill_root: Path) -> list[str]:
    root = skill_root.resolve()
    errors = []
    if not (root / "SKILL.md").is_file():
        return [f"{root}: missing SKILL.md; supply an actual unpacked Skill root"]

    def check(source, line, target, root_relative):
        issue = checked_file(root, source, target, root_relative)
        if issue:
            errors.append(f"{source.relative_to(root).as_posix()}:{line}: {target!r}: {issue}")

    sources = []

    def walk_error(error):
        errors.append(f"cannot inspect resource tree: {error}")

    for directory, dirs, files in os.walk(root, followlinks=False, onerror=walk_error):
        # Do not traverse directory symlinks/junctions or silently ignore scan errors.
        for name in list(dirs):
            path = Path(directory) / name
            try:
                info = path.lstat()
                if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
                    dirs.remove(name)
                    errors.append(f"{path.relative_to(root)}: symlink/reparse directory is not a packaged resource")
            except OSError as error:
                dirs.remove(name)
                walk_error(error)
        sources.extend(Path(directory) / name for name in files if name.endswith(".md"))

    for source in sorted(sources):
        relative = source.relative_to(root).as_posix()
        if issue := checked_file(root, root / "SKILL.md", relative, True):
            errors.append(f"{relative}: {issue}")
            continue
        try:
            text = source.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            errors.append(f"{relative}: cannot read Markdown ({type(error).__name__})")
            continue
        for line, target, root_relative in markdown_routes(text, relative):
            check(source, line, target, root_relative)

    # Reuse the package's existing registries, not a duplicate module/path inventory.
    for name in ("product-types.json", "shared-rules.json", "design-system.json"):
        source = root / name
        if not source.exists():
            errors.append(f"{name}: missing required resource registry")
            continue
        if issue := checked_file(root, root / "SKILL.md", name, True):
            errors.append(f"{name}: {issue}")
            continue
        try:
            data = json.loads(source.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                raise ValueError("registry must be an object")
            for target in registry_routes(data):
                check(source, "registry", target, True)
        except (OSError, ValueError, UnicodeError) as error:
            errors.append(f"{name}: cannot validate registry ({error})")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill-root", type=Path, action="append", help="repeat for each independent consumer root")
    args = parser.parse_args()
    failed = False
    for root in args.skill_root or [DEFAULT_SKILL]:
        errors = validate_resources(root)
        if errors:
            failed = True
            print(f"Resource route validation failed for {root}:")
            for error in errors:
                print(f"- {error}")
        else:
            print(f"Resource route validation passed: {root}")
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
