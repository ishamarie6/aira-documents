---
title: "Login PoC1 and PoC1A Integrated Control Pattern Traceability and Acceptance Matrix"
doc_id: "AIRA-43C"
version: "v1.1"
status: "revised"
category: "Continuous improvement, multimodal AI, and PoC1A"
source_docx: "AIRA_43C_Login_PoC1_and_PoC1A_Integrated_Control_Pattern_Traceability_and_Acceptance_Matrix_v1.1_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 43-continuous-improvement-multimodal-poc1a
  - revised
  - aira-43c
---



# Login PoC1 and PoC1A Integrated Control Pattern Traceability and Acceptance Matrix



AIRA
AI-Native Enterprise Platform

Login PoC 1 and PoC 1A Integrated Control Pattern,
Traceability, and Acceptance Matrix

Governed Login Baseline | Security Intelligence | Step-Up Authentication | Human Approval | Evidence Gates

AIRA-DOC-043C | Version v1.1 Revised | INTERNAL CONFIDENTIAL

Status: Draft for Architecture, Security, DevSecOps, DBA, QA/SDET, AI Governance, and CAB Review

Owner: Solutions Architecture Office / IT Head
Effective Date: Upon ARB / CAB approval
Evidence Path: OpenKM Tier-0 / AIRA / Evidence / PoC / Login-Control-Pattern / v1.1

# Document Control
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-043C |
| Document Title | AIRA Login PoC 1 and PoC 1A Integrated Control Pattern, Traceability, and Acceptance Matrix |
| Version | v1.1 Revised |
| Supersedes | 43C-AIRA_Login_PoC1_and_PoC1A_Integrated_Control_Pattern_Traceability_and_Acceptance_Matrix_v1.0.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Architecture Review Board, Security Governance, DevSecOps, DBA, QA/SDET, AI Governance, and CAB Review |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Security Architecture; Software Development Lead; QA/SDET; DevSecOps Lead; DBA; Platform Engineering; AI Governance; SRE / Operations; Internal Audit |
| Primary Audience | Software Developers, AI Coding Agents, Technical Leads, QA/SDET, DevSecOps, Security, DBA, Platform Engineering, Product Owners, Internal Audit |
| Review Cadence | After PoC 1 completion; after PoC 1A completion; before PoC 2 authorization; quarterly; unscheduled on material login, identity, policy, AI, workflow, database, Dynamic Workspace, or DevSecOps change |
| Primary Parents | 42C Foundation PoC Roadmap v1.4; 43D PoC 1A Execution Prompt v1.2; 22B Login MicroFunction Pattern; 23C PoC 1 Execution Prompt; 24 PoC 1 Runtime/DB Standard |
| Companion Standards | 01/01A/01B AVCI and Enterprise Design Principles; 10/10A-10E MicroFunction; 15/15A API; 16/16A/16B Flyway; 17/17A Security; 20 CI/CD Evidence; 31A Observability; 41/42 Dynamic Workspace and Composable Experience; 44A/44C System Builder and Agent Inventory; 45 PoC 2 |

# Change Summary
| Area | v1.1 Revision |
| --- | --- |
| Integrated control pattern | Retained PoC 1 and PoC 1A as a single governed login control pattern and strengthened PoC 2 readiness gates. |
| PoC 1 preservation | Reinforced that AUTH_LOGIN_CONTEXT_ESTABLISH remains the baseline login/session transaction and must not be broken by PoC 1A. |
| PoC 1A additive model | Aligned risk review, failure triage, step-up, account lock/unlock human approval, and AI incident analysis with 43D v1.2. |
| MicroFunction coverage | Added explicit transaction, step, evidence, idempotency, outbox, DLQ/replay, resilience, and observability controls. |
| DevSecOps evidence | Added PoC 2 entry evidence gate, GitNexus, authenticated DAST, SBOM/provenance, secret scan, policy tests, architecture fitness, and PR/MR AVCI evidence. |
| Dynamic Workspace | Aligned security review screens, safe user notifications, AI panel summaries, policy-filtered widgets, accessibility, and telemetry with revised 41, 42, 44-61, and 12A. |
| Runtime telemetry | Added runtime tuning for logging and trace verbosity while preserving mandatory audit, policy-decision, security, and evidence telemetry. |

# Table of Contents Placeholder

Insert or update the Microsoft Word automatic Table of Contents before final publication. Suggested command: References > Table of Contents > Automatic Table, then Update Field.

