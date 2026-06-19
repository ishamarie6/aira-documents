---
title: "Reporting Analytics Semantic Layer BI Governance Standard"
doc_id: "AIRA-DOC-084"
version: "v1.0"
status: "final"
category: "Reporting analytics and BI"
source_docx: "AIRA-DOC-084_Reporting_Analytics_Semantic_Layer_BI_Governance_Standard_v1.0.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 84-reporting-analytics-bi
  - final
  - aira-doc-084
---



# Reporting Analytics Semantic Layer BI Governance Standard



AIRA
AI-Native Enterprise Platform

Reporting, Analytics, Semantic Layer, and Business Intelligence Governance Standard

Reports | Dashboards | Semantic Layer | BI | Analytics | Data Mart Governance | AI-Assisted Analytics

AIRA-DOC-084 | Version v1.0 | INTERNAL CONFIDENTIAL
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-084 |
| Document Title | Reporting, Analytics, Semantic Layer, and Business Intelligence Governance Standard |
| Version | v1.0 |
| Status | DRAFT FOR ARB, DATA GOVERNANCE, DEVSECOPS, SECURITY, OPERATIONS/SRE, QA/SDET, AI GOVERNANCE, AND INTERNAL AUDIT REVIEW |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Data Governance; Business Operations; DevSecOps Lead; Security Architecture; Operations/SRE; DBA; QA/SDET; AI Governance; Internal Audit |
| Primary Audience | Solutions Architects, Product Owners, Batch Operators, Business SMEs, Developers, DevSecOps, SRE, DBA, Security, Data Governance, QA/SDET, Internal Audit |
| Generated | 2026-06-18 |

# Static Table of Contents

1. Document Control

2. Mandatory Practice Statement

3. Executive Summary

4. Purpose, Scope, and Authority

5. Reporting and Analytics Governance Model

6. Report Catalog

7. Report Types

8. Semantic Layer Governance

9. Analytics Data Governance

10. On-the-Fly Reporting Rules

11. Scheduled and EOD Report Rules

12. AI-Assisted Analytics Rules

13. Report Security and Distribution

14. Report Evidence and Audit

15. CI/CD and Report Promotion Gates

16. Lifecycle and Versioning

17. Acceptance Criteria

18. RACI

19. Anti-Patterns

20. Open Reconciliation Items

21. AVCI Compliance Summary

# Document Control
| Field | Required Value |
| --- | --- |
| Document ID | AIRA-DOC-084 |
| Document Title | Reporting, Analytics, Semantic Layer, and Business Intelligence Governance Standard |
| Version | v1.0 |
| Status | DRAFT FOR ARB, DATA GOVERNANCE, DEVSECOPS, SECURITY, OPERATIONS/SRE, QA/SDET, AI GOVERNANCE, AND INTERNAL AUDIT REVIEW |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Data Governance; Business Operations; DevSecOps Lead; Security Architecture; Operations/SRE; DBA; QA/SDET; AI Governance; Internal Audit |
| Target Audience | Solutions Architects, Product Owners, Batch Operators, Business SMEs, Developers, DevSecOps, SRE, DBA, Security, Data Governance, QA/SDET, Internal Audit |
| Parent Standards | 01/01A/01B AVCI and Enterprise Architecture Standards; 02 Engineering Blueprint; 03 Developer Guide; 04 Technology Stack; 10 through 10E MicroFunction standards; 11 and 11A DevSecOps standards; 15 API and Integration Contract Standard; 16 Database/Flyway standards; 17 Security, Identity, Secrets, and Access Control; 20 CI/CD Evidence Pack; 31/31A Observability and SRE; 63 PRR/ORR; 64 Resilience Lab; 65 Policy-as-Code; 66 Evidence Manifest Schema; 67 API/Event/Schema/DLQ/Replay Governance; 68 Control Objectives and Evidence Traceability Matrix; 71 Data Governance, Retention, Privacy, and Evidence Classification; 77-81 Data/Message Governance family; Dynamic Workspace 54-61 and 74-75. |
| Companion Documents | AIRA-DOC-082 Batch Governance; AIRA-DOC-083 Batch Operations Runbook; AIRA-DOC-085 Template Pack; 15 API; 16 Database/Flyway; 31/31A Observability; 66 Evidence Manifest; 71 Data Governance; 77-81 Data Dictionary, Message, Error Code, Validator, Localization, and Support Knowledge standards. |
| Review Cadence | Quarterly; unscheduled after Sev-1/Sev-2 incident, failed EOD, material batch/reporting model change, data-quality control failure, regulatory change, or architecture/security control change. |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Reporting-Analytics-Governance / AIRA-DOC-084 / v1.0/ |
| Approval Path | Draft -> Architecture/Data/Security/DevSecOps/SRE/QA/Internal Audit review -> ARB/CAB approval where production-impacting -> Register update -> Controlled publication. |
| Supersedence Rules | This document becomes canonical only after register adoption. Any supersedence, split, merge, or retirement must update document register 00A-00D, evidence paths, cross-references, and downstream implementation impact records. |

