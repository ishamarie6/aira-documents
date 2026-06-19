---
title: "Login PoC1A Code Parameter and Configuration Generation Execution Prompt Standard"
doc_id: "AIRA-43D"
version: "v1.2"
status: "revised"
category: "Continuous improvement, multimodal AI, and PoC1A"
source_docx: "AIRA_43D_Login_PoC1A_Code_Parameter_and_Configuration_Generation_Execution_Prompt_Standard_v1.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 43-continuous-improvement-multimodal-poc1a
  - revised
  - aira-43d
---



# Login PoC1A Code Parameter and Configuration Generation Execution Prompt Standard



AIRA

AI-Native Enterprise Platform

Login PoC 1A Code, Parameter, and Configuration Generation Execution Prompt Standard

v1.2 Revised

Additive Login Security Intelligence | Canonical Schema | Human Approval | Dynamic Workspace | DevSecOps Evidence | AVCI Always
| Mandatory Practice Statement PoC 1A must be implemented as a progressive, additive, non-destructive extension to corrected PoC 1. It must preserve AUTH_LOGIN_CONTEXT_ESTABLISH, canonical PoC 1 MicroFunction runtime assembly, OPA/SBAC authorization, audit/outbox evidence, observability, safe responses, Dynamic Workspace bootstrap, and canonical schema naming. PoC 1A may add risk review, failure triage, step-up decisioning, account lock/unlock human approval, and AI-assisted incident analysis only through additive MicroFunction transactions, additive Flyway migrations, policy-as-code, feature flags, deterministic tests, maker-checker review, CI/CD gates, and AVCI evidence. |
| --- |
| Document ID | AIRA-DOC-043D |
| --- | --- |
| Recommended Version | v1.2 Revised |
| Status | Draft for Architecture, Security, DevSecOps, QA/SDET, DBA, AI Governance, and Team Execution Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Security Architecture; Software Development Lead; DevSecOps Lead; QA/SDET; DBA; Platform Engineering; AI Governance; Enterprise Architecture; SRE / Operations; Internal Audit |
| Effective Date | Upon ARB / Security Governance / DevSecOps Governance approval |
| Review Cadence | After PoC 1A execution; before PoC 2; quarterly; unscheduled on material login, identity, policy, workflow, AI, database, Dynamic Workspace, DevSecOps, or roadmap change |

# Table of Contents

Insert an automatic Microsoft Word Table of Contents here before final publication. Use References > Table of Contents > Automatic Table, then update field after final pagination.

# 1. Document Control
| Document Title | AIRA Login PoC 1A Code, Parameter, and Configuration Generation Execution Prompt Standard |
| --- | --- |
| Document ID | AIRA-DOC-043D |
| Canonical Filename | AIRA_43D_Login_PoC1A_Code_Parameter_and_Configuration_Generation_Execution_Prompt_Standard_v1.2_Revised.docx |
| Version | v1.2 Revised |
| Supersedes | 43D v1.1 Corrected Additive System Builder / Codex Execution Baseline |
| Source Document Reviewed | 43D-AIRA_Login_PoC1A_Code_Parameter_and_Configuration_Generation_Execution_Prompt_Standard_v1.1.docx |
| Primary Parent | 23C-AIRA Login PoC 1 Code, Parameter, and Configuration Generation Execution Prompt Standard v1.1; 42C Foundation PoC Roadmap v1.4 Revised |
| Primary Audience | AIRA System Builder operators; VS Code Codex users; software developers; technical leads; security; QA/SDET; DevSecOps; DBA; AI Engineering; Product Owners; reviewers; Internal Audit |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / PoC / PoC1A / 43D-v1.2 / |
| External Alignment | OpenAPI 3.2.0; AsyncAPI 3.1.0; OWASP ASVS 5.0.0; OpenTelemetry Semantic Conventions; CloudEvents; NIST SSDF; SLSA |

