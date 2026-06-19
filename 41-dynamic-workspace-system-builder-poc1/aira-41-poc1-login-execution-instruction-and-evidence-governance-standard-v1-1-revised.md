---
title: "PoC1 Login Execution Instruction and Evidence Governance Standard"
doc_id: "AIRA-41"
version: "v1.1"
status: "revised"
category: "Dynamic workspace, system builder, and PoC1"
source_docx: "AIRA_41_PoC1_Login_Execution_Instruction_and_Evidence_Governance_Standard_v1.1_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 41-dynamic-workspace-system-builder-poc1
  - revised
  - aira-41
---



# PoC1 Login Execution Instruction and Evidence Governance Standard



AIRA
AI-Native Enterprise Platform

PoC 1 Login Execution Instruction and Evidence Governance Standard

AIRA-DOC-041 | v1.1 Revised

Login Baseline | MicroFunction Runtime Assembly | Evidence Governance | DevSecOps Readiness
| Property | Value |
| --- | --- |
| Document ID | AIRA-DOC-041 |
| Canonical Filename | AIRA_41_PoC1_Login_Execution_Instruction_and_Evidence_Governance_Standard_v1.1_Revised.docx |
| Version | v1.1 Revised |
| Supersedes | 41-AIRA_PoC1_Login_Execution_Instruction_and_Evidence_Governance_Standard_v1.0.md |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Architecture, Security, DevSecOps, QA/SDET, DBA, and Team Execution Review |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Software Development Lead; Security Architecture; DevSecOps Lead; QA/SDET; DBA; Platform Engineering; AI Governance; Internal Audit |
| Primary Execution References | 38 Login Function Prompt Standard; 23A Login Developer Source Code Generation Standard; 23C Login Code, Parameter, and Configuration Generation Execution Prompt Standard; 22B Login MicroFunction Design Pattern; 24 Login Runtime/DB Standard |
| Review Cadence | After PoC 1 execution, before PoC 1A entry, before PoC 2 authorization, quarterly, and after material identity/security/runtime change |

Mandatory practice statement. PoC 1 is not complete when code compiles or login appears to work. PoC 1 is complete only when source code, configuration, Flyway migrations, OPA/SBAC policies, tests, scans, outbox records, observability, GitNexus impact evidence, PR/MR records, rollback path, and AVCI evidence prove that AUTH_LOGIN_CONTEXT_ESTABLISH is secure, fail-closed, testable, observable, reversible, and ready as the preserved baseline for PoC 1A and PoC 2.

Table of Contents

This document uses Word-ready heading styles. In Microsoft Word, insert or update an automatic Table of Contents before controlled publication.
| Section | Title |
| --- | --- |
| 1 | Executive Summary and v1.1 Governance Verdict |
| 2 | Purpose, Scope, and Authority |
| 3 | Source Alignment and Corrections |
| 4 | PoC 1 Control Model |
| 5 | Mandatory Execution Workflow |
| 6 | Architecture and MicroFunction Requirements |
| 7 | API, Event, Database, and Configuration Requirements |
| 8 | Security, OPA/SBAC, and Fail-Closed Requirements |
| 9 | Testing, DevSecOps, GitNexus, and Evidence Pack Requirements |
| 10 | Observability, Runtime Telemetry, and Trace Reconstruction |
| 11 | PoC 1A and PoC 2 Readiness Gates |
| 12 | RACI, Review Queue, and AVCI Summary |

# 1. Executive Summary and v1.1 Governance Verdict

This v1.1 revision updates the original PoC 1 Login Execution Instruction and Evidence Governance Standard so it aligns with the revised AIRA roadmap, PoC 1A execution controls, PoC 1/1A integrated acceptance matrix, Dynamic Workspace controls, System Builder governance, MicroFunction requirements, DevSecOps evidence model, and PoC 2 readiness expectations.

