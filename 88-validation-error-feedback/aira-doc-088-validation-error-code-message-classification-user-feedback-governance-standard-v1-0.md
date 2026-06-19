---
title: "Validation Error Code Message Classification User Feedback Governance Standard"
doc_id: "AIRA-DOC-088"
version: "v1.0"
status: "final"
category: "Validation error feedback"
source_docx: "AIRA-DOC-088_Validation_Error_Code_Message_Classification_User_Feedback_Governance_Standard_v1.0.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 88-validation-error-feedback
  - final
  - aira-doc-088
---



# Validation Error Code Message Classification User Feedback Governance Standard



AIRA
AI-Native Enterprise Platform

Validation Error Code, Message, Classification, and User Feedback Governance Standard

Message Governance | Severity Classification | Safe User Feedback | Support Diagnostics | Evidence

AIRA-DOC-088 | Version v1.0 | INTERNAL CONFIDENTIAL
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-088 |
| Document Title | Validation Error Code, Message, Classification, and User Feedback Governance Standard |
| Version | v1.0 |
| Status | DRAFT FOR ARB, DATA GOVERNANCE, DEVSECOPS, SECURITY, OPERATIONS/SRE, QA/SDET, AI GOVERNANCE, PRODUCT OWNERS, AND INTERNAL AUDIT REVIEW |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Data Governance; Security Architecture; DevSecOps Lead; Software Development Lead; API Architecture; DBA; QA/SDET; Operations/SRE; AI Governance; Product Owners; Internal Audit |
| Primary Audience | Solutions Architects, Product Owners, Business SMEs, Frontend Developers, Backend Developers, API Architects, Workflow Designers, Data Engineers, DBAs, QA/SDET, DevSecOps, SRE, Security, AI Governance, Internal Audit |
| Generated | 2026-06-18 |

# Static Table of Contents

1. Document Control

2. Mandatory Practice Statement

3. Executive Summary

4. Purpose and Scope

5. Message Governance Principles

6. Severity and Visibility Model

7. Error Code and Message Code Registry

8. Validation Response Models

9. User Feedback Standard

10. Technical Diagnostic and Logging Rules

11. Localization and Accessibility

12. Operations, Sentry, Dashboard, and Evidence Rules

13. Security and Privacy Controls

14. Testing and CI Gates

15. RACI

16. Acceptance Criteria

17. Anti-Patterns

18. Open Reconciliation Items

19. AVCI Compliance Summary

# Document Control
| Field | Required Value |
| --- | --- |
| Document ID | AIRA-DOC-088 |
| Document Title | Validation Error Code, Message, Classification, and User Feedback Governance Standard |
| Version | v1.0 |
| Status | DRAFT FOR ARB, DATA GOVERNANCE, DEVSECOPS, SECURITY, OPERATIONS/SRE, QA/SDET, AI GOVERNANCE, PRODUCT OWNERS, AND INTERNAL AUDIT REVIEW |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Data Governance; Security Architecture; DevSecOps Lead; Software Development Lead; API Architecture; DBA; QA/SDET; Operations/SRE; AI Governance; Product Owners; Internal Audit |
| Target Audience | Solutions Architects, Product Owners, Business SMEs, Frontend Developers, Backend Developers, API Architects, Workflow Designers, Data Engineers, DBAs, QA/SDET, DevSecOps, SRE, Security, AI Governance, Internal Audit |
| Parent Standards | 01/01A/01B AVCI and Enterprise Architecture Standards; 02 Engineering Blueprint; 03 Developer Guide; 04 Technology Stack; 10 through 10E MicroFunction standards; 11 and 11A DevSecOps standards; 12A Dynamic Frontend Workspace governance; 15/15A API and Integration Contract standards; 16/16A/16B Database and Flyway standards; 17/17A Security and Access Control; 20 CI/CD Evidence Pack; 23B Architecture Fitness Function Catalog; 30/30A Change, Promotion, Reversibility, Compensation; 31/31A Production Operations and Observability; 42 AI Governance; 53 Dynamic Workspace Observability; 65 Policy-as-Code; 66 Evidence Manifest; 67 API/Event/Schema/DLQ/Replay Governance; 71 Data Governance and Classification; 77-81 Data, Variable, Message, and Governance family where adopted. |
| Companion Documents | AIRA-DOC-086, AIRA-DOC-087, AIRA-DOC-089; AIRA-DOC-015/015A API and Problem Details; AIRA-DOC-031/031A Observability; AIRA-DOC-053 Dynamic Workspace Observability; AIRA-DOC-071 Data Classification; message/variable governance family where adopted. |
| Review Cadence | Quarterly; unscheduled after validation bypass, critical/high data-quality defect, Sev-1/Sev-2 incident, security finding, audit finding, schema change, API/event contract change, workflow change, or AI governance change. |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Validation-Governance / AIRA-DOC-088 / v1.0/ |
| Approval Path | Draft -> Enterprise Architecture/Data/Security/DevSecOps/QA/SRE/AI Governance/Internal Audit review -> ARB/CAB approval when production-impacting -> Register update -> controlled publication. |
| Supersedence Rules | This document becomes canonical only after register adoption. Any supersedence, split, merge, or retirement must update 00A-00D registers, evidence paths, companion references, implementation impacts, and PR/MR templates. |

