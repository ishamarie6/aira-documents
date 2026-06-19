---
title: "MicroFunction Framework"
doc_id: "AIRA-10"
version: "v3.4"
status: "revised"
category: "MicroFunction framework"
source_docx: "AIRA_10_MicroFunction_Framework_v3.4_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 10-microfunction-framework
  - revised
  - aira-10
---



# MicroFunction Framework



AIRA
AI-Native Enterprise Platform

MicroFunction Framework

Configuration-First Runtime Assembly | Reusable Standard Steps | Runtime Evidence Envelope | System Builder Boundaries | Cross-Cutting Capability Coverage
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-010 |
| Document Title | AIRA MicroFunction Framework |
| Version | v3.4 - Foundation Synchronization, Runtime Governance, and Cross-Cutting Capability Coverage Revision |
| Source Reviewed | AIRA_10_MicroFunction_Framework_v3_3_Cross_Cutting_Capability_Update.docx |
| Supersedes | v3.3 Cross-Cutting Capability Update candidate upon ARB/CAB approval |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Architecture Review Board / CAB / Engineering Team Review |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; DBA; Platform Engineering; AI Engineering; SRE / Operations; Internal Audit |
| Primary Role | Parent framework standard for MicroFunction runtime assembly, standard steps, extension controls, configuration governance, evidence, publish gates, and quality controls |
| Companion Documents | 10A Design and Development Guide; 10B Implementation Standard; 10C Sequence Diagram Reference; 10D Standard Function Catalog and Assembly Templates; 10E Backend Service Generation and Runtime Configuration Standard |

Mandatory Practice Statement

Every AIRA transaction, MicroFunction, configuration row, runtime process definition, policy binding, AI-assisted change, and promotion event must preserve or improve SOLID compliance, Clean Architecture boundaries, DDD ownership, ports-and-adapters separation, idempotency, determinism, security, observability, testability, reversibility, rollbackability, and AVCI evidence. Teams must configure first, reuse standard functions, code only the bounded business gap, validate before activation, and submit evidence through controlled PR/MR and approval paths.

# Table of Contents

Insert a Microsoft Word automatic Table of Contents before final publication. Recommended setting: show levels 1 to 3. Update all fields after final approval and before distribution.

# 1. Executive Summary and v3.4 Revision Verdict

The uploaded v3.3 candidate already strengthens AIRA-DOC-010 by adding cross-cutting DevSecOps, eventing, observability, concurrency, resilience, security, and continuous-improvement coverage. This v3.4 revision preserves that direction while correcting version/status drift, tightening the parent-versus-companion boundary, making 10A the correct next review item, and converting cross-cutting requirements into a concise framework standard that developers, System Builder operators, reviewers, and auditors can apply consistently.

The main architectural decision remains unchanged: MicroFunctions are the governed runtime execution fabric of AIRA. They are not a code-generation convenience, workflow shortcut, UI action script, or AI automation bypass. A MicroFunction transaction is complete only when the business result, cross-cutting controls, contracts, policies, tests, evidence, observability, and rollback or compensation posture are all reviewable and reproducible.

# 2. v3.4 Correction and Alignment Summary

The following corrections are applied in this revision: foundation references are synchronized to the completed AIRA foundation revisions available in this workstream; unverified completion claims for 08, 08A, and 09 are removed; 10A is explicitly restored as the next required MicroFunction-family review item; the runtime evidence envelope is made mandatory for critical and production-bound steps; and cross-cutting capability coverage is moved from addendum language into the main framework authority. The framework remains the parent authority for 10A through 10E and must not be reinterpreted by companion documents as a weaker procedure.
| Alignment Area | v3.4 Required Treatment |
| --- | --- |
| Foundation governance | Uses 01A v1.2, 01 v3.2, 01B v1.2, 02 v5.2, 03 v4.2, 04 v9.2, 05 v4.2, 06 v3.2, 07 v3.2, and 07B v1.2 as the current revised foundation candidates. |
| Testing and environment references | Keeps 08, 08A, and 09 as existing/pending companion inputs unless a revised file is separately provided and verified. The document must not claim those files are complete without evidence. |
| MicroFunction sequencing | Confirms this file as parent framework. Next review is 10A, then 10B, 10C, 10D, and 10E. |
| System Builder boundary | System Builder may draft, analyze, generate, and propose, but cannot approve, activate, promote, or mutate production independently. |
| Runtime toggles | Allows runtime tuning for non-essential diagnostics while preserving mandatory audit, security, policy, classification, idempotency, outbox, and evidence signals. |
| Cross-cutting controls | DevSecOps, contracts, events, observability, resilience, Auto-Heal/Auto-Learn/Auto-Improve, security, and evidence coverage are mandatory applicability decisions for every MicroFunction change. |

