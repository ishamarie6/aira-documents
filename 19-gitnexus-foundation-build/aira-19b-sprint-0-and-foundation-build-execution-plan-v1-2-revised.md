---
title: "Sprint 0 and Foundation Build Execution Plan"
doc_id: "AIRA-19B"
version: "v1.2"
status: "revised"
category: "GitNexus and foundation build"
source_docx: "AIRA_19B_Sprint_0_and_Foundation_Build_Execution_Plan_v1.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 19-gitnexus-foundation-build
  - revised
  - aira-19b
---



# Sprint 0 and Foundation Build Execution Plan



AIRA

AI-Native Enterprise Platform

AIRA Sprint 0 and Foundation Build Execution Plan

v1.2 Revised

Foundation Backlog - Platform Bootstrap - Team Readiness - System Builder Lite - Dynamic Workspace - MicroFunction Runtime - DevSecOps Evidence - Resilience Lab
| Property | Value |
| --- | --- |
| Document ID | AIRA-DOC-019B |
| Canonical Filename | AIRA_19B_Sprint_0_and_Foundation_Build_Execution_Plan_v1.2_Revised.docx |
| Version | v1.2 - 09 v3.2, 39A v1.1, 39B v1.3, 39C v1.2, Dynamic Workspace, MicroFunction Runtime, DevSecOps Evidence, GitNexus, API/Eventing, Observability, Resilience Lab, Security, and Governed Auto-Improve Alignment Update |
| Supersedes | 19B-AIRA_Sprint_0_and_Foundation_Build_Execution_Plan_v1.1_Aligned.docx |
| Status | Draft for Architecture, DevSecOps, Security, Platform Engineering, QA/SDET, DBA, SRE, AI Governance, Knowledge Governance, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; DevSecOps Lead; Software Development Lead; Security Architecture; Platform Engineering; QA/SDET; DBA; SRE / Operations; AI Governance; Knowledge Governance; Internal Audit |
| Primary Audience | Software Development Team; DevSecOps; Infrastructure; Security; DBA; QA/SDET; Product Owner; System Builder Lite operators; AI agent owners; reviewers; Internal Audit |
| Primary Parents | 09-AIRA Greenfield Environment Standard v3.2 Revised; 39A VS Code Codex System Builder Lite Agent and Tool Setup Guide v1.1 Revised; 39B Greenfield AI DevSecOps Workstation Setup and System Builder Lite Implementation Guide v1.3 Revised; 39C Team Greenfield AI DevSecOps Workstation and Governed Agent Setup Playbook v1.2 Revised |
| Companion Sources | 01/01A AVCI and Enterprise Design Principles; 02 Engineering Blueprint; 03 Developer Guide; 04 Technology Stack; 07 Skills Framework; 07B Team Transformation; 10/10A/10B/10C/10D MicroFunction; 11/11A/20 DevSecOps and Evidence Pack; 12A/41/46-61 Dynamic Workspace; 15/15A API and Contract; 16/16A/16B Flyway and Database; 17/17A Security; 19 GitNexus; 19C Backlog Planning; 21A/21B Knowledge and Runtime Platform; 22A Prompt/Guardrail/Model Registry; 31/31A Operations and Observability; 42D-42S AI Agent Governance; 43 Continuous Improvement; 45 PoC 2 Foundation Factory |
| External Alignment Reference | NIST SP 800-218 SSDF and SP 800-218A AI software practices; OWASP ASVS 5.0.0; OpenTelemetry Semantic Conventions; SLSA v1.2 |
| Review Cadence | Weekly during Sprint 0; at Sprint 0 closeout; monthly through PoC 1/1A/2; quarterly after stabilization; unscheduled on material architecture, DevSecOps, toolchain, AI, repository, security, database, Dynamic Workspace, or MicroFunction change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Sprint-0-Foundation-Build / 19B / v1.2 / |
| Mandatory Practice Statement Sprint 0 is not a calendar formality and not a feature sprint. Sprint 0 is accepted only when the AIRA team can repeatedly build, test, secure, observe, govern, evidence, roll back, and improve a foundation change through approved repositories, System Builder Lite controls, MicroFunction runtime assembly, Dynamic Workspace boundaries, CI/CD gates, OPA/SBAC policy, GitNexus read-only impact analysis, and AVCI evidence. Business feature development must not start until the Ready-to-Code and Foundation Build Exit Gates are approved. |
| --- |

# Static Table of Contents

1. Executive Summary

2. v1.2 Update Verdict and Alignment Decision

3. Purpose, Scope, and Authority

4. Sprint 0 Operating Principles

5. Sprint 0 Governance Gates

6. Foundation Build Workstreams and Backlog

7. Execution Sequence and Sprint Board Model

8. Repository, Branch, PR/MR, and Evidence Controls

9. DevSecOps Pipeline, GitNexus, and Evidence Pack Baseline

10. Dynamic Workspace and MicroFunction Foundation Alignment

11. API, Eventing, Database, and Contract Foundation

12. Observability, Runtime Toggles, and Evidence Correlation

13. Security, OPA/SBAC, Secrets Hygiene, Abuse Cases, and Authenticated DAST

14. Concurrency, Heavy Transaction, Idempotency, Outbox, and Resilience Lab

15. System Builder Lite, Codex, Agent Sandbox, and AI Governance

16. Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop

17. Foundation Technical Build Details

18. Risks, Dependencies, Assumptions, and Decisions

19. RACI and Separation of Duties

20. Sprint 0 Closeout and Handoff to Sprint 1

21. Acceptance Criteria and Definition of Done

22. Open Issues and AVCI Reconciliation Items

23. AVCI Compliance Summary

Appendix A. Sprint 0 GitHub Issue Template

Appendix B. Sprint 0 Evidence Record Template

Appendix C. Ready-to-Code Sign-Off Checklist

# 1. Executive Summary

This v1.2 revision updates AIRA-DOC-019B from a foundation execution plan into the active Sprint 0 control plan that follows the newly revised Greenfield Environment and workstation/System Builder Lite documents. The document keeps the original baseline principle: Sprint 0 is the controlled execution bridge between approved architecture standards and the first production-bound development work. It now strengthens the plan so Sprint 0 explicitly proves the end-to-end AIRA engineering factory before the team starts feature volume.

