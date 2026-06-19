---
title: "AI Agent Policy as Code Reference Pack and OPA SBAC Rule Catalog"
doc_id: "AIRA-42N"
version: "v1.1"
status: "revised"
category: "AI governance and agent control"
source_docx: "AIRA_42N_AI_Agent_Policy_as_Code_Reference_Pack_and_OPA_SBAC_Rule_Catalog_v1.1_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 42-ai-governance-agent-control
  - revised
  - aira-42n
---



# AI Agent Policy as Code Reference Pack and OPA SBAC Rule Catalog



AIRA
AI-Native Enterprise Platform

AI Agent Policy-as-Code Reference Pack and OPA/SBAC Rule Catalog

Executable Agent Governance | OPA Decision Contracts | SBAC Skills | Runtime Policy Catalog | Evidence by Construction

Version v1.1 Revised | Draft for Architecture, Security, AI Governance, DevSecOps, Platform Engineering, and Internal Audit Review
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-042N |
| Canonical Filename | AIRA_42N_AI_Agent_Policy_as_Code_Reference_Pack_and_OPA_SBAC_Rule_Catalog_v1.1_Revised.docx |
| Version | v1.1 Revised - Runtime Policy, System Builder, Dynamic Workspace, and Evidence Alignment Update |
| Supersedes | 42N-AIRA_AI_Agent_Policy_as_Code_Reference_Pack_and_OPA_SBAC_Rule_Catalog_v1.0_FINAL.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Architecture, Security, AI Governance, DevSecOps, QA/SDET, Platform Engineering, and Internal Audit Review |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Security Architecture; AI Governance; DevSecOps Lead; Platform Engineering; Software Development Lead; QA/SDET; Internal Audit |
| Primary Parent | 42-AIRA AI Governance and Runtime Control Standard |
| Direct Companions | 42D Identity; 42E Runtime Security; 42F Autonomy; 42G Threat Model; 42H Tool/MCP; 42I Memory/RAG; 42J Certification; 42K Incident; 42L Delegation; 42M Supply Chain; 42O Runtime Registry |
| Review Cadence | Monthly during agent rollout; quarterly after controlled maturity; immediate after policy, tool, model-route, memory, incident, or autonomy control change |

Mandatory Practice Statement. AIRA AI agent policy is not a narrative guideline. It is an executable, versioned, testable, evidence-producing control layer. Every protected agent action, System Builder output, Dynamic Workspace AI action, tool/MCP invocation, model-route request, memory/RAG access, delegation chain, supply-chain artifact, runtime toggle, incident response, and autonomy promotion must be evaluated through approved policy-as-code, SBAC, OPA decision contracts, deterministic tests, and named human accountability. Missing identity, classification, skill, policy, guardrail, audit, approval, evidence, or rollback metadata must result in DENY, ESCALATE, QUARANTINE, SUSPEND, REVOKE, or DRY_RUN_ONLY rather than fail-open execution.

v1.1 Revision Focus. This revision strengthens the v1.0 42N baseline by aligning OPA/SBAC policy-as-code with the revised System Builder, Dynamic Workspace, Tool/MCP Gateway, agent runtime registry, GitNexus evidence, runtime-toggle governance, OpenTelemetry evidence correlation, DevSecOps promotion gates, and Auto-Heal/Auto-Learn/Auto-Improve candidate loops.

# Static Table of Contents

1. Executive Summary

2. Purpose, Scope, and Authority

3. Relationship to the AIRA AI Agent Governance Control Set

4. Policy-as-Code Operating Model

5. OPA Decision Contract

6. SBAC Skill Catalog Model

7. Rule Package Catalog

8. Decision Outcome Taxonomy and Approval Routing

9. Policy Testing, Certification, CI/CD, and Runtime Deployment

10. Runtime Toggles, Observability, Evidence, and Assurance Dashboards

11. Dynamic Workspace, System Builder, MicroFunction, and Tool Gateway Integration

12. Auto-Heal, Auto-Learn, Auto-Improve, and Incident-Driven Policy Improvement

13. RACI, Roadmap, Acceptance Criteria, and AVCI Summary

Appendix A. Rego Reference Patterns

Appendix B. Policy Bundle Manifest and PR/MR Checklist

# 1. Executive Summary

AIRA-DOC-042N defines the executable policy-as-code and OPA/SBAC rule catalog required to govern AI agents and System Builder assisted changes. It converts AIRA standards into deterministic allow, deny, escalate, quarantine, suspend, revoke, and dry-run-only decisions that are testable, versioned, promoted through CI/CD, observable at runtime, and reconstructable through AVCI evidence.

