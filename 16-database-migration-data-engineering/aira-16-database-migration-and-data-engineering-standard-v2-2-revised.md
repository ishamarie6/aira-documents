---
title: "Database Migration and Data Engineering Standard"
doc_id: "AIRA-16"
version: "v2.2"
status: "revised"
category: "Database migration and data engineering"
source_docx: "AIRA_16_Database_Migration_and_Data_Engineering_Standard_v2.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 16-database-migration-data-engineering
  - revised
  - aira-16
---



# Database Migration and Data Engineering Standard



AIRA

AI-Native Enterprise Platform

Database, Migration, and Data Engineering Standard

v2.2 Revised

PostgreSQL | Flyway | RLS | Outbox/Inbox | pgvector | Data Governance | Evidence | Resilience | AVCI
| Property | Value |
| --- | --- |
| Document ID | AIRA-DOC-016 |
| Canonical Filename | AIRA_16_Database_Migration_and_Data_Engineering_Standard_v2.2_Revised.docx |
| Version | v2.2 - Dynamic Workspace, MicroFunction Runtime, Flyway, API/Eventing, Observability, Resilience, AI Governance, and Evidence Alignment Update |
| Supersedes | 16-AIRA_Database_Migration_and_Data_Engineering_Standard_v2.1_Aligned.docx |
| Companion Guides | 16A Flyway Initial Database Baseline and Migration Governance Guide v1.2; 16B Flyway-Only Generation, Versioning, and Migration Control Standard v1.1; 33 Data Migration/Cutover Standard |
| Classification | INTERNAL CONFIDENTIAL |
| Status | DRAFT FOR ARCHITECTURE REVIEW BOARD / DBA / DATA GOVERNANCE / DEVSECOPS / SECURITY / CAB APPROVAL |
| Owner | Solutions Architecture Office / Database Architecture / Data Governance |
| Co-Owners | DBA; Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; SRE; AI/Retrieval Architecture; Internal Audit |
| Review Cadence | Quarterly; unscheduled on material schema, migration, data, RLS, evidence, pgvector, outbox, workspace, MicroFunction, AI, or production data change |
| Evidence Path | OpenKM Tier-0 / AIRA / Data-Governance / Database-Migration-Data-Engineering / v2.2/ |

Discipline First - Automation Second - Intelligence Third - AVCI Always

# Mandatory Data Principle

PostgreSQL is the Tier-0 system of record for AIRA application state, runtime configuration, audit evidence, retrieval metadata, lineage, and governed data artifacts. Redis/Valkey, pgvector indexes, LightRAG, dashboards, reports, AI summaries, embeddings, and caches are derivative accelerators and must never become sole authority. Every database object that influences system behavior must be versioned, reviewed, tested, classified, observable, reversible by forward-fix or compensation, and evidenced through AVCI.

# Static Table of Contents

1. Executive Summary and v2.2 Upgrade Decision

2. Purpose, Scope, Authority, and Companion Alignment

3. Data Authority, Bounded Contexts, and Schema Ownership

4. Flyway Governance and Migration Lifecycle

5. Database Design Rules for Dynamic Workspace, MicroFunction Runtime, API/Eventing, and Evidence

6. Security, Classification, RLS, Retention, and Secrets Hygiene

7. Data Engineering, pgvector, Retrieval, Cache, Lineage, and Data Quality Controls

8. Observability, Runtime Toggles, Testing, Concurrency, Heavy Transaction, and Resilience Lab

9. DevSecOps, GitNexus, AI-Assisted Database Change, Auto-Heal/Auto-Learn/Auto-Improve, and Promotion Gates

10. RACI, Acceptance Criteria, Open Reconciliation Items, and AVCI Summary

# 1. Executive Summary and v2.2 Upgrade Decision

