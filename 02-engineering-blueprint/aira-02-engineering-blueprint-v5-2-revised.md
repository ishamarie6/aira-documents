---
title: "Engineering Blueprint"
doc_id: "AIRA-02"
version: "v5.2"
status: "revised"
category: "Engineering blueprint"
source_docx: "AIRA_02_Engineering_Blueprint_v5.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 02-engineering-blueprint
  - revised
  - aira-02
---



# Engineering Blueprint



AIRA
AI-Native Enterprise Platform
AI-Native Engineering Blueprint
Build-Ready System Specification for the Software Development Team
Version 5.2 Revised | June 2026 | INTERNAL CONFIDENTIAL

Mandatory Architecture Position

AIRA is not production-ready because source code compiles, a screen renders, or an AI assistant produces a plausible answer. AIRA is production-ready only when every service, Dynamic Workspace experience, MicroFunction transaction, API, event, database migration, AI route, prompt, policy, workflow, pipeline, runtime operation, and improvement candidate preserves architecture boundaries and produces AVCI-complete evidence. The blueprint is the build-ready architecture authority below consolidated Architecture Board decisions and above implementation playbooks.
| Property | Value |
| --- | --- |
| Document ID | AIRA-DOC-002 |
| Document Title | AIRA AI-Native Engineering Blueprint |
| Canonical Filename | 02-AIRA_Engineering_Blueprint_v5.2_Revised.docx |
| Version | v5.2 - Dynamic Workspace, MicroFunction, System Builder, AI Governance, DevSecOps Evidence, and Runtime Assurance Update |
| Supersedes | 02-AIRA_Engineering_Blueprint_v5.1_Aligned.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | DRAFT FOR ARCHITECTURE REVIEW BOARD / CAB APPROVAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; DevSecOps; Security Architecture; Software Development Lead; QA/SDET; Platform Engineering; AI Engineering; Data Governance; SRE / Operations; Internal Audit |
| Primary Governance Inputs | 01A v1.2; 01 AVCI v3.2; 01B v1.2; Dynamic Workspace 43/43A/53-61; MicroFunction 10/10A-10E; AI Governance 42D-42S; API 15/15A; Database/Flyway 16/16A/16B; Security 17/17A; DevSecOps 11/20; Change 30/30A |
| Review Cadence | Quarterly; unscheduled after material architecture, stack, AI, security, Dynamic Workspace, MicroFunction, workflow, data, evidence, or production-control change |

# 1. Executive Summary

This v5.2 revision updates the AIRA Engineering Blueprint after the canonical 01A v1.2 consolidation, the AVCI v3.2 revision, and the AVCI Evidence 01B v1.2 revision. It converts the platform vision into a build-ready architecture specification for developers, DevSecOps, security, QA/SDET, platform engineering, data governance, AI governance, and internal audit.

The blueprint binds Dynamic Workspace UX, MicroFunction backend/runtime assembly, System Builder, AI agents, OpenAPI/AsyncAPI contracts, Kafka/CloudEvents eventing, Flyway-governed data, DevSecOps evidence, observability, security controls, resilience, and progressive autonomy into one enforceable engineering model.
| Strategic Outcome | v5.2 Required Architecture Result |
| --- | --- |
| Build-ready architecture | Every module has bounded context ownership, contract-first APIs/events, MicroFunction transaction boundaries, ports/adapters, policy gates, tests, observability, rollback, and evidence. |
| Safe Dynamic Workspace | Frontend composition remains backend-governed, policy-filtered, MicroFunction-backed, accessible, observable, reversible, and evidence-producing. |
| Configuration-first delivery | MicroFunctions, templates, OPA, DMN/rules, seed configuration, and reusable steps are preferred before custom code. |
| AI without authority bypass | System Builder and agents may analyze, draft, generate candidates, and propose actions; promotion and protected execution remain governed by humans, OPA/SBAC, Harness, CI/CD, and CAB/ARB. |
| Operational reconstruction | Runtime behavior can be reconstructed from trace_id, request_id, actor, policy decision, MicroFunction run, event/outbox, audit record, evidence_ref, and dashboard evidence. |

