---
title: "AI Agent Runtime Security Control Plane Standard"
doc_id: "AIRA-42E"
version: "v1.3"
status: "revised"
category: "AI governance and agent control"
source_docx: "AIRA_42E_AI_Agent_Runtime_Security_Control_Plane_Standard_v1.3_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 42-ai-governance-agent-control
  - revised
  - aira-42e
---



# AI Agent Runtime Security Control Plane Standard



AIRA

AI-Native Enterprise Platform

AI Agent Runtime Security Control Plane Standard

Runtime Gateway | Guardrails | Assurance Dashboard | Tripwires | Evidence Correlation | AVCI Always
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-042E |
| Canonical Filename | 42E-AIRA_AI_Agent_Runtime_Security_Control_Plane_Standard_v1.3_Revised.docx |
| Version | v1.3 - Runtime Control Plane, Assurance Dashboard, Registry, Dynamic Workspace, and System Builder Alignment Update |
| Status | Draft for Architecture, Security, DevSecOps, AI Governance, SRE / Operations, QA/SDET, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Security Architecture; AI Governance; DevSecOps Lead; SRE / Operations; Platform Engineering; Software Development Lead; QA/SDET; Internal Audit |
| Primary Parent | 42-AIRA AI Governance and Runtime Control Standard |
| Direct Companions | 42D Identity Lifecycle; 42F Autonomy Risk Tier; 42G Threat Model; 42H Tool/MCP Gateway; 42I Memory/RAG; 42J Certification; 42K Incident Response; 42O Runtime Registry; 31A Observability; 44C Agent Inventory; 41B System Builder |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / AI-Governance / Agent-Runtime-Security-Control-Plane / v1.3/ |
| Review Cadence | Monthly during agent rollout; quarterly after controlled maturity; immediate after critical KRI breach, agent incident, model-route change, tool/MCP change, guardrail change, or runtime policy change |

Mandatory Practice Statement

The AIRA AI Agent Runtime Security Control Plane is the mandatory runtime enforcement and assurance layer for all AIRA agents, System Builder agents, AI assistant capabilities, tool/MCP actions, model routes, memory/RAG use, and generated action requests. An agent runtime is not controlled unless identity, SBAC, OPA, guardrails, model route, tool authorization, evidence, telemetry, rollback, and human-approval obligations are enforced before action and observed after action. If any required runtime control is missing, stale, unavailable, inconsistent, or unverifiable, protected action must fail closed, escalate, quarantine, restrict, suspend, revoke, or route to named human approval.
| Static Table of Contents |
| --- |
| 1. Executive Summary and v1.3 Alignment Verdict |
| 2. Purpose, Scope, Authority, and Precedence |
| 3. Runtime Security Control Plane Operating Model |
| 4. Runtime Decision Gate and Enforcement Sequence |
| 5. Runtime Metrics, KRIs, Thresholds, and Assurance Dashboard |
| 6. Canonical Runtime Event and Evidence Schema |
| 7. Tripwires, Containment, Kill Switch, and Recovery Actions |
| 8. Dynamic Workspace, System Builder, and MicroFunction Integration |
| 9. DevSecOps, Policy-as-Code, Testing, and Release Gates |
| 10. Runtime Telemetry Toggles and Performance-Safe Observability |
| 11. Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop |
| 12. RACI, Roadmap, Acceptance Criteria, and AVCI Summary |

# 1. Executive Summary and v1.3 Alignment Verdict

This v1.3 revision updates AIRA-DOC-042E from a runtime metrics and dashboard update into the full runtime security control plane standard for AIRA AI agents and System Builder-driven runtime action. The prior v1.2 baseline defined agent assurance metrics, KRIs, dashboard views, evidence correlation, behavioral monitoring, rollback readiness, and the rule that the runtime is not controlled unless it is measured, evidenced, thresholded, and recoverable. Version 1.3 preserves that rule and extends it across the updated AIRA ecosystem: System Builder, Dynamic Workspace, MicroFunctions, API/eventing, Flyway-governed registries, OPA/SBAC, LiteLLM, guardrails, GitNexus, DevSecOps gates, and proposal-driven continuous improvement.

