---
title: "AI Agent Identity Lifecycle and Credential Hygiene Standard"
doc_id: "AIRA-42D"
version: "v1.3"
status: "revised"
category: "AI governance and agent control"
source_docx: "AIRA_42D_AI_Agent_Identity_Lifecycle_and_Credential_Hygiene_Standard_v1.3_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 42-ai-governance-agent-control
  - revised
  - aira-42d
---



# AI Agent Identity Lifecycle and Credential Hygiene Standard



AIRA
AI-Native Enterprise Platform

AI Agent Identity Lifecycle and Credential Hygiene Standard

v1.3 Revised - JML, Recertification, Registry, Runtime Assurance, and System Builder Alignment

Mandatory Practice Statement: No AIRA AI agent, System Builder agent, tool-using assistant, workflow automation agent, or AI-assisted runtime capability may be proposed, activated, delegated, certified, promoted, recertified, or retired unless its identity, owner, backup owner, classification ceiling, credentials, SBAC scope, OPA policy bindings, tool grants, model-route eligibility, guardrails, runtime evidence, and decommission path are registered, current, reviewable, fail-closed, and AVCI-complete.
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-042D |
| Canonical Filename | 42D-AIRA_AI_Agent_Identity_Lifecycle_and_Credential_Hygiene_Standard_v1.3_Revised.docx |
| Version | v1.3 Revised |
| Supersedes | 42D v1.2 JML and Recertification Automation Update |
| Status | Draft for Architecture, Security, AI Governance, DevSecOps, Platform Engineering, Data Governance, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | AI Governance; Security Architecture; DevSecOps Lead; Platform Engineering; Software Development Lead; SRE / Operations; DBA; QA/SDET; Internal Audit |
| Primary Parent | 42-AIRA AI Governance and Runtime Control Standard |
| Direct Companions | 42E Runtime Security Control Plane; 42F Autonomy Calibration; 42G Threat Model; 42H Tool/MCP Gateway; 42I Memory/RAG Integrity; 42J Certification; 42K Incident Response; 42N OPA/SBAC Rule Catalog; 42O Registry Schema; 44C Agent Inventory |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / AI-Governance / Agent-Identity-Lifecycle / v1.3/ |
| Review Cadence | Monthly during PoC and pilot rollout; quarterly after stabilization; immediate on owner, credential, tool, model-route, policy, runtime, incident, or registry change |

# 1. Executive Summary

This v1.3 revision strengthens AIRA-DOC-042D by aligning AI agent identity lifecycle and credential hygiene with the revised System Builder, Dynamic Workspace, registry, DevSecOps, observability, security, database, and change-control standards. It preserves the v1.2 Joiner/Mover/Leaver and automated recertification model while making registry-backed enforcement, runtime assurance, and evidence reconstruction mandatory.

The operating rule is simple: no owner, no agent; no current recertification, no privileged access; no credential proof, no tool action; no policy evidence, no promotion; no decommission denial test, no retirement closure.
| Strategic Outcome | v1.3 Required Result |
| --- | --- |
| No orphaned agents | Each agent has current owner, backup owner, authority scope, review cadence, and JML evidence. |
| Credential hygiene by construction | Credential references, leases, rotation dates, revocation tests, and exception records are controlled and evidence-backed. |
| Registry-backed authority | Agent identity and lifecycle state are authoritative only when recorded in the runtime registry and linked evidence. |
| Fail-closed runtime | Unknown owner, expired review, stale credential, missing policy, or incomplete evidence restricts, suspends, revokes, or escalates. |
| Traceable improvement | Incidents, policy denials, runtime anomalies, audit findings, and recertification gaps feed governed Auto-Heal, Auto-Learn, and Auto-Improve proposals only. |

