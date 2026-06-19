---
title: "Canonical Data Element Variable Message and Error Code Governance Standard"
doc_id: "AIRA-77"
version: "v1.0"
status: "final"
category: "Canonical data and message governance"
source_docx: "AIRA_77_Canonical_Data_Element_Variable_Message_and_Error_Code_Governance_Standard_v1.0.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 77-canonical-data-message-governance
  - final
  - aira-77
---



# Canonical Data Element Variable Message and Error Code Governance Standard



AIRA
AI-Native Enterprise Platform

Canonical Data Element, Variable, Message, and Error Code Governance Standard

AIRA-DOC-077 | Version v1.0

Canonical Data Dictionary | Variable Governance | Field Mapping | Message Catalog | Error Codes | Consistency Gates | Evidence by Construction | AVCI Always

# Document Control
| Document ID | AIRA-DOC-077 |
| --- | --- |
| Document Title | AIRA Canonical Data Element, Variable, Message, and Error Code Governance Standard |
| Version | v1.0 |
| Status | Draft for Architecture Review Board, Data Governance, Security, DevSecOps, QA/SDET, Operations, AI Governance, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Data Governance; API/Integration Architecture; Software Development; Frontend Development; Backend Development; DBA; DevSecOps; Security Architecture; QA/SDET; SRE/Operations; AI Governance; Internal Audit |
| Primary Audience | Developers, Architects, Data Stewards, API Designers, DBAs, QA/SDET, DevSecOps, SRE, Security, Product Owners, System Builder operators, AI agent owners, Internal Audit |
| Primary Parents | 01A Enterprise Architecture; 01 AVCI; 01B Evidence; 02 Engineering Blueprint; 11/11A DevSecOps; 20 CI/CD Evidence Pack; 65 Policy-as-Code; 66 Evidence Manifest; 67 API/Event/DLQ/Replay; 68 Control Traceability; 71 Data Governance; 76 Architecture Fitness Gates |
| Companion Standards | 10-10E MicroFunction; 12A/53-61 Dynamic Workspace; 15/15A API; 16/16A/16B Database/Flyway; 17/17A Security; 31/31A Observability; 42 AI Governance; 70 AI Evaluation; 72 Golden Paths; 73 System Builder; 74/75 Dynamic Workspace Certification |
| Review Cadence | Quarterly; unscheduled after material API, database, frontend, message catalog, evidence schema, policy, AI, integration, observability, or production-support change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Canonical-Data-Message-Governance / 077 / v1.0 / |

Static Table of Contents
1. Executive Summary
2. Mandatory Practice Statement
3. Purpose, Scope, and Authority
4. Governance Principles
5. Canonical Data Element Governance
6. Cross-Layer Consistency Rules
7. Data Type, Length, and Attribute Standard
8. Canonical Message and Error Code Governance
9. Severity, Classification, and Code Format
10. Standard Error Response and Message Usage Rules
11. Database, API/Event, Observability, and Evidence Bindings
12. Testing, CI/CD, and Policy-as-Code Gates
13. System Builder and AI Assistant Rules
14. Templates and Machine-Readable Records
15. RACI, Acceptance Criteria, Anti-Patterns, Reconciliation, and AVCI Summary

# 1. Executive Summary

This standard closes a critical enterprise gap in AIRA: the need for a single governed definition of every data element, variable, field, parameter, attribute, message, error code, warning, policy-denial reason, log event, audit event, API response, event payload, evidence field, and AI prompt variable used across the platform.

In an enterprise-grade application, a field is not merely a UI variable, Java property, JSON attribute, or database column. It is a governed data element with business meaning, technical definition, owner, steward, classification, type, length, validation, retention, mappings, lifecycle, and evidence. Likewise, a message or error is not merely text. It is a governed operational and user-support artifact with a code, severity, cause, solution, remediation path, classification, observability mapping, and evidence reference.

The target outcome is consistent, code-generatable, testable, supportable, and audit-ready behavior across frontend, backend, MicroFunctions, APIs, events, database, policy, observability, evidence packs, integrations, System Builder, and AI agents. This standard converts variable and message consistency into enforceable AIRA controls.

