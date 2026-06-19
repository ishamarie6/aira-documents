---
title: "Dynamic Workspace Certification Checklist and Evidence Template Pack"
doc_id: "AIRA-75"
version: "v1.0"
status: "final"
category: "Dynamic workspace certification"
source_docx: "AIRA_75_Dynamic_Workspace_Certification_Checklist_and_Evidence_Template_Pack_v1.0.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 75-dynamic-workspace-certification
  - final
  - aira-75
---



# Dynamic Workspace Certification Checklist and Evidence Template Pack



AIRA
AI-Native Enterprise Platform

Dynamic Workspace Certification Checklist and Evidence Template Pack

AIRA-DOC-075 | Version v1.0

Production UX | Experience Pack Certification | Evidence Templates | Policy Gates | AVCI Always
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-075 |
| Canonical Filename | AIRA_75_Dynamic_Workspace_Certification_Checklist_and_Evidence_Template_Pack_v1.0.docx |
| Version | v1.0 - Initial Dynamic Workspace Certification Checklist and Evidence Template Pack |
| Status | Draft for Architecture Review Board, CAB, Security, UX, DevSecOps, QA/SDET, Platform, AI Governance, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Dynamic Workspace Product Owner; UX Lead; DevSecOps Lead; Security Architecture; QA/SDET; Platform Engineering; AI Governance; Data Governance; SRE; Internal Audit |
| Primary Parents | AIRA-DOC-074 Dynamic Workspace Production UX and Experience Pack Certification Standard v1.0; 20 v1.3; 54/55/58/59/60/61 Dynamic Workspace standards; 63 PRR/ORR; 64 Resilience Lab; 65 Policy-as-Code; 66 Evidence Manifest; 71 Data Governance; 73 System Builder Operating Manual |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Dynamic-Workspace-Certification / 75 / v1.0 / |
| Mandatory Practice Statement
A Dynamic Workspace screen, widget, template, Experience Block, Experience Pack, or AI Assistant Panel capability is not production-certifiable merely because it renders correctly. It is certifiable only when UX, accessibility, policy filtering, backend authority, MicroFunction/API/event behavior, observability, security, resilience, rollback, evidence, and human approvals are complete, retained, and AVCI-traceable. |
| --- |

# Static Table of Contents

1. Executive Summary

2. Purpose, Scope, and Authority

3. Certification Checklist Operating Model

4. Checklist Taxonomy and Gate Severity

5. Certification Intake Template

6. Production UX and Accessibility Checklist

7. Experience Pack Runtime and Policy Checklist

8. Evidence Template Pack

9. Machine-Readable Certification Record

10. RACI, Acceptance Criteria, Anti-Patterns, and AVCI Summary

# 1. Executive Summary

This document provides the checklist and evidence-template pack that implements AIRA-DOC-074. It converts Dynamic Workspace certification from a policy statement into repeatable operational evidence: what must be checked, who owns the check, what evidence is required, how the decision is recorded, and how failures, waivers, conditional approvals, and improvement items are handled.

The pack is intended for screens, widgets, templates, Experience Blocks, Experience Packs, workspace personalization, Admin Builder outputs, AI Assistant Panel integrations, Dynamic Workspace actions, and MicroFunction-backed user experiences. It is also suitable as a PR/MR checklist, UAT checklist, PRR/ORR checklist, and Internal Audit evidence aid.

# 2. Purpose, Scope, and Authority
| Area | Required Treatment |
| --- | --- |
| Purpose | Define certification checklists and evidence templates for Dynamic Workspace production UX, Experience Packs, templates, widgets, policy-filtered actions, and AI-assisted workspace behavior. |
| In Scope | UX, accessibility, responsive behavior, role visibility, OPA/SBAC/ABAC filtering, MicroFunction/API/action bindings, AI panel behavior, telemetry, PRR/ORR, resilience, rollback, and evidence manifest linkage. |
| Out of Scope | Frontend-only business authority, ungoverned production activation, unmanaged template mutation, direct model-provider calls, policy bypass, raw Restricted evidence exposure, or ad hoc certification without retained evidence. |
| Authority | This template pack implements AIRA-DOC-074 and inherits AIRA AVCI, CI/CD evidence, Policy-as-Code, Data Governance, MicroFunction, Dynamic Workspace, AI Governance, PRR/ORR, and Resilience Lab standards. |
| Conflict Rule | When checklist guidance conflicts with another AIRA standard, apply the stricter control, log an AVCI reconciliation item, and route the decision through ARB/CAB/Security/Data Governance as applicable. |

