---
title: "AVCI Engineering Standard"
doc_id: "AIRA-01"
version: "v3.2"
status: "revised"
category: "Engineering standards"
source_docx: "AIRA_01_AVCI_Engineering_Standard_v3.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 01-engineering-standards
  - revised
  - aira-01
---



# AVCI Engineering Standard



AIRA
AI-Native Enterprise Platform
AVCI Engineering Standard
Attributable | Verifiable | Classifiable | Improvable
Universal Quality, Evidence, and Lifecycle Control Standard
Version 3.2 Revised | June 2026 | INTERNAL CONFIDENTIAL

Mandatory Practice Statement

Nothing that influences AIRA system behavior, customer outcomes, business decisions, security posture, operational evidence, Dynamic Workspace UX, MicroFunction runtime behavior, AI output, or DevSecOps promotion may be treated as production-ready unless it satisfies AVCI and the current canonical enterprise design principles. AVCI is not documentation style; it is the governed engineering control plane for trust, architecture discipline, safety, observability, reversibility, and continuous improvement.
| Property | Value |
| --- | --- |
| Document ID | AIRA-DOC-001 |
| Document Title | AIRA AVCI Engineering Standard |
| Canonical Filename | 01-AIRA_AVCI_Engineering_Standard_v3.2_Revised.docx |
| Version | v3.2 - Dynamic Workspace, MicroFunction, System Builder, AI Agent, Evidence, and Reconciliation Update |
| Supersedes | 01-AIRA_AVCI_Engineering_Standard_v3.1_Aligned.docx |
| Canonical Companion | 01A-AIRA_Enterprise_Architecture_Principles_SOLID_and_Fitness_Function_Standard_v1.2_Revised.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Architecture Review Board / CAB approval and controlled baseline adoption |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; DevSecOps; Security Architecture; QA/SDET; Platform Engineering; AI Governance; Data Governance; SRE / Operations; Internal Audit |
| Review Cadence | Quarterly; unscheduled on material architecture, security, AI, Dynamic Workspace, MicroFunction, DevSecOps, evidence, regulatory, or technology-stack change |
| Evidence Path | OpenKM Tier-0 / AIRA / Governance / AVCI / v3.2 / |

Document Control Note. This revision updates AIRA-DOC-001 after the canonical consolidation of 01A. 01A v1.2 is treated as the governing enterprise architecture and EDP authority. This document remains the universal AVCI quality and evidence gate that every AIRA artifact must satisfy before promotion.

# 1. Executive Summary

AIRA is a mission-critical, AI-native enterprise platform. Its quality model cannot depend on informal review or manual memory. It must be designed into the lifecycle of every artifact, including requirements, design, source code, configuration, MicroFunctions, Dynamic Workspace components, database migrations, APIs, events, prompts, guardrails, AI agents, model routes, environment provisioning, tests, runbooks, evidence records, and operational telemetry.

Version 3.2 upgrades the AVCI Engineering Standard to align with the newly consolidated 01A v1.2 architecture authority and the revised Dynamic Workspace, MicroFunction, System Builder, AI agent, DevSecOps, observability, and continuous-improvement control family. AVCI becomes the universal acceptance language for AIRA: every artifact must be attributable, verifiable, classifiable, and improvable before it is trusted.
| v3.2 Alignment Area | Required Outcome |
| --- | --- |
| 01A canonical consolidation | AVCI references one canonical 01A authority for EDP-01 through EDP-20, SOLID, Clean Architecture, DDD, ports/adapters, fitness functions, and architecture boundaries. |
| Dynamic Workspace | UX, templates, widgets, AI panel, Experience Blocks, Experience Packs, Admin Builder, and configuration seeders are backend-governed, policy-filtered, observable, reversible, and evidence-producing. |
| MicroFunction runtime | Runtime assembly, standard steps, custom business functions, outbox, audit, idempotency, DLQ/replay, rollback, and evidence are treated as AVCI-governed artifacts. |
| System Builder and AI agents | AI may analyze, recommend, draft, test, and propose. It may not approve, silently mutate production, bypass policy, or promote without AVCI evidence and human review. |
| DevSecOps and GitNexus | CI/CD, GitNexus, evidence packs, SAST, DAST, SCA, SBOM/provenance, policy checks, architecture fitness, and rollback evidence become mandatory verification paths. |
| Observability and runtime toggles | Logs, metrics, traces, audit, security, policy, classification, and evidence signals are designed for trace reconstruction; performance toggles cannot disable mandatory security/audit/evidence telemetry. |

