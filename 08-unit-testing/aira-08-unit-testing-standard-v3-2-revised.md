---
title: "Unit Testing Standard"
doc_id: "AIRA-08"
version: "v3.2"
status: "revised"
category: "Unit testing"
source_docx: "AIRA_08_Unit_Testing_Standard_v3.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 08-unit-testing
  - revised
  - aira-08
---



# Unit Testing Standard



AIRA
AI-Native Enterprise Platform

Unit Testing, Quality Engineering, and Evidence Standard

AIRA-DOC-008 | v3.2 Revised

Unit Tests | Component Tests | Contract Tests | Mutation Quality | Policy Tests | MicroFunction Evidence | Resilience Lab
| Property | Value |
| --- | --- |
| Document ID | AIRA-DOC-008 |
| Canonical Filename | AIRA_08_Unit_Testing_Standard_v3.2_Revised.docx |
| Version | v3.2 Revised |
| Supersedes | 08-AIRA_Unit_Testing_Standard_v3.1_Aligned.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | FOR ARCHITECTURE REVIEW BOARD / QA / DEVSECOPS APPROVAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | QA/SDET Lead; Software Development Lead; DevSecOps Lead; Security Architecture; Platform Engineering; AI Engineering; Internal Audit |
| Primary Companions | 01/01A AVCI and Enterprise Architecture; 08A Maker-Checker Prompt; 11/20 DevSecOps and Evidence; 23B Fitness Catalog; 52 Dynamic Workspace Testing; 10/10A-10D MicroFunction; 15 API; 16 Database/Flyway; 17 Security; 31A Observability; 42D-42S AI Agent Governance |
| Review Cadence | Quarterly; unscheduled after material technology, security, AI-risk, testing, CI/CD, MicroFunction, policy, or evidence change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Quality-Engineering / Unit-Testing / v3.2/ |

# Mandatory Practice Statement

AIRA tests are executable governance evidence, not optional quality accessories. No production-bound source code, configuration, MicroFunction, API, event schema, database migration, policy, AI agent, Dynamic Workspace component, or System Builder-generated artifact is ready for promotion unless its expected behavior, boundary constraints, security posture, failure paths, observability, reversibility, and AVCI evidence are proven through deterministic tests and CI/CD evidence gates.

AI may help draft, run, inspect, and improve tests. AI must not approve its own tests, suppress failing tests, weaken assertions, mark security defects as acceptable, merge changes, or promote artifacts. Maker-checker separation, CODEOWNERS review, QA/SDET accountability, Security review, and CAB/ARB gates remain mandatory where applicable.

# 1. Executive Summary

This v3.2 revision updates the AIRA Unit Testing Standard so the revised Architecture Fitness Function Catalog, Dynamic Workspace testing controls, PoC 1/1A/2 evidence gates, System Builder governance, and AI Agent Governance family become executable testing practice. It extends the earlier v3.1 unit testing discipline with stronger contract, policy, observability, mutation, resilience, AI-assisted maker-checker, and evidence-pack rules.
| Strategic Outcome | v3.2 Required Result |
| --- | --- |
| Tests as evidence | Every material change produces deterministic test evidence linked to ticket, branch, commit, PR/MR, reviewer, environment, classification, and evidence pack. |
| Architecture preservation | Tests verify SOLID, Clean Architecture, DDD, ports/adapters, MicroFunction boundaries, frontend non-authority, and direct-provider-call prohibitions. |
| Security and policy proof | OPA/SBAC/ABAC, RLS, classification, secrets hygiene, fail-closed, authenticated DAST, and safe-error paths are tested, not assumed. |
| Contract and event reliability | OpenAPI, AsyncAPI, Kafka, Avro, CloudEvents, outbox/inbox, idempotent consumers, DLQ, replay, and schema evolution have test coverage where applicable. |
| Resilience and reversibility | Retries, duplicate requests, concurrency, heavy transaction behavior, cache loss, rollback, compensation, safe disablement, and rebuild are covered by test scenarios. |
| Continuous improvement | Auto-Heal, Auto-Learn, and Auto-Improve may generate candidates only when failures, evidence, proposed fixes, tests, and human approval paths are traceable. |

