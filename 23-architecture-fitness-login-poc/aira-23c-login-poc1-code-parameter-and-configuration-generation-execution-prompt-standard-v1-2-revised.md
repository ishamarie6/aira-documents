---
title: "Login PoC1 Code Parameter and Configuration Generation Execution Prompt Standard"
doc_id: "AIRA-23C"
version: "v1.2"
status: "revised"
category: "Architecture fitness and login PoC"
source_docx: "AIRA_23C_Login_PoC1_Code_Parameter_and_Configuration_Generation_Execution_Prompt_Standard_v1.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 23-architecture-fitness-login-poc
  - revised
  - aira-23c
---



# Login PoC1 Code Parameter and Configuration Generation Execution Prompt Standard



AIRA

AI-Native Enterprise Platform

Login PoC 1 Code, Parameter, and Configuration Generation Execution Prompt Standard

AIRA-DOC-023C | v1.2 Revised

System Builder Lite | Codex Execution Prompt | MicroFunction Runtime Assembly | Canonical Schema | AVCI Evidence
| Document ID | AIRA-DOC-023C |
| --- | --- |
| Canonical Filename | AIRA_23C_Login_PoC1_Code_Parameter_and_Configuration_Generation_Execution_Prompt_Standard_v1.2_Revised.docx |
| Version | v1.2 Revised |
| Supersedes | 23C-AIRA_Login_PoC1_Code_Parameter_and_Configuration_Generation_Execution_Prompt_Standard_v1.1.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Architecture, Security, DevSecOps, DBA, QA/SDET, Frontend, and Team Execution Review |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Security Architecture; Software Development Lead; DevSecOps Lead; DBA; QA/SDET; Platform Engineering; Frontend Engineering; AI Governance; Internal Audit |
| Primary Audience | AIRA System Builder operators; VS Code Codex users; approved AI-assisted coding agents; developers; architects; security; QA/SDET; DevSecOps; DBA; reviewers |
| Primary Parent / Related Baseline | 23A Login PoC 1 Developer Source Code Generation Standard; 41 PoC 1 Execution Instruction; 22B Login MicroFunction Pattern; 24 Login Runtime/DB Standard; 42C Roadmap; 43C/43D/43 PoC 1A controls; 45 PoC2 System Factory standard |
| Effective Date | Upon approval by Solutions Architecture Office / ARB / CAB where required |
| Mandatory Practice Statement Login PoC 1 shall not be treated as a working login screen. It is complete only when AUTH_LOGIN_CONTEXT_ESTABLISH is generated as a governed, runtime-assembled, MicroFunction-backed, policy-controlled, evidence-producing capability with Keycloak/OIDC authentication, OPA/SBAC authorization, Dynamic Workspace bootstrap, Flyway-governed configuration, deterministic tests, observability, rollback/forward-fix path, DevSecOps evidence, GitNexus impact analysis, and AVCI proof. |
| --- |

Table of Contents

This document uses Word heading styles. Insert or update an automatic Microsoft Word Table of Contents before controlled publication.
| Section | Title |
| --- | --- |
| 1 | Executive Summary and v1.2 Correction Verdict |
| 2 | Purpose, Scope, and Authority |
| 3 | Source Alignment and Gap Analysis |
| 4 | Corrected Generation Rules |
| 5 | Canonical Database, Flyway, and Runtime Configuration Target |
| 6 | Canonical MicroFunction Transaction and Step Sequence |
| 7 | Frontend, Dynamic Workspace, and API/Event Requirements |
| 8 | Security, OPA/SBAC, and Fail-Closed Requirements |
| 9 | Testing, DevSecOps, GitNexus, and Evidence Pack Requirements |
| 10 | Observability, Runtime Telemetry, and Resilience Requirements |
| 11 | Copy-Ready System Builder / Codex Execution Prompt |
| 12 | Acceptance Criteria, RACI, Review Queue, and AVCI Summary |

# 1. Executive Summary and v1.2 Correction Verdict

This v1.2 revision updates the corrected 23C execution prompt so AIRA developers and approved coding agents can generate PoC 1 implementation artifacts consistently with the revised PoC 1 execution standard, PoC 1A preservation gates, PoC 2 readiness expectations, Dynamic Workspace standards, MicroFunction controls, and System Builder Lite governance.

