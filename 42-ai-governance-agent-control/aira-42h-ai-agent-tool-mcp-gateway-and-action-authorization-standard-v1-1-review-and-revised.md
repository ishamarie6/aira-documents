---
title: "AI Agent Tool MCP Gateway and Action Authorization Standard"
doc_id: "AIRA-42H"
version: "v1.1"
status: "revised"
category: "AI governance and agent control"
source_docx: "AIRA_42H_AI_Agent_Tool_MCP_Gateway_and_Action_Authorization_Standard_v1_1_Review_and_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 42-ai-governance-agent-control
  - revised
  - aira-42h
---



# AI Agent Tool MCP Gateway and Action Authorization Standard



AIRA

AI-Native Enterprise Platform

AIRA AI Agent Tool/MCP Gateway and Action Authorization Standard

Controlled Tool Invocation | MCP Governance | Harness-Mediated Execution | OPA/SBAC Decisions | Runtime Evidence | Rollback Readiness
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-042H |
| Recommended Version | v1.1 - Review, Alignment, and Tool/MCP Execution Control Update |
| Status | Draft for Architecture, Security, AI Governance, DevSecOps, Platform Engineering, QA/SDET, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Review Date | 2026-06-17 |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / AI-Governance / Tool-MCP-Gateway / v1.1/ |

Configure First - Tool Through Gateway - Policy Before Execution - Human Approval Where Required - Evidence Always - Fail Closed

# Document Control
| Control Field | Value |
| --- | --- |
| Document Title | AIRA AI Agent Tool/MCP Gateway and Action Authorization Standard |
| Document ID | AIRA-DOC-042H |
| Version | v1.1 - Review, Alignment, and Tool/MCP Execution Control Update |
| Source Document Reviewed | 42H-AIRA_AI_Agent_Tool_MCP_Gateway_and_Action_Authorization_Standard_v1.0.docx |
| Supersedes | 42H v1.0 draft candidate, subject to ARB / Security / AI Governance approval |
| Document Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Security Architecture; AI Governance; DevSecOps Lead; Platform Engineering; Software Development Lead; QA/SDET; SRE / Operations; Internal Audit |
| Target Audience | Enterprise Architects; Security Architects; AI Governance; Platform Engineering; DevSecOps; Software Developers; QA/SDET; SRE; Internal Audit; System Builder operators; AI Agent owners |
| Classification | INTERNAL CONFIDENTIAL |
| Review Cadence | Monthly during AI agent rollout; quarterly after maturity; immediate review after tool/MCP change, security incident, policy change, autonomy change, model route change, or production-impacting automation change |
| Change Summary | Aligned 42H with the revised AIRA AI governance, MicroFunction, DevSecOps, CI/CD, security, observability, API, database/Flyway, GitNexus, and evidence baselines. Strengthened Tool/MCP manifest schema, action authorization contract, dry-run, idempotency, human approval, kill-switch, telemetry, and rollback controls. |

# Table of Contents Placeholder

Insert a Microsoft Word automatic Table of Contents here before final publication: References > Table of Contents > Automatic Table. Update field after final formatting.

# 1. Executive Review Summary

This v1.1 review confirms that the source 42H standard is directionally correct and should be retained as the governing AIRA standard for AI agent tool invocation, MCP server governance, connector authorization, and action execution control. The original document already establishes the critical principles: no direct tool execution, default-deny access, manifest-based registration, OPA/SBAC authorization, Harness-mediated execution, human approval for high-risk actions, auditability, and rollback readiness.

The improvement required is not a change of intent. It is an operational hardening update. Tool and MCP gateway rules must be stated as mandatory implementation controls that can be enforced by System Builder, CI/CD, runtime policy, telemetry, and review workflows. This revision converts 42H into a more implementation-ready standard for developers, platform engineers, AI agent owners, security reviewers, and future automation.
| Review Area | v1.1 Treatment |
| --- | --- |
| Governance posture | Retained and strengthened. Tools and MCP servers remain authority-transfer points, not developer conveniences. |
| Execution boundary | Clarified that agents request, gateway validates, OPA/SBAC decides, humans approve where required, Harness executes, and evidence records the outcome. |
| Tool manifest | Expanded into a minimum schema with owner, purpose, non-goals, classification ceiling, allowed actions, risk tier, input/output schema, policy, idempotency, dry-run, rollback, rate limit, and decommission path. |
| MCP governance | Strengthened source provenance, registry, exposed capability inventory, network scope, sandbox-first testing, hidden-tool denial, and prompt/resource separation. |
| Security and evidence | Added stronger requirements for secrets hygiene, egress control, DLP, audit, OpenTelemetry-style correlation, kill-switch scope, and AVCI evidence. |
| System Builder alignment | Clarified that System Builder may draft candidate tool manifests, policies, tests, and evidence packs but must not approve, activate, or execute production-capable tools. |

