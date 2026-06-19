---
title: "Login MicroFunction Design Pattern Working Reference"
doc_id: "AIRA-40"
version: "v1.2"
status: "revised"
category: "Login MicroFunction reference"
source_docx: "AIRA_40_Login_MicroFunction_Design_Pattern_Working_Reference_v1.2_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 40-login-microfunction-reference
  - revised
  - aira-40
---



# Login MicroFunction Design Pattern Working Reference



AIRA
AI-Native Enterprise Platform

Login MicroFunction Design Pattern Working Reference
Disposition, Consolidation, and Controlled Companion Standard

v1.2 Revised

Configure First | Code Only the Business Gap | Govern Every Step | AVCI Always
| Property | Value |
| --- | --- |
| Document ID | AIRA-DOC-040 |
| Recommended Filename | AIRA_40_Login_MicroFunction_Design_Pattern_Working_Reference_v1.2_Revised.docx |
| Classification | INTERNAL CONFIDENTIAL |
| Status | CONTROLLED COMPANION / FOR MASTER REGISTER DISPOSITION |
| Owner | Solutions Architecture Office / IT Head |
| Supersedes | 40-AIRA_Login_MicroFunction_Design_Pattern_Working_Reference_v1.1_Aligned.docx |
| Canonical Authority | AIRA_22B_Login_and_Session_Establishment_MicroFunction_Design_Pattern_v1.2_Revised.docx |

# Document Control
| Field | Value |
| --- | --- |
| Document title | AIRA Login MicroFunction Design Pattern Working Reference |
| Document version | v1.2 Revised - Controlled Companion and Disposition Update |
| Primary classification | INTERNAL CONFIDENTIAL |
| Status | Controlled companion pending Master Register disposition |
| Owner | Solutions Architecture Office / IT Head |
| Co-owners | Enterprise Architecture; Software Development Lead; DevSecOps Lead; Security Architecture; QA/SDET; DBA; Platform Engineering; SRE; Internal Audit |
| Primary audience | Solutions Architects, Software Developers, QA/SDET, DevSecOps, Security, DBA, System Builder operators, Internal Audit |
| Source reviewed | 40-AIRA_Login_MicroFunction_Design_Pattern_Working_Reference_v1.1_Aligned.docx |
| Authoritative successor | AIRA_22B_Login_and_Session_Establishment_MicroFunction_Design_Pattern_v1.2_Revised.docx |
| Related execution standards | AIRA_23C_Login_PoC1_Code_Parameter_and_Configuration_Generation_Execution_Prompt_Standard_v1.2_Revised; AIRA_24_Login_PoC1_MicroFunction_Runtime_Configuration_Database_Schema_Standard_v1.2_Revised |
| Review cadence | One-time disposition review; then annual only if retained as a controlled companion |

# Table of Contents Placeholder

Insert a Microsoft Word automatic table of contents here before final publication. This document uses deterministic headings for reliable Word rendering and review.

# 1. Executive Review Summary

Document 40 is retained in v1.2 as a controlled working-reference companion only. It must not be treated as the authoritative Login MicroFunction design pattern. The authoritative Login and Session Establishment MicroFunction Design Pattern is Document 22B v1.2. Document 24 v1.2 governs PoC 1 runtime configuration and database schema. Document 23C v1.2 governs PoC 1 code, parameter, and configuration generation prompts.

The main improvement in this revision is disposition clarity. Unique useful notes from the former working reference are preserved as developer guidance, but all duplicative or conflicting guidance is subordinated to the canonical documents. This avoids architecture drift, duplicate login patterns, simplified schema invention, alternate step catalogs, and uncontrolled PoC 1A behavior leaking into PoC 1.

