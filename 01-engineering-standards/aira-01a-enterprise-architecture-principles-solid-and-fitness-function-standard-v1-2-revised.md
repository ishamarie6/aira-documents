---
title: "Enterprise Architecture Principles SOLID and Fitness Function Standard"
doc_id: "AIRA-01A"
version: "v1.2"
status: "revised"
category: "Engineering standards"
source_docx: "AIRA_01A_Enterprise_Architecture_Principles_SOLID_and_Fitness_Function_Standard_v1.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 01-engineering-standards
  - revised
  - aira-01a
---



# Enterprise Architecture Principles SOLID and Fitness Function Standard



AIRA
AI-Native Enterprise Platform

Enterprise Architecture Principles, SOLID, and Fitness Function Standard

Canonical 01A Authority | Duplicate 01A Reconciliation | Dynamic Workspace | MicroFunction | System Builder | AVCI Always
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-001A |
| Canonical Filename | AIRA_01A_Enterprise_Architecture_Principles_SOLID_and_Fitness_Function_Standard_v1.2_Revised.docx |
| Version | v1.2 - Canonical Consolidation, Dynamic Workspace, MicroFunction, System Builder, and Evidence Gate Update |
| Status | Draft for Architecture Review Board / CAB / Security Governance / DevSecOps / Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; Platform Engineering; AI Engineering; SRE / Operations; Internal Audit |
| Supersedes / Consolidates | 01A-AIRA_Enterprise_Architecture_Principles_SOLID_and_Fitness_Function_Standard_v1.1_final and 01A-AIRA_Enterprise_Design_Principles_and_SOLID_Enforcement_Layer_v1.1_Aligned as competing 01A authorities |
| Companion / Reference Disposition | Document 28 / Enterprise Design Principles Reference Library remains a companion/reference source only, not a controlling authority |
| Effective Date | Upon ARB / CAB approval |
| Review Cadence | Quarterly; unscheduled on material architecture, Dynamic Workspace, MicroFunction, System Builder, AI agent, DevSecOps, security, observability, or technology-stack change |
| Evidence Path | OpenKM Tier-0 / AIRA / Architecture / 01A-Enterprise-Architecture-Principles / v1.2/ |

Mandatory Practice Statement. No AIRA code, configuration, MicroFunction, prompt, guardrail, AI agent, Dynamic Workspace artifact, System Builder output, API, event, migration, pipeline, evidence record, or environment provisioning action is production-ready unless it preserves or improves SOLID, Clean Architecture, DDD bounded contexts, ports-and-adapters, testability, security, observability, reversibility, policy-as-code, resilience, progressive autonomy, and AVCI evidence. AI may accelerate work; it must never become authority or bypass human accountability, policy, classification, verification, or rollback controls.

# Static Table of Contents

1. Executive Summary and v1.2 Consolidation Verdict

2. Purpose, Scope, Authority, and Source Disposition

3. v1.2 Change Summary

4. Canonical Relationship to Existing AIRA Documents

5. Enterprise Architecture Control Model

6. Enterprise Design Principles EDP-01 through EDP-20

7. SOLID, Clean Architecture, DDD, and Ports-and-Adapters Enforcement

8. Dynamic Workspace and Frontend Architecture Rules

9. MicroFunction Backend and Runtime Assembly Rules

10. System Builder and AI Agent Architecture Governance Boundary

11. Contract, API, Event, Data, and Schema Boundary Rules

12. DevSecOps, GitNexus, Evidence Pack, and Promotion Gates

13. Observability, Telemetry, Runtime Toggles, and Evidence Correlation

14. Security, OPA/SBAC, Abuse Cases, DAST, and Secrets Hygiene

15. Concurrency, Heavy Transaction, Idempotency, Outbox, Replay, and Resilience Lab

16. Auto-Heal, Auto-Learn, and Auto-Improve Architecture Candidate Loop

17. Architecture Fitness Function Governance

18. ADR/TDL, Waivers, Exceptions, and Non-Conformance

19. RACI and Operating Responsibilities

20. Implementation Roadmap and Acceptance Criteria

21. Open Reconciliation Items

22. AVCI Compliance Summary

23. Appendices

# 1. Executive Summary and v1.2 Consolidation Verdict

AIRA is a mission-critical, AI-native enterprise platform. Architecture discipline is therefore not advisory wording; it is the control layer that determines whether generated work, human work, AI-assisted work, and operational improvement can safely move toward runtime activation. This v1.2 revision establishes one canonical 01A authority and removes ambiguity caused by two Pack 01 files using 01A numbering.

This revision consolidates the stronger architecture-governance scope of the Enterprise Architecture Principles, SOLID, and Fitness Function Standard with the principle-reference and SOLID enforcement content of the Enterprise Design Principles and SOLID Enforcement Layer. The resulting document is the single 01A architecture enforcement standard for AIRA.
| Decision Area | v1.2 Verdict | Required Treatment |
| --- | --- | --- |
| Duplicate 01A authority | Resolved | Only this 01A v1.2 is the canonical enforcement authority after approval. Older 01A v1.1 variants become superseded inputs. |
| Document 28 / reference library | Retained as companion | Reference/library material may support training and website references but cannot override 01A gates. |
| Dynamic Workspace | Strengthened | Frontend generation must remain backend-governed, policy-filtered, accessible, observable, reversible, and MicroFunction-backed. |
| MicroFunction runtime | Strengthened | Runtime assembly must preserve standard steps, policy, classification, idempotency, outbox, observability, rollback, and AVCI evidence. |
| System Builder | Strengthened | System Builder may classify, analyze, recommend, draft, validate, and propose; it may not silently mutate production or approve its own output. |
| AI agents | Strengthened | Agents are registered architecture artifacts with identity, owner, SBAC scope, OPA policy, tool boundary, model route, guardrails, telemetry, and retirement path. |
| Evidence and fitness | Strengthened | Every material change requires architecture impact evidence, automated checks, human review, and rollback or compensation path. |

