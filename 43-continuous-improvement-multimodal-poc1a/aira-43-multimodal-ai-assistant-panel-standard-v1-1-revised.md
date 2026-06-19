---
title: "Multimodal AI Assistant Panel Standard"
doc_id: "AIRA-43"
version: "v1.1"
status: "revised"
category: "Continuous improvement, multimodal AI, and PoC1A"
source_docx: "AIRA_43_Multimodal_AI_Assistant_Panel_Standard_v1.1_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 43-continuous-improvement-multimodal-poc1a
  - revised
  - aira-43
---



# Multimodal AI Assistant Panel Standard



AIRA

AI-Native Enterprise Platform

AIRA Multimodal AI Assistant Panel Standard

Toggleable Workspace AI Prompt | Multimodal Input and Output | Guardrails | Artifact Governance | Human-Approved Action Boundary

AIRA-DOC-043 | Version v1.1 Revised
| Property | Value |
| --- | --- |
| Document ID | AIRA-DOC-043 |
| Canonical Filename | AIRA_43_Multimodal_AI_Assistant_Panel_Standard_v1.1_Revised.docx |
| Recommended Version | v1.1 Revised |
| Status | Draft for Architecture, Security, DevSecOps, AI Governance, Product, QA/SDET, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Review Date | 2026-06-17 |
| Primary Source Reviewed | 43-AIRA_Multimodal_AI_Assistant_Panel_Standard_v1.0.docx |
| Supersedes | 43-AIRA_Multimodal_AI_Assistant_Panel_Standard_v1.0.docx upon approval |

Mandatory Control Statement

Dynamic, composable, AI-assisted, and multimodal capabilities must remain backend-governed, policy-filtered, MicroFunction-backed, auditable, reversible, and AVCI-compliant. Dynamic must never mean uncontrolled. AI may recommend, explain, summarize, generate, and propose; approved AIRA services, policies, workflows, MicroFunctions, and accountable human roles remain authoritative.

# 1. Document Control
| Field | Value |
| --- | --- |
| Document Title | AIRA Multimodal AI Assistant Panel Standard |
| Document ID | AIRA-DOC-043 |
| Version | v1.1 Revised |
| Status | Draft for Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; AI Governance; Security Architecture; DevSecOps Lead; Software Development Lead; Frontend Lead; Backend Lead; QA/SDET; Platform Engineering; SRE; Data Governance; Internal Audit |
| Target Audience | Solutions Architects, Software Developers, Frontend Developers, Backend Developers, DevSecOps, QA/SDET, Security, Product Owners, AI Engineers, SRE, Internal Audit |
| Source Document Reviewed | 43-AIRA_Multimodal_AI_Assistant_Panel_Standard_v1.0.docx |
| Companion Documents | 01/01A/01B AVCI and Enterprise Architecture; 10 MicroFunction Framework; 15/15A API; 16/16A/16B Database and Flyway; 17/17A Security; 22A Prompt, Guardrail, Model Alias, and AI Evaluation Registry; 31A Observability; 41 Dynamic Workspace; 42 AI Governance; 42O-42S Agent Registry and Governance; 43 Continuous Improvement; 46-61 Dynamic Workspace companion guides |
| Review Cadence | Quarterly; unscheduled after AI panel, prompt, guardrail, model route, Dynamic Workspace, MicroFunction, security, classification, workflow, observability, or DevSecOps control change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Dynamic-Workspace / AI-Assistant-Panel / v1.1/ |

## 1.1 Change Summary
| Change Area | v1.1 Revised Treatment |
| --- | --- |
| Governance posture | Retains the v1.0 rule that the AI panel is a governed assistant, not an autonomous business actor. Strengthens backend authority, MicroFunction execution boundaries, and human-approved action routing. |
| Multimodal controls | Clarifies controls for text, voice, files, images, screenshots, screen context, selected records, generated documents, voice, video, images, checklists, references, workflow proposals, and action proposals. |
| System Builder and agent alignment | Adds registry, capability, evidence, and policy fields needed for System Builder and future AI agents to consume this standard deterministically. |
| DevSecOps and evidence | Adds contract-first API/event requirements, CI/CD gates, GitNexus impact evidence, DAST/SAST/SCA, SBOM/provenance, evaluation evidence, and PR/MR AVCI summary expectations. |
| MicroFunction coverage | Adds standard step families for prompt intake, guardrails, retrieval, model routing, artifact registration, action proposal, idempotency, outbox, DLQ/replay, resilience lab, and Auto-Heal/Auto-Learn/Auto-Improve candidate loops. |
| Observability and runtime toggles | Defines mandatory telemetry and safe runtime tuning. Diagnostic logging and sampling may be adjusted at runtime, but minimum audit, security, guardrail, and evidence controls must not be disabled. |

## 1.2 Table of Contents Placeholder

Insert a Microsoft Word automatic Table of Contents here before final publication: References > Table of Contents > Automatic Table. Update fields after final pagination and approval.

# 2. Executive Review Summary

The v1.0 Multimodal AI Assistant Panel Standard correctly established the AIRA principle that the AI panel is a governed assistant, not a business authority. It also correctly defined multimodal input/output modes, guardrail checkpoints, artifact registration, and safe action boundaries. This v1.1 revision preserves those controls and strengthens them into a developer-ready, audit-ready, System Builder-consumable standard.

The primary improvements are: stronger integration with Dynamic Workspace backend governance; explicit AI capability registry fields; clearer MicroFunction-backed execution patterns; contract-first OpenAPI and AsyncAPI expectations; event/outbox/DLQ/replay requirements; runtime observability and telemetry controls; accessibility and UX expectations; AI evaluation and prompt registry alignment; and a practical validation checklist for software development, DevSecOps, QA, security, and AI governance teams.

