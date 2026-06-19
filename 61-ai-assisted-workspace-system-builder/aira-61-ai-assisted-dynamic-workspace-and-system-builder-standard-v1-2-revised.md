---
title: "AI Assisted Dynamic Workspace and System Builder Standard"
doc_id: "AIRA-61"
version: "v1.2"
status: "revised"
category: "AI-assisted workspace and system builder"
source_docx: "AIRA_61_AI_Assisted_Dynamic_Workspace_and_System_Builder_Standard_v1.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 61-ai-assisted-workspace-system-builder
  - revised
  - aira-61
---



# AI Assisted Dynamic Workspace and System Builder Standard



AIRA

AI-Native Enterprise Platform

AI-Assisted Dynamic Workspace and System Builder Standard

v1.2 Revised

Guided Requirements | Diagnostic Intake | System Builder | Dynamic Workspace | AI Agent Invocation | Human Approval | Evidence-Producing Promotion
| Property | Value |
| --- | --- |
| Document ID | AIRA-DOC-061 |
| Canonical Filename | AIRA_61_AI_Assisted_Dynamic_Workspace_and_System_Builder_Standard_v1.2_Revised.docx |
| Version | v1.2 - Dynamic Workspace, System Builder, MicroFunction, DevSecOps Evidence, AI Agent, Runtime Toggle, and Continuous Improvement Alignment Update |
| Supersedes | 61-AIRA_AI_Assisted_Dynamic_Workspace_and_System_Builder_Standard_v1.1.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | DRAFT FOR ARCHITECTURE REVIEW BOARD / AI GOVERNANCE / DYNAMIC WORKSPACE / CAB APPROVAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; System Builder Product Owner; Dynamic Workspace Owner; AI Governance; Security Architecture; DevSecOps Lead; Software Development Lead; DBA; QA/SDET; SRE; Internal Audit |
| Primary Sources | 41B/44 System Builder; 42 AI Governance; 46-60 Dynamic Workspace; 10 MicroFunction; 15/15A API; 16/16A/16B Database/Flyway; 17/17A Security; 20/45 CI/CD Evidence; 31/31A Observability; 30/30A Change; 32 SBAC; 34 Audit |
| Review Cadence | Quarterly; unscheduled on material System Builder, Dynamic Workspace, AI agent, model-route, MicroFunction, evidence, policy, security, DevSecOps, or production-promotion change |
| Evidence Path | OpenKM Tier-0 / AIRA / Dynamic-Workspace-System-Builder / AI-Assisted-Builder / v1.2/ |

Discipline First - Automation Second - Intelligence Third - AVCI Always

# Mandatory Practice Statement

The AIRA AI-Assisted Dynamic Workspace and System Builder must not operate as an uncontrolled low-code/no-code platform, autonomous code generator, production mutation agent, or authority bypass. It is a governed requirements-to-artifacts, diagnostics-to-remediation, and evidence-to-improvement capability. AI may analyze, recommend, draft, generate, test, summarize, and request approved agent action, but it must not approve, merge, deploy, activate, override policy, grant access, weaken controls, call models outside approved routes, or directly mutate production. Every output remains draft until AVCI evidence, human review, CI/CD gates, architecture/security checks, and rollback-ready promotion are complete.

# Static Table of Contents

Executive Summary and v1.2 Upgrade Verdict

Purpose, Scope, Authority, and Source Alignment

System Builder Control Boundary and Operating Model

Controlled Intake Categories and Guided Requirement Intelligence

Pre-Generation and Pre-Remediation Assessment Gates

Dynamic Workspace, Experience Pack, and Admin Builder Integration

MicroFunction, API/Event, Database/Flyway, and Runtime Configuration Integration

AI Agent Invocation, Tool Authorization, LiteLLM, Guardrails, and Autonomy Limits

DevSecOps Pipeline, GitNexus, Evidence Pack, Testing, and Runtime Toggles

Auto-Heal, Auto-Learn, Auto-Improve Candidate Loop

Data Model, API Contract Families, RACI, Roadmap, Acceptance Criteria, and AVCI Summary

# 1. Executive Summary and v1.2 Upgrade Verdict

AIRA is a governed AI-native enterprise platform whose Dynamic Workspace, MicroFunction runtime, API/event contracts, database configuration, evidence pipeline, and AI agents must remain controlled as a single engineering ecosystem. This standard defines the System Builder as the governed surface where authorized humans submit requirements, diagnostics, evidence, enhancement requests, templates, prompts, agent requests, and remediation proposals, and where AI assists only within approved boundaries.

