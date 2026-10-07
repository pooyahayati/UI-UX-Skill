"""Bounded, read-only comparison of a declared Skill subtree to immutable Git blobs."""
from __future__ import annotations

import base64
import hashlib
import os
from pathlib import Path
import re
import stat
from urllib.parse import quote

MAX_ENTRIES = 10000
MAX_FILE_BYTES = 32 * 1024 * 1024
MAX_PACKAGE_BYTES = 128 * 1024 * 1024
MAX_ENTRYPOINT_BYTES = 1024 * 1024


class CheckError(Exception):
    def __init__(self, message: str, status: int | None = None):
        super().__init__(message)
        self.status = status


def safe_path(value: object, *, root: bool = False) -> str:
    if root and value == ".":
        return ""
    if not isinstance(value, str) or not value or len(value) > 1024:
        raise CheckError("Invalid package path")
    parts = value.split("/")
    if len(parts) > 32:
        raise CheckError("Package path depth exceeds limit")
    for part in parts:
        if (not part or part in (".", "..") or part.casefold() == ".git"
                or part.endswith((".", " ")) or any(ord(c) < 32 or c in '\\:<>"|?*' for c in part)
                or re.fullmatch(r"(?i)(CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])(?:\..*)?", part)):
            raise CheckError(f"Unsafe/unsupported package path: {value!r}")
    return value


def oid(value: object) -> str:
    if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{40}", value):
        raise CheckError("Invalid Git object identity")
    return value


