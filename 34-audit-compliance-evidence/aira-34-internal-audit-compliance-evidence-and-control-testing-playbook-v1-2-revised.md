---
title: "Internal Audit Compliance Evidence and Control Testing Playbook"
doc_id: "AIRA-34"
version: "v1.2"
status: "revised"
category: "Audit compliance and evidence"
source_docx: "AIRA_34_Internal_Audit_Compliance_Evidence_and_Control_Testing_Playbook_v1.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 34-audit-compliance-evidence
  - revised
  - aira-34
---



# Internal Audit Compliance Evidence and Control Testing Playbook



AIRA

AI-Native Enterprise Platform

Internal Audit, Compliance Evidence, and Control Testing Playbook

v1.2 Revised

Continuous Assurance - Evidence Sampling - DevSecOps Controls - AI Governance Assurance - AVCI Evidence
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-034 |
| Canonical Filename | AIRA_34_Internal_Audit_Compliance_Evidence_and_Control_Testing_Playbook_v1.2_Revised.docx |
| Version | v1.2 - Revised audit, evidence, continuous assurance, Dynamic Workspace, MicroFunction, DevSecOps, security, observability, resilience, AI governance, and control-testing update |
| Supersedes | 34-AIRA_Internal_Audit_Compliance_Evidence_and_Control_Testing_Playbook_v1.1_Aligned.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Internal Audit, Compliance, Security, DevSecOps, SRE/Operations, Data Governance, AI Governance, QA/SDET, CAB, and Architecture Review Board review |
| Owner | Solutions Architecture Office / IT Head; Internal Audit / Compliance Office |
| Co-Owners | Enterprise Architecture; Security Architecture; DevSecOps Lead; QA/SDET Lead; SRE / Operations Lead; Data Governance; AI Governance; DBA; Product Owner; Business Process Owners; Service Desk Owner |
| Primary Companion | 31/31A Operations and Observability v1.2; 24B Incident/Auto-Heal v1.2; 29 UAT v1.2; 30/30A Release and Reversibility v1.4/v1.2; 35 BCDR v1.2; 36 Training v1.2; 20 CI/CD Evidence v1.2; 45 PoC2 System Factory v1.2 |
| Revised Inputs Considered | 09 v3.2 Greenfield Environment; 19B v1.2 Sprint 0; 20 v1.2 CI/CD Evidence; 24B v1.2 Incident; 29 v1.2 UAT; 30/30A v1.4/v1.2 Change; 31/31A v1.2 Operations/Observability; 35 v1.2 BCDR; 36 v1.2 Training; 39A/39B/39C Workstation/System Builder Lite; 45 v1.2 PoC2 System Factory |
| Governing AIRA Sources | 01/01A AVCI and Enterprise Design Principles; 02 Blueprint; 03 Developer Guide; 04 Technology Stack; 05 Information Nervous System; 08 Testing; 10 MicroFunction family; 12A and 41/46-61 Dynamic Workspace; 15/15A API; 16/16A/16B Database/Flyway; 17/17A Security; 19 GitNexus; 22A AI Registry; 25A MVP Acceptance; 26A Classification; 32 SBAC; 42 AI Governance; 43 Continuous Improvement |
| External Alignment Reference | NIST SP 800-218 SSDF; OWASP ASVS 5.0.0; OpenTelemetry Semantic Conventions; SLSA v1.2 |
| Review Cadence | Quarterly; unscheduled after regulatory change, material architecture/security/AI governance change, production incident, Sev-1/Sev-2 issue, CAB waiver, failed control test, or audit finding |
| Evidence Path | OpenKM Tier-0 / AIRA / Audit-and-Compliance / Control-Testing / v1.2 / |
| Mandatory Practice Statement No AIRA control shall be considered audit-ready unless its design, operating effectiveness, owner, evidence source, retention rule, classification, testing method, exception path, remediation workflow, and improvement route are defined, sampled, and traceable. Evidence must be produced by the system of work, not reconstructed manually after the fact. |
| --- |

# 1. Executive Summary

