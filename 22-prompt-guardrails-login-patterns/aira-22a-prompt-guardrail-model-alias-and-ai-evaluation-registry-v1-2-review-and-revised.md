---
title: "Prompt Guardrail Model Alias and AI Evaluation Registry"
doc_id: "AIRA-22A"
version: "v1.2"
status: "revised"
category: "Prompt guardrails and login patterns"
source_docx: "AIRA_22A_Prompt_Guardrail_Model_Alias_and_AI_Evaluation_Registry_v1_2_Review_and_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 22-prompt-guardrails-login-patterns
  - revised
  - aira-22a
---



# Prompt Guardrail Model Alias and AI Evaluation Registry



AIRA Prompt, Guardrail, Model Alias, and AI Evaluation Registry

Prompt Governance | Guardrail Profiles | LiteLLM Model Routes | AI Evaluation Evidence | Runtime Registry Control

Review, Alignment, Simplification, and Revised Standard

Recommended Version: v1.2

Status: Draft for Architecture Review Board / CAB / AI Governance Review

Classification: INTERNAL CONFIDENTIAL

Prepared for: Enterprise Architecture, AI Governance, Software Development, DevSecOps, Security, QA/SDET, Platform Engineering, SRE, Data Governance, and Internal Audit

Owner: Solutions Architecture Office / IT Head

Review Date: 16 June 2026

Mandatory Practice Statement

No AIRA prompt, guardrail, model alias, fallback route, tool-action policy, retrieval profile, evaluation dataset, benchmark, or AI runtime configuration is production-ready unless it is attributable, verifiable, classifiable, improvable, versioned, tested, approved, registered, observable, reversible, and governed by LiteLLM, guardrails, OPA/SBAC, Harness where applicable, CI/CD evidence, and human accountability.

# Document Control
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-022A |
| Document Title | AIRA Prompt, Guardrail, Model Alias, and AI Evaluation Registry |
| Recommended Version | v1.2 - AI Runtime Registry, Evaluation Evidence, Model Route, and Guardrail Lifecycle Alignment Update |
| Source Document Reviewed | 22A-AIRA_Prompt_Guardrail_Model_Alias_and_AI_Evaluation_Registry_v1.1_Aligned.docx |
| Supersedes | 22A-AIRA_Prompt_Guardrail_Model_Alias_and_AI_Evaluation_Registry_v1.1_Aligned.docx, upon approval |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Architecture Review Board / CAB / AI Governance / Security / DevSecOps Review |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; AI Governance; DevSecOps Lead; Security Architecture; QA/SDET Lead; Platform Engineering; SRE / Operations; Data Governance; Internal Audit |
| Primary Audience | Enterprise Architects; Developers; DevSecOps; Security; QA/SDET; AI Engineers; System Builder owners; AI Agent owners; Platform Engineers; SRE; Internal Audit |
| Source Pack Location | AIRA Word Source Pack 05 of 15 |
| Related AIRA Documents | 01A; 01/01B AVCI; 02 Engineering Blueprint; 03 Developer Guide; 04 Technology Stack; 05 Information Nervous System; 06 CLAUDE.md Reference; 10-10E MicroFunction baseline; 11/11A DevSecOps; 17/17A Security; 19 GitNexus; 20 CI/CD Evidence Pack; 23B Architecture Fitness; 30/30A Change and Reversibility; 31/31A Operations and Observability; 42 AI Governance; 42D-42S AI Agent control set |
| External Alignment References | NIST AI RMF 1.0; NIST AI 600-1 Generative AI Profile; OWASP Top 10 for LLM Applications 2025; OpenTelemetry GenAI semantic conventions; NIST SSDF; SLSA v1.2; OWASP ASVS; OPA policy-as-code guidance; LiteLLM and NeMo Guardrails as approved AIRA technology positions |
| Change Summary | Updated 22A from v1.1 to v1.2 to align the AI registry with the revised AI Governance v1.2, Architecture Fitness v1.2, Observability v1.2, Security v2.2, DevSecOps v3.2, CI/CD Evidence Pack v1.2, GitNexus v1.3, MicroFunction baseline, System Builder controls, prompt/guardrail lifecycle, evaluation evidence, rollback, runtime telemetry, and AVCI governance. |
| Review Queue Impact | Marks Sequence 43 as completed and recommends Sequence 44 as 42D AI Agent Identity Lifecycle and Credential Hygiene Standard. |

