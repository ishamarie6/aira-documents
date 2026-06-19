---
title: "Change Promotion Reversibility and Compensation Control Standard"
doc_id: "AIRA-30A"
version: "v1.2"
status: "revised"
category: "Release and change governance"
source_docx: "AIRA_30A_Change_Promotion_Reversibility_and_Compensation_Control_Standard_v1.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 30-release-change-governance
  - revised
  - aira-30a
---



# Change Promotion Reversibility and Compensation Control Standard



AIRA

AI-Native Enterprise Platform

Change, Promotion, Reversibility, and Compensation Control Standard

v1.2 Revised

Maker-Checker Governance - CAB/ARB Approval - System Builder Promotion Controls - Rollback - Compensation - Deactivation - Evidence
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-030A |
| Canonical Filename | AIRA_30A_Change_Promotion_Reversibility_and_Compensation_Control_Standard_v1.2_Revised.docx |
| Version | v1.2 - Revised change promotion, reversibility, compensation, deactivation, rollback, Dynamic Workspace, MicroFunction, API/eventing, database, AI governance, runtime toggle, incident, BCDR, and System Factory alignment update |
| Supersedes | 30A-AIRA_Change_Promotion_Reversibility_and_Compensation_Control_Standard_v1.1.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Architecture Review Board, CAB, DevSecOps, Security, SRE/Operations, Platform Engineering, DBA, QA/SDET, AI Governance, Data Governance, Business Owners, and Internal Audit Review |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; CAB Chair; DevSecOps Lead; Security Architecture; Software Development Lead; QA/SDET; DBA; SRE / Operations; Platform Engineering; AI Governance; Data Governance; Internal Audit |
| Primary Companion | 30 Release, Deployment, Change, and CAB Governance Standard v1.4; 20 CI/CD Evidence Pack v1.2; 45 PoC2 System Factory v1.2; 31/31A Operations and Observability v1.2; 24B Incident/Auto-Heal v1.2; 35 BCDR v1.2 |
| Revised Inputs Considered | 09 v3.2 Greenfield Environment; 19B v1.2 Sprint 0; 20 v1.2 CI/CD; 24B v1.2 Incident and Auto-Heal; 30 v1.4 Release/CAB; 31/31A v1.2 Operations/Observability; 35 v1.2 BCDR; 39A/39B/39C workstation and System Builder Lite; 45 v1.2 PoC2 System Factory |
| Governing AIRA Sources | 01/01A AVCI and Enterprise Design Principles; 02 Blueprint; 03 Developer Guide; 04 Technology Stack; 10 MicroFunction family; 12A and 41/46-61 Dynamic Workspace; 15/15A API; 16/16A/16B Database/Flyway; 17/17A Security; 19 GitNexus; 22A AI registry; 26A classification; 29 UAT; 32 SBAC; 34 Audit; 42 AI governance; 43 Continuous Improvement |
| External Alignment Reference | NIST SP 800-218 SSDF; OWASP ASVS 5.0.0; OpenTelemetry Semantic Conventions; SLSA v1.2 |
| Review Cadence | Quarterly; after material release, CAB, System Builder, AI agent, technology provisioning, security, evidence, model-route, Dynamic Workspace, MicroFunction, database, eventing, observability, BCDR, or production incident change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Change-Promotion-Reversibility-Compensation / v1.2 / |
| Mandatory Practice Statement No AIRA System Builder-generated requirement, evidence-derived remediation, improvement request, AI agent definition, environment provisioning plan, technology setup, configuration, code, policy, database migration, prompt, guardrail, model route, Dynamic Workspace artifact, MicroFunction runtime definition, API/event contract, operational runbook, or release candidate may be promoted unless the change is attributable, independently checked, classified, evidence-backed, reversible or compensable, observable, and approved through the required maker-checker, CAB/ARB, and policy path. |
| --- |

# 1. Executive Summary

