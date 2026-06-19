---
title: "AI Agent Memory Context and RAG Integrity Control Standard"
doc_id: "AIRA-42I"
version: "v1.1"
status: "revised"
category: "AI governance and agent control"
source_docx: "AIRA_42I_AI_Agent_Memory_Context_and_RAG_Integrity_Control_Standard_v1.1_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 42-ai-governance-agent-control
  - revised
  - aira-42i
---



# AI Agent Memory Context and RAG Integrity Control Standard



AIRA

AI-Native Enterprise Platform

AI Agent Memory, Context, and RAG Integrity Control Standard

Source Authority | Retrieval Integrity | RAG Poisoning Defense | Context Provenance | Memory Governance | AVCI Always
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-042I |
| Canonical Filename | 42I-AIRA_AI_Agent_Memory_Context_and_RAG_Integrity_Control_Standard_v1.1_Revised.docx |
| Version | v1.1 - Revised Memory/RAG Integrity, Runtime Evidence, System Builder, and Dynamic Workspace Alignment Update |
| Supersedes | 42I-AIRA_AI_Agent_Memory_Context_and_RAG_Integrity_Control_Standard_v1.0.docx |
| Status | Draft for Architecture, Security, AI Governance, DevSecOps, Knowledge Governance, Data Governance, QA/SDET, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Security Architecture; AI Governance; DevSecOps Lead; Knowledge Steward; Data Governance; Platform Engineering; QA/SDET; SRE / Operations; Internal Audit |
| Primary Parent | 42-AIRA AI Governance and Runtime Control Standard |
| Direct Companions | 01/01B AVCI; 05 Information Nervous System; 13 Knowledge Governance; 21A Knowledge Control Plane; 22A Prompt/Guardrail/Model Alias Registry; 25 Knowledge Access; 26A Data Classification; 31A Observability; 42D-42H and 42J-42O AI Agent Controls |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / AI-Governance / Agent-Memory-RAG-Integrity / v1.1/ |

Mandatory Practice Statement

Agent memory, context, retrieval, embeddings, summaries, graph links, semantic caches, RAG outputs, Auto-Learn notes, and conversational summaries are not business authority in AIRA unless they are traced to approved source truth, classified, reviewed, evidence-backed, and retrieval-eligible under policy. Retrieved content is evidence, not instruction. It may be stale, malicious, conflicting, superseded, incomplete, or intentionally poisoned. Therefore all context used by AIRA agents, System Builder, Dynamic Workspace AI panels, MicroFunctions, and Auto-Heal/Auto-Learn/Auto-Improve loops must pass source authority, classification, freshness, conflict, injection, redaction, guardrail, model-route, audit, and evidence checks before material recommendation or action.

No memory item, RAG chunk, vector embedding, retrieval summary, graph edge, AI note, or Auto-Learn output may become authoritative AIRA knowledge without human review, source citation, classification handling, approval, and AVCI evidence.

# Static Table of Contents

1. Executive Summary

2. Purpose, Scope, and Authority

3. Relationship to AIRA Agent and Knowledge Governance

4. Core Principles and Non-Negotiables

5. Source Authority and Knowledge Tier Model

6. Memory, Context, and Retrieval Taxonomy

7. Threat Model and Abuse Cases

8. Control Plane Architecture

9. Memory Lifecycle and State Model

10. Retrieval Eligibility and Context Assembly

11. RAG Poisoning Detection and Quarantine

12. Index Build, Rebuild, and Validation Controls

13. Memory Write and Auto-Learn Governance

14. Classification, Model Route, and Redaction Rules

15. Evidence, Audit, and Observability Requirements

16. Testing, Evaluation, Certification, and Resilience Gates

17. Incident Response, Recovery, and Reconciliation

18. RACI, Roadmap, Acceptance Criteria, and AVCI Summary

# 1. Executive Summary

This v1.1 revision strengthens AIRA-DOC-042I as the control standard for agent memory, context assembly, Retrieval-Augmented Generation (RAG), embeddings, summaries, knowledge graph links, semantic caches, retrieval tools, and durable memory writes. It aligns the v1.0 memory/RAG baseline with the updated agent identity, runtime security, autonomy, threat model, Tool/MCP gateway, registry, policy-as-code, Dynamic Workspace, System Builder, DevSecOps evidence, and observability documents.

