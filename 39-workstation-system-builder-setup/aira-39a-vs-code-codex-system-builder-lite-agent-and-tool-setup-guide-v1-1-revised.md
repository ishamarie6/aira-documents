---
title: "VS Code Codex System Builder Lite Agent and Tool Setup Guide"
doc_id: "AIRA-39A"
version: "v1.1"
status: "revised"
category: "Workstation and system builder setup"
source_docx: "AIRA_39A_VS_Code_Codex_System_Builder_Lite_Agent_and_Tool_Setup_Guide_v1.1_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 39-workstation-system-builder-setup
  - revised
  - aira-39a
---



# VS Code Codex System Builder Lite Agent and Tool Setup Guide



AIRA

AI-Native Enterprise Platform

AIRA VS Code Codex System Builder Lite Agent and Tool Setup Guide

v1.1 Revised

VS Code and Codex Governance - System Builder Lite - Agent and Tool Controls - Prompt Execution Workflow - DevSecOps Evidence - Dynamic Workspace and MicroFunction Readiness
| Property | Value |
| --- | --- |
| Document ID | AIRA-DOC-039A |
| Canonical Filename | AIRA_39A_VS_Code_Codex_System_Builder_Lite_Agent_and_Tool_Setup_Guide_v1.1_Revised.docx |
| Version | v1.1 - 09 v3.2, 39B v1.3, 39C v1.2, Dynamic Workspace, MicroFunction Runtime, DevSecOps Evidence, GitNexus, Resilience Lab, Runtime Toggle, and Governed Agent Alignment Update |
| Supersedes | 39A-AIRA_VS_Code_Codex_System_Builder_Lite_Agent_and_Tool_Setup_Guide_v1.0.docx |
| Status | Draft for Architecture, DevSecOps, Security, Platform Engineering, QA/SDET, AI Governance, DBA, Knowledge Governance, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; DevSecOps Lead; Software Development Lead; Security Architecture; Platform Engineering; QA/SDET; DBA; SRE / Operations; AI Governance; Knowledge Governance; Internal Audit |
| Primary Audience | Software Developers; VS Code Codex users; System Builder Lite operators; logical agent owners; technical leads; QA/SDET; Security; DBA; DevSecOps; Platform Engineering; AI Engineering; reviewers |
| Primary Parents | 09-AIRA Greenfield Environment Standard v3.2 Revised; 39B Greenfield AI DevSecOps Workstation Setup and System Builder Lite Implementation Guide v1.3 Revised; 39C Team Greenfield AI DevSecOps Workstation and Governed Agent Setup Playbook v1.2 Revised |
| Companion Sources | 01/01A AVCI and Enterprise Design Principles; 07 Skills Framework; 07B Team Transformation; 10 MicroFunction; 11/20 DevSecOps and Evidence Pack; 12A/41/46-61 Dynamic Workspace; 15 API; 16/16A Flyway and Database; 17 Security; 19 GitNexus; 23C PoC 1 Execution; 31A Observability; 42D-42S Agent Governance; 43 Continuous Improvement; 43D PoC 1A Execution |
| External Alignment Reference | NIST SP 800-218 SSDF; OWASP ASVS 5.0.0; OpenTelemetry Semantic Conventions; SLSA v1.2 |
| Review Cadence | Monthly during PoC 1/1A/2 execution; quarterly after stabilization; unscheduled on Codex, VS Code, tool, MCP, agent, policy, CI/CD, evidence, security, or source-baseline change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Greenfield / System-Builder-Lite / 39A / v1.1 / |
| Mandatory Practice Statement VS Code and Codex may accelerate AIRA development, but they must not become an architecture bypass, security bypass, approval bypass, or uncontrolled automation path. Codex may generate candidate code, configuration, migrations, tests, policies, documentation, prompts, runbooks, and evidence only inside a governed feature branch and only under AIRA repository instructions, tool restrictions, CI/CD gates, maker-checker review, and AVCI evidence. Codex must not approve, merge, deploy, disable controls, access production credentials, or silently mutate runtime behavior. System Builder Lite is the controlled bridge between manual AI-assisted development and the future full System Builder. |
| --- |

# Static Table of Contents

1. Executive Summary

2. v1.1 Update Verdict

3. Purpose, Scope, and Authority

4. Operating Position: System Builder Lite Before Prompt Execution

5. VS Code and Codex Setup Principles

6. Execution Surface and Authority Boundary

7. Logical Agent Model and Registry

8. Tool Registry and Action Authorization

9. Repository Instruction Model and AGENTS.md Templates

10. Branch, PR/MR, CODEOWNERS, and Evidence Controls

11. Codex Pre-Flight and Prompt Execution Workflow

12. Dynamic Workspace and MicroFunction Alignment Rules

13. DevSecOps, GitNexus, CI/CD, and Evidence Pack Gates

14. API, Eventing, Database, and Contract Readiness

15. Observability, Runtime Toggles, and Safe Telemetry Controls

16. Security, OPA/SBAC, Secrets Hygiene, and Authenticated DAST

17. Concurrency, Heavy Transaction, and Resilience Lab Readiness

18. Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop

19. Progressive Autonomy and Full System Builder Transition

20. RACI and Separation of Duties

21. Implementation Roadmap

22. Acceptance Criteria and Definition of Done

23. Open Issues and AVCI Reconciliation Items

24. AVCI Compliance Summary

Appendix A. Copy-Ready Root AGENTS.md Baseline

Appendix B. Copy-Ready Codex Pre-Flight Prompt

Appendix C. PR/MR Evidence Summary Template

# 1. Executive Summary

This v1.1 revision updates the original 39A VS Code Codex guide into the executable System Builder Lite control layer for AIRA developers. It keeps the original decision that the team should define logical agents, repository instructions, allowed tools, prohibited actions, branch controls, CI/CD gates, and evidence templates before running PoC prompts. It adds the controls required by the revised 09, 39B, and 39C documents: greenfield environment readiness, Day 0 activity ledger discipline, workstation cohort rollout, Dynamic Workspace readiness, MicroFunction runtime readiness, GitNexus evidence, runtime telemetry toggles, resilience lab setup, OPA/SBAC expansion, authenticated DAST boundaries, and Auto-Heal/Auto-Learn/Auto-Improve candidate governance.

