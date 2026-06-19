---
title: "Dynamic Workspace Frontend Reference Implementation Guide"
doc_id: "AIRA-56"
version: "v1.1"
status: "revised"
category: "Dynamic workspace"
source_docx: "AIRA_56_Dynamic_Workspace_Frontend_Reference_Implementation_Guide_v1.1_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 46-60-dynamic-workspace
  - revised
  - aira-56
---



# Dynamic Workspace Frontend Reference Implementation Guide



AIRA
AI-Native Enterprise Platform

Dynamic Workspace Frontend Reference Implementation Guide

Next.js App Router | Runtime Renderer | Component Registry | Widget Shell | AI Panel | Generated Clients | AVCI Evidence
| Document ID | AIRA-DOC-056 |
| --- | --- |
| Canonical Filename | 56-AIRA_Dynamic_Workspace_Frontend_Reference_Implementation_Guide_v1.1_Revised.docx |
| Version | v1.1 - Revised and Cross-Aligned |
| Supersedes | 56-AIRA_Dynamic_Workspace_Frontend_Reference_Implementation_Guide_v1.0.docx |
| Status | Draft for Architecture Review Board / CAB Approval |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Frontend Lead; Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; Platform Engineering; AI Engineering; SRE; Internal Audit |
| Primary Audience | Frontend Developers; Backend Developers; Solutions Architects; DevSecOps; QA/SDET; Security; Product Owners; Internal Audit |
| Effective Date | Upon ARB / CAB approval |
| Review Cadence | Quarterly; unscheduled on material Dynamic Workspace, MicroFunction, API, security, AI, rendering, database, DevSecOps, or observability change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Dynamic-Workspace / Frontend-Reference / v1.1/ |

Mandatory Practice Statement. The AIRA frontend is a governed rendering and interaction layer. It may present, validate, guide, and request approved backend actions, but it must not own business authority, invent endpoints, bypass OPA/SBAC/ABAC/RBAC, call model providers directly, execute tool actions directly, persist authoritative business state, or activate templates without evidence and approval. Backend APIs, MicroFunction runtime, workflow engines, policy-as-code, database constraints, and approved contracts remain the authority.

# Static Table of Contents

1. Executive Summary and v1.1 Upgrade Position

2. Purpose, Scope, and Authority

3. Governing Baseline and Cross-Document Alignment

4. Reference Frontend Architecture

5. Repository and Folder Structure

6. Next.js App Router Implementation Rules

7. Runtime Workspace Renderer and Component Registry

8. Widget Shell and User Interaction Pattern

9. Contract-First API, Event, and MicroFunction Binding

10. AI Assistant Panel and Multimodal Artifact Controls

11. Security, Classification, and OPA/SBAC Enforcement

12. State, Cache, Runtime Toggles, and Performance Controls

13. Observability, Audit, and Evidence

14. Testing, CI/CD, GitNexus, and Architecture Fitness

15. RACI, Roadmap, Acceptance Criteria, and AVCI Summary

# 1. Executive Summary and v1.1 Upgrade Position