The strategic objective is to prevent agent authority from being inferred from prompts, model confidence, convenience, or tool availability. Authority must be computed from registered identity, lifecycle state, owner, SBAC skill, classification ceiling, model route, memory eligibility, tool manifest, supply-chain provenance, autonomy tier, environment, approval path, evidence completeness, and rollback or containment readiness.

Policy-as-code therefore becomes the runtime enforcement seam between documentation and execution. Agents may recommend, draft, analyze, test, summarize, and request action; execution remains governed by OPA/SBAC, Harness or approved tool gateways, DevSecOps gates, maker-checker review, and CAB/ARB approval when risk requires it.

# 2. Purpose, Scope, and Authority
| Area | Required Treatment |
| --- | --- |
| Purpose | Define the AIRA OPA/SBAC reference model, policy decision contract, rule package catalog, tests, evidence schema, runtime deployment rules, and assurance metrics for AI agent actions. |
| In Scope | Agent identity, skills, model routes, memory/RAG access, tools/MCP connectors, delegation chains, supply-chain artifacts, runtime toggles, Dynamic Workspace AI actions, System Builder generation requests, incident controls, and improvement candidates. |
| Out of Scope | Replacing human approval, CAB/ARB, Security Governance, source-code review, DevSecOps gates, or production-change control. 42N supplies executable policy controls; it does not make AI an authority. |
| Authority | L0 ARB/CAB/Security Governance for high-risk policy exceptions; L1 AIRA AVCI/Security/AI/DevSecOps standards; L2 42N policy-as-code model; L3 OPA bundles, SBAC catalog, policy tests, CI/CD evidence, runtime decision logs. |
| Conflict Rule | Where policy is silent or documents conflict, apply the stricter AIRA control, fail closed where protected action is involved, and log an AVCI reconciliation item for 00D tracking. |

# 3. Relationship to the AIRA AI Agent Governance Control Set
| Source | 42N Policy Binding Responsibility |
| --- | --- |
| 42D Identity Lifecycle | Require active lifecycle state, current owner, backup owner, recertification, credential status, and decommission proof before protected actions. |
| 42E Runtime Security | Emit decision evidence, enforce tripwires, support quarantine/suspension/revocation, and feed assurance dashboards. |
| 42F Autonomy Calibration | Map T0-T5 autonomy risk tier to allowed action, escalation, approval, dry-run, and prohibition decisions. |
| 42G Threat Model | Convert abuse cases, attack surfaces, and red-team scenarios into negative tests and denial/escalation rules. |
| 42H Tool/MCP Gateway | Authorize tool requests using tool manifest, risk tier, idempotency, dry-run, rollback, Harness route, and human approval. |
| 42I Memory/RAG Integrity | Block or quarantine stale, poisoned, conflicting, unclassified, unauthorized, or non-authoritative context. |
| 42J Certification | Prevent promotion or high-risk execution when certification pack, red-team result, or expiry status fails policy. |
| 42K Incident Response | Support containment, kill switch, policy revoke, credential rotation, memory quarantine, and forensic evidence preservation. |
| 42L Multi-Agent Delegation | Prevent authority amplification, loop/cascade abuse, non-transparent delegation, collusion, and self-approval. |
| 42M Supply Chain | Require approved connector/MCP/plugin provenance, SBOM, signature, license, scan, registry status, and drift monitoring. |
| 42O Runtime Registry | Use registry-backed agent, tool, route, memory, lifecycle, certification, policy, and evidence records as authoritative decision input. |

# 4. Policy-as-Code Operating Model

AIRA policy-as-code is implemented as versioned policy bundles that are authored in Git, reviewed through PR/MR, tested through OPA/conftest and CI/CD, promoted through controlled environments, observed at runtime, and improved through evidence-driven backlog items. Policy may be advisory in early PoC stages, but protected actions cannot rely on advisory-only evaluation once enforcement is approved.
| Stage | Required Output | Evidence Gate |
| --- | --- | --- |
| Intake | PolicyChangeRequest or SystemBuilderPolicyImpact record | Owner, source, affected control set, risk tier, classification, expected outcome, rollback path. |
| Design | OPA input/output schema, SBAC skill mapping, rule package, and test plan | Architecture/Security/AI Governance review; threat and abuse-case coverage. |
| Build | Rego package, data bundle, SBAC catalog delta, test fixtures | Positive, negative, escalation, abuse-case, regression, and incident tests. |
| Promote | Signed policy bundle and deployment manifest | CI pass, evidence pack, GitNexus impact where relevant, maker-checker approval. |
| Runtime | Policy decision log and audit/evidence record | Trace ID, agent ID, policy version, input hash, decision, reason codes, approval route, rollback reference. |
| Improve | Policy defect, waiver, backlog, or recertification item | Finding owner, due date, compensating control, retest and closure evidence. |

