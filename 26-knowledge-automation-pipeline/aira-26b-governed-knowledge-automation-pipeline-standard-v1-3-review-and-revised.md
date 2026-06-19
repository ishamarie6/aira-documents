---
title: "Governed Knowledge Automation Pipeline Standard"
doc_id: "AIRA-26B"
version: "v1.3"
status: "revised"
category: "Knowledge automation pipeline"
source_docx: "AIRA_26B_Governed_Knowledge_Automation_Pipeline_Standard_v1_3_Review_and_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 26-knowledge-automation-pipeline
  - revised
  - aira-26b
---



# Governed Knowledge Automation Pipeline Standard



AIRA

AI-Native Enterprise Platform

Governed Knowledge Automation
Pipeline Standard

Automated Source Projection | Freshness Manifest | Conflict Detection | Retrieval Eligibility | Human Review Gates | AVCI Always

Version v1.3 - Review and Revised Edition

Status: Draft for Architecture Review Board / CAB / Knowledge Governance Review

Classification: INTERNAL CONFIDENTIAL

Prepared for: AIRA Software Development, DevSecOps, Security, QA/SDET, Platform Engineering, Knowledge Governance, AI Governance, SRE, and Internal Audit Teams

Prepared by: AIRA Enterprise Architecture, Governance, AI DevSecOps, Security, and Documentation Review Board

Review Date: 2026-06-16

# 1. Document Control
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-026B |
| Document Title | AIRA Governed Knowledge Automation Pipeline Standard |
| Recommended Version | v1.3 - Golden Source, Freshness Manifest, Conflict Detection, and Retrieval Eligibility Update |
| Source Document Reviewed | 26B-AIRA_Governed_Knowledge_Automation_Pipeline_Standard_v1.2_Aligned.docx |
| Supersedes | 26B-AIRA_Governed_Knowledge_Automation_Pipeline_Standard_v1.2_Aligned.docx after ARB/CAB approval |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Architecture Review Board, CAB, Knowledge Governance, DevSecOps, Security, AI Governance, SRE, and Internal Audit Review |
| Document Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Knowledge Governance; DevSecOps Lead; Security Architecture; QA/SDET; Platform Engineering; AI Governance; SRE; Internal Audit |
| Primary Audience | Knowledge Stewards; Developers; DevSecOps; AI Assistant Owners; System Builder Team; Security Reviewers; QA/SDET; Architects; Internal Audit |
| Review Cadence | Quarterly; unscheduled after source pack update, Obsidian/LLM Wiki index change, AI connector change, GitNexus change, classification change, source conflict, data exposure event, or retrieval incident |
| Evidence Path | OpenKM Tier-0 / AIRA / Knowledge-Governance / Knowledge-Automation-Pipeline / v1.3/ |
| Governing Parents | 01A v1.2; 01 v3.2; 01B v1.2; 02 v5.2; 05 v4.2; 06 v3.2; 18 v1.2; 21A v1.2; 25 v1.3 |
| Related Controls | 19 v1.3 GitNexus; 20 v1.2 CI/CD Evidence; 11/11A DevSecOps; 17/17A Security; 42I Memory/RAG Integrity; MicroFunction baseline 10 v3.3 through 10E v1.2 |
| External Alignment Checked | OpenAI Codex AGENTS.md guidance; GitHub CODEOWNERS and protected branches; Obsidian security and sync references; Claude Code memory guidance; NIST SSDF; SLSA v1.2 |

# 2. Table of Contents Placeholder

Insert a Microsoft Word automatic Table of Contents here before final publication: References > Table of Contents > Automatic Table. Update fields after final pagination.

