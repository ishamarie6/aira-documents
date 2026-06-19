---
title: "Enterprise Data Dictionary Reference Data Naming MDM Data Quality Governance Standard"
doc_id: "AIRA-DOC-094"
version: "v1.0"
status: "final"
category: "Enterprise data dictionary"
source_docx: "AIRA-DOC-094_Enterprise_Data_Dictionary_Reference_Data_Naming_MDM_Data_Quality_Governance_Standard_v1.0.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 94-enterprise-data-dictionary
  - final
  - aira-doc-094
---



# Enterprise Data Dictionary Reference Data Naming MDM Data Quality Governance Standard



AIRA
AI-Native Enterprise Platform

Enterprise Data Dictionary, Reference Data, Naming, Master Data Management, and Data Quality Governance Standard

Canonical field stewardship | Reference data | Naming | MDM | Data quality | Lineage
| Property | Value |
| --- | --- |
| Document ID | AIRA-DOC-094 |
| Version | v1.0 |
| Status | DRAFT FOR ARB / CAB / GOVERNANCE REVIEW |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Generated | 2026-06-18 09:43 +08:00 |
| Approval Path | Document owner -> Enterprise Architecture -> Product/Data/Security/DevSecOps/Operations as applicable -> ARB/CAB approval |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Governance / AIRA-DOC-094 / v1.0/ |

Discipline First - Automation Second - Intelligence Third - AVCI Always

# 1. Document Control
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-094 |
| Document Title | Enterprise Data Dictionary, Reference Data, Naming, Master Data Management, and Data Quality Governance Standard |
| Version | v1.0 |
| Status | DRAFT FOR ARB / CAB / GOVERNANCE REVIEW |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Data Governance; DBA; Enterprise Architecture; Product Owner; Business Data Owners; Security Architecture; DevSecOps; QA/SDET; Reporting/Analytics Owner; Internal Audit |
| Primary Audience | Data Owners, Data Stewards, DBAs, Architects, Developers, QA/SDET, Product Owners, Reporting/BI, Security, DevSecOps, Internal Audit |
| Parent Standards | AIRA-DOC-090 / 090A, 01B, 02, 10-10E, 15/15A, 16/16A/16B, 17/17A, 26A, 33, 34, 82-89 |
| Companion Documents | AIRA-DOC-091 product governance, AIRA-DOC-092 NFR governance, AIRA-DOC-093 config governance, AIRA-DOC-084/085 reporting and analytics governance |
| Review Cadence | Quarterly; unscheduled on material business, architecture, platform, data, security, operations, or AI-governance change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Governance / AIRA-DOC-094 / v1.0/ |
| Approval Path | Maker: document owner; Checker: Enterprise Architecture, Security, DevSecOps, Data Governance, QA/SDET, SRE as applicable; Approver: ARB/CAB or delegated governance forum. |
| Supersedence Rules | This document does not supersede the canonical baseline. It extends it. If conflicts appear, the stricter AIRA control governs and the issue must be logged in 00D as an AVCI reconciliation item. |

## Mandatory Practice Statement

No AIRA data field, reference value, message attribute, database column, report measure, analytics metric, AI retrieval attribute, or evidence attribute may be considered governed merely because it exists in code, a table, a screen, or a report. It is governed only when it is defined in an approved dictionary or registry, owned, classified, named consistently, validated, versioned, mapped across layers, quality-tested, lineage-linked, protected, retained, and evidence-producing.

# 2. Executive Summary

This standard closes the data dictionary, reference data, MDM, naming, data quality, and lineage gap identified by AIRA-DOC-090 and 090A. It complements AIRA-DOC-086 on validation and cross-layer consistency by establishing the governed enterprise data dictionary and master/reference data control model that ensures fields, values, identifiers, and meanings remain consistent across frontend, backend, APIs, events, databases, reports, analytics, logs, audit, and AI workflows.
| Data Governance Outcome | Required Result |
| --- | --- |
| Consistent field meaning | Canonical field definitions govern frontend variables, DTOs, API schemas, event payloads, DB columns, reports, logs, audit, and evidence. |
| Controlled reference data | Reference values are owned, versioned, classified, effective-dated, and promoted through approved paths. |
| MDM readiness | Master data domains define system of record, matching, survivorship, stewardship, reconciliation, and quality rules. |
| Data quality evidence | Quality dimensions, rules, tests, exceptions, and remediation are measured and evidenced. |
| Lineage and auditability | Data origin, transformation, persistence, report usage, retention, and disposal are reconstructable. |

# 3. Purpose, Scope, and Authority

The purpose is to define the enterprise data governance standard for data dictionary, reference data, naming, master data management, data quality, and lineage across AIRA. This document is the governing source for canonical field stewardship unless ARB consolidates it with AIRA-DOC-086 in a future release.
| In Scope | Out of Scope |
| --- | --- |
| Canonical field registry, data dictionary, naming conventions, reference data, MDM domains, field-level classification, cross-layer mapping, data quality, lineage, data ownership, data retention, and evidence. | Replacing database/Flyway standards, API contracts, validation standards, or reporting governance. This standard defines data meaning and stewardship; companion standards enforce implementation. |
| Frontend variables, backend DTOs, API schemas, event schemas, database columns, report fields, semantic metrics, logs, audit, evidence, and AI/RAG metadata. | Unmanaged spreadsheets, undocumented report fields, ad hoc reference values, or shadow master data. |

