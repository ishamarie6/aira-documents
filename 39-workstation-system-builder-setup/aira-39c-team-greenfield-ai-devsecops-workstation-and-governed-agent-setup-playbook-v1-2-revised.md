---
title: "Team Greenfield AI DevSecOps Workstation and Governed Agent Setup Playbook"
doc_id: "AIRA-39C"
version: "v1.2"
status: "revised"
category: "Workstation and system builder setup"
source_docx: "AIRA_39C_Team_Greenfield_AI_DevSecOps_Workstation_and_Governed_Agent_Setup_Playbook_v1.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 39-workstation-system-builder-setup
  - revised
  - aira-39c
---



# Team Greenfield AI DevSecOps Workstation and Governed Agent Setup Playbook



AIRA

AI-Native Enterprise Platform

AIRA Team Greenfield AI DevSecOps Workstation and Governed Agent Setup Playbook

v1.2 Revised

Team Rollout - Governed Agent Sandbox - Activity Ledger - System Builder Lite - Dynamic Workspace - MicroFunction Runtime - Evidence by Construction
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-039C |
| Canonical Filename | AIRA_39C_Team_Greenfield_AI_DevSecOps_Workstation_and_Governed_Agent_Setup_Playbook_v1.2_Revised.docx |
| Version | v1.2 - 09 v3.2, 39B v1.3, Dynamic Workspace, MicroFunction Runtime, DevSecOps Evidence, Agent Registry, Threat Model, and Progressive Autonomy Alignment Update |
| Supersedes | 39C-AIRA_Team_Greenfield_AI_DevSecOps_Workstation_and_Governed_Agent_Setup_Playbook_v1.1.docx |
| Status | Draft for Architecture, DevSecOps, Security, Platform Engineering, QA/SDET, AI Governance, DBA, SRE, Internal Audit, and Controlled Team Rollout Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; DevSecOps Lead; Software Development Lead; Security Architecture; Platform Engineering; QA/SDET; DBA; SRE / Operations; AI Governance; Knowledge Governance; Internal Audit |
| Primary Audience | Software Development Team; System Builder operators; Windows 11 workstation builders; VS Code Codex users; Hermes Agent operators; AI agent owners; architects; security; QA/SDET; DevSecOps; AI Engineering; reviewers |
| Primary Parents | 09-AIRA Greenfield Environment Standard v3.2 Revised; 39B-AIRA Greenfield AI DevSecOps Workstation Setup and System Builder Lite Implementation Guide v1.3 Revised |
| Companion Sources | 07 Skills Framework; 07B Team Transformation; 39/39A Workspace/Codex Guides; 10 MicroFunction; 11 DevSecOps; 12A/41/46-61 Dynamic Workspace; 15 API; 16 Flyway/Database; 17 Security; 19 GitNexus; 20 CI/CD Evidence; 31/31A Observability; 42D-42S Agent Governance; 43 Continuous Improvement; 42C Foundation PoC Roadmap |
| Effective Date | Upon Architecture Review Board / CAB / Security Governance / DevSecOps Governance / AI Governance approval |
| Review Cadence | Before first team rollout; after first three workstations; before first governed agent sandbox; quarterly; and on material toolchain, AI, security, Dynamic Workspace, MicroFunction, CI/CD, or observability change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Team-Greenfield-Workstation-Governed-Agent-Setup / v1.2 / |
| Generated | 2026-06-17 11:32 |
| Mandatory Practice Statement This playbook is not a team tool-installation checklist and not an authorization for uncontrolled agents. It is the controlled, repeatable rollout model for AIRA AI DevSecOps workstations, System Builder Lite usage, and governed agent sandbox preparation. From Day 0, every meaningful activity involving ChatGPT, Codex, Hermes Agent, manual commands, Git, Obsidian, LLM Wiki, LiteLLM, OpenRouter, NeMo Guardrails, DevSecOps tools, Dynamic Workspace artifacts, MicroFunction runtime artifacts, or AI agents must be logged with owner, purpose, source, classification, evidence, result, risk, and improvement path. AI may guide, recommend, draft, generate, analyze, test, and propose. AI must not approve, merge, deploy, disable controls, access production credentials, mutate production, bypass OPA/SBAC/Harness, or become business authority. |
| --- |

One Team Baseline - One Activity Ledger Model - One Evidence Discipline - No Shadow Agents - AVCI Always

# Static Table of Contents

1. Executive Summary

2. v1.2 Update Verdict and Change Summary

3. Purpose, Scope, and Authority

4. Source Basis, Supersedence, and Reconciliation Position

5. Team Rollout Control Model

6. Central Logging and Activity Ledger Governance Model

7. Team Roles, Cohorts, and Readiness Dashboard

8. Master Sequence and Tool Responsibility Matrix

9. Phase 0 - Team Rollout Authorization and Register Setup

10. Phase 1 - Day 0 Activity Ledger and Evidence Register

11. Phase 2 - Secure Windows 11 Baseline by Team Member

12. Phase 3 - ChatGPT Project Source Registration and Prompt Discipline

13. Phase 4 - Core Tool Installation and Version Evidence

14. Phase 5 - Repository Bootstrap, Branch Rules, and PR/MR Evidence

15. Phase 6 - VS Code, Codex, and System Builder Lite Team Controls

16. Phase 7 - Obsidian, LLM Wiki, and Knowledge Projection Readiness

17. Phase 8 - DevSecOps Pipeline, GitNexus, and Evidence Pack Readiness

18. Phase 9 - Dynamic Workspace and Frontend Team Readiness

19. Phase 10 - MicroFunction Backend Runtime Team Readiness

20. Phase 11 - API, Eventing, Kafka, Avro, CloudEvents, Outbox, DLQ, and Replay Readiness

21. Phase 12 - Observability, Audit, Runtime Toggle, and Dashboard Readiness

22. Phase 13 - Security, OPA/SBAC, Abuse Cases, Authenticated DAST, Secure APIs, and Secrets Hygiene

23. Phase 14 - Concurrency, Heavy Transaction, Idempotency, and Resilience Lab Readiness

24. Phase 15 - Governed Agent Sandbox, Hermes, LiteLLM, Guardrails, and Harness Readiness

25. Phase 16 - Agent Registry, Threat Model, Certification, and Promotion Gate

26. Phase 17 - Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop Readiness

27. Phase 18 - Team Dry Run PR/MR and Ready-to-Proceed Gate

28. Governed Agent Inventory Starter Matrix

29. RACI and Separation of Duties

30. Acceptance Criteria and Definition of Done

31. Risk and Control Register

32. Cross-Document Reconciliation and Future Regeneration Candidates

33. AVCI Compliance Summary

Appendix A - Copy-Ready Team Activity Ledger Template

Appendix B - Copy-Ready Team Readiness Dashboard

Appendix C - Copy-Ready Agent Identity Card Template

Appendix D - Copy-Ready Agent Sandbox Checklist

Appendix E - Copy-Ready Team Rollout Command Evidence Baseline

Appendix F - Copy-Ready PR/MR Team Readiness Evidence Template

# 1. Executive Summary

This v1.2 revision updates AIRA-DOC-039C from a Day 0 logging and team setup playbook into a full team rollout and governed agent setup baseline aligned with 09 v3.2 and 39B v1.3. The prior v1.1 playbook correctly made the AIRA Activity Ledger mandatory, defined interim Day 0 logging, connected Obsidian Git-backed central logs, and introduced tool-specific ChatGPT/Codex/Hermes logging rules. This revision preserves those controls and expands the playbook to cover team-level readiness for Dynamic Workspace, MicroFunction runtime, DevSecOps evidence, API/eventing, observability, security, resilience, agent registry, threat modeling, and progressive autonomy.

