---
title: "Greenfield Environment Standard"
doc_id: "AIRA-09"
version: "v3.2"
status: "revised"
category: "Greenfield environment"
source_docx: "AIRA_09_Greenfield_Environment_Standard_v3.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 09-greenfield-environment
  - revised
  - aira-09
---



# Greenfield Environment Standard



AIRA

AI-Native Enterprise Platform

AIRA Greenfield Environment Standard

v3.2 Revised

Dynamic Workspace · MicroFunction Runtime · DevSecOps Evidence · Observability · Resilience · Progressive Autonomy
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-009 |
| Canonical Filename | AIRA_09_Greenfield_Environment_Standard_v3.2_Revised.docx |
| Version | v3.2 - Dynamic Workspace, MicroFunction, Evidence, Observability, Resilience, and Progressive Autonomy Alignment Update |
| Supersedes | 09-AIRA_Greenfield_Environment_Standard_v3.1_Aligned.docx |
| Status | Draft for Architecture, DevSecOps, Security, Platform, QA/SDET, AI Governance, DBA, SRE, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; DevSecOps Lead; Software Development Lead; Security Architecture; Platform Engineering; QA/SDET; DBA; SRE / Operations; AI Governance; Internal Audit |
| Primary Audience | Software Developers; Frontend Developers; Backend Developers; DevSecOps; Platform Engineers; Security; QA/SDET; System Builder operators; AI agent owners; Reviewers |
| Effective Date | Upon Architecture Review Board / CAB / Security Governance approval |
| Review Cadence | Quarterly; unscheduled on material environment, technology stack, Dynamic Workspace, MicroFunction, CI/CD, security, AI, observability, or production-readiness change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Greenfield-Environment / v3.2 / |
| Generated | 2026-06-17 11:14 |

Mandatory Practice Statement

A greenfield AIRA environment is not ready merely because tools are installed. It is ready only when developers can build, test, secure, observe, govern, evidence, roll back, and improve AIRA through approved repositories, contracts, MicroFunctions, Dynamic Workspace controls, CI/CD gates, OPA/SBAC policy, AI governance, and AVCI evidence. Runtime flexibility is permitted only through governed configuration, policy-filtered toggles, audit, rollback, and evidence. No environment, workstation, devcontainer, repository, AI assistant, System Builder output, agent, pipeline, schema, API, event, workspace, or MicroFunction may bypass approved source authority, maker-checker review, classification, security gates, observability, rollback, or human accountability.

Discipline First · Automation Second · Intelligence Third · AVCI Always

# Static Table of Contents

1. Executive Summary

2. v3.2 Revision Verdict and Change Summary

3. Purpose, Scope, and Authority

4. Governing Source Baseline and External Alignment

5. Greenfield Environment Control Model

6. Enterprise Design Principles Applied to Greenfield Environments

7. Architecture and Bounded Context Readiness

8. Dynamic Workspace and Frontend UX Readiness

9. MicroFunction Backend and Runtime Assembly Readiness

10. Repository, Golden Source, Knowledge, and Activity Ledger Readiness

11. Workstation, Devcontainer, and Toolchain Baseline

12. DevSecOps Pipeline, Security Gates, Evidence Pack, and GitNexus

13. API, Eventing, Kafka, Avro, CloudEvents, Outbox, and Replay Readiness

14. Database, Flyway, Schema Evolution, Idempotency, and Evidence Readiness

15. Observability, Log4j2, OpenTelemetry, Sentry, Loki, Tempo, and Grafana

16. Runtime Telemetry Toggle and Performance Control Model

17. Concurrency, Heavy Transaction, Idempotency, Outbox, and Resilience Lab

18. Security, OPA/SBAC, Abuse Cases, Authenticated DAST, Secure APIs, and Secrets Hygiene

19. AI DevSecOps, System Builder Lite, Codex, Hermes, and Agent Readiness

20. Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop

21. Environment Promotion, Reversibility, and Recovery Readiness

22. RACI and Separation of Duties

23. Implementation Roadmap

24. Acceptance Criteria and Go/No-Go Gate

25. Cross-Document Reconciliation and Future Regeneration Candidates

26. Risk and Control Register

27. AVCI Compliance Summary

Appendix A. Greenfield Evidence Pack Template

Appendix B. Environment Validation Checklist

Appendix C. Source and External Reference Register

# 1. Executive Summary

This v3.2 revision upgrades AIRA-DOC-009 from a clean-slate environment standard into the controlled operating baseline for AI-native DevSecOps delivery. The document preserves the original greenfield intent: pristine baselines, reproducible workspaces, controlled onboarding, source authority, secure toolchains, and drift-free engineering. It adds the missing integration layer needed by the current AIRA direction: Dynamic Workspace readiness, MicroFunction runtime readiness, CI/CD evidence readiness, OpenAPI/AsyncAPI/Kafka readiness, observability readiness, resilience lab readiness, AI governance readiness, and proposal-driven continuous improvement readiness.

The key interpretation is that environment readiness must be judged by executable proof, not installation completion. Developers must be able to run an approved local workspace, work inside governed repositories, execute deterministic tests, validate OpenAPI and AsyncAPI contracts, run Flyway migrations, prove outbox and idempotency paths, emit safe telemetry, produce evidence packs, use GitNexus as read-only derivative code intelligence, and route all AI-assisted work through approved guardrails, source baselines, SBAC, OPA, and human review.

This standard also clarifies runtime flexibility. Logging, tracing, diagnostic verbosity, feature flags, workspace telemetry, AI assistant panels, and expensive debug instrumentation may be toggled at runtime only when the toggle is policy-governed, source-controlled, auditable, reversible, classification-aware, and safe by default. A performance concern may justify sampling or lower diagnostic verbosity. It does not justify removing audit, security events, policy decisions, error evidence, or minimum trace correlation from protected flows.
| Strategic Outcome | v3.2 Mandatory Result |
| --- | --- |
| Greenfield readiness | Ready only when toolchain, repositories, CI/CD, evidence, security, observability, rollback, and governance are proven. |
| Dynamic Workspace readiness | Frontend renders approved components; backend authorizes; MicroFunctions execute; PostgreSQL defines truth; Redis/Valkey accelerates only. |
| MicroFunction readiness | Configuration-first assembly with mandatory identity, classification, policy, validation, idempotency, audit, observability, error handling, and rollback paths. |
| AI-native readiness | AI may guide, analyze, draft, generate, test, and propose; it may not approve, merge, deploy, access production credentials, or mutate production directly. |
| Evidence readiness | Every meaningful setup, code, configuration, schema, policy, agent, workspace, and promotion action produces AVCI evidence. |

# 2. v3.2 Revision Verdict and Change Summary

