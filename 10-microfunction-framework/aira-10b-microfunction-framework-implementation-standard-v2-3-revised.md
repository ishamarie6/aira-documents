---
title: "MicroFunction Framework Implementation Standard"
doc_id: "AIRA-10B"
version: "v2.3"
status: "revised"
category: "MicroFunction framework"
source_docx: "AIRA_10B_MicroFunction_Framework_Implementation_Standard_v2.3_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 10-microfunction-framework
  - revised
  - aira-10b
---



# MicroFunction Framework Implementation Standard



AIRA
AI-Native Enterprise Platform

AIRA MicroFunction Framework Implementation Standard

Runtime Engine | Catalog Schema | Execution Envelope | Java 25 Implementation Controls | Cross-Cutting Capability Enforcement
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-010B |
| Version | v2.3 Revised - Implementation Control, Runtime Envelope, Cross-Cutting Capability, and Evidence Update |
| Status | Draft for Architecture Review Board / CAB / Engineering Team Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; DBA; Platform Engineering; AI Engineering; SRE / Operations; Internal Audit |
| Supersedes | 10B-AIRA_MicroFunction_Framework_Implementation_Standard_v2.1_Aligned.docx, upon approval |
| Source Reviewed | AIRA_10B_MicroFunction_Framework_Implementation_Standard_v2_2_Review_and_Revised.docx |
| Parent Standard | AIRA-DOC-010 MicroFunction Framework v3.4 Revised |
| Direct Companion | AIRA-DOC-010A MicroFunction Design and Development Guide v2.4 Revised |
| Primary Role | Implementation authority for runtime engine, package boundaries, Java contracts, configuration schema, execution envelope, adapters, tests, telemetry, and evidence gates. |

Mandatory Practice Statement

AIRA MicroFunction implementation is not complete when Java code runs. It is complete only when the runtime engine, catalogs, configuration validation, execution envelope, adapters, policies, tests, telemetry, evidence hooks, pipeline gates, resilience behavior, and rollback paths prove that every transaction is configurable, secure, observable, retry-safe, duplicate-safe, policy-governed, human-accountable where required, and AVCI-compliant.

# Table of Contents Placeholder

Insert a Microsoft Word automatic Table of Contents here before final publication. Recommended setting: show levels 1 to 3. Update all fields after final approval and before distribution.

# 1. Executive Summary

This v2.3 revision converts the v2.2 candidate into the implementation companion to the completed AIRA-DOC-010 v3.4 parent framework and AIRA-DOC-010A v2.4 design guide. It keeps the direction of the uploaded source while correcting parent references, tightening implementation gates, and making the required cross-cutting controls executable by developers, System Builder, CI/CD, and reviewers.

The operating position is simple: a MicroFunction implementation that passes only functional tests remains a draft. It becomes AIRA-ready only when architecture boundaries, security, contracts, observability, idempotency, replay, evidence, and rollback are proven.

# 2. Alignment Corrections Applied
| Correction Area | v2.3 Treatment |
| --- | --- |
| Parent authority corrected | From 10 v3.3 candidate to 10 v3.4 Revised. 10B implements the parent; it does not redefine it. |
| Direct companion corrected | From 10A v2.3 candidate to 10A v2.4 Revised. 10B translates the approved design procedure into build rules. |
| Review status corrected | 10B becomes completed / revised in this workstream. The next MicroFunction document is 10C. |
| Foundation handling | References to 01A, 01, 01B, 02, 03, 04, 05, 06, 07, and 07B are aligned to the recently revised foundation outputs. 08, 08A, and 09 remain companion dependencies unless separately confirmed as revised. |
| Cross-cutting addendum handling | The DevSecOps, API/eventing, observability, resilience, security, runtime toggle, and Auto-* controls are integrated into the implementation standard rather than left as a loose addendum. |

Figure 1. MicroFunction implementation control plane.

# 3. Purpose

This standard defines how AIRA implements the MicroFunction runtime engine, step contracts, catalog schema, configuration validation, execution envelope, adapters, telemetry, evidence hooks, DevSecOps gates, and runtime controls required for enterprise-grade, configuration-first transaction assembly.

