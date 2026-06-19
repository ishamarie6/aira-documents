---
title: "AI Evaluation Red Team Guardrail and Model Route Certification Standard"
doc_id: "AIRA-70"
version: "v1.0"
status: "final"
category: "AI evaluation and red team"
source_docx: "AIRA_70_AI_Evaluation_Red_Team_Guardrail_and_Model_Route_Certification_Standard_v1.0.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 70-ai-evaluation-red-team
  - final
  - aira-70
---



# AI Evaluation Red Team Guardrail and Model Route Certification Standard



AIRA
AI-Native Enterprise Platform

AI Evaluation, Red-Team, Guardrail, and Model Route Certification Standard

AIRA-DOC-070 | Version v1.0

Evaluation Harness | AI Red Team | Guardrails | Model Route Registry | Tool-Action Certification | Evidence by Construction
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-070 |
| Document Title | AIRA AI Evaluation, Red-Team, Guardrail, and Model Route Certification Standard |
| Version | v1.0 - Initial Enterprise AI Evaluation and Model Route Certification Standard |
| Status | Draft for Architecture Review Board, CAB, Security Governance, AI Governance, DevSecOps, SRE, Product Owner, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | AI Governance; Security Architecture; DevSecOps Lead; Software Development Lead; QA/SDET; SRE; Platform Engineering; Data Governance; Internal Audit |
| Primary Audience | AI Engineers; System Builder operators; Developers; Security; DevSecOps; QA/SDET; SRE; Product Owners; Internal Audit |
| Primary Parents | 01A, 01, 01B, 02, 03, 04, 11/11A, 20, 42-series, 43/43A, 58, 65, 66, 68, 69 |
| Companion Sources | 10-10E MicroFunction family; 12A and Dynamic Workspace standards; 15/15A API; 17/17A Security; 31/31A Observability; 63 PRR/ORR; 64 Resilience Lab; 67 API/Event/Replay Runbook |
| External Alignment Reference | NIST AI RMF 1.0; NIST AI 600-1 Generative AI Profile; OWASP Top 10 for LLM Applications 2025; OWASP Top 10 for Agentic Applications 2026; MITRE ATLAS; NIST SSDF |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / AI-Evaluation-Route-Certification / 70 / v1.0 / |

# Mandatory Practice Statement

No AIRA AI model route, prompt template, RAG flow, AI Assistant Panel behavior, tool action, agent skill, System Builder output path, or automated recommendation is production-eligible merely because it responds well in a demo. It is eligible only when its intended use, classification, model route, prompts, retrieval sources, guardrails, tool permissions, evaluations, red-team results, evidence pack, owner approval, runtime monitoring, rollback or suspension path, and improvement backlog are complete and AVCI-compliant.

# Static Table of Contents

1. Executive Summary and Industry Leadership Position

2. Purpose, Scope, and Authority

3. AI Evaluation Governance Principles

4. Model Route Certification Lifecycle

5. Model Route Risk Tiers and Certification Classes

6. Evaluation Taxonomy and Minimum Test Suites

7. Red-Team, Abuse Case, and Guardrail Validation

8. RAG, Tool-Action, Agent, and Dynamic Workspace Certification

9. Evidence Pack, CI/CD, and Runtime Monitoring Requirements

10. RACI, Acceptance Criteria, Rejection Rules, and AVCI Summary

# 1. Executive Summary and Industry Leadership Position

AIRA must treat AI evaluation and route certification as a governed engineering control, not a one-time prompt test. The purpose of this standard is to ensure that AI outputs, model routes, prompts, retrieval, guardrails, and tool actions are evaluated, monitored, reviewed, reversible, and evidence-producing before they influence protected workflows or enterprise decisions.

This document converts AI governance into executable certification gates. It binds model routes to use cases, classification, risk tiers, evaluation suites, red-team scenarios, guardrails, OPA/SBAC policy, evidence manifests, and runtime telemetry. AI remains advisory unless a certified route and governed action boundary explicitly allow higher-risk behavior.

