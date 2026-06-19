---
title: "API Event Schema Registry DLQ and Replay Governance Runbook"
doc_id: "AIRA-67"
version: "v1.0"
status: "final"
category: "API event schema registry"
source_docx: "AIRA_67_API_Event_Schema_Registry_DLQ_and_Replay_Governance_Runbook_v1.0.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 67-api-event-schema-registry
  - final
  - aira-67
---



# API Event Schema Registry DLQ and Replay Governance Runbook



AIRA
AI-Native Enterprise Platform

API, Event, Schema Registry, DLQ, and Replay Governance Runbook

AIRA-DOC-067 | Version v1.0

Contract-First APIs | Event Governance | Schema Evolution | Transactional Outbox | Idempotent Consumers | DLQ | Controlled Replay | Evidence by Construction
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-067 |
| Document Title | AIRA API, Event, Schema Registry, DLQ, and Replay Governance Runbook |
| Version | v1.0 - Initial Enterprise Governance Standard |
| Status | Draft for Architecture Review Board, CAB, DevSecOps, Security, Platform Engineering, DBA, QA/SDET, SRE, AI Governance, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; DevSecOps Lead; Software Development Lead; Security Architecture; Platform Engineering; DBA; QA/SDET; SRE / Operations; AI Governance; Internal Audit |
| Primary Parents | AIRA-DOC-020 CI/CD Pipeline and Evidence Pack Implementation Guide v1.3; AIRA-DOC-011 v3.3; AIRA-DOC-011A v1.3; AIRA-DOC-065 Policy-as-Code v1.0; AIRA-DOC-066 Evidence Manifest v1.0 |
| Companion Sources | 01/01A/01B AVCI and Enterprise Design Principles; 02 Engineering Blueprint; 10 through 10E MicroFunction; 15/15A API; 16/16B Database/Flyway; 17/17A Security; 31/31A Observability; 63 PRR/ORR; 64 Resilience Lab |
| External Alignment | OpenAPI Specification; AsyncAPI; CloudEvents; Apache Kafka; Apache Avro; schema registry compatibility practices; OpenTelemetry; OPA/Rego; NIST SSDF; SLSA v1.2 |
| Review Cadence | Quarterly; unscheduled after material API/event contract, schema, topic, DLQ, replay, data classification, security, CI/CD, or production incident change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / API-Event-Schema-DLQ-Replay / 67 / v1.0 / |

# Mandatory Practice Statement

No AIRA API, event, topic, schema, producer, consumer, outbox, DLQ, replay action, message repair, or schema migration is acceptable merely because data moves successfully. It is acceptable only when the contract, owner, classification, schema, compatibility rule, OPA/SBAC decision path, idempotency behavior, observability, evidence, rollback/compensation path, and replay governance are defined, tested, approved, and traceable.

# Static Table of Contents

1. Executive Summary

2. Purpose, Scope, and Authority

3. Governance Control Plane

4. API Contract Governance

5. Event and Topic Governance

6. Schema Registry and Evolution Governance

7. Transactional Outbox, Inbox, and Idempotent Consumers

8. DLQ, Replay, and Message Repair Governance

9. CI/CD, Evidence, PRR/ORR, and Resilience Lab Gates

10. Security, Policy-as-Code, and Classification Controls

11. Observability, Audit, and Runtime Evidence

12. Runbook Templates and Manifests

13. RACI and Separation of Duties

14. Acceptance Criteria, Anti-Patterns, and Reconciliation

15. AVCI Compliance Summary

# 1. Executive Summary

AIRA-DOC-067 establishes the governed implementation and operations runbook for APIs, events, schemas, schema registry lifecycle, dead-letter queues, replay, and event-driven recovery. It converts AIRA DevSecOps, MicroFunction, Policy-as-Code, Evidence Manifest, Production Readiness, and Resilience Lab standards into executable API and event governance controls.

