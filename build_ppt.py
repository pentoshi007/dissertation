#!/usr/bin/env python3
"""Build the dissertation evaluation PowerPoint.

Output: aniket-dissertation-presentation.pptx (16:9).

Style: presenter's deck (declarative, claim-style text) for an external MS
Economics evaluation. Title + 11 numbered content slides + thank-you.
No "guide" voice on slides.
"""

from __future__ import annotations

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Inches, Pt


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "aniket-dissertation-presentation.pptx"

# ----------------------------------------------------------------------------
# Palette
# ----------------------------------------------------------------------------
NAVY = RGBColor(0x14, 0x2A, 0x55)
NAVY_DARK = RGBColor(0x0B, 0x1B, 0x3A)
ACCENT_RED = RGBColor(0xB3, 0x1B, 0x1B)
ACCENT_AMBER = RGBColor(0xC2, 0x76, 0x0C)
ACCENT_BLUEGREY = RGBColor(0x47, 0x55, 0x69)
INK = RGBColor(0x1F, 0x29, 0x37)
INK_SOFT = RGBColor(0x4B, 0x55, 0x63)
RULE = RGBColor(0xD1, 0xD5, 0xDB)
RULE_SOFT = RGBColor(0xE5, 0xE7, 0xEB)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
PAGE_BG = RGBColor(0xFA, 0xFB, 0xFC)
TABLE_HEAD = RGBColor(0x14, 0x2A, 0x55)
TABLE_HEAD_TXT = WHITE
TABLE_ALT = RGBColor(0xF3, 0xF4, 0xF6)
CALLOUT_BG = RGBColor(0xFE, 0xF3, 0xC7)
CALLOUT_BORDER = RGBColor(0xC2, 0x76, 0x0C)
KEY_BG = RGBColor(0xEC, 0xF1, 0xF8)
KEY_BORDER = NAVY
ROW_HL_STRONG = RGBColor(0xFD, 0xEC, 0xEC)

# ----------------------------------------------------------------------------
# Geometry (16:9)
# ----------------------------------------------------------------------------
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)
MARGIN = Inches(0.55)
TITLE_TOP = Inches(0.45)
TITLE_H = Inches(0.85)
RULE_Y = Inches(1.32)
RULE_H = Inches(0.04)
BODY_TOP = Inches(1.55)
FOOTER_Y = Inches(7.05)
FOOTER_H = Inches(0.32)

FONT = "Calibri"
DECK_FOOTER = "Layered oil-price pass-through in India  |  Aniket Pandey, B.Tech + MS Economics"


def set_solid_fill(shape, rgb: RGBColor):
    shape.fill.solid()
    shape.fill.fore_color.rgb = rgb


def set_no_line(shape):
    shape.line.fill.background()


def set_line(shape, rgb: RGBColor, width_pt: float = 0.75):
    shape.line.color.rgb = rgb
    shape.line.width = Pt(width_pt)


def add_text(slide, left, top, width, height, text, *,
             size=18, bold=False, color=INK, align=PP_ALIGN.LEFT,
             anchor=MSO_ANCHOR.TOP, font_name=FONT, italic=False,
             line_spacing=1.15):
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame
    tf.margin_left = Inches(0.05)
    tf.margin_right = Inches(0.05)
    tf.margin_top = Inches(0.02)
    tf.margin_bottom = Inches(0.02)
    tf.word_wrap = True
    tf.vertical_anchor = anchor

    lines = text.split("\n") if isinstance(text, str) else list(text)
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.line_spacing = line_spacing
        run = p.add_run()
        run.text = line
        run.font.name = font_name
        run.font.size = Pt(size)
        run.font.bold = bold
        run.font.italic = italic
        run.font.color.rgb = color
    return tb


def add_rich_text(slide, left, top, width, height, paragraphs, *,
                  anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame
    tf.margin_left = Inches(0.05)
    tf.margin_right = Inches(0.05)
    tf.margin_top = Inches(0.02)
    tf.margin_bottom = Inches(0.02)
    tf.word_wrap = True
    tf.vertical_anchor = anchor

    for i, para in enumerate(paragraphs):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = para.get("align", PP_ALIGN.LEFT)
        p.line_spacing = para.get("line_spacing", 1.18)
        if para.get("space_after"):
            p.space_after = Pt(para["space_after"])
        if para.get("space_before"):
            p.space_before = Pt(para["space_before"])
        for run_def in para.get("runs", []):
            r = p.add_run()
            r.text = run_def["text"]
            r.font.name = run_def.get("font", FONT)
            r.font.size = Pt(run_def.get("size", 18))
            r.font.bold = run_def.get("bold", False)
            r.font.italic = run_def.get("italic", False)
            r.font.color.rgb = run_def.get("color", INK)
    return tb


def add_rectangle(slide, left, top, width, height, *,
                  fill=None, line_color=None, line_width=0.75):
    rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    rect.shadow.inherit = False
    if fill is None:
        rect.fill.background()
    else:
        set_solid_fill(rect, fill)
    if line_color is None:
        set_no_line(rect)
    else:
        set_line(rect, line_color, line_width)
    rect.text_frame.text = ""
    return rect


def add_round_rect(slide, left, top, width, height, *,
                   fill=None, line_color=None, line_width=0.75, radius=0.08):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shp.shadow.inherit = False
    try:
        shp.adjustments[0] = radius
    except Exception:
        pass
    if fill is None:
        shp.fill.background()
    else:
        set_solid_fill(shp, fill)
    if line_color is None:
        set_no_line(shp)
    else:
        set_line(shp, line_color, line_width)
    return shp


def add_arrow(slide, left, top, width, height, color=NAVY):
    arr = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, left, top, width, height)
    arr.shadow.inherit = False
    set_solid_fill(arr, color)
    set_no_line(arr)
    return arr


def add_chevron(slide, left, top, width, height, color=NAVY, text=None,
                text_color=WHITE, size=14):
    shp = slide.shapes.add_shape(MSO_SHAPE.CHEVRON, left, top, width, height)
    shp.shadow.inherit = False
    set_solid_fill(shp, color)
    set_no_line(shp)
    if text:
        tf = shp.text_frame
        tf.margin_left = Inches(0.08)
        tf.margin_right = Inches(0.18)
        tf.margin_top = Inches(0.04)
        tf.margin_bottom = Inches(0.04)
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.alignment = PP_ALIGN.CENTER
        p.line_spacing = 1.05
        r = p.add_run()
        r.text = text
        r.font.name = FONT
        r.font.size = Pt(size)
        r.font.bold = True
        r.font.color.rgb = text_color
    return shp


def style_table_cell(cell, text, *, size=12, bold=False, color=INK,
                     fill=None, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.MIDDLE):
    cell.margin_left = Inches(0.08)
    cell.margin_right = Inches(0.08)
    cell.margin_top = Inches(0.04)
    cell.margin_bottom = Inches(0.04)
    cell.vertical_anchor = anchor
    if fill is not None:
        cell.fill.solid()
        cell.fill.fore_color.rgb = fill
    tf = cell.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.alignment = align
    p.line_spacing = 1.1
    p.text = ""
    r = p.add_run()
    r.text = str(text)
    r.font.name = FONT
    r.font.size = Pt(size)
    r.font.bold = bold
    r.font.color.rgb = color


