# Provenance Benchmark — Rubric v14 (DRAFT, not pre-registered)

Date: 2026-10-03 (America/Edmonton) · Status: DRAFT. No scores exist. Nothing
has been published. This document becomes binding only when frozen into the
pre-registration packet (hash recorded, published) — until then every word is
revisable.

**What changed from v13 and why.** Auditor round 13
(receipt-auditor-rubric-v13.log) returned **HOLDS-WITH-FINDINGS** —
all v13 repair claims verified (general principle covers
suppression, direct D1=1, and direct D2/D3 0s; surviving-flag scope
closes the partial-drop two-board; both falsifiers match the five
steps) — with one MEDIUM finding, verified genuine against the body:
the v13 scoping ("provided the drop leaves no loss flag standing")
is too blunt. Cross-flag partial drop — lane A D2=0,
signature exercised, private `{set_loss}`, vs standing
`{payload_loss}` after `set_loss` dropped — blocks the correction
even though `payload_loss` does not license D2/D3 values at all
(§2), leaving the 0 unlicensed with no sentence assigning a number.
(The adversary's round-13 pass was still running when v14 was
drafted; v14 is DRAFT and unfrozen.) Repair:

1. **Per-anchor licensing scoping (auditor MEDIUM).** The proviso
   now reads "unless a surviving loss flag still licenses that
   value," with the licensing rules stated: D1=1 and D1 suppression
   are licensed by any non-empty flag subset (any standing flag
   blocks their correction — the round-12 hit-2 fix preserved);
   D2/D3 suppression and exercised-but-gated 0s are licensed by
   `set_loss` only, per §2, so a standing `payload_loss` alone does
   not block their correction. The auditor's falsifier now resolves
   to D2=2 beside `{payload_loss}` — licensed, since payload-loss
   does not gate D2/D3 — and is pinned alongside the D1/D2
   falsifiers.

Unchanged from v13: everything else — the coverage denominator and
missing=0 ordinal; the mixed-fault flag set with set-loss precedence;
loss (d) as a count; the ranged perfect-tracing ceiling; seal hashes
published per-seal before any reveal; §6 authorship exclusion; D5
reported-not-ranked; anchor honesty with UNKNOWN retention marked;
the "scored" definition and D1 ordinal-contribution sort key;
deterministic DOC scoring (§5.1) with the forced exactly-1 cap; the
§3 DOC-profile row; docs-silence → UNVERIFIED; D5 at DOC; the
straddling-range pin; flag re-examination wholly inside step 2 with
the determined-absent → drop production rule; step 3 cannot add or
drop flags; D1 2–3→1 under any non-empty merged loss-flag set;
D2/D3 2–3→0 under merged `set_loss` only; merged flags published
wherever non-empty; the general correction principle itself
(determined-absent supersedes contrary observation; complete-record
re-score).
## 0. What this benchmark is

A public rubric + leaderboard measuring **agent-level provenance** — what a
framework records about its own agents' tool calls, and whether that record
survives an adversarial presenter — across ~10 agent frameworks.

It answers one question: *when an agent built on framework F acts, can
someone else later establish what happened, who did it, in what order, and
whether the record is complete — without trusting the person showing the
record?*

It does not measure agent quality, task success, safety policy, or cost. A
framework can top this board and still build bad agents; a framework can
score zero here and still build excellent ones. That separation is deliberate
and stated.

## 1. Definitions

- **Provenance record**: the framework's native durable artifact describing
  tool calls made during an agent run (trace file, event log, transcript —
  whatever the framework itself emits, unmodified by the benchmark).
- **Presenter**: whoever hands you a provenance record. Assumed adversarial
  for scoring purposes: they may omit, reorder, or rewrite entries if the
  mechanism lets them.
- **Complete**: every tool call the agent made appears in the record, and
  the record says so in a checkable way. Completeness has two separable
  faults: **set-loss** (calls dropped or sampled — the set is wrong) and
  **payload-loss** (every call present, but arguments/results truncated —
  the set is right, the payload is lossy).
- **Verifiable**: a third party can check the record's authenticity without
  trusting the presenter.
- **Chain-of-custody**: the record's ordering and membership are
  tamper-evident — omission or reordering is detectable, not just unlikely.

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

## 3. Why these weights, and what the board can falsify (stated honestly)

