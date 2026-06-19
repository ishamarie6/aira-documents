---
title: "Login and Session Establishment MicroFunction Design Pattern"
doc_id: "AIRA-22B"
version: "v1.2"
status: "revised"
category: "Prompt guardrails and login patterns"
source_docx: "AIRA_22B_Login_and_Session_Establishment_MicroFunction_Design_Pattern_v1.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 22-prompt-guardrails-login-patterns
  - revised
  - aira-22b
---



# Login and Session Establishment MicroFunction Design Pattern



AIRA

AI-Native Enterprise Platform

Login and Session Establishment MicroFunction Design Pattern

AIRA-DOC-022B | v1.2 Revised

Identity Assembly | Session Context | OIDC/Keycloak | OPA/SBAC | Audit, Outbox, Observability | AVCI Always
| Document ID | AIRA-DOC-022B |
| --- | --- |
| Canonical Filename | AIRA_22B_Login_and_Session_Establishment_MicroFunction_Design_Pattern_v1.2_Revised.docx |
| Version | v1.2 Revised |
| Supersedes | 22B-AIRA_Login_and_Session_Establishment_MicroFunction_Design_Pattern_v1.1_Aligned.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Architecture, Security, DBA, DevSecOps, QA/SDET, Platform, SRE, and Team Execution Review |
| Owner | Solutions Architecture Office / Security Architecture / IT Head |
| Co-Owners | Enterprise Architecture; Software Development Lead; DevSecOps Lead; QA/SDET; DBA; Platform Engineering; SRE / Operations; AI Governance; Internal Audit |
| Primary Audience | Solutions Architects; Developers; Security; DBAs; QA/SDET; DevSecOps; System Builder operators; approved AI coding agents; Internal Audit |
| Effective Date | Upon ARB / Security Governance / CAB approval where required |
| Primary Companions | 23C PoC 1 Generation Prompt; 24 PoC 1 Runtime Configuration and Database Schema Standard; 41 PoC 1 Execution Instruction; 43/43C/43D/44 PoC 1A controls; 42C Roadmap; 45 PoC2 DevSecOps/System Factory; 48/49/51/53 Dynamic Workspace standards |
| Mandatory Login Design Rule AIRA shall not implement a custom password validation, password storage, account lockout, password policy, MFA, token issuance, or authentication engine inside application code. Login is a governed identity and session-context establishment transaction assembled from reusable MicroFunctions. Authentication is delegated to Keycloak federated with Active Directory; authorization is evaluated through RBAC, ABAC, SBAC, and OPA; secrets are governed through Vault-compatible controls; and every success, failure, denial, exception, outbox event, policy decision, and audit record must be attributable, verifiable, classifiable, and improvable. |
| --- |

Table of Contents

This document uses Microsoft Word heading styles. Insert or update an automatic Word Table of Contents before controlled publication.
| Section | Title |
| --- | --- |
| 1 | Executive Summary and v1.2 Alignment Verdict |
| 2 | Purpose, Scope, and Authority |
| 3 | Non-Negotiable Design Principles |
| 4 | Reference Architecture and Runtime Transaction |
| 5 | Canonical AUTH_LOGIN_CONTEXT_ESTABLISH Step Sequence |
| 6 | Security, Policy, Session, Token, and Classification Rules |
| 7 | Audit, Eventing, Outbox, Observability, and Evidence |
| 8 | PoC 1 / PoC 1A Boundary and Dynamic Workspace Bootstrap |
| 9 | DevSecOps, Testing, GitNexus, and Architecture Fitness Gates |
| 10 | Resilience Lab, Runtime Telemetry Toggles, and Improvement Loops |
| 11 | Acceptance Criteria, RACI, Review Queue, and AVCI Summary |

# 1. Executive Summary and v1.2 Alignment Verdict

This v1.2 revision updates the Login and Session Establishment MicroFunction Design Pattern as the parent design authority for PoC 1 login/session establishment. It aligns the conceptual pattern with the revised PoC 1 execution instruction, 23C generation prompt, Document 24 runtime and database schema standard, PoC 1A preservation controls, PoC 2 entry evidence, and the revised Dynamic Workspace and System Builder controls.

