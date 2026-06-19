---
title: "Developer Guide"
doc_id: "AIRA-03"
version: "v4.2"
status: "revised"
category: "Developer guide"
source_docx: "AIRA_03_Developer_Guide_v4.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 03-developer-guide
  - revised
  - aira-03
---



# Developer Guide



AIRA
AI-Native Enterprise Platform

Developer Guide

Implementation Patterns | Coding Standards | SOLID Enforcement | AI-Native Guardrails | Operational Procedures

Version v4.2 - Canonical Governance, Dynamic Workspace, MicroFunction, DevSecOps, and Evidence Alignment Update
| Property | Value |
| --- | --- |
| Document ID | AIRA-DOC-003 |
| Canonical Filename | 03-AIRA_Developer_Guide_v4.2_Revised.docx |
| Version | v4.2 - Revised and aligned after 01A v1.2, 01 v3.2, 01B v1.2, and 02 v5.2 |
| Supersedes | 03-AIRA_Developer_Guide_v4.1_Aligned.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | DRAFT FOR ARCHITECTURE REVIEW BOARD / CAB APPROVAL AND DEVELOPER ADOPTION |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; Platform Engineering; AI Engineering; DBA; SRE / Operations; Internal Audit |
| Primary Audience | Software Developers, Frontend Developers, Backend Developers, QA/SDET, DevSecOps, Security, DBA, AI-assisted coding operators, reviewers, and technical leads |
| Review Cadence | Quarterly; unscheduled on material architecture, technology stack, AI governance, Dynamic Workspace, MicroFunction, DevSecOps, security, observability, or evidence change |
| Evidence Path | OpenKM Tier-0 / AIRA / Engineering / Developer-Guide / v4.2/ |

# Mandatory Practice Statement

AIRA developer output is not complete when source code compiles or a screen appears to work. It is complete only when the code, configuration, contracts, migrations, policies, tests, observability signals, evidence records, rollback path, and PR/MR review prove AVCI, EDP-01 through EDP-20, SOLID, Clean Architecture, DDD, ports-and-adapters, secure-by-design, testability, observability, reversibility, and human accountability.

Discipline first. Automation second. Intelligence third. AVCI always.

# Static Table of Contents

1. Executive Summary

2. Purpose, Scope, and Authority

3. v4.2 Change Summary

4. Developer Operating Model

5. Enterprise Design Principles for Developers

6. Backend, Frontend, Dynamic Workspace, and MicroFunction Rules

7. Contract, Data, Event, and Workflow Implementation Rules

8. Security, AI, and Secrets Hygiene Rules

9. DevSecOps, GitNexus, CI/CD, and Evidence Pack Rules

10. Observability, Runtime Toggles, and Trace Reconstruction

11. Concurrency, Heavy Transaction, Resilience, and Auto-* Candidate Loops

12. PR/MR Evidence Template

13. RACI, Roadmap, Acceptance Criteria, and Open Reconciliation Items

14. External Alignment Register

15. AVCI Compliance Summary

# 1. Executive Summary

This v4.2 revision updates the AIRA Developer Guide as the execution standard for human developers and approved AI-assisted coding workflows. It translates the revised architecture and AVCI foundation into practical rules for implementing backend services, frontend components, Dynamic Workspace configurations, MicroFunction transactions, API/event contracts, database migrations, policies, tests, observability, and PR/MR evidence.

