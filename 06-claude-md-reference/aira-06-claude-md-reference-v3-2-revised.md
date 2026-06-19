---
title: "CLAUDE MD Reference"
doc_id: "AIRA-06"
version: "v3.2"
status: "revised"
category: "CLAUDE.md reference"
source_docx: "AIRA_06_CLAUDE_MD_Reference_v3.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 06-claude-md-reference
  - revised
  - aira-06
---



# CLAUDE MD Reference



AIRA
AI-Native Enterprise Platform

CLAUDE.md Reference

Repository AI Rules of Engagement | Human and AI-Assisted Development | Tool Adapter Governance | AVCI Evidence

Version v3.2 - Foundation Governance, Dynamic Workspace, MicroFunction, AI Tool, and Evidence Alignment Update
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-006 |
| Canonical Filename | AIRA_06_CLAUDE_MD_Reference_v3.2_Revised.docx |
| Version | v3.2 - Foundation Governance Alignment Update |
| Supersedes | 06-AIRA_CLAUDE_MD_Reference_v3.1_Aligned.docx |
| Status | Draft for ARB / CAB / DevSecOps / Security / AI Governance Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; Platform Engineering; AI Engineering; Knowledge Governance; Internal Audit |
| Primary Audience | Developers, repository maintainers, AI coding users, DevSecOps, QA/SDET, Security, DBA, Platform Engineering, AI Governance |
| Primary Authority Inputs | 01A v1.2; 01 v3.2; 01B v1.2; 02 v5.2; 03 v4.2; 04 v9.2; 05 v4.2; current AIRA source packs and revision-control register |
| Review Cadence | Quarterly; unscheduled on material AI tool, model route, MCP, repository, CI/CD, security, knowledge, Dynamic Workspace, or System Builder change |

Discipline First - Automation Second - Intelligence Third - AVCI Always

# Mandatory Practice Statement

AIRA repository rules are an enforceable control surface, not convenience notes. The root CLAUDE.md and directory-specific CLAUDE.md files must translate AIRA architecture, AVCI, security, testing, evidence, AI governance, Dynamic Workspace, MicroFunction, and DevSecOps rules into local behavior for human developers and approved AI assistants. Tool-specific adapters such as AGENTS.md, IDE rules, Codex instructions, MCP policies, or CI bundles may be generated from CLAUDE.md, but they must never weaken the canonical rules.

No AIRA change is acceptable merely because it compiles, renders, or passes a happy-path test. A change is acceptable only when it preserves or improves SOLID, Clean Architecture, DDD bounded contexts, ports/adapters, testability, security, observability, reversibility, rollbackability, runtime evidence, and AVCI compliance.

Figure 1. Repository rule hierarchy and inheritance model.

# 1. Executive Summary

This v3.2 revision updates the AIRA CLAUDE.md Reference after the foundation rework of 01A, 01, 01B, 02, 03, 04, and 05. It converts the repository rule model into a stronger, machine-enforceable, multi-assistant governance standard for human and AI-assisted development.

The document keeps the v3.1 purpose: define repository-local rules of engagement for AI-assisted and human development. It strengthens that purpose by aligning CLAUDE.md with Dynamic Workspace UX, MicroFunction runtime assembly, API/event contracts, DevSecOps evidence packs, GitNexus impact analysis, OPA/SBAC, guardrails, observability, heavy-transaction safety, and proposal-driven Auto-Heal / Auto-Learn / Auto-Improve loops.
| Outcome | Required v3.2 Treatment |
| --- | --- |
| One canonical repository rule baseline | Root CLAUDE.md governs every file; directory CLAUDE.md files may only tighten controls. |
| Many controlled adapters | AGENTS.md, IDE rules, Codex instructions, policy bundles, and MCP settings are generated projections and cannot become weaker alternate rulebooks. |
| Fail-closed AI-assisted work | If classification, policy, guardrail, evidence, CI, ownership, or reviewer controls are missing, the change stops at draft or recommendation state. |
| Machine enforcement | Hooks, CI, CODEOWNERS, branch protection, OPA/Conftest, architecture tests, secret scans, GitNexus, and evidence templates enforce the rules. |
| AVCI by construction | Every AI-assisted change records owner, source, prompt/tool use, affected files, tests, scans, evidence, classification, reviewer, and improvement path. |

