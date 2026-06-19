---
title: "Mortgage Experience Pack Reference Implementation"
doc_id: "AIRA-45"
version: "v1.1"
status: "revised"
category: "PoC2 and mortgage experience"
source_docx: "AIRA_45_Mortgage_Experience_Pack_Reference_Implementation_v1.1_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 45-poc2-mortgage-experience
  - revised
  - aira-45
---



# Mortgage Experience Pack Reference Implementation



AIRA
AI-Native Enterprise Platform

Mortgage Experience Pack Reference Implementation

Real Property Mortgage Building Blocks | Dynamic Workspace | MicroFunction Execution | KYC | Payment | Title Release | AI Guidance | Evidence Timeline

Version v1.1 Revised | June 2026

# Mandatory AIRA Control Statement

Dynamic, composable, AI-assisted, and multimodal mortgage capabilities must remain backend-governed, policy-filtered, MicroFunction-backed, auditable, reversible, and AVCI-compliant. The Mortgage Experience Pack is a governed reference implementation, not an uncontrolled low-code/no-code mortgage system. AI may recommend, explain, summarize, generate, and propose; approved AIRA services, policies, workflows, MicroFunctions, and accountable human roles remain authoritative.

# Document Control
| Property | Value |
| --- | --- |
| Document ID | AIRA-DOC-045 |
| Document Title | AIRA Mortgage Experience Pack Reference Implementation |
| Version | v1.1 Revised - Dynamic Workspace, MicroFunction, DevSecOps, AI Governance, and Evidence Alignment |
| Supersedes | 45-AIRA_Mortgage_Experience_Pack_Reference_Implementation_v1.0 |
| Classification | INTERNAL CONFIDENTIAL |
| Status | DRAFT FOR ARCHITECTURE REVIEW BOARD / CAB APPROVAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Product Owner; Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; DBA; Platform Engineering; AI Engineering; SRE; Internal Audit |
| Primary Audience | Solutions Architects, Product Owners, Mortgage Operations, Software Developers, Frontend Developers, Backend Developers, DevSecOps, QA/SDET, Security, Internal Audit |
| Review Cadence | Quarterly; unscheduled on material mortgage, KYC, payment, title release, AI, workflow, policy, database, or Dynamic Workspace change |
| Companion Documents | 41 Dynamic User Workspace; 42 Composable Experience Framework; 43/58 Multimodal AI; 46-61 Dynamic Workspace implementation set; 10 MicroFunction; 15 API; 16 Flyway; 17 Security; 31A/53 Observability; 45 PoC2 DevSecOps Evidence; 57 Experience Pack Authoring |

# 1. Executive Summary

The Mortgage Experience Pack is the first concrete reference implementation of the AIRA Composable Experience Framework. It demonstrates how a real-property mortgage journey can be assembled from governed Experience Blocks, Dynamic Workspace screens, backend MicroFunction capabilities, workflow approvals, document and KYC processing, payment servicing, collections monitoring, title release, audit evidence, and multimodal AI guidance.

This v1.1 revision converts the original concept into an enterprise-grade, implementation-ready reference package. It aligns the pack with the revised Dynamic Workspace documents 46 through 61, the MicroFunction framework, DevSecOps evidence gates, OpenAPI/AsyncAPI contracts, outbox/event patterns, observability, security, accessibility, resilience, and the Auto-Heal/Auto-Learn/Auto-Improve candidate loop.

The pack is not a standalone application and must not become a bypass around backend authority. It is a governed reusable domain package that can be assigned to approved tenants, roles, branches, products, and workflows through controlled configuration, registered components, approved APIs, OPA/SBAC policy, Flyway-governed data structures, and AVCI evidence.
| Strategic Outcome | Required Result |
| --- | --- |
| Reference implementation | Shows the complete mortgage journey as a reusable Experience Pack rather than a one-off application. |
| Backend authority | Mortgage status, KYC decision, payment state, title release eligibility, and official records remain backend-owned. |
| MicroFunction-backed | All mutating or high-impact actions map to approved MicroFunction transactions and workflow approvals. |
| Evidence-producing | Every critical action emits trace, metric, log, audit, outbox, policy, workflow, and evidence references. |
| Human accountable | KYC acceptance/rejection, credit approval, disbursement, collection action, and title release require named human authority where required. |
| Reusable and reversible | Blocks and packs are versioned, policy-bound, safe-disableable, rollbackable, and improvable through governed change. |

# 2. Purpose, Scope, and Authority

## 2.1 Purpose

Define the governed reference implementation for the Real Property Mortgage Workspace as an Experience Pack.

Map the mortgage journey to reusable Experience Blocks, screen templates, APIs, MicroFunctions, workflows, OPA/SBAC policies, AI guidance, and evidence profiles.

Provide an implementation baseline that software developers can use for PoC, MVP, and production-bound design without weakening AIRA architecture boundaries.

