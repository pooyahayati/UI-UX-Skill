#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "skills" / "ui-ux-skill" / "specialists.json"


class CheckError(Exception):
    pass


def load_registry() -> dict:
    try:
        data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    except Exception as exc:
        raise CheckError(f"Cannot read specialist registry: {exc}") from exc

    if data.get("schema_version") != 1:
        raise CheckError("Unsupported specialists.json schema_version")

    policy = data.get("policy", {})
    if policy.get("allow_version_pins") is not False:
        raise CheckError("Specialist registry must prohibit version pins")
    if policy.get("vendor_specialists") is not False:
        raise CheckError("Specialist registry must prohibit vendoring specialists")
    if policy.get("head_precedence") is not True:
        raise CheckError("Specialist registry must preserve Head precedence")

    specialists = data.get("specialists")
    if not isinstance(specialists, list) or not specialists:
        raise CheckError("Specialist registry must contain at least one specialist")

    seen: set[str] = set()
    forbidden_keys = {"version", "tag", "commit", "sha", "pinned_ref", "release"}

    for item in specialists:
        if not isinstance(item, dict):
            raise CheckError("Every specialist entry must be an object")
        missing = [
            key
            for key in [
                "id",
                "skill_name",
                "requirement",
                "trigger",
                "canonical_repository",
                "skill_path",
                "install_name",
            ]
            if not item.get(key)
        ]
        if missing:
            raise CheckError(f"Specialist entry missing fields {missing}: {item!r}")
        if item["id"] in seen:
            raise CheckError(f"Duplicate specialist id: {item['id']}")
        seen.add(item["id"])
        if item["requirement"] not in {"required", "recommended", "optional"}:
            raise CheckError(f"Invalid requirement for {item['id']}")
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", item["canonical_repository"]):
            raise CheckError(f"Invalid canonical_repository for {item['id']}")
        if any(key in item for key in forbidden_keys):
            raise CheckError(f"Version/ref pin is forbidden in specialist entry: {item['id']}")

    return data


def github_request(url: str) -> bytes:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "ui-ux-skill-specialist-check",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=20) as response:
            return response.read()
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise CheckError(f"GitHub HTTP {exc.code} for {url}: {body[:300]}") from exc
    except urllib.error.URLError as exc:
        raise CheckError(f"GitHub request failed for {url}: {exc}") from exc


def github_json(url: str) -> dict:
    return json.loads(github_request(url).decode("utf-8"))


def resolve_current_ref(repo: str) -> tuple[str, str]:
    latest_url = f"https://api.github.com/repos/{repo}/releases/latest"
    try:
        release = github_json(latest_url)
        tag = release.get("tag_name")
        if tag and not release.get("draft") and not release.get("prerelease"):
            return str(tag), "latest-stable-release"
    except CheckError as exc:
        if "HTTP 404" not in str(exc):
            raise

    meta = github_json(f"https://api.github.com/repos/{repo}")
    branch = meta.get("default_branch")
    if not branch:
        raise CheckError(f"Cannot determine default branch for {repo}")
    return str(branch), "default-branch"


def remote_skill_path(item: dict) -> str:
    base = item["skill_path"].strip("/")
    if base in {"", "."}:
        return "SKILL.md"
    return f"{base}/SKILL.md"


def fetch_remote_skill(item: dict) -> tuple[str, str, str]:
    repo = item["canonical_repository"]
    ref, channel = resolve_current_ref(repo)
    path = remote_skill_path(item)
    url = (
        f"https://api.github.com/repos/{repo}/contents/"
        f"{urllib.parse.quote(path, safe='/')}?ref={urllib.parse.quote(ref, safe='')}"
    )
    payload = github_json(url)
    if payload.get("encoding") != "base64" or "content" not in payload:
        raise CheckError(f"Unexpected GitHub content response for {repo}:{path}@{ref}")
    raw = base64.b64decode(payload["content"]).decode("utf-8")
    return raw, ref, channel


