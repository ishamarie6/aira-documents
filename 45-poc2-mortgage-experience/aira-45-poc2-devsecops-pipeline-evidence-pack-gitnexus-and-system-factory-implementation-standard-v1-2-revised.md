---
title: "PoC2 DevSecOps Pipeline Evidence Pack GitNexus and System Factory Implementation Standard"
doc_id: "AIRA-45"
version: "v1.2"
status: "revised"
category: "PoC2 and mortgage experience"
source_docx: "AIRA_45_PoC2_DevSecOps_Pipeline_Evidence_Pack_GitNexus_and_System_Factory_Implementation_Standard_v1.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 45-poc2-mortgage-experience
  - revised
  - aira-45
---



# PoC2 DevSecOps Pipeline Evidence Pack GitNexus and System Factory Implementation Standard



AIRA

AI-Native Enterprise Platform

PoC 2 DevSecOps Pipeline, Evidence Pack, GitNexus, and System Factory Implementation Standard

v1.2 Revised

Reusable Engineering Factory - CI/CD Gates - Evidence Packs - GitNexus Impact Analysis - Dynamic Workspace - MicroFunction Runtime - Secure Supply Chain - Resilience Lab - Governed AI Candidate Loops
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-045 |
| Canonical Filename | AIRA_45_PoC2_DevSecOps_Pipeline_Evidence_Pack_GitNexus_and_System_Factory_Implementation_Standard_v1.2_Revised.docx |
| Version | v1.2 - CI/CD Evidence Pack v1.2, Sprint 0 v1.2, Greenfield Environment v3.2, System Builder Lite workstation playbooks, Dynamic Workspace, MicroFunction backend, API/eventing, observability, resilience, security, AI governance, and progressive autonomy alignment update |
| Supersedes | 45-AIRA_PoC2_DevSecOps_Pipeline_Evidence_Pack_GitNexus_and_System_Factory_Implementation_Standard_v1.1.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for DevSecOps, Architecture, Security, QA/SDET, Platform Engineering, DBA, SRE, AI Governance, and Internal Audit Review |
| Owner | Solutions Architecture Office / IT Head |
| Primary Execution Owner | DevSecOps Lead + Software Development Team |
| Co-Owners | Enterprise Architecture; Development Lead; QA/SDET; Security Architecture; DBA; Platform Engineering; SRE / Operations; AI Governance; Knowledge Governance; Internal Audit |
| Primary Parents | 19B Sprint 0 and Foundation Build Execution Plan v1.2 Revised; 20 CI/CD Pipeline and Evidence Pack Implementation Guide v1.2 Revised; 09 Greenfield Environment Standard v3.2 Revised; 39A/39B/39C System Builder Lite and workstation setup revisions |
| Companion Sources | 01/01A AVCI and Enterprise Design Principles; 02 Engineering Blueprint; 03 Developer Guide; 04 Technology Stack; 07/07B Skills and Transformation; 08/08A Testing; 10/10A/10B/10C/10D/10E MicroFunction; 11/11A DevSecOps; 12A/41/46-61 Dynamic Workspace; 15/15A API Contract; 16/16A/16B Database/Flyway; 17/17A Security; 19 GitNexus; 21A/21B Knowledge and Runtime Platform; 22A Prompt/Guardrail/Model Registry; 31/31A Observability and Operations; 42D-42S AI Agent Governance; 43 Continuous Improvement |
| External Alignment Reference | NIST SP 800-218 SSDF; NIST SP 800-218A initial public draft where applicable for AI software; OWASP ASVS 5.0.0; OpenTelemetry Semantic Conventions; SLSA v1.2 |
| Review Cadence | At PoC 2 kickoff, every sprint during PoC 2, at pipeline gate changes, on material security or supply-chain change, before foundation capability reuse, and quarterly after stabilization |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / PoC2-DevSecOps-System-Factory / v1.2 / |
| Mandatory Practice Statement PoC 2 shall prove the reusable governed engineering factory for AIRA. It is not complete when a pipeline script runs. It is complete only when every pull request or merge request produces attributable, verifiable, classifiable, and improvable evidence for build, test, contract, policy, security, supply chain, GitNexus impact, Dynamic Workspace, MicroFunction, API/event, observability, resilience, rollback, and human approval controls. GitNexus and AI agents remain read-only or candidate-generating unless explicitly mediated through Harness, SBAC, OPA, evidence, and named human approval. |
| --- |

# 1. Executive Summary

PoC 2 is the first foundation factory proof point after PoC 1 and PoC 1A. Its purpose is to demonstrate that AIRA can repeatedly deliver governed changes through a reusable DevSecOps system factory rather than through one-off scripts, informal AI coding, or manually curated evidence. This v1.2 revision incorporates the revised Sprint 0, CI/CD Evidence Pack, Greenfield Environment, System Builder Lite, Dynamic Workspace, MicroFunction, and AI governance baselines.