# 2. Disposition Decision
| Disposition Item | Decision |
| --- | --- |
| Authority status | Not authoritative. Controlled companion only. |
| Canonical design pattern | 22B Login and Session Establishment MicroFunction Design Pattern v1.2. |
| Canonical runtime and database schema | 24 Login PoC 1 MicroFunction Runtime Configuration Database Schema Standard v1.2. |
| Canonical generation prompt | 23C Login PoC 1 Code, Parameter, and Configuration Generation Execution Prompt Standard v1.2. |
| Allowed use | Developer onboarding, historical traceability, concept walkthrough, and review of extracted lessons. |
| Prohibited use | Source of truth for table names, schemas, step sequence, controller behavior, security policy, or runtime activation. |
| Recommended Master Register action | Retain for one review cycle as supplemental controlled reference; extract unique lessons into 22B, 23C, 24, or 41; then archive as historical. |

# 3. Purpose

The purpose of this revised document is to control the remaining working-reference material for the Login MicroFunction design pattern while preventing it from competing with the canonical AIRA Login documents. It gives developers a safe interpretation path for older notes and establishes what must be merged, archived, or retained.

# 4. Scope
| In Scope | Out of Scope |
| --- | --- |
| Disposition of Document 40 working-reference material. | Defining a second Login MicroFunction design pattern. |
| Mapping older notes to the revised 22B, 23C, 24, 41, 43, 43C, and 43D documents. | Creating new table names, schemas, transaction codes, or step codes. |
| Developer guidance for historical or supplemental use. | Implementing PoC 1A risk review, step-up, lock/unlock, or AI incident analysis inside PoC 1. |
| Reconciliation and archive rules for the master register. | Bypassing Keycloak/OIDC, OPA/SBAC, Flyway, audit, outbox, telemetry, or CI/CD evidence gates. |

# 5. Authority and Precedence
| Level | Authority | Required Interpretation |
| --- | --- | --- |
| L0 | Architecture Board / CAB / IT Head | Final decision authority for disposition, archive, or promotion. |
| L1 | 01 AVCI; 01A EDP/SOLID; 02 Blueprint; 10 MicroFunction Framework | Universal governance, architecture, and evidence requirements. |
| L2 | 22B Login and Session Establishment MicroFunction Design Pattern v1.2 | Authoritative Login MicroFunction design pattern. |
| L2 | 24 Login PoC 1 Runtime Configuration Database Schema Standard v1.2 | Authoritative PoC 1 runtime configuration and database schema. |
| L2 | 23C Login PoC 1 Generation Prompt Standard v1.2 | Authoritative generation prompt for PoC 1 artifacts. |
| L3 | This Document 40 v1.2 | Controlled companion only; must not override L0-L2 sources. |

# 6. Alignment Findings
| Finding | Required Correction |
| --- | --- |
| Document 40 was originally a working reference. | Keep only as controlled companion and remove any implied authority. |
| 22B is now the formal reusable design pattern. | All design conflicts resolve in favor of 22B. |
| 23C and 24 now define generation, schema, and runtime configuration. | All code-generation and database references must point to those documents. |
| PoC 1A behavior must remain additive. | Do not place risk review, step-up, lock/unlock, or AI incident analysis into AUTH_LOGIN_CONTEXT_ESTABLISH except through approved extension hooks. |
| Runtime actions must remain MicroFunction-backed. | Frontend, AI, or controller code must not become business, policy, or database authority. |
| Operational requirements have expanded. | Add DevSecOps, GitNexus, API/event, observability, DAST, resilience, and continuous-improvement evidence expectations. |

# 7. Retained Guidance from the Working Reference

Login is a governed assembly of identity, session, policy, audit, event, and observability controls, not a custom authentication engine.

Authentication remains delegated to Keycloak/OIDC and enterprise identity integration patterns; AIRA application code establishes governed session context only after required controls pass.

MicroFunctions should remain small, reusable, single-responsibility, dependency-inverted, observable, testable, and evidence-producing.

The working reference may be used for onboarding explanations, sequence walkthroughs, and historical rationale after conflicts are resolved against canonical sources.

