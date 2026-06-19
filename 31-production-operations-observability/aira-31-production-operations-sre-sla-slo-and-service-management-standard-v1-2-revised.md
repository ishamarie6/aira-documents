---
title: "Production Operations SRE SLA SLO and Service Management Standard"
doc_id: "AIRA-31"
version: "v1.2"
status: "revised"
category: "Production operations and observability"
source_docx: "AIRA_31_Production_Operations_SRE_SLA_SLO_and_Service_Management_Standard_v1.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 31-production-operations-observability
  - revised
  - aira-31
---



# Production Operations SRE SLA SLO and Service Management Standard



AIRA

AI-Native Enterprise Platform

Production Operations, SRE, SLA/SLO, and Service Management Standard

v1.2 Revised

Zammad ITSM - SRE - SLO/Error Budget - Observability - SIEM/SOAR - Runbooks - DR Readiness - Dynamic Workspace - MicroFunction Runtime - AI Agent Operations - Auto-Heal/Auto-Learn/Auto-Improve
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-031 |
| Canonical Filename | AIRA_31_Production_Operations_SRE_SLA_SLO_and_Service_Management_Standard_v1.2_Revised.docx |
| Version | v1.2 - Revised Greenfield/Sprint 0/CI-CD/PoC 2/31A alignment, Dynamic Workspace and MicroFunction operations update, SRE evidence and runtime toggle hardening, resilience lab, AI agent operations, and controlled improvement loop update |
| Supersedes | 31-AIRA_Production_Operations_SRE_SLA_SLO_and_Service_Management_Standard_v1.1_Aligned.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Architecture, DevSecOps, SRE / Operations, Security, Platform Engineering, QA/SDET, DBA, AI Governance, and Internal Audit Review |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | SRE / Operations Lead; DevSecOps Lead; Service Desk Lead; Security Architecture; Platform Engineering; Software Development Lead; QA/SDET; DBA; AI Governance; Data Governance; Internal Audit |
| Primary Companion | 31A-AIRA Observability, Telemetry, and Evidence Correlation Standard v1.2 Revised |
| Revised Companion Sources | 09 v3.2 Greenfield Environment; 19B v1.2 Sprint 0; 20 v1.2 CI/CD Evidence Pack; 39A/39B/39C Workstation and System Builder Lite setup; 45 v1.2 PoC 2 DevSecOps System Factory; 31A v1.2 Observability |
| Core AIRA Sources | 01/01A AVCI and Enterprise Design Principles; 02 Engineering Blueprint; 03 Developer Guide; 04 Technology Stack; 10/10A/10B/10C/10D/10E MicroFunction; 12A and 41/46-61 Dynamic Workspace; 15/15A API; 16/16A/16B Database/Flyway; 17/17A Security; 19 GitNexus; 24B Operations/Incident/Auto-Heal; 30/30A Change/Reversibility; 42D-42S AI Agent Governance; 43 Continuous Improvement |
| Primary Tooling Baseline | Zammad for ITSM/service tickets; OpenTelemetry, Log4j2, Prometheus, Loki, Tempo, Grafana, Sentry and/or SigNoz for observability/APM; Wazuh for SIEM/XDR; TheHive/Cortex or approved equivalent for case management/SOAR-assisted response; GitHub/GitLab and CI evidence store; OpenKM/Obsidian/LLM Wiki for approved records and curated knowledge |
| External Alignment Reference | NIST SP 800-218 SSDF; NIST SP 800-218A initial public draft where applicable for AI software; OWASP ASVS 5.0.0; OpenTelemetry Semantic Conventions; SLSA v1.2 |
| Review Cadence | Monthly during MVP/early production; after every Sev-1/Sev-2, major release, control failure, incident drill, operational readiness gate, AI-agent runtime change, or material observability/security/tooling change; quarterly after stabilization |
| Evidence Path | OpenKM Tier-0 / AIRA / Operations / Production-Operations-SRE-Service-Management / v1.2 / |
| Mandatory Operating Rule No AIRA production service, platform component, AI capability, workflow, data store, integration, Dynamic Workspace feature, MicroFunction transaction, System Builder function, AI agent, operational automation, or environment capability may be considered service-ready unless it has a named owner, service criticality, SLO/SLI profile, Zammad service queue, observability coverage, security monitoring, incident and rollback runbooks, support model, DR/restore interface, evidence path, and AVCI-complete operating record. A deployment that succeeds technically is not service-ready until it can be monitored, supported, secured, recovered, explained, audited, and improved. |
| --- |

# 1. Executive Summary and v1.2 Update Verdict

