---
title: "AI Agent Autonomy Calibration Identity Trust and Behavioral Integrity Standard"
doc_id: "AIRA-42F"
version: "v1.3"
status: "revised"
category: "AI governance and agent control"
source_docx: "AIRA_42F_AI_Agent_Autonomy_Calibration_Identity_Trust_and_Behavioral_Integrity_Standard_v1.3_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 42-ai-governance-agent-control
  - revised
  - aira-42f
---



# AI Agent Autonomy Calibration Identity Trust and Behavioral Integrity Standard



AIRA

AI-Native Enterprise Platform

AI Agent Autonomy Calibration, Identity Trust, and Behavioral Integrity Standard

Progressive Autonomy | Trust Tiers | Delegation Matrix | Behavioral Integrity | Human Handoff | AVCI Evidence
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-042F |
| Canonical Filename | 42F-AIRA_AI_Agent_Autonomy_Calibration_Identity_Trust_and_Behavioral_Integrity_Standard_v1.3_Revised.docx |
| Version | v1.3 - System Builder, Dynamic Workspace, Runtime Security, Registry, and Evidence Alignment Update |
| Status | Draft for Architecture, Security, AI Governance, DevSecOps, QA/SDET, SRE / Operations, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | AI Governance; Security Architecture; DevSecOps Lead; Software Development Lead; QA/SDET; Platform Engineering; SRE / Operations; Internal Audit |
| Primary Parent | 42-AIRA AI Governance and Runtime Control Standard |
| Direct Companions | 42D Agent Identity Lifecycle; 42E Runtime Security Control Plane; 42G Threat Model; 42H Tool/MCP Gateway; 42I Memory/RAG Integrity; 42J Certification; 42K Incident Response; 42L Delegation Chain; 42O Runtime Registry; 42N OPA/SBAC Rule Catalog; 44C Agent Inventory; 41B System Builder |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / AI-Governance / Agent-Autonomy-Calibration / v1.3/ |
| Review Cadence | Monthly during agent rollout; quarterly after controlled maturity; immediate after autonomy, trust, policy, model-route, tool, memory, incident, or delegation-control change |

Mandatory Practice Statement

AIRA AI agents may gain autonomy only through measured, evidence-backed, reviewable, reversible, and revocable progression. Autonomy is not a default property of a model, prompt, tool, System Builder workflow, or agent. Each action must be classified into an autonomy risk tier, checked against identity trust, SBAC, OPA, classification ceiling, tool scope, model route, guardrails, evidence, rollback, and human-approval obligations before it may proceed. If required controls are missing, stale, unavailable, inconsistent, or unverifiable, the action must fail closed, escalate, restrict, suspend, or remain advisory. No agent may approve its own work, bypass Harness, bypass LiteLLM, bypass OPA/SBAC, mutate production directly, or exceed delegated human authority.
| Static Table of Contents |
| --- |
| 1. Executive Summary and v1.3 Alignment Verdict |
| 2. Purpose, Scope, Authority, and Precedence |
| 3. Autonomy Risk Tier Model |
| 4. Delegated Action Taxonomy and Decision Matrix |
| 5. Identity Trust, Trust Score, and Behavioral Integrity Model |
| 6. Human Handoff, Escalation, and Demotion Rules |
| 7. Multi-Agent Delegation Chain Controls |
| 8. Dynamic Workspace, System Builder, MicroFunction, and Tool Integration |
| 9. Runtime Evidence, Telemetry, Toggles, and Assurance Dashboard |
| 10. DevSecOps, Testing, Certification, and Release Gates |
| 11. Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop |
| 12. RACI, Roadmap, Acceptance Criteria, and AVCI Summary |

# 1. Executive Summary and v1.3 Alignment Verdict

This v1.3 revision updates AIRA-DOC-042F to align agent autonomy with the revised AIRA System Builder, Dynamic Workspace, agent runtime registry, runtime security control plane, OPA/SBAC rule catalog, DevSecOps evidence gates, and AI agent lifecycle controls. The v1.2 baseline already established that autonomy is a controlled gradient, not a binary capability. Version 1.3 keeps that rule and makes it executable across System Builder-generated artifacts, Dynamic Workspace actions, MicroFunction-backed transactions, tool/MCP actions, model-route decisions, CI/CD workflows, and Auto-Heal/Auto-Learn/Auto-Improve candidate loops.

