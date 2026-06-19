---
title: "Architecture Fitness Function Executable Gate Pack"
doc_id: "AIRA-76"
version: "v1.0"
status: "final"
category: "Architecture fitness gate pack"
source_docx: "AIRA_76_Architecture_Fitness_Function_Executable_Gate_Pack_v1.0.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 76-architecture-fitness-gate-pack
  - final
  - aira-76
---



# Architecture Fitness Function Executable Gate Pack



AIRA

AI-Native Enterprise Platform

Architecture Fitness Function Executable Gate Pack

AIRA-DOC-076 | v1.0 | Executable Architecture Controls | CI/CD Gate Pack | AVCI Evidence
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-076 |
| Canonical Filename | AIRA_76_Architecture_Fitness_Function_Executable_Gate_Pack_v1.0.docx |
| Version | v1.0 - Initial Executable Gate Pack |
| Status | Draft for Architecture Review Board / CAB / Engineering / DevSecOps / Security / QA / Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; DevSecOps Lead; Software Development Lead; Security Architecture; QA/SDET; Platform Engineering; DBA; SRE; AI Governance; Internal Audit |
| Primary Parents | 01A Enterprise Architecture Principles; 01 AVCI; 01B Evidence; 02 Engineering Blueprint; 20 CI/CD; 23B Architecture Fitness Function Catalog |
| Companion Sources | 10-10E MicroFunction; 11/11A DevSecOps; 15/15A API; 16/16A/16B Database/Flyway; 17/17A Security; 19 GitNexus; 31/31A Observability; 65 Policy-as-Code; 66 Evidence Manifest; 67 API/Event/Replay; 68 Control Matrix; 72 Golden Paths; 73 System Builder |
| Review Cadence | Quarterly; unscheduled after material architecture, CI/CD, security, MicroFunction, Dynamic Workspace, AI-agent, policy, evidence, or production-control change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Architecture-Fitness-Gate-Pack / 76 / v1.0 / |

# Mandatory Practice Statement

No AIRA change is merge-ready, promotion-ready, activation-ready, or production-ready merely because it compiles, deploys, renders, or passes a happy-path demo. It is ready only when the mandatory architecture fitness gates prove that SOLID, Clean Architecture, DDD, ports/adapters, policy-as-code, security, observability, idempotency, resilience, reversibility, and AVCI evidence are preserved or improved. Required gates fail closed. AI assistants, System Builder, GitNexus, and agents may propose, analyze, draft, or request checks; they must not approve, merge, deploy, suppress findings, weaken gates, or mutate production.

# Static Table of Contents

1. Executive Summary

2. Purpose, Scope, and Authority

3. Control Plane and Gate Stack

4. Gate Severity and Decision Model

5. Executable Gate Catalog

6. Toolchain Implementation Matrix

7. Repository Layout and CI Integration

8. Copy-Ready Gate Examples

9. Evidence Pack and Manifest Bindings

10. RACI and Separation of Duties

11. Implementation Roadmap and Acceptance Criteria

12. Anti-Patterns, Reconciliation Items, and AVCI Summary

# 1. Executive Summary

AIRA already has a strong architecture fitness foundation. AIRA-DOC-023B defines fitness functions as executable governance controls, not optional review suggestions. This document converts that catalog into an implementation-ready gate pack that repositories, CI/CD pipelines, PR/MR templates, System Builder outputs, and reviewers can use consistently.

The purpose of this gate pack is practical enforcement. It provides a standard set of gates, tool mappings, evidence outputs, sample rules, and escalation behavior so architecture quality is not dependent on memory, manual review, or AI judgment. Architecture fitness becomes executable, repeatable, observable, reversible, and evidence-producing.
| Outcome | How AIRA-DOC-076 Delivers It |
| --- | --- |
| Architecture drift prevention | Detects boundary violations, dependency direction errors, direct calls, missing contracts, unsafe toggles, and hidden authority bypasses before merge. |
| Executable governance | Converts EDP-01 through EDP-20, AVCI, MicroFunction, Dynamic Workspace, DevSecOps, and AI boundary rules into CI-validatable checks. |
| Evidence by construction | Produces machine-readable and human-readable evidence linked to commit, PR/MR, build, gate, owner, classification, waiver, and improvement path. |
| Safe automation | Allows System Builder and AI agents to generate candidates while preventing self-approval, direct provider calls, production mutation, and policy bypass. |
| Continuous improvement | Turns recurring failures into backlog, training, rule-pack, golden-path, and standard-update candidates. |