PoC 1 is the login/session/authorization foundation that later PoCs must preserve. It must prove that a simple login capability can be delivered through the AIRA model: configuration-first MicroFunction runtime assembly, Keycloak/OIDC authentication, OPA/SBAC authorization, Flyway-governed configuration, audit/outbox evidence, OpenTelemetry-ready observability, secure frontend rendering, deterministic tests, GitNexus impact analysis, and PR/MR AVCI evidence.
| Verdict Item | v1.1 Decision | Required Treatment |
| --- | --- | --- |
| Original PoC 1 execution instruction | Retain and strengthen | Keep the original one-step execution workflow, prompt verification, two-loop testing, GitNexus pass, and PR/MR evidence packaging. |
| Runtime baseline | Correct and align | Use Java 25 LTS, Spring Boot target baseline, React/TypeScript, Keycloak OIDC Authorization Code + PKCE, OPA/Rego, PostgreSQL/Flyway, and approved ports/adapters. |
| PoC 1 / PoC 1A boundary | Strengthen | PoC 1A must not rewrite PoC 1. PoC 1 must expose only approved extension points and regression evidence. |
| PoC 2 entry gate | Strengthen | PoC 2 cannot proceed until PoC 1 and PoC 1A evidence packs, regression proof, and Critical/High closure or waiver records are complete. |
| AI-assisted execution | Govern | Codex, Hermes, Claude, or other approved assistants may draft, test, and review but may not bypass human review, OPA/SBAC, CI/CD, GitNexus, or evidence gates. |

# 2. Purpose, Scope, and Authority

## 2.1 Purpose

- Define how the AIRA software development team shall execute PoC 1 Login in a repeatable, governed, testable, secure, and auditable manner.

- Ensure AUTH_LOGIN_CONTEXT_ESTABLISH becomes the preserved baseline for PoC 1A security intelligence and later platform PoCs.

- Convert team execution instructions into an evidence-producing engineering standard suitable for developers, reviewers, QA/SDET, Security, DevSecOps, DBA, and Internal Audit.

- Ensure generated artifacts satisfy AVCI, EDP, MicroFunction, DevSecOps, security, observability, reversibility, and PoC 2 readiness requirements.

## 2.2 Scope
| In Scope | Out of Scope |
| --- | --- |
| PoC 1 login authentication request, callback, session context, OPA/SBAC decision, audit, outbox, Dynamic Workspace bootstrap, tests, scans, evidence, and PR/MR package. | Custom authentication engine, password storage, direct credential validation, direct production access, unmanaged AI tool execution, or frontend-only authorization. |
| PoC 1 execution workflow, prompt compliance, GitNexus impact analysis, Derived Artifact summary, GitLens attribution, and Obsidian evidence projection. | Production deployment or CAB approval automation without human approval and complete evidence. |
| PoC 1 extension readiness for PoC 1A and PoC 2. | Implementing PoC 1A risk review or unlock behavior inside the PoC 1 baseline without approved extension hooks. |

## 2.3 Authority and Precedence
| Level | Authority | PoC 1 Interpretation |
| --- | --- | --- |
| L0 | Architecture Board / CAB / IT Head | Final authority for exceptions, production-impacting decisions, and PoC phase transition. |
| L1 | AIRA AVCI, 01A EDP, Engineering Blueprint, Security, DevSecOps, Database/Flyway, API, Observability, Change standards | Universal rules for evidence, architecture, security, testing, migration, contracts, observability, and rollback. |
| L2 | This AIRA-DOC-041 v1.1 Standard | Execution and evidence governance for PoC 1 Login. |
| L3 | 23A, 23C, 22B, 24, 38, 43C, 43D, 42C, PoC 2 standard | Implementation prompts, runtime schema, acceptance matrix, roadmap, and phase readiness controls. |
| L4 | Tickets, branches, commits, PR/MRs, CI runs, scans, traces, audit, evidence stores | Operational proof and improvement input. |

# 3. Source Alignment and Corrections
| Alignment Area | Correction Applied in v1.1 |
| --- | --- |
| Version and source status | Promoted the original Markdown execution directive into a Word-ready formal AIRA standard. |
| Technology baseline | Updated references to Java 25 LTS backend baseline, Spring Boot target baseline, React/TypeScript, Keycloak/OIDC/PKCE, OPA/SBAC, PostgreSQL/Flyway, OpenTelemetry, and approved CI/CD tooling. |
| MicroFunction baseline | Aligned to AUTH_LOGIN_CONTEXT_ESTABLISH as a governed, runtime-assembled transaction, not a hardcoded login flow. |
| PoC 1A dependency | Added explicit regression and extension-readiness obligations so PoC 1A can be additive and non-destructive. |
| PoC 2 dependency | Added entry gate mapping to PoC 2 DevSecOps, Evidence Pack, GitNexus, and System Factory readiness. |
| Dynamic Workspace | Added backend-authority, policy-filtered frontend, safe session-context display, and Dynamic Workspace bootstrap evidence. |
| External standards | Aligned contract, event, observability, security verification, and accessibility references with current official sources where applicable. |