This v1.2 revision strengthens AIRA-DOC-034 from a baseline audit playbook into a continuous assurance and evidence-testing control for an AI-native enterprise platform. It translates AIRA governance into repeatable audit procedures for engineering, security, operations, data, Dynamic Workspace, MicroFunction runtime, API/eventing, CI/CD, AI agents, model routing, incident response, BCDR, business readiness, and change governance.
| Management Intent Audit readiness is an engineering property. Controls must generate evidence during normal work through Git, CI/CD, GitNexus, OpenKM, PostgreSQL, Zammad, Wazuh/TheHive/Cortex, OpenTelemetry, Sentry/Loki/Tempo/Grafana, Vault, Keycloak, OPA, Harness, LiteLLM, NeMo Guardrails, Temporal/Flowable, Kafka, and Kubernetes evidence paths. Internal Audit validates that the evidence is complete, classifiable, tamper-resistant, sampled, retained, and tied to accountable owners. |
| --- |
| Strategic Outcome | How v1.2 Delivers It |
| --- | --- |
| Continuous audit readiness | Defines control ownership, evidence source, test method, frequency, classification, retention, and remediation route for critical AIRA controls. |
| Evidence by construction | Requires CI/CD, runtime, ticket, workflow, registry, policy, audit, and observability systems to produce evidence during work, not after-the-fact manual summaries. |
| AI governance assurance | Tests model routes, guardrails, prompt eligibility, agent registry, SBAC/OPA decisions, Harness tool actions, human approvals, and autonomy controls. |
| Operational resilience assurance | Tests incident records, BCDR drills, restore validation, DLQ/replay, outbox/inbox, telemetry toggles, rollback, compensation, and recovery evidence. |
| Management visibility | Defines dashboards for control health, evidence completeness, failed tests, overdue CAPA, waiver aging, exception expiry, and recurring findings. |

# 2. Purpose, Scope, and Authority
| Area | Requirement |
| --- | --- |
| Purpose | Define the audit operating model, evidence lifecycle, control-testing methodology, continuous compliance metrics, findings workflow, and audit-ready evidence expectations for AIRA. |
| In Scope | Plan, code, build, test, release, deploy, operate, recover, improve, AI governance, Dynamic Workspace, MicroFunctions, APIs/events, database/Flyway, identity/SBAC/OPA, CI/CD, observability, incident, BCDR, UAT, training, and change controls. |
| Out of Scope | Corporate audit procedures unrelated to AIRA, external auditor workpaper ownership, HR performance audits, procurement audits, or finance audits unless they supply AIRA control evidence. |
| Authority | Internal Audit and Compliance may request evidence and test controls. Control owners must provide traceable records. CAB/ARB/Security Governance/AI Governance/Data Governance decide high-risk exceptions and remediation priority. |
| Conflict Rule | Regulatory/legal requirements override local convenience. AIRA AVCI, security, data classification, release/CAB, AI governance, and architecture standards govern implementation-specific interpretations. Conflicts are logged as AVCI reconciliation items. |