# 2. v1.3 Update Verdict
| Control Area | Verdict | Required Treatment |
| --- | --- | --- |
| 42D v1.2 JML baseline | Retained and strengthened | Owner, backup owner, mover/leaver, inactive owner, delegated approver, and recertification triggers remain mandatory. |
| 42O registry integration | Added | Agent identity, lifecycle, credentials, SBAC grants, model routes, memory eligibility, runtime events, and evidence links must be registry-backed. |
| 44C inventory alignment | Added | Agent inventory views must show identity, owner, status, trust tier, review due, tool grants, model routes, and evidence references. |
| System Builder lifecycle | Strengthened | System Builder may draft or propose agent identity changes but must not activate, approve, revoke, or promote agents without governed workflow. |
| Dynamic Workspace admin screens | Added | UI may display and request actions only; backend policy, registry, workflow, and evidence decide. |
| Credential and secrets hygiene | Strengthened | No raw secrets in prompts, logs, migrations, seed data, tests, screenshots, evidence, or LLM indexes. |
| Runtime telemetry toggles | Added | Debug, trace, or audit verbosity may be changed only through policy-governed, classified, reversible, and audited configuration. |
| Auto loops | Clarified | Auto-Heal, Auto-Learn, and Auto-Improve may detect and propose; they cannot self-approve identity, credential, tool, or route changes. |

# 3. Purpose, Scope, and Authority

## 3.1 Purpose

Define the mandatory identity lifecycle for all AIRA AI agents, System Builder agents, coding agents, operational agents, Dynamic Workspace assistant agents, and environment-provisioning agents.

Prevent orphaned ownership, stale credentials, shared secrets, unreviewed tool grants, unapproved model routes, and unmanaged delegated authority.

Define JML, recertification, credential hygiene, registry, OPA/SBAC, dashboard, evidence, and decommission controls.

Ensure every agent remains attributable, verifiable, classifiable, improvable, secure, observable, reversible, and fail-closed.

## 3.2 Scope
| In Scope | Out of Scope / Prohibited |
| --- | --- |
| Agent identity, owner, backup owner, lifecycle state, credential references, SBAC grants, model routes, guardrails, tools, memory eligibility, recertification, suspension, revocation, retirement, and evidence. | Unregistered agents, shadow scripts, personal AI accounts, direct provider SDK calls, direct production credentials, shared secrets, self-approval, and unmanaged tool execution. |
| System Builder candidate agent definitions, agent update proposals, environment-provisioning agents, repository/coding agents, evidence agents, security agents, and Dynamic Workspace assistants. | AI approval of its own output, silent production mutation, bypass of CAB/ARB/OPA/SBAC/Harness, or activation outside the agent registry and approval workflow. |

## 3.3 Authority and Precedence
| Level | Authority | Role |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance / AI Governance | Final authority for production-impacting agent identity, credential, access, autonomy, and exception decisions. |
| L1 | 01 AVCI, 01A EDP/SOLID, 17 Security, 20 CI/CD, 30/30A Change, 31A Observability, 42 AI Governance | Universal governance, evidence, security, promotion, observability, rollback, and AI control authority. |
| L2 | This 42D Standard | Authoritative rule set for AI agent identity lifecycle, ownership, credential hygiene, JML, recertification, and orphaned-access prevention. |
| L3 | 42E-42N, 42O registry, 44C inventory, 44A implementation guide | Executable runtime, autonomy, tool, memory, certification, incident, policy, registry, and lifecycle companion controls. |
| L4 | Registry rows, OPA decisions, tool manifests, model-route records, audit events, evidence packs, tickets, PR/MR records | Operational proof and improvement input. |

# 4. Governing Source Baseline and Conflict Rule

