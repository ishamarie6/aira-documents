---
title: "DevSecOps Governance and Evidence Control Standard"
doc_id: "AIRA-11A"
version: "v1.3"
status: "revised"
category: "AI-native DevSecOps"
source_docx: "AIRA_11A_DevSecOps_Governance_and_Evidence_Control_Standard_v1.3_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 11-ai-native-devsecops
  - revised
  - aira-11a
---



# DevSecOps Governance and Evidence Control Standard



AIRA
AI-Native Enterprise Platform

DevSecOps Governance and Evidence Control Standard

AIRA-DOC-011A | Version v1.3 Revised

Governed CI/CD | Evidence Packs | Security Gates | GitNexus | System Builder | AI Agent Lifecycle | MicroFunction Delivery
| Field | Value |
| --- | --- |
| Status | Draft for Architecture Review Board, CAB, Security Governance, DevSecOps, QA, Platform Engineering, AI Governance, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Prepared for | AIRA Software Development, DevSecOps, Security, QA/SDET, Platform Engineering, SRE, AI Engineering, and Internal Audit Teams |
| Review Date | 2026-06-18 |
| Primary source reviewed | AIRA_11A_DevSecOps_Governance_and_Evidence_Control_Standard_v1_2_Review_and_Revised.docx |

Mandatory Practice Statement

No AIRA code, configuration, pipeline, prompt, guardrail, database migration, MicroFunction, infrastructure change, AI agent, technology setup, environment provisioning artifact, or System Builder-generated output may be promoted unless it passes AVCI, Enterprise Design Principles, security, evidence, GitNexus impact, CI/CD, and human-governance controls. System Builder accelerates governed change generation; it does not bypass engineering discipline.

# Document Control
| Control Field | Revised Value |
| --- | --- |
| Document ID | AIRA-DOC-011A |
| Document Title | AIRA DevSecOps Governance and Evidence Control Standard |
| Recommended Version | v1.3 Revised - DevSecOps Evidence Control, Parent 11 v3.3, and MicroFunction v3.4 Suite Alignment |
| Source Document Reviewed | 11A-AIRA_DevSecOps_Governance_and_Evidence_Control_Standard_v1.2_Review_and_Revised.docx |
| Supersedes | 11A v1.2 candidate, subject to ARB/CAB approval |
| Primary Parent | 11-AIRA_AI_Native_DevSecOps_Standard_v3.3_Revised |
| Aligned MicroFunction Baseline | 10 v3.4; 10A v2.4; 10B v2.3; 10C v2.3; 10D v2.3; 10E v1.3 |
| External Reference Alignment | NIST SSDF SP 800-218; OWASP ASVS; SLSA v1.2; OpenSSF Scorecard; OpenTelemetry Semantic Conventions; CloudEvents; Open Policy Agent |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / DevSecOps-Governance-and-Evidence-Control / v1.3 / |

# Table of Contents Placeholder

Insert Microsoft Word automatic Table of Contents here before final publication: References > Table of Contents > Automatic Table, then Update Field. This draft uses numbered headings and Word-readable tables for deterministic rendering and review.

# 1. Executive Review Summary

The uploaded 11A v1.2 candidate is structurally sound and remains the correct companion standard for DevSecOps governance and evidence control. The v1.3 revision keeps its operating intent while correcting parent references, tightening review-queue accuracy, and aligning it with the completed AIRA-DOC-011 v3.3 and MicroFunction 10 through 10E revised set.

The major control clarification is that DevSecOps evidence is produced by the system of work, not reconstructed after the fact. A change is not accepted because it compiles, deploys, passes a demo, or is AI-generated. It is accepted only when it has owner, source, classification, tests, security results, SBOM/provenance where applicable, GitNexus impact, architecture fitness, observability, rollback or compensation, waiver status, and maker-checker evidence.

Figure 1 - DevSecOps Governance Control Plane

