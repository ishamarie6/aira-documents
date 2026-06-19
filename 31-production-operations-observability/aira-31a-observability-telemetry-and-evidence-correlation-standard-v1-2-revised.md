---
title: "Observability Telemetry and Evidence Correlation Standard"
doc_id: "AIRA-31A"
version: "v1.2"
status: "revised"
category: "Production operations and observability"
source_docx: "AIRA_31A_Observability_Telemetry_and_Evidence_Correlation_Standard_v1.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 31-production-operations-observability
  - revised
  - aira-31a
---



# Observability Telemetry and Evidence Correlation Standard



AIRA

AI-Native Enterprise Platform

Observability, Telemetry, and Evidence Correlation Standard

v1.2 Revised

Log4j2 - OpenTelemetry - Sentry - Loki - Tempo - Grafana - Audit - Evidence Packs - Dynamic Workspace - MicroFunction Runtime - GitNexus - Runtime Toggles - Trace Reconstruction
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-031A |
| Canonical Filename | AIRA_31A_Observability_Telemetry_and_Evidence_Correlation_Standard_v1.2_Revised.docx |
| Version | v1.2 - PoC 4 observability foundation, revised Greenfield/Sprint 0/CI-CD/PoC 2 alignment, Dynamic Workspace, MicroFunction backend, API/eventing, resilience lab, runtime telemetry toggle, GitNexus, AI agent, and continuous improvement evidence update |
| Supersedes | 31A-AIRA_Observability_Telemetry_and_Evidence_Correlation_Standard_v1.1_System_Builder_Update.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Architecture, DevSecOps, SRE, Security, QA/SDET, Platform Engineering, AI Governance, DBA, and Internal Audit Review |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; DevSecOps Lead; SRE / Operations; Security Architecture; QA/SDET; Platform Engineering; AI Engineering; DBA; Knowledge Governance; Internal Audit |
| Primary Companion | 31-AIRA Production Operations, SRE, SLA/SLO, and Service Management Standard |
| Revised Companion Sources | 09 v3.2 Greenfield Environment; 19B v1.2 Sprint 0; 20 v1.2 CI/CD Evidence Pack; 39A/39B/39C workstation and System Builder Lite setup; 45 v1.2 PoC 2 DevSecOps System Factory; 42C v1.3 Foundation PoC Roadmap |
| Core AIRA Sources | 01/01A AVCI and Enterprise Design Principles; 02 Engineering Blueprint; 03 Developer Guide; 04 Technology Stack; 10/10A/10B/10C/10D/10E MicroFunction; 12A and 41/46-61 Dynamic Workspace; 15/15A API; 16/16A/16B Database/Flyway; 17/17A Security; 19 GitNexus; 30/30A Change/Reversibility; 42D-42S AI Agent Governance; 43 Continuous Improvement |
| External Alignment Reference | NIST SP 800-218 SSDF; NIST SP 800-218A initial public draft where applicable for AI software; OWASP ASVS 5.0.0; OpenTelemetry Semantic Conventions; SLSA v1.2 |
| Review Cadence | At every observability PoC milestone, every telemetry schema change, every dashboard/alert change, every major release, after Sev-1/Sev-2 incidents, and quarterly after stabilization |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Observability-Telemetry-Evidence-Correlation / v1.2 / |
| Mandatory Operating Rule No AIRA service, workflow, MicroFunction, Dynamic Workspace action, System Builder intake, generated artifact, AI agent action, environment provisioning action, database migration, policy change, event consumer, release, incident response, Auto-Heal proposal, Auto-Learn candidate, or Auto-Improve candidate is production-ready unless it emits classification-safe telemetry and can be reconstructed through correlated logs, traces, metrics, audit records, policy decisions, evidence references, Git/CI evidence, and named human or system decisions. Observability may be performance-tuned, sampled, and toggled only through governed, audited, policy-checked, reversible runtime configuration. |
| --- |

# 1. Executive Summary and v1.2 Governance Verdict

AIRA is an AI-native, mission-critical enterprise platform. Its behavior must be explainable after the fact, testable before release, observable during execution, and improvable through evidence. This standard defines the implementation model for logs, traces, metrics, audit records, evidence references, dashboards, alerting, error monitoring, trace reconstruction, runtime telemetry toggles, and evidence correlation across AIRA services, Dynamic Workspace, MicroFunction runtime, API/eventing, CI/CD, System Builder, AI agents, and continuous improvement loops.

