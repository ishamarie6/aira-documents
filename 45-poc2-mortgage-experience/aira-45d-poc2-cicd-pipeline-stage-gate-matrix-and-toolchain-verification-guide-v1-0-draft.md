---
title: "PoC2 CICD Pipeline Stage Gate Matrix and Toolchain Verification Guide"
doc_id: "AIRA-45D"
version: "v1.0"
status: "draft"
category: "PoC2 and mortgage experience"
source_docx: "AIRA_45D_PoC2_CICD_Pipeline_Stage_Gate_Matrix_and_Toolchain_Verification_Guide_v1.0_Draft.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 45-poc2-mortgage-experience
  - draft
  - aira-45d
---



# PoC2 CICD Pipeline Stage Gate Matrix and Toolchain Verification Guide



AIRA

AI-Native Enterprise Platform

PoC 2 CI/CD Pipeline Stage, Gate Matrix, and Toolchain Verification Guide

Pipeline Stages | Quality Gates | Toolchain Verification | Fail-Closed Evidence | Reusable Factory

# Document Control
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-045D |
| Document Title | PoC 2 CI/CD Pipeline Stage, Gate Matrix, and Toolchain Verification Guide |
| Recommended Filename | AIRA_45D_PoC2_CICD_Pipeline_Stage_Gate_Matrix_and_Toolchain_Verification_Guide_v1.0_Draft.docx |
| Version | v1.0 Draft |
| Status | Draft for Architecture / DevSecOps / Security / QA / Development Team Review and Controlled Execution |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Primary Execution Owner | DevSecOps Lead |
| Co-Owners | Enterprise Architecture; Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; DBA/Data Governance; Platform Engineering; SRE/Operations; AI Governance; Internal Audit |
| Primary Audience | Software Developers; DevSecOps Engineers; QA/SDET; Security; DBA; Platform Engineering; SRE; AI Governance; Internal Audit; System Builder Operators; AI Coding Assistant Users |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / PoC2 / AIRA-DOC-045D / v1.0/ |
| Approval Path | Draft -> Architecture / DevSecOps / Security / QA Review -> Controlled Execution -> Exit Evidence -> Register Update |
| Review Cadence | At PoC 2 kickoff; every sprint during PoC 2; after pipeline, scanner, GitNexus, evidence, or governance changes; before reuse by future AIRA modules |
| Supersedence | Companion document to AIRA-DOC-045 and AIRA-DOC-045A. Does not supersede AIRA-DOC-042C, AIRA-DOC-045, or parent standards. |

# Mandatory Practice Statement

PoC 2 artifacts are not accepted because scripts run, templates exist, or reports are generated. They are accepted only when owner, source, classification, test evidence, security evidence, GitNexus impact, rollback/safe-disable path, reviewer decision, and improvement path are complete and traceable. AI and automation may draft and generate candidate artifacts, but they must not approve, merge, deploy, waive controls, mutate production, or become authority.

# 1. Executive Summary

This companion guide defines the CI/CD stage model and toolchain verification required for PoC 2. It ensures that the reusable System Factory can prove build correctness, test correctness, security posture, architecture fitness, supply-chain integrity, GitNexus impact, and evidence-pack completeness on every PR/MR.

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

# 2. Toolchain Verification Matrix
| Toolchain Area | Minimum Required Verification | Evidence |
| --- | --- | --- |
| Source control | Repository URL, protected branch, CODEOWNERS, PR/MR checks | Repository readiness report |
| Java / Spring | Approved Java and build tool versions installed in CI and local dev | java -version, build logs |
| Frontend where applicable | Node/TypeScript package manager and lockfile verified | node/npm/pnpm version and build logs |
| Containers | Docker/Podman/buildx runner available if images are built | Runner capability report |
| Test frameworks | JUnit 5, Testcontainers, frontend test runner where applicable | Test report and dependency lockfile |
| Policy | OPA/Rego tests runnable | Policy test output |
| Scanners | Secret scan, SAST, SCA, SBOM, container scan, DAST available | Scanner versions and sample reports |
| GitNexus | Read-only token and commit-bound report configuration | GitNexus dry run report |
| Evidence generator | Manifest schema and derived artifact generation runnable | Sample evidence pack |

# 3. CI/CD Pipeline Gate Matrix
| Stage | Required Checks | Required Artifacts | Blocking Condition |
| --- | --- | --- | --- |
| 0. Intake | Ticket, owner, branch, classification, PR/MR template | Intake validation output | Missing owner, ticket, classification, or template |
| 1. Source governance | Branch rules, CODEOWNERS, AI-use declaration | Repository control proof | Direct protected-branch commit or missing reviewer |
| 2. Build | Backend and frontend build where applicable | Build logs, artifact hashes | Build failure or unpinned critical dependency |
| 3. Unit tests | JUnit 5 and frontend unit tests where applicable | Test reports | Failed required tests |
| 4. Integration | Testcontainers and disposable dependencies where applicable | Integration report | Unreproducible environment or failed test |
| 5. Contract | OpenAPI, AsyncAPI, schema compatibility where applicable | Contract test report | Contract drift or incompatible schema |
| 6. Flyway | Validate migrations where DB changes exist | Flyway validate log | Checksum drift or unmanaged DDL |
| 7. Policy | OPA/SBAC allow, deny, escalate, fail-closed tests | Policy test report | Fail-open path or missing negative test |
| 8. Architecture fitness | Boundary, dependency direction, banned import checks | Architecture fitness report | Boundary violation |
| 9. Security | Secret, SAST, SCA, license, DAST where applicable | Scan reports | Secret or unapproved Critical/High finding |
| 10. Supply chain | SBOM, provenance, image digest, container scan | SBOM and image scan report | Missing SBOM or Critical image finding |
| 11. GitNexus | Code map, impact, affected tests, report hash | GitNexus report | Missing, stale, or non-read-only report |
| 12. Evidence pack | Manifest, hashes, summaries, rollback, reviewers | Evidence pack | Incomplete or stale evidence |

# 4. Pipeline Execution Rules

The pipeline must run on every PR/MR open, update, and readiness review event.

All mandatory stage outputs must be stored with commit SHA, PR/MR ID, tool version, timestamp, and classification.

The pipeline must fail closed when evidence cannot be produced or cannot be linked to the source commit.

Manual reruns must be logged and linked to the same evidence pack.

Tool versions must be pinned or explicitly recorded. Version drift must be logged as a reconciliation or improvement item.

Pipeline summaries are evidence, not approval. Human reviewer sign-off remains required.

# 5. Minimal Pipeline Skeleton

stages:

- intake

- build

- test

- contract

- policy

- architecture

- security

- supply_chain

- gitnexus

- evidence

- review_readiness

gates:

fail_closed_on_missing_evidence: true

block_on_secret: true

block_on_unwaived_critical_high: true

require_codeowners_review: true

require_rollback_or_safe_disable: true

require_avci_summary: true

# 6. Toolchain Verification Checklist
| Item | Command / Proof | Pass Criteria |
| --- | --- | --- |
| Java | java -version | Matches approved AIRA Technology Stack or registered exception |
| Build tool | mvn -version or gradle -version | Version recorded in evidence |
| Node if used | node -v and package manager version | Version recorded and lockfile present |
| Container runner | docker version or equivalent | Available in CI when images are built |
| OPA | opa version and policy test run | OPA policy tests pass |
| Scanners | scanner --version and sample scan | Report generated and stored |
| GitNexus | dry-run read-only report | No write, merge, deploy, or production authority |
| Evidence generator | generate sample manifest | Valid schema and artifact references |

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