The guide remains implementation-oriented. It tells developers how to work inside the AIRA architecture without turning coding speed into architecture drift, uncontrolled automation, security bypass, or unverifiable artifacts. It is subordinate to the canonical 01A architecture principles, 01 AVCI, 01B evidence controls, and 02 Engineering Blueprint, but it is the primary developer-facing operating manual for daily engineering work.
| Strategic Developer Outcome | v4.2 Required Treatment |
| --- | --- |
| Governed speed | Developers and AI tools may accelerate drafting and test generation, but every output remains source-controlled, reviewed, tested, classified, and evidence-producing. |
| Architecture preservation | Code must preserve SOLID, Clean Architecture, DDD, ports/adapters, MicroFunction boundaries, Dynamic Workspace backend authority, and EDP-01 through EDP-20. |
| Safe integration | REST, events, schemas, workflows, outbox, DLQ, replay, and data changes are contract-first and migration-governed. |
| Evidence by construction | Every PR/MR contains tests, scans, GitNexus impact, policy decisions, observability references, rollback plan, and AVCI summary. |
| Human accountability | AI recommendations and generated artifacts remain draft until accepted by named reviewers under maker-checker and CODEOWNERS gates. |

# 2. Purpose, Scope, and Authority

## 2.1 Purpose

Define the mandatory developer practices for implementing AIRA changes in a repeatable, secure, testable, observable, reversible, and evidence-producing manner. The guide converts architecture standards into day-to-day execution rules for code, configuration, prompts, policies, schemas, migrations, UI, APIs, events, workflows, and operational runbooks.

## 2.2 Scope

Backend services, MicroFunction engine code, standard functions, adapters, workflows, and integration components.

Frontend applications, Dynamic Workspace components, widgets, templates, AI Assistant Panel surfaces, accessibility, and responsive UX.

OpenAPI, AsyncAPI, Kafka, Avro/JSON Schema, CloudEvents, idempotent consumers, outbox, DLQ, replay, schema evolution, and compatibility tests.

PostgreSQL/Flyway migrations, seed data, RLS, indexes, evidence tables, and Redis/Valkey derivative cache usage.

AI-assisted development, prompts, model-route usage, guardrails, AI evidence, and agent-safe action boundaries.

DevSecOps pipelines, GitNexus impact analysis, CI/CD evidence, security scans, SBOM/provenance, release readiness, and rollback proof.

## 2.3 Out of Scope

Autonomous production mutation by developers, agents, scripts, or tools.

Direct model-provider SDK calls from application code or developer scripts.

Manual production database edits, click-ops runtime configuration, or uncontrolled secrets handling.

Unreviewed AI-generated code, prompts, migrations, policies, or documentation treated as approved authority.

## 2.4 Authority and Precedence
| Level | Authority | Developer Interpretation |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance | Final authority for production-impacting developer exceptions, waivers, and promotion decisions. |
| L1 | 01A v1.2, 01 v3.2, 01B v1.2, 02 v5.2 | Non-negotiable architecture, AVCI, evidence, and blueprint controls. |
| L2 | This Developer Guide v4.2 | Primary daily execution standard for developers and AI-assisted coding operators. |
| L3 | Specialist standards: MicroFunction, API, Database/Flyway, Security, DevSecOps, Observability, Dynamic Workspace | Detailed implementation controls that must not be weakened by this guide. |
| L4 | Tickets, ADR/TDL, PR/MR, tests, pipeline evidence, runtime evidence | Implementation proof and operational trace. |

Conflict Rule: where standards appear inconsistent, developers must follow the stricter control, stop if production or Restricted impact exists, record the issue as an AVCI reconciliation item, and route the decision through the appropriate owner, ARB, CAB, or Security Governance path.

# 3. v4.2 Change Summary
| Change Area | Developer-Visible Improvement |
| --- | --- |
| Canonical governance alignment | References updated to 01A v1.2, 01 v3.2, 01B v1.2, and 02 v5.2. |
| Dynamic Workspace | Adds rules for widget states, template binding, backend authority, policy filtering, accessibility, and evidence. |
| MicroFunction runtime | Clarifies configuration-first delivery, reusable steps, ports/adapters, outbox, idempotency, DLQ/replay, rollback, and runtime evidence. |
| Contract-first development | Requires OpenAPI/AsyncAPI/schema work before implementation where boundaries are crossed. |
| DevSecOps evidence | Strengthens PR/MR evidence, GitNexus impact, security gates, SBOM/provenance, and promotion gates. |
| AI-safe coding | No direct provider SDK calls; all AI model access through LiteLLM or approved gateways with guardrails and audit. |
| Observability | Adds Log4j2, OpenTelemetry, Sentry, Loki, Tempo, Grafana, trace reconstruction, and runtime toggle controls. |
| Security expansion | Adds OPA/SBAC, abuse cases, authenticated DAST, secrets hygiene, secure APIs, and remediation evidence. |
| Heavy transaction readiness | Adds concurrency, retry, replay, outbox, idempotency, and Resilience Lab developer obligations. |
| Continuous improvement | Auto-Heal, Auto-Learn, and Auto-Improve may propose candidates only; no silent mutation or self-promotion. |