# 2. Purpose, Scope, and Authority

## 2.1 Purpose

The purpose of this blueprint is to define the canonical architecture structure, control boundaries, integration patterns, runtime flows, data and event governance, AI execution boundary, Dynamic Workspace behavior, MicroFunction assembly model, evidence obligations, and acceptance gates that all AIRA implementation work must follow.

## 2.2 Scope

Backend services, frontend experiences, Dynamic Workspace templates, AI Assistant Panel, Admin Builder, Experience Blocks, Experience Packs, APIs, events, workflows, policies, data schemas, prompts, guardrails, agents, pipelines, observability, and evidence packs.

System Builder intakes for new requirements, operational evidence, improvement requests, AI agent lifecycle, and AI DevSecOps provisioning.

MicroFunction runtime assembly, standard steps, transaction configuration, policy decisions, outbox/event publishing, idempotency, rollback, and traceability.

DevSecOps promotion controls, CI/CD gates, GitNexus read-only impact analysis, security scans, SBOM/provenance, CAB/ARB approvals, and post-promotion monitoring.

## 2.3 Authority and Precedence
| Level | Authority | Blueprint Interpretation |
| --- | --- | --- |
| L0 | Architecture Board / Consolidated Architecture Decisions | Final authority for end-to-end platform boundaries, material exceptions, and unresolved conflicts. |
| L1 | 02 Engineering Blueprint v5.2 | Build-ready architecture authority for service boundaries, Dynamic Workspace, MicroFunctions, events, AI control paths, data, evidence, and runtime behavior. |
| L1 | 01A v1.2 / 01 v3.2 / 01B v1.2 | Universal design-principle, AVCI, evidence, audit, and traceability gates inherited by this blueprint. |
| L2 | Specialist standards | Developer Guide, Technology Stack, MicroFunction, API, Database, Security, DevSecOps, Observability, Dynamic Workspace, AI Governance, and Change standards implement this blueprint. |
| L3 | ADR/TDL, tickets, PR/MR, runbooks, evidence packs | Implementation records that must trace to this blueprint and may tighten but not weaken it. |

# 3. v5.2 Change Summary
| Change Area | v5.2 Architecture Update |
| --- | --- |
| 01A / AVCI alignment | Updates all design-principle and evidence references to canonical 01A v1.2, 01 v3.2, and 01B v1.2. |
| Dynamic Workspace | Promotes Dynamic Workspace as a governed experience architecture, not a frontend-only UI layer. |
| MicroFunction runtime | Defines MicroFunction Coordinator, standard step sequence, policy/evidence binding, outbox, DLQ/replay, and rollback as core runtime architecture. |
| System Builder / AI agents | Treats AI as proposal and candidate-generation capability only unless governed approval, SBAC, OPA, certification, trust, and rollback gates authorize a bounded action. |
| Contract and event architecture | Requires OpenAPI, AsyncAPI, Avro/JSON Schema, CloudEvents, Kafka, schema evolution, idempotent consumers, outbox, DLQ, and replay patterns. |
| Observability and evidence | Aligns with Log4j2, OpenTelemetry, Sentry, Loki, Tempo, Grafana, audit, runtime toggles, and non-disableable security/audit/evidence signals. |
| Security and resilience | Adds authenticated DAST, abuse cases, secure APIs, secrets hygiene, OPA/SBAC, heavy transaction, concurrency, Resilience Lab, and Auto-* candidate-loop controls. |

# 4. Architecture Control Model

Figure 1. Architecture work starts from controlled intake and ends with runtime assurance and governed improvement. No architecture path allows direct production mutation, direct model-provider calls, uncontrolled frontend authority, unmanaged database changes, or evidence-free promotion.