The team must not scale AIRA development by giving every developer independent tool choices, independent AI practices, unmanaged Obsidian vaults, separate prompt rules, or uncontrolled agents. The AIRA team scales through a shared governed baseline: one source authority model, one workstation readiness standard, one activity ledger model, one repository evidence model, one agent registry path, one policy and guardrail boundary, and one maker-checker approval discipline.

This document converts the single-workstation 39B execution guide into a team rollout playbook. It defines cohorts, readiness dashboards, team evidence, agent identity cards, sandbox boundaries, acceptance gates, and non-negotiable rejection rules before the team proceeds to Login PoC 1, PoC 1A, PoC 2, Dynamic Workspace, and broader AIRA foundation development.
| Strategic Outcome | v1.2 Required Result |
| --- | --- |
| Repeatable team setup | Every workstation follows the same 09/39B baseline, tool registry, source register, activity ledger, validation steps, and evidence pack. |
| Controlled AI tool usage | ChatGPT guides, Codex drafts in governed branches, Hermes is introduced later in sandbox, and agents remain registry-bound, SBAC-limited, OPA-gated, and human-accountable. |
| Shared evidence discipline | All setup actions, AI usage, agent activity, commands, tests, scans, prompts, tool changes, and readiness gates are logged from Day 0. |
| Foundation development readiness | The team can prove readiness for DevSecOps, Dynamic Workspace, MicroFunctions, API/eventing, observability, security, resilience, and AI governance before business feature volume increases. |
| Progressive autonomy only | Agents advance from advisory to read-only to candidate generation only when evidence, trust, skill, guardrails, rollback, and human approval support it. |

# 2. v1.2 Update Verdict and Change Summary

Revision verdict: update 39C after 39B. Document 39B now defines the individual workstation setup. Document 39C must now govern the team rollout and early agent sandbox so that each developer does not interpret 39B differently, and no agent is created outside registry, threat-model, SBAC, OPA, guardrail, telemetry, and evidence controls.
| Update Area | v1.2 Improvement |
| --- | --- |
| 39B v1.3 inheritance | Converts single-workstation setup into team rollout, cohort tracking, readiness dashboard, and setup completion evidence. |
| 09 v3.2 inheritance | Adds environment readiness criteria for Dynamic Workspace, MicroFunction runtime, DevSecOps gates, observability, security, resilience, runtime toggles, and improvement loops. |
| Activity Ledger hardening | Retains Day 0 logging and adds team-level activity IDs, workstation IDs, agent IDs, evidence references, and readiness status. |
| Governed agent setup | Adds agent inventory, agent identity card, sandbox rules, threat model, autonomy tier, tool manifest, LiteLLM route, guardrails, SBAC, OPA, telemetry, kill switch, and certification preconditions. |
| Dynamic Workspace readiness | Adds frontend team controls for generated clients, component registry, accessibility, Playwright, visual regression, policy denial tests, and backend-governed workspace assembly. |
| MicroFunction readiness | Adds backend team controls for Java 25 target, ports/adapters, Flyway, OPA, audit/outbox, idempotency, Testcontainers, and architecture fitness. |
| DevSecOps/GitNexus | Adds team gate for CI/CD, GitNexus read-only analysis, SAST/SCA/DAST, SBOM, provenance, secrets scan, evidence pack, and PR/MR AVCI summaries. |
| Observability and toggles | Adds Log4j2, OpenTelemetry, Sentry, Loki, Tempo, Grafana, trace reconstruction, audit minimums, diagnostic toggles, and runtime sampling controls. |
| Resilience lab | Adds team readiness for retry-safe, duplicate-safe, concurrent, heavy-load, failure-aware transaction behavior. |

# 3. Purpose, Scope, and Authority

## 3.1 Purpose

Define the official team execution procedure for greenfield AIRA workstation setup and governed agent sandbox readiness.

Ensure every developer, reviewer, QA/SDET, DevSecOps engineer, security reviewer, and agent owner follows one repeatable setup and evidence model.

Make the AIRA Activity Ledger, Evidence Register, Source Register, Tool Registry, Agent Register, and Readiness Dashboard mandatory before broad development.

Clarify how ChatGPT, Codex, Hermes Agent, Obsidian, Git, LLM Wiki, LiteLLM, OpenRouter, NeMo Guardrails, GitNexus, OPA/SBAC, and DevSecOps tools are used without uncontrolled automation.

Prepare the team for governed Login PoC 1, PoC 1A, PoC 2, Dynamic Workspace, MicroFunction runtime, API/eventing, observability, security, resilience, and AI agent development.

## 3.2 Scope
| In Scope | Out of Scope |
| --- | --- |
| Team rollout authorization, cohort setup, workstation readiness, source registration, activity ledger, evidence register, tool registry, agent inventory, VS Code/Codex setup, Obsidian/LLM Wiki readiness, repository governance, DevSecOps evidence, Dynamic Workspace readiness, MicroFunction readiness, API/eventing readiness, observability, security, resilience lab, and governed agent sandbox. | Production deployment, production credentials, direct production database access, direct Kubernetes access, unrestricted agent execution, unrestricted MCP/tool expansion, CAB/ARB bypass, direct model-provider calls from application code, unapproved personal AI accounts, raw production data in prompts or Obsidian. |
| Team-level activity logging, templates, acceptance criteria, RACI, risk controls, and dry-run PR/MR evidence. | Full production System Builder runtime, Level 8 autonomy activation, active production agent execution, and production data processing without formally approved controls. |

## 3.3 Authority and Precedence
| Level | Authority | Role |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance / AI Governance | Final authority for production-impacting controls, major architecture decisions, exceptions, and autonomy delegation. |
| L1 | AIRA AVCI, Enterprise Architecture, AI Governance, Security, DevSecOps, Database, MicroFunction, Change Governance standards | Universal quality, evidence, architecture, security, testability, rollback, policy, and improvement discipline. |
| L2 | 09 v3.2, 39B v1.3, 39A, and this 39C v1.2 playbook | Greenfield environment, workstation setup, System Builder Lite, and team rollout execution authority. |
| L3 | AGENTS.md, CODEOWNERS, PR/MR templates, CI/CD, OPA, Flyway, Activity Ledger, Evidence Register, Agent Registry | Execution-level enforcement and evidence capture. |
| L4 | Feature branches, activity records, test results, scan evidence, prompt summaries, review records | Implementation proof and continuous improvement input. |
| Conflict Rule Where documents appear inconsistent, apply the stricter AIRA control temporarily, log the issue as an AVCI reconciliation item, assign an owner, and resolve through governed review. Do not silently select the easiest interpretation. |
| --- |

# 4. Source Basis, Supersedence, and Reconciliation Position

This playbook is based on the current AIRA greenfield, System Builder Lite, team transformation, knowledge governance, AI governance, agent governance, and PoC standards. It assumes active AIRA source baseline is available through ChatGPT Project Sources, approved repositories, or the governed knowledge baseline. It supersedes 39C v1.1 for team rollout execution while preserving the v1.1 Day 0 Activity Ledger discipline.
| Source / Companion | v1.2 Treatment |
| --- | --- |
| 39C v1.1 | Preserved as source baseline for Day 0 logging, Activity Ledger, central Obsidian logging, and ChatGPT/Codex/Hermes logging rules. |
| 09 v3.2 | Controls greenfield environment readiness and the rule that installed tools are insufficient without build, test, security, observability, evidence, rollback, and improvement proof. |
| 39B v1.3 | Controls individual workstation setup sequence and command/evidence discipline that this 39C scales to the team. |
| 07 / 07B | Controls skills, proficiency evidence, SBAC, trust scoring, maturity path, delegation limits, and progressive autonomy. |
| 10 / 10A / 10B / 10D / 10E | Controls MicroFunction design, runtime assembly, standard steps, backend generation, idempotency, ports/adapters, and evidence. |
| 12A / 41 / 46-61 | Controls Dynamic Workspace frontend, configuration, API, security, testing, observability, DevSecOps, UX, and Admin Builder governance. |
| 15 / 15A | Controls OpenAPI, AsyncAPI, Kafka, Avro, CloudEvents, schema evolution, idempotency, DLQ, replay, and contract-first implementation. |
| 16 / 16A / 16B | Controls Flyway-only database creation, migration, seed, RLS, outbox, schema ownership, and migration evidence. |
| 17 / 17A / 32 | Controls security, identity, secrets, RBAC/ABAC/SBAC, OPA, least privilege, and access governance. |
| 19 / 20 / 31 / 31A | Controls GitNexus read-only analysis, CI/CD evidence pack, SRE/operations, observability, trace correlation, dashboards, and evidence. |
| 42D-42S | Controls agent identity, runtime security, autonomy, threat model, tool/MCP gateway, memory/RAG, red team certification, incidents, registry, API/Flyway, dashboards, UAT, and roadmap. |
| 43 | Controls Auto-Heal, Auto-Learn, and Auto-Improve as proposal-driven candidate loops. |

