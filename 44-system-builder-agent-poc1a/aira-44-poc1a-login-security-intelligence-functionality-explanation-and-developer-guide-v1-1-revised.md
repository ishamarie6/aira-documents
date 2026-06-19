---
title: "PoC1A Login Security Intelligence Functionality Explanation and Developer Guide"
doc_id: "AIRA-44"
version: "v1.1"
status: "revised"
category: "System builder, AI agents, and PoC1A"
source_docx: "AIRA_44_PoC1A_Login_Security_Intelligence_Functionality_Explanation_and_Developer_Guide_v1.1_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 44-system-builder-agent-poc1a
  - revised
  - aira-44
---



# PoC1A Login Security Intelligence Functionality Explanation and Developer Guide



AIRA
AI-Native Enterprise Platform

AIRA PoC 1A Login Security Intelligence Functionality Explanation and Developer Guide

Developer-Ready Functional Explanation | Additive MicroFunction Design | Step-Up | Human Approval | AI Advisory | Evidence Gates
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-044-PoC1A-DEV-GUIDE (provisional qualified identifier pending master register cleanup) |
| Recommended Version | v1.1 Revised |
| Status | Draft for Architecture, Security, DevSecOps, QA/SDET, DBA, Platform Engineering, and Software Development Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Security Architecture; Software Development Lead; DevSecOps Lead; QA/SDET; DBA; Platform Engineering; AI Governance; Internal Audit |
| Primary Audience | Software Developers, Technical Leads, QA/SDET, DevSecOps, Security Administrators, DBA, Platform Engineers, AI Engineers |
| Source Reviewed | 44-AIRA_PoC1A_Login_Security_Intelligence_Functionality_Explanation_and_Developer_Guide_v1.0.docx and .md |
| Supersedes | AIRA-DOC-044 PoC 1A Login Security Intelligence Functionality Explanation and Developer Guide v1.0 |
| Primary Companions | 43 PoC 1A Execution Standard; 43C Integrated Control Matrix; 43D PoC 1A Generation Prompt; 42C Roadmap; 41 PoC 1 Login Evidence Standard |
| Effective Date | Upon ARB / Security / DevSecOps Governance approval |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / PoC / Login-PoC1A / Developer-Guide / v1.1/ |
| Mandatory Practice Statement PoC 1A explains and implements login security intelligence as an additive extension to PoC 1. It must preserve AUTH_LOGIN_CONTEXT_ESTABLISH, the Keycloak/OIDC identity boundary, OPA/SBAC authorization, audit/outbox evidence, observability, safe responses, Dynamic Workspace bootstrap, and all PoC 1 regression tests. PoC 1A may add risk review, failure triage, step-up, lock/unlock human approval, and AI-assisted incident analysis only through governed MicroFunction transactions, additive Flyway migrations, approved API/event contracts, policy-as-code, feature flags, tests, security evidence, rollback/safe-disable controls, and AVCI evidence. |
| --- |

# Table of Contents

Use Microsoft Word References > Table of Contents > Automatic Table, then Update Field before final publication. This placeholder is intentionally static for deterministic rendering during review.

# 1. Executive Review Summary

This v1.1 revision converts the original developer explanation guide into an implementation-ready, evidence-driven AIRA document. The original intent is retained: help developers understand PoC 1A capabilities and implement them as additive MicroFunction building blocks without destabilizing the PoC 1 login baseline.

The major correction is governance alignment. Document 44 is not a standalone security architecture authority and must not compete with 43, 43C, 43D, 42C, 22B, 23C, 24, or the revised Dynamic Workspace standards. This document is a developer explanation and implementation understanding guide. It explains what the functions mean, where they fit, and how developers should think about the behavior before coding or generating artifacts.
| Outcome | Required Treatment in v1.1 |
| --- | --- |
| Preserve PoC 1 | AUTH_LOGIN_CONTEXT_ESTABLISH, Keycloak/OIDC, OPA/SBAC, audit/outbox, observability, safe responses, tests, and Dynamic Workspace bootstrap remain intact. |
| Explain PoC 1A clearly | Developers receive functional meaning, transaction ownership, UI behavior, workflow behavior, evidence expectations, and anti-patterns. |
| Strengthen implementation alignment | Capabilities are mapped to MicroFunctions, OpenAPI/AsyncAPI, Kafka/Avro/CloudEvents, Flyway, OPA/SBAC, Flowable, observability, and evidence controls. |
| Make AI advisory only | AI may summarize approved evidence but may not approve access, unlock accounts, bypass step-up, or execute production-impacting actions. |
| Make acceptance evidence explicit | PoC 1A is complete only when regression, security, policy, workflow, observability, DAST, GitNexus, and PR/MR AVCI evidence are complete. |

# 2. Source Alignment and Correction Verdict

This document aligns with the active AIRA baseline and the revised documents generated during the current review sequence. Older references are retained only as lineage. Where conflicts appear, the stricter and newer AIRA control governs and the issue must be logged as an AVCI reconciliation item.
| Source / Standard | Required Alignment |
| --- | --- |
| 43 PoC 1A Execution Standard | Defines the mandatory additive login security-intelligence implementation baseline. |
| 43C Integrated Control Pattern Matrix | Defines integrated PoC 1 and PoC 1A acceptance gates and PoC 2 readiness. |
| 43D PoC 1A Generation Prompt | Defines code, parameter, configuration, Flyway, policy, workspace, and evidence generation requirements. |
| 22B / 23C / 24 Login Baseline | Defines canonical login pattern, 20-step login sequence, schemas, runtime configuration, and PoC 1 boundary rules. |
| 41 / 42 / 12A / 44-61 Dynamic Workspace family | Defines frontend/backend authority, component registry, policy-filtered rendering, observability, accessibility, and evidence. |
| 10 / 10A-D MicroFunction family | Defines configuration-first assembly, standard steps, idempotency, ports/adapters, evidence, and reuse-before-code. |
| 15 / 15A API Contract Standards | Defines contract-first REST/event design, generated clients, error semantics, idempotency, versioning, and evidence. |
| 31A / 53 Observability and Evidence | Defines trace, metric, log, audit, evidence, dashboard, redaction, and trace reconstruction requirements. |
| 42D-42S AI Agent Governance family | Governs any AI-assisted incident summary, model route, guardrail, registry, and runtime evidence. |

# 3. Purpose, Scope, and Authority

## 3.1 Purpose

Explain PoC 1A login security-intelligence functionality in a developer-understandable and architecture-compliant way.

Translate suspicious login review, failure triage, step-up, lock/unlock approval, and AI-assisted incident analysis into implementation-ready AIRA concepts.

Prevent developers or AI coding tools from treating PoC 1A as a login rewrite, frontend-only feature, or shortcut around Keycloak, OPA/SBAC, Flowable, audit, outbox, or observability.

Define the evidence and acceptance expectations that must be satisfied before PoC 1A can be considered complete and before PoC 2 can start.

## 3.2 In Scope

Developer explanation of PoC 1A capabilities and runtime behavior.

MicroFunction transaction explanation for AUTH_LOGIN_RISK_REVIEW, AUTH_LOGIN_FAILURE_TRIAGE, AUTH_STEP_UP_REQUIRED, AUTH_ACCOUNT_LOCK_REQUEST, AUTH_ACCOUNT_UNLOCK_REQUEST, and AUTH_LOGIN_INCIDENT_ANALYZE.

Dynamic Workspace screens, security review panels, user-safe notices, approval queues, and evidence timeline widgets.

API/event, data, workflow, observability, security, testing, DevSecOps, and evidence interpretation for developers.

## 3.3 Out of Scope

Replacing PoC 1 login authentication, session establishment, or authorization baseline.

Building a custom password, MFA, or credential validation engine inside AIRA application code.

Allowing the frontend, AI assistant, controller, or local script to approve access, unlock accounts, or bypass policy.

Providing production deployment approval. PoC 1A outputs remain review-ready until CI/CD, ARB/CAB, security, and acceptance gates are satisfied.

