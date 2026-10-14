You are Lane B (Grok auditor lane) in a two-lane sealed scoring of an agent-framework provenance benchmark. Score ONE framework against the frozen rubric v14 anchors below, using ONLY the evidence in this pack. Do not invent mechanisms not present in the evidence. Apply the set-completeness gate using your own D1 flag set. This is a sealed bid: no other lane's scores exist in this pack.

FRAMEWORK: openclaw/openclaw @ 9e0734be272f358832056da5c78e52b80b3e33e5 - evidence basis: DOC

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



RUBRIC SECTION 5.1 (DOC-tier forced rules - apply exactly):
### 5.1 Infeasible live runs — deterministic DOC scoring

When a live run is infeasible for a framework, the cause is logged per
framework in FRAMEWORKS.md, and every ranked dimension is scored from
DOC-tier evidence only, flagged DOC, by this forced rule — no cell is
left without a legal value:

- The score is the highest level whose anchor the pinned documentation
  satisfies **as a mechanism description**. Anchor clauses of the form
  "the scorer verifies / observes / exercises X" are read at DOC tier as
  "the documentation specifies X concretely enough to check" — named
  algorithm, identified key, specified record format and linkage rule. The
  tier carries the evidence discount; the number carries the mechanism.
  Both are printed (§7, §9).
- **DOC cap (forced).** D2 levels 2–3 and D3 levels 2–3 are unreachable
  at DOC tier: their anchors require the scorer to verify a signature or
  linkage on an artifact, which cannot be done without one. Where a level
  2–3 anchor is satisfied as a mechanism description but only via the DOC
  exercise-clause rewrite, the cell scores **exactly 1** — "at most 1"
  would license a clamp-vs-fallthrough choice the rubric does not grant.
  D1 and D4 have no scorer-exercise requirement in their anchors and
  score the documented mechanism (D1 up to 3, D4 up to 2).
- **D1 flags at DOC.** The flag set is whatever the documentation asserts
  about loss. Docs describing a lossy record (sampling, truncation,
  qualified completeness such as "may drop calls under load") → D1=1 with
  the asserted flags, and the set-completeness gate (§2) bites on
  `set_loss` exactly as at LIVE. Docs describing a structured per-call
  record with no loss asserted → scored on the D1=2/3 mechanism anchors,
  not D1=1 — D1=1's non-empty-flag rule is for records observed or
  described as lossy.
- **The gate applies to documented loss.** Documented set-loss forces the
  `set_loss` flag and the gate bites. A documented completeness assertion
  is not set-loss — but neither is it a verified complete set: D2/D3
  score exactly 1 when the 2–3 anchor is met only via the rewrite, else
  the highest satisfied anchor at or below 1.
- **UNVERIFIED stays INFERRED-only.** DOC-tier evidence always produces a
  number under this rule, never UNVERIFIED (§7).
- **Silence.** The forced number applies where the pinned documentation
  or source *states* something evaluable against the anchor (§7's word
  for the DOC tier). Where the docs/source are silent on the dimension —
  no described format, mechanism, or claim to score — there is no DOC
  evidence, and the cell is UNVERIFIED per §7 (INFERRED-only), not zero.
  A described format that lacks the anchor's element (e.g., a field list
  with no ordering discipline) is stated evidence and scores against the
  anchor — it is not silence.
- **D5 (reported, not ranked).** D5 follows the same exercise-clause
  rewrite: a documented-but-unexercised redaction mechanism scores D5=1
  (DOC). D5=2 is unreachable at DOC — it requires the scorer to check
  that verification survives redaction. The Silence rule applies: docs
  silent on redaction → UNVERIFIED, not 0. (A described record format
  with no redaction story stated evaluates to D5=0 under the anchor —
  that is stated evidence, not silence.)


PINNED DOC/SOURCE EXCERPTS:
Pinned docs state: docs/concepts/agent-loop.md lists lifecycle hook "tool_result_persist - Synchronously transforms tool results before they are written to an OpenClaw-owned session transcript"; docs/concepts/compaction.md: "OpenClaw keeps assistant tool calls paired with their matching toolResult entries". Pinned source (src/config/sessions/session-accessor.sqlite-archive-selection.ts) defines the session archive: CREATE TABLE records (idx INTEGER PRIMARY KEY, seq INTEGER NOT NULL, record_json TEXT NOT NULL, owns_run INTEGER NOT NULL). Sessions are per-agent. No signature scheme or transcript redaction mechanism is stated (Matrix channel docs use "redaction" only in the Matrix protocol sense).

