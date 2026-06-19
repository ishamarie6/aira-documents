---
title: "PoC2 Repository Bootstrap Branch Governance CODEOWNERS and PRMR Template Pack"
doc_id: "AIRA-45C"
version: "v1.0"
status: "draft"
category: "PoC2 and mortgage experience"
source_docx: "AIRA_45C_PoC2_Repository_Bootstrap_Branch_Governance_CODEOWNERS_and_PRMR_Template_Pack_v1.0_Draft.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 45-poc2-mortgage-experience
  - draft
  - aira-45c
---



# PoC2 Repository Bootstrap Branch Governance CODEOWNERS and PRMR Template Pack



AIRA

AI-Native Enterprise Platform

PoC 2 Repository Bootstrap, Branch Governance, CODEOWNERS, and PR/MR Template Pack

Repository Baseline | Branch Protection | CODEOWNERS | PR/MR Evidence | AI-Use Declaration

# Document Control
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-045C |
| Document Title | PoC 2 Repository Bootstrap, Branch Governance, CODEOWNERS, and PR/MR Template Pack |
| Recommended Filename | AIRA_45C_PoC2_Repository_Bootstrap_Branch_Governance_CODEOWNERS_and_PRMR_Template_Pack_v1.0_Draft.docx |
| Version | v1.0 Draft |
| Status | Draft for Architecture / DevSecOps / Security / QA / Development Team Review and Controlled Execution |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Primary Execution Owner | DevSecOps Lead / Repository Owner |
| Co-Owners | Enterprise Architecture; Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; DBA/Data Governance; Platform Engineering; SRE/Operations; AI Governance; Internal Audit |
| Primary Audience | Software Developers; DevSecOps Engineers; QA/SDET; Security; DBA; Platform Engineering; SRE; AI Governance; Internal Audit; System Builder Operators; AI Coding Assistant Users |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / PoC2 / AIRA-DOC-045C / v1.0/ |
| Approval Path | Draft -> Architecture / DevSecOps / Security / QA Review -> Controlled Execution -> Exit Evidence -> Register Update |
| Review Cadence | At PoC 2 kickoff; every sprint during PoC 2; after pipeline, scanner, GitNexus, evidence, or governance changes; before reuse by future AIRA modules |
| Supersedence | Companion document to AIRA-DOC-045 and AIRA-DOC-045A. Does not supersede AIRA-DOC-042C, AIRA-DOC-045, or parent standards. |

# Mandatory Practice Statement

PoC 2 artifacts are not accepted because scripts run, templates exist, or reports are generated. They are accepted only when owner, source, classification, test evidence, security evidence, GitNexus impact, rollback/safe-disable path, reviewer decision, and improvement path are complete and traceable. AI and automation may draft and generate candidate artifacts, but they must not approve, merge, deploy, waive controls, mutate production, or become authority.

# 1. Executive Summary

This companion document defines the repository and branch-control baseline required before PoC 2 pipeline work begins. The repository is the first control surface of the System Factory. If branch protection, CODEOWNERS, PR/MR evidence templates, issue linkage, and evidence folder conventions are absent, PoC 2 cannot produce trustworthy evidence.

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

# 2. Repository Bootstrap Requirements
| Requirement ID | Requirement | Acceptance Evidence |
| --- | --- | --- |
| 045C-REP-001 | Repository must have named owner, backup owner, and classification. | Repository metadata record |
| 045C-REP-002 | Default branch must be protected from direct pushes. | Branch protection screenshot/export |
| 045C-REP-003 | CODEOWNERS must require independent review for protected paths. | CODEOWNERS file and review rule |
| 045C-REP-004 | PR/MR template must require AVCI, tests, scans, rollback, evidence, and AI-use declaration. | Template committed under .github / .gitlab or docs/templates |
| 045C-REP-005 | AGENTS.md must define AI-assisted execution boundaries. | AGENTS.md committed and referenced |
| 045C-REP-006 | Evidence folder convention must be established. | evidence/README.md and sample manifest |
| 045C-REP-007 | Issue/ticket linkage must be mandatory. | Branch naming or PR/MR template rule |