# 2. Purpose, Scope, and Authority

## 2.1 Purpose

Define the certification standard for AIRA model routes, prompts, RAG flows, AI Assistant Panel behavior, agent skills, tool actions, and System Builder AI-generated outputs.

Require evaluation, red-team, guardrail, policy, evidence, and human-approval gates before production or production-like use.

Prevent direct model-provider calls, uncontrolled agentic behavior, prompt leakage, excessive agency, unbounded consumption, unsafe retrieval, and evidence-free AI recommendations.

Create a repeatable model-route certification process for advisory, drafting, evidence summarization, RAG, tool-advisory, tool-action, and high-risk AI workflows.

## 2.2 Scope
| Scope Area | Included Controls |
| --- | --- |
| Model routes | LiteLLM/private gateway routes, model aliases, fallback routes, cost/latency profiles, classification eligibility, and route suspension. |
| Prompts and responses | System prompts, user prompts, response templates, output schemas, citations, redaction, hallucination/confabulation controls, and retention. |
| RAG and retrieval | Source eligibility, retrieval filters, vector/keyword source controls, citation checks, stale-source detection, and evidence binding. |
| Agents and tool actions | Agent registry, SBAC skills, OPA inputs, tool scopes, approval boundaries, Harness-mediated execution, and rollback. |
| Dynamic Workspace and System Builder | AI Assistant Panel, generated artifacts, candidate changes, AI-assisted analysis, and proposal-only improvement loops. |
| Evidence and monitoring | Evaluation reports, red-team findings, guardrail results, policy decisions, audit logs, trace IDs, evidence manifests, and runtime drift monitoring. |

## 2.3 Authority and Precedence
| Level | Authority | Meaning for AIRA-DOC-070 |
| --- | --- | --- |
| L0 | ARB / CAB / Security Governance / AI Governance / IT Head | Final authority for production-impacting AI route certification, exceptions, high-risk tool actions, and route suspension. |
| L1 | 01A, 01, 01B, 02, 11/11A | Universal architecture, AVCI, evidence, delivery discipline, and promotion gates. |
| L2 | 42-series, 43/43A, 58, 65, this 70 | AI governance, continuous improvement, multimodal assistant, prompts/artifacts, policy-as-code, and certification controls. |
| L3 | 20, 66, 68, 69, 63, 64, 67 | CI/CD evidence, manifest schema, traceability matrix, secure design review, readiness, resilience, and API/event controls. |
| L4 | Model route registry, prompt registry, guardrail registry, eval reports, evidence packs | Operational proof; may tighten but must not weaken governing standards. |

# 3. AI Evaluation Governance Principles
| ID | Principle | Mandatory Meaning |
| --- | --- | --- |
| AI-EVAL-01 | AI is not authority | AI may recommend, summarize, draft, analyze, classify, and propose; humans and policy gates retain authority. |
| AI-EVAL-02 | Certified route only | Every production AI use must bind to an approved model route, use case, classification ceiling, guardrail set, and evidence profile. |
| AI-EVAL-03 | Evaluation before activation | Routes, prompts, tools, and RAG flows require deterministic, adversarial, safety, security, privacy, and regression evaluation before activation. |
| AI-EVAL-04 | Guardrails in layers | Controls apply at input, retrieval, tool/action, model route, output, evidence, and runtime-monitoring layers. |
| AI-EVAL-05 | Least privilege and SBAC | Agents and tools receive only the skills, scopes, data, environments, and actions explicitly approved. |
| AI-EVAL-06 | Fail closed | Missing policy, guardrail, identity, classification, audit, evidence, or route-certification dependency blocks protected AI behavior. |
| AI-EVAL-07 | Evidence by construction | Eval runs, red-team findings, guardrail decisions, model route metadata, and approvals are captured in the evidence manifest. |
| AI-EVAL-08 | Continuous recertification | Routes are re-evaluated after model, prompt, data, tool, policy, risk, incident, or environment changes. |

