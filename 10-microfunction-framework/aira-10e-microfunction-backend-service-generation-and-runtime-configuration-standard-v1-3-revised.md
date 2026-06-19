---
title: "MicroFunction Backend Service Generation and Runtime Configuration Standard"
doc_id: "AIRA-10E"
version: "v1.3"
status: "revised"
category: "MicroFunction framework"
source_docx: "AIRA_10E_MicroFunction_Backend_Service_Generation_and_Runtime_Configuration_Standard_v1.3_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 10-microfunction-framework
  - revised
  - aira-10e
---



# MicroFunction Backend Service Generation and Runtime Configuration Standard



AIRA
AI-Native Enterprise Platform

MicroFunction Backend Service Generation and Runtime Configuration Standard

Review, Correction, Alignment, Simplification, and Revised Standard
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-010E |
| Document Title | AIRA MicroFunction Backend Service Generation and Runtime Configuration Standard |
| Recommended Version | v1.3 Revised - Backend Generation, Runtime Configuration, Evidence, and Cross-Cutting Control Alignment |
| Source Reviewed | AIRA_10E_MicroFunction_Backend_Service_Generation_and_Runtime_Configuration_Standard_v1_2_Review_and_Revised.docx |
| Supersedes | 10E v1.2 candidate upon approval |
| Status | Draft for Architecture Review Board / CAB / Engineering Team Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Software Development; DevSecOps; Security; QA/SDET; DBA; AI Engineering; Platform Engineering; SRE; Internal Audit |
| Review Date | 2026-06-18 |
| Parent Baseline | 10 v3.4 Revised; 10A v2.4 Revised; 10B v2.3 Revised; 10C v2.3 Revised; 10D v2.3 Revised |
| Foundation Baseline | 01A v1.2; 01 v3.2; 01B v1.2; 02 v5.2; 03 v4.2; 04 v9.2; 05 v4.2; 06 v3.2; 07 v3.2; 07B v1.2 |

# Mandatory Practice Statement

AIRA backend service generation is not complete when a service compiles, starts, exposes an endpoint, or passes a happy-path test. It is complete only when generated source code, runtime configuration, contracts, migrations, policy, observability, tests, evidence, rollback, and approval records prove that the service is configurable, secure, observable, retry-safe, duplicate-safe, policy-governed, human-accountable where required, and AVCI-compliant.

System Builder, AI coding assistants, and automation services may recommend, draft, generate candidates, and prepare PR/MR-ready artifacts. They must not approve their own output, silently mutate runtime behavior, bypass OPA/SBAC/Harness/guardrails, alter production directly, or promote changes without maker-checker review and evidence.

# Table of Contents

1. Executive Review Summary

2. Source and Context Alignment

3. Corrections and Reconciliation

4. Purpose, Scope, Authority

5. Generation Control Plane

6. Backend Service Reference Structure

7. Runtime Configuration Lifecycle

8. Contract, Event, Database, and Security Controls

9. Observability, Resilience, Runtime Toggles, and Auto-* Controls

10. Testing, CI/CD, Evidence Pack, and Rejection Rules

11. Review Queue, Acceptance Criteria, RACI, and AVCI Summary

# 1. Executive Review Summary

The uploaded v1.2 candidate is directionally correct. It treats backend generation and runtime configuration as governed System Builder outputs rather than autonomous production mutation, and it recognizes five AIRA intake families: new requirements, operational/engineering evidence, improvement requests, AI agent lifecycle governance, and AI DevSecOps provisioning.

