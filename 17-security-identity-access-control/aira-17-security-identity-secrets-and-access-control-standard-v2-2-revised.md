---
title: "Security Identity Secrets and Access Control Standard"
doc_id: "AIRA-17"
version: "v2.2"
status: "revised"
category: "Security identity and access control"
source_docx: "AIRA_17_Security_Identity_Secrets_and_Access_Control_Standard_v2.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 17-security-identity-access-control
  - revised
  - aira-17
---



# Security Identity Secrets and Access Control Standard



AIRA

AI-Native Enterprise Platform

Security, Identity, Secrets, and Access Control Standard

v2.2 Revised

Identity Governance | Secrets Hygiene | OPA/SBAC/ABAC/RBAC | Secure APIs | Dynamic Workspace | MicroFunction Runtime | AI Agent Controls | AVCI Evidence
| Property | Value |
| --- | --- |
| Document ID | AIRA-DOC-017 |
| Canonical Filename | AIRA_17_Security_Identity_Secrets_and_Access_Control_Standard_v2.2_Revised.docx |
| Version | v2.2 - Dynamic Workspace, MicroFunction, AI Agent, DevSecOps Evidence, Runtime Toggle, and Secure API Update |
| Supersedes | 17-AIRA_Security_Identity_Secrets_and_Access_Control_Standard_v2.1_Aligned.docx |
| Companion Implementation Guide | 17A-AIRA_Security_and_Access_Control_Implementation_Guide_v1.1.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | DRAFT FOR ARCHITECTURE REVIEW BOARD / SECURITY GOVERNANCE / CAB APPROVAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Security Architecture; DevSecOps Lead; Platform Engineering; Software Development Lead; QA/SDET; Data Governance; SRE; AI Governance; Internal Audit; Business Process Owners |
| Review Cadence | Quarterly; unscheduled on identity, SBAC/OPA, secrets, Dynamic Workspace, MicroFunction, API/event, AI-agent, model route, CI/CD, incident, or production access change |
| Evidence Path | OpenKM Tier-0 / AIRA / Security / Identity-Secrets-Access-Control / v2.2/ |

Discipline First - Automation Second - Intelligence Third - AVCI Always

# Mandatory Practice Statement

No AIRA user, service, Dynamic Workspace component, MicroFunction transaction, API endpoint, Kafka topic, database role, CI/CD job, System Builder workflow, AI agent, model route, tool action, prompt, guardrail, runtime toggle, or operational recovery path may be activated unless identity, authorization, secrets, classification, policy, audit, observability, reversibility, and AVCI evidence controls are implemented and validated. Security failure must result in safe denial, suspension, quarantine, rollback, or human escalation - never silent bypass or fail-open behavior.

# Static Table of Contents

Executive Summary and v2.2 Update Verdict

Purpose, Scope, Authority, and Conflict Rule

Security Control Model and Non-Negotiable Rules

Identity, Authentication, Session, and Workload Identity Controls

Authorization Model: RBAC, ABAC, SBAC, OPA, and Separation of Duties

Secrets, Credential Hygiene, Key Management, and Environment Boundaries

Secure APIs, Events, MicroFunctions, and Dynamic Workspace Enforcement

AI Agent, System Builder, Model Route, Prompt, and Tool Security

DevSecOps, Testing, DAST, GitNexus, and Supply-Chain Evidence Gates

Observability, Incident Response, Runtime Toggles, and Continuous Improvement

RACI, Roadmap, Acceptance Criteria, and AVCI Summary

# 1. Executive Summary and v2.2 Update Verdict

