---
title: "AI Agent Supply Chain MCP Plugin and Connector Governance Standard"
doc_id: "AIRA-42M"
version: "v1.1"
status: "revised"
category: "AI governance and agent control"
source_docx: "AIRA_42M_AI_Agent_Supply_Chain_MCP_Plugin_and_Connector_Governance_Standard_v1.1_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 42-ai-governance-agent-control
  - revised
  - aira-42m
---



# AI Agent Supply Chain MCP Plugin and Connector Governance Standard



AIRA

AI-Native Enterprise Platform

AI Agent Supply Chain, MCP, Plugin, and Connector Governance Standard

Agent Runtime Dependencies | MCP Governance | Plugin Control | Connector Risk | Provenance | SBOM | AVCI Evidence

Version v1.1 Revised | Draft for Architecture, Security, AI Governance, DevSecOps, Platform Engineering, and Internal Audit Review
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-042M |
| Canonical Filename | 42M-AIRA_AI_Agent_Supply_Chain_MCP_Plugin_and_Connector_Governance_Standard_v1.1_Revised.docx |
| Version | v1.1 Revised |
| Supersedes | 42M-AIRA_AI_Agent_Supply_Chain_MCP_Plugin_and_Connector_Governance_Standard_v1.0_FINAL.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Security Architecture; AI Governance; DevSecOps Lead; Platform Engineering; Software Development Lead; QA/SDET; SRE / Operations; Internal Audit |
| Primary Parent | 42-AIRA AI Governance and Runtime Control Standard |
| Direct Companions | 42D Identity Lifecycle; 42E Runtime Security; 42F Autonomy; 42G Threat Model; 42H Tool/MCP Gateway; 42I Memory/RAG; 42J Red Team; 42K Incident Response; 42L Multi-Agent Orchestration; 42N OPA/SBAC Rule Catalog; 42O Runtime Registry |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / AI-Governance / Agent-Supply-Chain / v1.1/ |
| Review Cadence | Monthly during tool/MCP rollout; quarterly after controlled maturity; immediate after supply-chain, plugin, connector, MCP, model-route, or runtime artifact incident |

Mandatory Practice Statement. AIRA AI agents must not depend on unmanaged tools, unverified MCP servers, unapproved plugins, direct provider SDKs, unknown connectors, unsigned containers, unregistered prompt packages, undocumented workflow scripts, or uncontrolled model adapters. Every agent runtime dependency must be registered, owned, versioned, risk-tiered, scanned, signed or integrity-checked where feasible, policy-bound, observable, reversible, and revocable before activation. An artifact is not trusted because it works; it is trusted only when it is registered, verified, controlled, monitored, and removable without weakening AIRA operations.

v1.1 Revision Focus: this revision strengthens the v1.0 supply-chain baseline with explicit MCP connector risk controls, artifact registry fields, SBOM/provenance requirements, CI/CD and GitNexus evidence gates, runtime drift monitoring, quarantine/rollback, Dynamic Workspace/System Builder integration, and Auto-Heal/Auto-Learn/Auto-Improve candidate-loop boundaries.

# Static Table of Contents
| # | Section |
| --- | --- |
| 1 | Executive Summary |
| 2 | Purpose, Scope, and Authority |
| 3 | Agent Runtime Supply Chain Control Model |
| 4 | Artifact Taxonomy and Registry Minimum Fields |
| 5 | MCP, Plugin, Connector, and Adapter Onboarding Lifecycle |
| 6 | Provenance, SBOM, Signing, License, and Scan Requirements |
| 7 | OPA/SBAC, Tool Gateway, and Runtime Authorization |
| 8 | CI/CD, GitNexus, Evidence Pack, and Promotion Gates |
| 9 | Runtime Monitoring, Drift Detection, Quarantine, and Incident Response |
| 10 | Dynamic Workspace, System Builder, and MicroFunction Integration |
| 11 | Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loops |
| 12 | Acceptance Criteria and Rejection Rules |
| 13 | RACI, Roadmap, and AVCI Summary |

# 1. Executive Summary

AIRA-DOC-042M governs the runtime supply chain used by AI agents, System Builder workflows, Dynamic Workspace assistant capabilities, tool gateways, plugins, connectors, prompt packages, guardrail packages, model-route adapters, SDKs, containers, scripts, evaluation datasets, and external APIs. The standard exists to prevent the most dangerous agentic failure mode: an apparently useful tool or connector becoming an uncontrolled authority path.