# Table of Contents Placeholder

Insert a Microsoft Word automatic Table of Contents here before final publication. Recommended setting: show levels 1 to 3. Update all fields after final approval and before distribution.

# 1. Executive Review Summary

The v1.1 source is strong and directionally aligned with AIRA. It correctly treats prompts, guardrails, model aliases, tool-action policies, and AI evaluation datasets as first-class engineering artifacts. It also correctly establishes that application code must use LiteLLM aliases only, that guardrails must cover input, retrieval, execution, and output checkpoints, and that AI promotion requires golden datasets, adversarial tests, regression results, approval, and evidence.

The v1.2 revision improves operational precision. It makes the registry an enforceable runtime control, not merely a reference inventory. It adds tighter lifecycle controls, model-route eligibility rules, guardrail profile governance, tool-action policy binding, evaluation evidence thresholds, CI/CD gate expectations, observability fields, rollback and kill-switch linkage, and System Builder / AI Agent consumption rules.

# 2. Alignment Findings
| Alignment Area | Required Treatment |
| --- | --- |
| 42 AI Governance v1.2 | 22A is the implementation registry that operationalizes AI governance. Every prompt, guardrail, model alias, evaluation dataset, and route policy must be registered, tested, approved, observable, and reversible. |
| 23B Architecture Fitness | Fitness checks must detect direct provider SDK calls, unregistered prompts, hardcoded model names, missing guardrails, missing evaluation evidence, weak citations, unsafe tool-action policies, and stale model routes. |
| 31A Observability | AI calls must emit correlation-safe evidence: actor, agent, prompt version, guardrail profile, model alias, route, retrieval pack, evaluation profile, policy decision, tool action, and output classification. |
| 17/17A Security | Model routes, prompts, guardrails, and tool-action policies must enforce classification ceilings, least privilege, OPA/SBAC, secrets hygiene, safe logging, and fail-closed behavior. |
| 11/11A and 20 DevSecOps | Registry artifacts require PR/MR review, tests, CI/CD validation, SAST/SCA/secrets checks where applicable, evidence packs, CODEOWNERS, and promotion controls. |
| 10-10E MicroFunction | MicroFunctions and backend services must call approved aliases and registry-backed prompt/guardrail profiles only; AI-enabled steps must remain observable, idempotent, policy-controlled, and reversible. |
| 05/13/21A/25/26B Knowledge Governance | Retrieval prompts and RAG rules must preserve source authority, ACL filtering, freshness, conflict detection, citation requirements, and quarantine for stale or unsafe sources. |
| System Builder and AI Agents | System Builder may draft registry artifacts and propose updates. It must not activate prompts, routes, guardrails, agents, or tool policies without review, CI evidence, and approval. |

# 3. Review and Gap Analysis
| Finding Type | Board Decision |
| --- | --- |
| Retain | Keep the registry-first model, LiteLLM alias-only rule, NeMo guardrail profiles, AI evaluation datasets, lifecycle states, RACI, evidence manifest, and approval discipline. |
| Correct | Update references from older foundation versions to the revised AIRA candidate baselines: 01A, AVCI, Blueprint, Developer Guide, Technology Stack, AI Governance, MicroFunction, DevSecOps, Security, Observability, and Fitness Functions. |
| Strengthen | Make the registry enforceable at runtime through route lookup, guardrail resolution, policy decisions, telemetry, and CI/CD validation rather than treating it as documentation only. |
| Strengthen | Add tool-action policy metadata: Harness binding, SBAC skill, OPA policy, autonomy tier, approval route, idempotency requirement, rollback/compensation path, and blocked actions. |
| Strengthen | Add evaluation gates for groundedness, citation coverage, unsafe-output false negatives, prompt injection, data leakage, tool misuse, retrieval poisoning, and autonomy drift. |
| Simplify | Group the registry into five artifact families: prompts, guardrails, model aliases, tool-action policies, and evaluation/evidence assets. |
| Add | Runtime diagnostic toggles may tune sampling and verbosity, but audit, security decisions, policy outcomes, model-route evidence, guardrail results, idempotency records, outbox records, and critical AI evidence must not be disabled. |
| Add | Auto-Heal, Auto-Learn, and Auto-Improve may propose registry updates only. Activation requires tests, owner review, CI evidence, and approved change path. |

# 4. Revised AIRA Standard