# 3. Source and Context Alignment
| AIRA Area | Required Alignment for Document 43 |
| --- | --- |
| Enterprise Architecture and AVCI | All panel components, prompts, model routes, outputs, artifacts, and actions must remain attributable, verifiable, classifiable, and improvable. SOLID, Clean Architecture, DDD, ports/adapters, policy-as-code, observability, testability, security, and reversibility are mandatory. |
| System Builder | The System Builder may generate AI panel configuration, prompt templates, capability bindings, tests, and evidence manifests only as draft or PR-ready artifacts. It must not activate prompts, model routes, actions, or runtime behavior without approval. |
| MicroFunction Framework | The panel renders, collects user intent, and displays proposals. Backend MicroFunctions execute governed business actions using policy, idempotency, audit, outbox, observability, rollback, and evidence steps. |
| Dynamic Workspace | The panel is a registered AI widget/experience block. It must be policy-filtered, capability-bound, screen-context minimized, accessible, reversible, and backend-authorized. |
| AI Agent Governance | Agent and assistant capabilities must use registry-defined owners, classification ceilings, SBAC skills, OPA policies, model aliases, guardrails, tool/action scope, trust tier, and telemetry evidence. |
| DevSecOps Evidence | Changes must produce CI/CD evidence: tests, security scans, contract checks, policy checks, SBOM/provenance, GitNexus impact summary, AI evaluation evidence, and PR/MR AVCI summary. |
| Database/Flyway | AI capability, artifact, prompt, action proposal, approval, retention, and evidence tables must be managed through Flyway only. PostgreSQL remains authority; Redis/Valkey remains derivative cache. |
| API and Integration Contracts | AI Assist APIs must be OpenAPI-defined. AI events must be AsyncAPI-defined, CloudEvents-compatible where cross-boundary, schema-versioned, and supported by idempotent consumers and DLQ/replay. |
| Security and Access Control | Prompt, file, screen-context, artifact, and action handling must enforce identity, RBAC, ABAC, SBAC, OPA, classification, secrets hygiene, redaction, consent, and fail-closed behavior. |
| Observability and Evidence | Every prompt, guardrail, retrieval, model route, artifact, action proposal, policy decision, and error path must emit safe logs, metrics, traces, audit records, and evidence references. |
| Continuous Improvement | Failed guardrails, hallucination reports, user feedback, incident findings, test gaps, drift signals, and dashboard anomalies become proposal-driven Auto-Heal, Auto-Learn, or Auto-Improve candidates only. |

## 3.1 Conflict and Reconciliation Findings
| Finding | Severity | Correction Applied |
| --- | --- | --- |
| Document 43 and Document 58 overlap on multimodal prompt, artifact, response, and action-proposal governance. | Medium | Document 43 is positioned as the AI Assistant Panel component and runtime standard. Document 58 should remain the detailed prompt, artifact, and response governance guide and should be reviewed next for consolidation and cross-reference cleanup. |
| Older Dynamic Workspace documents reference 43 as a companion but do not consistently state the AI panel must use OpenAPI, AsyncAPI, outbox, DLQ/replay, and DevSecOps evidence. | Medium | This revision adds mandatory contract-first, event, outbox, observability, and DevSecOps evidence controls. |
| Some source snippets describe diagrams as Mermaid flow text, which is useful for design but not sufficient for implementation governance. | Low | This revision converts the flow into formal control sections, validation checkpoints, MicroFunction steps, and evidence requirements. |
| Runtime telemetry toggles could be misread as permission to disable governance logging. | High | This revision distinguishes performance tuning from security control disabling. Debug verbosity and sampling may be adjusted; mandatory audit, security, policy, guardrail, and evidence records must remain active. |

# 4. Review and Gap Analysis
| Review Area | Assessment |
| --- | --- |
| What is correct and should be retained | The v1.0 control statement, optional/toggleable panel concept, multimodal input/output model, artifact registry requirement, human approval boundary, mortgage guidance example, and prohibition against direct business execution are sound and retained. |
| What is outdated or weak | The v1.0 document is concise but too thin for developers. It lacks full DevSecOps gates, API/event contract detail, resilience and replay behavior, AI evaluation evidence, runtime telemetry tuning rules, and System Builder/agent consumption fields. |
| What is missing | Missing items include OpenAPI/AsyncAPI contracts, schema evolution, Kafka/CloudEvents/outbox/DLQ/replay, idempotent action proposals, authenticated DAST, abuse cases, resilience lab, GitNexus, and explicit evidence checklist. |
| Simplification need | Developers need a clear separation between what the AI panel may do, what it must never do, and when it must hand off to MicroFunctions, workflow, OPA/SBAC, Harness, and human approval. |
| Governance strengthening | The revised standard adds policy-as-code, classification, retention, AI capability registry, artifact registry, approval states, immutable evidence, and fail-closed rules. |
| Automation readiness | The revised standard introduces machine-readable capability metadata, validation checklist, fitness functions, event schema expectations, and review queue fields for System Builder and CI/CD use. |
| Terminology standardization | Use AI Assistant Panel, AI capability, action proposal, workflow proposal, generated artifact, source reference, model alias, guardrail result, evidence reference, classification ceiling, and MicroFunction-backed action consistently. |

# 5. Revised Full AIRA Document

## 5.1 Purpose

This standard defines the architecture, governance, implementation, security, observability, evidence, and acceptance requirements for the AIRA Multimodal AI Assistant Panel inside the Dynamic User Workspace. It enables users to interact with AIRA through text, voice, files, images, screenshots, selected records, and approved screen context while preserving backend authority, MicroFunction execution, OPA/SBAC policy control, guardrails, human approval, and AVCI evidence.