AIRA-DOC-017 remains the governing security authority for identity, secrets, access control, classification handling, secure APIs, policy-as-code, and fail-closed behavior. Version 2.2 aligns the standard with the revised Greenfield Environment, System Builder Lite, Sprint 0, CI/CD, PoC 2, observability, operations, recovery, release/CAB, audit, and SBAC catalog documents so security becomes executable from Day 0 rather than added after feature delivery.
| v2.2 Update Area | Required Security Outcome |
| --- | --- |
| Dynamic Workspace | UI and UX are policy-filtered derivative experiences. Workspace resolution, component visibility, admin builder actions, widget actions, and AI panel access require backend OPA/SBAC decisions and evidence. |
| MicroFunction Runtime | Every protected transaction step includes identity, classification, authorization, idempotency, audit, observability, safe error, and rollback/compensation controls before business logic. |
| API and Eventing | OpenAPI/AsyncAPI contracts, Kafka topics, Avro schemas, CloudEvents envelopes, outbox/inbox, DLQ, and replay flows must carry classification, correlation, security, and idempotency metadata. |
| Secrets Hygiene | No secrets in source code, prompts, logs, screenshots, test fixtures, Obsidian, LLM Wiki, GitNexus reports, CI artifacts, container images, or runtime telemetry. Secrets are references to approved vault paths, never pasted values. |
| AI Governance | System Builder and AI agents may analyze, recommend, draft, test, and propose. They may not approve their own outputs, receive direct production credentials, bypass LiteLLM/guardrails, bypass Harness/SBAC/OPA, or mutate production. |
| DevSecOps Evidence | Security gates include SAST, SCA, secrets scan, IaC/container scan, OPA policy tests, authenticated DAST, SBOM/provenance, architecture fitness, GitNexus impact, and remediation evidence. |

# 2. Purpose, Scope, Authority, and Conflict Rule
| Area | In Scope | Out of Scope |
| --- | --- | --- |
| Identity and access | Human identity, service identity, workload identity, sessions, RBAC/ABAC/SBAC, OPA/Rego, maker-checker, access review, recertification, and break-glass. | Unmanaged local users, shared accounts, hardcoded roles, direct production DB grants, bypass groups, or frontend-only authorization. |
| Secrets and keys | Vault/OpenBao or approved secrets manager patterns, key rotation, short-lived credentials, OIDC/workload identity, sealed secret handling, and audit evidence. | Secrets in code, .env files committed to Git, prompts, chat messages, screenshots, logs, test data, CI variables without scope, or documentation. |
| Runtime security | Gateway enforcement, secure API/event contracts, MicroFunction controls, Dynamic Workspace policy filtering, telemetry redaction, incident response, recovery, and runtime toggles. | Silent control disablement, uncontrolled debug logging, unapproved telemetry expansion, or performance-driven security bypass. |
| AI-native security | LiteLLM routing, guardrails, agent registry, tool authorization, trust tiers, model route eligibility, prompt security, retrieval ACL filtering, and AI evidence. | Direct provider SDK calls, unregistered agents, self-approved agent actions, uncontrolled memory writes, or unrestricted RAG over sensitive data. |

Authority. This standard is subordinate to the consolidated AIRA architecture, AVCI, data classification, legal/regulatory, and CAB/ARB decisions, but governs security interpretation where implementation documents are silent. Where two documents conflict, the stricter security control applies and the conflict must be logged as an AVCI reconciliation item assigned to the document owner and register owner.

# 3. Security Control Model and Non-Negotiable Rules
| Control Layer | Mandatory Rule | Evidence Required |
| --- | --- | --- |
| Identity layer | Every human, service, workload, AI agent, CI/CD job, and tool action has a unique identity, accountable owner, lifecycle state, and approved purpose. | Identity inventory, JML record, agent registry, service account owner, access review, lifecycle event. |
| Policy layer | Authorization is policy-as-code using OPA/Rego or approved policy abstraction with RBAC/ABAC/SBAC inputs. | Policy bundle version, test results, decision log, denial evidence, change approval. |
| Secret layer | Secrets are centrally managed, short-lived where feasible, rotated, least-privilege, and never exposed in artifacts or prompts. | Vault path reference, lease/rotation evidence, secret scan result, owner, expiry. |
| Contract layer | APIs, events, schemas, workflows, MicroFunctions, Dynamic Workspace actions, and AI tools declare security and classification metadata. | OpenAPI/AsyncAPI extensions, catalog records, schema registry, capability binding. |
| Verification layer | Security controls are tested in CI/CD and UAT, including negative tests, DAST, secrets scans, SAST/SCA, OPA tests, and architecture fitness. | Pipeline evidence, test reports, scan findings, remediation links, waiver records. |
| Runtime layer | Failures in identity, policy, secrets, guardrails, model gateway, audit, or evidence stores fail closed with safe error handling. | Trace/log/audit/evidence record, incident ticket, dashboard event, post-incident review. |

