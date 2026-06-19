---
title: "MicroFunction Design and Development Guide"
doc_id: "AIRA-10A"
version: "v2.4"
status: "revised"
category: "MicroFunction framework"
source_docx: "AIRA_10A_MicroFunction_Design_and_Development_Guide_v2.4_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 10-microfunction-framework
  - revised
  - aira-10a
---



# MicroFunction Design and Development Guide



AIRA

AI-Native Enterprise Platform

MicroFunction Design and Development Guide

Configuration-First Design | STP-BUS Isolation | Runtime Evidence | Cross-Cutting Capability Coverage

Version v2.4 Revised | June 2026

Draft for Architecture Review Board / CAB / Engineering Team Review
| Mandatory Practice Statement
AIRA MicroFunction design starts with configuration, standard step reuse, policy, evidence, and reversibility. New code is allowed only when no approved standard function, configuration, rule, DMN decision, OPA policy, adapter, or reusable service can satisfy the requirement. Every business MicroFunction must remain bounded, testable, dependency-inverted, observable, secure, reversible, rollbackable, and AVCI-complete before activation. |
| --- |

# Document Control
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-010A |
| Document Title | AIRA MicroFunction Design and Development Guide |
| Version | v2.4 Revised - Parent Framework v3.4 and Cross-Cutting Capability Alignment Update |
| Source Reviewed | AIRA_10A_MicroFunction_Design_and_Development_Guide_v2_3_Cross_Cutting_Capability_Update.docx |
| Supersedes | 10A-AIRA_MicroFunction_Design_and_Development_Guide_v2.1_Aligned.docx and v2.3 candidate/addendum, upon approval |
| Parent Standard | AIRA-DOC-010 MicroFunction Framework v3.4 Revised |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for ARB / CAB / Engineering Team Review |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; DBA; Platform Engineering; AI Engineering; SRE / Operations; Internal Audit |
| Primary Audience | Solutions Architects; Developers; QA/SDET; DevSecOps; DBA; Security; Platform Engineering; AI Engineering; System Builder operators; Internal Audit |
| Current Foundation References | 01A v1.2; 01 AVCI v3.2; 01B v1.2; 02 v5.2; 03 v4.2; 04 v9.2; 05 v4.2; 06 v3.2; 07 v3.2; 07B v1.2; 10 v3.4. Documents 08, 08A, and 09 remain inherited from the active baseline until separately revised. |

# 1. Executive Summary

This v2.4 revision converts the uploaded v2.3 cross-cutting capability update into a cleaner, developer-executable companion guide under AIRA-DOC-010 MicroFunction Framework v3.4 Revised. It preserves the original intent: configure first, reuse standard functions, code only the bounded business gap, and prove every change through evidence.

The key correction is authority alignment. 10A must not redefine the parent MicroFunction Framework. It translates parent controls into a design procedure, design record, checklist, evidence pack, and System Builder-ready workflow. The uploaded v2.3 file already added strong cross-cutting controls; this revision embeds those controls into the main design lifecycle instead of leaving them as a detached addendum.
| v2.4 Outcome | Required Result |
| --- | --- |
| Cleaner developer path | Configure first, then rule/DMN/OPA, then adapter reuse, then new adapter, and only then STP-BUS code when justified. |
| Parent alignment | All 10A design rules inherit 10 v3.4 and cannot weaken the parent framework. |
| Cross-cutting completeness | DevSecOps, contracts/events, observability, resilience, security, and improvement-loop coverage are mandatory applicability decisions. |
| System Builder safe generation | AI/System Builder may draft candidate artifacts only; activation, promotion, and production-impacting behavior remain human-governed. |
| Runtime evidence by design | Every design prepares the runtime evidence envelope before implementation and activation. |

