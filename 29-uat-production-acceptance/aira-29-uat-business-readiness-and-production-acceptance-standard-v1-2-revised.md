---
title: "UAT Business Readiness and Production Acceptance Standard"
doc_id: "AIRA-29"
version: "v1.2"
status: "revised"
category: "UAT and production acceptance"
source_docx: "AIRA_29_UAT_Business_Readiness_and_Production_Acceptance_Standard_v1.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 29-uat-production-acceptance
  - revised
  - aira-29
---



# UAT Business Readiness and Production Acceptance Standard



AIRA

AI-Native Enterprise Platform

UAT, Business Readiness, and Production Acceptance Standard

v1.2 Revised

UAT Evidence - Business Sign-Off - Production Readiness - Release Acceptance - Hypercare - AVCI Evidence
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-029 |
| Canonical Filename | AIRA_29_UAT_Business_Readiness_and_Production_Acceptance_Standard_v1.2_Revised.docx |
| Version | v1.2 - Revised UAT, business readiness, production acceptance, Dynamic Workspace, MicroFunction, DevSecOps, evidence, security, observability, resilience, AI governance, release/CAB, and hypercare alignment update |
| Supersedes | 29-AIRA_UAT_Business_Readiness_and_Production_Acceptance_Standard_v1.1_Aligned.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Architecture Review Board, CAB, Business Owners, Product Owners, QA/SDET, DevSecOps, Security, SRE/Operations, DBA, AI Governance, Data Governance, Service Desk, Compliance, and Internal Audit Review |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Product Owner; Business Process Owners; UAT Lead; QA/SDET Lead; DevSecOps Lead; Security Architecture; DBA; SRE / Operations; Service Desk / Zammad Owner; Data Governance; AI Governance; Compliance; Internal Audit |
| Primary Companion | 30 Release, Deployment, Change, and CAB Governance Standard v1.4; 30A Change Promotion Reversibility and Compensation v1.2; 31/31A Operations and Observability v1.2; 24B Incident/Auto-Heal v1.2; 35 BCDR v1.2; 36 Business User Training and Adoption |
| Revised Inputs Considered | 09 v3.2 Greenfield Environment; 19B v1.2 Sprint 0; 20 v1.2 CI/CD; 24B v1.2 Incident/Auto-Heal; 30 v1.4 Release/CAB; 30A v1.2 Change/Promotion; 31/31A v1.2 Operations/Observability; 35 v1.2 BCDR; 39A/39B/39C workstation and System Builder Lite; 45 v1.2 PoC2 System Factory |
| Governing AIRA Sources | 01/01A AVCI and Enterprise Design Principles; 02 Blueprint; 03 Developer Guide; 04 Technology Stack; 10 MicroFunction family; 12A and 41/46-61 Dynamic Workspace; 15/15A API; 16/16A/16B Database/Flyway; 17/17A Security; 19 GitNexus; 22A AI registry; 25A MVP Acceptance; 26A Classification; 32 SBAC; 34 Audit; 42 AI governance; 43 Continuous Improvement |
| External Alignment Reference | NIST SP 800-218 SSDF; OWASP ASVS 5.0.0; OpenTelemetry Semantic Conventions; SLSA v1.2 |
| Review Cadence | At every release gate; after major UAT finding, Sev-1/Sev-2 defect, security finding, data migration issue, production-readiness exception, CAB waiver, business-process change, AI capability change, or material technology update |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / UAT-Production-Acceptance / v1.2 / |
| Mandatory Practice Statement No AIRA release, MVP increment, module, workflow, MicroFunction, Dynamic Workspace capability, AI capability, data migration, integration, policy change, model route, agent, or production change may be accepted by the business or promoted toward production unless UAT readiness, business readiness, production acceptance, security/classification evidence, rollback or rework path, operational support, hypercare, and AVCI traceability have been proven and signed by named accountable owners. |
| --- |

# 1. Executive Summary