The original 23C v1.1 already made the most important corrections: canonical schema naming, canonical MicroFunction sequence, Dynamic Workspace bootstrap, System Builder Lite preconditions, and PoC 1A boundary controls. This v1.2 revision retains those corrections and strengthens the execution prompt with current AIRA-wide requirements for DevSecOps evidence, GitNexus, OpenAPI/AsyncAPI/Kafka/Avro/CloudEvents, outbox/inbox, schema evolution, idempotent consumers, DLQ/replay, observability, authenticated DAST, resilience lab, and controlled Auto-Heal/Auto-Learn/Auto-Improve candidate loops.
| Area | v1.2 Verdict | Required Treatment |
| --- | --- | --- |
| Canonical schema | Retain and strengthen | Use aira_mf, aira_cfg, aira_auth, aira_audit, aira_policy, aira_outbox, and aira_ui. Do not generate simplified physical schemas such as aira_config or aira_workspace. |
| Transaction sequence | Retain and strengthen | Generate AUTH_LOGIN_CONTEXT_ESTABLISH using the canonical 20-step sequence and evidence profile. |
| PoC 1A boundary | Strengthen | Reserve extension hooks only. Do not implement risk review, step-up, account lock/unlock, or AI incident analysis in PoC 1. |
| System Builder Lite | Strengthen | Require AGENTS.md, CODEOWNERS, PR/MR template, CI/CD gates, tests, scans, GitNexus impact analysis, and evidence pack before execution. |
| Enterprise readiness | Strengthen | Add API/event contracts, observability, resilience, security testing, rollback/safe-disable, and PoC 2 entry evidence. |

# 2. Purpose, Scope, and Authority

## 2.1 Purpose

Provide a controlled, repeatable, AI-executable prompt for generating PoC 1 code, runtime parameters, Flyway migrations, MicroFunction configuration, OPA policies, frontend bootstrap, tests, and evidence.

Prevent the System Builder, Codex, or AI-assisted coding agents from inventing non-canonical schemas, simplified step names, direct authorization logic, frontend authority, or PoC 1A behavior.

Translate revised PoC 1 governance into concrete developer deliverables, implementation phases, validation gates, and PR/MR evidence expectations.

Ensure PoC 1 becomes a stable preserved baseline for PoC 1A and a verified entry dependency for PoC 2.

## 2.2 Scope
| In Scope | Out of Scope |
| --- | --- |
| Java 25 / Spring Boot backend; React/TypeScript frontend; Keycloak/OIDC PKCE; OPA/SBAC; PostgreSQL/Flyway; MicroFunction runtime configuration; audit/outbox; Dynamic Workspace bootstrap; tests; evidence. | Custom authentication engine; password validation inside AIRA; frontend authorization authority; manual production DDL; raw token logging or browser storage; PoC 1A security-intelligence implementation. |
| System Builder Lite and Codex execution preconditions, generated repository structure, API contracts, seed data, OPA tests, CI/CD workflow, GitNexus evidence, and PR/MR AVCI summary. | Autonomous deployment, direct production mutation, uncontrolled agent tool use, direct model-provider calls, undocumented schema drift, or unreviewed prompt-driven runtime changes. |

## 2.3 Authority and Precedence
| Level | Authority | Interpretation |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance / Data Governance | Final authority for production-impacting identity, schema, policy, runtime, and evidence decisions. |
| L1 | AIRA AVCI, 01A Enterprise Design Principles, Engineering Blueprint, Security, Database/Flyway, DevSecOps, API, Observability Standards | Universal controls for architecture, evidence, classification, policy, migration, audit, rollback, and promotion. |
| L2 | This 23C v1.2 Standard | Execution prompt authority for PoC 1 code, parameter, configuration, and evidence generation. |
| L3 | 23A, 22B, 24, 41, 43C, 43D, 42C, 45 PoC2 | Specialist PoC 1, PoC 1A, roadmap, and readiness controls. |

