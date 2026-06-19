---
title: "Multimodal AI Assistant Panel Standard"
doc_id: "AIRA-43A"
version: "v1.1"
status: "revised"
category: "Continuous improvement, multimodal AI, and PoC1A"
source_docx: "AIRA_43A_Multimodal_AI_Assistant_Panel_Standard_v1.1_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 43-continuous-improvement-multimodal-poc1a
  - revised
  - aira-43a
---



# Multimodal AI Assistant Panel Standard



AIRA

AI-Native Enterprise Platform

Multimodal AI Assistant Panel Standard

Toggleable Workspace AI Prompt | Multimodal Input/Output | Guardrails | Artifact Governance | Human-Approved Action Boundary | AVCI Always

Version v1.1 Revised | June 2026
| Mandatory AIRA Control Statement
Dynamic, composable, AI-assisted, and multimodal capabilities must remain backend-governed, policy-filtered, MicroFunction-backed, auditable, reversible, and AVCI-compliant. Dynamic must never mean uncontrolled. AI may recommend, explain, summarize, generate, and propose; approved AIRA services, policies, workflows, and accountable human roles remain authoritative. |
| --- |
| Property | Value |
| --- | --- |
| Document Title | AIRA Multimodal AI Assistant Panel Standard |
| Document ID | AIRA-DOC-043A (proposed numbering; reconciles duplicate AIRA-DOC-043 records in Source Pack 12) |
| Canonical Filename | 43A-AIRA_Multimodal_AI_Assistant_Panel_Standard_v1.1_Revised.docx |
| Version | v1.1 Revised |
| Supersedes | 43-AIRA_Multimodal_AI_Assistant_Panel_Standard_v1.0 |
| Related but not superseded | 43 Continuous Improvement v1.2 Revised; 43 PoC1A Login Security Intelligence; 43C Login PoC Traceability Matrix |
| Classification | INTERNAL CONFIDENTIAL |
| Status | DRAFT FOR ARCHITECTURE REVIEW BOARD / CAB / AI GOVERNANCE APPROVAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Dynamic Workspace Product Owner; Security Architecture; DevSecOps Lead; Software Development Lead; QA/SDET; Platform Engineering; AI Governance; SRE; Internal Audit |
| Primary Audience | CTO / IT Head, Enterprise Architects, Software Developers, Frontend Developers, Backend Developers, DevSecOps, Security, QA/SDET, SRE, AI Engineering, Product Owners, Internal Audit |
| Review Cadence | Quarterly; unscheduled on material AI, guardrail, model route, Dynamic Workspace, MicroFunction, API/event, data, security, observability, or DevSecOps change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Dynamic-Workspace / Multimodal-AI-Assistant-Panel / v1.1/ |

Document Positioning Note. This revision updates only the Multimodal AI Assistant Panel standard. It does not regenerate 42S, the 42D-42R AI Agent Governance family, the recently revised 43 Continuous Improvement standard, or PoC 1 / PoC 1A artifacts.

# Static Table of Contents

1. Executive Summary

2. v1.1 Alignment Decision and Change Summary

3. Purpose, Scope, and Authority

4. Source Baseline and Numbering Reconciliation

5. Enterprise Design Principles Acceptance Gate

6. Architecture Position and Control Flow

7. Dynamic Workspace UX and Frontend Implementation Requirements

8. Multimodal Input Governance

9. Multimodal Output and Artifact Governance

10. Prompt Processing, Guardrails, RAG, and Model Routing

11. MicroFunction, Workflow, and Action Proposal Boundary

12. API, Event, Outbox, Schema Evolution, DLQ, and Replay Requirements

13. Data, Flyway, Registry, and Retention Requirements

14. Observability, Audit, Evidence, and Runtime Telemetry Toggle Rules

15. Security, OPA/SBAC, Abuse Cases, Authenticated DAST, and Secrets Hygiene

16. Concurrency, Heavy Transaction, Idempotency, and Resilience Lab

17. DevSecOps Pipeline, Security Gates, Evidence Pack, and GitNexus

18. Human Approval, Progressive Autonomy, and RACI

19. Testing, Evaluation, and Architecture Fitness Functions

20. Dashboards, Metrics, SLOs, and Operational Readiness

21. Implementation Roadmap and Acceptance Criteria

22. Known Reconciliation Items and Later Companion Updates

23. AVCI Compliance Summary

Appendices A-C. Schemas, Checklists, and External Alignment Register

# 1. Executive Summary

The AIRA Multimodal AI Assistant Panel is a standard, toggleable Dynamic Workspace component that allows authorized users and approved agents to interact with AIRA through text, voice, file, image, screenshot, selected screen context, and structured business context. It may generate text, references, checklists, images, voice responses, video jobs, document drafts, workflow proposals, and action proposals when policy allows.

This v1.1 revision turns the original panel concept into an enterprise-grade implementation standard. The panel is explicitly aligned with Dynamic Workspace UX, MicroFunction backend execution, DevSecOps evidence, OpenAPI/AsyncAPI contracts, Kafka/Avro/CloudEvents event governance, outbox and replay controls, Log4j2/OpenTelemetry/Sentry/Loki/Tempo/Grafana observability, OPA/SBAC policy enforcement, abuse-case testing, authenticated DAST, secrets hygiene, and human-approved action boundaries.
| Operating Verdict
The AI panel is not business authority and is not a production automation bypass. It is a governed assistant surface. AIRA backend services authorize, MicroFunctions execute, workflows approve, PostgreSQL and Git-managed configuration define truth, and AVCI evidence proves behavior. |
| --- |
| Strategic Outcome | v1.1 Required Result |
| --- | --- |
| Safe multimodal interaction | Text, voice, file, image, screen context, and structured context are classified, minimized, scanned, guarded, and routed only through approved adapters. |
| Backend-governed Dynamic Workspace | The frontend renders an approved panel and approved response artifacts; backend resolver, OPA/SBAC, and MicroFunction bindings decide capability and action eligibility. |
| Action boundary preservation | AI may propose workflow or action candidates; protected actions require OPA/SBAC, approved MicroFunction/workflow path, maker-checker review, and evidence. |
| Evidence by construction | Every prompt, model route, guardrail result, retrieval source, artifact, action proposal, approval, denial, and runtime result has a trace/evidence chain. |
| Enterprise-grade DevSecOps | Generated or changed panel artifacts require contracts, tests, SAST/SCA/secrets scan, authenticated DAST where applicable, AI evals, GitNexus impact evidence, and PR/MR AVCI summary. |

# 2. v1.1 Alignment Decision and Change Summary

