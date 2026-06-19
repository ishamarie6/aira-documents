---
title: "Production Readiness Review and Operational Readiness Review Standard"
doc_id: "AIRA-63"
version: "v1.0"
status: "final"
category: "Production and operational readiness"
source_docx: "AIRA_63_Production_Readiness_Review_and_Operational_Readiness_Review_Standard_v1.0.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 63-production-operational-readiness
  - final
  - aira-63
---



# Production Readiness Review and Operational Readiness Review Standard



AIRA
AI-Native Enterprise Platform

AIRA Production Readiness Review and Operational Readiness Review Standard

Production Readiness | Operational Readiness | Release Assurance | Evidence by Construction | AVCI Always
| Document ID | AIRA-DOC-063 |
| --- | --- |
| Version | v1.0 |
| Status | Draft for Architecture Review Board / CAB / Engineering Team Review |
| Classification | INTERNAL CONFIDENTIAL |

Discipline First. Automation Second. Intelligence Third. AVCI Always.

# Document Control
| Field | Value |
| --- | --- |
| Document Title | AIRA Production Readiness Review and Operational Readiness Review Standard |
| Document ID | AIRA-DOC-063 |
| Recommended Version | v1.0 |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; DevSecOps; Security Architecture; QA/SDET; Platform Engineering; SRE; DBA; AI Engineering; Internal Audit |
| Primary Parents | 01A; 01; 01B; 02; 10 through 10E; 11; 11A; 20; 30/30A; 31/31A; 42; 43; Dynamic Workspace standards |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for ARB/CAB/Engineering Review |
| Purpose | Define mandatory production readiness and operational readiness review controls before staging, pilot, production-like, or production activation. |
| External Alignment References | NIST SSDF; OWASP ASVS; SLSA; OpenTelemetry; CloudEvents; OPA; SRE/operational readiness practices |

# 1. Executive Summary

This standard defines how AIRA proves that a release, MicroFunction, Dynamic Workspace capability, AI agent, runtime configuration, API/event contract, database migration, or infrastructure change is ready for controlled promotion and sustainable operation. Production readiness validates that the change is safe to release. Operational readiness validates that the organization can run, observe, support, recover, improve, and audit it after release.

AIRA production readiness is not a sign-off meeting. It is an evidence-backed control gate. A change is not release-ready merely because it compiles, passes a demonstration, or has developer approval. It is release-ready only when architecture, security, DevSecOps, MicroFunction, API/event, database, observability, resilience, support, rollback, and AVCI evidence are complete and independently reviewable.

# 2. Mandatory Practice Statement

No AIRA artifact may be promoted to staging, pilot, production-like, or production unless it passes Production Readiness Review and Operational Readiness Review gates appropriate to its risk tier. Missing ownership, classification, evidence, rollback, observability, security, policy, idempotency, outbox, critical error, or approval evidence blocks promotion unless a formal time-bound waiver is approved by the required authority.

Figure 1. AIRA PRR/ORR Control Plane

# 3. Purpose and Scope
| In Scope | Out of Scope |
| --- | --- |
| PRR/ORR for applications, MicroFunctions, APIs, events, database migrations, AI agents, Dynamic Workspace changes, infrastructure, runtime config, and release packages. | Informal release approval, email-only signoff, direct production changes, manual DDL, untracked toggles, or agent/self-approved changes. |
| Evidence packs, release readiness, operational readiness, rollback, runbooks, dashboards, SLOs, support model, incident response, DR, and post-promotion assurance. | Replacing DevSecOps, security, architecture, data, observability, CAB, or ARB authority. |
| Human-authored, AI-assisted, System Builder-generated, and agent-generated candidate artifacts that require promotion. | Treating AI output, GitNexus, Obsidian, LLM Wiki, dashboards, or generated summaries as approval authority. |

# 4. Authority and Precedence
| Level | Authority | PRR/ORR Interpretation |
| --- | --- | --- |
| L0 | IT Head / ARB / CAB / Security Governance | Final authority for production-impacting acceptance, waivers, release gating, and exception handling. |
| L1 | 01A, 01, 01B, 02 | Universal architecture, AVCI, evidence, audit, traceability, and source governance controls. |
| L2 | 10 through 10E; 11; 11A; 20; 30/30A; 31/31A | Specialist readiness controls for MicroFunctions, DevSecOps, CI/CD, change, rollback, and observability. |
| L3 | This AIRA-DOC-063 Standard | Production and operational readiness control model. |
| L4 | Release evidence, runbooks, dashboards, PR/MR, CI/CD, audit logs | Operational proof. May tighten but must not weaken governing standards. |