# 4. Scope
| Scope Area | Treatment |
| --- | --- |
| In Scope | Runtime engine, step registry, catalog schema, configuration rows, runtime process assembly, validation, signature/hash verification, cache acceleration, execution envelope, standard steps, STP-BUS implementation, adapters, OPA/SBAC, outbox, observability, tests, evidence, runtime toggles, Auto-* candidate loops, and CI/CD gates. |
| Out of Scope | Unapproved process redesign, bypassing standard steps, direct production mutation, direct model/provider SDK calls, manual production DDL, frontend authorization authority, unmanaged Kafka publishing, AI approval of protected actions, and uncontrolled agents or tools. |

# 5. Authority and Precedence
| Level | Authority | Control Role |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance | Final authority for production-impacting runtime, security, data, workflow, AI, and exception decisions. |
| L1 | 01A, 01, 01B, 02 | Universal design, evidence, architecture, and conflict-resolution authority. |
| L2 | 10 MicroFunction Framework v3.4 | Parent MicroFunction runtime, catalog, governance envelope, and cross-cutting capability authority. |
| L3 | 10A / 10B / 10C / 10D / 10E | Design method, implementation details, sequence references, catalog entries, and generated backend service controls. |
| L4 | Repository code, Flyway, OpenAPI/AsyncAPI/Avro, OPA policy, CI/CD, telemetry, evidence packs | Executable implementation proof. May tighten but must not weaken the above standards. |

# 6. Implementation Principles
| Principle | Mandatory Implementation Meaning |
| --- | --- |
| Configure first | Transaction sequence, step bindings, parameters, policies, retry, timeout, compensation, evidence, and activation are versioned configuration whenever feasible. |
| Code only the business gap | New Java code belongs only in approved STP-BUS-* functions, adapters, or framework extensions when no standard function, rule, DMN, OPA policy, or configuration option satisfies the requirement. |
| Standard concerns are framework-owned | Receiving, correlation, validation, authorization, idempotency, audit, telemetry, outbox, error handling, response shaping, and guardrail execution are reusable standard functions. |
| Ports and adapters always | Database, Kafka, OpenKM, Redis/Valkey, Flowable, Temporal, Keycloak, Vault, LiteLLM, OPA, and external systems are accessed through explicit ports and adapters. |
| Evidence by construction | Every step execution produces or links evidence fields sufficient for reconstruction, audit, verification, rollback, and improvement. |
| Fail-safe execution | Missing identity, policy, classification, guardrail, audit, idempotency, evidence, or required runtime configuration blocks protected actions. |

# 7. Standard Repository and Package Layout

The implementation must use package boundaries that make dependency direction visible and testable. Exact repository names may differ, but the separation of responsibility must remain enforceable through architecture fitness functions.
| Package / Module | Required Responsibility |
| --- | --- |
| aira-mf-api | Public contracts, DTOs, OpenAPI/AsyncAPI generated types, problem/error contracts, and stable interfaces. No infrastructure implementation. |
| aira-mf-application | Runtime coordinator, use-case orchestration, execution envelope, validation services, policy request assembly, and publish-time validation. Depends on ports, not adapters. |
| aira-mf-domain | Typed MicroFunction contracts, domain rules, value objects, idempotency concepts, and bounded-context invariants. No Spring, DB, Kafka, UI, workflow engine, or provider SDK dependency. |
| aira-mf-adapters | PostgreSQL, Kafka, Redis/Valkey, OPA, Vault, Keycloak, Flowable, Temporal, OpenKM, LiteLLM, telemetry, and external system adapters. |
| aira-mf-config | Catalog seeders, runtime configuration schemas, validation rules, feature flags, policy bindings, and environment manifests. |
| aira-mf-test | Unit, component, contract, architecture fitness, failure injection, idempotency, replay, OPA, security, authenticated DAST, and evidence validation fixtures. |
| aira-mf-evidence | Evidence manifest templates, PR/MR evidence summaries, GitNexus reports, SBOM/provenance references, trace reconstruction references, and release readiness records. |

# 8. Authoritative Configuration and Schema Implementation