The standard prevents a common enterprise failure mode: allowing APIs and Kafka events to grow faster than their contracts, owners, compatibility rules, operational runbooks, security gates, and evidence records. In AIRA, APIs and events are not just integration artifacts. They are governed promises between bounded contexts and therefore require ownership, classification, compatibility, policy, evidence, and rollback discipline.
| Outcome | Required AIRA Control |
| --- | --- |
| Contract-first delivery | OpenAPI, AsyncAPI, Avro/JSON Schema, CloudEvents, and topic manifests exist before implementation or promotion. |
| Schema evolution safety | Compatibility is tested, consumers are identified, breaking changes require migration and approval. |
| Reliable event processing | Outbox/inbox, idempotent producer/consumer behavior, DLQ, replay, and error classification are tested. |
| Operational reconstructability | trace_id, correlation_id, event_id, schema_version, policy_decision_id, and evidence_ref are preserved. |
| Fail-safe governance | Missing identity, policy, schema, classification, observability, evidence, or approval blocks protected flows. |

Figure 1. AIRA API/Event Governance Control Plane

# 2. Purpose, Scope, and Authority

## 2.1 Purpose

Define the AIRA standard for contract-first API and event delivery across REST, messaging, workflow, Dynamic Workspace, MicroFunction, and AI/tool action boundaries.

Govern schema registry lifecycle, compatibility, versioning, consumer impact analysis, and schema deprecation/retirement.

Define safe DLQ, replay, reprocess, and message repair procedures that are idempotent, auditable, authorized, and evidence-producing.

Bind API/event work to CI/CD gates, Evidence Manifest, Policy-as-Code, PRR/ORR, Resilience Lab, and AVCI controls.

## 2.2 Scope
| In Scope | Out of Scope |
| --- | --- |
| OpenAPI, AsyncAPI, Kafka topics, schema registry subjects, Avro/JSON Schema, CloudEvents, outbox/inbox, idempotent consumers, DLQ/replay, replay review queues, and evidence manifests. | Ad hoc endpoints, unmanaged topics, manual message repair, direct production replay, schema changes outside CI/CD, and undocumented integration behavior. |
| MicroFunction event producers/consumers, Dynamic Workspace API calls, workflow signals, batch/file events, AI/tool-action events, and audit/evidence events. | Using frontend components, dashboards, LLM summaries, Obsidian projections, or GitNexus reports as authoritative contract truth. |
| CI/CD gates, policy checks, compatibility tests, replay tests, DLQ tests, PRR/ORR, Resilience Lab evidence, rollback/forward-fix, and production release controls. | Bypassing CI/CD, manual DDL, direct Kafka writes from business logic, direct model-provider calls, unapproved production credentials, or AI self-approval. |

## 2.3 Authority and Precedence
| Level | Authority | Meaning for AIRA-DOC-067 |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance / IT Head | Final authority for production-impacting API/event/schema/replay changes and exceptions. |
| L1 | 01A, 01, 01B, 02 | Enterprise design principles, AVCI, evidence, and architecture boundaries govern all contracts. |
| L2 | 11, 11A, 20, 65, 66 | DevSecOps, evidence, policy-as-code, and evidence manifest controls define promotion gates. |
| L3 | 10 through 10E, 15/15A, 16/16B, 17/17A, 31/31A, 63, 64 | MicroFunction, API, database, security, observability, readiness, and resilience companion controls. |
| L4 | Repository contracts, schemas, topic manifests, CI evidence, runtime telemetry | Operational proof; may tighten but must not weaken governing standards. |

# 3. Governance Control Plane
| Governance Domain | Control Requirement | Evidence |
| --- | --- | --- |
| Contract authority | Every API/event has an owner, bounded context, classification, version, consumers, and source path. | Contract manifest, CODEOWNERS, PR/MR evidence. |
| Schema authority | Schema registry subject, version, compatibility rule, lifecycle state, and producer/consumer ownership are explicit. | Schema manifest, compatibility report, consumer impact analysis. |
| Policy authority | OPA/SBAC governs protected API calls, event publication, replay, repair, and runtime toggles. | Policy decision log, Rego tests, evidence_ref. |
| Operational authority | DLQ, replay, reprocess, and repair actions require owner, classification, approval, dry-run, and monitoring. | Replay ticket, approval, trace/log/audit evidence. |
| Evidence authority | Each material API/event/schema/replay action emits evidence pack references and retained reports. | AIRA-DOC-066 manifest, CI artifacts, GitNexus, telemetry. |