The weights encode a judgment, stated plainly: **audit-grade provenance is
tamper-evidence over a set-complete record — in that order.** Set-completeness
comes first because a signature cannot repair a dropped call (the gate,
§2). Tamper-evidence comes second because "the record survived an
adversarial presenter" is what the benchmark exists to measure. ("Complete"
here means set-complete — every call present. A payload-lossy set-complete
record with full crypto outranking a D1=3 tracing record is the gate
working as designed, not a contradiction of the thesis.)

The ordinal is D1+D2+D3+D4 = **11 points**, and it **encodes the thesis**:
tamper-evidence over a complete record outranks completeness alone. That is
the benchmark's frozen, disclosed judgment — not a discovery the board could
make, and v14 does not pretend otherwise.

| Profile | D1 | D2 | D3 | D4 | Total /11 |
|---|---|---|---|---|---|
| Perfect tracing, zero crypto | 3 | 0–1 | 0–1 | 0–1 | **3–6** |
| Set-lossy (dropped calls) + full crypto | 1† | 0–1 | 0–1 | 2 | **3–5** |
| Mixed set+payload loss + full crypto | 1§ | 0–1 | 0–1 | 2 | **3–5** |
| Payload-lossy (set complete) + full crypto | 1‡ | 3 | 3 | 2 | **9** |
| Structured records (D1=2) + full crypto | 2 | 3 | 3 | 2 | 10 |
| Complete + full crypto (D1=3, D2=3, D3=3, D4=2) | 3 | 3 | 3 | 2 | 11 |
| DOC-only (live infeasible), docs claim signed + chained complete records | 2¶ | 1¶ | 1¶ | 2¶ | **6** |

