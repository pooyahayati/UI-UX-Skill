"""Executable contract checks; fresh isolated data, no installed dependency."""
import copy
from concurrent.futures import ThreadPoolExecutor
import http.client
import json
from pathlib import Path
import tempfile
import threading
import time
import unittest

from runtime_appearance import AppearanceError, DEFAULTS, ICON_DEFAULTS, LEGACY_DEFAULTS, FixtureServer, Store, catalog, resolve, stored_config, validate


class ConfigurationContract(unittest.TestCase):
    def test_every_offered_value_resolves_and_invalid_values_fail(self):
        for key, value in [("bodySize", True), ("bodySize", 8),
                           ("bodySize", 10**400),
                           ("font", "https://example.invalid/font.woff"),
                           ("palette", "<script>"), ("lineHeight", float("nan"))]:
            candidate = dict(DEFAULTS, **{key: value})
            with self.subTest(key=key, value=value), self.assertRaises(AppearanceError):
                validate(candidate)
        for candidate in [{}, dict(DEFAULTS, role="owner"), dict(DEFAULTS, schema=99)]:
            with self.assertRaises(AppearanceError):
                validate(candidate)
        self.assertIn("--chart-series", resolve(DEFAULTS))

    def test_prepared_icon_assignments_preserve_meaning_and_reject_asset_injection(self):
        for family in ("outline", "solid"):
            for use in catalog()["icons"]["uses"]:
                for variant in ("plain", "badge"):
                    config = dict(DEFAULTS, iconFamily=family, **{use + "Icon": variant})
                    icon = resolve(config)["icons"][use]
                    self.assertEqual((icon["use"], icon["variant"]), (use, variant))
                    self.assertTrue(all(icon["states"].values()))
                    if use == "disclosure":
                        self.assertNotEqual(icon["states"]["open"], icon["states"]["closed"])
                    self.assertEqual(icon["directional"], use in ("previous", "disclosure"))
        fallback = resolve(dict(DEFAULTS, iconFamily="solid", settingsIcon="badge"))["icons"]["settings"]
        self.assertEqual((fallback["family"], fallback["fallback"]), ("outline", True))
        for key, value in [("searchIcon", "delete"), ("iconFamily", "https://invalid/icon.svg"),
                           ("searchIcon", "<svg onload=alert(1)>"), ("iconSize", 100), ("iconStroke", True)]:
            with self.subTest(key=key), self.assertRaises(AppearanceError):
                validate(dict(DEFAULTS, **{key: value}))
        with self.assertRaises(AppearanceError):
            validate(dict(DEFAULTS, svg="M0 0"))
        self.assertEqual(resolve(dict(DEFAULTS, iconFamily="solid", iconStroke=1.5))["iconStroke"], 2)

    def test_only_complete_valid_legacy_storage_is_normalized(self):
        legacy = dict(LEGACY_DEFAULTS, palette="forest", bodySize=20, spacing=24, theme="dark")
        normalized = stored_config(json.dumps(legacy))
        for key in legacy.keys() - {"schema"}:
            self.assertEqual(normalized[key], legacy[key])
        self.assertEqual((normalized["schema"], normalized["iconFamily"]), (3, "outline"))
        for bad in [dict(legacy, schema=True), dict(legacy, schema=99), dict(legacy, radius=900),
                    dict(legacy, iconFamily="solid"), {"schema": 1}, LEGACY_DEFAULTS]:
            # Valid legacy storage is supported; old requests are intentionally not.
            with self.subTest(keys=list(bad)), self.assertRaises(AppearanceError):
                validate(bad)
        for bad in [dict(legacy, radius=900), dict(legacy, iconFamily="solid"), {"schema": 1}]:
            with self.assertRaises(AppearanceError):
                stored_config(json.dumps(bad))

    def test_catalog_values_have_resolved_effect_and_prepared_contrast(self):
        baseline = resolve(DEFAULTS)
        for spec in catalog()["settings"]:
            self.assertTrue(spec["consumers"])
            for value in spec["values"]:
                candidate = dict(DEFAULTS, **{spec["key"]: value})
                with self.subTest(setting=spec["key"], value=value):
                    tokens = resolve(candidate)
                    if value != spec["default"]:
                        self.assertNotEqual(tokens, baseline)
                    self.assertGreaterEqual(int(tokens["--control-height"][:-2]), 44)
        def luminance(hex_color):
            channels = [int(hex_color[i:i+2], 16) / 255 for i in (1, 3, 5)]
            channels = [v / 12.92 if v <= .04045 else ((v + .055) / 1.055)**2.4 for v in channels]
            return sum(v * weight for v, weight in zip(channels, (.2126, .7152, .0722)))
        def contrast(a, b):
            hi, lo = sorted([luminance(a), luminance(b)], reverse=True)
            return (hi + .05) / (lo + .05)
        for treatment in ("baseline", "material"):
            for palette in ("ocean", "forest", "plum"):
                for theme in ("light", "dark"):
                    tokens = resolve(dict(DEFAULTS, treatment=treatment, palette=palette, theme=theme))
                    for surface in ("--surface", "--surface-container", "--field-background"):
                        for foreground in ("--text", "--muted", "--danger", "--action"):
                            self.assertGreaterEqual(contrast(tokens[foreground], tokens[surface]), 4.5)
                        self.assertGreaterEqual(contrast(tokens["--border"], tokens[surface]), 3)
                    self.assertGreaterEqual(contrast(tokens["--primary-text"], tokens["--primary-bg"]), 4.5)

    def test_material_preserves_foundations_and_separates_heading_role(self):
        baseline = resolve(dict(DEFAULTS, palette="forest", spacing=24, radius=0, density="compact"))
        material = resolve(dict(DEFAULTS, palette="forest", spacing=24, radius=0, density="compact",
                                treatment="material", headingFont="serif"))
        changed = {key for key in material if material[key] != baseline[key]}
        self.assertEqual(changed, {"--surface-container", "--field-background", "--heading-font",
                                   "--control-height", "treatment"})
        self.assertEqual((baseline["--control-height"], material["--control-height"]), ("44px", "48px"))
        self.assertEqual(material["--font"], baseline["--font"])
        self.assertEqual(resolve(dict(DEFAULTS, font="serif"))["--heading-font"], "Georgia, serif")
        for key, value in [("treatment", "material-expressive"), ("treatment", "<style>"),
                           ("headingFont", "https://invalid/font.woff"), ("headingFont", True)]:
            with self.subTest(key=key), self.assertRaises(AppearanceError):
                validate(dict(DEFAULTS, **{key: value}))

    def test_complete_schema_two_storage_not_requests_is_normalized(self):
        old = dict(ICON_DEFAULTS, iconFamily="solid", settingsIcon="badge", theme="dark")
        normalized = stored_config(json.dumps(old))
        self.assertEqual(normalized, {**DEFAULTS, **old, "schema": 3})
        self.assertEqual(normalized["treatment"], "baseline")
        for bad in [dict(old, treatment="material"), dict(old, iconSize=99),
                    {key: value for key, value in old.items() if key != "searchIcon"}]:
            with self.assertRaises(AppearanceError):
                stored_config(json.dumps(bad))
        with self.assertRaises(AppearanceError):
            validate(old)


