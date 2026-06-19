---
title: "Obsidian and LLM Wiki Knowledge Governance Standard"
doc_id: "AIRA-13"
version: "v2.2"
status: "revised"
category: "Knowledge governance"
source_docx: "AIRA_13_Obsidian_and_LLM_Wiki_Knowledge_Governance_Standard_v2_2_Review_and_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 13-knowledge-governance
  - revised
  - aira-13
---



# Obsidian and LLM Wiki Knowledge Governance Standard



AIRA

AI-Native Enterprise Platform

Obsidian and LLM Wiki Knowledge Governance Standard

Curated Knowledge | Source Projection | Retrieval Governance | Classification-Aware AI Assistance | AVCI Always
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-013 |
| Recommended Version | v2.2 |
| Status | Draft for Architecture, Security, DevSecOps, Knowledge Governance, AI Governance, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; DevSecOps; Security Architecture; Data Governance; Knowledge Governance; AI Engineering; QA/SDET; SRE; Internal Audit |
| Source Document Reviewed | 13-AIRA_Obsidian_and_LLM_Wiki_Knowledge_Governance_Standard_v2.1_Aligned.docx |
| Supersedes | 13-AIRA_Obsidian_and_LLM_Wiki_Knowledge_Governance_Standard_v2.1_Aligned.docx after approval |
| Review Date | 2026-06-16 |
| Evidence Path | OpenKM Tier-0 / AIRA / Knowledge-Governance / Obsidian-LLM-Wiki / v2.2 / |

Mandatory Operating Principle

Obsidian and LLM Wiki are governed knowledge systems, not unmanaged file dumps. They may accelerate AIRA engineering and AI assistance only when source authority, classification, provenance, freshness, citations, SBAC/OPA authorization, human review, security, observability, reversibility, and AVCI evidence remain intact.

# 1. Document Control
| Property | Value |
| --- | --- |
| Document Title | AIRA Obsidian and LLM Wiki Knowledge Governance Standard |
| Document ID | AIRA-DOC-013 |
| Version | v2.2 - Golden Source, Retrieval Eligibility, and AI Governance Alignment Update |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Review |
| Owner | Solutions Architecture Office / IT Head |
| Primary Audience | Solutions Architects, Developers, DevSecOps, Security, DBA, QA/SDET, Knowledge Stewards, AI Engineers, Internal Audit |
| Related Documents | 01, 01A, 01B, 02, 03, 05, 06, 10 through 10E, 11, 11A, 13, 14, 15, 16, 17, 18, 19, 20, 21A, 25, 26B, 42I |
| Change Summary | Aligned v2.1 with revised AIRA knowledge, repository, MicroFunction, DevSecOps, security, GitNexus, and Golden Source governance; strengthened retrieval eligibility, metadata, quarantine, freshness, conflict handling, and AI assistant access controls. |

# 2. Table of Contents Placeholder

Before final publication in Microsoft Word, insert an automatic Table of Contents using References > Table of Contents, then update all fields. This placeholder is intentionally retained for deterministic rendering during review.

# 3. Executive Review Summary

The v2.1 source is directionally correct and should be retained. It already establishes that Obsidian and LLM Wiki are governed knowledge systems, not unmanaged file dumps, and that source authority, classification-aware retrieval, citations, review state, and Golden Source linkage must be preserved. This v2.2 revision strengthens the implementation-ready controls needed after the updates to the Golden Source, repository bootstrap, knowledge automation, DevSecOps, MicroFunction, API, database, security, GitNexus, and CI/CD evidence documents.

Retain: source-tier hierarchy, approval-aware retrieval, no secrets or real PII, no full-codebase copy into Obsidian, human review gates, and citation-by-default requirements.

Correct: make Tier-0 authority explicit, clarify when Obsidian is authoritative versus derivative, and state that LLM Wiki, embeddings, graph edges, and caches are derivative only.

Strengthen: retrieval eligibility, freshness manifest, conflict detection, quarantine, redaction, source hash, reviewer state, model-route eligibility, and audit evidence.

