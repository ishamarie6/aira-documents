---
title: "System Builder Implementation Guide AI Agent Creation and Environment Provisioning"
doc_id: "AIRA-44A"
version: "v1.1"
status: "revised"
category: "System builder, AI agents, and PoC1A"
source_docx: "AIRA_44A_System_Builder_Implementation_Guide_AI_Agent_Creation_and_Environment_Provisioning_v1.1_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 44-system-builder-agent-poc1a
  - revised
  - aira-44a
---



# System Builder Implementation Guide AI Agent Creation and Environment Provisioning



AIRA
AI-Native Enterprise Platform

System Builder Implementation Guide
AI Agent Creation and DevSecOps Environment Provisioning

Guided Intake | Agent Registry | Environment Manifests | Tool Authorization | Evidence by Construction | AVCI Always
| Property | Value |
| --- | --- |
| Document ID | AIRA-DOC-044A |
| Canonical Filename | 44A-AIRA_System_Builder_Implementation_Guide_AI_Agent_Creation_and_Environment_Provisioning_v1.1_Revised.docx |
| Version | v1.1 - Revised and Aligned Implementation Guide |
| Supersedes | 44A-AIRA_System_Builder_Implementation_Guide_AI_Agent_Creation_and_Environment_Provisioning_v1.0.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Architecture, Security, DevSecOps, AI Governance, DBA, QA/SDET, SRE, and Internal Audit Review |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; AI Governance; Security Architecture; DevSecOps Lead; Platform Engineering; DBA; QA/SDET; SRE; Internal Audit |
| Primary Parent | 41B / 44 System Builder and Governed AI-Assisted Change Generation Standard |
| Companion Sources | 01/01A/01B AVCI and EDP; 07/07B Skills and Maturity; 15/15A API; 16/16A/16B Database/Flyway; 17/17A Security; 20/45 DevSecOps Evidence; 31/31A Observability; 32 SBAC; 39A/39B/39C System Builder Lite; 42D-42O Agent Governance; 46-61 Dynamic Workspace |
| Review Cadence | Quarterly; unscheduled on System Builder, AI agent, tool/MCP, model route, environment, policy, data, security, or provisioning change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / System-Builder / Agent-Creation-and-Environment-Provisioning / v1.1/ |

Mandatory Practice Statement

The AIRA System Builder is a governed implementation factory, not an autonomous authority. It may analyze, recommend, draft, generate, validate, and package candidate AI agents, environment provisioning artifacts, APIs, workflows, policies, prompts, guardrails, database migrations, tests, dashboards, and evidence. It must not approve its own output, silently mutate runtime behavior, bypass OPA/SBAC, use direct model-provider calls, receive production credentials, deploy to production, or promote any artifact without maker-checker review, CI/CD gates, security review, ARB/CAB routing where required, rollback readiness, and AVCI evidence.

# 1. Executive Summary

This v1.1 guide converts the System Builder governance standard into executable implementation guidance for two high-risk factory capabilities: AI agent creation and AI DevSecOps environment provisioning. The guide defines the intake screens, contract outputs, registry records, policy decisions, seed packages, tool manifests, evidence packs, test gates, and approval routes needed to create agents and environments without uncontrolled automation.

The primary correction in v1.1 is explicit alignment with the revised Dynamic Workspace, MicroFunction, API/eventing, database/Flyway, security, observability, DevSecOps evidence, and agent-governance documents. System Builder output is treated as a candidate artifact until evidence proves it is attributable, verifiable, classifiable, and improvable.
| Strategic Outcome | Required v1.1 Treatment |
| --- | --- |
| No shadow agents | Every agent is requested, registered, owned, classified, tested, certified, observable, revocable, and linked to evidence before use. |
| No uncontrolled provisioning | Every environment setup is manifest-driven, Git-managed, scanned, policy-checked, approved, rebuildable, and rollbackable. |
| Contract-first delivery | Screens, APIs, AsyncAPI events, Flyway migrations, OPA policies, prompt/guardrail bundles, and evidence schemas are drafted before implementation. |
| Human-governed autonomy | System Builder may produce candidate artifacts and tool-action requests; authority remains with humans, policies, CI/CD gates, and CAB/ARB where applicable. |
| Evidence by construction | Every lifecycle transition captures source, owner, classification, trace, policy decision, test result, security result, and improvement path. |

