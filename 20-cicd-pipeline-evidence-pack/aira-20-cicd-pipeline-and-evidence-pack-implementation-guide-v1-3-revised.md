---
title: "CICD Pipeline and Evidence Pack Implementation Guide"
doc_id: "AIRA-20"
version: "v1.3"
status: "revised"
category: "CI/CD pipeline and evidence pack"
source_docx: "AIRA_20_CICD_Pipeline_and_Evidence_Pack_Implementation_Guide_v1.3_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 20-cicd-pipeline-evidence-pack
  - revised
  - aira-20
---



# CICD Pipeline and Evidence Pack Implementation Guide



AIRA
AI-Native Enterprise Platform

AIRA CI/CD Pipeline and Evidence Pack Implementation Guide
v1.3 Revised

Gated Delivery | Evidence by Construction | GitNexus | System Builder | Dynamic Workspace | MicroFunction Runtime | PRR/ORR | Resilience Lab
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-020 |
| Canonical Filename | AIRA_20_CICD_Pipeline_and_Evidence_Pack_Implementation_Guide_v1.3_Revised.docx |
| Version | v1.3 - Executable Governance, PRR/ORR, Resilience Lab, Evidence Manifest, MicroFunction, Dynamic Workspace, Security, Supply Chain, and Auto-Improve Alignment Update |
| Source Document Reviewed | AIRA_20_CICD_Pipeline_and_Evidence_Pack_Implementation_Guide_v1.2_Revised.docx |
| Supersedes | AIRA-DOC-020 v1.2 Revised, upon ARB/CAB/team approval |
| Status | Draft for Architecture, DevSecOps, Security, Platform Engineering, QA/SDET, DBA, SRE, AI Governance, Knowledge Governance, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; DevSecOps Lead; Software Development Lead; Security Architecture; Platform Engineering; QA/SDET; DBA; SRE / Operations; AI Governance; Knowledge Governance; Internal Audit |
| Primary Parents | 11 v3.3 Revised; 11A v1.3 Revised; 62 v1.0; 63 v1.0; 64 v1.0; 10 v3.4; 10A v2.4; 10B v2.3; 10C v2.3; 10D v2.3; 10E v1.3 |
| Companion Sources | 01/01A/01B; 02; 03; 04; 07/07B; 08/08A; 09; 12A/41/46-61 Dynamic Workspace; 15/15A API; 16/16A/16B Flyway and Database; 17/17A Security; 19 GitNexus; 21A/21B Knowledge; 22A Prompt/Guardrail/Model Registry; 30/30A Change; 31/31A Observability; 42 series AI Governance; 43 Continuous Improvement |
| Review Cadence | Every Sprint 0 / PoC / release gate; weekly during foundation build; quarterly after stabilization; unscheduled on material CI/CD, DevSecOps, AI, repository, security, database, Dynamic Workspace, MicroFunction, API/event, resilience, PRR/ORR, or evidence-model change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / CICD-Evidence-Pack / 20 / v1.3 / |
| Mandatory Practice Statement No AIRA repository, MicroFunction, Dynamic Workspace component, API/event contract, database migration, prompt, guardrail, agent manifest, infrastructure manifest, documentation artifact, runtime configuration, or release candidate is promotion-ready merely because it builds or appears to work. It is promotion-ready only when the pipeline produces AVCI-complete evidence for tests, security, policy, architecture, supply chain, GitNexus impact, observability, resilience, PRR/ORR readiness, rollback, approvals, and improvement backlog. Required gates fail closed. AI assistants and agents may draft, analyze, test, and recommend, but must not approve, merge, deploy, suppress findings, weaken gates, or mutate production. |
| --- |

# Static Table of Contents

1. Executive Summary and v1.3 Upgrade Verdict

2. Purpose, Scope, and Authority

3. v1.3 Change Summary

4. CI/CD Governance Principles

5. Target Pipeline Architecture and Stage Model

6. Mandatory Quality, Security, Policy, and Architecture Gates

7. Evidence Pack Architecture, Manifest, and Retention

8. GitNexus and Derived Artifact Governance

9. Dynamic Workspace and MicroFunction Pipeline Gates

10. API, Eventing, Database, and Schema Evolution Gates

11. Observability, Audit, and Runtime Toggle Evidence

12. Concurrency, Heavy Transaction, and Resilience Lab Gates

13. Production and Operational Readiness Gates

14. AI-Assisted Development, Agents, and Auto-Improve Candidate Loops

15. Environment Promotion, Release Governance, and Rollback

