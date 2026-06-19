---
title: "Governed Knowledge Control Plane Obsidian Codex GitHub Standard"
doc_id: "AIRA-21A"
version: "v1.2"
status: "revised"
category: "Knowledge control plane"
source_docx: "AIRA_21A_Governed_Knowledge_Control_Plane_Obsidian_Codex_GitHub_Standard_v1_2_Review_and_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 21-knowledge-control-plane
  - revised
  - aira-21a
---



# Governed Knowledge Control Plane Obsidian Codex GitHub Standard



AIRA

AI-Native Enterprise Platform

Governed Knowledge Control Plane -
Obsidian, Codex, and GitHub Standard

Central Knowledge | AI Assistant Context | GitHub Traceability | Golden Source Synchronization | AVCI Always

Version v1.2 - Review and Revised Edition

Status: Draft for Architecture Review Board / CAB / Knowledge Governance Review

Classification: INTERNAL CONFIDENTIAL

Prepared for: AIRA Software Development, DevSecOps, Security, Knowledge Governance, AI Governance, Platform Engineering, SRE, and Internal Audit Teams

Prepared by: AIRA Enterprise Architecture, Governance, AI DevSecOps, Security, and Documentation Review Board

Review Date: 2026-06-16

# 1. Document Control
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-021A |
| Document Title | AIRA Governed Knowledge Control Plane - Obsidian, Codex, and GitHub Standard |
| Recommended Version | v1.2 - Golden Source, AI Assistant Adapter, Retrieval, Evidence, and Control-Plane Alignment Update |
| Source Document Reviewed | 21A-AIRA_Governed_Knowledge_Control_Plane_Obsidian_Codex_GitHub_Standard_v1.1_Aligned.docx |
| Supersedes | 21A-AIRA_Governed_Knowledge_Control_Plane_Obsidian_Codex_GitHub_Standard_v1.1_Aligned.docx after ARB/CAB approval |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Architecture Review Board, CAB, Knowledge Governance, DevSecOps, Security, AI Governance, Platform Engineering, and Internal Audit Review |
| Document Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Knowledge Governance; DevSecOps Lead; Software Development Lead; Security Architecture; QA/SDET; Platform Engineering; AI Governance; SRE; Internal Audit |
| Primary Audience | Software Developers; Knowledge Stewards; DevSecOps; Security; AI Assistant Owners; System Builder Operators; Architects; Reviewers; Internal Audit |
| Review Cadence | Quarterly; unscheduled on material source authority, Obsidian, LLM Wiki, Codex, Claude Code, GitHub/GitLab, connector, MCP, classification, retrieval, evidence, or AI governance change |
| Governing Parents | 01A v1.2; 01 v3.2; 01B v1.2; 02 v5.2; 05 v4.2; 06 v3.2; 18 v1.2; 19 v1.3; 20 v1.2 |
| Related Standards | 10 v3.3; 10A v2.3; 10B v2.2; 10C v2.2; 10D v2.2; 10E v1.2; 11 v3.2; 11A v1.2; 15 v2.2; 15A v1.2; 16 v2.2; 16A v1.3; 16B v1.2; 17 v2.2; 17A v1.2 |
| External Alignment Checked | OpenAI Codex AGENTS.md guidance; GitHub CODEOWNERS and branch protection documentation; Anthropic Claude Code memory guidance; Obsidian Sync guidance; NIST SSDF; SLSA; OWASP ASVS |
| Change Summary | Aligns knowledge control plane with current AIRA source authority, AI assistant adapter governance, Golden Source, retrieval eligibility, CI/CD evidence, GitNexus, security, and System Builder constraints. |

# 2. Table of Contents Placeholder

Insert Microsoft Word automatic Table of Contents here before final publication: References > Table of Contents > Automatic Table. Update fields after final pagination.

# 3. Executive Review Summary

The v1.1 source document is structurally sound and should be retained as the foundation for AIRA knowledge-control-plane governance. It correctly defines one governed knowledge baseline consumed through controlled adapters by Obsidian, LLM Wiki, ChatGPT/Codex, Claude Code, IDE assistants, GitHub/GitLab, CI/CD, developers, and future AI agents.

Version v1.2 strengthens the standard after the updated Golden Source, CLAUDE.md, GitNexus, CI/CD, DevSecOps, MicroFunction, API, database/Flyway, security, and evidence baselines. The revised position is that Tier-0 sources remain authoritative; Obsidian is a Git-managed working and curated projection; LLM Wiki and retrieval indexes are derivative; GitNexus is read-only derivative code intelligence; AI assistants are consumers of governed knowledge and may draft, analyze, recommend, or create branch-bound candidate artifacts only through policy, classification, evidence, and human review controls.