AIRA operations must convert the AI-native engineering platform into a reliable, supportable, secure, observable, and continuously improvable service. This v1.2 revision updates the production operations, SRE, SLA/SLO, and service management baseline so it can govern the revised greenfield environment, team workstation rollout, Sprint 0 execution plan, CI/CD evidence pack, PoC 2 system factory, and 31A telemetry/evidence model. The document remains the operations authority for service readiness, incident management, SLOs, service catalog, runbooks, security operations, support model, and operational evidence.
| Strategic Outcome | v1.2 Required Operating Result |
| --- | --- |
| Service readiness is evidence-based | A service is not accepted by Operations until ownership, SLO/SLI, observability, Zammad queue, runbook, rollback, security monitoring, support tier, evidence path, and known-risk register are complete. |
| Operations aligns with engineering factory | Release evidence, GitNexus impact, CI/CD scans, SBOM/provenance, architecture fitness, contract tests, and post-deployment smoke evidence become part of service transition. |
| Dynamic Workspace is operations-governed | Workspace templates, components, personalization, AI assistant panel, widget actions, policy denials, and admin builder changes must be monitored, auditable, reversible, and supportable. |
| MicroFunction runtime is supportable | Every critical transaction has step-level traceability, idempotency evidence, audit/outbox status, DLQ/replay path, compensation/rollback, and owner/runbook mapping. |
| Observability is operational evidence | Log4j2, OpenTelemetry, Sentry, Loki, Tempo, Grafana, audit, dashboards, alerts, and trace reconstruction support incident response, SLOs, and improvement. |
| Auto loops remain controlled | Auto-Heal, Auto-Learn, and Auto-Improve may detect, analyze, propose, draft, and request action, but may not silently modify production, standards, policies, prompts, or runtime behavior. |
| AI agents are operational subjects | Agents, model routes, guardrails, tool actions, registry state, trust tier, and kill switches are part of production operations, not invisible developer utilities. |

# 2. Purpose, Scope, and Authority
| Scope Area | Included in v1.2 | Out of Scope / Boundary |
| --- | --- | --- |
| Production operations | DEV shared services, INT, UAT, STG, pilot, PROD, DR, maintenance and controlled sandbox environments where service readiness or operational evidence is required. | Non-AIRA enterprise helpdesk policy except where AIRA service queues and integrations are affected. |
| Service management | Zammad queues, incidents, service requests, problems, changes, runbook records, post-incident reviews, release transition, and known errors. | Detailed release approval remains governed by Document 30/30A and CAB procedures. |
| SRE and SLOs | SLI/SLO profiles, error budgets, alert rules, operational dashboards, post-deployment watch, capacity, performance, availability, and reliability review. | Business SLA negotiation outside the AIRA support model unless it influences operational controls. |
| Dynamic Workspace operations | Workspace resolver, template lifecycle, admin builder, widgets, component registry, personalization, AI panel, and policy-filtered rendering. | Frontend authority over business decisions; backend policy/MicroFunction execution remains authoritative. |
| MicroFunction operations | Transaction catalog, runtime assembly, step execution, audit/outbox, idempotency, DLQ/replay, compensation, feature flags, and runtime toggles. | Hardcoded one-off operational scripts outside approved runbooks and Harness controls. |
| AI and System Builder operations | System Builder intake, generated artifacts, agent registry, LiteLLM routes, guardrails, trust tiers, tool action requests, and evidence correlation. | Direct model-provider calls, shadow agents, direct production credentials, or AI approval of its own output. |
| Security operations | Wazuh/SIEM signals, TheHive/Cortex or equivalent case handling, SOAR-assisted response, secrets incidents, abuse cases, DAST findings, and remediation evidence. | Unapproved offensive testing, unauthorized production scanning, or bypass of security governance. |
| Authority Level | Source / Control | Operating Rule |
| --- | --- | --- |
| L0 | Regulatory, legal, executive risk, ARB/CAB/Security Governance | Mandatory risk and compliance decisions govern production operation and exceptions. |
| L1 | 01/01A AVCI and Enterprise Design Principles; 02 Engineering Blueprint; 17 Security; 30/30A Change/Reversibility | Universal rules for architecture, security, evidence, approval, rollback, and fail-safe operation. |
| L2 | This 31 Standard | Canonical operations authority for SRE, service management, SLA/SLO, incident/problem, runbook, support, readiness, and operational evidence. |
| L2 | 31A Observability Standard | Canonical telemetry/evidence implementation authority consumed by this operations standard. |
| L3 | 20 CI/CD, 45 PoC 2, 24B Runbook, 35 DR, 42 AI Governance, 43 Continuous Improvement | Detailed implementation/runbook controls that must emit operating evidence and inherit this standard. |
| L4 | Zammad tickets, CI/CD runs, dashboards, audit records, incident records, PR/MR evidence, CAB minutes | Execution-level proof and improvement input. |

