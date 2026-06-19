---
title: "AI Governance and Runtime Control Standard"
doc_id: "AIRA-42"
version: "v1.2"
status: "revised"
category: "AI governance and agent control"
source_docx: "AIRA_42_AI_Governance_and_Runtime_Control_Standard_v1_2_Review_and_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 42-ai-governance-agent-control
  - revised
  - aira-42
---



# AI Governance and Runtime Control Standard



AIRA AI Governance and Runtime Control Standard

Prompt Standards | Guardrails | LiteLLM Model Routing | Agent Runtime Control | System Builder Governance

Review, Alignment, Simplification, and Revised Standard

Recommended Version: v1.2

Status: Draft for Architecture Review Board / CAB / AI Governance Review

Classification: INTERNAL CONFIDENTIAL

Prepared for: AIRA Software Development, Enterprise Architecture, DevSecOps, Security, QA/SDET, SRE, Platform Engineering, AI Engineering, Data Governance, and Internal Audit Teams

Owner: Solutions Architecture Office / IT Head

Review Date: 16 June 2026

Mandatory Practice Statement

No AI-generated requirement, evidence interpretation, improvement proposal, agent, tool action, environment setup artifact, prompt, guardrail, model route, code, configuration, database change, workflow action, or operational recommendation may become authoritative or production-impacting unless it satisfies AVCI, source authority, classification, guardrails, OPA/SBAC policy, evidence, human approval, observability, and reversibility or compensation requirements. AI assists; AIRA governance decides.

# Document Control
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-042 |
| Document Title | AIRA AI Governance and Runtime Control Standard |
| Recommended Version | v1.2 - Runtime Control, Agent Registry, Evidence, and System Builder Alignment Update |
| Source Document Reviewed | 42-AIRA_AI_Governance_and_Runtime_Control_Standard_v1.1.docx |
| Supersedes | 42-AIRA_AI_Governance_and_Runtime_Control_Standard_v1.1.docx, upon approval |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Architecture Review Board / CAB / AI Governance / Security / DevSecOps Review |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; AI Governance; DevSecOps Lead; Security Architecture; QA/SDET Lead; Platform Engineering; SRE / Operations; Data Governance; Internal Audit |
| Primary Audience | Enterprise Architects; Developers; DevSecOps; Security; QA/SDET; AI Engineers; Platform Engineers; SRE; Product Owners; System Builder owners; AI Agent owners; Internal Audit |
| Source Pack Location | AIRA Word Source Pack 10 of 15 |
| Primary Governing Sources | 01A Enterprise Architecture Principles v1.2 candidate; 01 AVCI v3.2 candidate; 01B v1.2 candidate; 02 Engineering Blueprint v5.2 candidate; 03 Developer Guide v4.2 candidate; 04 Technology Stack v9.2 candidate; 05 Information Nervous System v4.2 candidate; 06 CLAUDE.md Reference v3.2 candidate |
| Key Related AIRA Documents | 07 Skills Framework; 08/08A Unit Testing; 10 through 10E MicroFunction baseline; 11/11A DevSecOps; 17/17A Security; 20 CI/CD Evidence Pack; 22A Prompt/Guardrail/Model Alias/AI Evaluation Registry; 23B Architecture Fitness Functions; 30/30A Change and Reversibility; 31/31A Operations and Observability; 41B System Builder; 42D through 42S AI Agent governance set |
| External Alignment References | NIST AI RMF 1.0; NIST AI 600-1 Generative AI Profile; OWASP Top 10 for LLM Applications 2025; OpenTelemetry GenAI semantic conventions; SLSA v1.2; NIST SSDF; OWASP ASVS; OPA policy-as-code guidance; LiteLLM and NeMo Guardrails implementation position as approved AIRA technology choices |
| Change Summary | Updated the parent AI governance standard from v1.1 to v1.2 to align with the completed AIRA foundation, MicroFunction, DevSecOps, CI/CD evidence, GitNexus, API, database/Flyway, security, operations, observability, architecture fitness, System Builder, and AI Agent governance baselines. Added stronger runtime control model, registry-backed activation, model-route governance, memory/RAG integrity, tool/MCP action gates, autonomy tiers, kill-switch, evidence correlation, runtime toggles, and review queue continuation. |
| Known Reconciliation Item | AIRA source pack contains multiple 42-prefixed documents. This revision recommends reserving AIRA-DOC-042 as the parent AI Governance and Runtime Control Standard and tracking remaining 42-prefix numbering through the canonical register / 00D reconciliation path. |