This v1.1 revision updates the AIRA Dynamic Workspace Frontend Reference Implementation Guide so developers can implement the runtime workspace shell consistently with the revised environment, DevSecOps, API, database, security, observability, Dynamic Workspace, and System Builder controls. It keeps the original v1.0 implementation pattern - Next.js App Router, React, TypeScript, generated clients, schema validation, component registry, widget shell, AI panel, and testing - but expands it into an enterprise-grade frontend reference baseline that is traceable, testable, secure, observable, reversible, and evidence-producing.
| Topic | Required Result |
| --- | --- |
| Frontend role | Governed renderer and interaction layer that consumes policy-filtered backend workspace definitions. |
| Backend authority | Workspace resolver, APIs, MicroFunctions, workflow engines, OPA/SBAC, database constraints, and evidence stores remain authoritative. |
| Developer outcome | A repeatable folder structure, rendering pattern, widget shell, generated-client discipline, AI panel boundary, test pattern, and CI evidence model. |
| v1.1 expansion | Adds runtime toggles, telemetry standards, Dynamic Workspace security, component governance, contract-first API/eventing, GitNexus evidence, resilience tests, and Auto-Heal/Auto-Learn/Auto-Improve candidate loops. |
| Area | v1.1 Improvement |
| --- | --- |
| Next.js App Router | Clarifies Server Component route shell, Client Component islands, secure no-store defaults, and PPR/streaming readiness. |
| Component registry | Requires compiled allow-listed components only; no arbitrary remote component import or runtime JavaScript execution from configuration. |
| Widget shell | Requires loading, empty, denied, error, validation, success, evidence, confirmation, and retry-safe states. |
| Contracts | Generated OpenAPI clients and typed event/action metadata are mandatory; frontend must not invent endpoints or payloads. |
| Security | Adds OPA/SBAC/ABAC/RBAC decision awareness, classification ceilings, safe token handling, CSP/safe rendering, and authenticated DAST readiness. |
| Observability | Adds Log4j2/OTel-compatible correlation from frontend to gateway, backend APIs, MicroFunction runtime, AI service, audit, and evidence. |
| Runtime toggles | Adds governed toggles for AI panel, diagnostics, sampling, feature exposure, component preview, and accessibility/UX telemetry. |
| Auto loops | Auto-Heal, Auto-Learn, and Auto-Improve may propose frontend fixes or learning items only; activation still requires PR/MR, tests, and approval. |

# 2. Purpose, Scope, and Authority

Define a reference implementation pattern for AIRA Dynamic Workspace frontend development using Next.js, React, TypeScript, generated clients, schema validation, and component registry controls.

Convert Dynamic Workspace governance into developer-executable frontend rules without weakening backend authority, MicroFunction governance, or API contracts.

Define secure frontend boundaries for AI Assistant Panel, multimodal artifacts, runtime toggles, policy-filtered layouts, and evidence-producing user actions.

Define the test, CI/CD, accessibility, observability, and GitNexus evidence that proves frontend readiness before promotion.
| Control | Interpretation |
| --- | --- |
| In Scope | Runtime workspace renderer; route shell; screen renderer; component registry; widget shell; AI panel; generated clients; schema validation; telemetry; frontend tests; visual and accessibility evidence. |
| Out of Scope | Backend business rules; database mutation authority; direct model-provider SDK calls; direct tool execution; policy override; production template activation; arbitrary runtime code loading. |
| L0 Authority | Architecture Board, CAB, Security Governance, Data Governance, and IT Head for production-impacting controls. |
| L1 Governing Standards | AVCI, Enterprise Design Principles, Engineering Blueprint, Developer Guide, Technology Stack, MicroFunction, API, Database/Flyway, Security, CI/CD, Observability, and Dynamic Workspace standards. |
| L2 This Guide | Reference implementation pattern for frontend developers; does not supersede parent architecture/security/API/database standards. |

# 3. Governing Baseline and Cross-Document Alignment
| Source | Required Frontend Alignment |
| --- | --- |
| 12A Dynamic Frontend Workspace Standard | Controls UI generation, template lifecycle, UX governance, backend authority, AI-assisted UI guardrails, and admin-builder boundaries. |
| 41/42/44/46-55 Dynamic Workspace set | Defines runtime workspace, composable experience, configuration/cache, developer guide, database, API, widgets, security, testing, observability, admin builder, and synchronization controls. |
| 15/15A API Contract Standards | Frontend integration must use OpenAPI/AsyncAPI contracts, generated clients, safe errors, idempotency, and compatibility gates. |
| 10 MicroFunction Standards | Widget actions bind to approved capability codes and backend MicroFunction transactions; frontend must not define MicroFunction execution sequence. |
| 17/17A Security Standards | Token handling, CSP, classification, OPA/SBAC, secrets hygiene, authenticated DAST, and safe rendering apply to all frontend code. |
| 20/45/60 DevSecOps Evidence Standards | Frontend changes require CI/CD evidence, accessibility tests, visual regression, SAST/SCA/secret scans, contract tests, GitNexus, and rollback evidence. |
| 31/31A/53 Observability Standards | Frontend events must correlate with backend traces, MicroFunction execution, policy decisions, audit records, and evidence references. |