Version 1.2 strengthens the v1.1 System Builder observability update by explicitly aligning to the revised Greenfield Environment, Sprint 0, CI/CD Evidence Pack, PoC 2 System Factory, Dynamic Workspace, MicroFunction backend, API/eventing, resilience lab, security hardening, and proposal-driven Auto-Heal/Auto-Learn/Auto-Improve standards. It also introduces a governed runtime telemetry toggle model so diagnostic depth can be increased or reduced without weakening AVCI, auditability, classification, security, or reversibility.
| Strategic Outcome | v1.2 Required Result |
| --- | --- |
| Traceable behavior | Every critical path has trace_id, span_id, request_id, correlation_id, causation_id, evidence_ref, owner, classification, and policy decision linkage. |
| Safe telemetry | Logs, traces, metrics, prompts, dashboards, screenshots, and evidence packs are redacted, classified, retention-governed, and forbidden from exposing secrets, tokens, raw PII, raw prompts with restricted data, embeddings, or unrestricted customer payloads. |
| Evidence by construction | CI/CD, GitNexus, PR/MR, OpenAPI/AsyncAPI, Flyway, Kafka, outbox/inbox, Dynamic Workspace, MicroFunction, AI agent, and incident evidence link into one reconstructable chain. |
| Operational readiness | Log4j2, OpenTelemetry, Sentry, Loki, Tempo, Grafana, Prometheus/Mimir/Thanos where approved, audit stores, and evidence registers are part of foundation readiness, not afterthoughts. |
| Controlled performance flexibility | Sampling, debug logging, trace depth, dashboard refresh, exception capture, and expensive diagnostics may be adjusted at runtime only through policy-checked, role-bound, audited, reversible configuration. |
| Proposal-driven improvement | Auto-Heal, Auto-Learn, and Auto-Improve consume telemetry as evidence, generate candidate proposals, and require tests, impact analysis, rollback, and human approval before promotion. |

# 2. v1.2 Change Summary
| Change Area | v1.1 Baseline | v1.2 Improvement |
| --- | --- | --- |
| Foundation PoC alignment | System Builder telemetry and evidence correlation were defined. | Adds explicit PoC 4 observability foundation gates and aligns with PoC 2, PoC 3, PoC 5, Sprint 0, and CI/CD readiness. AMarket module development must not start until observability exit evidence is accepted. |
| Dynamic Workspace | Referenced as a companion source. | Defines workspace load/render/action/policy/AI panel telemetry, frontend performance metrics, accessibility evidence, component evidence_ref, and safe user-action audit events. |
| MicroFunction runtime | Referenced through MicroFunction framework. | Defines step-level telemetry, policy decision evidence, idempotency/outbox evidence, retry/compensation events, and forbidden direct infrastructure shortcut signals. |
| API/eventing | Covered through correlation architecture. | Adds OpenAPI/AsyncAPI/Kafka/Avro/CloudEvents/outbox/inbox/DLQ/replay telemetry requirements and schema/version evidence. |
| CI/CD and GitNexus | Evidence pack linkage was required. | Adds pipeline telemetry, GitNexus report hash, affected tests, architecture drift, supply-chain evidence, and CI trace-to-release correlation. |
| Runtime toggles | Not explicit enough. | Adds governed runtime telemetry toggle model with owner, risk tier, default, approval, audit, rollback, and performance guardrails. |
| Security and privacy | Classification-safe telemetry required. | Adds explicit forbidden telemetry fields, secret/PII redaction tests, high-cardinality metric label controls, authenticated DAST evidence, and remediation traceability. |
| Auto-* loops | Proposal-driven improvement required. | Adds complete detection-to-improvement evidence workflow and post-change telemetry review criteria. |

# 3. Purpose, Scope, and Authority

## 3.1 Purpose

Define the AIRA standard for logs, traces, metrics, audit records, evidence references, dashboards, alerting, error monitoring, and trace reconstruction.

Ensure every critical AIRA runtime, build-time, design-time, AI-assisted, and operations action remains attributable, verifiable, classifiable, and improvable.

Define how observability supports Dynamic Workspace, MicroFunction runtime, API/eventing, database/Flyway, CI/CD, GitNexus, AI agents, System Builder Lite, and continuous improvement loops.

Prevent telemetry leakage of secrets, PII, raw prompts, tokens, embeddings, restricted documents, excessive identifiers, and uncontrolled customer payloads.

Define controlled runtime telemetry toggles that protect performance without weakening audit, policy, evidence, or classification obligations.

## 3.2 In Scope / Out of Scope
| In Scope | Out of Scope |
| --- | --- |
| Application, API, Dynamic Workspace, MicroFunction, workflow, event, database, AI, agent, CI/CD, GitNexus, security, and operational telemetry. | Generic monitoring theory not adopted as AIRA control, unmanaged dashboards, personal logs, and unreviewed screenshots treated as authority. |
| Log4j2 structured logs, OpenTelemetry traces/metrics/context propagation, Sentry exception intelligence, Loki log aggregation, Tempo tracing, Grafana dashboards, audit stores, and evidence registers. | Direct storage of raw secrets, tokens, passwords, raw PII, raw KYC files, raw restricted prompts, unrestricted customer payloads, or embeddings in telemetry sinks. |
| Telemetry correlation for OpenAPI, AsyncAPI, Kafka, Avro, CloudEvents, outbox/inbox, idempotent consumers, DLQ/replay, schema evolution, and API gateways. | Event publishing or consumer behavior without idempotency, replay, schema, audit, and correlation evidence. |
| Runtime telemetry toggles, sampling, diagnostic levels, emergency capture, redaction profiles, and safe performance tuning. | Ungoverned turning off of required audit, security telemetry, policy decision logging, evidence records, or incident signals. |
| Auto-Heal/Auto-Learn/Auto-Improve detection, evidence retrieval, candidate proposal, testing, human approval, and post-change monitoring. | Silent self-healing, self-learning, self-improving, self-approval, direct production mutation, or automatic promotion of knowledge without review. |

