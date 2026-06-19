---
title: "MicroFunction Standard Function Catalog and Assembly Templates"
doc_id: "AIRA-10D"
version: "v2.3"
status: "revised"
category: "MicroFunction framework"
source_docx: "AIRA_10D_MicroFunction_Standard_Function_Catalog_and_Assembly_Templates_v2.3_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 10-microfunction-framework
  - revised
  - aira-10d
---



# MicroFunction Standard Function Catalog and Assembly Templates



AIRA MicroFunction Standard Function Catalog
and Assembly Templates

Authoritative Step Catalog | Assembly Templates | Cross-Cutting Capability Coverage | Publish-Time Validation

v2.3 Revised - Catalog Governance, Runtime Evidence, and System Builder Alignment Update
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-010D |
| Document Title | AIRA MicroFunction Standard Function Catalog and Assembly Templates |
| Version | v2.3 Revised |
| Supersedes | AIRA_10D_MicroFunction_Standard_Function_Catalog_and_Assembly_Templates_v2_2_Review_and_Revised.docx upon approval |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Architecture Review Board / CAB / Engineering Team Review |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; DBA; Platform Engineering; AI Engineering; SRE / Operations; Internal Audit |
| Parent Standard | AIRA-DOC-010 MicroFunction Framework v3.4 Revised |
| Direct Companions | 10A v2.4 Revised; 10B v2.3 Revised; 10C v2.3 Revised; 10E pending review |
| Primary Role | Authoritative step catalog, metadata model, assembly templates, publish-time validation, and catalog lifecycle governance for MicroFunction runtime assembly. |

Mandatory Practice Statement

AIRA catalog entries and assembly templates are governed implementation controls. A transaction is not catalog-complete merely because the business step works. It is complete only when required security gates, policy decisions, idempotency, outbox, DLQ/replay, observability, audit, evidence, resilience, DevSecOps validation, GitNexus impact evidence, human approval boundaries, reversibility controls, and AVCI proof are defined, implemented, validated, and reviewable.

# 1. Executive Review Summary

The uploaded v2.2 candidate is structurally sound and correctly treats 10D as the authoritative MicroFunction catalog and assembly-template control. It already identifies that standard function selection, metadata, mandatory steps, validation gates, catalog lifecycle, System Builder generation, and evidence are not optional implementation details. This v2.3 revision preserves that direction and corrects the reference baseline to the now-revised MicroFunction family: 10 v3.4, 10A v2.4, 10B v2.3, and 10C v2.3.

The principal improvement in v2.3 is consolidation. Cross-cutting capability requirements are no longer treated as an addendum; they are embedded into the catalog metadata, template design, publish validators, runtime toggle rules, evidence pack, and acceptance checklist. This prevents incomplete MicroFunctions that pass functional tests but lack enterprise-grade security, resilience, observability, event governance, rollback, or audit proof.

# 2. Source Alignment and Corrective Decisions
| Aligned Source | Required 10D Treatment |
| --- | --- |
| 10 v3.4 Revised | Parent authority for runtime assembly, execution envelope, standard step categories, evidence envelope, AI/tool boundaries, cross-cutting capability coverage, and framework governance. |
| 10A v2.4 Revised | Design method for configure-first selection, STP-BUS isolation, design records, direct-call prohibitions, evidence chain, and System Builder design boundary. |
| 10B v2.3 Revised | Implementation authority for repository/package boundaries, Java contracts, catalog schema, runtime activation, telemetry, CI/CD gates, and forbidden imports. |
| 10C v2.3 Revised | Sequence evidence authority for Mermaid source, mandatory diagram coverage, runtime evidence paths, eventing, resilience, security, Auto-* loops, and runtime toggles. |
| 01A / 01 / 01B | EDP enforcement, AVCI quality gate, evidence/audit/traceability/classification model, and conflict treatment. |
| 02 / 03 / 04 / 05 / 06 / 07 / 07B | Blueprint, developer execution, technology baseline, information/source authority, repository AI rules, skill/SBAC model, and progressive autonomy direction. |
| 15 / 16 / 17 / 19 / 20 / 31A / 42 / 43 | Contract-first APIs/events, Flyway/database governance, security, GitNexus, CI evidence, observability, AI governance, and continuous improvement controls. |
| Decision | v2.3 Treatment |
| --- | --- |
| Version correction | Promote 10D to v2.3 Revised because the uploaded file is already a v2.2 candidate. |
| Parent correction | Replace 10 v3.3 candidate references with 10 v3.4 Revised. |
| Companion correction | Replace 10A v2.3 / 10B v2.2 / 10C v2.2 candidate references with 10A v2.4 / 10B v2.3 / 10C v2.3 Revised. |
| Queue correction | Mark 10D completed and set 10E as the next review item. |
| Addendum consolidation | Fold cross-cutting capability coverage into the body of the standard instead of retaining it as a loose update. |
| Register treatment | Record any stale references to older MicroFunction versions as AVCI reconciliation items for the canonical registers and revision matrix. |