16. Copy-Ready Pipeline Skeletons

17. PR/MR AVCI Evidence Summary Template

18. RACI and Separation of Duties

19. Implementation Roadmap and Acceptance Criteria

20. Open Reconciliation Items and Backlog

21. AVCI Compliance Summary

# 1. Executive Summary and v1.3 Upgrade Verdict

This v1.3 revision updates AIRA-DOC-020 from the v1.2 CI/CD evidence-pack implementation guide into the executable governance backbone for AIRA delivery. The guide now explicitly integrates the revised parent DevSecOps controls, the completed MicroFunction family, AIRA-DOC-062 executable governance roadmap, AIRA-DOC-063 production and operational readiness gates, and AIRA-DOC-064 resilience lab requirements.

The standard is intentionally implementation-oriented. It defines the gates, evidence folders, manifest fields, pipeline skeletons, review responsibilities, readiness checks, and rejection rules that make AIRA standards enforceable by CI/CD rather than merely described in Word documents.
| Upgrade Area | v1.3 Required Result | Verdict |
| --- | --- | --- |
| Executable governance | Convert document controls into CI/CD gates, manifest validation, policy-as-code, architecture fitness, and release evidence. | Strengthened |
| PRR/ORR integration | Production and operational readiness must be a promotion gate, not a post-release checklist. | Added |
| Resilience Lab | Performance, concurrency, idempotency, outbox/DLQ/replay, recovery, and chaos evidence become gated artifacts. | Added |
| Evidence manifest | Standardize machine-readable evidence metadata, hashes, classification, retention, owners, gate results, waivers, and runtime references. | Strengthened |
| MicroFunction and Dynamic Workspace | Maintain explicit gates for runtime configuration, backend authority, policy filtering, frontend evidence, and safe actions. | Retained and aligned |
| AI/System Builder | Keep AI and System Builder outputs draft/advisory unless promoted through PR/MR, CI/CD, maker-checker, and evidence. | Retained and hardened |

# 2. Purpose, Scope, and Authority

## 2.1 Purpose

- Define the standard CI/CD and evidence-pack implementation model for all AIRA repositories and promotion paths.

- Convert DevSecOps, MicroFunction, Dynamic Workspace, API/eventing, database, security, observability, PRR/ORR, and resilience requirements into executable delivery gates.

- Ensure every code, configuration, policy, database, prompt, guardrail, AI agent, runtime configuration, and infrastructure change is controlled through reviewable evidence.

- Provide copy-ready pipeline structures, evidence manifests, PR/MR templates, and acceptance criteria that teams can adopt without weakening enterprise controls.

## 2.2 Scope and Authority
| Scope Area | Required Treatment |
| --- | --- |
| In Scope | Backend services, frontend/Dynamic Workspace, MicroFunction runtime, API/event contracts, Flyway migrations, OPA/Rego, prompts, guardrails, model route aliases, agent manifests, devcontainers, IaC, documentation, evidence summaries, GitNexus outputs, PRR/ORR evidence, resilience lab outputs, and release artifacts. |
| Out of Scope | Direct production mutation, unmanaged deployment scripts, manual DDL, unreviewed AI-generated changes, bypassing CODEOWNERS, bypassing security gates, storing full source code or secrets in Obsidian, or letting GitNexus/AI tools become authority. |
| Authority | This guide implements but does not override AIRA AVCI, Enterprise Design Principles, Engineering Blueprint, Developer Guide, Technology Stack, DevSecOps, Security, Database/Flyway, API Contract, GitNexus, Dynamic Workspace, MicroFunction, Change/CAB, PRR/ORR, and Resilience Lab standards. |
| Conflict Rule | When documents conflict, apply the stricter control, create an AVCI reconciliation item, assign an owner, and do not silently normalize source numbering or authority gaps. |

# 3. v1.3 Change Summary
| Change Area | v1.3 Improvement |
| --- | --- |
| Parent alignment | Updates parent references to 11 v3.3, 11A v1.3, 62 v1.0, 63 v1.0, 64 v1.0, and the completed MicroFunction revised set. |
| Pipeline stage model | Adds PRR/ORR and Resilience Lab stages as explicit promotion gates. |
| Evidence manifest | Defines minimum manifest schema and retention rules for machine-readable evidence validation. |
| Dynamic Workspace | Retains component registry, accessibility, policy-filtered workspace resolver, generated client, telemetry, and backend MicroFunction action checks. |
| MicroFunction | Retains standard step evidence, runtime parameter validation, idempotency profile, outbox/inbox, audit, retry, DLQ, replay, and rollback checks. |
| Security and supply chain | Strengthens authenticated DAST, abuse cases, OPA/SBAC, secrets hygiene, SBOM/provenance, artifact digest, and remediation evidence gating. |
| AI and agents | Clarifies that Auto-Heal/Learn/Improve and System Builder outputs are candidate-only until reviewed, tested, approved, and promoted. |

