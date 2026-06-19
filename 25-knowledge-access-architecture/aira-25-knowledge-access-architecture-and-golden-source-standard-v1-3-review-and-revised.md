---
title: "Knowledge Access Architecture and Golden Source Standard"
doc_id: "AIRA-25"
version: "v1.3"
status: "revised"
category: "Knowledge access architecture"
source_docx: "AIRA_25_Knowledge_Access_Architecture_and_Golden_Source_Standard_v1_3_Review_and_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 25-knowledge-access-architecture
  - revised
  - aira-25
---



# Knowledge Access Architecture and Golden Source Standard



AIRA
AI-Native Enterprise Platform

AIRA Knowledge Access Architecture and Golden Source Standard

Review, Alignment, and Revised Standard

Recommended Version v1.3
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-025 |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Architecture Review Board, Security Governance, DevSecOps, Knowledge Governance, and Team Review |
| Owner | Solutions Architecture Office / IT Head |
| Review Date | 2026-06-16 |
| Prepared For | AIRA Software Development, DevSecOps, Security, QA/SDET, Platform Engineering, Knowledge Governance, AI Governance, and Internal Audit Teams |

# Document Control
| Field | Value |
| --- | --- |
| Document title | AIRA Knowledge Access Architecture and Golden Source Standard |
| Document ID | AIRA-DOC-025 |
| Source document reviewed | 25-AIRA_Knowledge_Access_Architecture_and_Golden_Source_Standard_v1.2_Aligned.docx |
| Recommended version | v1.3 |
| Supersedes | v1.2 aligned candidate after approval |
| Classification | INTERNAL CONFIDENTIAL |
| Document owner | Solutions Architecture Office / IT Head |
| Co-owners | Enterprise Architecture; Knowledge Governance; DevSecOps; Security Architecture; AI Governance; Platform Engineering; Software Development Lead; QA/SDET; Internal Audit |
| Target audience | Software Developers; DevSecOps; Security; QA/SDET; DBA; Platform Engineering; AI Agent Owners; Knowledge Stewards; Internal Audit |
| Related AIRA documents | 01A v1.2; 01 v3.2; 01B v1.2; 02 v5.2; 03 v4.2; 04 v9.2; 05 v4.2; 06 v3.2; 18 v1.2; 19 v1.3; 20 v1.2; 21A v1.2; 26B; 31A; 42I; updated MicroFunction baseline 10 through 10E |
| Change summary | Clarified Golden Source boundaries, retrieval eligibility, AI assistant access, Obsidian/LLM Wiki derivative status, GitNexus read-only status, evidence/freshness manifests, conflict quarantine, and System Builder consumption rules. |

# Table of Contents Placeholder

Insert Microsoft Word automatic table of contents here before final publication. Use References > Table of Contents > Automatic Table, then update fields after approval.

# 1. Executive Review Summary

This review confirms that the source document is directionally correct and should be retained as the governing Golden Source boundary standard for AIRA knowledge access. The revision strengthens the standard so that software developers, DevSecOps, knowledge stewards, AI assistants, System Builder, and future AIRA agents consistently know where authoritative truth lives and how derivative knowledge may be safely used.

The most important correction is to make source authority non-negotiable. Git repositories remain authoritative for source code, tests, contracts, migrations, policies, infrastructure-as-code, and agent/rule files. GitNexus remains derivative, read-only, commit-bound code intelligence. Obsidian remains a curated knowledge projection and documentation vault. LLM Wiki, LightRAG, embeddings, graph indexes, summaries, and AI responses remain derivative retrieval layers. OpenKM, approved DOCX/PDF records, Git, databases, workflow histories, evidence stores, security stores, and audit trails remain Tier-0 authority where applicable.

The revised document also adds enforceable rules for classification-aware retrieval, SBAC and OPA decisions, freshness manifests, conflict detection, stale-source quarantine, AI citation requirements, model-route eligibility, and non-authoritative AI outputs. These controls are necessary before AIRA uses ChatGPT, Codex, Claude, Hermes, System Builder agents, or future AI agents against project knowledge.

