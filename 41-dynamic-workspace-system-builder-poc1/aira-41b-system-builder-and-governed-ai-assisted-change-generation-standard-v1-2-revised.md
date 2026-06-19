---
title: "System Builder and Governed AI Assisted Change Generation Standard"
doc_id: "AIRA-41B"
version: "v1.2"
status: "revised"
category: "Dynamic workspace, system builder, and PoC1"
source_docx: "AIRA_41B_System_Builder_and_Governed_AI_Assisted_Change_Generation_Standard_v1.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 41-dynamic-workspace-system-builder-poc1
  - revised
  - aira-41b
---



# System Builder and Governed AI Assisted Change Generation Standard



AIRA

AI-Native Enterprise Platform

System Builder and Governed AI-Assisted Change Generation Standard

v1.2 Revised

Controlled Intake | Guided Requirements | Evidence-Driven Diagnostics | Dynamic Workspace | MicroFunction | AI Agent Lifecycle | DevSecOps Evidence | Governed Promotion
| Property | Value |
| --- | --- |
| Document ID | AIRA-DOC-041B |
| Canonical Filename | AIRA_41B_System_Builder_and_Governed_AI_Assisted_Change_Generation_Standard_v1.2_Revised.docx |
| Version | v1.2 - Dynamic Workspace, MicroFunction, Contract, Database/Flyway, Security, DevSecOps Evidence, Observability, Runtime Toggle, AI Agent, and Continuous Improvement Alignment Update |
| Supersedes | 41B-AIRA_System_Builder_and_Governed_AI_Assisted_Change_Generation_Standard_v1.1.docx |
| Related Duplicate / Overlap | 44-AIRA_System_Builder_and_Governed_AI_Assisted_Change_Generation_Standard_v1.1 remains an overlap/reconciliation source. Final authority should be confirmed in Register 00D / master document register. |
| Classification | INTERNAL CONFIDENTIAL |
| Status | DRAFT FOR ARCHITECTURE REVIEW BOARD / CAB / AI GOVERNANCE / DEVSECOPS / SECURITY REVIEW |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; System Builder Product Owner; DevSecOps Lead; Software Development Lead; Security Architecture; AI Governance; Platform Engineering; DBA; QA/SDET; SRE; Internal Audit |
| Primary Audience | IT Head; Enterprise Architects; Solutions Architects; Product Owners; Business Analysts; Developers; QA/SDET; DevSecOps; Security; DBA; SRE; AI Engineers; Platform Engineers; Internal Audit |
| Primary Sources | 01/01A AVCI and EDP; 02 Engineering Blueprint; 03 Developer Guide; 07/07B Skills and Maturity; 09 Greenfield; 10/10E MicroFunction; 15/15A API; 16/16A/16B Database/Flyway; 17/17A Security; 19/20/45 GitNexus and CI/CD Evidence; 30/30A Change; 31/31A Observability; 32 SBAC; 34 Audit; 42 AI Governance; 43 Continuous Improvement; 46-61 Dynamic Workspace |
| External Alignment Checked | NIST SSDF SP 800-218; OWASP ASVS 5.0.0; OpenTelemetry Semantic Conventions; SLSA v1.2 |
| Review Cadence | Quarterly; unscheduled on material System Builder, Dynamic Workspace, AI agent, model-route, MicroFunction, API/event, database, security, DevSecOps, evidence, runtime toggle, or production-promotion change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / System-Builder / Governed-Change-Generation / v1.2/ |

Analyze First - Recommend Second - Generate Only After Approval - Validate Through Evidence - Activate Only Through Governed Promotion

# Mandatory Practice Statement

The AIRA System Builder is a governed system factory and change-generation control plane. It may receive controlled intake, analyze requirements and evidence, recommend safe defaults, draft artifacts, request approved agent actions, generate candidate outputs, validate results, and assemble evidence packs. It must not silently mutate runtime behavior, approve its own output, bypass OPA/SBAC/ABAC/RBAC, skip tests or security gates, directly call model providers, create uncontrolled agents, alter production, or promote changes without AVCI evidence, maker-checker review, CI/CD gates, ARB/CAB approval where required, and rollback or compensation readiness.

# Static Table of Contents