# 8. Removed or Demoted Guidance
| Former Pattern Risk | v1.2 Treatment |
| --- | --- |
| Any alternate Login transaction name or step sequence | Rejected. Use AUTH_LOGIN_CONTEXT_ESTABLISH and the canonical sequence from 22B/23C/24. |
| Any simplified schema such as aira_config or aira_workspace | Rejected. Use canonical schemas such as aira_cfg and aira_ui. |
| Any implication that Document 40 is canonical | Rejected. Document 40 is controlled companion only. |
| Any direct controller or frontend authority for authorization | Rejected. Backend OPA/SBAC and MicroFunction execution remain authoritative. |
| Any AI, Auto-Heal, or Auto-Improve silent mutation | Rejected. Improvement loops generate candidates only, with evidence, tests, and human approval. |

# 9. Canonical Login Control Summary

The Login control pattern remains centered on AUTH_LOGIN_CONTEXT_ESTABLISH. The pattern must preserve identity resolution, correlation, authorization, classification, idempotency, vault/secrets safety, session encryption, audit, eventing, observability, safe response, and fail-closed error handling. The exact step catalog and database representation are governed by 22B, 23C, and 24, not by this working reference.
| Control Domain | Canonical Requirement |
| --- | --- |
| Identity | Keycloak/OIDC and enterprise identity integration; no custom password engine. |
| Authorization | OPA/Rego with RBAC, ABAC, and SBAC inputs. |
| Runtime assembly | Configuration-first MicroFunction runtime using approved step catalog and bindings. |
| Database | Flyway-only migrations; canonical schemas; no manual DDL or alternate schema invention. |
| Eventing | Transactional outbox, CloudEvents metadata, schema evolution, replay-safe consumers, DLQ as applicable. |
| Observability | OpenTelemetry trace correlation; safe Log4j2 logs; Sentry, Loki, Tempo, Grafana evidence where applicable. |
| Security testing | SAST, SCA, secrets scan, OPA tests, authenticated DAST, abuse-case tests, and remediation evidence. |
| Improvement | Auto-Heal, Auto-Learn, and Auto-Improve remain proposal-driven with tests and human approval. |

# 10. DevSecOps, Evidence, and GitNexus Requirements

Any continued use of Document 40 must be backed by a PR/MR evidence path when its content influences implementation. GitNexus may support read-only code intelligence and impact analysis, but it must not approve, merge, deploy, mutate production, or replace tests, security scans, CODEOWNERS, or human review.
| Evidence Area | Minimum Evidence Required |
| --- | --- |
| Source attribution | Source document, section, owner, reviewer, branch, commit, and related ticket. |
| Impact analysis | GitNexus read-only impact report or equivalent reviewer analysis. |
| Contract evidence | OpenAPI/AsyncAPI/schema validation where API or event behavior is affected. |
| Security evidence | SAST, SCA, secret scan, authenticated DAST where applicable, OPA/Rego tests, abuse-case review. |
| Runtime evidence | Trace ID, audit event, outbox event, policy decision, error handling, and safe response proof. |
| Rollback evidence | Feature disablement, forward-fix, rollback, compensation, or archive path. |

# 11. Observability, Runtime Toggles, and Forbidden Telemetry

Runtime logging and telemetry verbosity may be tuned when performance requires it. Mandatory audit, policy-decision, security, protected-action, evidence, and incident telemetry must not be disabled. Debug logging may be reduced, sampled, or temporarily elevated only through approved runtime controls with owner, expiry, classification, and audit evidence.

Never emit passwords, tokens, raw JWTs, secrets, private keys, unrestricted PII, raw customer documents, embeddings, or high-cardinality customer identifiers as metric labels.

Every protected login path must support trace reconstruction across frontend, gateway, backend adapter, MicroFunction runtime, OPA, audit, outbox, and observability stores.

Sentry or equivalent error monitoring must avoid leaking sensitive payloads and must use redaction before transmission or persistence.

Loki, Tempo, and Grafana dashboards must show safe operational signals without becoming sources of business truth.

# 12. Disposition Workflow

Compare Document 40 against 22B, 23C, 24, and 41 for unique reusable guidance.

Extract unique useful wording into the owning canonical document through a controlled PR/MR or documentation change request.

Classify each extracted item as design, runtime schema, generation prompt, evidence requirement, developer explanation, or historical rationale.

Retire duplicated material from active retrieval, or mark it as historical-only in Obsidian and the LLM Wiki retrieval metadata.