## Version History
| Version | Date | Owner | Summary |
| --- | --- | --- | --- |
| v1.0 | 2026-06-18 | Solutions Architecture Office / IT Head | Initial draft for batch, scheduled processing, reporting, analytics, evidence, and operational governance. |

# Mandatory Practice Statement

Mandatory Practice Statement. No report, dashboard, extract, analytics model, semantic layer, data mart, AI-generated analysis, or BI output may be treated as authoritative merely because it produces output. It is authoritative only when cataloged, classified, owner-approved, sourced from governed data, semantically defined, access-controlled, tested, reproducible, evidence-producing, retained, and approved according to its business, regulatory, operational, or management purpose.

# Executive Summary

Reporting and analytics are business decision surfaces. Incorrect definitions, stale data, hidden filters, ungoverned exports, inconsistent KPIs, uncontrolled dashboards, and AI-generated narratives can create financial, operational, regulatory, and reputational risk. AIRA therefore governs reports and analytics as controlled products with owners, definitions, lineage, access rules, evidence, and lifecycle states.

This standard defines the enterprise governance model for on-the-fly reports, EOD reports, scheduled reports, operational reports, regulatory/compliance reports, management reports, exception reports, reconciliation reports, dashboards, semantic layer metrics, analytics datasets, data marts, KPIs/KRIs, and AI-assisted analytics.

# Purpose, Scope, and Authority

The purpose of this standard is to ensure that report and analytics outputs are correct, traceable, secure, reproducible, classifiable, explainable, and reviewable. It applies across AIRA user workspaces, backend services, reporting read models, data marts, extracts, BI tools, dashboards, AI assistant outputs, scheduled jobs, and EOD processes.
| In Scope | Examples |
| --- | --- |
| Reports | On-the-fly, EOD, scheduled, operational, regulatory, management, exception, reconciliation, self-service query, export/extract. |
| Dashboards | Operational dashboards, SLO dashboards, management dashboards, evidence dashboards, analytics dashboards. |
| Semantic layer | Metrics, KPIs/KRIs, dimensions, measures, aggregation rules, grain, lineage, time definitions. |
| Analytics datasets | Read models, snapshots, materialized views, data marts, analytical extracts, certified datasets. |
| AI-assisted analytics | Narrative summaries, anomaly explanations, candidate insights, follow-up recommendations under human review. |

# Cross-Document Alignment and Control Baseline

