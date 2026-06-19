---
title: "Policy as Code Implementation Standard"
doc_id: "AIRA-65"
version: "v1.0"
status: "final"
category: "Policy as code"
source_docx: "AIRA_65_Policy_as_Code_Implementation_Standard_v1.0.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 65-policy-as-code
  - final
  - aira-65
---



# Policy as Code Implementation Standard



AIRA
AI-Native Enterprise Platform

Policy-as-Code Implementation Standard

AIRA-DOC-065 | v1.0

OPA/Rego | SBAC | CI/CD Policy Gates | Runtime Decisions | Evidence by Construction | AVCI Always
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-065 |
| Document Title | AIRA Policy-as-Code Implementation Standard |
| Version | v1.0 - Initial Policy-as-Code Control Plane and Runtime Decision Governance Standard |
| Status | Draft for Architecture Review Board, CAB, Security Governance, DevSecOps, Platform Engineering, AI Governance, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; DevSecOps Lead; Security Architecture; Software Development Lead; QA/SDET; Platform Engineering; SRE; DBA; AI Engineering; Internal Audit |
| Primary Audience | Solutions Architects; Developers; DevSecOps Engineers; Security Engineers; QA/SDET; Platform Engineers; System Builder operators; AI agent owners; Internal Audit |
| Primary Parents | 01A, 01, 01B, 02, 03, 04, 10-10E, 11, 11A, 20, 42 series, 43, 62, 63, 64 |
| Related Standards | 15/15A API; 16/16A/16B Database/Flyway; 17/17A Security; 19 GitNexus; 31/31A Observability; 41B/44 System Builder; Dynamic Workspace 54-61 |
| External Alignment | Open Policy Agent/Rego, Conftest, NIST SSDF, SLSA provenance, OWASP ASVS, OpenTelemetry, CloudEvents |
| Review Cadence | Quarterly; unscheduled after material policy, security, CI/CD, MicroFunction, AI-agent, runtime-toggle, model-route, Dynamic Workspace, or production-control change |

Mandatory Practice Statement

No AIRA protected action, MicroFunction transaction, API call, workflow transition, CI/CD promotion, runtime toggle, AI tool action, model route, data access, deployment, environment provision, or production change may proceed unless the applicable policy decision is versioned, tested, attributable, fail-closed, logged, and linked to AVCI evidence. Policy-as-code is an enforcement control, not an advisory checklist.

# Table of Contents Placeholder

Insert a Microsoft Word automatic Table of Contents here before final publication. Recommended setting: show levels 1 to 3. Update all fields after final approval and before distribution.

# 1. Executive Summary

This standard establishes Policy-as-Code as a first-class AIRA control plane for authorization, classification, admission, deployment, runtime toggles, AI tool actions, model-route eligibility, data handling, evidence requirements, and promotion decisions. It turns governance rules into executable, tested, versioned, auditable decisions that can be enforced consistently by CI/CD pipelines, gateways, services, MicroFunction runtime, Dynamic Workspace, System Builder, and approved AI agents.

# 2. Purpose

Define how AIRA designs, authors, tests, packages, deploys, evaluates, observes, audits, and improves policy-as-code artifacts. Ensure policy decisions are deterministic, fail-closed, evidence-producing, and aligned with AVCI, Enterprise Design Principles, DevSecOps gates, MicroFunction controls, System Builder boundaries, and AI governance.

# 3. Scope

This standard applies to OPA/Rego policies, Conftest policies, SBAC rules, CI/CD gate policies, deployment/admission policies, API authorization policies, data classification rules, runtime toggle policies, model-route policies, AI tool-action policies, Dynamic Workspace policies, MicroFunction policies, environment provisioning policies, and waiver/exception controls.