# 4. PoC 1 Control Model

PoC 1 shall implement only the login/session/authorization baseline. It must not implement PoC 1A security intelligence features except through clearly identified extension points, feature flags, contract stubs, and backlog references approved by Architecture and Security.
| Control Domain | Required PoC 1 Treatment | Evidence |
| --- | --- | --- |
| Identity | Delegate authentication to Keycloak using OIDC Authorization Code + PKCE. AIRA application code must not store, hash, compare, or validate passwords. | OIDC configuration evidence, tests, safe token handling review. |
| Session Context | Establish governed session context only after token validation, actor/tenant resolution, classification, OPA/SBAC decision, audit, and observability correlation. | Session context test evidence, policy decision log, audit records. |
| Authorization | Use OPA/Rego with RBAC/ABAC/SBAC inputs. No frontend, controller, service, or SQL hardcoding of roles or skills. | OPA policy tests, default-deny evidence. |
| MicroFunction Runtime | Represent AUTH_LOGIN_CONTEXT_ESTABLISH as a configured transaction with standard steps and narrow business functions behind ports/adapters. | Runtime configuration, MicroFunction step evidence, architecture fitness results. |
| Audit and Outbox | Produce append-only audit and transactional outbox records for security-relevant events and session-context establishment. | Audit rows, outbox event evidence, replay/idempotency test. |
| Frontend | Render safe login/session state and Dynamic Workspace bootstrap only from backend-authorized, policy-filtered responses. | Frontend tests, no token leakage proof, accessibility evidence. |
| Evidence | Every artifact must link to owner, branch, commit, prompt, CI run, test evidence, scan result, policy decision, trace/audit ref, classification, and improvement backlog. | PR/MR AVCI summary and Evidence Pack. |

# 5. Mandatory Execution Workflow
| Phase | Execution Requirement | Blocking Gate |
| --- | --- | --- |
| 0. Source Confirmation | Confirm 38, 23A, 23C, 22B, 24, security, API, database, MicroFunction, testing, DevSecOps, GitNexus, Dynamic Workspace, and observability standards are available to the developer and AI tools. | No generation until source references are listed in the task/ticket. |
| 1. Prompt Execution | Execute approved PoC 1 prompt using controlled AI assistant and repository context. Generate code, configuration, policies, migrations, tests, and evidence templates. | No uncontrolled table names, step codes, direct SQL, direct model calls, or hardcoded authorization. |
| 2. Prompt Compliance Verification | Use an independent approved checker to verify prompt compliance, artifact completeness, security, testing, and evidence coverage. | Critical and High gaps require fix or formal waiver. |
| 3. Improvement Gate | Classify gaps, implement fixes through branch/PR, update evidence, and prevent silent mutation. | No merge without reviewer confirmation. |
| 4. Two-Loop Testing | Loop 1 drafts and runs tests. Loop 2 independently checks assertions, missing coverage, edge cases, and regression quality. | Weak assertions or missing security/fail-closed tests block acceptance. |
| 5. Contract/Security/E2E Testing | Run contract tests, OPA tests, mutation tests where practical, SAST, SCA, secret scan, authenticated DAST, and Playwright/E2E login tests. | Critical/High security findings block acceptance unless formally waived. |
| 6. GitNexus and Derived Evidence | Produce code map, ownership map, impact analysis, affected-test mapping, architecture drift findings, and derived evidence summaries. | GitNexus is read-only and cannot approve, merge, deploy, or mutate. |
| 7. PR/MR Packaging | Package AVCI summary, design-principle impact, AI-use declaration, tests/scans, rollout/rollback, known limitations, and improvement backlog. | PR/MR is incomplete without evidence links. |
| 8. Final Acceptance | Architecture, Security, QA/SDET, DevSecOps, DBA, and IT Head review evidence and authorize PoC 1 exit or remediation. | PoC 1A cannot start until exit evidence is accepted. |

