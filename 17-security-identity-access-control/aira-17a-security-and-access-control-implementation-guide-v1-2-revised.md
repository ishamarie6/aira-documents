---
title: "Security and Access Control Implementation Guide"
doc_id: "AIRA-17A"
version: "v1.2"
status: "revised"
category: "Security identity and access control"
source_docx: "AIRA_17A_Security_and_Access_Control_Implementation_Guide_v1.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 17-security-identity-access-control
  - revised
  - aira-17a
---



# Security and Access Control Implementation Guide



AIRA

AI-Native Enterprise Platform

Security and Access Control Implementation Guide

v1.2 Revised

Implementation Patterns | OPA/SBAC | Keycloak/OIDC | Vault/OpenBao | Secure APIs | Dynamic Workspace | MicroFunctions | AI Agents | DevSecOps Evidence
| Property | Value |
| --- | --- |
| Document ID | AIRA-DOC-017A |
| Canonical Filename | AIRA_17A_Security_and_Access_Control_Implementation_Guide_v1.2_Revised.docx |
| Version | v1.2 - Dynamic Workspace, MicroFunction, Secure API, Authenticated DAST, AI Agent, Runtime Toggle, and Evidence Implementation Update |
| Supersedes | 17A-AIRA_Security_and_Access_Control_Implementation_Guide_v1.1.docx |
| Parent Standard | 17-AIRA_Security_Identity_Secrets_and_Access_Control_Standard_v2.2_Revised.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | DRAFT FOR ARCHITECTURE REVIEW BOARD / SECURITY GOVERNANCE / CAB APPROVAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Security Architecture; DevSecOps Lead; Platform Engineering; Software Development Lead; QA/SDET; Data Governance; SRE; AI Governance; Internal Audit; Business Process Owners |
| Review Cadence | Quarterly; unscheduled on identity, SBAC/OPA, secrets, Dynamic Workspace, MicroFunction, API/event, AI-agent, model route, CI/CD, incident, or production access change |
| Evidence Path | OpenKM Tier-0 / AIRA / Security / Security-Access-Control-Implementation / v1.2/ |

Discipline First - Automation Second - Intelligence Third - AVCI Always

# Mandatory Implementation Statement

This guide is the practical execution companion to the parent security standard. No AIRA implementation is secure because it merely uses Keycloak, Vault, OPA, Kafka, CI/CD, or an approved framework. It is secure only when those controls are wired into enforceable contracts, runtime decisions, tests, telemetry, evidence packs, rollback paths, and human approval gates. Missing identity, policy, classification, guardrail, secret, audit, evidence, or approval control must fail closed.

# Static Table of Contents

Executive Summary and v1.2 Update Verdict

Purpose, Scope, Source Alignment, and Authority

Implementation Principles and Non-Negotiable Developer Rules

Identity, Authentication, Session, and Workload Identity Implementation

Authorization Implementation: RBAC, ABAC, SBAC, OPA, and SoD

Secrets, Keys, Certificates, and Environment Boundary Implementation

Secure APIs, Events, MicroFunctions, and Dynamic Workspace Patterns

System Builder, AI Agent, Model Route, Prompt, Retrieval, and Tool Security

DevSecOps Security Gates, Authenticated DAST, GitNexus, and Evidence Packs

Observability, Runtime Toggles, Incident Response, and Continuous Improvement

Testing, Architecture Fitness, RACI, Roadmap, and AVCI Summary

# 1. Executive Summary and v1.2 Update Verdict

Document 17A operationalizes AIRA security controls for developers, DevSecOps, platform engineering, AI governance, QA/SDET, SRE, DBA, and reviewers. Version 1.2 aligns the implementation guide with the revised Security Standard v2.2, SBAC Catalog, CI/CD Evidence Pack, PoC 2 System Factory, Observability Standard, Production Operations, Release/CAB, Internal Audit, and Dynamic Workspace documents.
| v1.2 Update Area | Implementation Outcome |
| --- | --- |
| Security as executable control | Security requirements become OPA policies, SBAC grants, tests, CI gates, audit events, dashboards, evidence records, and rollback controls. |
| Dynamic Workspace enforcement | Frontend workspace rendering is policy-filtered and backend-governed; UI configuration cannot become authorization authority. |
| MicroFunction security envelope | Each protected transaction step includes identity, classification, authorization, idempotency, audit, telemetry, safe error, and reversibility before business logic. |
| Secure API/event implementation | OpenAPI, AsyncAPI, Kafka, Avro, CloudEvents, outbox/inbox, DLQ, and replay paths carry authentication, authorization, classification, idempotency, correlation, and evidence fields. |
| AI-native security | System Builder and agents remain candidate-generation actors unless governed through registry, SBAC, OPA, LiteLLM, guardrails, Harness, evidence, and human approval. |
| Evidence by construction | Security gates and runtime controls produce evidence suitable for PR/MR review, audit, incident response, Auto-Learn, and controlled improvement. |

