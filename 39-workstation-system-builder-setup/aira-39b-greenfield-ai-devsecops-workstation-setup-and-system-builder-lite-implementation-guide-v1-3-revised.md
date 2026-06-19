---
title: "Greenfield AI DevSecOps Workstation Setup and System Builder Lite Implementation Guide"
doc_id: "AIRA-39B"
version: "v1.3"
status: "revised"
category: "Workstation and system builder setup"
source_docx: "AIRA_39B_Greenfield_AI_DevSecOps_Workstation_Setup_and_System_Builder_Lite_Implementation_Guide_v1.3_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 39-workstation-system-builder-setup
  - revised
  - aira-39b
---



# Greenfield AI DevSecOps Workstation Setup and System Builder Lite Implementation Guide



AIRA

AI-Native Enterprise Platform

AIRA Greenfield AI DevSecOps Workstation Setup and System Builder Lite Implementation Guide

v1.3 Revised

Windows 11 Bootstrap · ChatGPT Project-First Guidance · VS Code Codex · Obsidian · Dynamic Workspace · MicroFunction Runtime · Evidence Before PoC
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-039B |
| Canonical Filename | AIRA_39B_Greenfield_AI_DevSecOps_Workstation_Setup_and_System_Builder_Lite_Implementation_Guide_v1.3_Revised.docx |
| Version | v1.3 - 09 v3.2 Environment Baseline, Dynamic Workspace, MicroFunction Runtime, DevSecOps Evidence, Observability, Resilience, and Progressive Autonomy Alignment Update |
| Supersedes | 39B-AIRA_Greenfield_AI_DevSecOps_Workstation_Setup_and_System_Builder_Lite_Implementation_Guide_v1.2.docx |
| Status | Draft for Architecture, DevSecOps, Security, Platform Engineering, QA/SDET, AI Governance, DBA, SRE, Internal Audit, and Team Controlled First Execution Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; DevSecOps Lead; Software Development Lead; Security Architecture; Platform Engineering; QA/SDET; DBA; SRE / Operations; AI Governance; Internal Audit |
| Primary Audience | AIRA System Builder operators; Windows 11 workstation builders; VS Code Codex users; developers; architects; security; QA/SDET; DevSecOps; AI Engineering; reviewers |
| Primary Parent | 09-AIRA Greenfield Environment Standard v3.2 Revised |
| Companion Sources | 07 AI DevSecOps Skills Framework; 07B Team Transformation; 09 Greenfield Environment; 10 MicroFunction; 11 DevSecOps; 12A/41/46-61 Dynamic Workspace; 15 API; 16 Flyway/Database; 17 Security; 19 GitNexus; 20 CI/CD Evidence; 31/31A Observability; 39A Codex System Builder Lite; 43 Continuous Improvement; 42D-42N Agent Governance |
| Effective Date | Upon Architecture Review Board / CAB / Security Governance / DevSecOps Governance approval |
| Review Cadence | Before team-wide rollout; after first workstation execution; quarterly; and on material toolchain, AI, security, Dynamic Workspace, MicroFunction, CI/CD, or observability change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Greenfield-Workstation-System-Builder-Lite / v1.3 / |
| Generated | 2026-06-17 11:25 |
| Mandatory Practice Statement This workstation setup is not a casual tool installation exercise. It is the controlled creation of an AIRA AI DevSecOps workstation that must inherit 09 v3.2 greenfield environment readiness, Dynamic Workspace discipline, MicroFunction runtime discipline, DevSecOps gates, evidence packs, GitNexus read-only analysis, API/eventing readiness, observability, resilience, security, AI governance, runtime toggle governance, and proposal-driven improvement loops. ChatGPT Project guides Day 0 governance and setup sequencing. Humans execute privileged installation and account actions. Codex starts only after VS Code, Git, repository controls, AGENTS.md, branch rules, and evidence capture are ready. AI may guide, recommend, draft, generate, analyze, test, and propose. AI must not approve, merge, deploy, disable controls, access production credentials, mutate production, or become business authority. |
| --- |

ChatGPT Project Guides Bootstrap · Human Executes Privileged Actions · Codex Works Only in Governed Branches · CI/CD Verifies · Humans Approve · AVCI Always

# Static Table of Contents

1. Executive Summary

2. v1.3 Update Verdict and Change Summary

3. Purpose, Scope, and Authority

4. Governing Source Baseline and External Alignment

5. Execution Surface Decision Model

6. Greenfield Setup Principles and Non-Negotiables

7. Target Local Folder and Source Governance Model

8. End-to-End Procedure Overview

9. Phase 0 - Pre-Start Readiness

10. Phase 1 - Secure Windows 11 Baseline

11. Phase 2 - ChatGPT Project and Active Source Bootstrap

12. Phase 3 - Local AIRA Workspace, Registers, and Evidence

13. Phase 4 - Install Core Workstation Tools

14. Phase 5 - Repository Bootstrap and System Builder Lite Guardrails

15. Phase 6 - VS Code, Codex, and AI-Assisted Developer Controls

16. Phase 7 - Obsidian, LLM Wiki Projection, and Knowledge Control Readiness

17. Phase 8 - Devcontainer and Toolchain Reproducibility Validation

18. Phase 9 - Dynamic Workspace and Frontend UX Readiness

19. Phase 10 - MicroFunction Backend and Runtime Assembly Readiness

20. Phase 11 - API, Eventing, Kafka, Avro, CloudEvents, Outbox, DLQ, and Replay Readiness

21. Phase 12 - Observability, Audit, Evidence, Runtime Toggle, and Dashboard Readiness

22. Phase 13 - Security, OPA/SBAC, Abuse Cases, Authenticated DAST, Secure APIs, and Secrets Hygiene

23. Phase 14 - Concurrency, Heavy Transaction, Idempotency, and Resilience Lab Readiness

24. Phase 15 - AI DevSecOps, Hermes, LiteLLM, Guardrails, Harness, and Agent Boundary Readiness

25. Phase 16 - Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop Readiness

26. Phase 17 - First PR/MR, Evidence Pack, and Go/No-Go Gate

27. RACI and Separation of Duties

28. Acceptance Criteria

29. Cross-Document Reconciliation and Regeneration Candidates

30. Risk and Control Register

31. AVCI Compliance Summary

Appendix A - Copy-Ready Windows PowerShell Command Baseline

Appendix B - Copy-Ready AGENTS.md Baseline

Appendix C - Copy-Ready Evidence Register

Appendix D - Copy-Ready PR/MR Template

Appendix E - Copy-Ready Validation Checklist

Appendix F - External Reference Register

# 1. Executive Summary

This v1.3 revision updates AIRA-DOC-039B so the step-by-step workstation setup guide implements the revised 09 Greenfield Environment Standard v3.2. The prior v1.2 guide correctly established ChatGPT Project-first guidance, human-executed privileged setup, Codex-after-VS-Code sequencing, local source/evidence registers, repository governance, and PoC readiness. Version v1.3 preserves those controls and expands them into a complete developer execution runway for Dynamic Workspace, MicroFunction backend, DevSecOps evidence, API/eventing, observability, security, resilience, and governed AI-assisted improvement.

The main operating decision is that a workstation is not ready because Windows, VS Code, Git, Java, Node, and Codex are installed. It is ready only when the workstation can reproducibly build, test, scan, observe, evidence, roll back, and improve AIRA artifacts through approved repositories, source baselines, contracts, MicroFunctions, Dynamic Workspace controls, CI/CD gates, OPA/SBAC policy, AI governance, and AVCI evidence.

This document is execution-oriented. It tells the team what to do in ChatGPT Project, what to do as a human OS/admin action, what to do in local CLI, what to do in VS Code/Codex, what to capture in Obsidian/Git, and what must be proven by CI/CD before PoC development proceeds.
| Strategic Outcome | v1.3 Required Result |
| --- | --- |
| Controlled Day 0 setup | ChatGPT Project guides sequencing; humans execute privileged actions; no AI gets install, credential, approval, merge, deployment, or production authority. |
| Governed coding runway | VS Code and Codex operate only after repository rules, AGENTS.md, CODEOWNERS, PR template, branch naming, and evidence register exist. |
| Dynamic Workspace readiness | Frontend setup includes backend-governed workspace resolution, component registry, generated clients, Playwright, accessibility, visual regression, and policy-denial testing. |
| MicroFunction readiness | Backend setup includes Java 25 target baseline, Spring, OPA, Flyway, Testcontainers, audit/outbox, idempotency, standard step catalog, and architecture fitness checks. |
| Evidence readiness | Every setup phase produces owner, source, evidence path, validation result, classification, known gaps, and follow-up action. |
| Progressive autonomy readiness | AI tools remain advisory and candidate-generating until evidence, trust, SBAC, OPA, guardrails, rollback, and named human approval permit limited delegation. |

# 2. v1.3 Update Verdict and Change Summary

