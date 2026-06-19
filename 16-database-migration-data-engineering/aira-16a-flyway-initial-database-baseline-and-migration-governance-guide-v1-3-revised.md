---
title: "Flyway Initial Database Baseline and Migration Governance Guide"
doc_id: "AIRA-16A"
version: "v1.3"
status: "revised"
category: "Database migration and data engineering"
source_docx: "AIRA_16A_Flyway_Initial_Database_Baseline_and_Migration_Governance_Guide_v1.3_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 16-database-migration-data-engineering
  - revised
  - aira-16a
---



# Flyway Initial Database Baseline and Migration Governance Guide



AIRA

AI-Native Enterprise Platform

Flyway Initial Database Baseline and Migration Governance Guide

v1.3 Revised

Greenfield Database Creation | Flyway from Day 0 | PostgreSQL | RLS | Outbox/Inbox | Evidence | Resilience | AVCI
| Property | Value |
| --- | --- |
| Document ID | AIRA-DOC-016A |
| Canonical Filename | AIRA_16A_Flyway_Initial_Database_Baseline_and_Migration_Governance_Guide_v1.3_Revised.docx |
| Version | v1.3 - Greenfield Flyway Execution, Dynamic Workspace, MicroFunction Runtime, API/Eventing, Observability, Resilience, AI Governance, and Evidence Alignment Update |
| Supersedes | 16A-AIRA_Flyway_Initial_Database_Baseline_and_Migration_Governance_Guide_v1.2_Aligned.docx |
| Parent Standard | 16-AIRA_Database_Migration_and_Data_Engineering_Standard_v2.2_Revised.docx |
| Companion Controls | 16B Flyway-Only Governance v1.1; 15/15A API Contract Standards; 17/17A Security; 20/45 DevSecOps Evidence; 30/30A Change; 31/31A Observability; 35 BCDR; Dynamic Workspace 46-61 |
| Classification | INTERNAL CONFIDENTIAL |
| Status | DRAFT FOR ARCHITECTURE REVIEW BOARD / DBA / DATA GOVERNANCE / DEVSECOPS / SECURITY / CAB APPROVAL |
| Owner | Solutions Architecture Office / Database Architecture / Data Governance |
| Co-Owners | DBA; Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; SRE; AI/Retrieval Architecture; Internal Audit |
| Review Cadence | Quarterly; unscheduled on material database baseline, Flyway, schema, RLS, seed, migration toolchain, environment, CI/CD, AI, or production data change |
| Evidence Path | OpenKM Tier-0 / AIRA / Data-Governance / Flyway-Initial-Baseline / v1.3/ |

Discipline First - Automation Second - Intelligence Third - AVCI Always

# Mandatory Position

Even when AIRA creates a database from scratch, Flyway is mandatory from Day 0. The initial schema is not a manual DBA setup shortcut and not a temporary bootstrap script. It is the first governed migration chain, the first database history record, the first reproducible baseline, and the first evidence-producing data-platform artifact. Production Flyway clean, baselineOnMigrate for greenfield, secrets in migration files, direct application DDL, and unreviewed AI-generated DDL are prohibited.

# Static Table of Contents

1. Executive Summary and v1.3 Upgrade Decision

2. Purpose, Scope, Authority, and Day-0 Flyway Decision

3. Greenfield Database Creation Model and Separation of Duties

4. Repository Structure, Naming, Header, and Initial Migration Chain

5. Flyway Configuration, Environment Promotion, and CI/CD Evidence

6. Database Baseline Design Rules for Dynamic Workspace, MicroFunction Runtime, API/Eventing, and Evidence

7. Security, Classification, RLS, Secrets, Synthetic Data, and Test Fixtures

8. Verification, Concurrency, Heavy Transaction, Resilience Lab, and Restore Validation

9. AI/System Builder Boundaries, Auto-Heal/Auto-Learn/Auto-Improve, Anti-Patterns, and Acceptance Criteria

10. RACI, Open Reconciliation Items, Templates, and AVCI Summary

# 1. Executive Summary and v1.3 Upgrade Decision

