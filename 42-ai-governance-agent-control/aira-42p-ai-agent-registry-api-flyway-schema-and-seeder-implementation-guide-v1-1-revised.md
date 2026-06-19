---
title: "AI Agent Registry API Flyway Schema and Seeder Implementation Guide"
doc_id: "AIRA-42P"
version: "v1.1"
status: "revised"
category: "AI governance and agent control"
source_docx: "AIRA_42P_AI_Agent_Registry_API_Flyway_Schema_and_Seeder_Implementation_Guide_v1.1_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 42-ai-governance-agent-control
  - revised
  - aira-42p
---



# AI Agent Registry API Flyway Schema and Seeder Implementation Guide



AIRA
AI-Native Enterprise Platform

AIRA AI Agent Registry API, Flyway Schema, and Seeder Implementation Guide

Authoritative Registry Implementation | Contract-First APIs | Flyway-Only Data Model | Seed Governance | AVCI Evidence
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-042P |
| Canonical Filename | 42P-AIRA_AI_Agent_Registry_API_Flyway_Schema_and_Seeder_Implementation_Guide_v1.1_Revised.docx |
| Version | v1.1 - Revised Alignment Update |
| Supersedes | 42P-AIRA_AI_Agent_Registry_API_Flyway_Schema_and_Seeder_Implementation_Guide_v1.0_a11y.docx |
| Status | Draft for Architecture / Security / DevSecOps / DBA / AI Governance Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Security Architecture; AI Governance; DevSecOps Lead; DBA; Platform Engineering; Software Development Lead; QA/SDET; Internal Audit |
| Primary Parent | 42O-AIRA AI Agent Runtime Registry Schema and Evidence Data Model Standard |
| Companion Sources | 42D-42N AI Agent Governance Controls; 42O Registry Model; 42Q Admin Workspace; 42R UAT/ORR; 42S Roadmap; 01/01B AVCI; 15/15A API; 16/16A/16B Flyway; 17/17A Security; 31A Observability; 32 SBAC; 41B/44A System Builder |
| Effective Date | Upon ARB / Security Governance / DevSecOps / DBA approval |
| Review Cadence | Quarterly; unscheduled on material registry, API, Flyway, seed, policy, tool gateway, model route, or evidence-model change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / AI-Governance / Agent-Registry-Implementation / v1.1/ |

Register every agent - Expose only governed APIs - Change data through Flyway - Seed by evidence - Fail closed - AVCI Always

# Mandatory Practice Statement

The AIRA AI Agent Registry is a Tier-0 governance control for agent identity, lifecycle, SBAC scope, OPA policy binding, tool authorization, model-route eligibility, memory/context eligibility, runtime events, certification, incidents, and decommission proof. It must be implemented as a governed backend capability with contract-first APIs, Flyway-only schema changes, deterministic seed-package governance, RLS/classification controls, observability, and evidence by construction.

No agent, tool/MCP gateway, policy bundle, model route, seed package, or runtime assurance event may become active through ad-hoc database inserts, manual production mutation, unmanaged scripts, direct SQL shortcuts, or unreviewed AI-generated configuration. The System Builder may draft candidate registry records, migrations, APIs, seed files, tests, and evidence manifests, but activation requires maker-checker review, CI/CD gates, OPA/SBAC validation, DBA review, and AVCI evidence.

# Static Table of Contents

Executive Summary

Purpose, Scope, and Authority

v1.1 Alignment Summary

Relationship to the AIRA AI Agent Control Set

Target Implementation Architecture

Registry API Implementation Standard

Flyway Schema and Migration Implementation Standard

Seeder Package and Reference Data Governance

Security, RLS, Classification, and Secrets Hygiene

Dynamic Workspace, System Builder, and MicroFunction Integration

Eventing, Outbox, DLQ, Replay, and Evidence Events

Observability, Runtime Toggles, and Assurance Views

CI/CD, GitNexus, Testing, and Resilience Lab Gates

Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loops

RACI

Implementation Roadmap

Acceptance Criteria and Definition of Done

AVCI Compliance Summary

# 1. Executive Summary