Figure 1. 01A duplicate authority reconciliation model.

# 2. Purpose, Scope, Authority, and Source Disposition

## 2.1 Purpose

The purpose of this standard is to define enforceable architecture principles, fitness gates, and evidence requirements for every artifact that can influence AIRA behavior, including code, configuration, prompts, guardrails, MicroFunctions, APIs, events, database migrations, Dynamic Workspace templates, System Builder outputs, AI agents, pipelines, runbooks, dashboards, and operational improvement proposals.

## 2.2 Scope

Backend, frontend, database, integration, workflow, AI, security, observability, infrastructure, knowledge, and evidence artifacts.

Dynamic Workspace, Composable Experience Framework, Experience Blocks, Experience Packs, Admin Builder, AI Assistant Panel, and responsive UX behavior.

MicroFunction framework, standard steps, runtime configuration, runtime assembly, outbox, replay, DLQ, evidence, and rollback controls.

System Builder intake categories: new requirements, operational/engineering evidence, improvement requests, AI agent lifecycle, and AI DevSecOps provisioning.

AI agents, skills, trust tiers, SBAC scopes, OPA policies, model routes, tool gateways, guardrails, monitoring, suspension, and retirement.

DevSecOps pipelines, GitNexus, evidence packs, policy-as-code, architecture fitness functions, CI/CD promotion gates, and CAB/ARB controls.

## 2.3 Out of Scope

Unreviewed personal notes, unmanaged chat transcripts, and AI drafts not promoted through AIRA source governance.

Frontend or AI-generated screens acting as business authority without backend policy, API, MicroFunction, database, and evidence controls.

Autonomous production mutation, direct model-provider calls, direct Git/CI/CD/Kubernetes/database credentials for agents, or unmanaged environment setup.

Manual production DDL, click-ops configuration, or runtime changes that bypass Flyway, GitOps/IaC, policy, audit, and evidence gates.

## 2.4 Authority and Precedence
| Level | Authority | Role |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance / Data Governance | Final authority for platform boundaries, production risk, material exceptions, and conflict resolution. |
| L1 | 01 AVCI, this 01A, 02 Engineering Blueprint | Universal quality, evidence, architecture, system-boundary, and design-principle enforcement. |
| L2 | Specialist standards: 03, 04, 05, 06, 07, 10, 11, 12A, 15, 16, 17, 19, 20, 30, 31A, 42, 43, 53-61 | Domain-specific implementation standards that must inherit 01A controls. |
| L3 | ADR/TDL, waivers, tickets, PR/MR evidence, runbooks, CI/CD records | Implementation-specific proof. These cannot weaken higher authority standards. |
| L4 | Runtime telemetry, audit, evidence stores, dashboards, incident records | Operational evidence used for review, improvement, and trace reconstruction. |

Conflict rule: when two documents appear inconsistent, reviewers must not silently choose the convenient interpretation. Log the issue as an AVCI reconciliation item, assign an owner, classify severity, recommend the governing source, and route through the revision-control matrix / 00D register.

# 3. v1.2 Change Summary
| Change Area | v1.2 Improvement |
| --- | --- |
| Canonicalization | Consolidates two 01A variants into one controlling 01A standard and demotes reference-library material to companion status. |
| Dynamic Workspace | Adds explicit UX/front-end boundary, backend authority, MicroFunction binding, policy filtering, accessibility, and evidence requirements. |
| MicroFunction | Strengthens configuration-first runtime assembly, standard steps, idempotency, outbox, replay, DLQ, rollback, and evidence gates. |
| System Builder | Requires intake classification, impact analysis, contract-first outputs, fitness checks, human approval, and proposal-only improvement workflows. |
| API/event/data | Adds OpenAPI, AsyncAPI, Kafka, Avro/JSON Schema, CloudEvents, outbox, schema evolution, idempotent consumers, DLQ, replay, and Flyway-only gates. |
| DevSecOps and GitNexus | Adds GitNexus read-only impact evidence, security gates, SBOM/provenance, signed artifact expectations, PR/MR AVCI, and promotion-readiness controls. |
| Observability | Adds Log4j2, OpenTelemetry, Sentry, Loki, Tempo, Grafana, trace reconstruction, runtime telemetry toggles, and non-disableable security/audit/evidence signals. |
| Security | Adds OPA/SBAC expansion, abuse cases, authenticated DAST, secure APIs, secrets hygiene, guardrail routing, and remediation evidence requirements. |
| Resilience | Adds concurrency, heavy transaction, idempotency, outbox, replay, cache consistency, rollback, and Resilience Lab gates. |
| Continuous improvement | Clarifies Auto-Heal, Auto-Learn, and Auto-Improve as candidate/proposal loops, never silent source-of-truth mutation. |