Add: System Builder, AI agent, Auto-Learn, GitNexus, AGENTS.md, CLAUDE.md, Codex, and evidence-pack integration rules.

Simplify: provide developers and knowledge stewards with one daily operating model and one minimum metadata checklist.

# 4. Alignment Findings
| Aligned Source | Required Impact on 13 v2.2 |
| --- | --- |
| 05 Information Nervous System v4.2 | Provides source tiers, reasoning axes, provenance, freshness, retrieval eligibility, and derivative-index governance. |
| 06 CLAUDE.md Reference v3.2 | Provides repository-local AI behavior rules and the source for generated AGENTS.md or tool-specific adapters. |
| 18 Repository Bootstrap v1.2 | Defines Git, branch protection, CODEOWNERS, devcontainers, evidence folders, and Golden Source repository layout. |
| 19 GitNexus v1.3 | Defines GitNexus as read-only, derivative, commit-bound code intelligence and impact evidence. |
| 21A Knowledge Control Plane v1.2 | Defines operational connection across Obsidian, Codex, GitHub, LLM Wiki, and governed retrieval. |
| 25 Knowledge Access and Golden Source v1.3 | Defines the Golden Source rule across Git, GitNexus, Obsidian, LLM Wiki/LightRAG, and AI assistants. |
| 26B Knowledge Automation Pipeline v1.3 | Defines automated detection, validation, summary generation, indexing, freshness manifests, and human approval gates. |
| 42I Agent Memory and RAG Integrity | Extends knowledge governance into agent memory, RAG integrity, poisoning defense, quarantine, and retrieval auditability. |

# 5. Gap Analysis and Review Verdict
| Finding Area | Assessment |
| --- | --- |
| Already correct | The v2.1 baseline correctly positions Obsidian and LLM Wiki as governed knowledge systems; defines source tiers; requires citations, classification, review gates, and staleness controls; and rejects secrets, real PII, and uncontrolled drafts. |
| Outdated or weak | The prior version does not fully reflect the later Golden Source, repository bootstrap, GitNexus, System Builder, AI agent memory, and knowledge automation decisions. |
| Missing | Minimum metadata contract, retrieval eligibility decision model, quarantine triggers, conflict-severity model, agent/AI access evidence, and operational runbook for ingestion-to-indexing. |
| Simplification need | Developers need a clear rule: create source in Git/OpenKM/approved docs, project curated content to Obsidian, index only eligible content into LLM Wiki, and require citations and evidence for AI output. |
| Governance strengthening | Must add maker-checker publication, CODEOWNERS, PR/MR evidence, classification scan, secret scan, freshness manifest, source hash, model route eligibility, and audit records. |
| Automation strengthening | Automated validation may propose projection, indexing, quarantine, or re-indexing, but cannot approve, supersede, publish canonical standards, or silently modify knowledge authority. |

# 6. Revised Full AIRA Standard

## 6.1 Purpose

This standard defines how AIRA governs Obsidian, LLM Wiki, LightRAG, retrieval indexes, Markdown projections, approved documents, knowledge summaries, prompts, guardrails, AI assistant context, and knowledge evidence. Its purpose is to make AIRA knowledge useful for humans and AI while preventing duplicate Golden Sources, stale context, unreviewed authority, sensitive data leakage, prompt or retrieval poisoning, and architecture drift.

## 6.2 Scope

This standard applies to approved AIRA documents, Obsidian vaults, LLM Wiki artifacts, LightRAG or vector indexes, Git-backed documentation repositories, AI assistant knowledge connectors, GitNexus-derived summaries, evidence summaries, prompt and guardrail references, ADR/TDL projections, runbooks, lessons learned, and Auto-Learn candidates. It excludes raw production data, uncontrolled chat logs, secrets, credentials, unrestricted customer data, and unofficial personal knowledge stores.

## 6.3 Authority and Precedence

