"""Fixture-only legacy text consumer; not a production migration tool."""
from pathlib import Path
import re


def read_profile(root: Path) -> dict[str, str]:
    text = (root / "design-profile.md").read_text(encoding="utf-8")
    result = {}
    for field in ("status", "density"):
        match = re.search(rf"^\s*{field}:\s*(\S+)\s*$", text, re.MULTILINE)
        if not match:
            raise ValueError(f"Legacy consumer missing {field}")
        result[field] = match[1]
    return result
