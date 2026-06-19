---
title: "Dynamic Workspace Security RBAC SBAC ABAC and OPA Policy Specification"
doc_id: "AIRA-51"
version: "v1.1"
status: "revised"
category: "Dynamic workspace"
source_docx: "AIRA_51_Dynamic_Workspace_Security_RBAC_SBAC_ABAC_and_OPA_Policy_Specification_v1.1_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 46-60-dynamic-workspace
  - revised
  - aira-51
---



# Dynamic Workspace Security RBAC SBAC ABAC and OPA Policy Specification



AIRA

AI-Native Enterprise Platform

Dynamic Workspace Security, RBAC, SBAC, ABAC, and OPA Policy Specification

Authorization | Field Visibility | Action Eligibility | Classification | Fail-Closed Policy | Rego Test Evidence | AVCI Always

AIRA-DOC-051 | Version v1.1 Revised | INTERNAL CONFIDENTIAL
| Mandatory Practice Statement | No AIRA Dynamic Workspace, screen, component, widget, field, layout, personalization rule, Admin Builder action, AI Assistant capability, file upload, generated artifact, workflow transition, or MicroFunction-backed action may be rendered, exposed, activated, invoked, or promoted unless backend policy has allowed it through RBAC, SBAC, ABAC, classification handling, OPA/Rego policy-as-code, audit, observability, and AVCI evidence. The backend must remove what the user is not allowed to see before the frontend receives the workspace definition. Missing identity, classification, policy, evidence, guardrail, audit, or approval fails closed. |
| --- | --- |

# Document Control
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-051 |
| Canonical Filename | 51-AIRA_Dynamic_Workspace_Security_RBAC_SBAC_ABAC_and_OPA_Policy_Specification_v1.1_Revised.docx |
| Version | v1.1 - Revised Dynamic Workspace Security, RBAC, SBAC, ABAC, OPA/Rego, Policy Evidence, Runtime Toggle, DevSecOps, and Auto-Improve Alignment |
| Status | Draft for Architecture Board, CAB, Security Architecture, DevSecOps, Workspace Platform, Frontend, Backend, QA/SDET, AI Governance, SRE, Product Owner, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Security Architecture; Workspace Platform Team; Frontend Lead; Backend Lead; Software Development Lead; DevSecOps Lead; QA/SDET; Platform Engineering; AI Governance; SRE; Internal Audit |
| Supersedes | 51-AIRA_Dynamic_Workspace_Security_RBAC_SBAC_ABAC_and_OPA_Policy_Specification_v1.0 |
| Primary Parents / Companions | 41 Dynamic User Workspace Framework; 42 Composable Experience Framework; 43 Multimodal AI Assistant Panel; 44 Next.js Rendering Strategy; 46 Runtime Configuration and Cache; 47 Developer Implementation Guide; 48 Database/Flyway Specification; 49 API/OpenAPI Contract Specification; 50 Component and Widget Development; 52 Testing and Fitness Functions; 53 Observability; 54 Admin Builder; 59 UX/Accessibility; 60 DevSecOps Evidence; 15/15A API Governance; 16/16A/16B Database/Flyway; 17/17A Security; 32 SBAC Catalog; 20/45 CI/CD and Evidence Pack; 31/31A Operations and Observability |
| External Alignment Checked | Open Policy Agent/Rego documentation; OWASP ASVS 5.0.0; OWASP API Security Top 10 2023; NIST SSDF SP 800-218; OpenTelemetry Semantic Conventions; SLSA v1.2 |

# Static Table of Contents

Executive Summary and Revision Verdict

Purpose, Scope, Authority, and Source Alignment

Authorization Model and Policy Decision Points

Canonical Policy Input, Output, and Decision Evidence Schema

Workspace, Screen, Component, Field, Action, AI, and Admin Policy Rules

OPA/Rego Design, Bundles, Tests, CI/CD Gates, and Runtime Enforcement

Security, Classification, Runtime Toggles, Observability, Resilience, and Incident Controls

RACI, Acceptance Criteria, AVCI Summary, and Appendices

# 1. Executive Summary and v1.1 Revision Verdict