# 2. Source and Context Alignment
| Source / Standard | Required Alignment for 42H v1.1 |
| --- | --- |
| 42 AI Governance and Runtime Control Standard v1.2 | Parent AI governance authority; AI outputs remain advisory unless policy, evidence, classification, review, and reversibility requirements are met. |
| 42D AI Agent Identity Lifecycle v1.3 | Tool access depends on active agent identity, current owner, valid lifecycle state, credential hygiene, and recertification. |
| 42E Runtime Security Control Plane v1.3 | Runtime gateway, guardrails, KRIs, tripwires, assurance dashboard, and kill-switch controls must include tool/MCP actions. |
| 42F Autonomy Calibration v1.3 | Every tool action maps to autonomy risk tier T0-T5, trust tier, delegation boundary, and human handoff rule. |
| 42G Threat Model v1.1 | 42H converts tool/MCP abuse cases into executable manifest, policy, dry-run, idempotency, audit, and rollback controls. |
| 22A Prompt, Guardrail, Model Alias, and AI Evaluation Registry v1.2 | Tool-action prompts, model routes, guardrails, and evaluation packs must reference approved registry records and route eligibility. |
| 17 / 17A Security and Access Control | OPA/SBAC, least privilege, secrets handling, fail-closed control, no direct production credentials, and separation of duties govern execution. |
| 31A Observability and Evidence Correlation | Tool requests, decisions, approvals, executions, denials, rollbacks, and incidents must be reconstructable through trace, audit, evidence, and telemetry. |
| MicroFunction Baseline 10 v3.3 through 10E v1.2 | MicroFunction-generated or invoked actions must use governed adapters, idempotency, outbox/DLQ/replay where applicable, and evidence-producing runtime envelopes. |
| 11/11A and 20 DevSecOps / CI/CD Evidence Pack | Tool/MCP changes must pass PR/MR review, CI tests, SAST/SCA/secrets/IaC/container checks, policy tests, SBOM/provenance, and evidence-pack gates. |
| 19 GitNexus v1.3 | GitNexus may provide read-only impact analysis and evidence context; it must not commit, approve, merge, deploy, or mutate production. |

# 3. Review and Gap Analysis
| Finding Type | Assessment | v1.1 Correction |
| --- | --- | --- |
| Retain | The source document correctly treats tools and MCP servers as governed security boundaries. | Retained as mandatory principle. |
| Retain | Default-deny tool access, manifest registration, OPA/SBAC policy, Harness execution, and human approval are correct. | Retained and converted into explicit gateway lifecycle controls. |
| Strengthen | The source identifies manifest, schema, risk tier, dry-run, idempotency, rollback, and audit requirements, but some developer implementation expectations need more precision. | Added minimum schema, validation gates, evidence envelope, action lifecycle, and rejection rules. |
| Strengthen | MCP server supply-chain and hidden capability risks require more explicit treatment. | Added MCP provenance, hidden-tool denial, network allowlisting, sandbox-first testing, prompt/resource separation, and decommission controls. |
| Strengthen | Runtime toggles and observability need to distinguish performance tuning from disabling mandatory evidence. | Added rule: diagnostic verbosity and sampling may be tuned, but audit, policy decisions, security events, idempotency records, tool-action evidence, and critical incident evidence must not be disabled. |
| Simplify | Developers need an execution-oriented model rather than only governance language. | Added a concise lifecycle: Request, Normalize, Validate, Decide, Approve, Dry-run, Execute, Post-check, Evidence, Learn. |
| Add | System Builder and AI agents need explicit no-approval/no-production-mutation boundaries. | Added System Builder alignment and prohibited-use rules. |
| Add | Tests and certification must cover prompt injection, tool hijack, schema bypass, classification failure, policy denial, rollback, and kill-switch. | Added test matrix and CI/CD evidence gate expectations. |

# 4. Revised Full AIRA Document

## 4.1 Purpose

Define the official AIRA control model for AI agent tool, MCP, connector, API, workflow, data, CI/CD, repository, database, security, and infrastructure action invocation.

Prevent prompt-driven, model-driven, or agent-driven tool use from bypassing identity, SBAC, OPA, Harness, classification, guardrails, human approval, evidence, and rollback controls.

Define the minimum Tool/MCP Manifest and Action Authorization Contract required before any tool is exposed to AIRA agents, System Builder, or AI-assisted engineering workflows.

Support progressive autonomy while ensuring protected actions remain fail-closed, human-approved where required, observable, idempotent, and reversible or compensable.

Provide implementation-ready evidence, telemetry, testing, CI/CD, and review requirements for tool and MCP gateway governance.

## 4.2 Scope
| In Scope | Out of Scope |
| --- | --- |
| Tool registry, MCP registry, connector manifest, action schema, API tools, workflow tools, CI/CD tools, Git tools, database adapters, knowledge tools, ticket tools, evidence tools, identity/security tools, infrastructure actions, model tool-calling, dry-run, idempotency, rollback, audit, and evidence. | Unapproved autonomous production mutation; direct production credentials in agents; uncontrolled MCP server installation; direct model-provider tool calls outside approved route; replacing CAB/ARB/Security/DBA/QA review; treating this document as approval to create production-capable agents without companion governance. |
| DEV, TEST, UAT, STAGING, PROD, DR, and sandbox tool boundaries. | Agent self-approval, agent-to-agent approval chains for protected actions, unregistered tool use, shadow automation, or unmanaged browser/IDE/plugin execution paths. |