# 1. Executive Summary and Governance Verdict

This revised matrix formalizes the integrated governance and acceptance baseline for AIRA PoC 1 - Login Authentication, Session Context, and Basic Authorization - and PoC 1A - Login Security Intelligence, Step-Up Authentication, and Human Approval Controls.

Governance Verdict: Conditional Accept with Mandatory Evidence Gates. PoC 1 and PoC 1A may proceed as the reusable AIRA Login Control Pattern, but PoC 2 must not start until the integrated acceptance, regression, security, observability, and evidence gates in this document are satisfied or formally waived through the required governance path.
| Control Area | Verdict | Required Treatment |
| --- | --- | --- |
| PoC 1 login baseline | Accept with verification | Complete AUTH_LOGIN_CONTEXT_ESTABLISH with Keycloak/OIDC, JWT validation, OPA/SBAC, session context, audit, outbox, observability, safe response, and fail-closed evidence. |
| PoC 1A security intelligence | Accept only as additive extension | Add deterministic risk review, failure triage, step-up, lock/unlock approval, and AI incident analysis without replacing or weakening PoC 1. |
| AI incident support | Advisory only | AI may summarize evidence and propose analysis; it must not approve access, unlock accounts, bypass MFA, override OPA, or execute identity actions. |
| Data and policy changes | Governed only | Use Flyway-only database changes, OPA/Rego policy-as-code, OpenAPI/AsyncAPI contract-first APIs, and audited runtime configuration. |
| PoC 2 readiness | Blocked until complete | PoC 2 requires accepted PoC 1/1A evidence pack, regression proof, and closure or formal waiver of Critical/High findings. |

# 2. Purpose, Scope, and Authority

The purpose of this document is to create one execution-control, traceability, and acceptance matrix for PoC 1 and PoC 1A. It prevents PoC 1A from becoming a destructive rewrite, uncontrolled security feature expansion, or isolated demo. It translates AIRA governance into developer, DBA, QA, Security, DevSecOps, AI Governance, and reviewer controls.

## 2.1 In Scope

PoC 1 transaction AUTH_LOGIN_CONTEXT_ESTABLISH and supporting runtime configuration, policy, database, API, frontend, audit, outbox, observability, and evidence artifacts.

PoC 1A additive transactions: AUTH_LOGIN_RISK_REVIEW, AUTH_LOGIN_FAILURE_TRIAGE, AUTH_STEP_UP_REQUIRED, AUTH_ACCOUNT_LOCK_REQUEST, AUTH_ACCOUNT_UNLOCK_REQUEST, and AUTH_LOGIN_INCIDENT_ANALYZE.

Flowable or approved workflow abstraction for human approval, separation of duties, and security review queues.

Dynamic Workspace security review screens, policy-filtered widgets, user-safe notifications, AI incident summary panels, and accessibility evidence.

CI/CD, GitNexus, evidence packs, tests, security scans, OpenAPI/AsyncAPI validation, Flyway validation, OPA/Rego tests, observability proof, and PoC 2 readiness evidence.

## 2.2 Out of Scope

Custom password authentication, password storage, password validation, credential checking, or MFA implementation inside AIRA application code.

AI approval of access, account unlock, MFA bypass, step-up bypass, OPA override, or production-impacting identity action.

Destructive migration of PoC 1 schemas, transaction codes, APIs, runtime configuration, or audit/evidence records without approved defect justification and rollback path.

Frontend authority for authorization, policy, workflow approval, identity action execution, or business decision finalization.

## 2.3 Authority and Precedence
| Level | Authority | Role |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance | Final authority for production-impacting login, identity, workflow, policy, AI, and release readiness decisions. |
| L1 | 01/01A/01B, 10/10A-10E, 15/15A, 16/16A/16B, 17/17A, 20, 31A | Universal AVCI, architecture, MicroFunction, API, database, security, CI/CD, and observability controls. |
| L2 | 42C v1.4 and this 43C v1.1 | PoC sequence, integrated login control pattern, traceability, and PoC 2 readiness gates. |
| L3 | 43D v1.2 and PoC implementation prompts | Execution instructions for code, configuration, policy, tests, documentation, and evidence generation. |
| L4 | PR/MR, CI/CD, runtime evidence, tickets, audit, and dashboard records | Operational proof, review evidence, and improvement inputs. |