The revised plan requires Sprint 0 to establish repository governance, developer workstation readiness, devcontainer parity, CI/CD evidence gates, GitNexus read-only impact analysis, security and OPA/SBAC controls, contract-first API and event baselines, Flyway-governed database baselines, MicroFunction runtime skeletons, Dynamic Workspace shell readiness, observability and runtime toggle controls, resilience lab readiness, System Builder Lite boundaries, and proposal-driven improvement loops.
| Strategic Outcome | Sprint 0 Delivery Mechanism |
| --- | --- |
| Controlled start | Approved repositories, branch protection, CODEOWNERS, PR/MR templates, issue templates, labels, milestones, and evidence paths are created before mergeable work. |
| Team readiness | Each developer has an attested workstation, approved AI seat, devcontainer/local stack, VS Code/Codex setup, and onboarding evidence. |
| Architecture enforcement | SOLID, Clean Architecture, DDD, ports/adapters, MicroFunction boundaries, Dynamic Workspace boundaries, and direct-provider/direct-DB prohibitions are checked locally and in CI. |
| Security from Day 0 | Keycloak/AD pattern, Vault/OpenBao reference, OPA/SBAC policy skeleton, secrets scan, abuse-case catalog, authenticated DAST scope, and classification-safe handling are established early. |
| Evidence readiness | Every workstream produces AVCI evidence: owner, source, verification, classification, approval, rollback, and improvement path. |
| Progressive autonomy | Codex and logical agents remain draft-and-review assistants. Tool actions are governed through System Builder Lite, Harness/SBAC/OPA, CI evidence, and human approval. |
| Executive Decision Controlled foundation development may start only after the Ready-to-Start Gate is approved. Business module coding must wait until the Ready-to-Code Gate, Ready-to-Integrate Gate, and Sprint 0 Foundation Exit Gate are approved or formally waived by the required authority. |
| --- |

# 2. v1.2 Update Verdict and Alignment Decision
| Area | v1.1 Baseline | v1.2 Required Update |
| --- | --- | --- |
| Environment readiness | Greenfield setup and readiness gates existed but were separated from workstation execution details. | Align Sprint 0 explicitly to 09 v3.2, 39A v1.1, 39B v1.3, and 39C v1.2 so the plan becomes executable by the team. |
| Dynamic Workspace | Frontend and workspace readiness were implicit foundation outcomes. | Add Dynamic Workspace foundation workstream: backend-governed layout, component registry, OpenAPI clients, policy-filtered resolver, telemetry, and safe UX/a11y baseline. |
| MicroFunction runtime | MicroFunction skeleton was part of the foundation baseline. | Require sample transaction proving idempotency, audit, outbox, compensation, policy, traceability, error handling, safe response, and backend ports/adapters. |
| DevSecOps / GitNexus | CI/CD and evidence gates were required. | Add GitNexus read-only impact evidence, Derived Artifact summary, SBOM/provenance, authenticated DAST preparation, SLSA-oriented supply-chain controls, and PR/MR AVCI validation. |
| API and eventing | Contract-first baseline existed. | Strengthen OpenAPI, AsyncAPI, Kafka, Avro, CloudEvents, schema evolution, outbox/inbox, DLQ, replay, idempotent consumer, correlation, and compatibility evidence. |
| Observability | Observability hooks were required. | Add Log4j2 structured logs, OpenTelemetry, Sentry, Loki, Tempo, Grafana dashboards, runtime telemetry toggles, forbidden telemetry fields, and trace reconstruction evidence. |
| Resilience / heavy transaction | Idempotency and outbox were included. | Add resilience lab readiness: concurrency tests, duplicate-safe consumers, failure injection, retry/circuit breaker/bulkhead checks, DLQ/replay, and compensation evidence. |
| Continuous improvement | Auto-Heal/Auto-Learn/Auto-Improve were advisory. | Make candidate loops Sprint 0-ready: issue detection, evidence retrieval, proposal, tests, PR, human approval, and knowledge-review gates. |

# 3. Purpose, Scope, and Authority

The purpose of this plan is to define the work, sequencing, acceptance criteria, roles, and evidence required to complete Sprint 0 for AIRA. It gives the Software Development, DevSecOps, Security, Infrastructure, DBA, QA/SDET, AI Engineering, and Knowledge Governance teams a governed execution model before normal feature delivery begins.
| In Scope | Out of Scope |
| --- | --- |
| Repository bootstrap, branch protection, CODEOWNERS, PR/MR templates, issue templates, labels, milestones, project board, and evidence register. | Full business module delivery except a controlled sample transaction used to prove the framework. |
| Workstation cohort readiness, VS Code/Codex setup, devcontainer/local stack parity, local hooks, and AI usage acknowledgement. | Production deployment, customer data migration, external customer go-live, production model use, or production secrets on developer machines. |
| CI/CD pipeline skeleton with build, unit, component, contract, migration, security, architecture, policy, SBOM, GitNexus, and evidence stages. | Direct autonomous deployment, direct model provider integration, direct production database access, or unmanaged public repository use. |
| MicroFunction runtime skeleton, sample transaction, Dynamic Workspace shell, OpenAPI/AsyncAPI baseline, Flyway schema baseline, observability baseline, security baseline, and resilience lab baseline. | Full DR/BCP, UAT, production operations manual, and full agentic autonomy beyond sandbox/draft/review controls. |
| System Builder Lite operating model, governed agent sandbox, logical reviewer agents, prompt execution workflow, and Auto-Heal/Auto-Learn/Auto-Improve candidate loop. | Allowing AI, Codex, GitNexus, or agents to approve, merge, deploy, mutate production, disable controls, or promote knowledge without review. |
| Authority Level | Document / Control | Sprint 0 Impact |
| --- | --- | --- |
| L0 | Architecture Board / CAB / IT Head | Final authority for major architecture direction, exceptions, waivers, production-impacting readiness, and unresolved conflicts. |
| L1 | 02 Engineering Blueprint; 11 DevSecOps; 09 Greenfield Environment | Controls architecture, lifecycle gates, environment readiness, CI/CD evidence, and platform build discipline. |
| L2 | 01 AVCI; 01A Enterprise Design Principles; 07/07B Skills and maturity | Controls SOLID, Clean Architecture, DDD, ports/adapters, progressive autonomy, trust evidence, and skill-based delegation. |
| L2 | 10 MicroFunction; 12A/41/46-61 Dynamic Workspace; 15 API; 16 Database; 17 Security; 19 GitNexus; 31A Observability; 42 AI Governance | Controls implementation-specific boundaries, contracts, policies, events, database, telemetry, security, AI, and evidence. |
| L3 | This Sprint 0 Plan | Controls execution sequence, backlog, readiness gates, acceptance criteria, and Sprint 0 closeout evidence. |
| L4 | Tickets, PRs/MRs, CI runs, evidence packs, dashboards, sign-offs | Operational proof. These cannot weaken higher-authority standards. |

