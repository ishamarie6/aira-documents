---
title: "Initial Canonical Data Dictionary Domain Code and Message Error Seed Catalog"
doc_id: "AIRA-79"
version: "v1.0"
status: "final"
category: "Canonical seed catalog"
source_docx: "AIRA_79_Initial_Canonical_Data_Dictionary_Domain_Code_and_Message_Error_Seed_Catalog_v1.0.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 79-canonical-seed-catalog
  - final
  - aira-79
---



# Initial Canonical Data Dictionary Domain Code and Message Error Seed Catalog



AIRA
AI-Native Enterprise Platform

Initial Canonical Data Dictionary, Domain Code,
and Message/Error Seed Catalog

AIRA-DOC-079 | Version v1.0

Canonical Seed Catalog | Cross-Layer Consistency | Message/Error Codes | Flyway Seed Baseline | Runtime Lookup | AVCI Evidence

# Document Control
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-079 |
| Document Title | AIRA Initial Canonical Data Dictionary, Domain Code, and Message/Error Seed Catalog |
| Version | v1.0 |
| Status | Draft for Architecture Review Board, Data Governance, DevSecOps, Security, QA/SDET, Operations, AI Governance, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Data Governance; Software Development; API/Integration Architecture; DBA; DevSecOps; Security Architecture; QA/SDET; SRE/Operations; AI Governance; Internal Audit |
| Primary Parents | AIRA-DOC-077 Canonical Data Element, Variable, Message, and Error Code Governance Standard; AIRA-DOC-078 Physical Schema, Flyway Seeder, and Admin Workflow Guide |
| Companion Sources | AIRA-DOC-020 CI/CD Evidence Pack Guide; AIRA-DOC-065 Policy-as-Code; AIRA-DOC-066 Evidence Manifest; AIRA-DOC-067 API/Event/DLQ/Replay; AIRA-DOC-071 Data Governance; MicroFunction and Dynamic Workspace standards |
| Review Cadence | Quarterly; unscheduled on material data dictionary, message catalog, API/event, database, policy, evidence, observability, Dynamic Workspace, MicroFunction, or AI generation change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Canonical-Data-and-Message-Catalog / 079 / v1.0 / |

Mandatory Practice Statement

No AIRA implementation may introduce, seed, reference, render, validate, log, emit, translate, or expose a data element, domain code, layer code, severity code, message code, or error code unless the seed record is registered, classified, versioned, mapped, validated, seeded through controlled configuration or Flyway, and linked to AVCI-complete evidence. Seed records are not informal examples. Once approved, they become controlled runtime and CI/CD inputs for frontend, backend, API, event, database, policy, observability, evidence, System Builder, and AI-assisted generation paths.

# Static Table of Contents

1. Executive Summary

2. Purpose, Scope, and Authority

3. Seed Catalog Governance Model

4. Domain, Layer, Severity, and Lifecycle Code Sets

5. Initial Canonical Data Element Seed Catalog

6. Initial Message and Error Code Seed Catalog

7. Runtime Lookup, API, Event, and Database Binding Rules

8. Flyway and Seeder Implementation Baseline

9. Admin Maker-Checker Workflow

10. CI/CD, Policy-as-Code, and Evidence Gates

11. RACI

12. Acceptance Criteria, Anti-Patterns, and AVCI Summary

# 1. Executive Summary

This document provides the initial controlled seed catalog for the AIRA canonical data dictionary, domain-code taxonomy, severity model, and message/error catalog. It operationalizes AIRA-DOC-077 and AIRA-DOC-078 by defining the first enterprise-grade seed records that should be used by generated code, Dynamic Workspace components, MicroFunctions, APIs, events, PostgreSQL/Flyway schema, OPA/SBAC policy inputs, evidence manifests, logs, traces, audit events, support workflows, and AI-assisted generation tools.

The strategic purpose is to stop field drift and message drift before they become defects. AIRA must not allow a field to mean one thing in TypeScript, another in Java, a different length in PostgreSQL, a different enum in OpenAPI, and a different label in logs or dashboards. Likewise, messages and errors must not be scattered as hardcoded strings without code, severity, solution, owner, classification, correlation, and support action.
| Outcome | Required Result |
| --- | --- |
| Cross-layer consistency | Field names, types, lengths, validation rules, enum values, classification, and mappings remain compatible across UI, API, backend, events, database, policy, evidence, and tests. |
| Message governance | Messages and errors have stable codes, severities, safe user messages, technical descriptions, causes, solutions, retry guidance, observability fields, and lifecycle status. |
| Runtime reuse | Services, MicroFunctions, Dynamic Workspace widgets, AI assistants, and integration adapters can look up approved definitions instead of inventing local variants. |
| Evidence by construction | Every seed record can be traced to owner, version, classification, seeder, approval, validation gate, and evidence reference. |