This v1.2 revision updates AIRA-DOC-029 as the governed bridge between engineering completion and business/production acceptance. UAT is not a screen-clicking exercise and production acceptance is not a simple go-live checklist. In AIRA, acceptance must prove that business outcomes, role permissions, workflow behavior, MicroFunction execution, Dynamic Workspace rendering, API/event contracts, database changes, observability, security, resilience, support readiness, and rollback/hypercare paths are complete, secure, observable, reversible, and evidence-producing.
| v1.2 Upgrade Area | Acceptance Meaning |
| --- | --- |
| Business readiness as a control | Training, access validation, support handoff, process-owner sign-off, and hypercare become mandatory production-readiness evidence, not optional adoption activities. |
| Dynamic Workspace acceptance | Screens, templates, widgets, AI panels, approval inboxes, dashboards, and personalized layouts must be policy-filtered, accessible, observable, and backed by approved contracts and MicroFunctions. |
| MicroFunction and backend acceptance | Business UAT scenarios must validate the transaction assembly, step evidence, idempotency, audit, outbox, policy decisions, safe errors, and rollback or compensation path. |
| Contract and event acceptance | OpenAPI, AsyncAPI, Kafka, Avro, CloudEvents, outbox/inbox, schema evolution, idempotent consumers, DLQ, and replay behavior must be proven where release scope crosses boundaries. |
| Evidence-driven go/no-go | No production acceptance without CI/CD evidence, GitNexus impact, security scans, observability proof, defect status, residual-risk acceptance, and CAB/ARB route where required. |
| AI-native acceptance | AI outputs, agents, prompt/guardrail/model-route changes, and System Builder outputs are accepted only when advisory boundaries, guardrails, OPA/SBAC, evaluation evidence, human approval, and rollback/deactivation are proven. |

# 2. Purpose, Scope, and Authority
| Dimension | v1.2 Requirement |
| --- | --- |
| Purpose | Define the controlled UAT, business readiness, production acceptance, go/no-go, hypercare, and evidence model for AIRA releases and production-bound changes. |
| In scope | Features, modules, workflows, Dynamic Workspace artifacts, MicroFunctions, APIs, events, database changes, policy changes, AI capabilities, agents, data migration, operational readiness, support transition, and release acceptance evidence. |
| Out of scope | Bypassing QA, replacing CAB/ARB, informal business sign-off, production mutation without evidence, AI approval of its own output, or accepting untested work because it appears to function in the UI. |
| Authority | Business owners approve business outcome readiness; QA/UAT lead owns execution evidence; DevSecOps owns build/release evidence; Security owns security/classification readiness; SRE/Service Desk owns operational readiness; CAB/ARB governs production-impacting acceptance. |
| Conflict rule | If documents conflict, apply the stricter AIRA control, log the issue as an AVCI reconciliation item, assign an owner, and resolve through controlled change. |

# 3. End-to-End Acceptance Operating Model
| Stage | Required Outcome | Blocking Condition |
| --- | --- | --- |
| QA exit | All required functional, unit, component, contract, security, policy, architecture, performance, accessibility, and regression tests completed. | Critical/high unapproved defect, missing test evidence, failed policy/security scan, unresolved architecture drift, or missing rollback/rework path. |
| UAT readiness | Business scenarios, UAT users, data, environment, access, support route, evidence capture, and defect workflow ready. | No owner, unstable environment, missing UAT data approval, missing access, no Zammad route, no trace/audit evidence path. |
| UAT execution | Business users validate complete scenarios with evidence, not informal observation. | Scenario not mapped to acceptance criteria, missing evidence, unclassified screenshots/data, or defect severity not triaged. |
| Business readiness | Process, training, access, communication, support, hypercare, and department sign-off complete. | Users untrained, access not validated, support route missing, process impact unresolved, or adoption risk unaccepted. |
| Production acceptance | CAB/ARB receives complete release candidate evidence pack, go/no-go decision, rollback plan, monitoring plan, residual risk, and sign-offs. | Missing evidence pack, open critical/high defect without approved risk acceptance, untested rollback, incomplete monitoring, or missing accountable sign-off. |
| Hypercare and closure | Go-live support, incident triage, adoption metrics, ticket trend, defect closure, knowledge updates, and lessons learned complete. | No hypercare owner, unresolved production acceptance condition, weak issue trend, or missing improvement backlog. |

