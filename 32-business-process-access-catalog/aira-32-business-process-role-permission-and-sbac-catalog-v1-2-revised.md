---
title: "Business Process Role Permission and SBAC Catalog"
doc_id: "AIRA-32"
version: "v1.2"
status: "revised"
category: "Business process and access catalog"
source_docx: "AIRA_32_Business_Process_Role_Permission_and_SBAC_Catalog_v1.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 32-business-process-access-catalog
  - revised
  - aira-32
---



# Business Process Role Permission and SBAC Catalog



AIRA

AI-Native Enterprise Platform

Business Process, Role, Permission, and SBAC Catalog

v1.2 Revised

Business Process Authority | RBAC / ABAC / SBAC | OPA Policy-as-Code | Dynamic Workspace and MicroFunction Binding | AVCI Evidence
| Property | Value |
| --- | --- |
| Document ID | AIRA-DOC-032 |
| Canonical Filename | AIRA_32_Business_Process_Role_Permission_and_SBAC_Catalog_v1.2_Revised.docx |
| Version | v1.2 - Dynamic Workspace, MicroFunction, AI Agent, DevSecOps Evidence, and Access Assurance Update |
| Supersedes | 32-AIRA_Business_Process_Role_Permission_and_SBAC_Catalog_v1.1_Aligned.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | DRAFT FOR ARCHITECTURE REVIEW BOARD / SECURITY GOVERNANCE / CAB APPROVAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Security Architecture; Business Process Owners; Product Owner; DevSecOps Lead; Software Development Lead; QA/SDET; Data Governance; SRE; AI Governance; Internal Audit |
| Review Cadence | Quarterly; unscheduled on business-process, role, skill, permission, SoD, OPA/SBAC, Dynamic Workspace, MicroFunction, AI-agent, or production access change |
| Evidence Path | OpenKM Tier-0 / AIRA / Registers / Business-Process-Role-Permission-SBAC / v1.2/ |

Discipline First - Automation Second - Intelligence Third - AVCI Always

# Mandatory Practice Statement

No AIRA business process, role, permission, skill, approval authority, service account, Dynamic Workspace action, MicroFunction transaction, API endpoint, event topic, AI-agent tool action, or privileged operation may be implemented unless it is cataloged, classified, owned, least-privilege mapped, checked for separation of duties, governed by OPA/SBAC policy, tested through CI/CD gates, observable, auditable, reversible where applicable, and evidenced through the approved access-control lifecycle. Access is not a convenience setting. It is a governed engineering artifact and a runtime control surface.

# Static Table of Contents

1. Executive Summary and v1.2 Update Verdict

2. Purpose, Scope, and Authority

3. Catalog Authority Model and Non-Negotiable Rules

4. Business Process, Role, Permission, and Skill Taxonomy

5. Dynamic Workspace and MicroFunction Authorization Binding

6. API, Event, Data, and Workflow Permission Model

7. OPA/SBAC Decision Inputs and Policy-as-Code Requirements

8. Access Request, Review, Recertification, and JML Controls

9. AI Agent and Progressive Autonomy Controls

10. DevSecOps, Testing, DAST, GitNexus, and Fitness Gates

11. Evidence, Audit, Dashboards, and Runtime Toggle Controls

12. RACI, Roadmap, Acceptance Criteria, and AVCI Summary

# 1. Executive Summary and v1.2 Update Verdict

AIRA-DOC-032 defines the authoritative operating catalog for business processes, roles, permissions, skills, approval authority, separation-of-duties rules, and SBAC enforcement. Version 1.2 updates the catalog so it can serve as the access-control backbone for the revised Greenfield Environment, workstation setup, Sprint 0, CI/CD evidence, PoC 2 system factory, observability, operations, recovery, release/CAB, UAT, business training, and audit documents.
| v1.2 Alignment Area | Required Result |
| --- | --- |
| Dynamic Workspace | Every visible screen, component, menu, widget action, AI panel action, layout edit, and admin-builder function must map to a cataloged capability and OPA/SBAC decision. Frontend state is never authority. |
| MicroFunction Runtime | Every transaction and step requiring protected action must declare capability_code, required_role, required_skill, classification ceiling, SoD rule, idempotency profile, and evidence profile. |
| API and Eventing | OpenAPI operations, AsyncAPI channels, Kafka topics, Avro schemas, CloudEvents types, outbox/inbox processing, DLQ, replay, and administrative operations require cataloged permissions and skills. |
| DevSecOps and Evidence | CI/CD must test policy bundles, SoD paths, role/skill seed data, migration evidence, DAST role coverage, secrets hygiene, GitNexus impact, and PR/MR AVCI summaries. |
| AI Governance | AI agents receive skills, tools, model routes, memory eligibility, and autonomy tier only through registry-backed, policy-approved, evidence-producing controls. |
| Operations and Audit | Access changes, exceptions, denials, recertifications, break-glass actions, runtime toggles, and Auto-Heal candidates must be reconstructable through audit, Zammad, traces, dashboards, and evidence packs. |

