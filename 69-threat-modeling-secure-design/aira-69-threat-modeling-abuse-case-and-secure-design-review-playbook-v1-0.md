---
title: "Threat Modeling Abuse Case and Secure Design Review Playbook"
doc_id: "AIRA-69"
version: "v1.0"
status: "final"
category: "Threat modeling and secure design"
source_docx: "AIRA_69_Threat_Modeling_Abuse_Case_and_Secure_Design_Review_Playbook_v1.0.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 69-threat-modeling-secure-design
  - final
  - aira-69
---



# Threat Modeling Abuse Case and Secure Design Review Playbook



AIRA
AI-Native Enterprise Platform

Threat Modeling, Abuse Case, and Secure Design Review Playbook

AIRA-DOC-069 | Version v1.0 | Secure-by-Design Gate Standard
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-069 |
| Document Title | AIRA Threat Modeling, Abuse Case, and Secure Design Review Playbook |
| Version | v1.0 |
| Status | Draft for Architecture Review Board / CAB / Security Governance / DevSecOps Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Security Architecture; Enterprise Architecture; DevSecOps Lead; Software Development Lead; QA/SDET; Platform Engineering; DBA; SRE; AI Governance; Internal Audit |
| Primary Audience | Architects, Developers, Security, DevSecOps, QA/SDET, Product Owners, System Builder operators, AI agent owners, SRE, DBA, CAB/ARB reviewers |
| Primary Parent Standards | 01A, 01, 01B, 02, 03, 11 v3.3, 11A v1.3, 20 v1.3, 65 v1.0, 66 v1.0 |
| Companion Standards | 10-10E MicroFunction family, 15/15A API, 16/16B Database, 17/17A Security, 31/31A Observability, 42 AI Governance, 43 Continuous Improvement, 62-68 executable governance standards |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Secure-Design-Review / 69 / v1.0 / |

Mandatory Practice Statement

No AIRA requirement, MicroFunction, API/event contract, Dynamic Workspace capability, database migration, AI/tool action, runtime configuration, or environment change is design-complete unless its threats, abuse cases, trust boundaries, controls, verification tests, evidence pack, owner, classification, and rollback or compensation path are defined and reviewed. Secure design review is a promotion gate, not a late advisory checklist.

# 1. Executive Summary

This playbook formalizes how AIRA performs threat modeling, abuse-case analysis, and secure design review before implementation and promotion. It converts secure-by-design intent into a governed, repeatable, evidence-producing process that aligns requirements, architecture, MicroFunctions, API/event contracts, data flows, AI model routes, agent tools, Dynamic Workspace actions, CI/CD gates, PRR/ORR, and continuous improvement.

AIRA must treat threat modeling as architecture evidence. The model identifies what is being built, what can go wrong, what controls are required, how those controls are verified, and whether the residual risk is acceptable. Any high-risk change that bypasses this playbook remains draft and cannot be promoted as AIRA-ready.

# 2. Purpose, Scope, and Authority
| Area | Required Treatment |
| --- | --- |
| Purpose | Define a standard method for threat modeling, abuse-case analysis, secure design review, control selection, verification planning, and evidence production across AIRA change types. |
| In Scope | MicroFunctions, Dynamic Workspace, APIs, events, database changes, file intake, AI/RAG/tool actions, agents, workflows, environment provisioning, runtime configuration, observability, and production-bound releases. |
| Out of Scope | Unreviewed production mutation, informal security comments with no evidence, AI self-approval, manual production DDL, direct provider calls, direct Git/CI/CD/Kubernetes/database credentials to agents, and frontend business authority. |
| Authority | This playbook is subordinate to AIRA architecture, AVCI, DevSecOps, security, data, AI governance, and change-management standards, but it is the operational secure-design gate for threat and abuse-case evidence. |
| Conflict Rule | When controls conflict, apply the stricter rule temporarily, log an AVCI reconciliation item, assign an owner, and route final decision through Security Governance, ARB, CAB, or Data Governance as applicable. |