## 4.3 Mandatory Practice Statement

No AIRA AI agent may call a tool, MCP server, connector, API, script, workflow, repository, database, CI/CD function, infrastructure action, model-side tool, or production-facing adapter directly unless the call is routed through an approved Tool/MCP Gateway or equivalent Harness-mediated control plane.

Every tool action must be attributable to a verified human or agent identity, verifiable through policy and evidence, classifiable by data and operational risk, and improvable through monitoring, incident learning, recertification, and controlled revision.

Tool/MCP access is denied by default. A tool becomes invocable only when it has an approved manifest, owner, schema, classification ceiling, risk tier, OPA/SBAC policy, environment boundary, audit fields, timeout, rate limit, idempotency rule, rollback or compensation path, and human approval rule where required.

## 4.4 Authority and Precedence
| Level | Authority | Role |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance | Final authority for production, security, identity, data, tool, and high-risk autonomy exceptions. |
| L1 | AIRA AVCI, Architecture, AI Governance, Security, DevSecOps, Database, MicroFunction, and Change Governance | Universal evidence, security, architecture, rollback, policy, and improvement discipline. |
| L2 | This 42H Standard | Tool/MCP gateway, tool manifest, action authorization, policy contract, execution boundary, and evidence authority. |
| L3 | Tool Registry, MCP Registry, SBAC Catalog, OPA Policies, Harness, LiteLLM, Guardrail Registry, 42O/42P Registry | Executable control-plane implementation. |
| L4 | Tool requests, audit events, traces, PR/MR records, CAB tickets, evidence packs, incident records | Operational proof and audit history. |

## 4.5 Core Concepts and Non-Negotiable Rules
| Concept | AIRA Meaning |
| --- | --- |
| Tool | Any callable capability that can read, write, analyze, mutate, execute, query, retrieve, deploy, approve-request, or produce evidence. |
| MCP Server | A server or protocol adapter that exposes tools, resources, prompts, or external context to an agent. It is governed as a privileged action gateway. |
| Tool/MCP Gateway | The runtime control plane that validates tool manifests, action requests, identity, policy, classification, approval, execution, and evidence. |
| Harness Executor | The approved execution boundary that performs brokered tool actions after policy and approval gates pass. |
| Action Request | A structured request by a human or agent to invoke a tool with intent, parameters, scope, evidence, and risk metadata. |
| Action Result | The output, status, evidence, telemetry, post-check, and rollback/compensation reference produced by a tool action. |

Tools are not helpers; they are authority-transfer points.

Tool access is denied by default and granted only through manifest, SBAC, OPA, classification, and approval controls.

Agents must never receive raw production credentials or direct execution access to production systems.

Every mutating action must be idempotent, observable, evidence-producing, and reversible or compensable where feasible.

Unavailable identity, policy, secrets, guardrails, Harness, audit, or evidence controls block protected actions.

## 4.6 AIRA Tool/MCP Gateway Reference Architecture

The Tool/MCP Gateway is the governed runtime boundary between agent reasoning and external system action. It centralizes manifest validation, policy enforcement, rate limiting, credential brokerage, human approval routing, execution, telemetry, and rollback evidence.
| Layer | Primary Responsibility | Must Not Do |
| --- | --- | --- |
| Agent Runtime | Produce structured action requests with agent identity, intent, evidence, and constraints. | Call production tools directly or bypass the gateway. |
| Tool/MCP Gateway | Validate manifest, schema, classification, risk, policy, rate limits, and tripwires. | Act as a blind proxy or execute without policy evidence. |
| Policy Plane | Evaluate SBAC, OPA, classification, environment, human approval, trust tier, and separation of duties. | Fail open when controls are unavailable. |
| Approval Plane | Route high-risk actions to human checker, CAB, DBA, Security, Product Owner, or AI Governance. | Let agents approve themselves or each other. |
| Harness Executor | Broker credentials and execute approved actions through adapters. | Expose raw secrets to agents or prompts. |
| Evidence Plane | Record action, decision, approval, trace, result, rollback, retention, and evidence lineage. | Discard denied, failed, escalated, or rolled-back actions. |

## 4.7 Tool and MCP Registry Operating Model

All tools and MCP servers must be registered before use. Registration does not automatically approve execution; it only creates a reviewable control artifact.
| Registry Artifact | Required Purpose |
| --- | --- |
| Tool Manifest Registry | Records each tool, owner, risk tier, allowed agents, input/output schemas, classification ceiling, approval rule, idempotency, rollback, and audit profile. |
| MCP Server Registry | Records each MCP server, source, version, signing/provenance, exposed tools/resources/prompts, network scope, sandbox mode, and retirement path. |
| Action Authorization Policy | OPA/SBAC policy package that maps identity, skills, tool, action, data class, environment, autonomy tier, trust tier, approval, and evidence. |
| Tool Adapter Catalog | Defines approved adapters to Git, CI/CD, DB, ticketing, DMS, workflow, knowledge, evidence, security, identity, and infrastructure systems. |
| Approval Workflow Catalog | Maps action risk to human reviewer, maker-checker path, CAB/ARB, Security, DBA, Product Owner, or emergency-change gate. |