# 2. Purpose, Scope, and Authority

## 2.1 Purpose

Define the executable architecture fitness gate pack for AIRA repositories, CI/CD pipelines, System Builder candidate outputs, Dynamic Workspace changes, MicroFunction runtime changes, API/event contracts, database migrations, AI-agent artifacts, prompts, guardrails, and infrastructure manifests.

## 2.2 Scope
| Area | Treatment |
| --- | --- |
| In scope | Java, TypeScript, Python, SQL, YAML, Dockerfile, Helm/Kubernetes, CI workflows, OPA/Rego, OpenAPI, AsyncAPI, schemas, prompts, guardrails, model route aliases, MicroFunction configuration, Dynamic Workspace templates, evidence manifests, and documentation that affects system behavior. |
| Out of scope | Manual production mutation, unmanaged scripts, advisory-only architecture comments with no gate binding, AI self-approval, direct model-provider calls, direct business logic in UI, manual DDL, and unreviewed local-only rules. |
| Authority | Subordinate to 01A/01/01B/02 and companion to 20, 23B, 65, 66, 68, and 73. When conflict exists, apply the stricter control and log an AVCI reconciliation item. |
| Gate posture | Blocking for protected branches and production-bound change; warning or advisory only when the gate is explicitly marked non-blocking for a lower-risk environment. |

# 3. Control Plane and Gate Stack

Figure 1. Architecture fitness gates connect AIRA principles, repository changes, CI/CD checks, evidence packs, maker-checker review, and promotion gates.

Figure 2. Required gate stack for protected changes. Lower-risk changes may run a profile subset, but missing mandatory identity, security, policy, classification, audit, evidence, and rollback gates cannot be waived silently.

# 4. Gate Severity and Decision Model
| Severity | Meaning | Required Evidence |
| --- | --- | --- |
| Advisory | Improvement recommended. Does not block by default, but must be captured if accepted. | Backlog item or training note. |
| Warning | Risk exists. Merge may proceed only with owner acknowledgement and documented follow-up. | PR/MR evidence note and due date. |
| Blocking | Merge or promotion prohibited until fixed or formally waived by required authority. | Remediation evidence or waiver record. |
| Critical Block | Immediate escalation. Production promotion prohibited; potential incident, security, compliance, or architecture authority breach. | Security/Architecture escalation, RCA, containment, and corrective action. |