# 2. Alignment Findings
| AIRA area | Required alignment for v1.3 |
| --- | --- |
| Enterprise Architecture and AVCI | Every knowledge artifact must retain owner, source, version, classification, verification path, and improvement path. |
| Information Nervous System | Knowledge tiers, retrieval eligibility, provenance, freshness, evidence, memory, and conflict handling must be explicit. |
| Repository and Golden Source | Git remains authority for executable artifacts; Obsidian and LLM Wiki must not become shadow repositories. |
| GitNexus | GitNexus output is read-only, derivative, commit-bound, and must not approve, merge, deploy, mutate, or replace tests and scans. |
| DevSecOps and Evidence | Knowledge updates must carry CI/CD, security, test, evidence-pack, SBOM/provenance, and review references where applicable. |
| MicroFunction baseline | MicroFunction catalog, runtime configuration, event contracts, policy references, observability, and evidence artifacts must be linked by exact source references. |
| System Builder | System Builder may analyze, recommend, draft, and package evidence; it must not silently promote knowledge, override authoritative sources, or bypass human review. |
| AI Agent Governance | Agent memory and retrieval are evidence inputs, not authority; unsafe, stale, conflicting, unclassified, or unapproved knowledge must be quarantined. |

# 3. Review and Gap Analysis
| Review area | Assessment | v1.3 correction |
| --- | --- | --- |
| Retain | The Golden Source rule is correct: code, code intelligence, governed knowledge, retrieval indexes, and AI assistant access require separate authority boundaries. | Retained and promoted to mandatory practice statement. |
| Correct | Prior wording could allow Obsidian or LLM Wiki to appear authoritative for more content than intended. | Clarified derivative status and authority hierarchy. |
| Strengthen | Freshness, source hash, artifact hash, and retrieval eligibility needed stronger implementation rules. | Added freshness manifest and retrieval gate requirements. |
| Strengthen | AI assistant access needed stronger SBAC/OPA, model route, guardrail, and audit requirements. | Added retrieval authorization, model eligibility, and audit evidence fields. |
| Simplify | Developers need a practical rule: do not copy full source code into Obsidian. | Converted into a non-negotiable developer rule with permitted derived artifacts. |
| Add | Conflict detection and stale-source quarantine should be explicit. | Added conflict classification, quarantine states, and reconciliation path. |
| Add | System Builder use of knowledge needed boundaries. | Added System Builder knowledge-consumption and generated-knowledge promotion rules. |
| Add | Auto-Learn, Auto-Heal, Auto-Improve needed knowledge-loop boundaries. | Added candidate-only loops with source evidence, tests, human review, and approved promotion. |

# 4. Revised Full AIRA Document

## 4.1 Mandatory Practice Statement

AIRA knowledge access is governed by source authority, not convenience. Code lives in Git repositories. Code intelligence lives in GitNexus as read-only derivative analysis. Governed knowledge lives in Obsidian or the approved documentation repository as curated, versioned, reviewed knowledge. Unified retrieval lives in LLM Wiki, LightRAG, indexes, embeddings, and knowledge APIs as derivative access paths only. AI assistants, System Builder, and AI agents may consume knowledge only through classification-aware, SBAC/OPA-controlled, audited, citation-ready, freshness-validated, and evidence-producing channels.

No AIRA team member, tool, AI assistant, System Builder workflow, or agent may treat an AI answer, embedding, summary, graph edge, GitNexus report, Obsidian projection, LLM Wiki result, or cached retrieval as authority unless it can be traced to an approved source of truth and passes classification, freshness, conflict, and retrieval eligibility checks.

## 4.2 Purpose

Define the authoritative source boundaries for AIRA source code, code intelligence, documents, evidence, policies, contracts, runtime configuration, prompts, agent instructions, and retrieval outputs.