# 4. UAT Readiness Gate
| Gate ID | Readiness Requirement | Minimum Evidence | Owner | Failure Action |
| --- | --- | --- | --- | --- |
| UAT-R01 | Approved UAT scope and scenario list | Scope record mapped to epics/stories/contracts/MicroFunctions/workflows | Product Owner | Hold UAT |
| UAT-R02 | Business owners, SMEs, and approvers assigned | Participant roster, role, availability, sign-off authority | Business Process Owner | Hold UAT |
| UAT-R03 | Controlled UAT environment and release candidate stable | Deployment version, environment readiness, smoke test, observability links | DevSecOps / SRE | Hold UAT |
| UAT-R04 | UAT data approved and classified | Synthetic/masked data register, retention/disposal, access controls | Data Governance / Security | Hold or restrict scenarios |
| UAT-R05 | QA exit and Must criteria passed | QA report, defect status, CI/CD evidence pack, GitNexus impact | QA Lead | Return to build/QA |
| UAT-R06 | No open Sev-1/Sev-2 defects | Defect register, risk/waiver record if conditional | QA Lead / Product Owner | Block UAT or block acceptance |
| UAT-R07 | Security and access ready | RBAC/ABAC/SBAC, OPA policy, identity/session, SoD, negative tests | Security Administrator | Hold affected scenarios |
| UAT-R08 | Evidence capture ready | Trace/audit/log/evidence path, screenshot policy, Zammad category | DevSecOps / QA | Hold UAT |
| UAT-R09 | Support and hypercare prepared | Zammad queues/categories, escalation contacts, runbook links, Service Desk briefing | Service Owner | Conditional or hold |
| UAT-R10 | Rollback, rework, or compensation path documented | Feature flag, rollback, forward-fix, compensation, replay, restore, or deactivation plan | DevSecOps / Tech Lead | Block production acceptance |

# 5. UAT Scenario Design and Evidence Coverage
| Scenario Group | Required Coverage | Acceptance Evidence |
| --- | --- | --- |
| Happy path | Standard business process with correct user, role, data, workflow, API/event behavior, and expected result. | Scenario result, screenshot if allowed, trace_id, audit_id, workflow_id, user sign-off. |
| Negative and policy-denied path | Invalid input, unauthorized user, missing SBAC skill, policy denial, expired session, duplicate submission, safe error response. | OPA decision, safe response proof, no sensitive leakage, audit evidence, defect or pass record. |
| Dynamic Workspace path | Workspace resolution, policy-filtered widgets, layout persistence, template/version change, AI panel safe state, accessibility/responsive behavior. | Visual/a11y result, workspace_code, component_instance_id, policy_ref, evidence_ref. |
| MicroFunction path | Transaction assembly, standard steps, business step, idempotency, audit, outbox, safe failure, compensation or rework. | transaction_code, step evidence, idempotency key, audit/outbox record, trace. |
| API / contract path | REST command/query, OpenAPI response, error semantics, generated client, authorization scope, idempotency key. | Contract test, request/response evidence, Problem Details response, client build evidence. |
| Event / integration path | AsyncAPI, Kafka topic, Avro schema, CloudEvents envelope, outbox/inbox, consumer idempotency, DLQ/retry/replay. | Schema compatibility, event ID, correlation/causation ID, consumer proof, replay/DLQ evidence. |
| Database / data path | Flyway migration, RLS/grants, reference data, data correction, retention, reporting, reconciliation. | Flyway evidence, checksum, DBA sign-off, data classification, reconciliation report. |
| Security / abuse path | Authenticated DAST, secrets hygiene, access bypass attempt, prompt injection, model-route restriction, classification handling. | DAST report, scan results, guardrail result, redaction proof, policy test, remediation evidence. |
| Performance / resilience path | Heavy transaction, concurrency, retry, timeout, rate limit, circuit breaker, queue delay, replay, rollback/restore. | Load/failure test result, SLO/SLI evidence, trace, DLQ/replay, resilience lab evidence. |
| AI-assisted path | AI advisory summary, citations, guardrails, model alias, prompt eligibility, human review, confidence/risk, no autonomous approval. | Prompt/model route audit, guardrail result, evaluation evidence, human decision record, rollback/deactivation path. |
| UAT Data Rule Use synthetic data by default. Masked or approved UAT data may be used only when synthetic data cannot validate the business scenario. Raw production PII, secrets, credentials, privileged logs, raw documents, unrestricted customer payloads, and Restricted data require formal approval, classification handling, retention/disposal, and access-control evidence. |
| --- |