Figure 1. Canonical data element and message governance control plane. The canonical dictionary and message catalog are the source of governed definitions; generated schemas, UI components, database objects, logs, audit, evidence, and AI artifacts are controlled projections.

# 2. Mandatory Practice Statement

No AIRA field, variable, parameter, attribute, database column, API property, event field, configuration value, message, error code, warning, log event, audit event, policy-denial reason, or AI prompt variable may be introduced, modified, reused, deprecated, or removed unless it is registered, classified, versioned, validated, traceable to source authority, and aligned across frontend, backend, integration, database, policy, observability, evidence, and test layers.

# 3. Purpose, Scope, and Authority

The purpose of AIRA-DOC-077 is to define the canonical governance model for data elements and messages so AIRA can prevent drift among UI forms, APIs, backend DTOs, domain objects, database columns, OPA/Rego inputs, Kafka events, audit records, logs, evidence manifests, and AI-generated artifacts.
| Area | In Scope | Out of Scope |
| --- | --- | --- |
| Data Elements | Fields, variables, parameters, attributes, identifiers, statuses, enums, dates, amounts, classification labels, trace/evidence IDs, policy inputs. | Unreviewed local-only variables or undocumented mappings used as production authority. |
| Messages and Errors | UI messages, validation messages, API errors, policy denials, event failures, DLQ/replay messages, logs, audit events, support messages, AI guardrail messages. | Hardcoded text, raw exception leakage, unmanaged developer-only errors, vague support messages. |
| Authority | This document is subordinate to AIRA architecture, AVCI, DevSecOps, data governance, API, database, security, observability, and change standards, and governs consistency across them. | Bypassing source-register, PR/MR, CI/CD, DBA, data governance, security, or maker-checker controls. |

# 4. Governance Principles
| Principle | Mandatory Meaning |
| --- | --- |
| CDE-01 Canonical before implementation | A field or message must be defined before it is projected into UI, API, backend, event, database, policy, evidence, or tests. |
| CDE-02 One meaning, many projections | One canonical data element may have layer-specific names, but the meaning, type, length, validation, classification, and lifecycle must remain traceable. |
| CDE-03 Evidence by construction | Schema, mapping, validation, message-code, log-redaction, uniqueness, and compatibility checks must produce CI/CD evidence. |
| CDE-04 Classification first | Fields and messages must carry data classification and handling rules before they are logged, displayed, stored, indexed, retrieved, or passed to AI. |
| CDE-05 Fail closed on drift | Inconsistent types, lengths, enums, policy inputs, messages, or unregistered fields block protected promotion until reconciled or waived. |
| CDE-06 AI is not authority | AI assistants and System Builder may draft candidate fields and messages only; human stewards approve canonical adoption. |

# 5. Canonical Data Element Governance

A canonical data element is the authoritative AIRA definition of a business, technical, security, audit, evidence, runtime, policy, or AI-context field. It defines what the element means, who owns it, where it appears, how it is validated, and how it is changed.
| Record Area | Required Fields |
| --- | --- |
| Identity | data_element_id, canonical_name, display_name, version, lifecycle_state, source_of_truth |
| Business ownership | business_definition, technical_definition, owning_bounded_context, owner, steward, approving_role |
| Classification | classification, security_sensitivity, privacy_sensitivity, retention_rule, masking/redaction_rule, encryption_requirement |
| Technical attributes | data_type, length, precision, scale, format, pattern, allowed_values, default_value, nullability, uniqueness, required_rule |
| Validation and normalization | validation_rules, normalization_rules, compatibility_rule, deprecation_rule, migration_rule |
| Layer mappings | frontend_mapping, backend_mapping, api_mapping, event_mapping, database_mapping, policy_mapping, observability_mapping, evidence_mapping, test_fixture_mapping |
| Evidence | evidence_ref, last_validation_result, CI_gate_ref, PR/MR_ref, waiver_ref if applicable |