def add_table(slide, left, top, width, height, headers, rows, *,
              col_widths=None, header_size=13, body_size=12,
              head_fill=TABLE_HEAD, head_color=TABLE_HEAD_TXT, alt_fill=TABLE_ALT,
              align_header=None, align_body=None, highlight_rows=None,
              highlight_fill=None):
    n_cols = len(headers)
    n_rows = 1 + len(rows)
    tbl_shape = slide.shapes.add_table(n_rows, n_cols, left, top, width, height)
    tbl = tbl_shape.table

    if col_widths is not None:
        total = sum(col_widths)
        for i, w in enumerate(col_widths):
            tbl.columns[i].width = Emu(int(width * (w / total)))

    align_header = align_header or [PP_ALIGN.CENTER] * n_cols
    align_body = align_body or [PP_ALIGN.LEFT] + [PP_ALIGN.CENTER] * (n_cols - 1)

    for j, h in enumerate(headers):
        style_table_cell(tbl.cell(0, j), h, size=header_size, bold=True,
                         color=head_color, fill=head_fill, align=align_header[j])

    for i, row in enumerate(rows):
        zebra = alt_fill if i % 2 == 1 else WHITE
        if highlight_rows and i in highlight_rows and highlight_fill is not None:
            zebra = highlight_fill
        for j, val in enumerate(row):
            bold = False
            color = INK
            if isinstance(val, tuple):
                txt, opts = val
                bold = opts.get("bold", False)
                color = opts.get("color", INK)
            else:
                txt = val
            style_table_cell(tbl.cell(i + 1, j), txt, size=body_size, bold=bold,
                             color=color, fill=zebra, align=align_body[j])

    return tbl_shape


def add_speaker_notes(slide, text):
    notes = slide.notes_slide
    tf = notes.notes_text_frame
    tf.text = text
    for p in tf.paragraphs:
        for r in p.runs:
            r.font.name = FONT
            r.font.size = Pt(14)


def slide_chrome(slide, title, *, page_num=None, total_pages=None,
                 title_color=NAVY, rule_color=ACCENT_RED):
    add_rectangle(slide, 0, 0, SLIDE_W, SLIDE_H, fill=PAGE_BG)
    add_text(slide, MARGIN, TITLE_TOP, SLIDE_W - 2 * MARGIN, TITLE_H,
             title, size=30, bold=True, color=title_color, align=PP_ALIGN.LEFT)
    add_rectangle(slide, MARGIN, RULE_Y, Inches(1.20), RULE_H, fill=rule_color)
    add_rectangle(slide, MARGIN + Inches(1.20), RULE_Y,
                  SLIDE_W - 2 * MARGIN - Inches(1.20), Inches(0.02), fill=RULE)
    add_rectangle(slide, MARGIN, FOOTER_Y - Inches(0.05),
                  SLIDE_W - 2 * MARGIN, Inches(0.01), fill=RULE_SOFT)
    add_text(slide, MARGIN, FOOTER_Y, SLIDE_W - 2 * MARGIN - Inches(1.0),
             FOOTER_H, DECK_FOOTER, size=9, color=INK_SOFT, align=PP_ALIGN.LEFT)
    if page_num and total_pages:
        add_text(slide, SLIDE_W - MARGIN - Inches(1.2), FOOTER_Y, Inches(1.2),
                 FOOTER_H, f"Slide {page_num} of {total_pages}",
                 size=9, color=INK_SOFT, align=PP_ALIGN.RIGHT)


def place_picture(slide, path, box_left, box_top, box_w, box_h, *, align="center"):
    if not Path(path).exists():
        return None
    from PIL import Image
    with Image.open(path) as im:
        iw, ih = im.size
    ratio = ih / iw
    w_emu = box_w
    h_emu = Emu(int(int(w_emu) * ratio))
    if h_emu > box_h:
        h_emu = box_h
        w_emu = Emu(int(int(h_emu) / ratio))
    fx = box_left + (box_w - w_emu) / 2
    fy = box_top + (box_h - h_emu) / 2 if align == "center" else box_top
    return slide.shapes.add_picture(str(path), fx, fy, width=w_emu, height=h_emu)


# ----------------------------------------------------------------------------
# Slide builders
# ----------------------------------------------------------------------------

TOTAL_PAGES = 11  # numbered slides (excludes title and thank-you)


def slide_title(prs, blank):
    s = prs.slides.add_slide(blank)
    add_rectangle(s, 0, 0, SLIDE_W, SLIDE_H, fill=WHITE)
    # left navy band
    add_rectangle(s, 0, 0, Inches(0.55), SLIDE_H, fill=NAVY)
    # small red rule (no text, matches reference image)
    add_rectangle(s, Inches(1.0), Inches(0.95), Inches(0.5), Inches(0.06), fill=ACCENT_RED)

    # Title + subtitle in a single text box so subtitle sits directly under title
    tb = s.shapes.add_textbox(Inches(1.0), Inches(1.55), Inches(11.3), Inches(2.5))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = Inches(0.05)
    tf.margin_right = Inches(0.05)
    tf.margin_top = Inches(0.02)
    tf.margin_bottom = Inches(0.02)

    p1 = tf.paragraphs[0]
    p1.alignment = PP_ALIGN.LEFT
    p1.line_spacing = 1.08
    r1 = p1.add_run()
    r1.text = "From wholesale prices to consumer inflation"
    r1.font.name = FONT
    r1.font.size = Pt(42)
    r1.font.bold = True
    r1.font.color.rgb = NAVY

    p2 = tf.add_paragraph()
    p2.alignment = PP_ALIGN.LEFT
    p2.line_spacing = 1.15
    p2.space_before = Pt(8)
    r2 = p2.add_run()
    r2.text = "Layered pass-through of global oil shocks in India, 1983\u20132026"
    r2.font.name = FONT
    r2.font.size = Pt(22)
    r2.font.italic = True
    r2.font.color.rgb = INK

    # divider
    add_rectangle(s, Inches(1.0), Inches(3.70), Inches(2.6), Inches(0.025), fill=RULE)

    # presenter block
    add_rich_text(
        s, Inches(1.0), Inches(3.90), Inches(11.3), Inches(2.0),
        [
            {"runs": [{"text": "Aniket Pandey", "size": 22, "bold": True, "color": NAVY}],
             "space_after": 4},
            {"runs": [{"text": "B.Tech + MS Economics", "size": 16, "color": INK}], "space_after": 2},
            {"runs": [{"text": "School Of Engineering, JNU", "size": 14, "color": INK_SOFT}],
             "space_after": 2},
            {"runs": [{"text": "Supervisor: Prof. Shakti Kumar", "size": 14, "color": INK_SOFT}]},
        ],
    )

    # bottom chevron strip
    chain_y = Inches(6.30)
    chain_h = Inches(0.55)
    seg_w = Inches(2.55)
    gap = Inches(0.10)
    items = [
        ("Brent crude", NAVY),
        ("Retail petrol", ACCENT_RED),
        ("Wholesale prices", ACCENT_AMBER),
        ("Consumer basket", ACCENT_BLUEGREY),
    ]
    x = Inches(1.0)
    for label, col in items:
        add_chevron(s, x, chain_y, seg_w, chain_h, color=col, text=label, size=12)
        x += seg_w + gap

def slide_motivation(prs, blank):
    s = prs.slides.add_slide(blank)
    slide_chrome(s, "Why oil-price pass-through matters for India",
                 page_num=1, total_pages=TOTAL_PAGES)

    bullets = [
        "India imports a large share of its crude oil.",
        "Crude is priced internationally, mainly in US dollars.",
        "Domestic oil pressure comes from Brent crude and INR/USD jointly.",
        "Oil moves through retail petrol, wholesale fuel, transport, and input costs.",
        "Headline CPI does not respond one-for-one with oil.",
    ]
    paras = [
        {"runs": [{"text": "\u25AA  ", "size": 19, "color": ACCENT_RED, "bold": True},
                  {"text": b, "size": 19, "color": INK}],
         "space_after": 12}
        for b in bullets
    ]
    add_rich_text(s, MARGIN, BODY_TOP, SLIDE_W - 2 * MARGIN, Inches(4.0), paras)

    # horizontal transmission chain (all arrows left-to-right)
    chain_y = Inches(5.55)
    chain_h = Inches(0.85)
    box_w = Inches(3.30)
    arr_w = Inches(0.55)
    arr_h = Inches(0.40)
    x = MARGIN

    def chain_box(x, color, text):
        add_round_rect(s, x, chain_y, box_w, chain_h, fill=WHITE, line_color=color, line_width=1.25)
        add_text(s, x, chain_y, box_w, chain_h, text, size=14, bold=True, color=color,
                 align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.10)

    chain_box(x, NAVY, "Brent crude  +  INR/USD")
    x += box_w
    add_arrow(s, x + Inches(0.05), chain_y + (chain_h - arr_h) / 2, arr_w, arr_h, color=ACCENT_RED)
    x += arr_w + Inches(0.10)
    chain_box(x, ACCENT_RED, "Domestic oil-cost pressure")
    x += box_w
    add_arrow(s, x + Inches(0.05), chain_y + (chain_h - arr_h) / 2, arr_w, arr_h, color=ACCENT_AMBER)
    x += arr_w + Inches(0.10)
    chain_box(x, ACCENT_AMBER, "Indian price system")

    add_speaker_notes(
        s,
        "After the title, I will first explain why this topic matters.\n\n"
        "India imports a large share of crude oil. Crude oil is priced in US dollars, so India is affected by two things: the global Brent crude price and the rupee-dollar exchange rate.\n\n"
        "Oil can enter the Indian price system through petrol prices, wholesale fuel prices, transport costs, and input costs. But headline CPI is a broad index. It has food, housing, services, and many non-fuel items. So my basic question is: if oil matters, why does the effect become weak in headline CPI?",
    )


