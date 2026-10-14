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
