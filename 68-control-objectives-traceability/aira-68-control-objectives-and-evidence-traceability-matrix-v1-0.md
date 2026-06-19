---
title: "Control Objectives and Evidence Traceability Matrix"
doc_id: "AIRA-68"
version: "v1.0"
status: "final"
category: "Control objectives and traceability"
source_docx: "AIRA_68_Control_Objectives_and_Evidence_Traceability_Matrix_v1.0.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 68-control-objectives-traceability
  - final
  - aira-68
---



# Control Objectives and Evidence Traceability Matrix



AIRA

AI-Native Enterprise Platform

Control Objectives and Evidence Traceability Matrix

AIRA-DOC-068 | v1.0 | Executable Governance, Audit Traceability, Evidence Assurance, and Industry Alignment Standard

Discipline First. Automation Second. Intelligence Third. AVCI Always.
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-068 |
| Document Title | AIRA Control Objectives and Evidence Traceability Matrix |
| Version | v1.0 - Initial Executable Governance and Assurance Matrix Standard |
| Canonical Filename | AIRA_68_Control_Objectives_and_Evidence_Traceability_Matrix_v1.0.docx |
| Status | Draft for Architecture Review Board, CAB, Security Governance, DevSecOps, AI Governance, SRE, DBA, QA/SDET, Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; DevSecOps Lead; Security Architecture; QA/SDET; DBA; SRE; Platform Engineering; AI Governance; Knowledge Governance; Internal Audit |
| Primary Parents | 01A v1.2; 01 v3.2; 01B v1.2; 02 v5.2; 11 v3.3; 11A v1.3; 20 v1.3; 62 v1.0; 63 v1.0; 64 v1.0; 65 v1.0; 66 v1.0; 67 v1.0 |
| MicroFunction Baseline | 10 v3.4; 10A v2.4; 10B v2.3; 10C v2.3; 10D v2.3; 10E v1.3 |
| External Alignment | NIST SSDF SP 800-218; NIST AI RMF / NIST AI 600-1; OWASP ASVS; SLSA v1.2; OpenTelemetry; CloudEvents; OPA/Rego; CycloneDX; ISO-aligned control mindset |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Control-Objectives-and-Traceability / 68 / v1.0 / |

# 1. Executive Summary

AIRA has matured from a documentation-centered architecture baseline into an executable governance program. This standard defines the control objective and evidence traceability matrix that connects AIRA intent, implementation control, evidence artifact, review authority, operational assurance, and continuous improvement. It is the bridge between enterprise standards and machine-verifiable governance.

The matrix must be used to prove that AIRA controls are not merely documented. They are implemented through CI/CD gates, Policy-as-Code, architecture fitness functions, evidence manifests, PRR/ORR gates, Resilience Lab tests, runtime telemetry, GitNexus impact analysis, audit records, waivers, approvals, and improvement loops.

Mandatory Practice Statement

No AIRA artifact, service, MicroFunction, Dynamic Workspace component, AI agent, pipeline, runtime configuration, policy, API/event contract, database migration, or production-bound release is enterprise-ready unless its control objectives map to implementation controls, evidence artifacts, owners, classifications, acceptance criteria, assurance results, and improvement paths. Missing traceability is a blocking governance defect unless formally waived with compensating controls and expiry.

Figure 1 - Control objectives and evidence traceability control plane

# 2. Purpose, Scope, and Authority
| Area | Standard Position |
| --- | --- |
| Purpose | Define the authoritative matrix model for tracing AIRA control objectives to standards, implementation gates, evidence artifacts, owners, classifications, verification methods, external frameworks, and improvement actions. |
| Scope | All AIRA standards, repositories, pipelines, evidence packs, MicroFunctions, Dynamic Workspace components, API/event contracts, database changes, AI agents, policies, prompts, runtime configurations, PRR/ORR records, Resilience Lab outputs, and production changes. |
| Authority | Subordinate to ARB/CAB/Security Governance final authority, but mandatory as the evidence traceability method for PR/MR, release, audit, exception, assurance, and continuous-improvement review. |
| Conflict Rule | Where sources conflict, apply the stricter control temporarily, create an AVCI reconciliation item, assign owner and due date, and route final authority through ARB/CAB/security/data-governance as appropriate. |

# 3. Traceability Model

Each control objective must be expressed as a traceable record, not as narrative only. The record must identify source authority, implementation mechanism, evidence artifact, gate result, owner, reviewer, classification, residual risk, waiver status, and improvement linkage.
| Traceability Field | Required Meaning |
| --- | --- |
| control_objective_id | Unique AIRA control objective identifier, for example ACO-SEC-001 or ACO-MF-004. |
| control_statement | Plain-language statement of the control intent and mandatory outcome. |
| aira_source_refs | AIRA documents, sections, registers, runbooks, standards, MicroFunction documents, or CI/CD guides that define the control. |
| external_refs | External control or assurance references such as NIST SSDF, NIST AI RMF, OWASP ASVS, SLSA, OPA, OpenTelemetry, CloudEvents, or CycloneDX where applicable. |
| implementation_control | Executable mechanism: CI job, OPA policy, test, scan, schema check, architecture fitness function, PRR/ORR gate, runbook, runtime guard, or manual review. |
| evidence_artifacts | Machine-readable and human-readable proof: manifest, test report, scan, SBOM/provenance, trace, audit, GitNexus, dashboard, approval, waiver, or rollback proof. |
| decision_gate | Pass, fail, warning, conditional, waived, expired waiver, deferred, or not applicable with approved reason. |
| owner_and_reviewer | Named accountable owner, checker, approver, evidence custodian, and independent audit reviewer where required. |
| classification_and_retention | Data classification, handling rule, retention period, redaction rule, and evidence storage location. |
| improvement_path | Backlog, Auto-Heal/Learn/Improve candidate, waiver remediation, control update, runbook update, or standard revision. |

Figure 2 - Minimum matrix fields for traceable assurance

# 4. Control Objective Domains

The following domains define the minimum AIRA control objective structure. Detailed matrix rows may be implemented in spreadsheet, database, or JSON/YAML manifest form, but the semantic fields below must remain consistent.
| Domain ID | Control Domain | Primary AIRA Sources | Minimum Evidence |
| --- | --- | --- | --- |
| ACO-ARCH | Architecture and Design Integrity | 01A, 02, 03, 10-10E, 63 | ADR/TDL, architecture fitness, boundary test, CODEOWNERS review, PRR/ORR result. |
| ACO-AVCI | AVCI Evidence and Audit Traceability | 01, 01B, 11A, 20, 66 | Evidence manifest, audit event, owner/reviewer, classification, evidence retention, improvement backlog. |
| ACO-DEVSEC | DevSecOps and Secure Delivery | 11, 11A, 20, 65, 66 | Build, tests, SAST/SCA/secrets/DAST, OPA/Conftest, GitNexus, SBOM/provenance, approvals. |
| ACO-MF | MicroFunction Runtime and Config Governance | 10-10E, 20, 63, 64 | Runtime config validation, catalog steps, idempotency, outbox, audit, observability, rollback. |
| ACO-API | API/Event/Schema/DLQ/Replay Governance | 15/15A, 20, 67 | OpenAPI/AsyncAPI diff, schema compatibility, CloudEvents validation, DLQ/replay evidence. |
| ACO-DATA | Database, Data, and Classification Governance | 16/16A/16B, 17/17A, 66 | Flyway output, RLS review, classification, redaction proof, migration rollback/forward-fix. |
| ACO-AI | AI Governance, Guardrails, and Agent Controls | 42 series, 43, 58, 65, 66 | Model route, guardrail result, tool policy, trust tier, human approval, evaluation evidence. |
| ACO-DW | Dynamic Workspace and UX Governance | 12A, 54-61, 20, 63 | Template registry, API contract, policy filter, accessibility, telemetry, rollback, evidence. |
| ACO-OBS | Observability and Operational Assurance | 31/31A, 63, 64, 66 | OTel trace, Log4j2 redaction, Sentry, Loki, Tempo, Grafana dashboard, alert, audit. |
| ACO-RES | Resilience, Performance, Concurrency, and Chaos | 64, 20, 63, 67 | Load/concurrency tests, idempotency, DLQ/replay, failure injection, recovery evidence. |
| ACO-CHANGE | Change, Release, PRR/ORR, and Rollback | 30/30A, 63, 20 | CAB/ARB decision, PRR/ORR checklist, release readiness, rollback/safe-disable proof. |
| ACO-SUPPLY | Supply Chain, SBOM, Provenance, and Dependency Integrity | 20, 66, 65 | SBOM, provenance/attestation, artifact digest, image scan, license/dependency review. |