The design position remains intentionally strict: AIRA does not build its own authentication engine. The platform delegates authentication to enterprise identity services and uses application code only to establish a governed session context after identity, token, policy, classification, idempotency, audit, outbox, and observability controls have passed.
| Alignment Area | v1.2 Decision | Required Treatment |
| --- | --- | --- |
| Login design authority | Retain and strengthen | 22B remains the reusable Login MicroFunction design pattern and parent authority for AUTH_LOGIN_CONTEXT_ESTABLISH. 23C generates; Document 24 persists runtime/schema; 41 governs execution evidence. |
| Custom authentication | Prohibited | No password storage, comparison, password policy, lockout engine, MFA engine, token issuance engine, or direct credential handling inside AIRA application code. |
| Canonical schemas | Enforced | Use aira_mf, aira_cfg, aira_auth, aira_policy, aira_audit, aira_outbox, and aira_ui. Do not generate aira_config or aira_workspace. |
| PoC 1A boundary | Explicit | PoC 1 may include extension hooks only. Risk review, step-up, lock/unlock, failure triage, and AI incident analysis remain additive PoC 1A capabilities. |
| Evidence by construction | Strengthened | Each login success, failure, denial, error, audit step, outbox message, OPA decision, trace, and dashboard record must be reconstructable and evidence-linked. |
| Industry alignment | Updated | API/event contracts, security verification, and telemetry semantics align with current OpenAPI, AsyncAPI, OWASP ASVS, and OpenTelemetry guidance. |

# 2. Purpose, Scope, and Authority

## 2.1 Purpose

Define the formal AIRA login design pattern using approved identity, security, session, audit, eventing, and observability components.

Define the reusable MicroFunction catalog and canonical transaction behavior for AUTH_LOGIN_CONTEXT_ESTABLISH.

Prevent custom authentication, unsafe token handling, scattered authorization logic, duplicated audit code, schema drift, and inconsistent login telemetry.

Establish the mandatory configuration, testing, evidence, and review gates required before login can be promoted beyond development.

## 2.2 Scope
| In Scope | Out of Scope |
| --- | --- |
| Keycloak/OIDC Authorization Code + PKCE integration through approved Spring Security and identity adapter patterns. | Custom password validation, password storage, password reset, credential checking, or token issuance inside AIRA. |
| Runtime-assembled MicroFunction transaction for session context, classification ceiling, OPA/SBAC decision, audit, outbox, and Dynamic Workspace bootstrap. | Frontend authorization authority, token storage in localStorage, direct Keycloak Admin calls from controllers, or client-side policy authority. |
| Canonical database schema guidance, Flyway-governed seed configuration, OPA/Rego tests, API/event contracts, and evidence records. | Account lock/unlock, step-up authentication, risk review, failure triage, or AI incident analysis inside PoC 1. |
| Observability, resilience, rollback/forward-fix, DevSecOps gates, GitNexus impact evidence, and PoC 1A/PoC 2 readiness hooks. | Direct model-provider SDK calls, production mutation, manual production DDL, or AI approval of access/security exceptions. |

## 2.3 Authority and Precedence
| Level | Authority | Role |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance | Final authority for production-impacting identity, session, policy, database, security, and release decisions. |
| L1 | AVCI, 01A, Engineering Blueprint, MicroFunction Framework, Security, Database/Flyway, API, DevSecOps, Observability standards | Universal evidence, architecture, security, migration, contract, observability, and promotion discipline. |
| L2 | This 22B Design Pattern | Parent authority for the login/session-establishment MicroFunction design pattern and canonical login transaction intent. |
| L2 | 23C and Document 24 | 23C controls code/config generation. Document 24 controls runtime configuration and database schema implementation. |
| L3 | Generated PR/MR, migrations, tests, policies, API/event contracts, dashboards, evidence pack | Candidate implementation evidence; not approved until reviewed and verified. |