This document inherits the AIRA control baseline and must be read as a governed companion to the existing AIRA source packs and canonical registers. It does not weaken any parent standard. If a conflict is found, the stricter control applies until the conflict is resolved through the AVCI reconciliation process.
| Control Area | Alignment Requirement | Evidence |
| --- | --- | --- |
| Architecture and AVCI | Every artifact has owner, source, version, classification, validation evidence, and improvement path. | 01/01A/01B evidence review and PR/MR AVCI summary. |
| Contract-first boundary | APIs, events, files, schemas, reports, and dashboards are governed before implementation. | OpenAPI, AsyncAPI, Avro/JSON schema, report definition, lineage, and compatibility tests. |
| Configuration-first delivery | Use MicroFunction steps, parameters, schedules, DMN/OPA rules, templates, and registries before custom code. | Runtime definition, feature flag, registry record, Flyway seed, and approval evidence. |
| Security and policy | OPA/SBAC, least privilege, classification, masking, secrets hygiene, SoD, and break-glass rules apply. | Policy decision log, access review, service-account record, and tamper-evident audit. |
| Observability and evidence | Every run, report, dashboard, extract, and analytics refresh emits trace, metric, log, audit, and evidence references. | OpenTelemetry trace, Log4j2 structured log, Sentry issue, Loki/Tempo/Grafana link, evidence manifest. |
| Reversibility and recovery | Batch and reporting changes must support rollback, forward-fix, compensation, replay, or safe disablement. | Runbook, checkpoint, DLQ/replay record, reconciliation signoff, and CAB/ARB decision. |

## Required Design Principles

AVCI

SOLID

Clean Architecture

DDD and bounded contexts

Ports and adapters

DRY, KISS, YAGNI

Idempotency by design

Determinism and reproducibility

Fail-safe, not fail-open

Human-in-the-loop

Least privilege and SBAC

Separation of duties

Observability by design

Policy as code

Testability by design

Secure by design

Resilience patterns

Architecture fitness functions

Progressive autonomy

Reversibility and rollbackability

Evidence by construction

# Reporting and Analytics Governance Model
| Governance Layer | Purpose | Required Evidence |
| --- | --- | --- |
| Catalog | Register reports, dashboards, datasets, extracts, KPIs/KRIs, and semantic objects. | Catalog record, owner, classification, lifecycle state. |
| Definition | Define business meaning, formulas, filters, parameters, source data, grain, and time semantics. | Definition approval, data dictionary link, query hash. |
| Lineage | Map source systems, transformations, snapshots, materialized views, data marts, and report outputs. | Lineage diagram, source_data_version, data_snapshot_ref. |
| Security | Apply OPA/SBAC, RLS/CLS, masking, export limits, external sharing approval, watermarking, and audit. | Policy decisions, masking tests, distribution record. |
| Quality | Validate calculations, reconciliation, freshness, completeness, performance, and reproducibility. | CI/CD gates, data-quality results, report test evidence. |
| Distribution | Control publication, email, download, export, retention, legal hold, and disposal. | Distribution evidence, retention/disposal record. |
| AI Advisory | Ensure AI summaries are citation-backed, classified, confidence-labeled, and human-reviewed. | AI-assisted analytics review record. |

# Report Catalog
| Catalog Field | Governance Requirement |
| --- | --- |
| report_id | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |
| report_code | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |
| report_name | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |
| report_type | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |
| business_owner | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |
| technical_owner | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |
| steward | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |
| classification | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |
| audience | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |
| purpose | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |
| source_data | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |
| canonical_data_elements | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |
| business_definition | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |
| calculation_rules | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |
| filters | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |
| parameters | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |
| refresh_frequency | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |
| freshness_SLO | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |
| distribution_rule | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |
| retention_rule | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |
| export_formats | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |
| masking_rule | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |
| approval_required | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |
| evidence_ref | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |
| lifecycle_state | Mandatory field. Must be versioned, reviewable, classifiable, and validated before production publication or distribution. |

