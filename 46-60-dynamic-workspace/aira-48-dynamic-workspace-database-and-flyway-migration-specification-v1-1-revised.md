---
title: "Dynamic Workspace Database and Flyway Migration Specification"
doc_id: "AIRA-48"
version: "v1.1"
status: "revised"
category: "Dynamic workspace"
source_docx: "AIRA_48_Dynamic_Workspace_Database_and_Flyway_Migration_Specification_v1.1_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 46-60-dynamic-workspace
  - revised
  - aira-48
---



# Dynamic Workspace Database and Flyway Migration Specification



AIRA

AI-Native Enterprise Platform

Dynamic Workspace Database and Flyway Migration Specification

Physical Schema | Flyway Sequencing | Runtime Configuration | MicroFunction Binding | Evidence by Construction | AVCI Always

AIRA-DOC-048 | Version v1.1 Revised | INTERNAL CONFIDENTIAL
| Mandatory Practice Statement | The AIRA Dynamic Workspace database is a governed runtime-control surface. PostgreSQL is authoritative for workspace templates, screen templates, component catalogs, layout definitions, capability bindings, AI capability metadata, policy bindings, evidence profiles, activation states, and user personalization overlays. Redis/Valkey may accelerate only derivative resolved views. All schemas, tables, indexes, constraints, seed/reference data, RLS policies, views, cache-invalidation metadata, and runtime database changes must be delivered through Flyway or an approved migration workflow with CI/CD evidence, security review, rollback/forward-fix path, and AVCI traceability. |
| --- | --- |

# Document Control
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-048 |
| Canonical Filename | 48-AIRA_Dynamic_Workspace_Database_and_Flyway_Migration_Specification_v1.1_Revised.docx |
| Version | v1.1 - Revised Dynamic Workspace, Flyway, MicroFunction, API/Eventing, Observability, Resilience, and AI Governance Alignment |
| Status | Draft for Architecture Board, CAB, DBA, Security, DevSecOps, Frontend, Backend, QA/SDET, Platform Engineering, AI Governance, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Workspace Platform Team; DBA; Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; Platform Engineering; AI Governance; SRE; Internal Audit |
| Supersedes | 48-AIRA_Dynamic_Workspace_Database_and_Flyway_Migration_Specification_v1.0 |
| Primary Parent / Companions | 41 Dynamic User Workspace Framework; 42 Composable Experience Framework; 46 Configuration, Parameter, and Runtime Cache; 47 Developer Implementation Guide; 49 API/OpenAPI Contract Specification; 50 Component/Widget Development; 51 Security/OPA/SBAC/ABAC; 52 Testing and Fitness Functions; 53 Observability; 54 Admin Builder; 55 Seeder/Runtime Synchronization; 60 Dynamic Workspace DevSecOps Evidence; 15/15A API; 16/16A/16B Database/Flyway; 17/17A Security; 20/45 CI/CD and PoC 2; 31/31A Operations and Observability |
| External Alignment Checked | NIST SSDF SP 800-218; OWASP ASVS 5.0.0; OpenTelemetry Semantic Conventions; SLSA v1.2 supply-chain provenance |

# Static Table of Contents

Executive Summary and Revision Verdict

Purpose, Scope, Authority, and Source Alignment

Authoritative Schema Ownership and Core Data Model

Flyway Migration Sequencing, Seed Data, and CI/CD Gates

Runtime Resolution, Cache Synchronization, and Runtime Toggles

MicroFunction, API/Eventing, Outbox, DLQ/Replay, and Workflow Integration

Security, Observability, Evidence, Testing, and Resilience Lab

RACI, Acceptance Criteria, and AVCI Summary

# 1. Executive Summary and v1.1 Revision Verdict

This revised specification upgrades AIRA-DOC-048 from a physical database specification for the Dynamic Workspace into the database execution authority for the Dynamic Workspace and Composable Experience Framework. It preserves the original v1.0 position that PostgreSQL is authoritative and Redis/Valkey is derivative, while aligning with the revised database/Flyway standards, API/eventing standards, security/SBAC standards, CI/CD evidence model, observability model, operations controls, and System Builder boundaries.