The revised standard positions PoC 2 as the minimum reusable foundation capability for every future AIRA module. It verifies repository bootstrap, branch protection, CODEOWNERS, devcontainer readiness, Java 25 backend assumptions, frontend and backend quality gates, OpenAPI/AsyncAPI contracts, Kafka/Avro/CloudEvents eventing, Flyway migration controls, outbox/inbox reliability, GitNexus read-only impact analysis, security testing, authenticated DAST, supply-chain provenance, architecture fitness, observability evidence, resilience laboratory validation, and proposal-driven Auto-Heal/Auto-Learn/Auto-Improve loops.
| Strategic Outcome | v1.2 Required Result |
| --- | --- |
| Factory before volume | CI/CD, test automation, GitNexus, evidence generation, repository controls, and review gates exist before broad business functionality is developed. |
| Reusable foundation capability | PoC 2 outputs become reusable templates, pipeline stages, evidence schemas, policy bundles, test packs, and runbooks for future AIRA systems. |
| Evidence by construction | Evidence packs are generated automatically and bound to commit, branch, ticket, policy, test, scan, trace, artifact, approver, and rollback data. |
| Secure and observable delivery | SAST, SCA, secrets scan, SBOM, provenance, image scan, OPA/SBAC, authenticated DAST, OpenTelemetry, Log4j2, Sentry, Loki, Tempo, and Grafana are part of the exit gate. |
| Dynamic Workspace and MicroFunction readiness | Frontend and backend changes are contract-bound, policy-filtered, MicroFunction-backed, observable, feature-flagged, and reversible. |
| AI-safe continuous improvement | Auto-Heal, Auto-Learn, and Auto-Improve detect, analyze, draft, test, and propose. They do not silently merge, deploy, approve, or mutate production. |

# 2. v1.2 Upgrade Verdict and Scope Decision
| Area | v1.1 Baseline | v1.2 Required Upgrade |
| --- | --- | --- |
| Pipeline posture | Defined CI/CD, evidence pack, GitNexus, and system factory intent. | Converts the intent into explicit implementation gates across Sprint 0, PoC 2, Dynamic Workspace, MicroFunction, API/eventing, observability, security, and resilience lab readiness. |
| GitNexus | Read-only code intelligence and impact analysis. | Adds required evidence schema fields: report_hash, index_commit_sha, affected_files, affected_tests, architecture_drift, policy_reference, human_checker, and follow-up issue. |
| Evidence pack | PR/MR evidence summary and derived artifacts. | Adds machine-readable manifest, evidence retention, trace correlation, remediation evidence, runtime toggle evidence, and rollback/forward-fix evidence. |
| Dynamic Workspace | Not the primary PoC 2 focus. | Adds workspace shell, component registry, OpenAPI client generation, OPA-filtered component availability, frontend telemetry, accessibility test, and template activation gate. |
| MicroFunction | Framework companion reference. | Adds backend skeleton and transaction assembly gates for idempotency, outbox, audit, policy, observability, rollback, and no direct infrastructure calls from business logic. |
| API/eventing | Contract tests and integration readiness. | Adds OpenAPI, AsyncAPI, Kafka, Avro, CloudEvents, schema evolution, outbox/inbox, idempotent consumer, DLQ, retry, and replay validation gates. |
| Security | SAST/DAST/SBOM/secret scan. | Adds authenticated DAST scope, abuse-case tests, OPA/SBAC expansion, secrets hygiene, secure API checks, remediation evidence, and waiver controls. |
| AI loops | Auto-* boundaries acknowledged. | Defines candidate-loop workflow: detection, evidence retrieval, candidate proposal, test proof, PR/MR, human approval, controlled learning update, and post-change monitoring. |

# 3. Purpose, Scope, and Authority

## 3.1 Purpose

Define PoC 2 as the reusable DevSecOps and System Factory proof point for AIRA.

Translate the revised CI/CD Evidence Pack guide into a concrete PoC implementation standard.

Ensure every future AIRA repository inherits the same branch governance, pipeline gates, evidence schema, GitNexus analysis, policy checks, supply-chain controls, observability, and rollback discipline.

Verify that Dynamic Workspace, MicroFunction runtime, API/eventing, database migration, security, AI agent, and resilience controls are tested before expanding business functionality.

Define the acceptance gates that prove AIRA can build safely with human developers and approved AI assistants without uncontrolled automation.

## 3.2 In Scope / Out of Scope
| In Scope | Out of Scope |
| --- | --- |
| Repository bootstrap, branch protection, CODEOWNERS, PR/MR templates, devcontainer, Java 25 toolchain, Node/TypeScript toolchain, test packs, CI/CD templates, and evidence manifest. | Production deployment automation without CAB, ARB, change approval, rollback evidence, and post-promotion monitoring. |
| Build, unit, component, contract, architecture fitness, SAST, SCA, secret scan, SBOM, image scan, DAST, OPA/Conftest, provenance, signature, and release-readiness gates. | GitNexus, AI agents, Codex, or System Builder approving, merging, deploying, altering production configuration, or bypassing gates. |
| Dynamic Workspace shell, component registry, generated API client, frontend telemetry, accessibility tests, and workspace evidence. | Frontend authorization authority, direct business rules in UI, or UI-generated behavior outside backend MicroFunction and policy controls. |
| MicroFunction backend skeleton, OpenAPI/AsyncAPI contracts, Kafka/Avro/CloudEvents, Flyway, outbox/inbox, DLQ/replay, idempotency, observability, and resilience test readiness. | Manual DDL, direct SQL bypass in business logic, direct Kafka/DB/Redis/OpenKM/model calls inside business MicroFunctions, and one-off undocumented runtime fixes. |
| Auto-Heal, Auto-Learn, and Auto-Improve as proposal-driven candidate loops. | Silent production self-modification, self-approval, unreviewed prompt/policy updates, or autonomous learning becoming authoritative without human review. |

## 3.3 Authority and Precedence
| Level | Authority | PoC 2 Interpretation |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance | Final authority for production-impacting pipeline gates, release readiness, waivers, critical findings, and promotion decisions. |
| L1 | AIRA AVCI, 01A Enterprise Design Principles, Engineering Blueprint, Security, DevSecOps, Database, MicroFunction, API, Change, AI Governance | Universal rules for evidence, classification, architecture, security, testability, observability, rollback, policy, and human accountability. |
| L2 | This 45 v1.2 Standard | PoC 2 implementation authority for the reusable engineering factory proof point and its exit criteria. |
| L3 | 19B Sprint 0, 20 CI/CD Evidence Pack, 39A/39B/39C setup guides, 45 PoC 2 task records | Execution-level pipeline and setup instructions that must implement this standard. |
| L4 | Feature branches, CI runs, PR/MR evidence, GitNexus reports, test results, scan results, dashboards, logs, traces, tickets | Operational proof and improvement input. |
| Conflict Rule If this PoC 2 standard conflicts with a higher-authority AIRA source, apply the stricter control, log the issue as an AVCI reconciliation item, assign an owner, and resolve through ADR/TDL, ARB, CAB, or register 00D. Do not silently choose the easier interpretation. |
| --- |