# 2. Scope, Authority, and Precedence
| In Scope | Out of Scope |
| --- | --- |
| Application, infrastructure, prompt, guardrail, model-route, contract, migration, Dynamic Workspace, MicroFunction, workflow, knowledge, and test repositories. | Personal AI rule files, unmanaged local prompts, unapproved MCP servers, personal accounts, shadow agents, or unreviewed generated rules. |
| Root and directory-specific CLAUDE.md files, AGENTS.md, IDE rules, Codex/Claude Code instructions, policy bundles, pre-commit hooks, CI controls, PR/MR templates, and onboarding acknowledgements. | Direct production mutation, direct model-provider SDK calls, direct database/Kubernetes/CI/CD credentials held by agents, or AI approval of its own output. |
| Human-authored and AI-assisted changes by approved coding assistants, System Builder agents, DevSecOps agents, remediation agents, and equivalent tools. | Any tool workflow that bypasses 01A, AVCI, OPA/SBAC, guardrails, Harness, CODEOWNERS, CI, or human review. |
| Authority Level | Control | Repository Meaning |
| --- | --- | --- |
| L0 | Architecture Board / CAB / Security Governance | Final authority for exceptions, production-impacting controls, and conflict resolution. |
| L1 | 01A v1.2, 01 v3.2, 01B v1.2, 02 v5.2 | Architecture, AVCI, evidence, and blueprint controls that CLAUDE.md must enforce. |
| L2 | 03 Developer Guide, 04 Technology Stack, 05 Information Nervous System, 07 Skills, 08 Testing, 10 MicroFunction, 11 DevSecOps, 15 API, 16 Database, 17 Security | Developer, technology, knowledge, testing, API/event, database, security, and DevSecOps implementation rules. |
| L3 | This 06 CLAUDE.md Reference | Canonical repository rule-of-engagement standard for human and AI-assisted changes. |
| L4 | Repository CLAUDE.md, AGENTS.md, hooks, CODEOWNERS, OPA, CI, policy bundles | Executable local enforcement that cannot weaken higher authority. |
| L5 | PR/MR, evidence pack, reviewer decision, runtime telemetry | Operational proof and improvement feedback. |

Conflict rule: Root and child rules may be stricter than this standard but must not be weaker. If CLAUDE.md conflicts with the Engineering Blueprint, AVCI, 01A, Security, API, Database, or DevSecOps standards, the higher-authority standard governs and the repository rule must be corrected as an AVCI reconciliation item.

# 3. CLAUDE.md Operating Model
| Rule Area | Mandatory Treatment |
| --- | --- |
| Root baseline | Root CLAUDE.md applies to the full repository and establishes global AIRA behavior, coding, testing, security, AI, evidence, and review rules. |
| Directory hardening | High-risk directories require local CLAUDE.md with stricter rules for APIs, migrations, policies, prompts, guardrails, Dynamic Workspace, MicroFunctions, infra, secrets, and production operations. |
| Nearest file rule | Apply root plus every parent plus nearest directory rule. A nearest file wins only when stricter. |
| Generated adapters | AGENTS.md, IDE settings, task-agent rules, Codex instructions, MCP policies, and CI bundles must be generated from the canonical baseline and compared for rule weakening. |
| Version and evidence | Every rule change requires owner, version, rationale, reviewer, affected scope, tests, rollout plan, rollback path, and PR/MR AVCI evidence. |
| Rule lock | Production-bound repositories must reject unreviewed changes to CLAUDE.md, AGENTS.md, CODEOWNERS, branch rules, CI gates, security policies, and hooks. |

Root CLAUDE.md is mandatory for every AIRA repository.

Directory-specific CLAUDE.md is mandatory for high-risk source areas: /api, /domain, /application, /adapters, /migrations, /policies, /prompts, /guardrails, /workspace, /microfunctions, /infra, /ops, /evidence, and /ai-agents.

Rule changes are code-like governance changes and must be reviewed by CODEOWNERS and Security / DevSecOps / Architecture where applicable.

AI may propose repository rule changes, but a named human remains accountable for acceptance and promotion.

