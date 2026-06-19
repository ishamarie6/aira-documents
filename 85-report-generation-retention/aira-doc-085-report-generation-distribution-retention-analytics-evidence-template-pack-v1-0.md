---
title: "Report Generation Distribution Retention Analytics Evidence Template Pack"
doc_id: "AIRA-DOC-085"
version: "v1.0"
status: "final"
category: "Report generation and retention"
source_docx: "AIRA-DOC-085_Report_Generation_Distribution_Retention_Analytics_Evidence_Template_Pack_v1.0.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 85-report-generation-retention
  - final
  - aira-doc-085
---



# Report Generation Distribution Retention Analytics Evidence Template Pack



AIRA
AI-Native Enterprise Platform

Report Generation, Distribution, Retention, and Analytics Evidence Template Pack

Template Pack | Report Evidence | Distribution | Retention | Analytics Certification | AI Review

AIRA-DOC-085 | Version v1.0 | INTERNAL CONFIDENTIAL
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-085 |
| Document Title | Report Generation, Distribution, Retention, and Analytics Evidence Template Pack |
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

5. Template Usage Rules

6. Report Catalog Record

7. KPI/KRI Definition Record

8. Semantic Layer Record

9. Report Run Evidence Record

10. Report Distribution Evidence Record

11. Report Approval and Signoff Record

12. Report Exception Record

13. EOD Report Checklist

14. Analytics Dataset Certification Record

15. Dashboard Certification Checklist

16. AI-Assisted Analytics Review Record

17. Report Retention and Disposal Record

18. Report PR/MR Evidence Checklist

19. Evidence Manifest Mapping

20. Acceptance Criteria

21. RACI

22. Anti-Patterns

23. Open Reconciliation Items

24. AVCI Compliance Summary

# Document Control
| Field | Required Value |
| --- | --- |
| Document ID | AIRA-DOC-085 |
| Document Title | Report Generation, Distribution, Retention, and Analytics Evidence Template Pack |
| Version | v1.0 |
| Status | DRAFT FOR ARB, DATA GOVERNANCE, DEVSECOPS, SECURITY, OPERATIONS/SRE, QA/SDET, AI GOVERNANCE, AND INTERNAL AUDIT REVIEW |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Data Governance; Business Operations; DevSecOps Lead; Security Architecture; Operations/SRE; DBA; QA/SDET; AI Governance; Internal Audit |
| Target Audience | Solutions Architects, Product Owners, Batch Operators, Business SMEs, Developers, DevSecOps, SRE, DBA, Security, Data Governance, QA/SDET, Internal Audit |
| Parent Standards | 01/01A/01B AVCI and Enterprise Architecture Standards; 02 Engineering Blueprint; 03 Developer Guide; 04 Technology Stack; 10 through 10E MicroFunction standards; 11 and 11A DevSecOps standards; 15 API and Integration Contract Standard; 16 Database/Flyway standards; 17 Security, Identity, Secrets, and Access Control; 20 CI/CD Evidence Pack; 31/31A Observability and SRE; 63 PRR/ORR; 64 Resilience Lab; 65 Policy-as-Code; 66 Evidence Manifest Schema; 67 API/Event/Schema/DLQ/Replay Governance; 68 Control Objectives and Evidence Traceability Matrix; 71 Data Governance, Retention, Privacy, and Evidence Classification; 77-81 Data/Message Governance family; Dynamic Workspace 54-61 and 74-75. |
| Companion Documents | AIRA-DOC-084 Reporting and Analytics Governance Standard; AIRA-DOC-082 Batch Governance; AIRA-DOC-083 Batch Operations Runbook; 66 Evidence Manifest Schema; 68 Control Objectives and Evidence Traceability Matrix; 71 Data Governance; 77-81 Data and Message Governance family. |
| Review Cadence | Quarterly; unscheduled after Sev-1/Sev-2 incident, failed EOD, material batch/reporting model change, data-quality control failure, regulatory change, or architecture/security control change. |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Reporting-Analytics-Template-Pack / AIRA-DOC-085 / v1.0/ |
| Approval Path | Draft -> Architecture/Data/Security/DevSecOps/SRE/QA/Internal Audit review -> ARB/CAB approval where production-impacting -> Register update -> Controlled publication. |
| Supersedence Rules | This document becomes canonical only after register adoption. Any supersedence, split, merge, or retirement must update document register 00A-00D, evidence paths, cross-references, and downstream implementation impact records. |