# 4. Governing Source Baseline and Reconciliation Position
| Source / Companion | v1.2 Treatment |
| --- | --- |
| 45 v1.1 PoC 2 Standard | Preserved as the baseline purpose: PoC 2 proves the governed engineering factory and reusable foundation capability, not a one-time pipeline script. |
| 20 CI/CD Pipeline and Evidence Pack v1.2 | Controls the executable stage model, evidence pack manifest, security gates, architecture fitness checks, provenance, and promotion controls. |
| 19B Sprint 0 v1.2 | Controls foundation build sequencing, repository readiness, Dynamic Workspace shell, MicroFunction skeleton, API/eventing readiness, and resilience lab setup. |
| 09 / 39A / 39B / 39C Greenfield and workstation guides | Control environment readiness, developer workstation execution, Codex/VS Code boundaries, Activity Ledger, System Builder Lite setup, and team rollout governance. |
| 10/10A/10B/10C/10D/10E MicroFunction | Controls configuration-first assembly, standard step sequencing, ports/adapters, idempotency, audit, observability, rollback, and no direct infrastructure shortcuts. |
| 12A and 41/46-61 Dynamic Workspace | Controls frontend generation, workspace resolver, component registry, template lifecycle, API contracts, accessibility, security policy, testing, and evidence. |
| 15/15A API Contract | Controls OpenAPI, AsyncAPI, CloudEvents, schema registry, idempotency, error semantics, compatibility, and generated clients. |
| 16/16A/16B Database/Flyway | Controls Flyway-only migrations, PostgreSQL authority, seed data, schema evolution, RLS, concurrency, outbox, and migration evidence. |
| 17/17A Security and Access Control | Controls Keycloak, OPA, SBAC/ABAC/RBAC, secrets, classification, secure APIs, fail-closed behavior, and authenticated DAST expectations. |
| 19 GitNexus | Controls read-only code intelligence, impact analysis, derivative evidence, report hashing, agent-callable boundaries, and non-authority status. |
| 31/31A Observability | Controls Log4j2, OpenTelemetry, Sentry, Loki, Tempo, Grafana, logs, metrics, traces, audit, evidence correlation, and trace reconstruction. |
| 42D-42S / 43 AI Governance and Continuous Improvement | Controls agent identity, tool authorization, autonomy tiers, threat model, certification, incident response, registry evidence, and proposal-driven Auto-* loops. |

# 5. PoC 2 System Factory Control Model
| Operating Rule PoC 2 must produce a reusable factory capability. AIRA must be able to onboard a new repository or module and automatically inherit repository rules, CI/CD stages, evidence manifests, GitNexus analysis, policy checks, security scans, architecture fitness checks, Dynamic Workspace gates, MicroFunction gates, API/eventing gates, observability checks, rollback expectations, and human review controls. |
| --- |
| Factory Plane | Required PoC 2 Capability | Blocking Failure |
| --- | --- | --- |
| Source and Branch Governance | Repository template, protected branches, CODEOWNERS, PR/MR template, signed commits where required, issue linkage, AI-use declaration. | Unprotected main branch, missing CODEOWNERS, missing PR evidence, direct commit to protected branch, unmanaged local-only change. |
| Build and Test Plane | Java 25 backend build, Node/TypeScript frontend build, unit/component/contract/API tests, OPA policy tests, architecture fitness, mutation threshold where applicable. | Compiles but missing tests, disabled checks, weak assertions, direct provider calls, direct database leakage, untested policy decisions. |
| Security and Supply Chain Plane | SAST, SCA, secrets scan, SBOM, image scan, license check, provenance, signature, authenticated DAST, remediation evidence. | Critical/high finding unremediated or unwaived, secret exposure, unsigned artifact, missing SBOM/provenance, unscoped DAST. |
| Contract and Event Plane | OpenAPI/AsyncAPI lint, generated client verification, Kafka/Avro/CloudEvents schema check, compatibility test, outbox/inbox, DLQ/replay tests. | API drift, undocumented event, incompatible schema, missing idempotency key, unsafe replay, DLQ not tested. |
| Dynamic Workspace Plane | Workspace shell build, component registry validation, OPA-filtered component authorization, accessibility checks, frontend telemetry, template lifecycle evidence. | Frontend bypasses backend policy, component renders without capability binding, missing accessibility gate, no trace/evidence reference. |
| MicroFunction Runtime Plane | Runtime transaction skeleton, standard steps, ports/adapters, audit, outbox, policy, classification, observability, rollback and compensation path. | Business logic in controller, direct DB/Kafka/Redis/OpenKM/model call from business MicroFunction, missing idempotency/audit/trace. |
| Observability and Evidence Plane | Log4j2 safe structured logs, OTel traces/metrics/log context, Sentry errors, Loki logs, Tempo traces, Grafana dashboards, evidence manifest, redaction tests. | No correlation IDs, logs leak secrets/PII, dashboards absent, evidence pack incomplete, runtime toggle not audited. |
| Human Governance Plane | Maker-checker, reviewer ownership, waiver, ADR/TDL, CAB/ARB where applicable, release readiness review. | AI self-approval, developer approves own high-risk change, waiver without expiry, production promotion without authority. |