The control objective is to ensure that every dependency an agent can use is known, version-pinned, policy-bound, scanned, monitored, reversible, and supported by AVCI evidence. Direct model-provider SDK calls, unmanaged MCP servers, ad hoc browser/IDE plugins, shadow connectors, unsigned images, unpinned tools, or unreviewed prompt packages must be blocked or quarantined.
| Strategic Outcome | v1.1 Required Result |
| --- | --- |
| No shadow runtime artifacts | Every MCP server, plugin, connector, SDK, prompt package, guardrail package, model adapter, container, script, and dataset is registered before use. |
| Supply-chain evidence by construction | Artifacts carry owner, source, version, checksum/digest, SBOM or dependency inventory, license disposition, scan result, policy binding, and evidence reference. |
| Fail-closed tool use | Agents cannot invoke unregistered tools, direct SDKs, unapproved egress paths, or unsupported connectors. Missing identity, policy, evidence, scan, or rollback blocks activation. |
| Safe removability | Every artifact can be disabled, quarantined, rolled back, replaced, or revoked without uncontrolled production mutation. |
| Runtime assurance | Runtime drift, unknown artifact invocation, unapproved egress, secret exposure, direct provider bypass, and connector anomalies generate alerts and incident evidence. |

# 2. Purpose, Scope, and Authority
| Area | In Scope | Out of Scope |
| --- | --- | --- |
| Runtime artifacts | MCP servers, plugins, connectors, SDKs, libraries, containers, prompt packs, guardrails, model adapters, tool scripts, CI actions, eval datasets, external APIs. | Unmanaged personal plugins, personal AI accounts, unapproved marketplace extensions, unregistered scripts, or local-only tool installs used for AIRA work. |
| Governance controls | Artifact registry, source provenance, version pinning, SBOM/inventory, signatures/checksums, scans, licenses, OPA/SBAC, telemetry, rollback, retirement. | Treating working functionality, popularity, or AI recommendation as trust authority. |
| Execution boundaries | Tool/MCP Gateway, Harness-mediated actions, LiteLLM/private gateway routes, CI/CD gates, GitNexus read-only evidence, human approval. | Direct production mutation, direct model-provider SDK bypass, connector credential sharing, or AI installation without review. |
| Authority Level | Authority | Role |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance | Final authority for production-impacting connectors, model routes, high-risk supply-chain exceptions, and waiver acceptance. |
| L1 | AIRA AVCI, Security, AI Governance, DevSecOps, Change Governance | Universal evidence, policy, security, testing, promotion, rollback, and fail-closed controls. |
| L2 | This 42M Standard | Agent supply-chain, MCP, plugin, connector, SDK, and runtime artifact governance authority. |
| L3 | Artifact Registry, Tool Registry, MCP Registry, SBAC Catalog, OPA Policies, LiteLLM Registry, Guardrail Registry | Executable control surfaces and approved runtime configurations. |
| L4 | Artifact manifests, SBOMs, signatures, scan results, policy decisions, telemetry, incident records | Implementation proof and audit evidence. |

# 3. Agent Runtime Supply Chain Control Model

The AIRA supply-chain control model treats every artifact as a governed dependency, not a developer convenience. Artifact onboarding follows a controlled path from intake through approval, registry activation, runtime monitoring, and retirement.
| Control Stage | Required Action | Minimum Evidence |
| --- | --- | --- |
| Intake | Classify artifact class, source, purpose, data access, environment, owner, risk tier, and intended agents. | Artifact intake record; owner and backup owner; classification ceiling; requested use case. |
| Verify | Check provenance, version, checksum/digest, signature where feasible, SBOM or dependency inventory, license, SAST/SCA/container/IaC scan. | SBOM/inventory, scan reports, license disposition, checksum/signature, source reference. |
| Policy Bind | Bind to SBAC skill, OPA policy package, Tool/MCP Gateway manifest, LiteLLM route where applicable, egress allowlist, telemetry profile. | OPA/SBAC decision tests, tool manifest, schema contracts, route policy, rollback method. |
| Activate | Promote only through PR/MR, CI/CD evidence, human approval, registry state transition, and runtime toggle default. | PR/MR evidence pack, approval reference, registry activation record, monitoring rule. |
| Operate | Monitor drift, egress, usage, anomalies, CVEs, license changes, denied attempts, and unauthorized invocation. | Runtime telemetry, alerts, dashboard record, incident link, review cadence. |
| Revoke/Retire | Quarantine, disable, rotate credentials, remove grants, archive evidence, update tests and knowledge. | Quarantine ticket, revocation evidence, denial test, replacement/rollback record. |

