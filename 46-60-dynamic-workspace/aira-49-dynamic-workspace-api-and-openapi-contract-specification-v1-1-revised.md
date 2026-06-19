---
title: "Dynamic Workspace API and OpenAPI Contract Specification"
doc_id: "AIRA-49"
version: "v1.1"
status: "revised"
category: "Dynamic workspace"
source_docx: "AIRA_49_Dynamic_Workspace_API_and_OpenAPI_Contract_Specification_v1.1_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 46-60-dynamic-workspace
  - revised
  - aira-49
---



# Dynamic Workspace API and OpenAPI Contract Specification



AIRA

AI-Native Enterprise Platform

Dynamic Workspace API and OpenAPI Contract Specification

REST Contracts | OpenAPI | Widget Actions | Backend Authority | MicroFunction Binding | Evidence APIs | AVCI Always

AIRA-DOC-049 | Version v1.1 Revised | INTERNAL CONFIDENTIAL
| Mandatory Practice Statement | No AIRA Dynamic Workspace component, widget, Experience Block, AI Assistant panel action, Admin Builder operation, or personalization change may call an endpoint that is not contract-defined, security-reviewed, capability-bound, MicroFunction-aware where applicable, observable, testable, versioned, reversible, and AVCI-evidenced. The frontend may render and submit approved inputs only. Backend APIs remain the authority for workspace resolution, policy filtering, field/action visibility, widget data, protected mutations, AI routing, and evidence retrieval. |
| --- | --- |

# Document Control
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-049 |
| Canonical Filename | 49-AIRA_Dynamic_Workspace_API_and_OpenAPI_Contract_Specification_v1.1_Revised.docx |
| Version | v1.1 - Revised Dynamic Workspace, OpenAPI, MicroFunction, Security, Observability, CI/CD, and Evidence Alignment |
| Status | Draft for Architecture Board, CAB, API Architecture, Security, DevSecOps, Frontend, Backend, QA/SDET, Platform Engineering, AI Governance, SRE, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; API Architecture; Workspace Platform Team; Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; Platform Engineering; AI Governance; SRE; Internal Audit |
| Supersedes | 49-AIRA_Dynamic_Workspace_API_and_OpenAPI_Contract_Specification_v1.0 |
| Primary Parent / Companions | 41 Dynamic User Workspace Framework; 42 Composable Experience Framework; 43 Multimodal AI Assistant Panel; 44 Next.js Rendering Strategy; 46 Runtime Configuration and Cache; 47 Developer Implementation Guide; 48 Database/Flyway Specification; 50 Component/Widget Development; 51 Security/OPA/SBAC/ABAC; 52 Testing and Fitness Functions; 53 Observability; 54 Admin Builder; 60 DevSecOps Evidence; 15/15A API Governance; 16/16A/16B Database/Flyway; 17/17A Security; 20/45 CI/CD and PoC 2; 31/31A Operations and Observability |
| External Alignment Checked | OpenAPI Specification 3.1+/3.2 where approved tooling supports; AsyncAPI 3.1.0; CloudEvents 1.0 family; OpenTelemetry Semantic Conventions; NIST SSDF SP 800-218; OWASP ASVS 5.0.0; SLSA v1.2 |

# Static Table of Contents

Executive Summary and Revision Verdict

Purpose, Scope, Authority, and Source Alignment

API Design Principles and Contract Families

Workspace API Groups, Headers, Envelopes, Errors, and Idempotency

Dynamic Workspace, MicroFunction, AI Assistant, and Evidence Endpoint Baseline

Security, OPA/SBAC, Classification, Rate Limits, Runtime Toggles, and Safe Responses

OpenAPI Governance, AsyncAPI/Event Interface, CI/CD Gates, and GitNexus Evidence

Observability, Testing, Resilience, RACI, Acceptance Criteria, and AVCI Summary

# 1. Executive Summary and v1.1 Revision Verdict

