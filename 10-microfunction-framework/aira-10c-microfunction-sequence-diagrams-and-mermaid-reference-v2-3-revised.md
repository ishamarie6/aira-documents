---
title: "MicroFunction Sequence Diagrams and Mermaid Reference"
doc_id: "AIRA-10C"
version: "v2.3"
status: "revised"
category: "MicroFunction framework"
source_docx: "AIRA_10C_MicroFunction_Sequence_Diagrams_and_Mermaid_Reference_v2.3_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 10-microfunction-framework
  - revised
  - aira-10c
---



# MicroFunction Sequence Diagrams and Mermaid Reference



AIRA
MicroFunction Sequence Diagrams and Mermaid Reference
Runtime Flow Verification | Sequence Evidence | Cross-Cutting Capability Coverage | Architecture Fitness Diagrams
v2.3 Revised - Parent v3.4 / 10A v2.4 / 10B v2.3 Alignment Update
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-010C |
| Document Title | AIRA MicroFunction Sequence Diagrams and Mermaid Reference |
| Version | v2.3 Revised - Cross-Cutting Capability, Diagram Governance, and Parent Alignment Update |
| Source Document Reviewed | AIRA_10C_MicroFunction_Sequence_Diagrams_and_Mermaid_Reference_v2_2_Review_and_Revised.docx |
| Supersedes | 10C-AIRA_MicroFunction_Sequence_Diagrams_and_Mermaid_Reference_v2.1_Aligned.docx and the v2.2 candidate, upon approval |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Architecture Review Board / CAB / Engineering Team Review |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; DBA; Platform Engineering; AI Engineering; SRE / Operations; Internal Audit |
| Parent Standard | AIRA-DOC-010 MicroFunction Framework v3.4 Revised |
| Direct Companions | AIRA-DOC-010A MicroFunction Design and Development Guide v2.4 Revised; AIRA-DOC-010B MicroFunction Framework Implementation Standard v2.3 Revised |
| Review Cadence | Quarterly; unscheduled on material MicroFunction, DevSecOps, API, database, security, AI, workflow, observability, runtime-toggle, or System Builder change |

Mandatory Practice Statement. AIRA sequence diagrams are governed architecture evidence. A diagram is acceptable only when its Mermaid source, rendered image, step order, runtime envelope, policy decision path, evidence envelope, error path, replay and compensation path, DevSecOps gate, observability signal, and human approval boundary remain aligned with AIRA-DOC-010 v3.4, 10A v2.4, 10B v2.3, AVCI, and the Enterprise Design Principles.

# Static Table of Contents

1. Executive Summary and v2.3 Update Verdict

2. Source Alignment, Corrections, and Precedence

3. Diagram Governance Model

4. Mandatory Diagram Metadata and Classification Controls

5. Mandatory Diagram Set and Applicability Matrix

6. Standard Step Sequence Reference

7. Copy-Ready Mermaid Source References

8. Review Gates, Validation Checklist, and Rejection Rules

9. Runtime Toggle and Performance-Sensitive Observability Rule

10. Evidence, RACI, Review Queue, and AVCI Summary

# 1. Executive Summary and v2.3 Update Verdict

Purpose. This v2.3 revision converts the uploaded v2.2 candidate into the active revised companion for MicroFunction diagram governance. It keeps Mermaid source as the editable authority and makes each diagram a verification artifact for runtime behavior, not an informal illustration.

Update verdict. The source is directionally strong and already covers mandatory sequence evidence, cross-cutting capability coverage, runtime toggles, DevSecOps, observability, eventing, resilience, security, and Auto-* loops. This revision corrects the parent/companion references, merges the cross-cutting coverage into the primary standard, and aligns the review queue with the completed 10 v3.4, 10A v2.4, and 10B v2.3 revisions.
| Area | v2.3 Treatment |
| --- | --- |
| Parent authority | Corrected from 10 v3.3 to AIRA-DOC-010 MicroFunction Framework v3.4 Revised. |
| Direct companions | Corrected to 10A v2.4 Revised and 10B v2.3 Revised. |
| Diagram role | Clarified as governed sequence evidence and architecture verification, not decorative documentation. |
| Cross-cutting controls | Integrated DevSecOps, API/eventing, observability, resilience, security, runtime toggles, and Auto-* candidate loops into required diagram coverage. |
| System Builder | May draft diagrams and metadata only; cannot approve, publish as canonical, or mutate runtime behavior. |
| Review queue | 10C is now completed; 10D Standard Function Catalog and Assembly Templates is next. |

