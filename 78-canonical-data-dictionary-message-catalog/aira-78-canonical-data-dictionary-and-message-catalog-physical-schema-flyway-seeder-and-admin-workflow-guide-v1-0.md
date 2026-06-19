---
title: "Canonical Data Dictionary and Message Catalog Physical Schema Flyway Seeder and Admin Workflow Guide"
doc_id: "AIRA-78"
version: "v1.0"
status: "final"
category: "Canonical data dictionary and message catalog"
source_docx: "AIRA_78_Canonical_Data_Dictionary_and_Message_Catalog_Physical_Schema_Flyway_Seeder_and_Admin_Workflow_Guide_v1.0.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 78-canonical-data-dictionary-message-catalog
  - final
  - aira-78
---



# Canonical Data Dictionary and Message Catalog Physical Schema Flyway Seeder and Admin Workflow Guide



AIRA
AI-Native Enterprise Platform

Canonical Data Dictionary and Message Catalog Physical Schema, Flyway Seeder, and Admin Workflow Guide

AIRA-DOC-078 | Version v1.0 | Physical Registry | Flyway Seeder | Admin Maker-Checker Workflow | AVCI Evidence
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-078 |
| Document Title | AIRA Canonical Data Dictionary and Message Catalog Physical Schema, Flyway Seeder, and Admin Workflow Guide |
| Version | v1.0 |
| Status | Draft for ARB, Data Governance, Security, DevSecOps, DBA, QA/SDET, SRE/Ops, AI Governance, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Data Governance; DBA; API/Integration Architecture; Software Development; DevSecOps; Security Architecture; QA/SDET; SRE/Ops; AI Governance; Internal Audit |
| Primary Parent | AIRA-DOC-077 Canonical Data Element, Variable, Message, and Error Code Governance Standard v1.0 |
| Companion Sources | 01/01A/01B; 10-10E MicroFunction; 11/11A DevSecOps; 15/15A API; 16/16A/16B Database/Flyway; 20 CI/CD; 65 Policy-as-Code; 66 Evidence Manifest; 67 API/Event/DLQ/Replay; 68 Traceability Matrix; 71 Data Governance; 73 System Builder; 74/75 Dynamic Workspace Certification; 76 Fitness Gates |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Canonical-Data-Dictionary-Message-Catalog / 078 / v1.0 / |

Mandatory Practice Statement

No AIRA canonical data element, variable, message, error code, enum value, database column, API/event field, policy input, prompt variable, evidence field, or runtime parameter may be activated unless it is registered in the canonical physical registry, seeded or migrated through Flyway or an approved governed configuration path, approved through maker-checker workflow, validated by CI/CD gates, mapped across consuming layers, observable, reversible, and AVCI-evidenced.

# Static Table of Contents

1. Executive Summary

2. Purpose, Scope, and Authority

3. Physical Registry Control Model

4. PostgreSQL Schema and Table Baseline

5. Flyway Migration and Seeder Governance

6. Admin Workflow and Maker-Checker Controls

7. Runtime Lookup, Caching, and API Exposure

8. CI/CD, Policy-as-Code, and Architecture Fitness Gates

9. Security, Classification, Retention, and Audit Controls

10. Integration with AIRA Standards and Runtime Components

11. Templates, RACI, Acceptance Criteria, and AVCI Summary

# 1. Executive Summary