# Table of Contents Placeholder

Insert a Microsoft Word automatic Table of Contents here before final publication. Recommended setting: show levels 1 to 3. Update all fields after final approval and before distribution.

# 1. Executive Review Summary

The v1.1 source is directionally correct. It establishes AIRA AI governance as a controlled runtime discipline for prompt standards, guardrails, LiteLLM routing, approved-agent invocation, policy-based controls, System Builder governance, and AVCI evidence. It correctly states that AI output cannot become authoritative merely because it is useful or operationally convenient.

The v1.2 revision strengthens the standard so it becomes the parent AI governance control plane for the now-expanded AIRA baseline. The revised document explicitly connects AI runtime control to agent identity, registry-backed lifecycle state, model-route eligibility, guardrail checkpoints, OPA/SBAC decisions, Harness-mediated tools, evidence correlation, GitNexus analysis, DevSecOps gates, kill-switch controls, incident response, and continuous-improvement candidate loops.

# 2. Source and Context Alignment
| Alignment Area | Required Treatment in v1.2 |
| --- | --- |
| 01A / EDP-01 to EDP-20 | AI governance must preserve SOLID, Clean Architecture, DDD, ports/adapters, idempotency, fail-safe behavior, human-in-the-loop, least privilege, separation of duties, observability, policy as code, testability, secure design, resilience, fitness functions, progressive autonomy, reversibility, and AVCI. |
| 05 Information Nervous System / 13 / 21A / 25 / 26B | AI answers and actions must be grounded in approved source authority, retrieval eligibility, classification, freshness, conflict detection, and evidence citations. Obsidian, LLM Wiki, embeddings, caches, and summaries are derivative unless expressly approved. |
| 06 CLAUDE.md / AGENTS.md | Repository-local AI rules must not weaken AIRA standards. AI assistants may draft, review, and recommend but must not bypass repository, CI/CD, CODEOWNERS, or approval controls. |
| 10 through 10E MicroFunction | AI steps are standard governed steps: input rail, retrieval rail, LiteLLM model invocation, execution rail, Harness action, output rail, audit, evidence, and improvement feedback. Direct provider SDKs and tool shortcuts are rejected. |
| 11 / 11A / 20 DevSecOps | Prompt, guardrail, model route, agent, policy, evaluation dataset, tool/MCP, and provisioning changes are engineering artifacts requiring tests, scans, evidence packs, promotion gates, and rollback/deactivation path. |
| 15 / 15A API and Integration | AI-facing APIs, tool contracts, evidence APIs, registry APIs, event contracts, OpenAPI, AsyncAPI, CloudEvents, Avro/JSON schema, outbox, DLQ, and replay must be contract-governed. |
| 16 / 16A / 16B Database and Flyway | AI agent registry, model-route registry, prompt/guardrail metadata, memory/context metadata, evidence tables, RLS, seed data, and runtime config must be Flyway-governed when persisted. |
| 17 / 17A Security | AI identities, services, tool calls, memory access, model routes, secrets, prompts, and outputs must be least-privilege, SBAC/OPA controlled, classified, redacted, audited, and fail-closed. |
| 22A Registry | Prompts, guardrails, LiteLLM aliases, tool-action policies, evaluation datasets, and AI artifact evidence must be registered, versioned, tested, approved, monitored, superseded, and retired. |
| 23B Fitness Functions | AI governance must be enforced by CI/CD checks, policy tests, import bans, registry checks, guardrail tests, evaluation thresholds, architecture gates, and evidence manifest validation. |
| 31 / 31A Operations and Observability | AI runtime calls, agent actions, model routes, guardrail outcomes, policy decisions, evidence references, denials, kill-switches, incidents, and improvements must be reconstructable. |
| 41B System Builder | System Builder may analyze, recommend, generate, validate, and package. It must not approve itself, mutate production directly, bypass policy, or promote output without maker-checker, CI/CD, ARB/CAB, and AVCI evidence. |
| 42D through 42S AI Agent Control Set | The parent standard must anchor identity lifecycle, runtime security, autonomy, threat model, tool/MCP gateway, memory/RAG integrity, red-team certification, incident response, multi-agent delegation, supply chain, policy rules, registry schema, dashboard, UAT, and roadmap controls. |

