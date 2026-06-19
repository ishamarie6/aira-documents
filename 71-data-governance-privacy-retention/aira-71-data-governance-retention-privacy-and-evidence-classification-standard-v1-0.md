---
title: "Data Governance Retention Privacy and Evidence Classification Standard"
doc_id: "AIRA-71"
version: "v1.0"
status: "final"
category: "Data governance privacy and retention"
source_docx: "AIRA_71_Data_Governance_Retention_Privacy_and_Evidence_Classification_Standard_v1.0.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 71-data-governance-privacy-retention
  - final
  - aira-71
---



# Data Governance Retention Privacy and Evidence Classification Standard



AIRA
AI-Native Enterprise Platform

Data Governance, Retention, Privacy, and Evidence Classification Standard

AIRA-DOC-071 | Version v1.0

Data Governance | Privacy by Design | Classification-Aware AI | Evidence Retention | Redaction | Disposal | AVCI Always
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-071 |
| Canonical Filename | AIRA_71_Data_Governance_Retention_Privacy_and_Evidence_Classification_Standard_v1.0.docx |
| Version | v1.0 - Initial Enterprise Data Governance, Privacy, Retention, and Evidence Classification Standard |
| Status | Draft for Architecture Review Board, CAB, Data Governance, Security, DevSecOps, AI Governance, SRE, DBA, Legal/Compliance, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Data Governance; Security Architecture; DevSecOps Lead; DBA; AI Governance; SRE; Software Development Lead; QA/SDET; Internal Audit; Legal/Compliance where applicable |
| Primary Parents | 01A, 01, 01B, 02, 11, 11A, 20, 62, 63, 64, 65, 66, 67, 68, 69, 70 and active MicroFunction/Dynamic Workspace/API/Security/Observability standards |
| Review Cadence | Quarterly; unscheduled after material data, privacy, retention, AI, evidence, API/event, telemetry, production-readiness, or regulatory change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Data-Governance-Privacy-Retention / 71 / v1.0 / |

Mandatory Practice Statement

No AIRA data, prompt, evidence, log, trace, event, document, test fixture, screenshot, model context, Dynamic Workspace artifact, or MicroFunction payload is acceptable unless it has a defined owner, purpose, classification, handling rule, retention rule, redaction posture, access policy, evidence reference, and improvement path. Missing classification or retention defaults to fail-closed handling for protected data and production-bound evidence.

Static Table of Contents

1. Executive Summary

2. Purpose, Scope, and Authority

3. Governance Principles

4. Data and Evidence Classification Taxonomy

5. Data Inventory and Processing Record

6. Data Lifecycle Controls

7. Retention, Legal Hold, Disposal, and Anonymization

8. Privacy by Design and Data Subject Rights

9. AI, RAG, Prompt, and Model Context Governance

10. MicroFunction, Dynamic Workspace, API/Event, and Evidence Controls

11. Observability, Logs, Traces, Screenshots, and Test Data

12. CI/CD, Policy-as-Code, Evidence Manifest, PRR/ORR, and Resilience Binding

13. RACI, Validation Checklist, Acceptance Criteria, and AVCI Summary

# 1. Executive Summary

This standard establishes the AIRA data governance, retention, privacy, and evidence classification control model. It turns data handling from an informal application concern into an executable enterprise discipline enforced by classification, Policy-as-Code, MicroFunction runtime controls, CI/CD evidence manifests, observability redaction, production readiness gates, and auditable lifecycle decisions.