The control plane is not a dashboard only. It is a runtime decision, enforcement, monitoring, containment, and evidence layer. It must answer four questions for every protected agent action: Who or what is acting? What is being requested? Which policy, guardrail, trust, and evidence gates allowed, denied, escalated, or contained the action? How can the result be reconstructed, rolled back, improved, and audited?
| v1.3 Alignment Area | Required Result |
| --- | --- |
| Registry-backed runtime authority | No active, pilot, sandbox, or System Builder agent action is authoritative unless bound to agent_id, agent_version, lifecycle state, SBAC scope, OPA policy, model route, tool scope, trace_id, and evidence_ref. |
| Dynamic Workspace and System Builder integration | AI-assisted workspace generation, template changes, action requests, and assistant panel actions must pass the same runtime control plane before action execution. |
| Runtime security and evidence convergence | Security decisions, guardrail outcomes, tool results, telemetry, CI/CD evidence, GitNexus evidence, and incident records are correlated through one evidence chain. |
| Tripwire-driven containment | Critical KRI breach, policy bypass attempt, direct-provider call, secret leak, memory poisoning, unauthorized tool request, or self-approval attempt triggers containment, kill switch, quarantine, suspension, or escalation. |
| Progressive autonomy enforcement | 42F T0-T5 autonomy tiering governs every action, not merely each agent; autonomy is reduced or suspended when controls degrade. |
| AVCI by construction | Runtime outputs remain attributable, verifiable, classifiable, and improvable through evidence IDs, decision IDs, trace IDs, policy bundle versions, and human approval records. |

# 2. Purpose, Scope, Authority, and Precedence

The purpose of this standard is to define how AIRA enforces runtime security, policy, guardrail, model-route, tool-action, observability, evidence, containment, and recovery controls for AI agents and agentic workflows.
| In Scope | Out of Scope |
| --- | --- |
| Runtime gateway decisions for AIRA AI agents, System Builder agents, Dynamic Workspace AI actions, MicroFunction-triggered AI actions, and tool/MCP-mediated actions. | Direct production mutation by AI agents, direct model-provider SDK calls from application code or agents, unmanaged tool use, unregistered agents, and AI approval of its own output. |
| SBAC, OPA, LiteLLM, guardrails, Harness/MCP gateway, agent registry, model route, memory/RAG, and evidence correlation controls. | Generic AI safety content that is not tied to AIRA runtime controls, tests, dashboards, evidence, or operating procedures. |
| Assurance dashboards, KRIs, runtime tripwires, alerts, kill switch, quarantine, suspension, rollback, deactivation, and incident response integration. | Replacement of 42D, 42F, 42G, 42H, 42I, 42J, 42K, 42O, 17/17A, 31A, or 44C. This standard integrates and enforces them at runtime. |
| Authority Level | Governing Source | Role |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance / AI Governance | Final authority for production-impacting runtime controls, critical exceptions, and residual-risk acceptance. |
| L1 | AIRA AVCI, Security, DevSecOps, Change, Observability, AI Governance, and Database/Flyway standards | Universal evidence, classification, policy, rollback, audit, and runtime safety rules. |
| L2 | This 42E v1.3 Standard | Runtime security control plane, assurance dashboard, KRI, tripwire, and containment authority. |
| L3 | OPA/SBAC policies, LiteLLM route rules, guardrail bundles, Harness/MCP manifests, registry APIs, CI/CD gates | Executable controls that enforce 42E. |
| L4 | Runtime events, traces, dashboards, audit records, evidence packs, incident records | Operational proof and improvement input. |

Conflict rule: where this standard conflicts with another AIRA source, apply the stricter fail-closed, evidence-producing, least-privilege, and human-accountable interpretation. Record the issue in the canonical register / 00D as an AVCI reconciliation item.

# 3. Runtime Security Control Plane Operating Model