## Version History
| Version | Date | Owner | Summary |
| --- | --- | --- | --- |
| v1.0 | 2026-06-18 | Solutions Architecture Office / IT Head | Initial draft for AIRA validation governance, implementation, error/message control, and validation evidence templates. |

# Mandatory Practice Statement

Mandatory Practice Statement. AIRA validation messages, error codes, warning codes, user feedback, technical diagnostics, logs, traces, audit events, Sentry issues, dashboards, and evidence records must be consistent, classified, safe, localizable, testable, and traceable. A validation message is not acceptable when it is merely understandable to a developer; it must also be safe for the user, useful for operations, attributable to a rule owner, and verifiable through evidence.

# Executive Summary

Validation cannot be enterprise-grade if each layer invents its own messages. AIRA requires a standard validation message and error-code model so users receive consistent feedback, APIs return predictable machine-readable responses, operators receive safe diagnostics, and auditors can reconstruct rule ownership and evidence without exposing sensitive data.

This standard defines severity, visibility, message registry, code structure, user message requirements, technical diagnostic rules, localization, accessibility, telemetry, security handling, and CI/CD gates for validation errors and warnings.

# Purpose and Scope

This document governs all validation-related messages generated by frontend components, backend services, APIs, event consumers, workflow engines, MicroFunctions, database constraints, import/export jobs, batch runs, reports, analytics refreshes, AI prompt validation, policy decisions, and operational tooling.

# Cross-Document Alignment and Control Baseline

This document inherits the active AIRA governance baseline and must not be interpreted as weakening any parent standard. If a conflict appears, the stricter control applies until the issue is recorded and resolved as an AVCI reconciliation item through the canonical registers.
| Control Area | Required Alignment | Evidence |
| --- | --- | --- |
| Architecture | Validation preserves SOLID, Clean Architecture, DDD ownership, ports/adapters, MicroFunction isolation, and boundary discipline. | Architecture impact assessment, fitness-function results, PR/MR AVCI summary. |
| Contract-first | OpenAPI, AsyncAPI, JSON Schema, Avro, CloudEvents, DTOs, database columns, reports, analytics fields, and canonical field registry must stay aligned. | Contract lint, schema compatibility tests, canonical field registry diff. |
| Database/Flyway | Persistence validation and constraints are delivered through Flyway only; no manual production DDL or uncontrolled SQL path. | Flyway validate/migrate report, checksum, migration review, rollback or forward-fix plan. |
| Security and policy | Validation enforces classification, OPA/SBAC, least privilege, secrets hygiene, safe error responses, and no sensitive telemetry. | OPA decision record, log redaction test, security scan, access review. |
| Observability | Validation outcomes emit safe trace, metric, log, audit, Sentry, Loki/Tempo/Grafana, and evidence references. | Telemetry sample, dashboard link, evidence manifest. |
| DevSecOps | Validation gates are tested, repeatable, reproducible, negative-test proven, and blocked by CI/CD when critical controls fail. | CI/CD evidence pack, test reports, SAST/SCA/DAST, fitness results. |

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

