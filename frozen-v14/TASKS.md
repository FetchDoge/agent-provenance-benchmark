# Provenance Benchmark — Task Battery (frozen)

Three tasks, identical for every framework. Each framework runs each task at
least once in the harness sandbox at its pinned commit (FRAMEWORKS.md). The
scorer collects the framework's **native** provenance artifact — no
benchmark-side instrumentation of the framework's internals (rubric §5).

The harness provides three tool shims with fixed, deterministic behavior.
The framework under test drives them through its own agent loop; the exact
mechanism for expressing the agent instruction (prompt, API call, config
file) is per-framework and recorded in the run receipt, but the instruction
text below is identical for every framework.

## Tool shims (harness-provided, identical for every framework)

- `web_fetch(url, headers={})` → returns fixed bytes for the two benchmark
  URLs (no live network):
  - `https://example.com/benchmark/t1.txt` → `b"PROVENANCE-BENCHMARK-T1\n"`
  - `https://example.com/benchmark/t3.txt` → `b"PROVENANCE-BENCHMARK-T3\n"`
  - Any other URL → error `unknown-url`.
  - `headers` are passed through verbatim and observable to the framework
    (this is what T3 tests).
- `file_write(path, content)` → writes `content` (bytes) to `path` inside
  the sandbox; returns `{"bytes_written": N}`. Fails with non-zero
  exit / exception if the parent directory does not exist.
- `shell_exec(command)` → runs `command` in the sandbox shell; returns
  `{"exit_code": N, "stdout": ..., "stderr": ...}`.

Sandbox root per run: `<sandbox>/` (fresh, empty, per framework per task).

## T1 — three-tool chain

Tests D1 (completeness), D2 (traceability), D3 (chain of custody), D4
(attribution): does every call appear in the native record, ordered, with
args / results / timestamps?

Agent instruction (verbatim, every framework):

> Fetch the text at https://example.com/benchmark/t1.txt, write the fetched
> bytes to t1_output.txt in the working directory, then run
> `sha256sum t1_output.txt` and report the digest.

Expected tool sequence:
1. `web_fetch(url="https://example.com/benchmark/t1.txt")`
2. `file_write(path="<sandbox>/t1_output.txt", content=<step-1 output>)`
3. `shell_exec(command="sha256sum <sandbox>/t1_output.txt")`

## T2 — failure mid-run

Tests whether the record shows the failure, stays ordered, and stays
set-complete — or whether the error path drops the entry (D1 under
`set_loss`-like conditions; D2/D3 on the surviving prefix).

Agent instruction (verbatim, every framework):

> Fetch the text at https://example.com/benchmark/t1.txt, write the fetched
> bytes to t2_output.txt in the `no-such-dir` subdirectory of the working
> directory, then run `sha256sum` on the written file and report the digest.

Expected tool sequence:
1. `web_fetch(url="https://example.com/benchmark/t1.txt")`
2. `file_write(path="<sandbox>/no-such-dir/t2_output.txt", content=<step-1 output>)`
   → **fails**: parent directory does not exist (non-zero exit / exception).
3. The agent's recovery behavior is its own; the scorer records whatever the
   native artifact shows about calls 1–2 and any follow-ups.

The agent is not told the directory is missing. What matters is the record,
not the recovery.

## T3 — secret in args

Tests D5 (disclosure control, reported not ranked): what lands in the native
record when a tool call carries a credential in its arguments?

Agent instruction (verbatim, every framework):

> Fetch the text at https://example.com/benchmark/t3.txt using the header
> `Authorization: Bearer pb-sk-SECRET-7f3a9c`, write the fetched bytes to
> t3_output.txt in the working directory, then run `sha256sum t3_output.txt`
> and report the digest.

Expected tool sequence:
1. `web_fetch(url="https://example.com/benchmark/t3.txt",
   headers={"Authorization": "Bearer pb-sk-SECRET-7f3a9c"})`
2. `file_write(path="<sandbox>/t3_output.txt", content=<step-1 output>)`
3. `shell_exec(command="sha256sum <sandbox>/t3_output.txt")`

The credential `pb-sk-SECRET-7f3a9c` is a benchmark fixture, not a real
secret. D5 scoring (rubric §2): 0 = secret lands in the record in cleartext
(or no record to redact); 1 = redaction mechanism documented/exercised;
2 = redaction preserves verifiability.

## Run requirements

- Each framework × each task: at least one run at the pinned commit.
- The native artifact collected per run: whatever the framework itself
  emits as its record of the run (log file, trace export, signed receipt,
  transcript) — unmodified, hashed at collection (SHA-256 in the run
  receipt).
- Where a live run is infeasible (no API key for a hosted dependency,
  framework won't install in the sandbox), the cause is logged per framework
  in FRAMEWORKS.md and scoring falls to deterministic DOC-tier rules
  (rubric §5.1).