Version 1.2 aligns the original v1.1 builder standard with the revised 09, 39A-39C, 19B, 20, 45, 31/31A, 24B, 30/30A, 29, 32, 17/17A, 15/15A, 16/16A/16B, and 48-60 Dynamic Workspace documents. The core decision remains unchanged: the Builder guides, analyzes, recommends, drafts, validates, and packages evidence. It does not become authority.
| v1.2 Alignment Area | Required Upgrade |
| --- | --- |
| Dynamic Workspace integration | Generated workspace, screen, component, widget, experience block, and template outputs must be backend-governed, OPA/SBAC-filtered, MicroFunction-backed, API-contract-bound, observable, accessible, reversible, and evidence-producing. |
| System Builder lifecycle | All new requirements, diagnostics, improvements, agents, and provisioning requests follow intake, classification, impact analysis, assumption validation, draft generation, PR/MR, CI/CD, evidence, approval, activation, monitoring, and improvement. |
| MicroFunction backend | Business capability is generated as configuration-first MicroFunction assembly before custom code; domain logic remains behind ports/adapters and framework concerns remain reusable. |
| DevSecOps evidence | Builder output cannot bypass branch protection, CODEOWNERS, SAST/SCA/DAST, SBOM/provenance, contract tests, policy tests, architecture fitness, GitNexus, and evidence pack gates. |
| AI governance | Agents and model routes are registry-backed, LiteLLM/guardrail-controlled, SBAC/OPA-authorized, Harness-mediated, observable, reversible, and human-accountable. |

# 2. Purpose, Scope, Authority, and Source Alignment
| Area | In Scope |
| --- | --- |
| Requirement intake | Business, system, workflow, UI, API, event, database, policy, integration, Dynamic Workspace, MicroFunction, AI agent, and DevSecOps provisioning requests. |
| Diagnostic intake | Errors, warnings, findings, logs, traces, metrics, screenshots, images, files, test reports, security scans, CI/CD failures, incidents, and user feedback. |
| Generated draft artifacts | Workspace templates, screens, components, APIs, events, MicroFunctions, Flyway migrations, OPA policies, tests, runbooks, prompts, agent manifests, evidence packs, ADR/TDL drafts, and PR/MR summaries. |
| Governance controls | AVCI, EDP-01 through EDP-20, OPA/SBAC/ABAC/RBAC, maker-checker, CI/CD, GitNexus, observability, runtime toggles, rollback, compensation, and CAB/ARB routing. |
| Out of Scope | Mandatory Boundary |
| --- | --- |
| Autonomous production mutation | AI, System Builder, and agents must not directly mutate production, approve their own work, deploy, merge, activate, or bypass approval. |
| Unreviewed low-code authority | Frontend/admin generated configuration is not business authority and cannot bypass backend policy, classification, contracts, MicroFunctions, or evidence. |
| Direct model-provider use | Application code, agents, scripts, and notebooks must not call model providers directly; traffic routes through LiteLLM or approved private gateways. |
| Uncontrolled source of truth | PostgreSQL/Git/OpenKM remain authority as applicable; Redis/Valkey, dashboards, indexes, LLM summaries, and AI narratives are derivative. |

# 3. System Builder Control Boundary and Operating Model

The Builder is a governed control plane above the Dynamic Workspace, Composable Experience Framework, MicroFunction runtime, API/event contracts, database/Flyway layer, policy engine, evidence pipeline, and AI governance layer. It converts raw requests and evidence into reviewable, testable, reversible, evidence-backed work packages.
| Lifecycle Stage | Mandatory Output | Blocking Condition |
| --- | --- | --- |
| Intake | Structured intake record with owner, source, classification, bounded context, risk tier, desired outcome, and evidence reference. | Missing owner, classification, source, or affected domain blocks analysis. |
| Analysis | Impact, reuse, dependency, policy, data, security, test, operational, and rollback analysis. | Conflicts, missing mandatory fields, unsupported technology, or policy ambiguity blocks generation. |
| Recommendation | Options, AIRA defaults, assumptions, risks, tests, artifacts, and approval route. | Unaccepted assumptions or unresolved risk blocks draft generation. |
| Draft generation | Branch/PR/MR-ready draft artifacts only. | Generated artifacts cannot activate runtime behavior directly. |
| Verification | CI/CD, tests, scans, OPA, architecture fitness, GitNexus, evidence pack, and human review. | Critical/high findings block promotion unless formally waived. |
| Activation | Approved template/config/contract release with rollback, cache invalidation, telemetry, and monitoring. | No rollback/deactivation path blocks activation. |

