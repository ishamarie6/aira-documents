---
title: "GitNexus Code Intelligence and Impact Analysis Standard"
doc_id: "AIRA-19"
version: "v1.3"
status: "revised"
category: "GitNexus and foundation build"
source_docx: "AIRA_19_GitNexus_Code_Intelligence_and_Impact_Analysis_Standard_v1_3_Review_and_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 19-gitnexus-foundation-build
  - revised
  - aira-19
---



# GitNexus Code Intelligence and Impact Analysis Standard



AIRA

AI-Native Enterprise Platform

GitNexus Code Intelligence and
Impact Analysis Standard

Read-Only Code Intelligence | PR/MR Impact Evidence | AI DevSecOps | System Builder Context | AVCI Always

Version v1.3 - Review and Revised Edition

Status: Draft for Architecture Review Board / CAB / DevSecOps Review

Classification: INTERNAL CONFIDENTIAL

Prepared for: AIRA Software Development, DevSecOps, Security, QA/SDET, Platform Engineering, AI Governance, Knowledge Governance, SRE, and Internal Audit Teams

Prepared by: AIRA Enterprise Architecture, Governance, AI DevSecOps, Security, and Documentation Review Board

Review Date: 2026-06-16

# 1. Document Control
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-019 |
| Document Title | AIRA GitNexus Code Intelligence and Impact Analysis Standard |
| Recommended Version | v1.3 - CI/CD Evidence, MicroFunction, System Builder, and Read-Only Impact Governance Update |
| Source Document Reviewed | 19-AIRA_GitNexus_Code_Intelligence_and_Impact_Analysis_Standard_v1.2_Aligned.docx |
| Supersedes | 19-AIRA_GitNexus_Code_Intelligence_and_Impact_Analysis_Standard_v1.2_Aligned.docx after ARB/CAB approval |
| Classification | INTERNAL CONFIDENTIAL |
| Status | Draft for Architecture Review Board, CAB, DevSecOps, Security, QA/SDET, Platform Engineering, Knowledge Governance, AI Governance, and Internal Audit Review |
| Document Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; DevSecOps Lead; Software Development Lead; Security Architecture; QA/SDET; Platform Engineering; Knowledge Governance; AI Governance; SRE; Internal Audit |
| Primary Audience | Software Developers; DevSecOps Engineers; AI Coding Assistant Owners; System Builder Team; Security Reviewers; QA/SDET; Architecture Reviewers; Internal Audit |
| Review Cadence | Quarterly; unscheduled after GitNexus tool change, repository indexing change, MCP/tool gateway change, AI assistant workflow change, CI/CD gate change, evidence schema change, or security incident |
| Evidence Path | OpenKM Tier-0 / AIRA / DevSecOps / GitNexus-Code-Intelligence / v1.3/ |
| Governing Parents | 01A v1.2; 01 v3.2; 01B v1.2; 02 v5.2; 05 v4.2; 06 v3.2; 11 v3.2; 11A v1.2; 20 v1.2 |
| Related MicroFunction Baseline | 10 v3.3; 10A v2.3; 10B v2.2; 10C v2.2; 10D v2.2; 10E v1.2 |
| External Alignment Checked | NIST SSDF SP 800-218; SLSA v1.2; OWASP ASVS 5.0.0; OpenSSF Scorecard; OpenTelemetry; Open Policy Agent; Apache Kafka concepts |

# 2. Table of Contents Placeholder

Insert a Microsoft Word automatic Table of Contents here before final publication: References > Table of Contents > Automatic Table. Update fields after final pagination.

# 3. Change Summary
| Change Area | v1.3 Improvement |
| --- | --- |
| Authority boundary | Strengthened the rule that GitNexus is read-only, derivative, commit-bound code intelligence. It does not become source truth, architecture authority, security scanner replacement, policy authority, approval authority, merge authority, deployment authority, or production runtime dependency. |
| CI/CD integration | Aligned GitNexus with 20 v1.2 as an evidence-producing PR/MR and pipeline gate, with index freshness, commit SHA binding, classification, retention, and human review. |
| MicroFunction alignment | Added explicit impact-analysis coverage for MicroFunction catalog entries, runtime configuration, assembly templates, step boundaries, outbox, DLQ, replay, idempotency, policy, observability, and compensation paths. |
| System Builder and AI agents | Clarified that System Builder, Codex, Claude, Hermes, and AI agents may use GitNexus only through approved read-only tool scope, SBAC, OPA, Harness/MCP gateway where applicable, prompt redaction, audit, and human approval. |
| Security and privacy | Strengthened controls for secret safety, Restricted content exclusion, repository eligibility, scan-before-indexing, index retention, no production data, no raw credentials, and private/on-prem handling for sensitive repositories. |
| Evidence schema | Expanded evidence fields for repository, branch, commit, index version, freshness, impact scope, affected tests, risk, classification, limitations, waivers, and reviewer decision. |
| Adoption maturity | Defined gate maturity from offline/manual to advisory, warning, selective blocking, and policy-integrated use, with accuracy and false-positive controls. |
| Developer usability | Simplified approved/prohibited use cases and provided implementation-ready rules for PR/MR, CI/CD, incident, Auto-Heal, Auto-Learn, and Auto-Improve workflows. |