This document is governed by the active AIRA canonical baseline and must be interpreted with the stricter control when source overlap exists. Known overlap between 41B and 44 System Builder sources, and between 42D/42E/42F/42H/42O registry controls, must be tracked through the reconciliation register and must not be silently normalized in implementation.
| Source Family | Required 42D Treatment |
| --- | --- |
| 42D v1.2 | Retain JML, recertification automation, owner/backup owner, credential rotation, OPA input, evidence template, and fail-closed rules. |
| 42E Runtime Security | Expose identity, credential, recertification, anomaly, tripwire, and dashboard signals for assurance. |
| 42F Autonomy | Identity and recertification state determine whether action tier remains advisory, read-only, candidate-generation, tool-request, or blocked. |
| 42G Threat Model | Map identity/credential sprawl, shadow agents, token replay, model-route bypass, and orphaned access to controls and tests. |
| 42H Tool/MCP Gateway | Tool grants require current identity, owner review, credential hygiene, idempotency, dry-run, approval, and rollback evidence. |
| 42O Registry | PostgreSQL/Flyway registry records are authoritative; dashboards, caches, summaries, and LLM narratives are derivative. |
| 44C Agent Inventory | Admin inventory and assurance screens display policy-filtered identity and lifecycle data, but cannot become authority. |

# 5. Agent Identity Lifecycle Model

The lifecycle state is assigned per agent version and enforced before every protected action. State transitions require owner, checker, policy decision, evidence reference, and rollback or decommission path.
| State | Entry Criteria | Allowed Actions | Exit Criteria / Control |
| --- | --- | --- | --- |
| Proposed | Need identified; accountable owner named; preliminary classification and risk tier recorded. | Draft purpose, non-goals, skills, tool needs, model route, and evidence plan. | Move to Designed only after identity record and owner acceptance are complete. |
| Designed | Definition, SBAC scope, tool/model/memory boundaries, credential pattern, guardrails, and tests drafted. | Threat-model, simulate, prepare contracts, policies, and evaluation plans. | Move to Sandbox after Security, AI Governance, and owner review. |
| Sandbox | Non-production approval; synthetic data; read-only tools by default. | Run evaluations, guardrail tests, blocked-action tests, and evidence generation. | Move to Pilot only when identity, credential, policy, and certification evidence pass. |
| Pilot | Scoped users, scoped data, strict monitoring, rollback and suspension ready. | Operate within pilot scope with manual review and dashboard monitoring. | Move to Active only after CAB/ARB or delegated approval. |
| Active | Approved scope, current owner, current credential, current policy, current certification, and complete evidence. | Operate only within approved skills, routes, tools, environment, and autonomy tier. | Remain active only through periodic and event-based recertification. |
| Restricted | Review, credential, policy, evidence, or risk condition requires reduced capability. | Advisory, read-only, or reduced-scope actions only. | Return to Active after remediation or move to Suspended/Revoked/Retired. |
| Suspended | Incident, stale owner, overdue review, failed evaluation, expired credential, or policy violation. | Protected actions blocked; evidence preserved; remediation workflow only. | Revalidate, revoke, or retire. |
| Revoked | Critical credential, identity, policy, security, or unauthorized-access condition. | No execution, model route, tool, memory, or dashboard privileged action. | Recreate only through new lifecycle approval. |
| Retired | No business purpose, superseded, unowned, or permanently decommissioned. | No runtime action; archival and denial tests only. | Closure requires route removal, credential revocation, tool denial, memory quarantine, and evidence archive. |

# 6. JML and Delegated Authority Controls

JML applies to the human owner, backup owner, technical owner, delegated approver, checker, operator, and any service account or workload identity holder associated with the agent.
| JML Event | Trigger | Mandatory Control | Evidence |
| --- | --- | --- | --- |
| Joiner | New owner or backup owner assigned. | Validate identity, role, approval authority, training, classification eligibility, and acceptance of accountability. | Owner acceptance, SBAC record, training evidence, policy decision, register update. |
| Mover | Owner changes role, team, authority, manager, or risk responsibility. | Trigger recertification; suspend approval capability until authority scope is revalidated. | HR/IAM or CODEOWNERS change, review decision, updated authority scope. |
| Leaver | Owner or approver exits organization or loses employment relationship. | Notify backup owner; restrict immediately; reassign, suspend, revoke, or retire within SLA. | Exit event, restriction record, reassignment or retirement evidence, denial test. |
| Inactive Owner | Owner does not respond to review, dashboard action, or incident workflow. | Escalate; restrict privileged access; suspend when SLA expires. | Escalation ticket, notification evidence, restriction/suspension event. |
| Delegated Approver Change | Approver, checker, or delegated authority changes. | Revalidate separation of duties, Flowable tasks, approval thresholds, and policy bundle. | Workflow update, SoD test, OPA decision, approval-chain record. |
| Ownership Conflict | Multiple owners, unclear authority, or owner belongs to conflicting role. | Block promotion and route to AI Governance/Security/ARB. | Conflict record, decision log, remediation plan. |

