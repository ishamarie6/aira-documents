---
title: "Architecture Fitness Function Catalog"
doc_id: "AIRA-23B"
version: "v1.2"
status: "revised"
category: "Architecture fitness and login PoC"
source_docx: "AIRA_23B_Architecture_Fitness_Function_Catalog_v1.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 23-architecture-fitness-login-poc
  - revised
  - aira-23b
---



# Architecture Fitness Function Catalog



AIRA

AI-Native Enterprise Platform

Architecture Fitness Function Catalog

Executable Architecture Controls | SOLID Enforcement | MicroFunction, DevSecOps, Security, Observability, Resilience, and AVCI Evidence
| Property | Value |
| --- | --- |
| Document ID | AIRA-DOC-023B |
| Document Title | AIRA Architecture Fitness Function Catalog |
| Version | v1.2 Revised - Dynamic Workspace, System Builder, AI Agent, PoC, and MicroFunction Enforcement Update |
| Supersedes | 23B-AIRA_Architecture_Fitness_Function_Catalog_v1.1_Aligned.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | DRAFT FOR ARCHITECTURE REVIEW BOARD / CAB APPROVAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; Platform Engineering; SRE; AI Governance; Internal Audit |
| Effective Date | Upon ARB / CAB approval |
| Review Cadence | Quarterly; unscheduled on material architecture, System Builder, MicroFunction, Dynamic Workspace, AI agent, DevSecOps, security, observability, or regulatory change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Architecture-Fitness-Functions / v1.2/ |

# Mandatory Practice Statement

No AIRA code, configuration, prompt, guardrail, model route, database migration, MicroFunction, API/event contract, Dynamic Workspace artifact, Experience Pack, AI agent, pipeline, infrastructure manifest, or AI-assisted remediation is review-ready or production-ready unless the mandatory architecture fitness functions pass or a formal, time-bound waiver is approved. Fitness functions are executable governance controls, not optional review suggestions.

Discipline First - Automation Second - Intelligence Third - AVCI Always

# Static Table of Contents

1. Executive Summary

2. Purpose, Scope, and Authority

3. v1.2 Change Summary

4. Canonical Relationship and Reconciliation Notes

5. Fitness Function Operating Model

6. Enforcement Levels, Toolchain, and Gate Placement

7. Architecture Fitness Function Catalog

8. DevSecOps, GitNexus, and Evidence Pack Gates

9. API, Event, Schema, Outbox, DLQ, and Replay Gates

10. Observability, Security, Resilience, and Runtime Toggle Gates

11. Dynamic Workspace, System Builder, AI Agent, and PoC Gates

12. Waivers, Exceptions, and Non-Conformance

13. RACI and Operating Responsibilities

14. Implementation Roadmap and Acceptance Criteria

15. PR/MR Fitness Evidence Manifest

16. AVCI Compliance Summary

Appendix A. Initial Rule Pack Backlog

Appendix B. Review Queue Control Register

# 1. Executive Summary

AIRA is a governed AI-native enterprise platform where architecture quality must be continuously measurable, repeatable, enforceable, and evidence-producing. This v1.2 revision updates the Architecture Fitness Function Catalog after the alignment of Dynamic Workspace, Composable Experience, System Builder, AI Agent Governance, Login PoC, PoC 1A, PoC 2, MicroFunction runtime, and DevSecOps evidence standards.

The catalog converts AIRA Enterprise Design Principles into checks that run locally, in pre-commit, CI/CD, release readiness, UAT, incident review, and Auto-Heal / Auto-Learn / Auto-Improve review. It provides a practical bridge between architecture standards and developer execution. It also prevents System Builder or AI agents from creating artifacts that look functional but weaken boundaries, security, policy, observability, rollback, or AVCI evidence.

# 2. Purpose, Scope, and Authority

Purpose. Define mandatory and recommended architecture fitness functions for AIRA and specify what each function checks, when it runs, who owns it, what evidence it produces, and what causes rejection or waiver.

Scope. This catalog applies to Java, TypeScript, Python, SQL, YAML, Dockerfile, Helm, Kubernetes, CI/CD, prompt, guardrail, model route, MicroFunction, Dynamic Workspace, Experience Pack, AI agent, data, API, event, workflow, and documentation changes that influence AIRA behavior.