# 3. Change Summary
| Change Area | v1.3 Improvement |
| --- | --- |
| Golden Source enforcement | Reconfirms that Git/GitHub/GitLab, approved DOCX/PDF, OpenKM/DMS, databases, workflow histories, security/evidence stores, and audit records remain authoritative. Obsidian, LLM Wiki, LightRAG, GitNexus summaries, embeddings, and AI outputs remain derivative unless formally approved. |
| Automation boundary | Clarifies that automation may detect, extract, project, validate, summarize, index, quarantine, and report, but must not publish canonical standards, overwrite approved artifacts, approve its own work, or promote unreviewed knowledge. |
| Freshness and conflict controls | Adds mandatory freshness manifests, source hash validation, supersedence tracking, duplicate detection, conflict detection, stale artifact quarantine, and reviewer-controlled promotion. |
| Retrieval eligibility | Adds retrieval eligibility gates for approval status, version, source tier, classification, SBAC/OPA access, model-route eligibility, freshness, evidence reference, and conflict status. |
| AI assistant integration | Aligns ChatGPT, Codex, Claude Code, Hermes, System Builder, and AI agents with governed knowledge access through AGENTS.md/CLAUDE.md adapters, approved connectors, citations, audit, and no Restricted data leakage. |
| GitNexus and code summaries | Reinforces that code intelligence may be summarized into Obsidian and LLM Wiki, but full source code is not copied wholesale into Obsidian and GitNexus remains read-only derivative evidence. |
| Security and privacy | Strengthens secret scanning, malware scan for uploads, prompt injection checks, raw PII/log exclusion, credential exclusion, redaction, quarantine, retention, and disposal requirements. |
| Evidence and CI/CD | Adds pipeline evidence requirements for source hash, artifact hash, index batch, validation result, approval, rollback point, and retrieval regression test. |
| Reversibility | Requires rollback of index batches, quarantine of stale/conflicting artifacts, supersedence paths, safe re-index, and evidence of knowledge rebuild. |

# 4. Executive Review Summary

This review confirms that the v1.2 Governed Knowledge Automation Pipeline Standard is directionally correct and should be retained. It correctly prevents full source-code copying into Obsidian, recognizes Git/GitHub/GitLab and GitNexus as the code and code-intelligence authority layers, positions Obsidian as curated knowledge, and uses LLM Wiki/LightRAG as governed retrieval indexes.

Version v1.3 strengthens the document after the revised Golden Source, repository bootstrap, DevSecOps, GitNexus, MicroFunction, API, database, and security baselines. It makes freshness, conflict detection, retrieval eligibility, metadata validation, quarantine, approval, rollback, and evidence production mandatory controls instead of optional operational practices.

Recommended Review Verdict: promote v1.3 as the candidate knowledge automation pipeline standard after ARB, CAB, Knowledge Governance, DevSecOps, Security, AI Governance, and Internal Audit review. Use it as the control baseline for Obsidian projection, LLM Wiki refresh, GitNexus-derived summaries, System Builder retrieval, AI assistant context, and source-pack regeneration.

# 5. Source and Context Alignment Findings
| AIRA Source / Control Area | Required Alignment for 26B v1.3 |
| --- | --- |
| 05 Information Nervous System | Use source tiers, provenance, confidence, freshness, retrieval eligibility, and derivative-index governance as mandatory knowledge controls. |
| 21A Governed Knowledge Control Plane | Operationalize the connection among Git, GitNexus, Obsidian, LLM Wiki, Codex, AGENTS.md, CLAUDE.md, and evidence stores. |
| 25 Knowledge Access and Golden Source | Preserve the Golden Source rule: code in Git, code intelligence in GitNexus, governed knowledge in Obsidian, retrieval in LLM Wiki/LightRAG, AI access through approved connectors. |
| 18 Repository Bootstrap | Source artifacts, AGENTS.md, CLAUDE.md, CI manifests, evidence manifests, and repository metadata must originate from governed repositories. |
| 19 GitNexus | Use GitNexus as read-only, derivative, commit-bound code intelligence. It may create summaries and evidence, not source truth. |
| 20 CI/CD Evidence Pack | Run metadata validation, secret scan, classification check, link validation, source hash check, index-build evidence, and retrieval regression tests as pipeline evidence. |
| 17 Security | Enforce SBAC/OPA, classification, secrets hygiene, redaction, approved connectors, and no raw production data in AI retrieval. |
| 42I Memory/RAG Integrity | Prevent prompt injection, retrieval poisoning, stale context, false authority, and memory promotion without review. |
| System Builder | Allow analysis, recommendation, draft projection, and evidence assembly; block silent canonical publication or production-impacting mutation. |
| AVCI | Every knowledge artifact must be attributable, verifiable, classifiable, and improvable with owner, source hash, evidence, classification, review path, and supersedence path. |

