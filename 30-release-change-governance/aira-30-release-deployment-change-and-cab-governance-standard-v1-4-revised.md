---
title: "Release Deployment Change and CAB Governance Standard"
doc_id: "AIRA-30"
version: "v1.4"
status: "revised"
category: "Release and change governance"
source_docx: "AIRA_30_Release_Deployment_Change_and_CAB_Governance_Standard_v1.4_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 30-release-change-governance
  - revised
  - aira-30
---



# Release Deployment Change and CAB Governance Standard



AIRA

AI-Native Enterprise Platform

Release, Deployment, Change, and CAB Governance Standard

v1.4 Revised

Release Governance - GitOps Promotion - CAB Discipline - Evidence Pack - Rollback/Compensation - Dynamic Workspace - MicroFunction Runtime - AI-Native Change Control
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-030 |
| Canonical Filename | AIRA_30_Release_Deployment_Change_and_CAB_Governance_Standard_v1.4_Revised.docx |
| Version | v1.4 - Revised release, deployment, CAB, promotion, rollback, Dynamic Workspace, MicroFunction, API/eventing, observability, security, AI governance, runtime toggle, BCDR, and System Factory alignment update |
| Supersedes | 30-AIRA_Release_Deployment_Change_and_CAB_Governance_Standard_v1.3.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Architecture Review Board, CAB, DevSecOps, Security, SRE/Operations, Platform Engineering, DBA, QA/SDET, AI Governance, Data Governance, Business Owners, and Internal Audit Review |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; CAB Chair; DevSecOps Lead; SRE / Operations Lead; Security Architecture; Software Development Lead; QA/SDET; DBA; Platform Engineering; AI Governance; Data Governance; Internal Audit |
| Primary Companion | 30A Change, Promotion, Reversibility, and Compensation Control Standard v1.1; 20 CI/CD Pipeline and Evidence Pack Guide v1.2; 45 PoC2 System Factory v1.2; 31/31A Operations and Observability v1.2; 24B Incident/Auto-Heal v1.2; 35 BCDR v1.2 |
| Revised Inputs Considered | 09 v3.2 Greenfield Environment; 19B v1.2 Sprint 0; 20 v1.2 CI/CD; 24B v1.2 Incident and Auto-Heal; 31/31A v1.2 Operations/Observability; 35 v1.2 BCDR; 39A/39B/39C workstation and System Builder Lite; 45 v1.2 PoC2 System Factory |
| Governing AIRA Sources | 01/01A AVCI and EDP; 02 Blueprint; 03 Developer Guide; 04 Technology Stack; 10 MicroFunction family; 12A and 41/46-61 Dynamic Workspace; 15/15A API; 16/16A/16B Database/Flyway; 17/17A Security; 19 GitNexus; 22A AI registry; 26A classification; 29 UAT; 32 SBAC; 34 Audit; 42 AI governance; 43 Continuous Improvement |
| External Alignment Reference | NIST SP 800-218 SSDF; OWASP ASVS 5.0.0; OpenTelemetry Semantic Conventions; SLSA v1.2 |
| Review Cadence | Quarterly; after material CI/CD, release, CAB, security, AI, model-route, Dynamic Workspace, MicroFunction, data, eventing, observability, BCDR, or production incident change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Release-Change-CAB / v1.4 / |
| Mandatory Practice Statement No AIRA release, deployment, configuration activation, database migration, policy change, model-route change, prompt/guardrail update, AI agent activation, Dynamic Workspace template activation, MicroFunction runtime change, event/schema change, operational remediation, or production-impacting action may proceed unless it is classified, owner-approved, evidence-backed, security-reviewed, test-proven, CAB/ARB-routed where required, reversible or compensable, observable, and traceable under AVCI. |
| --- |

# 1. Executive Summary

