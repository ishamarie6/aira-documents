---
title: "PoC2 Testing Architecture Fitness OPA SBAC Policy and Regression Gate Pack"
doc_id: "AIRA-45H"
version: "v1.0"
status: "draft"
category: "PoC2 and mortgage experience"
source_docx: "AIRA_45H_PoC2_Testing_Architecture_Fitness_OPA_SBAC_Policy_and_Regression_Gate_Pack_v1.0_Draft.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 45-poc2-mortgage-experience
  - draft
  - aira-45h
---



# PoC2 Testing Architecture Fitness OPA SBAC Policy and Regression Gate Pack



AIRA

AI-Native Enterprise Platform

PoC 2 Testing, Architecture Fitness, OPA/SBAC Policy, and Regression Gate Pack

v1.0 Draft
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-045H |
| Canonical Filename | AIRA_45H_PoC2_Testing_Architecture_Fitness_OPA_SBAC_Policy_and_Regression_Gate_Pack_v1.0_Draft.docx |
| Version | v1.0 Draft |
| Status | Draft for Architecture / DevSecOps / Security / QA-SDET / SRE / DBA / AI Governance / Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; DevSecOps Lead; Software Development Lead; Security Architecture; QA/SDET; DBA/Data Governance; Platform Engineering; SRE/Operations; AI Governance; Internal Audit |
| Primary Audience | Software Developers; DevSecOps Engineers; QA/SDET; Security; DBA; Platform Engineering; SRE; AI Governance; Internal Audit; System Builder Operators |
| Primary Parents | AIRA-DOC-042C; AIRA-DOC-045; AIRA-DOC-045A; AIRA-DOC-004; AIRA-DOC-011/011A/020; AIRA-DOC-019; AIRA-DOC-031/031A; AIRA-DOC-063-068 |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / PoC2-DevSecOps-System-Factory / AIRA-DOC-045H / v1.0 / |
| Approval Path | Draft -> Architecture / DevSecOps / Security / QA / SRE / DBA / AI Governance / Internal Audit review -> PoC 2 controlled execution -> Exit Review -> Register update |
| Supersedence Rule | Companion document only. Does not supersede AIRA-DOC-045. It operationalizes PoC 2 execution controls and must be registered if adopted. |
| Mandatory Practice Statement |
| --- |
| PoC 2 testing is not complete when unit tests pass. It is complete only when unit, component, integration, contract, policy, architecture-fitness, security, and regression gates produce reviewable evidence; PoC 1 and PoC 1A behavior remains preserved; fail-open policy behavior is blocked; and every material gap has an owner, waiver decision, remediation path, and AVCI evidence. |

# Table of Contents Placeholder

Insert a Microsoft Word automatic Table of Contents before controlled publication: References > Table of Contents > Automatic Table. Update all fields before release.

# 1. Executive Summary

This companion pack defines the testing, architecture fitness, OPA/SBAC policy, and regression gates required for AIRA PoC 2. It converts the PoC 2 System Factory baseline into executable quality controls so that future AIRA changes are not accepted merely because a pipeline completes. Each PR/MR must prove functional correctness, security-policy correctness, architecture-boundary correctness, and regression preservation with durable evidence.

The pack is intentionally strict. PoC 2 must prove that AIRA can block unsafe changes automatically, preserve PoC 1 and PoC 1A login behavior, enforce Clean Architecture and ports/adapters boundaries, reject fail-open policy behavior, and produce evidence that reviewers can inspect independently.

