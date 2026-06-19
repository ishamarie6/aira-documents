---
title: "Dynamic Workspace DevSecOps Pipeline and Evidence Pack Guide"
doc_id: "AIRA-60"
version: "v1.1"
status: "revised"
category: "Dynamic workspace"
source_docx: "AIRA_60_Dynamic_Workspace_DevSecOps_Pipeline_and_Evidence_Pack_Guide_v1.1_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 46-60-dynamic-workspace
  - revised
  - aira-60
---



# Dynamic Workspace DevSecOps Pipeline and Evidence Pack Guide



AIRA

AI-Native Enterprise Platform

Dynamic Workspace DevSecOps Pipeline and Evidence Pack Guide

CI/CD | Security Gates | GitNexus | Evidence Pack | Accessibility | Visual Regression | Supply Chain | Runtime Assurance

Version v1.1 - Dynamic Workspace, MicroFunction, AI Panel, Security, Observability, and Evidence Alignment Update
| Mandatory Practice Statement. AIRA Dynamic Workspace changes are not release-ready because a widget renders or a configuration loads. They are release-ready only when source, contracts, policies, MicroFunction bindings, UI behavior, AI panel controls, security gates, accessibility, visual regression, observability, evidence pack, rollback, and human approval are complete, traceable, and reviewable. Pipeline speed must never weaken AVCI, policy-as-code, SBAC, observability, secure-by-design, or reversibility. |
| --- |

# Document Control
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-060 |
| Canonical Filename | 60-AIRA_Dynamic_Workspace_DevSecOps_Pipeline_and_Evidence_Pack_Guide_v1.1_Revised.docx |
| Version | v1.1 - Dynamic Workspace, MicroFunction, AI Panel, Security, Observability, and Evidence Alignment Update |
| Supersedes | 60-AIRA_Dynamic_Workspace_DevSecOps_Pipeline_and_Evidence_Pack_Guide_v1.0.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | DRAFT FOR ARCHITECTURE REVIEW BOARD / CAB APPROVAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; Platform Engineering; AI Engineering; SRE / Operations; Internal Audit |
| Primary Audience | Solutions Architects, Frontend Developers, Backend Developers, DevSecOps, QA/SDET, Security, SRE, Product Owners, Internal Audit |
| Review Cadence | Quarterly; unscheduled on material Dynamic Workspace, MicroFunction, security, AI, workflow, rendering, database, observability, or DevSecOps change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Dynamic-Workspace / DevSecOps-Pipeline / v1.1/ |

# v1.1 Alignment Summary
| Alignment Area | v1.1 Required Improvement |
| --- | --- |
| Dynamic Workspace UX / Frontend | Treat every workspace, screen, widget, layout, AI panel, and personalization change as governed release artifacts with accessibility, visual regression, responsive, and policy-filtering evidence. |
| MicroFunction Backend | Validate capability binding, transaction code, idempotency profile, evidence profile, OPA/SBAC decision path, audit/outbox behavior, and rollback strategy before promotion. |
| DevSecOps and GitNexus | Every PR/MR must include CI/CD evidence, security scans, SBOM/provenance, GitNexus read-only impact summary, derived evidence, and human checker approval. |
| API / Event Contracts | OpenAPI, AsyncAPI, Kafka, Avro or JSON Schema, CloudEvents, outbox, DLQ, replay, and schema evolution checks are mandatory where affected. |
| Observability | Log4j2, OpenTelemetry, Sentry, Loki, Tempo, and Grafana signals must reconstruct frontend-to-backend-to-MicroFunction behavior without exposing forbidden fields. |
| Resilience and Heavy Transaction | Resilience Lab gates must prove retry-safe, duplicate-safe, concurrent, heavy-load, failure-aware behavior before release. |
| Continuous Improvement | Auto-Heal, Auto-Learn, and Auto-Improve loops remain candidate/proposal-driven until tests, evidence, policy, and human approval are complete. |
| Security Expansion | OPA/SBAC expansion, abuse cases, authenticated DAST, secure APIs, secrets hygiene, remediation evidence, and fail-closed controls are release blockers. |

# Static Table of Contents

1. Executive Summary

2. Purpose, Scope, and Authority

3. Canonical Source Alignment

4. Pipeline Control Model

5. Artifact Scope and Required Gates

6. Required CI/CD Stage Model

7. Architecture Fitness and Quality Gates

8. API, Event, Schema, Outbox, DLQ, and Replay Gates

9. MicroFunction and Backend Binding Gates

10. Security, OPA/SBAC, DAST, and Secrets Hygiene Gates

11. Accessibility, UX, Responsive, and Visual Regression Gates

12. Observability, Audit, Runtime Toggle, and Evidence Gates

13. GitNexus and Derived Evidence Rules

14. Evidence Pack Model and Manifest

15. Promotion, Rollback, and CAB/ARB Gates

16. Concurrency, Heavy Transaction, Idempotency, and Resilience Lab

17. Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop

18. Dashboards and Release Readiness Views

19. RACI and Separation of Duties

20. Implementation Roadmap

21. Acceptance Criteria and Definition of Done

22. Open Issues and Reconciliation Items

23. AVCI Compliance Summary

Appendices A-E

# 1. Executive Summary

This guide defines the release-control model for the AIRA Dynamic Workspace. It expands the v1.0 baseline from a pipeline checklist into an enterprise-grade, evidence-producing DevSecOps implementation guide for workspace templates, frontend components, widgets, configuration seeders, API contracts, policy bundles, AI panel capabilities, MicroFunction bindings, events, telemetry, and runtime assurance.