This revised specification upgrades AIRA-DOC-049 from a baseline REST/OpenAPI contract specification into the governed contract authority for the AIRA Dynamic Workspace, Composable Experience Framework, Admin Builder, widget runtime, AI Assistant panel, and backend-governed UI surface. It preserves the original rule that no workspace component may call an endpoint unless the endpoint is registered, contract-defined, security-reviewed, and capability-bound. It expands that rule to cover MicroFunction binding, OpenAPI contract testing, evidence APIs, runtime toggles, observability, CI/CD gates, and AI governance.

The Dynamic Workspace is not a frontend authority layer. It is a backend-governed experience plane. APIs must return already-authorized screens, fields, widgets, actions, data shapes, safe states, evidence references, and policy-filtered configuration. Mutating widget actions must flow through idempotent backend APIs, MicroFunction transactions where applicable, audit/evidence records, outbox events when required, and approval workflows for high-risk actions.
| v1.1 Outcome | Required Result |
| --- | --- |
| Backend-governed UI | Workspace resolution, field/action visibility, layout activation, AI eligibility, and protected actions are determined by backend services and OPA/SBAC, not browser logic. |
| Contract-first delivery | OpenAPI contracts, schemas, examples, error responses, security schemes, idempotency rules, and generated clients must exist before implementation is mergeable. |
| MicroFunction action binding | Widget actions map to capability_code, action_code, API operationId, MicroFunction transaction code, idempotency profile, audit profile, and evidence profile. |
| Evidence by construction | Every protected API response carries traceId and evidenceRef where applicable; protected mutations emit audit, telemetry, and evidence records. |
| Runtime-safe flexibility | Feature flags, telemetry verbosity, sampling, and safe-disable toggles are contract-visible only through governed configuration and never through ad hoc frontend switches. |

# 2. Purpose, Scope, Authority, and Source Alignment
| Area | Treatment |
| --- | --- |
| Purpose | Define REST and OpenAPI contract requirements for Dynamic Workspace resolution, component discovery, layout validation, widget runtime, Admin Builder lifecycle, AI Assistant interaction, evidence retrieval, runtime toggles, and protected actions. |
| In Scope | OpenAPI contracts, request/response envelopes, headers, security schemes, common errors, idempotency keys, pagination, optimistic concurrency, widget action contracts, generated frontend clients, mock servers, contract tests, OPA/SBAC inputs, audit/evidence fields, and CI/CD gates. |
| Out of Scope | Frontend-only authorization, unregistered endpoints, direct database access from UI, direct Kafka publish from browser, raw model-provider calls, uncontrolled prompt endpoints, manual bypass of OPA/SBAC, or production mutation outside governed APIs and approval gates. |
| Authority | AIRA-DOC-049 governs Dynamic Workspace API/OpenAPI implementation. AIRA-DOC-015/015A govern enterprise API and integration policy. AIRA-DOC-048 governs database backing tables. AIRA-DOC-051/17/17A/32 govern authorization. AIRA-DOC-053/31A govern observability and evidence. Conflicts are AVCI reconciliation items. |

# 3. API Design Principles and Contract Families
| Principle | Mandatory API Requirement |
| --- | --- |
| Contract-first | OpenAPI contract, schema, examples, security requirements, problem responses, and tests precede implementation and frontend consumption. |
| Backend authority | API responses expose only policy-filtered workspaces, screens, components, fields, actions, data, and AI capabilities. |
| Capability-bound | Every protected operation maps to capability_code, SBAC skill, OPA input schema, owning bounded context, and evidence profile. |
| Idempotent mutation | Mutating widget, layout, template, approval, and AI artifact actions require Idempotency-Key and duplicate-safe backend behavior. |
| Safe response | Errors use stable codes, safe message categories, traceId, evidenceRef where applicable, and no secrets, raw tokens, raw PII, prompt leakage, or exploit details. |
| Observable by design | REST, gateway, backend service, MicroFunction, policy, database, cache, workflow, and AI spans propagate trace and evidence correlation. |
| Versioned and reversible | APIs use versioned paths, backward-compatible schema evolution, deprecation windows, client compatibility checks, rollback/forward-fix, and feature-disable path. |