This v2.2 revision converts the parent database standard into the governing data platform control for the updated AIRA execution baseline. The standard now explicitly binds PostgreSQL, Flyway, RLS, pgvector, outbox/inbox, idempotency, Dynamic Workspace, MicroFunction runtime configuration, System Builder data proposals, AI agent registry evidence, DevSecOps evidence, observability, resilience lab validation, and BCDR interfaces into one auditable data discipline.
| v2.2 Alignment Area | Required Result |
| --- | --- |
| Flyway from Day 0 | Database creation, schemas, constraints, indexes, RLS, seed/reference data, evidence tables, outbox/inbox, and data fixes are migration-governed. |
| Dynamic Workspace | Workspace, template, component, widget, policy-filter, layout, personalization, and telemetry metadata remain backend-governed and Flyway-managed. |
| MicroFunction runtime | Runtime transaction definitions, step catalog, activation state, idempotency records, audit records, cache hashes, and evidence refs are governed data artifacts. |
| API/eventing | OpenAPI/AsyncAPI schemas, Kafka topic metadata, Avro schema references, CloudEvents attributes, outbox/inbox, DLQ, and replay state are traceable to database evidence. |
| Observability and toggles | DB spans, migration logs, slow queries, lock contention, telemetry sampling, diagnostic toggles, and evidence IDs must be safe, redacted, and auditable. |
| AI governance | System Builder and agents may draft migrations only through approved routes; DBA/security/human review is mandatory before promotion. |

# 2. Purpose, Scope, Authority, and Companion Alignment

The purpose of this standard is to define how AIRA designs, migrates, secures, observes, recovers, and improves governed data. It applies to all schemas, tables, views, functions, indexes, constraints, RLS policies, seed data, extensions, evidence records, outbox/inbox structures, registry tables, data repair scripts, retrieval metadata, and database-backed runtime configuration.
| Companion Source | Database Implication |
| --- | --- |
| 16A Flyway Initial Baseline | Defines greenfield Flyway-from-Day-0 creation and initial migration chain. |
| 16B Flyway-Only Governance | Blocks uncontrolled database generation, versioning drift, and manual mutation. |
| 15 / 15A API Contracts | Database changes that affect APIs/events require contract-first impact analysis and compatibility evidence. |
| 17 / 17A Security | RLS, secrets, identity references, data classification, OPA/SBAC, and secure data access are binding controls. |
| 20 / 45 DevSecOps | Migration validation, SAST/SCA/secret scans, SBOM/provenance, GitNexus impact, and evidence packs gate promotion. |
| 30 / 30A / 35 Release and BCDR | Production data changes require go/no-go criteria, forward-fix/compensation, restore validation, and CAB path. |
| 31 / 31A Observability | Database telemetry, trace correlation, audit evidence, dashboards, and forbidden telemetry fields are mandatory. |
| 46-61 Dynamic Workspace | Workspace configuration, runtime cache, API, security, testing, observability, and Admin Builder data must remain governed. |

# 3. Data Authority, Bounded Contexts, and Schema Ownership

AIRA treats database design as architecture. Each schema must map to a bounded context, owning team, classification ceiling, API/event contracts, runbook, retention rule, and evidence path. Shared tables without ownership are prohibited.
| Data Domain | Authoritative Treatment | Prohibited Shortcut |
| --- | --- | --- |
| Application state | Owned by bounded-context schemas and accessed through repositories/ports/adapters. | Direct cross-context writes or domain logic inside controllers. |
| Runtime configuration | PostgreSQL authoritative; Redis/Valkey may cache signed/hash-verified projections. | Cache-as-truth or config edited outside migration/governed admin workflow. |
| Audit/evidence | Append-only or tamper-evident where required; linked to trace_id, source_ref, actor, policy, and evidence_ref. | Editable audit records or evidence without source and owner. |
| Outbox/inbox | Transactional outbox and consumer inbox state are part of consistency and replay evidence. | Fire-and-forget event publishing without DB transaction linkage. |
| Retrieval metadata | Chunk lineage, embedding provenance, ACL, freshness, model-route eligibility, and quarantine status are stored as governed metadata. | Treating embeddings, summaries, or LLM answers as authoritative data. |
| Workspace data | Templates, layouts, widgets, policy filters, and personalization are backend-governed data artifacts. | Frontend-only authority or unmanaged local layout state. |

