#!/usr/bin/env python3
"""OpenClaw runner — P1 (framework rank 1, pinned commit 9e0734be...).

Drives OpenClaw's own agent loop through its headless embedded entry point
(`openclaw agent exec`, the documented CI path) with the harness tool shims
exposed as an OpenClaw tool plugin (harness/openclaw-plugin/, delegating to
harness/shims.py) and the pinned model registered as a custom
OpenAI-compatible provider pointing at the loopback bridge. Tool policy is
restrictive (tools.allow = exactly the three shim tools). The native artifact
collected is the framework's own emitted run record: the session transcript
file(s) written under the retained --state-dir, unmodified.
"""
import glob
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


def main():
    task = sys.argv[1]
    p1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    harness = os.path.join(p1, "harness")
    repo = os.path.join(p1, "src", "openclaw")
    run_dir = os.path.join(p1, "runs", f"openclaw-{task}")
    sandbox = os.path.join(run_dir, "sandbox")
    state = os.path.join(run_dir, "state")
    os.makedirs(sandbox, exist_ok=True)
    os.makedirs(state, exist_ok=True)

    config = {
        "models": {
            "providers": {
                "bridge": {
                    "baseUrl": "http://127.0.0.1:8377/v1",
                    "apiKey": "placeholder",
                    "api": "openai-completions",
                    "models": [{
                        "id": "pinned",
                        "name": "Bridge Pinned",
                        "reasoning": False,
                        "input": ["text"],
                        "cost": {"input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0},
                        "contextWindow": 128000,
                        "maxTokens": 8192,
                    }],
                }
            }
        },
        "agents": {"defaults": {"model": {"primary": "bridge/pinned"}}},
        "tools": {"allow": ["web_fetch", "file_write", "shell_exec"]},
        "plugins": {
            "load": {"paths": [os.path.join(harness, "openclaw-plugin")]},
            "entries": {
                "harness-shims": {"enabled": True, "config": {"sandboxDir": sandbox}}
            },
        },
    }
    cfg_path = os.path.join(run_dir, "config.json")
    with open(cfg_path, "w") as f:
        json.dump(config, f, indent=2)

    cmd = [
        "node", os.path.join(repo, "openclaw.mjs"), "agent", "exec",
        "--config", cfg_path,
        "--state-dir", state,
        "--cwd", sandbox,
        "--model", "bridge/pinned",
        "--json",
        INSTRUCTIONS[task],
    ]
    started = time.time()
    run_error = None
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=240,
                              cwd=sandbox, env=dict(os.environ))
        stdout, stderr, rc = proc.stdout, proc.stderr, proc.returncode
    except subprocess.TimeoutExpired as e:
        stdout, stderr, rc = (e.stdout or b"").decode() if isinstance(e.stdout, bytes) else (e.stdout or ""), "", -1
        run_error = "TimeoutExpired: 240s"
    elapsed = time.time() - started
    with open(os.path.join(run_dir, "exec-stdout.txt"), "w") as f:
        f.write(stdout or "")
    with open(os.path.join(run_dir, "exec-stderr.txt"), "w") as f:
        f.write((stderr or "")[-20000:])

    # The framework's own emitted run record: session transcripts in state dir.
    transcripts = sorted(
        glob.glob(os.path.join(state, "**", "*.jsonl"), recursive=True),
        key=lambda p: os.path.getmtime(p),
    )
    raw = b""
    for t in transcripts:
        with open(t, "rb") as f:
            raw += f.read()
    art_path = os.path.join(run_dir, "native-artifact.jsonl")
    with open(art_path, "wb") as f:
        f.write(raw)
    digest = hashlib.sha256(raw).hexdigest()
    receipt = {
        "framework": "openclaw/openclaw",
        "pinned_sha": "9e0734be272f358832056da5c78e52b80b3e33e5",
        "task": task,
        "evidence_tier": "LIVE",
        "model": "grok-4.20-0309-non-reasoning via loopback bridge (xAI)",
        "artifact_ref": art_path,
        "artifact_sha256": digest,
        "elapsed_s": round(elapsed, 2),
        "exec_exit_code": rc,
        "transcript_files": [os.path.relpath(t, run_dir) for t in transcripts],
    }
    if run_error:
        receipt["run_error"] = run_error
    with open(os.path.join(run_dir, "run-receipt.json"), "w") as f:
        json.dump(receipt, f, indent=2)
    print(json.dumps(receipt, indent=2))
    print("STDOUT tail:", (stdout or "")[-300:])


if __name__ == "__main__":
    main()
