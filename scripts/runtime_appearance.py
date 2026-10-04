"""Loopback-only, synthetic runtime appearance proof. Not production auth."""
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import math
from pathlib import Path
import re
import secrets
import sqlite3
import time
from urllib.parse import parse_qs, urlsplit

FIXTURE = Path(__file__).resolve().parents[1] / "evals/fixtures/runtime-appearance"
DEFAULTS = dict(schema=1, palette="ocean", font="system", bodySize=16,
                headingSize=28, labelSize=14, bodyWeight=400, headingWeight=700,
                lineHeight=1.6, density="balanced", spacing=16, radius=8,
                border=1, shadow="soft", buttonStyle="filled", theme="light",
                motion="reduced", chartStyle="bars", diagramStyle="outlined")

# Human contract and default source; none of these choices can alter permissions.
SETTING_SPECS = [
    ("palette", "Color palette", "Brand", ["ocean", "forest", "plum"], "actions, links, focus, chart, icons"),
    ("font", "Available font stack", "Typography", ["system", "serif"], "body, labels, headings, chart labels"),
    ("bodySize", "Body size (px)", "Typography", [16, 17, 18, 19, 20], "body, table, messages"),
    ("headingSize", "Heading size (px)", "Typography", [24, 28, 32, 36], "page/section headings"),
    ("labelSize", "Label size (px)", "Typography", [14, 15, 16, 17, 18], "form labels, controls, chart labels"),
    ("bodyWeight", "Body weight", "Typography", [400, 500], "body, table"),
    ("headingWeight", "Heading weight", "Typography", [600, 700], "headings"),
    ("lineHeight", "Line height", "Typography", [1.5, 1.6, 1.8], "body, labels, messages"),
    ("density", "Control and row density", "Spacing", ["compact", "balanced", "comfortable"], "buttons, fields, table rows"),
    ("spacing", "Section and item gap (px)", "Spacing", [12, 16, 20, 24], "section stacks, toolbars, forms"),
    ("radius", "Corner radius (px)", "Surfaces", [0, 8, 16], "controls, surfaces, overlay, diagram"),
    ("border", "Border width (px)", "Surfaces", [1, 2], "controls, surfaces, overlay, diagram"),
    ("shadow", "Overlay elevation", "Surfaces", ["none", "soft"], "product overlay"),
    ("buttonStyle", "Primary button style", "Components", ["filled", "outlined"], "primary action buttons"),
    ("theme", "Default theme", "Theme and motion", ["light", "dark"], "all semantic surfaces/native controls"),
    ("motion", "Feedback motion", "Theme and motion", ["reduced", "standard"], "state feedback transitions; system reduction wins"),
    ("chartStyle", "Chart presentation", "Visualization", ["bars", "lollipop"], "SVG chart; data/labels unchanged"),
    ("diagramStyle", "Diagram presentation", "Visualization", ["outlined", "filled"], "SVG workflow nodes; connections unchanged"),
]
SPECS = {row[0]: row for row in SETTING_SPECS}
PALETTES = {
    "ocean": ("#145f86", "#8bd3ff"),
    "forest": ("#21663f", "#9ee5b6"),
    "plum": ("#793b85", "#e5a6f0"),
}
THEMES = {
    "light": dict(canvas="#f5f6f8", surface="#ffffff", text="#17212b",
                  muted="#4d5966", border="#667483", danger="#a91c35", inverse="#ffffff"),
    "dark": dict(canvas="#111923", surface="#1c2937", text="#f3f6fa",
                 muted="#bbc8d5", border="#93a4b6", danger="#ffadbc", inverse="#111923"),
}
PRINCIPALS = {
    "owner-a": ("a", True), "owner-a-peer": ("a", True),
    "owner-b": ("b", True), "viewer-a": ("a", False),
}


class AppearanceError(Exception):
    def __init__(self, status, code, message, details=None):
        self.status, self.code, self.message = status, code, message
        self.details = details or {}
        super().__init__(message)