# 2. Purpose, Scope, and Authority
| Area | In Scope | Out of Scope |
| --- | --- | --- |
| Business access model | Business process catalog, role catalog, permission catalog, skill catalog, approval authority, SoD rules, access reviews, recertification, and access evidence. | Unmanaged spreadsheets, local-only access lists, informal privilege grants, or direct database/security changes outside approved lifecycle. |
| Runtime enforcement | Keycloak/AD groups, OPA/Rego decisions, SBAC skills, Dynamic Workspace filtering, MicroFunction capability checks, API gateway enforcement, audit, and denial evidence. | Frontend-only authorization, hardcoded authorization in controllers, bypass flags, or stale policy caches treated as authority. |
| AI and automation | AI-agent skill mapping, tool authorization, autonomy ceiling, model-route eligibility, human approval rules, and action evidence. | Autonomous approval, self-granted permissions, direct production credentials, direct model-provider calls, or unregistered tools. |
| Change lifecycle | Git-managed catalogs, Flyway seed data, CI/CD validation, CAB/ARB approvals, audit testing, and rollback/disablement. | Manual production edits, untracked role changes, policy weakening without ADR/TDL, or emergency changes without after-action evidence. |
| Authority Level | Source | Rule |
| --- | --- | --- |
| L0 | ARB / CAB / Security Governance / Executive Risk | Final authority for production-impacting access, privileged actions, SoD exceptions, and break-glass acceptance. |
| L1 | 01 AVCI; 01A EDP; 02 Blueprint; 17 Security; 30/30A Change | Universal governance for evidence, architecture, security, least privilege, promotion, rollback, and human approval. |
| L2 | This AIRA-DOC-032 Standard | Canonical catalog authority for business process, role, permission, skill, approval, SoD, and SBAC controls. |
| L3 | Keycloak/AD, OPA bundles, PostgreSQL/Flyway seed data, OpenAPI/AsyncAPI contracts, Dynamic Workspace config, MicroFunction catalog | Executable implementation controls that enforce this standard. |
| L4 | Zammad tickets, access reviews, audit records, CI/CD evidence, GitNexus reports, dashboards | Operational proof and improvement input. |

# 3. Catalog Authority Model and Non-Negotiable Rules

The catalog is the authoritative design source for who may do what, under which business process, data class, environment, tenant/unit, approval route, and evidence path.

RBAC remains a coarse grouping mechanism; ABAC adds context; SBAC gates actual capability; OPA makes policy decisions; audit/evidence proves the outcome.

No protected Dynamic Workspace component, MicroFunction, API, event consumer, workflow transition, data operation, AI tool action, runtime toggle, or replay action may exist without a capability code and policy binding.

Default posture is deny. Unknown role, missing skill, expired skill, stale policy, missing classification, missing owner, missing evidence, or unresolved SoD conflict blocks or escalates the action.

Catalog records are configuration artifacts. They are Git-managed, versioned, reviewed, tested, migrated through Flyway where database seed data is required, and promoted through CAB/ARB gates when production-impacting.
| Rule ID | Non-Negotiable Rule | Evidence Required |
| --- | --- | --- |
| SBAC-01 | Role is not enough for protected action; active skill and policy context are required. | OPA decision log; skill grant record; access review. |
| SBAC-02 | A requester must not approve the same high-risk request, workflow, deployment, unlock, exception, or access grant. | SoD matrix test; approval workflow evidence. |
| SBAC-03 | Privileged or Restricted-data access must be time-bound, scope-bound, reason-bound, and reviewable. | Zammad request; approval; expiration; audit trail. |
| SBAC-04 | Policy cache or runtime configuration failure must fail closed for protected actions. | Fail-closed test; incident/runbook evidence. |
| SBAC-05 | Emergency access is break-glass only: time-bound, monitored, logged, and reviewed after use. | Break-glass record; trace; RCA/CAPA if applicable. |