# 4. Enterprise Data Domains and Ownership
| Data Domain | Examples | Owner / Steward | Governance Notes |
| --- | --- | --- | --- |
| Party / Customer | person, organization, contact, identity reference | Business Data Owner / Data Steward | Requires classification, privacy, matching, survivorship, and consent/legal handling. |
| Account / Loan / Facility | loan_id, account status, balances, schedules, servicing state | Business Owner / Data Steward | High financial integrity; reconciliation and audit required. |
| Property / Collateral | property_id, address, appraisal, title, collateral status | Business Owner / Data Steward | Lineage to documents, valuations, and reports required. |
| Workflow / Case | case_id, task, status, SLA, approval, timer | Operations / Product Owner | State transitions and maker-checker evidence required. |
| Reference Data | status codes, types, calendars, reason codes, severity codes | Data Governance / Domain Steward | Versioned, effective-dated, and controlled. |
| Reporting / Analytics | KPI, measure, dimension, semantic metric | BI Owner / Data Governance | Lineage, quality, access, retention, and meaning control. |
| Evidence / Audit | trace_id, evidence_ref, policy_decision_id, run_id | Internal Audit / Architecture | Immutable or append-only where required. |

# 5. Canonical Data Dictionary Fields
| Field | Purpose |
| --- | --- |
| field_code | Stable canonical identifier used across code, contracts, data, reports, logs, and evidence. |
| field_name | Business-readable name. |
| business_definition | Approved business meaning and allowed interpretation. |
| owning_bounded_context | Domain that owns the meaning and lifecycle of the field. |
| data_type / length / precision / scale | Canonical type constraints for frontend, API, event, backend, database, and reports. |
| allowed_values / reference_set | Reference data set, enum, lookup, or governed value domain. |
| format / regex / validation_rule | Cross-layer validation rule and error/message code linkage. |
| classification | Public, Internal, Confidential, Restricted, plus handling rule. |
| masking / redaction / encryption | Security and privacy treatment in UI, logs, reports, storage, and AI retrieval. |
| source_of_truth | Authoritative system, table, API, owner, or external source. |
| cross_layer_mapping | Frontend, DTO, API, event, DB, report, analytics, audit, evidence mappings. |
| retention / lineage | Retention rule, lineage path, evidence path, disposal rule. |
| quality_rules | Completeness, validity, uniqueness, consistency, timeliness, accuracy, reconciliation rules. |
| lifecycle_state | draft, approved, active, deprecated, retired, revoked. |

# 6. Naming Standards
| Layer | Naming Rule |
| --- | --- |
| Canonical field | Use stable snake_case field_code; avoid ambiguous abbreviations; one meaning per field_code. |
| Frontend variables | May use camelCase for TypeScript, but must map to canonical field_code and generated/typed schema. |
| Backend DTOs | Use names aligned with API contract and canonical registry; no hidden translation without mapping record. |
| Database columns | Use snake_case, bounded-context schema, clear suffixes for _id, _code, _at, _by, _ref, _hash, _status. |
| Events and messages | Use schema-registry-controlled names; include version, source, subject, correlation fields where applicable. |
| Reports and analytics | Use business-approved label plus semantic metric definition; no report-only redefinition of core fields. |
| Logs / audit / evidence | Use standard correlation names: trace_id, span_id, correlation_id, request_id, evidence_ref, policy_decision_id. |

# 7. Reference Data Governance
| Reference Data Control | Required Treatment |
| --- | --- |
| Reference Set Registry | reference_set_code, owner, steward, classification, allowed values, effective dates, lifecycle state. |
| Value Definition | value_code, label, description, meaning, active_from, active_to, sort_order, deprecated_by. |
| Promotion | Reference data changes use Git/Flyway/approved admin workflow, maker-checker, tests, and evidence. |
| Compatibility | Deprecation must preserve backward compatibility where APIs/events/reports depend on value codes. |
| Audit | Reference changes record who changed what, why, approval, before/after hash, and evidence_ref. |
| No hardcoding | Business reference values must not be hardcoded in UI, controller, service, report, or workflow code. |

# 8. Master Data Management Model
| MDM Element | Required Definition |
| --- | --- |
| Master Domain | customer, account, loan, property, organization, product, user, branch, reference, or other approved domain. |
| System of Record | Authoritative source, ownership, update path, and conflict resolution. |
| Identity and Matching | Natural keys, surrogate keys, matching rules, duplicate detection, merge/split policy. |
| Survivorship | Rule for resolving conflicts among sources and timestamps. |
| Golden Record | Canonical record or composite view, if applicable, with lineage to source records. |
| Stewardship | Data owner, data steward, review cadence, exception queue, remediation path. |
| Reconciliation | Completeness, duplicate, balance, status, and downstream consumer reconciliation rules. |