# 3. MicroFunction Control Plane

Figure 1. AIRA MicroFunction Control Plane

Controllers, workspace actions, event listeners, scheduled jobs, batch tasks, and AI Panel requests remain thin adapters. They submit requests into the runtime execution envelope. The envelope resolves governed configuration, enforces standard cross-cutting steps, invokes bounded STP-BUS-* business functions through ports, and emits evidence by construction.

# 4. Purpose, Scope, and Authority
| Area | Definition |
| --- | --- |
| Purpose | Define AIRA MicroFunctions as the governed execution fabric for modular, runtime-assembled, configuration-first business and platform behavior. |
| In Scope | Transaction definitions, step catalogs, step bindings, parameters, policy bindings, retry/error/compensation profiles, activation controls, runtime assembly, signing, caching, audit, observability, idempotency, concurrency, outbox, DLQ, replay, AI/RAG steps, document-processing steps, and business extension patterns. |
| In Scope - AI/System Builder | System Builder-generated candidate MicroFunction configuration, code, tests, OPA policies, Flyway migrations, prompts, guardrails, model-route settings, and evidence packs. |
| Out of Scope | Uncontrolled scripts, hardwired orchestration, direct production mutation, direct provider SDK calls from business logic, direct database/Kafka/Redis writes from STP-BUS functions, and shadow MicroFunctions not registered in the catalog. |
| Precedence | L0 ARB/CAB/Security Governance; L1 foundation standards; L2 this parent framework; L3 10A-10E companions; L4 implementation evidence. |

# 5. Governing Principles
| Principle | Mandatory Rule |
| --- | --- |
| Configuration First | Assemble transactions using approved standard functions, parameters, rules, DMN, OPA policies, templates, and catalog entries before writing new code. |
| Code Only the Business Gap | New code is allowed only for a genuinely new STP-BUS-* business capability, approved adapter, or framework extension that cannot be satisfied by existing catalog capability. |
| Framework Owns Common Concerns | Receiving, correlation, session, security, classification, parsing, validation, idempotency, concurrency, audit, observability, eventing, error handling, response shaping, model routing, and guardrails are framework concerns. |
| Business Logic Is Isolated | Business logic belongs in STP-BUS-* functions, rules, DMN tables, OPA policies, or bounded-context services. It must not appear in controllers, adapters, repositories, UI code, AI prompts, or orchestration glue. |
| Fail-Safe, Not Fail-Open | If identity, classification, authorization, policy, guardrail, runtime configuration, audit, or evidence control is unavailable, protected action must stop or route to human review. |
| AVCI Always | Every artifact and execution has owner, source, classification, validation evidence, and improvement path. |

# 6. Runtime Lifecycle and Activation Governance

Figure 2. MicroFunction lifecycle from intake to activation and improvement

AIRA treats MicroFunction configuration as governed engineering source. A transaction definition, step binding, parameter set, policy binding, retry profile, error policy, compensation profile, AI route, guardrail reference, and activation status must be versioned, reviewed, tested, classified, and promoted through controlled change. Configuration is not an informal administrative shortcut.
| Lifecycle State | Entry Criteria | Exit Criteria |
| --- | --- | --- |
| Draft | Controlled intake exists with owner, source, bounded context, classification, and expected outcome. | Design record complete; applicable controls selected; candidate artifacts generated or updated. |
| For Validation | Configuration/code/policy/test/migration candidates exist in branch or sandbox. | Publish-time gates pass or findings are returned to draft. |
| For Review | Validation evidence, PR/MR summary, rollback path, and reviewer assignments exist. | Maker-checker/CODEOWNERS/ARB/CAB decisions recorded. |
| Approved | Human approval completed for the risk tier and environment. | Activation requested through CI/CD and runtime control path. |
| Active | Signed RuntimeProcessDefinition is available; caches invalidated; config.changed event emitted. | Runtime monitoring confirms safe operation or deactivation/supersedence occurs. |
| Superseded / Rolled Back / Retired | New version, rollback, compensation, or retirement plan approved. | Evidence proves safe transition and retention obligations are met. |