Operating Philosophy. Discipline first, automation second, intelligence third, and AVCI always. Discipline establishes the rules. Automation makes them repeatable. Intelligence accelerates analysis and generation. AVCI keeps all three trustworthy.

Figure 1. AVCI engineering control plane. The four AVCI properties bind architecture, promotion, runtime evidence, and continuous improvement.

# 2. Purpose, Scope, and Authority

## 2.1 Purpose

The purpose of this standard is to define the universal AIRA quality, trust, evidence, classification, and improvement discipline for every artifact that can influence system behavior, delivery risk, security posture, operational support, AI behavior, or auditability. It converts AIRA governance into practical lifecycle controls that can be verified through PR/MR evidence, CI/CD gates, runtime telemetry, dashboards, audit records, and improvement backlogs.

## 2.2 In Scope

Source code, configuration, infrastructure-as-code, database migrations, Flyway scripts, build scripts, container images, Helm charts, GitOps manifests, policies, secrets metadata, runtime parameters, prompts, guardrails, and deployment artifacts.

Dynamic Workspace artifacts: templates, widgets, Experience Blocks, Experience Packs, Admin Builder outputs, runtime configuration, accessibility evidence, UX behavior, component catalogs, AI Assistant Panel outputs, and configuration seed data.

MicroFunction artifacts: transaction definitions, step catalogs, runtime parameters, idempotency profiles, audit/outbox records, compensation paths, policy decisions, and execution evidence.

API, event, workflow, data, AI, and provisioning contracts: OpenAPI, AsyncAPI, Kafka, Avro/JSON Schema, CloudEvents, Flowable/Temporal, OPA/Rego, SBAC, model-route, tool-action, and provisioning manifests.

Evidence and operations artifacts: logs, traces, metrics, audit events, Sentry events, Grafana dashboards, Loki/Tempo records, incident records, SLO evidence, GitNexus reports, security scans, test results, SBOM/provenance, and rollback evidence.

## 2.3 Out of Scope

Informal notes, unmanaged chat transcripts, experimental AI outputs, personal prompts, or local-only artifacts that have not been promoted into AIRA source governance.

Autonomous production mutation, uncontrolled AI agent execution, direct model-provider calls, direct production credentials, manual production DDL, and any change path that bypasses AIRA policy, evidence, CI/CD, or human approval gates.

## 2.4 Authority and Precedence
| Level | Authority | Role |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance / Data Governance | Final authority for production-impacting exceptions, waivers, major architecture decisions, and unresolved conflicts. |
| L1 | 01A Enterprise Architecture Principles, SOLID, and Fitness Function Standard v1.2 | Canonical authority for EDP-01 through EDP-20, SOLID, Clean Architecture, DDD, ports/adapters, architecture fitness, and System Builder architecture boundaries. |
| L1 | This 01 AVCI Engineering Standard v3.2 | Universal quality, evidence, classification, lifecycle, acceptance, and improvement gate for all AIRA artifacts. |
| L2 | 02/03/04/05/06/07/10/11/12A/15/16/17/20/31A/42/43/53-61 companion standards | Specialist implementation standards that inherit AVCI and 01A controls. |
| L3 | ADRs, TDLs, waivers, tickets, PRs/MRs, runbooks, evidence packs | Implementation-specific records that must trace to approved standards and cannot weaken them. |

Conflict Rule. When two documents conflict, do not silently choose the easier interpretation. Identify the conflict, classify severity, recommend the governing source, and log it as an AVCI reconciliation item through the revision-control register.

