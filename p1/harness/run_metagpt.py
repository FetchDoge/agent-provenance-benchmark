#!/usr/bin/env python3
"""MetaGPT runner — P1 (framework rank 10, pinned commit 11cdf466...).

Drives MetaGPT's own general agent loop (metagpt.roles.di.role_zero.RoleZero)
with the harness tool shims (harness/shims.py, fixed behavior per frozen
TASKS.md) and the pinned model through the loopback bridge.

Integration notes (structural): in this pinned version, RoleZero's
tool_execution_map is a fixed built-in set (Plan.*, Browser.*, Editor.*) and
registered registry tools are only surfaced in the prompt, never wired into
the execution map — the class provides the `_update_tool_execution()` no-op
hook (comment: "can be updated by subclass") as the extension surface. This
runner subclasses RoleZero and uses exactly that hook to (a) register the
three harness shims as executable commands, (b) bind the framework's own
Terminal.run_command command to the harness shell shim, and (c) remove the
built-in Browser.*/Editor.* commands so the loop can only act through the
provided tools. The think/act/parse/execute/record machinery is unmodified
MetaGPT. The native artifact collected is the framework's own run record:
the role's memory message list after the run, serialized unmodified.
"""
import asyncio
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

# MetaGPT resolves its project root (and thus config/config2.yaml) from
# METAGPT_PROJECT_ROOT; the pip-installed layout has no config file, which
# makes Config.default() fail validation at import. Point it at the pinned
# source clone, which ships the framework's own config/config2.yaml.
_P1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ["METAGPT_PROJECT_ROOT"] = os.path.join(_P1, "src", "metagpt")

# --- pinned model via loopback bridge: mutate MetaGPT's cached config
# singleton before any role is constructed (roles read this same instance).
from metagpt.config2 import config  # noqa: E402
from metagpt.configs.llm_config import LLMType  # noqa: E402

config.llm.api_type = LLMType.OPENAI
config.llm.base_url = "http://127.0.0.1:8377/v1"
config.llm.api_key = "placeholder"
config.llm.model = "bridge-pinned"
config.llm.proxy = None
# The bridge serves whole (non-SSE) responses; MetaGPT's LLMConfig defaults
# stream=True, whose chunk iteration over a plain JSON body yields an empty
# string and crashes RoleZero's command parser. Use the framework's own
# config switch for non-streamed completions.
config.llm.stream = False

from metagpt.actions import UserRequirement  # noqa: E402
from metagpt.roles.di.role_zero import RoleZero  # noqa: E402
from metagpt.tools.tool_registry import register_tool  # noqa: E402

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

_SHIMS = {}  # bound per-run in main()


@register_tool()
def web_fetch(url: str, headers: dict = None) -> str:
    """
    Fetch a URL and return its text.

    Args:
        url (str): The URL to fetch.
        headers (dict): Optional HTTP headers to send verbatim.

    Returns:
        str: The fetched text.
    """
    return _SHIMS["web_fetch"](url, headers or {}).decode("utf-8")


@register_tool()
def file_write(path: str, content: str) -> str:
    """
    Write content to a file path in the working directory.

    Args:
        path (str): File path, relative to the working directory or absolute.
        content (str): The content to write.

    Returns:
        str: JSON result, e.g. {"bytes_written": N}, or an ERROR string.
    """
    sandbox = _SHIMS["sandbox"]
    p = path if os.path.isabs(path) else os.path.join(sandbox, path)
    try:
        return json.dumps(_SHIMS["file_write"](p, content))
    except ShimError as e:
        return f"ERROR: {e}"


@register_tool()
def shell_exec(command: str) -> str:
    """
    Run a shell command in the working directory.

    Args:
        command (str): The shell command to run.

    Returns:
        str: JSON result with exit_code, stdout and stderr.
    """
    return json.dumps(_SHIMS["shell_exec"](command))


async def _terminal_adapter(cmd: str, daemon: bool = False) -> str:
    """Bind MetaGPT's Terminal.run_command to the harness shell shim."""
    return json.dumps(_SHIMS["shell_exec"](cmd))


class HarnessRoleZero(RoleZero):
    """RoleZero equipped with exactly the harness tools (framework hook)."""

    def _update_tool_execution(self):
        m = self.tool_execution_map
        m["web_fetch"] = web_fetch
        m["file_write"] = file_write
        m["shell_exec"] = shell_exec
        m["Terminal.run_command"] = _terminal_adapter
        for k in [k for k in m if k.startswith("Browser.") or k.startswith("Editor.")]:
            del m[k]


async def amain(task: str):
    p1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    run_dir = os.path.join(p1, "runs", f"metagpt-{task}")
    sandbox = os.path.join(run_dir, "sandbox")
    os.makedirs(sandbox, exist_ok=True)
    shims = make_shims(sandbox)
    _SHIMS.update(shims)
    _SHIMS["sandbox"] = sandbox

    # NOTE: RoleZero sets observe_all_msg_from_buffer=True, so Role's
    # _process_role_extra deliberately never calls _watch() and rc.watch
    # stays empty — in MGX it is driven by an Environment via send_to
    # addressing instead. For a standalone run, call the role's own _watch()
    # (the idiom MetaGPT examples use inside role classes) so run() observes
    # the UserRequirement message.
    role = HarnessRoleZero(tools=["web_fetch", "file_write", "shell_exec"])
    role._watch([UserRequirement])
    started = time.time()
    run_error = None
    rsp = None
    try:
        rsp = await role.run(INSTRUCTIONS[task])
    except Exception as e:  # framework crashed mid-loop; its memory is still
        run_error = f"{type(e).__name__}: {e}"  # the emitted record — collect it
    elapsed = time.time() - started

    messages = [m.model_dump() for m in role.rc.memory.get()]
    artifact = {"framework": "FoundationAgents/MetaGPT", "task": task, "messages": messages}
    raw = json.dumps(artifact, indent=2, default=str).encode()
    art_path = os.path.join(run_dir, "native-artifact.json")
    with open(art_path, "wb") as f:
        f.write(raw)
    digest = hashlib.sha256(raw).hexdigest()
    receipt = {
        "framework": "FoundationAgents/MetaGPT",
        "pinned_sha": "11cdf466d042aece04fc6cfd13b28e1a70341b1f",
        "task": task,
        "evidence_tier": "LIVE",
        "model": "grok-4.20-0309-non-reasoning via loopback bridge (xAI)",
        "artifact_ref": art_path,
        "artifact_sha256": digest,
        "elapsed_s": round(elapsed, 2),
        "message_count": len(messages),
    }
    if run_error:
        receipt["run_error"] = run_error
    with open(os.path.join(run_dir, "run-receipt.json"), "w") as f:
        json.dump(receipt, f, indent=2)
    print(json.dumps(receipt, indent=2))
    print("FINAL:", str(getattr(rsp, "content", rsp))[:300])


if __name__ == "__main__":
    asyncio.run(amain(sys.argv[1]))