# 4. Controlled Intake Categories and Guided Requirement Intelligence
| Intake Category | Builder Responsibility | Required Evidence |
| --- | --- | --- |
| New requirements | Capture structured business, system, workflow, MicroFunction, UI, API, database, policy, and integration details. | Requirement record, acceptance criteria, affected contracts, owner, classification, and generation-readiness score. |
| Operational and engineering evidence | Classify, hash, scan, redact, correlate, and link errors, logs, traces, metrics, screenshots, files, tests, scans, and incidents. | Evidence ID, source hash, trace ID, retention rule, redaction state, and diagnostic quality rating. |
| Improvement requests | Convert Auto-Heal, Auto-Learn, Auto-Improve, refactor, performance, security, reliability, UX, and technical debt requests into candidate proposals. | Root-cause hypothesis, impact analysis, tests, rollback, and human approval route. |
| AI agent lifecycle | Draft agent purpose, owner, skills, SBAC, OPA, LiteLLM route, guardrails, tools, trust tier, tests, monitoring, suspension, and retirement metadata. | Agent registry draft, threat model linkage, certification gate, tool manifest, and runtime evidence schema. |
| AI DevSecOps provisioning | Create setup/provisioning plans, devcontainer/toolchain manifests, CI/CD templates, policies, secrets paths, and evidence tasks. | Provisioning manifest, security scan, SBOM/provenance, rollback/rebuild plan, and approval evidence. |

Guided defaults must reduce missing information without silently making risk decisions. Defaults may recommend values such as rendering mode, audit profile, idempotency profile, classification, retention, cache behavior, DAST scope, evidence profile, and approval route, but risk-bearing defaults require human confirmation.

# 5. Pre-Generation and Pre-Remediation Assessment Gates
| Gate | Required Sections |
| --- | --- |
| Pre-Generation Assessment | Requirement understanding; business objective; scope and exclusions; assumptions; missing information; recommended AIRA defaults; dependencies; conflict detection; reuse analysis; architecture impact; security classification; test strategy; rollback; generation readiness status. |
| Pre-Remediation Assessment | Issue reproduction; evidence received; evidence quality rating; affected workspace/component/API/MicroFunction/database/policy/agent; root-cause hypothesis; confidence; severity; remediation options; tests; blast radius; rollback/deactivation/compensation; agent invocation plan. |
| Readiness Status | Blocked, Diagnostic-Only, Draft-Only, Proposal-Ready, Review-Ready, Implementation-Ready, or Activation-Ready. Production-bound generation requires Review-Ready or stronger and named human approval. |

Generation is blocked when mandatory requirements are missing, policy/classification is unknown, security assumptions are unresolved, affected contracts are absent, or rollback is undefined.

AI must list assumptions and must not convert an assumption into authority without approval.

Low-confidence, Restricted, production-impacting, destructive, access-changing, financial/legal, or cross-domain requests require escalation.

# 6. Dynamic Workspace, Experience Pack, and Admin Builder Integration
| Artifact Family | Builder May Generate | Required Control |
| --- | --- | --- |
| Workspace and screen templates | Draft template JSON/YAML, layout schema, personalization rules, visibility rules, and activation metadata. | Admin Builder maker-checker, OPA/SBAC filters, classification ceiling, accessibility checks, audit, cache invalidation, rollback. |
| Components and widgets | Catalog entries, property schemas, action bindings, safe states, error states, telemetry hooks, and test fixtures. | Compiled allow-list, OpenAPI-generated clients, no frontend business authority, no direct DB/model/tool calls. |
| Experience Blocks/Packs | Reusable screen, widget, workflow, domain, and AI capability packages. | Compatibility declaration, owner, version, dependency matrix, acceptance evidence, rollback or retirement path. |
| AI Assistant Panel | Prompt templates, response schemas, artifact types, guardrail profile, model-route alias, and human approval actions. | No direct provider calls, no approval authority, citation/evidence requirement, forbidden content controls, artifact registry. |

# 7. MicroFunction, API/Event, Database/Flyway, and Runtime Configuration Integration
| Layer | Generation Boundary | Non-Negotiable Rules |
| --- | --- | --- |
| MicroFunction runtime | Draft transaction definitions, standard step sequence, parameters, idempotency profile, error policy, audit profile, observability profile, and rollback strategy. | Configure first; custom code only for the business gap; no business logic in controllers or frontend; ports/adapters required. |
| API and events | Draft OpenAPI, AsyncAPI, Avro schema, CloudEvents metadata, Kafka topic binding, outbox/inbox profile, DLQ/replay plan, and contract tests. | Contract before code; versioned schemas; idempotent consumers; safe response envelopes; correlation_id, causation_id, trace_id. |
| Database and Flyway | Draft migrations, seed data, RLS policies, indexes, configuration rows, and validation scripts. | Flyway only; PostgreSQL authority; no manual DDL; no production clean; DBA review; no secrets in migrations. |
| Runtime configuration | Draft feature flags, runtime toggles, cache invalidation, environment-scoped parameters, and evidence profiles. | Git-managed config and PostgreSQL truth; Redis/Valkey derivative; toggles audited, policy-controlled, reversible, and monitored. |

