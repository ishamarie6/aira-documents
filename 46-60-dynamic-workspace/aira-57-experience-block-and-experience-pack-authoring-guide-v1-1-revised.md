---
title: "Experience Block and Experience Pack Authoring Guide"
doc_id: "AIRA-57"
version: "v1.1"
status: "revised"
category: "Dynamic workspace"
source_docx: "AIRA_57_Experience_Block_and_Experience_Pack_Authoring_Guide_v1.1_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 46-60-dynamic-workspace
  - revised
  - aira-57
---



# Experience Block and Experience Pack Authoring Guide



AIRA

AI-Native Enterprise Platform

Experience Block and Experience Pack Authoring Guide

Reusable Domain Experiences | Dynamic Workspace Assembly | MicroFunction-Backed Capabilities | Evidence by Construction | AVCI Always

AIRA-DOC-057 | Version v1.1 Revised | INTERNAL CONFIDENTIAL
| Mandatory Practice Statement | AIRA Experience Blocks and Experience Packs may accelerate delivery only when they remain governed, reusable, versioned, policy-filtered, contract-bound, MicroFunction-backed, observable, reversible, and evidence-producing. An Experience Block is not a free-form widget, and an Experience Pack is not an uncontrolled low-code application. Blocks and packs render approved user experiences; backend APIs, MicroFunctions, workflow engines, OPA/SBAC policy, PostgreSQL/Flyway configuration, and human approval remain authoritative. |
| --- | --- |

# Document Control
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-057 |
| Canonical Filename | 57-AIRA_Experience_Block_and_Experience_Pack_Authoring_Guide_v1.1_Revised.docx |
| Version | v1.1 - Revised Dynamic Workspace, MicroFunction, API, Security, Observability, DevSecOps, and AI Governance Alignment |
| Status | Draft for Architecture Board, CAB, Dynamic Workspace, Product, Security, DevSecOps, QA/SDET, AI Governance, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Product Owner; Frontend Lead; Backend Lead; DevSecOps Lead; Security Architecture; QA/SDET; Platform Engineering; AI Governance; Internal Audit |
| Supersedes | 57-AIRA_Experience_Block_and_Experience_Pack_Authoring_Guide_v1.0 |
| Primary Parents | 42 Composable Experience Framework; 41 Dynamic User Workspace Framework; 12A Dynamic Frontend Workspace UI Generation and UX Governance Standard |
| Direct Companions | 46 Configuration and Runtime Cache; 48 Database/Flyway; 49 API/OpenAPI; 50 Component and Widget Development; 51 Security/OPA/SBAC/ABAC; 52 Testing/Fitness; 53 Observability/Audit/Evidence; 54 Admin Builder; 55 Configuration Seeder; 56 Frontend Reference; 58 Multimodal AI Governance; 59 UX/Accessibility; 60 DevSecOps Evidence; 61 AI-Assisted Dynamic Workspace and System Builder |
| External Alignment Checked | WCAG 2.2/WAI; Next.js App Router Server/Client Component guidance; React Rules of Hooks and component purity guidance; OpenTelemetry Semantic Conventions; OPA/Rego; OWASP ASVS; NIST SSDF; SLSA v1.2 |

# Static Table of Contents

Executive Summary and v1.1 Revision Verdict

Purpose, Scope, and Authority

Experience Block Definition and Metadata

Experience Pack Definition, Structure, and Compatibility

Authoring Procedure and Governance Gates

Dynamic Workspace, MicroFunction, API, Event, and Data Binding Rules

Security, Classification, OPA/SBAC, AI, and Runtime Toggle Controls

Testing, Observability, DevSecOps Evidence, and GitNexus Requirements

Mortgage Experience Pack Reference Pattern

Lifecycle, Versioning, Reuse, RACI, Acceptance Criteria, and AVCI Summary

# 1. Executive Summary and v1.1 Revision Verdict

This revised guide strengthens the original Experience Block and Experience Pack authoring guide after the completion of the Dynamic Workspace database, API, component, security, testing, observability, Admin Builder, runtime synchronization, and frontend reference implementation updates. It keeps the v1.0 rule - build once as governed blocks and assemble many systems through approved packs - while making the authoring path execution-ready for teams, System Builder Lite, Admin Builder, and future AIRA domain packages.