Decision: Proceed with v1.1 revision. The v1.0 source correctly established the panel as a toggleable, governed AI component, but it requires expansion to match the newer Dynamic Workspace, MicroFunction, DevSecOps, AI agent governance, observability, and continuous-improvement baselines.
| Alignment Area | v1.0 Baseline | v1.1 Improvement |
| --- | --- | --- |
| Dynamic Workspace UX | Panel is toggleable and optional. | Adds dock/minimize/expand/drawer behavior, accessibility, keyboard/screen-reader requirements, visible context indicators, policy-safe denial states, artifact status, and responsive behavior. |
| MicroFunction backend | Action proposals require workflow/MicroFunction controls. | Defines strict action boundary: AI proposes; OPA/SBAC approves eligibility; humans approve high-risk actions; MicroFunction runtime executes with idempotency, audit, outbox, and evidence. |
| API and events | AI Assist API implied. | Adds OpenAPI/AsyncAPI, CloudEvents, Kafka, Avro schema evolution, transactional outbox, idempotent consumers, DLQ, replay, and contract testing requirements. |
| Observability | Audit/evidence required. | Adds Log4j2 structured logging, OpenTelemetry traces/metrics, Sentry error monitoring, Loki logs, Tempo traces, Grafana dashboards, trace reconstruction, and protected telemetry toggle rules. |
| Security and testing | Guardrails and human review stated. | Adds OPA/SBAC expansion, abuse cases, prompt injection, unsafe output handling, authenticated DAST, secure API tests, secrets hygiene, malware scan, data-loss prevention, and remediation evidence. |
| Continuous improvement | Feedback improves prompts and guardrails. | Connects failed prompts, denials, incidents, hallucination reports, poor retrieval, slow model routes, and artifact failures to Auto-Heal/Auto-Learn/Auto-Improve candidate loops only. |

# 3. Purpose, Scope, and Authority

## 3.1 Purpose

Define how the Multimodal AI Assistant Panel is implemented as a secure, observable, reversible, and evidence-producing Dynamic Workspace component.

Prevent prompt-to-action, prompt-to-tool, prompt-to-database, prompt-to-production, and prompt-to-record mutation bypasses.

Standardize multimodal input and output handling across text, voice, file, image, screen context, generated media, documents, workflow proposals, and action proposals.

Ensure every panel capability maps to approved API contracts, policy decisions, model routes, guardrails, MicroFunction transactions, artifact registries, tests, dashboards, and evidence packs.

## 3.2 Scope
| In Scope | Out of Scope |
| --- | --- |
| AI panel rendering in Dynamic Workspace, prompt input, screen/context selection, response rendering, references, artifact status, accessibility, and responsive behavior. | Custom model-provider SDK calls directly from frontend, backend controllers, notebooks, scripts, or agents. |
| Backend AI Assist API, prompt classification, guardrails, retrieval, model routing through LiteLLM, artifact registry, workflow/action proposal, and evidence recording. | AI approval of business decisions, KYC decisions, title release, payment posting, access approval, production deployment, or security exception. |
| Multimodal file/image/voice processing through approved adapters with malware scan, classification, redaction, retention, consent, and evidence controls. | Unmanaged uploads, unclassified prompts, unrestricted raw prompt logging, unrestricted embeddings, or uncontrolled local files. |
| OpenAPI/AsyncAPI, Kafka/Avro/CloudEvents, outbox, idempotency, DLQ/replay, and schema evolution for AI panel events and artifact workflows. | Direct database writes from the panel, direct event publication without outbox where cross-boundary durability is required, or unversioned schema changes. |

## 3.3 Authority and Precedence
| Level | Authority | Role |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance / AI Governance | Final authority for production-impacting AI panel capability, model route, data handling, high-risk action, exception, and waiver decisions. |
| L1 | AIRA AVCI, 01A EDP/SOLID, AI Governance, Security, DevSecOps, Observability, Change/Reversibility Standards | Universal controls for evidence, classification, policy, audit, tests, rollback, and human approval. |
| L2 | This 43A Multimodal AI Assistant Panel Standard | Canonical control for panel behavior, multimodal modes, UX boundary, action proposal boundary, artifact governance, and evidence expectations. |
| L3 | OpenAPI/AsyncAPI, OPA/Rego, MicroFunction configuration, Flyway migrations, UI schema, CI/CD gates | Executable implementation controls that enforce this standard. |
| L4 | Tickets, PR/MR records, evidence packs, model route logs, guardrail results, runtime traces, incidents | Operational proof and improvement inputs. |

# 4. Source Baseline and Numbering Reconciliation

This revision uses the active AIRA baseline provided in the current source packs and the already revised companion documents from the current project conversation. It specifically updates the Multimodal AI Assistant Panel standard and treats older, duplicate, or overlapping documents as source inputs rather than automatically approved canonical replacements.
| Source / Companion | Required Treatment in v1.1 |
| --- | --- |
| 43 Multimodal AI Assistant Panel v1.0 | Superseded by this v1.1 revision for panel governance. |
| 43 Continuous Improvement v1.2 Revised | Companion source for proposal-driven Auto-Heal/Auto-Learn/Auto-Improve loops; not superseded by this document. |
| 58 Multimodal AI Prompt, Artifact, and Response Governance Guide v1.0 | Implementation guide requiring later alignment to this v1.1 standard. |
| 41 Dynamic User Workspace and 47-61 Dynamic Workspace companion set | Governs frontend, UX, security, cache, observability, DevSecOps, and template lifecycle integration. |
| 10/10A-10E MicroFunction framework | Governs backend execution, runtime assembly, idempotency, outbox, audit, and evidence. |
| 42D-42S AI Agent Governance family | Governs agent identity, trust, runtime controls, tool/MCP, memory/RAG, red team, incident response, policy, registry, and roadmap; not regenerated here. |
| Numbering Reconciliation Item
Source Pack 12 contains multiple AIRA-DOC-043 records. This revision uses AIRA-DOC-043A as a proposed canonical identifier for the Multimodal AI Assistant Panel until the master register / 00D reconciliation item confirms final numbering. The governing content should be tracked as a register reconciliation item rather than hidden in the document body. |
| --- |

# 5. Enterprise Design Principles Acceptance Gate