# 5. OPA Decision Contract

The OPA decision contract must be stable enough for APIs, Dynamic Workspace, System Builder, Harness, Tool/MCP Gateway, CI/CD, dashboards, and audit sampling to consume consistently. Runtime policy decisions must be deterministic and reproducible from stored input hash, policy bundle version, registry records, and evidence references.
| Input Domain | Minimum Required Fields |
| --- | --- |
| request | request_id, trace_id, actor_type, intent, environment, risk_tier, data_classification, action_type, source_ref, approval_context. |
| agent | agent_id, agent_version, lifecycle_state, owner_current, certification_current, recertification_current, classification_ceiling, trust_tier, autonomy_tier. |
| sbac | skills, skill_expiry, delegation_ceiling, environment_scope, sod_conflict, skills_current, reviewer_role. |
| tool | tool_id, operation, tool_risk_tier, registered, dry_run_supported, idempotency_key_present, rollback_method_present, harness_route. |
| model | route_alias, direct_provider_sdk, classification_route_allowed, guardrails_available, guardrail_version, budget_policy. |
| memory_context | retrieval_eligible, source_authoritative, freshness_valid, classification_allowed, conflict_detected, poisoning_signal, quarantine_status. |
| supply_chain | connector_registered, artifact_signed, sbom_present, provenance_valid, license_approved, drift_status. |
| evidence | evidence_ref, policy_test_ref, approval_ref, rollback_ref, incident_ref, retention_rule. |
| Output Field | Mandatory Meaning |
| --- | --- |
| decision_id | Unique policy decision record. |
| decision | ALLOW, DENY, ESCALATE, QUARANTINE, SUSPEND, REVOKE, or DRY_RUN_ONLY. |
| reason_codes | Stable explainable codes such as PAC-ALLOW-LOW-RISK-TOOL or PAC-RAG-POISONING-SIGNAL. |
| human_approval_required / approval_route | Security, Architecture, DevSecOps, CAB, Flowable, owner, or maker-checker route. |
| constraints | Runtime constraints such as dry_run_first, no_prod_without_cab, retain_evidence, no_memory_write. |
| evidence_required | Required records before execution or promotion. |
| policy_bundle / policy_version / input_hash | Reproducibility and tamper-evident traceability. |
| expires_at / audit_required | Decision TTL and audit obligations. |

# 6. SBAC Skill Catalog Model

SBAC skills must be narrow, explicit, expirable, reviewable, and mapped to permitted actions. A skill is not a role shortcut. It is a bounded capability with owner, evidence, expiry, separation-of-duties rules, environment scope, classification ceiling, and delegation ceiling.
| Skill Family | Examples | Default Authority |
| --- | --- | --- |
| agent.identity.* | register, review, recertify, suspend, revoke | Human approval required for suspension, revocation, production activation, and credential-impacting changes. |
| agent.tool.* | request, simulate, execute_low_risk, execute_high_risk | Execution mediated by Harness/Tool Gateway and OPA. High-risk and production actions escalate. |
| agent.memory.* | retrieve, quarantine, write_candidate, promote_context | Permanent memory writes or retrieval-source promotion require human review. |
| agent.modelroute.* | request_route, validate_guardrail, inspect_usage | Direct provider SDK use is denied; model route must be via approved LiteLLM alias and guardrails. |
| agent.policy.* | read_policy, propose_rule, run_tests, promote_bundle | Promotion of production bundles requires Security/AI Governance/DevSecOps approval. |
| agent.delegation.* | delegate_read, delegate_draft, delegate_tool_request | Delegation cannot exceed original actor authority, agent ceiling, or approval state. |
| agent.supplychain.* | register_connector, verify_artifact, quarantine_connector | Connector activation requires registry, provenance, scan, SBOM, signature, and policy tests. |
| agent.incident.* | contain, kill_switch_request, quarantine, revoke_route | Incident actions preserve evidence and follow 42K severity and approval rules. |