# 3. Certification Checklist Operating Model
| Stage | Required Action | Evidence Output |
| --- | --- | --- |
| 1. Register | Record package, screen, widget, owner, version, classification, target audience, capability codes, and activation target. | Certification intake record; inventory reference; classification record. |
| 2. Validate | Run UX, accessibility, responsive, policy, contract, MicroFunction, AI, telemetry, security, resilience, and data checks. | Checklist results; test reports; OPA decisions; trace/log/audit samples. |
| 3. Review | Maker-checker review by UX, Product, Security, DevSecOps, QA/SDET, Architecture, AI Governance, and SRE as applicable. | Review record; evidence manifest; waiver or conditional approval if required. |
| 4. Certify | Assign Certified, Conditionally Certified, Rejected, Suspended, Retired, or Revoked state. | Certification record; approval references; expiry date if conditional. |
| 5. Activate | Promote through controlled release path with PRR/ORR and rollback evidence. | Activation record; version hash; runtime telemetry baseline. |
| 6. Monitor and Improve | Observe user experience, policy denials, error rates, latency, accessibility feedback, incidents, and improvement candidates. | Dashboards; incident links; improvement backlog; recertification trigger. |

# 4. Checklist Taxonomy and Gate Severity
| Checklist Domain | Minimum Required Evidence | Blocking Condition |
| --- | --- | --- |
| UX and Usability | Usability review, workflow fit, user-safe messages, error states, empty states, loading states, help text, user acceptance feedback. | Critical path cannot be completed, user is misled, or unsafe decision/action is presented. |
| Accessibility | Keyboard navigation, focus order, labels, landmarks, contrast, responsive zoom, screen-reader semantics, no keyboard trap. | Protected or common workflow is inaccessible without waiver and compensating path. |
| Responsive and Rendering | Desktop/tablet/mobile layout evidence, supported browser checks, SSR/CSR/PPR behavior if applicable, no clipping/overlap. | Layout breaks critical action, hides policy state, or exposes unsafe data. |
| Security and Policy | OPA/SBAC/ABAC decisions, role visibility, tenant filtering, classification controls, authenticated DAST where applicable. | Frontend bypass, fail-open policy, missing authorization, or sensitive data exposure. |
| MicroFunction and API | Capability code, transaction code, OpenAPI/AsyncAPI contract, idempotency, outbox/DLQ/replay where applicable. | Widget mutates state outside governed API/MicroFunction path. |
| AI Assistant Panel | Prompt template, model route, guardrail result, evidence retention, citation/source rule, human approval for high-risk actions. | Direct provider call, raw Restricted prompt exposure, missing guardrail, or AI approval of action. |
| Observability and Evidence | Trace ID, logs, metrics, audit event, Sentry/Loki/Tempo/Grafana evidence, evidence_ref and manifest. | Action cannot be reconstructed or evidence is ownerless/unclassified. |
| PRR/ORR and Resilience | Support model, runbook, rollback, safe-disable, load/concurrency/failure evidence for critical flows. | No rollback, no monitoring, no support owner, or untested critical failure path. |
| Decision | Meaning | Required Control |
| --- | --- | --- |
| Pass | Control is satisfied with retained evidence. | Evidence reference and reviewer recorded. |
| Fail | Control is not satisfied and blocks certification. | Remediation owner and retest required. |
| Waived | Control is temporarily accepted despite risk. | Approver, risk owner, expiry, compensating control, and remediation evidence required. |
| Conditional | Allowed only for limited scope/time or non-production readiness. | Conditions, expiry, monitoring, rollback, and closure path required. |
| N/A | Control does not apply. | Justification and reviewer recorded. |

# 5. Certification Intake Template
| Field | Required Value / Instruction |
| --- | --- |
| certification_id | Unique ID, for example DWCERT-YYYYMMDD-###. |
| artifact_type | Screen, widget, template, Experience Block, Experience Pack, AI Assistant Panel, admin builder output, runtime config, or workspace policy. |
| artifact_name_and_version | Human-readable name, semantic version, package hash, and repository/config path. |
| owner_and_checker | Named maker, checker, product owner, UX reviewer, security reviewer, DevSecOps reviewer, and approver where required. |
| classification | Public, Internal, Confidential, Restricted, Evidence-Sensitive, plus handling and retention rules. |
| target_roles | Roles, skills, tenants, branches, units, and SBAC scopes eligible to see or invoke the artifact. |
| capability_bindings | API operation IDs, MicroFunction transaction codes, event/topic names, policy references, and feature flags. |
| risk_tier | Low, Medium, High, Critical, or Production-Controlled based on data, action, AI, security, operational impact, and reversibility. |
| required_evidence | Checklist results, evidence manifest, test reports, OPA decisions, telemetry, security scans, PRR/ORR, Resilience Lab, approvals. |