Demonstrate how mortgage-specific business capability remains configurable, testable, observable, secure, reversible, and AVCI-compliant.

## 2.2 In Scope

Mortgage application intake, borrower and property data capture, KYC upload/review, property appraisal, credit evaluation, approval queue, loan offer, amortization, payment schedule, collections monitoring, full-payment confirmation, title release request, and evidence timeline.

Dynamic Workspace screens, Experience Blocks, component registry entries, capability bindings, generated API clients, OpenAPI/AsyncAPI contracts, Kafka/CloudEvents integration, outbox/inbox, DLQ/replay, and runtime telemetry.

AI Mortgage Guide behavior for explanation, checklist generation, process guidance, document drafting, and workflow/action proposals under guardrails and human approval.

## 2.3 Out of Scope

AI approval of KYC, credit, disbursement, payment posting, collection action, title release, or official customer communication.

Direct frontend authorization, direct database access from UI, direct model-provider SDK calls, direct production mutation, or manual production DDL.

A full accounting core, title registry integration, payment gateway settlement implementation, or external credit bureau adapter beyond approved ports/adapters.

## 2.4 Authority and Precedence
| Level | Authority | Role |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Business Authority | Final authority for production release, business policy, high-impact exceptions, and production-impacting mortgage workflow changes. |
| L1 | AIRA AVCI, Architecture, Security, Database/Flyway, API, DevSecOps, Observability | Universal platform controls for evidence, classification, policy, migration, contracts, observability, rollback, and release. |
| L2 | This AIRA-DOC-045 v1.1 Standard | Mortgage Experience Pack reference implementation and domain-pack governance. |
| L3 | OpenAPI, AsyncAPI, Flyway, OPA, GitNexus, tests, CI/CD evidence | Executable implementation controls and evidence. |
| L4 | Runtime events, audit records, tickets, PR/MR, dashboards, runbooks | Operational proof and improvement input. |

# 3. v1.1 Revision Summary
| Revision Area | v1.1 Alignment |
| --- | --- |
| Dynamic Workspace alignment | Aligns Mortgage Pack with revised Documents 46-61 for configuration, cache, API, database, components, policy, tests, observability, Admin Builder, seeding, frontend reference, authoring, UX, DevSecOps, and AI-assisted generation. |
| MicroFunction coverage | Adds explicit transaction map, standard step families, idempotency profiles, audit profiles, outbox profiles, workflow bindings, and rollback paths. |
| API/event contracts | Adds OpenAPI, AsyncAPI, Kafka, Avro, CloudEvents, schema evolution, transactional outbox, idempotent consumers, DLQ, and replay expectations. |
| Security and policy | Adds RBAC/SBAC/ABAC/OPA, classification ceilings, field filtering, action filtering, abuse cases, authenticated DAST, and secrets hygiene. |
| Observability | Adds Log4j2, OpenTelemetry, Sentry, Loki, Tempo, Grafana, audit, dashboards, alerting, runtime telemetry toggles, and trace reconstruction. |
| Resilience | Adds duplicate-safe actions, retry-safe UX, concurrency controls, heavy transaction behavior, and resilience lab scenarios. |
| AI governance | Adds AI Mortgage Guide boundaries, artifact registry, guardrails, retrieval eligibility, action-proposal rules, and human approval gates. |
| Continuous improvement | Adds Auto-Heal, Auto-Learn, and Auto-Improve candidate loops with evidence retrieval, tests, PR/MR, human approval, and rollback. |

# 4. Mortgage Journey and Bounded Contexts

## 4.1 End-to-End Mortgage Journey

Start mortgage application and capture borrower intent.

Submit borrower, property, collateral, and consent information.

Upload and classify KYC, supporting, and property documents.

Validate document completeness and route KYC review.

Request and track property appraisal.

Perform credit evaluation and eligibility review.

Route maker-checker approval and exception handling.

Generate loan offer, amortization, and acceptance package.

Activate or disburse approved mortgage account after controlled checks.

View dues, receipts, arrears, and payment schedule.

Monitor collections and delinquency workflows.

Confirm full payment and title release eligibility.

Request title release, property award, and release documents.

Record final audit, evidence, and retention disposition.