PostgreSQL remains authoritative for runtime configuration, catalog entries, activation state, audit records, idempotency records, policy references, evidence pointers, and outbox/inbox records. Redis/Valkey and Caffeine are acceleration layers only.
| Schema / Table | Mandatory Purpose |
| --- | --- |
| aira_mf.step_catalog | Registered standard and business MicroFunctions, category, owner, version, classification ceiling, idempotency profile, error policy, compensation policy, observability profile, and status. |
| aira_mf.txn_definition | Transaction code, version, bounded context, owner, status, classification, activation window, rollback/safe-disable path, and publish evidence reference. |
| aira_mf.txn_step_binding | Ordered step sequence, mandatory/conditional flag, parameter binding, policy binding, retry/timeout/compensation binding, and execution condition. |
| aira_mf.runtime_definition_hash | Signed or hash-verified runtime process definition, source config checksum, activation evidence, maker/checker/approver, and effective date. |
| aira_mf.idempotency_registry | Idempotency key, request hash, actor/tenant, transaction code, status, prior response pointer, expiry, and duplicate detection result. |
| aira_outbox.event_outbox | Transactional outbox event intent, aggregate, event type, CloudEvents attributes, schema reference, status, retry count, DLQ link, and trace/evidence reference. |
| aira_inbox.processed_event_registry | Consumer idempotency record, event id, source, schema version, processing status, replay status, error classification, and evidence reference. |
| aira_audit.step_execution_audit | Immutable step execution record with trace_id, span_id, actor, transaction, step, duration, policy result, classification, outcome, error, and evidence_ref. |
| aira_policy.policy_decision_log | OPA/SBAC decision input hash, policy version, decision, reason code, risk tier, approval requirement, and evidence reference. |

Flyway rule: all schemas, tables, views, indexes, constraints, RLS policies, seed data, and reference data must be created and changed through Flyway or the approved migration workflow. Manual production DDL is prohibited.

# 9. Runtime Assembly, Signature, Cache, and Activation
| Assembly Stage | Implementation Requirement |
| --- | --- |
| Retrieve authoritative configuration | Load transaction definition, step bindings, policy references, retry/error/compensation profiles, feature flags, and evidence profile from PostgreSQL. |
| Validate mandatory controls | Reject activation when identity, classification, validation, authorization, idempotency, audit, observability, error handling, compensation, or evidence controls are missing for protected flows. |
| Construct RuntimeProcessDefinition | Assemble immutable runtime view with step sequence, typed contracts, parameter bindings, required ports, policy references, telemetry profile, and rollback/safe-disable metadata. |
| Sign or hash runtime definition | Create deterministic hash or signature and store activation evidence with maker/checker/approver references. |
| Cache for acceleration only | Caffeine L1 and Redis/Valkey L2 may cache validated definitions. Cache miss, rebuild, or invalidation must not change correctness. |
| Activate through governed path | Activation requires tests, configuration validation, policy results, evidence manifest, rollback/safe-disable path, and required approvals. |

Figure 2. Standard runtime execution flow through the MicroFunction envelope.

# 10. Execution Envelope
| Envelope Area | Mandatory Fields / Behavior |
| --- | --- |
| Identity and actor | actor_id, actor_type, tenant_id, org_unit, roles, skills, agent_id where applicable, session reference, and classification eligibility. |
| Correlation | trace_id, span_id, request_id, correlation_id, causation_id, transaction_execution_id, step_execution_id, and evidence_ref. |
| Policy and classification | classification, data-handling rule, OPA decision reference, SBAC skill decision, guardrail result, approval route where required. |
| Idempotency and concurrency | idempotency key, request hash, concurrency key, lock strategy, duplicate detection, retry attempt, and replay state. |
| Resilience | timeout budget, retry policy, backoff, jitter, circuit-breaker state, bulkhead group, fallback/compensation, and DLQ reference. |
| Observability | structured log context, OTel span attributes, metric dimensions, audit profile, Sentry release context, dashboard labels, and redaction state. |
| Result | typed output, safe response metadata, error classification, outbox references, audit references, evidence references, and improvement candidate flag. |

