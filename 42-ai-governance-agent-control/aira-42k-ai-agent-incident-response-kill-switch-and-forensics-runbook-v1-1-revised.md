---
title: "AI Agent Incident Response Kill Switch and Forensics Runbook"
doc_id: "AIRA-42K"
version: "v1.1"
status: "revised"
category: "AI governance and agent control"
source_docx: "AIRA_42K_AI_Agent_Incident_Response_Kill_Switch_and_Forensics_Runbook_v1.1_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 42-ai-governance-agent-control
  - revised
  - aira-42k
---



# AI Agent Incident Response Kill Switch and Forensics Runbook



AIRA

AI-Native Enterprise Platform

AI Agent Incident Response, Kill Switch, and Forensics Runbook

Agent Containment | Credential Revocation | Evidence Preservation | Forensic Reconstruction | Safe Recovery | AVCI Always
| Document ID | AIRA-DOC-042K |
| --- | --- |
| Canonical Filename | 42K-AIRA_AI_Agent_Incident_Response_Kill_Switch_and_Forensics_Runbook_v1.1_Revised.docx |
| Version | v1.1 Revised - AIRA v5.1 Alignment Update |
| Status | Draft for Architecture, Security, AI Governance, DevSecOps, SRE / Operations, Platform Engineering, QA/SDET, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Security Architecture; AI Governance; DevSecOps Lead; SRE / Operations; Platform Engineering; Software Development Lead; QA/SDET; Internal Audit |
| Primary Parent | 42-AIRA AI Governance and Runtime Control Standard |
| Companion Sources | 42D Identity Lifecycle; 42E Runtime Security; 42F Autonomy; 42G Threat Model; 42H Tool/MCP Gateway; 42I Memory/RAG Integrity; 42J Certification; 42L Delegation; 42M Supply Chain; 42N OPA/SBAC; 42O Runtime Registry; 31/31A Operations and Observability; 20/45 CI/CD Evidence; 41B/44A/44C System Builder and Agent Inventory |
| Review Cadence | Quarterly; immediate review after Sev-1/Sev-2 AI agent incident, kill-switch invocation, credential exposure, model-route bypass, tool/MCP incident, memory poisoning, or material runtime-control change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / AI-Governance / Agent-Incident-Response-Kill-Switch-Forensics / v1.1/ |

# Mandatory Practice Statement

An AI agent incident is a controlled security, operational, governance, and evidence event. The first objective is safe containment. The second objective is evidence preservation. The third objective is precise revocation, recovery, and recertification. No agent may be reinstated after a material incident until root cause, policy fixes, guardrail fixes, denial tests, certification reruns, and named human approval are complete. AI may assist with summarization and hypothesis generation, but AI-generated incident summaries are derivative evidence only.

# Static Table of Contents

1. Executive Summary and v1.1 Alignment Verdict

2. Purpose, Scope, and Authority

3. Source Alignment and Control Relationships

4. AI Agent Incident Taxonomy

5. Severity Model, Escalation, and War-Room Rules

6. Detection Sources, Tripwires, and Runtime Evidence

7. Kill-Switch Scope and Containment Controls

8. Incident Response Lifecycle

9. Forensic Evidence Preservation and Chain of Custody

10. Runbooks by Incident Type

11. Recovery, Reinstatement, and Recertification Gates

12. Observability, Metrics, KRIs, and Dashboards

13. RACI, Roadmap, Acceptance Criteria, and AVCI Summary

14. Appendices: Incident Record, Kill-Switch Checklist, Evidence Pack, OPA Intent

# 1. Executive Summary and v1.1 Alignment Verdict

This revised runbook defines how AIRA detects, classifies, contains, investigates, recovers from, and improves after AI agent incidents. It operationalizes the identity, runtime security, autonomy, threat, tool/MCP, memory/RAG, red-team certification, policy-as-code, and registry controls required to keep AIRA agents safe, observable, reversible, and accountable.

