---
title: "Database Governance Flyway Only Generation Versioning and Migration Control Standard"
doc_id: "AIRA-16B"
version: "v1.2"
status: "revised"
category: "Database migration and data engineering"
source_docx: "AIRA_16B_Database_Governance_Flyway_Only_Generation_Versioning_and_Migration_Control_Standard_v1.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 16-database-migration-data-engineering
  - revised
  - aira-16b
---



# Database Governance Flyway Only Generation Versioning and Migration Control Standard



AIRA

AI-Native Enterprise Platform

Database Governance: Flyway-Only Generation, Versioning, and Migration Control Standard

System Builder Database Boundary | Flyway-Only Authority | PostgreSQL Tier-0 Governance | Evidence by Construction | AVCI Always

AIRA-DOC-016B | Version v1.2 Revised | INTERNAL CONFIDENTIAL
| Mandatory Practice Statement | The AIRA System Builder, Codex, database-supporting agents, and human developers may analyze requirements, evidence, defects, performance signals, schema drift, and environment setup needs to draft database-impact proposals. They must not silently create, alter, repair, seed, truncate, clean, or promote database objects. All production-bound database changes must be Flyway-governed, versioned, classifiable, evidence-producing, reversible or forward-fixable, and approved through maker-checker, DBA, Security, DevSecOps, ARB/CAB, and Internal Audit controls. PostgreSQL remains the Tier-0 authority; Redis/Valkey, dashboards, generated summaries, embeddings, and caches remain derivative only. |
| --- | --- |

# Document Control
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-016B |
| Canonical Filename | 16B-AIRA_Database_Governance_Flyway_Only_Generation_Versioning_and_Migration_Control_Standard_v1.2_Revised.docx |
| Version | v1.2 - Revised Database Governance, Dynamic Workspace, MicroFunction, Resilience, and AI Control Alignment |
| Status | Draft for Architecture Board, CAB, DBA, Security, DevSecOps, Platform Engineering, QA/SDET, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / Database Architecture / Data Governance |
| Co-Owners | DBA; Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; Platform Engineering; AI Governance; SRE; Internal Audit |
| Supersedes | 16B v1.1 - System Builder Expansion Update |
| Primary Parent | 16-AIRA Database, Migration, and Data Engineering Standard v2.2 Revised |
| Direct Companions | 16A Flyway Initial Database Baseline v1.3; 15/15A API Contract Standards; 17/17A Security; 20 CI/CD Evidence; 30/30A Change and Reversibility; 31/31A Operations and Observability; 48 Dynamic Workspace Database/Flyway Specification |
| External Alignment Checked | NIST SSDF SP 800-218; OWASP ASVS 5.0.0; OpenTelemetry database semantic conventions; SLSA v1.2 supply-chain provenance |

# Static Table of Contents

Executive Summary and v1.2 Revision Verdict

Purpose, Scope, and Authority

Flyway-Only Control Model

System Builder and AI Database Generation Boundary

Governed Database Artifact and Registry Model

Dynamic Workspace, MicroFunction, API, and Event Integration

Migration Lifecycle, CI/CD Gates, and GitNexus Evidence

Security, Classification, Secrets, RLS, and Runtime Toggles

Concurrency, Heavy Transactions, Outbox/Inbox, DLQ/Replay, and Resilience Lab

Auto-Heal, Auto-Learn, Auto-Improve Database Candidate Loop

RACI, Acceptance Criteria, and AVCI Compliance Summary

# 1. Executive Summary and v1.2 Revision Verdict

This revised standard strengthens AIRA database governance after the alignment of the Greenfield Environment, System Builder Lite workstation guides, Sprint 0, CI/CD evidence, PoC 2 System Factory, Observability, Operations, Change/CAB, Security, API, and Database parent standards. Version v1.2 keeps the v1.1 System Builder expansion direction, but makes the Flyway-only control path operational for Dynamic Workspace, MicroFunction runtime configuration, OpenAPI/AsyncAPI contract evolution, Kafka/Avro/CloudEvents eventing, outbox/inbox, DLQ/replay, runtime toggles, resilience testing, and AI-assisted improvement proposals.