No custom authentication engine, custom password store, hardcoded role check, direct token exposure, or password handling inside AIRA application code.

No production data, production secrets, raw tokens, private keys, customer PII, account numbers, embeddings, or raw prompts in logs, screenshots, test fixtures, CI artifacts, GitNexus output, Obsidian, LLM Wiki, or AI conversations.

No direct model-provider calls from application code, notebooks, scripts, services, agents, or System Builder outputs; model traffic uses LiteLLM or approved private/on-prem gateway with guardrails.

No agent, tool, workflow, or runtime toggle may weaken security without CAB/ARB/Security approval, compensating controls, expiry, and evidence.

# 4. Identity, Authentication, Session, and Workload Identity Controls
| Identity Type | Approved Pattern | Rejected Pattern |
| --- | --- | --- |
| Human user | Enterprise identity through Keycloak/AD or approved IdP, OIDC Authorization Code + PKCE for web flows, MFA/step-up where risk requires, access tied to role/skill and owner-approved business purpose. | Local application passwords, shared accounts, static admin users, bypass login links, or identity stored directly in business tables without governance. |
| Service account | Named owner, purpose, environment scope, short-lived credential where feasible, least-privilege scopes, rotation, access review, and decommission plan. | Generic shared service accounts, long-lived unrotated secrets, broad DB/admin rights, or invisible ownership. |
| Workload identity | SPIFFE/SVID, OIDC workload federation, Kubernetes service account with bounded RBAC, mTLS, network policy, and environment-scoped secret access. | Hardcoded client secrets, copied kubeconfigs, direct production certificates, or namespace-wide privileges. |
| CI/CD identity | OIDC-to-cloud/provider federation or scoped CI tokens, branch/environment protections, separate build/promote identities, artifact signing, and audit trail. | Personal tokens in CI, unscoped PATs, mutable pipeline secrets, or deployment rights in build-only jobs. |
| AI agent identity | Agent registry identity, owner, purpose, trust tier, classification ceiling, allowed tools, model route, skill grants, approval state, and revocation path. | Unregistered agents, agents using human credentials, agent-to-agent privilege amplification, or tool access outside Harness/SBAC/OPA. |

Session establishment must create a safe session context containing only the minimum claims required for authorization, classification handling, audit, personalization, and Dynamic Workspace resolution. Raw JWTs, refresh tokens, secrets, and unnecessary PII must not be sent to the frontend, logs, traces, prompts, screenshots, or evidence summaries.

# 5. Authorization Model: RBAC, ABAC, SBAC, OPA, and Separation of Duties
| Authorization Dimension | Required Treatment |
| --- | --- |
| RBAC | Roles express organizational responsibility and broad job function. They do not directly become unrestricted authority. |
| ABAC | Decisions include tenant, branch/unit, data classification, case status, ownership, channel, device/risk, time, environment, and requested resource. |
| SBAC | Skills define what an actor or agent can do, at what proficiency/trust tier, for which tool, data class, environment, and action. Skills expire and require evidence-based recertification. |
| OPA/Rego | OPA policy packages are versioned, tested, reviewed, observable, and fail-closed. Application code asks for decisions and does not hide authorization logic. |
| Separation of Duties | Requesters, makers, checkers, approvers, deployers, operators, auditors, and agent owners remain separable for high-risk access, release, and recovery actions. |
| Deny evidence | Denials are safe, non-revealing, traceable, classified, and useful for improvement without exposing sensitive policy internals. |
| Protected Action | Minimum Authorization Inputs | Human Approval Trigger |
| --- | --- | --- |
| Dynamic Workspace admin template publish | actor, role, skill, tenant, classification, workspace_code, template_version, SoD status, policy_ref | Required for template activation, rollback, Restricted data exposure, or production-impacting UI changes. |
| MicroFunction transaction execution | actor, transaction_code, capability_code, idempotency_key, classification, environment, policy bundle, risk tier | Required for privileged, destructive, financial/legal, data-repair, account-lock/unlock, or production-change transactions. |
| Kafka replay / DLQ reprocess | actor, topic, consumer group, replay window, schema version, business impact, duplicate-safety proof | Required for production replay, customer-impacting reprocess, or Restricted data. |
| Runtime telemetry toggle change | actor, toggle, environment, duration, classification, performance impact, redaction profile | Required when disabling security/audit/trace coverage or expanding sensitive telemetry. |
| AI tool action | agent_id, tool_id, skill, trust tier, model route, guardrail result, environment, rollback, approval state | Required for T3+ tool action, Restricted data, prod-impacting action, or low-confidence result. |