## 4.1 Purpose

This standard defines the registry and governance model for AIRA prompts, guardrails, LiteLLM model aliases, fallback routes, tool-action policies, retrieval profiles, AI evaluation datasets, golden tests, adversarial tests, regression reports, and AI evidence manifests. It converts AI behavior into versioned, testable, reviewable, observable, reversible, and evidence-producing engineering artifacts.

## 4.2 Scope
| In Scope | Out of Scope |
| --- | --- |
| Prompt templates, system instructions, prompt fragments, prompt variables, retrieval-pack rules, output schemas, prompt tests, and prompt retirement records. | Private, unmanaged, personal, or one-off prompts that are not promoted into AIRA-controlled execution. |
| Guardrail profiles covering input, retrieval, execution, and output checks, including blocked-action rules, citation requirements, data leakage prevention, and fail-closed behavior. | Provider-native safety settings hidden in vendor consoles without AIRA registry evidence. |
| LiteLLM aliases, provider routes, fallback routes, classification ceilings, budgets, allowed use cases, evaluation profiles, and telemetry requirements. | Direct provider SDK calls, hardcoded model names, personal API keys, or untracked fallback logic. |
| Tool-action policies, Harness bindings, SBAC skills, OPA policies, autonomy tiers, trust thresholds, approval routes, and rollback/compensation requirements. | Agents directly executing tools, holding production credentials, or bypassing Harness/SBAC/OPA. |
| Evaluation datasets, adversarial tests, golden answers, prompt-injection tests, groundedness checks, evidence manifests, CI reports, and recertification records. | Unversioned manual tests, screenshots, or chat outputs that cannot be reproduced or audited. |

## 4.3 Authority and Precedence

1. 22A is the authoritative registry companion for prompt, guardrail, model alias, tool-action policy, retrieval profile, and AI evaluation artifacts.

2. 42 AI Governance is the parent AI governance authority. 22A must implement, not weaken, 42.

3. 17/17A govern security, classification, secrets, identity, access control, and fail-closed behavior.

4. 11/11A and 20 govern CI/CD, evidence packs, security gates, SBOM/provenance, and promotion controls.

5. 31A governs AI runtime telemetry, evidence correlation, dashboards, alerting, and trace reconstruction.

6. 23B governs automated fitness checks that prevent unregistered AI runtime behavior.

7. Where a conflict exists, the stricter control applies and the issue must be logged as an AVCI reconciliation item.

## 4.4 Non-Negotiable Registry Principles
| ID | Principle | Operational Meaning |
| --- | --- | --- |
| AI-REG-01 | Registry First | AI behavior is controlled by approved registry artifacts, not ad-hoc prompts, hardcoded model names, hidden environment variables, or personal AI workspace settings. |
| AI-REG-02 | LiteLLM Aliases Only | Applications, services, scripts, notebooks, MicroFunctions, System Builder, and agents must use approved model aliases. Direct model-provider calls are prohibited. |
| AI-REG-03 | Four-Rail Guardrails | Input, retrieval, execution, and output guardrails are mandatory where AI interacts with AIRA data, controlled actions, tools, or decision support. |
| AI-REG-04 | Classification-Aware Routing | Each alias and prompt has an approved classification ceiling. Confidential or Restricted data must not be routed to disallowed providers, tools, prompts, or logging paths. |
| AI-REG-05 | Evaluation Before Activation | Prompts, guardrails, model routes, and tool policies require golden tests, adversarial tests, regression tests, and acceptance thresholds before activation. |
| AI-REG-06 | Evidence by Default | Every AI call and registry promotion must be reconstructable through prompt version, guardrail version, model alias, retrieval pack, policy decision, output classification, and evidence reference. |
| AI-REG-07 | Human Accountability | AI and System Builder may draft registry updates. Human owners and required governance bodies approve activation, exceptions, rollback, and retirement. |
| AI-REG-08 | Reversible Runtime | Prompt, guardrail, model alias, and tool policy changes must support rollback, deactivation, fallback, route disablement, evaluation re-run, or safe stop. |

