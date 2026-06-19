---
title: "Message Localization Support Knowledge Base and User Communication Governance Guide"
doc_id: "AIRA-81"
version: "v1.0"
status: "final"
category: "Message localization and knowledge base"
source_docx: "AIRA_81_Message_Localization_Support_Knowledge_Base_and_User_Communication_Governance_Guide_v1.0.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 81-message-localization-knowledge-base
  - final
  - aira-81
---



# Message Localization Support Knowledge Base and User Communication Governance Guide



AIRA
AI-Native Enterprise Platform

Message Localization, Support Knowledge Base,
and User Communication Governance Guide

AIRA-DOC-081 | Version v1.0

Localization | Message Catalog | Error Communication | Support KB | User Guidance | Incident Communications | Evidence | AVCI
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-081 |
| Canonical Filename | AIRA_81_Message_Localization_Support_Knowledge_Base_and_User_Communication_Governance_Guide_v1.0.docx |
| Version | v1.0 |
| Status | Draft for Architecture Review Board, Data Governance, Security, DevSecOps, QA/SDET, SRE/Ops, AI Governance, Knowledge Governance, Product, Service Desk, and Internal Audit Review |
| Classification | INTERNAL CONFIDENTIAL |
| Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; Data Governance; Knowledge Governance; Product/UX; Software Development; DevSecOps; Security Architecture; QA/SDET; SRE/Operations; Service Desk; AI Governance; Internal Audit |
| Primary Parents | AIRA-DOC-077 Canonical Data Element, Variable, Message, and Error Code Governance Standard; AIRA-DOC-078 Physical Schema and Admin Workflow; AIRA-DOC-079 Seed Catalog; AIRA-DOC-080 CI/CD Validator and Test Pack |
| Companion Sources | AIRA-DOC-020 CI/CD Evidence; 065 Policy-as-Code; 066 Evidence Manifest; 071 Data Governance; 074/075 Dynamic Workspace Certification; 031 Operations/SRE; 43A/58 AI Assistant and Prompt Governance |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Message-Localization-Support-KB-Communication / 081 / v1.0 / |

# Static Table of Contents

1. Executive Summary

2. Purpose, Scope, and Authority

3. Mandatory Practice Statement

4. Governance Principles

5. Control Plane

6. Localization Governance

7. Support Knowledge Base Governance

8. User Communication Governance

9. Channel and Audience Rules

10. Message-to-Knowledge Lifecycle

11. Gate Stack and CI/CD Evidence

12. Templates and Machine-Readable Records

13. RACI

14. Acceptance Criteria

15. Anti-Patterns and Rejection Rules

16. Open Reconciliation Items

17. AVCI Compliance Summary

# 1. Executive Summary

AIRA-DOC-081 defines how AIRA turns canonical message and error-code governance into consistent user-facing, support-facing, operator-facing, developer-facing, and AI-facing communication. A message is not only text. It is a governed artifact that affects user trust, accessibility, support efficiency, incident response, compliance evidence, localization, and operational traceability.

This guide closes the gap between technical message catalogs and enterprise communication. AIRA messages must be understandable, localized where required, safe for the intended audience, traceable to the canonical message/error catalog, linked to support knowledge, observable in operations tooling, and improvable through incidents, service tickets, analytics, defects, and user feedback.

Strategic rule: no AIRA UI message, validation text, API error, AI assistant response, support article, release note, incident update, email notification, SMS/push content, audit explanation, or operator communication may become production-facing unless it is classified, approved, safe, supportable, evidence-linked, and consistent with the canonical message catalog.
| Outcome | Required Result |
| --- | --- |
| Consistent user experience | User-facing messages use approved wording, severity, action guidance, localization key, and support reference. |
| Support readiness | Every actionable error has a support article, escalation path, solution guidance, and correlation/evidence reference. |
| Safe communication | Messages do not expose secrets, stack traces, raw PII, internal topology, policy internals, model prompts, or Restricted payloads. |
| Operational traceability | Messages link to message_code, trace_id, correlation_id, evidence_ref, policy decision, and dashboard or ticket reference where applicable. |
| Continuous improvement | Usage, incidents, failed searches, repeated tickets, user confusion, and support feedback improve wording, KB articles, tests, and catalog records. |

# 2. Purpose, Scope, and Authority