Revision verdict: update 39B now. The revised 09 v3.2 standard defines the target governed environment. 39B is the document that converts that target into executable workstation setup steps. Delaying 39B would leave the development team with high-level governance but incomplete day-to-day instructions.
| Update Area | v1.3 Improvement |
| --- | --- |
| 09 v3.2 inheritance | Adds greenfield acceptance rule: tools installed is not enough; build, test, secure, observe, govern, evidence, rollback, and improvement proof are required. |
| Dynamic Workspace setup | Adds frontend/workspace readiness: Next.js/TypeScript, generated API client, component registry, accessibility, Playwright, visual regression, backend authority, OPA filtering, and no frontend authorization authority. |
| MicroFunction setup | Adds backend runtime readiness: Java 25 target, Spring, OPA, Flyway, Testcontainers, idempotency, outbox, audit, OpenTelemetry, architecture tests, and standard step validation. |
| DevSecOps/GitNexus | Adds early preparation for SAST, SCA, secret scan, SBOM, provenance, GitNexus read-only impact analysis, evidence pack, and PR/MR AVCI summary. |
| API/eventing | Adds OpenAPI, AsyncAPI, Kafka, Avro, CloudEvents, schema evolution, idempotent consumers, retry, DLQ, replay, correlation_id, causation_id, and trace_id readiness checks. |
| Observability/runtime toggles | Adds Log4j2, OpenTelemetry, Sentry, Loki, Tempo, Grafana, dashboard, alerting, trace reconstruction, runtime sampling, diagnostic toggles, and mandatory audit minimums. |
| Security/DAST | Adds OPA/SBAC expansion, abuse-case setup, authenticated DAST readiness, secure API testing, secrets hygiene, and remediation evidence. |
| Resilience lab | Adds local and CI-ready tests for retry-safe, duplicate-safe, concurrent, heavy-load, cache-loss, OPA failure, Kafka replay, and DB contention scenarios. |
| Auto-Heal/Auto-Learn/Auto-Improve | Adds candidate loop setup: detect issue, retrieve evidence, propose fix/learning, generate tests, route for human approval, and prevent silent mutation. |

# 3. Purpose, Scope, and Authority

## 3.1 Purpose

Define the exact greenfield Windows 11 workstation setup sequence for AIRA AI DevSecOps.

Distinguish what must be performed in ChatGPT Project, what must be performed in Codex, what must be human-executed, and what must be validated by local tools or CI/CD.

Prevent Codex, ChatGPT, Hermes, agents, MCP connectors, or any AI tool from becoming an uncontrolled installer, source authority, approval bypass, production actor, or credential holder.

Establish the local folder model that lets Codex reference active AIRA documents through a governed local workspace without treating local copies or AI summaries as Tier-0 authority.

Prepare the workstation for controlled Login PoC 1, PoC 1A, PoC 2 DevSecOps factory, Dynamic Workspace, MicroFunction runtime, API/eventing, observability, security, and resilience work.

## 3.2 Scope
| In Scope | Out of Scope |
| --- | --- |
| Windows 11 security baseline; browser/password manager readiness; ChatGPT Project setup; active source upload; local folder structure; VS Code; Git; GitHub/GitLab CLI; Java; Maven/Gradle; Node; pnpm/npm; Flyway; OPA; secret scanner; approved local tools; Codex; Obsidian; source register; evidence register; readiness gates. | Production deployment; production credentials; direct production database access; direct production Kubernetes access; direct production workflow mutation; direct model-provider calls from application code; uncontrolled MCP/tool expansion; bypass of CAB/ARB/Security/DBA/QA review. |
| System Builder Lite controls: AGENTS.md, CODEOWNERS, PR/MR template, branch naming, evidence register, source register, local validation, basic CI, AI-use declaration, architecture fitness, and rollback evidence. | Full AIRA System Builder runtime implementation; Level 8 autonomy delegation; self-approving agents; direct infrastructure provisioning by AI without IaC/GitOps approval; unmanaged local-only scripts used as authority. |
| Dynamic Workspace, MicroFunction, API/eventing, observability, security, resilience lab, and Auto-Heal candidate-readiness setup for developer machines and local/CI validation. | Building the full production Dynamic Workspace, MicroFunction engine, Kafka platform, observability cluster, AI gateway, or production runtime outside approved project scope. |

## 3.3 Authority and Precedence
| Level | Authority | Role |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance | Final authority for production-impacting controls, exceptions, high-risk autonomy, and material architecture decisions. |
| L1 | AIRA AVCI, Enterprise Architecture, AI Governance, Security, DevSecOps, MicroFunction, Database, Observability, Dynamic Workspace, and Change Governance standards | Universal quality, architecture, security, evidence, policy, rollback, and improvement discipline. |
| L2 | 09 v3.2 Greenfield Environment Standard, 39A Codex System Builder Lite Guide, and this 39B v1.3 guide | Environment and workstation setup baseline for controlled first execution. |
| L3 | AGENTS.md, CODEOWNERS, PR/MR templates, CI/CD, OPA, Flyway, evidence packs, local validation scripts | Execution-level enforcement. |
| L4 | Feature branches, logs, test results, scan evidence, prompt logs, review records | Implementation proof and improvement input. |
| Conflict Rule Where documents appear inconsistent, apply the stricter AIRA control temporarily, log the item as an AVCI reconciliation issue, assign an owner, and resolve through governed review. Do not silently select the easiest interpretation. |
| --- |

# 4. Governing Source Baseline and External Alignment

This guide must be executed using the current canonical AIRA baseline and the latest approved/revised outputs produced in this document sequence. Older versions, duplicate-number files, and informal drafts may be used for audit history only unless the canonical register authorizes them as active.
| Source Family | Required Use in 39B v1.3 |
| --- | --- |
| 01 / 01A / 01B | AVCI, enterprise design principles, SOLID, architecture fitness, evidence, traceability, classification, and improvement gates. |
| 07 / 07B | Skills, SBAC, trust scoring, team maturity, measured progressive autonomy, delegation limits, and recertification. |
| 09 v3.2 | Primary environment readiness authority: tools are not enough; readiness requires build/test/security/observability/evidence/rollback/improvement proof. |
| 10 / 10A-D / 10E | MicroFunction configuration-first design, runtime assembly, sequence, standard catalog, backend generation, and standard step validation. |
| 11 / 11A / 20 / 45 | DevSecOps pipeline, security gates, evidence pack, GitNexus, system factory, supply-chain, SBOM, provenance, and CI/CD readiness. |
| 12A / 41 / 46-61 | Dynamic Workspace, Composable Experience Framework, frontend UX, component registry, API binding, security, testing, observability, admin builder, and evidence. |
| 15 / 15A | OpenAPI, AsyncAPI, CloudEvents, Kafka, Avro, contract-first development, schema evolution, idempotency, error handling, and integration evidence. |
| 16 / 16A / 16B | Flyway-only database governance, schema ownership, migration validation, seed data, RLS, idempotency registry, outbox, and migration evidence. |
| 17 / 17A / 32 | Identity, secrets, RBAC/ABAC/SBAC, OPA, classification, policy-as-code, least privilege, and fail-closed access control. |
| 19 / 31 / 31A / 53 | GitNexus read-only impact analysis, observability, telemetry, audit, evidence correlation, safe redaction, dashboards, and trace reconstruction. |
| 42D-42N / 43 | AI agent lifecycle, tool gateway, memory/RAG integrity, red-team certification, incident response, policy catalog, and continuous improvement governance. |
| External Reference | Alignment Use |
| --- | --- |
| NIST SP 800-218 SSDF | Secure software development practices and evidence discipline for development lifecycle controls. |
| OWASP ASVS 5.0.0 | Application security verification requirements, authenticated testing, API security, and secure development expectations. |
| OpenTelemetry Semantic Conventions | Common names for traces, metrics, logs, resources, HTTP, database, messaging, and runtime telemetry attributes. |
| SLSA v1.2 | Software supply-chain provenance, build integrity, attestation, and progressive supply-chain hardening model. |

# 5. Execution Surface Decision Model

Use the execution surface below for every greenfield workstation action. The purpose is to prevent accidental delegation of privileged setup, source authority, repository mutation, approval, or promotion authority to an AI tool.
| Execution Surface | Use For | Do Not Use For |
| --- | --- | --- |
| ChatGPT Project | Source-aware setup guidance, AIRA governance interpretation, installation sequencing, checklist generation, evidence planning, risk/control decisions, prompt improvement. | Direct local file mutation, running commands, installing software, changing repo files, approving changes, or deploying. |
| Human-Executed OS/Admin Action | Windows security actions, account login, tool installation, running commands, accepting prompts, capturing screenshots, entering credentials. | Blindly executing AI-suggested commands without reading and understanding them. |
| Local Tool/CLI | Version checks, build/test, Git operations, Flyway validation, OPA tests, secret scan, SAST/SCA, SBOM, container scan, evidence capture. | Production mutation, direct production DB access, direct secrets access, or unapproved remote actions. |
| Codex in VS Code | Branch-bound file inspection, candidate generation, refactoring proposals, tests, documentation, and local validation after VS Code, Git, repo, AGENTS.md, CODEOWNERS, and evidence register exist. | Day 0 bootstrap before VS Code exists; production access; direct merge; deployment; disabling controls; approving own output. |
| Obsidian/Git | Curated Markdown projection of active AIRA sources, source register, evidence register, decisions, runbooks, prompts, and setup notes. | Uncontrolled source authority or storage of unmarked drafts as active baseline. |
| CI/CD / Repo Platform | Verification gates, PR/MR review, CODEOWNERS, scans, tests, evidence packs, merge protection, artifact proof. | Bypassing maker-checker review, CAB/ARB controls, or treating failed gates as advisory. |
| Harness / Agent Gateway | Future controlled tool-action execution after registry, SBAC, OPA, dry-run, audit, rollback, and approval rules exist. | Direct credential handoff to agents or unregistered MCP/tool actions. |
| Operating Rule ChatGPT guides. Humans execute privileged setup. Codex edits governed folders only. Local CLI validates. CI/CD verifies. GitNexus analyzes read-only. Humans approve. AVCI evidence records the path. |
| --- |