def invalid(message, details=None):
    return AppearanceError(422, "VALIDATION_ERROR", message, details)


def validate(config):
    if type(config) is not dict or set(config) != set(DEFAULTS):
        raise invalid("Provide the complete supported appearance configuration.")
    if type(config["schema"]) is not int or config["schema"] != 1:
        raise invalid("Unsupported configuration schema.", {"schema": "Use schema 1."})
    errors = {}
    for name, _, _, values, _ in SETTING_SPECS:
        value = config[name]
        numeric = type(values[0]) in (int, float)
        if numeric:
            valid_type = type(value) is int or (type(value) is float and math.isfinite(value))
        else:
            valid_type = type(value) is str
        if not valid_type or value not in values:
            errors[name] = "Choose one of the prepared values."
    if errors:
        raise invalid("Some appearance values are not supported.", errors)
    return dict(config)


def catalog():
    return {"schema": 1, "defaults": dict(DEFAULTS), "scope": "tenant product and owned admin preview",
            "settings": [{"key": key, "label": label, "group": group, "values": values,
                          "default": DEFAULTS[key], "consumers": consumers,
                          "permission": "tenant owner", "reset": "private defaults draft",
                          "dependencies": "prepared palette/theme; locked readability/target floors",
                          "themes": ["light", "dark"]}
                         for key, label, group, values, consumers in SETTING_SPECS]}


def resolve(config):
    config = validate(config)
    colors = THEMES[config["theme"]]
    action = PALETTES[config["palette"]][config["theme"] == "dark"]
    height, row = {"compact": (44, 44), "balanced": (48, 52), "comfortable": (56, 64)}[config["density"]]
    tokens = {"--" + key: value for key, value in colors.items()}
    tokens.update({"--action": action, "--focus": action, "--chart-series": action,
                   "--chart-label": colors["text"], "--chart-grid": colors["border"],
                   "--font": "system-ui, sans-serif" if config["font"] == "system" else "Georgia, serif",
                   "--body-size": f'{config["bodySize"]}px', "--heading-size": f'{config["headingSize"]}px',
                   "--label-size": f'{config["labelSize"]}px', "--body-weight": str(config["bodyWeight"]),
                   "--heading-weight": str(config["headingWeight"]), "--line-height": str(config["lineHeight"]),
                   "--control-height": f"{height}px", "--row-height": f"{row}px",
                   "--space": f'{config["spacing"]}px', "--radius": f'{config["radius"]}px',
                   "--border-width": f'{config["border"]}px',
                   "--shadow": "none" if config["shadow"] == "none" else "0 8px 28px #00000033",
                   "--primary-bg": action if config["buttonStyle"] == "filled" else colors["surface"],
                   "--primary-text": colors["inverse"] if config["buttonStyle"] == "filled" else action,
                   "--duration": "0ms" if config["motion"] == "reduced" else "140ms",
                   "--icon-size": f'{config["labelSize"] + 4}px',
                   "color-scheme": config["theme"], "chartStyle": config["chartStyle"],
                   "diagramStyle": config["diagramStyle"]})
    return tokens


def now():
    return datetime.now(timezone.utc).isoformat()


def integer(value, name):
    if type(value) is not int or value < 0 or value > 2**31 - 1:
        raise invalid(f"{name} must be a nonnegative revision.")
    return value


def stored_config(raw):
    """Persisted data can be missing/corrupt; never bypass the snapshot boundary."""
    if type(raw) is not str or len(raw) > 16384:
        raise invalid("Stored appearance configuration is not supported.")
    return validate(json.loads(raw, object_pairs_hook=strict_object))