# 4. Developer Operating Model

## 4.1 Standard Developer Flow

Read the controlling ticket, requirement, evidence item, ADR/TDL, or approved System Builder proposal.

Confirm bounded context, owner, classification, security level, affected contracts, schemas, APIs, events, MicroFunctions, policies, and Dynamic Workspace artifacts.

Draft or update contract/schema/configuration first when a boundary is crossed.

Implement using approved technology, Java 25 backend baseline, React/Next.js frontend baseline, ports/adapters, and thin controllers.

Run local checks before PR: formatting, unit tests, component tests, contract tests, policy tests, security checks, architecture fitness checks, and accessibility checks where applicable.

Create PR/MR with AVCI evidence, GitNexus impact, AI-use declaration, test results, scan results, rollback/forward-fix path, and known limitations.

Do not merge, deploy, activate, or promote without required CODEOWNERS, maker-checker, ARB/CAB, DBA, or Security approvals.

## 4.2 Developer Rejection Rules

Reject code that compiles but bypasses architecture boundaries, OPA/SBAC, audit, outbox, idempotency, classification, or tests.

Reject frontend logic that becomes business authority or security authority.

Reject hidden role checks, hardcoded permissions, direct database writes across bounded contexts, or direct calls to provider SDKs.

Reject runtime telemetry toggles that disable security, audit, policy, classification, or evidence signals.

Reject AI-generated artifacts that lack traceable prompt/source, human review, deterministic tests, and rollback path.

# 5. Enterprise Design Principles for Developers
| EDP | Developer Rule |
| --- | --- |
| EDP-01 SOLID | Keep classes, functions, prompts, components, and MicroFunctions single-purpose, interface-driven, extensible, substitutable, and dependency-inverted. |
| EDP-02 Clean Architecture | Domain and use-case logic must not depend on UI, database, queue, model provider, workflow engine, or framework transport types. |
| EDP-03 DDD / Bounded Contexts | Implement within the owning bounded context and do not write across another context boundary without approved API/event contract. |
| EDP-04 Ports and Adapters | Access databases, Kafka, OPA, Keycloak, LiteLLM, OpenKM, Redis, tools, and workflows through explicit ports/adapters. |
| EDP-05 DRY/KISS/YAGNI | Reuse standard MicroFunction steps and templates; avoid speculative abstractions and duplicated plumbing. |
| EDP-06 Idempotency | Mutating APIs, callbacks, event consumers, workflows, and tool actions must be retry-safe and duplicate-safe. |
| EDP-07 Determinism | Builds, migrations, tests, prompts, agent/tool routes, and evidence must be reproducible from approved source. |
| EDP-08 Fail-Safe | Missing identity, policy, guardrail, audit, evidence, or secrets control stops protected behavior. |
| EDP-09 Human-in-the-Loop | High-impact, low-confidence, Restricted, destructive, production-impacting, or policy-exception changes require named approval. |
| EDP-10 Least Privilege / SBAC | Grant only required skills, scopes, tools, data, and environment access. |
| EDP-11 Separation of Duties | Maker, checker, approver, deployer, operator, owner, and auditor roles remain separated for high-risk work. |
| EDP-12 Observability | Emit safe traces, metrics, logs, audit, model, agent, event, and evidence references. |
| EDP-13 Policy as Code | Authorization, routing, guardrail, data handling, deployment, and tool rules are versioned policies. |
| EDP-14 Testability | Every artifact must be independently testable with deterministic fixtures and CI evidence. |
| EDP-15 Secure by Design | Use secure defaults, validation, classification, tenant isolation, secrets hygiene, and supply-chain controls. |
| EDP-16 Resilience | Use timeouts, retries, circuit breakers, bulkheads, fallback, DLQ, replay, compensation, and recovery. |
| EDP-17 Fitness Functions | CI validates boundaries, dependencies, contracts, policies, evidence, and security rules continuously. |
| EDP-18 Progressive Autonomy | Automation progresses only with trust, evidence, guardrails, rollback, and human approval. |
| EDP-19 Reversibility | Support rollback, forward-fix, compensation, feature disablement, safe deactivation, or rebuild. |
| EDP-20 AVCI | Every output is attributable, verifiable, classifiable, and improvable. |