# 2. Purpose, Scope, Source Alignment, and Authority
| Area | In Scope | Implementation Boundary |
| --- | --- | --- |
| Human access | Keycloak/OIDC, Active Directory federation, MFA/step-up where applicable, session context, access request, JML, recertification, and break-glass. | AIRA does not build a custom authentication engine or store user passwords. |
| Service and workload identity | Service accounts, CI/CD identities, workload identity, short-lived credentials, tool identities, and agent service identities. | No shared privileged accounts; no direct production credentials in agents, scripts, prompts, or developer workstations. |
| Authorization | RBAC, ABAC, SBAC, OPA/Rego, SoD, maker-checker, approval matrices, resource scopes, classification ceilings, and environment boundaries. | No hardcoded roles or authorization logic inside controllers, UI, SQL scripts, or agents. |
| Secrets and keys | Vault/OpenBao patterns, key references, certificate lifecycle, rotation, revocation, break-glass custody, and evidence. | No secrets in Git, Obsidian, LLM Wiki, prompts, logs, screenshots, test data, CI artifacts, or GitNexus reports. |
| AI and System Builder | Agent registry, skill grants, model routes, guardrails, prompt handling, retrieval eligibility, tool manifests, Harness execution, and evidence. | No direct model-provider calls from application code; all model access routes through LiteLLM or approved private gateway. |

Authority hierarchy. The parent Document 17 defines mandatory security policy. This 17A guide defines implementation patterns and gates. The SBAC catalog, OPA policies, CODEOWNERS, CI/CD templates, architecture fitness functions, and evidence pack schemas may tighten this guide but may not weaken it. Any conflict must be logged as an AVCI reconciliation item and routed through ARB/CAB or the security governance owner.

# 3. Implementation Principles and Non-Negotiable Developer Rules
| Principle | Developer / DevSecOps Implementation Rule | Reject When |
| --- | --- | --- |
| Least privilege | Grant only the exact role, skill, tool, data scope, environment scope, and duration required. | A broad admin role, wildcard permission, or long-lived credential is used for convenience. |
| Policy before execution | Evaluate identity, classification, SBAC, OPA, guardrail, and approval status before protected action. | Business code executes first and checks policy later. |
| Fail closed | Unavailable identity, policy, secret, guardrail, audit, evidence, or approval control blocks protected action. | Code falls back to allow, default role, cached secret, local bypass, or debug override. |
| Ports and adapters | Keycloak, OPA, Vault/OpenBao, Kafka, DB, LiteLLM, OpenKM, workflow, CI/CD, and security tools are accessed through ports/adapters. | Domain or controller code imports infrastructure SDKs directly. |
| Classification-aware | Classification controls storage, routing, retrieval, model eligibility, logging, evidence, retention, and autonomy. | Confidential/Restricted data appears in external model routes, logs, screenshots, metrics labels, or prompts. |
| Evidence by construction | Every access decision, secret access, policy change, AI action, provisioning action, promotion, and exception emits evidence. | A security-impacting path has no trace_id, policy decision, audit record, approval, or evidence_ref. |

# 4. Identity, Authentication, Session, and Workload Identity Implementation

Implementation must separate authentication, authorization, session context, and business capability execution. Keycloak/OIDC establishes identity; AIRA establishes governed session context after token validation, classification, policy evaluation, audit, and observability controls pass.
| Control | Implementation Pattern | Evidence / Test |
| --- | --- | --- |
| OIDC login | Use Authorization Code + PKCE through Keycloak or approved enterprise identity provider. Validate issuer, audience, expiry, signature, nonce/state, and token claims. | OIDC config review, negative token tests, expired/invalid/audience mismatch tests, login trace. |
| Session context | Session context contains safe user hash, tenant/org context, roles, skills, classification ceiling, channel, and correlation IDs. | Session DTO contract, no raw token leakage, audit event, frontend safe display test. |
| Workload identity | Services, CI/CD jobs, agents, and tools use dedicated identities with owner, purpose, scope, expiry, and rotation evidence. | Identity inventory, service account owner, access review, credential lease evidence. |
| JML | Joiner/mover/leaver events trigger role review, skill updates, agent ownership review, credential rotation, and access removal. | JML ticket, recertification result, disabled access proof, exception record. |
| Break-glass | Time-bound human-only emergency access requires approval, reason, scope, monitoring, evidence, and post-event review. | Break-glass ticket, approval, session log, commands/actions, closure and RCA. |