Authority. The catalog is subordinate to the canonical AIRA architecture and AVCI standards but is the implementation authority for executable architecture checks. Where conflicts appear, the stricter control governs and the issue becomes an AVCI reconciliation item.

# 3. v1.2 Change Summary

This revision adds explicit gates for the revised Dynamic Workspace family, Composable Experience Framework, System Builder implementation guide, AI Agent Governance family, Login PoC and PoC 1A standards, PoC 2 System Factory, GitNexus evidence, API/event contracts, OpenTelemetry evidence, authenticated DAST, resilience lab, and runtime telemetry toggle requirements. It also strengthens waiver rules so failed fitness functions cannot be ignored or buried in narrative evidence.

# 4. Canonical Relationship and Reconciliation Notes

AIRA-DOC-001A remains the canonical Enterprise Architecture Principles and SOLID enforcement authority. This document implements those principles as executable checks. AIRA-DOC-023B remains canonical within the MicroFunction source order, but the number is subject to cross-pack numbering review because Pack 03 and Pack 04 both contain document numbers in the 22/23 range. This revision keeps 23B active and review-ready while preserving the master-register reconciliation item.
| Source / Control | Relationship to 23B v1.2 | Required Treatment |
| --- | --- | --- |
| 01A Enterprise Architecture Principles | Defines mandatory EDP/SOLID, Clean Architecture, DDD, ports/adapters, System Builder gates, and architecture evidence. | 23B implements executable checks and evidence requirements. |
| 10/10A/10B/10C/10D MicroFunction Standards | Define runtime assembly, standard steps, boundaries, configuration, and evidence. | 23B blocks direct DB/Kafka/Redis/model calls from business MicroFunctions and validates standard step controls. |
| 12A and 41/42/44-61 Dynamic Workspace family | Define frontend authority boundaries, component registry, templates, Experience Packs, APIs, cache, observability, testing, and evidence. | 23B validates no frontend authority, policy-filtered actions, contract alignment, accessibility, and trace evidence. |
| 41B / 44A System Builder | Define governed change generation and implementation path. | 23B blocks System Builder output promotion without intake, owner, contracts, tests, rollback, and evidence. |
| 42D-42S AI Agent Governance | Define agent identity, tools, autonomy, registry, policy, red-team, incidents, and readiness. | 23B validates agent manifests, tool scopes, model routes, memory/RAG eligibility, evidence, and certification references. |
| PoC 1 / 1A / 2 Standards | Define executable proof sequence for login, security intelligence, and System Factory. | 23B validates acceptance gates, regression, evidence, and readiness entry/exit criteria. |

# 5. Fitness Function Operating Model

A fitness function is an executable or reviewable assertion about AIRA architecture. AIRA uses seven control layers: repository rules, static analysis, policy-as-code, contract/schema validation, behavioral tests, runtime evidence checks, and knowledge feedback. Developers run a local subset. CI/CD runs the mandatory set. ARB/CAB, Security, QA, DevSecOps, and Internal Audit use the evidence pack for protected promotion.

# 6. Enforcement Levels, Toolchain, and Gate Placement