# 3. Production Operations Principles
| ID | Principle | Operational Meaning |
| --- | --- | --- |
| OPS-01 | No Ticket, No Work | Operational actions must trace to Zammad ticket, incident, change, runbook execution, approved automation record, or CI/CD evidence. |
| OPS-02 | Service Ownership | Every service, API, workspace capability, MicroFunction transaction, agent, model route, topic, database schema, and dashboard has an accountable owner. |
| OPS-03 | Observe Before Accept | No service transition without logs, traces, metrics, audit, dashboards, alerts, SLO profile, and trace reconstruction evidence. |
| OPS-04 | Secure Operations | Access, secrets, break-glass, DAST, SIEM/XDR, SOAR-assisted response, and remediation evidence are part of operating readiness. |
| OPS-05 | Fail-Safe Operations | If identity, policy, guardrail, audit, evidence, observability sink, secrets service, or critical dependency is unavailable, protected actions stop or degrade safely. |
| OPS-06 | Runbook or Reject | Critical operational action requires approved runbook, entry criteria, exit criteria, rollback/compensation, and evidence output. |
| OPS-07 | SLO and Error Budget Discipline | Reliability targets, error budgets, burn alerts, and service reviews guide prioritization and release risk decisions. |
| OPS-08 | Human Accountability for High Risk | Production-impacting, Restricted, destructive, low-confidence, high-severity, or policy-exception actions require named human approval. |
| OPS-09 | Operational Reversibility | Rollback, forward-fix, compensation, replay, cache rebuild, re-indexing, restore, or safe-disable path must exist and be tested by risk. |
| OPS-10 | Continuous Improvement with Controls | RCA, recurring defects, SLO burn, security findings, and user feedback become governed backlog, knowledge, runbook, test, or architecture improvement items. |

# 4. Service Catalog, Criticality, Ownership, and Readiness Model
| Service Class | Examples | Minimum Readiness Evidence |
| --- | --- | --- |
| Platform foundation | Identity, API gateway, PostgreSQL, Kafka, Redis/Valkey, OPA, Vault/OpenBao, LiteLLM gateway, observability stack, CI/CD runners. | Owner, criticality, dependency map, SLO/SLI, dashboard, alert, runbook, backup/restore, security monitoring, patch path, evidence store. |
| AIRA backend services | MicroFunction runtime, System Builder, contract registry, evidence service, workflow service, audit/outbox service, event consumers. | OpenAPI/AsyncAPI contracts, Flyway version, test evidence, log/trace/metric coverage, idempotency and DLQ/replay runbook, rollback path. |
| Dynamic Workspace | Workspace resolver, Admin Builder, template registry, component registry, AI assistant panel, dashboards, widget actions. | Policy-filtered rendering tests, component owner, telemetry fields, audit events, accessibility baseline, safe-disable feature flag, rollback of templates. |
| AI governance services | Agent registry, tool gateway/Harness, model route registry, guardrails, RAG/memory gateway, evaluation and certification dashboards. | Agent owner, trust tier, SBAC/OPA policy, kill switch, model route evidence, guardrail telemetry, incident response runbook. |
| Data and integration | OpenKM, pgvector/retrieval indexes, ETL/import, Avro schema registry, integration adapters, outbox/inbox processors. | Schema/data owner, classification, retention, lineage, replay/restore, migration evidence, access audit, data quality checks. |
| Business functions | Login/session, approval workflows, mortgage/loan operations, document actions, case management, reporting. | Business owner, process owner, workflow owner, SLO, support queue, user-facing runbook, error policy, audit and evidence matrix. |
| Readiness Gate | Required Evidence | Reject If Missing |
| --- | --- | --- |
| SR-01 Ownership | Accountable service owner, operations owner, support group, escalation path, backup owner. | No named owner or unclear support queue. |
| SR-02 Criticality | Criticality tier, RTO/RPO, SLA/SLO/SLI profile, dependency map, impact statement. | Criticality unknown or business impact not classified. |
| SR-03 Observability | Dashboards, alerts, traces, logs, metrics, audit events, evidence refs, synthetic checks. | Cannot reconstruct request/action or policy decision. |
| SR-04 Security | Access control, secrets path, vulnerability posture, DAST/SAST/SCA evidence, SIEM signal mapping, abuse-case runbook. | Secrets exposed, policy fails open, or critical/high findings unresolved without approved waiver. |
| SR-05 Resilience | Timeout/retry/circuit breaker/bulkhead, DLQ/replay, backup/restore, rollback/compensation, restore/replay test. | No recovery path for state-changing or customer-impacting flow. |
| SR-06 Operations Handoff | Zammad queue, runbook, known-error record, training, hypercare plan, CAB/ARB release evidence. | Support team cannot operate without developer tribal knowledge. |