# 4. Canonical Relationship to Existing AIRA Documents
| Document / Family | Relationship to 01A v1.2 | Required Treatment |
| --- | --- | --- |
| 01 AVCI Engineering Standard | Universal quality and lifecycle discipline | AVCI defines trust evidence; 01A defines architecture principle enforcement that every AVCI record must include. |
| 01B AVCI Evidence | Evidence/audit/traceability companion | Evidence schemas must include design-principle impact, fitness result, policy decision, rollback path, and improvement link. |
| 02 Engineering Blueprint | Build-ready architecture authority | Blueprint service boundaries, flows, contracts, and evidence models must satisfy 01A. |
| 03 Developer Guide | Developer execution standard | Coding rules, PR templates, AI-use declarations, and branch workflows must enforce 01A. |
| 04 Technology Stack | Approved technology baseline | Technology choices must prove alignment with security, observability, testability, supply chain, and reversibility. |
| 05 Information Nervous System | Source authority and retrieval governance | Retrieval and knowledge projections must not serve stale or superseded content as current authority. |
| 06 CLAUDE.md Reference | AI coding assistant behavior standard | Repository AI rules and tool adapters must be generated from approved standards and must not weaken 01A. |
| 07 Skills Framework | Human and AI skill eligibility | Skill certification must prove ability to preserve affected EDP controls. |
| 10 MicroFunction family | Runtime assembly and standard step governance | MicroFunction design must preserve boundary, policy, idempotency, observability, rollback, and evidence controls. |
| 12A / 53-61 Dynamic Workspace family | UI, UX, templates, observability, AI panel, and System Builder companion standards | UI and AI-generated workspace behavior must remain backend-governed, policy-filtered, accessible, traceable, and reversible. |
| 15 API / 15A Contract-First | OpenAPI/AsyncAPI/schema/event governance | Boundary-crossing behavior must be contract-first and testable before implementation or generation. |
| 16 / 16A / 16B Database and Flyway | Database truth and migration governance | All database objects, seeds, RLS, data fixes, and schema evolution must be Flyway-governed. |
| 17 / 17A Security | Identity, secrets, access, and secure implementation | OPA/SBAC, least privilege, fail-closed, secrets hygiene, and authenticated DAST must support architecture gates. |
| 19 GitNexus | Read-only derivative code intelligence | GitNexus may support impact analysis and evidence; it cannot approve, merge, deploy, mutate production, or replace tests. |
| 20 / 45 / 60 DevSecOps evidence packs | Pipeline and evidence implementation | CI/CD must produce architecture fitness, security, contract, supply-chain, observability, rollback, and AVCI evidence. |
| 42D-42S AI Agent Governance | Agent identity, autonomy, tools, memory, certification, incidents, and registry | Agent governance must be treated as architecture control and not separate automation convenience. |

# 5. Enterprise Architecture Control Model

AIRA enforces architecture through a layered control model: principles define the rules, standards codify them, ADRs and TDLs record decisions, implementation artifacts express approved changes, fitness functions verify behavior, promotion gates control movement, and runtime evidence supports improvement.

Figure 2. Enterprise architecture control model for 01A v1.2.

## 5.1 Non-Negotiable Architecture Rule

A change is not production-ready merely because it compiles, renders, tests happy paths, or produces a plausible AI response. It becomes promotion-ready only when it is attributable, verifiable, classifiable, improvable, policy-compliant, testable, secure, observable, reversible, and supported by architecture fitness evidence.

# 6. Enterprise Design Principles EDP-01 through EDP-20

The following principles are mandatory gates for AIRA design, implementation, review, generation, promotion, runtime operation, and continuous improvement. Each affected PR/MR, migration, template, workflow, agent, prompt, or runbook must declare principle impact and evidence.
| ID | Principle | Mandatory Architecture Gate | Required Evidence |
| --- | --- | --- | --- |
| EDP-01 | SOLID | Single responsibility, open/closed extensibility, substitutability, interface segregation, and dependency inversion are preserved. | Class design review, ArchUnit/dependency rules, PR principle summary. |
| EDP-02 | Clean Architecture | Domain/use-case logic does not depend on UI, database, workflow engine, model provider, or infrastructure framework. | Layer dependency checks, package rules, adapter tests. |
| EDP-03 | DDD / Bounded Contexts | Business domains own language, invariants, schemas, APIs, events, and runbooks. | Context map, schema ownership, API/event ownership, ADR/TDL. |
| EDP-04 | Ports and Adapters | External systems, databases, models, queues, tools, and providers are accessed through explicit ports/adapters. | Interface contracts, mock adapters, dependency scans. |
| EDP-05 | DRY, KISS, YAGNI | Avoid duplicated logic, accidental complexity, speculative abstractions, and over-engineering. | Code review, duplication scan, architecture review. |
| EDP-06 | Idempotency by Design | Retries, replays, callbacks, event consumers, and tool actions do not duplicate effects. | Idempotency key tests, replay tests, duplicate event tests. |
| EDP-07 | Determinism and Reproducibility | Builds, migrations, prompts, model routes, tests, environments, and evidence are reproducible from approved sources. | Pinned versions, CI logs, SBOM/provenance, migration checksums. |
| EDP-08 | Fail-Safe, Not Fail-Open | If identity, policy, guardrail, audit, evidence, or model gateway fails, protected actions stop. | Negative tests, OPA tests, gateway fault tests. |
| EDP-09 | Human-in-the-Loop | High-impact, low-confidence, Restricted, destructive, or production-impacting actions require named human approval. | Approval record, maker-checker evidence, CAB/ARB reference. |
| EDP-10 | Least Privilege / SBAC | Humans, services, System Builder, and AI agents receive only approved skills, tools, data, and environment scope. | SBAC grant, OPA decision, access review, recertification. |
| ID | Principle | Mandatory Architecture Gate | Required Evidence |
| --- | --- | --- | --- |
| EDP-11 | Separation of Duties | Maker, checker, approver, deployer, operator, owner, and auditor roles remain separated for high-risk workflows. | CODEOWNERS, approval workflow, SoD policy result. |
| EDP-12 | Observability by Design | Critical paths emit trace, metric, log, audit, model, agent, and evidence references with safe redaction. | OTel traces, logs, metrics, dashboards, forbidden-field tests. |
| EDP-13 | Policy as Code | Authorization, routing, guardrail, deployment, data-handling, and agent-tool rules are versioned policy artifacts. | OPA/Rego tests, policy PR evidence, decision logs. |
| EDP-14 | Testability by Design | Code, workflows, prompts, adapters, policies, and provisioning manifests are independently testable. | Unit/component/contract/policy/e2e tests, deterministic fixtures. |
| EDP-15 | Secure by Design | Threat controls, secrets hygiene, classification, tenant isolation, and secure defaults are built in. | SAST/SCA/DAST, secret scan, threat model, abuse cases. |
| EDP-16 | Resilience Patterns | Timeouts, retries, circuit breakers, bulkheads, fallback, DLQ, compensation, recovery, and rebuild are explicit. | Resilience Lab report, chaos/fault tests, DLQ/replay evidence. |
| EDP-17 | Architectural Fitness Functions | Automated checks continuously verify boundaries, contracts, security, agents, provisioning, and evidence rules. | CI fitness report, policy checks, drift report. |
| EDP-18 | Progressive Autonomy | Automation advances only when evidence, trust score, skills, risk tier, guardrails, and rollback controls support it. | Trust tier, certification, autonomy decision, kill switch evidence. |
| EDP-19 | Reversibility / Rollbackability | Changes support rollback, forward-fix, compensation, feature disablement, environment rebuild, or safe deactivation. | Rollback plan, rehearsal result, feature flag, compensation test. |
| EDP-20 | AVCI | Every artifact remains attributable, verifiable, classifiable, and improvable across lifecycle. | AVCI summary, evidence ref, classification, improvement backlog. |