The governing rule remains simple: no Dynamic Workspace change is production-ready without pipeline evidence, security evidence, policy evidence, test evidence, accessibility evidence, observability evidence, rollback evidence, and named human approval.
| Strategic Outcome | Required Result |
| --- | --- |
| Evidence by construction | Build, test, security, policy, accessibility, visual, contract, GitNexus, release, observability, and approval evidence are generated in the pipeline, not assembled manually after the fact. |
| Frontend without business authority | Dynamic Workspace remains a governed renderer; backend APIs, OPA/SBAC, workflows, and MicroFunctions own policy and business behavior. |
| Contract-first runtime | All API/event/schema boundaries are validated before generated clients, widget actions, MicroFunction bindings, or deployment are accepted. |
| Secure and observable release | Sensitive data is blocked from logs, traces, screenshots, prompts, artifacts, telemetry labels, and evidence summaries. Critical paths remain reconstructable. |
| Reversible promotion | Every activated template, component, policy, config, API, AI capability, or MicroFunction binding has rollback, disablement, forward-fix, or compensation evidence. |
| Improvement loop discipline | Auto-Heal, Auto-Learn, and Auto-Improve create candidates, tests, recommendations, and PRs only; promotion remains governed by maker-checker and evidence gates. |

# 2. Purpose, Scope, and Authority

## 2.1 Purpose

Define the mandatory DevSecOps stage model for Dynamic Workspace and Composable Experience changes.

Define evidence pack contents that prove AVCI, EDP, SOLID, security, accessibility, observability, testability, and reversibility.

Prevent dynamic UI, AI panel, admin builder, or configuration changes from bypassing backend policy, API contracts, MicroFunctions, or human approval.

Provide implementation-ready gates for GitHub/GitLab, GitNexus, CI/CD, Playwright, OPA, SAST, DAST, SBOM, visual regression, and runtime monitoring.

## 2.2 Scope
| In Scope | Out of Scope |
| --- | --- |
| Workspace templates, screen templates, layouts, component registry entries, widget code, rendering policies, personalization behavior, admin builder configuration, and experience packs. | Direct production mutation, manual production configuration edits, bypassing branch protection, bypassing CODEOWNERS, or accepting changes without evidence. |
| OpenAPI, AsyncAPI, Kafka topics, CloudEvents, Avro/JSON Schema, generated clients, idempotency, outbox, DLQ, replay, and schema compatibility checks. | Ad hoc endpoints, unregistered events, direct browser-to-database calls, direct model-provider calls, or unversioned schema changes. |
| OPA/SBAC, RBAC/ABAC, Keycloak/session context, feature flags, secrets handling, log redaction, authenticated DAST, and abuse-case tests. | Frontend authorization authority, hardcoded roles, raw token/secret logging, insecure screenshots, or unreviewed policy weakening. |
| Pipeline evidence, GitNexus read-only impact summaries, SBOM/provenance, artifact hashes, release manifests, rollback plans, and post-promotion monitoring. | Treating GitNexus as an approver, replacing tests or human review, or promoting derivative summaries as authority. |

## 2.3 Authority
| Level | Authority | Pipeline Interpretation |
| --- | --- | --- |
| L0 | ARB / CAB / Security Governance | Final authority for production-impacting gates, waivers, exceptions, and release readiness. |
| L1 | AVCI, EDP, DevSecOps, Security, API, Database, Observability, Change Standards | Universal controls for evidence, architecture, testability, policy, security, rollback, and audit. |
| L2 | This AIRA-DOC-060 Guide | Dynamic Workspace-specific pipeline, evidence pack, and promotion gate authority. |
| L3 | CI/CD definitions, OPA policies, OpenAPI/AsyncAPI contracts, test packs, GitNexus reports | Executable validation and evidence controls. |
| L4 | Runtime traces, audit records, dashboards, incidents, PR/MR evidence | Operational proof and improvement inputs. |

# 3. Canonical Source Alignment
| Source Family | Required Alignment in This Guide |
| --- | --- |
| 53 Observability / Audit / Evidence | CI must verify mandatory correlation fields, forbidden telemetry fields, evidence records, audit events, and dashboard readiness. |
| 54 Admin Builder / Template Governance | CI must validate template lifecycle, maker-checker fields, approval state, rollback target, immutable versioning, and cache invalidation events. |
| 55 Seeder and Runtime Synchronization | CI must validate Git-managed config, deterministic seeding, PostgreSQL authority, Redis derivative cache behavior, config.changed events, and rollback tests. |
| 56 Frontend Reference Implementation | CI must enforce generated API clients, component allow-list, widget states, CSR island safety, browser security, and redacted telemetry. |
| 57 Experience Block / Pack Authoring | CI must validate block metadata, component schema, capability binding, MicroFunction transaction code, policy binding, and evidence profile. |
| 58 Prompt / Artifact / Response Governance | AI prompt, artifact, response, multimodal input, guardrail, registry, and action proposal changes must pass model-route and evidence gates. |
| 59 UX / Accessibility / Responsive Design | Pipeline must run keyboard, screen-reader, responsive, denied-state, AI panel, visual regression, and accessibility tests. |
| 61 AI-Assisted Dynamic Workspace and System Builder | System Builder-generated artifacts remain drafts until this guide’s gates produce evidence and human approval. |
| Conflict Rule. If a companion standard conflicts with this guide, the stricter control governs temporarily. The conflict must be logged as an AVCI reconciliation item, assigned an owner, classified by severity, and resolved through the canonical register / 00D path. |
| --- |

Figure 1. Dynamic Workspace CI/CD Control Flow

# 4. Pipeline Control Model

