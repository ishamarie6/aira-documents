---
title: "Reference Implementation Golden Paths Standard"
doc_id: "AIRA-72"
version: "v1.0"
status: "final"
category: "Reference implementation golden paths"
source_docx: "AIRA_72_Reference_Implementation_Golden_Paths_Standard_v1.0.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 72-reference-implementation-golden-paths
  - final
  - aira-72
---



# Reference Implementation Golden Paths Standard



AIRA
AI-Native Enterprise Platform

Reference Implementation Golden Paths Standard

AIRA-DOC-072 | Version v1.0 | Draft for ARB/CAB/Engineering Review

Golden Paths | Reference Repositories | System Builder Seeds | Evidence by Construction | MicroFunction Runtime | Dynamic Workspace | AI Governance | AVCI Always
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-072 |
| Document Title | AIRA Reference Implementation Golden Paths Standard |
| Version | v1.0 |
| Status | Draft for Architecture Review Board / CAB / Engineering Team Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; DevSecOps; Software Development; Security Architecture; QA/SDET; DBA; Platform Engineering; SRE; AI Governance; Internal Audit |
| Primary Audience | Developers, architects, QA/SDET, DevSecOps, System Builder operators, AI agent owners, SRE, Internal Audit |
| Primary Parents | 01A, 01, 01B, 02, 03, 10-10E, 11/11A, 20, 62-71 |
| Review Cadence | Quarterly; unscheduled on material technology, security, policy, MicroFunction, Dynamic Workspace, AI route, or evidence-model change |

Mandatory Practice Statement

AIRA golden paths are governed reference implementations, not informal examples. A golden path is acceptable only when its source code, configuration, contracts, policies, tests, observability, evidence manifest, rollback or compensation path, and review records prove that it preserves AIRA architecture, security, DevSecOps, MicroFunction, Dynamic Workspace, AI governance, and AVCI controls.

Discipline First. Automation Second. Intelligence Third. AVCI Always.

# 1. Executive Summary

This standard defines the governed AIRA reference implementation golden paths. Golden paths are executable, testable, evidence-producing templates that developers, System Builder, AI coding assistants, reviewers, and auditors use as the preferred implementation baseline for repeatable AIRA delivery patterns.

The purpose is to reduce architecture drift, accelerate safe delivery, and ensure that generated or human-authored work follows the approved path for MicroFunction runtime, Dynamic Workspace, API/eventing, database/Flyway, OPA/SBAC, observability, CI/CD evidence, AI safety, resilience, PRR/ORR, and rollback. A golden path does not replace standards; it operationalizes them as working reference code and evidence packs.
| Area | Outcome |
| --- | --- |
| Why this document is needed | AIRA now has strong standards. The next maturity step is executable reference implementation so teams do not reinterpret standards differently. |
| Primary outcome | A small set of approved examples that compile, test, scan, emit evidence, and demonstrate rollback/compensation. |
| Governance outcome | System Builder and AI assistants generate from approved paths instead of inventing uncontrolled architectures. |
| Audit outcome | Every golden path has traceable source, evidence manifest, control objectives, reviewers, and improvement history. |

# 2. Purpose, Scope, and Authority

## 2.1 Purpose

Define the official AIRA golden path model, required reference implementations, governance lifecycle, repository structure, evidence requirements, certification gates, and acceptance criteria for enterprise-grade reuse.

## 2.2 Scope
| Scope Area | Treatment |
| --- | --- |
| In Scope | Reference repositories, code templates, MicroFunction transactions, Dynamic Workspace examples, API/event examples, Flyway migrations, OPA policies, CI/CD pipelines, evidence packs, dashboards, runbooks, AI/RAG/tool-action examples, and System Builder generation seeds. |
| Out of Scope | One-off demo code, ungoverned snippets, uncontrolled AI outputs, direct production mutation, direct model-provider calls, manual DDL, frontend-only business authority, and examples without tests/evidence. |
| Authority | This document is subordinate to the AIRA architecture, AVCI, MicroFunction, DevSecOps, Policy-as-Code, Evidence Manifest, Data Governance, AI Certification, and PRR/ORR standards. |
| Conflict Rule | The stricter governing control applies. Conflicts become AVCI reconciliation items and are routed to the proper owner, ARB/CAB, security, data, or AI governance path. |