AIRA Dynamic Workspace database design must support future systems without uncontrolled frontend logic, hardcoded screens, manual database mutation, uncontrolled cache truth, or AI-generated runtime side effects. The database stores governed configuration and runtime-control metadata; the frontend renders only backend-approved definitions; MicroFunctions execute governed backend actions; OPA/SBAC/ABAC policy filters data and actions; CI/CD and Flyway evidence prove trust.
| v1.1 Outcome | Required Result |
| --- | --- |
| Authoritative configuration | Workspace templates, screens, layouts, component catalog, rendering policies, capability bindings, AI capability metadata, evidence profiles, activation states, and personalization overlays are governed artifacts. |
| Flyway-only execution | All physical schema objects, constraints, indexes, seed/reference data, RLS policies, views, and runtime-control tables are delivered through versioned or repeatable Flyway migrations. |
| MicroFunction-backed actions | Every mutating widget action maps to a capability binding, OpenAPI endpoint, backend use case, MicroFunction transaction, idempotency policy, audit event, and evidence record. |
| Cache as acceleration only | Redis/Valkey may cache resolved views, component metadata, policy hashes, and layout snapshots, but PostgreSQL and Git-managed configuration remain the truth. |
| Evidence by construction | Workspace load, policy filtering, admin changes, user personalization, widget actions, AI panel activity, cache invalidation, and replay/rebuild actions must be reconstructable. |

# 2. Purpose, Scope, Authority, and Source Alignment
| Area | Treatment |
| --- | --- |
| Purpose | Define the physical schema, migration sequencing, seed data, constraints, indexes, rollback/forward-fix, runtime synchronization, cache invalidation, security, observability, and evidence requirements for Dynamic Workspace database implementation. |
| In Scope | aira_ui schema, workspace templates, screen templates, component catalog, layout definitions, rendering policies, capability bindings, AI capability metadata, workflow bindings, evidence profiles, user personalization overlays, activation records, cache synchronization metadata, RLS policies, indexes, seed data, and migration evidence. |
| Out of Scope | Frontend authorization authority, direct database calls from UI, arbitrary SQL from Admin Builder, production Flyway clean, direct AI-generated production DDL, uncontrolled Redis truth, unmanaged widget code execution, or direct model-provider/database calls from browser components. |
| Authority | This document governs Dynamic Workspace database and Flyway implementation. Parent database authority remains 16/16A/16B. API/event contracts are governed by 15/15A/49. Security and authorization are governed by 17/17A/51/32. Observability is governed by 31A/53. Conflicts are AVCI reconciliation items. |

# 3. Authoritative Schema Ownership and Table Domains

The Dynamic Workspace database model must preserve bounded-context ownership. The workspace platform owns workspace composition metadata; policy owners own policy bindings; audit/evidence owners own append-only records; AI governance owns AI capability metadata and model-route references; DBA/Data Governance owns physical integrity and migration controls.
| Schema | Owner | Representative Tables / References |
| --- | --- | --- |
| aira_ui | Workspace Platform Team | workspace_template, screen_template, component_catalog, layout_template, rendering_policy, capability_binding, workspace_activation, user_layout_overlay, feature_toggle, cache_invalidation_event. |
| aira_policy | Security Architecture | policy_binding_ref, opa_policy_ref, field_visibility_rule_ref, role_skill_binding_ref, classification_ceiling_ref, policy_decision_ref. |
| aira_microfunction | Backend Platform / MicroFunction Owner | transaction_ref, step_catalog_ref, capability_transaction_binding, idempotency_profile_ref, audit_profile_ref, outbox_profile_ref. |
| aira_ai | AI Governance | ai_panel_capability_ref, model_route_policy_ref, guardrail_policy_ref, prompt_template_ref, artifact_policy_ref, human_approval_rule_ref. |
| aira_audit / evidence | Audit/Evidence Team | workspace_audit_event, component_action_event, template_lifecycle_event, evidence_record, trace_correlation_ref. |
| aira_cache_meta | Platform Engineering / SRE | cache_key_registry, cache_policy, cache_version_hash, cache_invalidation_log, resolved_view_digest. |

# 4. Core Dynamic Workspace Data Model
| Table / Entity | Required Fields and Governance Meaning |
| --- | --- |
| workspace_template | workspace_code, version, tenant_scope, classification_ceiling, default_screen_code, status, owner, effective_from/to, rollback_ref, config_hash. |
| screen_template | screen_code, workspace_code, route_path, layout_code, rendering_policy_code, mandatory_components, optional_components, status. |
| component_catalog | component_key, component_type, schema_code, props_schema_ref, classification_ceiling, runtime_allowed, admin_builder_allowed, evidence_profile_ref. |
| layout_template | layout_code, grid_version, responsive_rules, accessibility_profile, layout_jsonb, layout_hash, approved_by, activation_state. |
| capability_binding | capability_code, component_key, action_code, api_contract_ref, microfunction_transaction_code, workflow_binding_ref, idempotency_required, approval_required. |
| ai_capability_binding | capability_code, input_modes, output_modes, prompt_template_ref, model_route_policy_ref, guardrail_policy_ref, artifact_registry_policy, human_approval_required_for. |
| user_layout_overlay | user_id_hash, workspace_code, overlay_jsonb, personalization_allowed, policy_hash, layout_hash, effective_state, last_modified_trace_id. |
| evidence_profile | profile_code, required_audit_events, trace_fields, retention_rule, redaction_rule, prompt_capture_allowed, dashboard_ref. |