AIRA processes multiple sensitive artifact types: business data, mortgage/loan records, documents, runtime configuration, workflow records, API/event payloads, prompts, model outputs, retrieval sources, telemetry, screenshots, tests, incidents, evidence packs, and generated artifacts. Each must be governed with consistent ownership, purpose, classification, access control, retention, redaction, and disposal rules.
| Outcome | Required Result |
| --- | --- |
| Enterprise data discipline | Data governance is explicit across source, runtime, evidence, observability, AI, Dynamic Workspace, MicroFunctions, and CI/CD. |
| Privacy by design | Purpose, minimization, access, retention, redaction, consent/legal basis where applicable, and privacy-impact review are built into design and delivery. |
| Evidence-safe operations | Evidence packs remain useful for audit and reconstruction without leaking secrets, raw PII, raw prompts, Restricted payloads, or unsafe telemetry. |
| Executable controls | Policy-as-Code, evidence manifest validation, PRR/ORR, Resilience Lab, API/event governance, and AI model-route certification enforce this standard. |
| AVCI assurance | Every data and evidence artifact remains attributable, verifiable, classifiable, and improvable across its lifecycle. |

# 2. Purpose, Scope, and Authority

## 2.1 Purpose

Define the standard treatment for AIRA data governance, privacy, retention, redaction, disposal, evidence classification, and classification-aware AI use.

Prevent uncontrolled storage, sharing, logging, prompting, retrieval, test-data use, and evidence publication of personal, confidential, restricted, or regulated data.

Bind data governance to CI/CD gates, evidence manifests, Policy-as-Code, production readiness, resilience testing, MicroFunction runtime controls, and audit assurance.

Create a reusable foundation for data inventories, records of processing, data subject rights, breach response evidence, retention schedules, and controlled disposal.

## 2.2 Scope
| In Scope | Out of Scope |
| --- | --- |
| Business data, customer data, personal data, documents, evidence packs, logs, traces, metrics, prompts, model outputs, embeddings, screenshots, tests, API/event payloads, database records, runtime configuration, Dynamic Workspace artifacts, and GitNexus outputs. | Unclassified data stores, unmanaged shadow repositories, raw production data in tests, unredacted telemetry, manual disposal without evidence, or AI use outside approved model routes. |
| Local development, DEV, TEST, UAT, STAGING, PILOT, PRODUCTION-like, and PRODUCTION environments, with stricter controls for higher-risk environments. | Production data copied into lower environments without approval, masking, minimization, access control, and retention evidence. |
| Human-authored, System Builder-generated, AI-assisted, imported, scanned, and operationally generated artifacts. | AI-generated summaries treated as authoritative data records or legal/compliance decisions without human review and evidence. |

## 2.3 Authority and Precedence
| Level | Authority | Data Governance Meaning |
| --- | --- | --- |
| L0 | ARB / CAB / Security Governance / Data Governance / IT Head | Final authority for production-impacting data, privacy, retention, evidence, AI route, and exception decisions. |
| L1 | 01A / 01 / 01B / 02 | Architecture, AVCI, evidence, audit, classification, and traceability are universal controls. |
| L2 | This AIRA-DOC-071 Standard | Data governance, retention, privacy, and evidence classification authority. |
| L3 | 20 / 63 / 64 / 65 / 66 / 67 / 68 / 69 / 70 | Executable enforcement through CI/CD, readiness, resilience, policy-as-code, evidence manifest, API/event governance, traceability, secure design, and AI certification. |
| L4 | Runtime records, PR/MR evidence, data inventory, retention schedule, audit logs | Operational proof; may tighten but must not weaken governing standards. |

# 3. Governance Principles
| Principle | Mandatory Meaning |
| --- | --- |
| Purpose limitation | Each data element, prompt, evidence record, and telemetry field must have a declared purpose and owner. |
| Minimization | Collect, store, log, prompt, retrieve, and retain only what is necessary for the approved purpose. |
| Classification first | Data without classification is treated as at least Internal; suspected sensitive or personal data is treated as Confidential or Restricted until confirmed. |
| Fail closed | Missing classification, policy, redaction, retention, consent/legal basis where applicable, or evidence path blocks protected processing. |
| Evidence without leakage | Evidence must support reconstruction and audit without exposing secrets, raw PII, raw tokens, raw prompts, or Restricted payloads. |
| Authoritative source discipline | Git, PostgreSQL/Flyway, OpenKM, approved evidence stores, and governed registries are authoritative; Obsidian/LLM Wiki/AI summaries are curated projections. |
| Human accountability | AI may classify, recommend, redact, and summarize as candidate support only; humans own final privacy, retention, production, and waiver decisions. |
| Improvability | Findings, incidents, access exceptions, retention failures, leaked fields, and redaction defects create backlog and Auto-Learn candidates. |