# 3. Purpose, Scope, and Authority

## 3.1 Purpose

This standard defines the authoritative AIRA MicroFunction standard function catalog, assembly templates, mandatory step classes, validation gates, lifecycle states, metadata fields, evidence requirements, and acceptance rules used to assemble governed runtime transactions. Its purpose is to make AIRA business functions configurable, reusable, secure, observable, testable, resilient, reversible, and AVCI-compliant without forcing developers to re-code enterprise plumbing in every feature.

## 3.2 Scope
| Scope Category | Treatment |
| --- | --- |
| In scope | Reusable standard steps, STP-BUS functions, adapter-bound steps, policy-bound steps, AI/RAG/tool-action steps, workflow steps, eventing steps, observability steps, evidence steps, assembly templates, catalog schema, and publish-time validation. |
| In scope | Synchronous API commands, API-to-event outbox, Kafka/event consumers, workflow approvals, heavy transactions, AI-assisted analysis, Auto-Heal/Learn/Improve candidates, and System Builder-generated catalog drafts. |
| Out of scope | Direct production mutation, direct provider/model SDK calls from business logic, manual production DDL, frontend authorization authority, unmanaged Kafka publishing, Redis/cache-as-authority, and AI self-approval. |
| Out of scope | Replacing the parent MicroFunction Framework, implementation standard, API standard, security standard, database governance, observability standard, or DevSecOps gates. |

## 3.3 Authority and Precedence
| Level | Authority | Catalog Impact |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance | Final authority for production-impacting catalog changes, new cross-boundary steps, high-risk tool actions, and exceptions. |
| L1 | 01A / 01 / 01B / 02 / 03 | Architecture principles, AVCI, evidence, blueprint, and developer behavior that every catalog entry inherits. |
| L2 | 10 MicroFunction Framework v3.4 | Parent standard for runtime assembly, reusable standard concerns, cross-cutting controls, and MicroFunction governance. |
| L2 | This 10D Catalog v2.3 | Authority for step categories, catalog metadata, assembly templates, mandatory/conditional/optional/prohibited steps, and catalog publish validation. |
| L3 | 10A / 10B / 10C / 10E | Design, implementation, diagram, backend-generation, and runtime-configuration companion standards that must not weaken 10D. |
| L4 | Runtime configuration rows, Flyway seed data, templates, PR/MR evidence | Implementation instances that may tighten but must not weaken mandatory catalog controls. |

# 4. Catalog Governance Rules

• Every catalog entry must have a unique step_code, category, owner, version, lifecycle status, bounded context, classification ceiling, input/output contract, idempotency profile, retry/error policy, compensation posture, observability profile, audit profile, evidence profile, security profile, test profile, rollback/deactivation path, and improvement path.

• A business function must use an STP-BUS-* prefix, remain domain-focused, and must not own framework concerns such as parsing, authorization, audit, event publishing, idempotency, telemetry, error handling, response shaping, model routing, or guardrail execution.

• New categories, execution modes, security behavior, AI tool actions, external integrations, event types, mutating data paths, and cross-context contracts require ADR/TDL assessment, tests, catalog registration, and approval.

• A transaction cannot be activated unless selected catalog steps satisfy mandatory preconditions, error path, audit, observability, idempotency, outbox/eventing, replay/DLQ, security, evidence, and compensation requirements.

• A catalog entry may be deprecated but must not be silently removed while active runtime definitions, historical evidence, runbooks, or replay procedures still reference it.