# 2. Purpose, Scope, and Authority

## 2.1 Purpose

Define AIRA-wide testing expectations for unit, component, contract, policy, architecture, security, frontend, MicroFunction, database, event, observability, resilience, and AI-related tests.

Convert architecture principles and fitness functions into executable, CI/CD-verifiable test evidence.

Prevent superficial AI-generated tests, weak assertions, fixture leakage, skipped tests, and tests that validate only happy paths.

Establish the required evidence model for PR/MR, CI/CD, GitNexus, release-readiness, incident response, and continuous improvement loops.

## 2.2 In Scope and Out of Scope
| In Scope | Out of Scope |
| --- | --- |
| Backend Java 25 tests, Spring Boot component tests, ports/adapters tests, policy tests, OpenAPI/AsyncAPI contract tests, MicroFunction tests, Flyway/RLS tests, frontend React/Next.js tests, accessibility tests, and resilience tests. | Using production data, real customer PII, secrets, unrestricted documents, raw prompts, production credentials, or unmanaged external systems in tests. |
| AI-assisted test generation and review under Codex-maker / independent-checker / human-review control. | Autonomous merge, approval, deployment, suppression of failing tests, or production remediation by AI. |
| Evidence generation for test reports, coverage, mutation quality, trace/log redaction, GitNexus impact, DAST/SAST, and release packs. | Treating coverage percentage as sufficient proof without assertion quality, boundary testing, security testing, or evidence review. |

## 2.3 Authority
| Authority Level | Source / Control | Testing Meaning |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance | Final authority for production-impacting test waivers, residual risk acceptance, and release blockers. |
| L1 | 01 AVCI, 01A Architecture Principles, 02 Blueprint | Universal rules for evidence, design boundaries, fail-closed behavior, reversibility, and fitness evidence. |
| L1 | This AIRA-DOC-008 Standard | Canonical testing discipline for engineering, QA, CI/CD, and AI-assisted test generation. |
| L2 | 08A Maker-Checker Prompt; 23B Fitness Catalog; 52 Dynamic Workspace Testing | Execution companions that implement test workflows, gates, and scenario catalogs. |
| L3 | Repository tests, CI/CD reports, security scans, GitNexus reports, evidence packs | Operational proof for acceptance, release, audit, and improvement. |

# 3. v3.2 Change Summary
| Change Area | v3.2 Alignment |
| --- | --- |
| Architecture fitness | Adds explicit linkage to 23B fitness functions and makes architecture tests blocking for boundary, dependency, policy, and evidence failures. |
| MicroFunction coverage | Requires step-level tests for receive, correlate, session, classify, authorize, validate, idempotency, business execution, audit, outbox, observability, and failure handling. |
| Dynamic Workspace | Adds frontend non-authority tests, component props/schema tests, accessibility, visual regression, policy-filtered action tests, and telemetry checks. |
| API and event contracts | Adds OpenAPI/AsyncAPI compatibility, CloudEvents envelope, Avro/schema evolution, outbox/inbox, DLQ/replay, and idempotent-consumer tests. |
| Security testing | Adds OPA/SBAC/ABAC tests, RLS tests, authenticated DAST evidence, secrets hygiene checks, safe error tests, and abuse-case coverage. |
| Observability | Adds trace/log/metric/audit/evidence correlation tests and runtime telemetry toggle tests without disabling mandatory audit/security evidence. |
| AI-assisted testing | Strengthens Codex maker and independent checker roles; AI output remains draft until human review and CI evidence validation. |
| Resilience lab | Adds concurrency, duplicate request, retry, cache loss, downstream failure, heavy transaction, rollback, and compensation tests. |

