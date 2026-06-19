---
title: "Repository Bootstrap and Golden Source Implementation Guide"
doc_id: "AIRA-18"
version: "v1.2"
status: "revised"
category: "Repository bootstrap and golden source"
source_docx: "AIRA_18_Repository_Bootstrap_and_Golden_Source_Implementation_Guide_v1_2_Review_and_Revised.docx"
converted_on: "2026-06-19"
tags:
  - aira
  - 18-repository-bootstrap-golden-source
  - revised
  - aira-18
---



# Repository Bootstrap and Golden Source Implementation Guide



AIRA
AI-Native Enterprise Platform

Repository Bootstrap and Golden Source Implementation Guide

Repository Structure | Branch Protection | CODEOWNERS | Devcontainer | Golden Source | AGENTS.md / CLAUDE.md | Evidence-First Bootstrap

Version v1.2 - Review and Revised

Status: Draft for ARB, DevSecOps, Security, Platform Engineering, AI Governance, and Team Review

Classification: INTERNAL CONFIDENTIAL

Prepared for: AIRA Software Development, DevSecOps, Security, Platform Engineering, QA/SDET, AI Governance, SRE, DBA, and Internal Audit Teams

# Document Control
| Field | Value |
| --- | --- |
| Document ID | AIRA-DOC-018 |
| Document Title | AIRA Repository Bootstrap and Golden Source Implementation Guide |
| Recommended Version | v1.2 |
| Source Document Reviewed | 18-AIRA_Repository_Bootstrap_and_Golden_Source_Implementation_Guide_v1.1_Aligned.docx |
| Supersedes | 18-AIRA_Repository_Bootstrap_and_Golden_Source_Implementation_Guide_v1.1_Aligned.docx, upon approval |
| Status | Draft for ARB, DevSecOps, Security, Platform Engineering, AI Governance, and Team Review |
| Classification | INTERNAL CONFIDENTIAL |
| Document Owner | Solutions Architecture Office / IT Head |
| Co-Owners | Enterprise Architecture; DevSecOps Lead; Platform Engineering; Security Architecture; Software Development Lead; QA/SDET; AI Engineering; SRE; DBA; Internal Audit |
| Primary Audience | Developers, DevSecOps, Security Administrators, Platform Engineers, AI Engineers, Repository Maintainers, System Builder operators, SRE, QA/SDET, DBA, and Internal Audit |
| Review Date | 2026-06-16 |
| Review Cadence | Quarterly; unscheduled after material toolchain, repository, branch protection, Golden Source, AI assistant, security, CI/CD, or evidence model change |
| Evidence Path | OpenKM Tier-0 / AIRA / Evidence / Repository-Bootstrap-Golden-Source / v1.2 / |

## Related AIRA Documents
| Ref | Document | Relationship |
| --- | --- | --- |
| 01A / 01 / 01B | Architecture Principles, AVCI, Evidence Control | Enterprise design principles, evidence, classification, audit, traceability, and improvement rules |
| 02 / 03 / 04 / 05 / 06 | Blueprint, Developer Guide, Technology Stack, Information Nervous System, CLAUDE.md | Build-ready architecture, developer workflow, approved toolchain, source authority, and AI rules of engagement |
| 07 / 08 / 08A / 09 | Skills, Testing, Maker-Checker Testing, Greenfield Environment | SBAC skills, test evidence, AI-assisted testing, and workstation/devcontainer readiness |
| 10-10E | Updated MicroFunction Baseline | Configure-first runtime assembly, catalog, backend generation, contracts, evidence, outbox, DLQ, replay, observability, and resilience |
| 11 / 11A / 20 | DevSecOps and CI/CD Evidence Pack | Pipeline, security gates, SBOM/provenance, scan evidence, and promotion gates |
| 15 / 15A | API and Contract-First Standards | OpenAPI, AsyncAPI, Kafka, Avro, CloudEvents, schema evolution, and generated code boundaries |
| 16 / 16A / 16B | Database and Flyway Governance | Flyway-only database changes, RLS, seed data, migrations, and database evidence |
| 17 / 17A | Security and Access Control | Keycloak/OIDC, OPA/SBAC, Vault/OpenBao, secrets hygiene, fail-closed implementation |
| 19 | GitNexus v1.3 | Read-only, derivative, commit-bound code intelligence and impact evidence |
| 21A / 25 / 26B | Knowledge Control, Golden Source, Knowledge Automation | Source authority, Obsidian projection, LLM Wiki indexing, and controlled knowledge automation |
| 41B / 44 | System Builder Standards | Governed generation, PR/MR-ready artifacts, no direct production mutation, and evidence-first change control |