class PersistedLifecycle(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="uiux-runtime-")
        self.path = Path(self.temp.name) / "appearance.sqlite"
        self.store = Store(self.path)
        self.changed = dict(DEFAULTS, palette="plum", font="serif", density="comfortable", radius=16)

    def tearDown(self):
        self.temp.cleanup()

    def save(self, actor="owner-a", base=0, draft=0, config=None):
        return self.store.save("a", actor, config or self.changed, base, draft)

    def test_private_draft_publish_restart_and_rollback(self):
        draft = self.save()
        self.assertIsNone(self.store.draft("a", "owner-a-peer"))
        self.assertEqual(self.store.published("a")["config"], DEFAULTS)
        publication = self.store.publish("a", "owner-a", draft["draftRevision"])
        self.assertEqual(publication["revision"], 1)
        self.assertEqual(Store(self.path).published("a")["config"], self.changed)
        self.assertEqual(self.store.published("b")["config"], DEFAULTS)
        restored = self.store.rollback("a", "owner-a", 0, 1)
        self.assertEqual(restored["revision"], 2)
        self.assertEqual(restored["config"], DEFAULTS)
        self.assertEqual([v["revision"] for v in self.store.history("a", 50)], [2, 1, 0])

    def test_legacy_published_draft_and_history_survive_without_rewrites(self):
        legacy = dict(LEGACY_DEFAULTS, palette="forest", font="serif", spacing=24, theme="dark")
        raw = json.dumps(legacy, indent=2)
        with self.store.connection(True) as db:
            db.execute("UPDATE versions SET config=? WHERE tenant='a' AND revision=0", (raw,))
            db.execute("INSERT INTO drafts VALUES ('a','owner-a',7,0,?)", (raw,))
            db.execute("INSERT INTO audit VALUES (7,'a','owner-a','draft-saved',7,'2026-10-04T22:00:00+00:00')")
        reopened = Store(self.path)
        normalized = stored_config(raw)
        self.assertEqual(reopened.published("a")["source"], "published")
        self.assertEqual(reopened.published("a")["config"], normalized)
        self.assertEqual(reopened.draft("a", "owner-a")["config"], normalized)
        self.assertTrue(reopened.history("a", 50)[0]["valid"])
        with reopened.connection() as db:
            self.assertEqual(db.execute("SELECT config FROM versions WHERE tenant='a'").fetchone()[0], raw)
            self.assertEqual(db.execute("SELECT config FROM drafts WHERE tenant='a'").fetchone()[0], raw)
        changed = dict(normalized, iconFamily="solid", searchIcon="badge", settingsIcon="badge", iconSize=24)
        draft = reopened.save("a", "owner-a", changed, 0, 7)
        self.assertGreater(draft["draftRevision"], 7)
        reopened.publish("a", "owner-a", draft["draftRevision"])
        self.assertEqual(Store(self.path).published("a")["config"], changed)
        self.assertCountEqual(reopened.history("a", 50)[0]["changedFields"], ["iconFamily", "searchIcon", "settingsIcon", "iconSize"])
        result = reopened.rollback("a", "owner-a", 0, 1)
        self.assertEqual(result["config"], normalized)
        with reopened.connection() as db:
            self.assertEqual(db.execute("SELECT config FROM versions WHERE tenant='a' AND revision=0").fetchone()[0], raw)
        self.assertEqual(reopened.published("b")["config"], DEFAULTS)

    def test_history_differences_are_reconstructable_without_invalid_baselines(self):
        draft = self.save()
        self.store.publish("a", "owner-a", draft["draftRevision"])
        history = self.store.history("a", 50)
        self.assertCountEqual(history[0]["changedFields"], ["palette", "font", "density", "radius"])
        self.assertEqual(history[1]["changedFields"], [])
        self.assertTrue(history[0]["valid"])
        with self.store.connection(True) as db:
            db.execute("UPDATE versions SET config=? WHERE tenant=? AND revision=0", ("not json", "a"))
        history = self.store.history("a", 50)
        self.assertIsNone(history[0]["changedFields"])
        self.assertFalse(history[1]["valid"])
        self.assertNotIn("config", history[1])

    def test_schema_two_material_migration_private_reset_restart_and_rollback(self):
        previous = dict(ICON_DEFAULTS, palette="plum", iconFamily="solid", settingsIcon="badge")
        raw = json.dumps(previous, indent=2)
        with self.store.connection(True) as db:
            db.execute("UPDATE versions SET config=? WHERE tenant='a' AND revision=0", (raw,))
            db.execute("INSERT INTO drafts VALUES ('a','owner-a',7,0,?)", (raw,))
        reopened = Store(self.path)
        normalized = stored_config(raw)
        self.assertEqual(reopened.draft("a", "owner-a")["config"], normalized)
        candidate = dict(normalized, treatment="material", headingFont="serif", density="compact")
        saved = reopened.save("a", "owner-a", candidate, 0, 7)
        self.assertEqual(reopened.published("a")["config"], normalized)
        reopened.publish("a", "owner-a", saved["draftRevision"])
        fresh = Store(self.path)
        self.assertEqual(fresh.published("a")["config"], candidate)
        self.assertCountEqual(fresh.history("a", 50)[0]["changedFields"], ["treatment", "headingFont", "density"])
        reset = fresh.reset("a", "owner-a", 1, 0)
        self.assertEqual(reset["config"], DEFAULTS)
        self.assertEqual(fresh.published("a")["config"], candidate)
        fresh.discard("a", "owner-a", reset["draftRevision"])
        self.assertEqual(fresh.rollback("a", "owner-a", 0, 1)["config"], normalized)
        with fresh.connection() as db:
            self.assertEqual(db.execute("SELECT config FROM versions WHERE tenant='a' AND revision=0").fetchone()[0], raw)
        self.assertEqual(fresh.published("b")["config"], DEFAULTS)

    def test_stale_draft_and_base_never_overwrite(self):
        own = self.save()
        peer = self.save("owner-a-peer")
        before = self.store.draft("a", "owner-a")
        with self.assertRaises(AppearanceError):
            self.save(draft=0)
        self.assertEqual(self.store.draft("a", "owner-a"), before)
        self.store.publish("a", "owner-a", own["draftRevision"])
        with self.assertRaises(AppearanceError):
            self.store.publish("a", "owner-a-peer", peer["draftRevision"])
        self.assertEqual(self.store.published("a")["revision"], 1)
        self.assertIsNotNone(self.store.draft("a", "owner-a-peer"))

    def test_concurrent_publication_has_one_winner_and_coherent_snapshot(self):
        first = self.save()
        second = self.save("owner-a-peer", config=dict(DEFAULTS, density="compact"))
        barrier = threading.Barrier(2)
        def publish(actor, draft):
            barrier.wait()
            try:
                return self.store.publish("a", actor, draft["draftRevision"])["revision"]
            except AppearanceError as error:
                return error.code
        with ThreadPoolExecutor(max_workers=2) as pool:
            futures = [pool.submit(publish, "owner-a", first), pool.submit(publish, "owner-a-peer", second)]
            outcomes = [future.result() for future in futures]
        self.assertCountEqual(outcomes, [1, "BASE_CONFLICT"])
        result = self.store.published("a")
        self.assertIn(result["config"], [first["config"], second["config"]])
        self.assertEqual(result["tokens"], resolve(result["config"]))
        self.assertEqual(len(self.store.history("a", 50)), 2)

    def test_invalid_draft_reset_discard_and_history_protection(self):
        draft = self.save()
        before = copy.deepcopy(self.store.published("a"))
        with self.assertRaises(AppearanceError):
            self.save(draft=draft["draftRevision"], config=dict(self.changed, radius=999))
        self.assertEqual(self.store.draft("a", "owner-a"), draft)
        reset = self.store.reset("a", "owner-a", 0, draft["draftRevision"])
        self.assertEqual(reset["config"], DEFAULTS)
        self.assertEqual(self.store.published("a"), before)
        self.store.discard("a", "owner-a", reset["draftRevision"])
        self.assertIsNone(self.store.draft("a", "owner-a"))
        self.assertEqual(len(self.store.history("a", 50)), 1)

    def test_invalid_missing_and_failed_load_are_whole_fallbacks(self):
        draft = self.save()
        self.store.publish("a", "owner-a", draft["draftRevision"])
        with self.store.connection() as db:
            db.execute("UPDATE versions SET config=? WHERE tenant=? AND revision=?", ('{"schema":1}', "a", 1))
        fallback = self.store.published("a")
        self.assertEqual(fallback["source"], "history-fallback")
        self.assertEqual(fallback["config"], DEFAULTS)
        with self.store.connection() as db:
            db.execute("DELETE FROM active WHERE tenant=?", ("a",))
        self.assertEqual(self.store.published("a")["source"], "history-fallback")
        with self.store.connection() as db:
            db.execute("UPDATE versions SET config=? WHERE tenant=?", ("not json", "a"))
        self.assertEqual(self.store.published("a")["source"], "defaults-fallback")
        failed = Store(self.path)
        failed.path = Path(self.temp.name) / "absent-parent" / "cannot-open.sqlite"
        state = failed.published("a")
        self.assertEqual(state["source"], "storage-fallback")
        self.assertEqual(state["config"], DEFAULTS)

    def test_deep_corrupt_storage_is_rejected_without_losing_safe_history(self):
        draft = self.save()
        self.store.publish("a", "owner-a", draft["draftRevision"])
        saved = self.save(base=1)
        corruptions = ["[" * 3000 + "0" + "]" * 3000, "x" * 16385,
                       json.dumps(DEFAULTS)[:-1] + ',"schema":1}']
        for corrupt in corruptions:
            with self.subTest(corruption_length=len(corrupt)):
                with self.store.connection(True) as db:
                    db.execute("UPDATE versions SET config=? WHERE tenant=? AND revision=1", (corrupt, "a"))
                    db.execute("UPDATE drafts SET config=? WHERE tenant=? AND actor=?", (corrupt, "a", "owner-a"))
                published = self.store.published("a")
                self.assertEqual((published["source"], published["config"]), ("history-fallback", DEFAULTS))
                history = self.store.history("a", 50)
                self.assertFalse(history[0]["valid"])
                self.assertNotIn("config", history[0])
                with self.assertRaises(AppearanceError) as rejected:
                    self.store.draft("a", "owner-a")
                self.assertEqual(rejected.exception.code, "DRAFT_UNAVAILABLE")
                with self.assertRaises(AppearanceError) as publication:
                    self.store.publish("a", "owner-a", saved["draftRevision"])
                self.assertEqual(publication.exception.code, "DRAFT_UNAVAILABLE")
        # Recovery never publishes or removes the corrupt private draft.
        self.assertEqual(saved["baseRevision"], 1)
        self.assertEqual(len(history), 2)