# 5. Team Rollout Control Model

The team rollout model prevents workstation drift and agent sprawl. Each developer workstation is a controlled node with a named owner, toolchain evidence, source access evidence, AI-use acknowledgement, repository branch boundary, knowledge projection boundary, and readiness status. Each agent is a controlled artifact with identity, owner, purpose, non-goals, SBAC scope, OPA policy, allowed tools, model route, guardrails, evidence path, threat model, certification state, and decommission path.
| Control Plane | Mandatory Treatment |
| --- | --- |
| Team Register | Every participant has role, workstation ID, approved tools, skill profile, access scope, and reviewer assignment. |
| Workstation Evidence | Each workstation has baseline evidence: OS security, tools, versions, repository clone, Codex boundary, Obsidian vault, and local validation. |
| Activity Ledger | Every meaningful setup, AI, command, prompt, test, scan, decision, and exception is logged from Day 0. |
| Source Register | Every referenced AIRA document has document ID, version, status, classification, source path, retrieval eligibility, and supersedence state. |
| Tool Registry | Every installed or enabled tool has owner, source, version, install method, approval, license, risk, and evidence. |
| Agent Register | Every proposed or active agent has identity card, owner, SBAC scope, autonomy tier, model route, tool grants, guardrails, telemetry, and kill switch. |
| Readiness Dashboard | Team lead tracks each person and agent through phases with evidence links and blocker status. |

# 6. Central Logging and Activity Ledger Governance Model

The AIRA Activity Ledger is the controlled daily record of setup, engineering, agent, and evidence activity. It is not a replacement for Git, CI/CD, ticketing, observability, audit logs, or OpenKM. It connects them with a human-readable, evidence-linked narrative that can be reviewed, corrected, approved, and later projected into Obsidian or LLM Wiki after classification review.
| Record Layer | Purpose | System of Record / Storage |
| --- | --- | --- |
| L0 Raw Evidence | Screenshots, command outputs, install logs, test reports, scan results, Git diffs, CI logs. | Evidence folder, Git, CI/CD artifacts, observability tools, OpenKM. |
| L1 Activity Record | Human-readable record of what happened, who did it, what tool was used, and what evidence exists. | Interim Markdown folder, then Git-backed Obsidian. |
| L2 Registers | Structured indexes for activities, evidence, sources, agents, decisions, issues, and improvements. | Obsidian registers under 00-Registers and Git repository where applicable. |
| L3 Decisions and Lessons | Approved decisions, lessons learned, corrections, repeatable procedures. | Obsidian reviewed folders, ADR/TDL where material. |
| L4 Approved Knowledge | Validated summaries and runbooks safe for team reuse. | Obsidian active folders with review metadata. |
| L5 Retrieval Layer | Search and AI retrieval over approved, current, classification-eligible knowledge. | LLM Wiki/LightRAG/pgvector through governed retrieval gateway. |
| Telemetry Safety Rule Never log passwords, raw JWTs, refresh tokens, secrets, private keys, production credentials, raw Restricted data, raw customer files, sensitive screenshots, or prompts containing confidential business data. Store secrets only in approved password manager or vault references. |
| --- |

# 7. Team Roles, Cohorts, and Readiness Dashboard

Team rollout must be performed in controlled cohorts. A pilot cohort validates the procedure, a checker cohort independently verifies the evidence, and the broader development cohort proceeds only after the setup pattern is accepted. Each team member must have a named checker. A developer cannot approve the readiness of their own workstation or agent.
| Role | Primary Responsibility | Cannot Do |
| --- | --- | --- |
| IT Head / Solutions Architecture | Own rollout direction, approve baseline interpretation, resolve escalations. | Bypass evidence or maker-checker review. |
| DevSecOps Lead | Own repository controls, CI/CD, scanner setup, evidence pack, GitNexus readiness. | Disable gates to accelerate setup. |
| Software Development Lead | Own developer sequencing, branch discipline, PoC readiness, code quality expectations. | Accept feature code before foundation readiness. |
| Security Architecture | Own OPA/SBAC, secrets hygiene, abuse cases, DAST, agent threat model. | Approve unsafe tool or model routes without evidence. |
| QA/SDET | Own deterministic tests, Playwright, Testcontainers, resilience tests, readiness evidence. | Accept demo-only evidence. |
| Knowledge Governance | Own Obsidian, LLM Wiki, source register, projection metadata, retrieval eligibility. | Treat AI summaries as source of truth. |
| Agent Owner | Own one or more agent identity cards, non-goals, risk tier, controls, evaluation, retirement. | Grant tools or autonomy without registry, OPA, and approval. |
| Developer | Execute setup, log evidence, use Codex within branch, build/test/scan. | Use personal AI tools, commit secrets, bypass PR/MR, or create shadow agents. |

# 8. Master Sequence and Tool Responsibility Matrix
| Phase | Primary Tool / Actor | Main Output | Gate |
| --- | --- | --- | --- |
| 0 | IT Head / Team Lead | Team rollout authorization and register skeleton. | Named owner, checker, evidence path. |
| 1 | Human + Obsidian/Git | Activity Ledger and evidence register. | Logging exists before broad setup. |
| 2 | Human / Admin | Secure Windows baseline. | Security evidence captured. |
| 3 | ChatGPT Project | Source registration and prompt discipline. | Active source context and no secret exposure. |
| 4 | Human CLI | Approved tools and versions. | Tool registry complete. |
| 5 | Git / Repo Platform | Branch rules, CODEOWNERS, PR template, AGENTS.md. | Repository governance PR/MR. |
| 6 | VS Code + Codex | Constrained AI-assisted development. | Codex respects AGENTS.md and branch boundary. |
| 7 | Obsidian / LLM Wiki | Central knowledge projection. | Metadata, classification, freshness. |
| 8 | CI/CD + GitNexus | Pipeline, scans, evidence, impact analysis. | Evidence pack created. |
| 9-14 | Frontend, backend, API, observability, security, resilience tools | Foundation technical readiness. | Dry-run tests pass or blockers recorded. |
| 15-16 | Hermes / LiteLLM / Guardrails / Agent Registry | Governed agent sandbox readiness. | Agent identity, threat model, SBAC, OPA, certification gate. |
| 17-18 | Team + CI/CD + Reviewers | Improvement loop and dry-run PR/MR. | Ready-to-proceed decision. |

