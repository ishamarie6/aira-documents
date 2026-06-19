---
title: "Business User Training Adoption and Change Management Plan"
doc_id: "AIRA-36"
version: "v1.2"
status: "revised"
category: "Training adoption and change management"
source_docx: "AIRA_36_Business_User_Training_Adoption_and_Change_Management_Plan_v1.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 36-training-adoption-change-management
  - revised
  - aira-36
---



# Business User Training Adoption and Change Management Plan



AIRA

AI-Native Enterprise Platform

Business User Training, Adoption, and Change Management Plan

v1.2 Revised

Business Readiness - Role-Based Enablement - Dynamic Workspace Adoption - AI-Safe Usage - Support Transition - AVCI Evidence
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-036 |
| Canonical Filename | AIRA_36_Business_User_Training_Adoption_and_Change_Management_Plan_v1.2_Revised.docx |
| Version | v1.2 - Revised business enablement, Dynamic Workspace, MicroFunction, DevSecOps evidence, security, observability, AI-safe use, support transition, hypercare, and continuous adoption update |
| Supersedes | 36-AIRA_Business_User_Training_Adoption_and_Change_Management_Plan_v1.1_Aligned.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Business Process Owners, Product Owner, UAT Lead, Service Desk, Operations, Security, Data Governance, AI Governance, Compliance, Internal Audit, CAB, and Architecture Review Board review |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Business Process Owners; Product Owner; UAT Lead; Training Lead; Change Manager; Service Desk / Zammad Owner; QA/SDET; DevSecOps; Security Architecture; SRE / Operations; Data Governance; AI Governance; Compliance; Internal Audit |
| Primary Companion | 29 UAT, Business Readiness, and Production Acceptance v1.2; 30 Release/CAB v1.4; 31 Production Operations v1.2; 31A Observability v1.2; 24B Incident/Auto-Heal v1.2; 35 BCDR v1.2; 32 SBAC Catalog |
| Revised Inputs Considered | 09 v3.2 Greenfield Environment; 19B v1.2 Sprint 0; 20 v1.2 CI/CD Evidence; 29 v1.2 UAT; 30/30A v1.4/v1.2 Release and Reversibility; 31/31A v1.2 Operations and Observability; 35 v1.2 BCDR; 39A/39B/39C Workstation/System Builder Lite; 45 v1.2 PoC2 System Factory |
| Governing AIRA Sources | 01/01A AVCI and Enterprise Design Principles; 02 Blueprint; 03 Developer Guide; 04 Technology Stack; 10 MicroFunction family; 12A and 41/46-61 Dynamic Workspace; 15/15A API; 16/16A/16B Database/Flyway; 17/17A Security; 19 GitNexus; 20 CI/CD; 22A AI Registry; 25A MVP Acceptance; 26A Classification; 32 SBAC; 34 Audit; 42 AI Governance; 43 Continuous Improvement |
| External Alignment Reference | NIST SP 800-218 SSDF; OWASP ASVS 5.0.0; OpenTelemetry Semantic Conventions; SLSA v1.2 |
| Review Cadence | Before UAT, before pilot/go-live, after major production issue, training failure, support trend, business-process change, AI capability change, CAB waiver, security issue, or material Dynamic Workspace/MicroFunction release |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Business-Enablement / Training-Adoption-Change / v1.2 / |
| Mandatory Practice Statement No business user, department representative, approver, processor, reviewer, administrator, service desk member, power user, or business owner is considered ready for AIRA production use until role-based training, process-change awareness, access and authority validation, AI-safe usage guidance, evidence-handling responsibilities, support-channel awareness, UAT/readiness participation, and sign-off evidence have been completed or formally waived by the accountable owner. |
| --- |

# 1. Executive Summary