# 4. Model Route Certification Lifecycle
| Stage | Required Action | Minimum Evidence |
| --- | --- | --- |
| 1. Route request | Declare use case, owner, audience, data classification, output authority, and route purpose. | Route request, owner, classification, affected workflow, risk tier. |
| 2. Risk classification | Classify route as advisory, drafting, RAG, evidence summarization, tool-advisory, tool-action, or high-risk. | Risk-tier decision, OPA/SBAC profile, approval trigger. |
| 3. Evaluation plan | Select functional, safety, security, privacy, RAG, tool, latency, cost, and resilience test suites. | Eval plan, test corpus hash, evaluator thresholds. |
| 4. Red-team execution | Run prompt injection, jailbreak, data leakage, retrieval poisoning, excessive agency, and tool misuse scenarios. | Red-team report, findings, severity, remediation. |
| 5. Guardrail validation | Validate input, retrieval, tool/action, output, retention, and evidence guardrails. | Guardrail report, policy decisions, failed-case handling. |
| 6. Certification decision | Approve, approve with restrictions, defer, suspend, or reject route. | Maker/checker approval, evidence pack, route registry update. |
| 7. Runtime monitoring | Monitor quality, denials, errors, latency, cost, safety events, drift, incidents, and feedback. | Telemetry, audit, dashboards, route-health report. |
| 8. Recertification | Re-run certification after material model, prompt, tool, data, policy, or incident change. | Delta eval, change record, updated approval. |

# 5. Model Route Risk Tiers and Certification Classes
| Class | Permitted Use | Certification Requirement |
| --- | --- | --- |
| C0 - Sandbox | Developer experimentation with synthetic/non-sensitive data only. | No production use; local/sandbox evidence and clear non-authority label. |
| C1 - Advisory | Summaries, explanations, draft suggestions, and low-risk productivity help. | Basic eval, safety checks, source disclaimers, no protected action. |
| C2 - Evidence Summarization | Summarize logs, traces, evidence packs, scans, PR/MR data, and incidents. | Classification filter, citation/source requirement, redaction, hallucination checks. |
| C3 - RAG Knowledge Assistant | Retrieval from approved knowledge sources with citations and source authority handling. | Retrieval eligibility, stale-source detection, citation verification, data-boundary tests. |
| C4 - Tool-Advisory | AI recommends tool action but does not execute protected action. | OPA/SBAC route, tool-scope review, abuse tests, human approval requirement. |
| C5 - Tool-Action Controlled | Harness-mediated low/medium-risk action in approved environment. | Full red-team, OPA/SBAC, audit, idempotency, rollback, monitoring, named approval. |
| C6 - High-Risk / Restricted | Security, data, production, financial, legal, policy, or destructive potential. | ARB/CAB/Security/AI Governance approval, enhanced testing, human-in-the-loop, mandatory fallback/suspend. |

# 6. Evaluation Taxonomy and Minimum Test Suites
| Evaluation Domain | Minimum Tests | Blocking Failure Example |
| --- | --- | --- |
| Functional correctness | Golden prompts, expected behavior, output schema, deterministic regression, role-specific acceptance. | Wrong workflow instruction, invalid schema, incorrect recommendation with high confidence. |
| Grounding and citation | Source retrieval, citation validity, stale-source detection, unsupported-claim detection. | Answer cites wrong source or produces unsupported operational instruction. |
| Safety and refusal | Unsafe content, policy-denied requests, protected action denial, escalation routing. | Route provides unsafe bypass or approves action it cannot authorize. |
| Security red-team | Prompt injection, jailbreak, indirect injection, tool misuse, data exfiltration, model-route bypass. | Prompt causes disclosure, guardrail bypass, or unauthorized tool request. |
| Privacy and classification | PII, secrets, prompt retention, retrieval eligibility, redaction, restricted evidence handling. | Restricted payload appears in output, log, evidence summary, or prompt store. |
| RAG integrity | Poisoned document, conflicting sources, stale canonical source, source-pack conflict, retrieval leakage. | Model treats non-authoritative source as active baseline. |
| Tool and agent behavior | Least privilege, SBAC skill, OPA decision, idempotency, dry-run, human approval, rollback. | Agent executes, escalates, or mutates without approved mediated path. |
| Operational performance | Latency, cost, timeout, fallback, unbounded consumption, route degradation, saturation. | Runaway model calls, excessive cost, timeout cascade, no safe fallback. |
| Observability and evidence | Trace, audit, model route ID, prompt/template ID, guardrail decision, evidence_ref. | No reconstruction path for AI decision or tool recommendation. |