# 6. Greenfield Setup Principles and Non-Negotiables
| ID | Principle | Operational Meaning |
| --- | --- | --- |
| GF-01 | Secure before sign-in | Do not log in to ChatGPT, Git, Codex, repositories, cloud services, or password manager until Windows baseline hardening and browser update are complete. |
| GF-02 | ChatGPT Project first | Use the AIRA ChatGPT Project with active sources as the Day 0 setup advisor and governance interpreter. |
| GF-03 | Codex after VS Code and repo controls | Codex starts only after VS Code, Git, repository folder, AGENTS.md, CODEOWNERS, branch rules, PR/MR template, and evidence register exist. |
| GF-04 | No production credentials | Never store or use production credentials, real customer data, production database URLs, production tokens, or raw secrets on the workstation. |
| GF-05 | Source authority preserved | Tier-0 sources remain approved DOCX/PDF, Git, OpenKM/DMS, databases, workflow histories, security/evidence stores, and audit records. Obsidian and AI outputs are governed projections unless approved. |
| GF-06 | Configure first | Use MicroFunction runtime configuration, OpenAPI/AsyncAPI contracts, Flyway migrations, OPA policies, and templates before custom code. |
| GF-07 | Frontend is not authority | Dynamic Workspace frontend renders backend-approved components only and never owns final authorization, classification, or business authority. |
| GF-08 | Evidence before PoC | No PoC code generation until source/evidence registers, branch rules, PR/MR template, local validation, baseline tests, and evidence capture exist. |
| GF-09 | Fail-safe by default | If identity, policy, guardrails, audit, evidence, secrets, model gateway, or Harness controls are unavailable, protected actions stop. |
| GF-10 | Runtime toggles are governed | Diagnostic verbosity, telemetry sampling, AI panel activation, feature flags, and expensive debug signals may be adjusted only through source-controlled, audited, reversible configuration. |

## 6.1 Rejection Rules

Do not paste passwords, tokens, secrets, raw JWTs, customer data, private keys, Restricted documents, or unredacted logs into ChatGPT, Codex, Obsidian, screenshots, prompts, tests, or evidence notes.

Do not install unmanaged AI agents, MCP connectors, browser extensions, package managers, SDKs, or CLI tools outside approved tool registry and security review.

Do not create repository code or configuration before AGENTS.md, CODEOWNERS, PR/MR template, source register, evidence register, and branch model exist.

Do not create manual database objects. Greenfield databases must be created from Flyway migrations.

Do not allow frontend code to call unregistered endpoints, hold tokens in localStorage, embed authorization rules, or execute remote component scripts.

Do not allow MicroFunction business functions to call database, Kafka, Redis, OpenKM, OPA, Keycloak, model providers, audit store, or outbox directly. Use ports/adapters and framework envelopes.

Do not let GitNexus, Codex, Hermes, System Builder Lite, or any agent commit, approve, merge, deploy, mutate production, replace tests, or override human review.

# 7. Target Local Folder and Source Governance Model

Unless otherwise directed, the default working folder for the AIRA team is D:\ChatGPT Workspace. This folder is a controlled local workspace, not an authoritative source repository by itself. All durable source truth must remain in approved Git repositories, OpenKM/DMS, approved document registers, and evidence stores.
| Path | Purpose | Authority Treatment |
| --- | --- | --- |
| D:\ChatGPT Workspace\Local Git Repo\aira-platform | Primary local clone of AIRA platform repositories. | Working copy only; Git remote and protected branches remain source control authority. |
| D:\ChatGPT Workspace\AIRA Evidence | Local evidence staging folder for screenshots, command outputs, setup logs, validation reports, and PR evidence drafts. | Staging only until committed, uploaded, or registered in approved evidence store. |
| D:\ChatGPT Workspace\AIRA Sources | Local copies of approved AIRA source packs and revised documents for human/Codex reference. | Derivative local copy; must include source hash, version, and approval status. |
| D:\ChatGPT Workspace\Obsidian Vault | Git-managed curated knowledge projection, notes, registers, runbooks, prompts, and evidence summaries. | Authority only when linked to Tier-0 source or formally approved as canonical. |
| D:\ChatGPT Workspace\Tool Evidence | Version outputs, winget search results, installer checks, hashes, and local validation outputs. | Evidence staging; register entries required. |
| D:\ChatGPT Workspace\Sandbox | Temporary experiments, command trials, non-authoritative notes, and AI-generated drafts. | Not authoritative; must be cleaned or promoted through review. |
| # Copy-ready PowerShell folder bootstrap - run from Windows PowerShell as the workstation owner New-Item -ItemType Directory -Force -Path "D:\ChatGPT Workspace" \| Out-Null New-Item -ItemType Directory -Force -Path "D:\ChatGPT Workspace\Local Git Repo" \| Out-Null New-Item -ItemType Directory -Force -Path "D:\ChatGPT Workspace\AIRA Evidence" \| Out-Null New-Item -ItemType Directory -Force -Path "D:\ChatGPT Workspace\AIRA Sources" \| Out-Null New-Item -ItemType Directory -Force -Path "D:\ChatGPT Workspace\Obsidian Vault" \| Out-Null New-Item -ItemType Directory -Force -Path "D:\ChatGPT Workspace\Tool Evidence" \| Out-Null New-Item -ItemType Directory -Force -Path "D:\ChatGPT Workspace\Sandbox" \| Out-Null Get-ChildItem "D:\ChatGPT Workspace" \| Select-Object FullName \| Tee-Object -FilePath "D:\ChatGPT Workspace\AIRA Evidence\EV-039B-folder-bootstrap.txt" |
| --- |

# 8. End-to-End Procedure Overview
| Phase | Name | Outcome |
| --- | --- | --- |
| 0 | Pre-start readiness | Confirm owner, device, account, network, approval, source baseline, and no-production-data rule. |
| 1 | Secure Windows 11 baseline | Update OS/browser, harden account posture, enable security controls, and capture baseline evidence. |
| 2 | ChatGPT Project and active source bootstrap | Create/use AIRA Project, load active sources, confirm source hierarchy, and ask for setup guidance. |
| 3 | Local AIRA workspace, registers, and evidence | Create D:\ChatGPT Workspace folders, source register, evidence register, and activity ledger. |
| 4 | Core tools | Install from approved sources: Git, VS Code, Java, build tools, Node, Flyway, OPA, scanners, and capture versions. |
| 5 | Repository bootstrap | Clone repo, branch model, CODEOWNERS, PR template, AGENTS.md, baseline CI, local validation. |
| 6 | VS Code / Codex | Install approved extensions and Codex; load repository rules; enforce workspace-write and on-request approval. |
| 7 | Obsidian / LLM Wiki projection | Create Git-backed vault projection with metadata, active/candidate/superseded zones, and no full code copy. |
| 8 | Devcontainer validation | Validate reproducible Java/Node/toolchain/devcontainer setup and evidence outputs. |
| 9 | Dynamic Workspace readiness | Prepare frontend and backend-resolver readiness for policy-filtered, MicroFunction-backed workspace flows. |
| 10 | MicroFunction backend readiness | Prepare backend runtime assembly, canonical steps, OPA, Flyway, idempotency, audit, outbox, and tests. |
| 11 | API/eventing readiness | Prepare OpenAPI, AsyncAPI, Avro, CloudEvents, Kafka, schema evolution, DLQ/replay, and generated clients. |
| 12 | Observability/runtime toggles | Prepare Log4j2, OTel, Sentry, Loki, Tempo, Grafana, audit, evidence, safe telemetry toggles, and dashboards. |
| 13 | Security / DAST / secrets | Prepare OPA/SBAC, secure APIs, secrets hygiene, authenticated DAST, abuse cases, and remediation evidence. |
| 14 | Resilience lab | Prepare retry, duplicate, concurrency, heavy-load, cache-loss, outbox, DLQ, replay, and failure-injection tests. |
| 15 | AI DevSecOps boundary | Prepare Hermes/LiteLLM/guardrails/Harness/agent boundary as advisory, registry-backed, SBAC/OPA-controlled. |
| 16 | Improvement loop readiness | Prepare Auto-Heal/Auto-Learn/Auto-Improve candidate flow: detect, retrieve evidence, propose, test, approve. |
| 17 | First PR/MR and go/no-go | Run first governed PR with evidence pack and decide whether PoC work may start. |

# 9. Phase 0 - Pre-Start Readiness
| Field | Required Content |
| --- | --- |
| Execution Surface | ChatGPT Project + Human Owner + Security/DevSecOps review |
| Objective | Confirm that the workstation build has accountable ownership, approved account path, device authorization, baseline sources, and no prohibited data. |
| Exit Gate | Proceed only when owner, reviewer, source baseline, device authorization, and data-handling controls are clear. |
| Minimum Evidence | Signed acknowledgement or team approval note; source baseline reference; no-production-data statement; initial evidence record. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 0.1 | Assign workstation owner, checker, and DevSecOps reviewer. | Owner/checker recorded in evidence register. |
| 0.2 | Confirm device is company-approved, patched, encrypted where required, and permitted for AIRA work. | Device readiness note. |
| 0.3 | Confirm no production credentials, production database, raw customer data, or Restricted artifacts will be stored locally. | No-production-data acknowledgement. |
| 0.4 | Confirm current active source baseline and known reconciliation items. | Source baseline note and conflict register seed. |
| 0.5 | Create initial activity ledger entry before installing or configuring tools. | EV-039B-0000 activity ledger entry. |