# 4. Executive Review Summary

This review confirms that the v1.2 GitNexus standard is fundamentally sound and should be retained. It correctly classifies GitNexus as a governed code-intelligence and impact-analysis layer that supports PR/MR review, affected-test discovery, architecture drift detection, code maps, AI context, and evidence generation. It also correctly prohibits GitNexus from becoming an architecture authority, security scanner replacement, production runtime dependency, or autonomous execution path.

Version v1.3 strengthens GitNexus as part of the AIRA engineering factory after the revised DevSecOps and MicroFunction baseline. GitNexus must support CI/CD evidence packs, System Builder impact analysis, MicroFunction delivery, AI-assisted coding, incident RCA, and Auto-Heal / Auto-Learn / Auto-Improve candidate loops without weakening source authority, human accountability, security gates, or AVCI evidence.

Recommended Review Verdict: Promote v1.3 as the candidate GitNexus standard after ARB, CAB, DevSecOps, Security, AI Governance, Knowledge Governance, and Internal Audit review. Use it initially in advisory and warning modes until freshness accuracy, repository eligibility, false-positive handling, and evidence schema quality are proven.

# 5. Source and Context Alignment Findings
| AIRA Source / Control Area | Required Alignment for AIRA-DOC-019 v1.3 |
| --- | --- |
| 01A Enterprise Architecture Principles | GitNexus findings must reinforce SOLID, Clean Architecture, DDD, ports/adapters, testability, observability, security, reversibility, and AVCI. |
| 01 and 01B AVCI Standards | GitNexus reports must be attributable to repository, branch, commit, index version, owner, classification, reviewer, and evidence path. |
| 02 Engineering Blueprint | GitNexus must analyze code against approved service boundaries, bounded contexts, API/event contracts, runtime flows, and integration topology. |
| 05 Information Nervous System | GitNexus is derivative code intelligence. Git/GitHub/GitLab remains the code golden source; Obsidian and LLM Wiki receive curated summaries and references, not uncontrolled full code copies. |
| 06 CLAUDE.md Reference | AI assistants may consume GitNexus context only through approved repository-local rules, generated adapters, safe prompts, and tool-use declarations. |
| 07 Skills Framework | Access to GitNexus must be controlled by skill, role, classification, repository eligibility, and trust tier. |
| 10 MicroFunction baseline | Impact analysis must detect affected MicroFunctions, catalog entries, runtime config, assembly templates, step contracts, outbox, DLQ, replay, idempotency, policy, and compensation. |
| 11 and 11A DevSecOps Standards | GitNexus supports DevSecOps evidence but does not replace CI, tests, scans, policy checks, CODEOWNERS, ARB/CAB, or human review. |
| 20 CI/CD Evidence Pack Guide | GitNexus output must be attached as read-only impact evidence with commit freshness and limitations in the PR/MR evidence pack. |
| 15 API and Integration Standards | GitNexus must detect affected APIs, clients, contracts, AsyncAPI topics, Kafka producers/consumers, schema impacts, and consumer-risk areas. |
| 16 Database/Flyway Standards | GitNexus impact must include affected migrations, repositories, repositories using database objects, data-access boundaries, and DBA review triggers. |
| 17 Security Standards | GitNexus must never index secrets or production data. It may identify security-sensitive code paths for reviewer attention only. |
| 31/31A Observability Standards | GitNexus access, index refresh, report generation, and agent retrieval must emit safe logs, traces, audit events, and evidence references. |
| 42 AI Agent Controls | Agent access to GitNexus must remain read-only, policy-governed, logged, revocable, and subject to SBAC/OPA and human approval where action follows analysis. |

# 6. Review and Gap Analysis
| Finding Type | Assessment | v1.3 Treatment |
| --- | --- | --- |
| Retain | The v1.2 baseline correctly adopts GitNexus as a controlled, derivative, read-only code-intelligence layer. | Retained as the core mandatory operating principle. |
| Correct | The document had a minor classification inconsistency: INTERNAL INTERNAL CONFIDENTIAL in one control block. | Standardized classification as INTERNAL CONFIDENTIAL. |
| Strengthen | CI/CD integration needed clearer commit freshness, required evidence fields, and gate maturity. | Added GitNexus gate levels, freshness checks, and evidence schema requirements aligned with 20 v1.2. |
| Strengthen | MicroFunction impacts were implied but not complete under the new v3.3/v2.3/v2.2 baseline. | Added mandatory MicroFunction impact-analysis scope. |
| Clarify | GitNexus relationship to Obsidian, LLM Wiki, and source truth needed stronger wording. | Reaffirmed code source truth in Git, derivative summaries in Obsidian, and governed retrieval via Knowledge API/LLM Wiki. |
| Add | System Builder and AI-agent usage needed explicit read-only, SBAC, OPA, Harness/MCP, and human review controls. | Added AI assistant and System Builder integration rules. |
| Add | Security needed stronger scan-before-index, no secret indexing, data classification, retention, and restricted processing rules. | Added repository eligibility, secret safety, DLP, retention, and private/on-prem handling controls. |
| Simplify | Approved/prohibited uses needed concise developer-ready rules. | Added direct approved-use and prohibited-use tables. |