# 3. Review and Gap Analysis
| Finding Type | Board Decision |
| --- | --- |
| Retain | The v1.1 core rule that AI-generated outputs are not authoritative without AVCI, classification, guardrails, review, evidence, and reversibility. |
| Correct | Standardize AIRA-DOC-042 as the parent AI governance authority and treat other 42-prefixed documents as numbered companions requiring canonical-register reconciliation. |
| Strengthen | Add registry-backed runtime control: agent_id, model_alias, prompt_version, guardrail_profile, tool_manifest, policy_decision_id, trace_id, evidence_ref, human approval state, rollback/disablement path. |
| Strengthen | Make LiteLLM aliases mandatory and prohibit direct model-provider SDK calls from services, scripts, notebooks, agents, and System Builder outputs. |
| Strengthen | Make NeMo or approved guardrail checkpoints mandatory for input, retrieval, execution, and output in controlled AI flows, with fail-closed behavior when guardrails are unavailable. |
| Strengthen | Add explicit AI agent autonomy tiers, tool/MCP action gates, Harness mediation, OPA/SBAC decisions, and human approval obligations. |
| Strengthen | Add memory/RAG integrity controls: source authority, ACL filtering, classification, freshness, conflict detection, poisoning defense, citations, quarantine, and derivative-cache rebuild rules. |
| Strengthen | Add observability and evidence correlation for model calls, prompts, guardrails, retrieval packs, model routes, token/cost metadata where safe, tool actions, approvals, denials, and incidents. |
| Simplify | Separate the standard into practical control families: artifact registry, runtime decision gate, agent lifecycle, tool action, memory/RAG, evaluation, evidence, change/promotion, and incident response. |
| Add | Explicit runtime toggle rule: sampling and diagnostic verbosity may be tuned, but audit, security decisions, policy outcomes, idempotency records, outbox records, agent action evidence, model-route evidence, and critical error evidence must not be disabled. |

# 4. Revised AIRA Standard

## 4.1 Purpose

This standard defines the AIRA-wide governance and runtime control model for artificial intelligence. It governs AI prompts, guardrails, model routes, AI agents, System Builder outputs, tool actions, memory/RAG, retrieval, AI-assisted DevSecOps, AI-generated artifacts, AI evaluations, and AI-produced recommendations across the AIRA platform.

The purpose is to enable useful AI assistance while preventing uncontrolled automation, hidden model access, prompt drift, guardrail bypass, tool-action privilege escalation, untraceable evidence, unsafe memory, data leakage, and production mutation outside governed change control.

## 4.2 Scope
| In Scope | Out of Scope |
| --- | --- |
| Prompt templates, prompt fragments, system instructions, guardrails, LiteLLM aliases, model route policies, evaluation datasets, golden tests, model calls, agent definitions, tool/MCP actions, memory/RAG context, System Builder generated artifacts, AI evidence, and AI-assisted improvement proposals. | Direct provider SDK calls from application code, scripts, notebooks, agents, or services; personal API keys; unregistered prompts; unmanaged agent tools; shadow model routes; direct production mutation; AI approval of its own output; and unreviewed AI outputs as authority. |
| AI usage in development, QA, DevSecOps, security, observability, operations, knowledge management, Dynamic Workspace, MicroFunction runtime, API/eventing, database/Flyway, and System Builder workflows. | Generic AI ethics theory not tied to AIRA controls, evidence, implementation, monitoring, or approval paths. |
| Runtime control gates for identity, classification, retrieval, guardrails, model routes, policy decisions, tool execution, human approval, evidence, rollback, and continuous improvement. | Bypassing CAB/ARB, maker-checker review, OPA/SBAC, LiteLLM, guardrails, Harness, CI/CD, registry governance, audit, or evidence controls. |

## 4.3 Authority and Precedence

1. AIRA-DOC-042 is the parent AI governance and runtime control standard for all AIRA AI usage.

2. 42D through 42S companion documents implement specific sub-controls and must not weaken this parent standard.

3. 22A is the required registry companion for prompt, guardrail, model alias, tool-action policy, and evaluation assets.

4. 17 and 17A govern security, identity, access control, secrets, fail-closed behavior, and classification handling.

5. 11, 11A, 20, 23B, 30, and 30A govern DevSecOps gates, architecture fitness, evidence packs, promotion, rollback, compensation, and change control.

6. 05, 13, 21A, 25, and 26B govern source authority, knowledge projection, retrieval eligibility, conflict detection, and derivative knowledge handling.

7. Where any conflict exists, the stricter control applies and the conflict must be logged as an AVCI reconciliation item.