# 6. Production UX and Accessibility Checklist
| ID | Checklist Item | Evidence Required | Decision |
| --- | --- | --- | --- |
| UX-01 | User objective is clear, bounded, and aligned with approved business workflow. | Journey map, acceptance criteria, UAT result. | Pass / Fail / Waived / N/A |
| UX-02 | Critical actions are obvious, reversible where possible, and require confirmation when high risk. | Screen capture, test case, approval flow evidence. | Pass / Fail / Waived / N/A |
| UX-03 | Loading, empty, partial failure, validation, denial, timeout, and retry states are defined. | UI state matrix and test evidence. | Pass / Fail / Waived / N/A |
| A11Y-01 | Keyboard navigation, focus order, focus visible, and no keyboard trap are proven. | Keyboard test report. | Pass / Fail / Waived / N/A |
| A11Y-02 | Form labels, names, roles, states, headings, landmarks, and status messages are accessible. | Accessibility scan and manual review. | Pass / Fail / Waived / N/A |
| A11Y-03 | Color contrast, responsive zoom, text scaling, and mobile readability are acceptable. | Screenshot set and contrast report. | Pass / Fail / Waived / N/A |
| RESP-01 | Supported viewport sizes render without clipped content, hidden controls, or layout overlap. | Responsive screenshot matrix. | Pass / Fail / Waived / N/A |
| RESP-02 | Progressive rendering strategy does not bypass backend policy or leak protected data. | Rendering strategy review and policy trace. | Pass / Fail / Waived / N/A |

# 7. Experience Pack Runtime and Policy Checklist
| ID | Checklist Item | Evidence Required | Decision |
| --- | --- | --- | --- |
| POL-01 | All visibility and action decisions are backed by OPA/SBAC/ABAC/RBAC policies. | OPA decision logs, policy version, tests. | Pass / Fail / Waived / N/A |
| POL-02 | Deny, hidden, filtered, require-approval, and safe-response states are user-safe and audited. | Policy-denial tests and audit sample. | Pass / Fail / Waived / N/A |
| MF-01 | Each state-changing action invokes a governed API/MicroFunction, not direct frontend mutation. | Capability map, API contract, transaction code evidence. | Pass / Fail / Waived / N/A |
| MF-02 | Idempotency, concurrency, outbox/inbox, DLQ/replay, audit, and compensation are handled where applicable. | Resilience and replay test reports. | Pass / Fail / Waived / N/A |
| API-01 | OpenAPI/AsyncAPI/schema artifacts are versioned, linted, and compatibility checked. | Contract validation report. | Pass / Fail / Waived / N/A |
| AI-01 | AI prompts, RAG sources, model routes, guardrails, citations, and artifact retention are certified. | AI certification record and guardrail result. | Pass / Fail / Waived / N/A |
| OBS-01 | Workspace load, render, policy filtering, widget action, AI prompt, and MicroFunction action emit trace/log/metric/audit evidence. | OTel, audit, dashboard, Sentry/Loki/Tempo/Grafana references. | Pass / Fail / Waived / N/A |
| DATA-01 | Screens, logs, prompts, screenshots, tests, and evidence do not expose secrets, tokens, raw PII, raw documents, or Restricted payloads. | Redaction test, classification review, data-governance signoff. | Pass / Fail / Waived / N/A |

# 8. Evidence Template Pack
| Template | Minimum Fields | Required Output |
| --- | --- | --- |
| T1 Certification Summary | certification_id, artifact, version, owner, risk_tier, classification, decision, expiry, approvers. | certification-summary.md and certification-record.json. |
| T2 UX/A11Y Evidence | journey, viewport matrix, keyboard test, screen-reader notes, contrast, error states, usability findings. | ux-a11y-evidence.md plus screenshots and report hashes. |
| T3 Policy Evidence | policy IDs, decision logs, test results, deny/fail-closed cases, waiver status. | policy-evidence.json and opa-test-results.json. |
| T4 Runtime Binding Evidence | capability codes, API operation IDs, MicroFunction transaction codes, event topics, idempotency/outbox references. | runtime-binding-map.md and contract reports. |
| T5 Observability Evidence | trace IDs, audit events, log queries, metric dashboard, Sentry issue, Loki/Tempo/Grafana links. | observability-evidence.md and trace-reconstruction.md. |
| T6 PRR/ORR and Resilience Evidence | support model, runbook, rollback, safe-disable, load/concurrency/failure/replay reports. | readiness-evidence.md and resilience-evidence.md. |
| T7 Approval and Waiver Evidence | maker, checker, approver, CODEOWNERS, UX, QA, Security, DevSecOps, SRE, CAB/ARB, waiver expiry. | approval-record.md and waiver-record.md. |