# 5. Enterprise Design Principles as Blueprint Invariants
| ID | Principle | Blueprint Invariant |
| --- | --- | --- |
| EDP-01 | SOLID | Services, agents, prompts, MicroFunctions, widgets, and adapters have single responsibility, explicit interfaces, and dependency inversion. |
| EDP-02 | Clean Architecture | Domain/use-case logic does not depend on UI, database, workflow engines, model providers, or tooling. |
| EDP-03 | DDD / Bounded Contexts | Contexts own language, APIs, events, schemas, invariants, policies, and runbooks. |
| EDP-04 | Ports and Adapters | All external systems, DBs, queues, model gateways, tools, and provisioning providers are accessed through ports/adapters. |
| EDP-05 | DRY, KISS, YAGNI | Reuse framework controls, standard steps, templates, and policies before adding custom code. |
| EDP-06 | Idempotency by Design | Retries, callbacks, replays, agent actions, and provisioning tasks must not duplicate effects. |
| EDP-07 | Determinism and Reproducibility | Builds, tests, migrations, prompts, environments, model routes, and evidence are reproducible from approved sources. |
| EDP-08 | Fail-Safe, Not Fail-Open | Missing identity, policy, guardrail, audit, evidence, or gateway controls blocks protected actions. |
| EDP-09 | Human-in-the-Loop | High-impact, low-confidence, Restricted, destructive, production, or exception actions require named human approval. |
| EDP-10 | Least Privilege / SBAC | Humans, services, System Builder, and agents receive only approved skills, tools, data, and environment scope. |
| ID | Principle | Blueprint Invariant |
| --- | --- | --- |
| EDP-11 | Separation of Duties | Maker, checker, approver, deployer, operator, agent owner, and auditor roles remain separable. |
| EDP-12 | Observability by Design | Critical paths emit safe traces, metrics, logs, audit, model, agent, provisioning, and evidence references. |
| EDP-13 | Policy as Code | Authorization, routing, guardrails, deployment, data handling, and tool rules are versioned policies. |
| EDP-14 | Testability by Design | Code, workflows, prompts, agents, adapters, policies, migrations, and manifests are testable with deterministic fixtures. |
| EDP-15 | Secure by Design | Threat controls, secrets hygiene, tenant isolation, classification handling, secure defaults, and supply-chain controls are built in. |
| EDP-16 | Resilience Patterns | Timeouts, retries, circuit breakers, bulkheads, fallback, DLQ, compensation, recovery, and rebuild are explicit. |
| EDP-17 | Architecture Fitness Functions | Automated checks verify boundaries, dependencies, contracts, security, agents, provisioning, and evidence. |
| EDP-18 | Progressive Autonomy | Automation advances only when evidence, trust, skill, risk, guardrails, and rollback controls support it. |
| EDP-19 | Reversibility / Rollbackability | Changes support rollback, forward-fix, compensation, feature disablement, environment rebuild, or safe deactivation. |
| EDP-20 | AVCI | Every artifact remains attributable, verifiable, classifiable, and improvable across its lifecycle. |

# 6. Logical Architecture Layers

Figure 2. AIRA separates experience, policy edge, application/use-case orchestration, domain logic, adapters, and evidence/operations. A lower layer may not depend on a higher layer. Domain logic must remain independent from UI frameworks, database details, model providers, workflow engines, and tooling.
| Layer | Owns | Must Not Own |
| --- | --- | --- |
| Experience Layer | Dynamic Workspace rendering, component states, accessibility, layout, user interaction, AI Panel inputs/outputs, safe messages. | Business authority, authorization decisions, direct DB writes, direct model/tool execution, secrets. |
| API and Policy Edge | OpenAPI contracts, input validation, idempotency keys, OPA/SBAC decisions, safe error envelopes, gateway policies. | Domain invariants hidden in controllers, hardcoded role logic, direct workflow or persistence coupling. |
| Application / Use Case | MicroFunction coordination, transaction boundaries, workflow orchestration, approvals, audit hooks, outbox coordination. | Framework-specific UI concerns, provider SDK calls, cross-context data ownership violations. |
| Domain Layer | Bounded-context language, aggregates, invariants, business rules, domain services, events. | Controller code, SQL, Kafka clients, Redis clients, model gateways, UI behavior. |
| Ports / Adapters | PostgreSQL, Kafka, Redis/Valkey, Keycloak, LiteLLM, OPA, OpenKM/MinIO, Flowable/Temporal integrations. | Business rule ownership or policy bypass. |
| Evidence and Operations | CI/CD, GitNexus, telemetry, audit, evidence store, incidents, RCA, dashboards, runbooks. | Silent mutation or becoming source of business truth unless designated as authoritative record. |