This v1.1 revised guide converts the 42O authoritative registry and evidence data model into an executable implementation baseline. It defines the backend registry service, OpenAPI and AsyncAPI contracts, PostgreSQL/Flyway schema ownership, seed package structure, runtime event capture, evidence correlation, testing gates, and developer execution controls required to implement the AIRA AI Agent Registry safely.

The registry is not a documentation inventory and not a dashboard-only catalog. It is the governed backend control plane that prevents shadow agents, invisible tool grants, disconnected evidence, stale credentials, unregistered model routes, unapproved memory context, and unverifiable AI-generated claims.
| Strategic Outcome | Implementation Result |
| --- | --- |
| Registry as authority | PostgreSQL/Flyway-governed registry tables hold authoritative agent, policy, tool, route, memory, certification, incident, and evidence state. |
| Contract-first control | OpenAPI and AsyncAPI exist before implementation; generated clients and event consumers use approved contracts only. |
| Flyway-only change | Schemas, indexes, RLS policies, views, reference data, and seed records are created and evolved through Flyway or approved migration workflow. |
| Evidence by construction | Every protected create, activate, tool grant, model-route grant, memory write, incident, and decommission event links to trace_id, policy_decision_id, approval_ref, and evidence_ref. |
| Fail-closed runtime | Unknown agent, missing owner, expired credential, stale certification, missing OPA/SBAC policy, missing evidence, or unapproved route blocks protected action. |

# 2. Purpose, Scope, and Authority

## 2.1 Purpose

Define the implementation path for the 42O AI Agent Runtime Registry schema and evidence model.

Specify contract-first APIs and event contracts for registry, evidence, policy decision, tool action, runtime event, memory/RAG, certification, incident, and decommission records.

Define Flyway migration sequencing, schema ownership, seed governance, data validation, and evidence requirements.

Prevent direct SQL shortcuts, unmanaged seed scripts, shadow registries, unreviewed AI-generated data, and dashboard-as-authority failure modes.

Provide developer, DBA, DevSecOps, System Builder, and AI Governance execution controls for registry implementation.

## 2.2 Scope
| In Scope | Out of Scope |
| --- | --- |
| Registry service API, OpenAPI contracts, generated clients, policy decision records, evidence APIs, runtime events, and Admin Workspace integration. | Replacing 42D-42O governance standards or making frontend screens the authorization authority. |
| Flyway migrations, PostgreSQL schemas, RLS/classification metadata, audit/evidence schema, indexes, views, and deterministic seed packages. | Manual production DDL, direct production SQL mutation, local-only seed scripts, or spreadsheet-driven registry authority. |
| Seeder package design, validation reports, CI/CD gates, GitNexus impact evidence, restore validation, and resilience tests. | Full production rollout without ARB/CAB/Security/DBA approval and operational readiness acceptance. |
| System Builder drafting of candidate APIs, migrations, seed records, tests, and evidence manifests. | System Builder self-approval, production activation, direct credential use, or direct model-provider execution. |

## 2.3 Authority and Precedence
| Level | Authority | Role |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance | Final authority for production-impacting registry controls, identity policy, exceptions, and material architecture decisions. |
| L1 | AVCI, Engineering Blueprint, AI Governance, Security, Database/Flyway, DevSecOps, Observability | Universal governance, architecture, security, rollback, policy, migration, testability, and evidence discipline. |
| L2 | 42O Runtime Registry Data Model | Defines canonical data domains and evidence model implemented by this guide. |
| L2 | This 42P Implementation Guide | Defines API, Flyway, seeding, validation, and delivery implementation baseline. |
| L3 | OpenAPI/AsyncAPI, Flyway migrations, seed packages, OPA/SBAC policies, CI/CD evidence | Executable implementation artifacts. |

Conflict Rule: Where this guide conflicts with a stricter AIRA source, apply the stricter rule, log the issue in Register 00D as an AVCI reconciliation item, and do not silently choose the easiest interpretation.