System Builder Lite is intentionally not the full System Builder. It is the minimum controlled operating layer that lets developers use Codex productively while preserving AIRA enterprise architecture, security, DevSecOps, MicroFunction, Dynamic Workspace, testability, observability, rollbackability, and AVCI evidence.
| Management Decision Proceed with System Builder Lite before executing large Codex prompts. VS Code remains the developer workspace. Codex is a branch-bound Builder Agent. Human reviewers, CI/CD, OPA/SBAC, GitNexus read-only impact analysis, and evidence packs remain the checker and promotion authority. |
| --- |
| Strategic Outcome | v1.1 Required Result |
| --- | --- |
| Controlled AI-assisted coding | Codex operates only inside local approved folders, feature branches, repository instructions, and PR/MR review gates. |
| Dynamic Workspace safety | Generated UI remains backend-governed, policy-filtered, MicroFunction-backed, contract-bound, observable, accessible, and reversible. |
| MicroFunction discipline | Generated backend changes preserve configuration-first assembly, ports/adapters, idempotency, outbox/audit evidence, and fail-closed behavior. |
| DevSecOps evidence by construction | Build, test, security, policy, Flyway, OpenAPI/AsyncAPI, GitNexus, and evidence manifest gates are required before merge. |
| Security and secrets hygiene | No production credentials, raw tokens, secrets, PII, or Restricted data are exposed in prompts, logs, screenshots, evidence, or generated files. |
| Progressive autonomy | Any later tool or agent authority is earned through SBAC, OPA, trust evidence, guardrails, audit, rollback, and human approval. |

# 2. v1.1 Update Verdict
| Area | Verdict | Required Treatment |
| --- | --- | --- |
| Original 39A purpose | Retained | Keep the baseline role of 39A as the minimum VS Code + Codex operating model before prompt execution. |
| 09 v3.2 alignment | Strengthened | Treat Codex setup as part of governed greenfield readiness, not only an IDE preference. |
| 39B v1.3 alignment | Strengthened | Codex starts only after secure workstation, Git, VS Code, local workspace, source register, evidence register, AGENTS.md, branch rules, and validation gates exist. |
| 39C v1.2 alignment | Added | Every meaningful Codex activity must be logged in the Activity Ledger with owner, purpose, source, classification, evidence, result, risk, and improvement path. |
| Dynamic Workspace alignment | Added | Codex-generated frontend artifacts require backend authority, generated clients, OPA/SBAC policy filtering, runtime config references, telemetry, a11y and visual tests. |
| MicroFunction alignment | Added | Generated backend artifacts must use canonical step/catalog patterns, ports/adapters, Flyway, outbox, idempotency, retry, DLQ, replay, safe responses, and evidence. |
| Tool/agent expansion | Tightened | MCP/connectors, local shells, repo write actions, and tool execution remain disabled or approval-gated until registry, SBAC, OPA, audit, and rollback controls exist. |
| Runtime toggles | Added | Logging, tracing, diagnostic verbosity, feature flags, AI panels, and expensive debug instrumentation can be toggleable only by governed configuration and audit. |

# 3. Purpose, Scope, and Authority

## 3.1 Purpose

Define the governed VS Code and Codex operating model for AIRA System Builder Lite execution.

Prevent casual prompt execution, uncontrolled AI-generated changes, unmanaged agent/tool expansion, direct model calls, credential leakage, and premature autonomy.

Establish repository instructions, logical agents, allowed/prohibited actions, branch controls, CI/CD gates, evidence templates, Activity Ledger entries, and maker-checker review before PoC prompts.

Align Codex execution with Dynamic Workspace, MicroFunction, DevSecOps, API/eventing, database/Flyway, observability, security, resilience lab, and Auto-* improvement standards.

Provide copy-ready templates for AGENTS.md, Codex pre-flight prompts, PR/MR evidence summaries, and execution checkpoints.

## 3.2 Scope
| In Scope | Out of Scope |
| --- | --- |
| VS Code and Codex setup as a branch-bound System Builder Lite development surface. | Direct production deployment, direct merge to protected branches, or production mutation by Codex. |
| Repository-level and directory-level AGENTS.md instructions for backend, frontend, db/Flyway, policy, docs/evidence, and scripts. | Autonomous agents with production credentials, direct production databases, privileged Keycloak admin access, or deployment keys. |
| Logical agent roles for Builder, Architecture Reviewer, Security Reviewer, QA/SDET, DBA/Flyway, Frontend/Dynamic Workspace, Evidence, DevSecOps, and Knowledge Governance. | Full MCP connector rollout, unrestricted shell tools, direct provider SDK calls from application code, or unreviewed memory/RAG writes. |
| Tool registry, action taxonomy, approval gates, Activity Ledger, CI/CD evidence, and PR/MR acceptance controls. | Replacing CAB, ARB, Security, DBA, QA, DevSecOps, Product Owner, Internal Audit, or maker-checker accountability. |
| Preconditions for PoC 1, PoC 1A, PoC 2, Dynamic Workspace, MicroFunction, observability, resilience, and DevSecOps evidence readiness. | Full AIRA System Builder runtime implementation, production-grade agent registry automation, or Level 8 delegated action without trust evidence. |