1. Executive Summary and v1.2 Upgrade Verdict

2. Purpose, Scope, Authority, and Reconciliation Treatment

3. Non-Negotiable System Builder Boundaries

4. Five Controlled Intake Categories

5. Unified Intake-to-Promotion Lifecycle

6. Guided Requirement Capture and Pre-Generation Assessment

7. Operational Evidence Intake and Pre-Remediation Assessment

8. Generation Scope, Artifact Governance, and Draft State Model

9. Dynamic Workspace, Experience Pack, and Admin Builder Generation Rules

10. MicroFunction, API/Event, Database/Flyway, and Runtime Configuration Rules

11. AI Agent Lifecycle, Tool Authorization, LiteLLM, Guardrails, and Autonomy Controls

12. DevSecOps, GitNexus, Evidence Pack, Testing, and Security Gates

13. Observability, Runtime Toggles, Audit, and Trace Reconstruction

14. Auto-Heal, Auto-Learn, Auto-Improve Candidate Loop

15. Data/Contract Model, RACI, Roadmap, Acceptance Criteria, and AVCI Summary

# 1. Executive Summary and v1.2 Upgrade Verdict

AIRA is an AI-native, mission-critical, enterprise-grade platform. The System Builder is the controlled front door for governed AI-assisted change generation across requirements, diagnostics, Dynamic Workspace, MicroFunctions, APIs, events, database migrations, policies, prompts, agents, tests, runbooks, CI/CD, evidence, and promotion workflows.

Version 1.2 strengthens the v1.1 System Builder baseline after the revision of the greenfield, workstation, Sprint 0, CI/CD, PoC 2, observability, operations, change, security, API, database, and Dynamic Workspace documents. It makes the Builder stricter: it must guide requirements before generating, retrieve and classify evidence before remediation, produce draft outputs only, and prove every candidate change through AVCI, EDP, policy, test, security, observability, rollback, and approval evidence.
| v1.2 Upgrade Area | Mandatory Result |
| --- | --- |
| Guided intake | The Builder does not ask only free-form questions. It captures structured requirements, detects missing fields, proposes defaults, lists assumptions, blocks unresolved conflicts, and routes approvals. |
| Dynamic Workspace integration | Workspace, screen, component, widget, template, experience block, and AI Assistant outputs are backend-governed, OPA/SBAC-filtered, API-bound, MicroFunction-backed, observable, accessible, and reversible. |
| System factory controls | Generated artifacts enter a branch/PR/MR, evidence package, review workflow, and promotion gate. No generated output is automatically authoritative. |
| AI agent lifecycle | Agent definitions, skills, tool scopes, model routes, guardrails, trust tiers, telemetry, suspension, recertification, and retirement are governed artifacts. |
| Continuous improvement | Auto-Heal, Auto-Learn, and Auto-Improve produce candidate proposals and evidence, not silent production changes. |

# 2. Purpose, Scope, Authority, and Reconciliation Treatment
| Purpose Element | Definition |
| --- | --- |
| Purpose | Define how the AIRA System Builder accepts controlled inputs, analyzes intent and evidence, recommends safe options, generates candidate artifacts, invokes approved agents, validates outputs, and prepares promotion evidence. |
| Scope | All System Builder-assisted generation of requirements, workflows, Dynamic Workspace templates, MicroFunctions, APIs, events, database migrations, OPA policies, tests, prompts, agents, provisioning plans, runbooks, and evidence packs. |
| Authority | This document is the working AIRA-DOC-041B System Builder standard. The similar AIRA-DOC-044 document is a duplicate/overlap source and must be reconciled through the canonical register. |
| Conflict rule | When 41B, 44, 61, 43, 42, or companion standards conflict, apply the stricter governance interpretation, record an AVCI reconciliation item, assign an owner, and route through ARB/CAB or Register 00D as applicable. |

This standard does not replace the Engineering Blueprint, MicroFunction Framework, API Contract Standard, Database/Flyway Standards, Security Standards, CI/CD Evidence Guide, Change/CAB Governance, Observability Standards, AI Governance Standards, or Dynamic Workspace specifications.

The System Builder may recommend and generate draft artifacts, but governing standards remain authority for their domains.

