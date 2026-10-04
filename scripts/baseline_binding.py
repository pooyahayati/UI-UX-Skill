"""Validate the frozen executable test input, not real customer approval."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


def validate_baseline(root: Path) -> list[str]:
    errors: list[str] = []
    try:
        record = json.loads((root / "BASELINE.json").read_text(encoding="utf-8"))
        if not isinstance(record, dict):
            return ["Baseline record must be an object"]
        if record.get("schema_version") != 1:
            errors.append("Unsupported baseline schema")
        if record.get("hash_method") != "sha256-exact-bytes-utf8-lf":
            errors.append("Unknown byte identity method")
        if record.get("authority_kind") != "explicitly-fictional-test-input":
            errors.append("Fixture authority cannot imply actual customer approval")
        entries = record.get("files")
        if not isinstance(entries, dict):
            return errors + ["Baseline files must be an object"]
        if set(entries) != {"index.html", "DESIGN.md"}:
            errors.append("Must bind both real source and canonical handbook")
        for name, expected in entries.items():
            if name not in {"index.html", "DESIGN.md"}:
                continue  # Never follow arbitrary manifest paths.
            content = (root / name).read_bytes()
            if b"\r" in content or content.startswith(b"\xef\xbb\xbf"):
                errors.append(f"{name}: input must retain exact UTF-8/LF bytes")
            if hashlib.sha256(content).hexdigest() != expected:
                errors.append(f"{name}: baseline bytes mismatch")
        html = (root / "index.html").read_text(encoding="utf-8")
        handbook = (root / "DESIGN.md").read_text(encoding="utf-8")
        notes = (root / "OWNER_NOTES.md").read_text(encoding="utf-8")
        for key in ("sample_id", "handbook_revision"):
            value = record.get(key)
            if not isinstance(value, str) or not value or any(value not in source for source in (html, handbook, notes)):
                errors.append(f"{key}: source/handbook/record identity mismatch")
        approval = record.get("approval_record")
        if not isinstance(approval, str) or not approval or approval not in handbook or approval not in notes:
            errors.append("Missing scoped approval record")
    except (OSError, ValueError, TypeError) as exc:
        errors.append(f"Baseline unavailable: {exc}")
    return errors
