---
title: "Architecture Decision Record and Technical Decision Log Standard"
doc_id: "AIRA-14"
version: "v2.3"
status: "revised"
category: "Decision records"
source_docx: "AIRA_14_Architecture_Decision_Record_and_Technical_Decision_Log_Standard_v2_3_Review_and_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 14-decision-records
  - revised
  - aira-14
---



# Architecture Decision Record and Technical Decision Log Standard



AIRA
AI-Native Enterprise Platform

Architecture Decision Record and Technical Decision Log Standard

Decision Governance | ADR Discipline | TDL Traceability | Reconciliation | AVCI Evidence

Version v2.3 - Review and Revised Edition

Status: Draft for Architecture Review Board / CAB / Engineering Adoption

Classification: INTERNAL CONFIDENTIAL
Owner: Solutions Architecture Office / IT Head
Review Date: 2026-06-16

# 1. Document Control
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-014 |
| Document Title | AIRA Architecture Decision Record and Technical Decision Log Standard |
| Recommended Version | v2.3 - Review and Revised Edition |
| Status | Draft for ARB / CAB / Engineering Adoption |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; DevSecOps; Security Architecture; QA/SDET; Platform Engineering; Data Governance; AI Governance; Internal Audit |
| Source Document Reviewed | 14-AIRA_Architecture_Decision_Record_and_Technical_Decision_Log_Standard_v2.2_Aligned.docx |
| Supersedes | AIRA-DOC-014 v2.2 after approval |
| Primary Alignment Inputs | 01A v1.2, 01 AVCI v3.2, 01B v1.2, 02 v5.2, 03 v4.2, 04 v9.2, 05 v4.2, 06 v3.2, 10 v3.3, 10A v2.3, 10B v2.2, 10C v2.2, 10D v2.2, 10E v1.2, 11 v3.2, 11A v1.2, 13 v2.2, 15 v2.2, 15A v1.2, 16 v2.2, 16A v1.3, 16B v1.2, 17 v2.2, 17A v1.2, 18 v1.2, 19 v1.3, 20 v1.2, 21A v1.2, 25 v1.3, 26B v1.3 |
| Review Cadence | Quarterly; unscheduled on material architecture, technology, security, AI, System Builder, MicroFunction, data, API, workflow, DevSecOps, production, or governance change |
| Evidence Path | OpenKM / AIRA / Governance / Decision-Governance / ADR-TDL / v2.3 or approved evidence repository equivalent |

# 2. Table of Contents Placeholder

Insert an automatic Microsoft Word Table of Contents here before publication. Update all fields before final PDF or controlled release generation.

# 3. Executive Review Summary

This v2.3 revision strengthens AIRA decision governance so material architecture and technical decisions cannot remain hidden in chat messages, meeting notes, code comments, AI outputs, unmanaged documents, or individual memory. ADRs and TDLs become authoritative, versioned, reviewable, retrievable, supersedable, evidence-linked governance artifacts that connect requirements, System Builder outputs, MicroFunctions, APIs, databases, security, DevSecOps evidence, AI agent controls, Dynamic Workspace changes, operational incidents, and release decisions.

The reviewed v2.2 source is structurally sound and should be retained. The main improvement is to align it with the newly revised AIRA source baseline, especially AVCI v3.2, MicroFunction v3.3/v2.x, DevSecOps v3.2, CI/CD evidence v1.2, API/database/security standards, knowledge governance, and System Builder boundaries. The revised standard clarifies when to use an ADR versus a TDL, which triggers are mandatory, how decisions become retrieval-eligible, and how waivers, exceptions, supersedence, and reconciliation items are controlled.