Revision verdict: v3.1 remains structurally valid as the greenfield environment baseline. The v3.2 action is not replacement by a different concept; it is controlled expansion so the environment baseline matches the current AIRA documents generated after the original 09 baseline. The revised standard must now be strong enough to guide the team before implementation begins, before System Builder Lite is used broadly, and before Dynamic Workspace, MicroFunction, API/eventing, AI agents, or Auto-Heal candidates are introduced.
| Revision Area | v3.2 Update |
| --- | --- |
| Dynamic Workspace alignment | Adds explicit frontend/backend/MicroFunction boundary readiness and workspace policy-filtering prerequisites. |
| MicroFunction alignment | Adds backend runtime assembly readiness, standard step enforcement, idempotency, outbox, audit, evidence, and cache correctness gates. |
| DevSecOps evidence | Elevates CI/CD, security gates, Evidence Pack, GitNexus, SBOM/provenance, and architecture fitness to greenfield exit gates. |
| API and eventing | Adds OpenAPI, AsyncAPI, Kafka, Avro, CloudEvents, schema evolution, idempotent consumers, DLQ, retry, and replay readiness. |
| Observability | Adds Log4j2 structured logging, OpenTelemetry traces/metrics/logs, Sentry, Loki, Tempo, Grafana, audit, dashboards, alerting, and trace reconstruction. |
| Concurrency and heavy transactions | Adds resilience lab readiness for retry-safe, duplicate-safe, concurrent, heavy-load, failure-aware behavior. |
| Runtime toggles | Adds governed on/off or sampling model for logs, traces, diagnostics, AI panel, workspace telemetry, and feature activation. |
| AI continuous improvement | Adds Auto-Heal, Auto-Learn, and Auto-Improve candidate loop boundaries: detect, retrieve evidence, propose, test, and request approval. |
| Security hardening | Adds OPA/SBAC expansion, abuse cases, authenticated DAST, secure APIs, secrets hygiene, remediation evidence, and fail-closed rules. |

# 3. Purpose, Scope, and Authority

## 3.1 Purpose

Define the minimum governed environment baseline before AIRA software development, Dynamic Workspace implementation, MicroFunction runtime work, API/eventing, AI agent work, or System Builder Lite execution proceeds.

Convert enterprise design principles into environment setup controls, validation gates, evidence requirements, and failure conditions.

Ensure workstations, devcontainers, repositories, source packs, Obsidian projections, CI/CD pipelines, test environments, and AI tools are reproducible, secure, observable, and AVCI-compliant.

Create an environment readiness model that supports PoC 1, PoC 1A, PoC 2, Dynamic Workspace PoCs, API/eventing PoCs, observability PoCs, resilience PoCs, and Auto-Heal/Auto-Learn/Auto-Improve candidate loops.

## 3.2 Scope
| Scope Area | Treatment |
| --- | --- |
| In Scope | Windows developer workstation baseline; devcontainers; repository bootstrap; branch protection; CODEOWNERS; PR/MR templates; CI/CD; GitNexus; local and CI tests; Flyway; OpenAPI/AsyncAPI; Kafka/Avro/CloudEvents; OPA/SBAC; Keycloak; Vault-compatible secret references; Log4j2/OTel/Sentry/Loki/Tempo/Grafana; Obsidian/LLM Wiki; System Builder Lite; Codex; Hermes; LiteLLM; guardrails; AI agent sandbox readiness; evidence packs. |
| Out of Scope | Direct production mutation; unmanaged personal AI accounts for AIRA work; unapproved plugins; direct model-provider calls from application code; manual production DDL; local production data; bypassing CI/CD/security gates; AI approval of its own output; GitNexus as authority; Redis/Valkey as truth; frontend business authority. |

## 3.3 Authority and Precedence
| Level | Authority | Role |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance / IT Head | Final authority for production-impacting environment baselines, exceptions, waivers, and promotion readiness. |
| L1 | AIRA AVCI, Enterprise Architecture, Security, DevSecOps, Database/Flyway, MicroFunction, API, Observability, Change, AI Governance Standards | Universal source of non-negotiable controls. |
| L2 | This 09 v3.2 Standard | Canonical environment readiness baseline and gate for greenfield setup. |
| L3 | 39/39A/39B/39C setup guides and System Builder Lite playbooks | Executable setup procedures subordinate to this standard. |
| L4 | Tickets, ADRs/TDLs, PR/MR evidence, CI/CD runs, environment manifests, runbooks, logs, traces, audit, dashboards | Operational proof and controlled implementation records. |

# 4. Governing Source Baseline and External Alignment

This document is aligned to the active AIRA baseline and the current expanded source packs, especially the Greenfield Environment Standard v3.1, Skills Framework, Team Transformation Maturity Direction, MicroFunction standards, DevSecOps evidence standards, GitNexus, API and contract-first standards, database/Flyway standards, security standards, Dynamic Workspace standards, System Builder standards, AI agent governance standards, and observability standards.
| Reference Area | Required Treatment |
| --- | --- |
| Primary AIRA source baseline | 01/01A/01B, 02, 03, 04, 05, 07, 07B, 08/08A, 09, 10/10A/10B/10C/10D/10E, 11/11A, 12A, 15/15A, 16/16A/16B, 17/17A, 19/20, 21A/21B, 22A/22B, 23A/23B/23C, 24/24B, 30/30A, 31/31A, 32, 39/39A/39B/39C, 41/41B, 42/42D-42S, 43/43C/43D, 44/44A/44C, 45-61. |
| Dynamic Workspace baseline | 41 Dynamic User Workspace; 42 Composable Experience Framework; 44 Next.js Rendering Strategy; 46-61 Dynamic Workspace configuration, API, DB, security, testing, observability, admin builder, UX, DevSecOps, AI-assisted workspace standards. |
| MicroFunction baseline | 10 MicroFunction Framework; 10A Design and Development; 10B Implementation; 10C Sequence Diagrams; 10D Standard Function Catalog; 10E Backend Generation; Login PoC MicroFunction patterns and runtime configuration standards. |
| DevSecOps baseline | 11/11A, 19 GitNexus, 20 CI/CD Evidence Pack, 23B Fitness Function Catalog, 30/30A Change and Rollback, 45 PoC 2 DevSecOps Pipeline and System Factory. |
| External alignment | NIST SSDF SP 800-218 v1.1 final; NIST SP 800-218A AI profile; NIST SP 800-218r1 v1.2 draft as watchlist only; OWASP ASVS 5.0.0; OpenTelemetry Semantic Conventions 1.42.0; SLSA v1.2; OWASP ZAP/DAST practices; CNCF/GitOps/supply-chain practices as approved by AIRA Technology Stack. |

