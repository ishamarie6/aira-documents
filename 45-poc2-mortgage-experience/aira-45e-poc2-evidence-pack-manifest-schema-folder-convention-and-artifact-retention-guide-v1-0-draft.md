---
title: "PoC2 Evidence Pack Manifest Schema Folder Convention and Artifact Retention Guide"
doc_id: "AIRA-45E"
version: "v1.0"
status: "draft"
category: "PoC2 and mortgage experience"
source_docx: "AIRA_45E_PoC2_Evidence_Pack_Manifest_Schema_Folder_Convention_and_Artifact_Retention_Guide_v1.0_Draft.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 45-poc2-mortgage-experience
  - draft
  - aira-45e
---



# PoC2 Evidence Pack Manifest Schema Folder Convention and Artifact Retention Guide



AIRA

AI-Native Enterprise Platform

PoC 2 Evidence Pack Manifest Schema, Folder Convention, and Artifact Retention Guide

Evidence Manifest | Artifact Hashing | Folder Convention | Classification | Retention

# Document Control
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-045E |
| Document Title | PoC 2 Evidence Pack Manifest Schema, Folder Convention, and Artifact Retention Guide |
| Recommended Filename | AIRA_45E_PoC2_Evidence_Pack_Manifest_Schema_Folder_Convention_and_Artifact_Retention_Guide_v1.0_Draft.docx |
| Version | v1.0 Draft |
| Status | Draft for Architecture / DevSecOps / Security / QA / Development Team Review and Controlled Execution |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Primary Execution Owner | DevSecOps Lead / Internal Audit Evidence Steward |
| Co-Owners | Enterprise Architecture; Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; DBA/Data Governance; Platform Engineering; SRE/Operations; AI Governance; Internal Audit |
| Primary Audience | Software Developers; DevSecOps Engineers; QA/SDET; Security; DBA; Platform Engineering; SRE; AI Governance; Internal Audit; System Builder Operators; AI Coding Assistant Users |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / PoC2 / AIRA-DOC-045E / v1.0/ |
| Approval Path | Draft -> Architecture / DevSecOps / Security / QA Review -> Controlled Execution -> Exit Evidence -> Register Update |
| Review Cadence | At PoC 2 kickoff; every sprint during PoC 2; after pipeline, scanner, GitNexus, evidence, or governance changes; before reuse by future AIRA modules |
| Supersedence | Companion document to AIRA-DOC-045 and AIRA-DOC-045A. Does not supersede AIRA-DOC-042C, AIRA-DOC-045, or parent standards. |

# Mandatory Practice Statement

PoC 2 artifacts are not accepted because scripts run, templates exist, or reports are generated. They are accepted only when owner, source, classification, test evidence, security evidence, GitNexus impact, rollback/safe-disable path, reviewer decision, and improvement path are complete and traceable. AI and automation may draft and generate candidate artifacts, but they must not approve, merge, deploy, waive controls, mutate production, or become authority.

# 1. Executive Summary

This guide defines the minimum evidence model for PoC 2. It prevents the team from treating scattered logs, screenshots, pipeline console output, or AI-generated summaries as sufficient proof. The evidence pack must be both machine-readable and human-reviewable, commit-bound, classification-aware, tamper-resistant where practical, and linked to reviewer decisions.

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

# 2. Evidence Class Requirements
| Evidence Class | Required Records | Required Metadata |
| --- | --- | --- |
| Source evidence | Branch ref, commit SHA, PR/MR URL, CODEOWNERS review, AI-use declaration, AGENTS.md version | Owner, maker, checker, bounded context, classification, change type |
| Build evidence | Build logs, toolchain versions, artifact digest, dependency lockfiles | Build ID, runner ID, environment, toolchain ref, reproducibility hash |
| Test evidence | Unit, component, integration, contract, OPA, architecture, regression, frontend where applicable | Test run ID, coverage, failed/skipped tests, waiver ref, affected tests |
| Security evidence | SAST, SCA, secret scan, DAST, container scan, remediation evidence | Scanner, version, ruleset, severity, finding ID, remediation commit, waiver expiry |
| Supply-chain evidence | SBOM, provenance, artifact digest, license review, dependency review | Artifact name, digest, signer, license decision, attestation ref |
| GitNexus evidence | Code map, impact analysis, affected tests, architecture drift, risk hotspots, report hash | Index commit SHA, report hash, scope, checker, limitations |
| Approval evidence | PR/MR AVCI summary, reviewer decisions, waiver decisions, rollback/forward-fix | Approver, decision time, change ticket, rollback ref, post-monitoring ref |

# 3. Folder Convention

evidence/

poc2/

README.md

manifest.schema.yaml

pr-mr/

<pr-or-mr-id>/

evidence-manifest.yaml

avci-summary.md

build/

tests/

security/

supply-chain/

contracts/

policy/

architecture/

gitnexus/

rollback/

approvals/

waivers/

observations/

# 4. Evidence Manifest Minimum Schema

evidence_manifest:

manifest_version: "aira-poc2-v1.0"

document_ref: "AIRA-DOC-045E"

ticket_ref: ""

pr_mr_ref: ""

branch_ref: ""

base_commit_sha: ""

head_commit_sha: ""

classification: "INTERNAL CONFIDENTIAL"

bounded_context: ""

owner: ""

maker: ""

checker: ""

ai_use:

used: false

tools: []

purpose: ""

human_reviewer: ""

artifacts:

source: []

build: []

tests: []

security: []

supply_chain: []

contracts: []

policy: []

architecture: []

observability: []

gitnexus: []

rollback: []

approvals: []

avci:

attributable: ""

verifiable: ""

classifiable: ""

improvable: ""

waivers: []

known_limitations: []

improvement_backlog: []

final_status: "draft | review-ready | accepted | conditionally-accepted | held | rejected"

# 5. Artifact Hashing and Integrity Rules
| Rule | Required Treatment |
| --- | --- |
| Commit-bound evidence | Evidence must identify base and head commit SHA. |
| Artifact hashes | Build artifacts, scan reports, SBOM, GitNexus reports, and evidence summaries must include hash or immutable reference where practical. |
| No silent replacement | Regenerated evidence must create a new timestamped or versioned record. |
| Human-readable and machine-readable | Each evidence pack must contain manifest YAML/JSON plus Markdown or Word-readable summary. |
| Redaction | Secrets, tokens, raw JWTs, raw PII, prompt payloads, and restricted evidence must be redacted or stored in approved restricted evidence locations. |

# 6. Retention and Classification Rules
| Artifact Type | Default Classification | Retention Guidance |
| --- | --- | --- |
| PR/MR summary | INTERNAL CONFIDENTIAL | Retain with release evidence and source history |
| Build logs | INTERNAL CONFIDENTIAL | Retain for PoC 2 exit and audit window |
| Scan reports | INTERNAL CONFIDENTIAL or higher if sensitive | Retain until remediation and audit closure |
| Secret finding evidence | Restricted / need-to-know | Store redacted public evidence and restricted incident evidence separately |
| GitNexus reports | INTERNAL CONFIDENTIAL | Retain with evidence pack and commit SHA |
| Waivers | INTERNAL CONFIDENTIAL | Retain until expiry, closure, and audit review |

# 7. Evidence Completeness Review

Verify all required folders exist and contain expected artifacts.

Verify manifest references are not stale and point to the correct commit and PR/MR.

Verify all Critical/High findings are closed or formally waived.

Verify rollback/safe-disable evidence exists for every material change.

Verify AI-use declaration is present when AI tools were used.

Verify evidence is classified and redacted before distribution.

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