## 5.2 Scope
| In Scope | Out of Scope |
| --- | --- |
| Toggleable AI panel component, prompt intake, multimodal inputs, retrieval/context assembly, model routing, generated outputs, artifact registration, references, workflow/action proposals, evidence, tests, and runtime observability. | Direct business approval, direct production mutation, direct model-provider SDK calls, unmanaged prompts, unregistered tools, direct database writes, frontend authorization authority, personal AI accounts, unrestricted telemetry, or AI-generated official actions without human approval. |
| Integration with Dynamic Workspace, System Builder, AI capability registry, prompt/guardrail/model alias registry, API/event contracts, MicroFunction runtime, Flowable/Temporal workflow, OPA/SBAC, Harness, OpenKM/DMS, and evidence stores. | Replacing official systems of record, approving KYC, posting payments, releasing titles, changing official records, bypassing branch/role/skill constraints, or storing Restricted data in uncontrolled model routes. |

## 5.3 Audience

This standard is for solutions architects, enterprise architects, frontend developers, backend developers, AI engineers, DevSecOps engineers, QA/SDET, security administrators, SRE, product owners, internal audit, and approved AI agents or System Builder workflows that generate or validate AI panel artifacts.

## 5.4 Governing Principles
| ID | Principle | AI Assistant Panel Application |
| --- | --- | --- |
| EDP-01 | SOLID | Panel UI, prompt processing, model routing, guardrails, artifacts, and action proposal services have single responsibilities and explicit interfaces. |
| EDP-02 | Clean Architecture | Domain and use-case logic does not depend on React, model providers, databases, workflow engines, or media-generation providers. |
| EDP-03 | DDD / Bounded Contexts | Mortgage, KYC, payment, title release, audit, evidence, and AI assistance remain separate bounded contexts. |
| EDP-04 | Ports and Adapters | Model routes, STT/TTS, vision, document generation, workflow, DMS, Kafka, Redis, and storage use ports/adapters. |
| EDP-05 | DRY, KISS, YAGNI | Reuse standard AI capability, artifact, evidence, and MicroFunction patterns before creating custom code. |
| EDP-06 | Idempotency by Design | Prompt submission, artifact generation, action proposal, approval callback, outbox publication, replay, and retries must be duplicate-safe. |
| EDP-07 | Determinism and Reproducibility | Prompts, model aliases, guardrails, retrieval packs, tests, and evidence are versioned and reproducible. |
| EDP-08 | Fail-Safe, Not Fail-Open | Missing identity, classification, policy, guardrail, model gateway, artifact registry, or audit blocks protected behavior. |
| EDP-09 | Human-in-the-Loop | Official, high-impact, Restricted, workflow-mutating, financial, KYC, title, and production-impacting actions require named approval. |
| EDP-10 | Least Privilege / SBAC | Capabilities, context, tools, data, and model routes are limited by role, skill, tenant, branch, classification, and purpose. |
| EDP-11 | Separation of Duties | Requester, generator, reviewer, approver, deployer, operator, and auditor remain separable for high-risk workflows. |
| EDP-12 | Observability by Design | Trace, metric, log, audit, guardrail, model route, artifact, action, and evidence references are emitted safely. |
| EDP-13 | Policy as Code | Input eligibility, retrieval, output, action, routing, data handling, and artifact approval rules are versioned policies. |
| EDP-14 | Testability by Design | Panel, APIs, prompts, retrieval, guardrails, policies, artifacts, and action proposals have deterministic tests. |
| EDP-15 | Secure by Design | Prompt injection, data leakage, insecure output handling, model denial-of-service, and supply-chain risks are controlled. |
| EDP-16 | Resilience Patterns | Timeouts, retries, circuit breakers, fallback, DLQ, replay, compensation, and safe degradation are explicit. |
| EDP-17 | Architectural Fitness Functions | CI/CD verifies boundaries, no direct provider calls, no unauthorized endpoints, policy tests, and evidence completeness. |
| EDP-18 | Progressive Autonomy | The panel starts advisory; action-taking requires evidence, policy, trust, approval, and rollback controls. |
| EDP-19 | Reversibility / Rollbackability | Capabilities, prompts, routes, templates, and generated artifacts support rollback, disablement, expiry, or revocation. |
| EDP-20 | AVCI | Each prompt, response, artifact, action proposal, policy decision, and improvement item is attributable, verifiable, classifiable, and improvable. |

## 5.5 Architecture Position

The AI Assistant Panel is a registered Dynamic Workspace component and AI experience block. The frontend renders the panel, captures user intent, displays grounded responses, and presents action proposals. The backend AI Assist service classifies the request, applies guardrails, assembles permitted context, routes through approved model aliases or media adapters, registers outputs, and emits evidence. Protected business actions are executed only by approved workflow and MicroFunction paths.
| Layer | Allowed Responsibility | Must Not Do |
| --- | --- | --- |
| AI Panel UI | Render toggleable/dockable accessible UI, show input mode, references, warnings, generated artifact status, and proposal state. | Own authorization, call unregistered endpoints, expose hidden context, store secrets, or execute protected actions. |
| AI Assist API | Accept prompt requests, enforce contract, classify, validate idempotency, call backend orchestration ports, and return safe responses. | Call model providers directly from controllers or bypass guardrails, OPA/SBAC, audit, or evidence. |
| AI Orchestrator | Apply input/retrieval/execution/output guardrails, select approved LiteLLM/model/media route, assemble context, and register output. | Treat AI output as business authority or invoke tools outside Harness and policy. |
| Workflow / Approval | Route high-impact proposals to Flowable/Temporal and named human reviewers. | Allow requester to approve own high-risk action or bypass SoD. |
| MicroFunction Runtime | Execute approved, idempotent, observable, auditable business steps after policy and approval. | Bypass audit, outbox, OPA/SBAC, rollback, or classification controls. |
| Evidence and Registry | Persist prompt, model route, guardrail, source references, artifact metadata, approvals, and outcome evidence. | Store raw secrets, raw tokens, unrestricted PII, or unmanaged prompt content. |

