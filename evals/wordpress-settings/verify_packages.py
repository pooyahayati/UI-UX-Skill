"""Verify actual consumer ZIP bytes/checksums against the selected source tree."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile

from test_contracts import ROOT, canonical_bytes


def verify(directory):
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    names = {f"ui-ux-skill-claude-v{version}.zip", f"ui-ux-plugin-v{version}.zip"}
    sums = {}
    for line in (directory / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        digest, name = line.split()
        if name in sums:
            raise ValueError("Duplicate checksum entry")
        sums[name] = digest
    if set(sums) != names:
        raise ValueError("Unexpected checksum inventory")
    source = ROOT / "skills/ui-ux-skill"
    records = []
    for name in sorted(names):
        archive = directory / name
        digest = hashlib.sha256(archive.read_bytes()).hexdigest()
        if sums[name] != digest:
            raise ValueError("Published checksum mismatch")
        plugin = "plugin" in name
        prefix = "ui-ux/skills/ui-ux-skill/" if plugin else "ui-ux-skill/"
        expected = {prefix + p.relative_to(source).as_posix(): p for p in source.rglob("*") if p.is_file()}
        if plugin:
            expected.update({"ui-ux/" + rel: ROOT / rel for rel in ["plugin.json", "assets/logo.svg", "assets/composer-icon.svg", "LICENSE", "PRIVACY.md", "TERMS.md", "SUPPORT.md"]})
        with zipfile.ZipFile(archive) as zipped:
            if zipped.testzip() is not None or len(zipped.namelist()) != len(expected) or set(zipped.namelist()) != set(expected):
                raise ValueError("Corrupt, duplicate or unexpected package members")
            for member, src in expected.items():
                if zipped.read(member).replace(b"\r\n", b"\n") != canonical_bytes(src):
                    raise ValueError(f"Consumer differs from canonical source: {member}")
            if zipped.read(prefix + "VERSION").decode().strip() != version:
                raise ValueError("Wrong installed version")
        records.append({"file": name, "sha256": digest, "members": len(expected), "crc": "passed", "canonical_source_identity": "passed"})
    return {"version": version, "checks": records, "scope": "Actual supplied archives, checksum manifest and complete canonical source identity; not browser/model evidence"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", required=True, type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    result = verify(args.directory)
    content = json.dumps(result, indent=2) + "\n"
    if args.report:
        if args.report.exists():
            raise ValueError("Choose a fresh verification report")
        args.report.write_text(content, encoding="utf-8")
    print(content, end="")
