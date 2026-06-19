---
title: "AI DevSecOps Skills Framework"
doc_id: "AIRA-07"
version: "v3.2"
status: "revised"
category: "AI DevSecOps skills"
source_docx: "AIRA_07_AI_DevSecOps_Skills_Framework_v3.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 07-ai-devsecops-skills
  - revised
  - aira-07
---



# AI DevSecOps Skills Framework



AIRA
AI-Native Enterprise Platform

AI-Native DevSecOps Skills Framework

Layered Skills Model | SBAC | Trust Governance | Harness-Enforced Execution | Progressive Autonomy | AVCI Evidence
| Property | Value |
| --- | --- |
| Document ID | AIRA-DOC-007 |
| Document Title | AIRA AI-Native DevSecOps Skills Framework |
| Version | v3.2 - Dynamic Workspace, System Builder, MicroFunction, Evidence, and Progressive Autonomy Alignment |
| Supersedes | 07-AIRA_AI_DevSecOps_Skills_Framework_v3.1_Aligned.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | FOR ARCHITECTURE REVIEW BOARD / CAB APPROVAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; Platform Engineering; AI Engineering; SRE / Operations; Knowledge Governance; Internal Audit |
| Primary Audience | Architects, developers, DevSecOps, QA/SDET, Security, DBA, SRE, AI Engineering, System Builder owners, agent owners, internal audit |
| Effective Date | Upon ARB / CAB approval |
| Review Cadence | Quarterly; unscheduled on material skill, tool, AI agent, System Builder, Dynamic Workspace, security, technology, pipeline, or evidence change |
| Governing References | 01A v1.2; 01 v3.2; 01B v1.2; 02 v5.2; 03 v4.2; 04 v9.2; 05 v4.2; 06 v3.2; 10 MicroFunction; 11 DevSecOps; 15 API; 16 Flyway; 17 Security; 31A Observability; 42 AI Governance; 53-61 Dynamic Workspace |
| External Alignment | NIST AI RMF / NIST AI 600-1; NIST SSDF; OWASP ASVS and LLM / GenAI security guidance; OpenTelemetry Semantic Conventions; SLSA v1.2 |

# Mandatory Practice Statement

A human, AI assistant, System Builder agent, or automation service may perform only the actions for which it has an active skill grant, sufficient proficiency, valid trust score, approved classification scope, OPA/SBAC decision, Harness-mediated execution path, required human approval, and AVCI-complete evidence. A skill grant is not authority to bypass architecture, security, policy, evidence, CI/CD, or CAB/ARB controls. Any action that weakens SOLID, Clean Architecture, DDD, ports/adapters, testability, security, observability, reversibility, or AVCI must be blocked or escalated.

# 1. Executive Summary

This v3.2 revision updates the AIRA AI-Native DevSecOps Skills Framework after the foundation updates to 01A, 01, 01B, 02, 03, 04, 05, and 06. It defines how AIRA scales human and AI-assisted engineering while preserving separation of duties, skill-based access control, trust scoring, progressive autonomy, security gates, evidence production, and human accountability.

The v3.1 baseline already established human and AI-agent skills, proficiency evidence, SBAC constraints, delegation limits, Java 25 baseline, LiteLLM/guardrail routing, GitNexus read-only use, and Harness/SBAC/OPA-controlled tool actions. Version 3.2 strengthens those controls for Dynamic Workspace, MicroFunction runtime assembly, System Builder, AI agents, DevSecOps evidence packs, observability, API/event governance, and Auto-Heal / Auto-Learn / Auto-Improve candidate loops.
| v3.2 Strategic Outcome | Mandatory Result |
| --- | --- |
| Governed capability multiplication | Humans and agents may accelerate delivery only inside approved skills, trust tiers, policy, evidence, and approval boundaries. |
| Dynamic Workspace and System Builder readiness | Skills cover UX, accessibility, template governance, AI Panel, Admin Builder, MicroFunction-backed actions, and frontend/backend authority separation. |
| MicroFunction and contract-first execution | Skills enforce configuration-first assembly, OpenAPI/AsyncAPI, Kafka, Avro/JSON Schema, CloudEvents, outbox, DLQ, replay, and Flyway governance. |
| Progressive autonomy with hard stops | Agent authority increases only after certification and evidence; high-risk actions remain human-controlled. |
| Evidence-producing operations | Every material skill use produces trace, audit, policy, test, scan, GitNexus, rollback, and improvement evidence. |