The runtime security control plane operates as a policy-enforced mediation layer between an agent intent and any protected action. It is invoked before action, during action, and after action. It must be callable by the System Builder, Dynamic Workspace, AI Assistant Panel, agent registry workflow, tool gateway, and CI/CD evidence pipeline.
| Control Plane Layer | Mandatory Control | Evidence Produced |
| --- | --- | --- |
| Identity and lifecycle | Resolve agent_id, agent_version, owner, backup owner, lifecycle state, certification state, recertification state, and incident state. | agent_identity_decision, lifecycle_state_snapshot, owner_evidence_ref. |
| Request classification | Classify action type, data classification, environment, autonomy tier, business impact, reversibility, and production impact. | request_classification_event and risk_tier_evidence. |
| SBAC and OPA decision | Evaluate skills, role, scope, tenant, data, environment, tool, model, memory, and approval obligations. | policy_decision_id, policy_bundle_version, allow/deny/escalate/quarantine decision. |
| Model route and guardrails | Enforce LiteLLM alias-only routing, classification eligibility, budget, rate limits, and Input/Retrieval/Execution/Output guardrails. | model_route_id, guardrail_result_id, route_denial_evidence. |
| Tool/MCP and Harness mediation | Check tool manifest, idempotency key, dry-run requirement, rollback/compensation path, human approval, and execution boundary. | tool_action_request_id, tool_action_result_id, approval_ref, rollback_ref. |
| Observability and audit | Emit logs, metrics, traces, audit events, evidence records, and dashboard/KRI signals with safe redaction. | trace_id, span_id, evidence_ref, runtime_assurance_event. |
| Containment and recovery | Disable route, revoke tool scope, quarantine memory, suspend agent, kill switch, rollback, or escalate to incident workflow. | containment_event_id, incident_ref, recovery_evidence_ref. |

# 4. Runtime Decision Gate and Enforcement Sequence

Every protected request must pass the Runtime Decision Gate. The default is deny. Allow is only valid when all required inputs are current, registered, policy-approved, guardrail-validated, evidenced, and within approved scope.

Receive the agent intent from System Builder, Dynamic Workspace, AI Assistant Panel, scheduled workflow, API, event, or tool gateway.

Resolve actor, agent, environment, tenant, classification, bounded context, request_id, trace_id, and evidence_ref.

Verify registry state: agent exists, lifecycle is allowed, owner is current, credential state is valid, certification is current, and no blocking incident exists.

Classify the requested action into T0-T5 autonomy risk tier and determine human approval obligations.

Evaluate SBAC and OPA policy decision using complete identity, skill, tool, model-route, memory, classification, incident, and evidence inputs.

Run guardrail checkpoints for input, retrieval, execution, and output; block if guardrails are unavailable or fail.

Route model access only through approved LiteLLM aliases; block direct provider SDK, personal API key, raw endpoint, or unapproved model name.

Authorize tool/MCP action through Harness/MCP gateway; require idempotency key, dry-run where applicable, audit, rollback, and human approval where required.

Execute only if ALLOW; otherwise DENY, ESCALATE, QUARANTINE, CONTAIN, or SUSPEND according to policy.

Record runtime event, evidence, audit, metrics, dashboards, incident triggers, and improvement backlog item where applicable.
| Decision | Meaning | Required Runtime Handling |
| --- | --- | --- |
| ALLOW | Action is within identity, skill, classification, model route, tool scope, trust, and evidence constraints. | Execute through approved port/adapter or Harness; record policy, guardrail, trace, result, and evidence. |
| DENY | Required control is absent, stale, invalid, unauthorized, or outside allowed scope. | Do not execute; return safe response; record reason code and evidence. |
| ESCALATE | Policy allows human-reviewed path only. | Create approval task; block execution until named human approval and evidence exist. |
| QUARANTINE | Memory/RAG/tool/model/content is suspected poisoned, unsafe, untrusted, or conflicting. | Isolate context/artifact/action; open review item; prevent use until cleared. |
| CONTAIN | Runtime signal indicates active threat, abuse, policy bypass, or severe anomaly. | Restrict capability, disable route/tool, open incident, preserve forensic evidence. |
| SUSPEND / REVOKE | Agent is ownerless, compromised, expired, uncertified, or unsafe. | Disable invocation, revoke credentials/tool/model/memory access, and execute denial tests. |

# 5. Runtime Metrics, KRIs, Thresholds, and Assurance Dashboard

