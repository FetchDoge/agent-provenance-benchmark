# Phase 3 Pre-registration Packet — v14 Freeze

**Rubric version:** v14 (review gate satisfied: auditor HOLDS, adversary HOLDS)  
**Packet freeze:** 2026-10-04T07:15:38Z  
**Packet aggregate SHA-256:** `8419a9513269fcc959d2dfa785d1f2d6dbc3fb0341375ae02d28049efdc2a1c8`  
*(SHA-256 of MANIFEST.sha256, which binds all packet file hashes)*

## Contents

| File | SHA-256 | Bytes |
|------|---------|-------|
| RUBRIC.md | 98608ea0bf7f73bb88dc5f407af6602c9793d955f3e84484c70f9bd8099bb01a | 47,443 |
| FRAMEWORKS.md | 7e4e550fe155aa6bc0883fe7598d13564da7a9d61d7fdbdac3454542c7c207e4 | 101,618 |
| TASKS.md | bf181efd81e5ffbcc0de11a6caf0627bcde781ee2c1615fd54067a2d6d774bf2 | 4,765 |
| PROCEDURE.md | 5a142825c6a1642261e1221e93631005f94887d5da3f0f2dd4e377658c950f76 | 7,604 |
| enumerate_frameworks.py | dbd8b5e3b6facd2e7e02ee0cd461246094191a41495059f7133fb8b01baccb96 | 4,619 |
| enumeration-raw.json | 251f86193bf7c4a90070e04a0039072fffa1dbe43757f2e78d588cf270d001cc | 717,436 |
| enumeration-run.log | 7c7e9dec9d375f57f3793177a354544a785f55fa4cc663f1539023cc9dcd5ddc | 55 |

## Authority

- **Pre-registration publication to Notion + Grok:** Pre-approved by Marcus Richards
  ("your call" → "use notion" → "and grok").
- **Review gate:** Both Grok lanes (auditor + adversary) returned HOLDS on rubric v14.
  See `receipt-auditor-rubric-v14.log` and `receipt-adversary-rubric-v14.log`.
- **Invariants:** No scores exist. No scores, seals, observations, leaderboard,
  scoring receipts, or scoring-transcript genesis may predate verified
  publication of this packet (rubric §8 ordering rule).

## What this packet establishes

1. The exact rubric (v14) that will govern scoring — byte-identical to the reviewed version.
2. The exact framework universe (1,023 candidates, 169 includes, top 10 frozen with pinned SHAs).
3. The exact task battery (T1–T3) and harness procedure.
4. The enumeration method and raw data for independent verification.

## What happens next

1. Publish this exact packet to public Notion + Grok (venue receipts in sidecar).
2. Verify both publication receipts (public URLs, server timestamps, packet hash match).
3. Only then: scoring-transcript genesis → P1 (run ~10 frameworks through T1–T3).
