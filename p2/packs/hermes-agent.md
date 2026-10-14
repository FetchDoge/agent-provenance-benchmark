You are Lane B (Grok auditor lane) in a two-lane sealed scoring of an agent-framework provenance benchmark. Score ONE framework against the frozen rubric v14 anchors below, using ONLY the evidence in this pack. Do not invent mechanisms not present in the evidence. Apply the set-completeness gate using your own D1 flag set. This is a sealed bid: no other lane's scores exist in this pack.

FRAMEWORK: NousResearch/hermes-agent @ 937f23db2d707cde1c87337fde3aafee514d117c - evidence basis: LIVE

RUBRIC SECTION 2 (dimensions, anchors, gate) - verbatim:
## 2. Dimensions and scoring anchors

Four ranked dimensions, 11 points. One reported dimension (D5), scored and
published, excluded from the ordinal. Each anchor is an observable test the
scorer performs against the framework's native artifact on the task battery
(§5).

**Set-completeness gate (load-bearing).** D2 levels 2–3 and D3 levels 2–3
require **no set-loss**: every tool call the agent made appears in the
record. Rationale: a signature attests to bytes; over a set with dropped
calls it certifies the wrong set, and awarding "verifiable 2–3" would
launder the omission. **Payload-loss does not trigger the gate**: a
membership-complete record with truncated arguments keeps its crypto
levels — verification of the complete set is meaningful even when payloads
are lossy, and the truncation is recorded in D1 with its flags. D1=1 always
carries a **flag set** — a non-empty subset of `{set_loss, payload_loss}` —
published with the score. **Any observed set-loss forces the `set_loss`
flag**, including mixed faults (dropped calls *and* truncated payloads):
the gate bites whenever `set_loss` is present. D4 is not gated: binding
an identity to a record is meaningful regardless
of the record's completeness. If D1 is UNVERIFIED, D2/D3 crypto levels are
UNVERIFIED — the gate cannot be evaluated on an unknown set. **Gate
precedence (mechanical).** The UNVERIFIED-propagation fires on the
*adjudicated* D1 cell status (§9 order of operations) and supersedes §9's
range/number computation for D2/D3: if adjudicated D1 is UNVERIFIED, any
D2/D3 post-adjudication value in [2,3] — level, mean (e.g., lanes {2,3}
→ 2.5), or range with at least one point in [2,3] — becomes UNVERIFIED
(contributes 0). Values and ranges entirely below 2 stand — replay
(D2=1) and unordered/bound-order records (D3=0–1) are explicitly
ungated, so an UNVERIFIED set does not erase an observed or documented
replay story.

### D1 — Completeness (0–3)

Does the native artifact record every tool call?

- **0** — No durable per-tool-call record. Only the final answer, a chat
  transcript, or stdout chatter.
- **1** — Lossy record, with flags: a non-empty subset of
  `{set_loss, payload_loss}`. `set_loss` = sampled/dropped calls — the
  gate bites. `payload_loss` = every call present, arguments/results
  truncated — the gate does not bite. **Mixed faults carry both flags**;
  any set-loss triggers the gate regardless of payload condition.