# 2. Purpose, Scope, and Authority
| Area | Required Treatment |
| --- | --- |
| Purpose | Define the initial seed baseline for canonical data elements, code sets, and messages/errors required for enterprise-grade AIRA consistency and supportability. |
| In Scope | Data elements, variables, attributes, API properties, event fields, DB columns, OPA inputs, runtime parameters, messages, errors, warnings, logs, audit events, evidence fields, and AI prompt variables. |
| Out of Scope | Unapproved business-specific field definitions that have no steward, hardcoded messages, local-only enums, direct production seeding, manual DDL, uncontrolled spreadsheet catalogs, and AI-invented runtime definitions. |
| Authority | This document is a seed catalog and operational companion. AIRA-DOC-077 governs policy. AIRA-DOC-078 governs physical schema and seeding. Stricter controls in parent standards prevail. |
| Conflict Rule | If a seed definition conflicts with API, database, data governance, security, MicroFunction, Dynamic Workspace, or evidence standards, block promotion, record an AVCI reconciliation item, and route through owner review. |

# 3. Seed Catalog Governance Model
| Lifecycle State | Meaning | Promotion Rule |
| --- | --- | --- |
| candidate | Proposed field/message/code not yet approved. | May appear in draft PR/MR only; cannot be used as runtime authority. |
| review_ready | Complete record submitted for maker-checker review. | Requires owner, steward, classification, mapping, tests, and evidence. |
| approved | Approved for seeding and controlled use. | May be inserted by Flyway/controlled seeder and referenced by contracts. |
| active | Available for runtime lookup and CI/CD validation. | Can be used by frontend/backend/API/event/database/policy/evidence layers. |
| deprecated | Still accepted for compatibility but no longer preferred. | Requires migration guidance, replacement code, and removal timeline. |
| retired | No longer accepted for new use. | References must fail CI unless waiver exists. |
| revoked | Unsafe or invalid record. | Runtime use blocked; incident/reconciliation evidence required. |

# 4. Domain, Layer, Severity, and Lifecycle Code Sets
| Code Type | Seed Values | Notes |
| --- | --- | --- |
| Domain Codes | AUTH, USER, MF, DW, API, EVT, DB, POL, AI, SEC, OBS, CICD, DATA, SYS, INT, CFG | Used in message codes, evidence records, policy inputs, dashboards, and owner routing. |
| Layer Codes | UI, API, SVC, MF, POL, DB, EVT, OBS, AI, CICD, INT, CFG | Identifies where a message or field is emitted, validated, or enforced. |
| Severity Codes | FATAL, ERROR, WARN, INFO, DEBUG, TRACE | Severity is operational behavior. It is not the same as data classification. |
| Classification Codes | PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED, EVIDENCE_SENSITIVE, SECURITY_SENSITIVE | Controls handling, retention, redaction, model-route eligibility, and visibility. |
| Lifecycle Codes | CANDIDATE, REVIEW_READY, APPROVED, ACTIVE, DEPRECATED, RETIRED, REVOKED | Controls whether a record can be seeded, referenced, rendered, or blocked. |

