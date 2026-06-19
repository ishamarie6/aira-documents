---
title: "System Builder Operating Manual and Maker Checker Runbook"
doc_id: "AIRA-73"
version: "v1.0"
status: "final"
category: "System builder operating manual"
source_docx: "AIRA_73_System_Builder_Operating_Manual_and_Maker_Checker_Runbook_v1.0.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 73-system-builder-operating-manual
  - final
  - aira-73
---



# System Builder Operating Manual and Maker Checker Runbook



AIRA
AI-Native Enterprise Platform

System Builder Operating Manual and Maker-Checker Runbook

AIRA-DOC-073
Version v1.0

Controlled Intake | Analysis | Candidate Generation | Human Review | Evidence Packs | Governed Promotion | No Silent Mutation
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-073 |
| Document Title | AIRA System Builder Operating Manual and Maker-Checker Runbook |
| Version | v1.0 |
| Status | Draft for Architecture Review Board / CAB / Engineering / Security / DevSecOps / AI Governance Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; DevSecOps Lead; Software Development Lead; Security Architecture; QA/SDET; Platform Engineering; SRE; DBA; AI Governance; Internal Audit |
| Primary Audience | System Builder operators; developers; reviewers; DevSecOps; Security; QA/SDET; Platform Engineering; AI agent owners; Internal Audit; CAB/ARB reviewers |
| Primary Alignment | AIRA 00E, 01A, 01, 01B, 02, 03, 10-10E, 11, 11A, 20, 42, 43, 61, 62-72 |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / System-Builder-Operating-Manual / 73 / v1.0 / |

Mandatory Practice Statement

System Builder is a governed change-generation control plane, not an autonomous production authority. It may intake, analyze, recommend, draft, generate candidate artifacts, prepare evidence, and create reviewable PR/MR packages. It must not approve its own output, bypass OPA/SBAC/guardrails, mutate production silently, create uncontrolled agents, weaken evidence, or promote changes without maker-checker review and AVCI proof.

# Static Table of Contents

1. Executive Summary

2. Purpose, Scope, and Authority

3. Operating Principles

4. Controlled Intake and Classification

5. System Builder Lifecycle

6. Maker-Checker Review Model

7. Tool-Action and Credential Boundaries

8. Generated Artifact Control

9. Evidence Pack and Manifest Requirements

10. MicroFunction and Dynamic Workspace Integration

11. AI Agent Lifecycle and Model Route Controls

12. Promotion, Activation, Rollback, and Runtime Operations

13. RACI and Separation of Duties

14. Validation Checklist, Acceptance Criteria, and Anti-Patterns

15. Implementation Roadmap, Reconciliation Items, and AVCI Summary

# 1. Executive Summary

This operating manual formalizes how AIRA System Builder is used as a disciplined engineering factory for controlled change generation. It converts AIRA governance standards into an operational runbook for intake classification, impact analysis, recommendation, candidate generation, evidence assembly, maker-checker review, PR/MR packaging, promotion readiness, activation, monitoring, and improvement.

The operating outcome is explicit: System Builder accelerates governed delivery without becoming authority. All outputs remain draft, review-ready, PR/MR-ready, change-ready, deployable, active, deprecated, retired, or revoked based on evidence and approval state. AI can recommend and generate, but humans own risk acceptance and production authority.
| Executive Requirement | Operating Rule |
| --- | --- |
| Analyze before generation | Every request is classified, scoped, risk-tiered, and impact-analyzed before candidate artifacts are created. |
| Recommend before action | System Builder proposes options, evidence needs, affected artifacts, tests, risks, and rollback path before generation or promotion. |
| Generate only controlled candidates | Generated code, configuration, policies, migrations, prompts, guardrails, agents, and runbooks remain draft until reviewed. |
| Validate by evidence | CI/CD, GitNexus, tests, scans, OPA/SBAC, observability, PRR/ORR, and evidence manifest are mandatory where applicable. |
| Activate only through governance | Promotion requires PR/MR, maker-checker review, CODEOWNERS, ARB/CAB/security/DBA approval where required, and rollback readiness. |

Figure 1. System Builder Operating Control Plane

# 2. Purpose, Scope, and Authority

## 2.1 Purpose

Define the approved operating model for System Builder intake, analysis, recommendation, candidate generation, validation, review, promotion, and monitoring.