# 6. PoC 2 Implementation Sequence
| Phase | Goal | Minimum Output | Exit Gate |
| --- | --- | --- | --- |
| 0. Intake and ownership | Create controlled PoC 2 task, owner, reviewer, classification, affected repositories, scope, and success metrics. | Ticket, RACI, risk tier, evidence path, acceptance criteria. | Solutions Architecture and DevSecOps confirm scope. |
| 1. Repository and branch baseline | Bootstrap reusable repository controls. | Repository template, branch rules, CODEOWNERS, PR/MR template, devcontainer, AGENTS.md, evidence folders. | No unprotected branch or missing owner. |
| 2. Toolchain and build baseline | Prove deterministic local and CI builds. | Java 25, Gradle/Maven, Node/TypeScript, container image digest, lockfiles, build logs. | Build repeatable locally and in CI. |
| 3. Quality and architecture baseline | Run tests and architecture fitness functions. | Unit/component/contract tests, ArchUnit/Semgrep rules, mutation test plan, coverage threshold. | Critical architecture violations block. |
| 4. Security and supply-chain baseline | Run security gates and supply-chain evidence. | SAST, SCA, secrets scan, SBOM, image scan, license result, provenance, signature plan. | Critical/high security findings block unless formally waived. |
| 5. API/event/data baseline | Prove contract-first and event-driven readiness. | OpenAPI, AsyncAPI, Avro schema, CloudEvents profile, Flyway migration, outbox/inbox, DLQ/replay tests. | API/event incompatibility blocks. |
| 6. Dynamic Workspace and MicroFunction baseline | Prove frontend/backend governance boundaries. | Workspace shell, component registry, generated client, OPA filtering, MicroFunction skeleton, audit/outbox/trace. | Frontend authority or MicroFunction shortcut blocks. |
| 7. Observability and resilience baseline | Prove trace reconstruction and failure behavior. | OTel, Log4j2, Sentry, Loki, Tempo, Grafana, resilience lab, concurrency tests, runtime toggles. | Missing redaction, missing dashboards, unsafe retry/replay blocks. |
| 8. GitNexus and derived artifacts | Generate read-only impact evidence. | GitNexus report, code map, blast radius, affected tests, architecture drift, report hash. | GitNexus cannot be sole authority; evidence must be corroborated. |
| 9. Final evidence and review | Assemble PR/MR and foundation capability pack. | Evidence manifest, PR AVCI summary, release readiness, known limitations, improvement backlog, rollback plan. | Named human approval required before adoption/reuse. |

# 7. Mandatory CI/CD Stage Gates
| Stage | Required Checks | Evidence Artifact | Fail-Closed Condition |
| --- | --- | --- | --- |
| Pre-commit / pre-push | Formatting, lint, secrets scan, dependency sanity, forbidden files, prompt/guardrail policy checks. | pre_commit_result.json; secret_scan_local.json | Secrets or unsafe local-only file detected. |
| Build | Java 25 backend build, frontend build, Docker/devcontainer build, reproducible version metadata. | build_report.json; build_image_digest.txt | Toolchain mismatch, unpinned dependency, build not reproducible. |
| Unit and component tests | JUnit5, Vitest/Jest, policy unit tests, component tests, deterministic fixtures. | unit_test_report.xml; component_test_report.xml | Required tests fail or are skipped without waiver. |
| Contract and schema tests | OpenAPI lint, API compatibility, AsyncAPI lint, Avro compatibility, CloudEvents validation, generated client tests. | contract_evidence.json; schema_compatibility.json | Contract drift, breaking schema, missing error/idempotency semantics. |
| Architecture fitness | ArchUnit, dependency rules, forbidden direct calls, package boundaries, frontend authority checks, MicroFunction boundary checks. | architecture_fitness_report.json | Controller bloat, direct DB/model/provider calls, cross-context writes, frontend authorization logic. |
| Security | SAST, SCA, secret scan, IaC scan, image scan, OPA/Conftest, authenticated DAST when applicable. | security_evidence_pack.json | Critical/high finding unresolved; scanner unavailable; waiver missing. |
| Supply chain | SBOM, provenance, artifact digest, signature, license policy, dependency review. | sbom.spdx.json; provenance.intoto.jsonl; signature.txt | Missing SBOM/provenance/signature, unapproved license, untrusted artifact. |
| Observability | OTel instrumentation, log redaction, error capture, trace IDs, dashboards, alert rules. | observability_evidence.json; dashboard_refs.json | No trace/log/metric/audit correlation or forbidden telemetry fields. |
| Resilience | Idempotency tests, retry/DLQ/replay tests, concurrency tests, failure injection, rollback/compensation proof. | resilience_lab_report.json | Duplicate side effect, unsafe replay, no rollback/compensation path. |
| Evidence finalization | Manifest, GitNexus report, test/scan summaries, PR AVCI, approval, known limitations, backlog. | evidence_manifest.json; pr_avci_summary.md | Incomplete evidence pack or missing human reviewer. |