# 3. Golden Path Governance Principles
| Principle | Mandatory Meaning |
| --- | --- |
| GP-01 Source Controlled | Golden paths live in approved Git repositories. Obsidian and LLM Wiki receive curated summaries only. |
| GP-02 Executable First | A golden path must build, test, scan, render evidence, and demonstrate runtime behavior in a controlled environment. |
| GP-03 Configuration First | Prefer MicroFunction configuration, policies, rules, templates, and approved adapters before new custom code. |
| GP-04 Evidence by Construction | CI/CD produces evidence manifests, test reports, scans, GitNexus impact, observability proof, and rollback evidence. |
| GP-05 No Authority Bypass | No golden path may bypass OPA/SBAC, classification, identity, audit, guardrails, evidence, maker-checker, or CAB/ARB rules. |
| GP-06 System Builder Safe Seeds | System Builder may use golden paths as generation seeds but generated outputs remain draft until reviewed and promoted. |
| GP-07 Continuous Certification | Golden paths expire or require recertification when dependencies, policies, standards, model routes, runtime behavior, or evidence schemas change. |

# 4. Required AIRA Golden Paths

The following golden paths are the minimum reference implementation set. Each path must include source, contracts, configuration, policies, tests, evidence, observability, rollback or compensation, and documentation.
| Golden Path | Required Coverage |
| --- | --- |
| GP-01 Login / Authentication / Session / Authorization | Keycloak/OIDC, session, OPA/SBAC, suspicious-login triage, lock/unlock approval, audit, Sentry/Loki/Tempo/Grafana evidence. |
| GP-02 Standard Synchronous MicroFunction API Command | OpenAPI, thin controller, MicroFunction runtime envelope, STP-BUS isolation, validation, idempotency, audit, safe response. |
| GP-03 Event / Outbox / Idempotent Consumer / DLQ / Replay | AsyncAPI, Kafka, CloudEvents, Avro/JSON Schema, transactional outbox, inbox dedupe, DLQ, controlled replay, evidence. |
| GP-04 Human Approval Workflow | Maker-checker workflow with Flowable/Temporal boundary, approval audit, timeout/escalation, resumption correlation, rollback. |
| GP-05 AI/RAG Advisory and Tool-Action Boundary | LiteLLM route, guardrails, retrieval eligibility, prompt/model audit, tool/Harness mediation, OPA/SBAC, human approval. |
| GP-06 Dynamic Workspace Experience Block | Backend-governed workspace component, policy-filtered resolver, MicroFunction-backed action, accessibility, telemetry, rollback. |
| GP-07 Auto-Heal / Auto-Learn / Auto-Improve Candidate Loop | Detection, evidence retrieval, hypothesis, candidate PR/runbook/test/policy update, human approval, monitoring, knowledge update. |
| GP-08 PRR/ORR and Resilience Lab Readiness | Performance/concurrency/chaos tests, SLO dashboards, runbooks, support model, rollback/forward-fix, release evidence. |

# 5. Golden Path Repository Model
| Repository Folder | Required Contents |
| --- | --- |
| /docs | Golden path overview, sequence diagrams, ADR/TDL, runbook, usage guide, review checklist. |
| /contracts | OpenAPI, AsyncAPI, Avro/JSON Schema, CloudEvents examples, generated clients, compatibility tests. |
| /src | Application, domain, ports, adapters, MicroFunction runtime or sample service implementation. |
| /config | Runtime configuration, feature flags, policy bindings, environment manifests, template parameters. |
| /migrations | Flyway migrations, seed data, RLS/index/view examples, rollback or forward-fix instructions. |
| /policies | OPA/Rego, Conftest, SBAC tests, data-handling policies, runtime-toggle policies, AI/tool-action policies. |
| /tests | Unit, component, contract, architecture, security, resilience, replay, performance, and regression tests. |
| /evidence | Evidence manifest, CI reports, GitNexus outputs, observability proof, approvals, PRR/ORR, Resilience Lab results. |
| /observability | Log4j2 config, OTel attributes, dashboard exports, Sentry/Loki/Tempo/Grafana queries and alert rules. |

# 6. Reference Implementation Lifecycle

Golden paths follow a controlled lifecycle. They may be proposed, built, certified, adopted, suspended, deprecated, or retired, but they must not be silently changed after teams and AI tools depend on them.
| Lifecycle State | Meaning |
| --- | --- |
| Draft | Candidate path created in branch or sandbox. Not reusable as authority. |
| Reviewed | Architecture, security, DevSecOps, QA, data, and AI reviewers validate design and evidence. |
| Certified | CI/CD, evidence manifest, Policy-as-Code, PRR/ORR, and Resilience Lab gates pass. |
| Adopted | May be used as developer template, System Builder seed, training reference, and reviewer baseline. |
| Suspended | Temporarily blocked due to defect, standard drift, security issue, dependency risk, or stale evidence. |
| Retired | Superseded path retained for lineage and audit but not used for new generation. |

# 7. Golden Path Evidence and Certification Gates

Every golden path must produce evidence that proves it is reusable. Evidence must be machine-readable where possible and mapped to control objectives and AVCI properties.
| Gate | Minimum Evidence |
| --- | --- |
| Architecture Gate | SOLID, Clean Architecture, DDD, ports/adapters, no direct infrastructure calls from business logic, bounded context isolation. |
| Contract Gate | OpenAPI/AsyncAPI/schema compatibility, generated client validation, safe errors, idempotency headers, CloudEvents metadata. |
| Database Gate | Flyway validate/migrate/clean-test, checksum, rollback/forward-fix, RLS/index/view evidence, no manual DDL. |
| Policy Gate | OPA/Rego and SBAC tests for allow, deny, escalate, classification, tenant, skill, tool, and environment decisions. |
| Security Gate | SAST/SCA/secrets/container/IaC/authenticated DAST where applicable, abuse cases, remediation evidence. |
| Observability Gate | Log4j2 redaction, OTel traces/metrics/logs, Sentry, Loki, Tempo, Grafana, audit, trace reconstruction. |
| Resilience Gate | Idempotency, concurrency, outbox/inbox, DLQ/replay, timeout, retry, circuit breaker, bulkhead, compensation tests. |
| AI Certification Gate | Model route, guardrail, red-team, RAG retrieval eligibility, prompt/output classification, tool-action boundary evidence. |
| Readiness Gate | PRR/ORR checklist, SLO, runbook, support model, rollback/safe-disable, monitoring, post-promotion plan. |

# 8. Golden Path Control Matrix
| Path | Core Controls | Evidence | Primary Owner |
| --- | --- | --- | --- |
| Login/Auth | Keycloak/OIDC, OPA/SBAC, session, lock/unlock workflow | Auth tests, abuse cases, audit, Sentry, policy decision log | Security Architecture / Development |
| Sync API Command | OpenAPI, MicroFunction envelope, STP-BUS, idempotency | Contract tests, architecture fitness, audit/log/trace evidence | Development / QA |
| Event/Replay | AsyncAPI, outbox, Kafka, schema registry, DLQ/replay | Outbox test, schema compatibility, replay approval and audit | Platform / SRE / DBA |
| Human Approval | Workflow boundary, SoD, maker-checker, escalation | Approval audit, workflow trace, timeout/escalation test | Business Owner / QA |
| AI/RAG/Tool | LiteLLM, guardrails, retrieval policy, Harness tool gateway | AI eval, red-team, prompt/model audit, human approval evidence | AI Governance |
| Dynamic Workspace | Policy-filtered resolver, MicroFunction action, accessibility | Component tests, e2e, telemetry, audit, policy result | Frontend / Product Owner |
| Auto-Improve | Proposal-only loop, evidence retrieval, candidate PR | RCA, tests, reviewer approval, improvement backlog | SRE / DevSecOps |
| PRR/ORR/Resilience | Production readiness, chaos/performance/concurrency | SLO, dashboard, runbook, rollback, Resilience Lab evidence | SRE / CAB |