## Mandatory Physical Design Rules

Every authority table requires owner, status, version, classification, created_by, created_at, updated_by, updated_at, source_ref, approval_ref, config_hash or row_version where applicable, and evidence_ref for activation or protected mutation.

JSONB is allowed for schema-driven configuration only when backed by JSON Schema validation, version, hash, owner, test evidence, and bounded-context approval. Free-form executable SQL or JavaScript in JSONB is prohibited.

Indexes must support workspace_code, screen_code, component_key, capability_code, tenant/context filters, status/effective-date filters, and policy/cache hash lookups. Index changes require performance evidence.

Foreign keys must preserve referential integrity between workspace, screen, layout, component, capability, policy, MicroFunction, evidence profile, and activation records unless an approved decoupled reference pattern is documented.

Activation state and runtime resolution must use approved versions only. Draft records must not be returned to runtime users.

# 5. Flyway Migration Sequencing, Naming, Seed Data, and CI/CD Gates

V048_001 creates aira_ui schema, base enums/reference tables, classification references, and common metadata conventions.

V048_002 creates workspace_template, screen_template, layout_template, rendering_policy, and activation-state tables.

V048_003 creates component_catalog, component_schema_ref, component_evidence_profile, and component classification tables.

V048_004 creates capability_binding, MicroFunction transaction references, workflow binding references, and idempotency requirements.

V048_005 creates AI capability bindings, prompt/artifact policy references, model-route and guardrail references without storing raw secrets or unrestricted prompts.

V048_006 creates user personalization overlay tables, cache metadata, cache invalidation event tables, and resolved-view digest records.

V048_007 creates audit/evidence linkage tables, trace correlation fields, policy decision references, and operational dashboard views where approved.

R__048_seed_dynamic_workspace_baseline inserts deterministic seed/reference data for foundation workspaces, rendering policies, evidence profiles, and component catalog entries.
| Gate | Requirement |
| --- | --- |
| Migration file header | Ticket, owner, bounded context, schema, classification, purpose, compatibility impact, rollback/forward-fix, test plan, evidence path, reviewer roles. |
| Seed/reference data | Deterministic, synthetic or approved reference data only; effective-dated where required; idempotent insert/upsert; no production data. |
| CI gates | Flyway validate, clean-migrate in disposable CI DB, upgrade migrate, schema diff, JSON Schema validation, RLS/policy tests, repository tests, contract tests. |
| Security gates | Secret scan, SAST/SCA where applicable, SQL linting, privilege review, tenant/RLS tests, no unrestricted grants, no raw PII in seed/config. |
| Evidence gates | PR/MR AVCI summary, migration logs, checksums, test reports, GitNexus impact, approvals, rollback/forward-fix evidence, dashboard/trace references. |

# 6. Dynamic Workspace Runtime Resolution, Cache Synchronization, and Runtime Toggles
| Runtime Area | Database / Flyway Requirement |
| --- | --- |
| Runtime resolution | Backend resolver loads approved workspace, screen, component, layout, capability, policy, feature toggle, AI capability, and evidence profile records from PostgreSQL and applies OPA/SBAC/ABAC before returning a filtered view. |
| Redis/Valkey cache | Cache only derivative resolved views, metadata, policy hashes, layout hashes, and component metadata. Cache entries must include version/hash, TTL, classification, and invalidation rule. |
| Cache invalidation | Any approved activation, rollback, template change, component change, policy hash change, capability binding change, or AI route/guardrail change must emit cache invalidation metadata and audit event. |
| Runtime toggles | Telemetry sampling, diagnostic verbosity, AI panel enablement, widget feature flags, cache refresh mode, preview mode, and admin-builder controls are governed records with owner, policy, approval, audit, and safe default. |
| Fail-closed behavior | Missing identity, policy, classification, component schema, capability binding, MicroFunction transaction, guardrail/model-route policy, cache hash, or audit/evidence write blocks protected runtime resolution. |

