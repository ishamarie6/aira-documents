---
title: "API and Integration Contract Standard"
doc_id: "AIRA-15"
version: "v2.2"
status: "revised"
category: "API and integration contracts"
source_docx: "AIRA_15_API_and_Integration_Contract_Standard_v2.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 15-api-integration-contracts
  - revised
  - aira-15
---



# API and Integration Contract Standard



AIRA

AI-Native Enterprise Platform

API and Integration Contract Standard

v2.2 Revised

Contract-First APIs | AsyncAPI | Kafka | Avro | CloudEvents | Outbox/Inbox | Idempotency | Dynamic Workspace | MicroFunctions | Evidence
| Property | Value |
| --- | --- |
| Document ID | AIRA-DOC-015 |
| Canonical Filename | AIRA_15_API_and_Integration_Contract_Standard_v2.2_Revised.docx |
| Version | v2.2 - Dynamic Workspace, MicroFunction, Eventing, Evidence, Runtime Toggle, and System Builder Alignment Update |
| Supersedes | 15-AIRA_API_and_Integration_Contract_Standard_v2.1_Aligned.docx |
| Companion Guide | 15A-AIRA_API_Governance_and_Contract_First_Implementation_Guide_v1.1 and future v1.2 update |
| Classification | INTERNAL CONFIDENTIAL |
| Status | DRAFT FOR ARCHITECTURE REVIEW BOARD / INTEGRATION GOVERNANCE / CAB APPROVAL |
| Owner | Solutions Architecture Office / Enterprise Architecture |
| Co-Owners | API Architecture; Integration Lead; DevSecOps Lead; Security Architecture; Software Development Lead; DBA; QA/SDET; Platform Engineering; SRE; AI Governance; Internal Audit |
| Review Cadence | Quarterly; unscheduled on material API, event, schema, gateway, MicroFunction, Dynamic Workspace, AI agent, evidence, security, model-route, or provisioning change |
| Evidence Path | OpenKM Tier-0 / AIRA / Architecture / API-Integration-Contracts / v2.2/ |

Discipline First - Automation Second - Intelligence Third - AVCI Always

# Mandatory Contract Statement

No AIRA API, event, schema, gateway route, widget action, MicroFunction trigger, System Builder output, AI agent tool call, provisioning request, or integration adapter may be implemented, generated, consumed, promoted, or exposed unless its contract is approved, versioned, secured, observable, testable, reversible, and tied to AVCI evidence. Runtime behavior must not be inferred from code alone; the contract is the governed boundary and evidence anchor.

# Static Table of Contents

1. Executive Summary and v2.2 Update Verdict

2. Purpose, Scope, Authority, and Source Alignment

3. Contract-First Governance Model

4. OpenAPI REST and Gateway Contract Rules

5. AsyncAPI, Kafka, Avro, CloudEvents, Outbox, Inbox, DLQ, and Replay Rules

6. MicroFunction, Dynamic Workspace, Workflow, and System Builder Integration

7. Security, Classification, SBAC, OPA, and Model-Route Enforcement

8. Error, Idempotency, Pagination, Concurrency, and Schema Evolution

9. Observability, Runtime Toggles, Evidence Correlation, and Trace Reconstruction

10. CI/CD Gates, GitNexus, Testing, Release, and Continuous Improvement

11. RACI, Roadmap, Acceptance Criteria, and AVCI Summary

# 1. Executive Summary and v2.2 Update Verdict

AIRA is contract-first. Version 2.2 updates the API and Integration Contract Standard so contracts govern not only REST and external integration, but also Dynamic Workspace widget actions, MicroFunction execution, AsyncAPI events, Kafka/Avro/CloudEvents, evidence ingestion, System Builder candidate generation, AI agent tool actions, DevSecOps provisioning, and Auto-Heal/Auto-Learn/Auto-Improve candidate loops.
| v2.2 Alignment Area | Required Result |
| --- | --- |
| Dynamic Workspace | Every widget action, workspace resolver call, admin builder change, dashboard query, and AI panel action binds to an approved backend contract and policy decision. |
| MicroFunction Runtime | REST, Kafka, workflow, batch, and UI triggers enter the MicroFunction envelope through typed contracts; business steps do not bypass the envelope. |
| Eventing Foundation | Kafka topics, Avro schemas, CloudEvents envelopes, outbox/inbox records, idempotent consumers, retry, DLQ, and replay are contract-governed. |
| DevSecOps Evidence | Contracts are linted, tested, diffed, security-checked, observed, and packaged into PR/MR and release evidence. |
| AI-native Governance | System Builder and agents may draft or recommend contracts, but activation requires maker-checker review, OPA/SBAC policy, CI/CD gates, and AVCI evidence. |
| Runtime Flexibility | Telemetry/logging/debug toggles may be configurable, but the contract defines safe bounds, audit requirements, classification, rollback, and performance guardrails. |