# 11. Standard Step and STP-BUS Implementation Rules
| Step Category | Implementation Rule |
| --- | --- |
| STP-RCV / STP-COR | Receive requests and establish correlation. Controllers and adapters remain thin; no business decisions or persistence logic. |
| STP-SES / STP-CLS / STP-SEC | Resolve actor, tenant, classification, authorization, SBAC, OPA, and approval posture before business execution. |
| STP-VAL | Perform schema, contract, and business-input validation. Reject invalid input safely and record evidence. |
| STP-IDEMP / STP-CONCUR | Apply idempotency, deduplication, locking, optimistic concurrency, replay protection, and duplicate effect prevention. |
| STP-BUS-* | Execute one bounded business responsibility only. No direct controller response, database driver, Kafka client, audit writer, model provider, cache manipulation, or cross-context write. |
| STP-OUTBOX / STP-EVT | Persist outbox intent transactionally; publish through approved adapter after commit; validate CloudEvents/Avro where applicable. |
| STP-AUD / STP-OBS | Emit immutable audit and telemetry evidence without secrets, raw PII, raw prompts, or high-cardinality metric labels. |
| STP-ERR / STP-COMP / STP-DLQ | Classify failure, apply retry/compensation/DLQ/human review, and produce safe response and remediation evidence. |
| STP-AI / STP-RAG / STP-TOOL | Route AI/model/tool action through LiteLLM, guardrails, Harness, SBAC, OPA, trust/risk gates, and human approval where required. |

# 12. Cross-Cutting Capability Implementation Matrix
| Capability Area | Mandatory Implementation Coverage |
| --- | --- |
| DevSecOps Pipeline, Security Gates, Evidence Pack, and GitNexus | CI/CD must run build, unit/component/contract/security/architecture tests, SAST, authenticated DAST where applicable, SCA, secret scan, SBOM, provenance, container scan, OPA/Conftest, GitNexus impact analysis, evidence manifest validation, and PR/MR AVCI summary. |
| OpenAPI, AsyncAPI, Kafka, Avro, CloudEvents, Outbox, Schema Evolution, Idempotent Consumers, DLQ, Replay | All boundary-crossing APIs/events require contracts before implementation. Mutating REST commands use idempotency. Event publication uses transactional outbox. Kafka consumers are idempotent and replay-safe. DLQ and replay runbooks must exist before operational reliance. |
| Observability, Log4j2, OpenTelemetry, Sentry, Loki, Tempo, Grafana | Implement structured logging, trace/metric/log correlation, Sentry error/release context, Loki logs, Tempo traces, Grafana dashboards, alerting, redaction, and trace reconstruction. |
| Concurrency, Heavy Transaction, Idempotency, Outbox, and Resilience Lab | Test optimistic locking, lock strategy, idempotency registry, outbox race conditions, consumer replay, backpressure, timeouts, circuit breakers, bulkheads, failure injection, and DLQ. |
| Auto-Heal, Auto-Learn, Auto-Improve Candidate Loop | Issue detection may assemble evidence and generate candidate fixes, tests, policy updates, runbook updates, or knowledge proposals. No direct production mutation or self-approval. |
| OPA/SBAC, Abuse Cases, Authenticated DAST, Secure APIs, Secrets Hygiene, Remediation Evidence | Protected APIs and MicroFunctions require policy coverage, abuse-case tests, authenticated DAST for staged services, safe errors, secret scanning, credential hygiene, and remediation evidence. |

# 13. API, Eventing, Outbox, DLQ, and Replay Implementation
| Implementation Item | Required Rule |
| --- | --- |
| OpenAPI | Required for synchronous REST commands and queries before implementation. Must define security scheme, problem response, error codes, idempotency headers, classification, examples, and contract tests. |
| AsyncAPI | Required for Kafka and other event topics. Must define topics, producers, consumers, payload schema, headers, CloudEvents attributes, security, retry, DLQ, and replay posture. |
| Avro / Schema Evolution | Structured events require versioned schemas and compatibility tests. Breaking changes require ADR/TDL, migration strategy, dual-run or deprecation plan, and consumer approval. |
| CloudEvents | Event metadata carries id, source, type, specversion, time, subject where applicable, correlation_id, causation_id, traceparent, classification, and evidence_ref where permitted. |
| Transactional Outbox | State change and event intent commit atomically. Business logic does not call Kafka directly. Publisher adapters drain outbox after commit with retry and DLQ behavior. |
| Idempotent Consumer | Consumers record processed events by event id/source/schema version and safely handle duplicate delivery, replay, partial failure, and reprocessing. |
| DLQ and Replay | DLQ routing requires error classification, reason code, payload handling policy, redaction, owner, replay eligibility, approval path, and evidence record. |