# 9. Phase 0 - Team Rollout Authorization and Register Setup
| Field | Required Content |
| --- | --- |
| Primary Owner / Execution Surface | IT Head / Solutions Architecture / Team Lead |
| Objective | Authorize controlled rollout and create the team-level registers before individual setup proceeds. |
| Exit Gate | Proceed only when team ownership, checker assignment, evidence path, and register skeletons exist. |
| Minimum Evidence | Rollout authorization; team register; candidate agent register; readiness dashboard; RACI record. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 0.1 | Confirm this 39C v1.2 playbook is the active rollout instruction. | Rollout authorization entry. |
| 0.2 | Assign rollout owner, cohort lead, checker, security reviewer, DevSecOps reviewer, QA reviewer, and knowledge steward. | RACI assignment. |
| 0.3 | Create TEAM_REGISTER.md with team member, role, workstation_id, approved tools, skill profile, and checker. | Team register. |
| 0.4 | Create AGENT_CANDIDATE_REGISTER.md for proposed agents only; no active agent yet. | Candidate register. |
| 0.5 | Create READINESS_DASHBOARD.md with phase status per workstation and per agent candidate. | Dashboard initialized. |

# 10. Phase 1 - Day 0 Activity Ledger and Evidence Register
| Field | Required Content |
| --- | --- |
| Primary Owner / Execution Surface | Human Developer + Knowledge Steward |
| Objective | Ensure evidence capture starts before broad installation, agent activity, or feature work. |
| Exit Gate | Proceed only when each participant can log setup actions and evidence without exposing secrets or sensitive data. |
| Minimum Evidence | Activity ledger; evidence register; first entry; handling rules. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 1.1 | Create local Activity Ledger folder and daily ledger file for each team member. | ACTIVITY_LEDGER-YYYY-MM-DD.md. |
| 1.2 | Create EVIDENCE_REGISTER.md with evidence_id, phase, owner, workstation_id, source_ref, path, hash, validation, classification. | Evidence register. |
| 1.3 | Define activity ID pattern: AIRA-ACT-YYYYMMDD-WKSxx-NNN and agent activity ID pattern: AIRA-AGT-ACT-YYYYMMDD-AGTxx-NNN. | ID convention. |
| 1.4 | Define evidence storage path and redaction rules. | Evidence path and handling note. |
| 1.5 | Log this setup start with ChatGPT/Codex/Hermes usage boundaries. | First ledger entry. |

# 11. Phase 2 - Secure Windows 11 Baseline by Team Member
| Field | Required Content |
| --- | --- |
| Primary Owner / Execution Surface | Human Developer / System Administrator / Security |
| Objective | Apply the workstation security baseline consistently across the team. |
| Exit Gate | Proceed only when each workstation has documented security posture and no uncontrolled local storage of secrets or production data. |
| Minimum Evidence | System info; security screenshot; patch status; folder tree; exceptions. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 2.1 | Confirm Windows 11 edition, patch status, device owner, local admin model, endpoint protection, firewall, disk encryption, and corporate Wi-Fi/network policy. | Security baseline evidence. |
| 2.2 | Install approved browser and password manager; prohibit secrets in prompts, markdown, screenshots, .env, or repository files. | Secrets hygiene acknowledgement. |
| 2.3 | Configure local folders under D:\ChatGPT Workspace unless approved otherwise. | Folder tree evidence. |
| 2.4 | Capture system info and patch evidence. | Evidence files. |
| 2.5 | Open security exceptions only through ticket/approval path. | Exception record if applicable. |

# 12. Phase 3 - ChatGPT Project Source Registration and Prompt Discipline
| Field | Required Content |
| --- | --- |
| Primary Owner / Execution Surface | ChatGPT Project + Human Operator |
| Objective | Use ChatGPT Project as governed advisory surface and not as installer, credential holder, or approver. |
| Exit Gate | Proceed only when ChatGPT is bound to advisory, source-cited, classification-aware, and evidence-linked use. |
| Minimum Evidence | Source register; prompt summary; classification notes; ledger entries. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 3.1 | Confirm active AIRA source packs and latest revised 09, 39B, and 39C are available. | Source register update. |
| 3.2 | Record which prompts are used for setup, review, and document generation. | Prompt evidence summary. |
| 3.3 | Classify every prompt input before use; do not paste secrets, raw production data, or Restricted records. | Classification note. |
| 3.4 | Ask ChatGPT to produce sequencing guidance only; humans execute privileged actions. | AI boundary record. |
| 3.5 | Log all material ChatGPT outputs in Activity Ledger as advisory unless approved. | Ledger entries. |

# 13. Phase 4 - Core Tool Installation and Version Evidence
| Field | Required Content |
| --- | --- |
| Primary Owner / Execution Surface | Human CLI + Team Checker |
| Objective | Install and validate approved tools consistently across the team using 39B commands and evidence patterns. |
| Exit Gate | Proceed only when tool evidence is complete and comparable across the team. |
| Minimum Evidence | Tool registry; version evidence; checker sign-off. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 4.1 | Validate package IDs before install. | winget search evidence. |
| 4.2 | Install Git, GitHub/GitLab CLI, VS Code, Java 25 target baseline, Maven/Gradle, Node, pnpm/npm, Flyway, OPA, gitleaks, Trivy, Syft, Cosign, Semgrep, and approved equivalents. | Tool versions. |
| 4.3 | Record install source, version, owner, license, approval, and evidence in TOOL_REGISTRY.md. | Tool registry entries. |
| 4.4 | Reject unmanaged plugins, personal AI accounts, unapproved MCP servers, and unapproved agent packages. | Non-conformance check. |
| 4.5 | Checker validates each workstation evidence before Codex is enabled. | Checker sign-off. |

# 14. Phase 5 - Repository Bootstrap, Branch Rules, and PR/MR Evidence
| Field | Required Content |
| --- | --- |
| Primary Owner / Execution Surface | DevSecOps Lead + Repository Admin + Developer |
| Objective | Ensure every team member works only in governed repositories and branches. |
| Exit Gate | Proceed only when repository governance is proven through a PR/MR and human review. |
| Minimum Evidence | Repo controls; AGENTS.md; governance PR/MR; GitNexus boundary record. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 5.1 | Clone approved repository into controlled local folder. | Clone and remote evidence. |
| 5.2 | Verify branch protection, CODEOWNERS, PR/MR template, issue templates, labels, and commit/approval rules. | Repo control evidence. |
| 5.3 | Create or update AGENTS.md, docs/aira-source-register.md, docs/aira-evidence-register.md, docs/aira-tool-registry.md. | Governance files. |
| 5.4 | Open a governance-only PR/MR for setup evidence before feature code. | PR/MR evidence. |
| 5.5 | GitNexus remains read-only and derivative; no commit, approve, merge, deploy, or production mutation authority. | GitNexus boundary record. |

# 15. Phase 6 - VS Code, Codex, and System Builder Lite Team Controls
| Field | Required Content |
| --- | --- |
| Primary Owner / Execution Surface | VS Code + Codex + Human Reviewer |
| Objective | Enable Codex only in governed repositories with explicit boundaries, AGENTS.md, and activity evidence. |
| Exit Gate | Proceed only when Codex demonstrates compliance with AGENTS.md, branch boundaries, tests, evidence, and human review. |
| Minimum Evidence | Extension list; Codex boundary summary; dry-run PR/MR. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 6.1 | Open only the governed repository folder in VS Code. | Workspace evidence. |
| 6.2 | Install only approved extensions and record extension list. | Extension evidence. |
| 6.3 | Configure Codex as candidate generator and reviewer assistant only; no merge, approval, deployment, secret, or production authority. | Codex boundary evidence. |
| 6.4 | Require Codex to read AGENTS.md and summarize restrictions before changes. | Codex restriction summary. |
| 6.5 | Run a documentation-only or validation-only test change before feature generation. | Dry-run branch/PR evidence. |