## 5.6 AI Capability Registry Requirement

Every AI capability exposed in the panel must be registered before activation. Registration is a governance artifact, not optional UI configuration.
| Field | Required Meaning |
| --- | --- |
| capability_id | Stable capability code such as AI_MORTGAGE_GUIDANCE or AI_LOGIN_INCIDENT_SUMMARY. |
| version | Semantic version of the capability definition. Material prompt, guardrail, retrieval, route, or output change creates a new version. |
| owner and reviewer | Named accountable owner and reviewer/checker. |
| input_modes | Allowed inputs: TEXT, VOICE, FILE, IMAGE, SCREEN_CONTEXT, SELECTED_RECORD_CONTEXT. |
| output_modes | Allowed outputs: TEXT, REFERENCES, CHECKLIST, IMAGE, VOICE, VIDEO, DOCUMENT, WORKFLOW_PROPOSAL, ACTION_PROPOSAL. |
| model_route_policy | Approved LiteLLM alias or approved private/on-prem route for classification level. |
| guardrails | Input, retrieval, execution, and output guardrail references. |
| classification_ceiling | Maximum allowed data and output classification. |
| retrieval_sources | Approved source collections with freshness, version, access, and citation rules. |
| human_approval_required_for | Actions and outputs requiring named approval, including official documents and high-impact recommendations. |
| evidence_profile | Required telemetry, audit, artifact, and PR/MR evidence fields. |
| rollback_or_disablement | Capability disablement, prompt rollback, model-route rollback, artifact expiration, or feature flag path. |

## 5.7 Input Modes and Required Controls
| Input Mode | Description | Mandatory Controls |
| --- | --- | --- |
| Text | Typed prompt from authorized user or approved agent. | Prompt classification, injection detection, input guardrail, rate limit, model budget, safe logging, evidence_ref. |
| Voice | Speech-to-text then prompt processing. | Consent, STT adapter, transcript classification, redaction, retention rule, user-visible indicator, guardrail. |
| File | Documents, forms, PDFs, images, spreadsheets, or other attachments. | Malware scan, content-type validation, DMS/OpenKM reference, OCR/extraction, classification, retention, restricted-route check. |
| Image / Screenshot | Photo, screenshot, scan, or visual record. | Vision route eligibility, redaction where required, classification, prompt injection detection in image text, evidence capture. |
| Screen Context | Current screen, widget, workflow, or document context. | Only approved fields; no hidden data leakage; context minimization; field-level policy filtering; tenant/branch/user scope check. |
| Selected Record Context | Specific customer, loan, property, KYC, task, or ticket references. | ABAC/SBAC/OPA validation, classification ceiling, access purpose, audit, trace, and evidence correlation. |

## 5.8 Output Modes and Required Controls
| Output Mode | Allowed Use | Mandatory Controls |
| --- | --- | --- |
| Text | Answer, explanation, summary, instruction, or recommendation. | Grounded where applicable, source references, confidence/limitations, output guardrail, safe disclaimer for advisory content. |
| References | Links or citations to approved source artifacts. | Source ID, version, classification, freshness, retrieval eligibility, and access policy. |
| Checklist | Step list based on approved process or policy. | Trace to approved SOP/process; no invented compliance requirement; owner and version. |
| Image | Generated image or visual explanation. | Artifact registration, content policy, classification, source prompt, storage_ref, retention. |
| Voice | TTS output from approved text response. | Derived from approved text, classification, retention, consent, and evidence. |
| Video | Async generated guide or demonstration. | Job registry, source prompt, approval if official, storage, retention, review state. |
| Document | DOCX/PDF/checklist/form/letter/report draft. | Template control, classification, document owner, human review if official or Confidential/Restricted. |
| Workflow Proposal | Proposed workflow start or task routing. | Human review before execution, policy check, workflow evidence, and rollback/withdrawal path. |
| Action Proposal | Suggested MicroFunction or tool action. | Harness/SBAC/OPA, idempotency key, human approval where required, audit, outbox, and evidence before execution. |

## 5.9 Standard Prompt Processing Flow
| Step | Control Point | Required Output |
| --- | --- | --- |
| 1 | Receive prompt through AI Assist API | prompt_id, trace_id, request_id, actor_id_hash, workspace_code, capability_id. |
| 2 | Classify input and context | classification, data handling rule, route eligibility, retention rule. |
| 3 | Scan and validate attachments | malware result, MIME validation, extraction result, source_ref. |
| 4 | Apply input guardrail | prompt injection result, abuse-case result, blocked/degraded/allowed decision. |
| 5 | Assemble retrieval and screen context | permitted source_refs, context_hash, freshness, policy decision. |
| 6 | Select model/media route | LiteLLM alias or approved adapter, budget, classification ceiling, fallback. |
| 7 | Execute model/media call | model_route_used, token/cost metadata, timeout/retry state, provider abstraction evidence. |
| 8 | Apply output guardrail | safety, leakage, unsupported claim, hallucination, citation, and output format checks. |
| 9 | Register response and artifacts | artifact_id, artifact_hash, storage_ref, retention, approval_state, evidence_ref. |
| 10 | Return response safely | safe response envelope with trace_id, evidence_ref, references, warnings, and proposal state. |
| 11 | Publish audit/outbox event | CloudEvents/AsyncAPI event, idempotency key, consumer state, DLQ/replay metadata. |
| 12 | Record improvement signals | feedback, guardrail failure, hallucination report, incident link, backlog candidate. |

## 5.10 MicroFunction Alignment