## Version History
| Version | Date | Owner | Summary |
| --- | --- | --- | --- |
| v1.0 | 2026-06-18 | Solutions Architecture Office / IT Head | Initial draft for batch, scheduled processing, reporting, analytics, evidence, and operational governance. |

# Mandatory Practice Statement

Mandatory Practice Statement. A report or analytics evidence record is incomplete if it cannot prove owner, source, definition, classification, data snapshot, parameters, query or transformation identity, policy decision, validation evidence, distribution, retention, and improvement path. Templates may be adapted by bounded context, but required fields must not be removed without approved waiver.

# Executive Summary

This template pack operationalizes AIRA-DOC-084 by giving teams reusable, audit-ready records for reports, KPIs/KRIs, semantic objects, report runs, distribution, approvals, exceptions, EOD reporting, analytics certification, dashboard certification, AI-assisted analytics review, retention/disposal, and PR/MR evidence. These templates are intended for Word, Obsidian projection, ticket forms, Git-managed YAML/JSON records, and future registry-backed implementation.

# Purpose, Scope, and Authority

The template pack applies to all official AIRA reports, dashboards, extracts, semantic objects, analytics datasets, data marts, scheduled reports, EOD reports, management reports, regulatory reports, and AI-assisted analytics narratives. It supports both manual evidence capture during early maturity and registry-backed automated capture when implementation matures.

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

# Template Usage Rules

Templates must be stored in Git-managed source or approved document repository and projected to Obsidian only as governed knowledge.

Required fields cannot be removed. Not applicable fields require reason and approver.

Restricted/Confidential content must not be copied into template summaries unless the repository and audience are eligible for that classification.

Template records must link to evidence_ref, source_ref, ticket, PR/MR, run_id, report_run_id, or audit_event_id where applicable.

Automation may pre-fill templates, but named human owners must review and approve authoritative records.

# Report Catalog Record
| Field | Required Entry / Control |
| --- | --- |
| report_id | Unique immutable identifier |
| report_code | Stable business-readable code |
| report_name | Approved display name |
| report_type | Operational/EOD/regulatory/management/exception/dashboard/dataset/export/AI-generated analysis |
| business_owner | Accountable owner |
| technical_owner | Implementation owner |
| steward | Data/semantic steward |
| classification | Public/Internal/Confidential/Restricted plus handling |
| audience | Eligible roles/skills/groups |
| purpose | Business reason and decision supported |
| source_data | Authoritative sources and source versions |
| canonical_data_elements | Links to data dictionary and message catalog |
| business_definition | Approved definition and exclusions |
| calculation_rules | Formula, aggregation, precision, rounding |
| filters | Default/hidden/security filters |
| parameters | User/system parameters |
| refresh_frequency | Refresh schedule or trigger |
| freshness_SLO | Maximum accepted staleness |
| distribution_rule | Channels and recipients |
| retention_rule | Retention/disposal/legal hold |
| export_formats | Allowed formats |
| masking_rule | Masking/redaction/RLS/CLS |
| approval_required | Yes/No plus approver role |
| evidence_ref | Evidence path |
| lifecycle_state | Draft/Review Ready/Approved/Active/Deprecated/Suspended/Retired |