## 3.3 Authority and Precedence
| Level | Authority | 31A v1.2 Interpretation |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance | Final authority for observability architecture, production-impacting telemetry exceptions, critical data-handling risk, and major conflict resolution. |
| L1 | 01 AVCI, 01A Enterprise Design Principles, 02 Engineering Blueprint, 05 Information Nervous System | Universal evidence, architecture, security, classification, source authority, and improvement discipline. |
| L1 | 31 Production Operations, SRE, SLA/SLO, and Service Management Standard | Defines operating model, service ownership, SLOs, incident management, and service readiness. 31A defines detailed telemetry and evidence correlation. |
| L2 | This 31A v1.2 Standard | Canonical implementation standard for observability, telemetry, monitoring, evidence correlation, runtime telemetry toggles, and trace reconstruction. |
| L3 | 10E, 11A, 12A, 15/15A, 16B, 17A, 19, 20, 30A, 42, 43, 45, 46-61 | Specialist standards that must emit and consume 31A-compliant evidence. |
| L4 | Tickets, ADRs, PRs/MRs, CI runs, GitNexus reports, audits, dashboards, incidents, runbooks | Implementation and operating evidence that must link into the 31A correlation chain. |
| Conflict Rule When documents conflict, the stricter AIRA control governs. The conflict must be logged as an AVCI reconciliation item with severity, owner, decision path, affected documents, and register tracking. Runtime convenience must not override source authority, auditability, security, or AVCI. |
| --- |

# 4. Canonical Correlation Architecture
| Correlation Rule AIRA observability is not separate from engineering evidence. The same intent-to-runtime chain must connect requirement, intake, source, branch, commit, CI run, tests, scan results, contract version, migration, policy decision, generated artifact, deployment, runtime traces, incidents, and improvement records. |
| --- |
| Correlation Layer | Primary Identifiers | Required Use |
| --- | --- | --- |
| Intent and intake | intake_id, ticket_id, requirement_id, source_ref, owner_id, classification | Every requirement, evidence upload, improvement request, agent request, or provisioning request receives governed identity before analysis or generation. |
| Design and decision | adr_id, tdl_id, waiver_id, bounded_context, capability_code, policy_ref | Architecture, policy, data, API, workflow, AI, and environment decisions must be traceable and reviewable. |
| Source and build | repo, branch, commit_sha, pr_id, ci_run_id, artifact_digest, sbom_ref, provenance_ref | Every generated artifact and evidence pack links to source control and CI/CD. |
| Contract and data | openapi_ref, asyncapi_ref, avro_schema_id, cloudevent_type, flyway_version, migration_checksum | APIs, events, schemas, and migrations remain versioned and reconstructable. |
| Runtime request | trace_id, span_id, request_id, correlation_id, causation_id, idempotency_key, actor_hash | Runtime actions link across frontend, gateway, services, workflows, database, events, and AI routes. |
| Policy and approval | opa_decision_id, sbac_skill_code, approval_id, reviewer_id, checker_id, cab_ref | Authorization, approval, and SoD controls are evidence-producing. |
| Evidence and learning | evidence_ref, incident_id, problem_id, rca_id, improvement_id, backlog_id | Operational findings become governed improvement inputs. |

# 5. Mandatory Signal Standards
| Signal | AIRA Standard | Required Evidence | Forbidden / Controlled |
| --- | --- | --- | --- |
| Logs | Log4j2 structured JSON logs with bounded fields, environment, service, route, trace_id, request_id, actor_hash, severity, error_code, and classification. | Log query reference, redaction proof, logger configuration version, sampling/toggle state. | No passwords, tokens, raw JWTs, secrets, raw PII, raw prompts, full payload dumps, embeddings, or high-cardinality metric-like labels. |
| Traces | OpenTelemetry traces with context propagation across frontend, gateway, backend, MicroFunction runtime, DB, Kafka, workflow, AI gateway, and external adapters. | trace_id, span_id, parent_span, service.name, route/topic, policy_decision_id, evidence_ref. | No sensitive payload attributes; span events must be redacted and bounded. |
| Metrics | OpenTelemetry/Prometheus-compatible metrics with bounded labels and approved SLO/SLI definitions. | Dashboard panel, alert rule, SLO target, threshold, owner, review cadence. | No account numbers, user IDs, document IDs, raw IPs, unrestricted tenant IDs, or high-cardinality labels. |
| Audit Events | Append-only business/security/governance audit records for actions, decisions, approvals, denials, template changes, policy changes, migrations, agent actions, and runtime toggles. | audit_event_id, actor_hash, action, source_ref, policy_ref, approval_ref, classification, result. | Audit cannot be disabled for protected actions. Missing audit requires fail-closed or incident recording. |
| Evidence Records | AVCI evidence records linked to source, owner, tests, scans, approvals, runtime traces, dashboards, and improvement path. | evidence_id, artifact_type, owner, source_ref, verification_evidence, classification, reversibility. | Evidence store cannot be a dumping ground for unclassified raw data. |
| Exception Intelligence | Sentry or approved equivalent for application exceptions, release health, suspect commits, and user-impact monitoring. | release_id, environment, error_fingerprint, affected route, linked trace, remediation reference. | No secret/PII breadcrumbs, request bodies, tokens, or screenshots without classification approval. |
| Dashboards | Grafana dashboards for service health, SLOs, logs, traces, errors, CI evidence, System Builder, Dynamic Workspace, AI agents, and continuous improvement. | dashboard_url/ref, owner, data classification, alert linkage, review cadence. | Dashboards must not expose restricted identifiers to broad viewers. |