# 4. Reference Frontend Architecture
| Layer | Allowed Responsibility | Forbidden |
| --- | --- | --- |
| Next.js Route Shell | Resolve route parameters, call backend workspace resolver, render secure shell, enforce server/client boundary. | Own business rules; trust frontend authorization; expose secrets. |
| Workspace Renderer | Render policy-filtered workspace definition and screen definitions from backend. | Load arbitrary components or execute configuration scripts. |
| Component Renderer | Map component_key to compiled allow-listed React component. | Import dynamic remote code based on database/config values. |
| Widget Component | Render data, capture user intent, use generated API client, handle safe states. | Call unregistered endpoints, embed domain rules, or perform final authorization. |
| AI Assistant Panel | Provide governed prompt UI, context selection, streaming response, and artifact references. | Call model providers directly or execute protected actions. |
| Telemetry Client | Propagate trace context, emit safe UX/action telemetry, and record evidence references. | Log raw PII, tokens, secrets, raw prompts, or high-cardinality sensitive labels. |

# 5. Repository and Folder Structure

The repository structure below is the reference starting point. Teams may refine names, but must preserve bounded-context ownership, generated-client separation, component registry discipline, tests, telemetry, and evidence paths.

apps/web-workspace/
  app/
    workspace/[workspaceCode]/page.tsx
    admin/workspace-builder/page.tsx
    layout.tsx
  components/
    workspace/WorkspaceRenderer.tsx
    workspace/ScreenRenderer.tsx
    workspace/ComponentRenderer.tsx
    widgets/<widgetKey>/
      <Widget>.tsx
      <Widget>.contract.ts
      <Widget>.schema.ts
      <Widget>.test.tsx
      <Widget>.a11y.test.tsx
      <Widget>.stories.tsx
    ai/AiAssistantPanel.tsx
  registry/
    componentRegistry.ts
    widgetContracts.ts
    renderingPolicies.ts
  lib/
    api/generated/
    api/clientFactory.ts
    auth/session.ts
    policy/policyContext.ts
    telemetry/clientTelemetry.ts
    validation/zodSchemas.ts
    toggles/runtimeToggles.ts
  tests/
    unit/ component/ contract/ e2e/ a11y/ visual/ resilience/
  evidence/
    frontend-evidence-template.md

# 6. Next.js App Router Implementation Rules
| Pattern | Required Use | Control |
| --- | --- | --- |
| Server Components | Default for secured route shell, layout, backend workspace resolver call, metadata, and read-only initial rendering. | User-specific secured workspace data should default to no-store unless explicitly approved. |
| Client Components | Required for drag/drop, resize, prompt input, upload, filters, forms, local widget interaction, and streaming UI. | Client components must still use generated clients and backend-returned allowed actions. |
| PPR / Streaming | Allowed for stable shells with dynamic policy-governed widget holes after policy model and cache safety are proven. | Must not stream unauthorized or unclassified content. |
| ISR | Allowed only for non-user-specific guides, product information, help content, and public/reference pages. | Not allowed for user, tenant, loan, KYC, workflow, or security-sensitive workspace content. |
| SSR / no-store | Default for role/skill/classification-aware workspace resolution. | Do not cache user-specific policy-filtered layouts without approved cache key and invalidation model. |
| React hooks | Follow Rules of Hooks and keep hooks pure/testable. | Do not call hooks conditionally, in loops, or as hidden control bypasses. |

// Secure route shell - simplified reference pattern
export default async function WorkspacePage({ params }: { params: { workspaceCode: string } }) {
  const workspace = await getResolvedWorkspace(params.workspaceCode, { cache: 'no-store' });
  return <WorkspaceRenderer workspace={workspace} />;
}

# 7. Runtime Workspace Renderer and Component Registry