# 4. Data and Evidence Classification Taxonomy

Classification must apply to source data, payloads, prompts, embeddings, retrieval chunks, events, logs, traces, metrics, screenshots, test fixtures, evidence packs, generated artifacts, model outputs, and documentation projections.
| Classification | Examples | Required Handling |
| --- | --- | --- |
| Public | Approved public documentation, published marketing-safe diagrams, public APIs without sensitive data. | May be shared externally only after approval and source review; no secrets, internal topology, or Restricted context. |
| Internal | General internal standards, non-sensitive build logs, role-neutral operational summaries. | AIRA internal access only; retain according to standard schedule; protect against unauthorized external disclosure. |
| Confidential | Customer/business records, internal architecture, non-public contracts, GitNexus reports, CI/CD evidence, operational dashboards. | Need-to-know access, redaction for summaries, retention schedule, audit trail, protected storage, controlled model-route eligibility. |
| Restricted | Secrets, credentials, tokens, financial identifiers, sensitive personal information, raw prompts with sensitive context, production incident evidence, privileged access logs. | Strict least privilege, encryption, no AI route unless certified, no raw logging, no lower-environment copy without masking/approval, legal hold and disposal evidence. |
| Evidence-Sensitive | Evidence that is not itself Restricted but reveals controls, topology, vulnerabilities, findings, residual risk, or incident details. | Treat at least Confidential; publish curated summaries only; store source evidence in controlled evidence repository. |
| Artifact Type | Minimum Classification Rule |
| --- | --- |
| Production logs/traces/audit | Confidential unless proven sanitized; Restricted when containing personal, secret, security, or privileged content. |
| Prompts/model outputs/RAG chunks | Confidential by default; Restricted when containing personal, financial, privileged, secret, or incident content. |
| Evidence packs | Internal Confidential by default; Restricted sections separated or redacted. |
| Screenshots/videos | Classify based on highest visible data; Restricted if credentials, personal data, customer data, or vulnerabilities are visible. |
| Test data/fixtures | Synthetic preferred; production-derived data requires approval, masking, expiry, and evidence. |
| Obsidian/LLM Wiki pages | Curated derivative; no raw source code, secrets, raw PII, raw prompts, or Restricted payloads. |

# 5. Data Inventory and Processing Record

AIRA shall maintain a governed data inventory and processing record for material systems, bounded contexts, MicroFunctions, Dynamic Workspace components, AI/RAG flows, evidence stores, and external integrations.
| Inventory Field | Required Meaning |
| --- | --- |
| data_asset_id | Unique data asset or evidence class identifier. |
| owner / steward | Named accountable owner and operational steward. |
| bounded_context | Business/domain boundary and owning schema/API/event family. |
| data_subject_or_entity | Person, account, property, case, loan, user, agent, service, system, or artifact. |
| purpose | Declared business, security, operational, evidence, or improvement purpose. |
| classification | Public, Internal, Confidential, Restricted, Evidence-Sensitive, and PII/sensitive flags. |
| source and destination | System of origin, authoritative store, downstream consumers, evidence stores, and projections. |
| legal_basis_or_policy_ref | Consent, contract, legitimate purpose, regulatory obligation, security requirement, policy ref, or internal authority where applicable. |
| retention_rule | Retention period, trigger, legal hold behavior, archive, deletion/anonymization method. |
| access_policy | RBAC/ABAC/SBAC/OPA rule, role/skill, tenant, environment, and approval path. |
| AI_route_eligibility | Allowed/blocked model routes, retrieval eligibility, redaction requirements, and guardrail profile. |
| evidence_ref | Evidence manifest, CI/CD validation, review record, and audit trail reference. |

