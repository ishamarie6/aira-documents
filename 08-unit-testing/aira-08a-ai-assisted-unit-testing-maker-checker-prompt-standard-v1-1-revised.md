---
title: "AI Assisted Unit Testing Maker Checker Prompt Standard"
doc_id: "AIRA-08A"
version: "v1.1"
status: "revised"
category: "Unit testing"
source_docx: "AIRA_08A_AI_Assisted_Unit_Testing_Maker_Checker_Prompt_Standard_v1.1_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 08-unit-testing
  - revised
  - aira-08a
---



# AI Assisted Unit Testing Maker Checker Prompt Standard



AIRA
AI-Native Enterprise Platform

AI-Assisted Unit Testing Maker-Checker Prompt Standard

AIRA-DOC-008A | v1.1 Revised

Codex Test Maker | Independent Checker | Human Review | CI/CD Evidence | AVCI Always
| Property | Value |
| --- | --- |
| Document ID | AIRA-DOC-008A |
| Canonical Filename | AIRA_08A_AI_Assisted_Unit_Testing_Maker_Checker_Prompt_Standard_v1.1_Revised.docx |
| Version | v1.1 Revised |
| Supersedes | 08A-AIRA_AI_Assisted_Unit_Testing_Maker_Checker_Prompt_Standard_v1.0.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | FOR ARCHITECTURE REVIEW BOARD / QA / DEVSECOPS APPROVAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | QA/SDET Lead; Software Development Lead; DevSecOps Lead; Security Architecture; AI Engineering; Platform Engineering; Internal Audit |
| Primary Parent | 08-AIRA Unit Testing, Quality Engineering, and Evidence Standard v3.2 Revised |
| Companion Sources | 01/01A AVCI and Enterprise Architecture; 03 Developer Guide; 07 Skills Framework; 11/20 DevSecOps and Evidence; 23B Architecture Fitness; 52 Dynamic Workspace Testing; 10/10A-10D MicroFunction; 15 API; 16 Flyway; 17 Security; 31A Observability; 42D-42S AI Agent Governance |
| Review Cadence | Quarterly; unscheduled after material testing, AI tooling, security, CI/CD, MicroFunction, System Builder, model route, or policy change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Quality-Engineering / AI-Assisted-Testing / v1.1/ |

# Mandatory Practice Statement

AI-assisted testing in AIRA is a governed maker-checker workflow. Codex or an approved coding assistant may act as the first-loop Test Maker. An independent approved AI checker may challenge and improve the test suite. A named human developer, QA/SDET, security reviewer, or architect remains accountable for acceptance. No AI tool may approve its own tests, merge its own output, suppress findings, weaken assertions, disable controls, or promote code without AVCI evidence.

The goal is not more test files. The goal is deterministic proof that behavior, security controls, architecture boundaries, MicroFunction steps, failure paths, observability, reversibility, and evidence production work as intended.

# 1. Executive Summary

This v1.1 revision updates the AIRA AI-Assisted Unit Testing Maker-Checker Prompt Standard after the revision of the parent Unit Testing Standard v3.2, Architecture Fitness Function Catalog v1.2, Dynamic Workspace testing controls, PoC 1 and PoC 1A evidence gates, and PoC 2 System Factory readiness expectations. It preserves the original two-loop Codex Maker and independent Checker pattern while strengthening it for enterprise-grade DevSecOps evidence.
| Strategic Outcome | v1.1 Required Result |
| --- | --- |
| No superficial AI tests | AI-generated tests must prove meaningful behavior, negative cases, failure paths, security boundaries, observability, and evidence production. |
| Separation of duties | Maker, checker, human reviewer, approver, and promoter remain distinct for high-risk or production-bound changes. |
| Evidence-first testing | Every AI-assisted test change records prompt, branch, commit, affected files, test commands, reports, findings, residual gaps, and reviewer decision. |
| AIRA-wide coverage | The prompt workflow covers backend, frontend, MicroFunction, policy, contract, event, Flyway, observability, resilience, security, and AI/evaluation tests where applicable. |
| Controlled improvement | Failed tests, weak assertions, missing coverage, flaky behavior, and AI hallucinations become improvement backlog items, not hidden defects. |