• System Builder may generate candidate catalog entries and templates only as review-ready drafts. It must not approve, activate, promote, or mutate runtime behavior independently.

## 4.1 Catalog Lifecycle States
| State | Required Meaning |
| --- | --- |
| Draft | Created by human, System Builder, or AI assistant; not executable outside sandbox or validation fixture. |
| Validation Failed | Blocked by missing metadata, policy, contract, test, evidence, security, idempotency, or rollback requirement. |
| For Review | Complete enough for maker/checker, CODEOWNERS, architecture, security, QA, and DevSecOps review. |
| Approved | Accepted for controlled activation but not yet active. Evidence, signatures, and rollback path must exist. |
| Active | Runtime-eligible, versioned, hashed/signed, observable, rollbackable, and traceable to approval evidence. |
| Deprecated | Still available for active/historical references but no new transaction should select it without waiver. |
| Superseded | Replaced by a newer entry or template; old version remains reconstructable for audit and replay. |
| Retired / Revoked | No longer eligible for runtime use. Revocation requires impact analysis and migration/compensation evidence. |

# 5. Mandatory Catalog Entry Metadata
| Metadata Domain | Mandatory Fields / Meaning |
| --- | --- |
| Identity | step_code, step_name, category, version, lifecycle_status, owner, co_owner, bounded_context, source_ref, supersedes_ref, approval_ref. |
| Contracts | input_schema_ref, output_schema_ref, OpenAPI/AsyncAPI operation or event binding, Avro/JSON schema reference, CloudEvents type/source, compatibility rule. |
| Security | classification_ceiling, tenant_scope, SBAC skill, OPA policy_ref, secrets_ref policy, data handling, abuse_case_ref, DAST/security test profile. |
| Runtime | execution_mode, timeout, retry_policy, circuit_breaker, bulkhead, concurrency_limit, idempotency_profile, lock_strategy, cache_profile. |
| Eventing | outbox_required, topic_ref, schema_version, producer_idempotency, consumer_dedupe, DLQ_ref, replay_policy, ordering_key, trace/evidence fields. |
| Observability | trace_required, span_name, metric_names, log_profile, Log4j2 category, Sentry issue profile, Loki labels, Tempo trace, Grafana dashboard_ref. |
| Evidence | audit_event_type, evidence_ref, GitNexus_impact_required, CI_evidence_required, test_profile, coverage_profile, remediation_evidence_ref. |
| Reversibility | compensation_step_ref, rollback_strategy, feature_flag, deactivation_rule, replay/reprocess guidance, non_compensatable_risk_approval. |
| AI / Improvement | model_route_ref, guardrail_policy_ref, tool_action_policy, trust_tier, human_approval_required, improvement_candidate_rules, kill_switch_ref. |

# 6. Enterprise Design Principle Enforcement in the Catalog
| Principle | Mandatory Catalog Enforcement |
| --- | --- |
| EDP-01 SOLID | Each step has one responsibility, stable contract, clear extension model, focused interface, and injected dependencies. |
| EDP-02 Clean Architecture | Domain/use-case logic cannot depend on frameworks, UI, database, model providers, workflow engines, or provisioning tools. |
| EDP-03 DDD / Bounded Contexts | Each business step declares owning context and cannot write across context boundaries except through contracts/events/workflows. |
| EDP-04 Ports and Adapters | External systems, databases, queues, models, tools, and providers are accessed through explicit ports/adapters. |
| EDP-05 DRY/KISS/YAGNI | Reuse standard functions and templates before adding new code or categories. |
| EDP-06 Idempotency by Design | Mutating, callback, retry, replay, event, and agent-tool steps declare dedupe and replay-safe behavior. |
| EDP-07 Determinism | Runtime definitions, schemas, tests, prompts, and evidence are reproducible from approved sources. |
| EDP-08 Fail-Safe | Missing identity, policy, guardrail, audit, evidence, model route, or required config stops protected actions. |
| EDP-09 Human-in-the-Loop | High-impact, low-confidence, Restricted, destructive, production-impacting, or exception actions require named approval. |
| EDP-10 Least Privilege / SBAC | Each step declares required skills, roles, tool scope, data scope, tenant scope, and classification ceiling. |
| EDP-11 Separation of Duties | Maker, checker, approver, deployer, operator, agent owner, and auditor roles are separable for high-risk flows. |
| EDP-12 Observability | Each critical path declares trace, metric, log, audit, model, agent, provisioning, and evidence references with redaction. |
| EDP-13 Policy as Code | Authorization, admission, routing, guardrail, deployment, data-handling, and tool rules are versioned policy artifacts. |
| EDP-14 Testability | Each step declares deterministic fixtures, unit tests, contract tests, negative tests, policy tests, and integration tests. |
| EDP-15 Secure by Design | Threat controls, secrets hygiene, classification, tenant isolation, supply-chain controls, and secure defaults are mandatory. |
| EDP-16 Resilience | Timeouts, retries, circuit breakers, bulkheads, fallback, DLQ, compensation, recovery, and rebuild are explicit. |
| EDP-17 Fitness Functions | Automated checks verify boundaries, dependencies, contracts, security, agents, provisioning, and evidence rules. |
| EDP-18 Progressive Autonomy | Automation advances only with evidence, trust score, skill, risk tier, guardrails, and rollback controls. |
| EDP-19 Reversibility | Changes support rollback, forward-fix, compensation, feature disablement, environment rebuild, or safe deactivation. |
| EDP-20 AVCI | Each catalog artifact remains attributable, verifiable, classifiable, and improvable across its lifecycle. |