# 4. Testing Taxonomy and Minimum Evidence

AIRA uses layered testing. A developer may not claim readiness by running only unit tests when the change crosses API, database, policy, AI, event, workflow, or frontend boundaries.
| Test Type | Required Use | Minimum Evidence |
| --- | --- | --- |
| Unit tests | Pure domain, use-case, validator, mapper, policy input builder, utility, and MicroFunction business step logic. | JUnit/Gradle or frontend test report; deterministic fixtures; assertion summary; changed-line coverage where feasible. |
| Component tests | Spring service slice, controller adapter, repository adapter, frontend component, widget shell, generated client adapter. | Mock/stub boundary proof; no direct infrastructure leakage; negative paths tested. |
| Contract tests | OpenAPI endpoints, Problem Details errors, generated clients, AsyncAPI messages, CloudEvents envelope, Avro schema compatibility. | Contract lint/report; request/response fixtures; compatibility result; versioning evidence. |
| Policy tests | OPA/Rego, SBAC, ABAC, classification ceilings, RLS expectations, field/action filtering. | Allowed/denied/escalated cases; negative tests; decision log sample. |
| Architecture tests | Package/layer boundaries, direct provider calls, direct DB access, frontend authority, framework dependency leaks. | ArchUnit/Semgrep/OPA result; failure blocks PR unless waived. |
| Security tests | Input validation, secrets, token/PII leakage, fail-closed paths, authenticated DAST, safe errors, abuse cases. | SAST/DAST/secrets reports; remediation evidence; waiver if not fixed. |
| Resilience tests | Timeouts, retries, duplicate requests, idempotency, cache loss, DLQ/replay, concurrent updates, heavy transactions. | Scenario result; evidence IDs; rollback/forward-fix proof. |
| Observability tests | Trace propagation, log redaction, metrics labels, audit records, evidence references, dashboard validation. | Trace export/screenshot, log-redaction test, metric/audit query, evidence record. |
| AI/evaluation tests | Guardrail behavior, model route classification, retrieval source eligibility, golden dataset, prompt safety, agent action blocking. | Eval report, guardrail result, model-route audit, blocked action evidence. |

# 5. Backend Java and MicroFunction Testing Standard

Java 25 LTS is the default backend test runtime. Java 21 is permitted only through a documented waiver with owner, risk, compatibility reason, compensating controls, and exit date.

JUnit Jupiter is the primary unit testing framework for Java services. Mockito or approved test doubles may be used only at explicit ports/adapters boundaries; do not mock the domain model to avoid testing behavior.

Testcontainers or equivalent approved ephemeral dependencies may be used for integration-style tests that require PostgreSQL, Kafka, Redis/Valkey, OpenSearch, or browser support, provided synthetic data and deterministic teardown are used.

Mutation testing through PIT or an approved equivalent is required for high-risk domain, policy-input, security, money, approval, identity, or MicroFunction business logic where practical.

Tests must prove fail-closed behavior when Keycloak, OPA, Vault/OpenBao, database, Kafka, workflow engine, model gateway, guardrail, audit, or evidence dependencies are unavailable.
| MicroFunction Step Family | Mandatory Test Coverage |
| --- | --- |
| Receive / correlate / session | Reject malformed input, preserve request_id/trace_id, resolve actor/tenant/channel, and block anonymous protected actions. |
| Classify / authorize | Apply classification ceiling, RBAC/ABAC/SBAC inputs, OPA allow/deny/escalate decisions, and safe response behavior. |
| Validate / idempotency | Validate schema and business invariants; duplicate callback, retry, replay, and concurrent request behavior must be duplicate-safe. |
| Business execution | Keep business logic inside the correct bounded context; prove no direct controller, frontend, DB, Kafka, Redis, or model-provider coupling. |
| Audit / outbox / observability | Emit append-only audit, transactional outbox, trace/log/metric/evidence records with redaction and classification. |
| Rollback / compensation | Prove rollback, safe disablement, feature flag, forward-fix, or compensation behavior for state-changing flows. |