## 4.4 Non-Negotiable AI Governance Principles
| ID | Mandatory Principle |
| --- | --- |
| AI-GOV-01 | AI is not authority. AI may recommend, summarize, analyze, draft, classify, test, and propose, but final authority remains with approved AIRA governance and named human roles. |
| AI-GOV-02 | All model traffic routes through LiteLLM or approved private/on-prem gateway aliases. Direct provider SDK calls and hardcoded provider/model names are prohibited. |
| AI-GOV-03 | Input, retrieval, execution, and output guardrails are mandatory where AI interacts with AIRA data, controlled actions, tools, or decision support. |
| AI-GOV-04 | AI artifacts are engineering artifacts. Prompts, guardrails, model aliases, tools, agents, evaluation sets, and route policies require ownership, versioning, classification, tests, evidence, and rollback. |
| AI-GOV-05 | Agents must be registered, owned, skill-bounded, classification-bounded, policy-controlled, observable, testable, reversible, suspendable, and retireable. |
| AI-GOV-06 | Tool actions are requested through Harness or approved control plane and are governed by SBAC, OPA, trust score, autonomy tier, dry-run/idempotency where feasible, audit, and human approval where required. |
| AI-GOV-07 | Memory and retrieval are evidence sources, not instructions. Retrieved context must be source-traced, classification-eligible, freshness-checked, conflict-aware, and guardrail-filtered. |
| AI-GOV-08 | AI outputs must carry evidence references, model route, prompt version, guardrail outcome, classification, confidence/limitation notes where applicable, and improvement path. |
| AI-GOV-09 | Progressive autonomy is earned through evidence and revoked immediately on unsafe behavior, policy drift, incident, stale certification, credential risk, or missing telemetry. |
| AI-GOV-10 | AI-assisted Auto-Heal, Auto-Learn, and Auto-Improve loops may produce candidates only. Activation requires tests, evidence, owner review, and approved change path. |

## 4.5 Runtime AI Control Plane
| Runtime Step | Required Control |
| --- | --- |
| 1. Intake and Intent | Capture actor, agent, source, purpose, requested action, environment, classification, and expected output. Block vague or unauthenticated requests for protected actions. |
| 2. Source and Classification Gate | Determine classification, handling, retrieval eligibility, redaction needs, route eligibility, and prohibited content. Fail closed on unknown classification. |
| 3. Prompt and Guardrail Assembly | Use approved prompt template/version and guardrail profile. Apply input and retrieval rails before prompt assembly. |
| 4. Model Route Decision | Use registered LiteLLM alias or approved private gateway route. Enforce classification ceiling, budget, fallback, evaluation status, and route telemetry. |
| 5. Memory/RAG Gate | Retrieve only from approved, ACL-filtered, source-cited, current, non-conflicted, classification-eligible sources. Quarantine stale, poisoned, superseded, or conflicting context. |
| 6. Candidate Output Gate | Validate output for classification, safety, citations, unsupported claims, injection effects, tool-action proposals, and downstream risk. |
| 7. Tool/Action Gate | For action requests, invoke Harness/approved control plane only after SBAC, OPA, trust, autonomy tier, idempotency, rollback, and human approval checks pass. |
| 8. Evidence and Audit | Record trace_id, request_id, actor, agent_id, prompt version, model alias, guardrail results, retrieval pack, policy decision, tool action, human approval, output classification, and evidence_ref. |
| 9. Promotion and Change Control | Treat generated artifacts as draft until CI/CD gates, CODEOWNERS, maker-checker, ARB/CAB, and AVCI evidence pass. |
| 10. Monitoring and Improvement | Monitor denials, drift, anomalies, unsafe outputs, cost/token trends, incidents, evaluation failures, and improvement proposals. |

## 4.6 AI Artifact Registry and Lifecycle
| Lifecycle State | Required Treatment |
| --- | --- |
| DRAFT | Created in branch or controlled sandbox. Must have owner, purpose, non-goals, classification ceiling, source references, test intent, and rollback candidate. |
| REVIEW | Reviewed by human owner, Security/AI Governance where applicable, and affected domain owners. Must pass classification and source-authority checks. |
| EVALUATED | Golden tests, adversarial tests, guardrail tests, route tests, policy tests, and regression checks executed. Results are retained as evidence. |
| APPROVED | Approved by required maker-checker path. CAB/ARB required for production-impacting, Restricted, high-risk, model-route, tool, or agent activation. |
| ACTIVE | Enabled through registry-controlled activation. Runtime telemetry, evidence, monitoring, and rollback/disablement path are active. |
| SUPERSEDED | Replaced by newer approved version. Not default eligible except for historical review or rollback. |
| SUSPENDED | Blocked due to incident, stale evaluation, unsafe behavior, expired approval, credential issue, or missing evidence. |
| RETIRED | Deactivated, credentials revoked, registry updated, evidence retained, and knowledge projections marked superseded. |