# 7. Dynamic Workspace and Frontend Architecture

The Dynamic Workspace is an enterprise experience layer governed by backend policy, configuration, MicroFunction capability bindings, API contracts, accessibility rules, observability, and evidence. It is not allowed to become a business-rule engine or authorization authority.
| Architecture Rule | Required Treatment |
| --- | --- |
| Backend-governed composition | Workspace, screen, template, component, and action eligibility are resolved from approved configuration, policy decisions, and role/skill/classification context. |
| Policy-filtered UI | OPA/SBAC may allow, deny, filter, mask, require approval, or require step-up. Frontend must render safe states without revealing hidden capabilities. |
| MicroFunction-backed action | Every state-changing widget action binds to a backend MicroFunction transaction or approved workflow signal with idempotency, audit, evidence, and rollback. |
| Accessible and responsive by design | WCAG-aligned keyboard, focus, screen-reader, contrast, motion, error, responsive, and alternate interaction rules are acceptance gates. |
| AI Panel boundary | AI assists with summarization, recommendations, artifact drafting, and candidate actions. It does not approve, authorize, or execute protected business actions. |
| Runtime toggles | Performance-oriented diagnostic toggles may reduce nonessential telemetry, but security, audit, classification, policy, evidence, and incident signals are non-disableable. |

# 8. MicroFunction Runtime Architecture

AIRA uses configuration-first MicroFunction assembly before custom code. Each MicroFunction is small, single-purpose, testable, observable, reversible, and dependency-inverted. The runtime sequence is explicitly governed by standard steps and evidence gates.
| Runtime Concern | Blueprint Requirement |
| --- | --- |
| Standard steps | Receive, correlate, resolve actor/tenant, rate limit, classify, authorize, validate, execute, persist, publish, audit, observe, respond, and record evidence. |
| Transaction boundary | Use-case orchestration owns transaction boundaries; domain logic owns invariants; adapters own external integration mechanics. |
| Idempotency | Mutating requests require idempotency keys, replay guards, deduplication, and duplicate-safe event consumers. |
| Outbox and events | Database state changes and event publication use transactional outbox and CloudEvents-compatible metadata. |
| DLQ and replay | Kafka consumers require schema-aware replay, DLQ handling, poison-message control, and audit evidence. |
| Rollback and compensation | Every mutating transaction declares rollback, forward-fix, compensation, feature-disablement, or safe-deactivation strategy. |

# 9. API, Event, Workflow, and Database Architecture
| Domain | Mandatory Architecture Controls |
| --- | --- |
| OpenAPI | Contract-first REST APIs with versioning, safe errors, pagination, correlation, idempotency, OPA/SBAC inputs, examples, tests, and generated clients where appropriate. |
| AsyncAPI / Kafka | Topic contracts, producer/consumer ownership, CloudEvents envelope, Avro/JSON Schema, compatibility checks, idempotent consumers, DLQ, replay, and schema evolution. |
| CloudEvents | Every material event carries source, type, subject, id, time, correlation_id, causation_id, traceparent, classification, schema_ref, and evidence_ref where applicable. |
| Workflows | Temporal/Flowable/DMN workflows remain orchestration adapters; domain decisions and policy authority stay outside workflow engine internals. |
| Database / Flyway | PostgreSQL is authoritative for system data where designated. Flyway governs schemas, seed data, indexes, RLS, views, reference data, and data-change evidence from Day 0. |
| Redis/Valkey | Cache and acceleration only. It must never become authoritative truth and must support invalidation, rebuild, stale-state handling, and evidence. |