The purpose of this guide is to define how canonical messages, localized message resources, support knowledge articles, communication templates, release communications, incident communications, AI assistant responses, and service-desk guidance are authored, approved, published, used, monitored, and improved across AIRA.
| Scope Area | Required Treatment |
| --- | --- |
| Frontend and Dynamic Workspace | All labels, validation messages, errors, empty states, policy-denied screens, AI panel messages, and accessibility text must be catalog-backed and localization-ready. |
| Backend, MicroFunction, APIs, and Events | Errors and outcomes must use canonical message/error codes, safe response models, support mappings, and evidence correlation. |
| Support Knowledge Base | Every user-actionable or support-actionable error must link to a governed KB article, runbook, or escalation procedure. |
| Operations and Incidents | Incident communications, status updates, RCA summaries, and service notices must use approved templates and avoid uncontrolled disclosure. |
| AI and System Builder | AI may draft messages, translations, and KB updates only as candidate artifacts; human review and catalog checks are mandatory before publication. |

# 3. Mandatory Practice Statement

No AIRA message, translation, support article, operator instruction, release note, incident update, AI assistant response, email/SMS/push notification, UI validation text, or API-facing communication may be published or promoted unless it is catalog-backed, audience-aware, classification-safe, localized or fallback-safe, accessibility-aware, support-linked, observable, evidence-producing, and approved through maker-checker governance.

# 4. Governance Principles
| Principle | Mandatory Meaning |
| --- | --- |
| Catalog-backed communication | Production-facing wording must reference a canonical message_code or approved communication template. |
| Audience-safe detail | End users receive safe guidance; support and operators receive controlled technical detail based on role and classification. |
| Localization by design | Messages use stable keys, interpolation rules, fallback language, pluralization, and review workflow. |
| Supportability by design | Actionable failures provide solution guidance, retryability, escalation, ticket evidence, and documentation reference. |
| Accessibility and clarity | Messages must be readable, concise, screen-reader compatible, and usable under stress or incident conditions. |
| Evidence by construction | Every published message bundle, KB article, or communication template has source, owner, version, classification, tests, and approval evidence. |
| Fail closed for unsafe content | Unsafe, unclassified, unapproved, unlocalized, or support-unmapped messages are blocked from protected release. |

# 5. Control Plane

Figure 1. The control plane shows that the canonical message catalog is the authority, localization resources and support KB are governed derivatives, and user communications are published only through policy, CI/CD, observability, and feedback controls.

# 6. Localization Governance

Localization governance ensures that AIRA messages are stable, testable, culturally appropriate, accessible, and safe across supported locales. Localization must not introduce different business meaning, weaker security language, missing remediation, or unapproved disclosure.
| Localization Field | Required Meaning |
| --- | --- |
| message_key | Stable resource key mapped to message_code and lifecycle state. |
| locale | Language and regional variant such as en-PH, en-US, fil-PH when adopted. |
| default_text | Approved fallback text used when localized value is unavailable. |
| localized_text | Human-reviewed localized content; AI translation is candidate only. |
| interpolation_vars | Approved variables with type, classification, masking, and fallback rules. |
| pluralization_rule | Locale-aware pluralization where counts are shown. |
| accessibility_text | Screen-reader friendly equivalent where visual text is insufficient. |
| review_status | Draft, Reviewed, Approved, Active, Deprecated, Superseded, or Retired. |
| evidence_ref | Reference to approval, test, screenshot, UX review, or localization QA evidence. |

# 7. Support Knowledge Base Governance

The support knowledge base is the governed operational extension of the message catalog. AIRA users, service desk, SRE, security, developers, and auditors must be able to move from a message_code to the correct explanation, solution, escalation path, known limitation, or incident record without exposing sensitive internals.
| KB Record Field | Required Content |
| --- | --- |
| kb_article_id | Unique article identifier linked to one or more message codes. |
| message_codes | Related canonical messages and errors. |
| audience | End user, support L1, support L2/L3, developer, SRE, security, auditor, or AI assistant. |
| summary | Plain-language explanation of the issue or communication. |
| cause | Known safe causes and diagnostic decision tree. |
| user_action | Action a normal user may safely perform. |
| support_action | Service desk or operator steps, including ticket routing and escalation. |
| developer_action | Code/config/test/remediation path when engineering is required. |
| security_action | Containment, monitoring, abuse-case, or incident-response path where applicable. |
| evidence_links | Trace, evidence pack, release note, known error, RCA, or dashboard reference. |
| review_owner | Named steward responsible for accuracy and expiry review. |

