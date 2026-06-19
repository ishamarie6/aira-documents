---
title: "Dynamic Workspace Developer Implementation Guide"
doc_id: "AIRA-47"
version: "v1.1"
status: "revised"
category: "Dynamic workspace"
source_docx: "AIRA_47_Dynamic_Workspace_Developer_Implementation_Guide_v1.1_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 46-60-dynamic-workspace
  - revised
  - aira-47
---



# Dynamic Workspace Developer Implementation Guide



AIRA

AI-Native Enterprise Platform

Dynamic Workspace Developer Implementation Guide

Frontend Renderer | Backend Workspace Resolver | Component Registry | Capability Binding | MicroFunction Integration | Evidence by Construction
| Mandatory Practice Statement: AIRA Dynamic Workspace development is acceptable only when frontend rendering, backend authorization, MicroFunction execution, contract-first APIs, policy-as-code, runtime configuration, observability, tests, security gates, rollback controls, and AVCI evidence operate together. The frontend renders. The backend authorizes. MicroFunctions execute. PostgreSQL defines truth. Redis/Valkey accelerates. AVCI proves trust. |
| --- |
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-047 |
| Canonical Filename | AIRA_47_Dynamic_Workspace_Developer_Implementation_Guide_v1.1_Revised.docx |
| Version | v1.1 Revised |
| Status | Draft for Architecture Review Board, Security, DevSecOps, QA/SDET, and CAB Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Software Development Lead; Frontend Lead; DevSecOps Lead; Security Architecture; QA/SDET; Platform Engineering; AI Engineering; SRE / Operations; Internal Audit |
| Primary Audience | Solutions Architects, Frontend Developers, Backend Developers, DevSecOps, QA/SDET, Security, Product Owners, Internal Audit, and approved AI coding agents |
| Supersedes | 47-AIRA_Dynamic_Workspace_Developer_Implementation_Guide_v1.0.docx |
| Primary Source Baseline | Active AIRA source packs, with focus on Documents 46 through 61 and the MicroFunction, API, Security, DevSecOps, Observability, and AVCI standards |
| Review Cadence | Quarterly; unscheduled on material Dynamic Workspace, MicroFunction, API, security, AI, workflow, cache, database, or DevSecOps change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Dynamic-Workspace / Developer-Implementation / v1.1/ |

# Table of Contents

1. Executive Summary

2. Source Alignment and v1.1 Revision Decision

3. Purpose, Scope, and Authority

4. Developer Operating Model

5. Reference Architecture and Repository Structure

6. Implementation Layers and Boundaries

7. Contract-First Development Workflow

8. Backend Workspace Services

9. Frontend Renderer and Component Rules

10. Component Registry, Experience Blocks, and Capability Binding

11. MicroFunction and Workflow Integration

12. Configuration, Feature Flags, Runtime Cache, and Synchronization

13. API, Event, Outbox, DLQ, and Replay Implementation

14. Security, OPA/SBAC, Secrets Hygiene, and Abuse Cases

15. Observability, Runtime Telemetry, Audit, and Evidence

16. Concurrency, Heavy Transaction, Idempotency, and Resilience Lab

17. DevSecOps Pipeline, GitNexus, and Evidence Pack

18. Testing and Architecture Fitness Functions

19. Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop

20. Developer Checklists and Definition of Done

21. RACI

22. Acceptance Criteria

23. Open Reconciliation Items

24. Review Queue Control Register

25. AVCI Compliance Summary

Appendices

Note: Before final publication, use Microsoft Word References > Table of Contents > Automatic Table, then update all fields.

# 1. Executive Summary

This revised implementation guide converts the Dynamic Workspace architecture into practical development instructions for the software development team. It defines how developers shall implement backend workspace resolution, frontend rendering, component registration, capability binding, MicroFunction integration, runtime configuration, API/event contracts, cache behavior, observability, tests, DevSecOps evidence, and controlled AI-assisted generation without weakening AIRA governance.

Version 1.1 strengthens the original v1.0 guide by making implementation behavior explicit across frontend, backend, MicroFunction runtime, contracts, events, cache, security, observability, resilience, accessibility, DevSecOps, and continuous-improvement loops. It also incorporates the revised direction from Documents 46, 59, 60, and 61 so that developer implementation remains aligned with runtime cache authority, UX/accessibility acceptance, evidence-pack enforcement, and AI-assisted System Builder governance.
| Core Developer Rule: The frontend must never become policy authority, workflow authority, data authority, AI action authority, or production authority. It may render approved workspace definitions, collect user intent, show safe state, and call generated clients only. Backend services, OPA/SBAC, workflow engines, and MicroFunctions remain authoritative. |
| --- |
| Strategic Outcome | Required Implementation Result |
| --- | --- |
| Backend-governed workspace | Workspace definitions, user layout, component visibility, policy filtering, classification ceiling, and action availability are resolved by backend services and policy decisions. |
| Contract-first delivery | OpenAPI, AsyncAPI, Avro/JSON Schema, CloudEvents, component schemas, and MicroFunction design records are created or updated before code. |
| MicroFunction-backed action model | Every protected widget action maps to a capability, policy decision, idempotency key, audit profile, evidence profile, and MicroFunction transaction. |
| Safe frontend implementation | No unregistered components, no invented endpoints, no browser-side authorization, no raw secrets/PII in browser logs, and no direct model/database calls. |
| Evidence by construction | PR/MR, CI/CD, GitNexus, tests, security scans, telemetry validation, accessibility proof, rollback plan, and runtime evidence are captured for every material change. |
| Governed improvement | Auto-Heal, Auto-Learn, and Auto-Improve generate candidate fixes and learning proposals only; human review and evidence gates remain mandatory. |

# 2. Source Alignment and v1.1 Revision Decision