The AI panel is not a MicroFunction replacement. It invokes or proposes governed MicroFunction transactions only through registered capability bindings and approved APIs. Every mutating or high-impact AI-driven action must map to a MicroFunction transaction with the following applicable step families.
| Step Family | Examples | Mandatory Treatment |
| --- | --- | --- |
| DevSecOps and Evidence | CI/CD, security gates, evidence pack, GitNexus. | Every panel capability change requires tests, scans, policy checks, AI evaluations, GitNexus impact summary, and PR/MR AVCI evidence. |
| Contract and Event Governance | OpenAPI, AsyncAPI, Kafka, Avro, CloudEvents. | All APIs/events are contract-first, schema-versioned, backward-compatible, and validated in CI. |
| Outbox, Idempotency, DLQ, Replay | Prompt events, artifact events, action proposals. | Cross-boundary events use transactional outbox. Consumers are idempotent. DLQ and replay are tested and evidence-producing. |
| Observability | Log4j2, OpenTelemetry, Sentry, Loki, Tempo, Grafana. | Logs, metrics, traces, audit, error monitoring, dashboards, alerts, and trace reconstruction are required with safe redaction. |
| Concurrency and Heavy Transaction | Duplicate prompt submit, repeated action proposal, parallel approvals. | Idempotency keys, optimistic locking, retry-safe steps, duplicate suppression, and resilience lab evidence are mandatory. |
| Security and Abuse Cases | Prompt injection, data exfiltration, insecure output handling, excessive agency. | OPA/SBAC expansion, authenticated DAST, secrets hygiene, secure APIs, red-team cases, and remediation evidence are required. |
| Auto-Heal / Auto-Learn / Auto-Improve | Guardrail failure, poor answer, stale source, failed action proposal. | The loop may detect, retrieve evidence, propose a fix or learning item, generate tests, and request human approval. It must not silently mutate active behavior. |

## 5.11 Safe Action Boundary

The AI panel must never directly execute protected business operations. It may propose actions and may route user intent into approved workflow or MicroFunction entry points only after policy, classification, idempotency, and approval requirements are satisfied.
| Action Type | Panel Permission | Execution Path |
| --- | --- | --- |
| General guidance | Allowed when classification and retrieval policy allow. | AI Assist API -> Guardrails -> Response -> Audit/Evidence. |
| Checklist or explanation | Allowed when grounded in approved sources. | AI Assist API -> Retrieval -> Output guardrail -> Artifact/evidence registry. |
| Official customer communication | Draft only unless approved. | Document generator -> Human review -> Approved communication workflow. |
| KYC acceptance/rejection | Not allowed as direct action. | Action proposal -> OPA/SBAC -> Workflow -> Human approval -> MicroFunction. |
| Payment posting | Not allowed as direct action. | Action proposal -> Payment workflow -> Maker-checker -> Approved payment MicroFunction. |
| Title release | Not allowed as direct action. | Action proposal -> Title release workflow -> Required approvals -> MicroFunction. |
| Production configuration change | Not allowed as direct action. | System Builder proposal -> PR/MR -> CI/CD -> ARB/CAB approval -> controlled promotion. |

## 5.12 Artifact Registry Standard
| Field | Required Meaning |
| --- | --- |
| artifact_id | Unique generated artifact identifier. |
| artifact_type | TEXT, IMAGE, AUDIO, VIDEO, DOCUMENT, CHECKLIST, REFERENCE, PROPOSAL. |
| prompt_id | Source prompt or request reference. |
| owner | Human or service owner responsible for artifact. |
| model_route | Approved model alias or media adapter route. |
| guardrail_result | Input/retrieval/execution/output guardrail outcome. |
| classification | Artifact classification and classification ceiling. |
| source_refs | Evidence and retrieval source references with version and freshness. |
| storage_ref | DMS/object store/OpenKM reference. |
| content_hash | Hash of canonical artifact representation. |
| retention_rule | Expiry, archive, legal hold, purge, or disposal rule. |
| approval_state | Draft, reviewed, approved, rejected, expired, retired. |
| evidence_ref | AVCI evidence record and trace correlation. |

## 5.13 API, Event, and Data Governance
| Domain | Requirement |
| --- | --- |
| OpenAPI | AI Assist REST APIs must be OpenAPI-defined with trace_id, request_id, idempotency key for mutations, classification, evidence_ref, safe error envelope, and generated clients. |
| AsyncAPI | Prompt submitted, artifact generated, guardrail failed, action proposed, approval completed, and model route used events must be AsyncAPI-defined. |
| Kafka and CloudEvents | Cross-boundary events should use Kafka where approved and CloudEvents metadata for interoperability when events leave a bounded context. |
| Avro and schema evolution | Event payloads requiring schema registry governance must use approved schema format, compatibility policy, versioning, and consumer impact tests. |
| Transactional outbox | Events that reflect database state change must be published through transactional outbox or an approved equivalent to prevent lost or duplicated events. |
| Idempotent consumers | Consumers must deduplicate by event_id, idempotency_key, prompt_id, artifact_id, action_proposal_id, or business key as applicable. |
| DLQ and replay | DLQ records must carry reason, source event, schema version, retry count, trace_id, evidence_ref, and replay approval where sensitive. |
| Flyway | AI panel configuration, capability registry, prompt/artifact metadata, approval state, and evidence tables must be managed through Flyway only. |

## 5.14 Security and Guardrail Requirements
| Control | Mandatory Rule |
| --- | --- |
| Identity | Every prompt and action proposal must resolve human, service, or agent identity and session context. |
| Classification | Input, retrieved context, generated output, artifacts, and events must carry classification and handling rules. |
| OPA/SBAC/ABAC | Access to capability, source, screen context, selected record, output mode, and action proposal is policy-filtered. |
| Prompt injection defense | User input, uploaded files, extracted text, images, screenshots, and retrieved content must pass injection checks. |
| Output handling | Generated output must be treated as untrusted until validated by output guardrails and, where needed, human review. |
| Secrets hygiene | Never expose passwords, tokens, raw JWTs, private keys, API keys, raw secrets, or credentials in prompts, logs, outputs, artifacts, screenshots, or evidence summaries. |
| Provider boundary | Application code, scripts, notebooks, agents, and MicroFunctions must use approved LiteLLM aliases or approved private/on-prem gateways. Direct provider SDK calls are prohibited. |
| Guardrail availability | If input, retrieval, execution, or output guardrails are unavailable for protected data/action, the panel must fail closed or safely degrade. |
| Authenticated DAST | AI panel APIs, upload flows, action proposal flows, and role-specific denial paths require authenticated DAST or equivalent dynamic security testing. |