# 9. System Builder and AI Assistant Usage Rules

System Builder, Codex, Claude Code, Hermes, and other approved AI assistants may use golden paths to draft artifacts, generate candidate code, produce tests, prepare policies, assemble evidence packs, and recommend improvements. They must not treat golden paths as authorization to self-approve or mutate production.
| Rule Area | Treatment |
| --- | --- |
| Allowed | Generate candidate artifacts from certified templates; prepare PR/MR drafts; create evidence summaries; propose tests, policies, and runbooks. |
| Required | AI-use declaration, source references, model route, guardrail result, classification, human checker, CI/CD evidence, rollback path. |
| Prohibited | Self-approval, direct Git merge, direct CI/CD/Kubernetes/database/secret access, direct model-provider calls, production mutation, gate suppression. |
| Failure Mode | If identity, policy, guardrail, evidence, tool gateway, or audit is unavailable, AI-assisted generation or action request fails closed. |

# 10. Production Use, PRR/ORR, and Resilience Requirements

A golden path must not be used for production-bound implementation unless it has current operational readiness and resilience evidence. The reference implementation must demonstrate safe deployment, safe disablement, rollback/forward-fix or compensation, and runtime monitoring.
| Binding | Required Result |
| --- | --- |
| PRR/ORR Binding | Golden path includes production readiness checklist, operational support model, SLO/SLA, alerting, runbook, dependency map, rollback plan. |
| Resilience Lab Binding | Golden path includes performance, load, concurrency, idempotency, outbox/DLQ/replay, failure injection, recovery, and chaos-safety evidence. |
| Runtime Evidence | Golden path includes sample traces, structured logs, metrics, audit events, dashboards, alerts, and trace reconstruction procedure. |
| Release Evidence | Golden path includes evidence manifest, SBOM/provenance, GitNexus impact, PR/MR AVCI summary, approvals, and change record. |

# 11. RACI
| Role | RACI | Responsibility |
| --- | --- | --- |
| Solutions Architecture Office / IT Head | A/R | Owns standard, approves golden path taxonomy, resolves conflicts and exceptions. |
| Enterprise Architecture | R | Reviews boundaries, EDP compliance, golden path certification, and architecture fitness. |
| DevSecOps Lead | A/R | Owns CI/CD templates, evidence pack automation, GitNexus, SBOM/provenance, and gate enforcement. |
| Software Development Lead | R | Owns reference implementation code quality, package boundaries, tests, and developer adoption. |
| Security Architecture | A/R | Owns OPA/SBAC, secure design, abuse cases, DAST, secrets hygiene, and risk acceptance. |
| QA/SDET | R | Owns deterministic tests, contract tests, replay tests, e2e tests, and evidence validation. |
| SRE / Platform Engineering | R | Owns resilience, observability, runtime readiness, dashboards, runbooks, and rollback exercises. |
| AI Governance | A/R | Owns model routes, guardrails, agent/tool-action certification, and AI-use evidence. |
| Internal Audit | C/I | Reviews evidence completeness, traceability, waiver aging, and control effectiveness. |