## 3.3 Authority and Precedence
| Level | Authority | Role |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance | Final authority for production-impacting controls, major architecture decisions, exceptions, and autonomy delegation. |
| L1 | AIRA AVCI, Enterprise Architecture, Security, DevSecOps, MicroFunction, Dynamic Workspace, Database, Observability, Change, and AI Governance Standards | Universal rules for architecture, evidence, classification, testability, security, rollback, observability, policy, and improvement discipline. |
| L2 | 09 v3.2, 39B v1.3, 39C v1.2, and this 39A v1.1 guide | Greenfield environment, workstation, team rollout, Codex, System Builder Lite, agent/tool setup, and execution baseline. |
| L3 | AGENTS.md, CODEOWNERS, PR/MR templates, CI/CD, OPA/Rego, Flyway, GitNexus, evidence manifests, Activity Ledger | Execution-level enforcement and evidence. |
| L4 | Feature branches, test results, scan outputs, policy decisions, prompt logs, review records | Implementation proof and improvement input. |
| Conflict Rule Where documents appear inconsistent, apply the stricter AIRA control temporarily, log the issue as an AVCI reconciliation item, assign an owner, and resolve through governed review. Do not silently select the easiest interpretation. |
| --- |

# 4. Operating Position: System Builder Lite Before Prompt Execution

The team must not run PoC 1, PoC 1A, Dynamic Workspace, MicroFunction, API, database, or DevSecOps prompts as one-off Codex requests. Large AI-assisted generation starts only after the local workspace, repository governance, AGENTS.md rules, branch controls, reviewer ownership, CI/CD gates, evidence paths, and Activity Ledger are ready.
| System Builder Lite Element | Mandatory Rule | Evidence |
| --- | --- | --- |
| Local controlled folder | Use the approved AIRA workspace folder, not Downloads, Desktop root, user profile root, or uncontrolled OneDrive root. | SOURCE_REGISTER.md, TOOL_REGISTRY.md, EVIDENCE_REGISTER.md, SETUP_EXECUTION_LOG.md. |
| Codex role | Codex acts as Builder Agent only. It may draft, generate, refactor, test, and summarize inside a feature branch. | AI-use declaration, prompt log, Activity Ledger entry, branch name, commit hash. |
| Human role | Human developer remains maker; named reviewer remains checker; CI/CD verifies; approver approves. | CODEOWNERS approvals, PR/MR evidence, CI run ID. |
| Repository instructions | AGENTS.md files define allowed scope, prohibited actions, standards, and required evidence. | Root and directory-level AGENTS.md committed. |
| Tool restrictions | No production credentials, deployment keys, direct model-provider SDKs, unrestricted MCP, or privileged scripts. | TOOL_REGISTRY.md, secrets scan, OPA tool-action policy. |
| Promotion gate | No merge or activation without CI, security, policy, test, architecture fitness, evidence, and human approval. | Pipeline evidence pack, GitNexus read-only impact report, PR/MR AVCI summary. |

# 5. VS Code and Codex Setup Principles
| ID | Principle | Required Behavior |
| --- | --- | --- |
| VCX-01 | Codex after VS Code and Git | Codex is activated after VS Code, Git identity, approved local folder, source/evidence registers, and repository controls exist. |
| VCX-02 | Existing folder discipline | Open the approved local repository folder only; do not let Codex infer uncontrolled context from personal folders. |
| VCX-03 | Branch-bound generation | All Codex file changes occur in a feature branch linked to a task/intake record. |
| VCX-04 | Prompt pre-flight | Before modifying files, Codex reads AGENTS.md and returns plan, impacted files, risks, tests, evidence, and reviewer roles. |
| VCX-05 | No hidden authority | Codex output is candidate work. It is not design approval, security approval, DBA approval, CAB approval, or production authority. |
| VCX-06 | Contract first | API, event, schema, MicroFunction, and Dynamic Workspace changes start from approved OpenAPI, AsyncAPI, Avro/JSON Schema, Flyway, policy, and config contracts. |
| VCX-07 | Evidence always | Each Codex session has Activity Ledger entry, prompt source, changed files, commands run, tests, scans, limitations, and improvement items. |
| VCX-08 | Fail closed | Missing identity, policy, secrets control, guardrail, audit, tests, evidence, or rollback path blocks merge or activation. |

# 6. Execution Surface and Authority Boundary
| Execution Surface | Allowed Use | Prohibited Use | Evidence Required |
| --- | --- | --- | --- |
| ChatGPT AIRA Project | Architecture review, source-aligned guidance, prompt improvement, document synthesis, setup sequencing. | Production secrets, direct code repository mutation, direct deployment, unrestricted Restricted data copy/paste. | Conversation summary, source references, decision record where material. |
| VS Code + Codex | Candidate code, tests, config, policies, migrations, docs, run commands, refactor plan in local branch. | Merge, approve, deploy, disable security controls, access production credentials, bypass AGENTS.md. | Prompt log, branch, changed files, tests, PR/MR AVCI summary. |
| Local CLI / PowerShell | Human-executed setup, build, tests, scans, render, local validation, evidence capture. | AI-executed privileged admin commands without human review; production shell access. | Command log, screenshots where safe, hash/output, Activity Ledger. |
| CI/CD | Automated build, tests, scan, policy, contract, Flyway, architecture fitness, evidence manifest. | Manual bypass of critical gates or undocumented waiver. | Pipeline ID, artifacts, SBOM, scan reports, evidence pack. |
| GitNexus | Read-only code intelligence, impact analysis, affected tests, architecture drift signals. | Commit, merge, deploy, production mutation, replacing tests/scans/human review. | Commit-bound GitNexus report and reviewer interpretation. |
| MCP / Connectors | Disabled by default; read-only candidate use after registry, SBAC, OPA, audit, and security review. | Unrestricted state-changing tools or production connectors. | Tool manifest, OPA decision, dry-run, approval, audit trail. |

# 7. Logical Agent Model and Registry