# 3. Source Baseline and Canonical Interpretation

This v1.1 revision treats the newer and more complete AIRA alignment as the governing interpretation. Older source references remain historical unless expressly retained. Where documents conflict, the stricter AIRA control governs and the conflict must be recorded as an AVCI reconciliation item.
| Source | Canonical Treatment |
| --- | --- |
| 42C v1.4 Foundation PoC Roadmap | Defines PoC sequence and developer immersion gates. PoC 1 and PoC 1A must complete before PoC 2. |
| 43D v1.2 PoC 1A Execution Prompt | Defines additive, non-destructive PoC 1A generation requirements and evidence expectations. |
| 22B Login MicroFunction Pattern | Defines reusable identity, session, policy, audit, event, and observability controls. |
| 23C PoC 1 Generation Prompt and 24 Runtime/DB Standard | Define PoC 1 baseline transaction, canonical schema names, runtime configuration, and Flyway controls. |
| 41, 42, 44-61, 12A Dynamic Workspace family | Defines backend authority, composable experience, frontend rendering, template lifecycle, security, testing, telemetry, evidence, and accessibility. |
| 44A/44C and 42D-42S | Define System Builder implementation boundaries and canonical AI agent governance path. |

# 4. Integrated Login Control Pattern

The integrated Login Control Pattern is the reusable identity and access foundation for AIRA. It proves that login is not only authentication; it is a governed identity, session, policy, risk, approval, audit, evidence, and observability flow.

## 4.1 Target Flow

Login attempt -> Keycloak or AD authentication -> JWT validation -> session context -> OPA/SBAC authorization -> classification ceiling -> audit/outbox/observability -> risk review where applicable -> step-up or human review where required -> safe response -> evidence and improvement backlog.

## 4.2 Non-Negotiable Architectural Rules
| Rule | Required Behavior | Reject If |
| --- | --- | --- |
| No custom login engine | AIRA delegates credential validation, MFA, account state, and token issuance to Keycloak/AD. | Application code validates passwords, stores password hashes, or builds its own credential checks. |
| Policy-as-code authorization | OPA/SBAC decides access, classification ceiling, step-up, review, block, or denial. | Frontend, controller, or database scripts hardcode authorization decisions. |
| MicroFunction assembly | Login behavior is assembled through governed runtime configuration and standard steps. | Controller or service hardcodes the full transaction sequence. |
| Fail-safe behavior | OPA, Vault, audit, identity, guardrail, or policy failure blocks protected access. | Protected access continues when a required control is unavailable. |
| AI advisory only | AI may summarize evidence or propose incident analysis. | AI approves login, unlocks accounts, bypasses MFA, or overrides policy. |
| Evidence by construction | Every success, failure, risk decision, approval, AI summary, and retry has trace/evidence. | Security-relevant action lacks audit, outbox, trace, owner, or classification. |
| Non-destructive extension | PoC 1A adds capabilities without breaking PoC 1. | PoC 1A deletes, renames, or destabilizes AUTH_LOGIN_CONTEXT_ESTABLISH. |

# 5. PoC 1 Baseline Acceptance Requirements

PoC 1 is the minimum secure login baseline. It must be finished, independently verified, and tagged before PoC 1A is accepted as an extension.
| Requirement | Minimum Control | Evidence Required |
| --- | --- | --- |
| Login initiation | React/Gateway starts OIDC Authorization Code + PKCE flow; rate limiting and security headers apply. | Trace ID, route, rate-limit decision, no credentials logged. |
| Identity authentication | Keycloak/AD validates credentials, MFA, account status, and identity lifecycle. | IdP audit, AD flags, MFA evidence where applicable. |
| Token validation | Spring Security validates issuer, audience, signature, expiry, claims, and replay controls. | JWT validation result; no raw token logging or storage. |
| Session context | AUTH_LOGIN_CONTEXT_ESTABLISH resolves actor, tenant, roles, skills, branch/unit, and classification ceiling. | Runtime definition version, policy result, session context evidence. |
| OPA/SBAC authorization | OPA/Rego decides allow, deny, step-up, review, or classification restrictions. | Policy decision ID, input hash, policy version, test result. |
| Audit and outbox | Login security event, policy decision, and session outcome are recorded append-only and through outbox. | Audit ID, outbox event ID, CloudEvent fields, trace correlation. |
| Dynamic Workspace bootstrap | Policy-filtered workspace bootstrap occurs only after governed session context is resolved. | Resolved workspace code, policy-filtered components, no unauthorized fields. |
| Fail-closed response | Missing identity, OPA, Vault, JWT validation, runtime config, audit, or policy denies protected access safely. | Negative-path tests and safe response evidence. |