# 2. Source Alignment, Corrections, and Precedence
| Source / Control | Required 10C v2.3 Alignment |
| --- | --- |
| 01A / 01 / 01B | Principles, AVCI, evidence, audit, traceability, classification, and improvement controls govern every diagram artifact. |
| 02 / 03 / 04 / 05 / 06 / 07 / 07B | Blueprint, developer behavior, technology baseline, information source authority, AI coding rules, skills/SBAC, and progressive autonomy set the implementation context. |
| 10 v3.4 | Parent authority for runtime assembly, reusable steps, cross-cutting capability coverage, governance envelope, and runtime evidence. |
| 10A v2.4 | Design-time procedure: configure first, reuse standard steps, code only approved STP-BUS gaps, and document design evidence. |
| 10B v2.3 | Implementation controls: runtime engine, repository/package boundaries, schema, execution envelope, OPA/SBAC, outbox, telemetry, tests, and CI/CD gates. |
| 10D / 10E | Catalog/templates and backend generation/runtime configuration must inherit this diagram vocabulary and metadata. |
| 11 / 15 / 16 / 17 / 19 / 20 / 31A / 42 / 43 | DevSecOps, API/event contracts, Flyway, security, GitNexus, CI evidence, observability, AI governance, and continuous improvement remain controlling companions. |

Precedence rule. If a diagram conflicts with AIRA-DOC-010 v3.4, 10A v2.4, 10B v2.3, 01A, AVCI, security, database, API, or DevSecOps standards, the stricter standard governs. The conflict must be logged as an AVCI reconciliation item and tracked through the canonical register / 00D path.

# 3. Diagram Governance Model

The source Mermaid file is the authoritative editable artifact. Rendered images, PDFs, and Obsidian/LLM Wiki projections are derivative. AIRA must never approve a hand-edited image that does not have updated source, rendering evidence, and PR/MR review.
| Rule | Mandatory Treatment |
| --- | --- |
| Mermaid source authority | Store diagram source in Git or approved Tier-0 knowledge source. Rendered PNG/SVG/PDF images are derivative. |
| No hand-edited image authority | Changing a picture without changing Mermaid source is rejected. |
| Version and classification | Every diagram has diagram_id, version, owner, classification, source_ref, transaction_code, and evidence_ref. |
| Review path | Diagram changes require PR/MR, CODEOWNERS where applicable, AVCI summary, affected-document impact review, and rendered visual QA. |
| System Builder use | System Builder may generate drafts and metadata but cannot approve, publish, activate, or override canonical controls. |
| Obsidian / LLM Wiki | Only curated projections are allowed. Retrieval eligibility requires source hash, classification, freshness, and conflict checks. |

# 4. Mandatory Diagram Metadata and Classification Controls
| Metadata Field | Required Meaning |
| --- | --- |
| diagram_id | Unique stable identifier, for example MF-SEQ-STANDARD-SYNC-v2.3. |
| transaction_code | MicroFunction transaction or reusable pattern represented. |
| owner | Named accountable role or office. |
| classification | Public, Internal, Confidential, or Restricted plus handling and retention rule. |
| source_ref | Git path, OpenKM path, Obsidian projection path, document reference, and source hash. |
| related_contracts | OpenAPI, AsyncAPI, Avro/JSON schema, CloudEvents, OPA, Flyway, workflow, or evidence schema references. |
| edp_impact | EDP-01 through EDP-20 controls addressed by the diagram. |
| verification_evidence | Tests, CI run, policy decision, trace, audit event, GitNexus result, rendered-output check, and reviewer reference. |
| runtime_toggle_posture | Allowed diagnostic sampling/verbosity and the non-disableable audit/security/policy/idempotency/outbox/evidence signals. |