# 6. Canonical Telemetry Field Model
| Field Group | Required Fields | Notes |
| --- | --- | --- |
| Actor and tenancy | actor_type, actor_hash, service_account_ref, agent_id, tenant_id_or_hash, org_unit_ref | Use hashes or stable safe identifiers. Do not expose raw PII unless classification and access rules explicitly permit. |
| Request correlation | trace_id, span_id, request_id, correlation_id, causation_id, session_ref_hash, idempotency_key | Required for all critical user, service, event, workflow, and agent actions. |
| Source and release | repo, branch, commit_sha, build_id, artifact_digest, release_id, environment, feature_flag_state | Used to connect runtime evidence to CI/CD and PR/MR evidence. |
| Contract and schema | api_operation_id, openapi_ref, asyncapi_ref, topic_name, cloudevent_type, schema_id, schema_version | Required for API, event, Kafka, webhook, and integration flows. |
| Policy and classification | classification, data_domain, policy_ref, opa_decision_id, sbac_skill_code, access_result, redaction_profile | Classification drives route, storage, masking, retention, and model eligibility. |
| MicroFunction | transaction_code, transaction_version, step_code, step_order, step_result, retry_count, compensation_ref, audit_event_id | Required for runtime-assembled transactions and step-level traceability. |
| Workspace | workspace_code, screen_code, component_key, component_instance_id, layout_hash, template_version, widget_action_id | Required for Dynamic Workspace resolution, rendering, personalization, and widget action tracing. |
| AI and agents | model_alias, guardrail_policy_version, prompt_template_ref, retrieval_decision_id, tool_action_id, trust_tier, autonomy_tier | Required for System Builder, AI assistant panel, agent runtime, retrieval, and tool action evidence. |
| Improvement | incident_id, problem_id, rca_id, improvement_id, candidate_id, backlog_id, post_action_review_ref | Required for Auto-Heal, Auto-Learn, Auto-Improve, RCA, and knowledge update loops. |

# 7. Dynamic Workspace Observability
| Workspace Event | Minimum Evidence | Acceptance Rule |
| --- | --- | --- |
| WORKSPACE_RESOLVED | actor_hash, workspace_code, role/skill context, policy_hash, layout_hash, cache_source, template_version, trace_id, evidence_ref | Workspace resolution must be reconstructable without exposing sensitive data. |
| COMPONENT_RENDERED | component_key, component_instance_id, screen_code, classification, capability_code, data_source_ref, render_latency_ms | Every rendered component must be policy-eligible and contract-bound. |
| COMPONENT_FILTERED_BY_POLICY | hidden_component, OPA decision, SBAC skill, reason_code, safe_response, evidence_ref | Policy-denied UI state must be auditable and user-safe. |
| LAYOUT_CHANGED | old_layout_hash, new_layout_hash, actor_hash, version, approval requirement, rollback_ref | Personalization and admin template changes are auditable and reversible. |
| WIDGET_ACTION_INVOKED | capability_code, idempotency_key, API operation, MicroFunction transaction, policy decision, outcome, evidence_ref | Widget actions must be backend-governed, not frontend-authoritative. |
| AI_PROMPT_SUBMITTED | prompt_template_ref, input_mode, classification, model_alias, guardrail_result, retrieval_decision_id, evidence_ref | AI panel telemetry must not record raw restricted prompts unless explicitly permitted by classification policy. |
| AI_ARTIFACT_GENERATED | artifact_type, source_refs, model_alias, guardrail_result, storage_ref, retention_rule, review_state | AI artifacts remain candidate or review-ready until approved. |