# 7. Standard Step Category Baseline
| Step Category | Purpose | Mandatory Treatment |
| --- | --- | --- |
| STP-RCV | Receive trigger | Accept approved REST, Kafka, webhook, batch, file, scheduled, workspace, or AI action trigger through thin adapters only. |
| STP-COR | Correlation | Create or propagate trace_id, request_id, correlation_id, causation_id, and evidence_ref. |
| STP-SES | Actor/session/tenant | Resolve human, service, agent, tenant, role, skill, branch/unit, channel, and trust context. |
| STP-RATE | Rate/quota | Apply API, tenant, user, workflow, and AI budget throttles where applicable. |
| STP-SEC / STP-CLS | Security and classification | Authenticate, authorize, classify, and evaluate RBAC/ABAC/SBAC/OPA inputs before business logic. |
| STP-PRS / STP-NRM | Parse and normalize | Parse payload, normalize input, and reject unsafe or malformed values. |
| STP-VAL | Validation | Apply schema, domain, rule, DMN, and policy validation. |
| STP-IDP / STP-CON | Idempotency and concurrency | Reserve dedupe keys, prevent duplicate mutation, and apply locking/concurrency controls. |
| STP-CFG / STP-CAC | Configuration and cache | Resolve active config and derivative cache; cache loss must not change correctness. |
| STP-BUS / STP-RUL | Business logic/rules | Execute bounded-context business operation or approved decision rule. |
| STP-DB | Persistence | Persist state through approved repository/port and Flyway-governed schema only. |
| STP-AUD / STP-HIS | Audit and history | Write immutable step evidence and business history where required. |
| STP-EVT | Outbox/event | Write transactional outbox and publish schema-managed CloudEvents/Kafka events through approved paths only. |
| STP-AIR / STP-GRD / STP-AIM | AI/RAG/guardrails/model route | Retrieve eligible evidence, apply guardrails, invoke approved LiteLLM/model gateway alias, and produce safe grounded response. |
| STP-GOV | Human approval/governance | Start Flowable or approved workflow for high-risk, exception, or maker-checker tasks. |
| STP-OBS | Observability | Emit OpenTelemetry-aligned trace, metric, log, SLO, and audit evidence without sensitive data. |
| STP-RSP / STP-ERR / STP-CMP | Safe response, error, compensation | Return safe output, classify failures, route retry/DLQ/compensation/human review as configured. |