# 5. Mandatory Diagram Set and Applicability Matrix
| Diagram ID | Required When | Minimum Coverage |
| --- | --- | --- |
| DIA-01 Standard Synchronous Transaction | Every MicroFunction transaction design | Receive, correlate, resolve actor, classify, validate, authorize, idempotency, concurrency, config, business, persist, outbox, audit, observe, respond. |
| DIA-02 API and Contract Boundary | REST/OpenAPI or external API entry | Thin controller, OpenAPI contract, application port, MicroFunction coordinator, safe response, policy and evidence. |
| DIA-03 Event-Driven and Outbox | Kafka/AsyncAPI/eventing transaction | CloudEvents, Avro/schema registry, outbox, publisher, topic, consumer, idempotency, DLQ, replay. |
| DIA-04 Observability and Evidence | Every critical transaction | Log4j2, OTel, Sentry, Loki, Tempo, Grafana, audit, evidence, alerting, trace reconstruction. |
| DIA-05 Concurrency and Heavy Transaction | Mutating, high-volume, batch, scheduled, financial-like, or retryable flows | Idempotency reservation, locks, bulkhead, rate limit, backpressure, retry safety, compensation, load evidence. |
| DIA-06 DevSecOps and Evidence Pack | Every PR/MR and release-bound change | Build, tests, scans, policy checks, architecture fitness, GitNexus, evidence pack, approval, promotion gate. |
| DIA-07 Security, OPA/SBAC, and Authenticated DAST | Protected API, admin action, high-risk capability | Identity, classification, OPA/SBAC, abuse cases, secure API checks, secret hygiene, authenticated DAST, remediation evidence. |
| DIA-08 Auto-Heal / Auto-Learn / Auto-Improve | Operational issue, recurring defect, or improvement candidate | Detection, evidence retrieval, candidate proposal, tests, policy check, human approval, PR/MR, monitoring. |
| DIA-09 AI/RAG/Tool Action | AI-assisted or agentic step | LiteLLM route, guardrails, retrieval eligibility, Harness/tool gateway, SBAC/OPA, approval, audit, rollback. |
| DIA-10 Runtime Toggles | Logging/sampling/diagnostic controls | Allowed diagnostics and non-disableable audit/security/policy/idempotency/outbox/critical error evidence. |

## 5.1 EDP-01 to EDP-20 Diagram Enforcement Map
| EDP | Diagram Enforcement |
| --- | --- |
| EDP-01 SOLID | Each participant and step has one responsibility and stable interface. |
| EDP-02 Clean Architecture | Domain/use-case logic is not shown depending on UI, DB clients, queues, model providers, or frameworks. |
| EDP-03 DDD | Bounded context, ownership, schema boundary, API/event, and runbook responsibility are explicit. |
| EDP-04 Ports/Adapters | External systems, DB, queue, model, tool, and provider calls pass through ports/adapters. |
| EDP-05 DRY/KISS/YAGNI | Standard concerns are reused; speculative duplicate steps are rejected. |
| EDP-06 Idempotency | Retries, replays, callbacks, and tool actions show idempotency and duplicate handling. |
| EDP-07 Determinism | Diagram, tests, and runtime assembly are reproducible from approved source. |
| EDP-08 Fail-safe | Missing identity, policy, guardrail, audit, evidence, or config routes to denial or safe stop. |
| EDP-09 Human-in-loop | High-impact or low-confidence action includes named approval/handoff. |
| EDP-10 Least privilege | Actors, services, agents, and tools have bounded skill/data/environment scope. |
| EDP-11 SoD | Maker/checker/approver/deployer/operator/auditor roles remain separated. |
| EDP-12 Observability | Logs, metrics, traces, audit, error monitoring, dashboards, alerts, and evidence references are visible. |
| EDP-13 Policy as code | OPA/Rego or approved policy artifacts are visible for authorization/routing/guardrails/data handling. |
| EDP-14 Testability | Unit, contract, policy, architecture, replay, and E2E validation points are visible. |
| EDP-15 Secure by design | Threat controls, secret hygiene, classification, tenant isolation, and secure defaults are explicit. |
| EDP-16 Resilience | Timeouts, retries, circuit breakers, bulkheads, fallback, DLQ, compensation, and recovery are shown. |
| EDP-17 Fitness | CI checks, package-boundary checks, contract checks, policy checks, and evidence gates are visible. |
| EDP-18 Progressive autonomy | Automation advances only with evidence, trust, skill, guardrail, risk tier, and rollback controls. |
| EDP-19 Reversibility | Rollback, forward-fix, compensation, feature disablement, rebuild, or safe deactivation path is shown. |
| EDP-20 AVCI | Diagram source, rendered image, transaction, evidence record, and improvement proposal remain AVCI-complete. |