# 4. Artifact Taxonomy and Registry Minimum Fields
| Artifact Class | Examples | Primary Risk | Mandatory Control |
| --- | --- | --- | --- |
| MCP server | Filesystem, browser, Git, ticketing, CI, database, workflow, DMS connectors | Tool hijack, excessive authority, data exfiltration, shadow capability | MCP registry, manifest, SBAC/OPA, gateway mediation, runtime telemetry, kill switch. |
| Plugin / extension | VS Code, browser, IDE, ChatGPT/Codex extension | Credential access, prompt/context leakage, malicious code | Approved source, version pinning, permissions review, scan, sandboxing, disablement path. |
| Connector | Internal API, SaaS API, database, knowledge, workflow connector | Unauthorized egress or mutation | Contract, classification ceiling, egress allowlist, action schema, audit, rate limit. |
| SDK / library | Provider SDK, MCP library, HTTP client, orchestration library | Direct bypass, vulnerable dependency, license risk | Approved technology stack, SCA, SBOM, no direct provider SDK bypass. |
| Prompt / guardrail package | System prompt, tool instructions, rails, templates | Unsafe authority, prompt injection, hallucinated permissions | Versioning, review, tests, red-team certification, source control, rollback. |
| Model / route adapter | LiteLLM route, embedding route, private gateway adapter | Wrong classification route, direct model bypass | LiteLLM registry, model alias policy, classification routing, guardrail evidence. |
| Container / image | Agent runtime image, MCP server image, devcontainer, CI image | Vulnerabilities, unsigned image, drift | SBOM, scan, signature/provenance, pinned digest, rebuild path. |
| Workflow/tool script | CI action, CLI tool, runbook script, migration helper | Destructive action, hidden secret, unreviewed execution | Code review, checksum, dry-run, idempotency, rollback, audit. |
| Evaluation dataset | Golden set, red-team set, abuse cases | Poisoned evaluation, false certification | Dataset provenance, immutability, versioning, review, restricted handling. |
| Registry Field | Required Meaning |
| --- | --- |
| artifact_id, artifact_name, artifact_class | Stable identity and class of the artifact. |
| owner, backup_owner, steward_role | Named accountability for lifecycle, risk, evidence, and retirement. |
| source_ref, supplier, repository, version, digest | Provenance, pinning, source authority, and reproducibility path. |
| classification_ceiling, data_categories, egress_profile | Maximum data class, handling rules, and network exposure. |
| sbom_ref, scan_refs, license_disposition, signature_ref | Supply-chain verification and legal/security evidence. |
| sbac_skill, opa_policy_ref, tool_manifest_ref | Executable authorization and policy binding. |
| input_schema, output_schema, idempotency_profile, rollback_method | Safe execution contract and recovery path. |
| runtime_toggle, kill_switch_scope, quarantine_state | Operational control and rapid disablement. |
| evidence_ref, review_date, recertification_due | AVCI traceability and lifecycle review. |

# 5. MCP, Plugin, Connector, and Adapter Onboarding Lifecycle
| Lifecycle Step | Required Gate | Rejection Condition |
| --- | --- | --- |
| Request | Business/technical purpose, owning bounded context, data class, intended agent, action scope, environment, and rollback expectation documented. | No owner, unclear purpose, unknown data class, unsupported environment, or no deactivation path. |
| Security and license review | Source authenticity, permissions, dependency risk, license, vulnerability posture, network flows, and secret exposure reviewed. | Unacceptable license, critical unmitigated CVE, excessive permissions, embedded secrets, or unapproved egress. |
| Contract review | Input/output schema, Problem Details/errors, idempotency, rate limit, audit fields, and OpenAPI/AsyncAPI where applicable defined. | No schema, no safe error model, non-idempotent mutation, or unbounded payload/egress. |
| Policy binding | SBAC skill, OPA policy, autonomy tier, approval rule, classification ceiling, and environment constraint defined. | No policy binding, T5-like action, or ability to bypass Tool/MCP Gateway. |
| Evidence trial | Run sandbox tests, dry-run, negative tests, red-team cases, scan gates, and observability smoke test. | Failed denial test, no trace/audit, no rollback, or evidence cannot be reconstructed. |
| Activation | Register approved version, pin digest, enable only through controlled configuration and runtime toggle. | Unpinned version, missing approval, direct install, or bypass of registry/API/Flyway/Git controls. |