# KPI/KRI Definition Record
| Field | Required Entry / Control |
| --- | --- |
| metric_code | Stable code |
| metric_name | Approved name |
| type | KPI or KRI |
| business_owner | Accountable owner |
| steward | Data steward |
| definition | Business definition |
| formula | Formula and calculation rules |
| grain | Level of detail |
| time_period | Time definition and cutoff |
| target_thresholds | Target, warning, breach |
| directionality | Higher/lower/within range is better |
| source_data | Authoritative source |
| classification | Handling |
| review_cadence | Review frequency |
| evidence_ref | Approval and test evidence |

# Semantic Layer Record
| Field | Required Entry / Control |
| --- | --- |
| semantic_object_id | Unique ID |
| object_type | Metric/dimension/measure/filter/time-period |
| name | Approved name |
| definition | Semantic definition |
| owner | Business/data owner |
| source_lineage | Source and transformation path |
| grain | Data grain |
| aggregation_rule | Sum/count/average/distinct/last/etc. |
| filter_semantics | Default and security filters |
| version | Semantic version |
| compatibility | Backward compatibility and deprecation |
| approval_ref | Approval workflow |
| evidence_ref | Validation evidence |

# Report Run Evidence Record
| Field | Required Entry / Control |
| --- | --- |
| report_run_id | Unique run identifier |
| report_id | Catalog reference |
| report_version | Definition version |
| business_date | Business date |
| generated_at | Timestamp |
| generated_by | Service/user identity |
| data_snapshot_ref | Snapshot/source version |
| query_hash | Query/transformation hash |
| parameter_hash | Parameters hash |
| row_count | Rows generated |
| classification | Classification |
| reconciliation_ref | Reconciliation reference if applicable |
| trace_id | Trace |
| audit_event_id | Audit event |
| evidence_ref | Evidence manifest |

# Report Distribution Evidence Record
| Field | Required Entry / Control |
| --- | --- |
| distribution_id | Unique ID |
| report_run_id | Report run |
| channel | Workspace/email/API/file/share |
| distribution_list | Recipients or hashed list reference |
| classification | Handling |
| watermark_applied | Yes/No/NA |
| export_format | Format |
| sent_at | Timestamp |
| sent_by | Service/user |
| external_sharing_approval | Approval ref if applicable |
| retention_rule | Retention |
| audit_event_id | Audit event |
| evidence_ref | Evidence |

# Report Approval and Signoff Record
| Field | Required Entry / Control |
| --- | --- |
| approval_id | Unique ID |
| report_run_id | Report run |
| approval_type | Definition/run/distribution/exception |
| maker | Prepared by |
| checker | Reviewed by |
| approver | Approved by |
| approval_decision | Approved/rejected/waived |
| decision_reason | Reason |
| open_exceptions | Exception refs |
| effective_period | Effective date/range |
| evidence_ref | Evidence |

# Report Exception Record
| Field | Required Entry / Control |
| --- | --- |
| exception_id | Unique ID |
| report_run_id | Report run |
| exception_type | Data/definition/access/performance/distribution/evidence |
| severity | Critical/High/Medium/Low/Info |
| description | Summary |
| affected_data | Scope |
| business_impact | Impact |
| owner | Assigned owner |
| target_resolution | Date |
| disposition | Fix/rerun/waive/forward-fix/retire |
| approval_ref | Approval or waiver |
| evidence_ref | Evidence |

# EOD Report Checklist
| Field | Required Entry / Control |
| --- | --- |
| business_date | Business date |
| batch_completion_ref | EOD batch completion |
| reconciliation_ref | Reconciliation result |
| report_list | Reports generated |
| snapshot_ref | Data snapshot |
| exceptions_reviewed | Yes/No |
| approval_ref | Signoff |
| distribution_ref | Distribution evidence |
| retention_ref | Retention record |
| handoff_ref | Operational handoff |

# Analytics Dataset Certification Record
| Field | Required Entry / Control |
| --- | --- |
| dataset_id | Unique ID |
| dataset_name | Name |
| owner | Business owner |
| technical_owner | Technical owner |
| steward | Data steward |
| purpose | Approved use |
| source_lineage | Source and transformations |
| quality_rules | Rules and results |
| freshness_SLO | Freshness |
| classification | Handling |
| access_policy | OPA/SBAC/RLS/CLS |
| retention | Retention/disposal |
| certification_status | Draft/certified/suspended/retired |
| evidence_ref | Certification evidence |