# 6. Standard Step Sequence Reference
| Order | Step Prefix | Purpose |
| --- | --- | --- |
| 1 | STP-RCV | Receive approved REST, Kafka, webhook, batch, file, UI, workflow, or scheduled trigger. |
| 2 | STP-COR | Create or propagate trace_id, request_id, correlation_id, causation_id, span_id, and evidence_ref. |
| 3 | STP-SES | Resolve human, service, AI agent, tenant, branch, role, skill, channel, and classification context. |
| 4 | STP-RATE | Apply quota, rate limit, AI budget, API throttling, abuse threshold, and backpressure control. |
| 5 | STP-SEC / STP-CLS | Authenticate, authorize, classify, evaluate RBAC/ABAC/SBAC/OPA, and enforce model-route eligibility. |
| 6 | STP-PRS / STP-NRM / STP-VAL | Parse, normalize, sanitize, validate schemas, validate business rules, and enforce API/event contracts. |
| 7 | STP-IDP / STP-CON | Reserve idempotency, check replay, prevent duplicate effects, and apply concurrency guard. |
| 8 | STP-CFG / STP-CAC | Resolve runtime configuration, feature flags, policy versions, cache source, and parameter sets. |
| 9 | STP-BUS / STP-RUL | Execute bounded business MicroFunction, rule, DMN decision, or approved adapter call. |
| 10 | STP-PER / STP-OUT / STP-EVT | Persist state, append history, write outbox, emit CloudEvents/Avro event through approved publisher. |
| 11 | STP-AUD / STP-OBS | Write audit, evidence, traces, metrics, logs, Sentry context, Loki record, Tempo trace, Grafana fields. |
| 12 | STP-ERR / STP-CMP / STP-DLQ / STP-RSP | Classify error, retry safely, compensate, route DLQ, support replay, escalate approval, return safe response. |

# 7. Copy-Ready Mermaid Source References

The snippets below are governed source templates. Production diagrams may expand participants and labels but must not remove mandatory control points. Rendered images must be regenerated from these sources before final publication.

## DIA-01 Standard Synchronous MicroFunction Transaction

sequenceDiagram
    autonumber
    participant C as Channel or Adapter
    participant G as API Gateway
    participant M as MicroFunction Coordinator
    participant P as OPA/SBAC Policy
    participant R as Runtime Config Registry
    participant B as STP-BUS Function
    participant D as PostgreSQL/Flyway Schema
    participant O as Outbox and Event Publisher
    participant E as Audit/Evidence Store
    participant T as Observability Stack
    C->>G: Request with idempotency key
    G->>M: STP-RCV and STP-COR
    M->>P: STP-SEC / STP-CLS decision
    P-->>M: allow, deny, approval, or step-up
    M->>R: STP-CFG resolve active definition
    M->>M: STP-VAL, STP-IDP, STP-CON
    M->>B: Execute bounded business function
    B->>D: Persist state through port/adapter
    M->>O: Write transactional outbox event
    M->>E: Audit and evidence record
    M->>T: Traces, metrics, logs, error context
    M-->>G: Safe response with trace_id and evidence_ref

## DIA-03 Event-Driven Outbox, Kafka, DLQ, and Replay

