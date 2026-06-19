from __future__ import annotations

import argparse
import re
import zipfile
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable
from xml.etree import ElementTree as ET


NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
}


SOURCE_FILES = [
    "AIRA_00E_Canonical_Baseline_Supersedence_and_Release_Train_Register_v1.0.docx",
    "AIRA_01_AVCI_Engineering_Standard_v3.2_Revised.docx",
    "AIRA_01A_Enterprise_Architecture_Principles_SOLID_and_Fitness_Function_Standard_v1.2_Revised.docx",
    "AIRA_01B_AVCI_Evidence_Audit_Traceability_and_Control_Standard_v1.2_Revised.docx",
    "AIRA_02_Engineering_Blueprint_v5.2_Revised.docx",
    "AIRA_03_Developer_Guide_v4.2_Revised.docx",
    "AIRA_04_Technology_Stack_v9.2_Revised.docx",
    "AIRA_05_AI_Native_Information_Nervous_System_v4.2_Revised.docx",
    "AIRA_06_CLAUDE_MD_Reference_v3.2_Revised.docx",
    "AIRA_07_AI_DevSecOps_Skills_Framework_v3.2_Revised.docx",
    "AIRA_07B_AI_DevSecOps_Team_Transformation_Maturity_and_Progressive_Autonomy_Direction_Standard_v1.2_Revised.docx",
    "AIRA_08_Unit_Testing_Standard_v3.2_Revised.docx",
    "AIRA_08A_AI_Assisted_Unit_Testing_Maker_Checker_Prompt_Standard_v1.1_Revised.docx",
    "AIRA_09_Greenfield_Environment_Standard_v3.2_Revised.docx",
    "AIRA_10_MicroFunction_Framework_v3.4_Revised.docx",
    "AIRA_10A_MicroFunction_Design_and_Development_Guide_v2.4_Revised.docx",
    "AIRA_10B_MicroFunction_Framework_Implementation_Standard_v2.3_Revised.docx",
    "AIRA_10C_MicroFunction_Sequence_Diagrams_and_Mermaid_Reference_v2.3_Revised.docx",
    "AIRA_10D_MicroFunction_Standard_Function_Catalog_and_Assembly_Templates_v2.3_Revised.docx",
    "AIRA_10E_MicroFunction_Backend_Service_Generation_and_Runtime_Configuration_Standard_v1.3_Revised.docx",
    "AIRA_11_AI_Native_DevSecOps_Standard_v3.3_Revised.docx",
    "AIRA_11A_DevSecOps_Governance_and_Evidence_Control_Standard_v1.3_Revised.docx",
    "AIRA_12A_Dynamic_Frontend_Workspace_UI_Generation_Template_Lifecycle_and_UX_Governance_Standard_v1.2_Revised.docx",
    "AIRA_13_Obsidian_and_LLM_Wiki_Knowledge_Governance_Standard_v2_2_Review_and_Revised.docx",
    "AIRA_14_Architecture_Decision_Record_and_Technical_Decision_Log_Standard_v2_3_Review_and_Revised.docx",
    "AIRA_15_API_and_Integration_Contract_Standard_v2.2_Revised.docx",
    "AIRA_15A_API_Governance_and_Contract_First_Implementation_Guide_v1.2_Revised.docx",
    "AIRA_15A_API_Governance_and_Contract_First_Implementation_Guide_v1_2_Review_and_Revised.docx",
]


CATEGORIES = {
    "00E": ("00-release-baseline", "Release baseline"),
    "01": ("01-engineering-standards", "Engineering standards"),
    "01A": ("01-engineering-standards", "Engineering standards"),
    "01B": ("01-engineering-standards", "Engineering standards"),
    "02": ("02-engineering-blueprint", "Engineering blueprint"),
    "03": ("03-developer-guide", "Developer guide"),
    "04": ("04-technology-stack", "Technology stack"),
    "05": ("05-ai-native-information-nervous-system", "AI-native information nervous system"),
    "06": ("06-claude-md-reference", "CLAUDE.md reference"),
    "07": ("07-ai-devsecops-skills", "AI DevSecOps skills"),
    "07B": ("07-ai-devsecops-skills", "AI DevSecOps skills"),
    "08": ("08-unit-testing", "Unit testing"),
    "08A": ("08-unit-testing", "Unit testing"),
    "09": ("09-greenfield-environment", "Greenfield environment"),
    "10": ("10-microfunction-framework", "MicroFunction framework"),
    "10A": ("10-microfunction-framework", "MicroFunction framework"),
    "10B": ("10-microfunction-framework", "MicroFunction framework"),
    "10C": ("10-microfunction-framework", "MicroFunction framework"),
    "10D": ("10-microfunction-framework", "MicroFunction framework"),
    "10E": ("10-microfunction-framework", "MicroFunction framework"),
    "11": ("11-ai-native-devsecops", "AI-native DevSecOps"),
    "11A": ("11-ai-native-devsecops", "AI-native DevSecOps"),
    "12A": ("12-frontend-workspace-ui", "Frontend workspace UI"),
    "13": ("13-knowledge-governance", "Knowledge governance"),
    "14": ("14-decision-records", "Decision records"),
    "15": ("15-api-integration-contracts", "API and integration contracts"),
    "15A": ("15-api-integration-contracts", "API and integration contracts"),
}


@dataclass(frozen=True)
class DocMeta:
    source_name: str
    doc_id: str
    title: str
    version: str
    status: str
    folder: str
    category: str
    slug: str