# 7. Revised Full AIRA Document

## 7.1 Mandatory Practice Statement

GitNexus may be used in AIRA only as a governed, read-only, derivative, commit-bound code intelligence and impact-analysis layer. It may help developers, architects, reviewers, DevSecOps, System Builder, and approved AI assistants understand code structure, dependency graphs, call chains, affected tests, blast radius, ownership, architecture drift, and evidence gaps. It must not commit, merge, approve, deploy, mutate files, edit production configuration, execute tools, access secrets, override policy, replace tests, replace scanners, replace human review, or become the source of truth.

A GitNexus report is evidence support. It is not authority. Authority remains with approved source repositories, contracts, tests, policies, CI/CD gates, ADRs/TDLs, CODEOWNERS, ARB/CAB, and named human reviewers.

## 7.2 Purpose

Define how GitNexus is evaluated, adopted, configured, accessed, controlled, audited, and used in AIRA.

Provide a safe model for code intelligence, impact analysis, affected-test discovery, code maps, architecture drift signals, security-sensitive path identification, and PR/MR evidence support.

Ensure GitNexus supports DevSecOps, MicroFunction delivery, System Builder, AI-assisted development, Auto-Heal, Auto-Learn, Auto-Improve, incident RCA, and release readiness without weakening governance.

Prevent GitNexus from becoming a second source of truth, an autonomous engineering actor, a scanner replacement, an approval path, or a production mutation path.

## 7.3 Scope
| In Scope | Out of Scope |
| --- | --- |
| Repository indexing, dependency graphs, code maps, call-chain analysis, ownership maps, affected-test discovery, architecture drift signals, security-sensitive code maps, PR/MR impact summaries, CI/CD evidence attachments, System Builder analysis context, AI assistant read-only context, and incident/improvement analysis. | Write access to repositories, commit creation, merge approval, pull request approval, deployment, production configuration mutation, production secret access, policy override, direct tool execution, replacing security scanners, replacing CI/CD, or replacing human reviewer judgment. |
| GitHub/GitLab repositories, CI artifact stores, approved evidence repositories, controlled GitNexus indexes, Obsidian curated summaries, LLM Wiki/LightRAG retrieval, and AIRA Knowledge API/MCP connectors. | Uncontrolled local folder indexing, personal developer vault indexing, unclassified repository ingestion, production data indexing, secret indexing, raw Restricted content indexing without approved private/on-prem controls. |
| Developer, DevSecOps, Architecture, QA, Security, SRE, DBA, System Builder, AI Governance, and Internal Audit use. | External or unmanaged AI assistants, public model routes, unmanaged MCP servers, or non-approved plugins for sensitive code. |

## 7.4 Authority and Precedence
| Level | Authority | Interpretation |
| --- | --- | --- |
| L0 | Architecture Review Board, CAB, Security Governance, IT Head | Final authority for production-impacting GitNexus adoption, exceptions, blocking gates, restricted indexing, and agent/tool access. |
| L1 | AIRA 01A, 01, 01B, 02, 05, 11, 11A, 20 | Universal architecture, AVCI, knowledge, DevSecOps, evidence, and pipeline authority. |
| L2 | This AIRA-DOC-019 v1.3 Standard | Controls GitNexus role, boundaries, evidence schema, adoption maturity, approved/prohibited uses, and access model. |
| L3 | Repository, CI/CD, CLAUDE.md/AGENTS.md, MCP Gateway, OPA/SBAC, Knowledge API, Evidence Store | Executable controls and operational evidence. |
| L4 | GitNexus reports and derived artifacts | Derivative evidence only. May inform review but cannot override higher authority. |

## 7.5 GitNexus Positioning in AIRA Architecture
| AIRA Layer | GitNexus Role | Non-Negotiable Boundary |
| --- | --- | --- |
| Source code | Reads repository metadata, code graph, package structure, dependencies, and ownership. | Git repository remains source truth. GitNexus index is derivative and rebuildable. |
| DevSecOps | Produces impact reports, affected-test recommendations, drift findings, and evidence summaries. | Does not replace CI/CD, tests, scanners, policy checks, CODEOWNERS, or release approvals. |
| MicroFunction | Identifies impacted MicroFunctions, catalog entries, runtime config, standard steps, outbox/DLQ/replay paths, idempotency, and compensation areas. | Does not change runtime configuration or catalog entries. |
| API and events | Maps affected OpenAPI/AsyncAPI contracts, Kafka topics, Avro schemas, CloudEvents metadata, clients, consumers, and producers. | Does not approve breaking changes or schema evolution. |
| Security | Identifies security-sensitive paths such as auth, policy, secrets handling, logging, PII, admin, AI model routing, and data access. | Does not index secrets or replace SAST/SCA/DAST/secret scanning. |
| AI assistants | Provides read-only context to approved assistants and System Builder through governed adapters. | No write tools, no direct production credentials, no unapproved MCP access, no bypass of SBAC/OPA. |
| Knowledge fabric | Feeds curated code maps and evidence summaries to Obsidian/LLM Wiki. | Full raw codebase is not copied to Obsidian. Summaries must cite exact repository and commit references. |