The v1.3 revision updates 10E to inherit the completed MicroFunction suite now established in this workstream: 10 v3.4, 10A v2.4, 10B v2.3, 10C v2.3, and 10D v2.3. It also corrects version drift in the review queue, strengthens generated-backend acceptance gates, and converts cross-cutting controls into concrete generated artifacts and evidence.
| Review Area | v1.3 Treatment |
| --- | --- |
| Retain | Governed System Builder generation, no silent mutation, runtime configuration lifecycle, contract-first APIs/events, Flyway-only changes, security, observability, evidence, and human approval boundaries. |
| Correct | Replace stale parent references to 10 v3.3 / 10A v2.3 / 10B v2.2 / 10C v2.2 / 10D v2.2 with the current revised suite. |
| Strengthen | Make generated outputs include OpenAPI, AsyncAPI, Avro/JSON Schema, CloudEvents, outbox, idempotency, DLQ, replay, Log4j2/OTel/Sentry/Loki/Tempo/Grafana, OPA/SBAC, DAST, GitNexus, SBOM/provenance, rollback and evidence by default. |
| Simplify | Use a practical generation lifecycle, backend package model, implementation checklist, non-negotiable rejection rules, and evidence-pack definition. |
| Govern | AI and Auto-Heal/Learn/Improve remain candidate/proposal loops unless a governed action tier, policy decision, Harness path, evidence pack, rollback, and human approval permit bounded action. |

# 2. Source and Context Alignment
| Alignment Source | Required 10E Treatment |
| --- | --- |
| 10 MicroFunction Framework v3.4 | Generated services must implement configure-first runtime assembly, standard reusable concerns, catalog governance, idempotency, outbox, DLQ/replay, resilience, observability, security and AVCI evidence. |
| 10A Design and Development Guide v2.4 | Generated outputs must reuse standard steps first, prefer rules/DMN/OPA/configuration before coded STP-BUS logic, and include a MicroFunction Design Record. |
| 10B Implementation Standard v2.3 | Generated Java/Spring code must preserve package boundaries, ports/adapters, execution envelope, validators, policy hooks, tests and evidence hooks. |
| 10C Sequence Diagrams v2.3 | Generated code/configuration must map to approved sequence evidence for synchronous, event-driven, workflow, AI/RAG/tool, Auto-* and runtime-toggle flows. |
| 10D Catalog and Assembly Templates v2.3 | Generated runtime configuration must use catalog metadata, assembly templates, publish-time validators and standard step definitions. |
| 01A / 01 / 01B / 02 | Generated artifacts must satisfy EDP-01 to EDP-20 and remain attributable, verifiable, classifiable and improvable. |
| 15 / 15A API Standards | APIs and events are contract-first using OpenAPI, AsyncAPI, safe errors, CloudEvents metadata, schema evolution and idempotency. |
| 16 / 16A / 16B Database Standards | Schemas, seed data, runtime configuration, RLS, outbox, idempotency and migrations are Flyway-governed. |
| 17 / 17A Security Standards | Generated services enforce Keycloak/OIDC, SBAC, OPA, secrets hygiene, classification, fail-closed behavior and secure defaults. |
| 20 / 31A DevSecOps and Observability | Generated services produce CI/CD, GitNexus, scan, SBOM/provenance, telemetry, audit, dashboard, alert and evidence-pack outputs. |
| 41B / 44 System Builder and 42 AI Governance | System Builder may analyze, recommend, draft and prepare PRs; it must not silently mutate runtime, production, policy, database or environment state. |

# 3. Corrections and Reconciliation Decisions
| Correction | Decision |
| --- | --- |
| Version promotion | The source is already v1.2 candidate, so the corrected output is v1.3 Revised. |
| Parent baseline | Use 10 v3.4, 10A v2.4, 10B v2.3, 10C v2.3 and 10D v2.3 as current MicroFunction candidate baseline. |
| Foundation references | Use completed foundation candidates through 07B and avoid claiming 08/08A/09 are completed in this current upload sequence unless separately verified. |
| Review queue | Mark 10E as completed after this revision. Next recommended document becomes 11-AIRA_AI_Native_DevSecOps_Standard_v3.2_Revised.docx. |
| Loose addendum handling | Embed cross-cutting backend generation rules into the governing standard body rather than treating them as optional appendix material. |
| AVCI reconciliation | Known numbering issues such as 11A duplicate numbering and 41B/44 System Builder overlap remain tracked items for Register 00D. |