# 2. v1.1 Alignment Decision and Scope
| Alignment Area | Implementation Impact |
| --- | --- |
| 41B / 44 System Builder overlap | Treat 41B as the governing standard and this 44A guide as the implementation playbook. Any 41B/44 duplicate-overlap issue remains an AVCI reconciliation item. |
| Dynamic Workspace | System Builder UI must be backend-governed, policy-filtered, MicroFunction-backed, OpenAPI-bound, observable, accessible, and reversible. |
| MicroFunction backend | Generated capabilities must bind to registered MicroFunction transaction codes; business authority remains backend-controlled. |
| API and eventing | OpenAPI, AsyncAPI, Kafka, Avro, CloudEvents, outbox/inbox, idempotency, DLQ, and replay impacts must be declared before generation. |
| Database/Flyway | Database outputs are candidate Flyway migrations and seed packages only; no direct SQL shortcuts or manual production DDL. |
| Security and SBAC | Agent and provisioning actions require owner, classification ceiling, SBAC skill scope, OPA decision, tool manifest, and fail-closed behavior. |
| Observability and evidence | Log4j2, OpenTelemetry, Sentry, Loki, Tempo, Grafana, audit, trace reconstruction, and evidence references must be part of generated readiness. |
| Auto-Heal/Auto-Learn/Auto-Improve | System Builder can create candidate loops, but cannot self-fix, self-learn into authority, or self-promote without human approval. |

# 3. Authority, Non-Goals, and Rejection Rules

44A is subordinate to the System Builder governance standard, AI governance, security, DevSecOps, database/Flyway, API contract, observability, change/CAB, and dynamic workspace standards. It does not authorize production mutation, direct provider SDK calls, direct Kubernetes/database/Git/CI access by agents, unreviewed MCP servers, or bypass of classification and evidence controls.

Reject any agent request without a named human owner, purpose, non-goals, classification ceiling, skill scope, model-route eligibility, tool manifest, test plan, kill-switch path, and retirement plan.

Reject any environment request that contains actual secrets, requests unapproved technology, bypasses Golden Source, disables scans, or lacks rebuild and rollback evidence.

Reject any generated UI, API, migration, policy, prompt, or agent definition that cannot be traced to an intake record, source baseline, reviewer, approval route, and evidence pack.

Reject any tool path where an agent can approve, merge, deploy, rotate production secrets, change policy, unlock privileged access, delete data, or approve its own output.

Reject any runtime toggle that weakens audit, policy, identity, guardrail, or evidence capture for protected actions.

# 4. Unified Implementation Workflow

The System Builder must execute through a deterministic workflow. Each stage produces evidence and either advances the request, returns it for clarification, or blocks it for governance resolution.
| Stage | Required Output | Blocking Condition |
| --- | --- | --- |
| 1. Intake | Structured request, owner, source, classification, bounded context, risk tier, target environment. | Missing owner, unclear authority, unsupported classification, or no business/technical purpose. |
| 2. Impact analysis | Affected contracts, MicroFunctions, data schemas, policies, repositories, environments, tools, agents, and evidence. | Conflicting source, missing baseline, unknown dependency, or high-risk change without review route. |
| 3. Recommendation | Options, risk, architecture impact, test path, rollback path, cost/complexity, approval route. | Recommendation weakens EDP, SOLID, security, observability, rollback, or AVCI. |
| 4. Approval to generate | Named maker-checker approval for candidate generation. | Self-approval, missing checker, or approval outside delegated authority. |
| 5. Candidate generation | Draft agent/environment artifacts in branch/sandbox only. | Direct production mutation, direct credentials, direct model-provider calls, or unregistered tool use. |
| 6. Validation | Tests, scans, OPA/Rego tests, contract checks, GitNexus, SBOM/provenance, evidence pack. | Critical/high findings, missing evidence, failed policy, failed migration, or missing rollback. |
| 7. Promotion request | PR/MR, CAB/ARB/security/DBA route, deployment plan, rollback/deactivation plan. | Incomplete AVCI summary, unresolved risks, or no accountable approver. |
| 8. Activation and monitoring | Registry state update, release evidence, dashboards, SLO/alerts, incident path. | No observability, no kill switch, no owner, or no post-promotion review. |