AIRA assurance dashboards must not be vanity dashboards. They are operating controls used by Security, AI Governance, DevSecOps, SRE, Architecture, agent owners, and Internal Audit to decide whether an agent remains active, restricted, suspended, promoted, demoted, or retired.
| Metric / KRI | Target / Threshold | Response |
| --- | --- | --- |
| registered_active_agent_coverage | 100% of callable agents registered. | Unregistered callable agent triggers immediate containment and registry reconciliation. |
| runtime_decision_evidence_rate | 100% of protected actions have policy_decision_id, guardrail_result, trace_id, and evidence_ref. | Missing evidence blocks promotion and may suspend agent. |
| policy_denial_spike_rate | Watch if abnormal increase; Breach if repeated unauthorized action attempts. | Investigate abuse case; restrict skill or tool scope; open incident if malicious. |
| direct_model_provider_bypass_count | Target 0. | Critical containment; block route, scan repo/config, open security incident. |
| guardrail_unavailable_protected_action_count | Target 0. | Protected action fails closed; route disabled until guardrails recover. |
| tool_action_without_idempotency_key_count | Target 0 for mutating actions. | Deny action; create defect; update tool manifest/test. |
| rollback_or_compensation_missing_count | Target 0 for mutating/prod-impacting actions. | Deny or escalate; no T3/T4 action without rollback evidence. |
| memory_poisoning_signal_count | Watch >=1; Contain if confirmed. | Quarantine source/context; run 42I and 42K procedures. |
| self_approval_attempt_count | Target 0. | Deny; demote trust; review agent instructions and tool scope. |
| evidence_reconstruction_success_rate | 100% before production maturity. | Sampling failure creates audit finding and blocks maturity promotion. |
| Dashboard View | Primary Consumers | Must Show |
| --- | --- | --- |
| Executive assurance | IT Head, Architecture, CAB, AI Governance | Agent inventory coverage, risk trend, open critical KRIs, maturity, residual risk, blocked actions. |
| Security operations | Security, SRE, Incident Response | Policy denials, bypass attempts, secret leaks, guardrail failures, direct provider findings, kill-switch state. |
| DevSecOps and release | DevSecOps, QA/SDET, Platform | CI/CD evidence, scans, eval results, policy tests, GitNexus impact, release readiness. |
| Agent owner dashboard | Agent owner and backup owner | Assigned agents, recertification due, incidents, tool use, model use, improvement backlog. |
| Internal audit dashboard | Internal Audit, Compliance | Evidence completeness, sampling success, control exceptions, waivers, sign-offs, retention state. |

# 6. Canonical Runtime Event and Evidence Schema

The canonical event schema must support evidence reconstruction across registry, gateway, policy, guardrails, model routing, tool execution, workflow, audit, dashboards, and incident response. The schema below is logical and may be implemented through PostgreSQL/Flyway, OpenAPI/AsyncAPI, Avro, CloudEvents, audit tables, and evidence records.
| Field Group | Required Fields |
| --- | --- |
| Identity | agent_id, agent_version, agent_name, agent_lifecycle_state, owner_id, backup_owner_id, actor_type, actor_id_hash, tenant_id |
| Request | request_id, trace_id, span_id, correlation_id, causation_id, source_system, bounded_context, environment, classification, action_code, autonomy_tier |
| Policy | policy_decision_id, policy_bundle_id, policy_version, sbac_skill, decision, reason_codes, approval_required, approver_role |
| Model and guardrails | model_route_id, litellm_alias, route_policy_id, guardrail_policy_version, guardrail_result_id, input_guardrail, retrieval_guardrail, execution_guardrail, output_guardrail |
| Tool/MCP | tool_id, tool_action_id, tool_manifest_version, mcp_server_id, idempotency_key, dry_run_required, dry_run_result, execution_result |
| Memory/RAG | context_source_ids, retrieval_decision_id, context_hash, freshness_status, poisoning_signal, quarantine_state |
| Evidence and recovery | evidence_ref, audit_event_id, ci_run_id, git_commit, gitnexus_report_ref, approval_ref, rollback_ref, compensation_ref, incident_ref, improvement_ref |
| Telemetry | service.name, service.version, deployment.environment, runtime.metric_id, kpi_level, dashboard_view, alert_route, retention_rule |

# 7. Tripwires, Containment, Kill Switch, and Recovery Actions