# 4. CI/CD Governance Principles
| ID | Principle | Implementation Meaning |
| --- | --- | --- |
| CICD-01 | Git is source of truth | Pipeline, policy, prompts, guardrails, migrations, contracts, IaC, and documentation changes originate from reviewed Git changes. |
| CICD-02 | Evidence before promotion | No promotion without complete evidence pack, manifest hash, retained reports, and PR/MR AVCI summary. |
| CICD-03 | Fail safe, not fail open | If scanner, signer, policy engine, evidence store, OPA, identity, guardrail, or required test is unavailable, protected gates fail. |
| CICD-04 | Least privilege and SoD | Developers, agents, tools, runners, and deployers receive scoped permissions; maker, checker, approver, and deployer are separable. |
| CICD-05 | Contract before implementation | OpenAPI, AsyncAPI, schema, policy, workflow, and MicroFunction contracts are validated before implementation is trusted. |
| CICD-06 | Reproducibility | Build images, toolchains, dependency locks, Java, Node, Gradle/Maven/npm/pnpm versions, and generated artifacts are pinned. |
| CICD-07 | Observability by design | Builds, tests, deployments, and smoke checks emit trace/build/evidence identifiers and redacted telemetry. |
| CICD-08 | AI is not authority | AI assistants, System Builder, Codex, Hermes, GitNexus, and agents may propose and draft only; humans approve material changes. |

# 5. Target Pipeline Architecture and Stage Model
| Target Control Flow Requirement or evidence intake -> branch and CODEOWNERS -> pre-commit and local checks -> CI build/test/security/contract/policy/architecture gates -> GitNexus read-only impact -> evidence manifest -> PR/MR AVCI review -> Resilience Lab where required -> PRR/ORR -> environment approval -> deploy or release candidate -> smoke/DAST/observability verification -> evidence retention -> improvement backlog. |
| --- |
| Stage | Required Evidence | Blocking Decision |
| --- | --- | --- |
| 0 Intake and Classification | Ticket/intake_id, owner, source, risk tier, data classification, bounded context, environment target, AI-use eligibility. | Blocks missing owner, classification, or scope. |
| 1 Preflight | Branch policy, CODEOWNERS, commit signing where adopted, secret scan, dependency lock, changed-file classification. | Blocks unauthorized branch, secrets, or forbidden file path. |
| 2 Build and Static Quality | Java/Spring, frontend build, lint, format, type check, dependency checks. | Blocks build errors, unmanaged dependency drift, runtime downgrade. |
| 3 Tests | Unit, component, policy fixtures, deterministic data, integration and regression as applicable. | Blocks failed or missing required tests. |
| 4 Contract and Compatibility | OpenAPI/AsyncAPI diff, generated client validation, schema compatibility, CloudEvents validation. | Blocks breaking contracts without versioning and migration plan. |
| 5 Database and Migration | Flyway validate/migrate/clean-test in non-prod, checksum, rollback/forward-fix, RLS/view/index evidence. | Blocks manual DDL and destructive migration without approval. |
| 6 Security and Policy | SAST, SCA, secret scan, container/IaC scan, OPA/Rego, Conftest, authenticated DAST where applicable. | Critical/High block unless formally waived. |
| 7 Architecture Fitness | ArchUnit/Semgrep/dependency rules; MicroFunction, Dynamic Workspace, ports/adapters, direct-provider-call checks. | Blocks architecture drift and authority bypass. |
| 8 Resilience Lab | Outbox/inbox, idempotency, DLQ/replay, concurrency, load, failure injection, recovery evidence. | Blocks unproven retry/replay/concurrency behavior for critical flows. |
| 9 Supply Chain | SBOM, provenance, artifact digest, signature where supported, license report, image scan. | Blocks unverifiable artifact lineage or unacceptable risk. |
| 10 GitNexus and Evidence | Read-only code map, impact analysis, affected-test map, drift report, derived artifact summaries. | Blocks incomplete PR/MR evidence when required. |
| 11 PRR/ORR and Promotion | Release readiness, SLO/runbook/dashboard, rollback, approvals, post-deploy verification, evidence retention. | Blocks deployment without named approval and rollback proof. |