# 8. User Communication Governance

AIRA user communication includes UI text, validation messages, onboarding guidance, service emails, support replies, release notes, incident updates, maintenance notices, chatbot/AI assistant responses, and Dynamic Workspace notifications. All communication must follow the same governance pattern: correct audience, safe detail, approved message source, evidence reference, and improvement path.
| Communication Type | Required Controls |
| --- | --- |
| UI / Dynamic Workspace | Catalog-backed text, accessible presentation, localization key, safe correlation reference, no stack trace. |
| API / Integration Response | Standard error response model, code, retryable flag, trace_id, evidence_ref, safe remediation hint. |
| Email / SMS / Push | Approved template, consent/channel policy, classification, no Restricted details, unsubscribe/notification policy where applicable. |
| Support Reply | KB-backed response, ticket reference, safe explanation, next-step ownership, no uncontrolled disclosure. |
| Release Note | Change summary, affected users, risk, rollback, known limitations, support link, evidence pack reference. |
| Incident Update | Severity, impact, status, next update time, workaround, support path, approved communications owner. |
| AI Assistant Response | Source-cited, guardrail-checked, role-filtered, no hidden authority, no direct approval or policy bypass. |

# 9. Channel and Audience Rules

AIRA separates message severity, business impact, data classification, and communication audience. A Fatal technical condition may produce a simple user message, a detailed SRE event, a security incident note, and an audit evidence record. These records share the same message_code lineage but expose different details based on role, classification, and channel.
| Audience | Allowed Detail | Forbidden Detail |
| --- | --- | --- |
| End User | Plain cause category, safe action, retry guidance, support reference, correlation ID when useful. | Stack traces, secrets, raw PII, policy internals, infrastructure names, exploit hints. |
| Service Desk | Troubleshooting steps, known error links, routing, escalation, safe evidence references. | Production secrets, raw tokens, unredacted Restricted payloads. |
| Developer / QA | Technical cause, test expectation, validation rule, code owner, reproduction path. | User secrets, uncontrolled production data, sensitive logs outside evidence controls. |
| SRE / Security | Operational impact, dashboards, trace links, containment, detection signals. | Unnecessary raw customer data or prompt payloads. |
| AI Assistant | Approved summary, citations, role-filtered guidance, candidate draft. | Authoritative approval, hidden policy bypass, sensitive prompt or tool outputs. |

# 10. Message-to-Knowledge Lifecycle

Figure 2. The lifecycle converts a message code into localized content, support knowledge, communication templates, operational feedback, and controlled improvement without losing traceability or approval history.

# 11. Gate Stack and CI/CD Evidence

Figure 3. Protected releases fail closed when a message, localization resource, KB article, or communication template lacks catalog integrity, localization completeness, safety review, support mapping, channel controls, evidence binding, or human approval.
| Gate | Required Evidence |
| --- | --- |
| Catalog integrity | Unique message_code, owner, severity, audience, lifecycle state, version, classification. |
| Localization completeness | Required locale bundle, fallback behavior, interpolation tests, missing-key report. |
| Safety and redaction | No forbidden telemetry fields, no raw PII/secrets, no stack trace exposure, safe wording review. |
| Support binding | KB article or runbook mapping for user-actionable and support-actionable messages. |
| Channel compliance | Template and channel rules for UI, API, email, notification, release, incident, and AI response. |
| Evidence manifest | Artifact references, tests, screenshots, approval, published version, rollback/supersedence path. |

# 12. Templates and Machine-Readable Records

## 12.1 Localization Resource Record
| Field | Example |
| --- | --- |
| message_code | AIRA-AUTH-API-ERROR-0001 |
| message_key | auth.login.session.expired |
| locale | en-PH |
| text | Your session has expired. Sign in again to continue. |
| interpolation_vars | [] |
| classification | Internal |
| accessibility_text | Session expired. Please sign in again. |
| fallback_key | auth.generic.retry |
| evidence_ref | evd-msgloc-2026-0001 |

## 12.2 Support KB Article Record
| Field | Example |
| --- | --- |
| kb_article_id | KB-AUTH-0001 |
| title | User session expired during secure access |
| audience | End User; Service Desk L1 |
| message_codes | AIRA-AUTH-API-ERROR-0001 |
| user_action | Sign in again. Contact support if the issue repeats. |
| support_action | Check session timeout policy, user role, and recent auth-service health. |
| escalation | Route repeated failures to Identity and Access support queue. |
| review_due | Quarterly or after auth/session policy change. |

## 12.3 Machine-Readable Communication Template Excerpt

{
  "message_code": "AIRA-AUTH-API-ERROR-0001",
  "message_key": "auth.login.session.expired",
  "severity": "ERROR",
  "audience": "END_USER",
  "locale": "en-PH",
  "safe_user_text": "Your session has expired. Sign in again to continue.",
  "support_kb_ref": "KB-AUTH-0001",
  "trace_display": "show_correlation_id_when_support_contact_needed",
  "classification": "INTERNAL",
  "evidence_ref": "evd-msgloc-2026-0001"
}

# 13. RACI
| Activity | Architect / IT Head | Data Gov | Knowledge Gov | Development | DevSecOps | Security | QA/SDET | SRE / Service Desk | AI Gov | Audit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Define message/localization standard | A/R | C | R | C | C | C | C | C | C | I |
| Approve message catalog changes | A | R | R | C | C | C | C | C | C | I |
| Approve support KB publication | A | C | A/R | C | I | C | C | R | C | I |
| Maintain localization resources | A | C | R | R | C | C | R | C | C | I |
| Run CI/CD message gates | A | C | C | R | A/R | C | R | C | C | I |
| Review incident communications | A | C | R | C | C | A/R | C | R | C | C |
| Audit evidence and retention | C | C | C | I | C | C | I | C | C | A/R |

# 14. Acceptance Criteria

• All production-facing messages trace to canonical message_code and message_key records.

• Required locale resources and fallback behavior are defined, tested, and evidence-linked.

• User-facing text is safe, accessible, actionable, classification-aware, and supportable.

• Every user-actionable and support-actionable error links to a KB article, runbook, escalation path, or support procedure.

• CI/CD blocks duplicate keys, missing translations, unsafe interpolation, hardcoded protected messages, missing KB mappings, and forbidden telemetry exposure.

• AI-generated translations, messages, and support content remain candidate artifacts until human review and evidence gates pass.

• Runtime telemetry and support tickets feed controlled improvement without silently changing production wording or catalog authority.

# 15. Anti-Patterns and Rejection Rules
| Anti-Pattern | Rejection Rule |
| --- | --- |
| Hardcoded UI strings for protected flows | Reject unless mapped to approved message catalog or explicitly classified as non-protected prototype text. |
| Different wording for same error across channels | Reject; consolidate under canonical message_code with channel-specific approved variants. |
| Translation changes business meaning | Reject and route to localization/content review. |
| Raw exception shown to user | Reject; map to safe message and internal technical evidence. |
| KB article without owner or expiry | Reject from publication and retrieval eligibility. |
| AI-generated support answer without source or KB link | Reject as advisory draft only. |
| Incident update discloses internal weakness or Restricted data | Reject and route to communications/security approval. |

# 16. Open Reconciliation Items
| ID | Item | Treatment | Owner |
| --- | --- | --- | --- |
| RI-081-001 | Propagate message localization gates into Dynamic Workspace certification and frontend implementation guides. | Track under 00E and next Dynamic Workspace update batch. | Architecture / UX |
| RI-081-002 | Integrate support KB records with Zammad/ITSM and OpenKM evidence paths. | Define adapter and evidence mapping in service management backlog. | SRE / Service Desk |
| RI-081-003 | Align AI Assistant Panel response policy with message catalog and KB source citation requirements. | Update AI assistant and prompt governance companion docs in next pass. | AI Governance |
| RI-081-004 | Define initial locale rollout and approved localization workflow. | Data/Knowledge Governance to confirm supported locale baseline. | Data / Knowledge Governance |

# 17. AVCI Compliance Summary
| AVCI Property | How This Guide Satisfies It |
| --- | --- |
| Attributable | Defines owners, stewards, catalog records, KB owners, communication approvers, version records, and evidence references. |
| Verifiable | Requires localization tests, missing-key checks, safety/redaction review, KB bindings, CI/CD gates, screenshots, support evidence, and approval records. |
| Classifiable | Requires classification for messages, translations, channels, audiences, support articles, telemetry fields, AI responses, and incident communications. |
| Improvable | Uses incidents, support tickets, repeated searches, failed gates, feedback, analytics, and RCA findings to improve wording, KB content, templates, and catalog records. |