## 7.6 Approved Use Cases
| Use Case | Required Controls |
| --- | --- |
| PR/MR impact analysis | Repository, branch, base/head commit SHA, changed files, affected packages, affected tests, risk summary, classification, reviewer acknowledgement. |
| Affected-test discovery | Mapped unit, component, contract, integration, architecture, security, replay, and regression tests. Suggestions cannot reduce mandatory test suite. |
| Architecture drift detection | Compare dependency direction, bounded-context boundaries, controller/service/domain boundaries, direct provider calls, and MicroFunction anti-patterns with ArchUnit/Semgrep/CI results. |
| MicroFunction impact map | Identify affected transaction codes, step codes, catalog entries, runtime configuration, idempotency profile, outbox topic, DLQ/replay path, OPA policy, observability envelope, and compensation path. |
| System Builder analysis | Use read-only impact evidence before recommending candidate code, configuration, tests, policies, migrations, or runbooks. |
| AI-assisted development context | Provide controlled context through approved repository rules, read-only MCP/connector, classification, prompt redaction, and AI-use declaration. |
| Incident RCA and Auto-Heal candidate analysis | Identify affected paths, related tests, recurring patterns, and candidate remediation. Fix remains a PR/MR candidate requiring tests and human approval. |
| Release readiness evidence | Attach code map, impact summary, affected tests, drift findings, security-sensitive code map, and limitations to evidence pack. |

## 7.7 Prohibited Uses
| Prohibited Use | Reason / Required Alternative |
| --- | --- |
| Commit, merge, approve PR/MR, deploy, or edit files. | Use human-reviewed PR/MR through CI/CD, CODEOWNERS, and approval gates. |
| Execute tools or mutate environments. | Use Harness/MCP execution paths with SBAC, OPA, dry-run, approval, audit, and rollback. |
| Replace SAST, SCA, secrets scan, DAST, API security tests, OPA tests, contract tests, or architecture fitness functions. | GitNexus may complement but cannot replace controlled tests and scanners. |
| Index secrets, tokens, credentials, private keys, production data, raw Restricted content, or unmanaged repositories. | Secret-scan and classify before indexing; exclude or quarantine sensitive artifacts. |
| Serve stale code graphs as current truth. | Use commit freshness validation and stale-index quarantine. |
| Override CODEOWNERS, ADR/TDL, CAB/ARB, DBA, Security, or human review. | Use GitNexus as evidence support only. |
| Provide unapproved AI assistants with repository context. | Use approved Knowledge API, scoped connector, or MCP gateway with audit and classification. |
| Copy full codebase into Obsidian or LLM Wiki as uncontrolled content. | Store curated summaries, code maps, evidence summaries, and links to exact commits. |

## 7.8 GitNexus Evidence Record Minimum Schema
| Field | Required Content |
| --- | --- |
| evidence_id | Unique GitNexus evidence record identifier. |
| report_type | Code map, impact summary, affected-test map, drift finding, security-sensitive map, incident/RCA support, release-readiness support. |
| repository_ref | Repository URL or internal reference, branch, base commit, head commit, commit SHA, index version, timestamp, and repository owner. |
| freshness_status | Current, reconciled, stale, partial, quarantined, or invalid. Must show match against PR/MR head/base. |
| classification | Repository classification, evidence classification, retention rule, ACL/SBAC rule, model-route eligibility. |
| scope_included | Included services, packages, modules, APIs, events, database objects, MicroFunctions, policies, agents, tests, docs, and environments. |
| scope_excluded | Excluded paths, unsupported languages, generated files, secret areas, binary files, restricted areas, and known blind spots. |
| impact_scope | Affected files, packages, services, contracts, topics, schemas, migrations, policies, tests, MicroFunctions, agents, environments, and runbooks. |
| risk_summary | Blast radius, critical paths, security/data implications, architecture boundary impact, production risk, release risk. |
| test_recommendations | Affected tests, missing tests, contract tests, architecture tests, security tests, replay tests, regression tests, performance tests. |
| architecture_findings | Boundary violations, cross-context coupling, direct provider calls, controller business logic, database leakage, forbidden imports. |
| security_findings | Security-sensitive paths, potential unsafe logging, secrets handling, auth/policy/admin/PII/model-routing impact. This is reviewer guidance only. |
| review_decision | Accepted, acknowledged, requires action, waiver required, blocked, false positive, or deferred with owner. |
| human_checker | Named reviewer or checker who interpreted the report. |
| evidence_refs | PR/MR, CI run, test report, scan report, ADR/TDL, waiver, evidence pack, incident, release record. |
| limitations | Known blind spots, confidence limits, stale areas, manual review required, false-positive notes. |
| improvement_path | Backlog item, test improvement, architecture fitness improvement, knowledge update, or GitNexus tuning item. |