Experience Blocks are governed user-experience and business-interaction building blocks. Experience Packs are domain-level compositions of blocks, screens, templates, workflows, APIs, MicroFunctions, AI capabilities, policies, rendering policies, runtime toggles, evidence profiles, and acceptance criteria. They enable reuse, but they do not move authority to the browser, to low-code metadata, or to AI-generated artifacts.
| v1.1 Outcome | Required Result |
| --- | --- |
| Governed reuse | Blocks and packs are reusable only when they have owner, bounded context, version, schema, policy binding, evidence profile, test pack, and rollback/deactivation path. |
| Backend authority | Blocks render and request; backend APIs, MicroFunctions, workflow engines, OPA/SBAC, database constraints, and approvals decide and execute. |
| Configuration-first | Teams reuse existing blocks, components, contracts, policies, and MicroFunctions before writing custom code. |
| Secure composition | Every block declares classification ceiling, role/skill/attribute policy, rendering eligibility, telemetry rules, and forbidden-data handling. |
| Evidence by construction | Every block action, AI guidance output, pack activation, rollback, user feedback, test, and production promotion must produce AVCI evidence. |

# 2. Purpose, Scope, and Authority
| Area | Authoring Treatment |
| --- | --- |
| Purpose | Define how teams author, review, test, approve, register, activate, monitor, improve, supersede, and retire AIRA Experience Blocks and Experience Packs. |
| In Scope | Reusable blocks; domain packs; screen packs; widget packs; component contracts; API/MicroFunction/workflow bindings; AI capability bindings; rendering policies; evidence profiles; OPA/SBAC controls; runtime toggles; test packs; Admin Builder lifecycle; System Builder candidate generation. |
| Out of Scope | Arbitrary JavaScript, direct database calls, direct model-provider calls, unregistered APIs, browser-owned authorization, uncontrolled SQL, self-activating AI output, production mutation outside CAB/CI/CD, and non-evidence-producing low-code changes. |
| Authority | Composable Experience Framework and Dynamic Workspace standards govern composition; MicroFunction, API, Database/Flyway, Security, Observability, CI/CD, Change/CAB, and AI Governance standards govern execution and promotion. |

# 3. Experience Block Definition and Metadata

An Experience Block is a reusable, governed unit of user experience that combines a frontend component, component schema, rendering policy, capability binding, API contract, MicroFunction transaction or read capability, workflow binding where applicable, OPA/SBAC policy binding, observability profile, evidence profile, and lifecycle controls.
| Required Metadata | Mandatory Meaning |
| --- | --- |
| block_code | Unique stable identifier, e.g., MORTGAGE_APPLICATION_BLOCK. |
| block_version | Semantic version; activated versions are immutable and superseded by new versions. |
| bounded_context | Owning domain such as mortgage-servicing, identity-access, document-management, or compliance. |
| component_key | Allow-listed frontend component registry key and version. |
| props_schema_ref | JSON/Zod schema or OpenAPI-linked schema for all block props and data contracts. |
| rendering_policy_code | SSR/CSR island/ISR/PPR/streaming/cache policy and sensitivity rules. |
| capability_code | Backend capability binding and allowed action list returned from backend authority. |
| api_microfunction_refs | Approved API contracts, generated clients, and MicroFunction transaction or query capability. |
| workflow_policy_ref | Temporal/Flowable binding and RBAC/SBAC/ABAC/OPA policy inputs where applicable. |
| classification_ceiling | Maximum classification the block may render or process. |
| ai_capability_binding_ref | Optional AI capability, prompt template, guardrail, LiteLLM route, and output-mode binding. |
| evidence_profile_code | Audit, trace, metric, log, evidence, retention, and dashboard profile. |
| rollback_policy | Disable, revert to previous version, fallback block, hide action, feature flag, or pack rollback. |

# 4. Experience Pack Definition, Structure, and Compatibility