# Message Governance Principles
| Principle | Required Treatment |
| --- | --- |
| One governed registry | All validation error/message codes are registered, owned, versioned, classified, and test-linked. |
| Safe by default | User messages and API responses must not expose internal rules, stack traces, SQL, policy logic, secrets, tokens, raw PII, or unrestricted payloads. |
| Consistent across layers | The same validation rule uses the same message_code/error_code across frontend, backend, API, events, batch, reports, and evidence where applicable. |
| Machine-readable and human-usable | Responses include structured code and safe text that both systems and humans can act on. |
| Localizable and accessible | Messages use localization keys and accessibility guidance; hardcoded UI strings are rejected. |
| Evidence-linked | Each message ties to validation_rule_id, field_code, severity, source layer, classification, and evidence_ref. |
| Improvable | Recurring messages feed data-quality, UX, training, rule tuning, or defect backlog. |

# Severity and Visibility Model
| Severity | Definition | Allowed Visibility |
| --- | --- | --- |
| Fatal | System cannot safely continue or protected validation dependency is unavailable. | User safe generic message; API safe code; logs/audit/Sentry/evidence with redacted diagnostic; immediate alert. |
| Error | Input fails blocking validation and action is rejected or quarantined. | User field/form message; API Problem Details; logs/audit/evidence; dashboard aggregation. |
| Warn | Input is accepted only with caution, pending review, defaulting, or non-blocking risk. | User warning where actionable; logs/metrics/evidence; approval path if required. |
| Info | Non-blocking validation information or confirmation. | User guidance, audit or metrics as needed; no sensitive diagnostic. |
| Debug | Developer/diagnostic detail for non-production or approved restricted troubleshooting. | Not shown to end users; log only under controlled, redacted, environment-specific policy. |
| Trace | Low-level diagnostic event used for trace reconstruction. | Not shown to users; traces only with safe fields and sampling controls. |

# Error Code and Message Code Registry
| Registry Field | Description |
| --- | --- |
| message_code | Stable user-facing and localization key reference, for example VAL-AUTH-LOGIN-001. |
| error_code | Machine-readable technical category or specific validation error, for API, logs, metrics, and support. |
| severity | Fatal, Error, Warn, Info, Debug, or Trace. |
| classification | Public, Internal, Confidential, Restricted plus handling rules. |
| source_layer | Frontend, API gateway, backend, domain, policy, workflow, adapter, database, batch, report, analytics, AI, or operations. |
| affected_field / field_code | Canonical field or field group affected by the message. |
| validation_rule_id | Rule that caused the message. |
| description | Control description for owners, developers, QA, SRE, and auditors. |
| safe_user_message | User-safe, action-oriented, localizable message without sensitive internals. |
| technical_diagnostic_message | Redacted diagnostic guidance for support and engineering. |
| remediation_guidance | Recommended correction, support path, or next step. |
| owner | Business/technical owner of the message and rule. |
| evidence_ref | Evidence path linking implementation, tests, and runtime examples. |
| localization_key | i18n key for UI and client rendering. |
| logging_eligibility | Whether and where the message may appear in logs, traces, audit, Sentry, and dashboards. |
| masking_redaction_rule | Fields or values that must be masked or excluded. |
| lifecycle_state | Draft, active, deprecated, superseded, retired, waiver-controlled. |

# Validation Response Models
| Channel | Required Response Behavior |
| --- | --- |
| Frontend field feedback | Show field-level message, summary banner where needed, focus management, ARIA attributes, and correction guidance. |
| Frontend form feedback | Show safe summary with message_code references where useful; preserve user-entered safe values; avoid exposing hidden policy internals. |
| REST API | Use approved Problem Details-compatible structure with status, error_code, message_code, correlation_id, field_errors, classification-safe details, and evidence_ref when allowed. |
| Event consumer | Reject, quarantine, DLQ, or acknowledge with safe error event according to contract; include schema version, event id, rule id, and reason code. |
| Batch/import | Produce reject file or exception list with safe field references, row/record identifier, message_code, error_code, and remediation path. |
| Report/analytics | Reject unsafe parameters or stale data with safe message; mark report as unavailable, partial, stale, or warning-reviewed as appropriate. |
| AI prompt/workflow | Deny or redact unsafe prompts using safe message; record guardrail result and route decision without exposing sensitive input. |

# User Feedback Standard

Messages must be plain-language, specific enough to correct, and safe enough for the user classification.

Messages must not blame the user or reveal internal implementation, policy logic, database names, stack traces, SQL, IDs that expose sensitive data, or raw rejected values.

For multiple field errors, show a summary and field-level links where supported.

For cross-field errors, identify the fields involved and the correction condition in safe terms.

For security-sensitive denials, provide minimal safe guidance and support path without disclosing detection logic.

For batch/import/report messages, provide action-oriented remediation, affected scope, and owner without exposing restricted records.

For AI guardrail messages, explain that the request cannot be processed under current data/classification policy and provide approved alternatives where allowed.

# Technical Diagnostic and Logging Rules
| Diagnostic Field | Rule |
| --- | --- |
| correlation_id / trace_id | Always include for support correlation. |
| validation_rule_id / field_code | Include to link support analysis to registry. |
| safe_summary | Use redacted, bounded, structured diagnostic text. |
| raw_value | Do not log raw value unless explicitly permitted by classification and redaction policy; default is no. |
| stack trace | Never expose to user; logs only under environment and severity policy with redaction. |
| policy details | Do not expose full OPA/Rego logic or sensitive rule thresholds to users. |
| evidence_ref | Include link/reference to evidence record when safe and authorized. |
| dashboard dimensions | Use bounded labels; do not use raw account numbers, names, raw payloads, or high-cardinality identifiers. |

# Localization and Accessibility
| Control | Requirement |
| --- | --- |
| Localization key | Every user-visible message must have localization_key and fallback language behavior. |
| Message parameters | Dynamic placeholders must be classification-safe and redacted when needed. |
| Screen reader support | Field errors and summary errors must be announced appropriately. |
| Focus management | On submit failure, focus moves to error summary or first invalid field according to UX standard. |
| Color and contrast | Validation state must not rely on color alone and must meet accessibility requirements. |
| Cognitive clarity | Messages must be concise, actionable, and avoid ambiguous technical jargon. |

# Operations, Sentry, Dashboard, and Evidence Rules

Validation messages should produce aggregate metrics by service, bounded_context, operation, field_code, validation_rule_id, error_code, severity, classification, and environment.

Critical/fatal validation dependency failures alert SRE and technical owner.

Repeated validation failures may create data-quality, UX, integration, training, or defect backlog items.

Sentry events must group by error_code and validation_rule_id, not raw payload.

Evidence packs must include representative validation events, test proof, message registry version, and dashboard links.

# Security and Privacy Controls

Never expose sensitive rejected values in UI/API response/logs/traces/Sentry/evidence.

Never echo passwords, tokens, secrets, private keys, raw prompts, raw documents, account numbers, or payment card data.

Apply classification-specific message detail limits.

Use generic denials for suspicious, abusive, rate-limited, injection, policy-bypass, or reconnaissance-like inputs.

Treat validation message catalogs as governed artifacts; malicious message changes can become social engineering or information disclosure risks.

# Testing and CI Gates
| Gate | Rejects |
| --- | --- |
| Registry completeness | User-visible validation message without message_code, localization_key, owner, severity, classification, or validation_rule_id. |
| Message consistency | Different layers using different codes/messages for the same rule without approved reason. |
| Sensitive leakage | Raw values, secrets, raw PII, payloads, stack traces, SQL, policy details, or tokens in user/API/log/Sentry messages. |
| Accessibility | Missing ARIA/error summary/focus management for frontend validation messages. |
| Problem Details schema | API validation response not conforming to approved response schema. |
| Localization | Hardcoded user-visible validation strings or missing fallback. |
| Evidence linkage | Message code not linked to tests, rule registry, and evidence_ref. |