# 14. Observability, Audit, Error Monitoring, and Runtime Toggles
| Area | Implementation Requirement |
| --- | --- |
| Structured Log4j2 logging | Use structured logs with trace_id, request_id, transaction_code, step_code, outcome, error_code, classification, and redaction state. Never log passwords, tokens, secrets, raw PII, raw prompts, embeddings, or unrestricted payloads. |
| OpenTelemetry | Propagate trace context across frontend, gateway, backend, MicroFunction runtime, database adapter, Kafka publisher/consumer, workflow engine, and AI gateway where applicable. |
| Sentry | Capture unhandled exceptions, release context, environment, issue linkage, sanitized stack summaries, and regression evidence without leaking restricted data. |
| Loki and Tempo | Logs and traces must be queryable by correlation and evidence fields for trace reconstruction. Retention and access follow classification policy. |
| Grafana dashboards and alerting | Critical MicroFunction health, latency, error rate, policy denial, DLQ, replay, idempotency conflict, outbox lag, and Auto-* candidate metrics must be visible. |
| Runtime toggles | Diagnostic verbosity, sampling rate, feature flags, and non-critical debug logs may be toggled through governed configuration. Mandatory audit, policy decisions, security events, idempotency records, outbox records, and critical errors must not be disabled. |

# 15. Concurrency, Heavy Transaction, Idempotency, and Resilience
| Control | Implementation Rule |
| --- | --- |
| Idempotency registry | All mutating commands, callbacks, replays, workflow signals, and tool actions must record idempotency or deterministic dedupe keys. |
| Optimistic concurrency | Use row_version, compare-and-set semantics, or transaction-boundary checks where state conflict is possible. |
| Locking strategy | Use scoped locks only when necessary, with timeout, owner, reason, expiry, and recovery behavior. |
| Heavy transaction handling | Use batching, pagination, chunking, backpressure, async handoff, outbox, and workflow partitioning for long-running or high-volume processing. |
| Retry safety | Retries must be bounded by timeout budget, backoff, jitter, idempotency, circuit-breaker state, and safe compensation. |
| Circuit breaker and bulkhead | Dependency failures must not cascade across bounded contexts or critical workflows. Isolation groups and fallbacks must be configured and tested. |
| Failure injection tests | Simulate downstream timeout, partial commit, duplicate delivery, transaction conflict, outbox backlog, DLQ, replay, and recovery. |

# 16. Security, OPA/SBAC, AI, and Secrets Enforcement
| Control | Implementation Rule |
| --- | --- |
| OPA/SBAC | Every protected action assembles OPA input with actor, skills, tenant, classification, action, resource, risk tier, environment, and evidence context. Deny by default. |
| Authenticated DAST | Staging/test APIs requiring identity must have authenticated DAST scripts using synthetic users and scoped credentials. Findings require remediation evidence or approved waiver. |
| Secrets hygiene | No secrets in source, logs, traces, screenshots, tests, prompts, or documentation. Use Vault or approved secret abstraction. Secret scanning is mandatory in CI. |
| Secure API behavior | No stack traces or internal provider details in responses. Use safe error profile and standard AIRA error codes. |
| AI gateway | AI/model access uses approved LiteLLM/model gateway routes and guardrails. Direct provider SDK calls from MicroFunction business logic are prohibited. |
| Tool actions | Agents and tools do not directly mutate Git, CI/CD, Kubernetes, database, workflow, secrets, or production. Tool actions route through Harness/SBAC/OPA and human approval where required. |

# 17. Auto-Heal, Auto-Learn, and Auto-Improve Implementation Controls
| Control | Implementation Rule |
| --- | --- |
| Detection | Allowed to read approved telemetry, test failures, CI evidence, security findings, DLQ records, incident records, and GitNexus analysis subject to classification and SBAC. |
| Evidence retrieval | Must collect source references, trace/log/audit/test/scan evidence, affected contracts, runtime configuration version, commit hash, and confidence score. |
| Candidate proposal | May draft root-cause hypothesis, candidate fix, test improvement, policy improvement, runbook update, or knowledge candidate. |
| Validation | Must run deterministic tests, affected contract tests, OPA/SBAC tests, security tests, architecture fitness, and regression checks before recommendation. |
| Human approval | Required for production-impacting, high-risk, Restricted, policy, security, data, workflow, model-route, or environment changes. |
| Prohibited | No direct production patch, direct DB edit, weakened policy, disabled guardrail, skipped tests, self-approval, or silent mutation. |