Generated artifacts are not approved, active, production-ready, or authoritative until promoted through the required gates.

# 3. Non-Negotiable System Builder Boundaries
| Boundary | Mandatory Meaning |
| --- | --- |
| No silent mutation | The Builder must not directly alter production systems, runtime configuration, policies, model routes, prompts, agents, databases, source repositories, workflows, or canonical knowledge without approved change path. |
| No self-approval | AI, agents, and Builder-generated reviewers cannot approve their own work, merge PRs, grant waivers, close audit findings, or authorize production action. |
| No governance bypass | OPA/SBAC/ABAC/RBAC, classification, secrets, guardrails, Harness, CI/CD, CODEOWNERS, ARB/CAB, DBA, Security, and Internal Audit controls remain enforceable gates. |
| No direct model/provider/tool path | All model routing uses LiteLLM or approved private gateways. Tool actions are routed through approved Harness/MCP/tool gateway controls. |
| Fail closed | Unknown actor, missing classification, missing owner, missing policy, unavailable audit/evidence, unregistered agent/tool, expired certification, or missing rollback blocks protected actions. |
| Evidence by construction | Every intake, analysis, recommendation, generated artifact, agent invocation, policy decision, approval, test, scan, deployment, incident, and improvement links to evidence. |

# 4. Five Controlled Intake Categories
| Category | Examples | Required Routing |
| --- | --- | --- |
| 1. New Requirements | Business, system, workflow, MicroFunction, configuration, UI, API, database, policy, and integration changes. | Structured requirement intake, bounded-context owner, acceptance criteria, architecture/security/data impact, contract-first outputs, test plan, rollback, approval route. |
| 2. Operational and Engineering Evidence | Errors, logs, traces, metrics, screenshots, files, test results, security scans, CI/CD evidence, incidents, feedback. | Evidence intake, classification, redaction, hash, correlation IDs, trace reconstruction, root-cause hypothesis, remediation candidate, evidence quality rating. |
| 3. Improvement Requests | Auto-Heal, Auto-Learn, Auto-Improve, AutoResearch, refactoring, performance, security, reliability, UX, technical debt. | Proposal-driven workflow, impact analysis, candidate branch/artifacts, tests, rollback/compensation, human approval. |
| 4. AI Agent Lifecycle | Purpose, owner, skills, SBAC, OPA, LiteLLM route, guardrails, tools, trust tier, tests, monitoring, suspension, retirement. | Agent charter, registry draft, threat model, tool manifest, certification, telemetry, kill switch, recertification, decommission proof. |
| 5. AI DevSecOps Provisioning | Infrastructure, software, libraries, devcontainers, pipelines, policies, secrets paths, model routes, environment setup. | Golden Source manifest, IaC/devcontainer, SBOM/provenance, policy checks, drift detection, setup evidence, rollback/rebuild plan. |

# 5. Unified Intake-to-Promotion Lifecycle
| Stage | System Builder Output | Gate / Evidence |
| --- | --- | --- |
| G0 Intake | Intake record, source, owner, classification, desired outcome, affected domains, evidence references. | Rejected or routed if source, owner, classification, domain, or risk cannot be established. |
| G1 Analysis | Impact analysis, conflict check, reuse recommendation, policy/data/security/architecture evaluation, missing information list. | Generation blocked when mandatory information, evidence, policy, or rollback is missing. |
| G2 Recommendation | Options, assumptions, AIRA default values, risk tier, approval route, test strategy, rollback strategy. | Named human accepts assumptions or returns for clarification. |
| G3 Draft Generation | Candidate artifacts in branch/sandbox: contracts, configs, code, migrations, tests, prompts, runbooks, policies, agents, evidence. | Draft-only state. No runtime activation. |
| G4 Validation | CI/CD, contract tests, OPA tests, Flyway validation, SAST/SCA/DAST/secrets, SBOM/provenance, accessibility, resilience, GitNexus. | Critical/high findings block promotion unless formal waiver exists. |
| G5 Review and Approval | Maker-checker, CODEOWNERS, Security, DBA, ARB/CAB, Product Owner, QA/UAT, Internal Audit where required. | Approval evidence and conditions recorded. |
| G6 Promotion and Activation | GitOps/CI/CD promotion, feature flag/toggle activation, cache invalidation, monitoring, support readiness. | Deployment evidence, rollback, observability, and smoke tests. |
| G7 Runtime Learning | Operational telemetry, incidents, user feedback, SLOs, audit findings, improvement candidates. | Feeds backlog or Auto-Heal/Auto-Learn/Auto-Improve proposal. |