# 10. Phase 1 - Secure Windows 11 Baseline
| Field | Required Content |
| --- | --- |
| Execution Surface | Human-Executed OS/Admin Action guided by ChatGPT Project |
| Objective | Create a secure endpoint baseline before signing in to AI, Git, repository, cloud, or development accounts. |
| Exit Gate | Proceed only when workstation security is acceptable and evidence is captured. |
| Minimum Evidence | Windows update evidence; endpoint security status; browser version; systeminfo; activity ledger entry. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 1.1 | Run Windows Update and reboot until no critical updates remain. | Windows Update screenshot or export. |
| 1.2 | Confirm Microsoft Defender or approved endpoint security is active. | Security status screenshot. |
| 1.3 | Confirm browser update, password manager policy, MFA availability, and corporate Wi-Fi/VPN posture. | Browser/security evidence. |
| 1.4 | Configure account lock, screen timeout, local admin use restriction, and approved firewall/network posture. | Security baseline checklist. |
| 1.5 | Capture system information and timezone. | systeminfo output and timestamp. |
| # Phase 1 evidence commands - run from Windows PowerShell New-Item -ItemType Directory -Force -Path "D:\ChatGPT Workspace\AIRA Evidence\Phase-01" \| Out-Null Get-ComputerInfo \| Out-File "D:\ChatGPT Workspace\AIRA Evidence\Phase-01\computer-info.txt" Get-TimeZone \| Out-File "D:\ChatGPT Workspace\AIRA Evidence\Phase-01\timezone.txt" Get-MpComputerStatus \| Out-File "D:\ChatGPT Workspace\AIRA Evidence\Phase-01\defender-status.txt" winget --version \| Out-File "D:\ChatGPT Workspace\AIRA Evidence\Phase-01\winget-version.txt" |
| --- |

# 11. Phase 2 - ChatGPT Project and Active Source Bootstrap
| Field | Required Content |
| --- | --- |
| Execution Surface | ChatGPT Project + Human-Executed Account Action |
| Objective | Create or use the AIRA ChatGPT Project as the Day 0 source-aware advisor without giving it authority over local commands, credentials, Git operations, or approvals. |
| Exit Gate | Proceed only when active source context is loaded, classification is understood, and ChatGPT is limited to advisory guidance. |
| Minimum Evidence | Project source list; prompt/response summary; assumptions register; evidence register entry. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 2.1 | Log in using the approved ChatGPT workspace/account only after Phase 1 gate passes. | Workspace/account path recorded; no password captured. |
| 2.2 | Upload or reference active AIRA source packs and latest revised documents, including 09 v3.2 and this 39B v1.3 when approved. | Project source list. |
| 2.3 | Ask ChatGPT to confirm active source hierarchy, known conflicts, and setup sequence. | ChatGPT setup guidance summary. |
| 2.4 | Record assumptions, gaps, and documents requiring future regeneration. | Reconciliation backlog seed. |
| 2.5 | Do not ask ChatGPT to run commands, enter credentials, install software, or approve outputs. | AI boundary acknowledgement. |

# 12. Phase 3 - Local AIRA Workspace, Registers, and Evidence
| Field | Required Content |
| --- | --- |
| Execution Surface | Human-Executed OS Action + Local Tool/CLI + Obsidian/Git later |
| Objective | Create the local folder structure, source register, evidence register, activity ledger, and tool registry before installing the full toolchain or using Codex. |
| Exit Gate | Proceed only when registers exist and will be updated for each subsequent phase. |
| Minimum Evidence | Folder tree; source register; evidence register; tool registry; activity ledger. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 3.1 | Create D:\ChatGPT Workspace folder tree. | Folder tree output. |
| 3.2 | Create SOURCE_REGISTER.md with document ID, filename, version, classification, source path, retrieval eligibility, and supersedence fields. | Source register draft. |
| 3.3 | Create EVIDENCE_REGISTER.md with evidence ID, date/time, phase, action, owner, path, validation, classification, and follow-up. | Evidence register draft. |
| 3.4 | Create TOOL_REGISTRY.md with tool, source, version, install method, owner, approval, license, and evidence fields. | Tool registry draft. |
| 3.5 | Create ACTIVITY_LEDGER.md for all setup actions, AI usage, command outputs, decisions, and gaps. | Activity ledger initialized. |

# 13. Phase 4 - Install Core Workstation Tools
| Field | Required Content |
| --- | --- |
| Execution Surface | ChatGPT-guided and Human-Executed OS/Admin Action |
| Objective | Install only approved tools from verified sources and capture version evidence. Package IDs must be searched and confirmed before installation. |
| Exit Gate | Proceed only when core tools are installed from approved sources and version evidence is captured. |
| Minimum Evidence | Version outputs; tool registry; winget search evidence; scanner versions; exceptions/waivers if any. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 4.1 | Ask ChatGPT Project for approved tool installation sequence and risk notes. | Tool install plan in TOOL_REGISTRY.md. |
| 4.2 | Verify winget/package source or approved installer. Use search before install when package IDs are uncertain. | winget search/version evidence. |
| 4.3 | Install Git, GitHub CLI or GitLab CLI, VS Code, Windows Terminal/PowerShell updates where approved. | Version evidence. |
| 4.4 | Install Java 25 target baseline or approved vendor path. Java 21 is waiver-only compatibility fallback. | java --version and waiver note if needed. |
| 4.5 | Install Maven/Gradle according to repo standard. | mvn/gradle version evidence. |
| 4.6 | Install Node.js LTS, npm, and pnpm according to frontend standard. | node/npm/pnpm version evidence. |
| 4.7 | Install Flyway CLI, OPA CLI, gitleaks, Syft, Trivy, Cosign, Semgrep, or approved equivalents as required. | Version evidence and tool registry entries. |
| 4.8 | Do not install AI agents, MCP connectors, runtime AI gateways, or unapproved browser/IDE plugins yet. | No unauthorized tools acknowledgement. |
| # Phase 4 evidence command pattern - validate package IDs before install Set-Location "D:\ChatGPT Workspace" New-Item -ItemType Directory -Force -Path ".\AIRA Evidence\Phase-04" \| Out-Null winget --version \| Tee-Object -FilePath ".\AIRA Evidence\Phase-04\winget-version.txt" winget search Git \| Tee-Object -FilePath ".\AIRA Evidence\Phase-04\winget-search-git.txt" winget search "Visual Studio Code" \| Tee-Object -FilePath ".\AIRA Evidence\Phase-04\winget-search-vscode.txt" winget search "GitHub CLI" \| Tee-Object -FilePath ".\AIRA Evidence\Phase-04\winget-search-gh.txt" winget search "Node.js" \| Tee-Object -FilePath ".\AIRA Evidence\Phase-04\winget-search-node.txt" winget search "OpenJDK" \| Tee-Object -FilePath ".\AIRA Evidence\Phase-04\winget-search-openjdk.txt" # Example version evidence after approved installation git --version \| Tee-Object -FilePath ".\AIRA Evidence\Phase-04\git-version.txt" gh --version \| Tee-Object -FilePath ".\AIRA Evidence\Phase-04\gh-version.txt" code --version \| Tee-Object -FilePath ".\AIRA Evidence\Phase-04\vscode-version.txt" java --version 2>&1 \| Tee-Object -FilePath ".\AIRA Evidence\Phase-04\java-version.txt" mvn --version 2>&1 \| Tee-Object -FilePath ".\AIRA Evidence\Phase-04\maven-version.txt" gradle --version 2>&1 \| Tee-Object -FilePath ".\AIRA Evidence\Phase-04\gradle-version.txt" node --version \| Tee-Object -FilePath ".\AIRA Evidence\Phase-04\node-version.txt" npm --version \| Tee-Object -FilePath ".\AIRA Evidence\Phase-04\npm-version.txt" pnpm --version \| Tee-Object -FilePath ".\AIRA Evidence\Phase-04\pnpm-version.txt" flyway -v 2>&1 \| Tee-Object -FilePath ".\AIRA Evidence\Phase-04\flyway-version.txt" opa version \| Tee-Object -FilePath ".\AIRA Evidence\Phase-04\opa-version.txt" gitleaks version 2>&1 \| Tee-Object -FilePath ".\AIRA Evidence\Phase-04\gitleaks-version.txt" trivy --version 2>&1 \| Tee-Object -FilePath ".\AIRA Evidence\Phase-04\trivy-version.txt" syft version 2>&1 \| Tee-Object -FilePath ".\AIRA Evidence\Phase-04\syft-version.txt" cosign version 2>&1 \| Tee-Object -FilePath ".\AIRA Evidence\Phase-04\cosign-version.txt" semgrep --version 2>&1 \| Tee-Object -FilePath ".\AIRA Evidence\Phase-04\semgrep-version.txt" |
| --- |