The pipeline control model is a governed sequence of gates. Each gate either produces evidence or fails closed. AIRA does not accept “green builds” that lack policy, security, classification, test, accessibility, rollback, or approval evidence.
| Control Layer | Purpose | Required Evidence |
| --- | --- | --- |
| Source control | Ensure every change starts from an approved branch, ticket, CODEOWNERS, and classification. | ticket_ref, branch, commit, author, reviewer, classification, affected bounded context |
| Contract validation | Prevent UI/API/event/config mismatch before code and widgets are promoted. | OpenAPI lint, AsyncAPI lint, schema compatibility, generated client hash, contract test results |
| Build and quality | Prove TypeScript/Java compilation, lint, formatting, unit, component, E2E, and visual correctness. | build report, lint report, unit/component/E2E report, accessibility report, visual report |
| Security and policy | Block unsafe HTML, secrets, policy bypass, insecure APIs, unauthorized capability bindings, and weak controls. | SAST, SCA, secret scan, authenticated DAST, OPA test, SBOM, container scan, abuse-case results |
| Evidence and impact | Correlate code, config, API, database, policy, MicroFunction, AI, tests, and release risk. | GitNexus impact summary, derived evidence, artifact hash, provenance, SBOM, architecture fitness summary |
| Promotion and runtime assurance | Promote only when approval, rollback, monitoring, and post-release evidence are ready. | approval record, rollback target, feature flag state, smoke test, dashboards, SLO / error budget signals |

# 5. Artifact Scope and Required Gates
| Artifact | Mandatory Gates | Release-Blocking Failure |
| --- | --- | --- |
| Frontend component / widget | type check, lint, component tests, accessibility, visual regression, generated client usage, browser security check | unregistered API calls, unsafe HTML, localStorage token storage, missing states, failed a11y, failed visual baseline |
| Workspace / screen / layout config | schema validation, hash/signature, policy binding, responsive grid, config seeder dry-run, rollback target | missing owner, invalid schema, no rollback target, direct Redis authority, unauthorized component |
| API contract | OpenAPI lint, compatibility, generated client, contract tests, Problem Details, idempotency profile | breaking change without versioning, missing error semantics, generated client mismatch |
| Event contract | AsyncAPI lint, CloudEvents envelope, Kafka topic policy, Avro/JSON Schema compatibility, consumer contract tests | unversioned event, missing correlation, schema incompatibility, no DLQ/replay strategy |
| OPA / SBAC policy | Rego tests, deny coverage, allow scenario, fail-closed tests, separation-of-duties test | policy weakens access, missing deny-by-default, no checker, no decision evidence |
| MicroFunction binding | catalog validation, transaction code, idempotency, outbox, evidence profile, integration test | hardcoded sequence bypass, missing idempotency key, no audit/outbox, no evidence profile |
| AI capability / prompt | model route, guardrails, prompt eval, retrieval test, artifact registry, action proposal boundary | direct provider SDK, prompt/tool bypass, unclassified artifact, missing guardrail evidence |
| Database/Flyway | migration lint, checksum, clean-migrate in test, rollback/forward-fix review, RLS where applicable | manual DDL, destructive migration without approval, missing migration evidence |

# 6. Required CI/CD Stage Model
| Stage | Name | Required Outputs |
| --- | --- | --- |
| S01 | Source and metadata validation | ticket, owner, classification, bounded context, change type, EDP impact, AI-use declaration |
| S02 | Dependency install from approved registry | lockfile verification, registry policy, SCA baseline, package allow-list |
| S03 | TypeScript / Java compilation | frontend build, backend build, generated client compilation, Java runtime evidence |
| S04 | Lint, formatting, and static quality | ESLint, Prettier, Checkstyle/Spotless, dead-code, unsafe import checks |
| S05 | Unit and component tests | coverage, changed-line tests, deterministic fixtures, widget state tests |
| S06 | Contract tests | OpenAPI/AsyncAPI compatibility, generated clients, mock server/consumer tests |
| S07 | OPA/SBAC and policy tests | allow/deny/step-up/require-approval scenarios, SoD, fail-closed results |
| S08 | Architecture fitness | Clean Architecture, DDD boundary, ports/adapters, direct-provider/direct-DB/direct-model call rejection |
| S09 | Security scans | SAST, SCA, secret scan, SBOM, image/container scan, malware scan for test fixtures |
| S10 | Authenticated DAST and abuse cases | sessioned DAST, CSRF/CORS, unsafe action, authorization bypass, injection, prompt/action abuse cases |
| S11 | Accessibility and UX tests | WCAG 2.2 AA target, keyboard, focus, screen reader labels, denied/disabled states |
| S12 | Playwright E2E and visual regression | critical journeys, responsive breakpoints, policy-filtered screens, screenshot redaction |
| S13 | Resilience and concurrency lab | retry, duplicate submit, stale cache, Redis unavailable, outbox replay, DLQ replay, load/concurrency |
| S14 | Evidence pack generation | manifest, artifact hashes, GitNexus report, logs, traces, scan reports, approvals, rollback |
| S15 | Deployment dry-run and rollback check | Kubernetes/Helm dry-run, config seeder dry-run, feature flag, smoke test, rollback target |
| S16 | Promotion request | maker-checker approval, CAB/ARB gate where applicable, post-promotion monitoring plan |