# 5. External Alignment Crosswalk
| External Reference | AIRA Control Objective Use | Required Evidence Binding |
| --- | --- | --- |
| NIST SSDF SP 800-218 | Secure software development practices, vulnerability mitigation, secure build, review, verification, and response alignment. | Secure SDLC evidence, SAST/SCA/secrets, test reports, remediation evidence, release gate records. |
| NIST AI RMF and NIST AI 600-1 | AI risk management, generative AI trustworthiness, model-route, guardrail, evaluation, and human oversight alignment. | AI route evidence, guardrail decisions, red-team/eval reports, classification and human approval records. |
| OWASP ASVS | Application and API security verification, secure coding, authentication, session, access control, input validation, API security. | ASVS-mapped test cases, authenticated DAST, abuse-case evidence, API contract security review. |
| SLSA v1.2 | Supply-chain integrity, build provenance, tamper resistance, source-to-artifact traceability. | SBOM, provenance, artifact digest, signed/integrity-checked artifact, dependency lock evidence. |
| OpenTelemetry | Trace, metric, log correlation, semantic conventions, observability and trace reconstruction. | Trace export, span attributes, metric evidence, log correlation, dashboard and alert references. |
| CloudEvents | Common event metadata for API/event governance and traceability. | Event envelope validation, id/source/type/time, trace/correlation/causation/evidence fields. |
| OPA/Rego and Conftest | Policy-as-code decisioning for runtime, CI/CD, environment, data, agent, and tool actions. | Policy bundle, Rego tests, decision logs, deny-by-default evidence, waiver records. |
| CycloneDX / SBOM practices | Machine-readable component inventory and evidence attachment model. | SBOM file, component lineage, vulnerability disposition, provenance and evidence references. |

# 6. Core Control Objectives and Evidence Traceability Matrix
| Control ID | Control Objective | AIRA Source | Evidence Artifact | Acceptance Rule |
| --- | --- | --- | --- | --- |
| ACO-ARCH-001 | Architecture boundaries are preserved. | 01A/02/03/10B | ArchUnit/Semgrep, CODEOWNERS, PR review | No domain-to-adapter dependency; no direct DB/Kafka/model provider calls. |
| ACO-AVCI-001 | Every artifact is AVCI-complete. | 01/01B/20/66 | evidence-manifest.json, PR/MR AVCI summary | Owner, source, classification, verification, improvement path complete. |
| ACO-DEVSEC-001 | Security gates fail closed. | 11/11A/20/65 | SAST, SCA, secrets, DAST, OPA, waiver record | Critical/high findings block or carry approved waiver with expiry. |
| ACO-SUPPLY-001 | Artifact lineage is reproducible. | 20/66 | SBOM, provenance, digest, image scan | Artifact source, dependency, build, digest, and release evidence linked. |
| ACO-MF-001 | MicroFunctions execute inside governed envelope. | 10/10B/10D/10E | runtime config validation, audit, trace, policy decision | Identity, classification, idempotency, outbox, audit, observability present. |
| ACO-API-001 | APIs and events are contract-first. | 15/20/67 | OpenAPI/AsyncAPI diff, schema compatibility | Breaking changes require versioning, migration plan, consumer approval. |
| ACO-EVT-001 | Event publication is outbox-governed. | 10B/20/67 | outbox/inbox test, CloudEvents validation | No business logic direct Kafka publish; DLQ/replay path exists. |
| ACO-DATA-001 | Database change is migration-governed. | 16/20 | Flyway validate/info/clean-migrate, DBA review | No manual production DDL; rollback/forward-fix defined. |
| ACO-AI-001 | AI is governed and cannot self-approve. | 42/43/58/65 | model route, guardrail, tool policy, approval | No direct provider calls; no agent production credentials; human approval for protected action. |
| ACO-DW-001 | Dynamic Workspace is backend-governed. | 12A/54-61/20 | template evidence, policy result, API binding | No frontend business authority or bypass of MicroFunction/API/policy controls. |
| ACO-OBS-001 | Critical flows are reconstructable. | 31A/63/66 | trace, log, metric, audit, dashboard, evidence_ref | Trace reconstruction works without secrets or restricted payload leakage. |
| ACO-RES-001 | Heavy transactions are resilient. | 64/20/67 | load, concurrency, retry, DLQ/replay, chaos evidence | Duplicate-safe, retry-safe, bounded, observable, recoverable behavior proven. |
| ACO-REL-001 | Production readiness is evidence-gated. | 63/20/30 | PRR/ORR checklist, rollback, CAB/ARB approval | Staging/pilot/production cannot proceed without readiness evidence. |
| ACO-POL-001 | Policy-as-code decisions are testable and auditable. | 65/11A/20 | OPA test, decision log, policy bundle hash | Protected action denies by default and records decision evidence. |
| ACO-IMP-001 | Auto-* loops are proposal-driven. | 43/11/65 | candidate proposal, tests, review, backlog | No silent mutation; improvements become PR/MR or approved knowledge/runbook updates. |