# 6. PoC 1A Additive Acceptance Requirements

PoC 1A is accepted only when PoC 1 still works, all PoC 1A capabilities are additive, all new security-intelligence flows are MicroFunction-governed, policy-driven, human-accountable, observable, reversible, test-proven, and AVCI-evidenced.
| Transaction | Required Behavior | Evidence Required |
| --- | --- | --- |
| AUTH_LOGIN_RISK_REVIEW | Deterministically evaluate risk signals and call OPA/SBAC for policy outcome. | Risk input schema, deterministic score, OPA decision, tests, evidence_ref. |
| AUTH_LOGIN_FAILURE_TRIAGE | Classify login/session/access failures into safe categories without leaking sensitive cause details. | Failure category, safe response, audit event, outbox event, DLQ where applicable. |
| AUTH_STEP_UP_REQUIRED | Trigger approved step-up only through Keycloak or approved identity capability. | Step-up request, challenge evidence, no AIRA custom MFA implementation. |
| AUTH_ACCOUNT_LOCK_REQUEST | Route account lock action through workflow and human approval where required. | Flowable instance, SoD proof, approval record, audit/outbox, rollback path. |
| AUTH_ACCOUNT_UNLOCK_REQUEST | Require elevated human approval and separation of duties for unlock actions. | Requester/approver separation, OPA decision, security review evidence. |
| AUTH_LOGIN_INCIDENT_ANALYZE | Generate advisory AI incident summary using approved model route and guardrails. | LiteLLM route, guardrail result, source references, classification, no execution authority. |

# 7. Integrated Traceability Matrix

The traceability matrix below converts PoC 1 and PoC 1A requirements into implementation, test, evidence, and acceptance controls. Critical and High gaps block PoC 2 unless waived by the required authority.
| ID | Requirement | Transaction | Implementation Binding | Tests | Evidence | Gate |
| --- | --- | --- | --- | --- | --- | --- |
| LGN-001 | PoC 1 login flow | AUTH_LOGIN_CONTEXT_ESTABLISH | OpenAPI, Spring Security, Keycloak/OIDC, OPA/SBAC | Unit, integration, contract, Playwright, negative tests | Trace, audit, outbox, policy decision, CI evidence | Blocking |
| LGN-002 | Session context and classification ceiling | AUTH_LOGIN_CONTEXT_ESTABLISH | Runtime config, OPA input, session API | OPA/Rego, schema, API, frontend safe display | Policy version, session context hash, no secrets/PII leakage | Blocking |
| LGN-003 | Risk review | AUTH_LOGIN_RISK_REVIEW | Risk model config, OPA decision, deterministic fixtures | Risk model tests, OPA tests, regression tests | Risk score, risk level, policy decision, evidence_ref | Blocking for PoC 1A |
| LGN-004 | Failure triage | AUTH_LOGIN_FAILURE_TRIAGE | Error taxonomy, safe Problem Details, audit/outbox | Negative tests, DLQ/replay tests, safe response tests | Error code, safe message, audit ID, outbox ID | Blocking for PoC 1A |
| LGN-005 | Step-up | AUTH_STEP_UP_REQUIRED | Keycloak/approved step-up integration, OPA outcome | Step-up branch tests, bypass tests | Challenge evidence, no custom MFA, no bypass | Blocking for high risk |
| LGN-006 | Lock/unlock human approval | AUTH_ACCOUNT_LOCK_REQUEST / UNLOCK_REQUEST | Flowable or approved workflow, OPA/SBAC, SoD | Workflow tests, SoD tests, approval denial tests | Workflow ID, approval record, actor/approver proof | Blocking for account actions |
| LGN-007 | AI incident analysis | AUTH_LOGIN_INCIDENT_ANALYZE | LiteLLM route, guardrails, source references | Guardrail tests, prompt safety tests, output classification tests | Model route, guardrail result, citations, advisory-only statement | Conditional |
| LGN-008 | PoC 2 readiness | All integrated transactions | CI/CD, GitNexus, Evidence Pack, DAST, SBOM, architecture fitness | Full regression, security scan, contract test, resilience lab | Exit checklist, PR/MR AVCI, unresolved Critical/High = 0 or waived | Blocking |