# 10. AI Governance, System Builder, and Agent Architecture Boundary

AI is an accelerator and proposal mechanism, not authority. The System Builder may intake, analyze, recommend, draft, generate candidates, prepare tests, create evidence summaries, and prepare PR/MR-ready artifacts. It must not approve its own output, silently mutate runtime behavior, bypass SBAC/OPA, call model providers directly, or alter production directly.
| AI / System Builder Capability | Allowed Architecture Position | Reject / Escalate Condition |
| --- | --- | --- |
| New requirements | Normalize into controlled intake, impact analysis, contracts, acceptance criteria, and draft artifacts. | Reject if source, owner, classification, bounded context, or approval path is missing. |
| Operational evidence | Analyze logs, traces, metrics, test results, scans, screenshots, incidents, and feedback as classified diagnostic input. | Escalate if evidence contains secrets/PII, lacks provenance, or implies direct production mutation. |
| Improvement requests | Generate Auto-Heal, Auto-Learn, Auto-Improve candidates, tests, PRs, knowledge updates, or runbook drafts. | Block self-modification, self-promotion, policy weakening, or unreviewed production change. |
| AI agent lifecycle | Draft agent purpose, skills, SBAC, tools, route, guardrails, tests, monitoring, suspension, and retirement records. | Block uncontrolled agents, direct credentials, direct Git/CI/DB/K8s access, or excessive skills. |
| AI DevSecOps provisioning | Prepare IaC/toolchain/devcontainer/pipeline proposals through Golden Source and evidence gates. | Block click-ops, unapproved technologies, direct secrets, and drift outside Git/IaC/CI evidence. |

# 11. DevSecOps, GitNexus, Evidence, and Promotion Architecture
| Gate | Required Evidence |
| --- | --- |
| Controlled intake | Ticket/intake ID, source, owner, classification, affected bounded context, risk tier, acceptance criteria, approval path. |
| Design gate | Architecture impact, ADR/TDL or waiver, threat/abuse case, API/event/schema/policy plan, rollback/compensation plan. |
| Build gate | Branch, commits, CODEOWNERS, AI-use record, generated artifact provenance, secrets hygiene, dependency source, SBOM. |
| Verification gate | Unit/component/contract tests, OPA/Rego tests, architecture fitness, SAST, SCA, authenticated DAST, accessibility, Playwright, mutation where applicable. |
| GitNexus gate | Read-only code map, impact analysis, affected tests/contracts, architecture drift signal, security-sensitive code map, PR/MR evidence summary. |
| Promotion gate | PR/MR AVCI summary, maker-checker review, CAB/ARB where required, CI evidence pack, rollback/forward-fix readiness, post-promotion monitoring. |

# 12. Observability, Audit, and Runtime Assurance

AIRA runtime behavior must be explainable, supportable, reconstructable, and improvable. Observability is built into design and cannot be retrofitted after production. Security, audit, policy, classification, and evidence telemetry cannot be disabled through runtime tuning.
| Signal | Architecture Requirement |
| --- | --- |
| Logs | Structured Log4j2 logs with correlation, classification, redaction, safe error codes, no secrets, no raw tokens, no unnecessary PII. |
| Traces | OpenTelemetry spans across frontend, gateway, API, policy, MicroFunction, adapters, Kafka, AI gateway, and workflow steps. |
| Metrics | SLI/SLO, latency, error rate, saturation, policy deny, DLQ, replay, cache, workflow, AI route, guardrail, and evidence completeness metrics. |
| Errors | Sentry or approved error-monitoring event with redacted context, release, environment, trace_id, owner, and remediation link. |
| Dashboards | Grafana dashboards for service health, workspace health, policy denials, action performance, AI usage, pipeline evidence, and evidence gaps. |
| Trace reconstruction | Given a user action, artifact, event, incident, or PR/MR, reviewers must reconstruct source, actor, policy, execution, evidence, outcome, rollback, and improvement path. |