# 4. Enterprise Design Principles and Repository Enforcement
| EDP | Repository Rule Enforcement |
| --- | --- |
| EDP-01 SOLID | Reject code, prompts, agents, and MicroFunctions that mix responsibilities or depend on concrete adapters where ports are required. |
| EDP-02 Clean Architecture | Reject domain/application logic that depends on frameworks, UI, databases, models, queues, workflow engines, or provisioning tools. |
| EDP-03 DDD / Bounded Contexts | Require affected bounded context, owner, invariants, APIs/events, schemas, and runbooks in PR/MR evidence. |
| EDP-04 Ports and Adapters | Require explicit ports for Keycloak, OPA, Kafka, PostgreSQL, Redis, Flowable, Temporal, LiteLLM, OpenKM, GitNexus, and MCP/tool gateways. |
| EDP-06 Idempotency | Mutating commands, event consumers, callbacks, migrations, seeding, replay, and agent actions require idempotency keys and duplicate-safe tests. |
| EDP-08 Fail-Safe | Protected changes fail closed if identity, policy, guardrails, audit, CI, evidence, secrets, or model gateway controls are unavailable. |
| EDP-09 Human-in-the-Loop | High-impact, Restricted, production-impacting, destructive, low-confidence, or policy-exception changes require named human approval. |
| EDP-12 Observability | Require trace, metric, log, audit, model/tool usage, policy decision, evidence_ref, and safe redaction for critical paths. |
| EDP-13 Policy as Code | Authorization, admission, model routing, guardrails, deployment, environment, data-handling, and tool-action rules are versioned policy artifacts. |
| EDP-18 Progressive Autonomy | AI tools advance only when trust, skill, evidence, guardrails, approval, rollback, and monitoring permit. |
| EDP-20 AVCI | Every change must be attributable, verifiable, classifiable, and improvable before merge or promotion. |

# 5. Root CLAUDE.md Global Baseline
| Rule | Baseline Text to Carry into Repository CLAUDE.md |
| --- | --- |
| Architecture | Preserve SOLID, Clean Architecture, DDD bounded contexts, ports/adapters, testability, security, observability, reversibility, and AVCI evidence. |
| No direct model calls | Application code, scripts, notebooks, services, and agents must not call model providers directly. Use approved LiteLLM or private gateway aliases with guardrails. |
| No secrets or Restricted data | Do not expose passwords, tokens, secrets, raw PII, production data, KYC/account records, Restricted prompts, embeddings, private keys, or confidential files in prompts, logs, screenshots, tests, or docs. |
| Configuration first | Prefer MicroFunction configuration, templates, policies, contracts, DMN/rules, and reusable components before custom code. |
| Thin adapters | Controllers, UI components, infrastructure adapters, prompts, and SQL scripts must not contain business logic. |
| Evidence required | Every PR/MR requires AVCI summary, tests, scans, policy evidence, architecture fitness, rollback/forward-fix or compensation plan, and AI-use declaration. |
| Fail closed | If uncertain or if required controls are unavailable, stop and request architecture/security review. |
| AI authority boundary | AI may draft, analyze, summarize, test, and recommend. It may not approve, merge, deploy, bypass gates, grant access, or mutate production directly. |

# 6. Directory-Specific Rule Set Requirements
| Directory / Area | Required Additional Controls |
| --- | --- |
| /domain | No framework, persistence, queue, model, UI, or infrastructure dependencies. Preserve invariants and bounded context language. |
| /application | Use cases orchestrate ports and policies; no direct database, Kafka, Redis, Keycloak, OPA, LiteLLM, or external SDK calls. |
| /adapters | Adapters implement ports only. Secrets, retries, timeouts, redaction, error mapping, telemetry, and policy outcomes must be explicit. |
| /api /contracts | OpenAPI/AsyncAPI, CloudEvents, Avro/JSON Schema, Problem Details, idempotency, versioning, schema compatibility, and contract tests are mandatory. |
| /migrations | Flyway-only schema and seed changes. No manual DDL. Include rollback/forward-fix, checksum, RLS/classification, and DBA review evidence. |
| /workspace | Dynamic Workspace components, templates, AI Panel, Admin Builder, accessibility, responsive behavior, safe states, OPA/SBAC, and evidence bindings must be backend-governed. |
| /microfunctions | Configuration-first assembly; transaction code, step order, idempotency, audit/outbox, policy decision, trace_id, rollback, DLQ/replay, and resilience tests required. |
| /prompts /guardrails | Prompts and guardrails are governed artifacts with classification, model route, retrieval policy, evaluation, red-team evidence, and output controls. |
| /infra /ops | IaC/GitOps only, pinned versions, secrets via Vault/approved store, SAST/SCA/IaC scan, SBOM/provenance, rollback and environment rebuild evidence. |
| /ai-agents | Agent identity, owner, SBAC skill, OPA policy, trust tier, tool manifest, model route, guardrails, monitoring, kill switch, recertification, and retirement controls. |