Fitness functions are assigned four enforcement levels: Advisory, Warning, Blocking, and Quarantine. Blocking findings must be corrected or formally waived before merge. Quarantine findings stop promotion and require Security / Architecture escalation.
| Level | Meaning | Required Action |
| --- | --- | --- |
| Advisory | Improvement signal that does not block merge by itself. | Record in PR/MR and backlog when recurring. |
| Warning | Medium-risk drift with compensating control or limited scope. | Reviewer disposition and named owner required. |
| Blocking | Architecture, security, data, test, evidence, or policy violation. | Fix before merge or obtain approved time-bound waiver. |
| Quarantine | Secrets, direct provider/model calls, Restricted-data leakage, policy bypass, guardrail failure, or production-impacting uncontrolled mutation. | Stop promotion; escalate to Security, Architecture, CAB/ARB, and incident process if applicable. |
| Tool / Control | Primary Fitness Role | Minimum Evidence |
| --- | --- | --- |
| ArchUnit / Java tests | Java architecture boundaries, dependency direction, layer/slice rules, forbidden packages, cyclic dependencies. | JUnit report, rule version, affected packages, pass/fail. |
| Semgrep | Forbidden imports, direct SDK calls, unsafe patterns, logging leaks, framework bypass, TypeScript/SQL/YAML checks. | SARIF/report, ruleset version, severity, remediation. |
| OPA / Conftest | Policy-as-code checks for IaC, model routes, SBAC, waivers, deployment, and action permission rules. | OPA decision, input hash, policy bundle version. |
| OpenAPI / AsyncAPI / schema linters | Contract completeness, compatibility, versioning, error shape, idempotency, security schemes. | Lint report, compatibility report, generated client check. |
| JUnit / Vitest / Playwright | Unit, component, workflow, frontend, idempotency, rollback, regression, and E2E tests. | Test report, coverage, mutation/negative path evidence. |
| Gitleaks / Trivy / Syft / Cosign | Secret scan, dependency/container scan, SBOM/provenance/signature fitness. | Scan report, SBOM, attestation, digest. |
| OpenTelemetry / Observability validator | Trace, metric, log, audit, span correlation, forbidden telemetry field checks. | Trace sample, dashboard evidence, log redaction check. |
| GitNexus / Impact analysis | Read-only code graph, blast radius, affected tests, ownership, architecture drift evidence. | Commit-bound report, affected files/tests, reviewer notes. |
| AIRA Evidence Validator | PR/MR AVCI summary, evidence manifest, waiver records, rollout/rollback evidence. | Validated evidence manifest and exception register. |

# 7. Architecture Fitness Function Catalog