# 2. Review Findings and v2.4 Corrections
| Finding Type | v2.4 Treatment |
| --- | --- |
| Retain | Configuration-first philosophy, standard function reuse, STP-BUS isolation, SOLID enforcement, AVCI evidence, and System Builder draft-only boundaries remain correct. |
| Correct | Parent reference is updated from MicroFunction Framework v3.2 candidate to AIRA-DOC-010 v3.4 Revised. Foundation references are corrected to the recently revised 01A, 01, 01B, 02, 03, 04, 05, 06, 07, and 07B artifacts. |
| Clarify | No-code / low-code / adapter / STP-BUS decision path is now the governing developer sequence. |
| Strengthen | Cross-cutting controls are elevated to mandatory design applicability decisions with explicit evidence requirements. |
| Simplify | Theory is converted into design checks, direct-call prohibitions, validation gates, and PR/MR evidence expectations. |
| Reconcile | The review queue is corrected: 10A is completed by this v2.4 revision and the next document is 10B Implementation Standard. |

# 3. Authority and Precedence
| Level | Authority | 10A Interpretation |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance | Final authority for material architecture, security, production, and waiver decisions. |
| L1 | 01A, 01, 01B, 02, 03, 04, 05, 06, 07, 07B | Foundation principles, evidence, architecture, developer behavior, technology, knowledge, AI rules, skills, and transformation direction. |
| L2 | 10 MicroFunction Framework v3.4 | Parent authority for runtime assembly, function categories, extension rules, configuration governance, evidence, and quality gates. |
| L3 | This 10A Guide | Design and development procedure. It operationalizes parent controls and must not become a competing authority. |
| L4 | 10B, 10C, 10D, 10E | Implementation, diagram, catalog, template, backend-generation, and runtime-configuration companions. |
| L5 | ADRs, TDLs, waivers, tickets, PR/MR evidence, runtime evidence | Implementation proof that cannot weaken higher authority standards. |

# 4. Design Operating Model

MicroFunction design is a governance activity before it is a coding activity. A design must identify the requirement source, owner, bounded context, data classification, trigger, actor, risk tier, standard-step reuse options, contracts, policies, tests, evidence, observability, rollback path, and improvement path.

## 4.1 Configuration-First Decision Path
| Decision Path | Use When | Required Evidence |
| --- | --- | --- |
| No-code configuration | Behavior can be expressed through approved step order, parameters, templates, feature flags, policy binding, or runtime configuration. | Configuration diff, validator result, tests, affected transaction list, rollback/safe-disable path. |
| Low-code rule / DMN / OPA | Behavior is a decision, threshold, route, classification, eligibility rule, authorization rule, or approval condition. | Rule/DMN/OPA change, test cases, policy decision evidence, owner approval. |
| Adapter reuse | A required dependency already has an approved port and adapter. | Contract reference, adapter version, timeout/retry profile, integration test. |
| New adapter | A new external capability is required and cannot be served by existing adapters. | ADR/TDL assessment, contract-first design, security review, secrets path, observability, test doubles. |
| New STP-BUS code | A narrow business capability cannot be satisfied by configuration, rules, policy, DMN, templates, or adapters. | MicroFunction Design Record, catalog registration, tests, architecture fitness, rollback/compensation plan. |

# 5. MicroFunction Design Record

Every new or materially changed MicroFunction must have a MicroFunction Design Record before implementation, System Builder generation, catalog registration, activation, or promotion.
| Design Record Field | Required Content |
| --- | --- |
| design_id | Unique design record identifier linked to ticket/intake, source reference, PR/MR, and evidence pack. |
| owner / reviewer | Named accountable owner and independent reviewer/checker. |
| bounded_context | Single owning bounded context. Cross-context writes require contract, event, workflow, or approved integration pattern. |
| transaction_code / step_code | Transaction code and STP-* step code following catalog naming rules. |
| classification / handling | Data classification, retention, redaction, retrieval eligibility, and telemetry handling requirements. |
| decision_path | No-code, low-code, adapter reuse, new adapter, or STP-BUS code-required decision with rationale. |
| contracts | OpenAPI, AsyncAPI, Avro/JSON Schema, CloudEvents, file/integration contract, and schema evolution posture as applicable. |
| policy / security | OPA/SBAC inputs, abuse cases, authenticated DAST need, secure API posture, secrets path, and safe response rules. |
| idempotency / resilience | Idempotency key, duplicate behavior, timeout, retry, lock strategy, outbox, DLQ, replay, compensation, and rollback. |
| observability | Log4j2 profile, OpenTelemetry spans, Sentry issue handling, Loki/Tempo/Grafana references, audit events, redaction tests. |
| tests / evidence | Unit, component, policy, contract, failure-path, architecture fitness, security, observability, concurrency, load, DAST, regression. |
| improvement path | Known limitations, Auto-Heal/Learn/Improve candidate eligibility, backlog link, and review cadence. |