The key decision remains unchanged: memory and retrieval improve reasoning, but they do not create authority. AIRA authority comes from approved Tier-0 source records, governed Git repositories, approved documents, controlled databases, signed evidence packs, workflow histories, and approved governance records. RAG and memory outputs are derivative and must remain attributable, verifiable, classifiable, and improvable.
| Strategic Outcome | v1.1 Required Treatment |
| --- | --- |
| Source-grounded AI | Every response, recommendation, tool request, or generated artifact using retrieval must link to source_id, source_tier, version/hash, classification, retrieval_decision_id, and evidence_ref. |
| Poisoning resistance | Prompt-injection, indirect injection, stale source, conflicting source, poisoned vector, suspicious metadata, and unauthorized memory are detected, downgraded, blocked, or quarantined. |
| Safe context assembly | Context is least-privilege, purpose-bound, redacted, freshness-checked, conflict-aware, model-route eligible, and policy-approved before it reaches a model. |
| Controlled memory writes | Agents may propose memory only as review-ready candidates; durable memory requires owner, source, classification, expiry, promotion path, and human approval. |
| Evidence reconstruction | Memory/RAG events emit trace, policy decision, retrieval decision, guardrail result, context hash, model route, output reference, and improvement path. |

# 2. Purpose, Scope, and Authority

## 2.1 Purpose

Define how AIRA governs AI agent memory, retrieval, context assembly, embeddings, vector indexes, summaries, knowledge graph edges, and RAG outputs.

Prevent AI agents and System Builder from acting on poisoned, stale, unauthorized, superseded, conflicting, or unclassified context.

Establish source authority, retrieval eligibility, memory lifecycle, quarantine, rebuild, evidence, and incident response controls.

Ensure Dynamic Workspace AI panels, MicroFunction AI steps, Tool/MCP requests, Auto-Learn candidates, and generated artifacts remain source-grounded and reviewable.

## 2.2 Scope
| In Scope | Out of Scope |
| --- | --- |
| Obsidian, LLM Wiki, LightRAG, pgvector, knowledge graph, search indexes, source metadata, embeddings, summaries, retrieval cache, semantic cache, prompt context, agent memory, Auto-Learn candidates, citations, evidence references, and context assembly. | Unreviewed personal chat memory as authority, unmanaged vector databases, uncontrolled model-provider memory, copying full source code into retrieval stores, or allowing RAG output to approve changes. |
| System Builder, Dynamic Workspace AI Assistant Panel, MicroFunction STP-AIR/STP-GRD/STP-AIM steps, Tool/MCP pre-action context, GitNexus summaries, incident analysis, and DevSecOps evidence retrieval. | Replacing Tier-0 source systems, CAB/ARB decisions, policy-as-code, tests, security scans, or human approval with AI retrieval results. |
| DEV, TEST, UAT, STAGING, PROD, DR, and offline evidence stores where retrieval or memory is used for AIRA work. | Use of Restricted or production data in unapproved prompts, embeddings, logs, screenshots, model training, or external retrieval tools. |

## 2.3 Authority and Precedence
| Level | Authority | Role |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security / AI Governance / Data Governance | Final authority for source authority, memory eligibility, Restricted retrieval, production use, exceptions, and incident closure. |
| L1 | AIRA AVCI, Information Nervous System, Knowledge Governance, Security, DevSecOps, Data Classification, Observability | Universal rules for source truth, classification, evidence, security, model routing, retention, and audit. |
| L2 | This 42I Standard | Authority for memory/RAG integrity, retrieval eligibility, source validation, quarantine, rebuild, context assembly, and durable memory writes. |
| L3 | OPA/SBAC, Guardrails, LiteLLM, Knowledge API, Index Pipelines, Registry, CI/CD | Executable enforcement mechanisms. |
| L4 | Retrieval logs, context hashes, index manifests, evidence packs, citations, incident tickets, reviewer approvals | Operational proof and improvement input. |