# 3. Source Alignment and Gap Analysis
| Source / Control | Alignment Applied in v1.2 |
| --- | --- |
| 23A Login PoC 1 Developer Source Code Generation Standard | Retains Keycloak/OIDC, OPA/SBAC, audit, outbox, safe response, Java 25/Spring Boot, and no custom login rules. |
| 41 PoC 1 Execution Instruction and Evidence Governance Standard v1.1 Revised | Aligns generated artifacts with PoC 1 exit evidence, GitNexus, DevSecOps gates, observability, rollback, and PoC 1A/PoC 2 readiness. |
| 22B / 24 Login MicroFunction and Runtime/DB Standards | Uses canonical runtime transaction, schema families, step catalog, runtime definitions, and Flyway-only seed/migration controls. |
| 43C / 43D / 43 PoC 1A controls | Preserves PoC 1 as baseline; blocks PoC 1A functions from being implemented inside PoC 1. |
| 42C Roadmap and 45 PoC2 System Factory Standard | Requires PoC 1 outputs to become entry evidence for PoC 1A and PoC 2. |
| 12A / 41 / 42 / 44-61 Dynamic Workspace family | Adds backend-governed Dynamic Workspace bootstrap, policy-filtered components, accessibility, telemetry, and evidence requirements. |
| Gap / Risk in Older Prompt | v1.2 Correction |
| --- | --- |
| Simplified schema names could cause drift from canonical database governance. | Physical schema names are locked to aira_mf, aira_cfg, aira_auth, aira_audit, aira_policy, aira_outbox, and aira_ui. |
| Generated code could focus on login screen success rather than runtime MicroFunction proof. | Prompt requires transaction definition, step bindings, audit/outbox, OPA/SBAC, idempotency, tests, and evidence. |
| PoC 1A features could be accidentally introduced into PoC 1. | Explicit boundary excludes risk review, step-up, lock/unlock, and AI incident analysis from PoC 1. |
| DevSecOps evidence and GitNexus checks were not strong enough for PoC 2 entry. | Prompt now requires CI/CD, SAST/SCA/secret scan, DAST plan, GitNexus, architecture fitness, SBOM/provenance, and PR/MR evidence pack. |
| Observability could be optional or inconsistent. | Runtime telemetry, Log4j2 safe logging, OpenTelemetry correlation, Sentry, Loki, Tempo, and Grafana evidence are mandatory for critical paths, with safe runtime toggles for non-critical debug verbosity. |

# 4. Corrected Generation Rules
| Non-Negotiable Generation Rule The System Builder, Codex, or approved coding agent must not generate code or configuration until it confirms the canonical schemas, canonical 20-step transaction, repository controls, OPA/SBAC policy model, Dynamic Workspace bootstrap, and evidence pack requirements. |
| --- |

Generate only PoC 1. Do not generate PoC 1A security-intelligence transactions except as disabled extension placeholders or backlog references.

Use contract-first API design and generated clients where practical. Do not invent endpoints outside the approved contract folder.

Use Flyway for all schema, seed, view, index, RLS, configuration, and reference data changes. Manual DDL is prohibited.

Keep controllers thin. Domain and application logic must not depend on transport, database, workflow, model provider, or UI framework details.

Access to Keycloak, OPA, Vault, PostgreSQL, Redis/Valkey, Kafka, observability, and external systems must go through explicit ports and adapters.

Use PostgreSQL as authority. Redis/Valkey may accelerate idempotency/session/cache lookups but must not become truth.

If Keycloak, OPA, Vault abstraction, audit, JWT validation, runtime configuration, or required evidence path is unavailable, protected access must fail closed.

Do not log or display passwords, raw JWTs, refresh tokens, ID tokens, secrets, private keys, raw PII, stack traces, or sensitive policy reasons.

# 5. Canonical Database, Flyway, and Runtime Configuration Target

## 5.1 Physical Schema Baseline
| Schema | Purpose |
| --- | --- |
| aira_mf | Reusable MicroFunction step catalog and step metadata. |
| aira_cfg | Runtime transaction definitions, step bindings, parameters, retry/error policy, adapter/table bindings, activation, validation results, and runtime definition artifacts. |
| aira_auth | Login/session state, safe session context, idempotency, and replay guard. No raw tokens. |
| aira_audit | Runtime execution, step execution, access decision, security control audit, and evidence references. |
| aira_policy | OPA/SBAC policy registry, policy metadata, and policy version references. |
| aira_outbox | Transactional security event outbox, publish attempts, retry metadata, and DLQ/replay correlation. |
| aira_ui | Dynamic Workspace templates, screens, component catalog, capability/policy bindings, and evidence profiles. |