def slide_objective(prs, blank):
    s = prs.slides.add_slide(blank)
    slide_chrome(s, "Objective and research question",
                 page_num=2, total_pages=TOTAL_PAGES)

    # Research question card
    add_round_rect(s, MARGIN, BODY_TOP, SLIDE_W - 2 * MARGIN, Inches(1.45),
                   fill=KEY_BG, line_color=KEY_BORDER, line_width=1.0)
    add_rich_text(
        s, MARGIN + Inches(0.30), BODY_TOP + Inches(0.10),
        SLIDE_W - 2 * MARGIN - Inches(0.6), Inches(1.25),
        [
            {"runs": [{"text": "Research question",
                       "size": 14, "bold": True, "color": ACCENT_RED}], "space_after": 4},
            {"runs": [{"text": (
                "How do global oil-price shocks transmit across India\u2019s wholesale, retail "
                "fuel, fuel-sensitive consumer, and headline consumer price layers, and where "
                "does this pass-through weaken?"
            ), "size": 18, "color": NAVY_DARK, "italic": True}],
             "line_spacing": 1.25},
        ],
    )

    col_top = BODY_TOP + Inches(1.70)
    col_h = Inches(3.30)
    col_w = (SLIDE_W - 2 * MARGIN - Inches(0.30)) / 2

    # Objective card
    add_round_rect(s, MARGIN, col_top, col_w, col_h, fill=WHITE, line_color=RULE, line_width=0.75)
    add_text(s, MARGIN + Inches(0.25), col_top + Inches(0.12), col_w - Inches(0.5), Inches(0.4),
             "Objective", size=16, bold=True, color=NAVY)
    objs = [
        "Estimate short-run oil-price pass-through across multiple Indian price layers.",
        "Identify the point at which the shock attenuates before reaching headline CPI.",
        "Compare strong and weak segments of the price system, layer by layer.",
    ]
    add_rich_text(
        s, MARGIN + Inches(0.25), col_top + Inches(0.55), col_w - Inches(0.5), col_h - Inches(0.7),
        [
            {"runs": [{"text": "\u25AA  ", "size": 16, "color": ACCENT_RED, "bold": True},
                      {"text": o, "size": 16, "color": INK}], "space_after": 10}
            for o in objs
        ],
    )

    # Contribution card
    cx = MARGIN + col_w + Inches(0.30)
    add_round_rect(s, cx, col_top, col_w, col_h, fill=WHITE, line_color=RULE, line_width=0.75)
    add_text(s, cx + Inches(0.25), col_top + Inches(0.12), col_w - Inches(0.5), Inches(0.4),
             "Contribution", size=16, bold=True, color=NAVY)
    contribs = [
        "Treats oil pass-through as a layered transmission problem.",
        "Moves beyond a single oil-to-headline-CPI estimate.",
        "Covers five layers: WPI, WPI Fuel, retail petrol, CPI Fuel and Light, headline CPI.",
        "Tests attenuation directly on a common sample.",
    ]
    add_rich_text(
        s, cx + Inches(0.25), col_top + Inches(0.55), col_w - Inches(0.5), col_h - Inches(0.7),
        [
            {"runs": [{"text": "\u25AA  ", "size": 15, "color": ACCENT_AMBER, "bold": True},
                      {"text": c, "size": 15, "color": INK}], "space_after": 9}
            for c in contribs
        ],
    )

    add_speaker_notes(
        s,
        "Now I move from the motivation to the exact research question.\n\n"
        "The main objective is to estimate short-run oil-price pass-through across different Indian price layers. I am not only looking at oil and headline CPI directly. I am checking the layers in between.\n\n"
        "The research question is: how do global oil shocks move through wholesale prices, retail fuel prices, fuel-sensitive CPI, and headline CPI, and where does the effect become weak?\n\n"
        "My contribution is the layered view. Each layer is estimated separately, so I am not claiming one simple WPI-to-CPI causal chain.",
    )


def slide_framework(prs, blank):
    s = prs.slides.add_slide(blank)
    slide_chrome(s, "Conceptual framework: a layered price map",
                 page_num=3, total_pages=TOTAL_PAGES)

    chain_top = BODY_TOP + Inches(0.55)
    chain_label_w = Inches(2.0)
    chevron_w = Inches(2.30)
    chevron_h = Inches(0.95)
    gap_x = Inches(0.10)

    add_text(s, MARGIN, chain_top, chain_label_w, chevron_h,
             "Consumer chain", size=14, bold=True, color=ACCENT_RED,
             anchor=MSO_ANCHOR.MIDDLE)
    row1 = [
        ("Brent crude", ACCENT_RED),
        ("PPAC retail petrol", ACCENT_RED),
        ("CPI Fuel and Light", ACCENT_AMBER),
        ("Headline CPI", ACCENT_BLUEGREY),
    ]
    x = MARGIN + chain_label_w
    for label, col in row1:
        add_chevron(s, x, chain_top, chevron_w, chevron_h, color=col, text=label, size=14)
        x += chevron_w + gap_x

    chain_top2 = chain_top + chevron_h + Inches(0.45)
    add_text(s, MARGIN, chain_top2, chain_label_w, chevron_h,
             "Wholesale map", size=14, bold=True, color=NAVY,
             anchor=MSO_ANCHOR.MIDDLE)
    row2 = [
        ("Rupee oil price", NAVY),
        ("WPI Fuel and Power", ACCENT_RED),
        ("Headline WPI", ACCENT_BLUEGREY),
    ]
    chev2_w = (4 * chevron_w + 3 * gap_x - 2 * gap_x) / 3
    x = MARGIN + chain_label_w
    for label, col in row2:
        add_chevron(s, x, chain_top2, chev2_w, chevron_h, color=col, text=label, size=14)
        x += chev2_w + gap_x

    legend_top = chain_top2 + chevron_h + Inches(0.55)
    legend_h = Inches(0.45)
    add_text(s, MARGIN, legend_top, Inches(1.5), legend_h,
             "Pass-through:", size=13, bold=True, color=INK,
             anchor=MSO_ANCHOR.MIDDLE)
    items = [("Strong", ACCENT_RED), ("Medium", ACCENT_AMBER), ("Weak", ACCENT_BLUEGREY)]
    lx = MARGIN + Inches(1.5)
    for label, col in items:
        add_rectangle(s, lx, legend_top + Inches(0.10), Inches(0.30), Inches(0.22), fill=col)
        add_text(s, lx + Inches(0.38), legend_top, Inches(1.2), legend_h, label,
                 size=13, color=INK, anchor=MSO_ANCHOR.MIDDLE)
        lx += Inches(1.7)

    add_speaker_notes(
        s,
        "This slide shows the map behind the whole dissertation.\n\n"
        "The first row is the consumer-side chain: Brent crude, then PPAC retail petrol, then CPI Fuel and Light, and finally headline CPI.\n\n"
        "The second row is the wholesale-side map: rupee oil price, then WPI Fuel and Power, and then headline WPI.\n\n"
        "The important point is that these are related price layers, but they are not estimated as one big mechanical chain. I use separate ADL models and then compare the pattern across layers.",
    )


