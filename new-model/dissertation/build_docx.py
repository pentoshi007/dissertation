#!/usr/bin/env python3
"""
Dissertation DOCX Builder
Assembles chapter markdown files into a single formatted Word document
with embedded figures and tables from the outputs directory.
"""

import os
import csv
import re
from pathlib import Path

try:
    from docx import Document
    from docx.shared import Pt, Inches, Cm, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.enum.section import WD_ORIENT
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-docx"])
    from docx import Document
    from docx.shared import Pt, Inches, Cm, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.enum.section import WD_ORIENT
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement

# ── Paths ──────────────────────────────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
OUTPUTS = PROJECT_ROOT / "outputs"
TABLES_DIR = OUTPUTS / "tables"
FIGURES_DIR = OUTPUTS / "figures"
OUTPUT_DOCX = SCRIPT_DIR / "dissertation.docx"

# ── Style helpers ──────────────────────────────────────────────────────────────

def set_cell_shading(cell, color_hex):
    """Apply shading to a table cell."""
    shading_elm = OxmlElement('w:shd')
    shading_elm.set(qn('w:fill'), color_hex)
    shading_elm.set(qn('w:val'), 'clear')
    cell._tc.get_or_add_tcPr().append(shading_elm)


def set_cell_borders(cell, top=None, bottom=None, left=None, right=None):
    """Set borders for a table cell."""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for edge, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        if val:
            el = OxmlElement(f'w:{edge}')
            el.set(qn('w:val'), val.get('val', 'single'))
            el.set(qn('w:sz'), val.get('sz', '4'))
            el.set(qn('w:color'), val.get('color', '000000'))
            el.set(qn('w:space'), '0')
            tcBorders.append(el)
    tcPr.append(tcBorders)


def configure_styles(doc):
    """Set up document styles matching the blueprint formatting rules."""
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    style.paragraph_format.line_spacing = 1.5
    style.paragraph_format.space_after = Pt(6)

    for level, (size, bold, align) in {
        1: (20, True, WD_ALIGN_PARAGRAPH.CENTER),
        2: (14, True, WD_ALIGN_PARAGRAPH.LEFT),
        3: (12, True, WD_ALIGN_PARAGRAPH.LEFT),
    }.items():
        hs = doc.styles[f'Heading {level}']
        hs.font.name = 'Times New Roman'
        hs.font.size = Pt(size)
        hs.font.bold = bold
        hs.font.color.rgb = RGBColor(0, 0, 0)
        hs.paragraph_format.alignment = align
        hs.paragraph_format.space_before = Pt(18 if level == 1 else 12)
        hs.paragraph_format.space_after = Pt(12 if level == 1 else 8)

    # Caption style
    if 'Caption' not in [s.name for s in doc.styles]:
        cap_style = doc.styles.add_style('Caption', 1)  # paragraph style
    else:
        cap_style = doc.styles['Caption']
    cap_style.font.name = 'Times New Roman'
    cap_style.font.size = Pt(10)
    cap_style.font.italic = True
    cap_style.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    cap_style.paragraph_format.space_before = Pt(4)
    cap_style.paragraph_format.space_after = Pt(8)


def configure_page(doc):
    """Set A4 page with specified margins."""
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Cm(3.54)
    section.right_margin = Inches(1)


# ── Content helpers ────────────────────────────────────────────────────────────

def add_title_page(doc):
    """Add a formatted title page."""
    for _ in range(6):
        doc.add_paragraph()

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("State-Dependent Oil-Price Pass-Through\nto India's Wholesale Fuel Inflation, 1994–2026")
    run.font.name = 'Times New Roman'
    run.font.size = Pt(22)
    run.bold = True

    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run2 = p2.add_run("Evidence from Monthly Local Projections")
    run2.font.name = 'Times New Roman'
    run2.font.size = Pt(16)
    run2.italic = True

    for _ in range(4):
        doc.add_paragraph()

    p3 = doc.add_paragraph()
    p3.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run3 = p3.add_run("A Dissertation Submitted in Partial Fulfilment\nof the Requirements for the Degree of\nMaster of Science in Economics")
    run3.font.name = 'Times New Roman'
    run3.font.size = Pt(14)

    for _ in range(3):
        doc.add_paragraph()

    p4 = doc.add_paragraph()
    p4.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run4 = p4.add_run("2026")
    run4.font.name = 'Times New Roman'
    run4.font.size = Pt(14)

    doc.add_page_break()


