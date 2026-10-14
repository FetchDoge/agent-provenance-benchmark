#!/usr/bin/env python3
"""SSE relay — streaming-client adapter in front of the harness model bridge.

Why: deepseek-harness's pi-ai adapter speaks OpenAI Chat Completions in
streaming mode only (SSE). The harness bridge (model_proxy.py) deliberately
collects whole JSON responses. This relay bridges the two without touching
the shared bridge or the pinned endpoint: it forwards each request to the
bridge unchanged (which pins model + decoding and carries the credential),
then re-emits the returned completion as a spec-shaped SSE stream
(content/tool-call deltas, finish chunk, [DONE]).

Usage: sse_relay.py [port] [upstream_base]   (default 8378, http://127.0.0.1:8377/v1)
"""
import json
import os
import sys
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

for _v in [k for k in list(os.environ) if k.lower().endswith("_proxy")]:
    os.environ.pop(_v, None)
os.environ["no_proxy"] = "127.0.0.1,localhost"

UPSTREAM = sys.argv[2] if len(sys.argv) > 2 else "http://127.0.0.1:8377/v1"


def upstream_post(path, body):
    req = urllib.request.Request(
        UPSTREAM + path,
        data=json.dumps(body).encode("utf-8"),
        method="POST",
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=300) as resp:
        return json.loads(resp.read().decode("utf-8"))


def sse_events(comp):
    """Yield SSE data payloads for one chat completion object."""
    choice = (comp.get("choices") or [{}])[0]
    msg = choice.get("message") or {}
    base = {
        "id": comp.get("id", "chatcmpl-relay"),
        "object": "chat.completion.chunk",
        "created": comp.get("created", 0),
        "model": comp.get("model", "bridge-pinned"),
    }
    def chunk(delta, finish=None, usage=None):
        c = dict(base)
        ch = {"index": 0, "delta": delta, "finish_reason": finish}
        c["choices"] = [ch]
        if usage is not None:
            c["usage"] = usage
        return c
    yield chunk({"role": "assistant", "content": ""})
    if msg.get("content"):
        yield chunk({"content": msg["content"]})
    for i, tc in enumerate(msg.get("tool_calls") or []):
        fn = tc.get("function") or {}
        yield chunk({"tool_calls": [{
            "index": i,
            "id": tc.get("id", f"call-{i}"),
            "type": "function",
            "function": {"name": fn.get("name", ""), "arguments": fn.get("arguments", "")},
        }]})
    yield chunk({}, finish=choice.get("finish_reason") or "stop",
                usage=comp.get("usage"))


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_GET(self):
        if self.path.rstrip("/").endswith("/models"):
            req = urllib.request.Request(UPSTREAM + "/models", method="GET")
            with urllib.request.urlopen(req, timeout=60) as resp:
                payload = resp.read()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if "/chat/completions" not in self.path:
            self.send_response(404)
            self.end_headers()
            return
        length = int(self.headers.get("Content-Length") or 0)
        body = json.loads(self.rfile.read(length) or b"{}")
        want_stream = bool(body.pop("stream", False))
        try:
            comp = upstream_post("/chat/completions", body)
        except Exception as exc:  # noqa: BLE001
            payload = json.dumps({"error": {"message": f"relay: {exc}"}}).encode()
            self.send_response(502)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return
        if "choices" not in comp or not want_stream:
            payload = json.dumps(comp).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "keep-alive")
        self.end_headers()
        for ev in sse_events(comp):
            self.wfile.write(f"data: {json.dumps(ev)}\n\n".encode())
            self.wfile.flush()
        self.wfile.write(b"data: [DONE]\n\n")
        self.wfile.flush()
        # Terminate the body explicitly: some streaming clients read to EOF
        # after [DONE]; relying on handler-return close can leave them hung.
        self.close_connection = True
        try:
            import socket as _s
            self.connection.shutdown(_s.SHUT_WR)
        except OSError:
            pass


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8378
    srv = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"sse relay on http://127.0.0.1:{port}/v1 -> {UPSTREAM}", flush=True)
    srv.serve_forever()