# 4. Non-Destructive PoC 1 Preservation Rules
| Core Rule PoC 1A adds capabilities to the Login MicroFunction design pattern. It must not replace PoC 1, bypass Keycloak/AD, bypass OPA/SBAC, weaken audit or observability, create frontend authorization authority, or hardcode authorization in controllers. |
| --- |
| Preservation Area | Developer Requirement |
| --- | --- |
| Transaction | AUTH_LOGIN_CONTEXT_ESTABLISH remains the baseline login/session transaction. |
| Regression | All existing PoC 1 unit, integration, OPA, API, frontend, and smoke tests must continue to pass. |
| Data model | Additive Flyway migrations only. No destructive rename, drop, rewrite, or simplified schema drift. |
| Runtime activation | PoC 1A feature flags default to disabled/draft. PoC 1 must work when all PoC 1A flags are disabled. |
| Policy | OPA/SBAC remains the authority for allow, deny, step-up, human-review, lock/unlock, and evidence-view decisions. |
| Frontend | Frontend renders policy-filtered state and actions only. It does not decide authorization or account action approval. |
| AI | AI summarizes approved evidence only. AI cannot approve, unlock, step-up bypass, or execute privileged action. |

# 5. PoC 1A Functional Capability Explanation

PoC 1A should be explained to developers as a risk-aware control layer around login, not as a new login product. Each capability has a business meaning, a MicroFunction transaction, a policy decision, a user or security workflow behavior, and an evidence requirement.
| Capability | Developer Explanation | Primary Transaction / Control | Evidence |
| --- | --- | --- | --- |
| Suspicious login risk review | Evaluates deterministic risk signals after identity/session context is available or when configured for elevated access exposure. | AUTH_LOGIN_RISK_REVIEW; LOGIN_RISK_MODEL_V1; OPA/SBAC policy decision. | Risk assessment record, policy decision, trace, audit, tests. |
| Login failure auto-triage | Classifies failures safely without user enumeration or sensitive leakage. Used for diagnostics, security review, and evidence. | AUTH_LOGIN_FAILURE_TRIAGE; safe failure categories; safe response profile. | Failure triage record, safe response proof, tests, no sensitive leakage evidence. |
| Policy-based step-up | OPA determines whether additional assurance is required; Keycloak performs the challenge. AIRA records decision and evidence. | AUTH_STEP_UP_REQUIRED; Keycloak/OIDC/MFA adapter; policy result. | Step-up decision, Keycloak evidence, regression tests, trace. |
| Account lock request | Creates a governed human-review request for security-sensitive lock or hold actions. It is not a direct UI/controller mutation. | AUTH_ACCOUNT_LOCK_REQUEST; Flowable security review workflow. | Workflow record, maker-checker evidence, SoD tests, audit. |
| Account unlock request | Creates a governed unlock request requiring elevated approval for privileged or sensitive accounts. | AUTH_ACCOUNT_UNLOCK_REQUEST; Flowable approval; Keycloak adapter only after approval. | Approval evidence, adapter result, policy decision, audit. |
| AI-assisted incident analysis | Generates an advisory summary from approved evidence references. It assists review but cannot approve or act. | AUTH_LOGIN_INCIDENT_ANALYZE; LiteLLM route; guardrails; evidence retrieval. | Prompt version, model alias, guardrail result, evidence refs, human review state. |

# 6. Architecture Interpretation for Developers

Developers shall implement PoC 1A through Clean Architecture, DDD, and ports/adapters. Domain and use-case logic must not depend directly on controllers, Keycloak Admin SDK, Flowable engine classes, OPA client, Kafka client, database tables, AI provider SDKs, telemetry exporters, or frontend state.
| Layer | Responsibility | Forbidden Coupling |
| --- | --- | --- |
| Domain | Risk assessment concepts, failure categories, account action request state, approval invariants, safe response concepts. | No controller, database, Keycloak, OPA, Flowable, AI, or Kafka dependencies. |
| Application / Use Case | Orchestrates ports, MicroFunction step behavior, policy request/response, workflow request, evidence references, and outcomes. | No direct SDK calls; use ports/adapters. |
| Inbound adapters | REST controllers, event consumers, workflow callbacks, frontend generated-client endpoints. | No business authority in controllers. |
| Outbound adapters | Keycloak, OPA, Flowable, Kafka/outbox, audit/evidence, AI gateway, database repository, telemetry. | No domain leakage into infrastructure. |
| Frontend | Displays policy-filtered components, safe notices, approval queues, evidence timeline, and advisory AI summary. | No token exposure, no authorization decisions, no direct unlock/lock mutation. |