# 4. API Contract Governance

AIRA APIs must be contract-first. The OpenAPI contract is the governed interface promise; controllers and generated clients are implementation artifacts derived from the contract. API behavior must preserve MicroFunction boundaries, backend policy authority, safe error handling, idempotency, and observability.
| API Control | Mandatory Rule |
| --- | --- |
| Source of truth | OpenAPI files in Git are authoritative for REST APIs. Generated clients and rendered documentation are derivative. |
| Security definition | Authentication, authorization, classification, rate limits, safe errors, and sensitive-field rules are defined in the contract and policy. |
| Idempotency | Mutating commands require idempotency key behavior, duplicate-safe response behavior, and retry documentation. |
| Versioning | Breaking API changes require versioning, consumer impact analysis, migration plan, rollback/forward-fix path, and approval. |
| Problem response | Errors use standard AIRA problem response fields without leaking secrets, stack traces, raw PII, or internal provider details. |
| CI gate | OpenAPI lint, diff, generated client validation, security review, and contract tests must pass before promotion. |

# 5. Event and Topic Governance

AIRA events are governed integration contracts. Kafka topic names, event types, schemas, CloudEvents metadata, producers, consumers, retention, replay rules, and DLQ strategy must be registered before operational reliance.
| Event Control | Required Treatment |
| --- | --- |
| AsyncAPI | Required for event channels, message shapes, producers, consumers, security, retry, DLQ, and replay posture. |
| Topic manifest | Topic owner, bounded context, purpose, retention, partitioning key, ACLs, classification, replay eligibility, and DLQ topic are declared. |
| CloudEvents envelope | Events carry stable identity and interoperability metadata such as id, source, type, time, subject where applicable, datacontenttype, trace context, classification, and evidence reference where permitted. |
| Producer discipline | Business state change and event intent use transactional outbox. Business logic does not publish directly to Kafka. |
| Consumer discipline | Consumers are idempotent, replay-safe, schema-aware, policy-aware where required, and evidence-producing. |
| Event retirement | Event types are deprecated with consumer migration, dual-run or compatibility window, and retained lineage. |

Figure 2. AIRA Outbox, DLQ, Replay, and Evidence Flow

# 6. Schema Registry and Evolution Governance

Schema registry governance ensures that producers and consumers evolve safely. AIRA supports Avro, JSON Schema, or approved schema formats, with compatibility rules selected by bounded context and risk. Backward-compatible evolution is the default recommendation unless the Architecture Board or Data Governance approves a stricter profile.
| Lifecycle State | Meaning | Required Gate |
| --- | --- | --- |
| Draft | Candidate schema or schema change exists in branch. | Owner, classification, subject name, examples, and compatibility intent. |
| Reviewed | Schema has technical and consumer review. | Compatibility check, consumer list, policy review, and test fixtures. |
| Approved | Schema can be promoted through CI/CD. | PR/MR approval, evidence manifest, rollback/forward-fix plan. |
| Active | Schema is used by runtime producers/consumers. | Runtime telemetry, schema_version, evidence_ref, and consumer health. |
| Deprecated | Schema is superseded but still supported. | Migration window, affected consumers, sunset date, and monitoring. |
| Retired | Schema is no longer used for new events. | Lineage retained for audit/replay; no new publication. |

Figure 3. Schema Lifecycle and Compatibility Assurance