# 2. Source Alignment and Correction Summary
| Source / Control | Alignment Applied |
| --- | --- |
| 08 Unit Testing Standard v3.2 | 08A is an execution prompt companion, not a parent testing authority. It implements the parent standard through copy-ready maker-checker prompts and evidence rules. |
| 23B Architecture Fitness Function Catalog | AI-assisted tests must include architecture, dependency, policy, security, and evidence gates when affected by a change. |
| PoC 1 / PoC 1A Standards | Login tests must prove AUTH_LOGIN_CONTEXT_ESTABLISH, PoC 1 preservation, PoC 1A additive behavior, OPA/SBAC, outbox, audit, Dynamic Workspace bootstrap, and fail-closed paths. |
| Dynamic Workspace 41/42/44-61 | Frontend tests must prove that the UI renders and requests safely, while backend policy, MicroFunctions, and PostgreSQL remain authority. |
| 42D-42S AI Agent Governance | Testing agents and checker agents must be registered, scoped, observable, reversible, and subordinate to human review and OPA/SBAC controls. |
| 11/20 DevSecOps and Evidence | Test outputs must be CI/CD-ready and evidence-pack-ready with GitNexus impact, scans, reports, waivers, and rollback references. |

# 3. Authority, Scope, and Non-Negotiable Boundaries

## 3.1 In Scope

AI-assisted generation, review, challenge, improvement, and evidence summarization of unit, component, contract, policy, architecture, frontend, database, event, observability, resilience, and AI evaluation tests.

Codex, Claude, ChatGPT, Hermes, or approved checker-agent usage inside branch-bound, repository-governed, classification-aware workflows.

Prompt execution standards for developers, QA/SDET, DevSecOps, security, architecture reviewers, and future System Builder test-generation workflows.

## 3.2 Out of Scope

Autonomous merge, approval, deployment, production mutation, waiver approval, or release promotion by AI.

Using production data, secrets, raw tokens, raw PII, unrestricted documents, raw prompts, or confidential customer evidence inside tests or screenshots.

Replacing human reviewer accountability, CODEOWNERS, CI/CD gates, QA sign-off, Security review, Architecture review, or CAB/ARB decision rights.

## 3.3 Conflict Rule

If this prompt standard conflicts with AIRA-DOC-008, 01A, 11/20, 17, 23B, 31A, 42D-42S, or a more specific current standard, the stricter and more specific current standard governs. The conflict must be recorded as an AVCI reconciliation item and assigned for register cleanup.

# 4. Maker-Checker Operating Model
| Role | Allowed Activities | Prohibited Activities | Required Output |
| --- | --- | --- | --- |
| Codex / Test Maker | Inspect change scope, identify test gaps, draft or update tests, run permitted local/CI commands, produce maker evidence. | Approve its own output, delete failing tests, weaken assertions, disable scans, bypass policy, merge code, or hide findings. | Maker Test Report with changed files, commands, results, evidence links, and open gaps. |
| Independent AI Checker | Review maker output, challenge assertions, add missing negative tests, verify determinism, security, architecture, evidence, and classification. | Rubber-stamp maker tests, approve merge, suppress high-risk findings, or rely only on coverage percentage. | Checker Findings Report with accepted tests, rejected tests, added tests, residual risk, and recommendation. |
| Human Developer | Review generated tests, fix code/test defects, confirm meaningful assertions, address checker findings, prepare PR/MR evidence. | Treat AI output as authority or proceed with unresolved Critical/High findings without waiver. | Developer confirmation in PR/MR AVCI summary. |
| QA/SDET / Security / Architecture | Approve sufficiency for risk, policy, security, accessibility, architecture, and release evidence. | Delegate acceptance to AI or skip required gates due to schedule pressure. | Review sign-off, waiver decision, or rejection with remediation path. |