# 7. Rule Package Catalog
| Package | Purpose | Mandatory Tests |
| --- | --- | --- |
| aira.agent.identity | Validate lifecycle, owner, credential, recertification, certification, and registry state. | Unregistered, retired, revoked, expired, missing owner, expired credential, and stale recertification denial tests. |
| aira.agent.sbac | Validate skills, environment scope, classification ceiling, SoD, delegation ceiling, and expiry. | Missing skill, expired skill, SoD conflict, over-classification, over-delegation, and production-scope tests. |
| aira.agent.tool | Authorize tool/MCP requests through manifest, Harness, risk tier, idempotency, dry-run, rollback, and approval. | Unregistered tool, direct execution, missing idempotency, no rollback, high-risk escalation, and destructive action denial tests. |
| aira.agent.modelroute | Enforce LiteLLM alias, classification route, budget, guardrails, and direct SDK prohibition. | Direct provider SDK denial, route mismatch, missing guardrail, budget breach, and restricted-data route tests. |
| aira.agent.memory | Protect RAG/context retrieval, source authority, freshness, poison/quarantine, conflict, and memory writes. | Stale source, conflict, poisoning signal, unauthorized context, and permanent write approval tests. |
| aira.agent.delegation | Prevent privilege amplification, hidden delegation, self-approval, loops, and cascade failures. | Authority ceiling, loop breaker, non-collusion, and delegated approval denial tests. |
| aira.agent.supplychain | Enforce signed artifacts, SBOM, provenance, license, scan, registry status, and drift controls. | Unsigned, no SBOM, unapproved license, vulnerable connector, drift, and shadow MCP denial tests. |
| aira.agent.incident | Support quarantine, suspend, revoke, kill switch, containment, forensic preservation, and recovery gates. | Incident tripwire, revoke decision, quarantine route, recovery approval, and evidence-chain tests. |
| aira.workspace.systembuilder | Govern Dynamic Workspace AI actions and System Builder generation, activation, and promotion requests. | Prompt-to-code bypass, unauthorized template activation, weak evidence, and missing maker-checker tests. |

# 8. Decision Outcome Taxonomy and Approval Routing
| Outcome | Meaning | Typical Route |
| --- | --- | --- |
| ALLOW | Request satisfies identity, SBAC, classification, tool/model/memory eligibility, risk, evidence, and approval constraints. | Proceed through approved adapter or Harness with audit. |
| DENY | Request violates a hard rule or lacks mandatory metadata for protected action. | Block safely, record reason code, and show safe response. |
| ESCALATE | Request may be allowed only after named human review or governance approval. | Owner, Security, Architecture, DevSecOps, CAB, Flowable, or maker-checker route. |
| QUARANTINE | Input, source, connector, memory, model route, or artifact is suspect and must be isolated. | Containment workflow, evidence preservation, investigation, revalidation. |
| SUSPEND | Agent, tool, route, connector, or skill must be temporarily disabled. | 42K incident response, owner notification, recertification required. |
| REVOKE | Authority, credential, connector, route, or agent must be permanently disabled or retired. | Security/AI Governance approval, decommission evidence, denial regression tests. |
| DRY_RUN_ONLY | Request can be simulated or analyzed but not executed. | Sandbox/CI/Harness dry-run, evidence review, human approval for execution. |

# 9. Policy Testing, Certification, CI/CD, and Runtime Deployment

Policy bundles are production-impacting controls. They must be tested like code, governed like security policy, versioned like release artifacts, and deployed like operational control-plane configuration. A policy that cannot be tested deterministically cannot become a blocking production gate.
| Gate | Minimum Requirement |
| --- | --- |
| Static policy lint | OPA/Rego lint, package namespace check, forbidden wildcard, unreachable rule, unsafe default, and formatting check. |
| Schema validation | Input/output schema compatibility with runtime registry, Tool/MCP Gateway, Dynamic Workspace, System Builder, and dashboard consumers. |
| Positive tests | Known-safe low-risk reads, simulations, and approved requests return ALLOW with correct constraints. |
| Negative tests | Missing identity, expired skills, direct SDK, unregistered tool, stale memory, and unsigned connector return DENY or QUARANTINE. |
| Escalation tests | Production, high-risk, Restricted, destructive, low-confidence, waiver, and approval-required paths return ESCALATE. |
| Incident tests | Tripwire conditions return SUSPEND, REVOKE, QUARANTINE, or DRY_RUN_ONLY and preserve evidence. |
| Promotion gates | Security, AI Governance, DevSecOps, QA/SDET, and Internal Audit evidence gates pass before staged enforcement. |
| Rollback | Previous signed bundle can be restored, decision service health is verified, and fail-closed mode is tested. |