Prevent uncontrolled automation, evidence-free generation, AI self-approval, unmanaged agent creation, and direct production mutation.

Standardize maker-checker, CODEOWNERS, GitNexus, Evidence Manifest, PRR/ORR, Resilience Lab, AI certification, and Policy-as-Code integration.

Provide an operational runbook that can be implemented in repositories, CI/CD pipelines, System Builder workflows, Dynamic Workspace admin flows, and evidence stores.

## 2.2 Scope
| In Scope | Out of Scope |
| --- | --- |
| Requirements, operational evidence, improvement requests, AI agent lifecycle, and DevSecOps provisioning intake. | Direct production mutation by AI, agents, notebooks, scripts, System Builder, or local tools. |
| Generated candidate artifacts: code, tests, policies, prompts, guardrails, OpenAPI/AsyncAPI, Flyway, runtime config, runbooks, evidence packs. | Self-approval, bypassing branch protection, bypassing CI/CD, disabling evidence, bypassing OPA/SBAC, or weakening guardrails. |
| PR/MR packaging, GitNexus read-only impact analysis, evidence manifest assembly, PRR/ORR readiness, resilience evidence, AI route certification. | Unapproved technologies, direct model-provider calls, direct Git/CI/CD/Kubernetes/database credentials in agents. |

## 2.3 Authority and Precedence
| Level | Authority | System Builder Meaning |
| --- | --- | --- |
| L0 | ARB / CAB / Security Governance / IT Head | Final authority for production-impacting, policy, data, security, runtime, and exception decisions. |
| L1 | 01A, 01, 01B, 02 | Enterprise principles, AVCI, evidence, and architecture boundaries govern all generated outputs. |
| L2 | 11, 11A, 20, 65, 66, 68 | DevSecOps, Policy-as-Code, evidence manifest, and control traceability gates determine acceptance. |
| L3 | 10-10E, 54-61, 67, 69, 70, 71, 72 | Domain-specific controls for MicroFunction, Dynamic Workspace, API/event, AI, data, secure design, and golden paths. |
| L4 | System Builder runs, PR/MR records, CI/CD reports, evidence packs | Operational proof only; may not override governing standards. |

# 3. Operating Principles
| Principle | Mandatory Operating Meaning |
| --- | --- |
| Discipline first | System Builder must follow controlled intake, classification, owner assignment, approval path, and evidence planning before automation. |
| Automation second | Automation executes predefined, policy-governed tasks and never silently expands its own authority. |
| Intelligence third | AI reasoning supports analysis, drafting, recommendations, and evidence summarization, but is not authority. |
| AVCI always | Every generated artifact has owner, source, intent, version, classification, verification evidence, approval state, and improvement path. |
| Fail closed | Missing identity, policy, guardrail, model route, audit, secrets control, evidence store, or Harness access blocks protected actions. |
| Progressive autonomy | Automation maturity increases only through evidence, trust tier, risk tier, test success, monitoring, rollback, and approval. |

# 4. Controlled Intake and Classification

Every System Builder request must be routed into one controlled intake domain. A request may belong to more than one domain; the highest risk and strictest control governs.
| Intake Domain | Required Classification and Evidence |
| --- | --- |
| New Requirement | Business/system/workflow/MicroFunction/config/UI/API/database/policy/integration scope, owner, acceptance criteria, risk, rollback, and test plan. |
| Operational and Engineering Evidence | Logs, traces, metrics, screenshots, incidents, scans, failed tests, alerts, user feedback, and support tickets treated as classified diagnostic evidence. |
| Improvement Request | Auto-Heal, Auto-Learn, Auto-Improve, refactoring, reliability, performance, security, observability, UX, or technical debt candidate with measurable benefit and rollback. |
| AI Agent Lifecycle | Purpose, owner, skills, SBAC, OPA, model route, tool scope, trust tier, evaluation, monitoring, suspension, retirement, and evidence. |
| AI DevSecOps Provisioning | Infrastructure/tool/library/container/devcontainer/pipeline/policy/secret path/model route/environment setup manifest with rebuild and rollback evidence. |
| Mandatory Intake Fields | Examples |
| --- | --- |
| intake_id, source_ref, requester, accountable_owner | Ticket, incident, PR/MR, Git commit, OpenKM source, approved meeting note. |
| classification, data handling, model route eligibility | Internal, Confidential, Restricted, Evidence-Sensitive; redaction and retention rules. |
| bounded_context, affected_contracts, affected_policies | MicroFunction transaction, OpenAPI/AsyncAPI, Flyway migration, OPA policy, runtime config. |
| risk_tier, approval_route, evidence_plan | Low/Medium/High/Critical; CODEOWNERS; Security/DBA/ARB/CAB; evidence pack. |