# 5. SLA, SLO, SLI, Error Budget, and Service Review Model
| Reliability Element | AIRA Rule | Evidence / Review |
| --- | --- | --- |
| SLA | Business-facing commitments may only be published after SLOs, monitoring, support capacity, escalation path, and service readiness are proven. | Approved SLA record, service catalog entry, escalation model, risk owner. |
| SLO | Every critical service has availability, latency, error-rate, durability, backlog, and security-response objectives appropriate to its class. | SLO profile, dashboard panels, alert rules, error budget policy. |
| SLI | SLIs must be measurable from classification-safe telemetry and use stable, bounded labels. | Metric query, data source, label policy, review cadence. |
| Error Budget | Burn rate informs release risk, freeze decisions, remediation priority, and backlog ranking. | Burn dashboard, release decision record, incident/problem links. |
| Operational Review | Monthly during MVP/early production and quarterly after stabilization, with special review after Sev-1/Sev-2 or repeated SLO burn. | Review minutes, action items, owner, due date, backlog and evidence references. |
| Synthetic Checks | Critical flows have smoke/synthetic monitoring for login, workspace load, widget action, API health, event lag, model route, guardrail, and evidence write path. | Synthetic test result, trace ID, dashboard screenshot/export, alert test evidence. |
| Example AIRA SLI | Applies To | Operational Note |
| --- | --- | --- |
| Workspace load p95 latency | Dynamic Workspace resolver, component registry, template rendering | Separate backend resolver, API gateway, and frontend render signals; no raw user identifiers in metrics. |
| MicroFunction transaction success rate | Login, approval, document action, case update, evidence write | Track by transaction_code, version, environment, and safe outcome code. |
| Kafka consumer lag and DLQ rate | Event consumers, outbox/inbox, audit and evidence pipelines | Alert on sustained lag, DLQ growth, schema errors, replay failure, or duplicate effect indicators. |
| Policy denial and fail-closed rate | OPA/SBAC, API gateway, workspace filtering, tool gateway | Denials must be visible without leaking sensitive authorization internals. |
| AI route and guardrail block rate | LiteLLM route, guardrails, System Builder, agent actions | Monitor route errors, blocked prompts, retrieval denials, tool denials, and trust-tier demotions. |
| Evidence completeness | CI/CD, runtime, incident, approval, Auto-Heal/Learn/Improve loops | Missing evidence for protected actions creates operational non-conformance. |

# 6. Zammad ITSM and Service Management Workflow
| Record Type | When Used | Required Fields / Evidence |
| --- | --- | --- |
| Service Request | Access request, environment support, dashboard request, non-incident support, workstation/tool assistance. | Requester, service, classification, approval need, due date, fulfillment evidence. |
| Incident | Service degradation, security alert, policy failure, unavailable dependency, failed release, data or evidence issue, failed Auto-Heal action. | Severity, service, owner, timeline, trace/log/metric refs, affected users/scope, mitigation, closure evidence. |
| Major Incident | Sev-1/Sev-2 business, security, production, Restricted data, identity/policy/evidence/control failure. | Incident commander, bridge record, comms owner, decision log, containment evidence, PIR/RCA requirement. |
| Problem / RCA | Recurring incident, SLO burn, unknown root cause, known error, architecture drift, high-risk defect pattern. | Root cause, contributing factors, known error, prevention recommendation, backlog item, fitness/test updates. |
| Change | Production-affecting release, config change, feature flag activation, policy change, model route change, migration, replay, rollback. | Change ticket, risk, impact, CAB/ARB/security approval, rollout/rollback plan, evidence pack. |
| Runbook Execution | Approved recovery, replay, cache rebuild, re-indexing, restore test, agent suspension, telemetry toggle change. | Runbook ID, executor, approver, parameters, start/end, result, trace/evidence refs. |
| Auto-Heal / Learn / Improve Candidate | Detected pattern or remediation/knowledge/improvement proposal. | Originating signal, evidence pack, candidate, risk, tests, approval path, closure state. |
| No Side-Channel Operations Operational work must not be hidden in chat, direct database sessions, local scripts, personal AI accounts, untracked screenshots, informal calls, or one-off commands. Conversations may coordinate work, but the authoritative record must be in Zammad, PR/MR, CI evidence, runbook execution record, audit record, or approved evidence repository. |
| --- |