# 5. AI Agent Creation Implementation Blueprint

An AIRA agent is a governed engineering artifact: model route plus instructions, tools, skills, workspace, memory/context, runtime controls, and evidence. Agents are not informal scripts or unmanaged assistants.
| Agent Artifact | Required Fields / Controls |
| --- | --- |
| Agent definition | agent_id, name, purpose, non-goals, owner, backup owner, bounded context, lifecycle state, version, source_ref. |
| Classification and data scope | classification ceiling, tenant/context scope, data eligibility, retrieval sources, forbidden data classes. |
| SBAC and OPA binding | skill codes, action classes, autonomy tier T0-T5, OPA policy refs, approval matrix, SoD constraints. |
| Model and guardrails | LiteLLM alias, fallback policy, input/retrieval/execution/output guardrails, evaluation threshold, prompt version. |
| Tool/MCP manifest | allowed tools, actions, dry-run support, idempotency profile, rollback method, Harness route, TTL, risk tier. |
| Memory/RAG profile | allowed sources, freshness, provenance, quarantine, memory write approval, context hashing, prompt-injection defenses. |
| Runtime telemetry | trace_id, run_id, actor, policy_decision_id, model_route_id, tool_action_id, evidence_ref, redaction state. |
| Certification and lifecycle | threat model, red-team tests, blocked-action tests, certification state, recertification due, suspension, retirement proof. |

Agent creation is allowed only as a candidate until registry records, policy tests, evaluation results, security review, DevSecOps evidence, and human approval are complete. Trust promotion is action-specific; the same agent may be allowed to read approved evidence but blocked from tool execution or production-impacting action.

# 6. Environment Provisioning Implementation Blueprint

Environment provisioning through System Builder must use declarative manifests and GitOps/IaC-style promotion. System Builder may draft environment setup but must not install unapproved technologies, bypass platform controls, store secrets, or mutate production directly.
| Provisioning Artifact | Required Treatment |
| --- | --- |
| Environment setup request | environment_id, purpose, owner, target tier, classification, network zone, dependencies, required approvals. |
| Toolchain manifest | approved versions, pinned images/digests, Java 25 baseline where backend applies, Node/Next.js baseline, scanner versions. |
| Devcontainer / runner config | Reproducible local and CI environment with no embedded secrets, policy checks, SBOM, and provenance. |
| IaC / platform draft | Terraform/Helm/Kustomize/ArgoCD or equivalent draft only; no direct production application without approval. |
| Secrets plan | Vault/OpenBao paths, secret classes, rotation policy, access owners, no values in prompts, migrations, logs, screenshots, or evidence. |
| Observability setup | OpenTelemetry, Log4j2, Sentry, Loki, Tempo, Grafana, dashboards, alerts, evidence refs, trace reconstruction. |
| Security validation | SAST, SCA, secret scan, SBOM, provenance, OPA, authenticated DAST for applicable apps, hardening checklist. |
| Rebuild and rollback | Destroy/rebuild path, restore validation, Helm/GitOps rollback, feature disablement, compensation or deactivation path. |