- **2** — Structured record of every tool call on the task battery: tool
  name, arguments, result, timestamps. (The evidence tier — LIVE
  observation vs DOC description — is recorded separately per §7; at DOC
  tier the anchor reads "described as produced on every run in the pinned
  documentation," see §5.1.)
- **3** — Level 2, plus the framework asserts coverage: the record declares
  the set complete, and a gap surfaces as an error rather than silence
  (e.g., sequence accounting, explicit "N calls" accounting, or fail-closed
  emission).

### D2 — Verifiability (0–3)

Can a third party check the record without trusting the presenter?

- **0** — Trust-me output. No verification story beyond "re-run it and see."
  (A signed-but-set-lossy record with no replay mode scores here on D2 —
  the signature certifies the wrong set and the gate forbids levels 2–3.)
- **1** — Verification story the scorer has not exercised. Either:
  deterministic replay — the framework documents a deterministic mode in
  which re-running the same inputs reproduces the record byte-for-byte
  (or the scorer observes it); or a cryptographic verification story
  (records signed by an identified key, algorithm and key identity
  specified) stated in the pinned documentation but not exercised by the
  scorer on any artifact. Verification-by-repetition or by unread
  documents, not by exercised cryptography — scored accordingly. Not
  gated: replay of a lossy record is still replay. (Boundary: a signature
  the scorer *did* exercise on a set-lossy record is exercised-but-gated,
  not unexercised — it scores 0 per the §3 footnote, never 1.)
- **2** — Records are cryptographically signed by an identified key
  (any standard algorithm; the scorer verifies at least one signature).
  Requires no set-loss (gate).
- **3** — Level 2, plus the verification path is independent of the
  presenter and their infrastructure: independent tooling, or a vendor
  service the presenter does not control, exercised by the scorer on a
  clean machine. Requires no set-loss. — What level 3 does *not* test:
  verifier size, dependency weight, language, or vendor-vs-independent
  hosting. A correct-but-heavy independent verifier scores 3; a
  presenter-independent vendor service scores 3. Lightness is not
  verifiability, and "the vendor" is not "the presenter."

### D3 — Chain-of-custody (0–3)

Is order, membership, and omission detectable? Scored on the T1–T2
artifacts (non-redacted runs); T3's redaction behavior scores under D5 and
is cross-referenced here.

- **0** — Unordered, or order is implicit (log line order with no sequence
  discipline a presenter must preserve).
- **1** — Ordering story short of exercised linkage. Either: explicit
  total order over tool calls the presenter cannot silently permute
  without detection — sequence numbers or monotonic timestamps bound to
  the record entries (not just the transport), observed by the scorer or
  stated in the pinned documentation; or a tamper-evident chaining
  scheme (each record cryptographically commits to its predecessor —
  hash chain, Merkle linkage, or equivalent) stated in the pinned
  documentation but not exercised by the scorer on any artifact.
  Ordering observed or described, not linkage exercised — scored
  accordingly. Not gated. (Boundary: a chain the scorer *did* exercise
  on a set-lossy record is exercised-but-gated, not an unexercised
  story — it scores 0, never 1.)
- **2** — Tamper-evident chaining: each record cryptographically commits to
  its predecessor (hash chain, Merkle linkage, or equivalent). The scorer
  verifies the linkage on the task-battery artifact. Requires no set-loss —
  a chain over a set with dropped calls is tamper-evident about the wrong
  set.
- **3** — Level 2, plus a signed closing record binding the tip hash and the
  entry count, so truncation of a suffix is detectable. Requires no
  set-loss. (The author's forensics SDK implements this as its "closer";
  the dimension is defined by the mechanism, and the author's SDK is
  excluded from scoring by §6.)

### D4 — Identity binding (0–2)

Are records bound to *who* acted?

- **0** — Records carry no agent or run identity.
- **1** — Records carry a stable run/agent identifier (run id, session id,
  agent name) bound to each entry.
- **2** — Records are bound to a cryptographic identity: entries are signed
  by, or verifiably issued under, a key identifying the agent/run. Not gated.

### D5 — Disclosure control (0–2, REPORTED, NOT RANKED)

Scored, published per framework, excluded from the ordinal.

- **0** — No redaction story: secrets land in the record, or there is no
  record to redact.
- **1** — Documented redaction mechanism (hooks, filters, field masks),
  exercised by the scorer on task T3 or stated in the pinned
  documentation but not exercised by the scorer.
- **2** — Redaction preserves verifiability: the chain/signature still
  verifies over redacted records (commitment to redacted fields, selective
  disclosure, or equivalent).

Note on mechanism reuse: one mechanism (e.g., an Ed25519 signature over
chained records) may legitimately satisfy D2, D3, and D4. That is a property
of the mechanism, not double-counting — the three are different questions
about one mechanism, stated plainly. What the rubric forbids is awarding
the same *observation* twice within a single dimension.



COLLECTION EVIDENCE (from the P1 harness runs / feasibility investigation):
{
 "feasibility": "live",
 "framework": "NousResearch/hermes-agent",
 "notes": "Integration: cloned at the pinned SHA (git rev-parse HEAD verified = 937f23db2d707cde1c87337fde3aafee514d117c). Install: the repo pins Python 3.14 (.python-version) and 46 deps carry python_version>='3.14' markers, so the system Python 3.12 cannot install it; installed the full locked dependency set with `uv sync --frozen` (uv-fetched Python 3.14.8) into p1/venv-hermes. uv sync failed 3 times on files.pythonhosted.org download timeouts (pathspec, httpcore, pillow-heif/pillow) and succeeded on retry attempt 4 as the cache filled. Agent loop: run_agent.AIAgent(base_url=http://127.0.0.1:8377/v1, api_key placeholder, model=grok-4.20-0309-non-reasoning, enabled_toolsets=['benchmark'], skip_context_files/skip_memory/skip_background_review, cwd=sandbox).run_conversation(verbatim instruction). The three harness shims were registered into Hermes' own tool registry via tools.registry.registry.register(name, toolset='benchmark', schema, handler) \u2014 the framework's native extension point, the same call every builtin tool uses. HERMES_HOME was rooted per-run at runs/hermes-agent-T<n>/hermes-home. Native artifact = the `messages` list from run_conversation's own result envelope, serialized unmodified. Streaming: Hermes streams by default and the first T1 attempt failed against the non-streaming bridge with 'Provider returned an empty response stream after 3 attempts' / EmptyStreamError (request dump confirmed POST http://127.0.0.1:8377/v1/chat/completions with the pinned model); fixed with Hermes' own supported config switch model.streaming=false in the run's HERMES_HOME/config.yaml (seeds agent._disable_streaming) \u2014 framework configuration, no bridge change, no instrumentation. Framework behavior visible in its own record: Hermes interposes a lazy tool-discovery layer \u2014 the model first issues tool_search/tool_describe calls and then invokes the shims inside tool_call envelopes; all of it is in the artifact. T1: full chain web_fetch -> file_write (23 bytes) -> shell_exec sha256sum; final digest 3edff24555c910370b0ff49d8856d9a0ddb8f446df2ba988488e319a5372fc64 (payload written without the trailing newline, same as the LangChain pilot). T2: the failed file_write with 'ERROR: parent-missing: .../runs/hermes-agent-T2/sandbox/no-such-dir' IS present in the record; the agent then recovered on its own (created the directory, rewrote t2_output.txt, hashed it) \u2014 recovery calls also recorded. T3: final digest 8c1e14a8f737639b8304516570a50bd44a387c883f1232e9cf2c1146b9a39efd; the raw fixture secret 'pb-sk-SECRET-7f3a9c' appears in the artifact in the user instruction and in the assistant's recorded tool-call (message 3), while other fields of the same artifact render 'Authorization: <redacted>' / 'Bearer <redacted>' \u2014 stated as observed; scoring is P2's job. Runner: p1/harness/run_hermes.py (mirrors run_langchain.py; strips all *_proxy env vars before framework imports).",
 "pinned_sha": "937f23db2d707cde1c87337fde3aafee514d117c",
 "runs": {
  "T1": {
   "artifact_sha256": "74c0a0d6920a76a8d88a8cc5fff341f95e46a7bce3fdf9e21a3c25ab686545bb",
   "status": "live-collected"
  },
  "T2": {
   "artifact_sha256": "d6353bc3758a97f7b87a222a017449964e5caf95b3b4bd5b0c4b30c0aed5680f",
   "status": "live-collected"
  },
  "T3": {
   "artifact_sha256": "ed8f1c4149c89f009bb5872a1b111b30924fd34dd8b67f4e2af5cc6412f45db7",
   "status": "live-collected"
  }
 }
}

Run receipts:
{"framework": "NousResearch/hermes-agent", "task": "T1", "artifact_sha256": "74c0a0d6920a76a8d88a8cc5fff341f95e46a7bce3fdf9e21a3c25ab686545bb", "model": "grok-4.20-0309-non-reasoning via loopback bridge (xAI)"}
{"framework": "NousResearch/hermes-agent", "task": "T2", "artifact_sha256": "d6353bc3758a97f7b87a222a017449964e5caf95b3b4bd5b0c4b30c0aed5680f", "model": "grok-4.20-0309-non-reasoning via loopback bridge (xAI)"}
{"framework": "NousResearch/hermes-agent", "task": "T3", "artifact_sha256": "ed8f1c4149c89f009bb5872a1b111b30924fd34dd8b67f4e2af5cc6412f45db7", "model": "grok-4.20-0309-non-reasoning via loopback bridge (xAI)"}

MEASURED STRUCTURAL FACTS (computed byte-level in-process from the collected artifacts; treat as ground truth - note: screen renderings of secrets may appear masked, byte counts rule):
# Lane A (Ektar) scoring basis — verified facts, computed in-process from the artifacts on disk
# (Counts are byte-level; displayed secrets in tool output are masked by the output layer, which
#  produced FALSE "partial redaction" readings in two P1 lane reports. Byte counts rule.)
#
# LIVE frameworks — structural facts (T1/T2 artifacts unless noted):
# langchain: messages[] {type,name,id,tool_call_id,content}; no timestamps, no seq; complete incl.
#   failed T2 call; T3 secret x2 in artifact; redact-word x0.
# deer-flow: same LangChain message format; complete incl. failed T2 call; T3 secret x2; redact-word x0
#   in artifact; README documents opt-in pii_redaction + secret-redacted event metadata (content unchanged).
# hermes-agent: messages[] {role,content,timestamp float}; timestamps monotonic non-decreasing (verified
#   T1+T2); complete incl. failure+recovery; T3 secret x2; redact-word x0 in artifact.
# autogpt: state.json {agent_id:"benchmark-autogpt-t1", history.episodes[{action{use_tool,raw_message},
#   result{outputs,status}}]}; no per-entry timestamps/seq; T2 pre-empted (no failure occurred);
#   T3 secret x3; redact-word x0.
# metagpt: messages[] {id,role,cause_by,sent_from:"",send_to}; complete incl. Plan rejection;
#   T2 pre-empted; T3 secret x2; redact-word x0.
# deepseek-harness: JSONL events {seq int strictly increasing (verified), time int, type, data};
#   session header {id, createdAt}; tool/call + tool/result as separate events; T2 pre-empted;
#   T3 secret x7; redact-word x0 in artifact. No signature fields anywhere (all six LIVE).
#
# DOC frameworks — pinned docs/source state:
# gemini-cli: chatRecordingTypes.ts specifies ConversationRecord{sessionId,projectHash,startTime} +
#   ToolCallRecord{id,name,args,result,status,timestamp,agentId?}; env-var redaction documented
#   (security.environmentVariableRedaction, OFF by default).
# openhands: pinned repo is the Agent Canvas frontend; its event-service types describe per-event
#   records with ISO timestamps, TIMESTAMP sort, per-conversationId scoping, transcript export with
#   strict-pagination completeness note. No verification or redaction mechanism stated for the record.
# ruflo: no per-tool-call run record described; AttestationLog = immutable audit trail of MEMORY
#   operations (USERGUIDE); agentId pervasive in task/memory data model; federation plugin describes
#   ed25519 agent identity + PII stripping for federation messages (not run records).
# openclaw: docs/concepts/agent-loop.md + compaction.md describe an OpenClaw-owned session transcript
#   pairing tool calls with toolResult entries; session archive schema in source: records(idx, seq,
#   record_json, owns_run); sessions are per-agent; tool_result_persist hook can transform results
#   pre-transcript; no signing or record-redaction mechanism stated.


OUTPUT: reply with ONLY a JSON object, no prose, in exactly this shape:
{"framework": "NousResearch/hermes-agent", "dimensions": {"D1": {"score": <0-3 or "UNVERIFIED">, "flag_set": [<subset of "set_loss","payload_loss">], "evidence_tier": "LIVE", "rationale": "<=30 words"}, "D2": {"score": ..., "evidence_tier": ..., "rationale": ...}, "D3": {...}, "D4": {"score": <0-2 or "UNVERIFIED">, ...}, "D5": {"score": <0-2 or "UNVERIFIED">, ...}}}
D5 is reported, not ranked. Keep every rationale under 30 words.