# 6. Standard Assembly Pattern

The default transaction sequence must preserve standard controls before business execution. Conditional omission is allowed only when the Design Record marks the control as Not Applicable with reason, owner, and reviewer acceptance. Mandatory security, audit, classification, idempotency, outbox, and evidence controls may not be disabled by ordinary configuration.
| Order | Step Family | Design Requirement |
| --- | --- | --- |
| 1 | Receive and Correlate | Accept approved trigger; create or propagate request_id, correlation_id, trace_id, causation_id, and evidence_ref. |
| 2 | Resolve Actor and Context | Resolve human/service/agent, tenant, channel, branch/unit, role, skill, classification context, and trust tier. |
| 3 | Rate Limit and Guard | Apply quota, abuse, throttling, AI budget, and preliminary guardrail checks where applicable. |
| 4 | Authorize and Classify | Evaluate RBAC/ABAC/SBAC, OPA policy, classification ceiling, data scope, and model/tool eligibility before protected action. |
| 5 | Validate and Normalize | Validate schema, domain preconditions, idempotency key, canonical input normalization, and deterministic constraints. |
| 6 | Execute STP-BUS / Rule / Adapter | Execute only bounded business logic, rule, DMN, OPA, approved adapter, or standard function under the runtime envelope. |
| 7 | Persist and Publish | Persist through domain ports/repositories; publish through transactional outbox, event adapter, schema-managed CloudEvents/Kafka path. |
| 8 | Audit, Observe, and Evidence | Emit audit, trace, metric, log, policy decision, step result, outbox, error-monitoring, and evidence records with redaction. |
| 9 | Respond Safely | Return stable response shape, safe error code, user-safe message, retry/compensation state, and correlation reference. |

# 7. Business MicroFunction Extension Rules

A business MicroFunction is allowed only when it performs one narrow business operation within one bounded context. It must not become a mini-service, controller, repository, workflow engine, policy engine, AI prompt authority, or integration gateway.
| Rule | Mandatory Treatment |
| --- | --- |
| One bounded context | Exactly one owning bounded context and named owner. Cross-context writes are prohibited without contract, event, workflow, or approved integration. |
| Typed input/output | Consumes typed input and returns typed output through the MicroFunction contract. Raw maps or god-context dependencies are prohibited unless formally approved. |
| No direct infrastructure | No direct SQL, Kafka, Redis, OpenKM, Keycloak, Flowable, Temporal, model-provider SDK, secret store, filesystem, or external API calls from STP-BUS code. |
| Ports and adapters | Business logic calls domain/application ports only. Infrastructure adapters implement details outside the business function. |
| Idempotent side effects | Mutating behavior declares idempotency key, replay behavior, duplicate response, transaction boundary, and compensation posture. |
| Safe errors | Errors map to stable safe error codes, evidence references, severity, recovery path, and redacted responses. |
| Complete tests | Success, invalid input, authorization denial, downstream failure, retry/replay, boundary cases, and compensation tests are required as applicable. |

# 8. Cross-Cutting Capability Coverage Matrix