This v1.4 revision updates AIRA release, deployment, change, and CAB governance so it becomes the controlling promotion standard for the newly revised greenfield, workstation, Sprint 0, CI/CD, PoC 2, observability, operations, incident, Auto-Heal, and BCDR documents. It preserves the existing Release Governance, GitOps Promotion, CAB Discipline, Rollback Readiness, and Evidence-by-Construction baseline while making the promotion path explicit for Dynamic Workspace, MicroFunction runtime assembly, OpenAPI/AsyncAPI, Kafka/Avro/CloudEvents, Flyway, outbox/inbox, DLQ/replay, OPA/SBAC, AI governance, runtime telemetry toggles, and controlled improvement loops.
| v1.4 Outcome | Required Result |
| --- | --- |
| Governed promotion path | All changes move through intake, impact analysis, PR/MR, CI/CD, evidence pack, maker-checker, CAB/ARB where triggered, GitOps/Flyway/registry activation, post-release verification, and hypercare. |
| No silent mutation | System Builder, AI agents, Auto-Heal, Auto-Learn, Auto-Improve, GitNexus, and developer tools may propose, draft, analyze, validate, and prepare evidence, but must not approve or mutate production autonomously. |
| Release-ready by evidence | Release readiness requires tests, scans, policy decisions, contract compatibility, architecture fitness, observability, rollback/compensation, BCDR impact, and named accountability. |
| Dynamic and runtime-safe | Runtime configuration, telemetry toggles, workspace templates, MicroFunction definitions, model routes, and policy bundles can be activated only through registry-backed, audit-ready, reversible change paths. |
| Continuous improvement | Failed gates, rollback events, incidents, DAST findings, performance regressions, DLQ/replay anomalies, and user feedback become controlled backlog or Auto-Learn candidates. |

# 2. Purpose, Scope, and Authority
| Area | In Scope | Out of Scope / Rejected |
| --- | --- | --- |
| Release and deployment | Application, platform, configuration, Dynamic Workspace, MicroFunction, API/event, database, workflow, AI, observability, and security releases. | Unapproved production changes, direct manual mutation, agent self-approval, bypassed gates, and undocumented hot fixes. |
| Change governance | Standard, normal, major, emergency, break-glass, runtime-toggle, database, policy, AI, and evidence-derived remediation changes. | Informal chat approval, undocumented exceptions, permanent waivers, or unclassified change records. |
| CAB and ARB | Risk-based approval, maker-checker, separation of duties, CAB agenda, ARB triggers, residual-risk acceptance, and evidence review. | CAB rubber-stamping without evidence, architecture bypass, or reviewer conflict of interest. |
| Promotion and rollback | GitOps, CI/CD, Flyway, feature flags, registry activation, deactivation, rollback, forward-fix, compensation, and hypercare. | Promotion without tested rollback/compensation or unverified runtime monitoring. |
| AI-native controls | System Builder, agents, prompt/guardrail/model routes, LiteLLM, NeMo Guardrails, SBAC/OPA, Harness action records, and AI evidence. | Direct model-provider calls, unregistered agents, direct credentials in agents, or AI deciding production approval. |
| Authority Rule When this standard conflicts with a lower-level implementation guide, this standard and 30A govern promotion, CAB routing, rollback, compensation, and release-readiness interpretation. If conflict exists with a canonical AIRA register, record it as an AVCI reconciliation item and route it through 00D / revision control. |
| --- |

# 3. v1.4 Alignment Summary
| Companion Revision | Release Governance Impact |
| --- | --- |
| 09 v3.2 Greenfield Environment | Environment is not ready unless repository, CI/CD, policy, observability, Dynamic Workspace, MicroFunction, security, resilience, and evidence paths can support controlled release. |
| 39A/39B/39C Setup Guides | Developer, Codex, workstation, and team setup must not create uncontrolled release authority; agents remain sandboxed until governed certification and approval. |
| 19B Sprint 0 | Sprint 0 exit becomes a release-readiness gate for repository, pipeline, evidence, observability, policy, and rollback foundations. |
| 20 v1.2 CI/CD Evidence Pack | The release decision consumes pipeline evidence, not manual claims. Missing critical evidence blocks promotion unless waived with expiry and owner. |
| 45 v1.2 PoC2 System Factory | PoC 2 proves the reusable engineering factory for all future release candidates. |
| 31/31A v1.2 Operations/Observability | Release gates require dashboards, logs, traces, metrics, audit events, SLO impact, and trace reconstruction readiness. |
| 24B v1.2 Incident/Auto-Heal | Emergency change and Auto-Heal remain proposal-driven unless specifically pre-approved, reversible, observable, and time-bound. |
| 35 v1.2 BCDR | Release readiness includes backup, restore, DR, RTO/RPO, data reconciliation, failover/failback, and rollback evidence where impacted. |

