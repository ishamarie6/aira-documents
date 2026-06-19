---
title: "AI Agent Runtime Registry Schema and Evidence Data Model Standard"
doc_id: "AIRA-42O"
version: "v1.1"
status: "revised"
category: "AI governance and agent control"
source_docx: "AIRA_42O_AI_Agent_Runtime_Registry_Schema_and_Evidence_Data_Model_Standard_v1.1_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 42-ai-governance-agent-control
  - revised
  - aira-42o
---



# AI Agent Runtime Registry Schema and Evidence Data Model Standard



AIRA

AI-Native Enterprise Platform

AI Agent Runtime Registry, Schema, and Evidence Data Model Standard

Authoritative Agent Registry | Canonical Runtime Schema | Evidence Correlation | Flyway-Governed Data Model | AVCI Always
| Document ID | AIRA-DOC-042O |
| --- | --- |
| Canonical Filename | 42O-AIRA_AI_Agent_Runtime_Registry_Schema_and_Evidence_Data_Model_Standard_v1.1_Revised.docx |
| Version | v1.1 Revised - AIRA v5.1 Alignment Update |
| Status | Draft for Architecture, Data Governance, Security, DevSecOps, AI Governance, Platform Engineering, QA/SDET, SRE / Operations, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; AI Governance; Security Architecture; DevSecOps Lead; Platform Engineering; Data Governance; DBA; QA/SDET; SRE / Operations; Internal Audit |
| Primary Parent | 42-AIRA AI Governance and Runtime Control Standard |
| Companion Sources | 01/01B AVCI; 15/15A API; 16/16A/16B Database/Flyway; 17/17A Security; 31A Observability; 32 SBAC; 41B/44A/44C System Builder and Agent Inventory; 42D-42N Agent Governance; 42P-42R Registry Implementation, Admin Workspace, and UAT/Readiness |
| Review Cadence | Monthly during agent-registry implementation; quarterly after controlled maturity; immediate review after registry, schema, policy, evidence, model-route, tool/MCP, memory/RAG, incident, certification, or audit change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / AI-Governance / Agent-Runtime-Registry / v1.1/ |

# Mandatory Practice Statement

The AIRA AI Agent Runtime Registry is the authoritative system of record for agent identity, lifecycle state, ownership, classification ceiling, SBAC scope, OPA policy references, tool authorization, model-route eligibility, credential metadata, memory/context eligibility, runtime events, evidence references, certification state, recertification, suspension, revocation, and decommissioning proof. PostgreSQL is the Tier-0 authority. Redis/Valkey, dashboards, embeddings, reports, LLM Wiki summaries, and AI-generated narratives are derivative views only and must never become the source of truth.

# Static Table of Contents

1. Executive Summary and v1.1 Alignment Verdict

2. Purpose, Scope, and Authority

3. Source Alignment and Control Relationships

4. Registry Control Model

5. Canonical Registry Data Domains

6. Authoritative Schema and Identifier Baseline

7. Agent Registry Entity Model

8. Evidence, Runtime Event, and Correlation Model

9. OpenAPI, AsyncAPI, CloudEvents, and Contract Requirements

10. Flyway, Data Governance, Security, RLS, and Retention

11. Data Quality, Reconciliation, Drift Detection, Metrics, and Assurance Views

12. Dynamic Workspace, System Builder, Tool/MCP, Memory/RAG, and DevSecOps Integration

13. Implementation Roadmap, Acceptance Criteria, RACI, and AVCI Summary

# 1. Executive Summary and v1.1 Alignment Verdict

AIRA-DOC-042O defines the canonical data backbone for AI agent governance. The 42D-42N control family defines what must be governed: identity, runtime control, autonomy, threat model, tool actions, memory, certification, incident response, delegation, supply chain, and policy-as-code. This standard defines the registry schema and evidence data model that make those controls executable, measurable, auditable, and reconstructable.