This revised specification upgrades AIRA-DOC-051 from the baseline Dynamic Workspace security and OPA policy specification into the controlling security policy standard for backend-governed workspace resolution, component filtering, field visibility, action eligibility, AI Assistant access, Admin Builder template lifecycle, file upload eligibility, generated artifact visibility, and MicroFunction invocation.

The core rule remains unchanged and is strengthened: the frontend must not be trusted to enforce authorization. The backend Workspace Resolver, capability binding services, API gateway, MicroFunction runtime, and AI Assistant gateway must evaluate identity, roles, skills, attributes, classification, trust, feature flags, workflow state, and policy. Disallowed screens, components, fields, actions, and AI affordances must be removed or safely disabled before rendering.
| v1.1 Outcome | Required Result |
| --- | --- |
| No frontend authority | The frontend may render allowed state and submit user intent only. It cannot decide business authority, access, policy, workflow, AI route, or data classification. |
| Layered authorization | RBAC supplies coarse role eligibility; SBAC gates skills; ABAC evaluates context; OPA/Rego returns policy decisions; classification limits data exposure, cache, telemetry, retention, and model routes. |
| Fail-closed workspace | Unknown actor, stale session, missing policy, unavailable OPA, missing classification, missing evidence store, missing guardrail, or absent approval blocks protected exposure/action. |
| Evidence by decision | Every policy decision that affects visibility, field filtering, action eligibility, AI access, admin template activation, or MicroFunction invocation emits decision evidence. |
| Reversible policy lifecycle | Policy bundles, versioned inputs, feature flags, runtime toggles, activation records, rollback plan, and policy test evidence are required before promotion. |

# 2. Purpose, Scope, Authority, and Source Alignment
| Area | Treatment |
| --- | --- |
| Purpose | Define how Dynamic Workspace security decisions are modeled, evaluated, tested, evidenced, promoted, observed, and improved. |
| In Scope | Workspace visibility, screen visibility, component availability, field visibility/editability, widget action eligibility, layout personalization, Admin Builder changes, AI capability access, upload/artifact visibility, MicroFunction invocation, workflow transitions, policy tests, and decision telemetry. |
| Out of Scope | Frontend-only access control, role-only authorization, scattered if/else policy in controllers, direct UI-controlled permissions, hardcoded security decisions, unreviewed Rego bundles, unmanaged local policies, and direct production policy mutation. |
| Authority | AIRA-DOC-051 governs Dynamic Workspace policy decisions. 17/17A govern enterprise security, identity, secrets, and access. 32 governs RBAC/ABAC/SBAC catalog. 49 governs APIs. 50 governs widgets. 53/31A govern telemetry. 52/20/45 govern policy tests and CI/CD evidence. |

# 3. Authorization Model and Policy Decision Points
| Layer | Mandatory Meaning |
| --- | --- |
| RBAC | Coarse role eligibility such as borrower, loan officer, branch manager, security reviewer, department admin, system admin, auditor, product owner, or AI agent owner. Reject role explosion and shared unrestricted roles. |
| SBAC | Skill-based authority such as KYC_REVIEW, LOAN_APPROVE, WORKSPACE_TEMPLATE_PUBLISH, SECURITY_REVIEW, AI_ASSIST_USE, DAST_RUN, or DLQ_REPLAY_REVIEW. Skills require proficiency, trust, scope, expiry, and recertification. |
| ABAC | Contextual constraints such as tenant, branch, department, workflow state, assigned queue, environment, time window, device posture, trust score, data classification, customer relationship, feature flag, and risk band. |
| OPA/Rego | Central policy-as-code decision point. Policies return allow, deny, filter, mask, require_approval, safe_disable, step_up, quarantine, or escalate. OPA errors default to deny for protected actions. |
| Classification | Controls workspace, screen, field, component, action, cache, telemetry, evidence, prompt, artifact, model route, retention, export, and sharing eligibility. |
| Policy Decision Point | Decision Question |
| --- | --- |
| Workspace visibility | Can the subject open the workspace code? |
| Screen visibility | Can the subject open the screen within this workspace? |
| Component availability | Can this component key be included in the resolved layout? |
| Widget action eligibility | Can this actor invoke this action with this payload and idempotency key? |
| Field visibility | Should a field be visible, masked, redacted, or omitted? |
| Field editability | Can the subject edit or submit this field under current workflow state? |
| Layout personalization | Can the user add, remove, move, resize, save, share, or reset a layout element? |
| Admin template change | Can the actor draft, propose, approve, publish, activate, deactivate, or rollback a template? |
| AI capability access | Can the actor submit this prompt, context, file, or output mode through this model route? |
| File/artifact eligibility | Can this file be uploaded, classified, scanned, used for retrieval, generated, viewed, exported, or retained? |
| MicroFunction invocation | Can the widget invoke the bound transaction code and capability? |
| Workflow transition | Can the actor perform this task action without violating maker-checker or SoD? |