# 6. Review and Gap Analysis
| Finding Type | Assessment | v1.3 Treatment |
| --- | --- | --- |
| Retain | The standard correctly prohibits copying the whole source-code repository into Obsidian. | Retained as a mandatory rule. |
| Retain | The standard correctly positions GitNexus, Obsidian, LLM Wiki/LightRAG, and AI assistants as different layers. | Retained and clarified by source-tier and authority boundaries. |
| Correct | Older references to v1.0/v1.1/v3.1 baselines must inherit the revised baselines already generated in this review queue. | Updated related-doc language to v1.2/v1.3/v3.2/v4.2 where applicable. |
| Strengthen | Freshness manifest, conflict detection, and retrieval eligibility were present but not operational enough. | Added mandatory control tables, pipeline gates, acceptance criteria, and evidence fields. |
| Strengthen | Security leakage, prompt injection, retrieval poisoning, stale context, and false authority risks require explicit controls. | Added quarantine, redaction, SBAC/OPA, source-tier, model-route, and guardrail requirements. |
| Simplify | The document needed a developer-friendly rule for what may and may not be automated. | Added allowed/prohibited automation table and standard operating workflow. |
| Add | System Builder and AI agents need a clear knowledge automation boundary. | Added System Builder and agent usage rules with fail-closed behavior. |
| Add | Review queue and source-pack regeneration must be tracked as evidence-producing workflows. | Added review queue controls and candidate next document recommendation. |

# 7. Revised Full AIRA Document

## 7.1 Purpose

The purpose of this standard is to define the governed automation model for projecting, validating, indexing, refreshing, quarantining, and retiring AIRA knowledge artifacts while preserving Golden Source authority, classification, provenance, freshness, traceability, security, and AVCI evidence.

This standard prevents knowledge drift, duplicate truth sources, Obsidian vault pollution, uncontrolled AI context, stale retrieval, secret leakage, false authority from generated summaries, and unreviewed AI-generated standards.

## 7.2 Scope
| In Scope | Out of Scope |
| --- | --- |
| Git-managed Obsidian vault projection, LLM Wiki/LightRAG index refresh, GitNexus-derived code intelligence summaries, evidence summaries, metadata manifests, classification validation, source freshness, conflict detection, and retrieval eligibility. | Copying full code repositories into Obsidian, using AI summaries as authority without review, indexing secrets or Restricted data without approved gateway controls, direct AI access to private systems without SBAC/OPA/audit, or bypassing ARB/CAB and source governance. |
| Source-pack regeneration support, document inventory, canonical register updates, duplicate detection, stale-source quarantine, and review queue automation. | Manual uncontrolled file dumps, unapproved personal notes, shadow repositories, uncontrolled sync tools, unmanaged external connectors, or AI memory outside AIRA governance. |
| System Builder knowledge retrieval, AI assistant context, AGENTS.md/CLAUDE.md-derived rules, and evidence-producing knowledge automation pipelines. | Silent production mutation, auto-publication of canonical standards, or automated approval of generated knowledge. |

## 7.3 Governing Principles
| Principle | Mandatory Meaning |
| --- | --- |
| Discipline first | Automation must follow Golden Source, classification, source-tier, human-review, CI/CD, evidence, and approval controls. |
| Automation second | Automation may scan, summarize, validate, index, quarantine, report, and propose. It must not approve or silently promote. |
| Intelligence third | AI may help discover, summarize, compare, and recommend. AI output is not authority until reviewed and promoted. |
| AVCI always | Every artifact, index batch, summary, and retrieval result must have owner, source, classification, verification evidence, and improvement path. |
| Fail-safe, not fail-open | Missing source hash, classification, owner, approval, source tier, freshness, or policy decision blocks retrieval or promotion. |

## 7.4 Golden Source and Derivative Layer Rules
| Layer | Authority | Allowed Automation | Prohibited Automation |
| --- | --- | --- | --- |
| Tier 0: Git, approved DOCX/PDF, OpenKM/DMS, databases, workflow/evidence/security/audit stores | Authoritative | Hash, inventory, classify, link, validate, project summaries, and create evidence manifests. | Overwrite, downgrade classification, or replace source with derivative summary. |
| Tier 1: Git-managed Obsidian projection | Authoritative only when linked to approved Tier 0 or directly approved | Curate standards, ADRs, runbooks, prompts, reviewed evidence, summary pages, and review queue notes. | Store uncontrolled full codebases, secrets, raw production data, raw logs, raw prompts with sensitive content, or unapproved standards as canonical. |
| Tier 2: LLM Wiki / curated retrieval artifacts | Derivative retrieval layer | Index approved/current/classification-eligible content with citations, source hashes, and retrieval tests. | Serve stale, superseded, conflicting, or unauthorized content as authoritative truth. |
| Tier 3: Embeddings, pgvector, LightRAG, graph, search indexes | Derivative only | Refresh through approved batch with manifests and rollback. | Become source of truth or retain content after source revocation. |
| Tier 4: AI outputs, chat drafts, generated summaries | Not authoritative | Create candidate drafts, recommendations, checklists, or review notes. | Publish or promote without named human approval and evidence. |