# 7. Incident, Major Incident, Problem, and RCA Control
| Severity | Examples | Mandatory Response |
| --- | --- | --- |
| SEV-1 Critical | Identity/policy/audit fails open; production outage of critical path; Restricted data exposure; irreversible data corruption; agent/tool unauthorized production action; broad evidence loss. | Immediate incident bridge, Incident Commander assigned, containment first, Security/ARB/CAB as applicable, evidence preservation, executive/risk notification assessment, PIR/RCA mandatory. |
| SEV-2 High | Material degradation; repeated SLO burn; high severity vulnerability exploitable in AIRA context; DLQ/replay failure affecting customers; missing rollback for production release; agent guardrail bypass in non-prod with production relevance. | Same business day response or faster, owner assigned, workaround, RCA/problem record, corrective action, monitoring watch. |
| SEV-3 Medium | Non-critical service degradation, dashboard gap, alert misfire, non-prod environment failure, recurring minor defect, medium vulnerability. | Triage within SLA, backlog item or problem record, remediation owner, evidence closure. |
| SEV-4 Low | Cosmetic operational issue, documentation gap, minor support friction, non-blocking alert tuning. | Planned remediation or knowledge update with owner and due date. |
| Incident Lifecycle Stage | Required Operational Evidence |
| --- | --- |
| Detect | Alert, user report, CI/CD failure, SIEM case, Sentry issue, dashboard threshold, DLQ signal, System Builder/agent tripwire. |
| Classify | Severity, service, criticality, data classification, affected users/processes, security/AI/provisioning involvement, blast radius estimate. |
| Contain | Feature flag safe-disable, rollback, route block, credential revoke, agent suspend, policy rollback, queue pause, circuit breaker, communication owner. |
| Diagnose | Trace reconstruction, log query, metrics, GitNexus impact, recent change list, CI/release evidence, policy decision, outbox/DLQ/event evidence. |
| Recover | Rollback, forward-fix, restore, replay, compensation, cache rebuild, re-indexing, manual workaround, approved runbook execution. |
| Validate | Smoke tests, synthetic checks, SLO recovery, security validation, evidence completeness, user confirmation where needed. |
| Learn | PIR/RCA, known error, runbook update, test/fitness improvement, Auto-Heal/Learn/Improve candidate, backlog linkage. |
| Close | Named owner approval, residual risk, monitoring period, evidence path, stakeholder communication, recurrence watch. |

# 8. Observability, APM, Logging, Metrics, Tracing, and Runtime Toggles
| Signal / Capability | Operational Requirement | Runtime Toggle Rule |
| --- | --- | --- |
| Log4j2 structured logs | JSON or structured logging with trace_id, service, environment, release, safe actor hash, classification, error_code, and redaction profile. | Log verbosity may be raised temporarily by approved runtime config with expiry, audit, owner, and rollback. Audit/security logs cannot be disabled. |
| OpenTelemetry traces | End-to-end traces across frontend, gateway, service, workflow, database, Kafka, MicroFunction runtime, AI gateway, and evidence store. | Sampling may be tuned through governed policy. Critical incidents may require temporary elevated sampling with retention and privacy controls. |
| Sentry / error monitoring | Release health, error fingerprinting, suspect commits, user-impact estimation using redacted metadata only. | Breadcrumb capture must obey forbidden telemetry rules; screenshots or payload capture require classification approval. |
| Loki / Tempo / Grafana | Dashboards and trace/log correlation for service health, SLOs, incidents, policy denial, queues, AI routes, and evidence completeness. | Dashboard access is role/classification-controlled. Emergency sharing requires redaction. |
| Audit and evidence | Append-only business/security/governance evidence for decisions, approvals, policy results, runbook actions, tool actions, and runtime toggles. | Protected-action audit is not optional. Failure to write audit/evidence blocks or escalates per fail-safe policy. |
| Runtime feature/diagnostic toggles | Operational toggles for telemetry verbosity, tracing sampling, diagnostic endpoints, AI panel activation, workspace modules, replay tools, and resilience tests. | Toggles are configuration artifacts with owner, scope, expiry, risk tier, OPA/SBAC check, audit event, rollback path, and dashboard visibility. |

# 9. Dynamic Workspace and Frontend Operations
| Operational Area | Required Control | Evidence |
| --- | --- | --- |
| Workspace resolution | Backend-governed, policy-filtered workspace resolver; frontend never becomes business authority. | WORKSPACE_RESOLVED audit event, policy decision, layout hash, cache source, trace_id. |
| Component / widget operations | Each component has owner, capability_code, API contract, classification, fallback behavior, performance SLO, and safe error state. | Component catalog record, API contract test, dashboard panel, frontend error evidence. |
| Admin Builder / templates | Template publish, rollback, retirement, activation, and seed sync require maker-checker approval and audit. | Template version, approver, activation log, rollback test, impact evidence. |
| AI assistant panel | Prompt metadata, model route, guardrail result, retrieval decision, artifact reference, classification, and human review state are captured. | AI_PROMPT_SUBMITTED and AI_ARTIFACT_GENERATED events, model route audit, guardrail result. |
| Accessibility and responsive UX | Operational readiness includes accessibility smoke checks, responsive rendering checks, and user-safe error messages. | UI test report, a11y check, screenshot evidence with no sensitive data. |
| Frontend incident handling | Frontend errors must correlate to backend traces, release ID, component key, and user-safe impact. | Sentry/browser telemetry, trace correlation, affected release, rollback/safe-disable plan. |