## 4.7 Model Routing and Guardrail Requirements
| Requirement | Mandatory Rule |
| --- | --- |
| LiteLLM alias only | Services, scripts, notebooks, agents, and MicroFunctions must call approved aliases. Provider names, model names, API keys, and fallback logic must not be embedded in application code. |
| Classification ceiling | Each alias has classification ceiling, allowed use cases, provider route, fallback route, budget policy, guardrail profile, and evaluation profile. |
| Four guardrail checkpoints | Input, Retrieval, Execution, and Output guardrails are mandatory for controlled AI flows. Missing guardrail result blocks protected action. |
| Evaluation evidence | Model route activation requires golden dataset result, adversarial result, safety result, regression threshold, rollback version, and owner approval. |
| Telemetry | Every material model call must capture route, alias, prompt version, guardrail result, retrieval pack, actor/agent, classification, output disposition, trace_id, and evidence_ref. |
| Fallback rule | Fallback must not lower classification controls, bypass private-route requirements, omit guardrails, or hide provider change from audit. |

## 4.8 AI Agent Governance and Progressive Autonomy
| Autonomy Tier | Default AIRA Treatment |
| --- | --- |
| T0 Advisory Only | Explain, summarize, classify, draft options. No mutation. Allowed with source, classification, and evidence controls. |
| T1 Read-Only Analysis | Read approved sources, logs, code, tickets, or evidence. Requires SBAC read skill, retrieval eligibility, and audit. |
| T2 Candidate Artifact Generation | Generate draft code, tests, policies, config, prompts, runbooks, diagrams, or documents in sandbox/branch. Requires PR/MR evidence before use. |
| T3 Tool Action Request | Request tool action through Harness/MCP gateway. Requires tool manifest, OPA/SBAC, risk tier, dry-run where feasible, and human approval where required. |
| T4 Limited Delegated Reversible Action | Low-risk, scoped, reversible, time-bound action after certification. Requires telemetry, kill-switch, owner approval, rollback, and active monitoring. |
| T5 Human-Controlled / Prohibited Autonomy | Production identity/secrets, destructive/irreversible changes, financial/legal/security policy/CAB decisions, privileged unlocks, and production mutation remain human-controlled or blocked. |

## 4.9 Tool, MCP, and Action Authorization

1. Every tool, MCP server, connector, API action, CLI script, workflow action, CI action, database action, Kubernetes action, Git action, and provisioning action must have a registered manifest before agent use.

2. Tool manifests must define owner, purpose, environment, allowed actions, target systems, classification ceiling, SBAC skills, OPA policy reference, required approvals, idempotency behavior, dry-run option, audit fields, rollback/disablement path, and expiry/review date.

3. Agents must not receive direct Git, CI/CD, Kubernetes, database, workflow, model-provider, or production credentials. Harness or approved control planes mediate actions.

4. Mutating tool actions must be idempotent or explicitly protected against duplicates, retries, and replays. Rollback, compensation, deactivation, or forward-fix must be defined.

5. High-risk, production-impacting, Restricted-data, destructive, low-confidence, or policy-exception actions require named human approval and separation of duties.

## 4.10 Memory, Context, and RAG Integrity
| Control | Mandatory Requirement |
| --- | --- |
| Source authority | Context must trace to Tier-0 or approved derivative sources. AI-generated summaries, embeddings, caches, and LLM Wiki notes are not authority unless linked to approved source and review state. |
| Retrieval eligibility | Default retrieval excludes drafts, stale, superseded, unclassified, conflicted, quarantined, Restricted-without-route, or unsafe content. |
| ACL and classification | Retrieval applies actor, tenant, role, skill, environment, data classification, and purpose before context leaves the retrieval layer. |
| Poisoning defense | Prompt injection, context poisoning, malicious documents, tool-instruction injection, false citations, and conflicting evidence must be detected or escalated. |
| Memory writes | Persistent memory writes require purpose, source, classification, retention, owner, evidence, approval rule, and deletion/quarantine path. |
| Rebuildability | Embeddings, caches, graph edges, summaries, and retrieval indexes must be rebuildable from authoritative sources and must not become source of truth. |