# 5. Two-Loop Workflow
| Phase | Maker-Checker Action | Required Evidence |
| --- | --- | --- |
| 0 - Intake and scope | Identify ticket, branch, commits, changed files, impacted bounded contexts, classification, risk tier, and affected AIRA standards. | Intake summary; affected contracts, APIs, events, migrations, policies, MicroFunctions, UI components, and evidence paths. |
| 1 - Codex maker analysis | Codex reviews existing tests and proposes missing test categories before editing files. | Gap analysis table; proposed tests; anti-pattern warnings; commands to run. |
| 2 - Codex test generation | Codex creates or revises tests in feature branch only and runs permitted commands. | Changed test files; command output; failing/passing report; known limitations. |
| 3 - Independent checker review | Checker challenges maker output for weak assertions, missing negative cases, classification leaks, architecture drift, and non-determinism. | Checker report; added tests; rejected assertions; required fixes. |
| 4 - Developer/QA remediation | Human resolves findings, reruns tests, updates evidence, and decides whether Security/Architecture/DBA review is needed. | Final test output; evidence pack; waiver requests if applicable. |
| 5 - PR/MR evidence closure | PR/MR includes maker report, checker report, CI evidence, GitNexus impact, scans, rollback/forward-fix plan, and AVCI summary. | PR/MR AVCI block; CI/CD artifacts; evidence pack reference. |

# 6. Copy-Ready Prompt A - Codex Test Maker
| Prompt A - Codex Test Maker |
| --- |
| Act as the AIRA Codex Test Maker for this repository branch. Purpose: generate and improve deterministic tests without weakening architecture, security, evidence, or AVCI. Inputs to inspect: ticket or task, changed files, existing tests, OpenAPI/AsyncAPI contracts, Flyway migrations, OPA policies, MicroFunction config, Dynamic Workspace components, CI rules, and AIRA standards. Required analysis before editing: identify impacted bounded contexts, risk tier, classification, required test types, missing negative cases, affected contracts, affected policies, affected events, affected telemetry, and rollback evidence. Allowed actions: draft or improve tests, create synthetic fixtures, run permitted local test commands, summarize evidence, and list gaps. Prohibited actions: do not approve, merge, deploy, edit production config, use production data, expose secrets/PII, disable failing tests, weaken assertions, bypass OPA/SBAC, or remove evidence controls. Generate or improve tests for applicable areas: unit, component, contract, OPA/Rego, architecture, frontend, accessibility, Flyway/RLS, outbox/inbox, Kafka/CloudEvents/Avro, DLQ/replay, observability, resilience, and AI/evaluation. Output: Maker Test Report with changed files, commands run, test results, gaps, risks, evidence references, and recommended checker focus areas. |

# 7. Copy-Ready Prompt B - Independent Test Checker
| Prompt B - Independent Test Checker |
| --- |
| Act as the AIRA Independent Test Checker. Purpose: challenge the Codex Test Maker output and prevent superficial, unsafe, non-deterministic, or misleading tests. Inputs to inspect: Maker Test Report, changed code, changed tests, CI output, coverage/mutation reports, security reports, contracts, OPA policies, MicroFunction config, evidence pack draft, and affected AIRA standards. Review focus: assertion quality, negative tests, failure paths, policy denial, fail-closed behavior, idempotency, concurrency, replay, DLQ, rollback, observability, secrets hygiene, classification safety, architecture boundaries, frontend non-authority, and test determinism. Required action: identify weak tests, missing tests, over-mocking, false positives, untested business invariants, untested security boundaries, missing evidence, and unsupported acceptance claims. Allowed actions: add or propose additional tests, recommend fixes, require reruns, classify findings, and produce acceptance recommendation. Prohibited actions: do not approve merge, suppress critical findings, use production data, accept coverage as sufficient proof, or mark unresolved high-risk defects as acceptable without waiver. Output: Checker Findings Report with accepted tests, rejected tests, added tests, unresolved findings, severity, required remediation, waiver candidates, and final recommendation: Block, Revise, Review-ready, or Accept with evidence. |