A MicroFunction transaction is not complete merely because the business step works. It is complete only when all applicable cross-cutting steps, controls, contracts, policies, observability signals, tests, evidence records, and rollback or compensation paths are defined, implemented, validated, and reviewable.
| Capability Area | Mandatory Design Treatment | Minimum Evidence |
| --- | --- | --- |
| DevSecOps, Security Gates, Evidence Pack, GitNexus | Repository controls, CODEOWNERS, CI/CD, SAST, SCA, secret scan, policy checks, architecture fitness, evidence pack, and GitNexus read-only impact analysis where available. | Build/test reports, scan reports, policy decisions, fitness results, GitNexus summary, PR/MR AVCI summary, approval, rollback. |
| OpenAPI, AsyncAPI, Kafka, Avro, CloudEvents, Outbox, Schema Evolution, DLQ, Replay | Boundary interactions are contract-first. APIs use OpenAPI; events use AsyncAPI, CloudEvents metadata, topic governance, schema registry, outbox, idempotent consumers, DLQ, replay controls. | Contract lint, compatibility result, schema approval, topic/consumer evidence, outbox records, DLQ test, replay test, event trace. |
| Observability: Log4j2, OpenTelemetry, Sentry, Loki, Tempo, Grafana | Critical steps emit classification-safe logs, traces, metrics, audit, error-monitoring, dashboards, alerts, and trace-reconstruction signals. | Trace/span IDs, Log4j2 config, OTel trace, Sentry issue, Loki query, Tempo trace, Grafana panel, alert rule, redaction test. |
| Concurrency, Heavy Transaction, Idempotency, Outbox, Resilience Lab | State-changing transactions are retry-safe, duplicate-safe, concurrency-safe, load-aware, and failure-aware with explicit locks, idempotency, timeout, retry, circuit breaker, bulkhead, compensation, DLQ. | Concurrency test, load test, idempotency test, retry/replay test, outbox delivery test, failure-injection, compensation evidence. |
| Auto-Heal, Auto-Learn, Auto-Improve Candidate Loop | Evidence may trigger issue detection, RCA, candidate fix, candidate learning, test proposal, prompt improvement, or backlog proposal. Automation remains advisory or draft-only unless a governed action tier permits bounded action. | Issue record, evidence bundle, candidate proposal, test impact, human checker, OPA/SBAC decision, risk tier, rollback/safe-disable, backlog. |
| Security, Abuse Cases, Authenticated DAST, Secure APIs, Secrets Hygiene | Design includes threat/abuse coverage, secure API patterns, OPA/SBAC expansion, classification handling, auth context, secret-safe execution, authenticated DAST where applicable, and remediation evidence. | Threat/abuse checklist, OPA tests, authenticated DAST report, ASVS evidence, secret scan, remediation ticket, retest result, waiver if any. |

# 9. Expanded Step Prefix Treatment
| Step Prefix | Purpose | Applicability | Representative Controls |
| --- | --- | --- | --- |
| STP-DEVSEC-* | DevSecOps and evidence gate steps | Conditional but mandatory for production-bound change generation and promotion. | CI/CD, scans, GitNexus, evidence pack, PR/MR AVCI. |
| STP-CONTRACT-* | API and event contract validation | Mandatory for boundary-crossing API, event, file, or integration. | OpenAPI, AsyncAPI, schema compatibility, registry, versioning. |
| STP-EVT-* | Eventing, outbox, consumer, DLQ, replay | Mandatory for event producers/consumers. | Kafka, Avro, CloudEvents, outbox, idempotent consumer, DLQ, replay. |
| STP-OBS-* | Telemetry, audit, error monitoring, dashboards, alerts | Mandatory for critical, security-sensitive, customer-impacting, or production-bound transactions. | Log4j2, OpenTelemetry, Sentry, Loki, Tempo, Grafana, trace reconstruction. |
| STP-RES-* | Resilience, concurrency, idempotency, load, recovery | Mandatory for mutating, retryable, long-running, high-volume, concurrent, or financial/operationally critical transactions. | Locks, retries, circuit breakers, bulkheads, idempotency, outbox, DLQ, compensation. |
| STP-AUTO-* | Auto-Heal/Learn/Improve candidate-loop steps | Conditional; never self-promoting. Mandatory where evidence triggers automation proposals. | Evidence retrieval, RCA, candidate proposal, tests, human approval. |
| STP-SEC-* | Security, policy, abuse cases, DAST, remediation | Mandatory for protected, security-sensitive, exposed, and privileged operations. | OPA/SBAC, authenticated DAST, secrets hygiene, secure APIs, remediation evidence. |