# 4. Source and Context Alignment Findings
| Alignment Area | Required Treatment in v2.3 |
| --- | --- |
| AIRA Enterprise Architecture | ADR/TDL records must prove impact on EDP-01 to EDP-20, SOLID, Clean Architecture, DDD, ports/adapters, reversibility, testability, and fitness functions. |
| AVCI and Evidence | Each decision record must identify owner, source, rationale, classification, verification evidence, lifecycle state, and improvement path. |
| System Builder | System Builder may draft ADR/TDL candidates and impact assessments; it must not approve, promote, or make decisions as authority. |
| MicroFunction | MicroFunction additions, catalog changes, standard steps, runtime configuration, idempotency, outbox, DLQ, replay, resilience, and observability changes require decision traceability. |
| API and Integration | OpenAPI, AsyncAPI, Kafka, Avro, CloudEvents, schema evolution, consumer impact, and contract compatibility decisions require ADR or TDL coverage. |
| Database and Flyway | Schema ownership, RLS, migration strategy, Flyway exception, data retention, outbox, seed data, and replay decisions require ADR/TDL evidence. |
| Security and AI Governance | Keycloak, OPA/SBAC, Vault/OpenBao, LiteLLM routes, guardrails, agent autonomy, tool authorization, and model-context decisions require decision records. |
| Knowledge Governance | Only accepted, current, classified, non-superseded decisions are retrieval eligible; drafts, waivers, conflicts, and stale items require quarantine or clear status handling. |
| DevSecOps and Change | Decision records must link to PR/MR, CI/CD evidence packs, GitNexus impact, scans, SBOM/provenance, waivers, rollback, and post-change evidence. |

# 5. Review and Gap Analysis
| Finding Type | Assessment |
| --- | --- |
| Retain | The source correctly treats ADR/TDL as mandatory for material decisions and aligns decisions with SOLID, Clean Architecture, DDD, ports/adapters, testability, security, observability, reversibility, and AVCI. |
| Correct | Older source references must inherit the current revised baseline rather than v1.1/v3.1 references where newer reviewed outputs exist. |
| Strengthen | Decision triggers must explicitly include System Builder, AI agents, model routes, guardrails, tool actions, MicroFunction catalogs, APIs/events, Flyway, OPA/SBAC, Dynamic Workspace, and Auto-Heal/Learn/Improve changes. |
| Simplify | Use ADRs for material or enterprise-impacting choices; use TDLs for tactical implementation choices; use waivers only for time-bound exception approval. |
| Add | Add retrieval eligibility, conflict handling, decision-state transitions, evidence-pack fields, GitNexus impact reference, and decision-to-release traceability. |
| Remove / Prevent | Do not allow chat-only decisions, unowned AI-generated decisions, stale Obsidian decisions as authority, or implied approvals from diagrams, code, or working demos. |
| Automation | Add validation rules for missing decision records, stale decisions, superseded records, missing owners, missing rollback, missing evidence, and unresolved conflicts. |

# 6. Revised Full AIRA Standard

## 6.1 Purpose

The purpose of this standard is to define how AIRA captures, reviews, approves, indexes, supersedes, reconciles, and audits architecture decisions and technical decisions across the platform. It ensures that decisions affecting architecture, technology, security, data, integration, workflow, AI, DevSecOps, operations, MicroFunction runtime assembly, and System Builder outputs are governed, traceable, evidence-linked, and retrievable without becoming uncontrolled authority.

## 6.2 Scope

This standard applies to all AIRA human-authored and AI-assisted decisions that materially affect architecture boundaries, runtime behavior, data, security, policies, model routes, agent permissions, tool actions, workflows, API/event contracts, database migrations, DevSecOps pipelines, observability, release controls, operations, and knowledge governance.

Out of scope are informal brainstorming notes, non-material implementation preferences, and draft AI outputs that have not been reviewed. Such artifacts may become inputs, but they are not authoritative decisions until promoted through this standard.

## 6.3 Decision Governance Principles

No material AIRA decision may exist only in chat, email, meeting notes, screenshots, slide decks, code comments, prompt output, or individual memory.

Every decision must have a named owner, reviewer, source context, status, classification, rationale, consequence, evidence reference, and revision path.

AI may draft, compare, summarize, and recommend decisions, but AI is never the approver or authority for AIRA decisions.

Decision records must preserve or improve EDP-01 to EDP-20 and AVCI. A weakening decision requires explicit waiver, risk owner, expiry, compensating controls, and remediation plan.

Accepted decisions must be retrievable from governed knowledge systems but only when current, classified, non-superseded, and source-linked.

Decisions that affect production, security, Restricted data, identity, secrets, agent authority, database schema, release controls, or irreversible behavior require ARB, CAB, Security, Data Governance, or AI Governance review as applicable.