This v1.2 revision updates AIRA-DOC-030A as the detailed control standard for how changes move from intake or evidence into approved promotion, rollback, compensation, deactivation, and learning. It preserves the v1.1 System Builder expansion baseline while aligning with the newly revised Greenfield Environment, workstation setup, Sprint 0, CI/CD, PoC 2 System Factory, observability, production operations, incident/Auto-Heal, BCDR, and release/CAB documents. The document is deliberately stricter than a deployment checklist: every change must prove that it can be reviewed, tested, secured, observed, reversed, compensated, or safely deactivated.
| v1.2 Outcome | Required Result |
| --- | --- |
| Promotion control strengthened | No generated artifact, configuration, prompt, model route, policy, migration, agent, template, or runtime parameter becomes active without owner, checker, evidence, classification, risk, approval, and rollback/compensation path. |
| Reversibility made explicit | Every change declares one or more paths: rollback, forward-fix, compensation, deactivation, quarantine, rebuild, replay, restore, or retirement. |
| Dynamic Workspace governed | Templates, components, widgets, AI panel configuration, and action bindings are frontend artifacts only; backend policy, APIs, MicroFunctions, and evidence govern authority. |
| MicroFunction-safe promotion | Runtime definitions, step catalog entries, and business MicroFunctions preserve standard envelope steps, idempotency, audit, observability, outbox, error handling, and compensation. |
| AI-native change guarded | System Builder and agents may analyze, draft, test, and propose. They do not approve, merge, deploy, bypass policy, rotate production secrets, or mutate production authority. |
| Incident learning controlled | Auto-Heal, Auto-Learn, and Auto-Improve create candidate actions and learning records only through evidence, tests, and human-approved promotion. |

# 2. Purpose, Scope, and Authority
| Category | In Scope | Out of Scope / Prohibited |
| --- | --- | --- |
| Change domains | Business, system, workflow, MicroFunction, UI, API, database, policy, integration, environment, AI agent, prompt, guardrail, model route, runtime parameter, operational remediation, and evidence-driven improvement changes. | Unregistered changes, side-channel fixes, undocumented manual production mutation, uncontrolled scripts, direct DB edits, direct model-provider calls, or changes without owner and evidence. |
| Promotion authority | Maker-checker, CODEOWNERS, CI/CD gates, OPA/SBAC, security review, DBA review, ARB/CAB where triggered, UAT/production readiness, deployment evidence. | Self-approval by the maker, AI approval of its own output, bypassing branch protection, bypassing policy or evidence, or using emergency access as a normal release path. |
| Reversibility | Rollback, forward-fix, compensation, deactivation, cache invalidation, schema forward migration, DLQ/replay, restore, rebuild, quarantine, feature disablement. | Irreversible change without explicit risk acceptance, business owner approval, BCDR evidence, and compensating controls. |
| Continuous improvement | Auto-Heal, Auto-Learn, Auto-Improve recommendations, candidate fixes, runbook updates, tests, policy hardening, observability tuning, backlog items. | Silent production self-healing that changes business state, access, schema, prompts, model routes, or runtime configuration without approved guardrails and evidence. |
| Authority Rule Document 30 governs release/CAB process. Document 30A governs the detailed safety mechanism required before any change can be promoted: independent checking, classification, evidence, rollback, compensation, deactivation, post-verification, and improvement capture. |
| --- |

# 3. Change Intake, Classification, and Routing
| Intake Type | Mandatory Intake Fields | Routing / Approval |
| --- | --- | --- |
| New requirement | intake_id, source_ref, owner, bounded_context, classification, affected contracts, acceptance criteria, risk tier, required evidence. | Product owner, architecture, security, QA/SDET, DevSecOps; ARB/CAB if architecture, production, data, or control impact exists. |
| Operational evidence | incident/error/trace/log/metric/test/scan/screenshot/file evidence, affected service, severity, correlation_id, evidence_ref, hypothesis. | SRE/Operations, DevSecOps, Security, application owner; incident or problem record drives change proposal. |
| Improvement request | measurable problem, evidence, proposed improvement, expected benefit, risk, test plan, rollback/compensation path. | Architecture and owner review; security/DBA/AI governance if related controls are affected. |
| AI agent lifecycle | agent_id, owner, purpose, tool scope, SBAC skills, OPA policies, model route, guardrail tests, trust tier, kill switch. | AI Governance, Security, DevSecOps, Architecture; activation only through registry and certification evidence. |
| Environment provisioning | target env, IaC/GitOps plan, approved sources, images, secrets paths, policy checks, drift detection, restore/rebuild plan. | Platform, DevSecOps, Security, DBA/SRE; CAB/ARB for staging/production or shared platform changes. |
| Runtime parameter/toggle | parameter key, allowed values, default-safe value, owner, performance rationale, observability impact, audit, rollback value. | Owner plus SRE/Security/Architecture depending on scope; all production-impacting toggles are auditable changes. |