External standards do not override AIRA governance. They inform control design, test depth, secure development expectations, telemetry naming, and supply-chain evidence. Any external-source conflict or version shift must become an AVCI reconciliation item and must be reviewed before adoption.

# 5. Greenfield Environment Control Model

The greenfield environment is a controlled engineering runway. It starts from identity, device, repository, source, toolchain, and evidence discipline; then enables coding, Dynamic Workspace rendering, MicroFunction runtime assembly, API/eventing, database migration, policy, security, observability, AI assistance, and controlled improvement.
| Control Plane | Authority Rule |
| --- | --- |
| Source Authority | Approved DOCX/PDF, Git repositories, OpenKM, official registers, ADR/TDL, evidence stores, databases, workflow histories. |
| Working Knowledge | Git-managed Obsidian projections and LLM Wiki retrieval are curated derivatives; they do not replace Tier-0 source records. |
| Execution Authority | Humans execute privileged setup and approvals. CI/CD executes validations. Harness/MCP gateway mediates governed tool actions. AI remains advisory or draft-producing unless explicitly approved. |
| Runtime Authority | Backend services, OPA/SBAC, Keycloak/OIDC, MicroFunction runtime, PostgreSQL, and policy-as-code define behavior. Frontend does not authorize business action. |
| Evidence Authority | PR/MR evidence, CI/CD reports, scan results, SBOM/provenance, GitNexus reports, audit, traces, logs, dashboards, ticket records, and approval records prove readiness. |

# 6. Enterprise Design Principles Applied to Greenfield Environments
| ID | Principle | Mandatory Meaning |
| --- | --- | --- |
| EDP-01 | SOLID | Components, agents, prompts, services, and MicroFunctions preserve single responsibility, extensibility, substitutability, interface focus, and dependency inversion. |
| EDP-02 | Clean Architecture | Domain and use-case logic do not depend on frameworks, UI, database, model providers, workflow engines, or provisioning tools. |
| EDP-03 | DDD / Bounded Contexts | Business domains own clear language, invariants, schema boundaries, APIs, events, and runbooks. |
| EDP-04 | Ports and Adapters | External systems, databases, models, queues, tools, agents, and provisioning providers are accessed through explicit ports and adapters. |
| EDP-05 | DRY, KISS, YAGNI | Avoid duplicated logic, accidental complexity, speculative abstractions, and over-engineering. |
| EDP-06 | Idempotency by Design | Retries, replays, callbacks, agent actions, and provisioning tasks do not duplicate business or infrastructure effects. |
| EDP-07 | Determinism and Reproducibility | Builds, tests, migrations, prompts, agents, model routes, environments, and evidence are reproducible from approved sources. |
| EDP-08 | Fail-Safe, Not Fail-Open | If identity, policy, guardrail, audit, model gateway, evidence, or provisioning controls fail, protected actions stop. |
| EDP-09 | Human-in-the-Loop | High-impact, low-confidence, Restricted, production-impacting, destructive, or policy-exception actions require named human approval. |
| EDP-10 | Least Privilege / SBAC | Humans, services, System Builder, and AI agents receive only approved skills, permissions, tools, data, and environment scope. |
| EDP-11 | Separation of Duties | Maker, checker, approver, deployer, operator, agent owner, and auditor roles remain separated for high-risk workflows. |
| EDP-12 | Observability by Design | Critical paths emit trace, metric, log, audit, model, agent, provisioning, and evidence references with safe redaction. |
| EDP-13 | Policy as Code | Authorization, admission, routing, guardrail, deployment, environment, data-handling, and agent-tool rules are versioned policy artifacts. |
| EDP-14 | Testability by Design | Code, workflows, prompts, agents, adapters, policies, and provisioning manifests are independently testable with deterministic fixtures. |
| EDP-15 | Secure by Design | Threat controls, secrets hygiene, classification handling, tenant isolation, supply-chain controls, and secure defaults are built in. |
| EDP-16 | Resilience Patterns | Timeouts, retries, circuit breakers, bulkheads, fallback, DLQ, compensation, recovery, and rebuild are explicit. |
| EDP-17 | Architectural Fitness Functions | Automated checks continuously verify boundaries, dependencies, contracts, security, agents, provisioning, and evidence rules. |
| EDP-18 | Progressive Autonomy | Automation advances only when evidence, trust score, skill, risk tier, guardrails, and rollback controls support it. |
| EDP-19 | Reversibility / Rollbackability | Changes support rollback, forward-fix, compensation, feature disablement, environment rebuild, or safe deactivation. |
| EDP-20 | AVCI | Every artifact remains attributable, verifiable, classifiable, and improvable across its lifecycle. |

Environment validation must produce evidence for all 20 principles. Failure against any principle must be recorded as a defect, waiver, or AVCI reconciliation item with a named owner and remediation path.

# 7. Architecture and Bounded Context Readiness
| Readiness Area | Required Greenfield Control |
| --- | --- |
| Package boundaries | Repository and devcontainer must support modules/libraries that separate domain, application/use case, adapters, API contracts, infrastructure, policy, and tests. |
| No direct infrastructure dependency | ArchUnit/Semgrep rules must reject business functions importing database clients, Kafka producers, Redis clients, OpenKM clients, model SDKs, or controller/UI dependencies. |
| DDD ownership | Each bounded context must declare owner, schema namespace, API/event contracts, runbook, evidence path, and release readiness checklist. |
| Configuration-first | Runtime behavior, workspace templates, MicroFunction steps, policies, model routes, telemetry profiles, and feature flags must be declared in approved configuration, not hidden inside uncontrolled code. |
| ADR/TDL triggers | New technology, environment deviation, runtime baseline change, schema ownership change, policy relaxation, production-impacting automation, or cross-boundary coupling requires ADR/TDL or waiver. |

# 8. Dynamic Workspace and Frontend UX Readiness

The Dynamic Workspace environment must be prepared before frontend development scales. The frontend must never become business authority. It renders approved layouts, captures user intent, invokes generated clients, and displays safe states. The backend resolves effective workspace, authorizes actions, applies OPA/SBAC/ABAC/RBAC policy, binds capabilities to APIs and MicroFunctions, emits evidence, and returns safe responses.
| Workspace Area | Environment Readiness Requirement |
| --- | --- |
| Frontend renderer | Next.js/React workspace shell uses approved component registry, generated API clients, safe error handling, accessibility baseline, and OpenTelemetry frontend correlation. |
| Backend resolver | Workspace service resolves workspace_code, screen_code, components, policy-filtered actions, role/skill eligibility, layout, personalization, and classification. |
| Component registry | Approved components define schema, props, data contract, action binding, classification ceiling, telemetry profile, accessibility requirements, and safe rendering policy. |
| Capability binding | Every widget action maps to OpenAPI endpoint, backend use case, MicroFunction transaction, OPA policy, idempotency profile, audit event, and evidence profile. |
| Admin Builder | Template changes require maker-checker approval, versioning, activation/deactivation, rollback, audit, and evidence pack. |
| Cache model | Redis/Valkey may cache derivative resolved views and metadata only. PostgreSQL and approved configuration are truth. Cache miss or invalidation must not change authorization or correctness. |
| AI Assistant Panel | Multimodal panel is toggleable, guardrailed, classification-aware, model-route controlled, observable, and unable to bypass backend policy or MicroFunction governance. |