# 4. Canonical Policy Input, Output, and Decision Evidence Schema

Every Dynamic Workspace policy request must be deterministic, classifiable, auditable, and testable. Policy input may be assembled by the Workspace Resolver, API Gateway, Backend-for-Frontend, Capability Binding Service, MicroFunction runtime, Admin Builder service, AI Assistant gateway, or workflow adapter. The frontend may pass user intent, but it must not be trusted as the source of authority.

{
  "subject": {
    "subjectType": "HUMAN|SERVICE|AI_AGENT",
    "userIdHash": "usr_hash",
    "tenantId": "BFS",
    "roles": ["LOAN_OFFICER"],
    "skills": ["MORTGAGE_VIEW", "KYC_REVIEW"],
    "department": "Loan Operations",
    "branch": "MAKATI",
    "trustScore": 85,
    "devicePosture": "COMPLIANT",
    "mfaSatisfied": true,
    "sessionAssurance": "STANDARD|STEP_UP"
  },
  "resource": {
    "resourceType": "WORKSPACE|SCREEN|COMPONENT|FIELD|ACTION|AI_CAPABILITY|TEMPLATE|ARTIFACT",
    "workspaceCode": "REAL_PROPERTY_MORTGAGE_WORKSPACE",
    "screenCode": "MORTGAGE_DASHBOARD",
    "componentKey": "mortgagePipelineWidget",
    "fieldCode": "borrowerName",
    "classification": "CONFIDENTIAL",
    "classificationCeiling": "CONFIDENTIAL",
    "capabilityCode": "MORTGAGE_PIPELINE_VIEW"
  },
  "action": "WIDGET_VIEW|WIDGET_ACTION|FIELD_EDIT|AI_PROMPT|TEMPLATE_PUBLISH",
  "context": {
    "environment": "PROD",
    "workflowState": "PENDING_REVIEW",
    "featureFlags": ["workspace-personalization-v1"],
    "riskBand": "LOW|MEDIUM|HIGH|CRITICAL",
    "requestId": "req-uuid",
    "traceId": "trace-id",
    "idempotencyKey": "uuid-v7"
  }
}
| Decision | Required Meaning |
| --- | --- |
| allow | The requested workspace/screen/component/action/field/AI capability is permitted under returned constraints. |
| deny | The request is blocked. Return user-safe denial without leaking sensitive policy detail. |
| filter | Return only allowed components, fields, actions, tabs, rows, or artifacts. Unauthorized items must be absent, not only hidden. |
| mask | Return redacted or masked value with clear classification and audit evidence. |
| require_approval | Action can proceed only after named human/workflow approval. Self-approval is blocked. |
| safe_disable | Render disabled state because feature flag, policy, classification, dependency, or approval is unavailable. |
| step_up | Require stronger session assurance, MFA, device posture, or reviewer confirmation before continuing. |
| quarantine | Block and isolate suspicious file, prompt, artifact, configuration, or policy input. |

## Decision Evidence Fields
| Field | Meaning |
| --- | --- |
| policy_decision_id | Unique policy decision identifier linked to trace, actor, request, and evidence record. |
| policy_ref / policy_version | OPA package/rule/bundle version and Git commit/hash used for decision. |
| decision | allow, deny, filter, mask, require_approval, safe_disable, step_up, quarantine, escalate. |
| reason_code | Safe non-sensitive reason code such as SKILL_MISSING, CLASSIFICATION_EXCEEDED, OPA_UNAVAILABLE. |
| obligations | Required audit, masking, approval, step-up, telemetry, retention, or post-action verification duties. |
| evidence_ref | Pointer to audit/evidence record, CI test evidence, approval, or runtime trace. |