## 7.5 Knowledge Automation Pipeline

Inventory source artifact and identify source tier, owner, classification, version, source path, source hash, and approval status.

Check source authority, supersedence, duplicate candidates, conflict status, and canonical register alignment.

Run security validation: secret scan, PII/redaction check, malware scan for uploads, prompt-injection scan for retrieved content, and classification eligibility.

Generate controlled projection or summary using approved templates. Do not copy full code repositories or restricted payloads into Obsidian.

Validate metadata completeness, links, source hashes, evidence references, document IDs, review status, and retrieval eligibility.

Route projection to human reviewer, CODEOWNER, knowledge steward, architect, security, or DevSecOps approver depending on classification and artifact type.

Publish approved projection to Obsidian or approved document repository and record commit, approval, evidence, and rollback reference.

Refresh LLM Wiki/LightRAG/index batch only after approval, then run retrieval regression tests and record index batch evidence.

Quarantine stale, superseded, conflicting, or classification-ineligible artifacts and update the freshness manifest.

Record improvement backlog items, unresolved conflicts, and review queue updates.

## 7.6 Mandatory Metadata Schema
| Metadata Field | Purpose | Required For |
| --- | --- | --- |
| document_id | Stable artifact identity. | All AIRA knowledge artifacts. |
| title and version | Human-readable identity and version. | All artifacts. |
| status | Draft, review-ready, approved, current, superseded, deprecated, revoked, quarantined. | All artifacts. |
| owner and reviewer | Attribution and accountability. | All artifacts. |
| classification | Handling and retrieval control. | All artifacts. |
| source_tier and source_path | Source authority and lineage. | All projections, summaries, and indexes. |
| source_hash and artifact_hash | Tamper detection and reproducibility. | All generated/projection/index artifacts. |
| approved_by and approval_date | Promotion evidence. | Approved/current artifacts. |
| supersedes and superseded_by | Lifecycle and drift prevention. | Versioned artifacts. |
| retrieval_eligible | Whether retrieval is permitted. | LLM Wiki/indexed artifacts. |
| model_route_allowed | Approved model route or gateway condition. | AI-consumable artifacts. |
| evidence_ref | Evidence pack pointer. | All promoted artifacts. |
| conflict_status | None, suspected, confirmed, waived, reconciled, quarantined. | All retrieval-eligible artifacts. |
| freshness_status | Current, stale, expired, superseded, unknown. | All indexed artifacts. |
| review_queue_ref | Links to document review and reconciliation queue. | Source-pack and standards artifacts. |

## 7.7 Freshness Manifest and Conflict Detection

A freshness manifest is mandatory for every source-pack refresh, Obsidian projection run, LLM Wiki refresh, GitNexus summary batch, and System Builder knowledge import. The manifest must be version-controlled and linked to CI/CD evidence.
| Control | Required Behavior | Fail-Closed Condition |
| --- | --- | --- |
| Source hash check | Compare current source hash against registered source hash. | Hash mismatch without approved source update blocks retrieval and promotion. |
| Version check | Compare version, supersedes, superseded_by, and current status. | Superseded or unknown version is quarantined. |
| Duplicate detection | Detect duplicate document ID, title, filename, and semantic overlap. | Duplicate authority is escalated to review queue. |
| Conflict detection | Detect conflicting requirements, terms, versions, controls, or standards. | Conflict is surfaced; AI must not silently pick convenient source. |
| Classification check | Confirm artifact and user/agent retrieval eligibility. | Classification mismatch blocks retrieval. |
| Review cadence check | Confirm review date has not expired. | Expired high-risk artifact becomes restricted or quarantined until reviewed. |
| Retrieval regression test | Test known queries against approved sources and citation expectations. | Failed regression blocks index promotion. |

## 7.8 Retrieval Eligibility Rules