## 7.9 CI/CD and Evidence Pack Integration
| CI/CD Gate | GitNexus Required Behavior | Evidence Output |
| --- | --- | --- |
| Local / Pre-PR | Optional developer-run code map and affected-test estimate. | Developer-attached advisory report or local attestation. |
| PR/MR Opened | Generate read-only impact analysis against base/head commits where available. | GitNexus impact report with commit SHA, classification, affected files, tests, and limitations. |
| Architecture Fitness Gate | Compare GitNexus drift findings with ArchUnit, Semgrep, dependency checks, and CODEOWNERS. | Architecture impact summary and reviewer decision. |
| MicroFunction Gate | Identify affected MicroFunction catalog/config/runtime/outbox/DLQ/replay/policy/observability areas. | MicroFunction impact map and required test recommendations. |
| Security Gate | Identify security-sensitive paths to focus reviewer and scanner attention. | Security-sensitive code map. Not a scanner result. |
| Evidence Finalization | Attach GitNexus summary to evidence pack and PR/MR AVCI summary. | Report hash, storage path, reviewer acknowledgement, freshness status, retention rule. |
| Release Readiness | Confirm GitNexus report corresponds to the released commit and not a stale branch. | Release evidence pack includes GitNexus commit freshness and limitations. |

## 7.10 GitNexus Gate Maturity Path
| Level | Mode | Required Treatment |
| --- | --- | --- |
| G0 | Offline / Manual | Architecture and developer review only. No CI gate. Use for initial familiarization and tool validation. |
| G1 | Advisory | Report attached to PR/MR or evidence pack. Findings inform review but do not block. |
| G2 | Warning | Missing/stale report or high-risk impact requires reviewer acknowledgement, explanation, or backlog item before merge. |
| G3 | Selective Blocking | Approved high-confidence findings may block selected high-risk repositories or change types, such as stale index, boundary violation, missing affected tests, or forbidden dependency. |
| G4 | Policy-Integrated | GitNexus evidence feeds policy-as-code and release readiness under approved deterministic thresholds, false-positive controls, waiver process, and ARB/CAB approval. |

Default initial maturity: G1 Advisory for normal repositories and G2 Warning for high-risk AIRA platform repositories. G3/G4 require accuracy validation, false-positive review, documented thresholds, waivers, and approval.

## 7.11 MicroFunction Impact Analysis Requirements
| Impact Area | Required GitNexus Analysis |
| --- | --- |
| Transaction and step code | Identify affected transaction_code, step_code, catalog function, business function, standard function, and generated runtime entry. |
| Runtime configuration | Identify changed runtime configuration, parameter, feature flag, policy binding, activation row, cache key, and deployment manifest. |
| API and event contracts | Identify related OpenAPI endpoint, AsyncAPI channel, Kafka topic, Avro schema, CloudEvents type, consumer, producer, and compatibility risk. |
| Idempotency and outbox | Identify idempotency key logic, outbox write, event publication, consumer deduplication, DLQ, replay, and compensation impact. |
| Observability envelope | Identify trace/log/metric/audit/error-monitoring coverage and any missing evidence_ref, trace_id, span_id, policy_decision_id, or audit_event_id. |
| Security and policy | Identify affected identity, OPA/SBAC, secrets, classification, tenant isolation, rate limit, abuse-case, DAST/API security, and remediation evidence areas. |
| Resilience | Identify timeout, retry, circuit breaker, bulkhead, fallback, recovery, load/concurrency, and failure-aware transaction paths. |
| Test scope | Recommend unit, component, contract, OPA, integration, replay, concurrency, heavy-load, security, architecture, and regression tests. |

## 7.12 System Builder, AI Assistant, and Agent Use
| Control | Mandatory Rule |
| --- | --- |
| Access model | AI assistants and agents access GitNexus only through approved read-only interface, repository-local rules, AIRA Knowledge API, or governed MCP gateway. |
| SBAC and OPA | Tool access must require skill scope, repository scope, classification eligibility, OPA decision, and audit trail. |
| Prompt safety | Prompted GitNexus context must avoid secrets, raw Restricted data, credentials, tokens, raw production data, and high-risk private content unless approved private/on-prem route exists. |
| Action boundary | AI may recommend, draft, summarize, test, and open candidate PRs where approved. AI may not approve, merge, deploy, mutate production, or bypass checks. |
| Evidence | AI use must record model/tool, prompt intent, retrieved source refs, classification, GitNexus report ref, generated artifact ref, reviewer, and limitations. |
| Human review | A named human must interpret GitNexus findings before they are used as decision evidence for merge, waiver, release, incident closure, or improvement adoption. |

## 7.13 Security, Privacy, Classification, and Retention Controls
| Control Area | Mandatory Rule | Minimum Evidence |
| --- | --- | --- |
| Repository eligibility | Only approved repositories and branches may be indexed. | Repository approval, classification, owner, branch scope. |
| Secret safety | Repositories must be secret-scanned and exclusion rules applied before indexing. | Gitleaks or approved secret scan result, exclusion config, DLP test. |
| Restricted handling | Confidential/Restricted repositories require private/on-prem processing or approved protected route. | Classification approval, ACL, encryption, retention, model-route eligibility. |
| Index retention | Indexes and reports follow data classification, audit, retention, and disposal rules. | Retention record, disposal rule, stale-index quarantine evidence. |
| Network and egress | GitNexus runtime must not make uncontrolled external callbacks for sensitive repositories. | Network policy, egress review, SBOM/SCA result. |
| Access logging | All report generation, context retrieval, and AI-agent access must be logged. | Tool access log, actor/agent ID, trace_id, repo_id, commit_sha. |
| License and supply chain | GitNexus tool binaries, images, plugins, and dependencies must be pinned, scanned, and approved. | SBOM, SCA/SAST result, signature, version pin, exception record. |