## 1.1 v1.2 Change Summary
| Change Area | v1.2 Treatment |
| --- | --- |
| Roadmap alignment | Aligns PoC 1A execution with 42C v1.4 and PoC 2 entry evidence expectations. |
| Dynamic Workspace alignment | Aligns security review screens, approval queues, AI advisory summary widgets, accessibility, and frontend authority boundaries with revised 41, 42, 44, 46-61, and 12A controls. |
| DevSecOps evidence | Adds explicit gates for GitNexus, Evidence Pack, SAST, SCA, authenticated DAST, contract tests, OPA tests, Flyway validation, architecture fitness, and PR/MR AVCI summary. |
| Event and integration readiness | Adds OpenAPI, AsyncAPI, Kafka, Avro, CloudEvents, outbox/inbox, schema evolution, idempotent consumers, DLQ, and replay evidence where applicable. |
| Observability and operations | Adds Log4j2, OpenTelemetry, Sentry, Loki, Tempo, Grafana, audit, alerting, trace reconstruction, and runtime telemetry toggle controls. |
| Resilience and concurrency | Adds retry-safe, duplicate-safe, concurrent, heavy-load, failure-aware transaction behavior and Resilience Lab requirements. |
| Continuous improvement | Adds Auto-Heal, Auto-Learn, and Auto-Improve candidate loop with issue detection, evidence retrieval, candidate proposal, tests, and human approval. |

# 2. Executive Review Summary

The v1.1 source document is structurally sound and must be retained as the execution baseline for PoC 1A. It correctly establishes that PoC 1A extends PoC 1 without replacing it, preserves AUTH_LOGIN_CONTEXT_ESTABLISH, uses canonical schema names, relies on additive Flyway migrations, and restricts step-up, lock, unlock, and AI incident analysis to governed, evidence-producing paths.

This v1.2 revision strengthens the execution prompt for developers and System Builder Lite by adding the controls introduced in the revised Dynamic Workspace, Composable Experience, System Builder, AI Agent Governance, DevSecOps, PoC roadmap, and PoC 2 evidence documents. It does not broaden PoC 1A into business module development. It makes PoC 1A a controlled proof of login security intelligence and a clean entry gate for PoC 2.

## 2.1 Retain, Correct, Strengthen
| Review Area | Decision | Required Treatment |
| --- | --- | --- |
| PoC 1 preservation | Retain and strengthen | PoC 1 must still pass with all PoC 1A feature flags disabled. |
| Canonical schemas | Retain | Use aira_mf, aira_cfg, aira_auth, aira_audit, aira_policy, aira_outbox, and aira_ui. Do not generate aira_config or aira_workspace. |
| Step-up authentication | Clarify | AIRA records the requirement and delegates challenge execution to Keycloak or approved IdP. AIRA does not implement MFA. |
| Lock/unlock | Strengthen | No UI, controller, AI, or agent directly locks/unlocks accounts without policy, workflow, human approval, and evidence. |
| AI incident analysis | Strengthen | AI is advisory only and must use LiteLLM or approved gateway, guardrails, classification, audit, and evidence. |
| Dynamic Workspace | Strengthen | Screens and widgets are policy-filtered, backend-governed, accessible, observable, and non-authoritative. |
| PoC 2 readiness | Add | PoC 1A exit evidence must feed PoC 2 entry gate and roadmap evidence pack. |

# 3. Source and Context Alignment Findings

This document must be interpreted as an execution prompt standard, not as an architecture authority that overrides the governing AIRA standards. It is subordinate to AVCI, Enterprise Design Principles, MicroFunction, Security, Database/Flyway, API/Event, Dynamic Workspace, AI Governance, DevSecOps, and Change/Release governance.
| Source / Standard Family | Alignment Required for 43D v1.2 |
| --- | --- |
| 01 / 01A / 01B AVCI and Enterprise Design Principles | Every generated artifact must be attributable, verifiable, classifiable, improvable, secure, testable, observable, reversible, and policy-governed. |
| 10 / 10A / 10B / 10C / 10D MicroFunction Standards | PoC 1A behavior is added as configured MicroFunction transactions and steps, not controller logic or direct database/tool calls. |
| 15 / 15A API and Integration Contract Standards | REST APIs, async events, CloudEvents, schemas, Problem Details, idempotency profiles, and generated clients must be contract-first. |
| 16 / 16A / 16B Database and Flyway Standards | All schema additions, seed data, RLS, indexes, views, outbox/inbox, replay, and rollback/forward-fix changes are Flyway-governed. |
| 17 / 17A Security Standards | Identity, tokens, secrets, roles, skills, policies, step-up, lock/unlock, redaction, and secure errors must fail closed. |
| 31A / 52 / 53 Observability and Testing | Each critical flow must emit and verify trace, metric, log, audit, outbox, policy, evidence, dashboard, and trace-reconstruction data. |
| 41 / 42 / 44 / 46-61 Dynamic Workspace Family | Workspace screens, widgets, AI panels, templates, and experience blocks are rendered from backend-governed, policy-filtered, contract-bound configuration. |
| 41B / 44A System Builder | System Builder may analyze, recommend, draft, and generate candidate artifacts only through branch-bound, evidence-producing, maker-checker workflows. |
| 42D-42S AI Agent Governance | Any AI-agent involvement must remain registered, scoped, tool-gated, observable, reversible, and subordinate to human approval. |
| 42C v1.4 and 45 PoC 2 | PoC 1A exit evidence must prove readiness for PoC 2 DevSecOps/System Factory execution. |