# 6. Architecture and MicroFunction Requirements
| Requirement | Mandatory Rule |
| --- | --- |
| SOLID and Clean Architecture | Controllers remain thin adapters. Domain/use-case logic does not depend on web, database, Keycloak, OPA client, Kafka, Redis, AI gateway, or framework details. |
| DDD and bounded context | Identity and Access owns AUTH_LOGIN_CONTEXT_ESTABLISH language, invariants, contracts, and runbooks. Other contexts may consume events or session context but must not write across boundaries. |
| Ports and adapters | Keycloak, OPA, Vault abstraction, PostgreSQL, outbox publisher, Dynamic Workspace resolver, observability sink, and CI evidence access must be behind explicit ports/adapters. |
| MicroFunction step integrity | No mutating, sensitive, or integration-facing flow may omit receive, correlate, actor/session resolution, rate-limit, authorize, classify, validate, idempotency, execute, audit, outbox, observe, and safe-response controls unless waived. |
| Configuration-first delivery | Prefer runtime configuration, seed data, policy, and reusable standard steps before custom code. Code only the business gap and keep it narrow. |
| Reversibility | PoC 1 changes must support rollback, forward-fix, safe-disable, configuration revert, Flyway repair strategy where appropriate, and PoC 1A regression preservation. |

# 7. API, Event, Database, and Configuration Requirements
| Area | PoC 1 Requirement | Evidence |
| --- | --- | --- |
| OpenAPI | Login/session-context APIs must be contract-first, safe-response modeled, versioned, and generated-client compatible. | OpenAPI lint, contract tests, generated client evidence. |
| AsyncAPI / Events | Outbox events and future security events must have AsyncAPI/Event contract alignment and CloudEvents metadata where applicable. | AsyncAPI validation, event schema tests. |
| Kafka / Avro / CloudEvents | Events must define schema subject, schema version, event type, source, id, time, correlation, classification, and replay behavior where used. | Schema registry or local schema validation evidence. |
| Transactional outbox | Security/session event writes must be transactionally bound to the database commit and retry-safe. | Outbox row evidence, duplicate-safe publisher test. |
| Idempotent consumers | Any consumer or downstream projection must tolerate retries, duplicate events, replay, and out-of-order handling within defined limits. | Idempotency tests and replay notes. |
| DLQ and replay | PoC 1 event processing must define DLQ, retry, poison-message handling, and manual replay guardrails where eventing is enabled. | DLQ/replay runbook or design record. |
| Flyway and PostgreSQL | All schema, seed, index, RLS, evidence, and configuration changes use Flyway. Manual DDL is prohibited. | Flyway info/validate/migrate evidence. |
| Runtime configuration | Transaction definitions, step parameters, feature flags, audit profile, observability profile, error policy, and rollback strategy are versioned and reviewable. | Configuration hash, Git commit, seed evidence. |

# 8. Security, OPA/SBAC, and Fail-Closed Requirements
| Security Control | Mandatory Requirement |
| --- | --- |
| No custom authentication | AIRA must not store, hash, compare, or validate passwords. Authentication remains delegated to Keycloak/enterprise identity target pattern. |
| Token safety | Never expose raw JWTs, refresh tokens, ID tokens, passwords, secrets, PII, or production data in UI, logs, traces, tests, screenshots, prompts, or evidence. |
| OPA/SBAC default deny | Missing policy, missing skill, wrong tenant, expired token, invalid classification, unavailable OPA, unavailable audit, or unavailable runtime configuration must deny protected access safely. |
| Secrets hygiene | Secrets must not exist in source code, .env committed files, prompts, screenshots, logs, or test outputs. Use Vault-compatible abstraction and synthetic local values. |
| Authenticated DAST | Authenticated DAST must test login/session flows using synthetic users and must verify no sensitive leakage, broken access control, unsafe redirects, or weak session handling. |
| Abuse cases | At minimum test repeated login failures, callback replay, CSRF/CORS weakness, token tampering, missing OPA, missing Keycloak, missing audit, stale session, and frontend manipulation. |
| Human accountability | AI and automation may recommend or draft fixes but cannot approve access, waive findings, merge code, or promote without named human accountability. |