Every AI panel capability, prompt template, adapter, API, event, MicroFunction binding, UI component, generated artifact, test, and evidence pack must pass EDP-01 through EDP-20 before activation. This gate applies equally to human-authored and AI-assisted changes.
| Principle | Mandatory AI Panel Interpretation |
| --- | --- |
| EDP-01 SOLID | Panel components, adapters, prompt handlers, artifact services, and MicroFunctions remain single-responsibility, interface-driven, and dependency-inverted. |
| EDP-02 Clean Architecture | Domain/use-case logic does not depend on Next.js, controllers, databases, LiteLLM, model providers, workflow engines, or storage providers. |
| EDP-03 DDD / Bounded Contexts | AI panel capabilities respect identity, mortgage, KYC, payments, title release, audit, policy, and workspace boundaries. |
| EDP-04 Ports and Adapters | STT, TTS, OCR, image generation, video generation, document generation, retrieval, model routing, storage, and workflow systems are behind explicit ports/adapters. |
| EDP-05 DRY, KISS, YAGNI | Reuse standard panel modes, artifact registry, guardrail rails, and MicroFunction bindings before adding new code. |
| EDP-06 Idempotency by Design | Prompt retries, artifact generation retries, workflow proposals, event consumers, and approvals must not duplicate business effects. |
| EDP-07 Determinism and Reproducibility | Prompts, routes, retrieval sources, tests, artifacts, migrations, and evidence are reproducible from approved source references. |
| EDP-08 Fail-Safe, Not Fail-Open | Missing identity, policy, classification, guardrail, model route, evidence, or adapter control blocks or safely degrades protected behavior. |
| EDP-09 Human-in-the-Loop | High-impact, low-confidence, Restricted, destructive, production-impacting, official, or exception actions require named human review. |
| EDP-10 Least Privilege / SBAC | Panel capabilities are skill-scoped; users, agents, services, and tools only receive approved modes, data, and actions. |
| EDP-11 Separation of Duties | Requester, maker, checker, approver, deployer, model route owner, policy owner, and auditor remain separable. |
| EDP-12 Observability by Design | Critical paths emit safe traces, metrics, logs, audit, model route events, artifact events, policy decisions, and evidence references. |
| EDP-13 Policy as Code | Capability access, model routing, artifact visibility, context use, and action proposal eligibility are governed by versioned policies. |
| EDP-14 Testability by Design | Panel UI, prompt templates, guardrails, model routes, policies, adapters, APIs, events, and MicroFunction bindings are independently testable. |
| EDP-15 Secure by Design | Prompt injection, data exfiltration, unsafe output, insecure adapters, secrets leakage, and cross-tenant data exposure are explicitly controlled. |
| EDP-16 Resilience Patterns | Timeouts, retries, circuit breakers, bulkheads, rate limits, DLQ, replay, compensation, and fallbacks are defined. |
| EDP-17 Architectural Fitness Functions | CI checks boundaries, direct provider calls, unregistered actions, forbidden telemetry, contract drift, policy drift, and evidence completeness. |
| EDP-18 Progressive Autonomy | The panel starts advisory; action scope advances only with evidence, trust, policy, guardrails, rollback, and human governance. |
| EDP-19 Reversibility / Rollbackability | Panel capabilities, routes, artifacts, feature flags, templates, and action bindings support rollback, disablement, forward-fix, or compensation. |
| EDP-20 AVCI | Every prompt, output, artifact, action proposal, policy decision, and improvement remains attributable, verifiable, classifiable, and improvable. |

# 6. Architecture Position and Control Flow

The AI Assistant Panel is a frontend workspace component backed by governed services. It must not carry business authority in the browser. The frontend displays eligible capabilities, captures user intent, shows context and references, and renders results. Backend services resolve authorization, classification, context, model route, guardrails, artifact state, and action proposal eligibility.

Figure 1. AIRA original governance flow for multimodal panel interaction. The panel captures intent, but guardrails, model routing, retrieval, artifact registration, audit, and AVCI evidence are governed outside the UI.

## 6.1 Component Responsibility Matrix
| Component | Allowed Responsibility | Must Not Do |
| --- | --- | --- |
| Next.js Workspace Shell | Render policy-filtered workspace shell, mount the AI panel where allowed, preserve SSR/CSR boundaries, and call generated clients. | Authorize business access, call model providers directly, embed secrets, or expose hidden context. |
| AI Assistant Panel Component | Capture prompt mode, show selected context, display references, collect feedback, show artifact status, and request backend actions. | Execute business actions, bypass guardrails, upload files directly to ungoverned storage, or treat AI output as authority. |
| AI Assist Service | Classify prompt, assemble minimal context, call guardrail rails, route through LiteLLM, register artifacts, emit evidence. | Contain domain business rules, direct provider SDK calls outside gateway, or unclassified logging. |
| Policy Service / OPA | Evaluate user, agent, workspace, capability, prompt mode, output mode, artifact visibility, and action proposal eligibility. | Fail open, accept frontend-provided authorization as final, or ignore classification ceiling. |
| MicroFunction Runtime | Execute approved backend transactions after policy and approval gates pass, with idempotency, audit, outbox, and observability. | Execute unregistered action requests or use AI output as direct command. |
| Artifact Registry | Store metadata, classification, content hash, references, retention, approval state, and evidence pointer. | Store unmanaged raw secrets, unrestricted raw prompts, or content without retention/classification. |

# 7. Dynamic Workspace UX and Frontend Implementation Requirements

The panel must be a standard optional workspace component. It can be enabled, hidden, disabled, minimized, docked, expanded, or rendered as a drawer according to workspace policy, screen policy, user role, SBAC skill, device posture, classification ceiling, and feature flags.
| UX Requirement | Mandatory Treatment |
| --- | --- |
| Toggleable and policy-aware | Users see the panel only when backend policy permits. Disabled or denied states must explain the safe reason without exposing unauthorized data. |
| Context-transparent | The panel shows whether it is using text, voice, file, image, screen context, selected record context, or no context. Users must be able to remove selected context before submission. |
| Accessible | Keyboard access, focus order, ARIA labels, screen-reader descriptions, visible focus, error associations, and reduced-motion support are mandatory. |
| Responsive | Desktop supports docked/expanded panel; tablet supports collapsible panel; mobile supports drawer or task-focused view without obscuring critical controls. |
| Non-obstructive | The panel must not cover approval buttons, legal warnings, required fields, security messages, or payment/title release controls. |
| Safe feedback | Users can rate response usefulness, report hallucination, report unsafe output, request correction, and link feedback to evidence without exposing secrets. |
| Artifact status | Generated document/image/audio/video/checklist/workflow proposal must show status, owner, classification, retention, approval state, and evidence link where allowed. |

## 7.1 Standard UI States
| State | Expected User-Safe Behavior |
| --- | --- |
| Loading | Show progress, trace-safe request reference, and cancellation where possible. |
| Empty | Explain what the assistant can do in the current workspace and capability scope. |
| Denied | State that policy prevents the requested capability; do not expose policy internals or hidden records. |
| Requires Approval | Show the named workflow path, approver role, and expected next step without executing. |
| Degraded | Explain unavailable dependency, disable protected action, and preserve audit/evidence if possible. |
| Unsafe Prompt Blocked | Explain safe remediation options and record guardrail result. |
| Artifact Pending | Show asynchronous job status and retrieval method; avoid polling storms. |

# 8. Multimodal Input Governance