The governing position is strict: database change is not a prompt side effect, not a local setup shortcut, not an emergency shell activity, and not a hidden agent action. It is a governed engineering change that begins with intake, impact analysis, classification, owner assignment, contract/schema review, Flyway migration design, CI/CD evidence, DBA/security review, and promotion approval.
| v1.2 Governance Outcome | Required Result |
| --- | --- |
| Flyway-only authority | All schemas, tables, views, constraints, indexes, reference data, RLS policies, extensions, outbox/inbox structures, idempotency registries, workspace configuration tables, and evidence schemas are delivered through Flyway or approved migration workflow. |
| System Builder boundary | System Builder may draft schema-change proposals and migration candidates; it cannot approve, run, repair, clean, truncate, seed production, or bypass DBA/CAB controls. |
| Dynamic Workspace readiness | Workspace templates, component catalogs, layout metadata, widget bindings, runtime parameters, and cache-invalidation metadata are Tier-0 database/configuration artifacts when they govern runtime behavior. |
| MicroFunction readiness | Runtime transaction definitions, step catalogs, capability bindings, idempotency profiles, audit profiles, and execution evidence tables are Flyway-governed and test-proven. |
| Resilience and audit readiness | Outbox/inbox, DLQ/replay, idempotent consumers, concurrency tests, restore validation, observability correlation, and rollback/forward-fix evidence are mandatory for production-bound database changes. |

# 2. Purpose, Scope, and Authority

The purpose of this standard is to define the mandatory Flyway-only governance path for database generation, versioning, migration control, seed/reference data, data-bearing configuration, database evidence, database-supporting AI agents, and System Builder-assisted database changes.
| Area | Governance Treatment |
| --- | --- |
| In Scope | New requirements with database impact; operational evidence that implies schema/configuration change; improvement proposals; Flyway migrations; data contracts; RLS; tenant isolation; pgvector metadata; outbox/inbox; idempotency; reference data; Dynamic Workspace configuration; MicroFunction runtime tables; AI registry data; CI/CD database gates. |
| Out of Scope | Direct production DDL; unmanaged local databases as source of truth; agent-held production DB credentials; AI-approved schema change; manual repair without follow-up migration; raw Restricted telemetry in prompts; production Flyway clean; schema drift accepted as normal behavior. |
| Authority | ARB/CAB and consolidated architecture decisions govern material database architecture; this 16B standard governs Flyway-only database generation/versioning controls; 16/16A govern parent database/data engineering and Day-0 Flyway execution; 30/30A govern promotion and reversibility. |

# 3. Flyway-Only Control Model

Flyway is mandatory from Day 0 for greenfield schema creation and remains mandatory for all ongoing schema, seed, RLS, index, extension, view, materialized view, outbox, idempotency, evidence, and runtime configuration changes.

Manual production DDL is rejected except approved break-glass remediation; any emergency change must be reconciled through a follow-up Flyway migration, incident record, evidence pack, and drift closure.

Production Flyway clean is prohibited. Clean-migrate is allowed only in disposable local/CI databases using synthetic data and explicit environment safeguards.

baselineOnMigrate must not be used as a greenfield shortcut. It is a waiver-only legacy onboarding pattern with DBA, ARB/CAB, and audit approval.

Migrations must be additive or expand/contract whenever practical. Destructive changes require impact analysis, backup/restore evidence, affected-consumer approval, and irreversible-change waiver where applicable.

Migration scripts must not contain secrets, real customer data, unapproved privileged users, unbounded grants, hardcoded production endpoints, raw tokens, or hidden tool execution.
| Control Surface | Flyway-Only Treatment |
| --- | --- |
| Schema object | Flyway migration with owner, bounded context, classification, rollback/forward-fix note, and evidence reference. |
| Reference / seed data | Versioned migration or repeatable migration with synthetic/protected-data rules and idempotent insert/upsert behavior. |
| RLS / tenant controls | Policy migration plus positive/negative tests and Security/DBA approval. |
| Dynamic Workspace config | Versioned tables and seed/config migration; activation controlled by backend policy and audit. |
| MicroFunction runtime config | Catalog, transaction, step, capability, idempotency, audit/outbox profile migrations with deterministic tests. |
| Database drift | Detected by CI/runtime drift checks; drift is a non-conformance requiring reconciliation, not an undocumented fix. |

# 4. System Builder and AI Database Generation Boundary

