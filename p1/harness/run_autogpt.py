#!/usr/bin/env python3
"""AutoGPT runner — P1 (framework rank 4, pinned commit f8b0e0a87c38...).

Drives CLASSIC AutoGPT's own agent loop (propose_action/execute — the same
primitives its own direct_benchmark runner uses) with the harness tool shims
registered through AutoGPT's documented component mechanism
(forge.agent.protocols.CommandProvider + forge.command.@command on an Agent
subclass; see classic/original_autogpt/autogpt/agents/README.md: "The easiest
way to build your own agent is to extend the Agent class and add additional
components"). The autogpt_platform/ tree is out of scope and never touched.

Native commands are removed from the callable set via the framework's own
AppConfig.disabled_commands (Agent._remove_disabled_commands), so the only
tools the model can call are web_fetch/file_write/shell_exec (the harness
shims, fixed behavior per frozen TASKS.md) + finish. This matters: the native
set has different semantics under test (e.g. FileManagerComponent.write_to_file
auto-creates parent directories — precisely what T2 probes).

Model: the pinned bridge, via the framework's native OpenAI provider config
(OPENAI_API_BASE_URL=http://127.0.0.1:8377/v1, placeholder key). The client-side
model names are registry labels (gpt-4o / gpt-4o-mini); the bridge pins the
actual model server-side. No substitution.

Native artifact: the agent's own persisted state file — state.json written by
FileManagerComponent.save_state(), carrying the full EpisodicActionHistory
(action proposals incl. tool name/arguments, and their results), unmodified.
A byte-identical copy is placed at native-artifact.json for layout uniformity
with the pilot; the receipt hashes the original bytes.
"""
import asyncio
import hashlib
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "harness"))
from shims import ShimError, make_shims  # noqa: E402

# Sandbox network posture (PROCEDURE.md): no egress except the loopback model
# bridge. Strip every *_proxy var in-process before framework imports (the
# VM's proxy env breaks httpx URL-pattern parsing); keep a clean loopback
# no_proxy. Also pin the model endpoint + tiktoken cache before imports.
for _v in [k for k in list(os.environ) if k.lower().endswith("_proxy")]:
    os.environ.pop(_v, None)
os.environ["NO_PROXY"] = "127.0.0.1,localhost"
os.environ["no_proxy"] = "127.0.0.1,localhost"

_P1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ["OPENAI_API_KEY"] = "placeholder"
os.environ["OPENAI_API_BASE_URL"] = "http://127.0.0.1:8377/v1"
os.environ["TIKTOKEN_CACHE_DIR"] = os.path.join(_P1, ".tiktoken-cache")

from autogpt.agent_factory.configurators import create_agent_state  # noqa: E402
from autogpt.agents.agent import Agent  # noqa: E402
from autogpt.app.config import ConfigBuilder  # noqa: E402
from forge.agent.protocols import CommandProvider  # noqa: E402
from forge.command import command  # noqa: E402
from forge.config.ai_directives import AIDirectives  # noqa: E402
from forge.config.ai_profile import AIProfile  # noqa: E402
from forge.file_storage import FileStorageBackendName, get_storage  # noqa: E402
from forge.llm.providers import MultiProvider  # noqa: E402
from forge.llm.providers.openai import OpenAIModelName  # noqa: E402
from forge.models.json_schema import JSONSchema  # noqa: E402
from forge.utils.const import FINISH_COMMAND  # noqa: E402

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

KEEP_COMMANDS = {FINISH_COMMAND, "web_fetch", "file_write", "shell_exec"}
MAX_STEPS = 12
RUN_TIMEOUT_S = 240


class HarnessShimComponent(CommandProvider):
    """The three harness shims as an AutoGPT command component."""

    def __init__(self, shims, sandbox):
        self._shims = shims
        self._sandbox = sandbox

    def get_commands(self):
        yield self.web_fetch
        yield self.file_write
        yield self.shell_exec

    @command(
        names=["web_fetch"],
        description="Fetch a URL and return its text content.",
        parameters={
            "url": JSONSchema(
                type=JSONSchema.Type.STRING,
                description="The URL to fetch",
                required=True,
            ),
            "headers": JSONSchema(
                type=JSONSchema.Type.OBJECT,
                description="Optional HTTP headers to send with the request",
                required=False,
            ),
        },
    )
    def web_fetch(self, url: str, headers: dict | None = None) -> str:
        """Fetch a URL and return its text content."""
        return self._shims["web_fetch"](url, headers or {}).decode("utf-8")

    @command(
        names=["file_write"],
        description="Write content to a file at the given path.",
        parameters={
            "path": JSONSchema(
                type=JSONSchema.Type.STRING,
                description="The path of the file to write",
                required=True,
            ),
            "content": JSONSchema(
                type=JSONSchema.Type.STRING,
                description="The content to write to the file",
                required=True,
            ),
        },
    )
    def file_write(self, path: str, content: str) -> str:
        """Write content to a file at the given path."""
        p = path if os.path.isabs(path) else os.path.join(self._sandbox, path)
        return json.dumps(self._shims["file_write"](p, content))

    @command(
        names=["shell_exec"],
        description="Run a shell command in the working directory and return its output.",
        parameters={
            "command": JSONSchema(
                type=JSONSchema.Type.STRING,
                description="The shell command to run",
                required=True,
            ),
        },
    )
    def shell_exec(self, command: str) -> str:
        """Run a shell command in the working directory."""
        return json.dumps(self._shims["shell_exec"](command))