## 4.11 Observability, Evidence, and Runtime Toggle Rules
| Requirement | Mandatory Treatment |
| --- | --- |
| Required telemetry | Trace, metric, structured log, audit event, policy decision, guardrail result, model route event, tool action event, evidence_ref, and dashboard signal for material AI flows. |
| Required correlation | actor_id, actor_type, agent_id, agent_version, prompt_id, prompt_version, model_alias, route_policy, guardrail_profile, retrieval_pack_id, policy_decision_id, tool_action_id, trace_id, request_id, classification, output disposition, human approval state. |
| Forbidden telemetry | Passwords, tokens, secrets, private keys, raw JWTs, raw PII, raw customer documents, sensitive payloads, embeddings containing Restricted content, and unredacted prompts containing Confidential/Restricted content. |
| Runtime toggles | Diagnostic verbosity, trace sampling, and debug logs may be adjusted to manage performance only through approved runtime configuration. |
| Non-disableable evidence | Audit events, security decisions, policy outcomes, agent action evidence, model-route evidence, guardrail results, idempotency records, outbox records, denials, kill-switch events, and critical error evidence must not be disabled. |
| Incident reconstruction | AIRA must reconstruct who or what invoked AI, what sources were retrieved, which route was used, which guardrails ran, what policy decided, which action was requested, who approved, what happened, and how it was reversed or improved. |

## 4.12 System Builder AI Governance
| System Builder Rule | Treatment |
| --- | --- |
| Allowed | Intake requirements, analyze evidence, draft designs, generate candidate code/config/tests/contracts/migrations/policies/prompts/runbooks, propose AI agents, prepare DevSecOps provisioning plans, and assemble evidence packs. |
| Required | Every output must include intake ID, owner, classification, source references, affected domains, design-principle impact, tests, scans, policy results, evidence, rollback/compensation path, and human checker. |
| Prohibited | Approve its own work, mutate production, bypass OPA/SBAC, bypass guardrails, invoke unapproved tools, install unapproved technologies, create uncontrolled agents, alter production data, rotate production secrets, merge PRs, or promote changes outside CAB/ARB path. |
| Evidence | System Builder run ID, prompt/template version, retrieved sources, model route, guardrail outcome, generated artifacts, validation results, reviewer decisions, PR/MR, CI/CD evidence, and post-promotion monitoring reference. |

## 4.13 DevSecOps, Fitness, and Evaluation Gates
| Gate Area | Required Checks |
| --- | --- |
| Prompt/guardrail/model route | Registry validation, version check, classification ceiling, guardrail tests, golden dataset, adversarial tests, rollback version, reviewer approval. |
| AI agent | Identity card, owner, purpose, non-goals, tool scope, memory policy, route policy, trust tier, autonomy tier, threat model, red-team evidence, kill-switch, retirement plan. |
| Tool/MCP action | Manifest validation, SBAC skill, OPA decision, dry-run/idempotency, approval, audit, rollback/disablement, evidence_ref. |
| Generated code/config | Architecture fitness, SAST/SCA/secrets, unit/component/contract/security tests, GitNexus impact, evidence pack, human review. |
| Database and registry | Flyway-only migration, RLS/tenant tests, clean-migrate, schema compatibility, drift detection, rollback/forward-fix evidence. |
| Runtime activation | CAB/ARB where required, signed/pinned artifacts, monitoring, dashboards, alerts, rollback/deactivation, incident/runbook, owner and support model. |

## 4.14 Change, Reversibility, Kill-Switch, and Incident Rules

1. AI artifacts must have rollback, supersedence, quarantine, deactivation, or retirement path before activation.

2. Model-route and guardrail changes must support immediate rollback to prior approved route/profile and re-run evaluation tests.

3. Agent activation requires kill-switch, suspension, credential revocation, tool-scope removal, memory quarantine, and incident evidence path.

4. Unsafe AI behavior triggers downgrade, route disablement, output quarantine, agent suspension, incident record, RCA, and recertification before reactivation.

5. Auto-Heal, Auto-Learn, and Auto-Improve may propose remediation, but must not activate without tests, evidence, approval, and change control.

## 4.15 Prohibited Patterns

1. Direct provider SDK calls or hardcoded model names in application code, scripts, notebooks, agents, or services.

2. Personal AI accounts, personal API keys, personal prompts, or unapproved vendor workspaces for AIRA work.

3. Agents holding direct production credentials or invoking Git, CI/CD, Kubernetes, database, workflow, storage, or production actions outside Harness/control-plane mediation.

4. Prompt or guardrail changes hidden in runtime variables, vendor console settings, notebooks, or undocumented local files.

5. Memory or retrieval becoming authoritative without source trace, classification, freshness, conflict check, and human review.

