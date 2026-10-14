#!/usr/bin/env python3
"""LangChain pilot runner — P1 (framework rank 5, pinned commit 57236d55...).

Drives LangChain's own agent loop (langchain.agents.create_agent) with the
harness tool shims (harness/shims.py, fixed behavior per frozen TASKS.md) and
the pinned model through the loopback bridge. The native artifact collected is
the framework's own run record: the final agent state message list, serialized
unmodified. Run receipt records artifact_sha256 per the rubric.
"""
import hashlib
import json
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "harness"))
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

from langchain.agents import create_agent  # noqa: E402
from langchain_core.tools import StructuredTool  # noqa: E402
from langchain_openai import ChatOpenAI  # noqa: E402

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
    run_dir = os.path.join(p1, "runs", f"langchain-{task}")
    sandbox = os.path.join(run_dir, "sandbox")
    os.makedirs(sandbox, exist_ok=True)
    shims = make_shims(sandbox)

    def web_fetch(url: str, headers: dict | None = None) -> str:
        return shims["web_fetch"](url, headers or {}).decode("utf-8")

    def file_write(path: str, content: str) -> str:
        p = path if os.path.isabs(path) else os.path.join(sandbox, path)
        try:
            return json.dumps(shims["file_write"](p, content))
        except ShimError as e:
            return f"ERROR: {e}"

    def shell_exec(command: str) -> str:
        return json.dumps(shims["shell_exec"](command))

    tools = [
        StructuredTool.from_function(web_fetch, name="web_fetch",
                                     description="Fetch a URL and return its text."),
        StructuredTool.from_function(file_write, name="file_write",
                                     description="Write content to a file path."),
        StructuredTool.from_function(shell_exec, name="shell_exec",
                                     description="Run a shell command in the working directory."),
    ]
    model = ChatOpenAI(model="bridge-pinned", base_url="http://127.0.0.1:8377/v1",
                       api_key="placeholder", temperature=0)
    agent = create_agent(model, tools)
    started = time.time()
    result = agent.invoke({"messages": [{"role": "user", "content": INSTRUCTIONS[task]}]})
    elapsed = time.time() - started

    messages = [m.model_dump() for m in result["messages"]]
    artifact = {"framework": "langchain-ai/langchain", "task": task, "messages": messages}
    raw = json.dumps(artifact, indent=2, default=str).encode()
    art_path = os.path.join(run_dir, "native-artifact.json")
    with open(art_path, "wb") as f:
        f.write(raw)
    digest = hashlib.sha256(raw).hexdigest()
    receipt = {
        "framework": "langchain-ai/langchain",
        "pinned_sha": "57236d55d9ffc8634bda987861e6fce460aff268",
        "task": task,
        "evidence_tier": "LIVE",
        "model": "grok-4.20-0309-non-reasoning via loopback bridge (xAI)",
        "artifact_ref": art_path,
        "artifact_sha256": digest,
        "elapsed_s": round(elapsed, 2),
        "message_count": len(messages),
    }
    with open(os.path.join(run_dir, "run-receipt.json"), "w") as f:
        json.dump(receipt, f, indent=2)
    print(json.dumps(receipt, indent=2))
    final = messages[-1].get("content") if messages else ""
    print("FINAL:", str(final)[:300])


if __name__ == "__main__":
    main()