# 5. Initial Canonical Data Element Seed Catalog
| ID | Canonical Name | Type | Length | Class | Definition | Layers | Validation / Use Rule |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CDE-SYS-TRACE-ID | trace_id | String | 64 | CONFIDENTIAL | End-to-end distributed trace identifier. | UI/API/SVC/EVT/OBS/AUDIT/EVIDENCE | Required on critical flows; no PII; regex safe ID. |
| CDE-SYS-CORRELATION-ID | correlation_id | String | 64 | CONFIDENTIAL | Cross-request business/process correlation identifier. | API/SVC/EVT/OBS/AUDIT | Propagate across APIs/events; safe for support display when redacted policy allows. |
| CDE-SYS-EVIDENCE-REF | evidence_ref | String | 96 | EVIDENCE_SENSITIVE | Pointer to retained evidence pack or evidence record. | CI/CD/API/OBS/AUDIT/DW/MF | Must not expose raw evidence content to unauthorized users. |
| CDE-SEC-CLASSIFICATION | classification | Enum | 32 | INTERNAL | Data/artifact classification label. | All layers | Allowed values from classification seed set; controls routing and masking. |
| CDE-SEC-POLICY-DECISION-ID | policy_decision_id | String | 96 | SECURITY_SENSITIVE | OPA/SBAC decision correlation ID. | POL/API/SVC/MF/DW/OBS | Required for protected actions and policy denials. |
| CDE-MF-TRANSACTION-CODE | microfunction_transaction_code | String | 80 | INTERNAL | Governed MicroFunction transaction code. | UI/API/SVC/MF/OBS/AUDIT | Must match registered MicroFunction catalog entry. |
| CDE-SYS-IDEMPOTENCY-KEY | idempotency_key | String | 128 | CONFIDENTIAL | Deduplication key for mutating requests/events. | UI/API/SVC/EVT/DB | Required for retry/replay-sensitive flows. |
| CDE-MSG-MESSAGE-CODE | message_code | String | 48 | INTERNAL | Canonical message/error code. | UI/API/SVC/MF/EVT/OBS | Pattern AIRA-{DOMAIN}-{LAYER}-{SEVERITY}-{NNNN}. |
| CDE-SYS-ACTOR-ID-HASH | actor_id_hash | String | 128 | CONFIDENTIAL | Hashed actor/user/service identity for telemetry. | UI/API/SVC/OBS/AUDIT | No raw user ID in logs unless policy-approved. |
| CDE-SYS-TENANT-ID | tenant_id | String | 64 | CONFIDENTIAL | Tenant or organizational context identifier. | UI/API/SVC/DB/OBS | Required for tenant-scoped records; avoid high-cardinality metric labels. |
| CDE-SYS-CREATED-AT | created_at | OffsetDateTime / timestamptz | N/A | INTERNAL | Creation timestamp. | API/SVC/DB/EVT/EVIDENCE | UTC / timezone-aware; ISO-8601 in APIs. |
| CDE-SYS-UPDATED-AT | updated_at | OffsetDateTime / timestamptz | N/A | INTERNAL | Last update timestamp. | API/SVC/DB/EVIDENCE | UTC / timezone-aware; update through governed persistence adapter. |

## 5.1 Type and Mapping Seed Baseline
| Conceptual Type | TypeScript | Java | OpenAPI / JSON Schema | PostgreSQL | Default Rule |
| --- | --- | --- | --- | --- | --- |
| Identifier | string | String / UUID when native UUID | type: string; format: uuid or pattern | uuid or varchar(64/96/128) | Use UUID for generated internal IDs; use varchar for externally shaped IDs. |
| Code | string enum | Enum or value object | enum; maxLength | varchar(32/48/80) + check/ref table | Codes are uppercase stable values; no local enum drift. |
| Message Code | string | String value object | pattern AIRA-* | varchar(48) unique | Must be globally unique and registered. |
| Timestamp | string | OffsetDateTime | format: date-time | timestamptz | UTC; timezone-aware; no local-only timestamps. |
| Money / Amount | number/string | BigDecimal | type number; multipleOf or string for precision | numeric(19,4) | No floating-point money. |
| Percentage | number | BigDecimal | number; min/max | numeric(7,4) | Define scale and bounds. |
| Flag | boolean | boolean / Boolean | boolean | boolean | Default value must be explicit. |
| JSON Metadata | object | JsonNode / Map | object with schema if stable | jsonb | Classify, validate, and avoid dumping uncontrolled payloads. |