# 6. Backend, Frontend, Dynamic Workspace, and MicroFunction Rules

## 6.1 Backend Implementation Rules

Java 25 LTS is the default backend runtime. Java 21 is waiver-only with owner, reason, risk, compensating controls, exit date, and CAB/ARB approval.

Use Spring Boot and framework code only as outer adapters. Domain and use-case logic remain framework-independent.

Controllers are thin. They receive, validate transport concerns, delegate to application services/MicroFunction coordinator, and return safe responses.

No direct SQL or database client calls in domain logic. Persistence is through ports/adapters and Flyway-governed schemas.

No direct Kafka, Redis, OpenKM, OPA, Keycloak, LiteLLM, provider SDK, or workflow engine calls from domain logic.

## 6.2 Frontend and Dynamic Workspace Rules

Frontend components render governed data and request approved capabilities; they do not own business authority or security authority.

Dynamic Workspace layouts, widgets, templates, and AI Panel experiences are backend-governed, policy-filtered, evidence-producing, accessible, and reversible.

All UI actions that mutate state must call approved APIs or MicroFunction-backed action endpoints with idempotency keys and trace propagation.

Widget states must include loading, empty, denied, disabled, stale, partial, requires approval, success, error, degraded, and offline where applicable.

Accessibility, responsive behavior, keyboard support, screen-reader support, focus management, and safe error states are required for merge readiness.

## 6.3 MicroFunction Development Rules

Prefer configuration-first assembly and reusable standard steps before custom code.

Business MicroFunctions must be small, reusable, single-responsibility, dependency-inverted, observable, testable, idempotent where mutating, and reversible.

Runtime configuration, transaction definitions, step catalogs, activation rows, templates, and seed data are engineering artifacts subject to Git, Flyway, CI/CD, classification, review, and evidence controls.

No MicroFunction may remove identity, classification, authorization, validation, idempotency, error handling, audit, observability, rollback, or evidence steps without approved waiver.

# 7. Contract, Data, Event, and Workflow Implementation Rules
| Area | Developer Requirement |
| --- | --- |
| OpenAPI | Define or update API contracts before implementation; include authentication, authorization, classification, error model, idempotency, pagination, correlation, and examples. |
| AsyncAPI / Kafka | Define topics, producers, consumers, event purpose, CloudEvents envelope, schema reference, retry, DLQ, replay, ordering, and consumer idempotency. |
| Avro / JSON Schema | Version schemas, validate compatibility, record ownership and classification, and avoid unsafe breaking changes without migration plan. |
| CloudEvents | Use standard metadata for event identity, source, type, subject, time, trace/correlation, causation, classification, and schema reference. |
| Outbox | State-changing transactions that publish events use transactional outbox or approved equivalent; direct publish after DB commit is not acceptable for critical flows. |
| DLQ / Replay | Consumers must define DLQ handling, replay authorization, idempotency, duplicate detection, and evidence linkage. |
| Flyway | All database changes, seed data, RLS, indexes, extensions, evidence tables, and schema evolution use Flyway or approved migration workflow only. |
| Workflow | Flowable/Temporal workflows are invoked through ports/adapters, emit audit/evidence, support human approval, and define compensation or safe stop behavior. |