Recommended Review Verdict: Promote v1.2 as the candidate control-plane standard after ARB/CAB/Knowledge Governance/Security/DevSecOps/AI Governance review. It should be enforced before broad team use of Obsidian, Codex, Claude Code, AGENTS.md adapters, LLM Wiki, connectors, MCP tools, or System Builder source retrieval.

# 4. Source and Context Alignment Findings
| Control Area | Alignment Required in v1.2 |
| --- | --- |
| AIRA source authority | Approved DOCX/PDF, Git repositories, ADRs/TDLs, PR/MR evidence, CI/CD records, OpenKM/DMS records, databases, workflow records, and audit stores remain Tier-0 or controlled authoritative sources. |
| Obsidian | Obsidian is a Git-managed working projection and curated knowledge vault. It must not become an unmanaged source dump, uncontrolled full-code mirror, or bypass for approved repositories and document registers. |
| LLM Wiki and retrieval indexes | LLM Wiki, pgvector, LightRAG, embeddings, semantic indexes, graph indexes, and summaries are derivative. They require classification, SBAC, freshness, provenance, quarantine, and citation controls. |
| GitHub/GitLab | Source code, contracts, policies, migrations, CI/CD, IaC, devcontainers, AGENTS.md, CLAUDE.md, and evidence manifests remain governed in repositories with CODEOWNERS, branch protection, required checks, and PR/MR AVCI evidence. |
| Codex and coding assistants | Codex and equivalent coding assistants must consume AGENTS.md / CLAUDE.md-derived rules and repository context. They may generate candidate artifacts but must not approve, merge, deploy, disable controls, or access production secrets. |
| Claude Code and IDE assistants | Claude Code, IDE assistants, and tool adapters must not have weaker rules than CLAUDE.md. Tool actions must remain bounded by SBAC/OPA/Harness/MCP gateway, classification, and audit. |
| GitNexus | GitNexus is read-only, derivative, commit-bound code intelligence. It may provide maps, impact analysis, and evidence summaries but cannot replace source, tests, scans, policy, or human review. |
| System Builder | System Builder uses the control plane to classify requests, retrieve authoritative sources, draft recommendations, generate candidate artifacts, and produce evidence; it must not silently mutate canonical sources or runtime behavior. |
| MicroFunction delivery | MicroFunction catalog, runtime configuration, API/event contracts, database migrations, observability, security, and evidence assets must be projected as governed metadata and references, not uncontrolled duplication. |
| Security and classification | All retrieval, indexing, summarization, connector, and assistant access requires classification, SBAC, redaction, secrets scanning, retention, logging, and fail-closed handling. |
| DevSecOps and evidence | Knowledge updates, adapter generation, retrieval refresh, AI output, and source projection require PR/MR evidence, CI checks, validation manifests, and review queue updates. |

# 5. Review and Gap Analysis
| Finding Type | Assessment | v1.2 Treatment |
| --- | --- | --- |
| Retain | The v1.1 document correctly rejects unmanaged shared folders, uncontrolled AI uploads, and multiple inconsistent rulebooks. | Retained as the core operating position. |
| Retain | Tier-0 official sources, GitHub/GitLab, Obsidian projection, LLM Wiki retrieval, and derivative indexes are correctly separated. | Retained and made more explicit with source-tier rules and blocking conditions. |
| Strengthen | AI assistant adapter rules were present but needed stronger alignment with revised CLAUDE.md, AGENTS.md, Codex, Claude Code, and CI strict mode. | Added adapter governance, rule compilation, and no-weaker-than-canonical controls. |
| Strengthen | GitNexus and evidence summary handling needed alignment with v1.3 GitNexus and v1.2 CI/CD evidence pack. | Added commit-bound derivative intelligence and PR/MR evidence requirements. |
| Strengthen | Retrieval eligibility needed stronger classification, freshness, quarantine, and evidence-reconstruction controls. | Added mandatory retrieval decision gate and source-freshness manifest. |
| Strengthen | System Builder use of knowledge sources needed stronger no-silent-mutation controls. | Added System Builder retrieval and generation guardrails. |
| Simplify | The original document was comprehensive but could be simplified for team execution. | Added clearer source-tier model, daily workflow, role responsibilities, and acceptance checklist. |
| Add | Runtime controls for connectors, MCP, apps, and AI assistant tool access were not sufficiently operational. | Added connector registry, allowlist, access logging, review cadence, and revocation rules. |
| Add | Knowledge automation linkage with 26B and 25 needed clearer sequencing. | Added review queue and next-document dependency path. |