# 8. Evidence Pack Architecture
| Evidence Pack Rule Every PoC 2 PR/MR must produce an evidence pack that is machine-readable, human-reviewable, classified, retained, and linked to the source branch, commit, ticket, artifact digest, policy decision, test run, scan result, GitNexus report, approver, and rollback path. |
| --- |
| Evidence Class | Required Files / Records | Required Metadata |
| --- | --- | --- |
| Source evidence | branch_ref, commit_sha, PR/MR URL, CODEOWNERS review, AI-use declaration, AGENTS.md version. | owner, maker, checker, affected bounded context, classification, change type. |
| Build evidence | build logs, toolchain version, Java 25 proof, Node version, image digest, dependency lockfiles. | build_id, runner_id, environment, toolchain_ref, reproducibility_hash. |
| Test evidence | unit, component, contract, OPA, frontend, Playwright, mutation, accessibility, architecture fitness. | test_run_id, coverage, failed/skipped tests, waiver_ref, affected_tests. |
| Security evidence | SAST, SCA, secret scan, IaC scan, image scan, DAST, abuse-case test, remediation evidence. | scanner, version, ruleset, severity, finding_id, remediation_commit, waiver_expiry. |
| Supply-chain evidence | SBOM, provenance, artifact digest, signature, license review, dependency review. | artifact_name, digest, signer, SLSA track target, license decision, attestation_ref. |
| Contract/event evidence | OpenAPI, AsyncAPI, Avro, CloudEvents, schema compatibility, generated client test, outbox/inbox, DLQ/replay. | contract_version, schema_id, topic, compatibility_mode, idempotency_profile. |
| Observability evidence | Log4j2 config, OTel traces, metrics, logs, Sentry issue, Loki query, Tempo trace, Grafana dashboard, audit event. | trace_id, metric_name, dashboard_ref, redaction_profile, sampling/toggle state. |
| GitNexus evidence | code map, impact analysis, affected tests, architecture drift, risk hotspots, report hash. | index_commit_sha, report_hash, tool_version, scope, checker, limitations. |
| Approval and release evidence | PR AVCI summary, ARB/CAB decision, deploy eligibility, rollback/forward-fix, known limitations, backlog. | approver, decision_time, change_ticket, rollback_ref, post-monitoring_ref. |
| evidence_manifest: manifest_version: "aira-poc2-v1.2" document_ref: "AIRA-DOC-045" ticket_ref: "" branch_ref: "" commit_sha: "" classification: "INTERNAL CONFIDENTIAL" bounded_context: "" artifacts: build: [] tests: [] security: [] supply_chain: [] contracts: [] observability: [] resilience: [] gitnexus: [] approvals: [] avci: attributable: "owner + maker + checker + source + version recorded" verifiable: "tests + scans + policy + traces + evidence manifest available" classifiable: "classification and redaction profile applied" improvable: "known limitations + backlog + review cadence captured" |
| --- |

# 9. GitNexus and Derived Artifact Generator Control

GitNexus is adopted in PoC 2 as read-only, derivative, commit-bound code intelligence. It may help generate code maps, dependency graphs, blast-radius reports, affected-test recommendations, architecture drift signals, and reviewer focus areas. It does not replace tests, scanners, architecture review, security review, CODEOWNERS, or human approval.
| GitNexus Output | Required Use | Prohibited Use | Evidence Required |
| --- | --- | --- | --- |
| Code map and dependency graph | Help reviewers understand affected modules, packages, adapters, contracts, and test areas. | Treating GitNexus output as architecture authority. | report_hash, index_commit_sha, scope, limitations, reviewer. |
| Impact analysis | Identify affected APIs, events, MicroFunctions, Dynamic Workspace components, database migrations, and tests. | Skipping test discovery or compatibility checks because GitNexus found no impact. | affected_files, affected_contracts, affected_tests, false_positive_notes. |
| Architecture drift signal | Support fitness function review and drift backlog. | Auto-fixing or auto-merging architecture changes. | drift_id, rule_ref, severity, owner, follow-up issue. |
| Security-sensitive map | Highlight auth, secrets, policy, audit, and external integration paths. | Replacing SAST, DAST, threat model, or secure review. | sensitive_area, policy_ref, checker, remediation_link. |
| Derived evidence summary | Create Obsidian-ready summary without copying full source code. | Publishing full repository contents or Restricted code into Obsidian/LLM Wiki. | summary_ref, source_commit, classification, retention, disposal. |

# 10. Dynamic Workspace and MicroFunction PoC 2 Gates
| Control Area | Dynamic Workspace Gate | MicroFunction Backend Gate |
| --- | --- | --- |
| Boundary | UI must render backend-approved workspace, screen, component, and action definitions. It must not become business authority. | Business MicroFunctions must use ports/adapters and must not parse transport payloads, own framework concerns, or call DB/Kafka/Redis/OpenKM/model providers directly. |
| Policy | OPA/SBAC/ABAC filters components, actions, templates, AI panel, and admin-builder functions before rendering or invocation. | OPA/SBAC decisions are part of the transaction steps and are recorded as evidence. |
| Contracts | Generated frontend clients come from approved OpenAPI contracts; async UI notifications must trace to AsyncAPI/CloudEvents definitions. | MicroFunction transactions expose approved APIs/events only; runtime config is Flyway/Golden Source governed. |
| Evidence | Workspace resolution, component render, policy denial, layout change, widget action, AI prompt, and template lifecycle events emit safe audit/evidence. | Every transaction emits correlation, classification, idempotency, validation, authorization, audit, outbox, metric, log, trace, and rollback/compensation evidence. |
| Testing | Frontend unit, Playwright smoke, accessibility, policy-filter, generated-client, and telemetry tests are required. | Unit, component, contract, OPA, idempotency, outbox, concurrency, rollback, and architecture fitness tests are required. |
| Rollback | Templates, feature flags, components, and telemetry toggles must be safely disableable. | Transaction definitions, seed data, policy versions, and feature flags must support rollback, forward-fix, or compensation. |