An Experience Pack is a governed collection of Experience Blocks, workspace templates, screen templates, widgets, workflows, APIs, MicroFunctions, AI capabilities, OPA policies, rendering policies, data requirements, evidence profiles, test packs, and activation rules for a domain such as Mortgage, KYC, Payments, Collections, CRM, Document Management, or Compliance.
| Pack Type | Examples |
| --- | --- |
| Domain Pack | Mortgage Experience Pack, Collections Pack, Document Management Pack, KYC Operations Pack. |
| Workflow Pack | Approval queue, KYC review, title release, exception handling, rework, escalation. |
| Screen Pack | Dashboard, application form, document viewer, task inbox, evidence timeline. |
| Widget Pack | KPI cards, charts, forms, document upload/viewer, AI guide, timeline, approval actions. |
| Admin Pack | User management, configuration, template review, runtime toggle view, evidence dashboard. |
| AI Pack | AI guidance, artifact generation, checklist generation, evidence summarization, proposal drafting under guardrails. |
| Compatibility Declaration | Required Meaning |
| --- | --- |
| required_platform_version | Minimum AIRA platform, Dynamic Workspace, MicroFunction, API, and security baseline. |
| required_component_versions | Compatible frontend component keys and versions. |
| required_contract_versions | OpenAPI/AsyncAPI/Avro/CloudEvents versions and generated client hash. |
| required_microfunction_catalog_version | Transaction catalog and step catalog versions. |
| required_opa_bundle_version | Policy bundle, SBAC skill catalog, ABAC attributes, and test result. |
| required_db_migration_version | Flyway migration chain and seed/config package version. |
| required_observability_profile | Trace/log/metric/audit/evidence schema and forbidden telemetry checks. |
| activation_scope | Tenant, branch, role, product, environment, user cohort, feature flag, and rollback boundary. |

# 5. Authoring Procedure and Governance Gates

Capture business intent, owner, source, bounded context, classification, target users, and acceptance criteria.

Search the Experience Block Registry and Experience Pack Registry before creating anything new; reuse or extend existing blocks where practical.

Determine whether the requested capability is display-only, action-capable, workflow-backed, document-backed, AI-assisted, evidence-viewing, or administrative.

Create or update the block schema and bind it only to approved component registry entries and generated API clients.

Bind all business or mutating actions to approved APIs, MicroFunction transactions, workflow tasks, idempotency profiles, and safe response contracts.

Define OPA/RBAC/SBAC/ABAC policy input, classification ceiling, field visibility, action visibility, runtime toggle eligibility, and audit profile.

Define rendering policy for SSR, CSR island, ISR, PPR, streaming, cache behavior, no-store rules, and sensitive-data constraints.

Define AI capability binding only through approved prompt templates, LiteLLM model routes, guardrails, retrieval policies, artifact profiles, and human approval rules.

Prepare tests: unit, component, contract, accessibility, OPA policy, E2E, resilience, visual regression, telemetry, and security tests.

Register the block or pack through Admin Builder and promote only after maker-checker review, CI/CD evidence, GitNexus impact, and required approvals.
| Gate | Required Evidence |
| --- | --- |
| Draft | Author/Product/Developer drafts block or pack proposal with metadata, schema, policy, and evidence intent. |
| Analyze | Architect, Security, DBA, DevSecOps, and QA review reuse, bounded context, contract, data, policy, and test impact. |
| Validate | CI/CD validates schema, contracts, generated clients, policy tests, accessibility, security, telemetry, and architecture fitness. |
| Approve | Product Owner, Security, Architecture, and CAB/ARB where applicable approve activation scope and rollback path. |
| Activate | Admin Builder or governed seeder activates versioned configuration with audit and cache invalidation evidence. |
| Observe | Dashboards track usage, denials, errors, latency, slow widgets, AI guardrails, and evidence completeness. |

# 6. Dynamic Workspace, MicroFunction, API, Event, and Data Binding Rules
| Binding Area | Mandatory Rule |
| --- | --- |
| Dynamic Workspace | Blocks are rendered only when returned by the backend workspace resolver after policy filtering. UI metadata must never invent allowed actions, fields, routes, or endpoints. |
| MicroFunction Runtime | Mutating or business-significant actions bind to approved MicroFunction transactions with idempotency, audit, outbox, error policy, observability, and compensation metadata. |
| OpenAPI | REST actions use approved OpenAPI contracts and generated clients. Frontend code must not build raw paths, hidden payload fields, or bypass safe response envelopes. |
| AsyncAPI / Kafka / Avro / CloudEvents | Event-producing or event-consuming blocks must reference approved event contracts, schemas, topics, CloudEvents attributes, outbox/inbox, DLQ/replay, and idempotent consumer profiles. |
| PostgreSQL / Flyway | Block and pack registries, assignments, rendering policies, capability bindings, evidence profiles, and seed configuration are Flyway-governed Tier-0 or Git-promoted configuration artifacts. |
| Redis / Valkey | Cache may store only derivative resolved workspace, block, policy, and capability views with TTL, invalidation, hash, and no-sensitive-payload controls. |
| Runtime Toggles | Feature, block, AI panel, telemetry, debug, and rollout toggles must be governed configuration with owner, environment scope, classification, approval, audit, and rollback path. |