# 13. Security, Access, Data, and Resilience Architecture
| Control Area | Blueprint Rule |
| --- | --- |
| Identity and access | Keycloak/enterprise identity, service identity, workload identity, RBAC/ABAC/SBAC, least privilege, separation of duties, recertification, and fail-closed checks. |
| Policy as code | OPA/Rego or approved policy abstraction governs authorization, routing, classification, tool action, deployment, data handling, and approval rules. |
| Secrets hygiene | No secrets in code, prompts, screenshots, logs, traces, docs, tests, or AI context. Use Vault-compatible abstractions and approved secret references. |
| Secure APIs | ASVS-aligned input validation, authn/authz, session controls, CSRF/CORS, rate limiting, safe errors, authenticated DAST, API abuse cases, and remediation evidence. |
| Data classification | Data, evidence, prompts, embeddings, artifacts, logs, traces, and caches carry classification and retention handling. |
| Heavy transaction and concurrency | Optimistic/pessimistic controls, retry-safe operations, duplicate-safe consumers, throttling, async job handling, bulkheads, circuit breakers, and Resilience Lab evidence. |

# 14. Architecture Fitness Functions
| Fitness Function | Example Check |
| --- | --- |
| Boundary enforcement | ArchUnit/Semgrep rules block controller-to-database, domain-to-framework, frontend-to-business-authority, direct provider SDK, and cross-context writes. |
| Contract compatibility | OpenAPI/AsyncAPI/schema checks block breaking changes without versioning, migration, compatibility, and consumer evidence. |
| Policy and security | OPA tests, ASVS controls, authenticated DAST, SAST/SCA/secrets scans, SBAC checks, and model-route guardrail tests. |
| MicroFunction integrity | Required steps, idempotency, classification, audit, outbox, evidence, rollback, and error policy must be present for mutating flows. |
| Observability completeness | Critical flows must emit trace, metric, log, audit, policy, evidence, and dashboard signals with forbidden fields blocked. |
| Evidence completeness | PR/MR evidence must include owner, source, classification, tests, scans, policy, GitNexus, rollback, approval, and improvement path. |

# 15. RACI
| Activity | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Architecture blueprint ownership | Enterprise Architecture | Solutions Architecture Office / IT Head | Security, DevSecOps, Platform, QA, Data Governance | Development teams, Internal Audit |
| MicroFunction runtime design | Software Development Lead | Enterprise Architecture | Security, DBA, QA, SRE | Product owners |
| Dynamic Workspace architecture | Frontend Lead + Backend Lead | Enterprise Architecture | Accessibility, Security, UX, Product Owner | Business users |
| API/event/data contracts | API/Data Architecture | Enterprise Architecture | DBA, DevSecOps, QA, Integration owners | Consumers |
| AI/System Builder controls | AI Governance + Platform Engineering | Architecture Board / Security Governance | DevSecOps, Security, Internal Audit | Developers |
| Promotion and production readiness | DevSecOps Lead | CAB / ARB | Security, QA, SRE, Product Owner | Operations and Audit |

# 16. Implementation Roadmap
| Phase | Priority | Architecture Deliverable | Exit Evidence |
| --- | --- | --- | --- |
| Phase 1 | Immediate | Adopt 01A v1.2, 01 v3.2, 01B v1.2, and this Blueprint v5.2 as foundation. | Approved source register, Obsidian projection, team notice, PR/MR template update. |
| Phase 2 | High | Update Developer Guide, Technology Stack, Information Nervous System, CLAUDE.md, Skills Framework. | Aligned documents, repository rules, CI checks, training acknowledgement. |
| Phase 3 | High | Propagate blueprint controls into MicroFunction, Dynamic Workspace, API/event, security, database, and DevSecOps templates. | Contract templates, policy tests, seed data, fitness functions, evidence pack. |
| Phase 4 | Medium | Run Resilience Lab and authenticated DAST for Dynamic Workspace and MicroFunction flows. | Test reports, remediation records, dashboard evidence, acceptance summary. |
| Phase 5 | Ongoing | Use runtime evidence, incidents, GitNexus, and Auto-* candidates to improve architecture under governance. | Backlog, RCA, ADR/TDL updates, approved supersedence records. |

