---
title: "Login PoC1 MicroFunction Runtime Configuration Database Schema Standard"
doc_id: "AIRA-24"
version: "v1.2"
status: "revised"
category: "Login runtime and operations"
source_docx: "AIRA_24_Login_PoC1_MicroFunction_Runtime_Configuration_Database_Schema_Standard_v1.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 24-login-runtime-operations
  - revised
  - aira-24
---



# Login PoC1 MicroFunction Runtime Configuration Database Schema Standard



AIRA

AI-Native Enterprise Platform

Login PoC 1 MicroFunction Runtime Configuration and Database Schema Standard

AIRA-DOC-024 | v1.2 Revised

Flyway-Governed Configuration | Canonical Schemas | MicroFunction Runtime Assembly | Outbox and Evidence | AVCI Always
| Document ID | AIRA-DOC-024 |
| --- | --- |
| Canonical Filename | AIRA_24_Login_PoC1_MicroFunction_Runtime_Configuration_Database_Schema_Standard_v1.2_Revised.docx |
| Version | v1.2 Revised |
| Supersedes | 24-AIRA_Login_PoC1_MicroFunction_Runtime_Configuration_Database_Schema_Standard_v1.1_Aligned.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Architecture, Security, DBA, DevSecOps, QA/SDET, Platform, and Team Execution Review |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Security Architecture; Software Development Lead; DBA; DevSecOps Lead; QA/SDET; Platform Engineering; SRE / Operations; Internal Audit |
| Primary Audience | Developers; DBAs; MicroFunction runtime implementers; System Builder operators; QA/SDET; DevSecOps; Security; reviewers; approved AI coding agents |
| Source Reviewed | 24-AIRA_Login_PoC1_MicroFunction_Runtime_Configuration_Database_Schema_Standard_v1.1_Aligned.docx |
| Primary Companions | 22B Login MicroFunction Design Pattern; 23C PoC 1 Generation Prompt; 41 PoC 1 Execution Instruction; 43C/43D/43 PoC 1A controls; 42C Roadmap; 45 PoC2 DevSecOps/System Factory; 48/49/51 Dynamic Workspace data/API/security standards |
| Effective Date | Upon approval by Solutions Architecture Office / ARB / CAB where required |
| Mandatory Practice Statement The Login PoC 1 runtime configuration and database schema are authoritative engineering controls, not optional seed data. AUTH_LOGIN_CONTEXT_ESTABLISH must be represented through Flyway-governed PostgreSQL schemas, versioned MicroFunction runtime configuration, canonical step bindings, OPA/SBAC policy references, audit/outbox/evidence records, Dynamic Workspace bootstrap configuration, and fail-closed activation controls. Redis/Valkey, dashboards, generated clients, LLM summaries, and AI-generated narratives are derivative only and must never become authority. |
| --- |

Table of Contents

This document uses Microsoft Word heading styles. Insert or update an automatic Word Table of Contents before controlled publication.
| Section | Title |
| --- | --- |
| 1 | Executive Summary and v1.2 Alignment Verdict |
| 2 | Purpose, Scope, and Authority |
| 3 | Source Alignment and Gap Analysis |
| 4 | Canonical Database and Flyway Target |
| 5 | Authoritative Runtime Configuration Model |
| 6 | Canonical AUTH_LOGIN_CONTEXT_ESTABLISH Step Sequence |
| 7 | Security, Policy, Audit, Outbox, and Evidence Model |
| 8 | Dynamic Workspace Bootstrap and API/Event Alignment |
| 9 | DevSecOps, Testing, GitNexus, and Evidence Gates |
| 10 | Observability, Runtime Telemetry, Resilience, and Improvement Loop |
| 11 | Acceptance Criteria, RACI, Review Queue, and AVCI Summary |

# 1. Executive Summary and v1.2 Alignment Verdict

This v1.2 revision updates the Login PoC 1 MicroFunction Runtime Configuration and Database Schema Standard so it becomes the authoritative runtime and data-control companion to the revised PoC 1 generation prompt and execution instruction. It preserves the original purpose of Document 24: define the Login PoC 1 MicroFunction runtime configuration schema, catalog tables, control data, evidence fields, and database-governed activation rules.