## Contract Families
| Contract Family | Purpose |
| --- | --- |
| Workspace Resolution | Resolve workspace, screen, layout, component instances, allowed actions, policy-filtered fields, evidence profiles, and safe UI states. |
| Component Catalog | Expose approved component metadata, schemas, rendering constraints, data-source contracts, classification ceilings, and accessibility requirements. |
| Layout / Personalization | Validate, save, reset, rollback, compare, and resolve user overlays under policy, version, idempotency, and optimistic concurrency. |
| Widget Runtime | Resolve widget data, execute widget action requests, validate inputs, enforce policy, bind to MicroFunctions/workflows, and return safe outcomes. |
| Admin Builder / Template Lifecycle | Draft, validate, publish, activate, retire, rollback, and evidence workspace templates through maker-checker approval. |
| AI Assistant Panel | Submit classified prompt requests, attach approved evidence references, route through LiteLLM/guardrails, store artifacts, and enforce human review. |
| Evidence and Audit | Retrieve permitted evidence references, event timelines, policy decisions, trace links, and acceptance evidence without exposing restricted data. |

# 4. Workspace API Groups, Headers, Envelopes, Errors, and Idempotency
| Group | Base Path | Purpose |
| --- | --- | --- |
| Workspace Resolution | /api/workspace/v1 | Resolve current workspace, screen, policy-filtered layout, safe states, evidence profile, and runtime configuration digest. |
| Component Catalog | /api/workspace/v1/components | Discover allowed component types, props schema, data contract, widget state model, action binding, classification ceiling, and accessibility profile. |
| Layout Management | /api/workspace/v1/layouts | Validate, save, reset, compare, rollback, activate, and retrieve layout versions and user overlays. |
| Widget Runtime | /api/workspace/v1/widgets | Resolve widget data, submit widget actions, perform dry-run where applicable, and retrieve action status. |
| Admin Template | /api/workspace/v1/admin | Manage template drafts, approvals, activations, retirements, safe disables, and rollback requests. |
| AI Assistant | /api/ai-assist/v1 | Submit prompt/artifact requests, retrieve AI outputs, view guardrail status, and link evidence references. |
| Evidence | /api/evidence/v1 | Retrieve evidence records, audit timelines, trace references, policy decisions, and acceptance results according to SBAC/classification. |
| Runtime Toggles | /api/workspace/v1/runtime-toggles | Read or request changes to approved telemetry, feature, diagnostic, and safe-disable toggles under maker-checker policy. |

## Common Required Headers
| Header | Required | Purpose |
| --- | --- | --- |
| Authorization | Yes | Bearer token, service token, or approved workload identity. Never expose token values in logs, UI, traces, or evidence. |
| X-Trace-Id | Yes | End-to-end correlation across frontend, gateway, API, MicroFunction, database, Kafka, workflow, AI, audit, and evidence. |
| X-Request-Id | Yes | Client/request correlation and deduplication support. |
| Idempotency-Key | Required for mutations | Duplicate-safe layout, widget, template, approval, AI artifact, and protected state-changing operations. |
| X-AIRA-Client-Version | Yes | Frontend compatibility, deprecation handling, generated-client validation, and incident traceability. |
| X-AIRA-Workspace-Version | Conditional | Workspace/layout version validation, optimistic concurrency, and stale client detection. |
| X-AIRA-Classification | Conditional | Declared client-side handling ceiling. Server classification and policy decision remain authoritative. |

## Standard Response Envelope

{
  "success": true,
  "traceId": "trc-...",
  "requestId": "req-...",
  "evidenceRef": "evd-...",
  "classification": "CONFIDENTIAL",
  "policyDecisionRef": "pol-...",
  "data": { },
  "warnings": [ ],
  "links": { }
}

## Problem Details / Safe Error Model
| Field | Required Meaning |
| --- | --- |
| errorCode | Stable AIRA error code such as AIRA-WS-403-POLICY-DENIED or AIRA-WS-409-VERSION-CONFLICT. |
| message | Safe, user-appropriate message without stack traces, raw SQL, tokens, prompt contents, exploit details, or PII. |
| traceId / evidenceRef | Always include traceId; include evidenceRef when an evidence record is created and the actor is eligible to receive the reference. |
| retryable / retryAfter | Declare whether retry is allowed and bounded. Do not encourage retry storms. |
| classification | Classification and handling rule for the error response. |