# 10. MicroFunction, API, Event, and Data Operations
| Domain | Operational Requirement | Runbook / Evidence Requirement |
| --- | --- | --- |
| MicroFunction runtime | Transactions have owner, step sequence, runtime config version, idempotency profile, error policy, audit profile, observability profile, and rollback strategy. | Transaction dashboard, step trace, runtime config evidence, rollback/disable runbook. |
| OpenAPI / REST | APIs are contract-first, secure, observable, rate-limited, idempotent where mutating, and safe-error compliant. | OpenAPI contract ref, API gateway telemetry, auth tests, DAST evidence, incident runbook. |
| AsyncAPI / Kafka | Topics, schemas, producers, consumers, DLQ, retry, replay, and schema evolution have owners and support procedures. | Topic registry, schema compatibility report, consumer lag dashboard, DLQ/replay approval runbook. |
| Avro / CloudEvents | Event payloads and CloudEvents envelope fields are governed and versioned. | Schema ID/version, compatibility mode, event_id/correlation_id/causation_id evidence. |
| Outbox / inbox | State-changing events use transactional outbox and idempotent inbox/consumer handling. | Outbox status dashboard, duplicate test, replay evidence, DLQ closure record. |
| Flyway / database | No manual production DDL. Migrations, seeders, RLS, indexes, and rollback/forward-fix plans are reviewed and evidenced. | Flyway report, checksum, DBA approval, performance check, restore/reversal test where needed. |
| Redis/Valkey/cache | Cache accelerates truth but is never authority. Cache invalidation and rebuild are runbooked. | Cache hit/miss dashboard, invalidation audit, rebuild runbook, source-of-truth verification. |

# 11. Security Operations, SIEM/SOAR, Authenticated DAST, and Secrets Hygiene
| Security Operations Area | Minimum Control | Evidence |
| --- | --- | --- |
| SIEM/XDR | Wazuh or approved equivalent receives relevant OS, container, application, identity, policy, audit, and security events. | SIEM rule, alert sample, case link, retention and classification rule. |
| Case management / SOAR | TheHive/Cortex or approved equivalent may assist triage and enrichment but must not bypass human accountability. | Case ID, analyzer/responder output, approval, containment action, audit trail. |
| Authenticated DAST | Authenticated scans use synthetic accounts, non-prod targets unless approved, bounded scope, rate limits, and secrets-safe configuration. | DAST plan, test account, findings report, remediation evidence, waiver if unresolved. |
| Secrets hygiene | No secrets in source, .env shared files, logs, traces, screenshots, prompts, Obsidian, LLM Wiki, GitNexus reports, or tickets. | Secret scan results, vault reference, rotation record, incident record if exposed. |
| Access review | Production, admin, agent, service account, model-route, tool, and dashboard access are periodically reviewed. | Access review record, recertification, removal evidence, exception expiry. |
| Abuse cases | Identity abuse, policy bypass, replay abuse, DLQ/replay misuse, AI prompt/route abuse, agent tool misuse, and evidence tampering are mapped to controls. | Threat model mapping, detection rule, runbook, control test result. |

# 12. Resilience, Heavy Transaction, DR, Backup, Restore, and Continuity Operations
| Capability | Operating Standard | Validation Evidence |
| --- | --- | --- |
| Resilience patterns | Timeouts, retries, circuit breakers, bulkheads, fallback, queue backpressure, DLQ, compensation, and safe degradation are explicit. | Resilience test, dashboard panel, runbook, failure mode evidence. |
| Heavy transaction readiness | Critical flows are tested for concurrency, idempotency, duplicate callbacks, high load, lock contention, slow dependencies, and retry storms. | Load/concurrency test, idempotency test, DB contention report, queue lag test. |
| Replay and compensation | Replay requires risk classification, dedupe/idempotency, approver where needed, blast radius, and post-replay verification. | Replay request, approval, result, trace IDs, before/after metrics. |
| Backup and restore | Database, object/document store, configuration, policies, registry data, evidence stores, dashboards, and indexes have backup/restore plans. | Restore drill, RTO/RPO result, exception list, retention proof. |
| DR readiness | DR runbooks define service order, dependencies, DNS/routing, identity, secrets, data restore, queue handling, observability, and support communications. | DR test record, gap register, follow-up actions. |
| Safe-disable | Feature flags and runtime toggles can disable risky capability without breaking foundational login, audit, evidence, or policy controls. | Safe-disable test, rollback evidence, dashboard visibility. |