# 10. Data, Integration, Security, Workflow, and AI Design Rules
| Area | Mandatory Rule |
| --- | --- |
| Data | Use repositories and approved persistence ports. Database changes and runtime seed/config rows are Flyway-governed. Redis/Valkey and Caffeine accelerate only; they do not become authority. |
| API / Event Contracts | Use contract-first APIs/events. OpenAPI, AsyncAPI, Avro/JSON Schema, CloudEvents metadata, and stable error models must be versioned, tested, and evidence-linked. |
| Integration | No direct Kafka, OpenKM, email, SMS, workflow, payment, model, or third-party SDK calls from business functions. Use approved ports/adapters with timeouts, retries, redaction, and secrets control. |
| Security | Use Keycloak/OIDC, OPA/SBAC, classification, safe responses, and secrets references through approved controls. Do not log secrets, raw tokens, raw PII, or Restricted content. |
| Workflow | Temporal is for durable machine workflow and sagas. Flowable is for human approval, exception review, and governance tasks. MicroFunctions must not confuse these boundaries. |
| AI/RAG/Tool Actions | Route model access through LiteLLM or approved gateway, guardrails, Harness, SBAC, OPA, audit, evidence, and human approval where required. AI output is advisory unless reviewed and promoted. |
| Dynamic Workspace | Frontend components, widgets, templates, and AI panels are not business authority. UI actions invoke backend-governed MicroFunction capability bindings. |

# 11. Runtime Toggle and Performance Protection Rules

Verbose diagnostic logging, trace sampling, debug enrichments, selected dashboard panels, and low-value telemetry labels may be adjusted at runtime only through approved configuration, policy filtering, audit, expiry, and review.

Mandatory audit events, security logs, policy decisions, classification labels, idempotency records, outbox records, model-route decisions, guardrail results, and critical error evidence must not be disabled by ordinary runtime toggles.

Runtime toggle changes must pass OPA/SBAC, be attributable to a human or approved service identity, carry classification, and include rollback or safe-disable instructions.

When telemetry is reduced for performance, trace reconstruction must still remain possible through correlation IDs, audit records, evidence references, and sampled traces.

# 12. Error Handling, Compensation, and Safe Response Design
| Control | Design Requirement |
| --- | --- |
| Timeout | Every external, database, workflow, AI, or tool-action dependency declares timeout behavior and failure classification. |
| Retry | Retries are bounded, idempotent, observable, and aligned with workflow/runtime policy. Blind retries are prohibited. |
| Error classification | Errors map to stable safe error codes, severity, recovery path, policy impact, and evidence record. |
| Compensation | Mutating steps declare rollback, compensation, forward-fix, DLQ, human escalation, or accepted non-compensatable risk. |
| Safe response | Responses avoid sensitive details and include correlation/evidence reference for support and audit. |
| Escalation | High-risk, low-confidence, policy-denied, repeated failure, Restricted-data, or irreversible scenarios require human review as defined by policy. |