This v1.3 revision updates the Flyway initial baseline guide to align with the revised AIRA greenfield, database, security, API, DevSecOps, observability, release, operations, and Dynamic Workspace standards. It clarifies that Day-0 database setup must be reproducible, contract-aware, security-tested, evidence-producing, and ready for the AIRA System Builder and MicroFunction runtime without granting AI, frontend code, or application services uncontrolled database authority.
| Upgrade Area | v1.3 Required Result |
| --- | --- |
| Greenfield baseline | The first database object is created through Flyway, with clean-migrate proof and immutable history from the beginning. |
| Dynamic Workspace | Initial schemas include governed foundations for workspace/template/component metadata, policy filtering, layout versioning, evidence refs, and cache invalidation. |
| MicroFunction runtime | Initial schemas support transaction definitions, step catalog, activation state, idempotency, outbox/inbox, audit, and observability. |
| API/eventing | Database baseline includes contract registry metadata, outbox/inbox, DLQ/replay readiness, Avro/schema references, and CloudEvents correlation fields where applicable. |
| Security and RLS | Initial baseline includes classification, tenant isolation, RLS policy scaffolding, synthetic data rules, and no secrets in migrations. |
| Evidence and promotion | Flyway logs, checksums, CI results, GitNexus impact, DBA/security approvals, and rollback/forward-fix plan become required baseline evidence. |

# 2. Purpose, Scope, Authority, and Day-0 Flyway Decision

The guide defines how AIRA creates its initial PostgreSQL database baseline and how the baseline evolves across local, integration, UAT, staging, and production-like environments. It operationalizes the parent database standard for clean greenfield execution, not long-term database policy replacement.
| In Scope | Out of Scope |
| --- | --- |
| Empty database creation path after PostgreSQL cluster/database provisioning. | Manual production DDL, unmanaged database console setup, or application-generated DDL. |
| Flyway migration chain, naming, headers, checksums, validation, repeatability, and evidence. | Physical server procurement, unmanaged local-only database runtimes, or production secret creation. |
| Initial schemas, extensions, RLS scaffolding, seed/reference data, outbox/inbox, audit, evidence, and runtime config tables. | Business data migration/cutover, which is governed by the data migration standard. |
| CI/CD migration gates, Testcontainers, clean-migrate, synthetic data, security tests, and promotion evidence. | Agent-approved schema mutation, AI direct database access, or bypass of DBA/security/CAB review. |

Authority rule: 16 remains the parent database standard. 16A is the greenfield Flyway execution guide. 16B governs Flyway-only database generation and System Builder database proposals. When conflicts appear, the stricter control governs and the issue is logged as an AVCI reconciliation item.

# 3. Greenfield Database Creation Model and Separation of Duties

AIRA separates platform provisioning from schema creation. Infrastructure/DBA automation may provision the PostgreSQL cluster, database, network policy, migration identity, monitoring hooks, and approved secret references. Flyway owns all schema objects, reference data, security policies, extensions, and initial baseline objects after that point.
| Layer | Owner | Flyway Relationship | Evidence |
| --- | --- | --- | --- |
| PostgreSQL cluster / empty DB | Platform / DBA | Provisioned before migration; not schema authority. | Provisioning record, secret reference, network policy, owner. |
| Migration identity | DBA / Security | Least-privilege role executes approved migrations only. | Credential lease/ref, SBAC/OPA approval, audit log. |
| Application schemas | DBA + owning bounded context | Created only by Flyway migrations. | Migration version, checksum, review, CI evidence. |
| RLS / grants / policies | Security + DBA | Versioned through Flyway where database-native objects are used. | Negative tests, policy review, access evidence. |
| Seed/reference data | Data owner + DBA | Versioned and deterministic; synthetic data for tests. | Source_ref, classification, owner, tests, row counts. |
| Evidence/audit/outbox | Architecture + DevSecOps + DBA | Created as first-class platform schemas when applicable. | Trace/evidence refs, outbox replay tests, dashboards. |

# 4. Repository Structure, Naming, Header, and Initial Migration Chain