## 4.2 Bounded Contexts
| Bounded Context | Owned Responsibility | Representative MicroFunctions |
| --- | --- | --- |
| Mortgage Origination | Application, borrower intent, product selection, offer generation | MORTGAGE_APPLICATION_SUBMIT; MORTGAGE_OFFER_GENERATE |
| KYC and Documents | KYC upload, extraction, completeness, review, retention | KYC_DOCUMENT_UPLOAD; KYC_REVIEW_DECISION |
| Property and Appraisal | Property profile, appraisal request, appraisal result | PROPERTY_APPRAISAL_REQUEST; APPRAISAL_RESULT_RECORD |
| Credit and Approval | Credit evaluation, approval queue, maker-checker, exceptions | CREDIT_EVALUATION_RESOLVE; MORTGAGE_APPROVAL_ROUTE |
| Servicing and Payments | Amortization, dues, receipts, payment processing | MORTGAGE_PAYMENT_SCHEDULE_VIEW; MORTGAGE_PAYMENT_PROCESS |
| Collections | Delinquency detection, arrears status, collection task routing | COLLECTIONS_STATUS_RESOLVE; COLLECTION_ACTION_ROUTE |
| Title Release | Full payment confirmation, release request, release evidence | TITLE_RELEASE_REQUEST; TITLE_RELEASE_APPROVAL |
| AI Guidance and Evidence | AI guidance, artifact generation, evidence timeline | AI_MORTGAGE_GUIDE; EVIDENCE_TIMELINE_VIEW |

# 5. Experience Pack Composition

The Mortgage Experience Pack is a governed collection of blocks, screens, workflows, APIs, AI capabilities, policies, evidence profiles, and runtime configuration. It must be installable, assignable, testable, observable, reversible, and auditable.

## 5.1 Pack Manifest Baseline

experience_pack:
  pack_code: MORTGAGE_EXPERIENCE_PACK
  version: 1.1.0
  bounded_context: real-property-mortgage
  classification_ceiling: CONFIDENTIAL
  default_workspace_code: REAL_PROPERTY_MORTGAGE_WORKSPACE
  rendering_policy_code: RP_SECURE_WORKSPACE_SSR
  cache_policy: NO_STORE_FOR_USER_DATA
  evidence_profile_code: MORTGAGE_EXPERIENCE_EVIDENCE
  required_contracts:
    openapi: aira-mortgage-workspace-api-v1
    asyncapi: aira-mortgage-events-v1
    avro_schema_set: aira-mortgage-events-avro-v1
  policies:
    - opa.workspace.mortgage
    - opa.mortgage.action
    - opa.mortgage.field_filter
  blocks:
    - MORTGAGE_APPLICATION_BLOCK
    - KYC_DOCUMENT_UPLOAD_BLOCK
    - PROPERTY_APPRAISAL_BLOCK
    - CREDIT_EVALUATION_BLOCK
    - APPROVAL_QUEUE_BLOCK
    - PAYMENT_SCHEDULE_BLOCK
    - COLLECTIONS_BLOCK
    - TITLE_RELEASE_BLOCK
    - AI_MORTGAGE_GUIDE_BLOCK
    - EVIDENCE_TIMELINE_BLOCK

## 5.2 Experience Blocks
| Block | Purpose | Rendering | Binding | Primary Role |
| --- | --- | --- | --- | --- |
| MORTGAGE_APPLICATION_BLOCK | Capture and submit borrower/property application. | SSR + CSR form island | MORTGAGE_APPLICATION_SUBMIT | Customer / Mortgage Officer |
| KYC_DOCUMENT_UPLOAD_BLOCK | Upload, classify, malware-scan, and track KYC documents. | SSR + CSR upload island | KYC_DOCUMENT_UPLOAD | Customer / KYC Officer |
| KYC_REVIEW_BLOCK | Review extracted KYC data and record completeness decision. | SSR + CSR action | KYC_REVIEW_DECISION | KYC Reviewer |
| PROPERTY_APPRAISAL_BLOCK | Request, assign, and track appraisal. | SSR + CSR action | PROPERTY_APPRAISAL_REQUEST | Mortgage Officer / Appraiser |
| CREDIT_EVALUATION_BLOCK | Track credit evaluation status and recommendation. | SSR | CREDIT_EVALUATION_RESOLVE | Credit Analyst |
| APPROVAL_QUEUE_BLOCK | Route maker-checker approval tasks and exceptions. | SSR + CSR action | MORTGAGE_APPROVAL_ROUTE | Approver / Checker |
| PAYMENT_SCHEDULE_BLOCK | Show amortization, dues, receipts, and arrears. | SSR | MORTGAGE_PAYMENT_SCHEDULE_VIEW | Customer / Servicing |
| PAYMENT_ACTION_BLOCK | Initiate governed payment request or confirmation. | SSR + CSR action | MORTGAGE_PAYMENT_PROCESS | Customer / Teller / Servicing |
| COLLECTIONS_BLOCK | Monitor delinquency and route collection actions. | SSR | COLLECTIONS_STATUS_RESOLVE | Collections |
| TITLE_RELEASE_BLOCK | Request title release after full payment and approval. | SSR + CSR action | TITLE_RELEASE_REQUEST | Title / Legal / Approver |
| AI_MORTGAGE_GUIDE_BLOCK | Explain process, generate checklists, and propose actions. | SSR shell + CSR prompt + streaming | AI_MORTGAGE_GUIDE | Eligible users |
| EVIDENCE_TIMELINE_BLOCK | Display audit, evidence, policy, workflow, and event history. | SSR | EVIDENCE_TIMELINE_VIEW | Auditor / Operator |