class Store:
    def __init__(self, path):
        self.path = Path(path)
        with self.connection() as db:
            db.executescript("""
                CREATE TABLE IF NOT EXISTS versions (
                  tenant TEXT NOT NULL, revision INTEGER NOT NULL, config TEXT NOT NULL,
                  actor TEXT NOT NULL, action TEXT NOT NULL, created TEXT NOT NULL,
                  PRIMARY KEY (tenant, revision));
                CREATE TABLE IF NOT EXISTS active (tenant TEXT PRIMARY KEY, revision INTEGER NOT NULL);
                CREATE TABLE IF NOT EXISTS drafts (
                  tenant TEXT NOT NULL, actor TEXT NOT NULL, draft INTEGER NOT NULL,
                  base INTEGER NOT NULL, config TEXT NOT NULL, PRIMARY KEY (tenant, actor));
                CREATE TABLE IF NOT EXISTS audit (
                  id INTEGER PRIMARY KEY, tenant TEXT NOT NULL, actor TEXT NOT NULL,
                  action TEXT NOT NULL, revision INTEGER NOT NULL, created TEXT NOT NULL);
            """)
            for tenant in ("a", "b"):
                if not db.execute("SELECT 1 FROM versions WHERE tenant=? LIMIT 1", (tenant,)).fetchone():
                    db.execute("INSERT INTO versions VALUES (?,0,?,?,?,?)",
                               (tenant, json.dumps(DEFAULTS), "fixture", "initial", now()))
                    db.execute("INSERT OR IGNORE INTO active VALUES (?,0)", (tenant,))

    @contextmanager
    def connection(self, write=False):
        db = sqlite3.connect(self.path, timeout=5, isolation_level=None)
        db.row_factory = sqlite3.Row
        try:
            db.execute("BEGIN IMMEDIATE" if write else "BEGIN")
            yield db
            if db.in_transaction:
                db.commit()
        except BaseException:
            if db.in_transaction:
                db.rollback()
            raise
        finally:
            db.close()

    def _published(self, db, tenant):
        active = db.execute("SELECT revision FROM active WHERE tenant=?", (tenant,)).fetchone()
        rows = db.execute("SELECT * FROM versions WHERE tenant=? ORDER BY revision DESC", (tenant,)).fetchall()
        # Active first, then prior valid history; no field-level merge or draft source.
        ordered = sorted(rows, key=lambda r: (not active or r["revision"] != active["revision"], -r["revision"]))
        for row in ordered:
            try:
                config = stored_config(row["config"])
            except (AppearanceError, ValueError, TypeError, RecursionError):
                continue
            source = "published" if active and row["revision"] == active["revision"] else "history-fallback"
            return {"revision": row["revision"], "source": source, "config": config, "tokens": resolve(config)}
        return self.fallback("defaults-fallback")

    @staticmethod
    def fallback(source):
        return {"revision": None, "source": source, "config": dict(DEFAULTS), "tokens": resolve(DEFAULTS)}

    def published(self, tenant):
        try:
            with self.connection() as db:
                return self._published(db, tenant)
        except sqlite3.Error:
            return self.fallback("storage-fallback")

    @staticmethod
    def _draft(db, tenant, actor):
        row = db.execute("SELECT * FROM drafts WHERE tenant=? AND actor=?", (tenant, actor)).fetchone()
        if not row:
            return None
        try:
            config = stored_config(row["config"])
        except (AppearanceError, ValueError, TypeError, RecursionError):
            raise AppearanceError(503, "DRAFT_UNAVAILABLE", "Saved draft is invalid; published values are unchanged.")
        return {"draftRevision": row["draft"], "baseRevision": row["base"], "config": config}

    def draft(self, tenant, actor):
        with self.connection() as db:
            return self._draft(db, tenant, actor)

    def _base(self, db, tenant, base):
        integer(base, "baseRevision")
        active = self._published(db, tenant)
        if active["source"] != "published":
            raise AppearanceError(503, "CONFIG_DEGRADED", "Restore valid published storage before changing appearance.")
        if active["revision"] != base:
            raise AppearanceError(409, "BASE_CONFLICT", "Published appearance changed; reconcile with the current revision.")
        return active

    @staticmethod
    def _expected(db, tenant, actor, revision):
        integer(revision, "draftRevision")
        row = db.execute("SELECT draft FROM drafts WHERE tenant=? AND actor=?", (tenant, actor)).fetchone()
        if (row["draft"] if row else 0) != revision:
            raise AppearanceError(409, "DRAFT_CONFLICT", "Saved draft changed; reload before replacing it.")

    @staticmethod
    def _audit(db, tenant, actor, action, revision):
        db.execute("INSERT INTO audit(tenant,actor,action,revision,created) VALUES (?,?,?,?,?)",
                   (tenant, actor, action, revision, now()))

    def save(self, tenant, actor, config, base, expected, action="draft-saved"):
        config = validate(config)
        with self.connection(True) as db:
            self._base(db, tenant, base)
            self._expected(db, tenant, actor, expected)
            # Actor-global audit identity also avoids ABA reuse after discard/publish.
            revision = db.execute("SELECT COALESCE(MAX(id),0)+1 FROM audit").fetchone()[0]
            db.execute("INSERT INTO drafts VALUES (?,?,?,?,?) ON CONFLICT(tenant,actor) DO UPDATE SET draft=excluded.draft,base=excluded.base,config=excluded.config",
                       (tenant, actor, revision, base, json.dumps(config)))
            self._audit(db, tenant, actor, action, revision)
            return self._draft(db, tenant, actor)

    def reset(self, tenant, actor, base, expected):
        return self.save(tenant, actor, DEFAULTS, base, expected, "draft-reset")

    def discard(self, tenant, actor, expected):
        with self.connection(True) as db:
            self._expected(db, tenant, actor, expected)
            db.execute("DELETE FROM drafts WHERE tenant=? AND actor=?", (tenant, actor))
            self._audit(db, tenant, actor, "draft-discarded", expected)
        return {"discarded": True}

    def _append(self, db, tenant, actor, config, action):
        config = validate(config)
        revision = db.execute("SELECT COALESCE(MAX(revision),-1)+1 FROM versions WHERE tenant=?", (tenant,)).fetchone()[0]
        db.execute("INSERT INTO versions VALUES (?,?,?,?,?,?)", (tenant, revision, json.dumps(config), actor, action, now()))
        db.execute("UPDATE active SET revision=? WHERE tenant=?", (revision, tenant))
        self._audit(db, tenant, actor, action, revision)
        return self._published(db, tenant)

    def publish(self, tenant, actor, expected):
        with self.connection(True) as db:
            self._expected(db, tenant, actor, expected)
            draft = self._draft(db, tenant, actor)
            if not draft:
                raise AppearanceError(409, "DRAFT_REQUIRED", "Save a private draft before publishing.")
            self._base(db, tenant, draft["baseRevision"])
            result = self._append(db, tenant, actor, draft["config"], "published")
            db.execute("DELETE FROM drafts WHERE tenant=? AND actor=?", (tenant, actor))
            return result

    def rollback(self, tenant, actor, revision, base):
        integer(revision, "revision")
        with self.connection(True) as db:
            self._base(db, tenant, base)
            row = db.execute("SELECT config FROM versions WHERE tenant=? AND revision=?", (tenant, revision)).fetchone()
            if not row:
                raise AppearanceError(404, "VERSION_NOT_FOUND", "That appearance version is unavailable.")
            try:
                config = stored_config(row["config"])
            except (AppearanceError, ValueError, TypeError, RecursionError):
                raise invalid("That historical configuration is not valid for this schema.")
            return self._append(db, tenant, actor, config, f"rollback:{revision}")

    def history(self, tenant, limit=20, before=2**31-1):
        with self.connection() as db:
            rows = db.execute("SELECT revision,actor,action,created,config FROM versions WHERE tenant=? AND revision<? ORDER BY revision DESC LIMIT ?", (tenant, before, limit)).fetchall()
            result = []
            for row in rows:
                entry = {key: row[key] for key in ("revision", "actor", "action", "created")}
                entry["changedFields"] = None
                try:
                    entry["config"] = stored_config(row["config"])
                    entry["valid"] = True
                    previous = db.execute("SELECT config FROM versions WHERE tenant=? AND revision<? ORDER BY revision DESC LIMIT 1", (tenant, row["revision"])).fetchone()
                    if previous:
                        try:
                            baseline = stored_config(previous["config"])
                            entry["changedFields"] = [key for key in SPECS if baseline[key] != entry["config"][key]]
                        except (AppearanceError, ValueError, TypeError, RecursionError):
                            pass  # No invented differences against corrupt history.
                    else:
                        entry["changedFields"] = []
                except (AppearanceError, ValueError, TypeError, RecursionError):
                    entry["valid"] = False
                result.append(entry)
            return result

    def audit(self, tenant):
        with self.connection() as db:
            return [dict(row) for row in db.execute("SELECT id,actor,action,revision,created FROM audit WHERE tenant=? ORDER BY id DESC LIMIT 50", (tenant,))]

    def validation_failed(self, tenant, actor):
        with self.connection(True) as db:
            active = db.execute("SELECT revision FROM active WHERE tenant=?", (tenant,)).fetchone()
            self._audit(db, tenant, actor, "validation-failed", active["revision"] if active else 0)