# 8. Policy Outcome Taxonomy and OPA Controls

OPA/SBAC decisions must use explicit, testable outcome taxonomy. Application code must not infer policy outcomes through ad hoc controller logic.
| Outcome | Meaning | Trigger Example | Evidence |
| --- | --- | --- | --- |
| ALLOW | User may proceed with governed session response. | PoC 1 or low-risk PoC 1A path. | Audit, outbox, trace, classification. |
| DENY | Access is blocked with safe error response. | Invalid token, unauthorized skill, classification ceiling breach, suspicious policy denial. | Audit denial, policy decision, safe Problem Details. |
| STEP_UP_REQUIRED | User must complete approved step-up through identity provider or approved mechanism. | Risk score or policy condition requires additional assurance. | Step-up request, OPA decision, no AIRA custom MFA. |
| HUMAN_REVIEW_REQUIRED | Request is routed to Flowable or approved review workflow. | Account lock/unlock, high-risk login, privileged action, ambiguous risk. | Workflow instance, maker-checker, decision proof. |
| QUARANTINE_OR_INVESTIGATE | Security event requires investigation but not autonomous identity action. | Pattern suggests abuse or incident candidate. | Incident candidate, evidence pack, AI advisory summary optional. |

# 9. Database, Flyway, Events, and Evidence Schema Controls

All database changes must be additive, versioned, reviewable, reversible, and delivered through Flyway. PostgreSQL remains the authoritative store. Redis/Valkey, dashboards, and AI summaries are derivative and must never become truth.

Use canonical AIRA schemas such as aira_mf, aira_policy, aira_audit, aira_outbox, aira_ui, aira_cfg, and applicable evidence or AI schemas. Do not create simplified parallel schemas that drift from the current baseline.

Use expand-only migrations for PoC 1A unless an approved defect correction authorizes a breaking change with rollback and compensation plan.

Every event-producing transaction must use transactional outbox with CloudEvents metadata, idempotency key, trace_id, correlation_id, causation_id, classification, and evidence_ref.

Event consumers must be idempotent, schema-version aware, retry-safe, DLQ-capable, and replay-tested.

Evidence tables must support trace reconstruction for login outcome, policy decision, risk score, workflow approval, AI summary, test run, security scan, and CI/CD evidence.

# 10. API, Frontend, and Dynamic Workspace Contract Requirements

APIs and frontend components must be contract-first. The frontend renders and collects user intent; the backend authorizes, policy filters, orchestrates, and executes through MicroFunctions and workflow controls.
| Contract Area | Mandatory Requirement |
| --- | --- |
| OpenAPI | All login/session/risk/approval APIs require versioned OpenAPI contracts, generated clients, safe Problem Details, idempotency profiles, and contract tests. |
| AsyncAPI | Kafka/event contracts require AsyncAPI and CloudEvents bindings for login security events, risk review, approval events, and incident candidates. |
| Frontend boundaries | React/Next.js components must not hardcode authorization, expose raw tokens, store secrets, or call AI/model providers directly. |
| Dynamic Workspace | Security review screens and widgets must be policy-filtered, accessibility-tested, audit-enabled, and backed by approved API/MicroFunction capability binding. |
| AI Assistant Panel | AI incident summary must be advisory, citation-bound, guardrailed, classified, and unable to execute identity actions. |

# 11. Flowable Human Approval Model

Account lock/unlock, privileged risk review, and high-impact identity actions require human approval through Flowable or an approved workflow abstraction. Approval workflows must preserve separation of duties and maker-checker evidence.
| Role | Control Responsibility |
| --- | --- |
| Requester | May submit lock/unlock/security review request but may not approve the same request. |
| Security Reviewer | Reviews evidence, risk, policy outcome, and user/account context. |
| Approver | Approves or rejects according to SBAC, policy, classification, and risk tier. |
| Executor | Executes approved action only through controlled adapter or identity provider integration, never directly from UI or AI. |
| Auditor | Reviews evidence pack, workflow trail, policy decision, trace, and incident record. |