# 4. Business Process, Role, Permission, and Skill Taxonomy
| Catalog Domain | Mandatory Fields | Owner |
| --- | --- | --- |
| Business Process | process_code, process_name, bounded_context, business_owner, classification, supported_channels, related_workflows, key risks, evidence_path | Business Process Owner / Product Owner |
| Role | role_code, role_name, intended persona, default environment, tenant/unit scope, allowed process families, incompatible roles | Business Owner + Security Architecture |
| Permission | permission_code, action_type, object/resource, API/event/UI binding, read/write/approve/admin/replay/toggle category, risk tier | Security Architecture + Service Owner |
| Skill | skill_code, skill_name, competency evidence, allowed tool/capability, trust threshold, certification requirement, expiration rule | Security Architecture + Skills Framework Owner |
| Approval Authority | authority_code, approval scope, monetary/risk/data threshold, SoD constraint, delegate rules, escalation path | Business Owner + CAB/ARB where applicable |
| Service / Agent Account | actor_id, owner, backup owner, credential_ref, allowed scopes, environment, rotation/recertification schedule, decommission evidence | Platform/Security + AI Governance for agents |
| Skill Family | Example Skills | Mandatory Boundary |
| --- | --- | --- |
| Business Processing | CASE_CREATE, CASE_UPDATE, MORTGAGE_REVIEW, KYC_REVIEW, PAYMENT_REVIEW | Requires process ownership, data-classification handling, audit, and UAT/business training evidence. |
| Approval and Override | APPROVE_WORKFLOW_TASK, APPROVE_EXCEPTION, APPROVE_UNLOCK, APPROVE_RELEASE | Requires maker-checker separation, reason code, traceability, and no self-approval. |
| DevSecOps | PIPELINE_RUN, RELEASE_PREPARE, DEPLOY_REQUEST, EVIDENCE_PACK_REVIEW, GITNEXUS_ANALYZE | May request or prepare actions; production promotion requires CAB/ARB and CI/CD evidence. |
| Security and Access | ACCESS_GRANT_REVIEW, POLICY_UPDATE_DRAFT, OPA_BUNDLE_REVIEW, SECRETS_REFERENCE_USE | No raw secrets; policy change requires tests, reviewer, and rollback. |
| Operations and Recovery | RUNBOOK_EXECUTE, DLQ_REPLAY_REQUEST, OUTBOX_REPAIR_REQUEST, TELEMETRY_TOGGLE_REQUEST | High-risk operations are time-bound, monitored, reversible, and evidence-producing. |
| AI and System Builder | AGENT_DRAFT, MODEL_ROUTE_REQUEST, TOOL_ACTION_REQUEST, MEMORY_WRITE_REQUEST | Advisory or candidate only unless registry, certification, SBAC, OPA, guardrails, and human approval pass. |

# 5. Dynamic Workspace and MicroFunction Authorization Binding

Dynamic Workspace rule: the frontend may display, hide, filter, route, and request actions, but it does not authorize business action. Authorization is decided by backend policy using cataloged capability, actor, role, skill, tenant/unit, environment, data classification, object state, workflow state, and evidence context.
| Workspace Element | Catalog Binding | Required Enforcement |
| --- | --- | --- |
| Workspace / screen | workspace_code, screen_code, role visibility, skill visibility, data class, tenant/unit scope | Resolver calls OPA/SBAC before returning layout and component set. |
| Component / widget | component_key, capability_code, allowed actions, policy_ref, evidence_profile | Backend filters component and action capabilities; unauthorized controls are hidden or disabled with safe messaging. |
| Widget action | action_code, API operation, idempotency key requirement, MicroFunction transaction_code | API gateway and MicroFunction coordinator recheck policy; frontend claim is ignored. |
| Admin Builder action | template publish, rollback, retire, layout default, configuration activation | Maker-checker, SoD, audit, versioning, rollback, and CAB/ARB gate where material. |
| AI Assistant action | prompt template, model route, retrieval eligibility, artifact type, tool action boundary | LiteLLM/guardrails/SBAC/OPA enforce classification and action boundary; high-risk output stays candidate. |
| MicroFunction Binding Field | Requirement |
| --- | --- |
| transaction_code | Stable identifier for protected transaction, e.g., AUTH_LOGIN_CONTEXT_ESTABLISH, CASE_APPROVAL_ROUTE, DLQ_REPLAY_REQUEST. |
| step_code / step_category | Standard step, business step, policy step, audit step, event step, or compensation step. |
| capability_code | Permission/skill bridge used by OPA/SBAC, audit, dashboard, and UAT evidence. |
| required_skills | One or more active skills with optional trust tier, certification, expiration, and environment scope. |
| classification_ceiling | Highest data class the transaction/step may access, display, emit, prompt, cache, or index. |
| sod_profile | Self-approval, maker/checker, deployer/approver, requester/fulfiller, and auditor separation rule. |
| evidence_profile | Trace, audit, policy decision, idempotency, test, and release evidence required for the action. |

