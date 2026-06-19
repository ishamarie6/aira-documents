---
title: "Technology Stack"
doc_id: "AIRA-04"
version: "v9.2"
status: "revised"
category: "Technology stack"
source_docx: "AIRA_04_Technology_Stack_v9.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 04-technology-stack
  - revised
  - aira-04
---



# Technology Stack



AIRA
AI-Native Enterprise Platform

Production-Ready Technology Stack Standard

Version v9.2 - Dynamic Workspace, MicroFunction, System Builder, AI Governance, DevSecOps, Evidence, and Runtime Assurance Alignment

Technology Selection | Lifecycle Governance | Approved Runtime Families | Version Pinning | AI-Native Control Plane | Secure and Observable Delivery | AVCI Always
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-004 |
| Canonical Filename | AIRA_04_Technology_Stack_v9.2_Revised.docx |
| Version | v9.2 - Technology Stack Governance Alignment Update |
| Supersedes | 04-AIRA_Technology_Stack_v9.1_Aligned.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Architecture Review Board, CAB, Security Governance, DevSecOps, Platform Engineering, and Internal Audit Review |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; DevSecOps Lead; Security Architecture; Software Development Lead; Platform Engineering; SRE; DBA; QA/SDET; AI Governance; Data Governance; Internal Audit |
| Primary Parent / Precedence | 01A v1.2 Enterprise Architecture Principles; 01 v3.2 AVCI; 01B v1.2 Evidence; 02 v5.2 Engineering Blueprint; 03 v4.2 Developer Guide |
| Review Cadence | Quarterly; unscheduled on material runtime, framework, AI, model gateway, security, infrastructure, database, observability, DevSecOps, or supply-chain change |
| Evidence Path | OpenKM Tier-0 / AIRA / Standards / Technology-Stack / v9.2 / and Git evidence pack references |

# Mandatory Practice Statement

No technology, framework, runtime, library, model gateway, database, tool, container image, SaaS connector, plugin, agent tool, or infrastructure component may be used for AIRA unless it is approved, version-pinned, source-controlled, license-reviewed, security-scanned, observable, supportable, rollbackable, and AVCI-evidenced. Popularity, convenience, or AI recommendation is not authority. The Technology Stack is an enterprise control surface, not a shopping list.

This v9.2 revision aligns the stack with the newly revised 01A, 01, 01B, 02, and 03 governance foundation, and with the Dynamic Workspace, MicroFunction, System Builder, AI Agent Governance, DevSecOps pipeline, GitNexus, observability, security, and runtime resilience requirements generated in the current alignment cycle.

# Static Table of Contents

1. Executive Summary and v9.2 Alignment Verdict

2. Purpose, Scope, and Authority

3. Technology Selection Control Model

4. Approved Technology Stack Baseline

5. Dynamic Workspace and Frontend Technology Controls

6. Backend, MicroFunction, Workflow, and API Technology Controls

7. Data, Event, Cache, and Evidence Technology Controls

8. AI, Model Gateway, Agent, and Tooling Controls

9. Security, Observability, DevSecOps, and Supply-Chain Controls

10. Runtime Toggle, Performance, Resilience, and Heavy Transaction Controls

11. Technology Lifecycle, Exceptions, and Reconciliation

12. RACI, Roadmap, Acceptance Criteria, and AVCI Summary

# 1. Executive Summary and v9.2 Alignment Verdict