# 7. SOLID, Clean Architecture, DDD, and Ports-and-Adapters Enforcement

## 7.1 SOLID Enforcement Standard
| SOLID Rule | AIRA Enforcement | Common Rejection Example |
| --- | --- | --- |
| Single Responsibility | Each service, MicroFunction, prompt, policy, adapter, and widget has one clear reason to change. | One service validates input, calls database, invokes model, formats UI, and writes audit directly. |
| Open/Closed | New behavior is added through configuration, policy, adapter, or extension points before modifying stable framework code. | Hardcoding new workflow branches into controllers or common runtime code. |
| Liskov Substitution | Adapters and implementations must respect port contracts and error semantics. | Mock/non-prod adapter permits behavior blocked by production adapter. |
| Interface Segregation | Ports expose narrow capability-specific interfaces, not broad God interfaces. | Agent tool interface grants read/write/delete/deploy when only read is needed. |
| Dependency Inversion | Domain and use-case logic depend on abstractions; frameworks and providers are adapters. | Domain service imports Keycloak, OPA client, Kafka producer, or OpenAI SDK directly. |

## 7.2 Clean Architecture Gate

Controllers, widgets, workflow handlers, agent tools, and event consumers are adapters; they must not own business rules.

Domain/application layers must not directly call PostgreSQL, Redis/Valkey, Kafka, Keycloak, OPA, LiteLLM, OpenKM, Flowable, Temporal, Sentry, Loki, or external APIs.

Infrastructure concerns are replaceable through adapters and tested with deterministic fixtures.

Any boundary leak requires rejection, refactoring, or approved waiver with exit plan.

## 7.3 DDD and Bounded Context Gate

Every schema, API, event, MicroFunction, workflow, prompt, and widget must declare owning bounded context.

No context may write directly across another context boundary; use published APIs, events, workflows, or controlled data products.

Context ownership must be visible in ADR/TDL, OpenAPI/AsyncAPI metadata, schema registry entries, and PR/MR evidence.

## 7.4 Ports-and-Adapters Gate

All external dependencies must be accessed through named ports and adapters.

Adapters must implement timeout, retry, circuit breaker, authentication, classification, audit, redaction, and observability behavior where applicable.

AI model access must route through LiteLLM or approved private/on-prem gateways; direct provider SDK calls from application code are rejected.

# 8. Dynamic Workspace and Frontend Architecture Rules

Dynamic Workspace enables composable role-aware user experiences. It does not create business authority. UI generation, widget arrangement, responsive behavior, and AI panel outputs are presentation and interaction surfaces governed by backend APIs, policies, MicroFunction transactions, and evidence records.
| Area | Mandatory Architecture Rule | Evidence |
| --- | --- | --- |
| Workspace resolution | Resolved layout must come from approved backend configuration and OPA/SBAC filtering. | workspace_resolved trace, layout hash, policy decision, evidence_ref. |
| Widget actions | Every state-changing widget action must call an approved API/MicroFunction or workflow. | OpenAPI operation, idempotency key, policy decision, audit event. |
| Frontend authority | Frontend code may hide, disable, or render safe states; it must not decide authorization or business outcome. | OPA decision from backend, UI denied-state test. |
| Accessibility and responsiveness | UX must meet approved accessibility, keyboard, focus, screen-reader, and responsive design standards. | Playwright/a11y/visual regression evidence. |
| AI panel | AI output is advisory unless converted into a governed proposal and approved through proper workflow. | prompt evidence, guardrail result, model route, action proposal record. |
| Template changes | Admin Builder changes must use maker-checker approval, versioning, rollback, and activation evidence. | template lifecycle audit, approval record, rollback ref. |

Figure 3. Dynamic Workspace and MicroFunction architecture boundary.

# 9. MicroFunction Backend and Runtime Assembly Rules