# 6. Revised Full AIRA Document

## 6.1 Mandatory Practice Statement

AIRA knowledge must be governed before it is retrieved, summarized, indexed, projected, or used by humans, AI assistants, System Builder, agents, pipelines, or dashboards. Approved sources remain authoritative; projections and indexes remain derivative; AI outputs remain advisory or candidate artifacts until reviewed and promoted. No AIRA knowledge-control-plane component may bypass classification, SBAC, OPA, CODEOWNERS, CI/CD gates, evidence requirements, source registers, human approval, or retention controls.

## 6.2 Purpose

This standard defines how AIRA governs the relationship among Obsidian, GitHub/GitLab, Codex, Claude Code, ChatGPT Projects, IDE assistants, LLM Wiki, GitNexus, evidence stores, connectors, and future System Builder retrieval services. Its purpose is to prevent knowledge drift, duplicate golden sources, classification leakage, stale AI context, uncontrolled agents, and unverifiable AI-generated claims.

## 6.3 Scope
| In Scope | Out of Scope |
| --- | --- |
| Git-managed Obsidian vaults, source projections, curated knowledge pages, ADR/TDL projections, standards, runbooks, prompts, and reviewed evidence summaries. | Unmanaged local folders, personal AI uploads, uncontrolled knowledge copies, unapproved plugins, private accounts, and unreviewed AI-generated standards used as authority. |
| GitHub/GitLab source repositories, PR/MR evidence, CODEOWNERS, branch protection, CI/CD, AGENTS.md, CLAUDE.md, contracts, migrations, policies, tests, and evidence manifests. | Replacing Git/GitHub/GitLab or OpenKM/DMS with Obsidian, LLM Wiki, GitNexus, embeddings, or AI-generated summaries as the sole authority. |
| LLM Wiki, retrieval gateway, metadata registry, freshness manifest, embeddings, graph indexes, citations, source hashes, classification, retention, and quarantine. | Indexing Restricted or secret-bearing content without classification approval, redaction, SBAC, retention rule, and retrieval eligibility. |
| Codex, Claude Code, ChatGPT, IDE assistants, Hermes, System Builder, and future AI agents consuming governed context. | AI assistants approving their own output, mutating production, bypassing policy, or receiving direct production credentials. |

## 6.4 Authority and Source Tiering Model
| Tier | Authority | Examples | Rule |
| --- | --- | --- | --- |
| Tier 0 | Authoritative records | Approved DOCX/PDF standards, OpenKM/DMS, Git repositories, signed releases, ADRs, TDLs, PR/MR records, CI evidence, audit logs, database records, workflow histories. | Used as source of truth. Changes require governed approval and evidence. |
| Tier 1 | Governed working projection | Git-managed Obsidian vault, curated Markdown projections, approved diagrams, runbooks, onboarding notes, reviewed evidence summaries. | May support daily work when linked to Tier-0 source, version, owner, classification, and source hash. |
| Tier 2 | Curated retrieval layer | LLM Wiki, Knowledge API, approved retrieval packs, citation-ready summaries, question-answer indexes. | Derivative. Requires freshness, classification, SBAC, provenance, and citation. |
| Tier 3 | Technical indexes and caches | pgvector, LightRAG, embeddings, graph edges, search indexes, GitNexus indexes, Redis/Valkey caches. | Derivative and non-authoritative. Must be rebuildable and revocable. |
| Tier 4 | AI-generated outputs | Draft answers, candidate code, candidate docs, candidate policies, summaries, review notes, proposed fixes. | Advisory or draft only until reviewed, tested, approved, and promoted. |

## 6.5 Non-Negotiable Operating Principles

One governed baseline: AIRA must maintain one approved source baseline and generate tool-specific adapters from it. Do not maintain separate weaker rulebooks for Codex, Claude, IDEs, or CI/CD.

Tier-0 authority remains explicit: Obsidian, LLM Wiki, GitNexus, embeddings, and summaries must not override approved documents, Git repositories, OpenKM/DMS records, or audit/evidence stores.

No full source-code copy into Obsidian: only curated summaries, code maps, evidence summaries, contract references, and exact Git references may be projected unless specifically approved.