Prevent duplicate Golden Sources, uncontrolled copying, stale AI context, sensitive data leakage, and inconsistent developer guidance.

Define how GitHub/GitLab, GitNexus, Obsidian, LLM Wiki/LightRAG, OpenKM, evidence stores, AIRA Knowledge API, Codex, Claude, ChatGPT, Hermes, System Builder, and AI agents interact safely.

Establish retrieval, citation, classification, freshness, and audit requirements for AI-assisted development and knowledge consumption.

## 4.3 Scope
| In scope | Out of scope |
| --- | --- |
| Git repositories, source code, tests, contracts, Flyway migrations, OPA/Rego policies, infrastructure-as-code, devcontainers, CI/CD templates, AGENTS.md, CLAUDE.md, prompt standards, MicroFunction runtime configuration, evidence manifests, and AI assistant retrieval. | Copying full source repositories into Obsidian, using Obsidian as a build system, using LLM Wiki as source authority, allowing AI tools to bypass Git/CI/CODEOWNERS, storing secrets in knowledge systems, or using unapproved AI connectors. |
| Obsidian projections, LLM Wiki/LightRAG indexes, GitNexus reports, evidence summaries, knowledge freshness manifests, document registers, conflict registers, and retrieval audit records. | Direct production mutation, direct model-provider calls from application code, unauthorized retrieval of Restricted data, or unreviewed promotion of AI-generated knowledge. |

## 4.4 Authority Model
| Authority tier | Authoritative examples | Treatment |
| --- | --- | --- |
| Tier 0 - Source of Truth | Approved DOCX/PDF records, Git repositories, OpenKM, databases, workflow histories, security/evidence stores, audit records. | Authoritative when approved, controlled, versioned, classified, and evidence-backed. |
| Tier 1 - Governed Working Projection | Git-managed Obsidian vault, approved Markdown projections, ADR/TDL/runbook repositories. | May be authoritative for working knowledge only when linked to Tier-0 source and approved. |
| Tier 2 - Curated Retrieval Knowledge | LLM Wiki, curated LightRAG corpus, citation-ready summaries, human-reviewed knowledge cards. | Derivative; must show source, version, status, freshness, and classification. |
| Tier 3 - Retrieval Indexes and Caches | Embeddings, vector indexes, graph edges, search indexes, semantic caches, Redis/Valkey caches. | Non-authoritative accelerators; must be rebuildable and invalidated when stale. |
| Tier 4 - AI Outputs | ChatGPT, Codex, Claude, Hermes, agents, System Builder narratives, summaries, recommendations, drafts. | Advisory only until reviewed, tested, classified, and promoted through governed change control. |

## 4.5 Golden Source Boundary Rules
| Artifact type | Golden Source | May be indexed by | Obsidian treatment |
| --- | --- | --- | --- |
| Source code | Git repository | GitNexus; LLM Wiki/LightRAG via governed read-only connector | Summary and exact links only; no full copy. |
| Tests and fixtures | Git repository | CI evidence tools; GitNexus; retrieval index | Evidence summary only; synthetic fixtures only. |
| OpenAPI, AsyncAPI, Avro, CloudEvents schemas | Git repository / contract registry | Contract registry; LLM Wiki; CI checks | Contract summary and versioned links. |
| Flyway migrations and seed data | Git repository and controlled database migration history | CI; DB evidence; GitNexus; knowledge index | Summary and migration evidence only. |
| OPA/Rego policies | Git repository / policy registry | Policy tests; CI; LLM Wiki | Policy summary, tests, and decision references. |
| AIRA standards, ADRs, TDLs, runbooks | Approved DOCX/PDF, Git-backed docs, OpenKM, Obsidian projection | LLM Wiki/LightRAG; knowledge API | Primary curated working knowledge if source-linked. |
| CI/CD, SAST, DAST, SBOM, provenance evidence | CI artifact store / evidence repository | Evidence index; GitNexus summaries | Curated evidence summary and links. |
| Logs, traces, metrics | Observability platform and audit/evidence store | Governed analytics only | No raw copy; summary only. |
| Secrets and credentials | Vault/OpenBao/approved secret manager | Never indexed | Never stored or summarized. |