Tier-0 approved sources govern. Obsidian may be authoritative only as a controlled projection or approved note with owner, version, source link, classification, review state, and evidence. LLM Wiki, LightRAG, embeddings, graph edges, caches, and AI outputs are derivative and must never override Tier-0 sources.

## 6.4 Knowledge Source Authority Model
| Tier | Source / Artifact | Authority Rule |
| --- | --- | --- |
| Tier 0 | Approved DOCX/PDF, OpenKM/DMS, Git repositories, ADR/TDL, database records, workflow histories, audit records, evidence stores | Authoritative source of record |
| Tier 1 | Git-managed Obsidian Markdown projection or approved operational note | Authoritative for day-to-day use only when linked to Tier 0 and current |
| Tier 2 | LLM Wiki curated artifact or approved knowledge summary | AI retrieval layer; derivative but usable when eligible and cited |
| Tier 3 | pgvector, LightRAG, search index, graph edge, Redis/Valkey cache | Derivative acceleration only; never source of truth |
| Tier 4 | AI output, draft, chat summary, Auto-Learn candidate, System Builder recommendation | Not authoritative until reviewed and promoted |

## 6.5 Mandatory Knowledge Governance Principles
| ID | Principle |
| --- | --- |
| KG-01 AVCI for Knowledge | Every note, artifact, prompt, guardrail, diagram, runbook, and wiki item must have owner, source, version, classification, verification evidence, and improvement path. |
| KG-02 Approved Sources First | Default retrieval uses approved and current artifacts only. Draft or candidate retrieval requires explicit query intent and authorization. |
| KG-03 Raw Source Authority | Approved source documents, Git repositories, OpenKM records, databases, and audit stores remain authoritative. Summaries and embeddings are derivative. |
| KG-04 Classification Governs Retrieval | Classification and SBAC/OPA determine who or what can retrieve content and which model route may process it. |
| KG-05 Citations by Default | AI responses must identify document ID, title, version, section, source path, and evidence reference where available. |
| KG-06 Staleness Is a Defect | Superseded, expired, unclassified, duplicate-conflict, or stale artifacts must be quarantined from default retrieval. |
| KG-07 Human Review Gates Promotion | AI-generated summaries, Auto-Learn candidates, lessons learned, and System Builder outputs do not become knowledge authority without named human review. |
| KG-08 No Secrets or Raw PII | Secrets, credentials, raw customer PII, raw production logs, unrestricted source payloads, private keys, tokens, and restricted data must not be stored or indexed unless an approved controlled evidence path exists. |
| KG-09 Conflicts Are Surfaced | Conflicting guidance must be reported with source/version context and routed to AVCI reconciliation rather than hidden by the retrieval layer. |
| KG-10 Design Principles Are Preserved | Knowledge artifacts and retrieval answers must preserve SOLID, Clean Architecture, DDD boundaries, ports/adapters, security, observability, testability, reversibility, and AVCI. |

## 6.6 Minimum Metadata and Front Matter Standard

Every Obsidian note, LLM Wiki artifact, prompt, guardrail, runbook, diagram, code-intelligence summary, evidence summary, and curated AI retrieval artifact must include the minimum metadata below before it becomes default retrievable.
| Metadata Group | Required Fields |
| --- | --- |
| Identity | document_id, title, canonical_filename, artifact_type, version, status, owner, co_owner |
| Authority | source_tier, source_system, source_path, source_hash, source_version, supersedes, superseded_by |
| Governance | classification, handling_rule, approval_status, approved_by, approval_date, review_date, expiry_date |
| Retrieval | retrieval_eligible, model_route_eligibility, sbac_skill_required, opa_policy_ref, freshness_status |
| Architecture | bounded_context, related_standard, related_adr, related_repository, related_module, principle_impact |
| Evidence | evidence_ref, index_batch_id, validation_result, conflict_status, quarantine_status, improvement_backlog_ref |

## 6.7 Vault and Repository Structure

00_Registers - document inventory, canonical register, review queue, source map, freshness manifest, and conflict register.