# 6. Guided Requirement Capture and Pre-Generation Assessment

The System Builder must guide users to provide complete AIRA-compliant requirements before generation. It may use question trees, defaults, sample patterns, and requirement templates, but it must not hide assumptions or infer sensitive business, risk, or security decisions without approval.
| Requirement Dimension | Minimum Required Capture |
| --- | --- |
| Business intent | Problem statement, expected outcome, process owner, impacted role, acceptance criteria, UAT owner, success metric. |
| Architecture impact | Bounded context, domain owner, reuse candidate, MicroFunction fit, API/event impact, database impact, policy impact, workflow impact. |
| Dynamic Workspace impact | Workspace/screen/template/component/widget/experience pack, personalization, accessibility, layout, runtime toggle, cache, telemetry, and rollback needs. |
| Security and classification | Data classification, identity context, RBAC/ABAC/SBAC, OPA policy, secrets handling, consent/PII, DAST scope, abuse cases. |
| Evidence and promotion | Tests, scans, GitNexus, evidence pack, audit, approval path, release route, rollback/deactivation/compensation, hypercare. |
| Pre-Generation Status | Meaning |
| --- | --- |
| Blocked | Mandatory information, policy, classification, ownership, source, conflict resolution, or rollback is missing. |
| Clarification Required | The Builder must ask targeted questions before draft generation. |
| Draft-Only | Sufficient for non-production draft artifacts, not enough for activation. |
| Review-Ready | Complete enough for PR/MR and formal review path. |
| Implementation-Ready | Contracts, tests, evidence, rollback, and required approvals are ready for controlled implementation. |

# 7. Operational Evidence Intake and Pre-Remediation Assessment

Evidence intake is not a chat upload bucket. Evidence must be scanned, classified, redacted, correlated, stored, and linked to a diagnostic record before AI-assisted remediation is allowed.
| Evidence Type | Required Handling |
| --- | --- |
| Logs/traces/metrics | Use correlation IDs, trace_id, span_id, service, environment, release, user hash, classification, and safe redaction. Never ingest raw secrets, tokens, unrestricted PII, raw documents, or high-cardinality metric labels. |
| Screenshots/images/files | Malware scan, hash, source owner, classification, retention, storage reference, redaction state, and evidence_ref are required. |
| Test/scans/CI evidence | Tool name/version, rule set, run ID, commit, branch, artifact digest, severity, waiver status, remediation link, and pass/fail status. |
| Incidents/user feedback | Severity, affected service/workspace/API/MicroFunction, impact, SLA/SLO, workaround, RCA hypothesis, runbook link, and improvement backlog. |
| Pre-Remediation Assessment Field | Required Content |
| --- | --- |
| Issue statement | What failed, where, when, who/what was affected, and how it was detected. |
| Evidence quality | Complete, partial, conflicting, sensitive, stale, insufficient, or quarantined. |
| Root-cause hypothesis | Candidate cause, confidence, affected artifacts, dependency graph, and known unknowns. |
| Remediation options | No change, config/toggle, rollback, forward fix, compensation, code fix, policy fix, schema fix, operational runbook, training, or monitoring. |
| Gate decision | Blocked, Diagnostic-Only, Candidate Fix, PR-Ready, Emergency Change, CAB/ARB Required. |

