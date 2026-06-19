---
title: "PoC2 Security Scanning SBOM DAST SCA Secret and Container Scan Playbook"
doc_id: "AIRA-45F"
version: "v1.0"
status: "draft"
category: "PoC2 and mortgage experience"
source_docx: "AIRA_45F_PoC2_Security_Scanning_SBOM_DAST_SCA_Secret_and_Container_Scan_Playbook_v1.0_Draft.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 45-poc2-mortgage-experience
  - draft
  - aira-45f
---



# PoC2 Security Scanning SBOM DAST SCA Secret and Container Scan Playbook



AIRA

AI-Native Enterprise Platform

PoC 2 Security Scanning, SBOM, DAST, SCA, Secret, and Container Scan Playbook

Security Gates | SAST | DAST | SCA | SBOM | Secret Scan | Container Scan | Waivers

# Document Control
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-045F |
| Document Title | PoC 2 Security Scanning, SBOM, DAST, SCA, Secret, and Container Scan Playbook |
| Recommended Filename | AIRA_45F_PoC2_Security_Scanning_SBOM_DAST_SCA_Secret_and_Container_Scan_Playbook_v1.0_Draft.docx |
| Version | v1.0 Draft |
| Status | Draft for Architecture / DevSecOps / Security / QA / Development Team Review and Controlled Execution |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Primary Execution Owner | Security Architecture / DevSecOps Lead |
| Co-Owners | Enterprise Architecture; Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; DBA/Data Governance; Platform Engineering; SRE/Operations; AI Governance; Internal Audit |
| Primary Audience | Software Developers; DevSecOps Engineers; QA/SDET; Security; DBA; Platform Engineering; SRE; AI Governance; Internal Audit; System Builder Operators; AI Coding Assistant Users |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / PoC2 / AIRA-DOC-045F / v1.0/ |
| Approval Path | Draft -> Architecture / DevSecOps / Security / QA Review -> Controlled Execution -> Exit Evidence -> Register Update |
| Review Cadence | At PoC 2 kickoff; every sprint during PoC 2; after pipeline, scanner, GitNexus, evidence, or governance changes; before reuse by future AIRA modules |
| Supersedence | Companion document to AIRA-DOC-045 and AIRA-DOC-045A. Does not supersede AIRA-DOC-042C, AIRA-DOC-045, or parent standards. |

# Mandatory Practice Statement

PoC 2 artifacts are not accepted because scripts run, templates exist, or reports are generated. They are accepted only when owner, source, classification, test evidence, security evidence, GitNexus impact, rollback/safe-disable path, reviewer decision, and improvement path are complete and traceable. AI and automation may draft and generate candidate artifacts, but they must not approve, merge, deploy, waive controls, mutate production, or become authority.

# 1. Executive Summary

This playbook defines how PoC 2 proves secure software delivery through repeatable, evidence-producing security gates. It establishes scan types, severity thresholds, remediation expectations, waiver controls, DAST scope boundaries, SBOM and supply-chain evidence, and fail-closed handling.

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

# 2. Security Gate Matrix
| Gate | Purpose | Minimum Evidence | Blocking Rule |
| --- | --- | --- | --- |
| Secret scan | Prevent committed secrets, tokens, keys, credentials | Scan report, finding status, remediation proof | Any real secret blocks merge and triggers containment |
| SAST | Detect code-level vulnerabilities and insecure patterns | Report with tool version and ruleset | Unwaived Critical/High blocks |
| SCA | Detect vulnerable dependencies and license issues | Dependency report and remediation/waiver status | Unwaived Critical/High or prohibited license blocks |
| SBOM | Record software bill of materials | CycloneDX/SPDX or approved equivalent, artifact hash | Missing SBOM blocks release-readiness |
| Container scan | Detect base image and package vulnerabilities | Image digest and scan report | Unwaived Critical/High blocks |
| DAST | Test runtime/API behavior in approved non-prod synthetic scope | DAST report, target, test account, exclusions | Unwaived Critical/High blocks |
| IaC/config scan where applicable | Detect insecure infrastructure/config patterns | Scan report and remediation status | Unwaived Critical/High blocks |
| Policy/security tests | Verify OPA/SBAC deny/fail-closed behavior | Policy test output | Fail-open path blocks |

# 3. Severity and Remediation Rules
| Severity | Default Action | Waiver Authority |
| --- | --- | --- |
| Critical | Block merge. Remediate or obtain explicit time-bound waiver with compensating control. | Security Governance / IT Head / CAB where required |
| High | Block merge unless accepted through controlled waiver. | Security Architecture / DevSecOps / CAB where required |
| Medium | Create remediation ticket and target date. May be allowed if no exploit path and controls exist. | Security Architecture / DevSecOps Lead |
| Low | Track for backlog or scheduled hardening. | Dev Lead / QA / Security reviewer |
| Informational | Review for trend, false positive, or improvement candidate. | DevSecOps / QA |

# 4. Authenticated DAST Scope Control
| Control | Required Treatment |
| --- | --- |
| Target environment | Non-production only unless separately approved. Use synthetic data and approved test accounts. |
| Authentication | Use dedicated test identities with least privilege. Do not use production accounts. |
| Rate limit | Configure safe scan rate and exclude destructive or state-changing endpoints unless specifically approved. |
| Data handling | No raw PII, production data, secrets, or restricted documents in DAST evidence. |
| Approval | Security and QA must approve DAST scope before scan. |
| Evidence | Capture target URL, test user, scope, exclusions, time window, report, findings, remediation, waiver status. |

# 5. SBOM and Supply-Chain Evidence
| Requirement | Acceptance Evidence |
| --- | --- |
| Generate SBOM for built artifacts or images | SBOM file and artifact digest |
| Record dependency source and lockfile state | Dependency lockfile and SCA report |
| Record image base and digest where containers are used | Image digest and container scan report |
| Review license concerns | License report and decision record |
| Record provenance where available | Build run ID, artifact digest, signed/attested artifact reference |

# 6. Waiver Template

waiver:

waiver_id: "WVR-P2-YYYY-NNN"

finding_id: ""

severity: "Critical | High | Medium | Low"

scanner: ""

owner: ""

approver: ""

reason: ""

compensating_control: ""

expiry_date: ""

remediation_ticket: ""

evidence_ref: ""

review_status: "open | accepted | expired | closed"

# 7. Security Review Checklist

Confirm scanner versions and rule sets are recorded.

Confirm secret scan has no real exposed secret. If found, rotate/revoke and preserve restricted evidence.

Confirm SAST/SCA/container/DAST Critical and High findings are remediated or formally waived.

Confirm SBOM and dependency review exist and are linked to the artifact digest.

Confirm DAST used approved non-prod synthetic scope.

Confirm security evidence is redacted and classified.

Confirm waiver expiry and remediation ticket exist for every accepted exception.

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

