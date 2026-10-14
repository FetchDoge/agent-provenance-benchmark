'use strict';
/* Emit the board scoring receipt, then close the transcript.
 * Usage: node close_transcript.js <scoring-spec.json>
 * scoring-spec.json: {args: {...}, result: {...}} for tool "benchmark-score".
 * Rebuilds emitter state exactly like append_receipt.js, emits the scoring
 * receipt, then emitCloser() and a full SDK verification. */
const crypto = require('crypto');
const fs = require('fs');
const path = require('path');
const SDK = '/home/hatch/workspace/portfolio-hackathon/phase2/sdk/ts';
const { Emitter } = require(SDK + '/emitter.js');
const { canonicalBytes } = require(SDK + '/canonical.js');
const { verifyTranscript } = require(SDK + '/verify.js');

const DIR = __dirname;
const keyFile = JSON.parse(fs.readFileSync(path.join(DIR, 'transcript-key.json'), 'utf8'));
const transcript = JSON.parse(fs.readFileSync(path.join(DIR, 'transcript.json'), 'utf8'));
const priv = crypto.createPrivateKey({ key: Buffer.from(keyFile.private_key_pkcs8_b64, 'base64'), format: 'der', type: 'pkcs8' });
const em = new Emitter(priv, keyFile.agent, keyFile.run_id, 'ifts/0.1.0');
if (em.keyId !== keyFile.key_id) throw new Error('key mismatch');
const tip = { ...transcript[transcript.length - 1] };
delete tip.signature;
em.prevHash = crypto.createHash('sha256').update(canonicalBytes(tip)).digest('hex');
em.seq = transcript.length;

const spec = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const now = new Date().toISOString();
const scoring = em.emitToolCall({
  tool: 'benchmark-score',
  args: JSON.stringify(spec.args),
  result: JSON.stringify(spec.result),
  startedAt: now, endedAt: now, issuedAt: now, disclosure: 'full',
});
transcript.push(scoring);
const closer = em.emitCloser(new Date().toISOString());
transcript.push(closer);
fs.writeFileSync(path.join(DIR, 'transcript.json'), JSON.stringify(transcript, null, 2));
const verdict = verifyTranscript(transcript);
console.log(JSON.stringify({ scoring_receipt: scoring.attestation_id, closer: closer.attestation_id, chain_len: transcript.length, verify: verdict }, null, 2));