# 5. Authorization Implementation: RBAC, ABAC, SBAC, OPA, and SoD

Authorization must be implemented as an explicit decision contract. Controllers, UI components, background jobs, consumers, System Builder workflows, and AI agents submit structured inputs to OPA/Rego or the approved policy abstraction. The decision result and policy version are stored as audit/evidence.
| OPA Input Field | Mandatory Meaning | Example |
| --- | --- | --- |
| actor | Human, service, CI/CD job, agent, or tool identity plus owner and lifecycle state. | actor.type=agent; owner=security-architecture; status=active |
| action | Requested capability, risk tier, mutating flag, approval requirement, and idempotency profile. | action=workspace.template.publish; risk=T3; mutating=true |
| resource | API route, workspace, component, MicroFunction, event topic, secret path, data object, repository, or environment. | resource.type=dynamic_workspace_component; classification=CONFIDENTIAL |
| context | Tenant/org, branch, channel, environment, request source, trace_id, business workflow state, and time. | env=UAT; channel=admin-builder; trace_id=... |
| evidence | Ticket, ADR/TDL, PR/MR, approval, policy version, tests, and rollback/compensation reference. | evidence_ref=EV-SEC-2026-0001 |
| Authorization Scenario | Required Decision | Fail-Closed Case |
| --- | --- | --- |
| Dynamic Workspace component visible | OPA returns allow or filtered layout for actor, tenant, classification, role, skill, and screen context. | Policy unavailable or unknown component classification means hidden/denied. |
| MicroFunction transaction executes | Actor has skill and resource scope; transaction has approved runtime config and policy binding. | Missing policy, stale config, absent audit sink, or exceeded classification blocks execution. |
| Kafka replay or DLQ reprocess | Requester has replay skill, bounded topic scope, idempotency proof, consumer compatibility, and approval. | Unbounded replay, missing idempotency key, or production topic without approval is blocked. |
| System Builder generates artifact | Request is classified, owner exists, source is registered, contract family selected, and generation remains draft/PR-bound. | Direct production mutation or self-approval is blocked. |

# 6. Secrets, Keys, Certificates, and Environment Boundary Implementation
| Secret Class | Approved Handling | Forbidden Handling |
| --- | --- | --- |
| Application secrets | Vault/OpenBao reference, environment-scoped path, short lease where feasible, rotation schedule, owner, and audit. | Hardcoded properties, committed .env, screenshots, prompt text, local notes, or CI artifacts. |
| Database credentials | Role-scoped, least privilege, non-shared, environment-specific, rotated, monitored, and bound to Flyway/runtime purpose. | Application superuser credentials, manual shared DBA credentials, production passwords in local dev. |
| Model/API keys | Route through LiteLLM or approved gateway; key material isolated from application code and prompts. | Direct provider SDK key in service code, agent config, prompt, or notebook. |
| Certificates/signing keys | Managed lifecycle, owner, issuance, renewal, revocation, and evidence. | Self-signed production bypass, expired certificate, private key in repository or chat. |
| Break-glass credentials | Sealed, time-bound, monitored, human-approved, post-reviewed, and rotated after use. | AI-agent invocation, unlogged sharing, standing emergency admin password. |

Local development rule. Developer workstations, devcontainers, tests, screenshots, Obsidian, and LLM Wiki must use synthetic data and secret references only. Real customer data, unrestricted production records, raw credentials, and Restricted artifacts are prohibited unless a named security exception, approved storage path, and evidence control exist.

# 7. Secure APIs, Events, MicroFunctions, and Dynamic Workspace Patterns
| Implementation Surface | Security Requirements | Evidence Required |
| --- | --- | --- |
| OpenAPI REST APIs | OIDC scheme, required scopes, SBAC skill, OPA policy ref, idempotency key for mutations, safe Problem Details, trace_id, request_id, evidence_ref. | Contract lint, security examples, negative auth tests, safe error tests, generated client tests. |
| AsyncAPI / Kafka / CloudEvents | Authenticated producer/consumer, topic ACL, schema compatibility, Avro registry, classification, traceparent, correlation_id, causation_id, idempotency key. | Schema validation, ACL proof, consumer idempotency tests, DLQ/replay test, event audit. |
| MicroFunction runtime | Standard security steps before business step: receive, correlate, resolve actor, classify, authorize, validate, idempotency, execute, audit, outbox, observe, respond. | Step trace, policy decision, audit record, test evidence, rollback/compensation path. |
| Dynamic Workspace | Backend resolves workspace, screens, components, and actions by policy; frontend renders filtered output only. Admin builder actions are maker-checker controlled. | Workspace policy test, layout hash, component filter audit, admin template approval, rollback evidence. |
| Outbox/inbox and DLQ/replay | Transactional outbox for state changes, inbox/dedup for consumers, bounded retries, DLQ with classified payload controls, controlled replay skill. | Outbox migration, dedup test, retry/DLQ test, replay approval, payload redaction test. |