# 4. Flyway Governance and Migration Lifecycle

Flyway is mandatory for AIRA from the first database object. Manual production DDL is rejected except approved emergency remediation with post-action reconciliation, ticketing, DBA/security review, migration backfill, and evidence capture.

1. Open a classified database change intake with owner, bounded context, source reference, data classification, affected contracts, and rollback/forward-fix strategy.

2. Create a Flyway migration using the approved naming, header, checksum, test, and evidence conventions.

3. Run clean-migrate in disposable local/CI PostgreSQL; run Flyway validate and repository/component tests.

4. Run RLS/tenant isolation, seed determinism, idempotency, outbox/inbox, and performance/lock checks where applicable.

5. Generate PR/MR Data Change Summary with DBA, security, QA, and owner review as required.

6. Promote through DEV/INT/UAT/STG/PROD only through CI/CD, GitOps or approved migration runner; capture Flyway logs, checksums, trace IDs, and smoke evidence.

7. For production failures, stop, classify incident/change, capture database state, apply reviewed forward-fix or compensation, and update runbooks and lessons learned.
| Migration Type | Mandatory Gate |
| --- | --- |
| Schema create/alter | Bounded context ownership, contract impact, clean-migrate, Flyway validate, DBA review. |
| Reference/seed data | Deterministic source, owner approval, classification, effective dating, repeatable test. |
| RLS/policy object | Security review, negative authorization tests, tenant tests, policy decision evidence. |
| Index/performance change | Query plan evidence, lock impact, rollback/forward-fix, SLO/performance impact. |
| Destructive change | Expand/contract strategy preferred; data owner, backup/restore validation, affected-row evidence, CAB approval. |
| Data repair | Ticket/incident source, row-level evidence, dry run, owner approval, post-repair reconciliation. |

# 5. Database Design Rules for Dynamic Workspace, MicroFunction Runtime, API/Eventing, and Evidence

Database structures must support the AIRA runtime rather than hardcode business shortcuts. Runtime assembly, workspace rendering, API responses, event publication, AI evidence, and audit reconstruction must be traceable to governed rows, contracts, and migrations.
| Architecture Area | Database Requirement |
| --- | --- |
| Dynamic Workspace | Store workspace/template/screen/component/widget/configuration metadata with version, status, classification, policy_ref, layout_hash, owner, approval, rollback/deactivation, and evidence_ref. |
| MicroFunction runtime | Store transaction_code, step order, capability_code, error_policy, retry_policy, idempotency_profile, observability_profile, activation state, config hash, and audit/evidence refs. |
| API contracts | Persist contract registry metadata, version, compatibility status, generated client version, deprecation date, and consumer impact record when required. |
| Eventing | Persist topic/channel registry, schema_id, CloudEvents type/source/specversion, producer/consumer ownership, outbox state, DLQ/replay status, and retention. |
| Evidence records | Every significant data change must link owner, source_ref, trace_id, policy_decision_ref, migration_version, verification evidence, classification, and improvement path. |
| Runtime toggles | Telemetry/debug/feature/security toggles require default value, environment scope, allowed actor, policy decision, audit event, expiry, rollback, and performance guardrail. |

# 6. Security, Classification, RLS, Retention, and Secrets Hygiene

Database security is not limited to credentials. AIRA requires classification, tenant isolation, RLS where appropriate, least privilege, OPA/SBAC policy inputs, redaction-safe telemetry, retention, purge/hold controls, and secure secret references.
| Control | Mandatory Treatment |
| --- | --- |
| Secrets | No secrets, passwords, raw tokens, private keys, or production credentials in migrations, seed data, test fixtures, prompts, logs, screenshots, or evidence. Use approved secret references only. |
| RLS and tenancy | Tenant-bearing tables require tenant_id or approved partitioning strategy, negative tests, policy review, and access evidence. |
| Classification metadata | Tables/columns carrying regulated, Confidential, or Restricted data require classification, retention, prompt eligibility, model-route eligibility, logging restrictions, and owner. |
| Access path | Application code uses ports/adapters/repositories; direct SQL leakage into controllers, UI, prompts, agents, or unrelated bounded contexts is rejected. |
| Data retention | Retention, legal hold, disposal, archive, restore, and evidence retention are defined for each governed data class. |
| Authenticated DAST support | Synthetic non-prod users and data fixtures must support authenticated DAST without exposing production data. |