# 9. MicroFunction Backend and Runtime Assembly Readiness

The environment must support MicroFunction development before developers implement business flows. A MicroFunction transaction is a governed runtime assembly of steps, policies, configuration, contracts, evidence, audit, observability, error handling, retry, compensation, and rollback. It is not a hardcoded controller-service pattern.
| MicroFunction Readiness Area | Mandatory Control |
| --- | --- |
| Standard step envelope | Receive, correlate, resolve actor/tenant, rate-limit, authorize/classify, validate, check idempotency, execute business step, audit, outbox, observe, shape safe response, and record evidence. |
| Ports/adapters | Keycloak, OPA, Kafka, database, Redis, OpenKM, Flowable/Temporal, model gateways, and external APIs are behind ports/adapters. |
| PostgreSQL authority | Runtime definitions, component bindings, step catalog, activation state, audit/evidence schema, and idempotency/outbox records are authoritative in PostgreSQL and governed by Flyway. |
| Runtime cache | Caffeine/Redis/Valkey accelerates resolved definitions only. Cache rebuild, invalidation, and cold-start paths must be tested. |
| Tests | Unit, component, contract, configuration, security, policy, idempotency, retry, outbox, replay, rollback, architecture, and observability tests are required where applicable. |
| Evidence | Each transaction has definition_hash, source commit, owner, approver, policy decision, test run, trace/audit/evidence reference, classification, and rollback/safe-disable path. |

# 10. Repository, Golden Source, Knowledge, and Activity Ledger Readiness
| Readiness Area | Required Treatment |
| --- | --- |
| Git repository | Code, tests, contracts, policies, Flyway migrations, devcontainers, CI/CD, IaC, Helm/Kustomize, AI prompts, guardrails, and runbooks are versioned in Git. |
| Branch protection | Default branch requires PR/MR, CODEOWNERS, signed commits/artifacts where supported, passing checks, no force-push, no unapproved admin bypass. |
| Source projection | Obsidian contains curated knowledge projection and approved summaries. LLM Wiki retrieval is derivative and must enforce ACL, SBAC, classification, freshness, provenance, and conflict checks. |
| Activity ledger | Day 0 setup actions, AI assistance, decisions, evidence, commands, deviations, errors, and follow-up items are logged in a Git-backed activity ledger. |
| Evidence register | Every environment setup, validation, waiver, tool install, source-pack adoption, and AI-assisted output links to an evidence record. |
| No uncontrolled copies | No full source code copied to Obsidian, prompts, personal drives, screenshots, or unmanaged AI contexts. Git/GitNexus remain code and code-intelligence authorities. |

# 11. Workstation, Devcontainer, and Toolchain Baseline

The workstation and devcontainer baseline must be reproducible and secure. Human administrators execute privileged operating-system or account actions. AI may guide and prepare commands, but it must not take privileged action or disable controls.
| Toolchain Area | Minimum Readiness Requirement |
| --- | --- |
| Operating system baseline | Windows 11 secured baseline; full disk encryption; approved endpoint protection; patching; firewall; corporate Wi-Fi/VPN controls; least privilege; no local production data. |
| Core engineering tools | VS Code, Git, GitHub/GitLab CLI as approved, Java 25 LTS, Gradle/Maven, Node.js/pnpm/npm, Docker/Podman where approved, Flyway, OPA, test tools, secret scanners, SAST/SCA tools. |
| Devcontainer baseline | Pinned images, digest/hash verification where possible, no unmanaged plugins, no embedded secrets, SBOM, SCA scan, reproducible build, architecture tests, CI parity. |
| Frontend tools | Next.js/React/TypeScript, generated clients, lint/type/test tooling, Playwright, accessibility checks, frontend telemetry SDK configuration, safe local fixtures. |
| Backend tools | Java 25 LTS, Spring Boot target baseline, JUnit 5, Mockito, Testcontainers, ArchUnit, OpenAPI/AsyncAPI tools, Avro/schema tools, Kafka local stack, Log4j2, OpenTelemetry SDK/agent. |
| Security tools | Gitleaks or equivalent secret scan, Semgrep/SAST, Trivy/SCA/container scan, Syft/SBOM, Cosign/signing where adopted, OWASP ZAP authenticated DAST for non-prod synthetic scope. |

# 12. DevSecOps Pipeline, Security Gates, Evidence Pack, and GitNexus

The greenfield environment must be able to prove the governed engineering factory before development volume increases. A sample service and sample workspace change must pass the same controls expected from later work.
| Pipeline Area | Mandatory Gate |
| --- | --- |
| Build and test | Compile, unit tests, component tests, frontend tests, contract tests, migration tests, OPA tests, architecture tests, and deterministic fixtures. |
| Security gates | Secret scan, SAST, SCA, container scan, SBOM, DAST where applicable, dependency license review, policy-as-code, log redaction tests, secure API checks. |
| Supply chain | Pinned dependencies, lock files, artifact digest, SBOM/provenance, signed artifacts/manifests where adopted, private mirrors/registries where applicable. |
| GitNexus | Read-only, derivative, commit-bound code intelligence for code map, impact analysis, affected tests, architecture drift, PR/MR evidence, and Auto-Heal proposal support. It cannot commit, approve, merge, deploy, or mutate production. |
| Evidence Pack | PR/MR summary includes owner, source, classification, tests, scans, SBOM/provenance, GitNexus report, architecture impact, rollback path, AI-use declaration, and improvement backlog. |
| Blocking rule | Critical/high unapproved findings, failed policy checks, missing evidence, missing rollback, direct infrastructure shortcuts, or secret leakage block merge or promotion. |