The v1.1 revision strengthens the baseline by aligning it with the revised System Builder, Dynamic Workspace, MicroFunction, API/eventing, Flyway-only database governance, OPA/SBAC rule catalog, Tool/MCP Gateway, observability, runtime toggle governance, GitNexus, DevSecOps evidence packs, and Auto-Heal/Auto-Learn/Auto-Improve candidate loops.
| Strategic Outcome | v1.1 Required Result | Evidence Required |
| --- | --- | --- |
| Single source of truth | PostgreSQL/Flyway-governed registry schemas own agent identity, lifecycle, policy, tool, model, memory, runtime, certification, incident, and decommission data. | Flyway report, schema version, DBA/data-governance approval, registry record. |
| Evidence reconstruction | Every agent action links agent_id, agent_version_id, agent_run_id, trace_id, request_id, policy_decision_id, tool_action_id, model_route_id, and evidence_ref. | Trace, audit, OPA/SBAC decision, tool result, model route, evidence manifest. |
| Fail-closed governance | Unknown agent, stale certification, expired credential, missing policy, missing evidence, or invalid classification blocks protected action. | Rejected runtime event, denial reason, policy package version, evidence_ref. |
| Reversibility and accountability | Registry fields support suspension, revocation, rollback, quarantine, decommission, retention, and legal hold. | Status history, kill-switch record, decommission certificate, retention rule. |
| Improvable controls | Registry data drives dashboards, recertification, red-team findings, incidents, drift reconciliation, and improvement backlog. | Assurance view, KRI, finding, backlog item, owner, closure evidence. |

# 2. Purpose, Scope, and Authority

## 2.1 Purpose

- Define the canonical registry and evidence data model for AI agent lifecycle, runtime activity, tool actions, policy decisions, memory/RAG context, supply-chain artifacts, certification gates, incidents, recertification, suspension, revocation, and decommissioning.

- Ensure the System Builder, Dynamic Workspace, agents, tools, dashboards, audit views, DevSecOps pipelines, and evidence packs reference one governed source of truth.

- Provide schema-ready guidance convertible into Flyway migrations, OpenAPI contracts, AsyncAPI/CloudEvents contracts, OPA input schemas, audit events, and assurance dashboards.

- Prevent orphaned agents, invisible tool grants, disconnected evidence, stale credentials, shadow registries, unmanaged runtime state, and unverifiable AI-generated claims.

## 2.2 Scope
| In Scope | Out of Scope |
| --- | --- |
| Agent registry schemas, tables, reference data, IDs, lifecycle states, RLS policies, indexes, views, events, evidence links, and retention rules. | Ad hoc spreadsheets, unmanaged lists, local-only files, tool-specific inventories, or AI-generated summaries used as authority. |
| Runtime events for agent runs, model routes, tool actions, policy decisions, guardrail results, memory context, certification, incidents, delegation, and registry drift. | Direct production mutation, direct model-provider calls, direct credentials inside agents, or unregistered tool execution. |
| Flyway-governed database changes, OpenAPI/AsyncAPI contracts, CI/CD validation, audit trails, dashboards, data quality checks, and decommission evidence. | General enterprise data governance outside AIRA unless used by AI agents, registry data, or agent-control evidence. |
| Dynamic Workspace and System Builder registry-backed screens, controls, approvals, runtime toggles, and operational dashboards. | Frontend-only authority, local-only runtime state, or dashboard data treated as source of truth. |

## 2.3 Authority and Precedence
| Level | Authority | Role |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance / Data Governance | Final authority for production-impacting registry, evidence, identity, policy, and data model decisions. |
| L1 | AIRA AVCI, AI Governance, Security, Database/Flyway, Observability, Change Governance | Universal rules for evidence, classification, migration, policy, audit, rollback, and retention. |
| L2 | This 42O Standard | Canonical authority for AI agent runtime registry schema, runtime evidence data model, and evidence correlation. |
| L3 | Flyway migrations, OpenAPI/AsyncAPI contracts, OPA input schemas, dashboard schemas, CI tests | Implementation controls that enforce 42O. |