# 3. Recommended Repository Structure

repo-root/

.github/ or .gitlab/

workflows/ or ci/

pull_request_template.md

.aira/

evidence-manifest.schema.yaml

policy/

templates/

AGENTS.md

CODEOWNERS

README.md

docs/

adr/

runbooks/

evidence/

src/

tests/

policy/opa/

api/openapi/

api/asyncapi/

db/migration/

evidence/

poc2/

pr-mr/<pr-number>/

# 4. Branch Protection Rules
| Rule | Minimum Setting | Reason |
| --- | --- | --- |
| Protected default branch | Required | Prevents uncontrolled mutation of baseline |
| Require PR/MR before merge | Required | Forces evidence and maker-checker review |
| Require status checks | Build, tests, scans, evidence, GitNexus | Prevents pipeline bypass |
| Require CODEOWNERS review | Required for protected paths | Enforces subject-matter review |
| Dismiss stale approvals | Recommended | Prevents approval of changed content |
| Require linear history / signed commits | Recommended where supported | Improves traceability |
| Restrict force-push and deletion | Required | Prevents evidence and history tampering |

# 5. CODEOWNERS Minimum Pattern

# AIRA PoC 2 CODEOWNERS - draft baseline

*                                      @aira-dev-lead @aira-devsecops-lead

/.github/                              @aira-devsecops-lead @aira-security-architecture

/.gitlab/                              @aira-devsecops-lead @aira-security-architecture

/.aira/                                @aira-architecture @aira-devsecops-lead @aira-internal-audit

/policy/                               @aira-security-architecture @aira-devsecops-lead

/api/openapi/                          @aira-architecture @aira-qa-lead

/api/asyncapi/                         @aira-architecture @aira-qa-lead

/db/migration/                         @aira-dba @aira-security-architecture

/src/**/security/                      @aira-security-architecture

/src/**/adapter/                       @aira-architecture @aira-dev-lead

/evidence/                             @aira-devsecops-lead @aira-internal-audit

/docs/runbooks/                        @aira-sre @aira-devsecops-lead

# 6. PR/MR Template

# AIRA PR/MR Evidence Summary

## Controlled Intake

- Ticket / Intake ID:

- Owner / Maker:

- Checker / Reviewer:

- Classification:

- Bounded Context / Component:

- Change Type: code | config | policy | test | doc | pipeline | evidence

## AVCI Summary

- Attributable:

- Verifiable:

- Classifiable:

- Improvable:

## AI-Assisted Work Declaration

- AI tools used:

- Purpose:

- Human reviewer:

- Confirmation: AI did not approve, merge, deploy, or mutate production.

## Verification Evidence

- Build:

- Unit tests:

- Integration / Testcontainers:

- Contract tests:

- OPA/SBAC tests:

- Architecture fitness:

- PoC 1 / PoC 1A regression:

## Security and Supply Chain Evidence

- Secret scan:

- SAST:

- SCA / dependency scan:

- SBOM:

- Container scan:

- DAST:

- Waivers:

## GitNexus and Derived Artifacts

- GitNexus report:

- Code map / impact map:

- Derived AVCI summary:

- Release-readiness summary:

## Rollback and Operations

- Rollback / forward-fix / safe-disable plan:

- Observability evidence:

- Known limitations:

- Improvement backlog:

# 7. Repository Acceptance Checklist
| Checklist Item | Required Status |
| --- | --- |
| Default branch protected | Pass before PoC 2 PR/MR |
| CODEOWNERS enforced | Pass before PoC 2 PR/MR |
| PR/MR template complete | Pass before PoC 2 PR/MR |
| Evidence folder initialized | Pass before evidence pack generation |
| AGENTS.md boundaries documented | Pass before AI-assisted coding |
| No direct production secrets or credentials in repo | Pass before execution |
| Repository classification documented | Pass before execution |

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