# 3. v3.2 Change Summary
| Change Area | v3.2 Improvement |
| --- | --- |
| Canonical 01A alignment | Updates the AVCI standard to reference 01A v1.2 as the single architecture-principle authority after duplicate 01A consolidation. |
| EDP-01 to EDP-20 linkage | Makes the 20 enterprise design principles mandatory evidence dimensions for material artifacts, not optional narrative statements. |
| Dynamic Workspace governance | Adds AVCI requirements for frontend UX, Admin Builder, AI panel, templates, widgets, accessibility, responsive behavior, safe states, and runtime configuration. |
| MicroFunction and backend assembly | Adds evidence requirements for runtime assembly, standard step reuse, configuration-first delivery, idempotency, outbox, audit, DLQ, replay, rollback, and resilience. |
| API/event/data contracts | Strengthens OpenAPI, AsyncAPI, Kafka, Avro/JSON Schema, CloudEvents, schema evolution, idempotent consumer, outbox, replay, and contract-test evidence. |
| DevSecOps and supply chain | Adds security gates, authenticated DAST, abuse cases, SAST/SCA/secret scans, SBOM/provenance, GitNexus impact analysis, and SLSA-style provenance evidence. |
| AI governance | Requires LiteLLM-approved model routes, guardrails, agent registry evidence, SBAC/OPA tool authorization, human approval, evaluation evidence, and fail-closed behavior. |
| Runtime toggles | Clarifies that performance-oriented telemetry toggles may adjust diagnostic verbosity, but must not disable mandatory security, policy, classification, audit, or evidence signals. |
| Continuous improvement | Constrains Auto-Heal, Auto-Learn, and Auto-Improve to candidate/proposal loops until review, tests, policy checks, rollback, and human approval are complete. |

# 4. The AVCI Standard
| AVCI Property | Mandatory Meaning | Minimum Evidence |
| --- | --- | --- |
| Attributable | The artifact has a named owner, source, intent, version, responsible role, approver/checker, and affected bounded context. | Owner field, source reference, ticket/ADR/TDL, branch/commit, CODEOWNERS, maker/checker, approval record. |
| Verifiable | The artifact can be independently checked through tests, scans, policy decisions, telemetry, trace reconstruction, review evidence, or runtime behavior. | Unit/component/contract/E2E tests, OPA tests, SAST/DAST/SCA, GitNexus report, CI run, evidence pack, dashboard, audit query. |
| Classifiable | The artifact and its data flows have classification, handling rules, retention, model-route eligibility, logging/redaction rules, and access constraints. | Classification tag, OPA/SBAC policy, data-handling rule, redaction proof, retention rule, retrieval eligibility, evidence path. |
| Improvable | The artifact has a feedback path, known limitations, owner review cadence, supersedence path, rollback/retirement path, and backlog linkage. | Improvement backlog, telemetry trend, incident/RCA, version history, deprecation plan, rollback/forward-fix, compensation evidence. |

AVCI Production Rule. AIRA does not accept artifacts that are merely functional. AIRA accepts artifacts only when they are governed, traceable, testable, secure, observable, reversible, and evidence-producing.

# 5. Universal AVCI Application Model
| Artifact Type | Attributable | Verifiable | Classifiable | Improvable |
| --- | --- | --- | --- | --- |
| Requirement / Intake | owner, source, business intent, affected context | acceptance criteria, impact analysis, review path | data class, risk tier, model-route eligibility | backlog link, change history, supersedence path |
| Source Code / Config | author, branch, commit, reviewer, module owner | tests, scans, architecture fitness, CI evidence | secret-safety, classification, runtime scope | technical debt, feature flag, rollback, refactor path |
| MicroFunction | transaction owner, step owner, config version | step tests, policy decision, audit/outbox, replay test | classification ceiling, actor scope, policy binding | catalog update, improvement metric, compensation path |
| Dynamic Workspace UX | template owner, component owner, approver | Playwright, accessibility, visual regression, API/policy tests | screen/component classification, redaction, safe states | UX feedback, A/B review, template supersedence, rollback |
| API/Event Contract | API/event owner, consumer list, schema version | lint, contract tests, compatibility, schema registry | payload classification, topic/API access policy | deprecation plan, consumer migration, replay plan |
| AI Prompt / Agent / Model Route | agent/prompt owner, purpose, skill scope | evals, guardrails, route audit, red-team/certification | classification ceiling, memory/RAG eligibility, tool scope | prompt registry versioning, recertification, retirement |
| Evidence Pack | release owner, PR/MR, pipeline, evidence producer | checksums, CI results, scan outputs, trace IDs, reviewer sign-off | storage class, retention, redaction, access scope | re-run path, evidence gaps, issue links, audit findings |