class HTTPBoundary(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="uiux-http-")
        self.store = Store(Path(self.temp.name) / "appearance.sqlite")
        self.server = FixtureServer(self.store)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        # Trusted test setup; no HTTP route accepts a principal selection.
        self.owner_token = self.server.create_session("owner-a")
        self.peer_token = self.server.create_session("owner-a-peer")
        self.viewer_token = self.server.create_session("viewer-a")
        self.other_token = self.server.create_session("owner-b")

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=5)
        self.temp.cleanup()

    def call(self, resource="draft", method="GET", body=None, token=None, tenant="a", headers=None, raw=None):
        path = resource if resource.startswith(("/", "http://", "https://")) else f"/api/v1/tenants/{tenant}/{resource}"
        host = f"127.0.0.1:{self.server.server_port}"
        request_headers = {"Host": host, "Content-Type": "application/json", "Origin": "http://" + host}
        if token:
            request_headers["Cookie"] = "fixture_session=" + token
            request_headers["X-Fixture-CSRF"] = self.server.sessions[token]["csrf"]
        request_headers.update(headers or {})
        connection = http.client.HTTPConnection("127.0.0.1", self.server.server_port, timeout=5)
        connection.request(method, path, body=raw if raw is not None else json.dumps(body) if body is not None else None, headers=request_headers)
        response = connection.getresponse()
        data = response.read()
        result = json.loads(data) if data and "application/json" in response.headers.get("Content-Type", "") else data
        returned_headers = dict(response.headers)
        status = response.status
        connection.close()
        return status, result, returned_headers

    def draft_body(self):
        return {"config": dict(DEFAULTS, palette="forest"), "baseRevision": 0, "draftRevision": 0}

    def protected(self):
        return {"published": self.store.published("a"), "history": self.store.history("a", 50),
                "draft": self.store.draft("a", "owner-a"), "other": self.store.published("b")}

    def test_allow_private_preview_publish_and_public_reader(self):
        code, script, script_headers = self.call("/dialog-focus.js")
        self.assertEqual(code, 200)
        self.assertEqual(script, (Path(__file__).resolve().parents[1] / "evals/fixtures/runtime-appearance/dialog-focus.js").read_bytes())
        self.assertIn("text/javascript", script_headers["Content-Type"])
        self.assertIn("frame-ancestors 'none'", script_headers["Content-Security-Policy"])
        code, draft, headers = self.call(method="PUT", body=self.draft_body(), token=self.owner_token)
        self.assertEqual(code, 200)
        self.assertIn("script-src 'self'", headers["Content-Security-Policy"])
        self.assertEqual(headers["Cache-Control"], "no-store")
        self.assertEqual(self.call(token=self.peer_token)[1], None)
        code, preview, _ = self.call("previews", "POST", {"config": draft["config"]}, self.owner_token)
        self.assertEqual((code, preview["source"]), (200, "private-preview"))
        self.assertEqual(self.call("published")[1]["config"], DEFAULTS)
        code, active, _ = self.call("publications", "POST", {"draftRevision": draft["draftRevision"]}, self.owner_token)
        self.assertEqual((code, active["revision"]), (200, 1))
        self.assertEqual(self.call("published")[1]["config"], draft["config"])
        self.assertEqual(self.call("published", tenant="b")[1]["config"], DEFAULTS)
        # Repeating a publication is a conflict, not another append.
        self.assertEqual(self.call("publications", "POST", {"draftRevision": draft["draftRevision"]}, self.owner_token)[0], 409)
        self.assertEqual(len(self.store.history("a", 50)), 2)

    def test_denied_actors_origins_tokens_and_spoofed_fields_preserve_state(self):
        before = self.protected()
        attempts = [
            ({}, 401), ({"token": self.viewer_token}, 403), ({"token": self.other_token}, 403),
            ({"token": self.owner_token, "headers": {"Origin": "https://attacker.invalid"}}, 403),
            ({"token": self.owner_token, "headers": {"X-Fixture-CSRF": "wrong"}}, 403),
            ({"token": self.owner_token, "headers": {"X-Fixture-CSRF": "é"}}, 403),
            ({"token": self.owner_token, "headers": {"Host": "attacker.invalid"}}, 403),
            ({"token": self.owner_token, "body": dict(self.draft_body(), actor="owner-b", role="owner", tenant="b")}, 422),
        ]
        for extra, expected in attempts:
            params = dict(resource="draft", method="PUT", body=self.draft_body())
            params.update(extra)
            with self.subTest(expected=expected, extra=list(extra), header_names=sorted(extra.get("headers", {}))):
                result = self.call(**params)
                self.assertEqual(result[0], expected)
                self.assertIn("code", result[1]["error"])
                self.assertEqual(self.protected(), before)
        for resource in ("draft", "history", "audit"):
            self.assertEqual(self.call(resource)[0], 401)
            self.assertEqual(self.call(resource, token=self.viewer_token)[0], 403)
            self.assertEqual(self.call(resource, token=self.owner_token, tenant="b")[0], 403)

    def test_material_http_lifecycle_and_denials_use_existing_authority(self):
        candidate = dict(DEFAULTS, treatment="material", headingFont="serif", theme="dark",
                         density="compact", iconFamily="solid", settingsIcon="badge")
        before = self.protected()
        for token, expected in [(None, 401), (self.viewer_token, 403), (self.other_token, 403)]:
            self.assertEqual(self.call("previews", "POST", {"config": candidate}, token)[0], expected)
            self.assertEqual(self.protected(), before)
        for bad in [dict(candidate, treatment="url(javascript:alert(1))"), ICON_DEFAULTS,
                    dict(candidate, css="body{display:none}"), dict(candidate, headingFont="../font.woff")]:
            self.assertEqual(self.call("previews", "POST", {"config": bad}, self.owner_token)[0], 422)
            self.assertEqual(self.protected(), before)
        code, preview, _ = self.call("previews", "POST", {"config": candidate}, self.owner_token)
        self.assertEqual((code, preview["tokens"]["treatment"]), (200, "material"))
        self.assertEqual(self.protected(), before)
        code, draft, _ = self.call("draft", "PUT", {"config": candidate, "baseRevision": 0, "draftRevision": 0}, self.owner_token)
        self.assertEqual(code, 200)
        self.assertEqual(self.call("published")[1]["config"], DEFAULTS)
        code, published, _ = self.call("publications", "POST", {"draftRevision": draft["draftRevision"]}, self.owner_token)
        self.assertEqual((code, published["config"]), (200, candidate))
        self.assertEqual(self.call("published")[1]["tokens"], preview["tokens"])
        self.assertTrue(published["tokens"]["icons"]["settings"]["fallback"])
        self.assertEqual(self.call("published", tenant="b")[1]["config"], DEFAULTS)
        self.assertEqual(self.call("rollbacks", "POST", {"revision": 0, "baseRevision": 1}, self.owner_token)[0], 200)
        self.assertEqual(self.call("published")[1]["config"], DEFAULTS)

    def test_malformed_unsafe_oversized_wrong_method_and_pagination(self):
        before = self.protected()
        attempts = [
            ({"raw": "{"}, 400),
            # Parser depth differs by Python host; either parse rejection or
            # valid JSON with an unsupported root shape is a controlled denial.
            ({"raw": "[" * 1100 + "0" + "]" * 1100}, (400, 422)),
            ({"body": dict(self.draft_body(), config=dict(DEFAULTS, bodySize=10**400))}, 422),
            ({"raw": '{"config":{},"config":{},"baseRevision":0,"draftRevision":0}'}, 400),
            ({"raw": "x" * 16385}, 413),
            ({"body": self.draft_body(), "headers": {"Content-Type": "text/plain"}}, 415),
            ({"body": dict(self.draft_body(), config=dict(DEFAULTS, font="url(javascript:alert(1))"))}, 422),
            ({"body": dict(self.draft_body(), config=dict(DEFAULTS, iconFamily="https://invalid/icon.svg"))}, 422),
            ({"body": dict(self.draft_body(), config=dict(DEFAULTS, searchIcon="delete"))}, 422),
            ({"body": dict(self.draft_body(), config=dict(DEFAULTS, searchIcon="<svg onload=alert(1)>"))}, 422),
            ({"body": dict(self.draft_body(), config=dict(DEFAULTS, svg="M0 0"))}, 422),
            ({"body": dict(self.draft_body(), config=LEGACY_DEFAULTS)}, 422),
            ({"body": dict(self.draft_body(), baseRevision=True)}, 422),
            ({"method": "PATCH", "body": self.draft_body()}, 405),
        ]
        for extra, expected in attempts:
            params = dict(resource="draft", method="PUT", token=self.owner_token)
            params.update(extra)
            with self.subTest(expected=expected):
                code = self.call(**params)[0]
                self.assertIn(code, expected if isinstance(expected, tuple) else (expected,))
                self.assertEqual(self.protected(), before)
        for query in ("limit=0", "limit=51", "limit=no", "before=-1", "role=owner", "limit=2&limit=3"):
            self.assertEqual(self.call("history?" + query, token=self.owner_token)[0], 422)

    def test_early_denial_returns_a_response_and_preserves_state(self):
        before = self.protected()
        # Early host/auth refusal can close a socket with unread request bytes.
        for _ in range(8):
            code, body, _ = self.call(method="PUT", body=self.draft_body(), token=self.owner_token,
                                     headers={"Host": "attacker.invalid"})
            self.assertEqual(code, 403)
            self.assertEqual(body["error"]["code"], "HOST_REJECTED")
        self.assertEqual(self.protected(), before)

    def test_ambiguous_headers_and_invalid_targets_preserve_state(self):
        before = self.protected()
        host = f"127.0.0.1:{self.server.server_port}"
        body = json.dumps(self.draft_body()).encode()
        valid_headers = [("Host", host), ("Content-Type", "application/json"),
                         ("Content-Length", str(len(body))), ("Origin", "http://" + host),
                         ("Cookie", "fixture_session=" + self.owner_token),
                         ("X-Fixture-CSRF", self.server.sessions[self.owner_token]["csrf"])]
        for name, value in valid_headers:
            with self.subTest(duplicate=name):
                connection = http.client.HTTPConnection("127.0.0.1", self.server.server_port, timeout=5)
                connection.putrequest("PUT", "/api/v1/tenants/a/draft", skip_host=True)
                for key, item in valid_headers + [(name, value)]:
                    connection.putheader(key, item)
                connection.endheaders(body)
                response = connection.getresponse()
                data = json.loads(response.read())
                self.assertEqual(response.status, 400)
                self.assertEqual(data["error"]["code"], "AMBIGUOUS_HEADERS")
                self.assertEqual(response.headers["Cache-Control"], "no-store")
                connection.close()
                self.assertEqual(self.protected(), before)
        for target in ("http://[broken/", "http://attacker.invalid/api/v1/tenants/a/published"):
            with self.subTest(target=target):
                code, result, headers = self.call(target)
                self.assertEqual(code, 400)
                self.assertEqual(result["error"]["code"], "INVALID_TARGET")
                self.assertEqual(headers["X-Content-Type-Options"], "nosniff")
                self.assertEqual(self.protected(), before)
        for query in ("limit=", "unknown=", "&".join(["limit=2"] * 20)):
            self.assertEqual(self.call("history?" + query, token=self.owner_token)[0], 422)
            self.assertEqual(self.protected(), before)

    def test_access_capability_is_one_use_secure_cookie_and_no_role_endpoint(self):
        link = self.server.access_link()
        path = link.split(f"localhost:{self.server.server_port}")[1]
        code, _, headers = self.call(path)
        self.assertEqual(code, 303)
        for flag in ("HttpOnly", "Secure", "SameSite=Strict", "Max-Age=3600"):
            self.assertIn(flag, headers["Set-Cookie"])
        self.assertEqual(self.call(path)[0], 401)
        self.assertEqual(self.call("/api/v1/session", "POST", {"role": "owner"})[0], 404)
        self.assertNotIn("csrf", self.call("/api/v1/session")[1])

    def test_expired_session_and_failed_storage_preserve_config(self):
        before = self.protected()
        self.server.sessions[self.owner_token]["expires"] = time.monotonic() - 1
        self.assertEqual(self.call(method="PUT", body=self.draft_body(), token=self.owner_token)[0], 401)
        self.assertEqual(self.protected(), before)
        self.owner_token = self.server.create_session("owner-a")
        original = self.store.path
        self.store.path = Path(self.temp.name) / "absent" / "failure.sqlite"
        try:
            code, public, _ = self.call("published")
            self.assertEqual((code, public["source"]), (200, "storage-fallback"))
            code, error, _ = self.call(method="PUT", body=self.draft_body(), token=self.owner_token)
            self.assertEqual((code, error["error"]["code"]), (503, "STORAGE_UNAVAILABLE"))
            self.assertNotIn("sqlite", error["error"]["message"].lower())
        finally:
            self.store.path = original
        self.assertEqual(self.protected(), before)

    def test_rejected_owner_input_is_audited_without_storing_raw_values(self):
        before = self.protected()
        body = dict(self.draft_body(), config=dict(DEFAULTS, font="untrusted-test-value"))
        self.assertEqual(self.call(method="PUT", body=body, token=self.owner_token)[0], 422)
        audit = self.call("audit", token=self.owner_token)[1]["items"]
        self.assertEqual(audit[0]["action"], "validation-failed")
        self.assertEqual(audit[0]["actor"], "owner-a")
        self.assertNotIn("untrusted-test-value", json.dumps(audit))
        self.assertEqual(self.protected(), before)


if __name__ == "__main__":
    unittest.main()