## 5.15 Observability, Audit, and Runtime Tuning

The AI Assistant Panel must emit enough telemetry and audit evidence to reconstruct who prompted, what context was used, which model route and guardrails were applied, what output was generated, whether an action was proposed, who approved, what executed, and how the outcome can be improved.
| Signal / Control | Requirement |
| --- | --- |
| Trace | End-to-end trace across frontend, AI Assist API, guardrails, retrieval, model route, artifact registry, workflow, MicroFunction, and evidence store. |
| Metrics | Latency, token/cost usage, guardrail block rate, retrieval freshness, artifact generation success/failure, proposal approval rate, policy denial rate, DLQ/replay count. |
| Logs | Structured diagnostic logs only. No raw PII, secrets, raw prompts with Confidential/Restricted data, tokens, account numbers, raw documents, or embeddings. |
| Audit events | AI_PROMPT_SUBMITTED, AI_CONTEXT_ASSEMBLED, AI_MODEL_ROUTE_USED, AI_GUARDRAIL_RESULT, AI_ARTIFACT_GENERATED, AI_ACTION_PROPOSED, AI_ACTION_DENIED, AI_ACTION_APPROVED, AI_FEEDBACK_RECORDED. |
| Dashboards | AI panel health, guardrail outcomes, model route usage, prompt volume, cost, policy denials, artifact states, action proposals, failures, and evidence completeness. |
| Runtime tuning | Debug logging, sampling, streaming verbosity, and non-security telemetry detail may be adjusted on-the-fly when performance impact is observed. Mandatory audit, security, policy, guardrail, error, and evidence records must not be disabled. |

## 5.16 Validation Checklist
| Validation Area | Pass Condition |
| --- | --- |
| Capability registry | Every enabled AI panel capability has owner, version, input/output modes, classification ceiling, model route, guardrails, tests, approval, and disablement path. |
| OpenAPI contract | AI Assist API passes lint, schema, security, compatibility, generated-client, and safe-error checks. |
| AsyncAPI/event contract | Events are schema-versioned, CloudEvents-compatible where required, idempotent, and covered by consumer tests. |
| Guardrail tests | Input, retrieval, execution, and output guardrails pass positive, negative, abuse-case, and regression tests. |
| Security tests | SAST, SCA, secret scan, authenticated DAST, dependency/license checks, prompt injection tests, and output handling tests pass or have approved waiver. |
| OPA/SBAC tests | Role, skill, branch, tenant, classification, source, action, and human approval rules are tested with Rego/policy tests. |
| MicroFunction tests | Action proposal path maps to approved transaction, idempotency, audit, outbox, rollback, and evidence. |
| Observability tests | Trace, logs, metrics, audit, Sentry, Loki, Tempo, Grafana, and evidence dashboards show expected correlation without forbidden fields. |
| Resilience lab | Timeout, model gateway failure, guardrail failure, retrieval failure, duplicate submission, outbox retry, DLQ, replay, cache loss, and partial degradation are tested. |
| Accessibility and UX | Keyboard, screen reader labels, focus management, responsive layout, non-obscuring panel behavior, and safe denial states pass. |
| Evidence pack | PR/MR contains owner, source, classification, tests, scans, policy results, GitNexus, AI evaluation, rollback, and improvement path. |

## 5.17 Implementation Guidance

Start from an approved ticket, intake record, or System Builder proposal with owner, source, classification, and acceptance criteria.

Register or update the AI capability before implementation. Confirm allowed input/output modes, model route, guardrails, retrieval sources, classification ceiling, and human approval rules.

Define or update OpenAPI and AsyncAPI contracts before coding. Generate clients from approved contracts only.

Implement frontend panel changes as registered Dynamic Workspace components. Do not embed business rules or hidden authorization in the UI.

Implement backend orchestration behind ports/adapters for LiteLLM, STT, TTS, vision, document generation, DMS, workflow, and evidence stores.

Use Flyway for all schema, seed, RLS, view, policy metadata, and evidence table changes.

Implement deterministic unit, component, integration, contract, OPA, AI evaluation, accessibility, E2E, security, resilience, and regression tests.

Produce a PR/MR evidence pack with GitNexus impact analysis, scans, test results, policy results, AI evaluation results, rollback/disablement path, and improvement backlog.

Activate only after maker-checker, security, QA, product owner, and required ARB/CAB approval based on risk and environment.

Monitor guardrail failures, policy denials, hallucination reports, support tickets, latency, costs, and artifact review outcomes after release.

## 5.18 Anti-Patterns
| Anti-Pattern | Required Correction |
| --- | --- |
| Frontend calls model provider or media provider directly. | Route through backend AI Assist API and approved LiteLLM/media adapters. |
| Panel displays hidden screen context or unauthorized fields. | Apply backend field-level policy filtering and context minimization. |
| AI output is treated as official business decision. | Treat output as advisory unless approved through workflow and accountable human review. |
| Action proposal executes without workflow or MicroFunction approval. | Route to OPA/SBAC, approval, Harness where applicable, and MicroFunction runtime. |
| Raw prompts, tokens, documents, or PII are logged. | Redact, hash, classify, store references only, and enforce forbidden telemetry tests. |
| Model name, API key, or fallback is hardcoded. | Use registered LiteLLM alias and route policy. |
| Generated artifacts lack owner, retention, or approval state. | Register artifacts with owner, classification, source refs, storage, retention, approval, and evidence. |
| Telemetry is turned off to improve performance. | Tune sampling/verbosity only; preserve minimum audit, security, policy, error, and evidence events. |