# 6. UAT Execution and Defect Governance
| Execution Rule | Required Treatment |
| --- | --- |
| Scenario ownership | Every scenario has a business owner, tester, role/skill, data set, acceptance criterion, expected evidence, and sign-off authority. |
| Evidence capture | Each result records scenario ID, release candidate, environment, user role, timestamp, trace_id/evidence_ref, observed result, expected result, defect link, and signer. |
| Defect severity | Sev-1/critical and Sev-2/high block production acceptance unless the correct authority documents risk acceptance, compensating control, expiry, and remediation ticket. |
| Security defects | Fail-open behavior, policy bypass, data leakage, secret exposure, privilege escalation, missing audit, or unsafe AI behavior block acceptance. |
| Data defects | Material data integrity, migration, reconciliation, retention, RLS, or reporting defects require Data Governance/DBA review before acceptance. |
| Rework and retest | All fixes must pass QA regression, affected UAT scenario retest, CI/CD gates, security checks where applicable, and evidence update. |
| Conditional acceptance | Conditional go-live requires named owner, residual risk, expiry date, monitoring, rollback/compensation plan, and CAB/ARB acknowledgement if production-impacting. |

# 7. Business Readiness Gate
| Readiness Domain | Minimum Acceptance Requirement |
| --- | --- |
| Process readiness | Business process owners confirm updated workflow, approvals, exception handling, SLAs, controls, and support path. |
| Role/access readiness | Users, approvers, processors, reviewers, administrators, and support roles are mapped to RBAC/ABAC/SBAC and tested before go-live. |
| Training readiness | Required users complete role-based training, job aids, quick references, AI-safe guidance, and assessments where required. |
| Communication readiness | Change impact, go-live date, downtime, support route, known limitations, hypercare contacts, and escalation rules are communicated. |
| Support readiness | Zammad queues/categories, service desk scripts, runbooks, known errors, monitoring links, and escalation contacts are ready. |
| Operational readiness | SLO/SLI, dashboards, alerts, runbooks, backup/restore interface, incident workflow, and hypercare schedule are validated. |
| Business sign-off | Department/process owner signs readiness with known limitations, residual risks, support assumptions, and post-go-live monitoring plan. |

# 8. Production Acceptance Gate and Go/No-Go Decision
| Gate | Go Criteria | No-Go / Conditional Trigger |
| --- | --- | --- |
| Functional acceptance | All Must scenarios pass and Should scenarios are accepted or deferred with owner. | Must scenario failed; unaccepted process gap; business owner does not sign. |
| Security/classification | Access, OPA/SBAC, secrets, DAST/SAST/SCA, model-route, classification, and redaction controls pass. | Critical/high security issue, fail-open path, unapproved data handling, or unresolved abuse case. |
| Technical readiness | CI/CD, GitNexus, tests, SBOM/provenance, Flyway, contracts, eventing, observability, and runtime toggles pass. | Missing evidence pack, weak rollback/replay/restore, schema drift, contract break, or unstable telemetry. |
| Operational readiness | Service catalog, support model, Zammad workflow, runbooks, SLOs, dashboards, incident response, and hypercare ready. | No owner, unsupported service, missing dashboard/runbook, no escalation path, or failed DR/restore dependency. |
| Release/CAB readiness | Change record, deployment plan, rollback/compensation, release notes, residual risk, monitoring window, CAB/ARB approval complete. | CAB missing, open blocking risk, untested rollback, incomplete release evidence, or SoD violation. |
| AI governance readiness | Prompt/guardrail/model-route/agent changes evaluated, classified, auditable, deactivatable, and human-accountable. | Direct provider call, agent approval of own output, missing guardrail, failed evaluation, or weak deactivation path. |
| ## Production Acceptance Evidence Block - Release candidate / version / environment: - UAT scope and passed scenario count: - Open defects by severity and accepted residual risks: - Business owner sign-off: - QA/UAT lead sign-off: - Security and data governance sign-off: - DevSecOps/CI/CD evidence pack path: - GitNexus impact evidence: - Observability dashboard / trace evidence: - Rollback / compensation / replay / restore proof: - CAB/ARB approval reference: - Hypercare owner, period, and closure criteria: |
| --- |