# 7. Function Category Naming Standard
| Category | Required Meaning |
| --- | --- |
| STP-RCV | Receive request, event, file, batch, schedule, webhook, UI command, AI action, or workflow signal through an adapter. |
| STP-COR | Create or propagate trace_id, span_id, request_id, correlation_id, causation_id, execution_id, and evidence_ref. |
| STP-SES | Resolve actor, service, agent, tenant, branch, role, skill, classification, and session context. |
| STP-SEC | Authenticate, authorize, enforce OPA/SBAC, validate secrets policy, check guardrails, and fail closed. |
| STP-CLS | Classify input, output, prompt, evidence, event, log, storage, retention, and route handling. |
| STP-VAL | Validate payload, schema, state, contract compatibility, business invariants, and negative cases. |
| STP-IDEMP | Apply idempotency key, replay guard, duplicate detection, lock/concurrency profile, and retry safety. |
| STP-BUS | Execute isolated bounded-context business logic only. |
| STP-DB | Call persistence ports/adapters and governed Flyway-owned schemas only. |
| STP-EVT | Write transactional outbox, publish event, validate CloudEvents/Avro, and record producer evidence. |
| STP-CONS | Consume Kafka/event messages with schema validation, dedupe, idempotency, retry, DLQ, and replay. |
| STP-WKF | Invoke Temporal/Flowable workflow boundaries, human approval, timers, compensation, and workflow evidence. |
| STP-AI | Invoke approved model/RAG/tool-action path through LiteLLM or approved gateway, guardrails, Harness, SBAC, OPA, and evidence. |
| STP-OBS | Emit telemetry, Log4j2 structured logs, OTel spans/metrics/logs, Sentry errors, Loki labels, Tempo traces, and Grafana dashboard refs. |
| STP-AUD | Persist immutable audit and AVCI evidence records. |
| STP-ERR | Classify errors, return safe responses, route incidents, preserve remediation evidence, and prevent leakage. |
| STP-COMP | Execute compensation, rollback, forward-fix, human review, DLQ, replay, or reprocess path. |
| STP-RESP | Shape safe API/UI/event response without exposing internal secrets or sensitive diagnostics. |

# 8. Mandatory, Conditional, Optional, and Prohibited Step Types
| Step Type | Definition and Required Treatment |
| --- | --- |
| Mandatory | Receive/correlate, actor/session resolution, classification, validation, authorization/policy, idempotency for mutations, audit/evidence, observability, error policy, and safe response. |
| Conditional | Outbox/event publish, event consumer, DLQ/replay, workflow approval, AI/RAG/tool action, heavy-transaction control, compensation, cache, file scan, DAST evidence, and GitNexus impact. |
| Optional | Additional diagnostic logging, non-critical metrics, enriched dashboard panels, advisory AI summary, optional sampling, non-blocking improvement suggestion. |
| Prohibited | Direct provider calls from domain logic; direct database/Kafka/model/audit calls in STP-BUS; disabled audit/security/policy evidence; hidden retries; swallowed exceptions; raw secret/PII logging; frontend business authority; AI self-approval; production mutation outside governed change control. |