## 5.2 Minimum Tables or Artifacts to Generate
| # | Artifact | Purpose |
| --- | --- | --- |
| 1 | aira_mf.step_catalog | Reusable MicroFunction step definitions. |
| 2 | aira_cfg.txn_definition | Runtime transaction definition for AUTH_LOGIN_CONTEXT_ESTABLISH. |
| 3 | aira_cfg.txn_step_binding | Ordered runtime step bindings. |
| 4 | aira_cfg.step_parameter | Step-level parameters and feature flags. |
| 5 | aira_cfg.retry_policy / error_policy | Retry and fail-closed policy metadata. |
| 6 | aira_cfg.adapter_binding / table_binding | Ports/adapters and governed table/config binding metadata. |
| 7 | aira_cfg.runtime_definition_artifact | Versioned runtime configuration artifact record. |
| 8 | aira_policy.policy_registry | OPA/SBAC policy registry and decision references. |
| 9 | aira_auth.login_idempotency / session_context | Login callback replay guard and safe session context reference. |
| 10 | aira_audit.runtime_execution / step_execution_audit / access_decision_audit / security_control_audit | Transaction, step, policy, and security-control evidence. |
| 11 | aira_outbox.security_event_outbox / outbox_publish_attempt | Transactional security event and publish/retry evidence. |
| 12 | aira_ui.workspace_template / screen_template / component_catalog / capability_binding | Backend-governed Dynamic Workspace bootstrap. |

# 6. Canonical MicroFunction Transaction and Step Sequence
| transaction_code | AUTH_LOGIN_CONTEXT_ESTABLISH |
| --- | --- |
| version | 1.0.0 |
| bounded_context | identity-and-access |
| classification | CONFIDENTIAL unless overridden by approved policy |
| idempotency_profile | login-callback-replay-guard-v1 |
| error_policy | fail-closed-auth-v1 |
| observability_profile | auth-login-otel-v1 |
| audit_profile | auth-login-audit-v1 |
| rollback_strategy | revert-runtime-definition-and-opa-policy-version; disable affected runtime activation; forward-fix through reviewed Flyway and policy update |
| Order | Step Code | Required Intent |
| --- | --- | --- |
| 1 | STP-RCV-AUTH-REQUEST | Receive authentication request through a thin adapter. |
| 2 | STP-COR-TRACE | Create or propagate trace_id, request_id, correlation_id, and causation_id. |
| 3 | STP-RATE-LOGIN | Apply login rate limit, quota, and abuse-protection policy. |
| 4 | STP-SEC-CSRF-CORS | Apply CSRF, CORS, secure header, and browser safety controls. |
| 5 | STP-AUTH-REDIRECT | Redirect to Keycloak/OIDC Authorization Code + PKCE flow. |
| 6 | STP-IDP-AUTHN | Represent external identity-provider authentication; no passwords in AIRA. |
| 7 | STP-IDP-CLAIMS | Resolve safe identity claims from Keycloak/AD token or profile. |
| 8 | STP-JWT-ISSUE | Represent external token issuance by Keycloak. |
| 9 | STP-JWT-VALIDATE | Validate issuer, audience, signature, expiry, required claims, and replay boundaries. |
| 10 | STP-SES-RESOLVE | Resolve governed AIRA session context. |
| 11 | STP-SEC-OPA-AUTHZ | Evaluate OPA/Rego RBAC/ABAC/SBAC authorization decision. |
| 12 | STP-CLS-CONTEXT | Establish classification ceiling and runtime classification context. |
| 13 | STP-IDP-LOGIN-IDEMP | Prevent callback replay and duplicate login event side effects. |
| 14 | STP-VAULT-SECRETS | Resolve secrets through Vault abstraction; fail closed if unavailable. |
| 15 | STP-ENC-SESSION | Protect and encode safe session context; no raw token persistence. |
| 16 | STP-AUD-LOGIN | Write append-only login/access/step audit evidence. |
| 17 | STP-EVT-LOGIN | Write transactional outbox security event. |
| 18 | STP-OBS-LOGIN | Emit OpenTelemetry-ready log, metric, and trace fields. |
| 19 | STP-RSP-SAFE-LOGIN | Return safe response without token, secret, PII, or stack trace leakage. |
| 20 | STP-ERR-AUTH | Handle all failure paths through fail-closed safe error handling. |

# 7. Frontend, Dynamic Workspace, and API/Event Requirements

## 7.1 Required Frontend Artifacts

LoginEntryPage with “Login with AIRA” action redirecting to the approved OIDC path.

OidcCallbackHandler that delegates token validation/session resolution to backend APIs.