# 6. Mandatory Quality, Security, Policy, and Architecture Gates
| Gate | Minimum Evidence | Owner | Decision |
| --- | --- | --- | --- |
| Build Gate | Backend, frontend, contracts, migrations, and docs build from pinned toolchains. | DevSecOps | Block |
| Test Gate | Unit, component, contract, OPA, architecture, frontend, e2e, regression, and mutation where required. | QA/SDET | Block |
| Security Gate | SAST, SCA, secret scan, container/IaC scan, authenticated DAST where applicable, remediation evidence. | Security | Block Critical/High |
| Policy Gate | OPA/Rego and Conftest checks for access, classification, deployment, runtime toggles, AI use, environments. | Security / DevSecOps | Block |
| Architecture Gate | ArchUnit/Semgrep rules for SOLID, Clean Architecture, DDD, ports/adapters, MicroFunction and Dynamic Workspace boundaries. | Enterprise Architecture | Block |
| Supply Chain Gate | SBOM, provenance, artifact digest, signature where supported, dependency lock, image digest, license report. | DevSecOps | Block material gaps |
| Evidence Gate | Evidence manifest, PR/MR AVCI summary, GitNexus outputs, derived artifacts, approvals, rollback/forward-fix. | DevSecOps / Audit | Block |

# 7. Evidence Pack Architecture, Manifest, and Retention
| Evidence Pack Rule Evidence must be produced by the pipeline, linked to commit SHA, build ID, branch, ticket, owner, classification, environment, tool versions, report hashes, and retained in approved stores. Obsidian receives curated summaries and links only; it must not become a full source-code or secrets repository. |
| --- |
| Folder | Required Contents |
| --- | --- |
| 00-manifest | evidence-manifest.json, evidence-index.md, classification-record.md, source-register.md |
| 01-build | build-log.txt, toolchain-version.txt, java-version.txt, node-version.txt, artifact-digest.txt |
| 02-tests | unit-report.xml, component-report.xml, contract-report.xml, e2e-report.xml, coverage-summary.json, mutation-report where applicable |
| 03-security | sast-report.json, sca-report.json, secret-scan-report.json, container-scan-report.json, dast-report.json, remediation-evidence.md |
| 04-policy | opa-test-results.json, conftest-results.json, sbac-decision-summary.md, branch-policy-check.md, runtime-toggle-policy-check.md |
| 05-architecture | archunit-report.xml, semgrep-architecture.json, dependency-boundary-report.json, microfunction-fitness-summary.md, dynamic-workspace-fitness-summary.md |
| 06-contracts | openapi-diff.json, asyncapi-diff.json, schema-compatibility.json, cloudevents-validation.json, generated-client-validation.md |
| 07-database | flyway-info.txt, flyway-validate.txt, clean-migrate-test.txt, migration-risk.md, rollback-forward-fix-plan.md |
| 08-events-resilience | outbox-inbox-test.json, idempotency-test.json, dlq-replay-test.json, concurrency-test.json, failure-injection-summary.md |
| 09-gitnexus | code-map.json, impact-summary.md, affected-tests.json, security-sensitive-map.md, architecture-drift.md |
| 10-supply-chain | sbom.cdx.json, provenance-attestation.json, license-report.json, image-scan.json, artifact-signature.txt |
| 11-observability | otel-correlation-summary.md, log4j2-redaction-test.json, sentry-test.md, loki-tempo-grafana-dashboard-links.md, trace-reconstruction.md |
| 12-readiness | prr-checklist.md, orr-checklist.md, slo-dashboard.md, runbook.md, rollback-drill.md |
| 13-approvals | code-review.md, qa-review.md, security-review.md, devsecops-review.md, dba-review.md, waiver-records.md, cab-approval.md where required |

## 7.1 Minimum Evidence Manifest Schema

{

"evidence_pack_id": "AIRA-EP-<repo>-<build>-<date>",

"classification": "INTERNAL CONFIDENTIAL",

"owner": "<named owner>",

"source_refs": ["ticket", "branch", "commit_sha", "adr_or_tdl"],

"change_type": ["code", "microfunction", "api", "event", "database", "workspace", "agent", "environment"],

"gate_results": {

"build": "pass|fail|waived", "tests": "pass|fail|waived", "security": "pass|fail|waived",

"policy": "pass|fail|waived", "architecture": "pass|fail|waived", "supply_chain": "pass|fail|waived",

"resilience_lab": "pass|not_applicable|fail", "prr_orr": "pass|not_applicable|fail"

},

"artifact_hashes": {"sbom": "sha256", "provenance": "sha256", "report_index": "sha256"},

"runtime_refs": {"trace_id": "", "audit_event_id": "", "evidence_ref": ""},

"rollback_refs": ["rollback plan", "safe-disable", "compensation", "restore/rebuild"],

"approvals": ["maker", "checker", "owner", "security", "cab_or_arb_if_required"],

"improvement_backlog_refs": []

}

# 8. GitNexus and Derived Artifact Governance

GitNexus is read-only, derivative, commit-bound code intelligence. It supports affected-test discovery, blast-radius review, architecture drift detection, code maps, PR/MR evidence, and release-readiness summaries. It must not approve, merge, deploy, mutate production, replace tests, replace scans, or become architecture authority.
| GitNexus Output | Pipeline Use | Required Control |
| --- | --- | --- |
| Code map | Reviewer orientation and architecture traceability | Advisory only; verify against source and tests. |
| Impact summary | Blast-radius assessment for PR/MR | Must be commit-bound and reviewed by human checker. |
| Affected tests | Test selection and reviewer focus | Cannot replace mandated tests for high-risk changes. |
| Security-sensitive map | Security review prioritization | Must not expose secrets or sensitive payloads. |
| Architecture drift | Fitness backlog and gate signal | Blocking only when approved as formal gate; otherwise advisory with owner. |

# 9. Dynamic Workspace and MicroFunction Pipeline Gates
| Change Type | Mandatory CI Evidence | Blocking Defect |
| --- | --- | --- |
| Dynamic Workspace screen/template | Component catalog diff, template version, OPA policy result, accessibility check, generated client check, frontend unit/e2e tests, telemetry event list. | Frontend-only authority, hidden backend bypass, missing policy filtering, accessibility failure, missing telemetry/evidence. |
| Experience Block / Widget | Capability binding, MicroFunction transaction code, idempotency key handling, safe error response, policy decision, frontend telemetry, audit event. | Widget directly mutates business state or bypasses MicroFunction/API contract. |
| MicroFunction transaction | Runtime configuration, standard step sequence, ports/adapters evidence, idempotency profile, audit/outbox, policy, tests, rollback/disable path. | Direct DB/Kafka/model/provider call from business function; missing idempotency or audit. |
| Runtime parameter / feature flag | Config diff, classification, policy, activation/rollback, audit event, safe default, performance impact note. | Ungoverned toggle or debug mode that leaks data or weakens controls. |
| AI Assistant Panel change | Prompt template, model route alias, guardrail result, classification, source citation rule, artifact retention, abuse-case test. | Direct model-provider call, raw Restricted prompt, missing guardrail/evidence route. |

# 10. API, Eventing, Database, and Schema Evolution Gates
| Domain | Gate | Minimum Evidence |
| --- | --- | --- |
| OpenAPI | Contract diff and generated client validation | No breaking API change without versioning, consumer migration, tests, and approval. |
| AsyncAPI | Topic/channel/message compatibility | AsyncAPI diff, consumer impact, topic authorization, replay safety, and evidence links. |
| Kafka | Topic, ACL, producer/consumer, DLQ, retry, replay checks | Topic manifest, consumer group, idempotent consumer test, DLQ/replay runbook, retention policy. |
| Schema Registry | Backward/forward compatibility and schema evolution | Compatibility report, schema version, owner, namespace, consumer list, migration plan. |
| CloudEvents | Envelope validation and correlation | specversion, type, source, id, subject, time, datacontenttype, trace_id, correlation_id, causation_id. |
| Outbox / Inbox | Transactional event publishing and deduplication | Outbox write with business transaction, inbox dedupe key, retry-safe publisher, replay proof. |
| Flyway | Versioned DB migration only | Flyway validate/info, clean-migrate in non-prod, checksum, rollback/forward-fix, DBA review if material. |
| Idempotency | Retry/callback/replay safety | Idempotency key policy, duplicate request test, concurrent execution test, safe response behavior. |

# 11. Observability, Audit, and Runtime Toggle Evidence