# 8. Cross-Cutting Capability Coverage Matrix
| Capability Area | Mandatory MicroFunction Treatment | Minimum Evidence |
| --- | --- | --- |
| DevSecOps, Security Gates, Evidence Pack, GitNexus | Every MicroFunction change passes repository controls, CODEOWNERS, CI/CD, unit/component/contract tests, policy checks, SAST/SCA/secret scan, architecture fitness, evidence pack generation, and GitNexus read-only impact analysis where available. | Build/test reports, scan reports, policy decisions, architecture fitness results, GitNexus impact summary, PR/MR AVCI summary, reviewer approval, rollback path. |
| OpenAPI, AsyncAPI, Kafka, Avro/JSON Schema, CloudEvents, Outbox, DLQ, Replay | Boundary-crossing interactions are contract-first. Event flows use approved topics, schema registry governance, transactional outbox, idempotent consumers, DLQ handling, replay controls, and versioned event metadata. | Contract lint, compatibility result, schema evolution approval, outbox records, idempotency tests, DLQ/replay tests, event trace. |
| Observability, Log4j2, OpenTelemetry, Sentry, Loki, Tempo, Grafana | Critical steps emit classification-safe logs, traces, metrics, audit, error-monitoring events, and dashboard-ready signals. Non-essential diagnostics may be tuned by policy; mandatory audit/security/evidence signals remain enabled. | Trace ID, span ID, Log4j2 config, OTel traces, Sentry issue link, Loki query, Tempo trace, Grafana panel, redaction test. |
| Concurrency, Heavy Transaction, Idempotency, Outbox, Resilience Lab | State-changing functions are retry-safe, duplicate-safe, concurrency-safe, heavy-load-aware, and failure-aware. Designs cover locking, transaction boundary, timeout, retry, circuit breaker, bulkhead, compensation, DLQ, and replay behavior. | Concurrency/load/idempotency/replay tests, outbox delivery evidence, failure injection result, compensation evidence. |
| Auto-Heal, Auto-Learn, Auto-Improve Candidate Loop | Runtime and engineering evidence may trigger issue detection, evidence retrieval, RCA, candidate fix, candidate learning, tests, prompt improvement, or backlog proposal. AI remains advisory or draft-only unless policy and approval allow bounded action. | Issue record, evidence bundle, candidate proposal, test impact, OPA/SBAC decision, human checker decision, risk tier, rollback/safe-disable path. |
| Security, Abuse Cases, Authenticated DAST, Secure APIs, Secrets Hygiene | Design covers threat and abuse cases, secure API patterns, OPA/SBAC expansion, classification handling, authentication context, authorization decisions, secret-safe execution, authenticated DAST, and remediation evidence where applicable. | Threat/abuse checklist, Rego tests, authenticated DAST, ASVS-aligned evidence, secret scan, remediation ticket, retest result, waiver if applicable. |

# 9. STP-BUS-* Isolation and Extension Rules

Belongs to exactly one bounded context and has an explicitly named owner.

Consumes typed input and returns typed result through the MicroFunction contract; raw maps and god-context objects are prohibited unless formally approved.

Does not construct HTTP responses, publish Kafka events, write audit records, call model providers, manipulate cache directly, or write across context boundaries.

Uses domain ports for persistence and external calls; adapters implement infrastructure details outside the business function.

Includes tests for success, invalid input, authorization failure, downstream failure, retry/idempotency, and boundary conditions as applicable.

Documents reversibility: no action needed, compensation, forward-fix, reprocess, manual review, or formal non-compensatable risk acceptance.

# 10. Contract, Event, Workflow, and AI Integration Rules
| Area | Mandatory Rule |
| --- | --- |
| API | REST boundaries use OpenAPI, typed error responses, idempotency headers where applicable, classification-safe payloads, and contract tests. |
| Events | Async boundaries use AsyncAPI, CloudEvents metadata, approved Kafka topic naming, schema registry governance, Avro/JSON Schema compatibility, and replay-safe consumers. |
| Outbox | State changes that emit events use transactional outbox. Direct publish from STP-BUS is prohibited. |
| Workflow | Temporal is for durable machine workflow and sagas. Flowable is for human approval, exception review, and governance tasks. MicroFunctions must not blur these boundaries. |
| AI/RAG | No direct model-provider SDK calls. All model traffic uses approved gateway/model aliases, guardrails, retrieval eligibility, audit, and output validation. |
| Dynamic Workspace | Frontend components and templates are not business authority. UI actions invoke backend-governed MicroFunction capability bindings and receive safe, policy-filtered responses. |

# 11. Runtime Evidence Envelope

Figure 3. Runtime evidence envelope and trace reconstruction model
| Field | Required Meaning |
| --- | --- |
| txn_code | Transaction or runtime process code. |
| step_code | Catalog step code such as STP-SEC, STP-VAL, STP-BUS, STP-AIR, STP-CMP. |
| execution_id | Unique execution instance. |
| configuration_version | Runtime configuration version used. |
| trace_id / span_id | Distributed trace correlation. |
| actor_ref / agent_id | Human, service, or AI-agent identity. |
| classification | Data classification and handling scope. |
| policy_decision_id | Authorization, classification, SBAC, or OPA decision. |
| idempotency_key_hash | Hash reference for mutation replay safety where applicable. |
| audit_event_id | Audit event emitted for protected or material action. |
| evidence_ref | Supporting evidence record. |
| outcome / error_code | Safe result status and stable error code. |
| duration_ms | Performance evidence. |
| compensation_ref | Compensation, rollback, or forward-fix evidence where applicable. |