# 6. Provenance, SBOM, Signing, License, and Scan Requirements
| Control | Minimum Requirement | Evidence |
| --- | --- | --- |
| Provenance | Artifact source, repository, build path, supplier, version, checksum/digest, and maintainer trust must be known. | Provenance record, digest, commit/tag, supplier review, approval. |
| SBOM / Inventory | Containers, packages, high-risk connectors, CI actions, MCP servers, and runtime images require SBOM or dependency inventory. | SBOM file, SCA report, component list, retention path. |
| Signing / Integrity | Images and packages must use signed artifacts or digest/checksum pinning where feasible. | Signature, digest pin, admission policy result. |
| License | License must be reviewed for enterprise use, redistribution, SaaS, self-hosted, model/data terms, and embedded third-party obligations. | License disposition, legal/procurement review, waiver if needed. |
| Security scans | SAST/SCA/secret/container/IaC scans apply according to artifact class; critical findings block promotion unless waived by authority. | Scan reports, remediation ticket, waiver with expiry. |
| Source retention | Evidence must be retained in approved evidence store and classified consistently with artifact and data exposure. | Evidence pack path, classification metadata, hash/immutable reference. |

# 7. OPA/SBAC, Tool Gateway, and Runtime Authorization

Artifact activation is not enough. Every runtime invocation must be authorized at execution time using identity, skill, policy, classification, environment, artifact state, tool action, route, risk tier, and evidence availability.
| OPA Input Category | Required Fields |
| --- | --- |
| Agent and actor | actor_id, agent_id, agent_version, owner, lifecycle_state, trust_tier, autonomy_tier. |
| Artifact | artifact_id, artifact_class, version, digest, approval_state, quarantine_state, risk_tier. |
| Action | action_code, tool_action_id, environment, dry_run_available, idempotency_key, rollback_method. |
| Data and route | classification, data_categories, egress_profile, model_alias, guardrail_policy_version. |
| Evidence | trace_id, evidence_ref, sbom_ref, scan_status, license_status, approval_ref, audit_sink_status. |
| Decision outcome | ALLOW, DENY, ESCALATE, QUARANTINE, SUSPEND, REVOKE, or DRY_RUN_ONLY. |
| Runtime Rule | Mandatory Treatment |
| --- | --- |
| Direct provider SDK bypass | Blocked unless explicitly waived; model traffic must route through LiteLLM or approved private/on-prem gateway. |
| Unknown MCP server | Deny invocation, alert, record policy decision, open incident or supply-chain review. |
| Unapproved plugin or extension | Disable or quarantine; remove grants; run endpoint and source review. |
| Connector with production mutation | Escalate to human approval; require dry-run, idempotency, rollback, audit, and monitoring. |
| Unapproved egress | Block at network/policy layer and route to security review. |
| Policy or evidence service unavailable | Fail closed for protected actions. |

# 8. CI/CD, GitNexus, Evidence Pack, and Promotion Gates
| Gate | Required Check | Minimum Evidence |
| --- | --- | --- |
| Repository/Golden Source | Artifact manifests, tool configs, prompts, guardrails, policies, and scripts live in approved repositories. | PR/MR, CODEOWNERS, branch protection, artifact manifest. |
| Build and dependency | Pinned toolchains, reproducible build, dependency lock, SCA, SBOM, license. | Build log, lock file, SBOM, license report. |
| Security | Secret scan, SAST/SCA/container/IaC scan, artifact permission review, egress review. | Scan summary, remediation, waiver if any. |
| Policy | OPA/Rego tests, SBAC scope tests, classification route checks, direct-SDK forbidden import checks. | Policy test result, denied-rule summary, fitness report. |
| GitNexus read-only | Impact analysis for affected agents, tools, APIs, configs, workflows, tests, policies, and runtime routes. | GitNexus report tied to commit; reviewer acknowledgement. |
| Evidence pack | SBOM, provenance, signatures/digests, scans, tests, approval, rollback, runtime monitoring rule, dashboard link. | Artifact evidence pack ID and evidence store path. |
| Promotion | Human maker-checker review and CAB/ARB/Security approval where risk requires. | Approval reference, registry activation, post-promotion monitoring. |