# 4. Authority and Precedence
| Level | Authority | Policy-as-Code Interpretation |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance / IT Head | Final authority for production-impacting policy posture, waiver, exception, runtime-toggle, AI tool-action, and release decisions. |
| L1 | 01A, 01 AVCI, 01B Evidence, 02 Engineering Blueprint | Universal architecture, evidence, classification, audit, and reconciliation authority. |
| L2 | 11, 11A, 20, 63, 64 | DevSecOps, evidence-pack, production readiness, operational readiness, and resilience gate authority. |
| L2 | This AIRA-DOC-065 | Policy-as-code implementation authority for AIRA policy source, runtime decision, testing, evidence, and lifecycle controls. |
| L3 | 10-10E, 15/15A, 16/16A/16B, 17/17A, 31/31A, 42 series, 43, 54-61 | Specialist standards that define domain-specific policy rules and evidence expectations. |
| L4 | Git policy source, bundles, CI logs, OPA decision logs, audit records, evidence packs | Operational proof; may tighten but must not weaken governing standards. |

# 5. Policy-as-Code Governance Principles
| Principle | Mandatory Rule |
| --- | --- |
| PAC-01 Source-governed policy | Policies are stored in approved Git repositories with CODEOWNERS, branch protection, versioning, tests, and review evidence. |
| PAC-02 Deny by default | Protected action is denied unless a tested policy explicitly allows or routes to human approval/step-up. |
| PAC-03 Fail closed | Missing policy bundle, unavailable decision point, invalid input, missing classification, missing identity, or missing audit blocks protected action. |
| PAC-04 Separation of policy and code | Application code assembles policy input and enforces decision obligations; policy rules remain versioned policy artifacts. |
| PAC-05 Evidence by decision | Each protected decision emits or links policy_decision_id, input_hash, policy_version, trace_id, actor, action, classification, outcome, and evidence_ref. |
| PAC-06 Least privilege / SBAC | Policies evaluate actor skill, role, tenant, branch/unit, environment, tool scope, risk tier, and data classification. |
| PAC-07 Test before promotion | Policy unit tests, negative tests, regression tests, and CI/Conftest checks pass before bundle promotion. |
| PAC-08 AI is not authority | AI may draft policies or tests, but human review, CI, security validation, and evidence are required before use. |

Figure 1. AIRA Policy-as-Code Control Plane

# 6. Policy Domain Coverage
| Policy Domain | Required Coverage | Evidence |
| --- | --- | --- |
| Authorization and access control | RBAC/ABAC/SBAC, tenant, branch, role, skill, data classification, action, resource, and risk-tier decisions. | OPA decision log, SBAC evidence, policy tests, audit event. |
| CI/CD and repository gates | Branch protection, required checks, PR/MR evidence, artifact integrity, security scans, and release readiness. | Conftest/OPA result, CI evidence pack, PR/MR AVCI summary. |
| Deployment and admission | Environment eligibility, image digest, SBOM/provenance, runtime configuration, secret path, and rollback validation. | Deployment policy decision, artifact digest, evidence manifest. |
| MicroFunction runtime | Step eligibility, STP-BUS isolation, idempotency, outbox/DLQ/replay, audit, observability, and compensation posture. | runtime_definition_version, publish validation, decision ID. |
| Dynamic Workspace | Experience block visibility, action binding, data handling, capability exposure, accessibility, telemetry, and backend authority. | Workspace resolver policy decision, UI telemetry, audit record. |
| AI/model routes | LiteLLM alias, classification eligibility, retrieval scope, guardrail result, tool-action scope, human approval requirement. | model_route_policy_decision, guardrail result, prompt/evidence refs. |
| Runtime toggles | Allowed diagnostic toggles, sampling, feature flags, timebox, rollback, non-disableable audit/security/evidence controls. | toggle decision, expiry, audit event, monitoring proof. |
| Waivers and exceptions | Risk owner, expiry, compensating controls, approval, remediation plan, and closure evidence. | Waiver record, aging report, closure evidence. |