## 5.19 Required Evidence
| Evidence Item | Minimum Content |
| --- | --- |
| AI capability registration | capability_id, owner, version, input/output modes, classification ceiling, model route, guardrails, approval, disablement path. |
| Prompt and guardrail evidence | Prompt version, guardrail version, evaluation dataset, adversarial tests, regression results, approval record. |
| API/event evidence | OpenAPI/AsyncAPI files, schema compatibility, generated clients, outbox and consumer tests. |
| Security evidence | SAST, SCA, secret scan, authenticated DAST, OPA/SBAC tests, prompt injection tests, output handling tests, waiver records if any. |
| Observability evidence | Trace sample, dashboard screenshot/reference, log redaction proof, metric names, alert rules, Sentry/Loki/Tempo/Grafana evidence. |
| Artifact evidence | artifact_id, source prompt, model route, storage_ref, hash, classification, retention, approval_state, evidence_ref. |
| DevSecOps evidence | CI run, test reports, SBOM/provenance, GitNexus impact summary, architecture fitness, deployment approval, rollback/disablement proof. |
| Improvement evidence | Feedback, guardrail failures, hallucination reports, incidents, RCA, candidate fix, tests, approval, and closure link. |

## 5.20 Acceptance Criteria and Definition of Done

All enabled AI panel capabilities are registered, approved, classified, versioned, tested, and disableable.

Text, voice, file, image, screenshot, screen context, and selected-record flows pass classification, guardrail, policy, and evidence checks where enabled.

All generated outputs and artifacts are registered with owner, source references, classification, retention, approval state, and evidence reference.

High-risk actions are proposals only until policy, workflow, MicroFunction, and human approval requirements are satisfied.

OpenAPI, AsyncAPI, Kafka/CloudEvents, schema evolution, outbox, idempotent consumers, DLQ, and replay paths are validated where applicable.

Observability, audit, dashboards, alerts, trace reconstruction, error monitoring, and forbidden telemetry tests pass.

Security gates, authenticated DAST, prompt injection tests, OPA/SBAC tests, AI evaluation tests, and resilience lab pass or have approved waivers.

PR/MR AVCI evidence pack is complete and linked to the review queue, change record, and improvement backlog.

## 5.21 RACI Matrix
| Activity | SAO / IT Head | Architecture | Dev Lead | AI Gov | Security | DevSecOps | QA/SDET | Product | Audit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Approve standard | A | R | C | C | C | C | C | C | I |
| Define AI capability | A | C | R | R | C | C | C | R | I |
| Define prompt/guardrail/model route | A | C | C | R | R | C | C | C | I |
| Implement panel/API/MicroFunction binding | C | C | A/R | C | C | R | C | I | I |
| Validate security/policy | A | C | C | C | R | C | R | I | I |
| Validate evidence and readiness | A | C | C | C | C | R | R | C | A/R |

## 5.22 Related AIRA Documents

Primary references include AIRA-DOC-001/001A/001B for AVCI and enterprise design; AIRA-DOC-010 series for MicroFunction framework; AIRA-DOC-015/015A for API and integration contracts; AIRA-DOC-016 series for Flyway/database governance; AIRA-DOC-017 series for security; AIRA-DOC-022A for prompt, guardrail, model alias, and AI evaluation registry; AIRA-DOC-031A for observability; AIRA-DOC-041 and 042 for Dynamic Workspace and Composable Experience; AIRA-DOC-042D through 42S for AI agent governance; AIRA-DOC-043 Continuous Improvement; and AIRA-DOC-046 through 061 for Dynamic Workspace implementation companions.

## 5.23 External Reference Register
| Reference | Use in This Standard |
| --- | --- |
| NIST AI RMF and NIST AI 600-1 Generative AI Profile | Risk framing for generative AI outputs, human-AI configuration, information integrity, data privacy, information security, and value-chain controls. |
| OWASP Top 10 for Large Language Model Applications | Prompt injection, sensitive information disclosure, insecure output handling, excessive agency, model denial-of-service, and supply-chain threat controls. |
| OpenAPI Specification | Contract-first REST API description for AI Assist endpoints and generated clients. |
| AsyncAPI Specification | Machine-readable event-driven API contracts for prompt, artifact, guardrail, approval, and action-proposal events. |
| CloudEvents Specification | Interoperable event metadata for cross-boundary event publishing and routing. |
| OpenTelemetry Semantic Conventions | Common naming and correlation model for traces, logs, metrics, events, profiles, and resources. |

## 5.24 Change Log
| Version | Date | Summary | Status |
| --- | --- | --- | --- |
| v1.0 | 2026-06-16 source pack baseline | Initial Multimodal AI Assistant Panel Standard. | Source baseline |
| v1.1 Revised | 2026-06-17 | Expanded into formal AIRA standard with alignment analysis, MicroFunction coverage, contract/event governance, observability, DevSecOps evidence, validation checklist, and review queue. | Draft for review |

# 6. Simplification Recommendations
| Recommendation | How to Simplify Without Weakening Governance |
| --- | --- |
| Separate component standard from detailed prompt/artifact guide | Keep Document 43 focused on AI Assistant Panel behavior and boundaries. Move detailed prompt response lifecycle, templates, and artifact examples to Document 58 and cross-reference it. |
| Use one capability registration template | Create one machine-readable AI capability template reused by System Builder, Admin Builder, CI/CD, and Obsidian. |
| Use standard acceptance checklist | Adopt the checklist in Section 5.16 as a reusable PR/MR gate so developers do not interpret requirements differently. |
| Avoid duplicate diagrams | Maintain one canonical flow diagram source and regenerate images for Word/Obsidian instead of copying inconsistent diagrams. |
| Apply feature flags carefully | Make AI panel capabilities toggleable by policy and feature flag, but do not make mandatory security, audit, guardrail, or evidence controls optional. |