# 7. Architecture Fitness and Quality Gates
| Gate | Reject If Detected | Recommended Check |
| --- | --- | --- |
| Frontend authority | Browser code decides business authorization, branch access, financial action eligibility, title release eligibility, or workflow state. | Semgrep/ESLint rules, code review checklist, generated client-only check |
| Direct provider call | Frontend, backend service, script, or agent calls LLM/model provider SDK directly instead of approved gateway/LiteLLM route. | Semgrep, dependency policy, allow-list, architecture test |
| Ports/adapters violation | Domain/use-case logic imports controllers, frameworks, database clients, Kafka clients, Redis clients, OpenKM, OPA client, Keycloak admin, or provider SDKs directly. | ArchUnit, package boundary tests, dependency graph |
| Unregistered API/event | Widget calls endpoint or topic not defined in contract registry and generated clients. | OpenAPI/AsyncAPI registry validation, generated client import policy |
| Unsafe telemetry | Logs, traces, metrics, screenshots, prompts, evidence, or visual test artifacts expose secrets, tokens, raw PII, account numbers, embeddings, or raw restricted files. | log scanner, screenshot scanner, OTel attribute allow-list, evidence redaction check |
| Missing reversibility | No rollback target, feature flag, previous template version, DLQ replay, config rollback, or forward-fix plan. | release manifest validation, change template enforcement |
| Quality Gate Rule. AIRA allows the pipeline to reject a change even when code compiles and functional tests pass. Production readiness requires complete evidence, not only successful execution. |
| --- |

# 8. API, Event, Schema, Outbox, DLQ, and Replay Gates
| Contract Area | Pipeline Requirement | Evidence Required |
| --- | --- | --- |
| OpenAPI | Lint, compatibility, versioning, generated clients, Problem Details, auth scopes, idempotency headers, pagination where applicable. | openapi-lint.json, compatibility report, generated-client hash, contract-test report |
| AsyncAPI | Lint topics/channels, producer/consumer contracts, message examples, correlation IDs, retry/DLQ contracts. | asyncapi-lint.json, consumer test, topic policy, event sample manifest |
| Kafka and CloudEvents | Require CloudEvents envelope, traceparent/correlation_id/causation_id, tenant/classification where safe, schema reference, producer owner. | event schema report, broker policy check, CloudEvents sample, trace propagation evidence |
| Avro / JSON Schema | Compatibility mode, schema registry references, field evolution rules, backward/forward test. | schema compatibility report, registry version, migration note |
| Transactional outbox | State-changing backend action must write business state and outbox in one transaction or approved equivalent. | outbox integration test, event-publish test, duplicate-safe check |
| Idempotent consumers | Consumers must deduplicate by event_id/idempotency key and be retry-safe. | duplicate delivery test, idempotency-key evidence, consumer-state proof |
| DLQ and replay | Poison messages go to DLQ with classification-safe payload and approved replay/repair runbook. | DLQ test report, replay dry-run, repair approval evidence |
| Schema evolution | Breaking changes require versioning, compatibility plan, consumer migration, and rollback/dual-run strategy. | ADR/TDL, contract compatibility result, consumer impact, GitNexus summary |

# 9. MicroFunction and Backend Binding Gates
| MicroFunction Control | Required Validation |
| --- | --- |
| Catalog entry | transaction_code, version, owner, bounded_context, classification, status, activation state, evidence_profile_code, rollback_strategy |
| Step sequence | standard receive/correlate/session/rate/classify/authorize/validate/idempotency/business/audit/outbox/observe/respond/error steps preserved unless waived |
| Capability binding | widget action is mapped to approved capability_code, OpenAPI operation, OPA decision input, SBAC skill, and MicroFunction transaction |
| Idempotency | mutating actions declare idempotency key, dedupe store, replay semantics, retry behavior, and duplicate-safe audit/outbox behavior |
| Audit and outbox | append-only audit record and transactional outbox event are produced for state-changing or evidence-critical actions |
| Failure behavior | policy unavailable, identity unavailable, audit unavailable, evidence unavailable, model route unavailable, or config unavailable causes protected action to fail closed |
| Rollback and disablement | feature flag, previous config version, previous template version, queue stop/replay, rollback migration, or forward-fix is documented and tested |

# 10. Security, OPA/SBAC, DAST, and Secrets Hygiene Gates
| Security Gate | Mandatory Treatment |
| --- | --- |
| OPA/SBAC expansion | New capabilities, widgets, actions, AI panel tools, admin functions, and MicroFunction transactions require SBAC skill definitions and OPA deny/allow/require-approval tests. |
| Abuse cases | Include unauthorized widget discovery, forced browsing, hidden-field leakage, IDOR, action replay, double-submit, CSRF, CORS, prompt injection, action injection, and privilege escalation cases. |
| Authenticated DAST | Run DAST using synthetic approved users and roles; test denied states and protected actions, not only public endpoints. |
| Secure APIs | Validate auth, authorization, rate limit, input validation, output filtering, safe errors, Problem Details, idempotency, and field-level classification filtering. |
| Secrets hygiene | No secrets in source, config, screenshots, prompts, tests, browser storage, logs, traces, evidence, build output, or GitNexus summaries. |
| Dependency and container security | SCA, SBOM, image scan, license policy, registry allow-list, and provenance are release blockers according to risk tier. |
| Remediation evidence | Each Critical/High finding has owner, status, fix commit, retest result, waiver if any, expiry, compensating control, and backlog/incident link. |

# 11. Accessibility, UX, Responsive, and Visual Regression Gates
| UX / A11y Gate | Required Evidence |
| --- | --- |
| WCAG 2.2 AA target | automated a11y test, keyboard-only walkthrough, screen-reader label check, focus order check, contrast/motion check |
| Responsive behavior | approved breakpoint screenshots, viewport matrix, no clipping/overlap, mobile/tablet restrictions where applicable |
| Widget states | loading, empty, error, denied, disabled, stale, success, partial, requires approval, offline/degraded are tested where applicable |
| Drag/drop alternatives | keyboard-accessible move/resize/reorder/reset path or approved alternative for personalization widgets |
| Visual regression | baseline screenshots for critical screens, redacted sensitive fields, policy-filtered views, printable/export layout where applicable |
| AI Assistant panel UX | toggle, dock, focus, labels, context notice, references, artifact status, safe warning, and non-obscuring critical workflow controls |
| User personas | loan officer, branch manager, KYC reviewer, collections user, admin, auditor, and borrower/user personas where applicable |