## 4.6 Prohibited Patterns

Copying full backend, frontend, database, infrastructure, or policy repositories into Obsidian.

Using Obsidian as the place where production code, policies, migrations, or infrastructure changes are authored outside Git review.

Treating GitNexus, LLM Wiki, embeddings, summaries, or AI responses as architecture, security, database, policy, or release authority.

Indexing secrets, raw tokens, private keys, Restricted data, unredacted PII, raw customer files, production logs, or confidential prompts without approved classification and redaction.

Allowing AI assistants or System Builder to apply changes directly to source, database, workflow, production runtime, or knowledge authority without PR/MR, review, CI, evidence, and approval gates.

Using stale, superseded, conflicting, unclassified, or unapproved documents as retrieval-eligible context.

## 4.7 Required Knowledge Metadata
| Field | Mandatory purpose |
| --- | --- |
| document_id / artifact_id | Stable identifier for traceability. |
| title / canonical_filename | Human-readable reference and canonical storage name. |
| version / status | Determines whether artifact is draft, review-ready, approved, superseded, deprecated, or revoked. |
| owner / co_owners | Defines accountable human and supporting roles. |
| classification / handling_rule | Controls retrieval, storage, prompt eligibility, model route, and retention. |
| source_ref / source_hash / artifact_hash | Proves provenance and freshness. |
| related_adr_tdl / related_ticket / related_pr | Links knowledge to decision and change records. |
| retrieval_eligibility | States whether artifact may be used by AI and under which role/model-route constraints. |
| review_due / supersedes / superseded_by | Supports lifecycle control and stale-source quarantine. |
| evidence_ref | Links tests, scans, approvals, audit, runtime evidence, or CI/CD evidence. |

## 4.8 Retrieval Eligibility Gate
| Gate | Required pass condition | Evidence |
| --- | --- | --- |
| Source authority | Artifact traces to approved Tier-0 or Tier-1 source, or is marked candidate only. | source_ref, hash, owner, version, status. |
| Classification | Classification and handling rule are present and enforceable. | OPA/SBAC decision and routing evidence. |
| Freshness | Artifact hash matches indexed hash and is not stale, expired, superseded, or revoked. | freshness manifest and index timestamp. |
| Conflict check | No higher-authority conflict exists; unresolved conflict is quarantined. | conflict scan result and reconciliation item. |
| Security hygiene | No secrets, raw PII, Restricted data, or unsafe prompt content are indexed incorrectly. | DLP/secret scan and reviewer attestation. |
| Citation quality | Retrieved answer can cite approved source, version, and evidence. | citation record and retrieval trace. |
| Human review | High-impact or promotion-bound knowledge has owner/checker approval. | approval record, PR/MR, CAB/ARB reference. |

## 4.9 AI Assistant, Codex, Claude, Hermes, and System Builder Access Rules

AI assistants may retrieve approved context only through AIRA Knowledge API, approved connector, LLM Wiki/LightRAG, or controlled repository context with classification-aware access.

Repository-local AI behavior must inherit the approved CLAUDE.md and AGENTS.md rules and must not weaken branch protection, CODEOWNERS, CI gates, testing, security scans, policy checks, or human review.

System Builder may analyze sources, generate recommendations, draft candidate artifacts, and prepare evidence packs. It must not approve, merge, publish, promote, deploy, or silently mutate authoritative knowledge.

AI-generated summaries, diagrams, prompts, runbooks, tests, code, policies, or migrations are candidate artifacts until reviewed, classified, tested where applicable, source-linked, and promoted through PR/MR or approved document-control workflow.