# 3. Relationship to AIRA Agent and Knowledge Governance
| Source | Relationship to 42I |
| --- | --- |
| 05 Information Nervous System | Defines source tiers, provenance, confidence, evidence retrieval, conflict handling, and AI memory governance. |
| 13 Obsidian and LLM Wiki Knowledge Governance | Defines curated knowledge projection, metadata, retrieval eligibility, and human review expectations. |
| 21A Knowledge Control Plane | Defines the controlled access layer that protects sources, indexes, classifications, and AI assistant retrieval. |
| 25 Knowledge Access and Golden Source | Establishes Git/OpenKM/databases/evidence stores as Tier-0/authoritative and Obsidian/LLM Wiki/indexes as governed derivative layers. |
| 26B Knowledge Automation Pipeline | Defines automated validation, projection, index refresh, quarantine, and freshness-manifest controls. |
| 31A Observability and Evidence | Defines trace/log/metric/audit/evidence correlation for retrieval and AI flows. |
| 42D-42H Agent Controls | Define identity, runtime security, autonomy, threat, and tool gateways that depend on safe context before action. |
| 42J-42N Agent Controls | Define certification, incident response, delegation, supply chain, and policy-as-code enforcement for memory/RAG decisions. |
| 42O Runtime Registry | Defines authoritative registry data for memory source references, retrieval decisions, context assembly, memory writes, and evidence links. |

# 4. Core Principles and Non-Negotiables
| Principle | Mandatory Treatment |
| --- | --- |
| Retrieved content is evidence, not instruction | Instructions inside retrieved documents, tickets, logs, source comments, screenshots, or memories are never executed unless they are part of an approved source, policy, workflow, or human instruction. |
| Tiered source authority | Tier-0 approved records govern over derivative Obsidian notes, summaries, embeddings, semantic caches, and AI-generated explanations. |
| Least-context | Context assembly retrieves only the minimum source snippets required for the approved purpose, classification, role, and model route. |
| Classification before retrieval | No source, chunk, prompt, embedding, summary, or artifact is retrieved, indexed, logged, or routed without classification metadata and handling rules. |
| Conflict-aware generation | Conflicting or superseded sources must be identified and either reconciled or clearly escalated before material recommendation. |
| Quarantine before trust | Suspicious, stale, poisoned, unowned, unclassified, or unauthorized context is quarantined, not silently ignored or promoted. |
| No silent learning | Auto-Learn and memory writes generate candidates only; durable memory requires human review, source evidence, expiry, and promotion approval. |
| Rebuild derivatives | When Tier-0 sources change, derivative summaries, embeddings, graph edges, cached context, and LLM Wiki projections must be invalidated or rebuilt. |
| AVCI always | Every memory and retrieval artifact must have owner, source, classification, evidence, and improvement path. |

# 5. Source Authority and Knowledge Tier Model
| Tier | Examples | Authority Rule | Retrieval Handling |
| --- | --- | --- | --- |
| Tier 0 - Authority | Approved DOCX/PDF standards, Git repositories, OpenKM records, database records, workflow histories, CI evidence, audit stores, signed ADR/CAB records. | Authoritative when current and within scope. | Eligible when user/agent has SBAC, classification, freshness, and source-owner approval. |
| Tier 1 - Governed Projection | Git-managed Obsidian vault, approved Markdown projections, reviewed runbooks, approved evidence summaries. | Derivative but controlled; must trace to Tier-0. | Eligible if projection hash and source hash are current. |
| Tier 2 - Retrieval Index | LLM Wiki, LightRAG, pgvector, graph edges, search index, semantic summaries. | Derivative retrieval support only. | Eligible only through Knowledge API with provenance, freshness, confidence, and redaction checks. |
| Tier 3 - Runtime Cache | Redis/Valkey, semantic cache, temporary prompt context, session memory. | Never authoritative. | Used only for acceleration; invalidated on source, policy, classification, or scope change. |
| Tier 4 - Unreviewed Candidate | AI draft, Auto-Learn candidate, incident note, unreviewed chat summary, developer scratch note. | Not authoritative. | Blocked from production use until reviewed, classified, cited, and promoted. |