# 5. System Builder Lifecycle
| Stage | Allowed Output | Required Gate |
| --- | --- | --- |
| 1. Intake | Classified request record; missing information checklist. | Owner, scope, classification, bounded context, and risk tier are mandatory. |
| 2. Analysis | Impact analysis, affected artifacts, contracts, tests, policies, evidence needs, reconciliation items. | GitNexus and source-reference check where applicable. |
| 3. Recommendation | Options, preferred path, risk, approval path, effort, rollback, acceptance criteria. | Human approval required before generation for material changes. |
| 4. Candidate Generation | Draft code/config/tests/policies/prompts/runbooks/migrations/diagrams/evidence manifest. | Generated outputs stored in branch/sandbox only. |
| 5. Validation | CI/CD gate results, policy results, scans, tests, architecture fitness, evidence manifest. | Blocking defects stop promotion; waivers must be risk-owned and time-bound. |
| 6. Maker-Checker Review | Independent review comments, CODEOWNERS, Security/QA/DBA/AI Governance approvals where required. | Maker cannot check or approve own output. |
| 7. PR/MR Packaging | PR/MR summary, AVCI evidence, rollback path, affected standards, generated artifact list. | PR/MR remains draft until evidence complete. |
| 8. Promotion and Activation | Release candidate, active runtime config, deployment, cache invalidation, monitoring. | CAB/ARB/owner approval and PRR/ORR gate where required. |
| 9. Monitoring and Improvement | SLO, audit, telemetry, incident link, improvement backlog, lesson learned. | Post-promotion monitoring required for material changes. |

Figure 2. Maker-Checker Lifecycle for System Builder Outputs

# 6. Maker-Checker Review Model
| Role | Accountability | Prohibited |
| --- | --- | --- |
| Maker | Creates or prepares candidate artifact, evidence manifest, generated output list, and proposed tests. | Approving own output, merging protected branch, accepting residual risk alone. |
| Checker | Verifies source, design, tests, evidence, security, policies, architecture, and rollback. | Acting as checker when they authored material output. |
| Approver | Accepts risk and authorizes promotion within delegated authority. | Approving without evidence pack, bypassing CAB/ARB/security triggers. |
| Operator | Executes approved deployment, activation, rollback, or safe-disable. | Executing unapproved change or silent production mutation. |
| Auditor | Reviews evidence, lineage, exceptions, and control effectiveness. | Becoming delivery bottleneck for normal approvals unless audit gate is triggered. |

## 6.1 Review Severity Model
| Severity | Meaning | Disposition |
| --- | --- | --- |
| Advisory | Improvement or clarity issue that does not weaken controls. | Capture in backlog or incorporate in PR/MR. |
| Warning | Risk exists; not production-blocking if accepted by owner. | Owner acknowledgement and follow-up evidence required. |
| Blocking | Merge, activation, or promotion prohibited until fixed or waived. | Required authority and remediation evidence. |
| Critical Block | Material security, production, data, policy, or evidence failure. | Escalate to Security/ARB/CAB; no promotion. |

# 7. Tool-Action and Credential Boundaries

System Builder actions must be mediated. Agents and AI assistants must not receive direct credentials to Git, CI/CD, Kubernetes, databases, workflow engines, secrets stores, model providers, production APIs, OpenKM, or runtime configuration stores. Harness or an approved tool gateway executes policy-authorized actions and produces audit evidence.