# Report Types
| Report Type | Definition | Minimum Control |
| --- | --- | --- |
| Operational report | Supports daily processing, queues, exceptions, service status, or frontline work. | Near-real-time freshness rule, access policy, safe drill-down, audit. |
| EOD report | Generated after EOD stage and tied to business date and data snapshot. | Batch dependency, reconciliation binding, immutable artifact, signoff. |
| Reconciliation report | Shows source-target, count, total, amount, hash, and exception comparison. | Control totals, exception aging, maker-checker approval. |
| Regulatory report | Supports regulatory, compliance, audit, or external obligation. | Formal definition, approval, retention/legal hold, external sharing approval. |
| Management report | Supports management decision-making, trends, KPIs, KRIs, and performance review. | Semantic layer definition, approval, evidence trail. |
| Exception report | Identifies failed, overdue, inconsistent, risky, or out-of-policy items. | Owner, SLA, escalation, evidence, aging. |
| Dashboard | Interactive visualization, status board, or operational display. | Policy-filtered data, drill-down controls, tested widgets. |
| Analytical dataset | Certified dataset for analysis or model input. | Lineage, freshness, quality, certification, access and retention. |
| Self-service query | Controlled user-created query over governed semantic/data layer. | Query safety, row/column-level security, limits, audit. |
| AI-generated analysis | AI-generated narrative, anomaly explanation, or candidate insight. | Source references, confidence, classification, human review. |
| Export/extract | File or API output sent to users/systems. | Contract, masking, distribution evidence, retention, audit. |

# Semantic Layer Governance
| Semantic Object | Required Definition | Approval Rule |
| --- | --- | --- |
| Canonical metric | Name, code, purpose, owner, formula, grain, filters, source, unit, time window, exclusions, rounding, lineage. | Business owner + data steward approval; versioned compatibility rules. |
| KPI/KRI | Target, threshold, directionality, calculation, frequency, owner, risk meaning, action trigger. | Business owner + risk/compliance where applicable. |
| Dimension | Business definition, allowed values, hierarchy, source, slowly changing behavior, classification. | Data steward approval. |
| Measure | Aggregation method, precision, null handling, deduplication, currency/unit, historical treatment. | Data steward + QA verification. |
| Time period | Business date, calendar date, transaction date, cutoff, timezone, holiday rules. | Data Governance approval. |
| Filter semantics | Default filters, hidden filters, security filters, inclusion/exclusion rules. | Visible in report metadata and audit. |

# Analytics Data Governance
| Data Asset | Mandatory Governance |
| --- | --- |
| Reporting read model | Owned by bounded context or reporting context, derived from authoritative sources, versioned, tested, and refreshed through governed pipelines. |
| Materialized view | Created/changed through Flyway; refresh policy, locking, performance, access, and invalidation defined. |
| Snapshot | Immutable or controlled mutable snapshot with snapshot_ref, business_date, source_version, retention, and reproducibility. |
| Data mart | Data mart eligibility, ownership, lineage, source contracts, quality rules, access, retention, disposal, and certification are explicit. |
| Data lake/lakehouse | Allowed only through approved architecture and data governance path; derivative status and access boundaries must be documented. |
| Data quality rule | Completeness, validity, uniqueness, referential integrity, timeliness, reconciliation, and anomaly rules are versioned and tested. |
| Privacy and classification | RLS/CLS, masking, minimization, retention, disposal, legal hold, and sensitive data handling are enforced. |

# On-the-Fly Reporting Rules
| Control | Rule |
| --- | --- |
| Query safety | Only approved query patterns, semantic models, or controlled query builders are allowed; no direct production SQL console as reporting feature. |
| RLS/CLS | Row-level and column-level access are enforced in backend/data layer, not only frontend. |
| Rate and export limits | Rate limits, pagination, export limits, timeout, max rows, and resource budgets prevent operational impact. |
| Masking and classification | Restricted fields are masked/redacted; access to Restricted data requires approval and audit. |
| Caching | Cache is derivative, classification-aware, TTL-bound, invalidated safely, and never authority. |
| Audit | Every query and export captures actor, purpose where required, parameters hash, query hash, row count, classification, and evidence_ref. |