# 13. AI Agent, System Builder, Model Route, and Tool Action Operations
| Operational Subject | Mandatory Operations Control | Reject / Escalate If |
| --- | --- | --- |
| System Builder | Every intake, analysis, generation, validation, recommendation, PR/MR draft, and provisioning plan links to source, owner, classification, policy, evidence, and approval state. | Generated artifact influences behavior without intake/evidence record. |
| AI agents | Registered identity, owner, purpose, trust tier, SBAC skill, OPA policy, model route, tool scope, evaluation state, telemetry, and retirement path. | Shadow agent, stale certification, unknown owner, expired credential, or missing kill switch. |
| Tool/Harness actions | Agents request actions through Harness/tool gateway with dry-run where feasible, idempotency, policy decision, approval, and rollback metadata. | Agent has direct Git, CI/CD, DB, Kubernetes, Vault, Keycloak, model provider, or production credentials. |
| Model routes | LiteLLM aliases, guardrail checkpoints, fallback rules, data classification eligibility, quota, and incident response are operationalized. | Direct model-provider SDK call, unapproved route, fallback to disallowed model, or guardrail unavailable with fail-open behavior. |
| Memory/RAG | Retrieval eligibility, source authority, freshness, poisoning defense, access control, quarantine, and deletion/retention are monitored. | Restricted data retrieved through unauthorized route or stale/conflicting knowledge used as authority. |

# 14. Auto-Heal, Auto-Learn, and Auto-Improve Operating Controls
| Loop Stage | Allowed | Not Allowed | Evidence |
| --- | --- | --- | --- |
| Detection | Read approved alerts, traces, logs, metrics, CI failures, security findings, DLQ, workflow errors, SLO burn, and user feedback. | Read secrets or unredacted Restricted data through unauthorized route. | Signal ID, evidence_ref, classification, owner. |
| Analysis | Generate evidence-backed hypothesis, confidence, blast radius, affected contracts/tests/services, and recommended path. | Unsupported root cause, hallucinated fix, or action without evidence. | RCA draft, GitNexus impact, trace/log/metric refs. |
| Proposal | Draft PR, config candidate, runbook update, test improvement, rollback plan, replay plan, knowledge candidate, or backlog item. | Direct production edit, manual DDL, direct kubectl, direct secrets/policy/model-route mutation. | Candidate ID, test plan, risk tier, approval path. |
| Execution | Run approved non-prod tests or pre-approved low-risk reversible action through Harness/SBAC/OPA. | Production-impacting action without named approval and evidence. | Harness action record, OPA decision, audit event. |
| Verification | Collect tests, telemetry, security, fitness, business validation, and before/after metrics. | Mark resolved without independent evidence or monitoring period. | Verification pack, dashboard refs, post-action review. |
| Learning | Create reviewed knowledge, runbook, prompt/guardrail test, evaluation dataset item, or architecture fitness improvement. | Auto-promote lessons, standards, prompt changes, guardrails, or policies as authoritative. | Knowledge candidate, reviewer, classification, publication state. |

# 15. RACI and Operating Responsibilities
| Activity | Accountable | Responsible | Consulted / Informed |
| --- | --- | --- | --- |
| Service catalog and readiness approval | IT Head / Service Owner | SRE Lead, DevSecOps Lead, Application Owner | Security, QA, DBA, Internal Audit, Business Owner |
| SLO/SLI definition and review | SRE Lead | Application Owner, DevSecOps, QA/SDET | Business Owner, Security, Internal Audit |
| Incident command | Incident Commander | Service Owner, SRE, Security, DevSecOps | IT Head, Business Owner, CAB/ARB as needed |
| Security operations case | Security Lead | Security Admin, SRE, Platform Engineering | AI Governance, Internal Audit, Legal/Risk as needed |
| Runbook authoring and execution | Service Owner | SRE, DevSecOps, DBA, Platform Engineering | QA, Security, Architecture |
| Dynamic Workspace operations | Frontend / Workspace Owner | Frontend, Backend, DevSecOps, SRE | Security, Product Owner, Accessibility reviewer |
| MicroFunction runtime operations | Backend / MicroFunction Owner | Backend Lead, SRE, DBA, DevSecOps | Security, QA, Product Owner |
| AI agent operations | AI Governance / Agent Owner | AI Engineering, DevSecOps, Security | SRE, Internal Audit, Architecture |
| Auto-Heal/Learn/Improve governance | SRE / AI DevSecOps Lead | DevSecOps, AI Engineering, QA/SDET | Architecture, Security, Product Owner, Internal Audit |
| Operational acceptance | CAB / ARB where applicable | Service Owner, DevSecOps, SRE | Business Owner, Security, Internal Audit |