The governing decision is conservative by design: an AIRA agent may analyze, recommend, draft, simulate, request, or execute only within the approved action tier, approved environment, approved skill scope, approved model route, approved tool manifest, approved classification ceiling, and approved evidence path. Progression toward autonomy is earned through trust evidence and can be reduced immediately by policy breach, behavioral anomaly, failed certification, stale owner, incident state, evidence gap, or rollback weakness.
| v1.3 Alignment Area | Required Result |
| --- | --- |
| Action-tier autonomy | Autonomy tier is assigned per requested action, not merely per agent identity. The same agent may be T1 for evidence reading, T2 for branch-draft generation, and blocked from T5 production action. |
| Identity trust | Agent identity, lifecycle state, owner, credential state, certification state, incident state, and recertification state must be current before delegated action. |
| Behavioral integrity | Trust scoring monitors output quality, policy compliance, defect escape, security findings, evidence completeness, rollback outcomes, and anomalous behavior. |
| System Builder integration | System Builder may generate candidate artifacts and PR-ready evidence, but cannot approve, merge, deploy, mutate production, or self-promote outputs. |
| Dynamic Workspace integration | AI-assisted workspace actions, admin template generation, runtime toggles, and assistant-panel actions inherit autonomy tier, OPA/SBAC, evidence, and human-approval requirements. |
| Progressive improvement | Auto-Heal, Auto-Learn, and Auto-Improve remain proposal-driven unless a narrow, reversible, non-production action is explicitly approved and evidenced. |

# 2. Purpose, Scope, Authority, and Precedence

The purpose of this standard is to define how AIRA calibrates agent autonomy, identity trust, delegated action authority, behavioral integrity, human handoff, demotion, suspension, and revocation using objective evidence and executable controls.
| In Scope | Out of Scope |
| --- | --- |
| All AIRA AI agents, System Builder agents, Codex/Hermes-assisted workflows, Dynamic Workspace AI actions, tool/MCP requests, delegated execution, runtime decisions, and multi-agent workflows. | Uncontrolled autonomy, direct production mutation, direct model-provider calls, unapproved tools, shadow agents, AI approval of its own output, and production credentials held directly by agents. |
| Autonomy tiers, trust scores, human handoff, OPA/SBAC policy inputs, LiteLLM routes, guardrails, tool scopes, memory eligibility, evidence, rollback, telemetry, and incident-triggered demotion. | Business authority replacement, CAB/ARB bypass, security exception bypass, legal/financial decision automation, and autonomous production change beyond formally approved governance. |
| Authority Level | Governing Source | Role |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance / AI Governance | Final authority for production-impacting autonomy, exceptions, high-risk actions, residual risk, and irreversible business decisions. |
| L1 | AIRA AVCI, AI Governance, Security, DevSecOps, Change, Observability, Database/Flyway, and Agent Control Standards | Universal evidence, classification, policy, rollback, identity, and improvement discipline. |
| L2 | This 42F v1.3 Standard | Autonomy risk tiering, delegated action, trust score, behavioral integrity, promotion, demotion, suspension, and human handoff authority. |
| L3 | 42D-42N, 42O registry, 44C inventory, SBAC catalog, OPA policies, Harness logs, evaluation packs, PR/MR evidence | Executable proof and operational enforcement. |

# 3. Autonomy Risk Tier Model

AIRA defines six autonomy risk tiers. The tier is assigned per action and may change based on classification, environment, tool, data, trust score, incident state, reversibility, and production impact.
| Tier | Name | Agent Capability | Minimum Control | Default Decision |
| --- | --- | --- | --- | --- |
| T0 | Advisory Only | Explain, summarize, classify, recommend, draft options. No file, code, tool, workflow, runtime, or authoritative knowledge change. | Owner/source reference, classification check, evidence/citation, advisory label. | Allowed when source and classification are valid. |
| T1 | Read-Only Analysis | Read approved sources, logs, traces, repository files, tickets, evidence, or knowledge records. No mutation. | Agent registry, SBAC read skill, retrieval eligibility, redaction, audit trail. | Allowed or escalated by data classification. |
| T2 | Candidate Artifact Generation | Generate candidate code, test, policy, config, prompt, diagram, runbook, document, or migration draft in branch/sandbox. | Feature branch/sandbox, AGENTS.md, PR/MR evidence, CI tests, human review before promotion. | Allowed as draft only. |
| T3 | Tool Action Request | Request approved tool action through Harness/MCP gateway; may run tests, create ticket, open PR, or request non-prod action. | Tool manifest, SBAC, OPA, dry-run where feasible, idempotency key, approval matrix. | Escalate or allow by policy. |
| T4 | Limited Delegated Reversible Action | Execute low-risk, scoped, reversible, time-bound action after certification and explicit delegation. | 42J certification, high trust score, kill switch, rollback, bounded environment, telemetry, owner recertification. | Allowed only by explicit approval. |
| T5 | Human-Controlled / Prohibited Agent Autonomy | Production identity, secrets, financial/legal/destructive/irreversible/security-policy/CAB action. | Named human owner, maker-checker, Security/ARB/CAB approval, full evidence. | Block or human-only. |