# 3. Governing Principles
| Principle | Mandatory Meaning |
| --- | --- |
| Secure by design | Threats, abuse cases, and controls are defined before implementation or generation is trusted. |
| Evidence by construction | Secure design outputs become CI/CD, PR/MR, evidence manifest, test, scan, observability, and PRR/ORR inputs. |
| Fail closed | Missing identity, classification, policy, guardrail, audit, evidence, or verification blocks protected design approval. |
| Abuse-case first | High-risk flows must prove negative-path and misuse-path behavior, not only happy-path success. |
| AI is not authority | AI may draft threat hypotheses and candidate controls, but humans approve residual risk, merge, and promotion. |
| Reversibility | Every state-changing design must define rollback, forward-fix, compensation, safe-disable, replay control, or recovery. |

# 4. Threat Modeling Lifecycle
| Stage | Required Action | Evidence Output |
| --- | --- | --- |
| 1. Intake and classify | Record owner, source, bounded context, data classification, risk tier, environment, AI involvement, and expected business outcome. | Intake record, classification, owner, affected systems. |
| 2. Decompose system | Identify actors, assets, trust boundaries, data flows, entry points, APIs/events, policies, stores, workflows, model routes, and dependencies. | Context diagram, data-flow record, asset and boundary list. |
| 3. Identify threats | Use STRIDE-style categories, abuse cases, known attack techniques, prior incidents, GitNexus impact, and domain-specific misuse scenarios. | Threat register and abuse-case register. |
| 4. Rank and decide | Assess likelihood, impact, exposure, data sensitivity, exploitability, detectability, and reversibility. | Risk rating, control decision, residual risk owner. |
| 5. Design controls | Define preventive, detective, corrective, compensating, policy, observability, resilience, and rollback controls. | Secure design control plan. |
| 6. Verify controls | Map controls to unit, component, contract, OPA/SBAC, abuse-case, DAST, resilience, PRR/ORR, and monitoring tests. | Verification plan and gate mapping. |
| 7. Approve and retain | Obtain maker-checker and required Security/Architecture/CAB approval; retain evidence and improvement items. | Evidence manifest, approval record, backlog item. |

# 5. Threat Taxonomy for AIRA
| Threat Domain | AIRA Examples |
| --- | --- |
| Identity and access | Account takeover, privilege escalation, missing step-up, weak session, overbroad agent skill, tenant bypass. |
| Data and classification | PII leakage, Restricted prompt exposure, unsafe telemetry, unredacted screenshots, test data misuse, evidence overexposure. |
| API and eventing | Broken object-level authorization, unsafe errors, schema break, replay abuse, duplicate delivery, poisoning, DLQ misuse. |
| MicroFunction runtime | Missing idempotency, direct DB/Kafka/model call, bad compensation, stale runtime configuration, disabled audit, cache authority confusion. |
| Dynamic Workspace | Frontend business authority, unfiltered widget, unauthorized template exposure, unsafe drag/drop action, missing backend policy. |
| AI/RAG/tool action | Prompt injection, retrieval leakage, model-route bypass, tool overreach, hallucinated action, agent self-approval, missing guardrail. |
| DevSecOps and supply chain | Secret in repo, unpinned dependency, missing SBOM/provenance, scanner bypass, malicious package, weak runner, stale waiver. |
| Operations and resilience | Retry storm, lock contention, outbox backlog, DLQ replay error, partial commit, incident diagnostic data leakage, rollback failure. |

# 6. Abuse Case Analysis Standard

Abuse cases describe how a system can be misused or attacked. In AIRA, abuse cases are mandatory for high-risk flows and must be linked to controls, tests, evidence, and residual risk decisions.
| ID | Abuse Case Pattern | Required Control Response |
| --- | --- | --- |
| AC-01 | Unauthorized actor attempts protected action | OPA/SBAC deny-by-default, Keycloak/OIDC, audit, safe error, alert. |
| AC-02 | Authorized user exceeds role or skill boundary | Least privilege, step-up, SoD, policy decision evidence, checker approval. |
| AC-03 | Duplicate/replay request attempts duplicate business effect | Idempotency registry, request hash, replay guard, outbox/inbox dedupe, audit. |
| AC-04 | Event payload is malformed, stale, or incompatible | Schema validation, compatibility checks, DLQ, replay review, message repair control. |
| AC-05 | AI prompt attempts retrieval or tool abuse | Guardrails, classification, retrieval eligibility, tool allowlist, Harness/SBAC/OPA, human approval. |
| AC-06 | Debug mode leaks secrets or Restricted data | Redaction tests, forbidden-field scanner, runtime toggle policy, timebox, audit and auto-revert. |
| AC-07 | Compromised dependency or generated artifact enters pipeline | SCA, SBOM/provenance, signature/digest, dependency policy, release block. |
| AC-08 | Production incident requires replay or compensation | Approval workflow, replay runbook, synthetic validation, evidence manifest, post-action monitoring. |