# 6. Cross-Layer Consistency Rules

AIRA shall treat field drift as an architecture and evidence defect. The same field must not silently change meaning, length, precision, enum values, timezone semantics, nullability, classification, masking rule, or validation rule as it moves from UI to API, backend, event, database, policy, observability, and evidence layers.

Figure 2. Cross-layer consistency gate stack. Candidate fields and messages move from intake to dictionary, contract, implementation, CI/CD evidence, and runtime assurance gates.
| Rule Area | Required Treatment |
| --- | --- |
| Naming | Use canonical_name for governance; allow layer-specific casing such as camelCase for JSON/TypeScript, PascalCase for classes, snake_case for database where mapped. |
| Identifiers | IDs must declare format, authority, mutability, uniqueness, collision rule, display eligibility, and privacy handling. |
| Dates and time | Use explicit timezone treatment. Production event and audit timestamps should use UTC or explicit offset. UI display may localize without changing stored meaning. |
| Amounts and decimals | Monetary, percentage, interest, score, and measurement fields must define precision, scale, rounding, currency/unit, and comparison behavior. |
| Enums and statuses | Enum values require owner, meaning, lifecycle, compatibility, localization label, allowed transitions, and backward compatibility assessment. |
| Correlation and evidence | trace_id, span_id, request_id, correlation_id, causation_id, idempotency_key, evidence_ref, policy_decision_id, and message_code must follow registered patterns. |
| Classification labels | Classification is required for fields, messages, logs, screenshots, prompts, evidence, and AI-context eligibility. |
| Generated code | Generated DTOs, clients, validators, forms, schema classes, migration stubs, and test fixtures must be produced from or validated against registered definitions. |

# 7. Data Type, Length, and Attribute Standard
| Concept | Frontend | Backend | API/Event | Database | Governance Rule |
| --- | --- | --- | --- | --- | --- |
| Short text / code | TypeScript string | Java String / value object | OpenAPI string maxLength | PostgreSQL varchar(n) | Must define max length, pattern, casing, trim rule, allowed values if code. |
| Long text | string with limit | String / Text value object | string maxLength | text with constraint where needed | Never use unbounded user input in logs/prompts; define redaction and retention. |
| Integer | number integer | Integer / Long | integer / int64 | integer / bigint | Define range, sign, unit, overflow behavior, and UI control. |
| Decimal / amount | number/string by precision | BigDecimal | number with multipleOf or string for exactness | numeric(p,s) | Define precision, scale, rounding, currency/unit, and comparison rules. |
| Boolean flag | boolean | Boolean | boolean | boolean | Name as affirmative condition; define default, nullability, and tri-state prohibition unless explicit. |
| Date | string date | LocalDate | format: date | date | Define timezone independence and business calendar rules. |
| Timestamp | string date-time | Instant / OffsetDateTime | format: date-time | timestamptz | Prefer UTC/offset; must support trace and audit reconstruction. |
| UUID / ID | string uuid | UUID / typed ID | format: uuid | uuid | Define authority, exposure rule, and correlation eligibility. |
| Enum / status | string enum | Enum or value object | enum | reference table or controlled enum | Reference-table preferred for governed lifecycle; DB enum requires migration compatibility review. |
| JSON/JSONB | object | JsonNode/value object | schema-defined object | jsonb | Must have schema, owner, classification, index policy, and compatibility plan. |

# 8. Canonical Message and Error Code Governance

AIRA messages and errors are governed operational records. The same condition must not produce different wording, inconsistent codes, conflicting severities, unsafe logs, or unhelpful support instructions across UI, API, backend, event processing, policy, audit, observability, and AI assistant outputs.
| Message Record Area | Required Fields |
| --- | --- |
| Identity | message_code, message_key, version, lifecycle_state, owning_bounded_context, owner, source_layer |
| Meaning | severity, category, subcategory, audience, description, cause, business_impact, security_impact |
| Message text | user_message, technical_message, localization_key, safe_display_rule, masking/redaction_rule |
| Resolution | recommended_solution, remediation_steps, support_action, developer_action, operator_action, security_action |
| Runtime behavior | retryable, idempotency_impact, rollback_or_compensation_impact, HTTP_status_mapping, API_error_mapping, event_DQL_mapping, audit_requirement |
| Evidence | trace_required, observability_fields, evidence_ref, policy_decision_ref, test_case_ref, documentation_ref |

Figure 3. Message and error code lifecycle. Messages are proposed, classified, validated, approved, published, monitored, and improved through evidence-producing governance.

# 9. Severity, Classification, and Code Format
| Severity | Definition | Examples |
| --- | --- | --- |
| Fatal | Unrecoverable or system-critical failure requiring immediate protection, containment, rollback, incident handling, or service halt. | Production-impacting data corruption risk, policy engine unavailable for protected action, payment/identity/security control failure. |
| Error | Failed operation requiring correction, retry, compensation, support intervention, or user action. | Validation failure, integration timeout after retries, idempotency conflict, DLQ failure requiring repair. |
| Warn | Abnormal or risky condition that does not stop processing but requires monitoring, follow-up, or policy attention. | Near-limit quota, deprecated field use, fallback route, recoverable schema compatibility warning. |
| Info | Normal operational, business, audit, lifecycle, or support information useful for traceability. | Record created, message published, workspace resolved, policy allowed, evidence pack completed. |
| Debug | Diagnostic detail allowed only under controlled runtime toggle, non-production, or time-bound production diagnostic policy. | Internal state summary, validator branch, non-sensitive payload shape. |
| Trace | Fine-grained execution detail allowed only when safe, redacted, policy-approved, and performance-aware. | Step-level timing, span correlation, retry attempt sequence, safe execution branch. |

Severity is not the same as data classification. A TRACE event can still contain Restricted information if not controlled, and an INFO audit message can be Evidence-Sensitive. Classification levels include Public, Internal, Confidential, Restricted, Evidence-Sensitive, and Security-Sensitive.

## 9.1 Message Code Format

AIRA message codes shall use the pattern: AIRA-{DOMAIN}-{LAYER}-{SEVERITY}-{NNNN}. Example codes: AIRA-AUTH-API-ERROR-0001, AIRA-AUTH-POLICY-WARN-0002, AIRA-MF-RUNTIME-FATAL-0001, AIRA-DW-UX-INFO-0001, AIRA-EVT-DLQ-ERROR-0001, AIRA-AI-GRD-WARN-0001.
| Segment | Meaning |
| --- | --- |
| DOMAIN | AUTH, MF, DW, EVT, DB, API, AI, SEC, OBS, CICD, SYSBLD, DATA, EVID |
| LAYER | UX, API, SVC, POLICY, DB, EVT, DLQ, RUNTIME, GRD, CICD, OBS, INT |
| SEVERITY | FATAL, ERROR, WARN, INFO, DEBUG, TRACE |
| NNNN | Zero-padded sequence unique within domain/layer/severity and lifecycle-controlled |
| Lifecycle | Draft -> Review -> Active -> Deprecated -> Retired; never reuse retired codes |

# 10. Standard Error Response and Message Usage Rules

API, integration, backend, and AI-assisted responses must expose safe, consistent, supportable error objects. Raw stack traces, internal exception names, tokens, secrets, raw PII, raw prompts, and unrestricted payloads must not be displayed or logged.

{
  "code": "AIRA-AUTH-API-ERROR-0001",
  "message": "Login session could not be established.",
  "user_message": "We could not complete sign-in. Please try again or contact support with the reference code.",
  "technical_message": "AUTH_LOGIN_CONTEXT_ESTABLISH failed at policy validation.",
  "severity": "ERROR",
  "category": "AUTHENTICATION",
  "correlation_id": "...",
  "trace_id": "...",
  "evidence_ref": "...",
  "timestamp": "2026-06-18T10:15:00Z",
  "retryable": false,
  "remediation_hint": "Verify OPA policy availability and session context inputs.",
  "documentation_ref": "AIRA-DOC-077/message-catalog/AUTH",
  "policy_decision_ref": "...",
  "validation_errors": []
}

## 10.1 UI and Dynamic Workspace Message Rules
| Rule | Required Treatment |
| --- | --- |
| Source from catalog | UI labels, validation text, policy-denial messages, support prompts, and AI Assistant messages must reference message_key or message_code. |
| User-safe wording | User-facing messages must be understandable, actionable, localized-ready, accessible, and free of sensitive technical detail. |
| Technical visibility | Technical_message may be visible only to authorized support, DevSecOps, SRE, Security, or audit roles based on policy. |
| Correlation display | Display a safe reference code or correlation ID when it helps support; never display trace payloads, tokens, stack traces, or policy internals. |
| Accessibility | Validation messages must be keyboard-accessible, screen-reader-compatible, focus-managed, and consistent across forms and widgets. |

## 10.2 Backend, MicroFunction, and Policy Message Rules

Backend services, MicroFunctions, policy decisions, and runtime envelopes must map exceptions, validation failures, policy denials, idempotency conflicts, outbox failures, DLQ events, replay outcomes, compensation events, rollback actions, and System Builder rejections to registered canonical message codes.

# 11. Database, API/Event, Observability, and Evidence Bindings
| Binding Area | Mandatory Rule |
| --- | --- |
| Database / Flyway | No unregistered database column, enum, reference value, validation constraint, view field, or seed value may be promoted. All schema changes must update canonical data element records, contracts, tests, evidence manifest, and Flyway migration evidence. |
| OpenAPI / AsyncAPI | Schemas must use registered data elements, message codes, error response model, classification labels, trace/correlation fields, and compatibility rules. Breaking changes require consumer impact analysis and approval. |
| Kafka / CloudEvents / DLQ / Replay | Events must use registered payload fields, headers, CloudEvents metadata, idempotency keys, message codes, replay status codes, and DLQ reason codes. |
| OPA / SBAC | Policy inputs must reference canonical fields. Policy-denial reasons must use registered message codes and safe explanation rules. |
| Logs / Traces / Metrics / Audit | message_code, severity, classification, trace_id, correlation_id, evidence_ref, actor hash, policy_decision_id, and safe status fields must be present where applicable. |
| Evidence Manifest | Evidence packs must include data/message catalog validation results, drift checks, log redaction tests, schema compatibility results, and message-code uniqueness evidence. |

## 11.1 Forbidden Telemetry Fields

Never log, trace, metric-label, audit-message, prompt, embed, screenshot, or evidence-index the following unless an explicitly approved secure evidence handling path exists: passwords, tokens, raw JWTs, secrets, raw PII, account numbers, raw documents, raw prompts containing Confidential or Restricted data, embeddings, private keys, payment data, and uncontrolled customer payloads.

# 12. Testing, CI/CD, and Policy-as-Code Gates
| Gate | Pass Condition |
| --- | --- |
| Dictionary completeness | Every changed frontend/API/event/database/policy/evidence field maps to an active canonical data element. |
| Field consistency | Type, length, precision, scale, nullability, format, enum, default, classification, and validation are consistent or explicitly mapped. |
| Message catalog | All message_code values are unique, registered, active, classified, and mapped to source layer, severity, cause, and solution. |
| Hardcoded message detection | UI/backend messages must reference catalog keys except approved internal-only test messages. |
| Schema compatibility | OpenAPI, AsyncAPI, Avro/JSON Schema, CloudEvents, and generated clients are compatible with canonical definitions. |
| Flyway validation | Database columns, constraints, enums, reference tables, and seed data are registered and migrated only through Flyway or approved controlled seeding. |
| Policy input validation | OPA/Rego tests validate expected fields, classifications, policy-denial codes, and fail-closed behavior. |
| Log redaction | Logs, traces, errors, Sentry, Loki, Tempo, dashboards, screenshots, prompts, and evidence records are checked for forbidden fields. |
| Evidence manifest | PR/MR evidence includes data/message drift report, changed catalog records, approvals, tests, waivers, and improvement backlog. |

## 12.1 Policy-as-Code Enforcement Examples

Reject conditions include: unregistered field; inconsistent field length; enum drift; unregistered error code; hardcoded UI message; log containing forbidden field; API schema without classification; database column without canonical mapping; message without remediation guidance; AI-generated field without approval.

# 13. System Builder and AI Assistant Rules
| Rule | Required Treatment |
| --- | --- |
| Candidate only | System Builder, ChatGPT, Codex, Claude, Hermes, and agents may draft new fields/messages only as candidates until human steward approval. |
| No invented authority | AI must not invent production field definitions, enum values, error codes, validation rules, database columns, or policy inputs without canonical registration. |
| Catalog-aware generation | Generated code, forms, DTOs, contracts, migrations, tests, prompts, policies, and evidence manifests must reference registered data elements and message codes. |
| Approval evidence | New candidates require owner, steward, classification, type, length, validation, mappings, message cause/solution, tests, evidence_ref, and PR/MR review. |
| Fail closed | If catalog, dictionary, policy, evidence store, or validation is unavailable, production-bound generation and promotion must fail closed. |

# 14. Templates and Machine-Readable Records

## 14.1 Canonical Data Element Record Template

data_element_id: CDE-AUTH-SESSION-CONTEXT-ID-0001
canonical_name: session_context_id
display_name: Session Context ID
business_definition: Unique reference to the governed login/session context.
owning_bounded_context: identity-and-access
classification: Confidential
data_type: UUID
length_precision_scale: uuid
format_pattern: RFC 4122 UUID
nullable: false
unique: true
source_of_truth: PostgreSQL aira_auth.session_context
frontend_mapping: sessionContextId
backend_mapping: SessionContextId value object
api_mapping: sessionContextId
policy_mapping: input.session_context_id
observability_mapping: session_context_id_hash only
evidence_mapping: evidence_ref/session_context_id_hash
version: 1.0.0
lifecycle_state: Active
evidence_ref: EVD-CDE-AUTH-0001

## 14.2 Message/Error Code Record Template

message_code: AIRA-AUTH-POLICY-ERROR-0001
message_key: auth.policy.denied
severity: ERROR
category: AUTHORIZATION
source_layer: POLICY
user_message: You are not authorized to perform this action.
technical_message: OPA/SBAC policy denied the requested capability.
description: Protected action denied because required skill, scope, or classification allowance was missing.
cause: Missing SBAC skill or policy condition not satisfied.
recommended_solution: Request proper access through approved workflow or use a permitted capability.
support_action: Verify actor, tenant, role, skill, policy version, and correlation ID.
retryable: false
http_status_mapping: 403
audit_requirement: Required
classification: Internal
evidence_ref: EVD-MSG-AUTH-0001
lifecycle_state: Active

## 14.3 PR/MR Data and Message Governance Checklist

• All changed fields are registered or submitted as candidates.

• Frontend, backend, API/event, database, policy, evidence, observability, and tests agree on type/length/validation or have approved mappings.

• All user-facing and technical messages use registered message codes and localization keys.

• No raw exception or sensitive value is exposed in UI/logs/traces/prompts/evidence.

• Flyway migrations and reference seed data match canonical records.

• OPA/SBAC policy input fields are registered and tested.

• Evidence manifest contains dictionary, schema, message, redaction, and mapping validation reports.

# 15. RACI, Acceptance Criteria, Anti-Patterns, Reconciliation, and AVCI Summary