The following initial catalog is mandatory unless a formally approved waiver exists. Teams may add stricter bounded-context or service-specific functions, but they may not remove or weaken mandatory AIRA controls.
| ID | Fitness Function | Primary Principle | Tool / Evidence | Trigger | Reject Condition |
| --- | --- | --- | --- | --- | --- |
| AFF-001 | Single Responsibility enforcement for services, MicroFunctions, adapters, policies, prompts, and widgets. | SOLID / SRP | ArchUnit, Sonar, code review | Every PR/MR | Class mixes controller, domain, persistence, workflow, AI routing, or UI authority concerns. |
| AFF-002 | Extension-by-configuration for MicroFunctions, Dynamic Workspace templates, policies, and prompts. | OCP / Config-first | Catalog validator, schema tests | Config or process change | Hardcoded process sequence or bypass of approved config/rule extension. |
| AFF-003 | Liskov-safe contract and DTO compatibility. | SOLID / LSP | Contract tests, schema compatibility | API/event change | Subtype or generated client breaks declared contract or consumer expectation. |
| AFF-004 | Interface segregation for ports, adapters, agents, and tool contracts. | SOLID / ISP | ArchUnit, API review | Service/agent change | Large generic port leaks provider, DB, workflow, or tool concerns into use case. |
| AFF-005 | Dependency inversion across UI, controllers, domain, persistence, messaging, model routes, and tools. | SOLID / DIP | ArchUnit, Semgrep | Every PR/MR | Domain/application logic depends directly on framework, provider SDK, DB, Kafka, Redis, OPA client, model SDK, or UI. |
| AFF-006 | Clean Architecture layer direction. | Clean Architecture | ArchUnit, dependency graph | Every backend PR | Infrastructure or adapter package is referenced from domain rules. |
| AFF-007 | DDD bounded-context ownership and cross-context write prevention. | DDD | ArchUnit, SQL review, events | Domain/schema change | Service writes across bounded context without API/event/workflow contract. |
| AFF-008 | Ports-and-adapters protection for external systems. | Ports/adapters | Semgrep, ArchUnit | Integration change | Direct calls to Keycloak, OPA, Flowable, Temporal, DB, Kafka, Redis, MinIO, OpenKM, or model provider from business logic. |
| AFF-009 | Thin controller and thin UI adapter enforcement. | Clean Architecture | ArchUnit, lint, review | API/UI change | Controller or UI performs authorization, business rules, persistence, workflow, audit, or policy decisions. |
| AFF-010 | MicroFunction standard-step preservation. | MicroFunction / AVCI | Catalog validator, tests | MicroFunction change | Identity, classification, authorization, validation, idempotency, error, audit, observability, or evidence step is removed. |
| AFF-011 | MicroFunction business-function boundary. | MicroFunction / DIP | ArchUnit, Semgrep | Backend PR | Business MicroFunction parses transport payload, writes audit/outbox directly, or owns framework concern. |
| AFF-012 | Flyway-only schema and seed governance. | Database / Reproducibility | Flyway validate, checksum, DBA review | DB change | Manual DDL, drifted checksum, unmanaged seed, simplified schema drift, or destructive migration without approval. |
| AFF-013 | RLS/classification and retention policy fitness. | Security / Data Governance | SQL tests, OPA, DBA review | Schema/data change | Missing classification, RLS, retention, evidence, or redaction rule for sensitive table/field. |
| AFF-014 | OpenAPI contract completeness and compatibility. | Contract-first | OpenAPI lint, contract tests | REST API change | Missing security scheme, Problem Details, idempotency profile, versioning, or generated-client compatibility. |
| AFF-015 | AsyncAPI, Kafka, Avro, CloudEvents, outbox, and replay fitness. | Event architecture | AsyncAPI lint, schema registry, integration tests | Event change | Topic/event has no schema evolution, CloudEvents metadata, outbox/inbox, DLQ, replay, idempotent consumer, or trace correlation. |
| AFF-016 | OPA/SBAC/RBAC/ABAC policy decision fitness. | Policy as Code | OPA/Rego tests, Conftest | Protected action | Authorization is hardcoded or protected action lacks OPA decision, skill scope, classification ceiling, or denial evidence. |
| AFF-017 | AI model route and guardrail boundary. | AI Governance | OPA, guardrail tests, registry validation | Prompt/model change | Direct provider SDK call, unregistered model alias, missing guardrail checkpoint, or prompt classification mismatch. |
| AFF-018 | Agent registry and tool/MCP authorization fitness. | AI Agent Governance | Registry validator, OPA, harness simulation | Agent/tool change | Unregistered agent/tool, excessive scope, no dry-run, no rollback, no owner, no certification reference. |
| AFF-019 | Dynamic Workspace frontend authority boundary. | Dynamic Workspace | Semgrep, UI tests, OPA tests | Frontend/template change | Frontend decides business authority, bypasses API/MicroFunction, exposes unauthorized data, or calls model/tools directly. |
| AFF-020 | Experience Block/Pack manifest completeness. | Composable Experience | Manifest validator, contract tests | Experience Pack change | Missing owner, capability binding, API/event contracts, policy profile, evidence profile, accessibility profile, or rollback path. |
| AFF-021 | Next.js rendering and cache classification fitness. | Secure rendering | Review, E2E, cache tests | Route/template change | User-specific, Confidential, or Restricted data rendered via unsafe caching/PPR/static mode. |
| AFF-022 | Accessibility and responsive behavior fitness. | UX / WCAG | axe, Playwright, manual keyboard test | UI change | Critical path fails keyboard operation, screen-reader labelling, focus handling, responsive layout, or accessible error feedback. |
| AFF-023 | Observability and trace reconstruction fitness. | Observability by Design | OTel validator, log tests | Critical flow change | No trace_id/span_id/request_id, missing audit/evidence ref, missing dashboard signal, or forbidden telemetry field. |
| AFF-024 | Log4j2/Sentry/Loki/Tempo/Grafana evidence consistency. | Operations / SRE | Logging tests, dashboard checks | Runtime change | Logs contain secrets/PII or traces/errors cannot reconstruct request, policy, action, and outcome. |
| AFF-025 | Idempotency, duplicate safety, and replay behavior. | Idempotency by Design | Unit/integration/resilience tests | Mutating/API/event change | Retry/replay duplicates business effect or lacks idempotency key/evidence. |
| AFF-026 | Concurrency and heavy-transaction behavior. | Resilience | Load/concurrency tests | State-changing flow | Race condition, stale state, lock contention, missing timeout/bulkhead, or unsafe long-running browser authority. |
| AFF-027 | DLQ, compensation, rollback, and safe-disable fitness. | Reversibility | Integration/resilience tests | Event/workflow/config change | No DLQ/replay path, rollback, compensation, forward-fix, or feature disablement evidence. |
| AFF-028 | Authenticated DAST and abuse-case test fitness. | Secure by Design | DAST, abuse-case tests | Release gate | Critical/High authz, injection, IDOR, session, CSP, or API abuse finding unresolved or waived incorrectly. |
| AFF-029 | DevSecOps Evidence Pack completeness. | AVCI / DevSecOps | Pipeline evidence validator | Every PR/MR/release | Missing owner, source, tests, scans, SBOM, provenance, GitNexus, policy, rollback, or acceptance evidence. |
| AFF-030 | Auto-Heal, Auto-Learn, Auto-Improve candidate safety. | Progressive Autonomy | Workflow checks, PR review, tests | Improvement loop | Candidate silently mutates production, weakens guardrails, bypasses approval, or lacks tests and rollback. |