The key governing interpretation is that AIRA is not building a custom login system. Login is a governed assembly of identity, session, policy, audit, event, observability, and safe response controls using Keycloak/OIDC, OPA/SBAC, MicroFunction runtime assembly, PostgreSQL/Flyway, and reviewed Dynamic Workspace bootstrap configuration.
| Area | v1.2 Verdict | Required Treatment |
| --- | --- | --- |
| Runtime authority | Retain and strengthen | PostgreSQL/Flyway and Git-managed configuration remain authoritative. Redis/Valkey, dashboards, generated clients, and AI summaries remain derivative. |
| Schema naming | Correct and enforce | Use aira_mf, aira_cfg, aira_auth, aira_policy, aira_audit, aira_outbox, and aira_ui. Do not generate aira_config or aira_workspace. |
| Step sequence | Canonical | AUTH_LOGIN_CONTEXT_ESTABLISH must use the canonical 20-step sequence. Simplified step lists are non-conforming. |
| PoC 1A boundary | Strict | Risk review, failure triage, step-up, lock/unlock, and AI incident analysis are PoC 1A additions and must not be embedded into PoC 1. |
| DevSecOps and evidence | Strengthened | Require CI/CD gates, GitNexus impact evidence, SAST/SCA/secret scan, authenticated DAST where applicable, Flyway validation, OPA tests, architecture fitness, and AVCI evidence pack. |
| Observability and resilience | Strengthened | Require Log4j2, OpenTelemetry, Sentry, Loki, Tempo, Grafana, outbox/DLQ/replay evidence, runtime telemetry toggles, and resilience-lab scenarios. |

# 2. Purpose, Scope, and Authority

## 2.1 Purpose

Define the canonical PostgreSQL schemas, table families, seed data, and runtime configuration required for Login PoC 1.

Ensure AUTH_LOGIN_CONTEXT_ESTABLISH is runtime-assembled through governed MicroFunction configuration instead of hardcoded controller or service logic.

Provide a Flyway-only database baseline for transaction definitions, step catalog references, policy bindings, audit records, outbox events, evidence references, and Dynamic Workspace bootstrap.

Prevent schema drift, simplified step catalogs, direct SQL mutation, manual DDL, frontend authorization authority, or PoC 1A feature leakage into PoC 1.

Define the validation, evidence, rollback, and improvement requirements that must be satisfied before PoC 1 can become a baseline for PoC 1A and PoC 2.

## 2.2 In Scope and Out of Scope
| In Scope | Out of Scope |
| --- | --- |
| Flyway migrations, schemas, table families, seed data, OPA/SBAC references, audit/outbox/evidence records, RLS/classification controls, Dynamic Workspace bootstrap, test data, and evidence manifests. | Manual DDL, production clean, direct database mutation outside approved migration flow, custom password engine, direct credential validation in AIRA, or schema aliases not approved by ADR/TDL. |
| Runtime transaction definition and step binding for AUTH_LOGIN_CONTEXT_ESTABLISH. | Embedding login risk scoring, account lock/unlock, step-up, or AI incident analysis inside PoC 1 instead of PoC 1A. |
| PoC 1 acceptance evidence for DevSecOps, testing, security, observability, idempotency, outbox, DLQ/replay, rollback, and GitNexus impact analysis. | Treating cache, dashboards, frontend state, AI narratives, or LLM Wiki summaries as the authoritative data model. |

## 2.3 Authority and Conflict Rule

If this document conflicts with revised 23C, 41 PoC 1, 43C/43D/43 PoC 1A, 42C roadmap, 10/10A-10E MicroFunction standards, 16/16A/16B database standards, 15/15A API standards, 17/17A security standards, or 31A/53 observability standards, apply the stricter control, record the conflict as an AVCI reconciliation item, and route the decision through the Architecture Board, Security Governance, DBA review, or CAB as applicable.