# 16. Phase 7 - Obsidian, LLM Wiki, and Knowledge Projection Readiness
| Field | Required Content |
| --- | --- |
| Primary Owner / Execution Surface | Knowledge Governance + Developer + AI Assistant |
| Objective | Create the central knowledge projection without treating local notes or AI summaries as stronger authority than Tier-0 sources. |
| Exit Gate | Proceed only when knowledge artifacts are classified, current, source-linked, reviewable, and retrieval-eligible by policy. |
| Minimum Evidence | Vault commit/hash; metadata; source/freshness register; indexing readiness. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 7.1 | Create Git-backed Obsidian vault structure for active baseline, candidates, evidence, ADR/TDL, runbooks, prompts, registers, superseded, quarantine. | Vault evidence. |
| 7.2 | Apply mandatory YAML metadata: document_id, version, status, owner, classification, source_tier, source_hash, retrieval_eligible, evidence_ref. | Metadata template. |
| 7.3 | Do not copy full source code into Obsidian; use Git/GitNexus for code and curated summaries only. | Projection policy note. |
| 7.4 | Prepare LLM Wiki index only after classification, freshness, source authority, and conflict checks. | Indexing readiness record. |
| 7.5 | Log all knowledge projections and corrections in Activity Ledger. | Ledger evidence. |

# 17. Phase 8 - DevSecOps Pipeline, GitNexus, and Evidence Pack Readiness
| Field | Required Content |
| --- | --- |
| Primary Owner / Execution Surface | DevSecOps Lead + QA/SDET + Security + Developer |
| Objective | Prepare the team to produce evidence by construction before feature volume increases. |
| Exit Gate | Proceed only when the team can produce a repeatable evidence pack for a controlled PR/MR. |
| Minimum Evidence | CI run; scan outputs; SBOM; GitNexus report; evidence pack; PR/MR AVCI summary. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 8.1 | Verify CI/CD stages for build, unit, component, contract, architecture, policy, SAST, SCA, secret scan, DAST readiness, SBOM, provenance, package, and evidence finalization. | Pipeline evidence. |
| 8.2 | Add PR/MR AVCI summary and AI-use declaration. | PR template. |
| 8.3 | Run GitNexus read-only code map and impact analysis where available. | GitNexus evidence. |
| 8.4 | Generate evidence pack from dry-run PR/MR. | Evidence pack. |
| 8.5 | Block feature expansion until CI/CD evidence can be produced and reviewed. | Go/no-go decision. |

# 18. Phase 9 - Dynamic Workspace and Frontend Team Readiness
| Field | Required Content |
| --- | --- |
| Primary Owner / Execution Surface | Frontend Developers + Backend Developers + QA/SDET + Security |
| Objective | Prepare frontend development to follow backend-governed, MicroFunction-backed, policy-filtered Dynamic Workspace controls. |
| Exit Gate | Proceed only when frontend can be developed without bypassing backend, OPA/SBAC, contracts, MicroFunctions, or evidence. |
| Minimum Evidence | Frontend setup; generated client; Playwright/a11y evidence; policy denial test. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 9.1 | Install and validate Node/pnpm, Next.js/React/TypeScript baseline according to approved repo. | Frontend version evidence. |
| 9.2 | Validate generated OpenAPI client pattern and no direct backend bypass. | Generated client evidence. |
| 9.3 | Prepare component registry, widget action contract, layout persistence test, policy denial handling, and safe session context display. | Workspace readiness evidence. |
| 9.4 | Prepare Playwright, accessibility, visual regression, and frontend telemetry tests. | Test readiness. |
| 9.5 | Confirm frontend is not authorization authority; backend policy and MicroFunction execution govern actions. | Boundary acknowledgement. |

# 19. Phase 10 - MicroFunction Backend Runtime Team Readiness
| Field | Required Content |
| --- | --- |
| Primary Owner / Execution Surface | Backend Developers + DBA + QA/SDET + Security |
| Objective | Prepare the team to build backend behavior through configuration-first MicroFunction runtime assembly. |
| Exit Gate | Proceed only when MicroFunction runtime patterns can be configured, tested, observed, and evidenced. |
| Minimum Evidence | Backend tests; Flyway report; OPA tests; architecture fitness; audit/outbox evidence. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 10.1 | Validate Java 25 target baseline, Spring, build tool, Testcontainers, and architecture fitness setup. | Backend version and test evidence. |
| 10.2 | Prepare MicroFunction standard step catalog, transaction definition, idempotency profile, error policy, observability profile, audit profile, and rollback strategy. | MicroFunction config evidence. |
| 10.3 | Validate OPA policy test harness and SBAC input contract. | OPA test evidence. |
| 10.4 | Validate Flyway migration path, seed governance, no manual DDL, and clean/rebuild evidence. | Flyway evidence. |
| 10.5 | Validate audit/outbox pattern and no direct DB/Kafka/Redis/model/audit shortcuts inside business MicroFunctions. | Boundary test evidence. |

# 20. Phase 11 - API, Eventing, Kafka, Avro, CloudEvents, Outbox, DLQ, and Replay Readiness
| Field | Required Content |
| --- | --- |
| Primary Owner / Execution Surface | API Architecture + Backend + DevSecOps + QA/SDET |
| Objective | Prepare the team for contract-first integration and event-driven reliability. |
| Exit Gate | Proceed only when API and event changes are contract-first, traceable, idempotent, and replay-safe. |
| Minimum Evidence | OpenAPI/AsyncAPI lint; schema compatibility; event tests; replay evidence. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 11.1 | Create or validate OpenAPI and AsyncAPI contract structure. | Contract files and lint evidence. |
| 11.2 | Prepare Kafka, Avro, schema registry, CloudEvents, outbox/inbox, idempotent consumer, retry, DLQ, and replay test patterns. | Eventing readiness evidence. |
| 11.3 | Require correlation_id, causation_id, trace_id, idempotency_key, classification, and evidence_ref fields. | Schema review evidence. |
| 11.4 | Validate schema evolution and backward compatibility gates. | Compatibility test evidence. |
| 11.5 | Document replay safety and duplicate handling. | Replay runbook draft. |

# 21. Phase 12 - Observability, Audit, Runtime Toggle, and Dashboard Readiness
| Field | Required Content |
| --- | --- |
| Primary Owner / Execution Surface | SRE / DevSecOps + Backend + Frontend + Security |
| Objective | Ensure critical paths can be reconstructed through logs, metrics, traces, audit, dashboards, and evidence. |
| Exit Gate | Proceed only when observability can support trace reconstruction without exposing secrets or PII. |
| Minimum Evidence | Telemetry config; dashboard screenshots; redaction tests; toggle policy; audit evidence. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 12.1 | Validate Log4j2 structured logging, OpenTelemetry SDK/collector, Sentry, Loki, Tempo, Grafana, and dashboard path where applicable. | Telemetry setup evidence. |
| 12.2 | Define mandatory correlation fields: trace_id, span_id, request_id, actor hash, tenant, classification, policy_ref, microfunction_transaction_code, evidence_ref. | Telemetry schema note. |
| 12.3 | Define forbidden telemetry fields and redaction tests. | Redaction test evidence. |
| 12.4 | Define runtime toggles for diagnostic verbosity, sampling, feature flags, workspace telemetry, and AI assistant telemetry with safe defaults. | Runtime toggle policy. |
| 12.5 | Ensure audit minimums cannot be disabled through runtime toggle. | Audit control evidence. |

# 22. Phase 13 - Security, OPA/SBAC, Abuse Cases, Authenticated DAST, Secure APIs, and Secrets Hygiene
| Field | Required Content |
| --- | --- |
| Primary Owner / Execution Surface | Security Architecture + QA/SDET + DevSecOps + Developer |
| Objective | Prepare security controls and negative tests before high-risk feature or agent work. |
| Exit Gate | Proceed only when security tests, DAST scope, secrets hygiene, OPA/SBAC, and remediation evidence are ready. |
| Minimum Evidence | OPA tests; DAST plan; secret scan; abuse cases; remediation evidence. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 13.1 | Validate OPA/SBAC policy inputs, skill catalog, role boundaries, and deny-by-default rules. | OPA/SBAC evidence. |
| 13.2 | Create abuse case templates for Dynamic Workspace, MicroFunction, API, agent, RAG, tool gateway, and CI/CD workflows. | Abuse case templates. |
| 13.3 | Prepare authenticated DAST with synthetic users and non-prod scope only. | DAST plan. |
| 13.4 | Validate secure API error handling, rate limiting, CORS/CSRF, token safety, and no secrets in logs/prompts. | Security test evidence. |
| 13.5 | Create remediation evidence template and waiver workflow. | Remediation template. |