# 9. Standard Assembly Templates
| Template | Required Sequence Coverage |
| --- | --- |
| Synchronous API Command | STP-RCV -> STP-COR -> STP-SES -> STP-CLS -> STP-VAL -> STP-SEC -> STP-IDEMP -> STP-BUS -> STP-DB -> STP-AUD -> STP-OBS -> STP-RESP -> STP-ERR/COMP as needed. |
| API-to-Event Outbox | API command template plus STP-EVT transactional outbox, CloudEvents metadata, Avro/schema version, producer idempotency, publish attempt evidence, and DLQ path. |
| Kafka/Event Consumer | STP-RCV event -> STP-COR -> STP-CLS -> schema compatibility -> STP-SEC policy -> STP-IDEMP consumer dedupe -> STP-BUS -> audit/outbox -> ack/nack -> DLQ/replay evidence. |
| Heavy Transaction / Concurrency | Add bounded concurrency, lock strategy, backpressure, timeout budget, bulkhead, circuit breaker, retry/backoff/jitter, compensation, load-test evidence, and saturation dashboard. |
| Human Approval Workflow | Business step requests approval through workflow boundary; maker/checker/approver separation, immutable decision audit, timeout/escalation, and resumption correlation are mandatory. |
| AI-Assisted Analysis | AI steps are advisory by default; route through approved gateway/guardrails/Harness/SBAC/OPA; record prompt metadata, model route, retrieval sources, output classification, evaluator result, and human acceptance. |
| Auto-Heal / Learn / Improve Candidate | Detection -> evidence retrieval -> impact analysis -> candidate proposal -> tests/scans/policy checks -> human review -> PR/MR -> controlled promotion. No silent mutation. |

# 10. Cross-Cutting Capability Coverage Matrix
| Capability Area | Mandatory Catalog / Template Coverage |
| --- | --- |
| DevSecOps / GitNexus | Repository controls, CODEOWNERS, CI/CD, unit/component/contract tests, SAST, SCA, secret scan, authenticated DAST where applicable, policy checks, architecture fitness, evidence pack, GitNexus read-only impact, SBOM/provenance, rollback path. |
| API / Event / Schema Governance | OpenAPI for synchronous APIs; AsyncAPI for evented APIs; Kafka topic governance; Avro/JSON schema compatibility; CloudEvents metadata; transactional outbox; idempotent consumers; DLQ; replay; schema evolution approval. |
| Observability | Log4j2 structured logs, OpenTelemetry traces/metrics/logs, Sentry error/release context, Loki log queries, Tempo traces, Grafana dashboards, alerting, audit events, evidence_ref, and redaction tests. |
| Concurrency / Heavy Transaction / Resilience | Idempotency key, duplicate safety, transaction boundary, lock strategy, timeout, retry/backoff/jitter, circuit breaker, bulkhead, backpressure, compensation, load/failure injection, DLQ, and safe replay behavior. |
| Auto-Heal / Auto-Learn / Auto-Improve | Issue detection, evidence retrieval, root-cause hypothesis, candidate fix or learning proposal, tests, policy/security/architecture checks, human checker, PR/MR/change proposal, monitoring, and knowledge update. |
| Security / Abuse / Remediation | OPA/SBAC expansion, abuse cases, authenticated DAST, secure API behavior, secrets hygiene, classification handling, safe responses, remediation tickets, retest evidence, and time-bound waiver records. |