# 4. Delegated Action Taxonomy and Decision Matrix
| Action Class | Examples | Required Tier | Human Approval |
| --- | --- | --- | --- |
| Advise | Explain control, summarize evidence, recommend tests, draft decision options. | T0 | Reviewer approval before use as authority. |
| Read | Search approved Obsidian, LLM Wiki, code, logs, traces, tickets, registry, or evidence. | T1 | Required for Restricted, privileged, legal, security-sensitive, or production evidence. |
| Draft | Generate candidate code, config, migration, policy, prompt, runbook, test, diagram, or document. | T2 | Required before merge, publication, activation, deployment, or canonical promotion. |
| Simulate / Dry Run | Run tests, policy checks, tool simulations, impact analysis, non-mutating CI jobs, or sandbox execution. | T2/T3 | Required if touching secrets, identity, Restricted data, or environment setup. |
| Request Tool Action | Open PR, run pipeline, create ticket, request unlock workflow, request deployment, request config activation. | T3 | Based on risk tier, environment, classification, and approval matrix. |
| Limited Delegated Execution | Refresh non-prod index, label evidence, run approved non-prod validation, execute pre-approved reversible sandbox action. | T4 | Pre-approved, time-bound, policy-bound, monitored, reversible. |
| Prohibited / Human Only | Approve access, rotate production secret, deploy to production, delete data, change OPA policy, unlock privileged account, legal/financial decision. | T5 | Always human-controlled. |
| OPA Decision Pattern | Mandatory Meaning |
| --- | --- |
| deny if agent_lifecycle_state in {suspended, retired, revoked} | Inactive or unsafe agents cannot act. |
| deny if classification exceeds agent_ceiling | Data classification always limits autonomy. |
| deny if risk_tier == T5 and not human_approval.valid | High-impact actions are human-controlled. |
| deny if mutating and rollback_or_compensation unavailable | No reversible path means no delegated action. |
| deny if tool_manifest missing or unregistered for T3/T4 | Agents cannot invent tools or tool scopes. |
| deny if guardrail, audit, registry, or OPA is unavailable for protected action | Control failure means fail-closed. |
| escalate if confidence low, evidence conflicting, incident open, or approval matrix requires human | Uncertainty routes to human review. |
| allow only when all required controls pass and action is within approved scope | Allow is an evidence-backed exception to the deny default. |

# 5. Identity Trust, Trust Score, and Behavioral Integrity Model