# 3. v1.1 Alignment Summary
| Alignment Area | v1.1 Required Improvement |
| --- | --- |
| 42O registry model | Implements the authoritative registry, identifiers, runtime event chain, OpenAPI/AsyncAPI contracts, Flyway-only schema, RLS, drift detection, and assurance views. |
| 42D-42N controls | Maps identity, runtime security, autonomy, threat model, tool/MCP, memory/RAG, certification, incident, delegation, supply-chain, and policy-as-code fields to registry APIs and tables. |
| Dynamic Workspace / Admin Workspace | Uses backend APIs only; frontend may display, request, and route governed actions but cannot authorize, activate, or mutate registry truth. |
| MicroFunction and System Builder | Registry operations are exposed through governed capabilities, typed contracts, OPA/SBAC decisions, idempotency keys, audit/evidence records, and maker-checker approval. |
| DevSecOps and evidence | Adds CI/CD gates for OpenAPI/AsyncAPI, Flyway clean-migrate, seed validation, policy tests, security scans, SBOM/provenance, GitNexus impact, and evidence pack closure. |

# 4. Relationship to the AIRA AI Agent Control Set
| Control | 42P Implementation Relationship |
| --- | --- |
| 42D Identity Lifecycle | Stores agent identity, owners, backup owners, credential references, JML status, recertification events, and decommission records. |
| 42E Runtime Security | Records runtime assurance events, tripwires, dashboard data, containment status, and kill-switch state. |
| 42F Autonomy and Trust | Stores autonomy tier, trust tier, delegation permissions, authority ceiling, human handoff rules, and promotion/demotion evidence. |
| 42G Threat Model | Links threat IDs, abuse-case controls, attack-surface tags, red-team results, and mitigation evidence to registry artifacts. |
| 42H Tool/MCP Gateway | Stores tool manifest references, tool scopes, action risk tier, dry-run requirement, approval rule, OPA binding, and rollback path. |
| 42I Memory/RAG Integrity | Stores source eligibility, context assembly, retrieval decisions, poison quarantine status, memory writes, and RAG evaluation evidence. |
| 42J Certification | Stores certification pack ID, evaluation result, exception status, expiry, trust promotion eligibility, and recertification due date. |
| 42K Incident Response | Stores incident references, forensic evidence, kill-switch scope, containment state, recovery approval, and reinstatement gate. |
| 42L Delegation Chain | Stores delegation-chain policy, authority ceiling, ledger references, loop/cascade limits, and orchestration approval. |
| 42M Supply Chain | Stores artifact provenance, MCP/plugin/connector references, SBOM, signature, license, scan result, and quarantine status. |
| 42N Policy-as-Code | Uses OPA/SBAC input/output schemas, decision IDs, rule package versions, policy bundle lifecycle, and policy test evidence. |

# 5. Target Implementation Architecture

The implementation architecture must preserve Clean Architecture and ports/adapters. Domain and application logic must not depend on the database driver, HTTP framework, Kafka client, LiteLLM provider, dashboard, or frontend state. Controllers and event consumers are adapters; the registry application service enforces use cases; persistence, OPA, Keycloak, Vault/OpenBao, Kafka, and evidence stores are reached through ports.
| Layer | Implementation Responsibility | Forbidden Shortcut |
| --- | --- | --- |
| API Adapter | Expose approved REST endpoints from OpenAPI and generated clients. | No ad-hoc endpoints, no business authority in controllers, no raw SQL from controller. |
| Application Use Case | Validate request, resolve actor/agent, enforce idempotency, call OPA/SBAC, produce audit/evidence, invoke repository port. | No direct database driver, Kafka client, model provider, or secret value handling. |
| Domain Model | Represent agent lifecycle invariants, state transitions, approval rules, authority ceilings, and evidence requirements. | No framework dependency or infrastructure-specific model leakage. |
| Persistence Adapter | Implement repository ports against PostgreSQL registry schemas. | No direct cross-context writes and no bypass of RLS/classification rules. |
| Event Adapter | Publish runtime and registry events through outbox and AsyncAPI-governed consumers. | No direct non-transactional event publish for protected state changes. |
| Evidence Adapter | Create append-only evidence records and evidence pack manifests. | No mutable evidence record and no missing trace/evidence correlation. |