# 7. Red-Team, Abuse Case, and Guardrail Validation
| Risk Pattern | Required Test / Control |
| --- | --- |
| Prompt injection and jailbreak | Direct, indirect, multilingual, context-stuffed, and tool-targeted injections must be tested. Guardrails must deny or safely degrade. |
| Sensitive information disclosure | Tests must verify that secrets, tokens, raw PII, Restricted evidence, raw prompts, source fragments, and credentials are not exposed. |
| Supply-chain and model/component risk | Model route, libraries, tools, connectors, embeddings, prompt packages, and retrieval sources must be recorded and reviewed. |
| Data/model poisoning | RAG sources, embeddings, uploaded files, and generated knowledge candidates must be classification-filtered, scanned, and source-authority checked. |
| Improper output handling | AI output must be treated as untrusted unless validated by schema, policy, human review, and target-context safety checks. |
| Excessive agency | Tool permissions, action scopes, environment boundaries, and approval requirements must prevent over-privileged or autonomous execution. |
| Unbounded consumption | Rate limits, budgets, quotas, timeout, token limits, retry limits, and circuit breakers must be enforced and observable. |

# 8. RAG, Tool-Action, Agent, and Dynamic Workspace Certification

## 8.1 RAG Certification Requirements

Every retrieval route must declare approved sources, source authority tier, freshness rule, classification ceiling, owner, and citation requirement.

Retrieval must reject stale, superseded, unauthorized, duplicate, poisoned, unclassified, or source-conflicting content unless a reconciliation item is created.

RAG outputs must distinguish source fact, model inference, uncertainty, and recommendation. Unsupported claims must be blocked or flagged.

## 8.2 Tool-Action and Agent Certification Requirements
| Control | Mandatory Treatment |
| --- | --- |
| Tool scope | Tool manifest must define permitted action, environment, data class, rate limit, human approval, rollback, and evidence. |
| Harness mediation | Agents must not receive direct Git, CI/CD, Kubernetes, database, secrets, workflow, production, or model-provider credentials. |
| OPA/SBAC | Every protected tool action assembles policy input with actor, skill, tenant, action, resource, route, risk, environment, and evidence context. |
| Idempotency and rollback | Mutating tool actions require idempotency, dry-run where feasible, duplicate-safe behavior, rollback/safe-disable, and audit. |
| Suspension | Route or tool can be suspended on failed eval, guardrail failure, incident, drift, waiver expiry, or policy-dependency outage. |

## 8.3 Dynamic Workspace and AI Assistant Panel Requirements

Dynamic Workspace AI behavior must remain backend-governed, MicroFunction-backed, policy-filtered, classifiable, observable, and reversible. UI generation, prompt suggestion, multimodal input, artifact creation, and action recommendations must not bypass backend policy, API contracts, or MicroFunction governance.