AIRA-DOC-077 defines what canonical data elements and message/error codes must contain. This guide defines how that governance becomes executable through a PostgreSQL/Flyway-backed physical registry, seed-data lifecycle, admin workflow, runtime lookup services, CI/CD validators, policy-as-code gates, and evidence records. The goal is to prevent cross-layer drift between TypeScript, Java, OpenAPI, AsyncAPI, Avro/JSON Schema, PostgreSQL, OPA/Rego, MicroFunction runtime configuration, Dynamic Workspace, observability, evidence manifests, tests, and integrations.
| Strategic Result | Required Outcome |
| --- | --- |
| Single authoritative registry | PostgreSQL/Flyway is the authoritative registry for approved data elements, mappings, message codes, enum values, lifecycle states, and seed batches. Redis, generated clients, UI bundles, docs, dashboards, and AI summaries are derivative. |
| Consistency by construction | Field type, length, precision, validation, enum, message code, localization key, and classification are validated before merge and before runtime activation. |
| Controlled catalog change | New or changed fields/messages require maker-checker workflow, impact analysis, schema bindings, test evidence, rollback/deprecation plan, and approved seed/migration path. |
| Runtime-safe use | Frontend, backend, MicroFunction, API/event, OPA/SBAC, AI prompts, logs, and evidence use cataloged codes and data element IDs instead of unregistered ad hoc strings. |
| Audit-ready operations | Every activation, deprecation, seed batch, cache refresh, rejected change, and runtime lookup emits traceable evidence and audit records. |

Figure 1. Canonical data dictionary and message catalog control plane.

# 2. Purpose, Scope, and Authority
| Area | Required Treatment |
| --- | --- |
| Purpose | Define the physical schema, Flyway migration/seeder pattern, admin workflow, runtime access model, validation gates, and evidence requirements for AIRA canonical data dictionary and message catalog implementation. |
| Scope | Data elements, variables, fields, messages, errors, warnings, enum values, database columns, API/event attributes, policy inputs, prompt variables, evidence fields, localization keys, and observability mappings. |
| Authority | This guide implements AIRA-DOC-077 and inherits stronger controls from AVCI, Enterprise Architecture, Database/Flyway, API/Event, DevSecOps, Policy-as-Code, Data Governance, Evidence Manifest, Dynamic Workspace, and System Builder standards. |
| Conflict Rule | When a field or message definition conflicts with an API schema, database column, generated client, UI validation, event schema, OPA input, or evidence manifest, the stricter governance rule applies until the conflict is logged, owned, classified, and reconciled through the canonical register. |

# 3. Physical Registry Control Model

The canonical registry must not be a passive spreadsheet. It is a controlled runtime and engineering authority used by CI/CD, code generators, schema generators, System Builder, Dynamic Workspace, MicroFunction runtime, OPA/SBAC, error handling, localization, observability, evidence manifests, and admin workflows. The registry stores approved meaning and lifecycle state; generated artifacts consume it but do not become authority.
| Control Principle | Implementation Rule |
| --- | --- |
| Authoritative storage | PostgreSQL schemas managed by Flyway. All tables, indexes, constraints, views, seed data, enum values, and reference records are migration-controlled. |
| Derivative projections | Generated TypeScript types, Java DTO/value objects, OpenAPI/AsyncAPI fragments, JSON Schema, Avro, message bundles, UI localization files, and dashboards are regenerated from approved registry records. |
| Runtime safety | Unknown, expired, revoked, draft-only, or unapproved field/message records fail closed in protected runtime paths. |
| Evidence binding | Each register record links to source_ref, change_request_id, approval_record_id, seed_batch_id, evidence_ref, and audit_event_id. |
| Lifecycle enforcement | Draft -> Review -> Approved -> Active -> Deprecated -> Retired -> Revoked. Production use requires Active status unless an approved migration/deprecation path exists. |

Figure 2. Canonical registry physical schema model.

# 4. PostgreSQL Schema and Table Baseline

The physical schema below is a logical baseline. Final names may be adjusted by the database register, but the implementation must preserve ownership, classification, evidence correlation, Flyway-only change control, RLS/least-privilege access, auditability, and rollback/deprecation behavior.
| Schema | Purpose | Representative Tables |
| --- | --- | --- |
| aira_catalog | Core catalog authority | catalog_namespace, catalog_record, lifecycle_state, approval_status, seed_batch, register_audit |
| aira_catalog_data | Canonical data element registry | data_element, data_element_version, data_element_mapping, validation_rule, enum_domain, enum_value |
| aira_catalog_msg | Message and error catalog | message_catalog, message_version, message_translation, remediation_action, message_channel_binding |
| aira_catalog_bind | Cross-layer binding | api_schema_binding, event_schema_binding, db_column_binding, policy_input_binding, ui_component_binding, evidence_field_binding |
| aira_catalog_admin | Admin workflow | change_request, impact_analysis, approval_record, waiver_record, deprecation_plan, publication_record |
| aira_catalog_obs | Observability and evidence | catalog_runtime_event, catalog_lookup_metric, catalog_cache_event, evidence_binding, redaction_test_result |