# 3. Audit Operating Model and Control Universe
| Control Domain | Audit Focus | Minimum Evidence Source |
| --- | --- | --- |
| Governance and AVCI | Owner, source, version, classification, verifier, improvement path, waiver handling. | Document register, ADR/TDL, PR/MR AVCI summary, evidence pack, waiver register. |
| DevSecOps and supply chain | Build/test/security gates, SBOM, provenance, signed artifacts, SAST/SCA/secrets/IaC/container scan results. | CI/CD pipeline, GitHub/GitLab, artifact registry, SLSA/provenance, scan outputs. |
| GitNexus and code intelligence | Read-only derivative use, impact analysis, affected tests, architecture drift, agent-call boundaries. | GitNexus report tied to commit/PR; reviewer validation; no write/deploy authority evidence. |
| Dynamic Workspace | Backend-governed template lifecycle, policy filtering, accessibility, UX, workspace evidence, runtime telemetry. | Workspace registry, OpenAPI contracts, OPA decisions, audit events, UI tests, template approvals. |
| MicroFunction runtime | Configuration-first transactions, standard steps, idempotency, audit/outbox, policy, observability, rollback. | MicroFunction catalog/config, execution records, policy decisions, trace_id/evidence_ref, tests. |
| API and eventing | OpenAPI/AsyncAPI, Kafka, Avro, CloudEvents, schema evolution, outbox/inbox, DLQ/replay, consumers. | Contract registry, schema registry, compatibility tests, replay evidence, consumer idempotency tests. |
| Database and data | Flyway-only migration, PostgreSQL authority, RLS, seed data, retention, reconciliation, data fixes. | Flyway reports, migration checksums, DB change tickets, data reconciliation, rollback/restore tests. |
| Security and access | RBAC/ABAC/SBAC, OPA, Keycloak, Vault/secrets, SoD, least privilege, authenticated DAST, secure APIs. | Access review, OPA logs, Keycloak groups, Vault audit, DAST report, security findings/CAPA. |
| Operations and resilience | SLO/SLA, incidents, Zammad, BCDR, backup/restore, DLQ/replay, telemetry toggles, Auto-Heal controls. | Zammad tickets, SRE dashboards, BCDR test, incident timeline, restore proof, toggle audit. |
| AI governance | LiteLLM routes, model aliases, prompt registry, guardrails, agent registry, trust tiers, tool actions, human approval. | AI registry, guardrail logs, model invocation evidence, Harness action records, certification tests. |

# 4. Evidence Lifecycle and Chain-of-Custody
| Lifecycle Step | Required Control | Audit Test |
| --- | --- | --- |
| Create | Evidence is generated by source system during normal work and includes owner, source_ref, classification, timestamp, environment, and correlation IDs. | Sample evidence records against originating Git/CI/runtime/ticket/workflow records. |
| Capture | Evidence is stored or linked in approved evidence path; screenshots/files are malware-scanned and redacted where needed. | Verify OpenKM/evidence path, hash, retention, classification, and redaction status. |
| Correlate | Evidence links trace_id, request_id, commit_sha, build_id, ticket_id, policy_decision_id, run_id, workflow_id, or evidence_ref. | Trace one change from intake to PR/MR, CI, deployment, runtime, support, and closure. |
| Protect | Access follows SBAC/RBAC/ABAC and classification. Secrets, tokens, raw PII, raw prompts, and restricted payloads are prohibited in evidence unless approved. | Inspect access control, redaction, sampling, forbidden field checks, and retention controls. |
| Retain | Retention, disposal, legal hold, and supersedence rules are defined and applied. | Validate retention metadata and disposal/hold proof for sampled evidence. |
| Review | Control owner and checker review evidence for completeness, accuracy, and exception status. | Check reviewer identity, approval timestamp, finding linkage, waiver, and CAPA status. |
| Improve | Findings, failed gates, recurring issues, and evidence gaps feed backlog, policy update, runbook update, training, or Auto-Learn/Auto-Improve candidate. | Verify CAPA closure and post-remediation retest evidence. |
| Evidence Quality Rule Evidence must be attributable to a system, actor, tool, commit, policy decision, or workflow event. Unlinked screenshots, manually edited spreadsheets, unreviewed AI summaries, and informal chat claims are not authoritative unless tied to approved source evidence and reviewed by the control owner. |
| --- |

# 5. Control Testing Methodology
| Step | Testing Activity | Required Output |
| --- | --- | --- |
| CT-01 Define control | Identify control objective, owner, frequency, system of record, risk, classification, and required evidence. | Control test plan. |
| CT-02 Test design effectiveness | Verify the control is properly designed to prevent/detect/correct the risk and aligns with AIRA standards. | Design effectiveness conclusion. |
| CT-03 Select sample | Choose risk-based sample across period, environment, role, service, release, data class, or incident type. | Sample rationale and population evidence. |
| CT-04 Test operating effectiveness | Verify the control operated as designed for sampled items and exceptions are captured. | Pass/fail result with evidence links. |
| CT-05 Test evidence integrity | Check hash, provenance, source authority, classification, retention, redaction, and chain-of-custody. | Evidence integrity assessment. |
| CT-06 Rate finding | Classify deficiency as Critical, High, Medium, Low, or Observation and assign owner/date. | Finding record and CAPA. |
| CT-07 Validate remediation | Retest fix, compensating control, policy update, training update, or rollback/compensation. | Closure evidence and residual risk statement. |
| CT-08 Feed improvement | Route lessons to backlog, runbook, standards, control register, dashboard, or Auto-Learn candidate. | Improvement record and revision path. |