# 2. Purpose, Scope, Authority, and Source Alignment

This standard defines mandatory contract rules for all AIRA boundary-crossing behavior. It preserves the parent-policy role of Document 15 while requiring its implementation companion, Document 15A, to follow the same updated controls. When this standard and any companion guide conflict, the stricter AIRA control governs and the issue must be logged as an AVCI reconciliation item.
| Contract Family | Examples | Governing Output |
| --- | --- | --- |
| REST and Gateway | Backend APIs, evidence intake, admin APIs, Dynamic Workspace APIs, agent registry APIs, provisioning APIs. | OpenAPI 3.x contract, generated client/server stubs where useful, security schemes, Problem Details, tests, evidence. |
| Events and Messaging | Kafka topics, domain events, audit/evidence events, System Builder lifecycle, workflow state, agent lifecycle. | AsyncAPI, Avro or JSON Schema, CloudEvents envelope, schema registry, topic registry, DLQ/replay runbook. |
| MicroFunction Transactions | Synchronous, asynchronous, workflow, batch, and AI-assisted MicroFunction executions. | MicroFunctionDesignRecord, input/output schema, idempotency profile, error policy, evidence mapping, step contract. |
| Dynamic Workspace | Widget action, layout save, template publish, dashboard query, AI assistant panel, admin builder action. | Backend capability contract, OPA decision input schema, frontend generated client, telemetry/evidence schema. |
| AI and System Builder | Requirement intake, evidence intake, candidate artifact, agent skill/tool action, model route, provisioning request. | Contract-first intake schema, OpenAPI/AsyncAPI/manifest, guardrail/model-route metadata, approval evidence. |

# 3. Contract-First Governance Model

AIRA contract-first governance is a lifecycle, not a documentation preference. It starts at intake and ends only after runtime evidence proves that the contract behaves safely under normal, failure, replay, abuse, and rollback conditions.

1. Classify the request, source, owner, bounded context, environment, data handling, and risk tier.

2. Select the contract family: OpenAPI, AsyncAPI, Avro/JSON Schema, CloudEvents, MicroFunction, workflow, policy, agent, evidence, or provisioning manifest.

3. Generate or update the contract draft before code or configuration generation.

4. Run lint, schema compatibility, security, policy-as-code, architecture, DAST/smoke, and observability checks.

5. Create implementation only after contract acceptance, and keep generated code subordinate to the approved contract.

6. Promote through PR/MR maker-checker review, CI/CD gates, GitNexus analysis, release evidence, CAB/ARB where applicable, and post-promotion monitoring.
| Non-Negotiable Rule | Rejected Pattern |
| --- | --- |
| Contract before code | Controller, Kafka producer, UI widget, workflow task, or agent tool action exists without an approved contract. |
| Contract before generation | System Builder jumps from prompt to code, schema, policy, or provisioning artifact without a contract draft and validation evidence. |
| Contract as boundary | Domain logic imports gateway, Kafka, database, model provider, Redis, or vendor classes directly. |
| Contract as evidence anchor | PR/MR lacks contract diff, compatibility result, security decision, test evidence, and rollback path. |
| Contract as reversible asset | Breaking changes lack versioning, deprecation, migration, replay, dual-run, rollback, or consumer sign-off. |

# 4. OpenAPI REST and Gateway Contract Rules

OpenAPI governs all synchronous APIs, gateway-routed services, command endpoints, query endpoints, evidence intake, admin operations, System Builder endpoints, Dynamic Workspace capability calls, and AI agent registry APIs.
| OpenAPI Area | Mandatory Rule | Evidence |
| --- | --- | --- |
| Path and versioning | Use bounded-context base paths such as /api/{context}/v{major}/{resource}; breaking changes require major version or approved compatibility waiver. | OpenAPI diff, compatibility report, consumer migration plan. |
| Security scheme | OIDC/OAuth2, scopes, tenant, subject, classification, SBAC skills, and OPA package references documented. | Policy test, security smoke, authorization matrix. |
| Idempotency | Mutating POST/PATCH/command APIs require Idempotency-Key or approved natural idempotency profile. | Duplicate-submit test and replay evidence. |
| Safe response | Use Problem Details style responses with AIRA error code, trace/request reference, safe message, and no stack trace/secrets/PII. | Error contract test and log redaction test. |
| Generated clients | Frontend, Dynamic Workspace, and service clients are generated or validated from accepted contracts. | Generated client hash and CI check. |
| Evidence linkage | Governed changes return trace_id, request_id, evidence_ref, status tracking reference, and classification where applicable. | Evidence record and audit sample. |

# 5. AsyncAPI, Kafka, Avro, CloudEvents, Outbox, Inbox, DLQ, and Replay Rules