AIRA is a governed AI-native enterprise platform. Its technology stack must therefore define approved technology families, enforcement rules, version authority, exception paths, evidence requirements, and runtime assurance expectations. This v9.2 update retains the v9.1 Java 25 baseline and expands the stack into a full lifecycle control standard.
| Strategic Outcome | v9.2 Required Result |
| --- | --- |
| Single governed stack | Approved runtime, UI, data, AI, security, observability, DevSecOps, and knowledge technologies are controlled by Golden Source pins and evidence packs. |
| No technology drift | Unapproved libraries, direct model SDK calls, unmanaged plugins, click-ops tools, local-only scripts, and hidden dependencies are rejected or quarantined. |
| Dynamic Workspace readiness | Frontend and workspace technologies remain backend-governed, policy-filtered, accessible, observable, and MicroFunction-backed. |
| MicroFunction consistency | Backend runtime, workflow, database, messaging, policy, audit, outbox, and replay technologies support configuration-first delivery and DDD boundaries. |
| Secure AI enablement | Model traffic routes through LiteLLM or approved gateways, with guardrails, OPA/SBAC, Harness-mediated tool actions, audit, and human approval. |
| Evidence by construction | Every technology decision produces owner, version, source, scan, SBOM/provenance, test, runtime, rollback, and improvement evidence. |

## v9.2 Verdict

Proceed with v9.2 as the governing technology baseline, subject to ARB/CAB confirmation of exact patch versions, product editions, hosting model, licensing, procurement, and security hardening. Any apparent version conflict with older source packs must be recorded in the revision-control matrix and resolved through the canonical register.

# 2. Purpose, Scope, and Authority

## 2.1 Purpose

Define approved AIRA technology families and their governance constraints.

Prevent technology drift, unsupported dependencies, direct provider coupling, direct production mutation, and unmanaged AI/tool execution.

Bind stack decisions to AVCI, EDP-01 through EDP-20, DevSecOps evidence, observability, security, rollback, and improvement controls.

Give developers, AI coding assistants, platform engineers, and reviewers a controlled baseline for implementation, provisioning, testing, and operations.

## 2.2 Scope
| In Scope | Out of Scope |
| --- | --- |
| Backend, frontend, workflow, database, cache, messaging, AI/model gateway, security, observability, DevSecOps, knowledge, platform, and developer tooling. | Ad hoc tool adoption, unmanaged plugins, personal AI accounts, local-only automation, production click-ops, or unsupported open-source components. |
| Version pinning, image digest pinning, SBOM/provenance, license review, security scans, CI/CD gates, rollback, and lifecycle status. | Vendor marketing claims, trial tools without controls, AI recommendations without validation, or technology choices made outside ARB/CAB governance. |
| Technology exceptions, waivers, migration paths, deprecation, retirement, and reconciliation of superseded files. | Permanent waivers, undocumented dual-runtime behavior, or silent replacement of canonical stack decisions. |

## 2.3 Authority and Precedence
| Level | Authority | Role |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance | Final authority for production stack decisions, exceptions, procurement-sensitive choices, and platform lifecycle changes. |
| L1 | 01A v1.2, 01 v3.2, 01B v1.2, 02 v5.2 | Defines architecture, AVCI, evidence, and build-ready governance that this technology stack must satisfy. |
| L2 | This Technology Stack Standard v9.2 | Defines approved technology families, lifecycle state, constraints, and evidence requirements. |
| L3 | Developer Guide, API, Database, Security, Observability, DevSecOps, MicroFunction, Dynamic Workspace Standards | Define implementation-specific usage rules for approved technologies. |
| L4 | Golden Source pins, IaC, devcontainer, Helm, pipeline, SBOM, evidence packs | Executable proof and enforceable runtime source of exact patch/digest values. |

Figure 1. AIRA technology stack governance control model.

# 3. Technology Selection Control Model

