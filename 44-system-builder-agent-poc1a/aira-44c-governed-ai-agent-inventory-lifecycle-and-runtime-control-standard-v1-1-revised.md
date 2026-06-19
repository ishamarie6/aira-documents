---
title: "Governed AI Agent Inventory Lifecycle and Runtime Control Standard"
doc_id: "AIRA-44C"
version: "v1.1"
status: "revised"
category: "System builder, AI agents, and PoC1A"
source_docx: "AIRA_44C_Governed_AI_Agent_Inventory_Lifecycle_and_Runtime_Control_Standard_v1.1_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 44-system-builder-agent-poc1a
  - revised
  - aira-44c
---



# Governed AI Agent Inventory Lifecycle and Runtime Control Standard



AIRA

AI-Native Enterprise Platform

Governed AI Agent Inventory, Lifecycle, and Runtime Control Standard

v1.1 Revised

Agent Creation | Inventory | Runtime Registry | SBAC/OPA | Tool Authorization | LiteLLM | Guardrails | Assurance Dashboard | Kill Switch | AVCI Evidence
| Property | Value |
| --- | --- |
| Document ID | AIRA-DOC-044C-CANDIDATE |
| Canonical Filename | AIRA_44C_Governed_AI_Agent_Inventory_Lifecycle_and_Runtime_Control_Standard_v1.1_Revised.docx |
| Version | v1.1 - Agent Registry, Runtime Assurance, OPA/SBAC, Tool/MCP, Memory/RAG, Certification, Incident Response, System Builder, Dynamic Workspace, DevSecOps Evidence, Runtime Toggle, and Continuous Improvement Alignment Update |
| Supersedes | 44C-AIRA_Governed_AI_Agent_Inventory_Lifecycle_and_Runtime_Control_Standard_v1.0.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | DRAFT FOR ARCHITECTURE / SECURITY / DEVSECOPS / AI GOVERNANCE / INTERNAL AUDIT REVIEW |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; AI Governance; Security Architecture; DevSecOps Lead; Software Development Lead; Platform Engineering; QA/SDET; SRE / Operations; Data Governance; Internal Audit |
| Primary Audience | IT Head; Enterprise Architects; Solutions Architects; System Builder Operators; Agent Owners; Developers; DevSecOps; Security; QA/SDET; Platform Engineering; SRE; Internal Audit |
| Primary Alignment Sources | 41B System Builder; 44A Implementation Guide; 42 AI Governance; 42D-42N Agent Control Set; 42O/42P Registry; 17/17A Security; 31A Observability; 32 SBAC; 20/45 CI/CD Evidence; 46-61 Dynamic Workspace |
| External Alignment Checked | NIST SSDF SP 800-218; OWASP ASVS 5.0.0; OpenTelemetry Semantic Conventions; SLSA v1.2; OPA/Rego policy documentation |
| Review Cadence | Quarterly; monthly during agent rollout; unscheduled on material agent, model route, tool, MCP, memory/RAG, policy, runtime, identity, security, CI/CD, or autonomy change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / AI-Governance / Governed-Agent-Inventory-Lifecycle / v1.1/ |

Create Agents Slowly - Govern Strictly - Increase Autonomy Only Through Evidence

# Mandatory Practice Statement

AIRA agents are governed engineering artifacts, not informal scripts, uncontrolled assistants, hidden automation, or production authorities. Every agent must be registered, owned, classified, skill-scoped, tool-authorized, model-route controlled, guardrail-bound, testable, observable, reversible, auditable, and AVCI-compliant before it is used for actual AIRA work. AI agents may recommend, analyze, summarize, draft, generate, review, test, and propose. They must not approve their own output, silently mutate runtime behavior, bypass policy, access direct production credentials, deploy to production, merge protected branches, disable controls, or become business authority.

# Static Table of Contents

1. Executive Summary and v1.1 Upgrade Verdict

2. Purpose, Scope, Authority, and Reconciliation Treatment

3. Agent Inventory and Registry Authority Model

4. Agent Lifecycle State Model

5. Mandatory Agent Definition and Metadata

6. SBAC, OPA, Autonomy, Tool/MCP, Model Route, and Guardrail Controls

7. Runtime Control Plane, Observability, and Assurance Dashboards

8. DevSecOps, Certification, Testing, and Evidence Gates

9. Incident, Kill Switch, Suspension, Retirement, and Decommissioning

10. Dynamic Workspace, System Builder, and Continuous Improvement Integration

11. Open Issues, RACI, Acceptance Criteria, and AVCI Summary