During PoC 1 and PoC 1A, agents are logical operating roles expressed through AGENTS.md, Codex prompts, reviewer checklists, and human responsibilities. They are not approved production autonomous agents. They must later be migrated into the full AIRA Agent Registry when PoC 2 and agent governance implementation mature.
| Logical Agent | Primary Tool | Allowed Authority | Prohibited Authority | Required Evidence |
| --- | --- | --- | --- | --- |
| Builder Agent | Codex in VS Code | Generate candidate code/config/tests/migrations/policies/docs on feature branch. | Approve, merge, deploy, disable controls, touch production credentials. | Prompt log, changed files, tests, evidence summary. |
| Architecture Reviewer | Human + optional AI review prompt | Check SOLID, Clean Architecture, DDD, ports/adapters, MicroFunction and Dynamic Workspace boundaries. | Approve own generated output without independent review. | Architecture review checklist, ADR/TDL/waiver if needed. |
| Security Reviewer | Human Security + OPA/SAST/DAST tools | Check OPA/SBAC, secrets, input validation, ASVS controls, fail-closed paths. | Accept secrets leakage, raw token logging, or frontend authority. | Security scan, policy tests, remediation evidence. |
| QA/SDET Agent | Human QA + test generation prompts | Generate and improve unit, integration, Playwright, mutation, contract, regression, failure tests. | Declare acceptance without executed tests. | Test report, coverage/mutation summary, failing tests backlog. |
| DBA/Flyway Agent | DBA + Codex draft | Review Flyway migrations, RLS, indexes, seed data, rollback/forward-fix, outbox/inbox. | Manual production DDL or destructive unapproved migrations. | Flyway clean/upgrade reports, migration summary. |
| Frontend/Dynamic Workspace Agent | Frontend engineer + Codex | Review Next.js, generated clients, component registry, a11y, policy-filtered layout, telemetry. | Treat UI as authorization/business authority. | A11y/visual tests, OpenAPI binding, policy denial tests. |
| Evidence Agent | Developer/DevSecOps | Collect PR/MR AVCI summary, evidence manifest, GitNexus report, CI artifacts, Activity Ledger entry. | Invent evidence or omit known gaps. | Evidence pack, hashes, links, reviewer sign-off. |
| DevSecOps Agent | DevSecOps + CI | Maintain pipeline gates, secret scans, SAST/SCA/DAST, SBOM, provenance, evidence. | Disable gates to make merge pass. | Pipeline run, waiver record, remediation plan. |

# 8. Tool Registry and Action Authorization
| Tool / Capability | Default State | Allowed Use | Approval Gate |
| --- | --- | --- | --- |
| VS Code | Approved after workstation baseline | Repository editing, review, terminal commands, extensions from approved list. | Workstation evidence and tool inventory. |
| Codex Extension | Approved after AGENTS.md and branch controls | Branch-bound candidate generation and tests. | Pre-flight plan approved by developer; PR/MR review for merge. |
| Git / GitHub / GitLab | Approved with least privilege | Branch, commit, push PR/MR, review, evidence links. | Protected branch, CODEOWNERS, signed/identified commits where feasible. |
| PowerShell / Local Shell | Human-executed only | Install, build, test, scan, local validation, evidence capture. | Activity Ledger and command review for privileged actions. |
| Docker / Devcontainer | Approved for local isolated dev/test | Reproducible runtime, Testcontainers, Kafka/PostgreSQL/OPA local labs. | Image pinning, SBOM/SCA, no production secrets. |
| OPA/Rego | Required for policy | Policy tests, local decisions, CI gates. | Security/architecture review before weakening any rule. |
| Flyway | Required from Day 0 | Schema creation, migrations, seeds, RLS, views, indexes. | DBA review for material data/schema changes. |
| GitNexus | Read-only derivative | Code intelligence, blast radius, affected tests, architecture drift. | No write authority; corroborate with tests/scans/human review. |
| OWASP ZAP / DAST | Non-prod synthetic scope | Authenticated DAST against dev/test using synthetic users. | Security-approved test account, scan scope, remediation evidence. |
| MCP / External Connectors | Disabled by default | Read-only pilot only after tool manifest and SBAC/OPA are ready. | Security, AI Governance, DevSecOps, audit approval. |

# 9. Repository Instruction Model and AGENTS.md Templates

AGENTS.md is the first executable policy surface for Codex behavior. It does not replace OPA/SBAC, CODEOWNERS, CI/CD, or human review, but it reduces prompt drift by making repository rules explicit and discoverable before file modification.
| File | Purpose | Minimum Required Controls |
| --- | --- | --- |
| /AGENTS.md | Root repository rules and universal AIRA constraints. | AVCI, EDP-01..20, no production secrets, branch-only changes, no direct deployment, read governing docs, pre-flight first. |
| /backend/AGENTS.md | Backend Java/Spring/MicroFunction rules. | Clean Architecture, ports/adapters, Java 25, MicroFunction step catalog, OPA/SBAC, outbox, audit, OTel, tests. |
| /frontend/AGENTS.md | Next.js/Dynamic Workspace rules. | Backend-governed UI, generated clients, no frontend authority, a11y, policy filtering, telemetry, safe session display. |
| /db/AGENTS.md | Flyway and PostgreSQL rules. | Flyway-only, additive migrations, no manual DDL, seed governance, RLS, schema ownership, rollback/forward-fix. |
| /policy/AGENTS.md | OPA/Rego and SBAC rules. | Fail-closed policy, negative tests, skill/role/scope mapping, no hardcoded authorization in app logic. |
| /docs/AGENTS.md | Documentation and evidence rules. | No full code copy to Obsidian, classification, citations/source refs, evidence manifests, revision-control notes. |
| /.github/AGENTS.md | CI/CD, PR/MR, templates, workflow rules. | Mandatory gates, CODEOWNERS, evidence manifest, security scan, GitNexus report, waiver handling. |

# 10. Branch, PR/MR, CODEOWNERS, and Evidence Controls
| Control | Minimum Rule | Merge-Blocking Condition |
| --- | --- | --- |
| Branching | Use named feature branches linked to ticket/intake, e.g., feature/poc1-auth-login-context. | Codex attempts direct main branch change or no task reference exists. |
| CODEOWNERS | Architecture, security, DBA, QA/SDET, frontend, DevSecOps, and AI Governance reviewers are mapped by path. | Required reviewer path absent for changed files. |
| PR/MR template | Includes scope, source prompt, AI use, EDP/AVCI impact, tests, scans, policy, migration, rollback, evidence, limitations. | Template incomplete or evidence links missing. |
| CI/CD gates | Build, test, type, lint, OPA, Flyway, OpenAPI/AsyncAPI, secret scan, SAST/SCA, architecture fitness, evidence manifest. | Critical/high failure without approved waiver. |
| Evidence pack | Collect CI artifacts, GitNexus report, test reports, scan results, policy decisions, screenshots where safe, Activity Ledger link. | Evidence cannot reconstruct what changed, why, who checked, or how to reverse. |
| Waiver discipline | Waivers require owner, reason, expiry, risk, compensating control, remediation plan, and approving authority. | Indefinite or ownerless waiver; waiver used to bypass security-critical gate. |
| Promotion | Merge does not equal production activation. Promotion follows release/CAB/environment gates. | Attempt to deploy from local Codex session or unapproved pipeline. |