# 14. Phase 5 - Repository Bootstrap and System Builder Lite Guardrails
| Field | Required Content |
| --- | --- |
| Execution Surface | Local Tool/CLI + Repo Platform + Human Reviewer |
| Objective | Create the governed repository runway before Codex generates or modifies code. |
| Exit Gate | Proceed only when repository governance exists and first governance PR/MR can prove controls without feature code. |
| Minimum Evidence | CODEOWNERS; PR template; AGENTS.md; branch protection; evidence register; initial PR/MR evidence. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 5.1 | Clone the approved repository into D:\ChatGPT Workspace\Local Git Repo. | Clone evidence and remote URL check. |
| 5.2 | Create or verify protected branch rules, branch naming, CODEOWNERS, PR/MR template, issue/backlog labels, and signed commit/artifact policy where available. | Repository settings evidence. |
| 5.3 | Create or update AGENTS.md from approved AIRA instructions. | AGENTS.md committed in branch. |
| 5.4 | Create docs/aira-active-source-index.md, docs/aira-evidence-register.md, docs/aira-tool-registry.md, docs/aira-activity-ledger.md. | Repository governance files. |
| 5.5 | Add local validation scripts for build, tests, OPA, Flyway, secrets, SAST/SCA, format, architecture, and evidence lint where practical. | Validation script output. |
| 5.6 | Open an initial governance PR/MR with no application feature code. | PR/MR evidence pack. |
| # Phase 5 repository command pattern - replace <repo-url> with approved remote only Set-Location "D:\ChatGPT Workspace\Local Git Repo" git clone <repo-url> aira-platform Set-Location "D:\ChatGPT Workspace\Local Git Repo\aira-platform" git remote -v \| Tee-Object -FilePath "D:\ChatGPT Workspace\AIRA Evidence\Phase-05\git-remote.txt" git status \| Tee-Object -FilePath "D:\ChatGPT Workspace\AIRA Evidence\Phase-05\git-status-initial.txt" git checkout -b chore/039b-greenfield-governance-baseline New-Item -ItemType Directory -Force -Path ".\docs" \| Out-Null New-Item -ItemType Directory -Force -Path ".\evidence" \| Out-Null |
| --- |

# 15. Phase 6 - VS Code, Codex, and AI-Assisted Developer Controls
| Field | Required Content |
| --- | --- |
| Execution Surface | VS Code + Codex in governed repository + Human Reviewer |
| Objective | Enable Codex only after repository and evidence controls exist. Codex is a candidate artifact generator, reviewer assistant, and local analysis helper, not an approver or production actor. |
| Exit Gate | Proceed only when Codex can demonstrate it respects AGENTS.md, branch boundaries, evidence updates, tests, and human review. |
| Minimum Evidence | VS Code extension list; Codex config; AI-use declaration; boundary summary; test PR/MR evidence. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 6.1 | Open only the governed repository folder in VS Code. | VS Code workspace evidence. |
| 6.2 | Install approved VS Code extensions only; record extension list. | Extension list evidence. |
| 6.3 | Install/enable Codex according to approved workspace/account policy. | Codex availability evidence; no secrets shown. |
| 6.4 | Configure Codex conservative settings: workspace-write only, on-request approval, no production credentials, and AGENTS.md as primary project rule. | Codex config evidence. |
| 6.5 | Ask Codex to read AGENTS.md and summarize boundaries before any file change. | Boundary summary saved. |
| 6.6 | Test Codex with documentation-only change or local validation script improvement, not product feature code. | Sandbox PR/MR or branch evidence. |

# 16. Phase 7 - Obsidian, LLM Wiki Projection, and Knowledge Control Readiness
| Field | Required Content |
| --- | --- |
| Execution Surface | Obsidian/Git + Knowledge Steward + ChatGPT/Codex guidance |
| Objective | Create the local curated knowledge projection without turning Obsidian or AI summaries into uncontrolled authority. |
| Exit Gate | Proceed only when knowledge projections are classified, source-cited, reviewable, and not treated as stronger authority than Tier-0 sources. |
| Minimum Evidence | Vault commit/hash; metadata template; source register; conflict register; indexing readiness evidence. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 7.1 | Create Git-backed Obsidian vault structure: active baseline, candidates, evidence, ADR/TDL, runbooks, prompts, superseded, quarantine. | Vault folder evidence. |
| 7.2 | Add mandatory YAML metadata for document_id, version, status, owner, classification, source_tier, source_hash, retrieval_eligible, model_route_allowed, evidence_ref. | Metadata template. |
| 7.3 | Project only approved/current source summaries and source references. Do not copy full codebase into Obsidian. | Projection policy note. |
| 7.4 | Create freshness/conflict register for older, duplicate, or superseded sources. | Conflict register. |
| 7.5 | Prepare LLM Wiki/LightRAG indexing only after review and classification filters exist. | Indexing readiness note. |

# 17. Phase 8 - Devcontainer and Toolchain Reproducibility Validation
| Field | Required Content |
| --- | --- |
| Execution Surface | Local Tool/CLI + CI/CD / Repo Platform |
| Objective | Prove that the workstation can reproduce the approved toolchain locally and through CI where available. |
| Exit Gate | Proceed only when local and CI evidence agree or deviations are formally recorded. |
| Minimum Evidence | Toolchain manifest; local validation output; CI run; SBOM/scan where available; waiver record. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 8.1 | Create or verify devcontainer baseline for backend/frontend/toolchain. | devcontainer JSON evidence. |
| 8.2 | Pin Java/toolchain, Node, package manager, build image, scanner versions, and dependency lock files. | Toolchain manifest. |
| 8.3 | Run sample build/test/scan locally. | Local validation report. |
| 8.4 | Run matching CI pipeline on initial PR/MR. | CI evidence pack. |
| 8.5 | Record any deviation as waiver with owner, risk, compensating control, and exit date. | Waiver record if needed. |

# 18. Phase 9 - Dynamic Workspace and Frontend UX Readiness
| Field | Required Content |
| --- | --- |
| Execution Surface | VS Code/Codex + Local Tool/CLI + CI/CD + UX/Security review |
| Objective | Prepare the workstation to implement Dynamic Workspace safely: frontend renders approved components; backend authorizes; MicroFunctions execute; PostgreSQL defines truth; Redis/Valkey accelerates only. |
| Exit Gate | Proceed only when frontend workspace work can be tested against backend authority and policy filtering. |
| Minimum Evidence | Typecheck/lint/test output; Playwright baseline; accessibility evidence; generated-client readiness; policy-denial test plan. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 9.1 | Verify frontend baseline: Next.js/React/TypeScript, package manager, lint, typecheck, unit/component test, Playwright, accessibility tooling. | Frontend tool evidence. |
| 9.2 | Create generated-client readiness for OpenAPI contracts. | Generated client test or placeholder. |
| 9.3 | Create component registry and workspace schema validation placeholders. | Schema validation evidence. |
| 9.4 | Prepare tests for backend-filtered layout, denied components, safe field visibility, token safety, accessibility, visual regression, and policy-denial path. | Test plan/evidence. |
| 9.5 | Confirm frontend has no direct DB, OPA bypass, model provider calls, unregistered endpoints, business authorization logic, or localStorage token usage. | Architecture/security check. |

# 19. Phase 10 - MicroFunction Backend and Runtime Assembly Readiness
| Field | Required Content |
| --- | --- |
| Execution Surface | VS Code/Codex + Local Tool/CLI + DBA/Security/Architecture review |
| Objective | Prepare backend development to implement configuration-first MicroFunction runtime assembly with mandatory security, observability, audit, outbox, idempotency, error handling, and rollback. |
| Exit Gate | Proceed only when backend development can prove MicroFunction boundaries before feature generation. |
| Minimum Evidence | Java/build evidence; Flyway clean-migrate; OPA tests; ArchUnit/Semgrep; idempotency/outbox/audit tests; fail-closed test plan. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 10.1 | Verify backend baseline: Java 25 target, Spring, build tool, test framework, ArchUnit/Semgrep boundary checks, OPA tests, Flyway tests, Testcontainers. | Backend tool evidence. |
| 10.2 | Prepare canonical schema naming: aira_mf, aira_cfg, aira_auth, aira_audit, aira_policy, aira_outbox, aira_ui where applicable. | Schema naming checklist. |
| 10.3 | Prepare MicroFunction standard step validation and STP-BUS direct-dependency rejection. | Architecture test evidence. |
| 10.4 | Prepare audit/outbox/idempotency registry test scaffolds. | Test scaffold evidence. |
| 10.5 | Prepare negative tests for missing Keycloak, OPA, Vault/secrets, audit, DB, runtime config, policy, and evidence controls. | Fail-closed test plan. |

# 20. Phase 11 - API, Eventing, Kafka, Avro, CloudEvents, Outbox, DLQ, and Replay Readiness
| Field | Required Content |
| --- | --- |
| Execution Surface | Local Tool/CLI + Codex + CI/CD + API/Event owner review |
| Objective | Prepare the workstation and repository for contract-first APIs and event-driven integration without hidden contract drift. |
| Exit Gate | Proceed only when API/event contracts can be validated locally and in CI before implementation. |
| Minimum Evidence | OpenAPI lint; AsyncAPI/schema lint; generated client evidence; event replay test plan; outbox/idempotency test evidence. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 11.1 | Create/verify contracts folder for OpenAPI, AsyncAPI, Avro/JSON schemas, CloudEvents examples, error contracts, and idempotency profiles. | Contract folder evidence. |
| 11.2 | Prepare OpenAPI lint, compatibility, generated client/server stubs or mock validation. | OpenAPI validation output. |
| 11.3 | Prepare AsyncAPI/Kafka topic/event conventions: event type, source, subject, trace_id, correlation_id, causation_id, idempotency key, schema version. | AsyncAPI/schema evidence. |
| 11.4 | Prepare transactional outbox, inbox/idempotent consumer, retry, DLQ, replay, and schema evolution test scaffolds. | Eventing test plan. |
| 11.5 | Reject direct Kafka publishing from business MicroFunctions; event publishing must go through approved outbox/adapters. | Architecture fitness rule. |