This v1.2 revision updates AIRA-DOC-036 from a general business enablement plan into a governed adoption and operational-readiness control. AIRA changes how business users work: they use role-filtered Dynamic Workspace screens, perform MicroFunction-backed actions, follow OPA/SBAC authority rules, provide evidence during UAT and production support, interact with AI-assisted panels under guardrails, and raise structured issues through Zammad and controlled hypercare. Training is therefore a production-readiness control, not an optional orientation activity.
| Management Intent Business adoption is a control. AIRA succeeds only when users understand the changed process, operate within classification and access rules, use approved Dynamic Workspace components correctly, submit complete evidence, avoid unsafe AI/prompt behavior, report issues through the right support path, and provide structured feedback for improvement. |
| --- |
| v1.2 Alignment Area | Required Business Enablement Outcome |
| --- | --- |
| Dynamic Workspace adoption | Users understand personalized screens, role-filtered widgets, layout behavior, notifications, accessibility, AI assistant panel limits, and safe evidence capture. |
| MicroFunction and workflow behavior | Users know that business actions are controlled transactions with audit, idempotency, approvals, exceptions, and evidence, not informal UI clicks. |
| DevSecOps and evidence awareness | Business users understand what evidence is required for UAT, defects, support tickets, sign-offs, hypercare, and post-release improvement. |
| Security, SBAC, and classification | Users are trained on least privilege, role/skill scope, SoD, secure data handling, no secrets in screenshots/prompts, and policy-denied behavior. |
| Observability and support transition | Users know how to report issues using Zammad with traceable details while avoiding sensitive data leakage. |
| AI-safe business use | AI output is advisory. Users must not treat generated summaries, suggestions, or documents as approved authority without human review and source evidence. |
| Continuous adoption improvement | Training gaps, recurring tickets, UAT defects, and hypercare trends become reviewed job aids, backlog items, runbook updates, or Auto-Learn candidates. |

# 2. Purpose, Scope, and Authority
| Area | Requirement |
| --- | --- |
| Purpose | Define the business-user training, communications, readiness, support transition, adoption measurement, and change-management evidence model for AIRA releases and modules. |
| In Scope | Business process change, role-based training, Dynamic Workspace adoption, MicroFunction/workflow user behavior, UAT participation, access validation, support transition, hypercare, AI-safe usage, adoption metrics, and sign-off evidence. |
| Out of Scope | Detailed coding standards, developer certification, HR performance management, and unmanaged informal training outside approved AIRA source and evidence controls. |
| Authority | Business Process Owners own readiness for their business process. Product Owner and UAT Lead coordinate adoption evidence. Security/Data/AI Governance own controlled usage requirements. CAB/ARB may block go-live when training gaps create operational, security, compliance, or reversibility risk. |
| Conflict Rule | When this plan conflicts with AVCI, 01A design principles, security, UAT, release/CAB, operations, Dynamic Workspace, MicroFunction, or AI governance standards, the stricter control governs and the issue is logged as an AVCI reconciliation item. |

# 3. Adoption Principles
| ID | Principle | Mandatory Meaning |
| --- | --- | --- |
| ADP-01 | Role-based enablement | Each persona receives the process context, functions, authority rules, evidence duties, and support path needed for that role only. |
| ADP-02 | Evidence before readiness | Attendance alone is insufficient. Readiness requires scenario practice, acknowledgement, access validation, or owner-approved waiver. |
| ADP-03 | Frontend is not authority | The Dynamic Workspace renders allowed actions; backend policy, MicroFunctions, workflows, and audit determine authority and execution. |
| ADP-04 | Secure and classifiable use | Users must avoid exposing secrets, credentials, raw PII, restricted data, privileged logs, or sensitive screenshots in tickets, prompts, training materials, or chat. |
| ADP-05 | Human accountability | AI-assisted summaries, recommendations, templates, and analysis require human validation before business use or approval. |
| ADP-06 | Supportable adoption | Every release has Zammad categories, known-issue handling, hypercare coverage, escalation contacts, and user feedback path. |
| ADP-07 | Continuous improvement | Training issues, confusing UI, repeated tickets, defect trends, and process friction become structured backlog or Auto-Learn/Auto-Improve candidates, not silent workarounds. |
| ADP-08 | AVCI always | Training artifacts, communications, job aids, sign-offs, support evidence, and adoption metrics remain attributable, verifiable, classifiable, and improvable. |

# 4. Stakeholder and Persona Training Model
| Persona | Primary Need | Training Emphasis | Readiness Evidence |
| --- | --- | --- | --- |
| Department Head / Process Owner | Understand process impact, accountability, metrics, escalation, and sign-off responsibility. | Operating model, changed controls, reporting, go/no-go obligations, residual risk. | Business readiness sign-off and participation in go/no-go review. |
| Business SME / Product Owner | Validate requirements, scenarios, and accepted outcomes. | UAT design, acceptance criteria, defect triage, backlog prioritization, evidence standards. | Approved scenarios, UAT participation, defect disposition record. |
| Requester / Frontline User | Submit and track transactions correctly. | Dynamic Workspace navigation, data entry, document upload, status tracking, safe support reporting. | Attendance, scenario exercise, quick-check assessment. |
| Processor / Analyst | Perform daily processing and exception handling. | Work queues, validation, evidence handling, classification, handoffs, MicroFunction outcomes. | Scenario completion, quality check, supervisor approval. |
| Approver / Checker | Make controlled approvals and exceptions. | Approval workflow, SoD, OPA/SBAC policy results, audit trail, decision evidence, rejection/rework. | Approval simulation and role-access validation. |
| Power User / Champion | Support peers and capture feedback. | Train-the-trainer, job aids, common issues, Zammad routing, improvement candidate capture. | Champion sign-off and hypercare support participation record. |
| Service Desk / Support | Receive, classify, and route user issues. | Zammad workflow, categories, SLA, trace/evidence references, safe data handling, escalation. | Support readiness checklist and test ticket execution. |
| Compliance / Internal Audit | Verify evidence and control operation. | Evidence paths, reports, access trails, change records, AI usage, support records. | Evidence sampling and audit walkthrough record. |