# 23. Phase 14 - Concurrency, Heavy Transaction, Idempotency, and Resilience Lab Readiness
| Field | Required Content |
| --- | --- |
| Primary Owner / Execution Surface | QA/SDET + Backend + DevSecOps + SRE |
| Objective | Prepare failure-aware, retry-safe, duplicate-safe, heavy-load behavior before business transaction volume. |
| Exit Gate | Proceed only when retry, duplicate, concurrent, heavy-load, and failure paths are testable and evidenced. |
| Minimum Evidence | Resilience lab report; test results; DLQ/replay evidence; rollback/compensation template. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 14.1 | Prepare Testcontainers or approved local/CI lab for PostgreSQL, Kafka, Redis/Valkey, OPA, and dependent services. | Lab setup evidence. |
| 14.2 | Create idempotency and duplicate request tests. | Test results. |
| 14.3 | Create outbox/inbox, retry, DLQ, replay, and consumer restart tests. | Event resilience evidence. |
| 14.4 | Create DB contention, optimistic locking, transaction timeout, cache loss, and backpressure tests. | Concurrency evidence. |
| 14.5 | Create failure injection runbook and compensation/rollback evidence template. | Resilience runbook. |

# 24. Phase 15 - Governed Agent Sandbox, Hermes, LiteLLM, Guardrails, and Harness Readiness
| Field | Required Content |
| --- | --- |
| Primary Owner / Execution Surface | AI Governance + Security + DevSecOps + Agent Owner |
| Objective | Introduce agents only as governed sandbox candidates after workstation and repository controls are stable. |
| Exit Gate | Proceed only when agents are sandboxed, registry-bound, policy-gated, guardrailed, observable, reversible, and human-accountable. |
| Minimum Evidence | Agent identity cards; model route evidence; guardrail policy; tool manifest; sandbox evidence. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 15.1 | Confirm no agent is installed or activated before identity card, owner, purpose, non-goals, scope, and evidence path exist. | Agent identity draft. |
| 15.2 | Configure LiteLLM/model aliases and guardrail checkpoints only through approved gateway patterns; no direct model-provider calls from application code. | Model route evidence. |
| 15.3 | Introduce Hermes only in sandbox with no production credentials and no autonomous production mutation. | Hermes sandbox evidence. |
| 15.4 | Define Harness/MCP/tool gateway boundary, dry-run requirement, idempotency, rollback, and approval rules. | Tool gateway draft. |
| 15.5 | Log each agent prompt, tool action request, model route, guardrail result, policy decision, and evidence reference. | Agent telemetry/evidence plan. |

# 25. Phase 16 - Agent Registry, Threat Model, Certification, and Promotion Gate
| Field | Required Content |
| --- | --- |
| Primary Owner / Execution Surface | AI Governance + Security + QA/SDET + Internal Audit |
| Objective | Prevent shadow agents and uncontrolled autonomy by binding all agents to registry, threat model, evaluation, and certification evidence. |
| Exit Gate | Proceed only when each agent has identity, owner, SBAC, OPA, tool scope, model route, threat model, evaluation, telemetry, and kill switch evidence. |
| Minimum Evidence | Registry draft; threat model; evaluation report; certification decision; lifecycle controls. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 16.1 | Create agent registry records or draft seed records for proposed agents. | Agent registry draft. |
| 16.2 | Complete threat model and abuse case mapping for each agent. | Threat model evidence. |
| 16.3 | Assign autonomy risk tier per action, not only per agent. | Autonomy tier matrix. |
| 16.4 | Run red-team/evaluation tests before any promotion beyond advisory or read-only use. | Evaluation evidence. |
| 16.5 | Define kill switch, suspension, revocation, recertification, and retirement path. | Lifecycle control evidence. |

# 26. Phase 17 - Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop Readiness
| Field | Required Content |
| --- | --- |
| Primary Owner / Execution Surface | DevSecOps + SRE + QA/SDET + AI Governance + Human Approver |
| Objective | Enable improvement loops as proposal-driven workflows, not autonomous mutation. |
| Exit Gate | Proceed only when improvement loops cannot silently mutate code, config, prompts, policy, agents, environments, or production. |
| Minimum Evidence | Detection register; candidate template; tests/scans; backlog; approval evidence. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 17.1 | Define issue detection sources: CI failures, tests, SAST/SCA/DAST findings, logs, traces, metrics, Sentry issues, GitNexus impact, incidents, and user feedback. | Detection source register. |
| 17.2 | Define evidence retrieval rules and classification filters. | Retrieval rule evidence. |
| 17.3 | Define candidate fix/learning/improvement proposal template. | Proposal template. |
| 17.4 | Require tests, scans, architecture fitness, rollback/forward-fix, and human approval before merge or activation. | Approval gate. |
| 17.5 | Record rejected, deferred, approved, and implemented candidates in improvement backlog. | Backlog evidence. |

# 27. Phase 18 - Team Dry Run PR/MR and Ready-to-Proceed Gate
| Field | Required Content |
| --- | --- |
| Primary Owner / Execution Surface | Team Lead + DevSecOps + QA/SDET + Security + Reviewers |
| Objective | Perform a team dry run to prove end-to-end readiness before PoC feature execution. |
| Exit Gate | Proceed only when the team can reproduce the same governed setup and evidence workflow across multiple workstations. |
| Minimum Evidence | Dry-run PRs/MRs; CI evidence; review notes; readiness dashboard; go/no-go decision. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 18.1 | Each developer creates a low-risk documentation or validation change in a branch. | Branch evidence. |
| 18.2 | Run local validation, tests, scans, and evidence generation. | Local evidence. |
| 18.3 | Open PR/MR with AVCI summary, AI-use declaration, evidence register update, and rollback/forward-fix note. | PR/MR evidence. |
| 18.4 | Reviewer checks setup compliance, Codex boundary, source references, tests, security, and evidence completeness. | Review evidence. |
| 18.5 | Hold Ready-to-Proceed review before Login PoC 1 / PoC 1A / PoC 2 work expands. | Go/no-go decision. |

# 28. Governed Agent Inventory Starter Matrix

The following starter matrix is not an approval to activate agents. It defines candidate agent categories that must be registered, scoped, tested, and certified before active use. Each agent must have a named owner, purpose, non-goals, SBAC scope, allowed tools, autonomy tier, OPA policy, model route, guardrails, evidence path, threat model, evaluation, telemetry, and retirement plan.
| Candidate Agent | Purpose | Allowed by Default | Prohibited by Default |
| --- | --- | --- | --- |
| Architecture Agent | Analyze architecture impacts, draft ADR/TDL options, detect boundary drift. | Advisory analysis, draft diagrams, draft impact review. | Approve architecture, waive fitness gates, merge code. |
| Developer Agent | Draft candidate code, tests, refactoring options, and local validation scripts. | Branch/sandbox candidate artifacts. | Direct push to main, production mutation, secret access. |
| Security Agent | Review OPA/SBAC, secrets hygiene, abuse cases, DAST/SAST findings, secure API gaps. | Advisory review and remediation proposal. | Grant access, override policy, suppress findings without approval. |
| Test Agent | Draft unit, contract, Playwright, OPA, mutation, resilience, and regression tests. | Candidate tests and test-gap analysis. | Mark quality gates as passed without execution evidence. |
| Documentation Agent | Draft standards, runbooks, summaries, evidence templates, and Obsidian projections. | Candidate documentation with sources. | Promote drafts as canonical without review. |
| Evidence Agent | Assemble evidence pack, trace links, source refs, test/scan summaries. | Derivative evidence summaries. | Fabricate evidence or replace raw evidence stores. |
| CI/CD Agent | Draft pipeline, workflow, validation, SBOM, signing, and scanner improvements. | Candidate CI/CD changes in branch. | Deploy, approve, disable gates, access production runners. |
| Knowledge Fabric Agent | Curate retrieval metadata, freshness, conflict flags, LLM Wiki indexing candidates. | Candidate projection and retrieval checks. | Index Restricted data or treat AI summary as Tier-0 authority. |