AI context must be classified: every retrieval or prompt context must include source, classification, owner, freshness, allowed use, and evidence reference.

AI assistants may draft, analyze, recommend, and generate candidate artifacts; they must not approve, merge, deploy, silently mutate canonical sources, or disable controls.

AGENTS.md and tool adapters must be generated from or aligned to CLAUDE.md and must never weaken root or directory-specific repository rules.

Connectors, MCP tools, apps, plugins, and retrieval gateways require registration, owner, SBAC scope, OPA policy, audit, review cadence, and revocation path.

Knowledge automation may validate, flag, summarize, queue, and propose; it may not promote unreviewed canonical documents or overwrite approved sources without human approval.

All source projection, retrieval, indexing, AI use, PR/MR, and evidence updates must be AVCI-compliant.

Fail closed: when source authority, classification, SBAC, OPA, freshness, evidence, or connector validation is missing, protected retrieval and protected action must stop.

## 6.6 Target Knowledge Control Plane Architecture
| Layer | Primary Function | Mandatory Controls |
| --- | --- | --- |
| Official Source Layer | Stores approved records and source-of-truth artifacts. | Document register, Git commit history, OpenKM/DMS record, approval, retention, classification, evidence hash. |
| Working Knowledge Layer | Supports human authoring and curated knowledge projection in Obsidian. | Git-backed vault, PR/MR review, front matter, backlinks, source hash, metadata validation, no secrets. |
| Retrieval Layer | Provides LLM Wiki / Knowledge API / semantic retrieval for approved users and AI assistants. | SBAC, OPA, classification, freshness, citation, source lineage, quarantine, prompt redaction. |
| Code Intelligence Layer | Provides GitNexus read-only code maps, impact analysis, affected tests, and evidence summaries. | Commit-bound indexing, no mutation, no secrets, freshness manifest, reviewer correlation. |
| AI Assistant Adapter Layer | Feeds governed context to Codex, ChatGPT, Claude Code, IDE assistants, Hermes, and agents. | CLAUDE.md/AGENTS.md alignment, tool allowlist, retrieval scope, no production credentials, audit. |
| DevSecOps Evidence Layer | Captures source, change, test, scan, policy, promotion, and runtime evidence. | CI/CD, CODEOWNERS, PR/MR evidence, SBOM/provenance, audit, rollback/forward-fix path. |

## 6.7 Obsidian Vault Governance

Obsidian vaults used for AIRA must be Git-managed or otherwise version-controlled under approved workspace governance.

Every canonical or curated page must include document ID, title, version, status, owner, classification, source reference, source hash, last reviewed date, approval state, and related documents.

Obsidian may contain curated projections of standards, ADRs, runbooks, prompt standards, diagrams, evidence summaries, and operational playbooks.

Obsidian must not become a raw full-code mirror, unrestricted log dump, uncontrolled prompt transcript repository, secret store, or Restricted data staging area.

Vault plugins, synchronization method, connector access, and publish/sync settings require approval, owner, data classification review, and rollback plan.

Vault changes that affect canonical guidance must be made through branch/PR review, not direct uncontrolled edits.

## 6.8 LLM Wiki, Retrieval Gateway, and Index Governance
| Control | Mandatory Rule |
| --- | --- |
| Retrieval eligibility | A source may be indexed only after classification, owner, source hash, retention, review state, and retrieval scope are recorded. |
| Freshness | Retrieval results must expose indexed timestamp, source version, source hash, stale/valid status, and source authority tier. |
| Citations | AI answers derived from indexed knowledge must cite or reference source records and must not claim authority without source evidence. |
| Restricted data | Restricted, secret-bearing, regulated, or customer-sensitive content requires explicit retrieval policy and may be excluded, redacted, or routed only to approved models and users. |
| Quarantine | Conflicting, stale, unapproved, duplicate, or sensitive artifacts must be quarantined and routed to a review queue. |
| Rebuildability | Indexes must be reproducible from approved sources and cannot become the only copy of a knowledge artifact. |
| Audit | Retrieval decisions, denied retrievals, context assembly, model route, and evidence references must be logged safely. |

## 6.9 GitHub/GitLab Repository Governance Integration

Repositories remain the golden source for source code, tests, CI/CD, API contracts, AsyncAPI, schemas, OPA policies, Flyway migrations, IaC, devcontainers, AGENTS.md, CLAUDE.md, evidence manifests, and generated adapters. The knowledge control plane must link to exact repository, branch, commit, path, and artifact digest. It must not duplicate repository authority inside Obsidian or LLM Wiki.