# 9. Runtime Monitoring, Drift Detection, Quarantine, and Incident Response
| Runtime Signal | Action Threshold | Required Response |
| --- | --- | --- |
| Unknown artifact invocation | Artifact not in registry or disabled/quarantined | Deny, alert, open incident, capture trace and agent_run_id. |
| Version drift | Runtime version/digest differs from approved registry | Quarantine artifact, block deployment, rebuild or rollback. |
| Direct SDK detection | Model/provider SDK path used outside approved gateway | Block merge/runtime, remove path, reroute via LiteLLM, run fitness check. |
| Connector exfiltration risk | Unexpected egress, excessive payload, policy mismatch, or unusual data class | Disable egress, revoke connector credentials, preserve evidence, security review. |
| Prompt/guardrail package unsafe | Unsafe tool instruction, prompt injection weakness, policy bypass, failed red-team | Suspend package, rollback last approved version, rerun evaluation. |
| Critical CVE or license violation | Critical vulnerability, unsupported license, malicious dependency indicator | Block promotion or disable runtime, patch/replace, rescan, update SBOM. |
| Missing telemetry | No trace/audit/evidence for protected action | Fail closed, open defect, do not certify artifact. |

# 10. Dynamic Workspace, System Builder, and MicroFunction Integration
| Integration Area | Governance Requirement |
| --- | --- |
| Dynamic Workspace | Frontend may display artifact status, request activation, and show evidence dashboards, but backend registry, OPA/SBAC, and Tool/MCP Gateway decide authority. Widgets cannot install tools, grant connectors, bypass policy, or expose secrets. |
| System Builder | May recommend, draft manifests, generate tests, create PR-ready artifacts, and prepare provisioning plans. It may not silently install plugins, activate connectors, approve risk tiers, waive scans, or mutate production. |
| MicroFunction runtime | MicroFunction steps may invoke only registered, policy-bound connectors through ports/adapters and Tool/MCP Gateway. Direct database, Kafka, Redis, OpenKM, model-provider, or external API calls from business logic are rejected. |
| API/event/database | OpenAPI/AsyncAPI/Kafka/Avro/CloudEvents contracts, Flyway migrations, outbox/inbox, DLQ/replay, RLS, and retention impacts must be reviewed for connector-related changes. |
| Runtime toggles | Diagnostic verbosity, tool enablement, sampling, connector activation, quarantine, and kill switch toggles must be registry-backed, audited, reversible, and policy-governed. |

# 11. Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loops
| Loop | Allowed Behavior | Prohibited Behavior |
| --- | --- | --- |
| Auto-Heal | Detect artifact drift, CVE, failed scan, runtime anomaly, direct SDK bypass, or connector failure; propose quarantine, rollback, patch PR, test plan, and approval path. | Silently install replacement tool, rotate production secret, disable production control, mutate policy, or bypass CAB/Security approval. |
| Auto-Learn | Summarize approved incident lessons, update registry metadata, propose new tests, improve threat models, and prepare reviewed knowledge artifacts. | Promote unreviewed memory, ingest Restricted data into AI context, or treat AI summary as source of truth. |
| Auto-Improve | Propose dependency upgrades, manifest normalization, policy hardening, scan coverage, SBOM automation, or connector isolation improvements through PR/MR. | Self-promote refactoring, weaken controls for convenience, or bypass maker-checker/CI evidence. |

# 12. Acceptance Criteria and Non-Negotiable Rejection Rules
| # | Acceptance Criterion |
| --- | --- |
| AC-01 | All agent runtime dependencies are registered with owner, source, version, risk tier, classification ceiling, evidence reference, and review date. |
| AC-02 | No agent can invoke an unregistered MCP server, plugin, connector, SDK, tool script, prompt package, model adapter, or container. |
| AC-03 | MCP/tool connectors have input/output schemas, SBAC/OPA policies, dry-run or simulation where feasible, audit fields, limits, and rollback methods. |
| AC-04 | Production-impacting, identity-impacting, secrets-impacting, customer-data, financial, or external-egress artifacts require human approval and enhanced monitoring. |
| AC-05 | Artifact promotion requires provenance, scan, license, policy, test, approval, monitoring, and revocation evidence. |
| AC-06 | Every artifact can be disabled, quarantined, rolled back, or replaced without uncontrolled production mutation. |
| AC-07 | SBOM/provenance evidence is retained for containers, packages, tools, and high-risk connectors where applicable. |
| AC-08 | All controls produce AVCI evidence and feed the Agent Assurance Dashboard. |
| Reject If | Required Treatment |
| --- | --- |
| Artifact has no owner, source, version, or classification ceiling. | Reject intake and require complete registry record. |
| Tool/MCP server lacks manifest, schema, SBAC/OPA policy, or rollback method. | Block activation; create remediation ticket. |
| Direct model-provider SDK bypass is detected. | Block merge/runtime and reroute through approved gateway. |
| SBOM/provenance/signature/checksum evidence is missing for high-risk artifact. | Block promotion or restrict to sandbox dry-run only. |
| Artifact has critical unmitigated vulnerability, license violation, or secret exposure. | Quarantine, patch/replace, and run incident/security review. |
| Agent or System Builder attempts to install or activate artifact without human approval. | Deny, audit, and trigger governance review. |