# 7. Security, Classification, OPA/SBAC, AI, and Runtime Toggle Controls

No block may be visible, actionable, or data-bearing without backend OPA/RBAC/SBAC/ABAC policy evaluation and a safe deny behavior.

Classification ceiling applies to props, API payloads, displayed fields, files, AI prompt context, generated artifacts, telemetry, screenshots, test data, and evidence records.

Frontend authorization is advisory only. Final authorization, field filtering, allowed actions, and sensitive-data suppression are backend decisions.

AI guidance blocks must route through approved AI service, LiteLLM aliases, guardrails, retrieval eligibility checks, output classification, artifact governance, and audit evidence.

AI-generated content must be labeled as advisory unless a governed human or workflow approval makes it authoritative for a specific business purpose.

Runtime toggles must not weaken policy, expose forbidden telemetry, bypass approval, or silently enable high-impact blocks in production.

Secrets, tokens, raw JWTs, raw PII, account numbers, raw documents, raw prompts containing Confidential/Restricted data, embeddings, and private keys must not be logged, rendered, prompted, or indexed in unauthorized contexts.
| Failure Condition | Required Behavior |
| --- | --- |
| Missing policy | Fail closed: hide block/action/field and emit policy-denial evidence. |
| Missing schema | Block cannot render or submit; submit authoring defect and CI failure. |
| Missing component registration | Reject activation and block runtime rendering. |
| Missing MicroFunction binding for mutating action | Action cannot be shown or invoked. |
| AI route or guardrail unavailable | AI block unavailable or degraded to non-AI guidance; protected action cannot proceed. |
| Telemetry control unavailable | Block activation is blocked for critical flows unless safe minimum audit/evidence still works. |

# 8. Testing, Observability, DevSecOps Evidence, and GitNexus Requirements
| Test / Evidence Area | Minimum Proof |
| --- | --- |
| Unit/component tests | Validate component rendering, props schema, empty/error/loading/denied states, and deterministic behavior. |
| Contract tests | Validate generated OpenAPI clients, AsyncAPI events, Avro/JSON schemas, CloudEvents attributes, safe response envelope, and version compatibility. |
| Policy tests | OPA/Rego positive/negative tests for block visibility, field filtering, action eligibility, AI prompt eligibility, runtime toggle eligibility, and admin actions. |
| Accessibility tests | Keyboard navigation, focus, labels, ARIA, contrast, responsive behavior, drag/drop alternatives, error messaging, and screen-reader behavior. |
| E2E tests | Playwright coverage for workspace resolution, block rendering, widget action, AI panel behavior, denied paths, cache invalidation, rollback, and hypercare smoke tests. |
| Security tests | Authenticated DAST scope, secrets scan, unsafe HTML checks, token leakage checks, authorization bypass tests, file upload controls, and AI prompt leakage checks. |
| Resilience tests | Idempotent action replay, duplicate submit, outbox/replay, DLQ path, API timeout, cache miss/loss, telemetry off/on, and feature disablement tests. |
| Observability tests | OpenTelemetry trace propagation, Log4j2 structured logs, Sentry error capture, Loki/Tempo/Grafana dashboards, audit events, evidence record completeness, and forbidden-field tests. |
| DevSecOps Evidence | Required Content |
| --- | --- |
| PR/MR AVCI summary | Owner, source, classification, affected blocks/packs, contracts, policies, tests, evidence path, reviewer, rollback. |
| GitNexus impact | Affected components, contracts, MicroFunctions, policies, database/configuration, tests, and architecture drift signals. |
| CI/CD gates | Build, lint, type check, component tests, contract tests, policy tests, accessibility, E2E, security scans, SBOM/provenance, evidence pack. |
| Runtime dashboards | Block usage, action success/failure, policy denials, slow widgets, AI guardrail outcomes, cache invalidations, error budget impact, evidence completeness. |

# 9. Mortgage Experience Pack Reference Pattern