# 11. Codex Pre-Flight and Prompt Execution Workflow

# 11.1. Pre-Flight Before Any Large Prompt
| Field | Required Content |
| --- | --- |
| Objective | Force Codex to inspect the repository instructions, source baseline, impacted areas, risks, tests, and evidence needs before file modification. |
| Exit Gate | Codex stops after the plan and waits for human confirmation. |
| Minimum Evidence | Pre-flight plan, reviewer role list, branch, source references, Activity Ledger entry. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 1 | Open approved local repository folder in VS Code. | Correct workspace path in Activity Ledger. |
| 2 | Create or checkout feature branch. | Branch name and task/intake ID recorded. |
| 3 | Ask Codex to read AGENTS.md files and return interpretation. | Codex confirms rules and prohibited actions. |
| 4 | Ask Codex for impact analysis and generation plan only. | Plan lists files, contracts, tests, policies, migrations, Dynamic Workspace changes, and reviewers. |
| 5 | Human reviews plan and approves or corrects before edits. | Plan approval note in Activity Ledger. |

# 11.2. Generation and Verification Loop
| Field | Required Content |
| --- | --- |
| Objective | Generate candidate artifacts in controlled increments and verify after each material change. |
| Exit Gate | Critical/high findings are fixed or formally waived before PR/MR acceptance. |
| Minimum Evidence | Test outputs, scans, GitNexus report, evidence manifest, PR/MR summary. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 1 | Execute prompt in small scoped increments, not one uncontrolled mega-prompt. | Incremental commits or staged changes. |
| 2 | Run local tests and commands proposed by Codex only after human review. | Command outputs captured where safe. |
| 3 | Run relevant policy, Flyway, frontend, backend, and architecture checks. | Pass/fail evidence and remediation notes. |
| 4 | Generate PR/MR AVCI summary and known limitations. | Evidence summary committed or pasted into PR/MR. |
| 5 | Request independent checker review. | Architecture/security/QA/DB/frontend/evidence review comments. |

# 12. Dynamic Workspace and MicroFunction Alignment Rules
| Area | Codex Must Do | Codex Must Not Do |
| --- | --- | --- |
| Dynamic Workspace authority | Generate UI/components that bind to approved APIs, policy-filtered workspace resolver, component registry, and generated clients. | Invent endpoints, hardcode authorization, expose hidden payload fields, or make frontend business authority. |
| Next.js rendering | Follow approved SSR/ISR/PPR/CSR strategy by page/component risk, data sensitivity, and performance need. | Render Restricted or policy-sensitive data client-side without backend filtering and safe session context. |
| MicroFunction runtime | Use canonical transaction codes, step catalog, runtime configuration, ports/adapters, audit/outbox, idempotency, and evidence records. | Place business logic in controllers, direct DB/Kafka/Redis/OpenKM/model calls inside domain logic, or bypass runtime config. |
| Policy binding | Call OPA/SBAC through policy adapter and emit policy decision evidence. | Hardcode role checks or hide policy behavior in UI or service logic. |
| Observability | Emit safe traces, logs, metrics, audit, evidence_ref, trace_id, request_id, correlation_id, and classification. | Log tokens, secrets, raw PII, raw prompts, account numbers, documents, embeddings, or high-cardinality metric labels. |
| Reversibility | Add feature flags, safe-disable, rollback/forward-fix, compensation, and cache invalidation plan. | Generate irreversible changes without rollback or remediation evidence. |

# 13. DevSecOps, GitNexus, CI/CD, and Evidence Pack Gates
| Gate | Minimum Check | Evidence Output |
| --- | --- | --- |
| Build and type safety | Backend build, frontend build, type checks, lint. | CI logs, build artifacts, toolchain versions. |
| Unit/component tests | JUnit 5, frontend component tests, service/adapters tests. | Test reports, coverage summary where available. |
| Contract tests | OpenAPI validation, generated clients, AsyncAPI/CloudEvents schema validation where applicable. | Contract lint report, compatibility result. |
| Database tests | Flyway clean migrate, upgrade path, seed validation, rollback/forward-fix plan. | Flyway report, checksum, DBA review. |
| Policy tests | OPA/Rego allow/deny/negative tests, SBAC skill scope tests. | Policy test report, decision examples. |
| Security gates | Secret scan, SAST, SCA, authenticated DAST in non-prod synthetic scope where applicable. | Findings, severity, remediation evidence, waiver record. |
| Architecture fitness | Boundary checks, direct-dependency bans, no direct provider calls, no frontend authority, no controller business logic. | Fitness function report and failures. |
| GitNexus read-only analysis | Impact analysis, code map, affected tests, architecture drift, security-sensitive paths. | Commit-bound GitNexus report. |
| Evidence finalization | AVCI summary, activity ledger, known limitations, rollback, improvement backlog. | Evidence pack path and PR/MR summary. |