# 13. API, Eventing, Kafka, Avro, CloudEvents, Outbox, and Replay Readiness
| Integration Capability | Readiness Requirement |
| --- | --- |
| OpenAPI | Every REST boundary has contract before implementation, generated clients where practical, Problem Details safe error profile, correlation headers, idempotency headers for mutating operations, compatibility checks. |
| AsyncAPI | Every event boundary has AsyncAPI contract, topic ownership, event naming, producer/consumer responsibilities, and compatibility test. |
| Kafka | Local or controlled DEV Kafka readiness with topic registry, ACL policy, retry/DLQ topic naming, consumer groups, idempotency, replay runbook, and trace propagation. |
| Avro and schema evolution | Schema registry decision, compatibility rules, versioning, backward/forward compatibility tests, deprecation path, consumer migration plan, evidence. |
| CloudEvents | Standard envelope carrying id, source, type, subject, time, datacontenttype, trace_id/correlation_id/causation_id, classification, and evidence reference where applicable. |
| Transactional outbox/inbox | State change and event intent are committed atomically; dispatcher publishes reliably; consumers deduplicate; inbox records prevent duplicate effects. |
| DLQ and replay | Dead-letter path, reason codes, retry policy, quarantine, manual review, replay approval, idempotency proof, and trace reconstruction are tested. |

# 14. Database, Flyway, Schema Evolution, Idempotency, and Evidence Readiness
| Database Readiness Area | Mandatory Control |
| --- | --- |
| Flyway from Day 0 | Initial schema creation, extensions, schemas, tables, indexes, RLS policies, seed data, views, evidence tables, and outbox/idempotency tables use Flyway. No manual greenfield DDL. |
| Schema ownership | Each schema/table has owning bounded context, owner, classification, tenant model, audit fields, trace fields, row_version, retention, and evidence expectations where applicable. |
| Idempotency registry | Mutating commands, callbacks, agent actions, replay, workflow steps, and provisioning tasks use stable idempotency keys and dedupe evidence. |
| Outbox/inbox | Outbox for reliable publication and inbox for idempotent consumer processing. Retry and replay prove no duplicate business effects. |
| Schema evolution | Backward-compatible migrations, expand/contract pattern where needed, compatibility tests, rollback/forward-fix plan, DBA review, and migration evidence. |
| Data safety | Synthetic data by default; classified UAT data only by approved handling rule. No production data on local machines. |

# 15. Observability, Log4j2, OpenTelemetry, Sentry, Loki, Tempo, and Grafana

Observability must exist before operational reliance. Critical flows must be reconstructable through trace, metric, log, audit, error, evidence, dashboard, and alert records without leaking secrets, tokens, raw prompts, or sensitive payloads.
| Observability Capability | Minimum Greenfield Baseline |
| --- | --- |
| Structured logs | Log4j2 JSON or structured logging profile with service, environment, trace_id, span_id, request_id, event_name, safe error code, classification, and redaction. No secrets, tokens, raw PII, raw prompts, or stack traces in user-visible responses. |
| OpenTelemetry | Trace, metric, log, resource, service, HTTP, messaging, database, and exception attributes aligned to OpenTelemetry semantic conventions where adopted. |
| Sentry | Error monitoring and release-health for frontend and backend where approved; events scrubbed and correlated to release, trace, issue, and evidence references. |
| Loki | Centralized logs with bounded labels, redaction, retention, query examples, alert rules, and incident evidence links. |
| Tempo | Distributed tracing with frontend, gateway, backend API, policy, MicroFunction, database, Kafka, workflow, AI gateway, and tool-action spans. |
| Grafana | Dashboards for service health, pipeline evidence, policy denials, workspace behavior, MicroFunction latency, Kafka lag/DLQ, SLO/error budget, security events, and evidence completeness. |
| Audit and evidence | Audit events are business/governance records; logs are diagnostics. Evidence records link owner, source, verification, classification, reversibility, and improvement path. |

# 16. Runtime Telemetry Toggle and Performance Control Model

AIRA allows runtime configurability for performance and troubleshooting, but dynamic must never mean uncontrolled. Toggleable logging or telemetry must preserve audit, security, policy, and evidence obligations. AIRA must support default-safe profiles, temporary escalation, sampling, and rollback without requiring source-code modification.
| Toggle Area | Mandatory Rule |
| --- | --- |
| Allowed runtime toggles | Log level, trace sampling, diagnostic detail, frontend telemetry sampling, widget performance instrumentation, AI assistant panel visibility, non-critical debug spans, feature flags, resilience lab fault-injection in non-prod. |
| Never fully disabled for protected flows | Security audit, access audit, OPA/SBAC decision logging, policy-deny evidence, authentication failure evidence, privileged action audit, agent/tool action audit, migration evidence, approval evidence, rollback evidence. |
| Governance path | Toggle change requires owner, reason, environment, classification impact, duration, rollback, approver, audit event, and evidence_ref. Production toggle changes require CAB or approved emergency process. |
| Default values | Secure and observable by default. High-volume debug disabled by default. PII/secrets redaction always enabled. Critical audit always enabled. Sampling may reduce trace/log volume but must preserve correlation. |
| Performance guardrail | If telemetry harms performance, reduce verbosity, sample, aggregate, or move expensive diagnostics to temporary windows; do not remove minimum security/audit/evidence signals. |
| Testing | CI must test that forbidden fields are not emitted and that protected actions still produce minimum trace/audit/evidence when diagnostic verbosity is lowered. |

# 17. Concurrency, Heavy Transaction, Idempotency, Outbox, and Resilience Lab

Greenfield readiness must include a resilience lab. The lab proves that retry, replay, duplicate messages, concurrent requests, heavy load, external dependency failure, cache outage, Kafka outage, policy outage, database contention, and partial failure produce safe, traceable outcomes.
| Resilience Area | Readiness Control |
| --- | --- |
| Concurrency tests | Optimistic locking, row_version, unique idempotency keys, transaction boundaries, deadlock handling, and duplicate request simulation. |
| Heavy transaction tests | Synthetic load for login/session, workspace resolution, MicroFunction execution, outbox publishing, Kafka consumers, audit writes, and evidence records. |
| Retry safety | Network retry, client retry, workflow retry, Kafka redelivery, outbox dispatcher retry, and agent/tool action retry must not duplicate effects. |
| DLQ/replay | DLQ reason, quarantine, approval, replay, reprocess, dedupe proof, trace reconstruction, and evidence closure. |
| Resilience patterns | Timeouts, retries with backoff, circuit breakers, bulkheads, fallback, compensation, backpressure, cache rebuild, and safe degraded modes. |
| Failure injection | Non-prod tests simulate OPA unavailable, Keycloak unavailable, Kafka broker down, DB deadlock, Redis down, model gateway unavailable, and evidence store unavailable. Protected flows fail closed or escalate. |