# 8. System Builder, AI Agent, Model Route, Prompt, Retrieval, and Tool Security

System Builder and AI agents are security-relevant actors. They may analyze, recommend, draft, test, generate candidates, create PRs, prepare evidence, and request approved actions. They must not approve their own output, bypass review, hold production credentials, call model providers directly, bypass LiteLLM/guardrails, or mutate production.
| Control | Implementation Requirement | Block / Escalate When |
| --- | --- | --- |
| Agent registry | Agent has owner, purpose, lifecycle state, version, classification ceiling, skill grants, model route, tool scope, tests, and retirement path. | Unknown owner, expired review, unregistered tool, stale evaluation, or excessive classification. |
| Model routing | All calls use LiteLLM or approved private gateway with classification-aware route policy and guardrail checkpoints. | Direct provider SDK, unmanaged API key, or Confidential/Restricted data sent to ineligible route. |
| Prompt and retrieval | Prompt templates, retrieval sources, chunks, memory writes, and outputs are classified, source-cited, and ACL/SBAC filtered. | Prompt injection, poisoned source, stale retrieval, missing provenance, or unauthorized memory write. |
| Tool action | Tool manifests define allowed operations, input/output schema, risk tier, dry-run, idempotency, rollback, Harness route, OPA policy, and audit fields. | T3/T4 action without approval, T5 human-only action, missing rollback, or attempted self-approval. |
| Auto-Heal / Auto-Learn / Auto-Improve | Loops create proposal, evidence, tests, PR/MR, knowledge candidate, or improvement backlog item. | Silent mutation, production change, control weakening, unsourced learning, or unreviewed knowledge publication. |

# 9. DevSecOps Security Gates, Authenticated DAST, GitNexus, and Evidence Packs
| Gate | Minimum Required Checks | Promotion Blocker |
| --- | --- | --- |
| Source and branch | Branch protection, CODEOWNERS, signed commits where applicable, AI-use declaration, no secret files, no generated bypass code. | Direct main push, missing reviewer, missing AI-use/evidence statement. |
| SAST / SCA / secrets | Static analysis, dependency vulnerability, license, secrets scan, container/IaC scan, policy-as-code tests. | Critical/high unwaived finding, secret leak, vulnerable dependency without disposition. |
| Authenticated DAST | Approved non-prod scope, synthetic users, stable seed data, login/session handling, anti-CSRF handling, safe rate limit, evidence of tested roles. | DAST against production without approval, real data, uncontrolled account lockout, or missing remediation evidence. |
| SBOM / provenance / signing | SBOM, artifact digest, build image digest, SLSA/provenance target, signed packages/images where applicable. | Unknown artifact source, mutable tag without digest, missing SBOM/provenance for promotion-bound artifact. |
| GitNexus | Read-only code map, impact analysis, security-sensitive code map, architecture drift signal, affected tests, PR evidence summary. | GitNexus attempts commit, merge, approve, deploy, or replace tests/scans/human review. |
| Evidence pack | Test results, scan results, OPA decisions, policy tests, DAST output, remediation, architecture fitness, rollback, approval, and known limitations. | Missing AVCI evidence, missing rollback, missing owner, or waiver not approved. |

# 10. Observability, Runtime Toggles, Incident Response, and Continuous Improvement
| Signal / Control | Implementation Rule | Forbidden / Guardrail |
| --- | --- | --- |
| Logs | Use Log4j2 structured logs with trace_id, request_id, actor hash, service, action, outcome, policy_ref, evidence_ref, and classification. | No passwords, tokens, raw JWTs, secrets, raw PII, prompts with sensitive content, or unrestricted payloads. |
| OpenTelemetry | Traces, metrics, logs, resources, and spans follow shared semantic naming and carry safe correlation fields. | High-cardinality identifiers, secrets, raw customer IDs, or unbounded labels. |
| Sentry / error monitoring | Capture sanitized exception context, release, trace_id, safe stack summary, owner, and remediation link. | Raw request body, SQL with data, tokens, credentials, private keys, or Restricted content. |
| Runtime toggles | Security-sensitive toggles are configuration-governed, role/SBAC-protected, audit-logged, bounded, reversible, and default-safe. | Unaudited toggle change, disabling auth/policy/audit, or permanent debug logging in production. |
| Incident response | Security incidents create ticket, severity, containment, evidence preservation, forensic chain, RCA, corrective action, and recertification where applicable. | Informal chat-only response, unlogged manual fix, side-channel secret rotation, or missing post-incident review. |