# 2. Authority, Scope, and Precedence
| Area | In Scope | Out of Scope |
| --- | --- | --- |
| Human skills | Architecture, development, QA, DevSecOps, security, DBA, SRE, knowledge, AI engineering, Dynamic Workspace, System Builder, and operations skills. | General HR performance, compensation, and employment policy. |
| AI skills | AI assistant, coding agent, testing agent, documentation agent, security triage agent, SRE agent, knowledge agent, System Builder agent, and tool-action agent skills. | Shadow agents, unmanaged personal AI accounts, direct credentials, direct production mutation, or unregistered tools. |
| Control model | SBAC, OPA, trust score, skill grant, proficiency, classification scope, Harness action, guardrails, audit, evidence, decay, suspension, recertification. | Uncontrolled autonomy, AI self-approval, bypassed CI/CD gates, manual production mutation, or model-provider direct calls. |

# 3. Skills Control Model

AIRA skills are versioned control artifacts. Each skill must state the actor type, owner, allowed actions, tools, classification ceiling, environment scope, proficiency level, trust threshold, evidence requirements, expiry, and recertification trigger. Skills are not broad role labels; they are action-specific permissions connected to policy and evidence.

Figure 1. AIRA Skills Control Model

# 4. Enterprise Design Principles as Skill Gates

EDP-01 through EDP-20 are mandatory skill eligibility gates. A person or agent cannot safely perform work if it lacks the skill to preserve the affected principle.
| EDP Gate | Skill Meaning |
| --- | --- |
| EDP-01 to EDP-04 | SOLID, Clean Architecture, DDD, and ports/adapters skills are required for code, MicroFunction, workflow, API, integration, AI agent, and service-boundary changes. |
| EDP-05 to EDP-08 | DRY/KISS/YAGNI, idempotency, determinism, and fail-safe skills are required for generated code, retries, replays, cache invalidation, and provisioning tasks. |
| EDP-09 to EDP-13 | Human-in-the-loop, least privilege, separation of duties, observability, and policy-as-code skills are required for protected actions. |
| EDP-14 to EDP-17 | Testability, secure-by-design, resilience, and fitness-function skills are required before implementation promotion. |
| EDP-18 to EDP-20 | Progressive autonomy, reversibility, and AVCI skills are required for AI-assisted actions, Auto-Heal, Auto-Learn, Auto-Improve, and production-bound changes. |