Flyway migration files live in the governed repository and follow deterministic naming, review, and evidence rules. The initial chain should be small enough for review but complete enough to establish AIRA platform foundations without manual side steps.
| Path / Artifact | Required Treatment |
| --- | --- |
| db/migration/common | Common extensions, governance schemas, migration metadata, evidence scaffolding, and reference tables. |
| db/migration/<bounded-context> | Context-owned schemas, tables, constraints, indexes, RLS, seed data, and views. |
| db/testdata/synthetic | Synthetic test fixtures only; no production data, secrets, raw PII, or Restricted records. |
| db/runbooks | Clean-migrate, validate, restore-smoke, replay, RLS, and failure-recovery runbooks. |
| VYYYYMMDDHHMM__description.sql | Versioned migrations for ordered baseline creation. |
| R__reference_or_view.sql | Repeatable migration only for approved deterministic objects; reviewed for drift impact. |
| Initial Chain Segment | Recommended Baseline Content |
| --- | --- |
| V001 governance schemas | Database metadata, evidence_ref pattern, classification reference, owner/source_ref fields, audit base, schema owner roles. |
| V002 security/RLS scaffold | Tenant column pattern, RLS enablement templates, deny-by-default grants, role separation, security views if needed. |
| V003 runtime config | MicroFunction transaction/step/config tables, activation status, config hash, idempotency profile, observability profile. |
| V004 integration evidence | Outbox/inbox, event schema refs, DLQ/replay metadata, CloudEvents fields, correlation and causation IDs. |
| V005 workspace metadata | Dynamic Workspace template/component/widget/layout/action metadata, policy_ref, classification, version, evidence_ref. |
| V006 seed/reference | Only approved initial reference rows, synthetic local/dev users where allowed, and deterministic test data. |

# 5. Flyway Configuration, Environment Promotion, and CI/CD Evidence

Flyway configuration must be reproducible from Golden Source. Local, CI, integration, UAT, staging, and production use environment-specific secret references, connection endpoints, and roles, but they must not redefine migration behavior silently.
| Environment | Flyway Rule | Promotion Evidence |
| --- | --- | --- |
| Local dev | Disposable PostgreSQL or devcontainer/Testcontainers; clean allowed only for local disposable DB. | Clean-migrate, validate, tests, no secrets, synthetic data proof. |
| CI | Fresh database per run; clean-migrate and validate are mandatory. | Pipeline run, checksum, logs, test results, evidence pack. |
| Integration/UAT | Forward-only migration; representative synthetic or approved masked data. | DBA/QA evidence, contract tests, RLS tests, migration smoke. |
| Staging/Prod-like | Forward-only; CAB/ARB gating for material changes. | Go/no-go, backup/restore validation, rollout plan, monitoring. |
| Production | No Flyway clean; no baselineOnMigrate for greenfield; human-approved migration runner only. | CAB approval, Flyway logs, post-migration smoke, rollback/forward-fix evidence. |
| CI Gate | Required Check |
| --- | --- |
| Flyway validate | Detect checksum drift, missing migrations, order errors, and unauthorised edits. |
| Clean-migrate | Prove greenfield reproducibility from empty database in local/CI. |
| Schema and contract tests | Verify OpenAPI/AsyncAPI/API consumers, generated clients, and backward compatibility where affected. |
| Security tests | RLS, grant, tenant isolation, secrets scan, migration content scan, and authenticated DAST fixture readiness. |
| Evidence pack | Capture migration versions, checksums, source commit, tool version, SBOM/provenance, GitNexus impact, reviewer approval, and trace/evidence refs. |

# 6. Database Baseline Design Rules for Dynamic Workspace, MicroFunction Runtime, API/Eventing, and Evidence