# 18. Security, OPA/SBAC, Abuse Cases, Authenticated DAST, Secure APIs, and Secrets Hygiene
| Security Area | Mandatory Baseline |
| --- | --- |
| OPA/SBAC expansion | Policy repository, Rego tests, decision input schema, skill catalog, approval policy, classification routing, denial reason taxonomy, and policy audit record. |
| Abuse cases | Authentication abuse, authorization bypass, step-up bypass, IDOR, prompt injection, tool abuse, unsafe agent action, replay abuse, DLQ replay abuse, workspace component abuse, admin template abuse. |
| Authenticated DAST | OWASP ZAP or approved DAST configured only for non-prod synthetic scope, authenticated sessions, least-privilege test accounts, excluded destructive actions, scan evidence, findings triage, and remediation proof. |
| Secure APIs | TLS, gateway enforcement, authN/authZ, tenant scoping, CSRF/CORS where applicable, safe errors, rate limits, input validation, output encoding, idempotency, correlation, and no stack traces or tokens. |
| Secrets hygiene | No secrets in Git, .env, prompts, screenshots, logs, tests, Obsidian, LLM Wiki, GitNexus reports, or generated artifacts. Use Vault-compatible references and approved local development adapters. |
| Security evidence | Secret scan, SAST, SCA, SBOM, container scan, DAST, policy tests, redaction tests, abuse-case tests, waiver records, remediation evidence, and closure approval. |

# 19. AI DevSecOps, System Builder Lite, Codex, Hermes, and Agent Readiness
| AI Readiness Area | Required Control |
| --- | --- |
| ChatGPT Project | Used for source-aware architecture review, document synthesis, setup guidance, and governance reasoning. No Restricted data unless approved. No raw production secrets or PII. |
| Codex in VS Code | Enabled only after repository rules, AGENTS.md/CLAUDE.md-derived instructions, branch protection, evidence capture, and local validation are ready. Drafts code/config/tests only in branch/sandbox. |
| Hermes Agent | Deferred until governed agent registry, SBAC, OPA, tool gateway, guardrails, logging, evidence, kill switch, and non-prod sandbox are ready. |
| LiteLLM / model gateway | All model routes use approved aliases, classification routing, guardrails, audit, quota, and fallback rules. Direct provider SDK calls from application code are prohibited. |
| Agent lifecycle | Agent definition, owner, purpose, non-goals, skill profile, classification ceiling, tool scope, model route, guardrail, evaluation dataset, autonomy tier, revocation path, and recertification record required. |
| Progressive autonomy | Advisory and draft generation may proceed under controls. Tool actions require Harness/MCP gateway, SBAC, OPA, audit, idempotency, dry-run where feasible, rollback, and human approval by risk tier. |

# 20. Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop

Auto-Heal, Auto-Learn, and Auto-Improve are candidate loops, not uncontrolled autonomy. The environment must support issue detection, evidence retrieval, impact analysis, candidate generation, tests, PR/MR evidence, human review, and controlled promotion.
| Candidate Loop Stage | Required Evidence-Producing Treatment |
| --- | --- |
| Detect | Use logs, traces, metrics, Sentry issues, audit events, security findings, CI failures, GitNexus impact, user feedback, incidents, and SLO burn as classified diagnostic input. |
| Retrieve evidence | Gather source commit, release, config version, contract, schema, trace, metric, log, audit, test, scan, policy, and evidence_ref without exposing sensitive data. |
| Analyze root cause | Classify severity, blast radius, affected bounded context, security impact, data impact, contract impact, tests required, rollback path, and human approval path. |
| Generate candidate | Draft fix, test, policy, configuration, runbook, learning note, or architecture improvement in branch/sandbox only. No direct production mutation. |
| Validate | Run deterministic tests, regression tests, policy tests, architecture fitness, scans, DAST where applicable, replay tests, and evidence pack generation. |
| Approve and promote | Human maker-checker approval, CODEOWNERS, ARB/CAB where required, rollback/forward-fix plan, monitoring, and post-change review. |
| Learn | Promote only reviewed lessons to Obsidian/LLM Wiki. Quarantine unverified AI conclusions and record known limitations. |

# 21. Environment Promotion, Reversibility, and Recovery Readiness
| Environment | Promotion / Readiness Gate |
| --- | --- |
| Local | Synthetic data only, no production secrets, devcontainer parity, local test evidence, no uncontrolled AI context. |
| DEV | GitOps/IaC or approved automation, smoke tests, policy checks, logs/traces, audit/evidence path, rollback and rebuild procedure. |
| INT/TEST | Contract compatibility, Kafka/event tests, Flyway migration validation, integration evidence, DAST with synthetic accounts, resilience tests. |
| UAT | Business readiness, representative synthetic or approved classified data, sign-off evidence, audit, accessibility, performance, rollback, training readiness. |
| STG | Production-like controls, change ticket, CAB readiness, observability dashboards, security monitoring, backup/restore, DR/recovery rehearsal. |
| PROD | Requires CAB/ARB/security approval, evidence pack, deployment plan, rollback/forward-fix/compensation, monitoring, hypercare, no direct mutation, break-glass only by approved process. |

# 22. RACI and Separation of Duties
| Role | RACI | Responsibilities |
| --- | --- | --- |
| Solutions Architecture Office / IT Head | A | Owns architecture baseline, final interpretation, cross-document reconciliation, and v3.2 adoption. |
| Enterprise Architecture | R/C | Reviews boundaries, DDD, SOLID, ports/adapters, ADR/TDL, and fitness functions. |
| DevSecOps Lead | R | Owns CI/CD, evidence pack, GitNexus integration, build/test/scan/provenance gates, and repository governance. |
| Security Architecture / IAM | R/C | Owns OPA/SBAC, identity, secrets, abuse cases, DAST scope, policy tests, and security evidence. |
| Software Development Lead | R | Owns developer workflow, backend/frontend implementation readiness, code review discipline, and test quality. |
| Frontend Lead | R | Owns Dynamic Workspace renderer, UX/accessibility, generated clients, frontend telemetry, and safe UI states. |
| Backend Lead | R | Owns MicroFunction runtime, API contracts, service boundaries, idempotency, outbox, and adapters. |
| DBA / Data Architect | R/C | Owns Flyway, PostgreSQL, schema ownership, RLS, idempotency/outbox schema, and migration evidence. |
| QA/SDET | R/C | Owns deterministic tests, Playwright, resilience lab tests, contract tests, DAST coordination, and evidence verification. |
| SRE / Operations | R/C | Owns observability, dashboards, SLOs, alerting, runbooks, incident/recovery paths, and telemetry toggle controls. |
| AI Governance / Agent Owner | R/C | Owns model routes, guardrails, agent lifecycle, evaluation, autonomy tier, and revocation. |
| Internal Audit | C/I | Reviews AVCI evidence, control operation, separation of duties, waiver aging, and evidence retention. |