# 12. Publish-Time Validation Gates
| Gate | Validation Rule | Evidence / Enforcer |
| --- | --- | --- |
| Completeness Gate | All mandatory step categories exist for the execution mode; no missing security, validation, error, audit, observability, or response path. | Configuration validator |
| Principle Gate | SOLID, Clean Architecture, DDD, ports/adapters, idempotency, observability, security, reversibility, and AVCI impact are declared and acceptable. | Fitness validator and reviewer |
| Security Gate | Classification ceiling, authorization policy, OPA rule, SBAC requirement, secrets handling, and redaction rules are present. | Security validator |
| Idempotency Gate | Mutating transactions declare idempotency key, dedupe, replay behavior, expiry, and conflict response. | Runtime validator |
| Error / Compensation Gate | Every step has error policy, retry policy, timeout, compensation posture, DLQ, or human escalation where required. | Error-policy validator |
| Observability Gate | Trace, metrics, logs, audit fields, and evidence references are configured without high-cardinality or sensitive labels. | Telemetry validator |
| AI Safety Gate | AI steps use approved model aliases, guardrail checkpoints, token budgets, classification route, Harness and approval where applicable. | AI governance validator |
| Test Gate | Unit, component, contract, negative, security, architecture, failure-path, idempotency, compensation, and regression tests exist or are linked. | CI evidence |
| Signature Gate | Activated runtime definitions are hashed, signed, versioned, immutable after activation, and reconstructable. | Definition signer |
| Cache Invalidation Gate | Activation emits config.changed event and invalidates Caffeine/Redis derived caches. | Runtime operations |

# 13. Runtime Toggle and Performance Protection Rules

Verbose diagnostic logging may be toggled at runtime when performance, incident analysis, or troubleshooting requires it; the change must create an audit record and must expire or be reviewed.

Trace sampling, non-essential debug enrichment, selected dashboard panels, and low-value telemetry labels may be adjusted by approved runtime configuration.

Mandatory audit events, security logs, policy decisions, classification labels, idempotency records, outbox records, critical error evidence, and evidence references must not be disabled by ordinary runtime toggles.

Runtime toggle changes must pass OPA/SBAC, be attributable to a human or approved service identity, carry classification, and include rollback or safe-disable instructions.

When telemetry is reduced for performance, trace reconstruction must still remain possible for critical paths through correlation IDs, audit records, evidence references, and sampled traces.

# 14. Architecture Fitness Functions and Quality Gates
| Fitness Function | Tool / Method | Blocks Merge When |
| --- | --- | --- |
| SOLID and package boundaries | ArchUnit, jQAssistant, dependency analysis | Domain depends on adapters, business code imports infrastructure, or cyclic dependencies exist. |
| No direct model/provider calls | Semgrep/import lint, dependency rules | Provider SDK imported outside approved gateway/adapter package. |
| No direct DB/Kafka/Redis from STP-BUS | ArchUnit/Semgrep | Business MicroFunction bypasses ports or framework envelope. |
| Contract integrity | OpenAPI/AsyncAPI/Avro compatibility tests | Endpoint, event, or error contract drifts without versioning. |
| OPA/SBAC policy | Rego unit tests and integration policy tests | Protected action can execute without allowed policy decision. |
| Idempotency and retry safety | Unit/component tests, mutation tests | Mutation path can double-post, retry unsafe action, or miss dedupe. |
| Determinism | Unit tests with fake clock/seed/environment | Tests rely on real time, random, filesystem, network, or uncontrolled state. |
| Reversibility | Migration tests, compensation tests, feature-flag disable tests | No rollback, forward-fix, compensation, or disable path exists for material change. |
| Observability | OpenTelemetry instrumentation and log redaction tests | Trace context missing or sensitive data appears in logs/traces. |

# 15. System Builder and AI-Assisted MicroFunction Generation Boundary