# 7. Repository and Package Structure
| Path / Area | Required Purpose |
| --- | --- |
| policy/authorization/ | API, MicroFunction, data, and action authorization policies. |
| policy/admission/ | Deployment, runtime configuration, environment, IaC, and container admission policies. |
| policy/cicd/ | PR/MR evidence, branch, test, scan, SBOM/provenance, and release gate policies. |
| policy/microfunction/ | Catalog, step sequence, idempotency, outbox, DLQ/replay, runtime-toggle, and evidence policies. |
| policy/ai/ | Model route, guardrail, retrieval, tool-action, agent lifecycle, and human approval policies. |
| policy/data/ | Classification, retention, redaction, logging, evidence, prompt, and telemetry handling policies. |
| data/ | Approved policy data documents such as environment tiers, role/skill maps, classification rules, and route catalogs. |
| tests/ | Rego unit tests, negative tests, golden decision sets, regression fixtures, and Conftest test cases. |
| bundles/ | Generated policy bundles, hashes, signatures, environment manifests, and promotion evidence. |
| evidence/ | Policy test outputs, decision samples, audit records, waiver records, and release evidence. |

# 8. Standard Policy Input and Decision Contract
| Input Field | Mandatory Meaning |
| --- | --- |
| actor | Human, service, AI agent, System Builder, CI/CD runner, or break-glass identity. |
| subject_context | tenant, branch/unit, role, SBAC skills, trust tier, session, authentication strength. |
| action | Requested capability, API operation, MicroFunction step, tool action, deployment, or runtime toggle. |
| resource | API, data object, transaction, environment, contract, policy, schema, tool, model, or evidence artifact. |
| classification | Input, output, evidence, prompt, telemetry, and resource classification. |
| risk | Risk tier, change type, environment, criticality, production impact, reversibility posture. |
| evidence_context | ticket, PR/MR, build ID, GitNexus ref, test result, scan result, approval, trace ID, evidence_ref. |
| runtime_context | runtime config version, policy bundle version, model route, guardrail result, toggle state, correlation IDs. |
| Decision Field | Required Meaning |
| --- | --- |
| decision | allow, deny, escalate, step_up, approval_required, break_glass_required, or not_applicable. |
| reason_code | Stable code for traceability, audit, and user-safe error mapping. |
| obligations | Required audit, redaction, approval, logging, evidence, monitoring, or rollback actions. |
| policy_decision_id | Unique decision reference for audit and evidence correlation. |
| input_hash | Hash of decision input excluding secrets and prohibited payloads. |
| policy_version | Policy bundle, rule, and data-document version used for the decision. |

Figure 2. Policy Lifecycle and Promotion Model

# 9. Minimum Rego Rule Pattern

The following pattern is illustrative. Teams must adapt it to approved AIRA packages, data documents, and evidence schemas. Deny-by-default remains mandatory.

package aira.authz

default allow := false
default approval_required := false

action_allowed if {
  input.actor.authenticated == true
  input.classification in data.classification.allowed[input.actor.clearance]
  input.action in data.sbac.allowed_actions[input.actor.skill]
  not high_risk_without_approval
}

allow if action_allowed

approval_required if {
  input.risk.tier == "high"
}

high_risk_without_approval if {
  input.risk.production_impact == true
  not input.evidence_context.approval_ref
}

deny[msg] if {
  not input.actor.authenticated
  msg := "PAC-AUTH-001 unauthenticated actor"
}

deny[msg] if {
  input.action == "runtime.toggle.disable_audit"
  msg := "PAC-TOGGLE-001 mandatory audit cannot be disabled"
}

# 10. Policy Lifecycle Controls
| Stage | Required Control | Blocking Condition |
| --- | --- | --- |
| Intake | Identify owner, policy domain, source requirement, classification, risk tier, and affected systems. | Owner, classification, or authority missing. |
| Design | Define decision intent, input schema, output schema, deny-by-default posture, and evidence fields. | Policy design omits identity, classification, audit, or fail-closed behavior. |
| Author | Create Rego/Conftest policy with data-document references and deterministic fixtures. | Policy hardcodes environment secrets, production-only values, or untestable external calls. |
| Test | Run unit, negative, regression, golden, CI/Conftest, and failure-path tests. | Policy tests fail or no negative tests exist for protected actions. |
| Bundle | Build versioned policy bundle with hash/signature where adopted and environment manifest. | Bundle is not tied to source commit or cannot be reconstructed. |
| Promote | Route through PR/MR, CODEOWNERS, CI gates, security review, and CAB/ARB where required. | Promotion lacks evidence, approval, rollback, or compatibility proof. |
| Operate | Log decision, metrics, denials, errors, drift, waiver use, and runtime health. | Protected decisions not logged or decision point fails open. |
| Improve | Review denied actions, false positives, incidents, abuse cases, waivers, and policy drift. | Learnings are not captured or expired waivers remain open. |