Technology selection follows a controlled lifecycle: candidate intake, fit assessment, security and licensing review, architecture boundary review, pilot approval, Golden Source version pinning, CI/CD validation, runtime evidence, operational readiness, and deprecation or retirement. AI may recommend technologies, but AI is not approval authority.
| Gate | Required Evidence | Fail-Closed Condition |
| --- | --- | --- |
| Candidate Intake | Owner, source, purpose, bounded context, classification, affected systems, alternatives considered. | Unknown owner, unclear purpose, duplicate function, or unsupported business need. |
| Architecture Fit | EDP impact, Clean Architecture and ports/adapters compatibility, DDD ownership, integration pattern. | Technology requires domain coupling to vendor/framework/database/model provider. |
| Security / Privacy | Threat model, data handling, secrets posture, authentication, authorization, CVE/SCA results, license review. | Unacceptable vulnerability, unclear license, direct secret handling, unsafe telemetry, or fail-open behavior. |
| DevSecOps / Supply Chain | Version pin, artifact digest, SBOM/provenance, signed artifact where feasible, reproducible build. | No deterministic source, no SBOM/provenance, no patch owner, or no reproducible setup. |
| Operational Readiness | SLO/SLA impact, observability, dashboards, runbooks, backup/restore, rollback, supportability. | No monitoring, no rollback, unsupported runtime, or unclear operational owner. |
| Promotion / Review | PR/MR evidence, CODEOWNERS review, ARB/CAB where required, post-promotion monitoring. | Missing approval, missing evidence, or uncontrolled production mutation. |

# 4. Approved Technology Stack Baseline

The following table defines approved technology families and mandatory handling. Exact patch versions, image digests, build images, Helm chart versions, package locks, and licenses must be recorded in Golden Source repositories and evidence packs. Java 21 may appear only as a waiver-based fallback; it must not become a quiet dual baseline.
| Domain | Approved / Target Baseline | Mandatory Controls |
| --- | --- | --- |
| Backend Runtime | Java 25 LTS; Spring Boot 4.x; Spring Framework 7.x where compatible; Spring Security; Gradle/Maven toolchains. | Java 25 is default. Java 21 is waiver-only with owner, reason, risk, compensating controls, exit date, CI evidence, and ARB/CAB approval. |
| Frontend / UX | React 19; Next.js 16; TypeScript 5.x; Node.js 24 LTS; component catalog; accessible UI libraries approved by ARB. | Dynamic Workspace remains backend-governed and policy-filtered. No frontend business authority or hardcoded authorization. |
| API / Integration | OpenAPI; AsyncAPI; CloudEvents; Problem Details; schema registry; generated clients/adapters. | Contract-first; compatibility tests; versioning/deprecation; idempotency; no invented fields outside approved schema. |
| Messaging / Events | Kafka 4.x KRaft; Avro or JSON Schema; transactional outbox; DLQ; replay tooling; idempotent consumers. | Events are contracts. Consumers must be duplicate-safe, replay-safe, and classification-aware. |
| Database / Search / Vector | PostgreSQL 18.x target; Flyway; pgvector; JSONB/GIN/trigram where approved. | Flyway-only schema, seed, RLS, extension, outbox, idempotency, and evidence changes. No manual production DDL. |
| Cache / Runtime State | Redis or Valkey for derivative cache, rate limits, sessions where approved. | Cache is not authority. Must support TTL, invalidation, rebuild, cache-loss behavior, and source-of-truth recovery. |
| Workflow / Orchestration | Temporal; Flowable BPMN/CMMN/DMN where appropriate; workflow event contracts. | Workflow state changes require audit, idempotency, compensation, and human approval where risk/classification requires. |
| Identity / Policy | Keycloak/OIDC/PKCE; enterprise identity federation; OPA/Rego; SBAC/RBAC/ABAC. | Fail closed when identity, token validation, policy, audit, or classification controls are unavailable. |
| Secrets / Credentials | Vault or OpenBao; workload identity; short-lived secrets; sealed secrets where approved. | No secrets in source, logs, screenshots, tests, prompts, or local-only files. Rotation and revocation must be evidenced. |
| AI / Model Gateway | LiteLLM or approved private/on-prem gateway; NeMo Guardrails; Hermes/Harness-mediated agent tooling; approved model aliases. | No direct model-provider calls from application code, scripts, notebooks, or agents. Model route, guardrail, audit, and classification checks are mandatory. |
| Observability | Log4j2; OpenTelemetry; Sentry; Loki; Tempo; Prometheus/Grafana; SigNoz where approved; audit/evidence store. | Trace, metric, log, audit, model, agent, policy, and evidence correlation. Security/audit/evidence signals are non-disableable. |
| DevSecOps / Source | GitHub/GitLab; CODEOWNERS; GitNexus read-only code intelligence; CI/CD; SBOM/provenance; SAST/SCA/DAST; container scans. | Git is code/config source of truth. GitNexus is derivative and read-only. No direct merge/deploy/production mutation by AI or GitNexus. |
| Knowledge / Records | OpenKM or approved DMS for Tier-0 records; Obsidian curated projection; LLM Wiki/LightRAG/pgvector governed retrieval. | Source tiers, classification, provenance, freshness, redaction, retrieval eligibility, and retention must be enforced. |
| Runtime Platform | Containers; Kubernetes where approved; Helm; Argo CD/GitOps; Harbor/registry; Proxmox/Linux baseline where applicable. | No manual production kubectl/click-ops except approved break-glass with evidence, time bound, and post-event reconciliation. |