# 3. Source Alignment and Gap Analysis
| Source / Control | Required Alignment in Document 24 v1.2 |
| --- | --- |
| 01 / 01A / 01B AVCI and Enterprise Architecture | Every schema, seed, runtime definition, migration, audit event, outbox event, policy binding, and evidence record must be attributable, verifiable, classifiable, and improvable. |
| 10 / 10A-10E MicroFunction Standards | Configure the process, reuse standard steps, code only the business gap, keep business logic behind ports/adapters, and produce step-level evidence. |
| 15 / 15A API and Contract-First Standards | Database and runtime configuration must expose approved OpenAPI/AsyncAPI/CloudEvents-compatible contracts and safe error semantics. |
| 16 / 16A / 16B Database and Flyway Standards | All schemas, tables, indexes, RLS, seed data, reference data, and corrections must be Flyway-governed with validation evidence. |
| 17 / 17A Security and Access Control | Identity, JWT validation, OPA/SBAC, secrets hygiene, classification ceilings, and fail-closed behavior must be enforceable and testable. |
| 23C and 41 PoC 1 Standards | Use canonical schemas and canonical 20-step sequence; generate only PoC 1 capabilities and complete PR/MR evidence. |
| 43C/43D/43 PoC 1A Controls | Preserve PoC 1 as stable baseline and allow PoC 1A only as additive, feature-flagged, reversible MicroFunction transactions. |
| 42C and 45 PoC 2 Controls | PoC 2 cannot start until PoC 1/1A exit evidence, regression proof, and unresolved Critical/High findings are complete or formally waived. |
| Gap / Risk Found | Correction Applied in v1.2 |
| --- | --- |
| Older or simplified schema references may generate aira_config or aira_workspace. | Mandates canonical schemas and explicitly maps older aliases to aira_cfg and aira_ui only as reconciliation notes, not physical schemas. |
| Simplified step lists may weaken the Login MicroFunction pattern. | Mandates the canonical 20-step AUTH_LOGIN_CONTEXT_ESTABLISH sequence and rejects missing safety/evidence steps. |
| Runtime cache may be mistaken for authority. | States that Redis/Valkey is derivative only and requires PostgreSQL/Flyway source-of-truth rebuild evidence. |
| PoC 1 and PoC 1A boundaries may blur. | Blocks PoC 1A risk, step-up, lock/unlock, and AI incident functionality from PoC 1 runtime configuration. |
| Observability and resilience may be implemented late. | Makes trace/log/metric/audit/outbox/evidence fields first-class schema and acceptance requirements. |
| Evidence may be produced outside CI. | Requires DevSecOps, GitNexus, Flyway validation, OPA tests, architecture fitness, and evidence pack gates before acceptance. |

# 4. Canonical Database and Flyway Target
| Canonical Schema Rule Use only the canonical physical schemas below unless the approved repository already contains equivalent schemas accepted by ADR/TDL. Do not create aira_config or aira_workspace. Older text referencing aira_config maps to aira_cfg. Older text referencing aira_workspace maps to aira_ui. |
| --- |
| Schema | Authority / Purpose | Minimum Table Families |
| --- | --- | --- |
| aira_mf | Reusable MicroFunction catalog and standard step definitions. | step_catalog; step_version; step_input_schema; step_output_schema; step_control_profile |
| aira_cfg | Runtime transaction definitions, bindings, parameters, policies, adapters, activation, validation, and versioned control data. | txn_definition; txn_step_binding; step_parameter; retry_policy; error_policy; adapter_binding; table_binding; activation; validation_result |
| aira_auth | Login/session/security state for PoC 1 only. | auth_session_context; login_idempotency_guard; jwt_claim_projection; session_capability_view; session_classification_context |
| aira_policy | OPA/SBAC policy registry and version references. | policy_registry; policy_version; policy_binding; policy_decision_ref; sbac_skill_ref |
| aira_audit | Append-only runtime, access decision, step execution, security-control, and evidence audit. | audit_event; access_decision_audit; step_execution_audit; security_control_audit; evidence_link |
| aira_outbox | Transactional event outbox and delivery evidence. | outbox_event; outbox_delivery_attempt; outbox_dead_letter; outbox_replay_request; schema_registry_ref |
| aira_ui | Dynamic Workspace bootstrap, components, capability bindings, policy bindings, and evidence profiles. | workspace_template; screen_definition; component_instance; capability_binding; policy_binding; evidence_profile |