Events are governed contracts, not logs. Every producer, consumer, topic, schema, retry path, DLQ entry, replay request, and audit/evidence event must be declared, tested, observable, and reversible.
| Event Artifact | Mandatory Fields / Controls | Validation Gate |
| --- | --- | --- |
| AsyncAPI | Topic/channel, producer, consumer, security, classification, lifecycle status, schema version, owner, retention, replay policy. | AsyncAPI lint, lifecycle review, consumer compatibility. |
| Avro / JSON Schema | Schema namespace, version, compatibility rule, required fields, default values, deprecation handling, schema registry metadata. | Schema registry compatibility and evolution test. |
| CloudEvents envelope | id, source, type, subject, time, datacontenttype, dataschema, trace_id, correlation_id, causation_id, classification, evidence_ref where applicable. | Envelope validation and trace propagation test. |
| Outbox | Business mutation and event publication intent committed atomically with trace_id, transaction_id, evidence_ref, and status. | Outbox integration test and failure injection. |
| Inbox / idempotent consumer | Duplicate-safe and replay-safe consumer state, message hash, processed status, retry count, and outcome evidence. | Duplicate delivery, replay, and poison-message tests. |
| Retry / DLQ / replay | Bounded retries, backoff, poison parking, replay approval, synthetic replay test, and runbook evidence. | DLQ/replay runbook dry-run and dashboard evidence. |

# 6. MicroFunction, Dynamic Workspace, Workflow, and System Builder Integration
| Integration Point | Contract Requirement | AIRA Boundary |
| --- | --- | --- |
| MicroFunction trigger | Each transaction has input schema, output schema, step contract, idempotency profile, policy decision input, error path, and evidence mapping. | Business functions execute only at STP-BUS-* or rule/DMN steps behind ports/adapters. |
| Dynamic Workspace widget | Widget actions bind to backend capability_code, OpenAPI operationId, OPA policy_ref, classification ceiling, telemetry profile, and evidence_ref. | Frontend renders and invokes; backend authorizes and executes. |
| Admin Builder/template | Template publish, activation, rollback, and retirement use contract-governed APIs and maker-checker workflow. | No UI-generated behavior becomes authoritative until approved backend configuration is active. |
| Flowable/Temporal | Human task, approval, saga, signal, compensation, and timeout events have contracts and trace/evidence mapping. | Flowable handles human approval; Temporal handles durable machine orchestration where applicable. |
| System Builder | Intake, analysis, recommendation, generation, validation, PR/MR, and promotion are expressed as contract families. | System Builder proposes and drafts; human and policy gates approve. |

# 7. Security, Classification, SBAC, OPA, and Model-Route Enforcement

Contracts must make security explicit. A secure implementation cannot rely on hidden framework defaults or undocumented gateway behavior. All protected actions must have policy inputs, safe outputs, redaction rules, telemetry controls, and failure behavior defined.
| Control | Required Contract Metadata | Fail-Closed Condition |
| --- | --- | --- |
| Classification | x-aira-classification, data categories, redaction, retention, retrieval/model-route eligibility. | Missing or lower-than-source classification blocks promotion. |
| SBAC / OPA | Required skill_code, scope, tenant, environment, resource, action, policy package/version, decision evidence. | Missing deny/allow decision blocks protected action. |
| Secrets and sensitive data | No secret values in examples, schemas, logs, screenshots, generated clients, or evidence. | Secret scan, redaction test, or review failure blocks merge. |
| AI model route | LiteLLM alias, guardrail policy, classification ceiling, retrieval eligibility, evidence capture. | Direct model provider call or unapproved route blocks merge. |
| Abuse and authenticated DAST | Auth flows, tenant boundaries, authorization failures, rate limits, and unsafe input cases represented in tests. | Critical/high unapproved finding blocks promotion. |

# 8. Error, Idempotency, Pagination, Concurrency, and Schema Evolution
| Concern | Mandatory Standard | Evidence |
| --- | --- | --- |
| Error model | Problem Details style with AIRA error code, safe message, trace/request reference, and classification-aware detail suppression. | Negative contract tests and safe response samples. |
| Idempotency | Idempotency key, request hash, response hash, reserve/complete/expire state, natural idempotency exception where approved. | Duplicate request and timeout/retry tests. |
| Pagination/filtering | Stable sort, limit bounds, cursor or page token rules, allowed filters, tenant/classification controls. | Contract tests and abuse tests. |
| Concurrency | row_version, optimistic lock, selective pessimistic lock, retry policy, conflict response, and compensation rules. | Concurrent update and heavy-transaction tests. |
| Schema evolution | Backward-compatible additions preferred; breaking changes require versioning, deprecation, dual-run or migration plan. | Compatibility diff and consumer sign-off. |

# 9. Observability, Runtime Toggles, Evidence Correlation, and Trace Reconstruction