# 7. Transactional Outbox, Inbox, and Idempotent Consumers
| Pattern | AIRA Rule | Required Evidence |
| --- | --- | --- |
| Transactional outbox | Business state and event intent are committed atomically. Publisher drains outbox after commit. | Outbox row, transaction ID, event ID, schema version, trace ID, publish attempt. |
| Inbox/processed registry | Consumers record processed event identity and processing outcome before or with side effects. | event_id/source/schema_version/consumer_id record and duplicate test. |
| Producer idempotency | Producer retry must not produce duplicate business effect. | Producer idempotency key and duplicate publish test. |
| Consumer idempotency | Consumer must safely handle duplicate delivery, replay, partial failure, and retry. | Replay test, duplicate delivery test, offset/reprocess evidence. |
| Ordering key | Ordering-sensitive events declare key and partitioning rationale. | Topic manifest, ordering tests, limitation statement. |
| Compensation | Non-reversible side effects require explicit risk acceptance or compensation strategy. | Compensation test, rollback/forward-fix plan, approval. |

# 8. DLQ, Replay, and Message Repair Governance
| Stage | Mandatory Runbook Control |
| --- | --- |
| DLQ classification | Classify error as transient, poison-message, schema-incompatible, policy-denied, dependency-failed, duplicate-risk, data-quality, or security-risk. |
| Containment | Stop uncontrolled retries, preserve payload handling rules, link trace/audit/evidence, and protect Restricted data. |
| Triage | Assign owner, bounded context, risk, affected consumers, business impact, and replay eligibility. |
| Remediation | Fix schema, policy, data, code, configuration, dependency, or runbook issue before replay when needed. |
| Replay approval | Replay requires maker-checker review, OPA/SBAC where applicable, replay window, target consumer group, dry-run when feasible, and rollback/stop plan. |
| Controlled replay | Replay is bounded, idempotent, observable, auditable, and linked to evidence_ref. |
| Closure | Closure records outcome, failed/successful counts, residual risk, monitoring, and Auto-Learn/Auto-Improve candidates. |
| Replay Type | Allowed Use | Approval |
| --- | --- | --- |
| Offset replay | Reprocess records within an approved topic/partition/offset or time window. | Owner + DevSecOps + SRE; Security/DBA if sensitive. |
| DLQ replay | Reinject or process DLQ records after remediation. | Owner + checker + CAB/ARB when production-impacting. |
| Synthetic replay | Use sanitized events to validate replay behavior. | QA/SDET + owner. |
| Message repair | Correct metadata/payload only through approved repair tooling and evidence. | Data owner + Security/DBA + CAB/ARB when material. |
| Production replay | Only when evidence, rollback/stop plan, monitoring, and business approval exist. | CAB or delegated authority; AI cannot approve. |

# 9. CI/CD, Evidence, PRR/ORR, and Resilience Lab Gates
| Gate | Blocks When Missing |
| --- | --- |
| OpenAPI/AsyncAPI gate | Contract missing, undocumented breaking change, unsafe error response, missing idempotency, or absent consumer impact analysis. |
| Schema compatibility gate | Schema compatibility result missing, consumer migration missing, version conflict, or unapproved breaking change. |
| Kafka/topic gate | Topic manifest, ACL, retention, partitioning key, DLQ, replay, and monitoring not defined. |
| Outbox/inbox gate | Direct Kafka publish from business logic, missing transactional outbox, missing consumer dedupe, or replay unsafe behavior. |
| Security/policy gate | OPA/SBAC, classification, secrets hygiene, authenticated DAST, or abuse-case evidence missing where required. |
| Observability gate | Missing trace/log/metric/audit/Sentry/Loki/Tempo/Grafana evidence or trace reconstruction fields. |
| Resilience Lab gate | No duplicate-safe, concurrent, replay, retry, DLQ, or failure-injection proof for critical flows. |
| PRR/ORR gate | Production readiness lacks runbook, dashboard, rollback, support owner, post-promotion monitoring, or release evidence. |

# 10. Security, Policy-as-Code, and Classification Controls
| Control | Mandatory Treatment |
| --- | --- |
| OPA/SBAC decision | Protected API access, event publication, replay, DLQ repair, schema promotion, and runtime toggle actions are policy-checked. |
| Classification | Contracts, schemas, events, payload examples, screenshots, logs, traces, DLQ records, and evidence packs declare handling rules. |
| Secrets hygiene | No raw tokens, passwords, private keys, raw JWTs, production credentials, or unrestricted PII in contracts, examples, DLQ, logs, prompts, or evidence. |
| Abuse cases | Privileged APIs, replay tools, admin topics, file events, AI/tool actions, and financial/customer-impacting flows require negative tests. |
| Authenticated DAST | External, privileged, customer-facing, or high-risk APIs require authenticated DAST in approved non-production scope. |
| Fail closed | If policy, identity, schema registry, evidence store, audit, guardrail, or approval path is unavailable, protected operation stops safely. |