## 4.1 Flyway Migration Governance

All clean-slate database creation, baseline schema, reference tables, seed data, indexes, views, RLS policies, and corrections must be created through Flyway or approved migration workflow only.

No manual DDL, unmanaged SQL patches, direct production mutation, or production clean is permitted.

Every migration must include owner, purpose, affected bounded context, classification, rollback/forward-fix note, validation evidence, and checksum proof.

Seed data must be deterministic, environment-safe, synthetic where applicable, and separated from production secrets or customer data.

Repeatable migrations are allowed for views, safe validation functions, and derived reference projections only when checksum behavior and promotion controls are understood.

# 5. Authoritative Runtime Configuration Model

Document 24 defines how the Login PoC 1 transaction is represented as data and configuration. The controller must not own transaction orchestration. The frontend must not own authorization. Runtime configuration must be validated before activation and must remain inactive until maker-checker review, CI/CD gates, OPA tests, Flyway validation, observability validation, and evidence-pack acceptance pass.
| Runtime Object | Required Fields / Evidence | Acceptance Rule |
| --- | --- | --- |
| Transaction definition | transaction_code, profile_code, version, owner, bounded_context, classification, status, activation_state, rollback_strategy, source_ref, evidence_ref. | AUTH_LOGIN_CONTEXT_ESTABLISH exists once per version/profile and remains inactive until reviewed. |
| Step binding | ordered step_code, dependency, idempotency flag, required input/output schema, policy hook, audit hook, observability hook, error path. | All 20 canonical steps exist in exact order unless formally waived. |
| Parameters | parameter_code, type, default, allowed values, classification, secret flag, runtime toggle flag, owner, environment scope. | No secret values or sensitive runtime values are stored in plaintext. |
| Adapter binding | port code, adapter type, allowed environment, timeout, retry, circuit breaker, owner, evidence_ref. | External dependencies remain behind explicit ports/adapters. |
| Policy binding | policy_ref, policy_version, decision schema, SBAC inputs, fail-closed behavior, decision evidence. | Missing OPA/SBAC binding blocks protected access. |
| Activation record | maker, checker, approver, CI run, Flyway checksum, OPA test result, security scan, effective_from, deactivation path. | No runtime activation without maker-checker and evidence gates. |

# 6. Canonical AUTH_LOGIN_CONTEXT_ESTABLISH Step Sequence