# 2. Purpose, Scope, and Authority
| Area | In Scope | Out of Scope |
| --- | --- | --- |
| Testing gates | Unit, component, integration, Testcontainers, contract, policy, architecture, regression, smoke, and security validation gates. | One-time manual testing that cannot be replayed in CI/CD or evidenced. |
| Architecture fitness | SOLID, Clean Architecture, DDD, dependency direction, ports/adapters, no direct infrastructure shortcuts, no direct model calls. | Using architecture checks as advisory only while allowing blocked patterns to merge. |
| Policy gates | OPA/SBAC allow, deny, escalate, fail-closed, classification ceiling, maker-checker, separation-of-duties, and reviewer-role tests. | Hardcoded authorization, frontend business authority, or policy decisions outside controlled policy bundles. |
| Regression preservation | PoC 1 and PoC 1A behavior, login security intelligence, audit, session, OPA/SBAC, observability, and rollback hooks. | Changing PoC 1/1A behavior without a controlled change record and regression evidence. |
| Evidence | Machine-readable and human-readable test/failure/evidence reports attached to PR/MR Evidence Pack. | Screenshots or informal developer statements as sole proof. |

# 3. Gate Operating Model
| Gate | Primary Question | Mandatory Outcome | Blocks When |
| --- | --- | --- | --- |
| Unit gate | Does isolated behavior work as designed? | JUnit 5 and applicable frontend unit reports. | Test failure, missing report, or unreviewed disabled test. |
| Component gate | Do service components behave through approved ports/adapters? | Component test evidence and mocked adapter controls. | Controller/business logic shortcut or adapter bypass. |
| Integration gate | Can dependencies be validated reproducibly? | Testcontainers or approved disposable dependency evidence. | Local-only dependency or unreproducible integration result. |
| Contract gate | Do APIs/events preserve approved contracts? | OpenAPI/AsyncAPI/Avro compatibility and generated-client evidence. | Breaking change without consumer impact, versioning, and approval. |
| Policy gate | Do OPA/SBAC decisions fail closed and enforce classification? | Allow/deny/escalate/fail-closed test results. | Fail-open, hardcoded role check, missing deny test, or policy bypass. |
| Architecture gate | Does code preserve AIRA architecture boundaries? | Fitness report for dependencies, packages, direct calls, and banned shortcuts. | Boundary violation, direct DB/model call, or frontend authority. |
| Regression gate | Are PoC 1 and PoC 1A preserved? | Regression report and linked baseline evidence. | Login/session/security regression or missing baseline comparison. |
| Evidence gate | Can reviewers reconstruct the result? | Evidence Pack references, artifact hashes, owners, and review status. | Missing evidence, stale evidence, or unclassified artifact. |

# 4. Testing Coverage Matrix
| Test Type | Minimum Coverage | Tooling Baseline | Evidence Artifact |
| --- | --- | --- | --- |
| Unit tests | Domain/use-case logic, validators, mappers, deterministic helpers, error classification, evidence manifest parsing. | JUnit 5; frontend unit framework where applicable. | unit-test-report.xml; coverage summary. |
| Component tests | Application services through ports, DTO validation, adapters mocked or substituted, safe error responses. | JUnit 5; Spring test slices where appropriate. | component-test-report.xml. |
| Integration tests | Database, queue, contract registry, evidence store, policy adapter, GitNexus stub, and scanner artifact flow where applicable. | Testcontainers or approved ephemeral services. | integration-test-report.xml; container logs. |
| Contract tests | OpenAPI lint, generated client compile, AsyncAPI/Avro compatibility, schema evolution checks. | OpenAPI/AsyncAPI validators; schema registry compatibility tools. | contract-test-report.json. |
| Policy tests | OPA/SBAC allow, deny, escalate, fail-closed, SoD, classification ceiling, branch/role restrictions. | OPA/Rego test or approved policy test runner. | policy-test-report.json. |
| Architecture tests | Dependency direction, package boundaries, no direct DB in controller, no model provider SDK, no production credential path. | ArchUnit, Semgrep, dependency analysis, custom rules. | architecture-fitness-report.json. |
| Regression tests | PoC 1 login/session and PoC 1A security intelligence are preserved. | JUnit 5, API tests, selected E2E/smoke checks. | regression-report.md. |
| Smoke tests | Representative service starts, health endpoint, pipeline artifact path, evidence manifest generated. | CI/CD smoke script. | smoke-test-report.txt. |