## 4.5 Registry Artifact Families
| Artifact Family | Mandatory Registry Content |
| --- | --- |
| Prompt Artifact | Template, variables, purpose, owning bounded context, classification ceiling, expected output schema, source dependencies, retrieval rules, safety instructions, test suite, and rollback version. |
| Guardrail Profile | Input rail, retrieval rail, execution rail, output rail, blocked content, blocked actions, citation requirements, redaction behavior, fail-closed handling, and bypass tests. |
| Model Alias | LiteLLM alias, provider route, fallback alias, budget policy, allowed use cases, classification ceiling, guardrail profile, evaluation profile, route telemetry, and retirement date. |
| Tool-Action Policy | Tool name, action scope, Harness binding, SBAC skill, OPA policy, autonomy tier, approval route, idempotency requirement, rollback/compensation path, evidence sink, and prohibited actions. |
| Evaluation Asset | Dataset manifest, golden cases, adversarial cases, expected outputs, thresholds, run reports, model/prompt/guardrail versions tested, risk findings, waivers, and recertification date. |

## 4.6 AI Artifact Lifecycle
| Lifecycle State | Required Treatment |
| --- | --- |
| DRAFT | Created in branch or controlled sandbox. Requires owner, purpose, classification, non-goals, source references, test plan, and rollback candidate. |
| REVIEW | Reviewed by owner, Security, AI Governance, DevSecOps, QA, and affected domain owners based on risk and classification. |
| EVALUATED | Golden tests, adversarial tests, guardrail tests, route tests, policy tests, citation tests, and regression checks executed and retained. |
| APPROVED | Approved through maker-checker and required CAB/ARB path. Production-bound or high-risk changes require formal evidence pack. |
| ACTIVE | Enabled only through registry-controlled activation. Telemetry, evidence, alerting, and rollback path are operational. |
| SUPERSEDED | No longer default eligible. Preserved for traceability, rollback, audit, and comparison. |
| SUSPENDED | Blocked due to incident, stale evaluation, unsafe output, policy drift, expired approval, unsupported route, or missing evidence. |
| RETIRED | Deactivated; route/tool access removed; references updated; evidence retained; retrieval projections marked superseded. |

## 4.7 Required Registry Metadata
| Metadata Area | Mandatory Fields |
| --- | --- |
| Identity | artifact_id, artifact_type, version, status, owner, co-owners, reviewers, bounded_context, repository_path, source_hash, change_request_ref. |
| Classification | classification_ceiling, allowed_data_classes, prohibited_data_classes, retention_rule, redaction_rule, evidence_classification, retrieval_eligibility. |
| Runtime Binding | prompt_ref, guardrail_profile, model_alias, fallback_alias, tool_action_policy, opa_policy_ref, sbac_skill_ref, harness_action_ref, budget_policy. |
| Testing | evaluation_profile, dataset_id, test_suite, adversarial_suite, acceptance_thresholds, last_eval_run, next_review_due, waiver_ref. |
| Observability | trace_required, metric_required, audit_required, dashboard_ref, alert_ref, evidence_schema_ref, forbidden_fields, diagnostic_toggle_policy. |
| Reversibility | rollback_version, deactivate_flag, fallback_route, compensation_path, cache_invalidation, retrieval_quarantine_rule, retirement_plan. |

## 4.8 Evaluation and Promotion Gates
| Promotion Gate | Pass Condition |
| --- | --- |
| Gate 1 - Static Registry Validation | Schema validation, required fields, owner, classification, source hash, repository path, and lifecycle state are complete. |
| Gate 2 - Security and Classification | Secrets scanning, prohibited data check, classification ceiling check, allowed route check, redaction check, and fail-closed behavior are verified. |
| Gate 3 - Guardrail Test | Input, retrieval, execution, and output rails pass positive, negative, bypass, injection, leakage, and blocked-action tests. |
| Gate 4 - Model Route Test | LiteLLM alias resolves correctly; fallback is registered; budget, allowed use case, route telemetry, and classification ceiling are enforced. |
| Gate 5 - Evaluation Test | Golden dataset, adversarial dataset, citation coverage, groundedness, unsafe-output false negatives, and unsupported-claim thresholds pass. |
| Gate 6 - Tool Policy Test | Harness binding, SBAC skill, OPA policy, autonomy tier, idempotency, approval route, rollback/compensation, and blocked-action tests pass. |
| Gate 7 - Evidence and Observability | Trace, log, metric, audit, dashboard, alert, evidence manifest, and retention references are present and classification-safe. |
| Gate 8 - Human Approval | Owner, maker-checker, Security, AI Governance, DevSecOps, QA, ARB/CAB, or model-route approval is captured based on risk. |

