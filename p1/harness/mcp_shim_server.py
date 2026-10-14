#!/usr/bin/env python3
"""MCP stdio server exposing the three harness tool shims (frozen TASKS.md).

Used by frameworks whose tool integration is MCP (e.g. deepseek-harness via
its dsh-mcp-client plugin). Behavior is exactly harness/shims.py — this is a
transport wrapper only. Sandbox root comes from the SANDBOX_ROOT env var,
set per-run by the launching patch config.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shims import make_shims, ShimError  # noqa: E402

SANDBOX = os.environ["SANDBOX_ROOT"]
os.makedirs(SANDBOX, exist_ok=True)
SHIMS = make_shims(SANDBOX)

TOOLS = [
    {
        "name": "web_fetch",
        "description": "Fetch a URL and return its text.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "url": {"type": "string"},
                "headers": {"type": "object", "additionalProperties": {"type": "string"}},
            },
            "required": ["url"],
        },
    },
    {
        "name": "file_write",
        "description": "Write content to a file path.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "path": {"type": "string"},
                "content": {"type": "string"},
            },
            "required": ["path", "content"],
        },
    },
    {
        "name": "shell_exec",
        "description": "Run a shell command in the working directory.",
        "inputSchema": {
            "type": "object",
            "properties": {"command": {"type": "string"}},
            "required": ["command"],
        },
    },
]


def call_tool(name, args):
    if name == "web_fetch":
        try:
            return SHIMS["web_fetch"](args["url"], args.get("headers") or {}).decode("utf-8"), False
        except ShimError as e:
            return f"ERROR: {e}", True
    if name == "file_write":
        p = args["path"]
        if not os.path.isabs(p):
            p = os.path.join(SANDBOX, p)
        try:
            return json.dumps(SHIMS["file_write"](p, args["content"])), False
        except ShimError as e:
            return f"ERROR: {e}", True
    if name == "shell_exec":
        return json.dumps(SHIMS["shell_exec"](args["command"])), False
    return f"ERROR: unknown tool {name}", True


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError:
            continue
        method = req.get("method")
        rid = req.get("id")
        if method == "initialize":
            result = {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "harness-shims", "version": "1.0.0"},
            }
        elif method == "tools/list":
            result = {"tools": TOOLS}
        elif method == "tools/call":
            params = req.get("params") or {}
            text, is_err = call_tool(params.get("name"), params.get("arguments") or {})
            result = {"content": [{"type": "text", "text": text}], "isError": is_err}
        elif method == "ping":
            result = {}
        else:
            if rid is not None:
                resp = {"jsonrpc": "2.0", "id": rid,
                        "error": {"code": -32601, "message": f"method not found: {method}"}}
                print(json.dumps(resp), flush=True)
            continue
        if rid is not None:
            print(json.dumps({"jsonrpc": "2.0", "id": rid, "result": result}), flush=True)


if __name__ == "__main__":
    main()