MicroFunctions are the governed unit of business-capability assembly. The preferred delivery model is configuration-first. Custom code is permitted only for the specific business capability gap after standard steps, templates, policies, and configuration patterns are proven insufficient.
| MicroFunction Control | Mandatory Requirement |
| --- | --- |
| Standard step sequence | Receive, correlate, resolve actor/session/tenant, classify, authorize, validate, idempotency, execute, audit, outbox, observe, respond, and record evidence. |
| Configuration authority | MicroFunction definitions, runtime parameters, feature flags, policy refs, and step orders are versioned source artifacts and promoted through CI/CD. |
| Backend authority | Business state changes occur in backend MicroFunction/application services, not in frontend templates or AI-generated client logic. |
| Database authority | PostgreSQL is the authority for runtime configuration and business state; Redis/Valkey accelerates but never becomes truth. |
| Rollback | Runtime definitions must support disable, revert, forward-fix, compensation, or safe stop. |
| Evidence | Every execution must carry trace_id, request_id, actor, policy_decision_id, microfunction_transaction_code, run_id, classification, and evidence_ref where applicable. |

# 10. System Builder and AI Agent Architecture Governance Boundary

## 10.1 System Builder Boundary

The System Builder is a governed AI-assisted engineering factory interface. It may intake, classify, analyze, recommend, draft, validate, and prepare candidate artifacts. It must not silently mutate runtime behavior, approve its own output, bypass policy or classification controls, install unapproved technologies, or promote changes without AVCI evidence.
| System Builder Stage | Required Control | Blocked Condition |
| --- | --- | --- |
| Intake | Capture source, owner, classification, domain, risk, desired outcome, and approval path. | Missing source, owner, classification, or affected domain. |
| Analysis | Retrieve current standards, affected contracts, runtime evidence, tests, and dependencies. | Stale, superseded, or classification-ineligible source served as current authority. |
| Recommendation | Present options, risk, impact, tests, policy, rollback, and required approvals. | Single-path recommendation with hidden assumptions or missing rollback path. |
| Generation | Generate draft contract, code, config, policy, prompt, migration, test, runbook, or evidence package only in approved branch/sandbox. | Direct production mutation or main-branch write. |
| Validation | Run architecture fitness, tests, scans, policy checks, contract compatibility, and evidence completeness checks. | Protected control unavailable, bypassed, or disabled. |
| Promotion | Require maker-checker, CODEOWNERS, ARB/CAB where triggered, signed artifacts, and evidence pack. | AI self-approval or missing human accountability. |

## 10.2 AI Agent Boundary

Every agent must have identity, owner, purpose, non-goals, skill scope, trust tier, classification ceiling, tool scope, model route, guardrails, runtime telemetry, suspension path, and retirement path.

Agents must not hold direct production credentials or direct Git/CI/CD/Kubernetes/database/model-provider authority.

Tool actions must be mediated by Harness/MCP gateway, SBAC, OPA, guardrails, audit, and human approval where required.

Progressive autonomy is action-specific, evidence-backed, reversible, and revocable.

# 11. Contract, API, Event, Data, and Schema Boundary Rules
| Boundary | Mandatory Rule | Evidence Gate |
| --- | --- | --- |
| OpenAPI | REST/API behavior must be contract-first, versioned, linted, tested, and safe-response aligned. | OpenAPI diff, contract tests, generated client/server evidence. |
| AsyncAPI | Kafka/event behavior must be contract-first and include topic ownership, event type, schema, retention, replay, and DLQ behavior. | AsyncAPI validation, consumer contract tests. |
| Avro / JSON Schema | Payload schemas must be versioned, compatible, governed, and classified. | Schema registry check, compatibility report. |
| CloudEvents | Domain/integration events should carry stable event metadata, source, subject, id, time, type, trace correlation, and classification where safe. | CloudEvents conformance tests. |
| Outbox | State changes that publish events must use transactional outbox or approved equivalent. | Outbox table, poller/relay evidence, duplicate suppression tests. |
| DLQ and Replay | Failed consumers must provide controlled DLQ, redaction, triage, replay, and idempotent processing. | DLQ runbook, replay test, idempotency evidence. |
| Schema evolution | Breaking changes require versioning, migration, consumer readiness, deprecation path, and rollback/compensation plan. | Compatibility report, consumer sign-off, deprecation evidence. |
| Flyway | Database schema, seed data, RLS, indexes, views, data fixes, and control tables must be Flyway-governed. | Flyway checksum, clean/migrate report, DBA review. |

# 12. DevSecOps, GitNexus, Evidence Pack, and Promotion Gates

AIRA DevSecOps gates convert architecture principles into continuous verification. The pipeline must not merely build software; it must prove that the change is attributable, verifiable, classifiable, improvable, secure, observable, testable, reversible, and architecture-compliant.
| Gate | Mandatory Evidence |
| --- | --- |
| Repository governance | Branch, commit, CODEOWNERS, PR/MR, AI-use declaration, issue/ticket, ADR/TDL if triggered. |
| Build and test | Reproducible build, Java/toolchain version, unit/component/contract/e2e/policy tests, mutation where applicable. |
| Security | SAST, SCA, secret scan, IaC/container scan, authenticated DAST, abuse-case tests, remediation evidence. |
| Supply chain | SBOM, provenance, artifact digest, signing/attestation, approved package source or mirror. |
| GitNexus | Read-only impact analysis, affected files/tests/contracts, architecture drift, ownership map, sensitive-code map. |
| Architecture fitness | Layering, dependency, package, API/event, database, policy, prompt, agent, and evidence completeness checks. |
| Promotion | Maker-checker approval, CI/CD evidence pack, rollback plan, CAB/ARB approval if triggered, post-promotion monitoring. |

# 13. Observability, Telemetry, Runtime Toggles, and Evidence Correlation

AIRA must be reconstructable from intent to runtime outcome and from runtime failure back to source, approval, release, and owner. Observability is not optional decoration; it is architecture evidence.
| Signal | Required Use | Non-Disableable Scope |
| --- | --- | --- |
| Logs / Log4j2 | Structured diagnostic logs with redaction, correlation IDs, safe error codes, and environment/service labels. | Security, audit, policy denial, evidence, incident, and control-failure logs. |
| Traces / OpenTelemetry | End-to-end traces across frontend, gateway, backend, policy, MicroFunction, workflow, event, model route, and storage. | Protected transaction traces and evidence correlation fields. |
| Metrics | Latency, throughput, error, SLO, policy denial, cache hit/miss, queue lag, DLQ, replay, AI/model route, and guardrail metrics. | Security and reliability SLO signals required for incident detection. |
| Sentry / error monitoring | Frontend/backend error aggregation with safe context and release correlation. | Critical security, runtime, and user-impacting error capture. |
| Loki / Tempo / Grafana | Log, trace, dashboard, alert, and trace reconstruction surfaces. | Dashboards for evidence completeness, security denials, incidents, and promotion readiness. |
| Runtime toggles | Verbose debug/diagnostic logging may be adjusted under policy and change control. | Do not disable audit, policy, classification, guardrail, security, evidence, or required incident telemetry. |

# 14. Security, OPA/SBAC, Abuse Cases, DAST, and Secrets Hygiene
| Security Control | Mandatory Architecture Requirement |
| --- | --- |
| OPA/SBAC expansion | Authorization must combine role, attribute, skill, resource, action, tenant, environment, classification, risk tier, and approval state where applicable. |
| Fail-closed access | Missing identity, token validation, OPA decision, policy bundle, classification, audit, or evidence blocks protected action. |
| Abuse cases | Requirements, APIs, Dynamic Workspace actions, AI prompts, agents, and workflows must include misuse/abuse cases and negative tests. |
| Authenticated DAST | Authenticated application paths, APIs, and role-specific workspace screens must be tested where practical before promotion. |
| Secure APIs | Use safe response models, Problem Details where applicable, rate limits, pagination controls, validation, content-type restrictions, CSRF/CORS controls, and audit events. |
| Secrets hygiene | Secrets must be referenced through Vault/OpenBao/approved secret manager; never in code, prompts, screenshots, tests, logs, environment dumps, or evidence packs. |
| AI security | Prompt injection, insecure output handling, data leakage, model denial of service, excessive agency, supply-chain, and retrieval poisoning risks must be controlled by guardrails and evaluation evidence. |

# 15. Concurrency, Heavy Transaction, Idempotency, Outbox, Replay, and Resilience Lab
| Concern | Required Treatment | Evidence |
| --- | --- | --- |
| Concurrent user actions | Use optimistic locking, idempotency keys, duplicate-submit protection, and safe UI states. | Concurrent execution test, stale-state UX evidence. |
| Heavy transactions | Split long-running work into workflow/job patterns with progress, timeout, cancellation, compensation, and evidence. | Load test, timeout test, workflow trace, recovery test. |
| Idempotency | Commands, callbacks, webhooks, event consumers, and agent tool actions must be retry-safe. | Idempotency fixture, duplicate replay test. |
| Outbox | Domain state changes and published events must be atomic or compensated. | Outbox relay test, publish failure test. |
| DLQ and replay | DLQ triage and replay must be controlled, classified, auditable, and policy-bound. | DLQ dashboard, replay evidence, human approval if required. |
| Cache consistency | Redis/Valkey is derivative; cache invalidation and rebuild must be safe and observable. | Cache loss/rebuild test, config hash validation. |
| Resilience Lab | Architecture fitness must include retry, timeout, circuit breaker, bulkhead, failover, rollback, and recovery scenarios. | Resilience Lab report linked to PR/MR evidence. |

# 16. Auto-Heal, Auto-Learn, and Auto-Improve Architecture Candidate Loop

Auto-Heal, Auto-Learn, and Auto-Improve are controlled candidate loops. They may detect issues, retrieve evidence, recommend fixes, draft tests, generate proposals, open reviewable artifacts, and update backlogs. They must not silently alter production behavior, weaken controls, or promote their own output.
| Loop Stage | Required Control |
| --- | --- |
| Issue detection | Detect from telemetry, incident, SLO burn, security scan, test failure, user feedback, architecture drift, or evidence gap. |
| Evidence retrieval | Retrieve only approved, current, classification-eligible evidence with provenance and freshness check. |
| Root cause hypothesis | Classify confidence, affected bounded context, architecture risk, data risk, and policy impact. |
| Candidate proposal | Prepare recommended fix/learning/improvement with tests, rollback, policy, security, observability, and evidence impacts. |
| Human approval | Maker-checker review, CODEOWNERS, owner sign-off, ARB/CAB/Security approval where triggered. |
| Validation | Run deterministic tests, security scans, contract checks, policy tests, architecture fitness, and resilience checks. |
| Promotion and monitoring | Promote through CI/CD only after evidence gates pass; monitor post-action behavior and record improvement outcome. |

Figure 4. Architecture fitness function and evidence loop.

# 17. Architecture Fitness Function Governance