# 9. Hypercare, Production Monitoring, and Acceptance Closure
| Hypercare Control | Required Treatment |
| --- | --- |
| Hypercare window | Defined by release risk, user population, business criticality, and residual risk; starts at go-live and ends only after formal closure criteria pass. |
| Daily triage | IT, business owner, QA/UAT, Service Desk, SRE, Security, and Product Owner review critical issues, defects, adoption friction, and monitoring signals. |
| Ticket categories | How-to, access/role, defect, data, performance, training gap, enhancement, security concern, AI-output issue, and operational incident categories are routed in Zammad. |
| Monitoring | Dashboards track errors, latency, SLOs, policy denials, queue lag, DLQ, replay, audit gaps, login/session issues, AI guardrail denials, and adoption metrics. |
| Closure | Hypercare exits after ticket trend review, unresolved critical issue review, adoption metric review, residual risk review, knowledge updates, and business owner acceptance. |
| Improvement feed | Lessons learned create backlog, runbook, knowledge, training, test, observability, resilience, policy, or architecture improvements with owners. |

# 10. Auto-Heal, Auto-Learn, and Auto-Improve Acceptance Interface
| Loop | Accepted Input From UAT / Go-Live | Required Governance |
| --- | --- | --- |
| Auto-Heal | Incident, SLO breach, failed smoke test, repeated defect, deployment issue, data inconsistency, policy denial spike, DLQ growth, or runtime error. | May propose containment, rollback, compensation, replay, runbook step, or remediation PR. Human approval and evidence required unless pre-approved low-risk reversible action. |
| Auto-Learn | Recurring UAT confusion, support ticket trend, stale knowledge, weak prompt answer, missing job aid, ambiguous process, evidence mismatch. | May draft knowledge/training/runbook/prompt improvements. Human review, source citation, classification check, and publication approval required. |
| Auto-Improve | Defect pattern, test gap, architecture drift, accessibility issue, resilience weakness, performance bottleneck, security hardening need. | May create improvement proposal, tests, design change, or PR. CI/CD, GitNexus, policy, security, CAB/ARB, and rollback gates apply. |
| No Silent Acceptance Rule AIRA must never allow AI, System Builder, Auto-Heal, Auto-Learn, Auto-Improve, or an agent to approve its own output, close UAT, waive defects, promote to production, alter acceptance criteria, or bypass CAB/ARB, OPA/SBAC, evidence, security, or human sign-off controls. |
| --- |

# 11. RACI and Operating Responsibilities
| Role | UAT / Readiness / Acceptance Responsibilities |
| --- | --- |
| Product Owner | Owns release scope, acceptance criteria, scenario priority, backlog decisions, and business go/no-go recommendation. |
| Business Process Owner | Owns process readiness, SME participation, department sign-off, role validation, known limitations, and adoption accountability. |
| UAT Lead / QA Lead | Owns UAT plan, scenario execution, defect severity, evidence capture, retest, exit report, and acceptance package quality. |
| DevSecOps Lead | Owns CI/CD, deployment evidence, GitNexus impact, SBOM/provenance, scan evidence, environment readiness, and release candidate traceability. |
| Security / Data Governance | Owns OPA/SBAC, access, classification, DAST/security findings, secrets hygiene, UAT data approval, redaction, and residual security risk. |
| DBA / Data Engineering | Owns Flyway, schema/data readiness, migration/reconciliation, RLS/grants, backup/restore dependency, and data evidence. |
| SRE / Operations / Service Desk | Owns service readiness, observability, Zammad workflows, runbooks, incident/hypercare process, dashboards, support model, and closure criteria. |
| CAB / ARB | Owns approval for production-impacting change, architecture/control risk, exception, waiver, rollback/compensation, and final go/no-go routing. |
| Internal Audit / Compliance | Reviews evidence completeness, control traceability, classification handling, waiver discipline, and acceptance defensibility. |