The System Builder may accelerate MicroFunction design and generation, but it is not authority. It may classify intake, analyze existing contracts, recommend options, draft configuration, generate candidate code, propose tests, produce policy or migration drafts, and prepare evidence. It must not approve its own output, activate runtime definitions, bypass OPA/SBAC, route around Harness, commit directly to protected branches, mutate production, or weaken classification and audit controls.
| Generated Output | Required Boundary |
| --- | --- |
| Candidate transaction definition | Draft only until validation gates and human approval complete. |
| Candidate STP-BUS code | Must use typed contracts, bounded context ownership, ports/adapters, tests, and PR/MR review. |
| Candidate OPA/Rego policy | Must include allow/deny tests, abuse cases, negative tests, and security review. |
| Candidate Flyway migration | DBA/architecture approval and migration evidence required before promotion. |
| Candidate API/event contract | OpenAPI/AsyncAPI/schema compatibility evidence required before code generation and consumer impact. |
| Candidate Auto-Heal action | Proposal-only unless action tier, OPA/SBAC, Harness path, risk gate, and human approval permit bounded execution. |

# 16. Required Evidence Pack
| Evidence Category | Required Content |
| --- | --- |
| Design Evidence | Ticket/intake, owner, bounded context, transaction intent, architecture impact, ADR/TDL where material. |
| Configuration Evidence | Transaction definition, step bindings, parameters, version, classification ceiling, activation status, validator output. |
| Code Evidence | STP-BUS or adapter source, typed contracts, dependency inversion proof, package-boundary proof, reviewer ownership. |
| Test Evidence | Unit, component, contract, policy, architecture, security, failure-path, idempotency, compensation, regression, AI guardrail, and resilience tests as applicable. |
| Security Evidence | OPA decision, SBAC skill, classification, secrets handling, redaction scan, SAST/SCA/secret scan, authenticated DAST where applicable. |
| Operational Evidence | Trace/log/metric/audit correlation, outbox evidence, DLQ/replay evidence, SLO/error signals, dashboard link. |
| Release Evidence | PR/MR AVCI summary, CI run, SBOM/provenance, waiver state, rollback/forward-fix/disable path, approval records. |
| Improvement Evidence | Known limitations, backlog items, Auto-Heal/Auto-Learn/Auto-Improve candidate records, review cadence. |

# 17. EDP-01 to EDP-20 MicroFunction Enforcement Map
| ID | Principle | Mandatory MicroFunction Enforcement |
| --- | --- | --- |
| EDP-01 | SOLID | Each MicroFunction, standard step, adapter, policy, prompt, and agent-assisted action has one clear responsibility, focused interface, and dependency-inverted implementation. |
| EDP-02 | Clean Architecture | Business and use-case logic must not depend on controllers, UI, database clients, Kafka clients, model providers, workflow engines, DevSecOps tools, or provisioning providers. |
| EDP-03 | DDD / Bounded Contexts | MicroFunctions operate inside an owning bounded context and must not write across another domain boundary without a contract, event, workflow, or approved integration pattern. |
| EDP-04 | Ports and Adapters | OpenAPI, AsyncAPI, Kafka, Avro, CloudEvents, database, cache, AI gateway, evidence store, and observability interactions occur through explicit ports and adapters. |
| EDP-05 | DRY, KISS, YAGNI | Reuse catalog steps and configuration before writing new code. Do not create speculative MicroFunctions, duplicated plumbing, or one-off shortcuts. |
| EDP-06 | Idempotency by Design | Retries, replays, callbacks, outbox publishing, consumers, tool actions, and recovery operations must be duplicate-safe and replay-safe. |
| EDP-07 | Determinism and Reproducibility | Runtime assembly, migrations, contracts, tests, model routes, environments, and evidence must be reproducible from approved source, configuration, and versioned manifests. |
| EDP-08 | Fail-Safe, Not Fail-Open | If identity, policy, guardrail, audit, evidence, model gateway, contract, schema registry, or provisioning control fails, protected actions stop safely. |
| EDP-09 | Human-in-the-Loop | High-impact, production-impacting, low-confidence, Restricted, destructive, or policy-exception transactions require named human approval and evidence. |
| EDP-10 | Least Privilege / SBAC | Human actors, services, System Builder, and AI agents receive only the approved skill, role, tool, data, environment, and transaction scope required. |
| EDP-11 | Separation of Duties | Maker, checker, approver, deployer, operator, agent owner, and auditor duties remain separated for high-risk or production-bound MicroFunction changes. |
| EDP-12 | Observability by Design | Critical paths emit logs, metrics, traces, audit events, error-monitoring signals, dashboard references, and evidence records with safe redaction. |
| EDP-13 | Policy as Code | Authorization, admission, routing, guardrails, deployment, data handling, tool actions, runtime toggles, and exception rules are versioned policy artifacts. |
| EDP-14 | Testability by Design | MicroFunctions, configurations, contracts, adapters, policies, workflows, prompts, and provisioning manifests are independently testable with deterministic fixtures. |
| EDP-15 | Secure by Design | Threat controls, abuse cases, secrets hygiene, tenant isolation, classification handling, supply-chain controls, secure APIs, and secure defaults are built in. |
| EDP-16 | Resilience Patterns | Timeouts, retries, circuit breakers, bulkheads, fallback, DLQ, compensation, recovery, replay, and rebuild paths are explicit and tested. |
| EDP-17 | Architectural Fitness Functions | Automated checks verify boundaries, dependencies, contracts, schema evolution, security, policies, agents, provisioning, evidence, and observability requirements. |
| EDP-18 | Progressive Autonomy | Automation advances only when evidence, trust score, skill, risk tier, guardrails, approval, and rollback controls support it. |
| EDP-19 | Reversibility / Rollbackability | Changes support rollback, forward-fix, compensation, feature disablement, runtime deactivation, environment rebuild, or safe decommissioning. |
| EDP-20 | AVCI | Every artifact and runtime action remains attributable, verifiable, classifiable, and improvable across its lifecycle. |

