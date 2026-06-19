---
title: "Dynamic Workspace Admin Builder and Template Governance Standard"
doc_id: "AIRA-54"
version: "v1.1"
status: "revised"
category: "Dynamic workspace"
source_docx: "AIRA_54_Dynamic_Workspace_Admin_Builder_and_Template_Governance_Standard_v1.1_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 46-60-dynamic-workspace
  - revised
  - aira-54
---



# Dynamic Workspace Admin Builder and Template Governance Standard



AIRA
AI-Native Enterprise Platform
Dynamic Workspace Admin Builder and Template Governance Standard
Admin Builder Control | Template Lifecycle | Runtime Activation | Evidence by Construction | AVCI Always

Figure 54-1. Admin Builder template lifecycle and mandatory control gates.
| Document ID | AIRA-DOC-054 |
| --- | --- |
| Canonical Filename | 54-AIRA_Dynamic_Workspace_Admin_Builder_and_Template_Governance_Standard_v1.1_Revised.docx |
| Version | v1.1 - Dynamic Workspace / MicroFunction / DevSecOps Alignment Revision |
| Supersedes | 54-AIRA_Dynamic_Workspace_Admin_Builder_and_Template_Governance_Standard_v1.0 |
| Classification | INTERNAL CONFIDENTIAL |
| Status | DRAFT FOR ARCHITECTURE REVIEW BOARD / CAB APPROVAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; Platform Engineering; AI Engineering; Data Governance; SRE; Internal Audit |
| Primary Audience | Solutions Architects; Frontend Developers; Backend Developers; DevSecOps; QA/SDET; Security; Product Owners; Internal Audit |
| Effective Date | Upon ARB / CAB approval |
| Review Cadence | Quarterly; unscheduled on material template, Dynamic Workspace, MicroFunction, security, AI, workflow, database, observability, or DevSecOps change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Dynamic-Workspace / Admin-Builder / v1.1/ |

Mandatory Practice Statement

The AIRA Admin Builder is a governed configuration and template authoring control plane. It may create, validate, route, approve, activate, deactivate, roll back, supersede, and retire workspace templates only through approved components, contracts, policies, MicroFunction bindings, evidence gates, and maker-checker approval. It must never become an uncontrolled low-code runtime, arbitrary script engine, policy bypass, direct SQL path, direct model-provider path, direct production mutation path, or self-approving AI automation path.

v1.1 Control Rule: No template, screen, Experience Block, component assignment, action binding, AI panel configuration, or layout change may become active unless it is attributable, verifiable, classifiable, improvable, policy-filtered, contract-bound, test-proven, observable, reversible, and approved by the required human role.

# Static Table of Contents

1. Executive Summary and v1.1 Upgrade Verdict

2. Purpose, Scope, and Authority

3. Source Baseline and Cross-Document Positioning

4. Admin Builder Control Model

5. Template Lifecycle and State Model

6. Roles, RACI, and Separation of Duties

7. Template and Configuration Object Model

8. Contract, MicroFunction, Workflow, and Event Binding Rules

9. Security, Classification, OPA/SBAC, and Abuse-Case Controls

10. DevSecOps Pipeline, Evidence Pack, and GitNexus Gates

11. Observability, Audit, Runtime Toggles, and Dashboards

12. Accessibility, UX, Responsive, and Safe State Requirements

13. Concurrency, Idempotency, Outbox, Replay, and Resilience Lab

14. Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop

15. Reversibility, Rollback, Deactivation, and Retirement

16. Roadmap, Acceptance Criteria, and Definition of Done

17. Open Reconciliation Items

18. AVCI Compliance Summary

Appendix A. Admin Builder PR/MR and Activation Evidence Checklist

Appendix B. EDP-01 through EDP-20 Control Mapping

# 1. Executive Summary and v1.1 Upgrade Verdict

This v1.1 revision upgrades AIRA-DOC-054 from a concise Admin Builder template-governance baseline into an enterprise-grade implementation and control standard. It preserves the v1.0 intent: authorized administrators configure approved building blocks, but they do not create uncontrolled code, APIs, SQL, policies, model calls, or business logic.