# 7. MicroFunction, API, Eventing, Outbox/Inbox, DLQ/Replay, and Workflow Integration
| Integration Area | Mandatory Record / Control |
| --- | --- |
| Widget action to capability | Every widget action must map to capability_code, action_code, OpenAPI endpoint, MicroFunction transaction, idempotency requirement, approval requirement, OPA policy input, and evidence profile. |
| OpenAPI / REST | API contract references are stored as metadata only; contract truth lives in Git. Database tables must track contract version/hash and compatibility state for active bindings. |
| AsyncAPI / Kafka / Avro / CloudEvents | Event-producing workspace/admin actions require schema version, topic/channel reference, CloudEvents type/source, correlation/causation/idempotency fields, and outbox profile. |
| Transactional outbox/inbox | Mutating admin/template/capability changes and evented actions must have outbox/inbox or equivalent reliable-event metadata, processed-event tracking, and replay controls. |
| DLQ / replay | DLQ/replay tables or references must capture failed event id, schema version, error reason, retry count, classification, replay eligibility, human approval rule, and replay evidence_ref. |
| Workflow integration | Human approval, template activation, high-risk widget action, AI action proposal, and rollback must reference workflow/process/task IDs and immutable approval evidence. |

# 8. Security, Classification, RLS, Tenant Isolation, and Secrets Hygiene
| Security Control | Database Enforcement |
| --- | --- |
| Classification ceiling | Workspace, screen, component, capability, AI panel, artifact, evidence profile, and field-level metadata must define classification and handling rules before activation. |
| RLS / tenant isolation | Tenant-scoped or organization-scoped records require RLS policy, tenant context, positive/negative tests, Security/DBA approval, and CI drift checks. |
| Least privilege | Runtime service accounts may read active configuration and write audit/evidence/correlation records only within approved scope. Admin Builder writes require elevated SBAC and maker-checker. |
| Secrets hygiene | No secrets, raw tokens, raw JWTs, credentials, production endpoints, private keys, unrestricted customer payloads, or raw Restricted prompts in migrations, seeds, config, logs, tests, evidence, or cache. |
| Admin Builder safety | Admin Builder may configure approved records only. It must not create arbitrary SQL, arbitrary code, direct API bypass, unauthorized policies, or unreviewed production activation. |

# 9. Observability, Audit, Evidence, GitNexus, and Trace Reconstruction

The Dynamic Workspace database must support full trace reconstruction for workspace resolution, admin changes, template activation, component rendering eligibility, user personalization, widget action, AI prompt/artifact workflow, cache invalidation, replay, rollback, and incident analysis. Observability must be classification-safe and performance-aware.
| Evidence Area | Requirement |
| --- | --- |
| Mandatory correlation fields | trace_id, span_id where applicable, request_id, tenant_id or safe tenant ref, user_id_hash, workspace_code, screen_code, component_key, capability_code, policy_ref, policy_decision_ref, microfunction_transaction_code, evidence_ref, classification. |
| Audit events | WORKSPACE_RESOLVED, COMPONENT_FILTERED_BY_POLICY, TEMPLATE_PUBLISHED, TEMPLATE_ROLLED_BACK, LAYOUT_CHANGED, WIDGET_ACTION_INVOKED, AI_PROMPT_SUBMITTED, CACHE_INVALIDATED, REPLAY_REQUESTED. |
| Evidence records | Every activation, migration, policy binding, capability binding, AI capability, admin approval, rollback, and replay must link to owner, source_ref, verification evidence, classification, reversibility, and improvement path. |
| GitNexus evidence | GitNexus may provide read-only impact analysis for schema, contracts, services, widgets, tests, and policies. It remains derivative and must include commit SHA/index timestamp. |
| Forbidden telemetry fields | Passwords, tokens, raw JWTs, secrets, raw PII, raw customer documents, embeddings, private keys, unrestricted prompts, and high-cardinality identifiers as metric labels are prohibited. |