# 5. Skill Families and Evidence
| Skill Family | Representative Skills | Required Evidence |
| --- | --- | --- |
| S1 Architecture and Design | SOLID, Clean Architecture, DDD, ports/adapters, ADR/TDL, bounded context, fitness functions | Architecture impact, ADR/TDL or waiver, GitNexus impact, fitness-function results, reviewer sign-off |
| S2 Security and Access | OPA/Rego, SBAC, secrets hygiene, IAM, Keycloak, Vault, threat modelling, classification | OPA tests, secrets scan, DAST/authenticated DAST, abuse cases, access review, remediation evidence |
| S3 Development | Java 25/Spring, TypeScript/React, MicroFunction, adapters, APIs, idempotency, resilience | Unit/component tests, code review, boundary tests, outbox/idempotency tests, PR/MR AVCI summary |
| S4 Test and Quality | Unit, contract, mutation, Playwright, visual regression, accessibility, AI eval, Resilience Lab | Test reports, coverage, mutation score, contract tests, Playwright report, WCAG evidence, resilience results |
| S5 DevSecOps and Platform | CI/CD, GitOps, containers, Kubernetes, Helm, SBOM, SLSA, GitNexus, evidence packs | Pipeline run, SBOM/provenance, SAST/SCA/secret/IaC/image scans, rollback plan, promotion record |
| S6 Data and Retrieval | PostgreSQL, Flyway, RLS, pgvector, LightRAG, metadata, lineage, cache governance | Flyway checksum, migration test, RLS test, source lineage, cache invalidation, retrieval evidence |
| S7 Workflow and Process | Temporal, Flowable, BPMN, DMN, approval, compensation, SLA timers | Workflow tests, approval evidence, compensation path, timeout/retry evidence, human task audit |
| S8 AI Governance | LiteLLM, guardrails, prompt lifecycle, model aliases, eval datasets, red-team, agent certification | Model route audit, guardrail result, prompt version, eval report, red-team result, human approval |
| S9 Observability and SRE | Log4j2, OpenTelemetry, Sentry, Loki, Tempo, Grafana, SLO, incident evidence | Trace/log/metric/audit correlation, dashboard export, alert test, redaction test, incident/RCA link |
| S10 Knowledge Governance | Obsidian, LLM Wiki, source tiers, citation, freshness, conflict quarantine, Auto-Learn | Source hash, citation, freshness, classification, review record, index manifest, quarantine decision |
| S11 Dynamic Workspace and UX | Next.js, widgets, templates, AI Panel, accessibility, responsive UX, safe states | UX review, WCAG evidence, policy-filter test, widget state tests, visual regression, template approval |
| S12 Governance and Audit | AVCI, RACI, maker-checker, CAB/ARB, evidence retention, internal audit | Evidence completeness, approval trail, SoD check, retention rule, audit-ready control test |

# 6. Proficiency Levels, Trust, and Risk Tiers
| Level | Human Meaning | AI / Agent Meaning | Default Authority |
| --- | --- | --- | --- |
| L0 Awareness | Understands terminology and constraints. | Can summarize with citations. | No independent action. |
| L1 Assisted | Performs work with close guidance. | Can draft bounded candidate output. | Draft only; mandatory review. |
| L2 Practitioner | Performs repeatable low-risk tasks with evidence. | Can run approved non-mutating analysis. | Read/analyze/draft within scope. |
| L3 Advanced | Performs complex work and reviews others in non-production. | Can propose tool actions through Harness. | Action request only; policy and human gate apply. |
| L4 Lead / Certified | Designs patterns, approves lower-risk work, owns evidence quality. | Can execute limited reversible non-production actions if certified. | Bounded execution only where policy allows. |
| L5 Authority | Sets standards, resolves conflicts, approves exceptions. | Not applicable as full autonomous authority. | Human-only authority for exceptions, production, and high-risk decisions. |

Trust is calculated from successful evidence-backed work, test quality, policy adherence, incident history, rework rate, security findings, review outcomes, and recertification status. Trust decays after inactivity, failed evidence, policy violations, unsafe recommendations, stale knowledge use, or incidents. Trust never overrides classification, OPA/SBAC, CAB/ARB, or human approval requirements.

# 7. Human Role Baseline
| Human Role | Primary Accountability | Minimum Skill Baseline |
| --- | --- | --- |
| Solutions Architect / IT Head | Architecture direction, conflict resolution, standards approval, high-impact AI use | S1 L5, S8 L4, S10 L4, S12 L5 |
| Software Development Lead | Code review, MicroFunction implementation, technical debt, branch quality | S1 L3, S3 L4, S4 L3, S11 L3 |
| DevSecOps Lead | CI/CD, GitOps, evidence pipeline, supply-chain, platform automation | S5 L4, S2 L3, S4 L3, S12 L3 |
| Security Administrator | Identity, secrets, access control, SBAC, OPA, classification, waivers | S2 L4, S8 L3, S12 L4 |
| QA / SDET Lead | TDD, contract/mutation/security testing, AI eval, fitness functions | S4 L4, S3 L2, S8 L3 |
| DBA / Data Engineer | Flyway, schema, RLS, lineage, vector storage, retrieval evidence | S6 L4, S2 L3, S4 L3 |
| SRE / Operations Lead | SLO, incident, telemetry, dashboards, resilience, support readiness | S9 L4, S5 L3, S12 L3 |
| Knowledge Governance Lead | Source authority, Obsidian/LLM Wiki, citations, Auto-Learn promotion | S10 L4, S12 L3, S8 L3 |
| Dynamic Workspace Lead | UX, widgets, templates, accessibility, responsive design, AI Panel alignment | S11 L4, S3 L3, S2 L3, S12 L3 |