# 5. Executable Gate Catalog
| ID | Gate | Method | Blocks When | Evidence |
| --- | --- | --- | --- | --- |
| AFF-001 | Layer Dependency Direction | ArchUnit / dependency graph | Domain/application depends on adapters, Spring web, persistence, Kafka, UI, model SDK, or infrastructure packages. | archunit-report.xml, dependency-boundary.json |
| AFF-002 | Thin Controller and Adapter Boundary | ArchUnit / Semgrep | Controller contains business rules, persistence writes, event publishing, policy decisions, or AI calls. | architecture-report.json, changed-file evidence |
| AFF-003 | STP-BUS Direct-Call Ban | ArchUnit / Semgrep | Business MicroFunction directly calls DB, Kafka, Redis, OpenKM, Flowable/Temporal, Keycloak, Vault, or model provider. | microfunction-fitness-summary.md |
| AFF-004 | No Direct Model Provider Calls | Semgrep / dependency rule | OpenAI, Anthropic, provider SDK, or direct HTTP model endpoint appears outside approved LiteLLM/private gateway adapter. | ai-route-fitness.json |
| AFF-005 | Contract-First API/Event Integrity | OpenAPI/AsyncAPI/schema checks | REST/event/schema/error contract changes without versioning, consumer impact, compatibility, or generated client validation. | openapi-diff.json, asyncapi-diff.json, schema-compatibility.json |
| AFF-006 | Flyway-Only Database Change | Flyway validate/info/clean-migrate test | Manual DDL, unmanaged schema change, destructive migration without approval, missing rollback/forward-fix. | flyway-validate.txt, migration-risk.md |
| AFF-007 | OPA/SBAC Policy Enforcement | OPA test / Conftest | Protected action can execute without allow decision, classification route, skill scope, SoD, or fail-closed behavior. | opa-test-results.json, policy-decision-summary.md |
| AFF-008 | Secrets and Forbidden Telemetry | Secrets scan / Semgrep / log tests | Secrets, tokens, raw PII, Restricted payloads, embeddings, prompts, or account identifiers appear in source, logs, traces, screenshots, tests, or evidence. | secret-scan-report.json, log-redaction-test.json |
| AFF-009 | Observability Correlation | OTel test / log schema test | Trace ID, request ID, actor hash, policy decision, evidence_ref, transaction code, or safe error fields are missing from critical paths. | otel-correlation-summary.md, trace-reconstruction.md |
| AFF-010 | Idempotency, Outbox, DLQ, Replay | Testcontainers / resilience tests | Mutating path can double-post, emit event outside outbox, replay unsafely, lose DLQ context, or bypass compensation. | idempotency-test.json, outbox-dlq-replay.json |
| AFF-011 | Runtime Toggle Safety | OPA/Conftest / config lint | Runtime toggle disables audit, security, policy decision, classification, idempotency, outbox, or critical error evidence. | runtime-toggle-policy-check.md |
| AFF-012 | Dynamic Workspace Backend Authority | Component lint / E2E / policy test | Frontend component mutates business state directly, bypasses MicroFunction/API contract, or hides required policy evidence. | dynamic-workspace-fitness-summary.md |
| AFF-013 | System Builder and AI Boundary | Prompt/rule lint / policy test | AI output approves itself, writes to protected branch, deploys, mutates runtime, calls tools without Harness/SBAC/OPA, or suppresses findings. | ai-boundary-fitness.json |
| AFF-014 | Evidence Manifest Completeness | JSON Schema / CI validator | Missing owner, classification, source refs, gate results, artifact hashes, GitNexus refs, rollback, approvals, or improvement path. | evidence-manifest-validation.json |
| AFF-015 | PRR/ORR and Resilience Binding | Readiness/resilience gate | Production-bound change lacks readiness, SLO/dashboard, rollback, runbook, resilience, concurrency, or post-deploy evidence. | prr-orr-summary.md, resilience-lab-summary.md |

# 6. Toolchain Implementation Matrix
| Tool / Method | Primary Use | Gate Profile |
| --- | --- | --- |
| ArchUnit | Java package boundaries, layer rules, forbidden dependencies, MicroFunction isolation. | Required for Java backend protected branches. |
| Semgrep | Cross-language forbidden imports, unsafe code patterns, direct provider calls, direct SQL/Kafka/Redis, frontend authority bypass. | Required for backend, frontend, scripts, CI templates, and generated code. |
| OPA/Rego and Conftest | Policy decisions, environment manifests, runtime toggles, agent action requests, deployment admission. | Required for policy-controlled and promotion-bound work. |
| OpenAPI/AsyncAPI/schema tools | Contract diff, compatibility, CloudEvents envelope, generated clients, schema registry readiness. | Required for API/event boundary changes. |
| Flyway | Migration validate/info, clean-migrate in non-prod, checksum, RLS/index/seed evidence. | Required for every database change. |
| Testcontainers and resilience tests | Kafka, PostgreSQL, outbox, DLQ/replay, idempotent consumer, dependency failure, concurrency. | Required for integration, eventing, and state-changing flows. |
| Evidence manifest validator | JSON Schema validation of gate outputs, owners, hashes, classification, approvals, waivers, rollback. | Required for protected PR/MR and release candidates. |
| GitNexus read-only analysis | Code map, impact analysis, affected tests, boundary drift, security-sensitive map. | Advisory or blocking based on repo maturity; always read-only and derivative. |

# 7. Repository Layout and CI Integration

AIRA repositories shall expose fitness gates through a predictable layout. Golden Paths may provide full examples, but every protected repository must preserve the following minimum structure or an approved equivalent.

/.aira/

fitness/

archunit/

semgrep/

opa/

conftest/

evidence-schema/

manifests/

service-manifest.yaml

classification.yaml

runtime-toggle-policy.yaml

/contracts/

openapi/

asyncapi/

schemas/

/src/main/java/...            # domain, application, ports, adapters separated

/evidence/                   # generated by CI, not hand-invented