The original Document 47 is structurally sound and should remain the developer implementation companion for the Dynamic Workspace family. It already states the correct operating rule: the frontend renders, the backend authorizes, MicroFunctions execute, PostgreSQL defines truth, Redis accelerates, and AVCI proves trust. Version 1.1 keeps that rule and expands the implementation details required for enterprise-grade engineering delivery.
| Source / Companion | Alignment Applied in v1.1 |
| --- | --- |
| 01 / 01A / 01B | AVCI, SOLID, Clean Architecture, DDD, ports/adapters, fitness functions, evidence, and change accountability are required for every frontend, backend, configuration, and AI-assisted artifact. |
| 10 / 10A / 10B / 10C / 10D / 10E | Dynamic Workspace actions must map to MicroFunction transaction assembly, standard step families, runtime configuration, idempotency, audit, observability, and rollback evidence. |
| 15 / 15A | Workspace APIs, evidence APIs, action APIs, generated clients, events, errors, idempotency, pagination, correlation, and versioning follow contract-first governance. |
| 16 / 16A / 16B | Schemas, seed data, RLS, indexes, reference data, config tables, and migrations are Flyway-governed. No manual production DDL. |
| 17 / 17A / 32 / 51 | Identity, RBAC, ABAC, SBAC, OPA, classification, secrets, tenant isolation, and policy decisions are backend and policy responsibilities. |
| 31 / 31A / 53 | Workspace loads, renders, widget actions, layout changes, AI prompts, policy denials, and MicroFunction-backed actions emit trace, metric, log, audit, and evidence signals. |
| 46 | PostgreSQL and Git-managed configuration define truth; Redis/Valkey holds derivative runtime views only and must be rebuildable. |
| 59 / 60 / 61 | UX/accessibility, evidence-pack gates, AI-assisted generation, System Builder workflows, backend authority, and rollback/deactivation controls are incorporated into developer execution. |

## 2.1 v1.1 Gap Closure Summary

Added explicit frontend/backend authority boundaries and anti-bypass controls.

Added contract-first development instructions for OpenAPI, AsyncAPI, Avro, CloudEvents, and generated clients.

Added MicroFunction binding rules for every protected widget action.

Added runtime cache rules, cache loss behavior, invalidation behavior, and feature-flag governance.

Added observability, audit, Sentry, Loki, Tempo, Grafana, and trace reconstruction requirements.

Added concurrency, heavy transaction, idempotency, resilience, DLQ, replay, and failure-aware UX behavior.

Added DevSecOps, GitNexus, security gates, authenticated DAST, accessibility, visual regression, and evidence pack requirements.

Added Auto-Heal, Auto-Learn, and Auto-Improve candidate-loop controls with human approval.

# 3. Purpose, Scope, and Authority

## 3.1 Purpose

The purpose of this guide is to define how AIRA developers implement Dynamic Workspace capabilities consistently across frontend, backend, contracts, MicroFunctions, configuration, cache, policy, tests, observability, and evidence. It is designed to be practical enough for sprint execution while strict enough to prevent architecture drift, frontend authority leakage, uncontrolled AI generation, and unverifiable runtime behavior.

## 3.2 Scope
| In Scope | Out of Scope |
| --- | --- |
| Runtime workspace renderer, component registry, widget shell, AI assistant panel integration, personalization UX, admin-builder integration, and safe frontend state handling. | A frontend-only low-code platform, browser-side business authority, browser-side authorization authority, or arbitrary remote component execution. |
| Backend workspace resolver, configuration APIs, capability binding service, generated clients, policy-filtered layout resolution, and MicroFunction execution boundary. | Direct SQL, direct Kafka, direct AI model, direct workflow, direct secret, or direct production calls from UI components. |
| OpenAPI/AsyncAPI contracts, schema evolution, Avro/JSON Schema, CloudEvents, outbox, idempotency, DLQ, replay, observability, tests, security scans, and evidence packs. | Manual production mutation, manual DDL, unregistered endpoints, unapproved topics, unreviewed policies, or unversioned configuration. |
| AI-assisted generation through System Builder under review, sandboxing, PR/MR, policy checks, security scans, and human approval. | AI approval of its own output, direct merge/deploy authority, ungoverned agent-created components, or production-impacting autonomous changes. |

## 3.3 Authority
| Level | Authority | Implementation Meaning |
| --- | --- | --- |
| L0 | Architecture Board, CAB, Security Governance, Data Governance | Final authority for production-impacting workspace architecture, policy, data, security, and release decisions. |
| L1 | AIRA AVCI, Enterprise Design Principles, Engineering Blueprint, Security, DevSecOps, API, Database, Observability, Change standards | Universal rules for architecture, security, contracts, migration, tests, evidence, rollback, and human accountability. |
| L2 | This Document 47 | Developer implementation authority for Dynamic Workspace frontend/backend implementation details. |
| L3 | OpenAPI/AsyncAPI contracts, Flyway migrations, component registry, OPA policies, MicroFunction catalog, CI/CD pipeline, evidence manifests | Executable controls that prove and enforce this guide. |
| L4 | Runtime telemetry, audit events, incidents, tickets, PR/MR evidence, dashboards, and runbooks | Operational proof and improvement inputs. |

# 4. Developer Operating Model
| Operating Model: Developers implement AIRA Dynamic Workspace features by changing approved contracts, schemas, configuration, component registry entries, policies, MicroFunction bindings, generated clients, tests, and evidence. Working screens alone are not sufficient. |
| --- |
| Step | Developer Action | Mandatory Evidence |
| --- | --- | --- |
| 1 | Start from approved ticket, requirement, incident, improvement proposal, or System Builder intake. | Ticket or intake ID, owner, classification, bounded context, affected workspace, and acceptance criteria. |
| 2 | Identify affected workspace, screen, component, capability, API, event, policy, MicroFunction, and data model. | Impact analysis, GitNexus or code-map reference, and affected contract list. |
| 3 | Update contracts and schemas before implementation. | OpenAPI/AsyncAPI/schema validation, compatibility result, and reviewer sign-off. |
| 4 | Update configuration, component registry, capability bindings, feature flags, and policies. | Config hash, policy test, registry diff, rollback target, and classification review. |
| 5 | Implement frontend and backend through defined ports/adapters and generated clients. | Unit/component tests, architecture fitness evidence, no direct provider/database/model calls. |
| 6 | Bind protected actions to MicroFunction transactions and workflow approvals where applicable. | MicroFunction transaction code, idempotency profile, audit profile, evidence profile, and OPA decision reference. |
| 7 | Run tests, scans, accessibility, DAST, resilience, observability, and evidence gates. | CI/CD evidence pack, security findings, waivers if any, and remediation evidence. |
| 8 | Submit PR/MR for maker-checker review and controlled promotion. | PR/MR AVCI summary, reviewer, approver, rollback/safe-disable plan, and post-promotion monitoring plan. |

# 5. Reference Architecture and Repository Structure

## 5.1 Reference Architecture