Figure 2. Controlled tool adapters generated from the canonical CLAUDE.md baseline.

# 7. Machine-Enforced Controls
| Control | Required Enforcement |
| --- | --- |
| Pre-commit | Secret scan, formatting, lint, CLAUDE.md weakening check, generated adapter drift check, policy bundle validation, and optional local unit smoke tests. |
| CI strict mode | Build, unit/component/contract tests, mutation where applicable, SAST, SCA, secrets scan, IaC scan, dependency license scan, OPA/Conftest, ArchUnit, Semgrep, SonarQube, DAST where applicable. |
| CODEOWNERS | Require owners for architecture, security, database, API contracts, Dynamic Workspace, MicroFunctions, policies, prompts, guardrails, workflows, infra, and production operations. |
| Branch protection | Require status checks and approving reviews before merge to protected branches; direct commits and skipped checks are prohibited for production-bound work. |
| GitNexus | Read-only code intelligence for code maps, impact, affected tests, architecture drift, and PR/MR evidence. It must not approve, merge, deploy, or mutate. |
| OPA/SBAC | Policy decisions govern access, tool actions, model routes, retrieval eligibility, Dynamic Workspace actions, agent actions, and deployment gates. |
| Evidence publishing | CI and PR/MR must persist evidence pack references with owner, source, commit, classification, test/scans, policy decisions, rollback, and improvement items. |

# 8. AI Tool Adapter and Multi-Assistant Governance
| Tool / Adapter | AIRA Required Treatment |
| --- | --- |
| Claude Code | Use root and directory CLAUDE.md, organization-managed instructions where available, approved MCP only, read-only retrieval by default, no production-impacting command execution outside Harness/SBAC/OPA. |
| Codex / ChatGPT coding surfaces | Use AGENTS.md and repository-local rules derived from CLAUDE.md, issue/ADR context, CODEOWNERS, CI strict mode, PR AVCI summary, no direct production credentials, and no gate bypass. |
| IDE assistants | Consume generated IDE rules from CLAUDE.md. They may suggest code and tests but cannot weaken repository rules or bypass branch protection. |
| System Builder agents | May analyze, recommend, draft artifacts, and prepare PR-ready changes. They must not approve, merge, deploy, provision uncontrolled tools, or mutate production. |
| MCP / connectors | Read-only by default. State-changing tools require trusted server, least privilege, tool manifest, OPA/SBAC decision, audit log, dry-run where feasible, human approval, and rollback/compensation path. |
| GitNexus | Provides read-only derivative impact evidence. It is not the source of truth, not a security scanner replacement, and not an autonomous execution path. |

All model access must route through approved LiteLLM or private/on-prem gateway aliases; direct model SDK usage in application code is prohibited.

NeMo Guardrails or approved equivalent checkpoints must cover input, retrieval, execution/tool action, and output when AI assists protected workflows.

AI-generated code, tests, policies, migrations, prompts, guardrails, documentation, or diagrams remain drafts until human-reviewed and evidenced.

# 9. Dynamic Workspace and MicroFunction Repository Rules
| Area | Repository Rule |
| --- | --- |
| Dynamic Workspace UX | Frontend configuration and UX generation are not business authority. Backend APIs, OPA/SBAC, MicroFunctions, classification, and evidence controls govern what may appear or execute. |
| Admin Builder and templates | Template changes require maker-checker, version, classification, contract binding, accessibility, responsive testing, rollback, and activation evidence. |
| AI Assistant Panel | Panel actions must separate advice, proposal, draft artifact, request tool action, and human-approved execution. No UI-side authorization or AI approval. |
| Experience Blocks / Packs | Blocks and packs must have owner, source, component contract, capability binding, policy binding, telemetry profile, rollback path, and evidence_ref. |
| MicroFunction runtime | Transactions require configured standard steps for receive, correlate, classify, authorize, validate, idempotency, execute, audit, outbox, observe, respond, and compensate. |
| Runtime toggles | Performance/debug logging may be tuned; security, audit, policy denial, classification, model-route, guardrail, evidence, and privileged-action telemetry must remain non-disableable. |