Agent memory, RAG context, embeddings, and retrieval outputs are treated as evidence inputs, not as business authority. Unsafe memory or context must be quarantined, not learned silently.

## 4.10 Knowledge and Code Flow

Documentation flow: approved source document or ADR is changed in the controlled source location, validated for metadata and classification, reviewed, merged or approved, projected into Obsidian where applicable, indexed into LLM Wiki/LightRAG, and recorded in the freshness manifest.

Code flow: developer or approved AI coding assistant creates a Git branch or pull request; CI/CD runs unit, integration, security, contract, architecture, and evidence checks; GitNexus produces read-only impact evidence; derived summaries may be curated into Obsidian; AI retrieval references exact repository, branch, commit, path, and evidence records.

AI retrieval flow: an assistant query passes through identity, SBAC, classification, model-route, freshness, conflict, and citation checks before approved context is returned. If any required control fails, the retrieval must block, return uncertainty, or request human review rather than fail open.

## 4.11 Auto-Learn, Auto-Heal, and Auto-Improve Knowledge Loop
| Loop | Permitted action | Required gate |
| --- | --- | --- |
| Auto-Learn | Convert approved PRs, incident RCAs, test failures, postmortems, review findings, and operational outcomes into candidate knowledge. | Source citations, classification check, conflict check, reviewer approval, evidence reference, review_due. |
| Auto-Heal | Use approved knowledge and evidence to draft remediation guidance, runbook updates, tests, or candidate PRs. | Root-cause evidence, minimal change, tests, security check, rollback path, human approval. |
| Auto-Improve | Propose refactoring, policy improvement, template improvement, retrieval tuning, or standard update. | Measurable benefit, ADR/TDL where material, principle-impact assessment, QA/security evidence, ARB/CAB where required. |
| AutoResearch | Collect and summarize current external or internal signals. | Non-authoritative until source-cited, classified, verified, and promoted. |

## 4.12 Observability, Audit, and Evidence Requirements
| Signal | Required treatment |
| --- | --- |
| Retrieval audit | Record actor, tool/agent, source IDs, classification, SBAC decision, model route, query class, evidence_ref, and result disposition. |
| Freshness evidence | Record source hash, index hash, indexed timestamp, stale/valid state, rebuild reference, and reviewer. |
| Conflict evidence | Record conflicting sources, governing source, severity, owner, reconciliation item, and disposition. |
| Security evidence | Record DLP/secret scan, redaction state, retention rule, and Restricted-data exclusion. |
| Usage metrics | Measure retrieval success, stale-source blocks, policy denies, citation completeness, index latency, and AI hallucination corrections. |
| Runtime toggles | Diagnostic verbosity and sampling may be tuned; audit, policy decisions, classification decisions, source references, and critical evidence must not be disabled. |

## 4.13 Acceptance Criteria

Every knowledge artifact has owner, version, status, classification, source reference, source hash, and review state.

Full source code repositories are not copied into Obsidian; only reviewed summaries, maps, diagrams, evidence summaries, and exact Git references are permitted.

AI assistants retrieve AIRA knowledge only through approved, classified, audited, source-linked, freshness-checked paths.

LLM Wiki, LightRAG, embeddings, caches, and AI outputs are treated as derivative and rebuildable.

Unclassified, stale, superseded, conflicting, revoked, or unsafe knowledge is excluded from retrieval or explicitly marked as non-authoritative.

GitNexus remains read-only, derivative, commit-bound, and unable to approve, merge, deploy, mutate, or replace tests/scans/human review.

System Builder and AI agents cannot promote candidate knowledge or generated artifacts without human review, evidence, and approved change-control path.

# 5. Simplification Recommendations

Use the one-line rule in all onboarding and repository templates: Code in Git, code intelligence in GitNexus, governed knowledge in Obsidian, retrieval in LLM Wiki/LightRAG, and AI access through governed connectors.