def text_of(node: ET.Element) -> str:
    chunks: list[str] = []
    for child in node.iter():
        if child.tag == f"{{{NS['w']}}}t":
            chunks.append(child.text or "")
        elif child.tag == f"{{{NS['w']}}}tab":
            chunks.append("\t")
        elif child.tag == f"{{{NS['w']}}}br":
            chunks.append("\n")
    return "".join(chunks).strip()


def paragraph_style(paragraph: ET.Element) -> str:
    style = paragraph.find("./w:pPr/w:pStyle", NS)
    return style.attrib.get(f"{{{NS['w']}}}val", "") if style is not None else ""


def paragraph_to_markdown(paragraph: ET.Element) -> str:
    text = text_of(paragraph)
    if not text:
        return ""

    style = paragraph_style(paragraph).lower()
    heading_match = re.search(r"heading([1-6])", style)
    if heading_match:
        level = int(heading_match.group(1))
        return f"{'#' * level} {text}"

    return text


def table_to_markdown(table: ET.Element) -> list[str]:
    rows: list[list[str]] = []
    for row in table.findall("./w:tr", NS):
        cells = []
        for cell in row.findall("./w:tc", NS):
            cell_text = " ".join(
                text_of(paragraph)
                for paragraph in cell.findall("./w:p", NS)
                if text_of(paragraph)
            )
            cells.append(cell_text.replace("|", "\\|"))
        if cells:
            rows.append(cells)

    if not rows:
        return []

    width = max(len(row) for row in rows)
    normalized = [row + [""] * (width - len(row)) for row in rows]
    header = normalized[0]
    lines = [
        "| " + " | ".join(header) + " |",
        "| " + " | ".join(["---"] * width) + " |",
    ]
    for row in normalized[1:]:
        lines.append("| " + " | ".join(row) + " |")
    return lines


def iter_body_blocks(root: ET.Element) -> Iterable[str]:
    body = root.find("w:body", NS)
    if body is None:
        return
    for child in body:
        if child.tag == f"{{{NS['w']}}}p":
            markdown = paragraph_to_markdown(child)
            if markdown:
                yield markdown
        elif child.tag == f"{{{NS['w']}}}tbl":
            for line in table_to_markdown(child):
                yield line


def parse_metadata(source_name: str) -> DocMeta:
    stem = Path(source_name).stem
    match = re.match(
        r"^(AIRA_[0-9]{2}[A-Z]?|AIRA-DOC-[0-9]{3}[A-Z]?)[_-](.+?)_v([0-9]+(?:[._][0-9]+)*)(?:_|$)",
        stem,
    )
    if not match:
        raise ValueError(f"Cannot parse metadata from {source_name}")

    raw_id, raw_title, raw_version = match.groups()
    doc_id = raw_id.replace("_", "-")
    short_id = doc_id.replace("AIRA-", "").replace("DOC-", "")
    version = "v" + raw_version.replace("_", ".")
    status = "draft" if "Draft" in stem else "revised" if "Revised" in stem else "final"
    title = raw_title.replace("_", " ")
    folder, category = CATEGORIES.get(short_id, ("99-unsorted", "Unsorted"))
    slug = re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-")
    return DocMeta(source_name, doc_id, title, version, status, folder, category, slug)


def yaml_scalar(value: str) -> str:
    escaped = value.replace('"', '\\"')
    return f'"{escaped}"'


def frontmatter(meta: DocMeta) -> str:
    tags = [
        "aira",
        meta.folder,
        meta.status,
        meta.doc_id.lower().replace("-", "-"),
    ]
    today = date.today().isoformat()
    lines = [
        "---",
        f"title: {yaml_scalar(meta.title)}",
        f"doc_id: {yaml_scalar(meta.doc_id)}",
        f"version: {yaml_scalar(meta.version)}",
        f"status: {yaml_scalar(meta.status)}",
        f"category: {yaml_scalar(meta.category)}",
        f"source_docx: {yaml_scalar(meta.source_name)}",
        f"converted_on: {yaml_scalar(today)}",
        "tags:",
    ]
    lines.extend(f"  - {tag}" for tag in tags)
    lines.append("---")
    return "\n".join(lines)


def convert_docx(source: Path, destination: Path, meta: DocMeta) -> None:
    with zipfile.ZipFile(source) as docx:
        document_xml = docx.read("word/document.xml")
    root = ET.fromstring(document_xml)
    body = list(iter_body_blocks(root))

    content = [frontmatter(meta), "", f"# {meta.title}", ""]
    if body:
        first = body[0].lstrip("# ").strip().lower()
        if first != meta.title.lower():
            content.extend(body)
        else:
            content.extend(body[1:])
    content.append("")

    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n\n".join(content).replace("\n\n|", "\n|").replace("|\n\n|", "|\n|"), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert first-batch AIRA DOCX files to Obsidian Markdown.")
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--target", required=True, type=Path)
    args = parser.parse_args()

    missing: list[str] = []
    generated: list[Path] = []
    for source_name in SOURCE_FILES:
        source = args.source / source_name
        if not source.exists():
            missing.append(source_name)
            continue
        meta = parse_metadata(source_name)
        destination = args.target / meta.folder / f"{meta.slug}.md"
        convert_docx(source, destination, meta)
        generated.append(destination)

    if missing:
        raise SystemExit("Missing source files:\n" + "\n".join(missing))

    print(f"Generated {len(generated)} Markdown files.")
    for path in generated:
        print(path)


if __name__ == "__main__":
    main()