# 5. Workspace, Screen, Component, Field, Action, AI, and Admin Policy Rules
| Policy Domain | Mandatory Rule |
| --- | --- |
| Workspace and screen | Resolver must evaluate actor, tenant, role, skill, branch, classification ceiling, environment, feature flags, and template status before returning any layout. |
| Component and widget | Component availability requires registry approval, runtime_allowed flag, classification ceiling, capability binding, schema validity, policy binding, and evidence profile. |
| Fields | Backend must decide visible, hidden, masked, read-only, editable, required, and exportable states. Unauthorized fields are omitted before frontend rendering. |
| Actions | Widget actions require action code, capability code, required skill, ABAC context, idempotency profile, API contract, MicroFunction/workflow binding, and audit profile. |
| Personalization | Personalization may only choose among allowed components and layout parameters. It cannot create new components, fields, actions, permissions, APIs, policies, or model routes. |
| Admin Builder | Template authoring, review, publish, activation, deactivation, rollback, retirement, and assignment require maker-checker, SoD, CI/policy evidence, and approval records. |
| AI Assistant | AI capability access requires approved prompt capability, model route alias, guardrails, classification-safe input/output, retrieval eligibility, artifact retention, audit, and human review where high risk. |
| File upload/artifact | Upload requires malware scan, classification, content-type policy, size limit, retention rule, source owner, storage reference, and retrieval eligibility decision. |
| Frontend State | Security Treatment |
| --- | --- |
| Loading | Allowed without sensitive data; no premature data display. |
| Denied | Return safe denial message and reason code without exposing policy internals, role names beyond user-safe text, query logic, data existence, or exploit signals. |
| Empty | Allowed only after policy-filtered query returns no allowed results. Do not reveal denied counts. |
| Error | Return safe error, trace reference where allowed, and support path. Never expose stack traces, raw policy input, secrets, tokens, PII, or raw SQL. |
| Safe-disabled | Component/action may be rendered disabled only when the user is permitted to know it exists; otherwise omit it. |
| Pending approval | Show only workflow state and approver path that the subject is authorized to view. |

# 6. OPA/Rego Design, Bundles, Tests, CI/CD Gates, and Runtime Enforcement
| OPA/Rego Area | Required Treatment |
| --- | --- |
| Policy packaging | Policies are versioned as code, reviewed through PR/MR, tested with deterministic fixtures, bundled with hash/version metadata, and promoted through environment gates. |
| Rule structure | Separate rule packages for workspace visibility, component filtering, field filtering, action eligibility, admin lifecycle, AI capability, artifacts, and MicroFunction invocation. |
| Default deny | Every package must define default allow := false or equivalent explicit deny behavior. Missing input, missing data, or parsing errors deny protected actions. |
| Obligations | Policies return obligations such as mask fields, require approval, require step-up, emit audit, restrict cache, restrict model route, or require post-action verification. |
| Data dependencies | Policy data must be sourced from approved registries and versioned snapshots. Runtime caches are derivative and must fail closed when stale or unknown. |
| Compatibility | Policy input/output schemas are contract-bound and versioned. Breaking policy changes require migration, tests, rollout plan, and rollback path. |

package aira.workspace.authorization

default allow := false

default decision := {"result": "deny", "reason_code": "DEFAULT_DENY"}

allow {
  input.subject.status == "ACTIVE"
  input.subject.mfaSatisfied == true
  input.subject.trustScore >= data.required_trust[input.resource.capabilityCode]
  input.resource.classificationCeiling >= input.resource.classification
  input.resource.capabilityCode in input.subject.allowedCapabilities
  input.context.environment in data.allowed_environments[input.resource.capabilityCode]
  not input.guardrail.blocked
  not input.breakGlassWithoutApproval
}

decision := {"result": "allow", "obligations": ["AUDIT", "TRACE", "CLASSIFY"]} {
  allow
}