## 4.8 Tool Action Lifecycle
| Stage | Required Control | Evidence Produced |
| --- | --- | --- |
| Request | Agent or user submits structured action request with identity, intent, target, tool_id, action, classification, environment, and evidence_ref. | tool_action_request_id, agent_run_id, trace_id |
| Normalize and Classify | Gateway normalizes request, classifies data/environment/impact, and detects missing or unsafe parameters. | classification_result, risk_tier |
| Manifest Validation | Gateway validates tool exists, action exists, parameter schema, output schema, risk tier, environment, approval rule, and decommission state. | manifest_validation_result |
| Policy Decision | OPA/SBAC returns ALLOW, DENY, ESCALATE, DRY_RUN, or QUARANTINE with reason codes. | policy_decision_id |
| Human Approval | Required approver acts through controlled workflow where risk, production, secrets, identity, finance, destructive action, or Restricted data requires it. | approval_ref, SoD check |
| Dry-Run / Simulation | Mutating or high-risk actions run simulation where technically feasible before execution. | dry_run_result |
| Execute via Harness | Harness or approved adapter executes with scoped credentials, timeout, retry, circuit breaker, and rate limit. | execution_ref, credential_broker_ref |
| Post-Check | Gateway verifies outcome, detects partial failure, records rollback need, and emits evidence. | post_check_result |
| Rollback / Compensation | If needed, execute rollback, safe deactivation, forward-fix, compensation, or incident containment. | rollback_ref or compensation_ref |
| Learn and Improve | Denied, failed, escalated, incident, or anomalous results feed backlog, policy tests, trust score, and recertification. | improvement_ref |

## 4.9 Tool Manifest Minimum Schema
| Field | Required Content |
| --- | --- |
| tool_id | Unique governed identifier, e.g., TOOL-GIT-PR-CREATE-V1. |
| tool_name | Human-readable name. |
| tool_type | api, mcp, script, workflow, ci_cd, git, database, knowledge, evidence, ticket, infrastructure, identity, security, or model_tool. |
| tool_owner | Named accountable owner and backup owner. |
| manifest_version | Semantically versioned manifest. |
| status | Draft, Review, Approved, Active, Suspended, Retired, or Revoked. |
| business_purpose and non_goals | Approved purpose and explicit prohibited uses. |
| allowed_agents and actions | Agent IDs/classes and allowed action verbs. |
| risk_tier | T0 through T5, aligned to 42F. |
| classification_ceiling | Maximum data classification the tool may process or return. |
| environment_scope | DEV, TEST, UAT, STAGING, PROD, DR, sandbox. |
| input_schema_ref / output_schema_ref | Strict schema references. Unknown parameters must be denied. |
| opa_policy_ref / sbac_skill_required | OPA package/version and required SBAC skill. |
| approval_rule | none, owner, security, dba, devsecops, cab, arb, product_owner, compliance, or emergency-change path. |
| idempotency_rule | Required key or duplicate protection for mutating actions. |
| dry_run_supported | Required value and exception statement if false. |
| rollback_or_compensation | Rollback, forward-fix, safe deactivation, compensation, restore, or replay plan. |
| rate_limit / timeout_and_retry | Per actor/agent/environment/window limits plus timeout, retry, bulkhead, and circuit breaker. |
| audit_profile | Required evidence fields, retention, redaction, and audit sink. |
| decommission_path | Disable, revoke, retire, deny-test, and evidence-retain steps. |

## 4.10 OPA/SBAC Action Authorization Contract

The gateway must produce deterministic policy input and must not execute protected actions unless the OPA/SBAC decision permits it. OPA unavailability or unknown policy version is fail-closed for protected actions.
| OPA Input Group | Minimum Fields |
| --- | --- |
| Actor | user_id, role, skills, tenant, branch/unit, auth_strength, approval authority, conflict-of-interest flags. |
| Agent | agent_id, agent_version, lifecycle_state, owner, trust_tier, autonomy_level, classification_ceiling, recertification_state. |
| Tool | tool_id, tool_action, risk_tier, tool_owner, environment_scope, classification_ceiling, manifest_version, decommission_state. |
| Request | intent, target_resource, parameters_hash, idempotency_key, evidence_ref, ticket_or_change_ref, requested_environment. |
| Data | classification, data_owner, tenancy, retention, redaction_required, export_or_egress flag. |
| Runtime | model_alias, prompt_id, guardrail_id, threat_model_id, abuse_case_id, trace_id, assurance_state. |
| Approval | required_approver_role, approval_ref, SoD result, CAB/ARB/security/DBA record where applicable. |
| Evidence | audit_sink_available, evidence_path, rollback_ref, dry_run_result, post_check_required, retention_rule. |
| OPA Decision | Meaning | Required Treatment |
| --- | --- | --- |
| ALLOW | Action may execute within approved scope. | Harness executes; evidence captured; post-check required. |
| DENY | Action is not permitted. | No execution; audit; alert where required. |
| ESCALATE | Human approval or specialist review is required. | Route to Flowable/CAB/Security/DBA/Owner; no execution until approved. |
| DRY_RUN | Simulation is required before execution. | Run safe dry-run; evaluate result before actual action. |
| QUARANTINE | Request, context, tool, or source is unsafe. | Block execution; quarantine artifact; notify Security/AI Governance. |