# 8. Security, AI, and Secrets Hygiene Rules

## 8.1 Security and OPA/SBAC

Use RBAC/ABAC/SBAC inputs and OPA/Rego or approved policy abstraction for protected decisions.

Policy decisions must capture subject, action, resource, classification, tenant, skill, policy version, decision result, trace_id, and evidence reference.

Unauthorized, wrong-tenant, expired, insufficient-skill, missing-policy, or failed-guardrail requests fail closed with safe responses.

Abuse cases are required for authentication, authorization, API, workflow, Dynamic Workspace, AI Panel, file upload, replay, and admin-builder flows.

## 8.2 AI-Assisted Development and Runtime AI

Declare AI tool usage in PR/MR evidence: tool, prompt/source, artifact type, reviewer, and accepted/rejected changes.

Application code, scripts, notebooks, services, and agents must not call model-provider SDKs directly. Use LiteLLM or approved private/on-prem gateways.

NeMo Guardrails or approved guardrail checkpoints apply to input, retrieval, execution, and output where AI is used.

AI may recommend, draft, test, summarize, and propose. It may not approve its own output, bypass policy, mutate production, or receive direct Git/CI/CD/Kubernetes/database/production credentials.

## 8.3 Secrets Hygiene and Data Handling

Never place secrets, passwords, raw tokens, raw JWTs, private keys, production customer data, or Restricted documents in Git, prompts, tests, logs, traces, screenshots, fixtures, or embeddings.

Use Vault or approved secrets manager references. Local development adapters must be safe, synthetic, and clearly non-production.

Logs, traces, metrics, prompts, generated artifacts, and evidence must follow classification, redaction, retention, and access-control rules.

# 9. DevSecOps, GitNexus, CI/CD, and Evidence Pack Rules

## 9.1 Required Developer Gates
| Gate | Required Evidence |
| --- | --- |
| Local readiness | Build passes; unit tests pass; formatting/lint pass; no secrets detected; local run instructions updated. |
| Contract readiness | OpenAPI/AsyncAPI/schema lint, compatibility, mock, generated client, and contract tests where applicable. |
| Quality readiness | Unit, component, integration, regression, mutation or equivalent quality signal, architecture fitness, and deterministic fixtures. |
| Security readiness | SAST, SCA, secret scan, dependency review, authenticated DAST where relevant, abuse-case tests, and remediation evidence. |
| GitNexus readiness | Read-only impact analysis, affected files, dependency graph, affected tests, risk summary, and architecture drift findings. |
| Supply chain readiness | SBOM, artifact digest, build image digest, provenance or attestation, toolchain versions, and CI run ID. |
| Promotion readiness | PR/MR AVCI summary, reviewers, approvals, rollback/forward-fix/compensation plan, monitoring plan, and known limitations. |

## 9.2 GitNexus Boundary

GitNexus is read-only, derivative, commit-bound code intelligence. Developers may use it to understand impact, dependencies, call chains, affected tests, and architecture drift, but it cannot commit, approve, merge, deploy, mutate production, replace tests/scans, or replace human review.

# 10. Observability, Runtime Toggles, and Trace Reconstruction