Required repository controls: branch protection, CODEOWNERS, required status checks, signed or controlled commits where applicable, PR/MR templates, AI-use declaration, and evidence manifests.

Required knowledge controls: exact Git reference, source hash, artifact type, owner, classification, source tier, and evidence path.

Forbidden patterns: copying full repositories into Obsidian, storing secrets in vaults, using AI-generated repository rules without review, or allowing AI to weaken CODEOWNERS or CI/CD gates.

## 6.10 Codex, AGENTS.md, Claude Code, and Multi-Assistant Adapter Governance
| Assistant / Adapter | Allowed Use | Mandatory Boundary |
| --- | --- | --- |
| Codex | Repository-aware code analysis, test generation, refactoring proposals, candidate code, documentation drafts, PR suggestions. | Must read AGENTS.md/project instructions, remain branch-bound, follow repository rules, produce evidence, and avoid production credentials or direct production mutation. |
| AGENTS.md | Tool-specific AI coding instruction adapter. | Generated from or aligned to CLAUDE.md; may add stricter repository-specific rules; must not weaken AIRA controls. |
| Claude Code | Codebase analysis, refactoring proposals, test generation, explanation, documentation, and controlled command proposals. | Must follow CLAUDE.md hierarchy and approved settings; tool execution must remain controlled and auditable. |
| ChatGPT Project | Architecture review, document synthesis, requirements analysis, controlled troubleshooting, and source-aware advisory work. | Must use approved project sources/connectors, source citations, classification checks, and no Restricted data copy-paste outside approved channels. |
| IDE Assistants | Developer productivity assistance within local repositories. | Must use generated rules and must not bypass local checks, CI/CD, secrets policy, CODEOWNERS, or PR/MR evidence. |
| System Builder Agents | Controlled intake, impact analysis, candidate artifact generation, evidence pack preparation, review queue updates. | No self-approval, no silent mutation, no direct production tools, no unregistered agents, no direct model provider calls. |

## 6.11 Metadata, Front Matter, and Source Register Standard
| Required Field | Purpose |
| --- | --- |
| document_id | Stable AIRA identifier. |
| canonical_filename | Official file name or current projection name. |
| title | Human-readable document title. |
| version | Approved or candidate version. |
| status | Draft, review, approved, superseded, deprecated, retired, or revoked. |
| classification | Public, Internal, Confidential, Restricted, or project-specific handling classification. |
| owner | Accountable human or role. |
| source_tier | Tier 0, Tier 1, Tier 2, Tier 3, or Tier 4. |
| source_ref | Git commit, OpenKM/DMS record, source pack, PR/MR, ticket, ADR/TDL, or evidence path. |
| source_hash | Hash of authoritative source or projection artifact. |
| retrieval_eligibility | Allowed, allowed with restrictions, quarantined, excluded, or expired. |
| retention_rule | Retention and disposal requirement. |
| related_documents | Parent and companion AIRA standards. |
| evidence_ref | Evidence record proving review, validation, or promotion. |

## 6.12 Knowledge Change Workflow

Intake: capture request, source, owner, classification, affected document/repository, and intended outcome.

Authority check: identify Tier-0 source and determine whether the change is a projection, correction, canonical update, or new artifact.

Impact analysis: check affected cross-references, companion standards, prompts, AGENTS.md/CLAUDE.md adapters, CI/CD rules, System Builder retrieval, and LLM Wiki indexes.

Draft: create candidate change in branch or controlled draft state.

Validation: run metadata checks, link checks, duplicate detection, terminology checks, classification scan, secret scan, and source-reference validation.

Review: maker-checker review by owner, architecture, security, DevSecOps, knowledge governance, or CAB/ARB as required.

Promotion: merge or publish only after evidence pack is complete.

Projection and indexing: update Obsidian, LLM Wiki, retrieval manifests, and related source registers.

Observation: monitor retrieval accuracy, stale source warnings, broken links, citation quality, and user feedback.

Improvement: route gaps to backlog, review queue, ADR/TDL, or source reconciliation register.