Figure 2. Technology family integration map and authority boundaries.

# 5. Dynamic Workspace and Frontend Technology Controls

Dynamic Workspace technologies must support composable screens, widgets, templates, AI Panel interactions, personalization, responsive behavior, accessibility, and runtime telemetry without moving business authority to the frontend. Frontend artifacts are presentation and interaction adapters; backend MicroFunctions, APIs, policy, workflow, and evidence stores remain authoritative.
| Area | Required Technology Behavior |
| --- | --- |
| Rendering Strategy | Use SSR, CSR, ISR, PPR, streaming, or client rendering only when the selected mode satisfies classification, authorization, latency, cache, and evidence requirements. |
| Component / Widget Catalog | Widgets are cataloged, versioned, tested, accessible, and bound to approved capabilities, contracts, policy decisions, and MicroFunction-backed actions. |
| AI Assistant Panel | AI Panel can explain, summarize, propose, and draft artifacts; it cannot approve, execute protected actions, bypass policy, or become business authority. |
| Accessibility and Responsive UX | WCAG-aligned keyboard, focus, screen reader, contrast, motion, responsive layout, and degraded-state behavior must be validated in CI where applicable. |
| Safe UI States | Loading, empty, denied, disabled, stale, error, partial, success, requires approval, and degraded/offline states must not leak secrets or bypass backend controls. |
| Frontend Telemetry | Workspace load, component render, widget action, policy deny, AI prompt, artifact generation, layout change, and template changes emit safe trace/audit evidence. |

# 6. Backend, MicroFunction, Workflow, and API Technology Controls

Backend technologies must preserve Clean Architecture and ports/adapters. Controllers, Kafka consumers, schedulers, workflow triggers, and AI tools are adapters. Business use cases and MicroFunctions must not depend on Spring Web, database clients, Kafka producers, Redis, OpenKM, LiteLLM, Vault, Flowable, Temporal, or provider SDKs directly.
| Control | Mandatory Rule |
| --- | --- |
| Java 25 / Spring Boot 4 | Default backend baseline. Use Java 25 toolchains in devcontainers, CI runners, build metadata, GitNexus indexes, tests, and runtime evidence. |
| MicroFunction Runtime | Prefer configuration-first assembly. New code is allowed only for reusable business gaps or framework capabilities after catalog/config options are insufficient. |
| Workflow Engines | Temporal and Flowable are adapters for orchestration and approval. Workflow state and human approval evidence must remain auditable and replay-safe. |
| API Contracts | OpenAPI/AsyncAPI must exist before implementation for boundary-crossing behavior. Generated clients/types should be used instead of handwritten contract drift. |
| Outbox and Events | Mutating transactions that publish events use transactional outbox and idempotent consumers. Kafka publishing is not embedded directly in domain logic. |
| Error Handling | Use safe, typed errors and Problem Details where applicable. Do not expose stack traces, secrets, tokens, raw PII, or policy internals. |