# 2. Source and Context Alignment Findings
| Aligned Source | Required 11A v1.3 Treatment |
| --- | --- |
| 11 DevSecOps v3.3 | Treat AIRA-DOC-011 as the parent DevSecOps lifecycle standard. 11A translates it into governance, evidence-pack, waiver, GitNexus, System Builder, AI-agent, and release-control rules. |
| 01A / 01 / 01B | Enforce EDP-01 through EDP-20 and AVCI on every pipeline, PR/MR, release, waiver, evidence pack, and improvement candidate. |
| 02 / 03 / 06 | Protect architecture boundaries, daily developer workflow, repository AI rules, branch discipline, PR/MR evidence, and maker-checker review. |
| 10 through 10E | Require MicroFunction evidence for contracts, eventing, outbox, DLQ/replay, idempotency, observability, concurrency, resilience, runtime toggles, security, and rollback. |
| 19 GitNexus / 20 CI/CD Evidence | GitNexus remains read-only and derivative; Document 20 should implement 11/11A controls as concrete pipelines and evidence manifests. |
| 30 / 30A Change and Rollback | Promotion must include release readiness, CAB/ARB triggers, rollback, forward-fix, compensation, deactivation, or rebuild path. |
| 42 AI Governance and Agent Controls | AI agents and System Builder outputs route through LiteLLM, guardrails, Harness/SBAC/OPA, evidence packs, trust tiers, and human approval where required. |

# 3. Review and Gap Analysis
| Gap Area | v1.3 Correction |
| --- | --- |
| Parent version drift | Corrected parent reference from 11 v3.2 candidate to 11 v3.3 Revised and MicroFunction references from v3.3/v2.3/v2.2/v1.2 to the completed revised set. |
| Unverified completion status | Review queue no longer marks 08, 08A, and 09 as completed in this workstream unless supplied or verified. They remain dependency candidates for later reconciliation if not already approved elsewhere. |
| Evidence completeness | Expanded evidence pack taxonomy with fields for AI-use, GitNexus limitation, waiver aging, runtime toggle decisions, observability proof, release evidence, and post-promotion monitoring. |
| Security gates | Clarified authenticated DAST, abuse-case testing, secrets hygiene, policy tests, IaC/container scan, dependency/license review, and remediation evidence. |
| Runtime toggles | Allowed diagnostic and sampling changes only when versioned, authorized, auditable, reversible, and unable to disable mandatory security, audit, policy, idempotency, outbox, critical-error, or compliance evidence. |
| Auto-* loops | Auto-Heal, Auto-Learn, and Auto-Improve remain candidate/proposal loops only, with evidence retrieval, tests, policy checks, human approval, and PR/MR promotion. |

# 4. Revised Full AIRA Standard

## 4.1 Purpose

This standard defines the governance, evidence, pipeline, security, GitNexus, System Builder, AI-agent, environment-provisioning, waiver, and promotion controls required for all AIRA DevSecOps work. It ensures that every engineering change is governed, testable, secure, observable, reversible, and evidence-producing before it is merged, released, activated, or promoted.

## 4.2 Scope

This standard applies to all AIRA code, configuration, MicroFunctions, database migrations, OpenAPI and AsyncAPI contracts, Kafka/Avro/CloudEvents schemas, infrastructure-as-code, devcontainers, pipelines, policies, prompts, guardrails, AI agents, Dynamic Workspace configuration, environment setup, runtime configuration, evidence artifacts, and operational remediation candidates.

## 4.3 Authority and Precedence
| Level | Authority | Role |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance / IT Head | Final authority for production-impacting changes, waivers, promotion gates, high-risk automation, and exceptions. |
| L1 | 01A, 01 AVCI, 01B Evidence, 02 Blueprint, 11 DevSecOps | Universal architecture, evidence, audit, lifecycle discipline, and conflict-resolution authority. |
| L2 | This 11A Standard | DevSecOps governance and evidence-control authority for CI/CD, security gates, GitNexus, System Builder, AI agents, and provisioning artifacts. |
| L3 | Specialist Standards | MicroFunction, API, database, security, observability, change, AI governance, Dynamic Workspace, and CI/CD implementation standards. |
| L4 | Tickets, PR/MR, CI runs, evidence packs, audit logs, dashboards | Operational proof and improvement input; never a substitute for governing standards. |