# 12. Observability, Audit, Runtime Toggle, and Evidence Gates

Figure 2. Evidence Correlation Model
| Signal | Required Release Evidence |
| --- | --- |
| Log4j2 / structured logs | structured diagnostic logs, redaction tests, safe fields only, no secrets or raw PII |
| OpenTelemetry traces | frontend-to-gateway-to-backend-to-MicroFunction-to-AI/service trace propagation using trace_id and span_id |
| Metrics | workspace load latency, policy deny rate, widget action success/failure, cache hit/miss, AI response latency, error budget indicators |
| Sentry / error monitoring | frontend/backend error grouping, release version, source map governance, PII redaction, remediation link |
| Loki / Tempo / Grafana | logs, traces, metrics, dashboards, annotations, release markers, evidence dashboard URLs |
| Audit events | workspace resolved, component rendered/filtered, layout changed, widget action invoked/denied, AI prompt/artifact, config cache invalidated |
| Runtime toggles | debug logs, expensive traces, sampling, visual diagnostics, and feature flags may be changed at runtime only through approved controls and audit. |
| Non-Disableable Signal | Reason |
| --- | --- |
| Security audit events | Required for accountability, incident response, and compliance reconstruction. |
| Policy decisions and denials | Required to prove OPA/SBAC enforcement and fail-closed behavior. |
| Evidence references | Required to link runtime behavior to PR/MR, release, and incident evidence. |
| Error and incident triggers | Required for SRE, Auto-Heal candidate creation, and operational support. |
| Minimal trace correlation | Required for trace reconstruction even when sampling is reduced. |

# 13. GitNexus and Derived Evidence Rules
| Rule | Mandatory Interpretation |
| --- | --- |
| Read-only and derivative | GitNexus may analyze code, dependency graph, impact, affected tests, ownership, and architecture drift. It must not commit, approve, merge, deploy, or mutate production. |
| Commit-bound | Every GitNexus report must include repository, branch, commit SHA, tool version/configuration, generated_at, classification, and evidence hash. |
| Corroborated | GitNexus findings must be corroborated by tests, security scans, contract checks, architecture fitness, and human review. |
| Evidence use | Use GitNexus to identify affected components, widgets, MicroFunctions, APIs, events, policies, DB migrations, tests, and runbooks. |
| Security-safe | Generated code maps and summaries must not include secrets, raw customer data, proprietary restricted payloads, or raw production logs. |
| Improvement input | GitNexus can feed Auto-Learn and Auto-Improve backlog items, but not self-promote changes or override CODEOWNERS. |

# 14. Evidence Pack Model and Manifest
| Evidence Category | Required Content |
| --- | --- |
| Source evidence | ticket, ADR/TDL/waiver, branch, commit, author, reviewer, CODEOWNERS, AI-use declaration, classification, bounded context |
| Build evidence | dependency lock, approved registry, compiler/runtime versions, artifact hash, container image digest, SBOM, provenance |
| Quality evidence | unit, component, integration, contract, E2E, accessibility, visual regression, changed-line tests, mutation where applicable |
| Security evidence | SAST, SCA, secret scan, container scan, authenticated DAST, abuse cases, remediation evidence, waiver register |
| Policy evidence | OPA/SBAC tests, decision examples, deny coverage, fail-closed scenarios, SoD checks, policy bundle version |
| Contract/event evidence | OpenAPI, AsyncAPI, Avro/JSON Schema, CloudEvents, compatibility, idempotency, outbox, DLQ, replay |
| Observability evidence | trace samples, logs/metrics dashboards, Sentry release, Loki/Tempo/Grafana links, forbidden telemetry check |
| GitNexus evidence | impact analysis, affected tests, code map, architecture drift, sensitive code map, owner map |
| Release evidence | approval, promotion request, deployment dry-run, rollback plan, feature flag state, smoke test, post-release monitoring |

## 14.1 Minimum Manifest Fields
| Field | Meaning |
| --- | --- |
| evidence_pack_id | Unique ID for the PR/MR, release, incident, or candidate improvement evidence pack. |
| source_ref | Ticket, PR/MR, branch, commit, ADR/TDL, waiver, or incident reference. |
| artifact_refs | Build artifacts, generated clients, config hashes, images, SBOMs, policy bundles, dashboards, and report locations. |
| classification | Public, Internal, Confidential, Restricted and handling requirements. |
| verification_results | Gate-level pass/fail, severity, waiver status, and remediation link. |
| principle_impact | EDP/SOLID/Clean Architecture/DDD/ports/adapters/security/observability/reversibility impact. |
| approval_state | maker, checker, approver, CAB/ARB, Security, DevSecOps, QA, Product Owner as applicable. |
| runtime_evidence | trace_id, release version, dashboard URL, audit event IDs, incident/error references. |
| improvement_path | backlog item, Auto-Heal candidate, Auto-Learn update, Auto-Improve proposal, or post-release review. |

# 15. Promotion, Rollback, and CAB/ARB Gates

Figure 3. Promotion Decision Gate
| Promotion State | Allowed Action | Required Control |
| --- | --- | --- |
| DRAFT | Run local/branch validation only. | No production activation; evidence may be incomplete. |
| FOR_REVIEW | Run full CI and checker review. | All automated gates complete or findings classified. |
| APPROVED | Prepare deployment dry-run and rollback evidence. | Approval, rollback target, feature flag, and monitoring plan complete. |
| RELEASE_CANDIDATE | Run environment promotion gates. | Change ticket, CAB/ARB if applicable, security sign-off, smoke tests. |
| ACTIVE | Monitor and retain evidence. | Dashboards, SLO signals, error monitoring, audit, evidence manifest retained. |
| ROLLED_BACK | Restore previous approved state. | Rollback evidence, root cause, remediation plan, and improvement backlog created. |
| RETIRED | Disable and retain audit history. | Retirement evidence, deactivation proof, retained references. |
| Rollback Rule. Rollback must activate the previous approved version or a designated rollback version. Direct-editing production configuration, Redis/Valkey, database tables, or runtime state is prohibited except through approved break-glass with evidence. |
| --- |