# 3. Source Alignment and Control Relationships
| Source | Relationship to 42O | Required Registry/Data Link |
| --- | --- | --- |
| 42D | Identity lifecycle | agent_registry, agent_owner, agent_credential_ref, access_review, recertification, decommission certificate. |
| 42E | Runtime security | agent_run, runtime_event, tripwire_event, assurance metrics, containment and kill-switch state. |
| 42F | Autonomy/trust | trust tier, autonomy risk tier, authority ceiling, promotion/demotion history, human-handoff record. |
| 42G | Threat model | threat scenario, abuse case mapping, control link, incident trigger, red-team evidence. |
| 42H | Tool/MCP Gateway | tool_manifest, tool_scope, action_request, dry-run, approval, execution result, rollback_ref. |
| 42I | Memory/RAG | source eligibility, retrieval decision, context assembly, context hash, quarantine state, memory write evidence. |
| 42J | Certification | evaluation dataset, red-team result, certification decision, waiver, expiry, recertification schedule. |
| 42K | Incident response | incident evidence chain, containment action, kill-switch scope, recovery gate, forensic hash. |
| 42L | Multi-agent delegation | delegation_chain_id, parent_run_id, child_run_id, authority ceiling, loop/cost limits. |
| 42M/42N | Supply chain and policy | artifact registry, SBOM/provenance, policy package, OPA decision, SBAC skill reference. |
| 41B/61 | System Builder and Dynamic Workspace | intake_id, generated artifact refs, approval refs, workspace/admin actions, evidence pack. |

# 4. Registry Control Model

The runtime registry is not a passive inventory. It is a control surface that determines whether an agent may be registered, activated, invoked, delegated, routed, granted tool access, certified, recertified, suspended, revoked, or retired. Protected runtime paths must query registry-backed state and fail closed when required records are missing, stale, expired, unapproved, or inconsistent.
| Registry Principle | Required Treatment |
| --- | --- |
| Authority | PostgreSQL registry tables are authoritative; Redis/Valkey, dashboards, reports, LLM Wiki, pgvector, and AI summaries are derivative and rebuildable. |
| Correlation | Every record must link through stable identifiers such as agent_id, agent_version_id, run_id, trace_id, policy_decision_id, tool_action_id, model_route_id, context_assembly_id, and evidence_ref. |
| State enforcement | Agent lifecycle state, certification state, recertification state, trust tier, credential state, and policy binding are checked before runtime action. |
| Evidence by construction | Registry write paths emit audit, trace, evidence, and change history records automatically. |
| Fail-closed | Unknown agent, unknown state, missing owner, expired credential, missing policy, missing evidence, stale certification, or unapproved tool/model/memory route blocks protected action. |

# 5. Canonical Registry Data Domains
| Domain | Purpose | Primary Owner | Example Fields |
| --- | --- | --- | --- |
| Agent Identity | Unique identity, purpose, owner, lifecycle, non-goals, classification ceiling. | AI Gov / Security | agent_id, owner_id, lifecycle_state |
| Credential Hygiene | Logical credential references, TTL, rotation, revocation, decommission proof. | Security / Platform | credential_ref, lease_expiry |
| SBAC and Delegation | Skills, delegation scope, authority ceiling, separation-of-duties, expiry. | Security / AI Gov | skill_code, scope, delegation_chain_id |
| Tool and MCP | Tool manifests, actions, risk tier, dry-run, idempotency, rollback, approval rules. | DevSecOps / Platform | tool_id, action_code, rollback_method |
| Model Route and Guardrails | LiteLLM aliases, classification eligibility, fallback, guardrail and evaluation evidence. | AI Gov | model_alias, route_policy_id |
| Memory and RAG | Context eligibility, source authority, freshness, quarantine, memory writes. | Knowledge / Data Gov | source_id, context_hash |
| Runtime Evidence | Agent runs, policy decisions, tool actions, model use, results, audit and evidence refs. | SRE / Audit | run_id, trace_id, evidence_ref |
| Certification and Incidents | Red-team results, trust tier, recertification, suspension, kill switch, forensic chain. | Security / QA | cert_id, incident_id |

# 6. Authoritative Schema and Identifier Baseline