01_Approved_Standards - approved AIRA standards and controlled projections.

02_Architecture_and_ADR - ADRs, TDLs, blueprint decisions, diagrams, and architecture review notes.

03_Engineering_and_MicroFunction - MicroFunction, DevSecOps, API, database, security, and testing guidance.

04_Runbooks_and_Operations - SRE, incident, backup, restore, release, and support runbooks.

05_Evidence_Summaries - curated CI/CD, scan, test, GitNexus, deployment, and operational evidence summaries.

06_AI_Governance_and_Agents - approved prompts, guardrails, model route summaries, agent definitions, and evaluation results.

90_Candidates - drafts, AI proposals, unapproved Auto-Learn items, and System Builder outputs pending review.

95_Quarantine - stale, conflicted, unclassified, unsafe, supersedence-unclear, or failed-validation artifacts.

99_Superseded - retained historical documents with explicit supersession links and retrieval exclusion by default.

## 6.8 Ingestion, Projection, and Publication Workflow
| Stage | Required Control |
| --- | --- |
| Intake | Identify source, owner, version, status, classification, source hash, and intended use. |
| Validate | Run metadata validation, classification scan, secret scan, link check, duplicate detection, and version conflict check. |
| Project | Create Markdown projection or curated summary from approved sources without changing source authority. |
| Review | Named knowledge steward and content owner validate accuracy, completeness, classification, and citations. |
| Approve | Publish approved note or artifact through Git/PR or controlled repository workflow. |
| Index | Index only retrieval-eligible content into LLM Wiki/LightRAG with batch ID, source hash, chunk metadata, and validation results. |
| Operate | Enforce SBAC/OPA, classification, freshness, conflict detection, citations, model-route eligibility, and audit trail. |
| Improve | Record corrections, stale signals, conflicts, retrieval failures, lessons learned, and improvement backlog items. |

## 6.9 LLM Wiki and Retrieval Eligibility Standard
| Eligibility Area | Required Rule |
| --- | --- |
| Allowed by default | Approved, current, classified, owner-assigned, source-linked, hash-verified, reviewed artifacts with retrieval_eligible = true. |
| Allowed only by explicit request | Draft, candidate, historical, superseded, experiment, or incomplete material when requester is authorized and intent is clear. |
| Blocked by default | Unclassified, stale, conflicting, expired, quarantined, duplicate-number conflict, secret-bearing, raw PII, raw production log, or unauthorized Restricted content. |
| Mandatory retrieval output | Document ID, title, version, section, source path, source tier, confidence, freshness status, classification decision, and evidence reference where available. |
| Mandatory audit | User/agent, query, policy decision, retrieved artifacts, model route, classification, timestamp, confidence, output reference, and evidence_ref. |

## 6.10 AI Assistant, Codex, AGENTS.md, and CLAUDE.md Controls

AI assistants must retrieve AIRA context through approved projects, connectors, LLM Wiki, knowledge APIs, or repository rules, not unmanaged personal copies.

AGENTS.md and CLAUDE.md must be generated or maintained from approved repository and knowledge governance baselines and must not weaken AIRA controls.

AI outputs are advisory or draft until reviewed, tested, and promoted through the required PR/MR, document-review, or evidence workflow.

Prompt, guardrail, model-route, retrieval-source, and AI-tool usage metadata must be captured when AI assistance affects engineering or governance artifacts.

Restricted, security-sensitive, customer, legal, or production-impacting content requires classification approval, model-route eligibility, and human review before use.

## 6.11 Security, Classification, and Privacy Controls

Do not store secrets, tokens, raw credentials, private keys, raw production logs, raw PII, unrestricted customer documents, or unsafe screenshots in Obsidian or LLM Wiki.

Apply malware scanning, secret scanning, classification scanning, redaction validation, and retention tagging before indexing uploaded files or evidence summaries.

Use approved encryption, access control, backup, sync, and version-history controls for the central vault and approved knowledge repositories.