# 3. Non-Negotiable Design Principles
| Principle | Login Pattern Requirement |
| --- | --- |
| SOLID / Clean Architecture | Controllers remain thin adapters. Identity provider, OPA, Vault, audit, outbox, database, messaging, and observability are accessed through ports/adapters. |
| DDD / Bounded Context | Identity-and-access owns login/session intent; policy, audit, outbox, UI, and evidence domains retain separate schema and ownership boundaries. |
| Configure first | Reuse standard MicroFunction steps and runtime configuration before coding new business logic. |
| Fail-safe, not fail-open | If identity, JWT validation, OPA/SBAC, Vault, audit, outbox, runtime config, or classification checks fail, protected access is denied safely. |
| Idempotency by design | Callbacks, retries, duplicate clicks, refreshes, and outbox publication use idempotency keys and duplicate-safe processing. |
| Observability by design | Every critical path emits trace_id, request_id, user hash, classification, policy version, step result, error code, and evidence_ref without leaking secrets or raw PII. |
| Reversibility | Runtime activation, policy versions, seed data, frontend bootstraps, and feature flags support rollback, forward-fix, or safe disablement. |
| AVCI | Every artifact, decision, migration, policy, test, telemetry signal, and improvement candidate is attributable, verifiable, classifiable, and improvable. |
| Rejection Rule Reject any generated login implementation that stores credentials, creates a custom password/MFA/token engine, hardcodes roles in controllers, bypasses OPA/SBAC, stores tokens in browser localStorage, writes audit or outbox records directly from controllers, removes telemetry/evidence, or mixes PoC 1A security-intelligence behavior into PoC 1. |
| --- |

# 4. Reference Architecture and Runtime Transaction

The login pattern is implemented as a governed transaction that starts from an HTTP/OIDC callback or approved session-establishment trigger and ends only after session context, classification ceiling, policy outcome, audit evidence, outbox event, observability correlation, and Dynamic Workspace bootstrap eligibility have been established.
| Layer | Responsibility | Boundary Rule |
| --- | --- | --- |
| Frontend / Next.js / React | Initiates login redirect, displays safe session state, requests workspace bootstrap through approved APIs. | No password collection, no frontend authorization authority, no raw token persistence, no direct policy decisions. |
| API / Gateway / Controller | Receives callback/session requests, correlates request, invokes backend use case. | Thin adapter only; no business or security decision ownership. |
| Application / Use Case | Coordinates AUTH_LOGIN_CONTEXT_ESTABLISH through MicroFunction runtime. | Depends on ports, not frameworks or provider SDKs. |
| MicroFunction Runtime | Executes configured step sequence, policies, retries, audit, evidence, and outbox. | Runtime assembly is configuration-governed and evidence-producing. |
| Identity / Policy / Secrets Adapters | Keycloak/OIDC, Spring Security JWT validation, OPA/SBAC, Vault-compatible secret references. | External systems accessed through explicit ports/adapters. |
| Database / Event / Evidence | PostgreSQL/Flyway authority, outbox event, audit/evidence records, Dynamic Workspace seed. | No manual DDL; Redis/Valkey and dashboards are derivative only. |
| Runtime Transaction Definition transaction_code: AUTH_LOGIN_CONTEXT_ESTABLISH \| bounded_context: identity-and-access \| classification: CONFIDENTIAL \| idempotency_profile: login-callback-replay-guard-v1 \| error_policy: fail-closed-auth-v1 \| observability_profile: auth-login-otel-v1 \| audit_profile: auth-login-audit-v1 \| rollback_strategy: revert-runtime-definition-and-opa-policy-version |
| --- |

# 5. Canonical AUTH_LOGIN_CONTEXT_ESTABLISH Step Sequence