Figure 3. Tool-Action Boundary and Prohibited Direct Actions
| Action Type | Allowed Through System Builder | Required Control |
| --- | --- | --- |
| Read-only analysis | Source search, GitNexus impact, evidence retrieval, trace/log summary, policy/test review. | Classification, source_ref, freshness, redaction, evidence_ref. |
| Candidate generation | Code, tests, config, policies, prompts, guardrails, diagrams, runbooks, PR/MR draft. | Branch/sandbox only; generated artifact manifest; human review. |
| Tool invocation | CI rerun, GitNexus analysis, ticket creation, non-prod validation, evidence pack assembly. | Harness/SBAC/OPA decision, audit, no privileged direct credentials. |
| Runtime or production action | Only after approved change path and through deployment/activation controls. | ARB/CAB/security/owner approval, rollback, monitoring, evidence pack. |

# 8. Generated Artifact Control
| Artifact Type | Generation Rule | Evidence Required |
| --- | --- | --- |
| Code and tests | Generate in branch/sandbox; preserve Clean Architecture, ports/adapters, MicroFunction boundaries. | Generated file list, tests, architecture fitness, AI-use declaration, reviewer. |
| Database/Flyway | Generate migration candidates only; no manual production DDL. | Flyway validate/migrate, checksum, rollback/forward-fix, DBA review. |
| API/event contracts | Generate OpenAPI/AsyncAPI/schema before implementation. | Contract diff, compatibility test, consumer impact, schema owner. |
| Policies/guardrails | Generate Rego/Conftest/guardrail candidates with tests. | Policy tests, deny-by-default proof, decision log sample, security review. |
| Runtime configuration | Generate draft configuration with version, owner, classification, activation and rollback path. | Publish-time validation, OPA/SBAC, cache invalidation plan, activation evidence. |
| AI agents/tools | Generate manifest only; no uncontrolled agent. | Agent owner, skill scope, model route, tool permissions, evaluation, suspension path. |
| Documents/runbooks | Generate controlled drafts with source_refs, status, version, owner, and supersedence. | 00E register update, review path, classification, approval state. |

# 9. Evidence Pack and Manifest Requirements

Every material System Builder run must produce or update a machine-readable run manifest that links intake, generated artifacts, validation evidence, approval state, runtime activation, and improvement backlog.
| Manifest Section | Required Fields |
| --- | --- |
| builder_run | builder_run_id, intake_id, owner, maker, checker, run_timestamp, model_route, tools_used, source_refs. |
| classification | artifact_classification, data_classification, evidence_classification, retention_rule, redaction_profile. |
| generated_artifacts | artifact_id, type, path, hash, status, source_template, parent_standard, target_repository. |
| validation | tests, scans, policy_results, architecture_fitness, contract_checks, GitNexus_refs, evidence_pack_id. |
| approval | maker, checker, approver, CODEOWNERS, Security/DBA/QA/AI Governance/ARB/CAB status. |
| promotion | target_environment, release_id, PRR_ORR_result, rollback_path, monitoring_plan, activation_status. |
| improvement | known_limitations, backlog_refs, lessons_learned, Auto-Heal/Learn/Improve candidates. |

## 9.1 Minimum System Builder Run Record

{
  "builder_run_id": "sb-2026-0001",
  "intake_id": "REQ-0001",
  "owner": "Solutions Architecture Office / IT Head",
  "classification": "INTERNAL CONFIDENTIAL",
  "risk_tier": "medium",
  "model_route": "approved-gateway-route-alias",
  "tools_used": ["gitnexus-readonly", "ci-evidence-validator"],
  "generated_artifacts": [{"path": "services/example", "status": "draft", "hash": "sha256:..."}],
  "gates": {"policy": "pass", "tests": "pass", "security": "pending", "evidence": "pass"},
  "approval_state": "review-ready",
  "rollback_path": "feature-disable + revert PR + config rollback",
  "evidence_pack_id": "EP-0001"
}

# 10. MicroFunction and Dynamic Workspace Integration
| Area | System Builder Obligation |
| --- | --- |
| MicroFunction | Reuse standard catalog steps first; generate STP-BUS only by approved gap; enforce identity, classification, validation, OPA/SBAC, idempotency, audit, observability, outbox, DLQ/replay, rollback. |
| Runtime configuration | Generate draft runtime definitions with owner, version, classification, publish-time validation, signature/hash, cache invalidation, rollback/safe-disable. |
| Dynamic Workspace | Generate UI/template candidates only when backend MicroFunction, API contract, policy filter, telemetry, accessibility, evidence, and rollback are defined. |
| AI Assistant Panel | Route all model traffic through approved gateway, guardrails, classification, source citation rules, retention controls, and tool-action policy. |
| Golden paths | Prefer AIRA reference implementations before custom patterns; deviations require ADR/TDL or waiver. |