# 16. Concurrency, Heavy Transaction, Idempotency, and Resilience Lab
| Scenario | Required Test / Evidence |
| --- | --- |
| Double-submit widget action | same idempotency key returns same outcome or safe duplicate response; no duplicate business effect |
| Concurrent personalization update | optimistic version or conflict-safe merge; no lost update; audit records old/new layout hash |
| Config activation during active sessions | active request resolves consistent version; cache invalidation does not break correctness |
| Redis/Valkey unavailable | resolver falls back to PostgreSQL authoritative state; performance degradation is observable and safe |
| Kafka/outbox retry | duplicate event delivery does not duplicate audit, workflow, or business effects |
| DLQ replay | replay is permissioned, classified, traceable, and duplicate-safe |
| Heavy-load dashboard | slow widgets degrade safely; expensive logging/tracing sampling can be tuned without disabling audit/security evidence |
| Failure injection | OPA unavailable, AI route unavailable, evidence store unavailable, API dependency timeout, database lock, queue failure all fail safely |
| Resilience patterns | timeouts, retries, circuit breakers, bulkheads, fallback, compensation, and monitoring are explicit and tested |

# 17. Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop
| Loop Stage | Required Behavior |
| --- | --- |
| Issue detection | Detect from CI failures, runtime errors, SLO burn, policy denials, failed tests, security findings, accessibility findings, visual regression, support tickets, or incidents. |
| Evidence retrieval | Retrieve only approved, classification-eligible evidence with source, freshness, provenance, SBAC, and redaction checks. |
| Root-cause / hypothesis | Generate explanation, affected components, impacted contracts, suspected cause, confidence, risk, and missing evidence questions. |
| Candidate fix / learning proposal | Draft code/config/policy/test/runbook/prompt improvement in branch/sandbox only; include alternatives and risk. |
| Tests and validation | Generate or update deterministic tests, abuse cases, a11y tests, contract tests, policy tests, and rollback tests. |
| Human approval | Maker-checker, CODEOWNERS, Security/DevSecOps/QA/Product Owner/CAB/ARB approvals according to risk. |
| Promotion and monitoring | Promote through normal gates, monitor post-release, link incidents/backlog, and update knowledge only after review. |
| Auto Loop Boundary. Auto-Heal, Auto-Learn, and Auto-Improve may propose, draft, test, and open PR/MR-ready artifacts. They must not approve their own output, bypass OPA/SBAC/Harness, merge, deploy, activate, or directly mutate production. |
| --- |

# 18. Dashboards and Release Readiness Views
| Dashboard | Minimum Widgets / Signals |
| --- | --- |
| Workspace Release Readiness | CI status, required gates, findings by severity, waiver status, pending approvals, rollback readiness |
| Evidence Completeness | evidence pack fields, missing reports, stale evidence, classification mismatch, source-to-runtime correlation |
| Security and Policy | SAST/SCA/DAST/secrets/SBOM results, OPA deny/allow coverage, policy-denied runtime events, abuse-case status |
| Accessibility and UX | a11y test result, keyboard/focus issues, visual regression status, responsive matrix, user feedback |
| API / Event / Schema | OpenAPI/AsyncAPI status, schema compatibility, consumer impact, outbox, DLQ, replay readiness |
| Observability and Runtime | trace coverage, Sentry errors, Loki logs, Tempo traces, Grafana panels, cache behavior, slow widgets |
| GitNexus Impact | affected components, tests, MicroFunctions, APIs/events, policies, owners, architecture drift, code map |
| Continuous Improvement | Auto-Heal candidates, Auto-Learn updates, Auto-Improve proposals, test gaps, recurring defect trends |

# 19. RACI and Separation of Duties
| Activity | Maker | Checker | Approver | Evidence Consumer |
| --- | --- | --- | --- | --- |
| Widget / frontend component change | Frontend Developer | Frontend Lead / QA | Product Owner / ARB if material | Internal Audit / SRE |
| Workspace config / template activation | Admin Builder Maker | Template Checker / Security | Product Owner / CAB if production | Operations / Internal Audit |
| API / event contract change | Backend/API Developer | API Architect / QA | ARB / Product Owner | Consumers / SRE |
| OPA/SBAC policy change | Security / Platform Engineer | Security Architect | Security Governance / CAB | Auditor / Runtime Ops |
| MicroFunction binding | Backend Developer | Enterprise Architect / QA | ARB / Product Owner | SRE / Audit |
| AI capability / prompt change | AI Engineer | AI Governance / Security | AI Governance / ARB / CAB where required | Model Risk / Audit |
| Pipeline gate change | DevSecOps Engineer | Security / QA / Architecture | DevSecOps Lead / CAB | All teams |
| Release promotion | Release Manager | QA/Security/DevSecOps | CAB / ARB according to risk | Operations / Internal Audit |
| Separation of Duties. The same person, agent, or automation must not act as maker, checker, approver, and promoter for high-risk or production-impacting changes. AI-generated artifacts require named human accountability. |
| --- |