All input modes must pass classification, eligibility, injection checks, minimization, consent/retention rules, and guardrail controls before retrieval, model routing, or tool/action proposal generation. The panel must not attach hidden context that the user is not authorized to see.
| Input Mode | Required Controls |
| --- | --- |
| Text | Prompt classification, prompt injection and jailbreak checks, template binding, user/session/tenant correlation, and input guardrail. |
| Voice | Explicit consent where required, STT adapter, transcript classification, retention rule, language metadata, and ability to review/edit transcript before submission for high-impact workflows. |
| File | Upload eligibility, malware scan, type validation, DMS/OpenKM reference, content extraction/OCR, classification, retention, size limits, and prompt-injection-in-document checks. |
| Image / Screenshot | Image classification, redaction where required, vision route eligibility, OCR result review, sensitive data handling, and evidence record. |
| Screen Context | Backend-approved context fields only, field-level policy filtering, context minimization, no hidden data leakage, and visible context summary. |
| Selected Record Context | ABAC and SBAC checks, tenant/branch/workflow-state validation, classification ceiling, and source freshness. |
| Agent-Provided Context | Agent identity, trust tier, tool scope, memory/RAG eligibility, and registry-backed source references. |
| Input Minimization Rule
The panel should send the minimum context needed to answer the authorized request. It must not forward the full screen, raw document, complete customer record, or unrestricted conversation history when a scoped summary, source reference, or field-filtered payload is sufficient. |
| --- |

# 9. Multimodal Output and Artifact Governance

Outputs are not just rendered messages. They may be records, artifacts, generated media, checklists, documents, references, or workflow/action proposals. Every output must carry classification, source references, retention, visibility, review state, and evidence handling commensurate with impact.
| Output Mode | Allowed Result | Required Controls |
| --- | --- | --- |
| Text | Answer, explanation, summary, instructions. | Grounded in eligible sources where business/process guidance is provided; output guardrail; confidence/limitations when needed. |
| References | Source IDs, policies, SOPs, documents, tickets, records, or evidence links. | Show only authorized sources with version, freshness, classification, and provenance. |
| Checklist | Operational or process checklist. | Trace to approved process/policy; mark draft vs approved; link evidence and owner. |
| Image | Generated or transformed visual artifact. | Register artifact, classification, prompt lineage, content hash, review state, and retention. |
| Voice | TTS from approved text response. | Generated only after text output passes guardrail; retention/consent controls apply. |
| Video | Asynchronous generated video or guide. | Job record, approved script, review gate for official guidance, storage reference, retention, and evidence. |
| Document | DOCX/PDF/checklist/report draft. | Owner, classification, source references, approval state, watermark/label where required, and evidence. |
| Workflow Proposal | Suggested workflow start/transition or approval route. | Human review before execution; workflow engine or MicroFunction path must be approved. |
| Action Proposal | Request to perform protected action. | OPA/SBAC/Harness/MicroFunction/human approval required; AI cannot execute directly. |

## 9.1 Artifact Registry Minimum Metadata
| Field | Purpose |
| --- | --- |
| artifact_id | Unique generated or attached artifact identifier. |
| artifact_type | Text, reference, checklist, image, audio, video, document, workflow proposal, action proposal, evidence summary. |
| prompt_id / request_id / trace_id | Correlation to input, service call, trace, and runtime evidence. |
| owner / requester / reviewer | Attribution and human accountability. |
| model_route_id / adapter_id | Approved route or adapter used to generate or transform the artifact. |
| guardrail_result_id | Input/output/retrieval/execution guardrail evidence. |
| source_refs | Eligible sources used, with version/freshness/classification. |
| content_hash / storage_ref | Integrity and retrieval pointer. |
| classification / retention_rule | Handling, retention, disposal, and visibility controls. |
| approval_state | Draft, pending review, approved, rejected, retired, revoked. |
| evidence_ref / improvement_path | AVCI evidence and feedback or incident linkage. |

# 10. Prompt Processing, Guardrails, RAG, and Model Routing

Prompt processing is a governed backend flow. Input, retrieval, execution, and output guardrails are mandatory. Model access must route through LiteLLM or approved private/on-prem gateways; direct provider SDK calls from application code, scripts, notebooks, services, agents, or frontend components are prohibited.
| Stage | Mandatory Control | Fail-Closed Condition |
| --- | --- | --- |
| Prompt intake | Record prompt_id, user/agent identity, workspace, capability, input mode, classification, and context references. | Missing identity, missing workspace policy, or unknown capability blocks protected processing. |
| Input guardrail | Injection/jailbreak detection, data exfiltration checks, malware/extraction result review, and classification ceiling. | Unsafe prompt, Restricted data without route eligibility, or failed scan blocks or sanitizes request. |
| Retrieval and context assembly | Use approved sources only; enforce SBAC/ABAC/classification/freshness; preserve source references. | Unavailable retrieval policy or source conflict produces safe partial answer or blocks business guidance. |
| Model route | Route via LiteLLM alias, private/on-prem route where required, guardrail policy, model capability, cost and rate controls. | Unknown route, route-policy mismatch, or direct provider path blocks. |
| Output guardrail | Unsafe content, hallucination risk, policy leakage, sensitive data leakage, ungrounded advice, or dangerous instructions are blocked or rewritten safely. | High-risk official output without approval becomes draft/proposal only. |
| Response and artifact registry | Register output, references, content hash, classification, review state, retention, evidence, feedback link. | Registry failure blocks durable artifact publication and limits response to safe transient output. |

Copy-ready reference flow:

Prompt Input -> Identity / Session / Tenant Resolution -> Prompt Classification

-> Input Guardrail -> Context Eligibility / Retrieval / Evidence Assembly

-> OPA/SBAC Capability Check -> LiteLLM Route -> Model / Adapter Invocation

-> Output Guardrail -> Artifact Registry -> Audit / Evidence -> Feedback / Improvement Loop

# 11. MicroFunction, Workflow, and Action Proposal Boundary

The AI panel can suggest a next step, draft a workflow proposal, or prepare an action proposal. It cannot directly mutate official records, payment state, KYC state, title release state, access rights, production configuration, policies, model routes, database schema, workflow definitions, or canonical knowledge.