# Table of Contents Placeholder

Insert a Microsoft Word automatic Table of Contents here before controlled publication. Suggested TOC depth: Heading 1 through Heading 3. Use References > Table of Contents > Automatic Table, then Update Field before final distribution.

# 1. Executive Review Summary

The v1.1 source document is structurally sound and should be retained as the repository bootstrap baseline. It already defines repository structure, branch protection, CODEOWNERS, devcontainer, Golden Source, and evidence-first bootstrap as mandatory AIRA controls. Version v1.2 strengthens the guide so every new or regenerated AIRA repository becomes a governed engineering workspace from Day 0.

This revision aligns the repository bootstrap model with the newly revised MicroFunction, DevSecOps, CI/CD Evidence Pack, GitNexus, API, database/Flyway, security, Information Nervous System, CLAUDE.md/AGENTS.md, and Golden Source controls. Repository bootstrap is now treated as a controlled supply-chain and evidence boundary, not a convenience setup task.
| Review Decision | v1.2 Treatment |
| --- | --- |
| Retain | Repository skeleton, branch protection, CODEOWNERS, devcontainer, Golden Source registry, pre-commit hooks, CI/CD gates, and evidence-first onboarding. |
| Correct | Update references to revised AIRA baselines, including MicroFunction v3.3 family, DevSecOps v3.2, CI/CD evidence v1.2, GitNexus v1.3, API v2.2, Flyway governance, and security v2.2. |
| Strengthen | Add mandatory AGENTS.md / CLAUDE.md alignment, System Builder generation boundaries, AI-agent repository access controls, contract folders, Flyway folders, evidence manifests, GitNexus index metadata, and supply-chain provenance expectations. |
| Simplify | Express bootstrap as a staged B0-B12 execution path with clear pass/fail gates. |
| Govern | No repository is ready for AIRA development unless it has owner, classification, source authority, branch protections, CODEOWNERS, AI rules, CI strict mode, security gates, and evidence path. |

# 2. Source and Context Alignment
| Alignment Area | Mandatory Repository Meaning |
| --- | --- |
| Golden Source Authority | Git is authoritative for source code, tests, contracts, policies, migrations, IaC, devcontainers, CI/CD definitions, prompt adapters, and generated artifacts pending review. Obsidian and LLM Wiki are curated projections unless explicitly approved as source for a specific artifact. |
| Security and Access Control | Repository bootstrap must enforce least privilege, named ownership, CODEOWNERS, branch protection, signed or protected commits where feasible, secret scanning, dependency governance, and fail-closed CI gates. |
| AI-Assisted Development | Repository-local AI behavior must derive from approved CLAUDE.md and AGENTS.md rules. AI assistants may draft or analyze but must not bypass CI, CODEOWNERS, security gates, or human approval. |
| MicroFunction Baseline | Repository layout must include contracts, catalog/configuration, backend services, adapters, tests, observability, evidence, outbox/DLQ/replay, and resilience folders required by the MicroFunction family. |
| DevSecOps and CI/CD | Bootstrap must include pre-commit hooks, CI strict mode, SAST/SCA/secrets/IaC/container scans, unit/contract/API/security tests, SBOM/provenance, GitNexus evidence, and PR/MR AVCI summary. |
| API and Database Governance | Contracts, OpenAPI/AsyncAPI schemas, Avro/JSON Schema, CloudEvents, Flyway migrations, seed data, and database policy artifacts must be versioned and reviewed in the repository. |
| Knowledge and Evidence | Repository metadata must support OpenKM evidence paths, Obsidian projection, LLM Wiki indexing, freshness manifests, and source-to-evidence traceability. |

# 3. Review and Gap Analysis
| Finding Type | Board Finding |
| --- | --- |
| Already Correct | The v1.1 baseline correctly defines repository bootstrap as evidence-first and includes repository structure, branch protection, CODEOWNERS, devcontainer, CI/CD, dependency governance, AI-assisted development, and Golden Source registry. |
| Outdated or Weak | References to older Pack 01/02 baselines needed alignment to the revised 2026 review sequence and current document versions generated in this review cycle. |
| Missing Detail | More explicit implementation guidance was needed for System Builder-generated repositories, AGENTS.md adapters, GitNexus metadata, contract folders, MicroFunction runtime configuration, event/schema folders, and Flyway-only database assets. |
| Simplification Need | Developers need a concise bootstrap checklist that clearly says when a repository is or is not ready for development. |
| Enterprise Strengthening | Repository creation is now treated as a supply-chain, access-control, evidence, and knowledge-governance event. |
| Automation Support | The guide now supports future scripts for repository inventory, branch protection validation, Golden Source manifest validation, duplicate rule detection, template drift checks, and evidence completeness checks. |