def slide_data(prs, blank):
    s = prs.slides.add_slide(blank)
    slide_chrome(s, "Data sources and variable purpose",
                 page_num=3, total_pages=TOTAL_PAGES)

    headers = ["Series", "Source", "Transformation", "Purpose"]
    rows = [
        ["Brent crude price", "World Bank Pink Sheet (FRED POILBREUSDM)",
         "Monthly log difference", "Global oil shock"],
        ["INR/USD exchange rate", "FRED EXINUS",
         "Monthly log difference", "Exchange-rate component"],
        ["Rupee oil price", "Brent \u00D7 INR/USD",
         "Monthly log difference", "Oil shock for WPI and headline CPI"],
        ["Headline WPI", "OEA, chained to 2011-12 base",
         "Monthly log difference", "Wholesale headline layer"],
        ["WPI Fuel and Power", "OEA, chained to 2011-12 base",
         "Monthly log difference", "Wholesale fuel-sensitive layer"],
        ["PPAC Delhi retail petrol", "PPAC ready reckoner",
         "Monthly log difference", "Direct retail fuel layer"],
        ["CPI Fuel and Light", "MoSPI harmonised series",
         "Monthly log difference", "Fuel-sensitive consumer bridge"],
        ["Headline CPI", "MoSPI / FRED CPI source",
         "Monthly log difference", "Consumer endpoint"],
        ["IIP", "MoSPI", "Monthly log difference", "Activity control"],
    ]
    add_table(
        s, MARGIN, BODY_TOP, SLIDE_W - 2 * MARGIN, Inches(5.05),
        headers, rows,
        col_widths=[2.4, 4.0, 2.2, 3.8],
        header_size=13, body_size=12,
        align_header=[PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT],
        align_body=[PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.LEFT],
    )

    add_speaker_notes(
        s,
        "Now I will explain the data used in the study.\n\n"
        "The data are monthly. Brent crude captures the international oil shock. The exchange rate captures the rupee-dollar part. I combine Brent and the exchange rate to create the rupee oil price, which is the domestic oil-cost pressure.\n\n"
        "For prices, I use WPI, WPI Fuel and Power, PPAC Delhi retail petrol, CPI Fuel and Light, and headline CPI. I also use IIP as an activity control.\n\n"
        "All main variables are converted into monthly log differences. In simple terms, these can be read as approximate monthly percentage changes.",
    )


def slide_methodology(prs, blank):
    s = prs.slides.add_slide(blank)
    slide_chrome(s, "Short-run asymmetric ADL model",
                 page_num=4, total_pages=TOTAL_PAGES)

    eq_top = BODY_TOP
    eq_h = Inches(1.30)
    add_round_rect(s, MARGIN, eq_top, SLIDE_W - 2 * MARGIN, eq_h,
                   fill=KEY_BG, line_color=KEY_BORDER, line_width=1.0)
    add_text(
        s, MARGIN + Inches(0.25), eq_top + Inches(0.12),
        SLIDE_W - 2 * MARGIN - Inches(0.5), Inches(0.35),
        "Estimating equation, by layer", size=13, bold=True, color=ACCENT_RED,
    )
    add_text(
        s, MARGIN + Inches(0.25), eq_top + Inches(0.50),
        SLIDE_W - 2 * MARGIN - Inches(0.5), Inches(0.75),
        "\u0394y\u209C  =  \u03B1  +  \u03A3 \u03C6\u1D62 \u0394y\u209C\u208B\u1D62"
        "  +  \u03A3 \u03B2\u2C7C\u207A \u0394x\u207A\u209C\u208B\u2C7C"
        "  +  \u03A3 \u03B2\u2C7C\u207B \u0394x\u207B\u209C\u208B\u2C7C"
        "  +  \u03B3\u02B9 Z\u209C  +  \u03BC\u2098  +  \u03B5\u209C",
        size=22, bold=True, color=NAVY_DARK,
        align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE,
    )

    cols_top = eq_top + eq_h + Inches(0.30)
    col_h = Inches(3.30)
    col_w = (SLIDE_W - 2 * MARGIN - Inches(0.30)) / 2

    # Model features (no plain-English explanation column)
    add_round_rect(s, MARGIN, cols_top, col_w, col_h, fill=WHITE, line_color=RULE, line_width=0.75)
    add_text(s, MARGIN + Inches(0.25), cols_top + Inches(0.15), col_w - Inches(0.5), Inches(0.4),
             "Model features", size=16, bold=True, color=NAVY)
    feats = [
        "Autoregressive\u2009\u2014\u2009own lagged inflation captures persistence.",
        "Distributed lag\u2009\u2014\u2009oil enters at lags 0\u2013L.",
        "Asymmetric\u2009\u2014\u2009positive and negative shocks enter separately.",
        "Short-run focus\u2009\u2014\u2009monthly changes, no cointegration step.",
        "Controls: IIP for activity, month dummies for seasonality.",
    ]
    add_rich_text(
        s, MARGIN + Inches(0.25), cols_top + Inches(0.60), col_w - Inches(0.5), col_h - Inches(0.7),
        [
            {"runs": [{"text": "\u25AA  ", "size": 15, "color": ACCENT_RED, "bold": True},
                      {"text": f, "size": 15, "color": INK}], "space_after": 8}
            for f in feats
        ],
    )

    # Reported quantities + inference
    cx = MARGIN + col_w + Inches(0.30)
    add_round_rect(s, cx, cols_top, col_w, col_h,
                   fill=KEY_BG, line_color=KEY_BORDER, line_width=1.0)
    add_text(s, cx + Inches(0.25), cols_top + Inches(0.15), col_w - Inches(0.5), Inches(0.4),
             "Reported quantities and inference", size=16, bold=True, color=NAVY)
    items = [
        ("CPT\u207A", "sum of positive-shock coefficients across lags"),
        ("CPT\u207B", "sum of negative-shock coefficients across lags"),
        ("p-values", "tests for CPT\u207A, CPT\u207B and CPT\u207A = CPT\u207B"),
        ("Estimation", "OLS"),
        ("Inference", "Newey\u2013West HAC standard errors"),
    ]
    paras = []
    for sym, expl in items:
        paras.append({
            "runs": [
                {"text": f"  {sym}", "size": 15, "bold": True, "color": ACCENT_RED},
                {"text": "   \u2014  ", "size": 14, "color": INK_SOFT},
                {"text": expl, "size": 14, "color": INK},
            ],
            "space_after": 8,
        })
    add_rich_text(s, cx + Inches(0.25), cols_top + Inches(0.60),
                  col_w - Inches(0.5), col_h - Inches(0.7), paras)

    add_speaker_notes(
        s,
        "After the data, I will explain the model in simple words.\n\n"
        "I use a short-run asymmetric ADL model. ADL means current inflation depends on its own past values and on current and past oil shocks.\n\n"
        "This is useful because oil-price effects may not appear fully in the same month. They may spread across a few months.\n\n"
        "Positive and negative oil shocks are kept separate. This lets me check whether prices respond differently when oil rises and when oil falls.\n\n"
        "The main reported numbers are CPT plus and CPT minus. They are the total response over the lag window. I use Newey-West HAC standard errors for p-values because this is monthly time-series data.",
    )