# 7. Evidence Artifact Classes
| Evidence Class | Examples | Retention / Handling Rule |
| --- | --- | --- |
| Design and architecture | ADR, TDL, design record, diagram source, Mermaid render, CODEOWNERS review. | Retain with source and release record; classify to match system/data impact. |
| Build and tests | Build log, unit/component/contract/E2E reports, mutation/coverage, resilience tests. | Commit-bound and immutable after release; use synthetic data only. |
| Security and policy | SAST, SCA, secrets, DAST, abuse-case, OPA/Conftest, SBAC decisions, waivers. | Critical/high findings require closure or time-bound waiver with compensating control. |
| Supply chain | SBOM, provenance, artifact digest, signature/integrity proof, dependency license review. | Retain for release lifetime and audit retention period. |
| Runtime observability | OpenTelemetry trace, Log4j2 redaction, Sentry, Loki, Tempo, Grafana, alert, audit event. | Redact secrets/PII; retain query links and exported evidence where required. |
| Operational readiness | PRR/ORR checklist, runbook, SLO/SLA, support model, rollback, DR/backup validation. | Required for staging, pilot, production-like, and production promotion. |
| Improvement evidence | Incident/RCA, Auto-Heal/Learn/Improve proposal, remediation evidence, backlog item, lesson learned. | Link to source findings and closure evidence; never self-approved by AI. |

# 8. Gate Severity and Decision Model
| Severity | Meaning | Decision Treatment |
| --- | --- | --- |
| Advisory | Improvement recommended but risk is low and no protected gate is violated. | Record backlog item or accept with rationale. |
| Warning | Control weakness exists but can be mitigated within the same release or follow-up window. | Owner acknowledgement and follow-up required. |
| Blocking | Merge, activation, or promotion is not allowed until fixed or formally waived. | Fix or obtain approved waiver with compensating control and expiry. |
| Critical Block | Security, production, data, policy, identity, evidence, or rollback defect creates unacceptable risk. | Immediate escalation; production promotion prohibited. |
| Waived | Temporary risk acceptance approved by authorized role. | Must include owner, expiry, compensating control, evidence ref, and remediation plan. |
| Not Applicable | Control does not apply to the change type. | Requires reason, owner, and reviewer confirmation for P0/P1 changes. |

# 9. Assurance Operating Model

Control assurance is a recurring loop. It begins with source authority, moves through implementation and evidence generation, and ends only when findings, waivers, and operational signals feed back into standards, tests, policy, runbooks, and backlog updates.