## Idempotency and Optimistic Concurrency Rules

All POST/PATCH/DELETE operations that can mutate workspace state, layout, template lifecycle, widget actions, AI artifacts, approval requests, runtime toggles, or evidence records require Idempotency-Key.

Idempotency result reuse must return the original safe response or a stable status reference, not duplicate state changes or duplicate events.

Layout and template updates must use version/hash checks. Stale workspace versions must return safe conflict responses and must not overwrite newer approved state.

Mutating actions must persist idempotency, audit, evidence, and outbox intent in one governed transactional boundary where applicable.

# 5. Endpoint Baseline and Mandatory Operation Contracts
| Operation | Mandatory Contract Behavior |
| --- | --- |
| GET /workspaces/current | Resolve allowed workspace for actor/channel/tenant/role/skill; return policy-filtered screens, layout digest, safe states, evidence profile. |
| GET /workspaces/{workspaceCode}/screens/{screenCode} | Resolve one screen including component instances, actions, field visibility, runtime toggles, and classification ceiling. |
| GET /components | List only approved and actor-eligible component metadata with props schema and supported action contracts. |
| POST /layouts/validate | Validate layout JSON/schema, policy bindings, component constraints, accessibility rules, and MicroFunction/action bindings. |
| POST /layouts/save | Save personal overlay or draft layout using idempotency, optimistic concurrency, audit, and policy checks. |
| POST /widgets/{componentInstanceId}/data-query | Resolve data through backend service/adapters. No widget may build SQL or call protected backend internals directly. |
| POST /widgets/{componentInstanceId}/actions/{actionCode} | Invoke a capability-bound widget action through policy, idempotency, MicroFunction/workflow binding, audit, and evidence. |
| POST /admin/templates/publish-request | Create maker-checker approval request for template publication or activation; direct production activation is prohibited. |
| POST /ai-assist/prompts | Submit classified, policy-filtered AI request through approved prompt template, evidence refs, guardrails, LiteLLM route, and artifact policy. |
| GET /evidence/{evidenceRef} | Return permitted evidence summary or redacted evidence reference based on SBAC, classification, legal hold, and retention rules. |
| POST /runtime-toggles/change-request | Request telemetry, feature, diagnostic, safe-disable, sampling, or AI capability toggle change through OPA/SBAC and approval workflow. |

## MicroFunction Binding Contract
| Binding Field | Required Meaning |
| --- | --- |
| capability_code | Stable capability identifier exposed to policy and audit. |
| action_code | Widget action submitted by frontend. Must not be interpreted as authority. |
| operationId | OpenAPI operationId mapped to backend use case and generated client. |
| microfunction_transaction_code | Runtime transaction executed by backend when the action is mutating or business-governed. |
| idempotency_profile | Defines duplicate-safe behavior, retry/replay handling, and response reuse. |
| audit_profile / evidence_profile | Defines append-only audit events, evidence schema, retention, and dashboard linkage. |
| approval_required | True for maker-checker, Restricted, destructive, high-risk, privilege, production-impacting, and policy-exception actions. |

# 6. Security, OPA/SBAC, Classification, Runtime Toggles, and AI Safety
| Control | API Requirement |
| --- | --- |
| Authentication | OIDC/JWT or approved workload identity is mandatory. Unauthenticated protected workspace endpoints fail closed. |
| Authorization | OPA/SBAC/ABAC/RBAC decisions are evaluated server-side. Frontend visibility is a rendering effect, not an authorization decision. |
| Classification | Every response carries classification; raw Restricted data, secrets, raw prompts, raw documents, and tokens are never returned unless explicitly approved and necessary. |
| Least privilege | APIs expose only capabilities within actor skills, role, tenant, branch/unit, workflow assignment, trust tier, and classification ceiling. |
| Rate limits and quotas | Apply user, tenant, API, widget, AI budget, and workflow limits. Responses must be safe and observable without leaking thresholds exploitable by attackers. |
| Runtime toggles | Runtime toggles are approved configuration, not developer shortcuts. Changes require owner, reason, scope, expiry where applicable, evidence, rollback, and audit. |
| AI safety | AI Assistant APIs route only through approved gateway/LiteLLM aliases and guardrails. AI output is advisory unless a separately approved workflow grants authority. |