# 8. Required Test Coverage Decision Matrix
| Change Type | Required Maker Coverage | Required Checker Challenge |
| --- | --- | --- |
| Backend domain/use-case logic | Unit and component tests; negative paths; boundary tests; mutation candidate for high-risk logic. | Verify meaningful assertions, no over-mocking, no controller/business coupling, no direct infrastructure leakage. |
| MicroFunction transaction or step | Step sequence, idempotency, audit, outbox, policy, observability, rollback, failure paths. | Verify mandatory steps not removed and standard sequence evidence is traceable. |
| OpenAPI / REST contract | Request/response fixtures, safe Problem Details errors, generated-client compatibility, auth failures. | Verify contract drift, versioning impact, safe error content, and classification-safe responses. |
| AsyncAPI / Kafka / Avro / CloudEvents | Schema compatibility, envelope validation, correlation, outbox/inbox, idempotent consumer, DLQ and replay. | Verify schema evolution and replay do not duplicate effects or bypass authorization. |
| Database / Flyway / RLS | Clean-migrate, upgrade migrate, seed determinism, RLS positive/negative tests, no manual DDL. | Verify canonical schema, repeatability, rollback/forward-fix, and classification handling. |
| Dynamic Workspace / frontend | Component, form, generated client, accessibility, policy-filtered action, denied state, duplicate-click, telemetry. | Verify frontend does not authorize, mutate authority state, expose tokens/PII, or invent contracts. |
| Security or policy | OPA/SBAC/ABAC allow/deny/escalate, secrets scan, safe logs, authenticated DAST where applicable. | Verify abuse cases, classification ceilings, missing identity, stale policy, and fail-closed dependency failures. |
| AI agent, prompt, model route, retrieval | Eval/golden dataset, guardrail, route eligibility, retrieval source, tool-denial, audit evidence. | Verify no direct model calls, no unapproved tool actions, and no promotion without human review. |

# 9. Evidence Report Templates
| Report | Required Fields |
| --- | --- |
| Maker Test Report | Ticket/task, branch, commit, AI tool, prompt version, changed files, affected standards, generated tests, commands run, results, failed tests, known gaps, evidence refs. |
| Checker Findings Report | Maker report reviewed, files reviewed, weak assertions, missing tests, added tests, security concerns, architecture concerns, residual findings, severity, recommendation. |
| PR/MR Test Evidence Summary | Owner, reviewer, CI run, coverage/mutation, unit/component/contract/policy/security/accessibility/resilience results, GitNexus impact, waivers, rollback/forward-fix. |
| Improvement Backlog Record | Issue detected, evidence retrieved, candidate fix or learning, tests required, owner, due date, approval route, and closure evidence. |

# 10. Quality Gates and Blocking Conditions

Critical or High security findings block acceptance unless a named risk owner approves a time-bound waiver with compensating controls and remediation evidence.

A test suite that passes by skipping, disabling, weakening, over-mocking, removing assertions, or ignoring policy failures is non-conformant.

Frontend, Dynamic Workspace, or AI assistant changes that cannot prove safe denial, accessibility, redaction, and telemetry must not be promoted.

Database, event, or MicroFunction changes that cannot prove idempotency, outbox/inbox, DLQ/replay, Flyway repeatability, and rollback/forward-fix remain review-only.

AI-generated tests are not accepted until an independent checker and named human reviewer confirm the assertions are meaningful and evidence is complete.

# 11. Runtime Telemetry, DAST, and Resilience Lab Instructions
| Area | Prompt Instruction |
| --- | --- |
| Runtime telemetry toggles | Ask the maker to test that debug/sampling toggles may reduce non-critical diagnostics but cannot disable mandatory audit, security, policy-decision, evidence, or protected-action telemetry. |
| Authenticated DAST | Ask the maker to provide authenticated DAST setup notes for protected web/API paths and capture findings, severity, remediation, and waiver evidence. |
| Resilience Lab | Ask the maker and checker to cover retry, duplicate request, concurrency, cache loss, downstream failure, workflow timeout, DLQ, replay, compensation, and rollback behavior where impacted. |
| Observability reconstruction | Ask for trace_id, request_id, policy_decision_id, evidence_ref, audit record, outbox event, and dashboard/log query proof where practical. |