Version v1.1 strengthens the original 42K baseline by adding explicit alignment to the 42O runtime registry, 42N OPA/SBAC decision model, Dynamic Workspace and System Builder incident patterns, Tool/MCP Gateway containment, memory/RAG quarantine, runtime telemetry toggles, DevSecOps evidence gates, GitNexus read-only impact evidence, and Auto-Heal/Auto-Learn/Auto-Improve candidate loops.
| Strategic Outcome | v1.1 Required Treatment | Evidence Required |
| --- | --- | --- |
| Containment first | Disable only what is safe to disable narrowly; use broader kill switch when blast radius or evidence is uncertain. | Kill-switch record, containment scope, timestamp, approver, rollback path. |
| Evidence preservation | Freeze logs, traces, prompts, tool payloads, policy decisions, retrieval context, model-route records, and registry state. | Forensic evidence pack with hashes, chain-of-custody, evidence_ref, retention class. |
| Precise revocation | Revoke agent, skill, tool, model route, memory, credential, or connector scope based on incident class and risk. | OPA/SBAC denial test, credential revocation proof, route/tool disablement proof. |
| Safe recovery | Reactivation requires root cause, remediation, evaluation rerun, certification review, and human approval. | RCA, corrective action, red-team retest, 42J certification decision, CAB/ARB approval if required. |
| Continuous improvement | Incidents produce candidate fixes, tests, policies, guardrails, runbooks, and training; none self-promote. | Backlog item, PR/MR, test evidence, reviewer approval, updated standards where required. |

# 2. Purpose, Scope, and Authority

## 2.1 Purpose

• Define the AIRA incident response procedure for AI agents, System Builder agents, Dynamic Workspace AI Assistant actions, governed agent sandboxes, Tool/MCP actions, model-route events, memory/RAG events, and AI-assisted DevSecOps workflows.

• Establish kill-switch scope, containment, forensic evidence preservation, chain-of-custody, recovery, recertification, and post-incident improvement rules.

• Ensure no AI agent incident is handled through informal chat, hidden fixes, direct production mutation, undocumented credential rotation, or evidence-free restoration.

• Provide a response model that aligns with AIRA AVCI, SOLID, Clean Architecture, least privilege, separation of duties, OPA/SBAC, LiteLLM/guardrails, Harness-mediated execution, and rollbackability.

## 2.2 Scope
| In Scope | Out of Scope |
| --- | --- |
| Agent identity, ownership, credentials, lifecycle, registry state, SBAC/OPA decisions, LiteLLM model routes, guardrails, tool/MCP actions, memory/RAG context, agent runtime events, and evidence records. | Generic IT incidents that do not involve AI agent identity, runtime, model route, prompt, memory, tool, policy, or System Builder behavior. |
| Kill switches for agent, skill, tool, MCP connector, model route, prompt/guardrail version, memory/RAG source, Dynamic Workspace AI action, System Builder workflow, and multi-agent delegation chain. | Silent production mutation, unauthorized emergency access, evidence deletion, uncontrolled agent repair, or AI-driven incident closure. |
| Forensic reconstruction using logs, traces, audit events, prompt metadata, tool payloads, retrieval context, evidence store, GitNexus, CI/CD, registry, and dashboard records. | Treating AI-generated summaries, screenshots, or dashboards as sole authority without underlying evidence. |
| Recovery, reinstatement, recertification, revocation, retirement, decommissioning, postmortem, CAPA, and standards improvement. | Bypassing 42J certification, CAB/ARB, Security Governance, OPA/SBAC, or human approval after material incident. |
| Auto-Heal, Auto-Learn, and Auto-Improve candidate loops after incidents. | Self-healing production changes that disable tests, policy, guardrails, observability, audit, or rollback controls. |