# 9. Evidence Pack, CI/CD, and Runtime Monitoring Requirements
| Evidence Class | Required Fields / Artifacts |
| --- | --- |
| Model route evidence | route_id, model_alias, gateway, purpose, owner, version, classification ceiling, risk tier, lifecycle state, fallback route. |
| Prompt/guardrail evidence | prompt_template_id, prompt_version, guardrail_policy_id, input/output filters, policy decisions, failed-case handling. |
| Evaluation evidence | eval_plan_id, test_corpus_hash, evaluator version, thresholds, pass/fail results, false-positive/negative notes, reviewer. |
| Red-team evidence | scenario set, attack family, severity, finding, exploitability, mitigation, retest result, residual risk. |
| RAG evidence | source_refs, source authority, freshness, citation validity, retrieval filter, conflicting-source treatment. |
| Tool/agent evidence | agent_id, tool_id, SBAC skill, OPA decision, harness request, approval, idempotency key, rollback/safe-disable path. |
| Runtime evidence | trace_id, request_id, route_id, prompt_id, policy_decision_id, guardrail result, latency, cost, denial, error, evidence_ref. |
| Certification evidence | maker, checker, approver, certification decision, restrictions, expiry, recertification trigger, suspension criteria. |

## 9.1 CI/CD Gate Integration
| Gate | Blocking Condition |
| --- | --- |
| Route registry gate | Missing owner, risk tier, model route, classification ceiling, fallback, monitoring, or suspension path. |
| Prompt/guardrail gate | Prompt or guardrail change lacks version, tests, redaction, classification, or approval. |
| Evaluation gate | Required test suite not run, threshold missed, or critical red-team finding unresolved. |
| Policy gate | OPA/SBAC missing or fail-open path exists for protected AI route or tool action. |
| Evidence gate | Evidence manifest missing route, prompt, guardrail, eval, red-team, approval, runtime, or rollback fields. |
| PRR/ORR gate | Production route lacks monitoring dashboard, runbook, incident route, rollback/suspend path, or support owner. |

## 9.2 Machine-Readable Certification Record

{
  "route_id": "aira.route.advisory.rag.internal.v1",
  "owner": "AI Governance / Product Owner",
  "classification_ceiling": "INTERNAL CONFIDENTIAL",
  "certification_class": "C3-RAG-Knowledge-Assistant",
  "model_gateway": "LiteLLM-or-approved-private-gateway",
  "prompt_template_id": "prompt.ai_panel.answer.v1",
  "guardrail_policy_id": "guardrail.input.output.retrieval.v1",
  "opa_policy_ref": "policy/ai/model_route.rego",
  "eval_plan_id": "eval.rag.security.safety.v1",
  "red_team_report_ref": "evidence/03-redteam/report.md",
  "decision": "approved_with_restrictions",
  "expires_on": "YYYY-MM-DD",
  "suspension_triggers": ["critical finding", "route drift", "policy outage", "guardrail failure"]
}

# 10. RACI, Acceptance Criteria, Rejection Rules, and AVCI Summary

## 10.1 RACI
| Activity | AI Governance | Security | DevSecOps | Product/Owner | QA/SDET | SRE | Internal Audit |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Route certification baseline | A/R | C | C | C | C | C | I |
| Evaluation suite design | A/R | R | C | C | R | C | I |
| Red-team and abuse-case review | A | A/R | C | C | R | C | I |
| Guardrail/policy approval | A | A/R | R | C | C | C | I |
| Production route activation | A | A | R | A/R | C | R | I |
| Evidence assurance | C | C | R | C | C | C | A/R |

## 10.2 Acceptance Criteria

Every production or production-like AI route has a registered owner, route ID, classification ceiling, certification class, evaluation plan, guardrail policy, OPA/SBAC policy, evidence profile, and suspension path.

Required functional, grounding, safety, security, privacy, RAG, tool, latency, cost, and regression evaluations pass or have approved remediation and residual-risk decision.

Red-team findings are severity-rated, remediated, retested, and linked to evidence manifest records.

Tool-action and agentic routes are Harness-mediated, least-privilege, policy-controlled, auditable, idempotent where mutating, and human-approved where required.