# 11. CI/CD and Conftest Gate Integration
| Gate | Required Policy Check |
| --- | --- |
| PR/MR evidence | Evidence manifest contains owner, classification, tests, scans, GitNexus, rollback, AI-use declaration, and approvals. |
| IaC/container/devcontainer | No privileged container, unsafe hostPath, public secret, missing resource limit, unpinned base image, or insecure network exposure unless approved. |
| API/event contracts | OpenAPI/AsyncAPI/schema changes include security scheme, classification, versioning, compatibility result, and consumer impact. |
| Database/Flyway | No manual DDL; migration includes checksum, clean-migrate validation, rollback/forward-fix, and DBA review where material. |
| MicroFunction publish | Mandatory steps, idempotency, outbox, DLQ/replay, audit, observability, policy, and compensation are present. |
| Release promotion | SBOM/provenance, artifact digest, signed or integrity-checked artifact, PRR/ORR, Resilience Lab evidence, rollback, and approval exist. |

# 12. Runtime Policy Decision Enforcement
| Runtime Location | Required Enforcement |
| --- | --- |
| API Gateway | Authenticate, classify, enforce route eligibility, rate limits, coarse access, and safe denial response. |
| Application / MicroFunction Coordinator | Assemble full policy input, enforce decision obligations, prevent bypass, and emit policy_decision_id. |
| Dynamic Workspace Resolver | Filter templates, widgets, actions, data blocks, and AI panel capabilities before rendering or invocation. |
| Workflow / Approval Engine | Evaluate maker-checker, escalation, separation-of-duties, timeout, and resumption policies. |
| AI Tool Gateway / Harness | Authorize tool action, model route, data scope, environment, risk tier, and human approval. |
| CI/CD Pipeline | Enforce build, security, evidence, environment, artifact, and release policies. |

Figure 3. Policy Decision Evidence Chain

# 13. MicroFunction, Dynamic Workspace, and AI Policy Rules
| Area | Mandatory Policy Rule |
| --- | --- |
| MicroFunction | A mutating transaction must be denied unless idempotency, authorization, classification, audit, evidence, observability, error policy, and rollback/compensation are present. |
| STP-BUS | Business functions must not be allowed to perform direct database, Kafka, Redis, model-provider, secrets, audit, or workflow calls. |
| Dynamic Workspace | UI components and Experience Blocks are rendered only when backend capability binding, policy, classification, and MicroFunction authority are allowed. |
| AI model route | Route is allowed only when actor, purpose, classification, retrieval scope, model alias, guardrail, cost/rate budget, and audit are eligible. |
| Tool action | Tool action requires SBAC, OPA, Harness mediation, risk tier, environment scope, and human approval where protected. |
| Runtime toggles | Diagnostic toggles may be approved; audit/security/policy/idempotency/outbox/critical-error evidence toggles must be denied. |

# 14. Policy Testing Standard
| Test Type | Minimum Requirement |
| --- | --- |
| Unit tests | Each allow, deny, escalate, step-up, and approval path has deterministic policy tests. |
| Negative tests | Protected actions deny when identity, classification, skill, approval, evidence, or environment is missing. |
| Golden decision tests | Representative decisions are versioned as stable fixtures and tested on every policy change. |
| Regression tests | Past incidents, waivers, abuse cases, and false positives become regression fixtures. |
| Conftest tests | Structured configuration, Kubernetes/Helm/Terraform/YAML/JSON manifests, and CI evidence are validated. |
| Performance tests | Runtime policy evaluation budget is measured for critical high-volume paths. |
| Failure-path tests | Policy service unavailable, stale bundle, invalid input, and storage failure are tested for fail-closed behavior. |