# 7. Credential Hygiene and Secret Handling

AIRA agents do not own raw production secrets. Credentials must be represented by controlled references, workload identity, signed token leases, or approved secret-manager paths. Human users, agents, prompts, repositories, logs, tests, screenshots, migrations, evidence records, Obsidian, LLM Wiki, and GitNexus reports must not contain raw secrets.
| Credential Surface | Required Control | Reject / Block Condition |
| --- | --- | --- |
| Workload identity | Use approved identity provider, SPIFFE/SVID or equivalent pattern where adopted, and short-lived tokens. | Static personal token, shared credential, unmanaged service account, or unclear owner. |
| Vault/OpenBao references | Store only logical reference, lease metadata, TTL, rotation due date, and revocation evidence in registry. | Raw secret value in registry, seed data, prompt, log, or evidence. |
| Model route credentials | Route through LiteLLM or approved gateway; bind route to classification, guardrails, owner, and policy. | Direct model-provider SDK call, unmanaged key, route mismatch, or guardrail unavailable. |
| Tool/MCP credentials | Tool actions go through Harness/MCP gateway with SBAC, OPA, dry-run where feasible, idempotency, and rollback. | Agent receives direct Git, CI/CD, Kubernetes, database, workflow, or production credential. |
| Rotation and revocation | Define rotation cadence, emergency rotation procedure, revocation test, and evidence reference. | Expired lease, unknown age, failed revocation test, or unapproved exception. |
| Exception handling | Time-bound, owner-approved, risk-accepted, monitored, and tracked through CAB/ARB/Security where needed. | Permanent exception, no owner, no expiry, no compensating control, or no evidence. |

# 8. Recertification Automation Model

Recertification automation is a governed control loop. It may collect evidence, calculate due dates, detect risk, restrict scope, suspend actions, and generate evidence. It must not silently approve high-risk access, expand authority, rotate production secrets without approval, or overrule Security, AI Governance, ARB, CAB, or owner decisions.
| Trigger Type | Examples | Expected Decision Path |
| --- | --- | --- |
| Time-based | Monthly during PoC/pilot; quarterly after maturity; shorter cadence for high-risk agents. | Review owner, backup owner, access, credential, model route, memory, certification, and runtime state. |
| Event-based | Owner JML event, tool grant change, model-route change, credential lease event, policy bundle update, CI/CD change. | Restrict affected capability until validation and evidence complete. |
| Risk-based | Trust downgrade, anomaly, policy denial spike, failed guardrail, memory poisoning signal, tool misuse pattern. | Escalate to Security/AI Governance and consider suspension or revocation. |
| Evidence-based | Missing evidence pack, expired certification, missing rollback, stale threat model, failed decommission denial test. | Block promotion and create remediation backlog. |
| Incident-based | 42K incident, suspected credential exposure, prompt injection, tool hijack, data leakage, or orphaned agent activity. | Incident response overrides normal recertification; containment first. |
| Recertification Type | Minimum Verification |
| --- | --- |
| Owner Recertification | Owner, backup owner, technical owner, checker, authority scope, SoD, review cadence, and acceptance evidence. |
| Access Recertification | SBAC skills, RBAC/ABAC claims, environment, repository, knowledge, API, Dynamic Workspace, and tool scope. |
| Credential Recertification | Credential reference, TTL, lease state, rotation, exception, revocation, and no raw-secret exposure. |
| Model Route Recertification | LiteLLM alias, classification ceiling, fallback, guardrail version, provider policy, cost/capacity signal. |
| Memory/RAG Recertification | Retrieval eligibility, source freshness, citation, quarantine, memory TTL, and memory write controls. |
| Runtime Recertification | 42E metrics, tripwire status, policy denial rates, incident state, rollback, and dashboard signal. |
| Certification Recertification | 42J red-team, evaluation, golden dataset, adversarial tests, blocked-action evidence, and expiry. |