# 4. Purpose, Scope, and Authority

## 4.1 Purpose

This standard defines how AIRA generates, validates, activates, operates, improves, suspends and retires MicroFunction-backed backend services and runtime configuration. It applies to human-authored, AI-assisted and System Builder-generated artifacts, including code, contracts, policies, migrations, tests, runtime configuration, evidence packs and runbooks.

## 4.2 Scope
| In Scope | Out of Scope |
| --- | --- |
| Java/Spring backend service skeletons, controllers, use cases, ports, adapters, DTOs, validators, MicroFunction runtime classes and tests. | Direct production mutation by AI, System Builder, agents, scripts, notebooks, or generated services. |
| Runtime configuration records, catalog bindings, RuntimeProcessDefinition, feature flags, parameters, retry/error/compensation policies and activation controls. | Hardcoded authorization, direct provider model SDK calls, direct database coupling, uncontrolled runtime shortcuts or frontend business authority. |
| OpenAPI, AsyncAPI, Avro/JSON Schema, CloudEvents, outbox, Kafka publishing/consumption, DLQ, replay, idempotent consumer, schema evolution and event evidence. | Manual DDL, unmanaged event formats, undocumented replays, unsupported data repair or non-governed Kafka publishing. |
| DevSecOps gates, SAST/SCA/secrets scan, authenticated DAST, architecture fitness, GitNexus, SBOM/provenance and evidence pack generation. | Promotion without PR/MR evidence, CODEOWNERS, maker-checker review, ARB/CAB where required, or rollback/compensation path. |

## 4.3 Authority and Precedence
| Level | Authority | Meaning for 10E |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance / IT Head | Final authority for production-impacting generation, runtime activation, security exceptions and material conflicts. |
| L1 | 01A / 01 / 01B / 02 | Universal design-principle, quality, evidence, classification, audit and architecture authority. |
| L2 | 10 MicroFunction Framework v3.4 | Parent authority for runtime assembly, standard concerns and MicroFunction governance. |
| L3 | This 10E v1.3 Standard | Controls how backend services and runtime configuration are generated, validated, activated, monitored, improved and retired. |
| L4 | 10A/10B/10C/10D; API/DB/Security/DevSecOps/Observability standards | Specialist controls that generated artifacts must satisfy. |
| L5 | Tickets, ADRs, TDLs, PR/MR records, CI evidence, runbooks, activation records | Implementation proof that may tighten but must not weaken higher authority. |

# 5. Generation Control Plane

Figure 1. Backend generation is a governed control plane. Intake, analysis, recommendation, generation, validation, approval, activation, observability and improvement are separated so automation cannot become authority.

## 5.1 Generation Lifecycle
| Stage | Required Action | Required Evidence |
| --- | --- | --- |
| 1. Intake | Capture request, source, owner, bounded context, classification, risk, data handling and outcome. | Ticket, intake record, classification, owner, scope and acceptance criteria. |
| 2. Analysis | Check parent standards, affected contracts, schemas, policies, services, workflows, agents and evidence. | Impact analysis, dependency map, GitNexus candidate report and conflict list. |
| 3. Recommendation | Generate options, risks, affected artifacts, tests, policy changes, rollback and approvals required. | Recommendation record, ADR/TDL trigger and approval path. |
| 4. Candidate Generation | Generate backend skeleton, ports/adapters, configuration, contracts, migrations, tests, policies and runbooks in branch/sandbox. | Generated artifact manifest, branch, commit and AI-use record. |
| 5. Validation | Run tests, scans, policy checks, architecture fitness, migration validation, replay/concurrency and evidence checks. | CI results, test reports, scan outputs, migration validation and fitness evidence. |
| 6. Review | Perform maker-checker, CODEOWNERS, Security, DBA, Architecture and ARB/CAB when triggered. | Approvals, waivers, risk acceptance and SoD proof. |
| 7. Activation | Promote through controlled pipeline; publish active runtime configuration; invalidate caches; monitor. | Promotion evidence, activation record, cache invalidation event and runtime traces. |
| 8. Improvement | Capture defects, incidents, metrics, GitNexus impacts, lessons and candidates. | Backlog item, Auto-* proposal and monitoring evidence. |