# 8. MicroFunction Runtime Evidence Model
| Runtime Step / Concern | Telemetry Requirement | Blocking Failure |
| --- | --- | --- |
| Receive and correlate | STP-RCV and STP-COR create or propagate trace_id, request_id, correlation_id, causation_id. | Missing correlation on mutating or protected action. |
| Resolve actor/tenant/session | Record safe actor_hash, tenant/org context, session_ref_hash, channel, device risk where applicable. | Protected action proceeds without actor/session evidence. |
| Authorize/classify | OPA/SBAC/ABAC/RBAC decision, policy version, classification, data-handling route. | Policy dependency unavailable and action fails open. |
| Validate/idempotency | Input validation result, idempotency key, duplicate detection, replay status. | Duplicate business effect from retry or callback. |
| Execute business step | step_code, version, adapter used, result, duration, retry, safe error code. | Business MicroFunction directly calls DB/Kafka/Redis/OpenKM/model provider or writes audit directly. |
| Audit/outbox | audit_event_id, outbox_id, event_id, schema version, publish state, DLQ state. | State mutation without audit/outbox evidence. |
| Compensation/reversal | compensation_ref, rollback_strategy, forward_fix_ref, feature_flag_state. | No recovery path for state-changing action. |
| Evidence closeout | evidence_ref, test_ref, approval_ref, improvement_backlog_ref. | Transaction cannot be reconstructed from evidence. |

# 9. API, Event, Kafka, Avro, CloudEvents, Outbox, DLQ, and Replay Correlation
| Domain | Correlation Requirement | Required Tests / Evidence |
| --- | --- | --- |
| OpenAPI REST | operation_id, request_id, trace_id, actor_hash, idempotency_key, policy_decision_id, safe error code, evidence_ref. | OpenAPI lint, generated client test, contract test, negative auth test, safe error test. |
| AsyncAPI / Kafka | topic, partition, offset, event_id, correlation_id, causation_id, traceparent, schema_id, producer service, consumer service. | AsyncAPI lint, consumer contract, schema compatibility, produce/consume trace propagation. |
| Avro / Schema Evolution | schema_id, schema_version, compatibility_mode, migration_ref, producer_version, consumer_version. | Backward/forward compatibility tests and controlled deprecation evidence. |
| CloudEvents | id, source, type, specversion, subject, time, datacontenttype, traceparent, dataschema. | Envelope validation and topic registry evidence. |
| Outbox / Inbox | outbox_id, aggregate_id, event_id, status, published_at, inbox_dedupe_key, processed_at. | Transactional outbox test, duplicate event test, retry-safe consumer test. |
| DLQ / Replay | dlq_event_id, failure_reason, redaction_status, replay_request_id, approver, replay_result. | DLQ routing test, replay runbook, idempotent replay evidence, human approval when risk tier requires. |
| Workflow correlation | Temporal workflow_id/run_id/activity_id; Flowable process_instance_id/task_id/approver/DMN decision. | Retry, timeout, compensation, human approval, escalation, and SLA timer evidence. |

# 10. CI/CD, GitNexus, Evidence Pack, and Release Correlation
| Evidence Source | Required Observability Linkage | Acceptance Rule |
| --- | --- | --- |
| CI/CD run | ci_run_id, branch, commit_sha, build_image_digest, test reports, scan reports, SBOM, provenance, artifact_digest. | Pipeline evidence must be included in PR/MR and release evidence packs. |
| GitNexus | index_commit_sha, report_hash, affected_files, affected_tests, dependency graph, architecture drift, security-sensitive path, reviewer. | GitNexus is read-only and derivative. Its outputs support review but do not replace tests/scans/human judgment. |
| Security scans | SAST/SCA/secrets/image/DAST findings, severity, rule set, tool version, remediation_ref, waiver_ref. | Critical/high findings block unless formally remediated or waived with expiry and owner. |
| Architecture fitness | ArchUnit/Semgrep/OpenRewrite/dependency rule results, boundary violations, policy-as-code results. | Boundary, direct provider, direct DB, direct model, and frontend authority violations block. |
| Release evidence | release_id, artifact_digest, deployment_ref, rollback_plan, CAB/ARB approval, monitoring dashboard, smoke traces. | Release is not ready without post-deployment telemetry and rollback evidence. |
| Evidence Pack | evidence_manifest_id, classification, retention, source_refs, verification refs, approver, improvement_path. | Evidence pack must be machine-readable, human-reviewable, and stored in approved path. |