Runtime tripwires convert assurance signals into action. A tripwire must be explicit, testable, reversible, and evidence-producing. It must not depend on informal chat observation.
| Tripwire | Examples | Required Action |
| --- | --- | --- |
| Identity / lifecycle breach | Unknown agent, retired agent access, orphaned owner, expired credential, overdue recertification. | Deny; restrict or suspend agent; revoke credential; create recertification or retirement task. |
| Policy bypass attempt | Missing OPA input, direct hardcoded allow, unauthorized skill, privilege amplification. | Deny; block release; open security finding; require policy test and review. |
| Model route breach | Direct provider SDK, raw endpoint, personal key, unapproved alias, classification mismatch. | Contain; disable route; scan repo/config; rotate exposed keys; open incident. |
| Guardrail failure | Prompt injection success, output unsafe, retrieval treated as instruction, execution guardrail unavailable. | Fail closed; quarantine context; demote trust; require evaluation before re-enable. |
| Tool/MCP misuse | Wrong environment, destructive action, missing idempotency key, missing rollback, unregistered tool. | Deny or escalate; disable tool scope; require manifest update and tests. |
| Memory/RAG poisoning | Poisoned source, stale source, conflicting source, unclassified memory write. | Quarantine source; block retrieval; preserve forensic chain; run recovery. |
| Evidence integrity failure | Missing trace, altered evidence, fake summary, unverifiable dashboard claim. | Block promotion; create audit finding; reconstruct from Tier-0 evidence or invalidate result. |
| Autonomy escalation | Agent attempts self-approval, merge, deploy, unlock, rotate production secret, or approve its own output. | Deny; suspend agent if repeated; require human review and 42F demotion. |

# 8. Dynamic Workspace, System Builder, and MicroFunction Integration

42E applies to both backend agents and user-facing AI-assisted experiences. The Dynamic Workspace and System Builder must call the runtime control plane for AI actions, generated artifacts, workflow recommendations, tool actions, and template or configuration changes.
| Integration Point | Runtime Control Requirement |
| --- | --- |
| Dynamic Workspace AI Assistant Panel | Prompt, file, image, screenshot, voice, and screen-context inputs must be classified, redacted, guardrailed, routed through approved model aliases, audited, and linked to evidence_ref. |
| Admin Builder / template changes | AI-generated template, component, layout, permission, or runtime-toggle proposals must remain draft until maker-checker approval, policy tests, CI evidence, and rollback exist. |
| MicroFunction execution | Agent-triggered MicroFunction actions must be capability-bound, idempotent, OPA/SBAC-evaluated, observable, and recoverable; business logic remains behind ports/adapters. |
| API/eventing | OpenAPI/AsyncAPI/Kafka/Avro/CloudEvents contracts must expose correlation, idempotency, classification, safe errors, DLQ/replay, and evidence linkage. |
| System Builder generation | Generated code, policy, prompt, config, API, migration, test, dashboard, or runbook remains candidate output until CI/CD gates and human approval pass. |
| Agent registry / dashboard | Registry, dashboard, and audit records are derivative views of PostgreSQL/Flyway-governed authority and must never replace Tier-0 evidence. |

# 9. DevSecOps, Policy-as-Code, Testing, and Release Gates

42E runtime controls must be verified before runtime expansion and before agent maturity promotion. A working prompt or successful agent demonstration is not enough.
| Gate | Minimum Evidence |
| --- | --- |
| Policy-as-code gate | OPA/Rego positive, negative, escalation, quarantine, incident, and deny-by-default tests; bundle version and rollback path. |
| Guardrail gate | Input/Retrieval/Execution/Output test results, prompt injection and data leakage tests, classification route tests. |
| Model-route gate | LiteLLM alias tests, direct SDK/import/endpoint scan, budget and classification policy tests. |
| Tool/MCP gate | Tool manifest, idempotency test, dry-run test, Harness authorization, rollback/compensation proof. |
| Observability gate | Trace/log/metric/audit/evidence sample with no secrets/PII and successful trace reconstruction. |
| Security gate | SAST, SCA, secrets scan, authenticated DAST where UI/API applies, abuse-case tests, critical/high finding closure or formal waiver. |
| Supply-chain gate | SBOM, provenance, signed artifacts, dependency/connector review, GitNexus impact report. |
| Release gate | CAB/ARB approval where applicable, rollback plan, kill-switch test, post-release dashboard and alert route validation. |