## 7.14 Observability and Operational Evidence
| Signal | Minimum Fields |
| --- | --- |
| Logs | event_name, actor_ref, agent_id where applicable, repo_id, branch, commit_sha, index_version, report_type, classification, evidence_ref, safe_error_code. |
| Traces | trace_id, span_id, GitNexus operation, repository scope, duration_ms, result, failure point, evidence_ref. |
| Metrics | index freshness, report generation latency, stale-index count, failed-index count, report coverage, false-positive trend, waiver trend, security exclusion count. |
| Audit | who requested report, why, source ticket/PR, repository scope, policy decision, reviewer, retention, classification, outcome. |
| Dashboards | GitNexus health, indexing freshness, repository coverage, stale reports, high-risk impacts, findings by severity, waiver aging, AI retrieval usage. |
| Alerts | stale index used in CI, secret detected before indexing, unauthorized repository access, failed policy check, Restricted content routing violation. |

## 7.15 Auto-Heal, Auto-Learn, and Auto-Improve Candidate Loop

GitNexus may support Auto-Heal, Auto-Learn, and Auto-Improve by identifying affected files, dependency paths, related tests, recurring weak areas, architecture drift, and candidate refactoring opportunities. It must not directly fix, promote, or deploy. All improvement outputs remain candidate artifacts until reviewed through the PR/MR and evidence process.
| Loop Step | Required Behavior |
| --- | --- |
| Issue detection | Detection may originate from CI failure, incident, Sentry issue, security finding, test failure, GitNexus drift, observability alert, or user feedback. |
| Evidence retrieval | Retrieve GitNexus impact, code map, affected tests, CI logs, traces, scans, policy decisions, and related incidents. |
| Candidate proposal | Generate candidate remediation or learning item with assumptions, affected artifacts, risks, tests, rollback, and limitations. |
| Validation | Run deterministic tests, architecture fitness, security checks, contract checks, replay/concurrency checks where applicable. |
| Human approval | Named maker/checker/approver decides whether the candidate is accepted, revised, deferred, or rejected. |
| Knowledge update | Approved lessons become curated Obsidian/LLM Wiki knowledge with source references, not raw code dumps. |

## 7.16 Anti-Patterns

Using GitNexus output as authority when source, tests, contracts, or human review disagree.

Using stale GitNexus index output in CI/CD without freshness validation.

Granting GitNexus, MCP, or AI assistant write access to repositories or environments.

Copying full source code into Obsidian instead of storing curated summaries and exact references.

Indexing secrets, credentials, raw production data, or Restricted artifacts without approved protected handling.

Suppressing test, scan, or architecture fitness requirements because GitNexus reported low impact.

Allowing AI assistants to use GitNexus context without SBAC, OPA, classification, prompt safety, and audit.

Using GitNexus as an undocumented shadow inventory instead of a governed evidence-producing code-intelligence layer.

## 7.17 Acceptance Criteria

GitNexus is registered as a governed, read-only, derivative code-intelligence capability with owner, version, scope, classification, retention, and operating model.

No write, merge, approval, deployment, production mutation, or secret access capability exists in GitNexus configuration, tokens, MCP tools, or agent connectors.

Repository eligibility, classification, branch scope, secret scan, exclusion rules, retention, and access-control evidence exist before indexing.

Every GitNexus report used in PR/MR, CI/CD, incident, or release evidence contains repository, branch, commit SHA, index version, freshness, classification, impact scope, limitations, and human checker decision.

CI/CD integration starts at advisory/warning maturity and promotes to blocking only after accuracy, freshness, false-positive, waiver, and approval controls are proven.

MicroFunction impact analysis covers catalog, runtime configuration, standard steps, business steps, OpenAPI/AsyncAPI, Kafka, Avro, CloudEvents, outbox, idempotency, DLQ, replay, policy, observability, resilience, and compensation impacts.

System Builder and AI assistant use is read-only, SBAC/OPA-governed, audited, classified, and subject to human review before action.

GitNexus evidence is stored in approved evidence repositories and projected to Obsidian/LLM Wiki only as curated summaries with exact source references.

Operational dashboards show GitNexus health, index freshness, access logs, stale report alerts, report coverage, and high-risk findings.

All non-conformances, waivers, false positives, incidents, and improvements feed an accountable backlog and review cadence.

## 7.18 RACI
| Activity | Architecture | DevSecOps | Development | Security | QA/SDET | Platform/SRE | AI Governance | Knowledge Governance | Internal Audit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Approve standard | A | C | C | C | C | C | C | C | C |
| Configure GitNexus read-only access | C | A/R | C | C | I | R | C | I | I |
| Approve repository eligibility | A | R | C | R | I | C | C | C | I |
| Maintain evidence schema | A | R | C | C | C | C | C | C | C |
| Use in PR/MR review | C | C | A/R | C | R | I | I | I | I |
| Security and privacy review | C | C | I | A/R | I | C | C | C | I |
| AI assistant integration | C | C | I | C | I | C | A/R | C | I |
| Knowledge projection | C | C | C | C | I | I | C | A/R | C |
| Control testing | C | C | I | C | C | C | C | C | A/R |