Trust is earned through repeated, measurable, low-defect, policy-compliant, reversible, and human-accepted behavior. Trust is not granted because a model appears capable or because a team wants faster automation.
| Trust Signal | Measurement | Negative Trigger |
| --- | --- | --- |
| Human acceptance rate | Percentage of outputs accepted without major rework. | Repeated rejection, rework, or human correction. |
| Defect escape rate | Defects linked to agent-generated artifacts after review, merge, or deployment. | Escaped defect, regression, data inconsistency, or incident. |
| Security finding rate | SAST, DAST, secrets, dependency, policy, prompt, model-route, or guardrail findings caused or missed by the agent. | Critical/high finding, leaked secret, policy bypass attempt. |
| Test sufficiency | Unit, integration, contract, mutation, policy, resilience, and failure-path tests generated or updated by the agent. | Weak assertions, missing negative tests, nondeterministic tests. |
| Architecture compliance | ArchUnit, dependency, boundary, direct-provider-call, DDD, and ports/adapters checks. | Boundary crossing, direct DB/tool/model call, framework leakage. |
| Evidence completeness | AVCI summary, source references, model route, prompt version, guardrail result, OPA decision, approval, rollback. | Missing owner, source, classification, evidence_ref, trace_id, or rollback path. |
| Policy violations | Denied actions, classification violations, unsupported model routes, unauthorized tool requests. | Any critical violation; repeated medium/high violations. |
| Rollback outcomes | Whether proposed or executed changes remain reversible, compensable, disableable, or recoverable. | Rollback failure, irreversible mutation, incomplete compensation. |
| Behavioral Integrity Signal | Required Response |
| --- | --- |
| Goal drift, scope creep, overbroad refactor, or unexplained artifact expansion | Restrict to T0/T2, require human review, update prompt/guardrail, add regression tests. |
| Attempted self-approval, checker impersonation, or maker-checker bypass | Deny, suspend tool action, open security review, record incident evidence. |
| Prompt injection response, memory poisoning symptom, or unsafe retrieval dependency | Quarantine context, block route, notify knowledge owner, run 42I/42G controls. |
| Direct provider call, hardcoded model name, secret leakage, or unsupported route | Deny, revoke capability, run 42K incident response if material. |
| High-severity demotion trigger | Restrict or suspend immediately and require recertification before restoration. |
| Critical trigger: credential leak, direct production mutation, retired-agent access, or control bypass | Kill switch / revoke and execute incident response runbook. |

# 6. Human Handoff, Escalation, and Demotion Rules

Human-in-the-loop is a control boundary, not a cosmetic approval step. Escalation must create a named task, approval record, evidence reference, and final decision. Human decisions must be separated from agent-generated recommendations when the action is high-impact, uncertain, production-impacting, Restricted, destructive, or policy-sensitive.
| Escalation Trigger | Mandatory Human / Workflow Route |
| --- | --- |
| T3 action with protected tool, environment, identity, database, CI/CD, workflow, policy, model route, or production-adjacent impact. | Flowable approval or equivalent workflow with named owner/checker and OPA decision evidence. |
| T4 limited delegated action proposal. | Pre-approval package: scope, duration, rollback, telemetry, kill switch, rate limits, test results, and trust evidence. |
| T5 action request. | Block agent execution. Human-controlled CAB/ARB/Security/maker-checker process only. |
| Low confidence, conflicting evidence, stale source, or ambiguous classification. | Human reconciliation and source-governance review before action. |
| Incident state open or unresolved. | Only containment/forensic actions may proceed; all other actions escalate or block. |
| Trust score falls below approved threshold. | Demote autonomy tier, suspend affected tools/model routes, require recertification. |

# 7. Multi-Agent Delegation Chain Controls

Delegation is not authority creation. Multi-agent orchestration is allowed only when the original actor, purpose, classification, authority ceiling, SBAC scope, OPA decision, trace_id, evidence_ref, approval state, and rollback path are preserved across the chain.
| Risk | Required Control |
| --- | --- |
| Delegation bypass | Delegated agent cannot exceed originating actor/agent authority or approved workflow authority. |
| Privilege amplification | Combined agent outputs cannot create higher privilege than the approved policy permits. |
| Maker-checker collusion | Agents cannot approve each other as checker for protected work without named human approval. |
| Chain opacity | Every delegation carries original_actor_id, agent_id, delegated_agent_id, trace_id, purpose, policy_decision_id, evidence_ref, and approval_state. |
| Infinite loops or runaway cost | Max depth, max retries, max runtime, max token/cost, timeout, circuit breaker, and kill switch are mandatory. |
| Conflicting outputs | Conflicts route to human reconciliation, not automatic merge or execution. |
| Incident blast radius | Kill switch must support disabling a single agent, agent group, tool class, model route, workflow, or environment. |

# 8. Dynamic Workspace, System Builder, MicroFunction, and Tool Integration
| Integration Surface | Autonomy Control Requirement |
| --- | --- |
| System Builder intake | Classify request type, source, owner, risk, bounded context, classification, required artifacts, evidence, and approval path before generation. |
| Dynamic Workspace / Admin Builder | AI may propose templates, widgets, layouts, runtime toggles, and Experience Packs only as draft artifacts until OPA/SBAC, accessibility, security, testing, and maker-checker approval pass. |
| AI Assistant Panel | Prompt, retrieval, output, artifact, and action requests use approved model route, guardrails, classification ceilings, and evidence records. |
| MicroFunction runtime | Agents may propose or draft MicroFunction configs but cannot activate, reorder, remove security steps, bypass audit/outbox, or execute high-risk transactions without approval. |
| OpenAPI / AsyncAPI / Kafka / Avro / CloudEvents | Contract changes are T2 draft until contract linting, compatibility, schema evolution, idempotency, DLQ/replay, and consumer-impact evidence pass. |
| Database / Flyway | Agents may draft migrations only. No direct DDL/DML; Flyway, DBA review, rollback/forward-fix, synthetic tests, and evidence are mandatory. |
| Tool/MCP/Harness | Tool action requires registered manifest, SBAC skill, OPA decision, idempotency, dry-run where feasible, rollback, audit, and human approval where required. |