# 4. Change Classification and Routing
| Change Class | Examples | Approval Route | Minimum Evidence |
| --- | --- | --- | --- |
| Low-risk standard change | Documentation projection, non-prod config, approved dependency patch, non-prod index refresh, internal dashboard tweak. | Pre-approved standard change catalog plus owner/checker; CAB visibility as defined. | Ticket, classification, test/smoke evidence, rollback/deactivation path, audit log. |
| Normal change | Code release, API contract update, Dynamic Workspace component, MicroFunction config, policy update, observability config, minor database migration. | PR/MR, CODEOWNERS, CI/CD, Security/QA/DevSecOps as applicable, CAB approval if production impacting. | Evidence pack, tests/scans, contract/Flyway/policy evidence, GitNexus impact, rollback/forward-fix. |
| Major / architecture change | New bounded context, data model change, event topology, critical workflow, System Builder capability, new agent/tool, platform shift. | ARB plus CAB, business owner, security, DBA, SRE, internal audit where required. | ADR/TDL, risk assessment, compatibility plan, BCDR impact, load/resilience evidence, rollback/compensation. |
| Emergency / break-glass | Security containment, critical outage recovery, data corruption containment, certificate/key emergency, production-impacting Sev-1 fix. | Incident commander, Security, SRE/Ops, CAB emergency approver; retrospective CAB review mandatory. | Incident ID, reason, time-box, actions, approvals, audit, post-verification, RCA, permanent fix backlog. |
| Runtime-toggle change | Telemetry sampling, feature flag, AI route enable/disable, workspace template activation, MicroFunction activation, cache invalidation. | Registry-backed maker-checker; CAB if production/risk tier requires; emergency path if outage/security. | Old/new values, reason, policy decision, audit event, monitoring window, rollback value, owner. |
| Restricted / high-risk change | Identity, secrets, OPA/SBAC, model route for sensitive data, production DB repair, privileged account, legal/financial/customer-impacting action. | Security + CAB/ARB + accountable owner; separation of duties mandatory. | Threat review, access review, tests, audit, evidence pack, rollback/compensation, residual-risk sign-off. |

# 5. End-to-End Promotion Workflow
| Intake / Ticket / Evidence Trigger -> Classification + Owner + Bounded Context + Risk Tier -> Impact Analysis: Architecture + Security + Data + API/Event + Dynamic Workspace + MicroFunction + AI + BCDR -> ADR / TDL / Waiver if triggered -> Candidate Branch / Pull Request / Change Package -> CI/CD: build + tests + contracts + Flyway + security + policy + fitness + GitNexus + evidence pack -> Maker-Checker / CODEOWNERS / QA / Security / DBA / SRE Review -> CAB / ARB / Business Approval as required -> Promotion: GitOps / Flyway / Registry Activation / Feature Flag / Model Route / Workspace Template -> Post-Promotion Verification: smoke + telemetry + audit + SLO + error monitor + rollback readiness -> Hypercare / PIR / Improvement Backlog / Auto-Learn Candidate |
| --- |
| Gate | Release Control | Blocking Condition |
| --- | --- | --- |
| G1 Intake completeness | Owner, source, ticket, classification, affected domains, acceptance criteria, and target environment defined. | Unknown owner, missing classification, missing ticket, or unclear business intent. |
| G2 Impact analysis | GitNexus, architecture, dependency, data, security, BCDR, Dynamic Workspace, MicroFunction, API/event, AI, and operational impact checked. | High/critical impact without ADR/TDL, risk owner, reviewer, or mitigation. |
| G3 Evidence pack | CI/CD evidence includes tests, SAST/SCA/secrets, DAST where applicable, SBOM/provenance, OPA, contracts, Flyway, observability, rollback. | Critical security, policy, architecture, test, scan, contract, or evidence failure without approved waiver. |
| G4 Approval | Maker-checker, CODEOWNERS, QA/Security/DBA/SRE, CAB/ARB, business owner approvals are complete where triggered. | Maker approves own work, AI self-approves, missing SoD, or CAB bypass. |
| G5 Promotion | Promotion uses approved GitOps/Flyway/registry path; no manual production DDL or direct mutation. | Manual mutation, direct credentials in agent/tool, or unrecorded runtime change. |
| G6 Post-release verification | Smoke test, traces, logs, metrics, audit, Sentry, dashboards, DLQ, error budget, user-safe outcomes verified. | No traceable verification, SLO breach ignored, or rollback path untested/unavailable. |