# 13. RACI, Roadmap, and AVCI Summary
| Activity | Architecture | Security | AI Gov | DevSecOps | Platform | Dev Lead | Internal Audit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Approve standard | A | C | R | C | C | C | I |
| Register artifact | C | C | A/R | R | R | C | I |
| Approve MCP/tool risk tier | C | A/R | C | C | R | C | I |
| Approve model adapter/route | C | C | A/R | C | R | C | I |
| Run scans and SBOM | I | C | C | A/R | R | C | I |
| Approve production connector | A | R | C | R | R | C | I |
| Monitor runtime drift | I | R | C | A/R | R | C | I |
| Quarantine artifact | A | R | R | R | R | C | I |
| Audit evidence | I | C | C | C | C | I | A/R |
| Phase | Focus | Exit Criteria |
| --- | --- | --- |
| 0 | Register 42M in canonical source and 00D reconciliation register. | Document approved as additive agent supply-chain standard. |
| 1 | Create Agent Runtime Artifact Registry. | Schema, required fields, owners, and seed inventory approved. |
| 2 | Inventory existing tools, MCP servers, plugins, connectors, SDKs, images, prompt packs. | All known artifacts classified, risk-tiered, and assigned owner. |
| 3 | Bind high-risk artifacts to SBAC/OPA and Tool/MCP Gateway. | No high-risk artifact callable outside policy. |
| 4 | Add CI/CD supply-chain gates. | SBOM, scans, license, secret scan, version pinning, and GitNexus evidence enforced. |
| 5 | Enable runtime drift and egress monitoring. | Dashboard, alerts, runtime toggle audit, and incident workflow active. |
| 6 | Run red-team supply-chain tests. | Tool hijack, direct SDK, egress, secret leakage, and shadow artifact tests pass. |
| AVCI Property | 42M Evidence |
| --- | --- |
| Attributable | Every artifact has owner, source, supplier, version, registry ID, approval reference, and responsible role. |
| Verifiable | Provenance, SBOM/inventory, scan, license, signature/checksum, policy test, telemetry, and activation evidence prove trust path. |
| Classifiable | Artifacts define classification ceiling, data handling, egress profile, prompt/telemetry restrictions, and model-route eligibility. |
| Improvable | Drift, incidents, denied actions, scan findings, red-team failures, and operational lessons feed controlled improvement backlog and recertification. |

## Appendix A. Artifact Manifest Minimum Schema
| Manifest Field | Example / Required Content |
| --- | --- |
| artifact_id | ART-AIRA-MCP-GIT-001 |
| artifact_class | MCP_SERVER \| PLUGIN \| CONNECTOR \| SDK \| PROMPT_PACKAGE \| MODEL_ADAPTER \| CONTAINER \| SCRIPT \| DATASET |
| source_ref | Repository, supplier, commit/tag/version, digest, signature/checksum. |
| risk_and_classification | Risk tier, classification ceiling, data categories, egress profile, environment scope. |
| policy_refs | SBAC skill, OPA package/rule, tool manifest, LiteLLM/model route if applicable, guardrail version. |
| evidence_refs | SBOM, SCA/SAST/container scan, license, red-team/eval, CI run, approval, rollback test. |
| operational_controls | Runtime toggle, kill switch scope, monitoring rule, quarantine state, review date. |

## Appendix B. PR/MR Evidence Checklist

• Artifact registry record created or updated with owner, backup owner, source, version, risk tier, classification ceiling, and evidence reference.

• SBOM or dependency inventory produced where applicable; scan, license, secret, and provenance checks attached.

• OPA/SBAC policy tests and Tool/MCP Gateway manifest tests pass with fail-closed denial cases.

• GitNexus impact analysis shows affected agents, tools, policies, APIs, MicroFunctions, workflows, tests, and environments.

• Rollback, quarantine, disablement, and recovery instructions are present and tested for high-risk artifacts.

• Human approval is attached for high-risk, production, identity, secrets, customer-data, or external-egress artifacts.