The revision aligns the Admin Builder with the Dynamic Workspace implementation family, MicroFunction backend assembly, contract-first API/event governance, DevSecOps evidence gates, GitNexus impact analysis, OPA/SBAC policy enforcement, observability, accessibility, resilience, and proposal-driven continuous improvement.
| Strategic Outcome | v1.1 Required Result |
| --- | --- |
| Admin Builder speed without control loss | Templates are metadata-driven, but activation is blocked until validation, evidence, maker-checker review, and rollback are complete. |
| Backend authority preserved | The browser and Admin Builder request changes; backend APIs, MicroFunctions, workflow, database constraints, and OPA/SBAC remain authoritative. |
| Contract-first binding | Templates bind only to approved OpenAPI/AsyncAPI contracts, generated clients, Action Registry entries, schema versions, and MicroFunction transaction codes. |
| Runtime-safe activation | Activation uses signed template versions, feature flags, cache invalidation, observability proof, audit, and safe deactivation. |
| AI-assisted, not AI-authorized | AI may recommend layouts, content, tests, and improvement candidates, but cannot approve, activate, deploy, or mutate production. |

# 2. Purpose, Scope, and Authority

## 2.1 Purpose

Define how AIRA templates, screen templates, layout definitions, component assignments, Experience Blocks, and action bindings are authored, reviewed, tested, approved, activated, monitored, rolled back, superseded, and retired.

Prevent the Admin Builder from becoming an uncontrolled low-code platform, policy bypass, direct production mutation path, or arbitrary script execution engine.

Establish template lifecycle states, maker-checker duties, evidence gates, API/event bindings, policy controls, observability signals, and rollback obligations.

Ensure every Admin Builder output satisfies EDP-01 through EDP-20 and AVCI.

## 2.2 In Scope and Out of Scope
| Area | Treatment |
| --- | --- |
| In Scope | Workspace templates, screen templates, component placements, layout grids, Experience Blocks, UI content, data-visibility metadata, action bindings, AI panel configuration, template activation workflow, evidence, rollback, and retirement. |
| Out of Scope | Custom backend Java code generation inside the Admin Builder, arbitrary JavaScript/SQL, direct database mutation, direct model-provider calls, direct workflow mutation, direct Kubernetes/CI/Git actions, and production activation without approval. |

## 2.3 Authority and Precedence
| Level | Source / Control | Governs |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance | Final authority for production-impacting template activation, security exception, policy exception, and rollback decisions. |
| L1 | 01 AVCI, 01A Enterprise Design Principles, 02 Engineering Blueprint, 11 DevSecOps, 17 Security | Cross-cutting authority for evidence, architecture, security, policy, promotion, and rollback. |
| L2 | This 54 Standard | Canonical authority for Admin Builder template lifecycle, template activation workflow, and Admin Builder authority boundaries. |
| L2 | 12A, 46-53, 55-61 Dynamic Workspace Standards | Companion implementation, UX, observability, API, database, DevSecOps, and AI-assisted workspace standards. |
| L3 | OpenAPI/AsyncAPI, Flyway, OPA bundles, CI/CD, tests, tickets, PR/MR, evidence records | Executable implementation proof and operational evidence. |

Conflict rule: if this standard appears inconsistent with a higher-authority AIRA standard, the stricter control applies temporarily, the conflict is logged as an AVCI reconciliation item, and the governing source is confirmed through the canonical register / 00D path.

# 3. Source Baseline and Cross-Document Positioning

The v1.0 source standard already defines the Admin Builder as a controlled configuration tool for creating, editing, reviewing, approving, activating, deactivating, rolling back, and retiring workspace templates. It expressly states that admins configure approved building blocks and do not create uncontrolled code, APIs, policies, SQL, or business logic.