The renderer must be deterministic, allow-listed, schema-driven, policy-aware, and safe-by-default. Runtime configuration may select from approved components, but must not import arbitrary code or weaken backend policy.

export const componentRegistry = {
  mortgagePipelineWidget: MortgagePipelineWidget,
  kycDocumentUploadWidget: KycDocumentUploadWidget,
  paymentScheduleWidget: PaymentScheduleWidget,
  titleReleaseStatusWidget: TitleReleaseStatusWidget,
  evidenceTimelineWidget: EvidenceTimelineWidget,
  aiAssistantPanel: AiAssistantPanel,
} as const;

export function ComponentRenderer({ instance }: { instance: ComponentInstance }) {
  const Component = componentRegistry[instance.componentKey as keyof typeof componentRegistry];
  if (!Component) return <UnsupportedComponent instance={instance} />;
  return <Component {...instance.props} allowedActions={instance.allowedActions} evidenceRef={instance.evidenceRef} />;
}
| Field | Implementation Meaning |
| --- | --- |
| componentKey | Stable component catalog key returned by backend and registered in compiled registry. |
| propsSchemaCode | Zod/JSON Schema reference used to validate backend-provided props before rendering. |
| allowedActions | Backend-filtered actions only; frontend must not add hidden action options. |
| classificationCeiling | Maximum content classification the component may display. |
| evidenceProfileCode | Telemetry/audit/evidence requirements for render and action events. |
| renderingPolicyCode | SSR/CSR/ISR/PPR/cache/sampling policy from approved registry. |

# 8. Widget Shell and User Interaction Pattern
| Required State | Reference Behavior |
| --- | --- |
| Loading | Skeleton or progressive load state with trace context and no sensitive placeholder data. |
| Empty | Business-safe empty state with guidance and no inference of unauthorized records. |
| Denied | Safe policy-denied state with support/reference code, not internal policy details. |
| Validation Error | Field-level errors from approved schema and safe Problem Details response. |
| Action Confirmation | High-impact/idempotent actions require confirmation, idempotency key, and safe retry semantics. |
| Success | Display result, trace/evidence reference where appropriate, and next-step guidance. |
| Failure | Safe message, retry boundary, correlation ID, no stack traces, and support/escalation path. |
| Degraded | Component works safely if cache, telemetry, AI panel, or optional data source is unavailable. |

type AiraWidgetAction = {
  actionCode: string;
  capabilityCode: string;
  label: string;
  idempotencyRequired: boolean;
  requiresConfirmation: boolean;
  highImpact: boolean;
  evidenceRequired: boolean;
};

// Render only actions returned by backend resolver.
// Never render client-invented action codes.

# 9. Contract-First API, Event, and MicroFunction Binding
| Rule | Frontend Treatment |
| --- | --- |
| Generated clients only | OpenAPI-generated client or approved typed SDK must be used for REST/API calls. |
| No endpoint invention | Frontend code and metadata must not assemble unregistered endpoints or payload fields. |
| Safe response envelope | Use approved Problem Details, trace reference, error code, and UX copy registry. |
| Idempotency | Mutating widget actions must include idempotency key and duplicate-safe UI behavior. |
| MicroFunction binding | Each action maps to approved capability_code and microfunction_transaction_code returned by backend. |
| Async awareness | Long-running actions expose status, trace_id, causation_id, CloudEvent reference, and evidence_ref. |
| DLQ/replay visibility | Operational widgets may display DLQ/replay status only to authorized roles and without exposing sensitive payloads. |

# 10. AI Assistant Panel and Multimodal Artifact Controls
| Control | Required Implementation |
| --- | --- |
| Toggle policy | Panel may be enabled, disabled, docked, expanded, or hidden only by backend policy and runtime toggle controls. |
| Input modes | Text, voice, file, image, screenshot, selected screen context, and selected task/customer context only where classification permits. |
| Output modes | Text, references, checklist, draft document, generated image/audio/video, and action proposal where approved. |
| Guardrails | Input, retrieval, execution, and output guardrails are mandatory; failure safely blocks or degrades the response. |
| Model routing | Frontend calls AIRA AI Assistant API only; no direct provider SDK or browser-to-model calls. |
| Action proposals | AI may recommend or draft action proposals; execution requires API policy, Harness/tool gateway, OPA/SBAC, and human approval where required. |
| Artifact evidence | Generated artifacts require artifact ID, source references, content hash, classification, retention, owner, and evidence_ref. |