# 6. Release Evidence Pack Requirements
| Evidence Family | Required Artifacts |
| --- | --- |
| Attribution and source | Ticket, owner, branch, commit, PR/MR, reviewer/checker, CAB/ARB decision, AI-use declaration, prompt/agent/tool usage where applicable. |
| Build and supply chain | Build logs, toolchain versions, Java/runtime baseline, container image digest, SBOM, provenance/attestation, SCA, container/IaC scan, dependency disposition. |
| Tests and quality | Unit/component/integration/contract/E2E tests, Playwright/visual/a11y for UI, mutation/changed-line where applicable, performance/load/resilience evidence. |
| Security and policy | SAST, authenticated DAST where applicable, secret scan, OPA/Rego/Conftest, RBAC/ABAC/SBAC tests, abuse-case checks, remediation evidence, waiver status. |
| Architecture and GitNexus | Code map, dependency/impact analysis, affected tests, architecture fitness results, boundary/drift findings, reviewer disposition. |
| API/event/database | OpenAPI/AsyncAPI diff, schema compatibility, Kafka/Avro/CloudEvents checks, idempotent consumer tests, outbox/inbox/DLQ/replay evidence, Flyway validate/info. |
| Observability and operations | Log4j2 structure, OpenTelemetry traces, Sentry release/error signal, Loki/Tempo/Grafana dashboards, alert test, runbook, SLO impact, post-release watch. |
| Rollback/compensation | Feature flag, config version, previous artifact, database expand/contract or forward-fix, workflow compensation, AI route rollback, template deactivation, recovery plan. |
| AVCI and improvement | Attributable/verifiable/classifiable/improvable summary, known limitations, residual risks, hypercare plan, improvement backlog, Auto-Learn candidate if applicable. |

# 7. Dynamic Workspace and MicroFunction Release Rules
| Artifact Type | Promotion Rule | Rollback / Safe Disable |
| --- | --- | --- |
| Dynamic Workspace template | Must be backend-governed, policy-filtered, schema-validated, accessibility checked, visual tested, and approved through maker-checker before activation. | Deactivate template, restore previous active version, invalidate cache, show safe fallback, preserve audit evidence. |
| Component / widget | Must bind to approved OpenAPI/action contract; frontend cannot own business authority; component telemetry must be safe and classifiable. | Rollback component release, disable action binding, restore previous generated client, run smoke test. |
| AI Assistant Panel config | Prompt, guardrail, model route, retrieval eligibility, output schema, and classification route must be approved and tested. | Disable panel/config, revert prompt/route/guardrail, quarantine unsafe artifacts, notify AI Governance. |
| MicroFunction runtime definition | Configured transaction must preserve standard steps: identity, correlation, authorization, validation, idempotency, audit, outbox, observability, error handling, rollback. | Deactivate version, restore prior config, compensate partial execution, invalidate caches, verify audit/outbox state. |
| Runtime parameter / toggle | Toggle must have owner, allowed values, default-safe setting, audit trail, rollback value, monitoring window, and performance rationale. | Restore previous value, trigger alert review, update runbook if recurring. |
| Frontend Authority Rule Dynamic Workspace and frontend changes are presentation and interaction changes only. They do not authorize data access, bypass OPA/SBAC, mutate business state directly, call models directly, or activate templates without backend policy and release evidence. |
| --- |

# 8. API, Eventing, Database, and Workflow Release Controls
| Change Area | Mandatory Release Checks | CAB / ARB Trigger |
| --- | --- | --- |
| OpenAPI / REST | Contract-first change, generated client validation, backward compatibility, error semantics, idempotency keys, auth scopes, rate limits, safe response model. | Breaking change, external consumer impact, Restricted data, new high-risk action, production gateway policy change. |
| AsyncAPI / Kafka / CloudEvents | Topic/schema contract, Avro compatibility, partition/key strategy, consumer lag impact, replay plan, DLQ handling, outbox/inbox alignment. | New event domain, incompatible schema, retention/PII impact, cross-context event ownership change. |
| Database / Flyway | Flyway migration only, no manual production DDL, migration rehearsal, expand/contract strategy, RLS/security, backup/restore/forward-fix plan. | Destructive change, data migration, customer impact, RLS/access-control change, performance/index risk. |
| Workflow / Temporal / Flowable | Versioned workflow, in-flight instance handling, compensation, approval task behavior, SLA timers, audit, rollback/deactivation path. | Approval authority change, compensation logic change, critical business process change. |
| Outbox / Inbox / DLQ / Replay | Idempotency registry, duplicate-safe consumers, retry policy, replay authorization, correlation/causation IDs, reconciliation report. | Bulk replay, cross-system resync, data correction, operational incident recovery. |
| Cache / Redis / Valkey | Cache is acceleration only; invalidation, warmup, TTL, fallback, stale-data behavior, and source-of-truth checks are required. | Cache affects authorization, financial/customer-visible data, or critical workflow state. |