# 6. Initial Message and Error Code Seed Catalog
| Code | Severity | Domain/Layer | User-Safe Message | Description / Cause | Solution / Action | Retryable | Evidence / Handling |
| --- | --- | --- | --- | --- | --- | --- | --- |
| AIRA-AUTH-API-ERROR-0001 | ERROR | AUTH/API | Login session cannot be established. | Identity token, policy, or session context validation failed. | Retry login. If repeated, contact support with correlation ID. | No | Log safe; audit required; no token exposure. |
| AIRA-AUTH-POL-WARN-0001 | WARN | AUTH/POL | Access requires additional verification. | Policy requires step-up, approval, or elevated validation. | Complete the required verification or request access through the approved workflow. | Yes | Policy decision ID required. |
| AIRA-MF-RUNTIME-FATAL-0001 | FATAL | MF/MF | MicroFunction runtime cannot continue safely. | Mandatory identity, classification, policy, audit, or runtime configuration is unavailable. | Stop protected action, raise incident, and use rollback or safe-disable plan. | No | Incident and evidence pack required. |
| AIRA-EVT-DLQ-ERROR-0001 | ERROR | EVT/EVT | Event moved to DLQ. | Consumer failed after approved retry policy or schema validation failed. | Review DLQ evidence, repair if approved, and replay through controlled runbook. | Maybe | DLQ/replay evidence required. |
| AIRA-DB-FLYWAY-ERROR-0001 | ERROR | DB/DB | Database migration validation failed. | Checksum, order, compatibility, or clean-migrate validation failed. | Block promotion. Correct migration through PR/MR and DBA review. | No | Flyway evidence required. |
| AIRA-DW-UI-WARN-0001 | WARN | DW/UI | Workspace component hidden by policy. | OPA/SBAC policy denied or filtered a component/action. | User may request access if business need exists. | No | No technical details to end user. |
| AIRA-AI-GRD-WARN-0001 | WARN | AI/AI | AI output requires guardrail review. | Guardrail confidence, classification, or source citation rule requires human review. | Route to human checker; do not use output as authority. | No | Model route and guardrail evidence required. |
| AIRA-CICD-GATE-ERROR-0001 | ERROR | CICD/CICD | Promotion gate failed. | Required tests, scans, policy, evidence, or approval is missing or failed. | Fix failing gate or obtain formal waiver with expiry and owner. | No | Evidence manifest must record decision. |
| AIRA-DATA-CATALOG-ERROR-0001 | ERROR | DATA/SVC | Unregistered data element used. | Code, schema, message, policy, or migration references a field not in the canonical dictionary. | Register candidate, obtain approval, seed catalog, and update mappings. | No | CI should block. |
| AIRA-MSG-CATALOG-ERROR-0001 | ERROR | DATA/SVC | Unregistered message code used. | Code, UI, API, or event references a message code not in the canonical catalog. | Register message with owner, severity, cause, solution, and evidence. | No | CI should block. |

## 6.1 Message Record Mandatory Fields
| Field | Required Meaning |
| --- | --- |
| message_code | Globally unique code using AIRA-{DOMAIN}-{LAYER}-{SEVERITY}-{NNNN}. |
| message_key | Localization-ready key, stable across languages and UI variants. |
| severity | FATAL, ERROR, WARN, INFO, DEBUG, TRACE. |
| category / subcategory | Business, security, validation, integration, runtime, policy, data, AI, observability, or CI/CD category. |
| user_message | Safe wording for users; no stack traces, secrets, raw PII, tokens, or internal-only detail. |
| technical_message | Internal diagnostic detail visible only by role, classification, and support workflow. |
| cause and solution | Cause summary plus user, developer, operator, and security action when applicable. |
| mappings | HTTP status, API error response, event/DLQ, log level, audit, evidence, localization, and observability mapping. |
| lifecycle | Candidate, approved, active, deprecated, retired, or revoked. |

# 7. Runtime Lookup, API, Event, and Database Binding Rules

Frontend forms, generated clients, Dynamic Workspace widgets, and AI Assistant Panel responses must use canonical field definitions and message keys instead of local hardcoded variants.

Backend DTOs, value objects, validators, exception handlers, and MicroFunction runtime envelopes must reference canonical data_element_id and message_code where practical.

OpenAPI, AsyncAPI, Avro/JSON Schema, and CloudEvents payloads must carry compatible type, length, enum, classification, correlation, and error mappings.

Database columns, constraints, indexes, enum/reference tables, and seed data must be traceable to canonical data element records.

OPA/Rego input schemas must use registered canonical names and classification labels; policy decisions must emit policy_decision_id and message_code for denials.

Logs, traces, metrics, audit events, Sentry issues, Loki queries, Tempo traces, Grafana dashboards, and evidence manifests must use registered correlation and evidence fields.