# 6. Screen and Workspace Reference Layout
| Screen | Primary Content | Eligible Roles |
| --- | --- | --- |
| MORTGAGE_DASHBOARD | Pipeline, task summary, policy-filtered KPIs, evidence alerts | Mortgage Officer, Approver, Servicing, Collections |
| MORTGAGE_APPLICATION | Application form, borrower/property panels, submit action | Customer, Mortgage Officer |
| KYC_DOCUMENT_UPLOAD | Upload, classification, checklist, completeness status | Customer, KYC Officer |
| KYC_REVIEW | Extracted fields, reviewer decision, exception notes | KYC Reviewer, Checker |
| PROPERTY_APPRAISAL | Appraisal request, assignment, result tracking | Mortgage Officer, Appraiser |
| CREDIT_EVALUATION | Credit status, recommendation, supporting evidence | Credit Analyst, Approver |
| APPROVAL_QUEUE | Task queue, maker-checker actions, exception handling | Approver, Checker |
| PAYMENT_SCHEDULE | Amortization, dues, receipts, arrears, payment actions | Customer, Servicing |
| TITLE_RELEASE_STATUS | Full-payment proof, release workflow, release documents | Title, Legal, Approver |
| AI_MORTGAGE_GUIDE | Multimodal guidance, checklist, references, action proposals | Eligible users |
| EVIDENCE_TIMELINE | Trace/audit/policy/workflow/evidence reconstruction | Auditor, SRE, Support, Management |

# 7. MicroFunction and Workflow Binding Model

## 7.1 Standard Step Coverage

Every mortgage action begins with receive/correlate/session/tenant resolution and continues through rate limiting, authorization, classification, validation, idempotency, business step execution, audit, outbox, observability, error handling, and evidence finalization.

Business MicroFunctions must not parse transport payloads, build HTTP responses, write audit directly, call Kafka/Redis/database/model providers directly, or own framework concerns.

High-impact actions such as KYC decision, credit approval, disbursement activation, payment posting, collection escalation, and title release must use workflow approval and separation-of-duties controls.

## 7.2 Transaction Map
| Transaction | Capability | Idempotency / Control | Evidence Path |
| --- | --- | --- | --- |
| MORTGAGE_APPLICATION_SUBMIT | Submit application | Idempotency key per application draft/version; duplicate submit returns prior accepted state. | audit + outbox + evidence |
| KYC_DOCUMENT_UPLOAD | Upload document | Content hash + document slot + applicant ID; duplicate upload links existing hash or new version by policy. | malware scan + storage ref + evidence |
| KYC_REVIEW_DECISION | Accept/reject/request more info | Decision idempotency by review task; SoD checker required where policy demands. | workflow + audit + policy |
| PROPERTY_APPRAISAL_REQUEST | Request appraisal | One active appraisal request per property/application unless exception approved. | workflow + event |
| CREDIT_EVALUATION_RESOLVE | Record credit result | Versioned credit decision with maker/checker and evidence snapshot. | workflow + evidence |
| MORTGAGE_APPROVAL_ROUTE | Route approval | Approval task idempotency by workflow task and actor; no self-approval. | workflow + OPA decision |
| MORTGAGE_PAYMENT_PROCESS | Initiate/confirm payment | Payment request idempotency key; duplicate-safe callback and reconciliation. | outbox + ledger ref + receipt evidence |
| COLLECTION_ACTION_ROUTE | Route collection action | Task scoped to delinquency snapshot and approval policy. | workflow + audit |
| TITLE_RELEASE_REQUEST | Request title release | Allowed only after full-payment proof, no hold flags, and required approvals. | workflow + document evidence |
| AI_MORTGAGE_GUIDE | Explain/generate/propose | Read-only or draft/proposal only; no authoritative mutation. | model route + guardrails + artifact registry |

# 8. API, Event, Schema, Outbox, DLQ, and Replay Requirements

## 8.1 OpenAPI REST Contract Families
| API Family | Purpose | Control Requirement |
| --- | --- | --- |
| /mortgage/applications | Create/read/update draft and submit application. | No submission without idempotency key, OPA allow, classification, and audit. |
| /mortgage/applications/{id}/kyc-documents | Upload/list KYC documents and statuses. | Malware scan, hash, storage reference, retention, and field-level policy filtering. |
| /mortgage/applications/{id}/appraisals | Request/read appraisal workflow state. | No direct vendor coupling; appraisal provider behind adapter. |
| /mortgage/applications/{id}/credit-evaluation | Read/resolve credit workflow status. | Credit decision requires policy, workflow state, and evidence snapshot. |
| /mortgage/approval-tasks | List and act on approval queue. | No self-approval; SoD and SBAC enforced by backend. |
| /mortgage/accounts/{id}/payment-schedule | Read amortization, dues, receipts, arrears. | Policy-filtered response; no sensitive fields above classification ceiling. |
| /mortgage/accounts/{id}/payments | Initiate or confirm payment request. | Idempotent payment key; duplicate-safe callback; reconciliation proof. |
| /mortgage/accounts/{id}/title-release | Request and track title release. | Full-payment proof, legal/title review, and maker-checker approval required. |
| /mortgage/evidence-timeline | Read audit/evidence trail. | Redacted and role-filtered timeline only. |
| /mortgage/ai-guide | Submit prompt and receive guidance/proposals. | Routes through approved AI gateway, guardrails, and artifact registry. |