# 6. Backend Service Reference Structure
| Generated Area | Mandatory Rule |
| --- | --- |
| API adapters | Controllers are thin adapters. No business rules, direct SQL, Kafka publishing, policy decisions, AI calls or workflow orchestration. |
| Application/use case layer | Coordinates ports, policies, validation results, MicroFunction runtime execution, idempotency and safe responses without framework dependency leakage. |
| Domain layer | Owns business language, invariants, value objects and business errors. No Spring, database, Kafka, OPA, Keycloak or model-provider dependency. |
| Ports | Define required capabilities such as repository, identity, policy, event, audit, observability, workflow, model gateway, evidence and external system actions. |
| Adapters | Implement external integrations with approved libraries/configuration and timeout, retry, resilience, redaction and evidence hooks. |
| MicroFunction runtime | Loads signed active RuntimeProcessDefinition from PostgreSQL authority, applies validation gates, executes the step envelope and emits evidence. |
| Configuration binding | Maps runtime configuration into immutable execution context with version pinning, feature flags, parameter sets and policy versions. |
| Tests | Generated tests prove positive, negative, boundary, failure, concurrency, idempotency, replay, contract, policy and evidence behavior. |

## 6.1 Generated Output Manifest
| Artifact Class | Required Generated or Updated Output |
| --- | --- |
| Source code | Controller adapters, application services, domain objects, ports, infrastructure adapters, MicroFunction classes, validators and error model. |
| Contracts | OpenAPI, AsyncAPI, Avro/JSON Schema, CloudEvents metadata, examples, compatibility checks and generated client/server stubs where approved. |
| Database/config | Flyway migrations, seed/reference data, runtime configuration rows, outbox/inbox/idempotency records, RLS/indexes where applicable. |
| Policy/security | OPA/Rego policies or tests, SBAC skill bindings, Keycloak/OIDC scopes, secret references, abuse cases and authenticated DAST setup. |
| Observability | Log4j2 profiles, OTel instrumentation, Sentry context, Loki labels, Tempo trace linkage, Grafana dashboards and alert rules. |
| Evidence | PR/MR AVCI summary, GitNexus impact, test reports, scan results, SBOM/provenance, rollback/compensation plan and approval records. |

# 7. Runtime Configuration Lifecycle

Figure 2. Runtime configuration progresses through controlled states and is reconstructable from source, version, hash/signature, approval, policy and evidence records.
| State | Meaning | Allowed Action |
| --- | --- | --- |
| Draft | Candidate runtime configuration created by developer, System Builder or AI assistant. | Edit in branch/sandbox; run lint and tests. |
| Reviewed | Configuration passed initial technical review and mandatory validators. | Prepare PR/MR and evidence pack. |
| Approved | Maker-checker, CODEOWNERS and Security/DBA/Architecture where required have approved. | Promote through CI/CD and activation workflow. |
| Active | Configuration version is effective after activation, hash/signature and cache invalidation. | Execute; monitor; audit; generate evidence. |
| Suspended | Configuration temporarily disabled due to incident, defect, policy failure or rollback. | Block or route to previous approved version. |
| Retired | Configuration version superseded and kept for lineage, audit, replay or rollback reference. | No new execution; retain evidence and lineage. |

# 8. Contract, Event, Database, and Security Controls

## 8.1 Contract-First API and Event Generation

Generate OpenAPI before controller implementation and use generated clients or stubs where practical.

Generate AsyncAPI and event schemas before Kafka producer or consumer implementation.

Use CloudEvents metadata for event identity, type, source, subject, time, data schema, trace correlation, classification and evidence reference.