# 7. Data Engineering, pgvector, Retrieval, Cache, Lineage, and Data Quality Controls

Data engineering pipelines must not bypass source authority. Extracts, transformations, embeddings, retrieval indexes, reports, dashboards, and AI-generated summaries are derived views unless explicitly promoted through a governed data product lifecycle.
| Area | Required Control |
| --- | --- |
| pgvector / embeddings | Store source_ref, chunk_id, source_hash, embedding_model_alias, embedding_version, created_by, classification, ACL/RLS eligibility, freshness, and quarantine fields. |
| LightRAG / LLM Wiki | Index rebuilds require freshness manifest, source authority check, classification check, retrieval regression test, and rollback of index changes. |
| Redis/Valkey | Use only as accelerator; cache key, source hash, TTL, invalidation reason, and fallback-to-PostgreSQL behavior must be tested. |
| Data quality | Control totals, checksums, uniqueness, referential integrity, row counts, sampling, anomaly flags, and reconciliation evidence are required where data moves or transforms. |
| JSONB | Use for bounded extensibility with schema validation, indexes, classification review, and migration path; do not hide uncontrolled business model drift in JSONB. |
| Lineage | Every data product, migration, import, export, embedding, evidence pack, report, or dashboard needs source lineage and owner. |

# 8. Observability, Runtime Toggles, Testing, Concurrency, Heavy Transaction, and Resilience Lab

AIRA database behavior must be observable and testable under normal, retry, replay, concurrent, heavy-load, and failure conditions. Observability must avoid forbidden fields and high-cardinality metric labels.
| Validation Area | Required Evidence |
| --- | --- |
| Migration tests | Flyway clean-migrate, validate, checksum, repeatability, seed determinism, schema diff, component test. |
| Concurrency | Optimistic locking row_version, unique constraints, idempotency keys, transaction isolation evidence, deadlock/lock timeout tests. |
| Heavy transaction | Batch size, timeout, retry, backpressure, partitioning, pagination, SLO, and resource profile evidence. |
| Outbox/inbox | Duplicate-safe producer/consumer tests, replay tests, DLQ routing, poison-message handling, causation/correlation linkage. |
| Observability | OpenTelemetry DB spans/metrics/logs, Log4j2 redacted logs, Sentry error context, Loki/Tempo/Grafana dashboards, audit/evidence records. |
| Runtime toggles | Telemetry sampling, SQL diagnostics, slow-query threshold, trace verbosity, and feature toggles are policy-gated, environment-scoped, audited, and reversible. |
| Resilience lab | PostgreSQL outage, network timeout, lock contention, migration failure, cache loss, DLQ replay, restore smoke, and schema compatibility tests. |

# 9. DevSecOps, GitNexus, AI-Assisted Database Change, Auto-Heal/Auto-Learn/Auto-Improve, and Promotion Gates

Database changes are production-impacting engineering artifacts. AI may recommend, draft, explain, and test migration candidates, but it must not directly mutate databases, approve its own output, bypass DBA/security review, or execute production changes.
| Gate | Database-Specific Requirement |
| --- | --- |
| CI/CD | Build, Flyway validate/migrate, repository/component tests, RLS tests, seed tests, outbox/inbox tests, SAST/SCA/secrets scan, SBOM/provenance, evidence pack. |
| GitNexus | Read-only impact analysis for affected repositories, contracts, migrations, tests, consumers, MicroFunctions, workspace components, and runbooks. |
| System Builder | Database intake becomes SchemaChangeProposal plus Flyway migration plan; generation remains candidate-only until review. |
| AI agent controls | Agent must have registry entry, SBAC database migration skill, OPA decision, tool gateway boundary, human checker, and evidence ref before any candidate action. |
| Auto-Heal | May detect failed migration, stale index, missing seed, lock contention, outbox backlog, or RLS defect and propose remediation; production execution requires human/CAB path. |
| Auto-Learn / Auto-Improve | Lessons become reviewed standards, tests, runbooks, or backlog items; no silent schema/model/index mutation. |