The implementation architecture separates presentation, resolution, policy, contracts, MicroFunction execution, workflow, evidence, and runtime telemetry. Each layer must expose explicit ports and adapters and must avoid leaking infrastructure choices into domain or use-case logic.
| Layer | Allowed Responsibility | Must Not Do |
| --- | --- | --- |
| Next.js route shell | Render secure workspace shell, call backend resolver, handle route-level loading/error boundaries, preserve server/client boundaries. | Own business rules, final authorization, policy decisions, or raw sensitive data exposure. |
| Runtime renderer | Map approved component keys to compiled React components and schema-validated props. | Load arbitrary remote components, execute configuration scripts, or render unregistered components. |
| Widget component | Render data, capture user intent, handle safe states, and call generated API clients. | Call unregistered endpoints, embed domain decisions, store secrets, or bypass idempotency. |
| Workspace service | Resolve effective workspace through identity, policy, role/skill/tenant/classification, template, layout, and preference inputs. | Trust frontend-provided authorization or stale cache as authority. |
| Capability binding service | Validate action-to-contract-to-MicroFunction mapping and return allowed action metadata. | Execute business logic directly or bypass workflow approval. |
| MicroFunction runtime | Execute governed backend steps with idempotency, audit, outbox, observability, and rollback profile. | Bypass policy, audit, evidence, retry safety, or error handling. |
| Evidence and observability layer | Capture trace, metric, log, audit, error, policy, and evidence references. | Record secrets, raw PII, raw JWTs, restricted prompts, or high-cardinality unsafe labels. |

## 5.2 Standard Repository Structure
| Repository Area | Required Contents |
| --- | --- |
| apps/web-workspace | Next.js App Router workspace shell, runtime renderer, component library, widget shell, AI panel integration, test fixtures, accessibility tests, visual tests. |
| services/workspace-service | Workspace resolver, policy filtering, template resolution, layout persistence, personalization rules, cache read-through, evidence emission. |
| services/component-registry-service | Component catalog, schema registration, rendering policy, classification ceiling, version state, deprecation metadata. |
| services/capability-binding-service | Action-to-OpenAPI, action-to-workflow, action-to-MicroFunction, idempotency, approval, evidence, and rollback mapping. |
| services/ai-assist-service | Approved AI panel backend APIs, LiteLLM route aliases, guardrail checkpoints, retrieval eligibility, artifact registry integration. |
| libs/aira-contracts | Generated OpenAPI and AsyncAPI clients, JSON Schema, Avro schema, CloudEvents envelope, Problem Details, idempotency contract. |
| libs/aira-ui-schema | Component prop schemas, layout schemas, rendering policy schemas, personalization schemas, and validation helpers. |
| libs/aira-security-client | Policy decision client, safe denial handling, classification helpers, redaction helpers, and no-secret utilities. |
| libs/aira-observability | Browser telemetry initialization, trace propagation, safe logging wrappers, Sentry integration, evidence reference helpers. |
| microfunctions/catalog and runtime | Transaction definitions, standard steps, business MicroFunctions, idempotency profiles, audit profiles, outbox profiles, rollback profiles. |
| contracts/openapi, asyncapi, schemas | Approved API/event contracts, schema compatibility tests, mock generation, generated clients, and contract evidence. |
| config/workspace, rendering, ai, policy | Git-managed configuration projections, seed packages, feature flags, OPA/Rego policies, and runtime activation records. |
| infra/flyway, helm, kubernetes | Flyway migrations, seed loaders, environment manifests, deployment configuration, policy bundles, and runtime toggles. |
| docs/adr, tdl, runbooks | Architecture decisions, technical decision logs, operational runbooks, rollback procedures, and review notes. |

# 6. Implementation Layers and Boundaries

## 6.1 Clean Architecture Boundary Rules

Domain and application use cases must not depend on Next.js, React, database drivers, Redis/Valkey, Kafka clients, OPA clients, workflow SDKs, model SDKs, or browser APIs.

Backend adapters may call PostgreSQL, Redis/Valkey, Kafka, OPA, workflow engines, OpenKM, Sentry, and LiteLLM only through explicit ports.

Frontend components may call only generated API clients and may not import backend domain logic, policy logic, database logic, AI provider SDKs, or direct messaging clients.

Cross-bounded-context writes are prohibited unless mediated by approved API/event contracts and MicroFunction/workflow boundaries.

Framework and infrastructure exceptions require ADR/TDL or waiver and must be visible in PR/MR evidence.

## 6.2 Frontend Authority Boundary
| Rule | Required Treatment |
| --- | --- |
| No browser authorization authority | The browser may hide or disable actions based on resolved metadata, but final allow/deny decisions remain with backend OPA/SBAC and MicroFunction validation. |
| No arbitrary rendering | Runtime renderer must use an allow-list of compiled components from the component registry. Configuration cannot load arbitrary scripts or remote components. |
| No invented endpoints | Widgets must call generated clients from approved OpenAPI contracts only. Any missing endpoint is a contract gap, not a reason for ad hoc calls. |
| No raw sensitive storage | No raw JWTs, refresh tokens, secrets, passwords, raw PII, raw documents, or Restricted prompts in localStorage, browser logs, screenshots, tests, or telemetry. |
| No direct model access | AI panel and widgets must call approved backend APIs. All model traffic routes through approved LiteLLM/gateway/guardrail paths. |
| No direct data authority | Workspace state displayed in the UI is a view. PostgreSQL and approved source records remain authoritative; Redis/Valkey is derivative. |

# 7. Contract-First Development Workflow

Every Dynamic Workspace feature that crosses a boundary must begin with a contract. Contract-first does not only apply to REST APIs; it also applies to events, schemas, component props, action bindings, policy inputs, MicroFunction design records, evidence events, and AI artifacts.
| Contract Type | When Required | Developer Output |
| --- | --- | --- |
| OpenAPI | REST command/query APIs, workspace resolver APIs, action APIs, evidence APIs, AI panel APIs. | Versioned contract, generated TypeScript client, backend interface, mocks, contract tests, Problem Details, idempotency metadata. |
| AsyncAPI | Kafka topics, notifications, config changed events, evidence events, outbox publish events, artifact job events. | Versioned event contract, topic/channel registry, security scheme, correlation headers, retry/DLQ/replay semantics. |
| Avro or JSON Schema | Events, component props, configuration records, evidence records, artifact metadata, seed packages. | Schema compatibility test, semantic version, classification metadata, owner, migration notes. |
| CloudEvents envelope | Cross-service integration events and evidence events. | source, type, subject, id, time, datacontenttype, data schema, trace/correlation/causation references. |
| Component schema | Any new or changed widget/component. | Props schema, rendering policy, accessibility role expectations, classification ceiling, test fixtures. |
| Capability binding record | Any action exposed by a widget, AI panel, or admin builder. | Capability code, generated client method, policy input, MicroFunction transaction code, workflow approval, idempotency profile, audit/evidence profile. |
| Policy input schema | OPA/SBAC decision input changes. | Actor, tenant, branch, role, skill, classification, action, component, transaction, resource, environment, risk tier, and evidence reference fields. |
| Compatibility Rule: Breaking changes require versioned contracts, consumer migration plan, dual-run where applicable, rollback/forward-fix plan, test evidence, and ARB/CAB approval for production-bound consumers. |
| --- |