# 14. API, Eventing, Database, and Contract Readiness
| Contract Domain | Required Codex Behavior | Rejection Condition |
| --- | --- | --- |
| OpenAPI | Update or generate API contract before controllers/clients; preserve error model, security, idempotency, correlation, classification. | Controller created without approved contract or generated client. |
| AsyncAPI / Kafka | Define topics, producers/consumers, CloudEvents envelope, Avro/JSON schema, schema evolution, retry/DLQ/replay. | Event published without schema, outbox, idempotent consumer, or replay handling. |
| CloudEvents | Use consistent id, source, type, subject, time, data schema, correlation_id, causation_id, trace_id, classification. | Ad hoc event payloads without metadata or compatibility. |
| Database / Flyway | Use Flyway from Day 0; additive migrations, schema ownership, RLS where needed, seed governance, migration evidence. | Manual DDL, destructive schema change, uncontrolled seed, or untracked migration. |
| Outbox / Inbox | Mutating transactions emit outbox where integration event required; consumers use inbox/dedup and idempotency keys. | Direct publish without transactional boundary or duplicate-safe consumer. |
| Schema evolution | Backward-compatible changes, versioned schemas, consumer impact check, migration and replay plan. | Breaking contract without versioning, compatibility evidence, or consumer migration. |

# 15. Observability, Runtime Toggles, and Safe Telemetry Controls
| Control | Default Rule | Runtime Toggle Boundary |
| --- | --- | --- |
| Log4j2 structured logging | Structured, redacted, classification-aware logs with trace_id/request_id; no secrets or raw PII. | Verbosity may increase temporarily in dev/test with audit and expiry; production changes require approved runtime config. |
| OpenTelemetry traces | Propagate trace_id across frontend, gateway, backend, MicroFunction, DB, Kafka, workflow, AI gateway where applicable. | Sampling can be tuned through approved config; protected flows keep minimum trace/audit correlation. |
| Metrics | Bounded cardinality metrics for latency, success/failure, policy denial, queue age, retry, DLQ, replay, cache hit/miss. | Expensive or high-cardinality metrics disabled by default unless reviewed. |
| Sentry / error monitoring | Safe error grouping, source release, environment, trace correlation, no sensitive payloads. | Diagnostic context can be elevated only with redaction and TTL. |
| Loki / Tempo / Grafana | Dashboards for build, runtime, policy denial, workspace health, MicroFunction traces, eventing, errors, CI gates. | Dashboard access filtered by classification and role. |
| Audit and evidence | Audit cannot be disabled for protected actions. Evidence_ref required for material changes and runtime decisions. | Debug telemetry may toggle; audit/evidence for protected actions must not be disabled. |
| Feature flags | Use feature flags for PoC 1A and dynamic capabilities; defaults fail safe. | Flag changes require owner, reason, environment, expiry, rollback, and audit. |

# 16. Security, OPA/SBAC, Secrets Hygiene, and Authenticated DAST
| Security Area | Mandatory Codex Control | Evidence |
| --- | --- | --- |
| OPA/SBAC | Generated authorization uses policy adapter and skill/role/scope inputs; missing policy fails closed. | Policy tests, decision logs, negative tests. |
| Secrets hygiene | No secrets in prompts, .env committed files, screenshots, logs, tests, docs, Obsidian, LLM Wiki, GitNexus reports, or AI memory. | Secret scan, redaction review, approved secret reference. |
| Authentication | Use Keycloak/OIDC/PKCE or approved identity pattern; no custom password engine in AIRA application code. | Security review, token-handling tests, safe response check. |
| Secure APIs | Validate input, enforce authn/authz, Problem Details, rate limits, idempotency, safe errors, CORS/CSRF where applicable. | OpenAPI security review, API tests, ASVS mapping. |
| Authenticated DAST | Use synthetic non-prod accounts and approved scope; no production target or real customer data. | DAST plan, scan report, findings remediation. |
| Abuse cases | Prompt injection, tool abuse, privilege escalation, over-broad retrieval, schema drift, frontend authority, replay, duplicate effects. | Threat/abuse case checklist and controls. |
| Remediation evidence | Critical/high findings block merge unless approved waiver exists. | Remediation PR, retest result, waiver with expiry. |

# 17. Concurrency, Heavy Transaction, and Resilience Lab Readiness

Codex-generated code must be testable under retry, duplicate, concurrent, heavy-load, and failure-aware conditions. The workstation and repository must support a Resilience Lab before heavy business expansion.
| Readiness Area | Required Test / Control | Evidence |
| --- | --- | --- |
| Idempotency | Idempotency keys, replay guards, deduplication, safe retries for mutating APIs/events. | Unit/integration idempotency tests. |
| Outbox/inbox | Transactional outbox, inbox/dedup for consumers, ordered processing where required. | DB state + Kafka/Testcontainers tests. |
| Concurrency | Optimistic locking, unique constraints, isolation review, race-condition tests. | Concurrent test results and failure-mode notes. |
| Retry and DLQ | Bounded retry, backoff, circuit breaker, DLQ, replay procedure, poison message handling. | Retry/DLQ/replay tests and runbook. |
| Load and backpressure | Synthetic load for API, DB, Kafka, workflow, Dynamic Workspace widget action, and MicroFunction transaction. | Load test summary and bottleneck evidence. |
| Resilience patterns | Timeouts, bulkheads, fallback, compensation, safe stop, graceful degradation. | Resilience test report and rollback evidence. |
| Observability under stress | Trace reconstruction, metric visibility, log safety, dashboard response under load. | Grafana/Tempo/Loki/Sentry evidence snapshots where safe. |

# 18. Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop
| Loop Stage | Allowed Codex / AI Behavior | Required Human / Gate |
| --- | --- | --- |
| Detect | Analyze CI failures, logs, traces, security findings, GitNexus impact, test failures, SLO/quality signals. | Evidence must be classified and source-linked. |
| Retrieve evidence | Summarize relevant code, contracts, tests, policies, telemetry, incidents, and runbooks. | No Restricted data or secrets copied into AI context without approval. |
| Propose candidate | Draft fix, test, refactor, policy, prompt, runbook, or learning update. | Candidate remains advisory until reviewed. |
| Validate | Run deterministic tests, security scans, policy checks, architecture fitness, and regression checks. | Critical/high failures block merge. |
| Approve | Human maker-checker, CODEOWNERS, ARB/CAB as needed. | AI cannot approve its own output. |
| Promote / learn | Merge or publish reviewed artifact; update Obsidian/LLM Wiki only after approval. | Evidence, source refs, classification, rollback, improvement path. |
| Monitor | Observe result and feed lessons back into backlog, AGENTS.md, tests, runbooks, or standards. | Activity Ledger and improvement backlog updated. |