# 8. DevSecOps, GitNexus, and Evidence Pack Gates

Every PR/MR and System Builder output must produce a validated evidence pack. GitNexus remains read-only, derivative, commit-bound code intelligence and cannot approve, merge, deploy, or mutate production.
| Gate | Required Evidence |
| --- | --- |
| Build and unit tests | Java/toolchain version, build image digest, test report, coverage, mutation status where applicable. |
| Security and supply chain | SAST, SCA, secret scan, SBOM, provenance, signing/attestation where applicable. |
| GitNexus impact evidence | Affected files, call graph, dependencies, owners, affected tests, architecture drift findings. |
| Review evidence | CODEOWNERS, maker/checker, ARB/CAB where required, AI-use declaration, waiver status. |

# 9. API, Event, Schema, Outbox, DLQ, and Replay Gates

AIRA contract-first delivery requires OpenAPI, AsyncAPI, Avro/JSON Schema, CloudEvents, outbox/inbox, DLQ/replay, idempotent consumer, and trace correlation checks before protected promotion.
| Gate | Reject Condition |
| --- | --- |
| REST contracts | Missing versioning, security schemes, Problem Details, idempotency profile, pagination/filtering rules, or generated-client validation. |
| Event contracts | Missing AsyncAPI topic, Avro/JSON schema, CloudEvents attributes, compatibility check, or replay rule. |
| Outbox/inbox | Event publish occurs outside transaction boundary, consumer is not idempotent, or replay causes duplicate effects. |
| DLQ/replay | No DLQ classification, retry/backoff policy, replay approval, or trace reconstruction evidence. |

# 10. Observability, Security, Resilience, and Runtime Toggle Gates

Observability and runtime toggles may improve performance, but mandatory audit, security, policy, evidence, and protected-action telemetry must not be disabled. Debug verbosity and sampling can be tuned; compliance evidence cannot be turned off.
| Gate | Required Control |
| --- | --- |
| Telemetry minimum | Trace, metric, structured log, audit event, evidence_ref, policy_decision_id, classification, and redaction state. |
| Forbidden telemetry | Passwords, tokens, raw JWTs, secrets, raw PII, embeddings, raw documents, and unrestricted customer payloads blocked by tests. |
| Resilience lab | Timeouts, retries, circuit breakers, bulkheads, DLQ, compensation, cache rebuild, fail-closed behavior, and rollback tested. |
| Runtime toggles | Toggle registry, owner, scope, default, safety floor, audit record, and rollback evidence. |

# 11. Dynamic Workspace, System Builder, AI Agent, and PoC Gates

The revised Dynamic Workspace and PoC standards require fitness functions that cover generated UI, templates, Experience Packs, System Builder outputs, agent manifests, PoC 1/1A/2 evidence, and production readiness.
| Area | Fitness Requirement |
| --- | --- |
| Dynamic Workspace | Frontend renders only; backend authorizes; MicroFunctions execute; PostgreSQL defines truth; Redis/Valkey accelerates only. |
| System Builder | Analyze first, recommend second, generate after approval, validate through evidence, promote through governed gates. |
| AI Agents | Registry-backed identity, owner, SBAC, OPA, tool/MCP, model route, guardrails, certification, incident, and revocation evidence. |
| PoC gates | PoC 1 and 1A must be accepted before PoC 2; PoC 2 proves reusable System Factory, Evidence Pack, and DevSecOps gates. |