Figure 2. AIRA original action boundary. The AI panel drafts and proposes; OPA/SBAC, human approval, and MicroFunction runtime execute protected actions.
| Action Type | AI Panel Treatment | Required Execution Path |
| --- | --- | --- |
| Explain / Summarize | Allowed when sources, classification, and prompt safety pass. | No state mutation; evidence and references recorded. |
| Draft Document / Checklist | Allowed as draft with classification and evidence. | Human review before official use where high-impact or Confidential/Restricted. |
| Start Workflow Proposal | May prepare proposal and pre-fill safe fields. | OPA/SBAC, workflow validation, human confirmation, MicroFunction/workflow runtime. |
| Business State Change | AI may explain or propose only. | Named human approval, policy decision, idempotent MicroFunction, audit/outbox, evidence. |
| Security / Access Change | Advisory or request only. | Security-approved workflow, maker-checker, SBAC, OPA, audit, rollback, access review evidence. |
| Production / CAB Change | Proposal only. | ADR/TDL, PR/MR, CI/CD, security scans, CAB/ARB approval, rollback and monitoring. |
| Prohibited Direct Actions
The panel must not directly approve mortgage applications, verify KYC, post payments, release titles, unlock privileged accounts, change OPA policies, rotate production secrets, deploy production, alter database schema, approve its own generated output, or mutate canonical records without approved human-governed execution path. |
| --- |

# 12. API, Event, Outbox, Schema Evolution, DLQ, and Replay Requirements

All AI panel capability boundaries must be contract-first. REST-like synchronous operations use OpenAPI. Event-driven operations use AsyncAPI, CloudEvents, Kafka topic contracts, Avro or approved schema registry formats, outbox, idempotent consumers, DLQ, and replay procedures.
| Contract / Pattern | Mandatory Requirement |
| --- | --- |
| OpenAPI | AI Assist API, artifact registry API, prompt feedback API, approval proposal API, and capability discovery API must publish versioned contracts with classification, idempotency, error, and security profiles. |
| AsyncAPI | Prompt submitted, artifact generated, guardrail blocked, approval requested, response feedback, model route anomaly, and evidence finalized events must have event contracts where asynchronous behavior is used. |
| Kafka / CloudEvents | Cross-boundary events use CloudEvents envelope fields including id, source, type, subject, time, datacontenttype, specversion, trace_id, classification, and evidence_ref. |
| Avro / Schema Registry | Event payloads use versioned schemas with compatibility rules, owner, classification, retention, and deprecation policy. |
| Transactional Outbox | Events resulting from durable changes must be published from an outbox to avoid dual-write inconsistency. |
| Idempotent Consumers | Consumers deduplicate using event_id, idempotency_key, artifact_id, action_proposal_id, and schema_version where applicable. |
| DLQ | Poison messages and unrecoverable failures go to DLQ with safe payload handling, redaction, classification, remediation owner, and replay decision. |
| Replay | Replay must be explicit, bounded, authorized, idempotent, evidence-producing, and tested against duplicate effects. |

## 12.1 Required Event Families
| Event Family | Example Event Types | Evidence Fields |
| --- | --- | --- |
| Prompt Lifecycle | ai.prompt.submitted, ai.prompt.blocked, ai.prompt.completed | prompt_id, trace_id, workspace_code, capability_code, classification, guardrail_result_id, evidence_ref |
| Model Route | ai.model.route.used, ai.model.route.failed, ai.model.route.fallback | model_route_id, LiteLLM alias, guardrail_policy, token/cost metadata, route_decision_id |
| Artifact | ai.artifact.generated, ai.artifact.reviewed, ai.artifact.revoked | artifact_id, artifact_type, source_refs, content_hash, storage_ref, retention_rule, approval_state |
| Action Proposal | ai.action.proposed, ai.action.approved, ai.action.rejected, ai.action.executed | action_proposal_id, MicroFunction transaction code, OPA decision, approver, idempotency_key, audit_ref |
| Improvement | ai.feedback.received, ai.guardrail.false_positive, ai.hallucination.reported | feedback_id, incident_ref, prompt_template_ref, evidence_ref, backlog_ref |

# 13. Data, Flyway, Registry, and Retention Requirements

PostgreSQL and Git-managed configuration define authoritative truth. Redis/Valkey may cache resolved panel capability views, safe context metadata, and artifact status summaries, but it must never become authority. All tables, indexes, seed data, views, RLS policies, and reference data must be delivered through Flyway or approved migration workflow.
| Logical Schema / Registry | Purpose | Key Controls |
| --- | --- | --- |
| aira_ui.ai_capability_registry | Approved panel capabilities, input/output modes, routes, and display policies. | Flyway seed, OPA binding, owner, version, classification ceiling, feature flag. |
| aira_ai.prompt_request | Prompt metadata, identity, workspace, capability, input mode, context refs. | No unrestricted raw secrets; classification; retention; trace_id; guardrail refs. |
| aira_ai.model_route_event | LiteLLM alias, model route decision, fallback, cost/tokens, guardrail policy. | Direct provider route prohibited; route policy version required. |
| aira_ai.artifact_registry | Generated artifacts and attached input artifact metadata. | content_hash, storage_ref, classification, retention_rule, approval_state, evidence_ref. |
| aira_ai.action_proposal | AI-originated workflow or action proposal records. | OPA/SBAC decision, human approval state, MicroFunction transaction code, idempotency key, rollback path. |
| aira_audit.ai_assistant_audit | Append-only audit for prompt, guardrail, route, artifact, denial, approval, and execution events. | Append-only or versioned; tamper-evident storage where available. |

## 13.1 Retention and Disposal

Prompt and artifact retention follows data classification, business record status, legal hold, and evidence requirements.

Raw prompts containing Confidential or Restricted content must not be logged in unrestricted telemetry or copied into AI training, public SaaS systems, or unmanaged knowledge stores.

Generated artifacts that become official records must move from draft artifact governance to records-management governance with owner and retention rule.

Embeddings and retrieval indexes are derivative; they inherit classification and disposal rules from source materials and must be rebuildable from approved sources.

# 14. Observability, Audit, Evidence, and Runtime Telemetry Toggle Rules

The panel must support trace reconstruction across frontend, gateway, AI Assist API, policy engine, retrieval service, model gateway, adapters, artifact registry, MicroFunction runtime, outbox, event consumers, and evidence store. Observability must be safe by design: no passwords, tokens, raw JWTs, secrets, raw PII, raw KYC documents, unrestricted prompts, embeddings, or account numbers in unrestricted logs, metrics, traces, screenshots, or dashboards.

Figure 3. AIRA original evidence correlation chain. Prompt, trace, policy, model route, artifact, MicroFunction, and evidence identifiers must allow reconstruction.
| Signal | Required Tooling / Treatment |
| --- | --- |
| Structured logs | Log4j2 structured JSON logs with trace_id, request_id, workspace_code, capability_code, safe error code, classification, and evidence_ref where safe. |
| Traces | OpenTelemetry spans for panel request, API, policy, retrieval, model route, guardrail, adapter, artifact registry, MicroFunction, outbox, and event consumer. |
| Metrics | Latency, error rate, guardrail block rate, denial rate, artifact generation time, model route cost, token usage where allowed, retry counts, DLQ size, replay count, and approval SLA. |
| Error monitoring | Sentry or approved equivalent for frontend/backend errors, with redaction, release, route, feature flag, and trace correlation. |
| Logs and traces backends | Loki for logs, Tempo for traces, Grafana for dashboards and trace-linked panels. |
| Audit events | Append-only business/governance audit for prompt submitted, blocked, artifact generated, action proposed, approval outcome, MicroFunction execution, denial, and revocation. |
| Evidence records | AVCI record linking owner, source, classification, verification evidence, principle impact, rollback/deactivation path, and improvement path. |