The logical schema names below are proposed implementation groupings. Physical names may be finalized through the database register, but any deviation must preserve bounded-context ownership, Flyway-only migration, RLS/classification controls, auditability, and evidence correlation.
| Schema | Purpose | Example Tables |
| --- | --- | --- |
| aira_agent | Agent identity, lifecycle, ownership, status, certification, trust tier, registry metadata. | agent_registry, agent_version, agent_owner, status_history |
| aira_agent_sec | Credential references, workload identity, token lease metadata, recertification, revocation, access review. | credential_ref, access_review, recertification |
| aira_agent_policy | SBAC grants, OPA policy references, policy decisions, approvals, delegation ceilings. | sbac_grant, policy_binding, policy_decision |
| aira_agent_tool | Tool/MCP manifest, tool scopes, action requests, dry-runs, approvals, execution results, rollback metadata. | tool_manifest, tool_scope, action_request, action_result |
| aira_agent_model | Model route eligibility, LiteLLM aliases, guardrail bindings, model invocation evidence. | model_route, guardrail_binding, invocation_event |
| aira_agent_memory | Memory/RAG context, retrieval provenance, source eligibility, quarantine, context assembly, memory writes. | context_source, retrieval_decision, context_assembly, memory_write |
| aira_agent_run | Runtime executions, events, trace correlation, state transitions, anomalies, tripwires. | agent_run, runtime_event, tripwire_event |
| aira_agent_evidence | Evidence pack manifest, audit references, certification results, incident forensics, decommission proof. | evidence_manifest, certification_result, incident_chain, decommission_certificate |

## 6.1 Core Identifier Standard
| Identifier | Required Use | Example |
| --- | --- | --- |
| agent_id | Stable identity across versions and runtime runs. | AGT-AIRA-SECURITY-001 |
| agent_version_id | Immutable version of instructions, tool scope, model route, and policies. | AGTV-20260618-0001 |
| agent_run_id | Unique execution instance for traceability. | RUN-20260618-0000001 |
| trace_id | Distributed trace correlation across services, tools, policies, and evidence. | OTel trace ID |
| policy_decision_id | OPA/SBAC decision record. | POLD-20260618-0001 |
| tool_action_id | Tool/MCP action request/result chain. | TACT-20260618-0001 |
| context_assembly_id | Memory/RAG context assembly and retrieval decision. | CTX-20260618-0001 |
| evidence_ref | Stable pointer to evidence manifest or evidence pack. | EVID-AIRA-AGENT-20260618-0001 |

# 7. Agent Registry Entity Model
| Entity | Minimum Fields | Primary Controls |
| --- | --- | --- |
| agent_registry | agent_id, name, type, purpose, non_goals, owner_id, backup_owner_id, lifecycle_state, classification_ceiling, created_at, retired_at | Owner, state, classification, fail-closed unknown state. |
| agent_version | agent_version_id, agent_id, semantic_version, instruction_hash, prompt_refs, model_route_policy_id, tool_scope_hash, guardrail_policy_id, effective_from, effective_to | Immutable version; material change creates new version. |
| agent_owner | owner_id, user_id, role, department, active_status, backup_owner_id, jml_status | Owner tied to JML and recertification. |
| agent_sbac_grant | grant_id, agent_id, skill_code, scope, environment, expires_at, approver_id, status | Skill grants expire and must be recertified. |
| agent_policy_binding | binding_id, agent_id, opa_package, policy_version, decision_scope, environment, status | Policy binding required before protected action. |
| agent_tool_scope | scope_id, agent_id, tool_id, action_code, risk_tier, dry_run_required, approval_required, rollback_method | Default deny and manifest bound. |
| agent_model_route | route_id, agent_id, model_alias, classification_ceiling, guardrail_policy_id, fallback_policy, status | LiteLLM route required; direct provider calls prohibited. |
| agent_credential_ref | credential_ref_id, agent_id, secret_path_ref, workload_identity_ref, ttl, rotation_due, revoked_at, status | Logical references only; no secret values. |

# 8. Evidence, Runtime Event, and Correlation Model

