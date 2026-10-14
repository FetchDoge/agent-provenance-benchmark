#!/usr/bin/env python3
"""deepseek-harness runner — P1 (framework rank 3, pinned commit 5badb150...).

Drives DeepSeek Harness's own agent loop (dsh headless profile, run from the
pinned source via tsx) with:
  - the pinned model through the loopback bridge, configured as a custom
    OpenAI-Completions provider in a per-run Cordis patch overlay;
  - the harness tool shims (harness/shims.py) exposed through dsh's own MCP
    client plugin (harness/mcp_shim_server.py, stdio);
  - dsh's native tool plugins disabled in the same patch, so the shim tools
    are the agent's tool surface (same posture as the other runners).
The native artifact collected is the framework's own emitted run record: the
persisted session JSONL written by dsh's session-persistence-jsonl plugin,
copied unmodified.
"""
import hashlib
import json
import os
import subprocess
import sys
import time

# Sandbox network posture (PROCEDURE.md): no egress except the loopback model
# bridge. The VM's proxy env (incl. IPv6 literals in no_proxy) breaks httpx
# URL-pattern parsing and would route around the sandbox anyway — strip every
# *_proxy var in-process for every framework runner; keep a clean loopback
# no_proxy.
for _v in [k for k in list(os.environ) if k.lower().endswith("_proxy")]:
    os.environ.pop(_v, None)
os.environ["NO_PROXY"] = "127.0.0.1,localhost"
os.environ["no_proxy"] = "127.0.0.1,localhost"

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

DISABLED_TOOLS = [
    "tool-bash", "tool-pwsh", "tool-jobs", "tool-fs", "tool-fs-search",
    "tool-skill", "tool-subagent-control", "tool-subagent-list-agents",
    "tool-subagent", "tool-subagent-fork", "tool-workflow", "tool-todo",
    "tool-goal", "tool-ralph", "tool-web", "otel", "session-telemetry-otel",
]

PATCH_TEMPLATE = """\
- id: llm-pi-ai
  config:
    providers:
      bridge:
        apiKeyEnv: BRIDGE_API_KEY
        api: openai-completions
        baseURL: http://127.0.0.1:8378/v1
        models:
          - id: bridge-pinned

- id: agent-loop
  config:
    agents:
      - id: main
        provider: bridge
        model: bridge-pinned
        cwd: {sandbox}

- id: agent-default-model
  config:
    provider: bridge
    model: bridge-pinned

- id: session-persistence-jsonl
  config:
    root: {sessions_root}
    compression: none

- insert:
    - id: harness-shims-mcp
      name: '@deepseek-ai/dsh-mcp-client'
      config:
        serverName: harness_shims
        transport: stdio
        command: python3
        args: ['{mcp_server}']
        cwd: {sandbox}
        env:
          SANDBOX_ROOT: {sandbox}

{disabled}
"""


def main():
    task = sys.argv[1]
    p1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    repo = os.path.join(p1, "src", "deepseek-harness")
    run_dir = os.path.join(p1, "runs", f"deepseek-harness-{task}")
    sandbox = os.path.join(run_dir, "sandbox")
    dsh_home = os.path.join(run_dir, "dsh-home")
    sessions_root = os.path.join(dsh_home, "sessions")
    os.makedirs(sandbox, exist_ok=True)
    os.makedirs(sessions_root, exist_ok=True)

    disabled = "\n".join(f"- id: {t}\n  disabled: true\n" for t in DISABLED_TOOLS)
    patch = PATCH_TEMPLATE.format(
        sessions_root=sessions_root,
        mcp_server=os.path.join(p1, "harness", "mcp_shim_server.py"),
        sandbox=sandbox,
        disabled=disabled,
    )
    patch_path = os.path.join(run_dir, "bench.patch.yml")
    with open(patch_path, "w") as f:
        f.write(patch)

    env = dict(os.environ)
    env["DSH_HOME"] = dsh_home
    env["BRIDGE_API_KEY"] = "placeholder"
    # dsh's pi-ai adapter is streaming-only; the shared bridge collects whole
    # JSON responses. The per-run SSE relay (harness/sse_relay.py) adapts the
    # transport in front of the same pinned bridge endpoint.
    relay = subprocess.Popen(
        [sys.executable, os.path.join(p1, "harness", "sse_relay.py"), "8378"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, env=env)
    time.sleep(1.0)
    cmd = [
        "node", "--import", "tsx/esm",
        os.path.join(repo, "apps", "cli", "src", "bin.ts"),
        "--profile", "headless",
        "--patch", patch_path,
        "--json",
        INSTRUCTIONS[task],
    ]
    started = time.time()
    # Launch from the repo root: node's --import tsx/esm resolves from cwd.
    # The agent's workspace cwd is pinned to the sandbox in the patch instead.
    try:
        proc = subprocess.run(cmd, cwd=repo, env=env, capture_output=True,
                              text=True, timeout=900)
    finally:
        relay.terminate()
    elapsed = time.time() - started
    with open(os.path.join(run_dir, "stdout.log"), "w") as f:
        f.write(proc.stdout)
    with open(os.path.join(run_dir, "stderr.log"), "w") as f:
        f.write(proc.stderr)
    print(f"exit={proc.returncode} elapsed={elapsed:.1f}s")
    print("STDOUT tail:", proc.stdout[-800:])
    if proc.returncode != 0:
        print("STDERR tail:", proc.stderr[-800:])
        sys.exit(1)

    # Collect the framework's persisted session record (unmodified bytes).
    candidates = []
    for root, _dirs, files in os.walk(sessions_root):
        for fn in files:
            candidates.append(os.path.join(root, fn))
    candidates.sort(key=lambda p: os.path.getmtime(p))
    print("session files:", candidates)
    if not candidates:
        print("NO SESSION ARTIFACT")
        sys.exit(2)
    art_path = os.path.join(run_dir, "native-artifact.jsonl")
    with open(candidates[-1], "rb") as src, open(art_path, "wb") as dst:
        raw = src.read()
        dst.write(raw)
    digest = hashlib.sha256(raw).hexdigest()
    lines = raw.decode("utf-8", errors="replace").count("\n")
    receipt = {
        "framework": "deepseek-ai/deepseek-harness",
        "pinned_sha": "5badb15009ae1756c3afe0ae0cef1faafc290ccc",
        "task": task,
        "evidence_tier": "LIVE",
        "model": "grok-4.20-0309-non-reasoning via loopback bridge (xAI)",
        "artifact_ref": art_path,
        "artifact_sha256": digest,
        "elapsed_s": round(elapsed, 2),
        "session_file": candidates[-1],
        "session_lines": lines,
    }
    with open(os.path.join(run_dir, "run-receipt.json"), "w") as f:
        json.dump(receipt, f, indent=2)
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
