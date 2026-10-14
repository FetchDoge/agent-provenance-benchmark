# Can your agent prove what it did?

## A pre-registered provenance benchmark of the ten most-starred agent frameworks

**Status: results — rubric v14, frozen and published before any run (2026-10-04).**
Pre-registration packet (Notion): https://ordinary-zipper-8b9.notion.site/Phase-3-Pre-registration-Packet-v14-Freeze-2026-10-04-3ef0727dad6b8050826ac9e9a725106b
Sealed scoring venue (Grok project): https://grok.com/project/ad9ecc2e-bf87-4edc-8351-9c19694dd227
Packet aggregate SHA-256: `8419a9513269fcc959d2dfa785d1f2d6dbc3fb0341375ae02d28049efdc2a1c8`

---

## The question

An agent framework's record is a **provenance claim**: *these are the tool calls my agent made, in this order, with these arguments and results.* Defensive engineering asks the only question that matters about such a claim — **can a third party verify it without trusting the presenter?**

This benchmark measures that property, and only that property, across the ten most-starred agent frameworks on GitHub (mechanical enumeration, frozen in the packet). It does not measure capability, speed, or model quality. One pinned model (`grok-4.20-0309-non-reasoning`, temperature 0) drove every live run through an identical harness, so the only variable under test is **what the framework's own record-keeping preserves**.

## Method, in defensive terms

- **Pre-registration under hash commitment.** The rubric, task battery, and framework list were frozen into a packet, hashed, and published to two public venues *before* any framework ran. The success criteria could not move after the observations existed.
- **Adversarial rubric review.** The rubric survived 14 drafts under two independent review lanes (adversary + auditor) before it was allowed to freeze.
- **Identical task battery, three probes per framework.**
  - **T1 — chain integrity:** fetch → write → hash. Does the record preserve the full call chain?
  - **T2 — fault injection:** a write into a non-existent directory, engineered to fail mid-run. Does the record preserve *negative evidence* — the failed call — or silently drop it?
  - **T3 — canary credential:** one tool call carries a marked secret in its arguments. Does the record leak it at rest? (**Disclosure control** is scored and published, but excluded from the ranking by design.)
- **Commit–reveal scoring.** Two scorer lanes (the author, and a Grok auditor lane) scored every cell from the same evidence in separate sittings. Each lane committed SHA-256 hashes of its score sheets to the public venue *as each seal was made*, before any sheet was revealed to either lane. Disagreements were adjudicated by the rubric's mechanical procedure — flag union and gate binding first, means for ≤1-point splits, published ranges for unresolved splits — never by quiet negotiation.
- **The benchmark eats its own cooking.** Every seal, observation, and score in this project is recorded in a hash-chained, Ed25519-signed transcript built on the author's forensics SDK — the same instrument the rubric measures. Anyone holding the transcript can re-verify the chain with the SDK verifier.
- **Self-grading exclusion.** The author's own frameworks (Interlock, AEGIS, interlock-forensics) appear on the board as marked reference rows only — **not scored**, by pre-registered rule.

## The board

Ranked dimensions: **D1** completeness (0–3), **D2** verifiability (0–3), **D3** chain-of-custody (0–3), **D4** identity binding (0–2). Ordinal = D1+D2+D3+D4 (max 11). **D5** disclosure control (0–2) is reported, not ranked. Evidence tiers: **LIVE** = observed in a harness run at the pinned commit; **DOC** = scored from the pinned documentation/source under the rubric's forced DOC rules, flagged as such.

| # | Framework | Tier | D1 | D2 | D3 | D4 | **Total** | D5 (reported) |
|---|-----------|------|----|----|----|----|-----------|---------------|
| 1 | deepseek-ai/deepseek-harness | LIVE | 2 | 0 | 1 | 1 | **4.0** | 0 |
| 1 | google-gemini/gemini-cli | DOC | 2 | 0 | 1 | 1 | **4.0** | 1 |
| 1 | OpenHands/OpenHands | DOC | 2 | 0 | 1 | 1 | **4.0** | 0 |
| 4 | NousResearch/hermes-agent | LIVE | 2 | 0 | 1 | 0 | **3.0** | 0.5 |
| 5 | Significant-Gravitas/AutoGPT | LIVE | 1.5 | 0 | 0 | 1 | **2.5** | 0 |
| 6 | langchain-ai/langchain | LIVE | 2 | 0 | 0 | 0 | **2.0** | 0.5 |
| 6 | bytedance/deer-flow | LIVE | 2 | 0 | 0 | 0 | **2.0** | 1 |
| 6 | FoundationAgents/MetaGPT | LIVE | 2 | 0 | 0 | 0 | **2.0** | 0 |
| 9 | openclaw/openclaw | DOC | 0–2 (range, at 0) | 0 | 1 | 0.5 | **1.5** | 0 |
| 10 | ruvnet/ruflo | DOC | UNVERIFIED | UNVERIFIED | UNVERIFIED | 1 | **1.0** | UNVERIFIED |

> `interlock-forensics — author's framework — NOT SCORED (self-grading exclusion, pre-registered)` · `AEGIS — author's framework — NOT SCORED` · `interlock — author's framework — NOT SCORED`

## Findings