An artifact is retrieval-eligible only when all of the following conditions pass. If any mandatory condition fails, the retrieval gateway, LLM Wiki, or AI assistant adapter must fail closed.
| Eligibility Gate | Pass Condition |
| --- | --- |
| Authority | Artifact traces to Tier 0 or approved Tier 1 source. |
| Approval | Artifact is approved/current or explicitly marked review-ready for limited use. |
| Classification | User/agent has clearance and SBAC skill for the artifact classification. |
| Freshness | Artifact is current and not superseded, revoked, stale, or quarantined. |
| Conflict | No unresolved material conflict exists, or conflict is surfaced with governing-source recommendation. |
| Evidence | Artifact has source hash, evidence reference, owner, approval state, and retention rule. |
| Model route | Approved model route or private gateway exists for the classification. |
| Purpose | Retrieval purpose is related to approved task, ticket, PR/MR, incident, review, or authorized query. |
| Audit | Query, sources, model/tool route, returned artifacts, and output reference are auditable. |

## 7.9 Obsidian Projection Rules

Obsidian may store canonical AIRA standards, ADRs, TDLs, runbooks, prompts, diagrams, review queues, and reviewed evidence summaries only when they are approved or linked to authoritative sources.

Obsidian must not become a duplicate full source-code repository, secret store, raw log archive, production-data dump, or uncontrolled AI output vault.

Markdown projections must retain source document ID, version, owner, classification, source path, source hash, approval status, review date, supersedence, evidence reference, and retrieval eligibility.

Generated summaries must be clearly labeled as derivative and must reference the source artifact and evidence path.

Obsidian publication requires human review for architecture, security, policy, Restricted, production, AI-agent, or database-impacting knowledge.

## 7.10 LLM Wiki / LightRAG Refresh Rules
| Refresh Control | Mandatory Requirement |
| --- | --- |
| Pre-index validation | Only approved/current/review-eligible and classification-permitted artifacts enter the index batch. |
| Chunk lineage | Every chunk must retain source_id, source_path, source_hash, artifact_hash, chunk_id, classification, owner, version, and evidence_ref. |
| Prompt-injection defense | Text from external or user-supplied sources must be scanned, tagged, and isolated from system instructions. |
| Index batch evidence | Each batch records batch_id, input manifest, excluded artifacts, validation result, index time, reviewer, and rollback point. |
| Retrieval test | Known-answer and denied-access tests must pass before the new index becomes default. |
| Rollback | Prior index version remains available until the new index is accepted. |
| Audit | Queries and retrieval results are logged with safe redaction and classification labels. |

## 7.11 GitNexus-Derived Knowledge Rules

GitNexus output may be used as code intelligence, impact analysis, code map, affected-test guidance, architecture drift signal, and PR/MR evidence only when bound to a specific repository, branch, commit, index version, source hash, and evidence record.

GitNexus must remain read-only and derivative.

GitNexus must not commit, merge, approve, deploy, mutate production, edit source code, modify CI, or replace tests/scans/human review.

Only summaries, code maps, dependency graphs, affected-test recommendations, and evidence references may be projected into Obsidian.

Full source-code copies, secrets, raw credentials, environment files, private keys, tokens, and Restricted content must not be copied into Obsidian or AI prompts.

GitNexus-derived summaries must include limitations and must be corroborated by CI, tests, scanners, and human review.

## 7.12 System Builder and AI Assistant Rules
| Actor | Allowed | Prohibited |
| --- | --- | --- |
| System Builder | Classify request, retrieve approved context, detect conflicts, generate candidate summaries, propose updates, create review queue items, prepare PR/MR-ready artifacts. | Silently publish standards, approve its own output, bypass retrieval controls, mutate production, bypass CAB/ARB, or promote unreviewed knowledge. |
| Codex / Claude Code / Hermes | Use AGENTS.md/CLAUDE.md-adapter guidance, approved repository context, read-only GitNexus summaries, and classified retrieval outputs. | Use personal accounts for AIRA Restricted data, bypass repository rules, retrieve unapproved sources, or treat AI output as authority. |
| AI agents | Retrieve only through approved knowledge API/MCP connector with SBAC/OPA, classification, route, guardrail, and audit controls. | Use direct credentials, unapproved tools, direct Git/CI/database/Kubernetes production access, or unmanaged memory. |
| Human reviewers | Approve, reject, quarantine, supersede, or escalate knowledge artifacts and automation results. | Rubber-stamp generated summaries without source/evidence review. |

