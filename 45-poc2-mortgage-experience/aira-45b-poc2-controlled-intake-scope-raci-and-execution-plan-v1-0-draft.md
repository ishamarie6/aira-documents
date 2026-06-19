---
title: "PoC2 Controlled Intake Scope RACI and Execution Plan"
doc_id: "AIRA-45B"
version: "v1.0"
status: "draft"
category: "PoC2 and mortgage experience"
source_docx: "AIRA_45B_PoC2_Controlled_Intake_Scope_RACI_and_Execution_Plan_v1.0_Draft.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 45-poc2-mortgage-experience
  - draft
  - aira-45b
---



# PoC2 Controlled Intake Scope RACI and Execution Plan



AIRA

AI-Native Enterprise Platform

PoC 2 Controlled Intake, Scope, RACI, and Execution Plan

Controlled Intake | Scope Discipline | RACI | Execution Cadence | Exit Evidence | AVCI Always

# Document Control
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-045B |
| Document Title | PoC 2 Controlled Intake, Scope, RACI, and Execution Plan |
| Recommended Filename | AIRA_45B_PoC2_Controlled_Intake_Scope_RACI_and_Execution_Plan_v1.0_Draft.docx |
| Version | v1.0 Draft |
| Status | Draft for Architecture / DevSecOps / Security / QA / Development Team Review and Controlled Execution |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Primary Execution Owner | DevSecOps Lead |
| Co-Owners | Enterprise Architecture; Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; DBA/Data Governance; Platform Engineering; SRE/Operations; AI Governance; Internal Audit |
| Primary Audience | Software Developers; DevSecOps Engineers; QA/SDET; Security; DBA; Platform Engineering; SRE; AI Governance; Internal Audit; System Builder Operators; AI Coding Assistant Users |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / PoC2 / AIRA-DOC-045B / v1.0/ |
| Approval Path | Draft -> Architecture / DevSecOps / Security / QA Review -> Controlled Execution -> Exit Evidence -> Register Update |
| Review Cadence | At PoC 2 kickoff; every sprint during PoC 2; after pipeline, scanner, GitNexus, evidence, or governance changes; before reuse by future AIRA modules |
| Supersedence | Companion document to AIRA-DOC-045 and AIRA-DOC-045A. Does not supersede AIRA-DOC-042C, AIRA-DOC-045, or parent standards. |

# Mandatory Practice Statement

PoC 2 artifacts are not accepted because scripts run, templates exist, or reports are generated. They are accepted only when owner, source, classification, test evidence, security evidence, GitNexus impact, rollback/safe-disable path, reviewer decision, and improvement path are complete and traceable. AI and automation may draft and generate candidate artifacts, but they must not approve, merge, deploy, waive controls, mutate production, or become authority.

# 1. Executive Summary

This companion document is the PoC 2 execution starter. It defines how the team will initiate PoC 2, confirm scope, assign accountable owners, preserve PoC 1 and PoC 1A, identify entry and exit gates, and route all work through controlled intake and evidence-producing delivery. It prevents PoC 2 from becoming an informal tooling exercise or premature business-module development effort.

# Source Alignment
| Source / Control | Required Treatment |
| --- | --- |
| AIRA-DOC-042C Foundation PoC Roadmap and Developer Technology Immersion Sequence Governance Standard v1.4 Revised | Treat PoC 2 as a governed capability proof and keep business module development blocked until foundation readiness evidence is accepted. |
| AIRA-DOC-045 PoC 2 DevSecOps Pipeline, Evidence Pack, GitNexus, and System Factory Implementation Standard v1.2 Revised | Implement DevSecOps pipeline, Evidence Pack, GitNexus, and reusable System Factory baseline with PR/MR evidence gates. |
| AIRA-DOC-045A PoC 2 Requirements and Execution Standard v1.0 Draft | Implement DevSecOps pipeline, Evidence Pack, GitNexus, and reusable System Factory baseline with PR/MR evidence gates. |
| AIRA-DOC-004 Technology Stack v9.2 Revised | Use approved, version-pinned, security-scanned, observable, supportable, rollbackable, and evidence-linked technologies. |
| AIRA-DOC-001 / 001A / 001B AVCI, Enterprise Architecture, Evidence, Audit, Traceability, and Control Standards | Every artifact must be attributable, verifiable, classifiable, and improvable. |
| AIRA-DOC-011 / 011A / 020 DevSecOps, Governance, and CI/CD Evidence Pack Standards | Use CI/CD gates, test reports, scans, SBOM, provenance, release readiness, and evidence manifest. |
| AIRA-DOC-017 / 017A Security, Identity, Secrets, and Access Control Standards | Apply least privilege, OPA/SBAC, secrets hygiene, authenticated DAST boundaries, fail-closed behavior, and waiver control. |
| AIRA-DOC-019 GitNexus Code Intelligence and Impact Analysis Standard | Keep GitNexus read-only, derivative, commit-bound, and non-authoritative. |
| AIRA-DOC-031 / 031A Operations, Observability, Telemetry, and Evidence Correlation Standards | Bind pipeline and runtime evidence to logs, traces, metrics, audit, dashboards, redaction, and trace reconstruction where applicable. |
| AIRA-DOC-041B / 044A / 073 System Builder and Maker-Checker Operating Standards | Use as governing companion control. Conflicts are AVCI reconciliation items and the stricter control governs until resolved. |

# Authority and Non-Negotiable Boundaries
| Boundary | Mandatory Rule |
| --- | --- |
| Human accountability | Each PoC 2 artifact has a named owner, maker, checker, reviewer, and approval state. |
| AI boundary | AI may recommend, analyze, draft, generate candidates, summarize evidence, and propose improvements only. |
| No self-approval | AI, GitNexus, System Builder, scanners, and pipeline summaries must not approve their own output. |
| No direct production mutation | No production deployment, production DDL, production secret access, or production data mutation is permitted in these companion documents. |
| No direct model-provider calls | Application code, scripts, notebooks, agents, and services must route through approved model gateway controls where AI is used. |
| Fail closed | Missing identity, policy, evidence, scan result, reviewer, rollback path, or classification blocks protected action. |

# 2. Purpose and Scope
| Area | In Scope | Out of Scope |
| --- | --- | --- |
| Intake | PoC 2 ticket, scope statement, risk tier, classification, owner, evidence path | Informal chat-only work, undocumented local scripts, unapproved tool execution |
| Execution | Repository, pipeline, scans, GitNexus, evidence pack, review gates, exit report | Actual production deployment or broad business module development |
| Governance | RACI, maker-checker, waiver authority, approval path, sign-offs | AI approval, scanner approval, GitNexus approval, author-only sign-off |
| Preservation | PoC 1 and PoC 1A regression evidence and no weakening of login controls | Rewriting login/session/security behavior as part of PoC 2 |

# 3. Controlled Intake Template
| Field | Required Value / Guidance |
| --- | --- |
| intake_id | P2-INTAKE-YYYY-NNN or equivalent ticket reference |
| requester | Named requester and owning team |
| accountable_owner | Named owner from Solutions Architecture / DevSecOps |
| scope_statement | What PoC 2 will prove and what it will not attempt to prove |
| classification | INTERNAL CONFIDENTIAL unless register assigns a stricter class |
| risk_tier | Low / Medium / High; High requires Security and Architecture review |
| affected_repository | Repository name, branch model, CODEOWNERS path |
| affected_controls | CI/CD, tests, scans, GitNexus, evidence, rollback, policy, observability |
| entry_evidence | PoC 1/1A acceptance, repository readiness, toolchain readiness, evidence path |
| exit_evidence | PR/MR evidence pack, scans, GitNexus report, acceptance sign-off |
| waiver_policy | Waivers require owner, expiry, approver, compensating control, closure ticket |