Provide developers with a short allowed/prohibited examples table for Obsidian content.

Generate metadata templates automatically for new standards, ADRs, prompts, runbooks, and evidence summaries.

Use a single freshness manifest instead of ad hoc spreadsheet tracking for indexing and retrieval readiness.

Automate stale-source and duplicate-number detection but keep promotion approval human-controlled.

# 6. Automation Recommendations
| Automation area | Recommended control |
| --- | --- |
| Document inventory | Maintain canonical manifest with document ID, title, version, status, owner, classification, source path, source hash, and supersedence. |
| Cross-reference validation | Detect broken links, stale companion references, superseded document references, duplicate numbers, and missing companion documents. |
| Terminology consistency | Validate canonical terms: AIRA, AVCI, System Builder, MicroFunction, GitNexus, Obsidian, LLM Wiki, LightRAG, SBAC, OPA, LiteLLM, NeMo Guardrails. |
| Conflict detection | Compare active standards and flag conflicts by severity with recommended governing source. |
| Metadata validation | Reject knowledge artifacts missing owner, version, classification, status, source_ref, evidence_ref, or retrieval eligibility. |
| Security scanning | Run DLP/secret scans before Obsidian projection or LLM Wiki indexing. |
| Freshness manifest | Update source hash, artifact hash, index timestamp, and stale/valid state on each approved change. |
| Agent-assisted review queue | Use AI to draft findings and queue items, but require human approval before canonical promotion. |
| Obsidian/Git tracking | Treat Obsidian vault changes as Git pull requests with CODEOWNERS, branch protection, CI checks, and evidence summary. |

# 7. Review Queue Control Register
| Seq | File Name | Pack | Current Version | Recommended Version | Review Status | Priority | Dependency | Action Required | Next Step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 31 | 21A-AIRA_Governed_Knowledge_Control_Plane_Obsidian_Codex_GitHub_Standard_v1.1_Aligned.docx | Pack 05 | v1.1 | v1.2 | Completed / Revised | P1 | Knowledge control plane | Completed | Use as aligned control-plane baseline |
| 32 | 25-AIRA_Knowledge_Access_Architecture_and_Golden_Source_Standard_v1.2_Aligned.docx | Pack 06 | v1.2 | v1.3 | Completed / Revised | P1 | 21A, 18, 05, 06, 19, 20 | Completed | Adopt as Golden Source boundary candidate after review |
| 33 | 26B-AIRA_Governed_Knowledge_Automation_Pipeline_Standard_v1.2_Aligned.docx | Pack 07 | v1.2 | v1.3 | Next for Review | P1 | 25 v1.3, 21A v1.2, 18 v1.2 | Review and align | Proceed next |

# 8. Change Log
| Version | Date | Summary | Owner |
| --- | --- | --- | --- |
| v1.3 | 2026-06-16 | Review and revised version aligned with 21A v1.2, 18 v1.2, 05 v4.2, 06 v3.2, GitNexus, DevSecOps, MicroFunction, API, database/Flyway, security, and AI governance baselines. | Solutions Architecture Office / IT Head |
| v1.2 | Prior aligned source | Aligned source-pack candidate. | Solutions Architecture Office |

# 9. AVCI Compliance Summary
| AVCI property | Evidence in this revised standard |
| --- | --- |
| Attributable | Defines owners, source tiers, document IDs, source references, hashes, source paths, actor/tool access, and review ownership. |
| Verifiable | Requires freshness manifests, source hashes, retrieval audit, conflict checks, CI/evidence links, and citation-ready AI retrieval. |
| Classifiable | Requires classification, handling rules, retrieval eligibility, SBAC/OPA controls, DLP/secret scans, and Restricted-data exclusion. |
| Improvable | Defines Auto-Learn, Auto-Heal, Auto-Improve, AutoResearch, stale-source quarantine, supersedence, and review cadence. |