# 23. Implementation Roadmap
| Phase | Milestone | Exit Evidence |
| --- | --- | --- |
| Phase 0 | Approve v3.2 baseline | Review with Architecture, DevSecOps, Security, QA/SDET, DBA, SRE, AI Governance; record adoption decision and open reconciliation items. |
| Phase 1 | Secure workstation and source bootstrap | Windows baseline, approved accounts, Git workspace, active sources, activity ledger, evidence register, Obsidian projection. |
| Phase 2 | Repository and devcontainer control | Branch protection, CODEOWNERS, AGENTS.md/CLAUDE.md-derived rules, PR/MR templates, pinned toolchains, devcontainer smoke test. |
| Phase 3 | CI/CD and evidence factory | Build/test/scan/SBOM/provenance/GitNexus/evidence pack for sample service and sample workspace component. |
| Phase 4 | Security and policy baseline | Keycloak/OIDC, OPA/SBAC, Vault-compatible references, policy tests, secret scan, abuse-case checklist, authenticated DAST scope. |
| Phase 5 | API/event/database baseline | OpenAPI, AsyncAPI, Kafka/Avro/CloudEvents, outbox/inbox, Flyway, idempotency, replay/DLQ runbooks. |
| Phase 6 | Dynamic Workspace and MicroFunction readiness | Workspace resolver, component registry, capability binding, MicroFunction runtime assembly, frontend generated clients, policy-filtered rendering. |
| Phase 7 | Observability and resilience lab | Log4j2, OpenTelemetry, Sentry, Loki, Tempo, Grafana dashboards, runtime toggles, heavy transaction/concurrency tests. |
| Phase 8 | System Builder Lite and AI agent sandbox readiness | Codex constrained use, LiteLLM/guardrails, agent registry, SBAC, OPA, evaluation, non-prod tool gateway, evidence. |

# 24. Acceptance Criteria and Go/No-Go Gate
| Gate | Pass Condition |
| --- | --- |
| AC-01 Source authority | Approved source baseline loaded; register references current; activity ledger and evidence register active; obsolete/superseded docs identified. |
| AC-02 Workstation security | Baseline secured, patched, encrypted, endpoint-protected, least privilege, no production data, no unmanaged tools. |
| AC-03 Repository governance | Branch protection, CODEOWNERS, PR/MR templates, AI-use declaration, AVCI summary, rollback section, evidence path. |
| AC-04 Toolchain reproducibility | Pinned Java 25/devcontainer/build tools; local and CI smoke tests pass; SBOM and scan evidence generated. |
| AC-05 CI/CD evidence | Build, unit, component, contract, policy, architecture, security, SCA, secrets, SBOM/provenance, GitNexus, and evidence pack pass. |
| AC-06 Dynamic Workspace | Backend resolver, component registry, capability binding, policy-filtered rendering, safe UI states, accessibility, frontend telemetry, and rollback evidence proven. |
| AC-07 MicroFunction runtime | Runtime assembly, mandatory steps, policy, idempotency, audit, outbox, observability, cache rebuild, and rollback tests pass. |
| AC-08 API/eventing | OpenAPI/AsyncAPI, Avro/CloudEvents, Kafka, schema compatibility, idempotent consumers, DLQ and replay pass with evidence. |
| AC-09 Database/Flyway | Flyway clean migrate validates initial schema; no manual DDL; idempotency/outbox/evidence schema tested. |
| AC-10 Observability | Log4j2/OTel/Sentry/Loki/Tempo/Grafana pipeline active; trace reconstruction works; forbidden telemetry fields blocked. |
| AC-11 Resilience lab | Concurrent, heavy-load, retry, duplicate, outage, DLQ/replay, compensation, and failure-aware tests pass. |
| AC-12 Security | OPA/SBAC tests, abuse-case tests, authenticated DAST scope, secret scans, secure API tests, and remediation evidence complete. |
| AC-13 AI governance | Codex/System Builder Lite constrained; LiteLLM/guardrails ready; no direct provider calls; agents not activated without registry/evaluation/SBAC/OPA. |
| AC-14 Runtime toggles | Telemetry and feature toggles are policy-governed, audited, reversible, time-bound where needed, and minimum audit/security evidence remains on. |
| AC-15 AVCI | Every output is attributable, verifiable, classifiable, and improvable with owner, source, evidence, classification, and improvement path. |

Go decision: all P0 gates pass, Critical/High findings are fixed or formally waived, evidence is complete, and owner/checker approvals are recorded. No-go decision: missing source authority, missing evidence, secret leakage, direct production mutation, failed policy/security gate, uncontrolled AI action, missing rollback, or any fail-open protected action.

# 25. Cross-Document Reconciliation and Future Regeneration Candidates
| Item | Gap / Risk | Severity | Recommended Action |
| --- | --- | --- | --- |
| Runtime telemetry toggles | Partially covered in observability/runtime configuration documents but needs consistent treatment across 31A, 53, 60, and runtime platform guides. | High | Create or update Runtime Telemetry Toggle Governance section in observability and dynamic workspace standards. |
| Greenfield readiness vs PoC readiness | 09, 39B/39C, 42C, and 45 overlap but do not always share the same readiness vocabulary. | Medium | Adopt v3.2 readiness gates as the greenfield umbrella and cross-reference in PoC roadmap. |
| Dynamic Workspace in environment baseline | Strong coverage in 46-61 but not always pulled back into the core 09 environment standard. | High | This v3.2 version makes Dynamic Workspace readiness a 09 gate. |
| Heavy transaction / resilience lab | Roadmap covers concurrency and resilience, but environment setup must ensure tools, fixtures, Kafka, DB, and tests exist before feature delivery. | High | Add resilience lab readiness to 09, 31, 52, 60, and PoC roadmap. |
| Authenticated DAST | Referenced in DevSecOps and security, but setup details need synthetic accounts, scan boundaries, exclusions, and remediation evidence. | High | Add authenticated DAST readiness to 09, 11A, 17A, 20, 45, and Dynamic Workspace DevSecOps guide. |
| Secrets hygiene in local AI workflows | Covered broadly but must be stricter for prompts, screenshots, Obsidian, LLM Wiki, GitNexus, and AI-generated test fixtures. | High | Add local AI secrets hygiene gate to 09, 39B/39C, 22A, 42H, and 58. |
| Known numbering issues | 11A duplicate numbering, 41B/44 System Builder overlap, 01A v1.1 placement, older superseded references, active-source deduplication, future packer/regeneration runbook. | Medium | Track in 00D / revision-control matrix and avoid silent normalization. |

