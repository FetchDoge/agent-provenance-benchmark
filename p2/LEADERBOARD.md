# Provenance Benchmark — Leaderboard (rubric v14)

Pre-registration packet aggregate SHA-256: `8419a9513269fcc959d2dfa785d1f2d6dbc3fb0341375ae02d28049efdc2a1c8`
Ranked: D1 completeness (0–3) + D2 verifiability (0–3) + D3 chain-of-custody (0–3) + D4 identity binding (0–2) = ordinal of 11. D5 disclosure control (0–2) is reported, not ranked. Tiers: LIVE = observed in harness runs at the pinned commit; DOC = scored from pinned documentation/source under §5.1 forced rules.

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

Reference rows (pre-registered, §6):

> `interlock-forensics — author's framework — NOT SCORED (self-grading exclusion, pre-registered)`
> `AEGIS — author's framework — NOT SCORED (self-grading exclusion, pre-registered)`
> `interlock — author's framework — NOT SCORED (self-grading exclusion, pre-registered)`

## Adjudication notes (summary; full worksheet in `adjudication-worksheet.json`, determinations in `determinations.json`)

- **Flag merge:** both lanes' D1 flag sets were empty on every framework; merged sets are empty; no gate binding changed any lane value.
- **D1 timestamp clause (langchain, deer-flow — Lane B 0 vs Lane A 2):** resolved on re-examination. Lane B conceded complete, loss-free structured per-call records; D1=0 requires the absence of a durable per-call record and D1=1 requires a non-empty loss-flag set, so 2 is the only anchor-consistent value. The absent timestamps are the recorded defect (contrast Hermes/DeepSeek, whose records carry them).
- **AutoGPT D1 (2 vs 1, ≤1):** mechanical mean 1.5 per §9 — the same timestamp defect costs AutoGPT half a point purely because the lanes landed one point apart instead of two. Published as-is; the procedure is the procedure.
- **OpenHands D1 (DOC, 2 vs 0):** resolved on re-examination of the fuller pinned source (`get-action-content.ts:105` pins `tool_name` on action events; in-repo fixtures construct such events) — Lane B had scored from the types excerpt alone.
- **OpenClaw D1 (DOC, 2 vs 0):** unresolved after re-examination — the transcript's tool-call/toolResult pairing is documented, but no pinned format contract specifies per-entry name/arguments/timestamps. Published as the range 0–2, entering the ordinal at 0 per §9.
- **Ruflo D1/D2/D3 (UNVERIFIED vs 0):** determined UNVERIFIED under the §5.1 silence rule. Both lanes' factual findings concur that no run-record format, verification mechanism, or ordering mechanism is described (the AttestationLog covers memory operations; ed25519 covers federation agents). Absence of evidence is not evidence of absence (§5).
- **Hermes D5 (1 vs 0) and LangChain D5 (1 vs 0):** mechanical means of 0.5. Lane A's 1s rest on documented mechanisms (Hermes SECURITY.md output redaction; LangChain's PIIMiddleware in pinned source); Lane B scored the artifacts alone — its LangChain pack did not include the middleware evidence, a Lane A pack gap disclosed here.
- **OpenClaw D4 (1 vs 0):** mean 0.5.
- **UNVERIFIED propagation (§2):** ruflo's adjudicated D1 is UNVERIFIED; its D2/D3 were already UNVERIFIED, so no value changed.