# 6. Relationship to Enterprise Design Principles

The four AVCI dimensions and the 20 Enterprise Design Principles must be evaluated together. AVCI asks whether an artifact can be trusted across its lifecycle. EDP-01 through EDP-20 ask whether it preserves architecture, security, resilience, autonomy, reversibility, and evidence discipline. A material artifact is not accepted when it satisfies AVCI wording but weakens the design principles.
| EDP Group | AVCI Evidence Required |
| --- | --- |
| EDP-01 to EDP-05: SOLID, Clean Architecture, DDD, Ports/Adapters, DRY/KISS/YAGNI | Architecture impact summary, boundary review, dependency graph, CODEOWNERS, ADR/TDL where required. |
| EDP-06 to EDP-08: Idempotency, Determinism, Fail-Safe | Retry/replay tests, deterministic fixtures, idempotency keys, fail-closed tests, compensation plan. |
| EDP-09 to EDP-11: Human-in-the-Loop, Least Privilege/SBAC, Separation of Duties | Approval workflow, SBAC grant, OPA decision, maker-checker split, privileged action evidence. |
| EDP-12 to EDP-17: Observability, Policy as Code, Testability, Secure by Design, Resilience, Fitness Functions | Trace/log/metric/audit schema, OPA/Rego tests, SAST/DAST/SCA, abuse cases, Resilience Lab, CI gates. |
| EDP-18 to EDP-20: Progressive Autonomy, Reversibility/Rollbackability, AVCI | Trust tier, autonomy risk tier, kill switch, rollback, forward-fix, evidence pack, improvement path. |

# 7. AVCI Evidence Record Schema v3.2
| Field | Required Meaning |
| --- | --- |
| evidence_id | Unique evidence record identifier. |
| artifact_id / artifact_type | Code, config, API, event, MicroFunction, workspace, prompt, agent, migration, workflow, runbook, evidence pack, or provisioning artifact. |
| owner / maker / checker / approver | Named accountable parties with separation-of-duties evidence where required. |
| source_ref | Ticket, requirement, incident, log query, document, PR/MR, ADR/TDL, upload, workflow, or controlled conversation reference. |
| bounded_context / service / workspace_code | Domain, service, schema, workspace, transaction, or platform capability affected. |
| classification / handling_rule | Public, Internal, Confidential, Restricted; redaction, retention, retrieval, model-route, logging, and storage rules. |
| verification_refs | Test IDs, scan IDs, policy decisions, CI run, contract evidence, GitNexus report, trace IDs, dashboard URLs, audit records. |
| policy_decision_refs | OPA/SBAC/ABAC/RBAC/admission/guardrail/model-route/tool-authorization decisions. |
| trace_refs | trace_id, span_id, request_id, correlation_id, causation_id, event_id, microfunction_run_id, agent_run_id. |
| risk_and_principle_impact | Risk tier, affected EDP IDs, architecture impact, security impact, privacy impact, reliability impact. |
| reversibility_ref | Rollback, forward-fix, compensation, deactivation, restore, rebuild, retirement, or kill-switch plan. |
| improvement_ref | Backlog item, RCA, SLO burn, audit finding, Auto-Heal/Learn/Improve proposal, supersedence record. |

Figure 2. AVCI artifact lifecycle and evidence gates. Protected artifacts fail closed when required evidence is missing.

# 8. Dynamic Workspace and Frontend AVCI Requirements