## 4.1 Mandatory Table Groups
| Table | Required Purpose |
| --- | --- |
| data_element | Stores canonical field identity, definition, ownership, classification, type, length, precision, scale, format, nullability, default, allowed values, validation profile, masking, retention, lifecycle and evidence. |
| data_element_mapping | Maps one canonical element to frontend property, Java field, OpenAPI property, AsyncAPI/Avro field, PostgreSQL column, OPA input, log/audit/evidence field, and test fixture name. |
| validation_rule | Stores reusable validation rules such as required, min/max length, regex, range, enum, uniqueness, checksum, date/timezone rule, money precision, redaction, and policy dependency. |
| message_catalog | Stores message_code, message_key, severity, category, source layer, user message, technical message, cause, solution, remediation, retryable flag, HTTP mapping, DLQ mapping, localization, classification, lifecycle and evidence. |
| message_translation | Stores locale-specific user-safe text, accessibility instructions, UI display constraints, and approval status. |
| enum_domain / enum_value | Stores reusable code sets with lifecycle, compatibility rule, external mapping, deprecation rule, and test expectation. |
| change_request / approval_record | Stores maker-checker, impact analysis, approvers, ARB/CAB triggers, waivers, seed batch, evidence pack, and release record. |
| catalog_runtime_event | Stores runtime lookup, cache refresh, rejected lookup, unknown code, drift event, and evidence correlation events. |

## 4.2 Minimum Physical Column Baseline
| Column Group | Minimum Columns |
| --- | --- |
| Registry identity | id uuid, code varchar(80), version_semver varchar(20), namespace varchar(80), tenant_scope varchar(80), bounded_context varchar(80) |
| Ownership | owner_id varchar(80), steward_id varchar(80), approver_role varchar(80), source_ref varchar(200), change_request_id uuid |
| Classification | classification varchar(30), handling_rule_code varchar(80), retention_rule_code varchar(80), redaction_rule_code varchar(80) |
| Lifecycle | lifecycle_state varchar(30), effective_from timestamptz, effective_to timestamptz, deprecated_from timestamptz, retired_at timestamptz |
| Evidence | evidence_ref varchar(120), evidence_pack_id varchar(120), approval_record_id uuid, seed_batch_id uuid, audit_event_id uuid |
| Integrity | record_hash varchar(128), source_hash varchar(128), created_at timestamptz, updated_at timestamptz, created_by varchar(80), updated_by varchar(80) |

# 5. Flyway Migration and Seeder Governance

The registry is delivered through Flyway. Flyway creates schemas, tables, indexes, constraints, RLS policies, lookup views, seed-batch tracking, and approved baseline seed data. Runtime admin changes may create candidate records, but approved production activation must still be traceable to a controlled seed/migration or approved configuration seeder path.
| Migration | Required Content |
| --- | --- |
| V078_001__create_catalog_schemas.sql | Create aira_catalog, aira_catalog_data, aira_catalog_msg, aira_catalog_bind, aira_catalog_admin, aira_catalog_obs schemas. |
| V078_002__create_catalog_core_tables.sql | Create catalog_record, lifecycle_state, seed_batch, audit base tables, common constraints, and indexes. |
| V078_003__create_data_element_tables.sql | Create data_element, data_element_version, data_element_mapping, validation_rule, enum_domain, enum_value. |
| V078_004__create_message_catalog_tables.sql | Create message_catalog, message_version, message_translation, remediation_action, message_channel_binding. |
| V078_005__create_binding_and_admin_tables.sql | Create API/event/db/policy/UI/evidence bindings plus change_request, impact_analysis, approval_record, waiver_record. |
| V078_006__seed_core_domains.sql | Seed lifecycle states, severity levels, classification codes, source layers, mapping types, data type registry, and reserved message-code domains. |
| V078_007__create_views_and_policy.sql | Create catalog lookup views, validation views, RLS policies, read-only runtime roles, and admin workflow roles. |
| R078__seed_message_catalog.sql | Repeatable seed for approved message catalog records; checksum and row-count evidence are captured per seed batch. |