Use Avro or approved schema formats with compatibility policy, schema version, owner, retention and migration plan.

Do not invent endpoints, topic names, error formats, event names, schema fields or response semantics outside approved contracts.

Every generated API or event must include authentication, authorization, classification, idempotency, validation, safe errors, observability and test evidence.

## 8.2 Database, Flyway, and Persistence Controls

All schema changes, seed data, runtime configuration tables, outbox tables, idempotency records, indexes, views, RLS policies, extensions and reference data must be delivered through Flyway or an approved migration workflow.

Generated code must not execute free-form SQL from runtime configuration.

PostgreSQL is authoritative for runtime configuration, audit, evidence, workflow lineage and outbox/idempotency authority. Redis, Valkey, Caffeine, dashboards and AI summaries are derivative only.

Generated repositories must use approved ports/adapters and must not leak persistence models into domain logic.

Migrations must include rollback, forward-fix, compensation or safe-disable strategy and CI validation evidence.

## 8.3 Security, OPA, SBAC, Guardrails, and Harness
| Security Area | Mandatory Generated Control |
| --- | --- |
| Fail closed | Generated services stop protected actions when identity, secrets, policy, guardrails, audit, runtime configuration or evidence controls are unavailable. |
| OPA/SBAC | Authorization is expressed through policy decisions and skill scopes, not hidden if/else role logic. |
| Secrets hygiene | No secrets in source, logs, prompts, screenshots, tests or documentation; use approved secret references and Vault-compatible abstractions. |
| AI gateway | AI/model traffic routes through approved LiteLLM or private gateways with guardrails and audit evidence. |
| Harness mediation | Agents do not receive direct credentials to Git, CI/CD, Kubernetes, databases, production APIs, OpenKM or runtime configuration stores. |
| Security testing | Include abuse cases, negative authorization tests, authenticated DAST where applicable, secret scanning, dependency scanning and remediation evidence. |

# 9. Observability, Resilience, Runtime Toggles, and Auto-* Controls
| Signal | Mandatory Generated Fields |
| --- | --- |
| Logs | timestamp, service, environment, trace_id, request_id, actor_hash, tenant, transaction_code, step_code, result, error_code, classification, evidence_ref. |
| Traces | trace_id, span_id, parent_span_id, transaction_code, runtime_definition_version, step_code, dependency, policy_decision_id, outbox_id, evidence_ref. |
| Metrics | request count, latency, error rate, saturation, retry count, timeout count, DLQ count, outbox lag, policy denies, cache hit/miss, SLO indicators. |
| Audit | actor, owner, source_ref, action, policy result, classification, before/after reference where safe, approval, evidence_ref, retention rule. |
| Evidence | artifact type, source commit, contract version, migration version, test run, scan result, GitNexus report, approval, rollback path, improvement path. |

## 9.1 Runtime Toggle Governance
| Control | May Be Tuned | Must Not Be Disabled |
| --- | --- | --- |
| Logging verbosity | Debug/trace verbosity, sampling rate, diagnostic categories and short-lived incident logging windows. | Security logs, auth denials, policy decisions, audit events, critical errors and evidence references. |
| Tracing | Trace sampling, baggage limits and low-risk span enrichment. | Trace_id propagation, correlation IDs, critical transaction spans, policy-decision correlation and evidence_ref. |
| Metrics | Metric cardinality, scrape interval, dashboard aggregation and non-critical labels. | SLO/SLA metrics, error rates, latency, saturation, security-denial counters and outbox/DLQ metrics. |
| Feature flags | Optional capabilities and progressive rollout controls. | Identity, classification, policy, validation, audit, idempotency, outbox, security and evidence controls. |
| AI features | AI advisory summaries and non-critical model-assisted diagnostics. | Guardrails, LiteLLM route enforcement, prompt/model audit, classification checks and human approval controls. |