# 7. Secure Design Review Gate Stack
| Gate | Pass Condition |
| --- | --- |
| Design Gate | System decomposition, trust boundaries, data flows, actors, APIs/events, runtime configs, dependencies, and assets are identified. |
| Security Gate | Identity, OPA/SBAC, classification, secrets hygiene, abuse cases, DAST scope, secure errors, and fail-closed behavior are defined. |
| Architecture Gate | SOLID, Clean Architecture, DDD, ports/adapters, MicroFunction rules, Dynamic Workspace backend authority, and direct-call prohibitions are satisfied. |
| Data Gate | Data classification, retention, redaction, test data, prompt/log/trace handling, evidence storage, and model route eligibility are controlled. |
| AI Gate | LiteLLM route, guardrails, retrieval controls, tool/action policy, trust tier, human approval, audit, rollback, and kill-switch are defined. |
| Operations Gate | Observability, alerting, SLO/SLA indicators, rollback/compensation, PRR/ORR, resilience tests, and post-promotion monitoring are specified. |

# 8. AIRA Change-Type Review Matrix
| Change Type | Secure Design Review Focus |
| --- | --- |
| MicroFunction / STP-BUS | Step isolation, standard concerns, policy, idempotency, outbox, audit, observability, compensation, no direct DB/Kafka/model calls. |
| API / Dynamic Workspace action | OpenAPI, backend authority, safe response, OPA/SBAC, BOLA/BFLA, rate limit, accessibility, telemetry, generated client. |
| Kafka/event/schema | AsyncAPI, CloudEvents, Avro/JSON schema, compatibility, outbox/inbox, idempotent consumer, DLQ, replay, retention. |
| Database / migration | Flyway-only, RLS/tenant isolation, indexes, data classification, rollback/forward-fix, DBA review, no manual DDL. |
| AI/RAG/tool action | Prompt injection, retrieval leakage, model route, guardrail, SBAC/OPA, tool boundary, human approval, prompt/output evidence. |
| Agent / System Builder | Agent owner, trust tier, skills, tool scope, no production credentials, evaluation, monitoring, suspension, retirement. |
| Environment / IaC | Manifest first, least privilege, secret paths, IaC/container scans, SBOM/provenance, rebuild/rollback, break-glass control. |
| Runtime toggle | Allowed diagnostic tuning only; never disables audit, security, policy, classification, idempotency, outbox, or critical evidence. |

# 9. Control Selection and Verification Mapping
| Control Type | Examples | Verification Evidence |
| --- | --- | --- |
| Preventive | OPA/SBAC deny, input validation, schema validation, secret management, rate limit, least privilege, guardrails. | Unit, policy, contract, abuse-case, secret scan. |
| Detective | Audit, structured logs, OTel traces/metrics, Sentry, Loki/Tempo/Grafana alerts, GitNexus drift, security scans. | Trace reconstruction, dashboard, alert, scan evidence. |
| Corrective | Rollback, compensation, DLQ/replay, safe-disable, incident runbook, message repair, forward-fix. | Resilience Lab, PRR/ORR, replay drill, rollback test. |
| Compensating | Time-bound waiver, manual checker, restricted rollout, extra monitoring, feature flag, reduced scope. | Waiver record, expiry, owner, evidence and closure plan. |
| Assurance | PR/MR AVCI summary, evidence manifest, tests, scans, SBOM/provenance, GitNexus, approvals. | CI/CD evidence pack and release-readiness record. |