# 6. API, Event, Data, and Workflow Permission Model
| Surface | Permission/Skill Requirement | Special Controls |
| --- | --- | --- |
| OpenAPI REST operation | operationId must map to permission_code and capability_code; mutating operations require idempotency profile and audit profile. | Contract tests, authorization negative tests, authenticated DAST role coverage, safe errors. |
| AsyncAPI / Kafka topic | Publish/consume/replay permissions must be separated; topic, schema, event type, and consumer group require owner and classification. | Avro compatibility, CloudEvents fields, DLQ/retry/replay approvals, idempotent consumer tests. |
| Outbox / inbox | Repair, re-drive, purge, or replay must be privileged operations with skill and approval matrix. | Replay evidence, duplicate-safety evidence, trace reconstruction. |
| Database / Flyway | DDL, seed data, RLS, role grants, policy seed changes, and reference data changes require DBA/security review. | No manual production DDL; migration evidence; rollback/forward-fix plan. |
| Workflow task | Claim, assign, approve, delegate, escalate, override, cancel, compensate require distinct permissions and SoD rules. | Flowable/Temporal audit, task history, maker-checker evidence, queue ownership. |
| Runtime toggle | Access-affecting, telemetry, feature, route, or diagnostic toggle requires owner, expiry, environment, and audit. | Default-safe values, no security weakening without CAB/security approval. |

# 7. OPA/SBAC Decision Inputs and Policy-as-Code Requirements

OPA policy inputs must include actor identity, actor type, tenant/unit, role, active skills, trust/certification state, environment, action, resource, classification, workflow state, request source, evidence reference, and requested autonomy risk tier where applicable.

Policy bundles must be versioned, tested, signed or checksum-verified, promoted through CI/CD, and associated with a rollback or previous-known-good policy version.

OPA denial is not an error to hide; denial reason, policy_ref, decision_id, safe user message, and evidence_ref must be logged without exposing sensitive data.

Policy-as-code must cover positive tests, negative tests, expired skills, stale certification, missing classification, SoD conflicts, break-glass expiration, replay abuse, and unknown policy cache.
| Decision Result | Required Treatment |
| --- | --- |
| allow | Execute only within granted scope; emit policy_decision_id, trace_id, audit_id, evidence_ref. |
| deny | Return safe denial; do not reveal sensitive internal reason; record policy_ref and reason_code. |
| filter | Remove unauthorized fields, rows, buttons, widgets, layout blocks, or evidence references before display. |
| require_approval | Route to maker-checker, workflow approval, Security/ARB/CAB, or business owner approval. |
| step_up | Require stronger assurance such as MFA, privileged approval, reauthentication, or restricted session. |
| break_glass_only | Block normal path; require emergency record, time-bound grant, monitoring, and post-action review. |