Classification labels must propagate from source artifacts to Obsidian projections, LLM Wiki chunks, retrieval logs, and AI output evidence.

Knowledge access must fail closed when classification, SBAC, OPA, source hash, model route, or retrieval eligibility cannot be validated.

## 6.12 Freshness, Conflict, Quarantine, and Rebuild Controls
| Control | Required Evidence |
| --- | --- |
| Freshness manifest | Record source hash, artifact hash, indexed timestamp, source version, approval state, model/chunking configuration, and validation result. |
| Conflict detection | Flag contradictory rules, duplicate numbering, supersedence ambiguity, stale references, or active-source conflicts. |
| Quarantine triggers | Unclassified content, expired review date, stale source hash, secret/PII hit, unsafe link, duplicate conflict, weak provenance, or failed validation. |
| Rebuild triggers | New approved baseline, source-pack regeneration, major version update, classification change, security incident, schema change, or retrieval failure trend. |
| Recovery proof | Re-index report, sample queries, citation validation, source hash match, policy decision log, reviewer sign-off, and evidence_ref. |

## 6.13 Auto-Heal, Auto-Learn, and Auto-Improve Knowledge Loop

Knowledge automation may detect issues, retrieve evidence, propose candidate fixes, create draft summaries, recommend re-indexing, and open review items. It must not approve its own knowledge changes, promote drafts to authority, silently modify standards, weaken retrieval controls, bypass classification, or mutate production systems.
| Loop Stage | Required Control |
| --- | --- |
| Detection | Telemetry, CI/CD evidence, GitNexus impact, retrieval failures, stale index, user feedback, and conflict reports. |
| Evidence retrieval | Approved sources only; source IDs, hashes, citations, and classification decisions retained. |
| Candidate proposal | Draft correction, summary, metadata fix, quarantine action, re-index plan, or backlog item. |
| Verification | Human review, test query validation, citation audit, classification check, source hash verification, and evidence pack. |
| Promotion | Maker-checker approval; PR/MR or controlled knowledge workflow; updated freshness manifest and review queue. |

## 6.14 Observability and Evidence Requirements

Knowledge ingestion, projection, indexing, retrieval, quarantine, rebuild, and AI access must emit audit records with trace_id, actor, source, policy decision, and evidence_ref where practical.

Dashboards must track index freshness, retrieval denials, stale references, conflict counts, quarantine backlog, retrieval failures, citation quality, and knowledge review aging.

Logs must not contain secrets, raw PII, raw prompts containing Restricted data, raw embeddings, or high-cardinality sensitive identifiers.

Evidence must support reconstruction of who added or changed knowledge, why it was indexed, what source it came from, who approved it, what AI accessed it, and what answer used it.

## 6.15 Developer and Knowledge Steward Operating Procedure

Create or update official documents in approved Tier-0 systems or Git-backed knowledge repositories.

Do not copy complete code repositories, raw logs, secrets, or sensitive production data into Obsidian.

Add or update required metadata and classification before review.

Submit changes through PR/MR, CODEOWNERS, or an approved document-control workflow.

Run metadata, classification, secret, link, duplicate, and source-hash validation before approval.

Publish approved Markdown projections, curated summaries, diagrams, and evidence references to Obsidian.

Index only approved, current, classification-eligible artifacts into LLM Wiki or LightRAG.

Record freshness manifest, index batch ID, chunking/model configuration, and validation results.

Require AI assistants to cite document ID, version, section, and evidence references when answering from AIRA knowledge.

Quarantine stale, conflicted, unsafe, unclassified, or superseded artifacts and raise AVCI reconciliation items.