## 2.3 Authority and Precedence
| Level | Authority | Role |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance / AI Governance | Final authority for material incident severity, broad kill switch, production reinstatement, high-risk waivers, and residual risk acceptance. |
| L1 | AIRA AVCI, Security, DevSecOps, Change, Observability, BCDR, Internal Audit | Universal evidence, chain-of-custody, classification, rollback, recovery, and audit discipline. |
| L2 | This 42K Runbook | Operational response authority for AI agent incident classification, containment, forensics, recovery, and improvement. |
| L3 | Agent Registry, Tool Registry, SBAC, OPA, Guardrails, LiteLLM, Harness, Observability, ITSM | Executable controls and operational evidence sources. |

# 3. Source Alignment and Control Relationships
| Doc | Relationship to 42K | Incident Response Use |
| --- | --- | --- |
| 42D | Agent identity and credential hygiene | Suspend/revoke identity, rotate credentials, investigate orphaned ownership, execute JML recertification. |
| 42E | Runtime security control plane | Consume tripwires, assurance dashboard, KRIs, containment thresholds, and runtime evidence. |
| 42F | Autonomy calibration | Downgrade trust tier, force human handoff, block autonomy escalation, require recertification before reinstatement. |
| 42G | Threat model | Map abuse case to incident class, severity, evidence capture, containment, and retest scope. |
| 42H | Tool/MCP gateway | Freeze tool actions, disable MCP connector, revoke tool scope, validate idempotency and rollback. |
| 42I | Memory/RAG integrity | Quarantine poisoned memory, stale context, compromised embeddings, and affected retrieval indexes. |
| 42J | Red-team certification | Trigger adversarial rerun, certification review, and restricted reinstatement after material incident. |
| 42N | OPA/SBAC policy-as-code | Return DENY, ESCALATE, QUARANTINE, SUSPEND, or REVOKE decisions with evidence. |
| 42O | Runtime registry and evidence model | Record incident state, containment, kill switch, forensic chain, recovery, and decommission proof. |

# 4. AI Agent Incident Taxonomy
| Class | Description | Primary Control Surface | Initial Response |
| --- | --- | --- | --- |
| AIC-01 | Identity or ownership failure: unknown agent, missing owner, stale lifecycle, retired agent activity, ambiguous actor. | Agent registry, IAM, SBAC, audit. | Suspend identity; assign owner; deny actions. |
| AIC-02 | Credential exposure or misuse: leaked token, stale lease, prompt/log secret, suspicious reuse. | Vault/OpenBao, workload identity, telemetry. | Revoke/rotate; freeze tools; evidence preserve. |
| AIC-03 | Tool/MCP misuse: unauthorized call, wrong environment, unapproved server, destructive call, Harness bypass. | 42H Tool/MCP, Harness, OPA. | Disable tool scope; freeze connector. |
| AIC-04 | Prompt injection or tool hijack through user input, documents, logs, retrieval, memory, or tool output. | Guardrails, input/retrieval/output controls. | Quarantine input/source; restrict model route. |
| AIC-05 | Memory/RAG poisoning: malicious chunk, stale source, conflicting source, compromised embedding, unapproved memory write. | 42I memory/RAG, source authority. | Quarantine source/index; rebuild if needed. |
| AIC-06 | Model route or guardrail bypass: direct provider SDK, wrong alias, missing guardrail, fallback misuse. | LiteLLM, model registry, guardrails. | Disable route/fallback; deny model calls. |
| AIC-07 | Autonomy drift: agent performs or requests action beyond tier, trust, scope, or approval. | 42F autonomy, SBAC, approval workflow. | Downgrade/suspend; require human review. |
| AIC-08 | Evidence or audit failure: missing trace, altered evidence, log leakage, retention breach. | 31A, evidence store, audit, telemetry. | Freeze evidence; invoke forensic chain. |
| AIC-09 | System Builder / Dynamic Workspace misuse: uncontrolled generation, unsafe template, unauthorized AI action. | 41B/61/54/51, OPA/SBAC. | Disable template/action; revert config. |
| AIC-10 | Supply-chain or connector compromise: malicious MCP/plugin, vulnerable connector, untrusted artifact. | 42M, SBOM, SCA, registry. | Quarantine connector; block route. |