## 9.2 Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop
| Step | Mandatory Control |
| --- | --- |
| Issue detection | Use telemetry, incidents, scans, test failures, GitNexus, user feedback and SLO signals as classified evidence inputs. |
| Evidence retrieval | Retrieve only approved evidence with classification, freshness, provenance and access checks. |
| Candidate proposal | Generate root-cause hypothesis, candidate fix/learning, risk, affected contracts/schemas/policies, tests and rollback. |
| Validation | Run deterministic tests, security checks, architecture fitness, contract checks, migration checks and replay/concurrency checks. |
| Human approval | Require named maker, checker, owner and approver where risk demands. AI cannot approve its own output. |
| Promotion | Promote only through PR/MR, CI/CD gates, ARB/CAB where required, evidence pack and monitored activation. |
| Learning | Approved lessons become curated knowledge, updated prompts, guardrails, tests, policies or MicroFunction configuration with lineage. |

# 10. Testing, CI/CD, Evidence Pack, and Rejection Rules

Figure 3. Generated services must produce a connected evidence chain from source request to runtime monitoring and improvement.

## 10.1 Testing and CI/CD Gates
| Gate | Generated Requirement |
| --- | --- |
| Unit and component tests | Prove use-case, domain, adapter, validation, idempotency and error behavior with deterministic fixtures. |
| Contract tests | Validate OpenAPI, AsyncAPI, Avro/schema, generated clients, safe error formats and backward compatibility. |
| OPA/SBAC tests | Validate allow, deny, escalate, classification, tenant, skill, trust and human approval rules. |
| Database tests | Validate Flyway clean/migrate, checksum, seed data, RLS, idempotency, outbox and rollback/forward-fix evidence. |
| Architecture fitness | Block direct controller business logic, direct provider SDK calls, direct SQL/domain leakage, unauthorized imports and missing ports/adapters. |
| Security tests | Run SAST, SCA, secrets scan, authenticated DAST where applicable, dependency risk checks and abuse-case tests. |
| Resilience/load tests | Validate retries, timeouts, circuit breakers, concurrency control, duplicate suppression, DLQ, replay and compensation. |
| Evidence-pack gate | Block promotion when required AVCI, test, scan, GitNexus, audit, observability, rollback or approval evidence is missing. |

## 10.2 Required Evidence Pack
| Evidence Category | Minimum Evidence |
| --- | --- |
| Attributable | Owner, developer, reviewer/checker, source request, ticket, branch, commit, AI tools used, prompt/model route, runtime configuration version. |
| Verifiable | Unit/component/contract/policy/security/migration/architecture/concurrency/replay tests, scan results, GitNexus report and dashboard/trace evidence. |
| Classifiable | Data classification, telemetry classification, prompt/model eligibility, retention rule, redaction proof, secret handling and evidence storage location. |
| Improvable | Known limitations, improvement backlog, Auto-Heal/Learn/Improve candidate records, lessons learned, prompt/standard updates and monitoring. |
| Reversible | Rollback, forward-fix, compensation, safe-disable feature flag, migration recovery, replay/reprocess plan and cache invalidation plan. |

## 10.3 Non-Negotiable Rejection Rules

Reject generated services that place business logic in controllers or adapters.

Reject generated code that bypasses Keycloak/OIDC, OPA/SBAC, Vault-compatible secret controls, LiteLLM, guardrails, Harness, audit, or evidence controls.

Reject generated runtime configuration that omits identity, classification, validation, idempotency, authorization, observability, audit or error path for mutating or sensitive transactions.

Reject generated database changes that are not Flyway-governed or that rely on manual production DDL.

Reject generated APIs/events that are not contract-first or that lack schema evolution, idempotency, safe errors and evidence correlation.

Reject generated observability that logs secrets, raw tokens, raw PII, raw prompts, raw documents or high-cardinality unsafe labels.

Reject Auto-Heal, Auto-Learn or Auto-Improve behavior that silently mutates production or authoritative sources.

