'use strict';
/* Scoring-transcript initializer (re-issue).
 * The first genesis (2026-10-14T03:00Z) was emitted with an ephemeral key
 * whose private half was never persisted, so its chain could not be
 * continued. This script re-issues the genesis with a persisted transcript
 * key. Genesis args are byte-identical ({prereg_sha256, rubric_version});
 * issued_at still satisfies the rubric section 8 ordering rule (>= the
 * 2026-10-04T08:03:10Z pre-reg publication). The superseded genesis is kept
 * at genesis-superseded.json and the re-issue is recorded in
 * PUBLICATION-RECEIPTS.json. */
const crypto = require('crypto');
const fs = require('fs');
const path = require('path');
const { Emitter } = require('/home/hatch/workspace/portfolio-hackathon/phase2/sdk/ts/emitter.js');

const DIR = __dirname;
const { privateKey, publicKey } = crypto.generateKeyPairSync('ed25519');
const runId = Emitter.newRunId();
const em = new Emitter(privateKey, 'benchmark-phase3-v14', runId, 'ifts/0.1.0');

const keyFile = {
  key_id: em.keyId,
  run_id: runId,
  agent: 'benchmark-phase3-v14',
  private_key_pkcs8_b64: privateKey.export({ format: 'der', type: 'pkcs8' }).toString('base64'),
  note: 'Benchmark transcript signing key (not a user credential). Persisted so the scoring chain can be continued and closed.',
};
fs.writeFileSync(path.join(DIR, 'transcript-key.json'), JSON.stringify(keyFile, null, 2), { mode: 0o600 });

const now = new Date().toISOString();
const genesis = em.emitToolCall({
  tool: 'benchmark-genesis',
  args: JSON.stringify({
    prereg_sha256: '8419a9513269fcc959d2dfa785d1f2d6dbc3fb0341375ae02d28049efdc2a1c8',
    rubric_version: 'v14',
  }),
  result: JSON.stringify({ status: 'genesis', packet: 'frozen-v14', reissue: true }),
  startedAt: now, endedAt: now, issuedAt: now, disclosure: 'full',
});
fs.writeFileSync(path.join(DIR, 'transcript.json'), JSON.stringify([genesis], null, 2));
console.log(JSON.stringify({ genesis_id: genesis.attestation_id, key_id: genesis.key_id, issued_at: now, run_id: runId }, null, 2));