# 5. Change Impact Assessment Model
| Impact Area | Assessment Questions | Required Output |
| --- | --- | --- |
| Process change | What business steps are added, removed, automated, controlled, or reassigned? | Updated process map, change summary, SOP/job-aid update. |
| Role / authority change | Which roles, skills, permissions, approvals, or SoD rules change? | Role impact and access validation list mapped to SBAC/OPA. |
| Data handling change | What data is entered, viewed, uploaded, exported, classified, retained, or masked differently? | Data handling and classification note plus user obligations. |
| Control change | Which approvals, audit logs, evidence paths, exception rules, or policy denials are new? | Control explanation and decision/evidence responsibilities. |
| Dynamic Workspace change | Which screens, widgets, templates, AI panels, notifications, or accessibility/responsive behaviors change? | User journey update, job aid, affected persona list. |
| MicroFunction/workflow change | Which transactions, queues, approval paths, outbox events, replay/rework paths, or compensations affect users? | Scenario walkthrough, support script, escalation path. |
| Support change | What issues may users raise and how will support triage them? | Zammad categories, KB article, known-error note, escalation matrix. |
| Adoption risk | Which groups may resist, struggle, misuse AI, bypass process, or need coaching? | Mitigation plan, champion assignment, targeted communication. |
| High-Impact Change Rule High-impact changes require targeted training, power-user rehearsal, UAT-linked walkthrough, formal communication, support readiness, hypercare plan, and department-head acknowledgement before go-live. Changes affecting Restricted data, approvals, AI guidance, production-impacting workflows, financial/legal outputs, or irreversible decisions require elevated owner sign-off. |
| --- |

# 6. Training Architecture and Curriculum
| Training Component | Source of Truth | Minimum Content | Evidence |
| --- | --- | --- | --- |
| Release briefing | Release notes, CAB record, product roadmap | What changes, who is affected, date, known limitations, support path. | Communication log and acknowledgement where required. |
| Role-based process module | Approved process map, UAT scenarios, SOP | End-to-end user journey, roles, approvals, exceptions, rework. | Attendance, quiz/exercise, owner sign-off. |
| Dynamic Workspace module | Workspace configuration, template catalog, UX standard | Navigation, widgets, policy-hidden actions, layout behavior, accessibility, notifications. | Scenario completion and issue feedback. |
| MicroFunction/workflow module | Transaction catalog, workflow definition, job aids | What happens after submit/approve/reject, idempotency, audit, status, evidence. | Scenario evidence tied to transaction/workflow ID. |
| Security/classification module | Security standard, SBAC catalog, data classification register | Secure use, data handling, safe screenshots/tickets, no secrets or raw PII, SoD. | Acknowledgement and access-validation evidence. |
| AI-safe usage module | AI governance, prompt/guardrail registry, assistant panel guide | AI is advisory, cite sources, do not paste Restricted data/secrets, require human review. | AI-safe usage acknowledgement and sample review exercise. |
| Support and hypercare module | Zammad workflow, operations runbook, known errors | How to report issues, severity, expected evidence, escalation, workaround handling. | Test ticket and closure evidence. |
| Power-user/champion module | Trainer guide and feedback template | Peer support, coaching, capture feedback, triage common issues, escalate patterns. | Champion readiness record and hypercare roster. |

# 7. AI-Safe Business User Guidance
| Rule | User Instruction | Control Evidence |
| --- | --- | --- |
| AI is advisory | Do not treat AI output as approved policy, business decision, legal answer, or access approval. Validate sources and obtain required human approval. | Training acknowledgement; reviewer sign-off for AI-assisted outputs. |
| No sensitive prompt leakage | Do not paste passwords, tokens, secrets, raw PII, account numbers, privileged logs, Restricted documents, or raw customer files into AI prompts or tickets. | Prompt safety training; sampling; incident ticket if violated. |
| Use approved channels | Use the AIRA AI Assistant Panel or approved workspace route only; do not use personal AI accounts for AIRA work. | Access logs; model-route/guardrail evidence. |
| Cite and verify | AI-generated summaries must link to evidence, source documents, workflow IDs, or approved records before business use. | Evidence_ref and source_ref in output or decision record. |
| Human approval remains mandatory | Approvals, unlocks, exceptions, financial/legal/security decisions, production changes, and Restricted decisions remain human-controlled. | Approval workflow and SoD evidence. |
| Report unsafe behavior | Report hallucination, policy bypass, sensitive output, prompt injection, or unsafe recommendation through Zammad/security channel. | Zammad/security case and model/guardrail incident evidence. |