# 6. Registry API Implementation Standard
| API Family | Required Capabilities | Controls |
| --- | --- | --- |
| Agent Registry API | Create draft agent, read registry record, submit update, activate, suspend, revoke, retire, create new immutable version. | Maker-checker for activation and material changes; idempotency key for mutating requests; OPA/SBAC decision required. |
| Agent Evidence API | Attach evidence, register evidence manifest, close evidence pack, link audit and CI evidence. | Append-only where applicable; classification-aware; retention-bound; evidence_ref mandatory. |
| Agent Decision API | Record OPA/SBAC inputs, outputs, reason codes, decision TTL, and policy version. | No overwrite of policy decisions; corrections are new records. |
| Agent Tool Action API | Record tool requests, dry-runs, approvals, execution results, rollback metadata, and Harness results. | Must integrate with 42H Tool/MCP Gateway and respect risk tier. |
| Agent Runtime API | Start run record, update runtime status, capture route, guardrail, context, model, tool, and result evidence. | trace_id, request_id, agent_run_id, policy_decision_id, and evidence_ref must be present where required. |
| Admin Workspace API | Serve dashboard, review workflow, certification, recertification, incident, and assurance views. | Read-only or request-routed UI behavior; frontend cannot become authority. |

API design requirements: use OpenAPI before implementation; require Problem Details safe error responses; document authentication, authorization scopes, SBAC skill requirements, classification ceiling, idempotency behavior, pagination, filtering, optimistic concurrency, audit events, and rate limits.

# 7. Flyway Schema and Migration Implementation Standard
| Schema Area | Minimum Tables / Objects | Mandatory Treatment |
| --- | --- | --- |
| aira_agent | agent_registry, agent_version, agent_owner, agent_status_history | Agent identity and lifecycle state are authoritative and versioned. |
| aira_agent_sec | agent_credential_ref, agent_access_review, agent_recertification | Secret values are never stored; only logical references and credential metadata. |
| aira_agent_policy | agent_sbac_grant, agent_policy_binding, agent_policy_decision | OPA/SBAC version, input hash, output, reason, TTL, and evidence are retained. |
| aira_agent_tool | tool_manifest_ref, agent_tool_scope, tool_action_request, tool_action_result | Tool scope is default-deny, manifest-bound, risk-tiered, and rollback-aware. |
| aira_agent_model | agent_model_route, agent_guardrail_binding, model_invocation_event | LiteLLM aliases only; direct provider calls are prohibited. |
| aira_agent_memory | context_source_ref, retrieval_decision, context_assembly, memory_write | Source eligibility, freshness, quarantine, and memory-write approvals are tracked. |
| aira_agent_run | agent_run, agent_runtime_event, agent_tripwire_event | Runtime events carry trace_id, request_id, policy_decision_id, and evidence_ref. |
| aira_agent_evidence | evidence_manifest, certification_result, incident_evidence_chain, decommission_certificate | Evidence is append-only or versioned and retention-bound. |

Every migration must include a migration evidence header with ticket, owner, bounded context, classification, purpose, verification evidence, rollback/forward-fix, and reviewer.

Greenfield and ongoing migrations use Flyway from Day 0; manual production DDL is prohibited except approved break-glass with follow-up migration and reconciliation.

Breaking schema changes must use expand/contract migration with compatibility windows, consumer migration, and rollback/deactivation strategy.

RLS, tenant/environment scope, classification metadata, retention flags, legal-hold flags, and audit columns must be designed with the initial schema, not added as an afterthought.

# 8. Seeder Package and Reference Data Governance