Developers must build observability as part of the feature, not as an afterthought. Critical paths must emit structured logs, traces, metrics, audit events, evidence references, and safe error information sufficient to reconstruct who did what, when, why, under which policy, with what outcome, and with which rollback or improvement path.
| Signal | Developer Rule |
| --- | --- |
| Log4j2 / Structured Logs | Use structured, redacted diagnostic logs. No secrets, raw PII, raw prompts, raw documents, tokens, or high-cardinality metric labels. |
| OpenTelemetry | Propagate trace_id, span_id, request_id, correlation_id, causation_id, tenant context where safe, service/version, route/topic, and dependency span. |
| Sentry | Capture frontend/backend exceptions with release, environment, component, trace, safe breadcrumbs, and no sensitive payloads. |
| Loki / Tempo / Grafana | Ensure logs, traces, and dashboards can link PR/MR, release, runtime behavior, audit, and evidence records. |
| Runtime toggles | Performance-sensitive diagnostic verbosity may be toggled, but security, audit, policy, classification, evidence, trace correlation, and error-monitoring signals are non-disableable. |
| Trace reconstruction | Critical flows must reconstruct API call, policy decision, MicroFunction steps, DB/outbox, event, consumer, workflow, AI call where applicable, and user-visible result. |

# 11. Concurrency, Heavy Transaction, Resilience, and Auto-* Candidate Loops

## 11.1 Concurrency and Heavy Transaction Rules

Mutating endpoints must define idempotency key behavior, duplicate detection, retry semantics, and safe response on replay.

Use database constraints, optimistic locking, unique request keys, outbox status transitions, and consumer deduplication where applicable.

Heavy or long-running work should use async job orchestration, workflow, batch, or queue patterns with progress evidence, cancellation, and retry boundaries.

Critical transaction paths must be tested in the Resilience Lab for duplicate submission, concurrent requests, timeout, partial failure, dependency outage, DLQ, replay, and rollback/compensation.

## 11.2 Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop
| Stage | Developer Obligation |
| --- | --- |
| Detect | Convert logs, metrics, traces, errors, scans, failed tests, incidents, user feedback, or GitNexus findings into classified evidence. |
| Retrieve Evidence | Collect ticket, trace, logs, audit, commits, tests, contracts, policies, runtime config, and affected dashboard references. |
| Propose Candidate | Generate candidate fix, learning, prompt update, rule update, test addition, or refactoring as draft only. |
| Verify | Run deterministic tests, security scans, contract checks, policy checks, architecture fitness, and rollback validation. |
| Approve | Named human reviewer and required checker approve before merge, activation, or promotion. |
| Monitor | Post-change signals and evidence confirm improvement or trigger rollback/backlog refinement. |

# 12. PR/MR Evidence Template
| Section | Required Content |
| --- | --- |
| Attributable | Owner, developer, reviewer/checker, ticket, branch, commit, AI tools used, prompt standard, affected bounded context, affected docs. |
| Verifiable | Build/test results, unit/component/contract/integration/mutation tests, SAST/SCA/secrets/authenticated DAST, OPA tests, GitNexus report, SBOM/provenance, architecture fitness results. |
| Classifiable | Data classification, secrets handling, PII handling, model route eligibility, prompt/output classification, evidence storage path, retention rule. |
| Improvable | Known limitations, rejected options, backlog items, follow-up tests, prompt/standard improvements, runbook updates, monitoring feedback. |
| Design Principle Impact | EDP-01 through EDP-20 review, SOLID impact, Clean Architecture, DDD, ports/adapters, testability, security, observability, reversibility, AVCI. |
| Runtime / Operations | Trace dashboard, audit query, error-monitoring link, rollback/forward-fix plan, feature toggle plan, DLQ/replay plan, post-promotion monitoring. |

# 13. RACI, Roadmap, Acceptance Criteria, and Open Reconciliation Items

## 13.1 RACI
| Activity | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Implement backend/frontend/MicroFunction change | Developer | Software Development Lead | Architect, Security, QA/SDET, DBA as needed | Product Owner, SRE |
| Contract/schema/database change | Developer / DBA | Architecture / DBA Lead | API Owner, Data Governance, Security | DevSecOps, QA |
| Security-sensitive change | Developer / Security | Security Architecture | OPA/SBAC Owner, DevSecOps, Internal Audit | CAB/ARB |
| AI-assisted or agent-generated artifact | Developer / AI Operator | AI Governance / Development Lead | Security, Architecture, QA | Internal Audit |
| Release promotion | DevSecOps | CAB / Release Manager | Architecture, Security, QA, SRE | Business Owner |