# Scheduled and EOD Report Rules
| Rule Area | Mandatory Treatment |
| --- | --- |
| Batch dependency | Scheduled/EOD reports must verify required batch jobs, data refreshes, reconciliation gates, and source completeness. |
| Business date and cutoff | Report output declares business_date, cutoff, timezone, data_snapshot_ref, and report_version. |
| Immutable artifact | Official EOD/regulatory/management report artifacts are immutable after approval; corrections create new version or addendum. |
| Reconciliation binding | Reports using reconciled data must link to reconciliation_ref and exception status. |
| Approval and signoff | Required reports have maker-checker approval before distribution. |
| Distribution evidence | Distribution list, channel, classification, watermark, export format, and retention are recorded. |

# AI-Assisted Analytics Rules
| AI May | AI Must Not |
| --- | --- |
| Summarize, explain, detect anomalies, generate draft narratives, recommend follow-up, and produce candidate insights using approved sources and citations. | Become financial, regulatory, business, or management-report authority. |
| Assist users by explaining report definitions, trends, variances, and possible root causes with confidence, limitation, and source references. | Invent metrics, change semantic definitions, suppress exceptions, approve reports, send external distributions, or expose Restricted data. |
| Create candidate backlog, query optimization suggestions, test cases, and data-quality hypotheses. | Bypass OPA/SBAC, use direct model-provider calls, store sensitive prompts, or mutate production data/model/report definitions. |

# Report Security and Distribution
| Control | Required Treatment | Evidence |
| --- | --- | --- |
| OPA/SBAC and RBAC | Access is role, skill, attribute, classification, tenant, branch/unit, and purpose aware. | Policy decision and access review. |
| Classification-aware distribution | Distribution channel must be eligible for classification; external sharing requires approval. | Distribution evidence and approval. |
| Watermarking | Confidential/Restricted exports include watermark, generated_by, timestamp, and report_run_id where feasible. | Artifact metadata and sample. |
| Download/export controls | Export formats, limits, masking, logging, and retention are enforced. | Export audit and policy test. |
| Email restrictions | Email distribution is controlled by classification and requires approved distribution list. | Distribution list hash and channel record. |
| Support access | Support personnel receive limited, audited, time-bound access; no unrestricted report impersonation. | Support access audit. |
| Legal hold and retention | Reports follow retention, disposal, legal hold, and audit evidence requirements. | Retention/disposal record. |

# Report Evidence and Audit
| Evidence Field | Required Use |
| --- | --- |
| report_run_id | Required for official report runs, dashboards, scheduled reports, EOD reports, extracts, certified datasets, and AI-assisted analytics where applicable. |
| report_version | Required for official report runs, dashboards, scheduled reports, EOD reports, extracts, certified datasets, and AI-assisted analytics where applicable. |
| data_snapshot_ref | Required for official report runs, dashboards, scheduled reports, EOD reports, extracts, certified datasets, and AI-assisted analytics where applicable. |
| query_hash | Required for official report runs, dashboards, scheduled reports, EOD reports, extracts, certified datasets, and AI-assisted analytics where applicable. |
| parameter_hash | Required for official report runs, dashboards, scheduled reports, EOD reports, extracts, certified datasets, and AI-assisted analytics where applicable. |
| source_data_version | Required for official report runs, dashboards, scheduled reports, EOD reports, extracts, certified datasets, and AI-assisted analytics where applicable. |
| generated_by | Required for official report runs, dashboards, scheduled reports, EOD reports, extracts, certified datasets, and AI-assisted analytics where applicable. |
| approved_by | Required for official report runs, dashboards, scheduled reports, EOD reports, extracts, certified datasets, and AI-assisted analytics where applicable. |
| distribution_list | Required for official report runs, dashboards, scheduled reports, EOD reports, extracts, certified datasets, and AI-assisted analytics where applicable. |
| classification | Required for official report runs, dashboards, scheduled reports, EOD reports, extracts, certified datasets, and AI-assisted analytics where applicable. |
| retention | Required for official report runs, dashboards, scheduled reports, EOD reports, extracts, certified datasets, and AI-assisted analytics where applicable. |
| evidence_ref | Required for official report runs, dashboards, scheduled reports, EOD reports, extracts, certified datasets, and AI-assisted analytics where applicable. |
| reconciliation_ref | Required for official report runs, dashboards, scheduled reports, EOD reports, extracts, certified datasets, and AI-assisted analytics where applicable. |
| trace_id | Required for official report runs, dashboards, scheduled reports, EOD reports, extracts, certified datasets, and AI-assisted analytics where applicable. |
| audit_event_id | Required for official report runs, dashboards, scheduled reports, EOD reports, extracts, certified datasets, and AI-assisted analytics where applicable. |

