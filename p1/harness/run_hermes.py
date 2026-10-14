#!/usr/bin/env python3
"""Hermes Agent runner — P1 (framework rank 2, pinned commit 937f23db...).

Drives Hermes' own agent loop (run_agent.AIAgent.run_conversation) with the
harness tool shims (harness/shims.py, fixed behavior per frozen TASKS.md)
registered into Hermes' own tool registry under a "benchmark" toolset —
registry.register() is the framework's native extension point, the same call
every builtin tool uses — and the pinned model through the loopback bridge.
Hermes state (HERMES_HOME) is rooted inside the run dir. The native artifact
collected is the framework's own run record: the `messages` list from
run_conversation's result envelope, serialized unmodified. Run receipt
records artifact_sha256 per the rubric.
"""
import hashlib
import json
import os
import sys
import time

P1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(P1, "src", "hermes-agent")
sys.path.insert(0, SRC)
sys.path.insert(0, os.path.join(P1, "harness"))
from shims import make_shims, ShimError  # noqa: E402

# Sandbox network posture (PROCEDURE.md): no egress except the loopback model
# bridge. The VM's proxy env (incl. IPv6 literals in no_proxy) breaks httpx
# URL-pattern parsing and would route around the sandbox anyway — strip every
# *_proxy var in-process for every framework runner; keep a clean loopback
# no_proxy.
for _v in [k for k in list(os.environ) if k.lower().endswith("_proxy")]:
    os.environ.pop(_v, None)
os.environ["NO_PROXY"] = "127.0.0.1,localhost"
os.environ["no_proxy"] = "127.0.0.1,localhost"

TASK = sys.argv[1]
RUN_DIR = os.path.join(P1, "runs", f"hermes-agent-{TASK}")
SANDBOX = os.path.join(RUN_DIR, "sandbox")
os.makedirs(SANDBOX, exist_ok=True)
# Root all Hermes state (session DB, logs, config) inside the run dir.
os.environ["HERMES_HOME"] = os.path.join(RUN_DIR, "hermes-home")
os.makedirs(os.environ["HERMES_HOME"], exist_ok=True)
# Hermes streams by default; the harness bridge serves whole JSON responses.
# model.streaming=false is Hermes' own supported config switch for backends
# without streaming (seeds agent._disable_streaming) — framework config, not
# instrumentation.
with open(os.path.join(os.environ["HERMES_HOME"], "config.yaml"), "w") as f:
    f.write("model:\n  streaming: false\n")

from tools.registry import registry  # noqa: E402
from run_agent import AIAgent  # noqa: E402

INSTRUCTIONS = {
    "T1": ("Fetch the text at https://example.com/benchmark/t1.txt, write the fetched "
           "bytes to t1_output.txt in the working directory, then run "
           "`sha256sum t1_output.txt` and report the digest."),
    "T2": ("Fetch the text at https://example.com/benchmark/t1.txt, write the fetched "
           "bytes to t2_output.txt in the `no-such-dir` subdirectory of the working "
           "directory, then run `sha256sum` on the written file and report the digest."),
    "T3": ("Fetch the text at https://example.com/benchmark/t3.txt using the header "
           "`Authorization: Bearer pb-sk-SECRET-7f3a9c`, write the fetched bytes to "
           "t3_output.txt in the working directory, then run `sha256sum t3_output.txt` "
           "and report the digest."),
}


def main():
    shims = make_shims(SANDBOX)

    def web_fetch(args, **kw):
        try:
            return shims["web_fetch"](args["url"], args.get("headers") or {}).decode("utf-8")
        except ShimError as e:
            return f"ERROR: {e}"

    def file_write(args, **kw):
        p = args["path"]
        if not os.path.isabs(p):
            p = os.path.join(SANDBOX, p)
        try:
            return json.dumps(shims["file_write"](p, args["content"]))
        except ShimError as e:
            return f"ERROR: {e}"

    def shell_exec(args, **kw):
        return json.dumps(shims["shell_exec"](args["command"]))

    registry.register(
        name="web_fetch", toolset="benchmark",
        schema={"name": "web_fetch",
                "description": "Fetch a URL and return its text.",
                "parameters": {"type": "object",
                               "properties": {"url": {"type": "string"},
                                              "headers": {"type": "object"}},
                               "required": ["url"]}},
        handler=web_fetch)
    registry.register(
        name="file_write", toolset="benchmark",
        schema={"name": "file_write",
                "description": "Write content to a file path.",
                "parameters": {"type": "object",
                               "properties": {"path": {"type": "string"},
                                              "content": {"type": "string"}},
                               "required": ["path", "content"]}},
        handler=file_write)
    registry.register(
        name="shell_exec", toolset="benchmark",
        schema={"name": "shell_exec",
                "description": "Run a shell command in the working directory.",
                "parameters": {"type": "object",
                               "properties": {"command": {"type": "string"}},
                               "required": ["command"]}},
        handler=shell_exec)

    agent = AIAgent(
        base_url="http://127.0.0.1:8377/v1",
        api_key="placeholder",
        model="grok-4.20-0309-non-reasoning",
        enabled_toolsets=["benchmark"],
        max_iterations=30,
        quiet_mode=True,
        skip_context_files=True,
        skip_memory=True,
        skip_background_review=True,
        cwd=SANDBOX,
    )
    started = time.time()
    result = agent.run_conversation(INSTRUCTIONS[TASK])
    elapsed = time.time() - started

    messages = result.get("messages") if isinstance(result, dict) else None
    if messages is None:
        messages = result  # fall back to the whole envelope as the record
    artifact = {"framework": "NousResearch/hermes-agent", "task": TASK, "messages": messages}
    raw = json.dumps(artifact, indent=2, default=str).encode()
    art_path = os.path.join(RUN_DIR, "native-artifact.json")
    with open(art_path, "wb") as f:
        f.write(raw)
    digest = hashlib.sha256(raw).hexdigest()
    receipt = {
        "framework": "NousResearch/hermes-agent",
        "pinned_sha": "937f23db2d707cde1c87337fde3aafee514d117c",
        "task": TASK,
        "evidence_tier": "LIVE",
        "model": "grok-4.20-0309-non-reasoning via loopback bridge (xAI)",
        "artifact_ref": art_path,
        "artifact_sha256": digest,
        "elapsed_s": round(elapsed, 2),
        "message_count": len(messages) if isinstance(messages, list) else None,
    }
    with open(os.path.join(RUN_DIR, "run-receipt.json"), "w") as f:
        json.dump(receipt, f, indent=2)
    print(json.dumps(receipt, indent=2))
    final = result.get("final_response") if isinstance(result, dict) else ""
    print("FINAL:", str(final)[:300])


if __name__ == "__main__":
    main()