# 7. Data, Event, Cache, and Evidence Technology Controls

PostgreSQL and Git-managed configuration define truth. Redis/Valkey, dashboards, embeddings, reports, search indexes, and AI-generated summaries are derivative. Database, event, cache, and evidence technologies must support reconciliation, replay, rollback, and trace reconstruction.
| Technology Area | Control Standard |
| --- | --- |
| PostgreSQL / Flyway | All schema, RLS, extension, seed, reference data, evidence, outbox, idempotency, and registry changes use Flyway or approved migration workflow. |
| Kafka / Schema Registry | All events use registered schemas, versioning, compatibility rules, correlation IDs, classification, DLQ, and replay controls. |
| Redis / Valkey | Caches must be rebuildable, non-authoritative, TTL-controlled, invalidation-aware, and safe under cache loss or stale data conditions. |
| MinIO / OpenKM / Object Evidence | Files and artifacts require malware scan, hash, classification, owner, retention, access rules, and evidence reference. |
| pgvector / Retrieval Indexes | Embeddings and retrieval indexes are derivative. Source authority, provenance, freshness, quarantine, and retrieval eligibility must be enforced. |
| Evidence Stores | Evidence records must link source_ref, artifact_hash, trace_id, policy_decision_id, event_id, microfunction_run_id, rollback_ref, and improvement_ref. |

# 8. AI, Model Gateway, Agent, and Tooling Controls

AI technology is advisory unless a governed workflow, SBAC skill, OPA decision, guardrail result, Harness tool execution record, human approval, and rollback/evidence path allow more. The stack prohibits direct model-provider SDK use from application code, scripts, notebooks, agents, or services.
| AI / Agent Technology | Required Control |
| --- | --- |
| LiteLLM / Approved Gateway | All model routes use approved aliases, classification eligibility, tenant/skill constraints, guardrails, logging, and cost/latency/error telemetry. |
| NeMo Guardrails / Guardrail Layer | Input, retrieval, execution, and output checkpoints are mandatory for AI-assisted decisions and generated artifacts. |
| Hermes / Harness / Tool Gateway | Agents request tool actions; Harness executes under SBAC/OPA and audit. Agents do not receive direct Git, CI/CD, database, Kubernetes, production, or secret credentials. |
| AI Agent Registry | Every agent has owner, purpose, non-goals, trust tier, classification ceiling, tools, model routes, tests, monitoring, suspension, and retirement evidence. |
| GitNexus | Read-only, derivative, commit-bound code intelligence. It cannot commit, approve, merge, deploy, mutate production, replace tests, or become architecture authority. |
| Dograh / Voice Orchestration | Voice flows require consent, classification, transcript handling, guardrails, policy checks, and evidence. Dograh is orchestration only, not a hardcoded provider. |

# 9. Security, Observability, DevSecOps, and Supply-Chain Controls

Security, observability, and DevSecOps technologies are mandatory parts of the stack, not optional operational add-ons. Each production-bound change must generate test evidence, scan evidence, policy evidence, architecture fitness evidence, SBOM/provenance, runtime observability, and rollback proof.
| Control Family | Required Stack Capability |
| --- | --- |
| Security | Keycloak/OIDC, OPA/SBAC, Vault/OpenBao, secret scanning, authenticated DAST, abuse-case tests, SAST/SCA, container scans, Wazuh/SIEM where applicable. |
| Observability | Log4j2 structured logs, OpenTelemetry traces/metrics/log correlation, Sentry error monitoring, Loki logs, Tempo traces, Grafana dashboards, audit records. |
| Runtime Toggle Rules | Diagnostic logging and some telemetry may be tunable for performance. Security, audit, classification, policy, model-route, guardrail, and evidence signals are non-disableable. |
| DevSecOps | CI/CD, CODEOWNERS, branch protection, policy-as-code, contract tests, mutation tests where appropriate, Playwright/visual tests, accessibility tests, SBOM/provenance. |
| Supply Chain | Version pins, image digests, artifact hashes, license review, dependency update policy, vulnerability triage, provenance, and reproducible build evidence. |
| GitOps / Deployment | Argo CD/GitOps and approved pipelines for deployment. Manual production mutation is break-glass only, time-bound, logged, and reconciled. |