# 8. AI Agent Role Catalog
| Agent Role | May Do | Required Skills | Must Not Do |
| --- | --- | --- | --- |
| Architecture Agent | Draft ADR/TDL, boundary review, fitness recommendations | S1, S10, S12 | Approve architecture, bypass ARB, or weaken EDP rules. |
| Backend Java Agent | Draft Java 25/Spring adapters, services, tests, MicroFunction steps | S3, S4, S1 | Commit directly, call provider SDKs, write direct SQL, or bypass ports/adapters. |
| Frontend / Workspace Agent | Draft React/Next.js widgets, AI Panel UI, accessibility tests | S11, S3, S4 | Make frontend business/security authority or expose sensitive data. |
| DevSecOps Pipeline Agent | Analyze CI failures, draft pipeline/evidence improvements | S5, S4, S12 | Disable gates, bypass scans, change protected branches, or deploy production. |
| Security Triage Agent | Classify findings, propose remediation, map abuse cases | S2, S4, S12 | Approve exceptions, rotate production secrets, or suppress findings. |
| Test Author Agent | Draft unit, contract, mutation, Playwright, DAST fixtures | S4, S3, S2 | Use production data or weaken assertions. |
| SRE Analysis Agent | Analyze traces/logs/metrics and draft incident hypotheses | S9, S10, S12 | Execute recovery outside approved Harness/runbook gates. |
| Knowledge Steward Agent | Detect stale knowledge, conflicts, missing citations, learning candidates | S10, S12, S8 | Promote knowledge without human review. |
| System Builder Agent | Normalize intake, draft contracts, proposals, code/config/test candidates | S1, S3, S5, S8, S12 | Silently mutate runtime, approve own output, or bypass CAB/ARB. |

# 9. Harness-Enforced Action Flow

Harness is the execution boundary between AI reasoning and tool action. An AI agent may propose an action, but Harness validates identity, skill, trust, scope, classification, policy, guardrail result, rate limit, approval requirement, and evidence contract before any tool executes.

Figure 2. Harness-Enforced Action Flow
| Step | Control | Minimum Evidence |
| --- | --- | --- |
| 1. Receive request or signal | Human request, CI failure, alert, incident, drift event, or knowledge review task | request_id, source, classification, trace_id |
| 2. Assemble context | Approved retrieval only; ACL, source tier, freshness, and classification filters applied | evidence pack, citations, source versions, freshness score |
| 3. Guardrail pre-check | Input/Retrieval rails validate context and prompt eligibility | guardrail policy version, allow/block result |
| 4. Propose action | Agent declares intended action, risk tier, confidence, EDP impact, files/tools | action proposal record |
| 5. SBAC validation | Skill, proficiency, classification, environment, and tool scope checked | skill decision ID, trust score, expiry status |
| 6. OPA decision | Policy-as-code determines allow/deny/escalate | OPA input/output, policy bundle version |
| 7. Approval if required | High-risk, low-confidence, Confidential/Restricted, production, or exception actions escalate | approver, reason, expiry, conditions |
| 8. Tool execution | Harness invokes approved tool/API with bounded credentials and rate limits | tool invocation ID, inputs, outputs, duration, status |
| 9. Evidence and learning | Audit/outbox record is written; learning candidate may be proposed | audit ID, evidence_ref, improvement_ref |