## 4.11 Tool Risk Tiering and Approval Matrix
| Tier | Examples | Default Decision | Approval Requirement |
| --- | --- | --- | --- |
| T0 Informational | Read static docs, list local test files, summarize approved knowledge. | Allow if classified and logged. | No approval; reviewer required before source promotion. |
| T1 Read-only Operational | Read logs, query non-sensitive metrics, inspect PR diff, read test evidence. | Allow or dry-run if manifest-approved. | Owner approval for Restricted or production evidence. |
| T2 Candidate Generation | Create branch draft, generate config, draft migration, draft policy, draft test. | Allow only in branch/sandbox. | PR/MR review required. |
| T3 Controlled Mutation in Non-Prod | Run test pipeline, update sandbox ticket, execute non-prod workflow. | Dry-run then allow if policy approves. | DevSecOps or owner approval. |
| T4 High-Risk / Production Request | Production read connector, deployment request, access review workflow, credential rotation request. | Escalate by default. | Human approval by Security/CAB/DBA/Product Owner as applicable. |
| T5 Human-Controlled / Prohibited for Autonomy | Production mutation, delete data, rotate production secrets, approve access, deploy to production, change policy. | Block or human-only. | CAB/ARB/Security approval; no full agent autonomy. |

## 4.12 MCP Server Governance

MCP servers are treated as tool containers and attack surfaces. They may expose multiple tools, resources, and prompt templates; therefore their risk is the aggregate of all exposed capabilities.
| MCP Control | Mandatory Requirement |
| --- | --- |
| Source and Provenance | Approved source, repository, version, checksum/signature, SBOM where applicable, and owner approval. |
| Exposed Capability Inventory | List every tool, resource, prompt, template, and dynamic capability exposed by the server. Hidden dynamic tools are prohibited. |
| Network Boundary | Outbound destinations, inbound access, and environment scope are allowlisted and audited. Internet egress requires approval and DLP controls. |
| Sandbox First | MCP server must be evaluated in sandbox before non-prod or production exposure. |
| Schema Validation | All tool calls require strict input/output schemas and deny unknown parameters. |
| Prompt/Tool Separation | Retrieved content and tool outputs must not become tool instructions unless explicitly transformed through governed policy. |
| Secret Handling | MCP server may retrieve secrets only for execution through approved runtime; secret values must not be exposed to agent prompt context. |
| Rate and Cost Limits | Tool call quotas, timeout, retries, concurrency, token/cost limits, and circuit breakers are mandatory. |
| Decommission Path | Each MCP server must have disable, revoke, retire, deny-test, and evidence-retention procedures. |

## 4.13 Data, Secret, Egress, and Environment Controls
| Control Area | Mandatory Treatment |
| --- | --- |
| Data Classification | Tool input, output, logs, artifacts, prompts, memory exposure, and evidence inherit classification and handling rules. |
| Secrets | Agents and models never receive raw secret values. Harness or secret broker provides scoped credentials only at execution time. |
| Egress | External API calls, webhooks, MCP network access, and data export require allowlist, DLP, classification, and audit controls. |
| Environment Segregation | DEV/TEST/UAT/STAGING/PROD/DR credentials, endpoints, tool scopes, and policy packages remain isolated. |
| Prompt and Output Safety | Tool results must be redacted, classified, and filtered before any model-context reuse. |
| Production Boundary | Production tool actions require explicit human approval and cannot be triggered solely by model output. |

## 4.14 Idempotency, Dry-Run, Rollback, and Compensation
| Requirement | AIRA Rule |
| --- | --- |
| Idempotency | Every mutating action must have an idempotency key, natural duplicate protection, dedupe registry, or replay-safe design. |
| Dry-Run | High-risk or production-impacting actions require dry-run/simulation where technically feasible. Exceptions require documented waiver and approval. |
| Pre-Check | Gateway must verify state before mutation, including policy, target version, resource lock, current environment, and rollback feasibility. |
| Post-Check | Gateway must verify expected result and detect partial failure. |
| Rollback | Rollback, safe deactivation, previous version restore, or disablement must be defined for reversible actions. |
| Compensation | When rollback is unsafe, define business compensation, forward-fix, replay, or manual recovery procedure. |
| Replay and DLQ | Event-producing tools must include replay and DLQ strategy aligned to Kafka/outbox and MicroFunction runtime controls where applicable. |
| Evidence | Dry-run, execution, post-check, rollback, and compensation all require evidence references. |

