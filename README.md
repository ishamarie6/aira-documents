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

The conversion helper lives in `tools/convert_aira_docx.py`. It converts the first-batch DOCX source files into Markdown and preserves the original source filename in frontmatter.