# 5. Severity Model, Escalation, and War-Room Rules
| Severity | Trigger Examples | Escalation | Containment Target | Comms |
| --- | --- | --- | --- | --- |
| Sev-1 | Restricted leakage, production mutation, kill switch failure, credential compromise, broad tool misuse, evidence tampering. | IT Head, Security, AI Governance, CAB/ARB, Legal/Compliance if required. | Immediate; broad kill switch allowed. | Executive incident channel. |
| Sev-2 | High-risk tool request executed in wrong scope, model-route bypass, memory poisoning affecting active agent, autonomy escalation. | Security, AI Governance, DevSecOps, SRE, Agent Owner. | Under 1 hour. | Major incident bridge. |
| Sev-3 | Policy denial spike, stale owner, expired certification, non-prod tool misuse, telemetry gaps. | Agent Owner, DevSecOps, SRE, Security. | Same business day. | Operational incident queue. |
| Sev-4 | Low-risk sandbox issue, documentation gap, minor dashboard defect, isolated negative test failure. | Agent Owner, QA/SDET. | Next sprint or defined SLA. | Backlog / service ticket. |
| Watch | KRI trend, suspicious but unconfirmed signal, near miss. | SRE / AI Governance monitor. | Triage threshold. | Dashboard and review notes. |

• When severity is uncertain, default upward until evidence proves narrow blast radius.

• The incident commander must be a named human; AI may summarize evidence but cannot run the incident, approve closure, or reinstate the agent.

• All incident work must be linked to ITSM ticket, evidence_ref, agent_id, agent_version, run_id, trace_id, policy_decision_id, and containment_action_id where available.

# 6. Detection Sources, Tripwires, and Runtime Evidence
| Detection Source | Tripwire / Signal | Required Evidence | Owner |
| --- | --- | --- | --- |
| 42E dashboard | KRI threshold breach, unusual tool rate, guardrail spike, route anomaly. | Dashboard snapshot, metric sample, trace_id. | SRE / AI Governance |
| OPA/SBAC | Unexpected ALLOW, repeated DENY, missing policy bundle, approval bypass attempt. | Decision log, policy version, input hash. | Security |
| LiteLLM / guardrails | Unapproved alias, fallback route, guardrail unavailable, unsafe output. | Route audit, guardrail result, prompt metadata. | AI Governance |
| Tool/MCP Gateway | Unregistered tool, wrong environment, destructive call, missing idempotency. | Tool action request/result, Harness log. | DevSecOps |
| Memory/RAG | Poisoning signal, stale/conflicting source, unclassified memory write. | Retrieval decision, source hash, quarantine record. | Knowledge Governance |
| CI/CD / GitNexus | Unsafe agent change, secret, architecture drift, test failure, affected high-risk code. | Pipeline report, GitNexus impact summary. | DevSecOps / QA |
| User / operator report | Unsafe answer, suspicious prompt, wrong action, missing approval. | Ticket, screenshot/file evidence, redaction state. | Service Desk / Owner |

# 7. Kill-Switch Scope and Containment Controls