# 12. Implementation Roadmap
| Phase | Execution Focus | Exit Evidence |
| --- | --- | --- |
| Phase 0 | Approve golden path taxonomy and repository naming convention. | Golden path register and owner list. |
| Phase 1 | Build GP-01, GP-02, and GP-03 as minimum technical foundations. | Login, synchronous API, and event/outbox paths compile, test, scan, and produce evidence. |
| Phase 2 | Build GP-04, GP-05, and GP-06 for workflow, AI, and Dynamic Workspace. | Human approval, AI/RAG/tool, and workspace examples certified. |
| Phase 3 | Build GP-07 and GP-08 for improvement and production-readiness. | Auto-Improve candidate loop and PRR/ORR/Resilience path certified. |
| Phase 4 | Integrate golden paths into System Builder templates and CI/CD validators. | System Builder can generate branch-bound candidates with evidence manifests. |
| Phase 5 | Quarterly assurance, drift detection, recertification, and retirement process. | Golden path register shows active, suspended, deprecated, and retired paths. |

# 13. Acceptance Criteria

• Each golden path has a named owner, bounded context, classification, source repository, CODEOWNERS, and lifecycle status.

• Each golden path builds from pinned toolchains and produces a complete evidence manifest.

• Mandatory API, event, database, policy, security, observability, AI, and resilience gates are represented where applicable.

• No golden path contains direct provider calls, manual DDL, frontend business authority, direct DB/Kafka from business logic, or hidden policy logic.

• Each golden path includes rollback, forward-fix, compensation, safe-disable, deactivation, or replay/reprocess guidance.

• System Builder and AI assistant usage is explicitly draft/proposal-only until human review, CI/CD gates, and approval are complete.

• Golden path examples are mapped to AIRA control objectives and evidence classes in the traceability matrix.

# 14. Anti-Patterns and Rejection Rules
| Anti-Pattern | Required Response |
| --- | --- |
| Demo-only path | Reject. Golden paths must be executable, tested, scanned, observed, reversible, and evidence-producing. |
| Generated path without human review | Reject. AI/System Builder output remains draft until reviewed and approved. |
| Happy-path-only tests | Reject. Include negative, abuse-case, failure, concurrency, replay, and rollback/compensation evidence. |
| Obsidian as authority | Reject. Git/Flyway/PostgreSQL and approved evidence stores remain authoritative; Obsidian is projection. |
| Disabled gates for speed | Reject. Required architecture, security, policy, audit, evidence, and promotion gates fail closed. |
| Golden path drift | Suspend until dependencies, standards, policies, evidence schema, and runtime behavior are recertified. |

# 15. Open Reconciliation Items
| ID | Issue | Severity | Owner |
| --- | --- | --- | --- |
| RI-072-001 | Assign canonical repository naming and package structure for golden paths. | Medium | Solutions Architecture Office |
| RI-072-002 | Map golden paths to 00D/00E canonical register and document supersedence model. | Medium | Architecture Board |
| RI-072-003 | Create System Builder template bindings for each certified golden path. | High | AI Governance / DevSecOps |
| RI-072-004 | Decide whether GP-01 Login should reuse PoC 1/1A or become a separate reference repository. | Medium | Development Lead |
| RI-072-005 | Define recertification triggers for external dependency, model route, and policy changes. | Medium | Security / SRE |

# 16. AVCI Compliance Summary
| AVCI Property | Evidence in This Standard |
| --- | --- |
| Attributable | Golden paths define owner, source repository, branch, commit, version, CODEOWNERS, reviewers, approvers, AI-use records, and lifecycle status. |
| Verifiable | Golden paths require CI/CD results, tests, scans, policy decisions, architecture fitness, contracts, Flyway, evidence manifests, observability, PRR/ORR, and Resilience Lab evidence. |
| Classifiable | Golden paths require data, artifact, prompt, evidence, telemetry, model-route, and repository classification with redaction and handling rules. |
| Improvable | Golden paths include issue backlog, failed-gate learning, runtime feedback, drift detection, recertification, deprecation, and versioned improvement path. |

Final Rule

AIRA golden paths are production-grade reference implementations only when they are executable, governed, evidence-producing, secure, observable, reversible, and AVCI-compliant. A sample without evidence is not a golden path.