# 4. Sprint 0 Operating Principles
| ID | Principle | Sprint 0 Meaning |
| --- | --- | --- |
| S0-01 | AVCI by construction | Every artifact has owner, source, version, classification, verification evidence, and improvement path. |
| S0-02 | Architecture first | Repositories, services, packages, events, schemas, and pipelines follow approved boundaries before business code is added. |
| S0-03 | Configuration-first | Use MicroFunction catalog entries, templates, DMN/rules, OPA, OpenAPI/AsyncAPI, and configuration before custom code. |
| S0-04 | Secure by default | No secret, credential, raw token, PII, unapproved model key, or unrestricted admin path enters code, logs, prompts, screenshots, or evidence. |
| S0-05 | Deterministic evidence | Mergeable code includes deterministic tests, reproducible build, migration proof, policy results, and evidence manifest. |
| S0-06 | Fail-safe, not fail-open | If identity, policy, guardrail, secrets, audit, or evidence dependencies fail, controlled operations stop. |
| S0-07 | One contribution path | All changes enter through protected Git workflow, CODEOWNERS review, CI gates, signed/reproducible artifacts, and retained evidence. |
| S0-08 | AI bounded by governance | AI drafts and analyzes. Humans approve. Tool execution follows System Builder Lite, Harness, SBAC, OPA, trust score, and audit boundaries. |
| S0-09 | Observable and reversible | Foundation components emit trace/log/metric/audit/evidence and define rollback, forward-fix, rebuild, safe-disable, or compensation. |
| S0-10 | Rebuildability | A new workstation/devcontainer can be rebuilt from Golden Source and produce equivalent build/test/evidence results. |

# 5. Sprint 0 Governance Gates

## 5.1 Ready-to-Start Gate
| Gate | Minimum Evidence | Owner | Decision |
| --- | --- | --- | --- |
| G1 Canonical Sources Confirmed | Active standards, source packs, 09/39A/39B/39C revisions, document register, and reconciliation items identified. | Solutions Architect | Required |
| G2 Owners Assigned | Workstream owners, reviewers, CODEOWNERS, RACI, and escalation paths defined. | IT Head / PMO | Required |
| G3 Environment Baseline Approved | Workstation, devcontainer, repository, AI seat, and evidence path standards approved. | DevSecOps / Security | Required |
| G4 Risk and Classification Set | Data classification, AI tool eligibility, secrets rules, source handling, and evidence storage rules approved. | Security / Data Governance | Required |

## 5.2 Ready-to-Code Gate
| Gate | Minimum Evidence | Owner | Decision |
| --- | --- | --- | --- |
| C1 Workstation Attested | OS baseline, endpoint controls, installed tools, AI seat, access rights, VS Code/Codex setup, and local hooks verified. | System Administrator | Required |
| C2 Repository Protected | Branch protection, CODEOWNERS, PR template, issue templates, CLAUDE.md/AGENTS.md, and labels active. | DevSecOps | Required |
| C3 Local + CI Parity | Local build, tests, lint, secret scan, architecture checks, and CI strict mode pass on sample PR. | Developer / QA | Required |
| C4 Evidence Working | Pipeline artifacts, test reports, scan results, GitNexus output, SBOM, and AVCI summary stored in approved path. | DevSecOps / Internal Audit | Required |
| C5 AI Governance Verified | Codex/assistant use, no shadow AI, LiteLLM-only app model routing, guardrail placeholders, and human approval boundaries verified. | AI Governance | Required |

## 5.3 Foundation Exit Gate
| Gate | Minimum Evidence | Owner | Decision |
| --- | --- | --- | --- |
| F1 Foundation Services Build | Gateway, sample bounded-context service, MicroFunction runtime, Dynamic Workspace shell, policy, evidence, and observability stubs build and run. | Development Lead | Required |
| F2 Contracts Validated | OpenAPI/AsyncAPI, Avro/JSON schemas, CloudEvents metadata, error model, and idempotency contracts pass validation. | API Architect / QA | Required |
| F3 Database and Events Proven | Flyway clean/upgrade migration, outbox/inbox, DLQ/replay, idempotent consumer, and schema evolution proof complete. | DBA / Integration Lead | Required |
| F4 Security and DAST Ready | OPA/SBAC tests, abuse cases, secrets hygiene, authenticated DAST safe scope, and remediation evidence path complete. | Security | Required |
| F5 Closeout Approved | Sprint 0 closeout report, risks, waivers, backlog, evidence pack, and Sprint 1 handoff signed off. | Architecture Board / CAB | Required |