SessionContextLoader that consumes generated API client responses only.

AuthenticatedWorkspaceShell that renders backend-filtered workspace components.

AccessDeniedPage with safe generic denial messages and trace reference.

LogoutButton using approved logout endpoint or redirect path.

SessionSummaryWidget, UserCapabilitiesWidget, and EvidenceTimelineWidget showing safe fields only.

## 7.2 API and Event Contract Requirements
| Contract Area | Mandatory Requirement |
| --- | --- |
| OpenAPI | Define session context, logout, workspace bootstrap, capability binding, error, and evidence endpoints before code generation. |
| AsyncAPI | Define login security event publication, outbox publish attempt, DLQ/replay events, and evidence correlation where Kafka is enabled or stubbed. |
| CloudEvents | Use CloudEvents-style metadata for security events where practical: id, source, type, subject, time, trace, correlation, causation, classification, and evidence reference. |
| Avro / JSON Schema | Define versioned schemas for events and request/response payloads. Schema evolution must be backward-compatible unless explicitly waived. |
| Problem Details | Use safe, classification-aware errors with trace/evidence references and no stack traces or sensitive policy reasons. |
| Frontend Authority Boundary The frontend renders. The backend authorizes. MicroFunctions execute. PostgreSQL defines truth. Redis/Valkey accelerates. AVCI proves trust. The frontend must not decide authorization, classification, workflow approval, or business authority. |
| --- |

# 8. Security, OPA/SBAC, and Fail-Closed Requirements
| Control | Required Treatment |
| --- | --- |
| Authentication | Delegate to Keycloak/OIDC Authorization Code + PKCE. Do not build a custom login or password engine. |
| Token safety | Do not log, display, persist, or store raw JWT, ID token, refresh token, password, or secrets. No token localStorage. |
| Authorization | Use OPA/Rego and SBAC inputs for allow/deny, classification ceiling, safe response, and policy references. |
| Secrets hygiene | Use Vault or a Vault-compatible abstraction. Local dev uses placeholders only and .env.example without secrets. |
| Abuse cases | Test brute force, replay, missing claim, expired token, tenant mismatch, OPA unavailable, forged UI action, and policy bypass attempts. |
| Authenticated DAST | Run authenticated DAST against local/test environments with synthetic users only and produce remediation evidence. |
| Fail closed | If identity, policy, Vault, audit, guardrail, runtime config, or evidence path is unavailable, deny protected access safely. |

# 9. Testing, DevSecOps, GitNexus, and Evidence Pack Requirements
| Test / Gate | Minimum Required Evidence |
| --- | --- |
| Unit and component tests | MicroFunction coordinator, step execution envelope, OPA adapter, Vault adapter, audit/outbox writer, safe response builder, frontend components. |
| Integration tests | Keycloak/OIDC callback, JWT validation, OPA decision, Flyway migrations, PostgreSQL writes, outbox transaction, Redis/Valkey acceleration where used. |
| Contract tests | OpenAPI and AsyncAPI lint/validation, generated client compatibility, error schema, versioning, and idempotency headers. |
| OPA/Rego tests | Valid user allowed; missing skill denied; expired token denied; tenant mismatch denied; admin without MFA denied for Restricted ceiling; replay denied. |
| Security scans | SAST, SCA, secrets scan, container/IaC scan, dependency license review, authenticated DAST, and remediation or waiver record. |
| Architecture fitness | No direct DB/model/provider calls from controllers; no frontend authority; no role hardcoding; no direct Keycloak admin from UI/controller; ports/adapters preserved. |
| GitNexus | Read-only code map, affected files/tests, architecture drift findings, sensitive-code map, PR/MR impact summary, and evidence record. |
| Evidence Pack | CI run, commit, branch, test reports, scan reports, SBOM/provenance, contract reports, policy result, GitNexus output, rollback path, and PR/MR AVCI summary. |