# 13. Testing and Architecture Fitness Functions
| Test / Check | Minimum Requirement | Blocks Merge When |
| --- | --- | --- |
| Unit tests | Verify core business behavior, edge cases, invalid input, deterministic outcomes. | Behavior is untested or non-deterministic. |
| Policy tests | Verify OPA/SBAC/classification decisions, denies, step-up, and human-review branches. | Protected action can execute without valid allow decision. |
| Contract tests | Verify input/output schemas, API/event compatibility, generated clients, and stable errors. | OpenAPI/AsyncAPI/schema/event contract drifts without versioning. |
| Failure-path tests | Verify timeout, retry, idempotency replay, compensation, DLQ, safe response, audit evidence. | Mutating or side-effecting path is unsafe under failure. |
| Architecture fitness | Reject direct controller business logic, direct DB/Kafka/Redis/model/provider calls, cross-context writes, dependency-direction violations. | Business logic bypasses ports/adapters or runtime envelope. |
| Observability tests | Verify trace_id/span_id, audit_event_id, policy_decision_id, evidence_ref, redaction, forbidden-field controls. | Trace reconstruction or redaction cannot be proven. |
| Security / DAST | Run SAST, SCA, secret scan, authenticated DAST where applicable, abuse-case tests, remediation retest. | High/critical finding lacks remediation, waiver, or risk acceptance. |
| Resilience Lab | Run concurrency, load, idempotency, replay, outbox, DLQ, retry, circuit breaker, and compensation tests where applicable. | Heavy transaction is not duplicate-safe, retry-safe, or recoverable. |

# 14. System Builder and AI-Assisted Generation Alignment

System Builder, Codex, Claude Code, Hermes Agent, or another approved AI assistant may generate candidate MicroFunction artifacts only inside a governed workflow. They may not approve, merge, deploy, activate runtime behavior, mutate production, bypass CI/CD, bypass SBAC/OPA, or remove mandatory evidence controls.
| Stage | Allowed Output | Required Gate |
| --- | --- | --- |
| Intake | Structured requirement, owner, classification, bounded context, risk tier, desired outcome. | Source and classification validation. |
| Analysis | Affected transactions, standard-step reuse options, rule/config alternatives, impacted contracts/schemas. | Architecture and security review. |
| Recommendation | Preferred configure/rule/adapter/code path with rationale, risk, test plan, evidence plan. | Human maker-checker decision. |
| Generation | Candidate design record, config, tests, contracts, policies, adapter skeletons, PR summary. | Branch-bound draft only; no direct runtime activation. |
| Validation | CI results, policy tests, architecture fitness, security scans, evidence pack. | Required pass or approved waiver. |
| Promotion | PR/MR-ready package with rollback/safe-disable path. | CODEOWNERS, ARB/CAB where applicable, post-promotion monitoring. |

# 15. Required Evidence Pack
| Evidence Item | Minimum Content |
| --- | --- |
| MicroFunction Design Record | Owner, source, requirement, bounded context, step code, classification, responsibility, dependencies, contract, policy, error model, evidence path. |
| Configuration Evidence | Transaction definition, step order, parameter rows, version, hash, activation state, publish-time validation result. |
| Catalog Evidence | Function entry, owner, status, version, classification ceiling, test profile, error policy, compensation behavior. |
| Test Evidence | Unit, policy, contract, failure-path, architecture fitness, regression, coverage/mutation, concurrency/load, DAST evidence where applicable. |
| Security Evidence | OPA/SBAC decisions, classification, secrets path, redaction, safe response, direct-call check, AI/model-route eligibility. |
| Runtime Evidence | trace_id, span_id, execution_id, transaction code, step result, policy decision, audit event, evidence_ref, outcome, compensation_ref. |
| PR/MR Evidence | AVCI summary, design-principle impact, AI-use declaration, affected contracts/schemas, scans, tests, reviewer approvals, rollback path. |