# 6. Secrets, Credential Hygiene, Key Management, and Environment Boundaries
| Control | Mandatory Requirement | Evidence |
| --- | --- | --- |
| Secret source | Use Vault/OpenBao or approved secrets manager. Store only references in Git, config, prompts, runbooks, and evidence. | Vault path reference, access policy, rotation schedule, owner. |
| Credential lifetime | Prefer short-lived tokens, workload identity, OIDC federation, and automatic rotation. Long-lived credentials require waiver and expiry. | Lease evidence, expiration, rotation proof, access review. |
| Developer machines | No production secrets or data. Local development uses synthetic data and local adapters. .env files are local-only, ignored, and never pasted into AI tools. | Secret scan, workstation checklist, synthetic data proof. |
| CI/CD | Environment-scoped secrets, masked logs, OIDC federation, restricted runners, no secrets in artifact names/log output. | Pipeline secret scan, runner policy, redaction proof. |
| Containers/IaC | No secrets baked into images, Helm values, Terraform state, devcontainers, Dockerfiles, or sample manifests. | Image scan, IaC scan, state protection, SBOM/provenance. |
| Rotation and revocation | Credentials are rotated on schedule, on role transfer, incident, compromise suspicion, environment teardown, or agent retirement. | Rotation ticket, audit log, validation test, decommission evidence. |

Secrets hygiene applies equally to generated artifacts: System Builder outputs, Codex suggestions, GitNexus summaries, Obsidian notes, LLM Wiki projections, screenshots, DAST recordings, Playwright traces, Sentry events, Loki logs, Tempo traces, and Grafana dashboards must never contain secret values or raw tokens.

# 7. Secure APIs, Events, MicroFunctions, and Dynamic Workspace Enforcement
| Component | Security Requirement |
| --- | --- |
| API Gateway | TLS, JWT validation, audience/issuer checks, rate limiting, WAF/security headers where applicable, correlation, safe error mapping, and policy route binding. |
| OpenAPI | Security schemes, scopes, classification, idempotency, safe errors, evidence_ref, trace_id, request_id, and OPA/SBAC requirements are contract fields. |
| AsyncAPI / Kafka | Schema-managed events, CloudEvents envelope, classification metadata, trace_id/correlation_id/causation_id, producer/consumer authorization, idempotent consumers, DLQ, replay controls, and audit evidence. |
| MicroFunction | Security, classification, session, SBAC/OPA, idempotency, audit, event, observability, safe response, retry, compensation, and evidence steps are standard envelope responsibilities. |
| Dynamic Workspace | Workspace resolver filters screens, components, widgets, menus, templates, and AI panel actions by backend policy. Frontend permissions are presentation hints only. |
| Database | Least-privilege roles, Flyway-only changes, RLS where applicable, classification columns, audit fields, approved views/functions, and no direct app bypass of domain policies. |

Authenticated DAST must use synthetic users, synthetic data, non-production targets, explicit scan windows, safe throttling, exclusion rules for destructive actions, evidence capture, and remediation tracking. Any scan that requires elevated access must be pre-approved and must not become a shortcut around normal authorization.