# 18. Java 25 / Spring Boot Reference Contract Rules
| Rule Area | Implementation Rule |
| --- | --- |
| MicroFunction interface | Typed input, typed output, execution envelope, policy context, idempotency context, evidence context, and deterministic error classification. |
| Dependency inversion | Business functions depend on ports, not adapter implementations, framework clients, database drivers, Kafka clients, or model SDKs. |
| Thin adapters | Controllers, Kafka listeners, workflow handlers, scheduled jobs, and tool endpoints adapt transport to application use cases and do not contain business logic. |
| Validation | DTO/schema validation occurs before business execution; domain invariants are enforced inside domain/application boundary. |
| Error handling | No swallowed exception. Error is classified, audited, linked to evidence, and mapped to safe response or compensation/DLQ/human review. |
| Generated code | System Builder or AI-generated implementation is draft until human-reviewed, tested, scanned, policy-checked, and accepted through PR/MR. |

# 19. Testing, Architecture Fitness, and CI/CD Evidence
| Test / Gate | Minimum Evidence |
| --- | --- |
| Unit tests | STP-BUS logic, policy input assembly, idempotency decisions, error classification, and domain invariants. |
| Component tests | Runtime assembly, cache miss/rebuild, step execution, outbox write, OPA adapter, telemetry emission, and evidence generation. |
| Contract tests | OpenAPI, AsyncAPI, Avro/schema compatibility, problem responses, idempotency behavior, and consumer compatibility. |
| Architecture tests | No domain-to-infrastructure dependency, no direct Kafka/DB/model provider, no controller business logic, bounded-context isolation, and ports/adapters compliance. |
| Security tests | OPA/Rego tests, SBAC negative tests, secrets scan, SAST/SCA, authenticated DAST where applicable, and abuse-case tests. |
| Resilience tests | Retry, timeout, circuit breaker, bulkhead, DLQ, replay, compensation, duplicate delivery, and concurrent execution tests. |
| Evidence tests | Evidence manifest, audit record fields, trace/log correlation, GitNexus impact output, SBOM/provenance, and PR/MR AVCI summary completeness. |

# 20. EDP-01 to EDP-20 Implementation Enforcement Matrix
| Principle | Implementation Enforcement |
| --- | --- |
| EDP-01 SOLID | Reject mixed responsibility, god functions, excessive coupling, and missing interfaces. |
| EDP-02 Clean Architecture | Domain/application packages cannot depend on frameworks, UI, persistence, workflow engines, or provider SDKs. |
| EDP-03 DDD / Bounded Contexts | Each STP-BUS belongs to one bounded context and cannot write another context schema directly. |
| EDP-04 Ports and Adapters | External dependencies use ports and adapters; direct clients in business logic are prohibited. |
| EDP-05 DRY/KISS/YAGNI | Reuse standard steps; avoid speculative framework code and duplicated plumbing. |
| EDP-06 Idempotency | Mutating, replay, callback, workflow, and tool actions prove duplicate-safe behavior. |
| EDP-07 Determinism | Builds, tests, migrations, config, prompts, and evidence are source-controlled and repeatable. |
| EDP-08 Fail-safe | Missing control dependency blocks protected action. |
| EDP-09 Human-in-the-loop | High-risk and production-impacting actions require named human approval. |
| EDP-10 Least Privilege / SBAC | Actors, services, agents, and tools receive only scoped skills and authority. |
| EDP-11 Separation of Duties | Maker/checker/approver/deployer/operator/auditor remain separable. |
| EDP-12 Observability | Trace, metrics, logs, audit, evidence, model/agent refs are emitted safely. |
| EDP-13 Policy as Code | OPA, admission, routing, guardrail, environment, and agent-tool policies are versioned artifacts. |
| EDP-14 Testability | Code, configuration, policies, prompts, adapters, workflows, and manifests are independently testable. |
| EDP-15 Secure by Design | Threat controls, secrets hygiene, classification, tenant isolation, and supply-chain controls are built in. |
| EDP-16 Resilience | Timeouts, retries, circuit breakers, bulkheads, fallback, DLQ, compensation, and recovery are explicit. |
| EDP-17 Fitness Functions | Automated checks validate boundaries, contracts, security, agents, provisioning, and evidence. |
| EDP-18 Progressive Autonomy | Automation advances only with evidence, trust, skill, risk tier, guardrails, and rollback controls. |
| EDP-19 Reversibility | Rollback, forward-fix, compensation, feature disablement, rebuild, or deactivation is documented. |
| EDP-20 AVCI | Every artifact is attributable, verifiable, classifiable, and improvable across lifecycle. |