# 7. Generated Artifact Families
| Artifact Family | Generation Boundary | Evidence Required |
| --- | --- | --- |
| Screens / Dynamic Workspace | Generate templates, layouts, widget bindings, and admin-builder drafts only. | OPA/SBAC proof, accessibility tests, visual regression, template approval, rollback. |
| APIs / events | Generate OpenAPI/AsyncAPI/CloudEvents/Avro drafts and mocks before code. | Contract lint, compatibility, generated client tests, idempotency and error-profile evidence. |
| MicroFunctions | Generate candidate transaction definitions and step bindings; code only business gap. | Step tests, idempotency tests, policy decisions, audit/outbox, trace evidence. |
| Database / Flyway | Generate Flyway migration drafts and seed packages only. | Clean migrate, checksum, RLS tests, data classification, DBA review. |
| OPA / SBAC policy | Generate Rego drafts, policy input/output schema, and tests. | Allow/deny/step-up/human-review tests, fail-closed checks, approval matrix. |
| Prompts / guardrails | Generate prompt templates, guardrail configs, model-route aliases, eval cases. | LiteLLM route proof, guardrail results, red-team/eval output, forbidden-output checks. |
| CI/CD and evidence | Generate pipeline draft, evidence schema, GitNexus mapping, PR templates. | Build/test/scan/SBOM/provenance/architecture fitness evidence. |

# 8. DevSecOps, GitNexus, and Evidence Gates

Every System Builder candidate must produce a PR/MR-ready evidence pack. GitNexus remains read-only and derivative. It may provide code maps, impact analysis, affected tests, and architecture drift indicators; it must not commit, merge, approve, deploy, mutate runtime state, or replace tests, scans, or human review.

Minimum gates: build, unit, component, contract, OPA/Rego, Flyway clean-migrate, SAST, SCA, secret scan, SBOM, provenance, authenticated DAST where applicable, architecture fitness, accessibility, and resilience checks.

Evidence pack contents: intake_id, agent_id/environment_id, source_ref, branch/commit, generated artifacts, policy decisions, test results, scan results, GitNexus report, telemetry plan, rollback/deactivation path, known limitations, and owner approvals.

Promotion is blocked when critical/high findings are unresolved, evidence is missing, generated artifacts bypass architecture boundaries, or rollback/deactivation is not defined.

# 9. Runtime Toggles, Observability, and Trace Reconstruction

Runtime toggles are configuration-governed controls, not informal switches. They may adjust diagnostic verbosity, sampling, feature activation, AI assistant availability, template activation, model route eligibility, or non-critical telemetry volume only when policy, audit, evidence, and rollback controls remain intact.
| Toggle Class | Allowed Use | Control Requirement |
| --- | --- | --- |
| Feature / template toggle | Enable, disable, pilot, or rollback non-production or approved production capability. | Owner, approval route, audit event, fallback state, evidence_ref. |
| Telemetry sampling | Reduce performance overhead for high-volume traces or logs. | Never disable protected-action audit, policy decision, or security evidence. |
| AI capability toggle | Disable prompt panel, model route, tool action, memory write, or agent delegation. | Fail closed, record reason, notify owner, preserve forensic evidence. |
| Environment diagnostic toggle | Temporarily increase logging/tracing during incident or test. | Time-bound, redacted, approved, observable, and reverted after review. |

# 10. Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop

The System Builder may support continuous improvement only through proposal-driven loops. It may detect issues, retrieve evidence, classify root cause, recommend remediation, draft candidate artifacts, run tests, and prepare PR/MR evidence. It must not silently mutate production, write authoritative standards, change policy, or promote code/configuration without approval.

Detect issue from logs, traces, metrics, errors, tickets, scans, GitNexus drift, or user feedback.

Retrieve governed evidence with classification and source authority validation.

Classify issue by severity, bounded context, risk tier, and affected artifact families.

Generate candidate fix, learning artifact, test addition, policy proposal, runbook update, or environment change in branch/sandbox.

Run deterministic tests, security checks, policy checks, contract checks, and evidence-pack validation.

Route through maker-checker, CODEOWNERS, ARB/CAB/Security/DBA where applicable.

Promote only after approval; monitor, compare expected behavior, and capture lessons learned.