## Runtime Toggle Categories
| Toggle Category | Governed API Treatment |
| --- | --- |
| Telemetry sampling | May adjust trace/log/metric sampling within approved bounds. Must not disable audit evidence for protected actions. |
| Diagnostic verbosity | May increase safe diagnostics temporarily. Must not log PII, secrets, tokens, raw prompts, or raw customer documents. |
| Feature safe-disable | May hide/deactivate a component, action, template, or AI capability safely without corrupting authoritative configuration. |
| AI capability route | May disable AI panel capability, enforce stronger guardrails, change approved model alias, or require human review; direct provider fallback is prohibited. |
| Cache behavior | May bypass, invalidate, or rebuild derivative cache. PostgreSQL/Git-approved configuration remains authoritative. |

# 7. OpenAPI, AsyncAPI/Event Interface, CI/CD Gates, and GitNexus Evidence

OpenAPI files must define paths, operationIds, schemas, examples, security schemes, response envelopes, problem details, idempotency headers, pagination, versioning, and deprecation metadata.

Generated frontend clients must be produced from approved OpenAPI contracts and must not hand-code protected endpoint paths or bypass contract validation.

Contract lint, breaking-change detection, schema validation, generated-client build, mock server tests, and Playwright/API integration tests are CI gates before merge.

If a Dynamic Workspace API produces or consumes events, the event interface must be declared in AsyncAPI with Kafka topic, Avro schema, CloudEvents attributes, security, compatibility, DLQ, replay, and retention rules.

GitNexus evidence is read-only and derivative: code map, endpoint ownership, affected clients, affected components, impact summary, contract drift, and sensitive operation map support review but do not replace tests or human approval.

## Event and Outbox Integration Requirements
| Event | Required Contract Metadata |
| --- | --- |
| TemplatePublishedEvent | Emitted after approved template publication/activation through transactional outbox; includes workspace_code, version, actor, approval_ref, trace_id, evidence_ref. |
| WorkspaceLayoutChangedEvent | Emitted when approved/personalized layout changes require downstream cache invalidation, audit projection, or synchronization. |
| WidgetActionRequestedEvent | Optional async event for long-running widget action; action execution remains idempotent and capability-bound. |
| AIArtifactGeneratedEvent | Emitted only for approved artifact metadata, not raw prompts or restricted output. Guardrail result, model alias, trace_id, evidence_ref required. |
| RuntimeToggleChangedEvent | Emitted for approved runtime toggle changes with scope, TTL, approver, old/new hash, rollback_ref, and evidence_ref. |

## CI/CD Evidence Gates
| Gate | Minimum Evidence |
| --- | --- |
| Contract lint and schema validation | OpenAPI/JSON Schema lint report, examples validation, generated client compile proof. |
| Backward compatibility | Breaking-change scan, versioning/deprecation decision, consumer impact evidence. |
| Security | Auth scheme validation, OPA/SBAC tests, authenticated DAST scope, secret scan, safe error tests. |
| Observability | Trace propagation tests, log redaction tests, evidenceRef tests, dashboard readiness evidence. |
| Resilience | Idempotency tests, duplicate submit tests, stale version tests, retry/DLQ/replay tests for async operations. |
| GitNexus | Read-only impact summary linking endpoints, frontend clients, components, MicroFunctions, policies, tests, and evidence pack. |