# 10. Observability, Runtime Telemetry, and Resilience Requirements
| Area | Mandatory Treatment |
| --- | --- |
| Log4j2 and structured logging | Emit safe JSON logs with trace_id, request_id, transaction_code, step_code, policy_ref, evidence_ref, and classification. No secrets or raw PII. |
| OpenTelemetry | Propagate traces across frontend, gateway/backend, OPA, PostgreSQL, outbox, and optional Kafka publishing. Use standard semantic attributes where practical. |
| Sentry | Capture frontend/backend errors with safe redaction and trace correlation. No token or secret capture. |
| Loki / Tempo / Grafana | Logs, traces, metrics, dashboards, alerting, and trace reconstruction must link runtime execution, audit, outbox, and PR/MR evidence. |
| Runtime toggles | Debug verbosity and sampling may be adjusted at runtime where performance is affected. Mandatory audit, security, policy-decision, failure, and evidence telemetry must not be disabled. |
| Concurrency and heavy transaction behavior | Use idempotency keys, replay guards, duplicate-safe outbox, retry limits, timeouts, circuit breakers, safe errors, and resilience-lab tests. |
| DLQ and replay | Outbox publish failures must produce retry evidence and DLQ/replay references without duplicating login or audit side effects. |

## 10.1 Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop

PoC 1 may emit improvement candidates from failed tests, security scans, telemetry anomalies, GitNexus drift findings, policy-denial trends, and support feedback. These loops may retrieve evidence and draft candidate fixes, tests, or learning updates, but they must not mutate protected code, runtime configuration, policy, prompts, schemas, model routes, or production environments without human approval, PR/MR review, CI/CD gates, and rollback evidence.

# 11. Copy-Ready System Builder / Codex Execution Prompt
| Usage Rule Use this prompt only inside the approved AIRA System Builder Lite / Codex workflow after repository controls, source baseline, AGENTS.md, CODEOWNERS, PR/MR template, and CI/CD evidence gates are available. |
| --- |

1. You are acting as the AIRA System Builder / AI-assisted senior enterprise engineering agent. Your task is to generate the complete, governed implementation package for AIRA Login PoC 1: Login Authentication, Session Context Establishment, and Basic Authorization.

2. Use the current AIRA canonical baseline as authority: AVCI, Enterprise Design Principles, Engineering Blueprint, Developer Guide, Technology Stack, MicroFunction Framework, API/Integration Contract Standards, Database/Flyway Standards, Security Standards, Observability Standards, DevSecOps Evidence Pack, Dynamic User Workspace Framework, and PoC 1 / PoC 1A / PoC 2 governance standards.

3. Generate PoC 1 only. Do not implement PoC 1A features. Reserve extension hooks only where explicitly required and disabled by default.

4. Implement AUTH_LOGIN_CONTEXT_ESTABLISH as a runtime-assembled MicroFunction transaction using the canonical 20-step sequence, canonical physical schemas, Flyway migrations, OPA/SBAC, audit, outbox, observability, and safe response handling.

5. Use Java 25 / Spring Boot and Spring Security for backend; React/TypeScript for frontend; Keycloak OIDC Authorization Code + PKCE for identity; OPA/Rego for authorization; PostgreSQL/Flyway for authoritative schema; Redis/Valkey only as derivative accelerator; Kafka/outbox as optional/stubbed PoC event path where infrastructure maturity requires.

6. Generate repository structure, OpenAPI/AsyncAPI contracts, generated client configuration, backend ports/adapters, frontend components, OPA policies and tests, Flyway migrations, runtime configuration seed data, Docker Compose/local environment, test suites, CI/CD workflow, GitNexus evidence expectations, README, and PR/MR AVCI evidence summary.

7. Before generating code, output an implementation plan and gap assumptions table. After generating code, output validation commands, test commands, security scan commands, evidence checklist, rollback/forward-fix plan, and known limitations.

8. Reject any approach that stores passwords or tokens in AIRA application code, logs raw secrets/PII, hardcodes authorization in controllers or frontend, uses manual DDL, bypasses OPA/SBAC, bypasses audit/outbox/observability, or allows protected access when identity/policy/evidence controls fail.

# 12. Acceptance Criteria, RACI, Review Queue, and AVCI Summary

## 12.1 Definition of Done
| Category | Acceptance Evidence |
| --- | --- |
| Runnable implementation | Local environment starts; login flow works through Keycloak local realm; backend validates token and resolves safe session context. |
| MicroFunction runtime | AUTH_LOGIN_CONTEXT_ESTABLISH executes through coordinator using canonical step sequence and canonical runtime definitions. |
| Policy and security | OPA/SBAC decision is used; failures fail closed; no raw token/password/secret/PII leakage; synthetic users only. |
| Data and events | Flyway migrations apply cleanly; audit records and outbox event are produced once; idempotency/replay guard is proven. |
| Frontend | Dynamic Workspace bootstrap renders backend-filtered components with safe session fields and accessible loading/denied/error states. |
| DevSecOps | Tests, SAST/SCA, secrets scan, authenticated DAST plan/results, contract tests, GitNexus evidence, SBOM/provenance, and PR/MR AVCI summary are complete. |
| Readiness | PoC 1A entry gate and PoC 2 entry dependency are documented; known limitations and improvement backlog are captured. |