# 11. Publish-Time Validation Gates
| Gate | Blocking Rule |
| --- | --- |
| G-01 Catalog Metadata | Reject if owner, version, classification ceiling, lifecycle state, source_ref, bounded context, or review evidence is missing. |
| G-02 Architecture Boundary | Reject direct framework leakage into business logic, direct provider calls, cross-context mutation, or missing ports/adapters. |
| G-03 Security / OPA / SBAC | Reject missing identity, policy_ref, skill scope, secrets hygiene, classification, tenant isolation, or fail-closed behavior. |
| G-04 Contract and Event Governance | Reject missing OpenAPI/AsyncAPI/Avro/CloudEvents contract, schema compatibility, idempotent producer/consumer, DLQ, or replay policy when eventing is used. |
| G-05 Idempotency and Concurrency | Reject mutating steps without idempotency key, dedupe, timeout, retry safety, lock/concurrency control, and compensation posture. |
| G-06 Observability and Audit | Reject missing trace/span, metric, structured log, Sentry/Loki/Tempo/Grafana linkage, audit event, evidence_ref, or forbidden-field protection. |
| G-07 DevSecOps and GitNexus | Reject production-bound change without tests, scans, architecture fitness, GitNexus impact evidence, SBOM/provenance where applicable, and PR/MR AVCI summary. |
| G-08 Reversibility | Reject missing rollback, forward-fix, compensation, feature disablement, replay/reprocess, or approved non-compensatable risk. |
| G-09 AI and Improvement | Reject AI/tool-action steps without model route, guardrails, Harness/SBAC/OPA, trust tier, human approval rules, evaluation, and incident/kill-switch path. |

# 12. Runtime Toggle Rules

AIRA allows runtime flexibility for diagnostic and performance-sensitive controls, but dynamic behavior must remain governed, observable, reversible, attributable, and evidence-producing.
| Toggle Rule | Required Treatment |
| --- | --- |
| Allowed | Diagnostic verbosity, trace sampling, non-critical debug logs, dashboard enrichment, synthetic probe frequency, non-essential advisory telemetry, cache refresh mode, and selected feature flags. |
| Governed | Toggles must be stored in governed configuration, versioned, auditable, classified, reversible, time-bound when required, and subject to OPA/SBAC and approval based on environment and risk. |
| Non-disableable | Mandatory audit events, security logs, policy decisions, classification labels, idempotency records, outbox records, access decisions, incident evidence, critical error evidence, and regulatory evidence. |
| Trace reconstruction | When telemetry is reduced, critical paths must still reconstruct behavior using trace_id, request_id, actor/session, policy decision, audit event, evidence_ref, and outbox/event reference. |
| Review | Performance-driven toggle changes must be captured as evidence and reviewed during service health, incident, release readiness, or CAB review as applicable. |

# 13. Security, Abuse Case, and Remediation Evidence Rules
| Security Control | Mandatory Catalog Treatment |
| --- | --- |
| OPA/SBAC expansion | Each protected action declares policy input, required skill, classification, tenant, branch/unit, tool scope, risk tier, environment, and policy decision evidence. |
| Abuse cases | Catalog entries for identity, authorization, eventing, file intake, AI, workflow, and privileged actions must reference abuse cases and negative tests. |
| Authenticated DAST | Protected APIs and Dynamic Workspace capabilities must include authenticated DAST or equivalent security validation evidence when applicable. |
| Secure APIs | OpenAPI contracts must define auth requirements, safe errors, idempotency keys, problem responses, rate limits, and forbidden data exposure. |
| Secrets hygiene | No secrets, raw tokens, raw JWTs, private keys, passwords, or production credentials may appear in code, config, logs, prompts, screenshots, tests, events, or evidence artifacts. |
| Remediation evidence | Security fixes require finding reference, root cause, changed catalog step/template, tests, scans, reviewer, approval, closure evidence, and residual risk state. |

# 14. System Builder and AI-Assisted Catalog Generation
| System Builder Rule | Treatment |
| --- | --- |
| Allowed | Generate candidate catalog entries, assembly templates, metadata manifests, evidence checklists, Mermaid/source diagrams, tests, OPA policy drafts, OpenAPI/AsyncAPI drafts, and PR/MR summaries. |
| Required before generation | Classify request, identify owner, bounded context, source authority, risk tier, applicable cross-cutting capabilities, standard-step reuse, and expected evidence path. |
| Required validation | Run catalog schema validation, duplicate detection, direct-call detection, contract checks, policy tests, architecture fitness, security scans, and evidence completeness checks. |
| Prohibited | Approve its own output, activate runtime state, merge code, deploy, mutate production, bypass CI/CD, bypass SBAC/OPA, create uncontrolled agents, or remove mandatory evidence controls. |
| Promotion | Only through PR/MR, CODEOWNERS, maker-checker review, policy and security gates, evidence pack, rollback/safe-disable path, and ARB/CAB where applicable. |