# 8. Generation Scope, Artifact Governance, and Draft State Model
| Artifact Type | Allowed Builder Output | Promotion Gate |
| --- | --- | --- |
| Requirements and stories | Draft story, acceptance criteria, process impact, UAT script, risk and evidence checklist. | Product Owner and architecture/security review where applicable. |
| Contracts and schemas | OpenAPI, AsyncAPI, Avro, CloudEvents, Problem Details, idempotency profile, schema evolution plan. | Contract linting, compatibility tests, consumer review, CI/CD gate. |
| MicroFunctions and workflows | Transaction definition, step sequence, parameter profile, Temporal/Flowable/DMN draft, approval workflow. | MicroFunction review, policy tests, workflow tests, observability and rollback. |
| Database/Flyway | Migration draft, seed data, RLS, indexes, views, configuration rows, rollback/forward-fix note. | Flyway validation, DBA review, no manual DDL, restore validation. |
| Frontend/Dynamic Workspace | Template, screen, component, widget, generated client, UX/accessibility test, admin-builder package. | OPA/SBAC policy, component allow-list, accessibility, visual regression, evidence. |
| Security/policy | OPA/Rego draft, SBAC catalog update, abuse case mapping, DAST scope, secret handling controls. | Security review, OPA tests, threat model, audit evidence. |
| AI/agent/prompts | Prompt template, guardrail binding, model-route alias, agent charter, tool manifest, evaluation plan. | AI Governance, 42D-42N controls, certification, telemetry, kill switch. |

# 9. Dynamic Workspace, Experience Pack, and Admin Builder Generation Rules
| Rule | Required Treatment |
| --- | --- |
| Backend-governed UI | Frontend-generated layout, widgets, and components may render approved state but cannot authorize, decide, approve, unlock, classify, or execute business authority. |
| Template lifecycle | Draft, reviewed, approved, active, suspended, deprecated, retired, and rolled-back states must be recorded with maker-checker evidence. |
| Experience packs | Blocks and packs must declare owner, purpose, version, bounded context, API/MicroFunction/data/policy dependencies, classification ceiling, compatibility, tests, and rollback. |
| Runtime toggles | Workspace features, AI panels, diagnostic modes, telemetry levels, and template activation toggles are policy-controlled, auditable, reversible, environment-scoped, and monitored. |
| Accessibility and UX | WCAG-aligned checks, responsive behavior, keyboard navigation, safe error states, loading/degraded states, and visual regression evidence are mandatory. |

# 10. MicroFunction, API/Event, Database/Flyway, and Runtime Configuration Rules
| Layer | Builder Rule |
| --- | --- |
| MicroFunction | Configure first, reuse standard steps, generate custom code only for the business gap, preserve Clean Architecture and ports/adapters, and emit trace/audit/evidence for every step. |
| API/Event | Generate OpenAPI/AsyncAPI before implementation; include idempotency keys, safe response envelopes, versioning, schema evolution, CloudEvents metadata, correlation_id, causation_id, trace_id. |
| Kafka/Avro/outbox/inbox | Use transactional outbox/inbox, idempotent consumers, schema registry rules, retry topics, DLQ, replay evidence, and compensation path. |
| Database/Flyway | PostgreSQL is authority; Flyway-only migration; no manual DDL; no production clean; RLS and seed data through migrations; Redis/Valkey derivative only. |
| Runtime config | Feature flags, telemetry toggles, cache profiles, policy references, evidence profiles, and environment parameters are Git-managed, PostgreSQL-backed, audited, and rollback-ready. |

# 11. AI Agent Lifecycle, Tool Authorization, LiteLLM, Guardrails, and Autonomy Controls

The System Builder may request approved agent work only through a registry-backed, SBAC/OPA-authorized, Harness-mediated, LiteLLM-routed, guardrail-controlled, evidence-producing path. Agents are digital team members with bounded responsibilities; they are not unmanaged scripts or production administrators.
| Control Surface | Mandatory Requirement |
| --- | --- |
| Agent charter | Purpose, owner, non-goals, classification ceiling, skill set, model route, guardrails, memory/RAG eligibility, tool scopes, environment scope, tests, trust tier, lifecycle state, retirement plan. |
| Autonomy risk tier | Classify each action as T0 advisory, T1 read-only, T2 draft, T3 tool action request, T4 limited reversible action, or T5 human-controlled/prohibited. |
| Tool/MCP gateway | Tool calls require approved manifest, action schema, SBAC grant, OPA decision, risk tier, dry-run where feasible, idempotency, timeout, audit, rollback/compensation, and human approval rules. |
| Model route and guardrails | All prompts and model calls route through LiteLLM or approved private gateway, with input, retrieval, execution, and output guardrails. Direct model-provider SDK calls are prohibited. |
| Kill switch and incident response | Runtime tripwires, anomaly detection, suspension, revocation, quarantine, forensics, and recertification evidence are required for agent activation. |