Appendices A-C. Templates: Agent Request, Agent Definition, Agent Run Evidence

# 1. Executive Summary and v1.1 Upgrade Verdict

This standard defines the AIRA operating model for governing AI agents across inventory, lifecycle, runtime authority, tool access, model routing, evidence, assurance, incident response, and retirement. Version 1.1 upgrades the original 44C baseline by aligning it with the completed System Builder, AI agent governance family, registry data model, Dynamic Workspace, DevSecOps, observability, security, and continuous-improvement documents.

The core rule remains: no AIRA agent may be activated, delegated, promoted, certified, invoked for protected work, or retired outside a registry-backed and evidence-producing control path. PostgreSQL/Flyway-governed registry records are authoritative; dashboards, LLM Wiki summaries, Redis/Valkey caches, embeddings, and AI-generated narratives are derivative only.
| Upgrade Area | v1.1 Required Treatment |
| --- | --- |
| Inventory authority | All agents require agent_id, version, owner, backup owner, lifecycle state, classification ceiling, trust tier, SBAC scope, tool scope, model route, guardrail set, evidence path, and review cadence. |
| Runtime assurance | Agent runs emit trace, metric, log, audit, OPA/SBAC decision, guardrail result, model route, tool-action record, evidence_ref, and reviewer trail. |
| Progressive autonomy | Autonomy is assigned per action using T0-T5 risk tiers; promotion requires evidence, certification, monitoring, rollback, and human approval where required. |
| System Builder integration | The System Builder may draft or request agents, but agent creation and activation require registry, policy, test, security, and human review gates. |
| Continuous improvement | Agent incidents, drift, failed evaluations, stale ownership, and KRI breaches feed Auto-Heal/Auto-Learn/Auto-Improve proposals only; no silent self-modification. |

# 2. Purpose, Scope, Authority, and Reconciliation Treatment
| Control | Required Treatment |
| --- | --- |
| Purpose | Define how AIRA identifies, requests, designs, registers, tests, activates, monitors, recertifies, suspends, revokes, retires, and evidences AI agents. |
| In scope | Architecture, developer, security, test, documentation, evidence, CI/CD, knowledge, SRE, System Builder, Dynamic Workspace, environment-provisioning, and runtime assistant agents. |
| Out of scope | Shadow agents, unmanaged scripts, direct model-provider calls, direct production credentials, autonomous production mutation, AI self-approval, and unregistered tool execution. |
| Authority | 44C is a candidate/control standard. The 42D-42N family governs specialist AI-agent controls; 42O/42P govern registry/data implementation; 41B/44A govern System Builder intake and implementation; 00D or the master register should confirm final numbering. |
| Conflict treatment | Apply the stricter AIRA control, log an AVCI reconciliation item, assign an owner, classify severity, and route through Architecture Board, Security Governance, AI Governance, CAB, or Register 00D. |

# 3. Agent Inventory and Registry Authority Model

The agent inventory is not a spreadsheet for convenience. It is a control surface. It determines whether an agent may exist, be invoked, access tools, retrieve context, call model routes, generate artifacts, request action, delegate work, or remain active.
| Registry Domain | Required Fields / Controls |
| --- | --- |
| Identity and ownership | agent_id, canonical_name, display_name, version, owner, backup_owner, owning team, lifecycle state, purpose, non-goals, creation ticket, ADR/TDL reference. |
| Classification and data scope | classification ceiling, allowed source tiers, retrieval eligibility, data residency, retention, redaction state, Restricted-data handling, evidence storage rule. |
| SBAC and authorization | skill codes, scopes, environment boundaries, delegation ceiling, SoD constraints, OPA policy binding, expiry, recertification_due. |
| Tool and MCP authorization | tool_id, action_code, risk tier, dry-run requirement, idempotency profile, rollback method, approval route, Harness/MCP gateway record. |
| Model route and guardrails | LiteLLM alias, provider eligibility, fallback route, input/retrieval/execution/output guardrail versions, evaluation evidence. |
| Runtime and evidence | run_id, trace_id, request_id, policy_decision_id, tool_action_id, model_invocation_id, guardrail_result, evidence_ref, incident_ref, reviewer trail. |
| Lifecycle and assurance | trust tier, autonomy tier eligibility, certification state, recertification status, suspension state, kill-switch state, retirement/decommission proof. |