# 12. Waivers, Exceptions, and Non-Conformance

A failed mandatory fitness function cannot be ignored. A waiver is acceptable only when it is time-bound, risk-accepted, owned, traceable to a ticket/ADR/TDL, supported by compensating controls, and linked to a remediation plan and expiry date. Quarantine findings are not eligible for ordinary waiver without Security, Architecture, and CAB/ARB review.
| Waiver Field | Required Content |
| --- | --- |
| waiver_id | Unique waiver reference linked to PR/MR, ticket, ADR/TDL, and affected fitness function. |
| owner / approver | Named accountable owner and required approval authority. |
| risk / classification | Impact, classification, affected environment, affected data/control, and severity. |
| compensating control | Temporary control that preserves safety while remediation is pending. |
| expiry / exit plan | Expiry date, remediation owner, validation method, and closure evidence. |

# 13. RACI and Operating Responsibilities
| Role | Responsibilities |
| --- | --- |
| Solutions Architecture Office / IT Head | Owns catalog, approves major changes, arbitrates conflicts, and reports readiness to ARB/CAB. |
| Enterprise Architecture | Maintains principle mapping, boundary rules, ADR/TDL triggers, and architecture waivers. |
| Software Development Lead | Ensures local and CI fitness checks are implemented and developers remediate findings. |
| DevSecOps Lead | Owns pipeline integration, evidence validator, GitNexus integration, SBOM/provenance, and gate enforcement. |
| Security Architecture | Owns OPA/SBAC, DAST, SAST, secrets, classification, abuse-case, and quarantine controls. |
| QA/SDET | Owns tests, mutation, E2E, accessibility, resilience lab, and regression evidence. |
| SRE / Operations | Owns observability, trace reconstruction, SLO/error budget evidence, runtime telemetry toggles, and incident feedback. |
| AI Governance | Owns AI agent, model route, guardrail, RAG/memory, tool/MCP, certification, and autonomy fitness inputs. |
| Internal Audit | Reviews evidence completeness, waiver integrity, control testing, and audit readiness. |

# 14. Implementation Roadmap and Acceptance Criteria
| Phase | Action | Exit Evidence |
| --- | --- | --- |
| Phase 0 | Confirm active catalog, source order, and cross-pack numbering treatment for 23B. | Register entry and open reconciliation item, if numbering remains unresolved. |
| Phase 1 | Implement baseline rule packs: ArchUnit, Semgrep, OPA/Conftest, OpenAPI/AsyncAPI lint, secret scan, SBOM. | Passing CI dry run and documented false-positive handling. |
| Phase 2 | Add MicroFunction, Dynamic Workspace, System Builder, AI Agent, and PoC-specific validators. | Evidence manifest shows each control family mapped to tests and owners. |
| Phase 3 | Enable blocking gates for Critical/High findings after pilot. | CAB/ARB approval, waiver process, incident escalation path. |
| Phase 4 | Use fitness failures to drive Auto-Learn and training improvements. | Backlog items, training updates, revised prompts/rules, and closure evidence. |
| Acceptance Criterion | Pass Condition |
| --- | --- |
| Catalog completeness | All mandatory fitness functions have owner, tool/evidence, trigger, severity, and reject condition. |
| CI/CD enforcement | Mandatory checks run in PR/MR and promotion pipelines with auditable outputs. |
| Evidence validation | PR/MR includes validated AVCI summary, GitNexus, tests, scans, policy, rollback, and waiver status. |
| No silent bypass | System Builder, agents, Auto-Heal, or developers cannot suppress or override mandatory gates without formal waiver. |
| Improvement loop | Recurring failures produce backlog, rule refinement, training, and document update candidates. |

# 15. PR/MR Fitness Evidence Manifest