## 4.9 Runtime Toggle Policy

AIRA may tune AI runtime diagnostics to manage performance, cost, and data minimization. Examples include log level, trace sampling, token/cost metric collection, payload capture suppression, and debug prompt visibility. However, the following must not be disabled for protected or production-bound flows: audit events, security logs, OPA/SBAC decisions, guardrail outcomes, model alias decisions, route denials, tool-action requests, human approval records, idempotency records, outbox records, critical error evidence, incident evidence, and rollback or deactivation evidence.

## 4.10 System Builder and AI Agent Usage Rules

1. System Builder may propose prompt, guardrail, model alias, tool-action policy, or evaluation updates, but may not activate them without human approval and CI/CD evidence.

2. AI agents must resolve their approved prompts, guardrails, model aliases, and tool policies from the registry at runtime or through controlled compiled configuration derived from the registry.

3. Agents must not create their own hidden prompts, self-approve prompt changes, bypass LiteLLM, bypass guardrails, bypass OPA/SBAC, or bypass Harness.

4. Agent-generated registry updates remain candidate artifacts until evaluated, reviewed, approved, and promoted through the required path.

5. Any registry artifact associated with an AI incident must be suspendable, traceable, revertible, and linked to the incident record and evidence pack.

## 4.11 Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop
| Loop Step | Required Treatment |
| --- | --- |
| Issue Detection | Detect prompt failure, citation weakness, model-route denial, guardrail bypass attempt, cost anomaly, unsafe output, stale evaluation, tool misuse, or drift signal. |
| Evidence Retrieval | Retrieve approved traces, logs, evaluation reports, prompt versions, guardrail outcomes, model aliases, source citations, and incident references. |
| Candidate Proposal | Generate a candidate prompt, guardrail, route, evaluation, policy, or documentation update with owner, risk, classification, expected benefit, and rollback path. |
| Testing | Run golden, adversarial, regression, classification, guardrail, route, tool-action, and observability tests in CI or controlled evaluation environment. |
| Human Approval | Named owner and required review boards approve or reject. AI may not promote the update. CAB/ARB applies for production-impacting or high-risk registry changes. |
| Activation and Monitoring | Activate through registry-controlled versioning, observe telemetry, retain evidence, and create improvement backlog or rollback if needed. |

# 5. Validation Checklist
| Checklist Item | Acceptance Condition |
| --- | --- |
| Registry Schema | All registry artifacts have required metadata, owner, classification, version, lifecycle state, evidence path, and rollback plan. |
| No Direct Provider Calls | CI detects and blocks direct provider SDK calls, hardcoded model names, personal keys, and hidden fallbacks. |
| Guardrails | Input, retrieval, execution, and output guardrails are registered, tested, observable, and fail closed. |
| Evaluation | Golden, adversarial, regression, grounding, citation, leakage, injection, and tool-misuse tests meet thresholds. |
| Security | OPA/SBAC, Harness, secrets hygiene, classification ceilings, route eligibility, and blocked-action rules pass. |
| Observability | AI runtime emits trace, metrics, logs, audit, model route, guardrail, retrieval, evaluation, and evidence references safely. |
| Promotion | CODEOWNERS, maker-checker, Security, AI Governance, DevSecOps, QA, and CAB/ARB approvals exist where triggered. |
| Reversibility | Rollback, deactivation, route disablement, guardrail rollback, cache invalidation, retrieval quarantine, and retirement path are tested. |

# 6. Anti-Patterns and Rejection Rules
| Anti-Pattern | Required Response |
| --- | --- |
| Unregistered prompt in production | Reject and convert to registry candidate with owner, classification, tests, and evidence. |
| Direct provider SDK call | Reject; route through approved LiteLLM alias or approved private gateway. |
| Hardcoded model name or fallback | Reject; move to model alias registry with route, fallback, budget, guardrail, and evaluation metadata. |
| Guardrail disabled for convenience | Reject; fail closed or approve time-bound waiver only if compensating controls exist. |
| One-off manual evaluation | Reject as promotion evidence; require reproducible dataset, run report, and retained evidence. |
| Agent creates or activates its own policy | Reject; violates separation of duties and human accountability. |
| Debug logging exposes prompts or sensitive data | Reject; sanitize, classify, redact, and re-test. Critical audit evidence remains required without leaking sensitive content. |