# 12. Acceptance Criteria and Definition of Done
| Area | Definition of Done |
| --- | --- |
| UAT readiness | All UAT readiness gates UAT-R01 through UAT-R10 are passed or formally waived with owner, expiry, and compensating control. |
| Scenario execution | Critical business, negative, security, workflow, recovery, Dynamic Workspace, MicroFunction, API/event, data, performance/resilience, and AI scenarios are executed and evidenced as applicable. |
| Defect closure | No open critical defect; no high defect without approved compensating control, owner, remediation ticket, expiry, and acceptance by the correct authority. |
| Business readiness | Training, role/access validation, communication, support path, department/process owner sign-off, and hypercare plan are complete. |
| Production acceptance | Release/CAB package includes UAT report, evidence pack, security/data sign-off, operational readiness, rollback/compensation, monitoring plan, and residual risk. |
| Observability and support | Dashboards, traces, logs, metrics, audit, evidence references, alerts, Zammad workflow, runbooks, and escalation paths are tested. |
| Reversibility | Rollback, forward-fix, feature disablement, compensation, DLQ/replay, restore, or safe deactivation path is tested or accepted with risk. |
| AVCI closure | Owner, source, intent, classification, evidence, approval, residual risk, lessons learned, and improvement path are recorded in the evidence path. |

# 13. External Reference and Control Alignment
| Reference | Use in AIRA 29 v1.2 |
| --- | --- |
| NIST SP 800-218 Secure Software Development Framework | Secure software and evidence-oriented development practices used to strengthen pre-UAT and production acceptance controls. |
| OWASP ASVS 5.0.0 | Application security verification reference for authenticated DAST, access control, secure API, session, logging, and data-protection acceptance. |
| OpenTelemetry Semantic Conventions | Telemetry consistency reference for trace, metric, log, resource, and event correlation across UAT, operations, and evidence reconstruction. |
| SLSA v1.2 | Supply-chain provenance and integrity reference for release candidate acceptance, artifact identity, build provenance, and evidence pack expectations. |
| AIRA Canonical Standards | AIRA AVCI, Enterprise Design Principles, MicroFunction, Dynamic Workspace, API, Flyway, Security, CI/CD, Operations, Change/CAB, BCDR, and AI governance standards remain controlling. |

# 14. AVCI Compliance Summary
| AVCI Property | Compliance Mechanism |
| --- | --- |
| Attributable | Every UAT scenario, defect, business sign-off, evidence record, release candidate, waiver, residual risk, go/no-go decision, and hypercare item has a named owner, source, reviewer, and approver. |
| Verifiable | Acceptance depends on tests, UAT records, CI/CD evidence, GitNexus impact, scans, policy decisions, Flyway results, dashboards, traces, logs, audit, runbook drills, rollback/replay/restore evidence, and retained sign-offs. |
| Classifiable | UAT data, screenshots, logs, prompts, traces, dashboards, AI outputs, tickets, evidence packs, and sign-offs inherit classification, redaction, retention, disposal, SBAC, and retrieval restrictions. |
| Improvable | Defects, waivers, user feedback, ticket trends, hypercare findings, incident drills, adoption metrics, AI evaluation results, and lessons learned feed controlled backlog, standards, runbooks, training, tests, and improvement loops. |
| v1.2 Acceptance Position AIRA production acceptance is not complete when the system works for one tester or one screen. It is complete only when the business can operate, support can respond, security can prove controls, operations can observe and recover, CAB can defend the decision, and AVCI evidence can reconstruct what was accepted, by whom, under which risk, and with which rollback or improvement path. |
| --- |