# 11. API, Eventing, Database, and Replay Readiness
| Capability | PoC 2 Minimum Proof | Evidence / Gate |
| --- | --- | --- |
| OpenAPI | At least one API contract with request/response schema, Problem Details, correlation headers, idempotency header where mutating, generated client, and contract test. | openapi.yaml, lint result, generated client test, contract test report. |
| AsyncAPI | At least one event contract with topic, payload schema, CloudEvents metadata, retry/DLQ behavior, and consumer contract. | asyncapi.yaml, compatibility report, consumer test. |
| Kafka / Avro / CloudEvents | Topic naming, Avro schema compatibility, CloudEvents envelope, correlation_id, causation_id, traceparent, tenant/classification metadata where safe. | schema registry compatibility, sample event, replay test. |
| Outbox / inbox | Transactional outbox for event publication and inbox/deduplication for consumer idempotency. | outbox migration, inbox/dedup test, failure/retry evidence. |
| Schema evolution | Backward/forward compatibility rules and migration sequence. | schema diff, compatibility gate, consumer impact matrix. |
| DLQ and replay | Retry strategy, DLQ route, replay authorization, replay idempotency, replay audit, and safe recovery procedure. | DLQ test, replay test, OPA approval evidence, no duplicate side effect proof. |
| Flyway and database | Flyway-only migration from Day 0, seed data, indexes, RLS where needed, rollback/forward-fix strategy. | Flyway report, checksum, clean-migrate test, DBA review. |
| Concurrency and heavy transaction | Optimistic locking, unique constraints, idempotency keys, bounded retry, queue backpressure, and load/failure behavior. | concurrency_test_report, load_test_summary, resilience_lab_report. |

# 12. Observability, Runtime Telemetry Toggles, and Evidence Correlation

PoC 2 must prove that AIRA can reconstruct a change and its runtime behavior from source, pipeline, evidence, and telemetry. Observability is not optional and must be classification-safe. Runtime toggles may adjust diagnostic depth, sampling, and expensive instrumentation, but they must not disable required audit, security, evidence, or safety signals.
| Signal / Toggle | Required Baseline | Governed Runtime Behavior |
| --- | --- | --- |
| Log4j2 structured logs | JSON-safe logs with trace_id, span_id, request_id, service, environment, severity, error_code, and classification. | Log verbosity may be changed through approved config only; no tokens, secrets, raw PII, raw prompts, embeddings, or unrestricted payloads. |
| OpenTelemetry | Traces and metrics across frontend, gateway, backend, MicroFunction runtime, DB, Kafka, OPA, and AI gateway where applicable. | Sampling may be tuned but critical error/security/audit paths must remain traceable. |
| Sentry | Frontend/backend error monitoring with safe redaction and release/commit correlation. | Issue creation can be toggled for non-prod noise reduction but critical errors still require evidence capture. |
| Loki / Tempo / Grafana | Logs, traces, dashboards, policy-denial views, pipeline health, workspace health, MicroFunction performance, DLQ/replay, and evidence completeness. | Dashboards and queries are controlled artifacts and must be linked in evidence packs. |
| Audit and evidence records | Append-only governance events for PR/MR, pipeline gates, policy decisions, runtime actions, AI use, approvals, waivers, and rollback. | Cannot be turned off for protected actions. Audit writer failure fails closed or blocks promotion. |
| Runtime diagnostic toggles | Feature flags for debug traces, verbose SQL explain in non-prod, widget telemetry, API client telemetry, resilience probes. | Each toggle has owner, default, allowed values, scope, risk, approval, audit event, expiry, and rollback path. |

# 13. Security, OPA/SBAC, Abuse Cases, and Authenticated DAST
| Security Control | Required PoC 2 Treatment | Evidence |
| --- | --- | --- |
| OPA/SBAC/ABAC expansion | Pipeline must test policy bundles for repository, API, workspace, MicroFunction, AI agent, tool action, DAST scope, replay, and promotion decisions. | opa_test_report, policy_decision_log, policy_bundle_hash. |
| Secrets hygiene | No secrets in source, .env, prompts, screenshots, logs, traces, tests, Obsidian, LLM Wiki, GitNexus, or evidence summaries. Use approved secret references only. | secret_scan_report, redaction_test, vault_ref_check. |
| Authenticated DAST | DAST uses synthetic users, synthetic data, approved non-prod URLs, scoped auth, rate limit, safe test windows, and remediation evidence. | dast_scope.md, zap/burp report, remediation_ticket. |
| Secure APIs | API gateway, authN/authZ, request validation, rate limit, secure headers, Problem Details, safe errors, idempotency, and classification handling. | api_security_test_report, contract_security_lint. |
| Abuse cases | Test misuse cases: bypass policy, replay action, duplicate idempotency key, unauthenticated API, insufficient skill, excessive widget action, unsafe replay, model/tool overreach. | abuse_case_test_matrix, findings, remediation evidence. |
| AI and tool boundary | AI may recommend, draft, test, summarize, and open candidates; tool actions go through Harness/SBAC/OPA and human approval. | AI-use declaration, tool_action_request, approval evidence. |
| Waivers | Waivers require owner, reason, compensating control, expiry, risk acceptance, and follow-up backlog. | waiver_ref, approval, expiration, closure evidence. |

# 14. Resilience Lab and Heavy-Transaction Evidence
| Scenario | Minimum Test | Pass Condition |
| --- | --- | --- |
| Retry-safe API request | Repeat mutating API call with same idempotency key. | Single business effect; duplicate is safely recognized and evidenced. |
| Outbox publication failure | Simulate DB commit success but Kafka publish unavailable. | Outbox retains event; retry publishes once; audit shows recovery path. |
| Consumer crash before ack | Crash consumer after receive and before completion. | Inbox/dedup prevents duplicate effect; replay is safe. |
| DLQ and replay | Force poison message to DLQ and replay after remediation. | Replay requires authorization, preserves traceability, and does not duplicate effects. |
| Concurrent updates | Run simultaneous updates against same aggregate/config. | Optimistic lock or version check prevents lost update; safe response returned. |
| Heavy transaction / backpressure | Load test queue/API with bounded concurrency. | SLO behavior measured; rate limits, bulkheads, circuit breakers, and queue backpressure operate. |
| Policy service unavailable | OPA unavailable during protected action. | Protected action fails closed and evidence captures policy dependency failure. |
| Observability sink unavailable | Logging/tracing/exporter failure in non-critical path. | System degrades safely without leaking data; required audit/evidence still captured or protected action blocks. |
| Rollback / forward-fix | Trigger feature disablement, config rollback, or forward-fix plan. | Rollback path is documented, tested, and evidence-linked. |