def slide_main_results(prs, blank):
    s = prs.slides.add_slide(blank)
    slide_chrome(s, "Main result: pass-through weakens across layers",
                 page_num=5, total_pages=TOTAL_PAGES)

    headers = ["Layer", "Sample", "N", "CPT\u207A", "p", "CPT\u207B", "p",
               "Asym. p", "Reading"]

    def num(x, bold=False, color=INK):
        return (x, {"bold": bold, "color": color})

    rows = [
        ["WPI Fuel and Power", "2010-04 to 2026-03", "186",
         num("0.5205", bold=True, color=ACCENT_RED), num("<0.001", color=ACCENT_RED),
         num("0.4195", bold=True, color=ACCENT_RED), num("<0.001", color=ACCENT_RED),
         "0.1642", num("Strong wholesale fuel", bold=True, color=ACCENT_RED)],
        ["PPAC retail petrol", "2004-08 to 2024-12", "245",
         num("0.3459", bold=True, color=ACCENT_RED), num("<0.001", color=ACCENT_RED),
         num("0.1912", bold=True, color=ACCENT_RED), num("0.0002", color=ACCENT_RED),
         "0.0999", num("Strong direct fuel", bold=True, color=ACCENT_RED)],
        ["CPI Fuel and Light", "2011-05 to 2024-12", "164",
         num("0.1777", bold=True, color=ACCENT_AMBER), num("0.0021", color=ACCENT_AMBER),
         "0.1058", "0.1741",
         "0.4554", num("Bridge evidence", bold=True, color=ACCENT_AMBER)],
        ["Headline WPI", "1983-05 to 2026-03", "515",
         num("0.0301", bold=True, color=ACCENT_BLUEGREY), num("0.0240", color=ACCENT_BLUEGREY),
         num("0.0374", bold=True, color=ACCENT_BLUEGREY), num("0.0012", color=ACCENT_BLUEGREY),
         "0.6727", num("Modest but significant", bold=True, color=ACCENT_BLUEGREY)],
        ["Headline CPI", "2004-08 to 2024-12", "245",
         num("0.0213", bold=True, color=ACCENT_BLUEGREY), num("0.1220", color=ACCENT_BLUEGREY),
         num("0.0006", bold=True, color=ACCENT_BLUEGREY), num("0.9375", color=ACCENT_BLUEGREY),
         "0.2408", num("Weak, not significant", bold=True, color=ACCENT_BLUEGREY)],
    ]
    add_table(
        s, MARGIN, BODY_TOP, SLIDE_W - 2 * MARGIN, Inches(3.20),
        headers, rows,
        col_widths=[2.6, 2.4, 0.6, 1.0, 0.8, 1.0, 0.8, 1.0, 2.0],
        header_size=13, body_size=12,
        align_header=[PP_ALIGN.LEFT, PP_ALIGN.CENTER, PP_ALIGN.CENTER, PP_ALIGN.CENTER,
                      PP_ALIGN.CENTER, PP_ALIGN.CENTER, PP_ALIGN.CENTER, PP_ALIGN.CENTER,
                      PP_ALIGN.LEFT],
        align_body=[PP_ALIGN.LEFT, PP_ALIGN.CENTER, PP_ALIGN.CENTER, PP_ALIGN.RIGHT,
                    PP_ALIGN.RIGHT, PP_ALIGN.RIGHT, PP_ALIGN.RIGHT, PP_ALIGN.RIGHT,
                    PP_ALIGN.LEFT],
        highlight_rows=[0, 1, 4],
        highlight_fill=ROW_HL_STRONG,
    )

    take_top = BODY_TOP + Inches(3.45)
    add_round_rect(s, MARGIN, take_top, SLIDE_W - 2 * MARGIN, Inches(1.55),
                   fill=KEY_BG, line_color=KEY_BORDER, line_width=1.0)
    add_rich_text(
        s, MARGIN + Inches(0.30), take_top + Inches(0.15),
        SLIDE_W - 2 * MARGIN - Inches(0.6), Inches(1.30),
        [
            {"runs": [{"text": "Reading", "size": 14, "bold": True, "color": ACCENT_RED}],
             "space_after": 4},
            {"runs": [{
                "text": (
                    "Pass-through is strongest in WPI Fuel and Power and PPAC retail petrol, "
                    "smaller in CPI Fuel and Light, modest in headline WPI, and weak and "
                    "statistically insignificant in headline CPI. Diagnostics pass for each "
                    "claim-bearing specification (BG, HAC-RESET, recursive CUSUM)."
                ),
                "size": 15, "color": INK,
            }], "line_spacing": 1.30},
        ],
    )

    add_speaker_notes(
        s,
        "Now I come to the main results table.\n\n"
        "I will not read every number. The main pattern is more important.\n\n"
        "Pass-through is strongest in WPI Fuel and Power, with CPT plus around 0.52. It is also strong in PPAC retail petrol, around 0.35. CPI Fuel and Light is smaller, around 0.18, but still statistically significant.\n\n"
        "The broad headline indices are much smaller. Headline WPI is around 0.03. Headline CPI is around 0.02, but its p-value is 0.122, so it is not statistically significant.\n\n"
        "So the main message is: strong near fuel prices, weak at headline CPI.",
    )


def slide_wholesale(prs, blank):
    s = prs.slides.add_slide(blank)
    slide_chrome(s, "Wholesale results: WPI and WPI Fuel and Power",
                 page_num=6, total_pages=TOTAL_PAGES)

    left_w = Inches(5.6)
    h_top = BODY_TOP
    h_h = Inches(2.30)
    add_round_rect(s, MARGIN, h_top, left_w, h_h,
                   fill=WHITE, line_color=RULE, line_width=0.75)
    add_text(s, MARGIN + Inches(0.20), h_top + Inches(0.12), left_w - Inches(0.4), Inches(0.4),
             "Headline WPI", size=15, bold=True, color=NAVY)
    add_rich_text(
        s, MARGIN + Inches(0.20), h_top + Inches(0.50), left_w - Inches(0.4), h_h - Inches(0.55),
        [
            {"runs": [{"text": "Sample: ", "size": 14, "bold": True, "color": INK_SOFT},
                      {"text": "1983-05 to 2026-03  (N = 515)", "size": 14, "color": INK}],
             "space_after": 4},
            {"runs": [{"text": "CPT\u207A = ", "size": 14, "color": INK_SOFT},
                      {"text": "0.0301", "size": 18, "bold": True, "color": ACCENT_BLUEGREY},
                      {"text": "      p = 0.0240", "size": 14, "color": INK}],
             "space_after": 2},
            {"runs": [{"text": "CPT\u207B = ", "size": 14, "color": INK_SOFT},
                      {"text": "0.0374", "size": 18, "bold": True, "color": ACCENT_BLUEGREY},
                      {"text": "      p = 0.0012", "size": 14, "color": INK}],
             "space_after": 6},
            {"runs": [{"text": "Modest but statistically significant.",
                       "size": 14, "italic": True, "color": INK}]},
        ],
    )

    f_top = h_top + h_h + Inches(0.25)
    f_h = Inches(2.45)
    add_round_rect(s, MARGIN, f_top, left_w, f_h,
                   fill=KEY_BG, line_color=KEY_BORDER, line_width=1.0)
    add_text(s, MARGIN + Inches(0.20), f_top + Inches(0.12), left_w - Inches(0.4), Inches(0.4),
             "WPI Fuel and Power  \u00B7  preferred", size=15, bold=True, color=NAVY)
    add_rich_text(
        s, MARGIN + Inches(0.20), f_top + Inches(0.50), left_w - Inches(0.4), f_h - Inches(0.55),
        [
            {"runs": [{"text": "Sample: ", "size": 14, "bold": True, "color": INK_SOFT},
                      {"text": "2010-04 to 2026-03, excl. Apr\u2013Sep 2020 (N = 186)",
                       "size": 14, "color": INK}], "space_after": 4},
            {"runs": [{"text": "CPT\u207A = ", "size": 14, "color": INK_SOFT},
                      {"text": "0.5205", "size": 20, "bold": True, "color": ACCENT_RED},
                      {"text": "      p < 0.001", "size": 14, "color": INK}],
             "space_after": 2},
            {"runs": [{"text": "CPT\u207B = ", "size": 14, "color": INK_SOFT},
                      {"text": "0.4195", "size": 20, "bold": True, "color": ACCENT_RED},
                      {"text": "      p < 0.001", "size": 14, "color": INK}],
             "space_after": 6},
            {"runs": [{"text": "Strong wholesale fuel pass-through. Post-2010 sample, COVID months excluded.",
                       "size": 14, "italic": True, "color": INK}]},
        ],
    )

    fig_path = ROOT / "models/wpi/outputs/figures/fig_04_cumulative_passthrough.png"
    fig_l = MARGIN + left_w + Inches(0.30)
    fig_w = SLIDE_W - fig_l - MARGIN
    place_picture(s, fig_path, fig_l, BODY_TOP, fig_w, Inches(4.40))
    add_text(s, fig_l, BODY_TOP + Inches(4.45), fig_w, Inches(0.40),
             "Cumulative pass-through across WPI specifications",
             size=11, italic=True, color=INK_SOFT, align=PP_ALIGN.CENTER)

    add_speaker_notes(
        s,
        "Next I separate the wholesale results.\n\n"
        "Headline WPI shows a statistically significant response, but the size is small. This is expected because headline WPI is a broad index.\n\n"
        "WPI Fuel and Power is different. It is much closer to fuel and energy items. In the preferred post-2010 model, excluding the abnormal COVID months, the pass-through is large and statistically significant.\n\n"
        "So the wholesale evidence says that oil is clearly visible in the fuel-sensitive wholesale layer, but it becomes smaller in the broad headline WPI.",
    )


def slide_consumer_fuel(prs, blank):
    s = prs.slides.add_slide(blank)
    slide_chrome(s, "Consumer fuel layers: retail petrol and CPI Fuel and Light",
                 page_num=7, total_pages=TOTAL_PAGES)

    # Two cards stacked, each full width
    p_top = BODY_TOP
    p_h = Inches(2.30)
    add_round_rect(s, MARGIN, p_top, SLIDE_W - 2 * MARGIN, p_h,
                   fill=WHITE, line_color=RULE, line_width=0.75)
    add_text(s, MARGIN + Inches(0.25), p_top + Inches(0.12),
             SLIDE_W - 2 * MARGIN - Inches(0.5), Inches(0.4),
             "PPAC retail petrol  \u00B7  shock = Brent",
             size=16, bold=True, color=NAVY)
    add_rich_text(
        s, MARGIN + Inches(0.25), p_top + Inches(0.55),
        SLIDE_W - 2 * MARGIN - Inches(0.5), p_h - Inches(0.65),
        [
            {"runs": [
                {"text": "Sample: ", "size": 14, "bold": True, "color": INK_SOFT},
                {"text": "2004-08 to 2024-12  (N = 245)", "size": 14, "color": INK},
            ], "space_after": 6},
            {"runs": [
                {"text": "CPT\u207A = ", "size": 14, "color": INK_SOFT},
                {"text": "0.3459", "size": 20, "bold": True, "color": ACCENT_RED},
                {"text": "      p < 0.001", "size": 14, "color": INK},
                {"text": "         |         ", "size": 14, "color": INK_SOFT},
                {"text": "CPT\u207B = ", "size": 14, "color": INK_SOFT},
                {"text": "0.1912", "size": 20, "bold": True, "color": ACCENT_RED},
                {"text": "      p = 0.0002", "size": 14, "color": INK},
            ], "space_after": 6},
            {"runs": [
                {"text": "Asymmetry p = 0.0999 (marginal at 10%). Strong direct fuel pass-through.",
                 "size": 14, "italic": True, "color": INK},
            ]},
        ],
    )

    c_top = p_top + p_h + Inches(0.25)
    c_h = Inches(2.45)
    add_round_rect(s, MARGIN, c_top, SLIDE_W - 2 * MARGIN, c_h,
                   fill=KEY_BG, line_color=KEY_BORDER, line_width=1.0)
    add_text(s, MARGIN + Inches(0.25), c_top + Inches(0.12),
             SLIDE_W - 2 * MARGIN - Inches(0.5), Inches(0.4),
             "CPI Fuel and Light  \u00B7  shock = PPAC retail petrol",
             size=16, bold=True, color=NAVY)
    add_rich_text(
        s, MARGIN + Inches(0.25), c_top + Inches(0.55),
        SLIDE_W - 2 * MARGIN - Inches(0.5), c_h - Inches(0.65),
        [
            {"runs": [
                {"text": "Sample: ", "size": 14, "bold": True, "color": INK_SOFT},
                {"text": "2011-05 to 2024-12  (N = 164)", "size": 14, "color": INK},
            ], "space_after": 6},
            {"runs": [
                {"text": "CPT\u207A = ", "size": 14, "color": INK_SOFT},
                {"text": "0.1777", "size": 20, "bold": True, "color": ACCENT_AMBER},
                {"text": "      p = 0.0021", "size": 14, "color": INK},
                {"text": "         |         ", "size": 14, "color": INK_SOFT},
                {"text": "CPT\u207B = ", "size": 14, "color": INK_SOFT},
                {"text": "0.1058", "size": 20, "bold": True, "color": ACCENT_BLUEGREY},
                {"text": "      p = 0.1741", "size": 14, "color": INK},
            ], "space_after": 6},
            {"runs": [
                {"text": "Bridge from retail fuel to the consumer fuel basket; effect smaller than upstream petrol.",
                 "size": 14, "italic": True, "color": INK},
            ]},
        ],
    )

    add_speaker_notes(
        s,
        "After the wholesale side, I move to the consumer fuel side.\n\n"
        "Retail petrol responds strongly to Brent crude shocks. This is the direct fuel layer, so a stronger response is expected.\n\n"
        "Then I look at CPI Fuel and Light. Here the shock variable is PPAC retail petrol. The positive pass-through is smaller than retail petrol, but it is still statistically significant.\n\n"
        "This slide supports the bridge idea. Oil first appears strongly in retail fuel, and then a smaller part appears in the fuel-sensitive consumer category.",
    )


def slide_headline_cpi(prs, blank):
    s = prs.slides.add_slide(blank)
    slide_chrome(s, "Headline CPI: where the oil signal becomes weak",
                 page_num=8, total_pages=TOTAL_PAGES)

    left_w = Inches(5.5)
    add_round_rect(s, MARGIN, BODY_TOP, left_w, Inches(4.85),
                   fill=KEY_BG, line_color=KEY_BORDER, line_width=1.0)
    add_text(s, MARGIN + Inches(0.20), BODY_TOP + Inches(0.12), left_w - Inches(0.4), Inches(0.4),
             "Headline CPI model", size=16, bold=True, color=NAVY)
    add_rich_text(
        s, MARGIN + Inches(0.20), BODY_TOP + Inches(0.55), left_w - Inches(0.4), Inches(2.5),
        [
            {"runs": [{"text": "Sample: ", "size": 14, "bold": True, "color": INK_SOFT},
                      {"text": "2004-08 to 2024-12  (N = 245)", "size": 14, "color": INK}],
             "space_after": 8},
            {"runs": [{"text": "CPT\u207A = ", "size": 14, "color": INK_SOFT},
                      {"text": "0.0213", "size": 22, "bold": True, "color": ACCENT_BLUEGREY},
                      {"text": "    p = 0.1220", "size": 14, "color": INK}],
             "space_after": 6},
            {"runs": [{"text": "CPT\u207B = ", "size": 14, "color": INK_SOFT},
                      {"text": "0.0006", "size": 22, "bold": True, "color": ACCENT_BLUEGREY},
                      {"text": "    p = 0.9375", "size": 14, "color": INK}],
             "space_after": 6},
            {"runs": [{"text": "Asymmetry p = 0.2408", "size": 14, "color": INK}]},
        ],
    )
    add_text(s, MARGIN + Inches(0.20), BODY_TOP + Inches(3.10), left_w - Inches(0.4), Inches(0.4),
             "Reading", size=14, bold=True, color=ACCENT_RED)
    reads = [
        "Positive CPT\u207A has the expected sign but is not significant.",
        "Headline CPI is broad and food-heavy; fuel weight is limited.",
        "Taxes, margins, and policy can absorb part of the shock.",
        "This is attenuation, not absence.",
    ]
    add_rich_text(
        s, MARGIN + Inches(0.20), BODY_TOP + Inches(3.45), left_w - Inches(0.4), Inches(1.35),
        [
            {"runs": [{"text": "\u25AA  ", "size": 14, "color": ACCENT_RED, "bold": True},
                      {"text": r, "size": 14, "color": INK}], "space_after": 4}
            for r in reads
        ],
    )

    fig_path = ROOT / "models/cpi/outputs/figures/fig_13_dilution_chain.png"
    fig_l = MARGIN + left_w + Inches(0.30)
    fig_w = SLIDE_W - fig_l - MARGIN
    place_picture(s, fig_path, fig_l, BODY_TOP, fig_w, Inches(4.40))
    add_text(s, fig_l, BODY_TOP + Inches(4.45), fig_w, Inches(0.40),
             "Cumulative positive pass-through across the consumer-price chain",
             size=11, italic=True, color=INK_SOFT, align=PP_ALIGN.CENTER)

    add_speaker_notes(
        s,
        "Now I move to the final consumer endpoint, headline CPI.\n\n"
        "This is an important slide because headline CPI is the main inflation measure for consumers and policy.\n\n"
        "The positive coefficient has the expected sign, but the p-value is 0.122. So I cannot say it is statistically significant at conventional levels.\n\n"
        "This does not mean oil is irrelevant. It means that by the time the shock reaches the broad CPI basket, the effect is weak. CPI includes many non-fuel items, and taxes, margins, and basket weights can absorb part of the oil shock.\n\n"
        "So my safe interpretation is attenuation, not absence.",
    )


def slide_attenuation(prs, blank):
    s = prs.slides.add_slide(blank)
    slide_chrome(s, "Attenuation across the consumer chain",
                 page_num=9, total_pages=TOTAL_PAGES)

    left_w = Inches(6.6)

    def num(x, bold=False, color=INK):
        return (x, {"bold": bold, "color": color})

    headers = ["Stage", "Relationship", "CPT\u207A", "p"]
    rows = [
        [num("Stage 1", bold=True), "Brent \u2192 PPAC retail petrol",
         num("0.4007", bold=True, color=ACCENT_RED),
         num("0.0001", color=ACCENT_RED)],
        [num("Stage 2", bold=True), "PPAC petrol \u2192 CPI Fuel and Light",
         num("0.1777", bold=True, color=ACCENT_AMBER),
         num("0.0021", color=ACCENT_AMBER)],
        [num("Stage 3", bold=True), "Rupee oil \u2192 Headline CPI",
         num("0.0064", bold=True, color=ACCENT_BLUEGREY),
         num("0.6355", color=ACCENT_BLUEGREY)],
    ]
    add_table(
        s, MARGIN, BODY_TOP, left_w, Inches(2.10), headers, rows,
        col_widths=[1.4, 3.4, 1.0, 0.8],
        align_header=[PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.RIGHT, PP_ALIGN.RIGHT],
        align_body=[PP_ALIGN.LEFT, PP_ALIGN.LEFT, PP_ALIGN.RIGHT, PP_ALIGN.RIGHT],
        body_size=13, header_size=13,
    )

    # Simplified attenuation panel
    comp_top = BODY_TOP + Inches(2.40)
    add_round_rect(s, MARGIN, comp_top, left_w, Inches(2.45),
                   fill=KEY_BG, line_color=KEY_BORDER, line_width=1.0)
    add_text(s, MARGIN + Inches(0.25), comp_top + Inches(0.12),
             left_w - Inches(0.5), Inches(0.4),
             "Pass-through shrinks across stages", size=15, bold=True, color=NAVY)
    add_rich_text(
        s, MARGIN + Inches(0.25), comp_top + Inches(0.55), left_w - Inches(0.5), Inches(1.85),
        [
            {"runs": [
                {"text": "Stage 1 vs Stage 3 ratio:  ", "size": 15, "color": INK_SOFT},
                {"text": "0.40 / 0.006 \u2248 ", "size": 16, "color": INK},
                {"text": "63\u00D7 smaller", "size": 18, "bold": True, "color": ACCENT_RED},
            ], "space_after": 8},
            {"runs": [
                {"text": "Coefficient-equality test (Stage 1 = Stage 3):  ", "size": 15, "color": INK_SOFT},
                {"text": "F = 14.35,  p = 0.0002", "size": 16, "bold": True, "color": ACCENT_RED},
            ], "space_after": 6},
            {"runs": [
                {"text": "Equality is rejected; the headline-CPI response is significantly smaller "
                         "than the upstream retail-petrol response.",
                 "size": 14, "color": INK},
            ]},
        ],
    )

    fig_path = ROOT / "models/cpi/outputs/figures/fig_13b_dilution_common_sample.png"
    fig_l = MARGIN + left_w + Inches(0.30)
    fig_w = SLIDE_W - fig_l - MARGIN
    place_picture(s, fig_path, fig_l, BODY_TOP, fig_w, Inches(4.85))

    add_speaker_notes(
        s,
        "After showing the headline CPI result, I test the attenuation pattern more directly.\n\n"
        "Here I use a common-sample consumer chain. Stage 1 is Brent to retail petrol. Stage 2 is retail petrol to CPI Fuel and Light. Stage 3 is rupee oil to headline CPI.\n\n"
        "The numbers fall from about 0.40 in Stage 1 to about 0.18 in Stage 2 and almost zero in Stage 3.\n\n"
        "The Wald test compares Stage 1 and Stage 3. The p-value is 0.0002, so equality is rejected. This means the fall in pass-through is statistically supported, not just a visual pattern.",
    )


def slide_discussion_policy(prs, blank):
    s = prs.slides.add_slide(blank)
    slide_chrome(s, "Discussion and policy relevance",
                 page_num=10, total_pages=TOTAL_PAGES)

    add_round_rect(s, MARGIN, BODY_TOP, SLIDE_W - 2 * MARGIN, Inches(0.90),
                   fill=KEY_BG, line_color=KEY_BORDER, line_width=1.0)
    add_text(
        s, MARGIN + Inches(0.30), BODY_TOP + Inches(0.12),
        SLIDE_W - 2 * MARGIN - Inches(0.6), Inches(0.65),
        "Pass-through falls sharply: retail petrol 0.4007 → CPI Fuel 0.1777 → headline CPI 0.0064.",
        size=18, bold=True, color=NAVY, anchor=MSO_ANCHOR.MIDDLE,
    )

    cols_top = BODY_TOP + Inches(1.15)
    col_w = (SLIDE_W - 2 * MARGIN - Inches(0.30)) / 2
    col_h = Inches(3.95)

    add_round_rect(s, MARGIN, cols_top, col_w, col_h, fill=WHITE, line_color=RULE, line_width=0.75)
    add_text(s, MARGIN + Inches(0.25), cols_top + Inches(0.15), col_w - Inches(0.5), Inches(0.4),
             "What the results mean", size=15, bold=True, color=NAVY)
    a = [
        "Oil is clearly visible in fuel prices.",
        "The CPI Fuel and Light response is smaller, but still significant.",
        "Headline CPI dilutes the oil signal across a broad basket.",
        "The main result is attenuation across layers.",
    ]
    add_rich_text(
        s, MARGIN + Inches(0.25), cols_top + Inches(0.60), col_w - Inches(0.5), col_h - Inches(0.7),
        [
            {"runs": [{"text": "\u25AA  ", "size": 15, "color": ACCENT_RED, "bold": True},
                      {"text": x, "size": 15, "color": INK}], "space_after": 10}
            for x in a
        ],
    )

    cx = MARGIN + col_w + Inches(0.30)
    add_round_rect(s, cx, cols_top, col_w, col_h, fill=WHITE, line_color=RULE, line_width=0.75)
    add_text(s, cx + Inches(0.25), cols_top + Inches(0.15), col_w - Inches(0.5), Inches(0.4),
             "Policy focus", size=15, bold=True, color=NAVY)
    b = [
        "Do not rely only on headline CPI.",
        "Track retail fuel, WPI Fuel and Power, and CPI Fuel and Light.",
        "Watch transport and input costs for second-round pressure.",
        "Fuel taxes and pricing choices can change pass-through.",
    ]
    add_rich_text(
        s, cx + Inches(0.25), cols_top + Inches(0.60), col_w - Inches(0.5), col_h - Inches(0.7),
        [
            {"runs": [{"text": "\u25AA  ", "size": 15, "color": ACCENT_AMBER, "bold": True},
                      {"text": x, "size": 15, "color": INK}], "space_after": 10}
            for x in b
        ],
    )

    add_round_rect(s, MARGIN, Inches(6.25), SLIDE_W - 2 * MARGIN, Inches(0.62),
                   fill=CALLOUT_BG, line_color=CALLOUT_BORDER, line_width=0.75)
    add_text(
        s, MARGIN + Inches(0.30), Inches(6.25),
        SLIDE_W - 2 * MARGIN - Inches(0.6), Inches(0.62),
        "Policy message: oil pressure can build in fuel layers before it appears in headline CPI.",
        size=15, bold=True, color=ACCENT_AMBER, anchor=MSO_ANCHOR.MIDDLE,
    )

    add_speaker_notes(
        s,
        "After the attenuation test, I will explain what the result means.\n\n"
        "The numbers fall sharply across the consumer chain. Retail petrol responds strongly. CPI Fuel and Light responds less, but still significantly. Headline CPI is almost zero in the common-sample chain.\n\n"
        "This makes sense because headline CPI is a broad basket. Fuel is only one part of it. So the oil signal becomes weaker when it is mixed with food, services, housing, and other items.\n\n"
        "For policy, the important point is monitoring. Headline CPI alone may miss pressure building in fuel-sensitive layers. Retail fuel, WPI Fuel and Power, and CPI Fuel and Light should be watched together.\n\n"
        "The model does not prove one exact policy action. It shows that policy should separate direct fuel shocks from wider second-round inflation.",
    )