# 8. Flyway and Seeder Implementation Baseline
| Artifact | Required Baseline |
| --- | --- |
| V079_001__create_canonical_seed_catalog_baseline.sql | Creates base schema/tables or extends AIRA-DOC-078 physical schema for seed records where not already present. |
| V079_002__seed_domain_layer_severity_lifecycle_codes.sql | Seeds domain codes, layer codes, severity codes, classification codes, and lifecycle states. |
| V079_003__seed_initial_canonical_data_elements.sql | Seeds initial common data elements such as trace_id, correlation_id, evidence_ref, classification, idempotency_key, message_code, and timestamps. |
| V079_004__seed_initial_message_error_catalog.sql | Seeds the initial enterprise message/error codes and default English user-safe messages. |
| R__canonical_catalog_validation_views.sql | Creates validation views for duplicate code detection, orphan mappings, inactive references, and missing classification. |
| R__canonical_catalog_runtime_projection.sql | Creates approved read views or materialized views for runtime lookup, admin review, and evidence export. |

## 8.1 Copy-Ready Seed Record Sketch

-- Example only. Final physical names must follow AIRA-DOC-078 and approved Flyway naming.
insert into aira_catalog.message_catalog
(message_code, severity_code, domain_code, layer_code, message_key, user_message,
 technical_message, retryable, classification, lifecycle_state, owner, evidence_ref)
values
('AIRA-DATA-CATALOG-ERROR-0001', 'ERROR', 'DATA', 'SVC',
 'data.catalog.unregistered_element',
 'A required data definition is not registered. Please contact support with the correlation ID.',
 'Unregistered canonical data element reference detected by validation gate.',
 false, 'INTERNAL', 'ACTIVE', 'Data Governance', 'EVD-CATALOG-SEED-V079-004');

# 9. Admin Maker-Checker Workflow
| Step | Maker Action | Checker / Approver Control | Evidence |
| --- | --- | --- | --- |
| Create candidate | Data/message steward submits new or changed record. | System validates completeness, uniqueness, and classification. | Candidate record, source_ref, owner, draft evidence. |
| Impact analysis | System Builder/GitNexus identifies affected UI/API/event/DB/policy/tests. | Architecture/Data/Security review impact and severity. | Impact summary and affected artifact list. |
| Review | Maker responds to comments and attaches mappings/tests. | Checker validates type/length, message safety, remediation guidance, and policy impact. | Review comments and gate results. |
| Approve | Record becomes approved for seed promotion. | Data Governance, Security, DevSecOps, DBA, ARB/CAB as required. | Approval record and evidence_ref. |
| Seed / activate | Flyway or controlled configuration seeder promotes record. | CI/CD verifies runtime projection and no drift. | Flyway report, hashes, validation views, evidence manifest. |
| Monitor / improve | Usage, support tickets, incidents, and defects reviewed. | Deprecate, revise, or expand catalog through same workflow. | Improvement backlog and lifecycle change record. |

# 10. CI/CD, Policy-as-Code, and Evidence Gates
| Gate | Blocking Condition | Evidence Required |
| --- | --- | --- |
| Data dictionary completeness | Field/property/column/event/policy input is not mapped to active canonical data element. | data-dictionary-validation.json and mapping report. |
| Type/length compatibility | Frontend/backend/API/event/database definitions are incompatible. | cross-layer-field-diff.json. |
| Enum/reference drift | Enum value appears in code/schema/database but not in approved seed catalog. | enum-drift-report.json. |
| Message catalog uniqueness | Duplicate, malformed, deprecated, or unregistered message code is used. | message-catalog-validation.json. |
| Message safety | User message exposes stack trace, token, secret, raw PII, or internal-only detail. | message-redaction-test.json. |
| Localization readiness | UI-visible message lacks localization key or fallback. | localization-key-validation.json. |
| Policy alignment | OPA input or denial message uses unregistered field/message. | opa/conftest result and policy_decision_id. |
| Evidence manifest binding | Seed change lacks owner, approval, hash, classification, retention, or rollback/deprecation path. | evidence-manifest.json. |

## 10.1 OPA/Conftest Policy Sketch

package aira.catalog

deny[msg] {
  input.kind == "api_schema"
  field := input.fields[_]
  not field.data_element_id
  msg := sprintf("Unregistered field: %s", [field.name])
}

deny[msg] {
  input.kind == "message_reference"
  not startswith(input.message_code, "AIRA-")
  msg := sprintf("Invalid AIRA message code: %s", [input.message_code])
}