# 18. Anti-Patterns and Rejection Rules
| Anti-Pattern | Example | Required Response |
| --- | --- | --- |
| Hardwired orchestration | Transaction sequence coded in controller/service instead of governed configuration. | Reject; move sequence to transaction definition and standard step bindings. |
| Business logic in adapters | Rules hidden in controller, repository, Kafka consumer, UI, prompt, or integration adapter. | Reject; move to STP-BUS, DMN/rule, or OPA policy. |
| Direct infrastructure calls from STP-BUS | STP-BUS calls database driver, Kafka, Redis, OpenKM, Keycloak, model SDK, or external API directly. | Reject; use domain ports and adapters. |
| Missing error/compensation path | Mutating step has no retry, timeout, idempotency, compensation, safe response, or DLQ/human review decision. | Block activation. |
| Cache as authority | Redis/Valkey or Caffeine value becomes source of truth. | Reject; cache is derivative only. |
| AI as authority | AI summary, prompt, model answer, or agent recommendation changes access, workflow, schema, production state, or policy directly. | Block; route through Harness/SBAC/OPA/human approval. |
| Evidence after the fact | Manual reconstruction of evidence after code/config already changed. | Reject; evidence must be produced by the system of work. |

# 19. RACI and Operating Responsibilities
| Activity | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Approve parent framework | Enterprise Architecture | Architecture Board / IT Head | DevSecOps, Security, Development, QA, DBA | Engineering and Internal Audit |
| Maintain catalog | Platform Engineering / MicroFunction Owner | Software Development Lead | Architecture, QA, Security | Developers |
| Approve STP-BUS function | Domain Lead | Development Lead | Architecture, QA, Security | Product Owner, Internal Audit |
| Validate configuration activation | DevSecOps / QA | Platform Engineering Lead | Security, DBA, SRE | Release stakeholders |
| Approve production-impacting change | Change Owner | CAB | Architecture, Security, QA, SRE | Affected teams |
| Promote Auto-Learn knowledge | Knowledge Steward | Domain Owner | Architecture, Security, QA | Developers and AI users |

# 20. Acceptance Criteria

The revised MicroFunction Framework is approved as the parent authority for 10A, 10B, 10C, 10D, and 10E.

Developers can explain and apply the configure-first rule without ambiguity.

Standard step categories, cross-cutting capability coverage, and STP-BUS isolation rules are reflected in code-generation prompts and System Builder templates.

Publish-time validation gates are machine-checkable or reviewer-checkable and linked to PR/MR evidence.

Runtime evidence envelope fields are available for audit, observability, incident response, trace reconstruction, and Auto-Learn candidate generation.

All MicroFunction changes have tests, security/policy validation, architecture fitness results, and rollback/forward-fix evidence.