# 9. Security, AI, and Runtime Governance Gates
| Gate | Required Control |
| --- | --- |
| Identity and secrets | No passwords/tokens/secrets in code, prompts, logs, screenshots, Obsidian, LLM Wiki, GitNexus reports, test data, or evidence. Use approved secret references and rotation evidence. |
| OPA / SBAC / ABAC / RBAC | Authorization and skill decisions are policy-as-code, tested, logged, and fail-closed. Privilege expansion requires explicit business/security approval. |
| Authenticated DAST | Production-like authenticated scan uses synthetic users, non-prod scope, rate limits, scan windows, safe payloads, and remediation evidence. |
| AI governance | All model traffic routes through approved LiteLLM/gateway aliases with guardrails, classification eligibility, evaluation evidence, telemetry, and rollback route. |
| AI agents and System Builder | Agents may propose, draft, analyze, test, and prepare PRs. They cannot approve, merge, deploy, rotate production secrets, unlock privileged accounts, or bypass Harness/SBAC/OPA. |
| Runtime telemetry toggles | Logging/tracing/sampling/diagnostic toggles are approved configuration changes with safe defaults, performance guardrails, audit events, and rollback values. |
| Break-glass | Break-glass is time-bound, least-privilege, logged, monitored, business/security approved where possible, and subject to retrospective CAB and root-cause review. |

# 10. Rollback, Forward-Fix, Compensation, and BCDR Interface
| Change Type | Required Reversibility Path |
| --- | --- |
| Application release | Rollback artifact or forward-fix branch; smoke test; traffic/feature flag control; Sentry/trace monitoring; rollback decision owner. |
| Configuration / runtime toggle | Previous version/value, activation/deactivation path, registry audit, cache invalidation, monitoring window, owner approval. |
| Dynamic Workspace | Previous template/component/action binding; safe fallback page; layout/template cache invalidation; visual/a11y smoke test. |
| MicroFunction | Previous transaction definition, step deactivation, idempotency guard, audit/outbox reconciliation, compensation procedure. |
| Database | Expand/contract or forward-fix; backup/restore or PITR if required; data reconciliation; no ungoverned direct edits. |
| Event / Kafka replay | Replay by approved runbook; idempotent consumers; schema compatibility; DLQ sample validation; reconciliation report. |
| AI agent / model route / prompt | Disable agent, revoke/scope tools, revert prompt/guardrail/route, quarantine unsafe memory/RAG/context/output, rerun evals. |
| Infrastructure / environment | GitOps/Helm/IaC rollback, immutable artifact restore, drift remediation, secret rotation, BCDR evidence update. |
| Emergency change | Temporary containment is allowed only with incident evidence; permanent fix follows normal change path with RCA/PIR. |

# 11. CAB Operating Model and Decision Records
| CAB Element | Required Minimum Content |
| --- | --- |
| Agenda item | Change ID, owner, service, classification, environment, release window, affected users, risk tier, business driver. |
| Evidence review | CI/CD evidence pack, GitNexus impact, security scan status, contract/Flyway/policy evidence, test results, observability readiness, rollback. |
| Approval decision | Approved, approved with conditions, deferred, rejected, emergency ratified, or waiver approved with expiry and remediation plan. |
| Separation of duties | Maker, checker, approver, deployer, operator, and auditor roles are named and separated for high-risk changes. |
| Risk and waiver | Residual risk, compensating controls, accountable risk owner, waiver expiry, follow-up evidence, and due date. |
| Implementation window | Start/end, blackout/conflict checks, communication plan, monitoring, hypercare, rollback decision point. |
| Post-review | Success/failure, incidents, rollback events, DAST/security findings, SLO impact, PIR/RCA, improvement backlog. |