# 9. Agent Registry and Schema-Ready Fields

The registry is the authoritative source for agent identity and lifecycle state. PostgreSQL/Flyway-governed registry rows are authoritative. Redis/Valkey, dashboards, reports, embeddings, Obsidian, LLM Wiki, and AI-generated narratives are derivative views.
| Field Group | Required Fields |
| --- | --- |
| Identity | agent_id, agent_version, agent_name, purpose, non_goals, lifecycle_state, status_reason, owner_user_id, backup_owner_user_id, technical_owner_id |
| Authority | classification_ceiling, risk_tier, autonomy_tier, owner_authority_scope, sbac_scope_ref, opa_policy_ref, separation_of_duties_ref |
| Credential | credential_ref, credential_type, lease_expiry, credential_last_rotated_at, credential_next_rotation_due, revocation_test_ref, exception_ref |
| Model and Guardrails | litellm_route_alias, direct_provider_sdk=false, guardrail_policy_ref, fallback_route_ref, model_route_status |
| Tool and MCP | tool_manifest_refs, allowed_actions, dry_run_required, idempotency_required, approval_rule_ref, rollback_method |
| Memory/RAG | context_source_refs, memory_write_eligibility, retrieval_policy_ref, freshness_state, quarantine_state |
| JML and Review | owner_status, backup_owner_status, jml_event_ref, review_due_at, recertification_state, recertification_decision, evidence_pack_ref |
| Telemetry and Evidence | run_id, trace_id, policy_decision_id, tool_action_id, evidence_ref, dashboard_signal_state, incident_ref, decommission_ref |

# 10. OPA / SBAC Decision Inputs and Fail-Closed Rules
| Condition | Required Decision |
| --- | --- |
| Unknown agent, unregistered agent, shadow agent, or missing lifecycle state | DENY and create security finding. |
| No current owner or unresolved leaver event | RESTRICT immediately; SUSPEND when SLA expires. |
| No backup owner for high-risk or production-impacting agent | RESTRICT privileged actions and open remediation. |
| Review overdue or certification expired | RESTRICT to advisory/read-only until recertification completes. |
| Credential expired, unknown, shared, or revocation test failed | DENY authentication/tool/model action; revoke stale reference. |
| Tool manifest missing or changed | DENY tool action until 42H authorization and tests pass. |
| Model route missing, route classification mismatch, or direct provider SDK detected | DENY model invocation and raise route-bypass finding. |
| Incident open or tripwire critical | 42K containment overrides normal action; SUSPEND or KILL SWITCH where required. |
| Evidence missing for promotion, trust increase, or decommission closure | BLOCK promotion or closure until evidence is complete. |

# 11. Dynamic Workspace, Admin Console, and System Builder Integration