Seed data in 42P is governance data. It must be deterministic, idempotent, classified, owner-approved, effective-dated, and evidence-backed. Seed packages are not informal bootstrap scripts and must not contain production secrets, real personal data, uncontrolled prompts, or environment-specific credentials.
| Seed Category | Examples | Governance Rule |
| --- | --- | --- |
| Lifecycle states | draft, review, approved, active, suspended, revoked, retired, decommissioned | Seed through versioned Flyway reference-data migration or approved seeder package. |
| Risk and autonomy tiers | T0-T5, low/medium/high/critical, advisory/read/draft/tool/request/execute/prohibited | Trace to 42F and 42H; changes require AI Governance and Security review. |
| Policy decision outcomes | allow, deny, escalate, require_approval, quarantine, suspend, revoke | Trace to 42N OPA/SBAC decision contract and tests. |
| Runtime event types | agent.registered, agent.run.started, policy.decision.recorded, tool.action.requested, memory.context.assembled | Trace to AsyncAPI/CloudEvents schema and observability dashboard fields. |
| Certification levels | certification_pending, certified_nonprod, limited_delegated, expired, revoked | Trace to 42J certification gate and recertification lifecycle. |

# 9. Security, RLS, Classification, and Secrets Hygiene
| Control | Implementation Requirement |
| --- | --- |
| Authentication | All APIs require approved identity token validation through gateway/security adapter; unauthenticated requests fail closed. |
| Authorization | Every protected API route and event consumer evaluates OPA/SBAC with actor, agent, action, resource, environment, classification, risk tier, and requested outcome. |
| RLS / tenant scope | Tenant, environment, workspace, and Restricted records enforce RLS or equivalent database and service-layer constraints. |
| Secrets hygiene | Registry stores only logical secret_path_ref, workload_identity_ref, lease metadata, TTL, rotation_due, and revoked_at; never secret values. |
| Classification and redaction | Every table/API/event carries classification and redaction behavior; dashboards and logs redact secrets, PII, Restricted data, and sensitive prompts. |
| Separation of duties | Agent owner, policy approver, tool approver, certification reviewer, DBA, and promoter roles remain separable. |
| Authenticated DAST | Authenticated DAST must use synthetic non-prod identities and validate access denial, elevation attempts, IDOR, unsafe errors, and API authorization failures. |

# 10. Dynamic Workspace, System Builder, and MicroFunction Integration

The registry implementation supports Dynamic Workspace and System Builder, but it does not delegate authority to frontend state or AI-generated proposals. The Admin Workspace may display, request, review, and route actions. Backend APIs, OPA/SBAC policy, maker-checker workflows, Flyway-governed data, and evidence records decide and preserve truth.
| Integration Surface | Required Binding |
| --- | --- |
| Dynamic Workspace Admin Screens | Use generated clients from OpenAPI; no direct database access; no frontend-only activation, tool grant, model route, or decommission closure. |
| System Builder | May draft candidate agent records, APIs, migrations, seed files, tests, policies, evidence manifests, and PR/MR summaries; cannot approve or activate its own output. |
| MicroFunction Runtime | Registry actions are capability-bound MicroFunctions with receive, correlate, resolve actor, authorize/classify, validate, idempotency, execute, audit, outbox, and evidence steps. |
| Workflow / Human Approval | Material state transitions route to Flowable or approved maker-checker workflow with requester/approver separation. |
| AI Assistant Panel | May summarize registry evidence and propose next actions; cannot override OPA/SBAC, evidence, certification, or approval status. |

# 11. Eventing, Outbox, DLQ, Replay, and Evidence Events

Registry events are first-class governance evidence. Cross-boundary publication must use transactional outbox, AsyncAPI and CloudEvents-compatible schemas, idempotent consumers, schema evolution controls, DLQ, replay, and trace reconstruction.
| Event Type | Required Fields | Eventing Control |
| --- | --- | --- |
| agent.registered | agent_id, owner_id, lifecycle_state, classification_ceiling, evidence_ref | Published after committed registry write. |
| agent.run.started | agent_run_id, agent_id, agent_version_id, requester_id, trace_id, request_class | Correlates runtime invocation to registry state. |
| policy.decision.recorded | policy_decision_id, agent_run_id, opa_package, decision, reason, evidence_ref | Append-only; cannot be overwritten. |
| tool.action.requested | tool_action_id, agent_run_id, tool_id, action_code, risk_tier, approval_required | Routes to 42H gateway controls and approval workflow. |
| model.route.used | agent_run_id, model_alias, route_policy_id, guardrail_result, token_usage, classification | Direct provider calls are rejected. |
| memory.context.assembled | context_assembly_id, source_ids, classification, context_hash, freshness_result | Unapproved/stale/quarantined context blocks protected output. |
| decommission.completed | agent_id, revoked_credentials, disabled_routes, denial_tests, approval_ref | Cannot close without denial tests and evidence archival. |