## 14.1 Runtime Toggle Rules

Runtime logging and telemetry can be tuned on-the-fly for performance and incident response, but not all signals are eligible for disablement. Toggle changes are configuration changes and must be policy-governed, time-bound where elevated, auditable, reversible, and visible in dashboards.
| Signal Category | Toggle Policy |
| --- | --- |
| Business audit, security audit, OPA decision logs, approval records, artifact registry writes, evidence_ref generation | Cannot be disabled for protected flows. If unavailable, protected action must fail closed or safely degrade to advisory-only. |
| Trace sampling | May be reduced under policy, but critical/high-risk prompts, denials, incidents, action proposals, and production errors remain sampled or force-sampled. |
| Debug logs | Disabled by default in production; may be enabled temporarily with approval, TTL, redaction, and incident/change reference. |
| Model payload logging | Disabled by default. Allowed only for approved evaluation datasets or explicit incident forensics with redaction, classification, and retention controls. |
| Metrics | Must remain enabled for SLO and capacity signals; high-cardinality labels and sensitive values are prohibited. |
| Frontend client diagnostics | May be opt-in, redacted, and sampled; must not capture raw prompts, hidden fields, tokens, or unauthorized context. |

# 15. Security, OPA/SBAC, Abuse Cases, Authenticated DAST, and Secrets Hygiene

The AI panel has a large attack surface because it accepts multimodal input, retrieves context, calls models and adapters, generates artifacts, and proposes actions. Security controls must be applied at design, implementation, CI/CD, runtime, and evidence layers.
| Control Area | Mandatory Requirement |
| --- | --- |
| OPA/SBAC expansion | Policy decisions are required for panel visibility, prompt mode, context eligibility, file upload, model route, output mode, artifact visibility, workflow proposal, and MicroFunction invocation. |
| Prompt injection and jailbreak | Test direct prompt injection, indirect prompt injection in files/web-like content, roleplay bypass, tool-instruction injection, output smuggling, and policy extraction attempts. |
| Data exfiltration | Prevent unauthorized context disclosure, hidden field leakage, cross-tenant leakage, source reference leakage, and embedding/retrieval leakage. |
| Insecure output handling | Never pass model output directly into HTML rendering, shell execution, SQL, workflow transitions, OPA policy updates, or MicroFunction execution without validation and approval. |
| Authenticated DAST | Run authenticated DAST against AI panel APIs and Dynamic Workspace flows with user roles/skills representing borrower, loan officer, KYC reviewer, branch manager, admin, and auditor where applicable. |
| Secure APIs | Use generated clients, CSRF/CORS controls, authN/authZ, rate limits, idempotency keys, safe errors, Problem Details, schema validation, and contract tests. |
| Secrets hygiene | No API keys, model credentials, tokens, JWTs, refresh tokens, private keys, DB passwords, or Vault values in frontend, prompts, logs, traces, screenshots, tests, docs, or generated artifacts. |
| Remediation evidence | Every critical/high finding requires ticket, owner, fix evidence, regression test, re-scan, waiver if applicable, and closure record. |

## 15.1 Abuse Case Register
| Abuse Case | Expected Control |
| --- | --- |
| User uploads document instructing model to ignore policy and reveal hidden KYC data. | File extraction guardrail detects indirect injection; retrieval is field-filtered; output guardrail blocks leakage; evidence created. |
| User asks panel to approve KYC or release title. | Panel provides explanation or proposal only; OPA/SBAC blocks direct action; human workflow required. |
| Agent tries to use panel context to call unregistered tool. | Tool/action requires agent registry, SBAC skill, OPA decision, approved tool manifest, Harness/MicroFunction path. |
| Prompt requests raw tokens, secrets, or hidden system messages. | Input/output guardrails block and audit; safe response generated. |
| Generated HTML/Markdown contains script or unsafe link. | Output renderer sanitizes; artifact validation and content security controls apply. |
| Replay duplicate action proposal or event. | Idempotency key and event deduplication prevent duplicate effects; replay evidence is recorded. |

# 16. Concurrency, Heavy Transaction, Idempotency, and Resilience Lab

The panel must remain safe under retries, duplicate submissions, slow model routes, large file uploads, concurrent users, multiple tabs, asynchronous media generation, event replay, and partial dependency failure. Heavy and long-running work should be asynchronous and observable.
| Scenario | Required Behavior |
| --- | --- |
| Duplicate prompt submit | Client and backend idempotency keys prevent duplicate artifact/action proposal creation. |
| Concurrent action proposals | Workflow/action proposal records enforce versioning, optimistic locking, and approval state transitions. |
| Long-running media/document generation | Use asynchronous job with status events, cancellation where feasible, timeout, retry policy, and artifact registry state. |
| Model route timeout | Use timeout, retry budget, fallback policy where approved, safe response, and route failure event. |
| File processing backlog | Apply size/rate controls, queue metrics, backpressure, DLQ, and user-safe status. |
| Outbox/event consumer failure | Outbox retry, DLQ, replay runbook, idempotent consumers, and evidence of recovery. |
| Policy/guardrail unavailable | Protected flows fail closed; low-risk explanatory flow may safely degrade only if classification and identity are still valid. |
| Cache loss | Redis/Valkey is rebuilt from PostgreSQL/Git truth; no loss of authority. |

## 16.1 Resilience Lab Acceptance Tests

Retry storm test for prompt submission and artifact creation.

Concurrent approval/action proposal race test.

DLQ and replay test for ai.artifact.generated and ai.action.proposed events.

Model route timeout and fallback test.

OPA outage fail-closed test.

Artifact registry outage degraded-mode test.

Large file and malware-scan queue backpressure test.

Trace reconstruction test from frontend request to model route and evidence_ref.

# 17. DevSecOps Pipeline, Security Gates, Evidence Pack, and GitNexus