Dynamic Workspace outputs are not exempt from backend governance. A template, widget, Experience Block, Experience Pack, Admin Builder change, AI Assistant Panel action, or UX state is accepted only when its backend binding, policy decision, classification, telemetry, accessibility, and rollback evidence are present.
| Workspace Area | AVCI Requirement |
| --- | --- |
| Workspace resolution | Record actor hash, tenant/context, workspace_code, screen_code, template version, policy hash, layout hash, cache source, and evidence_ref. |
| Component / widget rendering | Evidence component_key, component_instance_id, classification, policy decision, safe/denied/empty/error/degraded state, and accessibility result. |
| Widget action | Bind action to OpenAPI contract, OPA/SBAC policy, idempotency key, MicroFunction transaction, audit event, outbox event, and trace_id. |
| Admin Builder / templates | Maker, checker, approver, version, activation date, rollback target, compatibility tests, accessibility tests, and evidence pack are required. |
| AI Assistant Panel | Prompt metadata, input/output mode, model route, guardrail result, source references, artifact IDs, tool action request, human approval, and safe action boundary are required. |

# 9. MicroFunction and Backend Runtime AVCI Requirements
| Control Area | Mandatory Rule |
| --- | --- |
| Configuration-first delivery | Use existing standard steps, OPA/DMN/rules, templates, and runtime configuration before writing new business code. |
| Step evidence | Every step that affects state, policy, classification, integration, AI, or user outcome must emit trace, audit, metric, and evidence references. |
| Idempotency | Mutating steps, callbacks, consumers, replays, approvals, and tool actions must be retry-safe and duplicate-safe. |
| Outbox and events | Business-state changes that publish events must use transactional outbox or equivalent governed reliability pattern. |
| DLQ and replay | DLQ entries must carry classification, correlation IDs, schema version, retry count, failure reason, owner, and replay authorization path. |
| Reversibility | Each transaction defines rollback, forward-fix, compensation, deactivation, or safe stop behavior. |
| No business logic in adapters | Controllers, UI, queue consumers, and infrastructure adapters remain thin. Business rules live in domain/application/MicroFunction/policy layers. |

# 10. API, Event, Database, and Workflow Evidence

Figure 3. Dynamic Workspace, MicroFunction, API/event, and evidence correlation model.
| Artifact | Mandatory Verification Evidence |
| --- | --- |
| OpenAPI | Contract linting, generated client compatibility, auth/error/idempotency profile, OPA/SBAC mapping, DAST result, safe response tests. |
| AsyncAPI / Kafka | Topic ownership, schema version, CloudEvents attributes, consumer compatibility, idempotent consumer tests, DLQ/replay evidence. |
| Avro / JSON Schema | Backward/forward compatibility, classification tags, PII redaction rules, schema registry evidence, producer/consumer tests. |
| CloudEvents | source, type, subject, id, time, datacontenttype, specversion, correlation/causation IDs, classification extension, trace context. |
| Database / Flyway | Owner, migration ID, checksum, clean/migrate report, rollback/forward-fix, RLS/classification, seed data, no manual DDL evidence. |
| Temporal / Flowable / DMN | Workflow owner, state model, compensation, timeout/escalation, approval rules, SoD, audit trail, replay test. |

# 11. DevSecOps, GitNexus, and Evidence Pack Gates

Every production-bound artifact must pass the appropriate CI/CD, security, policy, architecture, accessibility, contract, resilience, and evidence gates. GitNexus may provide code intelligence and impact evidence, but it remains read-only, derivative, and subordinate to tests, scans, policy checks, and human review.
| Gate | Required Evidence |
| --- | --- |
| Repository / branch governance | CODEOWNERS, branch protection, signed commits where required, PR/MR AVCI summary, AI-use declaration. |
| Build / package | Java/runtime/toolchain version, build image digest, dependency lock, artifact digest, reproducible build evidence. |
| Tests | Unit, component, contract, E2E, Playwright, accessibility, mutation, policy, migration, idempotency, replay, resilience tests as applicable. |
| Security | SAST, SCA, secret scan, IaC scan, container scan, authenticated DAST, API security, abuse cases, threat-model delta, remediation evidence. |
| Supply chain | SBOM, provenance/attestation, dependency license review, package signing, trusted build/pipeline evidence. |
| GitNexus | Code map, blast radius, affected tests/contracts/workflows, architecture drift, sensitive area impact, reviewer focus summary. |
| Promotion | Maker-checker, CI pass, ARB/CAB trigger decision, rollback/forward-fix/compensation, monitoring plan. |