Reject any runtime toggle that disables mandatory audit, policy decision, security, idempotency, outbox, critical error or evidence records.

# 11. Review Queue, Acceptance Criteria, RACI, and AVCI Summary

## 11.1 Review Queue Control Register
| Seq | File Name | Current | Recommended | Status | Next Step |
| --- | --- | --- | --- | --- | --- |
| 13 | 10-AIRA_MicroFunction_Framework | v3.4 | v3.4 | Completed / Revised | Use as parent MicroFunction baseline. |
| 14 | 10A-AIRA_MicroFunction_Design_and_Development_Guide | v2.4 | v2.4 | Completed / Revised | Use as design companion baseline. |
| 15 | 10B-AIRA_MicroFunction_Framework_Implementation_Standard | v2.3 | v2.3 | Completed / Revised | Use as implementation companion baseline. |
| 16 | 10C-AIRA_MicroFunction_Sequence_Diagrams_and_Mermaid_Reference | v2.3 | v2.3 | Completed / Revised | Use as sequence evidence baseline. |
| 17 | 10D-AIRA_MicroFunction_Standard_Function_Catalog_and_Assembly_Templates | v2.3 | v2.3 | Completed / Revised | Use as catalog/template baseline. |
| 18 | 10E-AIRA_MicroFunction_Backend_Service_Generation_and_Runtime_Configuration_Standard | v1.2 | v1.3 | Completed / Revised | Use as backend generation/runtime config baseline. |
| 19 | 11-AIRA_AI_Native_DevSecOps_Standard | v3.1 | v3.2 | Next for Review | Review next to align DevSecOps gates and evidence with the MicroFunction suite. |

## 11.2 Acceptance Criteria

10E v1.3 references the corrected MicroFunction suite: 10 v3.4, 10A v2.4, 10B v2.3, 10C v2.3 and 10D v2.3.

Generated backend outputs include code, contracts, runtime configuration, Flyway migrations, policies, tests, observability, evidence, rollback and approval records.

System Builder and AI assistants remain draft/candidate generators and cannot self-approve, silently mutate production, or bypass policy and evidence gates.

Generated services enforce contract-first APIs/events, Flyway-only database changes, OPA/SBAC, secrets hygiene, guardrails, Harness-mediated tool actions and fail-closed behavior.

Runtime toggles are governed, auditable and reversible and cannot disable mandatory security, audit, policy, idempotency, outbox or evidence signals.

The review queue advances to 11-AIRA_AI_Native_DevSecOps_Standard v3.2 review.

## 11.3 RACI
| Activity | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Approve 10E standard | Enterprise Architecture | Architecture Board / IT Head | DevSecOps, Security, DBA, QA, SRE | Engineering and Internal Audit |
| Generate candidate backend | System Builder Operator / Developer | Software Development Lead | Architecture, Security, QA, DBA | Product Owner |
| Validate runtime configuration | DevSecOps / QA | Platform Engineering Lead | Security, DBA, SRE | Release stakeholders |
| Approve production activation | Change Owner | CAB | Architecture, Security, QA, SRE | Affected teams |
| Promote learning/improvement | Knowledge Steward | Domain Owner | Architecture, Security, QA | Developers and AI users |

## 11.4 AVCI Compliance Summary
| AVCI Property | Evidence in 10E v1.3 Revised |
| --- | --- |
| Attributable | Defines owner, co-owners, source request, developer, reviewer, AI tools used, branch, commit, runtime configuration version and approval trail. |
| Verifiable | Requires tests, scans, GitNexus, SBOM/provenance, policy decisions, contracts, migrations, telemetry samples, evidence pack and activation records. |
| Classifiable | Requires classification for data, telemetry, prompts, model routes, evidence, logs, runtime configuration and retention/handling rules. |
| Improvable | Defines Auto-Heal/Learn/Improve candidate loops, backlog linkage, post-promotion monitoring, lessons, prompts, policies, tests and versioned change path. |