## 6.13 Evidence Requirements
| Evidence Type | Minimum Evidence Required |
| --- | --- |
| Source authority evidence | Source tier, owner, source system, source path, source hash, version, approval status, and supersedes relationship. |
| Projection evidence | Obsidian path, projection hash, projection date, reviewer, affected links, and metadata validation result. |
| Retrieval evidence | Index ID, indexed timestamp, source hash, allowed audience, classification, retrieval decision, and citation test. |
| AI assistant evidence | Assistant/tool used, prompt source, classification check, model route, tool scope, output classification, human reviewer, and PR/MR reference. |
| Repository evidence | Repository, branch, commit, PR/MR, CODEOWNERS, required checks, evidence manifest, GitNexus report, and CI/CD result. |
| Security evidence | Secrets scan, classification scan, access review, connector review, tool permission review, and retention rule. |
| Rollback evidence | Previous version, rollback path, re-index rollback, cache invalidation, and notification path. |

## 6.14 Security, Connector, MCP, and Plugin Controls

Every connector, app, plugin, MCP server, retrieval gateway, and AI tool integration must have an owner, purpose, classification ceiling, SBAC scope, OPA policy, audit path, retention rule, and revocation procedure.

Personal accounts, unmanaged plugins, uncontrolled browser extensions, unapproved local MCP servers, and direct production credentials are prohibited for AIRA work.

Connectors must fail closed when classification, identity, policy, audit, or source eligibility cannot be verified.

Connector output must never include raw secrets, raw tokens, raw Restricted documents, raw customer records, or unredacted production data unless explicitly approved and controlled.

Tool permissions must be reviewed at onboarding, quarterly, after role change, after incident, and before production-impacting workflow adoption.

## 6.15 Auto-Heal, Auto-Learn, and Auto-Improve Governance

The knowledge control plane may support Auto-Heal, Auto-Learn, and Auto-Improve by retrieving evidence, identifying recurring gaps, drafting candidate fixes, updating review queues, suggesting prompt improvements, or generating candidate knowledge artifacts. It must not automatically promote canonical documents, merge code, change policies, modify runtime configuration, or update production indexes without approval.
| Loop | Allowed Knowledge-Control-Plane Behavior | Required Gate |
| --- | --- | --- |
| Auto-Heal | Retrieve incident evidence, related standards, code maps, runbooks, and candidate remediation notes. | Human review, ticket, tests, security review, PR/MR evidence, and rollback plan. |
| Auto-Learn | Identify recurring gaps, stale knowledge, inconsistent terminology, missing evidence, and failed retrieval cases. | Knowledge steward review, source citation, backlog item, and controlled publication. |
| Auto-Improve | Draft standard updates, adapter improvements, metadata fixes, link repairs, and retrieval enhancements. | Maker-checker review, CI checks, classification scan, and source register update. |

## 6.16 Validation Checklist
| Checklist Item | Pass Condition |
| --- | --- |
| Source tier identified | Every referenced artifact has source tier, owner, classification, status, and source reference. |
| Metadata complete | Required front matter or register fields are present. |
| Classification safe | No prohibited Restricted data, secrets, tokens, raw PII, or production data is projected or indexed. |
| Repository-linked | Code-related knowledge references exact repository, branch, commit, and path. |
| Adapter aligned | AGENTS.md, IDE rules, and tool instructions do not weaken CLAUDE.md or AIRA standards. |
| Retrieval fresh | Index and LLM Wiki records match current approved source hash or are marked stale/quarantined. |
| Evidence complete | PR/MR, CI, review, source hash, validation, and approval evidence are attached. |
| Rollback ready | Previous source, projection, index, and adapter versions can be restored or invalidated. |
| Human approval captured | Canonical or production-impacting changes have named maker, checker, and approver. |

## 6.17 Anti-Patterns

Copying entire repositories or production logs into Obsidian or AI project sources.

Treating AI-generated summaries as authoritative without source citation and human review.

Using one AI assistant rule file that conflicts with or weakens CLAUDE.md, AGENTS.md, CODEOWNERS, or CI policies.

Indexing confidential or Restricted content without classification, redaction, SBAC, retention, and retrieval controls.

Allowing Codex, Claude Code, or System Builder to approve, merge, deploy, change secrets, alter production configuration, or mutate canonical sources directly.

Using stale LLM Wiki or embedding results when authoritative sources have changed.

Ignoring duplicate-numbering conflicts, old versions, or superseded documents.

Publishing unreviewed Obsidian notes as approved AIRA standards.

Letting GitNexus, LLM Wiki, or embeddings become source of truth.

## 6.18 Acceptance Criteria

A source-tier register exists and distinguishes Tier-0 authority, Obsidian projections, LLM Wiki, indexes, caches, and AI outputs.