# 8. AI Agent Invocation, Tool Authorization, LiteLLM, Guardrails, and Autonomy Limits

The Builder may request approved agent work only through a registry-backed, SBAC/OPA-authorized, Harness-mediated, evidence-producing path. Agents may analyze, draft, test, scan, summarize, and recommend; tool action is bounded by autonomy risk tier, environment, classification, skill, approval, and rollback controls.
| Control | Required Treatment |
| --- | --- |
| Agent registry | Every callable agent has purpose, owner, version, lifecycle state, classification ceiling, allowed skills, prohibited actions, tool manifest, LiteLLM route, guardrail profile, tests, monitoring, and retirement path. |
| Tool authorization | Tool calls require manifest, SBAC grant, OPA decision, risk tier, dry-run where feasible, idempotency key, audit, and rollback/deactivation method. |
| Model route | All model traffic routes through LiteLLM or approved private gateway; input, retrieval, execution, and output guardrails apply. |
| Autonomy | T0-T2 advisory/read/draft actions are allowed by policy; T3 tool requests require approval logic; T4 limited reversible actions require certification; T5 human-controlled actions remain blocked for agents. |
| Prohibited actions | Approve own output, merge PRs, deploy production, grant access, rotate production secrets, change policy without approval, directly modify databases, bypass tests/scans, or suppress evidence. |

# 9. DevSecOps Pipeline, GitNexus, Evidence Pack, Testing, and Runtime Toggles
| Evidence Gate | Required Evidence |
| --- | --- |
| PR/MR evidence | Owner, intake ID, branch, commits, AI tools used, prompt/template version, affected contracts, generated artifacts, reviewer/checker, classification, rollback, and improvement backlog. |
| CI/CD gates | Build, unit, component, integration, contract, OPA policy, Flyway, architecture fitness, SAST, SCA, secrets scan, authenticated DAST, SBOM/provenance, accessibility, visual regression, and E2E tests. |
| GitNexus | Read-only impact analysis, code map, affected tests, dependency graph, architecture drift findings, security-sensitive code map, and evidence summary. It cannot commit, approve, merge, deploy, or mutate production. |
| Observability | Log4j2 structured logs, OpenTelemetry traces/metrics/logs, Sentry errors, Loki logs, Tempo traces, Grafana dashboards, audit events, evidence records, and trace reconstruction. |
| Runtime toggles | Logging, tracing, diagnostic verbosity, feature flags, AI capability exposure, cache refresh, and high-cost telemetry are runtime-changeable only through policy, classification, approval, audit, defaults, rollback, and SLO monitoring. |

# 10. Auto-Heal, Auto-Learn, Auto-Improve Candidate Loop
| Loop | Builder Behavior | Approval Boundary |
| --- | --- | --- |
| Auto-Heal candidate | Detect issue, retrieve evidence, identify affected artifacts, propose remediation, generate tests, draft PR/MR, and attach rollback. | No silent production fix; protected actions require human approval, CI/CD, security review, and evidence. |
| Auto-Learn candidate | Convert resolved incidents, test failures, recurring defects, and review findings into curated knowledge, prompt improvements, runbook updates, or training backlog. | No unreviewed knowledge becomes authoritative; Obsidian/LLM Wiki updates require provenance and reviewer approval. |
| Auto-Improve candidate | Propose refactoring, performance, reliability, security, UX, architecture, contract, policy, or test improvements. | No activation without impact analysis, ADR/TDL where needed, tests, rollback, CAB/ARB when production-impacting. |