# 8. Access Request, Review, Recertification, and JML Controls
| Lifecycle Stage | Required Controls | Evidence |
| --- | --- | --- |
| Joiner | Role, business process, unit, skills, training prerequisites, classification acknowledgement, default-deny baseline. | Onboarding ticket; approvals; training completion; access grant record. |
| Mover | Old role/skills reviewed before new skills activated; incompatible roles removed; SoD rechecked. | Mover ticket; delta review; revocation proof; new approval. |
| Leaver | Access revoked or disabled; service/agent ownership transferred or suspended; credentials invalidated. | Leaver checklist; deprovision evidence; orphan scan. |
| Periodic recertification | Role owner, skill owner, business owner, security, and audit review based on risk tier. | Access review campaign; exceptions; remediation closure. |
| Emergency access | Time-bound, monitored, reason-coded, ticketed, and reviewed after use. | Break-glass approval; trace/audit; post-action review. |
| Service/agent account review | Owner, backup owner, credential_ref, rotation, scopes, classification, environment, and tool grants reviewed. | Credential review; denial test; decommission proof. |

# 9. AI Agent and Progressive Autonomy Controls
| Autonomy Tier | Access Treatment |
| --- | --- |
| T0 Advisory | May explain, summarize, classify, or draft from approved sources; no mutation. Requires classification and citation/evidence. |
| T1 Read-only | May read approved knowledge/evidence/code/log sources only with SBAC read skill and retrieval eligibility. |
| T2 Candidate generation | May generate candidate code/config/policy/test/runbook/document in branch/sandbox; no activation. |
| T3 Tool action request | May request Harness/MCP tool action after OPA/SBAC, tool manifest, dry-run where feasible, and human approval where required. |
| T4 Limited reversible action | Only explicit, certified, low-risk, reversible, time-bound, monitored actions in approved environment. |
| T5 Human-controlled/prohibited | Production secret, legal/financial, destructive, irreversible, policy approval, CAB approval, privileged unlock, or production deployment remains human-controlled. |

No agent receives permissions directly through code, prompt text, memory, local files, or hidden tool configuration. Permissions come from the registry, SBAC catalog, tool manifest, model route policy, guardrails, and OPA decision path.

Agent skill grants require owner, backup owner, purpose, allowed tools, classification ceiling, model-route eligibility, test evidence, red-team/certification evidence where applicable, and expiry.

Agent output that changes access, policy, prompt, guardrail, model route, runtime configuration, database seed data, or workflow authority remains candidate until human review and promotion evidence pass.

# 10. DevSecOps, Testing, DAST, GitNexus, and Fitness Gates
| Gate | Minimum Required Evidence |
| --- | --- |
| Catalog lint | Unique codes; valid owners; valid classifications; no orphan permissions; no missing expiry for high-risk skills. |
| OPA policy tests | Positive/negative tests; missing-skill denial; expired skill denial; SoD conflict; stale policy; break-glass expiry. |
| Contract tests | OpenAPI/AsyncAPI operation-to-permission mapping; safe error; unauthorized/forbidden behavior. |
| Authenticated DAST | Synthetic users representing roles/skills; tests for horizontal/vertical privilege escalation, IDOR, admin bypass, hidden endpoints, and unsafe direct object access. |
| Architecture fitness | No controller hardcoded roles; no frontend authority; no direct DB privilege decision; no bypass flag; no direct model-provider action authority. |
| GitNexus impact | Changed files, affected policies, affected APIs/events, affected MicroFunctions, affected tests, ownership and blast-radius summary. |
| Evidence pack | PR/MR AVCI summary; role/skill/policy diff; tests/scans; approval; rollback/disablement plan; known limitations. |

# 11. Evidence, Audit, Dashboards, and Runtime Toggle Controls
| Evidence Type | Required Fields |
| --- | --- |
| Access decision | actor_hash, actor_type, role, active_skills, action, resource, policy_ref, decision, reason_code, trace_id, evidence_ref, classification. |
| Catalog change | change_id, source_ref, owner, maker, checker, approver, diff_summary, affected_roles, affected_permissions, affected_skills, rollback. |
| Recertification | campaign_id, reviewer, role/skill/account, result, exception, remediation_due, closure_evidence. |
| Runtime toggle | toggle_code, owner, reason, environment, default value, new value, expiry, risk, approval, audit, rollback. |
| Break-glass | incident/change/ticket, approver, affected actor, privilege, duration, monitoring, post-review result. |
| Auto-Heal / Auto-Learn / Auto-Improve | trigger, evidence retrieved, proposed access/policy change, tests, risk classification, human approval, PR/MR or backlog item. |

Dashboards must show denied actions, elevated access, expired skills, pending recertifications, SoD exceptions, break-glass use, policy bundle version, stale cache, and high-risk AI-agent tool requests.