# 6. Data Lifecycle Controls
| Lifecycle Stage | Mandatory Control |
| --- | --- |
| Intake | Capture source, owner, purpose, classification, consent/legal/policy basis where applicable, and evidence path. |
| Collection | Minimize fields; reject unknown source; scan files; validate API/event/schema; apply classification. |
| Processing | Use MicroFunction, API, policy, workflow, AI, and database controls; fail closed on missing identity/policy/classification. |
| Storage | Use approved stores; encrypt where required; segregate Restricted data; bind retention and evidence_ref. |
| Access and Sharing | Enforce OPA/SBAC, need-to-know, purpose, tenant, environment, and classification controls; log decisions. |
| Use in AI/RAG | Check route eligibility, retrieval policy, redaction, prompt classification, guardrails, model audit, and human review where required. |
| Retention | Apply retention schedule, legal hold, audit hold, evidence retention, and review cadence. |
| Disposal | Delete, anonymize, archive, or destroy with certification and evidence; update inventory and manifest. |
| Improvement | Findings, defects, incidents, complaints, or retention failures feed controlled Auto-Learn/Improve backlog. |

# 7. Retention, Legal Hold, Disposal, and Anonymization
| Artifact Class | Default Retention Rule | Disposal / Review Control |
| --- | --- | --- |
| CI/CD evidence packs | Retain per release/audit policy and applicable regulatory needs; production releases require longer retention than DEV-only evidence. | Archive in approved evidence store; delete only by policy and with destruction evidence. |
| Security scans and findings | Retain until closure plus audit period; Critical/High findings retain remediation evidence. | Do not delete open findings; waiver closure requires evidence. |
| Logs and traces | Retain according to classification, operational need, and storage cost; Restricted logs require minimization and redaction. | Aggregate/anonymize where possible; legal hold overrides deletion. |
| Audit records | Retain as immutable records according to audit and regulatory posture. | No alteration; disposal only by approved lifecycle policy. |
| Prompts and model outputs | Retain only if needed for evidence, evaluation, RCA, or improvement; store metadata over raw content where feasible. | Redact/anonymize; raw Restricted prompts require approval and strict retention. |
| Test data | Synthetic retained with tests; production-derived masked data expires and must be reviewed. | Destroy or refresh; prove masking and disposal. |
| Customer/business records | Follow system-of-record, legal, business, and regulatory schedule. | Archive/delete according to approved retention and hold rules. |
| Backups | Retention follows backup policy; restricted data remains protected through backup lifecycle. | Expire through backup lifecycle; document restore and destruction posture. |

Legal hold, audit hold, incident hold, or investigation hold suspends normal disposal and must be recorded with owner, scope, start, review cadence, and release condition.

Anonymization must be irreversible for the intended context; pseudonymization remains personal or sensitive data if re-identification is possible through available mappings.

Deletion must consider primary stores, indexes, caches, search projections, vector stores, derived summaries, screenshots, evidence packs, backups, and downstream consumers.

# 8. Privacy by Design and Data Subject Rights
| Control Area | Required Treatment | Evidence |
| --- | --- | --- |
| Privacy impact review | Required for new or changed processing of personal, sensitive, AI, cross-border, high-risk, or large-scale data. | Privacy impact record, threat model, data inventory update, approval. |
| Transparency and notice | Where applicable, processing purpose, scope, retention, sharing, and rights must be communicated through approved channels. | Notice reference, consent/legal basis record, policy mapping. |
| Data subject rights | Access, correction, erasure/blocking where applicable, objection, portability, and complaint handling must have workflow and evidence. | Request ID, verification, decision, action, completion evidence. |
| Breach notification readiness | Security/privacy incidents involving personal data require classification, containment, assessment, notification decision, and remediation evidence. | Incident record, RCA, notification log, evidence pack, closure. |
| Third-party processors | Vendors/processors must be bound by contract, security, confidentiality, retention, deletion, breach, and audit requirements. | DPA/DPA-equivalent contract, vendor risk, evidence, review cadence. |
| Privacy engineering | Privacy controls must be built into design, lifecycle, tests, and runtime evidence, not added after production. | Secure design review, test evidence, PRR/ORR gate. |