owner, developer, checker, reviewer, ticket, branch, commit, and AI tools used

affected bounded context, package, MicroFunction, API, event, schema, workflow, Dynamic Workspace, agent, or pipeline artifact

ArchUnit, Semgrep, OPA/Conftest, OpenAPI/AsyncAPI/schema, SAST/SCA/secrets, SBOM/provenance, DAST, and accessibility results

GitNexus impact report, affected tests, affected owners, and architecture-drift findings

OpenTelemetry trace/log/metric/audit/evidence references and forbidden telemetry validation

idempotency, concurrency, resilience, outbox/inbox, DLQ/replay, rollback, safe-disable, and compensation test results

waiver status, residual risk, compensating controls, expiry, and remediation plan where applicable

AVCI summary: attributable, verifiable, classifiable, improvable

# 16. AVCI Compliance Summary
| AVCI Property | Evidence in This v1.2 Revision |
| --- | --- |
| Attributable | Document control, owner, co-owners, fitness function owner roles, PR/MR manifest, GitNexus, policy decision, and waiver ownership. |
| Verifiable | Executable checks, pipeline gates, tests, scan outputs, OPA decisions, contract validation, runtime evidence, and trace reconstruction. |
| Classifiable | Classification handling for artifacts, telemetry, evidence, prompts, logs, traces, and policy decisions. |
| Improvable | Recurring failures feed backlog, training, prompt updates, ruleset changes, ADR/TDL updates, and controlled Auto-Heal/Auto-Learn/Auto-Improve proposals. |

# Appendix A. Initial Rule Pack Backlog
| Rule Pack | Purpose | Initial Owner |
| --- | --- | --- |
| aira-java-archunit-core | Layering, package, dependency, controller, MicroFunction, and direct SDK rules. | Software Development Lead |
| aira-semgrep-secure-boundaries | Forbidden imports, direct provider/model SDK calls, secrets/logging leaks, frontend authority patterns. | Security Architecture |
| aira-opa-conftest-gates | SBAC, model route, waiver, deployment, template activation, tool/MCP, and environment policy checks. | Security / DevSecOps |
| aira-contract-lint-pack | OpenAPI, AsyncAPI, Avro/JSON Schema, CloudEvents, Problem Details, idempotency, and versioning. | API Architecture |
| aira-observability-validator | OTel semantic attributes, Log4j2 redaction, Sentry/Loki/Tempo/Grafana correlation, forbidden telemetry fields. | SRE / DevSecOps |
| aira-resilience-lab-pack | Retry, timeout, circuit breaker, bulkhead, outbox, DLQ, replay, cache rebuild, rollback, heavy transaction. | QA/SDET / SRE |
| aira-evidence-validator | PR/MR AVCI summary, evidence manifest, GitNexus, waiver, audit, and rollback evidence. | DevSecOps / Internal Audit |

# Appendix B. Review Queue Control Register
| Seq | File Name | Current Version | Recommended Version | Status | Priority | Dependency / Next Step |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 23B-AIRA_Architecture_Fitness_Function_Catalog_v1.1_Aligned.docx | v1.1 | v1.2 Revised | Completed in this document | High | Use as CI/CD enforcement catalog for revised MicroFunction, Dynamic Workspace, System Builder, AI Agent, PoC, and DevSecOps controls. |
| 2 | 08-AIRA_Unit_Testing_Standard_v3.1_Aligned.docx | v3.1 | v3.2 Revised | Recommended next | High | Align unit/component/mutation/test evidence with the updated architecture fitness catalog. |
| 3 | 08A-AIRA_AI_Assisted_Unit_Testing_Maker_Checker_Prompt_Standard_v1.0.docx | v1.0 | v1.1 Revised | Recommended after 08 | High | Update AI-assisted test-generation prompts so they generate evidence compatible with 23B and 08. |
| 4 | 20-AIRA_CICD_Pipeline_and_Evidence_Pack_Implementation_Guide_v1.1_Aligned.docx | v1.1 | v1.2 Revised | Later validation patch | Medium | Ensure CI/CD guide includes the 23B v1.2 rule pack and evidence manifest. |

End of Document