Figure 3 - Control assurance and continuous improvement loop
| Assurance Activity | Cadence | Responsible Roles | Evidence Output |
| --- | --- | --- | --- |
| PR/MR evidence review | Every material change | Maker, checker, CODEOWNERS, DevSecOps, Security as needed | PR/MR AVCI summary, evidence manifest, gate result. |
| Release assurance | Every release candidate | DevSecOps, QA/SDET, SRE, Security, DBA, Product Owner | Release evidence pack, PRR/ORR, rollback, approvals. |
| Quarterly control assurance | Quarterly | Architecture, Security, Internal Audit, DevSecOps, SRE | Control coverage report, open risk, expired waiver, improvement plan. |
| Incident-driven assurance | On incident or escaped defect | SRE, Security, QA, Development, Architecture | RCA, trace reconstruction, remediation evidence, new fitness test. |
| Canonical baseline assurance | After document batch or release train | Solutions Architecture Office / IT Head, Knowledge Governance | Register update, supersedence map, 00D reconciliation items. |

# 10. Machine-Readable Matrix Record

The matrix should be maintained in a machine-readable representation so CI/CD, Policy-as-Code, GitNexus, System Builder, and audit tooling can validate coverage automatically. The following minimum JSON shape is normative for automation design.

{
  "control_objective_id": "ACO-DEVSEC-001",
  "control_statement": "Security gates fail closed for protected changes.",
  "aira_source_refs": ["AIRA-DOC-011", "AIRA-DOC-011A", "AIRA-DOC-020", "AIRA-DOC-065"],
  "external_refs": ["NIST-SSDF", "OWASP-ASVS", "SLSA"],
  "classification": "INTERNAL CONFIDENTIAL",
  "implementation_controls": ["sast", "sca", "secret_scan", "opa_tests", "authenticated_dast"],
  "required_evidence": ["sast_report", "sca_report", "secret_scan_report", "policy_decision_log", "waiver_record"],
  "decision_gate": "blocking",
  "owner": "Security Architecture",
  "reviewer": "DevSecOps Lead",
  "status": "pass|fail|waived|not_applicable",
  "waiver": {"allowed": true, "expiry_required": true, "compensating_control_required": true},
  "improvement_path": "security-remediation-backlog"
}

# 11. RACI
| Role | RACI Position | Primary Responsibility |
| --- | --- | --- |
| Solutions Architecture Office / IT Head | A/R | Owns standard, matrix direction, control-objective taxonomy, ARB/CAB escalation, and canonical baseline alignment. |
| Enterprise Architecture | R | Maps AIRA principles, architecture controls, fitness functions, and bounded-context evidence. |
| DevSecOps Lead | A/R | Implements CI/CD evidence gates, evidence manifest validation, supply-chain controls, and promotion evidence. |
| Security Architecture | A/R | Owns OPA/SBAC, threat/abuse cases, DAST, secrets, waivers, remediation, and security control mapping. |
| QA/SDET | R | Maps test evidence, deterministic fixtures, contract tests, resilience validation, and acceptance criteria. |
| SRE / Platform Engineering | R | Maps observability, runtime health, SLO/SLA, PRR/ORR, rollback, and operational evidence. |
| DBA / Data Governance | R | Maps Flyway, RLS, schema, retention, classification, and data-fix evidence. |
| AI Governance / AI Engineering | A/R | Maps AI model-route, guardrail, evaluation, agent/tool action, and human-approval evidence. |
| Internal Audit | C/I | Reviews control coverage, evidence completeness, expired waivers, and continuous assurance effectiveness. |

# 12. Implementation Roadmap
| Phase | Execution Focus | Exit Criteria |
| --- | --- | --- |
| Phase 0 - Register | Create ACO taxonomy and seed initial matrix from 01A, 01, 01B, 10-10E, 11/11A/20, 62-67. | Matrix owner assigned, canonical source references added, open reconciliation items logged. |
| Phase 1 - Evidence binding | Bind evidence classes from AIRA-DOC-066 to each control objective. | Every P0/P1 control has required evidence artifact list and retention rule. |
| Phase 2 - CI/CD enforcement | Connect ACO records to pipeline gates and policy-as-code checks. | CI can detect missing evidence, missing owner, stale version, and critical gate failures. |
| Phase 3 - Runtime assurance | Bind observability, audit, PRR/ORR, and Resilience Lab evidence to controls. | Critical runtime flows can be reconstructed and assurance-tested. |
| Phase 4 - External crosswalk | Complete mapping to NIST SSDF, NIST AI RMF, OWASP ASVS, SLSA, OPA, OTel, CloudEvents, and SBOM practices. | Audit-ready crosswalk report available and reviewed quarterly. |
| Phase 5 - Continuous assurance | Use findings, waivers, incidents, GitNexus drift, and Auto-* candidates to improve controls. | Quarterly control assurance cycle produces action plan and closure evidence. |