# 6. Memory, Context, and Retrieval Taxonomy
| Type | Purpose | Storage / Authority | Control Requirement |
| --- | --- | --- | --- |
| Ephemeral context | Single-run prompt context and retrieved snippets. | Runtime only; no authority. | Trace, context_hash, classification, guardrail result, retention limit. |
| Session memory | Short-lived conversation or task continuity. | Derivative; time-bound. | Owner, expiry, classification, no secrets, no durable promotion without review. |
| Durable agent memory | Approved lessons, preferences, runbook notes, or known constraints. | Registry-backed derivative memory. | Human review, source citation, expiry, recertification, revocation path. |
| RAG source chunk | Source excerpt used for answer or action analysis. | Derived from Tier-0/Tier-1. | source_id, chunk_id, source_hash, chunk_hash, freshness, classification, access check. |
| Embedding/vector record | Semantic retrieval acceleration. | Derivative index. | Embedding lineage, model/version, rebuild trigger, no raw Restricted data unless approved. |
| Knowledge graph edge | Relationship between sources, code, agents, controls, events, and evidence. | Derivative analytical layer. | Edge provenance, confidence, source references, conflict and supersedence checks. |
| Auto-Learn candidate | Proposed improvement from incidents, test failures, or repeated denials. | Draft candidate. | Cannot become approved knowledge until reviewed, tested, classified, and promoted. |

# 7. Threat Model and Abuse Cases
| Threat / Abuse Case | Example | Required Control |
| --- | --- | --- |
| Direct prompt injection | User asks model to ignore policy or reveal secrets. | Input guardrail, instruction hierarchy, classification check, policy decision, safe refusal. |
| Indirect prompt injection | Retrieved document contains hidden instruction to execute a tool or exfiltrate data. | Retrieval guardrail, source parser, instruction stripping, content quarantine, human review. |
| RAG poisoning | Poisoned source, malicious issue comment, compromised wiki page, or vector record influences answer. | Source authority validation, hash verification, anomaly detection, quarantine, rebuild. |
| Stale/superseded source | Older AIRA pack contradicts active register or revised standard. | Freshness manifest, supersedence metadata, conflict detection, 00D reconciliation item. |
| Unauthorized memory persistence | Agent saves unreviewed user data, secret, or unsafe instruction as memory. | Memory write policy, redaction, review gate, expiry, denial tests. |
| Classification leakage | Restricted source enters prompt, log, embedding, screenshot, or model route. | Data classification, redaction, model-route eligibility, forbidden telemetry tests. |
| Context overreach | Agent retrieves more data than needed for task. | Least-context policy, chunk limits, purpose binding, SBAC and ABAC checks. |
| Citation laundering | AI cites weak derivative summary as if it were authoritative. | Citation to source tier and version, confidence score, source hash, reviewer challenge. |
| Index drift | Embeddings or summaries not rebuilt after source update. | Index manifest, source hash comparison, rebuild job, CI/index freshness gate. |
| Memory-to-tool escalation | Poisoned memory leads to unsafe Tool/MCP action. | 42H tool gateway requires retrieval_decision_id, risk tier, OPA/SBAC, dry-run, approval, rollback. |

# 8. Control Plane Architecture

The memory/RAG control plane sits before model invocation and before tool action. It protects source discovery, source retrieval, chunk selection, context assembly, memory write requests, index build/rebuild, and evidence creation. The approved pattern is: source authority -> metadata validation -> classification -> SBAC/OPA -> freshness/conflict check -> injection/poisoning scan -> context assembly -> guardrail -> LiteLLM route -> output evidence -> feedback/improvement path.
| Control Layer | Required Component | Evidence Produced |
| --- | --- | --- |
| Source registry | Source catalog with owner, tier, version/hash, classification, retention, authority, supersedes/superseded-by. | source_ref, source_hash, freshness_status, authority_score. |
| Knowledge API / Retrieval Gateway | Single access path for approved retrieval and context assembly. | retrieval_decision_id, context_hash, access decision, redaction result. |
| Policy and guardrails | OPA/SBAC plus input/retrieval/execution/output guardrails. | policy_decision_id, guardrail_result_id, deny/escalate reason. |
| Index pipeline | Chunker, embedding generator, graph builder, summarizer, quarantine scanner, rebuild runner. | index_manifest_id, chunk_hash, embedding_model_version, rebuild_evidence. |
| Runtime registry | 42O data model for context_source_ref, retrieval_decision, context_assembly, memory_write. | agent_run_id, trace_id, evidence_ref, memory_write_id. |
| Observability and audit | OTel traces, structured logs, audit events, dashboard metrics. | trace, metric, audit_event, dashboard_snapshot. |