# 21. Phase 12 - Observability, Audit, Evidence, Runtime Toggle, and Dashboard Readiness
| Field | Required Content |
| --- | --- |
| Execution Surface | Local Tool/CLI + SRE/DevSecOps review + CI/CD |
| Objective | Prepare safe telemetry, trace reconstruction, audit evidence, and governed runtime toggles before high-volume feature development. |
| Exit Gate | Proceed only when observability is built into the development workflow and runtime flexibility cannot disable mandatory audit/security evidence. |
| Minimum Evidence | Log redaction; OTel trace; dashboard placeholder; toggle catalog; audit/event schema; evidence correlation test plan. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 12.1 | Prepare Log4j2 structured logging with redaction tests and no secrets/raw PII/raw prompts/raw documents. | Log redaction test. |
| 12.2 | Prepare OpenTelemetry trace/metric/log propagation for frontend, gateway, backend, MicroFunction, DB, Kafka, AI gateway, and audit evidence. | OTel test/export evidence. |
| 12.3 | Prepare Sentry, Loki, Tempo, Grafana dashboard/export placeholders for dev/test. | Dashboard readiness evidence. |
| 12.4 | Define runtime toggle catalog for telemetry sampling, diagnostic verbosity, feature flags, AI panel, workspace telemetry, and expensive debug probes. | Toggle catalog draft. |
| 12.5 | Mark minimum audit/security/policy/evidence signals as non-disableable unless break-glass is approved, logged, time-bound, and reviewed. | Toggle policy evidence. |

# 22. Phase 13 - Security, OPA/SBAC, Abuse Cases, Authenticated DAST, Secure APIs, and Secrets Hygiene
| Field | Required Content |
| --- | --- |
| Execution Surface | Security + Local Tool/CLI + CI/CD + Human Checker |
| Objective | Prepare the workstation for secure-by-design implementation and security verification from the first PR/MR. |
| Exit Gate | Proceed only when security tests and secrets hygiene can block unsafe work before merge. |
| Minimum Evidence | Secret scan; OPA tests; DAST plan; abuse cases; remediation evidence; security reviewer assignment. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 13.1 | Create local security baseline: no secrets in Git, prompts, screenshots, logs, tests, Obsidian, or evidence notes. | Secret hygiene acknowledgement. |
| 13.2 | Prepare OPA/Rego tests for RBAC/ABAC/SBAC, classification, allow/deny, require-approval, fail-closed, and policy-denial evidence. | OPA test evidence. |
| 13.3 | Prepare authenticated DAST scope using synthetic users and non-prod endpoints only. | DAST scope and test account evidence. |
| 13.4 | Prepare abuse-case checklist for login, workspace actions, APIs, AI prompts, retrieval, file upload, DLQ/replay, and admin actions. | Abuse-case checklist. |
| 13.5 | Prepare remediation evidence workflow: finding, severity, owner, fix candidate, test, scan rerun, waiver, or closure. | Remediation evidence template. |

# 23. Phase 14 - Concurrency, Heavy Transaction, Idempotency, and Resilience Lab Readiness
| Field | Required Content |
| --- | --- |
| Execution Surface | QA/SDET + DevSecOps + Backend + Local Tool/CLI |
| Objective | Prepare the workstation and repository to test retry-safe, duplicate-safe, concurrent, heavy-load, and failure-aware behavior before business modules depend on it. |
| Exit Gate | Proceed only when the team can prove failure-aware transaction behavior locally and in CI-ready test paths. |
| Minimum Evidence | Resilience lab plan; test fixtures; failure injection results where available; known limitations and backlog. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 14.1 | Prepare Testcontainers or approved equivalent for PostgreSQL, Kafka, Redis/Valkey, OPA, and service dependencies where practical. | Testcontainers readiness. |
| 14.2 | Prepare idempotency and duplicate request tests for REST callbacks, event consumers, workflow signals, and approval actions. | Idempotency test evidence. |
| 14.3 | Prepare outbox/replay/DLQ tests including duplicate event, poison message, schema evolution, retry exhaustion, and replay with idempotent consumers. | DLQ/replay test plan. |
| 14.4 | Prepare concurrency tests for optimistic locking, row contention, idempotency registry race, cache invalidation, and approval double-submit. | Concurrency test plan. |
| 14.5 | Prepare failure-injection tests: DB unavailable, OPA unavailable, Kafka unavailable, cache unavailable, model gateway unavailable, audit store unavailable. | Resilience test plan. |

# 24. Phase 15 - AI DevSecOps, Hermes, LiteLLM, Guardrails, Harness, and Agent Boundary Readiness
| Field | Required Content |
| --- | --- |
| Execution Surface | AI Governance + Security + DevSecOps + Codex/Hermes in sandbox only |
| Objective | Prepare AI-assisted development without direct model-provider calls, uncontrolled agents, production credentials, or unsafe tool actions. |
| Exit Gate | Proceed only when AI tooling remains advisory/candidate-producing unless registry, SBAC, OPA, guardrails, Harness, evidence, and human approval allow limited action. |
| Minimum Evidence | Model route evidence; guardrail checklist; agent registry candidate; AI-use declaration; tool action denial test plan. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 15.1 | Confirm all model access routes through approved LiteLLM or private/on-prem gateway aliases where AIRA application/runtime code is involved. | Model route policy note. |
| 15.2 | Prepare guardrail checkpoints for input, retrieval, execution/tool action, and output where AI workflows are used. | Guardrail checklist. |
| 15.3 | Prepare agent/tool registry draft: purpose, owner, skills, tools, SBAC scope, OPA policy, trust tier, environment, rollback, and monitoring. | Agent registry candidate. |
| 15.4 | Prepare Harness/tool gateway boundary for action requests; agents must not receive direct Git, CI/CD, Kubernetes, DB, workflow, model, or production credentials. | Harness boundary note. |
| 15.5 | Prepare AI usage declaration in PR/MR evidence: prompt intent, model route, sources, generated files, tests, limitations, reviewer. | AI-use evidence template. |

# 25. Phase 16 - Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop Readiness
| Field | Required Content |
| --- | --- |
| Execution Surface | System Builder Lite + SRE/DevSecOps + Human Approval |
| Objective | Prepare continuous improvement as a proposal-driven, evidence-backed loop, not autonomous production mutation. |
| Exit Gate | Proceed only when improvement loops can produce proposals, tests, PR/MR evidence, and approval routes without self-promotion. |
| Minimum Evidence | Improvement intake template; candidate loop; GitNexus placeholder; knowledge candidate workflow; silent mutation rejection rules. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 16.1 | Create improvement intake record for issues, logs, traces, metrics, test failures, security scans, CI/CD evidence, screenshots, incidents, and feedback. | Improvement intake template. |
| 16.2 | Define candidate loop: issue detection, evidence retrieval, root-cause hypothesis, candidate fix/learning proposal, tests, impact analysis, rollback, and human approval. | Candidate loop template. |
| 16.3 | Prepare GitNexus read-only impact analysis use for affected files, tests, architecture drift, and blast radius. | GitNexus evidence placeholder. |
| 16.4 | Prepare Auto-Learn knowledge candidate zone in Obsidian/LLM Wiki. Candidates are not retrievable as active baseline until reviewed. | Knowledge candidate workflow. |
| 16.5 | Prepare denial rules for silent mutation of code, config, prompts, guardrails, model routes, policies, database, environments, MicroFunction catalogs, agents, or runtime toggles. | Prohibited mutation checklist. |

# 26. Phase 17 - First PR/MR, Evidence Pack, and Go/No-Go Gate
| Field | Required Content |
| --- | --- |
| Execution Surface | CI/CD / Repo Platform + Human Maker-Checker + Architecture/Security/DevSecOps review |
| Objective | Run the first controlled governance PR/MR to prove the workstation and System Builder Lite path before PoC code generation begins. |
| Exit Gate | PoC work starts only if Go/Conditional Go is approved with named conditions and evidence. |
| Minimum Evidence | PR/MR; evidence pack; review approvals; go/no-go decision; improvement backlog. |
| Step | Action | Output / Evidence |
| --- | --- | --- |
| 17.1 | Create a PR/MR that adds/updates governance files only: AGENTS.md, CODEOWNERS, PR template, source index, evidence register, tool registry, validation checklist. | Initial governance PR/MR. |
| 17.2 | Run local validation and CI gates available at this phase: format, tests, OPA, Flyway dry-run where applicable, secret scan, SAST/SCA/SBOM where available. | Validation evidence. |
| 17.3 | Attach evidence pack: tool versions, source baseline, security baseline, AI-use declaration, test/scan outputs, known gaps, rollback plan. | Evidence pack. |
| 17.4 | Review by owner, checker, DevSecOps, Security, Architecture, QA/SDET, DBA/SRE as applicable. | Review record. |
| 17.5 | Approve, conditionally approve, defer, or reject PoC readiness. | Go/No-Go decision. |

# 27. RACI and Separation of Duties
| Activity | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Workstation ownership and setup execution | Workstation Owner | IT Head / Solutions Architecture Office | Security, DevSecOps | Development Team |
| Windows security baseline | Workstation Owner / System Administrator | Security Architecture | DevSecOps, Infra | Internal Audit |
| ChatGPT Project source bootstrap | Solutions Architect / Knowledge Steward | IT Head | AI Governance, Security | Team |
| Tool installation and validation | Workstation Owner / DevSecOps | DevSecOps Lead | Security, Platform | Team |
| Repository governance bootstrap | DevSecOps / Development Lead | Solutions Architecture Office | Security, QA/SDET | Team |
| Codex enablement | Developer / DevSecOps | AI Governance + Development Lead | Security, Architecture | Team |
| Dynamic Workspace readiness | Frontend Lead | Solutions Architecture Office | Security, QA/SDET, Backend Lead | Product Owner |
| MicroFunction readiness | Backend Lead | Solutions Architecture Office | DBA, Security, QA/SDET | Product Owner |
| Security/DAST/OPA/SBAC readiness | Security Architecture | Security Governance | DevSecOps, QA/SDET | Internal Audit |
| Go/No-Go decision | Architecture/Security/DevSecOps reviewers | IT Head / ARB delegate | QA/SDET, DBA, SRE | Team |