# 6. Frontend, Dynamic Workspace, and Accessibility Testing

Frontend tests must prove that the UI renders, validates, explains, and requests actions safely. The frontend must never become business authority, authorization authority, workflow authority, policy authority, model-route authority, or data source of truth.

React/Next.js component tests must verify props schemas, loading states, empty states, error states, permission-denied states, retry-safe submit states, duplicate-click protection, and stale-data warnings.

Dynamic Workspace tests must verify policy-filtered layout resolution, component visibility, action binding, safe field redaction, runtime cache loss behavior, and evidence emission.

Accessibility testing must include keyboard operation, focus order, labels, screen-reader semantics, color/contrast acceptance, reduced motion, accessible drag/drop alternatives, and AI panel accessibility.

Visual regression tests must cover critical dashboards, approval screens, evidence views, and security states; snapshots must not contain secrets, tokens, raw PII, or real customer data.

Frontend tests must use generated clients or contract fixtures; they must not hardcode invented endpoints, fields, action codes, MicroFunction transaction names, or policy outcomes.

# 7. Contract, Event, Database, and Workflow Testing
| Control Area | Required Tests |
| --- | --- |
| OpenAPI and REST | Contract linting, generated client compatibility, Problem Details safe errors, idempotency header behavior, pagination/filtering, classification-safe redaction, and negative authorization cases. |
| AsyncAPI / Kafka / Avro | Producer/consumer contract tests, schema evolution compatibility, CloudEvents envelope validation, correlation/causation IDs, replay safety, and topic naming governance. |
| Outbox / Inbox / DLQ | Transactional outbox write with business transaction, idempotent consumer deduplication, DLQ routing, replay authorization, poison-message handling, and trace reconstruction. |
| Flyway / Database / RLS | Flyway validate, clean-migrate in non-prod, upgrade migration, seed determinism, rollback/forward-fix plan, RLS negative tests, and no manual DDL evidence. |
| Temporal / Flowable | Durable workflow retry/compensation, human approval maker-checker, escalation, timeout, cancellation, duplicate approval, and audit evidence tests. |

# 8. Security, Policy, Abuse-Case, and DAST Testing

Every protected action must include positive and negative tests for RBAC, ABAC, SBAC, classification, tenant/branch/unit, data ownership, and SoD constraints.

OPA/Rego tests must include ALLOW, DENY, ESCALATE/REQUIRE_APPROVAL, invalid input, stale policy bundle, missing identity, and classification-over-ceiling scenarios.

Authenticated DAST is required for production-bound web/API paths where authentication, session, access control, file upload, admin action, or Dynamic Workspace action is involved.

Secret scanning and log-redaction tests must prove that passwords, tokens, raw JWTs, private keys, raw PII, raw prompts, embeddings, account numbers, and unrestricted documents are not stored in test artifacts or evidence.

Abuse cases must be translated into tests for high-risk flows, including prompt injection, indirect tool action, replay, duplicate submission, privilege escalation, stale cache, hidden field tampering, and bypass of approval workflow.

# 9. Observability, Runtime Toggle, and Evidence Tests

Testing must prove not only that code works, but that behavior can be reconstructed. Traceability is part of correctness in AIRA.
| Evidence Signal | Test Requirement |
| --- | --- |
| Logs | Structured Log4j2 logs must be redacted, classification-safe, correlation-aware, and free of secrets/PII/raw prompts. |
| Traces | OpenTelemetry traces must link frontend/gateway/backend/MicroFunction/workflow/database/event/model/tool paths where applicable. |
| Metrics | Metrics must use bounded labels and support SLO/error-budget analysis without high-cardinality sensitive identifiers. |
| Sentry / errors | Error monitoring must capture safe diagnostic context without leaking customer data or secrets. |
| Loki / Tempo / Grafana | Dashboards and trace reconstruction must demonstrate how a reviewer can locate related logs, traces, audit records, events, and evidence references. |
| Runtime telemetry toggles | Sampling/debug toggles may reduce non-critical diagnostic volume, but tests must prove mandatory audit, security, policy-decision, evidence, and protected-action telemetry cannot be disabled casually. |