# 4. Maker-Checker, Separation of Duties, and Approval Gates
| Gate | Required Control | Reject / Escalate When |
| --- | --- | --- |
| Maker declaration | Author declares intent, AI involvement, files/config/contracts affected, classification, risk, tests, and reversibility path. | No ticket/owner, hidden AI use, vague impact, or missing classification. |
| Independent checker | Reviewer is not the maker; validates architecture, security, tests, evidence, rollback/compensation, and user/business impact. | Maker self-approves, reviewer lacks required domain skill, or evidence is incomplete. |
| Specialist review | Security, DBA, API, DevSecOps, QA/SDET, SRE, AI Governance, Data Governance, or UX/a11y review based on affected domain. | Privilege expansion, schema impact, breaking contract, Restricted data, model route, or critical workflow lacks specialist sign-off. |
| Policy decision | OPA/SBAC/ABAC/RBAC/admission controls validate who may request, approve, activate, deploy, replay, restore, or revoke. | Policy unavailable, deny result, stale policy, missing skill, SoD conflict, or unclassified evidence. |
| CAB/ARB routing | CAB approves production-impacting operational risk; ARB approves architecture/control impacts. Both require evidence. | Change bypasses CAB/ARB trigger, weakens a control, or lacks rollback/compensation proof. |
| Post-promotion verification | Runtime traces, audit events, dashboards, SLOs, error monitoring, and evidence closure prove the change behaved as approved. | No monitoring window, missing trace/evidence, unresolved critical alerts, or rollout deviates from approved plan. |

# 5. Evidence Pack and Promotion Readiness
| Evidence Domain | Minimum Required Evidence |
| --- | --- |
| Attributable | Ticket/intake ID, owner, maker, checker, approver, bounded context, classification, branch/commit/version, source prompt/evidence, release/change ID. |
| Verifiable | CI run, unit/component/contract/E2E/security/architecture/OPA/AI evaluation evidence, GitNexus impact, scan reports, SBOM/provenance, deployment/runbook proof. |
| Classifiable | Data classification, evidence classification, model-route eligibility, log/cache/event restrictions, retention/disposal, Restricted data handling, redaction status. |
| Improvable | Known limitations, residual risks, waiver expiry, post-promotion monitoring, incident/problem links, backlog item, runbook/knowledge update, metric owner. |
| Design principles | SOLID, Clean Architecture, DDD, ports/adapters, idempotency, determinism, fail-closed behavior, security, observability, rollback/compensation impact. |
| Reversibility | Rollback, forward-fix, compensation, deactivation, replay, restore, rebuild, quarantine, kill switch, or retirement plan with owner and evidence. |
| ## AIRA 30A Change Promotion Evidence Block - Change ID / Intake ID / Ticket / ADR / TDL: - Owner / Maker / Checker / Approver: - Classification / Risk tier / Bounded context: - Affected artifacts: code \| config \| MicroFunction \| UI \| API \| event \| DB \| policy \| agent \| model route \| prompt \| environment - Tests and scans: unit \| component \| contract \| E2E \| OPA \| SAST \| SCA \| secrets \| DAST \| a11y \| resilience \| AI eval - GitNexus / impact / affected tests: - Evidence pack path and retention: - Rollback / forward-fix / compensation / deactivation / restore: - Post-promotion monitoring and acceptance window: - Known limitations / residual risks / waiver expiry: |
| --- |