# 12. DevSecOps, GitNexus, Evidence Pack, Testing, and Security Gates
| Gate Family | Required Evidence |
| --- | --- |
| Repository and PR/MR | Issue/intake ID, branch, commit, CODEOWNERS, AI-use declaration, generated artifact list, prompt/template version, reviewer/checker, design-principle impact, rollback. |
| Quality gates | Unit, component, integration, contract, mutation where required, E2E, Playwright, accessibility, visual regression, load/concurrency, resilience, OPA, Flyway, and architecture fitness tests. |
| Security gates | SAST, SCA, secrets scan, container scan, authenticated DAST, API security tests, OPA negative tests, SBAC denial evidence, threat/abuse case coverage. |
| Supply chain | Pinned toolchain, build image digest, SBOM, provenance/attestation, artifact signing where applicable, dependency review, license evidence. |
| GitNexus | Read-only code graph, code map, affected tests, dependency impact, security-sensitive code map, architecture drift, evidence summary. GitNexus cannot commit, approve, merge, deploy, or mutate production. |

# 13. Observability, Runtime Toggles, Audit, and Trace Reconstruction
| Observability / Runtime Area | System Builder Requirement |
| --- | --- |
| Telemetry stack | Generated and runtime flows must emit Log4j2 structured logs, OpenTelemetry traces/metrics/logs, Sentry errors, Loki logs, Tempo traces, Grafana dashboards, audit events, and evidence references. |
| Correlation fields | intake_id, artifact_id, agent_id, run_id, trace_id, span_id, request_id, correlation_id, causation_id, policy_decision_id, evidence_ref, classification, environment, release_id. |
| Runtime toggles | Logging level, trace sampling, diagnostic verbosity, AI capability visibility, feature flags, cache refresh, DAST scope, and expensive instrumentation must be policy-controlled, audited, reversible, and SLO-aware. |
| Forbidden telemetry | Passwords, tokens, raw JWTs, secrets, raw PII, account numbers, raw documents, raw Restricted prompts, embeddings, payment card data, private keys, and unrestricted customer payloads are prohibited. |
| Trace reconstruction | Every critical path must reconstruct who requested, what was generated, under which policy, by which model/agent/tool, with which evidence, approval, runtime effect, and rollback path. |

# 14. Auto-Heal, Auto-Learn, Auto-Improve Candidate Loop
| Loop | Allowed System Builder Behavior | Prohibited Behavior |
| --- | --- | --- |
| Auto-Heal | Detect issue, retrieve evidence, classify severity, identify affected contracts/artifacts, generate candidate fix, create tests, propose rollback, open PR/MR, assemble evidence. | Silent production fix, direct database change, policy weakening, CI bypass, self-approval, or closing incident without evidence. |
| Auto-Learn | Convert resolved incidents, failed tests, audit findings, user feedback, and RCA lessons into curated knowledge, prompt/rule updates, training items, or runbook drafts. | Publishing unreviewed AI narratives as authoritative knowledge or indexing Restricted content without controls. |
| Auto-Improve | Propose refactoring, performance, resilience, security, UX, accessibility, observability, contract, policy, test, and architecture improvements. | Activating improvement without impact analysis, tests, owner, reviewer, rollback, and CAB/ARB route where required. |