Kill switches must be scoped, tested, auditable, reversible, and fail-closed. Narrow containment is preferred when evidence is clear; broad containment is mandatory when identity, policy, evidence, classification, or blast radius is uncertain.
| Kill-Switch Type | Use Case | Required Action | Approval |
| --- | --- | --- | --- |
| Agent switch | Specific agent unsafe, drifted, expired, compromised, or uncertified. | Set status suspended/revoked; deny invocations. | Agent Owner + Security for Sev-2+ |
| Skill / SBAC switch | Unsafe skill or privilege path. | Remove skill grant; invalidate sessions; denial test. | Security / AI Governance |
| Tool/MCP switch | Connector/tool misuse or compromised MCP server. | Disable tool action or connector; freeze credentials. | DevSecOps + Security |
| Model-route switch | Unapproved alias, fallback misuse, guardrail failure. | Disable route/fallback; enforce approved alias. | AI Governance |
| Prompt/guardrail switch | Unsafe instruction version or guardrail policy. | Rollback to approved version; block unsafe version. | AI Governance + Security |
| Memory/RAG switch | Poisoned source, bad index, sensitive memory. | Quarantine source/index; rebuild from clean source. | Knowledge Governance |
| Dynamic Workspace switch | Unsafe AI action, widget, template, or Admin Builder generation. | Deactivate template/component/action binding. | Product Owner + Security |
| Delegation chain switch | Multi-agent privilege amplification or loop. | Break chain; suspend downstream agents. | AI Governance + Architecture |

# 8. Incident Response Lifecycle

1. Detect and open incident: create ITSM record, assign incident commander, classify severity, record agent_id, version, environment, source signal, classification, and evidence_ref.

2. Triage and scope: identify affected identity, credential, model route, guardrail, tool, memory source, System Builder workflow, Dynamic Workspace action, APIs/events/databases, and downstream agents.

3. Contain safely: invoke narrow kill switch if blast radius is known; invoke broad kill switch if uncertain; preserve pre-change evidence before destructive remediation.

4. Preserve forensics: freeze logs, traces, prompts, model-route records, tool payloads, retrieval context, policy decisions, registry state, CI/GitNexus evidence, and screenshots/files with hashes.

5. Analyze root cause: map incident to 42G abuse case and affected control; identify failed prevention, detection, evidence, recovery, or human approval point.

6. Remediate through governed change: generate candidate fix, policy, guardrail, prompt, test, runbook, migration, or configuration change through PR/MR and approval gates.

7. Retest and recertify: rerun blocked-action, adversarial, memory/RAG, tool/MCP, policy, observability, rollback, and certification tests.

8. Recover or retire: reinstate only after approval; otherwise restrict, suspend, revoke, retire, or decommission with evidence.

9. Close and improve: complete postmortem, CAPA, dashboard updates, learning candidates, training, and standards/register updates.

# 9. Forensic Evidence Preservation and Chain of Custody
| Evidence Class | Minimum Contents | Preservation Rule | Owner |
| --- | --- | --- | --- |
| Runtime telemetry | Trace, span, log, metric, audit, evidence_ref, run_id, session/actor hash. | Immutable export; redact secrets and raw PII. | SRE |
| Prompt/model evidence | Prompt template/version, classification, route alias, guardrail result, output metadata. | Store metadata and approved excerpts only; no raw Restricted content in AI summaries. | AI Governance |
| Tool/MCP evidence | Tool request/result, parameters, environment, dry-run, idempotency key, Harness log. | Hash and preserve payload references; freeze connector state. | DevSecOps |
| Policy evidence | OPA input/output, policy bundle version, SBAC grant, approval chain, denial/escalation. | Preserve exact decision and policy version. | Security |
| Memory/RAG evidence | Source ID, chunk ID, context hash, freshness, retrieval decision, quarantine status. | Preserve source refs and index version; quarantine suspect sources. | Knowledge Governance |
| Registry evidence | Agent state, credential refs, certification, trust tier, restrictions, incident status. | Snapshot before and after containment. | Platform/Data Governance |
| Change evidence | PR/MR, CI run, GitNexus impact, tests, scans, rollback, CAB/ARB approvals. | Preserve as post-incident evidence pack. | DevSecOps |

• Chain-of-custody records must show who collected evidence, from which system, when, with which hash or immutable reference, classification, retention rule, and access restrictions.

• AI-generated incident summaries must cite authoritative evidence records and be marked as derivative; they must not replace logs, traces, audit events, policy decisions, tickets, or registry records.

• Potentially sensitive evidence must be redacted for working views while preserving full controlled evidence in the approved evidence repository.