# 8. Backend Workspace Services

Backend services are the authority for workspace resolution, component visibility, action eligibility, policy filtering, classification ceilings, personalization rules, cache validation, and MicroFunction invocation. They must remain thin at transport adapters and enforce use-case rules in application services behind ports/adapters.
| Service | Required Responsibilities | Required Tests |
| --- | --- | --- |
| Workspace Resolver Service | Resolve workspace using identity, tenant, branch, roles, skills, classification, active templates, layout, feature flags, policy decisions, preferences, and cache state. | Valid user resolution, invalid role denial, missing skill denial, invalid tenant denial, classification mismatch, Redis unavailable fallback, OPA unavailable fail-closed. |
| Component Registry Service | Register component keys, schemas, owners, versions, rendering policies, classification ceilings, evidence profiles, deprecation state, and compatibility metadata. | Schema validation, unregistered component rejection, version state tests, deprecation behavior, classification ceiling tests. |
| Capability Binding Service | Map widget actions to OpenAPI operations, workflows, MicroFunction transactions, idempotency profiles, approval rules, rollback methods, audit profiles, and evidence profiles. | Action mapping, denied capability, missing MicroFunction binding, idempotency behavior, approval-required behavior, safe denial response. |
| Admin Builder Integration | Create, review, approve, activate, roll back, retire, and audit workspace templates and rendering configuration through maker-checker workflow. | Maker-checker, SoD, rollback, activation, cache invalidation, audit/evidence emission. |
| AI Assist Service | Accept multimodal prompts, classify inputs, route through guardrails/model gateway, retrieve eligible context, generate artifacts, and record evidence without direct action authority. | Prompt injection blocking, classification checks, reference citation, artifact registry, no direct execution, guardrail fail-closed. |

# 9. Frontend Renderer and Component Rules

## 9.1 Renderer Requirements

Render only backend-approved screen definitions and allow-listed component keys.

Validate component props against approved schemas before rendering.

Support standard widget states: loading, empty, error, denied, disabled, stale data, success, partial data, requires approval, and offline/degraded.

Use generated API clients only; do not manually construct protected URLs or payloads.

Propagate traceparent or approved correlation headers from browser to gateway where permitted.

Keep client-side state reversible, resettable, bounded, and safe for refresh/back/forward behavior.

Apply responsive behavior and accessibility semantics from Document 59.

Never render sensitive fields unless backend response includes classification, redaction, masking, and authorization metadata.

## 9.2 Rendering Mode Pattern
| Area | Preferred Mode | Notes |
| --- | --- | --- |
| Secure workspace route | SSR by default | Use backend-resolved workspace metadata and avoid sensitive client bootstrapping payloads. |
| Interactive drag, resize, reorder | CSR island | Client-side interaction is allowed only for UX state; persistence requires backend validation and policy. |
| AI prompt input | CSR island with backend API | No browser-side model calls; prompt and artifact governance are backend mediated. |
| Static guidance and help | ISR where non-sensitive | Static pages must not contain user data, secrets, or Restricted content. |
| Stable shell | PPR-ready after maturity | Only after evidence proves no sensitive leakage or authorization bypass. |

## 9.3 Accessibility and UX Requirements

Critical workspace flows must meet the approved WCAG 2.2 AA target or approved internal equivalent.

Keyboard-only navigation must work for menus, widgets, tabs, forms, AI panel, and layout alternatives.

Screen-reader labels, roles, descriptions, focus order, and live-region behavior must be defined for critical components.

Denied and disabled actions must explain safe reason codes without exposing policy internals or sensitive data.

Personalization must be reversible and resettable; mandatory widgets cannot be removed by users.

Visual regression tests must cover critical workspace layouts and approval screens.

# 10. Component Registry, Experience Blocks, and Capability Binding

Components are governed artifacts, not merely UI files. Experience Blocks combine component metadata, schema, rendering policy, capability binding, policy binding, MicroFunction transaction, evidence profile, and test profile. A component cannot be production-active without a registry entry and evidence.
| Registry Field | Required Meaning |
| --- | --- |
| component_key | Stable unique component key used by runtime renderer. |
| owner | Named accountable owner and owning bounded context. |
| version and status | Draft, review-ready, approved, active, deprecated, retired, or revoked. |
| schema_ref | Approved component props schema and validation rules. |
| classification_ceiling | Maximum classification that may be rendered by the component. |
| rendering_policy_ref | Allowed modes, responsive behavior, accessibility expectations, and safe state behavior. |
| capability_bindings | Allowed actions mapped to API operations, workflow approvals, and MicroFunction transactions. |
| policy_binding_ref | OPA/SBAC policy used to decide visibility, field masking, and action allow/deny. |
| evidence_profile_ref | Audit, telemetry, evidence, and retention obligations. |
| rollback_method | Safe disable, rollback, feature flag, component revocation, or forward-fix path. |

## 10.1 Capability Binding Rule
| Rule: A widget action is not implementable until it has a capability code, OpenAPI operation or AsyncAPI event contract, OPA/SBAC input, idempotency key requirement, audit profile, evidence profile, rollback method, and MicroFunction transaction binding where state may change. |
| --- |

# 11. MicroFunction and Workflow Integration

Protected Dynamic Workspace actions must not call business logic directly from the UI, controller, or capability service. The action must invoke a backend use case that coordinates policy, idempotency, audit, workflow, outbox, and MicroFunction execution through standard step families.
| Standard Step Family | Dynamic Workspace Developer Requirement |
| --- | --- |
| STP-RCV | Receive approved REST, event, webhook, file, scheduled, or workspace action trigger through a thin adapter. |
| STP-COR | Create or propagate trace_id, request_id, correlation_id, causation_id, user/session/action identifiers, and evidence_ref. |
| STP-SES | Resolve actor, tenant, branch, role, skill, session, channel, and classification context. |
| STP-RATE | Apply user, tenant, API, workflow, AI, and action-level rate limits or quotas. |
| STP-SEC / STP-CLS | Authenticate, authorize, classify, evaluate OPA/SBAC, and enforce fail-closed behavior. |
| STP-VAL | Validate request schema, component schema, contract compatibility, business preconditions, and version state. |
| STP-IDEMP | Apply idempotency key, duplicate request protection, replay guard, and concurrency control. |
| STP-BUS | Execute the business MicroFunction only after framework controls pass. |
| STP-AUD / STP-OBS | Write audit, trace, metric, log, policy decision, and evidence references safely. |
| STP-OUTBOX | Write outbox event intent for asynchronous publication when integration or notification is required. |
| STP-ERR / STP-COMP | Return safe errors, route to DLQ/retry/replay or compensation where applicable, and record remediation evidence. |