## 8.2 AsyncAPI, Kafka, Avro, CloudEvents
| Event | Meaning | Contract Rule |
| --- | --- | --- |
| mortgage.application.submitted.v1 | Application submitted and ready for KYC/appraisal workflow. | CloudEvents envelope; Avro payload; outbox source. |
| mortgage.kyc.document.uploaded.v1 | KYC document accepted into controlled storage. | Includes document hash, classification, storage reference, trace_id. |
| mortgage.kyc.review.completed.v1 | KYC review decision completed. | No raw KYC payload; decision summary and evidence_ref only. |
| mortgage.appraisal.requested.v1 | Property appraisal requested. | External adapter consumes from outbox/integration boundary. |
| mortgage.credit.evaluation.completed.v1 | Credit evaluation completed. | Evidence snapshot required; no sensitive model details in event. |
| mortgage.approval.completed.v1 | Approval workflow completed. | Maker/checker and policy references included. |
| mortgage.payment.posted.v1 | Payment posting or confirmation event. | Duplicate-safe consumer; replay idempotent by payment_id and event_id. |
| mortgage.title.release.requested.v1 | Title release workflow requested. | Requires full-payment proof and policy decision reference. |
| mortgage.evidence.recorded.v1 | Evidence timeline record appended. | For read model/dashboard synchronization. |

All events must include CloudEvents id, source, specversion, type, time, subject, trace_id, correlation_id, causation_id, classification, tenant/branch context where safe, and evidence_ref.

Schema evolution must be backward-compatible for active consumers. Breaking changes require new event type/version, consumer migration plan, replay test, and rollback plan.

All consumers must be idempotent. DLQ records must preserve event metadata, failure reason, retry count, consumer version, evidence_ref, and replay eligibility.

# 9. Security, OPA/SBAC, Classification, and Abuse Cases
| Abuse Case | Risk | Mandatory Control |
| --- | --- | --- |
| Application submission abuse | Automated spam, duplicate submit, malicious payload | Rate limit, CSRF/CORS, validation, idempotency, OPA allow, audit. |
| KYC document abuse | Malware, forged file, oversharing, prompt injection in documents | Malware scan, content hash, classification, extraction guardrails, restricted prompt assembly. |
| Approval bypass | Requester approving own task or hidden privileged action | SoD policy, SBAC approval skill, workflow task ownership, OPA deny by default. |
| Payment duplicate or tampering | Double payment, replayed callback, modified amount | Idempotency key, signed callback adapter, reconciliation, ledger reference, DLQ/replay controls. |
| Title release bypass | Release before full payment, missing legal hold, direct UI action | Full-payment proof, hold check, workflow approval, human authority, audit evidence. |
| AI overreach | AI recommends approval as authority or triggers mutation | AI guidance only; action proposal routed to MicroFunction/workflow/human approval. |
| Data leakage | Unauthorized fields in UI, telemetry, exports, AI prompts | Field filtering, classification ceiling, redaction, forbidden telemetry tests. |
| Config drift | Unapproved pack activation or runtime cache tampering | Git/PostgreSQL authority, cache rebuild, config hash, maker-checker activation. |

## 9.1 Policy Decision Inputs

actor identity, role, skill, branch, department, relationship to case, delegation status, and trust tier.

case status, workflow task ownership, classification, tenant, channel, amount, exception flags, legal hold, delinquency status, full-payment proof, and evidence state.

requested action code, component key, capability code, MicroFunction transaction code, API route, data fields requested, output mode, and risk tier.

environment, feature flag state, OPA bundle version, policy binding version, evidence profile, and runtime telemetry state.

# 10. AI Mortgage Guide and Multimodal Artifact Governance

The AI Mortgage Guide may explain the mortgage journey, summarize policy-filtered status, generate checklists, draft customer communications, create internal notes, produce process diagrams, and propose workflow actions.

It must not approve KYC, approve credit, post payments, release title, update official records, override policy, bypass workflow, or directly call model/provider SDKs.

All prompts and outputs must pass input, retrieval, execution, and output guardrails. Prompt context must be field-filtered before assembly. Generated artifacts must be registered with source references, model route, guardrail result, classification, retention, approval state, content hash, and evidence reference.