# 15. Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop
| Non-Negotiable AI Boundary Auto-Heal, Auto-Learn, and Auto-Improve may detect, correlate evidence, propose fixes, generate tests, prepare PR/MR drafts, recommend knowledge updates, and route approvals. They must not self-approve, silently mutate runtime behavior, bypass policy, update production, change canonical standards, or promote learning into authority without human review. |
| --- |
| Loop Step | Auto-Heal / Learn / Improve Action | Required Human / Control Gate | Evidence |
| --- | --- | --- | --- |
| 1. Issue detection | Detect failed gate, test regression, security finding, trace anomaly, SLO breach, DLQ growth, policy denial trend, or GitNexus drift signal. | Classification and severity triage by owner/checker. | issue_ref, trigger_type, trace/log/test/scan evidence. |
| 2. Evidence retrieval | Retrieve approved sources, pipeline evidence, GitNexus report, logs, traces, contracts, policies, and recent changes. | Retrieval must respect SBAC, classification, freshness, and provenance. | retrieval_log, source_refs, context_hash. |
| 3. Candidate proposal | Draft fix options, test additions, policy changes, config changes, runbook updates, or learning notes. | Candidate remains draft until reviewer accepts. | candidate_proposal.md, risk, rollback, affected tests. |
| 4. Validation | Generate or request unit/contract/security/resilience tests and run simulations. | CI/CD and policy gates execute; AI cannot mark its own output approved. | validation_report, test_results, policy_decisions. |
| 5. PR/MR or backlog | Open PR/MR or create backlog item with AVCI summary. | CODEOWNERS, maker-checker, ARB/CAB where applicable. | PR link, reviewer, approval, evidence manifest. |
| 6. Controlled learning | Update prompt, runbook, knowledge, test pack, or fitness function only after approval. | Knowledge Governance and source authority rules apply. | knowledge_update_ref, Obsidian/Git commit, review record. |
| 7. Monitoring | Observe post-change behavior and rollback if needed. | SRE/DevSecOps monitor and close loop. | dashboard_ref, incident closure, improvement backlog. |

# 16. RACI and Separation of Duties
| Activity | IT Head / Solutions Architecture | DevSecOps Lead | Developer | QA/SDET | Security | DBA | SRE / Platform | Internal Audit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Approve PoC 2 scope | A | R | C | C | C | C | C | I |
| Repository and branch baseline | A | R | C | C | C | I | C | I |
| CI/CD implementation | A | R | C | C | C | C | C | I |
| Test pack and quality gates | C | A | R | R | C | C | C | I |
| Security gates and DAST | C | C | C | C | A/R | I | C | I |
| Flyway / database gates | C | C | C | C | C | A/R | I | I |
| GitNexus analysis | C | A/R | C | C | C | I | I | I |
| Evidence pack review | A | R | C | C | C | C | C | C |
| Waiver approval | A | C | I | C | R for security waivers | R for DB waivers | C | C |
| Foundation reuse decision | A/R | C | C | C | C | C | C | I |

# 17. Definition of Done and Acceptance Criteria
| Acceptance Category | Required Evidence | Decision Rule |
| --- | --- | --- |
| Repository readiness | Protected branch, CODEOWNERS, PR/MR template, AGENTS.md, devcontainer, dependency locks, evidence folder. | Must pass before feature PR volume. |
| Pipeline readiness | Build/test/security/supply-chain/contract/architecture/observability/resilience/evidence stages implemented and repeatable. | No critical stage may be manual-only without waiver. |
| Evidence completeness | Evidence manifest, scan/test reports, GitNexus report, dashboards, policy decisions, approvals, rollback, backlog. | Incomplete evidence blocks acceptance. |
| Security readiness | No unresolved critical/high findings; secrets hygiene proven; authenticated DAST scoped; OPA/SBAC tests pass. | Unwaived high-risk finding blocks. |
| Dynamic Workspace readiness | Workspace shell, component registry, generated client, OPA filtering, telemetry, accessibility, template lifecycle evidence. | Frontend authority bypass blocks. |
| MicroFunction readiness | Runtime skeleton, standard steps, ports/adapters, audit, outbox, idempotency, rollback, policy, tests. | Direct infra shortcut blocks. |
| API/event/data readiness | OpenAPI, AsyncAPI, Avro, CloudEvents, Flyway, outbox/inbox, DLQ/replay, schema compatibility. | Contract or replay failure blocks. |
| Resilience readiness | Concurrency, idempotency, retry, circuit breaker, DLQ/replay, failure injection, rollback tests. | Duplicate side effect blocks. |
| AI governance readiness | AI use declared; agent actions mediated; Auto-* candidate loop evidence; no self-approval. | AI self-approval or uncontrolled mutation blocks. |
| Reusable foundation handoff | Templates, runbooks, evidence schemas, known limitations, backlog, owner, review cadence, support path. | Cannot be reused until owner accepts operating responsibility. |