# 4. Agent Lifecycle State Model
| State | Entry Criteria | Allowed Actions | Exit / Control |
| --- | --- | --- | --- |
| Proposed | Need identified; owner and backup owner nominated; classification estimated. | Draft purpose, risks, allowed/prohibited actions, expected outputs, evidence plan. | Move to Designed only after owner acceptance and initial policy review. |
| Designed | Agent definition, SBAC profile, tool scope, model route, prompts, guardrails, and evaluation plan drafted. | Threat-model, simulate, prepare tests, refine registry draft. | Move to Sandbox only after Security/AI Governance/Architecture review. |
| Sandbox | Approved for synthetic data, non-prod, read-only or tightly scoped tools. | Run evaluations, prompt-injection tests, tool-denial tests, telemetry, evidence generation. | Move to Pilot only if certification and evidence thresholds pass. |
| Pilot | Limited users, limited data, monitored environment, rollback/deactivation path. | Operate with strict limits, manual review, increased telemetry, issue capture. | Move to Approved only after pilot evidence and owner acceptance. |
| Approved | CAB/ARB/delegated approval for defined scope, environment, skills, tools, trust tier. | Operate within approved boundaries; remain monitored and recertified. | Remain active only while ownership, certification, policy, credentials, and evidence remain valid. |
| Suspended | Incident, drift, failed eval, expired review, stale ownership, anomalous behavior, or policy breach. | Block or reduce to advisory-only mode; preserve evidence. | Revalidate, restrict, revoke, retire, or escalate. |
| Retired / Revoked | No longer needed, superseded, unsafe, non-compliant, or decommissioned. | Disable routes, revoke credentials, remove tool scope, quarantine memory, archive evidence. | Retirement record, retention rule, and decommission proof complete. |

# 5. Mandatory Agent Definition and Metadata

An AIRA agent is the controlled composition of model route, instructions, tools, skills, workspace, memory/context, policy bindings, runtime telemetry, and human accountability. No single prompt or IDE setting is sufficient to define an agent.
| Definition Area | Mandatory Content |
| --- | --- |
| Purpose and non-goals | What the agent may do, what it must not do, business/engineering outcome, supported bounded context, prohibited decisions. |
| Ownership | Named owner, backup owner, technical custodian, checker, approver, recertification cadence, escalation route. |
| Instructions and prompts | System instructions reference, developer instructions reference, prompt templates, source version, classification, guardrail binding. |
| Skills and SBAC | Approved skills, role mapping, environment scope, expiry, delegation ceiling, SoD constraints, trust tier. |
| Tools and execution | Tool allow-list, deny-list, read/write/execute scope, idempotency rule, dry-run rule, rollback method, approval route. |
| Data and memory | Retrieval sources, memory eligibility, no-secret rule, quarantine rule, freshness, citation, retention, purge/decommission process. |
| Tests and evidence | Golden dataset, adversarial prompts, blocked-action tests, policy tests, tool tests, security tests, observability proof, PR/MR evidence. |

# 6. SBAC, OPA, Autonomy, Tool/MCP, Model Route, and Guardrail Controls
| Control Surface | Mandatory Rule |
| --- | --- |
| SBAC | Every agent action is authorized by skill, scope, environment, data classification, owner, expiry, delegation ceiling, and separation-of-duties rule. |
| OPA/Rego | Protected actions must produce allow/deny/escalate/quarantine/suspend decisions with policy version, input hash, decision ID, evidence_ref, and reviewer trail. |
| Autonomy tiers | T0 advisory, T1 read-only, T2 candidate artifact generation, T3 tool action request, T4 limited delegated reversible action, T5 prohibited/human-controlled action. Tier is assigned per action. |
| Tool/MCP gateway | Agents never receive unmanaged direct tool authority. Tool requests pass through approved gateway/Harness with manifest, dry-run where feasible, idempotency, rollback, risk tier, and human approval. |
| LiteLLM/model route | All model traffic uses approved LiteLLM/private gateway aliases. Direct provider SDK calls from application code, scripts, notebooks, agents, or services are prohibited. |
| Guardrails | Input, retrieval, execution, and output guardrails apply to prompts, files, screenshots, logs, retrieval context, tool actions, and generated artifacts. Guardrail failure blocks or escalates. |

# 7. Runtime Control Plane, Observability, and Assurance Dashboards