# 21. Runtime Toggle and Performance Control Standard
| Toggle Area | Control |
| --- | --- |
| Allowed runtime toggles | Log verbosity, trace sampling percentage, debug diagnostic payloads, non-critical metric detail, feature flags, cache refresh mode, dashboard sampling, and synthetic probe frequency. |
| Restricted runtime toggles | OPA/SBAC, identity validation, classification handling, secrets redaction, audit, idempotency, outbox, DLQ routing, critical security logging, and critical error evidence may not be disabled for protected flows. |
| Approval requirement | Runtime toggles that change business behavior, security posture, evidence completeness, or production performance require owner approval, audit record, rollback, and post-change monitoring. |
| Performance rule | Performance tuning must reduce overhead by sampling, batching, async handoff, or aggregation; it must not remove accountability or reconstructability. |

# 22. Anti-Patterns and Rejection Rules
| Anti-Pattern | Required Response |
| --- | --- |
| Direct Kafka in STP-BUS | Reject. Use outbox and adapter publisher. |
| Direct database driver in domain function | Reject. Use repository port and adapter. |
| Controller contains business logic | Reject. Controller is a thin adapter. |
| AI/model SDK in business function | Reject. Use approved gateway, guardrails, and tool authorization. |
| Missing idempotency for mutating operation | Reject until idempotency, duplicate handling, and replay tests exist. |
| Missing telemetry or audit | Reject for protected or critical flows. |
| Manual production DDL | Reject. Flyway-only or approved migration workflow. |
| Security finding waived without evidence | Reject. Waiver requires owner, risk, expiry, compensating controls, and remediation plan. |
| Auto-Heal directly patches production | Reject. Candidate PR/runbook only unless controlled low-risk action is pre-approved through Harness/SBAC/OPA. |

# 23. Required Evidence and Definition of Done
| Evidence Area | Required Evidence |
| --- | --- |
| Code and configuration | Branch, commits, CODEOWNERS review, generated artifact list, runtime config diff, Flyway migration output, and catalog registration evidence. |
| Contracts and schemas | OpenAPI/AsyncAPI/Avro/JSON schema validation, compatibility report, examples, and generated clients where applicable. |
| Tests | Unit, component, contract, architecture, OPA/SBAC, security, resilience, failure injection, authenticated DAST where applicable, regression, and changed-line coverage as required. |
| Security | SAST/SCA/secrets/container scan, authenticated DAST evidence, abuse-case results, remediation/waiver record, and secrets hygiene confirmation. |
| Observability | Trace/log/metric/audit sample, dashboard link, Sentry issue/release context where applicable, Loki/Tempo query examples, and alert rule evidence. |
| Resilience | Idempotency proof, concurrency proof, outbox proof, DLQ proof, replay proof, retry/circuit/bulkhead proof, and compensation or rollback plan. |
| GitNexus and impact | Read-only impact analysis, affected files/tests/contracts, architecture drift signal, risk summary, and reviewer guidance. |
| AVCI and review | Owner, reviewer, classification, verification evidence, known limitations, improvement backlog, rollback/safe-disable path, and human approvals. |

Figure 3. Implementation evidence chain from design to promotion.

# 24. RACI
| Activity | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Runtime engine implementation | Platform Engineering / Backend Developers | Software Development Lead | Architecture, QA/SDET, Security, DBA | Engineering Team |
| Schema and Flyway changes | DBA / Backend Developers | DBA Lead | Architecture, Security, DevSecOps | Release stakeholders |
| OPA/SBAC and security gates | Security Architecture / DevSecOps | Security Lead | Development, QA/SDET | Internal Audit |
| CI/CD and evidence gates | DevSecOps | DevSecOps Lead | QA/SDET, Security, Architecture | Engineering Team |
| Production-impacting promotion | Change Owner | CAB | Architecture, Security, SRE, QA | Affected teams |
| Auto-* candidate acceptance | Domain Owner / Reviewer | Architecture or Product Owner as applicable | Security, QA, DevSecOps | Knowledge Steward / Internal Audit |