flowchart LR
    A[STP-PER Persist business state] --> B[STP-OUT Write transactional outbox]
    B --> C[Outbox Publisher]
    C --> D[CloudEvents Envelope]
    D --> E[Avro or JSON Schema Validation]
    E --> F[Kafka Topic]
    F --> G[Idempotent Consumer]
    G --> H{Process Result}
    H -->|Success| I[Consumer Offset / Evidence]
    H -->|Retryable Failure| J[Retry with Backoff and Limit]
    J --> G
    H -->|Non-retryable| K[DLQ Topic]
    K --> L[Replay Review Queue]
    L --> M[Human Approval / Remediation Evidence]
    M --> N[Controlled Replay]
    N --> G

## DIA-04 Observability, Audit, and Trace Reconstruction

flowchart TD
    A[MicroFunction Execution Envelope] --> B[OpenTelemetry Trace]
    A --> C[OpenTelemetry Metrics]
    A --> D[Structured Log4j2 Event]
    A --> E[Audit Event]
    A --> F[Evidence Record]
    D --> G[Loki Log Store]
    B --> H[Tempo Trace Store]
    C --> I[Prometheus / Metrics Store]
    A --> J[Sentry Error Monitoring]
    G --> K[Grafana Dashboard]
    H --> K
    I --> K
    J --> K
    E --> L[Audit / OpenKM Evidence]
    F --> L
    K --> M[Trace Reconstruction using trace_id, request_id, run_id, evidence_ref]

## DIA-05 Concurrency, Heavy Transaction, and Resilience Lab

flowchart TD
    A[Incoming concurrent requests] --> B[Rate Limit and Quota]
    B --> C[Idempotency Reservation]
    C --> D{Duplicate or Replay?}
    D -->|Existing Success| E[Return prior safe response]
    D -->|New| F[Concurrency Guard]
    F --> G[Bulkhead / Circuit Breaker]
    G --> H[Bounded Business Function]
    H --> I{Outcome}
    I -->|Success| J[Persist, Outbox, Audit]
    I -->|Retryable Failure| K[Retry with jitter and limit]
    K --> H
    I -->|Permanent Failure| L[Compensation / DLQ / Human Escalation]
    J --> M[Load Test and Evidence Pack]
    L --> M

## DIA-06 DevSecOps Pipeline, GitNexus, and Evidence Pack

flowchart LR
    A[Issue / ADR / TDL] --> B[Branch and Diagram Update]
    B --> C[Unit, Contract, OPA, Architecture Tests]
    C --> D[SAST, SCA, Secret Scan, Authenticated DAST]
    D --> E[GitNexus Read-Only Impact Analysis]
    E --> F[Evidence Pack]
    F --> G[PR/MR Maker-Checker Review]
    G --> H{ARB/CAB or Owner Approval}
    H -->|Approved| I[Promote through CI/CD]
    H -->|Rejected| J[Remediate and Re-test]
    I --> K[Runtime Monitoring and Improvement Backlog]
    J --> C

## DIA-08 Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop

flowchart TD
    A[Issue Detection: alert, trace, Sentry, CI failure, DAST finding] --> B[Evidence Retrieval]
    B --> C[Root Cause and Impact Analysis]
    C --> D[Candidate Fix or Learning Proposal]
    D --> E[Policy, Security, Architecture, and Test Plan]
    E --> F[Human Maker-Checker Approval]
    F -->|Approved| G[Create PR/MR or Change Proposal]
    F -->|Rejected| H[Backlog or Close with Reason]
    G --> I[Tests, Scans, GitNexus, Evidence Pack]
    I --> J[Controlled Promotion]
    J --> K[Post-Change Monitoring]
    K --> L[Knowledge Update after Review]