Panel implementation and changes must flow through standard AIRA DevSecOps gates. A visually working panel is not accepted unless its contracts, policies, tests, scans, telemetry, artifact registry, and evidence are complete.
| Pipeline Gate | Required Evidence |
| --- | --- |
| Intake and design | Ticket/intake ID, owner, classification, affected workspace/screen/component/capability/API/event/MicroFunction, ADR/TDL trigger decision. |
| Contract gate | OpenAPI/AsyncAPI/schema lint, compatibility check, generated client evidence, error/idempotency profile. |
| Build and unit tests | Frontend component tests, backend service tests, adapter tests, policy input tests, deterministic prompt fixtures. |
| Security gates | SAST, SCA, secrets scan, IaC/container scan, OPA/Rego tests, prompt injection tests, authenticated DAST where applicable. |
| AI evaluation gate | Golden prompt set, refusal tests, grounding tests, hallucination checks, guardrail tests, model route eligibility and fallback tests. |
| Observability gate | Log redaction tests, OpenTelemetry span tests, Sentry redaction, Loki/Tempo/Grafana dashboard validation, trace reconstruction evidence. |
| GitNexus impact | Read-only code map, affected files, affected tests, dependency impact, security-sensitive path impact, architecture drift indicators. |
| PR/MR AVCI summary | Attributable owner/source, verifiable tests/scans/evidence, classifiable data/model/log rules, improvable backlog/feedback/limitations. |
| Promotion gate | Maker-checker, CODEOWNERS, ARB/CAB when required, rollback/deactivation plan, post-promotion monitoring. |

# 18. Human Approval, Progressive Autonomy, and RACI

The panel must remain advisory-first. Autonomy may increase only when evidence, trust tier, policy, guardrails, rollback, and human accountability support it. High-risk and official outcomes require named humans.
| Action / Output | Default Autonomy | Human Approval Requirement |
| --- | --- | --- |
| General explanation with public/internal sources | Advisory allowed | Reviewer only if used as official policy. |
| Confidential process guidance | Advisory with references | Owner review for formal publication or customer-facing use. |
| Restricted data analysis | Restricted route only; advisory | Named approver and evidence required; may be blocked based on policy. |
| Generated official document | Draft only | Business owner / Legal / Compliance / Security review as applicable. |
| Workflow/action proposal | Proposal only | Named maker-checker before execution. |
| Production/security/access change | Human-controlled | Security/ARB/CAB approval; AI cannot self-approve. |

## 18.1 RACI
| Activity | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Panel UX and component implementation | Frontend Lead | Dynamic Workspace Product Owner | Security, QA/SDET, Accessibility Reviewer | Developers, Product Owners |
| AI Assist API and adapters | Backend / AI Engineering | AI Governance Lead | Security, Platform, SRE | Developers, Internal Audit |
| OPA/SBAC policy | Security Architecture | Security Governance | Business Owner, Enterprise Architecture | DevSecOps, QA |
| MicroFunction action binding | Backend Lead | Solutions Architecture Office | Workflow Owner, QA, Security | Product Owner |
| DevSecOps pipeline and evidence | DevSecOps Lead | IT Head / CAB as applicable | QA, Security, Internal Audit | Development Team |
| Artifact retention and records | Data Governance / Records Owner | Compliance / Business Owner | Security, Legal, Internal Audit | Users |

# 19. Testing, Evaluation, and Architecture Fitness Functions
| Test Type | Required Coverage |
| --- | --- |
| Unit / component | Prompt input controls, mode selection, context display, response rendering, artifact status, disabled/denied states. |
| Accessibility | Keyboard-only workflow, screen-reader labels, focus management, contrast, live regions, responsive drawer behavior. |
| Contract | OpenAPI/AsyncAPI/schema compatibility, generated clients, error semantics, idempotency headers. |
| Policy | OPA/Rego tests for panel visibility, prompt mode, context, output, artifact, action proposal, MicroFunction invocation. |
| Security | Prompt injection, indirect injection, insecure output, exfiltration, XSS/sanitization, file scan bypass, secrets leak, cross-tenant access. |
| Authenticated DAST | Role/skill-based browser/API flow testing across user personas and protected routes. |
| E2E | Login, resolve workspace, toggle panel, submit safe prompt, attach file, generate artifact, request approval, denial path, feedback. |
| AI eval | Golden prompts, refusal/allowed behavior, source grounding, hallucination detection, route eligibility, guardrail false positives/negatives. |
| Resilience | Timeout, retry, duplicate submit, DLQ/replay, OPA outage, model route outage, artifact registry outage, cache rebuild. |
| Architecture fitness | No direct provider calls, no frontend authority, no direct DB from UI, no unregistered action, no forbidden telemetry, no non-Flyway schema changes. |

# 20. Dashboards, Metrics, SLOs, and Operational Readiness

Operational readiness requires dashboards and SLOs for usability, safety, cost, performance, security, and evidence completeness.
| Dashboard | Minimum Signals |
| --- | --- |
| AI panel health | Request volume, success/error rate, p95 latency, route failures, fallback rate, queue/backlog, uptime. |
| Guardrail and safety | Input blocks, output blocks, unsafe prompt patterns, false positives/false negatives, abuse-case trend. |
| Retrieval and references | Source eligibility failures, stale source attempts, missing citation rate, retrieval latency, source conflict count. |
| Artifact lifecycle | Generated artifacts by type, pending review, approved/rejected, retention exceptions, registry failures. |
| Action proposals | Proposals created, approved, rejected, executed, denied, average approval SLA, policy denial reasons. |
| Security and privacy | DAST findings, secrets scan findings, redaction failures, restricted route usage, cross-tenant denial attempts. |
| Evidence completeness | Prompt/action/artifact records with evidence_ref, missing correlation fields, trace reconstruction pass rate. |
| Cost and capacity | Model route usage, token/cost where allowed, adapter job duration, media generation queue, rate-limit events. |

# 21. Implementation Roadmap and Acceptance Criteria
| Phase | Target Outcome | Exit Evidence |
| --- | --- | --- |
| Phase 0 - Register and reconcile | Confirm document number, source baseline, owner, and companion update list. | 00D/register item, owner assignment, affected-document list. |
| Phase 1 - Contract and schema baseline | Define AI Assist API, artifact registry API, events, schemas, policies, and Flyway migrations. | OpenAPI/AsyncAPI/schema lint, Flyway dry run, OPA test draft. |
| Phase 2 - Frontend panel shell | Implement toggleable, accessible, policy-aware panel in Dynamic Workspace. | Component/a11y tests, UX walkthrough, visual evidence. |
| Phase 3 - Backend prompt flow | Implement classification, guardrails, retrieval, LiteLLM routing, output guardrail, artifact registry, audit/evidence. | Unit/integration tests, model route logs, trace evidence. |
| Phase 4 - Action proposal integration | Add workflow/action proposal boundary with OPA/SBAC/human approval/MicroFunction execution. | Policy tests, approval workflow tests, idempotency/outbox evidence. |
| Phase 5 - DevSecOps and security hardening | Complete CI gates, SAST/SCA/secrets, authenticated DAST, prompt-injection/abuse cases, GitNexus impact. | CI evidence pack and PR/MR AVCI summary. |
| Phase 6 - Operational readiness | Dashboards, alerts, SLOs, runbooks, rollback/deactivation, evidence completeness monitoring. | Grafana dashboards, SRE runbook, post-promotion monitoring proof. |