# 18. Risks, Anti-Patterns, and Required Controls
| Risk / Anti-Pattern | Why It Matters | Required Control |
| --- | --- | --- |
| Pipeline theater | A pipeline runs but does not prove safety, quality, architecture, security, or evidence. | Evidence pack completeness and required gates block promotion. |
| GitNexus over-trust | Code intelligence is helpful but derivative. | GitNexus output must be corroborated by tests, scans, contracts, and reviewer judgment. |
| AI bypass | AI tool generates code or fixes without governance. | AI use declaration, branch-bound execution, Harness/SBAC/OPA, CODEOWNERS, human approval. |
| Frontend authority | Workspace UI makes authorization or business decisions. | Backend policy filtering, MicroFunction action binding, contract tests, architecture fitness. |
| MicroFunction shortcut | Business logic calls DB/Kafka/Redis/OpenKM/model providers directly. | Ports/adapters checks, ArchUnit/Semgrep rules, code review, and tests. |
| Eventing without replay safety | Kafka events are published but consumers are not idempotent. | Outbox/inbox, idempotency keys, DLQ/replay test, duplicate effect checks. |
| Telemetry leakage | Logs/traces capture secrets, raw PII, prompts, tokens, or embeddings. | Forbidden field tests, redaction profile, sampling controls, safe log review. |
| Waiver sprawl | Exceptions become permanent weaknesses. | Expiry, owner, compensating control, CAB/ARB approval, backlog closure evidence. |
| One-off factory | PoC 2 outputs cannot be reused. | Foundation capability packaging and consumer onboarding acceptance criteria. |

# 19. Implementation Roadmap
| Milestone | Target Output | Review Gate |
| --- | --- | --- |
| M1 - PoC 2 kickoff | PoC 2 ticket, scope, RACI, repo list, evidence path, setup checklist. | Solutions Architecture + DevSecOps review. |
| M2 - Repository and toolchain baseline | Repository template, branch rules, devcontainer, Java 25/Node toolchain, AGENTS.md, pre-commit. | Branch governance and environment evidence review. |
| M3 - CI/CD stage baseline | Build/test/security/supply-chain/architecture/contract/evidence stages implemented. | Dry run on controlled sample repository. |
| M4 - Dynamic Workspace and MicroFunction gates | Workspace shell, API client, policy-filtered component registry, MicroFunction skeleton, audit/outbox/trace. | Architecture and security review. |
| M5 - API/eventing/data gates | OpenAPI/AsyncAPI/Kafka/Avro/CloudEvents/Flyway/outbox/DLQ/replay readiness. | Contract and DBA review. |
| M6 - Observability and resilience lab | Dashboards, trace reconstruction, runtime telemetry toggles, idempotency/concurrency/failure tests. | SRE/QA/DevSecOps review. |
| M7 - GitNexus and derived artifacts | GitNexus reports, code map, impact summary, evidence summaries, known limitations. | Reviewer validation and evidence manifest check. |
| M8 - Acceptance and reuse | Reusable foundation package, templates, runbooks, evidence schema, onboarding guide, improvement backlog. | ARB/CAB adoption decision. |

# 20. PR/MR AVCI Evidence Summary Template
| ## AIRA PoC 2 PR/MR AVCI and System Factory Evidence Summary ### Attributable - Ticket / intake ID: - Owner / maker: - Checker / reviewer: - Repository / branch / commit: - AI tools used and prompt references: - GitNexus report hash: ### Verifiable - Build evidence: - Unit/component/contract tests: - Architecture fitness: - SAST/SCA/secrets/image scan: - Authenticated DAST scope/result: - SBOM/provenance/signature: - OpenAPI/AsyncAPI/schema compatibility: - Flyway migration evidence: - Outbox/inbox/DLQ/replay evidence: - Observability and dashboard references: - Resilience lab evidence: ### Classifiable - Data classification: - Secrets/PII handling: - Evidence storage path: - Telemetry redaction profile: - Model/AI route eligibility: ### Improvable - Known limitations: - Waivers and expiry: - Follow-up backlog: - Auto-Heal/Learn/Improve candidate items: - Standards requiring update: ### Reversibility - Rollback / forward-fix / compensation path: - Feature flags / runtime toggles: - Post-change monitoring: - Approver decision: |
| --- |

# 21. External Alignment Register
| External Source | AIRA PoC 2 Treatment |
| --- | --- |
| NIST SP 800-218 SSDF | Secure development practices are operationalized as governed repository, build, test, vulnerability, release, and evidence gates. |
| NIST SP 800-218A Initial Public Draft, where applicable | AI software considerations are treated as additional candidate-control guidance, not as a replacement for AIRA governance. |
| OWASP ASVS 5.0.0 | Authenticated DAST, secure API, authentication, session, authorization, validation, error handling, and secure configuration gates are mapped to web/API verification expectations. |
| OpenTelemetry Semantic Conventions | Traces, metrics, logs, resources, HTTP, database, messaging, CI/CD, and error telemetry use consistent semantic attributes where practical. |
| SLSA v1.2 | Supply-chain controls include source governance, build integrity, provenance, artifact digest, signatures, dependency review, and attestation evidence. |

# 22. AVCI Compliance Summary
| AVCI Property | PoC 2 Evidence |
| --- | --- |
| Attributable | Document control identifies owner, co-owners, source baseline, companion sources, execution owners, evidence path, PR/MR owner, maker, checker, approver, repository, branch, commit, toolchain, and AI-use references. |
| Verifiable | Pipeline gates produce build, test, contract, security, supply-chain, architecture fitness, GitNexus, observability, resilience, policy, approval, and rollback evidence. |
| Classifiable | All source, evidence, telemetry, scans, prompts, AI outputs, GitNexus summaries, dashboards, logs, traces, and derived artifacts carry classification, redaction, retention, and retrieval eligibility controls. |
| Improvable | Known limitations, waivers, failure trends, GitNexus drift, DAST findings, test gaps, SLO evidence, incident patterns, and Auto-Heal/Learn/Improve candidates feed controlled backlog and source-standard updates. |