# 11. Runtime Telemetry Toggle and Performance Control Model
| Runtime Toggle Rule AIRA may allow selected telemetry controls to be adjusted on-the-fly for performance, troubleshooting, or incident response. This flexibility is permitted only when the toggle is policy-governed, SBAC-scoped, audited, time-bound where required, reversible, and unable to disable mandatory audit/security/evidence collection for protected actions. |
| --- |
| Toggle Category | Allowed Runtime Adjustment | Controls Required | Cannot Disable |
| --- | --- | --- | --- |
| Log verbosity | Raise/lower diagnostic level per service, package, tenant-safe scope, request class, or temporary incident window. | SBAC skill, OPA decision, change/audit event, expiry, safe redaction profile. | Security audit logs, policy decisions, access denials, secret scan alerts. |
| Trace sampling | Adjust sampling rate, always-sample selected incident trace, sample low-risk high-volume paths. | Approved profile, bounded duration, environment scope, dashboard/audit record. | Trace correlation for protected actions, incident reconstruction evidence. |
| Metrics cardinality | Enable/disable optional diagnostic labels and histograms. | Label allowlist, cardinality budget, owner, SRE approval for production. | Core SLI/SLO metrics, security and availability indicators. |
| Sentry / error capture | Enable release-health, breadcrumbs, stack traces, or additional context with redaction. | Redaction profile, environment scope, data classification review. | Critical exception reporting for production-bound services. |
| Frontend diagnostics | Enable workspace performance timing, component render tracing, client action breadcrumbs, visual/a11y diagnostics. | No raw PII, no tokens, no raw payloads; feature flag and audit event required. | User action audit for protected widget actions. |
| AI/agent diagnostics | Enable model route metrics, guardrail decisions, retrieval trace, tool action telemetry, trust/demotion signals. | AI Governance and Security controls, classification-aware storage, evidence_ref. | Guardrail result, policy decision, tool action audit, model route audit. |
| Emergency incident mode | Increase capture depth for active incident. | Incident ID, approver, timebox, post-review, data disposal or retention rule. | Mandatory data-handling, redaction, and evidence capture. |

# 12. Security, Classification, Redaction, and Forbidden Fields
| Control Area | Mandatory Rule | Evidence |
| --- | --- | --- |
| Classification | Every telemetry item must carry or inherit classification and handling rules. | classification field, redaction_profile, retention_rule, model_route_eligibility. |
| Secret safety | Never log passwords, tokens, refresh tokens, ID tokens, raw JWTs, API keys, private keys, credentials, seed secrets, or vault material. | Gitleaks/log redaction tests, SAST rules, forbidden field test report. |
| PII minimization | Use actor_hash, tenant-safe identifier, or classified reference instead of raw PII. | Data-handling review, privacy/security approval where raw PII is unavoidable. |
| Prompt and AI content | Do not store raw restricted prompts, confidential document payloads, embeddings, or unrestricted retrieval context in broad telemetry sinks. | Prompt metadata only, prompt_template_ref, context_hash, retrieval_decision_id, guardrail_result. |
| Metrics labels | Use bounded low-cardinality labels only. | Cardinality budget and dashboard review. |
| Dashboards | Dashboards must be access-controlled by role/skill/classification and must not expose restricted fields to broad viewers. | Dashboard ACL, owner, review cadence, classification label. |
| Incident evidence | Screenshots, dumps, logs, and attachments must be malware-scanned, hashed, classified, redacted, and stored in approved evidence paths. | File evidence record, hash, malware scan, classification, retention, access audit. |

# 13. Trace Reconstruction and Resilience Lab Observability
| Scenario | Telemetry Required | Exit Criteria |
| --- | --- | --- |
| End-to-end user action | Frontend workspace action -> gateway -> backend -> MicroFunction -> DB/outbox -> Kafka -> consumer -> audit -> dashboard. | One trace or linked trace chain reconstructs the full path and human/business outcome. |
| Duplicate/retry/replay | Retry count, idempotency key, dedupe decision, outbox/inbox state, replay_request_id, final business effect. | No duplicate business effect; replay evidence is deterministic and approved where required. |
| DLQ incident | failure_reason, original event metadata, redaction state, policy decision, owner, replay/repair plan. | DLQ item can be triaged, fixed, replayed, or retired with evidence. |
| Concurrent heavy transaction | lock wait, contention, bulkhead, circuit breaker, queue depth, latency, error budget, fallback state. | Load/failure test identifies safe behavior under heavy transaction conditions. |
| Policy/identity dependency failure | OPA/Keycloak/Vault/guardrail dependency state, fail-closed decision, safe response, incident/evidence ref. | Protected action stops safely; support team can reconstruct cause. |
| Telemetry sink degradation | exporter status, queue depth, dropped spans/logs/metrics, fallback evidence, audit continuity. | System degrades safely without leaking data; protected actions block when required evidence cannot be captured. |
| Rollback/feature disablement | feature_flag_state, config version, approver, rollback_ref, post-change dashboard. | Rollback/forward-fix is visible, controlled, and reversible. |

# 14. AI Agent, System Builder, and Continuous Improvement Observability
| Subject | Required Observability | Control Gate |
| --- | --- | --- |
| System Builder intake | intake_id, source_ref, owner, classification, request_type, risk_tier, affected contracts, evidence_ref. | No analysis/generation before intake evidence exists. |
| Generated artifact | artifact_id, generator, source standards, prompt_template_ref, validation results, reviewer, PR/MR ref. | Generated artifacts remain candidate until validated and approved. |
| AI agent action | agent_id, agent_version, skill_code, trust_tier, autonomy_tier, tool_action_id, policy decision, run_id, evidence_ref. | No tool action outside registry/SBAC/OPA/Harness and no self-approval. |
| Model route | model_alias, route_policy, guardrail_policy_version, input/output classification, redaction status. | Direct provider calls and unapproved routes are blocked. |
| Retrieval/RAG | source_id, chunk_id, classification, ACL, freshness, context_hash, retrieval_decision_id, citation/evidence completeness. | No unapproved or poisoned source becomes authority. |
| Auto-Heal | trigger, evidence, proposed fix, blast radius, test plan, rollback, approval path, post-change monitoring. | May propose and draft only unless bounded reversible action is pre-approved by policy. |
| Auto-Learn | lesson candidate, source evidence, conflict check, reviewer, publication status, retirement path. | Knowledge candidate requires human review before retrieval eligibility. |
| Auto-Improve | measurable benefit, implementation plan, tests, risk, architecture impact, monitoring metric. | Improvement requires PR/MR, tests, policy checks, and approval. |