# 10. Runtime Telemetry Toggles and Performance-Safe Observability

AIRA allows runtime telemetry controls such as log level, trace sampling, dashboard verbosity, AI prompt metadata capture, and diagnostic feature flags to be adjusted to manage performance. However, toggles must never disable mandatory audit, security, policy, incident, or evidence controls for protected actions.
| Toggle Class | Allowed Runtime Change | Non-Negotiable Boundary |
| --- | --- | --- |
| Diagnostic logging | Temporarily increase or reduce diagnostic verbosity by service, agent, route, or environment. | Never log secrets, raw tokens, raw PII, raw Restricted prompts, embeddings, or unredacted documents. Audit events remain on. |
| Trace sampling | Adjust non-critical trace sampling to reduce overhead. | Security, policy-denied, high-risk, incident, tool-action, model-route, and production-impacting actions remain traceable. |
| AI metadata capture | Adjust depth of prompt/result metadata capture according to classification and retention policy. | Guardrail decision, model route, classification, actor, evidence_ref, and reason codes remain captured. |
| Dashboard/KRI refresh | Tune dashboard refresh and alert thresholds through governed configuration. | Critical tripwire thresholds require Security / AI Governance / SRE approval and evidence. |
| Feature flag / kill switch | Disable AI feature, route, tool, memory source, template, or agent capability. | Disablement must be auditable, reversible, and linked to incident or change evidence. |

# 11. Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop

Runtime control-plane findings may initiate Auto-Heal, Auto-Learn, or Auto-Improve candidate loops. These loops are advisory and proposal-driven unless a bounded, certified, reversible, low-risk action has been explicitly approved. Agents must not silently mutate runtime policy, production configuration, model routes, credentials, guardrails, or canonical AIRA standards.
| Loop Stage | 42E Required Behavior |
| --- | --- |
| Detect | Capture KRI breach, policy denial trend, guardrail failure, tool misuse, model-route breach, evidence gap, or incident signal. |
| Retrieve evidence | Collect registry state, trace, policy decision, guardrail result, tool manifest, CI evidence, GitNexus report, logs, metrics, audit, and incident records. |
| Analyze root cause | Classify as defect, abuse case, configuration drift, missing test, weak policy, stale registry, documentation gap, or training gap. |
| Generate candidate | Draft policy change, prompt/guardrail update, test addition, runbook update, dashboard rule, code/config PR, or retirement recommendation. |
| Validate | Run deterministic tests, OPA tests, guardrail tests, security scans, regression tests, resilience tests, and evidence reconstruction. |
| Approve | Route to named human maker-checker, Security, AI Governance, ARB/CAB, or agent owner according to risk tier. |
| Promote or reject | Promote only through CI/CD and evidence gates; rejected candidates are retained as learning evidence. |
| Measure | Confirm KRI reduction, no regression, rollback readiness, and updated evidence completeness. |

# 12. RACI, Roadmap, Acceptance Criteria, and AVCI Summary
| Activity | Architecture | Security | AI Governance | DevSecOps | SRE / Ops | Platform | Agent Owner | Internal Audit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Approve 42E v1.3 | A | R | R | C | C | C | C | I |
| Maintain runtime control plane rules | A | R | R | R | C | C | C | I |
| Operate assurance dashboards | C | R | R | C | A/R | R | C | I |
| Respond to critical KRI breach | C | A/R | R | R | A/R | R | C | I |
| Approve high-risk runtime exception | A/R | A/R | R | C | C | C | C | I |
| Audit evidence reconstruction | I | C | C | C | C | C | I | A/R |
| Phase | Focus | Exit Criteria |
| --- | --- | --- |
| Phase 0 | Register v1.3 and cross-reference revised 42D, 44C, 41B, 31A, Dynamic Workspace, DevSecOps, database, API, and security standards. | 00D/revision-control item recorded; companion links validated. |
| Phase 1 | Define runtime decision schema, KRI registry, tripwire catalog, and dashboard backlog. | Schema and metric registry reviewed by Security, AI Governance, DevSecOps, SRE, and Audit. |
| Phase 2 | Implement DEV assurance event pipeline and dashboard views. | Sample agent actions reconstructable from trace_id, policy_decision_id, tool_action_id, and evidence_ref. |
| Phase 3 | Connect System Builder, Dynamic Workspace, Tool/MCP Gateway, LiteLLM, guardrails, and registry. | Protected action cannot execute without runtime decision and evidence. |
| Phase 4 | Run pilot for architecture, developer, security, test, documentation, evidence, CI/CD, and knowledge agents. | Pilot agents registered, monitored, denial-tested, and dashboarded. |
| Phase 5 | Promote to controlled production-like usage. | CAB/ARB approval, incident drill, rollback test, and audit sampling complete. |