# 10. Dynamic Workspace, MicroFunction, API/Event, and DevSecOps Skill Requirements
| Domain | Mandatory Skill Treatment |
| --- | --- |
| Dynamic Workspace UX / Frontend | Skills must cover backend-governed widgets, policy-filtered templates, safe states, accessibility, responsive design, Admin Builder lifecycle, AI Panel boundary, telemetry, and evidence. Frontend code never becomes business/security authority. |
| MicroFunction Backend | Skills must support configuration-first runtime assembly, standard steps, thin adapters, policy, audit, outbox, idempotency, rollback, compensation, and traceable evidence. Code only the business gap. |
| API and Event Contracts | Skills must enforce OpenAPI, AsyncAPI, Kafka, Avro/JSON Schema, CloudEvents, idempotent consumers, DLQ, replay, schema evolution, Problem Details, and compatibility gates. |
| Database and Cache | Skills must enforce Flyway-only schema/seed changes, PostgreSQL as authority, Redis/Valkey as derivative cache, RLS, lineage, migration evidence, and rollback/forward-fix. |
| DevSecOps and GitNexus | Skills must produce CI/CD evidence, SAST/SCA/secret/authenticated DAST, SBOM/provenance, GitNexus impact analysis, CODEOWNERS review, and CAB/ARB approval where triggered. |
| Observability | Skills must preserve Log4j2 structured logs, OpenTelemetry traces/metrics/logs, Sentry errors, Loki logs, Tempo traces, Grafana dashboards, audit events, and trace reconstruction. |
| Runtime Toggles | Performance/debug telemetry may be tuned on the fly, but security, audit, policy decision, classification, denial, model-route, guardrail, and evidence signals are non-disableable. |

# 11. Auto-Heal, Auto-Learn, and Auto-Improve Skill Rules
| Loop | Allowed Skill Use | Required Gate |
| --- | --- | --- |
| Auto-Heal | Detect issue, retrieve evidence, classify cause, draft remediation, run safe non-production validation, propose PR/MR or runbook update. | No production mutation without human approval, OPA/SBAC, Harness, rollback, test evidence, and incident linkage. |
| Auto-Learn | Convert resolved incidents, accepted fixes, tests, RCA lessons, and standards updates into candidate knowledge. | Human review, citations, source hash, classification, freshness, conflict quarantine, and retrieval regression test. |
| Auto-Improve | Identify recurring defects, architecture drift, missing tests, performance bottlenecks, security gaps, and UX issues. | Ticket/ADR/TDL, impact analysis, tests, security review, evidence pack, rollback or compensation path. |

# 12. Evidence, Recertification, Suspension, and Waivers

Figure 3. Skill Evidence and Recertification Map
| Control | Rule |
| --- | --- |
| Skill evidence record | Must include actor_id, actor_type, skill_code, proficiency_level, trust_score, scope, classification ceiling, environment, tools, evidence_refs, expiry, reviewer, and recertification date. |
| Recertification | Quarterly by default; immediate after incident, failed audit, policy violation, security finding, tool change, model-route change, major architecture update, or expanded autonomy request. |
| Decay | Skills decay when unused, unsupported by recent evidence, linked to weak outputs, or affected by technology/policy changes. |
| Suspension | Suspended on policy breach, unauthorized tool use, unsafe AI output, failed audit, secret/PII leak, direct production mutation attempt, or repeated low-quality evidence. |
| Waiver | Waivers require owner, risk, expiry, compensating controls, evidence, reviewer, CAB/ARB where applicable, and exit plan. Waivers cannot approve illegal, unsafe, or untraceable actions. |

# 13. RACI
| Activity | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Skill taxonomy update | DevSecOps Lead / AI Governance | Solutions Architecture Office | Security, QA, SRE, Data, Knowledge | Developers, Auditors |
| Skill grant approval | Role owner / Security | IT Head or delegated owner | DevSecOps, HR if applicable, Internal Audit | Affected actor |
| AI agent skill certification | AI Governance / QA / Security | Architecture Board | DevSecOps, SRE, Data Governance | Agent owner, Internal Audit |
| High-risk action approval | Human approver / CAB | CAB / ARB / IT Head | Security, DevSecOps, Business Owner | Operations, Audit |
| Recertification and decay | Skill owner | Role owner | Security, QA, DevSecOps | Actor, Audit |
| Evidence review | QA / DevSecOps / Internal Audit | Solutions Architecture Office | Security, SRE, Knowledge Governance | CAB / ARB where triggered |

# 14. Implementation Roadmap
| Phase | Target Outcome | Exit Evidence |
| --- | --- | --- |
| Phase 1 - Register and normalize | Approve v3.2 skill families, role baselines, agent-role catalog, skill evidence schema. | Skill registry draft, owner list, SBAC mapping, review record. |
| Phase 2 - Enforce in DevSecOps | Connect skill declarations to PR/MR template, CI gates, GitNexus, OPA policy, and evidence pack. | CI evidence, policy tests, PR/MR skill declaration samples. |
| Phase 3 - Agent certification | Certify selected agents for advisory/read/draft tasks and limited non-production Harness actions. | Agent profiles, trust score, eval reports, blocked-action tests. |
| Phase 4 - Dynamic Workspace and System Builder | Apply skills to Admin Builder, AI Panel, template lifecycle, MicroFunction runtime, and System Builder proposals. | UX evidence, template approval, action registry test, MicroFunction trace. |
| Phase 5 - Continuous improvement | Operate recertification, decay, suspension, Auto-Learn promotion, and skill improvement backlog. | Quarterly review pack, audit evidence, improvement backlog, updated skills. |

# 15. Acceptance Criteria

Skill registry exists with owners, versions, allowed actions, classification ceilings, environment scope, tools, trust thresholds, evidence, expiry, and recertification rules.

Human role baseline and AI agent role catalog are approved and mapped to SBAC and OPA policies.

Harness blocks unknown actors, expired skills, low trust, missing approvals, missing evidence, and prohibited actions.

AI agents cannot directly access production credentials, Git protected branches, CI/CD deployment controls, database administration, Kubernetes, OpenKM, or model-provider SDKs.

PR/MR evidence includes skill declaration, EDP impact, tests, scans, GitNexus impact, policy decisions, rollback path, and reviewer approval.

Dynamic Workspace, MicroFunction, API/event, database/cache, observability, security, and DevSecOps skills are represented in the framework.

Auto-Heal, Auto-Learn, and Auto-Improve produce candidate proposals only unless a governed, approved, reversible Harness action is explicitly allowed.

Runtime toggle controls preserve non-disableable security, audit, policy, classification, guardrail, model-route, denial, and evidence signals.

Skill recertification, decay, suspension, waiver, and audit review are operational and evidence-producing.

AVCI is satisfied for every skill, grant, action, decision, output, trust change, and improvement.

# 16. Open Reconciliation Items
| Item | Treatment |
| --- | --- |
| 06 numbering collision | CLAUDE.md Reference and Revision Control Matrix both use 06. Revision Control Matrix should remain 06 register/control matrix, while CLAUDE.md may need canonical suffix confirmation in 00D. |
| 07B prior update verification | Do not regenerate 07B unless missing/stale in the aligned desktop folder. Verify the expected v1.1_Revised or later file in final reconciliation. |
| Skill registry physical schema | Confirm whether skills, trust, agent roles, and recertification live in AI agent registry, SBAC catalog, or dedicated skills schema. Track through register 00D. |
| Runtime telemetry toggles | Ensure the non-disableable signal rule is propagated to SRE, Dynamic Workspace, observability, and runbook documents. |
| Agent autonomy certification | Ensure 42D-42S control family maps to skill families, trust tiers, and Harness action classes. |

# 17. AVCI Compliance Summary
| AVCI Property | v3.2 Evidence |
| --- | --- |
| Attributable | Every skill, role, agent, grant, action, trust change, approval, and waiver has an owner, source, actor, reviewer, and evidence reference. |
| Verifiable | Skills are verified through tests, scans, policy decisions, GitNexus impact, trace/audit data, evaluations, recertification, and CI/CD evidence packs. |
| Classifiable | Skill grants and actions carry classification ceilings, data-handling rules, model-route eligibility, environment scope, retention, and redaction requirements. |
| Improvable | Skill decay, incidents, RCA, Auto-Learn candidates, audit findings, training gaps, and technology changes feed controlled improvement backlog and recertification. |

## Final Control Statement

AIRA may use AI to multiply DevSecOps capability only when skill boundaries, policy decisions, guardrails, Harness execution, human accountability, evidence, and reversibility remain stronger than the automation being introduced. Skills enable safe acceleration; they do not transfer governance authority to AI.