# 29. RACI and Separation of Duties
| Activity | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Team rollout approval | Team Lead | IT Head / Solutions Architecture | Security, DevSecOps, QA, AI Governance | Development team |
| Workstation setup | Developer / System Admin | Team Lead | Security, DevSecOps | IT Head |
| Tool registry | Developer | DevSecOps Lead | Security, QA | Team |
| Activity ledger | Developer | Team Lead | Knowledge Governance | Reviewers |
| Repository controls | DevSecOps | DevSecOps Lead | Security, Architecture | Developers |
| Codex enablement | Developer | Software Development Lead | Security, DevSecOps | QA |
| Obsidian projection | Knowledge Steward | Knowledge Governance | Architecture, Security | Team |
| Agent identity card | Agent Owner | AI Governance | Security, DevSecOps, Architecture | Internal Audit |
| Agent threat model | Security / Agent Owner | Security Architecture | AI Governance, QA | Team Lead |
| Agent sandbox approval | AI Governance / Security | Architecture Board / delegated approver | DevSecOps, QA | Internal Audit |
| CI/CD evidence | DevSecOps / QA | DevSecOps Lead | Security, Architecture | Team |
| Ready-to-proceed gate | Team Lead | IT Head / Architecture | Security, QA, DevSecOps, AI Governance | All stakeholders |

# 30. Acceptance Criteria and Definition of Done
| Acceptance Area | Required Evidence |
| --- | --- |
| Team readiness | Every team member has assigned role, workstation_id, checker, source access, tool registry, and activity ledger. |
| Workstation readiness | Windows baseline, approved tools, versions, folders, repository clone, VS Code, Codex boundary, and local validation evidence exist. |
| Repository readiness | Branch rules, CODEOWNERS, PR/MR template, AGENTS.md, evidence register, source register, and first dry-run PR/MR exist. |
| Knowledge readiness | Obsidian vault, metadata, source register, freshness/conflict register, and LLM Wiki readiness controls exist. |
| DevSecOps readiness | CI/CD pipeline, security scans, SBOM/provenance, GitNexus read-only analysis, architecture fitness, and evidence pack are proven. |
| Dynamic Workspace readiness | Generated API client, component registry, policy-denial handling, Playwright/a11y/visual tests, and frontend telemetry readiness exist. |
| MicroFunction readiness | Java 25 target, Flyway, OPA/SBAC, audit/outbox, idempotency, Testcontainers, architecture tests, and standard step catalog are ready. |
| API/eventing readiness | OpenAPI, AsyncAPI, Kafka, Avro, CloudEvents, schema evolution, outbox/inbox, idempotent consumers, DLQ, retry, and replay patterns are testable. |
| Observability readiness | Log4j2, OpenTelemetry, Sentry, Loki, Tempo, Grafana, dashboards, audit events, trace reconstruction, and runtime toggle controls are defined. |
| Security readiness | OPA/SBAC, abuse cases, authenticated DAST scope, secure API tests, secrets hygiene, remediation evidence, and waiver workflow exist. |
| Resilience readiness | Retry-safe, duplicate-safe, concurrent, heavy-load, failure-injection, DLQ/replay, cache-loss, and DB contention tests are ready. |
| Agent readiness | No agent is active unless identity card, registry, owner, SBAC, OPA, tool scope, model route, guardrails, threat model, evaluation, telemetry, kill switch, and approval evidence exist. |
| Improvement readiness | Auto-Heal/Auto-Learn/Auto-Improve candidate loop is proposal-driven and cannot silently mutate production or canonical sources. |

# 31. Risk and Control Register
| Risk | Severity | Mandatory Control | Evidence |
| --- | --- | --- | --- |
| Different developers install different tools or versions. | High | Approved tool registry, version evidence, checker sign-off, devcontainer where possible. | TOOL_REGISTRY.md; version files. |
| Personal AI tools or accounts used for AIRA work. | High | Approved AI accounts only; AI-use declaration; no Restricted data in prompts. | AI-use records; policy acknowledgement. |
| Codex modifies files outside branch or without evidence. | High | AGENTS.md, branch protection, PR/MR evidence, human review. | PR/MR; Git diff; ledger. |
| Hermes or agent introduced too early as installer/orchestrator. | High | Hermes deferred to sandbox; no production credentials; registry and threat model required. | Agent sandbox checklist. |
| Secrets exposed in .env, logs, prompts, screenshots, or Obsidian. | Critical | Approved secret vault/password manager only; secret scan; redaction; training. | Secret scan; remediation evidence. |
| Agent privilege amplification or multi-agent bypass. | Critical | SBAC, OPA, tool gateway, autonomy tier per action, human approval, telemetry. | Policy decisions; audit events. |
| Frontend bypasses backend policy. | High | Backend-governed Dynamic Workspace; generated clients; OPA/SBAC; policy-denial tests. | Contract and tests. |
| MicroFunction shortcuts create architecture drift. | High | Ports/adapters, architecture fitness, no direct DB/Kafka/model/audit shortcuts. | ArchUnit/Semgrep evidence. |
| Evidence becomes narrative without raw proof. | Medium | Ledger links to raw evidence, CI artifacts, Git commits, scans, traces, and approvals. | Evidence register. |
| Auto-Heal mutates without approval. | Critical | Candidate-only loop; tests, scans, rollback, human approval. | Improvement proposal and PR/MR. |

# 32. Cross-Document Reconciliation and Future Regeneration Candidates
| Item | Issue / Risk | Recommended Treatment |
| --- | --- | --- |
| 39A/39B/39C overlap | 39A governs VS Code/Codex setup, 39B governs individual workstation execution, 39C governs team rollout and agent setup. | Keep distinctions visible in document register and cross-references. |
| 41B / 44 System Builder overlap | System Builder standard appears in multiple pack positions. | Track in 00D and use canonical register when updated. |
| Older Java/runtime references | Some older source text may reference older baselines. | Java 25 is default backend baseline unless waived. |
| Agent registry timing | 42O-42S define formal registry; early team setup may use draft registers before implementation. | Use draft register fields and later migrate to authoritative registry via Flyway/API. |
| Runtime telemetry toggles | Logging/telemetry toggles need consistent governance across 09, 31A, 53, and runtime config docs. | Track as improvement item and strengthen in observability/runtime config documents. |
| Source pack de-duplication | Known duplicate numbering and superseded references remain. | Treat as AVCI reconciliation items and do not silently normalize. |

# 33. AVCI Compliance Summary
| AVCI Property | How This Playbook Satisfies It |
| --- | --- |
| Attributable | Defines owner, co-owners, team roles, workstation IDs, agent IDs, source references, tool ownership, activity IDs, evidence IDs, reviewer/checker roles, and approval paths. |
| Verifiable | Requires workstation evidence, version evidence, CI/CD evidence, GitNexus output, tests, scans, dashboards, OPA decisions, agent evaluation, threat model, dry-run PR/MR, and raw evidence links. |
| Classifiable | Requires classification for source documents, prompts, evidence, logs, screenshots, Obsidian projections, LLM Wiki retrieval, agent context, model routes, and telemetry. |
| Improvable | Creates feedback paths through Activity Ledger, improvement backlog, Auto-Heal/Auto-Learn/Auto-Improve candidate loop, readiness dashboard, risk register, and cross-document reconciliation items. |