# 19. Progressive Autonomy and Full System Builder Transition
| Phase | Recommended Tool / Agent Maturity | Promotion Condition |
| --- | --- | --- |
| PoC 1 | Codex as Builder Agent only; humans and CI as checker. | Login baseline passes tests, OPA/SBAC, audit/outbox, Dynamic Workspace bootstrap, evidence. |
| PoC 1A | Add logical reviewer agents/checklists for architecture, security, QA, DB, frontend, evidence. | PoC 1 preserved; PoC 1A additive, feature-flagged, tested, human-approved. |
| PoC 2 | Formalize CI/CD Evidence, GitNexus, agent/tool registry, SBAC skills, OPA tool-action policy, evidence validator. | Reusable system factory produces evidence on every PR/MR. |
| Post-PoC 2 | Introduce governed agents with lifecycle, trust tiers, guardrails, audit, suspension, retirement. | Agent registry, certification, telemetry, incident response, kill switch, recertification. |
| Level 8 measured autonomy | Only low-risk, reversible, time-bound, policy-approved, observable actions may be delegated. | Trust evidence, OPA/SBAC approval, rollback, audit, named owner, revocation path. |

# 20. RACI and Separation of Duties
| Activity | Solutions Architect | Dev Lead | Developer | DevSecOps | Security | DBA | QA/SDET | AI Governance | Internal Audit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Define AGENTS.md baseline | A/R | C | C | C | C | C | C | C | I |
| Configure VS Code/Codex local workspace | C | A | R | C | C | I | I | C | I |
| Execute Codex generation | C | A | R | C | C | C | C | C | I |
| Review architecture/MicroFunction/Dynamic Workspace | A/R | C | C | C | C | C | C | C | I |
| Review security/OPA/SBAC/secrets | C | C | C | C | A/R | I | C | C | I |
| Review Flyway/database/outbox | C | C | C | C | C | A/R | C | I | I |
| Review tests/evidence | C | C | C | C | C | C | A/R | C | I |
| Approve PR/MR | A | A/R | C | C | C | C | C | C | I |
| Promote environment change | C | C | I | A/R | C | C | C | C | I |
| Audit evidence | C | C | I | C | C | C | C | C | A/R |

# 21. Implementation Roadmap
| Step | Action | Exit Criteria |
| --- | --- | --- |
| 1 | Confirm 09 v3.2, 39B v1.3, 39C v1.2 are available in local source register. | SOURCE_REGISTER.md updated. |
| 2 | Open approved local repository folder in VS Code. | Path and workspace evidence logged. |
| 3 | Install/enable Codex extension only after workstation and Git controls are ready. | TOOL_REGISTRY.md updated; no production credentials. |
| 4 | Create root and directory-level AGENTS.md files. | Codex pre-flight confirms rules are detected. |
| 5 | Create/update CODEOWNERS and PR/MR template. | Required reviewers and AVCI fields present. |
| 6 | Confirm CI/CD baseline. | Build/test/policy/Flyway/security/evidence gates exist or backlog with owner. |
| 7 | Execute PoC 1 pre-flight prompt. | Plan approved before modification. |
| 8 | Execute PoC 1 generation prompt in increments. | Artifacts generated, tests run, evidence drafted. |
| 9 | Review, fix, and merge PoC 1 through governed gates. | Human/CI evidence accepted. |
| 10 | Execute PoC 1A pre-flight and additive generation. | PoC 1 preserved and regression passed. |
| 11 | Prepare PoC 2 factory capabilities. | GitNexus, CI/CD Evidence Pack, registry, resilience lab readiness backlog. |
| 12 | Improve AGENTS.md, prompt standards, tests, runbooks, and source documents based on lessons learned. | Improvement backlog and revision-control entries created. |

# 22. Acceptance Criteria and Definition of Done

Repository root and directory-level AGENTS.md files exist, are version-controlled, and are detected by Codex pre-flight.

Codex executes only inside approved local folder and feature branches linked to intake/ticket records.

No production credentials are available to Codex, ChatGPT prompts, local logs, screenshots, generated code, tests, docs, Obsidian, LLM Wiki, or GitNexus reports.

CODEOWNERS, PR/MR template, branch protection, evidence register, Activity Ledger, and CI/CD readiness are in place before PoC generation prompts.

CI validates build, tests, OPA/Rego, Flyway, OpenAPI/AsyncAPI where applicable, security scans, architecture fitness, and evidence manifest.

GitNexus is used only as read-only derivative impact evidence and never as authority or execution path.

Dynamic Workspace outputs remain backend-governed, policy-filtered, MicroFunction-backed, observable, accessible, and reversible.

MicroFunction outputs preserve configuration-first assembly, ports/adapters, idempotency, outbox/audit, safe responses, and observability evidence.

Authenticated DAST uses only approved non-prod synthetic accounts and scope.

Runtime telemetry toggles are governed, audited, time-bound, safe by default, and do not disable mandatory audit/evidence for protected actions.

Auto-Heal, Auto-Learn, and Auto-Improve create candidates and evidence only; human approval remains mandatory before merge, activation, or promotion.

Lessons learned update AGENTS.md, prompt standards, source docs, tests, runbooks, and improvement backlog.

