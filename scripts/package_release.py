#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "ui-ux-skill"
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()

def copy_file(src: Path, dst: Path) -> None:
    if src.is_symlink():
        raise RuntimeError(f"Refusing to package symlink: {src}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)

def copy_tree(src: Path, dst: Path) -> None:
    for path in sorted(src.rglob("*")):
        if path.is_symlink():
            raise RuntimeError(f"Refusing to package symlink: {path}")
        if path.is_file():
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

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="dist")
    args = parser.parse_args()

    out = ROOT / args.output
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)

    skill_src = ROOT / "skills" / SKILL_NAME

    claude_root = out / "claude" / SKILL_NAME
    copy_tree(skill_src, claude_root)
    claude_zip = out / f"{SKILL_NAME}-claude-v{VERSION}.zip"
    zip_tree(claude_root, claude_zip)

    plugin_name = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))["name"]
    plugin_root = out / "plugin" / plugin_name
    copy_file(ROOT / "plugin.json", plugin_root / "plugin.json")
    copy_tree(ROOT / "assets", plugin_root / "assets")
    copy_tree(skill_src, plugin_root / "skills" / SKILL_NAME)
    for name in ["LICENSE", "PRIVACY.md", "TERMS.md", "SUPPORT.md"]:
        copy_file(ROOT / name, plugin_root / name)

    plugin_zip = out / f"{plugin_name}-plugin-v{VERSION}.zip"
    zip_tree(plugin_root, plugin_zip)

    checksums = out / "SHA256SUMS.txt"
    checksums.write_text(
        f"{sha256(claude_zip)}  {claude_zip.name}\n"
        f"{sha256(plugin_zip)}  {plugin_zip.name}\n",
        encoding="utf-8",
    )

    print(claude_zip)
    print(plugin_zip)
    print(checksums)

if __name__ == "__main__":
    main()