# 11. Security, Classification, and OPA/SBAC Enforcement
| Area | Mandatory Rule |
| --- | --- |
| Token handling | Do not expose raw tokens, refresh tokens, ID tokens, JWTs, secrets, or session internals in UI, logs, screenshots, prompts, or tests. |
| Authorization | Frontend uses backend-returned permissions/actions; final authorization remains with backend and OPA/SBAC. |
| Classification | Component, field, prompt, artifact, and response rendering must honor classification ceiling and redaction rules. |
| CSP and safe rendering | No unsafe HTML unless formally approved, sanitized, tested, and monitored. Prefer structured rendering. |
| Uploads | File/image/screenshot uploads require classification, malware scan path, hash, retention rule, and approved storage reference. |
| Authenticated DAST | Use synthetic users and non-production environments; scans must not trigger real business effects. |
| Secrets hygiene | No secrets in .env committed files, prompts, console logs, fixtures, Storybook stories, screenshots, or telemetry. |

# 12. State, Cache, Runtime Toggles, and Performance Controls
| Topic | Control |
| --- | --- |
| Authoritative state | PostgreSQL/backend services own truth; frontend state is view/interactivity state only. |
| Cache safety | Cache keys must include tenant, user hash, workspace, policy hash, layout hash, version, and classification where applicable. |
| Runtime toggles | AI panel, diagnostic verbosity, telemetry sampling, component preview, visual regression mode, and beta widgets must be controlled by backend policy/config. |
| Performance | Use code splitting, progressive rendering, memoization, and bounded polling; never bypass policy for speed. |
| Failure behavior | If policy, workspace resolver, generated client, telemetry, or required config is unavailable, protected actions stop safely. |
| On-the-fly change | Runtime toggle changes must be audited, reversible, policy-checked, and observable. |

# 13. Observability, Audit, and Evidence
| Signal | Required Treatment |
| --- | --- |
| Required correlation | trace_id, span_id, request_id, tenant_id where safe, user_id_hash, workspace_code, screen_code, component_key, capability_code, policy_ref, evidence_ref, classification. |
| Frontend telemetry | Workspace load, component render, widget action, policy-hidden component, layout preference, AI prompt, artifact generation, cache invalidation, runtime toggle change. |
| Forbidden telemetry | Passwords, tokens, raw JWTs, secrets, raw PII, account numbers, raw documents, KYC files, raw restricted prompts, embeddings, payment card data, private keys. |
| Dashboards | Workspace health, component errors, action latency, policy denials, AI panel usage, guardrail outcomes, cache hit/miss, evidence completeness, slow widgets. |
| Evidence pack | PR/MR evidence, contract evidence, policy evidence, test evidence, accessibility/visual evidence, runtime trace evidence, rollback evidence, known limitations. |

# 14. Testing, CI/CD, GitNexus, and Architecture Fitness
| Gate | Minimum Required Evidence |
| --- | --- |
| Type and lint | TypeScript strict mode, ESLint, formatting, dependency rules, forbidden imports. |
| Unit/component | Renderer, widget shell, registry, schema validation, error states, denied states, action rendering. |
| Contract | Generated client compatibility, Problem Details handling, idempotency headers, mock server tests. |
| OPA/SBAC | Allow/deny/hidden field/action tests using representative roles, skills, classification, tenant, and branch scenarios. |
| Accessibility | WCAG 2.2-oriented keyboard, focus, labels, ARIA, contrast, responsive, reduced-motion, screen-reader tests. |
| E2E/visual | Playwright flows, screenshot comparisons, policy-filtered layout tests, admin preview tests. |
| Security | SAST/SCA/secret scan, authenticated DAST, CSP tests, unsafe rendering checks, upload controls. |
| Resilience | Cache loss, backend timeout, duplicate click, retry, idempotency, slow widget, AI unavailability, telemetry unavailable. |
| GitNexus | Read-only impact analysis, affected tests, sensitive-code map, frontend boundary drift, no write authority. |