# 23. Open Issues and AVCI Reconciliation Items
| Item | Issue | Severity | Recommended Resolution |
| --- | --- | --- | --- |
| 39A-OI-001 | Exact Codex extension/plugin configuration syntax may vary by installed version, workspace policy, or plan availability. | Medium | Treat this document as control intent; maintain local tool-specific setup notes and update when tool UI/API changes. |
| 39A-OI-002 | Full AIRA System Builder registry and runtime control plane are not yet implemented before PoC 1. | Medium | Use System Builder Lite for PoC 1/1A and implement registry/control-plane capabilities in PoC 2 and agent governance workstream. |
| 39A-OI-003 | MCP/connectors can quickly expand tool authority beyond approved scope. | High | Keep disabled by default; allow only reviewed, registered, least-privilege, auditable, OPA/SBAC-governed, reversible tool actions. |
| 39A-OI-004 | Developers may paste prompts without pre-flight review. | High | Make pre-flight prompt, Activity Ledger entry, branch-only execution, and reviewer plan mandatory in team procedure. |
| 39A-OI-005 | Runtime telemetry toggles can be misused to hide errors or disable useful evidence. | High | Permit performance-sensitive toggles only through approved runtime config; audit all changes; never disable protected-action audit/evidence. |
| 39A-OI-006 | Dynamic Workspace UI generation may drift into frontend authority if not checked. | High | Block generated UI that invents endpoints, bypasses OPA/SBAC, or handles business authorization client-side. |
| 39A-OI-007 | Heavy transaction/resilience tests may be deferred because they slow early development. | Medium | Create Resilience Lab backlog and require idempotency/outbox/DLQ/replay tests before integration scale. |
| 39A-OI-008 | Known source numbering overlap remains across 11A, 41B/44, older source references, and active-source deduplication. | Medium | Track through canonical registers and 00D/Revision Control; do not silently normalize without governed register decision. |

# 24. AVCI Compliance Summary
| AVCI Property | Compliance Evidence in This Guide |
| --- | --- |
| Attributable | Defines owner, co-owners, primary parents, companion sources, logical agent roles, RACI, branch ownership, PR/MR accountability, Activity Ledger, and evidence path. |
| Verifiable | Requires pre-flight review, CI/CD gates, OPA/Rego tests, Flyway tests, contract checks, DAST/SAST/SCA/secret scans, architecture fitness, GitNexus impact evidence, and PR/MR evidence packs. |
| Classifiable | Requires classification-aware prompts, code, logs, traces, screenshots, generated files, Dynamic Workspace outputs, telemetry, evidence, Obsidian/LLM Wiki projections, and tool outputs. |
| Improvable | Provides implementation roadmap, open issues, lessons-learned loop, AGENTS.md updates, prompt improvement, test/runbook updates, source-register updates, and transition path to full System Builder. |

# Appendix A. Copy-Ready Root AGENTS.md Baseline
| # AIRA Repository Agent Instructions You are operating inside the AIRA AI-Native Enterprise Platform repository. You are a branch-bound Builder Agent, not an approver, deployer, security authority, DBA authority, CAB authority, or production operator. Mandatory rules: 1. Read this file and any nested AGENTS.md before changing files. 2. Work only on the current feature branch. Never commit or merge to main directly. 3. Do not access, request, write, infer, or expose production credentials, tokens, secrets, raw JWTs, passwords, customer data, or Restricted data. 4. Preserve SOLID, Clean Architecture, DDD, ports/adapters, MicroFunction boundaries, Dynamic Workspace backend authority, OPA/SBAC, Flyway-only migrations, observability, rollbackability, and AVCI evidence. 5. Do not call model providers directly from application code. AI/model traffic must use approved AIRA gateway/LiteLLM routes and guardrails. 6. Do not hardcode authorization in controllers, services, frontend, or database scripts. Use OPA/SBAC policy and tests. 7. Do not create manual DDL or uncontrolled schema files. Use Flyway migrations and DBA-reviewed evidence. 8. Do not invent endpoints, topics, schemas, step codes, table names, or configuration keys when canonical contracts exist. 9. Before large changes, return a pre-flight plan and stop for human approval. 10. Every output must include tests, evidence, known limitations, rollback or safe-disable path, and PR/MR AVCI summary. |
| --- |

# Appendix B. Copy-Ready Codex Pre-Flight Prompt
| You are acting as AIRA System Builder Lite / branch-bound Codex Builder Agent. Before modifying any file: 1. Read the root AGENTS.md and all nested AGENTS.md files relevant to the requested change. 2. Identify the governing AIRA sources and the affected bounded context. 3. Identify affected contracts: OpenAPI, AsyncAPI, Avro/JSON Schema, CloudEvents, Flyway, OPA/SBAC, MicroFunction configuration, Dynamic Workspace configuration, tests, and evidence. 4. List files that must not be destructively changed. 5. Propose the minimum safe implementation plan. 6. Identify tests, security checks, policy checks, architecture fitness checks, observability evidence, and rollback/safe-disable path. 7. Identify required human reviewers: architecture, security, DBA, QA/SDET, frontend, DevSecOps, AI governance, product owner, or CAB/ARB if applicable. 8. Identify risks, assumptions, and open questions. 9. Stop after the plan and wait for approval. Do not generate code yet. Do not run commands. Do not modify files. |
| --- |

# Appendix C. PR/MR Evidence Summary Template
| ## AIRA PR/MR AVCI and System Builder Lite Evidence Summary ### Attributable - Ticket / Intake ID: - Owner / Developer: - Checker(s): - Branch: - Commit(s): - AI tools used: - Prompt standard used: - AGENTS.md files applied: ### Verifiable - Backend build/tests: - Frontend build/tests: - OPA/Rego policy tests: - Flyway clean/upgrade validation: - OpenAPI/AsyncAPI/schema validation: - Security scans: SAST / SCA / secret scan / DAST: - Architecture fitness results: - GitNexus impact report: - Evidence manifest path: ### Classifiable - Data classification: - Secrets/PII handling: - Prompt/log/screenshot redaction: - Runtime telemetry fields reviewed: - Evidence retention path: ### Improvable - Known limitations: - Risks accepted or waived: - Follow-up backlog: - AGENTS.md or prompt improvements: - Runbook / test / source documentation updates: ### Reversibility - Rollback / forward-fix / compensation / safe-disable plan: - Feature flags or runtime toggles changed: - Validation after rollback or disablement: |
| --- |
| Final Operating Rule Codex may build. CI must verify. GitNexus may inform. Humans must approve. AIRA evidence must prove. System Builder Lite must never silently mutate production, weaken controls, or replace accountable engineering discipline. |
| --- |