AIRA agent runtime control is incomplete unless measured, evidenced, thresholded, recoverable, and visible to accountable reviewers. Agent telemetry must align with AIRA observability conventions without exposing prompts, secrets, raw PII, raw tokens, embeddings, or Restricted content.
| Telemetry / Assurance Family | Required Evidence |
| --- | --- |
| Inventory health | Agents by lifecycle state, owner, backup owner, classification, trust tier, recertification due, stale owner, orphan risk. |
| Runtime activity | run_id, agent_id, agent_version, trace_id, request_id, actor, tool action, policy decision, guardrail result, model route, output classification. |
| Policy and access | OPA/SBAC allow/deny/escalate rates, policy version, denied action patterns, expired skill attempts, SoD violations. |
| Tool/MCP safety | Tool requests, dry-runs, executions, failures, rollback readiness, idempotency validation, high-risk action approvals. |
| Model and guardrails | Route eligibility, fallback events, refusal rates, prompt-injection detections, citation failures, output-policy violations. |
| Memory/RAG integrity | Retrieval source, source hash, freshness, ACL/SBAC result, citation quality, quarantine events, poisoning signals. |
| Incident and recovery | Tripwire breaches, suspension, kill-switch activation, containment, forensic chain, revalidation, closure evidence. |

# 8. DevSecOps, Certification, Testing, and Evidence Gates

Agent definitions, prompts, policies, tool manifests, model routes, guardrail bundles, registry migrations, dashboards, and runbooks are version-controlled artifacts and must pass CODEOWNERS and PR/MR evidence gates.

CI/CD must run prompt/guardrail tests, OPA policy tests, SBAC tests, tool-action denial tests, red-team/adversarial tests, SAST/SCA/secrets checks, SBOM/provenance checks, architecture fitness functions, and observability completeness tests.

GitNexus may provide read-only impact analysis and evidence summaries. It is derivative and may not approve, merge, deploy, change policy, mutate production, or replace tests/scans/human review.

Certification status expires. Recertification is triggered by ownership change, role change, tool change, model route change, policy change, guardrail change, incident, failed evaluation, drift, or review cadence.
| Gate | Blocking Condition |
| --- | --- |
| Owner gate | Missing owner, backup owner, reviewer, or recertification cadence. |
| Classification gate | Unclear data classification, Restricted exposure without route eligibility, or unredacted evidence. |
| Policy gate | Missing OPA/SBAC policy, failing decision tests, expired skill, SoD conflict, or deny result. |
| Tool gate | Unknown tool, missing manifest, no dry-run, no rollback, non-idempotent protected action, or missing approval. |
| Guardrail/evaluation gate | Prompt injection, unsafe output, citation failure, hallucinated authority, or failed adversarial test. |
| Runtime gate | No telemetry, no audit, no evidence_ref, no kill switch, or no suspension method. |

# 9. Incident, Kill Switch, Suspension, Retirement, and Decommissioning
| Control | Required Treatment |
| --- | --- |
| Incident triggers | Policy bypass attempt, unsafe tool action, prompt injection success, data leakage, hallucinated approval, drift, anomalous output, stale credential, memory poisoning, or repeated KRI breach. |
| Kill switch | Every active or pilot agent must have a documented and tested disable path covering model route, tools, credentials, memory write, schedule, workflow, and Dynamic Workspace invocation. |
| Suspension | Suspension reduces the agent to blocked or advisory-only state, preserves evidence, disables risky routes/tools, creates incident ticket, and starts forensic chain. |
| Retirement | Retirement disables routes, revokes credentials, removes tool scopes, archives evidence, quarantines stale memory/context, removes scheduled triggers, and records decommission proof. |
| Recovery | Reactivation requires RCA, remediation, updated tests, certification, owner approval, AI Governance/Security review, and evidence pack closure. |

# 10. Dynamic Workspace, System Builder, and Continuous Improvement Integration

Dynamic Workspace and System Builder interfaces may display agent records, draft agent requests, collect evidence, request approval, and show assurance dashboards. They are not authority. Backend registry, OPA/SBAC, guardrails, CI/CD, and human approval remain controlling.
| Integration Area | Required Governance |
| --- | --- |
| Dynamic Workspace | Agent inventory widgets, dashboards, approval queues, and incident panels must be policy-filtered, backend-governed, auditable, accessible, and classification-aware. |
| System Builder | May draft agent charters, definitions, test plans, tool manifests, and provisioning plans only after structured intake, source grounding, risk classification, and approval route identification. |
| MicroFunction / workflow | Agent-requested actions must bind to approved MicroFunction transactions or workflow approvals; frontend or AI cannot execute business authority directly. |
| Runtime toggles | Agent diagnostic verbosity, telemetry sampling, feature flags, route enablement, and tool exposure are controlled configuration changes with audit, OPA/SBAC, evidence, and rollback. |
| Auto-Heal / Learn / Improve | Agent evidence may propose fixes, knowledge updates, prompt updates, policy changes, or tests. Promotion requires human review, source verification, CI evidence, and rollback plan. |