Every contract must be observable without leaking secrets, tokens, raw PII, prompts, embeddings, customer documents, or excessive high-cardinality labels. Runtime toggles are allowed for performance protection only when bounded by policy, audit, and safe default settings.
| Signal / Toggle | Contract Requirement | Evidence |
| --- | --- | --- |
| Trace | trace_id, span context, operationId/event type, bounded context, policy decision, MicroFunction transaction code where applicable. | OpenTelemetry trace sample and trace reconstruction review. |
| Logs | Structured Log4j2 JSON logs with safe event category, outcome, trace_id, error code, and redacted fields. | Log sample and redaction test. |
| Metrics | Latency, throughput, error rate, policy denial, Kafka lag, DLQ count, replay count, schema errors, contract drift. | Grafana dashboard or metric query. |
| Audit/evidence | evidence_ref, owner, source_ref, classification, verification evidence, reversibility, improvement path. | Evidence manifest and audit record. |
| Runtime toggles | Sampling, debug fields, log level, tracing depth, widget telemetry, DAST scope, and replay dry-run flags have owner, TTL, policy, audit, and rollback. | Toggle change record and expiration check. |

# 10. CI/CD Gates, GitNexus, Testing, Release, and Continuous Improvement
| Gate | Required Check | Blocking Rule |
| --- | --- | --- |
| Contract lint | OpenAPI/AsyncAPI/schema syntax, naming, metadata, classification, examples, and compatibility. | Invalid or incomplete contract blocks merge. |
| Contract tests | Provider/consumer tests, generated client validation, mock/stub tests, error cases, idempotency, auth failure cases. | Missing tests for changed contract blocks merge. |
| Security tests | SAST, SCA, secrets, OPA policy, authenticated DAST for protected APIs, log redaction. | Critical/high findings require fix or formal waiver. |
| Architecture fitness | No direct DB/Kafka/Redis/model/provider calls from domain or STP-BUS; controllers remain thin; ports/adapters enforced. | Boundary violations block merge. |
| GitNexus evidence | Read-only impact analysis, affected tests, code map, architecture drift, security-sensitive file impact. | GitNexus is advisory only and cannot replace tests or review. |
| Release evidence | Contract diff, compatibility status, API/event registry update, rollback/deprecation, dashboards, runbook update, CAB where applicable. | Promotion blocked without AVCI evidence. |

Auto-Heal, Auto-Learn, and Auto-Improve may detect contract drift, schema incompatibility, replay failure, telemetry gaps, or missing tests. They may produce candidates, test plans, contract drafts, PRs, or knowledge updates. They must not silently mutate contracts, schemas, production APIs, topics, policies, or runtime behavior.

# 11. RACI, Roadmap, Acceptance Criteria, and AVCI Summary
| Activity | EA/API | Dev Lead | DevSecOps | Security | DBA | QA/SDET | SRE | AI Gov | Audit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contract policy and versioning | A | R | C | C | C | C | C | C | I |
| OpenAPI/AsyncAPI/schema authoring | A | R | C | C | C | R | C | C | I |
| Security and OPA/SBAC checks | C | R | C | A | I | R | C | C | I |
| CI/CD and GitNexus evidence | C | R | A | C | C | R | C | C | I |
| Release compatibility and rollback | A | R | C | C | C | R | R | C | I |
| Audit/control testing | C | C | C | C | C | C | C | C | A |
| Phase | Milestone | Acceptance Criteria |
| --- | --- | --- |
| R0 | Contract repository baseline | OpenAPI, AsyncAPI, schemas, examples, lints, CODEOWNERS, PR template, and evidence folders exist. |
| R1 | Gateway and API baseline | OIDC/SBAC/OPA, Problem Details, idempotency, generated client, and contract tests pass. |
| R2 | Eventing foundation | Kafka/Avro/CloudEvents/outbox/inbox/DLQ/replay contracts and tests pass. |
| R3 | Dynamic Workspace and MicroFunction binding | Widget actions and MicroFunction transactions are contract-bound and policy-filtered. |
| R4 | CI/CD and evidence maturity | Contract diff, security, architecture, GitNexus, observability, and release evidence are automated. |
| R5 | Operational readiness | Dashboards, runbooks, replay tests, DAST scope, runtime toggles, and improvement loops are approved. |
| AVCI Property | v2.2 Evidence |
| --- | --- |
| Attributable | Every contract has owner, bounded context, source_ref, version, approver, status, and responsible role. |
| Verifiable | Contracts have lint, compatibility, unit/component/contract, policy, security, observability, replay, and release evidence. |
| Classifiable | Contracts carry classification, redaction, retention, model-route eligibility, telemetry handling, and evidence handling rules. |
| Improvable | Contract drift, incidents, findings, consumer feedback, and telemetry become backlog, ADR/TDL, runbook, test, or Auto-Improve candidates. |

