---
title: "PoC2 GitNexus Read Only Impact Analysis and Derived Artifact Generator Runbook"
doc_id: "AIRA-45G"
version: "v1.0"
status: "draft"
category: "PoC2 and mortgage experience"
source_docx: "AIRA_45G_PoC2_GitNexus_Read_Only_Impact_Analysis_and_Derived_Artifact_Generator_Runbook_v1.0_Draft.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 45-poc2-mortgage-experience
  - draft
  - aira-45g
---



# PoC2 GitNexus Read Only Impact Analysis and Derived Artifact Generator Runbook



AIRA

AI-Native Enterprise Platform

PoC 2 GitNexus Read-Only Impact Analysis and Derived Artifact Generator Runbook

GitNexus Read-Only | Impact Analysis | Code Map | Derived Artifacts | Non-Authority Controls

# Document Control
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-045G |
| Document Title | PoC 2 GitNexus Read-Only Impact Analysis and Derived Artifact Generator Runbook |
| Recommended Filename | AIRA_45G_PoC2_GitNexus_Read_Only_Impact_Analysis_and_Derived_Artifact_Generator_Runbook_v1.0_Draft.docx |
| Version | v1.0 Draft |
| Status | Draft for Architecture / DevSecOps / Security / QA / Development Team Review and Controlled Execution |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Primary Execution Owner | DevSecOps Lead / System Builder Owner |
| Co-Owners | Enterprise Architecture; Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; DBA/Data Governance; Platform Engineering; SRE/Operations; AI Governance; Internal Audit |
| Primary Audience | Software Developers; DevSecOps Engineers; QA/SDET; Security; DBA; Platform Engineering; SRE; AI Governance; Internal Audit; System Builder Operators; AI Coding Assistant Users |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / PoC2 / AIRA-DOC-045G / v1.0/ |
| Approval Path | Draft -> Architecture / DevSecOps / Security / QA Review -> Controlled Execution -> Exit Evidence -> Register Update |
| Review Cadence | At PoC 2 kickoff; every sprint during PoC 2; after pipeline, scanner, GitNexus, evidence, or governance changes; before reuse by future AIRA modules |
| Supersedence | Companion document to AIRA-DOC-045 and AIRA-DOC-045A. Does not supersede AIRA-DOC-042C, AIRA-DOC-045, or parent standards. |

# Mandatory Practice Statement

PoC 2 artifacts are not accepted because scripts run, templates exist, or reports are generated. They are accepted only when owner, source, classification, test evidence, security evidence, GitNexus impact, rollback/safe-disable path, reviewer decision, and improvement path are complete and traceable. AI and automation may draft and generate candidate artifacts, but they must not approve, merge, deploy, waive controls, mutate production, or become authority.

# 1. Executive Summary

This runbook defines how GitNexus and the Derived Artifact Generator operate inside PoC 2. GitNexus is read-only, derivative, commit-bound code intelligence. The Derived Artifact Generator creates review-ready summaries and evidence indexes. Neither may approve, merge, deploy, waive findings, mutate production, or replace human review.

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
| AIRA-DOC-044C Governed AI Agent Inventory, Lifecycle, and Runtime Control Standard v1.1 Revised | Use as governing companion control. Conflicts are AVCI reconciliation items and the stricter control governs until resolved. |

# Authority and Non-Negotiable Boundaries
| Boundary | Mandatory Rule |
| --- | --- |
| Human accountability | Each PoC 2 artifact has a named owner, maker, checker, reviewer, and approval state. |
| AI boundary | AI may recommend, analyze, draft, generate candidates, summarize evidence, and propose improvements only. |
| No self-approval | AI, GitNexus, System Builder, scanners, and pipeline summaries must not approve their own output. |
| No direct production mutation | No production deployment, production DDL, production secret access, or production data mutation is permitted in these companion documents. |
| No direct model-provider calls | Application code, scripts, notebooks, agents, and services must route through approved model gateway controls where AI is used. |
| Fail closed | Missing identity, policy, evidence, scan result, reviewer, rollback path, or classification blocks protected action. |