This v1.1 revision does not replace the Dynamic Workspace framework. It specializes the admin/template lifecycle and must be read with the Dynamic Workspace observability, configuration seeding, frontend reference implementation, Experience Block authoring, prompt/artifact governance, UX/accessibility, DevSecOps evidence, and AI-assisted System Builder standards.
| Companion Standard | Required Treatment for AIRA-DOC-054 |
| --- | --- |
| 53 Observability, Audit, and Evidence | Defines telemetry, audit events, evidence records, dashboards, and forbidden telemetry fields that Admin Builder changes must emit. |
| 54 This Standard | Defines template authoring, approval, activation, rollback, retirement, and Admin Builder authority boundaries. |
| 55 Configuration Seeder and Runtime Synchronization | Must implement seed, sync, cache, environment, and runtime propagation of approved template versions. |
| 56 Frontend Reference Implementation | Must render only backend-resolved, policy-filtered templates and component states. |
| 57 Experience Block and Experience Pack Authoring | Must constrain reusable blocks, pack packaging, ownership, and compatibility. |
| 58 Prompt/Artifact/Response Governance | Must govern AI prompts and AI-generated UX suggestions used by the Admin Builder. |
| 59 UX Accessibility and Responsive Design | Must govern usability, accessibility, responsive layout, and safe states before template activation. |
| 60 Dynamic Workspace DevSecOps Pipeline | Must produce the evidence gates required before template activation or frontend source promotion. |
| 61 AI-Assisted Dynamic Workspace and System Builder | Must govern AI-assisted suggestions, diagnostics, candidate generation, and approval routing. |

# 4. Admin Builder Control Model

The Admin Builder is a governed workspace for authorized makers, reviewers, approvers, and auditors. It provides controlled configuration authoring, validation, workflow routing, preview, and activation-request capabilities. It is not an application runtime authority.

Figure 54-2. Admin Builder authority boundary: what the builder may do and must block.
| Control Plane Element | Mandatory Responsibility |
| --- | --- |
| Component Catalog | Allow-list only; new components require PR/MR or registry workflow, tests, accessibility contract, and security review. |
| Template Registry | PostgreSQL/Flyway-governed authority for template metadata, versions, approvals, activation records, and rollback references. |
| Action Registry | Maps UI actions to approved backend API, capability code, MicroFunction transaction, idempotency profile, and policy binding. |
| Policy Control Plane | OPA/SBAC/RBAC/ABAC evaluates authoring permission, reviewer authority, activation eligibility, visibility, editability, and action risk. |
| Evidence Store | Records lifecycle changes, validation results, approvals, audit events, runtime traces, and post-activation monitoring. |
| Runtime Resolver | Resolves active template versions, feature flags, policy-filtered components, user preferences, cache state, and safe fallback. |

# 5. Template Lifecycle and State Model

Every template must move through explicit states. State transition is not a label change; it is a governance event with owner, source, validation, policy decision, evidence, and rollback path.
| State | Meaning | Allowed Actions | Control Rule |
| --- | --- | --- | --- |
| DRAFT | Initial or edited template/configuration. | Edit, preview with safe data, validate, submit for review. | Cannot affect runtime users. |
| VALIDATION_FAILED | One or more schema, policy, accessibility, contract, security, test, or evidence gates failed. | Return to maker with evidence and remediation. | Cannot be submitted until corrected. |
| FOR_REVIEW | Validation passed and human review is required. | Review, comment, return, approve, reject. | Maker cannot self-approve high-risk or production changes. |
| APPROVED | Approved but not yet active. | Schedule activation, prepare rollback, validate cache plan. | Activation still requires environment/promotion control. |
| ACTIVE | Current runtime template version. | Monitor, supersede, deactivate, rollback. | Runtime must emit telemetry and evidence. |
| SUPERSEDED | Replaced by newer version. | Read-only historical reference. | Cannot be reactivated without new validation. |
| ROLLED_BACK | Reverted from failed or unsafe version. | Keep evidence, RCA, remediation backlog. | Requires root-cause review. |
| RETIRED | No longer available for assignment. | Historical/audit only. | Cannot be assigned to new users. |