## 4.15 Runtime Tripwires and Kill Switches
| Tripwire | Required Action |
| --- | --- |
| Prompt injection indicator | Block or quarantine input; no tool execution; preserve evidence. |
| Tool not in manifest | Deny; create governance finding. |
| Invalid parameter schema | Deny; return safe error; audit. |
| Classification ceiling exceeded | Deny or escalate to authorized human. |
| Policy unavailable | Fail closed; no protected action. |
| Secret exposure risk | Block; rotate if exposure occurred; invoke incident process. |
| Unexpected egress | Block; quarantine tool/MCP server; notify Security. |
| Repeated denied actions | Throttle agent, reduce trust, trigger recertification. |
| Tool loop or cost spike | Circuit-breaker; disable tool class or agent route. |
| Partial failure | Stop, post-check, rollback/compensate, open incident if required. |
| Critical incident | Invoke 42K kill switch: disable agent, tool, MCP server, model route, workflow, or environment scope as required. |

## 4.16 Observability, Audit, and AVCI Evidence

Tool/MCP actions must be reconstructable without exposing secrets, raw sensitive prompts, raw customer data, or unsafe tool outputs. Logging and diagnostic verbosity may be adjusted for performance, but mandatory audit, security decisions, policy outcomes, guardrail outcomes, idempotency records, tool-action evidence, and critical incident evidence must not be disabled.
| Evidence Field | Required Meaning |
| --- | --- |
| tool_action_id | Unique identifier for the tool action request and result. |
| agent_id / agent_run_id | Agent identity and runtime instance. |
| actor_id | Human requester or approving actor. |
| tool_id / manifest_version | Tool and manifest used. |
| mcp_server_id / version | MCP server reference where applicable. |
| request_class and action_class | Controlled intake and delegated action taxonomy. |
| risk_tier and autonomy_tier | T0-T5 risk and agent autonomy classification. |
| classification and environment | Data and environment handling context. |
| parameters_hash | Hash of request parameters; raw secrets and PII not logged. |
| idempotency_key | Duplicate prevention proof for mutating actions. |
| opa_decision_id and sbac_skill_id | Authorization basis. |
| approval_ref | Human approval record where required. |
| dry_run_result_ref | Simulation evidence for high-risk actions. |
| execution_ref | Harness/adaptor execution reference. |
| post_check_ref | Outcome verification evidence. |
| rollback_or_compensation_ref | Recovery evidence. |
| trace_id / span_id | Telemetry reconstruction keys. |
| evidence_ref and retention_rule | AVCI evidence path and retention handling. |

## 4.17 Testing, Red Team, and Certification Gates
| Test Type | Minimum Required Coverage |
| --- | --- |
| Manifest validation tests | Unknown tool, unknown action, invalid schema, wrong environment, classification mismatch, missing owner, retired tool. |
| OPA/SBAC policy tests | Allow, deny, escalate, dry-run, quarantine, missing skill, expired grant, separation-of-duties conflict, production approval requirement. |
| Prompt injection tool tests | Malicious input tries to force tool call, override policy, expose secrets, change target, or bypass approval. |
| MCP safety tests | Unexpected exposed tool, hidden prompt/resource, network egress, stale server, unsigned artifact, and malicious connector behavior. |
| Idempotency and replay tests | Duplicate submission, retry after timeout, partial failure, outbox/DLQ/replay where applicable. |
| Rollback and compensation tests | Rollback path, safe deactivation, forward-fix, restore, manual compensation, incident escalation. |
| Observability tests | Logs, metrics, traces, audit events, dashboards, alerts, evidence correlation, and redaction. |
| Security tests | SAST, SCA, secrets, IaC, container, authenticated DAST, API security, abuse-case validation, SBOM/provenance. |
| Kill-switch tests | Disable agent, tool, MCP server, model route, tool class, workflow, or environment scope. |

## 4.18 System Builder, MicroFunction, and DevSecOps Alignment

System Builder may draft candidate tool manifests, MCP server records, OPA/SBAC policies, tests, evidence envelopes, adapter skeletons, and PR/MR summaries. It must not approve, activate, grant production access, execute production tools, alter production, or bypass maker-checker, CI/CD, CAB/ARB, Security, DBA, or AI Governance gates.

MicroFunction-backed tool actions must preserve ports/adapters, idempotency, retry safety, outbox/DLQ/replay where applicable, audit, observability, classification, policy, rollback, and evidence. Business MicroFunctions must not directly call databases, Kafka, Redis, OpenKM, model providers, CI/CD, or external systems outside governed adapters and tool gateways.

DevSecOps pipelines must validate tool/MCP manifests, schemas, OPA/SBAC policies, SBOM/provenance, source provenance, secrets hygiene, SAST/SCA/DAST where applicable, and evidence-pack completeness before activation.