# 13. Acceptance Criteria

Every P0/P1 AIRA control objective has owner, source authority, external reference where applicable, implementation control, evidence artifacts, decision gate, classification, and retention rule.

Every production-bound change can link PR/MR evidence, CI/CD gate results, policy decisions, security evidence, observability evidence, rollback proof, and approval record to at least one control objective.

Every waiver is time-bound, risk-owned, compensating-control-backed, evidence-linked, and tracked for expiry and remediation.

AIRA-DOC-066 evidence manifest can represent the control objective evidence required by this matrix.

Policy-as-Code checks can reject protected changes that omit mandatory control-objective evidence.

Internal Audit can sample a control objective and reconstruct source, implementation, test, runtime evidence, decision, approval, waiver, and improvement path.

# 14. Anti-Patterns and Rejection Rules
| Anti-Pattern | Required Response |
| --- | --- |
| Control exists only in a Word document and has no implementation gate or evidence binding. | Reject as incomplete; create implementation/evidence backlog item. |
| Evidence exists but cannot be traced to owner, source, commit, artifact, classification, or retention path. | Reject evidence pack until manifest is corrected. |
| External framework mapping is asserted without tests, scans, or evidence. | Treat as advisory claim only; require verifiable mapping. |
| AI/System Builder claims a control is satisfied without CI/CD, policy, scan, test, or human review proof. | Reject claim as authority; require evidence and maker-checker validation. |
| Waiver has no expiry, compensating control, risk owner, or remediation path. | Reject waiver or escalate as non-conformance. |
| Production release proceeds without PRR/ORR, rollback, observability, and evidence manifest links. | Block promotion and escalate to CAB/ARB. |

# 15. Open Reconciliation Items
| ID | Issue | Required Treatment | Severity | Owner |
| --- | --- | --- | --- | --- |
| RI-068-001 | Existing source packs contain references to older MicroFunction and DevSecOps versions. | Cross-reference validation must flag stale references and route to register 00D / canonical baseline update. | Medium | Solutions Architecture Office |
| RI-068-002 | 11A duplicate numbering remains a known source-pack issue. | Do not silently renumber; track as 00D reconciliation item and distinguish parent 11 vs companion 11A. | Medium | Architecture Board |
| RI-068-003 | 41B / 44 System Builder overlap may affect control authority mapping. | Record governing source decision in canonical register before automation. | Medium | Architecture Board |
| RI-068-004 | External framework mappings may change over time. | Refresh external alignment during quarterly assurance or material standard updates. | Low | Security / Internal Audit |
| RI-068-005 | Matrix should eventually be implemented as database-backed registry or YAML/JSON repository. | Start with document and spreadsheet/export, then automate as part of System Builder governance. | Low | DevSecOps / Knowledge Governance |

# 16. AVCI Compliance Summary
| AVCI Property | How This Standard Satisfies It |
| --- | --- |
| Attributable | Defines control objective IDs, owners, source references, external references, gate owners, reviewers, evidence custodians, and approval paths. |
| Verifiable | Requires evidence artifacts, CI/CD gates, policy tests, security scans, architecture fitness, runtime telemetry, PRR/ORR, Resilience Lab outputs, and audit sampling. |
| Classifiable | Requires classification and handling for control records, evidence artifacts, logs, traces, prompts, screenshots, model routes, retention, and redaction. |
| Improvable | Links every finding, failed gate, waiver, incident, GitNexus drift, assurance result, and control gap to backlog, Auto-* candidate, runbook, test, or standard update. |

# 17. Change Log
| Version | Date | Summary |
| --- | --- | --- |
| v1.0 | 2026-06-18 | Initial AIRA Control Objectives and Evidence Traceability Matrix standard. Establishes control-objective domains, traceability fields, external alignment crosswalk, core matrix records, assurance operating model, machine-readable record shape, RACI, roadmap, acceptance criteria, and AVCI summary. |