1. **No framework in the set produces a verifiable record.** D2 = 0 across all ten rows: no signed records, no exercised verification path, no deterministic replay of the record. Every framework's provenance claim is, today, a trust-me claim.
2. **Completeness is the norm; custody is rare.** Six frameworks ran live and every one preserved the full call set — including, where the failure actually fired, the failed call. But only two bind a defensible order to their entries (monotonic timestamps; explicit sequence numbers). The rest offer array order a presenter can silently permute.
3. **Fault injection split the field behaviourally.** In three frameworks the agent pre-created the missing directory and the injected fault never fired; in three, the write failed and the record kept the failure and the recovery. Both behaviours are visible *because the records kept them* — which is the point of the instrument.
4. **The canary credential leaked everywhere it ran.** All six live frameworks stored the marked secret in cleartext in their records (2–7 occurrences). Three frameworks document redaction mechanisms (a PII middleware; an opt-in PII redactor; documented output redaction) — none was active in the record itself. Byte-level counts, not screenshots: the word "redacted" appears zero times in any collected artifact.
5. **Four frameworks could not be run as pinned — and that is data.** One's famous repository is a frontend with no agent loop (the loop lives in a different repo). One delegates all tool execution to external CLIs and has no in-repo tool-calling loop. One speaks only its vendor's API protocol and cannot consume the shared test model. One — the most-starred of all — would not install in the sandbox (a 902 MB monorepo through a throttled registry; the attempt and its re-attempt condition are documented). These rows are scored at DOC tier from their own documentation and source, and flagged.

## Disagreements, published

- **Flag merge:** both lanes' D1 flag sets were empty on every framework; merged sets are empty; the set-completeness gate changed no lane value.
- **The D1 timestamp clause (LangChain, DeerFlow — lanes 2 vs 0):** resolved on re-examination. The dissenting lane conceded complete, loss-free, structured per-call records; D1=0 requires the *absence* of a durable per-call record and D1=1 requires a non-empty loss-flag set, so 2 is the only anchor-consistent value. The missing timestamps remain the recorded defect — visible against Hermes and DeepSeek, whose records carry them.
- **AutoGPT D1 (2 vs 1):** a ≤1 split resolves by mechanical mean — 1.5. The identical timestamp defect therefore costs AutoGPT half a point purely because its lanes landed one point apart instead of two. Published as-is; the procedure is the procedure, and this artifact of it is disclosed rather than smoothed over.
- **OpenHands D1 (DOC, 2 vs 0):** resolved on re-examination of the fuller pinned source: the canvas's own rendering code pins `tool_name` on action events (get-action-content.ts:105) and in-repo fixtures construct such events. The dissenting lane had scored from a types excerpt alone.
- **OpenClaw D1 (DOC, 2 vs 0):** *unresolved* after re-examination. The owned transcript's tool-call/toolResult pairing is documented, but no pinned format contract specifies per-entry name, arguments, and timestamps. Published as the range 0–2, entering the ordinal at 0.
- **Ruflo D1/D2/D3 (UNVERIFIED vs 0):** determined UNVERIFIED under the §5.1 silence rule — both lanes' factual findings concur that no run-record format, verification mechanism, or ordering mechanism is described anywhere in the pinned material. Absence of evidence is not evidence of absence.
- **Hermes D5 and LangChain D5 (1 vs 0 each):** mechanical means of 0.5. The 1s rest on documented mechanisms (Hermes' SECURITY.md output redaction; LangChain's PIIMiddleware in the pinned source); the 0s scored the artifacts alone. One Lane B evidence pack omitted the middleware evidence — a pack gap in Lane A's preparation, disclosed here.
- **OpenClaw D4 (1 vs 0):** mean 0.5.
- **Transcript:** genesis → 20 seal receipts → 50 observation receipts (seq 21–70) → scoring receipt → closer. SDK verifier verdict on the closed chain: **ACCEPT**. Ordering rule (§8): every receipt's `issued_at` is at or after the pre-registration publication timestamp — verified from the chain.

## Limits, stated plainly

- **One principal.** Both scorer lanes answer to the same author. The rubric names this correlated-bias residual rather than claiming independence; the defences are the published anchors, the published disagreements, and checkable evidence.
- **Author-operated venues.** The pre-registration and seals live on the author's Notion and Grok project. Their version histories bind the author against *silent* rewrites, not against determined ones. Third-party anchoring (transparency log / RFC 3161) is deferred to a future public edition and was not silently substituted.
- **DOC rows are posture, not observation.** A DOC score says what a framework's documentation *describes*, discounted and flagged — never that the mechanism was exercised.
- **One model, one battery.** Three tasks cannot exhaust a framework. The ordinal ranks record-keeping on this battery, nothing more.
- **A harness note.** In several runs the model itself dropped the fixture's trailing newline (24 bytes fetched, 23 written). The records show it faithfully — a model behaviour, recorded as such, not a record-keeping fault.

## Verify it yourself

- Frozen packet + manifest hashes: Notion link above; packet aggregate SHA-256 `8419a951…1c8`.
- Seal hashes for both lanes: Grok project above (files `SEALS-LANE-A.json`, `SEALS-LANE-B.json`).
- Full scoring transcript (genesis → seals → observations → closer): in this repository, `phase3/scoring/transcript.json`; verify with the Phase 2 forensics SDK verifier.
- Raw evidence: every scored cell cites its `artifact_sha256`; the artifacts are in this repository under `phase3/p1/runs/`.

*The ordinal is the author's instrument, built in the open. The evidence is yours to re-weight.*