Forbidden evidence fields include passwords, tokens, raw JWTs, secrets, private keys, raw Restricted data, unnecessary PII, raw prompts containing Confidential/Restricted data, and unredacted customer payloads.

Runtime toggles may adjust diagnostic verbosity, policy-cache refresh behavior, workspace visibility experimentation in non-production, and temporary evidence capture levels only when governed. They must not silently weaken least privilege, SoD, encryption, audit, or policy enforcement.

# 12. RACI, Roadmap, Acceptance Criteria, and AVCI Summary
| Activity | Business Owner | Security | DevSecOps | Developer | QA/SDET | Internal Audit |
| --- | --- | --- | --- | --- | --- | --- |
| Define business process and role intent | A | C | I | C | C | I |
| Define permissions, skills, SoD, and approval rules | C | A | C | C | C | C |
| Implement policy, seed data, and runtime binding | C | C | A | R | C | I |
| Test access, policy, DAST, and fitness gates | I | C | C | R | A/R | C |
| Approve production-impacting access model change | A | A | C | I | C | C |
| Perform recertification and audit testing | C | R | I | I | C | A/R |
| Roadmap Step | Exit Criteria |
| --- | --- |
| 1. Normalize catalog schema | Business process, role, permission, skill, approval authority, SoD, and evidence schema approved. |
| 2. Seed foundation access data | Initial foundation roles, skills, and policies delivered through Git/Flyway and verified in CI. |
| 3. Bind workspace and MicroFunction capabilities | Dynamic Workspace components and MicroFunction transactions resolve capability_code and OPA/SBAC decisions. |
| 4. Add API/event/workflow coverage | OpenAPI/AsyncAPI/workflow/replay/toggle operations mapped to permissions and tested. |
| 5. Enable reviews and dashboards | Recertification workflow, audit dashboard, denial dashboard, SoD exceptions, and evidence views operational. |
| 6. Extend to AI agents | Agent skills, autonomy tiers, tool grants, model routes, and action evidence integrated with registry and OPA. |
| Acceptance Criterion | Required Condition |
| --- | --- |
| Least privilege | Every protected action maps to business process, permission, skill, classification, owner, and policy decision. |
| Fail closed | Unknown/missing/stale role, skill, policy, classification, owner, evidence, or approval blocks protected action. |
| SoD enforcement | Maker/checker, requester/approver, deployer/approver, and auditor separation rules are tested. |
| Dynamic Workspace safety | Unauthorized components/actions are filtered by backend policy and rechecked on action execution. |
| MicroFunction/API/event coverage | MicroFunction transactions, OpenAPI operations, AsyncAPI channels, Kafka topics, DLQ/replay, and toggles have catalog bindings. |
| Audit and recertification | Access changes, decisions, exceptions, reviews, and break-glass actions are reconstructable from evidence. |
| AI governance | AI-agent privileges remain registry-backed, tiered, reversible, evidence-producing, and human-governed where required. |
| AVCI Property | Compliance Evidence |
| --- | --- |
| Attributable | Defines accountable owners, co-owners, business owners, security owners, reviewers, approvers, service owners, agent owners, and evidence paths for cataloged access. |
| Verifiable | Requires OPA tests, policy decisions, CI/CD gates, DAST role coverage, access reviews, recertification, dashboards, GitNexus impact, and audit evidence. |
| Classifiable | Requires classification for processes, roles, permissions, skills, workspace components, MicroFunctions, APIs, events, evidence, prompts, and AI-agent scopes. |
| Improvable | Converts denials, access review findings, SoD exceptions, incidents, DAST findings, audit findings, and Auto-Heal candidates into controlled backlog and policy improvements. |

# Appendix A. External Reference Baseline
| Reference | Use in This Standard |
| --- | --- |
| NIST SP 800-218 Secure Software Development Framework (SSDF) | Secure development, verification, evidence, and vulnerability response discipline. |
| OWASP Application Security Verification Standard 5.0.0 | Access control, authentication, session, API, and secure configuration verification expectations. |
| OpenTelemetry Semantic Conventions | Consistent naming and correlation for access, policy, API, service, and runtime telemetry. |
| SLSA v1.2 | Supply-chain provenance, build integrity, and attestation alignment for access-control artifacts and policy bundles. |