# 11. AI Agent Lifecycle and Model Route Controls
| Lifecycle Stage | Required Control |
| --- | --- |
| Proposed | Purpose, owner, use case, data classification, skill scope, tools, model route, risk tier, success metrics. |
| Evaluated | AI certification, red-team/abuse-case tests, guardrail tests, retrieval tests, tool-action simulations, evidence pack. |
| Approved | Named owner, OPA/SBAC policy, LiteLLM/private gateway route, monitoring, kill-switch, suspension criteria. |
| Active | Runtime telemetry, audit, cost/latency/error metrics, policy decisions, tool-action evidence, user feedback. |
| Suspended | Triggered by failed evaluation, incident, policy violation, unsafe output, drift, data issue, or owner request. |
| Retired | Revoked from registry, routes disabled, evidence retained, lessons captured, downstream references updated. |

# 12. Promotion, Activation, Rollback, and Runtime Operations
| Gate | Required Evidence |
| --- | --- |
| PR/MR Gate | AVCI summary, generated artifact list, AI-use declaration, tests/scans, GitNexus impact, evidence manifest, rollback plan. |
| CI/CD Gate | Build, tests, contracts, policies, architecture fitness, security scans, SBOM/provenance, evidence pack completeness. |
| PRR/ORR Gate | Operational readiness, dashboards, alerts, runbooks, support model, rollback/safe-disable, incident path. |
| Resilience Gate | Idempotency, concurrency, outbox/inbox, DLQ/replay, recovery, failure injection, performance evidence. |
| Activation Gate | Approvals, signed/hash runtime definition, cache invalidation, audit event, monitoring window, release record. |
| Rollback Gate | Revert PR, config rollback, feature disablement, compensation, replay/reprocess, restore/rebuild, post-incident evidence. |

## 12.1 Runtime Status Model
| Status | Meaning |
| --- | --- |
| Draft | Generated or authored candidate not yet reviewed. |
| Review-Ready | Evidence and validation prepared for checker review. |
| PR/MR-Ready | Branch-bound with required checklist and evidence manifest. |
| Deployable | All required gates passed but not yet active. |
| Active | Approved and promoted artifact/runtime configuration is in effect. |
| Suspended | Temporarily disabled due to defect, incident, risk, or policy failure. |
| Deprecated | Still usable during transition but no longer preferred. |
| Retired/Revoked | No new use; retained for lineage, audit, and rollback reference. |

# 13. RACI and Separation of Duties
| Activity | IT Head / Architect | System Builder Operator | DevSecOps | Security | QA/SDET | DBA/Platform | AI Governance | Audit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Define operating policy | A/R | C | C | C | C | C | C | I |
| Classify intake | A | R | C | C | C | C | C | I |
| Generate candidate | A | R | C | C | C | C | C | I |
| Review evidence | A | R | R | R | R | C | C | C |
| Approve high-risk change | A/R | I | C | R | C | C | R | I |
| Promote to production | A/R | I | R | C | C | C | C | I |
| Audit controls | C | I | C | C | C | C | C | A/R |

# 14. Validation Checklist, Acceptance Criteria, and Anti-Patterns

## 14.1 Validation Checklist
| Checkpoint | Pass Condition |
| --- | --- |
| Controlled intake | intake_id, owner, source_ref, classification, bounded context, risk, acceptance criteria. |
| Analysis | Affected contracts, policies, schemas, services, tests, evidence, and reconciliation items identified. |
| Generation control | Candidate generated only after approved recommendation path; stored in branch/sandbox. |
| Evidence | Evidence manifest links tests, scans, policy decisions, GitNexus, observability, rollback, approvals. |
| Maker-checker | Maker, checker, approver, and operator separation enforced for material changes. |
| Policy and security | OPA/SBAC, guardrails, secrets hygiene, DAST/security gates, AI route controls pass. |
| Promotion readiness | CI/CD, PRR/ORR, Resilience Lab, release, rollback, monitoring, and CAB/ARB triggers complete. |

## 14.2 Acceptance Criteria

System Builder cannot execute protected actions without policy, classification, audit, and evidence controls.