# 15. Required Evidence Pack and Definition of Done
| Evidence Class | Required Content |
| --- | --- |
| Design Evidence | Catalog diff, affected templates, architecture impact, EDP impact, owner, bounded context, classification, ADR/TDL or waiver if required. |
| Implementation Evidence | Code/config/Flyway changes, OpenAPI/AsyncAPI/Avro/CloudEvents contracts, OPA policies, tests, and generated artifacts. |
| Quality Evidence | Unit/component/contract/integration/OPA/policy tests, architecture fitness, mutation or negative tests where applicable, load/concurrency tests for heavy flows. |
| Security Evidence | SAST/SCA/secrets scan, authenticated DAST where applicable, dependency review, SBOM/provenance where applicable, abuse-case tests, remediation closure. |
| Observability Evidence | OTel trace, Log4j2 structured log sample, Sentry issue mapping, Loki labels, Tempo trace, Grafana dashboard, audit event, evidence_ref. |
| Eventing Evidence | Outbox row, publish attempt, Kafka/topic ref, Avro schema compatibility, CloudEvents metadata, consumer dedupe, DLQ/replay test. |
| GitNexus Evidence | Read-only impact analysis, affected files/functions/tests, architecture drift signal, sensitive-path review, PR/MR summary. |
| Reversibility Evidence | Rollback/forward-fix, compensation, replay/reprocess, deactivation, feature flag, cache invalidation, approval evidence. |

# 16. Anti-Patterns and Rejection Rules
| Anti-Pattern | Required Response |
| --- | --- |
| Duplicate framework plumbing | Creating a new STP-BUS function to perform parsing, auth, audit, event publishing, model invocation, logging, or error handling that already belongs to standard framework steps. |
| Unsafe activation | Activating a transaction without publish-time validation evidence, mandatory audit, idempotency, outbox, observability, safe error path, or rollback/compensation posture. |
| Cache or AI as authority | Treating Redis/Valkey, dashboards, LLM Wiki, generated summaries, or AI outputs as authoritative catalog truth instead of PostgreSQL/Flyway/Git-managed approved sources. |
| Telemetry suppression | Using runtime toggles to hide security evidence, policy decisions, audit trails, failed steps, idempotency conflicts, outbox backlog, or critical errors. |
| AI self-approval | Allowing AI or System Builder output to approve itself, mutate production, bypass OPA/SBAC/Harness, or skip maker-checker review. |
| Ungoverned event evolution | Promoting event schemas without compatibility validation, DLQ/replay strategy, idempotent consumer design, and outbox evidence. |

# 17. Acceptance Checklist
| Acceptance ID | Pass Condition |
| --- | --- |
| AC-01 | Every catalog entry has complete mandatory metadata, lifecycle state, owner, bounded context, classification ceiling, and evidence profile. |
| AC-02 | Every assembly template includes mandatory identity, classification, validation, authorization, idempotency, audit, observability, error, evidence, and safe response controls. |
| AC-03 | Eventing templates include OpenAPI/AsyncAPI, Kafka, Avro/JSON schema, CloudEvents, outbox, schema evolution, idempotent consumer, DLQ, and replay rules where applicable. |
| AC-04 | Heavy transaction templates include concurrency, retry safety, duplicate safety, load test, timeout, bulkhead, circuit breaker, and compensation evidence. |
| AC-05 | DevSecOps gates include tests, SAST/SCA/secrets/DAST where applicable, architecture fitness, GitNexus, SBOM/provenance where applicable, and PR/MR AVCI. |
| AC-06 | Runtime toggles do not disable mandatory audit, security, policy, idempotency, outbox, or critical error evidence. |
| AC-07 | Auto-Heal/Learn/Improve remains proposal-driven with evidence retrieval, candidate fix, tests, policy decision, and human approval. |
| AC-08 | System Builder generation is draft-only until validated, reviewed, approved, and promoted through governed PR/MR or change control. |
| AC-09 | The review queue and canonical registers are updated after approval. |