## 13.2 Roadmap
| Phase | Target Outcome |
| --- | --- |
| Phase 1 | Adopt v4.2 developer checklist and PR/MR evidence template for all active AIRA repositories. |
| Phase 2 | Enforce contract, security, architecture, and evidence gates in CI/CD with developer-friendly failure messages. |
| Phase 3 | Integrate GitNexus impact summaries, Dynamic Workspace component checks, MicroFunction runtime tests, and Resilience Lab scenarios. |
| Phase 4 | Use evidence trends to improve prompts, templates, test packs, runbooks, and training without allowing silent mutation. |

## 13.3 Acceptance Criteria

Developers can identify governing source, bounded context, classification, owner, and evidence path before coding.

All mergeable changes include tests, security checks, architecture fitness, GitNexus impact, rollback plan, and AVCI summary.

Dynamic Workspace and MicroFunction changes prove backend authority, policy filtering, idempotency, observability, and reversibility.

No direct provider SDK calls, direct production credentials, direct production mutation, manual DDL, or hidden business authority exist in reviewed code.

Runtime telemetry and evidence can reconstruct critical actions without exposing secrets, raw PII, or Restricted content.

## 13.4 Open Reconciliation Items

Update 04 Technology Stack after this guide to confirm Java 25, Spring Boot target, frontend baseline, DevSecOps tools, observability stack, model gateway, and approved versions.

Update 05 Information Nervous System to align source authority, AI retrieval, evidence, Obsidian/LLM Wiki, GitNexus, and memory controls.

Update 06 CLAUDE.md Reference to compile developer rules into repository-level AI assistant instructions.

Update 07 Skills Framework to align SBAC skill grants, trust tiers, developer roles, and agent action boundaries.

Update 06 Revision Control Matrix last to record supersedence, duplicate handling, and aligned folder completeness.

# 14. External Alignment Register
| External Reference | Developer Guide Alignment |
| --- | --- |
| NIST AI RMF / NIST AI 600-1 | AI-assisted development, model route risk, guardrail evidence, human accountability, evaluation, and generated-output risk management. |
| NIST SSDF SP 800-218 | Secure software development, threat-informed design, verification, vulnerability remediation, and supply-chain evidence. |
| OWASP ASVS 5.0.0 / OWASP GenAI / LLM guidance | Secure API, authentication, session, access control, input validation, abuse cases, secrets handling, AI prompt/output security, and authenticated DAST. |
| OpenTelemetry Semantic Conventions | Common trace, metric, log, resource, and GenAI observability attributes for interoperable telemetry. |
| SLSA v1.2 | Build provenance, artifact integrity, supply-chain control, trusted builders, and attestation expectations. |
| W3C WCAG 2.2 / WAI-ARIA | Accessible frontend, Dynamic Workspace, widget states, focus, keyboard, semantic structure, and responsive UX. |

# 15. AVCI Compliance Summary
| AVCI Property | Developer Guide v4.2 Evidence |
| --- | --- |
| Attributable | Defines document owner, co-owners, developer roles, RACI, source hierarchy, PR/MR ownership, AI-use declaration, reviewer/checker accountability, and evidence paths. |
| Verifiable | Requires tests, scans, contract checks, policy decisions, architecture fitness, GitNexus impact, SBOM/provenance, observability, audit, rollback, and acceptance criteria. |
| Classifiable | Requires classification for code, configuration, data, prompts, logs, traces, screenshots, evidence, model routes, artifacts, and runtime outputs. |
| Improvable | Defines open reconciliation items, Auto-Heal/Auto-Learn/Auto-Improve candidate loops, feedback paths, runbook updates, prompt improvements, and quarterly review. |

## Final Control Statement

The AIRA Developer Guide accelerates delivery only when developers remain inside the governed engineering system. A change that cannot be attributed, verified, classified, improved, observed, tested, secured, reversed, or reviewed is not ready for AIRA, regardless of whether it works locally.