Update the master register with owner, disposition, supersedence, archive location, and retrieval eligibility.

Run retrieval regression checks to confirm AI assistants prefer 22B, 23C, and 24 over Document 40 for authoritative login answers.

# 13. Validation Checklist
| Checklist Item | Pass Condition |
| --- | --- |
| Canonical authority clear | Document states that 22B, 23C, and 24 govern over Document 40. |
| No duplicate schema authority | No new physical schemas, alternate table names, or simplified runtime tables are introduced. |
| PoC 1/PoC 1A boundary preserved | PoC 1A behavior remains additive and feature-flagged outside the baseline PoC 1 transaction. |
| Security preserved | Keycloak/OIDC, OPA/SBAC, Vault abstraction, audit, outbox, and fail-closed behavior remain mandatory. |
| Evidence complete | PR/MR evidence includes tests, scans, GitNexus impact, contract checks, policy checks, telemetry proof, and rollback. |
| Retrieval safe | Obsidian/LLM Wiki metadata marks this document as controlled companion or historical-only when superseded. |

# 14. Anti-Patterns

Using Document 40 as the source of truth after 22B, 23C, and 24 have been revised.

Creating a second login design pattern because the working reference contains older wording.

Embedding authorization logic in frontend components, controllers, or database scripts.

Treating Redis/Valkey, dashboards, AI summaries, or GitNexus output as authoritative truth.

Allowing AI-generated code or Auto-Heal proposals to bypass tests, policy checks, human approval, or CI/CD gates.

Logging raw tokens, credentials, secrets, raw PII, or detailed security failure reasons in user-visible channels.

# 15. RACI
| Activity | Responsible | Accountable | Consulted | Informed |
| --- | --- | --- | --- | --- |
| Disposition decision | Solutions Architecture | IT Head / ARB | DevSecOps; Security; DBA; QA | Development Team |
| Unique content extraction | Solutions Architecture; Documentation Owner | IT Head | Software Development Lead; Security | Internal Audit |
| Repository update | DevSecOps | Software Development Lead | QA; Security | Product Owner |
| Obsidian/LLM Wiki metadata update | Knowledge Steward | Knowledge Governance Owner | Architecture; Security | All users |
| Archive approval | Architecture Board | IT Head | Internal Audit; DevSecOps | Development Team |

# 16. Change Log
| Version | Change Summary | Disposition |
| --- | --- | --- |
| v1.1 Aligned | Promoted working reference into controlled provisional artifact pending master-register disposition. | Superseded by v1.2. |
| v1.2 Revised | Clarified non-authoritative status, mapped authority to 22B/23C/24, added extraction/archive workflow, and strengthened DevSecOps, API/event, observability, resilience, DAST, and improvement evidence. | Current controlled companion. |

# 17. Review Queue Control Register
| Seq | File Name | Recommended Version | Priority | Dependency | Action Required | Next Step |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 40 Working Reference v1.2 | v1.2 | High | 22B, 23C, 24, 41 | Disposition update | Extract unique content, then archive or retain as supplement. |
| 2 | 23B Architecture Fitness Function Catalog | v1.2 | High | 10, 10A-10D, 22B, 24 | Align automated gates | Review next. |
| 3 | 10D MicroFunction Catalog and Assembly Templates | v2.2 | High | 10, 10B, 22B, 24 | Align standard steps and templates | Review after 23B. |
| 4 | 10B MicroFunction Implementation Standard | v2.2 | High | 10, 10A, 10D, 23B | Align runtime engine rules | Review after 10D. |

# 18. AVCI Compliance Summary
| AVCI Property | Evidence in This Revision |
| --- | --- |
| Attributable | Document owner, source document, canonical successor, related execution standards, and disposition owner are identified. |
| Verifiable | Disposition decision, validation checklist, evidence gates, review queue, and retrieval regression expectations are defined. |
| Classifiable | Document is INTERNAL CONFIDENTIAL and explicitly controls Obsidian/LLM Wiki retrieval eligibility. |
| Improvable | Unique content extraction, archive workflow, and next review queue support controlled improvement without duplicate authority. |