# 25. Review Queue Control Register
| Seq | File | Current | Recommended | Status | Next Step |
| --- | --- | --- | --- | --- | --- |
| 13 | 10-AIRA_MicroFunction_Framework_v3.1_Aligned.docx | v3.1 | v3.4 Revised | Completed / Revised | Use as parent for 10A/10B/10C/10D/10E |
| 14 | 10A-AIRA_MicroFunction_Design_and_Development_Guide_v2.1_Aligned.docx | v2.1 | v2.4 Revised | Completed / Revised | Use as design companion for 10B |
| 15 | 10B-AIRA_MicroFunction_Framework_Implementation_Standard_v2.1_Aligned.docx | v2.1 | v2.3 Revised | Completed / Revised | Proceed to 10C |
| 16 | 10C-AIRA_MicroFunction_Sequence_Diagrams_and_Mermaid_Reference_v2.1_Aligned.docx | v2.1 | v2.2 Revised recommended | Next for Review | Align diagrams with 10/10A/10B implementation controls |
| 17 | 10D-AIRA_MicroFunction_Standard_Function_Catalog_and_Assembly_Templates_v2.1_Aligned.docx | v2.1 | v2.2 Revised recommended | Pending | Review after 10C |
| 18 | 10E-AIRA_MicroFunction_Backend_Service_Generation_and_Runtime_Configuration_Standard_v1.1.docx | v1.1 | v1.2 Revised recommended | Pending | Review after 10D |

# 26. Change Log
| Version | Status | Summary |
| --- | --- | --- |
| v2.1 | Prior aligned baseline | Java 25 implementation and Pack 04 v1.2 alignment update. |
| v2.2 candidate | Uploaded source | Aligned with 10 v3.3 and 10A v2.3; added explicit cross-cutting implementation controls, runtime toggles, EDP enforcement, API/eventing, observability, concurrency, security hardening, Auto-* candidate loops, and evidence gates. |
| v2.3 Revised | This output | Corrects parent/companion references to 10 v3.4 and 10A v2.4, integrates cross-cutting controls into the body, tightens implementation gates, corrects the review queue, and adds final acceptance/rejection criteria. |

# 27. Acceptance Criteria

10B is approved as the implementation companion to AIRA-DOC-010 v3.4 and AIRA-DOC-010A v2.4.

Runtime engine and STP-BUS implementations enforce package boundaries, dependency direction, ports/adapters, and direct-call prohibitions.

Authoritative configuration, runtime definitions, idempotency registry, outbox/inbox, audit, and policy decision logs are Flyway-governed and evidence-producing.

OpenAPI, AsyncAPI, Avro/schema, CloudEvents, outbox, DLQ, replay, and idempotent consumer requirements are implemented where applicable.

Log4j2, OpenTelemetry, Sentry, Loki, Tempo, Grafana, audit, and trace reconstruction are implemented without leaking forbidden fields.

Concurrency, heavy-transaction handling, resilience, failure-injection, DAST, secrets hygiene, and remediation evidence are included in CI/CD gates.

Auto-Heal, Auto-Learn, and Auto-Improve remain candidate/proposal loops unless governed action tier, OPA/SBAC decision, Harness path, and human approval permit bounded action.

PR/MR evidence proves AVCI, EDP-01 to EDP-20, rollback/safe-disable path, reviewer approval, and post-promotion monitoring readiness.

# 28. AVCI Compliance Summary
| AVCI Property | How This Standard Satisfies It |
| --- | --- |
| Attributable | Defines owner, co-owners, audience, parent standards, companion documents, runtime actors, maker/checker/approver records, PR/MR evidence, and traceable source/config references. |
| Verifiable | Requires tests, CI/CD gates, policy results, contract compatibility, security scans, GitNexus impact analysis, telemetry samples, outbox/DLQ/replay proof, and evidence manifests. |
| Classifiable | Requires classification handling across configuration, payloads, telemetry, logs, prompts, events, evidence, AI routes, and retention. |
| Improvable | Defines Auto-Heal/Auto-Learn/Auto-Improve candidate loops, backlog linkage, review queue updates, known limitations, remediation evidence, and versioned change path. |

Final Implementation Rule

A MicroFunction implementation that passes functional tests but fails architecture, security, observability, idempotency, evidence, or rollback checks is not AIRA-ready. It remains a draft until the required controls are proven and reviewed.