# 15. Decision Logging, Observability, and Evidence
| Evidence Field | Required Meaning |
| --- | --- |
| policy_decision_id | Unique decision identifier correlated to audit and trace. |
| input_hash | Hash of normalized policy input, excluding secrets and prohibited payloads. |
| policy_bundle_version | Bundle, rule, data document, and source commit used for the decision. |
| actor_ref | Human, service, agent, System Builder, or runner identity reference. |
| action_resource | Action and resource evaluated by policy. |
| classification | Classification and handling rule applied. |
| decision_outcome | allow, deny, escalate, step_up, approval_required, break_glass_required. |
| reason_code | Stable denial/approval/review reason code. |
| trace_id / evidence_ref | Runtime trace, audit event, evidence pack, PR/MR, or incident link. |
| obligations | Required redaction, monitoring, approval, audit, expiry, or rollback obligations. |

# 16. Waivers, Exceptions, and Break-Glass

Waivers are time-bound risk records, not permanent bypasses.

A waiver must identify policy, owner, reason, affected control, risk rating, compensating control, expiry, approval, and remediation plan.

Critical and High policy waivers require Security and Architecture approval; production-impacting waivers require CAB or delegated change authority.

Break-glass access must be logged, time-bound, least-privilege, monitored, and reviewed after use.

Policy must continue logging decisions during break-glass unless the logging control itself is unavailable; in that case incident handling and compensating evidence are mandatory.

# 17. RACI and Operating Responsibilities
| Activity | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Define policy domains and authority | Enterprise Architecture / Security | IT Head / Architecture Board | DevSecOps, Development, QA, SRE | Internal Audit |
| Author and test Rego policies | Security / DevSecOps | Security Architecture | Developers, QA/SDET, Platform | Architecture |
| Maintain policy bundles | DevSecOps / Platform | DevSecOps Lead | Security, SRE | Internal Audit |
| Implement policy input assembly | Development | Software Development Lead | Security, Architecture | QA/SDET |
| Review runtime decisions and denials | SRE / Security | Security Architecture | DevSecOps, Product Owner | Internal Audit |
| Approve waivers and exceptions | Risk Owner / Security | CAB / IT Head when required | Architecture, DevSecOps | Internal Audit |
| Audit policy evidence | Internal Audit | IT Head | Security, DevSecOps | Architecture Board |

# 18. Validation Checklist
| Checkpoint | Pass Condition |
| --- | --- |
| Policy source governance | Policy files are in approved Git path with owner, CODEOWNERS, branch protection, and review evidence. |
| Input/output contract | Policy input and decision output schemas are defined and versioned. |
| Deny-by-default | Protected policy has explicit default deny or safe escalation behavior. |
| Tests | Unit, negative, regression, golden, and CI/Conftest tests pass. |
| Evidence | Decision logs include decision ID, policy version, input hash, actor, action, classification, reason, trace, and evidence reference. |
| Fail-closed | Unavailable policy decision point, stale bundle, invalid input, or missing classification blocks protected action. |
| AI/tool controls | Model routes, guardrails, tool actions, and agent skills are policy-gated and human-approved where required. |
| Runtime toggles | No policy allows disabling mandatory audit/security/policy/idempotency/outbox/critical error evidence. |
| Waivers | Exceptions are time-bound, risk-owned, approved, tracked, and linked to remediation. |

# 19. Anti-Patterns and Rejection Rules

Hardcoded role checks in application code replace OPA/SBAC decisions.

Policy allows protected action when identity, classification, actor skill, policy bundle, or audit is missing.

A business MicroFunction bypasses policy by calling databases, queues, models, secrets, or tools directly.

CI/CD, System Builder, or AI agent proceeds without policy decision evidence.

Runtime toggle disables audit, security, policy, idempotency, outbox, DLQ/replay, or critical error evidence.

Policy bundle is promoted without tests, source commit, version, hash/signature, rollback plan, and reviewer approval.

GitNexus, AI output, Obsidian summary, or dashboard is treated as policy authority instead of Git-managed policy and decision evidence.