# 20. Implementation Roadmap
| Phase | Target Outcome | Exit Evidence |
| --- | --- | --- |
| Phase 0 - Baseline | Confirm canonical source mapping, register placement, branch rules, CODEOWNERS, PR/MR templates, and evidence schema. | approved implementation plan, issue backlog, evidence template |
| Phase 1 - Pipeline Minimum | Implement build, lint, unit/component, OPA, OpenAPI, SAST/SCA/secrets/SBOM, accessibility, Playwright, evidence pack. | first green evidence pack on synthetic workspace change |
| Phase 2 - Dynamic Workspace Gates | Add config seeder dry-run, responsive/visual matrix, widget states, generated client enforcement, telemetry checks. | workspace release readiness dashboard |
| Phase 3 - API/Event/MicroFunction | Add AsyncAPI, Kafka/CloudEvents, schema compatibility, outbox, DLQ/replay, MicroFunction binding tests. | event and MicroFunction evidence pack |
| Phase 4 - Security Hardening | Add authenticated DAST, abuse cases, secrets hygiene, OPA/SBAC expansion, remediation evidence. | security gate blocking mode enabled |
| Phase 5 - Resilience and Observability | Add heavy transaction, failure injection, OTel trace reconstruction, Sentry/Loki/Tempo/Grafana dashboards. | resilience lab and runtime observability report |
| Phase 6 - Improvement Loop | Add Auto-Heal/Auto-Learn/Auto-Improve candidate intake, GitNexus-driven impact, human approval workflow. | candidate-loop evidence and approved PR flow |

# 21. Acceptance Criteria and Definition of Done
| Acceptance Area | Required Evidence |
| --- | --- |
| Source and ownership | ticket, owner, co-owner, reviewer, classification, bounded context, CODEOWNERS, branch, commit |
| Architecture | EDP-01 to EDP-20 impact statement, SOLID/Clean Architecture/DDD/ports-adapters fitness checks |
| Contracts | OpenAPI/AsyncAPI/schema compatibility, generated clients, CloudEvents/Kafka contracts where affected |
| MicroFunction | catalog validation, capability binding, transaction code, idempotency, audit/outbox, OPA/SBAC, evidence profile |
| Security | SAST, SCA, secrets, SBOM, container scan, authenticated DAST, abuse cases, remediation evidence |
| UX / A11y | WCAG target, keyboard/focus/screen-reader tests, responsive matrix, visual regression, denied/disabled state tests |
| Observability | Log4j2/OTel/Sentry/Loki/Tempo/Grafana proof, forbidden telemetry check, dashboard links |
| Resilience | concurrency, duplicate-safe, outbox/replay, DLQ, cache loss, failure injection, heavy transaction tests |
| Evidence pack | manifest, hashes, GitNexus report, derived evidence, approvals, rollback/forward-fix, retention path |
| Promotion | maker-checker approval, CAB/ARB if applicable, deployment dry-run, smoke test, post-release monitoring |

## 21.1 EDP-01 to EDP-20 Pipeline Control Mapping
| Principle | Pipeline Enforcement |
| --- | --- |
| EDP-01 SOLID | Component, service, prompt, policy, and MicroFunction single-responsibility checks. |
| EDP-02 Clean Architecture | Dependency rules block framework, database, model, and UI leakage into domain/use-case logic. |
| EDP-03 DDD / Bounded Contexts | Change declares owning context, affected APIs/events/schema, and cross-context impact. |
| EDP-04 Ports and Adapters | External systems, queues, databases, AI routes, and tools accessed only through adapters. |
| EDP-05 DRY, KISS, YAGNI | Duplicate widgets, APIs, policy rules, and speculative abstractions are rejected. |
| EDP-06 Idempotency | Mutating actions, callbacks, events, retries, and replay paths are duplicate-safe. |
| EDP-07 Determinism | Builds, migrations, tests, prompts, routes, and evidence are reproducible from source. |
| EDP-08 Fail-Safe | Missing identity, policy, guardrail, audit, evidence, or gateway blocks protected actions. |
| EDP-09 Human-in-the-Loop | High-impact, Restricted, destructive, production-impacting, or low-confidence actions need approval. |
| EDP-10 Least Privilege / SBAC | Skill, role, tenant, classification, and tool/action grants are minimal and tested. |
| EDP-11 Separation of Duties | Maker, checker, approver, deployer, operator, and auditor remain separated. |
| EDP-12 Observability | Trace, metric, log, audit, model, policy, tool, and evidence references are emitted safely. |
| EDP-13 Policy as Code | Authorization, routing, data handling, deployment, and guardrail rules are versioned policy. |
| EDP-14 Testability | Code, configuration, workflows, prompts, policies, and adapters have deterministic tests. |
| EDP-15 Secure by Design | Threat controls, secrets, classification, tenant isolation, and secure defaults are built in. |
| EDP-16 Resilience Patterns | Timeouts, retries, circuit breakers, bulkheads, fallback, DLQ, compensation, recovery tested. |
| EDP-17 Fitness Functions | CI verifies boundaries, dependencies, contracts, security, agents, provisioning, evidence. |
| EDP-18 Progressive Autonomy | Automation advances only with evidence, trust score, risk tier, rollback, and approval. |
| EDP-19 Reversibility | Changes define rollback, forward-fix, compensation, feature disablement, or safe deactivation. |
| EDP-20 AVCI | Every artifact remains attributable, verifiable, classifiable, and improvable. |