# 26. Risk and Control Register
| Risk ID | Risk | Required Control |
| --- | --- | --- |
| R-01 Uncontrolled tool installation | Unapproved tools or plugins weaken reproducibility and security. | Technology Stack approval, devcontainer pinning, SBOM, SCA, workstation inventory, ARB/CAB waiver. |
| R-02 AI bypass of governance | AI assistant drafts or executes outside source authority or human approval. | AGENTS.md/CLAUDE.md, LiteLLM, guardrails, SBAC, OPA, Harness, no direct production credentials, AI-use evidence. |
| R-03 Frontend authority drift | Frontend embeds authorization, business rules, or unregistered endpoints. | Generated clients, backend resolver, OPA/SBAC, component registry, architecture fitness, Playwright/security tests. |
| R-04 MicroFunction hardcoding | Business logic bypasses runtime assembly, policy, audit, or outbox. | Publish validator, package rules, ArchUnit/Semgrep, mandatory step tests, PR/MR principle impact. |
| R-05 Observability overload | Excessive telemetry affects performance and causes teams to disable controls. | Telemetry profiles, sampling, runtime toggle governance, minimum security/audit evidence always on. |
| R-06 Secret leakage | Secrets exposed in prompts, logs, screenshots, tests, Obsidian, LLM Wiki, or Git. | Secret scans, redaction tests, Vault-compatible references, prompt hygiene, evidence scrubbing, training. |
| R-07 Event replay duplication | DLQ/replay or retries duplicate business effects. | Idempotency registry, inbox, deterministic replay tests, dedupe evidence, replay approval workflow. |
| R-08 Evidence gaps | Work appears complete but cannot be audited or reconstructed. | Evidence pack generator, required PR/MR template, CI artifacts, dashboards, audit records, reviewer gate. |

# 27. AVCI Compliance Summary
| AVCI Property | v3.2 Evidence |
| --- | --- |
| Attributable | Document control defines owner, co-owners, authority, review cadence, evidence path, supersedes value, and implementation roles. Environment actions must record actor, source, ticket, branch, commit, tool, prompt, model route, policy decision, and approver. |
| Verifiable | Readiness requires tests, scans, SBOM/provenance, GitNexus impact, contract tests, Flyway validation, OPA tests, observability proof, resilience tests, DAST evidence, and acceptance gates. |
| Classifiable | Workstations, repositories, prompts, logs, traces, metrics, audit records, evidence, screenshots, Dynamic Workspace configuration, AI outputs, and artifacts carry classification and handling rules. |
| Improvable | Findings, failed gates, incidents, SLO burn, DAST findings, GitNexus drift, missing tests, duplicate docs, and setup lessons feed controlled Auto-Learn/Auto-Improve backlogs without silent mutation. |

# Appendix A. Greenfield Evidence Pack Template

Environment identity: environment name, owner, purpose, classification, target use, date, approver, evidence path.

Source baseline: active source pack/register versions, source commit/hash, superseded documents excluded, open reconciliation items.

Workstation proof: OS baseline, patch status, endpoint protection, encryption, user privilege, approved tool list, no production data attestation.

Repository proof: branch protection, CODEOWNERS, rules, PR/MR templates, AGENTS.md/CLAUDE.md-derived controls, signed commits/artifacts where supported.

Toolchain proof: Java/toolchain versions, Node/package manager versions, devcontainer digest, CI runner image digest, dependency locks.

Build/test proof: compile, unit, component, contract, policy, architecture, frontend, Playwright, Flyway, outbox, idempotency, and resilience tests.

Security proof: secret scan, SAST, SCA, SBOM, container scan, authenticated DAST where applicable, abuse-case tests, remediation evidence.

Observability proof: logs, traces, metrics, audit, dashboards, Sentry/Loki/Tempo/Grafana links, forbidden field tests, runtime toggle evidence.

AI-use proof: model route, prompt version, guardrail result, tool action scope, human checker, generated artifacts, limitations, and revocation path.

Rollback proof: rebuild steps, safe-disable controls, feature flags, migration forward-fix, compensation, cache rebuild, replay/reprocess path.

AVCI summary: attributable, verifiable, classifiable, improvable evidence and outstanding issues.

# Appendix B. Environment Validation Checklist
| Checklist Area | Pass Condition |
| --- | --- |
| Source and governance | Active source baseline loaded; document register current; reconciliation items logged; evidence path exists. |
| Workstation security | Encrypted, patched, least privilege, endpoint protection, approved network, no local production data. |
| Repository | Branch protection, CODEOWNERS, PR template, AI-use declaration, rollback section, evidence path, secret scanning. |
| Devcontainer | Pinned versions, no secrets, SBOM, SCA, local/CI parity, sample build passes. |
| CI/CD | Build, test, scan, SBOM, provenance, GitNexus, evidence pack, and blocker rules operate. |
| Contracts | OpenAPI, AsyncAPI, Avro, CloudEvents, generated clients, compatibility tests. |
| Database | Flyway clean migrate, idempotency/outbox schema, RLS where applicable, rollback/forward-fix plan. |
| MicroFunction | Runtime assembly, mandatory steps, policy, audit, outbox, observability, cache rebuild tests. |
| Dynamic Workspace | Backend resolver, component registry, capability binding, OPA/SBAC filtering, accessibility, frontend telemetry. |
| Observability | Log4j2, OpenTelemetry, Sentry, Loki, Tempo, Grafana, audit/evidence, forbidden field tests. |
| Security | OPA/SBAC, secrets hygiene, abuse cases, authenticated DAST scope, secure API tests, remediation workflow. |
| Resilience | Retry, replay, concurrency, heavy transaction, failure injection, DLQ, compensation, and trace reconstruction. |
| AI governance | LiteLLM, guardrails, Codex constraints, System Builder Lite boundaries, agent sandbox controls, no direct model calls. |

# Appendix C. Source and External Reference Register
| Reference | AIRA Treatment |
| --- | --- |
| AIRA internal references | AIRA active baseline: Manifest v2.0, Registers 00A-00D, Source Packs 01-10 plus current expanded source packs provided for review. Older manifests, superseded files, duplicates, and informal drafts remain historical unless used for audit comparison or reconstruction. |
| NIST SP 800-218 SSDF v1.1 | Secure Software Development Framework final reference for secure development practices and supplier/customer secure software vocabulary. |
| NIST SP 800-218A | Secure software development practices for generative AI and dual-use foundation models; used as AI-secure-development alignment input. |
| NIST SP 800-218r1 / SSDF v1.2 draft | Draft watchlist only. Do not treat as binding AIRA baseline until final adoption review. |
| OWASP ASVS 5.0.0 | Application security verification requirements reference for secure API, authentication, authorization, session, input validation, error handling, logging, and verification depth. |
| OpenTelemetry Semantic Conventions 1.42.0 | Reference for consistent telemetry attributes across traces, metrics, logs, resources, messaging, HTTP, database, and exceptions. |
| SLSA v1.2 | Software supply-chain evidence reference for provenance, build integrity, and artifact trust controls. |
| AIRA interpretation rule | External sources inform control design but do not override AIRA governance, owner approval, classification, SBAC/OPA, CAB/ARB, or AVCI evidence. |