# 16. Validation Checklist
| Checklist ID | Validation Item | Gate |
| --- | --- | --- |
| VC-10A-001 | Requirement classified with owner, source, bounded context, data class, risk tier, and acceptance evidence. | Required |
| VC-10A-002 | Approved standard functions and templates searched before coding. | Required |
| VC-10A-003 | No-code / low-code / adapter / code-required decision documented. | Required |
| VC-10A-004 | New STP-BUS function has one responsibility and one owning bounded context. | Required when code added |
| VC-10A-005 | Direct DB/Kafka/Redis/OpenKM/workflow/model/secrets calls are absent from business logic. | Required |
| VC-10A-006 | Idempotency, timeout, retry, safe response, compensation, DLQ, replay, and rollback behavior declared. | Required for mutating/side-effecting steps |
| VC-10A-007 | OPA/SBAC/classification, abuse cases, guardrail, and DAST posture present where applicable. | Required |
| VC-10A-008 | Unit, policy, contract, failure-path, architecture fitness, security, observability, and regression tests pass. | Required before promotion |
| VC-10A-009 | Runtime evidence envelope emits trace, audit, policy, classification, idempotency, outbox, and evidence references. | Required |
| VC-10A-010 | PR/MR evidence pack includes AVCI summary, reviewer approvals, AI-use declaration, and rollback/safe-disable path. | Required |

# 17. Anti-Patterns and Rejection Rules
| Anti-Pattern | Required Response |
| --- | --- |
| Controller contains business logic or orchestration | Reject; move behavior to application service, MicroFunction runtime, or STP-BUS function behind approved ports. |
| Business function performs direct SQL, Kafka, Redis, OpenKM, workflow, model, or secrets access | Reject; use approved ports/adapters and policy-controlled runtime path. |
| Configuration bypasses identity, classification, authorization, idempotency, audit, telemetry, or evidence | Reject unless an approved waiver states why the control is not applicable. |
| AI-generated code activates behavior without review | Reject; require PR/MR, tests, policy checks, and human approval. |
| MicroFunction has multiple unrelated responsibilities | Reject; split into separate narrow functions or reuse standard steps. |
| Retry without idempotency and compensation | Reject for mutating or side-effecting steps. |
| Sensitive data in logs, prompts, traces, screenshots, tests, or dashboards | Block acceptance; remediate and record security evidence. |
| Evidence after the fact | Reject; evidence must be produced by the system of work and runtime controls, not manually reconstructed after mutation. |

# 18. RACI and Operating Responsibilities
| Activity | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Approve 10A guide | Enterprise Architecture | Architecture Board / IT Head | DevSecOps, Security, Development, QA, DBA | Engineering, Internal Audit |
| Create design record | Solutions Architect / Developer | Domain Owner | Security, QA, DBA, DevSecOps | Product Owner |
| Approve STP-BUS design | Domain Lead | Development Lead | Architecture, QA, Security | Internal Audit |
| Validate configuration activation | DevSecOps / QA | Platform Engineering Lead | Security, DBA, SRE | Release stakeholders |
| Review security posture | Security Architecture | Security Lead | DevSecOps, QA, Product Owner | Internal Audit |
| Promote production-bound change | Change Owner | CAB | Architecture, Security, QA, SRE | Affected teams |
| Promote learned knowledge | Knowledge Steward | Domain Owner | Architecture, Security, QA | Developers and AI users |

# 19. Review Queue and Next Document
| Seq | File | Current | Revised Target | Status | Next Step |
| --- | --- | --- | --- | --- | --- |
| 13 | 10-AIRA_MicroFunction_Framework_v3.1_Aligned.docx | v3.1 / v3.3 candidate | v3.4 Revised | Completed | Parent authority for 10A-10E |
| 14 | 10A-AIRA_MicroFunction_Design_and_Development_Guide_v2.1_Aligned.docx / v2.3 candidate | v2.1 / v2.3 candidate | v2.4 Revised | Completed by this revision | Use as design/development companion |
| 15 | 10B-AIRA_MicroFunction_Framework_Implementation_Standard_v2.1_Aligned.docx | v2.1 | v2.4 Revised | Next for Review | Translate parent and design rules into runtime implementation, package boundaries, adapters, tests, CI/CD gates |
| 16 | 10C-AIRA_MicroFunction_Sequence_Diagrams_and_Mermaid_Reference_v2.1_Aligned.docx | v2.1 | v2.2/v2.4 TBD | Pending | Review after 10B |
| 17 | 10D-AIRA_MicroFunction_Standard_Function_Catalog_and_Assembly_Templates_v2.1_Aligned.docx | v2.1 | v2.2/v2.4 TBD | Pending | Review after 10C |
| 18 | 10E-AIRA_MicroFunction_Backend_Service_Generation_and_Runtime_Configuration_Standard_v1.1.docx | v1.1 | v1.2 TBD | Pending | Review after 10D |