# 11. Testing, Architecture Fitness, RACI, Roadmap, and AVCI Summary
| Test / Fitness Function | Purpose | Minimum Evidence |
| --- | --- | --- |
| RBAC / ABAC / SBAC tests | Prove role, attribute, skill, resource, environment, tenant, and classification enforcement. | Positive and negative tests, OPA decision logs, CI results. |
| OPA fail-closed tests | Prove unavailable/stale policy blocks protected actions. | OPA outage/stale-bundle tests, denial evidence. |
| Secret handling tests | Prove no secrets in source, prompts, logs, traces, screenshots, test fixtures, evidence, or artifacts. | Secrets scan, redaction test, telemetry inspection. |
| Authenticated DAST tests | Prove secure behavior through real login/session paths in non-prod using synthetic users. | DAST report, remediation evidence, safe test account evidence. |
| Architecture boundary tests | Block hardcoded roles, direct provider SDKs, direct Vault reads from domain code, frontend authority, cross-context DB writes, and adapter bypass. | ArchUnit/Semgrep/custom tests, GitNexus corroboration. |
| AI agent security tests | Prove unregistered tool, autonomy escalation, model route bypass, prompt injection, retrieval poisoning, and self-approval attempts are blocked. | Agent eval report, guardrail result, OPA denial evidence. |
| Reversibility tests | Prove policy rollback, secret rotation, feature disablement, config rollback, DLQ/replay safety, and break-glass closure. | Rollback drill, compensation record, closure evidence. |
| Role | Implementation Responsibility |
| --- | --- |
| Security Architecture | Owns security patterns, OPA/SBAC design, secrets standards, threat model, and exception review. |
| DevSecOps Lead | Owns pipeline gates, scan tools, SBOM/provenance, evidence pack, and remediation workflow. |
| Software Development Lead | Ensures services, APIs, MicroFunctions, frontend, and tests implement this guide without boundary drift. |
| Platform Engineering | Owns Keycloak, Vault/OpenBao, gateway, Kubernetes, CI runners, observability, and tool integrations. |
| QA/SDET | Owns positive, negative, security, DAST, architecture fitness, regression, and failure-mode tests. |
| AI Governance | Owns agent, model-route, prompt, guardrail, retrieval, and tool-action controls. |
| Internal Audit | Verifies evidence completeness, control operation, recertification, findings, and CAPA closure. |
| Phase | Target Outcome | Exit Criteria |
| --- | --- | --- |
| Phase 1 - Adoption | Approve 17A v1.2 and link with parent 17 v2.2, SBAC catalog, CI/CD, observability, and Dynamic Workspace standards. | ARB/CAB/security review complete; Obsidian/OpenKM evidence path ready. |
| Phase 2 - Policy contracts | OPA input/output schemas, SBAC skill mappings, and authorization decision logs implemented. | Policy tests pass; fail-closed cases evidenced. |
| Phase 3 - Secure delivery gates | SAST/SCA/secrets/IaC/container/authenticated DAST/SBOM/provenance/evidence pack pipeline enabled. | CI blocks missing or failing security evidence. |
| Phase 4 - Runtime assurance | Logs, traces, metrics, audit, Sentry, Loki, Tempo, Grafana, and runtime toggle audit are active. | Trace reconstruction and forbidden telemetry tests pass. |
| Phase 5 - Continuous improvement | Incident, Auto-Heal, Auto-Learn, and Auto-Improve loops produce governed proposals and remediation evidence. | No silent mutation; approved PRs/evidence/backlog items only. |

AVCI summary. Attributable: owners, roles, policies, tickets, PRs, agents, identities, and approvals are named. Verifiable: tests, OPA decisions, scans, telemetry, DAST, evidence packs, and audit records prove behavior. Classifiable: data, prompts, telemetry, logs, screenshots, evidence, models, and routes carry classification and handling rules. Improvable: incidents, findings, defects, DAST results, GitNexus findings, access reviews, and user feedback enter controlled improvement loops.