The initial baseline must not be a minimal table dump that later requires uncontrolled restructuring. It must include the foundation objects needed to enforce AIRA architecture boundaries from the first executable PoC.
| Area | Day-0 Baseline Rule |
| --- | --- |
| Dynamic Workspace | Workspace templates, screen definitions, component/widget catalog, layout/personalization, policy_ref, classification, version, status, and evidence_ref are backend-governed. |
| MicroFunction runtime | Transaction definitions, step sequence, capability_code, idempotency_profile, error_policy, retry policy, observability profile, and activation state are versioned data artifacts. |
| API/event contracts | Contract registry, endpoint/event version, schema ID, compatibility status, consumer impact, and deprecation metadata are represented where needed. |
| Kafka/eventing | Outbox/inbox tables include event_id, aggregate_ref, schema_ref, CloudEvents type/source/specversion, status, retry_count, DLQ reason, replay state, correlation_id, causation_id. |
| Evidence | Critical tables include owner, source_ref, classification, created/updated audit fields, trace/evidence linkage, retention, and improvement path where applicable. |
| Runtime toggles | Telemetry/debug/feature toggles require default value, environment scope, allowed actor, policy, expiry, audit event, rollback, and performance guardrail. |

# 7. Security, Classification, RLS, Secrets, Synthetic Data, and Test Fixtures

The Flyway baseline is also the first security baseline. Data classification, tenant isolation, least privilege, and test-data discipline must be visible in migrations and CI evidence.
| Security Control | Required Implementation |
| --- | --- |
| No secrets in migrations | Migration SQL, seed data, fixtures, screenshots, prompts, logs, and documentation must not contain passwords, tokens, keys, production endpoints, or raw secrets. |
| Least privilege | Migration, application, read-only, audit, and support roles are separated; broad owner privileges are not used by application services. |
| RLS / tenant isolation | Tenant-bearing tables include approved tenant strategy, deny-by-default tests, bypass review, and negative access tests. |
| Synthetic data only | Local/CI/test data is synthetic unless a masked/approved dataset is formally authorized and classified. |
| Prompt/model eligibility | Migration evidence and test data must state whether content is eligible for AI prompt/RAG/model use; Restricted data is blocked by default. |
| Authenticated DAST fixtures | Synthetic users, roles, tenant scopes, and safe records support authenticated DAST without production data exposure. |

# 8. Verification, Concurrency, Heavy Transaction, Resilience Lab, and Restore Validation

The initial baseline is accepted only when it can survive deterministic testing and controlled failure scenarios. AIRA does not wait for production incidents before proving idempotency, replay, lock behavior, and restore readiness.
| Validation Area | Required Evidence |
| --- | --- |
| Clean-slate creation | Empty database to fully migrated baseline using Flyway clean-migrate in disposable environments. |
| Idempotency and replay | Idempotency keys, unique constraints, inbox deduplication, outbox publication, DLQ/replay, and duplicate-safe consumer tests. |
| Concurrency / heavy transaction | Optimistic locking, row_version, transaction isolation, deadlock/lock timeout handling, batch sizing, retry/backpressure tests. |
| Observability | Log4j2 redacted migration logs, OpenTelemetry DB spans/metrics/logs, Sentry error context, Loki/Tempo/Grafana dashboards, trace/evidence refs. |
| Restore validation | Backup/restore smoke test proves baseline can be restored, validated, and compared through checksum/control totals. |
| Resilience lab | PostgreSQL outage, migration failure, cache loss, lock contention, slow query, outbox backlog, DLQ replay, and rollback/forward-fix rehearsal. |

# 9. AI/System Builder Boundaries, Auto-Heal/Auto-Learn/Auto-Improve, Anti-Patterns, and Acceptance Criteria

AI may assist the database baseline only through governed proposal paths. System Builder, Codex, Hermes, agents, or IDE assistants may draft migration candidates, tests, diagrams, and runbooks, but they must not directly mutate databases, approve their own work, or bypass DBA/security/CAB controls.
| AI / Automation Area | Required Boundary |
| --- | --- |
| System Builder | Classifies database impact and creates SchemaChangeProposal plus candidate Flyway migration; no direct promotion. |
| Codex / IDE assistant | May generate or refactor migration drafts and tests in branch/sandbox only, with AI-use declaration and human checker. |
| Agent tool access | Requires agent registry entry, SBAC skill, OPA decision, tool gateway, approved environment, audit, and evidence. |
| Auto-Heal | May detect failed migration, drift, stale seed, RLS defect, outbox backlog, or index issue and propose fix; production execution follows change/CAB path. |
| Auto-Learn / Auto-Improve | Lessons become reviewed standards, tests, runbooks, backlog items, or candidates; no silent schema mutation. |
| Rejected Practice | Reason |
| --- | --- |
| Manual application DDL | Destroys reproducibility, evidence, ownership, and rollback path. |
| Production Flyway clean | Destructive and prohibited except explicitly approved non-production/disposable contexts. |
| baselineOnMigrate for greenfield | Hides initial object history; greenfield must start with the first migration chain. |
| Secrets or real customer data in migrations | Violates secrets hygiene, classification, and AI/retrieval safety. |
| Direct AI or app production DB credentials | Breaks least privilege, SBAC, separation of duties, and fail-safe governance. |
| Cache-as-truth baseline | Redis/Valkey and indexes are derivative and rebuildable; PostgreSQL remains authority. |