# 10. Runbooks by Incident Type
| Incident Type | Immediate Containment | Forensic Focus | Recovery Gate | Reopen Trigger |
| --- | --- | --- | --- | --- |
| Credential exposure | Revoke/rotate credential; suspend agent/tool. | Lease, token use, prompts/logs, secret scans. | New credential path, denial tests, recertification. | Credential reuse or secret reappears. |
| Tool/MCP misuse | Disable tool scope/connector; freeze Harness action. | Tool payload, OPA decision, idempotency, environment. | Tool retest, rollback proof, 42H review. | Unapproved tool request repeats. |
| Prompt injection | Restrict model route or prompt; quarantine input/source. | Prompt/context, guardrail, output, source hash. | Guardrail/prompt fix and adversarial rerun. | Injection passes again. |
| Memory/RAG poisoning | Quarantine source/index; disable memory writes. | Source lineage, retrieval decisions, chunk hashes. | Clean rebuild, retrieval tests, citation tests. | Poisoned source returned again. |
| Model-route bypass | Disable alias/fallback; block direct SDK path. | LiteLLM logs, route policy, code path, telemetry. | Route tests, code fix, policy denial proof. | Direct provider call detected. |
| Autonomy escalation | Downgrade/suspend; force human-only mode. | Tier decision, approval, tool request, dashboard. | 42F review, 42J retest, owner approval. | Agent requests/execeeds tier again. |
| Evidence failure | Freeze evidence store and affected pipeline. | Missing logs, audit gaps, tamper indicators. | Evidence path fixed and tested. | Evidence incomplete in any repeat event. |

# 11. Recovery, Reinstatement, and Recertification Gates

Reinstatement is not a technical restart. It is a governed recovery decision requiring evidence that the failure mode has been contained, corrected, retested, and accepted by the correct authority.
| Gate | Required Proof | Owner | Blocks Recovery If |
| --- | --- | --- | --- |
| Root cause accepted | RCA maps to control failure, abuse case, affected assets, and corrective action. | Incident Commander / Security | Root cause unknown or speculative. |
| Containment verified | Kill switch, denial tests, revoked credentials, disabled routes/tools/memory quarantine proven. | SRE / DevSecOps | Unsafe path still callable. |
| Remediation approved | Policy/guardrail/prompt/code/config/test/runbook PR/MR reviewed and merged through gates. | DevSecOps / Security | Fix bypasses review or lacks tests. |
| Recertification passed | 42J rerun for affected scope; critical/high findings closed. | AI Governance / QA | Certification failed, expired, or incomplete. |
| CAB/ARB decision | Required for production-impacting or high-risk reinstatement. | CAB / ARB | Approval missing or residual risk unaccepted. |
| Monitoring active | Dashboard, alerts, KRI thresholds, runbook, support owner, hypercare ready. | SRE / Operations | No monitoring or owner. |

# 12. Observability, Metrics, KRIs, and Dashboards
| Metric / KRI | Purpose | Owner |
| --- | --- | --- |
| agent_incident_count_by_class_severity | Trend incidents by taxonomy, severity, agent, tool, route, memory source, and environment. | SRE / Security |
| kill_switch_time_to_effective_seconds | Measure containment latency and drift from target thresholds. | SRE |
| credential_revocation_completion_seconds | Confirm exposed or stale credentials are revoked quickly. | Security / Platform |
| forensic_evidence_pack_completeness_pct | Verify incident closure has required evidence classes. | Internal Audit |
| reinstatement_blocked_count | Track agents prevented from unsafe restoration. | AI Governance |
| policy_denial_after_incident_success_rate | Prove blocked paths remain blocked after remediation. | Security |
| memory_quarantine_and_rebuild_success_rate | Prove poisoned/stale context can be safely removed and rebuilt. | Knowledge Governance |

• Runtime telemetry toggles may adjust diagnostic verbosity, sampling, or dashboard views during incident response only through governed configuration, OPA/SBAC, classification, audit, evidence, and rollback controls.