# 6. Roles, RACI, and Separation of Duties
| Role | Responsibility | Restriction |
| --- | --- | --- |
| Template Maker | Drafts and revises templates, layout, labels, help text, and configuration within assigned scope. | Cannot approve own template or activate production version. |
| UX Reviewer | Reviews usability, accessibility, task flow, responsive behavior, safe states, and design-system compliance. | Cannot override security, API, or architecture gates. |
| Security Reviewer | Reviews classification, redaction, data exposure, OPA/SBAC binding, CSP, browser storage, and abuse cases. | Cannot approve business acceptance alone. |
| Architecture Reviewer | Reviews bounded context, contract binding, MicroFunction binding, ports/adapters, and architectural fitness. | Cannot waive security or audit controls alone. |
| QA/SDET Reviewer | Reviews tests, visual baselines, Playwright, accessibility automation, contract tests, and regression risk. | Cannot waive critical/high failures without formal waiver. |
| Product Owner | Confirms business fit, mandatory widgets, wording, workflow fit, and readiness. | Cannot override fail-closed technical/security gates. |
| Template Promoter | Promotes approved version to target environment through controlled workflow. | Must be separated from maker for high-risk or production changes. |
| Internal Audit | Reviews evidence, segregation of duties, exception records, and lifecycle history. | Read-only; cannot alter templates. |
| AI Assistant / Agent | May recommend, draft, compare, generate candidate tests, or identify drift. | Cannot approve, activate, merge, deploy, or mutate production. |
| Activity | Maker | UX | Security | Architecture | QA | Product | Promoter | Audit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Create draft | R | C | C | C | C | C | I | I |
| Submit for review | R | C | C | C | C | C | I | I |
| Approve UX/accessibility | C | A/R | C | C | R | C | I | I |
| Approve security/policy | C | C | A/R | C | C | C | I | I |
| Approve architecture/contract | C | C | C | A/R | C | C | I | I |
| Approve business readiness | C | C | C | C | C | A/R | I | I |
| Promote activation | I | C | C | C | C | C | A/R | I |
| Audit evidence | I | I | I | I | I | I | I | A/R |

# 7. Template and Configuration Object Model

The Admin Builder may manage configuration records only through approved registry APIs and Flyway-governed schemas. PostgreSQL is authoritative. Redis/Valkey/Caffeine caches accelerate runtime resolution but must never become authority.
| Object | Definition and Governance Requirement |
| --- | --- |
| Workspace Template | Container for screens assigned by tenant, role, skill, branch, department, user type, or experience pack. |
| Screen Template | Page-level metadata: route, layout, title, policy, responsive behavior, evidence profile, safe state rules. |
| Experience Block | Reusable group of components, text, actions, policies, states, and evidence bindings. |
| Component Catalog Entry | Approved frontend component definition with props schema, accessibility contract, security constraints, and version. |
| Widget Instance | Specific component placement within a screen, including display policy, data source, action binding, and state model. |
| Capability Binding | Mapping to approved API operation, action code, MicroFunction transaction, idempotency profile, OPA/SBAC policy, audit profile. |
| Policy Binding | OPA package, SBAC skill, roles, attributes, tenant/branch scope, classification ceiling, editability/visibility rules. |
| Feature Flag Binding | Rollout, enablement, disablement, rollback, environment, and safe fallback control. |
| Template Evidence Record | AVCI evidence record linking version, owner, source, validation, policy, tests, approvals, activation, rollback, and monitoring. |

# 8. Contract, MicroFunction, Workflow, and Event Binding Rules

The Admin Builder must not invent endpoints, payloads, error semantics, roles, event schemas, or action semantics. All bindings must reference approved contracts and registries.
| Binding Area | Mandatory Rule |
| --- | --- |
| OpenAPI | UI actions and data widgets bind to operation_id, version, error model, classification, idempotency, and generated client evidence. |
| AsyncAPI / Kafka / CloudEvents | Event-driven widgets and notifications reference topic/channel, CloudEvent type, Avro/JSON schema, compatibility policy, DLQ, replay, and consumer group rules. |
| Avro / JSON Schema | Template payloads, component props, action request bodies, and event schemas must validate against registered versions. |
| MicroFunction | Mutating action bindings must declare transaction_code, standard step sequence, idempotency profile, audit profile, outbox event, error policy, and compensation. |
| Flowable / Temporal | Human approvals, exception reviews, long-running tasks, and compensating actions must route through approved workflow contracts. |
| Outbox and Replay | Template-triggered backend mutations that publish events require transactional outbox, idempotent consumers, DLQ handling, and replay governance. |