Conflict rule: where standards conflict, the stricter control governs temporarily, the issue is logged as an AVCI reconciliation item, and the final decision is routed through the appropriate ARB/CAB/security/data-governance path.

## 4.4 DevSecOps Governance Principles
| Principle | Mandatory Meaning |
| --- | --- |
| Discipline first | No pipeline, tool, agent, shortcut, waiver, or runtime toggle may weaken architecture, security, evidence, or approval controls. |
| Evidence by construction | Evidence is generated by repository, CI/CD, security tooling, GitNexus, observability, approvals, and audit stores. |
| Shift left and verify continuously | Architecture, security, policy, tests, supply-chain, and evidence checks begin before merge and continue after release. |
| Fail closed | Missing identity, policy, guardrail, audit, evidence, scan, artifact integrity, or approval blocks protected promotion. |
| Human accountability | AI may draft, analyze, test, propose, and prepare PR/MR candidates; humans own approval, merge, promotion, production, and risk acceptance. |
| Reversibility | Every material change has rollback, forward-fix, compensation, deactivation, feature-disablement, restore, or rebuild path. |

## 4.5 Controlled Intake Domains
| Intake Domain | Required DevSecOps Treatment |
| --- | --- |
| New Requirement | Capture owner, source, classification, affected bounded context, acceptance criteria, contract outputs, test plan, evidence plan, and release impact. |
| Operational and Engineering Evidence | Treat logs, traces, metrics, screenshots, scan results, failed tests, incidents, tickets, and feedback as classified diagnostic input. |
| Improvement Request | Require measurable benefit, risk, candidate fix, tests, rollback path, and backlog linkage for refactoring, reliability, security, UX, performance, or technical debt. |
| AI Agent Lifecycle | Require purpose, owner, skill, SBAC, OPA, tool scope, model route, guardrails, evaluation, monitoring, suspension, and retirement evidence. |
| Environment Provisioning | Require manifest, IaC/devcontainer/toolchain versioning, secret path, SBOM/provenance where applicable, scan output, and rollback/rebuild proof. |

## 4.6 Repository, Branch, and PR/MR Governance

All source-controlled artifacts must live in approved repositories with CODEOWNERS, branch protection, signed commits or equivalent provenance where feasible, required reviews, and required CI checks. PR/MR records must include owner, source intake, classification, affected domains, generated artifacts, AI assistance declaration, tests, scans, GitNexus summary, architecture impact, evidence-pack reference, and rollback path.

Maker, checker, approver, and promoter roles must remain separable for high-risk, production-impacting, security, policy, data, AI-agent, or environment changes. Personal AI accounts, unmanaged scripts, direct production mutations, click-ops changes, unreviewed local files, and undocumented bypasses are prohibited for AIRA work.

## 4.7 CI/CD Pipeline Governance
| Stage | Mandatory Controls |
| --- | --- |
| Pre-commit / pre-PR | Formatting, secrets scan, dependency hygiene, local tests, generated contract checks, prompt/guardrail lint where applicable. |
| PR/MR validation | Build, unit/component/contract tests, architecture fitness, OPA tests, SAST/SCA/secrets/IaC/container scans, GitNexus impact, evidence pack generation. |
| Integration / environment validation | Deploy to controlled environment, migration tests, smoke tests, API/event compatibility, authenticated DAST where applicable, observability and audit evidence. |
| Release readiness | SBOM/provenance, signed or integrity-checked artifacts where feasible, release notes, rollback/forward-fix, CAB/ARB/security approvals where triggered. |
| Post-promotion | Runtime health, SLO/error monitoring, security alerts, logs/traces, evidence retention, incident linkage, and improvement backlog. |

