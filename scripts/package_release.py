#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "ui-ux-skill"
LEGAL_FILES = ("LICENSE", "PRIVACY.md", "TERMS.md", "SUPPORT.md")


def reject_links(path: Path) -> None:
    """Reject symlinks and Windows reparse points, including junction ancestors."""
    for item in (path, *path.parents):
        try:
            info = item.lstat()
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
            raise ValueError(f"Refusing symlink/reparse path: {item}")


def validate_output(root: Path, output: str | Path) -> Path:
    raw = str(output)
    if not raw.strip():
        raise ValueError("Output must name a fresh directory")
    candidate = Path(raw)
    if os.name == "nt":
        # Avoid alternate streams, device paths and Win32 spelling aliases.
        if raw.replace("/", "\\").startswith(("\\\\?\\", "\\\\.\\")) or bool(candidate.drive) != bool(candidate.root):
            raise ValueError("Use a fully qualified or ordinary relative output path")
        for part in candidate.parts[1:] if candidate.anchor else candidate.parts:
            if part in (".", ".."):
                continue
            if part.endswith((".", " ")) or any(c in part for c in ':<>"|?*') or re.fullmatch(
                r"(?:CON|PRN|AUX|NUL|COM[1-9¹²³]|LPT[1-9¹²³])(?:\..*)?", part, re.I
            ):
                raise ValueError(f"Unsafe Windows output component: {part!r}")
    if not candidate.is_absolute():
        candidate = root / candidate
    reject_links(candidate)
    out = candidate.resolve()
    if out == root or out in root.parents:
        raise ValueError(f"Output cannot be the repository or an ancestor: {out}")
    # Only the established CI default may live inside the source checkout.
    if out.is_relative_to(root) and out != root / "dist":
        raise ValueError("Inside the repository only a fresh top-level dist is allowed")
    if out.exists():
        raise ValueError(f"Output already exists; choose a new directory: {out}")
    if not out.parent.is_dir():
        raise ValueError(f"Output parent must already exist: {out.parent}")
    return out


def source_files(src: Path):
    reject_links(src)
    if not src.is_dir():
        raise ValueError(f"Missing source directory: {src}")

    def walk_error(error):
        raise error

    for directory, dirs, files in os.walk(src, followlinks=False, onerror=walk_error):
        for name in sorted(dirs):
            reject_links(Path(directory) / name)
        for name in sorted(files):
            path = Path(directory) / name
            reject_links(path)
            if not stat.S_ISREG(path.stat().st_mode):
                raise ValueError(f"Source is not a regular file: {path}")
            yield path


def validate_sources(root: Path) -> tuple[str, str]:
    skill = root / "skills" / SKILL_NAME
    required = [root / "VERSION", root / "plugin.json", skill / "VERSION", skill / "SKILL.md",
                root / "assets/logo.svg", root / "assets/composer-icon.svg",
                *(root / name for name in LEGAL_FILES)]
    for path in required:
        reject_links(path)
        if not path.is_file():
            raise ValueError(f"Missing required package input: {path}")
    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("Repository VERSION must use x.y.z")
    if (skill / "VERSION").read_text(encoding="utf-8").strip() != version:
        raise ValueError("Skill VERSION does not match repository VERSION")
    plugin = json.loads((root / "plugin.json").read_text(encoding="utf-8"))
    if not isinstance(plugin, dict) or plugin.get("version") != version:
        raise ValueError("Plugin version does not match repository VERSION")
    name = plugin.get("name")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z][a-z0-9]*(?:-[a-z0-9]+)*", name):
        raise ValueError("Plugin name must be a lowercase hyphenated slug")
    # Preflight all copied trees before creating output/staging directories.
    for tree in (skill, root / "assets"):
        for _ in source_files(tree):
            pass
    return version, name

def copy_file(src: Path, dst: Path) -> None:
    reject_links(src)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)

def copy_tree(src: Path, dst: Path) -> None:
    for path in source_files(src):
        copy_file(path, dst / path.relative_to(src))

def zip_tree(source_root: Path, zip_path: Path) -> None:
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for path in sorted(source_root.rglob("*")):
            if not path.is_file():
                continue
            arc = path.relative_to(source_root.parent).as_posix()
            info = zipfile.ZipInfo(arc)
            info.date_time = (2026, 1, 1, 0, 0, 0)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, path.read_bytes())

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def build_artifacts(root: Path, out: Path, version: str, plugin_name: str) -> list[Path]:
    skill_src = root / "skills" / SKILL_NAME
    claude_root = out / "claude" / SKILL_NAME
    copy_tree(skill_src, claude_root)
    claude_zip = out / f"{SKILL_NAME}-claude-v{version}.zip"
    zip_tree(claude_root, claude_zip)

    plugin_root = out / "plugin" / plugin_name
    copy_file(root / "plugin.json", plugin_root / "plugin.json")
    copy_tree(root / "assets", plugin_root / "assets")
    copy_tree(skill_src, plugin_root / "skills" / SKILL_NAME)
    for name in LEGAL_FILES:
        copy_file(root / name, plugin_root / name)

    plugin_zip = out / f"{plugin_name}-plugin-v{version}.zip"
    zip_tree(plugin_root, plugin_zip)

    checksums = out / "SHA256SUMS.txt"
    checksums.write_text(
        f"{sha256(claude_zip)}  {claude_zip.name}\n"
        f"{sha256(plugin_zip)}  {plugin_zip.name}\n",
        encoding="utf-8",
    )

    return [claude_zip, plugin_zip, checksums]


def package_release(output: str | Path = "dist", *, root: Path | None = None) -> list[Path]:
    """Build offline in a trusted, stable local hierarchy; never replace output."""
    root = (ROOT if root is None else root).resolve(strict=True)
    out = validate_output(root, output)
    version, plugin_name = validate_sources(root)
    # Only this invocation's random temporary directory can be recursively cleaned.
    # The caller's output path is never passed to rmtree, even on a failed build.
    with tempfile.TemporaryDirectory(prefix=".uiux-package-", dir=out.parent) as temporary:
        staged = Path(temporary) / "output"
        artifacts = build_artifacts(root, staged, version, plugin_name)
        # Catch destinations created while building, including empty directories.
        if validate_output(root, output) != out:
            raise ValueError("Output path changed during packaging")
        staged.rename(out)
    return [out / artifact.name for artifact in artifacts]


def main() -> None:
    parser = argparse.ArgumentParser(description="Build packages without replacing existing files")
    parser.add_argument("--output", default="dist", help="fresh directory under an existing parent")
    args = parser.parse_args()
    try:
        artifacts = package_release(args.output)
    except (OSError, ValueError, RuntimeError) as error:
        parser.exit(1, f"Packaging failed: {error}\n")
    for artifact in artifacts:
        print(artifact)

if __name__ == "__main__":
    main()