## 6.4 Decision Record Types
| Type | Name | When Used | Approval Path |
| --- | --- | --- | --- |
| ADR | Architecture Decision Record | Material architecture, platform, boundary, security, data, integration, workflow, AI, or enterprise design decision with durable consequence. | ARB / CAB / Specialist governance as applicable |
| TDL | Technical Decision Log | Tactical technical choice that affects implementation but does not independently change major architecture authority. | Technical lead plus required reviewer |
| Waiver | Controlled Exception | Time-bound permission to deviate from a standard, gate, tool baseline, or control. | Risk owner plus required governance owner |
| Reconciliation Item | Conflict / Source Alignment Record | Source conflict, duplicate numbering, superseded reference, stale decision, or contradiction requiring controlled resolution. | Solutions Architecture Office / register owner |
| Decision Index Entry | Decision Registry Metadata | Machine-readable metadata used for retrieval, CI validation, evidence, and audit. | Knowledge Governance / DevSecOps |

## 6.5 Mandatory ADR and TDL Triggers
| Trigger Category | Mandatory ADR/TDL Trigger |
| --- | --- |
| Architecture / Boundary | New bounded context, service split, package boundary change, cross-context data write, or ports/adapters exception. |
| MicroFunction | New standard step family, STP-BUS function, runtime assembly pattern, catalog field, publish-time validator, idempotency profile, outbox/DLQ/replay behavior, or resilience pattern. |
| API / Integration | OpenAPI/AsyncAPI change with consumer impact, Kafka topic or Avro/JSON schema evolution, CloudEvents envelope change, compatibility break, external integration, or event replay strategy. |
| Database / Flyway | Schema ownership, RLS/tenant isolation, Flyway exception, baseline strategy, data retention, migration rollback/forward-fix strategy, seed data authority, or production data repair pattern. |
| Security / Identity / Secrets | Keycloak/OIDC pattern, OPA/SBAC policy model, Vault/OpenBao secret lifecycle, service identity, break-glass, MFA/session/token rule, or secrets-handling exception. |
| AI / Agent / Model | LiteLLM route, guardrail change, prompt standard, memory/RAG eligibility, agent skill/tool scope, autonomy tier, agent registry data model, or direct model-route exception. |
| DevSecOps / Release | Pipeline gate, SAST/SCA/DAST rule, SBOM/provenance target, GitNexus role, artifact signing, deployment/promotion control, rollback/compensation strategy, or CI waiver. |
| Dynamic Workspace / UX | Backend-governed workspace policy, template lifecycle, component/action authority, personalized layout persistence, rendering strategy, or UI generation boundary. |
| Operations / Auto Improvement | Auto-Heal/Learn/Improve loop, incident remediation pattern, trace reconstruction method, diagnostic toggle rule, SLO/SLA threshold, or runbook authority. |
| Technology Deviation | Java 25/Spring Boot 4 baseline deviation, unsupported library, unapproved tool, unmanaged plugin, cloud/service adoption, or change to approved technology stack. |

## 6.6 Decision Lifecycle and Status Model
| Status | Meaning |
| --- | --- |
| Draft | Created by human or approved AI assistant; not authoritative. |
| Proposed | Submitted with owner, scope, classification, rationale, options, risk, and evidence needs. |
| Under Review | Reviewed by required technical, security, data, DevSecOps, AI governance, or business owners. |
| Accepted | Approved through the required path and eligible for implementation subject to PR/MR and CI evidence. |
| Implemented | Linked to PR/MR, CI/CD evidence, tests, scans, runtime evidence, release record, and monitoring. |
| Superseded | Replaced by a newer decision; must remain retrievable for history but not served as current authority. |
| Deprecated | Still historically valid but no longer recommended for new work. |
| Rejected | Evaluated and declined; useful as rationale but not authority. |
| Waived | Exception granted with expiry, risk owner, compensating controls, and remediation path. |
| Quarantined | Untrusted due to conflict, missing classification, stale source, broken traceability, or suspected unsafe content. |
| Retired | No longer active and retained only per retention/audit policy. |

## 6.7 ADR Required Structure

Decision ID, title, status, date, owner, reviewers, approver, classification, bounded context, affected systems, and source references.

Problem statement, context, constraints, options considered, decision, rationale, alternatives rejected, and consequences.

Impact assessment for EDP-01 to EDP-20, AVCI, security, privacy, data, API/event contracts, database/Flyway, observability, operations, reversibility, and evidence.

Implementation plan, PR/MR references, CI/CD evidence expectations, tests/scans, GitNexus impact, rollout plan, rollback/forward-fix/compensation path, and monitoring plan.