# Dashboard Certification Checklist
| Field | Required Entry / Control |
| --- | --- |
| dashboard_id | Unique ID |
| dashboard_name | Name |
| owner | Owner |
| audience | Eligible audience |
| widgets | Widget list |
| source_reports_datasets | Sources |
| metric_definitions | Semantic links |
| access_test | Policy test result |
| performance_test | Result |
| visual_validation | Result |
| drilldown_rules | Allowed drilldown |
| export_controls | Controls |
| evidence_ref | Evidence |

# AI-Assisted Analytics Review Record
| Field | Required Entry / Control |
| --- | --- |
| ai_review_id | Unique ID |
| related_report_or_dataset | Report/dataset |
| prompt_template_ref | Approved template |
| model_route | LiteLLM alias |
| guardrail_result | Input/retrieval/execution/output guardrails |
| source_references | Citations/lineage |
| confidence_or_limitations | Confidence/limitations |
| classification | Handling |
| human_reviewer | Reviewer |
| approved_use | Internal explanation/draft narrative/backlog only/etc. |
| prohibited_use_checked | Authority, regulatory, financial, and access decisions not delegated to AI |
| evidence_ref | Evidence |

# Report Retention and Disposal Record
| Field | Required Entry / Control |
| --- | --- |
| retention_id | Unique ID |
| artifact_ref | Report/dataset/export |
| classification | Handling |
| retention_rule | Rule |
| legal_hold_status | None/active |
| disposal_due | Date |
| disposal_method | Approved method |
| disposal_approver | Approver |
| disposal_evidence | Evidence |
| exceptions | Exceptions |

# Report PR/MR Evidence Checklist
| Field | Required Entry / Control |
| --- | --- |
| pr_mr_ref | PR/MR |
| change_type | New/update/deprecate/retire |
| catalog_updated | Yes/No |
| semantic_validation | Result |
| query_review | Result |
| lineage_review | Result |
| performance_test | Result |
| access_policy_test | Result |
| masking_test | Result |
| calculation_test | Result |
| reconciliation_test | Result |
| snapshot_reproducibility | Result |
| dashboard_test | Result |
| evidence_manifest | Evidence |
| rollback_forward_fix | Plan |
| approvals | Maker/checker/CODEOWNERS/CAB/ARB as required |

# Evidence Manifest Mapping
| Evidence Dimension | Required Template Links |
| --- | --- |
| Attribution | Report Catalog Record; KPI/KRI Definition; Semantic Layer Record; Approval and Signoff Record. |
| Verification | Report Run Evidence; Dataset Certification; Dashboard Certification; PR/MR Evidence Checklist. |
| Classification | All records include classification, access, masking, distribution, retention, and legal hold where applicable. |
| Improvement | Report Exception Record; AI-Assisted Analytics Review; PR/MR backlog and post-implementation review. |
| Reversibility | PR/MR Evidence Checklist; Retention and Disposal Record; versioning/deprecation path. |

# Acceptance Criteria

Templates cover all required report, KPI/KRI, semantic, run, distribution, approval, exception, EOD, certification, AI review, retention, and PR/MR evidence scenarios.

Template records can be stored as Word, Markdown projection, YAML/JSON, ticket form, or registry data without losing required fields.

Every template supports owner, classification, source, verification evidence, retention, and improvement path.

Templates are approved for controlled use and updated in the document/register baseline.

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

Removing mandatory fields to simplify evidence collection.

Copying Confidential/Restricted raw data into evidence summaries where not required.

Using a template record as approval when no named approver exists.

Treating AI-generated report narrative as approved signoff.

Creating spreadsheet-only report definitions outside Git/registry governance.

Retaining exports without retention/disposal rule.

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