This pattern controls the canonical 20-step sequence that 23C and Document 24 must generate, seed, test, and evidence. Step names may be implemented through configured rows and reusable catalog functions, but step intent and control coverage must not be removed.
| Order | Step Code | Required Intent |
| --- | --- | --- |
| 1 | STP-RCV-AUTH-REQUEST | Receive approved login/callback/session request through thin adapter. |
| 2 | STP-COR-TRACE | Create or propagate trace_id, request_id, correlation_id, causation_id. |
| 3 | STP-RATE-LOGIN | Apply login, callback, tenant, user, and channel rate limits. |
| 4 | STP-SEC-CSRF-CORS | Validate CSRF/CORS/session initiation controls where applicable. |
| 5 | STP-AUTH-REDIRECT | Redirect to Keycloak/OIDC login path when unauthenticated. |
| 6 | STP-AUTH-CALLBACK | Receive OIDC authorization-code callback through approved adapter. |
| 7 | STP-AUTH-TOKEN-EXCHANGE | Exchange authorization code through Spring Security/OIDC adapter; never expose raw tokens. |
| 8 | STP-VAL-JWT | Validate token signature, issuer, audience, expiry, nonce, and required claims. |
| 9 | STP-RES-ACTOR | Resolve user/service/agent, tenant, branch/unit, channel, and synthetic/test state. |
| 10 | STP-CLS-CONTEXT | Determine data classification ceiling and handling restrictions. |
| 11 | STP-SEC-OPA-SBAC | Evaluate RBAC/ABAC/SBAC using OPA/Rego or approved policy abstraction. |
| 12 | STP-IDEMP-CHECK | Apply callback replay guard and duplicate-safe idempotency behavior. |
| 13 | STP-SES-BUILD | Build governed session context; do not store sensitive raw tokens. |
| 14 | STP-AUDIT-ACCESS | Write append-only access decision and step evidence. |
| 15 | STP-OUTBOX-LOGIN-EVENT | Create transactional security event outbox record using CloudEvents-compatible metadata. |
| 16 | STP-UI-BOOTSTRAP | Resolve policy-filtered Dynamic Workspace bootstrap eligibility and safe response. |
| 17 | STP-OBS-EMIT | Emit logs, metrics, traces, audit references, error-monitoring, and evidence references. |
| 18 | STP-SAFE-RESPONSE | Return safe response without secrets, raw JWTs, passwords, raw PII, or policy internals. |
| 19 | STP-ERR-FAIL-CLOSED | On failure, deny protected access and emit safe denial/evidence records. |
| 20 | STP-EVD-CLOSE | Close transaction with evidence_ref, policy_version, config_version, and improvement hooks. |

# 6. Security, Policy, Session, Token, and Classification Rules
| Control Domain | Mandatory Rule | Evidence Required |
| --- | --- | --- |
| Identity | Use Keycloak/OIDC through approved Spring Security and identity adapter patterns. | Provider config reference, issuer/audience validation proof, callback test, safe redirect proof. |
| Token handling | No raw JWT, refresh token, ID token, password, or secret in UI, logs, traces, screenshots, tests, prompts, or docs. | Secret scan, log redaction test, browser storage test, negative evidence query. |
| Authorization | Use OPA/Rego with RBAC/ABAC/SBAC input; no hardcoded authorization logic in controllers or frontend. | OPA test results, policy version, decision_id, deny/default-deny test. |
| Classification | Determine classification ceiling before workspace bootstrap or capability exposure. | classification field in audit/evidence, route eligibility check, redaction proof. |
| Session context | Build only safe session context; session state must not become authorization authority. | Session fixture tests, API response contract, safe-response review. |
| Secrets | Use Vault-compatible abstraction. No secrets in source, .env committed files, logs, docs, screenshots, prompts, or tests. | Secret scan, Vault adapter test, local synthetic secret proof. |

# 7. Audit, Eventing, Outbox, Observability, and Evidence

Audit, outbox, eventing, and observability are not optional cross-cutting concerns. They are mandatory step outputs that prove AVCI and allow incident reconstruction, policy review, and PoC 2 readiness.
| Signal / Record | Minimum Required Fields | Handling Rule |
| --- | --- | --- |
| Audit event | actor_hash, tenant, transaction_code, step_code, policy_ref, decision, classification, evidence_ref, timestamp | Append-only. No raw token, secret, password, or raw PII. |
| Outbox event | event_id, aggregate_id, event_type, CloudEvents metadata, idempotency_key, trace_id, schema_version, payload_ref | Transactional outbox only; replay-safe and schema-versioned. |
| Trace | trace_id, span_id, service.name, route, dependency, policy decision span, MicroFunction step span | Use OpenTelemetry conventions and classification-safe attributes. |
| Logs | structured event, severity, error_code, safe message, trace_id, evidence_ref | Log4j2 structured logging; no secrets or high-cardinality PII labels. |
| Metrics | latency, success/deny/failure counts, policy-deny rate, outbox lag, DLQ count, cache hit/miss where applicable | Grafana dashboards and alerts; labels bounded and safe. |
| Error monitoring | exception fingerprint, safe stack metadata, release, environment, trace_id | Sentry or approved error-monitoring path with redaction. |
| Evidence pack | PR/MR, commit, CI run, tests, scans, OPA results, Flyway validation, GitNexus report, dashboard proof, rollback plan | Stored in approved evidence path and linked to tickets/ADRs as applicable. |