## 4.8 Mandatory Security Gates
| Gate | Mandatory Evidence |
| --- | --- |
| Secrets hygiene | No secrets in source, logs, prompts, screenshots, fixtures, evidence packs, generated artifacts, or documentation. Gitleaks or approved equivalent is blocking. |
| SAST and secure coding | Static analysis and secure coding checks run for protected branches and release candidates; critical/high findings block unless formally waived. |
| SCA and license review | Dependencies are inventoried, scanned, license-reviewed, pinned, and governed through approved dependency controls. |
| SBOM and provenance | Release artifacts, images, and deployable packages require SBOM and build provenance where tooling supports it. |
| DAST and API security | Authenticated DAST and API security testing are required for externally exposed, privileged, customer-facing, or security-sensitive flows. |
| OPA/SBAC policy checks | Authorization, admission, tool-action, environment, data-handling, and agent-policy rules are tested as versioned policy artifacts. |
| Abuse cases | High-risk functions, AI agents, authentication flows, file intake, admin functions, and financial/customer-impacting actions require abuse-case and threat-control evidence. |

## 4.9 MicroFunction DevSecOps Evidence Controls
| Control Area | Required Treatment |
| --- | --- |
| Contract-first interface | OpenAPI, AsyncAPI, schema, Avro, CloudEvents, or internal contract is versioned, tested, and compatibility-checked. |
| Eventing and outbox | Kafka, transactional outbox, CloudEvents, idempotent consumers, DLQ, replay, and schema evolution are tested where applicable. |
| Idempotency and concurrency | Retry-safe, duplicate-safe, replay-safe, and concurrent behavior is tested under expected and stress conditions. |
| Observability | Trace, metric, structured Log4j2 log, audit event, Sentry error record, Loki/Tempo/Grafana dashboard link, and evidence reference are emitted where required. |
| Resilience | Timeouts, retries, circuit breakers, bulkheads, fallback, compensation, DLQ, restore, reprocess, or safe-stop behavior is defined and tested. |
| Security | OPA/SBAC, secrets hygiene, classification, tenant isolation, abuse-case controls, safe errors, and authenticated DAST are applied where relevant. |
| Evidence pack | Tests, scans, GitNexus impact, architecture fitness, policy decisions, observability proof, and rollback/compensation references are attached. |

## 4.10 Evidence Pack Standard

Figure 2 - Evidence Pack Lifecycle and AVCI Fields
| Field | Required Meaning |
| --- | --- |
| evidence_pack_id | Unique evidence pack identifier. |
| pack_type | PR, release, audit, incident, environment, agent, System Builder, MicroFunction, runtime toggle, waiver, or operational remediation. |
| owner and source_refs | Named accountable owner and links to ticket, ADR/TDL, prompt, evidence, incident, requirement, or review item. |
| classification | Data and artifact classification, handling rule, retention rule, and model-route eligibility. |
| artifact_refs | Repository path, commit hash, generated artifact hash, image digest, contract version, migration checksum, or package reference. |
| test_reports | Unit, component, integration, contract, architecture, policy, performance, regression, DAST, or smoke-test results. |
| security_reports | SAST, SCA, secrets, IaC, container, dependency, license, vulnerability, abuse-case, and remediation evidence. |
| SBOM and provenance | SBOM, build provenance, artifact integrity, signing where feasible, and source-to-artifact trace. |
| GitNexus_refs | Impact, affected files, affected services, affected tests, boundary findings, security-sensitive findings, and limitations. |
| observability_refs | Trace ID, audit event, log query, metric dashboard, Sentry issue, Loki/Tempo/Grafana references, and alert evidence. |
| approval and waiver refs | Maker-checker, CODEOWNERS, Security, QA, DevSecOps, DBA, ARB/CAB, waiver, and risk acceptance records. |
| reversibility_refs | Rollback, forward-fix, compensation, deactivation, feature flag, restore, rebuild, or retirement evidence. |

## 4.11 GitNexus Impact Analysis Governance

GitNexus is a read-only, derivative, commit-bound code intelligence and impact-analysis layer. It may support affected-test discovery, blast-radius review, security-sensitive code mapping, dependency analysis, architecture-drift detection, and PR/MR evidence. It must not commit, approve, merge, deploy, mutate production, replace tests, replace scans, or replace human review.
| Rule | Treatment |
| --- | --- |
| Required when | Material code, configuration, MicroFunction, API, event, database, security, AI-agent, environment, or architecture boundary change. |
| Minimum output | Changed files, affected services, affected APIs, affected tests, dependency/call-chain impact, security-sensitive areas, boundary findings, recommendations, and limitations. |
| Evidence status | Advisory until corroborated by tests, scans, policy checks, code review, and human approval. |
| Fail-closed condition | If required GitNexus evidence is unavailable, stale, or incomplete, the PR/MR must disclose this and apply compensating review before merge. |

## 4.12 System Builder and AI Agent Change Controls

System Builder outputs remain advisory, draft, review-ready, PR/MR-ready, change-ready, deployable, active, deprecated, or revoked based on governance state. No AI agent may approve its own output, bypass OPA/SBAC, receive production credentials, call model providers directly, deploy to production, merge protected branches, or alter runtime behavior silently.
| Action | Required Control |
| --- | --- |
| Generate code, tests, configuration, policies, prompts, pipelines, runbooks, or documentation | Feature branch, source references, AI-use declaration, deterministic tests, security scans, human checker, and PR/MR evidence. |
| Analyze logs, traces, scans, incidents, or runtime evidence | Classification check, redaction, evidence reference, root-cause hypothesis, recommended action, and no silent mutation. |
| Create AI agent or tool manifest | Agent registry, owner, SBAC scope, OPA policy, model route, tool limits, evaluation, red-team/certification where applicable. |
| Prepare environment provisioning | Declarative manifest, IaC review, secret path check, policy scan, sandbox/test validation, and rollback/rebuild plan. |

## 4.13 Runtime Toggles, Waivers, and Release Promotion

Figure 3 - Waiver, Runtime Toggle, and Release Gate Boundaries

Runtime toggles may be used for diagnostic verbosity, sampling, non-critical debug logs, and feature exposure where performance or risk requires it. These toggles must be versioned, authorized, auditable, observable, reversible, environment-scoped, and time-bound where applicable. Mandatory audit events, security events, policy decisions, classification labels, idempotency records, outbox records, critical error evidence, and required compliance evidence must not be disabled.

Waivers are temporary risk records, not permanent bypasses. A waiver must identify the affected control, owner, reason, risk rating, compensating controls, expiry, remediation plan, approvers, evidence pack reference, and closure criteria. Critical and High waivers require security, architecture, and risk-owner approval and must be reviewed for aging.

Promotion to staging, pilot, production-like, or production requires a completed evidence pack, successful CI/CD gates, security review, release notes, rollback/forward-fix plan, operational readiness, monitoring, and approval evidence. Production-impacting changes require CAB/ARB or delegated approval as defined by change risk, business impact, security sensitivity, and reversibility.

## 4.14 Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop
| Stage | Required Control |
| --- | --- |
| Detect | Observability, security, support, CI, GitNexus, runtime, or user evidence identifies a problem or opportunity. |
| Retrieve evidence | Trace, logs, metrics, Sentry, Loki, Tempo, Grafana, audit, test result, GitNexus, incident, and configuration evidence are collected with classification controls. |
| Classify and impact | Risk, affected services, affected contracts, data classification, security impact, rollback path, and required approvers are identified. |
| Generate candidate | Candidate fix, learning proposal, runbook update, test improvement, policy change, or MicroFunction configuration proposal is generated in a branch or backlog item. |
| Verify | Tests, scans, policy checks, architecture fitness, GitNexus impact, and evidence pack are produced. |
| Approve | Named human maker-checker, CODEOWNERS, Security/QA/DevSecOps, ARB/CAB where required approve before promotion. |
| Improve | Approved lessons update Obsidian/LLM Wiki, prompts, guardrails, runbooks, tests, and standards through governed knowledge controls. |

## 4.15 Gate Severity Model
| Severity | Meaning |
| --- | --- |
| Advisory | Improvement recommended but does not block. Capture in backlog if accepted. |
| Warning | Risk exists. Merge may proceed only with owner acknowledgement and documented follow-up where appropriate. |
| Blocking | Merge/promotion prohibited until fixed or formally waived by required authority. |
| Critical Block | Promotion prohibited. Requires immediate remediation, security/architecture escalation, or incident handling. |

