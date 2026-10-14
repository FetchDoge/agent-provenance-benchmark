#!/usr/bin/env python3
"""Harness model bridge — local OpenAI-compatible endpoint -> DeepSeek.

Why this exists (the gap it bridges): the frozen PROCEDURE pins ONE
OpenAI-compatible model endpoint for every framework, but the only sanctioned
DeepSeek credential path is the connector surrogate, which authd exchanges
solely for Python-urllib requests built by the connector helpers. No
framework's own HTTP client can carry it. So the harness runs this loopback
proxy: frameworks point OPENAI_BASE_URL at http://127.0.0.1:8377/v1 with any
placeholder key; the proxy forwards each request to api.deepseek.com through
the sanctioned urllib+surrogate path and returns the response verbatim.

Frozen decoding (PROCEDURE.md): temperature 0, top_p 1 are forced here so
cross-framework differences reflect the framework, not sampling. The forced
values are part of the recorded run configuration.

Usage: model_proxy.py [port] [provider] [model]
       (default 8377, xai, grok-4.20-0309-non-reasoning)
Provider note: the DeepSeek pin proved infeasible at P1 start — the connected
account returns 'Insufficient Balance' on chat completions (models list OK).
xAI is the cheapest working sanctioned endpoint; the switch happened before
any run and is recorded in run-config.json.
"""
import json
import sys
import urllib.request
import urllib.error
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

for _p in ("/opt/muse/skills/custom-connector-setup/bin",
           "/opt/muse/skills/custom-connector-setup/templates/skill/bin"):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from dynamic_credentials import add_surrogate_to_request, read_json_response, DynamicCredentialError  # noqa: E402

PROVIDERS = {
    "deepseek": ("custom.deepseek", ["api.deepseek.com"], "https://api.deepseek.com"),
    "xai": ("custom.xai", ["api.x.ai"], "https://api.x.ai/v1"),
}
_provider = sys.argv[2] if len(sys.argv) > 2 else "xai"
CREDENTIAL, ALLOWED_HOSTS, BASE = PROVIDERS[_provider]
PINNED_MODEL = sys.argv[3] if len(sys.argv) > 3 else "grok-4.20-0309-non-reasoning"


def forward(method, path, body=None):
    url = BASE + path
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    if data:
        req.add_header("Content-Type", "application/json")
    add_surrogate_to_request(req, CREDENTIAL, allowed_hosts=ALLOWED_HOSTS)
    with urllib.request.urlopen(req, timeout=300) as resp:
        return resp.status, read_json_response(resp)


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):  # keep stdout clean
        pass

    def _send(self, status, obj):
        payload = json.dumps(obj).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        if self.path.rstrip("/").endswith("/models"):
            try:
                status, out = forward("GET", "/models")
                self._send(status, out)
            except Exception as exc:  # noqa: BLE001
                self._send(502, {"error": {"message": f"bridge: {exc}"}})
        else:
            self._send(404, {"error": {"message": "not found"}})

    def do_POST(self):
        if "/chat/completions" not in self.path:
            self._send(404, {"error": {"message": "not found"}})
            return
        try:
            length = int(self.headers.get("Content-Length") or 0)
            body = json.loads(self.rfile.read(length) or b"{}")
        except Exception as exc:  # noqa: BLE001
            self._send(400, {"error": {"message": f"bad json: {exc}"}})
            return
        # Frozen configuration: one pinned model, deterministic decoding.
        body["model"] = PINNED_MODEL
        body["temperature"] = 0
        body["top_p"] = 1
        body.pop("stream", None)  # harness collects whole responses
        try:
            status, out = forward("POST", "/chat/completions", body)
            self._send(status, out)
        except urllib.error.HTTPError as exc:
            try:
                detail = exc.read().decode("utf-8", errors="replace")[:1000]
                self._send(exc.code, json.loads(detail))
            except Exception:  # noqa: BLE001
                self._send(exc.code, {"error": {"message": "upstream error"}})
        except (DynamicCredentialError, Exception) as exc:  # noqa: BLE001
            self._send(502, {"error": {"message": f"bridge: {exc}"}})


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8377
    srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"model bridge on http://127.0.0.1:{port}/v1 provider={_provider} model={PINNED_MODEL}", flush=True)
    srv.serve_forever()