6. AI approving, merging, deploying, rotating production secrets, changing policy, unlocking privileged accounts, or closing its own findings.

7. Runtime diagnostic toggles disabling mandatory audit, policy, security, agent action, model-route, guardrail, idempotency, outbox, or critical error evidence.

8. AI-generated code, configuration, database migration, policy, prompt, or runbook promoted without PR/MR, CI/CD gates, evidence, and human checker.

## 4.16 Required Evidence
| Evidence Category | Minimum Required Content |
| --- | --- |
| AI runtime evidence | trace_id, request_id, actor/agent identity, prompt version, model alias, guardrail results, retrieval pack, policy decision, output classification, evidence_ref. |
| AI artifact evidence | artifact ID, owner, purpose, version, source, classification, tests, evaluation profile, approval, rollback version, activation state. |
| Agent evidence | agent_id, owner, lifecycle state, skill scope, OPA policy, tool scope, model route, memory policy, certification, trust tier, audit, kill-switch, retirement plan. |
| Tool action evidence | tool manifest, action request, risk tier, SBAC skill, OPA decision, human approval, dry-run/idempotency, execution result, rollback/compensation, audit. |
| Evaluation evidence | golden dataset, adversarial tests, prompt-injection tests, leakage tests, hallucination/unsupported claim checks, tool-misuse tests, guardrail pass/fail, red-team result. |
| Promotion evidence | PR/MR, CI/CD run, architecture fitness, SAST/SCA/secrets, SBOM/provenance, contract tests, Flyway tests, GitNexus impact, CAB/ARB decision, post-promotion monitoring. |

## 4.17 RACI
| Role | RACI | Responsibility |
| --- | --- | --- |
| Solutions Architecture Office / IT Head | A | Own parent AI governance standard, approve architecture alignment, resolve conflicts, escalate CAB/ARB issues. |
| AI Governance Lead | A/R | Own prompt, guardrail, model route, agent certification, evaluation, trust, and registry governance. |
| Security Architecture | A/R | Own OPA/SBAC, secrets, classification, route eligibility, threat model, abuse cases, tool action risk, and incident/security sign-off. |
| DevSecOps Lead | R | Implement CI/CD gates, evidence packs, SBOM/provenance, registry validation, Harness integration, and deployment controls. |
| QA/SDET Lead | R | Own AI evaluation datasets, regression suites, red-team tests, tool-action tests, model-route tests, and evidence quality. |
| Platform / SRE | R | Operate LiteLLM, guardrail runtime, observability, dashboards, alerts, kill-switch, runtime toggles, and incident response. |
| Developers / System Builder Users | R | Use approved prompts, aliases, tools, repositories, PR/MR templates, tests, and evidence paths; do not bypass controls. |
| Internal Audit | C/I | Review evidence chain, control operation, access reviews, waiver treatment, and audit defensibility. |

## 4.18 Validation Checklist
| ID | Validation Check |
| --- | --- |
| VC-01 | No direct provider SDK or hardcoded model/provider references exist in controlled code paths. |
| VC-02 | All AI model calls route through approved LiteLLM/private gateway aliases with classification ceiling and guardrails. |
| VC-03 | Prompt, guardrail, model alias, tool policy, evaluation dataset, and agent changes are registered, versioned, tested, and approved. |
| VC-04 | Input, Retrieval, Execution, and Output guardrail checkpoints execute or fail closed. |
| VC-05 | Agent identity, lifecycle, SBAC scope, OPA policy, classification ceiling, trust tier, tool scope, memory policy, and kill-switch are valid before activation. |
| VC-06 | Tool/MCP actions are mediated by Harness/control plane and have manifest, OPA/SBAC, approval, idempotency, audit, and rollback evidence. |
| VC-07 | Memory/RAG uses approved sources only, with ACL, classification, freshness, conflict, citation, and poisoning checks. |
| VC-08 | All material AI flows emit trace, metric, log, audit, policy, model-route, guardrail, and evidence references without secrets or raw sensitive payloads. |
| VC-09 | Runtime toggles do not disable mandatory audit, security, policy, idempotency, outbox, guardrail, agent action, model-route, or critical error evidence. |
| VC-10 | Auto-Heal, Auto-Learn, and Auto-Improve outputs remain candidates until approved change path, tests, evidence, and human approval are complete. |