# 15. RACI, Roadmap, Acceptance Criteria, and AVCI Summary
| Role | Responsibility |
| --- | --- |
| Solutions Architecture Office | Accountable for architecture, standards alignment, and acceptance interpretation. |
| Frontend Lead | Owns implementation pattern, component registry, client-side code quality, and frontend evidence. |
| Backend Lead | Owns workspace resolver, APIs, MicroFunction bindings, and backend authority boundaries. |
| Security Architecture | Reviews OPA/SBAC, token handling, classification, CSP, DAST scope, and AI panel controls. |
| QA/SDET | Owns unit/component/contract/E2E/accessibility/visual/resilience evidence. |
| DevSecOps Lead | Owns CI/CD gates, evidence pack, GitNexus read-only integration, SBOM/provenance, and promotion path. |
| Product Owner / Business SME | Confirms business usability, labels, workflows, safe guidance, and user acceptance criteria. |
| Internal Audit | Reviews evidence completeness and control traceability; does not approve own changes. |
| Phase | Target | Exit Evidence |
| --- | --- | --- |
| Phase 1 | Approve v1.1 reference and update repository templates. | ARB/CAB approval and developer acknowledgement. |
| Phase 2 | Implement reference shell, generated clients, renderer, registry, and widget shell. | Demo with synthetic workspace and policy-filtered layout. |
| Phase 3 | Add AI panel, telemetry, runtime toggles, and evidence hooks. | Guardrail, policy, telemetry, and evidence tests pass. |
| Phase 4 | Harden through CI/CD, GitNexus, accessibility, authenticated DAST, visual regression, and resilience tests. | All blocking gates pass or formal waiver exists. |
| Phase 5 | Promote as reusable frontend foundation capability. | Repository template, runbook, and evidence pack accepted. |

Reference implementation renders only backend-approved workspace definitions and allow-listed components.

Frontend uses generated OpenAPI clients and approved typed SDKs only.

Widgets handle loading, empty, denied, error, validation, confirmation, success, degraded, and retry-safe states.

Backend remains authoritative for authorization, classification, business rules, data access, workflow, MicroFunction execution, and evidence.

AI Assistant Panel uses approved API/gateway/guardrails and cannot approve or execute protected actions directly.

Runtime toggles are policy-controlled, audited, reversible, and tested.

Telemetry is correlation-ready and redaction-safe; forbidden fields are blocked by tests.

CI/CD evidence includes type/lint, unit/component/contract/E2E/accessibility/visual/security/resilience tests, GitNexus, and rollback evidence.

All artifacts are attributable, verifiable, classifiable, and improvable.
| AVCI Property | Evidence |
| --- | --- |
| Attributable | Document owner, co-owners, repository path, component owner, ticket, PR/MR, template version, generated client version, and evidence_ref identify accountability. |
| Verifiable | Tests, contract checks, policy checks, GitNexus analysis, telemetry, visual/a11y evidence, CI/CD evidence, and runtime traces prove behavior. |
| Classifiable | Components, fields, prompts, artifacts, telemetry, screenshots, test data, and evidence carry classification and redaction rules. |
| Improvable | Defects, UX friction, performance regressions, denied actions, failed guardrails, slow widgets, incidents, and Auto-Learn candidates feed backlog and controlled revisions. |

External Alignment Note. This revision was aligned for implementation posture with current official Next.js App Router server/client component guidance, React Rules of Hooks, WCAG 2.2 accessibility guidance, and OpenTelemetry Semantic Conventions. AIRA governance remains the controlling implementation authority where external guidance is broader or less restrictive.