# 6. Reversibility and Compensation Pattern Catalog
| Change Class | Required Reversibility / Compensation Pattern | Evidence Required |
| --- | --- | --- |
| Application code | Rollback artifact, feature flag, canary/blue-green strategy, forward-fix branch, smoke test, monitoring window. | Artifact digest, deployment log, smoke test, Sentry/error evidence, trace sample, rollback test. |
| Dynamic Workspace | Previous template/component/action binding, safe fallback, cache invalidation, visual/a11y smoke test. | Template version diff, approval workflow, policy decision, visual/a11y report, rollback activation record. |
| MicroFunction runtime | Previous transaction definition, step deactivation, idempotency guard, compensation function, outbox/audit reconciliation. | Config diff, validator result, step tests, audit/outbox proof, compensation result. |
| API / OpenAPI | Backward-compatible versioning, generated clients, dual-run/deprecation, consumer migration, safe error response. | Contract diff, consumer tests, generated client build, gateway policy evidence. |
| Event / AsyncAPI / Kafka / Avro | Schema compatibility, replay plan, idempotent consumers, DLQ routing, causation/correlation preservation. | Schema registry result, replay test, DLQ test, consumer idempotency evidence, lag/reconciliation report. |
| Database / Flyway | Expand/contract, forward-only migration, PITR/backup interface where needed, RLS validation, data reconciliation. | Flyway validate/migrate, checksum, rollback/forward-fix plan, restore rehearsal, DBA sign-off. |
| Policy / OPA / SBAC | Versioned policy, deny-by-default fallback, skill/grant expiry, negative tests, approval route. | OPA tests, decision logs, SBAC catalog diff, SoD check, rollback policy version. |
| AI prompt / guardrail / model route | Revert route/prompt/guardrail, quarantine unsafe outputs, rerun evaluation suite, disable affected feature. | Model route audit, guardrail result, eval report, prompt version diff, approval record. |
| AI agent | Suspend/revoke/decommission, disable tool scope, kill switch, revoke credential lease, registry update. | Agent registry record, tool action logs, OPA decision, certification/demotion evidence, incident chain. |
| Environment / platform | GitOps rollback, Helm rollback, IaC rebuild, drift remediation, secret rotation, backup/restore validation. | Argo/Helm/IaC evidence, image digest, policy result, drift report, restore test. |

# 7. Dynamic Workspace, MicroFunction, API/Event, and Database Promotion Controls
| Domain | Non-Negotiable Promotion Control |
| --- | --- |
| Dynamic Workspace | Frontend never becomes business authority. Template, component, widget, AI panel, and action binding changes require registry validation, OPA/SBAC filtering, generated client compatibility, a11y/visual tests, safe fallback, audit, and previous active version. |
| MicroFunction | Runtime assembly must include identity, correlation, classification, authorization, validation, idempotency, transaction, audit, outbox, observability, safe error, retry/DLQ/compensation, and evidence steps unless formally waived. |
| OpenAPI / AsyncAPI | Contract-first change; compatibility, schema evolution, error semantics, authorization scope, idempotency key, correlation/causation ID, generated client, and consumer impact checks are mandatory. |
| Kafka / Avro / CloudEvents | Topic ownership, schema registry, Avro compatibility, event type/version, outbox/inbox, idempotent consumer, DLQ/retry/replay, retention, PII classification, and trace propagation are validated. |
| Database / Flyway | Flyway only. No manual production DDL or data-fix bypass. Migration rehearsal, RLS tests, backup/PITR impact, performance/index plan, and reconciliation evidence are required. |
| Runtime toggles | Logging/tracing/sampling/feature/diagnostic toggles are runtime-configurable only through approved parameters with safe defaults, allowed values, audit, rollback value, owner, and monitoring. |