## 4.19 Non-Negotiable Rejection Rules

Reject any unknown, unregistered, unowned, or retired tool/MCP server request.

Reject any tool without approved manifest, risk tier, schema, classification ceiling, approval rule, idempotency rule, audit profile, and decommission path.

Reject tool execution when the agent is not registered, not active, not recertified, or lacks required SBAC skill.

Reject protected actions when OPA returns deny, OPA is unavailable, policy version is unknown, or audit is unavailable.

Reject any execution path that exposes raw production credentials to an agent, prompt, model, log, UI, or user output.

Reject mutating actions that lack idempotency, duplicate protection, post-check, or rollback/compensation strategy.

Reject production, identity, policy, financial, data deletion, or deployment actions without required human approval.

Reject MCP servers that expose hidden tools, unreviewed prompt resources, unapproved egress, or unknown source/provenance.

Reject tool actions that cannot be monitored, audited, rolled back, compensated, disabled, or reconstructed through evidence.

## 4.20 RACI and Operating Responsibilities
| Activity | Architecture | Security | AI Governance | DevSecOps | Platform | Dev Lead | QA/SDET | Internal Audit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Approve 42H standard | A | R | R | C | C | C | C | I |
| Register tool/MCP manifest | C | C | C | R | R | C | C | I |
| Approve high-risk tool | A | R | C | R | C | C | C | I |
| Define OPA/SBAC policy | C | A/R | C | R | C | C | C | I |
| Review MCP supply chain | C | A/R | C | R | R | C | C | I |
| Approve production action | A/R | R | C | R | C | C | C | I |
| Run test and certification gates | C | C | C | R | C | C | A/R | I |
| Audit tool evidence | I | C | C | C | C | I | C | A/R |

## 4.21 Implementation Roadmap
| Phase | Focus | Exit Criteria |
| --- | --- | --- |
| R0 | Approve this standard and register 42H in 00D. | Document registered as active candidate and companion to 42D-42G. |
| R1 | Inventory existing tools and MCP candidates. | Tool/MCP inventory complete with owners and risk tiers. |
| R2 | Define Tool Manifest Registry and schema. | Manifest template approved; no tool activation without manifest. |
| R3 | Implement OPA/SBAC decision contract. | Policy tests pass for allow, deny, escalate, dry-run, and quarantine. |
| R4 | Implement Harness/tool adapter boundary. | Agents cannot call tools directly; brokered execution proof exists. |
| R5 | Add observability and evidence profile. | Tool action evidence appears in audit/evidence repository and 31A dashboards. |
| R6 | Run red-team and failure tests. | Prompt injection, tool hijack, MCP misuse, rollback, and kill-switch tests pass. |
| R7 | Pilot low-risk tools only. | T0-T2 tools operate with evidence and no production credentials. |
| R8 | Governed expansion. | Higher-risk tools require ARB/Security/CAB approval and recurring recertification. |

## 4.22 Acceptance Criteria and Definition of Done

All tools and MCP servers exposed to agents are registered with owner, purpose, risk tier, classification ceiling, environment scope, manifest version, evidence profile, and decommission path.

No agent has direct production tool credentials, direct production database access, direct deployment authority, direct merge authority, or direct approval authority for protected actions.

Every protected tool action has SBAC skill mapping and OPA policy decision evidence.

High-risk, destructive, production-impacting, identity-impacting, Restricted-data, financial, or irreversible actions require human approval.

Mutating actions include idempotency, timeout, retry, post-check, and rollback or compensation controls.

Tool outputs are redacted and classified before exposure to agent/model context.

Denied, escalated, failed, dry-run, rolled-back, and compensated actions are retained as audit evidence.

Gateway kill switches can disable an agent, tool, MCP server, model route, environment action, or tool class.

Policy, manifest, audit, guardrail, identity, secret broker, or Harness failure blocks protected actions.

Tool/MCP changes pass CI/CD, security scanning, policy tests, evaluation gates, and maker-checker review before activation.

## 4.23 AVCI Compliance Summary
| AVCI Property | 42H v1.1 Evidence Mechanism |
| --- | --- |
| Attributable | Every tool action links actor, agent, tool, owner, manifest, policy, approval, executor, and evidence reference. |
| Verifiable | Manifest validation, OPA/SBAC tests, dry-run, post-check, audit fields, rollback tests, kill-switch tests, and CI/CD evidence verify the control. |
| Classifiable | Tool input, output, environment, evidence, logs, prompts, memory exposure, and model-returned content carry classification and handling rules. |
| Improvable | Denied actions, incidents, red-team findings, drift, runtime metrics, rollback results, and recertification findings feed backlog, policy tests, and standard revisions. |

# 5. Simplification Recommendations

Keep the developer-facing version of 42H centered on one decision path: Register tool, validate manifest, evaluate policy, approve if required, execute through Harness, emit evidence, and recover if needed.

Use a single Tool Manifest template as the default intake form for every tool, MCP server, connector, CI/CD action, database adapter, API action, or workflow action.