# 10. RACI, Open Reconciliation Items, Templates, and AVCI Summary
| Activity | Solutions Architect | DBA | Developer | DevSecOps | Security/Data Owner | QA/SRE |
| --- | --- | --- | --- | --- | --- | --- |
| Define baseline scope | A/R | C | C | C | C | C |
| Author migration | C | C | R | I | C | C |
| Review DDL/RLS/grants | C | A/R | C | I | A/R | C |
| Run clean-migrate/CI | I | C | R | A/R | I | C |
| Approve promotion | A | R | C | R | C | C |
| Capture evidence | A | C | C | R | C | R |
| Acceptance ID | Ready-to-Use Gate |
| --- | --- |
| AC-01 | Empty database creation is reproducible through Flyway clean-migrate in local/CI and forward-only in controlled environments. |
| AC-02 | No manual DDL, production Flyway clean, greenfield baselineOnMigrate, secrets in migrations, or production data in fixtures exists. |
| AC-03 | Initial baseline includes governance, security/RLS, runtime config, outbox/inbox, evidence, and required Dynamic Workspace/MicroFunction foundation objects. |
| AC-04 | CI evidence includes Flyway validate, checksums, tests, RLS/tenant tests, idempotency/outbox tests, security scans, and GitNexus impact. |
| AC-05 | Promotion package includes owner, source_ref, classification, migration versions, DBA/security review, rollback/forward-fix, restore-smoke, and CAB path where required. |

Open reconciliation items: retain 16 as parent database standard, 16A as Day-0 greenfield Flyway execution guide, and 16B as Flyway-only governance; confirm final pack/register placement in the master document register; resolve any older references to PostgreSQL, Java, Technology Stack, or Pack order through 00D/revision-control matrix rather than silent normalization.
| Template Field | Required Content |
| --- | --- |
| Migration header | Document ID, migration ID, owner, source_ref, bounded_context, classification, intent, dependencies, verification, rollback/forward-fix, evidence path. |
| PR/MR Data Change Summary | Affected schemas, tables, contracts, events, RLS, seed data, test evidence, security review, performance risk, GitNexus impact, deployment window, rollback. |
| Flyway Evidence Record | Command, environment, version, checksum, tool version, commit, runner, logs, test result, approval, trace/evidence_ref. |
| AVCI Property | v1.3 Evidence |
| --- | --- |
| Attributable | Owner, co-owners, parent/companion sources, migration author, reviewer, approver, source_ref, and evidence path are identified. |
| Verifiable | Clean-migrate, Flyway validate, checksums, tests, RLS evidence, security scans, GitNexus output, restore-smoke, and dashboards verify readiness. |
| Classifiable | Migrations, seeds, logs, screenshots, evidence, test data, retrieval metadata, and runtime toggles carry classification and handling rules. |
| Improvable | Failed migrations, drift, RLS issues, outbox/replay defects, performance findings, audit findings, and lessons learned become controlled backlog/runbook/standard updates. |

# External Alignment Reference

This revision was checked for directional alignment with NIST SSDF SP 800-218, OWASP ASVS 5.0.0, OpenTelemetry semantic conventions for database signals, and SLSA v1.2 supply-chain provenance. These external references inform secure development, application security verification, telemetry consistency, and supply-chain evidence; AIRA-specific controls remain governed by the canonical AIRA register and approval path.