# 2. GitNexus Operating Model
| Capability | Allowed Use | Prohibited Use |
| --- | --- | --- |
| Code map | Map changed files, packages, components, dependencies, test impact | Cannot change source code or architecture decisions |
| Impact analysis | Identify blast radius, affected tests, risk hotspots, schema/API/policy impact | Cannot waive required tests or scans |
| Architecture drift detection | Flag boundary shortcuts, dependency direction issues, risky imports | Cannot approve or reject alone |
| Evidence summary | Summarize commit-bound reports into evidence pack | Cannot replace evidence manifest or reviewer sign-off |
| Improvement candidates | Suggest backlog items for test gaps, drift, documentation, security tuning | Cannot silently change runtime, policies, prompts, agents, or database |

# 3. GitNexus Minimum Report Fields
| Field | Required Purpose |
| --- | --- |
| report_id | Unique report identifier |
| tool_version | Toolchain traceability |
| base_commit_sha / head_commit_sha | Commit-bound evidence |
| repository_ref | Source traceability |
| changed_files | Source impact |
| affected_components | Architecture impact |
| affected_tests | Test targeting and reviewer awareness |
| security_hotspots | Security review targeting |
| architecture_drift_findings | Boundary review |
| database_api_event_policy_impact | Specialist reviewer routing |
| limitations | Known blind spots and manual review required |
| report_hash | Evidence integrity |
| reviewer_acknowledgement | Human review confirmation |

# 4. Derived Artifact Generator Outputs
| Output | Required Contents | Acceptance Rule |
| --- | --- | --- |
| PR/MR AVCI summary | Owner, source, intent, classification, verification, improvement path | Attached to PR/MR and evidence pack |
| Release-readiness summary | Build/test/security/policy/architecture/GitNexus/rollback status | Identifies blockers and waivers |
| Rollback checklist | Rollback, forward-fix, safe-disable, compensation, owner | Required for material change |
| Test evidence index | Links to unit, integration, contract, policy, architecture, regression results | All required tests linked |
| Security evidence index | Links to secret, SAST, SCA, SBOM, container, DAST, waivers | All required scans linked |
| Architecture impact summary | Boundary impact, dependency changes, direct shortcut risk | Reviewed by Architecture when material |
| Improvement candidates | Backlog entries for gaps, drift, tests, docs, tooling | No silent change; candidate-only |

# 5. Runbook Procedure

Confirm PR/MR has intake ID, owner, classification, and branch reference.

Run GitNexus in read-only mode against base and head commit SHA.

Store GitNexus report under evidence/poc2/pr-mr/<id>/gitnexus/.

Generate report hash and update evidence manifest.

Run Derived Artifact Generator using pipeline outputs, scan outputs, test reports, GitNexus report, and rollback input.

Store derived artifacts under evidence/poc2/pr-mr/<id>/approvals/ or derived/.

Update PR/MR with AVCI summary and release-readiness summary.

Require human reviewer acknowledgement of GitNexus findings and limitations.

Route any Critical/High impact to Security, Architecture, DBA, SRE, QA, or CAB as required.

Capture improvement candidates without auto-mutating source, policy, prompt, agent, database, or runtime behavior.

# 6. GitNexus Non-Authority Controls
| Control | Mandatory Rule |
| --- | --- |
| Read-only token | GitNexus must not have write, merge, deploy, production, or database credentials. |
| Report freshness | Report must match current base/head commit. Stale reports block review readiness. |
| Human review | GitNexus output requires reviewer acknowledgement and cannot be treated as approval. |
| Limitations | Report must disclose unsupported languages, generated files, ignored paths, missing dependency graphs, and confidence gaps. |
| No evidence suppression | GitNexus and generator must not hide failed tests, failed scans, waivers, or known limitations. |
| No production mutation | No tool in this runbook may deploy, mutate runtime, modify database, or alter production configuration. |

# 7. Derived Artifact Template Skeleton

derived_artifacts:

pr_mr_avci_summary: "derived/avci-summary.md"

release_readiness_summary: "derived/release-readiness.md"

rollback_checklist: "rollback/rollback-safe-disable.md"

test_evidence_index: "derived/test-evidence-index.md"

security_evidence_index: "derived/security-evidence-index.md"

architecture_impact_summary: "derived/architecture-impact.md"

gitnexus_summary: "gitnexus/gitnexus-summary.md"

improvement_candidates: "derived/improvement-backlog.md"

review_required:

architecture: true

security: true

qa: true

devsecops: true

dba: "if database impact"

sre: "if operational impact"

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