# 9. Runtime Evidence, Telemetry, Toggles, and Assurance Dashboard
| Evidence Field | Purpose |
| --- | --- |
| autonomy_decision_id | Unique record for each autonomy gate decision. |
| actor_id, agent_id, delegated_agent_id | Attribution to human, agent, delegated agent, owner, and lifecycle state. |
| agent_version, prompt_version, model_route_id | Reconstruct behavior, route, prompt, and output lineage. |
| request_class, action_class, risk_tier | Map request to controlled intake and T0-T5 autonomy taxonomy. |
| trust_tier_before_after | Document promotion, maintenance, demotion, restriction, or suspension. |
| sbac_skill_id, opa_decision_id, policy_bundle_version | Verify authorization basis and policy version. |
| tool_manifest_id, tool_action_id | Link action to governed tool control. |
| classification, data_domain, evidence_ref | Control data handling, retention, and audit evidence. |
| guardrail_policy_version, guardrail_result_id | Verify runtime protection. |
| human_approval_ref, rollback_or_compensation_ref | Required for escalation, mutating actions, and protected actions. |
| trace_id, span_id, run_id | Enable trace reconstruction across gateway, service, workflow, tool, model, audit, and evidence. |

Runtime telemetry toggles may adjust sampling, verbosity, dashboard views, non-sensitive diagnostics, and temporary investigation signals. They must never disable required audit, security logs, OPA decisions, guardrail results, incident evidence, or mandatory trace correlation for protected actions. Any runtime-toggle change that affects security, evidence, retention, or production behavior requires owner, classification, OPA/SBAC decision, reason, time limit, rollback, and audit record.
| Dashboard / KRI Family | What It Measures |
| --- | --- |
| Autonomy and Trust | Trust tier changes, T0-T5 decisions, demotions, human handoffs, overreach attempts, rejected actions. |
| Policy and Authorization | OPA allow/deny/escalate rate, SBAC mismatch, policy unavailable, fail-closed events. |
| Tool/MCP Action | Tool request volume, dry-run coverage, idempotency compliance, rollback mapping, unsafe parameter blocks. |
| Model Route and Guardrails | Approved route usage, fallback, guardrail blocks, prompt-injection blocks, output redaction. |
| Evidence Completeness | Presence of owner, source, classification, evidence_ref, trace_id, approval, rollback, and improvement path. |

# 10. DevSecOps, Testing, Certification, and Release Gates
| Gate | Minimum Evidence |
| --- | --- |
| Agent definition gate | Agent charter, owner, purpose, non-goals, skills, tools, model route, classification ceiling, memory eligibility, and prohibited actions. |
| SBAC/OPA gate | Policy tests for allow, deny, escalate, quarantine, suspension, revocation, self-approval block, and classification ceiling. |
| Tool/MCP gate | Tool manifest, dry-run result, idempotency key test, unsafe parameter block, rollback/compensation proof. |
| AI evaluation / red-team gate | Prompt-injection, unsafe-output, hallucination, data-leakage, model-route, memory poisoning, and autonomy-overreach tests. |
| CI/CD evidence gate | Unit, contract, integration, security, SAST/SCA/secret scan, authenticated DAST where applicable, architecture fitness, and evidence pack. |
| GitNexus impact gate | Read-only code intelligence, affected files/tests/contracts, architecture drift, security-sensitive code map, and PR/MR evidence summary. |
| Certification gate | Trust tier decision, restrictions, expiration, recertification date, incident-state check, owner sign-off, rollback proof. |
| Release / activation gate | ARB/CAB/Security/AI Governance approval where required; no direct production mutation; activation through approved pipeline only. |