The Mortgage Experience Pack is the reference implementation pattern for Experience Pack authoring. It demonstrates how reusable blocks become a governed business journey without creating a monolithic mortgage application or bypassing backend authority.
| Block | Purpose | Backend Binding | Classification | Rendering |
| --- | --- | --- | --- | --- |
| MORTGAGE_APPLICATION_BLOCK | Capture and submit mortgage application. | MORTGAGE_APPLICATION_SUBMIT | CONFIDENTIAL | SSR wrapper + CSR form island |
| KYC_DOCUMENT_UPLOAD_BLOCK | Upload and track KYC documents. | KYC_DOCUMENT_UPLOAD | RESTRICTED | SSR wrapper + CSR upload island |
| APPRAISAL_REQUEST_BLOCK | Request and track property appraisal. | PROPERTY_APPRAISAL_REQUEST | CONFIDENTIAL | SSR + workflow status |
| PAYMENT_SCHEDULE_BLOCK | View dues, amortization, and payment status. | MORTGAGE_PAYMENT_SCHEDULE_VIEW | CONFIDENTIAL | SSR + streamed refresh |
| TITLE_RELEASE_BLOCK | Request title release after full payment. | TITLE_RELEASE_REQUEST | CONFIDENTIAL | SSR + guarded action |
| AI_MORTGAGE_GUIDANCE_BLOCK | Explain journey and generate references/artifacts. | AI_MORTGAGE_GUIDE | CONFIDENTIAL ceiling | SSR shell + CSR/streaming AI panel |
| EVIDENCE_TIMELINE_BLOCK | Show AVCI and audit history. | EVIDENCE_TIMELINE_VIEW | CONFIDENTIAL | SSR evidence timeline |

# 10. Lifecycle, Versioning, Reuse, RACI, Acceptance Criteria, and AVCI Summary
| Lifecycle State | Meaning |
| --- | --- |
| DRAFT | Authoring state; may be edited, validated, and reviewed. Not available for runtime use. |
| FOR_REVIEW | Ready for checker review of business fit, schema, policy, classification, test, and evidence. |
| APPROVED | Approved but not active; may be scheduled for activation or seeding. |
| ACTIVE | Runtime eligible within activation scope after cache invalidation and observability confirmation. |
| SUPERSEDED | Replaced by newer version; retained for traceability and rollback comparison. |
| DISABLED | Temporarily unavailable by feature flag, incident control, or policy decision. |
| ROLLED_BACK | Reverted after failed activation with incident/root-cause evidence. |
| RETIRED | No longer available; kept for audit and historical reconstruction. |
| Role | Responsibility |
| --- | --- |
| Product Owner | Owns business intent, user journey, acceptance criteria, and pack business approval. |
| Solutions Architect | Owns bounded context, reuse, architecture fit, and ADR/TDL decisions. |
| Frontend Lead | Owns component contract, renderer fit, accessibility, and UI quality evidence. |
| Backend Lead / MicroFunction Owner | Owns API/MicroFunction capability binding, idempotency, audit, error, and rollback behavior. |
| Security Architect | Owns classification, OPA/SBAC/ABAC, AI route eligibility, secrets, and abuse-case coverage. |
| DevSecOps Lead | Owns CI/CD gates, evidence pack, GitNexus, SBOM/provenance, and release readiness. |
| QA/SDET | Owns test strategy, coverage, E2E, accessibility, resilience, and evidence completeness. |
| Internal Audit | Reviews evidence, chain-of-custody, control effectiveness, and AVCI completeness. |

Every block and pack has owner, version, bounded context, classification ceiling, schema, component key, policy binding, evidence profile, and rollback/deactivation path.

No block renders user-specific or Confidential/Restricted data through ISR or unaudited cache paths.

All mutating actions bind to approved APIs and MicroFunction transactions with idempotency, audit, outbox, observability, and safe failure behavior.

All AI-enabled blocks use approved model routes, guardrails, retrieval eligibility, artifact governance, and human approval where required.

All blocks and packs pass unit, component, contract, policy, accessibility, E2E, security, resilience, observability, and architecture fitness gates before production activation.

All activation, rollback, disablement, incident, Auto-Heal, Auto-Learn, and Auto-Improve proposals create AVCI evidence and cannot self-promote.
| AVCI Property | Evidence |
| --- | --- |
| Attributable | Block/pack owner, author, reviewer, approver, version, source ticket, contract refs, policy refs, component refs, and evidence refs are recorded. |
| Verifiable | Tests, CI/CD gates, GitNexus impact, contract validation, OPA decisions, telemetry, dashboards, and runtime evidence prove behavior. |
| Classifiable | Classification ceiling, data-handling rules, AI route eligibility, telemetry redaction, retention, and access controls are declared and enforced. |
| Improvable | Usage metrics, errors, denials, UX feedback, incidents, slow widgets, test gaps, and Auto-Improve candidates feed governed backlog and versioning. |