def slide_conclusion(prs, blank):
    s = prs.slides.add_slide(blank)
    slide_chrome(s, "Conclusion: oil pass-through is layered and attenuated",
                 page_num=11, total_pages=TOTAL_PAGES)

    add_round_rect(s, MARGIN, BODY_TOP, SLIDE_W - 2 * MARGIN, Inches(1.10),
                   fill=NAVY, line_color=NAVY)
    add_text(
        s, MARGIN + Inches(0.30), BODY_TOP + Inches(0.10),
        SLIDE_W - 2 * MARGIN - Inches(0.6), Inches(0.95),
        "Oil shocks matter in India, but their effect weakens across the price system.",
        size=20, bold=True, color=WHITE, italic=True, anchor=MSO_ANCHOR.MIDDLE,
    )

    cols_top = BODY_TOP + Inches(1.30)
    col_w = (SLIDE_W - 2 * MARGIN - Inches(0.30)) / 2
    col_h = Inches(3.20)

    add_round_rect(s, MARGIN, cols_top, col_w, col_h, fill=WHITE, line_color=RULE, line_width=0.75)
    add_text(s, MARGIN + Inches(0.25), cols_top + Inches(0.15), col_w - Inches(0.5), Inches(0.4),
             "Findings by layer", size=15, bold=True, color=NAVY)
    findings = [
        ("Strong", "WPI Fuel and Power and PPAC retail petrol", ACCENT_RED),
        ("Bridge", "CPI Fuel and Light: smaller but significant", ACCENT_AMBER),
        ("Modest", "Headline WPI: small, statistically significant", ACCENT_BLUEGREY),
        ("Weak", "Headline CPI: not statistically significant", ACCENT_BLUEGREY),
    ]
    add_rich_text(
        s, MARGIN + Inches(0.25), cols_top + Inches(0.60), col_w - Inches(0.5), col_h - Inches(0.7),
        [
            {"runs": [{"text": f"{tag}  ", "size": 14, "bold": True, "color": col},
                      {"text": "\u2014  ", "size": 14, "color": INK_SOFT},
                      {"text": text, "size": 14, "color": INK}], "space_after": 10}
            for tag, text, col in findings
        ],
    )

    cx = MARGIN + col_w + Inches(0.30)
    add_round_rect(s, cx, cols_top, col_w, col_h,
                   fill=KEY_BG, line_color=KEY_BORDER, line_width=1.0)
    add_text(s, cx + Inches(0.25), cols_top + Inches(0.15), col_w - Inches(0.5), Inches(0.4),
             "Takeaways", size=15, bold=True, color=NAVY)
    why = [
        "Attenuation pattern is visible at every step of the consumer chain.",
        "Stage 1 vs Stage 3 ratio: about 63\u00D7 smaller; equality test rejected.",
        "Asymmetry is not the central result; only retail petrol is marginal.",
        "Fuel-only and headline-CPI views give different policy reads.",
    ]
    add_rich_text(
        s, cx + Inches(0.25), cols_top + Inches(0.60), col_w - Inches(0.5), col_h - Inches(0.7),
        [
            {"runs": [{"text": "\u25AA  ", "size": 14, "color": ACCENT_RED, "bold": True},
                      {"text": w, "size": 14, "color": INK}], "space_after": 10}
            for w in why
        ],
    )

    add_round_rect(s, MARGIN, Inches(6.20), SLIDE_W - 2 * MARGIN, Inches(0.70),
                   fill=CALLOUT_BG, line_color=CALLOUT_BORDER, line_width=0.75)
    add_text(
        s, MARGIN + Inches(0.30), Inches(6.20),
        SLIDE_W - 2 * MARGIN - Inches(0.6), Inches(0.70),
        "Attenuation, not absence, of oil-price transmission.",
        size=15, bold=True, color=ACCENT_AMBER, anchor=MSO_ANCHOR.MIDDLE,
    )

    add_speaker_notes(
        s,
        "To conclude, the central finding is layered attenuation.\n\n"
        "Oil shocks matter in India, but the effect is not equally strong everywhere. It is strong in WPI Fuel and Power and retail petrol. It is smaller in CPI Fuel and Light. It is modest in headline WPI. It is weak and not statistically significant in headline CPI.\n\n"
        "The formal attenuation test also supports this result.\n\n"
        "So my final conclusion is simple: oil-price transmission is present, but it becomes diluted before reaching headline CPI.\n\n"
        "Thank you. I am happy to take your questions.",
    )


def slide_thank_you(prs, blank):
    s = prs.slides.add_slide(blank)
    add_rectangle(s, 0, 0, SLIDE_W, SLIDE_H, fill=WHITE)
    add_rectangle(s, 0, 0, SLIDE_W, Inches(0.10), fill=NAVY)
    add_rectangle(s, 0, Inches(7.40), SLIDE_W, Inches(0.10), fill=NAVY)
    add_text(s, MARGIN, Inches(2.6), SLIDE_W - 2 * MARGIN, Inches(1.2),
             "Thank you", size=66, bold=True, color=NAVY,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_text(s, MARGIN, Inches(3.9), SLIDE_W - 2 * MARGIN, Inches(0.7),
             "Questions are welcome.",
             size=22, italic=True, color=INK_SOFT,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    add_rectangle(s, SLIDE_W / 2 - Inches(1.0), Inches(4.85),
                  Inches(2.0), Inches(0.04), fill=ACCENT_RED)
    add_text(s, MARGIN, Inches(5.10), SLIDE_W - 2 * MARGIN, Inches(0.6),
             "Aniket Pandey  \u00B7  B.Tech + MS Economics  \u00B7  School Of Engineering, JNU",
             size=14, color=INK_SOFT, align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)


# ----------------------------------------------------------------------------
def make_presentation():
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    blank = prs.slide_layouts[6]

    slide_title(prs, blank)
    slide_motivation(prs, blank)
    slide_objective(prs, blank)
    slide_data(prs, blank)
    slide_methodology(prs, blank)
    slide_main_results(prs, blank)
    slide_wholesale(prs, blank)
    slide_consumer_fuel(prs, blank)
    slide_headline_cpi(prs, blank)
    slide_attenuation(prs, blank)
    slide_discussion_policy(prs, blank)
    slide_conclusion(prs, blank)
    slide_thank_you(prs, blank)
    return prs


def main():
    prs = make_presentation()
    prs.save(OUT)
    print(f"Saved: {OUT}")


if __name__ == "__main__":
    main()