# 10. Runtime Toggles, Observability, Evidence, and Assurance Dashboards

Runtime toggles may adjust diagnostic verbosity, sampling, shadow-evaluation, advisory/enforcement mode, or dashboard thresholds. They must not weaken policy outcome, bypass fail-closed controls, disable audit, hide denials, suppress security tripwires, or allow direct tool/model/provider access. Toggle changes require owner, reason, classification, expiry, approval path, audit, rollback, and evidence.
| Evidence / Metric | Required Purpose |
| --- | --- |
| decision_id, request_id, trace_id | Correlate agent request, policy decision, tool/model/memory action, approval, and audit trail. |
| agent_id, agent_version, actor_id, owner_id | Attribute the decision to exact agent and accountable human or service actor. |
| policy_bundle, policy_version, input_hash | Reconstruct decision behavior from approved policy source. |
| decision, reason_codes, approval_ref | Explain outcome and approval route. |
| tool_action_id, model_alias, guardrail_version | Bind action and model routing to authorized control paths. |
| classification, rollback_ref, containment_ref | Maintain data handling, reversibility, and incident response evidence. |
| Dashboard metrics | Decision count, deny/escalation rate, policy error rate, unregistered-tool denial, direct-SDK bypass, retrieval quarantine, delegation amplification denial, mean time to revoke. |

# 11. Dynamic Workspace, System Builder, MicroFunction, and Tool Gateway Integration
| Integration Area | Policy Requirement |
| --- | --- |
| Dynamic Workspace | Workspace, screen, component, widget action, AI Assistant prompt, admin-template activation, and runtime-toggle action must include capability code, SBAC skill, OPA policy reference, idempotency profile, audit profile, and evidence reference. |
| System Builder | Requirement intake, evidence intake, improvement request, agent creation, environment provisioning, and candidate generation must be classified and policy-evaluated before generation, PR creation, activation, or promotion. |
| MicroFunction Runtime | AI-governed MicroFunctions must evaluate identity, classification, authorization, idempotency, tool/model/memory eligibility, error handling, observability, and rollback before state change. |
| Tool/MCP Gateway | No tool executes directly from agent context. Tool request is evaluated by OPA/SBAC, routed through Harness or approved gateway, audited, and bounded by dry-run, idempotency, approval, and rollback constraints. |
| API/Event/Database | OpenAPI/AsyncAPI/Kafka/Avro/CloudEvents/Flyway/outbox/DLQ/replay actions require contract, schema, classification, version, and evidence gates before execution or activation. |

# 12. Auto-Heal, Auto-Learn, Auto-Improve, and Incident-Driven Policy Improvement

Auto-Heal, Auto-Learn, and Auto-Improve may detect policy friction, missing tests, recurrent denials, false positives, incident patterns, risky tools, stale retrieval sources, or skill catalog drift. They may create candidate rule changes, candidate SBAC updates, proposed tests, dashboards, tickets, or PR drafts. They must not self-promote policy bundles, approve their own changes, weaken controls to pass tests, or modify production enforcement without human review and evidence.
| Loop | Allowed 42N Output | Non-Negotiable Boundary |
| --- | --- | --- |
| Auto-Heal | Candidate policy fix, denial reason correction, incident containment rule, missing rollback constraint, new negative test. | No silent production policy mutation; human review, CI, and rollback evidence required. |
| Auto-Learn | Reviewed knowledge update, test fixture, rule catalog improvement, dashboard threshold recommendation. | No direct durable memory or authoritative source promotion without knowledge governance approval. |
| Auto-Improve | Refactoring proposal, policy package modularization, SBAC catalog cleanup, rule coverage improvement. | No weaker identity, SBAC, classification, evidence, guardrail, approval, or fail-closed controls. |

