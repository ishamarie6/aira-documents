# AIRA Documents

Obsidian-ready Markdown vault for the AIRA standards corpus.

## Batch 1

This repository currently contains the first batch of converted AIRA DOCX files:

- `00-release-baseline`
- `01-engineering-standards`
- `02-engineering-blueprint`
- `03-developer-guide`
- `04-technology-stack`
- `05-ai-native-information-nervous-system`
- `06-claude-md-reference`
- `07-ai-devsecops-skills`
- `08-unit-testing`
- `09-greenfield-environment`
- `10-microfunction-framework`
- `11-ai-native-devsecops`
- `12-frontend-workspace-ui`
- `13-knowledge-governance`
- `14-decision-records`
- `15-api-integration-contracts`

## Batch 2

The second batch adds the following converted AIRA DOCX sections:

- `16-database-migration-data-engineering`
- `17-security-identity-access-control`
- `18-repository-bootstrap-golden-source`
- `19-gitnexus-foundation-build`
- `20-cicd-pipeline-evidence-pack`
- `21-knowledge-control-plane`
- `22-prompt-guardrails-login-patterns`
- `23-architecture-fitness-login-poc`
- `24-login-runtime-operations`
- `25-knowledge-access-architecture`
- `26-knowledge-automation-pipeline`
- `29-uat-production-acceptance`
- `30-release-change-governance`
- `31-production-operations-observability`
- `32-business-process-access-catalog`
- `34-audit-compliance-evidence`
- `35-business-continuity-disaster-recovery`
- `36-training-adoption-change-management`
- `39-workstation-system-builder-setup`
- `40-login-microfunction-reference`
- `41-dynamic-workspace-system-builder-poc1`
- `42-ai-governance-agent-control`
- `43-continuous-improvement-multimodal-poc1a`
- `44-system-builder-agent-poc1a`
- `45-poc2-mortgage-experience`
- `46-60-dynamic-workspace`

## Batch 3

The third batch adds these converted AIRA DOCX and AIRA-DOC sections:

- `61-ai-assisted-workspace-system-builder`
- `62-enterprise-governance-roadmap`
- `63-production-operational-readiness`
- `64-resilience-performance-chaos`
- `65-policy-as-code`
- `66-evidence-manifest-data-model`
- `67-api-event-schema-registry`
- `68-control-objectives-traceability`
- `69-threat-modeling-secure-design`
- `70-ai-evaluation-red-team`
- `71-data-governance-privacy-retention`
- `72-reference-implementation-golden-paths`
- `73-system-builder-operating-manual`
- `74-dynamic-workspace-production-ux`
- `75-dynamic-workspace-certification`
- `76-architecture-fitness-gate-pack`
- `77-canonical-data-message-governance`
- `78-canonical-data-dictionary-message-catalog`
- `79-canonical-seed-catalog`
- `80-data-message-governance-cicd`
- `81-message-localization-knowledge-base`
- `82-batch-run-governance`
- `83-batch-operations-recovery`
- `84-reporting-analytics-bi`
- `85-report-generation-retention`
- `86-input-validation-data-integrity`
- `87-cross-layer-validation-implementation`
- `88-validation-error-feedback`
- `89-validation-evidence-testing`
- `90-enterprise-application-foundation`
- `91-product-management-governance`
- `91-94-compliance-register-adoption`
- `92-nfr-enterprise-readiness`
- `94-enterprise-data-dictionary`
- `95-register-adoption-source-pack`

Each Markdown file includes YAML frontmatter for Obsidian properties:

- `title`
- `doc_id`
- `version`
- `status`
- `category`
- `source_docx`
- `converted_on`
- `tags`

## Conversion

The conversion helper lives in `tools/convert_aira_docx.py`. It converts the registered DOCX source files into Markdown and preserves the original source filename in frontmatter.