decision := {"result": "require_approval", "reason_code": "HIGH_RISK_ACTION"} {
  input.context.riskBand == "HIGH"
  input.action == "WIDGET_ACTION"
}
| Test / Gate | Minimum Coverage |
| --- | --- |
| Policy unit tests | Allow, deny, filter, mask, require_approval, safe_disable, step_up, quarantine, missing input, stale data, and OPA unavailable scenarios. |
| Contract tests | Policy input/output schema compatibility with Workspace Resolver, Gateway, AI Assistant, Admin Builder, and MicroFunction runtime. |
| Security tests | BOLA/BOPLA, field over-posting, action tampering, role/skill spoofing, tenant/branch mismatch, replay, prompt injection, and unauthorized artifact access. |
| Authenticated DAST | Authenticated scans with synthetic users across roles/skills, ensuring hidden/denied fields and actions are not reachable server-side. |
| CI/CD gates | Rego formatting, unit tests, schema checks, static analysis, affected policy map, GitNexus impact, SAST/SCA/secrets, evidence pack, approval, and rollback checks. |

# 7. Security, Classification, Runtime Toggles, Observability, Resilience, and Incident Controls
| Security Area | Control |
| --- | --- |
| Forbidden exposure | No passwords, raw JWTs, refresh tokens, secrets, raw PII, account numbers, raw documents, raw KYC files, raw prompts containing Confidential/Restricted data, embeddings, private keys, or unrestricted customer payloads in UI, logs, traces, metrics, prompts, screenshots, or evidence summaries. |
| Object and property authorization | Every object, row, field, document, task, artifact, and action must be authorized server-side. Field filtering is mandatory for property-level authorization. |
| Classification routing | Classification governs component availability, field exposure, cache eligibility, log fields, evidence retention, file handling, AI route eligibility, and export rules. |
| Secrets and tokens | Frontend receives only safe session state and backend-supplied CSRF/session controls. Raw tokens and secrets are never rendered, logged, persisted, or sent to AI. |
| Prompt and artifact safety | Prompt context and generated artifacts are classified, guardrail-checked, reference-bound, retention-governed, and reviewed when high-risk or low-confidence. |
| Runtime Toggle Area | Governance Rule |
| --- | --- |
| Allowed toggles | Policy evaluation tracing, deny reason verbosity in non-prod, telemetry sampling, feature rollout, component safe-disable, AI panel availability, synthetic DAST users, and diagnostic dashboards. |
| Prohibited toggles | Authorization bypass, OPA bypass, audit/evidence disablement, secret redaction disablement, classification bypass, field-filter disablement, unauthenticated DAST avoidance, or production policy mutation without approval. |
| Runtime control | Toggle change requires owner, environment, reason, expiry, risk tier, policy decision, approval where required, audit, evidence_ref, rollback path, and post-change verification. |
| Performance control | Policy decision telemetry and debug traces must support sampling, payload bounds, and privacy-safe redaction to avoid production performance or data exposure impact. |
| Area | Required Evidence |
| --- | --- |
| Telemetry | trace_id, span_id, actor_hash, workspace_code, screen_code, component_key, action_code, policy_ref, policy_decision_id, reason_code, classification, and evidence_ref. |
| Dashboards | Policy denial analysis, skill gap, field filtering, admin template approvals, AI guardrail outcomes, upload quarantines, MicroFunction denies, and suspicious access attempts. |
| Incident triggers | Repeated deny anomaly, policy bundle drift, OPA outage, unauthorized field exposure, prompt injection, secret leakage, high-risk action bypass attempt, template tampering, or audit/evidence failure. |
| Resilience | OPA outage, registry/cache loss, stale policy data, backend dependency failure, duplicate action submission, replay attempt, and degraded-mode behavior must be tested and fail closed. |

# 8. RACI, Acceptance Criteria, and AVCI Summary
| Activity | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Policy model and rule catalog | Security Architecture | Security Lead | Workspace Platform; Product Owner; Backend; Frontend | Internal Audit |
| OPA/Rego implementation | Security / Backend Engineer | Security Architecture | QA/SDET; DevSecOps; Architecture | Product Owner; Audit |
| Workspace Resolver enforcement | Backend Lead | Architecture | Security; Frontend; QA/SDET | Product Owner; Audit |
| Component/action binding | Workspace Platform | Product Owner / Architecture | Security; Backend; Frontend; QA | Internal Audit |
| Policy tests and authenticated DAST | QA/SDET / Security | QA Lead / Security Lead | DevSecOps; Product Owner; Developers | Internal Audit |
| CI/CD evidence and promotion | DevSecOps | CAB/ARB as applicable | Security; QA; Architecture; Product Owner | Internal Audit |
| Access review and recertification | Security / Process Owner | Business Owner / Security Lead | Internal Audit; HR/JML; System Owner | CAB/ARB where applicable |