Dynamic Workspace and System Builder interfaces must never become identity authority. They may collect requests, display policy-filtered registry data, generate candidate artifacts, and route review workflows, but backend registry, OPA/SBAC, workflow approval, and evidence decide protected actions.
| Interface | Allowed | Prohibited |
| --- | --- | --- |
| Agent Inventory Workspace | Search, view, filter, and display current policy-filtered identity and lifecycle records. | Activate, suspend, revoke, retire, or grant access through frontend state alone. |
| Agent Identity Card | Display owner, backup owner, lifecycle, credential status, route, tool grants, certification, and evidence. | Expose raw secrets, tokens, Restricted evidence, or hidden policy reasons to unauthorized users. |
| Recertification Queue | Route review tasks, collect attestations, show overdue status, and link evidence. | Self-approve by agent, bypass checker, or auto-approve high-risk access. |
| Credential Console | Display reference metadata, TTL, rotation due, exception status, and revocation evidence. | Display, copy, export, or prompt raw secrets. |
| System Builder | Draft agent definitions, OPA inputs, migration/API/test proposals, runbooks, and evidence checklists. | Directly create active agents, grant production tools, rotate secrets, approve change, or mutate production. |

# 12. Evidence, Observability, and Runtime Toggle Requirements
| Evidence Type | Required Records |
| --- | --- |
| JML Evidence | HR/IAM event, CODEOWNERS change, owner transfer, manual attestation, approval-chain update. |
| Ownership Evidence | Owner and backup owner acceptance, authority scope, review date, checker, and SoD evidence. |
| Access Evidence | SBAC skills, OPA decision, tool grants, repository scope, workspace access, model route, memory access. |
| Credential Evidence | Credential reference, TTL, rotation, exception, revocation test, no-secrets scan, Vault/OpenBao audit. |
| Runtime Evidence | agent_id, agent_version, run_id, trace_id, policy_decision_id, model route, guardrail result, tool_action_id, evidence_ref. |
| Toggle Evidence | Requested telemetry/debug toggle, owner, reason, classification, expiry, policy decision, rollback, and audit trail. |
| Closure Evidence | Restriction, suspension, revocation, retirement, denial test, memory quarantine, route removal, and archive record. |

Runtime logging, tracing, debug, model-route, workspace telemetry, and diagnostic toggles may be adjusted only through approved runtime configuration, policy checks, classification handling, audit, expiration, and rollback. Performance concerns may reduce sampling or verbosity; they must not disable mandatory security, audit, identity, policy, or evidence signals.

# 13. DevSecOps, Certification, and Release Gates

CI/CD must verify agent definition schemas, registry migrations, policy bundles, secrets scans, SBOM/provenance, architecture fitness, OPA tests, and evidence-pack completeness.

GitNexus may provide read-only derivative impact analysis for identity-related code, policy, configuration, migration, and agent changes; it cannot approve, merge, deploy, or mutate runtime state.

Authenticated DAST and negative authorization tests must prove suspended, revoked, retired, and unreviewed agents cannot authenticate, call tools, retrieve memory, invoke model routes, or access dashboards.

42J certification must include identity, credential, access, tool, memory, autonomy, observability, incident, kill-switch, revocation, and decommission denial tests.

CAB/ARB/Security/AI Governance approval is required for production-impacting, Restricted, high-risk, privileged, irreversible, or exception-based identity and credential changes.

# 14. Auto-Heal, Auto-Learn, and Auto-Improve Boundaries
| Loop | Allowed Behavior | Blocked Behavior |
| --- | --- | --- |
| Auto-Heal | Detect orphaned owner, expired credential, overdue review, failed policy, or dashboard anomaly; restrict/suspend where pre-approved; create ticket and evidence. | Silently approve access, expand SBAC scope, rotate production secrets without workflow, or reactivate an agent. |
| Auto-Learn | Summarize patterns from recertification failures, incidents, denials, review delays, and audit findings into reviewed knowledge. | Promote unreviewed lessons to canonical standards or retrieval-eligible knowledge. |
| Auto-Improve | Propose policy, dashboard, test, runbook, schema, or workflow improvements with measurable benefit and rollback path. | Apply production identity, credential, policy, model-route, or tool changes without human approval and evidence. |

