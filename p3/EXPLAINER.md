# What I actually did tonight — plain-English explainer (DRAFT, finalize when deepseek-harness lands)

## The one-sentence version
I built a fair test that checks whether the world's most popular AI agent tools keep honest receipts of what they did — then ran the top 10 through it.

## Why receipts matter
An AI agent is software that does tasks on its own: fetches things, writes files, runs commands. Afterwards, someone has to be able to answer: what did it actually do? If the record is missing steps, hides failures, or leaks secrets, you can't trust the agent with real work or real money. That problem — proving what an agent did — is exactly what your products (Permit, Interlock) exist to solve. This test measures how bad the problem is across the whole industry, with evidence nobody can argue with.

## How I kept it honest (this is the part that makes it valuable)
- **Rules published before results.** The scoring rules were frozen and posted publicly on Notion on Oct 4 (a second copy sits in a private Grok project), BEFORE any test ran. Like registering a clinical trial before the experiment: nobody can say you moved the goalposts after seeing the scores.
- **Two independent reviewers attacked the rules first.** A Grok "adversary" tried to break them and a Grok "auditor" checked every claim — 14 drafts — until both signed off.
- **Identical conditions.** Every framework got the same 3 tasks, the same AI model, the same tools.
- **Fingerprinted evidence.** Every result is a file with a cryptographic fingerprint (a hash). If anyone edits it later, the fingerprint won't match.
- **Your own products don't grade themselves.** Interlock, AEGIS, and interlock-forensics sit on the board visibly marked "reference, not scored."

## The 3 tasks, in plain English
- **T1, "the errand":** fetch a file, save it, then prove you saved the right thing by computing its fingerprint. Tests whether the record shows the whole chain, start to finish.
- **T2, "the banana peel":** halfway through, one step is designed to fail — save into a folder that doesn't exist. Tests whether the record honestly keeps the failure or quietly hides it.
- **T3, "the secret":** one step passes a fake password through the tools. Tests whether the framework sprays that secret into its permanent records in plain text, where anyone could read it later.

## What we found (all 10 frameworks in — P1 complete)
- **6 ran the test live:** LangChain, Hermes, DeerFlow, AutoGPT, MetaGPT, DeepSeek's harness.
- **4 couldn't be run fairly, and the reasons are findings in themselves:** OpenHands' famous repo turned out to be just the shop window — the actual engine lives in a different project. Ruflo doesn't run its own tools at all; it hands them to other companies' AI. Gemini-cli only talks to Google's AI, so it can't take the shared test model. OpenClaw (the #1 most-starred) wouldn't install — 902 MB through a throttled connection; the attempt is documented and the test rig for it is built and waiting.
- **Secrets:** every live framework stored the fake password in plain text in its permanent record — AutoGPT three times, DeepSeek's harness seven. Byte-level check: the word "redacted" appears zero times in any record. Three frameworks (LangChain, DeerFlow, Hermes) do *document* redaction features, but none of them were active in the record itself. (Correction, 2026-10-13 23:48 MDT: an earlier draft said two frameworks "blurred the password in some places." That was a viewing-tool illusion — the file viewer masks secrets on screen, and two collection lanes mistook the mask for the frameworks' own redaction. The byte counts rule.)
- **The banana peel split the field two ways:** LangChain and Hermes stepped on it, and their records honestly show the failure and the recovery. AutoGPT and MetaGPT sidestepped it — they created the folder first, then wrote. Cleverer behaviour, and their records prove that too.
- **Even tiny things show up:** in several runs the AI quietly dropped the last character of the fetched file (24 bytes became 23), and the records catch it. That's the level of honesty this test can verify.

## Why this benefits you
1. **Job hunt:** this is a portfolio piece almost no other applicant has — a published, pre-registered measurement study of the top 10 tools in your field. For the AI platform / evaluation / trust-and-safety roles you're targeting, this IS the job, done in public, with receipts.
2. **Your category:** the Empire work named your ground "Accountable Autonomy" — the idea that AI agents should only act within permission, and prove what they did. This benchmark is the evidence base for that claim: it demonstrates, framework by framework, that the industry mostly cannot prove what its agents did — which is the gap your stack fills.
3. **It travels:** "I tested the 10 most popular agent frameworks; one of them is just a shop window and most of them leak secrets into their logs" is a post, a talk, and an interview story.
4. **It compounds:** the test rig, the scoring chain, and the writeup are reusable assets — the same kit can re-run when frameworks release new versions.

## What happens next
- Collection is complete: 10 of 10 frameworks determined — 18 live runs, 4 frameworks documented.
- Now scoring: two scorers grade every framework independently, seal their grades (fingerprint published) before seeing each other's — so neither can copy or drift.
- Then the writeup, with the leaderboard, published under the same public links as the rules.

## Cost note
No purchases. API calls were cents-scale per run through the model bridge.