The following canonical step sequence is mandatory for PoC 1 runtime configuration. The implementation may map one step to existing reusable functions, but it must not remove mandatory identity, security, validation, idempotency, audit, event, observability, response, or error controls.
| Order | Step Code | Required Intent |
| --- | --- | --- |
| 1 | STP-RCV-AUTH-REQUEST | Receive approved authentication request or callback through thin adapter. |
| 2 | STP-COR-TRACE | Create or propagate trace_id, span_id, request_id, correlation_id, and causation_id. |
| 3 | STP-RATE-LOGIN | Apply login, callback, tenant, channel, and abuse-rate limits. |
| 4 | STP-SEC-CSRF-CORS | Apply CSRF, CORS, redirect URI, origin, and safe callback controls. |
| 5 | STP-AUTH-REDIRECT | Redirect to approved Keycloak/OIDC Authorization Code + PKCE flow. |
| 6 | STP-IDP-AUTHN | Delegate authentication to Keycloak/AD; no AIRA password validation. |
| 7 | STP-IDP-CLAIMS | Receive and normalize approved identity claims. |
| 8 | STP-JWT-ISSUE | Use IDP-issued token flow; no custom token engine inside AIRA. |
| 9 | STP-JWT-VALIDATE | Validate issuer, audience, expiry, signature, claims, nonce/state where applicable. |
| 10 | STP-SES-RESOLVE | Resolve actor, tenant, branch/unit, roles, groups, skills, and channel. |
| 11 | STP-SEC-OPA-AUTHZ | Call OPA/Rego using RBAC, ABAC, and SBAC inputs. |
| 12 | STP-CLS-CONTEXT | Determine classification ceiling and safe capability exposure. |
| 13 | STP-IDP-LOGIN-IDEMP | Guard callback replay, duplicate session establishment, and retry behavior. |
| 14 | STP-VAULT-SECRETS | Use Vault or approved abstraction; never expose secrets to UI, logs, prompts, tests, or documents. |
| 15 | STP-ENC-SESSION | Protect session context and safe token handling; no token localStorage. |
| 16 | STP-AUD-LOGIN | Write append-only audit and access decision evidence. |
| 17 | STP-EVT-LOGIN | Write transactional outbox event using CloudEvents-compatible metadata. |
| 18 | STP-OBS-LOGIN | Emit trace, metric, structured log, audit, and evidence references. |
| 19 | STP-RSP-SAFE-LOGIN | Return safe session context, capabilities, workspace bootstrap, and safe denial messages. |
| 20 | STP-ERR-AUTH | Apply fail-closed error policy, safe response, audit, outbox/DLQ handling, and improvement capture. |
| PoC 1A Boundary Control The PoC 1 runtime schema must not include AUTH_LOGIN_RISK_REVIEW, AUTH_LOGIN_FAILURE_TRIAGE, AUTH_STEP_UP_REQUIRED, AUTH_ACCOUNT_LOCK_REQUEST, AUTH_ACCOUNT_UNLOCK_REQUEST, or AUTH_LOGIN_INCIDENT_ANALYZE. Those are additive PoC 1A transactions and must be added only through later feature-flagged, reversible Flyway migrations and approval evidence. |
| --- |

# 7. Security, Policy, Audit, Outbox, and Evidence Model
| Control Area | Mandatory Runtime/Data Requirement |
| --- | --- |
| Security | No password storage, hashing, comparison, token leakage, raw JWT logs, raw PII telemetry, client-side policy authority, or direct model-provider calls. |
| OPA/SBAC | All protected actions require policy_ref, policy_version, decision result, decision reason code, classification ceiling, and evidence_ref. |
| Audit | Append-only audit records must capture actor hash, tenant, transaction, step, policy decision, classification, outcome, trace_id, source_ref, and evidence_ref. |
| Outbox | Login security events must be recorded transactionally before delivery. Delivery uses idempotent producer/consumer design, CloudEvents-compatible metadata, schema version, DLQ and replay records. |
| RLS and Classification | Sensitive tables must support least-privilege access, role separation, environment scope, classification metadata, retention rule, and audit of privileged access. |
| Evidence | Evidence records must link migration checksum, CI run, tests, scan results, OPA decision tests, runtime traces, audit IDs, outbox IDs, GitNexus impact analysis, reviewer, and acceptance status. |

## 7.1 Required Event and Replay Fields
| Field | Purpose |
| --- | --- |
| event_id | Globally unique event identifier. |
| event_type | Example: aira.identity.login.context_established or aira.identity.login.denied. |
| source | Service or bounded context producing the event. |
| subject | Hashed actor/session reference only. |
| schema_version | Avro/JSON schema version registered and compatibility-checked. |
| idempotency_key | Deduplication key for retry-safe production and consumption. |
| trace_id / correlation_id / causation_id | End-to-end trace reconstruction and event lineage. |
| classification / retention_rule | Data handling and disposal controls. |
| dlq_reason / replay_request_id | Failure diagnosis and controlled replay evidence. |

# 8. Dynamic Workspace Bootstrap and API/Event Alignment