## 7.19 AVCI Compliance Summary
| AVCI Property | How v1.3 Satisfies It |
| --- | --- |
| Attributable | GitNexus reports include repository, branch, commit SHA, index version, timestamp, owner, actor, agent where applicable, reviewer, PR/MR, CI run, and evidence path. |
| Verifiable | Reports are bound to source commits, freshness checks, CI/CD evidence, tests, scanners, architecture fitness, human review, and limitations. |
| Classifiable | Repository eligibility, data classification, index handling, retention, ACL, model-route eligibility, and Restricted-content controls are mandatory. |
| Improvable | Findings, false positives, stale indexes, missing tests, architecture drift, security-sensitive paths, incidents, and reviewer feedback feed backlog, tuning, and controlled improvement loops. |

# 8. Simplification Recommendations
| Recommendation | Rationale |
| --- | --- |
| Use one standard GitNexus evidence schema. | Prevents every team from inventing different impact report fields. |
| Start with advisory mode. | Allows learning and tuning before blocking merges. |
| Auto-select report type based on changed paths. | Reduces developer burden and ensures MicroFunction, API, database, policy, and security paths get the right analysis. |
| Publish concise PR/MR summaries. | Reviewers need affected areas, tests, risks, and limitations, not raw graph dumps. |
| Separate GitNexus from scanners. | Avoids false confidence; security and supply-chain gates remain authoritative. |
| Keep Obsidian summaries small. | Preserves knowledge quality and avoids duplicating the full codebase. |

# 9. Automation Recommendations
| Automation Area | Recommended Control |
| --- | --- |
| Repository inventory | Maintain GitNexus repository eligibility register with owner, classification, indexed branches, exclusions, retention, and evidence path. |
| Index freshness | Automatically compare GitNexus index commit SHA to PR/MR base/head and quarantine stale reports. |
| Path-based analysis | Trigger MicroFunction, API/event, database, security, policy, AI-agent, or documentation impact reports based on changed paths and manifests. |
| Evidence manifest generation | Automatically generate report hash, report path, freshness status, impact scope, test recommendations, and limitations. |
| Secret and Restricted content exclusion | Block indexing until secret scans and classification checks pass. |
| CI/CD integration | Attach GitNexus summaries to PR/MR evidence packs in G1/G2 mode before any blocking adoption. |
| False-positive tracking | Track reviewer decisions to tune future rules and avoid over-blocking. |
| AI assistant retrieval control | Require Knowledge API/MCP authorization, SBAC, OPA, prompt redaction, and audit logging for GitNexus context retrieval. |
| Dashboarding | Publish index freshness, coverage, stale reports, high-risk impact count, warning/blocking trends, and evidence completeness. |
| Knowledge projection | Summarize approved GitNexus outputs into Obsidian/LLM Wiki with exact repository/commit references and classification. |

