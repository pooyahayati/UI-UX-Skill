"""Prepared original fixture artwork. Configuration selects IDs, never vector code."""
from copy import deepcopy

USES = {
    "search": "Search", "add": "Add", "edit": "Edit", "delete": "Delete",
    "settings": "Settings", "previous": "Previous", "disclosure": "Disclosure",
}
FAMILIES = {
    "outline": {"label": "Prepared outline", "stroke": True},
    "solid": {"label": "Prepared solid", "stroke": False},
}
VARIANTS = ["plain", "badge"]

# Only path data is supplied to the fixed renderer: no tags, URLs or attributes
# are ever supplied by owner input. Solid artwork has no configurable stroke.
OUTLINE = {
    "search": "M15 15L21 21 M17 10A7 7 0 1 1 3 10A7 7 0 1 1 17 10Z",
    "add": "M12 4V20 M4 12H20",
    "edit": "M4 17L17 4L20 7L7 20H4Z M14 7L17 10",
    "delete": "M4 6H20 M9 6V3H15V6 M6 6L7 21H17L18 6 M10 10V17 M14 10V17",
    "settings": "M4 7H20 M4 17H20 M8 4V10 M16 14V20",
    "previous": "M14 5L7 12L14 19 M7 12H21",
    "disclosure-closed": "M7 5L14 12L7 19",
    "disclosure-open": "M5 8L12 15L19 8",
}
SOLID = {
    "search": "M10 2A8 8 0 1 0 15 16L20 21L22 19L17 14A8 8 0 0 0 10 2Z M10 5A5 5 0 1 1 10 15A5 5 0 1 1 10 5Z",
    "add": "M10 3H14V10H21V14H14V21H10V14H3V10H10Z",
    "edit": "M3 17L16 4L20 8L7 21H3Z M17 3L19 1L23 5L21 7Z",
    "delete": "M4 4H9V2H15V4H20V7H4Z M6 9H18L17 22H7Z M9 11V19H11V11Z M13 11V19H15V11Z",
    "settings": "M3 5H7V3H10V5H21V8H10V10H7V8H3Z M3 16H14V14H17V16H21V19H17V21H14V19H3Z",
    "previous": "M13 3L4 12L13 21L15 19L10 14H22V10H10L15 5Z",
    "disclosure-closed": "M6 3L15 12L6 21L4 19L11 12L4 5Z",
    "disclosure-open": "M3 6L12 15L21 6L23 8L12 19L1 8Z",
}


def asset(family, use, variant):
    """Known missing solid settings badge demonstrates meaningful fallback."""
    fallback = family == "solid" and use == "settings" and variant == "badge"
    actual = "outline" if fallback else family
    paths = OUTLINE if actual == "outline" else SOLID
    keys = ["disclosure-closed", "disclosure-open"] if use == "disclosure" else [use]
    states = {}
    for key in keys:
        artwork = [{"d": paths[key], "badge": False}]
        if variant == "badge":
            artwork.append({"d": "M1 1H23V23H1Z M3 3V21H21V3Z", "badge": True})
        states[key.rsplit("-", 1)[-1] if use == "disclosure" else "default"] = artwork
    return {"use": use, "variant": variant, "requestedFamily": family,
            "family": actual, "stroke": FAMILIES[actual]["stroke"],
            "fallback": fallback, "directional": use == "previous" or use == "disclosure",
            "states": states}


def icon_catalog():
    return {"families": deepcopy(FAMILIES), "uses": dict(USES),
            "variants": list(VARIANTS),
            "assets": {family: {use: {variant: asset(family, use, variant)
                                      for variant in VARIANTS} for use in USES}
                       for family in FAMILIES},
            "policy": "Prepared IDs only; solid stroke is dormant, fallback uses its prepared stroke."}


def resolve_icons(config):
    return {use: asset(config["iconFamily"], use, config[use + "Icon"]) for use in USES}