# 6. Foundation Build Workstreams and Backlog
| Workstream | Purpose | Exit Evidence |
| --- | --- | --- |
| W1 Governance and Source Baseline | Approve Sprint 0 plan, reconcile source references, publish decision log, create evidence path. | Document register update, reconciliation log, Sprint 0 kickoff approval. |
| W2 Repository Bootstrap | Create repo, branch rules, CODEOWNERS, PR/MR and issue templates, labels, milestones, AGENTS.md/CLAUDE.md. | Protected repo with sample governance PR. |
| W3 Workstation and Devcontainer Readiness | Apply 39B/39C/39A setup, attest workstations, install toolchain, test devcontainer rebuild. | Workstation attestation and rebuild evidence. |
| W4 CI/CD Evidence Pipeline | Implement build, unit, component, contract, migration, security, policy, GitNexus, SBOM, provenance, and evidence stages. | Sample PR evidence pack and pipeline summary. |
| W5 Security and Identity Baseline | Create OIDC/Keycloak local pattern, OPA/SBAC skeleton, secrets abstraction, safe local adapter, abuse-case tests. | Policy tests, negative authorization tests, no-secrets scan. |
| W6 API and Event Contract Baseline | Create OpenAPI, AsyncAPI, Avro/JSON schema, CloudEvents metadata, error contract, idempotency profile. | Linted contracts, generated clients/stubs, compatibility test. |
| W7 Database and Flyway Baseline | Create Flyway baseline for framework tables, audit, idempotency, outbox, inbox, DLQ, replay request, schema registry refs. | Clean/upgrade migration evidence and rollback/forward-fix plan. |
| W8 MicroFunction Runtime Skeleton | Create coordinator, step catalog, execution envelope, policy hooks, idempotency, audit, telemetry, outbox, compensation. | Sample transaction executes standard pre/post controls. |
| W9 Dynamic Workspace Shell | Create backend-governed workspace resolver, component registry, policy filtering, OpenAPI binding, frontend shell, UX/a11y baseline. | Workspace load trace, policy-deny test, component render smoke test. |
| W10 Observability and Runtime Toggles | Implement Log4j2 JSON logging, OTel traces/metrics, Loki/Tempo/Grafana/Sentry profile, telemetry toggles, forbidden-field tests. | Trace reconstruction sample and dashboard stub. |
| W11 Resilience Lab | Create concurrency, retry, circuit breaker, bulkhead, DLQ/replay, duplicate-message, failure injection, and heavy-load test harness. | Resilience lab report and defect backlog. |
| W12 System Builder Lite and Agent Sandbox | Configure Codex boundaries, logical reviewer agents, tool registry, SBAC/OPA action model, and no-direct-mutation rules. | Agent sandbox registry and tool action simulation evidence. |
| W13 Auto-Heal/Learn/Improve Candidate Loop | Create signal-to-candidate workflow: detect issue, retrieve evidence, propose fix/learning, test, PR, human approval. | Candidate loop dry run with rejected/approved examples. |
| W14 Operations and Knowledge Handoff | Create starter runbooks, evidence projection to Obsidian, LLM Wiki eligibility rules, closeout report, Sprint 1 readiness pack. | Closeout pack and handoff approval. |

# 7. Execution Sequence and Sprint Board Model
| Sequence | Major Activity | Dependencies | Exit Gate |
| --- | --- | --- | --- |
| Day 0 | Kickoff, source baseline confirmation, owners/RACI, evidence path, team acknowledgement. | Approved 09/39A/39B/39C and active source baseline. | Ready-to-Start |
| Days 1-2 | Repository bootstrap, issue board, branch protection, CODEOWNERS, templates, AGENTS.md/CLAUDE.md, labels. | Owners and Git platform access. | Repository Protected |
| Days 2-4 | Workstation/devcontainer cohort setup, VS Code/Codex config, local hooks, tool version report. | Repository bootstrap and workstation baseline. | Workstation Attested |
| Days 3-6 | CI/CD skeleton, tests, scans, SBOM, GitNexus, evidence manifest, sample PR. | Local build and repo templates. | CI Strict Mode |
| Days 5-9 | Security, API/event, Flyway, MicroFunction, Dynamic Workspace, observability, and resilience skeletons. | CI evidence pipeline and owners. | Foundation Build |
| Days 8-10 | Candidate loop dry run, closeout report, risks/waivers, Sprint 1 backlog readiness, acceptance review. | All workstream evidence. | Sprint 0 Exit |
| Board Column | Entry Rule | Exit Rule |
| --- | --- | --- |
| Intake | Request is captured with owner, classification, workstream, dependency, and acceptance evidence. | Ready for analysis or rejected as duplicate/out of scope. |
| Analysis | Impact, standards, risks, affected contracts, and required reviewers are identified. | Ready for design/build task. |
| Build / Configure | Work proceeds in feature branch or approved sandbox. | Local checks and draft evidence produced. |
| Review | Human maker-checker review, GitNexus impact, security/architecture checks, and evidence validation occur. | CI passes or risk is escalated. |
| Accepted | Gate owner confirms evidence and readiness. | Closeout or Sprint 1 handoff. |
| Blocked / Waiver | Critical issue, unresolved dependency, policy failure, or risk exception. | Resolved, waived with expiry, or deferred with owner. |

# 8. Repository, Branch, PR/MR, and Evidence Controls
| Control | Sprint 0 Required Baseline | Evidence |
| --- | --- | --- |
| Repository structure | Separate packages/modules for domain, application, adapter, infrastructure, config, contracts, tests, policies, migrations, docs, and evidence. | Repository tree and architecture fitness result. |
| Branch protection | No direct push to main; required reviews; CODEOWNERS; signed commits where feasible; required status checks; no bypass flags. | Branch rule screenshot/export and sample rejected bypass. |
| PR/MR template | Includes scope, EDP impact, AVCI summary, security, database, API/event, Dynamic Workspace, MicroFunction, tests, observability, rollback, AI use, and evidence links. | Merged template PR and sample completed PR. |
| Issue templates | Epic/story/task/security/defect/evidence/waiver templates include owner, classification, acceptance criteria, test path, evidence path, and dependencies. | GitHub/GitLab issue templates and sample issues. |
| Repository instructions | AGENTS.md/CLAUDE.md define no direct provider calls, no secrets, ports/adapters, no policy bypass, no production mutation, and evidence requirements. | Instruction files and CI check verifying presence. |
| Evidence retention | Pipeline artifacts, test reports, scan reports, GitNexus reports, SBOM, provenance, and AVCI summaries retained and linked to PR. | Evidence manifest and storage path. |
| Non-Negotiable Repository Rule AIRA source code, configuration, contracts, policies, migrations, prompts, and evidence must enter through protected Git workflow. Obsidian and LLM Wiki may contain curated summaries and approved knowledge projections, but they must not become uncontrolled replacement sources for code or production configuration. |
| --- |

# 9. DevSecOps Pipeline, GitNexus, and Evidence Pack Baseline
| Pipeline Stage | Minimum Sprint 0 Gate | Evidence Artifact |
| --- | --- | --- |
| Source / Preflight | Branch rule, CODEOWNERS, issue link, AI-use declaration, classification, and no-secret local pre-commit. | PR metadata, hook logs, secret scan output. |
| Build | Backend Java 25, frontend build, generated clients, devcontainer image digest, dependency lockfiles. | Build report, toolchain versions, image digest. |
| Unit / Component | JUnit, Vitest, component tests, policy tests, adapter tests, deterministic fixtures. | Test report, coverage, changed-line evidence. |
| Contract / Schema | OpenAPI, AsyncAPI, Avro/JSON schema, CloudEvents, Problem Details, idempotency, compatibility. | Contract lint, schema compatibility, generated client evidence. |
| Database / Migration | Flyway clean migration, upgrade migration, checksum, RLS/policy where applicable, rollback/forward-fix plan. | Flyway report, migration validation, DBA review. |
| Security | Secrets scan, SAST, SCA, container scan, IaC/Conftest, OPA/SBAC tests, authenticated DAST readiness. | Scan reports, policy decision, remediation backlog. |
| Architecture Fitness | ArchUnit, dependency rules, no direct provider calls, no direct DB from domain, no frontend authority, no policy bypass. | Fitness report and exception list. |
| GitNexus | Read-only impact analysis, affected tests/contracts, call graph, dependency graph, and drift signal for material changes. | GitNexus evidence record with commit SHA and report hash. |
| SBOM / Provenance | SBOM, package digest, tool version, build identity, provenance placeholder aligned to SLSA track readiness. | SBOM/provenance artifact and retention path. |
| Evidence Finalization | AVCI summary, known limitations, rollback, approvals, improvement backlog, closeout result. | Evidence pack manifest. |

# 10. Dynamic Workspace and MicroFunction Foundation Alignment
| Foundation Area | Sprint 0 Requirement | Acceptance Evidence |
| --- | --- | --- |
| Dynamic Workspace resolver | Backend resolves workspace, layout, component eligibility, policy filtering, classification, and cache source. Frontend must not become business authority. | Workspace resolution trace, OPA decision, layout hash, policy-deny test. |
| Component registry | Catalog contains component_key, version, owner, capability binding, classification, data contract, and MicroFunction/API binding. | Component registry seed and validation report. |
| Frontend shell | Next.js/React shell renders approved layout, generated client calls, safe error states, a11y baseline, and redaction. | Smoke test, accessibility check, redaction screenshot. |
| MicroFunction coordinator | Runtime assembler executes standard steps before/after STP-BUS logic: correlation, identity, classification, authorization, validation, idempotency, audit, telemetry, error, outbox, evidence. | Sample transaction execution evidence. |
| Business function isolation | Sample STP-BUS function uses ports/adapters and does not parse transport, write DB/Kafka/audit directly, call AI provider, or own framework concerns. | ArchUnit report and unit tests. |
| Configuration governance | Runtime definitions, parameters, feature flags, and toggle values are versioned, classified, promoted through CI, and safe-disabled. | Config diff, validation, rollback/safe-disable plan. |
| Traceability | Widget action -> API -> policy -> MicroFunction -> audit/outbox/evidence must be reconstructable with trace_id/request_id/evidence_ref. | Trace reconstruction report. |

# 11. API, Eventing, Database, and Contract Foundation
| Contract / Data Area | Sprint 0 Baseline | Gate |
| --- | --- | --- |
| OpenAPI | Initial REST contract skeleton, error model, auth scheme, correlation headers, idempotency headers, pagination pattern, generated client placeholder. | OpenAPI lint and contract test. |
| AsyncAPI | Initial event/topic contract skeleton for audit/event/outbox/replay signals with CloudEvents metadata. | AsyncAPI lint and consumer/producer stub test. |
| Kafka / Eventing | Local profile or testcontainer; topic naming; Avro/JSON schema; schema registry placeholder; retry/DLQ topics; replay request model. | Event contract and message roundtrip test. |
| CloudEvents | Standard attributes include id, source, type, specversion, subject, time, datacontenttype, trace_id, correlation_id, causation_id, classification. | CloudEvents validation sample. |
| Schema evolution | Compatibility rules, versioning policy, deprecation path, migration owner, consumer impact evidence. | Schema compatibility report. |
| Outbox / Inbox | Transactional outbox for event emission; inbox/deduplication for consumers; idempotency keys and replay-safe handlers. | Duplicate/replay test and DB records. |
| Flyway | All schema, seed, RLS, indexes, extension, audit, idempotency, outbox, inbox, DLQ/replay tables created through Flyway. | Clean/upgrade migration report. |
| Data truth | PostgreSQL is authority; Redis/Valkey accelerates only; caches never become source of truth. | Cache invalidation and rebuild test. |

# 12. Observability, Runtime Toggles, and Evidence Correlation
| Observability Control | Sprint 0 Requirement | Evidence |
| --- | --- | --- |
| Log4j2 structured logging | JSON-safe logs with trace_id, span_id, request_id, actor hash, component, classification, and safe error code. No secrets or raw PII. | Log sample and forbidden-field test. |
| OpenTelemetry | Frontend, gateway, backend API, MicroFunction runtime, policy, database, Kafka, and AI gateway spans where applicable. | Trace in Tempo or equivalent. |
| Sentry / error monitoring | Safe error monitoring for frontend/backend exceptions without raw tokens, PII, secrets, or unrestricted payloads. | Synthetic error event and redaction proof. |
| Loki / Tempo / Grafana | Starter dashboards for build health, API latency, policy denials, MicroFunction execution, outbox/DLQ, cache behavior, and evidence completeness. | Dashboard screenshot or JSON export. |
| Runtime toggles | Diagnostic logging, trace sampling, widget telemetry, AI panel diagnostics, and heavy debug mode must be change-controlled, audited, role-restricted, time-bound, and safe-default. | Toggle registry, policy, audit event, rollback test. |
| Audit and evidence | Critical actions produce append-only audit and evidence_ref linked to PR/MR, runtime trace, policy decision, and test evidence. | Evidence record sample. |
| Trace reconstruction | Sample transaction can reconstruct who did what, when, through which policy, with which input class, and what result. | Trace reconstruction report. |
| Performance-Safe Toggle Rule Runtime logging and telemetry may be adjusted for performance only through approved configuration, RBAC/SBAC/OPA policy, audit, rollback, and expiration controls. A toggle must not disable security audit, policy decisions, evidence capture, or incident-relevant telemetry for protected actions. |
| --- |