# 18. Automation Recommendations
| Automation Area | Recommended Control |
| --- | --- |
| Catalog schema validation | Validate step metadata, template metadata, required fields, lifecycle state, version, owner, classification, and evidence fields in CI. |
| Duplicate detection | Compare catalog step_code, event type, API operation, schema ID, policy ID, workflow key, and template ID before activation. |
| Cross-reference validation | Detect stale references to older MicroFunction versions and generate AVCI reconciliation items. |
| Evidence checklist validation | Block PR/MR or activation when required evidence classes are missing, stale, unreviewed, or not classifiable. |
| Direct-call detection | Reject direct database, Kafka, Redis, workflow, model-provider, secrets, audit, or telemetry bypasses from business logic packages. |
| Knowledge projection | Publish approved summaries to Obsidian/LLM Wiki only after source hash, version, classification, and retrieval eligibility are recorded. |

# 19. Review Queue Control Register
| Seq | File Name | Current | Recommended | Status | Next Step |
| --- | --- | --- | --- | --- | --- |
| 13 | 10-AIRA_MicroFunction_Framework_v3.1_Aligned.docx | v3.1 | v3.4 Revised | Completed | Parent MicroFunction standard; use as active candidate pending ARB/CAB approval. |
| 14 | 10A-AIRA_MicroFunction_Design_and_Development_Guide_v2.1_Aligned.docx | v2.1 | v2.4 Revised | Completed | Design/development companion; use for design handoff and System Builder design generation. |
| 15 | 10B-AIRA_MicroFunction_Framework_Implementation_Standard_v2.1_Aligned.docx | v2.1 | v2.3 Revised | Completed | Implementation standard; use for runtime engine, package, catalog schema, telemetry, CI/CD, and evidence controls. |
| 16 | 10C-AIRA_MicroFunction_Sequence_Diagrams_and_Mermaid_Reference_v2.1_Aligned.docx | v2.1 | v2.3 Revised | Completed | Diagram and sequence evidence standard; use for Mermaid source and rendered diagram governance. |
| 17 | 10D-AIRA_MicroFunction_Standard_Function_Catalog_and_Assembly_Templates_v2.1_Aligned.docx | v2.1 | v2.3 Revised | Completed | Catalog and assembly-template standard; this document. |
| 18 | 10E-AIRA_MicroFunction_Backend_Service_Generation_and_Runtime_Configuration_Standard_v1.1.docx | v1.1 | v1.2 recommended | Next | Align generated backend service and runtime configuration rules with the completed 10-10D MicroFunction candidate set. |

# 20. Change Log
| Version | Status | Summary |
| --- | --- | --- |
| v2.1 | Source baseline | Enterprise Design Principles and SOLID Enforcement Edition; authoritative catalog for standard function selection and assembly templates. |
| v2.2 candidate | Uploaded source | Cross-cutting capability update aligned with then-current 10 v3.3, 10A v2.3, 10B v2.2, and 10C v2.2 candidate set. |
| v2.3 Revised | This output | Corrects parent/companion references to 10 v3.4, 10A v2.4, 10B v2.3, and 10C v2.3; embeds cross-cutting coverage into catalog metadata, assembly templates, validators, runtime toggles, evidence pack, System Builder rules, and acceptance checklist. |

# 21. AVCI Compliance Summary
| AVCI Property | Evidence in This Standard |
| --- | --- |
| Attributable | Defines owner, co-owners, parent and companion standards, catalog entry ownership, bounded context, source references, version, status, reviewer, and PR/MR evidence. |
| Verifiable | Defines publish-time validators, tests, security gates, contract/schema checks, eventing tests, observability proof, GitNexus impact evidence, and CI/CD evidence pack requirements. |
| Classifiable | Requires classification ceilings, data handling, secret hygiene, log/prompt/evidence redaction, tenant scope, retrieval eligibility, storage, retention, and model-route eligibility. |
| Improvable | Defines catalog lifecycle, deprecation, feedback loops, Auto-Heal/Learn/Improve proposal gates, review queue updates, controlled supersedence, and improvement backlog linkage. |

Final Catalog Rule

A catalog entry or assembly template that enables runtime functionality but fails architecture, security, observability, idempotency, evidence, or rollback checks is not AIRA-ready. It remains draft until the required controls are proven, reviewed, and traceable.