def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    block = parts[1]
    result: dict[str, str] = {}
    for line in block.splitlines():
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.+?)\s*$", line)
        if match:
            result[match.group(1)] = match.group(2).strip().strip('"').strip("'")
        nested_version = re.match(r"^\s+version:\s*(.+?)\s*$", line)
        if nested_version and "version" not in result:
            result["version"] = nested_version.group(1).strip().strip('"').strip("'")
    return result


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def installed_roots(args: argparse.Namespace) -> list[Path]:
    roots = [Path(p).expanduser() for p in (args.installed_root or [])]
    if args.check_codex:
        codex_home = Path(os.environ.get("CODEX_HOME", "~/.codex")).expanduser()
        roots.append(codex_home / "skills")
    unique: list[Path] = []
    for root in roots:
        resolved = root.resolve()
        if resolved not in unique:
            unique.append(resolved)
    return unique


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate UI/UX Skill specialist registry and optional freshness."
    )
    parser.add_argument(
        "--check-upstream",
        action="store_true",
        help="Resolve each canonical source to its latest stable release or default branch and validate SKILL.md.",
    )
    parser.add_argument(
        "--check-codex",
        action="store_true",
        help="Check installed specialists under $CODEX_HOME/skills (default ~/.codex/skills).",
    )
    parser.add_argument(
        "--installed-root",
        action="append",
        help="Additional installed Skills root to inspect. May be supplied multiple times.",
    )
    parser.add_argument(
        "--require-required-installed",
        action="store_true",
        help="Fail when a required specialist is missing from every inspected install root.",
    )
    parser.add_argument(
        "--require-current",
        action="store_true",
        help="Fail when an inspected required specialist differs from current canonical upstream.",
    )
    args = parser.parse_args()

    try:
        registry = load_registry()
    except CheckError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    specialists = registry["specialists"]
    roots = installed_roots(args)
    failures: list[str] = []
    remote: dict[str, dict] = {}

    if args.check_upstream or roots:
        for item in specialists:
            try:
                text, ref, channel = fetch_remote_skill(item)
                meta = parse_frontmatter(text)
                found_name = meta.get("name")
                if found_name != item["skill_name"]:
                    failures.append(
                        f"{item['id']}: upstream Skill name is {found_name!r}, expected {item['skill_name']!r}"
                    )
                    continue
                remote[item["id"]] = {
                    "text": text,
                    "ref": ref,
                    "channel": channel,
                    "version": meta.get("version"),
                    "sha256": sha256_text(text),
                }
                version_note = f" reported_version={meta.get('version')}" if meta.get("version") else ""
                print(
                    f"UPSTREAM {item['id']}: OK "
                    f"source={item['canonical_repository']} channel={channel} ref={ref}{version_note}"
                )
            except CheckError as exc:
                failures.append(f"{item['id']}: {exc}")

    if roots:
        for item in specialists:
            found_any = False
            current_any = False
            for root in roots:
                skill_file = root / item["install_name"] / "SKILL.md"
                if not skill_file.is_file():
                    continue
                found_any = True
                installed_text = skill_file.read_text(encoding="utf-8")
                installed_meta = parse_frontmatter(installed_text)
                if installed_meta.get("name") != item["skill_name"]:
                    failures.append(
                        f"{item['id']}: installed Skill name mismatch at {skill_file}"
                    )
                    continue

                upstream = remote.get(item["id"])
                if upstream:
                    same = sha256_text(installed_text) == upstream["sha256"]
                    state = "CURRENT" if same else "DIFFERS_FROM_CURRENT_UPSTREAM"
                    current_any = current_any or same
                    print(f"INSTALLED {item['id']}: {state} path={skill_file}")
                else:
                    print(f"INSTALLED {item['id']}: FOUND path={skill_file}")

            if not found_any:
                print(f"INSTALLED {item['id']}: MISSING")
                if args.require_required_installed and item["requirement"] == "required":
                    failures.append(f"{item['id']}: required specialist is not installed")
            elif (
                args.require_current
                and item["requirement"] == "required"
                and remote.get(item["id"])
                and not current_any
            ):
                failures.append(
                    f"{item['id']}: required installed specialist is not current with canonical upstream"
                )

    if failures:
        print("\nSpecialist validation failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print("\nSpecialist registry validation passed.")
    if not args.check_upstream and not roots:
        print("No network/install freshness check requested.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