# 13. Security, OPA/SBAC, Secrets Hygiene, Abuse Cases, and Authenticated DAST
| Security Area | Sprint 0 Requirement | Blocker Condition |
| --- | --- | --- |
| OPA/SBAC skeleton | Create baseline policies for developer, reviewer, admin, agent, CI service, tool action, and workspace capability decisions. | Protected action allowed without policy decision. |
| Secrets hygiene | No secrets in .env, code, tests, prompts, screenshots, logs, Obsidian, GitNexus output, CI artifacts, or LLM context. Use approved secret references only. | Secret found in repository or evidence. |
| Abuse cases | Create starter abuse-case catalog for login, API abuse, replay, privilege escalation, prompt injection, RAG poisoning, tool misuse, DLQ replay misuse, and workspace policy bypass. | High-risk flow without abuse case. |
| Authenticated DAST readiness | Prepare non-prod authenticated DAST scope with synthetic users, test tenant, no destructive scans, rate limits, safe exclusions, and remediation evidence path. | DAST attempts against production or real customer data. |
| Secure APIs | Authentication, authorization, validation, rate limiting, error safe-response, idempotency, correlation, and classification controls are included in contract baseline. | API accepts protected request without identity/policy/correlation. |
| Classification handling | Public/Internal/Confidential/Restricted handling rules apply to code, data, evidence, prompts, logs, screenshots, telemetry, and retrieval. | Restricted data exposed to unapproved tool/model/index. |
| Fail-closed controls | If identity, policy, secrets, guardrail, audit, or evidence systems are unavailable, protected actions stop or route to human approval. | Protected path fails open. |

# 14. Concurrency, Heavy Transaction, Idempotency, Outbox, and Resilience Lab
| Resilience Capability | Sprint 0 Setup | Acceptance Test |
| --- | --- | --- |
| Idempotency registry | Create request/action idempotency table and API profile for retries, callbacks, replays, widget actions, and tool actions. | Duplicate request produces single business effect. |
| Transactional outbox | Store event atomically with business/audit action and publish asynchronously. | DB commit without event loss; publisher retry test. |
| Inbox / consumer dedup | Consumer records event IDs and processing status to avoid duplicate effects. | Duplicate message replay is safe. |
| Retry / DLQ / replay | Retry policies, DLQ topics/tables, replay request workflow, classification, approval, and audit. | Poison message goes to DLQ; replay requires approval and evidence. |
| Concurrency testing | Simulate concurrent updates, duplicate callbacks, rapid widget actions, lock contention, and optimistic locking. | No double-approval, double-event, or lost update. |
| Heavy-load test profile | Create synthetic load profile for sample transaction, workspace load, API calls, Kafka events, and DB contention. | Baseline latency/error report and tuning backlog. |
| Failure injection | Simulate OPA unavailable, DB timeout, Kafka unavailable, cache stale, AI gateway unavailable, and telemetry exporter failure. | Fail-safe or degraded-safe behavior documented. |
| Compensation and rollback | Define forward-fix, compensation, feature flag safe-disable, migration rollback strategy, and rebuild path. | Rollback/compensation dry-run evidence. |

# 15. System Builder Lite, Codex, Agent Sandbox, and AI Governance
| AI Governance Element | Sprint 0 Requirement | Evidence |
| --- | --- | --- |
| System Builder Lite boundary | Use ChatGPT/Codex to analyze, draft, generate candidates, propose tests, and prepare PR/MR evidence only. No autonomous approval, merge, deploy, or production mutation. | AGENTS.md, prompt logs, AI-use declaration. |
| Logical agents | Define architecture, developer, security, test, documentation, evidence, CI/CD, and knowledge agents as logical roles with purpose, owner, scope, prohibited actions, and reviewer gates. | Agent catalog draft and RACI. |
| Tool registry | Document allowed tools, risk tier, environment scope, data class, action type, dry-run, idempotency, rollback, and human approval requirement. | Tool registry and policy tests. |
| Model routing | Application/model traffic must route through LiteLLM or approved private/on-prem gateway when implemented. No direct provider SDK calls from app code. | Architecture fitness test for direct SDK imports. |
| Guardrails | Input, retrieval, execution, and output guardrail checkpoints are defined for prompt standards, RAG, tool calls, and evidence output. | Guardrail placeholder tests. |
| Trust and autonomy | Sprint 0 permits T0 advisory, T1 read-only approved-source analysis, and T2 candidate generation in branches/sandboxes. T3+ actions require explicit approval path. | Autonomy risk assessment and approval record. |