# 8. Security, AI Governance, and Abuse-Case Controls
| Control | Required Treatment |
| --- | --- |
| Secrets hygiene | No secrets, tokens, raw JWTs, credentials, private keys, or Restricted data in code, prompts, screenshots, logs, tests, evidence, Obsidian, LLM Wiki, or GitNexus summaries. Use approved secret references only. |
| Authenticated DAST | DAST uses synthetic users, non-production scope, rate limits, allowlisted targets, safe windows, evidence retention, finding ownership, and remediation proof. |
| OPA / SBAC expansion | Any skill, role, data scope, tool permission, or approval-path expansion is treated as a high-risk change and requires policy tests, negative tests, SoD review, and expiry/recertification where appropriate. |
| AI agent and tool action | Agent actions go through registry, SBAC, OPA, Harness/tool gateway, guardrails, dry-run where feasible, human approval by risk tier, audit, and rollback/compensation path. |
| Prompt / guardrail / model route | Changes are versioned, evaluated against golden/adversarial datasets, classification-gated, rollbackable, and tied to model route audit. Direct provider SDK calls are prohibited. |
| Abuse cases | Privilege escalation, prompt injection, tool misuse, model-route bypass, evidence tampering, policy weakening, secrets leakage, replay abuse, data exfiltration, and silent mutation are tested or explicitly risk-accepted. |
| Fail-closed behavior | If identity, policy, guardrail, model gateway, evidence, audit, registry, or approval system is unavailable, protected actions stop or escalate rather than proceed silently. |

# 9. Auto-Heal, Auto-Learn, and Auto-Improve Control Loop
| Loop | Allowed Output | Promotion Gate |
| --- | --- | --- |
| Auto-Heal | Incident analysis, containment recommendation, rollback/deactivation proposal, remediation branch, tests, runbook update, monitoring recommendation. | Human-approved change/incident path; bounded pre-approved action only if low-risk, reversible, audited, and policy-authorized. |
| Auto-Learn | Lesson learned, knowledge correction candidate, retrieval update candidate, prompt/guardrail test improvement, metric trend, training note. | Knowledge governance review, classification check, source citation, conflict check, human approval before canonical or retrieval eligibility. |
| Auto-Improve | Refactoring proposal, policy hardening, contract/schema improvement, test gap fix, observability tuning, resilience improvement, UX/a11y correction. | Ticket/ADR/TDL/PR, CI/CD gates, GitNexus impact, tests/scans, maker-checker, CAB/ARB if triggered, rollback/compensation proof. |
| Silent Mutation Rejection Rule Issue detection, evidence retrieval, candidate fix or learning proposal, tests, and human approval are mandatory. Auto-Heal, Auto-Learn, and Auto-Improve may accelerate the change lifecycle but must never silently mutate production systems, policies, prompts, guardrails, model routes, MicroFunction catalogs, databases, or runtime configuration. |
| --- |

# 10. Waivers, Emergency Changes, and Break-Glass
| Scenario | Minimum Governance Treatment |
| --- | --- |
| Standard waiver | Specific control, reason, risk owner, residual risk, compensating controls, expiry, remediation plan, evidence pack, approvers, and closure criteria are mandatory. |
| Emergency change | Incident-linked, time-bound, least-privilege, logged, monitored, rollback-ready, and retrospectively reviewed by CAB with RCA/PIR and improvement backlog. |
| Break-glass access | Named user, business/security approval where feasible, elevated session recording/logging, restricted duration, post-action reconciliation, credential rotation if applicable. |
| Irreversible change | Requires ARB/CAB, business owner risk acceptance, BCDR impact, data protection review, legal/compliance review where applicable, and explicit compensation path. |
| Control degradation | Any proposal that disables tests, weakens OPA/SBAC, hides errors, removes observability, skips evidence, broadens secrets access, or bypasses review is rejected or escalated as non-conformance. |
| waiver_id: AIRA-WAIVER-YYYY-NNN requested_by: <name> risk_owner: <name> control_or_gate: <specific control> reason: <why waiver is requested> risk_rating: LOW \| MEDIUM \| HIGH \| CRITICAL compensating_controls: [] expiry: <date or release> remediation_plan: <owner / due date / evidence> required_approvers: [architecture, security, devsecops, data, dba, sre, cab_if_required] evidence_pack_ref: <path> status: PROPOSED \| APPROVED \| EXPIRED \| CLOSED \| REJECTED |
| --- |