# 8. Business Readiness, UAT Alignment, and Sign-Off
| Gate | Requirement | Minimum Evidence | Owner |
| --- | --- | --- | --- |
| BRG-01 Process readiness | Business process owner confirms target process, SOP, roles, exceptions, and metrics. | Approved process note/SOP and change impact register. | Business Process Owner |
| BRG-02 Training readiness | Affected users trained, briefed, or formally waived by accountable owner. | Attendance, assessment, acknowledgement, waiver register. | Product Owner / Training Lead |
| BRG-03 Access readiness | Role, access, approvals, SBAC skills, and SoD rules validated. | Access test evidence and role/SBAC catalog reference. | Security / Business Owner |
| BRG-04 UAT alignment | UAT scenarios, defects, accepted limitations, and rework items reflected in training/job aids. | UAT sign-off, defect disposition, job-aid update. | UAT Lead / Product Owner |
| BRG-05 Support readiness | Service Desk prepared with categories, FAQs, known errors, escalation, and hypercare roster. | Zammad setup proof, support checklist, test ticket. | Service Desk Owner |
| BRG-06 Communication readiness | Go-live impact, timeline, support path, known limitations, and user obligations communicated. | Communication plan and distribution evidence. | Change Manager |
| BRG-07 Go-live sign-off | Business owner accepts readiness, residual risks, support assumptions, and post-go-live monitoring. | Business sign-off and CAB/acceptance reference. | Department Head / Process Owner |

# 9. Support Transition, Zammad Workflow, and Hypercare
| Support Phase | Required Treatment | Evidence |
| --- | --- | --- |
| Pre-go-live support rehearsal | Service Desk, power users, process owners, and IT support run sample tickets for access issue, defect, data issue, training issue, policy denial, and incident. | Test tickets, category validation, escalation proof. |
| Go-live support | Hypercare channel, Zammad queue, escalation roster, known-issue list, daily review cadence, and communication owner active. | Hypercare roster, daily dashboard, ticket trend report. |
| Issue capture | Every issue is classified as defect, access issue, data issue, training issue, support request, security concern, incident, or improvement candidate. | Zammad ticket with owner, severity, classification, evidence_ref. |
| Evidence-safe reporting | Users provide screenshots only when approved and redact sensitive data. Encourage trace/reference IDs instead of raw data. | Ticket sampling and redaction checks. |
| Closure and transition | Hypercare exits only when open critical/high issues are resolved/accepted, training updates are complete, and support model is stable. | Hypercare closure report and BAU handover sign-off. |

# 10. Adoption Metrics and Continuous Improvement
| Metric / Signal | Interpretation | Improvement Action |
| --- | --- | --- |
| Training completion rate | Shows readiness coverage but not proficiency alone. | Target missing users, issue waivers, or delay go-live for high-risk roles. |
| Assessment / scenario pass rate | Shows whether users can execute the process, not only attend. | Refresh job aids, add coaching, update UAT scenarios. |
| Ticket volume and category trend | High training/access/support tickets indicate adoption friction. | Create KB articles, simplify UX, improve communication, add automation candidate. |
| Policy-denied and access errors | May indicate correct security behavior or poor role mapping/training. | Review SBAC mapping, training content, and support scripts. |
| Dynamic Workspace usability feedback | Identifies confusing widgets, layout problems, missing information, accessibility issues. | Backlog UX improvement through governed Dynamic Workspace changes. |
| AI safety incidents or misuse | Indicates prompt/data-handling gaps or unclear AI authority boundaries. | Retrain users, update AI-safe guidance, adjust guardrails/model routing. |
| Recurring defects or workarounds | Indicates process or system weakness beyond training. | Create problem record, Auto-Learn/Auto-Improve candidate, backlog item, or ADR/TDL. |
| Auto-Learn and Auto-Improve Boundary Adoption analytics may propose job-aid updates, FAQ changes, workflow improvements, Dynamic Workspace changes, support scripts, or backlog items. AI must not silently change training materials, role rules, workspace templates, production behavior, prompt guidance, or policies without named owner review, classification check, approval, publication evidence, and rollback/depublication path. |
| --- |