# 9. AI, RAG, Prompt, and Model Context Governance
| AI/Data Area | Required Control | Blocking Condition |
| --- | --- | --- |
| Prompt intake | Prompt metadata must record owner, purpose, classification, model route, retrieval source, and evidence_ref. | Raw Restricted prompt sent to unapproved model route. |
| RAG retrieval | Retrieval must enforce source authority, classification, tenant, purpose, freshness, and SBAC/OPA eligibility. | Retrieved content exceeds actor skill, model route, or classification ceiling. |
| Embeddings/vector stores | Embeddings are derivative data and inherit classification and retention from source; deletion/anonymization must handle vector projections. | Vector store becomes uncontrolled authority or contains untracked personal/Restricted data. |
| Model output | Output classification derives from input, retrieved sources, generated content, and destination channel. | Output exposes sensitive details, authority claims, unsafe instructions, or unverified recommendations. |
| AI evidence | Prefer metadata, hashes, citations, evaluation scores, and redacted summaries over raw sensitive prompts/outputs. | Evidence pack contains secrets, raw tokens, raw PII, or Restricted payloads without approval. |
| Model route certification | Route eligibility must follow AIRA-DOC-070 certification, guardrail, red-team, and approval requirements. | Uncertified model route or bypass of LiteLLM/private gateway. |

# 10. MicroFunction, Dynamic Workspace, API/Event, and Evidence Controls
| Control Surface | Data Governance Requirement |
| --- | --- |
| MicroFunction runtime | Every transaction declares classification ceiling, input/output contract, policy decision, idempotency, audit, evidence_ref, retention, and error redaction. |
| Dynamic Workspace | Frontend may render only policy-filtered data from backend-governed MicroFunctions/APIs; UI configuration does not become business authority. |
| OpenAPI/AsyncAPI | Contracts must declare classification, security scheme, safe error model, idempotency, schema version, examples without sensitive data, and retention-impact notes. |
| Kafka/CloudEvents/Schema Registry | Events inherit classification; CloudEvents metadata must carry safe correlation/evidence fields; schemas must support evolution, retention, DLQ, replay, and redaction. |
| Outbox/inbox/DLQ/replay | Replay must not violate retention, consent/purpose, classification, or legal hold. DLQ payloads require restricted access and redaction review. |
| Evidence manifest | Evidence packs must reference data classes, retention rules, redaction status, privacy-impact decisions, and disposal/review dates. |
| Policy-as-Code | OPA/SBAC policy must enforce data access, AI route eligibility, runtime toggles, deployment gates, and retention/disposal approvals. |

# 11. Observability, Logs, Traces, Screenshots, and Test Data
| Artifact | Allowed | Prohibited |
| --- | --- | --- |
| Structured logs | Safe correlation, actor hash, tenant, transaction, step, result, error code, classification, evidence_ref. | Passwords, tokens, raw JWTs, raw PII, account numbers, raw prompts, documents, embeddings, unrestricted payloads. |
| Traces | Trace/span IDs, safe attributes, dependency timing, policy decision ID, outbox ID, evidence_ref. | Sensitive payload attributes, high-cardinality personal labels, secret headers. |
| Metrics | Counts, rates, latency, saturation, errors, DLQ, policy denies, SLOs. | Personal identifiers or sensitive values as labels. |
| Sentry/errors | Sanitized stack summary, release, environment, error code, trace, evidence reference. | Secrets, raw request body, raw documents, unrestricted screenshots. |
| Screenshots/videos | Redacted UI evidence, synthetic data, cropped sensitive areas, classification label. | Visible credentials, customer records, Restricted payloads, private keys, tokens. |
| Test data | Synthetic, masked, or generated fixtures with classification labels. | Unmasked production data in local/dev/test without approval and expiry. |