Obsidian vault governance includes Git control, metadata validation, classification scan, and review workflow.

LLM Wiki and retrieval gateway enforce classification, SBAC, freshness, source hash, and citation requirements.

Codex, Claude Code, and IDE assistants use AGENTS.md / CLAUDE.md-aligned rules and cannot bypass CI/CD, CODEOWNERS, or human approval.

GitNexus outputs are derivative, read-only, commit-bound, and linked to PR/MR evidence only.

Knowledge automation can propose and validate, but cannot promote unreviewed canonical sources.

All changes produce AVCI evidence and a rollback or re-index invalidation path.

# 7. Simplification Recommendations
| Audience | Simplified Message |
| --- | --- |
| Software Developers | Code lives in Git. Rules live in CLAUDE.md/AGENTS.md. Knowledge summaries may live in Obsidian. Retrieval comes from approved sources. AI can help, but PR/MR evidence and human review decide. |
| Knowledge Stewards | Never publish or index without owner, source, version, classification, freshness, and evidence. Quarantine conflicts and stale sources. |
| DevSecOps | Treat knowledge projection and adapter generation as CI-validated artifacts. Scan, validate, and evidence them like code. |
| Security | Protect source access, connector scope, secrets, classification, retrieval, and model routes. Fail closed if eligibility is unknown. |
| AI Governance | AI outputs are draft or advisory unless promoted through source governance. Agents may retrieve and propose, not self-approve or mutate. |

# 8. Automation Recommendations
| Automation Capability | Purpose | Control |
| --- | --- | --- |
| Document inventory scanner | Detect missing metadata, duplicate IDs, superseded versions, stale links, and source-tier gaps. | Runs in CI or scheduled knowledge pipeline; outputs review queue item. |
| Metadata/front matter validator | Ensure required fields exist before Obsidian projection or indexing. | Blocks publication when required fields are missing. |
| Classification and secrets scanner | Prevent leakage into Obsidian, LLM Wiki, prompts, indexes, and AI project sources. | Fail closed for secrets and Restricted content without approved route. |
| Cross-reference validator | Check AIRA document references, related standards, source hashes, and broken links. | Creates reconciliation items. |
| Adapter generator | Generate AGENTS.md, IDE rules, and CI policy bundles from CLAUDE.md and AIRA standards. | No-weaker-than-canonical rule. |
| Retrieval freshness manifest | Track source hash, projection hash, index hash, indexed date, stale state, and retrieval eligibility. | Blocks stale authoritative retrieval for protected decisions. |
| GitNexus evidence projector | Create read-only code maps and impact summaries linked to commit SHA and PR/MR. | No source mutation; no approval authority. |
| Review queue agent | Triage gaps, assign owners, and recommend next document or source correction. | Human approves queue and priority. |
| Evidence completeness checker | Validate PR/MR, CI/CD, source, retrieval, and knowledge-promotion evidence. | Blocks promotion when AVCI evidence is incomplete. |

