#!/usr/bin/env python3
from __future__ import annotations

import argparse
import http.client
import json
import os
from pathlib import Path
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

from specialist_integrity import CheckError, inspect_package, remote_package, safe_path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "skills" / "ui-ux-skill" / "specialists.json"


MAX_RESPONSE_BYTES = 8 * 1024 * 1024


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def load_registry() -> dict:
    try:
        data = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    except Exception as exc:
        raise CheckError(f"Cannot read specialist registry: {exc}") from exc

    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise CheckError("Unsupported specialists.json schema_version")

    policy = data.get("policy", {})
    if not isinstance(policy, dict):
        raise CheckError("Invalid specialist registry policy")
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
            if not isinstance(item.get(key), str) or not item[key].strip()
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
        safe_path(item["canonical_repository"])
        if any(key in item for key in forbidden_keys):
            raise CheckError(f"Version/ref pin is forbidden in specialist entry: {item['id']}")
        safe_path(item["skill_path"], root=True)
        if "/" in safe_path(item["install_name"]):
            raise CheckError("install_name must be a single directory name")

    return data


def github_request(url: str) -> bytes:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https" or parsed.netloc != "api.github.com" or not parsed.path.startswith("/repos/"):
        raise CheckError("Refusing noncanonical GitHub API destination")
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
        with urllib.request.build_opener(NoRedirect()).open(req, timeout=20) as response:
            body = response.read(MAX_RESPONSE_BYTES + 1)
            if len(body) > MAX_RESPONSE_BYTES:
                raise CheckError("GitHub response exceeds size limit")
            return body
    except urllib.error.HTTPError as exc:
        # Never print remote bodies or credentials; HTTP 404 alone permits release fallback.
        raise CheckError(f"GitHub HTTP {exc.code} for {url}", status=exc.code) from exc
    except (urllib.error.URLError, OSError, http.client.HTTPException) as exc:
        raise CheckError(f"GitHub request unavailable ({type(exc).__name__}) for {url}") from exc


def github_json(url: str) -> dict:
    try:
        payload = json.loads(github_request(url).decode("utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("object required")
        return payload
    except ValueError as exc:
        raise CheckError(f"Malformed GitHub JSON for {url}") from exc


def resolve_current_ref(repo: str) -> tuple[str, str]:
    latest_url = f"https://api.github.com/repos/{repo}/releases/latest"
    try:
        release = github_json(latest_url)
        tag = release.get("tag_name")
        if isinstance(tag, str) and tag and release.get("draft") is False and release.get("prerelease") is False:
            return tag, "latest-stable-release"
        raise CheckError(f"Malformed stable release for {repo}")
    except CheckError as exc:
        if exc.status != 404:
            raise

    meta = github_json(f"https://api.github.com/repos/{repo}")
    branch = meta.get("default_branch")
    if not isinstance(branch, str) or not branch:
        raise CheckError(f"Cannot determine default branch for {repo}")
    return str(branch), "default-branch"


def fetch_remote_package(item: dict) -> dict:
    ref, channel = resolve_current_ref(item["canonical_repository"])
    return remote_package(item, ref, channel, github_json)


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


def installed_roots(args: argparse.Namespace) -> list[Path]:
    roots = [Path(p).expanduser() for p in (args.installed_root or [])]
    if args.check_codex:
        codex_home = Path(os.environ.get("CODEX_HOME", "~/.codex")).expanduser()
        roots.append(codex_home / "skills")
    unique: list[Path] = []
    for root in roots:
        # Keep link spelling so inspection can reject links instead of erasing them.
        resolved = Path(os.path.abspath(root))
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
        help="Validate an immutable package manifest and entrypoint at the current canonical source; no installation.",
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
        help="Require a valid required specialist entrypoint in EACH explicitly inspected root.",
    )
    parser.add_argument(
        "--require-current",
        action="store_true",
        help="Require exact package byte identity in EACH inspected root (including presence); local additions are not certified.",
    )
    args = parser.parse_args()

    try:
        registry = load_registry()
    except CheckError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    specialists = registry["specialists"]
    roots = installed_roots(args)
    if (args.require_current or args.require_required_installed) and not roots:
        print("ERROR: strict installed/current checks require --check-codex or --installed-root", file=sys.stderr)
        return 1
    failures: list[str] = []
    remote: dict[str, dict] = {}

    if args.check_upstream or roots:
        for item in specialists:
            try:
                package = fetch_remote_package(item)
                meta = parse_frontmatter(package["text"])
                found_name = meta.get("name")
                if found_name != item["skill_name"]:
                    failures.append(
                        f"{item['id']}: upstream Skill name is {found_name!r}, expected {item['skill_name']!r}"
                    )
                    continue
                remote[item["id"]] = package
                version_note = f" reported_version={meta.get('version')}" if meta.get("version") else ""
                print(
                    f"UPSTREAM {item['id']}: MANIFEST_VERIFIED "
                    f"source={item['canonical_repository']} channel={package['channel']} "
                    f"ref={package['ref']} commit={package['commit']} files={len(package['files'])}{version_note}"
                )
            except CheckError as exc:
                failures.append(f"{item['id']}: UPSTREAM_UNVERIFIED: {exc}")

    if roots:
        for item in specialists:
            for root in roots:
                path = root / item["install_name"]
                report = inspect_package(path, remote.get(item["id"]))
                state = report["state"]
                print(f"INSTALLED {item['id']}: {state} entrypoint={report['entrypoint']} path={path}")
                for problem in report["problems"]:
                    print(f"  {problem}")
                for addition in sorted(report["additions"]):
                    print(f"  LOCAL_ADDITION (not certified): {addition}")
                if state == "UNVERIFIED":
                    failures.append(f"{item['id']}: inspection unverified at {path}")
                if item["requirement"] == "required":
                    if args.require_current and state != "CURRENT":
                        failures.append(f"{item['id']}: required package is not current at {path}")
                    if args.require_required_installed and (
                            parse_frontmatter(report.get("entrypoint_text", "")).get("name") != item["skill_name"]):
                        failures.append(f"{item['id']}: required entrypoint is missing/invalid at {path}")

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