Adopt a small initial risk-tier catalog for low-risk pilot tools before permitting high-risk or production-facing actions.

Represent OPA/SBAC decisions using five outcomes only: ALLOW, DENY, ESCALATE, DRY_RUN, and QUARANTINE.

Provide one copy-ready review checklist and one evidence envelope so developers and reviewers do not create inconsistent tool review formats.

# 6. Automation Recommendations
| Automation Area | Recommended Control |
| --- | --- |
| Tool Inventory | Generate and maintain tool_manifest.yaml records with owner, risk, schema, policy, approval, idempotency, rollback, and evidence metadata. |
| MCP Registry | Scan approved MCP server definitions, exposed capabilities, network scope, package versions, SBOM/provenance, and decommission states. |
| Manifest Validation | CI validates required fields, schema references, status, owner, risk tier, classification ceiling, and approved environment scope. |
| Policy Tests | OPA test suite covers allow, deny, escalate, dry-run, quarantine, abuse cases, and separation-of-duties rules. |
| Connector Drift | Compare registered tools to runtime-exposed tools; quarantine hidden or unregistered capabilities. |
| Evidence Validation | Check that every tool action emits trace_id, policy_decision_id, approval_ref, execution_ref, rollback_ref, and evidence_ref. |
| Runtime Monitoring | Alert on denied-action spikes, schema failures, unapproved egress, tool loops, cost spikes, and kill-switch activations. |
| Review Queue | Create review items for new tools, risk-tier changes, policy changes, MCP server updates, and incidents. |

# 7. Review Queue Control Register
| Seq | Document | Version Movement | Review Status | Action / Next Step |
| --- | --- | --- | --- | --- |
| 42 | 42 AI Governance and Runtime Control | v1.1 to v1.2 | Completed / Revised | Use as parent authority for the AI governance family. |
| 43 | 22A Prompt, Guardrail, Model Alias, and AI Evaluation Registry | v1.1 to v1.2 | Completed / Revised | Use as route, prompt, guardrail, and evaluation registry authority. |
| 44 | 42D Agent Identity Lifecycle and Credential Hygiene | v1.2 to v1.3 | Completed / Revised | Use before any tool authorization or credentialed action. |
| 45 | 42E Agent Runtime Security Control Plane | v1.2 to v1.3 | Completed / Revised | Use for runtime action monitoring, tripwires, and kill-switch. |
| 46 | 42F Agent Autonomy Calibration and Trust | v1.2 to v1.3 | Completed / Revised | Use for autonomy risk tier and trust scoring. |
| 47 | 42G Agent Threat Model and Abuse Case Control | v1.0 to v1.1 | Completed / Revised | Use threat IDs and abuse cases as 42H inputs. |
| 48 | 42H Agent Tool/MCP Gateway and Action Authorization | v1.0 to v1.1 | Completed / Revised | Current document. Use as tool/action execution control. |
| 49 | 42I Agent Memory, Context, and RAG Integrity | v1.0 to v1.1 | Next for Review | Review memory, context, retrieval eligibility, poisoning defense, quarantine, and evidence lineage next. |

# 8. Next Document Recommendation

The next AIRA document to review is 42I-AIRA_AI_Agent_Memory_Context_and_RAG_Integrity_Control_Standard_v1.0.docx. 42H governs tool/action invocation. 42I should be next because it governs the memory and retrieval layer that feeds the agent before tool actions occur, including context provenance, poisoning detection, retrieval eligibility, stale-source quarantine, memory retention, source citation, classification handling, and evidence lineage.

# 9. Change Log
| Version | Date | Owner | Summary of Change |
| --- | --- | --- | --- |
| v1.0 | 2026-06-16 | Solutions Architecture Office / IT Head | Initial Tool/MCP Gateway and Action Authorization Standard. |
| v1.1 | 2026-06-17 | AIRA Enterprise Architecture, Governance, AI DevSecOps, Security, and Documentation Review Board | Review, alignment, simplification, and implementation hardening update aligned to AI governance, MicroFunction, DevSecOps, CI/CD, GitNexus, security, observability, and evidence baselines. |

# Appendix A. External Reference Register
| Reference | Use in 42H v1.1 |
| --- | --- |
| Model Context Protocol Specification, 2025-06-18 | Authoritative context for MCP as a protocol that connects LLM applications to external data sources and tools. |
| NSA, Model Context Protocol Security Design Considerations for AI-Driven Automation, May 2026 | Security considerations for MCP-enabled automation, used to strengthen gateway, egress, provenance, and execution controls. |
| NIST AI RMF and NIST AI 600-1 Generative AI Profile | Risk management, governance, measurement, and control alignment for AI systems and generative AI. |
| OWASP Top 10 for LLM Applications 2025 and OWASP MCP Top 10 | Threat categories for prompt injection, tool misuse, supply-chain vulnerabilities, and MCP-specific security concerns. |
| OpenTelemetry GenAI Semantic Conventions | Telemetry field and event alignment for GenAI, model, agent, and tool-call observability. |