Generated artifacts are always labeled with lifecycle state and never treated as approved by default.

Every material System Builder run creates an evidence manifest and generated artifact manifest.

AI-generated code, tests, policies, prompts, guardrails, runbooks, and migrations are reviewed through PR/MR and CI/CD.

No agent or assistant has direct production credentials or direct authority to approve, merge, deploy, mutate, or disable controls.

Rollback, safe-disable, compensation, or rebuild path exists before activation of material change.

## 14.3 Anti-Patterns and Rejection Rules
| Anti-Pattern | Required Response |
| --- | --- |
| System Builder output is treated as approved because it looks complete. | Reject; require maker-checker review, tests, scans, evidence, and approval. |
| AI agent asks for direct Git, CI/CD, database, Kubernetes, workflow, secrets, or production credentials. | Reject; route through Harness/tool gateway with SBAC/OPA and audit. |
| Generated artifact bypasses MicroFunction, API contract, Flyway, OPA/SBAC, or observability standards. | Reject; refactor through governed architecture and evidence gates. |
| Auto-Heal directly patches production. | Block; convert to candidate PR/MR or approved runbook action with evidence and human approval. |
| Runtime toggle disables audit, policy, security, idempotency, outbox, or critical error evidence. | Reject; mandatory evidence controls are non-disableable. |

# 15. Implementation Roadmap, Reconciliation Items, and AVCI Summary

## 15.1 Implementation Roadmap
| Phase | Execution Focus | Exit Evidence |
| --- | --- | --- |
| Phase 0 | Adopt this operating manual; publish 00E register entry; define System Builder roles and lifecycle states. | Approved draft, RACI, register record, initial run manifest template. |
| Phase 1 | Add PR/MR templates, evidence manifest fields, generated artifact manifest, AI-use declaration. | Repository template and evidence pack examples. |
| Phase 2 | Connect System Builder to GitNexus read-only analysis, CI/CD evidence validator, Policy-as-Code gates. | Non-prod pilot with recorded evidence. |
| Phase 3 | Integrate MicroFunction, Dynamic Workspace, API/event, data governance, PRR/ORR, and Resilience Lab gates. | Golden path reference implementation passes gates. |
| Phase 4 | Implement agent registry, trust tiers, model-route certification, tool-action gateway, monitoring and suspension rules. | Certified low-risk agent actions with audit evidence. |
| Phase 5 | Quarterly control assurance, drift detection, waiver aging, stale-source checks, and improvement backlog. | Assurance report and updated 00E/00D reconciliation records. |

## 15.2 Open Reconciliation Items
| ID | Issue | Required Treatment |
| --- | --- | --- |
| RI-073-001 | 41B / 44 System Builder overlap remains a known baseline concern. | Use 00E and 00D to designate canonical governing source and supersedence path. |
| RI-073-002 | System Builder Lite versus full System Builder capability may blur authority. | Define trust tier, environment scope, and allowed actions for each deployment mode. |
| RI-073-003 | Agent registry, skill catalog, and SBAC policy schema require executable implementation. | Create machine-readable registry and policy bundle; link to AIRA-DOC-065 and AIRA-DOC-070. |
| RI-073-004 | Evidence manifest fields must be implemented in CI/CD tools. | Use AIRA-DOC-066 schema and AIRA-DOC-020 pipeline templates as executable baseline. |

## 15.3 AVCI Compliance Summary
| AVCI Property | How This Runbook Satisfies It |
| --- | --- |
| Attributable | Defines owner, co-owners, maker/checker/approver/operator/auditor roles, source_refs, generated artifact manifest, and run IDs. |
| Verifiable | Requires impact analysis, tests, scans, policy decisions, CI/CD evidence, GitNexus, PRR/ORR, Resilience Lab, AI certification, and approval proof. |
| Classifiable | Requires classification of intake, source, prompts, evidence, generated artifacts, tool actions, model routes, retention, and redaction. |
| Improvable | Links findings, incidents, failed gates, waivers, drift, runtime telemetry, and audit observations to Auto-Heal/Learn/Improve candidate loops. |

Final Rule: System Builder may accelerate AIRA delivery only when every generated output remains governed, reviewed, evidence-producing, reversible, and human-accountable. AI is not authority. AVCI is mandatory.