# 12. Auto-Heal, Auto-Learn, and Auto-Improve Release Interface
| Loop | Allowed Release-Related Action | Promotion Boundary |
| --- | --- | --- |
| Auto-Heal | Detect issue, retrieve evidence, recommend containment, draft rollback/forward-fix, open incident/change/PR, run sandbox validation. | May not directly mutate production unless specifically pre-approved as a bounded, reversible, audited runbook action with human oversight. |
| Auto-Learn | Summarize incidents, failed gates, rollback outcomes, DAST results, test gaps, runtime anomalies, and reviewer feedback. | Learning output becomes a reviewed knowledge candidate; it does not update canonical standards or retrieval indexes without approval. |
| Auto-Improve | Draft refactoring, tests, policy, contract, prompt, guardrail, runbook, telemetry, resilience, and pipeline improvements. | Improvement must become ticket/ADR/TDL/PR with CI/CD, evidence, maker-checker, and CAB/ARB if triggered. |
| Candidate Loop Rule Issue detection, evidence retrieval, candidate fix or learning proposal, tests, and human approval are mandatory. Automation helps AIRA learn faster but never removes accountability, classification, policy, release, rollback, or evidence gates. |
| --- |

# 13. RACI and Responsibilities
| Role | Accountable Responsibilities |
| --- | --- |
| IT Head / Solutions Architecture Office | Owns governance standard, final architecture escalation, release principle interpretation, and major risk acceptance recommendation. |
| CAB Chair / Change Manager | Runs CAB, validates change classification, approval record, release window, waiver, emergency ratification, and post-change review. |
| DevSecOps Lead | Owns CI/CD gates, evidence pack, GitOps promotion, SBOM/provenance, release automation, and pipeline enforcement. |
| Software Development Lead | Owns code readiness, design-principle impact, branch discipline, PR quality, rollback strategy, and developer accountability. |
| Security Architecture / InfoSec | Owns security gates, OPA/SBAC, secrets hygiene, DAST/SAST review, threat impacts, break-glass oversight, and remediation evidence. |
| DBA / Data Governance | Owns Flyway release, database backup/restore impact, data classification, RLS, migration rehearsal, and reconciliation evidence. |
| SRE / Operations | Owns monitoring readiness, deployment runbook, SLO/error budget, hypercare, incident interface, rollback execution support, and operational handover. |
| QA/SDET | Owns test evidence, regression, contract, E2E, visual/a11y, resilience, and release-quality sign-off. |
| AI Governance | Owns agent, prompt, guardrail, model route, evaluation, trust tier, and AI telemetry release gates. |
| Internal Audit / Compliance | Reviews evidence completeness, control traceability, waiver closure, CAB records, and release auditability. |

# 14. Acceptance Criteria and Definition of Done
| Acceptance Area | Release Is Acceptable Only When |
| --- | --- |
| Governance | Change is classified, owned, ticketed, reviewed, approved through the correct path, and free from unresolved severe AVCI conflicts. |
| Evidence | Evidence pack is complete, tamper-resistant enough for audit needs, linked to source/commit/build/approval, and stored in the approved evidence path. |
| Security | Critical/high security, secret, policy, access-control, DAST, or supply-chain findings are resolved or formally waived with owner, expiry, and remediation. |
| Architecture | SOLID, Clean Architecture, DDD, ports/adapters, MicroFunction, Dynamic Workspace, API/event/database, and AI boundaries are preserved or improved. |
| Operations | Dashboards, alerts, runbooks, SLO impact, on-call/support, incident route, and hypercare window are ready. |
| Reversibility | Rollback, forward-fix, compensation, deactivation, or safe fallback is documented, tested where practical, and owned. |
| Post-release | Smoke tests, traces/logs/metrics/audit, error monitoring, DLQ/replay status, Sentry issues, and business outcome checks are completed. |
| Improvement | Known limitations, failed gates, waived risks, incidents, and improvement candidates are logged with owner and due date. |

# 15. AVCI Compliance Summary
| AVCI Property | Compliance Evidence |
| --- | --- |
| Attributable | Every release/change has owner, source, version, branch, commit, ticket, reviewer, approver, CAB/ARB record, deployment actor, and runtime evidence reference. |
| Verifiable | Release decisions rely on tests, scans, SBOM/provenance, policy checks, GitNexus impact, contract/Flyway evidence, telemetry, rollback proof, and post-release verification. |
| Classifiable | All changes, artifacts, evidence, logs, traces, model routes, AI outputs, screenshots, and records carry classification and handling rules. |
| Improvable | Failures, waivers, rollback events, incidents, post-release findings, support trends, and audit observations feed backlog, runbook, knowledge, prompt, guardrail, pipeline, and standard improvements. |
| Final Control Statement AIRA production promotion is not granted because a release builds successfully. It is granted only when governance, evidence, security, architecture, observability, reversibility, operational readiness, BCDR impact, human approval, and AVCI are complete. Delivery pressure does not lower the release gate. |
| --- |