For production-impacting template changes, contract compatibility and generated-client validation must run before activation. If a backend operation is missing or incompatible, the template must remain in draft or rework state.

# 9. Security, Classification, OPA/SBAC, and Abuse-Case Controls
| Control | Required Treatment |
| --- | --- |
| Default deny | Missing identity, template state, policy binding, classification, schema, contract, or audit profile blocks protected authoring and runtime activation. |
| Least privilege / SBAC | Makers, reviewers, promoters, agents, and service accounts receive only allowed skills, actions, scopes, environments, and classification ceilings. |
| Classification-aware preview | Preview uses synthetic, masked, or approved non-production data. Restricted or raw PII preview is prohibited unless explicitly authorized and audited. |
| OPA/SBAC policy tests | Visibility, editability, action invocation, approval routing, self-approval blocking, tenant/branch scope, and classification decisions require positive/negative tests. |
| Browser safety | No unsafe HTML, inline script, dynamic code execution, token storage, secret exposure, raw JWT, direct model call, or unapproved external resource. |
| Authenticated DAST | Admin Builder and activated template flows require authenticated DAST for privileged routes, template endpoints, action invocations, and policy-denied states. |
| Abuse cases | Test unauthorized template activation, hidden-field exposure, action-binding tampering, self-approval, stale cache, replayed approval, prompt injection in UI content, and downgrade attacks. |
| Secrets hygiene | No secrets in template metadata, screenshots, logs, prompts, tests, localStorage, sessionStorage, browser cache, or evidence summaries. |

# 10. DevSecOps Pipeline, Evidence Pack, and GitNexus Gates

Admin Builder changes may be metadata/configuration changes rather than frontend source code changes, but they remain governed engineering artifacts. They must pass validation, security, evidence, approval, and rollback gates before activation.
| Gate | Required Evidence |
| --- | --- |
| Schema and registry validation | Template metadata validates against registry schema, component schema, responsive grid bounds, feature flags, and compatibility rules. |
| Contract compatibility | OpenAPI, AsyncAPI, schema, generated clients, action registry, error contract, idempotency, and policy binding are compatible. |
| Policy and security gates | OPA tests, SBAC checks, classification, CSP, browser storage tests, secrets scan, SAST/SCA where applicable, authenticated DAST for admin flows. |
| Accessibility and UX gates | WCAG 2.2 AA target, keyboard navigation, focus order, screen-reader semantics, responsive behavior, safe states, visual regression, and Playwright smoke. |
| GitNexus impact evidence | Read-only impact analysis identifies affected components, contracts, tests, routes, MicroFunctions, policies, and evidence records; it cannot approve or activate changes. |
| SBOM/provenance | Required for frontend source, generated packages, component libraries, and release artifacts; template metadata must link to source version and validation run. |
| Evidence pack finalization | PR/MR evidence, CI run, test reports, security scans, policy results, approval records, activation record, rollback plan, and monitoring plan are attached. |

Figure 54-3. Evidence correlation required for template activation and reconstruction.

# 11. Observability, Audit, Runtime Toggles, and Dashboards

Admin Builder operations and activated templates must emit trace, metric, log, audit, and evidence signals. Runtime performance tuning is allowed, but non-disableable security, audit, policy, evidence, and incident signals must remain active.
| Signal / Dashboard | Required Treatment |
| --- | --- |
| Trace fields | trace_id, span_id, request_id, actor_id_hash, tenant_id, workspace_code, screen_code, component_key, template_version, policy_ref, evidence_ref. |
| Audit events | TEMPLATE_DRAFT_CREATED, TEMPLATE_VALIDATED, TEMPLATE_SUBMITTED, TEMPLATE_APPROVED, TEMPLATE_ACTIVATED, TEMPLATE_ROLLED_BACK, TEMPLATE_RETIRED, ACTION_BINDING_CHANGED, CONFIG_CACHE_INVALIDATED. |
| Metrics | Validation failure rate, activation success/failure, rollback rate, policy-deny rate, slow template resolution, cache hit/miss, accessibility defects, evidence completeness. |
| Logs | Structured diagnostic logs only; no passwords, tokens, raw JWTs, secrets, raw PII, raw documents, raw prompts, or high-cardinality metric labels. |
| Dashboards | Admin template lifecycle, approval backlog, failed gates, activation health, rollback history, policy denials, evidence completeness, DAST/security findings, accessibility drift. |
| Runtime toggles | Verbose debug logs may be temporarily enabled with approval and time-bound expiry; security/audit/evidence/policy signals cannot be disabled. |