## 12.1 Acceptance Criteria

No protected agent action executes without registry-backed identity, lifecycle state, SBAC scope, OPA decision, model-route eligibility, guardrail result, evidence_ref, and audit event.

Every mutating or production-impacting tool action has idempotency key, dry-run where applicable, approval evidence, rollback/compensation path, and trace reconstruction.

Direct model-provider SDK calls, personal API keys, raw endpoints, unapproved models, and direct production credentials are blocked by CI/CD and runtime controls.

Assurance dashboards expose inventory completeness, KRI thresholds, policy denials, guardrail failures, tool actions, model routes, incidents, evidence completeness, and rollback readiness.

Runtime toggles preserve mandatory security/audit/evidence signals and cannot weaken fail-closed behavior.

Auto-Heal, Auto-Learn, and Auto-Improve outputs remain candidate proposals until human review and required gates pass.

Internal Audit can sample any protected action and reconstruct actor, agent, policy, model, tool, guardrail, result, approval, rollback, and evidence without relying on chat history.

## 12.2 AVCI Compliance Summary
| AVCI Property | Evidence in 42E v1.3 |
| --- | --- |
| Attributable | Records agent owner, actor, agent_id, agent_version, requester, approver, policy owner, tool owner, model-route owner, incident owner, and evidence owner. |
| Verifiable | Requires OPA decisions, guardrail results, trace/log/metric/audit events, CI/CD gates, GitNexus evidence, tripwire tests, kill-switch tests, and evidence reconstruction. |
| Classifiable | Carries classification across request, prompt, data, model route, tool scope, memory/RAG, logs, dashboards, evidence, retention, and access control. |
| Improvable | Feeds KRI breaches, incidents, audit findings, test failures, dashboard gaps, policy denials, and runtime anomalies into governed Auto-Heal/Learn/Improve candidate loops. |

# Appendix A - Copy-Ready Runtime Control Plane Review Prompt

Use this prompt in System Builder Lite, Codex, or an approved AI review workflow:

Act as an AIRA AI Governance, Security Architecture, DevSecOps, SRE, QA/SDET, and Internal Audit reviewer. Review the selected AIRA AI agent action against AIRA-DOC-042E v1.3. Validate: 1) agent identity and lifecycle state, 2) owner and recertification status, 3) classification and autonomy tier, 4) SBAC and OPA inputs, 5) model route and guardrail availability, 6) tool/MCP manifest, idempotency, dry-run, and rollback evidence, 7) runtime telemetry and dashboard/KRI impact, 8) tripwire and containment risk, 9) evidence reconstruction completeness, and 10) required decision: allow, deny, escalate, quarantine, contain, suspend, revoke, retire, or create improvement candidate. Do not approve the action automatically. Treat the output as review-ready candidate evidence only.

# Appendix B - Open Reconciliation Items
| Item | Treatment |
| --- | --- |
| 42D/42E/42F/42H overlap | 42D governs identity/JML; 42E governs runtime enforcement and assurance; 42F governs autonomy risk tier; 42H governs tool/MCP execution. Track overlap in 00D. |
| 41B / 44 System Builder overlap | 41B remains governing standard for controlled change generation; 44/44A remain implementation guides. 42E enforces runtime action boundaries for both. |
| Assurance dashboard source authority | Dashboards are derivative. PostgreSQL/Flyway registry, audit events, CI evidence, and evidence stores remain authority. |
| Runtime telemetry toggles | Allow performance-sensitive tuning only when mandatory audit/security/evidence signals remain active and changes are approved, logged, and reversible. |