# 12. CI/CD, Policy-as-Code, Evidence Manifest, PRR/ORR, and Resilience Binding
| Gate | Required Data Governance Evidence |
| --- | --- |
| CI/CD evidence gate | Evidence manifest includes classification, retention, redaction status, data-source provenance, AI-use declaration, and evidence storage path. |
| Policy-as-Code gate | OPA/SBAC tests prove data access, classification, AI route, retention, legal hold, and runtime toggle rules fail closed. |
| PRR/ORR gate | Production readiness verifies data inventory, privacy review, retention schedule, observability redaction, access model, backup/restore, and support runbooks. |
| Resilience Lab gate | Performance/concurrency/chaos tests must use synthetic or approved masked data and prove evidence remains reconstructable under failure. |
| Threat modeling gate | Threat model and abuse cases include data exfiltration, unauthorized processing, prompt leakage, evidence leakage, replay misuse, and retention failure. |
| AI certification gate | Model routes, prompts, RAG sources, tool actions, and agent outputs pass classification, guardrail, red-team, and evidence retention criteria. |

# 13. RACI, Validation Checklist, Acceptance Criteria, and AVCI Summary
| Role | RACI | Responsibility |
| --- | --- | --- |
| Solutions Architecture Office / IT Head | A/R | Owns standard, architecture fit, conflict resolution, and escalation. |
| Data Governance / Privacy Owner | A/R | Owns classification taxonomy, data inventory, retention schedule, privacy impact review, and data subject rights workflow. |
| Security Architecture | A/R | Owns security controls, OPA/SBAC, secrets hygiene, abuse-case review, incident/breach evidence. |
| DevSecOps Lead | R | Owns CI/CD, evidence manifest, policy-as-code gates, retention validation, and release evidence. |
| DBA / Platform / SRE | R | Owns stores, backups, retention implementation, logs/traces, restoration, deletion, and observability controls. |
| AI Governance | A/R | Owns AI route eligibility, prompt/RAG/model-output governance, and AI evidence controls. |
| Software Development / QA/SDET | R | Implements data-safe code, tests, masking, contracts, telemetry redaction, and evidence artifacts. |
| Internal Audit | C/I | Reviews control effectiveness, evidence retention, exceptions, and remediation closure. |

## 13.1 Validation Checklist
| Checkpoint | Pass Condition |
| --- | --- |
| Data inventory | Material data assets, evidence classes, prompts, telemetry, and runtime artifacts have owner, purpose, classification, source, retention, and access rules. |
| Classification | All records, payloads, logs, prompts, screenshots, tests, and evidence packs have classification and handling rules. |
| Privacy impact | Personal, sensitive, AI, high-risk, or new processing has impact review and approval evidence. |
| Retention and disposal | Retention, legal hold, anonymization/deletion, and disposal evidence are defined and testable. |
| AI/RAG | Model route, retrieval eligibility, prompt classification, guardrails, and output handling are certified. |
| Observability redaction | Logs/traces/metrics/Sentry/screenshots are redaction-tested and free of prohibited fields. |
| Policy-as-Code | OPA/SBAC tests enforce data access, classification, AI route, retention, legal hold, and runtime toggle decisions. |
| Evidence manifest | Manifest references classification, retention, redaction, owner, source, hash, storage path, and review/disposal dates. |
| AVCI | Artifacts are attributable, verifiable, classifiable, and improvable. |

## 13.2 Anti-Patterns and Rejection Rules