# 20. Implementation Roadmap
| Phase | Execution Focus | Exit Evidence |
| --- | --- | --- |
| Phase 0 - Baseline | Create policy repository structure, CODEOWNERS, PR template, policy data documents, and test folder. | Repository governance and initial policy manifest. |
| Phase 1 - CI policy gates | Implement Conftest/OPA checks for PR/MR evidence, IaC, environment, and runtime configuration manifests. | CI policy test reports and blocking gates. |
| Phase 2 - Runtime authorization | Integrate OPA/SBAC policy decisions into API gateway and MicroFunction coordinator. | Decision logs, audit events, denial tests. |
| Phase 3 - AI/tool policy | Gate model route, retrieval, guardrails, and tool actions through policy and Harness. | Model/tool policy evidence and agent tests. |
| Phase 4 - Dynamic Workspace | Apply policy-filtered component/action/data visibility and backend capability binding. | Workspace resolver policy evidence. |
| Phase 5 - Assurance | Create dashboards for denials, waivers, stale bundles, policy drift, and decision latency. | Grafana/Sentry/Loki/Tempo evidence and review cadence. |

# 21. Open Reconciliation Items and Backlog
| ID | Issue | Required Treatment | Owner |
| --- | --- | --- | --- |
| RI-065-001 | 41B / 44 System Builder overlap may create policy-authority ambiguity. | Refer to canonical register; System Builder may request decisions but must not be policy authority. | Architecture Board |
| RI-065-002 | Policy input schemas must be harmonized with evidence manifest schemas. | Generate or align AIRA Evidence Manifest Schema and Evidence Pack Data Model. | DevSecOps Lead |
| RI-065-003 | Runtime toggle policies must be reflected in Observability and Runtime Configuration documents. | Create cross-document update item and validator. | SRE / Platform |
| RI-065-004 | SBAC skill taxonomy must be stable enough for policy decisions. | Align with 07 Skills Framework and agent lifecycle registry. | Security / AI Governance |
| RI-065-005 | OPA deployment mode must be selected per component. | Document approved modes: library, sidecar, service, gateway plugin, CI/Conftest. | Platform Engineering |

# 22. External Alignment References
| Reference | AIRA Use |
| --- | --- |
| Open Policy Agent / Rego | Declarative policy language and decision engine for authorization, admission, CI/CD, and runtime policy evaluation. |
| Conftest | Policy testing for structured configuration and manifests using Rego-based assertions. |
| NIST SSDF SP 800-218 | Secure software development control alignment for policy, verification, and remediation practices. |
| SLSA v1.2 | Supply-chain provenance and artifact integrity alignment for policy-gated builds and promotions. |
| OWASP ASVS | Application security verification alignment for access control, error handling, API, and security test expectations. |
| OpenTelemetry / CloudEvents | Decision, audit, trace, event, and evidence correlation for policy-governed runtime flows. |

# 23. AVCI Compliance Summary
| AVCI Property | How This Standard Satisfies It |
| --- | --- |
| Attributable | Defines policy owners, source repositories, bundles, reviewers, decision IDs, actor references, PR/MR evidence, waiver owners, and runtime decision lineage. |
| Verifiable | Requires policy tests, Conftest/OPA outputs, decision logs, input hashes, policy versions, CI evidence, audit events, runtime traces, and assurance dashboards. |
| Classifiable | Requires classification in policy input, data handling, model route, evidence, logs, traces, prompts, runtime toggles, and retention rules. |
| Improvable | Denied actions, waivers, incidents, policy drift, false positives, abuse cases, failed tests, and runtime signals feed Auto-Learn and Auto-Improve backlogs. |

# 24. Change Log and Next Recommended Document
| Version | Date | Summary |
| --- | --- | --- |
| v1.0 | 2026-06-18 | Initial AIRA Policy-as-Code Implementation Standard covering OPA/Rego, Conftest, SBAC, CI/CD gates, runtime decisions, AI/tool action policies, decision evidence, waivers, and AVCI controls. |

Next recommended document: AIRA Evidence Manifest Schema and Evidence Pack Data Model v1.0. This will define machine-readable evidence pack schemas used by CI/CD, policy decisions, GitNexus, PR/MR gates, production readiness reviews, Resilience Lab, and audit traceability.