# 9. Testing, DevSecOps, GitNexus, and Evidence Pack Requirements
| Evidence Area | Required Coverage |
| --- | --- |
| Unit and component tests | Backend use cases, ports/adapters, policy input mapping, idempotency, safe errors, and frontend safe rendering. |
| OPA/Rego tests | Allow, deny, missing skill, wrong tenant, invalid classification, default-deny, and unavailable dependency decisions. |
| Contract tests | OpenAPI safe response, schema compatibility, generated clients, Problem Details, and error semantics. |
| Playwright / E2E | Successful login, denied login, session context display, Dynamic Workspace bootstrap, logout/session expiry, and fail-closed dependency path where practical. |
| Security scans | SAST, SCA, secret scan, dependency review, container/IaC scan where applicable, and authenticated DAST. |
| Architecture fitness | No controller business logic, no direct DB from domain, no direct OPA/Keycloak/provider calls from UI/controller, no hardcoded roles, and no frontend authority. |
| GitNexus | Read-only code map, impact analysis, affected tests, architecture drift signal, security-sensitive code map, and PR/MR evidence summary. |
| Evidence Pack | AVCI summary, test results, scan results, policy decisions, migration evidence, observability trace references, audit/outbox refs, GitNexus report, rollback/forward-fix path, known limitations, and improvement backlog. |

# 10. Observability, Runtime Telemetry, and Trace Reconstruction

PoC 1 must be observable by construction. Runtime logging may be tuned through approved runtime toggles when performance is affected, but mandatory security, audit, policy-decision, evidence, and protected-action telemetry must not be disabled.
| Telemetry Area | Required Behavior |
| --- | --- |
| Correlation | Propagate trace_id, span_id, request_id, correlation_id, causation_id, actor hash, tenant/context, transaction code, policy ref, idempotency key, and evidence_ref where safe. |
| Log4j2 / Logs | Structured logs only. No passwords, raw tokens, secrets, raw PII, account numbers, or raw prompts. Include classification and redaction state. |
| OpenTelemetry / Tempo | Trace frontend, gateway, backend API, MicroFunction coordinator, OPA decision, audit/outbox write, and dependencies. |
| Sentry | Capture sanitized frontend/backend errors and release context without sensitive payloads. |
| Loki / Grafana | Dashboards must show login success/failure, deny rates, dependency failures, policy-denial trends, latency, error rates, and evidence completeness. |
| Trace reconstruction | An auditor must reconstruct who initiated login, which policy decided, what transaction executed, what audit/outbox records were written, which tests/scans supported the release, and what improvement items remain. |
| Runtime toggles | Allow debug verbosity, sampling, and non-critical diagnostic events to be adjusted on the fly; never allow toggles to disable audit, security decision, policy denial, or evidence records. |

# 11. PoC 1A and PoC 2 Readiness Gates
| Readiness Gate | Required Exit Evidence Before Proceeding |
| --- | --- |
| PoC 1A entry | PoC 1 regression suite passes; AUTH_LOGIN_CONTEXT_ESTABLISH works; OPA/SBAC default-deny proof exists; audit/outbox evidence exists; Dynamic Workspace bootstrap works; no Critical/High open findings. |
| PoC 1A preservation | PoC 1A can be disabled without breaking PoC 1; extension hooks are documented; PoC 1 API/contract compatibility is preserved. |
| PoC 2 entry | PoC 1 and PoC 1A evidence packs are accepted; GitNexus and derived evidence are complete; tests/scans/policies are complete; architecture impact is documented; rollback path exists. |
| Improvement backlog | Known limitations, gaps, candidate refactors, prompt improvements, policy improvements, resilience scenarios, and evidence automation items are captured and assigned. |

# 12. RACI, Review Queue, and AVCI Summary
| Activity | Developer | Tech Lead | Security | QA/SDET | DBA | DevSecOps | Solutions Architect / IT Head |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PoC 1 implementation | R | A/R | C | C | C | C | A |
| MicroFunction design and runtime config | R | A/R | C | C | C | C | A |
| OPA/SBAC policy | C | C | A/R | C | I | C | A |
| Flyway migration and seed review | R | C | C | C | A/R | C | A |
| Testing and evidence | R | C | C | A/R | C | C | A |
| Security scans and DAST | C | C | A/R | C | I | R | A |
| GitNexus and derived evidence | R | A/R | C | C | I | C | A |
| Final PoC 1 exit acceptance | C | C | C | C | C | C | A/R |