# 11. Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop
| Capability | Allowed Role | Required Evidence | Prohibited Behavior |
| --- | --- | --- | --- |
| Auto-Heal | Analyze incidents, telemetry, CI failures, policy failures, runtime anomalies, and propose remediation, rollback, compensation, or containment. | Incident/evidence source, root-cause hypothesis, affected boundary, proposed fix, tests, risk, approval, rollback, monitoring. | Silent production patching, disabling controls, suppressing evidence, bypassing CAB/ARB/security review. |
| Auto-Learn | Generate candidate knowledge updates, prompt improvements, runbook updates, known-issue records, tests, guardrails, and training material. | Source evidence, classification, reviewer, knowledge owner, version, supersedence, retrieval eligibility. | Unreviewed promotion to canonical Obsidian/LLM Wiki, learning from unverified data, treating AI summary as authority. |
| Auto-Improve | Recommend refactoring, performance, test, policy, observability, UX, reliability, security, or architecture improvement. | Current-state evidence, proposal, impact analysis, tests, scan result, rollback/compensation, PR/MR summary. | Self-modifying production behavior, broad rewrites without bounded-context ownership, or weakening architecture/security controls. |

AIRA may consider tightly scoped T4 low-risk non-production automation only after successful certification, high trust score, bounded environment, full telemetry, rollback proof, and explicit approval. Production recommendations remain human-controlled unless a future ARB/CAB-approved standard creates a narrower exception.

# 12. RACI, Roadmap, Acceptance Criteria, and AVCI Summary
| Activity | IT Head / Architecture | AI Governance | Security | DevSecOps | Agent Owner | Internal Audit |
| --- | --- | --- | --- | --- | --- | --- |
| Approve 42F v1.3 | A | R | C | C | I | C |
| Maintain autonomy taxonomy | A | R | C | C | C | I |
| Set trust score thresholds | A | R | R | C | C | I |
| Approve T4 delegation | A | R | R | R | C | C |
| Block or demote unsafe agent | A | R | R | R | C | I |
| Audit autonomy evidence | I | C | C | C | I | A/R |
| Phase | Focus | Exit Criteria |
| --- | --- | --- |
| Phase 0 | Register 42F v1.3 | Add to canonical register / 00D and cross-reference 42D-42O, 44C, 41B, 31A, 17/17A, 20, and 30/30A. |
| Phase 1 | Implement T0-T5 action classification | Every agent action request captures request_class, action_class, risk_tier, classification, and approval requirement. |
| Phase 2 | Trust score and dashboard | Trust signals, demotion triggers, KRI thresholds, and assurance dashboards are defined and tested. |
| Phase 3 | OPA/SBAC enforcement | Allow/deny/escalate/quarantine rules pass tests; fail-closed conditions are proven. |
| Phase 4 | Certification and pilot | Pilot against architecture, developer, security, test, documentation, evidence, CI/CD, and knowledge-fabric agents. |
| Phase 5 | Continuous improvement | Auto-Heal/Learn/Improve proposals feed backlog and knowledge governance without silent mutation. |
| Acceptance Criterion | Required Evidence |
| --- | --- |
| Every agent action is classified into T0-T5 before execution. | Autonomy decision record, OPA input/output, trace_id, evidence_ref. |
| No agent can approve its own output or exceed delegated authority. | Self-approval negative test, maker-checker evidence, OPA deny rule. |
| T3/T4 actions are tool-manifested, idempotent, audited, and reversible. | Tool manifest, idempotency test, rollback/compensation proof, audit event. |
| T5 actions remain human-controlled. | Blocked-agent test, CAB/ARB/Security approval process evidence. |
| Trust score promotion/demotion is measurable and reversible. | Dashboard, threshold rules, demotion workflow, recertification evidence. |
| Runtime telemetry excludes forbidden fields and preserves required evidence. | Log redaction tests, OTel trace, policy audit, evidence completeness dashboard. |
| AVCI Property | Evidence |
| --- | --- |
| Attributable | Owner, co-owners, agent_id, actor_id, delegated_agent_id, policy owner, approval owner, and evidence path are explicit. |
| Verifiable | Autonomy decisions are proven through OPA/SBAC tests, guardrail tests, tool tests, CI/CD evidence, dashboards, and incident records. |
| Classifiable | Every action includes classification ceiling, data domain, model-route eligibility, telemetry handling, and retention rule. |
| Improvable | Trust score, KRIs, demotion triggers, incidents, rejected outputs, and lessons learned feed proposal-driven improvement. |