# 11. Training and Adoption Evidence Templates
| ## Training Readiness Record - Release / module / capability: - Persona / role / SBAC scope: - Training source version and job-aid version: - Attendance / completion date: - Scenario or assessment result: - Access validation evidence: - AI-safe usage acknowledgement: - Support-channel acknowledgement: - Waiver, condition, or restriction if any: - Owner / reviewer / sign-off: - Evidence path: ## Change Communication Record - Change summary and affected personas: - Process / screen / workflow / AI / support impact: - Effective date and go-live window: - Known limitations and residual risks: - Support path and hypercare contacts: - Communication owner and approval: - Distribution evidence: |
| --- |

# 12. RACI, Roadmap, and Acceptance Criteria
| Activity | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Change impact assessment | Product Owner / Change Manager | Business Process Owner | Security, Data, Operations, AI Governance | Affected users |
| Training material preparation | Training Lead / SME | Product Owner | Architecture, Security, UAT Lead | Business users |
| Access and authority validation | Security Administrator | Business Owner | SBAC Owner, Compliance | Affected users |
| UAT-linked walkthrough | UAT Lead / SME | Product Owner | QA/SDET, DevSecOps | Process owners |
| Support transition and hypercare | Service Desk Owner | SRE / Operations Lead | Product Owner, Training Lead, Security | All users |
| Adoption metrics and improvement | Change Manager / Product Owner | Business Process Owner | SRE, Service Desk, QA, AI Governance | CAB/ARB/Internal Audit |
| Phase | Required Outcome |
| --- | --- |
| Phase 0 - Source alignment | Confirm active sources, personas, impacted processes, UAT scope, release readiness path, and evidence path. |
| Phase 1 - Impact and curriculum | Complete change impact, persona map, role curriculum, AI-safe guidance, and support training plan. |
| Phase 2 - UAT-linked enablement | Run role-based walkthroughs, scenario exercises, access validation, and support rehearsal. |
| Phase 3 - Go-live readiness | Complete sign-offs, communication, hypercare roster, Zammad setup, known issues, and go/no-go evidence. |
| Phase 4 - Hypercare and improvement | Monitor adoption, triage tickets, update job aids, create backlog/problem/Auto-Learn candidates, and close hypercare evidence. |
| Acceptance Criterion | Required Proof |
| --- | --- |
| All affected personas identified | Persona map and training needs assessment exist. |
| Training materials are source-controlled and current | Job aids cite approved source version, owner, classification, and review date. |
| Users are prepared for role-specific actions | Training completion, scenario exercise, or formal waiver exists. |
| Access and authority are verified | RBAC/ABAC/SBAC/OPA access test evidence exists for critical roles. |
| Support transition is ready | Zammad categories, known issues, escalation, support scripts, and hypercare roster are verified. |
| AI-safe usage is covered | Business users acknowledge AI boundaries, prompt/data restrictions, and human approval rules. |
| Adoption improvement loop is active | Ticket trends, feedback, UAT issues, and hypercare findings feed backlog/runbook/training updates. |
| AVCI is satisfied | Every material training, communication, sign-off, waiver, and improvement item has owner, source, classification, verification evidence, and improvement path. |

# 13. AVCI Compliance Summary
| AVCI Property | Compliance Statement |
| --- | --- |
| Attributable | Training artifacts, job aids, communications, sign-offs, waivers, support records, and adoption metrics identify owner, source, version, affected role, approver, and evidence path. |
| Verifiable | Readiness is proven through training records, scenario exercises, access validation, UAT evidence, Zammad support rehearsal, communication logs, and hypercare closure evidence. |
| Classifiable | Training and adoption artifacts inherit source classification; sensitive data, screenshots, prompts, logs, tickets, and evidence are governed by data-handling, redaction, and retention rules. |
| Improvable | User feedback, UAT defects, support ticket trends, adoption metrics, and hypercare findings feed backlog, job-aid updates, runbook updates, problem records, and governed Auto-Learn/Auto-Improve candidates. |

# Appendix A. External Reference Baseline
| Reference | Use in This Standard |
| --- | --- |
| NIST SP 800-218 SSDF | Secure development and release evidence expectations that training/adoption must not bypass. |
| OWASP ASVS 5.0.0 | Web application and API security verification expectations for user-facing training, secure usage, and defect awareness. |
| OpenTelemetry Semantic Conventions | Consistent telemetry vocabulary for evidence references, support tickets, and trace-aware issue reporting. |
| SLSA v1.2 | Supply-chain provenance and trusted build evidence that business readiness must reference during release acceptance. |