# 7. MicroFunction and Runtime Assembly Requirements

Every PoC 1A function must be expressed as a governed, versioned, observable, policy-controlled, idempotent MicroFunction transaction or sub-transaction. Configuration is preferred before custom code. Code is allowed only for genuine business behavior or adapters not already covered by standard steps.
| Step Family | Required Use in PoC 1A |
| --- | --- |
| STP-RCV / STP-COR | Receive request or event; create trace_id, request_id, correlation_id, causation_id. |
| STP-SES / STP-SEC / STP-CLS | Resolve actor/session/tenant; authorize; classify; enforce OPA/SBAC and classification ceiling. |
| STP-VAL / STP-IDEMP | Validate inputs and enforce idempotency for retries, callbacks, approvals, and replay. |
| STP-BUS | Run deterministic risk review, failure triage, step-up decision mapping, or account action request logic. |
| STP-WF | Create or update Flowable human-review tasks where required. |
| STP-AI | Call approved AI gateway only for advisory evidence summaries with guardrails and approved retrieval. |
| STP-AUD / STP-OUTBOX | Write audit and transactional outbox events before external publication. |
| STP-OBS / STP-ERR | Emit safe logs, metrics, traces, alerts, error categories, and failure evidence. |

# 8. Data, API, Event, and Workflow Contracts

PoC 1A implementation must be contract-first. Developers must not invent endpoints, response fields, Kafka topics, event payloads, schema names, workflow states, or error semantics without approved contracts and tests.
| Contract Area | Required Control |
| --- | --- |
| OpenAPI | REST endpoints for risk review result, failure triage evidence, step-up status, lock/unlock request, approval queue, and incident summary must be documented, versioned, generated, and contract-tested. |
| AsyncAPI | Asynchronous login security events, approval events, DLQ/replay events, and evidence events must be documented as message-driven contracts. |
| Kafka / Avro / CloudEvents | Security events must use versioned schemas, CloudEvents metadata, trace correlation, idempotency key, schema compatibility, and classification metadata. |
| Outbox / Inbox | State-changing transactions publish through transactional outbox; consumers are idempotent, retry-safe, DLQ-aware, and replay-capable. |
| Flyway | All schema changes, seed data, views, indexes, RLS, outbox, audit, evidence, and configuration changes use Flyway. |
| Flowable | Lock/unlock and human-review workflows require maker-checker, SoD, status transitions, SLA timers, audit, and evidence. |

# 9. Canonical Schema and Configuration Interpretation
| Schema | PoC 1A Use |
| --- | --- |
| aira_mf | Reusable MicroFunction catalog, capability references, standard step definitions. |
| aira_cfg | Runtime transaction definitions, step bindings, parameters, retry/error policies, adapters, activation, validation. |
| aira_auth | Login/session/security-intelligence state, risk review, failure triage, idempotency references. |
| aira_policy | OPA/SBAC policy registry, versions, policy decision evidence, allow/deny/step-up/review outcomes. |
| aira_audit | Runtime, step, access-decision, security-control, workflow, and AI audit records. |
| aira_outbox | Transactional security event outbox, CloudEvents metadata, DLQ/replay references. |
| aira_ui | Dynamic Workspace templates, screens, components, capability bindings, policy bindings, evidence profiles. |
| aira_ai / aira_agent where applicable | AI advisory summary references, model route evidence, guardrail result, agent/run evidence only if AI agent controls are used. |
| Schema Drift Correction Do not create aira_config or aira_workspace for PoC 1A. If older notes or generated code reference aira_config, map it to aira_cfg. If older notes reference aira_workspace, map it to aira_ui. Any deviation requires ADR/TDL or register reconciliation. |
| --- |