# 9. Memory Lifecycle and State Model
| State | Meaning | Allowed Use | Exit / Transition Rule |
| --- | --- | --- | --- |
| PROPOSED | Candidate memory or source discovered. | Not used for protected action. | Move to REVIEW_READY after metadata, classification, and source evidence exist. |
| REVIEW_READY | Candidate prepared for human/owner review. | May be inspected by reviewer. | Approve, reject, quarantine, or request remediation. |
| APPROVED | Reviewed and eligible for limited retrieval. | Retrieve within approved scope and classification. | Expires, superseded, revoked, or recertified. |
| ACTIVE | Currently eligible source/memory/index entry. | May support answer or draft if policy permits. | Monitor for drift, conflicts, source changes, and incidents. |
| STALE | Freshness window exceeded or source changed. | Blocked or downgraded unless explicitly marked historical. | Refresh, rebuild, or archive. |
| CONFLICTED | Conflicts with higher-authority or peer source. | Escalate; may cite conflict but not silently resolve. | Resolve through register/ADR/TDL/owner review. |
| QUARANTINED | Potentially poisoned, unsafe, unauthorized, or leaked. | Not retrievable except incident/reviewer context. | Remediate, rebuild, reject, or archive. |
| REVOKED / RETIRED | No longer eligible for retrieval. | Blocked; denial evidence retained. | Reinstatement requires approval and denial tests. |

# 10. Retrieval Eligibility and Context Assembly
| Gate | Pass Condition | Fail-Closed Behavior |
| --- | --- | --- |
| Purpose and intent | Task, agent, user, ticket, and requested outcome are known and allowed. | Deny retrieval or ask for clarification. |
| Identity and SBAC | Actor/agent has skill, role, scope, environment, and data access eligibility. | Deny and emit policy evidence. |
| Classification and route | Source classification is allowed for actor, model route, storage, prompt, and evidence path. | Block, redact, downgrade route, or escalate. |
| Source authority | Source tier, owner, version/hash, review state, and supersedence are valid. | Deny, downgrade to historical, or create reconciliation item. |
| Freshness and drift | Source within review cadence and derivative index current. | Block derivative retrieval; force source refresh or rebuild. |
| Conflict detection | No unresolved conflict with governing standard, register, ADR, policy, or security control. | Escalate conflict and cite both sides; do not silently select convenient source. |
| Injection and poisoning scan | Retrieved text and metadata pass prompt-injection and poisoning checks. | Quarantine source/chunk and alert owner/security. |
| Least-context assembly | Only relevant excerpts are included; sensitive fields redacted; context budget controlled. | Reduce, redact, or block context. |

# 11. RAG Poisoning Detection and Quarantine
| Signal | Detection Evidence | Required Action |
| --- | --- | --- |
| Instructional content in source | Patterns such as ignore policy, reveal secret, execute tool, disable guardrail, override previous instruction. | Strip as data, quarantine if suspicious, require reviewer decision before reuse. |
| Unexpected source mutation | Hash change without approved commit, document approval, ticket, or seeder evidence. | Quarantine source and dependent chunks; rebuild only after owner approval. |
| Metadata inconsistency | Missing owner, classification, version, source_ref, retention, or authority tier. | Block retrieval until metadata is corrected. |
| Conflict spike | Multiple sources disagree or retrieval contradicts active register. | Open reconciliation item and downgrade confidence. |
| High-risk content | Secrets, credentials, raw PII, restricted payload, customer documents, or uncontrolled screenshots. | Block, redact, purge from index, preserve incident evidence. |
| Poisoned retrieval behavior | Prompt output changes to unsafe tool action, unsafe recommendation, or hallucinated approval. | Tripwire event; quarantine source/context; rerun certification and guardrail tests. |
| Embedding/index anomaly | Duplicate chunks, stale embedding version, unlinked vector record, suspicious nearest-neighbor cluster. | Disable affected index partition; rebuild from approved sources. |