# 15. Required Dashboards and Alerts
| Dashboard / Alert Domain | Minimum Content | Audience |
| --- | --- | --- |
| AIRA Platform Health | Availability, latency, saturation, dependency health, error budget, release health, critical incidents. | SRE, DevSecOps, IT Head. |
| MicroFunction Traceability | transaction_code, step latency, policy denials, audit/outbox, retries, compensations, failed steps. | Developers, architects, QA/SDET, SRE. |
| Dynamic Workspace Health | workspace load latency, cache hit/miss, component render failures, policy-filtered components, widget actions, accessibility/performance trends. | Frontend, product, architects, SRE. |
| API/Eventing Health | API error rate, Kafka lag, DLQ depth, schema compatibility, outbox stuck items, replay outcomes. | Backend, integration, DBA, SRE. |
| Security and DAST | auth failures, policy denials, DAST findings, SAST/SCA high findings, secret scan events, remediation status. | Security, DevSecOps, Internal Audit. |
| CI/CD Evidence | build/test/scan pass rate, evidence completeness, GitNexus findings, waiver expiry, SBOM/provenance status. | DevSecOps, QA, architecture, audit. |
| System Builder / AI Governance | intake volume, generated artifacts, validation pass rate, agent actions, guardrail blocks, model routes, trust tier changes. | AI Governance, Security, Architecture. |
| Continuous Improvement | Auto-Heal/Learn/Improve candidates, accepted/rejected, cycle time, recurrence reduction, unresolved risks. | IT Head, DevSecOps, SRE, Knowledge Governance. |

# 16. Implementation Roadmap
| Phase | Activities | Exit Criteria |
| --- | --- | --- |
| Phase 1 - Governance adoption | Approve 31A v1.2, assign owners, confirm forbidden fields, define telemetry schemas, align with 31 SRE and 20 CI/CD. | Document approved for pilot use; owners and evidence path confirmed. |
| Phase 2 - Baseline instrumentation | Implement Log4j2 JSON logs, OTel SDK/collector, correlation propagation, Sentry, Loki, Tempo, Grafana, audit store linkage. | PoC 4 baseline service emits logs, metrics, traces, audit, and evidence_ref. |
| Phase 3 - Dynamic Workspace and MicroFunction coverage | Add workspace and MicroFunction telemetry fields, policies, tests, and dashboard panels. | Workspace action and MicroFunction transaction are reconstructable end-to-end. |
| Phase 4 - API/eventing/data/workflow coverage | Add OpenAPI/AsyncAPI/Kafka/Avro/CloudEvents/Flyway/outbox/DLQ/replay/workflow correlation. | Event-driven path and workflow path can be replayed and audited safely. |
| Phase 5 - Runtime toggle control | Implement audited configuration model for log level, trace sampling, metrics labels, Sentry context, and incident mode. | Toggles are SBAC/OPA controlled, audited, reversible, and tested. |
| Phase 6 - CI/CD and GitNexus integration | Bind telemetry validation, forbidden field tests, dashboard smoke, GitNexus outputs, and evidence manifest into pipeline gates. | Evidence pack includes telemetry proof and trace reconstruction result. |
| Phase 7 - Auto-* candidate loop | Use incidents and telemetry findings to generate proposal-driven improvements under maker-checker review. | Candidate loop produces approved or rejected improvements with evidence. |
| Phase 8 - Management reporting and audit readiness | Create evidence completeness dashboard, control sampling process, retention review, and management reporting pack. | Internal audit can sample and reconstruct critical flows. |

# 17. RACI
| Activity | IT Head / Architecture | DevSecOps | SRE / Operations | Development | QA/SDET | Security | DBA | AI Governance | Internal Audit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Approve 31A baseline | A | C | C | C | C | C | C | C | I |
| Telemetry schema design | A | R | R | C | C | C | C | C | I |
| Instrumentation implementation | C | C | C | R | C | C | C | C | I |
| Dashboard and alert ownership | C | C | A/R | C | C | C | C | C | I |
| Forbidden field and redaction tests | C | C | C | C | R | A/R | C | C | I |
| Runtime telemetry toggles | A | R | R | C | C | C | C | C | I |
| Incident trace reconstruction | C | C | A/R | C | C | C | C | C | I |
| AI/agent telemetry | C | C | C | C | C | C | I | A/R | I |
| Evidence sampling | C | C | C | C | C | C | C | C | A/R |