# 9. Machine-Readable Certification Record

{
  "certification_id": "DWCERT-YYYYMMDD-001",
  "artifact_type": "experience_pack",
  "artifact_name": "example-pack",
  "version": "1.0.0",
  "classification": "INTERNAL_CONFIDENTIAL",
  "risk_tier": "HIGH",
  "owner": "named-owner",
  "checker": "named-checker",
  "decision": "conditional_certified",
  "expiry_date": "YYYY-MM-DD",
  "capability_bindings": [
    {
      "capability_code": "CAP-EXAMPLE",
      "api_operation_id": "example.post",
      "microfunction_transaction_code": "TXN_EXAMPLE"
    }
  ],
  "gate_results": [
    {
      "gate_id": "POL-01",
      "result": "pass",
      "evidence_ref": "evidence/04-policy/opa-test-results.json",
      "reviewer": "security"
    }
  ],
  "readiness_refs": {
    "prr_orr": "evidence/13-approvals/prr-orr.md",
    "resilience": "evidence/08-events-resilience/resilience-summary.md"
  },
  "rollback_ref": "evidence/13-approvals/rollback-plan.md",
  "avci": {
    "attributable": true,
    "verifiable": true,
    "classifiable": true,
    "improvable": true
  }
}

# 10. RACI, Acceptance Criteria, Anti-Patterns, and AVCI Summary
| Role | RACI | Responsibility |
| --- | --- | --- |
| Solutions Architecture Office / IT Head | A/R | Owns this template pack, resolves conflicts, and approves material certification exceptions. |
| Dynamic Workspace Product Owner | A/R | Owns user outcome, Experience Pack readiness, acceptance criteria, and product risk. |
| UX / Accessibility Lead | A/R | Owns UX, accessibility, responsive, usability, and human-centered evidence. |
| DevSecOps Lead | A/R | Owns CI/CD evidence, evidence manifest, release gates, GitNexus, and retention. |
| Security Architecture | A/R | Owns OPA/SBAC/ABAC, abuse cases, data exposure, authenticated DAST, and waivers. |
| QA/SDET | R | Owns functional, e2e, accessibility automation, regression, and test evidence. |
| SRE / Platform Engineering | R | Owns PRR/ORR, monitoring, runtime toggles, rollback, support model, and Resilience Lab evidence. |
| Internal Audit | C/I | Reviews evidence completeness, traceability, waivers, and control effectiveness. |
| Acceptance Criterion | Pass Condition |
| --- | --- |
| Checklist complete | All applicable UX, accessibility, policy, runtime, AI, evidence, PRR/ORR, resilience, security, and approval gates are Pass, N/A with justification, or explicitly Waived/Conditional with expiry. |
| Evidence retained | Evidence references resolve to approved evidence-pack artifacts and machine-readable certification record. |
| Backend authority preserved | No frontend, widget, template, AI panel, or Experience Pack bypasses API/MicroFunction/backend policy authority. |
| Safe activation | Rollback, safe-disable, monitoring, support owner, and post-activation review are defined. |
| AVCI satisfied | Every certification decision is attributable, verifiable, classifiable, and improvable. |
| Anti-Pattern | Required Response |
| --- | --- |
| Certifying a screen because it looks good but lacks policy, audit, accessibility, or evidence. | Reject certification; complete missing gates. |
| Using frontend visibility as authorization. | Reject; enforce backend OPA/SBAC and API/MicroFunction checks. |
| Allowing AI panel actions without model-route, guardrail, classification, and human-approval rules. | Reject or downgrade to advisory only. |
| Publishing Experience Packs without rollback, safe-disable, or operational owner. | Block activation until PRR/ORR evidence is complete. |
| Waivers without expiry, owner, compensating control, and remediation plan. | Reject waiver and log non-conformance. |
| AVCI Property | How This Pack Satisfies It |
| --- | --- |
| Attributable | Requires certification ID, owner, maker, checker, approver, artifact version, source references, policy references, and evidence owner. |
| Verifiable | Requires test reports, screenshots, accessibility checks, OPA decisions, contract reports, telemetry, PRR/ORR, resilience evidence, approvals, and manifest hashes. |
| Classifiable | Requires data/artifact classification, redaction proof, retention path, model-route eligibility, and evidence handling rules. |
| Improvable | Findings, failed gates, waivers, incidents, telemetry, UX feedback, and audit results feed improvement backlog and recertification triggers. |