## 12.2 RACI
| Activity | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Prompt execution and candidate generation | Developer / approved coding agent | Software Development Lead | Solutions Architecture; Security; QA/SDET | IT Head; DevSecOps |
| Canonical schema and Flyway review | Developer / DBA | DBA Lead | Architecture; Security | QA/SDET; DevSecOps |
| OPA/SBAC and security review | Security Engineer | Security Architecture | Developer; QA/SDET; Architecture | IT Head; Internal Audit |
| DevSecOps evidence and GitNexus | DevSecOps Engineer | DevSecOps Lead | QA/SDET; Architecture; Security | Software Development Lead |
| Acceptance decision | Architecture / QA / Security reviewers | Solutions Architecture Office / IT Head | DevSecOps; DBA; Product Owner | Development Team |

## 12.3 Review Queue Control Register
| Seq | File | Recommended Version | Review Status | Priority | Dependency | Action Required | Next Step |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | AIRA_23C_Login_PoC1_Code_Parameter_and_Configuration_Generation_Execution_Prompt_Standard | v1.2 Revised | Completed in this output | High | 41 PoC1; 23A; 22B; 24; 42C; 43C/43D; 45 PoC2 | Approve or provide comments for finalization. | Use as PoC 1 code/config generation prompt. |
| 2 | AIRA_24_Login_PoC1_MicroFunction_Runtime_Configuration_Database_Schema_Standard | v1.2 Revised | Recommended next | High | 23C v1.2; 41 PoC1; 48 Dynamic Workspace DB/Flyway | Align runtime configuration tables, seed data, canonical schemas, Flyway, RLS, outbox, audit, and rollback with revised 23C. | Review next. |
| 3 | AIRA_22B_Login_and_Session_Establishment_MicroFunction_Design_Pattern | v1.2 Revised | Pending | High | 23C and 24 | Align design pattern with revised canonical 20-step transaction, PoC 1A boundary, and evidence gates. | Review after 24. |
| 4 | AIRA_23A_Login_PoC1_Developer_Source_Code_Generation_Standard | v1.3 Revised | Pending | Medium | 23C, 41, 24, 22B | Align developer prompts with final 23C/24 corrections and revised evidence expectations. | Review after 22B. |

## 12.4 AVCI Compliance Summary
| AVCI Property | Evidence in This v1.2 Revision |
| --- | --- |
| Attributable | Document owner, co-owners, source baseline, governing documents, roles, RACI, prompt user, branch/commit, and generated artifacts are identified. |
| Verifiable | Requires canonical schemas, step sequence, tests, OPA decisions, Flyway validation, audit/outbox, observability, GitNexus, CI/CD evidence, and PR/MR summary. |
| Classifiable | Document is INTERNAL CONFIDENTIAL; generated code, logs, prompts, evidence, telemetry, session context, and artifacts require classification and redaction controls. |
| Improvable | Known limitations, backlog, scan findings, telemetry anomalies, GitNexus findings, and Auto-Heal/Auto-Learn/Auto-Improve candidates feed governed improvement loops. |

# 13. Change Log and External Alignment Notes
| Version | Change Summary |
| --- | --- |
| v1.1 | Corrected System Builder / Codex execution baseline: canonical schema, canonical 20-step sequence, Dynamic Workspace bootstrap, and System Builder Lite preconditions. |
| v1.2 Revised | Aligned with revised PoC 1, PoC 1A, PoC 2, Dynamic Workspace, MicroFunction, DevSecOps, GitNexus, API/event, observability, DAST, resilience, and continuous improvement controls. |

External alignment references used for current industry terminology: OpenAPI 3.2.0 for HTTP API contracts; AsyncAPI 3.1.0 / AsyncAPI Initiative for event-driven API contracts; OpenTelemetry Semantic Conventions for telemetry naming; and OWASP ASVS 5.0.0 for application/API security verification expectations. AIRA implementation remains governed by internal source authority first.