After a successful and authorized session-context establishment, PoC 1 may bootstrap the Dynamic Workspace using backend-governed aira_ui configuration. Component visibility must be policy-filtered. Widget actions must map to approved capability bindings. The frontend renders; the backend authorizes; MicroFunctions execute; PostgreSQL defines truth; Redis/Valkey accelerates; AVCI proves trust.
| Artifact | Document 24 Requirement |
| --- | --- |
| OpenAPI | Expose session context, capabilities, denial responses, workspace bootstrap, and evidence references through approved contract-first APIs. |
| AsyncAPI / Kafka | Publish login security events and runtime evidence events through approved topics with schema compatibility and replay rules. |
| Dynamic Workspace seed | Seed only safe screens/components needed for PoC 1: authenticated shell, session summary, capability view, evidence timeline, access denied, logout. |
| Frontend safety | No token localStorage, no password collection, no raw denial internals, no hardcoded role visibility, no direct OPA calls, no direct database calls. |
| Generated clients | Frontend and test clients must be generated or validated against approved OpenAPI/AsyncAPI contracts. |
| Policy filtering | Backend resolver must remove unauthorized components, actions, and fields before frontend rendering. |

# 9. DevSecOps, Testing, GitNexus, and Evidence Gates
| Gate | Required Evidence |
| --- | --- |
| Build and migration | Java 25 toolchain, dependency lock, Flyway clean migrate in test, checksum report, no manual DDL, deterministic seed results. |
| Unit and integration tests | Runtime configuration validation, canonical sequence validation, JWT validation, OPA allow/deny, audit writes, outbox writes, fail-closed paths. |
| Contract tests | OpenAPI validation, AsyncAPI validation, schema compatibility, safe Problem Details responses, generated client compatibility. |
| Security gates | SAST, SCA, secret scan, OPA/Rego tests, authenticated DAST where applicable, dependency/license checks, no forbidden telemetry fields. |
| Architecture fitness | No controller business logic, no direct DB/domain leakage, no direct provider SDK calls, ports/adapters preserved, frontend not authority. |
| GitNexus | Read-only impact analysis, affected files, affected tests, architecture drift signals, security-sensitive code map, evidence record; no commit/merge/deploy authority. |
| Evidence Pack | PR/MR AVCI summary, test matrix, policy evidence, Flyway evidence, observability evidence, GitNexus evidence, known limitations, rollback/forward-fix plan. |

## 9.1 Required Test Scenarios

Happy path login context establishment with Keycloak/OIDC and policy allow.

Invalid token, expired token, missing claim, invalid issuer, invalid audience, OPA deny, OPA unavailable, Vault unavailable, audit failure, outbox failure, runtime configuration missing, and database unavailable fail-closed behavior.

Idempotency replay guard and duplicate callback handling.

Canonical schema generation and canonical 20-step sequence validation.

Dynamic Workspace component filtering and safe access denial screen.

No passwords, tokens, raw JWTs, raw PII, secrets, or Restricted payloads in logs, traces, screenshots, prompts, tests, or evidence.

PoC 1A non-implementation check: risk review, step-up, lock/unlock, and AI incident analysis must not exist in PoC 1 runtime configuration.

# 10. Observability, Runtime Telemetry, Resilience, and Improvement Loop

Every successful, denied, failed, retried, replayed, or degraded login transaction must support trace reconstruction without leaking sensitive values. Runtime telemetry may be tuned for performance, but mandatory audit, security, policy decision, outbox, evidence, and protected-action telemetry must not be disabled.
| Signal / Control | Required Treatment |
| --- | --- |
| Log4j2 structured logs | Structured diagnostic logs with trace_id, event code, outcome, safe reason code, and redaction; no secrets or raw PII. |
| OpenTelemetry | Trace/span correlation across frontend callback, gateway, backend, OPA, database, outbox, audit, and workspace resolver. |
| Sentry | Error monitoring for frontend/backend exceptions with redaction and classification controls. |
| Loki / Tempo / Grafana | Logs, traces, dashboards, alerting, policy-denial analysis, outbox/DLQ monitoring, and trace reconstruction. |
| Runtime toggles | Sampling and debug verbosity may be controlled by approved parameters; mandatory security/audit/evidence telemetry remains on. |
| Resilience lab | Test retry-safe, duplicate-safe, cache-loss-safe, database-failure, OPA-failure, outbox-DLQ, replay, heavy-load, and concurrent-callback behavior. |
| Auto-Heal / Auto-Learn / Auto-Improve | May detect issues, retrieve evidence, generate candidate fixes or learning proposals, recommend tests, and open reviewed backlog items; must not self-promote or mutate production silently. |