# 10. Testing, Heavy Transaction, Resilience Lab, Restore Validation, and Auto-Improve Loop
| Test / Improvement Area | Minimum Evidence |
| --- | --- |
| Schema and migration tests | Flyway validate, clean-migrate in disposable CI, upgrade from previous baseline, repeatable migration determinism, schema diff, JSON Schema validation. |
| Security and access tests | OPA/SBAC binding tests, RLS positive/negative tests, tenant isolation, field visibility, secrets scan, authenticated DAST fixtures, admin-maker-checker tests. |
| Runtime tests | Workspace resolution, component filtering, feature toggles, cache hit/miss/invalidation, user personalization, action-to-MicroFunction mapping, AI panel metadata, safe fallback. |
| Heavy transaction and concurrency | Concurrent admin edit, activation race, duplicate widget action, retry callback, stale cache, optimistic locking, idempotency, outbox duplication, DLQ replay, and long-running migration tests. |
| Restore and rebuild | Backup/restore, rebuild from Flyway chain, cache rebuild from PostgreSQL, restored activation state, replay safety, and evidence reconstruction tests. |
| Auto-Heal/Learn/Improve | Detected incidents or telemetry may generate candidate schema/config/index/test/policy improvements only. Human review, CI, DBA/Security approval, and PR/MR promotion remain mandatory. |

# 11. RACI, Acceptance Criteria, and AVCI Summary
| Role | Responsibility |
| --- | --- |
| Solutions Architecture Office | Accountable for architecture fit, source conflict resolution, bounded-context ownership, and ARB escalation. |
| Workspace Platform Team | Responsible for workspace/schema requirements, runtime resolution behavior, activation lifecycle, and configuration semantics. |
| DBA / Data Governance | Accountable for schema design, Flyway review, RLS, constraints, indexes, migration safety, backup/restore, and drift closure. |
| Security Architecture | Accountable for OPA/SBAC/ABAC, classification, secrets hygiene, tenant isolation, RLS tests, and high-risk approval controls. |
| DevSecOps | Responsible for CI/CD gates, migration runners, evidence packs, SBOM/provenance, GitNexus integration, and promotion controls. |
| QA/SDET | Responsible for contract, migration, runtime, security, accessibility, E2E, resilience, replay, and regression evidence. |
| SRE / Operations | Responsible for telemetry, dashboards, cache operation, runtime toggles, incident/recovery linkage, and operational readiness. |
| Internal Audit | Assures control testing, evidence completeness, chain-of-custody, and waiver closure. |

## Acceptance Criteria

The aira_ui and companion schemas are created and evolved through Flyway from an empty database, with validation evidence and no manual setup SQL as authority.

Workspace, screen, component, layout, rendering policy, capability binding, AI capability, evidence profile, activation, cache metadata, and personalization tables exist with owner, version, classification, status, and evidence fields where applicable.

Baseline seed/reference data is deterministic, classified, owner-approved, idempotent, and safe for CI/local execution using synthetic or approved reference values only.

Dynamic Workspace runtime resolution can be rebuilt from PostgreSQL truth, filtered by OPA/SBAC/ABAC, accelerated through Redis/Valkey, and invalidated safely on approved changes.

All mutating widget/admin actions use idempotency and map to approved API, MicroFunction, workflow, audit, and evidence records.

CI/CD produces Flyway logs, checksums, contract/test/security evidence, GitNexus read-only impact, and PR/MR AVCI summary before merge or promotion.

Rollback, safe deactivation, forward-fix, cache rebuild, replay/reprocess, and restore validation are documented and tested according to risk tier.

Auto-Heal, Auto-Learn, and Auto-Improve outputs remain candidate proposals until human-reviewed, tested, approved, and promoted through governed PR/MR and Flyway paths.

## AVCI Compliance Summary
| AVCI Property | Evidence |
| --- | --- |
| Attributable | Database artifacts identify owner, source requirement, bounded context, migration, component/capability binding, policy, approver, commit, and evidence reference. |
| Verifiable | Flyway history, CI/CD migration tests, schema validation, OPA/RLS tests, runtime tests, GitNexus impact, audit events, telemetry, restore validation, and replay evidence prove behavior. |
| Classifiable | Workspace records, components, AI capabilities, evidence, telemetry, seeds, prompts/artifacts, and cache metadata carry classification and handling rules. |
| Improvable | Incidents, denied actions, slow queries, failed migrations, replay failures, user feedback, audit findings, and telemetry become governed improvement candidates. |

## Revision and Reconciliation Notes

This v1.1 specification preserves AIRA-DOC-048 as the Dynamic Workspace database/Flyway implementation specification and does not replace parent database standards 16/16A/16B.

If Dynamic Workspace source documents conflict with API, Security, Database, Observability, or Change/CAB standards, the stricter fail-closed, evidence-producing, backend-authoritative interpretation governs until resolved through the canonical register.

Known source-baseline reconciliation items, including duplicate numbering and System Builder overlap, remain AVCI reconciliation items and must not be silently normalized inside implementation work.