# 8. PoC 1 / PoC 1A Boundary and Dynamic Workspace Bootstrap
| PoC Boundary Rule PoC 1 establishes login, session context, basic authorization, audit, outbox, observability, and Dynamic Workspace bootstrap. PoC 1A adds risk review, failure triage, step-up, lock/unlock human approval, and AI-assisted incident analysis. PoC 1 must reserve extension hooks only and must not implement PoC 1A behavior prematurely. |
| --- |
| Capability | PoC 1 Treatment | PoC 1A Treatment |
| --- | --- | --- |
| AUTH_LOGIN_CONTEXT_ESTABLISH | Canonical baseline transaction. Must pass tests before any extension. | Must be preserved and reused; not replaced. |
| Risk review | May emit extension-ready evidence and safe signals only. | Add AUTH_LOGIN_RISK_REVIEW transaction and deterministic risk policy. |
| Failure triage | Basic fail-closed error handling and safe response. | Add AUTH_LOGIN_FAILURE_TRIAGE and support incident classification. |
| Step-up | No custom MFA or bypass logic in AIRA. | Add policy-based step-up decisioning through approved identity/workflow patterns. |
| Lock/unlock | No direct account lock/unlock implementation. | Human approval, SoD, Flowable/workflow, and privileged policy controls. |
| AI advisory | No incident analysis in PoC 1. | Advisory only through approved gateway/guardrails; no authority to approve access. |
| Dynamic Workspace | Backend-governed, policy-filtered aira_ui bootstrap after session context. | Add security-review screens and approval queues as policy-filtered widgets. |

# 9. DevSecOps, Testing, GitNexus, and Architecture Fitness Gates
| Gate | Required Checks | Blocking Criteria |
| --- | --- | --- |
| Build and unit tests | Java 25/Spring backend, React/TypeScript frontend, deterministic fixtures. | Compile or unit failures; waiver required for non-blocking known limits. |
| Contract tests | OpenAPI response, safe Problem Details, generated client compatibility, AsyncAPI/CloudEvents schema checks. | Contract drift or undocumented endpoint/event changes. |
| Policy tests | OPA/Rego allow, deny, default-deny, missing skill, expired session, classification ceiling. | Any fail-open outcome or missing default deny. |
| Flyway and data tests | Clean migrate, checksum validation, seed validation, rollback/forward-fix plan, RLS/classification checks where applicable. | Manual DDL, checksum drift, unapproved schema, missing canonical schema. |
| Security scans | SAST, SCA, secret scan, dependency/license scan, authenticated DAST where applicable. | Critical/High findings without approved waiver and remediation evidence. |
| Architecture fitness | No direct DB/domain leakage, no direct provider SDK from domain/controller, no frontend authority, no hardcoded roles. | Boundary violation or bypass of MicroFunction runtime/policy controls. |
| GitNexus | Read-only impact analysis, affected tests, sensitive code map, architecture drift summary. | GitNexus used as authority, write path, or replacement for tests/scans/review. |
| Evidence pack | AVCI summary, CI run, tests, scans, OPA/Flyway results, trace/audit proof, rollback/feature-disable proof. | Missing owner, source, classification, verification evidence, or improvement path. |

# 10. Resilience Lab, Runtime Telemetry Toggles, and Improvement Loops

The Login pattern must be tested under failure, replay, retry, and degraded-observability scenarios before being treated as a reusable foundation. Runtime toggles may adjust debug verbosity, sampling, or dashboard detail, but must never disable mandatory audit, security, policy, outbox, evidence, or protected-action telemetry.
| Scenario | Required Behavior | Evidence |
| --- | --- | --- |
| Keycloak unavailable | Protected access denied safely; no local credential fallback. | Fail-closed test, safe user notice, trace and audit evidence. |
| OPA unavailable | Deny protected access or require approved emergency path; no implicit allow. | Default-deny OPA test and policy error evidence. |
| Duplicate callback / retry | Idempotency prevents duplicate session effects and duplicate outbox business meaning. | Replay test, idempotency key evidence, outbox dedupe result. |
| Outbox failure | Transaction does not silently lose event; retry/DLQ/replay path is visible. | Outbox lag/DLQ metric, replay runbook evidence. |
| Telemetry sink degradation | Core audit/evidence continues; optional debug sampling may reduce load. | Toggle record, evidence reference, dashboard alert. |
| High-load login burst | Rate limits, circuit breakers, bulkheads, and safe errors protect identity and policy dependencies. | Load test, SLO metrics, Resilience Lab report. |
| Auto-Heal / Auto-Learn / Auto-Improve | May create candidate fix/learning proposals only. No silent mutation of code, policy, config, prompts, model routes, or production. | Ticket, RCA, GitNexus impact, tests, PR/MR, human approval, rollback plan. |