Figure 3. Technology evidence chain from selection to runtime assurance and improvement.

# 10. Runtime Toggle, Performance, Resilience, and Heavy Transaction Controls

AIRA permits runtime tuning for performance only where governance evidence remains intact. Logging, sampling, tracing, dashboard detail, feature activation, and diagnostic verbosity may be adjusted through approved runtime configuration and policy. Controls that prove security, audit, policy, classification, model route, guardrail, evidence, and regulated action integrity must not be disabled.
| Scenario | Required Technology Response |
| --- | --- |
| High concurrency | Use idempotency keys, optimistic locking where appropriate, queue backpressure, rate limits, bulkheads, database constraints, and duplicate-safe event consumers. |
| Heavy transaction | Use async job orchestration, workflow state, outbox, progress events, timeout policy, compensation, dashboard visibility, and safe retry/replay. |
| Kafka replay | Consumers must be replay-safe, ordered where required, schema-compatible, classification-aware, and protected against duplicate business effects. |
| Cache failure | Fallback to authoritative PostgreSQL/Git/config source where permitted; otherwise fail safe with visible degradation and evidence. |
| AI/model degradation | Route through approved fallback policy or stop protected AI action. Do not bypass guardrails or direct-call providers. |
| Auto-Heal / Auto-Learn / Auto-Improve | Issue detection, evidence retrieval, candidate proposal, tests, human approval, PR/MR, rollback, and post-action monitoring. No silent mutation. |

# 11. Technology Lifecycle, Exceptions, and Reconciliation

Technology lifecycle states prevent uncontrolled adoption. A technology may move through candidate, trial, approved, restricted, deprecated, retired, or revoked status. Each movement requires owner, rationale, risk, evidence, and approval appropriate to impact.
| State | Meaning | Required Action |
| --- | --- | --- |
| Candidate | Under evaluation only; not used for production behavior. | Assign owner, evaluate fit, security, license, operations, alternatives, and PoC scope. |
| Trial | Controlled non-production use approved. | Pin versions, isolate scope, produce scan/test/evidence, and set review date. |
| Approved | Permitted under defined conditions. | Maintain Golden Source pins, patch process, evidence, runbooks, support model, and monitoring. |
| Restricted | Permitted only for named scope or classification. | Require SBAC, OPA, compensating controls, enhanced evidence, and periodic recertification. |
| Deprecated | Do not expand usage; migration required. | Create exit plan, replacement target, timeline, risk acceptance, and compatibility evidence. |
| Retired / Revoked | No new use; remove or disable. | Remove from templates, block in CI, archive evidence, and update revision-control matrix. |

## Known Reconciliation Items

Confirm canonical treatment of legacy Technology Stack v9.0 and v9.1 references after v9.2 approval.

Update companion documents that still reference Java 21 as a normal option; Java 21 is waiver-only fallback.

Confirm final approved patch versions for Java 25 distribution, Spring Boot 4.x, Spring Framework 7.x, Node.js 24 LTS, Next.js 16, React 19, PostgreSQL 18.x, Kafka 4.x, and observability tool versions in Golden Source.

Update revision-control matrix after all Pack 01 and Dynamic Workspace companion rework is complete.

Track direct model-provider call prohibition across all developer prompts, agents, notebooks, scripts, and provisioning runbooks.

# 12. RACI, Roadmap, Acceptance Criteria, and AVCI Summary