def strict_object(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ValueError("Duplicate JSON key")
        obj[key] = value
    return obj


class FixtureServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, store, port=0, principal="owner-a"):
        if principal not in PRINCIPALS:
            raise ValueError("Unknown synthetic principal")
        self.store, self.sessions, self.links = store, {}, {}
        self.principal = principal
        super().__init__(("127.0.0.1", port), Handler)
        self.hosts = {f"localhost:{self.server_port}", f"127.0.0.1:{self.server_port}"}

    def create_session(self, principal):
        tenant, owner = PRINCIPALS[principal]
        token = secrets.token_urlsafe(32)
        self.sessions[token] = {"actor": principal, "tenant": tenant, "canEdit": owner,
                                "csrf": secrets.token_urlsafe(32), "expires": time.monotonic() + 3600}
        return token

    def access_link(self):
        code = secrets.token_urlsafe(32)
        self.links[code] = self.create_session(self.principal)
        return f"http://localhost:{self.server_port}/fixture/access/{code}"


class Handler(BaseHTTPRequestHandler):
    server_version = "SyntheticAppearance"

    def log_message(self, *args):
        pass  # Access capabilities and cookie values must not enter logs.

    def response(self, status, payload, mime="application/json", extra=None):
        # HTTP/1.0 closes after refusal. Discard only a bounded, unread body so
        # pending client bytes cannot reset the socket before the error arrives.
        if not getattr(self, "body_consumed", False) and self.command != "GET":
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if 0 < length <= 16384 and not self.headers.get("Transfer-Encoding"):
                    self.body_consumed = True
                    self.rfile.read(length)
            except (ValueError, OSError):
                pass
        content = json.dumps(payload, ensure_ascii=False, allow_nan=False).encode() if mime == "application/json" else payload
        self.send_response(status)
        self.send_header("Content-Type", mime + "; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'none'; frame-ancestors 'none'; form-action 'self'")
        for key, value in (extra or {}).items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(content)

    def session(self):
        cookie = SimpleCookie()
        try:
            cookie.load(self.headers.get("Cookie", ""))
        except Exception:
            return None
        item = cookie.get("fixture_session")
        session = self.server.sessions.get(item.value) if item else None
        if session and session["expires"] > time.monotonic():
            return session
        return None

    def owner(self, tenant, write=False):
        session = self.session()
        if not session:
            raise AppearanceError(401, "SESSION_REQUIRED", "A synthetic fixture session is required.")
        if not session["canEdit"] or session["tenant"] != tenant:
            raise AppearanceError(403, "FORBIDDEN", "This principal cannot manage that appearance scope.")
        if write:
            origin = f'http://{self.headers.get("Host")}'
            if self.headers.get("Origin") != origin:
                raise AppearanceError(403, "ORIGIN_REJECTED", "Write origin is not allowed.")
            csrf = self.headers.get("X-Fixture-CSRF", "")
            if not secrets.compare_digest(csrf.encode("utf-8"), session["csrf"].encode("ascii")):
                raise AppearanceError(403, "CSRF_REJECTED", "Write validation token is missing or invalid.")
        return session

    def body(self, fields):
        if self.headers.get("Transfer-Encoding"):
            raise AppearanceError(400, "INVALID_BODY", "Transfer encoding is not supported.")
        if self.headers.get_content_type() != "application/json":
            raise AppearanceError(415, "JSON_REQUIRED", "Use application/json.")
        try:
            length = int(self.headers.get("Content-Length", "-1"))
        except ValueError:
            raise AppearanceError(400, "INVALID_BODY", "Invalid request length.")
        if length < 0 or length > 16384:
            raise AppearanceError(413, "BODY_LIMIT", "Request is missing a length or exceeds 16 KiB.")
        try:
            self.body_consumed = True
            value = json.loads(self.rfile.read(length), object_pairs_hook=strict_object,
                               parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))
        except (ValueError, UnicodeError, RecursionError):
            raise AppearanceError(400, "INVALID_JSON", "Provide valid JSON without duplicate keys.")
        if type(value) is not dict or set(value) != set(fields):
            raise invalid("Unsupported or missing request fields.")
        return value

    def dispatch(self):
        self.connection.settimeout(5)
        session = None
        try:
            for name in ("Host", "Content-Length", "Content-Type", "Origin", "Cookie", "X-Fixture-CSRF", "Transfer-Encoding"):
                if len(self.headers.get_all(name, [])) > 1:
                    raise AppearanceError(400, "AMBIGUOUS_HEADERS", "Duplicate security or framing headers are not supported.")
            host = self.headers.get("Host")
            if host not in self.server.hosts:
                raise AppearanceError(403, "HOST_REJECTED", "Only the fixture loopback host is allowed.")
            if not self.path.startswith("/") or self.path.startswith("//"):
                raise AppearanceError(400, "INVALID_TARGET", "Use a relative fixture resource path.")
            try:
                parsed = urlsplit(self.path)
            except ValueError:
                raise AppearanceError(400, "INVALID_TARGET", "Use a valid fixture resource path.")
            if parsed.fragment:
                raise AppearanceError(400, "INVALID_TARGET", "Fragments are not request resources.")
            path = parsed.path
            if self.command == "GET" and path.startswith("/fixture/access/"):
                # Same-site navigation only; cross-site bootstrap is not a login flow.
                if self.headers.get("Sec-Fetch-Site") == "cross-site":
                    raise AppearanceError(403, "ORIGIN_REJECTED", "Cross-site fixture access is not allowed.")
                token = self.server.links.pop(path.rsplit("/", 1)[-1], None)
                if not token:
                    raise AppearanceError(401, "ACCESS_EXPIRED", "Fixture access link is invalid or already used.")
                return self.response(303, b"", "text/plain", {
                    "Location": "/", "Set-Cookie": f"fixture_session={token}; HttpOnly; Secure; SameSite=Strict; Path=/; Max-Age=3600"})
            assets = {"/": ("index.html", "text/html"), "/reader": ("index.html", "text/html"),
                      "/app.js": ("app.js", "text/javascript"), "/app.css": ("app.css", "text/css")}
            if self.command == "GET" and path in assets:
                file, mime = assets[path]
                return self.response(200, (FIXTURE / file).read_bytes(), mime)
            if path == "/api/v1/session" and self.command == "GET":
                session = self.session()
                safe = {key: session[key] for key in ("actor", "tenant", "canEdit", "csrf")} if session else {"actor": "anonymous", "tenant": "a", "canEdit": False}
                return self.response(200, safe)
            match = re.fullmatch(r"/api/v1/tenants/(a|b)/(published|catalog|draft|previews|publications|resets|rollbacks|history|audit)", path)
            if not match:
                raise AppearanceError(404, "NOT_FOUND", "Fixture resource not found.")
            tenant, resource = match.groups()
            methods = {"published": {"GET"}, "catalog": {"GET"}, "draft": {"GET", "PUT", "DELETE"},
                       "previews": {"POST"}, "publications": {"POST"}, "resets": {"POST"},
                       "rollbacks": {"POST"}, "history": {"GET"}, "audit": {"GET"}}
            if self.command not in methods[resource]:
                raise AppearanceError(405, "METHOD_REJECTED", "Method is not supported for this resource.")
            store = self.server.store
            if resource == "published":
                return self.response(200, store.published(tenant))
            if resource == "catalog":
                return self.response(200, catalog())
            session = self.owner(tenant, write=self.command != "GET")
            actor = session["actor"]
            if resource == "draft":
                if self.command == "GET":
                    result = store.draft(tenant, actor)
                elif self.command == "PUT":
                    body = self.body({"config", "baseRevision", "draftRevision"})
                    result = store.save(tenant, actor, body["config"], body["baseRevision"], body["draftRevision"])
                else:
                    body = self.body({"draftRevision"})
                    result = store.discard(tenant, actor, body["draftRevision"])
            elif resource == "previews":
                body = self.body({"config"})
                config = validate(body["config"])
                result = {"source": "private-preview", "config": config, "tokens": resolve(config)}
            elif resource == "publications":
                body = self.body({"draftRevision"})
                result = store.publish(tenant, actor, body["draftRevision"])
            elif resource == "resets":
                body = self.body({"baseRevision", "draftRevision"})
                result = store.reset(tenant, actor, body["baseRevision"], body["draftRevision"])
            elif resource == "rollbacks":
                body = self.body({"baseRevision", "revision"})
                result = store.rollback(tenant, actor, body["revision"], body["baseRevision"])
            elif resource == "history":
                try:
                    query = parse_qs(parsed.query, keep_blank_values=True, max_num_fields=16)
                except ValueError:
                    raise invalid("History query exceeds supported bounds.")
                if set(query) - {"limit", "before"} or any(len(v) != 1 for v in query.values()):
                    raise invalid("Unsupported history query.")
                try:
                    limit, before = int(query.get("limit", [20])[0]), int(query.get("before", [2**31-1])[0])
                except (ValueError, TypeError):
                    raise invalid("Invalid history pagination.")
                if not 1 <= limit <= 50 or not 0 <= before <= 2**31-1:
                    raise invalid("History pagination is outside the supported range.")
                result = {"items": store.history(tenant, limit, before)}
            else:
                result = {"items": store.audit(tenant)}
            return self.response(200, result)
        except AppearanceError as error:
            if session and self.command != "GET" and error.status in (400, 413, 415, 422):
                try:
                    self.server.store.validation_failed(session["tenant"], session["actor"])
                except (sqlite3.Error, OSError):
                    pass  # Audit failure never reports a successful write or exposes raw input.
            return self.response(error.status, {"error": {"code": error.code, "message": error.message, "details": error.details}})
        except (sqlite3.Error, OSError):
            return self.response(503, {"error": {"code": "STORAGE_UNAVAILABLE", "message": "Could not confirm the operation. Preserve your inputs and reload published/history state before retrying.", "details": {}}})

    do_GET = do_POST = do_PUT = do_DELETE = do_PATCH = do_OPTIONS = dispatch


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state-dir", required=True, type=Path)
    parser.add_argument("--port", type=int, default=8772)
    parser.add_argument("--principal", choices=tuple(PRINCIPALS), default="owner-a")
    args = parser.parse_args()
    directory = args.state_dir.resolve()
    repository = Path(__file__).resolve().parents[1]
    if directory == repository or repository in directory.parents:
        parser.error("State must remain outside the product repository.")
    directory.mkdir(parents=True, exist_ok=True)
    server = FixtureServer(Store(directory / "appearance.sqlite"), args.port, args.principal)
    (directory / "access.json").write_text(json.dumps({"url": server.access_link()}), encoding="utf-8")
    print(f"Synthetic loopback fixture on port {server.server_port}; one-use link in external access.json", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