# 13. RACI, Roadmap, Acceptance Criteria, and AVCI Summary
| Activity | Architecture | Security | AI Governance | DevSecOps | Platform | QA/SDET | Internal Audit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Approve 42N standard | A | R | R | C | C | C | I |
| Own policy package design | R | R | R | C | C | C | I |
| Maintain SBAC catalog | C | A/R | C | C | C | I | I |
| Implement OPA tests | C | R | C | A/R | C | R | I |
| Approve production bundle | A | A/R | R | R | C | C | I |
| Monitor decision metrics | C | R | R | A/R | R | C | I |
| Investigate policy incident | A | R | R | R | R | C | A/R |
| Phase | Focus | Exit Criteria |
| --- | --- | --- |
| 0 | Register 42N and reconcile with 42D-42M, 42O, Dynamic Workspace, and System Builder standards. | Approved source-register entry and open issues captured in 00D. |
| 1 | Finalize OPA input/output schema and SBAC skill catalog. | Schema accepted by Architecture, Security, AI Governance, DevSecOps, and Platform. |
| 2 | Implement initial rule packages and fixtures. | Positive, negative, escalation, incident, and abuse-case tests pass. |
| 3 | Integrate with CI/CD, System Builder Lite, Tool/MCP Gateway, LiteLLM, and dashboards. | PR/MR evidence pack includes policy test and decision evidence. |
| 4 | Run red-team and certification suite. | Controlled pilot approved with rollback and monitoring. |
| 5 | Promote staged enforcement. | Production enforcement only after CAB/Security/ARB approval where required. |
| AVCI Property | 42N Compliance Mechanism |
| --- | --- |
| Attributable | Every policy, skill, bundle, decision, approval, exception, incident, and improvement has owner, source, version, approver, and evidence path. |
| Verifiable | OPA tests, policy bundle hashes, CI evidence, runtime decision logs, dashboards, red-team results, and audit sampling prove behavior. |
| Classifiable | Policy inputs, decisions, evidence, logs, dashboards, prompts, memory context, tools, and model routes carry classification and redaction rules. |
| Improvable | Policy denials, false positives, incidents, drift, red-team findings, audit findings, and developer friction feed controlled backlog and recertification. |

# Appendix A. Rego Reference Patterns

package aira.agent.runtime

default decision := {"decision": "DENY", "reason_codes": ["DEFAULT_DENY"]}

registered_agent if {
  input.agent.agent_id != ""
  input.agent.lifecycle_state == "active"
  input.agent.owner_current == true
  input.agent.recertification_current == true
}

classification_allowed if {
  input.request.data_classification == "internal"
} else if {
  input.agent.classification_ceiling == "confidential"
  input.request.data_classification != "restricted"
} else if {
  input.agent.classification_ceiling == "restricted"
}

allow_low_risk_tool if {
  registered_agent
  classification_allowed
  input.sbac.skills_current == true
  input.sbac.sod_conflict == false
  input.tool.tool_risk_tier == "low"
  input.tool.idempotency_key_present == true
  input.model.direct_provider_sdk == false
  input.model.guardrails_available == true
}

decision := {"decision": "ALLOW", "reason_codes": ["PAC-ALLOW-LOW-RISK-TOOL"]} if allow_low_risk_tool

decision := {"decision": "ESCALATE", "reason_codes": ["PAC-HUMAN-APPROVAL-REQUIRED"]} if {
  input.environment == "prod"
  input.request.risk_tier == "high"
}

decision := {"decision": "QUARANTINE", "reason_codes": ["PAC-RAG-POISONING-SIGNAL"]} if {
  input.memory_context.poisoning_signal == true
}

decision := {"decision": "DENY", "reason_codes": ["PAC-MODEL-DIRECT-SDK-BYPASS"]} if {
  input.model.direct_provider_sdk == true
}

# Appendix B. Policy Bundle Manifest and PR/MR Checklist

policy_bundle_id: aira.agent.runtime
version: 1.1.0
owner: security-architecture
co_owners: [ai-governance, devsecops, platform-engineering]
classification: internal-confidential
packages: [aira.agent.identity, aira.agent.sbac, aira.agent.tool, aira.agent.modelroute,
  aira.agent.memory, aira.agent.delegation, aira.agent.supplychain, aira.agent.incident,
  aira.workspace.systembuilder]
test_command: opa test policies/ tests/
promotion_gate: security_architecture_ai_governance_devsecops
rollback_method: previous_signed_bundle
waiver_allowed: false_for_critical_controls
evidence_path: evidence://ai-governance/policy-as-code/42N/v1.1/

Policy owner and reviewer identified; affected AIRA standards and risk tiers listed.

Positive, negative, escalation, abuse-case, regression, incident, and runtime-toggle tests included.

OPA/conftest results, CI evidence, GitNexus impact, and approval references attached.

Policy bundle version, changelog, signature/hash, rollback path, and previous bundle reference updated.

SBAC skill catalog delta includes owner, expiry, SoD, classification ceiling, environment scope, and evidence.

Security, AI Governance, Architecture, DevSecOps, QA/SDET, and Internal Audit reviews completed where required.