# 22. Open Issues and Reconciliation Items
| Item | Severity | Recommended Treatment |
| --- | --- | --- |
| Runtime telemetry toggles across documents | Medium | Standardize non-disableable security/audit/evidence signal list across observability, SRE, Dynamic Workspace, and AI Panel documents. |
| Authenticated DAST placement | Medium | Cross-reference DAST requirements in Security, API, Testing, Dynamic Workspace, and CI/CD evidence documents. |
| Heavy Transaction / Resilience Lab templates | Medium | Propagate duplicate-safe, replay, concurrency, failure injection, and load testing gates into MicroFunction and CI templates. |
| OpenAPI / AsyncAPI / Kafka / Avro / CloudEvents matrix | Medium | Add a reusable contract/event/replay matrix into System Builder proposal templates and evidence pack schema. |
| Dynamic Workspace cross-trace fields | Medium | Standardize trace_id, evidence_ref, policy_decision_id, microfunction_transaction_code, artifact_id, and release_version across UI/API/evidence docs. |
| 61 System Builder alignment | High | Regenerate 61 after 60 so System Builder-generated workspace changes inherit the full pipeline and evidence pack gates. |

# 23. AVCI Compliance Summary
| AVCI Property | How This v1.1 Guide Satisfies It |
| --- | --- |
| Attributable | Defines document owner, co-owners, source baseline, artifact owners, PR/MR ownership, CODEOWNERS, human approvers, GitNexus report references, and evidence pack identifiers. |
| Verifiable | Defines CI/CD gates, contract tests, security scans, OPA/SBAC tests, accessibility tests, visual regression, observability proof, resilience lab evidence, GitNexus impact evidence, and release smoke tests. |
| Classifiable | Requires classification for source, prompts, screenshots, logs, traces, metrics, AI artifacts, config, evidence packs, dashboards, and runtime telemetry. Blocks forbidden telemetry and sensitive data leakage. |
| Improvable | Connects pipeline failures, runtime incidents, accessibility findings, security findings, GitNexus impact, support tickets, Auto-Heal candidates, Auto-Learn updates, and Auto-Improve proposals to backlog and controlled revisions. |

# Appendix A. PR/MR Evidence Summary Template

### AIRA Dynamic Workspace PR/MR Evidence Summary
- Ticket / ADR / TDL / Waiver:
- Owner / Maker / Checker / Approver:
- Bounded Context and Classification:
- Affected Workspace / Screen / Component / Widget:
- Affected API / Event / Schema / Policy / MicroFunction:
- AI tools or agents used:
- Build and quality evidence:
- Contract evidence:
- Security evidence:
- OPA/SBAC evidence:
- Accessibility and visual evidence:
- Observability evidence:
- GitNexus impact evidence:
- Resilience / idempotency / replay evidence:
- Rollback / disablement / compensation plan:
- Known limitations and follow-up backlog:
- EDP-01 to EDP-20 impact:
- AVCI summary:

# Appendix B. Evidence Pack Manifest Skeleton

evidence_pack:
  id: EVD-DW-YYYY-NNN
  source_ref: <ticket/pr/commit/adr>
  classification: INTERNAL_CONFIDENTIAL
  owner: <named owner>
  artifact_refs:
    build: <artifact hash / image digest>
    contracts: <openapi / asyncapi / schema refs>
    policies: <opa bundle version>
    microfunctions: <transaction codes>
    screenshots: <redacted visual regression refs>
  verification:
    tests: <unit/component/e2e/a11y/visual/resilience>
    security: <sast/sca/secrets/dast/sbom/container>
    policy: <opa/sbac/fail-closed>
    observability: <trace/log/metric/audit dashboard refs>
  gitnexus:
    report_ref: <commit-bound report>
    affected_tests: <list>
    architecture_drift: <none/findings>
  promotion:
    maker: <name>
    checker: <name>
    approver: <name>
    cab_arb: <reference if applicable>
    rollback: <disable/rollback/forward-fix/compensation>
  improvement:
    backlog_ref: <optional>
    auto_heal_candidate: <optional>

# Appendix C. External Alignment Reference
| Reference | Use in This Guide |
| --- | --- |
| OWASP ASVS 5.0.0 | Application/API security verification, authenticated testing, secure APIs, abuse-case coverage, and remediation evidence. |
| OWASP Web Security Testing Guide / OWASP guidance | DAST, authenticated testing, vulnerability verification, test evidence, and secure remediation discipline. |
| W3C WCAG 2.2 / WAI guidance | Accessibility target, keyboard/focus/screen-reader behavior, responsive design, and test evidence. |
| OpenTelemetry Semantic Conventions | Trace, metric, log, span/event, and GenAI-related telemetry conventions where applicable. |
| SLSA v1.2 | Supply-chain provenance, artifact integrity, attestation, build control, and release evidence. |
| NIST AI RMF / GenAI Profile | AI panel risk management, model route governance, guardrail and evidence discipline. |

# Appendix D. Final Release Readiness Checklist

All required CI stages are passing or approved with non-expired waiver and compensating control.

No Critical or High security finding remains open without approved waiver and remediation plan.

OpenAPI/AsyncAPI/schema/policy compatibility is proven and generated clients are current.

All affected MicroFunction bindings have idempotency, audit/outbox, OPA/SBAC, evidence, and rollback proof.

Accessibility, responsive, visual, and Playwright tests pass across approved personas and breakpoints.

Observability dashboards, Sentry release, Loki/Tempo/Grafana correlation, and forbidden telemetry tests are complete.

GitNexus report is commit-bound, derivative, and corroborated by tests/scans/human review.

Promotion request has maker, checker, approver, CAB/ARB if applicable, and rollback/safe-disable path.

Post-promotion monitoring window and improvement backlog are defined.

# Appendix E. Final Adoption Rule
| Final Rule. AIRA may accelerate Dynamic Workspace, Admin Builder, AI Assistant Panel, and System Builder delivery only when backend authority, contracts, OPA/SBAC, guardrails, evidence, tests, observability, rollback, and human approval remain intact. Artifacts that weaken these controls must be rejected, quarantined, or waived with expiry and remediation plan. |
| --- |