# 10. API, Event, Database, and Workflow Rules
| Control Family | Repository Rule |
| --- | --- |
| OpenAPI | Contract-first REST changes; no controller-first accidental APIs; include Problem Details, idempotency, pagination, correlation, classification, and contract tests. |
| AsyncAPI / Kafka | Topic/event changes require AsyncAPI, CloudEvents envelope, schema reference, idempotent consumer rule, DLQ/replay, and compatibility evidence. |
| Avro / JSON Schema | Schema evolution must be backward/forward compatible or explicitly versioned with migration and consumer communication evidence. |
| Outbox and replay | State-changing integration uses transactional outbox, deduplication, retry-safe publishing, DLQ analysis, replay evidence, and compensation path. |
| Flyway | All schema, seed, RLS, extension, index, view, and data-fix changes go through Flyway or approved migration workflow. No manual production DDL. |
| Workflow | Flowable/Temporal changes require workflow contract, idempotency, timeout/retry, compensation, human approval, audit, and replay-safe tests. |

# 11. Auto-Heal, Auto-Learn, and Auto-Improve Rules

Repository rules must keep all continuous-improvement loops proposal-driven. Automation may detect, analyze, recommend, draft, test, simulate, and open a review-ready PR/MR or change request, but it must not silently mutate canonical standards, code, prompts, policies, guardrails, environments, production data, or runtime behavior.
| Loop | Allowed | Blocked Without Human Approval |
| --- | --- | --- |
| Auto-Heal | Detect incident, retrieve evidence, propose fix, generate tests, create branch/PR, run non-prod validation, prepare rollback. | Direct production patch, suppression of evidence, disabling policy/security gates, bypassing CAB, or changing secrets/identity. |
| Auto-Learn | Summarize recurring findings, propose rule improvements, update draft knowledge artifact, generate retrieval candidate, recommend fitness check. | Publishing unreviewed memory/retrieval content as authoritative or weakening CLAUDE.md/AGENTS.md rules. |
| Auto-Improve | Draft refactor, improve tests, harden policy, propose performance tuning, update templates, recommend architecture decision. | Merging refactor, modifying production config, changing public API/event contract, or promoting autonomy without approval. |

Figure 3. AI-assisted development delivery and evidence gate.

# 12. PR/MR Evidence and Completion Criteria
| Evidence Field | Mandatory Content |
| --- | --- |
| Attributable | Owner, developer, reviewer/checker, ticket/ADR/TDL, branch, commit, source standards, AI tools/models used, prompt intent, files affected. |
| Verifiable | Build, unit/component/contract tests, OPA policy tests, security scans, authenticated DAST where applicable, architecture fitness, GitNexus impact, runtime evidence. |
| Classifiable | Data classification, model-route eligibility, secrets/PII handling, log redaction, evidence storage, retention, retrieval eligibility. |
| Improvable | Known limitations, backlog items, defect/RCA links, rule improvement candidates, prompt/guardrail improvement, follow-up owner. |
| Architecture impact | SOLID, Clean Architecture, DDD, ports/adapters, idempotency, determinism, resilience, rollbackability, and AVCI impact. |
| Promotion decision | CODEOWNERS approval, maker-checker, CAB/ARB/Security/DBA approval where required, rollback/forward-fix or compensation plan, post-promotion monitoring. |

