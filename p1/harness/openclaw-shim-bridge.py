#!/usr/bin/env python3
"""One-shot bridge: OpenClaw plugin (Node) -> harness tool shims (Python).

Protocol: argv[1] = tool name; env SHIM_SANDBOX = sandbox root; stdin = JSON
args object; stdout = one JSON result object {"ok": bool, "text": str} or
{"ok": false, "error": str}. Behavior mirrors the LangChain pilot wrappers
exactly: web_fetch errors surface as errors, file_write errors are returned
as an "ERROR: ..." result string, shell_exec returns its JSON result string.
The shim implementations themselves live in shims.py and are not modified.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shims import make_shims, ShimError  # noqa: E402


def main():
    tool = sys.argv[1]
    sandbox = os.environ["SHIM_SANDBOX"]
    args = json.loads(sys.stdin.read() or "{}")
    shims = make_shims(sandbox)
    try:
        if tool == "web_fetch":
            out = shims["web_fetch"](args["url"], args.get("headers") or {})
            print(json.dumps({"ok": True, "text": out.decode("utf-8")}))
        elif tool == "file_write":
            path = args["path"]
            p = path if os.path.isabs(path) else os.path.join(sandbox, path)
            try:
                res = shims["file_write"](p, args["content"])
                print(json.dumps({"ok": True, "text": json.dumps(res)}))
            except ShimError as e:
                print(json.dumps({"ok": True, "text": f"ERROR: {e}"}))
        elif tool == "shell_exec":
            res = shims["shell_exec"](args["command"])
            print(json.dumps({"ok": True, "text": json.dumps(res)}))
        else:
            print(json.dumps({"ok": False, "error": f"unknown tool {tool}"}))
    except ShimError as e:
        print(json.dumps({"ok": False, "error": str(e)}))


if __name__ == "__main__":
    main()