# 11. Data Model, API Contract Families, RACI, Roadmap, Acceptance Criteria, and AVCI Summary
| Registry / Table Family | Purpose |
| --- | --- |
| builder_intake_request | Canonical record for requirement, diagnostic, improvement, agent, and provisioning intake. |
| builder_assessment_report | Pre-generation and pre-remediation assessments, assumptions, readiness status, risk, dependencies, and approval route. |
| builder_artifact_package | Generated draft artifacts, source references, artifact hashes, contract references, tests, evidence, and promotion status. |
| builder_agent_invocation | Agent request, OPA decision, Harness action, model route, tool output, trace ID, evidence reference, and human checker. |
| builder_runtime_toggle_request | Toggle change request, policy decision, runtime target, SLO impact, audit, effective window, rollback, and post-change validation. |
| API Contract Family | Example Operations |
| --- | --- |
| Intake APIs | Submit requirement, upload evidence, classify request, retrieve status, attach acceptance criteria. |
| Assessment APIs | Create assessment, update assumptions, score completeness, request clarification, record approval. |
| Artifact APIs | Generate draft package, list artifact versions, submit PR/MR request, bind evidence, request activation. |
| Agent APIs | Request agent task, check policy decision, retrieve output, quarantine output, attach reviewer decision. |
| Audit/Evidence APIs | Record audit event, retrieve evidence pack, correlate trace, export reviewer-ready evidence summary. |
| Role | Responsibilities |
| --- | --- |
| Solutions Architecture / IT Head | Owns standard, approves architecture boundary, resolves conflicts, and escalates CAB/ARB items. |
| System Builder Product Owner | Owns intake workflow, defaulting rules, user experience, backlog, and business acceptance. |
| Security / AI Governance | Owns OPA/SBAC, classification, guardrails, agent authorization, model routes, abuse cases, and high-risk approvals. |
| DevSecOps / Platform | Owns CI/CD, evidence packs, GitNexus, repositories, toolchains, environments, and deployment gates. |
| Development / QA / DBA / SRE | Own implementation quality, tests, contracts, Flyway, operational readiness, observability, and recovery validation. |
| Internal Audit | Reviews evidence completeness, chain-of-custody, control testing, findings, waivers, and improvement closure. |

## Implementation Roadmap
| Phase | Outcome |
| --- | --- |
| P0 Governance baseline | Adopt v1.2, reconcile 41B/44 overlap, define register placement, approve intake and evidence schemas. |
| P1 Builder Lite | Implement structured intake, pre-generation assessment, assumptions approval, evidence upload, PR/MR handoff, and dashboards. |
| P2 Dynamic Workspace generation | Enable governed workspace/screen/component/experience pack draft generation with OPA/SBAC, tests, and rollback. |
| P3 MicroFunction/API/database generation | Enable draft MicroFunction, OpenAPI/AsyncAPI, Flyway, policy, tests, and evidence package generation. |
| P4 Governed agent integration | Enable registry-backed agent invocation through Harness/SBAC/OPA with trust tier, audit, and certification evidence. |
| P5 Measured progressive autonomy | Enable only evidence-backed, reversible, time-bound, limited actions after ARB/CAB approval and runtime assurance. |

## Acceptance Criteria

All builder intake is structured, classified, owned, source-linked, and evidence-backed.

AI produces pre-generation or pre-remediation assessment before draft generation.

Missing mandatory requirements, unresolved conflicts, unknown classification, or missing rollback blocks generation or activation.

Generated outputs enter branch/PR/MR and pass CI/CD, tests, policy, security, architecture, GitNexus, and evidence gates before approval.

Dynamic Workspace, MicroFunction, API/event, database, policy, AI, and runtime-toggle outputs are contract-bound, observable, reversible, and audit-ready.

Auto-Heal, Auto-Learn, and Auto-Improve remain candidate loops under human approval and evidence control.

All artifacts satisfy AVCI and EDP-01 through EDP-20.

## AVCI Compliance Summary
| AVCI Property | Evidence |
| --- | --- |
| Attributable | Named owner, requester, reviewer, source, intake ID, branch, agent/model/tool route, policy decision, and approval record. |
| Verifiable | Assessment reports, tests, scans, OPA decisions, GitNexus outputs, CI/CD evidence, audit events, trace IDs, evidence packs, and dashboards. |
| Classifiable | All requests, uploads, generated artifacts, telemetry, prompts, model routes, evidence, and indexes carry classification and handling rules. |
| Improvable | Diagnostic intake, findings, user feedback, incidents, test gaps, prompt improvements, runbook updates, and controlled Auto-Heal/Auto-Learn/Auto-Improve backlog. |

# Final Control Statement

The AIRA System Builder must not simply ask users what they want and generate code. It must guide users toward complete AIRA-compliant requirements, recommend safe defaults, detect conflicts, validate assumptions, assess risk, identify reusable building blocks, obtain human approval, and only then generate draft artifacts for review, testing, evidence, and controlled activation. AI helps AIRA heal, learn, and improve; it does not silently change AIRA.