# 28. Acceptance Criteria
| ID | Acceptance Criterion |
| --- | --- |
| AC-01 | Windows baseline is patched, secured, and evidenced before sign-in to AIRA AI/repository services. |
| AC-02 | ChatGPT Project contains or references the active AIRA source baseline and is limited to advisory guidance. |
| AC-03 | D:\ChatGPT Workspace folder model, source register, evidence register, tool registry, and activity ledger exist. |
| AC-04 | Core tools are installed from approved sources and version evidence is captured. |
| AC-05 | Repository has AGENTS.md, CODEOWNERS, PR/MR template, branch naming, evidence path, and baseline validation controls. |
| AC-06 | Codex is enabled only inside governed VS Code workspace with conservative permissions and no production credentials. |
| AC-07 | Obsidian projection is source-cited, classified, Git-managed, and does not copy the full codebase or treat AI summaries as Tier-0 truth. |
| AC-08 | Devcontainer/toolchain can reproduce Java/Node/build/test/scanner baseline locally and in CI where available. |
| AC-09 | Dynamic Workspace frontend readiness includes generated clients, backend authority, OPA-denial tests, accessibility, Playwright, and no frontend authorization authority. |
| AC-10 | MicroFunction backend readiness includes Flyway, OPA, idempotency, audit, outbox, OpenTelemetry, canonical steps, and architecture fitness tests. |
| AC-11 | OpenAPI/AsyncAPI/Kafka/Avro/CloudEvents/outbox/DLQ/replay readiness is present or explicitly deferred with owner and date. |
| AC-12 | Log4j2, OpenTelemetry, Sentry/Loki/Tempo/Grafana readiness and safe runtime telemetry toggle model are documented. |
| AC-13 | OPA/SBAC, secrets hygiene, abuse cases, authenticated DAST scope, and remediation evidence workflow are ready. |
| AC-14 | Resilience lab plan covers retries, duplicates, concurrency, heavy transactions, cache loss, outbox, DLQ, replay, and fail-closed dependencies. |
| AC-15 | Auto-Heal/Auto-Learn/Auto-Improve loop is candidate-only and cannot silently mutate production or canonical sources. |
| AC-16 | Initial governance PR/MR produces AVCI evidence and receives Go/Conditional Go before PoC code generation. |

# 29. Cross-Document Reconciliation and Regeneration Candidates
| Item | Gap / Risk | Recommended Action |
| --- | --- | --- |
| Runtime telemetry toggles | Partially covered across observability and workspace docs; v1.3 adds workstation/runtime setup governance. | Track for future strengthening in 31A, 46, 53, and runtime configuration standards. |
| 39A / 39B / 39C overlap | 39B now becomes execution guide for one workstation; 39C should govern team rollout; 39A should govern VS Code/Codex details. | Update 39C next, then 39A. |
| Dynamic Workspace vs System Builder numbering overlap | 41B/44/61 references remain active/reconciliation-prone. | Keep as AVCI reconciliation item; governing register 00D should decide canonical numbering. |
| Java 25 fallback handling | Java 25 remains target baseline; Java 21 fallback is waiver-only if tool availability blocks execution. | Record waiver with owner, risk, compensating controls, and exit date. |
| Authenticated DAST tooling | Tool may vary by approved stack; ZAP or equivalent must be scoped to synthetic users/non-prod only. | Security to confirm tool choice before blocking CI gate. |
| GitNexus maturity | GitNexus remains read-only derivative and may begin as advisory before becoming CI gate. | Track adoption maturity and evidence schema readiness. |
| Auto-Heal loop | Must remain proposal-driven, not autonomous repair. | Regenerate operations/runbook docs later if implementation details change. |

# 30. Risk and Control Register
| Risk ID | Risk | Impact | Controls |
| --- | --- | --- | --- |
| R-039B-01 | AI tool receives excessive authority | Direct code/production mutation or approval bypass | Codex after repo controls; workspace-write; on-request approval; no production credentials; human checker. |
| R-039B-02 | Secrets leak into prompts/logs/screenshots | Credential exposure and compliance failure | No secrets in prompts/logs/docs/tests; secret scans; redaction tests; password manager policy. |
| R-039B-03 | Toolchain drift | Non-reproducible builds and support issues | Tool registry, pinned versions, devcontainer, CI evidence, waiver process. |
| R-039B-04 | Obsidian becomes uncontrolled authority | Stale or draft knowledge influences code | Tier-0 hierarchy, metadata, retrieval eligibility, candidate/quarantine/superseded zones. |
| R-039B-05 | Frontend becomes authorization authority | Data leakage and policy bypass | Backend-filtered workspace definitions, OPA/SBAC, denied component tests, no frontend role rules. |
| R-039B-06 | MicroFunctions bypass ports/adapters | Architecture drift and untestable business logic | Architecture fitness, Semgrep/ArchUnit, standard step envelope, no direct DB/Kafka/Redis/model calls. |
| R-039B-07 | Observability disabled for performance | Loss of audit and trace reconstruction | Governed toggles, non-disableable audit/security minimums, sampling not removal. |
| R-039B-08 | Auto-Heal self-mutates production | Unreviewed destructive change | Candidate-only loop, PR/MR, tests, evidence, approval, rollback, CAB/ARB where required. |

# 31. AVCI Compliance Summary
| AVCI Property | Evidence in this Guide |
| --- | --- |
| Attributable | Defines document owner, co-owners, execution surfaces, workstation owner, checker, reviewers, source baseline, tool registry, AI-use declaration, and PR/MR ownership evidence. |
| Verifiable | Requires rendered tool/version outputs, Windows baseline evidence, repository settings, local validation, CI/CD evidence, tests, scans, OPA/Flyway checks, observability proof, DAST scope, resilience tests, and go/no-go records. |
| Classifiable | Classifies workstation artifacts, prompts, logs, evidence, source projections, tool outputs, AI usage records, telemetry, screenshots, and knowledge projections as governed AIRA artifacts with no production secrets/customer data. |
| Improvable | Creates activity ledger, known gaps, reconciliation register, tool registry, source freshness/conflict register, Auto-Heal/Auto-Learn/Auto-Improve candidate loop, and future regeneration candidates. |

# Appendix A - Copy-Ready Windows PowerShell Command Baseline
| Execution Warning These commands are examples for controlled workstation setup. The human executor must verify package IDs, publishers, licenses, versions, network destination, and company approval before running installation commands. Do not paste credentials or secrets into commands, screenshots, ChatGPT, or Codex. |
| --- |
| # AIRA 39B v1.3 - Workstation baseline folders and evidence paths Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force $Root = "D:\ChatGPT Workspace" $Evidence = Join-Path $Root "AIRA Evidence" $ToolEvidence = Join-Path $Root "Tool Evidence" $RepoRoot = Join-Path $Root "Local Git Repo" $Sources = Join-Path $Root "AIRA Sources" $Vault = Join-Path $Root "Obsidian Vault" $Sandbox = Join-Path $Root "Sandbox" @($Root,$Evidence,$ToolEvidence,$RepoRoot,$Sources,$Vault,$Sandbox) \| ForEach-Object { New-Item -ItemType Directory -Force -Path $_ \| Out-Null } Get-ChildItem $Root \| Select-Object FullName \| Tee-Object -FilePath (Join-Path $Evidence "EV-039B-root-folders.txt") # Baseline evidence Get-ComputerInfo \| Out-File (Join-Path $Evidence "EV-039B-computer-info.txt") Get-TimeZone \| Out-File (Join-Path $Evidence "EV-039B-timezone.txt") Get-MpComputerStatus \| Out-File (Join-Path $Evidence "EV-039B-defender-status.txt") winget --version \| Out-File (Join-Path $ToolEvidence "winget-version.txt") # Search before install - validate package IDs before any install command winget search Git \| Tee-Object -FilePath (Join-Path $ToolEvidence "winget-search-git.txt") winget search "Visual Studio Code" \| Tee-Object -FilePath (Join-Path $ToolEvidence "winget-search-vscode.txt") winget search "GitHub CLI" \| Tee-Object -FilePath (Join-Path $ToolEvidence "winget-search-gh.txt") winget search "Node.js" \| Tee-Object -FilePath (Join-Path $ToolEvidence "winget-search-node.txt") winget search "OpenJDK" \| Tee-Object -FilePath (Join-Path $ToolEvidence "winget-search-openjdk.txt") # Version evidence after approved installation git --version \| Tee-Object -FilePath (Join-Path $ToolEvidence "git-version.txt") gh --version \| Tee-Object -FilePath (Join-Path $ToolEvidence "gh-version.txt") code --version \| Tee-Object -FilePath (Join-Path $ToolEvidence "vscode-version.txt") java --version 2>&1 \| Tee-Object -FilePath (Join-Path $ToolEvidence "java-version.txt") mvn --version 2>&1 \| Tee-Object -FilePath (Join-Path $ToolEvidence "maven-version.txt") gradle --version 2>&1 \| Tee-Object -FilePath (Join-Path $ToolEvidence "gradle-version.txt") node --version \| Tee-Object -FilePath (Join-Path $ToolEvidence "node-version.txt") npm --version \| Tee-Object -FilePath (Join-Path $ToolEvidence "npm-version.txt") pnpm --version \| Tee-Object -FilePath (Join-Path $ToolEvidence "pnpm-version.txt") flyway -v 2>&1 \| Tee-Object -FilePath (Join-Path $ToolEvidence "flyway-version.txt") opa version \| Tee-Object -FilePath (Join-Path $ToolEvidence "opa-version.txt") gitleaks version 2>&1 \| Tee-Object -FilePath (Join-Path $ToolEvidence "gitleaks-version.txt") trivy --version 2>&1 \| Tee-Object -FilePath (Join-Path $ToolEvidence "trivy-version.txt") syft version 2>&1 \| Tee-Object -FilePath (Join-Path $ToolEvidence "syft-version.txt") semgrep --version 2>&1 \| Tee-Object -FilePath (Join-Path $ToolEvidence "semgrep-version.txt") # VS Code extension evidence code --list-extensions --show-versions \| Tee-Object -FilePath (Join-Path $ToolEvidence "vscode-extensions.txt") |
| --- |

