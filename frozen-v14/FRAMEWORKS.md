# FRAMEWORKS.md — Phase 3 Universe Predicate

**Rubric:** v14 (frozen, see RUBRIC.md)  
**Enumeration timestamp:** 2026-10-04T06:51:37Z  
**Packet freeze:** 2026-10-04T07:15:38Z  
**Candidates:** 1,023  
**Predicate:** include iff the primary abstraction is an agent loop that issues tool calls. Reject: pure human-wired workflow UIs, pure chat wrappers without a tool abstraction, single-vertical agents, closed-source repos, non-OSI-licensed repos.

## Enumeration method

GitHub search `topic:ai-agents stars:>=1000`, sorted by stars descending (643 candidates), UNION repositories linked by two awesome lists:

- `e2b-dev/awesome-ai-agents` @ `9596ab1e69fbbb6c95291141c8dab5c181083216` (main, 30,263 stars at enumeration)
- `slavakurilyak/awesome-ai-agents` @ `5ed220d6e2f7ad1bb49a6a1fcb8b2b6635c40966` (main, 2,301 stars at enumeration)

Deduplicated by repository ID; sorted by stargazers_count descending.

## Top 10 (frozen)

SHAs pinned at observation time 2026-10-04T07:13:43Z (immediately pre-freeze).

| # | Repository | Stars | License | Default branch | HEAD SHA | HEAD date |
|---|------------|-------|---------|---------------|----------|-----------|
| 1 | openclaw/openclaw | 391257 | MIT | main | `9e0734be272f` | 2026-10-04T07:10:39Z |
| 2 | NousResearch/hermes-agent | 251025 | MIT | main | `937f23db2d70` | 2026-10-04T07:09:15Z |
| 3 | deepseek-ai/deepseek-harness | 243037 | MIT | master | `5badb15009ae` | 2026-10-03T03:48:13Z |
| 4 | Significant-Gravitas/AutoGPT | 187644 | MIT (agent) + Polyform Shield (autogpt_platform/) — see note | master | `f8b0e0a87c38` | 2026-10-02T14:16:47Z |
| 5 | langchain-ai/langchain | 147421 | MIT | master | `57236d55d9ff` | 2026-10-02T19:35:20Z |
| 6 | google-gemini/gemini-cli | 107227 | Apache-2.0 | main | `fb972b2f87fe` | 2026-10-02T05:49:39Z |
| 7 | OpenHands/OpenHands | 89932 | MIT | main | `a6bba78ffd5a` | 2026-10-03T14:30:29Z |
| 8 | bytedance/deer-flow | 83364 | MIT | main | `830de11c664d` | 2026-10-04T06:54:08Z |
| 9 | ruvnet/ruflo | 73815 | MIT | main | `caf5078be662` | 2026-10-04T05:56:40Z |
| 10 | geekan/MetaGPT (now FoundationAgents/MetaGPT) | 70732 | MIT | main | `11cdf466d042` | 2026-01-21T10:12:32Z |

**License note — AutoGPT:** Dual-licensed. Everything outside `autogpt_platform/` is MIT; the `autogpt_platform/` folder is Polyform Shield (non-OSI). The autonomous agent loop (the scored artifact) is MIT. Included because the scored component is OSI-licensed; the non-OSI platform folder is out of scope for T1–T3.

**Canonical aliases:** Non-canonical entries (redirects, renames, transfers appearing twice, or duplicate listings) counted once under their canonical name:

- `KillianLucas/open-interpreter` → `OpenInterpreter/open-interpreter`
- `OpenDevin/OpenDevin` → `OpenHands/OpenHands`
- `Significant-Gravitas/Auto-GPT` → `Significant-Gravitas/AutoGPT`
- `dot-agent/nextpy` → `dot-agent/dotagent`
- `e2b-dev/awesome-ai-sdks` → `e2b-dev/awesome-sdks-for-ai-agents`
- `emrgnt-cmplxty/Automata` → `emrgnt-cmplxty/automata`
- `joaomdmoura/CrewAI` → `crewAIInc/crewAI`
- `joaomdmoura/crewAI` → `crewAIInc/crewAI`
- `joaomdmoura/crewai` → `crewAIInc/crewAI`
- `paul-gauthier/aider` → `Aider-AI/aider`
- `princeton-nlp/SWE-agent` → `SWE-agent/SWE-agent`

**Transfers:** Enumerated under the old name; repository now lives at the new location:

- `geekan/MetaGPT` → `FoundationAgents/MetaGPT`

## Reference rows (unscored, per rubric §6)

Excluded from scoring by rule; appear on the leaderboard only as marked reference rows:

- **Interlock** — Marcus Richards's provenance-first agent infrastructure (reference implementation).
- **AEGIS** — Agent operating system for AI coding work (Memory Utility Labs).
- **interlock-forensics** — Forensics companion to Interlock.

Not in the candidate universe (not returned by the enumeration query); never self-scored.

## Full candidate ledger (1,023)

`rank | stars | repository | verdict | reason`. `[ALIAS]` = non-canonical duplicate; `[MOVED]` = transferred to a new location.