# 10. Dynamic Workspace Behavior
| Workspace / Component | Developer Meaning | Authority Boundary |
| --- | --- | --- |
| AIRA_SECURITY_REVIEW_WORKSPACE | Security review workspace for high-risk login events, approval queue, incident analysis, and evidence timeline. | Visible only after backend resolver and OPA/SBAC filtering. |
| LOGIN_RISK_REVIEW_PANEL | Displays deterministic risk band, reason codes, and next action. | Read-only unless user has approved security skill. |
| LOGIN_FAILURE_TRIAGE_PANEL | Shows safe failure category and operational evidence without leaking sensitive reasons to the end user. | Evidence view is classification-filtered. |
| STEP_UP_STATUS_PANEL | Shows step-up required, pending, passed, failed, or expired state. | Keycloak performs step-up; frontend only displays state. |
| ACCOUNT_LOCK_REQUEST_FORM | Requests lock or hold workflow based on policy. | Submits a request; does not lock directly. |
| ACCOUNT_UNLOCK_REQUEST_FORM | Requests unlock workflow with reason, context, and evidence. | Requires maker-checker approval; AI cannot approve. |
| ACCOUNT_ACTION_APPROVAL_QUEUE | Shows actionable tasks for authorized security reviewers. | Backend and Flowable own state transition. |
| LOGIN_INCIDENT_SUMMARY_WIDGET | Displays AI-assisted advisory summary with evidence references and confidence. | Read-only advisory; human review required. |

# 11. Security, OPA/SBAC, and Human Approval Rules

OPA/SBAC must decide allow, deny, step_up_required, human_review_required, account_action_allowed, and evidence_view_allowed outcomes.

Privileged-account lock/unlock requires elevated approval and separation of duties. The requester cannot approve the same request.

The frontend, AI assistant, controller, and local scripts must never decide or execute account unlock authority.

No passwords, refresh tokens, ID tokens, raw JWTs, secrets, unnecessary PII, or sensitive reason details may be stored, logged, displayed, prompted, or captured in screenshots.

Authenticated DAST, SAST, SCA, secret scanning, dependency scanning, OPA tests, API contract tests, and failure-mode tests are mandatory before acceptance.

Abuse cases must include user enumeration, step-up bypass, token leakage, direct unlock attempt, approval spoofing, replayed callback, prompt injection, evidence overexposure, and DLQ replay misuse.

# 12. Observability, Audit, and Evidence Requirements

PoC 1A must be reconstructable from frontend interaction through backend API, policy decision, MicroFunction execution, workflow task, audit record, outbox event, AI advisory summary, and evidence pack. Logging may be tuned at runtime for performance, but mandatory security, audit, policy, evidence, and protected-action telemetry must not be disabled.
| Signal | Required Evidence |
| --- | --- |
| Trace | trace_id, span_id, request_id, correlation_id, causation_id across frontend, gateway, API, policy, MicroFunction, workflow, outbox, and AI gateway. |
| Logs | Safe structured Log4j2 logs with redaction and no forbidden fields. |
| Metrics | Risk-review counts, step-up outcomes, failure categories, approval durations, policy denials, DLQ/replay counts, error rates, and SLO indicators. |
| Audit | Actor, action, policy result, workflow state, evidence_ref, classification, reason code, and outcome. |
| Sentry / Error Monitoring | Frontend and backend error traces linked to release, route, feature flag, and trace_id. |
| Loki / Tempo / Grafana | Logs, traces, dashboards, alerting, denial analysis, evidence completeness, and trace reconstruction. |
| Evidence Pack | PR/MR evidence, tests, security scans, policy decisions, GitNexus impact, rollback, known limitations, and improvement backlog. |

# 13. Concurrency, Heavy Transaction, Idempotency, DLQ, and Resilience Lab
| Scenario | Required Behavior |
| --- | --- |
| Duplicate risk review request | Idempotency key and deterministic risk model prevent duplicate effects; repeated request returns safe current state. |
| Repeated failed login | Failure triage aggregates safely without user enumeration or excessive telemetry cardinality. |
| Step-up callback replay | Callback is replay-safe, duplicate-safe, and bounded by nonce/session/state validation. |
| Lock/unlock duplicate submit | Workflow idempotency prevents duplicate approval tasks for the same active request. |
| Outbox publish failure | Event remains in outbox, retries with bounded policy, escalates to DLQ when required, and supports replay with evidence. |
| OPA unavailable | Protected action fails closed and emits denial/error evidence. |
| Flowable unavailable | Account action request is not executed; safe response and incident/backlog evidence are generated. |
| AI gateway unavailable or guardrail blocks output | Incident analysis remains unavailable/advisory; no business action is blocked if non-AI evidence path is sufficient. |