Runtime evidence must support reconstruction. A reviewer must be able to answer who initiated a request, which agent acted, which policy was applied, which tool or model was used, what evidence supported the action, what changed, who approved it, and how it can be reversed or improved.
| Event Type | Required Fields | Evidence Requirement |
| --- | --- | --- |
| agent.registered | agent_id, owner_id, lifecycle_state, classification_ceiling, evidence_ref | Registry approval evidence. |
| agent.run.started | agent_run_id, agent_id, agent_version_id, requester_id, trace_id, request_class | Runtime trace and request evidence. |
| policy.decision.recorded | policy_decision_id, agent_run_id, opa_package, decision, reason, confidence, evidence_ref | OPA/SBAC decision log. |
| tool.action.requested | tool_action_id, agent_run_id, tool_id, action_code, risk_tier, approval_required | Tool intent and authorization evidence. |
| tool.action.executed | tool_action_id, executor, result, changed_resource, rollback_ref, audit_ref | Harness/tool result and audit. |
| model.route.used | agent_run_id, model_alias, route_policy_id, guardrail_result, token_usage, classification | Model routing and guardrail evidence. |
| memory.context.assembled | context_assembly_id, source_ids, classification, context_hash, freshness_result | RAG provenance evidence. |
| agent.incident.contained | incident_id, kill_switch_scope, containment_action, forensic_evidence_ref | Incident chain and containment evidence. |
| decommission.completed | agent_id, revoked_credentials, disabled_routes, denial_tests, approval_ref | Decommission certificate. |

# 9. OpenAPI, AsyncAPI, CloudEvents, and Contract Requirements

The registry must expose controlled service APIs and event contracts. Frontend screens, dashboards, System Builder, agents, CI/CD, and audit tools must use generated clients or governed event consumers. Direct database mutation outside approved service/migration paths is prohibited.
| Contract | Purpose | Controls |
| --- | --- | --- |
| Agent Registry API | Create, read, update status, version, owner, classification, lifecycle metadata. | Maker-checker for activation, suspension, revocation, retirement. |
| Agent Evidence API | Register manifests, attach evidence, close packs, link audit records. | Append-only where applicable; classification-aware and retention-bound. |
| Agent Decision API | Record OPA/SBAC outcomes and policy inputs/outputs. | No decision overwrite; corrections are new records. |
| Agent Tool Action API | Record tool requests, dry-runs, approvals, execution results, rollback metadata. | Integrates with 42H Tool/MCP Gateway. |
| Agent Runtime Events AsyncAPI | Publish lifecycle, run, model, tool, memory, policy, incident, decommission events. | Transactional outbox for cross-boundary publication. |
| CloudEvents Envelope | Standardize event metadata for source, type, subject, id, time, trace, classification. | Schema validation, versioning, DLQ/replay, consumer idempotency. |

# 10. Flyway, Data Governance, Security, RLS, and Retention
| Control | Mandatory Rule | Acceptance Evidence |
| --- | --- | --- |
| Flyway-only | All schemas, tables, indexes, views, functions, seed data, RLS policies, and evidence tables are created through Flyway or approved migration workflow. | Flyway validate/migrate report, checksum, DBA approval. |
| No manual production DDL | Manual production schema mutation is prohibited except approved break-glass with follow-up migration and reconciliation. | CAB/break-glass record, reconciliation migration. |
| Migration evidence header | Every migration includes ticket, owner, bounded context, classification, purpose, verification, rollback/forward-fix, reviewer. | Migration header and PR/MR AVCI summary. |
| Immutable activation records | Activated agent versions, policy decisions, certification results, tool results, incidents, decommission certificates are append-only or versioned. | Append-only table/view checks. |
| Classification metadata | Every registry and evidence table carries classification metadata or policy reference. | Classification/RLS tests. |
| RLS / tenant scope | Tenant, environment, workspace, and restricted records enforce database and service-layer controls. | Negative access tests and audit proof. |
| No raw secrets | Registry stores logical secret references and credential metadata only. | Secret scan and schema review. |
| Retention and disposal | Evidence, incident, decommission, audit records have retention, disposal, and legal-hold flags. | Retention policy row and disposal evidence. |