COLLECTION EVIDENCE (from the P1 harness runs / feasibility investigation):
{
 "feasibility": "doc-tier",
 "framework": "openclaw/openclaw",
 "notes": "DOC-TIER: the framework would not install in this environment within the harness effort cap, and its architecture makes a lightweight harness integration impossible. Concrete evidence: (1) Architecture \u2014 OpenClaw is a multi-channel gateway/daemon product, not an embeddable agent-loop library: package.json description 'Multi-channel AI gateway with extensible messaging integrations'; the only headless one-shot path is `openclaw agent exec` (docs/cli/agent.md: 'runs one embedded agent turn without connecting to a Gateway... recommended headless entry point for CI'), which requires the full source build (openclaw.mjs -> dist/) at the pinned commit \u2014 there is no published-artifact shortcut faithful to the pin. (2) Tool integration surface exists but is build-gated: harness tools require a tool plugin via the plugin SDK (docs/plugins/sdk-entrypoints/define-tool-plugin.md, defineToolPlugin from 'openclaw/plugin-sdk/tool-plugin'); a complete plugin was authored (p1/harness/openclaw-plugin/ + openclaw-shim-bridge.py delegating to the frozen shims.py, restrictive tools.allow config, custom OpenAI-compatible provider registration per docs/gateway/config-tools/custom-providers.md) but it can only be exercised through the built CLI. (3) Install failure in this environment: `pnpm install --frozen-lockfile` (pnpm 12.5.1 per packageManager field; Node v24.20.0 present) crawls through the egress-throttled npm registry \u2014 log /tmp/openclaw-install.log shows 'Request took 30392-51411ms' for registry metadata and 'Tarball download average speed 5-45 KiB/s'; the first full install died mid-linking after 'Progress: resolved 1473, reused 512, downloaded 432, added 928' with node_modules left unlinked; a filtered retry (`--filter openclaw... --prefer-offline`) sat in resolution >10 minutes at ~1% CPU (network-bound stall) and was stopped. The pinned tree is 902 MB with a Rust crates/ workspace alongside the TypeScript monorepo, so the subsequent `pnpm build` would be a second long grind. (4) Record shape if it had run: session state is SQLite-backed in this version (src/config/sessions/session-sqlite-target-paths.ts, src/state/agent-database-admission.ts), retained via agent exec --state-dir, not a plain per-run transcript file. Clone verified at the exact pinned SHA before the install attempts. Re-attempt condition: an environment with unthrottled registry access (or a pre-populated pnpm store + dist build) would make the prepared plugin/runner path (p1/harness/run_openclaw.py) directly usable.",
 "pinned_sha": "9e0734be272f358832056da5c78e52b80b3e33e5",
 "runs": {
  "T1": {
   "artifact_sha256": null,
   "blocker": "doc-tier: framework would not install in this environment (egress-throttled npm registry; monorepo install died mid-linking after 928 packages added, filtered retry stalled in resolution) and offers no embeddable agent loop \u2014 the only headless path (openclaw agent exec) requires the full source build at the pinned commit.",
   "status": "doc-tier"
  },
  "T2": {
   "artifact_sha256": null,
   "blocker": "doc-tier: same install/architecture blocker as T1.",
   "status": "doc-tier"
  },
  "T3": {
   "artifact_sha256": null,
   "blocker": "doc-tier: same install/architecture blocker as T1.",
   "status": "doc-tier"
  }
 }
}


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
{"framework": "openclaw/openclaw", "dimensions": {"D1": {"score": <0-3 or "UNVERIFIED">, "flag_set": [<subset of "set_loss","payload_loss">], "evidence_tier": "DOC", "rationale": "<=30 words"}, "D2": {"score": ..., "evidence_tier": ..., "rationale": ...}, "D3": {...}, "D4": {"score": <0-2 or "UNVERIFIED">, ...}, "D5": {"score": <0-2 or "UNVERIFIED">, ...}}}
D5 is reported, not ranked. Keep every rationale under 30 words.