# 7. Required Evidence Pack
| Evidence Category | Minimum Evidence |
| --- | --- |
| Registry Evidence | Artifact metadata, owner, version, lifecycle state, repository path, source hash, classification, review record, approval record. |
| Evaluation Evidence | Dataset manifest, test run, golden/adversarial results, thresholds, failures, waivers, model alias, prompt version, guardrail version, evaluation date. |
| Runtime Evidence | Trace_id, actor, agent_id, model alias, provider route through LiteLLM, prompt_ref, guardrail_ref, retrieval_pack_ref, policy decision, output classification, evidence_ref. |
| Security Evidence | Secrets scan, route eligibility, classification check, OPA/SBAC result, Harness action record, blocked-action tests, redaction and forbidden-field tests. |
| DevSecOps Evidence | PR/MR, CODEOWNERS review, CI/CD job links, architecture fitness checks, SAST/SCA/secrets scans where applicable, SBOM/provenance where applicable. |
| Change Evidence | Rollback route, deactivation plan, fallback path, promotion approval, CAB/ARB if triggered, post-promotion monitoring, improvement backlog. |

# 8. Review Queue Control Register
| Seq | File Name | Pack | Current Version | Recommended Version | Review Status | Priority | Dependency | Action Required | Next Step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 42 | 42-AIRA_AI_Governance_and_Runtime_Control_Standard_v1.1.docx | Pack 10 | v1.1 | v1.2 | Completed / Revised | P0 | Parent AI governance | Completed | Use as AI governance parent baseline. |
| 43 | 22A-AIRA_Prompt_Guardrail_Model_Alias_and_AI_Evaluation_Registry_v1.1_Aligned.docx | Pack 05 | v1.1 | v1.2 | Completed / Revised | P0 | Depends on 42 v1.2 | Completed | Adopt as AI runtime registry candidate. |
| 44 | 42D-AIRA_AI_Agent_Identity_Lifecycle_and_Credential_Hygiene_Standard_v1.2_JML_and_Recertification_Automation_Update_FINAL.docx | Pack 10 | v1.2 | v1.3 | Next for Review | P0 | Depends on 42 v1.2 and 22A v1.2 | Review and align agent identity, credential hygiene, registry binding, recertification, suspension, and kill-switch readiness. | Proceed next. |
| 45 | 42E-AIRA_AI_Agent_Runtime_Security_Control_Plane_Standard_v1.2_Runtime_Metrics_and_Agent_Assurance_Dashboard_Update.docx | Pack 10 | v1.2 | v1.3 | Pending | P0 | After 42D | Align runtime security control plane with identity, registry, telemetry, Harness, OPA/SBAC, and incident response. | Review after 42D. |
| 46 | 42F-AIRA_AI_Agent_Autonomy_Calibration_Identity_Trust_and_Behavioral_Integrity_Standard_v1.2_Autonomy_Risk_Tier_and_Delegation_Matrix_Update.docx | Pack 11 | v1.2 | v1.3 | Pending | P0 | After 42D/42E | Align autonomy tiers, trust scoring, delegation and human handoff. | Review after runtime control plane. |

# 9. Simplification Recommendations

1. Keep 22A as the operational registry standard and avoid duplicating the full AI agent lifecycle that belongs in 42D through 42S.

2. Publish a concise registry template pack for developers: prompt template, guardrail profile, model alias, tool-action policy, evaluation manifest, and evidence manifest.

3. Make CI/CD checks read the machine-readable registry so enforcement is automated and not dependent on manual document review.

4. Use dashboards to show active aliases, expired evaluations, stale prompts, suspended guardrails, unapproved tool policies, and evidence completeness.

5. Maintain a single current registry manifest and generate Obsidian/LLM Wiki views as derivative projections.

# 10. AVCI Compliance Summary
| AVCI Property | Evidence in This Standard |
| --- | --- |
| Attributable | Every registry artifact has owner, version, source reference, repository path, reviewer, approver, route owner, and evidence reference. |
| Verifiable | Registry artifacts require tests, evaluations, CI/CD checks, policy results, telemetry, audit records, and evidence packs. |
| Classifiable | Prompts, guardrails, aliases, tool policies, datasets, outputs, logs, and evidence carry classification ceilings and handling rules. |
| Improvable | Findings, incidents, drift, failed evaluations, model changes, and user feedback become candidate improvements with tests, review, and controlled promotion. |