† `set_loss` flag — gate bites. ‡ `payload_loss` flag — gate does not bite.
§ both flags — any set-loss triggers the gate, so the mixed fault is capped
like the set-lossy row; flagging payload-only on a mixed fault is forbidden.
D2=0 for the set-lossy and mixed rows unless deterministic replay is
observed (an exercised-but-gated signature is not an unexercised story —
D2=1's boundary clause, §2).
¶ Every cell tier DOC, flagged (§5.1): the numbers describe the mechanism
*as documented*. D1 scores the documented mechanism (tier de-embedded from
the anchor); D2/D3 score exactly 1 — forced, not capped — because levels
2–3 require the scorer to exercise the crypto; D4 has no exercise
requirement. The DOC tier is printed with every score — a reader who
discounts unexercised claims can re-weight to zero from the published
components.

The perfect-tracing row is a **ceiling**, not a derivation: 6 requires
observing deterministic replay (D2=1), bound order (D3=1), *and* a run id
(D4=1). A tracing record with none of those scores D1=3 only — total 3.

**What the board can falsify, pre-registered** — the losses that must be
possible, and are (b, c, e) — plus one published count that claims no
consequence (d):

- **(b)** The median clusters low. Nothing forces high scores; a low median
  cuts the "signed receipts are the bar" claim in the ecosystem as found.
- **(c)** Per-dimension views contradict the ordinal. Components and tiers
  are published; any reader can re-rank, and the ordinal is labeled the
  *thesis-weighted view*.
- **(d)** The count of frozen frameworks achieving D1≥2 ∧ D2≥2 is
  published. A count of zero is a finding about the field — no consequence
  for the instrument is claimed.
- **(e)** A framework the thesis disfavors wins a dimension that matters:
  e.g., a pure-tracing framework takes D1=3 across the battery while
  crypto-heavy entries sit at D1=1 `set_loss` — visible in the published
  components whatever the ordinal says.

What is NOT claimed: that the ordinal could rank pure tracing above the
complete + full-crypto row. Under the stated question it cannot, and the
rubric says so instead of staging a forced test as an open one.

## 4. Framework selection (mechanical rank, auditable discretion)

Cherry-picking frameworks is the easiest way to rig a benchmark. The
universe predicate ("primary abstraction is an agent loop that issues tool
calls") is a human judgment; v14 does not pretend otherwise. What is
mechanical, and what is auditable:

1. **Candidate enumeration (mechanical, pre-registered):** the exact method
   is frozen in the pre-reg packet — e.g., "GitHub topic:ai-agents,
   ≥1,000 stars, as of <freeze date>" UNION the repos listed in two named
   awesome-lists at frozen commits. The query text, the list names, and
   their frozen commits are recorded verbatim.
2. **Universe predicate (human, logged):** from the candidates, include a
   repo iff its primary abstraction is an agent loop that issues tool
   calls. Exclude by rule: pure workflow-automation UIs (human-wired DAGs,
   not agent-issued calls), pure chat wrappers with no tool abstraction,
   single-vertical agents, closed-source or non-OSI-licensed repos.
   **Every candidate appears in FRAMEWORKS.md with include/reject and, for
   rejects, the reason in one line.** The log makes discretion auditable
   after the fact; it is honestly labeled "auditable discretion," not
   "cherry-pick-proof."
3. **Rank (mechanical):** included repos ranked by stargazers as of the
   freeze date; top 10. Tie-breaks: most recent commit, then oldest repo
   creation date.
4. **Commit pin (mechanical):** the evaluated commit is the default-branch
   HEAD SHA as of the freeze timestamp (GitHub API), recorded per
   framework. No cherry-picked parents, no floating "latest."
5. The enumeration script and its raw output are committed to the packet.

The list is **not** asserted in this draft. Any names in working notes
before the freeze are candidates, not selections.

## 5. Task battery (frozen, identical for every framework)

Three tasks. Each framework runs each task at least once in the harness
sandbox at the pinned commit. The scorer collects the framework's **native**
provenance artifact — no benchmark-side instrumentation of the framework's
internals.

- **T1 — three-tool chain**: `web-fetch` → `file-write` → `shell-exec`,
  fixed inputs. Tests: does every call appear, ordered, with
  args/results/timestamps?
- **T2 — failure mid-run**: the second tool call errors (non-zero exit /
  exception). Tests: does the record show the failure, stay ordered, and
  stay set-complete — or does the error path drop the entry?
- **T3 — secret in args**: a tool call carries a credential in its
  arguments. Tests: what lands in the native record (feeds D5).

Where a live run is infeasible (no API key for a hosted dependency,
framework won't install in the sandbox), the dimension is scored from
DOC-tier evidence and flagged — see §7. A dimension resting only on
INFERRED is marked `UNVERIFIED`, not zero; absence of evidence is not
evidence of absence.

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

## 6. His frameworks: marked, not scored

Interlock, AEGIS, and interlock-forensics are **excluded from scoring by
rule** and appear on the leaderboard only as marked reference rows:

> `interlock-forensics — author's framework — NOT SCORED (self-grading
> exclusion, pre-registered)`

No ordinal position, no total, no dimension scores from this benchmark. The
exclusion is mechanical (authorship), not discretionary, so it cannot be
quietly lifted for a favorable version. If a future independent party scores
them with this rubric, that row is theirs to add — not his. (Attacked twice
by the adversary; held both times. Unchanged.)

## 7. Evidence tiers (claim tiers for every scored observation)

Every dimension score cites evidence at one of three tiers:

- **LIVE** — observed in a harness run at the pinned commit. Strongest.
- **DOC** — stated in the framework's documentation or source at the pinned
  commit; mechanism not exercised by the scorer.
- **INFERRED** — scorer judgment from partial evidence. Flagged in the
  leaderboard; a dimension resting only on INFERRED is marked UNVERIFIED.

The leaderboard shows the tier per dimension per framework, plus the merged
D1 flag set wherever it is non-empty. A reader can see exactly how much of any score was watched happen. The tier is part of the sealed score
sheet (§9) — a lane cannot quietly upgrade DOC to LIVE after the seals.

## 8. Dogfooding: the benchmark's own evidence chain

The benchmark eats its own cooking. All scoring evidence is recorded as a
**forensics-SDK transcript** (ProvenanceAttestation v1):

- **Genesis receipt** commits the SHA-256 of the frozen pre-registration
  packet. Its `args` carry `{prereg_sha256, rubric_version: "v14"}`.
- **Seal receipts**: each scorer lane commits `SHA-256(canonical score
  sheet)` — a sealed bid. **No framework's scores are revealed to either
  lane until all frameworks' seal hashes exist**, and each seal hash is
  **published to the Grok project venue as the seal is made** — before any
  sheet is revealed to either lane. The version history makes a
  re-seal-after-reading detectable — **provided the venue retains its
  history** (§10.4) — not impossible; if history is purged, the re-seal is
  not detectable at all. This **constrains**
  cross-framework adaptation to publication order; it does not kill it,
  and v14 does not claim otherwise. Reveal receipts follow, carrying the
  sheets.
- **What seals are and aren't.** The lanes score in separate sittings from
  the same evidence artifacts. The seal is a hash commitment against
  *silent* alteration of a sheet after sealing — it is process, not
  cryptographic blindness. Under one principal a lane could read the other
  sheet and re-seal before any external publication; v14 names that residual
  instead of implying the ceremony prevents it. Correlated bias between the
  lanes is the known residual (§10).
- **Observation receipts**: `tool="benchmark-observe"`,
  `args={framework, dimension, task, evidence_tier, artifact_ref,
  artifact_sha256, prereg_sha256}`, `result={score, rationale}`. One
  receipt per scored (framework, dimension) cell. `artifact_sha256` binds
  the native artifact bytes the score rests on. (A hash is a commitment to
  bytes, not the bytes — a reader can re-weight published scores but
  cannot re-observe from a hash alone. Stated, not hidden.)
- **Scoring receipts** reference the observation seqs they aggregate.
- **Closer** commits tip hash + count over the whole scoring transcript.
- **Ordering rule (mechanical):** no seal, observation, or scoring receipt
  may carry `issued_at` earlier than the pre-reg publication timestamp. The
  writeup verifies this from the chain; a violation voids the board.
- **Anchoring, honestly labeled.** The pre-reg packet is published to
  Notion + Grok at freeze; the scoring transcript is published to the Grok
  project as scoring completes, and seal hashes are published there as
  each seal is made (§8). These are **author-operated venues** — their
  server timestamps and version histories bind the author against *silent*
  rewrites (an edit leaves history to explain), not against determined
  rewriting. The "single-principal" label rests on the freeze-time
  publication receipts (account/workspace identifiers recorded in the
  packet manifest), not on this rubric's assertion. **Marked gap:**
  retention and purge-resistance of these venues' version histories are
  UNKNOWN — if a venue purges history, the binding degrades to the venue's
  word. They are not third-party anchors and v14 does not
  call them that. True third-party anchoring (transparency log / RFC 3161
  over the packet hash) is deferred to the public edition — publishing even
  a bare hash externally is a public move and needs Marcus Richards's
  explicit approval.

Anyone holding the transcript can re-verify every score's provenance with
the SDK verifier — the same instrument the benchmark preaches. The
benchmark's *judgments* remain its own (§9, §10); the *record* of those
judgments is tamper-evident against silent alteration.

## 9. Scoring procedure

- **Two scorer lanes under one principal**: Ektar and one Grok-crew bot
  (auditor lane), scoring each dimension from the same evidence artifacts
  in separate sittings. Not "independent scorers" — both lanes answer to
  the same principal, and v14 labels it honestly. Correlated bias is the
  known residual (§10); the defenses are the published anchors, the
  published disagreements, and the checkable evidence — not the word
  "independent."
- **Sealed bids**: each lane commits its score-sheet hash per §8; no reveal
  until all frameworks' seals exist.
- **Adjudication**: disagreements of ≤1 point → mean, spread shown.
  Disagreements >1 point → re-examination against the anchors; if
  unresolved, the cell is published as a **range** (e.g., "1–3") and enters
  the ordinal at its **lower bound**, with the range printed beside the
  total. No silent averaging of genuine disagreement. A cell is scored
  only if **both** lanes produce a number: if one lane is UNVERIFIED and
  the other scores a number, the lanes re-examine; if the UNVERIFIED lane
  still cannot score from the evidence, the cell is UNVERIFIED — a single
  unconfirmed judgment does not enter the ordinal.
- **Flag merge and gate binding (mechanical).** D1 flag sets are
  adjudicated before D1 points, and they are not meaned: the
  adjudicated flag set is the **union** of both lanes' sets. A flag
  asserted by exactly one lane is re-examined **inside this step**,
  before any re-scoring — never "together with" the step-3 point
  dispute. Re-examination concludes **determined absent** (the loss is
  affirmatively shown not to have occurred) → the flag is
  **dropped** before any re-scoring; **confirmed** or **undetermined**
  → the flag **stands** — an observed loss is not erased by the
  other lane's non-observation,
  and the gate exists to prevent laundering omissions. Step 3
  adjudicates points only and cannot add or drop flags. The
  set-completeness gate then binds the **merged** flag set, not each
  lane's private view: before point adjudication, each lane's
  D1/D2/D3 values are re-scored against the merged flags from that
  lane's recorded observations. A lane D1 of 2–3 under any non-empty
  merged loss-flag set — `set_loss` or `payload_loss` — becomes 1:
  its structured-record observation, now known lossy, since the
  D1=2/3 anchors require arguments-and-results evidence that a
  standing loss denies. A lane D2/D3 of 2–3 under merged `set_loss`
  becomes 0 via the exercised-but-gated boundary — per the D2=1/D3=1
  boundary clauses, which score 0, never 1. A lane value
  licensed — by suppression or by anchor — by a loss flag the merge removed as
  determined absent is re-scored from its observations with the loss premise removed,
  unless a surviving loss flag still licenses that value: the determined-absent finding
  — the loss affirmatively shown not to have occurred — supersedes the lane's contrary
  observation on that point, so the lane is scored as a complete record, the highest
  non-loss anchor its remaining observations support. (Licensing is per-anchor: D1=1 and
  D1 suppression are licensed by any non-empty flag subset, so any standing flag blocks
  their correction; D2/D3 suppression and exercised-but-gated 0s are licensed by
  `set_loss` only, per §2 — a standing `payload_loss` alone does not block their
  correction.) (Falsifier pinned: lane A D1=1
  `{payload_loss}` vs lane B D1=3 `{}`, flag determined absent → dropped, merged empty;
  lane A re-scores as a complete record — D1=2, or 3 if its observations assert coverage;
  step 3 adjudicates two complete-record scores and cannot re-attach the flag. D2/D3
  exercised-but-gated 0s re-score the same way: lane A D2=0, signature exercised, private
  `{set_loss}`, vs lane B D2=3 `{}`, `set_loss` determined absent → dropped, merged empty;
  lane A re-scores as a complete record — D2=2, the exercised signature now certifying a
  complete set. Auditor pin: lane A D2=0, signature exercised, private `{set_loss}`, vs
  standing `{payload_loss}` after `set_loss` dropped → D2=2 beside `{payload_loss}`, the
  exercised signature now certifying a complete set.) If a surviving flag still licenses
  the value, the correction does not fire for it; the lane is re-scored against the
  surviving merged flags per the rules above — a standing loss keeps its anchors and
  its gate. Values the merge
  does not affect stand — 0–1, replay, bound order, and the
  documented disjuncts are not gated. The merged flag set is published
  with the D1 cell wherever it is non-empty.
- **Order of operations (mechanical).** (1) Each lane scores every cell
  from the evidence, applying the set-completeness gate to its own D1
  flag set. (2) Flag merge and gate binding (above): flag
  re-examination wholly inside this step, then lane D1/D2/D3 values
  re-scored; step 3 cannot add or drop flags. (3) Per-cell point adjudication on the
  post-gate lane values: ≤1 → mean; >1 → re-examination → range at
  lower bound if unresolved; UNVERIFIED-vs-number → re-examination →
  UNVERIFIED if unresolved. (4) §2's UNVERIFIED-propagation fires on
  the *adjudicated* D1 status: UNVERIFIED D1 forces any D2/D3
  post-adjudication value in [2,3] — level or mean — and any range with
  at least one point in [2,3] to UNVERIFIED, superseding the step-3
  computation; values and ranges entirely below 2 stand.
  (5) The ordinal sums the post-gate cells: UNVERIFIED → 0, range → lower
  bound. Two readers following these steps compute the same board.
- **UNVERIFIED cells** (§5, §7) are marked UNVERIFIED, not zero, as a cell
  status — absence of evidence is not evidence of absence. But the ordinal
  needs a number: an UNVERIFIED cell contributes **0** to the ordinal sum,
  with its status printed beside the total. The published components let
  any reader re-weight.
- **Coverage and the ordinal (mechanical).** Cells total = the 4 ranked
  dimensions (D1–D4); D5 is reported, not ranked. **Scored** := cell status
  is not UNVERIFIED. The ordinal is the **sum over all 4 cells**:
  UNVERIFIED cells contribute 0, disagreement-range cells contribute their
  **lower bound** (conservative under disagreement; the full range is
  published for re-weighting). Coverage = scored cells / 4, printed beside
  every total. **Every scored framework appears in the ordinal — there is
  no unranked list and no coverage cliff.** (§6 marked reference rows are
  outside the ordinal set: no ordinal position, no total.) Sort: total
  descending, then coverage descending, then D1 descending, where the D1
  sort key is the cell's **ordinal contribution** (range → lower bound,
  UNVERIFIED → 0). Two readers compute the same board from the published
  sheets.
- **No re-scoring after the ordinal**: the ordinal script runs on revealed
  scores. Re-opening a cell requires a versioned rubric amendment with
  rationale, committed as a new receipt in the chain.

## 10. Limitations (explicit, pre-registered)

1. Scores are the benchmark team's judgment against this rubric — not an
   independent audit. Both scorer lanes sit under one principal, and the
   seal ceremony does not create blindness between them.
2. The ordinal encodes the thesis (§3). It is a disclosed, frozen judgment,
   not a neutral discovery.
3. The evidence chain is verified with the SDK's own verifier
   (circularity, named): if that verifier is wrong, the board's chain
   inherits the error silently. Independent reimplementation of the
   verifier is future work, not claimed here.
4. Residual backdating risk: a transcript fully assembled *before* first
   external publication is undetectable by the chain alone. Notion/Grok
   timestamps are author-operated; they raise the cost of silent
   rewriting (version history — retention and purge-resistance UNKNOWN,
   marked gap) but are not third-party anchors.
5. Live runs depend on model and network behavior; non-determinism is noted
   per run, and T1–T3 are designed to minimize it.
6. The benchmark measures provenance mechanisms, not agent quality, safety,
   or usefulness.
7. Weights and the set-completeness gate are v14 judgment (§3). Per-dimension
   scores, tiers, and D1 flags are published so any reader can re-weight;
   the pre-reg freezes v14, not the reader.
8. Framework commits move; scores are pinned to the frozen SHAs in the
   pre-reg packet. Re-running later is a new edition, not a correction.
9. DOC-tier scores rest on presenter claims. Under the adversarial-
   presenter assumption (§1), a DOC-tier D1=2/D2=1/D3=1/D4=2 describes the
   mechanism *as documented*, not as exercised — documentation is the
   presenter's claims about their own mechanism, and v14 does not pretend
   DOC-tier crypto was verified. The tier is printed with every score
   (§7, §9) and the components are published for re-weighting; a reader
   who discounts unexercised claims can zero the DOC cells.

## 11. Versioning

- v1 was broken by the adversary (review-adversary-rubric-v1.md; the v1
  auditor pass never completed — rail outage); never frozen, no scores
  under it.
- v2 was broken by adversary round 2 (receipt-adversary-rubric-v2.log);
  never frozen, no scores under it.
- v3 was broken by adversary round 3 (receipt-adversary-rubric-v3.log,
  verdict BREAKS); the auditor held with findings
  (receipt-auditor-rubric-v3.log, verdict HOLDS-WITH-FINDINGS). Never
  frozen, no scores under it.
- v4: adversary round 4 part 1 ruled mixed-fault REPAIRED, §3-honesty
  REPAIRED, coverage and seals PARTIALLY (receipt-adversary-rubric-v4-
  p1.log); the auditor confirmed all six §3 rows and returned
  HOLDS-WITH-FINDINGS with five findings (receipt-auditor-rubric-v4-
  p1.log, receipt-auditor-rubric-v4-p2.log). The adversary's part-2 final
  verdict never landed — the xAI rail dropped the call twice (6 attempts,
  RemoteDisconnected; retry.log). v4 was never frozen, no scores under it.
- "No scores" is verified by enumeration: receipt-phase3-listing-2026-10-03.txt
  (SHA-256 0f70de8deaf5d935b504c0d9dc964d872a405d8822ad243f0b5f1fb3258fc3d5)
  lists the phase-3 directory as of 2026-10-03 — no score or leaderboard
  artifacts, only drafts, prompts, review receipts, and retry logs.
- v4 marked the version-history retention/purge-resistance gap that v3
  left unmarked (auditor round 3, finding 1).
- Round 5 (2026-10-03): the auditor returned HOLDS with findings none
  (receipt-auditor-rubric-v5.log), verifying all five v5 repairs; the
  adversary returned BREAKS (receipt-adversary-rubric-v5.log) — repairs
  1–5 VERIFIED, two determinism holes: infeasible-live cells with no
  legal value (§5/§7 vs §2 anchors), and §2 UNVERIFIED-propagation vs §9
  ordinal computation. v5 was never frozen, no scores under it.
- v6 pins both round-5 hits: deterministic DOC scoring (§5.1, widened
  D2=1 anchor, tier de-embedded from the D1=2 anchor, §3 DOC-profile row)
  and gate precedence (§2, §9 order of operations). v6 was never frozen,
  no scores under it.
- Round 6 (2026-10-03): the auditor returned BREAKS
  (receipt-auditor-rubric-v6.log) — one breaking inconsistency (DOC-only
  documented hash chain had no unique D3 value: D3=1's anchor unwidened,
  §5.1's cap "at most 1") plus two unmarked UNKNOWNs (adjudicated means
  in [2,3] under the gate; docs-silence vs §5.1's forced number). v7
  repairs all three: D3=1 widened with the forced exactly-1 cap, gate
  precedence extended to means, docs-silence pinned to UNVERIFIED. (The
  adversary's round-6 fresh-eyes pass never landed — xAI rail dropped the
  call 3×, RemoteDisconnected; receipt-adversary-rubric-v6.log holds only
  the rail-failure output — so there were no adversary hits to fold in;
  round 7 runs both lanes on v7.)
- Round 7 (2026-10-03/04): the auditor returned BREAKS
  (receipt-auditor-rubric-v7.log) — one breaking inconsistency (D3=1's
  header contradicted §3's ceiling on observed bound order; exercised
  chain on a set-lossy record had no legal value) plus three findings:
  §5.1 "capped at 1" vs forced exactly-1, straddling-range membership
  under the gate, and the v2 retraction clause sitting in the §3 body.
  v8 repairs all four.
- Round 7 adversary (2026-10-03/04): returned BREAKS
  (receipt-adversary-rubric-v7.log) — v7 repairs (a) and (c) VERIFIED,
  repair (b) partial on ranges (closed by the straddling-range pin),
  plus three hits: the range×"below 2" collision (same as the
  auditor's finding 2 — repaired), flag-set merge and gate binding
  time (new — no rule merged lane D1 flag sets or fixed when "requires
  no set-loss" binds), and D5-at-DOC (new — reported D5 had no legal
  value for documented-but-unexercised redaction). v8 repairs the two
  new hits in the preceding sentence (v8's changelog repairs 5–6 of
  v8). No rail failures in
  round 7 — both lanes landed.
- v2 claimed the head-to-head "ran clean" while the gate forced it. That
  claim is retracted (moved here from the §3 body in v8).
- Round 8 (2026-10-03/04): the auditor returned BREAKS
  (receipt-auditor-rubric-v8.log) — one breaking inconsistency (the
  flag-merge paragraph scheduled single-lane flag re-examination both
  with the step-3 point dispute and as the step-2 re-score
  precondition, licensing two boards) plus two medium findings (§11's
  stale "still running" parenthetical and false "below"; D1/flag
  binding unspecified for non-1 adjudicated D1 under a standing flag).
  v9 repairs all three: re-examination wholly inside step 2, lane D1
  re-scored against merged flags, §11 contradiction removed. (The
  adversary's round-8 fresh-eyes pass never landed — xAI rail dropped
  the call 3×, RemoteDisconnected; receipt-adversary-rubric-v8.log
  holds only the rail-failure output — so there were no adversary hits
  to fold in; round 9 runs both lanes on v9.)
- Round 9 (2026-10-03/04): the auditor returned HOLDS-WITH-FINDINGS
  (receipt-auditor-rubric-v9.log) — all nine v9 repair claims
  VERIFIED, no breaking inconsistency, 4 findings (3 MEDIUM: D1
  re-score under standing `payload_loss`; determined-absent drop
  rule; §11 "repairs 5–6" pointer — 1 LOW: the "(D2=1, D3=1)"
  locator). v10 repairs all four. The adversary's round-9 pass had
  not landed when v10 was drafted (xAI rail down through the
  round-9 window); the retry cron is re-armed for both lanes on v10.
- Round 10 (2026-10-03/04): the adversary returned HOLDS
  (receipt-adversary-rubric-v10.log) — all four v10 repairs VERIFIED,
  no second mechanical value, no two-board scheduling — with one
  residual: the merge-removed re-score sentence covered only
  `set_loss`, so a determined-absent `payload_loss` could leave the
  flagging lane's D1=1 standing and publish range 1–3 beside an empty
  flag set (ordinal lower bound 1, unlicensed by the D1=1 anchor).
  v11 extends the sentence to both loss flags. The auditor's round-10
  pass had not landed when v11 was drafted (xAI rail still flapping);
  both lanes retargeted to v11.
- Round 11 (2026-10-04): both lanes landed in the same retry window.
  The adversary returned BREAKS (receipt-adversary-rubric-v11.log) —
  one hit: the v11 restoration sentence covered only *suppressed*
  values, so a step-1 D1=1 scored directly as the lossy-record anchor
  survived a determined-absent drop, and step 3 could publish range
  1–3 beside an empty flag set (ordinal lower bound 1, unlicensed by
  the D1=1 anchor); even a forced re-score had no unique legal value
  under v11. The auditor returned HOLDS
  (receipt-auditor-rubric-v11.log), findings none — all v11 repair
  claims verified — reading "suppressed" broadly (INFERRED) and asking
  the falsifier's post-step-2 numbers be pinned in §9. The author
  converges with the adversary on the text ("suppressed" denotes the
  two defined suppressions; a direct D1=1 is an anchor value) and
  folds the auditor's promote into the repair. v12 adds the
  correction principle — a determined-absent finding supersedes the
  lane's contrary observation, so the lane is scored as a complete
  record — and pins the falsifier. The retry cron self-reported both
  verdicts but its own disable call failed in the detached-run
  context; the author disabled it directly.
- Round 12 (2026-10-04): both lanes landed. The adversary returned
  BREAKS (receipt-adversary-rubric-v12.log) — two hits, both verified:
  (1) the v12 correction sentence was D1-only, so a D2/D3
  exercised-but-gated 0 (a direct anchor value licensed by set-loss,
  not a suppressed 2–3) had no re-score rule after a
  determined-absent drop — "stand 0–1" vs "re-score → 2" both
  readable, range 0–3 publishable with ordinal 0 unlicensed; (2) the
  correction was unscoped to emptied flag sets — with a surviving
  loss flag, the sentence ordered a complete-record 2/3 while the
  clamp ordered 1, three productions with no order rule. The auditor
  returned HOLDS-WITH-FINDINGS (receipt-auditor-rubric-v12.log) —
  all v12 repair claims verified — with one MEDIUM finding
  independently converging on hit 2 (partial-drop two boards; fix:
  scope to "merged loss-flag set is empty after the drop"). v13
  replaces the two specific sentences with one general principle —
  any value licensed by suppression or by anchor by a removed flag
  is re-scored with the loss premise removed, provided no loss flag
  stands; surviving flags keep their anchors and gate — and pins the
  D2 falsifier.
- Round 13 (2026-10-04): the auditor returned HOLDS-WITH-FINDINGS
  (receipt-auditor-rubric-v13.log) — all v13 repair claims verified
  (general principle covers suppression, direct D1=1, and direct
  D2/D3 0s; surviving-flag scope closes the partial-drop two-board;
  both falsifiers match the five steps) — with one MEDIUM finding,
  verified genuine: the v13 scoping ("provided the drop leaves no
  loss flag standing") is too blunt for cross-flag partial drops. A
  D2/D3 value licensed by `set_loss`, with `set_loss` dropped and
  `payload_loss` standing, had its correction blocked even though
  `payload_loss` does not license D2/D3 values at all (§2) — the 0
  left unlicensed with no sentence assigning a number. v14 refines
  the proviso to per-anchor licensing: "unless a surviving loss flag
  still licenses that value" — D1 values need any surviving flag to
  block; D2/D3 values need a surviving `set_loss`. The auditor's
  falsifier now resolves to D2=2 beside `{payload_loss}` and is
  pinned. (The adversary's round-13 pass was still running when v14
  was drafted.)
- The frozen v14 is the pre-reg packet's RUBRIC.md; its SHA-256 is the
  version identifier.
- Amendments after freezing → v15 with a changelog receipt in the chain. v14
  scores stand under v14 forever; they are not "updated" to v15.

## 12. Pre-registration mechanics

The pre-reg packet contains: RUBRIC.md (frozen v14), FRAMEWORKS.md
(enumeration method + full candidate list + reject log + frozen top-10 +
star counts + pinned SHAs + freeze timestamp), TASKS.md (exact T1–T3
inputs), PROCEDURE.md (harness + scoring procedure, §§8–9), the
enumeration script + raw output, and SHA-256 hashes of each file. The
packet is **published to Notion + Grok before any seal, observation, or
scoring receipt is emitted** — publication timestamps are the ordering
anchors in §8. Publication was approved in advance by Marcus Richards
(2026-10-02, chat — his "use notion" and "and grok"); the packet manifest
records the citation at freeze. Until the packet is frozen and published,
**no scoring begins**. A public transparency-log anchor over the packet
hash is NOT assumed; it needs his explicit separate approval.