## 17.1 Fitness Function Families
| Fitness Family | Example Checks | Gate Type |
| --- | --- | --- |
| Layering and dependencies | No controller-to-database, domain-to-framework, direct model SDK, or direct infrastructure dependency. | Blocking |
| Bounded context | No cross-context write, schema ownership conflict, or unapproved shared table. | Blocking |
| Contract compatibility | OpenAPI/AsyncAPI/schema breaking change detection; consumer readiness. | Blocking or waiver-controlled |
| Database governance | Flyway checksum, migration reversibility, no manual DDL, RLS/index/seed review. | Blocking |
| Security | SAST/SCA/secret/DAST/OPA/abuse-case results and remediation evidence. | Blocking for Critical/High unless formally waived |
| Observability | Required trace/log/metric/audit/evidence fields and forbidden telemetry tests. | Blocking for critical paths |
| AI and agent governance | LiteLLM route, guardrails, SBAC/OPA, tool registry, trust tier, certification, kill switch. | Blocking for agent/runtime actions |
| Dynamic Workspace | Accessibility, responsive design, widget states, policy-denied states, backend authority, MicroFunction binding. | Blocking for UX release |
| Evidence completeness | AVCI summary, owner, source, classification, tests, rollback, improvement path. | Blocking for promotion |

## 17.2 Minimum CI Evidence Fields

artifact_id, branch, commit, author, reviewer, owner, source_ref, ticket_ref, ADR/TDL/waiver_ref where applicable.

bounded_context, affected_contracts, affected_schemas, affected_microfunctions, affected_workspace_components, affected_agents.

classification, data_handling, secrets_result, policy_decision_ref, test_report_ref, security_scan_ref, GitNexus_report_ref.

architecture_boundary_impact, design_principle_impact, fitness_function_result, rollback_plan_ref, evidence_ref, improvement_backlog_ref.

# 18. ADR/TDL, Waivers, Exceptions, and Non-Conformance
| Trigger | Decision Artifact Required |
| --- | --- |
| New bounded context, service, schema, API family, event family, agent type, model route, or workflow engine behavior | ADR |
| Technology version deviation, Java fallback, database exception, tool adoption, package source exception, or infrastructure pattern change | ADR or TDL with exit plan |
| Temporary control bypass, failing fitness function, delayed remediation, or security/test waiver | Formal waiver with owner, risk acceptance, expiry, compensating controls, and review date |
| Production incident or recurrent defect that reveals architecture weakness | TDL/RCA-linked architecture improvement record |
| Duplicate document authority or source-pack conflict | AVCI reconciliation item in revision-control matrix / 00D register |

## 18.1 Explicitly Rejected Patterns

Direct model provider SDK usage from application services, scripts, notebooks, or agents.

Frontend code, admin template, or AI panel output acting as authorization or business-decision authority.

Manual production database edits or data fixes outside Flyway and approved incident/change governance.

System Builder or AI agent approving, merging, deploying, or promoting its own output.

Disabling security, audit, policy, classification, guardrail, or evidence telemetry for performance convenience.

GitNexus, Obsidian, LLM Wiki, Redis/Valkey, dashboards, or AI summaries becoming source of truth without authoritative backing.

Auto-Heal fix that disables a control, hides a finding, skips a test, or bypasses approval to make a pipeline pass.

# 19. RACI and Operating Responsibilities
| Role | Architecture Responsibility | Approval / Evidence Responsibility |
| --- | --- | --- |
| IT Head / Solutions Architecture Office | Owns 01A, resolves architecture priority, assigns reconciliation actions. | Approves standard updates and major governance exceptions. |
| Architecture Board | Reviews material architecture decisions and conflicts. | Approves ADRs, major waivers, and platform boundary changes. |
| Software Development Lead | Ensures design and code preserve 01A principles. | Provides PR/MR evidence and remediation closure. |
| DevSecOps Lead | Implements CI/CD gates, GitNexus, SBOM/provenance, and evidence packs. | Ensures promotion gates and supply-chain evidence are complete. |
| Security Architecture | Defines OPA/SBAC, secrets, abuse cases, DAST, guardrail, and classification requirements. | Approves security exceptions and Critical/High remediation. |
| QA/SDET | Defines deterministic test, contract, policy, accessibility, visual, and resilience evidence. | Validates test adequacy and evidence quality. |
| DBA / Data Governance | Owns Flyway, schema evolution, RLS, data classification, migration and retention controls. | Approves database changes and data-fix governance. |
| SRE / Operations | Owns runtime telemetry, SLOs, incident evidence, rollback, and recovery. | Confirms operational readiness and trace reconstruction. |
| AI Governance / Agent Owner | Owns agent purpose, model route, trust tier, guardrails, tools, monitoring, and retirement. | Approves agent lifecycle, autonomy, certification, and kill-switch readiness. |
| Internal Audit | Reviews AVCI completeness, evidence retention, control testing, and traceability. | Issues audit findings and verifies closure evidence. |

# 20. Implementation Roadmap and Acceptance Criteria
| Wave | Scope | Acceptance Criteria |
| --- | --- | --- |
| Wave 0 | Approve 01A v1.2 canonical consolidation | ARB/CAB confirms this document as sole 01A enforcement authority; duplicate 01A inputs marked superseded. |
| Wave 1 | Update 01, 01B, and 02 | AVCI, evidence, and Engineering Blueprint inherit v1.2 control mapping. |
| Wave 2 | Update developer execution standards | Developer Guide, CLAUDE.md, Skills, Unit Testing, and DevSecOps rules enforce 01A gates. |
| Wave 3 | Update MicroFunction and Dynamic Workspace families | Runtime assembly, UI generation, AI panel, templates, seeding, observability, and pipeline documents align to 01A v1.2. |
| Wave 4 | Update API/data/security/observability/AI governance | OpenAPI/AsyncAPI, Flyway, OPA/SBAC, telemetry, AI agent governance, and System Builder controls are synchronized. |
| Wave 5 | Operationalize gates | CI/CD, GitNexus, dashboards, runtime evidence, ADR/TDL, waiver, and audit workflows are working and measured. |