## 6.16 Validation Checklist
| Checklist ID | Pass Condition |
| --- | --- |
| VC-01 | Document ID, owner, version, status, classification, source path, and source hash are present. |
| VC-02 | Artifact is current, approved, and not superseded or expired. |
| VC-03 | Classification and SBAC/OPA policy allow retrieval by the intended user, agent, or model route. |
| VC-04 | No secrets, tokens, raw PII, raw production logs, unrestricted customer data, or unsafe attachments are present. |
| VC-05 | Citations include document ID, title, version, section, and evidence reference where available. |
| VC-06 | Freshness manifest includes source hash, artifact hash, index batch ID, and validation result. |
| VC-07 | Conflict check completed; unresolved conflicts are routed to AVCI reconciliation. |
| VC-08 | Human reviewer approved canonical publication or default retrieval eligibility. |
| VC-09 | AI outputs using this knowledge remain advisory until reviewed and promoted. |
| VC-10 | Audit record and improvement path are recorded. |

## 6.17 Anti-Patterns

Treating LLM Wiki, embeddings, graph edges, or AI summaries as official AIRA standards.

Copying the whole source code repository into Obsidian.

Allowing stale or superseded content to influence default AI retrieval.

Indexing unclassified content, Restricted data, secrets, raw PII, or raw logs without approved evidence controls.

Using personal vaults, unmanaged browser memory, or private AI accounts as AIRA knowledge authority.

Letting System Builder or an AI agent approve, publish, supersede, or quarantine knowledge without human governance.

Removing citations, source hashes, classification labels, or review metadata to simplify retrieval.

Using knowledge automation to bypass PR/MR, CODEOWNERS, CAB/ARB, security, or evidence requirements.

## 6.18 RACI
| Role | RACI | Responsibility |
| --- | --- | --- |
| Solutions Architecture Office / IT Head | A/R | Owns standard, precedence, and final governance interpretation. |
| Knowledge Governance Lead | A/R | Owns vault taxonomy, metadata, retrieval eligibility, index freshness, and quarantine workflow. |
| Security Architecture | A/R | Owns classification, secrets, Restricted content, model route, and retrieval safety controls. |
| DevSecOps Lead | R | Owns automation pipeline, PR/MR gates, CI validation, evidence generation, and GitNexus integration. |
| Data Governance / DBA | C/R | Owns data classification, retention, RLS-sensitive references, and database-backed metadata. |
| AI Governance / AI Engineering | C/R | Owns AI assistant retrieval, prompt/guardrail alignment, memory/RAG integrity, and model route evidence. |
| Software Development Lead | R | Ensures developers use approved knowledge sources and do not bypass repository rules. |
| Internal Audit | C/I | Reviews evidence, traceability, and control operation. |

## 6.19 Implementation Roadmap
| Phase | Outcome |
| --- | --- |
| Phase 1 | Stabilize source register, vault taxonomy, metadata template, classification rules, and retrieval eligibility checklist. |
| Phase 2 | Implement validation jobs for metadata, secrets, links, duplicates, source hashes, stale content, and conflict detection. |
| Phase 3 | Integrate LLM Wiki/LightRAG indexing with freshness manifest, chunk metadata, citation tests, and retrieval audit. |
| Phase 4 | Integrate Codex, Claude, ChatGPT, Hermes, System Builder, and approved AI agents through governed retrieval adapters. |
| Phase 5 | Operationalize dashboards, recurring reconciliation, Auto-Learn candidate queue, and quarterly knowledge control review. |

## 6.20 Acceptance Criteria

No full source-code repository is copied into Obsidian.

All default-retrievable content has required metadata, classification, source hash, owner, status, and review evidence.

LLM Wiki retrieval blocks stale, superseded, unclassified, conflicted, or unauthorized content by default.

AI responses sourced from AIRA knowledge provide citations and indicate uncertainty or conflict when detected.

Knowledge automation produces evidence and recommendations but does not approve or promote its own output.

Quarantine, re-indexing, conflict resolution, and freshness rebuild workflows are tested and auditable.

The review queue, canonical register, freshness manifest, and evidence references remain synchronized.

## 6.21 Change Log
| Version | Summary |
| --- | --- |
| v2.1 | Aligned source version before this review. |
| v2.2 | Golden Source, retrieval eligibility, AI governance, metadata, quarantine, conflict detection, freshness manifest, and evidence alignment update. |

# 7. Simplification Recommendations