# 12. Testing, Security, Observability, and Evidence Gates
| Gate | Mandatory Evidence |
| --- | --- |
| Build and unit tests | Java 25/Spring backend, React/TypeScript frontend, OPA policy, and MicroFunction step tests must pass. |
| Contract tests | OpenAPI, AsyncAPI, CloudEvents, Avro/JSON Schema, generated client, safe error, and backwards compatibility tests must pass. |
| Security tests | SAST, SCA, secret scan, authenticated DAST, OPA abuse-case tests, token-leakage tests, and safe-response tests must pass. |
| Resilience lab | Duplicate-click, retry, replay, outbox failure, DLQ, workflow timeout, cache loss, and degraded dependency scenarios must be tested. |
| Observability | Log4j2 structured logs, OpenTelemetry traces/metrics/logs, Sentry errors, Loki logs, Tempo traces, Grafana dashboards, and trace reconstruction proof are required. |
| Accessibility and UX | Dynamic Workspace screens must pass keyboard, screen-reader, safe-error, responsive, and user notification tests. |
| Evidence Pack | PR/MR AVCI summary, GitNexus impact, CI evidence, test results, security scan results, SBOM/provenance, rollback plan, and known limitations are required. |

# 13. Runtime Telemetry Toggle Policy

AIRA may allow runtime tuning of debug logging, trace sampling, widget diagnostics, and dashboard verbosity when performance is impacted. However, telemetry toggles must not disable mandatory audit, security decision, OPA/SBAC decision, workflow approval, outbox, evidence_ref, incident, or protected-action traceability. Any temporary reduction must be time-bound, approved, logged, and reversible.

# 14. Concurrency, Heavy Transaction, Idempotency, and Resilience Controls

Every mutating login security transaction must accept or generate an idempotency key and must deduplicate retries, callbacks, browser resubmits, workflow retries, and event replays.

Outbox and inbox records must protect against duplicate event publication and duplicate consumption.

Heavy login-risk analysis must run as backend orchestration or asynchronous workflow, not as long-running frontend authority.

Resilience controls must include timeout, retry limit, circuit breaker, bulkhead, safe fallback, DLQ, replay procedure, and compensation or forward-fix path.

Concurrent lock/unlock or step-up decisions must enforce optimistic locking, workflow state transition validation, and separation-of-duties checks.

# 15. RACI and Operating Responsibilities
| Activity | IT Head / SAO | Dev Lead | Developer | QA/SDET | Security | DevSecOps | DBA / Platform | AI Governance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Approve PoC sequence and priority | A/R | C | I | C | C | C | C | C |
| Define acceptance criteria | A/R | R | C | C | C | C | C | C |
| Implement code/config/policies | C | A | R | C | C | C | C | I |
| Execute tests and evidence capture | C | A | R | R | C | C | C | C |
| Review security and access controls | A | C | C | C | R | C | C | C |
| Generate CI/CD and GitNexus evidence | C | C | R | C | C | A/R | C | C |
| Review Flyway/database changes | C | C | C | C | C | C | A/R | I |
| Review AI-assisted outputs and guardrails | A | C | C | C | C | C | I | R |
| Accept PoC exit review | A/R | R | C | R | R | R | C | C |

# 16. Risks, Controls, and Non-Conformance Handling
| Risk | Why It Matters | Control |
| --- | --- | --- |
| PoC 1A breaks PoC 1 | Future modules inherit unstable login/session behavior. | Feature flags, regression guard, expand-only migration, safe disablement, PoC 1 tests must pass. |
| AI overreach | AI could appear to approve access or unlock accounts. | AI advisory-only banner, OPA/SBAC block, tool denial, human approval path, guardrail tests. |
| Policy bypass in frontend | User may access unauthorized widgets or actions. | Backend policy filtering, generated clients only, contract tests, OPA tests, DAST. |
| Evidence gaps | Cannot prove security, audit, or readiness. | Evidence Pack required; missing Critical/High evidence blocks PoC 2. |
| Duplicate/replay effects | Retries may duplicate account actions or incident records. | Idempotency keys, outbox/inbox, workflow state validation, replay tests. |
| Secrets or token leakage | Security incident and audit failure. | Secret scan, redaction tests, no token UI/log/storage, Sentry/Loki filtering, safe screenshots. |

# 17. Implementation Sequence and PoC 2 Readiness Gate

Confirm PoC 1 baseline tag, branch, commit, tests, contracts, evidence pack, and known limitations.

Inspect PoC 1 implementation and confirm AUTH_LOGIN_CONTEXT_ESTABLISH, audit/outbox, OPA/SBAC, runtime configuration, and Dynamic Workspace bootstrap are preserved.