deny[msg] {
  input.kind == "telemetry"
  forbidden := {"password", "token", "raw_jwt", "secret", "raw_pii"}
  forbidden[input.field_name]
  msg := sprintf("Forbidden telemetry field: %s", [input.field_name])
}

# 11. RACI
| Activity | Architecture / IT Head | Data Governance | Development | DBA | DevSecOps | Security | QA/SDET | SRE/Ops | AI Gov | Audit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Approve seed governance | A/R | R | C | C | C | C | C | C | C | I |
| Maintain data element catalog | A | A/R | R | C | C | C | C | C | C | I |
| Maintain message/error catalog | A | A/R | R | C | C | R | C | R | C | I |
| Review DB/Flyway seeds | A | C | C | A/R | C | C | C | I | I | I |
| Implement CI validation | A | C | C | C | A/R | C | R | C | C | I |
| Approve security-sensitive messages | A | C | C | C | C | A/R | C | C | C | I |
| Review evidence completeness | A | R | R | R | R | R | R | R | R | A/R |

# 12. Acceptance Criteria, Anti-Patterns, and AVCI Summary
| Acceptance Criterion | Pass Condition |
| --- | --- |
| Seed baseline exists | Domain, layer, severity, classification, lifecycle, initial data elements, and initial message/error records are defined and seedable. |
| Cross-layer validation works | CI can detect unregistered fields/messages, type/length drift, enum drift, unsafe messages, and missing mappings. |
| Runtime lookup is controlled | Approved records can be resolved by services/UI/policies through governed read paths and caches are non-authoritative. |
| Message catalog is support-ready | Each message has code, severity, audience, cause, solution, actions, retryability, classification, and evidence mapping. |
| AVCI evidence exists | Seed changes produce owner, source, classification, test, approval, seeder, hash, retention, and improvement evidence. |

## 12.1 Anti-Patterns and Rejection Rules

Reject any field/property/column/event attribute introduced without a canonical data_element_id and classification.

Reject inconsistent UI/API/backend/database lengths, precision, scale, formats, or enum values.

Reject hardcoded UI/backend messages that bypass the canonical message catalog.

Reject message/error records without cause, solution, support/developer/operator action, retryability, and classification.

Reject logs, errors, prompts, evidence, screenshots, or telemetry that include passwords, raw tokens, raw JWTs, secrets, raw PII, embeddings, or uncontrolled customer payloads.

Reject direct production changes to catalog tables outside Flyway or approved controlled configuration workflow.

Reject AI-generated fields/messages unless submitted as candidates and approved through maker-checker review.

## 12.2 Open Reconciliation Items
| ID | Item | Treatment | Owner |
| --- | --- | --- | --- |
| RI-079-001 | Propagate AIRA-DOC-077/078/079 references into API, database, Dynamic Workspace, MicroFunction, CI/CD, observability, evidence manifest, and System Builder standards. | Track through 00E and affected source registers. | Solutions Architecture Office |
| RI-079-002 | Define final physical schema naming if AIRA-DOC-078 implementation differs from this seed sketch. | DBA/Data Governance decision before first Flyway implementation. | DBA / Data Governance |
| RI-079-003 | Map existing message strings and database columns from PoC repositories to canonical records. | Perform GitNexus/code scan and seed candidate backlog. | Development / GitNexus / Data Governance |
| RI-079-004 | Resolve all duplicate numbering and System Builder overlap references through canonical register. | Do not silently renumber; record supersedence and authority. | Architecture Board |

## 12.3 AVCI Compliance Summary
| AVCI Property | How AIRA-DOC-079 Satisfies It |
| --- | --- |
| Attributable | Defines owner, steward, bounded context, source reference, seed migration, approval path, and lifecycle state for every initial data/message seed record. |
| Verifiable | Requires schema validation, uniqueness checks, cross-layer mapping checks, type/length compatibility checks, message safety tests, Flyway evidence, and CI/CD evidence. |
| Classifiable | Requires classification and handling rules for every data element, message, evidence field, telemetry field, and runtime lookup. |
| Improvable | Provides lifecycle states, deprecation paths, usage analytics, support feedback, incident linkage, catalog drift detection, and backlog-driven improvement. |

Initial Seed Catalog - Controlled by Governance, Enforced by CI/CD, Proven by Evidence - AVCI Always