# 4. Revised Full AIRA Document

## 4.1 Purpose

This guide defines how AIRA repositories are created, initialized, protected, connected to Golden Source, prepared for AI-assisted development, and made ready for governed engineering work. It provides a practical implementation baseline for repository maintainers, developers, DevSecOps, security, platform engineering, AI engineering, and System Builder operators.

## 4.2 Scope
| Scope Type | Description |
| --- | --- |
| In Scope | Repository creation, naming, classification, branch protection, CODEOWNERS, PR/MR templates, issue templates, CLAUDE.md, AGENTS.md, devcontainers, pre-commit hooks, CI/CD templates, evidence paths, contract folders, MicroFunction folders, Flyway folders, IaC folders, policy folders, and Golden Source registry. |
| In Scope | System Builder repository scaffolding proposals, AI-assisted code generation boundaries, GitNexus indexing metadata, SBOM/provenance, secrets scanning, CI strict mode, and evidence pack requirements. |
| Out of Scope | Manual production deployment, direct production mutation, unmanaged personal repositories, unmanaged AI rules, local-only source copies, direct model-provider calls, direct secret storage, and repository setup outside approved templates and review gates. |

## 4.3 Mandatory Practice Statement

No AIRA repository is ready for development until it has a named owner, classification, bounded context or platform capability, Golden Source registry entry, protected main branch, CODEOWNERS, repository-local AI rules, devcontainer or documented toolchain baseline, security scanning, CI strict mode, PR/MR AVCI template, evidence path, and ready-to-develop sign-off. A repository that can compile but cannot prove source authority, security gates, evidence, reversibility, and human accountability is not AIRA-ready.

## 4.4 Bootstrap Operating Principles
| Principle | Mandatory Meaning |
| --- | --- |
| Source authority first | Repository source, contracts, policies, migrations, tests, CI/CD, devcontainers, prompts, and IaC must be traceable to approved Golden Source. |
| Secure by default | Branch protection, least privilege, CODEOWNERS, secret scanning, dependency scanning, and security gates are enabled before feature work. |
| Evidence by construction | Bootstrap produces evidence: repository metadata, owner, classification, initial commit, branch rules, CI run, scan results, devcontainer build, and sign-off. |
| AI governed locally | CLAUDE.md and AGENTS.md adapters define allowed AI behavior. AI-generated changes must be visible, reviewable, and CI-validated. |
| Reproducibility | Toolchains are pinned through approved devcontainers, Gradle/Maven/Node configuration, package locks, container digests, and CI evidence. |
| No shadow setup | Developers may not depend on undocumented local tools, unmanaged packages, private scripts, personal AI accounts, or untracked configuration. |
| Fail closed | Missing source authority, branch protection, policy, evidence, identity, secret scan, or CI validation blocks protected development and promotion. |

## 4.5 Golden Source Architecture
| Source Layer | Authority Boundary |
| --- | --- |
| Git Repository | Authoritative for source code, tests, API/event contracts, policies, Flyway migrations, IaC, devcontainers, CI/CD workflows, prompt adapters, generated artifacts under review, and repository evidence manifests. |
| OpenKM / Approved DMS | Authoritative for approved signed documents, evidence packs, controlled records, approvals, waivers, incident records, and audit artifacts. |
| Obsidian | Curated knowledge projection for standards, ADRs, runbooks, reviewed summaries, diagrams, and team guidance. It must reference authoritative sources. |
| LLM Wiki / Retrieval Index | Derivative retrieval layer with classification, provenance, freshness, SBAC, and conflict checks. It is not authority by itself. |
| GitNexus | Read-only, derivative, commit-bound code intelligence and impact evidence. It cannot commit, merge, approve, deploy, or mutate production. |
| Package/Image Registries | Approved source for versioned dependencies, container images, internal packages, artifact digests, SBOM, provenance, and promotion history. |