## 21.1 Acceptance Criteria

Panel renders only when backend policy permits and remains accessible across approved breakpoints.

All input and output modes are classified, guarded, tested, and evidence-producing.

No frontend, controller, script, notebook, or agent uses direct model-provider calls.

OpenAPI/AsyncAPI/schema contracts exist and pass lint/compatibility checks.

OPA/SBAC decisions cover panel, prompt, context, model route, artifact, workflow/action proposal, and MicroFunction invocation.

Generated artifacts are registered with owner, classification, source refs, content hash, approval state, retention, and evidence_ref.

Action proposals cannot execute without MicroFunction/workflow path, idempotency, audit/outbox, policy decision, and human approval where required.

Log4j2, OTel, Sentry, Loki, Tempo, and Grafana evidence proves trace reconstruction and redaction.

Authenticated DAST, prompt-injection, abuse-case, and secrets-hygiene tests produce remediation evidence.

Rollback, feature disablement, route deactivation, artifact revocation, and safe degradation paths are documented and tested.

# 22. Known Reconciliation Items and Later Companion Updates

The following items should be tracked in the canonical registers and addressed in later companion-document updates. They do not block this draft, but they must not be hidden.
| Item | Severity | Recommended Resolution |
| --- | --- | --- |
| Duplicate AIRA-DOC-043 numbering across Continuous Improvement, Multimodal AI Panel, and PoC1A source files. | High | Confirm suffix hierarchy in 00D/master register. Proposed: 43 Continuous Improvement, 43A Multimodal AI Panel, 43B PoC1A Execution, 43C Traceability Matrix, or equivalent approved register decision. |
| Runtime telemetry toggle rules not yet uniformly propagated across Observability, SRE, Dynamic Workspace, and AI panel runbooks. | Medium | Update observability/SRE/runbook companion documents with cannot-disable signal categories and TTL-governed debug toggles. |
| OpenAPI/AsyncAPI/Kafka/Avro/CloudEvents replay matrix still needs explicit implementation template. | Medium | Add template to 15/15A, 58, 60, and System Builder proposal templates. |
| Heavy transaction and Resilience Lab gates require deeper MicroFunction test-pack integration. | Medium | Update 10D/10E and 52 with prompt/artifact/action-proposal resilience fixtures. |
| Multimodal prompt/artifact/response implementation guide must be synchronized with this standard. | High | Next recommended update: 58-AIRA_Multimodal_AI_Prompt_Artifact_and_Response_Governance_Guide_v1.1_Revised.docx. |

# 23. AVCI Compliance Summary
| AVCI Property | Evidence in This Standard |
| --- | --- |
| Attributable | Defines owner, co-owners, audience, document ID, source baseline, capability owners, prompt/artifact/action owners, policy owners, model route owners, reviewers, approvers, and evidence paths. |
| Verifiable | Requires contracts, tests, OPA policy tests, AI evals, authenticated DAST, SAST/SCA/secrets scans, observability evidence, GitNexus impact, runtime traces, dashboards, and acceptance criteria. |
| Classifiable | Requires classification for prompts, inputs, screen context, retrieval sources, outputs, generated artifacts, logs, traces, metrics, evidence, retention, and model route eligibility. |
| Improvable | Links feedback, blocked prompts, hallucination reports, incidents, guardrail failures, route failures, security findings, user ratings, and telemetry into governed improvement candidates only. |

# Appendix A. Prompt and Artifact Evidence Schema

The following schema is illustrative and must be translated into approved OpenAPI/AsyncAPI/Avro/Flyway artifacts before implementation.

{

"prompt_id": "PRM-20260618-0001",

"trace_id": "<otel-trace-id>",

"workspace_code": "MORTGAGE_WORKSPACE",

"screen_code": "MORTGAGE_DASHBOARD",

"capability_code": "AI_MORTGAGE_GUIDE",

"actor_type": "human|agent|service",

"user_id_hash": "usr_hash",

"tenant_id": "BFS",

"input_modes": ["text", "file", "screen_context"],

"output_modes_requested": ["text", "references", "checklist", "document"],

"classification": "CONFIDENTIAL",

"policy_decision_id": "POLD-20260618-0001",

"guardrail_input_result_id": "GRI-20260618-0001",

"retrieval_decision_id": "RET-20260618-0001",

"model_route_id": "ROUTE-LITELLM-APPROVED-001",

"guardrail_output_result_id": "GRO-20260618-0001",

"artifact_ids": ["ART-20260618-0001"],

"action_proposal_id": null,

"evidence_ref": "EVID-AIRA-AI-PANEL-20260618-0001"

}

# Appendix B. PR/MR Evidence Checklist
| Checklist Item | Required Evidence |
| --- | --- |
| Intake and ownership | Ticket/intake ID, owner, reviewer, classification, affected capability. |
| Architecture | ADR/TDL decision or waiver, EDP impact, DDD boundary, ports/adapters map. |
| Contracts | OpenAPI/AsyncAPI/schema changes, compatibility check, generated clients. |
| Policies | OPA/SBAC rule changes and tests. |
| MicroFunction binding | Transaction code, idempotency profile, audit/outbox profile, rollback/deactivation path. |
| Security | SAST/SCA/secrets scan, authenticated DAST, prompt abuse tests, remediation evidence. |
| AI governance | Model route, guardrail rails, golden prompt eval, hallucination/safety tests. |
| Observability | OTel spans, Log4j2 logs, Sentry/Loki/Tempo/Grafana evidence, forbidden telemetry test. |
| GitNexus | Read-only code map, impact summary, affected tests, architecture drift findings. |
| AVCI | Attributable, verifiable, classifiable, and improvable summary completed. |

# Appendix C. External Alignment Register
| External Reference | Alignment Use in This Standard |
| --- | --- |
| NIST AI Risk Management Framework (AI RMF) | Trustworthy AI risk management language; govern, map, measure, and manage mindset; human accountability and risk framing. |
| OWASP Top 10 for LLM / GenAI Security Project | Prompt injection, insecure output handling, data leakage, supply-chain, agent/tool abuse, and security testing controls. |
| OpenTelemetry Generative AI Semantic Conventions | GenAI traces, metrics, events, model route metadata, token/cost attributes where allowed, and standardized telemetry naming. |
| SLSA v1.2 | Supply-chain integrity, provenance, attestation, artifact integrity, and CI/CD evidence expectations. |
| Final Interpretation
External references inform AIRA controls but do not override AIRA source governance, classification, OPA/SBAC, MicroFunction runtime, DevSecOps gates, or human approval requirements. |
| --- |