# 8. AI Agent, System Builder, Model Route, Prompt, and Tool Security
| AI Security Control | Required Treatment |
| --- | --- |
| Model routing | All model traffic goes through LiteLLM or approved private/on-prem gateway. Classification determines eligible route, guardrail profile, retention, and logging level. |
| Guardrails | Input, retrieval, execution, and output guardrails apply based on risk. Missing guardrail or route policy blocks protected actions. |
| Tool execution | Agents request tool actions through Harness/MCP gateway. SBAC, OPA, trust score, dry-run, idempotency, rollback, and human approval are evaluated before execution. |
| Prompt and memory | Prompts, system instructions, RAG context, memory writes, and retrieval results are classified, source-cited, freshness-checked, and protected from poisoning/leakage. |
| Agent lifecycle | Agents require registry identity, owner, purpose, allowed tools, classification ceiling, trust tier, certification, telemetry, suspension, and retirement evidence. |
| Prohibited agent actions | Approving access, changing production secrets, modifying security policy, bypassing CI/CD, deploying to production, deleting data, or approving its own output. |
| Autonomy Tier | Security Decision |
| --- | --- |
| T0 Advisory | Allowed with source grounding, classification check, and human review before use as authority. |
| T1 Read-only | Allowed only for approved sources and eligible classification; Restricted evidence requires additional approval. |
| T2 Candidate generation | Allowed in branch/sandbox only; must pass tests, scans, and maker-checker review before merge or activation. |
| T3 Tool action request | Requires Harness/SBAC/OPA decision, dry-run where feasible, audit, rollback, and approval based on risk. |
| T4 Limited delegated reversible action | Only after certification, explicit approval, bounded scope, kill switch, telemetry, and rollback proof. |
| T5 Human-controlled/prohibited | Human-only for production secrets, privileged access, legal/financial decisions, destructive actions, policy exceptions, and CAB decisions. |

# 9. DevSecOps, Testing, DAST, GitNexus, and Supply-Chain Evidence Gates
| Gate | Required Security Evidence |
| --- | --- |
| Pre-commit / local | Formatting, lint, dependency hygiene, no secret/PII/token leakage, no forbidden imports, no direct provider SDK calls, no direct DB/Kafka/Redis/OpenKM from business logic. |
| Build / unit / component | Secure coding tests, negative tests, input validation, output redaction, fail-closed behavior, identity/session handling, and deterministic fixtures. |
| Policy and access | OPA/Rego tests, SBAC skill tests, SoD tests, denial tests, role/permission seed validation, and access regression. |
| SAST / SCA / secrets / IaC | SAST findings, dependency/license/SCA results, secrets scan, IaC/container scan, SBOM, provenance, and remediation/waiver records. |
| Contract and DAST | OpenAPI/AsyncAPI security diff, authenticated DAST, API abuse case checks, rate-limit tests, session tests, authorization bypass tests. |
| GitNexus | Read-only impact analysis, security-sensitive code map, affected tests, blast radius, forbidden boundary findings, and reviewer focus evidence. |
| Promotion | Security sign-off, CAB/ARB routing, evidence pack, rollback/compensation plan, post-promotion monitoring, and hypercare/security watch. |

Security waivers must identify owner, risk, scope, compensating controls, expiry date, evidence, reviewer, and removal plan. Waivers cannot approve secret leakage, direct production mutation, disabled audit, direct model-provider bypass, hardcoded admin access, or intentional authorization bypass.

# 10. Observability, Incident Response, Runtime Toggles, and Continuous Improvement
| Area | Required Treatment |
| --- | --- |
| Telemetry safety | Log4j2, OpenTelemetry, Sentry, Loki, Tempo, and Grafana must support trace reconstruction without exposing secrets, raw tokens, raw PII, Restricted payloads, prompts, embeddings, or high-cardinality sensitive labels. |
| Runtime toggles | Security-relevant toggles for logging, tracing, sampling, feature flags, workspace telemetry, AI panel telemetry, and debug verbosity require owner, policy, environment, duration, audit, safe defaults, and rollback. |
| Incident response | Identity compromise, secret exposure, authorization bypass, agent misuse, prompt injection, model-route bypass, DAST critical finding, DLQ/replay abuse, or data leak triggers containment, evidence preservation, RCA, and CAB/security review. |
| Auto-Heal | May detect and propose remediation; may execute only approved, bounded, reversible, observable, policy-gated actions with human approval where required. |
| Auto-Learn | May produce source-cited learning candidates from evidence; cannot promote unreviewed knowledge to Obsidian, LLM Wiki, prompts, policies, or runbooks. |
| Auto-Improve | May propose hardening, refactor, test, policy, prompt, guardrail, model-route, or environment changes; activation requires tests, security evidence, approval, and rollback. |