# 10. Review Queue Control Register
| Sequence | File Name | Pack | Current Version | Recommended Version | Review Status | Priority | Dependency | Action Required | Next Step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 01A-AIRA_Enterprise_Architecture_Principles_SOLID_and_Fitness_Function_Standard_v1.1_final.docx | Pack 01 | v1.1 | v1.2 | Completed / Revised | P0 | Foundation | Completed | Candidate canonical 01A v1.2 |
| 2 | 01-AIRA_AVCI_Engineering_Standard_v3.1_Aligned.docx | Pack 01 | v3.1 | v3.2 | Completed / Revised | P0 | 01A | Completed | Candidate canonical 01 v3.2 |
| 3 | 01B-AIRA_AVCI_Evidence_Audit_Traceability_and_Control_Standard_v1.1.docx | Pack 01 | v1.1 | v1.2 | Completed / Revised | P0 | 01/01A | Completed | Candidate canonical 01B v1.2 |
| 4 | 02-AIRA_Engineering_Blueprint_v5.1_Aligned.docx | Pack 01 | v5.1 | v5.2 | Completed / Revised | P0 | 01A/01/01B | Completed | Candidate canonical 02 v5.2 |
| 5 | 03-AIRA_Developer_Guide_v4.1_Aligned.docx | Pack 01 | v4.1 | v4.2 | Completed / Revised | P1 | 02 | Completed | Candidate canonical 03 v4.2 |
| 6 | 04-AIRA_Technology_Stack_v9.1_Aligned.docx | Pack 01 | v9.1 | v9.2 | Completed / Revised | P1 | 03 | Completed | Candidate canonical 04 v9.2 |
| 7 | 05-AIRA_AI_Native_Information_Nervous_System_v4.1_Aligned.docx | Pack 01 | v4.1 | v4.2 | Completed / Revised | P1 | 04 | Completed | Candidate canonical 05 v4.2 |
| 8 | 06-AIRA_CLAUDE_MD_Reference_v3.1_Aligned.docx | Pack 01 | v3.1 | v3.2 | Completed / Revised | P1 | 05 | Completed | Candidate canonical 06 v3.2 |
| 9 | 07-AIRA_AI_DevSecOps_Skills_Framework_v3.1_Aligned.docx | Pack 02 | v3.1 | v3.2 | Completed / Revised | P1 | 06 | Completed | Candidate canonical 07 v3.2 |
| 10 | 08-AIRA_Unit_Testing_Standard_v3.1_Aligned.docx | Pack 02 | v3.1 | v3.2 | Completed / Revised | P1 | 07 | Completed | Candidate canonical 08 v3.2 |
| 11 | 08A-AIRA_AI_Assisted_Unit_Testing_Maker_Checker_Prompt_Standard_v1.0.docx | Pack 02 | v1.0 | v1.1 | Completed / Revised | P1 | 08 | Completed | Candidate canonical 08A v1.1 |
| 12 | 09-AIRA_Greenfield_Environment_Standard_v3.1_Aligned.docx | Pack 02 | v3.1 | v3.2 | Completed / Revised | P1 | 08A | Completed | Candidate canonical 09 v3.2 |
| 13 | 10-AIRA_MicroFunction_Framework_v3.1_Aligned.docx | Pack 02 | v3.1 | v3.3 | Completed / Regenerated | P0 | 09 | Completed | Candidate canonical 10 v3.3 |
| 14 | 10A-AIRA_MicroFunction_Design_and_Development_Guide_v2.1_Aligned.docx | Pack 02 | v2.1 | v2.3 | Completed / Regenerated | P0 | 10 | Completed | Candidate canonical 10A v2.3 |
| 15 | 10B-AIRA_MicroFunction_Framework_Implementation_Standard_v2.1_Aligned.docx | Pack 02 | v2.1 | v2.2 | Completed / Revised | P0 | 10/10A | Completed | Candidate canonical 10B v2.2 |
| 16 | 10C-AIRA_MicroFunction_Sequence_Diagrams_and_Mermaid_Reference_v2.1_Aligned.docx | Pack 03 | v2.1 | v2.2 | Completed / Revised | P1 | 10/10A/10B | Completed | Candidate canonical 10C v2.2 |
| 17 | 10D-AIRA_MicroFunction_Standard_Function_Catalog_and_Assembly_Templates_v2.1_Aligned.docx | Pack 03 | v2.1 | v2.2 | Completed / Revised | P0 | 10C | Completed | Candidate canonical 10D v2.2 |
| 18 | 10E-AIRA_MicroFunction_Backend_Service_Generation_and_Runtime_Configuration_Standard_v1.1.docx | Pack 03 | v1.1 | v1.2 | Completed / Revised | P0 | 10D | Completed | Candidate canonical 10E v1.2 |
| 19 | 11-AIRA_AI_Native_DevSecOps_Standard_v3.1_Aligned.docx | Pack 03 | v3.1 | v3.2 | Completed / Revised | P0 | 10E | Completed | Candidate canonical 11 v3.2 |
| 20 | 11A-AIRA_DevSecOps_Governance_and_Evidence_Control_Standard_v1.1.docx | Pack 03 | v1.1 | v1.2 | Completed / Revised | P0 | 11 | Completed | Candidate canonical 11A v1.2 |
| 21 | 20-AIRA_CICD_Pipeline_and_Evidence_Pack_Implementation_Guide_v1.1_Aligned.docx | Pack 05 | v1.1 | v1.2 | Completed / Revised | P0 | 11/11A/MicroFunction baseline | Completed | Candidate canonical 20 v1.2 |
| 22 | 19-AIRA_GitNexus_Code_Intelligence_and_Impact_Analysis_Standard_v1.2_Aligned.docx | Pack 05 | v1.2 | v1.3 | Completed / Revised | P1 | 20 | Completed | Candidate canonical 19 v1.3 |
| 23 | 15-AIRA_API_and_Integration_Contract_Standard_v2.1_Aligned.docx | Pack 04 | v2.1 | v2.2 | Next for Review | P0 | MicroFunction/DevSecOps/GitNexus baseline | Review and align | Review next |

# 11. Next Recommended Document

Recommended next document: 15-AIRA_API_and_Integration_Contract_Standard_v2.1_Aligned.docx, to be reviewed and revised as v2.2.

Reason: The MicroFunction and DevSecOps baselines now explicitly depend on contract-first APIs and eventing. The API and Integration Contract Standard should be reviewed before database, security, observability, Dynamic Workspace, System Builder, and PoC documents so OpenAPI, AsyncAPI, Kafka, Avro, CloudEvents, idempotency, error semantics, schema evolution, consumers, DLQ, replay, and evidence contracts are governed consistently.

# 12. External Source Register
| External Reference | Use in v1.3 Alignment |
| --- | --- |
| NIST SP 800-218 Secure Software Development Framework | Used to align secure development, verification, vulnerability response, and evidence discipline. |
| SLSA Specification v1.2 | Used to align provenance, artifact integrity, and supply-chain evidence expectations. |
| OWASP ASVS 5.0.0 | Used to align application and API security verification expectations. |
| OpenSSF Scorecard | Used to align dependency and repository security-health review concepts. |
| OpenTelemetry | Used to align logs, metrics, traces, observability signals, and trace correlation. |
| Open Policy Agent | Used to align policy-as-code and authorization decision evidence. |
| Apache Kafka documentation | Used to align eventing, consumers, replay, DLQ, and operational evidence concepts. |