def read_csv_table(filename):
    """Read a CSV file and return headers + rows."""
    path = TABLES_DIR / filename
    if not path.exists():
        return None, None
    with open(path, 'r') as f:
        reader = csv.reader(f)
        headers = next(reader)
        rows = [row for row in reader if any(cell.strip() for cell in row)]
    return headers, rows


def add_styled_table(doc, headers, rows, caption=None):
    """Add a formatted table to the document."""
    if caption:
        p = doc.add_paragraph(caption, style='Caption')

    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.style = 'Table Grid'

    # Header row
    for j, header in enumerate(headers):
        cell = table.rows[0].cells[j]
        cell.text = ''
        p = cell.paragraphs[0]
        run = p.add_run(header)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(9)
        run.bold = True
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_cell_shading(cell, 'D9E2F3')

    # Data rows
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            cell = table.rows[i + 1].cells[j]
            cell.text = ''
            p = cell.paragraphs[0]
            run = p.add_run(str(val))
            run.font.name = 'Times New Roman'
            run.font.size = Pt(9)
            # Right-align numeric columns
            try:
                float(val.replace('<', '').replace('>', ''))
                p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            except (ValueError, AttributeError):
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT

    doc.add_paragraph()  # spacing


def add_figure(doc, filename, caption):
    """Add a figure with caption."""
    path = FIGURES_DIR / filename
    if not path.exists():
        p = doc.add_paragraph(f"[Figure not found: {filename}]")
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        return

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    run.add_picture(str(path), width=Inches(5.8))

    cap = doc.add_paragraph(caption, style='Caption')
    cap.alignment = WD_ALIGN_PARAGRAPH.LEFT


def add_body_text(doc, text):
    """Add a paragraph of body text."""
    p = doc.add_paragraph(text)
    # Ensure proper font
    for run in p.runs:
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)


def add_block_quote(doc, text):
    """Add a block quote (indented, italic)."""
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(1.27)
    p.paragraph_format.right_indent = Cm(1.27)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(11)
    run.italic = True