# RACI and Operating Responsibilities
| Role | RACI | Responsibilities |
| --- | --- | --- |
| Business Owner | A/R | Defines business meaning, acceptable values, cross-field rules, regulatory meaning, approval thresholds, and exception disposition. |
| Product Owner | R/A | Ensures validation behavior, user feedback, acceptance criteria, and usability are represented in backlog and UAT. |
| Domain Owner | A/R | Owns domain invariants, business rule placement, bounded-context validation ownership, and non-duplication across contexts. |
| Frontend Developer | R | Implements user-experience validation, accessibility-compliant feedback, localization keys, and frontend tests aligned to canonical registry. |
| Backend Developer | R | Implements authoritative request, command, domain, policy, idempotency, and adapter validation behind ports/adapters. |
| API Architect | A/R | Owns OpenAPI, AsyncAPI, schema, Problem Details, compatibility, and contract validation rules. |
| DBA / Data Engineer | A/R | Owns Flyway constraints, reference data, RLS, data-quality checks, and schema drift detection. |
| QA/SDET | A/R | Owns negative, boundary, mutation, contract, event, database, E2E, accessibility, and regression evidence. |
| Security Architecture | A/C | Owns classification, redaction, injection defense, secrets controls, OPA/SBAC, and secure error handling. |
| DevSecOps | R/C | Owns CI/CD validation gates, evidence pack generation, SBOM/provenance, scans, and promotion controls. |
| SRE / Operations | R/C | Owns runtime evidence, dashboards, alerting, operational triage, and recurring validation failure review. |
| Data Governance | A/C | Owns canonical field definitions, data lineage, quality dimensions, retention, privacy, and semantic consistency. |
| AI Governance | A/C | Owns prompt intake validation, model-route eligibility, guardrails, output validation, and advisory-only boundaries. |
| Internal Audit | C/I | Reviews evidence completeness, control operation, sampling, traceability, and exception handling. |
| ARB / CAB | A | Approves production-impacting validation architecture, waivers, exceptions, and promotion gates. |

# Acceptance Criteria

All validation messages and error codes are registered, owned, classified, and versioned.

Severity levels are consistently applied and mapped to allowed visibility.

User messages are safe, localizable, accessible, and action-oriented.

Technical diagnostics are redacted, structured, correlation-ready, and supportable.

API, event, import, batch, report, dashboard, and AI guardrail responses use governed code/message models.

CI/CD blocks missing registry data, inconsistent messages, sensitive leakage, accessibility defects, and response schema drift.

# Explicitly Rejected Anti-Patterns

Frontend-only validation for business-critical, security-sensitive, financial, workflow, integration, or persistence rules.

Scattered hardcoded validation in controllers, UI components, SQL scripts, workflow scripts, or integration adapters without registry ownership.

Different field lengths, types, formats, nullability, enum values, messages, or classification across frontend, backend, API, events, database, reports, and analytics.

Saving unvalidated input to database, logs, audit, evidence, reports, analytics datasets, prompts, or external systems.

Logging or displaying passwords, tokens, secrets, raw PII, raw documents, raw prompts, account numbers, unrestricted payloads, or high-cardinality identifiers.

Direct model-provider calls for AI validation or AI-generated acceptance without approved LiteLLM/gateway, guardrails, policy, and human review.

Manual production DDL, unmanaged data corrections, or database constraints that are not versioned, tested, reviewed, and delivered through Flyway.

Validation bypasses for batch, file import, event replay, emergency runs, admin screens, reports, or AI-assisted workflows.

# Open Reconciliation Items
| ID | Issue | Severity | Owner | Required Evidence |
| --- | --- | --- | --- | --- |
| VAL-088-01 | Register AIRA-DOC-086 through AIRA-DOC-089 in canonical registers 00A-00D and assign source-pack placement. | High | Solutions Architecture Office / Knowledge Governance | Updated register, source-pack manifest, cross-reference map. |
| VAL-088-02 | Confirm relationship with the existing variables/messages/data governance family and avoid duplicate authority. | High | Data Governance / Enterprise Architecture | 00D reconciliation item and governing-source decision. |
| VAL-088-03 | Define physical schema names for canonical field registry, validation rule registry, and message code registry. | High | DBA / Data Governance / DevSecOps | Flyway migration proposal, dry-run, checksum, rollback/forward-fix plan. |
| VAL-088-04 | Confirm validation library/tooling choices for frontend, backend, contract, event, database, and AI prompt validation. | Medium | Software Development Lead / API Architect / Security | Tool decision record, ADR/TDL where required, CI validation evidence. |

# AVCI Compliance Summary
| AVCI Property | Validation Governance Evidence |
| --- | --- |
| Attributable | Validation rules, field definitions, message codes, owners, approvers, source contracts, schema references, and implementation owners are explicit. |
| Verifiable | Validation tests, contract tests, schema checks, database constraints, policy decisions, telemetry, evidence packs, and acceptance records prove behavior. |
| Classifiable | Inputs, outputs, prompts, files, errors, messages, logs, traces, reports, analytics fields, and evidence records carry classification and handling rules. |
| Improvable | Validation failures, false positives, false negatives, usability feedback, audit findings, security findings, and recurring data-quality defects feed a controlled backlog. |