Runtime toggles preserve mandatory security, audit, policy, classification, idempotency, outbox, and evidence signals.

Companion documents are updated in correct dependency order without becoming competing authorities.

# 21. MicroFunction Family Review Queue

Figure 4. Corrected MicroFunction family review queue
| Seq | Document | Current Treatment | Recommended Action |
| --- | --- | --- | --- |
| 13 | 10-AIRA_MicroFunction_Framework | Completed / revised as v3.4 candidate | Use as parent authority pending ARB/CAB approval. |
| 14 | 10A-AIRA_MicroFunction_Design_and_Development_Guide | Next for review | Align developer design procedure, design record template, applicability matrix, STP-BUS design rules, and evidence checklist. |
| 15 | 10B-AIRA_MicroFunction_Framework_Implementation_Standard | Pending after 10A | Translate parent rules into concrete runtime implementation, package boundaries, adapters, tests, and CI/CD gates. |
| 16 | 10C-AIRA_MicroFunction_Sequence_Diagrams_and_Mermaid_Reference | Pending after 10B | Update sequence diagrams and Mermaid governance to match v3.4 standard steps and evidence envelope. |
| 17 | 10D-AIRA_MicroFunction_Standard_Function_Catalog_and_Assembly_Templates | Pending after 10C | Update catalog, templates, step prefixes, and assembly patterns. |
| 18 | 10E-AIRA_MicroFunction_Backend_Service_Generation_and_Runtime_Configuration_Standard | Pending after 10D | Update System Builder/code generation and runtime configuration standards. |

# 22. Open Reconciliation Items
| Item | Severity | Required Resolution |
| --- | --- | --- |
| Source v3.3 candidate referred to 01 v3.3, 06 v3.3, and 07 v3.3 candidates, while current verified outputs in this workstream are 01 v3.2, 06 v3.2, and 07 v3.2. | Medium | Register 00D / Revision Control Matrix must record final target numbering before source-pack regeneration. |
| Source v3.3 candidate marked 08, 08A, and 09 as completed/revised, but these files are not verified in the current uploaded sequence. | Medium | Verify aligned folder or regenerate later; do not claim completion until artifact is present. |
| Source review queue text said next review remains 10B even though 10A is listed as next for review. | High | Corrected: 10A is next, then 10B. |
| Known AIRA numbering conflicts remain: 11A duplicate numbering and 41B/44 System Builder overlap. | Medium | Track in 00D and Revision Control Matrix v1.3 or later. |

# 23. Change Log
| Version | Summary |
| --- | --- |
| v3.1 | Previous aligned baseline with Enterprise Design Principles, SOLID enforcement, Java 25 alignment, and MicroFunction governance. |
| v3.3 Candidate | Added cross-cutting DevSecOps, eventing, observability, concurrency, resilience, security, and continuous-improvement coverage. |
| v3.4 Revised | Corrects version/status drift, incorporates cross-cutting coverage into the parent framework, strengthens runtime evidence envelope, fixes review queue sequence, and aligns to current foundation outputs. |

# 24. External Reference Note

External references are supplemental validation sources only and do not override AIRA source governance. They support the current interpretation of observability, event metadata, policy-as-code, workflow retry semantics, secure software development, application security verification, and supply-chain evidence expectations. Applicable reference families include OpenTelemetry, CloudEvents, Open Policy Agent, Temporal retry and workflow guidance, NIST SSDF, OWASP ASVS, and SLSA.

# 25. AVCI Compliance Summary
| AVCI Property | Evidence in This v3.4 Revision |
| --- | --- |
| Attributable | Identifies owner, co-owners, source document, companion documents, target audience, review queue sequence, RACI, and PR/MR ownership expectations. |
| Verifiable | Defines publish-time gates, architecture fitness functions, tests, runtime evidence envelope, CI evidence, trace reconstruction, and acceptance criteria. |
| Classifiable | Requires classification ceilings, handling rules, model-route eligibility, log/cache/event redaction, Restricted-data controls, and non-disableable classification evidence. |
| Improvable | Defines Auto-Heal, Auto-Learn, Auto-Improve, AutoResearch, improvement backlog, review cadence, open reconciliation items, and next review queue item. |