# 12. Observability, Audit, Runtime Toggle, and Trace Reconstruction

Observability is an AVCI verification mechanism. AIRA must be able to reconstruct who did what, why it happened, under which policy, with what input classification, through which MicroFunction/API/event/workflow/agent route, and with which outcome.
| Signal | Required Treatment |
| --- | --- |
| Logs / Log4j2 | Structured logs only; no secrets, raw tokens, raw PII, raw prompts with Restricted data, embeddings, private keys, or uncontrolled customer payloads. |
| Traces / OpenTelemetry | Propagate trace_id, span_id, request_id, correlation_id, causation_id, policy decision ID, MicroFunction run ID, agent run ID, and evidence_ref. |
| Metrics / Grafana | Low-cardinality operational metrics for latency, error rate, policy denials, cache hit/miss, queue lag, DLQ, replay, SLO burn, guardrail outcomes. |
| Error monitoring / Sentry | Classified error events with release, environment, service, route/topic, safe stack summary, correlation IDs, and remediation links. |
| Loki / Tempo | Log and trace stores must support trace reconstruction without leaking sensitive data. |
| Audit events | Append-only, actor-bound, policy-linked, classification-aware evidence for material user, system, agent, workflow, and admin actions. |
| Runtime toggles | Diagnostic verbosity may be tuned for performance; mandatory security, policy, classification, audit, evidence, and regulatory signals are non-disableable without approved break-glass record. |

# 13. Security, Classification, OPA/SBAC, and Model-Route Controls
| Security Area | AVCI Control |
| --- | --- |
| OPA/SBAC/RBAC/ABAC | Every protected action has policy input, decision ID, actor, skill, role, context, classification, and evidence record. |
| Secrets hygiene | No secrets in code, prompts, logs, screenshots, tests, documentation, telemetry, AI context, or generated artifacts. Vault or approved abstraction is required. |
| Authenticated DAST | Protected APIs and Dynamic Workspace flows must be tested with authenticated roles, denied roles, expired sessions, and abuse cases. |
| Secure APIs | OpenAPI defines auth, idempotency, safe errors, rate limits, validation, classification, pagination, and problem details. |
| Model routes | No direct model-provider calls from application code, notebooks, scripts, or agents. Use LiteLLM-approved aliases and guardrails. |
| Guardrails | Input, retrieval, execution/tool action, and output checkpoints are required for AI-assisted workflows and Dynamic Workspace AI features. |
| Remediation evidence | Security findings require severity, owner, SLA, fix evidence, retest evidence, waiver if any, and audit closure. |

# 14. Concurrency, Heavy Transaction, Idempotency, Outbox, and Resilience Lab

AVCI verification must include failure-aware transaction behavior. AIRA systems must be retry-safe, duplicate-safe, concurrent-safe, replay-safe, and resilient under expected and degraded load.
| Scenario | Minimum Evidence |
| --- | --- |
| Double submit / repeated click / retry | Idempotency key, duplicate detection, safe user message, no duplicate business effect. |
| Concurrent approval or state transition | Optimistic locking or state-machine guard, SoD check, stale decision handling, audit trail. |
| Heavy transaction / async job | Job ID, progress state, timeout, back-pressure, retry policy, cancellation/compensation, dashboard. |
| Outbox publish failure | Outbox persistence, retry worker, DLQ escalation, replay authorization, event schema version. |
| Consumer failure | Idempotent consumer, dead-letter policy, poison message isolation, replay test, operator runbook. |
| Dependency outage | Timeouts, circuit breakers, bulkheads, degraded mode, safe fallback, no fail-open protected action. |