Supersedence, expiry if applicable, related ADR/TDL/waiver/reconciliation item, and knowledge/retrieval eligibility metadata.

## 6.8 TDL Required Structure

TDL ID, title, owner, reviewer, classification, component, source ticket, and affected repository path.

Technical choice, implementation rationale, constraints, affected tests, affected contracts, affected configurations, and impacted runtime behavior.

Risk level, security/data impact, rollback method, evidence required, and whether escalation to ADR is required.

Decision state, review result, implementation link, evidence pack reference, and supersedence reference.

## 6.9 ADR versus TDL Selection Rule
| Decision Form | Selection Rule |
| --- | --- |
| Use ADR | The decision changes architecture authority, platform direction, bounded context ownership, security posture, model/agent authority, database strategy, event strategy, production operations, or enterprise-wide standard. |
| Use TDL | The decision is implementation-specific, reversible, low-to-medium risk, bounded to one component, and does not establish enterprise precedent. |
| Escalate TDL to ADR | The TDL creates repeated pattern, exception, cross-context impact, security/data concern, agent/tool authority change, technology deviation, or production-impacting behavior. |
| Use Waiver | The team cannot meet a required standard or gate and needs time-bound, risk-owned exception approval. |
| Use Reconciliation Item | Documents, code, diagrams, prompts, source packs, or operational records conflict or create unclear authority. |

## 6.10 Repository, Obsidian, and LLM Wiki Structure

ADR and TDL source files must live in Git-managed repositories or approved document repositories. Obsidian may contain curated projections and summaries. LLM Wiki and retrieval indexes are derivative and must link back to Tier-0 source records. A decision projection is not authoritative unless its source record is accepted, current, classified, non-superseded, and traceable to evidence.

## 6.11 Retrieval Eligibility Rules
| Rule | Treatment |
| --- | --- |
| Eligible | Accepted or Implemented decisions with owner, classification, current status, source reference, and evidence link. |
| Restricted Eligibility | Confidential or Restricted decisions may be retrievable only through SBAC/OPA, classification-aware route, and approved model/retrieval policy. |
| Not Eligible as Current Authority | Draft, proposed, rejected, superseded, deprecated, waived, expired, conflicted, quarantined, or source-broken decisions. |
| Required Metadata | decision_id, status, version, owner, classification, source_ref, supersedes, superseded_by, evidence_ref, review_date, expiry, and retrieval_eligibility. |
| Conflict Handling | Conflicting records must produce a reconciliation item and must not be served as final authority until resolved. |

## 6.12 PR/MR, CI/CD, and Evidence Requirements

Any PR/MR that implements a material decision must reference the ADR or TDL ID. CI/CD validation should flag material changes without decision references, stale or superseded decision references, missing rollback strategy, missing classification, missing evidence pack, missing tests, direct model-provider calls, direct production mutation, direct SQL/DDL bypassing Flyway, or direct tool/agent authority outside Harness/SBAC/OPA.

Evidence must include source ticket, decision record, PR/MR, reviewer approval, tests, security scans, architecture fitness checks, policy results, GitNexus impact, SBOM/provenance where applicable, migration evidence where applicable, deployment evidence where applicable, rollback or compensation path, and post-change monitoring evidence.

## 6.13 System Builder and AI Agent Decision Governance

System Builder may classify intake, analyze impact, identify decision triggers, draft ADR/TDL candidates, create options, and assemble evidence packs.

System Builder must not approve decisions, waive controls, merge code, promote artifacts, mutate production, or become source of authority.

AI agents may assist with drafting, comparison, evidence summarization, and conflict detection only within registered skills, trust tier, classification ceiling, tool scope, and OPA/SBAC policy.

Agent-related decisions must capture purpose, owner, agent ID, skill scope, model route, tool permission, memory/RAG eligibility, guardrail policy, evaluation evidence, incident/kill-switch path, and retirement rule.

## 6.14 Waivers, Exceptions, and Non-Conformance

Waivers are controlled exceptions, not alternate standards. Every waiver must have a risk owner, impacted control, business/technical reason, classification, expiry, compensating controls, remediation plan, approvers, evidence reference, and review cadence. Expired waivers must fail closed until renewed or remediated. Repeated waivers trigger an ADR, TDL, risk review, or standard improvement item.