# 8. Observability, Testing, Resilience, RACI, Acceptance Criteria, and AVCI Summary
| Signal | Required API Evidence |
| --- | --- |
| Trace correlation | Every request propagates trace_id/request_id through frontend, gateway, backend, OPA, MicroFunction, database, cache, Kafka, workflow, AI, audit, and evidence. |
| Metrics | Latency, error rate, policy-deny rate, widget action success/failure, cache hit/miss, AI guardrail outcomes, contract drift, DAST results, and evidence completeness. |
| Logs | Structured Log4j2/backend and frontend logs with redaction and no raw tokens, secrets, raw PII, raw prompts, unrestricted documents, or high-cardinality labels. |
| Dashboards | Workspace API health, policy denials, slow widgets, contract drift, runtime toggle state, AI panel usage, cache invalidation, and evidence completeness. |

## Testing and Resilience Baseline
| Test Type | Minimum Required Coverage |
| --- | --- |
| Contract tests | OpenAPI diff, schema examples, generated-client tests, mock server tests, error model tests, response-envelope tests. |
| Security tests | OPA/Rego policy tests, SBAC skill tests, classification tests, authenticated DAST, safe response tests, rate limit tests. |
| MicroFunction tests | Capability binding, idempotency, execution envelope, audit/evidence, outbox, retry, compensation, and safe disable. |
| Frontend integration | Generated client usage, loading/empty/error/denied/safe-disabled states, accessibility, and no hardcoded protected endpoint bypass. |
| Resilience lab | Duplicate action replay, stale layout version, cache loss, OPA unavailable, evidence store unavailable, Kafka publish failure, DLQ/replay, and AI guardrail failure. |

## RACI Summary
| Activity | Architecture/API | Development | QA/SDET | Security | DevSecOps/SRE | Internal Audit |
| --- | --- | --- | --- | --- | --- | --- |
| Approve API contract standard | A/R | C | C | C | C | I |
| Author/update OpenAPI contracts | A | R | R | C | C | I |
| Validate security and OPA/SBAC | C | R | C | A/R | C | I |
| Build generated clients/tests | C | R | R | C | C | I |
| Operate CI/CD evidence gates | C | C | R | C | A/R | I |
| Review audit/evidence completeness | C | C | C | C | C | A/R |

## Acceptance Criteria

All Dynamic Workspace API endpoints are present in approved OpenAPI contracts with schemas, examples, security schemes, response envelopes, problem details, and operationIds.

Generated frontend clients compile and are used by workspace components; protected endpoints are not hand-coded or bypassed.

Workspace resolution returns only backend-authorized screens, components, fields, actions, and AI capabilities.

Mutating widget, layout, template, AI artifact, and runtime-toggle operations enforce idempotency, policy, evidence, audit, and rollback/safe-disable path.

Async event impacts are described in AsyncAPI with Kafka, Avro, CloudEvents, outbox/inbox, idempotent consumer, DLQ/replay, and schema compatibility evidence where applicable.

CI/CD evidence proves contract linting, compatibility, tests, security scans, authenticated DAST, GitNexus impact, observability checks, and AVCI summary completion.

## AVCI Compliance Summary
| AVCI Property | Evidence |
| --- | --- |
| Attributable | Every API contract, operationId, capability binding, owner, source reference, approval, commit, generated client, and evidence record identifies responsible roles and source. |
| Verifiable | OpenAPI/AsyncAPI contracts, tests, generated clients, OPA decisions, traces, audit records, GitNexus reports, CI/CD gates, and dashboard evidence prove behavior. |
| Classifiable | Contracts carry classification, response handling, field visibility, retention, prompt/artifact routing, and forbidden telemetry/data rules. |
| Improvable | Contract drift, API failures, policy denials, performance issues, DAST findings, widget feedback, and Auto-Heal/Auto-Learn/Auto-Improve candidates feed controlled backlog items. |

# Final Governance Rule

AIRA-DOC-049 is accepted only when Dynamic Workspace APIs can be generated, consumed, tested, secured, observed, audited, versioned, rolled back, and improved without frontend authority drift, unregistered endpoints, uncontrolled AI actions, manual production mutation, unsafe telemetry, or missing evidence. Contract-first delivery is mandatory; working screens without governed contracts are not accepted.