## 15.1 RACI Summary
| Role | Responsibility |
| --- | --- |
| Solutions Architecture Office / IT Head | Accountable for standard authority, conflict escalation, material exception approval, and release-train alignment. |
| Enterprise Architecture | Owns cross-layer consistency, bounded-context mapping, architecture fitness rules, and source precedence. |
| Data Governance | Owns canonical data dictionary, classification, retention, stewardship, reference data, and data-quality controls. |
| API / Integration Architecture | Owns OpenAPI, AsyncAPI, CloudEvents, Avro/JSON Schema, external mappings, DLQ/replay field and message rules. |
| Software / Frontend / Backend Development | Implements registered fields, messages, validators, error handling, and catalog-based generated code. |
| DBA | Owns Flyway migration validation, column mapping, constraints, indexes, reference data, and seed governance. |
| Security Architecture | Owns sensitive-field handling, secrets hygiene, policy-denial messages, redaction, abuse cases, and secure error behavior. |
| DevSecOps / QA/SDET | Owns CI/CD gates, tests, schema validators, evidence generation, uniqueness checks, and release-blocking behavior. |
| SRE / Operations | Owns runtime observability, support messages, incident mappings, alert codes, dashboards, and trace reconstruction. |
| AI Governance | Owns AI prompt variable, model-route, guardrail, RAG, tool-action, and agent-output field/message controls. |
| Internal Audit | Reviews evidence completeness, change traceability, exceptions, and control effectiveness. |

## 15.2 Acceptance Criteria

• The standard defines enforceable rules for consistent variables, fields, types, lengths, attributes, validation, messages, severity, descriptions, solutions, observability, evidence, and lifecycle governance.

• The data dictionary and message catalog can be represented as machine-readable records and validated in CI/CD.

• New or changed fields/messages require owner, steward, classification, mappings, tests, and evidence.

• API/event/database/policy/frontend/backend/evidence layers can be checked for drift.

• Message/error codes include cause, description, recommended solution, support/developer/operator/security action, retryability, rollback/compensation impact, and evidence reference.

• AIRA System Builder and AI assistants are constrained to candidate-generation unless human-approved.

## 15.3 Anti-Patterns and Rejection Rules

• Inconsistent type or length between UI, API, backend, event, policy, and database.

• Hardcoded messages scattered across frontend/backend instead of a governed catalog.

• Unregistered or duplicated error codes.

• Vague messages without cause, solution, remediation, support action, or evidence reference.

• Raw technical exceptions, stack traces, tokens, secrets, PII, raw prompts, or sensitive payloads exposed to users/logs/evidence.

• Database enum drift, unversioned schema changes, or reference data outside Flyway/controlled seeding.

• Policy inputs not aligned with contracts and canonical data definitions.

• AI-invented fields, messages, enum values, validation rules, or database columns without approval.

## 15.4 Open Reconciliation Items
| ID | Issue | Severity | Owner |
| --- | --- | --- | --- |
| RI-077-001 | Propagate this standard into API, database/Flyway, Dynamic Workspace, MicroFunction, CI/CD, observability, AI governance, and evidence manifest documents. | High | Solutions Architecture Office |
| RI-077-002 | Create or extend physical canonical data dictionary and message catalog tables with Flyway-governed schema and seed data. | High | Data Governance / DBA |
| RI-077-003 | Add CI/CD validators for field drift, message-code uniqueness, forbidden telemetry fields, and hardcoded messages. | High | DevSecOps / QA/SDET |
| RI-077-004 | Register source-authority and supersedence placement in 00E release-train register. | Medium | Architecture Governance |
| RI-077-005 | Resolve known duplicate numbering and 41B/44 System Builder overlap without silently renumbering historical sources. | Medium | Architecture Board |

## 15.5 AVCI Compliance Summary
| AVCI Property | How AIRA-DOC-077 Satisfies It |
| --- | --- |
| Attributable | Owners, stewards, source mappings, PR/MR records, catalog records, code/message owners, and approval paths are explicit. |
| Verifiable | Contracts, schemas, database constraints, validators, policy checks, tests, CI/CD gates, log redaction reports, and evidence records prove consistency. |
| Classifiable | Data elements, messages, logs, traces, prompts, screenshots, evidence, AI-context fields, and support outputs carry classification and handling rules. |
| Improvable | Changes, deprecations, incidents, support findings, telemetry, failed gates, message confusion, and defects feed backlog, catalog updates, tests, and standards improvement. |

Data Consistency by Design - Message Discipline by Design - Evidence by Construction - AVCI Always