# 12. Index Build, Rebuild, and Validation Controls

Every index build must produce an index manifest containing source_id, source_hash, source_tier, chunker version, embedding model/version, graph-builder version, build timestamp, owner, classification coverage, secret-scan result, quarantine result, and evidence_ref.

Any source update, classification change, policy change, model-route change, RLS change, security incident, or source-register reconciliation may require derivative rebuild or retrieval invalidation.

Redis/Valkey, vector indexes, graph indexes, summaries, and cached contexts are acceleration layers only. They must never become source of truth.

CI/CD must validate index manifests, deny stale derivative artifacts, and confirm that forbidden fields are not embedded, logged, or exported.
| Build/Rebuild Trigger | Required Validation |
| --- | --- |
| Approved source update | Recompute source hash, affected chunks, summaries, embeddings, graph edges, and retrieval regression tests. |
| Classification or retention change | Re-evaluate route eligibility, redaction, storage, index partition, and purge requirements. |
| Policy or guardrail update | Rerun retrieval eligibility, prompt-injection, redaction, and model-route tests. |
| Memory poisoning incident | Quarantine affected sources, rebuild clean index, run denial tests, preserve forensic chain. |
| New Experience Pack / Dynamic Workspace source | Validate component metadata, MicroFunction/API/event binding, classification, and accessibility/evidence fields. |
| Agent promotion or autonomy increase | Rerun memory/RAG certification tests before trust promotion. |

# 13. Memory Write and Auto-Learn Governance

AIRA allows learning only through a governed candidate loop. Agents may propose a memory, knowledge update, prompt improvement, guardrail improvement, runbook update, test improvement, or source-register reconciliation item. They must not silently persist or promote durable memory.
| Memory Write Type | Who May Propose | Approval Required | Controls |
| --- | --- | --- | --- |
| Ephemeral run note | Agent or System Builder | No durable approval if discarded after run. | Trace, classification, retention, no secrets. |
| Session memory | Approved assistant / workspace panel | Owner or user where policy requires. | TTL, scope, deletion, no Restricted unless approved. |
| Durable agent memory | Agent owner / Knowledge Steward / AI Governance | Human review and knowledge owner approval. | Source citation, expiry, classification, evidence_ref, recertification. |
| Knowledge artifact update | System Builder or Auto-Learn candidate | Maker-checker and source-owner approval. | PR/MR, tests, source links, change log, rollback path. |
| Policy or guardrail update | Security / AI Governance / DevSecOps | Security/AI Governance and CI policy tests. | OPA/guardrail tests, red-team regression, CAB if material. |
| Incident-derived memory | Incident owner / SRE / Security | Postmortem owner and Knowledge Steward. | Forensic evidence, root cause, validation, retention, non-sensitive summary. |

# 14. Classification, Model Route, and Redaction Rules
| Control | Mandatory Rule |
| --- | --- |
| Classification ceiling | Context cannot exceed actor, agent, model route, environment, and evidence-store classification ceiling. |
| Restricted content | Restricted data is blocked by default from external models, embeddings, semantic cache, screenshots, chat transcript, logs, and unapproved retrieval indexes. |
| Prompt redaction | Secrets, raw tokens, raw PII, account numbers, private keys, raw customer documents, and prompt-injection payloads must be redacted, blocked, or quarantined. |
| Model route eligibility | LiteLLM alias and guardrail policy must match classification, purpose, geography, budget, provider risk, and data handling rules. |
| Evidence retention | Memory/RAG evidence must store safe metadata, hashes, decisions, and references; do not store raw sensitive payload unless approved evidence repository allows it. |
| Output citation | Material answers and recommendations must include source references or explain why source-grounding is insufficient. |
| Forbidden telemetry | Do not log raw prompts containing Confidential/Restricted data, embeddings, retrieved sensitive documents, secrets, raw PII, or high-cardinality labels. |