# 12. RACI
| Activity | Developer | Codex Maker | Checker | QA/SDET | Security | Architecture | DevSecOps |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Define test scope | A/R | C | C | R | C | C | C |
| Generate initial tests | A/R | R | I | C | C | C | C |
| Challenge test quality | C | I | R | A/R | C | C | C |
| Approve security sufficiency | C | I | C | C | A/R | C | C |
| Approve architecture sufficiency | C | I | C | C | C | A/R | C |
| Run CI/CD and evidence gates | R | C | C | C | C | C | A/R |
| Approve PR/MR readiness | A/R | I | C | R | R | R | R |

# 13. Acceptance Criteria

The maker prompt was executed on the correct branch with scoped, classified, and approved repository context.

The maker produced or improved tests for all affected risk areas, not only the happy path.

The checker independently reviewed the tests and identified weak assertions, gaps, or acceptance blockers.

All Critical and High findings were fixed or formally waived by the correct authority with expiry and remediation plan.

Tests cover relevant backend, frontend, MicroFunction, contract, policy, database, event, security, observability, resilience, and AI/evaluation domains.

No production data, secrets, raw tokens, raw PII, raw prompts, or restricted artifacts appear in tests, screenshots, logs, prompts, or evidence.

CI/CD evidence pack includes test results, security scans, policy checks, GitNexus impact, architecture fitness, rollback/forward-fix, and AVCI summary.

Human reviewer confirms that AI-generated tests are meaningful, deterministic, architecture-aligned, and release-relevant.

# 14. Review Queue Control Register
| Sequence | File | Recommended Version | Status | Dependency | Next Step |
| --- | --- | --- | --- | --- | --- |
| 1 | 08-AIRA_Unit_Testing_Standard_v3.2_Revised | v3.2 | Completed | Parent testing standard | Use as parent authority for 08A. |
| 2 | 08A-AIRA_AI_Assisted_Unit_Testing_Maker_Checker_Prompt_Standard | v1.1 | This document | 08 parent standard; 23B; 52; DevSecOps | Approve for team use after review. |
| 3 | 07-AIRA_AI_DevSecOps_Skills_Framework | v3.2 | Recommended next | 08/08A now define testing skills and evidence needs | Align human and AI testing skills, SBAC, trust, certification, and team maturity. |
| 4 | 07B-AIRA_AI_DevSecOps_Team_Transformation_Maturity_and_Progressive_Autonomy_Direction_Standard | v1.1 | Next after 07 | Skills framework and maker-checker practice | Align team maturity roadmap with revised AI-assisted testing and progressive autonomy controls. |

# 15. AVCI Compliance Summary
| AVCI Property | Evidence in This Standard |
| --- | --- |
| Attributable | Names owner, co-owners, maker, checker, human reviewer, branch, commit, prompt version, test reports, and PR/MR evidence. |
| Verifiable | Defines maker report, checker report, CI/CD evidence, test commands, security scans, fitness gates, GitNexus impact, and acceptance conditions. |
| Classifiable | Requires synthetic fixtures, classification-safe prompts, redacted evidence, no secrets/PII/raw prompts, and approved evidence storage. |
| Improvable | Turns weak tests, missing assertions, flakiness, AI hallucinations, recurring defects, and failed gates into backlog and controlled improvement candidates. |

# 16. External Reference Register
| Reference | Use in This Standard |
| --- | --- |
| JUnit Jupiter / JUnit Platform | Primary Java testing framework baseline for backend test generation and execution. |
| Mockito | Approved mocking and test-double support at explicit ports/adapters boundaries. |
| PIT Mutation Testing | Mutation quality check for high-risk Java/JVM code where practical. |
| Testcontainers for Java | Ephemeral dependency support for deterministic integration-style tests where needed. |