## 4.6 Repository Topology and Naming Standard
| Topology Rule | Required Treatment |
| --- | --- |
| Monorepo Allowed | A controlled monorepo may be used for early foundation work when it simplifies governance. Bounded contexts must remain visible through top-level folders, CODEOWNERS, CI path filters, and architecture fitness checks. |
| Multi-Repo Allowed | Separate repositories may be used for mature bounded contexts, platform services, contracts, documentation, IaC, and agents when ownership and promotion controls are clear. |
| Naming Format | Repository names should use aira-{bounded-context}-{capability}, aira-platform-{capability}, aira-contracts, aira-docs, aira-infra, or another ARB-approved convention. |
| Classification | Each repository must declare classification ceiling and retrieval eligibility. Restricted repositories require elevated access, stronger logging, and restricted AI retrieval. |

## 4.7 Standard Repository Layout
| Path | Required Content |
| --- | --- |
| /.github or /.gitlab | Workflows, issue templates, PR/MR templates, CODEOWNERS, security policy, dependabot/renovate rules, and repository governance files. |
| /contracts | OpenAPI, AsyncAPI, Avro/JSON Schema, CloudEvents, evidence contracts, agent/tool contracts, provisioning contracts, and compatibility tests. |
| /services | Backend services, MicroFunction coordinators, adapters, ports, application services, and domain code. |
| /microfunctions | Catalog entries, runtime configuration, assembly templates, activation records, validation schemas, and MicroFunction evidence templates. |
| /db/flyway | Flyway migrations, seed data, RLS policies, views, extensions, reference data, outbox/DLQ/replay schema, and migration tests. |
| /policies | OPA/Rego, SBAC catalogs, policy tests, authorization schemas, admission policies, and model/tool routing policies. |
| /frontend | Frontend workspace code, typed API clients, component tests, accessibility tests, and policy-aware UI bindings. |
| /infra | IaC, Helm/Kustomize, devcontainer build assets, environment manifests, observability config, and rollback/teardown scripts. |
| /tests | Unit, component, contract, integration, security, authenticated DAST, E2E, performance, resilience, and regression tests. |
| /evidence | Evidence manifests and generated summaries only. Raw official evidence should be stored in OpenKM or approved evidence stores and referenced by evidence_ref. |
| /docs | Approved or draft repository-local documentation, ADRs, TDLs, runbooks, generated diagrams, and Obsidian projection source where applicable. |