# 11. Observability, Audit, and Runtime Evidence
| Signal | Required Fields / Evidence |
| --- | --- |
| Logs | trace_id, request_id, correlation_id, transaction_code, event_type, schema_version, consumer_group, result, error_code, classification, evidence_ref. |
| Traces | producer/consumer spans, outbox_id, topic, partition, offset where safe, policy_decision_id, schema_version, replay_id, evidence_ref. |
| Metrics | API latency/error, producer lag, outbox lag, consumer lag, DLQ count, replay success/failure, schema errors, policy denials. |
| Audit | actor, action, resource, policy result, approval reference, before/after safe references, replay decision, evidence_ref. |
| Error monitoring | Sentry or approved equivalent captures sanitized issue, release, environment, stack summary, owner, and remediation evidence. |
| Dashboards | Grafana links show API health, event health, outbox lag, consumer lag, DLQ/replay status, and schema error trends. |

# 12. Runbook Templates and Manifests

## 12.1 API Contract Manifest

api_id: AIRA-API-<bounded-context>-<capability>
owner: <role/name>
classification: INTERNAL CONFIDENTIAL
bounded_context: <context>
openapi_path: contracts/openapi/<name>.yaml
idempotency_required: true|false
security_scheme: OIDC + OPA/SBAC
problem_response_profile: AIRA-PROBLEM-v1
consumer_list: [<consumer>]
rollback_or_deprecation_path: <path>
evidence_ref: <evidence_pack_id>

## 12.2 Event Topic and Schema Manifest

topic_name: <domain.event.v1>
event_type: <com.aira.domain.event.created.v1>
owner: <role/name>
producer_service: <service>
consumer_groups: [<consumer-group>]
classification: INTERNAL CONFIDENTIAL
schema_subject: <subject-name>
schema_format: Avro|JSONSchema
compatibility: BACKWARD|FULL|FORWARD|approved-custom
cloudevents_required: true
outbox_required: true
dlq_topic: <domain.event.dlq.v1>
replay_policy: approval-required
retention_policy: <duration>
evidence_ref: <evidence_pack_id>

## 12.3 Replay Approval Checklist
| Checklist Item | Pass Condition |
| --- | --- |
| Owner and classification | Named accountable owner, business impact, data classification, and evidence pack exist. |
| Root cause | Cause is identified or replay risk is formally accepted with compensating controls. |
| Idempotency | Duplicate-safe and replay-safe behavior is proven or replay is blocked. |
| Replay window | Topic/partition/offset/time range and target consumer group are explicit. |
| Policy and approval | OPA/SBAC, maker-checker, CAB/ARB/security/data approval where required. |
| Monitoring and stop plan | Dashboards, alerts, rollback/stop condition, and post-replay validation defined. |

# 13. RACI and Separation of Duties
| Activity | Architecture | DevSecOps | Development | QA/SDET | Security | DBA/SRE | Internal Audit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Define API/event governance | A/R | R | C | C | C | C | I |
| Approve breaking contract/schema | A/R | C | R | C | C | C | I |
| Maintain CI gates | C | A/R | C | C | C | C | I |
| Operate schema registry | A | C | R | C | C | A/R | I |
| DLQ triage and replay | A | R | R | C | C | A/R | I |
| Security and policy review | C | C | C | C | A/R | C | I |
| Evidence review | A | R | R | R | R | C | A/R |

# 14. Acceptance Criteria, Anti-Patterns, and Reconciliation

## 14.1 Acceptance Criteria

Every API has an OpenAPI contract, owner, classification, security scheme, idempotency rule where applicable, tests, and evidence pack binding.