# 10. RACI, Acceptance Criteria, Open Reconciliation Items, and AVCI Summary
| Activity | Solutions Architect | DBA | Developer | DevSecOps | Security/Data Owner | QA/SRE |
| --- | --- | --- | --- | --- | --- | --- |
| Define schema ownership | A/R | C | C | I | C | C |
| Author Flyway migration | C | C | R | I | C | C |
| Review DDL/performance | C | A/R | C | I | C | C |
| Review RLS/classification | C | C | I | I | A/R | C |
| Run CI migration tests | I | C | R | A/R | I | C |
| Approve production promotion | A | R | C | R | C | C |
| Capture evidence/runbook | A | C | C | R | C | R |
| Acceptance ID | Ready-to-Use Requirement |
| --- | --- |
| AC-01 | All schemas, tables, constraints, indexes, RLS policies, seed data, outbox/inbox, idempotency, evidence tables, and runtime config objects are created or changed through Flyway or approved migration workflow. |
| AC-02 | PostgreSQL remains Tier-0 authority; Redis/Valkey, pgvector, LightRAG, dashboards, and AI summaries are derivative and rebuildable. |
| AC-03 | Every migration includes owner, source_ref, bounded context, classification, verification, security impact, and forward-fix/reversibility statement. |
| AC-04 | CI proves clean-migrate, Flyway validate, tests, RLS/tenant isolation, seed determinism, idempotency, outbox/inbox, and security scan evidence. |
| AC-05 | Dynamic Workspace and MicroFunction configuration tables are versioned, policy-bound, cache-safe, observable, and safely deactivatable. |
| AC-06 | Database changes that affect OpenAPI, AsyncAPI, Avro, CloudEvents, Kafka, DLQ/replay, UI, workflows, or AI agents have contract and consumer-impact evidence. |
| AC-07 | Runtime telemetry toggles are default-safe, permissioned, audited, time-bound where appropriate, and cannot expose secrets or raw PII. |
| AC-08 | Auto-Heal/Auto-Learn/Auto-Improve outputs remain proposal-driven until reviewed and approved by the required human control path. |

Open reconciliation items: retain 16 as the parent database standard and 16A as the greenfield Flyway execution guide; verify any older references to Technology Stack versions, Java runtime fallback, or Pack 05 order during the next master register update; log unresolved conflicts in 00D / revision-control matrix.
| AVCI Property | v2.2 Evidence |
| --- | --- |
| Attributable | Document owner, co-owners, source baseline, migration owner, source_ref, DBA/security/CAB reviewers, and evidence path are defined. |
| Verifiable | Flyway logs, checksums, clean-migrate, tests, RLS evidence, contract impact, GitNexus output, dashboards, and restore/forward-fix evidence verify behavior. |
| Classifiable | Schemas, columns, seed data, telemetry, retrieval metadata, evidence, and prompts carry classification, retention, access, and model-route rules. |
| Improvable | Incidents, slow queries, failed migrations, replay errors, cache drift, retrieval quality issues, and audit findings feed controlled backlog and standard updates. |

# External Alignment Reference

This revision was checked for directional alignment with NIST SSDF SP 800-218, OWASP ASVS 5.0.0, OpenTelemetry semantic conventions for database signals, and SLSA v1.2 supply-chain provenance. These external references inform secure development, application security verification, telemetry consistency, and supply-chain evidence; AIRA-specific controls remain governed by the canonical AIRA register and approval path.