# 15. RACI and Operating Responsibilities
| Role | Responsibilities |
| --- | --- |
| AI Governance | Own agent governance policy, lifecycle interpretation, trust criteria, and recertification cadence. |
| Security Architecture | Own credential hygiene, OPA/SBAC policy requirements, secrets controls, and incident escalation. |
| Agent Owner | Accept accountability, validate purpose/scope, complete recertification, approve remediation, and ensure retirement when needed. |
| Backup Owner | Act during owner absence, leaver event, incident, or overdue review; confirm continued accountability. |
| DevSecOps Lead | Implement CI/CD gates, policy tests, evidence pack, SBOM/provenance, GitNexus integration, and release checks. |
| Platform Engineering | Operate registry services, identity integrations, LiteLLM routes, Harness/MCP gateway, and secret-manager integrations. |
| QA/SDET | Run identity, credential, blocked-action, negative authorization, DAST, regression, and certification tests. |
| Internal Audit | Test evidence completeness, chain-of-custody, access recertification, and control operation effectiveness. |

# 16. Implementation Roadmap
| Phase | Focus | Exit Criteria |
| --- | --- | --- |
| 0 | Register v1.3 and reconciliation items | 42D v1.3 recorded; 42D/42E/42F/42H/42O/44C overlaps tracked in 00D. |
| 1 | Schema and contract alignment | Registry fields, OpenAPI/AsyncAPI events, OPA input schema, and dashboard signals drafted. |
| 2 | Policy and evidence implementation | OPA/SBAC tests, evidence templates, recertification records, and denial tests pass. |
| 3 | Dynamic Workspace admin integration | Agent inventory, identity card, recertification queue, and credential console are backend-governed and policy-filtered. |
| 4 | CI/CD and certification gates | SAST/SCA/secrets, architecture fitness, DAST, registry migration, and red-team evidence pass. |
| 5 | Pilot and assurance dashboard | Pilot agents show current owner, credential, review, route, tool, policy, runtime, and evidence state. |
| 6 | Production governance readiness | CAB/ARB/Security/AI Governance approve residual risk, rollback, incident, and decommission paths. |

# 17. Acceptance Criteria and Definition of Done

Every registered agent has owner, backup owner, technical owner, lifecycle state, classification ceiling, SBAC scope, OPA binding, model route, tool scope, credential reference, review due date, and evidence path.

No unregistered, retired, revoked, suspended, or stale-review agent can authenticate, invoke a model route, call a tool, retrieve memory, access Dynamic Workspace privileged screens, or perform protected actions.

JML events trigger recertification, restriction, suspension, reassignment, revocation, or retirement according to policy and SLA.

Credential rotation, TTL, lease state, revocation test, exception handling, and no-secret leakage checks are evidenced.

OPA/SBAC policies deny or escalate based on lifecycle, owner, backup owner, review due date, credential state, classification, tool risk, model route, and incident status.

Runtime telemetry emits agent_id, agent_version, run_id, trace_id, policy_decision_id, tool_action_id, model_route, guardrail_result, classification, and evidence_ref without leaking secrets or raw PII.

Dynamic Workspace and System Builder cannot activate, promote, suspend, revoke, retire, or grant access without backend registry, policy, workflow, and evidence decisions.

CI/CD evidence includes registry migration validation, policy tests, secrets scans, SAST/SCA, authenticated DAST, architecture fitness, GitNexus impact, SBOM/provenance, and rollback/decommission proof.

Auto-Heal, Auto-Learn, and Auto-Improve outputs remain proposal-driven and cannot self-approve identity, credential, access, tool, route, memory, or production changes.