## 4.8 Branching, Protection, and CODEOWNERS
| Branch / Control | Required Treatment |
| --- | --- |
| main | Protected. Requires PR/MR, required checks, review, CODEOWNERS where applicable, signed evidence, no force push, no deletion, and no direct push except approved break-glass. |
| release/* | Protected. Requires release evidence, CAB or delegated approval where applicable, rollback plan, and tagged artifact provenance. |
| feature/* | Developer or AI-assisted candidate work. Must not contain production secrets, real customer data, or unapproved generated artifacts. |
| hotfix/* | Allowed only for approved incident or urgent remediation. Requires issue link, security classification, tests, evidence, rollback/forward-fix plan, and post-fix review. |
| CODEOWNERS | Must cover architecture, security, API/contracts, database/Flyway, MicroFunction, DevSecOps, frontend, AI, observability, documentation, and evidence paths. |

## 4.9 Initial File Baseline
| Required File | Minimum Content |
| --- | --- |
| README.md | Purpose, owner, classification, bounded context, build/run/test instructions, evidence path, support model, and source authority statement. |
| CODEOWNERS | Named review owners by folder and artifact type. High-risk folders require architecture/security/DBA/DevSecOps owners. |
| CLAUDE.md | Canonical repository-local AI rules derived from AIRA standards. Must not weaken central AIRA instructions. |
| AGENTS.md | Tool-neutral AI-agent adapter generated from CLAUDE.md and approved System Builder/AI-agent controls. |
| .devcontainer/devcontainer.json | Pinned development environment metadata and reproducible toolchain baseline. |
| .pre-commit-config.yaml | Secret scan, formatting, linting, policy, contract, and metadata validation where applicable. |
| pull_request_template.md | AVCI summary, tests, scans, GitNexus impact, AI usage, rollback, and evidence requirements. |
| contract-register.yaml | API/event/schema/evidence/agent/provisioning contract ownership, classification, compatibility, and evidence fields. |
| golden-source-register.yaml | Approved sources, package registries, image digests, model aliases, toolchain versions, and evidence paths. |
| evidence-manifest.yaml | Evidence references for CI, scans, tests, approvals, SBOM, provenance, GitNexus, and deployment readiness. |

## 4.10 Devcontainer and Workstation Integration

AIRA repositories must prefer reproducible devcontainers or an approved workstation profile. The devcontainer must use approved base images, pinned tool versions, no production secrets, no production data, and no unrestricted cloud or production access. Java, Node, Gradle/Maven, Docker tooling, OPA, contract tools, security scanners, and test utilities must be declared through Golden Source rather than hidden local installation steps.
| Area | Required Treatment |
| --- | --- |
| Runtime Baseline | Java 25 LTS for backend development; Java 21 only by waiver with risk, owner, compensating control, and exit plan. |
| Package Baseline | Pinned dependency versions, lock files, approved registries, SCA scan, license policy, and update workflow. |
| Security Baseline | No secrets in devcontainer, no production data, least-privilege credentials, secret scanning, and classification-safe local fixtures. |
| Evidence Baseline | Devcontainer build evidence, image digest, SBOM where applicable, toolchain versions, and first CI run. |

## 4.11 CI/CD, Pre-Commit, and Evidence Gates
| Gate | Required Checks |
| --- | --- |
| Pre-Commit | Format, lint, secret scan, contract lint, YAML/JSON validation, policy test, and metadata validation where practical. |
| Build and Test | Compile, unit, component, contract, API, event, OPA policy, migration, MicroFunction catalog/config, frontend, and architecture fitness tests. |
| Security | SAST, SCA, secrets, container, IaC, API security, authenticated DAST for applicable environments, abuse-case tests, and remediation evidence. |
| Supply Chain | SBOM, provenance, artifact digest, image digest, signed or attested artifacts where supported, and dependency source verification. |
| GitNexus | Read-only impact analysis, code map, affected tests, architecture drift, ownership map, and security-sensitive path evidence. |
| Promotion | Merge and deployment blocked when required checks, owner review, evidence pack, classification, rollback, or approvals are missing. |

## 4.12 Dependency, Package, Image, and Artifact Governance
| Artifact Type | Required Control |
| --- | --- |
| Dependencies | Use approved registries, lock files, SCA, license checks, vulnerability thresholds, and upgrade evidence. Do not add libraries by convenience without design review. |
| Images | Use approved base images, digest pinning, vulnerability scanning, SBOM, provenance, and rebuild cadence. |
| Artifacts | Generated artifacts are derivative and must be traceable to source, contract, prompt, tool version, branch, commit, and CI run. |
| Model Aliases and AI Tools | Model aliases, prompt adapters, guardrail versions, and tool routes must be registry-backed and must not be embedded as uncontrolled local configuration. |

## 4.13 AI-Assisted Development and CLAUDE.md / AGENTS.md Enforcement
| AI Control | Required Treatment |
| --- | --- |
| CLAUDE.md | Repository-local canonical AI instructions for coding assistants. Must derive from AIRA central standards and include forbidden actions. |
| AGENTS.md | Tool-neutral adapter for Codex, Claude Code, Hermes, System Builder agents, IDE assistants, and controlled automation. Must not weaken CLAUDE.md. |
| AI Use Declaration | Every PR/MR with AI assistance records tool, prompt source, model route, files affected, human checker, tests, and evidence. |
| No Direct Authority | AI may recommend, draft, analyze, generate tests, or prepare PRs. It may not approve its own output, bypass checks, receive production credentials, or mutate production. |
| Context Safety | AI retrieval must be classification-aware, source-cited, freshness-checked, and avoid secrets, raw PII, raw restricted records, and unapproved production evidence. |

## 4.14 GitHub / GitLab Configuration Guide

Create repository only from approved AIRA template or System Builder-generated scaffold PR.

Set repository owner, classification, bounded context, support path, and evidence path before first feature branch.

Enable branch protection for main and release branches, requiring pull request review, required checks, and CODEOWNERS review where applicable.

Enable secret scanning, dependency alerts, SCA, code scanning, and security advisory workflow where available.

Register CI/CD workflows, path filters, protected environments, approval rules, deployment gates, and evidence outputs.

Register GitNexus index metadata as derivative evidence tied to commit SHA.

Confirm CLAUDE.md, AGENTS.md, CODEOWNERS, PR template, and evidence manifest are present before declaring ready-to-develop.

## 4.15 Bootstrap Procedure B0-B12
| Step | Name | Exit Gate |
| --- | --- | --- |
| B0 | Controlled Intake | Ticket or approved request exists with owner, classification, purpose, bounded context, and risk. |
| B1 | Source Template Selection | Approved repository scaffold selected; no ad hoc initialization. |
| B2 | Repository Creation | Repository created with owner, visibility, classification, support path, and initial README. |
| B3 | Golden Source Registration | golden-source-register.yaml and repository inventory updated. |
| B4 | Access Control | Teams, roles, branch protection, CODEOWNERS, and least-privilege access configured. |
| B5 | AI Rules | CLAUDE.md and AGENTS.md installed and validated against central AIRA instructions. |
| B6 | Devcontainer / Toolchain | Pinned devcontainer or approved toolchain profile builds successfully. |
| B7 | Contracts and Policy Folders | contracts, schemas, policies, db/flyway, microfunctions, tests, docs, and evidence folders exist. |
| B8 | Pre-Commit and CI | Pre-commit hooks and first CI strict-mode pipeline run successfully. |
| B9 | Security and Supply Chain | Secrets scan, SAST/SCA baseline, container/IaC scans, SBOM/provenance where applicable. |
| B10 | GitNexus and Evidence | GitNexus read-only index or planned evidence path registered; evidence manifest created. |
| B11 | Ready-to-Develop Review | DevSecOps, Security, Architecture, and repository owner review evidence. |
| B12 | Activation | Repository marked ready only after gate evidence, sign-off, and backlog/linkage are complete. |

## 4.16 Ready-to-Develop Acceptance Gates
| Acceptance Gate | Status Requirement |
| --- | --- |
| Repository owner, purpose, classification, bounded context, and support path are documented. | Required |
| Golden Source registry entry exists and is linked to repository, evidence path, package registries, and approved templates. | Required |
| Branch protection, required reviews, required checks, no force push, and CODEOWNERS are active. | Required |
| CLAUDE.md and AGENTS.md exist, derive from approved AIRA rules, and prohibit unsafe AI actions. | Required |
| Devcontainer or approved workstation profile builds and exposes approved toolchain versions. | Required |
| Contracts, policies, db/flyway, microfunctions, tests, docs, evidence, and infra folder structure exists where applicable. | Required |
| Pre-commit and CI strict mode pass with build, tests, scans, contract checks, and evidence generation. | Required |
| Secrets scan has zero unresolved findings; no production data or secrets exist in repository. | Required |
| SBOM/provenance, GitNexus impact evidence, and OpenKM evidence path are configured where applicable. | Required |
| Ready-to-develop sign-off is recorded with owner, reviewer, date, known limitations, and improvement backlog. | Required |

## 4.17 Required Evidence
| Evidence Type | Minimum Evidence |
| --- | --- |
| Repository Evidence | Repository URL, owner, classification, purpose, branch protection export/screenshot, CODEOWNERS, PR template, README, initial commit, and protected branch settings. |
| Toolchain Evidence | Devcontainer build log, image digest, Java/Node/build tool versions, package lock, registry source, and workstation setup evidence. |
| Security Evidence | Secrets scan, SAST/SCA, dependency/license checks, branch protection, access review, policy checks, and no-production-data proof. |
| CI/CD Evidence | First CI strict-mode pipeline run, test reports, contract validation, migration validation, architecture fitness, SBOM/provenance, and evidence manifest. |
| AI Governance Evidence | CLAUDE.md/AGENTS.md validation, AI-use declaration template, model/tool route constraints, and prohibited action list. |
| Knowledge Evidence | Obsidian projection plan, LLM Wiki retrieval eligibility, OpenKM evidence path, freshness manifest, and source authority record. |

## 4.18 Anti-Patterns

Creating a repository manually with no approved template, owner, classification, branch protection, or evidence path.

Allowing direct push to main or release branches for normal development.

Using personal scripts, local-only packages, unmanaged Docker images, unpinned toolchains, or personal AI accounts for AIRA work.

Copying production secrets, tokens, raw customer data, or restricted evidence into source control, prompts, tests, screenshots, logs, or AI context.

Letting AI generate code, migrations, policies, contracts, or CI templates without PR/MR review, tests, and evidence.

Treating GitNexus, Obsidian, LLM Wiki, or AI summaries as source authority for source code or production behavior.

Disabling security gates, evidence generation, audit, branch protection, policy checks, or tests to accelerate delivery.

## 4.19 RACI
| Role | RACI | Responsibility |
| --- | --- | --- |
| Repository Owner | A/R | Owns repository purpose, classification, support model, backlog, and readiness sign-off. |
| Enterprise Architecture | A/C | Approves repository topology, bounded context placement, and architecture boundaries. |
| DevSecOps Lead | A/R | Owns CI/CD, branch protection, pre-commit, evidence pack, SBOM/provenance, and GitNexus integration. |
| Security Architecture | A/R | Approves access control, secrets handling, scans, security gates, AI retrieval boundaries, and policy controls. |
| Software Development Lead | R/C | Ensures developer usability, code layout, tests, standards adoption, and PR/MR discipline. |
| Platform Engineering | R/C | Owns devcontainer, base images, package registries, infrastructure templates, and environment integration. |
| AI Governance | A/C | Approves CLAUDE.md/AGENTS.md rules, AI assistant boundaries, model/tool routes, and agent access constraints. |
| Internal Audit | C/I | Reviews evidence completeness, traceability, classification, and control effectiveness. |

## 4.20 AVCI Compliance Summary
| AVCI Property | Repository Bootstrap Evidence |
| --- | --- |
| Attributable | Repository owner, source template, branch rules, CODEOWNERS, AI tools, CI run, evidence path, and approval records are named and linked. |
| Verifiable | Bootstrap produces renderable evidence: CI logs, checks, scans, devcontainer build, branch settings, GitNexus index metadata, and sign-off. |
| Classifiable | Repository classification, source authority, retrieval eligibility, secrets handling, model-route eligibility, and evidence handling are recorded. |
| Improvable | Bootstrap exceptions, drift, failures, missing controls, developer feedback, scan findings, and recurring issues become controlled backlog items. |

# 5. Simplification Recommendations

Keep the canonical standard detailed, but provide a one-page Ready-to-Develop Checklist for developers.

Maintain approved repository templates instead of asking each team to recreate structure manually.

Generate CLAUDE.md, AGENTS.md, CODEOWNERS, PR templates, evidence manifests, and contract folders from a controlled template package.

Use CI to validate repository readiness so humans review exceptions rather than manually checking every file.

Group bootstrap gates into B0-B12 so the team can follow a simple execution sequence without weakening governance.

# 6. Automation Recommendations
| Automation Area | Recommended Mechanism |
| --- | --- |
| Repository inventory | Script or System Builder service scans repositories for owner, classification, support path, CODEOWNERS, branch protection, and readiness status. |
| Golden Source validation | Validate golden-source-register.yaml against approved package registries, image digests, toolchain versions, model aliases, and evidence paths. |
| Branch protection drift | Continuously detect missing branch protections, force-push permissions, missing required checks, and CODEOWNERS gaps. |
| Template drift detection | Compare repository baseline files against approved templates for README, CLAUDE.md, AGENTS.md, CODEOWNERS, PR template, devcontainer, and workflows. |
| Evidence checklist validation | CI validates evidence-manifest.yaml and blocks readiness when mandatory evidence is missing. |
| Secret and policy validation | Secret scan, OPA policy tests, SBAC catalog validation, classification checks, and AI retrieval eligibility tests. |
| GitNexus integration | Commit-bound code intelligence output is captured as derivative evidence and linked to PR/MR evidence packs. |
| Review queue integration | New or drifted repositories become controlled review-queue items with owner, priority, dependency, action, and next step. |

# 7. Review Queue Control Register
| Sequence | File Name | Pack | Current Version | Recommended Version | Review Status | Priority | Dependency | Action Required | Next Step |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1-12 | Foundation through Greenfield standards | Multiple | Completed | Revised | Completed | P0/P1 | Foundation sequence | Maintain as revised baseline | Continue downstream alignment |
| 13 | 10-AIRA_MicroFunction_Framework | Pack 02 | v3.1 | v3.3 | Completed / Regenerated | P1 | Architecture foundation | Use as parent MicroFunction baseline | Done |
| 14 | 10A-AIRA_MicroFunction_Design_and_Development_Guide | Pack 02 | v2.1 | v2.3 | Completed / Regenerated | P1 | 10 | Use as design companion | Done |
| 15 | 10B-AIRA_MicroFunction_Framework_Implementation_Standard | Pack 02 | v2.1 | v2.2 | Completed / Revised | P1 | 10/10A | Use as implementation baseline | Done |
| 16 | 10C-AIRA_MicroFunction_Sequence_Diagrams_and_Mermaid_Reference | Pack 03 | v2.1 | v2.2 | Completed / Revised | P1 | 10/10A/10B | Use as diagram evidence baseline | Done |
| 17 | 10D-AIRA_MicroFunction_Standard_Function_Catalog_and_Assembly_Templates | Pack 03 | v2.1 | v2.2 | Completed / Revised | P1 | 10-10C | Use as catalog/template baseline | Done |
| 18 | 10E-AIRA_MicroFunction_Backend_Service_Generation_and_Runtime_Configuration_Standard | Pack 03 | v1.1 | v1.2 | Completed / Revised | P1 | 10-10D | Use as backend generation baseline | Done |
| 19 | 11-AIRA_AI_Native_DevSecOps_Standard | Pack 03 | v3.1 | v3.2 | Completed / Revised | P1 | MicroFunction baseline | Use as DevSecOps parent | Done |
| 20 | 11A-AIRA_DevSecOps_Governance_and_Evidence_Control_Standard | Pack 03 | v1.1 | v1.2 | Completed / Revised | P1 | 11 | Use as DevSecOps evidence companion | Done |
| 21 | 20-AIRA_CICD_Pipeline_and_Evidence_Pack_Implementation_Guide | Pack 05 | v1.1 | v1.2 | Completed / Revised | P1 | 11/11A | Use as CI/CD evidence implementation baseline | Done |
| 22 | 19-AIRA_GitNexus_Code_Intelligence_and_Impact_Analysis_Standard | Pack 05 | v1.2 | v1.3 | Completed / Revised | P1 | 20/11/11A | Use as code intelligence baseline | Done |
| 23 | 15-AIRA_API_and_Integration_Contract_Standard | Pack 04 | v2.1 | v2.2 | Completed / Revised | P1 | MicroFunction/DevSecOps | Use as API/event parent standard | Done |
| 24 | 15A-AIRA_API_Governance_and_Contract_First_Implementation_Guide | Pack 04 | v1.1 | v1.2 | Completed / Revised | P1 | 15 | Use as contract-first implementation guide | Done |
| 25 | 16-AIRA_Database_Migration_and_Data_Engineering_Standard | Pack 04 | v2.1 | v2.2 | Completed / Revised | P1 | 15/15A/MicroFunction | Use as database parent standard | Done |
| 26 | 16A-AIRA_Flyway_Initial_Database_Baseline_and_Migration_Governance_Guide | Pack 04 | v1.2 | v1.3 | Completed / Revised | P1 | 16 | Use as Flyway baseline guide | Done |
| 27 | 16B-AIRA_Database_Governance_Flyway_Only_Generation_Versioning_and_Migration_Control_Standard | Pack 04 | v1.1 | v1.2 | Completed / Revised | P1 | 16/16A | Use as Flyway-only System Builder control | Done |
| 28 | 17-AIRA_Security_Identity_Secrets_and_Access_Control_Standard | Pack 04 | v2.1 | v2.2 | Completed / Revised | P1 | 15/16/MicroFunction | Use as security parent standard | Done |
| 29 | 17A-AIRA_Security_and_Access_Control_Implementation_Guide | Pack 04 | v1.1 | v1.2 | Completed / Revised | P1 | 17 | Use as security implementation baseline | Done |
| 30 | 18-AIRA_Repository_Bootstrap_and_Golden_Source_Implementation_Guide | Pack 04 | v1.1 | v1.2 | Completed / Revised | P1 | 17/17A and source authority | Use as repository bootstrap baseline | Done |
| 31 | 21A-AIRA_Governed_Knowledge_Control_Plane_Obsidian_Codex_GitHub_Standard | Pack 05 | v1.1 | v1.2 | Next for Review | P1 | 18 and 05/06 | Align Golden Source, Obsidian, Codex, GitHub, LLM Wiki, retrieval, and evidence controls | Review next |

# 8. Change Log
| Version | Date | Owner | Summary |
| --- | --- | --- | --- |
| v1.1 | April/May 2026 | Prior aligned baseline | Repository bootstrap, branch protection, CODEOWNERS, devcontainer, Golden Source, and evidence-first bootstrap. |
| v1.2 | 2026-06-16 | AIRA Review Board | Aligned with revised AIRA architecture, AVCI, MicroFunction, DevSecOps, CI/CD, GitNexus, API, database/Flyway, security, source authority, CLAUDE.md/AGENTS.md, and Golden Source governance. |