# 15. Data/Contract Model, RACI, Roadmap, Acceptance Criteria, and AVCI Summary
| Registry / Contract Family | Purpose |
| --- | --- |
| SystemBuilderIntakeRequest | Canonical intake for requirements, evidence, improvements, agents, and provisioning requests. |
| SystemBuilderAssessmentReport | Pre-generation/pre-remediation assessment, assumptions, risk, dependency, readiness status, and approval route. |
| GeneratedArtifactPackage | Draft artifact manifest, source references, generated files, contract refs, tests, hashes, evidence refs, promotion state. |
| AgentActionRequest | Agent invocation, tool action request, OPA/SBAC decision, LiteLLM route, guardrail result, human approval, trace/evidence. |
| RuntimeToggleChangeRequest | Toggle target, scope, SLO impact, approval, effective window, audit, rollback, monitoring, post-change validation. |
| PromotionEvidencePack | CI/CD, scans, tests, GitNexus, SBOM, provenance, UAT, change/CAB, deployment, runtime verification, improvement backlog. |
| Role | Primary Responsibilities |
| --- | --- |
| Solutions Architecture Office / IT Head | Owns the standard, resolves architecture conflicts, governs boundaries, and routes ARB/CAB decisions. |
| System Builder Product Owner | Owns intake UX, defaulting logic, builder backlog, requirement quality, and adoption metrics. |
| Enterprise Architecture | Reviews bounded contexts, SOLID/Clean Architecture, MicroFunction fit, API/data boundaries, and ADR/TDL triggers. |
| Security / AI Governance | Owns classification, OPA/SBAC, guardrails, agent routes, threat model, secrets hygiene, and high-risk approvals. |
| DevSecOps / Platform | Owns repositories, CI/CD, GitNexus, evidence packs, toolchains, environments, SBOM/provenance, and deployment gates. |
| Development / QA / DBA / SRE | Own generated artifact review, implementation correctness, tests, Flyway, operations readiness, telemetry, and recovery validation. |
| Internal Audit | Tests evidence completeness, chain-of-custody, control operation, waiver handling, segregation of duties, and improvement closure. |
| Roadmap Phase | Exit Outcome |
| --- | --- |
| P0 Reconciliation and governance baseline | 41B/44 overlap recorded in Register 00D; v1.2 adopted as working builder standard; intake and evidence schemas approved. |
| P1 System Builder Lite | Structured intake, pre-generation/pre-remediation assessment, assumptions approval, evidence upload, PR/MR handoff, and dashboards. |
| P2 Dynamic Workspace generation | Draft workspace/template/component/widget/experience-pack generation with OPA/SBAC, tests, accessibility, evidence, and rollback. |
| P3 MicroFunction/API/database generation | Draft MicroFunction, OpenAPI/AsyncAPI, Flyway, OPA, tests, and evidence-package generation through CI/CD gates. |
| P4 Governed agent integration | Registry-backed agent invocation with Harness/SBAC/OPA, LiteLLM, guardrails, certification, telemetry, and kill-switch controls. |
| P5 Measured progressive autonomy | Only bounded, reversible, certified, time-limited, evidence-backed actions proceed under explicit approval. |

## Minimum Acceptance Criteria

Every Builder request has source, owner, classification, bounded context, risk tier, desired outcome, and evidence reference.

The Builder performs assessment before generation and blocks unresolved assumptions, conflicts, missing policy, unknown classification, or absent rollback.

Generated outputs remain draft until PR/MR, CI/CD, tests, security scans, OPA/SBAC, GitNexus, evidence pack, and human approval gates pass.

Dynamic Workspace, MicroFunction, API/event, database/Flyway, policy, AI, runtime-toggle, and agent outputs follow their governing standards.

Auto-Heal, Auto-Learn, and Auto-Improve remain candidate loops with evidence, tests, human review, and controlled promotion.

No direct model-provider calls, direct production credentials, direct production mutation, self-approval, policy bypass, or evidence suppression is allowed.

## AVCI Compliance Summary
| AVCI Property | Evidence |
| --- | --- |
| Attributable | Owner, requester, reviewer, actor/agent, source, intake ID, artifact ID, branch, model route, tool action, policy decision, approval, and evidence reference. |
| Verifiable | Assessment records, tests, scans, OPA decisions, GitNexus reports, CI/CD logs, SBOM/provenance, audit events, traces, dashboards, and approval records. |
| Classifiable | All requests, evidence, generated artifacts, prompts, model routes, telemetry, indexes, caches, and records carry classification and handling rules. |
| Improvable | Findings, diagnostics, incidents, failed gates, user feedback, prompt updates, runbook improvements, and Auto-Heal/Auto-Learn/Auto-Improve backlog are captured and reviewed. |

# Final Control Statement

The AIRA System Builder must help the team build faster only by becoming more governed, more traceable, more testable, more secure, more observable, and more reversible. It is a disciplined enterprise system factory, not an autonomous mutation engine. Discipline first. Automation second. Intelligence third. AVCI always.