def process_markdown_to_docx(doc, md_text, chapter_figures_tables):
    """
    Parse markdown text and add content to the document.
    Handles headings, paragraphs, block quotes, and placeholders for figures/tables.
    """
    lines = md_text.strip().split('\n')
    current_para_lines = []

    def flush_para():
        if current_para_lines:
            text = ' '.join(current_para_lines).strip()
            if text:
                add_body_text(doc, text)
            current_para_lines.clear()

    i = 0
    while i < len(lines):
        line = lines[i]

        # Skip empty lines (flush paragraph)
        if not line.strip():
            flush_para()
            i += 1
            continue

        # Headings
        if line.startswith('# ') and not line.startswith('## '):
            flush_para()
            doc.add_heading(line[2:].strip(), level=1)
            i += 1
            continue
        if line.startswith('## '):
            flush_para()
            doc.add_heading(line[3:].strip(), level=2)
            i += 1
            continue
        if line.startswith('### '):
            flush_para()
            doc.add_heading(line[4:].strip(), level=3)
            i += 1
            continue

        # Block quotes
        if line.startswith('> '):
            flush_para()
            quote_lines = []
            while i < len(lines) and lines[i].startswith('> '):
                quote_lines.append(lines[i][2:])
                i += 1
            add_block_quote(doc, ' '.join(quote_lines))
            continue

        # Figure/table placeholders
        if line.strip().startswith('**[') and line.strip().endswith(']**'):
            flush_para()
            placeholder = line.strip()[3:-3]

            # Check for figure
            if 'fig_' in placeholder.lower() or 'figure' in placeholder.lower():
                # Extract filename from placeholder
                fig_match = re.search(r'(fig_\d+\w*\.png)', placeholder)
                if fig_match:
                    add_figure(doc, fig_match.group(1), placeholder)
                else:
                    add_body_text(doc, f"[{placeholder}]")

            # Table CSV placeholders — skip embedding full CSVs;
            # compact inline markdown tables in the chapter text are used instead
            elif 'table_' in placeholder.lower():
                pass  # table data is already in inline markdown tables
            else:
                add_body_text(doc, f"[{placeholder}]")

            i += 1
            continue

        # Markdown tables (| ... | format)
        if line.strip().startswith('|') and '|' in line:
            flush_para()
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_lines.append(lines[i])
                i += 1

            # Parse the table
            parsed_rows = []
            for tl in table_lines:
                cells = [c.strip() for c in tl.strip().strip('|').split('|')]
                # Skip separator rows
                if all(re.match(r'^[-:]+$', c) for c in cells):
                    continue
                parsed_rows.append(cells)

            if len(parsed_rows) >= 2:
                headers = parsed_rows[0]
                data_rows = parsed_rows[1:]
                add_styled_table(doc, headers, data_rows)
            continue

        # Regular text - accumulate
        # Clean markdown formatting
        clean = line.strip()
        clean = re.sub(r'\*\*(.+?)\*\*', r'\1', clean)  # bold
        clean = re.sub(r'\*(.+?)\*', r'\1', clean)  # italic
        # Handle list items
        if clean.startswith('- '):
            flush_para()
            p = doc.add_paragraph(clean[2:], style='List Bullet')
            for run in p.runs:
                run.font.name = 'Times New Roman'
                run.font.size = Pt(12)
            i += 1
            continue

        current_para_lines.append(clean)
        i += 1

    flush_para()


# ── Main build ─────────────────────────────────────────────────────────────────

def build():
    print("Building dissertation DOCX...")

    doc = Document()
    configure_styles(doc)
    configure_page(doc)

    # Title page
    add_title_page(doc)

    # Chapter files in order
    chapters = [
        ("00_abstract.md", {}),
        ("01_introduction.md", {}),
        ("02_background_literature.md", {}),
        ("03_data_variables.md", {
            "table_01": "table_01_data_spans.csv",
            "table_03": "table_03_descriptive_stats.csv",
            "table_04": "table_04_unit_root_battery.csv",
            "fig_01": "fig_01_wpi_fuel_chained.png",
            "fig_02": "fig_02_rupee_oil_shock.png",
        }),
        ("04_methodology.md", {}),
        ("05_results.md", {
            "table_05": "table_05_lp_all_sample.csv",
            "table_06": "table_06_lp_post2010.csv",
            "table_10": "table_10_diagnostics.csv",
            "fig_03": "fig_03_lp_all_sample.png",
            "fig_04": "fig_04_lp_state_comparison_post2010.png",
        }),
        ("06_robustness_limitations.md", {
            "table_07": "table_07_lp_post2014.csv",
            "table_08": "table_08_lp_high_volatility.csv",
            "table_09": "table_09_asymmetry_secondary.csv",
            "fig_05": "fig_05_lp_state_comparison_post2014.png",
            "fig_06": "fig_06_lp_high_volatility.png",
        }),
        ("07_conclusion.md", {}),
        ("08_references.md", {}),
    ]

    for filename, figs_tables in chapters:
        md_path = SCRIPT_DIR / filename
        if not md_path.exists():
            print(f"  WARNING: {filename} not found, skipping.")
            continue

        print(f"  Processing {filename}...")
        with open(md_path, 'r') as f:
            md_text = f.read()

        process_markdown_to_docx(doc, md_text, figs_tables)

        # Add page break between chapters (but not after references)
        if filename != "08_references.md":
            doc.add_page_break()

    # Save
    doc.save(str(OUTPUT_DOCX))
    print(f"\nDissertation saved to: {OUTPUT_DOCX}")
    print(f"File size: {OUTPUT_DOCX.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    build()