# 5. Architecture Fitness Function Rules
| Rule ID | Fitness Rule | Detection Method | Gate Result |
| --- | --- | --- | --- |
| AFF-P2-001 | Controllers remain thin adapters and do not own business decisions, policy decisions, audit writes, or direct database access. | ArchUnit/Semgrep package and import checks. | Block on violation. |
| AFF-P2-002 | Application/use-case layer depends on ports, not infrastructure implementations. | Dependency direction rule. | Block on violation. |
| AFF-P2-003 | Infrastructure adapters implement ports and may not leak framework/provider types into domain code. | Package and signature scan. | Block or require waiver. |
| AFF-P2-004 | No direct model-provider SDK call from application code. | Dependency and import scan. | Block on violation. |
| AFF-P2-005 | No direct production credential, Kubernetes, database, or CI/CD mutation path in agents or generated services. | Secret/path/tooling scan and CODEOWNERS review. | Block on violation. |
| AFF-P2-006 | OpenAPI/AsyncAPI and generated clients remain contract-first and source-controlled. | Contract file and generated client validation. | Block if missing where applicable. |
| AFF-P2-007 | Flyway governs database schema/seed changes; manual DDL is prohibited. | Migration path and SQL scan. | Block on manual DDL. |
| AFF-P2-008 | Frontend remains renderer and request initiator, not business authority or policy authority. | Code review and static scan for policy shortcuts. | Block on frontend authority. |
| AFF-P2-009 | Evidence generation cannot suppress failed checks or rewrite prior evidence. | Evidence manifest integrity checks. | Block on tampering risk. |
| AFF-P2-010 | MicroFunction-related changes preserve idempotency, audit, outbox, observability, error policy, and rollback hooks. | Configuration and test matrix validation. | Block if protected path lacks controls. |

# 6. OPA/SBAC Policy Test Pack
| Policy Scenario | Required Test | Expected Result | Evidence |
| --- | --- | --- | --- |
| Allowed reviewer action | Authorized role, correct branch, correct classification, valid ticket, current approval scope. | ALLOW with policy_decision_id. | allow-policy-test.json. |
| Denied unowned action | Actor lacks required CODEOWNER or SBAC skill. | DENY with safe reason code. | deny-owner-test.json. |
| Escalated high-risk change | Security, database, policy, or protected pipeline change requiring checker. | ESCALATE with required reviewer list. | escalate-test.json. |
| Fail-closed outage | OPA unavailable, bundle invalid, missing identity, missing classification, or stale policy. | DENY or controlled HOLD; never allow. | fail-closed-test.json. |
| Classification ceiling | Actor attempts to access higher-classification evidence or scan artifact. | DENY or redacted access. | classification-test.json. |
| Separation of duties | Author attempts to approve own protected output. | DENY or ESCALATE to independent checker. | sod-test.json. |
| Waiver creation | Critical/High waiver requested. | ESCALATE to required authority with expiry and compensating control. | waiver-policy-test.json. |
| Agent/tool action | AI agent or tool requests mutation authority. | DENY unless approved Harness-mediated non-production action exists. | agent-tool-policy-test.json. |

# 7. PoC 1 and PoC 1A Regression Preservation
| Baseline Area | Minimum Regression Check | Blocks PoC 2 Acceptance When |
| --- | --- | --- |
| Login/session establishment | Existing login/session happy path, failure path, token/session context, and audit evidence still pass. | Login or session behavior changes without controlled approval. |
| PoC 1A step-up/risk review | Security intelligence, step-up, lock/unlock, and human approval behaviors remain additive. | PoC 1A overwrites or weakens PoC 1 behavior. |
| OPA/SBAC login decisions | Allow/deny/escalate/fail-closed policy tests still pass. | Policy regression or fail-open path appears. |
| Audit/outbox/observability | Audit, outbox, trace, log, metric, and evidence references remain reconstructable. | Missing trace/evidence/audit field. |
| Error/message behavior | Safe error codes, classifications, and user feedback remain consistent. | Raw exception, sensitive leakage, or inconsistent code/message appears. |
| Rollback/safe disable | Feature flags or rollback path for new PoC 2 controls do not break login baseline. | Rollback disables required security or audit controls. |