# 16. Implementation Roadmap and Acceptance Criteria
| Phase | Target Outcome | Exit Evidence |
| --- | --- | --- |
| P0 - Baseline readiness | Service catalog, owners, support queues, criticality, SLO drafts, operating evidence path, standard runbook template. | Catalog export, Zammad queues, owner map, readiness checklist. |
| P1 - Observability operationalization | 31A v1.2 telemetry implemented for foundation services, Dynamic Workspace, MicroFunction runtime, and CI/CD evidence. | Dashboards, alert rules, trace/log/metric samples, audit/evidence queries. |
| P2 - Incident and runbook readiness | Incident lifecycle, major incident command, recovery runbooks, rollback, replay, restore, and safe-disable are tested. | Incident drill, runbook execution records, rollback/replay/restore evidence. |
| P3 - Security operations integration | SIEM/XDR, case management, authenticated DAST, secrets hygiene, access reviews, and abuse-case detection are integrated. | Security case samples, DAST reports, secret scan, access recertification. |
| P4 - AI and System Builder operations | Agent registry, model routes, guardrails, tool action evidence, kill switch, and agent incident runbooks are ready. | Agent dashboard, policy denials, guardrail samples, certification and suspension test. |
| P5 - Controlled improvement loop | Auto-Heal/Learn/Improve candidate loop operates with evidence, tests, human approval, and knowledge review. | Candidate records, draft PR, review workflow, before/after metric, closure evidence. |
| Acceptance ID | Acceptance Criterion |
| --- | --- |
| AC-01 | Every production-bound service has owner, criticality, SLO/SLI profile, support queue, dashboards, alerts, runbooks, security monitoring, rollback/recovery plan, evidence path, and operational acceptance record. |
| AC-02 | Dynamic Workspace and MicroFunction runtime operations can be traced from UI action or API/event input to backend policy decision, transaction steps, audit/outbox, telemetry, and evidence record. |
| AC-03 | CI/CD, GitNexus, SBOM/provenance, SAST/SCA/DAST, contract, Flyway, architecture fitness, and post-deployment validation evidence are consumed by operations during service transition. |
| AC-04 | Logs, traces, metrics, audit records, dashboards, and runtime toggles comply with classification, redaction, retention, access, and fail-safe rules. |
| AC-05 | Incident, problem, RCA, Auto-Heal, Auto-Learn, and Auto-Improve loops produce attributable, verifiable, classifiable, and improvable evidence and cannot silently mutate production or source-of-truth systems. |
| AC-06 | Security operations can detect, triage, contain, and evidence identity, policy, secrets, AI route, agent tool, DAST, abuse-case, and evidence-tampering incidents. |
| AC-07 | Rollback, forward-fix, compensation, replay, cache rebuild, re-indexing, backup/restore, and DR runbooks have been tested or risk-accepted with owner and due date. |

# 17. Non-Negotiable Rejection Rules

Reject service readiness when a service has no named owner, support queue, criticality, or SLO/SLI profile.

Reject release transition when protected actions cannot be reconstructed through trace, log, metric, audit, policy, approval, and evidence references.

Reject operations acceptance when secrets, raw tokens, raw PII, raw prompts, restricted records, or unrestricted payloads appear in logs, traces, screenshots, prompts, tickets, dashboards, or evidence summaries.

Reject any AI agent, System Builder action, model route, or tool action that can bypass registry, identity, SBAC, OPA, Harness, guardrails, audit, or human approval when required.

Reject production use of Dynamic Workspace capabilities that make frontend code the business authority or bypass backend policy and MicroFunction execution.

Reject state-changing flows without idempotency, audit/outbox, DLQ/replay where applicable, rollback/compensation, and monitoring evidence.

Reject Auto-Heal, Auto-Learn, or Auto-Improve candidates that weaken SOLID, Clean Architecture, DDD ownership, ports/adapters, security, observability, testability, reversibility, or AVCI evidence.

# 18. AVCI Compliance Summary
| AVCI Property | Evidence in This Standard |
| --- | --- |
| Attributable | Defines owners, co-owners, service owners, incident commanders, support queues, RACI, Zammad records, runbook ownership, agent owners, model route owners, and evidence paths. |
| Verifiable | Requires SLO/SLI dashboards, trace/log/metric/audit evidence, CI/CD and GitNexus evidence, runbook tests, restore/replay tests, DAST/security evidence, incident/RCA proof, and acceptance criteria. |
| Classifiable | Requires classification-aware telemetry, redaction, secrets hygiene, dashboard access control, evidence retention, SIEM/case handling, and restricted-data escalation rules. |
| Improvable | Converts incidents, SLO burn, problems, security findings, operational reviews, runbook gaps, and Auto-Heal/Learn/Improve candidates into governed backlog, knowledge, test, policy, and architecture improvements. |
| Final Control Statement AIRA production operations are complete only when services can be supported without hidden tribal knowledge, recovered without uncontrolled mutation, secured without fail-open shortcuts, observed without sensitive leakage, improved without architecture drift, and audited through AVCI evidence. Operations may use automation and AI assistance, but accountability, policy, evidence, and human approval remain mandatory where risk requires. |
| --- |