# 11. Acceptance Criteria, RACI, Review Queue, and AVCI Summary

## 11.1 Acceptance Criteria

Login delegates authentication to Keycloak/OIDC and does not implement custom password, token, MFA, or credential handling.

AUTH_LOGIN_CONTEXT_ESTABLISH is represented through canonical runtime configuration and tested as a MicroFunction-backed transaction.

Canonical schemas and step sequence are used; no aira_config, aira_workspace, simplified steps, or alternate transaction codes are introduced.

OPA/SBAC decisions, classification ceiling, audit evidence, outbox event, trace correlation, and Dynamic Workspace bootstrap are produced.

PoC 1A extension hooks are visible but risk review, step-up, lock/unlock, failure triage, and AI incident analysis are not implemented in PoC 1.

CI/CD, GitNexus, tests, security scans, policy checks, Flyway validation, observability evidence, and rollback/forward-fix proof are attached to the PR/MR.

## 11.2 RACI
| Activity | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Pattern ownership | Security Architecture; Solutions Architecture | IT Head / Architecture Board | DevSecOps; DBA; QA/SDET; Platform | Software Development Team |
| Implementation | Software Development Lead; Developers | Development Lead | Security; DBA; QA/SDET | Product Owner; Internal Audit |
| Policy and access review | Security Architecture | Security Governance | AI Governance; Internal Audit | Development Team |
| Flyway/data review | DBA; DevSecOps | Data Governance / CAB where required | Security; Developers | SRE / Operations |
| Evidence and acceptance | QA/SDET; DevSecOps | ARB/CAB or delegated approver | GitNexus reviewer; Security; Audit | Stakeholders |

## 11.3 Review Queue
| Priority | Next File | Reason |
| --- | --- | --- |
| 1 | AIRA_40_Login_MicroFunction_Design_Pattern_Working_Reference_v1.2_Revised or archive/consolidation note | Document 40 is a legacy/working reference. It should be reviewed for merge, supersedence, or archival now that 22B is revised. |
| 2 | AIRA_23A_Login_PoC1_Developer_Source_Code_Generation_Standard_v1.3_Revised | Developer prompt standard should align with revised 22B, 23C, 24, and PoC 1/1A/2 readiness gates. |
| 3 | AIRA_38_Login_Function_Prompt_Standard_v1.2_Revised | Earlier login prompt should be checked for schema, step, security, Dynamic Workspace, and evidence drift. |
| 4 | Register / Master Cross-Reference Update | Capture 22B v1.2 revised filename, supersedence, duplicate-numbering notes, and Document 40 disposition. |

## 11.4 AVCI Compliance Summary
| AVCI Property | Evidence in This Revision |
| --- | --- |
| Attributable | Document ID, owner, co-owners, source baseline, companion documents, RACI, review queue, and runtime transaction ownership are explicit. |
| Verifiable | Canonical steps, schemas, tests, OPA decisions, Flyway validation, CI/CD gates, GitNexus evidence, observability, and acceptance criteria are defined. |
| Classifiable | Document is INTERNAL CONFIDENTIAL and requires classification-safe session context, telemetry, logs, evidence, and Dynamic Workspace bootstrap. |
| Improvable | PoC 1A boundary, Auto-Heal/Auto-Learn/Auto-Improve candidate rules, review queue, and register update path are captured. |
| External Source Register Used for Current Alignment OpenAPI Specification 3.2.0; AsyncAPI Specification 3.1.0; OpenTelemetry Semantic Conventions; OWASP Application Security Verification Standard. These references support API contract, event contract, telemetry, and security-verification alignment. AIRA source standards remain the primary authority for AIRA-specific governance. |
| --- |