## 6.15 Auto-Heal, Auto-Learn, and Auto-Improve Decision Governance

Auto-Heal, Auto-Learn, and Auto-Improve loops may detect issues, retrieve evidence, propose decisions, generate candidate fixes, draft PRs, and recommend knowledge updates. They must not silently change architecture, code, configuration, data, policies, prompts, guardrails, model routes, agent permissions, or production environments. Any candidate that changes durable behavior must create or reference an ADR, TDL, waiver, or reconciliation item before implementation.

## 6.16 Anti-Patterns

Chat-only architecture decisions or AI-generated recommendations treated as approval.

Code, diagram, prompt, or running demo used as substitute for decision rationale.

Superseded ADRs served by LLM Wiki as current authority.

Waivers without expiry, risk owner, compensating controls, or remediation evidence.

Security, database, AI-agent, model-route, or production changes implemented without ADR/TDL reference.

Direct production mutation justified by an undocumented operational decision.

Conflicting source-pack references hidden rather than logged as reconciliation items.

## 6.17 Validation Checklist
| Checkpoint | Pass Condition |
| --- | --- |
| Owner and Approver | Named owner, reviewer, and approver are present. |
| Classification | Classification, handling rule, and retrieval eligibility are present. |
| Source and Context | Ticket, requirement, incident, evidence item, prompt, or source reference is linked. |
| Options and Rationale | Options considered, selected decision, rejected alternatives, and consequences are documented. |
| Architecture Impact | EDP-01 to EDP-20 and AVCI impact is assessed. |
| Security/Data Impact | Identity, secrets, OPA/SBAC, RLS, classification, retention, and privacy impact are assessed. |
| Implementation Evidence | PR/MR, tests, scans, GitNexus, CI/CD, SBOM/provenance, and runtime evidence are identified where applicable. |
| Reversibility | Rollback, forward-fix, compensation, disablement, rebuild, restore, or waiver path is clear. |
| Supersedence | Related, superseded, and superseding decisions are linked. |
| Knowledge Eligibility | Obsidian/LLM Wiki projection and retrieval status are controlled. |

## 6.18 Implementation Guidance

Create an ADR or TDL at intake when a material decision trigger is detected.

Use TDL for local, reversible implementation decisions; escalate to ADR when scope, risk, or precedent expands.

Attach decision IDs to backlog items, PR/MR templates, CI/CD evidence packs, release records, and knowledge projections.

Use CODEOWNERS and branch rules to require decision review by the correct authority.

Run automated checks for missing decision references and stale/superseded decision links.

Project accepted decisions into Obsidian and LLM Wiki only through the governed knowledge pipeline.

Review decisions quarterly and after major incidents, architecture changes, security findings, technology updates, or source-pack reconciliation.

## 6.19 Required Evidence
| AVCI Dimension | Decision Evidence Required |
| --- | --- |
| Attributable | Decision owner, reviewer, approver, source ticket, source documents, affected repositories, and AI assistance declaration. |
| Verifiable | Options, rationale, test plan, scan results, GitNexus impact, PR/MR link, CI/CD evidence pack, policy results, and runtime evidence. |
| Classifiable | Data classification, handling rules, model/retrieval eligibility, retention, redaction requirements, and access controls. |
| Improvable | Known limitations, review date, supersedence plan, improvement backlog reference, lessons learned, and standard update triggers. |

## 6.20 Change Log
| Version | Summary |
| --- | --- |
| v2.0 | Enterprise Design Principles and SOLID enforcement revision. |
| v2.2 | Supplemental alignment update for Java 25, GitNexus, Dograh, Flyway-from-Day-0, retrieval eligibility, and Pack 01-05 alignment. |
| v2.3 | Current review revision: aligned with revised AIRA v5.1 foundation, MicroFunction, DevSecOps, CI/CD, GitNexus, API, database/Flyway, security, Golden Source, Obsidian/LLM Wiki, System Builder, AI agent governance, waiver, reconciliation, and retrieval controls. |

# 7. Simplification Recommendations

To keep this document practical for developers and AI assistants, maintain three operating forms: ADR for material decisions, TDL for tactical technical choices, and Waiver for controlled exceptions. All three should use short, repeatable templates with mandatory metadata. Longer rationale should be permitted only where risk, security, data, AI, or production impact justifies it.