## Acceptance Criteria

All workspace, screen, component, field, action, AI, admin, artifact, workflow, and MicroFunction decisions are evaluated server-side through RBAC/SBAC/ABAC/classification/OPA policy.

Frontend receives only backend-filtered workspace definitions and safe response envelopes; unauthorized fields/actions/components are omitted or safely disabled according to policy.

Policy input/output schemas are versioned, contract-tested, and traceable to registry fields, API contracts, component keys, capability codes, and MicroFunction transactions.

OPA/Rego policies have default deny, deterministic fixtures, allow/deny/filter/mask/approval/step-up/quarantine tests, and CI/CD evidence.

Authenticated DAST with synthetic users verifies server-side denial and object/property authorization across roles, skills, tenants, branches, classifications, and workflow states.

Runtime toggles are governed, audited, reversible, time-bound where applicable, and cannot disable authorization, OPA, audit, redaction, classification, or evidence controls.

Observability dashboards can reconstruct denied actions, field filtering, admin approvals, AI guardrail decisions, MicroFunction invocations, and policy drift without exposing secrets or PII.

Promotion requires PR/MR AVCI summary, policy tests, architecture fitness, GitNexus impact, rollback plan, CAB/ARB approval where required, and post-promotion monitoring.

## Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop
| Loop Stage | Control |
| --- | --- |
| Trigger | Policy denials, access incidents, authenticated DAST findings, user feedback, widget errors, prompt guardrail failures, policy drift, GitNexus impact, or audit exceptions. |
| Candidate action | AI/System Builder may summarize evidence, propose policy refinement, draft Rego test, suggest SBAC catalog update, or open a PR draft. It may not self-approve, weaken policy, or mutate production. |
| Validation | Security owner review, regression tests, OPA tests, DAST evidence, contract impact, classification review, rollback path, and maker-checker approval. |
| Promotion | Only reviewed and approved policy changes with CI/CD evidence, CAB/ARB where applicable, activation record, telemetry, and rollback plan become active. |

## AVCI Compliance Summary
| AVCI Property | Policy Evidence |
| --- | --- |
| Attributable | Policy owner, rule package, policy version, source commit, subject/resource/action, component key, capability code, MicroFunction transaction, approver, and evidence path are recorded. |
| Verifiable | OPA tests, contract tests, authenticated DAST, policy decision logs, runtime traces, CI/CD gates, GitNexus impact, and audit evidence prove behavior. |
| Classifiable | Policy inputs, outputs, UI fields, components, actions, prompts, artifacts, evidence, telemetry, cache, and retention are classification-aware and redacted. |
| Improvable | Denied-action analytics, incidents, tests, user feedback, DAST findings, audit findings, policy drift, and Auto-Learn outputs feed controlled improvement. |

# Appendix A - PR/MR Policy Evidence Checklist

Ticket, owner, bounded context, policy package, policy version, component/action/capability impact, and classification declared.

Policy input/output schema impact reviewed and versioned.

OPA/Rego unit tests cover allow, deny, filter, mask, require_approval, safe_disable, step_up, quarantine, missing input, stale data, and OPA unavailable behavior.

Affected workspaces, screens, fields, components, widget actions, AI capabilities, and MicroFunction transactions listed.

Authenticated DAST and server-side authorization evidence attached where applicable.

Telemetry, audit, evidence_ref, and forbidden-field checks confirmed.

GitNexus impact, architecture fitness, rollback path, and post-promotion monitoring documented.

Maker-checker, Security, Product Owner, CAB/ARB, or Internal Audit approval attached where required.

# Appendix B - Final Control Statement

A Dynamic Workspace is not secure because a button is hidden or a screen is difficult to reach. It is secure only when the backend has removed unauthorized data and actions before rendering, all protected operations are re-authorized server-side, policy decisions are evidence-producing, and every exception is governed, testable, observable, reversible, and AVCI-compliant.