# 18. Acceptance Criteria and Definition of Done
| Acceptance Category | Required Evidence | Decision Rule |
| --- | --- | --- |
| Core instrumentation | Logs, traces, metrics, audit, evidence_ref, Sentry, Loki, Tempo, Grafana for representative critical flows. | No critical flow accepted without reconstructable evidence. |
| Correlation completeness | trace_id, request_id, correlation_id, causation_id, idempotency_key, policy_decision_id, evidence_ref propagated where applicable. | Missing mandatory correlation blocks foundation readiness. |
| Redaction and classification | Forbidden field tests, redaction profile, classification labels, retention rules, dashboard ACLs. | Telemetry leakage blocks acceptance. |
| Dynamic Workspace | Workspace resolution, component render/filter, widget action, AI panel, and template lifecycle events emitted and tested. | Frontend authority or untraced action blocks. |
| MicroFunction | Step-level trace, audit/outbox, policy, idempotency, retry, compensation, safe error, evidence closeout. | Direct infrastructure shortcuts or missing audit/outbox block. |
| API/eventing/data | OpenAPI/AsyncAPI/Kafka/Avro/CloudEvents/Flyway/outbox/DLQ/replay correlation proven. | Replay or schema drift failure blocks. |
| Runtime toggles | Toggle registry, policy, approval, audit, rollback, expiry, performance guardrails tested. | Uncontrolled toggle or disabled mandatory audit blocks. |
| Auto-* loop | Detection, evidence retrieval, proposal, tests, approval, PR/MR or knowledge candidate, post-monitoring evidence. | Silent mutation or self-approval blocks. |
| Audit readiness | Internal audit can sample an action and trace it from intake/source to runtime outcome and improvement backlog. | Sampling failure requires remediation before promotion. |

# 19. PR/MR and Runtime Evidence Summary Template
| ## AIRA Observability / Evidence Correlation Summary ### Attributable - Owner: - Service / bounded context: - Repository / branch / commit: - Intake / ticket / ADR / TDL: - CI run / release ID: ### Verifiable - Trace reconstruction evidence: - Log query evidence: - Metrics / dashboard evidence: - Audit event references: - Policy decision references: - Test evidence: - Security / redaction evidence: - GitNexus / impact evidence: ### Classifiable - Data classification: - Redaction profile: - Forbidden field test result: - Dashboard ACL / evidence storage path: - Retention rule: ### Improvable - Known telemetry gaps: - Incidents / findings linked: - Auto-Heal / Auto-Learn / Auto-Improve candidate: - Backlog item: - Review date: ### Runtime Toggle Record, if applicable - Toggle name / value: - Reason / incident ID: - Approved by: - Start / expiry: - Rollback / default value: - Audit event ID: |
| --- |

# 20. External Alignment Register
| External Source | AIRA 31A v1.2 Treatment |
| --- | --- |
| NIST SP 800-218 SSDF | Secure software practices are supported through evidence-producing telemetry for build, test, vulnerability response, release, operations, and improvement. Where SP 800-218A AI software considerations are used, they are candidate guidance and do not override AIRA governance. |
| OWASP ASVS 5.0.0 | Application security verification is reinforced through authenticated DAST evidence, secure API telemetry, access-control audit, safe error handling, and redaction controls. |
| OpenTelemetry Semantic Conventions | AIRA telemetry uses consistent semantic attributes for traces, metrics, logs, HTTP, database, messaging, CI/CD, errors, and GenAI/agent signals where mature and appropriate. |
| SLSA v1.2 | Supply-chain observability links artifacts, provenance, build evidence, CI runs, artifact digests, SBOMs, signatures, and release evidence into the same traceability model. |
| Google SRE / Observability practice references | SLOs, SLIs, alerts, error budgets, dashboards, incident review, and service ownership are implemented through AIRA 31 and 31A controls rather than informal monitoring. |

# 21. AVCI Compliance Summary
| AVCI Property | 31A v1.2 Evidence |
| --- | --- |
| Attributable | Document control, service owners, telemetry owners, dashboard owners, source_refs, CI runs, PR/MR records, policy decisions, runtime toggles, agent IDs, and approval records identify responsible actors and systems. |
| Verifiable | Logs, traces, metrics, audit events, Sentry issues, Loki queries, Tempo traces, Grafana dashboards, CI evidence, GitNexus reports, policy checks, tests, incidents, and trace reconstruction prove behavior. |
| Classifiable | Every telemetry and evidence record carries or inherits classification, redaction, model-route eligibility, ACL, retention, dashboard access, and forbidden-field controls. |
| Improvable | Incidents, failed gates, SLO burn, DLQ trends, policy denials, GitNexus drift, DAST findings, telemetry gaps, runtime toggle reviews, and user feedback become governed backlog, runbook, prompt, policy, test, and architecture improvements. |
| Final Control Statement AIRA observability is complete only when a reviewer, operator, auditor, or authorized AI assistant can safely reconstruct what happened, who or what caused it, which policy and evidence applied, what changed, how it was verified, how it can be reversed or improved, and why no sensitive data was exposed. |
| --- |