Every production-bound change must preserve trace, metric, log, audit, model, agent, evidence, and policy correlation without leaking secrets, raw tokens, raw PII, account numbers, embeddings, or Restricted payloads. Runtime telemetry toggles may tune verbosity, sampling, or expensive diagnostics only through governed configuration, OPA/SBAC approval where required, audit event, safe default, and rollback path.
| Toggle Type | Allowed Use | Required Gate |
| --- | --- | --- |
| Log verbosity | Temporary non-prod or time-bound production diagnostic increase | Owner, duration, classification, redaction check, audit event, auto-revert. |
| Trace sampling | Performance-aware trace coverage tuning | Sampling policy, SLO impact, trace reconstruction requirement, dashboard link. |
| Feature flag | Safe enable/disable of capability | Default-safe value, policy, tests for enabled/disabled states, rollback evidence. |
| AI assistant mode | Enable/disable multimodal prompt, artifact, or route behavior | Model route, guardrail, classification, SBAC, retention, human approval for high risk. |
| Debug diagnostics | Short-lived diagnostics for incident/RCA | No secrets/PII, approved scope, timebox, incident link, removal evidence. |

# 12. Concurrency, Heavy Transaction, and Resilience Lab Gates
| Risk Area | Mandatory Test / Evidence | Acceptance Rule |
| --- | --- | --- |
| Duplicate requests | Idempotency key, replay, and duplicate callback tests | No duplicate business effect, audit, approval, event, or notification. |
| Concurrent mutation | Optimistic/pessimistic lock or serialization test | Lost update and inconsistent state are blocked or safely retried. |
| Heavy transaction | Load/concurrency smoke, timeout, resource, queue, and SLO evidence | No uncontrolled thread, connection, memory, or queue exhaustion. |
| Event replay | DLQ/replay runbook test using synthetic events | Replay is bounded, authorized, auditable, and idempotent. |
| Dependency failure | Timeout, retry, circuit breaker, bulkhead, and fallback tests | Failure is contained; protected actions fail closed. |
| Compensation | Rollback, forward-fix, or compensating action scenario | State-changing workflow has a reversible or recoverable path. |
| Observability under load | Trace/log/metric/audit sample under stress | Evidence can reconstruct failures without sensitive data leakage. |

# 13. Production and Operational Readiness Gates

AIRA-DOC-063 is now treated as a promotion companion to this guide. Production Readiness Review and Operational Readiness Review are required before staging, pilot, production-like, or production activation for material releases, high-risk MicroFunctions, Dynamic Workspace capabilities, AI/tool-action workflows, database changes, externally exposed APIs, and critical event flows.
| Readiness Area | Required Evidence |
| --- | --- |
| Service ownership | Named owner, support team, escalation path, RACI, operational contact, product owner. |
| SLO and monitoring | SLO/SLA, golden signals, dashboards, alerts, error budget posture, on-call response path. |
| Runbooks | Deployment, rollback, incident triage, DLQ/replay, data repair, restore/rebuild, support scripts. |
| Security and compliance | Security gates passed, waivers reviewed, secrets hygiene, classification, audit retention, access review. |
| Operational resilience | Capacity, load, failure injection, backup/restore, DR assumptions, compensation/recovery paths. |
| Release readiness | Evidence pack, CAB/ARB triggers, release notes, known limitations, residual risk, approval record. |

# 14. AI-Assisted Development, Agents, and Auto-Improve Candidate Loops
| AI Boundary Rule AI may assist with code, tests, policies, documentation, impact analysis, RCA, candidate fixes, and evidence summaries. AI output remains draft/advisory until human review, tests, policy checks, security scans, and PR/MR approval are complete. No agent receives direct production credentials or direct Git/CI/CD/Kubernetes/database/model-provider authority outside approved Harness/SBAC/OPA controls. |
| --- |
| Loop | Pipeline Trigger | Permitted Output | Approval Rule |
| --- | --- | --- | --- |
| Auto-Heal Candidate | Failed build/test/scan, incident, SLO burn, runtime error | RCA, affected files, candidate patch branch, tests, rollback plan, PR draft | Human checker and owner approval before merge or execution. |
| Auto-Learn Candidate | Repeated review finding, escaped defect, recurring warning | Reviewed knowledge update, prompt improvement, test gap, runbook update | Knowledge steward and owner approval before retrieval eligibility. |
| Auto-Improve Candidate | Architecture drift, poor test coverage, slow pipeline, reliability gap | Refactoring proposal, pipeline improvement, additional fitness function, backlog item | ADR/TDL or ticket when material; PR evidence required. |
| Agent Tool Request | AI requests CI rerun, GitNexus analysis, ticket creation, non-prod validation | Harness-mediated action request with SBAC/OPA decision and audit | Policy decides; humans approve risk-tiered actions. |