# 18. Risks, Controls, and Reconciliation Items
| Risk | Severity | Required Control |
| --- | --- | --- |
| Agent remains active after owner leaves or changes role. | Critical | JML integration, backup owner, immediate restriction, recertification SLA, suspension/retirement path. |
| Credential rotation disconnected from owner review. | High | Credential recertification is mandatory sub-check of owner/access review. |
| System Builder creates or activates agents directly. | Critical | System Builder may draft only; activation requires registry workflow, policy, evidence, and approval. |
| Dashboard becomes authority. | High | Dashboard is derivative; PostgreSQL/Flyway registry and policy decisions are authoritative. |
| Secrets appear in prompts, logs, tests, screenshots, or evidence. | Critical | No raw secrets; redaction, secret scan, DLP, and incident response. |
| 42D/42E/42F/42H/42O/44C overlap causes inconsistent approval rules. | Medium | Record in 00D; stricter control governs until ARB resolves. |
| Automation silently approves access. | Critical | Automation may restrict/suspend and generate evidence; high-risk approval remains human-controlled. |

# 19. AVCI Compliance Summary
| AVCI Property | v1.3 Evidence Treatment |
| --- | --- |
| Attributable | Agent owner, backup owner, technical owner, reviewer, approver, credential owner, tool owner, model-route owner, policy owner, and recertification actor are recorded. |
| Verifiable | JML event evidence, registry record, access scan, credential rotation record, OPA decision, dashboard signal, denial test, CI/CD evidence, and recertification pack prove control operation. |
| Classifiable | Agent classification ceiling, data scope, tool scope, model route, memory/RAG access, evidence handling, telemetry, and owner authority are assessed during every review. |
| Improvable | Expired reviews, ownership gaps, credential findings, policy denials, incidents, audit findings, runtime anomalies, and certification failures feed governed improvement backlogs. |

# Appendix A. Recertification Evidence Template
| Field | Required Meaning |
| --- | --- |
| recertification_id | Unique review identifier. |
| agent_id / agent_version | Agent identity under review. |
| trigger_type / trigger_ref | Time, event, risk, evidence, incident, manual, HR/IAM, Git, CI, Vault, OPA, or LiteLLM trigger. |
| owner_user_id / backup_owner_user_id | Current accountable owners. |
| owner_status / backup_owner_status | active, moved, inactive, leaver, unknown. |
| classification_ceiling / requested_scope | Maximum classification and requested or current authority. |
| current_sbac / current_tools | Skills, tool grants, environment scope, repository scope, and allowed actions. |
| credential_status | Lease, rotation, exception, revocation test, and no-secret-leakage status. |
| model_route_status / guardrail_status | LiteLLM route, fallback, classification eligibility, and guardrail version. |
| memory_context_status | Source eligibility, freshness, quarantine, memory write status. |
| runtime_dashboard_status | 42E signal state and anomaly/tripwire status. |
| decision | approve, approve-with-remediation, restrict, suspend, revoke, retire, or escalate. |
| evidence_ref / next_review_due | Evidence pack path and next required review date. |

# Appendix B. Copy-Ready Review Prompt

Act as an AIRA AI Governance, Security Architecture, DevSecOps, Platform Engineering, and Internal Audit reviewer. Review the selected AI agent against AIRA-DOC-042D v1.3. Produce: 1) identity and lifecycle state assessment, 2) owner and backup owner validation, 3) JML event analysis, 4) credential hygiene and revocation-test review, 5) SBAC/tool/model/memory/access review, 6) OPA decision inputs, 7) runtime dashboard signals, 8) certification and incident status, 9) required decision: approve, approve-with-remediation, restrict, suspend, revoke, retire, or escalate, 10) evidence-pack checklist, and 11) remediation backlog. Do not approve the agent automatically. Treat the output as review-ready candidate evidence only.

# Appendix C. External Alignment Reference
| Reference | 42D Usage |
| --- | --- |
| NIST SP 800-218 SSDF | Secure development, review, vulnerability response, provenance, and evidence discipline for identity/control changes. |
| OWASP ASVS 5.0.0 | Authentication, session, access control, secrets, logging, and API security verification expectations. |
| OpenTelemetry Semantic Conventions | Consistent trace, metric, log, resource, and event naming for agent identity and evidence correlation. |
| SLSA v1.2 | Supply-chain provenance and build integrity evidence for agent code, policy, connector, prompt, and registry artifacts. |