For Confidential or Restricted content, route through approved private/on-prem or formally approved model route. Raw prompts, tokens, secrets, PII, raw KYC files, account numbers, and raw documents must not be logged in unrestricted telemetry.
| Output Type | Default Permission | Control |
| --- | --- | --- |
| Explanation | Allowed | Grounded references and confidence; no legal/credit authority. |
| Checklist | Allowed | Trace checklist to approved process or policy version. |
| Document draft | Allowed with review | Classification, retention, source refs, human approval before official use. |
| Workflow proposal | Allowed as proposal | Must route to workflow and human approval before execution. |
| Payment/title action | Not directly allowed | Only a governed action proposal; MicroFunction/workflow/human approval executes. |
| KYC/credit decision | Not directly allowed | AI may summarize evidence; named human/approved workflow decides. |

# 11. Observability, Audit, Evidence, and Dashboards

All mortgage workspace loads, component renders, layout changes, widget actions, policy denials, AI prompts, generated artifacts, workflow decisions, MicroFunction executions, outbox publishes, consumer actions, DLQ writes, replay actions, and cache invalidations must be traceable and classifiable.

Backend services must use Log4j2 structured logs with safe redaction and OpenTelemetry trace, metric, and log correlation. Sentry captures frontend/backend errors where approved. Loki stores logs, Tempo stores traces, and Grafana provides dashboards and alerting.

Runtime telemetry toggles may adjust sampling and debug verbosity for performance, but must not disable mandatory security, audit, policy-decision, high-impact-action, payment, title release, or evidence telemetry.

Every evidence record must include owner, source_ref, trace_id, correlation_id, policy_decision_ref, workflow_ref where applicable, MicroFunction transaction, classification, verification evidence, reversibility, and improvement path.
| Dashboard | Minimum Content |
| --- | --- |
| Mortgage health dashboard | Application status, KYC backlog, approval queue, payment errors, title release SLA. |
| Policy denial dashboard | Denied actions by screen, role/skill, policy version, reason code, and safe response. |
| Evidence completeness dashboard | Missing evidence_ref, missing policy_decision_ref, missing trace link, weak audit fields. |
| Payment and replay dashboard | Payment callbacks, duplicates, DLQ, replay results, reconciliation exceptions. |
| AI guide dashboard | Prompt volume, guardrail outcomes, output modes, artifact approvals, denied prompt contexts. |
| Performance and resilience dashboard | Latency, error rate, cache hit/miss, outbox lag, consumer lag, slow widgets, heavy transaction behavior. |

# 12. Runtime Configuration, Cache, and Promotion

Git-managed YAML/JSON and PostgreSQL/Flyway-governed tables define authoritative Mortgage Experience Pack configuration. Redis/Valkey accelerates resolved runtime views only and must never become authority.

Pack activation must create config_change_event evidence with old/new config hash, cache keys affected, policy impact, tests, approval reference, trace_id, and evidence_ref.

Cache invalidation must be deterministic and scoped by tenant, branch, role, product, workspace, screen, pack version, rendering policy, capability binding, AI capability, and policy bundle version.

If Redis/Valkey is unavailable, the workspace resolver must rebuild from PostgreSQL/Git-authorized source, degrade safely, and preserve protected-action policy enforcement.
| Environment | Promotion Requirement |
| --- | --- |
| dev | Synthetic data only; all blocks may run with mock adapters and local policy bundle. |
| sit | Integrated adapters in controlled sandbox; contract tests and event replay tests required. |
| uat | Business UAT, accessibility, policy walk-through, evidence completeness, and operational readiness. |
| prod | CAB/ARB approval, production secrets paths, observability proof, rollback plan, and hypercare required. |

# 13. DevSecOps, GitNexus, Testing, and Evidence Pack

## 13.1 Required Pipeline Gates
| Gate | Minimum Evidence |
| --- | --- |
| Source and config lint | YAML/JSON/schema validation, component contracts, manifest hash, no prohibited fields. |
| OpenAPI/AsyncAPI validation | Contract lint, backward compatibility, generated client refresh, Problem Details test. |
| Unit/component tests | Frontend components, Zod/JSON schema, backend use cases, adapters, validators. |
| MicroFunction tests | Step order, idempotency, authorization, audit, outbox, error paths, compensation. |
| OPA/Rego tests | RBAC/SBAC/ABAC cases, field filtering, action filtering, denial evidence, SoD checks. |
| Flyway tests | Clean migrate, repeatable migrations, checksums, RLS, seed verification, rollback/rebuild runbook. |
| Accessibility and visual regression | WCAG 2.2 AA, keyboard, ARIA, focus, responsive layout, critical screen baseline. |
| Security scans | SAST, SCA, secrets scan, authenticated DAST, API abuse cases, CSP and frontend storage checks. |
| Event and replay tests | Outbox publish, idempotent consumers, DLQ, replay, schema evolution, duplicate safety. |
| Observability tests | Trace/log/metric/audit/evidence correlation and forbidden telemetry detection. |
| GitNexus impact review | Read-only code graph, affected tests, blast radius, architecture drift, evidence summary. |
| Evidence pack finalization | PR/MR AVCI, tests, scans, policy, contracts, dashboards, rollback, known limitations. |