# 9. Data Quality Governance
| Quality Dimension | Examples of Evidence |
| --- | --- |
| Completeness | Required fields present; missing data exceptions tracked by rule_id and field_code. |
| Validity | Field values conform to dictionary, validation rule, reference set, schema, and format. |
| Uniqueness | Duplicate customers, accounts, cases, documents, or reference values are detected and stewarded. |
| Consistency | Cross-layer and cross-system values agree or have approved transformation lineage. |
| Timeliness | Data freshness, update SLA, report refresh, batch cutoff, and event lag are measured. |
| Accuracy | Business verification, source-of-truth confirmation, reconciliation, or sampling evidence exists. |
| Integrity | Referential integrity, lineage, audit trail, immutability, and reconciliation prove trust. |

# 10. Lineage and Cross-Layer Mapping

Every critical field must map across frontend component, DTO, OpenAPI schema, AsyncAPI/Avro schema, domain model, database column, report field, analytics metric, log/audit/evidence field, and AI/RAG metadata where applicable.

Lineage must capture source, transformation, validation, persistence, event publication, report/analytics usage, retention, and disposal.

Data transformations must be owned by adapters, mappers, or data pipeline components; domain logic must not depend on transport or persistence naming conventions.

Cross-layer drift must be detected through schema tests, dictionary validation, migration checks, report validation, and architecture fitness functions.

# 11. CI/CD and Architecture Fitness Functions

Reject new API/event/database/report fields without dictionary entry or approved exception.

Reject database migrations that introduce unclassified fields or naming-standard violations.

Reject report measures without semantic definition, owner, lineage, and reconciliation rule.

Reject hardcoded reference values in UI, backend, workflow, report, or policy code where reference registry is required.

Reject cross-layer type/length/nullability mismatches between dictionary, API, DTO, event, database, and report definitions.

Reject AI/RAG retrieval metadata that lacks source authority, classification, freshness, and lineage.

# 12. Templates
| Template | Required Fields |
| --- | --- |
| Canonical Field Dictionary Entry | field_code, definition, type, length, context, classification, validation, mapping, owner, quality, lineage |
| Reference Set Register | reference_set_code, owner, steward, classification, value list, effective dates, lifecycle |
| Master Data Domain Register | domain_code, system_of_record, matching_rule, survivorship_rule, steward, quality_rules |
| Data Quality Rule Register | dq_rule_id, field_code, dimension, rule, severity, test, threshold, owner, evidence_ref |
| Lineage Record | lineage_id, source, transformation, target, validation, report_usage, retention, evidence_ref |
| Naming Waiver Record | waiver_id, affected artifact, deviation, reason, risk, approval, exit plan |

# Governance and RACI
| Role | Primary Responsibility | Evidence |
| --- | --- | --- |
| Data Owner | Owns meaning, value, usage, classification, and business quality of data domain. | Approved dictionary/domain records. |
| Data Steward | Maintains field definitions, reference data, quality rules, exceptions, and remediation. | Dictionary, reference register, DQ issue records. |
| DBA | Enforces schema naming, constraints, Flyway governance, indexing, and data integrity. | Migration validation, schema checks. |
| Enterprise Architecture | Ensures bounded context, contract, lineage, and cross-layer consistency. | Architecture review and fitness checks. |
| QA/SDET | Tests validation, data quality, schema compatibility, and regression. | Test reports and DQ evidence. |
| Reporting / Analytics Owner | Owns semantic measures, dashboard definitions, report lineage, and reconciliation. | Semantic layer and report evidence. |
| Security / Data Privacy | Owns classification, masking, redaction, encryption, and access rules. | Security review and policy evidence. |

# 13. Acceptance Criteria

Critical fields have approved dictionary entries before production use.

Reference data is governed, versioned, effective-dated, tested, and auditable.

Master data domains define system of record, matching, survivorship, stewardship, quality, and reconciliation.

Cross-layer mappings remain consistent across UI, backend, API, events, database, reports, audit, evidence, and AI metadata.

Data quality rules and lineage evidence are available for critical reports, analytics, integrations, and batch jobs.

Naming deviations are formally waived with risk, approval, and exit plan.

# 14. Open Issues and Consolidation Decision

Register this document in 00A-00D and source-pack roadmap.

ARB may later consolidate this document with AIRA-DOC-086 if a single data validation and dictionary standard is preferred. Until then, 086 governs validation and cross-layer consistency; 094 governs data meaning, stewardship, reference data, MDM, quality, and lineage.

Update 15/15A, 16/16B, 26A, 33, 84/85, 86/87, and 90/90A with cross-references.

# AVCI Compliance Summary
| AVCI Property | Evidence in This Standard |
| --- | --- |
| Attributable | Assigns data owner, steward, DBA, report owner, security, and architecture accountability for fields and data domains. |
| Verifiable | Requires dictionary, reference registers, quality tests, lineage, schema checks, report reconciliation, and evidence. |
| Classifiable | Field-level classification, masking, redaction, encryption, retention, and retrieval eligibility are mandatory. |
| Improvable | Data quality issues, lineage gaps, naming waivers, reference-data defects, and report disputes feed remediation and backlog. |