# 11. Data Quality, Reconciliation, Drift Detection, Metrics, and Assurance Views
| Quality Check / Metric | Reject or Escalate If | Target |
| --- | --- | --- |
| agent_registry_completeness_rate | Any active agent lacks owner, backup owner, lifecycle state, classification ceiling, trust tier, model route, tool scope, or revocation path. | 100%; critical gap blocks activation. |
| unlinked_agent_event_count | Runtime events lack agent_id, run_id, trace_id, or evidence_ref. | 0. |
| orphaned_credential_count | Credential has no active owner, TTL, rotation state, or registry-bound agent. | 0; critical if production-capable. |
| policy_decision_unlinked_count | Tool/model/memory action lacks policy_decision_id. | 0. |
| registry_drift_findings | Runtime tools, CI/CD, repositories, connectors, dashboards, or credentials show agent/tool state not present in registry. | Immediate reconciliation. |
| decommission_denial_test_pass_rate | Retired or revoked agents can still authenticate, route, retrieve, or use tools. | 100% denial tests pass. |
| evidence_reconstruction_success_rate | Sampled actions cannot reconstruct full evidence chain. | 100% before production maturity. |

- Assurance views must support AI Governance, Security, DevSecOps, SRE, Data Governance, Internal Audit, and CAB review without exposing secrets, raw prompts, raw PII, or Restricted content.

- Dashboards are derivative and must display source freshness, schema version, classification, redaction state, evidence_ref, and last reconciliation status.

- Drift findings must open evidence-backed improvement or incident records and, where material, update 00D as an AVCI reconciliation item.

# 12. Dynamic Workspace, System Builder, Tool/MCP, Memory/RAG, and DevSecOps Integration
| Integration Surface | 42O Required Binding | Evidence Required |
| --- | --- | --- |
| Dynamic Workspace | Admin screens and dashboards read registry APIs only; UI cannot activate, certify, suspend, or revoke without backend policy and maker-checker flow. | OpenAPI contract, OPA decision, audit event, evidence_ref. |
| System Builder | Generated agent, prompt, tool, route, policy, and environment artifacts become draft registry records before activation. | intake_id, generated artifact refs, validation evidence. |
| Tool/MCP Gateway | Tool action eligibility is registry-bound and policy-mediated. | tool_action_id, tool_manifest_id, policy_decision_id. |
| Memory/RAG | Context assembly and memory writes require source eligibility, freshness, classification, quarantine, and evidence references. | context_assembly_id, retrieval_decision_id. |
| MicroFunction/API/Event | Agent actions affecting business workflows must use governed MicroFunction/API/event paths with idempotency and outbox. | transaction_code, idempotency_key, CloudEvents ID. |
| CI/CD and GitNexus | Schema, contracts, policies, and generated code pass CI/CD gates; GitNexus is advisory/read-only impact evidence. | CI run, test reports, scan reports, GitNexus ref. |
| Runtime toggles | Diagnostic verbosity, tracing, sampling, route availability, and safe-disable flags are registry- and policy-governed. | toggle change evidence, approval, rollback, audit. |

# 13. Implementation Roadmap, Acceptance Criteria, RACI, and AVCI Summary

## 13.1 Implementation Roadmap
| Phase | Focus | Exit Criteria |
| --- | --- | --- |
| 0 | Register 42O in AIRA source register and 00D reconciliation register. | 42O accepted as active candidate companion to 42D-42N. |
| 1 | Create logical registry model and data dictionary. | Entities, IDs, states, enums, owners, classifications confirmed. |
| 2 | Generate Flyway baseline for DEV registry schemas. | Clean migrate passes and seed data validated. |
| 3 | Create OpenAPI/AsyncAPI/CloudEvents contracts and generated clients. | Contracts validate and client generation passes. |
| 4 | Connect 42D-42N controls to registry fields and policies. | Each control has authoritative table/event/evidence mapping. |
| 5 | Build assurance views and reconciliation queries. | Dashboards and drift checks run against DEV data. |
| 6 | Pilot with existing architecture, developer, security, test, evidence, CI/CD, documentation, and knowledge agents. | All pilot agents registered, certified, monitored, and evidence-linked. |