/.github/workflows/aira-ci.yml or .gitlab-ci.yml
| Stage | Fitness Coverage | Evidence Output |
| --- | --- | --- |
| Local / IDE | Fast checks: formatting, unit tests, Semgrep subset, ArchUnit subset, secret scan. | Developer maker evidence. |
| PR/MR CI | Full build, test, contract, policy, architecture, security, database, evidence manifest validation. | Blocking evidence for protected branches. |
| Release Candidate | Supply chain, PRR/ORR, resilience lab, performance/concurrency, dashboards, rollback, CAB/ARB triggers. | Release evidence pack. |
| Post-promotion | Runtime trace reconstruction, policy-denial monitoring, SLOs, incidents, improvement backlog. | Operational evidence and Auto-Learn inputs. |

# 8. Copy-Ready Gate Examples

## 8.1 ArchUnit Examples

// Domain must not depend on adapters or infrastructure.

classes()

.that().resideInAPackage("..domain..")

.should().onlyDependOnClassesThat()

.resideInAnyPackage("java..", "jakarta..", "com.aira..domain..", "com.aira..shared..")

.because("domain logic must remain independent of frameworks and adapters");

// Business MicroFunctions must not call infrastructure directly.

noClasses()

.that().resideInAPackage("..microfunction..business..")

.should().dependOnClassesThat()

.resideInAnyPackage("..adapter..", "org.springframework.kafka..", "org.springframework.data..",

"redis.clients..", "dev.langchain4j..", "com.openai..", "com.anthropic..");

## 8.2 Semgrep Examples

rules:

- id: aira-no-direct-model-provider

message: "Use approved LiteLLM/private gateway adapter; direct provider SDK calls are prohibited."

severity: ERROR

languages: [java, typescript, python]

pattern-either:

- pattern: import $X from "openai"

- pattern: import com.openai.$X

- pattern: import com.anthropic.$X

metadata:

aira_gate: AFF-004

- id: aira-no-business-sql

message: "Business logic must use domain ports/repositories; direct SQL is prohibited."

severity: ERROR

languages: [java]

patterns:

- pattern: $JDBC.$METHOD(...)

- metavariable-regex:

metavariable: $METHOD

regex: "(query|update|execute).*"

## 8.3 OPA / Conftest Examples

package aira.fitness.runtime_toggle

default allow = false

mandatory_controls := {"audit", "security", "policy_decision", "classification", "idempotency", "outbox", "critical_error"}

allow {

input.change_type == "runtime_toggle"

not disables_mandatory_control

input.owner != ""

input.classification != ""

input.rollback_path != ""

}

disables_mandatory_control {

some c

c := input.disabled_controls[_]

mandatory_controls[c]

}

# 9. Evidence Pack and Manifest Bindings

Figure 3. Gate results become evidence, waivers, remediation, and improvement inputs. Evidence records must be linked to the PR/MR and control matrix.
| Evidence Folder | Required Contents |
| --- | --- |
| evidence/05-architecture | archunit-report.xml, semgrep-architecture.json, dependency-boundary-report.json, architecture-fitness-summary.md |
| evidence/04-policy | opa-test-results.json, conftest-results.json, sbac-decision-summary.md, runtime-toggle-policy-check.md |
| evidence/06-contracts | openapi-diff.json, asyncapi-diff.json, schema-compatibility.json, cloudevents-validation.json |
| evidence/08-events-resilience | outbox-inbox-test.json, idempotency-test.json, dlq-replay-test.json, concurrency-test.json |
| evidence/11-observability | otel-correlation-summary.md, log4j2-redaction-test.json, sentry-test.md, trace-reconstruction.md |
| evidence/00-manifest | evidence-manifest.json with gate_results[], artifact_refs[], waiver_refs[], rollback_refs[], approval_refs[] |

# 10. RACI and Separation of Duties
| Role | RACI | Responsibility |
| --- | --- | --- |
| Enterprise Architecture | A/R | Owns gate catalog, severity model, boundary rules, architecture waiver decisions, and control interpretation. |
| DevSecOps Lead | A/R | Implements gates in CI/CD, evidence manifest validation, runner hardening, and promotion status checks. |
| Software Development Lead | R | Ensures code structure, package boundaries, ports/adapters, MicroFunction isolation, and remediation. |
| Security Architecture | A/R | Owns OPA/SBAC, direct-call bans, secrets hygiene, DAST/security findings, and AI/tool boundary gates. |
| QA/SDET | R | Owns deterministic tests, contract tests, mutation/load where applicable, and quality evidence. |
| DBA / Data Governance | R | Owns Flyway gate, RLS/schema controls, data classification, retention, and migration evidence. |
| SRE / Platform | R | Owns observability, resilience, PRR/ORR, runtime toggle safety, SLO evidence, and rollback readiness. |
| Internal Audit | C/I | Reviews evidence completeness, waiver aging, control effectiveness, and traceability. |