# 4. Gap Analysis and Corrections
| Gap / Risk | v1.2 Correction |
| --- | --- |
| PoC 1A can be mistaken as a second login design. | States that PoC 1A is an additive security-intelligence layer only; PoC 1 remains the login/session foundation. |
| Generated code could implement lock/unlock directly in UI or controller. | Blocks direct mutation; requires workflow, OPA/SBAC, maker-checker, human approval, and audit/evidence. |
| Frontend could be treated as security authority. | Defines frontend as non-authoritative renderer only; backend policy and MicroFunctions decide. |
| AI summary could be treated as decision authority. | AI remains advisory and cannot approve access, unlock users, change policy, or bypass step-up. |
| Insufficient PoC 2 readiness evidence. | Adds explicit exit evidence mapped to PoC 2 entry gate, GitNexus, Evidence Pack, tests, scans, and rollback proof. |
| Concurrency and heavy transaction behavior not explicit enough. | Adds idempotency keys, outbox/inbox, locking, duplicate suppression, replay safety, DLQ handling, and Resilience Lab scenarios. |
| Telemetry could expose tokens or PII. | Adds forbidden telemetry fields, Log4j2 safe logging, OTel redaction, Sentry sanitization, Loki label discipline, and metric cardinality control. |

# 5. Purpose, Scope, and Authority

## 5.1 Purpose

The purpose of this standard is to provide a controlled, copy-ready, AI-executable, and developer-usable prompt standard for generating Login PoC 1A code, parameters, configuration, tests, policies, evidence, and documentation without architecture drift.

## 5.2 In Scope

Progressive extension of corrected PoC 1 without destructive rewrite.

Additive MicroFunction transactions for login risk review, failure triage, step-up decisioning, account lock request, account unlock request, and AI-assisted login incident analysis.

Additive Flyway migrations, canonical schema use, runtime parameters, feature flags, OPA/Rego policies, Flowable workflow definitions or safe workflow abstractions, and Dynamic Workspace security review screens.

OpenAPI contracts, generated clients, AsyncAPI/event definitions, CloudEvents, Avro schemas, outbox/inbox, idempotency, DLQ/replay, observability, security tests, and PR/MR evidence.

System Builder Lite / VS Code Codex execution under branch-bound, maker-checker, evidence-producing controls.

## 5.3 Out of Scope

Replacing PoC 1 or rewriting AUTH_LOGIN_CONTEXT_ESTABLISH except approved defect correction or explicitly approved extension hook.

Custom password authentication, password storage, password validation, credential checking, or MFA implementation inside AIRA.

Direct account lock, unlock, step-up bypass, or access approval from UI, controller, AI, or unapproved automation.

Frontend authorization authority or client-side policy authority.

Manual DDL, direct production data mutation, direct model-provider SDK calls, or unmanaged agent/tool execution.

Promotion to PoC 2 without PoC 1 and PoC 1A exit evidence accepted by the required reviewers.

## 5.4 Authority and Precedence
| Level | Authority | Role |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance | Final authority for production-bound interpretation, high-risk controls, and exceptions. |
| L1 | AIRA AVCI, Enterprise Architecture, Security, DevSecOps, Database, MicroFunction, API, AI Governance, and Change Standards | Universal governance, quality, evidence, policy, rollback, and improvement discipline. |
| L2 | This 43D v1.2 Standard | Execution prompt authority for PoC 1A code, parameter, configuration, test, policy, and evidence generation. |
| L3 | Generated PR/MR, tests, migrations, policies, contracts, evidence pack, and review records | Candidate implementation proof; not authoritative until approved. |
| Conflict Rule Where documents conflict, apply the stricter AIRA control temporarily, record the issue as an AVCI reconciliation item, assign an owner, and resolve through governed review. Do not silently choose the easier interpretation. |
| --- |

# 6. Non-Negotiable Generation Rules