## 13.2 PR/MR AVCI Evidence Summary

Owner, ticket, ADR/TDL, branch, commit, developer, checker, AI tools used, and prompt/source references.

Affected blocks, screens, APIs, events, schemas, policies, MicroFunctions, workflows, seeds, configuration files, and cache keys.

Test evidence for unit, component, E2E, contract, OPA, Flyway, accessibility, visual regression, authenticated DAST, replay, resilience, and observability.

GitNexus report, architecture impact, security impact, classification impact, policy impact, rollback/safe-disable plan, evidence storage path, and improvement backlog.

# 14. Concurrency, Heavy Transaction, Idempotency, and Resilience Lab
| Scenario | Failure / Load Condition | Required Behavior |
| --- | --- | --- |
| Duplicate application submit | Same draft submitted multiple times | Return same accepted application state; no duplicate account or workflow. |
| Concurrent KYC uploads | Multiple files or duplicate file hashes | Versioned document records, hash detection, no duplicate required slot completion. |
| Approval race | Two approvers act on same task | Optimistic lock/workflow task state; one succeeds, one receives safe stale-state response. |
| Payment callback replay | Gateway callback retries or duplicate messages | Idempotent consumer by payment_id/event_id; reconciliation evidence. |
| Outbox lag | Event bus unavailable or slow | Outbox retry with backoff; user sees pending state; no business data loss. |
| DLQ replay | Consumer failure corrected and replayed | Replay from DLQ with same trace/correlation and no duplicate effect. |
| Cache loss | Redis/Valkey unavailable | Rebuild from PostgreSQL; protected actions still policy-enforced. |
| AI service degradation | Model route or guardrail unavailable | AI guide degrades or blocks; mortgage actions remain unaffected. |
| Title release hold added late | Legal hold appears before release approval | Policy re-check blocks release and records denial evidence. |

# 15. Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop

The Mortgage Experience Pack may feed continuous improvement, but it must not self-mutate production behavior. All improvement loops are proposal-driven, evidence-backed, testable, reviewable, and reversible.
| Loop Stage | Mortgage Pack Requirement |
| --- | --- |
| Issue detection | Telemetry, Sentry errors, policy denials, slow widgets, DAST findings, DLQ spikes, user feedback, support tickets. |
| Evidence retrieval | Trace, logs, metrics, audit, policy decisions, GitNexus impact, test failures, contract version, runtime config hash. |
| Candidate proposal | Suggested fix, policy change, UX improvement, test addition, prompt improvement, or runbook update. |
| Validation | Unit/contract/policy/security/accessibility/replay/resilience tests and architecture fitness checks. |
| Human approval | Owner/checker/ARB/CAB as required by impact, classification, environment, and risk tier. |
| Promotion and monitoring | PR/MR, CI/CD evidence, feature flag or safe-disable path, post-promotion dashboard and rollback watch. |

# 16. Implementation Roadmap
| Phase | Outcome |
| --- | --- |
| Phase 0 | Confirm source baseline, ADR/TDL, pack manifest, bounded contexts, API/event naming, and ownership. |
| Phase 1 | Register Mortgage Experience Pack, initial screens, blocks, rendering policies, and evidence profiles. |
| Phase 2 | Implement application, KYC upload, payment schedule, and evidence timeline read flows using generated clients. |
| Phase 3 | Implement MicroFunction-backed mutating actions with workflow approval, OPA/SBAC, outbox, audit, and tests. |
| Phase 4 | Implement AI Mortgage Guide with guardrails, retrieval eligibility, artifact registry, and action proposal controls. |
| Phase 5 | Implement event consumers, outbox/inbox, DLQ/replay, resilience lab, and observability dashboards. |
| Phase 6 | Complete UAT, accessibility, authenticated DAST, GitNexus impact review, evidence pack, rollback rehearsal, and CAB readiness. |
| Phase 7 | Controlled pilot activation, hypercare, telemetry review, and improvement backlog closure. |

# 17. Acceptance Criteria and Definition of Done

Mortgage Experience Pack manifest, blocks, screens, rendering policies, capability bindings, policies, AI capabilities, workflows, and evidence profiles are registered and versioned.

All user-facing blocks use generated clients and approved API contracts; no frontend business authority, direct database access, direct model calls, or unregistered APIs exist.

All mutating actions invoke backend MicroFunctions with idempotency, OPA/SBAC, audit, outbox, observability, and rollback/compensation behavior.

KYC, payment, collections, credit, approval, and title release flows are fail-closed, policy-filtered, and human-accountable where required.