# 15. Evidence, Audit, and Observability Requirements
| Evidence Field | Required Purpose |
| --- | --- |
| agent_id / agent_version_id / agent_run_id | Identify the requesting agent and immutable runtime context. |
| actor_id_hash / owner_id / requester_ref | Attribute who requested, approved, or reviewed retrieval/memory. |
| source_id / source_ref / source_hash / source_tier | Prove source authority and version. |
| chunk_id / chunk_hash / context_hash | Reconstruct exact context used without necessarily storing raw sensitive payload. |
| retrieval_decision_id / policy_decision_id | Prove OPA/SBAC decision and retrieval eligibility. |
| classification / redaction_state / model_route_id | Prove data-handling and route eligibility. |
| guardrail_result_id / injection_scan_result | Prove retrieval and prompt safety checks. |
| conflict_status / freshness_status / quarantine_status | Prove quality of source and derivative artifacts. |
| evidence_ref / trace_id / span_id | Link to evidence pack and runtime trace reconstruction. |
| improvement_ref / reconciliation_item | Ensure gaps become backlog or register items. |
| Metric / KRI | Purpose | Target Direction |
| --- | --- | --- |
| retrieval_denial_rate_by_reason | Detect excessive blocked retrieval, stale source, missing classification, or policy drift. | Explainable trend; investigate spikes. |
| memory_write_approval_rate | Measure candidate quality and reviewer workload. | Stable with low rejection for repeat patterns. |
| poisoned_context_detection_count | Detect direct/indirect injection and poisoning attempts. | Increase detection quality; decrease successful exposure. |
| source_freshness_compliance | Measure derivative rebuild and source review timeliness. | Increase to agreed threshold. |
| unresolved_conflict_count | Detect cross-document, register, and source contradictions. | Decrease; time-bound resolution. |
| context_reconstruction_success_rate | Measure ability to reconstruct answer/action context. | Increase to near 100 percent for protected actions. |
| forbidden_telemetry_findings | Detect sensitive data in logs/prompts/traces/embeddings. | Zero. |
| memory_quarantine_recovery_time | Measure response speed after RAG poisoning or stale-source incident. | Decrease. |

# 16. Testing, Evaluation, Certification, and Resilience Gates
| Test Category | Mandatory Tests |
| --- | --- |
| Source authority | Tier ordering, supersedence, invalid hash, missing owner, missing classification, stale review, and unapproved source denial. |
| Retrieval eligibility | RBAC/SBAC/ABAC, classification ceiling, model-route eligibility, purpose binding, least-context, redaction, and retention tests. |
| Prompt injection | Direct and indirect prompt-injection payloads in documents, tickets, code comments, screenshots, markdown, metadata, and OCR-like text. |
| RAG poisoning | Poisoned chunk, stale embedding, unauthorized index entry, malicious graph edge, and compromised source projection tests. |
| Conflict detection | Current vs superseded documents, duplicate numbering, conflicting standards, stale register, and ADR/CAB override tests. |
| Memory write | Unauthorized durable memory denied; candidate created; reviewer approval required; expiry and deletion verified. |
| Dynamic Workspace / System Builder | AI Assistant panel retrieval, generated artifact evidence, Admin Builder context, Experience Pack metadata, and component policy tests. |
| MicroFunction and tool-action preconditions | STP-AIR/STP-GRD/STP-AIM guardrails and 42H tool requests cannot proceed on unsafe context. |
| Observability | trace_id, retrieval_decision_id, context_hash, guardrail_result, model_route, evidence_ref, and dashboard tests. |
| Resilience | Index unavailable, vector store stale, cache corrupted, source repository down, and rebuild/rollback/restore tests. |

# 17. Incident Response, Recovery, and Reconciliation
| Incident / Finding | Immediate Containment | Recovery Gate |
| --- | --- | --- |
| Memory poisoning suspected | Quarantine source, chunks, embeddings, graph edges, summaries, and cached contexts; disable affected retrieval policy. | Clean rebuild from approved source; denial tests; reviewer approval; evidence preserved. |
| Sensitive data in prompt/index/log | Block route, purge/rotate as applicable, preserve incident evidence, notify Security/Data Governance. | Redaction validated; forbidden telemetry tests pass; retention/disposal confirmed. |
| Stale or conflicting source used | Mark context as conflicted; disable derivative retrieval; open reconciliation item. | Governing source confirmed, derivative rebuilt, citation rules updated. |
| Unauthorized memory write | Suspend memory write path; restrict agent if needed. | Policy fixed, memory removed/quarantined, recertification passed. |
| Retrieval gateway failure | Fail closed for protected actions; allow only safe no-retrieval advisory fallback where policy permits. | Gateway, policy, audit, and evidence path restored and validated. |
| Evidence reconstruction gap | Freeze promotion or incident closure; preserve available logs/traces/evidence. | Reconstruction accepted or exception approved; evidence schema fixed. |