## 12.1 Review Queue Control Register
| Seq | File | Recommended Version | Status | Priority | Dependency | Next Step |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | AIRA_41_PoC1_Login_Execution_Instruction_and_Evidence_Governance_Standard | v1.1 Revised | Completed in this revision | High | 43C, 43D, 43, 42C, 45 PoC2 | Team review and Obsidian upload after approval. |
| 2 | AIRA_23C_Login_PoC1_Code_Parameter_and_Configuration_Generation_Execution_Prompt_Standard | v1.2 Revised | Recommended next | High | 41 v1.1; 22B; 24; Dynamic Workspace 41/42/44-61 | Update code/parameter/config generation prompt so developers generate PoC 1 exactly from the revised execution standard. |
| 3 | AIRA_38_Login_Function_Prompt_Standard | v1.2 Revised | Recommended after 23C | High | 41 and 23C | Align primary login prompt with revised PoC 1 and PoC 1A boundary controls. |
| 4 | AIRA_24_Login_PoC1_MicroFunction_Runtime_Configuration_Database_Schema_Standard | v1.2 Revised | Queued | High | 23C and 48 | Align runtime config, canonical schemas, Flyway, audit, outbox, and RLS. |
| 5 | AIRA_22B_Login_and_Session_Establishment_MicroFunction_Design_Pattern | v1.2 Revised | Queued | High | 41, 23C, 24 | Update design pattern after implementation prompts and schema alignment. |

## 12.2 AVCI Compliance Summary
| AVCI Property | Evidence in v1.1 |
| --- | --- |
| Attributable | Defines owner, co-owners, RACI, source baseline, execution references, branches, commits, prompts, AI tools, reviewers, and PR/MR evidence. |
| Verifiable | Requires deterministic tests, OPA/Rego tests, contract tests, Playwright/E2E, SAST/SCA/secret scan/authenticated DAST, GitNexus impact analysis, Flyway evidence, traces, audit, and outbox records. |
| Classifiable | Classifies the document as INTERNAL CONFIDENTIAL and requires classification/redaction for code, prompts, logs, traces, evidence, screenshots, tokens, PII, and AI usage. |
| Improvable | Captures known limitations, candidate fixes, Auto-Heal/Auto-Learn/Auto-Improve proposals, prompt improvements, policy gaps, test gaps, and next-review queue items. |

# Appendix A. PR/MR AVCI Evidence Template
| Template Field | Required Content |
| --- | --- |
| Attributable | Owner; developer; reviewer/checker; ticket; branch; commit; AI tools used; prompt standard used; source documents referenced. |
| Verifiable | Backend unit tests; frontend tests; OPA tests; contract tests; mutation tests where practical; Playwright tests; SAST; SCA; secret scan; authenticated DAST; GitNexus report; migration evidence; observability evidence. |
| Classifiable | Data classification; secrets/PII handling; token handling; log redaction; model/prompt eligibility; evidence storage location; retention rule. |
| Improvable | Known limitations; recommended improvements; backlog items; prompt improvements; AIRA standards requiring update; Auto-Heal/Auto-Learn/Auto-Improve candidates. |
| Design Principle Impact | SOLID; Clean Architecture; DDD; ports/adapters; idempotency; fail-safe behavior; testability; security; observability; reversibility; AVCI. |

# Appendix B. Non-Negotiable Rejection Rules

- Reject any implementation that builds a custom authentication engine or handles passwords inside AIRA code.

- Reject any implementation that exposes raw JWTs, refresh tokens, passwords, secrets, raw PII, or production data in logs, UI, tests, traces, screenshots, prompts, or evidence.

- Reject any implementation that hardcodes authorization in controllers, frontend code, services, SQL, or tests instead of using OPA/SBAC policy inputs.

- Reject any implementation that bypasses Flyway, uses manual DDL, invents non-canonical tables, or writes directly across bounded-context boundaries.

- Reject any implementation that omits audit, outbox, observability, idempotency, safe errors, or rollback/forward-fix path for protected flows.

- Reject any implementation where AI, GitNexus, or agents approve, merge, deploy, waive findings, mutate production, or bypass maker-checker review.

- Reject any implementation that weakens PoC 1 to make PoC 1A or PoC 2 easier.

# Appendix C. Change Log
| Version | Date | Summary |
| --- | --- | --- |
| v1.0 | 2026-05-25 | Initial Markdown execution instruction and evidence governance standard for PoC 1 Login. |
| v1.1 Revised | 2026-06-17 | Promoted to formal Word-ready AIRA standard; aligned with revised 42C, 43C, 43D, 43 PoC1A, 45 PoC2, Dynamic Workspace, MicroFunction, DevSecOps, API/event, observability, security, and evidence controls. |