# 7. Automation Recommendations
| Automation Area | Recommended Control |
| --- | --- |
| Document inventory | Maintain a Git/Obsidian/OpenKM document manifest with document ID, filename, version, owner, classification, source pack, supersedes, status, and review date. |
| Canonical register | Update the canonical register after every revised document and block duplicate document IDs or conflicting titles. |
| Cross-reference validation | Run a script to detect stale references to superseded filenames, missing companion references, and wrong version numbers. |
| Version tracking | Compare current document control against source register and previous revised output. |
| Duplicate detection | Detect duplicate content across 43 and 58 and classify as intentional overlap, companion detail, or consolidation candidate. |
| Terminology consistency | Validate controlled terms such as AI Assistant Panel, AI capability, model alias, guardrail, action proposal, evidence_ref, and MicroFunction-backed action. |
| Conflict detection | Flag direct provider calls, frontend authority, unmanaged prompts, manual DDL, unapproved telemetry, or missing approval routes. |
| Missing-section detection | Require document control, alignment findings, gap analysis, mandatory rules, validation checklist, evidence requirements, RACI, and change log. |
| Evidence checklist validation | Validate PR/MR evidence against tests, security scans, GitNexus, AI evaluation, policy checks, rollback, and AVCI summary. |
| Agent-assisted review queue | System Builder may propose next document review order and draft revisions, but approval remains human-owned. |
| Obsidian or Git tracking | Store approved summaries in Obsidian, authoritative source in OpenKM/Git, and review status in a versioned register. |
| Optional scripts/manifests | Use YAML/JSON manifests for documents, controlled terms, source pack membership, cross-references, review queue, and evidence checklist status. |

# 8. Review Queue Control Register
| Sequence | File Name | Pack | Current Version | Recommended Version | Review Status | Priority | Dependency | Action Required | Next Step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 43-AIRA_Multimodal_AI_Assistant_Panel_Standard_v1.0.docx | Pack 12 | v1.0 | AIRA_43_Multimodal_AI_Assistant_Panel_Standard_v1.1_Revised | Completed draft revision | High | 42S, 43 Continuous Improvement, 22A, 41/42 Dynamic Workspace, 58 companion guide | Review, approve, and update canonical register | Proceed to 58 after Jun confirmation |
| 2 | 58-AIRA_Multimodal_AI_Prompt_Artifact_and_Response_Governance_Guide_v1.0.docx | Pack 15 | v1.0 | AIRA_58_Multimodal_AI_Prompt_Artifact_and_Response_Governance_Guide_v1.1_Revised | Recommended next | High | 43 AI Assistant Panel; 22A Prompt/Guardrail/Model Alias Registry; 53 Observability | Align detailed prompt, artifact, output, retention, and action-proposal rules with revised 43; reduce overlap; add DevSecOps/MicroFunction coverage | Review next |
| 3 | 53-AIRA_Dynamic_Workspace_Observability_Audit_and_Evidence_Specification_v1.0.docx | Pack 15 | v1.0 | AIRA_53_Dynamic_Workspace_Observability_Audit_and_Evidence_Specification_v1.1_Revised | Queued | High | 43 and 58 | Align AI prompt/artifact telemetry, forbidden fields, dashboards, trace reconstruction, and runtime toggles | Review after 58 |
| 4 | 54-AIRA_Dynamic_Workspace_Admin_Builder_and_Template_Governance_Standard_v1.0.docx | Pack 15 | v1.0 | AIRA_54_Dynamic_Workspace_Admin_Builder_and_Template_Governance_Standard_v1.1_Revised | Queued | Medium | 43, 46, 53, 58 | Ensure Admin Builder can configure AI panel capabilities without becoming authority or bypassing policy | Review after observability |
| 5 | 60-AIRA_Dynamic_Workspace_DevSecOps_Pipeline_and_Evidence_Pack_Guide_v1.0.docx | Pack 15 | v1.0 | AIRA_60_Dynamic_Workspace_DevSecOps_Pipeline_and_Evidence_Pack_Guide_v1.1_Revised | Queued | Medium | 43, 53, 58 | Ensure dynamic workspace, AI panel, and experience pack changes produce complete DevSecOps evidence | Review after Admin Builder |

## 8.1 Next Recommended Review

Next document to review: 58-AIRA_Multimodal_AI_Prompt_Artifact_and_Response_Governance_Guide_v1.0.docx. It should be next because it directly overlaps with Document 43 and contains the detailed prompt, artifact, response, reference, checklist, document, workflow proposal, and action proposal governance rules. Reviewing 58 next will prevent duplication and ensure that the panel standard remains concise while the detailed prompt/artifact guide becomes the implementation companion.

# 9. AVCI Compliance Summary
| AVCI Property | Compliance Evidence |
| --- | --- |
| Attributable | Owner, co-owners, source document reviewed, supersedes, related documents, capability owner, prompt owner, artifact owner, approver, and review queue are defined. |
| Verifiable | Validation checklist, API/event contracts, guardrail tests, security scans, OPA/SBAC tests, AI evaluations, observability evidence, and PR/MR evidence pack are required. |
| Classifiable | Inputs, screen context, retrieved sources, outputs, artifacts, prompts, events, logs, and evidence carry classification, ceiling, handling, retention, and route eligibility. |
| Improvable | Feedback, guardrail failures, hallucination reports, incidents, telemetry, support tickets, GitNexus findings, and review queue items become controlled improvement candidates. |