# CI/CD and Report Promotion Gates
| Gate | Blocking Rule |
| --- | --- |
| report definition review | Required before production publication or activation. Critical/High failures block promotion unless formally waived by owner with compensating controls and exit date. |
| semantic layer validation | Required before production publication or activation. Critical/High failures block promotion unless formally waived by owner with compensating controls and exit date. |
| SQL/query review | Required before production publication or activation. Critical/High failures block promotion unless formally waived by owner with compensating controls and exit date. |
| data lineage check | Required before production publication or activation. Critical/High failures block promotion unless formally waived by owner with compensating controls and exit date. |
| performance test | Required before production publication or activation. Critical/High failures block promotion unless formally waived by owner with compensating controls and exit date. |
| access policy test | Required before production publication or activation. Critical/High failures block promotion unless formally waived by owner with compensating controls and exit date. |
| masking/redaction test | Required before production publication or activation. Critical/High failures block promotion unless formally waived by owner with compensating controls and exit date. |
| calculation verification | Required before production publication or activation. Critical/High failures block promotion unless formally waived by owner with compensating controls and exit date. |
| reconciliation test | Required before production publication or activation. Critical/High failures block promotion unless formally waived by owner with compensating controls and exit date. |
| snapshot reproducibility test | Required before production publication or activation. Critical/High failures block promotion unless formally waived by owner with compensating controls and exit date. |
| dashboard test | Required before production publication or activation. Critical/High failures block promotion unless formally waived by owner with compensating controls and exit date. |
| evidence manifest validation | Required before production publication or activation. Critical/High failures block promotion unless formally waived by owner with compensating controls and exit date. |
| contract/schema compatibility | Required before production publication or activation. Critical/High failures block promotion unless formally waived by owner with compensating controls and exit date. |
| authenticated DAST where applicable | Required before production publication or activation. Critical/High failures block promotion unless formally waived by owner with compensating controls and exit date. |
| SBOM/provenance where applicable | Required before production publication or activation. Critical/High failures block promotion unless formally waived by owner with compensating controls and exit date. |

# Lifecycle and Versioning
| Lifecycle State | Meaning |
| --- | --- |
| Draft | Definition is being prepared and must not be used as authority. |
| Review Ready | Definition, lineage, security, tests, and evidence are ready for review. |
| Approved | Approved for controlled publication or non-prod use. |
| Active | Published for intended audience under access and distribution controls. |
| Deprecated | Replaced but retained during migration. |
| Suspended | Blocked due to quality, security, lineage, or evidence issue. |
| Retired | Removed from active use and retained/disposed according to policy. |

# Acceptance Criteria

Report/dashboard/dataset is cataloged with owner, purpose, classification, audience, lineage, semantic definitions, calculations, filters, parameters, refresh, distribution, retention, and evidence.

Semantic metrics, KPIs/KRIs, dimensions, measures, time definitions, aggregation rules, and compatibility are approved.

Access policy, RLS/CLS, masking, export controls, and distribution rules are tested.

Report run is reproducible using data_snapshot_ref, query_hash, parameter_hash, report_version, and source_data_version.

Scheduled/EOD reports bind to batch completion and reconciliation where required.