## 11.1 Workflow Approval Interface

High-impact, low-confidence, Restricted, production-impacting, destructive, privileged, or policy-exception actions must route to human approval.

Flowable or approved workflow abstractions may manage human approvals; Temporal or approved durable orchestration may manage long-running machine workflows.

The UI may present approval tasks and capture intent, but the workflow engine and backend services remain authoritative.

Requester, checker, approver, deployer, and auditor separation must be preserved.

# 12. Configuration, Feature Flags, Runtime Cache, and Synchronization

Dynamic Workspace implementation depends on deterministic configuration and cache behavior. PostgreSQL and Git-managed configuration remain authoritative. Redis/Valkey accelerates resolved views only and must never become the source of truth.
| Area | Required Developer Treatment |
| --- | --- |
| Configuration source | Workspace templates, screen templates, layout definitions, component registry, capability bindings, AI capability bindings, feature flags, policy bindings, and evidence profiles are Git/Flyway/config-importer governed. |
| Runtime cache | Cache only derivative views such as resolved workspace, component metadata, policy-filtered layout, and feature-flag snapshots. Never cache raw secrets, raw PII, raw documents, tokens, or Restricted prompts. |
| Cache keys | Use tenant, workspace, component, version, policy hash, layout hash, and classification-aware keys. Include hash/version to prevent stale privilege. |
| Invalidation | Invalidate on template, component, schema, capability, policy, role assignment, feature flag, preference, evidence profile, or AI capability change. |
| Redis unavailable | Resolver must fall back to PostgreSQL where safe and emit degraded metric/evidence. Correctness must not depend on Redis. |
| PostgreSQL unavailable | Protected actions fail closed. UI shows safe degraded state and must not serve stale privileged actions. |
| Runtime toggles | Debug verbosity, trace sampling, frontend diagnostics, Sentry sampling, and non-critical logs may be adjusted by approved runtime configuration. Audit, policy decisions, security denials, evidence, and protected action telemetry must not be disabled. |
| Rollback | Feature flag disablement, previous active version reactivation, cache invalidation, smoke tests, incident evidence, and improvement backlog entry are mandatory for failed activation. |

# 13. API, Event, Outbox, DLQ, and Replay Implementation

## 13.1 REST API Rules

All workspace APIs use OpenAPI contracts, generated clients, standardized errors, idempotency headers where mutating, pagination and filtering rules where listing, and correlation headers.

Controllers remain thin adapters. They do not own business logic, authorization logic, database writes, Kafka publishes, or workflow decisions.

Safe Problem Details responses must avoid secrets, raw PII, policy internals, stack traces, and sensitive classification details.

## 13.2 Event Rules
| Event Area | Required Rule |
| --- | --- |
| AsyncAPI | Kafka topics, evidence events, config.changed events, artifact events, and notification events must be described in AsyncAPI. |
| Avro / schema registry | Event payloads use Avro or approved schema format with compatibility checks and versioned evolution. |
| CloudEvents | Integration events carry standard id, source, type, subject, time, datacontenttype, data schema, correlation, causation, and trace references. |
| Transactional outbox | State-changing transactions that publish events write an outbox record in the same transaction as the authoritative state change. |
| Idempotent consumers | Consumers maintain processed-event registry or equivalent deduplication by event id, source, subject, version, and consumer group. |
| DLQ and replay | Failed events route to DLQ with reason, classification, retry count, and evidence reference. Replay must be controlled, idempotent, auditable, and authorized. |
| Schema evolution | Breaking changes require versioning, compatibility tests, consumer migration, and rollback/forward-fix plan. |

# 14. Security, OPA/SBAC, Secrets Hygiene, and Abuse Cases

Dynamic Workspace security must be built into implementation, not added after a screen is working. Developers must implement secure APIs, classification-aware rendering, tenant isolation, secrets hygiene, CSP, safe errors, and policy-as-code before PR/MR acceptance.
| Security Area | Mandatory Implementation Control |
| --- | --- |
| Identity and session | Use approved identity/session context. Do not store raw tokens in localStorage. Do not expose refresh tokens, raw JWTs, passwords, or secrets in UI, logs, traces, screenshots, or tests. |
| OPA/SBAC | All protected visibility, field masking, action eligibility, template authoring, approval, and AI action proposal decisions require OPA/SBAC inputs and evidence. |
| Classification | Responses include classification and redaction metadata. The UI must not render higher classification than allowed by policy. |
| Tenant and branch isolation | Every query, action, cache key, policy decision, telemetry record, and evidence record must include safe tenant/branch or organizational scope where applicable. |
| Secure APIs | Use generated clients, CSRF/CORS controls, rate limits, schema validation, safe errors, and idempotency for mutating actions. |
| Secrets hygiene | Use Vault or approved secrets abstraction. No secrets in code, .env committed files, frontend bundles, screenshots, test fixtures, prompts, or telemetry. |
| Abuse cases | Test prompt injection, unauthorized widget activation, stale policy cache, IDOR, replay/double submit, cross-tenant access, unsafe HTML, excessive telemetry, and unauthorized AI action proposal. |
| Authenticated DAST | DAST must run against approved DEV/TEST instances with synthetic data, scoped credentials, safe scan configuration, and remediation evidence. |

# 15. Observability, Runtime Telemetry, Audit, and Evidence