# 16. Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop
| Loop Stage | Sprint 0 Control | Required Evidence |
| --- | --- | --- |
| Signal detection | Receive issue from CI failure, test failure, security scan, observability signal, GitNexus drift, or reviewer finding. | Signal ID, source, severity, trace/commit reference. |
| Evidence retrieval | Retrieve only approved evidence by classification, source authority, freshness, and SBAC scope. | Retrieval log, evidence refs, classification decision. |
| Candidate analysis | AI or agent may summarize cause, affected files, affected tests/contracts, risk, and options. | Analysis summary with confidence and limitations. |
| Candidate fix / learning | Generate draft PR, test addition, runbook update, knowledge candidate, policy proposal, or backlog item. | Draft artifact in branch/sandbox; no direct main/production mutation. |
| Validation | Run deterministic tests, scans, policy checks, contract checks, GitNexus impact, and architecture fitness. | Validation evidence and remaining risks. |
| Human approval | Named maker-checker approval before merge, knowledge promotion, policy activation, or environment change. | Approval record and PR/MR AVCI summary. |
| Improvement capture | Approved learning becomes curated Obsidian/LLM Wiki candidate; rejected proposals retain reason and remediation backlog. | Knowledge review record and backlog link. |
| No Self-Healing Production Mutation Auto-Heal may detect, analyze, propose, test, and prepare a draft remediation. It must not merge, deploy, alter production configuration, rotate production secrets, approve access, or update authoritative knowledge without governed human approval and evidence. |
| --- |

# 17. Foundation Technical Build Details
| Recommended repository baseline: /aira-root /apps /api-gateway /dynamic-workspace-web /admin-governance-web /services /microfunction-runtime /identity-access-service /evidence-service /workflow-adapter-service /integration-event-service /libs /domain-kernel /application-ports /adapter-contracts /test-fixtures /contracts /openapi /asyncapi /schemas-avro /schemas-json /cloudevents /db /flyway /seeds /rls /policies /opa /conftest /sbac /observability /otel /log4j2 /grafana /sentry /devsecops /github-actions-or-gitlab-ci /evidence-pack /sbom-provenance /gitnexus /docs /adr /tdl /runbooks /evidence-summaries |
| --- |
| Artifact | Minimum Required Content |
| --- | --- |
| Sample transaction | One safe transaction that exercises correlation, identity, policy, validation, idempotency, STP-BUS, audit, outbox, observability, safe response, and evidence. |
| Sample workspace | One role-filtered workspace screen with backend-resolved components, generated API client, policy-denied component test, and safe error state. |
| Sample event | One CloudEvents-compliant outbox event with schema version, trace_id, correlation_id, causation_id, classification, and replay-safe consumer. |
| Sample evidence pack | One PR/MR evidence pack linking issue, commit, AI-use declaration, tests, scans, GitNexus report, SBOM, policy decisions, and approval. |
| Sample resilience run | One controlled test proving duplicate-safe behavior and DLQ/replay request governance. |

# 18. Risks, Dependencies, Assumptions, and Decisions
| Risk / Dependency | Severity | Required Treatment |
| --- | --- | --- |
| Developers start business features before gates pass. | High | Block merge of business-feature PRs until Ready-to-Code and Foundation Exit evidence are approved. |
| Toolchain drift across developer workstations. | High | Use devcontainer, version pinning, tool report, rebuild test, and drift dashboard. |
| AI assistant weakens architecture or security through generated code. | High | Enforce AGENTS.md, architecture fitness, direct provider/import checks, OPA/SBAC, and human review. |
| Observability overhead affects local performance. | Medium | Use governed runtime toggles and sampling controls without disabling audit/security evidence. |
| Kafka/Temporal/Flowable/Keycloak setup complexity delays Sprint 0. | Medium | Use local profiles or stubs where allowed, but retain contracts, adapters, tests, and future integration evidence. |
| Source numbering conflicts remain. | Medium | Track 11A duplicate numbering, 41B/44 overlap, 01A placement, and older superseded references in AVCI reconciliation register. |
| Security scans create false positives and slow delivery. | Medium | Tune rules through reviewed policy-as-code; do not disable critical gates silently. |
| Knowledge projection duplicates source of truth. | Medium | Keep Git/OpenKM/Tier-0 as authority; Obsidian/LLM Wiki curated and derivative with provenance. |

# 19. RACI and Separation of Duties
| Activity | IT Head / SAO | DevSecOps | System Admin | Security | Development | QA/SDET | DBA | AI Governance | Internal Audit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Approve Sprint 0 plan | A | C | C | C | C | C | C | C | I |
| Repository bootstrap | C | A/R | I | C | R | C | I | C | I |
| Workstation cohort setup | I | C | A/R | C | R | C | I | C | I |
| CI/CD evidence pipeline | C | A/R | C | C | R | R | C | C | I |
| Security/OPA/SBAC baseline | C | C | C | A/R | R | R | C | C | I |
| Flyway/database baseline | C | C | I | C | R | C | A/R | I | I |
| MicroFunction runtime skeleton | C | C | I | C | A/R | R | C | C | I |
| Dynamic Workspace shell | C | C | I | C | A/R | R | C | C | I |
| Agent sandbox and System Builder Lite | A | C | I | C | R | C | I | A/R | I |
| Sprint 0 closeout acceptance | A | R | C | C | R | R | C | C | C |
| Separation of Duties Rule The maker of a foundation artifact must not be the sole checker or approver of that artifact. High-risk security, database, policy, agent, CI/CD, and production-readiness decisions require independent review and evidence. |
| --- |

# 20. Sprint 0 Closeout and Handoff to Sprint 1
| Closeout Item | Required Content | Recipient |
| --- | --- | --- |
| Sprint 0 Closeout Report | Completed workstreams, gates passed, waivers, risks, known limitations, evidence links, and recommended Sprint 1 scope. | Architecture Board / CAB |
| Foundation Evidence Pack | Repository, pipeline, tests, scans, GitNexus, SBOM, API/event, Flyway, security, observability, resilience, and approval evidence. | DevSecOps / Audit |
| Sprint 1 Readiness Backlog | Only items meeting Definition of Ready: owner, classification, acceptance criteria, contracts, tests, evidence path, dependencies, and risk tier. | Product Owner / Dev Lead |
| Runbook Starter Pack | Local run, rebuild, troubleshooting, rollback, evidence rebuild, DLQ/replay request, policy deny handling, agent suspension. | SRE / Operations |
| Knowledge Projection | Curated Obsidian summaries and LLM Wiki candidates with source references, freshness, classification, and review status. | Knowledge Governance |
| Improvement Backlog | Open gaps, toolchain improvements, test gaps, architecture fitness improvements, security findings, and Auto-Improve candidates. | PMO / SAO |

# 21. Acceptance Criteria and Definition of Done
| Category | Sprint 0 Definition of Done |
| --- | --- |
| Governance | Document register and reconciliation items updated; RACI assigned; source baseline known; waivers recorded with owner, expiry, risk, and compensation. |
| Repository | Protected repository exists with branch rules, CODEOWNERS, templates, AGENTS.md/CLAUDE.md, issue board, labels, and evidence path. |
| Developer readiness | Every developer in scope has attested workstation, devcontainer/local setup, AI usage acknowledgement, and local validation evidence. |
| Pipeline | Sample PR passes build, tests, scans, policy, architecture, contract, migration, GitNexus, SBOM/provenance, and evidence finalization gates. |
| MicroFunction | Sample transaction executes mandatory controls and produces trace, audit, outbox, policy, idempotency, error, and evidence records. |
| Dynamic Workspace | Sample backend-governed workspace resolves, filters, renders, calls approved API/MicroFunction, emits telemetry, and denies unauthorized component/action safely. |
| API/event/database | OpenAPI/AsyncAPI/schema/Flyway/outbox/DLQ/replay/idempotent consumer baseline validates and has compatibility/replay evidence. |
| Security | OPA/SBAC tests, abuse-case catalog, secrets hygiene, fail-closed tests, authenticated DAST scope, and remediation evidence path are complete. |
| Observability | Log4j2, OTel, Sentry, Loki, Tempo, Grafana profile and runtime toggles are represented; sample trace reconstruction succeeds. |
| Resilience | Duplicate-safe, retry-safe, concurrent, heavy-load, failure-aware tests execute and produce a resilience lab report. |
| AI governance | System Builder Lite, Codex, logical agents, tool registry, guardrail/model-route placeholders, and progressive autonomy limits are active. |
| Closeout | Sprint 0 closeout report approved; Sprint 1 backlog is ready; risks and improvement items are owned. |

# 22. Open Issues and AVCI Reconciliation Items
| Item | Issue | Recommended Handling |
| --- | --- | --- |
| RI-001 | 11A duplicate numbering exists across development readiness and DevSecOps governance variants. | Track in 00D/register; do not silently renumber in Sprint 0 artifacts without register approval. |
| RI-002 | 41B / 44 System Builder overlap remains visible in source packs. | Treat as System Builder governance consolidation item; cite controlling source by title until register is cleaned. |
| RI-003 | 01A v1.1/other 01A variant placement and references require canonical register confirmation. | Use active canonical enterprise design principles as governing source; record any conflict. |
| RI-004 | Older references to v3/v4/v5 standards remain in source content. | Apply latest active baseline in document control while preserving provenance. |
| RI-005 | Full packer/regeneration runbook remains future work. | Create backlog item after key foundation documents are aligned. |
| RI-006 | Runtime observability toggle thresholds require operational tuning after sample load tests. | Keep default safe values; tune only through evidence-backed change request. |

# 23. AVCI Compliance Summary
| AVCI Property | Sprint 0 Evidence |
| --- | --- |
| Attributable | Document control identifies owner, co-owners, source baseline, companion standards, workstream owners, RACI, PR/MR ownership, AI usage, and evidence path. |
| Verifiable | Readiness gates require local+CI evidence, tests, scans, policy decisions, contract validation, Flyway reports, GitNexus impact, SBOM/provenance, observability traces, resilience lab, and closeout report. |
| Classifiable | All artifacts, evidence, telemetry, prompts, logs, screenshots, contracts, database records, workspace components, and AI outputs carry classification and handling rules. |
| Improvable | Risks, defects, scan findings, architecture drift, recurring failures, test gaps, knowledge candidates, and rejected AI proposals become owned backlog items with review cadence and revision path. |

# Appendix A. Sprint 0 GitHub Issue Template
| Title: [S0-Wx] <short workstream task title> Type: Epic \| Story \| Task \| Security \| Test \| Evidence \| Waiver \| Defect Owner: Checker: Workstream: Classification: Public \| Internal \| Confidential \| Restricted Affected bounded context / capability: Companion standards: Acceptance criteria: Required tests: Required evidence: Security / OPA / SBAC impact: API / event / database impact: Dynamic Workspace / MicroFunction impact: Observability / resilience impact: Rollback / forward-fix / safe-disable path: AI assistance used: none \| ChatGPT \| Codex \| other approved tool Human approval required: yes/no Links: ADR/TDL \| PR/MR \| CI run \| evidence pack \| GitNexus report |
| --- |

# Appendix B. Sprint 0 Evidence Record Template
| evidence_id: workstream_id: artifact_type: owner: checker: source_ref: branch: commit_sha: classification: verification_evidence: tests: scans: policy_decisions: contract_validation: migration_validation: gitnexus_report: sbom_provenance: observability_trace: resilience_result: approval_ref: known_limitations: rollback_or_rebuild_path: improvement_backlog_ref: retention_path: |
| --- |

# Appendix C. Ready-to-Code Sign-Off Checklist
| Checklist Item | Pass Condition | Owner |
| --- | --- | --- |
| Workstation ready | Attested device, approved tools, VS Code/Codex configured, local hooks active. | System Administrator / Developer |
| Repository ready | Branch protection, CODEOWNERS, templates, AGENTS.md/CLAUDE.md, labels, and issue board active. | DevSecOps |
| CI ready | Sample PR passes strict mode and stores evidence. | DevSecOps / QA |
| Security ready | OPA/SBAC, secrets hygiene, abuse cases, and authenticated DAST scope ready. | Security |
| Architecture ready | Package boundaries, ports/adapters, MicroFunction rules, Dynamic Workspace boundaries, and direct-provider/DB checks active. | Solutions Architect |
| Data/API/event ready | OpenAPI/AsyncAPI/Flyway/outbox/DLQ/replay/idempotency baseline validates. | API Architect / DBA |
| Observability ready | Trace/log/metric/audit/evidence sample reconstructs sample transaction. | SRE / DevSecOps |
| AI governance ready | System Builder Lite and logical agent boundaries acknowledged; no shadow AI; human approval path active. | AI Governance |
| Closeout ready | Sprint 1 approved. | IT Head / PMO |