# 15. Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop
| Loop Stage | Allowed Behavior | Blocked Behavior |
| --- | --- | --- |
| Issue detection | Detect evidence from telemetry, incident, scan, test, user feedback, SLO burn, or GitNexus impact. | Suppress evidence, self-close incidents, or silently mutate production. |
| Evidence retrieval | Retrieve approved evidence with classification, provenance, freshness, and SBAC checks. | Use Restricted evidence without approval or leak sensitive content into prompts. |
| Candidate proposal | Generate candidate fix, learning item, test improvement, policy hardening, or refactor proposal. | Directly commit to main, approve itself, bypass ADR/TDL, or weaken controls. |
| Verification | Run deterministic tests, scans, contract checks, policy tests, replay tests, and architecture fitness checks. | Treat AI confidence or functional pass as sufficient evidence. |
| Human approval | Maker-checker review, Security/DBA/ARB/CAB when triggered, rollback plan, monitoring plan. | Allow AI to approve privileged, destructive, production, security, or policy-exception actions. |
| Activation and learning | Promote only through controlled PR/MR or change workflow; update runbooks/standards/backlog. | Update canonical knowledge, prompts, policies, agents, or production config without review. |

# 16. PR/MR AVCI Compliance Summary Template

Every non-trivial pull request or merge request must include an AVCI compliance summary. Teams may extend this template, but must not remove required fields.
| Section | Required Content |
| --- | --- |
| Attributable | Owner, maker, checker, approver, ticket/source, bounded context, branch, commit, AI tools used, prompt/agent/model-route references. |
| Verifiable | Tests, security scans, OPA/SBAC results, architecture fitness, contract checks, migration checks, GitNexus, evidence pack, runtime smoke tests. |
| Classifiable | Data class, handling, logging/redaction, secrets/PII/token handling, model-route eligibility, evidence storage/retention. |
| Improvable | Known limitations, backlog items, telemetry to watch, rollback/forward-fix, runbook updates, prompt/standard improvements. |
| EDP Impact | EDP-01 through EDP-20 impact status: preserved, improved, not applicable, exception requested, or rejected. |

# 17. Waivers, Exceptions, and Non-Conformance

Waivers are controlled risk records, not shortcuts. A waiver may be considered only when business need, technical constraint, risk acceptance, compensating controls, owner, expiry, remediation path, and approval authority are explicit. Waivers cannot authorize uncontrolled AI execution, direct production mutation, direct model-provider calls, secrets leakage, manual production DDL, or bypass of mandatory audit/security/evidence controls.
| Severity | Example | Required Action |
| --- | --- | --- |
| Critical | Missing policy check for protected action; direct model-provider call; secrets in code/logs; production mutation without approval. | Block promotion; create incident/security finding; remediate before acceptance unless formal break-glass path exists. |
| High | Missing rollback for production-bound change; failing authenticated DAST; missing classification for sensitive flow. | Block release unless CAB/ARB-approved waiver with expiry and compensating controls. |
| Medium | Incomplete GitNexus impact summary; non-critical accessibility gap; missing dashboard panel. | Create remediation task; may proceed only with owner, due date, and risk acceptance. |
| Low | Minor documentation drift or improvement opportunity. | Track in backlog; correct in next planned update. |

# 18. RACI
| Activity | Owner | Dev Lead | DevSecOps | Security | QA/SDET | DBA/Data | SRE/Ops | Internal Audit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| AVCI standard ownership | A/R | C | C | C | C | C | C | C |
| PR/MR AVCI evidence | A | R | R | C | R | C | C | I |
| Security and policy evidence | A | C | R | R | C | C | C | I |
| Database/Flyway evidence | A | C | C | C | C | R | I | I |
| Runtime observability evidence | A | C | R | C | C | I | R | I |
| Waiver / exception review | A/R | C | C | C/R | C | C | C | C |
| Audit sampling and control testing | A | I | I | C | C | C | C | R |