1 | 391257 | `openclaw/openclaw` | **INCLUDE** | General-purpose AI agent; primary abstraction is an agent loop issuing tool calls.
2 | 272423 | `affaan-m/ECC` | **REJECT** | Harness-optimization skills system for existing coding agents, not an agent loop itself.
3 | 251025 | `NousResearch/hermes-agent` | **INCLUDE** | General-purpose self-improving AI agent with tool-calling loop (verified via README).
4 | 243037 | `deepseek-ai/deepseek-harness` | **INCLUDE** | Plugin-based agent harness.
5 | 188352 | `firecrawl/firecrawl` | **REJECT** | Web-scraping API for agents; single-vertical tool, not an agent loop.
6 | 187644 | `Significant-Gravitas/Auto-GPT` [ALIAS] | **INCLUDE** | Autonomous general-purpose agent (duplicate entry of AutoGPT; counted once).
7 | 187644 | `Significant-Gravitas/AutoGPT` | **INCLUDE** | Autonomous general-purpose agent (duplicate entry of Auto-GPT; counted once).
8 | 182140 | `ollama/ollama` | **REJECT** | Model runner/inference server; no agent loop.
9 | 153789 | `DietrichGebert/ponytail` | **REJECT** | Agent skills/prompting plugin for coding agents, not an agent loop.
10 | 147421 | `langchain-ai/langchain` | **INCLUDE** | Agent engineering platform.
11 | 123603 | `Graphify-Labs/graphify` | **REJECT** | Codebase knowledge-graph tool; single vertical.
12 | 117091 | `browser-use/browser-use` | **REJECT** | Browser-automation agent; single vertical per rubric exclusion.
13 | 107227 | `google-gemini/gemini-cli` | **INCLUDE** | Terminal AI agent with tool use.
14 | 95721 | `thedotmack/claude-mem` | **REJECT** | Memory layer for agents; infrastructure, not an agent loop.
15 | 91642 | `infiniflow/ragflow` | **REJECT** | RAG engine; single vertical.
16 | 90050 | `Panniantong/Agent-Reach` | **REJECT** | Web-access API for agents; tool, not an agent loop.
17 | 89932 | `OpenDevin/OpenDevin` [ALIAS] | **INCLUDE** | AI-driven development agent (duplicate entry of OpenHands; counted once).
18 | 89932 | `OpenHands/OpenHands` | **INCLUDE** | AI-driven development agent (duplicate entry of OpenDevin; counted once).
19 | 84719 | `unclecode/crawl4ai` | **REJECT** | Web crawler for LLMs; single-vertical tool.
20 | 84564 | `stablyai/orca` | **REJECT** | Fleet runner/orchestrator for coding agents; orchestration, not an agent loop.
21 | 83364 | `bytedance/deer-flow` | **INCLUDE** | Long-horizon SuperAgent harness with tools and subagents.
22 | 82975 | `lobehub/lobehub` | **REJECT** | Chat/agent UI platform; primary abstraction is the app, not an agent loop.
23 | 78815 | `dair-ai/Prompt-Engineering-Guide` | **REJECT** | Guide, not software.
24 | 76441 | `ComposioHQ/awesome-claude-skills` | **REJECT** | Curated list, not software.
25 | 76391 | `microsoft/ai-agents-for-beginners` | **REJECT** | Tutorials, not software.
26 | 74350 | `thedaviddias/Front-End-Checklist` | **REJECT** | Checklist, not software.
27 | 73815 | `ruvnet/ruflo` | **INCLUDE** | Agent harness; multi-player swarms and autonomous workflows.
28 | 72734 | `diegosouzapw/OmniRoute` | **REJECT** | AI gateway; infrastructure, not an agent loop.
29 | 71669 | `daytonaio/daytona` | **REJECT** | Infrastructure for running AI-generated code; not an agent loop.
30 | 70732 | `geekan/MetaGPT` [MOVED] | **INCLUDE** | Multi-agent framework.
31 | 69807 | `cline/cline` | **INCLUDE** | Autonomous coding agent (SDK/IDE/CLI).
32 | 69782 | `code-yeongyu/oh-my-openagent` | **REJECT** | Prompt/config for graph engineering, not an agent loop.
33 | 68844 | `asgeirtj/system_prompts_leaks` | **REJECT** | Leaked system prompts documentation, not software.
34 | 68502 | `KillianLucas/open-interpreter` [ALIAS] | **INCLUDE** | Coding agent for open models (duplicate entry; counted once).
35 | 68502 | `OpenInterpreter/open-interpreter` | **INCLUDE** | Coding agent for open models (duplicate entry; counted once).
36 | 67047 | `shanraisshan/claude-code-best-practice` | **REJECT** | Guide, not software.
37 | 66697 | `Mintplex-Labs/anything-llm` | **REJECT** | Local RAG/chat app; primary abstraction is the app, not an agent loop.
38 | 66547 | `mem0ai/mem0` | **REJECT** | Memory infrastructure for agents, not an agent loop.
39 | 63312 | `rohitg00/ai-engineering-from-scratch` | **REJECT** | Tutorial, not software.
40 | 62650 | `upstash/context7` | **REJECT** | Documentation tool for LLMs, not an agent loop.
41 | 61251 | `microsoft/autogen` | **INCLUDE** | Programming framework for agentic AI.
42 | 60108 | `BerriAI/litellm` | **REJECT** | LLM gateway; infrastructure.
43 | 59329 | `crewAIInc/crewAI` | **INCLUDE** | Multi-agent orchestration framework (duplicate entries; counted once).
44 | 59329 | `joaomdmoura/crewai` [ALIAS] | **INCLUDE** | Multi-agent orchestration framework (duplicate entries; counted once).
45 | 59329 | `joaomdmoura/crewAI` [ALIAS] | **INCLUDE** | Multi-agent orchestration framework (duplicate entries; counted once).
46 | 59329 | `joaomdmoura/CrewAI` [ALIAS] | **INCLUDE** | Multi-agent orchestration framework (duplicate entries; counted once).
47 | 57557 | `imartinez/privateGPT` | **REJECT** | Private RAG app; single vertical (duplicate entry; counted once).
48 | 57557 | `zylon-ai/private-gpt` | **REJECT** | Private RAG app; single vertical (duplicate entry; counted once).
49 | 55487 | `FlowiseAI/Flowise` | **REJECT** | Visual builder; human-wired flows per rubric UI exclusion.
50 | 55057 | `AntonOsika/gpt-engineer` | **INCLUDE** | Codegen agent (CLI).
51 | 54922 | `aaif-goose/goose` | **INCLUDE** | Open-source extensible AI agent (block/goose line).
52 | 52404 | `run-llama/llama_index` | **REJECT** | Document-processing/RAG platform; single vertical.
53 | 49365 | `paul-gauthier/aider` [ALIAS] | **INCLUDE** | AI pair-programming agent (duplicate entry; counted once).
54 | 49365 | `Aider-AI/aider` | **INCLUDE** | AI pair-programming agent (duplicate entry; counted once).
55 | 48851 | `calcom/cal.com` | **REJECT** | Scheduling infrastructure.
56 | 48769 | `HKUDS/nanobot` | **INCLUDE** | Personal AI agent framework with tools and memory.
57 | 47228 | `sickn33/agentic-awesome-skills` | **REJECT** | Skills catalog, not software.
58 | 47224 | `zhayujie/CowAgent` | **INCLUDE** | Personal AI assistant and agent harness; plans tasks, runs tools.
59 | 44889 | `MadsLorentzen/ai-job-search` | **REJECT** | Job-search app; single vertical.
60 | 44781 | `janhq/jan` | **REJECT** | ChatGPT alternative; chat wrapper.
61 | 42687 | `langchain-ai/langgraph` | **INCLUDE** | Framework for building resilient agents.
62 | 42543 | `agno-agi/agno` | **INCLUDE** | Agent platform.
63 | 42121 | `herdrdev/herdr` | **REJECT** | Runtime for coding agents; infrastructure, not an agent loop.
64 | 40756 | `HKUDS/DeepTutor` | **REJECT** | Tutoring app; single vertical.
65 | 40556 | `tinyhumansai/openhuman` | **INCLUDE** | Open-source agent harness.
66 | 40183 | `wshobson/agents` | **REJECT** | Plugin marketplace, not software.
67 | 39570 | `Yeachan-Heo/oh-my-claudecode` | **REJECT** | Orchestration pack for Claude Code, not a framework.
68 | 38592 | `VectifyAI/PageIndex` | **REJECT** | RAG tool; single vertical.
69 | 38490 | `stanfordnlp/dspy` | **REJECT** | LM programming framework, not an agent loop.
70 | 38287 | `ashishpatel26/500-AI-Agents-Projects` | **REJECT** | Collection of projects, not software.
71 | 37796 | `microsoft/playwright-mcp` | **REJECT** | MCP server; tool.
72 | 37003 | `ItzCrazyKns/Vane` | **REJECT** | Answering-engine app.
73 | 36298 | `reworkd/AgentGPT` | **INCLUDE** | Autonomous agents in the browser.
74 | 36105 | `continuedev/continue` | **INCLUDE** | Open-source coding agent.
75 | 35599 | `JCodesMore/ai-website-cloner-template` | **REJECT** | Template, not software.
76 | 35429 | `agentscope-ai/QwenPaw` | **REJECT** | Personal assistant app, not a framework.
77 | 35351 | `langfuse/langfuse` | **REJECT** | Observability platform, not an agent loop.
78 | 35176 | `VoltAgent/awesome-agent-skills` | **REJECT** | Skills collection, not software.
79 | 34439 | `OpenBMB/ChatDev` | **INCLUDE** | Multi-agent collaboration for software development.
80 | 33893 | `TabbyML/tabby` | **REJECT** | Coding assistant; primary abstraction is assistance, not an agent loop.
81 | 33761 | `mukul975/Anthropic-Cybersecurity-Skills` | **REJECT** | Skills collection, not software.
82 | 33659 | `Pythagora-io/gpt-pilot` | **INCLUDE** | AI developer (coding agent).
83 | 33532 | `virgiliojr94/book-to-skill` | **REJECT** | Tool, not an agent loop.
84 | 33351 | `github/github-mcp-server` | **REJECT** | MCP server; tool.
85 | 33259 | `getcursor/cursor` | **REJECT** | Closed-source; excluded by rule.
86 | 32174 | `Fincept-Corporation/FinceptTerminal` | **REJECT** | Finance app; single vertical.
87 | 31882 | `CloakHQ/CloakBrowser` | **REJECT** | Stealth browser; tool.
88 | 31338 | `topoteretes/cognee` | **REJECT** | Memory platform for agents; infrastructure.
89 | 30876 | `nanocoai/nanoclaw` | **INCLUDE** | Lightweight agent (OpenClaw-like).
90 | 30426 | `ComposioHQ/composio` | **REJECT** | Toolkits for agents; tool infrastructure.
91 | 30261 | `decolua/9router` | **REJECT** | AI gateway; infrastructure.
92 | 29970 | `oraios/serena` | **REJECT** | MCP toolkit; tool.
93 | 29902 | `assafelovic/gpt-researcher` | **INCLUDE** | Autonomous research agent (broad domain).
94 | 29826 | `openai/openai-agents-python` | **INCLUDE** | Framework for multi-agent workflows.
95 | 29812 | `jackwener/OpenCLI` | **REJECT** | Tool, not an agent loop.
96 | 29667 | `huggingface/smolagents` | **INCLUDE** | Barebones agent library (code agents).
97 | 29433 | `chroma-core/chroma` | **REJECT** | Vector database; infrastructure.
98 | 29320 | `alibaba/page-agent` | **REJECT** | In-page GUI agent; single vertical (web).
99 | 29062 | `kestra-io/kestra` | **REJECT** | Orchestration platform; workflow UI per rubric exclusion.
100 | 28935 | `pydantic/pydantic` | **REJECT** | Validation library, not software.
101 | 28797 | `harvard-edge/cs249r_book` | **REJECT** | Textbook, not software.
102 | 28544 | `mastra-ai/mastra` | **INCLUDE** | TypeScript framework for AI applications and agents.
103 | 28256 | `BloopAI/vibe-kanban` | **REJECT** | Kanban UI for coding agents; orchestration UI, not an agent loop.
104 | 27107 | `vercel/ai` | **REJECT** | AI SDK; primary abstraction is LLM primitives, not an agent loop.
105 | 26648 | `deepset-ai/haystack` | **REJECT** | Pipeline orchestration framework; primary abstraction is pipelines, not an agent loop.
106 | 25723 | `enescingoz/awesome-n8n-templates` | **REJECT** | Templates, not software.
107 | 25720 | `Donchitos/Claude-Code-Game-Studios` | **REJECT** | Prompt/skill pack for Claude Code, not a framework.
108 | 25530 | `browserbase/stagehand` | **REJECT** | Browser-automation SDK; single vertical.
109 | 25488 | `VoltAgent/awesome-claude-code-subagents` | **REJECT** | Collection, not software.
110 | 25384 | `microsoft/JARVIS` | **REJECT** | Research system connecting LLMs to ML; single purpose, not a framework.
111 | 25278 | `titanwings/distilly` | **REJECT** | Skills distillation tool, not an agent loop.
112 | 25228 | `vxcontrol/pentagi` | **REJECT** | Autonomous pentesting agents; single vertical.
113 | 25022 | `letta-ai/letta` | **INCLUDE** | Platform for stateful agents (duplicate entry of MemGPT; counted once).
114 | 25022 | `cpacker/MemGPT` | **INCLUDE** | Platform for stateful agents (duplicate entry of letta; counted once).
115 | 24888 | `activepieces/activepieces` | **REJECT** | Workflow-automation platform; UI exclusion.
116 | 24606 | `pascalorg/editor` | **REJECT** | 3D architectural editor; not an agent loop.
117 | 24569 | `dolthub/dolt` | **REJECT** | Git for data; not an agent loop.
118 | 24454 | `NirDiamant/GenAI_Agents` | **REJECT** | Tutorials, not software.
119 | 24447 | `nocobase/nocobase` | **REJECT** | No-code platform, not an agent loop.
120 | 23812 | `vanna-ai/vanna` | **REJECT** | Text-to-SQL chat; single vertical.
121 | 23132 | `Skyvern-AI/skyvern` | **REJECT** | Browser-workflow automation; single vertical.
122 | 23082 | `micro/go-micro` | **REJECT** | Microservices framework; primary abstraction is services, not agents.
123 | 22650 | `NVIDIA/NemoClaw` | **REJECT** | Secure runner for agents; infrastructure, not an agent loop.
124 | 22364 | `comet-ml/opik` | **REJECT** | Observability platform, not an agent loop.
125 | 22363 | `yoheinakajima/babyagi` | **INCLUDE** | Task-driven autonomous agent (classic agent loop).
126 | 22194 | `PromtEngineer/localGPT` | **REJECT** | Document chat (RAG); single vertical.
127 | 21863 | `docmost/docmost` | **REJECT** | Wiki software, not an agent loop.
128 | 21805 | `screenpipe/screenpipe` | **REJECT** | Computer-history recorder; tool, not an agent loop.
129 | 21788 | `guidance-ai/guidance` | **REJECT** | Control language for LLMs, not an agent loop.
130 | 21701 | `google/adk-python` | **INCLUDE** | Agent Development Kit (Python).
131 | 21526 | `NirDiamant/agents-towards-production` | **REJECT** | Tutorials, not software.
132 | 21141 | `KKKKhazix/khazix-skills` | **REJECT** | Skills collection, not software.
133 | 21050 | `jnMetaCode/agency-agents-zh` | **REJECT** | Agent-role pack, not a framework.
134 | 20484 | `princeton-nlp/SWE-agent` [ALIAS] | **INCLUDE** | Autonomous coding agent for GitHub issues (duplicate entry; counted once).
135 | 20484 | `SWE-agent/SWE-agent` | **INCLUDE** | Autonomous coding agent for GitHub issues (duplicate entry; counted once).
136 | 20299 | `hummingbot/hummingbot` | **REJECT** | Crypto-trading bots; single vertical.
137 | 20245 | `kortix-ai/suna` | **INCLUDE** | Open-source generalist AI agent (autonomous).
138 | 20077 | `eosphoros-ai/DB-GPT` | **REJECT** | Agentic data assistant; single vertical (data).
139 | 19557 | `stitionai/devika` | **INCLUDE** | Agentic software engineer (coding agent).
140 | 19107 | `hypit-ai/hypit` | **REJECT** | Viral-video cloner; single vertical.
141 | 18754 | `nesquena/hermes-webui` | **REJECT** | WebUI for Hermes Agent; interface, not an agent loop.
142 | 18736 | `walkinglabs/learn-harness-engineering` | **REJECT** | Tutorial, not software.
143 | 18299 | `emcie-co/parlant` | **INCLUDE** | Harness for building customer-facing AI agents.
144 | 18246 | `langchain-ai/langchainjs` | **INCLUDE** | Agent engineering platform (JS).
145 | 18210 | `RightNow-AI/openfang` | **INCLUDE** | Open-source Agent Operating System (agent).
146 | 17996 | `rowboatlabs/rowboat` | **INCLUDE** | AI coworker agent with memory.
147 | 17809 | `camel-ai/camel` | **INCLUDE** | Multi-agent framework.
148 | 17800 | `Canner/WrenAI` | **REJECT** | Text-to-SQL (GenBI); single vertical.
149 | 17463 | `img2threejs/img2threejs` | **REJECT** | Image-to-3D tool; single vertical.
150 | 17074 | `tradecatlabs/vibe-coding-cn` | **REJECT** | Tutorial, not software.
151 | 16963 | `cft0808/edict` | **REJECT** | Specific multi-agent orchestration setup, not a general framework.
152 | 16634 | `earthtojake/text-to-cad` | **REJECT** | CAD tool for agents; tool, not an agent loop.
153 | 16461 | `triggerdotdev/trigger.dev` | **REJECT** | Durable-workflow platform; primary abstraction is workflows.
154 | 16424 | `HBAI-Ltd/Toonflow-app` | **REJECT** | AI creation platform (images/video); single vertical.
155 | 16295 | `ag-ui-protocol/ag-ui` | **REJECT** | Agent-user interaction protocol; specification, not an agent loop.
156 | 15898 | `dottxt-ai/outlines` | **REJECT** | Structured-outputs library, not an agent loop.
157 | 15688 | `plandex-ai/plandex` | **INCLUDE** | Open-source AI coding agent.
158 | 15276 | `n8n-io/self-hosted-ai-starter-kit` | **REJECT** | Template, not software.
159 | 14859 | `superset-sh/superset` | **REJECT** | Agentic IDE orchestrating coding agents; orchestration, not an agent loop.
160 | 14467 | `livekit/agents` | **INCLUDE** | Framework for building realtime voice AI agents.
161 | 14354 | `waooAI/waoowaoo` | **REJECT** | AI film-production platform; single vertical.
162 | 14143 | `e2b-dev/E2B` | **REJECT** | Sandboxed execution environments for agents; infrastructure, not an agent loop (duplicate entry; counted once).
163 | 14143 | `e2b-dev/e2b` | **REJECT** | Sandboxed execution environments for agents; infrastructure, not an agent loop (duplicate entry; counted once).
164 | 13972 | `567-labs/instructor` | **REJECT** | Structured-outputs library, not an agent loop.
165 | 13933 | `microsoft/agent-framework` | **INCLUDE** | Framework for building and orchestrating AI agents.
166 | 13904 | `nanobrowser/nanobrowser` | **REJECT** | Web-automation browser extension; single vertical.
167 | 13813 | `browseros-ai/BrowserOS` | **REJECT** | Agentic browser; single vertical.
168 | 13595 | `XiaomiMiMo/MiMo-Code` | **REJECT** | Description does not establish an agent loop (model/agent co-evolution research).
169 | 13383 | `corsairdev/corsair` | **REJECT** | App-integration connector, not an agent loop.
170 | 13052 | `InsForge/InsForge` | **REJECT** | Backend platform for coding agents; platform, not an agent loop.
171 | 12991 | `neuml/txtai` | **REJECT** | Semantic-search framework; primary abstraction is search, not an agent loop.
172 | 12529 | `simular-ai/Agent-S` | **INCLUDE** | Open agentic framework for computer use.
173 | 12303 | `0x4m4/hexstrike-ai` | **REJECT** | MCP server; tool.
174 | 12186 | `smol-ai/developer` | **INCLUDE** | Library for embedding a developer agent in apps.
175 | 11725 | `Jeffallan/claude-skills` | **REJECT** | Skills collection, not software.
176 | 11701 | `Arize-ai/phoenix` | **REJECT** | Observability platform, not an agent loop.
177 | 11693 | `MemTensor/MemOS` | **REJECT** | Memory OS for agents; infrastructure.
178 | 11643 | `cocoindex-io/cocoindex` | **REJECT** | Data engine for agents; infrastructure, not an agent loop.
179 | 11456 | `holaboss-ai/holaOS` | **REJECT** | Agentic workspace (platform), not an agent loop.
180 | 11412 | `cobusgreyling/loop-engineering` | **REJECT** | Patterns and tools for loop engineering, not a framework.
181 | 11091 | `aden-hive/hive` | **INCLUDE** | Multi-agent harness for production AI.
182 | 11080 | `bytebot-ai/bytebot` | **INCLUDE** | Self-hosted AI desktop agent.
183 | 11013 | `NopeCHALLC/nopecha-extension` | **REJECT** | CAPTCHA solver; tool.
184 | 10932 | `google/artemis` | **REJECT** | Android-automation agent; single vertical.
185 | 10723 | `VoltAgent/voltagent` | **INCLUDE** | AI agent engineering platform (TypeScript).
186 | 10485 | `sigoden/aichat` | **REJECT** | LLM CLI tool; agent features secondary to chat.
187 | 10467 | `omnigent-ai/omnigent` | **REJECT** | Meta-harness orchestrating existing coding agents; orchestration.
188 | 10297 | `OthersideAI/self-operating-computer` | **INCLUDE** | Framework for computer operation by multimodal models.
189 | 10279 | `astrid-runtime/astrid` | **REJECT** | Capability-secure OS; not an agent loop.
190 | 9956 | `cloudflare/moltworker` | **REJECT** | Deployment adapter for OpenClaw on Workers.
191 | 9911 | `microsoft/UFO` | **REJECT** | Windows UI-automation agent; single vertical.
192 | 9780 | `alirezadir/AIMLInterviews` | **REJECT** | Interview guide, not software.
193 | 9723 | `unicity-sphere/sphere` | **REJECT** | Web3 wallet and agent platform; app.
194 | 9645 | `frankbria/ralph-claude-code` | **REJECT** | Autonomous loop script for Claude Code; pattern, not a framework.
195 | 9567 | `droidrun/mobilerun` | **REJECT** | Mobile-device automation; single vertical.
196 | 9555 | `ntegrals/openbrowser` | **REJECT** | Browser toolkit for agents; tool, single vertical.
197 | 9552 | `trailhq/Graft` | **REJECT** | Optimization tool for coding agents, not an agent loop.
198 | 9492 | `BloopAI/bloop` | **REJECT** | Code-search engine; tool.
199 | 9407 | `Nasiko-Labs/nasiko` | **REJECT** | Runtime for AI agents; infrastructure, not an agent loop.
200 | 9381 | `BoundaryML/baml` | **REJECT** | Programming language for agents, not an agent loop.
201 | 9376 | `modelcontextprotocol/modelcontextprotocol` | **REJECT** | Protocol specification, not an agent loop.
202 | 9131 | `MervinPraison/PraisonAI` | **INCLUDE** | Multi-agent framework (AI workforce).
203 | 9131 | `mnfst/awesome-free-llm-apis` | **REJECT** | List, not software.
204 | 8998 | `nexu-io/html-anything` | **REJECT** | Agentic HTML editor; tool.
205 | 8719 | `liyupi/codefather` | **REJECT** | Programming guide, not software.
206 | 8689 | `microsoft/TypeChat` | **REJECT** | Natural-language-interface library, not an agent loop.
207 | 8647 | `strands-agents/harness-sdk` | **INCLUDE** | SDK for building and controlling an agent harness.
208 | 8568 | `lastmile-ai/mcp-agent` | **INCLUDE** | Agent framework built on Model Context Protocol.
209 | 8552 | `OpenBMB/XAgent` | **INCLUDE** | Autonomous LLM agent for complex task solving.
210 | 8525 | `firerpa/lamda` | **REJECT** | Android device-control platform; tool.
211 | 8398 | `automazeio/ccpm` | **REJECT** | Project-management skill system, not an agent loop.
212 | 8370 | `HarnessMD/munder-difflin` | **REJECT** | Claude Code office orchestration; orchestration, not a framework.
213 | 8213 | `anthropics/claude-agent-sdk-python` | **INCLUDE** | Official Claude Agent SDK.
214 | 8151 | `GetStream/Vision-Agents` | **INCLUDE** | Framework for voice and vision agents.
215 | 8077 | `YaoApp/yao` | **REJECT** | Agent workspace app, not an agent loop.
216 | 7956 | `Upsonic/Upsonic` | **INCLUDE** | Framework for autonomous AI agents (Python).
217 | 7886 | `datahaven-xyz/datahaven` | **REJECT** | Blockchain, not an agent loop.
218 | 7781 | `2FastLabs/agent-squad` | **INCLUDE** | Framework for managing multiple AI agents.
219 | 7733 | `steel-dev/steel-browser` | **REJECT** | Browser API for agents; infrastructure.
220 | 7619 | `flyteorg/flyte` | **REJECT** | Orchestration platform, not an agent loop.
221 | 7524 | `Gentleman-Programming/gentle-ai` | **REJECT** | Config for coding agents, not an agent loop.
222 | 7483 | `Human-Agent-Society/reef` | **REJECT** | Infrastructure for self-improving agents, not an agent loop.
223 | 7482 | `guardrails-ai/guardrails` | **REJECT** | Guardrails library, not an agent loop.
224 | 7455 | `plastic-labs/honcho` | **REJECT** | Memory library, not an agent loop.
225 | 7388 | `arcee-ai/mergekit` | **REJECT** | Model-merging tools, not an agent loop.
226 | 7340 | `WenyuChiou/awesome-agentic-ai-zh` | **REJECT** | Learning roadmap, not software.
227 | 7271 | `Zipstack/unstract` | **REJECT** | Unstructured-data extraction; single vertical.
228 | 7267 | `xerrors/Yuxi` | **REJECT** | Knowledge-agent platform; single vertical (knowledge/RAG).
229 | 7243 | `MineDojo/Voyager` | **REJECT** | Embodied Minecraft agent; single vertical.
230 | 7243 | `NVIDIA-NeMo/Guardrails` | **REJECT** | Guardrails toolkit, not an agent loop.
231 | 7230 | `kyegomez/swarms` | **INCLUDE** | Multi-agent orchestration framework.
232 | 7220 | `steipete/agent-scripts` | **REJECT** | Scripts, not software.
233 | 7154 | `deanpeters/Product-Manager-Skills` | **REJECT** | Skills collection, not software.
234 | 7139 | `AIPentest/CyberStrikeAI` | **REJECT** | Cybersecurity agents; single vertical.
235 | 7137 | `enricoros/big-AGI` | **REJECT** | AI chat suite; app, not an agent loop.
236 | 7082 | `TokenRhythm/opensquilla` | **INCLUDE** | Token-efficient AI agent.
237 | 7047 | `grab/cursor-talk-to-figma-mcp` | **REJECT** | MCP integration; tool.
238 | 7008 | `XiaoDuoYa/codex-with-chatgpt` | **REJECT** | Config/pattern, not software.
239 | 7002 | `yjh051108/dsh-routing-suite` | **REJECT** | Router kit, not an agent loop.
240 | 6976 | `0xpayne/gpt-migrate` | **REJECT** | Codebase-migration tool; single vertical.
241 | 6974 | `open-multi-agent/open-multi-agent` | **INCLUDE** | Self-hosted TypeScript agent runtime.
242 | 6971 | `Osmantic/ODS` | **REJECT** | Pre-release; description does not establish an agent loop.
243 | 6765 | `homanp/superagent` | **REJECT** | Prompt-injection protection; security tool (duplicate entry; counted once).
244 | 6765 | `superagent-ai/superagent` | **REJECT** | Prompt-injection protection; security tool (duplicate entry; counted once).
245 | 6725 | `GreptimeTeam/greptimedb` | **REJECT** | Observability database, not an agent loop.
246 | 6626 | `TencentCloud/Octop` | **REJECT** | AI assistant app, not a framework.
247 | 6614 | `Devin-AXIS/iPolloWork` | **REJECT** | Agent workbench; orchestration UI.
248 | 6613 | `BlockRunAI/ClawRouter` | **REJECT** | LLM router; infrastructure.
249 | 6578 | `julep-ai/julep` | **INCLUDE** | Durable, composable AI agents (framework).
250 | 6560 | `airweave-ai/airweave` | **REJECT** | Context-retrieval layer; infrastructure.
251 | 6548 | `anus-dev/anus` | **INCLUDE** | Free coding agent in the terminal.
252 | 6530 | `linyiLYi/street-fighter-ai` | **REJECT** | Street Fighter II agent; single vertical (game).
253 | 6445 | `agiresearch/AIOS` | **REJECT** | AI Agent Operating System; infrastructure, not an agent loop.
254 | 6426 | `lexmount/moli` | **REJECT** | Headless browser for agents; tool, single vertical.
255 | 6389 | `microsoft/agent-governance-toolkit` | **REJECT** | Governance toolkit; policy enforcement, not an agent loop.
256 | 6382 | `e2b-dev/fragments` | **REJECT** | Next.js template for AI-generated apps; not an agent loop.
257 | 6370 | `czlonkowski/n8n-skills` | **REJECT** | n8n skillset; skills, not an agent loop.
258 | 6359 | `internet-court/internet-court-skill` | **REJECT** | Trust layer for agent commerce; not an agent loop.
259 | 6339 | `mahseema/awesome-ai-tools` | **REJECT** | Curated list, not software.
260 | 6307 | `Sylinko/Everywhere` | **REJECT** | Desktop AI assistant app; not a framework.
261 | 6300 | `builderz-labs/mission-control` | **REJECT** | Control plane for agents; orchestration, not an agent loop.
262 | 6271 | `VoltAgent/awesome-codex-subagents` | **REJECT** | Subagent collection, not software.
263 | 6258 | `heilcheng/awesome-agent-skills` | **REJECT** | Tutorials and directories, not software.
264 | 6204 | `PrefectHQ/marvin` | **REJECT** | Ambient-intelligence library; not an agent loop.
265 | 6199 | `Helicone/helicone` | **REJECT** | LLM observability platform; not an agent loop.
266 | 6169 | `microsoft/TaskWeaver` | **REJECT** | Code-first agent framework for data analytics; single vertical.
267 | 6147 | `loopx-project/loopx` | **REJECT** | Control plane with durable state kernel; orchestration, not an agent loop.
268 | 6092 | `browser-act/skills` | **REJECT** | Browser-automation CLI; single vertical.
269 | 6076 | `Dicklesworthstone/destructive_command_guard` | **REJECT** | Command guard; tool, not an agent loop.
270 | 5980 | `CopilotKit/OpenBot` | **INCLUDE** | Open-source AI coworkers with their own computers (agent system).
271 | 5967 | `kuafuai/DevOpsGPT` | **INCLUDE** | Multi-agent system for AI-driven software development.
272 | 5965 | `aiwaves-cn/agents` | **INCLUDE** | Open-source framework for data-centric autonomous language agents.
273 | 5960 | `jacklandrin/OnlySwitch` | **REJECT** | Menu-bar app; not an agent loop.
274 | 5944 | `oomol-lab/open-connector` | **REJECT** | Auth gateway; infrastructure, not an agent loop.
275 | 5930 | `liyupi/mianshiya` | **REJECT** | Interview-question website; not an agent loop.
276 | 5881 | `AgentOps-AI/agentops` | **REJECT** | Agent-monitoring SDK; observability, not an agent loop.
277 | 5808 | `Klavis-AI/klavis` | **REJECT** | MCP integration platform; tool infrastructure, not an agent loop.
278 | 5792 | `0xNyk/awesome-hermes-agent` | **REJECT** | Directory, not software.
279 | 5738 | `OpenSenseNova/SenseNova-Skills` | **REJECT** | Skills collection, not an agent loop.
280 | 5735 | `potpie-ai/potpie` | **REJECT** | Context graph for SDLC; infrastructure, not an agent loop.
281 | 5687 | `the-open-agent/openagent` | **REJECT** | Personal AI assistant app; not a framework.
282 | 5658 | `Galaxy-Dawn/claude-scholar` | **REJECT** | Research assistant; single vertical (academic).
283 | 5616 | `junhoyeo/tokscale` | **REJECT** | Token-usage tracker; tool, not an agent loop.
284 | 5387 | `unicity-sphere/sphere-sdk` | **REJECT** | SDK for a specific agent platform; not a general loop.
285 | 5355 | `metalbear-co/mirrord` | **REJECT** | Process mirroring; tool, not an agent loop.
286 | 5303 | `filipecalegario/awesome-vibe-coding` | **REJECT** | Curated list, not software.
287 | 5298 | `beclab/Olares` | **REJECT** | Personal cloud OS for agents; infrastructure, not an agent loop.
288 | 5202 | `Adam-CAD/CADAM` | **REJECT** | Text-to-CAD web app; single vertical.
289 | 5153 | `OpenBMB/AgentVerse` | **INCLUDE** | Framework for deploying multiple LLM-based agents.
290 | 5129 | `EverMind-AI/Raven` | **INCLUDE** | Harness of harnesses; persistent self-evolving multi-agent system.
291 | 5086 | `ApodexAI/FrontierAgent` | **INCLUDE** | Agent framework (native command tools).
292 | 5036 | `developersdigest/llm-answer-engine` | **REJECT** | Answer-engine app; not an agent loop.
293 | 5020 | `GaiaNet-AI/gaianet-node` | **REJECT** | Node for deploying agent services; infrastructure, not an agent loop.
294 | 4961 | `FellouAI/eko` | **REJECT** | Agentic-workflow builder; workflow tool, not an agent loop.
295 | 4948 | `getzep/zep` | **REJECT** | Examples and integrations; not an agent loop.
296 | 4919 | `SolaceLabs/solace-agent-mesh` | **INCLUDE** | Event-driven framework for multi-agent AI systems.
297 | 4905 | `aipotheosis-labs/aci` | **REJECT** | Tool-calling platform; tool infrastructure, not an agent loop.
298 | 4887 | `darrenhinde/OpenAgentsControl` | **INCLUDE** | AI agent framework for plan-first development workflows.
299 | 4886 | `breferrari/obsidian-mind` | **REJECT** | Obsidian vault memory; infrastructure, not an agent loop.
300 | 4883 | `callstack/agent-device` | **REJECT** | Mobile-app automation for agents; tool, not an agent loop.
301 | 4863 | `xlang-ai/OpenAgents` | **INCLUDE** | Open platform for language agents.
302 | 4828 | `pguso/ai-agents-from-scratch` | **REJECT** | Tutorial, not software.
303 | 4808 | `Agenta-AI/agenta` | **REJECT** | Workspace for building agents; platform, not an agent loop.
304 | 4781 | `mvanhorn/cli-printing-press` | **REJECT** | API tool; not an agent loop.
305 | 4771 | `thunderbird/thunderbolt` | **REJECT** | AI app; not an agent loop.
306 | 4770 | `Integuru-AI/Integuru` | **REJECT** | Integration-building agent; single vertical.
307 | 4745 | `liveblocks/liveblocks` | **REJECT** | Realtime infrastructure; not an agent loop.
308 | 4692 | `ai-boost/awesome-harness-engineering` | **REJECT** | Awesome list, not software.
309 | 4677 | `NateBJones-Projects/OB1` | **REJECT** | Thinking infrastructure; not an agent loop.
310 | 4666 | `eugeniughelbur/obsidian-second-brain` | **REJECT** | Persistent memory; infrastructure, not an agent loop.
311 | 4659 | `serenakeyitan/awesome-notebookLM-prompts` | **REJECT** | Prompts collection, not software.
312 | 4634 | `Gaurav-Gosain/tuios` | **REJECT** | Terminal window manager; not an agent loop.
313 | 4591 | `memgraph/memgraph` | **REJECT** | Graph database; infrastructure, not an agent loop.
314 | 4590 | `VRSEN/agency-swarm` | **INCLUDE** | Reliable multi-agent orchestration framework.
315 | 4579 | `FareedKhan-dev/all-agentic-architectures` | **REJECT** | Architectures collection, not software.
316 | 4552 | `phodal/auto-dev` | **INCLUDE** | Multi-agent coding development platform.
317 | 4544 | `macro-inc/macro` | **REJECT** | Unified workspace; not an agent loop.
318 | 4536 | `0xNyk/council-of-high-intelligence` | **REJECT** | Deliberation system; not an agent loop.
319 | 4517 | `CaviraOSS/LongMemory` | **REJECT** | Memory store; infrastructure, not an agent loop.
320 | 4486 | `embabel/embabel-agent` | **INCLUDE** | Agent framework for the JVM.
321 | 4461 | `judge0/judge0` | **REJECT** | Code-execution system; tool, not an agent loop.
322 | 4443 | `gptme/gptme` | **INCLUDE** | Terminal agent with local tools.
323 | 4428 | `crmne/ruby_llm` | **INCLUDE** | Ruby-native AI framework with agents and tools.
324 | 4399 | `melgarafael/DeskcommCRM` | **REJECT** | AI sales OS/CRM; single vertical.
325 | 4377 | `miqdadbadjuber/anti-slop` | **REJECT** | Rules for coding agents; not software.
326 | 4343 | `UditAkhourii/adhd` | **REJECT** | Skill for coding agents; not an agent loop.
327 | 4333 | `microsoft/flint-chart` | **REJECT** | Visualization language; tool, not an agent loop.
328 | 4324 | `nolabs-ai/nono` | **REJECT** | Agent-runtime security; infrastructure, not an agent loop.
329 | 4304 | `walkinglabs/awesome-harness-engineering` | **REJECT** | Tools and guides list, not software.
330 | 4266 | `kirodotdev/KiroCrew` | **REJECT** | Persistent workspace; not an agent loop.
331 | 4261 | `wang2122/sprix-sage-router` | **REJECT** | Router for agent networks; infrastructure, not an agent loop.
332 | 4256 | `arcboxlabs/arcbox` | **REJECT** | Machines for running agents; infrastructure, not an agent loop.
333 | 4250 | `dagucloud/dagu` | **REJECT** | Workflow orchestrator; UI exclusion.
334 | 4222 | `GiovanniPasq/agentic-rag-for-dummies` | **REJECT** | Tutorial, not software.
335 | 4189 | `microsoft/skill-recorder` | **REJECT** | Session recorder; tool, not an agent loop.
336 | 4172 | `openagents-org/openagents` | **REJECT** | Collaboration OS for agents; infrastructure, not an agent loop.
337 | 4142 | `nyldn/claude-octopus` | **REJECT** | Multi-model comparison tool; not an agent loop.
338 | 4111 | `langroid/langroid` | **INCLUDE** | Multi-agent programming framework.
339 | 4106 | `abhi1693/openclaw-mission-control` | **REJECT** | Orchestration dashboard; not an agent loop.
340 | 4055 | `sergebulaev/linkedin-skills` | **REJECT** | Skills collection, not an agent loop.
341 | 4051 | `yifanfeng97/Hyper-Extract` | **REJECT** | Text extraction; single vertical, not an agent loop.
342 | 4046 | `muxuuu/serenity-skill` | **REJECT** | Agent skill; not an agent loop.
343 | 4042 | `darkzOGx/youtube-automation-agent` | **REJECT** | YouTube automation; single vertical.
344 | 4012 | `TarrySingh/Artificial-Intelligence-Deep-Learning-Machine-Learning-Tutorials` | **REJECT** | Courses, not software.
345 | 4011 | `milind-soni/OpenMausBot` | **REJECT** | Bot; not a framework.
346 | 3995 | `mergisi/awesome-openclaw-agents` | **REJECT** | Agent templates; not an agent loop.
347 | 3931 | `microsoft/apm` | **REJECT** | Agent package manager; tool, not an agent loop.
348 | 3895 | `nowork-studio/notfair-plugin` | **REJECT** | Skills; not an agent loop.
349 | 3887 | `Sumanth077/Hands-On-AI-Engineering` | **REJECT** | Projects collection, not software.
350 | 3877 | `zvec-ai/zvec-grep` | **REJECT** | Workspace search; tool, not an agent loop.
351 | 3876 | `dromara/liteflow` | **REJECT** | Rule engine; not an agent loop.
352 | 3865 | `nickjvandyke/opencode.nvim` | **REJECT** | Neovim plugin; not an agent loop.
353 | 3859 | `yvgude/lean-ctx` | **REJECT** | Context gateway; infrastructure, not an agent loop.
354 | 3817 | `Atmosphere/atmosphere` | **INCLUDE** | Portable AI agent runtime for the JVM (@Agent class).
355 | 3816 | `Leonxlnx/unlazy` | **REJECT** | Skill for agents; not an agent loop.
356 | 3811 | `pipeshub-ai/pipeshub-ai` | **REJECT** | Context layer; infrastructure, not an agent loop.
357 | 3803 | `HughYau/qiushi-skill` | **REJECT** | Skill; not an agent loop.
358 | 3790 | `tutti-os/tutti` | **REJECT** | Collaboration concept; not identifiably an agent loop.
359 | 3769 | `JetBrains/go-modern-guidelines` | **REJECT** | Guidelines, not software.
360 | 3726 | `stickerdaniel/linkedin-mcp-server` | **REJECT** | MCP server; tool, not an agent loop.
361 | 3723 | `code-yeongyu/lazycodex` | **INCLUDE** | Agent harness for complex codebases.
362 | 3693 | `graykode/abtop` | **REJECT** | Agent monitor; tool, not an agent loop.
363 | 3688 | `hemansnation/AI-Engineer-Headquarters` | **REJECT** | Collection, not software.
364 | 3677 | `strukto-ai/mirage` | **REJECT** | Virtual terminal for agents; infrastructure, not an agent loop.
365 | 3649 | `Ontos-AI/knowhere` | **REJECT** | Extraction tool; single vertical, not an agent loop.
366 | 3618 | `google-antigravity/antigravity-sdk-python` | **INCLUDE** | Python library for building AI agents.
367 | 3590 | `skyhook-io/radar` | **REJECT** | Kubernetes UI; tool, not an agent loop.
368 | 3589 | `truera/trulens` | **REJECT** | LLM evaluation; tool, not an agent loop.
369 | 3555 | `onecli/onecli` | **INCLUDE** | Open-source sandboxed agent harness for teams.
370 | 3550 | `foryourhealth111-pixel/Vibe-Skills` | **REJECT** | Skill routing; tool, not an agent loop.
371 | 3549 | `agentscope-ai/ReMe` | **REJECT** | Memory management kit; infrastructure, not an agent loop.
372 | 3519 | `NVIDIA/skills` | **REJECT** | Skills collection, not an agent loop.
373 | 3489 | `Jakubantalik/thinking-orbs` | **REJECT** | UI indicators; not an agent loop.
374 | 3454 | `entropy-research/Devon` | **INCLUDE** | Open-source pair programmer (agent).
375 | 3405 | `RunMaestro/Maestro` | **REJECT** | Orchestration command center; not an agent loop.
376 | 3379 | `Ataraxy-Labs/sem` | **REJECT** | Version control; tool, not an agent loop.
377 | 3363 | `metorial/metorial` | **REJECT** | Integration connector; tool, not an agent loop.
378 | 3362 | `ANative-Lab/EvoAgentX` | **INCLUDE** | Self-evolving multi-agent ecosystem framework.
379 | 3335 | `langchain-ai/langgraphjs` | **INCLUDE** | Framework for resilient language agents as graphs (JS).
380 | 3317 | `johnbean393/Sidekick` | **REJECT** | macOS LLM chat app; not an agent loop.
381 | 3301 | `elie222/rakazo` | **REJECT** | Bot; not a framework.
382 | 3286 | `amitshekhariitbhu/ai-engineering-interview-questions` | **REJECT** | Interview questions, not software.
383 | 3278 | `pezzolabs/pezzo` | **REJECT** | LLMOps platform; not an agent loop.
384 | 3269 | `Louis-CFM/coucou` | **REJECT** | Desktop companion app; not an agent loop.
385 | 3266 | `open-webui/open-terminal` | **REJECT** | Cloud computer; not an agent loop.
386 | 3264 | `oxylabs/ai-crawler-py` | **REJECT** | Web crawler; single vertical, not an agent loop.
387 | 3259 | `liaohch3/claude-tap` | **REJECT** | API-traffic inspector; tool, not an agent loop.
388 | 3217 | `Josh-XT/AGiXT` | **REJECT** | Agent automation platform; orchestration, not an agent loop.
389 | 3171 | `TurixAI/TuriX-CUA` | **REJECT** | Official website; not the agent software itself.
390 | 3171 | `dosco/graphjin` | **REJECT** | Graph for agents; infrastructure, not an agent loop.
391 | 3169 | `lackeyjb/playwright-skill` | **REJECT** | Skill; not an agent loop.
392 | 3164 | `Forward-Future/loopy` | **INCLUDE** | Library of practical AI-agent loops.
393 | 3162 | `mikeyobrien/ralph-orchestrator` | **REJECT** | Technique implementation; pattern, not a framework.
394 | 3161 | `wquguru/harness-books` | **REJECT** | Books, not software.
395 | 3161 | `TanStack/ai` | **REJECT** | TypeScript AI SDK; primitives, not an agent loop.
396 | 3142 | `ScrapeCreators/social-media-research-skills` | **REJECT** | Skills; not an agent loop.
397 | 3137 | `GH05TCREW/pentestagent` | **REJECT** | Pentest agent framework; single vertical (security).
398 | 3127 | `SynkraAI/aiox-core` | **REJECT** | AI-orchestrated dev system; orchestration, not an agent loop.
399 | 3125 | `KhazP/vibe-coding-prompt-template` | **REJECT** | Templates, not software.
400 | 3118 | `allenpeng0705/EnvoyMesh` | **REJECT** | P2P mesh for agents; infrastructure, not an agent loop.
401 | 3112 | `MaxMiksa/Auto-Company` | **REJECT** | Specific autonomous system; not a general framework.
402 | 3101 | `oceanbase/seekdb` | **REJECT** | AI-native search database; infrastructure, not an agent loop.
403 | 3091 | `wesammustafa/Claude-Code-Everything-You-Need-to-Know` | **REJECT** | Guide, not software.
404 | 3053 | `MemMachine/MemMachine` | **REJECT** | Memory layer; infrastructure, not an agent loop.
405 | 3038 | `bergside/awesome-design-skills` | **REJECT** | List, not software.
406 | 3000 | `Tiger3807861189/J-Space-Cognition-Suite` | **REJECT** | Inference-time control suite; not an agent loop.
407 | 2997 | `eli64s/readme-ai` | **REJECT** | README generator; tool, not an agent loop.
408 | 2966 | `gmpetrov/databerry` | **REJECT** | No-code platform for building agents; UI exclusion.
409 | 2924 | `muellerberndt/mini-agi` | **INCLUDE** | Simple general-purpose AI agent.
410 | 2919 | `deeplethe/forkd` | **REJECT** | microVM forking; infrastructure, not an agent loop.
411 | 2900 | `rohitg00/pro-workflow` | **REJECT** | Self-correcting memory; tool, not an agent loop.
412 | 2865 | `HarnessRouter/harnessrouter` | **REJECT** | Router; infrastructure, not an agent loop.
413 | 2821 | `datachain-ai/datachain` | **REJECT** | Context layer; infrastructure, not an agent loop.
414 | 2806 | `jeremylongshore/tons-of-skills-marketplace` | **REJECT** | Skills marketplace; not an agent loop.
415 | 2775 | `marketcalls/openalgo` | **REJECT** | Algo-trading platform; single vertical.
416 | 2748 | `wquguru/nof0` | **REJECT** | AI trading arena; single vertical.
417 | 2740 | `AtomicBot-ai/atomic-agent` | **INCLUDE** | Local-first AI agent.
418 | 2728 | `Armur-Ai/Pentest-Swarm-AI` | **REJECT** | Pentest swarm; single vertical (security).
419 | 2716 | `refraction-ray/xalpha` | **REJECT** | Backtest engine; tool, not an agent loop.
420 | 2712 | `runkids/skillshare` | **REJECT** | Skills/agent manager; tool, not an agent loop.
421 | 2702 | `wanikua/danghuangshang` | **INCLUDE** | Open-source multi-agent collaboration system.
422 | 2695 | `supabase/agent-skills` | **REJECT** | Skills; not an agent loop.
423 | 2688 | `yaojingang/yao-meta-skill` | **REJECT** | Meta-skill; not an agent loop.
424 | 2677 | `Nicolepcx/ai-agents-the-definitive-guide` | **REJECT** | Guide, not software.
425 | 2670 | `crbnos/carbon` | **REJECT** | Manufacturing ERP; single vertical, not an agent loop.
426 | 2662 | `brightdata/brightdata-mcp` | **REJECT** | MCP server; tool, not an agent loop.
427 | 2661 | `Natively-AI-assistant/natively-cluely-ai-assistant` | **REJECT** | Meeting assistant; single vertical.
428 | 2645 | `agentrhq/webcmd` | **REJECT** | Agent browser; single vertical.
429 | 2645 | `wshobson/commands` | **REJECT** | Archived commands; not software.
430 | 2607 | `Agent-Field/agentfield` | **REJECT** | Platform for running agents; not an agent loop itself.
431 | 2585 | `kayba-ai/agentic-context-engine` | **REJECT** | Learning infrastructure; not an agent loop.
432 | 2581 | `feder-cr/dots` | **REJECT** | Web agent with browser; single vertical.
433 | 2578 | `datawhalechina/deepagents-in-action` | **REJECT** | Tutorial, not software.
434 | 2553 | `webfuse-com/awesome-autoresearch` | **REJECT** | Curated list, not software.
435 | 2541 | `biobootloader/mentat` | **REJECT** | No description; coding assistant (defunct), cannot verify.
436 | 2524 | `QIN2DIM/hcaptcha-challenger` | **REJECT** | CAPTCHA solver; tool, not an agent loop.
437 | 2497 | `Nano-Collective/nanocoder` | **INCLUDE** | Open coding agent for the terminal.
438 | 2486 | `itmeo/webgradients` | **REJECT** | Gradients; not an agent loop.
439 | 2471 | `lennney/stop-that-shit` | **REJECT** | Hook/skill guard; tool, not an agent loop.
440 | 2458 | `wxtsky/CodeIsland` | **REJECT** | Status panel; tool, not an agent loop.
441 | 2454 | `zerobootdev/zeroboot` | **REJECT** | VM sandboxes; infrastructure, not an agent loop.
442 | 2444 | `vercel/workflow` | **REJECT** | Workflow SDK; primary abstraction is workflows, not an agent loop.
443 | 2439 | `dsphper/lanhu-mcp` | **REJECT** | MCP server; tool, not an agent loop.
444 | 2414 | `K-Dense-AI/claude-scientific-writer` | **REJECT** | Scientific writer; single vertical.
445 | 2403 | `apify/agent-skills` | **REJECT** | Skills collection, not an agent loop.
446 | 2401 | `FrancyJGLisboa/agent-skills-platform` | **REJECT** | Skills platform; not an agent loop.
447 | 2390 | `redhat-et/ripwire` | **REJECT** | Context search CLI; tool, not an agent loop.
448 | 2386 | `Turbo1123/roubao` | **REJECT** | Android automation; single vertical, not an agent loop.
449 | 2377 | `study8677/awesome-architecture` | **REJECT** | Tutorials, not software.
450 | 2375 | `agentuniverse-ai/agentUniverse` | **INCLUDE** | LLM multi-agent framework.
451 | 2366 | `0xMassi/webclaw` | **REJECT** | Web-content extraction; tool, single vertical, not an agent loop.
452 | 2363 | `DenisSergeevitch/agents-best-practices` | **REJECT** | Agent skill; not an agent loop.
453 | 2361 | `KrishMunot/awesome-startup` | **REJECT** | Resources collection, not software.
454 | 2359 | `tigerless-labs/agent-memory` | **REJECT** | Memory runtime; infrastructure, not an agent loop.
455 | 2356 | `datopian/portaljs` | **REJECT** | Framework for data portals; single vertical.
456 | 2348 | `dot-agent/nextpy` [ALIAS] | **REJECT** | Unverifiable claims; not identifiably an agent loop (duplicate entry; counted once).
457 | 2348 | `dot-agent/dotagent` | **REJECT** | Unverifiable claims; not identifiably an agent loop (duplicate entry; counted once).
458 | 2328 | `langchain-ai/langserve` | **REJECT** | Deployment for LangChain runnables; infrastructure, not an agent loop.
459 | 2327 | `xzf-thu/VoiceMem` | **REJECT** | Voice-agent infrastructure; not an agent loop.
460 | 2321 | `jnMetaCode/agency-orchestrator` | **REJECT** | Specific one-person-company system; not a general framework.
461 | 2319 | `iFurySt/open-codex-computer-use` | **INCLUDE** | Open-source computer-use agent.
462 | 2311 | `moorcheh-ai/memanto` | **REJECT** | Memory; infrastructure, not an agent loop.
463 | 2309 | `zebbern/no-cost-ai` | **REJECT** | List, not software.
464 | 2309 | `Appllama/appllama-skills` | **REJECT** | Skills; not an agent loop.
465 | 2308 | `trypromptly/LLMStack` | **REJECT** | No-code multi-agent framework; UI exclusion.
466 | 2306 | `0xSteph/pentest-ai-agents` | **REJECT** | Pentest agents; single vertical (security).
467 | 2304 | `ChunelFeng/CGraph` | **REJECT** | DAG framework; not an agent loop.
468 | 2300 | `Infisical/agent-vault` | **REJECT** | Credential vault; infrastructure, not an agent loop.
469 | 2296 | `Sahir619/fable-method` | **REJECT** | Workflow distilled into skills; not an agent loop.
470 | 2287 | `agiresearch/OpenAGI` | **REJECT** | Research project; not a framework.
471 | 2281 | `google/mantis` | **REJECT** | Toolkit for coding agents; tool, not an agent loop.
472 | 2267 | `agno-agi/dash` | **REJECT** | Data agent; single vertical.
473 | 2259 | `cortexkit/magic-context` | **REJECT** | Memory/context; infrastructure, not an agent loop.
474 | 2253 | `GammaLabTechnologies/harmonist` | **REJECT** | Agent orchestration; not an agent loop.
475 | 2253 | `tractorjuice/arc-kit` | **REJECT** | Governance harness; not an agent loop.
476 | 2243 | `cogwheel0/conduit` | **REJECT** | Mobile client; interface, not an agent loop.
477 | 2241 | `Mintplex-Labs/vector-admin` | **REJECT** | Vector-DB tool; not an agent loop.
478 | 2220 | `777genius/agent-teams-ai` | **REJECT** | Team-management app; not a framework.
479 | 2208 | `Stack-Cairn/LiveAgent` | **REJECT** | Desktop client; interface, not an agent loop.
480 | 2200 | `kevinluosl/deepbot` | **REJECT** | System AI assistant; not a framework.
481 | 2199 | `Kritt-ai/open-kritt` | **REJECT** | Vulnerability-research tool; single vertical.
482 | 2182 | `Dicklesworthstone/mcp_agent_mail` | **REJECT** | Coordination layer; infrastructure, not an agent loop.
483 | 2178 | `duty1g/x64dbg-mcp-server` | **REJECT** | MCP server; tool, not an agent loop.
484 | 2159 | `atomicstrata/llm-wiki-compiler` | **REJECT** | Knowledge compiler; tool, not an agent loop.
485 | 2150 | `Orkas-AI/Orkas` | **REJECT** | Desktop app; interface, not an agent loop.
486 | 2146 | `satellitecomponent/Neurite` | **REJECT** | Mind-mapping; not an agent loop.
487 | 2135 | `OpenVidu/openvidu` | **REJECT** | Video platform; not an agent loop.
488 | 2118 | `apioo/fusio` | **REJECT** | API management; not an agent loop.
489 | 2108 | `future-agi/future-agi` | **REJECT** | Evaluation platform; not an agent loop.
490 | 2107 | `LetsFG/LetsFG` | **REJECT** | Travel search/booking; single vertical.
491 | 2105 | `4thfever/cultivation-world-simulator` | **REJECT** | World simulator; game, not an agent loop.
492 | 2103 | `Lumiwealth/lumibot` | **REJECT** | Trading agents; single vertical.
493 | 2103 | `agentset-ai/agentset` | **REJECT** | RAG platform; single vertical.
494 | 2097 | `arcsin1/oh-my-ppt` | **REJECT** | Presentation builder; tool, not an agent loop.
495 | 2092 | `eugene1g/agent-safehouse` | **REJECT** | Sandbox; infrastructure, not an agent loop.
496 | 2091 | `voocel/ainovel-cli` | **REJECT** | Novel generation; single vertical.
497 | 2089 | `rynfar/meridian` | **REJECT** | Local API gateway; infrastructure, not an agent loop.
498 | 2086 | `andyrewlee/awesome-agent-orchestrators` | **REJECT** | List, not software.
499 | 2066 | `hyperspaceai/agi` | **REJECT** | Unverifiable AGI claims; not an agent loop.
500 | 2065 | `superglue-ai/superglue` | **REJECT** | Integration builder; tool, not an agent loop.
501 | 2063 | `Anil-matcha/ai-creator-academy` | **REJECT** | Curriculum, not software.
502 | 2061 | `LiuMengxuan04/shushu-internship-tool` | **REJECT** | Job tool; single vertical, not an agent loop.
503 | 2061 | `A9T9/RPA` | **REJECT** | RPA automation; tool, not an agent loop.
504 | 2045 | `iniwap/AIWriteX` | **REJECT** | Writing automation; single vertical, not an agent loop.
505 | 2041 | `memorax-ai/memorax-code` | **REJECT** | Memory plugin; infrastructure, not an agent loop.
506 | 2024 | `MemTensor/memmy-agent` | **INCLUDE** | Personal AI agent with local memory hub.
507 | 1999 | `patterns-ai-core/langchainrb` | **INCLUDE** | Ruby port of LangChain (agent framework).
508 | 1998 | `AntigmaLabs/ante` | **INCLUDE** | Self-contained agent harness.
509 | 1982 | `doobidoo/mcp-memory-service` | **REJECT** | Persistent memory; infrastructure, not an agent loop.
510 | 1968 | `xu-xiang/everything-claude-code-zh` | **REJECT** | Translation/config collection; not an agent loop.
511 | 1945 | `eneskirca/nodeterm` | **REJECT** | Terminal manager; tool, not an agent loop.
512 | 1927 | `MicrosoftDocs/mcp` | **REJECT** | MCP server; tool, not an agent loop.
513 | 1926 | `vstorm-co/full-stack-ai-agent-template` | **REJECT** | App generator template; not an agent loop.
514 | 1919 | `the-open-engine/zeroshot` | **INCLUDE** | Multi-agent coding system (graph of agents).
515 | 1918 | `caramaschiHG/awesome-ai-agents-2026` | **REJECT** | List, not software.
516 | 1909 | `melih-unsal/DemoGPT` | **REJECT** | Agentic-app builder; not an agent loop.
517 | 1875 | `ballred/obsidian-claude-pkm` | **REJECT** | Starter kit; not an agent loop.
518 | 1873 | `agentjido/jido` | **INCLUDE** | Autonomous agent framework for Elixir.
519 | 1866 | `jina-ai/dev-gpt` | **REJECT** | Virtual development team; specific system, not a framework.
520 | 1854 | `timescale/pg-aiguide` | **REJECT** | MCP server; tool, not an agent loop.
521 | 1853 | `Kav-K/GPTDiscord` | **REJECT** | Discord bot; not a framework.
522 | 1849 | `happier-dev/happier` | **REJECT** | Client and orchestrator; not an agent loop.
523 | 1843 | `trpc-group/trpc-agent-go` | **INCLUDE** | Go framework for building production agent systems.
524 | 1841 | `unicodeveloper/globalthreatmap` | **REJECT** | Threat map; not an agent loop.
525 | 1837 | `Dicklesworthstone/pi_agent_rust` | **INCLUDE** | High-performance AI coding agent CLI (Rust).
526 | 1830 | `nimbalyst/nimbalyst` | **REJECT** | Visual workspace; not an agent loop.
527 | 1828 | `OpenAgentPlatform/Dive` | **REJECT** | MCP host desktop app; interface, not an agent loop.
528 | 1826 | `a5c-ai/babysitter` | **REJECT** | Governance for agentic workforces; not an agent loop.
529 | 1818 | `VoltAgent/awesome-ai-agent-papers` | **REJECT** | Papers collection, not software.
530 | 1810 | `open-mercato/open-mercato` | **REJECT** | Framework for CRM/ERP/commerce; single vertical.
531 | 1808 | `phronesis-io/eigenflux` | **REJECT** | Communication protocol; not an agent loop.
532 | 1801 | `Mcp-Brasil/mcp-brasil` | **REJECT** | MCP server; tool, not an agent loop.
533 | 1796 | `Jamailar/Beav` | **REJECT** | Social-media operations; single vertical, not an agent loop.
534 | 1793 | `standardagents/dmux` | **REJECT** | Dev-agent multiplexer; tool, not an agent loop.
535 | 1791 | `onestardao/WFGY` | **REJECT** | Vague; not identifiably an agent loop.
536 | 1764 | `feigeCode/navop` | **REJECT** | Workspace; not an agent loop.
537 | 1764 | `AgentDock/AgentDock` | **REJECT** | Framework retired; not software.
538 | 1750 | `relaticle/relaticle` | **REJECT** | CRM; single vertical, not an agent loop.
539 | 1749 | `lahfir/agent-desktop` | **REJECT** | Computer-use tool; not an agent loop.
540 | 1745 | `iwe-org/iwe` | **REJECT** | Knowledge graph; infrastructure, not an agent loop.
541 | 1743 | `google/adk-java` | **INCLUDE** | Agent Development Kit (Java).
542 | 1732 | `sallowayma-git/IELTS-practice` | **REJECT** | Education system; single vertical, not an agent loop.
543 | 1724 | `101dotxyz/GPTeam` | **REJECT** | Multi-agent simulation; not an agent loop.
544 | 1716 | `mims-harvard/ToolUniverse` | **REJECT** | AI-scientist tool universe; single vertical (science).
545 | 1700 | `fynnfluegge/agtx` | **REJECT** | Development environment; not an agent loop.
546 | 1696 | `lst97/claude-code-sub-agents` | **REJECT** | Subagent collection; not an agent loop.
547 | 1685 | `Lynpoint/CyberVerse` | **REJECT** | Voice-first agent platform; single vertical (voice).
548 | 1679 | `bubbuild/bub` | **INCLUDE** | Tiny agent runtime with plugins.
549 | 1673 | `patoles/agent-flow` | **REJECT** | Visualization; tool, not an agent loop.
550 | 1671 | `e2b-dev/runtime` | **REJECT** | Runtime; infrastructure, not an agent loop.
551 | 1668 | `DataTalksClub/ai-dev-tools-zoomcamp` | **REJECT** | Course, not software.
552 | 1667 | `ghostwright/ghost-os` | **REJECT** | Computer-use infrastructure for agents; not an agent loop.
553 | 1662 | `kubeshop/testkube` | **REJECT** | Testing platform; not an agent loop.
554 | 1659 | `lucasastorian/llmwiki` | **REJECT** | Wiki; not an agent loop.
555 | 1659 | `spec-kitty/spec-kitty` | **REJECT** | Spec-driven development; not an agent loop.
556 | 1654 | `eylonmiz/react-agent` | **REJECT** | React-specific agent; not a general framework.
557 | 1646 | `lucaswalter/n8n-ai-automations` | **REJECT** | Collection, not software.
558 | 1640 | `fetchai/uAgents` | **INCLUDE** | Framework for creating decentralized agents.
559 | 1639 | `codeaholicguy/ai-devkit` | **REJECT** | Control plane; orchestration, not an agent loop.
560 | 1638 | `alchaincyf/huashu-skills` | **REJECT** | Skills directory; not an agent loop.
561 | 1638 | `HumanSignal/Adala` | **REJECT** | Data-labeling agent framework; single vertical.
562 | 1637 | `ariacom/Seal-Report` | **REJECT** | Reporting tool; not an agent loop.
563 | 1636 | `pguso/rag-from-scratch` | **REJECT** | Tutorial, not software.
564 | 1624 | `openchoreo/openchoreo` | **REJECT** | Developer platform; not an agent loop.
565 | 1622 | `uber/ADR` | **REJECT** | Security for agents; not an agent loop.
566 | 1621 | `activeloopai/hivemind` | **REJECT** | Skills from traces; tool, not an agent loop.
567 | 1618 | `ray-r-ren/agent-apprenticeship` | **REJECT** | Ecosystem; not an agent loop.
568 | 1614 | `monid-ai/monid` | **REJECT** | Tool router; infrastructure, not an agent loop.
569 | 1608 | `Kaelio/ktx` | **REJECT** | Context layer; infrastructure, not an agent loop.
570 | 1607 | `actionbook/actionbook` | **REJECT** | Tool; not an agent loop.
571 | 1606 | `869413421/ai-moive-studio` | **REJECT** | Video creation; single vertical, not an agent loop.
572 | 1603 | `DeadWaveWave/opencove` | **REJECT** | Workspace; not an agent loop.
573 | 1595 | `MeetKai/functionary` | **REJECT** | Language model; not an agent framework.
574 | 1589 | `xmanrui/dsh-im` | **REJECT** | IM integration; not an agent loop.
575 | 1583 | `universal-tool-calling-protocol/code-mode` | **REJECT** | Library; not an agent loop.
576 | 1583 | `rivet-dev/agents` | **REJECT** | Durable-process infrastructure; not an agent loop.
577 | 1583 | `CopilotKit/OpenGenerativeUI` | **REJECT** | Generative-UI framework; not an agent loop.
578 | 1579 | `steel-dev/awesome-web-agents` | **REJECT** | List, not software.
579 | 1576 | `kenryu42/cc-safety-net` | **REJECT** | Guard; tool, not an agent loop.
580 | 1563 | `oxylabs/browser-agent-py` | **REJECT** | Browser agent; single vertical.
581 | 1563 | `fim-ai/fim-one` | **REJECT** | Enterprise agent platform; not an agent loop.
582 | 1563 | `Farama-Foundation/chatarena` | **REJECT** | Game environments; not an agent loop.
583 | 1562 | `langwatch/better-agents` | **REJECT** | Standards; not an agent loop.
584 | 1558 | `miscusi-peek/cheatengine-mcp-bridge` | **REJECT** | Bridge; tool, not an agent loop.
585 | 1554 | `agentlas-ai/Agentlas-OS` | **REJECT** | Agent OS; infrastructure, not an agent loop.
586 | 1554 | `Prismer-AI/PrismerCloud` | **REJECT** | Vague; not identifiably an agent loop.
587 | 1553 | `WecoAI/aideml` | **REJECT** | ML-engineering agent; single vertical.
588 | 1542 | `video-db/Director` | **REJECT** | Video-agents framework; single vertical.
589 | 1539 | `fujibee/agmsg` | **REJECT** | Messaging; protocol, not an agent loop.
590 | 1538 | `vanloctech/youwee` | **REJECT** | Downloader; tool, not an agent loop.
591 | 1523 | `plugin87/ux-ui-agent-skills` | **REJECT** | Skills; not an agent loop.
592 | 1512 | `YGYOOO/WorldX` | **REJECT** | World generator; not an agent loop.
593 | 1512 | `memfreeme/memfree` | **REJECT** | Search engine; not an agent loop.
594 | 1507 | `eatmoreduck/boss-zhipin-scraper` | **REJECT** | Scraper; tool, not an agent loop.
595 | 1504 | `imxv/Pretty-mermaid-skills` | **REJECT** | Skill; not an agent loop.
596 | 1494 | `Open-Source-Legal/OpenContracts` | **REJECT** | Document platform; not an agent loop.
597 | 1494 | `dyoshikawa/rulesync` | **REJECT** | CLI tool; not an agent loop.
598 | 1493 | `openonion/connectonion` | **INCLUDE** | Agent CLI harness.
599 | 1482 | `najmuzzaman-mohammad/gawkbot` | **REJECT** | Bot; not a framework.
600 | 1478 | `ghostwright/phantom` | **INCLUDE** | AI co-worker with its own computer (agent).
601 | 1477 | `agent0ai/dox` | **REJECT** | Documentation; not an agent loop.
602 | 1467 | `HexmosTech/git-lrc` | **REJECT** | Code review; tool, not an agent loop.
603 | 1466 | `nixopus/nixopus` | **REJECT** | Infrastructure; not an agent loop.
604 | 1458 | `win4r/ClawTeam-OpenClaw` | **REJECT** | Swarm coordination fork; orchestration, not an agent loop.
605 | 1457 | `veedstudio/open-edit` | **REJECT** | Editing pipeline; not an agent loop.
606 | 1451 | `Paritok-official/paritok-4b-v1` | **REJECT** | Compression gateway; tool, not an agent loop.
607 | 1451 | `farizrahman4u/loopgpt` | **INCLUDE** | Python implementation of OpenCode (agent).
608 | 1449 | `inkeep/agents` | **REJECT** | No-code builder; UI exclusion.
609 | 1444 | `kodustech/kodus-ai` | **REJECT** | Code review; tool, not an agent loop.
610 | 1435 | `Unclecheng-li/AI_Animation` | **REJECT** | Prompts; not an agent loop.
611 | 1435 | `eumemic/ai-legion` | **REJECT** | Agent platform; infrastructure, not an agent loop.
612 | 1428 | `google/adk-js` | **INCLUDE** | Agent Development Kit (TypeScript).
613 | 1423 | `mnemox-ai/tradememory-protocol` | **REJECT** | Memory for trading agents; single vertical, not an agent loop.
614 | 1423 | `preset-io/agor` | **REJECT** | Command center; orchestration, not an agent loop.
615 | 1422 | `Jwuthri/Tracely-ai` | **REJECT** | CI/CD for agents; tool, not an agent loop.
616 | 1420 | `hesamsheikh/octogent` | **REJECT** | Orchestration dashboard; not an agent loop.
617 | 1420 | `mohitagw15856/pm-claude-skills` | **REJECT** | Skills; not an agent loop.
618 | 1418 | `myshell-ai/AIlice` | **INCLUDE** | Fully autonomous general-purpose AI agent.
619 | 1416 | `CloudAI-X/claude-workflow-v2` | **REJECT** | Workflow plugin; not an agent loop.
620 | 1412 | `JoasASantos/NeuroSploit` | **REJECT** | Pentest framework; single vertical (security).
621 | 1407 | `e2b-dev/e2b-cookbook` | **REJECT** | Examples, not software.
622 | 1405 | `razzant/ouroboros` | **REJECT** | Specific self-creating agent; not a framework.
623 | 1398 | `nrslib/takt` | **REJECT** | Coordination topology; not an agent loop.
624 | 1395 | `BitMiracle-AI/Dormice` | **REJECT** | Agent sandboxes; infrastructure, not an agent loop.
625 | 1393 | `m0n0x41d/haft` | **REJECT** | Decisions engine; tool, not an agent loop.
626 | 1386 | `lycorp-jp/sim-use` | **REJECT** | Simulator tool; not an agent loop.
627 | 1385 | `PentesterFlow/agent` | **REJECT** | Offensive-security agent; single vertical.
628 | 1382 | `AnandChowdhary/continuous-claude` | **REJECT** | Loop pattern; not a framework.
629 | 1380 | `tmgthb/Autonomous-Agents` | **REJECT** | Papers, not software.
630 | 1379 | `sipyourdrink-ltd/bernstein` | **REJECT** | Governance framework; not an agent loop.
631 | 1378 | `awslabs/cli-agent-orchestrator` | **REJECT** | Orchestration; not an agent loop.
632 | 1377 | `zjunlp/SkillNet` | **REJECT** | Skills; not an agent loop.
633 | 1371 | `irgolic/AutoPR` | **REJECT** | PR tool; not an agent loop.
634 | 1370 | `firecrawl/open-scouts` | **REJECT** | Web-monitoring platform; single vertical, not an agent loop.
635 | 1366 | `ntegrals/10x` | **INCLUDE** | Open-source coding agent.
636 | 1364 | `heymrun/heym` | **REJECT** | Agentic-systems platform; orchestration, not an agent loop.
637 | 1361 | `amplifthq/opentag` | **REJECT** | Mention tool; not an agent loop.
638 | 1358 | `RefoundAI/lenny-skills` | **REJECT** | Skills; not an agent loop.
639 | 1357 | `Team-Commonly/commonly` | **REJECT** | Chat room; not an agent loop.
640 | 1355 | `Yuan-ManX/ai-game-devtools` | **REJECT** | Game-dev hub; single vertical, not an agent loop.
641 | 1355 | `thetahealth/mirobody` | **REJECT** | Health-data engine; single vertical, not an agent loop.
642 | 1354 | `petergyang/human-review` | **REJECT** | Editor; tool, not an agent loop.
643 | 1352 | `agentplugins/agent-plugins-spec` | **REJECT** | Specification; not an agent loop.
644 | 1347 | `boyang-hu/website-rebuild-skill` | **REJECT** | Skill; not an agent loop.
645 | 1337 | `OpenRaiser/NanoResearch` | **REJECT** | Research assistant; single vertical.
646 | 1327 | `proxysoul/Empryo` | **REJECT** | Engine; not an agent loop.
647 | 1325 | `SanMuzZzZz/LuaN1aoAgent` | **REJECT** | Pentest agent; single vertical (security).
648 | 1324 | `gokayfem/awesome-vlm-architectures` | **REJECT** | Catalog, not software.
649 | 1320 | `jayminwest/overstory` | **REJECT** | Orchestration; not an agent loop.
650 | 1317 | `GanyuanRan/Aegis` | **REJECT** | Tool for coding agents; not an agent loop.
651 | 1315 | `Ataraxy-Labs/weave` | **REJECT** | Merge driver; tool, not an agent loop.
652 | 1314 | `neurogen-dev/NeuroAPI` | **REJECT** | API; infrastructure, not an agent loop.
653 | 1305 | `pierpaolo28/Awesome-FDE-Roadmap` | **REJECT** | Roadmap, not software.
654 | 1305 | `s2b-dev/smart-second-brain` | **REJECT** | Plugin; not an agent loop.
655 | 1304 | `Anil-matcha/awesome-muse-connectors` | **REJECT** | Catalog, not software.
656 | 1302 | `puppyone-ai/puppyone-cloud` | **REJECT** | Context drive; infrastructure, not an agent loop.
657 | 1300 | `ksimback/hermes-ecosystem` | **REJECT** | Decision layer; not an agent loop.
658 | 1299 | `SmythOS/sre` | **REJECT** | Runtime environment; infrastructure, not an agent loop.
659 | 1298 | `Spielewoy/autoprompt-skill` | **REJECT** | Skill; not an agent loop.
660 | 1297 | `Agentshire/Agentshire` | **REJECT** | Plugin; not an agent loop.
661 | 1296 | `gamedev-skills/awesome-gamedev-agent-skills` | **REJECT** | Skills; not an agent loop.
662 | 1295 | `caliber-ai-org/ai-setup` | **REJECT** | Setup sync; tool, not an agent loop.
663 | 1293 | `codefuse-ai/codefuse-chatbot` | **REJECT** | Assistant; not a framework.
664 | 1291 | `mcpjungle/MCPJungle` | **REJECT** | MCP manager; tool, not an agent loop.
665 | 1291 | `pipeboard-co/meta-ads-mcp` | **REJECT** | MCP server; tool, not an agent loop.
666 | 1286 | `pnoker/iot-dc3` | **REJECT** | IoT runtime; single vertical, not an agent loop.
667 | 1284 | `AI-Builder-Club/skills` | **REJECT** | Skills; not an agent loop.
668 | 1278 | `TaxyAI/browser-extension` | **REJECT** | Browser extension; single vertical, not an agent loop.
669 | 1276 | `bug0inc/qa-agent` | **REJECT** | Testing library; single vertical, not an agent loop.
670 | 1265 | `ChesterRa/cccc` | **REJECT** | Coordination; not an agent loop.
671 | 1263 | `conorluddy/ios-simulator-skill` | **REJECT** | Skill; not an agent loop.
672 | 1262 | `OpenPetsHQ/openpets` | **REJECT** | Desktop pets; not an agent loop.
673 | 1261 | `AgenticHealthAI/Awesome-AI-Agents-for-Healthcare` | **REJECT** | Papers; not software.
674 | 1257 | `2akouwu/reverify` | **REJECT** | Verification tool; not an agent loop.
675 | 1255 | `huytieu/COG-second-brain` | **REJECT** | Closed-source; excluded by rule.
676 | 1254 | `0xranx/OpenContext` | **REJECT** | Context store; infrastructure, not an agent loop.
677 | 1247 | `sums001/Windows-Copilot-API` | **REJECT** | API; not an agent loop.
678 | 1244 | `tintinweb/pi-subagents` | **REJECT** | Orchestration; not an agent loop.
679 | 1240 | `Clearailhc/clearai-dsh` | **REJECT** | Plugin; not an agent loop.
680 | 1240 | `hashgraph-online/standards-sdk` | **REJECT** | SDK; not an agent loop.
681 | 1237 | `dariubs/awesome-workflow-automation` | **REJECT** | List, not software.
682 | 1235 | `michaelshimeles/skills` | **REJECT** | Skills; not an agent loop.
683 | 1234 | `hoangnb24/repository-harness` | **REJECT** | Workspace preparer; tool, not an agent loop.
684 | 1229 | `e2b-dev/awesome-ai-sdks` [ALIAS] | **REJECT** | Database; not an agent loop.
685 | 1229 | `e2b-dev/awesome-sdks-for-ai-agents` | **REJECT** | Database; not an agent loop.
686 | 1223 | `pashov/skills` | **REJECT** | Skills; not an agent loop.
687 | 1214 | `Spark-To-Paper-Skills/paperjury` | **REJECT** | Skill; not an agent loop.
688 | 1211 | `kalil0321/reverse-api-engineer` | **REJECT** | API-generation agent; single vertical.
689 | 1208 | `l0ng-ai/tty7` | **REJECT** | Terminal; not an agent loop.
690 | 1208 | `webbrain-one/webbrain` | **REJECT** | Browser agent; single vertical.
691 | 1208 | `browserable/browserable` | **REJECT** | Browser automation; single vertical, not an agent loop.
692 | 1207 | `brycewang-stanford/Awesome-Journal-Skills` | **REJECT** | Skill packs; not an agent loop.
693 | 1206 | `i365dev/free4chat` | **REJECT** | Chat rooms; not an agent loop.
694 | 1203 | `mikehasa/golive-skill` | **REJECT** | Skill; not an agent loop.
695 | 1200 | `polterguy/magic` | **REJECT** | App builder; not an agent loop.
696 | 1198 | `TrafficGuard/typedai` | **REJECT** | AI platform; not an agent loop.
697 | 1193 | `Gentleman-Programming/gentle-shell` | **INCLUDE** | Pi-native coding-agent harness.
698 | 1192 | `matthiasn/lotti` | **REJECT** | Logbook; not an agent loop.
699 | 1191 | `alookai/alook` | **REJECT** | Rooms; not an agent loop.
700 | 1190 | `volcengine/SearchCLI` | **REJECT** | CLI; tool, not an agent loop.
701 | 1189 | `oceanbase/powercontext` | **REJECT** | Memory; infrastructure, not an agent loop.
702 | 1188 | `pskrunner14/trading-bot` | **REJECT** | Stock-trading bot; single vertical.
703 | 1187 | `Chorus-AIDLC/Chorus` | **INCLUDE** | Agent harness for AI-human collaboration.
704 | 1186 | `Ido-Levi/Hephaestus` | **INCLUDE** | Semi-structured agentic framework.
705 | 1186 | `AltanS/collie` | **REJECT** | Mobile client for Herdr; interface, not an agent loop.
706 | 1182 | `zjunlp/LightMem` | **REJECT** | Memory; infrastructure, not an agent loop.
707 | 1182 | `AGenUI/AGenUI` | **REJECT** | UI renderer for agents; interface, not an agent loop.
708 | 1181 | `Azure/agent-landing-zone` | **REJECT** | Agentic RAG accelerator; infrastructure, not an agent loop.
709 | 1173 | `ProxyShard/ShardBrowser` | **REJECT** | Anti-detect browser launcher; tool, single vertical.
710 | 1172 | `kharmanskyi/open-steps` | **REJECT** | Agent skills collection, not an agent loop.
711 | 1169 | `tomasz-tomczyk/crit` | **REJECT** | Feedback-loop tool, not an agent loop.
712 | 1165 | `chubbyguan/chubbyskills` | **REJECT** | Skills collection, not an agent loop.
713 | 1162 | `fcakyon/claude-codex-settings` | **REJECT** | Configs and plugins, not an agent loop.
714 | 1161 | `fancyboi999/ai-engineering-from-scratch-zh` | **REJECT** | Tutorial, not software.
715 | 1159 | `Dicklesworthstone/coding_agent_session_search` | **REJECT** | Session-search tool, not an agent loop.
716 | 1159 | `ferdinandobons/startup-skill` | **REJECT** | Skills, not an agent loop.
717 | 1158 | `uvwt/agentdock` | **REJECT** | MCP runtime; infrastructure, not an agent loop.
718 | 1158 | `awlevin/typesafe-computer-use` | **INCLUDE** | Computer-use agent (screen OCR + action loop).
719 | 1155 | `edenfunf/reelmimic` | **REJECT** | Video-creation tool; single vertical.
720 | 1150 | `ClawBio/ClawBio` | **REJECT** | Skill library, not an agent loop.
721 | 1149 | `fetchai/innovation-lab-examples` | **REJECT** | Examples, not software.
722 | 1148 | `OpenLAIR/dr-claw` | **REJECT** | AI lab app, not an agent loop.
723 | 1146 | `MoizIbnYousaf/ai-agent-skills` | **REJECT** | Skill installer; tool, not an agent loop.
724 | 1144 | `withkynam/vibecode-pro-max-kit` | **INCLUDE** | Spec-driven coding harness.
725 | 1141 | `Anil-matcha/awesome-gpt-6-astra` | **REJECT** | Collection, not software.
726 | 1140 | `DeepMyst/Mysti` | **INCLUDE** | AI coding agent team for VS Code.
727 | 1139 | `XiaoLuoLYG/GOD` | **REJECT** | Control room for agent societies; observability, not an agent loop.
728 | 1136 | `0xsline/awesome-deepseek-harness` | **REJECT** | Ecosystem list, not software.
729 | 1133 | `BagelHole/DevOps-Security-Agent-Skills` | **REJECT** | Skills collection, not an agent loop.
730 | 1132 | `alibaba/skill-up` | **REJECT** | Evaluation tool for skills, not an agent loop.
731 | 1129 | `cognizant-ai-lab/neuro-san-studio` | **REJECT** | Playground, not an agent loop.
732 | 1112 | `ongridio/ongrid` | **REJECT** | Ops agent; single vertical (infrastructure operations).
733 | 1111 | `digitalknk/openclaw-runbook` | **REJECT** | Runbook, not software.
734 | 1111 | `lee-to/ai-factory` | **REJECT** | Setup tool for agents, not an agent loop.
735 | 1107 | `whchien/ai-trader` | **REJECT** | Algorithmic-trading framework; single vertical.
736 | 1101 | `fastcrw/crw` | **REJECT** | Web scraper; single vertical.
737 | 1095 | `bubblelabai/BubbleLab` | **REJECT** | Workflow engine, not an agent loop.
738 | 1095 | `perplexityai/numbat` | **REJECT** | Agent-activity observability; tool, not an agent loop.
739 | 1093 | `garylab/MakeMoneyWithAI` | **REJECT** | List, not software.
740 | 1089 | `VoAPI/VoAPI` | **REJECT** | API gateway; infrastructure, not an agent loop.
741 | 1084 | `andrepimenta/claude-code-chat` | **REJECT** | Chat interface; not an agent loop.
742 | 1084 | `NirDiamant/Agent_Memory_Techniques` | **REJECT** | Tutorials, not software.
743 | 1084 | `autonomous-ai/openharness` | **INCLUDE** | Harness for coding agents.
744 | 1081 | `asklokesh/loki-mode` | **INCLUDE** | Autonomous software factory (agent).
745 | 1080 | `polywrap/evo.ninja` | **INCLUDE** | Versatile generalist agent.
746 | 1078 | `atlassian/atlassian-mcp-server` | **REJECT** | MCP server; tool, not an agent loop.
747 | 1076 | `vstorm-co/pydantic-deepagents` | **INCLUDE** | Self-hosted terminal AI assistant (coding agent).
748 | 1073 | `openops-cloud/openops` | **REJECT** | FinOps platform; not an agent loop.
749 | 1072 | `pikpikcu/airecon` | **REJECT** | Cybersecurity agent; single vertical.
750 | 1067 | `langchain-ai/langsmith-sdk` | **REJECT** | SDK; not an agent loop.
751 | 1065 | `rogue-security/rogue` | **REJECT** | Agent evaluator and red-team platform; tool, not an agent loop.
752 | 1064 | `metaskills/experts` | **REJECT** | Assistants deployer; tool, not an agent loop.
753 | 1064 | `MayDay-wpf/snow-cli` | **INCLUDE** | Agentic coding CLI (terminal agent).
754 | 1062 | `Mininglamp-OSS/octo-server` | **REJECT** | Workplace backend; not an agent loop.
755 | 1061 | `Evokoa/pgGraph` | **REJECT** | Graph database; infrastructure, not an agent loop.
756 | 1060 | `nexscope-ai/eCommerce-Skills` | **REJECT** | Skills, not an agent loop.
757 | 1060 | `stackql/stackql` | **REJECT** | Query tool, not an agent loop.
758 | 1059 | `WecoAI/awesome-autoresearch` | **REJECT** | Curated list, not software.
759 | 1058 | `RyanAlberts/best-of-Agent-Harnesses` | **REJECT** | Ranked list, not software.
760 | 1056 | `lennybase/browsernode` | **REJECT** | Browser automation for agents; single vertical.
761 | 1055 | `mpaepper/llm_agents` | **INCLUDE** | Framework for building LLM-controlled agents.
762 | 1051 | `metauto-ai/GPTSwarm` | **REJECT** | Research on self-improving agents, not a framework.
763 | 1048 | `docker/compose-for-agents` | **REJECT** | Examples collection, not software.
764 | 1046 | `kreneskyp/ix` | **REJECT** | Agent platform; infrastructure, not identifiably an agent loop.
765 | 1044 | `Human-Agent-Society/CORAL` | **REJECT** | Autoresearch project, not a framework.
766 | 1040 | `hardness1020/learn-agent-architecture` | **REJECT** | Tutorial, not software.
767 | 1040 | `hoangsonww/Claude-Code-Agent-Monitor` | **REJECT** | Monitoring dashboard; tool, not an agent loop.
768 | 1035 | `androoAGI/starnet` | **REJECT** | Art project; harness is incidental, not the primary abstraction.
769 | 1033 | `johannesjo/parallel-code` | **REJECT** | Multi-agent runner; tool, not an agent loop.
770 | 1028 | `ZhangJinHaHaHa/AgentLens` | **REJECT** | Agent-trading platform; not an agent loop.
771 | 1027 | `pguso/agents-from-scratch` | **REJECT** | Tutorial, not software.
772 | 1026 | `Agent-Field/SWE-AF` | **INCLUDE** | Autonomous software-engineering agent fleet.
773 | 1025 | `clawkwork/clawk` | **REJECT** | VM for coding agents; infrastructure, not an agent loop.
774 | 1024 | `zabirauf/AutoGPT.js` | **INCLUDE** | Auto-GPT port (agent).
775 | 1023 | `SylphxAI/anymd` | **REJECT** | File converter; tool, not an agent loop.
776 | 1021 | `avinash201199/free-ai-agents-resources` | **REJECT** | Resources collection, not software.
777 | 1016 | `tensorlakeai/tensorlake` | **REJECT** | Serverless runtime; infrastructure, not an agent loop.
778 | 1009 | `bytechefhq/bytechef` | **REJECT** | Workflow-automation platform; UI exclusion.
779 | 1007 | `victordibia/autogen-ui` | **REJECT** | Web UI; interface, not an agent loop.
780 | 1006 | `jarrodwatts/claude-delegator` | **REJECT** | Task delegator; tool, not an agent loop.
781 | 1004 | `ZeroPointRepo/youtube-skills` | **REJECT** | Skills, not an agent loop.
782 | 1002 | `shanraisshan/codex-cli-best-practice` | **REJECT** | Guide, not software.
783 | 1001 | `EvoLinkAI/awesome-openclaw-usecases-moltbook` | **REJECT** | Examples, not software.
784 | 992 | `dzoba/gptrpg` | **REJECT** | Demo/game, not an agent loop.
785 | 957 | `ur-whitelab/chemcrow-public` | **REJECT** | Chemistry agent; single vertical.
786 | 932 | `TIGER-AI-Lab/ClawBench` | **REJECT** | Benchmark, not an agent loop.
787 | 908 | `seanpixel/Teenage-AGI` | **REJECT** | No description; cannot verify agent-loop abstraction.
788 | 897 | `vostride/agent-qa` | **REJECT** | QA agent; single vertical.
789 | 888 | `cuga-project/cuga-agent` | **INCLUDE** | Generalist agent harness.
790 | 872 | `promptise-com/Foundry` | **REJECT** | Foundation layer; infrastructure, not an agent loop.
791 | 850 | `DataBassGit/AgentForge` | **REJECT** | Vague AGI claims; not identifiably an agent loop.
792 | 849 | `Oneirocom/Magick` | **REJECT** | Builder toolkit, not an agent loop.
793 | 827 | `Technion-Kishony-lab/data-to-paper` | **REJECT** | Scientific-research tool; single vertical.
794 | 792 | `pgalko/BambooAI` | **REJECT** | Data analyst; single vertical.
795 | 789 | `usemoss/moss` | **REJECT** | Retrieval layer; infrastructure, not an agent loop.
796 | 731 | `team-openpm/workgpt` | **INCLUDE** | GPT agent framework for API invocation.
797 | 709 | `frontman-ai/frontman` | **REJECT** | Browser-resident agent; single vertical.
798 | 682 | `emrgnt-cmplxty/automata` | **INCLUDE** | Self-coding agent (duplicate entry; counted once).
799 | 682 | `emrgnt-cmplxty/Automata` [ALIAS] | **INCLUDE** | Self-coding agent (duplicate entry; counted once).
800 | 681 | `sandbaseai/sandbase-harness` | **REJECT** | Agent runtime; infrastructure, not an agent loop.
801 | 608 | `fjrdomingues/autopilot` | **REJECT** | Code tool, not an agent loop.
802 | 592 | `yeagerai/yeagerai-agent` | **REJECT** | No description; cannot verify agent-loop abstraction.
803 | 569 | `jbexta/AgentPilot` | **REJECT** | Workflow-automation platform; UI exclusion.
804 | 565 | `rumpfmax/Multi-GPT` | **INCLUDE** | Autonomous agent experiment.
805 | 563 | `YoanWai/agent-manager` | **REJECT** | Agent manager; tool, not an agent loop.
806 | 556 | `giselles-ai/giselle` | **REJECT** | App builder; UI exclusion.
807 | 553 | `composable-models/llm_multiagent_debate` | **REJECT** | Research, not a framework.
808 | 548 | `airtai/fastagency` | **INCLUDE** | Multi-agent workflow framework.
809 | 509 | `madarco/agentbox` | **REJECT** | Multi-agent runner; tool, not an agent loop.
810 | 503 | `LehengTHU/Agent4Rec` | **REJECT** | Research implementation, not a framework.
811 | 492 | `eidolon-ai/eidolon` | **INCLUDE** | Pluggable agent SDK.
812 | 473 | `statelyai/agent` | **INCLUDE** | Library for creating LLM agents.
813 | 460 | `stepanogil/autonomous-hr-chatbot` | **REJECT** | HR agent; single vertical.
814 | 452 | `AutoPackAI/beebot` | **INCLUDE** | Autonomous AI agent.
815 | 424 | `vivekchand/clawmetry` | **REJECT** | Observability; tool, not an agent loop.
816 | 411 | `ennucore/clippy` | **REJECT** | Programming assistant; not an agent loop.
817 | 408 | `genia-dev/GeniA` | **INCLUDE** | Engineering AI team member (agent).
818 | 383 | `nicepkg/gpt-runner` | **REJECT** | Preset runner; tool, not an agent loop.
819 | 350 | `felixbrock/lemon-agent` | **REJECT** | Workflow-automation agent; narrow scope.
820 | 350 | `Charlie85270/Dorothy` | **REJECT** | Unclear; not identifiably an agent loop.
821 | 341 | `mediar-ai/fazm` | **REJECT** | Desktop app, not an agent loop.
822 | 329 | `blob42/Instrukt` | **REJECT** | AI environment; not an agent loop.
823 | 321 | `busabase/busabase` | **REJECT** | Database and workspace; infrastructure, not an agent loop.
824 | 314 | `SaynaAI/sayna` | **REJECT** | Voice layer; infrastructure, not an agent loop.
825 | 300 | `codeintegrity-ai/mutahunter` | **REJECT** | Mutation testing; tool, not an agent loop.
826 | 300 | `zenml-io/kitaru` | **REJECT** | Agent traces; tool, not an agent loop.
827 | 296 | `uilicious/english-compiler` | **REJECT** | Compiler; tool, not an agent loop.
828 | 274 | `Continuum-AI-Corp/OrcaReplay` | **REJECT** | Replay/debug tool, not an agent loop.
829 | 260 | `zapier/sdk` | **REJECT** | SDK/docs; tool, not an agent loop.
830 | 254 | `l33tdawg/sage` | **REJECT** | Vague; not identifiably an agent loop.
831 | 232 | `smartcomputer-ai/agent-os` | **REJECT** | Agent OS; infrastructure, consistent with AIOS exclusion.
832 | 230 | `FOLLGAD/Godmode-GPT` | **REJECT** | App, not an agent loop.
833 | 226 | `krohling/bondai` | **REJECT** | Development tool, not an agent loop.
834 | 220 | `jmagly/aiwg` | **REJECT** | Cognitive architecture; not an agent loop.
835 | 219 | `omega-memory/omega-memory` | **REJECT** | Memory; infrastructure, not an agent loop.
836 | 202 | `autohandai/code-cli` | **INCLUDE** | Self-evolving coding agent CLI.
837 | 195 | `orbi-build/orbi` | **INCLUDE** | Autonomous coding agent (AGPL-3.0, OSI-approved).
838 | 190 | `stoneforge-ai/stoneforge` | **REJECT** | Orchestration dashboard; not an agent loop.
839 | 189 | `topoteretes/PromethAI-Backend` | **INCLUDE** | Framework providing AI agents.
840 | 189 | `iPythoning/b2b-sdr-agent-template` | **REJECT** | Template; single vertical (sales).
841 | 186 | `stackwiseai/stackwise` | **REJECT** | App collection, not an agent loop.
842 | 173 | `daxaur/openpaw` | **REJECT** | Assistant wizard; tool, not an agent loop.
843 | 167 | `CR-Gjx/Suspicion-Agent` | **REJECT** | Game agent; single vertical.
844 | 167 | `oxgeneral/ORCH` | **REJECT** | Orchestrator; tool, not an agent loop.
845 | 166 | `VedankPurohit/LiveRecall` | **REJECT** | Recall alternative; app, not an agent loop.
846 | 160 | `samholt/l2mac` | **REJECT** | Paper framework for automatic programming; not an agent loop.
847 | 156 | `looptroop-ai/LoopTroop` | **REJECT** | Coding orchestration; not an agent loop.
848 | 151 | `x-zheng16/Awesome-Embodied-AI-Safety` | **REJECT** | Survey, not software.
849 | 148 | `Muvon/octomind` | **INCLUDE** | AI coding agent and agent runtime.
850 | 146 | `xeol-io/bumpgen` | **REJECT** | Package-upgrade agent; single vertical.
851 | 146 | `pilot-protocol/pilotprotocol` | **REJECT** | Protocol, not an agent loop.
852 | 144 | `socai-io/jev-social` | **REJECT** | Social-media agent; single vertical.
853 | 141 | `kubestellar/console` | **REJECT** | Kubernetes management; tool, not an agent loop.
854 | 138 | `luoyuctl/agenttrace` | **REJECT** | Audit tool, not an agent loop.
855 | 135 | `ikamensh/kodo` | **REJECT** | Orchestrator; tool, not an agent loop.
856 | 124 | `The-Context-Company/observatory` | **REJECT** | No description; likely observability.
857 | 120 | `Detrol/quorum-cli` | **REJECT** | Debate CLI; not a tool-calling agent loop.
858 | 118 | `markeljan/web3gpt` | **REJECT** | Smart-contract tool; single vertical.
859 | 115 | `Necmttn/ax` | **REJECT** | Observability and memory; infrastructure, not an agent loop.
860 | 115 | `zoharbabin/due-diligence-agents` | **REJECT** | Due-diligence agents; single vertical.
861 | 112 | `DrDroidLab/open-index` | **REJECT** | Memory layer; infrastructure, not an agent loop.
862 | 111 | `OktoLabsAI/okto-pulse` | **REJECT** | SDLC workbench; not an agent loop.
863 | 107 | `Zfinix/aster` | **INCLUDE** | Agent harness for software work.
864 | 103 | `RubricLab/maige` | **REJECT** | Workflow infrastructure, not an agent loop.
865 | 101 | `chaitin/baizhi-agent-toolkit` | **REJECT** | No description; cannot verify agent-loop abstraction.
866 | 94 | `PersonalJarvis/PersonalJarvis` | **REJECT** | Personal assistant app, not a framework.
867 | 93 | `agentrhq/authsome` | **REJECT** | Credential gateway; infrastructure, not an agent loop.
868 | 91 | `seahyinghang8/blinky` | **REJECT** | Debugging agent; single vertical.
869 | 88 | `Blave-TW/blave-agent` | **REJECT** | Quant infrastructure; not an agent loop.
870 | 88 | `NetMindAI-Open/NarraNexus` | **INCLUDE** | Framework for building nexuses of agents.
871 | 82 | `mczhuge/NLSOM` | **REJECT** | Research concept, not a framework.
872 | 82 | `bkuan001/halo-record` | **REJECT** | Audit trails; tool, not an agent loop.
873 | 79 | `sagentic-ai/sagentic-af` | **INCLUDE** | Agent framework (unified platform).
874 | 76 | `Moresyl/dsh-studio` | **REJECT** | Desktop client for DeepSeek Harness; interface, not an agent loop.
875 | 70 | `gfernandf/agent-skills` | **REJECT** | Runtime for executable cognition; infrastructure, not an agent loop.
876 | 69 | `OktoLabsAI/okto-nexus` | **REJECT** | Coordination hub; infrastructure, not an agent loop.
877 | 68 | `MarlBurroW/hivekeep` | **REJECT** | Platform of personal agents; not an agent loop itself.
878 | 67 | `amirrezasalimi/friday` | **INCLUDE** | Developer assistant (autonomous project creation).
879 | 66 | `ajhous44/cody` | **REJECT** | Coding assistant; not an agent loop.
880 | 66 | `OpenCoven/coven` | **REJECT** | Runtime for project-scoped coding-agent sessions; infrastructure, not an agent loop.
881 | 66 | `taskade/taskade` | **REJECT** | AI-native workspace platform; not an agent loop.
882 | 62 | `zooid-ai/zooid` | **REJECT** | Chat app for collaborating with agents; interface, not an agent loop.
883 | 61 | `saten-private/BabyCommandAGI` | **INCLUDE** | CLI+LLM autonomous agent experiment.
884 | 60 | `TheoLvs/westworld` | **REJECT** | Multi-agent simulation library; not an agent loop.
885 | 56 | `blackwell-systems/gcf` | **REJECT** | Wire format for structured data; not an agent loop.
886 | 54 | `agents-squads/squads-cli` | **REJECT** | CLI for managing agent squads; manager, not an agent loop.
887 | 53 | `pj4533/yourgoal` | **INCLUDE** | Swift implementation of BabyAGI (agent port).
888 | 46 | `yanauto/opus-manager` | **REJECT** | Manager skill; not an agent loop.
889 | 44 | `contextstream/mcp-server` | **REJECT** | Persistent memory; infrastructure, not an agent loop.
890 | 44 | `shleder/vetto` | **REJECT** | OS security boundary and sandbox; infrastructure, not an agent loop.
891 | 42 | `Felo-Inc/memclaw` | **REJECT** | Persistent project memory; infrastructure, not an agent loop.
892 | 41 | `alexk-dev/golemcore-bot` | **REJECT** | Agent platform; not an agent loop itself.
893 | 38 | `sagiyaacoby/TeamHero` | **REJECT** | Agent orchestration; not an agent loop.
894 | 38 | `uizze/uizze` | **REJECT** | UI tool for coding agents; not an agent loop.
895 | 36 | `agentguard-ai/tealtiger` | **REJECT** | Security and cost tracking for agents; tool, not an agent loop.
896 | 33 | `nikoSchoinas/routeweiler-python-sdk` | **REJECT** | Financial OS for agents; infrastructure, not an agent loop.
897 | 31 | `CorellisOrg/Corellis` | **REJECT** | Fleet scaling for OpenClaw; infrastructure, not an agent loop.
898 | 31 | `cgoinglove/thursday` | **INCLUDE** | Team of bots doing work in browser, shell, and files (agent team).
899 | 30 | `ramarlina/agx` | **REJECT** | Team runner for coding agents; not an agent loop.
900 | 29 | `thenaxon/somora_agent` | **INCLUDE** | Personal AI team (agent).
901 | 29 | `pungme/superagent-desktop` | **REJECT** | Desktop home for coding agents; interface, not an agent loop.
902 | 29 | `tale-project/tale` | **REJECT** | Project workspace; not an agent loop.
903 | 27 | `aporthq/aport-agent-guardrails` | **REJECT** | Pre-action authorization; guardrails, not an agent loop.
904 | 27 | `regnull/openbot` | **REJECT** | Platform for running bot teams; not an agent loop itself.
905 | 26 | `mnemoverse/mcp-memory-server` | **REJECT** | Hosted memory; infrastructure, not an agent loop.
906 | 25 | `operantlabs/operant-mcp` | **REJECT** | MCP tool; not an agent loop.
907 | 23 | `Cznorth/winkterm` | **INCLUDE** | AI terminal where the AI types commands (terminal agent).
908 | 21 | `CogitoForge-AI/cogito-studio` | **REJECT** | Workspace AI; not an agent loop.
909 | 21 | `ZiwayZhao/agent-coworker` | **REJECT** | P2P collaboration protocol; not an agent loop.
910 | 20 | `sabir-gbs/the-polyglot-protocol` | **REJECT** | Protocol, not an agent loop.
911 | 19 | `HMAKT99/AKF` | **REJECT** | Trust metadata; not an agent loop.
912 | 19 | `yanghao1143/rust-norion` | **REJECT** | Self-evolving LLM runtime; infrastructure, not an agent loop.
913 | 19 | `Djtony707/TITAN` | **REJECT** | AI operating system; infrastructure, not an agent loop.
914 | 18 | `fresh-claw/hermes-zh-cn` | **REJECT** | Language pack for Hermes Agent; not an agent loop.
915 | 18 | `TerminallyLazy/Tree-Ring-Memory` | **REJECT** | Memory lifecycle; infrastructure, not an agent loop.
916 | 17 | `hivemoot/hivemoot` | **INCLUDE** | Framework for AI agent teams building software.
917 | 16 | `remembra-ai/remembra` | **REJECT** | Session handoffs; tool, not an agent loop.
918 | 15 | `1420079678-ctrl/agent-body` | **REJECT** | Token optimization for DeepSeek Harness; tool, not an agent loop.
919 | 15 | `BuyWhere/buywhere-mcp` | **REJECT** | MCP server; tool, not an agent loop.
920 | 15 | `Open-Twin/opentwins` | **REJECT** | Digital twins for social platforms; single vertical.
921 | 15 | `sidclawhq/platform` | **REJECT** | Approval and accountability layer; infrastructure, not an agent loop.
922 | 14 | `CorvinLabs/CorvinOS` | **REJECT** | Agentic OS; infrastructure, not an agent loop.
923 | 13 | `agentweave/cortex` | **REJECT** | Chief-of-staff for agents; not an agent loop.
924 | 13 | `flik2002/openclaw-monitor` | **REJECT** | Monitoring dashboard; tool, not an agent loop.
925 | 13 | `ModernOps888/the-forge` | **REJECT** | Code-evolution platform; not an agent loop.
926 | 12 | `allxsmith/bestax` | **REJECT** | React component library; not an agent loop.
927 | 12 | `lucinate-ai/lucinate` | **REJECT** | Terminal chat client; interface, not an agent loop.
928 | 11 | `Strategic-Automation/arachne` | **INCLUDE** | DSPy-native autonomous AI agent runtime.
929 | 11 | `moching-ai-dev/moching` | **INCLUDE** | Digital operator controlling the PC (computer-use agent).
930 | 11 | `juanmanueldaza/n3rv` | **REJECT** | Engineering infrastructure; not an agent loop.
931 | 11 | `Writbase/writbase` | **REJECT** | Task management for agent fleets; not an agent loop.
932 | 10 | `proficientai/js` | **REJECT** | Monorepo; not an agent loop.
933 | 10 | `yagobski/agentleak` | **REJECT** | Privacy testing for agents; tool, not an agent loop.
934 | 10 | `everafterlabs/jes` | **REJECT** | Guardrails for agents; tool, not an agent loop.
935 | 10 | `Prismer-AI/k8s4claw` | **REJECT** | Kubernetes operator; infrastructure, not an agent loop.
936 | 9 | `venkat22022202/black-vault` | **REJECT** | API key firewall; tool, not an agent loop.
937 | 9 | `SKULLFIRE07/cortex-memory` | **REJECT** | Persistent memory; infrastructure, not an agent loop.
938 | 9 | `momenbasel/CryptoGuard` | **REJECT** | Safety layer for crypto; tool, not an agent loop.
939 | 9 | `jarvismaximum-hue/profitplay-starter` | **REJECT** | Prediction-market sandbox; tool, not an agent loop.
940 | 9 | `sunglasses-dev/sunglasses` | **REJECT** | Input firewall; tool, not an agent loop.
941 | 9 | `Upload-Post/upload-post-mcp` | **REJECT** | MCP server; tool, not an agent loop.
942 | 8 | `agent-express-ai/agent-express` | **INCLUDE** | Fast minimalist agentic AI framework (TypeScript).
943 | 8 | `human-pages-ai/humanpages` | **REJECT** | MCP server; tool, not an agent loop.
944 | 8 | `sortlist/overloop-cli` | **REJECT** | No description; cannot verify agent-loop abstraction.
945 | 8 | `trevhud/rote` | **REJECT** | Skill compiler; tool, not an agent loop.
946 | 8 | `happy520ai/unified-ai-system` | **REJECT** | Model routing gateway; infrastructure, not an agent loop.
947 | 7 | `ZeroPointRepo/zillow-skills` | **REJECT** | Skills; not an agent loop.
948 | 6 | `MukundaKatta/agent-stack` | **REJECT** | Reliability stack; tool, not an agent loop.
949 | 6 | `BindBrain/BindAI` | **REJECT** | No description; cannot verify agent-loop abstraction.
950 | 6 | `YugantM/hvtracker` | **REJECT** | Trust registry; tool, not an agent loop.
951 | 6 | `danielyedaniel/jevme` | **INCLUDE** | Voice agent for Mac (talk and it does it).
952 | 6 | `melaya-labs/melaya` | **INCLUDE** | Governed AI agents that do the work.
953 | 6 | `MohammadHijjawi97/since-cutoff` | **REJECT** | API-change finder; tool, not an agent loop.
954 | 5 | `socialrobot-io/agent-kit` | **INCLUDE** | Production-ready AI agents (agent kit).
955 | 5 | `Aigen-Protocol/aigen-protocol` | **REJECT** | Agent economy token; not an agent loop.
956 | 5 | `runcycles/cycles-server` | **REJECT** | Runtime authority server; infrastructure, not an agent loop.
957 | 5 | `HagiCode-org/desktop` | **REJECT** | Desktop app; interface, not an agent loop.
958 | 5 | `rusharlabs/house-party-protocol` | **INCLUDE** | Local harness for agent teams.
959 | 5 | `louis030195/hyperconsciousness` | **REJECT** | Knowledge layer; infrastructure, not an agent loop.
960 | 5 | `solveathome/platform` | **INCLUDE** | MIT framework for a swarm of AI agents.
961 | 5 | `echennells/sparkbtcbot` | **REJECT** | Agent skill; not an agent loop.
962 | 4 | `islomkhon/CerebrumKit` | **REJECT** | Starter kit; not an agent loop.
963 | 4 | `benjaminLedel/covey` | **REJECT** | Platform running agents like employees; not an agent loop itself.
964 | 4 | `posteverywhere/mcp` | **REJECT** | MCP server; tool, not an agent loop.
965 | 4 | `HNF-FRN/Reel-watcher-telegram-Agent` | **REJECT** | Reel-watching bot; single vertical.
966 | 3 | `Deesmo/Arch-AI-Tools` | **REJECT** | API tools; tool, not an agent loop.
967 | 3 | `PramodDutta/browserbash` | **REJECT** | No description; likely browser tool, cannot verify.
968 | 3 | `skeptrunedev/call4me` | **REJECT** | Phone-call tool; not an agent loop.
969 | 3 | `samirasadov28-code/PolyMind` | **REJECT** | No description; cannot verify agent-loop abstraction.
970 | 3 | `Prismfy/prismfy-wizard` | **REJECT** | Search installer; tool, not an agent loop.
971 | 3 | `HarperZ9/telos` | **REJECT** | Shared workspaces; not an agent loop.
972 | 3 | `simin-yuan/self-auditing-agent` | **INCLUDE** | Self-auditing agent (public audit log).
973 | 3 | `User0856/snaprender-integrations` | **REJECT** | Integrations; tool, not an agent loop.
974 | 2 | `bill10/agent-007` | **REJECT** | Vague; not identifiably an agent loop.
975 | 2 | `Ace-li521/agent-platform` | **REJECT** | Multi-agent collaboration platform; not an agent loop itself.
976 | 2 | `alexfleetcommander/agent-trust-stack-mcp` | **REJECT** | MCP server; tool, not an agent loop.
977 | 2 | `Virt92/agentfix-oss-scanner` | **REJECT** | Readiness scanner; tool, not an agent loop.
978 | 2 | `vbkotecha/agentservices-api` | **REJECT** | Premium APIs; tool, not an agent loop.
979 | 2 | `vinaybhosle/agentstamp` | **REJECT** | Trust verification; tool, not an agent loop.
980 | 2 | `maxfain/basedagents` | **REJECT** | Task marketplace; not an agent loop.
981 | 2 | `azeemkafridi/bulkpublish-api` | **REJECT** | Publishing API; tool, not an agent loop.
982 | 2 | `Ceki-me/mcp-server` | **REJECT** | Browser rental; tool, not an agent loop.
983 | 2 | `Ceki-me/python-sdk` | **REJECT** | SDK for browser rental; tool, not an agent loop.
984 | 2 | `foklepoint/court-rules-mcp` | **REJECT** | Court-rules data; single vertical, not an agent loop.
985 | 2 | `vakandi/EliaAgent` | **INCLUDE** | AI Agent System for macOS.
986 | 2 | `synergenius-fw/flow-weaver` | **REJECT** | Workflow compiler; tool, not an agent loop.
987 | 2 | `JesseGdotIO/hermesplant-mcp-server` | **REJECT** | MCP bridge; tool, not an agent loop.
988 | 2 | `douglasborthwick-crypto/mcp-server-insumer` | **REJECT** | MCP server; tool, not an agent loop.
989 | 2 | `sortlist/max-cli` | **REJECT** | No description; cannot verify agent-loop abstraction.
990 | 2 | `parkain707/nexus-agent` | **INCLUDE** | Autonomous AI engineering agent.
991 | 2 | `arian-gogani/nobulex-registry` | **REJECT** | Prototype; not an agent loop.
992 | 2 | `ivoshemi-sys/oixa-protocol` | **REJECT** | Protocol; not an agent loop.
993 | 2 | `rafsilva85/skillflow-mcp-server` | **REJECT** | MCP server; tool, not an agent loop.
994 | 2 | `sksareen/smartipedia` | **REJECT** | Encyclopedia for agents; data, not an agent loop.
995 | 2 | `baronmuh/synapse-messenger` | **REJECT** | Agent messaging; protocol, not an agent loop.
996 | 2 | `100monkeys-ai/zaru-cli` | **REJECT** | No description; cannot verify agent-loop abstraction.
997 | 1 | `TheoLvs/westworldjs` | **REJECT** | Multi-agent simulation; not an agent loop.
998 | 1 | `nicofains1/agentwatch` | **REJECT** | Multi-agent observability; tool, not an agent loop.
999 | 1 | `dann26parr69/aifordatabase-mcp` | **REJECT** | MCP server; tool, not an agent loop.
1000 | 1 | `NavikkumarModi/AIActGuard` | **REJECT** | No description; cannot verify agent-loop abstraction.
1001 | 1 | `Ceki-me/js-sdk` | **REJECT** | SDK for browser rental; tool, not an agent loop.
1002 | 1 | `paperandbeyond23-gif/edgrapi-skills` | **REJECT** | Government-data MCP server; single vertical, not an agent loop.
1003 | 1 | `Mafengwo292/evo-ai` | **REJECT** | Self-evolving language model network; not an agent loop.
1004 | 1 | `douglasborthwick-crypto/langchain-insumer` | **REJECT** | LangChain toolkit; tool, not an agent loop.
1005 | 1 | `Acekorneya/POK-Agent` | **INCLUDE** | Windows computer-use AI agent.
1006 | 1 | `0000F8/salt-mcp` | **REJECT** | MCP server; tool, not an agent loop.
1007 | 1 | `satohubai/sato-hub-skill` | **REJECT** | Skill; not an agent loop.
1008 | 1 | `sonz-ai/sonzai-go` | **REJECT** | No description; cannot verify agent-loop abstraction.
1009 | 1 | `stipend-sh/stipend` | **REJECT** | USDC wallet for agents; tool, not an agent loop.
1010 | 1 | `samirasadov28-code/storyroute` | **REJECT** | App; not an agent loop.
1011 | 1 | `ItSeemedLikeAGoodIdeaAtTheTime/strata` | **REJECT** | Game for AI agents; not an agent loop.
1012 | 1 | `nybarius/SVRF` | **REJECT** | Merge queue for agent swarms; tool, not an agent loop.
1013 | 1 | `ifyoubuildit/the-agentic-leaderboard-data` | **REJECT** | Data mirror; not an agent loop.
1014 | 1 | `Bengtsson78/genesis-accord-standard` | **REJECT** | Standard; not an agent loop.
1015 | 1 | `xmacna/funcionario-digital-agentget` | **REJECT** | Instructions; not an agent loop.
1016 | 0 | `sourcegraph/sourcegraph` | **REJECT** | Code search; not an agent loop (0 stars, backfill artifact).
1017 | 0 | `features/preview` | **REJECT** | Not a repository (enumeration backfill artifact).
1018 | 0 | `orgs/community` | **REJECT** | Not a repository (enumeration backfill artifact).
1019 | 0 | `apps/use-tusk` | **REJECT** | Not a repository (enumeration backfill artifact).
1020 | 0 | `empac666/agent-argue-cards` | **REJECT** | Game; not an agent loop.
1021 | 0 | `priors-agents/agent001` | **INCLUDE** | Open-source AI agent with its own wallet.
1022 | 0 | `theNamek/kith` | **REJECT** | Social memory; infrastructure, not an agent loop.
1023 | 0 | `myspecs/claude-plugins` | **REJECT** | Plugin directory; not an agent loop.