# 14. Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop

PoC 1A may generate improvement candidates but must not silently mutate production, policy, prompts, schema, workflow, MicroFunction configuration, model routes, or runtime feature flags.
| Loop Stage | Required Treatment |
| --- | --- |
| Issue detection | Triggered by failed tests, policy denials, telemetry anomalies, security findings, repeated failure triage, Sentry events, DAST findings, or user feedback. |
| Evidence retrieval | Retrieve only approved evidence references with classification checks, freshness, source authority, and redaction. |
| Candidate proposal | Generate candidate fix, policy update, test, prompt guardrail, runbook update, or backlog item. |
| Impact analysis | Use GitNexus, contract impact, schema impact, policy impact, architecture fitness, and rollback analysis. |
| Human approval | Named owner, checker, security/architecture review, and CAB/ARB where required. |
| Implementation | PR/MR with tests, scans, evidence pack, rollback/safe-disable plan, and post-merge monitoring. |

# 15. Developer Implementation Sequence

Read PoC 1 baseline and confirm AUTH_LOGIN_CONTEXT_ESTABLISH, tests, API contracts, runtime configuration, OPA policy, audit/outbox, and Dynamic Workspace bootstrap exist.

Create a PoC 1A implementation branch and record source prompt, AI tools, owner, reviewer, and evidence path.

Define or update OpenAPI, AsyncAPI, Avro/CloudEvents schemas, OPA policy inputs, Flowable workflow contract, and Dynamic Workspace capability bindings before code generation.

Add Flyway migrations and seed data for additive configuration, evidence, outbox, policy, workflow, and UI records.

Implement application use cases and ports/adapters for risk review, failure triage, step-up, lock/unlock request, and AI advisory summary.

Implement frontend widgets only through generated clients and policy-filtered capability bindings.

Run unit, integration, OPA, contract, accessibility, Playwright, authenticated DAST, SAST/SCA, secret scan, architecture fitness, resilience, DLQ/replay, and PoC 1 regression tests.

Produce GitNexus impact analysis, evidence pack, PR/MR AVCI summary, rollback/safe-disable proof, and known limitations.

Obtain review and approval before enabling PoC 1A feature flags beyond local/demo scope.

# 16. Acceptance and Definition of Done
| Acceptance Gate | Pass Condition |
| --- | --- |
| PoC 1 preserved | PoC 1 works and all PoC 1 regression tests pass with all PoC 1A flags disabled. |
| Risk review | Deterministic risk model produces auditable risk band, reason codes, policy outcome, and tests. |
| Failure triage | Failures are classified safely without user enumeration or sensitive leakage. |
| Step-up | OPA returns step-up when required; Keycloak performs challenge; AIRA records evidence. |
| Lock/unlock | Flowable maker-checker workflow controls security-sensitive account actions; AI cannot approve. |
| AI advisory | Summary uses approved evidence only, guardrails pass, and human review state is recorded. |
| Dynamic Workspace | Security review workspace and user notices are policy-filtered, accessible, and safe. |
| Contracts and events | OpenAPI/AsyncAPI/Avro/CloudEvents contracts are versioned, generated, and tested. |
| Security and DevSecOps | SAST/SCA/secrets/authenticated DAST/OPA tests pass or have approved waivers. |
| Evidence | CI/CD evidence pack, GitNexus impact, trace reconstruction, rollback/safe-disable, and PR/MR AVCI summary are complete. |

# 17. Non-Negotiable Anti-Patterns

Creating a second login architecture for PoC 1A.

Adding risk/step-up/lock/unlock logic directly in the frontend or controller.

Using AI to approve access, unlock accounts, bypass step-up, or classify authority.

Logging raw tokens, secrets, passwords, raw PII, raw prompts, raw documents, or sensitive denial reasons.