# 15. Environment Promotion, Release Governance, and Rollback
| Environment | Mandatory Evidence | Promotion Authority |
| --- | --- | --- |
| DEV | Automated build/test/security/architecture/evidence pack on PR/MR. | Developer maker and checker review. |
| INT | Integration, contract, eventing, Flyway, resilience, observability smoke, and Dynamic Workspace checks. | DevSecOps, QA/SDET, and Platform review. |
| UAT | Business workflow smoke, secure test data, authenticated DAST where applicable, release notes, known limitations. | Product Owner, QA, Security review. |
| STG | Production-like release candidate, SBOM/provenance/signature, rollback plan, runbook, SLO/dashboard readiness. | Architecture, SRE, Security, DevSecOps approval. |
| PROD | CAB/ARB triggers satisfied, evidence pack retained, deployment approval, post-deploy verification, rollback/forward-fix ready. | CAB/authorized approvers only; AI cannot approve/deploy. |

# 16. Copy-Ready Pipeline Skeletons

## 16.1 GitHub Actions Skeleton

name: aira-ci-evidence-pack

on: [pull_request, workflow_dispatch]

permissions:

contents: read

pull-requests: read

security-events: write

jobs:

aira-ci:

runs-on: ubuntu-latest

steps:

- uses: actions/checkout@v4

- name: Create evidence folders

run: mkdir -p evidence/{00-manifest,01-build,02-tests,03-security,04-policy,05-architecture,06-contracts,07-database,08-events-resilience,09-gitnexus,10-supply-chain,11-observability,12-readiness,13-approvals}

- name: Toolchain evidence

run: |

java -version 2> evidence/01-build/java-version.txt || true

node --version > evidence/01-build/node-version.txt || true

- name: Build and test

run: ./gradlew clean test || ./mvnw test || npm test

- name: Gate placeholders

run: echo "Run SAST/SCA/secrets/OPA/OpenAPI/AsyncAPI/Flyway/ArchUnit/GitNexus/Resilience/PRR-ORR gates here"

- name: Evidence manifest

run: echo '{"avci":"required","status":"draft","classification":"INTERNAL CONFIDENTIAL"}' > evidence/00-manifest/evidence-manifest.json

- uses: actions/upload-artifact@v4

with:

name: aira-evidence-pack

path: evidence

# 17. PR/MR AVCI Evidence Summary Template

## AIRA PR/MR AVCI and Evidence Summary

### Attributable

- Owner:

- Developer / Maker:

- Reviewer / Checker:

- Branch / Commit SHA:

- Ticket / intake_id:

- AI tools or agents used:

- GitNexus index timestamp:

### Verifiable

- Build/test/contract/Flyway results:

- Architecture fitness:

- OPA/SBAC/policy tests:

- Security scans and DAST:

- SBOM/provenance/artifact digest:

- GitNexus evidence:

- Observability and resilience evidence:

- PRR/ORR decision where required:

### Classifiable

- Data classification:

- Secret/PII/token handling:

- Evidence retention path:

- Model/AI route eligibility:

### Improvable

- Known limitations:

- Improvement backlog:

- Auto-Heal / Auto-Learn / Auto-Improve candidates:

- Rollback / forward-fix / compensation path:

# 18. RACI and Separation of Duties
| Activity | IT Head / Architect | DevSecOps | Development | QA/SDET | Security | DBA / Platform | Internal Audit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Define pipeline baseline | A/R | R | C | C | C | C | I |
| Maintain CI templates | A | R | C | C | C | C | I |
| Review architecture gates | A/R | C | C | C | C | C | I |
| Run and review tests | A | C | R | A/R | C | C | I |
| Review security findings | A | C | C | C | A/R | C | I |
| Review DB/Flyway evidence | A | C | C | C | C | A/R | I |
| Review evidence pack | A/R | R | R | R | R | C | C |
| Approve production promotion | A/R | C | C | C | C | C | I |
| Audit evidence retention | C | C | I | I | C | C | A/R |