# 10. Secure Design Review Evidence Pack
| Folder | Required Contents |
| --- | --- |
| 00-manifest | secure-design-review-manifest.json, classification-record.md, source-register.md |
| 01-model | system-context.md, data-flow.md, trust-boundaries.md, assets-and-entry-points.md |
| 02-threats | threat-register.csv, abuse-case-register.csv, risk-ranking.md, residual-risk.md |
| 03-controls | control-selection.md, OPA-policy-map.md, SBAC-skill-map.md, guardrail-map.md |
| 04-verification | test-plan.md, abuse-case-tests.md, DAST-scope.md, resilience-test-map.md, PRR-ORR-map.md |
| 05-evidence | GitNexus-impact.md, scan-summary.md, trace-audit-examples.md, evidence-manifest-link.md |
| 06-approvals | maker-checker.md, security-review.md, architecture-review.md, waiver-record.md, CAB-ARB-link.md |
| 07-improvement | open-findings.md, remediation-plan.md, Auto-Learn-candidates.md, backlog-links.md |

# 11. Secure Design Review Manifest Excerpt

{
  "secure_design_review_id": "SDR-<system>-<date>-<sequence>",
  "classification": "INTERNAL CONFIDENTIAL",
  "owner": "<accountable owner>",
  "change_type": ["microfunction", "api", "event", "ai_tool_action"],
  "bounded_context": "<context>",
  "threat_model": {
    "assets": [], "actors": [], "trust_boundaries": [], "data_flows": [],
    "threats": [{"id":"TH-001", "category":"spoofing", "risk":"high", "control_refs":[]}],
    "abuse_cases": [{"id":"AB-001", "misuse_path":"...", "test_ref":"..."}]
  },
  "verification": {
    "opa_sbac_tests": "required", "authenticated_dast": "risk_based",
    "resilience_lab": "required_for_mutating_or_event_flows", "prr_orr": "production_bound"
  },
  "avci": {"attributable": true, "verifiable": true, "classifiable": true, "improvable": true}
}

# 12. RACI and Separation of Duties
| Role | RACI | Responsibility |
| --- | --- | --- |
| Solutions Architecture Office / IT Head | A/R | Owns playbook, resolves architecture conflicts, approves material exceptions and review queue direction. |
| Security Architecture | A/R | Owns threat model method, abuse-case requirements, control selection, DAST scope, risk acceptance, waivers. |
| DevSecOps Lead | R | Integrates secure design evidence into CI/CD, evidence manifests, policy gates, and release controls. |
| Software Development Lead | R | Ensures designs, code, tests, MicroFunctions, and PR/MR evidence reflect approved controls. |
| QA/SDET | R | Owns negative tests, abuse-case tests, regression, DAST coordination, and verification evidence. |
| DBA / Data Governance | R/C | Reviews data flows, Flyway, RLS, retention, classification, migration risk, and data repair paths. |
| AI Governance | A/R | Reviews model route, guardrails, prompt/retrieval/tool risks, evaluation, agent trust tier, and AI evidence. |
| Internal Audit | C/I | Reviews evidence completeness, control traceability, waiver aging, and assurance readiness. |

# 13. Acceptance Criteria

Every high-risk or production-bound AIRA change has a threat model, abuse-case register, secure design review record, and evidence manifest link.

Every protected flow shows identity, classification, OPA/SBAC, validation, audit, observability, safe error, idempotency, and rollback or compensation controls where applicable.

API/event changes include OpenAPI/AsyncAPI/schema/CloudEvents compatibility, outbox/inbox, idempotent consumer, DLQ, and replay controls where applicable.

AI/RAG/tool-action changes include LiteLLM route, guardrails, retrieval eligibility, tool policy, trust tier, human approval, audit, and rollback/kill-switch controls.

Authenticated DAST, abuse-case tests, policy tests, architecture fitness, GitNexus impact, resilience tests, PRR/ORR, and evidence pack requirements are mapped before promotion.

Any accepted residual risk has owner, expiry, compensating control, waiver record, remediation plan, and CAB/ARB/security approval where required.