# 10. AI-Assisted Maker-Checker Testing Workflow

The 08A companion standard remains the execution playbook for two-loop AI-assisted testing. This parent standard defines the mandatory control expectations.
| Actor / Loop | Allowed Role | Required Evidence |
| --- | --- | --- |
| Codex / Maker | Inspect repository, identify test gaps, draft or improve tests, run permitted commands, summarize evidence and remaining gaps. | Maker report with changed files, commands, test output, coverage/mutation result if applicable, and known gaps. |
| Independent Checker | Challenge weak assertions, detect missing negative tests, verify determinism, security, classification, architecture boundaries, and evidence completeness. | Checker verdict with accepted/rejected tests, added cases, unresolved findings, and escalation items. |
| Human Reviewer / QA | Approve meaning, sufficiency, risk treatment, CI/CD evidence, and readiness. | PR/MR review, CODEOWNERS approval, QA/Security/Architecture sign-off where required. |

AI-generated tests must not be accepted merely because they increase coverage. They must validate meaningful behavior, failure paths, security boundaries, and evidence requirements.

AI may not mark tests as skipped, weaken assertions, disable policies, alter production configuration, approve PRs, or suppress findings.

Repeated AI-generated test weaknesses must create improvement backlog items for prompt standards, unit testing prompts, repository rules, or fitness functions.

# 11. Coverage, Mutation, and Quality Thresholds

AIRA uses thresholds as decision aids, not blind release authority. Lower-risk code may use agreed minimums; high-risk code requires stronger branch/change evidence, mutation quality, negative tests, and reviewer sign-off.
| Risk Class | Minimum Expectation |
| --- | --- |
| Low-risk utility or UI display | Relevant unit/component tests, no secrets, no architecture drift, CI pass, and reviewer acceptance. |
| Business, workflow, policy, or MicroFunction logic | Changed-line coverage, negative tests, idempotency/failure tests, policy tests where applicable, and architecture gate pass. |
| Identity, access, money, legal, Restricted, production-impacting, or irreversible actions | Strong unit/component/contract/policy/security tests, mutation quality signal, authenticated DAST where applicable, rollback/compensation proof, and named human approval. |
| AI agent, model route, retrieval, tool action, or System Builder generation | Golden dataset or eval test, guardrail test, route/classification test, tool-denial test, audit evidence, and human approval before activation. |

# 12. CI/CD Gates and PR/MR Evidence Pack

CI/CD must reject production-bound changes when mandatory test evidence is missing, stale, synthetic-data unsafe, classification unsafe, or inconsistent with the declared change scope.

Required PR/MR evidence includes ticket/task, owner, branch, commit, AI tools used, test commands, test reports, coverage/mutation result, security scan result, policy check result, architecture fitness result, GitNexus impact, rollback/forward-fix plan, classification handling, and known limitations.

Skipped tests must include owner, reason, risk, expiry date, follow-up ticket, and approver. Indefinite skipped tests are not allowed for production-bound high-risk controls.

Flaky tests must be quarantined only through a tracked defect with owner and deadline; quarantine cannot hide security, access-control, migration, data-loss, or audit failures.

Evidence packs must be retained in approved evidence stores and projected to Obsidian/LLM Wiki only as curated summaries or links, not as uncontrolled full-source duplication.