# 12. Accessibility, UX, Responsive, and Safe State Requirements
| UX / Accessibility Area | Control Requirement |
| --- | --- |
| Keyboard and focus | All Admin Builder screens, dialogs, grids, drag/drop replacements, approval forms, and rollback actions must be keyboard-operable with visible focus. |
| Screen reader semantics | Labels, regions, tables, alerts, validation errors, dialog roles, form hints, and state changes must be accessible. |
| Responsive rules | Templates declare breakpoint behavior, minimum/maximum dimensions, overflow handling, print/export treatment, and safe mobile/tablet limits. |
| Widget safe states | Loading, empty, denied, disabled, stale, partial, error, retrying, requires approval, and degraded states are required. |
| Error and warning copy | User-visible text must be safe, clear, non-sensitive, localized where needed, and actionable without exposing internal controls or exploit signals. |
| Visual regression | Critical Admin Builder and activated template flows require visual baseline testing before activation. |

# 13. Concurrency, Idempotency, Outbox, Replay, and Resilience Lab

Admin Builder activation is a high-integrity configuration operation. It must be safe under concurrent edits, repeated submit/approve/activate requests, stale caches, partial failures, and retry/replay scenarios.
| Scenario | Required Behavior |
| --- | --- |
| Concurrent editing | Optimistic locking or version checks block lost updates. Makers must rebase/review when template base version changes. |
| Idempotent submit/approve/activate | Submit, approve, activate, deactivate, rollback, and retire operations require idempotency keys and duplicate-safe outcomes. |
| Cache invalidation | Activation/deactivation/rollback emits config.changed event and invalidates L1/L2 caches; stale cache must fail safe or refresh. |
| Transactional outbox | Activation and rollback events are written atomically with authoritative registry state and published through governed outbox. |
| DLQ and replay | Failed sync, cache invalidation, or event publication routes to DLQ with replay controls, owner, evidence, and no duplicate activation effects. |
| Resilience Lab | Tests must simulate duplicate activation clicks, stale template reads, concurrent approvals, OPA outage, DB timeout, Kafka failure, cache inconsistency, and rollback under load. |

# 14. Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop

Admin Builder telemetry, validation failures, accessibility defects, policy denials, and runtime incidents may feed continuous improvement. The loop is proposal-driven only.
| Loop Stage | Mandatory Treatment |
| --- | --- |
| Issue detection | Detect recurring validation failure, template render error, policy denial spike, accessibility regression, slow workspace load, unsafe content, or failed activation. |
| Evidence retrieval | Retrieve trace, logs, test output, GitNexus impact, template version, policy decision, contract version, and affected user journey. |
| Candidate proposal | Generate candidate fix, updated template, rollback recommendation, test improvement, policy clarification, or documentation update. |
| Validation | Run schema, contract, OPA/SBAC, accessibility, visual, Playwright, security, Resilience Lab, and evidence checks. |
| Human approval | Maker-checker and required reviewers approve before merge, activation, knowledge promotion, or policy update. |
| Post-action monitoring | Observe rollback rate, defect closure, SLO recovery, user impact, and recurrence; update backlog or runbook. |

Auto-Heal may recommend rollback or deactivate an unsafe template only when the action path is pre-approved, time-bound, reversible, policy-gated, observable, and has human approval where risk requires. Auto-Learn may draft knowledge artifacts only. Auto-Improve may propose refactoring or template changes only through PR/MR or registry workflow.

# 15. Reversibility, Rollback, Deactivation, and Retirement
| Scenario | Required Response |
| --- | --- |
| Broken rendering | Activate previous known-good template version or safe fallback; alert owner; record incident and evidence. |
| Sensitive data exposure risk | Immediately deactivate affected template/action, invalidate caches, preserve evidence, trigger security review, and notify required owners. |
| Wrong action binding | Disable action binding, restore previous binding, run contract/policy regression, and review Action Registry. |
| Accessibility critical regression | Rollback or hotfix if critical flow is blocked; create defect with owner and evidence. |
| Policy failure or OPA outage | Fail closed; hide protected components/actions; no default allow. |
| AI panel unsafe behavior | Disable affected prompt/panel config, preserve prompt/guardrail audit, and route to AI Governance. |
| Template retirement | Remove from future assignment, preserve lifecycle/evidence history, retain according to classification and retention rule. |

# 16. Roadmap, Acceptance Criteria, and Definition of Done
| Milestone | Outcome | Exit Evidence |
| --- | --- | --- |
| M1 | Confirm canonical registry schema, lifecycle states, evidence schema, and OPA input model. | Architecture + Security + DBA approval. |
| M2 | Implement Admin Builder draft/edit/validate/submit/review/approve workflow for non-production templates. | Local/UAT workflow evidence. |
| M3 | Add OpenAPI/AsyncAPI, MicroFunction, Action Registry, policy, and schema compatibility checks. | Contract and policy test evidence. |
| M4 | Add accessibility, visual regression, Playwright, authenticated DAST, and Resilience Lab gates. | CI/CD evidence pack. |
| M5 | Enable controlled activation, rollback, feature flag, cache invalidation, audit, dashboards, and runtime monitoring. | UAT + CAB/ARB evidence. |
| M6 | Enable Auto-Heal/Auto-Learn/Auto-Improve proposal loop for template governance. | Candidate workflow with human approval. |

Definition of Done: A template is done only when it has owner, source, version, classification, contracts, policy bindings, schema validation, tests, accessibility evidence, security evidence, GitNexus impact, approval, activation record, observability proof, rollback plan, and improvement path.

# 17. Open Reconciliation Items
| ID | Reconciliation Item | Priority | Owner |
| --- | --- | --- | --- |
| 54-R01 | Confirm whether 54 remains the canonical Admin Builder lifecycle standard while 54/61 overlap on AI-assisted System Builder template generation. | Medium | 00D / Master Register |
| 54-R02 | Propagate non-disableable telemetry rules into 53, 55, 56, 60, SRE, and observability runbooks where not explicit. | High | Observability + DevSecOps |
| 54-R03 | Ensure canonical aira_ui schema names, table names, and activation APIs align with 48/49/55 before implementation. | High | DBA + API Architecture |
| 54-R04 | Add Admin Builder abuse-case and authenticated DAST scenarios to security and testing standards. | High | Security + QA/SDET |
| 54-R05 | Ensure OpenAPI/AsyncAPI/Kafka/Avro/CloudEvents replay matrix is included in System Builder template proposal forms. | Medium | API Architecture + System Builder Owner |

# 18. AVCI Compliance Summary
| AVCI Property | Evidence in This Standard |
| --- | --- |
| Attributable | Defines document owner, co-owners, lifecycle roles, maker/checker/approver/auditor responsibilities, template owner, source_ref, version, and evidence path. |
| Verifiable | Requires schema, contract, OPA/SBAC, accessibility, visual, Playwright, authenticated DAST, Resilience Lab, GitNexus, CI/CD, approval, telemetry, and rollback evidence. |
| Classifiable | Requires template classification, component/data/action classification, preview data controls, forbidden telemetry fields, redaction, retention, and classification-aware policy. |
| Improvable | Defines Auto-Heal/Auto-Learn/Auto-Improve candidate loop, dashboards, recurring defect feedback, reconciliation items, backlog linkage, and review cadence. |

# Appendix A. Admin Builder PR/MR and Activation Evidence Checklist

Ticket, source request, owner, maker, checker, approver, classification, affected workspace, affected screen, and affected component recorded.

Template metadata, component schema, layout bounds, responsive behavior, feature flags, and safe states validated.