class HarnessAgent(Agent):
    """Classic AutoGPT Agent + the harness shim component (documented
    extension pattern: subclass Agent, add a component attribute)."""

    def __init__(self, *args, harness_component=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.harness_shims = harness_component


async def build_agent(task: str, run_dir: str, sandbox: str):
    shims = make_shims(sandbox)
    component = HarnessShimComponent(shims, sandbox)

    app_config = ConfigBuilder.build_config_from_env(workspace=Path(run_dir))
    app_config.smart_llm = OpenAIModelName.GPT4_O
    app_config.fast_llm = OpenAIModelName.GPT4_O_MINI
    app_config.noninteractive_mode = True
    app_config.continuous_mode = True
    app_config.temperature = 0

    agent_data = os.path.join(run_dir, "agent_data")
    file_storage = get_storage(
        FileStorageBackendName.LOCAL,
        root_path=Path(agent_data),
        restrict_to_root=True,
    )
    file_storage.initialize()

    agent_id = f"benchmark-autogpt-{task.lower()}"
    state = create_agent_state(
        agent_id=agent_id,
        task=INSTRUCTIONS[task],
        ai_profile=AIProfile(ai_name="AutoGPT"),
        directives=AIDirectives(),
        app_config=app_config,
    )
    agent = HarnessAgent(
        settings=state,
        llm_provider=MultiProvider(),
        file_storage=file_storage,
        app_config=app_config,
        harness_component=component,
    )

    # Enumerate every command the stock agent + shim component offer, then
    # disable all native commands through the framework's own config so the
    # callable set is exactly {web_fetch, file_write, shell_exec, finish}.
    cmds = await agent.run_pipeline(CommandProvider.get_commands)
    all_names = sorted({n for c in cmds for n in c.names})
    app_config.disabled_commands = [n for n in all_names if n not in KEEP_COMMANDS]
    return agent, agent_id, all_names


async def run_task(task: str) -> dict:
    run_dir = os.path.join(_P1, "runs", f"autogpt-{task}")
    sandbox = os.path.join(run_dir, "sandbox")
    os.makedirs(sandbox, exist_ok=True)

    agent, agent_id, all_names = await build_agent(task, run_dir, sandbox)

    steps = 0
    finished = False
    error = None

    async def loop():
        nonlocal steps, finished
        for _ in range(MAX_STEPS):
            proposal = await agent.propose_action()
            steps += 1
            tool = getattr(proposal, "use_tool", None)
            if tool is None or tool.name == FINISH_COMMAND:
                finished = True
                break
            await agent.execute(proposal)

    started = time.time()
    try:
        await asyncio.wait_for(loop(), timeout=RUN_TIMEOUT_S)
    except Exception as e:  # noqa: BLE001 - recorded, not hidden
        error = f"{type(e).__name__}: {e}"
    elapsed = time.time() - started

    # Persist the agent's own state (its native record) and hash it.
    await agent.file_manager.save_state()
    state_path = None
    for root, _dirs, files in os.walk(os.path.join(run_dir, "agent_data")):
        if "state.json" in files:
            state_path = os.path.join(root, "state.json")
            break
    if state_path is None:
        raise RuntimeError("agent state.json not found after save_state()")
    with open(state_path, "rb") as f:
        raw = f.read()
    art_path = os.path.join(run_dir, "native-artifact.json")
    with open(art_path, "wb") as f:
        f.write(raw)
    digest = hashlib.sha256(raw).hexdigest()

    state = json.loads(raw)
    episodes = state.get("history", {}).get("episodes", [])
    receipt = {
        "framework": "Significant-Gravitas/AutoGPT",
        "pinned_sha": "f8b0e0a87c38b67f6e6cb21f3ee03ff5584c3588",
        "task": task,
        "evidence_tier": "LIVE",
        "model": "grok-4.20-0309-non-reasoning via loopback bridge (xAI)",
        "artifact_ref": art_path,
        "artifact_sha256": digest,
        "elapsed_s": round(elapsed, 2),
        "episode_count": len(episodes),
        "steps": steps,
        "finished": finished,
        "error": error,
        "artifact_origin": state_path,
        "callable_commands": sorted(KEEP_COMMANDS),
        "disabled_native_commands": [
            n for n in all_names if n not in KEEP_COMMANDS
        ],
    }
    with open(os.path.join(run_dir, "run-receipt.json"), "w") as f:
        json.dump(receipt, f, indent=2)
    return receipt


async def probe() -> None:
    """Build the agent and enumerate commands WITHOUT any LLM call."""
    run_dir = os.path.join(_P1, "runs", "autogpt-probe")
    sandbox = os.path.join(run_dir, "sandbox")
    os.makedirs(sandbox, exist_ok=True)
    agent, _agent_id, all_names = await build_agent("T1", run_dir, sandbox)
    print("ALL COMMAND NAMES:", json.dumps(all_names))
    print("DISABLED:", json.dumps(agent.app_config.disabled_commands))
    missing = KEEP_COMMANDS - set(all_names)
    print("KEEP SET PRESENT:", not missing, "| missing:", sorted(missing))


if __name__ == "__main__":
    if sys.argv[1] == "probe":
        asyncio.run(probe())
    else:
        receipt = asyncio.run(run_task(sys.argv[1]))
        print(json.dumps(receipt, indent=2))
        eps_note = receipt["episode_count"]
        print(f"EPISODES: {eps_note} finished={receipt['finished']} error={receipt['error']}")