Inspect the corrected PoC 1 implementation before generating any PoC 1A artifact.

Preserve AUTH_LOGIN_CONTEXT_ESTABLISH, PoC 1 contracts, PoC 1 tests, PoC 1 database migrations, OPA integration, audit/outbox evidence, and Dynamic Workspace bootstrap.

Use canonical schemas: aira_mf, aira_cfg, aira_auth, aira_audit, aira_policy, aira_outbox, aira_ui, and approved AI/evidence schemas where applicable.

Do not create aira_config, aira_workspace, duplicate login runtime tables, parallel login flows, or controller-owned policy decisions.

Implement PoC 1A behavior through additive MicroFunction transactions and step bindings, additive Flyway migrations, runtime flags, and OPA/SBAC policy decisions.

Keep all business logic behind Clean Architecture boundaries and ports/adapters. Controllers, UI components, workflow tasks, and AI tools must remain adapters or orchestrated interfaces.

All model traffic routes through LiteLLM or approved private gateway with guardrails. Application code must not call model providers directly.

Every state-changing action must be idempotent, audit-producing, observable, reversible or safely disableable, and backed by PR/MR evidence.

# 7. PoC 1A Additive Capability Model
| Transaction Code | Purpose | Invocation Pattern | Evidence Required |
| --- | --- | --- | --- |
| AUTH_LOGIN_RISK_REVIEW | Deterministically evaluate login risk using approved signals and OPA policy. | After PoC 1 identity/session context is available and before elevated capability exposure where configured. | risk_decision_id, policy_decision_id, trace_id, evidence_ref, risk factors hash. |
| AUTH_LOGIN_FAILURE_TRIAGE | Classify login/session/access failures into safe categories and record evidence. | On failed login, denied policy decision, expired/invalid token, lock state, or repeated failure pattern. | failure_category, safe_reason_code, actor_hash, correlation_id, audit_event_id. |
| AUTH_STEP_UP_REQUIRED | Determine and record policy-based step-up requirement and delegate challenge to Keycloak or approved IdP. | When OPA returns step-up or risk/classification requires higher assurance. | step_up_request_id, policy_ref, idp_challenge_ref, outcome_ref. |
| AUTH_ACCOUNT_LOCK_REQUEST | Create governed human approval request for lock or security hold. | Critical risk, suspicious attempts, security admin request, or policy-directed review. | workflow_id, requester, checker, policy_decision, evidence_ref, SoD check. |
| AUTH_ACCOUNT_UNLOCK_REQUEST | Create governed human approval request for unlock. | User/support/security unlock request after policy screening. | workflow_id, requester, approver, reason_code, evidence_ref, SoD check. |
| AUTH_LOGIN_INCIDENT_ANALYZE | Generate advisory AI incident analysis from approved evidence. | After evidence retrieval and classification eligibility checks. | model_route_ref, guardrail_result, source_refs, summary_hash, reviewer_decision. |

# 8. Canonical Schema and Configuration Rules

The generated package must use the corrected canonical schema names and must not introduce simplified schema drift. All new tables, views, indexes, RLS policies, seed data, and reference data must be delivered through Flyway migrations and validated through CI/CD gates.
| Schema | Required Use in PoC 1A | Generation Rule |
| --- | --- | --- |
| aira_mf | MicroFunction catalog, step catalog, transaction definitions, step bindings, execution profiles. | Additive rows only. Do not hardcode transaction steps in application code. |
| aira_cfg | Runtime parameters, feature flags, retry policies, error policies, activation, validation, adapter bindings. | Use configuration-first assembly and safe disablement. |
| aira_auth | Login security intelligence reference records, risk decisions, step-up state references, approved synthetic users where applicable. | No password storage, no raw tokens, no direct credential checks. |
| aira_policy | OPA/SBAC policy binding records, policy versions, policy decision references. | Policies are versioned artifacts with tests and fail-closed defaults. |
| aira_audit | Append-only audit events and evidence linkages. | No updates that destroy prior audit state. |
| aira_outbox | Transactional outbox/inbox, CloudEvents, DLQ, replay, and idempotency records. | Every important security event is durable and replay-safe. |
| aira_ui | Dynamic Workspace configuration, screens, widgets, action bindings, approval queues, safe notices. | Policy-filtered rendering only; frontend remains non-authoritative. |