Apply PoC 1A additive Flyway migrations, runtime configuration, feature flags, policies, API contracts, and tests.

Implement PoC 1A MicroFunction transactions behind ports/adapters and approved workflow/action boundaries.

Execute full regression, security, contract, workflow, accessibility, observability, resilience, and evidence gates.

Package GitNexus, derived artifacts, CI/CD evidence, test evidence, security evidence, rollback plan, and PR/MR AVCI summary.

Hold integrated PoC 1/1A exit review. PoC 2 may start only when Critical findings are closed and High findings are closed or formally waived with compensating controls.
| Readiness Item | Pass Condition | PoC 2 Gate |
| --- | --- | --- |
| PoC 1 baseline verified | All PoC 1 tests pass; login/session/API/audit/outbox/OPA evidence complete. | Required |
| PoC 1A additive proof | PoC 1 works with PoC 1A flags disabled; no destructive schema/API/runtime drift. | Required |
| Integrated security evidence | SAST/SCA/secret scan/authenticated DAST/OPA abuse-case tests complete. | Required |
| Observability proof | Trace reconstruction for success, deny, step-up, approval, failure triage, and AI summary paths. | Required |
| Evidence Pack closure | GitNexus, CI/CD, tests, scans, SBOM/provenance, rollback, known limitations, and AVCI summary complete. | Required |
| Governance sign-off | Owner, checker, Security, QA/SDET, DevSecOps, DBA where applicable, and IT Head/SAO approval recorded. | Required |

# 18. Review Queue Control Register
| Seq | File Name | Pack | Current Version | Recommended Version | Review Status | Priority | Dependency | Action Required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | AIRA_43C_Login_PoC1_and_PoC1A_Integrated_Control_Pattern_Traceability_and_Acceptance_Matrix_v1.1_Revised | Pack 12 | v1.0 | v1.1 | Completed - ready for review | High | 42C v1.4; 43D v1.2; 22B; 23C; 24 | Publish for team review after owner approval |
| 2 | AIRA_44_PoC1A_Login_Security_Intelligence_Functionality_Explanation_and_Developer_Guide_v1.1_Revised | Pack 13 | v1.0 | v1.1 | Next recommended | High | 43C v1.1; 43D v1.2; 42C v1.4 | Revise developer-facing explanation and functionality guide |
| 3 | AIRA_43_PoC1A_Login_Security_Intelligence_StepUp_Human_Approval_Execution_Standard_v1.1_Revised | Pack 12 | v1.0 | v1.1 | Queued | High | 43C and 43D | Align execution standard with integrated acceptance matrix |
| 4 | AIRA_41_PoC1_Login_Execution_Instruction_and_Evidence_Governance_Standard_v1.1_Revised | Pack 10 | v1.0 | v1.1 | Queued | Medium | 43C; 42C; PoC 2 | Back-port evidence and readiness improvements to PoC 1 execution instruction |
| 5 | Register and Master Cross-Reference Update | Register | TBD | TBD | Later | Medium | All revised documents | Update filenames, supersedence, dependencies, numbering conflicts, and review status |

# 19. AVCI Compliance Summary
| AVCI Property | Evidence in This Standard |
| --- | --- |
| Attributable | Defines document owner, PoC ownership, transaction ownership, RACI, evidence responsibilities, PR/MR ownership, and review roles. |
| Verifiable | Defines deterministic tests, OPA/Rego tests, workflow tests, AI guardrail tests, security scans, contract tests, GitNexus impact, observability proof, and PoC 2 readiness gates. |
| Classifiable | Requires classification for login risk data, failure triage, account actions, AI summaries, prompts, logs, telemetry, evidence records, dashboards, and retention. |
| Improvable | Requires known limitations, improvement backlog, post-PoC feedback, Auto-Heal/Auto-Learn/Auto-Improve candidate loops, and future standard updates. |

# 20. Appendix A. Minimum PR/MR AVCI Evidence Template

The PR/MR must include owner, developer, reviewer/checker, ticket/task, branch, commit, AI tools used, PoC 1 baseline reference, PoC 1 regression proof, risk review tests, failure triage tests, OPA/SBAC policy tests, step-up tests, Flowable approval tests, AI incident analysis tests, contract tests, Playwright tests, SAST/DAST/secret scan, GitNexus report, derived artifact evidence, classification, secrets handling, rollback plan, and known limitations.