## 20.1 Definition of Done

Every material change declares affected EDP IDs and architecture boundary impact.

Architecture fitness functions execute in CI/CD and produce evidence.

OpenAPI/AsyncAPI/schema/Flyway/OPA/SBAC changes are validated before implementation or promotion.

Dynamic Workspace changes are accessible, policy-filtered, MicroFunction-backed, observable, and reversible.

AI/System Builder outputs are proposals until reviewed, tested, approved, and promoted through governed workflow.

Runtime telemetry supports trace reconstruction without exposing secrets, tokens, raw PII, or prohibited prompt content.

Rollback, compensation, disablement, forward-fix, or rebuild path is documented and tested where applicable.

AVCI evidence pack is complete and references source, owner, classification, validation, and improvement path.

# 21. Open Reconciliation Items
| Item | Severity | Recommended Treatment |
| --- | --- | --- |
| Two Pack 01 files currently use 01A numbering and overlapping authority language. | High | Adopt this 01A v1.2 as sole canonical authority; mark both v1.1 01A inputs as superseded. |
| Document 28 / EDP reference library may be confused with 01A authority. | Medium | Maintain Document 28 as reference-library companion only; add cross-reference to 01A v1.2. |
| Older references to Technology Stack v9.0, Java fallback, and source-pack v3.0/v1.1 appear across documents. | Medium | Update downstream files during next pass; log version normalization in revision-control matrix. |
| Runtime telemetry toggle rules are not consistently stated across all older observability, SRE, and Dynamic Workspace documents. | Medium | Propagate non-disableable signal rules through 31, 31A, 53, 55, 60, and runbooks. |
| Authenticated DAST, abuse-case evidence, and Resilience Lab gates are stronger in newer revisions than older standards. | Medium | Propagate into security, testing, CI/CD, MicroFunction, and developer standards. |
| 42D-42S AI Agent Governance family is broad and must remain linked without replacing 01A. | Low | Cross-reference agent governance as specialist controls inheriting 01A. |

# 22. AVCI Compliance Summary
| AVCI Property | Compliance Evidence in 01A v1.2 |
| --- | --- |
| Attributable | Identifies document ID, owner, co-owners, source disposition, superseded files, companion documents, authority hierarchy, RACI, and review cadence. |
| Verifiable | Defines architecture fitness functions, CI/CD gates, PR/MR evidence, tests, security scans, GitNexus impact evidence, OPA/SBAC decisions, telemetry, rollback evidence, and acceptance criteria. |
| Classifiable | Marks the document INTERNAL CONFIDENTIAL and requires classification handling for code, prompts, logs, telemetry, evidence, AI retrieval, Dynamic Workspace, and System Builder outputs. |
| Improvable | Provides roadmap, open reconciliation items, non-conformance handling, Auto-Heal/Learn/Improve candidate loop, revision-control routing, and quarterly/triggered review cadence. |

# 23. Appendices

## Appendix A - Architecture Impact Assessment Template
| Field | Required Content |
| --- | --- |
| intake_id / ticket_ref | Controlled intake reference and source. |
| owner / checker / approver | Named accountable roles. |
| bounded_context | Affected business/platform context and owning team. |
| artifact_types | Code, config, API, event, DB, policy, prompt, guardrail, UI, MicroFunction, agent, pipeline, runbook, evidence. |
| EDP impact | Affected EDP IDs and whether each is preserved, improved, weakened, or not applicable. |
| contract impact | OpenAPI, AsyncAPI, schema, CloudEvents, Kafka topic, outbox, DLQ, replay, compatibility, consumer impact. |
| data/security impact | Classification, PII/secrets, tenant isolation, OPA/SBAC, abuse cases, DAST, remediation evidence. |
| observability impact | Trace, log, metric, audit, evidence, dashboard, redaction, runtime toggle treatment. |
| reversibility | Rollback, forward-fix, compensation, disablement, environment rebuild, or retirement plan. |
| fitness evidence | Tests, scans, policy checks, GitNexus report, architecture fitness report, CI evidence. |

## Appendix B - PR/MR 01A Evidence Summary Template

Owner / developer / checker / approver:

Ticket / ADR / TDL / waiver references:

Affected bounded context, contracts, schemas, MicroFunctions, workspace components, agents:

Affected EDP IDs and impact statement:

Architecture boundary checks:

Contract/API/event/schema/Flyway evidence:

OPA/SBAC/security/abuse-case/DAST/secrets evidence:

Test evidence and Resilience Lab evidence:

GitNexus impact and affected tests/contracts:

Observability/evidence/dashboard impact:

Rollback/compensation/disablement plan:

Known limitations and improvement backlog:

## Appendix C - Source Disposition Summary
| Source | Disposition in v1.2 |
| --- | --- |
| 01A-AIRA_Enterprise_Architecture_Principles_SOLID_and_Fitness_Function_Standard_v1.1_final | Primary baseline absorbed and superseded by this v1.2. |
| 01A-AIRA_Enterprise_Design_Principles_and_SOLID_Enforcement_Layer_v1.1_Aligned | Unique principle/enforcement content absorbed; no longer a competing authority after v1.2 approval. |
| 28-AIRA_Enterprise_Design_Principles_and_SOLID_Reference_Library_v1.1_Aligned | Retained as Document 28 / 01A companion reference library only. |
| 06-AIRA_Revision_Control_Matrix_v1.2_Supplemental_Update | Must be updated later to record this consolidation decision and downstream supersedence. |