## 13.2 Acceptance Criteria

- All active agents have registry records with mandatory fields and evidence references.

- No protected agent action can execute without registry-backed lifecycle state, SBAC scope, OPA policy, tool/model route eligibility, and evidence correlation.

- All registry database objects are created through Flyway with migration headers, checksums, validation reports, and DBA/data-governance review.

- All registry service APIs and events are contract-first and validated through CI/CD.

- No registry table stores raw secrets, raw prompts, raw PII, raw documents, or unredacted Restricted data unless explicitly approved and protected by classification/RLS/retention controls.

- Runtime events support reconstruction across agent_id, version, run_id, trace_id, policy decision, tool action, model route, memory context, approval, and evidence pack.

- Registry drift, orphaned credentials, stale certification, missing evidence, and shadow tool grants are detectable and escalated.

- Suspension, revocation, decommission, and denial tests work before production activation.

- Auto-Heal, Auto-Learn, and Auto-Improve may propose registry/schema/policy improvements only as reviewable candidates with tests, evidence, human approval, and rollback path.

- Assurance dashboards show registry completeness, policy linkage, credential hygiene, drift, decommission denial tests, and evidence reconstruction success without leaking forbidden telemetry.

## 13.3 RACI
| Activity | IT/Arch | Data/DBA | Security | AI Gov | DevSecOps/QA/Audit |
| --- | --- | --- | --- | --- | --- |
| Approve 42O standard | A | C | C | R | I |
| Own physical schema and migrations | C | A/R | C | C | C |
| Define agent registry fields | A | R | R | R | C |
| Approve policy/data access rules | C | C | A/R | R | C |
| Run CI/CD and evidence gates | I | C | C | C | A/R |
| Audit registry evidence | I | C | C | C | A/R |

## 13.4 AVCI Compliance Summary
| AVCI Property | How 42O Satisfies It |
| --- | --- |
| Attributable | Agent, owner, version, credential, tool, model route, policy, memory context, action, approval, incident, and decommission records have stable IDs and responsible roles. |
| Verifiable | Flyway migrations, contract tests, policy decisions, runtime traces, evidence packs, CI/CD runs, GitNexus refs, dashboards, and denial tests prove registry behavior. |
| Classifiable | All registry and evidence records carry classification, handling, redaction, retention, route eligibility, and RLS/security enforcement metadata. |
| Improvable | Drift, incidents, red-team results, recertification failures, orphaned credentials, missing evidence, and Auto-* candidates feed controlled backlog, policy updates, tests, and 00D reconciliation. |

# Appendix A - Copy-Ready Registry Review Prompt

Use this prompt only to review registry readiness. Do not approve activation.

Act as an AIRA 42O registry reviewer. Review the proposed AI agent registry schema, migrations, APIs, events, OPA/SBAC inputs, evidence model, dashboards, and runtime data flows. Produce: missing fields, schema boundary risks, Flyway gaps, RLS/classification gaps, evidence reconstruction gaps, tool/model/memory linkage gaps, drift risks, acceptance failures, and required remediation before activation.

# Appendix B - Non-Negotiable Rejection Rules

- Reject any active agent without registry record, owner, backup owner, lifecycle state, classification ceiling, trust tier, certification state, model route, tool scope, and decommission path.

- Reject any protected action without policy_decision_id, trace_id, evidence_ref, and registry-backed tool/model/memory eligibility.

- Reject any registry implementation that stores raw secrets, unredacted Restricted data, raw prompts, raw documents, or unmanaged production PII.

- Reject any manual production DDL, unmanaged seed data, or dashboard-only registry state.

- Reject any direct database mutation by Dynamic Workspace, System Builder, agent, or frontend component outside approved service/migration paths.

- Reject any runtime state that cannot be reconstructed from registry, audit, trace, policy, action, model, context, approval, and evidence records.

- Reject any Auto-Heal, Auto-Learn, or Auto-Improve output that changes production registry state without human approval, CI/CD evidence, rollback path, and audit.