# 13. Auto-Heal, Auto-Learn, and Auto-Improve Test Controls
| Loop | Testing Rule |
| --- | --- |
| Auto-Heal | May propose or draft remediation only after failure signal, affected test set, risk classification, rollback plan, and human approval path are captured. It must not silently patch production. |
| Auto-Learn | May generate knowledge candidates only after tests/evidence prove the lesson; knowledge remains draft until review and retrieval eligibility approval. |
| Auto-Improve | May propose refactoring, new tests, new policies, or fitness checks only if architecture, security, observability, reversibility, and AVCI are preserved or improved. |

# 14. RACI
| Activity | Developer | QA/SDET | DevSecOps | Security | Architecture | DBA/Platform | Product / Owner |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Define test approach | R | A/R | C | C | C | C | C |
| Implement unit/component tests | A/R | C | C | C | C | C | I |
| Implement contract/policy/security tests | R | A/R | C | A/R | C | C | I |
| Run CI/CD, coverage, mutation, evidence gates | R | C | A/R | C | C | C | I |
| Review architecture fitness failures | C | C | C | C | A/R | C | I |
| Approve security test waivers | I | C | C | A/R | C | C | I |
| Approve release test evidence | C | A/R | A/R | R | R | C | A |

# 15. Acceptance Criteria

All changed production-bound code/configuration has deterministic tests appropriate to risk and impact.

Architecture fitness gates pass or have approved, time-bound waiver with compensating controls.

Security, policy, classification, secrets, safe-error, and fail-closed tests pass for protected paths.

Contract, event, Flyway/RLS, outbox/DLQ/replay, workflow, and MicroFunction tests run where impacted.

Frontend tests prove non-authority, safe state handling, accessibility, policy filtering, and telemetry where impacted.

Observability and evidence tests prove trace/log/metric/audit/evidence correlation without sensitive leakage.

Mutation or equivalent assertion-quality evidence exists for high-risk logic or a documented deferral is approved.

AI-assisted test generation has maker-checker evidence and named human review.

CI/CD evidence pack links tickets, commits, tests, scans, GitNexus, approvals, rollback/forward-fix, and known limitations.

Auto-Heal, Auto-Learn, and Auto-Improve outputs remain candidate-only until tests, evidence, and human approval are complete.

# 16. Source Alignment and External Reference Register
| Reference | Alignment Use |
| --- | --- |
| AIRA 01A Enterprise Architecture Principles | Establishes architecture fitness, System Builder hard gates, and evidence discipline inherited by testing. |
| AIRA 08A AI-Assisted Unit Testing Maker-Checker Prompt Standard | Defines Codex maker and independent checker workflow used by this parent standard. |
| AIRA 23B Architecture Fitness Function Catalog | Supplies executable architecture and policy gates that unit/testing practice must implement. |
| AIRA 52 Dynamic Workspace Testing and Architecture Fitness Function Standard | Supplies frontend, accessibility, Dynamic Workspace, and widget test expectations. |
| JUnit Jupiter / JUnit Platform | Primary Java unit testing framework family for backend tests. |
| Mockito | Approved mocking/test-double framework at explicit ports/adapters boundaries. |
| PIT Mutation Testing | Mutation quality signal for Java/JVM tests where practical. |
| Testcontainers for Java | Ephemeral dependency testing for databases, brokers, browsers, and integration-style scenarios where needed. |

# 17. AVCI Compliance Summary
| AVCI Property | Evidence in This Standard |
| --- | --- |
| Attributable | Defines owners, co-owners, roles, PR/MR evidence, maker-checker records, CI/CD reports, and named human accountability. |
| Verifiable | Defines executable test evidence across unit, component, policy, contract, security, architecture, observability, resilience, and AI/eval domains. |
| Classifiable | Requires synthetic data, classification-safe fixtures, redaction, forbidden telemetry prevention, and evidence handling rules. |
| Improvable | Converts weak assertions, missing tests, flaky tests, recurring defects, and AI test gaps into reviewed backlog and controlled improvement candidates. |