# 4. Entry Gate Checklist
| Gate | Pass Evidence | Failure Action |
| --- | --- | --- |
| PoC 1 accepted | Exit evidence and no unresolved Critical/High findings | Hold PoC 2 start |
| PoC 1A accepted | Additive security intelligence and regression proof | Hold PoC 2 start |
| Repository selected | Repository URL, owner, branch strategy | Create or approve repository first |
| Evidence path ready | OpenKM/Git evidence path and classification assigned | Create evidence path before execution |
| Toolchain ready | Java/Spring, CI runner, scanners, GitNexus, artifact store verified | Complete 045D toolchain verification |
| RACI assigned | Named owner, maker, checker, reviewers | Assign before any PR/MR |

# 5. Execution Plan and Cadence
| Phase | Workstream | Exit Evidence |
| --- | --- | --- |
| 0 | Confirm intake, scope, owners, classification, and risk tier | Approved PoC 2 intake record |
| 1 | Bootstrap repository and branch controls | 045C checklist complete |
| 2 | Verify toolchain and CI/CD runner | 045D verification report |
| 3 | Add pipeline stages and evidence generation | Pipeline logs, evidence manifest |
| 4 | Add scans and security playbook | 045F scan reports and remediation plan |
| 5 | Integrate GitNexus and Derived Artifact Generator | 045G report and generated summaries |
| 6 | Run representative PR/MR and regression proof | Complete PR/MR evidence pack |
| 7 | Exit review and reusable factory handoff | Exit sign-off and backlog |

# 6. RACI
| Activity | Responsible | Accountable | Consulted | Evidence |
| --- | --- | --- | --- | --- |
| Scope and intake approval | DevSecOps Lead / Solutions Architecture | IT Head / SAO | Security, QA, DBA, SRE, Development Lead | Intake record, approval note |
| Repository and pipeline implementation | DevSecOps / Development Lead | DevSecOps Lead | Security, QA, Architecture | PR/MR, pipeline logs |
| Security gates and waiver review | Security Architecture | Security Governance | DevSecOps, QA, Development Lead | Scan results, waiver register |
| Testing and quality gates | QA/SDET | QA/SDET Lead | DevSecOps, Development Lead, Architecture | Test reports, coverage, defect register |
| Evidence pack completeness review | DevSecOps / Internal Audit | Solutions Architecture Office | Security, QA, SRE, DBA | Evidence manifest, traceability matrix |
| Exit decision | Solutions Architecture / DevSecOps | IT Head / ARB/CAB where required | Security, QA, DBA, SRE, Internal Audit | Exit sign-off pack |

# 7. Exit Review Inputs

Approved intake record and scope statement.

Completed repository, pipeline, security, evidence, and GitNexus companion checklists.

At least one representative PR/MR with complete evidence pack.

PoC 1 and PoC 1A preservation/regression proof.

Known limitations, waivers, residual risks, and improvement backlog.

Reusable factory handoff decision: Accepted, Conditionally Accepted, Held, or Rejected.

# Acceptance Criteria and Blocking Conditions
| Acceptance Area | Minimum Required Evidence | Blocks Acceptance When |
| --- | --- | --- |
| Ownership | Named owner, maker, checker, reviewer, evidence steward | Owner, reviewer, or accountability path missing |
| Classification | Classification and redaction profile for code, config, logs, scans, evidence | Classification unclear or Restricted data exposed |
| Verification | Tests, scans, policy checks, GitNexus report, evidence manifest | Required evidence missing, stale, failed, or unactioned |
| Security | No secrets, Critical/High findings resolved or approved with waiver | Secret exposure or unapproved Critical/High finding |
| Reversibility | Rollback, forward-fix, safe-disable, or compensation path | No reversal or safe-disable evidence |
| Review | CODEOWNERS / maker-checker approval and sign-off record | Author-only approval or missing reviewer |

# AVCI Compliance Summary
| AVCI Property | How This Document Satisfies It |
| --- | --- |
| Attributable | Defines owners, source baseline, document ID, role responsibilities, reviewer path, and evidence path. |
| Verifiable | Defines evidence, tests, scans, policy checks, GitNexus outputs, artifact hashes, and review gates. |
| Classifiable | Requires INTERNAL CONFIDENTIAL handling, classification fields, data handling rules, and redaction expectations. |
| Improvable | Requires known limitations, backlog items, lessons learned, waiver closure, and register/update path. |