# 11. Implementation Roadmap and Acceptance Criteria
| Phase | Execution Focus | Exit Evidence |
| --- | --- | --- |
| Phase 0 - Adopt Gate Pack | Add AIRA-DOC-076 to canonical register, project source, Obsidian/LLM Wiki projection, and repository references. | Approved candidate record and source hash. |
| Phase 1 - Baseline Rules | Add ArchUnit, Semgrep, OPA/Conftest, secret scan, evidence manifest validation, and PR/MR template references. | Protected branch runs baseline gates. |
| Phase 2 - Contract and Data Gates | Enable OpenAPI, AsyncAPI, schema compatibility, CloudEvents, Flyway, and database fitness checks. | API/event/database changes cannot bypass contract and migration gates. |
| Phase 3 - MicroFunction/Dynamic Workspace Gates | Enable STP-BUS direct-call bans, runtime config validators, UI backend-authority checks, widget/MicroFunction evidence. | MicroFunction and Dynamic Workspace changes produce fitness evidence. |
| Phase 4 - Resilience/PRR Binding | Enable idempotency, outbox, DLQ/replay, concurrency, PRR/ORR, and resilience lab gate profiles. | Release candidates include readiness and resilience evidence. |
| Phase 5 - Continuous Assurance | Track waiver aging, gate bypass attempts, recurring failures, rule coverage, and improvement candidates. | Quarterly control assurance report and updated gate backlog. |

## Minimum acceptance criteria:

Protected branches run mandatory architecture fitness gates and retain gate reports in the evidence pack.

Required gates fail closed for Critical/Blocking findings unless a formal, time-bound waiver is approved.

Every fitness failure has an owner, severity, remediation path, evidence reference, and improvement classification.

Gate outputs map to AIRA-DOC-066 evidence manifest fields and AIRA-DOC-068 control objectives.

System Builder and AI-generated candidates cannot bypass the same gates required of human-authored changes.

# 12. Anti-Patterns, Reconciliation Items, and AVCI Summary

## 12.1 Anti-Patterns

Treating fitness functions as advisory review comments instead of enforceable gates.

Disabling Semgrep, ArchUnit, OPA, contract, or evidence checks to make a deadline.

Accepting AI-generated code because it appears correct while it weakens boundaries, security, tests, or evidence.

Allowing GitNexus or System Builder findings to replace tests, scans, policy checks, or human review.

Using waivers as permanent bypasses instead of time-bound risk records with remediation evidence.

## 12.2 Open Reconciliation Items
| ID | Issue | Severity | Owner |
| --- | --- | --- | --- |
| RI-076-001 | AIRA-DOC-023B exists as the Architecture Fitness Function Catalog; AIRA-DOC-076 should be registered as the executable gate pack companion, not a duplicate authority. | Medium | 00E / Architecture Board |
| RI-076-002 | Tool choices may vary by repository maturity. Gate requirements must remain tool-neutral while Golden Paths pin the implementation. | Low | DevSecOps Lead |
| RI-076-003 | Existing Dynamic Workspace and MicroFunction documents contain fitness language that should cross-reference this gate pack after adoption. | Medium | Solutions Architecture Office |
| RI-076-004 | System Builder must generate candidate gate metadata but must not downgrade gate severity or self-waive failures. | High | AI Governance / Security |

## 12.3 AVCI Compliance Summary
| AVCI Property | Evidence in This Gate Pack |
| --- | --- |
| Attributable | Defines document owner, co-owners, gate owners, tool owners, evidence locations, PR/MR links, and waiver authority. |
| Verifiable | Requires executable gate reports, policy results, architecture tests, contract checks, migration checks, resilience evidence, and evidence manifest validation. |
| Classifiable | Requires classification for code, evidence, logs, traces, prompts, AI routes, Dynamic Workspace outputs, screenshots, and gate results. |
| Improvable | Turns failures, waivers, drift, bypass attempts, and recurring defects into backlog, rule-pack, training, golden-path, and standard-update candidates. |

Architecture Fitness Is Executable Governance - Gates Fail Closed - AVCI Always