## 7.13 Security, Classification, and Retention

All automation must run secret scanning, classification validation, retention tagging, and redaction checks before projection or indexing.

Raw secrets, tokens, credentials, private keys, production customer data, raw KYC documents, raw logs with sensitive fields, raw embeddings containing Restricted content, and raw prompts with sensitive content must not be indexed or projected unless explicitly approved through secure private controls.

Restricted or Confidential data must use approved model routes, private gateways, guardrails, audit, and retrieval policy. If route validation fails, retrieval is blocked.

Malware scanning is required for file uploads before knowledge extraction.

Retention and disposal rules must be inherited from the source artifact and evidence store.

Quarantined artifacts must be excluded from default retrieval and explicitly visible in the review queue.

## 7.14 CI/CD and Evidence Requirements
| Evidence Item | Required Fields |
| --- | --- |
| Source inventory evidence | document_id, title, version, source_tier, source_path, source_hash, owner, classification, status. |
| Projection evidence | projection_id, template_version, generated_by, source_hash, artifact_hash, reviewer, approval status, evidence_ref. |
| Security validation evidence | secret scan, classification result, redaction status, upload malware scan, prompt-injection scan, policy result. |
| Index batch evidence | batch_id, included/excluded artifacts, index version, source manifest hash, retrieval tests, rollback point, reviewer. |
| Conflict evidence | conflict_id, affected documents, severity, governing-source recommendation, owner, status, resolution path. |
| Retrieval audit evidence | actor, agent, query purpose, retrieved artifacts, classification, model route, response reference, citations, timestamp. |
| Improvement evidence | feedback item, stale source, recurring issue, backlog link, proposed fix, reviewer, closure status. |

## 7.15 Runtime Toggles and Non-Disableable Controls

To manage performance and operational load, diagnostic verbosity, retrieval sampling, non-critical debug logging, and dashboard refresh intervals may be adjusted at runtime through approved configuration. However, the following controls must not be disabled: audit events, security events, policy decisions, classification labels, source hash checks, retrieval eligibility decisions, index-batch evidence, quarantine rules, and critical error evidence.

## 7.16 Auto-Heal, Auto-Learn, and Auto-Improve Integration

Knowledge automation may participate in Auto-Heal, Auto-Learn, and Auto-Improve as a candidate loop only. It may detect stale documents, broken links, conflicting terms, outdated references, missing metadata, failed retrieval tests, unsafe summaries, weak evidence, duplicate sources, or incorrect citations. It may retrieve evidence and propose fixes, but human review is required before canonical publication, index promotion, or baseline update.
| Loop | Allowed Output | Approval Gate |
| --- | --- | --- |
| Auto-Heal | Candidate correction for broken link, stale index, failed metadata validation, or unsafe retrieval routing. | Knowledge Steward + Security/DevSecOps where applicable. |
| Auto-Learn | Pattern summary for recurring documentation drift, duplicate numbering, missing evidence, or terminology inconsistency. | Architecture / Knowledge Governance review. |
| Auto-Improve | Candidate updates to templates, manifests, metadata schema, review queue, or index validation rules. | ARB/CAB or delegated governance approval depending on risk. |

## 7.17 Acceptance Criteria

All knowledge artifacts have document_id, owner, classification, source tier, source path, source hash, status, review date, and evidence reference.

No full source-code repository, secrets, raw production data, or uncontrolled logs are copied into Obsidian.

All projections and summaries are clearly marked as canonical or derivative.

Freshness manifests are generated and stored for every source-pack, Obsidian, GitNexus, or LLM Wiki refresh.

Duplicate and conflict detection runs and unresolved conflicts are added to the review queue.

LLM Wiki / LightRAG retrieval excludes stale, superseded, revoked, quarantined, or unauthorized content.

Retrieval regression tests pass before new indexes become default.

AI assistants consume knowledge through approved connectors, AGENTS.md/CLAUDE.md rules, SBAC/OPA, model route controls, and audit.

Rollback exists for every index batch and projection release.

AVCI evidence is complete and reviewable.