# 19. Implementation Roadmap and Acceptance Criteria
| Phase | Execution Focus | Exit Evidence |
| --- | --- | --- |
| Phase 0 - Baseline adoption | Add this document, evidence folders, PR/MR template, CODEOWNERS, branch rules, and required checks. | Repository rejects unreviewed changes and produces initial evidence pack. |
| Phase 1 - Build/test/security gates | Enable build, unit, component, SAST, SCA, secret scan, SBOM, and OPA baseline. | Critical/High findings block unless waived. |
| Phase 2 - Contracts/database/eventing | Enable OpenAPI/AsyncAPI diff, schema checks, CloudEvents, Flyway validation, outbox/inbox/idempotency tests. | Breaking changes and manual DDL are blocked. |
| Phase 3 - Architecture/Dynamic/MicroFunction | Enable architecture fitness, MicroFunction and Dynamic Workspace gate checks. | Boundary violations and frontend/backend authority bypass are blocked. |
| Phase 4 - GitNexus/derived evidence | Enable commit-bound GitNexus output and derived artifact summaries. | PR/MR evidence includes code map, impact, affected tests, and release-readiness summary. |
| Phase 5 - Resilience and observability | Enable resilience lab, telemetry, log redaction, trace reconstruction, dashboards, runtime toggle evidence. | Failures are diagnosable, redacted, reproducible, and recoverable. |
| Phase 6 - PRR/ORR and promotion | Enable readiness gates, environment approvals, release gates, rollback evidence, CAB triggers, and post-deploy verification. | STG/PROD promotion requires named human approval and complete evidence pack. |

## 19.1 Minimum Acceptance Criteria

- Every PR/MR contains a completed AVCI and Enterprise Design Principle impact summary.

- Every pipeline run generates a standard evidence pack with manifest, hashes, classification, gate results, and retention path.

- Build, test, security, policy, architecture, contract, Flyway, supply-chain, resilience, readiness, and evidence gates are represented in CI/CD.

- Dynamic Workspace and MicroFunction changes have specific fitness checks and safe rollback/disable evidence.

- API/eventing changes validate OpenAPI, AsyncAPI, schema compatibility, CloudEvents, outbox/inbox, idempotency, DLQ, and replay where applicable.

- Observability evidence proves Log4j2 redaction, OpenTelemetry correlation, Sentry/Loki/Tempo/Grafana readiness, and trace reconstruction for critical paths.

- GitNexus is integrated only as read-only derivative evidence and never as an authority or autonomous action path.

- Auto-Heal, Auto-Learn, and Auto-Improve outputs become candidate PRs, tickets, runbook updates, or knowledge updates with human approval.

- Critical and High findings are fixed or formally waived with owner, expiry, compensating control, and remediation plan.

# 20. Open Reconciliation Items and Backlog
| ID | Issue | Required Treatment | Severity | Owner |
| --- | --- | --- | --- | --- |
| RI-020-001 | 11A duplicate numbering remains visible in source packs. | Track in 00D / Revision Control Matrix; do not silently renumber inside this guide. | Medium | Solutions Architecture Office |
| RI-020-002 | 41B / 44 System Builder overlap can confuse CI agent authority. | Pipeline evidence must reference governing System Builder source by canonical register decision. | Medium | Architecture Board |
| RI-020-003 | Runtime telemetry toggle governance must propagate to observability/runtime configuration documents. | Add cross-document backlog item after 20 v1.3 review. | Medium | SRE / DevSecOps |
| RI-020-004 | PoC 2 document 45 and CI/CD guide 20 overlap. | Treat 20 as reusable implementation guide and 45 as PoC 2 execution standard. | Low | DevSecOps Lead |
| RI-020-005 | Tool choices for SAST/SCA/DAST/SBOM may change. | Keep gates technology-neutral and pin actual tools in Golden Source. | Low | DevSecOps Lead |
| RI-020-006 | Evidence manifest schema should become machine-readable standard. | Generate AIRA Evidence Manifest Schema and Evidence Pack Data Model as next control document. | High | DevSecOps / Internal Audit |

# 21. AVCI Compliance Summary
| AVCI Property | Evidence in This Guide |
| --- | --- |
| Attributable | Document control identifies owner, co-owners, status, classification, superseded source, companion sources, evidence path, and approval route. Pipeline evidence captures developer, reviewer, branch, commit, ticket, build ID, tool versions, AI-use declaration, GitNexus metadata, PRR/ORR decision, and resilience evidence. |
| Verifiable | The guide requires build, tests, security scans, policy checks, architecture fitness, contract checks, Flyway validation, SBOM/provenance, GitNexus, observability, resilience, DAST, readiness, approvals, and release proof. |
| Classifiable | The guide requires classification for source, evidence, logs, traces, artifacts, screenshots, prompts, AI routes, Obsidian summaries, retention, and model eligibility. Secrets, raw PII, tokens, Restricted payloads, and unsafe evidence are blocked. |
| Improvable | Findings, failed gates, waivers, incidents, GitNexus drift, test gaps, security issues, runtime telemetry, readiness failures, and developer feedback feed governed Auto-Heal, Auto-Learn, Auto-Improve, backlog, runbook, and standard-update candidates. |