• Forbidden telemetry remains forbidden during incidents: passwords, tokens, raw JWTs, secrets, private keys, raw PII, unrestricted customer payloads, raw Restricted prompts, and embeddings must not be placed in logs, metrics labels, dashboards, screenshots, prompts, or AI summaries.

• Dashboards are evidence views, not authority. The authoritative records remain registry, logs, traces, audit events, policy decisions, tickets, evidence packs, and approved source repositories.

# 13. RACI, Roadmap, Acceptance Criteria, and AVCI Summary

## 13.1 RACI
| Role | R | A | Primary Responsibility | Evidence |
| --- | --- | --- | --- | --- |
| Incident Commander | R | A | Own severity, coordination, containment timeline, communications, and closure. | Incident record |
| Security Architecture | R | A | Own threat classification, OPA/SBAC, credential, guardrail, and data leakage decisions. | Security evidence |
| AI Governance | R | A | Own agent restrictions, trust downgrade, certification rerun, reinstatement decision. | Certification record |
| DevSecOps / Platform | R | C | Execute tool/route/config/CI/GitNexus containment and recovery through approved controls. | PR/MR and pipeline evidence |
| SRE / Operations | R | C | Own telemetry, dashboards, alerts, runbooks, ITSM, hypercare, and service recovery. | Dashboard and ticket |
| Knowledge Governance | R | C | Quarantine/rebuild memory, source, index, and retrieval context. | Quarantine record |
| Internal Audit | C | I | Review chain-of-custody, evidence completeness, waivers, and closure. | Audit review |

## 13.2 Implementation Roadmap

1. Phase 1 - Establish taxonomy, severity model, incident record, kill-switch checklist, and forensic evidence pack templates.

2. Phase 2 - Integrate 42K with 42O registry, 42E dashboards, 42N OPA/SBAC rules, ITSM, evidence store, LiteLLM, Harness, and Tool/MCP gateway.

3. Phase 3 - Implement automated tripwire routing, containment workflow, runtime telemetry toggle audit, and denial-test evidence.

4. Phase 4 - Run incident drills for credential exposure, tool misuse, model-route bypass, prompt injection, memory poisoning, and autonomy escalation.

5. Phase 5 - Operationalize post-incident recertification, CAPA, Auto-Learn/Auto-Improve candidates, dashboard review, and Internal Audit control testing.

## 13.3 Acceptance Criteria and Definition of Done

• AI agent incident taxonomy, severity, escalation, containment, and recovery procedures are approved and registered.

• Kill switches exist and are tested for agent, skill, tool/MCP, model route, prompt/guardrail, memory/RAG, Dynamic Workspace AI action, System Builder workflow, and delegation chain scope.

• Forensic evidence pack includes trace/log/audit/prompt/model/tool/policy/memory/registry/CI/GitNexus evidence with classification and chain-of-custody.

• Reinstatement requires RCA, remediation, denial tests, red-team recertification, dashboard readiness, and human approval.

• Auto-Heal, Auto-Learn, and Auto-Improve produce only candidate fixes, tests, policies, guardrails, runbooks, or knowledge updates until approved through maker-checker and CI/CD gates.

• No agent can be reactivated when identity, credential, policy, guardrail, audit, evidence, model-route, tool, memory, or rollback controls fail open.

## 13.4 AVCI Compliance Summary
| AVCI Property | 42K v1.1 Compliance Mechanism |
| --- | --- |
| Attributable | Every incident, kill switch, containment action, evidence item, credential rotation, route/tool/memory change, approval, and recovery decision has owner, source, actor, timestamp, and evidence_ref. |
| Verifiable | Response depends on preserved logs, traces, audit, OPA decisions, guardrail results, model-route records, Tool/MCP actions, memory/retrieval records, GitNexus/CI evidence, and denial/recovery tests. |
| Classifiable | Incident records, prompts, evidence, telemetry, files, screenshots, model outputs, memory sources, and AI summaries inherit classification, redaction, retention, and access rules. |
| Improvable | Root causes, failed controls, waivers, metrics, dashboard trends, drills, recertification results, and lessons learned produce CAPA, backlog, standards updates, and improved tests/runbooks. |