All OpenAPI, AsyncAPI, Avro, CloudEvents, outbox, DLQ/replay, schema evolution, and consumer idempotency tests pass.

WCAG 2.2 AA accessibility, keyboard operation, focus management, responsive behavior, and visual regression checks pass for critical screens.

SAST, SCA, secrets scan, authenticated DAST, OPA tests, architecture fitness functions, GitNexus impact analysis, and PR/MR AVCI evidence are complete.

Runtime telemetry dashboards prove trace/log/metric/audit/evidence correlation and forbidden telemetry tests block secrets, tokens, raw PII, raw KYC, raw prompts, and high-cardinality labels.

Pack activation, rollback, safe disablement, cache rebuild, DLQ replay, and post-promotion monitoring are rehearsed and evidence-producing.

# 18. RACI
| Role | RACI | Responsibility |
| --- | --- | --- |
| Solutions Architecture Office / IT Head | A | Owns architecture intent, final governance interpretation, and ARB/CAB readiness. |
| Mortgage Product Owner | A/R | Owns business journey, acceptance criteria, user value, and domain accuracy. |
| Software Development Lead | R | Owns implementation quality, boundaries, generated clients, MicroFunction integration, and PR/MR delivery. |
| Frontend Lead | R | Owns workspace renderer, components, accessibility, responsive behavior, and frontend telemetry. |
| Backend Lead | R | Owns APIs, MicroFunctions, outbox, workflows, policy integration, and adapters. |
| Security Architecture | A/R | Owns OPA/SBAC/ABAC, abuse cases, DAST, secrets hygiene, model route eligibility, and fail-closed controls. |
| DevSecOps Lead | R | Owns pipeline gates, evidence pack, GitNexus, scans, SBOM/provenance, and promotion automation. |
| QA/SDET | R | Owns unit, contract, E2E, accessibility, replay, resilience, and regression test evidence. |
| DBA / Data Governance | R | Owns Flyway, RLS, schemas, seed data, retention, and database evidence. |
| SRE / Operations | R | Owns dashboards, alerts, runbooks, incident readiness, and hypercare. |
| Internal Audit | C/I | Reviews AVCI completeness, evidence traceability, and control testability. |

# 19. AVCI Compliance Summary
| AVCI Property | Evidence in Mortgage Experience Pack |
| --- | --- |
| Attributable | Every block, screen, API, event, MicroFunction, policy, workflow, AI capability, artifact, config, and evidence record has owner, version, source, approval, and responsible role. |
| Verifiable | Behavior is proven by contracts, unit/component/E2E tests, OPA tests, Flyway checks, DAST, accessibility, replay, resilience lab, GitNexus, dashboards, and PR/MR evidence. |
| Classifiable | Data, prompts, artifacts, telemetry, events, documents, fields, blocks, screens, and APIs declare classification ceilings, handling rules, retention, and redaction. |
| Improvable | Usage, errors, policy denials, incidents, DAST findings, DLQ/replay outcomes, user feedback, and telemetry produce governed improvement candidates with human approval and rollback. |

# 20. Open Issues and Reconciliation Items
| Item | Issue | Severity | Owner / Register |
| --- | --- | --- | --- |
| AIRA-045-REC-001 | Confirm final pack numbering because Document 45 exists both as PoC2 DevSecOps and Mortgage Experience Pack in different source groups. | High | Register 00D / Revision Control Matrix |
| AIRA-045-REC-002 | Confirm exact mortgage data model table names, external adapters, and record retention class before physical implementation. | Medium | DBA / Data Governance |
| AIRA-045-REC-003 | Confirm whether payment processing is advisory/request-only for the PoC or integrated with an approved payment adapter in later phases. | High | Product Owner / Security / CAB |
| AIRA-045-REC-004 | Confirm official title-release business authority, maker-checker path, legal hold checks, and retention requirements before production use. | High | Legal / Title Operations / CAB |
| AIRA-045-REC-005 | After this revision, update the master cross-reference matrix so Documents 41, 42, 45, 46-61, and 57 point to this v1.1 reference implementation. | Medium | Solutions Architecture Office |

# Appendix A - Reference Artifact Checklist

experience/packs/mortgage-experience-pack-v1.1.yaml

experience/blocks/mortgage-application-block.yaml

experience/blocks/kyc-document-upload-block.yaml

experience/blocks/payment-schedule-block.yaml

experience/blocks/title-release-block.yaml

screens/mortgage-dashboard.yaml and related screen templates

api/openapi/aira-mortgage-workspace-api-v1.yaml

api/asyncapi/aira-mortgage-events-v1.yaml

schemas/avro/mortgage/*.avsc

policy/opa/mortgage.rego and policy tests

microfunctions/mortgage/*.yaml

evidence/evidence-profiles/mortgage-experience-evidence.yaml

tests/accessibility, e2e, contract, policy, replay, resilience, and observability packs

docs/PR-MR-AVCI-mortgage-pack-template.md