## 12.1 RACI
| Activity | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Technology proposal and fit analysis | Enterprise Architecture / Platform Engineering | Solutions Architecture Office / IT Head | Security, DevSecOps, SRE, DBA, QA, AI Governance | Developers, Product Owners |
| Version pin and Golden Source update | DevSecOps / Platform Engineering | DevSecOps Lead | Security, QA, SRE | Development Team |
| Security and supply-chain validation | Security Architecture / DevSecOps | Security Governance | Internal Audit, Platform, AI Governance | ARB/CAB |
| Runtime observability readiness | SRE / Platform Engineering | SRE Lead | DevSecOps, Security, Development | Operations and Support |
| Exception or waiver approval | Request Owner | ARB/CAB / Security Governance | Enterprise Architecture, Internal Audit | Affected Teams |
| Deprecation and retirement | Technology Owner | Solutions Architecture Office | DevSecOps, Security, SRE, Product Owner | All Consumers |

## 12.2 Implementation Roadmap
| Phase | Target Outcome | Exit Evidence |
| --- | --- | --- |
| Phase 1 - Foundation Baseline | Approve v9.2 and update Golden Source technology register. | ARB/CAB record, version register, exception register, source commit. |
| Phase 2 - Pipeline Enforcement | CI validates Java/toolchain pins, contracts, scans, SBOM/provenance, policy, and architecture fitness. | Pipeline evidence pack and failing-control examples. |
| Phase 3 - Dynamic Workspace Binding | Frontend, widget, AI Panel, Admin Builder, and templates consume approved stack and evidence model. | Workspace test evidence, accessibility evidence, policy deny tests, trace reconstruction. |
| Phase 4 - Runtime Assurance | Dashboards, logs, traces, metrics, audit, runtime toggles, and incident evidence validate operations. | Grafana/Sentry/Loki/Tempo evidence, SLO review, incident/runbook proof. |
| Phase 5 - Continuous Improvement | Auto-Heal/Learn/Improve candidate workflows use stack evidence without silent mutation. | Improvement proposals, tests, PR/MR evidence, rollback proof, post-change monitoring. |

## 12.3 Acceptance Criteria

Approved technology families and forbidden usage are clear, version-pinned, and enforceable through CI/CD and review gates.

Java 25 is the default backend baseline, and Java 21 appears only through approved waiver evidence.

Dynamic Workspace, MicroFunction, System Builder, AI agents, DevSecOps, security, observability, and evidence controls are explicitly represented.

OpenAPI, AsyncAPI, Kafka, Avro/JSON Schema, CloudEvents, outbox, DLQ, replay, schema evolution, and Flyway controls are included.

Runtime telemetry toggles are permitted only for performance-safe diagnostics; security/audit/evidence/policy/classification signals cannot be disabled.

Technology exceptions, deprecations, and reconciliation items feed the revision-control matrix and governance backlog.

## 12.4 AVCI Compliance Summary
| AVCI Element | Evidence in this Standard |
| --- | --- |
| Attributable | Defines document owner, co-owners, technology owners, approval authorities, version authority, and RACI responsibilities. |
| Verifiable | Requires Golden Source pins, CI/CD evidence, tests, scans, SBOM/provenance, observability, GitNexus impact, runtime evidence, and rollback proof. |
| Classifiable | Requires technology, telemetry, prompts, records, source data, evidence, model routes, and artifacts to honor classification and handling rules. |
| Improvable | Defines lifecycle states, review cadence, exceptions, deprecation, incident feedback, Auto-Heal/Learn/Improve candidate loop, and revision-control reconciliation. |

# External Alignment Register

External references reviewed for alignment include Oracle/OpenJDK Java 25 LTS release material; Spring Boot 4.0 and Spring Framework 7 release material; OpenTelemetry Semantic Conventions; SLSA v1.2; NIST AI RMF / NIST AI 600-1; NIST SSDF; OWASP ASVS and OWASP GenAI / LLM guidance; and W3C WCAG 2.2. These sources inform technology governance, but AIRA approval, Golden Source pins, and ARB/CAB decisions remain controlling for AIRA implementation.

