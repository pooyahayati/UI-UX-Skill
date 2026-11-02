"""Import-safe raw evidence loading; preserve the existing duplicate-field rule."""
import json
from pathlib import Path


def unique_object(pairs: list[tuple[str, object]]) -> dict:
    """Do not silently overwrite contradictory JSON object fields."""
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"Duplicate JSON field: {key}")
        value[key] = item
    return value


def load_json(path: Path | str):
    path = Path(path)
    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    except ValueError as error:
        raise ValueError(f"{path}: {error}") from error