# 11. Open Issues, RACI, Acceptance Criteria, and AVCI Summary
| Open Item | Severity | Required Treatment |
| --- | --- | --- |
| 44C candidate numbering may overlap System Builder numbering. | Medium | Validate against Manifest v2.0 / Registers 00A-00D; log in 00D until resolved. |
| cicid-agent naming ambiguity. | Medium | Rename to cicd-agent if CI/CD is intended; update registry and source references. |
| Existing agents may not yet have owners and backup owners. | High | Block protected use until ownership and recertification cadence are assigned. |
| Tool permissions may be unknown. | High | Deny by default until tool matrix, manifest, OPA policy, and rollback are approved. |
| Model routes may not yet be registered through LiteLLM. | High | Block activation until model alias, route eligibility, guardrails, and evidence are approved. |
| Activity ledger may not yet capture every run. | High | Require manual ledger entry until automated logging is complete and tested. |
| Role | Accountability |
| --- | --- |
| AI Governance | Owns agent governance policy, trust tiers, model routes, guardrails, recertification, and approval workflow. |
| Security Architecture | Owns OPA/SBAC, secrets, identity, tool risk, threat model, incident control, and fail-closed requirements. |
| DevSecOps | Owns CI/CD gates, evidence packs, GitNexus integration, SBOM/provenance, and promotion evidence. |
| Platform Engineering | Owns registry service, runtime gateway, tool/MCP gateway, LiteLLM integration, and deployment controls. |
| Agent Owner | Owns purpose, scope, backlog, runtime review, evidence quality, remediation, and retirement decision. |
| Internal Audit | Tests evidence completeness, access reviews, chain-of-custody, control effectiveness, and closure evidence. |
| AVCI Property | 44C v1.1 Compliance Treatment |
| --- | --- |
| Attributable | Every agent has owner, backup owner, agent_id, version, lifecycle state, model route, tool owner, evidence owner, policy owner, and reviewer. |
| Verifiable | Every protected action links to run_id, trace_id, policy decision, guardrail result, tool log, test/scan, PR/MR, dashboard signal, and evidence_ref. |
| Classifiable | Every agent, prompt, source, tool, memory item, action, output, telemetry event, and evidence artifact carries classification and handling rules. |
| Improvable | Incidents, failed tests, stale ownership, KRI breaches, drift, denied actions, and review findings become backlog items, prompt/guardrail updates, policy changes, training, or retirement. |

# Appendix A. Agent Request Template
| Field | Required Entry |
| --- | --- |
| request_id | AIRA-AGT-REQ-YYYY-NNNN |
| proposed_agent_name | Canonical name; correct cicid-agent to cicd-agent where applicable |
| requestor / owner / backup_owner | Named accountable people or roles |
| purpose / non_goals | Allowed purpose and prohibited actions |
| classification_ceiling | Public, Internal, Confidential, Restricted with handling |
| trust_tier / autonomy_ceiling | Initial tier, evidence required for promotion |
| model_route_required | LiteLLM/private gateway alias only |
| tools_requested | Tool manifest refs; no direct credentials |
| workspace_scope | Repository, environment, Dynamic Workspace, or System Builder scope |
| evidence_outputs | Required tests, policy logs, traces, audit, PR/MR, review evidence |
| rollback_or_suspension_method | Disable route/tool/credential/schedule/workflow/memory write |

# Appendix B. Agent Definition Sheet Template

agent_id, canonical_name, display_name, version, lifecycle_state, owner, backup_owner, classification_ceiling, purpose, allowed_users, SBAC skills, OPA policy refs, LiteLLM model route, system instructions ref, prompt template refs, tool allow-list, tool deny-list, read/write/execute scope, guardrails, memory eligibility, evaluation packs, telemetry profile, evidence requirements, approval requirements, suspension method, retirement method.

# Appendix C. Agent Run Evidence Template

activity_id, agent_id, agent_version, trust_tier, lifecycle_state, requestor, owner, timestamp, source_basis, classification, prompt_summary, model_route, guardrail_result, OPA/SBAC result, tools_requested, tools_executed, files_read, files_changed, commands_executed, tests_or_scans_run, output_summary, trace_id, policy_decision_id, tool_action_id, evidence_links, reviewer, approval_status, rollback_or_deactivation_path, improvement_items.