Use one short operating rule in team communications: Tier-0 is authority; Obsidian is curated projection; LLM Wiki is governed retrieval; indexes and AI answers are derivative.

Create one reusable YAML/front-matter template for every knowledge artifact instead of many document-specific templates.

Use one central review queue and freshness manifest for all knowledge changes.

Keep only essential daily developer rules in AGENTS.md and CLAUDE.md; link to this standard for full governance.

Provide a one-page checklist for import, projection, indexing, and AI retrieval approval.

# 8. Automation Recommendations
| Automation Control | Recommended Implementation |
| --- | --- |
| Document inventory | Generate register from source folders, Obsidian vault, OpenKM export, and Git repositories. |
| Canonical register | Validate document ID, version, status, owner, classification, supersedes, superseded_by, source hash, and active/historical state. |
| Cross-reference validation | Check related document links, ADR links, repository paths, evidence references, and broken links. |
| Version tracking | Detect duplicate filenames, duplicate numbers, stale version references, and supersedence ambiguity. |
| Duplicate detection | Compare hashes, titles, document IDs, and semantic similarity before indexing. |
| Terminology consistency | Flag deviations from AIRA terms: AVCI, System Builder, MicroFunction, Dynamic Workspace, SBAC, OPA, GitNexus, Golden Source. |
| Conflict detection | Detect contradictory rules and route to AVCI reconciliation with owner, severity, and proposed governing source. |
| Missing-section detection | Check required document-control, purpose, scope, authority, evidence, security, observability, rollback, and AVCI sections. |
| Evidence checklist validation | Confirm evidence_ref, source_hash, reviewer, CI run, scan result, and policy-decision references where applicable. |
| Agent-assisted review queue | Use AI to propose queue priority, but require human confirmation before publication, retirement, or supersedence. |

# 9. Review Queue Control Register
| Seq | File Name | Pack | Current Version | Recommended Version | Review Status | Priority | Dependency | Action Required | Next Step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 33 | 26B-AIRA_Governed_Knowledge_Automation_Pipeline_Standard_v1.2_Aligned.docx | Pack 07 | v1.2 | v1.3 | Completed / Revised | P1 | Depends on 25, 21A, 18, 05, 06 | Completed | Retain as reviewed baseline |
| 34 | 13-AIRA_Obsidian_and_LLM_Wiki_Knowledge_Governance_Standard_v2.1_Aligned.docx | Pack 03 | v2.1 | v2.2 | Completed / Revised | P1 | Depends on 26B, 25, 21A, 18, 05, 06 | Completed | Promote as candidate after ARB/CAB/team review |
| 35 | 14-AIRA_Architecture_Decision_Record_and_Technical_Decision_Log_Standard_v2.2_Aligned.docx | Pack 03 | v2.2 | v2.3 | Next for Review | P1 | Depends on architecture, AVCI, knowledge, DevSecOps, API, database, security standards | Review and align | Review next |

# 10. Next Recommended Document

The next document should be 14-AIRA_Architecture_Decision_Record_and_Technical_Decision_Log_Standard_v2.2_Aligned.docx. It should be reviewed next because the knowledge governance layer now defines how authoritative decisions, source projections, citations, versioning, and evidence are represented. ADR/TDL governance must inherit these controls so architecture, technology, AI-agent, DevSecOps, database, API, security, MicroFunction, and System Builder decisions remain attributable, verifiable, classifiable, improvable, and traceable from decision to implementation evidence.

# 11. External Reference Register
| Reference | Alignment Use |
| --- | --- |
| OpenAI Codex AGENTS.md guidance | Used to align repository-local AI instructions and agent guidance. |
| GitHub CODEOWNERS and branch protection documentation | Used to align review ownership and protected-branch controls. |
| Obsidian security and privacy / Sync documentation | Used to align vault security, privacy, and encryption considerations. |
| Anthropic Claude Code memory / CLAUDE.md guidance | Used to align repository-local AI memory and project instruction behavior. |