# 11. RACI and Operating Responsibilities
| Role | Accountable Responsibilities |
| --- | --- |
| Solutions Architecture Office / IT Head | Owns 30A interpretation, unresolved architecture/control escalation, final recommendation for material exceptions, and source-register alignment. |
| CAB Chair / Change Manager | Owns change workflow, CAB agenda, approval records, emergency ratification, waiver tracking, and post-change review completeness. |
| DevSecOps Lead | Owns CI/CD gates, evidence pack generation, GitOps promotion, SBOM/provenance, signed artifacts, and pipeline enforcement. |
| Security Architecture / InfoSec | Owns security review, OPA/SBAC, secrets hygiene, DAST, abuse-case checks, fail-closed validation, and remediation evidence. |
| Software Development Lead | Owns code/config quality, architecture boundary adherence, PR evidence, rollback/forward-fix strategy, and developer accountability. |
| DBA / Data Governance | Owns Flyway migration governance, RLS/data controls, backup/restore implications, data reconciliation, and retention/classification evidence. |
| SRE / Operations | Owns runbooks, monitoring, deployment support, incident interface, rollback execution support, SLO impact, and hypercare evidence. |
| QA/SDET | Owns test strategy, deterministic regression, contract, E2E, a11y/visual, resilience, and release-quality evidence. |
| AI Governance | Owns prompt/guardrail/model route/agent lifecycle change review, evaluation evidence, trust-tier implications, and registry controls. |
| Internal Audit | Reviews evidence completeness, control operation, waiver trail, SoD, and continuous assurance sampling. |

# 12. Acceptance Criteria and Definition of Done

Every change has intake ID, owner, source, classification, bounded context, risk tier, impact analysis, and approval route.

Promotion evidence includes CI/CD, tests, scans, policy checks, GitNexus impact, architecture fitness, SBOM/provenance where applicable, and human checker evidence.

Dynamic Workspace, MicroFunction, OpenAPI/AsyncAPI, Kafka/Avro/CloudEvents, Flyway, policy, AI, runtime-toggle, and environment changes use their specialist gates before activation.

Rollback, forward-fix, compensation, deactivation, quarantine, replay, restore, rebuild, or retirement path is documented and feasible.

Post-promotion monitoring confirms traces, logs, metrics, audit, Sentry/errors, dashboards, and evidence records are complete and classification-safe.

Waivers are time-bound, risk-owned, evidence-backed, approved by appropriate authorities, and tracked to closure.

Auto-Heal, Auto-Learn, and Auto-Improve outputs remain proposal-driven until promoted through maker-checker, tests, evidence, and CAB/ARB when triggered.

# 13. AVCI Compliance Summary
| AVCI Property | Compliance Evidence |
| --- | --- |
| Attributable | Every intake, change, generated artifact, approval, rollback, compensation, deactivation, waiver, learning record, and promotion has owner, source, version, reviewer, approver, timestamp, and evidence path. |
| Verifiable | Promotion requires tests, scans, policy checks, architecture fitness, GitNexus impact, guardrail/model-route evidence, deployment proof, rollback/compensation/deactivation proof, and post-verification. |
| Classifiable | All intakes, outputs, evidence, runtime records, logs, prompts, AI artifacts, and knowledge updates carry classification and handling rules that govern access, model route, storage, retention, and retrieval eligibility. |
| Improvable | Rejected changes, incidents, failed gates, waivers, rollback events, compensation outcomes, audit findings, SLO trends, and user feedback become governed backlog, runbook, prompt, guardrail, knowledge, policy, and control improvements. |
| Final Control Statement AIRA moves quickly only when it can prove control. A change is promotion-ready only when it is independently checked, policy-authorized, test-proven, evidence-backed, classifiable, observable, reversible or compensable, and improvable under AVCI. |
| --- |