Next recommended document: 10B-AIRA_MicroFunction_Framework_Implementation_Standard_v2.1_Aligned.docx. Reason: 10B must now implement the corrected parent and 10A design controls as package boundaries, ports/adapters, runtime validators, configuration model, tests, and CI/CD enforcement before sequence diagrams and catalogs are finalized.

# 20. Acceptance Criteria

10A is approved as the design and development companion to AIRA-DOC-010 v3.4 and does not conflict with the parent standard.

Developers can apply the configure-first decision path without ambiguity before writing code.

Every new or changed MicroFunction has a complete Design Record, cross-cutting applicability matrix, tests, evidence, and rollback/compensation path.

STP-BUS functions remain isolated from controllers, infrastructure, workflow engines, model providers, and direct data-store clients.

System Builder templates include the Design Record, direct-call prohibitions, cross-cutting coverage matrix, runtime toggle rules, and PR/MR evidence checklist.

Critical, mutating, boundary-crossing, security-sensitive, AI-assisted, or production-bound transactions pass contract, policy, security, observability, idempotency, resilience, and evidence gates.

# 21. Open Reconciliation Items
| Item | Treatment |
| --- | --- |
| Foundation references to 08, 08A, and 09 | Do not mark as completed in this workstream unless verified. Inherit active baseline until those files are uploaded/revised or reconciled. |
| Version number harmonization | This file uses v2.4 because the uploaded file was already a v2.3 candidate/addendum. Register 00D / revision matrix should record supersedence. |
| 10B/10C/10D/10E dependency chain | 10B should be reviewed next before diagram and catalog documents to avoid rework. |
| 41B / 44 System Builder overlap | Continue to reference both until master register reconciles final authority. |
| Runtime telemetry toggles | Companion implementation and observability documents must preserve non-disableable audit, security, policy, classification, idempotency, outbox, model-route, and evidence signals. |

# 22. AVCI Compliance Summary
| AVCI Property | Evidence in This v2.4 Revision |
| --- | --- |
| Attributable | Defines owner, co-owners, role responsibilities, Design Record ownership, catalog ownership, source document, parent standard, and review queue sequence. |
| Verifiable | Defines validation checklist, test gates, architecture fitness checks, CI/CD evidence, publish-time validation, runtime evidence envelope, and acceptance criteria. |
| Classifiable | Requires classification for requirements, configuration, inputs/outputs, logs, traces, events, model routes, tool actions, tests, screenshots, prompts, and evidence. |
| Improvable | Defines simplification recommendations, automation controls, improvement path, versioning, review cadence, next-document review queue, and Auto-Heal/Learn/Improve candidate governance. |

# 23. Change Log
| Version | Date | Owner | Summary |
| --- | --- | --- | --- |
| v2.1 | 2026-05-21 | Solutions Architecture Office / IT Head | Aligned Pack 04 v1.2 design/development and Java 25 update. |
| v2.3 candidate | 2026-06-16 | AIRA Review Board / AI-assisted review | Reviewed, corrected, aligned, simplified, and improved against revised foundation, parent MicroFunction candidate, System Builder, DevSecOps, security, observability, and evidence model. |
| v2.4 revised | 2026-06-18 | Solutions Architecture Office / IT Head | Promotes v2.3 candidate into a revised companion guide aligned to AIRA-DOC-010 v3.4, embeds cross-cutting capability coverage, corrects review queue, and strengthens design records, evidence, and System Builder controls. |