# Appendix A - Copy-Ready Team Activity Ledger Template
| # AIRA Team Activity Ledger Entry activity_id: AIRA-ACT-YYYYMMDD-WKSxx-NNN agent_activity_id: AIRA-AGT-ACT-YYYYMMDD-AGTxx-NNN # if applicable workstation_id: WKSxx agent_id: N/A or AGT-xxxx owner: <name> checker: <name> date_time_local: <YYYY-MM-DD HH:MM +08:00> tool_or_actor: ChatGPT \| Codex \| Hermes \| Human \| Git \| CI \| OPA \| Flyway \| GitNexus \| Other phase: <39C phase number> purpose: <why the activity was performed> source_ref: <AIRA doc / ticket / branch / prompt / command> classification: Public \| Internal \| Confidential \| Restricted input_summary: <redacted summary only> action_taken: <what was done> output_summary: <result summary> evidence_ref: <path / commit / CI run / screenshot / report> validation_result: PASS \| FAIL \| BLOCKED \| WAIVED risk_or_issue: <if any> follow_up: <next action> approver_required: Yes \| No approval_ref: <ticket / PR / CAB / ARB / reviewer> |
| --- |

# Appendix B - Copy-Ready Team Readiness Dashboard
| # AIRA Team Readiness Dashboard \| Workstation ID \| Owner \| Checker \| Phase 0 \| Phase 1 \| Phase 2 \| Phase 3 \| Phase 4 \| Phase 5 \| Phase 6 \| Phase 7 \| Phase 8 \| Phase 9-14 \| Phase 15-16 Agent \| Phase 17-18 \| Blocker \| Evidence Ref \| \|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\| \| WKS01 \| <name> \| <checker> \| Not Started \| Not Started \| Not Started \| Not Started \| Not Started \| Not Started \| Not Started \| Not Started \| Not Started \| Not Started \| Deferred \| Not Started \|  \|  \| Status values: Not Started \| In Progress \| Evidence Pending \| Checker Review \| Passed \| Blocked \| Deferred \| Waived by Approval |
| --- |

# Appendix C - Copy-Ready Agent Identity Card Template
| # AIRA Agent Identity Card agent_id: AGT-xxxx agent_name: <candidate name> agent_type: architecture \| developer \| security \| test \| documentation \| evidence \| cicd \| knowledge \| other owner: <named human owner> backup_owner: <named human backup> purpose: <specific purpose> non_goals: <what the agent must not do> lifecycle_state: candidate \| sandbox \| certified \| active \| suspended \| revoked \| retired classification_ceiling: Internal \| Confidential \| Restricted allowed_data_scope: <approved sources only> sbac_skills: <skill codes> opa_policy_ref: <policy package/version> autonomy_tier_allowed: T0 \| T1 \| T2 \| T3 \| T4 \| T5-human-only model_route: <LiteLLM alias or approved route> guardrail_profile: <input/retrieval/execution/output checkpoints> allowed_tools: <tool manifest IDs> prohibited_tools: <explicitly prohibited> threat_model_id: <required before sandbox expansion> abuse_case_ids: <required> evaluation_pack_ref: <red-team/certification evidence> telemetry_fields: agent_id, run_id, trace_id, policy_decision_id, tool_action_id, evidence_ref kill_switch: <how to suspend> rollback_or_deactivation: <safe stop path> recertification_due: <date> retirement_plan: <decommission proof> |
| --- |

# Appendix D - Copy-Ready Agent Sandbox Checklist
| # AIRA Governed Agent Sandbox Checklist [ ] Named owner and backup owner assigned [ ] Purpose and non-goals documented [ ] Agent identity card completed [ ] Source, data, and classification ceiling defined [ ] SBAC skills and OPA policy references drafted [ ] LiteLLM/model route and guardrail profile approved for sandbox [ ] Tool manifest drafted; dry-run required where feasible [ ] No production credentials assigned [ ] No direct model-provider calls from application code [ ] No direct Git merge/deploy/approval authority [ ] Threat model and abuse cases completed [ ] Evaluation/red-team checklist created [ ] Telemetry fields defined: agent_id, run_id, trace_id, policy_decision_id, tool_action_id, evidence_ref [ ] Kill switch and suspension path defined [ ] Evidence path created [ ] Human checker assigned [ ] Sandbox approval recorded |
| --- |

# Appendix E - Copy-Ready Team Rollout Command Evidence Baseline
| # Evidence folders Set-Location "D:\ChatGPT Workspace" New-Item -ItemType Directory -Force -Path ".\AIRA Evidence\Team-Rollout" \| Out-Null New-Item -ItemType Directory -Force -Path ".\AIRA Evidence\Team-Rollout\Phase-04-Tools" \| Out-Null New-Item -ItemType Directory -Force -Path ".\AIRA Evidence\Team-Rollout\Phase-05-Repo" \| Out-Null # Basic version evidence - run after approved installation $EvidenceRoot = "D:\ChatGPT Workspace\AIRA Evidence\Team-Rollout\Phase-04-Tools" Get-ComputerInfo \| Out-File "$EvidenceRoot\computer-info.txt" git --version \| Tee-Object -FilePath "$EvidenceRoot\git-version.txt" gh --version \| Tee-Object -FilePath "$EvidenceRoot\gh-version.txt" code --version \| Tee-Object -FilePath "$EvidenceRoot\vscode-version.txt" java --version 2>&1 \| Tee-Object -FilePath "$EvidenceRoot\java-version.txt" mvn --version 2>&1 \| Tee-Object -FilePath "$EvidenceRoot\maven-version.txt" gradle --version 2>&1 \| Tee-Object -FilePath "$EvidenceRoot\gradle-version.txt" node --version \| Tee-Object -FilePath "$EvidenceRoot\node-version.txt" npm --version \| Tee-Object -FilePath "$EvidenceRoot\npm-version.txt" pnpm --version \| Tee-Object -FilePath "$EvidenceRoot\pnpm-version.txt" flyway -v 2>&1 \| Tee-Object -FilePath "$EvidenceRoot\flyway-version.txt" opa version \| Tee-Object -FilePath "$EvidenceRoot\opa-version.txt" gitleaks version 2>&1 \| Tee-Object -FilePath "$EvidenceRoot\gitleaks-version.txt" trivy --version 2>&1 \| Tee-Object -FilePath "$EvidenceRoot\trivy-version.txt" syft version 2>&1 \| Tee-Object -FilePath "$EvidenceRoot\syft-version.txt" cosign version 2>&1 \| Tee-Object -FilePath "$EvidenceRoot\cosign-version.txt" semgrep --version 2>&1 \| Tee-Object -FilePath "$EvidenceRoot\semgrep-version.txt" # VS Code extension evidence code --list-extensions \| Tee-Object -FilePath "$EvidenceRoot\vscode-extensions.txt" |
| --- |

# Appendix F - Copy-Ready PR/MR Team Readiness Evidence Template
| ## AIRA Team Readiness PR/MR Evidence Summary ### Attributable - Owner: - Checker: - Workstation ID: - Branch: - Commit(s): - Related Activity IDs: - Related Evidence IDs: - AI tools used: - Agent IDs involved, if any: ### Verifiable - Tool version evidence: - Local validation: - Unit/component/contract tests: - OPA/SBAC tests: - Flyway validation: - Secret scan: - SAST/SCA/DAST readiness: - GitNexus evidence: - Observability evidence: - Resilience evidence: ### Classifiable - Data classification: - Prompt classification: - Evidence classification: - Secrets/PII handling: - Retrieval eligibility: ### Improvable - Known gaps: - Blockers: - Improvement candidates: - Reconciliation items: - Next recommended action: ### Approval - Maker: - Checker: - Security reviewer: - DevSecOps reviewer: - QA reviewer: - Final readiness decision: Proceed \| Block \| Proceed with waiver |
| --- |