System Builder database generation is advisory and draft-producing. It may assist analysis, compare options, generate candidate DDL, create Flyway drafts, identify missing indexes, propose RLS hardening, draft rollback/forward-fix paths, and prepare tests. It must not execute database mutation unless the action is explicitly routed through an approved, environment-scoped, Harness/SBAC/OPA-controlled path and permitted by governance.
| Action Class | Default Decision | Required Control |
| --- | --- | --- |
| Analyze | Allowed | Read approved contracts, source schemas, migration history, CI evidence, traces, performance metrics, and incidents using permitted data classification. |
| Draft | Allowed as candidate | Generate SchemaChangeProposal, migration draft, test draft, index recommendation, RLS test, replay plan, or evidence summary. |
| Dry-run | Allowed in sandbox/CI only | Run migration validation against disposable synthetic databases if tool scope, logs, secrets, and evidence are controlled. |
| Apply to DEV/TEST | Controlled | May be requested through pipeline/Harness if branch, review, CI, SBAC, OPA, and DBA rules permit. |
| Apply to UAT/STAGING/PROD | Human-controlled | Requires approved PR/MR, DBA review, security review, CAB/ARB where required, backup/restore validation, and promotion evidence. |
| Approve, bypass, clean, truncate, repair production | Prohibited | AI and agents must never approve their own output, run production clean, or perform side-channel fixes. |

# 5. Governed Database Artifact and Registry Model

AIRA must treat database artifacts as registered, classified, and evidence-linked engineering assets. The registry may be implemented as database tables, YAML manifests, repository metadata, or evidence-store records, but it must remain reconcilable to Git, Flyway, CI/CD, and runtime evidence.
| Metadata Field | Mandatory Meaning |
| --- | --- |
| schema_change_id | Unique identifier linking ticket, ADR/TDL, System Builder intake, PR/MR, and migration files. |
| owner / approver | Named accountable owner, DBA reviewer, Security reviewer, and CAB/ARB approver where applicable. |
| bounded_context / schema | DDD context and physical schema ownership; cross-context writes require explicit decision record. |
| classification / retention | Data classification, field sensitivity, retention rule, model-route eligibility, and evidence handling. |
| migration_refs | Versioned and repeatable migration files, checksums, CI result, environment application history. |
| contract_refs | OpenAPI, AsyncAPI, Avro/JSON Schema, CloudEvents, MicroFunction, workflow, and Dynamic Workspace references. |
| evidence_refs | Tests, scans, drift reports, restore evidence, performance evidence, OPA/RLS tests, GitNexus impact, and approvals. |
| reversibility | Expand/contract plan, backup/restore, forward-fix, compensation, feature disablement, replay/rebuild, or waiver. |

# 6. Dynamic Workspace, MicroFunction, API, and Event Integration
| Integration Area | Database Governance Requirement |
| --- | --- |
| Dynamic Workspace | Workspace layouts, template lifecycle, component catalog, widget bindings, user preferences, access-filtered resolved views, runtime cache metadata, activation state, rollback state, and audit evidence are governed database/configuration artifacts when they influence runtime behavior. Frontend code must not become authority. |
| MicroFunction Runtime | Transaction definitions, standard steps, capability bindings, policy inputs, idempotency profiles, retry profiles, audit profiles, observability profiles, and outbox events must be stored, versioned, migrated, and tested through governed tables and Flyway migrations. |
| OpenAPI / REST | Database changes that alter request/response semantics, resource shape, error behavior, pagination, idempotency, classification, or evidence fields require contract update, compatibility review, and generated-client/test refresh. |
| AsyncAPI / Kafka / Avro / CloudEvents | Event schema changes, topic/channel changes, header/correlation changes, compatibility mode, DLQ/replay behavior, and consumer idempotency require contract and schema-registry evidence before migration promotion. |
| Workflow / Approval | Temporal/Flowable state, approval records, maker-checker decisions, and long-running process migrations must preserve in-flight compatibility and compensation evidence. |

# 7. Migration Lifecycle, CI/CD Gates, and GitNexus Evidence

Intake: capture owner, ticket/source, business intent, affected bounded context, classification, risk tier, affected contracts, data retention, and acceptance criteria.

Impact analysis: review existing schemas, APIs/events, MicroFunctions, Dynamic Workspace tables, workflows, RLS policies, outbox/inbox, consumers, dashboards, tests, and rollback/restore implications.