# 5. Simplification Recommendations
| Recommendation | Reason |
| --- | --- |
| Use one-page AI runtime gate card | Developers and agents need a short checklist: source, classification, prompt, guardrail, route, policy, evidence, approval, rollback. |
| Use registry templates | Prompt, guardrail, alias, dataset, tool, and agent YAML templates should prevent ad-hoc artifact definitions. |
| Make route aliases boring | Application teams should select from approved aliases and not design provider routing unless assigned AI Governance responsibility. |
| Package tests as CI templates | Guardrail, model-route, OPA/SBAC, direct-provider-import, prompt-registry, and evidence-manifest tests should be reusable pipeline components. |
| Separate advisory AI from action-taking AI | Default all AI to advisory until explicit registry, trust, policy, and tool evidence prove action eligibility. |

# 6. Automation Recommendations
| Automation Area | Recommended Control |
| --- | --- |
| AI artifact inventory | Generate a registry inventory for prompts, guardrails, model aliases, evaluation datasets, tool manifests, agents, and memory policies. |
| Direct provider call detection | Use Semgrep/import rules to reject direct OpenAI/Anthropic/Gemini/provider SDK imports in application code and agents. |
| Route and guardrail validation | Validate LiteLLM aliases, classification ceilings, fallback routes, budgets, guardrail profiles, and evaluation status in CI. |
| Agent registry validation | Block activation when agent owner, purpose, classification ceiling, SBAC, OPA, tools, memory policy, certification, telemetry, or retirement path is missing. |
| RAG eligibility scan | Check source authority, freshness, conflict state, classification, ACL, citations, and quarantine state before retrieval index publication. |
| Evidence manifest validation | Require AI evidence fields in CI/CD, PR/MR, incident, release, UAT, and operations records. |
| Assurance dashboard | Track prompt/guardrail/model-route drift, direct-provider violations, unsafe outputs, blocked tool actions, guardrail failures, evaluation expiry, token/cost anomalies, and agent trust changes. |
| Agent-assisted review queue | AI may prioritize review findings and draft remediation, but final closure remains human-approved and evidence-backed. |

# 7. Review Queue Control Register
| Sequence | File Name | Pack | Current Version | Recommended Version | Review Status | Priority | Dependency | Action Required | Next Step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 41 | 23B Architecture Fitness Function Catalog | Pack 06 | v1.1 | v1.2 | Completed / Revised | P1 | 01A, 08, 10-10E, 11/11A, 20, 31A | Completed | Use as executable architecture control baseline |
| 42 | 42 AI Governance and Runtime Control Standard | Pack 10 | v1.1 | v1.2 | Completed / Revised | P0 | 01A, 01/01B, 11/11A, 17/17A, 20, 23B, 31A | Completed | Use as parent AI governance baseline |
| 43 | 22A Prompt, Guardrail, Model Alias, and AI Evaluation Registry | Pack 05 | v1.1 | v1.2 | Next for Review | P0 | 42 v1.2, 05, 06, 17/17A, 20, 31A | Review registry companion for prompts, guardrails, LiteLLM aliases, model routes, and evaluations | Proceed next |
| 44 | 42D AI Agent Identity Lifecycle and Credential Hygiene Standard | Pack 10 | v1.2 | v1.3 recommended | Pending | P0 | 42 v1.2, 22A v1.2, 17/17A, 31A | Review after 22A so agent identity inherits corrected registry and model-route governance | Review after 22A |

# 8. Change Log
| Version | Date | Owner | Summary |
| --- | --- | --- | --- |
| v1.1 | May 2026 | Solutions Architecture Office | System Builder expansion and agent lifecycle governance update. |
| v1.2 | 16 June 2026 | Solutions Architecture Office / IT Head | Review, correction, alignment, simplification, and expanded runtime-control update. Aligned with current AIRA foundation, MicroFunction, DevSecOps, security, API, database/Flyway, observability, architecture fitness, System Builder, AI Agent, and knowledge governance baselines. |

# 9. AVCI Compliance Summary
| AVCI Property | Evidence in This Standard |
| --- | --- |
| Attributable | Every AI artifact, call, route, guardrail, agent, tool action, System Builder output, approval, and evidence record has owner, source, version, actor/agent identity, and reviewer. |
| Verifiable | AI behavior is verified through registry checks, guardrail tests, route tests, golden/adversarial evaluations, OPA/SBAC decisions, CI/CD gates, telemetry, audit, and evidence packs. |
| Classifiable | AI inputs, retrieved context, prompts, outputs, model routes, memory, logs, evidence, and storage destinations carry classification and handling rules. |
| Improvable | Failures, denials, unsafe outputs, incidents, waivers, drift, and evaluation regressions feed backlog, Auto-Learn candidates, standards updates, training, and recertification. |