# 11. RACI
| Activity | Architecture / IT Head | AI Governance | Security | DevSecOps / Platform | DBA / Data | QA/SDET / Audit |
| --- | --- | --- | --- | --- | --- | --- |
| Approve System Builder implementation pattern | A | C | C | C | C | C |
| Review AI agent definition and autonomy tier | A/R | R | R | C | C | C |
| Approve tool/MCP and model route | A | R | R | R | C | C |
| Review environment provisioning manifest | A | C | R | R | R | C |
| Validate CI/CD and evidence pack | A | C | C | R | C | R |
| Approve production-impacting change | A | C | R | R | R | C |
| Audit lifecycle and recertification evidence | C | C | C | C | C | A/R |

# 12. Acceptance Criteria

System Builder screens capture structured intake for agent creation and environment provisioning with owner, source, classification, risk tier, bounded context, approvals, and evidence path.

Agent creation produces registry-ready definitions, SBAC skills, OPA policy bindings, LiteLLM model-route references, guardrail bundles, tool manifests, tests, telemetry, certification evidence, kill switch, and retirement plan.

Environment provisioning produces manifest-driven setup artifacts, pinned toolchains, devcontainer/runner config, IaC/GitOps drafts, secret-path references, scan evidence, observability, rollback/rebuild plan, and approval records.

Generated outputs remain candidate artifacts until maker-checker review, CI/CD gates, policy checks, security validation, and AVCI evidence pass.

Dynamic Workspace, MicroFunction, API/event, database/Flyway, observability, security, DevSecOps, and change-management impacts are declared and validated before promotion.

No direct production credentials, direct provider SDK calls, unapproved tools, silent mutation, self-approval, or bypass of OPA/SBAC/guardrails is possible in the implementation path.

# 13. AVCI Compliance Summary
| AVCI Property | Required Evidence |
| --- | --- |
| Attributable | Document owner, request owner, maker, checker, approver, source baseline, agent/environment owner, branch, commit, and evidence path are recorded. |
| Verifiable | Contracts, tests, scans, policy decisions, GitNexus reports, registry records, telemetry, certification, and promotion evidence prove behavior. |
| Classifiable | All agent, environment, prompt, artifact, data, telemetry, and evidence records include classification and handling rules. |
| Improvable | Known limitations, rejected options, findings, recertification items, lessons learned, and improvement backlog entries are captured and tracked. |

# Appendix A. Agent Creation Intake Template
| Field | Required Value |
| --- | --- |
| agent_name / agent_id | <unique name and stable identifier> |
| purpose and non-goals | <what the agent may and must not do> |
| owner / backup owner | <named accountable humans> |
| classification ceiling | <Public/Internal/Confidential/Restricted eligibility> |
| skills and SBAC scope | <skill codes, action classes, environment scope, expiry> |
| model route and guardrails | <LiteLLM alias, guardrail policy, eval threshold> |
| tools / MCP / APIs | <manifest refs, allowed actions, dry-run, idempotency, rollback> |
| memory/RAG eligibility | <allowed sources, provenance, freshness, quarantine> |
| tests and evidence | <red-team, unit, policy, tool, blocked action, telemetry, rollback> |

# Appendix B. Environment Provisioning Manifest Template

environment_request_id: <id>
owner: <human owner>
target_environment: <dev/test/stage/prod>
classification: <classification and handling>
components: [repo, devcontainer, ci_cd, kubernetes, gitops, vault, database, observability, ai_runtime]
approved_sources: [golden_source_repo, approved_registry, package_mirror]
secrets_requirement: <Vault/OpenBao paths only; no secret values>
validation_required: [sbom, provenance, sast, sca, secret_scan, opa, dast, smoke_test, drift_check, restore_test]
approval_route: [architecture, security, devsecops, dba, cab]
rollback_or_rebuild: <destroy/rebuild, helm rollback, argocd rollback, restore, deactivation>

# Appendix C. PR/MR AVCI Summary Block

Request ID / Ticket / ADR/TDL:
Owner / maker / checker / approver:
AI assistance used and approved route:
Generated agent/environment artifacts:
Classification and handling:
SOLID / Clean Architecture / DDD impact:
Security / SBAC / OPA / guardrail impact:
Tests, scans, policy checks, and evidence links:
Observability and audit evidence:
Rollback / forward-fix / compensation / deactivation:
Known limitations and improvement backlog:

