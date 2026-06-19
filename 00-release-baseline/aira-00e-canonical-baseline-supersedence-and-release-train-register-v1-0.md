---
title: "Canonical Baseline Supersedence and Release Train Register"
doc_id: "AIRA-00E"
version: "v1.0"
status: "final"
category: "Release baseline"
source_docx: "AIRA_00E_Canonical_Baseline_Supersedence_and_Release_Train_Register_v1.0.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 00-release-baseline
  - final
  - aira-00e
---



# Canonical Baseline Supersedence and Release Train Register



AIRA
AI-Native Enterprise Platform

Canonical Baseline, Supersedence, and Release Train Register

AIRA-DOC-00E | Version v1.0

Source Authority | Baseline Control | Supersedence | Release Train | AVCI Reconciliation
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-00E |
| Document Title | AIRA Canonical Baseline, Supersedence, and Release Train Register |
| Version | v1.0 - Initial Executable Governance Register Standard |
| Status | Draft for Architecture Review Board / CAB / Engineering Team Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; DevSecOps; Security Architecture; QA/SDET; Platform Engineering; AI Governance; Knowledge Governance; Internal Audit |
| Prepared For | AIRA Architecture, DevSecOps, System Builder, Dynamic Workspace, MicroFunction, Security, QA, SRE, DBA, AI Engineering, and Internal Audit Teams |
| Primary Parents | 00A-00D Registers; 01A; 01; 01B; 02; 11; 11A; 20; 62; 66; 68 |
| Review Cadence | At every release train; monthly during active regeneration; quarterly after stabilization; unscheduled on material source-pack or authority conflict |

Mandatory Practice Statement

AIRA must not operate from memory, informal filenames, duplicate drafts, generated summaries, or untracked projections. Every active document, candidate artifact, superseded source, exception, conflict, waiver, and release-train decision must be registered, owned, classified, evidence-linked, and traceable through an AVCI-compliant baseline control path.

# Static Table of Contents

1. Executive Summary

2. Purpose, Scope, and Authority

3. Canonical Baseline Operating Model

4. Baseline State Taxonomy

5. Required Register Fields

6. Supersedence and De-Duplication Rules

7. Release Train Governance

8. Initial AIRA Release Train Baseline

9. Conflict and AVCI Reconciliation Workflow

10. Evidence and Publication Package

11. Automation and Machine-Readable Register Controls

12. RACI and Separation of Duties

13. Acceptance Criteria

14. Open Reconciliation Items

15. AVCI Compliance Summary

# 1. Executive Summary

AIRA has progressed from foundational standards into an integrated engineering ecosystem covering enterprise architecture, AVCI, MicroFunction runtime, DevSecOps, CI/CD evidence packs, Dynamic Workspace, AI governance, policy-as-code, production readiness, resilience testing, evidence manifests, API/event governance, threat modeling, AI model-route certification, data governance, and golden-path reference implementations.

This document formalizes the governing register standard that prevents architecture drift as the document set grows. It defines how AIRA identifies the active baseline, controls supersedence, groups related documents into release trains, handles duplicates and stale references, and preserves source authority across Git, OpenKM, Obsidian, LLM Wiki, CI/CD evidence, and generated Word/PDF artifacts.

The operating rule is simple: a document is not canonical merely because it exists. It becomes an active candidate or active canonical source only when it has document control, owner, classification, version, source lineage, review state, rendered QA evidence, supersedence decision, and approval route.

# 2. Purpose, Scope, and Authority

## 2.1 Purpose

Define the AIRA canonical register model for active, candidate, superseded, duplicate, retired, and revoked documents.

Prevent stale references, duplicate numbering, conflicting document authority, uncontrolled source-pack drift, and undocumented regeneration decisions.

Establish release train governance for grouped AIRA changes across foundation, MicroFunction, DevSecOps, Dynamic Workspace, AI governance, evidence, and operational readiness documents.

Create a machine-readable register structure that can be validated by CI/CD, System Builder, GitNexus, Obsidian projection, LLM Wiki freshness checks, and audit workflows.

## 2.2 Scope
| In Scope | Out of Scope |
| --- | --- |
| All AIRA standards, guides, runbooks, registers, manifests, source packs, evidence packs, images, rendered PDFs, generated DOCX files, diagrams, schemas, and release-train records. | Informal notes, private scratchpads, unreviewed AI drafts, unmanaged local copies, screenshots without evidence binding, and generated summaries that are not registered. |
| Version state, supersedence, duplicate detection, canonical source selection, approval route, reconciliation item tracking, publication rules, and evidence linkage. | Silent renumbering, undocumented replacement of authoritative files, deleting lineage, treating Obsidian/LLM Wiki as source authority, or using AI output as approval authority. |

## 2.3 Authority

AIRA-DOC-00E is a register-control standard. It does not replace the technical authority of the engineering standards. It governs which version is treated as active, candidate, superseded, duplicate, retired, or revoked. When conflicts appear, the stricter control applies temporarily and the issue is routed to the appropriate owner through AVCI reconciliation.

# 3. Canonical Baseline Operating Model

The baseline control plane ties each source to its owner, status, evidence, release train, and reconciliation path. Git/OpenKM-approved sources remain authoritative. Obsidian and LLM Wiki may publish curated projections, but they must not become independent truth.
| Control Area | Mandatory Rule |
| --- | --- |
| Source authority | Every active or candidate document must have a governing path, source reference, generated output path, and publication state. |
| Version truth | Filename version, document-control version, register version, and supersedence state must match before publication. |
| Evidence linkage | Rendered QA, approval record, source/candidate lineage, and evidence-pack reference must be recorded. |
| Projection control | Obsidian, LLM Wiki, dashboards, and AI summaries are derivative projections and must link back to the registered source. |
| Reconciliation | Conflicts, duplicates, stale references, and missing evidence are logged as AVCI reconciliation items, not silently normalized. |

# 4. Baseline State Taxonomy
| State | Meaning | Allowed Use |
| --- | --- | --- |
| Draft | Generated or edited artifact not yet fully reviewed or rendered. | Internal review only; not canonical. |
| Review-Ready | Rendered and visually checked, but not yet approved. | ARB/CAB/team review; may be cited as candidate. |
| Active Candidate | Preferred updated version pending final approval. | Used for alignment with visible candidate status. |
| Active Canonical | Approved governing version in the register. | Primary authority for implementation and audit. |
| Superseded | Replaced by a later approved or active candidate version. | Retained for lineage and audit only. |
| Historical | Older baseline retained for reconstruction. | Audit comparison and trace reconstruction only. |
| Duplicate | Duplicate or overlapping authority requiring reconciliation. | Do not use until governing source is selected. |
| Retired | No longer relevant but retained as record. | No new implementation use. |
| Revoked | Withdrawn due to error, risk, or invalid authority. | Blocked from use except investigation. |

# 5. Required Register Fields

The register must exist in a human-readable form and a machine-readable form. A spreadsheet may be used during transition, but the target state is a Git-managed YAML/JSON register with CI validation and generated Word/Obsidian views.
| Field Group | Required Fields |
| --- | --- |
| Identity | doc_id, title, canonical_filename, source_pack, current_path, generated_path, owner, co_owners, classification |
| Versioning | current_version, recommended_version, status, supersedes, superseded_by, release_train, review_date, next_review_date |
| Authority | parent_documents, companion_documents, related_documents, governing_source, conflict_rule, approval_route |
| Evidence | render_qa_path, evidence_pack_ref, source_hash, generated_hash, approver_refs, waiver_refs, publication_refs |
| Lifecycle | state, activation_date, retirement_date, deprecation_reason, reconciliation_items, improvement_backlog_refs |

# 6. Supersedence and De-Duplication Rules

A newer document does not automatically supersede an older one unless the document-control block and register both state the supersedence relationship.

A candidate may guide the next alignment step, but it must be labeled as candidate until ARB/CAB or delegated owner approval is recorded.

Duplicate numbering, title collisions, and overlapping authority must be logged as reconciliation items. Do not silently renumber in the body of a dependent document.

Superseded documents remain available for trace reconstruction, but they must not be used as active authority for new design or implementation decisions.

If a generated file corrects a prior file, the register must preserve source lineage, generated output path, evidence path, and reviewer action required.

# 7. Release Train Governance

AIRA release trains group related document changes so dependencies move together instead of drifting independently. Each release train requires a scope statement, included documents, excluded documents, decision owner, evidence pack, compatibility note, known reconciliation items, and next review trigger.
| Release Train | Purpose | Typical Contents |
| --- | --- | --- |
| RT-Foundation | Preserve enterprise architecture and AVCI authority. | 00A-00E, 01A, 01, 01B, 02, 03, 04, 05, 06, 07, 07B |
| RT-MicroFunction | Govern MicroFunction runtime, design, implementation, diagrams, catalog, and backend generation. | 10, 10A, 10B, 10C, 10D, 10E |
| RT-DevSecOps | Govern CI/CD, evidence packs, policy, security gates, promotion, and executable governance. | 11, 11A, 20, 62, 63, 64, 65, 66, 68 |
| RT-Integration | Govern APIs, events, schemas, outbox, DLQ, replay, and contracts. | 15/15A, 67, related MicroFunction and CI/CD gates |
| RT-AI-Governance | Govern AI model routes, guardrails, agents, evaluation, red-team, and System Builder. | 42 series, 43, 43A, 58, 61, 70 |
| RT-Dynamic-Workspace | Govern workspace UX, templates, Admin Builder, pipeline, runtime sync, and AI-assisted UI. | 54, 55, 59, 60, 61, 71 as classification authority |
| RT-Operational-Assurance | Govern readiness, resilience, observability, incidents, continuity, and rollback. | 31/31A, 63, 64, 68, 69, 71 |

# 8. Initial AIRA Release Train Baseline

The following initial register grouping records the current active candidate set generated or updated in this workstream. Items not supplied, not regenerated, or not register-verified must not be marked complete solely because they appear in older review queues.
| Group | Documents / Candidate Versions | Register Treatment |
| --- | --- | --- |
| Foundation completed in this workstream | 01A v1.2, 01 v3.2, 01B v1.2, 02 v5.2, 03 v4.2, 04 v9.2, 05 v4.2, 06 v3.2, 07 v3.2, 07B v1.2 | Active Candidate pending ARB/CAB or delegated approval. |
| MicroFunction completed in this workstream | 10 v3.4, 10A v2.4, 10B v2.3, 10C v2.3, 10D v2.3, 10E v1.3 | Active Candidate MicroFunction suite; dependent documents must reference these versions. |
| DevSecOps completed in this workstream | 11 v3.3, 11A v1.3, 20 v1.3 | Active Candidate DevSecOps suite; Doc 20 is implementation companion. |
| Dynamic Workspace candidate set | 43, 43A, 54, 55, 58, 59, 60, 61 | Active Candidate where generated; verify source-pack authority in register. |
| Executable governance additions | 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72 | New Active Candidate documents pending ARB/CAB/team review. |
| Pending verification | 08, 08A, 09 and other older review-queue references not regenerated in current sequence | Register as Source Pack / Pending Verification unless separately supplied or approved. |

# 9. Conflict and AVCI Reconciliation Workflow

Conflicts must be managed as controlled reconciliation items. A conflict is any mismatch in document ID, title, version, filename, parent/companion reference, source pack, supersedence statement, classification, owner, approval status, or technical control requirement.
| Step | Required Action | Evidence |
| --- | --- | --- |
| Detect | Identify conflict, duplicate, stale reference, missing evidence, or unclear authority. | Reconciliation item with source refs and severity. |
| Classify | Assign severity: Critical, High, Medium, Low. | Classification and affected release train. |
| Contain | Apply stricter control temporarily; block unsafe publication if needed. | Containment note and owner. |
| Decide | Recommend governing source and route to owner, ARB/CAB, Security, Data, or DevSecOps path. | Decision record and approval route. |
| Correct | Update document, register, cross-reference, manifest, and projections. | Updated files, render QA, evidence pack. |
| Close | Verify no stale references remain and link closure evidence. | Closure timestamp, reviewer, improvement backlog. |

# 10. Evidence and Publication Package

Every candidate or active canonical document must have a publication package. The package should align with the evidence manifest model and CI/CD evidence-pack structure so document governance becomes executable and auditable.
| Evidence Class | Required Evidence |
| --- | --- |
| Source lineage | Source file, source pack, prior version, generated file, source hash, generated hash, and change summary. |
| Render QA | PDF or PNG render path, page count, visual QA confirmation, defect corrections, and final render timestamp. |
| Review evidence | Owner, checker, ARB/CAB or delegated approval route, unresolved comments, waivers, and acceptance decision. |
| Cross-reference evidence | Parent/companion versions, supersedence mapping, stale-reference scan, duplicate detection, and affected documents. |
| Publication evidence | Git/OpenKM path, Obsidian projection path, LLM Wiki freshness timestamp, retention rule, and classification handling. |

# 11. Automation and Machine-Readable Register Controls
| Automation Control | Expected Behavior |
| --- | --- |
| Version lint | Compare filename, title page, document control, change log, and register version. |
| Cross-reference scan | Detect stale references to superseded document versions and unresolved companion links. |
| Duplicate detection | Detect duplicate document IDs, titles, filenames, semantic near-duplicates, and numbering conflicts. |
| Evidence check | Verify render QA, source hash, generated hash, approval route, classification, and evidence pack references. |
| Projection freshness | Validate Obsidian and LLM Wiki projections are derived from the active registered source. |
| Release train gate | Block release-train promotion when required documents are missing, stale, unrendered, unclassified, or unresolved. |

## 11.1 Minimum Machine-Readable Record

doc_id: AIRA-DOC-00E
title: AIRA Canonical Baseline, Supersedence, and Release Train Register
version: v1.0
state: active_candidate
classification: INTERNAL CONFIDENTIAL
owner: Solutions Architecture Office / IT Head
release_train: RT-Foundation
supersedes: null
parents: [00A, 00B, 00C, 00D, 01A, 01, 01B, 02, 11, 11A, 20, 62, 66, 68]
evidence:
  render_qa: required
  source_hash: required
  approval_record: pending
  reconciliation_items: []

# 12. RACI and Separation of Duties
| Activity | Architecture / IT Head | DevSecOps | Knowledge Governance | Security | Internal Audit |
| --- | --- | --- | --- | --- | --- |
| Maintain 00E register standard | A/R | C | R | C | C |
| Update machine-readable register | A | R | R | C | I |
| Approve active canonical state | A/R | C | C | C | I |
| Validate CI/CD and evidence linkage | A | R | C | C | C |
| Resolve conflicts and duplicates | A/R | C | R | C | C |
| Audit register completeness | C | C | C | C | A/R |

# 13. Acceptance Criteria

All generated AIRA documents have a register entry with document ID, title, version, owner, classification, source path, generated path, status, supersedes, and release train.

The active MicroFunction, DevSecOps, Dynamic Workspace, AI governance, and executable governance candidate sets are clearly separated from historical and pending-verification sources.

Duplicate numbering and overlapping authority issues are logged as reconciliation items and not hidden in dependent documents.

The register can be exported to Word, Excel, YAML/JSON, Obsidian, and LLM Wiki projection without changing authority.

Release-train promotion is blocked if required documents are unrendered, unclassified, unresolved, missing evidence, or inconsistent with parent references.

# 14. Open Reconciliation Items
| ID | Issue | Required Treatment | Severity |
| --- | --- | --- | --- |
| RI-00E-001 | 11A duplicate numbering appears in historical/source references. | Track in 00D/00E and do not silently renumber until governing source is confirmed. | Medium |
| RI-00E-002 | 41B / 44 System Builder overlap remains a known authority concern. | Create or update System Builder Operating Manual and register governing source. | High |
| RI-00E-003 | 01A v1.1 Pack 01 placement and older source-pack references may conflict with revised outputs. | Maintain source-pack lineage and active-candidate designation until approval. | Medium |
| RI-00E-004 | Some review queues marked 08, 08A, and 09 complete without current regenerated files in this sequence. | Register as pending verification unless source or approval evidence is supplied. | Medium |
| RI-00E-005 | Future packer/regeneration runbook is needed to rebuild packs and manifests deterministically. | Create backlog item for source packer and regeneration runbook. | High |

# 15. AVCI Compliance Summary
| AVCI Property | How This Standard Satisfies It |
| --- | --- |
| Attributable | Every baseline decision identifies document owner, source, version, state, release train, approver, supersedence path, and reconciliation owner. |
| Verifiable | Register entries link to source hashes, generated hashes, render QA, evidence packs, approvals, publication paths, and closure evidence. |
| Classifiable | Every document, projection, evidence pack, register entry, screenshot, and source artifact must carry classification and handling rules. |
| Improvable | Conflicts, stale references, defects, audit findings, and release-train gaps feed reconciliation items, backlog, standards updates, and automation controls. |

# 16. Recommended Next Document

The next recommended AIRA document is AIRA System Builder Operating Manual and Maker-Checker Runbook v1.0. This is the correct follow-on because 41B / 44 overlap is a known reconciliation item and because System Builder is now referenced across DevSecOps, Policy-as-Code, AI certification, Golden Paths, Evidence Manifest, Dynamic Workspace, and MicroFunction governance.

Final Rule: AIRA must never allow document generation, System Builder generation, AI-assisted development, or Dynamic Workspace projection to outrun canonical source control. The register governs the baseline. Evidence proves the baseline. Human authority approves the baseline.