All critical flows must emit enough evidence to reconstruct who did what, when, why, under which policy, using which component, against which backend capability, with which outcome. Telemetry must be useful, safe, redacted, and classifiable.
| Signal | Required Treatment |
| --- | --- |
| Traces | Propagate trace_id/span_id from browser through gateway, workspace resolver, policy engine, backend API, MicroFunction runtime, outbox, consumer, and AI service where applicable. |
| Metrics | Track workspace load latency, resolver latency, cache hit/miss, policy deny rate, widget action success/failure, AI response latency, outbox lag, DLQ count, and accessibility/test quality trends. |
| Logs | Use structured logging through approved backend logging, including Log4j2 where applicable. Do not log secrets, raw PII, raw tokens, raw documents, prompts with Confidential/Restricted content, or high-cardinality unsafe labels. |
| Error monitoring | Use Sentry or approved equivalent for frontend/backend error grouping, release correlation, source maps where safe, and remediation tracking. |
| Logs and traces backends | Loki, Tempo, Grafana, and approved observability tools must support trace reconstruction, policy denial analysis, slow widget analysis, and evidence completeness. |
| Audit events | Audit workspace resolved, component rendered, policy filtered, layout changed, action invoked, action denied, template published, AI prompt submitted, artifact generated, and cache invalidated events. |
| Evidence records | Every protected action links owner, source_ref, verification evidence, classification, principle impact, reversibility, and improvement path. |

## 15.1 Forbidden Telemetry Fields

Developers must not emit passwords, tokens, raw JWTs, secrets, raw PII, account numbers, raw documents, raw KYC files, raw prompts containing Confidential or Restricted data, embeddings, payment card data, private keys, unrestricted customer payloads, or high-cardinality sensitive identifiers as metric labels.

# 16. Concurrency, Heavy Transaction, Idempotency, and Resilience Lab

Dynamic Workspace must behave safely under duplicate clicks, retries, stale screens, long-running transactions, heavy loads, browser refresh, network loss, partial failure, cache loss, policy change, and replay. Developers must design both backend behavior and user experience for failure-aware execution.
| Concern | Developer Requirement |
| --- | --- |
| Duplicate click / double submit | Use idempotency keys, disabled pending states, server-side duplicate protection, and safe replay response. |
| Stale screen / stale policy | Backend validates current policy and version before action. UI shows stale state and refreshes authoritative view. |
| Heavy transaction | Route long-running work through workflow/orchestration and asynchronous status APIs. Do not block browser as authority. |
| Concurrent layout changes | Use layout version, hash, optimistic concurrency, conflict response, reset option, and audit trail. |
| Outbox lag | Show safe pending state if publication is asynchronous; do not claim final downstream completion until confirmed. |
| Retry and replay | Retries and replay must be idempotent, authorized, audited, and linked to evidence. |
| Circuit breaker / fallback | Backend dependencies use timeouts, retries, circuit breakers, bulkheads, fallback, and safe degradation. UI shows clear degraded state. |
| DLQ and recovery | Failures route to DLQ or incident workflow with classification, owner, trace, and remediation evidence. |

# 17. DevSecOps Pipeline, GitNexus, and Evidence Pack

Every material Dynamic Workspace change must pass a repeatable pipeline. The pipeline is allowed to reject a change even if the screen works. Evidence completeness, security posture, accessibility, observability, architecture boundaries, and reversibility are part of the definition of done.
| Gate | Minimum Required Result |
| --- | --- |
| Build and type check | Frontend and backend build, generated clients compile, and TypeScript/Java toolchain versions match Golden Source. |
| Lint and format | Frontend, backend, contracts, schemas, and policies pass approved lint/format rules. |
| Unit and component tests | Widget, renderer, resolver, policy client, generated client, and backend use-case tests pass. |
| Contract tests | OpenAPI, AsyncAPI, Avro/JSON Schema, CloudEvents, Problem Details, idempotency, compatibility, and generated client tests pass. |
| Architecture fitness | No frontend authority, no direct provider SDKs, no direct database/Kafka/model calls in prohibited layers, no unregistered component rendering, no missing MicroFunction binding. |
| Security gates | SAST, SCA, secrets scan, dependency scan, container scan, OPA/Conftest, CSP/security header checks, and authenticated DAST pass or have approved waivers. |
| Accessibility and visual gates | Critical widgets pass keyboard, screen-reader, ARIA, focus, responsive, visual regression, and E2E tests. |
| GitNexus impact analysis | Read-only impact analysis identifies affected components, contracts, tests, policies, MicroFunctions, APIs, and risk areas. GitNexus remains derivative and cannot approve, merge, or deploy. |
| Evidence pack | PR/MR AVCI summary, test reports, scan reports, policy decisions, GitNexus report, screenshots, trace proof, rollback plan, and known limitations are linked. |

# 18. Testing and Architecture Fitness Functions

## 18.1 Minimum Test Set Per Workspace Capability

Authorizes valid user and denies invalid role, missing skill, invalid tenant or branch, and classification mismatch.

Validates component schema, OpenAPI/AsyncAPI contracts, idempotency, and safe error responses.

Maps protected action to backend capability, OPA policy, MicroFunction transaction, audit event, and evidence record.

Rejects unregistered component keys, unregistered endpoints, unauthorized widgets, unsafe HTML, and frontend authority bypass.

Handles Redis unavailable, PostgreSQL unavailable, OPA unavailable, stale layout hash, template supersession, and policy change.

Supports accessibility, responsive layout, Playwright E2E happy/deny paths, and visual regression for critical screens.

Verifies no secrets, raw tokens, raw PII, or Restricted content appear in browser storage, logs, traces, screenshots, prompts, or test artifacts.

## 18.2 Architecture Fitness Functions
| Fitness Function | Reject If |
| --- | --- |
| No frontend business authority | Widget contains final approval, payment, policy, access, or domain decision logic. |
| No direct provider SDK | Frontend or backend imports direct AI provider SDK outside approved gateway/orchestration boundary. |
| No invented endpoints | Component calls endpoint not generated from approved OpenAPI contract. |
| Component allow-list | Runtime renderer can render an unregistered component key. |
| Policy required | Resolver returns component or action without OPA/SBAC policy evaluation. |
| Cache not authority | Test passes only when Redis/Valkey is available or uses stale cache for privileged action. |
| MicroFunction binding | Mutating widget action lacks transaction binding, idempotency profile, audit profile, or evidence profile. |
| Evidence required | Protected action lacks audit/evidence reference. |
| Accessibility required | Critical component fails keyboard, focus, label, or screen-reader checks without approved waiver. |
| Classification required | Confidential/Restricted data renders without classification and redaction metadata. |

# 19. Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop

Auto-Heal, Auto-Learn, and Auto-Improve support Dynamic Workspace quality but must not silently mutate production, weaken policy, or bypass review. The loop produces candidate evidence, not authority.
| Loop Stage | Required Treatment |
| --- | --- |
| Issue detection | Detect UX errors, policy denial spikes, accessibility failures, slow widgets, cache drift, DLQ growth, failed tests, security findings, Sentry error groups, and user feedback. |
| Evidence retrieval | Retrieve only eligible logs, traces, metrics, GitNexus impact, contracts, code map, test results, policy decisions, screenshots, and incident records. |
| Candidate proposal | Generate candidate fix, test, policy update, runbook update, learning artifact, or backlog item in a branch/sandbox only. |
| Impact analysis | Assess affected contracts, components, MicroFunctions, policies, cache, schemas, APIs, events, tests, security posture, and rollback path. |
| Human approval | Named checker and approver review the candidate. High-risk or production-impacting changes require ARB/CAB/Security review. |
| Validation | Run tests, scans, DAST where applicable, accessibility, visual regression, contract compatibility, observability, and resilience checks. |
| Promotion and learning | Promote only through PR/MR and CI/CD. Learning artifacts become reviewed knowledge, not hidden model memory. |
| Closure | Evidence pack records root cause, fix, tests, rollout, rollback readiness, residual risk, and improvement backlog linkage. |

# 20. Developer Checklists and Definition of Done

## 20.1 Developer Pre-Implementation Checklist

Ticket, owner, classification, bounded context, workspace, screen, component, capability, API/event, policy, and MicroFunction are identified.

Relevant ADR/TDL or waiver is linked when architecture, policy, data, AI, or infrastructure behavior changes.

Contract-first outputs are complete or explicitly not applicable.

Configuration, feature flag, registry, cache, and rollback impacts are known.

Security, classification, tenant isolation, secrets, OPA/SBAC, and abuse cases are understood.

Observability, evidence, test, DAST, accessibility, and resilience requirements are planned.

## 20.2 Definition of Done

Component schema, catalog registration, rendering policy, capability binding, policy binding, and evidence profile are complete.

Frontend uses generated clients only and cannot render unauthorized or unregistered components.

Backend resolver validates identity, tenant, skills, classification, policy, feature flags, template version, and cache state.

Protected actions route through approved backend use case, OPA/SBAC, idempotency, audit, outbox, and MicroFunction transaction.

OpenAPI/AsyncAPI/schema compatibility, OPA tests, unit tests, component tests, E2E tests, accessibility tests, visual tests, and resilience tests pass.

SAST, SCA, secrets scan, authenticated DAST, dependency/container scan, and policy-as-code checks pass or have approved waivers.

Telemetry and evidence records support trace reconstruction and do not leak forbidden fields.

PR/MR AVCI summary, GitNexus impact, rollback/safe-disable plan, and post-promotion monitoring plan are complete.

# 21. RACI
| Activity | Owner | Reviewer / Checker | Approver |
| --- | --- | --- | --- |
| Workspace feature design | Product Owner / Solutions Architect | Enterprise Architecture; Security; QA/SDET | Architecture Board when material |
| Frontend component implementation | Frontend Developer | Frontend Lead; QA/SDET; Security | Software Development Lead |
| Backend resolver or capability service | Backend Developer | Software Development Lead; Security; DBA where data impact exists | Solutions Architecture Office |
| MicroFunction transaction binding | Backend Developer / MicroFunction Owner | Enterprise Architecture; QA/SDET; Security | Architecture Board or Change Owner when material |
| Contracts and schemas | API Owner / Developer | API Architecture; QA/SDET; Consumer Owner | Architecture Board for breaking changes |
| OPA/SBAC policies | Security Architecture | Software Development Lead; QA/SDET | Security Governance |
| Flyway migrations and seed packages | DBA / Backend Developer | Data Governance; QA/SDET | DBA Lead / CAB for production |
| CI/CD and evidence pack | DevSecOps Lead | Security; QA/SDET; Internal Audit | CAB for production-bound promotion |
| Runtime operations and monitoring | SRE / Operations | DevSecOps; Security; Product Owner | Service Owner |
| AI-assisted generation outputs | System Builder Owner / Developer | Human Checker; Security; Architecture | Named Approver by risk tier |

# 22. Acceptance Criteria
| Acceptance Area | Pass Condition |
| --- | --- |
| Architecture boundary | No frontend authority, no direct model/database/Kafka calls in prohibited layers, no business logic in controllers, no cross-context writes. |
| Contracts | OpenAPI/AsyncAPI/schemas/CloudEvents/component schemas are approved, validated, generated, tested, and versioned. |
| MicroFunction integration | All protected actions have transaction, idempotency, audit, outbox, evidence, rollback, and policy references. |
| Security | OPA/SBAC tests pass; secrets hygiene is proven; DAST/SAST/SCA/secrets scans pass or have approved waivers; no sensitive telemetry. |
| Cache behavior | Redis/Valkey loss does not break correctness; PostgreSQL loss fails safely; cache invalidation and rebuild are proven. |
| Observability | Trace, metric, log, audit, Sentry/error monitoring, Loki/Tempo/Grafana dashboard evidence, and trace reconstruction proof are available. |
| Accessibility and UX | Critical flows pass keyboard, screen-reader, focus, responsive, visual, and E2E checks. |
| Resilience | Duplicate, retry, stale, concurrent, outbox, DLQ, replay, degraded, and rollback behavior are tested. |
| Evidence | PR/MR contains AVCI summary, evidence pack, GitNexus report, tests, scans, policy evidence, rollback plan, and known limitations. |
| Human approval | High-impact, production-bound, Restricted, destructive, or policy-exception changes have named approval and separation of duties. |

# 23. Open Reconciliation Items

The following items should remain visible in Register 00D or the active reconciliation register until formally resolved.
| Item | Severity | Recommended Treatment |
| --- | --- | --- |
| Dynamic Workspace document family v1.0 to v1.1 propagation | Medium | After Documents 46 through 61 are revised, update master index, cross-reference matrix, and source pack manifest. |
| 41B / 44 System Builder overlap | Medium | Continue treating 41B as System Builder authority and route 44/44A references through controlled reconciliation. |
| Older references to Java 21 or earlier technology baselines | Medium | Use current AIRA baseline unless explicit waiver exists. Document exceptions in PR/MR evidence. |
| Duplicate numbering and source-pack cleanup | Low to Medium | Preserve suffix hierarchy and update packer/regeneration runbook during next source pack rebuild. |
| Document 47 dependency update | Medium | Update companion references in 48, 49, 50, 51, 52, 56, and 57 after revised 47 is accepted. |