# 11. RACI, Roadmap, Acceptance Criteria, and AVCI Summary
| Role | Accountability |
| --- | --- |
| Solutions Architecture Office / IT Head | Owns standard, resolves cross-document security conflicts, routes ARB/CAB decisions, and accepts material risk only through governance. |
| Security Architecture | Owns identity, secrets, access-control design, threat model, policy-as-code, secure API/event requirements, and security acceptance. |
| DevSecOps Lead | Implements CI/CD security gates, evidence packs, SBOM/provenance, scans, GitNexus integration, and promotion controls. |
| Software Development Lead | Ensures code, MicroFunctions, frontend, APIs, events, and tests comply with security boundaries and no bypass rules. |
| Platform Engineering / SRE | Owns workload identity, vault integration, runtime toggles, observability, incident readiness, and operational security. |
| AI Governance | Owns model route, guardrail, AI agent, prompt, memory, retrieval, and autonomy-security controls. |
| Internal Audit | Tests evidence completeness, access review, control operation, waiver closure, and AVCI traceability. |
| Roadmap Step | Output |
| --- | --- |
| R1 - Baseline adoption | Approve v2.2, update companion cross-references, and register reconciliation items. |
| R2 - Policy bundle hardening | OPA/SBAC policy packages, tests, denial evidence, and access catalog alignment. |
| R3 - Secrets and identity hygiene | Vault/OpenBao paths, workload identity, service account inventory, rotation, and recertification. |
| R4 - CI/CD security gates | SAST/SCA/secrets/IaC/DAST/OPA/SBOM/provenance/GitNexus gates with evidence pack integration. |
| R5 - AI and runtime controls | Agent registry, LiteLLM/guardrail routing, tool-action controls, telemetry toggle governance, incident runbooks. |
| Acceptance Criterion | Pass Condition |
| --- | --- |
| Identity and access | All protected actors, services, agents, tools, roles, skills, and approvals are cataloged, tested, and recertifiable. |
| Secrets hygiene | No real secret, token, private key, production credential, raw PII, or Restricted payload appears in source, CI, logs, screenshots, prompts, docs, or evidence. |
| Runtime enforcement | Dynamic Workspace, MicroFunction, API, event, database, workflow, and AI tool actions fail closed on missing identity, policy, guardrail, secret, audit, or evidence controls. |
| Verification | CI/CD produces security, policy, DAST, supply-chain, GitNexus, observability, and remediation evidence. |
| Reversibility | Access, policy, secret, prompt, guardrail, model-route, tool, runtime toggle, and security configuration changes can be rolled back, revoked, rotated, disabled, or compensated. |
| AVCI Property | Security Evidence |
| --- | --- |
| Attributable | Named owner, role, actor, agent_id, policy version, secret owner, ticket, commit, CI run, approval, and evidence reference. |
| Verifiable | Tests, scans, OPA decisions, DAST results, SBOM/provenance, GitNexus impact, traces, audit records, dashboards, and incident evidence. |
| Classifiable | Every artifact, log, prompt, event, trace, API, workspace component, evidence record, and AI route carries classification and handling rules. |
| Improvable | Findings, incidents, denials, failed tests, scans, SLO/security signals, and user feedback become reviewed backlog, runbook, policy, test, or architecture improvements. |

# Appendix A. Required Cross-Document Alignment Notes

17A should remain the implementation guide and should be reviewed after this standard if detailed code/configuration examples need expansion.

32 SBAC Catalog v1.2 is now the access catalog companion for role, skill, permission, and capability binding.

31A Observability v1.2 governs trace/log/metric/audit/evidence correlation and forbidden telemetry fields.

20/45 govern the CI/CD and PoC 2 security gates that operationalize this standard.

42D-42N and 42O-42P govern AI agent identity, autonomy, tools, memory/RAG, certification, incidents, policy-as-code, registry, and evidence data model.

Known reconciliation items, including older references to 17 v2.0/v2.1 and 41B/44 overlap, should remain visible in 00D until the canonical register approves final disposition.