# 8. Review Gates, Validation Checklist, and Rejection Rules
| Gate | Pass Condition |
| --- | --- |
| Design gate | Diagram has owner, transaction code, step sequence, bounded context, classification, and related standards. |
| Architecture gate | No direct database, Kafka, Redis, model-provider, workflow-engine, or external-system call from business logic. |
| Security gate | Identity, OPA/SBAC, classification, secrets hygiene, safe response, abuse-case, and authenticated DAST controls are visible where required. |
| API/event gate | OpenAPI/AsyncAPI/Avro/CloudEvents contracts, outbox, schema evolution, idempotent consumer, DLQ, and replay are shown where applicable. |
| Observability gate | Log4j2, OTel, Sentry, Loki, Tempo, Grafana, audit, evidence, alerting, and trace reconstruction fields are shown. |
| Resilience gate | Timeout, retry, circuit breaker, bulkhead, concurrency guard, compensation, recovery, and safe degradation are visible. |
| DevSecOps gate | Tests, scans, GitNexus, evidence pack, maker-checker, and promotion controls are visible. |
| Improvability gate | Auto-Heal/Learn/Improve loop remains proposal-driven, test-backed, policy-checked, and human-approved before mutation. |
| Checklist ID | Pass Condition |
| --- | --- |
| VC-10C-001 | Diagram source has metadata, owner, version, classification, and evidence reference. |
| VC-10C-002 | Diagram matches 10 v3.4, 10A v2.4, 10B v2.3, and 10D catalog rules. |
| VC-10C-003 | All applicable cross-cutting capabilities are shown or formally marked not applicable with reason, owner, and reviewer. |
| VC-10C-004 | Security, OPA/SBAC, classification, secrets, abuse-case, and authenticated DAST paths are visible where required. |
| VC-10C-005 | Outbox, Kafka, Avro/JSON Schema, CloudEvents, idempotent consumer, DLQ, and replay are shown for eventing flows. |
| VC-10C-006 | Log4j2, OTel, Sentry, Loki, Tempo, Grafana, audit, evidence, dashboard, and alerting paths are shown for critical flows. |
| VC-10C-007 | Concurrency, idempotency, retry, duplicate-safety, compensation, and heavy-load behavior are shown for mutating or high-volume flows. |
| VC-10C-008 | Auto-* diagrams remain candidate-proposal flows with tests, evidence, policy checks, and human approval. |
| VC-10C-009 | Mermaid source renders successfully and rendered diagrams are regenerated before publication. |
| VC-10C-010 | PR/MR evidence includes diagram impact, affected standards, tests/scans, GitNexus result, reviewer, and improvement backlog. |
| Anti-Pattern | Required Correction |
| --- | --- |
| Happy-path-only diagram | Reject; add policy denial, error path, retry, compensation, evidence, and human approval. |
| Business logic calls infrastructure directly | Reject; route through ports/adapters and the runtime envelope. |
| Diagram image edited without source | Reject; update Mermaid source and regenerate rendered artifact. |
| Observability omitted for performance | Reject unless approved sampling/toggle plan preserves mandatory evidence. |
| AI improvement loop mutates production | Reject; Auto-* must remain proposal-driven and human-approved. |
| Event flow without schema and DLQ | Reject; add schema governance, idempotent consumer, DLQ, and replay path. |
| Policy hidden in application code | Reject; OPA/SBAC decision must be explicit and evidence-producing. |

# 9. Runtime Toggle and Performance-Sensitive Observability Rule

Non-disableable evidence rule. Runtime toggles may reduce logging verbosity, trace sampling, dashboard granularity, or diagnostic payload size when performance requires it. They must not disable mandatory audit events, security logs, OPA/SBAC policy decisions, classification labels, idempotency records, outbox records, DLQ/replay records, critical error evidence, or legally/audit-required telemetry.
| Toggle Type | Allowed? | Required Control |
| --- | --- | --- |
| Log verbosity | Allowed | Preserve security, audit, error, and evidence logs; record toggle event and expiry. |
| Trace sampling | Allowed with control | Critical and Restricted flows require minimum sampling or always-on trace markers; record sampling policy. |
| Metrics cardinality | Allowed | Control high-cardinality labels; SLO and error metrics remain mandatory. |
| Sentry event sampling | Allowed with risk control | Critical security and production-impacting errors must not be suppressed. |
| Audit/policy/idempotency/outbox evidence | Not allowed | Reject toggle unless replaced by an approved stronger evidence mechanism. |