# 24. Review Queue Control Register
| Sequence | File Name | Pack | Current Version | Recommended Version | Review Status | Priority | Dependency | Action Required | Next Step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | AIRA_47_Dynamic_Workspace_Developer_Implementation_Guide_v1.1_Revised.docx | Pack 14 | v1.0 | v1.1 Revised | Completed in this output | High | 46, 59, 60, 61 | Adopt after review | Use as developer execution guide for Dynamic Workspace implementation. |
| 2 | 48-AIRA_Dynamic_Workspace_Database_and_Flyway_Migration_Specification_v1.0.docx | Pack 14 | v1.0 | v1.1 Revised | Recommended next | High | 46, 47, 16/16A/16B | Review and align | Translate workspace configuration, registry, policy, evidence, and personalization needs into Flyway-governed schema. |
| 3 | 49-AIRA_Dynamic_Workspace_API_and_OpenAPI_Contract_Specification_v1.0.docx | Pack 14 | v1.0 | v1.1 Revised | Queued | High | 47, 48, 15/15A | Review after 48 | Align APIs, events, OpenAPI, AsyncAPI, CloudEvents, idempotency, and generated clients. |
| 4 | 50-AIRA_Dynamic_Workspace_Component_and_Widget_Development_Standard_v1.0.docx | Pack 14 | v1.0 | v1.1 Revised | Queued | High | 47, 49, 59 | Review after 49 | Align component standards, widget states, accessibility, registry, tests, and evidence. |
| 5 | 51-AIRA_Dynamic_Workspace_Security_RBAC_SBAC_ABAC_and_OPA_Policy_Specification_v1.0.docx | Pack 14 | v1.0 | v1.1 Revised | Queued | High | 47, 49, 50 | Review after 50 | Strengthen OPA/SBAC, classification, abuse cases, secure APIs, and DAST. |
| 6 | 52-AIRA_Dynamic_Workspace_Testing_and_Architecture_Fitness_Function_Standard_v1.0.docx | Pack 14 | v1.0 | v1.1 Revised | Queued | High | 47, 50, 51, 60 | Review after 51 | Consolidate testing, architecture fitness, accessibility, resilience, and evidence gates. |

# 25. AVCI Compliance Summary
| AVCI Property | Compliance Evidence |
| --- | --- |
| Attributable | Document owner, co-owners, target audience, source baseline, companion documents, RACI, component owner, capability owner, and PR/MR attribution are defined. |
| Verifiable | Contract tests, unit tests, component tests, E2E tests, accessibility tests, visual tests, OPA tests, DAST/SAST/SCA/secrets scans, GitNexus impact, telemetry validation, and evidence pack gates prove behavior. |
| Classifiable | Workspace data, component props, telemetry, prompts, artifacts, policies, cache entries, evidence records, and test data carry classification and redaction rules. |
| Improvable | Runtime telemetry, incidents, Sentry errors, DLQ events, accessibility findings, security findings, user feedback, and GitNexus analysis feed controlled Auto-Heal, Auto-Learn, and Auto-Improve candidate loops. |

# Appendix A. PR/MR AVCI Summary Template
| Field | Required Entry |
| --- | --- |
| Owner / ticket / ADR / TDL | Named owner, source ticket, affected decision records, and waiver references if any. |
| Change type | Workspace, screen, component, API, event, policy, MicroFunction, config, cache, AI panel, evidence, or test. |
| Affected artifacts | Component keys, workspace codes, screen codes, capability codes, API operations, topics, schemas, MicroFunction transactions, policies. |
| Classification impact | Data classes touched, redaction/masking behavior, retention, and retrieval eligibility. |
| Security impact | OPA/SBAC decisions, secrets hygiene, abuse cases, DAST/SAST/SCA/secrets scan result. |
| Contract impact | OpenAPI/AsyncAPI/schema compatibility, generated clients, backward compatibility, migration plan. |
| MicroFunction impact | Transaction code, idempotency profile, outbox profile, audit profile, rollback/compensation method. |
| Observability impact | Trace, metric, log, audit, evidence, Sentry, Loki, Tempo, Grafana, alerting, and trace reconstruction proof. |
| Accessibility impact | Keyboard, screen reader, focus, responsive, visual regression, and UX walkthrough evidence. |
| Resilience impact | Duplicate, retry, stale, concurrent, heavy-load, DLQ, replay, fallback, and cache-loss behavior evidence. |
| GitNexus impact | Read-only code map, affected tests/contracts/components/policies/MicroFunctions, and risk notes. |
| Rollback / safe disable | Feature flag, previous active version, cache invalidation, rollback test, forward-fix or compensation path. |
| Human checker / approver | Named reviewer, checker, approver, and approval evidence. |

# Appendix B. External Alignment Register
| External Reference | Use in this Guide |
| --- | --- |
| OpenAPI Specification 3.2.0 or AIRA-approved supported version | HTTP API contract description, generated clients, documentation, and contract validation. |
| AsyncAPI Specification 3.1.0 or AIRA-approved supported version | Kafka/event-driven contract description, channel/topic governance, message validation, and consumer testing. |
| CloudEvents | Interoperable event envelope and correlation metadata for integration and evidence events. |
| OpenTelemetry Semantic Conventions | Trace, metric, log, resource, and attribute naming consistency. |
| OWASP ASVS 5.0.0 or AIRA-approved verification baseline | Secure web application and API verification requirements. |
| WCAG 2.2 AA or AIRA-approved accessibility target | Accessibility acceptance for keyboard, screen reader, focus, contrast, reduced motion, and responsive UX. |
| SLSA and SBOM/provenance practices | Supply-chain evidence and build provenance for CI/CD evidence packs. |

# Appendix C. Anti-Patterns
| Anti-Pattern | Required Correction |
| --- | --- |
| Frontend decides authorization | Move decision to backend OPA/SBAC and return safe resolved metadata. |
| Widget calls unregistered endpoint | Create/update OpenAPI contract and generated client. |
| Component renders raw server payload | Validate schema, apply classification, masking, and rendering policy. |
| Redis treated as truth | Read authoritative state from PostgreSQL or fail safely. Rebuild cache from truth. |
| Direct Kafka publish from controller or widget | Use backend use case, transaction, outbox, and publisher. |
| AI panel executes action directly | Convert to action proposal, policy decision, workflow/MicroFunction path, and human approval when required. |
| Working screen without tests or evidence | Reject PR/MR until tests, scans, policy, observability, accessibility, rollback, and evidence pack are complete. |
| Auto-fix silently changes production | Convert to candidate proposal, branch, tests, review, approval, and controlled promotion. |