Migration design: choose additive, expand/contract, repeatable, reference-data, compatibility, or forward-fix pattern; record destructive-change waivers where required.

Evidence draft: prepare migration header, schema diff, test plan, synthetic data plan, RLS tests, idempotency tests, performance/index assessment, restore validation, and observability plan.

CI validation: run Flyway validate, clean-migrate in disposable CI database, upgrade migration from previous baseline, repository tests, contract tests, security scans, architecture fitness, GitNexus impact, and evidence pack generation.

Promotion: require CODEOWNERS, DBA, Security, QA/SDET, DevSecOps, and CAB/ARB approvals based on risk and environment; production mutation occurs only through approved pipeline path.

Post-promotion: verify health, traces, dashboards, audit, evidence refs, migration history, schema drift status, outbox/DLQ status, performance signals, and rollback/forward-fix readiness.
| Gate | Minimum Evidence |
| --- | --- |
| Flyway checks | info, validate, migrate, checksum verification, clean-migrate in disposable CI, upgrade path, repeatable migration consistency. |
| Security checks | Secrets scan, least-privilege grants, RLS tests, tenant isolation tests, negative access tests, authenticated DAST data-fixture validation. |
| Contract checks | OpenAPI/AsyncAPI/schema compatibility, generated clients, consumer contract tests, idempotency behavior, Problem Details errors. |
| Operational checks | Backup/restore evidence, performance/index baseline, query plan review, migration duration risk, locking risk, heavy-transaction tests. |
| GitNexus checks | Read-only impact graph, affected services/tests/contracts, architecture drift signal, sensitive code/data surface mapping. |
| Evidence checks | PR/MR AVCI summary, migration evidence, approvals, telemetry, trace IDs, dashboard links, known limitations, improvement backlog. |

# 8. Security, Classification, Secrets, RLS, and Runtime Toggles
| Control | Mandatory Treatment |
| --- | --- |
| Secrets hygiene | No secrets in migration files, seed data, screenshots, prompts, logs, tests, examples, Obsidian notes, GitNexus reports, or evidence summaries. Use approved secret references only. |
| Classification | Every database object and evidence record that stores or references sensitive data must carry classification and retention metadata. Restricted content requires elevated handling and model-route controls. |
| RLS and tenant isolation | Tenant-scoped tables require RLS policy, test fixtures, positive/negative tests, DBA and Security approval, and drift checks. |
| Runtime toggles | Database-backed feature flags, logging/tracing toggles, diagnostic verbosity, replay toggles, and workspace activation flags must be versioned, authorized, audited, reversible, and fail-closed. |
| Audit and observability | Migration execution, runtime configuration activation, policy changes, cache invalidation, replay actions, and evidence generation must emit traceable audit records without leaking secrets or PII. |

# 9. Concurrency, Heavy Transactions, Outbox/Inbox, DLQ/Replay, and Resilience Lab

AIRA database governance must prove retry-safe, duplicate-safe, concurrent, heavy-load, and failure-aware behavior before production promotion. Heavy-transaction and replay readiness is not optional for evented, MicroFunction-backed, or workflow-bound features.
| Reliability Control | Database Evidence Requirement |
| --- | --- |
| Idempotency registry | Mutating requests, callbacks, workflow events, outbox consumers, and replay operations use idempotency keys, natural keys, or deduplication records with deterministic behavior. |
| Transactional outbox/inbox | Business state changes and event publication are coordinated through transactional outbox/inbox patterns; direct publish-without-persistence is rejected for critical flows. |
| DLQ and replay | DLQ records include schema version, event id, causation/correlation IDs, failure reason, classification, retry count, replay eligibility, human approval where required, and replay evidence. |
| Concurrency controls | Optimistic/pessimistic locking, version fields, unique constraints, retry boundaries, isolation expectations, timeout behavior, and deadlock handling are tested. |
| Resilience lab | CI/non-prod validates migration failure, partial migration, duplicate event, concurrent command, long-running transaction, DB failover, cache stale-state, DLQ replay, and restore scenarios using synthetic data. |

# 10. Auto-Heal, Auto-Learn, Auto-Improve Database Candidate Loop