# 9. Required Generated Artifact Package
| Artifact Family | Minimum Required Outputs |
| --- | --- |
| Backend implementation | Java 25 / Spring Boot services, ports, adapters, use cases, MicroFunction handlers, OPA client adapter, workflow adapter, AI gateway adapter, audit/outbox adapter, safe error handling. |
| Frontend implementation | React/TypeScript components, generated API clients, Dynamic Workspace screens, approval queue widgets, user-safe notices, accessibility support, and policy-filtered rendering. |
| Database and configuration | Additive Flyway migrations, seed data, RLS policies, indexes, views, feature flags, runtime parameters, cache invalidation records, rollback/safe-disable plan. |
| Contracts and events | OpenAPI contracts, AsyncAPI contracts, Avro schemas, CloudEvents definitions, Problem Details errors, idempotency profile, schema evolution notes, DLQ/replay plan. |
| Policy and workflow | OPA/Rego policies and tests, SBAC skills, ABAC inputs, Flowable workflow definitions or safe workflow abstraction, maker-checker and separation-of-duties rules. |
| AI advisory controls | LiteLLM route references, guardrail tests, approved evidence retrieval, prompt template, source citation/ref rules, AI output disclaimer, reviewer approval path. |
| Tests and evidence | Unit, component, integration, contract, OPA, workflow, frontend, Playwright, accessibility, authenticated DAST, SAST, SCA, secret scan, architecture fitness, resilience lab, GitNexus, and Evidence Pack. |

# 10. API, Event, Idempotency, and Replay Rules

PoC 1A APIs and events must be contract-first and evidence-producing. Where a feature is not implemented in PoC 1A, the contract must either be absent or clearly marked as draft/test-only. No UI or agent may invent endpoints, event topics, schemas, or action semantics outside approved contracts.
| Control Area | Mandatory Rule |
| --- | --- |
| OpenAPI | REST endpoints use approved paths, request/response schemas, Problem Details errors, correlation IDs, idempotency keys, authentication, authorization, and generated clients. |
| AsyncAPI / Kafka | Security intelligence events and workflow outcomes use AsyncAPI where asynchronous messaging is present. |
| Avro / Schema Evolution | Event payloads use registered schemas with compatibility rules and version metadata. |
| CloudEvents | Security, step-up, workflow, audit, and evidence events carry consistent CloudEvents metadata. |
| Outbox / Inbox | Database state and event publication are transactionally coupled; consumers are duplicate-safe and replay-safe. |
| DLQ / Replay | Failed event processing produces DLQ records, reason codes, remediation path, and replay evidence. |

# 11. Dynamic Workspace and Frontend Generation Rules

PoC 1A screens and widgets are governed Dynamic Workspace artifacts. They render approved state and request approved actions. They do not decide authorization, perform privileged account actions, or become business authority.
| Workspace Element | Required Behavior |
| --- | --- |
| Security Review Queue | Shows policy-filtered suspicious login review items, risk category, evidence summary, allowed actions, and approval status. |
| Step-Up Notice | Shows user-safe message when step-up is required; does not expose raw risk scoring, policies, tokens, or internal signals. |
| Lock / Unlock Request Screen | Allows authorized request creation and review, subject to OPA/SBAC, SoD, workflow, and maker-checker controls. |
| AI Incident Summary Widget | Displays advisory summary with source/evidence references, guardrail result, classification, reviewer status, and non-authority disclaimer. |
| Evidence Timeline | Shows trace, audit, policy decision, workflow, outbox, and event references without exposing secrets or raw PII. |
| Accessibility | All screens support keyboard operation, accessible labels, focus management, responsive layout, safe error messages, and WCAG 2.2 AA target controls. |

# 12. Security, OPA/SBAC, and AI Advisory Controls
| Control | Mandatory Treatment |
| --- | --- |
| OPA/SBAC/ABAC | Policies determine allow, deny, step-up, human review, lock request, unlock request, security hold, missing skill, and policy exception paths. |
| Secrets hygiene | No secrets, raw tokens, passwords, raw JWTs, private keys, privileged credentials, or production data in source, prompts, logs, UI, tests, screenshots, traces, or evidence summaries. |
| Step-up | AIRA can decide and record step-up requirement; approved IdP performs the challenge. AIRA must not implement MFA logic internally. |
| Lock/unlock | Lock/unlock is human-accountable and workflow-controlled. No direct lock/unlock from UI, controller, AI, or unapproved automation. |
| AI incident analysis | AI summarizes approved evidence only. It cannot approve, deny, unlock, lock, bypass step-up, change policy, or mutate production. |
| Authenticated DAST | Authenticated flows must be scanned with synthetic identities, safe test tenants, policy-controlled roles/skills, and remediation evidence for Critical/High findings. |