## 4.16 RACI Summary
| Role | RACI | Responsibility |
| --- | --- | --- |
| Solutions Architecture Office / IT Head | A/R | Owns standard, resolves architecture conflicts, approves major exceptions. |
| DevSecOps Lead | A/R | Owns pipeline governance, CI/CD gates, evidence pack automation, and release gate enforcement. |
| Software Development Lead | R | Ensures code, tests, MicroFunctions, and PR/MR evidence comply with the standard. |
| Security Architecture | A/R | Owns security gates, threat/abuse-case requirements, secrets, access, policy, and risk acceptance. |
| QA/SDET | R | Owns test strategy, deterministic tests, regression, DAST coordination, and quality evidence. |
| Platform Engineering / SRE | R | Owns runtime environments, IaC, containers, devcontainers, observability, reliability, and rollback readiness. |
| AI Governance / AI Engineering | A/R | Owns AI-agent, model-route, guardrail, evaluation, and AI evidence controls. |
| Internal Audit | C/I | Reviews control evidence, findings, remediation, and continuous compliance. |

## 4.17 Validation Checklist
| Checkpoint | Pass Condition |
| --- | --- |
| Intake and owner | Ticket/intake, accountable owner, classification, affected domain, risk tier, and acceptance criteria present. |
| Architecture | SOLID, Clean Architecture, DDD, ports/adapters, API/event/data boundaries, and ADR/TDL triggers assessed. |
| MicroFunction | Runtime configuration, catalog fields, standard steps, STP-BUS isolation, idempotency, outbox/DLQ/replay, and rollback validated. |
| Tests | Unit, component, contract, policy, architecture, regression, integration, performance, and DAST tests applied where relevant. |
| Security | Secrets, SAST, SCA, IaC, container, abuse-case, authenticated DAST, SBOM, provenance, OPA/SBAC evidence present. |
| GitNexus | Impact, affected tests, affected services, boundary findings, and limitations attached or compensating review documented. |
| Observability | OpenTelemetry trace, structured logs, metrics, audit, Sentry, Loki/Tempo/Grafana or approved equivalent evidence present. |
| Release | Rollback, forward-fix, compensation, deactivation, restore, rebuild, CAB/ARB triggers, and post-promotion monitoring defined. |
| AVCI | Attributable, Verifiable, Classifiable, and Improvable evidence complete. |

## 4.18 Anti-Patterns and Rejection Rules

Accepting AI-generated output because it compiles while weakening architecture, security, tests, observability, or rollbackability.

Disabling CI, security gates, audit logging, policy decisions, or required evidence to improve speed.

Using direct model-provider SDK calls from applications, scripts, notebooks, agents, or services instead of approved gateways.

Using direct SQL, manual DDL, click-ops, production kubectl edits, or unmanaged environment mutation outside approved change control.

Allowing GitNexus, System Builder, or AI agents to commit, merge, deploy, approve, rotate production secrets, or bypass human approval.

Promoting changes without evidence pack, rollback/compensation path, classification, owner, and maker-checker approval.

## 4.19 Acceptance Criteria

11A v1.3 is accepted as the DevSecOps governance and evidence-control companion to 11 v3.3 after ARB/CAB/security/internal-audit review.

PR/MR templates include intake, AVCI, EDP impact, AI-use declaration, GitNexus summary, evidence pack, test/scan summary, rollback plan, and human checker confirmation.

CI/CD pipelines generate evidence packs for builds, tests, scans, SBOM/provenance, architecture fitness, policy checks, GitNexus impact, and environment validation.

MicroFunction implementation and runtime configuration changes produce contract, eventing, idempotency, outbox/DLQ/replay, observability, security, and rollback evidence.

No System Builder, AI assistant, agent, GitNexus component, or automation path can approve, merge, deploy, mutate production, or bypass protected gates.

Waivers are time-bound, risk-owned, compensating-control-backed, and linked to remediation evidence.