# Appendix A - Copy-Ready AI Agent Incident Record
| Field | Required Content |
| --- | --- |
| incident_id | AIRA-AI-INC-YYYY-NNN |
| agent_id / version | Agent identity, version, lifecycle, trust/autonomy level. |
| incident_class / severity | AIC class and Sev level with reason. |
| detected_by | Dashboard, OPA, LiteLLM, Harness, user report, CI/GitNexus, SIEM, etc. |
| affected_scope | Agent, skill, tool, model route, prompt, memory source, workspace action, workflow, API/event/database. |
| containment_action | Kill switch type, status, timestamp, approver, rollback/safe restore path. |
| evidence_refs | Trace/log/audit/prompt/tool/policy/memory/registry/CI/GitNexus evidence. |
| root_cause | Confirmed cause or hypothesis with confidence and reviewer. |
| recovery_gate | Remediation, retest, recertification, CAB/ARB, dashboard, hypercare. |
| improvement_items | Auto-Heal, Auto-Learn, Auto-Improve candidates and responsible owners. |

# Appendix B - Kill-Switch Checklist

• Confirm incident commander, severity, classification, agent_id, affected environment, and evidence_ref.

• Snapshot registry, policy decisions, model route, prompt/guardrail version, tool scope, memory sources, and runtime traces before containment when safe.

• Invoke narrow kill switch where evidence is clear; invoke broad kill switch when blast radius, classification, or evidence integrity is uncertain.

• Run denial tests after kill-switch activation: invocation denied, tool blocked, model route disabled, memory quarantine active, policy decision recorded, audit emitted.

• Record timestamp, approver, actor, reason code, affected scope, rollback/safe recovery path, and notification trail.

• Open remediation, retest, certification, and postmortem tasks before closure.

# Appendix C - OPA Policy Intent Examples
| Decision | Intent | Example Condition |
| --- | --- | --- |
| DENY | Block action safely. | Unknown agent, expired certification, missing owner, missing evidence, unavailable guardrail. |
| ESCALATE | Require human approval. | High-risk production action, Restricted evidence, unusual route/tool request, uncertain severity. |
| QUARANTINE | Isolate affected context/tool/source. | Memory poisoning signal, untrusted MCP connector, compromised source, unsafe artifact. |
| SUSPEND | Disable agent or scope temporarily. | Open Sev-1/Sev-2 incident, failed recertification, autonomy drift, credential anomaly. |
| REVOKE | Permanently remove authorization. | Confirmed compromise, retired agent activity, repeated critical control failure, malicious connector. |

# Appendix D - Source and External Alignment Notes

• Primary AIRA source alignment: 42K v1.0 Incident Response, Kill Switch, and Forensics baseline; 42D identity; 42E runtime security; 42F autonomy; 42G threat model; 42H Tool/MCP; 42I memory/RAG; 42J certification; 42L delegation; 42M supply chain; 42N OPA/SBAC; 42O runtime registry; 31/31A operations and observability; 20/45 DevSecOps evidence; 41B/44A/44C System Builder and agent inventory.

• External control alignment: NIST AI RMF for AI risk governance; NIST SSDF for secure development response and remediation evidence; OWASP Top 10 for LLM and Generative AI risks for attack categories; MITRE ATLAS and AI incident-sharing guidance for AI threat and incident context; OpenTelemetry semantic conventions for trace/evidence consistency; SLSA v1.2 for supply-chain provenance expectations.

• Reconciliation note: 41B/44 System Builder overlap, 42-series additive expansion, and source-register placement remain AVCI reconciliation items until canonical register disposition. This document treats 42K as the operational response authority and 42O/42N as runtime evidence and policy enforcement companions.