# 17. Acceptance Criteria

All implementation work identifies owner, source, bounded context, classification, contracts, test path, policy path, evidence path, and rollback path.

Dynamic Workspace outputs are backend-governed, policy-filtered, accessible, observable, reversible, and MicroFunction-backed for material actions.

MicroFunction transactions prove idempotency, audit, outbox/event publication, DLQ/replay, safe errors, observability, and evidence.

System Builder and AI agents remain proposal-driven unless explicit approval, trust, SBAC, OPA, Harness, and rollback controls authorize bounded action.

All APIs/events/database changes are contract-first, schema-governed, versioned, tested, and promoted through CI/CD and evidence packs.

Security, audit, policy, classification, and evidence signals cannot be disabled by runtime telemetry toggles.

Auto-Heal, Auto-Learn, and Auto-Improve produce candidates, tests, PRs, knowledge drafts, or runbooks only; they do not self-promote production behavior.

# 18. Open Reconciliation Items
| Item | Severity | Recommended Resolution |
| --- | --- | --- |
| 01A duplicate authority | Resolved by 01A v1.2; keep reference-library material as companion, not authority. | Record in Revision Control Matrix v1.3 and 00D register. |
| Runtime telemetry toggle propagation | Medium | Propagate non-disableable signal rule into SRE, Observability, Dynamic Workspace, and operations runbooks. |
| Heavy transaction / Resilience Lab templates | Medium | Add explicit tests and CI evidence requirements to MicroFunction, API, and DevSecOps templates. |
| OpenAPI/AsyncAPI replay matrix | Medium | Add to System Builder proposal and contract-generation templates. |
| Dynamic Workspace 53, 56, 57 pending review | Medium | Process remaining Dynamic Workspace companion files before closing Pack 15 family. |

# 19. External Alignment Register
| Reference | Blueprint Alignment Use |
| --- | --- |
| NIST AI RMF / NIST AI 600-1 | AI risk governance, human accountability, trustworthy AI controls, evaluation, and monitoring. |
| NIST SSDF SP 800-218 | Secure software development, CI/CD evidence, vulnerability mitigation, provenance, and developer workflow controls. |
| OWASP ASVS / OWASP LLM and GenAI guidance | Secure APIs, authenticated testing, abuse cases, session/access controls, model/prompt/tool risk controls. |
| OpenTelemetry Semantic Conventions | Trace, metric, log, model/agent, and runtime correlation model. |
| SLSA v1.2 | Software supply-chain provenance, build integrity, attestations, and promotion evidence. |
| W3C WCAG 2.2 / WAI-ARIA APG | Accessibility and inclusive Dynamic Workspace UX acceptance gates. |

# 20. AVCI Compliance Summary
| AVCI Property | How v5.2 Satisfies It |
| --- | --- |
| Attributable | Defines document ownership, architecture authority, RACI, source hierarchy, bounded-context ownership, actor/service/agent identity, PR/MR ownership, and approval responsibilities. |
| Verifiable | Requires contracts, tests, architecture fitness, policy checks, security scans, GitNexus, SBOM/provenance, telemetry, audit, dashboards, and acceptance evidence. |
| Classifiable | Applies classification to data, prompts, artifacts, evidence, logs, traces, events, AI context, Dynamic Workspace outputs, and retention decisions. |
| Improvable | Defines Auto-* candidate loops, RCA, backlog, ADR/TDL, supersedence, runtime metrics, dashboard feedback, and revision-control reconciliation paths. |

Final Control Position

AIRA shall be built as a governed, evidence-producing, AI-native enterprise platform. The blueprint rejects architecture drift, uncontrolled automation, frontend business authority, direct model-provider calls, unmanaged production mutation, manual database truth, and evidence-free promotion. Discipline first. Automation second. Intelligence third. AVCI always.