Runtime monitoring captures model route, prompt version, guardrail result, policy decision, trace ID, latency, cost, denial/error rates, and evidence reference without leaking restricted data.

Recertification is triggered by model, prompt, retrieval corpus, guardrail, tool, policy, risk, incident, or environment change.

## 10.3 Anti-Patterns and Rejection Rules
| Anti-Pattern | Required Response |
| --- | --- |
| Direct model-provider SDK call from application, script, notebook, agent, or service | Reject. Route through LiteLLM or approved private gateway with guardrails and evidence. |
| AI tool action executes without SBAC/OPA/Harness/human approval where required | Block. Convert to mediated request with policy decision and evidence. |
| Prompt change promoted without regression and red-team checks | Reject PR/MR or route activation. |
| RAG answer treats stale or non-authoritative source as canonical | Block or flag. Create reconciliation item and cite source authority. |
| Guardrail failure hidden to improve user experience | Reject. Critical guardrail failures are evidence and improvement inputs. |
| AI-generated recommendation mutates production or authoritative knowledge silently | Block. Candidate PR/MR or backlog item only. |
| Evaluation uses real Restricted data without approval and redaction controls | Reject and handle as security/privacy incident if exposed. |

## 10.4 External Alignment
| External Reference | AIRA Use |
| --- | --- |
| NIST AI RMF 1.0 | Trustworthy AI risk management, governance, mapping, measurement, management, and lifecycle discipline. |
| NIST AI 600-1 Generative AI Profile | Generative AI-specific risk profile for testing, incidents, value chain, privacy, information security, and human-AI configuration. |
| OWASP Top 10 for LLM Applications 2025 | Security risk taxonomy for prompt injection, sensitive disclosure, supply chain, poisoning, output handling, excessive agency, and unbounded consumption. |
| OWASP Top 10 for Agentic Applications 2026 | Agentic AI risk taxonomy for autonomous action, tool use, planning, memory, and authorization boundaries. |
| MITRE ATLAS | Adversarial AI tactics, techniques, red-team scenario enrichment, and threat-informed testing. |
| NIST SSDF | Secure software development practices and evidence-backed engineering controls. |

## 10.5 Open Reconciliation Items
| ID | Issue | Treatment | Owner |
| --- | --- | --- | --- |
| RI-070-001 | Model route registry schema must be synchronized with AIRA-DOC-066 evidence manifest schema. | Add route_certification object to evidence schema backlog. | AI Governance / DevSecOps |
| RI-070-002 | 42-series AI governance documents may overlap with this certification standard. | Treat this document as implementation certification layer; reconcile through 00D register. | Architecture Board |
| RI-070-003 | Tool-specific eval harness choices may change. | Keep standard tool-neutral; pin actual tools in Golden Source and pipeline manifests. | AI Governance |
| RI-070-004 | Agentic AI guidance is evolving rapidly. | Require quarterly external reference review and recertification profile update. | Security Architecture |

## 10.6 AVCI Compliance Summary
| AVCI Property | How This Standard Satisfies It |
| --- | --- |
| Attributable | Defines route owner, prompt owner, guardrail owner, model gateway, route version, evaluator, checker, approver, source refs, and lifecycle state. |
| Verifiable | Requires eval suites, red-team findings, guardrail decisions, OPA/SBAC tests, runtime telemetry, evidence manifest, recertification triggers, and approvals. |
| Classifiable | Requires classification ceiling, retrieval eligibility, model-route eligibility, redaction, retention, evidence handling, and restricted-data protections. |
| Improvable | Findings, drift, incidents, failed evals, feedback, guardrail misses, and route-health metrics feed governed backlog, tests, prompts, policies, and recertification. |

# Final Rule

An AIRA AI capability that passes demonstration but fails evaluation, red-team, guardrail, policy, classification, evidence, monitoring, human-accountability, or rollback checks is not AIRA-ready. It remains a draft or candidate until the required controls are proven and reviewed.