def blob_id(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def tree_entries(payload: dict, expected_sha: str, *, package_scope: bool = True) -> list[dict]:
    entries = payload.get("tree")
    if payload.get("sha") != expected_sha or payload.get("truncated") is not False:
        raise CheckError("Unverified or truncated Git tree")
    if not isinstance(entries, list) or len(entries) > MAX_ENTRIES:
        raise CheckError("Invalid/oversized Git tree")
    seen: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            raise CheckError("Invalid Git tree entry")
        path = entry.get("path")
        if package_scope:
            safe_path(path)
        elif not isinstance(path, str) or not path or "/" in path:
            raise CheckError("Malformed ancestor tree entry")
        key = path.casefold() if package_scope else path
        if key in seen:
            raise CheckError(f"Duplicate/case-colliding Git path: {path}")
        seen.add(key)
        oid(entry.get("sha"))
    return entries


def remote_package(item: dict, ref: str, channel: str, get_json) -> dict:
    """Resolve once, then use only immutable commit/tree/blob object identities."""
    api = f"https://api.github.com/repos/{item['canonical_repository']}"
    commit = get_json(f"{api}/commits/{quote(ref, safe='')}")
    revision = oid(commit.get("sha"))
    try:
        tree = oid(commit["commit"]["tree"]["sha"])
    except (KeyError, TypeError) as exc:
        raise CheckError("Malformed commit tree") from exc
    package_path = safe_path(item["skill_path"], root=True)
    for segment in package_path.split("/") if package_path else []:
        entries = tree_entries(get_json(f"{api}/git/trees/{tree}"), tree, package_scope=False)
        selected = next((x for x in entries if x["path"] == segment), None)
        if not selected or selected.get("type") != "tree" or selected.get("mode") != "040000":
            raise CheckError(f"Package directory missing or unsupported: {package_path}")
        tree = selected["sha"]
    entries = tree_entries(get_json(f"{api}/git/trees/{tree}?recursive=1"), tree)
    files: dict[str, dict] = {}
    total = 0
    for entry in entries:
        kind, mode, path = entry.get("type"), entry.get("mode"), entry["path"]
        if kind == "tree" and mode == "040000":
            continue
        if kind != "blob" or mode not in ("100644", "100755"):
            raise CheckError(f"Unsupported upstream link/submodule/type: {path}")
        size = entry.get("size")
        if type(size) is not int or not 0 <= size <= MAX_FILE_BYTES:
            raise CheckError(f"Invalid/oversized upstream file: {path}")
        total += size
        if total > MAX_PACKAGE_BYTES:
            raise CheckError("Package byte limit exceeded")
        files[path] = {"sha": entry["sha"], "size": size}
    # Refuse ambiguous ancestors even if a malformed server omits directory entries.
    identities: dict[str, str] = {}
    for entry in entries:
        parts = entry["path"].split("/")
        for index in range(1, len(parts) + 1):
            name = "/".join(parts[:index])
            if name.casefold() in identities and identities[name.casefold()] != name:
                raise CheckError(f"Case-colliding package ancestors: {name}")
            identities[name.casefold()] = name
            if index < len(parts) and name in files:
                raise CheckError(f"File used as package directory: {name}")
    if "SKILL.md" not in files or files["SKILL.md"]["size"] > MAX_ENTRYPOINT_BYTES:
        raise CheckError("Missing or oversized package SKILL.md")
    identity = files["SKILL.md"]
    payload = get_json(f"{api}/git/blobs/{identity['sha']}")
    try:
        if (payload.get("encoding") != "base64" or payload.get("sha") != identity["sha"]
                or payload.get("size") != identity["size"]):
            raise CheckError("Invalid entrypoint blob metadata")
        raw = base64.b64decode("".join(payload["content"].split()), validate=True)
        if len(raw) != identity["size"] or blob_id(raw) != identity["sha"]:
            raise CheckError("Entrypoint blob identity mismatch")
        text = raw.decode("utf-8")
    except (KeyError, AttributeError, TypeError, ValueError) as exc:
        raise CheckError("Malformed entrypoint blob") from exc
    return {"ref": ref, "channel": channel, "commit": revision, "tree": tree,
            "files": files, "text": text}


def regular_stat(path: Path):
    info = path.lstat()
    if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
        raise CheckError(f"Unsupported local link/reparse point: {path}")
    return info


def inspect_package(package: Path, upstream: dict | None) -> dict:
    """No writes, code execution, link traversal, normalization or inferred Head waivers."""
    result = {"state": "UNVERIFIED", "entrypoint": "UNVERIFIED", "problems": [], "additions": []}
    try:
        # Check all ancestors before enumerating; supported roots are trusted and stable.
        for parent in reversed((package, *package.parents)):
            info = regular_stat(parent)
            if not stat.S_ISDIR(info.st_mode):
                raise CheckError(f"Not a package directory: {parent}")
    except FileNotFoundError:
        result["state"] = "MISSING"
        return result
    except (OSError, CheckError) as exc:
        result["problems"].append(str(exc))
        return result
    if upstream is None:
        result["problems"].append("Upstream unavailable; package comparison not performed")
        return result
    try:
        expected = upstream["files"]
        actual: dict[str, str] = {}
        pending = [package]
        visited, total = 0, 0
        names: set[str] = set()
        while pending:
            directory = pending.pop()
            with os.scandir(directory) as scan:
                for entry in scan:
                    visited += 1
                    if visited > MAX_ENTRIES:
                        raise CheckError("Local package entry limit exceeded")
                    path = Path(entry.path)
                    info = regular_stat(path)
                    name = path.relative_to(package).as_posix()
                    # Ignore only untracked runtime caches / Git metadata, never a required file.
                    if name not in expected and (entry.name == ".git" or entry.name == "__pycache__"
                                                  or entry.name.endswith((".pyc", ".pyo"))):
                        continue
                    safe_path(name)
                    if name.casefold() in names:
                        raise CheckError(f"Case-colliding local paths: {name}")
                    names.add(name.casefold())
                    if stat.S_ISDIR(info.st_mode):
                        pending.append(path)
                        continue
                    if not stat.S_ISREG(info.st_mode):
                        raise CheckError(f"Unsupported local file: {name}")
                    if info.st_size > MAX_FILE_BYTES:
                        raise CheckError(f"Local file size limit exceeded: {name}")
                    if name == "SKILL.md" and info.st_size > MAX_ENTRYPOINT_BYTES:
                        raise CheckError("Local entrypoint size limit exceeded")
                    total += info.st_size
                    if total > MAX_PACKAGE_BYTES:
                        raise CheckError("Local package byte limit exceeded")
                    if name in expected:
                        with path.open("rb") as stream:
                            data = stream.read(MAX_FILE_BYTES + 1)
                        if len(data) != info.st_size:
                            raise CheckError(f"Local file changed during inspection: {name}")
                        actual[name] = blob_id(data)
                        if name == "SKILL.md":
                            try:
                                result["entrypoint_text"] = data.decode("utf-8")
                            except UnicodeError as exc:
                                raise CheckError("Unreadable local entrypoint encoding") from exc
                    else:
                        result["additions"].append(name)
        for name, identity in expected.items():
            if name not in actual:
                result["problems"].append(f"MISSING_FILE {name}")
            elif actual[name] != identity["sha"]:
                result["problems"].append(f"MODIFIED_FILE {name}")
        result["entrypoint"] = ("MATCH" if actual.get("SKILL.md") == expected["SKILL.md"]["sha"]
                                else "MISSING_OR_MODIFIED")
        result["state"] = ("DIFFERS" if result["problems"] else
                           "UPSTREAM_MATCH_WITH_ADDITIONS" if result["additions"] else "CURRENT")
    except (OSError, CheckError) as exc:
        result["problems"].append(str(exc))
    return result