# 14. Anti-Patterns and Rejection Rules
| Anti-Pattern | Required Response |
| --- | --- |
| Threat model created after coding only for compliance | Reject. Threat model must inform controls and verification before promotion. |
| Happy-path-only design review | Reject. Abuse cases, negative paths, denial paths, error handling, rollback, and evidence are mandatory for risk flows. |
| AI-generated control accepted without verification | Reject. AI recommendations are draft until tests, scans, policy checks, and human review pass. |
| Direct DB/Kafka/model/provider call from business logic | Reject. Use ports/adapters, outbox, LiteLLM, guardrails, and MicroFunction envelope. |
| Runtime toggle disables audit/security/policy evidence | Reject. Diagnostic tuning cannot disable mandatory evidence or critical controls. |
| Waiver without owner, expiry, compensating control, and closure plan | Reject or escalate as non-conformance. |
| Replay or data repair without approval and evidence | Reject. Replay and repair must be bounded, authorized, auditable, and reversible where possible. |

# 15. Roadmap
| Phase | Execution Focus | Exit Evidence |
| --- | --- | --- |
| Phase 1 | Adopt this playbook as secure design gate for new MicroFunctions, APIs/events, Dynamic Workspace actions, AI/tool actions, and production-bound changes. | Secure design review template and evidence folder used in PR/MR. |
| Phase 2 | Convert threat/abuse-case requirements into CI evidence manifest fields, OPA/SBAC policy checks, PR/MR templates, and GitNexus prompts. | Pipeline validates secure design evidence references. |
| Phase 3 | Create reference threat models for login, event/outbox, AI advisory, Dynamic Workspace admin action, and Auto-Heal candidate loops. | Golden-path secure design examples available. |
| Phase 4 | Automate control traceability to Document 68 and quarterly assurance reporting. | Control objective coverage and waiver aging dashboards. |

# 16. Open Reconciliation Items
| ID | Issue | Severity | Owner |
| --- | --- | --- | --- |
| RI-069-001 | Map this playbook to 17/17A security standards when those files are next updated. | Medium | Security Architecture |
| RI-069-002 | Bind threat model fields to Document 66 evidence manifest schema and Document 68 traceability matrix. | High | DevSecOps Lead |
| RI-069-003 | Create reference abuse-case library for MicroFunction, Dynamic Workspace, API/event, AI/tool, and environment provisioning. | Medium | Security / QA |
| RI-069-004 | Resolve 41B/44 System Builder overlap for secure design review evidence ownership. | Medium | Architecture Board |
| RI-069-005 | Define formal risk-scoring thresholds for mandatory authenticated DAST, PRR/ORR, and Resilience Lab execution. | Medium | Security / SRE |

# 17. External Alignment Reference
| Reference | AIRA Use |
| --- | --- |
| OWASP Threat Modeling Cheat Sheet | Supports decomposition, threat identification/ranking, mitigations, review, and validation. |
| OWASP ASVS | Provides application and API security verification requirements that can be mapped to tests and evidence. |
| NIST SP 800-218 SSDF | Defines secure software development practices for reducing software vulnerability risk. |
| MITRE ATT&CK Enterprise | Provides adversary tactics, techniques, and mitigation references useful for abuse-case enrichment. |
| AIRA Documents 20, 65, 66, 67, 68 | Provide CI/CD gate, policy-as-code, evidence manifest, API/event/replay, and control traceability bindings. |

# 18. AVCI Compliance Summary
| AVCI Property | How This Playbook Satisfies It |
| --- | --- |
| Attributable | Threat models and secure design reviews identify owner, source, bounded context, classification, reviewer, approver, residual risk owner, and evidence path. |
| Verifiable | Each threat and abuse case maps to control, test, scan, policy decision, DAST scope, GitNexus output, trace/audit record, PRR/ORR or resilience evidence. |
| Classifiable | Data, prompts, logs, traces, screenshots, events, artifacts, model routes, evidence, and retention are classified and redacted according to policy. |
| Improvable | Threat findings, incidents, failed gates, waivers, vulnerabilities, abuse-case gaps, and runtime signals feed Auto-Learn/Auto-Improve backlog and standard updates. |

Final Rule

A secure design review that does not produce evidence, tests, policy decisions, traceability, residual-risk ownership, and improvement path is incomplete. It remains advisory and must not be treated as an approved AIRA control gate.

