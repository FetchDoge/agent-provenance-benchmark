# Provenance Benchmark — Procedure (frozen)

Harness + scoring procedure. The scoring rules are rubric §§8–9, quoted
below; the harness specification is new in this packet and frozen here.

## Harness

**Sandbox.** Each run executes in a fresh Linux sandbox (this VM's
container): empty working directory. Network egress is restricted to two
destinations only: (a) the harness's own tool shims (TASKS.md — the shims
serve fixed bytes; no live external requests), and (b) the single fixed
model endpoint defined below. All other egress is blocked at the sandbox
boundary. Wall-clock timeout per task run: 10 minutes.

**Fixed model/provider/configuration (frozen for comparability).** Every
live run uses the same model, provider, and decoding configuration so
that cross-framework differences reflect the framework, not the model:

- **Provider:** OpenAI-compatible API (the harness supplies the base URL;
  the exact endpoint is recorded in the run receipt).
- **Model:** The harness pins one OpenAI-compatible chat model for all
  runs; the model identifier is recorded in the run receipt at freeze
  time. (Selection criterion: the cheapest model that reliably follows
  tool-calling instructions; the choice is documented, not optimized per
  framework.)
- **Decoding:** temperature 0, top_p 1 (where supported). No per-framework
  tuning.
- **API key:** The harness supplies a fixed benchmark key via environment;
  the key value is never written to the native artifact path under test
  (it lives in harness env, outside the framework's record).

Where the framework cannot run against this fixed configuration (requires
a different provider, a model the harness does not supply, or will not
install in the sandbox), the run is declared infeasible, the cause is
logged per framework in FRAMEWORKS.md, and scoring falls to rubric §5.1
(deterministic DOC tier). Incompatibility with the frozen model choice is
an infeasible LIVE run, not a reason to substitute a different model.

**Driving the loop.** The agent instruction text (TASKS.md, verbatim) is
delivered through the framework's native entry point (CLI prompt, API
message, config file — per framework, recorded in the run receipt). The
three tool shims (`web_fetch`, `file_write`, `shell_exec`) are exposed
through the framework's native tool-definition mechanism. The harness
does not modify, wrap, or re-emit the framework's own record.

**Native artifact collection.** After each run, the scorer collects the
framework's native provenance artifact — whatever the framework itself
emits as its record of the run (log file, trace export, signed receipt,
transcript). The bytes are hashed (SHA-256) at collection; the hash is
the `artifact_sha256` in the observation receipt. No benchmark-side
instrumentation of the framework's internals.

**Native-artifact rule (frozen).** A native stdout/trace/log export counts
as the framework's provenance artifact **only when emitted by the
framework itself** through its own code path. The harness may capture
stdout/stderr for the run receipt's `exit_status`, but captured output is
**not** the provenance artifact unless the framework's own documentation
or code identifies that stream as its record of the run. No benchmark
wrapper, shim, or harness code may manufacture, reformat, or re-emit
provenance on the framework's behalf. If the framework emits no
identifiable record of the run, the artifact is absent (D1 cannot be
verified from an absent artifact; rubric §2 UNVERIFIED-propagation
applies).

**Run receipt.** Per (framework, task): `{framework, pinned_sha,
task, instruction_delivery, tool_binding, exit_status,
artifact_sha256, issued_at}` as a forensics-SDK receipt.

## Scoring procedure (rubric §8, verbatim)

- **Genesis receipt** commits the SHA-256 of the frozen pre-registration
  packet. Its `args` carry `{prereg_sha256, rubric_version: "v14"}`.
- **Seal receipts**: each scorer lane commits `SHA-256(canonical score
  sheet)` — a sealed bid. **No framework's scores are revealed to either
  lane until all frameworks' seal hashes exist**, and each seal hash is
  **published to the Grok project venue as the seal is made** — before any
  sheet is revealed to either lane.
- **Observation receipts**: `tool="benchmark-observe"`,
  `args={framework, dimension, task, evidence_tier, artifact_ref,
  artifact_sha256, prereg_sha256}`, `result={score, rationale}`. One
  receipt per scored (framework, dimension) cell.
- **Scoring receipts** reference the observation seqs they aggregate.
- **Closer** commits tip hash + count over the whole scoring transcript.
- **Ordering rule (mechanical):** no seal, observation, or scoring receipt
  may carry `issued_at` earlier than the pre-reg publication timestamp. A
  violation voids the board.

## Scoring procedure (rubric §9, verbatim)

- **Two scorer lanes under one principal**: Ektar and one Grok-crew bot
  (auditor lane), scoring each dimension from the same evidence artifacts
  in separate sittings.
- **Sealed bids**: each lane commits its score-sheet hash per §8; no reveal
  until all frameworks' seals exist.
- **Adjudication**: disagreements of ≤1 point → mean, spread shown.
  Disagreements >1 point → re-examination against the anchors; if
  unresolved, the cell is published as a **range** and enters the ordinal
  at its **lower bound**. A cell is scored only if **both** lanes produce
  a number: UNVERIFIED-vs-number → re-examination → UNVERIFIED if
  unresolved.
- **Flag merge and gate binding (mechanical).** D1 flag sets are
  adjudicated before D1 points; the adjudicated flag set is the **union**
  of both lanes' sets. Single-lane flags are re-examined inside this
  step: determined absent → dropped; confirmed/undetermined → stands.
  Step 3 cannot add or drop flags. The set-completeness gate binds the
  **merged** flag set: lane D1 2–3 under any non-empty merged loss-flag
  set → 1; lane D2/D3 2–3 under merged `set_loss` → 0; values licensed by
  a removed flag are re-scored with the loss premise removed unless a
  surviving flag still licenses that value (per-anchor licensing, §9).
  The merged flag set is published with the D1 cell wherever non-empty.
- **Order of operations (mechanical).** (1) Each lane scores every cell
  from the evidence, applying the gate to its own D1 flag set. (2) Flag
  merge and gate binding; flag re-examination wholly inside this step.
  (3) Per-cell point adjudication on post-gate values. (4) §2
  UNVERIFIED-propagation fires on adjudicated D1: UNVERIFIED D1 forces
  D2/D3 values in [2,3] (level, mean, or range touching [2,3]) to
  UNVERIFIED; values entirely below 2 stand. (5) The ordinal sums the
  post-gate cells: UNVERIFIED → 0, range → lower bound.
- **Coverage and the ordinal (mechanical).** Cells total = D1–D4 (D5
  reported, not ranked). Ordinal = sum over all 4 cells (UNVERIFIED → 0,
  range → lower bound). Coverage = scored/4, printed beside every total.
  **Every scored framework appears in the ordinal.** Sort: total desc,
  coverage desc, D1 ordinal-contribution desc. §6 reference rows are
  outside the ordinal set.

## Venue honesty (rubric §8, abridged)

Pre-reg packet → Notion + Grok at freeze. Seal hashes → Grok project
venue as made. Scoring transcript → Grok project as scoring completes.
These are **author-operated venues**: server timestamps and version
histories bind against *silent* rewrites, not determined rewriting.
Retention/purge-resistance: UNKNOWN (marked gap). Not third-party
anchors. Transparency-log / RFC 3161 anchoring needs separate approval.