# 5. Readiness Review Model
| Review Type | Primary Question | Mandatory Outcome |
| --- | --- | --- |
| Production Readiness Review | Is this change safe, secure, evidence-backed, reversible, and approved for promotion? | Go / No-Go / Conditional Go with waiver and controls. |
| Operational Readiness Review | Can AIRA operate, monitor, support, recover, audit, and improve this capability after release? | Run-ready operating model with SLOs, runbooks, dashboards, escalation, support and recovery proof. |
| Release Readiness Review | Is the release package complete, immutable, traceable, and promoted through approved environments? | Release evidence pack, artifact integrity, approval, rollback and monitoring plan. |
| Post-Promotion Assurance | Did the release behave as expected and produce evidence after activation? | Health confirmation, issues/RCA, lessons and backlog updates. |

Figure 2. Production Readiness Gate Stack

# 6. Production Readiness Gate Matrix
| Gate | Minimum Evidence | Blocks Promotion When |
| --- | --- | --- |
| Architecture | EDP impact, boundary review, ADR/TDL or waiver, package/ports-adapters proof. | Boundary violation, unresolved architecture conflict, no owner, or unreviewed material design change. |
| DevSecOps | CI/CD run, tests, scans, evidence manifest, GitNexus impact, SBOM/provenance where applicable. | Required checks missing, failed, stale, ownerless, or not linked to PR/MR. |
| Security and Policy | OPA/SBAC, secrets scan, SAST/SCA, authenticated DAST where required, abuse cases, remediation. | Critical/high risk without approved waiver and remediation plan; fail-open path exists. |
| MicroFunction Runtime | Catalog entry, runtime config, step envelope, idempotency, outbox, DLQ/replay, compensation, safe response. | Protected or mutating transaction lacks mandatory standard steps, evidence envelope, or rollback path. |
| API/Event/Data | OpenAPI, AsyncAPI, Avro/JSON Schema, CloudEvents, Flyway migration, compatibility, consumer impact. | Breaking change unmanaged; schema or migration missing tests and approval. |
| Observability | Log4j2, OpenTelemetry, Sentry, Loki, Tempo, Grafana, audit, alerts, trace reconstruction. | Critical paths cannot be observed or reconstructed by trace/evidence/audit references. |
| Resilience | Load/concurrency/failure tests, timeout/retry/bulkhead/circuit breaker, recovery and compensation proof. | Retry unsafe, duplicate unsafe, no DLQ/replay, no recovery or rollback evidence. |
| Operations | Runbook, support owner, on-call/escalation, SLO/SLI, backup/DR, knowledge handoff. | No accountable operator, runbook, monitoring, escalation, or recovery readiness. |

# 7. Operational Readiness Requirements
| Readiness Area | Required Control |
| --- | --- |
| Service Ownership | Named product/system owner, technical owner, SRE/operator, support group, escalation path, and steward for evidence and knowledge. |
| SLO/SLI/SLA | Defined availability, latency, error rate, throughput, saturation, DLQ, replay, policy-denial, and business outcome indicators. |
| Runbooks | Start/stop, health check, rollback, replay, DLQ handling, escalation, evidence retrieval, incident response, and break-glass procedures. |
| Dashboards and Alerts | Grafana panels and alert rules for health, SLO, errors, saturation, policy denies, outbox lag, DLQ, replay, and security signals. |
| Incident Management | Severity model, incident commander, communication path, RCA template, evidence preservation, and post-incident improvement process. |
| Backup, Restore, DR | Backup scope, restore procedure, RTO/RPO, restore test evidence, DR owner, data repair constraints, and recovery validation. |
| Knowledge and Training | Team handoff, support checklist, known errors, dependencies, limitations, and approved Obsidian/LLM Wiki projection. |
| Post-Promotion Monitoring | Timeboxed hypercare, release health report, rollback trigger, Auto-Learn candidate, and acceptance closure evidence. |

Figure 3. Operational Assurance and Continuous Improvement Loop

# 8. Evidence Pack Requirements
| Evidence Category | Minimum Content |
| --- | --- |
| Attributable | Owner, requester, source intake, branch, commit, reviewer, approver, runtime config version, affected service, AI-use declaration. |
| Verifiable | Tests, scans, policy decisions, architecture fitness, GitNexus, contract/schema results, migration proof, observability samples, release run. |
| Classifiable | Data classification, handling rule, retention rule, redaction proof, model route eligibility, evidence repository and access controls. |
| Improvable | Known limitations, waiver status, backlog items, incident/RCA references, lessons, prompt/guardrail/runbook/test updates. |
| Reversible | Rollback, forward-fix, compensation, feature disablement, cache invalidation, replay/reprocess, restore/rebuild, deactivation plan. |