# 6. Key Control Testing Procedures
| Control Area | Minimum Test Procedure | Pass Criteria |
| --- | --- | --- |
| CI/CD gate evidence | Select PR/MR sample; verify build, unit/component/contract/security/architecture tests, SBOM, provenance, GitNexus, evidence pack, reviewer approval. | All required gates pass or approved waiver exists with owner, expiry, risk acceptance, and remediation. |
| Dynamic Workspace release | Verify template approval, API contract, policy filtering, accessibility tests, frontend telemetry, rollback/deactivation, and user evidence. | Workspace behavior is backend-governed, policy-filtered, observable, reversible, and tested. |
| MicroFunction transaction | Trace transaction from intake/API/UI/event through standard steps, policy, idempotency, audit, outbox, observability, tests, rollback. | Execution evidence proves no controller/domain/database/provider boundary bypass. |
| API/event contract | Verify OpenAPI/AsyncAPI, Avro/CloudEvents, schema compatibility, idempotency, DLQ/replay, safe errors, consumer tests. | Contract and event changes are versioned, compatible, tested, and traceable to release evidence. |
| Flyway/database | Sample migrations; verify Flyway checksum, review, no manual DDL, rollback/forward-fix plan, RLS/data classification, restore/reconciliation. | Database authority remains PostgreSQL/Flyway; changes are reversible or compensable. |
| Access/SBAC/OPA | Sample privileged roles/actions; verify role/skill scope, OPA decision, SoD, approval, periodic access review, denial evidence. | Least privilege and separation of duties operate; denied access fails safe. |
| Observability/toggles | Sample runtime change or incident; verify Log4j2/OTel/Sentry/Loki/Tempo/Grafana signals, forbidden fields, toggle approval, audit, expiry. | Telemetry supports trace reconstruction without leaking secrets/PII and toggle changes are governed. |
| Incident/Auto-Heal | Sample incident or Auto-Heal proposal; verify Zammad record, evidence retrieval, RCA, candidate fix, tests, human approval, rollback, closure. | Auto-Heal remains policy-gated, evidence-backed, human-accountable, and non-silent. |
| AI agent/tool action | Sample agent action; verify registry, SBAC, OPA, model route, guardrails, Harness action, approval, run_id, trace_id, evidence_ref, kill switch. | Agent action does not exceed trust tier, tools, data class, or environment scope. |
| BCDR/restore | Sample backup/restore/DR exercise; verify RTO/RPO, immutable backup, restore validation, evidence, owner sign-off, lessons learned. | Recovery capability is tested, documented, and linked to business/service criticality. |

# 7. Continuous Compliance Dashboards and Metrics
| Metric / Indicator | Purpose | Escalation Trigger |
| --- | --- | --- |
| Evidence completeness rate | Shows whether PR/MR, release, incident, control, and AI evidence packs are complete. | Below target or missing critical evidence. |
| Failed or waived gate count | Shows systemic weakness in CI/CD, security, architecture, or release controls. | Repeated waivers, expired waivers, or Critical/High gate bypass. |
| Overdue CAPA / findings aging | Shows remediation discipline and control-owner accountability. | Critical/High overdue; repeated extensions without risk owner approval. |
| Access review exceptions | Shows least privilege/SBAC/SoD drift. | Privileged stale access, orphaned user/agent, or SoD conflict. |
| Telemetry forbidden-field violations | Shows evidence leakage risk. | Any secret/token/raw PII/restricted prompt in logs, traces, metrics, screenshots, or tickets. |
| Incident recurrence and MTTR | Shows operational control effectiveness. | Recurring Sev-1/Sev-2, missed SLO, failed runbook, or unresolved problem record. |
| AI governance exceptions | Shows prompt/model/agent/tool safety posture. | Unregistered agent, direct model call, guardrail failure, unauthorized tool action, or missing approval. |
| BCDR test result | Shows recoverability and continuity evidence. | Failed restore, untested critical service, exceeded RTO/RPO, or missing backup integrity proof. |