# 19. Implementation Roadmap and Acceptance Criteria
| Phase | Target Outcome | Exit Criteria |
| --- | --- | --- |
| Phase 1 - Adopt v3.2 | AVCI v3.2 approved as the universal quality/evidence gate after 01A v1.2 consolidation. | ARB/CAB approval, source register update, companion references updated. |
| Phase 2 - Update templates | PR/MR, evidence pack, System Builder, Dynamic Workspace, MicroFunction, and AI agent templates include AVCI v3.2 fields. | Templates committed; sample PR/MR passes review. |
| Phase 3 - CI/CD enforcement | AVCI evidence schema, architecture fitness, policy, security, contract, and rollback checks are pipeline-visible. | CI reports show pass/fail evidence and waiver handling. |
| Phase 4 - Runtime evidence dashboards | Trace, log, metric, audit, policy, MicroFunction, AI, and workspace evidence are correlated. | Dashboards and trace reconstruction queries available. |
| Phase 5 - Continuous improvement | Auto-Heal/Learn/Improve candidates use governed proposal workflow. | Candidate loop generates proposals, tests, and approval records without silent mutation. |

## Minimum Acceptance Criteria

01A v1.2 is referenced as the canonical enterprise architecture and EDP authority.

AVCI v3.2 is used by PR/MR templates, evidence packs, System Builder intake, Dynamic Workspace governance, MicroFunction runtime, AI agent lifecycle, and DevSecOps promotion gates.

Every production-bound artifact includes owner, classification, verification evidence, policy evidence where applicable, rollback/compensation path, and improvement path.

Security, audit, classification, policy, and evidence telemetry cannot be disabled by ordinary runtime toggles.

Auto-Heal, Auto-Learn, and Auto-Improve remain proposal-driven unless a bounded, reversible, approved automation path exists with evidence and human accountability.

# 20. Open Reconciliation Items
| Item | Reason | Recommended Treatment |
| --- | --- | --- |
| 01A duplicate naming lineage | Pack 01 contained two 01A files with overlapping authority. | Close through 01A v1.2 and revision-control register update; demote reference-library content to companion/reference. |
| 11A duplicate numbering | Development Readiness and DevSecOps Governance both use 11A lineage in some packs. | Track in 00D / Revision Control Matrix and assign suffix hierarchy. |
| 41B / 44 System Builder overlap | System Builder appears in multiple numbering paths. | Preserve active governing source, identify superseded duplicates, and reconcile register. |
| Runtime telemetry toggle consistency | Several companion docs now require non-disableable security/audit/evidence signals. | Propagate exact toggle rule into observability, SRE, Dynamic Workspace, and runbooks. |
| External standards refresh cadence | NIST, OWASP, OpenTelemetry, and SLSA references evolve. | Update external alignment appendix quarterly or on material standard release. |

# 21. External Alignment Register
| Reference | AIRA v3.2 Alignment Use |
| --- | --- |
| NIST AI RMF / NIST AI 600-1 Generative AI Profile | AI risk governance, AI output trust, evaluation, human accountability, and model/agent risk handling. |
| NIST SSDF SP 800-218 | Secure software development practices, secure-by-design evidence, vulnerability remediation, and development lifecycle controls. |
| OWASP ASVS / OWASP GenAI and LLM guidance | Secure API/application verification, authenticated DAST, abuse cases, prompt/agent/tool risks, and secure-by-design controls. |
| OpenTelemetry Semantic Conventions | Trace, metric, log, model, agent, and runtime telemetry conventions for reconstruction and dashboards. |
| SLSA v1.2 | Supply-chain provenance, build integrity, artifact signing, attestations, and promotion evidence. |
| W3C WCAG 2.2 / WAI-ARIA | Dynamic Workspace accessibility, keyboard/screen-reader UX, safe widget states, and responsive design evidence. |

# 22. AVCI Compliance Summary for This Document
| AVCI Property | Evidence in This v3.2 Revision |
| --- | --- |
| Attributable | Identifies document ID, owner, co-owners, superseded source, canonical companion, review cadence, and evidence path. |
| Verifiable | Defines evidence schema, PR/MR template, CI/CD gates, security scans, policy checks, GitNexus, observability, trace reconstruction, and acceptance criteria. |
| Classifiable | Classifies the document as INTERNAL CONFIDENTIAL and requires classification for artifacts, telemetry, evidence, prompts, model routes, workspace components, and runtime data. |
| Improvable | Records roadmap, open reconciliation items, feedback loops, Auto-Heal/Learn/Improve boundaries, revision cadence, and companion-document propagation needs. |

End of Document