# 12. Observability, Runtime Toggles, and Assurance Views
| Signal / Control | Requirement |
| --- | --- |
| Trace | Registry APIs, OPA decisions, tool gateway calls, model route calls, memory assembly, outbox events, and evidence writes propagate trace_id and span_id. |
| Logs | Use structured Log4j2-style application logs; no secrets, raw JWT, raw prompt, raw PII, raw Restricted content, or raw model output leakage. |
| Metrics | Expose registry completeness, drift findings, unlinked events, policy decision failures, DAST findings, seed validation, Flyway failures, and evidence reconstruction rate. |
| Runtime toggles | Telemetry verbosity, sampling, dashboard debug, AI summarization, seeder dry-run, and expensive diagnostics may be toggled only through governed configuration with audit and expiry. |
| Assurance views | Dashboards are derivative evidence views; if dashboard conflicts with PostgreSQL registry, registry plus evidence records govern. |

# 13. CI/CD, GitNexus, Testing, and Resilience Lab Gates
| Gate | Required Evidence |
| --- | --- |
| OpenAPI / AsyncAPI contract gate | Lint, schema validation, examples, generated clients, compatibility checks, safe error examples, idempotency tests. |
| Flyway gate | Clean migrate from empty PostgreSQL, Flyway validate, checksum report, schema diff, RLS tests, seed validation, rollback/forward-fix statement. |
| Security gate | SAST, SCA, secret scan, container scan, authenticated DAST, OPA/SBAC policy tests, permission negative tests. |
| Architecture fitness gate | No direct provider SDK, no direct SQL from controller/domain, no frontend authority, no cross-context database write, no unmanaged scripts. |
| GitNexus impact gate | Read-only impact analysis for affected APIs, schemas, seed files, policies, tests, dashboards, and downstream consumers. |
| Resilience lab gate | Concurrent activation attempts, duplicate idempotency keys, outbox replay, DLQ replay, database contention, cache loss, OPA unavailable, evidence store unavailable, and partial failure scenarios. |

# 14. Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loops

Auto-Heal, Auto-Learn, and Auto-Improve are proposal-driven. They may detect registry drift, missing evidence, stale credential metadata, failed policy binding, seed mismatch, contract regression, or RLS failure. They may retrieve evidence, draft a candidate fix, generate tests, prepare a PR/MR, and request human approval. They must not silently mutate registry state, disable controls, approve their own output, alter production schema, or suppress audit evidence.
| Loop | Allowed Candidate Output | Promotion Gate |
| --- | --- | --- |
| Auto-Heal | Incident ticket, evidence pack, candidate migration, seed correction, policy test, rollback/forward-fix plan. | Human approval, DBA/Security review, CI/CD green, CAB where production-impacting. |
| Auto-Learn | Reviewed knowledge update, playbook improvement, policy test case, dashboard metric improvement. | Knowledge steward review, source citations, classification check, Obsidian/LLM Wiki publication gate. |
| Auto-Improve | Refactoring proposal, API improvement, schema performance index proposal, event contract hardening, test coverage gap closure. | ADR/TDL if material, architecture fitness, performance evidence, security scan, rollback evidence. |

# 15. RACI
| Activity | Architecture | DBA | DevSecOps | Security / AI Gov | Developers | QA/SDET | Audit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Define schema/API baseline | A | C | C | C | R | C | I |
| Create Flyway migrations | C | A/R | C | C | R | C | I |
| Create OpenAPI/AsyncAPI contracts | A | C | C | C | R | C | I |
| Approve seed package | C | A/R | C | A/R | R | C | I |
| Run CI/CD/security gates | I | C | A/R | C | R | R | I |
| Approve activation workflow | A | C | C | A/R | I | C | C |
| Retain evidence pack | C | C | A/R | C | C | C | A |