# Appendix B - Copy-Ready AGENTS.md Baseline
| # AIRA AGENTS.md - System Builder Lite Baseline ## Governing Rule Discipline first. Automation second. Intelligence third. AVCI always. ## Mandatory Principles Preserve or improve SOLID, Clean Architecture, DDD / Bounded Contexts, Ports and Adapters, DRY/KISS/YAGNI, Idempotency, Determinism, Fail-Safe not Fail-Open, Human-in-the-Loop, Least Privilege / SBAC, Separation of Duties, Observability, Policy as Code, Testability, Secure by Design, Resilience, Architecture Fitness Functions, Progressive Autonomy, Reversibility, and AVCI. ## Before Changing Files 1. Identify governing AIRA source documents and versions. 2. State assumptions and intended files. 3. Work only in the active feature branch. 4. Generate or update tests when code/config changes. 5. Update evidence and PR/MR AVCI summary. 6. Do not use production credentials, production data, or Restricted content. ## Rejection Rules Reject changes that bypass OPA/SBAC/ABAC/RBAC, bypass Flyway, bypass CI/CD gates, create duplicate AIRA schemas, weaken PoC 1 / PoC 1A boundaries, leak secrets, disable observability/evidence, call model providers directly, or permit frontend authorization authority. ## AI Boundary AI may analyze, recommend, draft, generate candidate artifacts, test, and propose. AI must not approve, merge, deploy, activate, disable controls, access production credentials, mutate production, or become business authority. |
| --- |

# Appendix C - Copy-Ready Evidence Register
| # AIRA Evidence Register - 39B Workstation Setup \| Evidence ID \| Date/Time \| Phase \| Action \| Execution Surface \| Owner \| Evidence Path \| Validation Result \| Classification \| Follow-Up \| \|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\| \| EV-039B-0000 \| YYYY-MM-DD HH:MM \| Phase 0 \| Pre-start readiness acknowledged \| Human \| Workstation Owner \| AIRA Evidence/phase-00-readiness.md \| Pending/Pass \| INTERNAL \| None \| \| EV-039B-0001 \| YYYY-MM-DD HH:MM \| Phase 1 \| Windows baseline captured \| Human-Executed OS/Admin \| Workstation Owner \| AIRA Evidence/Phase-01 \| Pass \| INTERNAL \| None \| \| EV-039B-0002 \| YYYY-MM-DD HH:MM \| Phase 2 \| ChatGPT Project source bootstrap \| ChatGPT Project \| Solutions Architect \| AIRA Evidence/Phase-02 \| Pass \| INTERNAL CONFIDENTIAL \| Confirm sources \| \| EV-039B-0003 \| YYYY-MM-DD HH:MM \| Phase 3 \| Workspace folders and registers created \| Local Tool/CLI \| Workstation Owner \| AIRA Evidence/Phase-03 \| Pass \| INTERNAL \| None \| \| EV-039B-0004 \| YYYY-MM-DD HH:MM \| Phase 4 \| Core tool versions captured \| Local Tool/CLI \| Workstation Owner \| Tool Evidence \| Pass \| INTERNAL \| Tool gaps \| \| EV-039B-0005 \| YYYY-MM-DD HH:MM \| Phase 5 \| Repository guardrails added \| Git/Repo \| DevSecOps Lead \| PR/MR link \| Pending \| INTERNAL CONFIDENTIAL \| Reviewer approval \| |
| --- |

# Appendix D - Copy-Ready PR/MR Template
| # PR/MR AVCI Summary ## Purpose ## Source / Requirement / Ticket ## Governing AIRA Documents - 09 Greenfield Environment Standard v3.2 - 39B Greenfield AI DevSecOps Workstation Setup and System Builder Lite Guide v1.3 - 01 / 01A / 01B AVCI and Enterprise Design Principles - 10 MicroFunction, 11/20 DevSecOps, 15 API, 16 Flyway, 17 Security, 31A Observability, Dynamic Workspace documents as applicable ## Scope of Change ## AI Assistance Declaration - AI tool used: - Prompt intent: - Files suggested or changed: - Human reviewer: - Limitations / assumptions: ## AVCI - Attributable: owner, developer, checker, ticket, source baseline - Verifiable: tests, scans, policy checks, evidence links - Classifiable: data/classification impact, log/prompt/evidence handling - Improvable: known gaps, backlog, follow-up actions ## Change Type - [ ] Code - [ ] Configuration - [ ] Flyway migration - [ ] OPA policy - [ ] Prompt/guardrail/model route - [ ] Dynamic Workspace component/configuration - [ ] MicroFunction transaction/configuration - [ ] API/event contract - [ ] Documentation/evidence ## Validation - [ ] Build passed - [ ] Unit/component tests passed - [ ] Integration/contract tests passed where applicable - [ ] OPA/Rego tests passed where applicable - [ ] Flyway clean migration passed where applicable - [ ] Secret scan passed - [ ] SAST/SCA/SBOM evidence attached - [ ] Architecture fitness checks passed or waiver attached - [ ] Observability/log redaction evidence attached where applicable - [ ] Accessibility/Playwright evidence attached where applicable - [ ] Resilience/idempotency/DLQ/replay evidence attached where applicable ## Rollback / Safe Disable Describe rollback, forward-fix, feature flag, compensation, deactivation path, or environment rebuild path. ## Reviewer Requirements Architecture, Security, DBA, QA/SDET, DevSecOps, SRE, Product, AI Governance, and CAB/ARB as applicable. |
| --- |

# Appendix E - Copy-Ready Validation Checklist
| Checklist ID | Validation Item |
| --- | --- |
| VC-01 | Windows and browser updated before ChatGPT/Git/Codex sign-in. |
| VC-02 | No production credentials, production data, real customer records, raw tokens, or Restricted data on workstation. |
| VC-03 | D:\ChatGPT Workspace folders created and evidenced. |
| VC-04 | Source register, evidence register, tool registry, and activity ledger created. |
| VC-05 | Core tool versions captured and reviewed. |
| VC-06 | Java 25 target baseline captured or waiver recorded. |
| VC-07 | Repository cloned from approved remote only. |
| VC-08 | AGENTS.md, CODEOWNERS, PR/MR template, branch naming, and evidence paths exist. |
| VC-09 | Codex enabled only after repository controls exist. |
| VC-10 | Codex boundary summary captured before any file changes. |
| VC-11 | Obsidian vault is Git-managed and metadata-compliant. |
| VC-12 | No full codebase copy to Obsidian. |
| VC-13 | Devcontainer/toolchain reproducibility validated. |
| VC-14 | Dynamic Workspace readiness checks defined. |
| VC-15 | MicroFunction runtime readiness checks defined. |
| VC-16 | OpenAPI/AsyncAPI/Kafka/Avro/CloudEvents readiness checks defined. |
| VC-17 | Log4j2/OpenTelemetry/Sentry/Loki/Tempo/Grafana readiness checks defined. |
| VC-18 | Runtime toggle policy prevents disabling mandatory audit/security/evidence. |
| VC-19 | OPA/SBAC, authenticated DAST, secrets hygiene, and remediation evidence defined. |
| VC-20 | Resilience lab readiness defined. |
| VC-21 | Auto-Heal/Auto-Learn/Auto-Improve candidate loop is proposal-driven only. |
| VC-22 | Initial governance PR/MR reviewed with go/no-go decision. |

# Appendix F - External Reference Register
| Reference | URL / Usage |
| --- | --- |
| NIST SP 800-218 SSDF v1.1 | https://csrc.nist.gov/pubs/sp/800/218/final - Secure software development framework practices and evidence discipline. |
| OWASP ASVS Project / ASVS 5.0.0 | https://owasp.org/www-project-application-security-verification-standard/ - Application security verification baseline; use stable ASVS 5.0.0 where adopted. |
| OpenTelemetry Semantic Conventions | https://opentelemetry.io/docs/specs/semconv/ - Common semantic attributes for traces, metrics, logs, resources, HTTP, database, messaging, and runtime telemetry. |
| SLSA v1.2 | https://slsa.dev/spec/v1.2/ - Supply-chain levels, provenance, build integrity, and attestation guidance. |
| Official product documentation | At execution time, verify current behavior for ChatGPT Projects/Codex, Microsoft winget, VS Code, Git, Java distribution, package managers, and security tools from official vendor documentation. |