Publishing Kafka events directly from business logic without transactional outbox and schema governance.

Changing database schemas manually or creating non-canonical schemas.

Disabling audit, policy-decision, evidence, or security telemetry because of performance concerns.

Treating a working screen as acceptance without tests, scans, evidence, rollback, and approval.

# 18. RACI and Review Responsibilities
| Activity | Developer | Tech Lead | Security | QA/SDET | DBA | DevSecOps | Solutions Architect / IT Head |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Functional understanding and design explanation | R | A/R | C | C | I | C | A |
| MicroFunction extension design | R | A/R | C | C | C | C | A |
| OPA/SBAC policy design | C | C | A/R | C | I | C | A |
| Flyway migration and seed plan | R | C | C | C | A/R | C | A |
| Flowable approval workflow | R | A/R | C | C | C | C | A |
| AI advisory prompt and guardrails | R | C | C | C | I | C | A |
| Tests, scans, DAST, resilience lab | R | C | C | A/R | C | C | A |
| Final PoC 1A readiness | C | C | C | C | C | C | A/R |

# 19. Review Queue Control Register
| Seq | File Name | Current Version | Recommended Version | Status | Next Step |
| --- | --- | --- | --- | --- | --- |
| 1 | 44-AIRA_PoC1A_Login_Security_Intelligence_Functionality_Explanation_and_Developer_Guide | v1.0 | v1.1 Revised | Completed in this output | Approve or return comments. |
| 2 | 43-AIRA_PoC1A_Login_Security_Intelligence_StepUp_Human_Approval_Execution_Standard | v1.0 | v1.1 Revised | Recommended next | Align parent execution standard with revised 43C, 43D, 42C, and PoC 2 evidence. |
| 3 | 41-AIRA_PoC1_Login_Execution_Instruction_and_Evidence_Governance_Standard | v1.0 | v1.1 Revised | Queue | Update PoC 1 execution evidence with revised PoC 1A and PoC 2 readiness. |
| 4 | 23C-AIRA_Login_PoC1_Code_Parameter_and_Configuration_Generation_Execution_Prompt_Standard | v1.1 | v1.2 Revised | Queue | Patch cross-references after 43/43C/43D/44 alignment. |
| 5 | Register / Master Cross-Reference Update | Mixed | TBD | Later | Update filenames, supersedence, duplicate numbering, and dependency matrix. |

# 20. External Alignment Register
| Reference | Use in This Document |
| --- | --- |
| OpenAPI 3.2.0 | HTTP API contract descriptions and generated clients. |
| AsyncAPI 3.1.0 | Message-driven contracts for Kafka/event flows. |
| CloudEvents | Standard event envelope metadata for outbox/replay traceability. |
| OpenTelemetry Semantic Conventions | Trace, metric, log, resource, and attribute naming consistency. |
| OWASP ASVS 5.0.0 | Authenticated web/API security verification and secure development controls. |
| WCAG 2.2 | Accessibility expectations for security review screens and user notices. |

# 21. AVCI Compliance Summary
| AVCI Property | Evidence in This v1.1 Revision |
| --- | --- |
| Attributable | Document owner, co-owners, source reviewed, companion documents, RACI, transactions, and evidence path are explicit. |
| Verifiable | Acceptance gates include regression tests, OPA tests, contract tests, DAST, scans, observability, GitNexus, and trace reconstruction. |
| Classifiable | Document and all PoC 1A artifacts are INTERNAL CONFIDENTIAL unless higher classification applies; telemetry and AI outputs carry handling rules. |
| Improvable | Auto-Heal/Auto-Learn/Auto-Improve loops create candidate improvements through evidence, tests, PR/MR, review, and human approval. |

# 22. Change Log
| Version | Date | Summary |
| --- | --- | --- |
| v1.0 | 2026-05 | Initial PoC 1A functionality explanation and developer guide. |
| v1.1 Revised | 2026-06 | Aligned with revised PoC 1A traceability, generation prompts, Dynamic Workspace controls, System Builder, AI Agent governance, DevSecOps evidence, API/event contracts, observability, resilience, and acceptance gates. |