# 16. Implementation Roadmap
| Phase | Focus | Exit Evidence |
| --- | --- | --- |
| F0 | Confirm source authority, document register entry, owners, classification, and 00D reconciliation items. | Register update, owner approval, classification record. |
| F1 | Create API and event contract drafts for registry, evidence, decision, tool action, runtime, memory, incident, and decommission. | OpenAPI/AsyncAPI PR, lint report, generated client proof. |
| F2 | Create Flyway baseline for registry schemas, RLS, indexes, views, audit/evidence tables, and seed reference data. | Clean-migrate report, validation report, schema review, DBA approval. |
| F3 | Implement service use cases with ports/adapters, idempotency, OPA/SBAC, outbox, audit, and evidence emission. | Unit/integration/contract tests, architecture fitness evidence. |
| F4 | Connect Admin Workspace, System Builder, Tool/MCP Gateway, LiteLLM route, memory/RAG, and observability integrations. | Smoke tests, dashboard sample, denied-action evidence, trace reconstruction. |
| F5 | Run security, authenticated DAST, resilience lab, replay, restore, and evidence reconstruction tests. | Evidence pack, remediation register, approval record. |
| F6 | Pilot non-prod registry with controlled agents and prepare 42Q/42R readiness path. | Pilot report, UAT readiness, ORR/CAB entry evidence. |

# 17. Acceptance Criteria and Definition of Done

All registry database objects are created through Flyway with migration evidence headers, clean-migrate proof, validation proof, and DBA review.

OpenAPI and AsyncAPI contracts exist before implementation and pass lint, compatibility, example, generated-client, and contract tests.

No protected registry action executes without lifecycle state, SBAC scope, OPA policy decision, tool/model/memory eligibility, trace_id, and evidence_ref where required.

Seed packages are deterministic, idempotent, classified, owner-approved, effective-dated, and validated in CI.

Dynamic Workspace and Admin Workspace consume only governed APIs and cannot authorize or directly mutate registry truth.

System Builder outputs remain candidate artifacts until PR/MR review, CI/CD evidence, policy evidence, and human approval are complete.

Authenticated DAST, RLS tests, access negative tests, secret scans, architecture fitness, and resilience lab tests pass or have approved waivers.

Outbox, idempotent consumers, DLQ, replay, and event schema evolution are tested for registry events.

Observability dashboards can reconstruct selected actions from request, agent run, policy decision, tool/model/context result, evidence pack, review, and improvement record.

Rollback, forward-fix, compensation, deactivation, restoration, denial tests, and decommission proof are defined and tested where applicable.

# 18. AVCI Compliance Summary
| AVCI Element | How 42P Satisfies It | Evidence |
| --- | --- | --- |
| Attributable | Every API, migration, seed package, registry record, policy decision, runtime event, and evidence record has owner, source, version, approver, and responsible role. | Document control, PR/MR, migration headers, seed manifest, policy decision, evidence_ref. |
| Verifiable | Contracts, migrations, seeders, policies, RLS, DAST, resilience, replay, restore, and evidence reconstruction are tested through CI/CD and reviewed evidence packs. | OpenAPI/AsyncAPI reports, Flyway logs, test reports, GitNexus impact, dashboards, trace exports. |
| Classifiable | Registry data, seed data, API responses, telemetry, dashboards, evidence, and prompts carry classification and redaction rules. | Classification metadata, RLS policy, redaction tests, retention/disposal records. |
| Improvable | Incidents, drift, failed tests, assurance metrics, Auto-Heal/Auto-Learn/Auto-Improve candidates, and audit findings feed backlog and controlled improvement. | Improvement register, incident records, CAPA, reviewed knowledge updates, policy/test updates. |

Final Control Statement: AIRA 42P is accepted only when the AI Agent Registry can be built, tested, secured, seeded, observed, evidenced, rolled back or forward-fixed, and improved through governed APIs, Flyway migrations, OPA/SBAC policy, CI/CD gates, GitNexus evidence, and named human approval. Functional screens or passing local scripts alone are not acceptance evidence.