CI/CD, policy, performance, DAST, evidence, and dashboard tests pass.

AI analytics remain advisory and are source-referenced, classified, confidence-labeled, and human-reviewed.

# RACI and Operating Responsibilities
| Role | RACI | Responsibility |
| --- | --- | --- |
| Business Owner | A/R | Defines business outcome, cutoff, reconciliation tolerance, report meaning, signoff, and exception disposition. |
| Technical Owner | A/R | Owns implementation, runtime configuration, recoverability, tests, observability, and evidence path. |
| Data Steward | R/C | Owns data definitions, quality rules, lineage, classification, retention, and semantic consistency. |
| DevSecOps Lead | R/C | Owns CI/CD gates, scan evidence, provenance, deployment controls, and PR/MR evidence completeness. |
| Operations/SRE | R/C | Owns scheduling, monitoring, incident response, SLO tracking, runbook execution, and post-run review. |
| Security Architecture | A/C | Owns OPA/SBAC, privileged access, service accounts, secrets hygiene, security monitoring, and break-glass review. |
| DBA / Data Engineering | R/C | Owns Flyway migrations, data store performance, backup/restore, partitioning, views, snapshots, and data correction controls. |
| QA/SDET | R/C | Owns deterministic tests, reconciliation tests, restart tests, contract tests, performance tests, and evidence validation. |
| AI Governance | C | Reviews AI-assisted analysis, model routing, guardrails, prompt eligibility, and advisory-only boundaries. |
| Internal Audit | C/I | Reviews evidence completeness, control operation, sampling path, and audit reconstruction readiness. |
| CAB / ARB | A | Approves production-impacting activation, high-risk changes, waivers, and material architectural decisions. |

# Explicitly Rejected Anti-Patterns

Dashboard becomes business authority without governed source and definition.

Same KPI has multiple formulas in different reports.

Report filters are hidden or undocumented.

Exports bypass masking or distribution approval.

Direct SQL access replaces governed reporting APIs or semantic layer.

AI-generated narrative is circulated as approved management/regulatory result.

Report generated after unreconciled EOD is released without exception signoff.

Cache, spreadsheet, or BI extract becomes source of truth.

# Open Reconciliation Items
| ID | Issue | Severity | Owner | Required Evidence |
| --- | --- | --- | --- | --- |
| REG-082-01 | Add AIRA-DOC-082 through AIRA-DOC-085 to canonical register 00A-00D and assign source-pack placement. | High | Solutions Architecture Office / Knowledge Governance | Register update and cross-pack regeneration evidence. |
| REG-082-02 | Validate references to documents 63-81 and Dynamic Workspace 74-75 against the active source baseline and register state. | High | Solutions Architecture Office / Data Governance | 00D reconciliation item with governing source decision. |
| REG-082-03 | Resolve known 11A duplicate numbering and 41B/44 System Builder overlap if cross-references are promoted into these documents. | Medium | Architecture Board | Updated register and supersedence note. |
| REG-082-04 | Confirm physical database schema names, report catalog tables, batch registry tables, and seed ownership through Flyway governance. | High | DBA / Data Governance / DevSecOps | Flyway migration plan, dry-run, checksum, and rollback/forward-fix plan. |

# AVCI Compliance Summary
| AVCI Property | Evidence in This Document |
| --- | --- |
| Attributable | Names document owner, co-owners, business/technical/data owners, source baseline, role responsibilities, run/report owner, checker, approver, and evidence path. |
| Verifiable | Requires tests, policy checks, reconciliation, telemetry, audit events, CI/CD gates, run evidence, report snapshots, dashboards, and approval records. |
| Classifiable | Requires classification for jobs, parameters, inputs, outputs, logs, reports, dashboards, extracts, analytics datasets, AI prompts, evidence, and retention handling. |
| Improvable | Captures incidents, exceptions, failed gates, user feedback, false positives, performance bottlenecks, data-quality defects, and controlled improvement backlog items. |