Logging raw personal data, credentials, tokens, prompts, Restricted payloads, documents, or embeddings.

Using production data in local, DEV, TEST, or demos without masking, approval, retention, and disposal evidence.

Treating AI summaries, Obsidian projections, vector stores, dashboards, or GitNexus output as authoritative data truth.

Creating API/event schemas without classification, retention, and safe examples.

Allowing replay, DLQ repair, or backfill to ignore purpose, retention, or classification constraints.

Deleting data without checking legal hold, audit hold, evidence retention, downstream copies, indexes, caches, and backups.

Permitting AI route use when source classification, retrieval eligibility, or guardrail result is missing.

## 13.3 Acceptance Criteria

AIRA-DOC-071 is added to the canonical register as the governing data governance, retention, privacy, and evidence classification standard.

Data inventory and processing record templates exist for MicroFunctions, Dynamic Workspace, API/event flows, AI/RAG routes, evidence packs, and operational telemetry.

CI/CD evidence manifests include classification, retention, redaction, source, owner, route eligibility, storage path, and disposal/review fields.

Policy-as-Code tests can block unclassified data flows, unsafe AI routes, missing retention, missing redaction, and prohibited evidence content.

PRR/ORR and Resilience Lab gates verify data governance and evidence classification before production or production-like activation.

Open reconciliation items are tracked in 00D or the canonical release train register.

## 13.4 Open Reconciliation Items
| ID | Issue | Treatment | Owner |
| --- | --- | --- | --- |
| RI-071-001 | Create enterprise retention schedule with exact durations by artifact class. | Route to Legal/Compliance, Data Governance, Security, Internal Audit, and business owners; do not hardcode durations until approved. | Data Governance |
| RI-071-002 | Define formal Data Privacy Officer / privacy owner role assignment for AIRA operations. | Add to RACI and organization operating model. | IT Head / Governance |
| RI-071-003 | Propagate classification fields to evidence manifest, API/event schema, log/trace standards, and Dynamic Workspace metadata. | Create cross-document update tasks for 66, 67, 31A, 54, 59, 60, 61. | Architecture Office |
| RI-071-004 | Confirm legal/regulatory retention and breach notification obligations for BFS production deployment. | Review with legal/compliance before production. | Legal/Compliance |

## 13.5 External Alignment Reference
| Reference | AIRA Use |
| --- | --- |
| NIST Privacy Framework 1.0 / 1.1 IPD | Privacy risk management outcomes and privacy-by-design control alignment. |
| ISO/IEC 27701:2025 | Privacy information management system control inspiration for PII governance. |
| Philippines Data Privacy Act of 2012 and NPC guidance | Local privacy and personal data processing alignment for Philippine deployment context; final interpretation requires legal/compliance review. |
| NIST AI RMF and AIRA-DOC-070 | AI data, prompt, model route, and guardrail risk management. |
| AIRA-DOC-066 Evidence Manifest | Machine-readable evidence classification and retention binding. |
| AIRA-DOC-065 Policy-as-Code | Executable enforcement for access, classification, route eligibility, retention, and runtime toggles. |

## 13.6 AVCI Compliance Summary
| AVCI Property | How This Standard Satisfies It |
| --- | --- |
| Attributable | Defines owners, stewards, source refs, data inventory fields, prompt/model routes, evidence refs, approvals, and decision records. |
| Verifiable | Requires classification tests, privacy impact evidence, policy decisions, redaction tests, retention/disposal proof, CI/CD evidence, and audit records. |
| Classifiable | Defines data and evidence classification taxonomy, handling rules, AI route eligibility, telemetry classification, and evidence-sensitive treatment. |
| Improvable | Findings, incidents, redaction failures, retention defects, access exceptions, privacy issues, and audit observations feed governed backlog and Auto-Learn/Improve loops. |

Classification Before Processing - Evidence Without Leakage - Retain by Rule - Dispose with Proof - AVCI Always