# 8. Required Evidence Artifacts

JUnit 5 test report and coverage summary.

Component and integration test reports, including Testcontainers logs where used.

Contract validation report for applicable OpenAPI, AsyncAPI, Avro, or generated client changes.

OPA/SBAC policy test report with allow, deny, escalate, and fail-closed cases.

Architecture fitness report with boundary, direct-call, and dependency-direction findings.

PoC 1 and PoC 1A regression report.

PR/MR AVCI summary and reviewer acknowledgement.

Evidence manifest with artifact hashes, classification, source commit, owner, and improvement backlog references.

# 9. Blocking Conditions and Waivers
| Condition | Default Decision | Waiver Eligibility |
| --- | --- | --- |
| Failing unit/component/integration test | Block merge/review readiness. | Only for non-critical flaky test with owner, expiry, and remediation ticket. |
| Fail-open policy behavior | Block and treat as security defect. | No ordinary waiver; requires Security/ARB risk acceptance if ever considered. |
| Architecture boundary violation | Block unless explicitly accepted by Architecture. | Time-bound waiver with ADR/TDL and refactoring plan. |
| PoC 1/1A regression | Block PoC 2 acceptance. | No waiver for security/login integrity regression. |
| Missing evidence artifact | Block review readiness. | No waiver unless artifact is non-applicable and documented. |
| Direct model-provider or production credential path | Block and log control violation. | No waiver for PoC 2. |
| Critical/High security finding | Block merge. | Security-approved waiver only with compensating control and expiry. |

# 10. RACI
| Activity | SAO/IT Head | DevSecOps | Dev Lead | Security | QA/SDET | DBA | SRE | AI Gov | Audit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gate scope approval | A | R | C | C | C | C | C | C | I |
| Test strategy | C | C | R | C | A/R | C | C | I | I |
| Architecture fitness rules | A | R | R | C | R | C | C | C | I |
| OPA/SBAC policy tests | C | R | C | A/R | R | I | C | C | I |
| Regression baseline | A | C | R | R | A/R | C | C | I | I |
| Evidence review | A | R | C | C | R | C | C | C | C |
| Exit decision input | A | R | R | R | R | C | C | C | C |

# 11. Acceptance Criteria

All mandatory test categories applicable to the PR/MR execute in CI/CD.

Architecture fitness checks detect and block at least one seeded boundary violation during PoC validation.

OPA/SBAC tests prove allow, deny, escalate, fail-closed, separation-of-duties, and classification behavior.

PoC 1 and PoC 1A regression suite passes after PoC 2 pipeline and repository controls are introduced.

Evidence Pack includes test, architecture, policy, regression, waiver, and improvement-backlog references.

No Critical/High testing, architecture, policy, or regression finding remains unresolved without approved waiver.

Reviewers can reconstruct at least one PR/MR from source commit to test evidence and final gate status.

# 12. AVCI Compliance Summary
| AVCI Dimension | PoC 2 045H Evidence |
| --- | --- |
| Attributable | Each test, rule, policy scenario, regression check, owner, reviewer, and evidence artifact is tied to a PR/MR and accountable role. |
| Verifiable | JUnit, Testcontainers, contract, OPA/SBAC, architecture, and regression reports can be replayed and inspected. |
| Classifiable | Test data, policy inputs, logs, reports, and evidence follow classification, redaction, and retention rules. |
| Improvable | Failed tests, drift findings, policy gaps, regression risks, and waiver decisions create backlog items and improvement evidence. |