# 13. RACI and Ownership
| Role | Responsibilities |
| --- | --- |
| Solutions Architecture Office / IT Head | Owns canonical CLAUDE.md Reference, approves major rule changes, resolves architecture conflicts, and governs source baseline. |
| Software Development Lead | Ensures repository rules are understood, enforced, and evidenced in PR/MR workflows. |
| DevSecOps Lead | Implements hooks, CI strict mode, branch protection, CODEOWNERS, evidence publishing, GitNexus, and policy gates. |
| Security Architecture | Owns secrets hygiene, classification, OPA/SBAC, model/tool risk, abuse cases, authenticated DAST, and remediation evidence. |
| QA/SDET | Owns deterministic test evidence, regression coverage, architecture fitness, Playwright, contract, mutation, and resilience tests. |
| AI Governance | Owns AI tool eligibility, model-route rules, guardrails, agent capabilities, MCP/connectors, and progressive autonomy controls. |
| Repository Maintainers | Maintain root/directory CLAUDE.md, generated adapters, local hooks, rule drift checks, and onboarding acknowledgements. |
| Internal Audit | Reviews evidence completeness, traceability, separation of duties, retention, and control effectiveness. |

# 14. Roadmap and Acceptance Criteria
| Phase | Exit Criteria |
| --- | --- |
| Phase 1 - Baseline publication | Root CLAUDE.md template, directory templates, AGENTS.md projection, PR evidence template, and ownership map approved. |
| Phase 2 - Repository rollout | Priority repositories adopt CLAUDE.md, CODEOWNERS, branch protection, pre-commit, CI strict mode, secret scans, and evidence publishing. |
| Phase 3 - Tool adapter hardening | Codex, Claude Code, IDE assistants, MCP/connectors, GitNexus, and System Builder use generated rules and fail-closed permissions. |
| Phase 4 - Fitness and policy gates | OPA/Conftest, ArchUnit, Semgrep, SonarQube, SAST/SCA/DAST, contract tests, and GitNexus evidence become required for production-bound PRs. |
| Phase 5 - Continuous improvement | Auto-Heal/Learn/Improve proposals update repository rules only through PR/MR, human review, tests, and evidence. |

Root and high-risk directory CLAUDE.md files exist and are versioned.

Generated adapters are checked for rule weakening before commit.

Protected branches require status checks and CODEOWNERS approval.

Direct model-provider SDK calls, secrets in prompts/logs/tests, and production-impacting AI tool execution are blocked or flagged.

PR/MR evidence proves AVCI, architecture, security, tests, observability, rollback, and human review.

# 15. Open Reconciliation Items
| Item | Required Register Action |
| --- | --- |
| 06 numbering collision | The CLAUDE.md Reference and Revision Control Matrix both use 06 in the current list. Keep CLAUDE.md as AIRA-DOC-006 only if the matrix is explicitly registered as the revision-control register artifact or renumbered in 00D. |
| AGENTS.md projection standard | Confirm whether AGENTS.md should be a formal companion document or generated repository artifact controlled by this 06 standard. |
| MCP connector policy details | Cross-reference 42H/42M and security standards to ensure connector permission, audit, prompt-injection, and revocation rules are identical. |
| Dynamic Workspace rule templates | Add concrete directory templates for /workspace, /experience-packs, /admin-builder, /ai-panel, /components, and /templates in the rollout pack. |
| Runtime telemetry toggles | Ensure non-disableable security/audit/evidence signal rules are propagated to observability, SRE, Dynamic Workspace, and DevSecOps standards. |
| Revision matrix update | Record v3.2 supersedence and affected companion files after the foundation batch is complete. |

# 16. AVCI Compliance Summary
| AVCI Property | Evidence in This v3.2 Revision |
| --- | --- |
| Attributable | Defines owner, co-owners, source baseline, supersedence, repository roles, tool-adapter ownership, PR/MR ownership, and reviewer accountability. |
| Verifiable | Requires hooks, CI strict mode, tests, scans, OPA/SBAC, architecture fitness, GitNexus impact, evidence packs, and human review before merge/promotion. |
| Classifiable | Requires classification-aware prompts, logs, tests, retrieval, model-route eligibility, evidence storage, and protection of secrets/PII/Restricted data. |
| Improvable | Defines Auto-Heal/Learn/Improve candidate loops, rule-change PRs, backlog linkage, telemetry review, and open reconciliation items for future updates. |

Final Control Statement: AIRA CLAUDE.md is not a suggestion file. It is the local, executable expression of AIRA governance inside each repository. Any human or AI-assisted change that weakens repository rules, bypasses evidence, or obscures accountability is non-conforming and must be rejected, remediated, or escalated.