Auto-Heal, Auto-Learn, and Auto-Improve may use database evidence to propose improvements. They must remain proposal-driven and must not self-modify schemas, policies, reference data, runtime configuration, migration history, or production records.
| Loop Stage | Required Database Governance |
| --- | --- |
| Detection | Inputs may include failed migration, drift signal, slow query, deadlock, DLQ growth, replay failure, RLS denial anomaly, SLO burn, incident, DAST finding, or audit finding. |
| Evidence retrieval | Retrieve approved traces, logs, metrics, schema history, GitNexus impact, CI evidence, incidents, contracts, and runtime config with classification filtering. |
| Candidate generation | Draft migration, index, RLS hardening, query refactor, replay fix, retention cleanup, test improvement, or knowledge update proposal. |
| Validation | Run deterministic tests, migration validation, performance comparison, contract checks, security checks, RLS tests, restore validation, and architecture fitness. |
| Human approval | DBA, Security, DevSecOps, QA, owner, and CAB/ARB approval occur before any protected activation or production-bound promotion. |
| Learning | Approved lessons become cited, classified, reviewed Obsidian/LLM Wiki knowledge; unreviewed AI output is not authoritative. |

# 11. RACI, Acceptance Criteria, and AVCI Compliance Summary
| Role | Responsibility |
| --- | --- |
| Solutions Architecture Office | Accountable for architecture fit, bounded-context decisions, cross-document reconciliation, and ARB escalation. |
| DBA / Data Governance | Accountable for physical schema, migration review, RLS, backup/restore evidence, performance risk, and drift closure. |
| Security Architecture | Accountable for secrets, classification, RLS/tenant tests, OPA/SBAC impact, and security findings. |
| DevSecOps | Accountable for CI/CD gates, Flyway runners, evidence packs, SBOM/provenance, and promotion controls. |
| Software Development / QA/SDET | Responsible for migration drafts, repository tests, contract tests, synthetic fixtures, and regression evidence. |
| SRE / Operations | Responsible for migration observability, runtime verification, rollback/forward-fix readiness, incident linkage, and dashboards. |
| Internal Audit | Consulted/assured for evidence sufficiency, traceability, control testing, and waiver closure. |

## Acceptance Criteria

All database-affecting work has intake, owner, bounded context, classification, migration plan, test plan, risk tier, evidence path, and approval route.

All database objects, reference data, RLS policies, indexes, runtime configuration, outbox/inbox, idempotency, and evidence schemas are Flyway-governed or governed by approved migration workflow.

CI/CD validates clean-migrate in disposable databases, upgrade migrate from prior baseline, schema compatibility, RLS, idempotency, contract, performance, restore, security, and architecture fitness evidence.

GitNexus outputs remain read-only and derivative; they support impact analysis but do not replace tests, DBA review, security scans, or human approval.

No production Flyway clean, manual production DDL, hardcoded secrets, AI-approved database change, direct agent database credential, or silent schema mutation exists.

Rollback, forward-fix, compensation, feature disablement, replay/reprocess, or restore path is documented and tested according to risk tier.

Auto-Heal/Auto-Learn/Auto-Improve outputs remain proposals until human-reviewed, tested, approved, and promoted through the governed path.

## AVCI Compliance Summary
| AVCI Property | Evidence |
| --- | --- |
| Attributable | Every database change identifies owner, requester, source, bounded context, migration file, reviewer, approver, pipeline run, and evidence reference. |
| Verifiable | Flyway history, CI/CD gates, tests, scans, GitNexus impact, OPA/RLS decisions, migration logs, restore validation, and runtime telemetry prove behavior. |
| Classifiable | Database objects, evidence, logs, test data, generated proposals, prompts, and knowledge updates carry classification, retention, redaction, and model-route rules. |
| Improvable | Incidents, failed migrations, drift, slow queries, replay failures, audit findings, and lessons learned feed controlled improvement proposals and reviewed knowledge updates. |

## Revision and Reconciliation Notes

This v1.2 revision preserves 16B as the database governance control standard and does not replace the parent 16 Database Migration and Data Engineering Standard or the 16A Day-0 Flyway execution guide.

If future source-pack regeneration finds conflicts among older 16/16A/16B references, the stricter Flyway-only, fail-closed, evidence-producing, DBA-reviewed interpretation governs until the canonical register is updated.

Known source-baseline reconciliation items, including duplicate numbering and historical source references, must remain visible in the revision-control register and must not be silently normalized in implementation.