# 8. Findings, Exceptions, Waivers, and CAPA Workflow
| Severity | Definition | Required Treatment |
| --- | --- | --- |
| Critical | Control failure creates production, security, Restricted data, legal/regulatory, financial, irreversible, or uncontrolled AI/autonomy risk. | Immediate containment; executive/security/CAB notification; block release or disable capability until approved exception. |
| High | Material evidence/control gap may allow unauthorized access, unsafe release, audit failure, or unreliable recovery. | Owner-assigned CAPA, due date, compensating control, retest, and management tracking. |
| Medium | Control design or operation weakness with bounded impact and available workaround. | Scheduled remediation, evidence improvement, training/update, and retest. |
| Low | Documentation, consistency, or minor evidence gap without immediate material risk. | Backlog item or next-cycle improvement with owner. |
| Observation | Opportunity to improve clarity, automation, sampling, reporting, or usability. | Route to improvement backlog or standard revision candidate. |
| ## Control Finding / CAPA Record - Finding ID / date / source: - Control ID and domain: - Severity and risk statement: - Evidence sampled: - Failed requirement or missing evidence: - Root cause and impacted services/processes: - Immediate containment or compensating control: - Corrective and preventive action owner: - Target date and waiver/exception expiry: - Retest plan and closure evidence: - Improvement backlog / ADR / TDL / runbook link: |
| --- |

# 9. AI-Native Control Testing Requirements
| AI Control | Audit Test | Pass Criteria |
| --- | --- | --- |
| Model routing | Verify no direct provider calls; all model traffic uses approved LiteLLM/private gateway aliases and classification rules. | Route logs and code scan show approved gateway only. |
| Prompt and guardrails | Sample prompts/templates; verify input, retrieval, execution, and output guardrail checkpoints plus classification handling. | Guardrail evidence exists and blocks unsafe inputs/outputs. |
| Agent registry | Sample agents; verify owner, purpose, classification ceiling, skills, tools, trust tier, certification, recertification, suspension/retirement path. | No active shadow/orphaned/uncertified agent. |
| Tool/Harness execution | Sample tool actions; verify SBAC, OPA, dry-run where required, approval, idempotency, rollback, and evidence. | Agents request; Harness executes; humans approve protected actions. |
| Memory/RAG integrity | Verify source authority, freshness, provenance, retrieval eligibility, quarantine, redaction, and context traceability. | AI output cites eligible sources and does not use stale/conflicted/restricted context incorrectly. |
| Auto-Heal/Auto-Learn/Auto-Improve | Sample candidate loops; verify issue detection, evidence retrieval, proposal, tests, human approval, PR/MR, rollback, and no silent production mutation. | Improvement remains proposal-driven and reviewable. |