# 8. Automation Recommendations
| Automation Area | Recommended Control |
| --- | --- |
| Document inventory | Maintain a machine-readable manifest of every source document, version, status, owner, source path, source hash, classification, and pack placement. |
| Canonical register | Use a canonical register to identify governing source, superseded source, duplicate numbering, review status, and next action. |
| Cross-reference validation | Check that every referenced AIRA document exists, version is current, and relationship is valid. |
| Version tracking | Detect stale version references such as older 01A/AVCI/Technology Stack/MicroFunction/Flyway references. |
| Duplicate detection | Run filename, document ID, title, and semantic duplicate checks. |
| Terminology consistency | Validate terms such as AVCI, System Builder, MicroFunction, Golden Source, LLM Wiki, GitNexus, SBAC, OPA, LiteLLM, and NeMo Guardrails. |
| Conflict detection | Flag conflicts by severity and route to review queue and 00D reconciliation tracking. |
| Missing-section detection | Validate required document control, purpose, scope, governance, evidence, security, observability, rollback, acceptance, and AVCI sections. |
| Evidence checklist validation | Check that every artifact has owner, source, classification, verification path, evidence path, and improvement path. |
| Agent-assisted review queue | Allow AI to propose review priorities but require human confirmation before publication. |
| Obsidian/Git tracking | Store projection changes through Git commits with source hash, reviewer, and evidence reference. |
| Optional scripts/manifests | Implement doc_inventory.yaml, canonical_register.csv, freshness_manifest.json, retrieval_eligibility.json, index_batch_manifest.json, and conflict_register.csv. |

# 9. Review Queue Control Register
| Sequence | File Name | Pack | Current Version | Recommended Version | Review Status | Priority | Dependency | Action Required | Next Step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 31 | 21A-AIRA_Governed_Knowledge_Control_Plane_Obsidian_Codex_GitHub_Standard_v1.1_Aligned.docx | Pack 05 | v1.1 | v1.2 | Completed / Revised | P1 | Knowledge control plane | Completed | Use as operational control-plane baseline. |
| 32 | 25-AIRA_Knowledge_Access_Architecture_and_Golden_Source_Standard_v1.2_Aligned.docx | Pack 06 | v1.2 | v1.3 | Completed / Revised | P1 | Golden Source boundaries | Completed | Use as Golden Source and retrieval access baseline. |
| 33 | 26B-AIRA_Governed_Knowledge_Automation_Pipeline_Standard_v1.2_Aligned.docx | Pack 07 | v1.2 | v1.3 | Completed / Revised | P1 | 21A v1.2 and 25 v1.3 | This review completed | Promote as candidate after ARB/CAB and Knowledge Governance review. |
| 34 | 13-AIRA_Obsidian_and_LLM_Wiki_Knowledge_Governance_Standard_v2.1_Aligned.docx | Pack 03 | v2.1 | v2.2 | Next for Review | P1 | 05 v4.2, 21A v1.2, 25 v1.3, 26B v1.3 | Review and align | Proceed next to close the Obsidian/LLM Wiki governance layer. |
| 35 | 31A-AIRA_Observability_Telemetry_and_Evidence_Correlation_Standard_v1.1_System_Builder_Update.docx | Pack 07 | v1.1 | v1.2 | Pending | P1 | DevSecOps, MicroFunction, knowledge, security | Review later | Review after 13 or when shifting to observability phase. |

# 10. Next Document Recommendation

The next document should be 13-AIRA_Obsidian_and_LLM_Wiki_Knowledge_Governance_Standard_v2.1_Aligned.docx. Rationale: 21A, 25, and 26B now establish the control plane, Golden Source boundaries, and automation pipeline. Document 13 should be reviewed next because it governs the Obsidian and LLM Wiki operational knowledge layer that the automation pipeline projects into and the AI retrieval layer depends on. Reviewing 13 now closes the knowledge-governance foundation before moving to observability, operations, change/release, Dynamic Workspace, System Builder, and AI Agent documents.

# 11. AVCI Compliance Summary
| AVCI Property | Evidence in v1.3 |
| --- | --- |
| Attributable | Defines owner, co-owners, source document, source tier, source path, source hash, reviewer, approver, index batch owner, and evidence path. |
| Verifiable | Requires metadata validation, source hash, artifact hash, secret scan, classification check, freshness manifest, retrieval regression test, index batch evidence, and rollback proof. |
| Classifiable | Requires classification label, SBAC/OPA retrieval eligibility, model-route check, redaction, retention, quarantine, and restricted-content exclusion. |
| Improvable | Defines stale detection, conflict detection, duplicate detection, review queue, feedback loop, supersedence, rollback, and Auto-Heal / Auto-Learn / Auto-Improve candidate paths. |