# 9. Review Queue Control Register
| Seq | File / Standard | Recommended Version | Review Status | Priority | Next Action |
| --- | --- | --- | --- | --- | --- |
| 1 | 01A Enterprise Architecture Principles | v1.2 | Completed | Done | No immediate action |
| 2 | 01 AVCI Engineering Standard | v3.2 | Completed | Done | No immediate action |
| 3 | 01B AVCI Evidence, Audit, Traceability, and Control Standard | v1.2 | Completed | Done | No immediate action |
| 4 | 02 Engineering Blueprint | v5.2 | Completed | Done | No immediate action |
| 5 | 03 Developer Guide | v4.2 | Completed | Done | No immediate action |
| 6 | 04 Technology Stack | v9.2 | Completed | Done | No immediate action |
| 7 | 05 AI-Native Information Nervous System | v4.2 | Completed | Done | No immediate action |
| 8 | 06 CLAUDE.md Reference | v3.2 | Completed | Done | No immediate action |
| 9 | 07 AI DevSecOps Skills Framework | v3.2 | Completed | Done | No immediate action |
| 10 | 08 Unit Testing Standard | v3.2 | Completed | Done | No immediate action |
| 11 | 08A AI-Assisted Unit Testing Maker-Checker Prompt Standard | v1.1 | Completed | Done | No immediate action |
| 12 | 09 Greenfield Environment Standard | v3.2 | Completed | Done | No immediate action |
| 13 | 10 MicroFunction Framework | v3.3 | Completed | Done | No immediate action |
| 14 | 10A MicroFunction Design and Development Guide | v2.3 | Completed | Done | No immediate action |
| 15 | 10B MicroFunction Framework Implementation Standard | v2.2 | Completed | Done | No immediate action |
| 16 | 10C MicroFunction Sequence Diagrams and Mermaid Reference | v2.2 | Completed | Done | No immediate action |
| 17 | 10D MicroFunction Standard Function Catalog and Assembly Templates | v2.2 | Completed | Done | No immediate action |
| 18 | 10E MicroFunction Backend Service Generation and Runtime Configuration Standard | v1.2 | Completed | Done | No immediate action |
| 19 | 11 AI-Native DevSecOps Standard | v3.2 | Completed | Done | No immediate action |
| 20 | 11A DevSecOps Governance and Evidence Control Standard | v1.2 | Completed | Done | No immediate action |
| 21 | 20 CI/CD Pipeline and Evidence Pack Implementation Guide | v1.2 | Completed | Done | No immediate action |
| 22 | 19 GitNexus Code Intelligence and Impact Analysis Standard | v1.3 | Completed | Done | No immediate action |
| 23 | 15 API and Integration Contract Standard | v2.2 | Completed | Done | No immediate action |
| 24 | 15A API Governance and Contract-First Implementation Guide | v1.2 | Completed | Done | No immediate action |
| 25 | 16 Database, Migration, and Data Engineering Standard | v2.2 | Completed | Done | No immediate action |
| 26 | 16A Flyway Initial Database Baseline and Migration Governance Guide | v1.3 | Completed | Done | No immediate action |
| 27 | 16B Database Governance Flyway-Only Generation Versioning and Migration Control Standard | v1.2 | Completed | Done | No immediate action |
| 28 | 17 Security, Identity, Secrets, and Access Control Standard | v2.2 | Completed | Done | No immediate action |
| 29 | 17A Security and Access Control Implementation Guide | v1.2 | Completed | Done | No immediate action |
| 30 | 18 Repository Bootstrap and Golden Source Implementation Guide | v1.2 | Completed | Done | No immediate action |
| 31 | 21A Governed Knowledge Control Plane - Obsidian, Codex, and GitHub Standard | v1.2 | Completed / This document | P1 | No immediate action |
| 32 | 25 Knowledge Access Architecture and Golden Source Standard | v1.3 recommended | Next for Review | P1 | Proceed |
| 33 | 26B Governed Knowledge Automation Pipeline Standard | v1.3 recommended | Pending after 25 | P1 | No immediate action |

# 10. Next Document Recommendation

The next recommended document to review is 25-AIRA_Knowledge_Access_Architecture_and_Golden_Source_Standard_v1.2_Aligned.docx.

Reason: 21A now defines the operational control plane connecting Obsidian, Codex, GitHub/GitLab, LLM Wiki, GitNexus, adapters, and AI assistants. Document 25 should be reviewed next because it defines the source-of-truth boundaries and access architecture across GitHub, GitNexus, Obsidian, LLM Wiki, and AI retrieval. Reviewing 25 before 26B prevents the automation pipeline from implementing the wrong source authority model.

Recommended confirmation prompt: Proceed with 25-AIRA_Knowledge_Access_Architecture_and_Golden_Source_Standard_v1.2_Aligned.docx. Review, correct, align with 21A v1.2, 18 v1.2, 05 v4.2, 06 v3.2, GitNexus, DevSecOps, CI/CD Evidence Pack, MicroFunction, API, database/Flyway, security, Obsidian, LLM Wiki, Codex, AGENTS.md, CLAUDE.md, and evidence governance, simplify, improve, update the review queue, and generate the revised Microsoft Word document as v1.3.

# 11. AVCI Compliance Summary
| AVCI Property | Evidence in This v1.2 Revision |
| --- | --- |
| Attributable | Defines owner, co-owners, source document, related AIRA baselines, source tiers, AI assistant roles, connector owners, and review responsibilities. |
| Verifiable | Defines metadata validation, source hashes, freshness manifests, PR/MR evidence, retrieval evidence, connector audit, CI validation, and acceptance criteria. |
| Classifiable | Requires classification for sources, projections, indexes, retrieval, prompts, connectors, AI outputs, and evidence artifacts. |
| Improvable | Creates review queue linkage, Auto-Heal/Learn/Improve candidate controls, stale-source detection, feedback routing, and quarterly review cadence. |