OpenAPI/AsyncAPI/schema/action registry/MicroFunction/workflow bindings referenced and compatibility-checked.

OPA/SBAC tests include allow, deny, self-approval rejection, tenant/branch mismatch, classification ceiling, and missing-skill paths.

Accessibility, visual regression, Playwright, contract, security, authenticated DAST, and Resilience Lab evidence attached.

GitNexus read-only impact summary attached where source/config impact analysis applies.

Telemetry/evidence sample includes trace_id, template_version, policy_ref, evidence_ref, and audit event.

Rollback, safe deactivation, feature flag, previous active version, cache invalidation, and DLQ/replay plan recorded.

Known limitations, waiver decisions, open issues, and improvement backlog entered.

# Appendix B. EDP-01 through EDP-20 Control Mapping
| Principle | Admin Builder Enforcement |
| --- | --- |
| EDP-01 SOLID | Admin Builder services, template validators, registries, and adapters remain single-purpose and interface-driven. |
| EDP-02 Clean Architecture | Template metadata and UI do not own domain, database, policy, model, or workflow logic. |
| EDP-03 DDD / Bounded Contexts | Templates and actions declare owning bounded context and approved integration boundary. |
| EDP-04 Ports and Adapters | APIs, workflow, Kafka, Redis, database, model gateways, and evidence stores are accessed through explicit ports/adapters. |
| EDP-05 DRY, KISS, YAGNI | Reuse approved components, Experience Blocks, contracts, templates, and MicroFunction patterns. |
| EDP-06 Idempotency by Design | Submit, approve, activate, deactivate, rollback, retire, and widget action requests are duplicate-safe. |
| EDP-07 Determinism and Reproducibility | Runtime rendering is reproducible from template version, policy version, feature flags, user preference, and contract versions. |
| EDP-08 Fail-Safe, Not Fail-Open | Missing identity, policy, classification, schema, contract, audit, or cache validation blocks protected actions. |
| EDP-09 Human-in-the-Loop | High-risk template activation, policy exceptions, production changes, and AI-generated proposals require human approval. |
| EDP-10 Least Privilege / SBAC | Makers, reviewers, promoters, agents, and services receive only approved skills, tools, data scope, and environment authority. |
| EDP-11 Separation of Duties | Maker, checker, security reviewer, promoter, approver, and auditor roles remain separable. |
| EDP-12 Observability by Design | Template lifecycle, runtime rendering, policy denials, cache invalidations, and action invocations emit safe telemetry. |
| EDP-13 Policy as Code | Visibility, editability, activation, approval, action binding, and classification controls use OPA/SBAC policies. |
| EDP-14 Testability by Design | Schema, contract, policy, accessibility, visual, Playwright, DAST, and Resilience Lab tests are mandatory. |
| EDP-15 Secure by Design | No unsafe script, token exposure, arbitrary SQL, direct provider SDK, unapproved data exposure, or secrets in metadata/evidence. |
| EDP-16 Resilience Patterns | Timeout, retry, circuit breaker, cache refresh, DLQ, replay, compensation, rollback, and safe fallback are explicit. |
| EDP-17 Architectural Fitness Functions | CI and registry validation reject boundary violations, unsafe bindings, invented endpoints, and missing evidence. |
| EDP-18 Progressive Autonomy | AI suggests and drafts only; activation and protected actions remain governed by trust, policy, approval, and evidence. |
| EDP-19 Reversibility / Rollbackability | Every active template has rollback, deactivation, previous version, feature flag, cache invalidation, and retention path. |
| EDP-20 AVCI | Every artifact is attributable, verifiable, classifiable, and improvable across draft, review, activation, runtime, and retirement. |

# Appendix C. External Alignment Reference Note

This revision was checked against current external practice areas relevant to Admin Builder and template governance: W3C WCAG 2.2 / WAI guidance for accessibility, OWASP ASVS 5.0.0 for application-security verification, OpenTelemetry semantic conventions including GenAI observability attributes, and SLSA v1.2 supply-chain integrity guidance. External sources inform controls but do not override AIRA canonical governance.