# 9. Readiness Severity and Decision Model
| Decision | Meaning | Required Action |
| --- | --- | --- |
| Go | All mandatory gates pass and evidence is complete. | Proceed with controlled promotion and post-promotion monitoring. |
| Conditional Go | Non-critical gaps exist with approved waiver, compensating controls, owner, expiry and follow-up. | Proceed only within approved risk boundary and monitor closely. |
| No-Go | Blocking or critical evidence/control gap exists. | Do not promote. Remediate, retest and reconvene readiness review. |
| Rollback / Suspend | Post-promotion signal breaches stop condition. | Execute rollback, safe-disable, compensation, suspension or incident response. |

# 10. PRR / ORR RACI
| Role | Responsibility |
| --- | --- |
| Solutions Architecture Office / IT Head | Accountable for readiness standard, architecture approval, material exception routing, and release-governance direction. |
| Product/System Owner | Owns business acceptance, operational impact, risk acceptance request, and post-release benefit validation. |
| DevSecOps Lead | Owns pipeline, evidence pack, supply-chain controls, release artifact integrity, and promotion mechanics. |
| Security Architecture | Owns OPA/SBAC, secrets, threat/abuse cases, DAST scope, findings, and waivers. |
| QA/SDET | Owns test completeness, regression, performance, failure-path, acceptance, and evidence verification. |
| SRE / Platform Engineering | Owns operational readiness, SLOs, dashboards, runbooks, alerts, capacity, rollback and recovery execution. |
| DBA / Data Governance | Owns Flyway, schema/data readiness, restore tests, RLS/retention, data-fix controls, and migration evidence. |
| AI Governance / AI Engineering | Owns model route, guardrails, agent/action boundaries, AI evaluations, and AI-use evidence. |
| Internal Audit | Reviews evidence completeness, waiver aging, traceability, and control effectiveness. |

# 11. Non-Negotiable Rejection Rules

Reject production readiness when there is no named owner, no classification, no rollback path, no evidence pack, or no independent review.

Reject operational readiness when runbooks, dashboards, alerts, support model, restore/recovery proof, or post-promotion monitoring are missing.

Reject any change that disables mandatory audit, security, policy, classification, idempotency, outbox, DLQ/replay, or critical error evidence.

Reject direct production mutation by AI, System Builder, scripts, agents, notebooks, or developers outside approved change control.

Reject release of protected APIs without security testing, authenticated DAST where applicable, OPA/SBAC evidence, safe errors and remediation evidence.

Reject MicroFunction or event-driven releases without idempotency, outbox, consumer dedupe, DLQ/replay and trace reconstruction evidence where applicable.

# 12. Acceptance Criteria

PRR and ORR checklists are embedded into the release process and PR/MR evidence templates.

Every production-bound release has an evidence pack with AVCI, tests, scans, contracts, observability, rollback and approvals.

Every critical capability has SLOs, dashboards, alerts, runbooks, support ownership, incident path and post-promotion monitoring.

MicroFunction, API, event, database, Dynamic Workspace and AI-agent changes inherit their specialist readiness gates.

Waivers are risk-owned, time-bound, evidence-linked and reviewed for closure or escalation.

Post-promotion signals feed incidents, RCA, Auto-Learn candidates, runbook updates and backlog improvements.

# 13. External Reference Note

External references are supplemental validation sources only. They do not override AIRA source governance. They support secure development, application security verification, supply-chain evidence, telemetry consistency, event interoperability and policy-as-code practices.

# 14. AVCI Compliance Summary
| AVCI Property | How This Standard Satisfies It |
| --- | --- |
| Attributable | Defines owners, reviewers, approvers, release decision makers, support roles, evidence sources and operational accountability. |
| Verifiable | Requires tests, scans, contracts, policy decisions, observability, runbooks, GitNexus, evidence packs and post-promotion health proof. |
| Classifiable | Requires classification of releases, evidence, logs, traces, prompts, screenshots, runtime config, support data and retention handling. |
| Improvable | Links readiness gaps, incidents, waivers, SLO breaches, RCA, Auto-Learn candidates and backlog actions to controlled improvement. |