# 13. Observability, Runtime Telemetry, and Evidence Requirements

PoC 1A is not accepted unless its behavior can be reconstructed from logs, metrics, traces, audit records, policy decisions, workflow events, outbox events, and evidence records. Debug verbosity may be runtime-toggled when performance is affected, but protected-action audit, security, policy, evidence, and trace-correlation telemetry must not be disabled.
| Signal / Tool | Required Evidence |
| --- | --- |
| Log4j2 / structured logs | Safe diagnostic logs with correlation_id, trace_id, event_code, classification, redaction state, and no forbidden fields. |
| OpenTelemetry | Traces and metrics across frontend, gateway, backend, OPA, workflow, database, outbox, Kafka, AI gateway, and evidence store. |
| Sentry | Sanitized error monitoring for frontend/backend exceptions, with source maps controlled and no secrets/PII. |
| Loki / Tempo / Grafana | Queryable logs, traces, dashboards, alerts, policy-denial analysis, slow transaction views, and trace reconstruction. |
| Audit and evidence | Append-only security audit events and Evidence Pack references for each sensitive action. |
| Runtime toggles | Configurable debug verbosity and sampling, with mandatory audit/security/evidence telemetry always on. |

# 14. Testing, DevSecOps, GitNexus, and Resilience Gates
| Gate | Minimum Acceptance Evidence |
| --- | --- |
| PoC 1 regression | All existing PoC 1 tests pass with PoC 1A disabled and enabled. |
| Unit and component tests | Backend, frontend, MicroFunction, policy, workflow, adapter, and AI-gateway stubs tested with deterministic fixtures. |
| Contract tests | OpenAPI, generated clients, Problem Details, AsyncAPI/events, Avro schemas, CloudEvents, and idempotency profiles validated. |
| Security tests | SAST, SCA, secret scan, OPA tests, authenticated DAST, dependency/license checks, and secure API tests pass or have approved waiver. |
| Architecture fitness | CI rejects controller business logic, direct DB/domain leakage, direct model-provider calls, frontend authority, direct Keycloak Admin calls from controller, and missing evidence. |
| GitNexus | Read-only code map, impact analysis, affected tests, security-sensitive code map, and architecture drift review generated. |
| Resilience Lab | Retry, duplicate callback, concurrent approval, outbox failure, DLQ, replay, cache loss, OPA outage, AI gateway failure, workflow timeout, and heavy-load synthetic tests executed. |
| Evidence Pack | PR/MR AVCI summary, test reports, scan reports, policy results, migration validation, trace samples, dashboards, GitNexus report, rollback/safe-disable proof, and improvement backlog. |

# 15. Copy-Ready PoC 1A System Builder Lite / Codex Execution Prompt
| Use Instruction The following prompt may be copied into VS Code Codex or the approved System Builder Lite execution surface after the readiness gates are met. It must be executed on a feature branch only. Generated output remains draft until maker-checker review, CI/CD gates, and AVCI evidence are accepted. |
| --- |

Read and summarize AGENTS.md, CODEOWNERS, PR template, current PoC 1 implementation, 23C PoC 1 prompt standard, 43D v1.2, 42C v1.4 roadmap, MicroFunction standards, API/database/security/observability standards, and Dynamic Workspace standards. Do not edit files until the inspection summary is accepted.

Confirm that AUTH_LOGIN_CONTEXT_ESTABLISH exists and that PoC 1 tests, contracts, runtime configuration, OPA/SBAC, audit/outbox, observability, and Dynamic Workspace bootstrap are understood.

Generate PoC 1A only as additive changes. Do not rename PoC 1 transactions, replace PoC 1 schemas, duplicate login tables, create aira_config, create aira_workspace, implement custom authentication, implement MFA, call model providers directly, or place business logic in controllers.

Create additive MicroFunction transactions: AUTH_LOGIN_RISK_REVIEW, AUTH_LOGIN_FAILURE_TRIAGE, AUTH_STEP_UP_REQUIRED, AUTH_ACCOUNT_LOCK_REQUEST, AUTH_ACCOUNT_UNLOCK_REQUEST, and AUTH_LOGIN_INCIDENT_ANALYZE.