## 5.1 Copy-Ready Flyway Baseline Excerpt

-- V078_001__create_catalog_schemas.sql
create schema if not exists aira_catalog;
create schema if not exists aira_catalog_data;
create schema if not exists aira_catalog_msg;
create schema if not exists aira_catalog_bind;
create schema if not exists aira_catalog_admin;
create schema if not exists aira_catalog_obs;

-- Core lifecycle reference. Physical implementation may expand fields, but must not weaken AVCI.
create table if not exists aira_catalog.lifecycle_state (
  state_code varchar(30) primary key,
  display_name varchar(80) not null,
  is_runtime_eligible boolean not null default false,
  requires_approval boolean not null default true,
  description text not null
);

create table if not exists aira_catalog_data.data_element (
  data_element_id uuid primary key,
  canonical_name varchar(120) not null unique,
  bounded_context varchar(80) not null,
  classification varchar(30) not null,
  data_type varchar(40) not null,
  length integer null,
  precision_value integer null,
  scale_value integer null,
  format_pattern varchar(200) null,
  nullable boolean not null default false,
  lifecycle_state varchar(30) not null references aira_catalog.lifecycle_state(state_code),
  evidence_ref varchar(120) not null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

## 5.2 Seeder Rules
| Seeder Rule | Required Treatment |
| --- | --- |
| Seed batch identity | Every seed run records seed_batch_id, migration_version, source commit, checksum, source file, environment, approver, row counts and evidence_ref. |
| Idempotency | Seed scripts use deterministic natural keys and upsert only approved reference records. Silent overwrites of active meanings are prohibited. |
| Promotion safety | Draft records may exist in non-prod. Production runtime lookup exposes only Active records and approved deprecation aliases. |
| Rollback and repair | Each seed batch defines reversal, deactivation, supersedence, or forward-fix path. Destructive deletes are prohibited unless approved and evidence-backed. |
| Cache invalidation | Approved seed changes trigger catalog cache invalidation, generated-artifact refresh, and post-refresh lookup validation evidence. |

# 6. Admin Workflow and Maker-Checker Controls

Figure 3. Admin maker-checker workflow for data dictionary and message catalog changes.
| Workflow Step | Required Control |
| --- | --- |
| Request creation | Maker submits new or changed field/message with source_ref, owner, classification, business definition, technical definition, mapping, validation, evidence need, and desired effective date. |
| Reuse analysis | Catalog steward checks whether an existing element/message can be reused. Duplicates are rejected or merged through supersedence. |
| Impact analysis | System identifies affected frontend forms, Java DTOs, OpenAPI/AsyncAPI schemas, Avro/JSON Schema, database columns, OPA inputs, tests, logs, dashboards, evidence manifests, integrations, and support runbooks. |
| Review routing | Data Governance, Enterprise Architecture, DBA, Security, API Architecture, DevSecOps, QA/SDET, SRE/Ops, AI Governance, and Internal Audit are routed based on risk and change type. |
| Approval | Checker validates semantics, type/length, validation, security, observability, localization, deprecation, seed plan, rollback, and evidence before Active status. |
| Publication | Approved records generate seed batch, registry update, derived schema fragments, message bundles, documentation projection, cache refresh, and evidence manifest update. |
| Monitoring | Runtime unknown-field, unknown-message, validation-failure, message-code collision, and drift events feed the improvement backlog and control assurance cycle. |

# 7. Runtime Lookup, Caching, and API Exposure

Runtime systems must resolve canonical data and message records through controlled lookup APIs or generated immutable bundles. Direct database access from business logic is prohibited. Lookup failure for protected fields/messages fails closed or returns a safe fallback message code according to policy.
| Runtime Capability | Required Rule |
| --- | --- |
| Read API | Internal catalog API exposes approved Active records by data_element_id, canonical_name, message_code, locale, bounded_context, classification, and version. |
| Generated bundles | Frontend messages, TypeScript types, Java enums/value classes, API schema fragments, and test fixtures are generated from approved registry snapshots. |
| Cache model | Redis/Valkey may cache registry snapshots by version/hash but is not authority. Cache refresh emits audit event, trace_id, catalog_version, and evidence_ref. |
| Safe fallback | Unknown user-facing error returns a generic safe message with correlation_id. Technical details remain in protected logs/evidence only. |
| Localization | User messages use localization keys and approved translations. Technical message and remediation remain role-protected. |
| System Builder use | System Builder may propose records and generate bindings only from Active or approved candidate records. It must not invent production semantics. |

# 8. CI/CD, Policy-as-Code, and Architecture Fitness Gates
| Gate | Blocking Rule |
| --- | --- |
| DATA-001 Registry completeness | Reject data element without owner, steward, classification, data type, length/precision rule, validation rule, mapping, lifecycle state, and evidence_ref. |
| DATA-002 Cross-layer type drift | Reject API/event/frontend/backend/database mismatch unless compatibility waiver and migration plan are approved. |
| DATA-003 Enum drift | Reject enum value in code, database, schema, or OPA input if not registered in enum_domain/enum_value. |
| MSG-001 Code uniqueness | Reject duplicate message_code, duplicate message_key, invalid domain/layer/severity format, or reused retired code. |
| MSG-002 Remediation completeness | Reject error/warning without description, cause, recommended solution, retryability, support/developer/operator action, classification, and evidence_ref. |
| MSG-003 Hardcoded message | Reject hardcoded UI/backend user messages for catalog-governed flows unless explicitly allowed for bootstrap failure. |
| OBS-001 Unsafe telemetry | Reject logs/traces/errors containing passwords, tokens, raw JWTs, secrets, raw PII, raw prompts, account numbers, embeddings, private keys, or uncontrolled customer payloads. |
| DB-001 Unregistered column | Reject Flyway migration that adds a data-bearing column without canonical data_element and db_column_binding. |
| POL-001 Policy input drift | Reject Rego/OPA input field not mapped to a canonical data element or approved policy-only field. |
| EVD-001 Evidence manifest binding | Reject release evidence missing catalog version, seed batch, schema compatibility, validation reports, and message-code uniqueness result. |

## 8.1 OPA/Conftest Policy Sketch

package aira.catalog.gates

deny[msg] {
  input.kind == "openapi_schema"
  field := input.fields[_]
  not field.data_element_id
  msg := sprintf("Unregistered API field: %s", [field.name])
}

deny[msg] {
  input.kind == "message_catalog"
  rec := input.records[_]
  not startswith(rec.message_code, "AIRA-")
  msg := sprintf("Invalid AIRA message code: %s", [rec.message_code])
}

deny[msg] {
  input.kind == "flyway_migration"
  col := input.new_columns[_]
  not col.canonical_mapping_exists
  msg := sprintf("Database column without canonical mapping: %s.%s", [col.table, col.name])
}

# 9. Security, Classification, Retention, and Audit Controls
| Security Area | Mandatory Control |
| --- | --- |
| Classification | Every catalog record declares classification and handling rules. Restricted or Security-Sensitive records cannot be exposed to UI, logs, AI prompts, LLM Wiki, screenshots, or broad retrieval unless explicitly permitted. |
| Least privilege | Runtime readers, admin makers, checkers, seeders, auditors, and System Builder roles use separate DB/API roles and SBAC permissions. |
| RLS and audit | PostgreSQL RLS or equivalent access controls protect admin and sensitive views. All create/update/deprecate/activate/revoke events are append-only audit events. |
| Retention | Catalog records are retained for lineage. Retired/deprecated records remain for traceability unless disposal is legally required and approved. |
| Secrets and PII | Catalog records must not store actual secret values, raw PII, raw tokens, or sample production data. Examples use synthetic and redacted values only. |
| Evidence sensitivity | Evidence references may identify protected evidence packs, but user-facing/runtime catalogs must not expose confidential evidence content. |

# 10. Integration with AIRA Standards and Runtime Components
| Source / Component | Required Binding |
| --- | --- |
| AIRA-DOC-077 | Defines canonical data/message governance semantics; this document implements physical schema, seeders, and admin workflow. |
| AIRA-DOC-020 / 066 | CI/CD and evidence manifest must capture catalog version, seed batch, validation gates, schema compatibility, message-code uniqueness, and PR/MR approval evidence. |
| AIRA-DOC-065 / 076 | Policy-as-Code and executable fitness gates enforce catalog registration, type consistency, message code uniqueness, field mappings, and safe telemetry. |
| AIRA-DOC-067 | API/event/schema/DLQ/replay governance consumes data_element mappings, enum lifecycle, message codes, error responses, and DLQ/replay remediation guidance. |
| AIRA-DOC-071 | Data classification, retention, privacy, redaction, and disposal rules govern catalog fields and message text. |
| MicroFunction 10-10E | MicroFunction runtime parameters, standard steps, errors, audit, outbox, idempotency, and evidence fields must use canonical records. |
| Dynamic Workspace 53-61, 74-75 | UI labels, validation messages, widget errors, AI Assistant Panel messages, accessibility text, policy-denied messages, and telemetry fields must come from approved catalog records. |
| System Builder 73 | System Builder may draft catalog candidates, generated schemas, seed scripts, and admin workflow proposals but cannot activate them without maker-checker approval. |

# 11. Templates, RACI, Acceptance Criteria, and AVCI Summary

## 11.1 Canonical Data Element Record Template
| Field | Example / Required Value |
| --- | --- |
| data_element_id | UUID generated by registry; stable across versions. |
| canonical_name | customer_id, account_status_code, transaction_amount, evidence_ref. |
| business_definition | Plain-language business meaning. |
| technical_definition | Layer-neutral technical meaning and constraints. |
| type attributes | data_type, length, precision, scale, format, nullable, default, validation rules. |
| mappings | frontend, backend, API, event, DB, policy, observability, evidence, tests. |
| governance | owner, steward, classification, retention, lifecycle, approval, deprecation, evidence_ref. |

## 11.2 Message/Error Code Record Template
| Field | Example / Required Value |
| --- | --- |
| message_code | AIRA-AUTH-API-ERROR-0001 |
| message_key | auth.login.invalid_context |
| severity | Fatal, Error, Warn, Info, Debug, or Trace. |
| messages | user_message, technical_message, description, cause, recommended_solution. |
| actions | support_action, developer_action, operator_action, security_action, retryable, compensation impact. |
| bindings | HTTP status, API error response, DLQ event, log level, audit event, evidence_ref, localization key. |
| governance | owner, bounded_context, classification, lifecycle, version, deprecation rule. |

## 11.3 RACI
| Role | RACI | Responsibility |
| --- | --- | --- |
| Solutions Architecture / IT Head | A/R | Owns standard, resolves cross-document conflicts, approves material exceptions and release-train adoption. |
| Data Governance | A/R | Owns data definition quality, stewardship, classification alignment, retention and glossary semantics. |
| DBA | A/R | Owns physical schema, Flyway migrations, seed integrity, indexes, RLS, and database evidence. |
| API / Integration Architecture | R | Owns OpenAPI, AsyncAPI, schema registry, event mapping, external mappings and compatibility evidence. |
| Software Development | R | Uses generated types/messages and avoids unregistered fields, hardcoded messages and drift. |
| DevSecOps | R | Automates CI/CD, policy, schema, message-code, seed and evidence validations. |
| Security Architecture | A/R | Owns secrets hygiene, safe errors, policy denials, redaction, classification and security-sensitive messages. |
| QA/SDET | R | Owns validation, localization, regression, schema compatibility, negative-path and error-message test evidence. |
| SRE/Ops | R | Owns operational messages, logs, metrics, dashboards, support runbooks and incident mapping. |
| AI Governance | R | Ensures AI prompts, model outputs, agent actions and System Builder candidates use approved fields/messages. |
| Internal Audit | C/I | Reviews evidence completeness, lineage, exceptions, approvals, and control effectiveness. |

## 11.4 Acceptance Criteria

Physical registry schemas, tables, indexes, constraints, seed batches and lookup views are defined and Flyway-governed.

Data element, mapping, validation rule, enum value, message catalog, translation, approval, evidence and audit records are represented.

Admin workflow enforces maker-checker review, impact analysis, approval routing, lifecycle control, publication, cache refresh and monitoring.

CI/CD gates reject unregistered fields, type/length mismatch, enum drift, duplicate message codes, unsafe logs, missing mappings and evidence gaps.

Runtime consumers use approved registry snapshots or controlled lookup APIs; derivative caches and generated artifacts are not authoritative.

All production-bound catalog changes include source, owner, classification, validation evidence, seed batch, approval record, rollback/deprecation plan and evidence_ref.

## 11.5 Anti-Patterns and Rejection Rules
| Anti-Pattern | Required Response |
| --- | --- |
| Spreadsheet as authority | Reject. Spreadsheets may support review but are not runtime or publication authority unless controlled and synchronized to the registry. |
| UI/backend hardcoded meanings | Reject. User messages, validation semantics, status values and error codes must be catalog-backed or explicitly bootstrap-scoped. |
| Database-only meaning | Reject. Columns, enums and reference codes must map to canonical data elements and contracts. |
| Uncontrolled seed overwrite | Reject. Seed changes must be idempotent, versioned, approved and evidence-backed. |
| Debug messages in production | Reject unless time-bound, redacted, policy-approved, audited and auto-reverted. |
| AI-invented catalog values | Reject. AI-generated fields/messages remain candidates until human-approved and seeded. |

## 11.6 Open Reconciliation Items
| ID | Item |
| --- | --- |
| RI-078-001 | Propagate AIRA-DOC-077/078 references into API, database/Flyway, Dynamic Workspace, MicroFunction, CI/CD, evidence manifest, Policy-as-Code and System Builder documents during next release-train refresh. |
| RI-078-002 | Decide whether the physical registry belongs to aira_catalog or aira_reference bounded context in the canonical database register. |
| RI-078-003 | Define generated-artifact locations for TypeScript types, Java constants/value objects, OpenAPI fragments, OPA input schemas, localization bundles and test fixtures. |
| RI-078-004 | Add catalog validation jobs to the Architecture Fitness CI Rule Pack and Evidence Manifest schema. |
| RI-078-005 | Track known AIRA duplicate numbering and 41B/44 System Builder overlap through 00D/00E register controls. |

## 11.7 AVCI Compliance Summary
| AVCI Property | How AIRA-DOC-078 Satisfies It |
| --- | --- |
| Attributable | Every catalog record has owner, steward, source_ref, bounded_context, approver, seed_batch_id, change_request_id and evidence_ref. |
| Verifiable | Flyway migrations, seed checksums, schema compatibility tests, message-code uniqueness tests, policy gates, audit events and evidence manifests prove consistency. |
| Classifiable | Every data element, mapping, message, translation, evidence reference and runtime lookup carries classification and handling rules. |
| Improvable | Runtime drift, unknown-field events, support findings, localization gaps, incidents, deprecation usage and failed gates feed controlled improvement backlog and release-train updates. |

End of AIRA-DOC-078 v1.0 | Draft for Review | Registry-Backed Consistency | Evidence by Construction