# 18. RACI, Roadmap, Acceptance Criteria, and AVCI Summary

## 18.1 RACI
| Activity | Architecture / IT Head | AI Governance | Security | Knowledge / Data | DevSecOps / Platform | QA/SDET | Internal Audit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Approve memory/RAG standard and exceptions | A | R | R | C | C | C | I |
| Define source authority and metadata | A | C | C | R | C | C | I |
| Implement Knowledge API / retrieval gateway | C | C | C | C | A/R | C | I |
| Define OPA/SBAC and guardrail rules | C | R | A/R | C | R | C | I |
| Operate index build/rebuild/quarantine | C | C | C | A/R | R | C | I |
| Test poisoning, injection, leakage, freshness | C | C | R | C | R | A/R | I |
| Audit retrieval and memory evidence | I | C | C | C | C | C | A/R |

## 18.2 Implementation Roadmap
| Phase | Target Outcome | Exit Criteria |
| --- | --- | --- |
| P0 Baseline | Inventory sources, indexes, memory paths, retrieval tools, and current AI assistant behavior. | Source/register map, classification gaps, and risk backlog approved. |
| P1 Control Plane | Implement source metadata, Knowledge API, OPA/SBAC retrieval decision, guardrails, and evidence schema. | Protected retrieval fails closed and emits evidence. |
| P2 Index Governance | Implement chunking, embedding, graph, summary, freshness manifest, quarantine, rebuild, and regression tests. | Indexes rebuild from approved sources and reject stale/poisoned context. |
| P3 Runtime Integration | Integrate Dynamic Workspace AI panel, System Builder, MicroFunction STP-AIR/STP-GRD/STP-AIM, and 42H tool preconditions. | Protected AI and tool workflows require retrieval_decision_id and context evidence. |
| P4 Assurance | Dashboards, UAT, red-team, incident drill, audit sampling, and Auto-Learn candidate loop. | CAB/ARB receives evidence pack and residual risk statement. |

## 18.3 Acceptance Criteria and Rejection Rules

Every protected memory/RAG retrieval path uses source authority, classification, SBAC/OPA, freshness, conflict, injection, redaction, guardrail, and model-route checks.

No RAG output, memory item, embedding, summary, graph edge, cache, or Auto-Learn candidate is treated as authority without source citation, human review, classification, and evidence.

Dynamic Workspace, System Builder, MicroFunction AI steps, and Tool/MCP pre-action flows cannot proceed on unsafe, stale, unclassified, or unauthorized context.

Index manifests and source freshness evidence are generated through CI/CD and retained in the evidence path.

Forbidden telemetry and prompt-content tests prove that secrets, raw PII, Restricted data, raw embeddings, and raw sensitive prompts are not exposed.

Quarantine, rebuild, denial, rollback, incident, and recovery procedures are tested and auditable.

Internal Audit can sample any protected AI output or tool action and reconstruct sources, context, decisions, classification, evidence, reviewer, and improvement path.

## 18.4 AVCI Compliance Summary
| AVCI Property | How This Standard Satisfies It |
| --- | --- |
| Attributable | Every source, chunk, memory item, retrieval decision, context assembly, model route, guardrail, reviewer, owner, agent, and evidence record has traceable ownership and source reference. |
| Verifiable | Retrieval eligibility, source authority, freshness, conflict, poisoning, redaction, guardrail, CI/CD, testing, incident, and rebuild evidence can be independently verified. |
| Classifiable | All sources, chunks, embeddings, memories, contexts, prompts, outputs, traces, dashboards, and evidence records carry classification and handling rules. |
| Improvable | Rejected retrievals, quarantines, conflicts, stale sources, incidents, test failures, and audit findings create governed backlog, register, prompt, guardrail, policy, index, and runbook improvements. |