Use canonical schemas aira_mf, aira_cfg, aira_auth, aira_policy, aira_audit, aira_outbox, and aira_ui. Generate additive Flyway migrations, seed rows, policy bindings, RLS where applicable, outbox/inbox support, idempotency keys, and safe-disable flags.

Generate OpenAPI contracts, generated clients, safe Problem Details errors, AsyncAPI/event definitions if events are used, Avro schemas where applicable, CloudEvents metadata, outbox/DLQ/replay behavior, and contract tests.

Generate backend Java 25 / Spring implementation using Clean Architecture, DDD boundaries, ports/adapters, thin controllers, OPA/SBAC policy checks, workflow adapter, AI gateway adapter, audit/outbox adapter, and safe error handling.

Generate Dynamic Workspace React/TypeScript components and configuration for security review queue, step-up notice, lock/unlock request workflow, AI advisory summary widget, and evidence timeline. The frontend must be policy-filtered and non-authoritative.

Generate OPA/Rego policies and tests for allow, deny, step-up, human review, security hold, lock request, unlock request, privileged unlock, separation of duties, missing skill, stale evidence, and fail-closed paths.

Generate observability, audit, and evidence instrumentation using safe Log4j2 logging, OpenTelemetry trace/metric/log correlation, Sentry sanitization, Loki/Tempo/Grafana dashboard metadata, evidence references, and runtime telemetry toggle configuration. Never log passwords, raw tokens, raw JWTs, secrets, raw PII, prompts with restricted data, embeddings, or high-cardinality sensitive identifiers.

Generate deterministic tests and evidence scripts covering PoC 1 regression, PoC 1A unit/component/integration, contract tests, OPA tests, workflow tests, frontend tests, accessibility tests, authenticated DAST preparation, resilience lab scenarios, concurrency, duplicate callback, idempotency, DLQ/replay, cache loss, and AI gateway failure.

Generate PR/MR AVCI summary, GitNexus request checklist, evidence manifest, rollback/safe-disable plan, known limitations, improvement backlog, and reviewer checklist. Stop after generating candidate artifacts; do not merge, deploy, approve, or mutate production.

# 16. PR/MR AVCI and Evidence Template
| AVCI Area | Required PR/MR Content |
| --- | --- |
| Attributable | Owner, developer, reviewer/checker, ticket, branch, commit, prompt standard, AI tools used, generated artifact list, source standards referenced. |
| Verifiable | Build results, unit tests, frontend tests, OPA tests, contract tests, workflow tests, Playwright tests, SAST/SCA/secret scan, authenticated DAST result or planned evidence, Flyway validation, GitNexus report, trace/dashboard samples. |
| Classifiable | Data classification, synthetic data declaration, secrets/PII handling, token handling, log redaction, model route eligibility, evidence storage path, retention rule. |
| Improvable | Known limitations, deferred items, improvement backlog, prompt improvements, standards requiring update, resilience gaps, observability tuning recommendations. |

# 17. Final Acceptance Criteria

PoC 1 works unchanged when PoC 1A feature flags are disabled.

PoC 1A adds only approved transactions, policies, configurations, migrations, widgets, tests, and evidence.

All account lock/unlock and privileged security actions require OPA/SBAC, workflow, maker-checker, separation of duties, and named human approval.

Step-up decisioning is recorded by AIRA but the challenge is performed by Keycloak or the approved IdP.

AI incident analysis remains advisory, source-grounded, guardrailed, auditable, and human-reviewed.

Canonical schemas, Flyway-only migration, RLS/classification controls, outbox/inbox, idempotency, DLQ/replay, and rollback/safe-disable evidence are present.

Dynamic Workspace screens are backend-governed, policy-filtered, accessible, responsive, observable, and non-authoritative.

CI/CD gates pass or have approved waivers. Critical and High security findings block acceptance unless formally approved by required authority.

Evidence Pack is complete and PoC 1A exit review is accepted before PoC 2 proceeds.

# 18. RACI and Operating Responsibilities
| Activity | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| PoC 1A design and prompt execution | Developer / System Builder Lite Operator | Software Development Lead | Solutions Architecture; Security; QA/SDET; DBA | IT Head; Internal Audit |
| Security policy and OPA/SBAC | Security Architecture / Developer | Security Architecture Lead | Enterprise Architecture; QA/SDET | DevSecOps; Internal Audit |
| Flyway migrations and schema governance | Developer / DBA | DBA Lead | Security; Architecture; QA/SDET | DevSecOps |
| Dynamic Workspace screens | Frontend Developer | Software Development Lead | Security; UX; Architecture | Product Owner |
| CI/CD evidence and GitNexus | DevSecOps | DevSecOps Lead | Developer; QA/SDET; Security | IT Head; Internal Audit |
| Exit review | QA/SDET and Reviewers | Architecture Board / Security Governance | DevSecOps; Product Owner; DBA | Team |