Keep ADRs concise but complete: decision, context, options, rationale, consequences, evidence, and reversibility.

Use TDLs as lightweight records that can be escalated into ADRs when impact expands.

Compile decision metadata into a machine-readable register for CI/CD, LLM Wiki, Obsidian, and System Builder validation.

Use pre-approved trigger rules so developers know when a decision record is mandatory.

# 8. Automation Recommendations
| Automation Area | Recommended Control |
| --- | --- |
| Decision Inventory | Maintain a machine-readable ADR/TDL register with ID, status, owner, classification, source, and supersedence fields. |
| Cross-Reference Validation | CI checks verify that PRs changing governed paths reference valid ADR/TDL/waiver records. |
| Version Tracking | Automated checks flag references to superseded or deprecated decisions. |
| Duplicate Detection | Knowledge pipeline flags duplicate titles, duplicate decision IDs, and conflicting source-pack entries. |
| Terminology Consistency | Lint decision records for approved AIRA terms: AVCI, MicroFunction, System Builder, OPA/SBAC, GitNexus, Flyway, LiteLLM, and Golden Source. |
| Conflict Detection | Quarantine conflicting decisions and create reconciliation items before retrieval eligibility. |
| Missing Section Detection | Validate required ADR/TDL fields before acceptance. |
| Evidence Checklist Validation | Block acceptance when evidence, rollback, classification, or reviewer fields are missing. |
| Agent-Assisted Review Queue | Use approved AI to triage stale, conflicted, missing, or weak decision records; human reviewers remain accountable. |
| Obsidian / Git Tracking | Project accepted decisions to Obsidian and LLM Wiki with source link, hash, status, and freshness metadata. |

# 9. Review Queue Control Register

This register continues the running AIRA review queue. The current document is now marked completed, and the next recommended review item is the change, promotion, reversibility, and compensation control standard.
| Seq | File Name | Pack | Current | Recommended | Status | Priority | Dependency | Action Required | Next Step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 31 | 21A-AIRA_Governed_Knowledge_Control_Plane_Obsidian_Codex_GitHub_Standard_v1.1_Aligned.docx | Pack 05 | v1.1 | v1.2 | Completed | P1 | 05/06/18/25/26B | Completed revised control plane. | Retain v1.2 candidate |
| 32 | 25-AIRA_Knowledge_Access_Architecture_and_Golden_Source_Standard_v1.2_Aligned.docx | Pack 06 | v1.2 | v1.3 | Completed | P1 | 21A/18/05/06 | Completed Golden Source revision. | Retain v1.3 candidate |
| 33 | 26B-AIRA_Governed_Knowledge_Automation_Pipeline_Standard_v1.2_Aligned.docx | Pack 07 | v1.2 | v1.3 | Completed | P1 | 25/21A/13 | Completed knowledge automation revision. | Retain v1.3 candidate |
| 34 | 13-AIRA_Obsidian_and_LLM_Wiki_Knowledge_Governance_Standard_v2.1_Aligned.docx | Pack 03 | v2.1 | v2.2 | Completed | P1 | 26B/25/21A | Completed Obsidian/LLM Wiki revision. | Retain v2.2 candidate |
| 35 | 14-AIRA_Architecture_Decision_Record_and_Technical_Decision_Log_Standard_v2.2_Aligned.docx | Pack 03 | v2.2 | v2.3 | Completed | P0 | 13/26B/25/21A/11/15/16/17 | Review, correct, align, simplify, and improve decision governance. | Deliver v2.3 candidate |
| 36 | 30A-AIRA_Change_Promotion_Reversibility_and_Compensation_Control_Standard_v1.1.docx | Pack 07 | v1.1 | v1.2 | Next for Review | P0 | 14/11/20/17/16/15/10 | Align promotion, reversibility, compensation, maker-checker, System Builder, and CAB/ARB controls. | Review next |

# 10. Next Recommended Document

The next recommended document is 30A-AIRA_Change_Promotion_Reversibility_and_Compensation_Control_Standard_v1.1.docx. It should be reviewed next because ADR/TDL records define and approve decisions, while 30A governs how those decisions are promoted, reversed, compensated, disabled, rolled back, or escalated through maker-checker, ARB, CAB, and System Builder promotion controls. Reviewing 30A next prevents a gap between decision authority and production-bound change control.

Recommended next version: v1.2.