# 11. Acceptance Criteria, RACI, Review Queue, and AVCI Summary

## 11.1 Definition of Done

Canonical schemas exist and no unauthorized schema aliases are generated.

AUTH_LOGIN_CONTEXT_ESTABLISH transaction definition, step bindings, parameters, policy binding, audit profile, observability profile, error policy, idempotency profile, and activation record are complete.

The canonical 20-step sequence is validated automatically.

Flyway migration and seed evidence is complete and deterministic.

OPA/SBAC policy tests, security tests, architecture fitness tests, OpenAPI/AsyncAPI validation, frontend bootstrap tests, and resilience scenarios pass.

Audit, outbox, DLQ/replay, trace, metric, log, dashboard, and evidence records are generated without forbidden telemetry fields.

GitNexus and CI/CD Evidence Pack are attached to PR/MR.

PoC 1A boundary is verified and PoC 2 readiness evidence is updated.

## 11.2 RACI
| Activity | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Schema and Flyway migration | DBA / Developer | DBA Lead | Architecture, Security, QA | DevSecOps, Internal Audit |
| MicroFunction runtime configuration | Developer / MicroFunction Owner | Software Development Lead | Architecture, Security | QA/SDET |
| OPA/SBAC and security controls | Security Engineer | Security Architecture | Developer, QA, DBA | IT Head, Internal Audit |
| CI/CD and evidence pack | DevSecOps Engineer | DevSecOps Lead | QA, Security, Developer | Architecture, Internal Audit |
| Acceptance and promotion | Maker/Checker Reviewers | Solutions Architecture Office / IT Head | ARB/CAB as required | Delivery Team |

## 11.3 Review Queue Control Register
| Seq | File Name | Recommended Version | Priority | Dependency | Action Required |
| --- | --- | --- | --- | --- | --- |
| 1 | AIRA_24_Login_PoC1_MicroFunction_Runtime_Configuration_Database_Schema_Standard_v1.2_Revised.docx | v1.2 Revised | Completed | 23C, 41 PoC 1, 22B, 43C/43D/43, 42C | Review output and approve or return comments. |
| 2 | AIRA_22B_Login_and_Session_Establishment_MicroFunction_Design_Pattern_v1.2_Revised.docx | v1.2 Revised | High | 24 v1.2, 23C v1.2, 41 v1.1, 43C/43D/43 | Update the parent login MicroFunction design pattern so it aligns with canonical schema, runtime configuration, PoC 1/1A boundaries, DevSecOps evidence, and resilience controls. |
| 3 | AIRA_23A_Login_PoC1_Developer_Source_Code_Generation_Standard_v1.3_Revised.docx | v1.3 Revised | High | 22B and 24 | Update developer source-code generation prompts after the parent login pattern and runtime schema are aligned. |
| 4 | AIRA_38_Login_Function_Prompt_Standard_v1.2_Revised.docx | v1.2 Revised | Medium | 23A, 23C, 24, 41 | Align general login prompt with corrected PoC 1 execution and evidence model. |

## 11.4 AVCI Compliance Summary
| AVCI Property | Evidence in This Standard |
| --- | --- |
| Attributable | Identifies document owner, co-owners, source reviewed, supersedes value, companion standards, RACI, migration ownership, runtime owners, and PR/MR evidence references. |
| Verifiable | Defines Flyway validation, canonical schema checks, canonical step-sequence checks, tests, security scans, OPA decisions, outbox evidence, trace reconstruction, GitNexus analysis, and acceptance gates. |
| Classifiable | Requires classification fields, RLS/least-privilege controls, forbidden telemetry controls, safe evidence storage, no raw PII/secrets/tokens, and classification-aware workspace bootstrap. |
| Improvable | Routes gaps, failed tests, telemetry anomalies, security findings, drift, DLQ/replay outcomes, and GitNexus findings into controlled backlog, candidate fixes, and human-approved improvement loops. |