# 10. Evidence, RACI, Review Queue, and AVCI Summary
| Evidence Class | Required Evidence |
| --- | --- |
| Diagram source evidence | Mermaid source path, source hash, version, owner, classification, affected transaction, and change reason. |
| Rendered evidence | Rendered PNG/SVG/PDF output, generation timestamp, and verification that rendered image matches source. |
| Architecture evidence | Boundary review, EDP impact, ADR/TDL or waiver where applicable, and fitness-function pass result. |
| Implementation evidence | OpenAPI/AsyncAPI/schema/policy references, tests, CI run, GitNexus read-only impact, and PR/MR summary. |
| Runtime evidence | trace_id, audit event, evidence_ref, policy decision, outbox event, logs, metrics, and dashboard link where applicable. |
| Improvement evidence | Issue/incident/finding, candidate proposal, tests, human approval, remediation proof, monitoring, and knowledge update. |
| Activity | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Maintain 10C standard | Enterprise Architecture / Platform Engineering | Solutions Architecture Office / IT Head | DevSecOps, Security, QA/SDET, SRE | Engineering, Internal Audit |
| Create/update Mermaid source | Developer / Architect / System Builder operator | Document or transaction owner | QA/SDET, Security, DBA, SRE | Reviewers |
| Validate diagram against runtime implementation | QA/SDET / DevSecOps | Software Development Lead | Architecture, Security, Platform Engineering | ARB/CAB where applicable |
| Approve production-impacting diagram change | Change Owner | CAB / ARB where applicable | Security, SRE, DBA, QA | Affected teams |
| Publish Obsidian/LLM Wiki projection | Knowledge Steward | Knowledge Governance Owner | Architecture, Security | Developers and AI users |
| Seq | File | Recommended Version | Status | Next Step |
| --- | --- | --- | --- | --- |
| 13 | 10-AIRA_MicroFunction_Framework | v3.4 Revised | Completed | Parent standard for MicroFunction suite. |
| 14 | 10A-AIRA_MicroFunction_Design_and_Development_Guide | v2.4 Revised | Completed | Design companion for 10B/10C/10D. |
| 15 | 10B-AIRA_MicroFunction_Framework_Implementation_Standard | v2.3 Revised | Completed | Implementation companion for sequence and catalog alignment. |
| 16 | 10C-AIRA_MicroFunction_Sequence_Diagrams_and_Mermaid_Reference | v2.3 Revised | Completed | Use as diagram governance standard after approval. |
| 17 | 10D-AIRA_MicroFunction_Standard_Function_Catalog_and_Assembly_Templates | v2.2 Revised | Next for Review | Update catalog entries, assembly templates, mandatory cross-cutting columns, and publish validators. |
| Version | Date | Summary |
| --- | --- | --- |
| v2.1 | 2026-05-21 | Pack alignment, Java 25 diagram governance update, rendered diagram and copy-ready Mermaid edition. |
| v2.2 candidate | 2026-06-16 | Cross-cutting capability and diagram governance update aligned with 10 v3.3, 10A v2.3, and 10B v2.2. |
| v2.3 Revised | 2026-06-18 | Corrects parent and companion references to 10 v3.4, 10A v2.4, and 10B v2.3; integrates cross-cutting coverage into the core diagram standard; updates review queue to 10D. |
| AVCI Property | Evidence in 10C v2.3 Revised |
| --- | --- |
| Attributable | Defines diagram owner, source, version, transaction code, classification, related standards, and PR/MR accountability. |
| Verifiable | Requires Mermaid source/render consistency, validation checklist, CI/test/security/evidence gates, and trace reconstruction evidence. |
| Classifiable | Requires diagram and source classification, safe telemetry representation, secrets hygiene, and model-route/data-handling controls. |
| Improvable | Provides controlled diagram revision path, Auto-Heal/Learn/Improve candidate loop, review queue update, and knowledge update evidence. |

Final Diagram Rule: A diagram that looks correct but hides policy, evidence, error, replay, compensation, observability, or human-approval behavior is not AIRA-ready.