Every event has AsyncAPI/topic manifest, CloudEvents metadata, schema reference, producer and consumer owners, compatibility rule, DLQ/replay posture, and observability evidence.

Schema changes pass compatibility checks and consumer impact review; breaking changes use explicit versioning, migration, deprecation, and approval.

All mutating events use outbox/inbox and idempotent consumer behavior unless formally waived with risk owner and compensating controls.

DLQ and replay are bounded, authorized, auditable, redacted, monitored, reversible where feasible, and linked to evidence_ref.

CI/CD, PRR/ORR, Resilience Lab, and Evidence Manifest controls are satisfied before production reliance.

## 14.2 Anti-Patterns and Rejection Rules
| Anti-Pattern | Required Response |
| --- | --- |
| Event published directly from STP-BUS or controller | Reject. Use transactional outbox and approved adapter. |
| Schema change promoted without compatibility test | Reject. Require compatibility report and consumer impact analysis. |
| DLQ replay performed manually in production | Reject unless approved break-glass, logged, time-bound, and reconciled. |
| Consumer is not idempotent | Reject operational reliance; add inbox/dedupe and replay tests. |
| Contract examples contain secrets or raw PII | Reject; redact and classify correctly. |
| AI-generated replay or repair action self-approves | Reject. Convert to candidate proposal with human approval. |
| Dashboard or LLM summary treated as contract truth | Reject. Git contracts and registry records are authoritative. |

## 14.3 Open Reconciliation Items
| ID | Issue | Treatment | Owner |
| --- | --- | --- | --- |
| RI-067-001 | Schema registry product choice may vary across environments. | Keep this standard technology-neutral; pin actual implementation in Technology Stack and environment manifests. | Architecture / Platform |
| RI-067-002 | Existing API/event documents may reference older OpenAPI/AsyncAPI/schema versions. | Track in 00D and update through canonical register rather than silent normalization. | Solutions Architecture Office |
| RI-067-003 | Replay tooling requires maturity before production use. | Start with synthetic and non-production replay, then controlled pilot with PRR/ORR and Resilience Lab evidence. | SRE / DevSecOps |
| RI-067-004 | API/event governance overlaps 15/15A and 20. | Treat 15/15A as contract standard, 20 as CI implementation, and this 67 as operational governance/runbook. | Architecture Board |

# 15. AVCI Compliance Summary
| AVCI Property | How This Standard Satisfies It |
| --- | --- |
| Attributable | Requires owners, bounded context, CODEOWNERS, topic/schema/API owner, producer/consumer ownership, replay approver, commit SHA, and evidence_pack_id. |
| Verifiable | Requires OpenAPI/AsyncAPI/schema compatibility, OPA/SBAC tests, outbox/inbox/idempotency tests, DLQ/replay tests, observability proof, CI results, and retained evidence. |
| Classifiable | Requires classification for contracts, schemas, payload examples, events, logs, traces, DLQ records, replay actions, prompts, and evidence artifacts. |
| Improvable | DLQ trends, replay failures, schema errors, contract drift, GitNexus findings, incidents, and audit observations feed Auto-Learn and Auto-Improve candidate backlogs. |

# Appendix A. External Alignment Reference
| Reference | AIRA Use |
| --- | --- |
| OpenAPI Specification | Formal description of HTTP APIs; used for contract-first REST/API governance. |
| AsyncAPI | Formal description of event-driven and messaging interfaces; used for event/channel governance. |
| CloudEvents | Common event metadata and interoperability envelope for event identity and routing. |
| Apache Kafka | Event streaming platform pattern for topics, partitions, offsets, producers and consumers. |
| Apache Avro and schema registry compatibility practices | Schema evolution and compatibility governance for serialized events. |
| OpenTelemetry | Trace, metric, log, and resource correlation model for runtime evidence. |
| OPA/Rego and Conftest | Policy-as-code and CI policy validation for authorization, classification, deployment, and replay decisions. |
| NIST SSDF and SLSA | Secure development and supply-chain evidence alignment for production-bound artifacts. |

Contract First - Schema Safe - Replay Controlled - Evidence by Construction - AVCI Always