# 10. RACI, Roadmap, and Acceptance Criteria
| Activity | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Control universe maintenance | Compliance / Internal Audit | IT Head / Control Owner Council | Security, DevSecOps, SRE, Data, AI Governance | CAB/ARB |
| Evidence pack production | DevSecOps / System Owners | Control Owner | QA/SDET, SRE, Security | Internal Audit |
| Control testing | Internal Audit / Compliance | Chief Audit/Compliance Owner or delegate | Control Owners, SMEs | Management |
| Findings and CAPA | Assigned Control Owner | Domain Executive / IT Head | Security, DevSecOps, SRE, Product Owner | Internal Audit / CAB |
| Continuous dashboards | SRE / DevSecOps / Compliance | Control Owner Council | Security, Data, AI Governance | Management |
| AI control assurance | AI Governance / Security | AI Governance Owner | DevSecOps, Internal Audit, Platform | CAB/ARB |
| Phase | Required Outcome |
| --- | --- |
| Phase 0 - Baseline alignment | Update control universe, evidence sources, sampling model, dashboard ownership, and companion-document references. |
| Phase 1 - Evidence model | Implement evidence request templates, evidence manifest, chain-of-custody fields, and OpenKM/Tier-0 evidence paths. |
| Phase 2 - Control testing pilots | Pilot tests for CI/CD, Dynamic Workspace, MicroFunction, API/eventing, access/SBAC, observability, incident, BCDR, and AI governance. |
| Phase 3 - Continuous assurance | Publish dashboards for evidence completeness, failed gates, waiver aging, CAPA, access exceptions, incidents, AI controls, and BCDR readiness. |
| Phase 4 - Operationalization | Quarterly control testing, remediation review, audit committee/management reporting, and standard improvement cycle. |
| Acceptance Criterion | Required Proof |
| --- | --- |
| Control universe exists and is current | Each control has owner, risk, frequency, evidence source, classification, retention, and test method. |
| Evidence is system-produced | Evidence samples originate from Git/CI/CD/runtime/ticket/workflow/registry systems and link to source records. |
| Critical domains are testable | CI/CD, Dynamic Workspace, MicroFunction, API/eventing, database/Flyway, security/SBAC, observability, incident, BCDR, AI governance, UAT, and release controls have test procedures. |
| Findings are governed | Every finding has severity, owner, due date, CAPA, retest plan, waiver/exception status, and closure evidence. |
| Dashboards support oversight | Management can see evidence gaps, failed gates, overdue CAPA, waiver aging, access exceptions, incident recurrence, and AI governance exceptions. |
| AVCI is satisfied | Every control, test, evidence item, finding, waiver, CAPA, and improvement path is attributable, verifiable, classifiable, and improvable. |

# 11. AVCI Compliance Summary
| AVCI Property | Compliance Statement |
| --- | --- |
| Attributable | Controls, evidence, tests, findings, waivers, remediations, dashboards, and reports identify owner, source, system of record, approver, tester, reviewer, and timestamp. |
| Verifiable | Control design and operating effectiveness are proven through sampled evidence, CI/CD runs, runtime traces, audit logs, tickets, policy decisions, registry records, dashboards, and retest evidence. |
| Classifiable | Evidence, screenshots, logs, traces, prompts, tickets, findings, and audit reports carry classification, access, retention, redaction, and disposal rules. |
| Improvable | Failed controls, recurring issues, evidence gaps, waiver patterns, incidents, UAT defects, support trends, and AI evaluation results feed CAPA, backlog, runbook updates, standards updates, and Auto-Learn/Auto-Improve candidates. |

# Appendix A. Evidence Request and Control Test Templates
| ## Evidence Request Template - Request ID / control ID: - Evidence period and sample population: - Evidence owner and system of record: - Required records: PR/MR, CI run, SBOM, scan, policy decision, trace, ticket, approval, registry, backup, workflow, or dashboard - Classification and handling rule: - Retention / legal hold / disposal rule: - Due date and reviewer: - Submitted evidence links and hashes: ## Control Test Plan Template - Control objective and risk: - Design effectiveness criteria: - Operating effectiveness criteria: - Sample method and sample size: - Evidence sources: - Test steps: - Exceptions and finding severity rules: - CAPA and retest requirement: - Final conclusion: |
| --- |

# Appendix B. External Reference Baseline
| Reference | Use in This Playbook |
| --- | --- |
| NIST SP 800-218 SSDF | Secure development and software supply-chain evidence expectations for CI/CD, release, remediation, and vulnerability management. |
| OWASP ASVS 5.0.0 | Application/API security verification evidence for secure design, authentication, access control, input validation, logging, and configuration. |
| OpenTelemetry Semantic Conventions | Common telemetry attributes and naming to make audit evidence, traces, logs, metrics, and dashboards reconstructable across services. |
| SLSA v1.2 | Provenance, build integrity, and supply-chain control expectations for release evidence and artifact trust. |