# 19. Non-Negotiable Rejection Rules and Anti-Patterns

Generated code replaces or weakens AUTH_LOGIN_CONTEXT_ESTABLISH.

Generated code creates a parallel login engine or stores/validates passwords inside AIRA.

Frontend directly approves, denies, locks, unlocks, or bypasses step-up.

Controllers contain business rules, policy decisions, direct database writes, direct event publishing, or direct Keycloak Admin calls.

AI approves access, unlocks accounts, modifies policy, or calls model providers directly.

Schema drift appears, including aira_config, aira_workspace, duplicate runtime tables, or manual DDL.

Logs, traces, prompts, screenshots, tests, or evidence expose raw tokens, secrets, PII, passwords, or raw JWTs.

PoC 2 begins before PoC 1 and PoC 1A exit evidence is accepted.

# 20. Review Queue Control Register
| Seq | File Name | Pack | Current Version | Recommended Version | Review Status | Priority | Dependency | Action Required | Next Step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 43D Login PoC1A Code/Parameter/Config Prompt | 13 | v1.1 | v1.2 Revised | Complete | High | 23C, 42C, 43C, 45 PoC2 | Generate revised execution prompt | Review and approve for team execution |
| 2 | 43C PoC1 and PoC1A Traceability Matrix | 12 | v1.0 | v1.1 Revised | Next | High | 43D v1.2, PoC 1, PoC 1A, 42C v1.4 | Align traceability and acceptance criteria | Proceed after 43D |
| 3 | 43 PoC1A Security Intelligence Execution Standard | 12 | v1.0 | v1.1 Revised | Queued | High | 43D, 43C, 42C | Align functional execution standard | Review after 43C |
| 4 | 44 PoC1A Functionality Explanation and Developer Guide | 13 | v1.0 | v1.1 Revised | Queued | Medium | 43D, 43C, 43 PoC1A | Update developer explanation guide | Review after execution standards |

# 21. Change Log
| Version | Date | Change Summary | Owner |
| --- | --- | --- | --- |
| v1.0 | 2026-05-30 | Initial PoC 1A execution prompt standard. | Solutions Architecture Office |
| v1.1 | 2026-06-16 | Corrected canonical schema naming, additive PoC 1A boundary, and System Builder Lite alignment. | Solutions Architecture Office |
| v1.2 Revised | 2026-06-17 | Aligned with revised Dynamic Workspace family, 42C v1.4 roadmap, PoC 2 evidence expectations, DevSecOps, eventing, observability, resilience, and Auto-Heal/Auto-Learn/Auto-Improve controls. | Solutions Architecture Office / IT Head |

# 22. AVCI Compliance Summary
| AVCI Property | Evidence in This Standard |
| --- | --- |
| Attributable | Identifies owner, co-owners, source baseline, supersedence, target audience, review cadence, generated artifact owners, and PR/MR responsibility. |
| Verifiable | Defines tests, scans, contracts, policy results, migration validation, observability signals, GitNexus analysis, Evidence Pack, and exit gates. |
| Classifiable | Requires classification-aware UI, logs, prompts, traces, evidence, model routes, screenshots, test data, and retention handling. |
| Improvable | Defines known limitations, improvement backlog, Auto-Heal/Auto-Learn/Auto-Improve candidate loops, and next document review queue. |

# Appendix A. External Reference Register
| Reference | Use in This Standard |
| --- | --- |
| OpenAPI Specification 3.2.0 | REST contract, generated client, error, security, and test alignment. |
| AsyncAPI Specification 3.1.0 | Event-driven API, Kafka, and asynchronous integration contract alignment. |
| CloudEvents | Common event metadata model for security, workflow, audit, outbox, and evidence events. |
| OpenTelemetry Semantic Conventions | Trace, metric, log, resource, and attribute naming alignment. |
| OWASP ASVS 5.0.0 | Secure API, authentication, authorization, session, input, logging, and testing verification baseline. |
| NIST SSDF and SLSA | Secure software development, provenance, supply-chain, evidence, and pipeline controls. |