## 4.20 AVCI Compliance Summary
| AVCI Property | How v1.3 Satisfies It |
| --- | --- |
| Attributable | Defines owners, co-owners, source documents, intake IDs, evidence pack fields, PR/MR templates, approvals, GitNexus records, waivers, and release records. |
| Verifiable | Requires CI/CD results, tests, scans, SBOM, provenance, architecture fitness, policy decisions, GitNexus impact, observability evidence, approvals, and post-promotion monitoring. |
| Classifiable | Requires classification of requirements, evidence, prompts, logs, artifacts, model routes, environment scope, retention, and handling rules. |
| Improvable | Findings, incidents, failed gates, waivers, GitNexus findings, runtime signals, and audit results feed governed Auto-Learn and Auto-Improve backlogs. |

# 5. Simplification Recommendations

Create a one-page developer checklist extracted from repository, CI/CD, evidence pack, and MicroFunction gate sections for daily PR/MR use.

Automate evidence pack creation so developers provide source/context and the pipeline generates most evidence fields automatically.

Use a standard gate matrix per change type: documentation-only, code, MicroFunction config, database, API/event, AI-agent, environment, and production change.

Keep the formal standard detailed, but provide role-specific quick guides for developer, DevSecOps, security, QA, and AI-agent/System Builder operators.

# 6. Automation Recommendations
| Automation Area | Recommended Control |
| --- | --- |
| Document inventory | Generate a Git/Obsidian/OpenKM manifest of all standards, versions, owners, statuses, supersedes, and source pack placement. |
| Canonical register | Maintain a controlled register with active, superseded, candidate, retired, and duplicate-number status. |
| Cross-reference validation | Scan documents for stale references to older versions and missing parent/companion links. |
| Evidence checklist validation | Use CI or scripts to verify that PR/MR records include required evidence fields for each change type. |
| Duplicate detection | Detect duplicate document IDs, duplicate titles, and near-duplicate content. |
| Agent-assisted review queue | Route documents to AI-assisted reviewers, but require named human approval and evidence before canonical adoption. |

# 7. Review Queue Control Register
| Seq | File Name | Current | Recommended | Status | Next Step |
| --- | --- | --- | --- | --- | --- |
| 19 | 11-AIRA_AI_Native_DevSecOps_Standard | v3.2 candidate | v3.3 Revised | Completed / Revised | Use as parent DevSecOps baseline pending approval. |
| 20 | 11A-AIRA_DevSecOps_Governance_and_Evidence_Control_Standard | v1.2 candidate | v1.3 Revised | Completed / Revised | Use as governance/evidence companion pending approval. |
| 21 | 20-AIRA_CICD_Pipeline_and_Evidence_Pack_Implementation_Guide | v1.1 aligned | v1.2 recommended | Next for Review | Convert 11/11A controls into CI/CD stages, evidence automation, status checks, security scans, SBOM/provenance, GitNexus, release readiness, and PR/MR templates. |
| 22 | 08 / 08A / 09 dependency candidates | source marks completed but not verified in this upload sequence | verify or regenerate as needed | AVCI reconciliation item | Do not treat as completed in this workstream without source or register confirmation. |

# 8. Recommended Next Document

The next document to review should be 20-AIRA_CICD_Pipeline_and_Evidence_Pack_Implementation_Guide_v1.1_Aligned.docx. It should convert 11 v3.3 and 11A v1.3 into concrete CI/CD stages, evidence pack automation, status checks, security scans, SBOM/provenance, GitNexus integration, release readiness, and PR/MR evidence templates.

# 9. Change Log
| Version | Date | Summary |
| --- | --- | --- |
| v1.0 | May 2026 | Initial companion standard for GitHub governance, CI/CD gates, security gates, evidence packs, and GitNexus impact analysis. |
| v1.1 | May 2026 | Expanded for System Builder intake, operational evidence, improvement requests, AI agent lifecycle, and environment provisioning. |
| v1.2 | 2026-06-16 | Aligned with 11 v3.2 and updated MicroFunction candidate baseline; strengthened evidence, security, GitNexus, AI/System Builder, Auto-* loops, runtime toggles, waiver aging, and release promotion. |
| v1.3 Revised | 2026-06-18 | Corrected parent to 11 v3.3, aligned MicroFunction family to 10 v3.4 through 10E v1.3, tightened review queue accuracy, and strengthened implementation-ready evidence governance. |

