"""Build dissertation.docx with proper OMML equations and thesis page layout."""
from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml.ns import qn, nsmap
from docx.oxml import OxmlElement, parse_xml
import os

ROOT = "/Users/aniketpandey/Desktop/fresh-dissertation"
OUT = os.path.join(ROOT, "dissertation.docx")

doc = Document()

# ============================================================
# Page setup: A4, fixed one-sided thesis margins
# ============================================================
for section in doc.sections:
    section.page_height = Cm(29.7)
    section.page_width = Cm(21.0)
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Cm(3.54)
    section.right_margin = Inches(1)
    sectPr = section._sectPr

    # Do not use Word mirror margins here. This dissertation file is prepared
    # as a one-sided submission draft, so mirroring makes the text block shift
    # left/right from page to page in PDF review.
    for existing in sectPr.findall(qn('w:mirrorMargins')):
        sectPr.remove(existing)

    # Gutter zero so the binding margin is exactly the explicit left margin.
    pgMar = sectPr.find(qn('w:pgMar'))
    if pgMar is not None:
        pgMar.set(qn('w:gutter'), '0')

# Remove document-level mirror margins so Word does not alternate the inside
# margin between odd and even pages.
settings_el = doc.settings.element
for existing in settings_el.findall(qn('w:mirrorMargins')):
    settings_el.remove(existing)


def force_tnr(style):
    style.font.name = 'Times New Roman'
    rpr = style.element.get_or_add_rPr()
    rfonts = rpr.find(qn('w:rFonts'))
    if rfonts is None:
        rfonts = OxmlElement('w:rFonts')
        rpr.append(rfonts)
    for k in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'):
        rfonts.set(qn(k), 'Times New Roman')


# Normal style
normal = doc.styles['Normal']
normal.font.size = Pt(12)
force_tnr(normal)
pf = normal.paragraph_format
pf.line_spacing = 1.5
pf.space_after = Pt(6)
pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

# Heading 1 (Chapter title) - centered, large bold
h1 = doc.styles['Heading 1']
h1.font.size = Pt(20)
h1.font.bold = True
h1.font.color.rgb = RGBColor(0, 0, 0)
force_tnr(h1)
h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
h1.paragraph_format.space_before = Pt(24)
h1.paragraph_format.space_after = Pt(18)
h1.paragraph_format.keep_with_next = True
h1.paragraph_format.line_spacing = 1.5

# Heading 2 (Section)
h2 = doc.styles['Heading 2']
h2.font.size = Pt(14)
h2.font.bold = True
h2.font.color.rgb = RGBColor(0, 0, 0)
force_tnr(h2)
h2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
h2.paragraph_format.space_before = Pt(14)
h2.paragraph_format.space_after = Pt(6)
h2.paragraph_format.keep_with_next = True
h2.paragraph_format.line_spacing = 1.5

# Heading 3 (Subsection)
h3 = doc.styles['Heading 3']
h3.font.size = Pt(12)
h3.font.bold = True
h3.font.color.rgb = RGBColor(0, 0, 0)
force_tnr(h3)
h3.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
h3.paragraph_format.space_before = Pt(10)
h3.paragraph_format.space_after = Pt(4)
h3.paragraph_format.keep_with_next = True
h3.paragraph_format.line_spacing = 1.5

# Caption style for Word-generated figure/table lists later.
caption_style = doc.styles['Caption']
caption_style.font.size = Pt(10)
caption_style.font.color.rgb = RGBColor(0, 0, 0)
force_tnr(caption_style)
caption_style.paragraph_format.line_spacing = 1.0
caption_style.paragraph_format.space_before = Pt(3)
caption_style.paragraph_format.space_after = Pt(6)


# ============================================================
# Helpers
# ============================================================
def add_para(text, bold=False, italic=False, align=None, first_line_indent=None):
    p = doc.add_paragraph()
    if align is not None:
        p.alignment = align
    if first_line_indent is not None:
        p.paragraph_format.first_line_indent = first_line_indent
    r = p.add_run(text)
    r.bold = bold
    r.italic = italic
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    return p


def chapter_heading(chapter_num_text, title_text):
    """Two-line centered Heading 1: 'Chapter N' / 'Title'."""
    p = doc.add_paragraph(style='Heading 1')
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r1 = p.add_run(chapter_num_text)
    r1.bold = True
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(20)
    r1.add_break()
    r2 = p.add_run(title_text)
    r2.bold = True
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(20)


def section_heading(text):
    p = doc.add_paragraph(style='Heading 2')
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = p.add_run(text)
    r.bold = True
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)


def subsection_heading(text):
    p = doc.add_paragraph(style='Heading 3')
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = p.add_run(text)
    r.bold = True
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)


def page_break():
    p = doc.add_paragraph()
    p.add_run().add_break(WD_BREAK.PAGE)


def add_figure(path, caption, width_in=5.5):
    if os.path.exists(path):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(2)
        p.add_run().add_picture(path, width=Inches(width_in))
        cp = doc.add_paragraph(style='Caption')
        cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        cr = cp.add_run(caption)
        cr.italic = True
        cr.font.size = Pt(10)
        cr.font.name = 'Times New Roman'
    else:
        add_para(f"[FIGURE NOT FOUND: {path}]", italic=True)


def add_table(headers, rows, caption=None, col_widths=None, font_size=10):
    """col_widths must sum to ~5.8 inches (A4 fixed-margin text width)."""
    if caption:
        cp = doc.add_paragraph(style='Caption')
        cp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        cr = cp.add_run(caption)
        cr.bold = True
        cr.font.size = Pt(11)
        cr.font.name = 'Times New Roman'
    t = doc.add_table(rows=1 + len(rows), cols=len(headers))
    try:
        t.style = 'Table Grid'
    except KeyError:
        pass
    t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    t.autofit = False

    # Force fixed layout
    tbl = t._tbl
    tblPr = tbl.tblPr
    # tblLayout fixed
    layout = OxmlElement('w:tblLayout')
    layout.set(qn('w:type'), 'fixed')
    tblPr.append(layout)
    # tblW total in dxa (twips); 1 inch = 1440 twips
    if col_widths:
        total_twips = int(sum(col_widths) * 1440)
        tblW = tblPr.find(qn('w:tblW'))
        if tblW is None:
            tblW = OxmlElement('w:tblW')
            tblPr.append(tblW)
        tblW.set(qn('w:w'), str(total_twips))
        tblW.set(qn('w:type'), 'dxa')
        # Build/replace tblGrid
        old_grid = tbl.find(qn('w:tblGrid'))
        if old_grid is not None:
            tbl.remove(old_grid)
        grid = OxmlElement('w:tblGrid')
        for w in col_widths:
            gc = OxmlElement('w:gridCol')
            gc.set(qn('w:w'), str(int(w * 1440)))
            grid.append(gc)
        # Insert tblGrid right after tblPr
        tbl.insert(list(tbl).index(tblPr) + 1, grid)
        # Set each cell width
        for row in t.rows:
            for ci, cell in enumerate(row.cells):
                tcPr = cell._tc.get_or_add_tcPr()
                tcW = tcPr.find(qn('w:tcW'))
                if tcW is None:
                    tcW = OxmlElement('w:tcW')
                    tcPr.append(tcW)
                tcW.set(qn('w:w'), str(int(col_widths[ci] * 1440)))
                tcW.set(qn('w:type'), 'dxa')

    hdr = t.rows[0].cells
    for i, h in enumerate(headers):
        hdr[i].text = ''
        para = hdr[i].paragraphs[0]
        run = para.add_run(h)
        run.bold = True
        run.font.size = Pt(font_size)
        run.font.name = 'Times New Roman'
        para.alignment = WD_ALIGN_PARAGRAPH.CENTER
        para.paragraph_format.space_after = Pt(0)
    for ri, row in enumerate(rows, start=1):
        cells = t.rows[ri].cells
        for ci, val in enumerate(row):
            cells[ci].text = ''
            para = cells[ci].paragraphs[0]
            run = para.add_run(str(val))
            run.font.size = Pt(font_size)
            run.font.name = 'Times New Roman'
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT if ci == 0 else WD_ALIGN_PARAGRAPH.CENTER
            para.paragraph_format.space_after = Pt(0)
    trPr = t.rows[0]._tr.get_or_add_trPr()
    tblHeader = OxmlElement('w:tblHeader')
    trPr.append(tblHeader)
    return t


def add_note(text):
    p = doc.add_paragraph()
    r = p.add_run("Notes: " + text)
    r.italic = True
    r.font.size = Pt(10)
    r.font.name = 'Times New Roman'
    p.paragraph_format.space_after = Pt(10)


# ============================================================
# OMML equation helpers
# ============================================================
M_NS = 'http://schemas.openxmlformats.org/officeDocument/2006/math'


W_NS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'


def add_equation(omml_inner, label=None):
    """Insert a numbered display equation inline at the current document position.

    Uses doc.add_paragraph() so the paragraph is correctly inserted before the
    body's section properties, and then appends OMML and label runs as children
    of that paragraph. This is the standard OOXML pattern for numbered equations.
    """
    p = doc.add_paragraph()
    p_elem = p._p
    pPr = p_elem.get_or_add_pPr()

    tabs = OxmlElement('w:tabs')
    for val, pos in [('center', '4230'), ('right', '8460')]:
        tab = OxmlElement('w:tab')
        tab.set(qn('w:val'), val)
        tab.set(qn('w:pos'), pos)
        tabs.append(tab)
    pPr.append(tabs)

    spacing = OxmlElement('w:spacing')
    spacing.set(qn('w:before'), '120')
    spacing.set(qn('w:after'), '120')
    spacing.set(qn('w:line'), '360')
    spacing.set(qn('w:lineRule'), 'auto')
    pPr.append(spacing)

    # leading tab to push to centre stop
    p_elem.append(parse_xml(
        f'<w:r xmlns:w="{W_NS}"><w:tab/></w:r>'
    ))
    # the equation itself
    p_elem.append(parse_xml(
        f'<m:oMath xmlns:m="{M_NS}">{omml_inner}</m:oMath>'
    ))
    # right-aligned label
    if label:
        p_elem.append(parse_xml(
            f'<w:r xmlns:w="{W_NS}">'
            f'<w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="24"/></w:rPr>'
            f'<w:tab/><w:t xml:space="preserve">{label}</w:t></w:r>'
        ))
    return p


def add_para_math(text, align=None, first_line_indent=None):
    """Add a paragraph that interprets _x, _{xx}, ^x, ^{xx} as sub/superscripts.

    Plain text is rendered as Times New Roman 12 pt; sub/superscript spans
    use the same font at the same nominal size with sub/superscript on.
    """
    p = doc.add_paragraph()
    if align is not None:
        p.alignment = align
    else:
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if first_line_indent is not None:
        p.paragraph_format.first_line_indent = first_line_indent

    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        if c in ('_', '^'):
            sub = (c == '_')
            i += 1
            if i < n and text[i] == '{':
                j = text.index('}', i)
                content = text[i + 1:j]
                i = j + 1
            elif i < n:
                content = text[i]
                i += 1
            else:
                content = ''
            r = p.add_run(content)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(12)
            if sub:
                r.font.subscript = True
            else:
                r.font.superscript = True
        else:
            j = i
            while j < n and text[j] not in ('_', '^'):
                j += 1
            r = p.add_run(text[i:j])
            r.font.name = 'Times New Roman'
            r.font.size = Pt(12)
            i = j
    return p


def mr(text):
    """Math run."""
    # Escape XML special chars
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    return f'<m:r><m:t xml:space="preserve">{text}</m:t></m:r>'


def msub(base, sub):
    return f'<m:sSub><m:e>{base}</m:e><m:sub>{sub}</m:sub></m:sSub>'


def msup(base, sup):
    return f'<m:sSup><m:e>{base}</m:e><m:sup>{sup}</m:sup></m:sSup>'


def msubsup(base, sub, sup):
    return f'<m:sSubSup><m:e>{base}</m:e><m:sub>{sub}</m:sub><m:sup>{sup}</m:sup></m:sSubSup>'


def mfenced(inner):
    return f'<m:d><m:dPr><m:begChr m:val="("/><m:endChr m:val=")"/></m:dPr><m:e>{inner}</m:e></m:d>'


def mnary_sum(sub, sup, body):
    """Sigma summation with limUpp for display."""
    return (
        '<m:nary>'
        '<m:naryPr><m:chr m:val="∑"/><m:limLoc m:val="undOvr"/><m:subHide m:val="0"/><m:supHide m:val="0"/></m:naryPr>'
        f'<m:sub>{sub}</m:sub><m:sup>{sup}</m:sup><m:e>{body}</m:e>'
        '</m:nary>'
    )


# ============================================================
# ABSTRACT
# ============================================================
chapter_heading("", "Abstract")
add_para(
    "India imports around 87% of its crude petroleum, yet oil-price shocks do not pass evenly through the domestic price system. This dissertation studies oil-price pass-through in India as a layered transmission process rather than as a single coefficient on the wholesale price index (WPI) or the consumer price index (CPI). The shock is traced across four points in the chain: international Brent crude in rupee terms, retail petrol prices at the pump, fuel-sensitive sub-indices of the wholesale and consumer price indices, and the two headline aggregates. Monthly data are drawn from official WPI series spliced to the 2011-12 base, Petroleum Planning and Analysis Cell (PPAC) retail fuel prices, Brent crude prices, the INR/USD exchange rate, and CPI series, with the WPI evidence covering a long historical sample from 1983 and the CPI and PPAC retail fuel evidence covering the shorter but policy-relevant post-2004 period. The estimates use short-run asymmetric autoregressive distributed lag (ADL) models in log differences with Newey-West HAC inference, cumulative pass-through tests, and a restricted-residual circular block bootstrap with 4,999 replications for symmetry checks. The evidence shows a clear ordering. Retail petrol and WPI Fuel and Power respond strongly to rupee oil shocks; headline WPI responds significantly but with a much smaller coefficient; headline CPI shows only weak positive pass-through and no reliable evidence of short-run asymmetry. The pre/post-2010 WPI split is consistent with stronger pass-through after the move toward more market-linked fuel pricing, although it should be read as institutional evidence rather than a clean causal estimate of deregulation. The conclusion is that oil shocks are not absent from Indian prices; they are absorbed unevenly, with much of the shock diluted before it reaches headline consumer inflation."
)
page_break()

# ============================================================
# CHAPTER 1
# ============================================================
chapter_heading("Chapter 1", "Introduction")

section_heading("1.1 Motivation and Empirical Puzzle")
add_para(
    "India imports around 87% of the crude petroleum it consumes; therefore, the rupee value of imported oil is one of the more important external cost shocks absorbed by the domestic price system. Because crude is invoiced internationally in United States dollars, the domestic shock is in fact two-dimensional: the dollar oil price and the INR/USD exchange rate together determine the rupee oil price that enters refining margins, distribution, and final demand. However, how this shock flows through the Indian price system is neither even nor unmediated. The same oil shock that visibly alters retail petrol prices at the pump can leave only a faint signature on headline consumer inflation, the index that anchors monetary policy. This is the empirical puzzle that this dissertation examines."
)
add_para(
    "The puzzle is not a contradiction. It is instead a sign that the shock weakens somewhere inside the price system. A rupee oil shock can move directly through retail fuel prices and through fuel-sensitive sub-indices of the wholesale and consumer price indices; it can move indirectly through transport costs, packaging, fertiliser, and industrial inputs; and it can be partially absorbed by inventories, by oil marketing companies, by state and central excise adjustments, and by the small direct weight of fuel in the overall consumer basket. Each of these stages dilutes a portion of the shock. Treating the pass-through as a single elasticity between Brent and headline CPI hides where this dilution occurs. Therefore, instead of analysing oil-price pass-through as a simple elasticity, this dissertation analyses the layered transmission process across the four points of the chain that matter most for inflation diagnostics."
)

section_heading("1.2 Research Question and Approach")
add_para(
    "The research question asked here is intentionally architectural: how do global oil-price shocks transmit across India's wholesale, retail fuel, fuel-sensitive consumer, and headline consumer price layers, and where does the pass-through weaken? The framing is not whether oil affects CPI, nor whether pass-through is asymmetric. Those are secondary questions. The main framing is transmission and attenuation across layers."
)
add_para(
    "To estimate pass-through at these points in the chain, the dissertation employs short-run asymmetric ADL models in log differences with Newey-West heteroscedasticity-and-autocorrelation-consistent inference. Positive and negative oil-change components are entered separately, cumulative pass-through coefficients are summarised across the lag window, and a Wald test is used to ask whether the positive and negative cumulative effects are equal. Symmetry is also assessed using a restricted-residual circular block bootstrap with 4,999 replications. Granger-causality tests and Bai-Perron structural break tests are used to support the directional reading of the chain rather than to claim structural causality."
)

section_heading("1.3 Main Findings")
add_para(
    "The main results can be stated early. The cumulative pass-through to headline WPI for positive shocks, denoted CPT+, is about 0.030 and statistically significant. The cumulative pass-through to WPI Fuel and Power is about 0.287; to PPAC retail petrol it is about 0.346; to the CPI Fuel and Light bridge series it is about 0.178; and to headline CPI it is about 0.021 with a p-value of 0.122. The ordering is clear: the shock is strong in retail fuel and fuel-sensitive layers, statistically visible but small in headline WPI, and weak or statistically indistinguishable from zero in headline CPI. Across all layers, the evidence for short-run asymmetry is weak; where it appears, in the retail petrol layer, it is only marginal at the 10 percent level."
)

section_heading("1.4 Why the Question Matters for Policy")
add_para(
    "The layered framing speaks to two policy debates. The first is whether headline CPI is the appropriate anchor for monetary policy in an economy with large external cost shocks: if oil shocks barely move headline CPI, the framework looks unresponsive even when upstream prices are rising sharply. The dissertation cannot settle this debate, but it can locate the empirical fact that oil shocks reach headline CPI only weakly, with most of the shock absorbed before that point. The second debate concerns administered fuel prices and tax adjustments. The pre/post-2010 split provides indirect evidence because the post-2010 sample reflects more frequent retail revisions, and the post-2010 cumulative pass-through coefficients are accordingly larger."
)

section_heading("1.5 Contribution and Structure")
add_para(
    "The contribution of this dissertation is therefore modest and architectural. It is not the introduction of a new estimator and it is not a claim of being the first study of oil-price pass-through in India. The paper contributes by treating oil-price pass-through in India as a layered transmission problem, showing that oil shocks are strong in retail fuel and fuel-sensitive prices but much weaker in headline consumer inflation. The pre/post-2010 wholesale split is reported as institutional evidence consistent with more market-linked fuel pricing rather than as a clean causal estimate of deregulation."
)
add_para(
    "The rest of the dissertation is organised as follows. Chapter 2 places the empirical design inside India's oil-pricing institutions and the existing literature. Chapter 3 describes the data, the chained series, and the variable transformations. Chapter 4 develops the ADL specification, the inference strategy, and the supporting diagnostic tests. Chapter 5 presents the layered results in order: long-horizon headline WPI, WPI Fuel and Power, PPAC retail petrol, the CPI Fuel and Light bridge, headline CPI, the integrated attenuation map, and the pre/post-2010 wholesale split. Chapter 6 reports robustness checks, diagnostics, and the limitations of the design. The conclusion returns to the research question and answers it directly."
)
page_break()

# ============================================================
# CHAPTER 2
# ============================================================
chapter_heading("Chapter 2", "Institutional Background and Literature")

section_heading("2.1 India's Oil Pricing and Inflation Context")
add_para(
    "The transmission chain examined in this dissertation can be written compactly. The Brent crude price, expressed in US dollars per barrel, combines with the INR/USD exchange rate to yield a rupee oil price; the rupee oil price feeds into domestic retail fuel prices through refining and marketing margins together with central and state taxes; retail fuel prices and bulk fuel costs enter the fuel-sensitive sub-indices of the wholesale and consumer price indices; and these sub-indices, together with food and services prices, aggregate into headline WPI and CPI. Each link in the chain is mediated by institutional rules that influence how much of the shock is allowed through and how quickly."
)
add_para(
    "India imports the majority of its crude oil requirement; therefore, global oil prices enter the domestic economy as an external cost shock rather than as a domestic supply variable. Because crude is priced internationally in US dollars, the exchange rate is mechanically part of the domestic shock: a rise in Brent and a depreciation of the rupee can amplify each other, while a strong rupee can blunt a Brent rise. This dissertation therefore uses the rupee oil price as the main shock variable in the headline ADL specifications and reports a Brent-and-exchange-rate decomposition as a robustness check."
)
add_para(
    "Retail fuel pricing in India has moved over time from administered pricing toward more market-linked pricing. Petrol prices were deregulated in June 2010 and diesel prices were deregulated in October 2014. Under administered pricing, the government set retail prices for long stretches and absorbed part of the shock through under-recoveries to oil marketing companies and through subsidy adjustments; under market-linked pricing, oil marketing companies revise retail prices much more frequently, which raises the empirical pass-through that an econometric model can detect. The dissertation reports a pre/post-2010 split for the wholesale models to capture this institutional shift, while remaining careful not to interpret the post-2010 increase as a clean causal estimate of deregulation."
)
add_para(
    "WPI and CPI answer different empirical questions. The wholesale price index is closer to upstream and producer-side price pressure, with a relatively heavy weight on manufactured products, primary articles, and a fuel and power group that includes mineral oils, electricity, and coal. The consumer price index is closer to household-facing inflation and is the index targeted by the monetary policy framework introduced in 2016. Because food and non-fuel services dominate household consumption weights, the direct weight of fuel in the CPI basket is limited, and CPI dilution is therefore not surprising as a structural feature rather than as a model artefact. This dissertation does not rebuild the basket-weight calculation; it uses the institutional weight evidence as supporting context for the dilution story it documents econometrically."
)

section_heading("2.2 What Existing Studies Already Show")
add_para(
    "The literature most directly relevant to this dissertation can be summarised in a few studies. Mandal, Bhattacharyya, and Bhoi (2012) show that oil-price pass-through in India became more relevant once domestic price adjustment grew more frequent, which anticipates the institutional point that the empirical pass-through is partly a function of the pricing regime rather than only a function of refining and tax structure. Bhanumurthy, Das, and Bose (2012) embed oil shocks in a broader macroeconomic framework that combines pass-through policy, inflation, fiscal costs, and growth trade-offs, and provide useful context for why the political economy of pass-through is complicated even when the engineering of pass-through is straightforward."
)
add_para(
    "Pal and Mitra (2016) provide evidence of asymmetric oil-product pricing in India using a multiple-threshold nonlinear ARDL approach, and motivate the asymmetric specification used in this dissertation, where positive and negative oil shocks are entered as separate cumulative effects. Pradeep (2022) studies the impact of diesel price reform on the asymmetricity of oil-price pass-through to disaggregated wholesale prices, retail diesel, and aggregate consumer prices, and is the closest in spirit to the layered design adopted here, although the present dissertation extends the layered map to include retail petrol, the WPI Fuel and Power group, the CPI Fuel and Light bridge series, and headline CPI within a single empirical frame."
)
add_para(
    "On the methodological side, Newey and West (1987) provide the HAC covariance estimator used for inference in the ADL models. Bai and Perron (2003) provide the multiple-break test used in the structural-break diagnostics. The asymmetric split between positive and negative oil changes follows the applied pass-through literature and is used here as a transparent way to test whether cumulative positive and negative responses differ. These references are used because each one performs concrete work in the empirical design rather than as decoration."
)

section_heading("2.3 Gap and Hypotheses")
add_para(
    "The gap addressed here is architectural. Existing Indian studies often answer one of the following questions in isolation: does oil affect WPI, does oil affect CPI, do retail fuel prices adjust asymmetrically, and did deregulation alter pass-through. Each of these is a useful question, but together they leave the reader without a single map of where the shock survives and where it fades. This dissertation asks a different question: where does the shock weaken as it moves through the price system? The four-layer design is the answer."
)
add_para(
    "The empirical hypotheses can be stated as follows. H1: oil shocks pass through significantly to headline WPI, but the magnitude is small. H2: pass-through is stronger in retail fuel and fuel-sensitive price layers than in headline indices. H3: headline CPI shows attenuation relative to upstream and fuel-sensitive layers. H4: post-2010 wholesale pass-through is larger than pre-2010 pass-through, consistent with more market-linked fuel pricing. H5: short-run asymmetry is not the central finding, and where it appears most clearly it is at the retail petrol layer and only marginally so."
)
page_break()

# ============================================================
# CHAPTER 3
# ============================================================
chapter_heading("Chapter 3", "Data and Variables")

section_heading("3.1 Data Sources")
add_para(
    "The data used in this dissertation are monthly series drawn from official Indian statistical agencies and standard international macroeconomic databases. The wholesale price evidence is built from the Office of the Economic Adviser (OEA) Wholesale Price Index series, with the headline aggregate and the Fuel and Power group chained across successive base years to a common 2011-12 base. The retail fuel evidence is taken from the Petroleum Planning and Analysis Cell (PPAC) ready reckoner, which publishes monthly retail prices of petrol and diesel for the major Indian metropolitan markets. The international Brent crude price is obtained from the World Bank Pink Sheet (series POILBREUSDM, accessed through the FRED database). The INR/USD exchange rate is obtained from FRED (series EXINUS). The all-India consumer price index is taken from the Ministry of Statistics and Programme Implementation (MoSPI) and is cross-checked against the FRED INDCPIALLMINMEI series; the harmonised CPI Fuel and Light component is taken from MoSPI for the post-2011 period."
)
add_para(
    "All series are merged at monthly frequency on common dates, with active samples reported in Section 3.5 after inner joins. The wholesale series carry a non-trivial chaining step that is documented separately in Section 3.3. The CPI Fuel and Light component is treated as a bridge series rather than as a direct headline mandate because the harmonised post-2011 series limits its sample to 164 months."
)

section_heading("3.2 Main Variables and Transformations")
add_para(
    "The main variables can be defined briefly. Brent crude is the international benchmark price in US dollars per barrel. The INR/USD exchange rate is the monthly average rupee-per-dollar series. The rupee oil price is constructed as Brent multiplied by the INR/USD exchange rate; it is the main shock variable in the headline ADL specifications. Headline WPI is chained to the 2011-12 base using official linking factors, as is the WPI Fuel and Power group. PPAC Delhi retail petrol price is the monthly average pump price reported by the Petroleum Planning and Analysis Cell. Headline CPI is the all-India general index. CPI Fuel and Light is used as a bridge series only, because the harmonised post-2011 series limits the available sample to about 164 months. The Index of Industrial Production and the activity controls already used in the CPI and retail-fuel specifications are retained as controls in the relevant models."
)
add_para_math(
    "All main model variables are transformed into month-on-month log differences. Writing the rupee oil price as x_t and a generic dependent price index as y_t, the log-difference transformation is defined in equation (3.1)."
)

# Eq 3.1: Δy_t = ln(y_t) - ln(y_{t-1})
eq_3_1 = (
    mr('Δ') + msub(mr('y'), mr('t')) + mr(' = ln') +
    mfenced(msub(mr('y'), mr('t'))) + mr(' − ln') +
    mfenced(msub(mr('y'), mr('t−1')))
)
add_equation(eq_3_1, label="(3.1)")

add_para(
    "The differences are interpreted as approximate percentage changes. Reporting is consistent throughout the dissertation: cumulative pass-through coefficients should be read as the cumulative response of the dependent log difference to a one-unit log-difference shock in rupee oil prices, summed over the lag window. The same convention is used for the Brent and exchange-rate decomposition."
)

section_heading("3.3 Splice and Chaining of the WPI Series")
add_para(
    "The wholesale series carry a non-trivial construction step. The Office of the Economic Adviser publishes WPI under successive base years, with the most recent base being 2011-12 = 100. Earlier vintages used 1981-82, 1993-94, and 2004-05 as base years. To assemble a continuous monthly headline WPI series and a continuous Fuel and Power group from May 1983 to March 2026, the dissertation chains the published vintages using their official linking factors, with overlap-period checks to verify that the splice does not introduce visible level breaks. The chain-factor table and the splice-check table reported in the wpi outputs document each linking step. The chained series is then rebased to 2011-12 = 100 so that all wholesale comparisons in the empirical work share a common base."
)
add_para(
    "Two practical points follow from this construction. First, the chained WPI series is the most extensive, methodologically consistent series available for the headline WPI exercise, and its long sample is what makes the pre/post-2010 split feasible at all. Second, the splice has been verified at the level of the headline aggregate; component-level chaining for the Fuel and Power group has been carried out separately, since the OEA component definitions changed across base years. Where the component definitions are not exactly comparable across vintages, the dissertation prefers the longest internally consistent stretch over a shorter, perfectly homogeneous stretch."
)

section_heading("3.4 Descriptive Patterns")
add_para(
    "Two features of the data are worth noting before the formal estimation. The first is the asymmetric distribution of the rupee oil log difference. The series exhibits visible negative tails during the 2008 commodity correction, the 2014-15 oil price collapse, and the early-2020 COVID-19 demand shock, alongside positive tails during the 2007-08 commodity peak, the 2011-12 Brent surge, and the 2022 European energy episode. These tails motivate the asymmetric specification used in the ADL models. The second feature is the visible co-movement between rupee oil price changes and WPI Fuel and Power log differences across the entire sample, which is much weaker for headline CPI log differences. The naked-eye co-movement is consistent with the layered attenuation result reported in Chapter 5."
)

section_heading("3.5 Data Table and Model Specifications")
add_table(
    headers=["Series", "Source", "Transformation", "Active sample"],
    rows=[
        ["Brent crude (USD/bbl)", "World Bank Pink Sheet via FRED (POILBREUSDM)", "Δln, monthly", "1983-05 to 2026-03"],
        ["INR/USD exchange rate", "FRED EXINUS", "Δln, monthly", "1983-05 to 2026-03"],
        ["Rupee oil price", "Brent × INR/USD (constructed)", "Δln, monthly", "1983-05 to 2026-03"],
        ["Headline WPI (chained)", "OEA, MoCI; chained to 2011-12 = 100", "Δln, monthly", "1983-05 to 2026-03"],
        ["WPI Fuel and Power (chained)", "OEA, MoCI; chained to 2011-12 = 100", "Δln, monthly", "1995-05 to 2026-03"],
        ["PPAC Delhi retail petrol", "PPAC ready reckoner (pre/post-2017 files)", "Δln, monthly", "2004-08 to 2024-12"],
        ["Headline CPI (all-India)", "MoSPI / FRED INDCPIALLMINMEI", "Δln, monthly", "2004-08 to 2024-12"],
        ["CPI Fuel and Light (bridge)", "MoSPI harmonised series", "Δln, monthly", "2011-05 to 2024-12"],
        ["IIP / activity control", "MoSPI", "Δln, monthly", "matched to layer"],
    ],
    caption="Table 3.1: Series, sources, transformations, and sample spans",
    col_widths=[1.55, 1.95, 1.05, 1.25],
    font_size=9,
)
add_note(
    "Wholesale series are chained to a common 2011-12 = 100 base using official linking factors. Active samples are reported after inner joins on common dates. CPI Fuel and Light is treated as supporting bridge evidence because the harmonised series begins in 2011."
)

add_table(
    headers=["Layer", "Dependent (Δln)", "Shock variable (Δln)", "Own lags", "Shock lags"],
    rows=[
        ["Headline WPI", "Headline WPI", "Rupee oil price", "12", "0–6"],
        ["WPI Fuel and Power", "WPI Fuel & Power", "Rupee oil price", "12", "0–6"],
        ["PPAC retail petrol", "Delhi retail petrol", "Brent crude (USD)", "6", "0–4"],
        ["CPI Fuel and Light (bridge)", "CPI Fuel & Light", "PPAC retail petrol", "6", "0–4"],
        ["Headline CPI", "Headline CPI", "Rupee oil price", "6", "0–4"],
    ],
    caption="Table 3.2: Model specifications across the four-layer chain",
    col_widths=[1.65, 1.35, 1.35, 0.65, 0.80],
    font_size=9,
)
add_note(
    "Each layer is estimated as a separate asymmetric ADL specification. The shock variable differs by layer: rupee oil price for the WPI and headline CPI specifications, Brent crude for the retail petrol mechanism, and PPAC retail petrol for the CPI Fuel and Light bridge. Calendar-month fixed effects, an activity control, and (where applicable) the exchange-rate component are included as controls."
)

add_figure(
    os.path.join(ROOT, "models", "wpi", "outputs", "figures", "fig_01_wpi_chained_series.png"),
    "Figure 3.1: Chained headline WPI and Fuel and Power series, rebased to 2011-12 = 100.",
)
add_figure(
    os.path.join(ROOT, "models", "wpi", "outputs", "figures", "fig_03_oil_decomposition.png"),
    "Figure 3.2: Decomposition of the rupee oil price into Brent and INR/USD contributions.",
)
page_break()

# ============================================================
# CHAPTER 4: METHODOLOGY
# ============================================================
chapter_heading("Chapter 4", "Empirical Methodology")

section_heading("4.1 Main ADL Specification")
add_para(
    "The main empirical strategy is a short-run asymmetric autoregressive distributed lag model in log differences. The asymmetry is introduced by splitting the rupee oil log difference into positive and negative components. Writing the rupee oil log difference as in equation (4.1),"
)

# Eq 4.1: Δx_t = ln(x_t) - ln(x_{t-1})
eq_4_1 = (
    mr('Δ') + msub(mr('x'), mr('t')) + mr(' = ln') +
    mfenced(msub(mr('x'), mr('t'))) + mr(' − ln') +
    mfenced(msub(mr('x'), mr('t−1')))
)
add_equation(eq_4_1, label="(4.1)")

add_para(
    "the positive and negative components are defined in equation (4.2)."
)

# Eq 4.2: Δx_t^+ = max(Δx_t, 0),   Δx_t^- = min(Δx_t, 0)
delta_x_t = mr('Δ') + msub(mr('x'), mr('t'))
delta_x_t_plus = msup(mr('Δ') + msub(mr('x'), mr('t')), mr('+'))
delta_x_t_minus = msup(mr('Δ') + msub(mr('x'), mr('t')), mr('−'))
eq_4_2 = (
    delta_x_t_plus + mr(' = max') + mfenced(delta_x_t + mr(', 0')) +
    mr(',     ') +
    delta_x_t_minus + mr(' = min') + mfenced(delta_x_t + mr(', 0'))
)
add_equation(eq_4_2, label="(4.2)")

add_para(
    "By construction the two components sum back to the original log difference, which preserves the standard interpretation of the underlying shock. The general estimating equation has the form given in equation (4.3)."
)

# Eq 4.3: ADL model
sum_phi = mnary_sum(
    mr('i=1'), mr('p'),
    msub(mr('φ'), mr('i')) + mr(' Δ') + msub(mr('y'), mr('t−i'))
)
sum_beta_plus = mnary_sum(
    mr('j=0'), mr('q'),
    msup(msub(mr('β'), mr('j')), mr('+')) + mr(' ') + msup(msub(mr('Δx'), mr('t−j')), mr('+'))
)
sum_beta_minus = mnary_sum(
    mr('j=0'), mr('q'),
    msup(msub(mr('β'), mr('j')), mr('−')) + mr(' ') + msup(msub(mr('Δx'), mr('t−j')), mr('−'))
)
eq_4_3 = (
    mr('Δ') + msub(mr('y'), mr('t')) + mr(' = α + ') + sum_phi +
    mr(' + ') + sum_beta_plus + mr(' + ') + sum_beta_minus +
    mr(' + ') + msup(msub(mr('Z'), mr('t')), mr('′')) + mr(' γ + ') +
    msub(mr('μ'), mr('m')) + mr(' + ') + msub(mr('ε'), mr('t'))
)
add_equation(eq_4_3, label="(4.3)")

add_para_math(
    "In equation (4.3), Δy_t is the dependent log difference, the φ_i are own-lag coefficients with own-lag order p, the β_j^+ and β_j^{−} are the asymmetric distributed-lag coefficients on the positive and negative oil components with distributed-lag order q, Z_t is a vector of controls (including, where applicable, the exchange-rate component, an activity control, and lagged inflation), μ_m are calendar-month fixed effects, and ε_t is the residual. For the headline WPI specifications, the model uses twelve own lags and oil lags from zero to six. The same lag structure is retained for WPI Fuel and Power. For the PPAC retail petrol and headline CPI specifications, the lag structure follows the channel-mechanism model-gate specifications and is not re-tuned ex post. The CPI Fuel and Light bridge inherits the same structure as the headline CPI specifications because of its shorter sample."
)

add_para(
    "Cumulative pass-through coefficients are then constructed by summing the lag coefficients on the relevant component, as in equation (4.4)."
)

# Eq 4.4: CPT+ = Σ β_j^+,  CPT- = Σ β_j^-
sum_cpt_plus = mnary_sum(mr('j=0'), mr('q'), msup(msub(mr('β'), mr('j')), mr('+')))
sum_cpt_minus = mnary_sum(mr('j=0'), mr('q'), msup(msub(mr('β'), mr('j')), mr('−')))
eq_4_4 = (
    msup(mr('CPT'), mr('+')) + mr(' = ') + sum_cpt_plus +
    mr(',     ') +
    msup(mr('CPT'), mr('−')) + mr(' = ') + sum_cpt_minus
)
add_equation(eq_4_4, label="(4.4)")

add_para(
    "Plain interpretation is straightforward. A CPT+ of 0.030 means that a one percent positive rupee-oil shock is associated with about a 0.03 percent cumulative increase in the dependent price index over the model's lag window, holding the model's controls fixed; a CPT+ of 0.287 means that a one percent positive shock is associated with about a 0.287 percent cumulative increase, and so on for the other layers."
)

section_heading("4.2 Inference")
add_para(
    "Inference uses Newey-West heteroscedasticity-and-autocorrelation-consistent standard errors for both individual coefficient tests and the cumulative restriction tests. The HAC covariance estimator is the standard one of Newey and West (1987) with a Bartlett kernel and a data-dependent bandwidth. Three formal tests are reported for each layer: whether CPT+ differs from zero, whether CPT- differs from zero, and whether CPT+ equals CPT-. The first two tests are the standard cumulative pass-through tests; the third is a Wald symmetry test of the joint linear restriction in equation (4.5)."
)

# Eq 4.5: H_0: CPT+ = CPT-
eq_4_5 = (
    msub(mr('H'), mr('0')) + mr(': ') +
    msup(mr('CPT'), mr('+')) + mr(' = ') + msup(mr('CPT'), mr('−'))
)
add_equation(eq_4_5, label="(4.5)")

add_para(
    "Symmetry is also assessed using a restricted-residual circular block bootstrap with 4,999 replications. The bootstrap p-values reported in the results chapter for the headline WPI, WPI Fuel and Power, and headline CPI models are 0.746, 0.820, and 0.500 respectively, none of which support a rejection of the null of symmetric short-run pass-through. The bootstrap is restricted-residual to preserve the imposed null structure under resampling, and the circular block is used to retain the within-block autocorrelation of the residual process. Where the asymptotic and the bootstrap p-values disagree by a non-trivial margin, the bootstrap is treated as the more conservative reading."
)

section_heading("4.3 Stationarity and Lag Selection")
add_para(
    "Because the main specifications operate on log differences rather than on levels, the integration order of the underlying series is less binding than it would be for a levels regression. Nevertheless, the unit root battery is reported for completeness. The augmented Dickey-Fuller, Phillips-Perron, and KPSS tests of Kwiatkowski, Phillips, Schmidt, and Shin (1992) are reported for each series in levels and in first differences. The combined evidence supports treating the rupee oil price, headline WPI, WPI Fuel and Power, PPAC retail petrol, and headline CPI as integrated of order one in levels and stationary in first differences, which is the standard requirement for the differenced ADL specification. The Zivot-Andrews test is reported for the same series with an endogenous break, and the implied break dates cluster around the well-known regime episodes referenced in Chapter 2."
)
add_para(
    "Lag selection in the main specifications follows the model-gate and lag-selection tables produced for each layer. The own-lag order is set to twelve for the long WPI specifications to capture annual seasonality even after month fixed effects are imposed; the distributed-lag order on the oil components is set to six for the wholesale specifications and is inherited from the channel-mechanism model-gate specifications for the retail petrol, CPI Fuel and Light, and headline CPI layers. Information criteria (AIC, BIC, and HQIC) and a sequence of nested Wald tests on the longest insignificant lag confirm that these choices are not extreme; results are stable when the distributed-lag order is varied between four and eight."
)

section_heading("4.4 Supporting Tests")
add_para(
    "Two additional tools are used in support of interpretation rather than as identification claims. Granger-causality tests are reported for oil to WPI and oil to Fuel and Power. They support a directional reading of the chain but do not establish structural causality. Bai-Perron structural break tests are used to verify that the empirical samples are not dominated by a single regime change in the relationship between rupee oil prices and the dependent series; where breaks are detected, the pre/post-2010 wholesale split addresses them in the most institutionally relevant way."
)
page_break()

# ============================================================
# CHAPTER 5: RESULTS
# ============================================================
chapter_heading("Chapter 5", "Results")

section_heading("5.1 Long-Horizon Headline WPI Results")
add_para(
    "The long-horizon headline WPI specification estimates the asymmetric ADL on the chained WPI series from May 1983 to March 2026, a sample of N = 515 months covering 42.92 years. The model achieves an adjusted R² of 0.421. The cumulative pass-through estimates are CPT+ = 0.030 with p = 0.024, and CPT− = 0.037 with p = 0.001. Both cumulative effects are statistically distinguishable from zero at conventional levels. The asymmetry test gives p = 0.673 under HAC inference and p = 0.746 in the restricted-residual circular block bootstrap, so the headline WPI specification does not support short-run asymmetry."
)
add_para(
    "The interpretation is restrained. Headline WPI responds significantly to rupee oil shocks, but the magnitude is small. A one percent positive rupee-oil shock is associated with about a 0.03 percent cumulative response in headline WPI over the lag window, which is statistically visible but quantitatively modest given that fuel and power, mineral oils, and oil-intensive manufactured products together account for a substantial share of the WPI basket. The Brent and exchange-rate decomposition, reported in the headline robustness model, gives a similar conclusion with CPT+ = 0.031 and CPT− = 0.037, which is consistent with the rupee-oil specification and indicates that the headline WPI conclusion is not an artefact of how the shock variable is constructed."
)

add_figure(
    os.path.join(ROOT, "models", "wpi", "outputs", "figures", "fig_04_cumulative_passthrough.png"),
    "Figure 5.1: Cumulative pass-through profile for headline WPI from the asymmetric ADL specification.",
)

section_heading("5.2 WPI Fuel and Power")
add_para(
    "The WPI Fuel and Power specification is estimated on the chained Fuel and Power series from May 1995 to March 2026, a sample of N = 371 months covering 30.92 years. The model achieves an adjusted R² of 0.463. The cumulative pass-through estimates are CPT+ = 0.287 with p < 0.001 and CPT− = 0.268 with p < 0.001. Both cumulative effects are large and highly significant. The asymmetry test gives p = 0.783 under HAC inference and p = 0.820 in the bootstrap, so the Fuel and Power specification also does not support short-run asymmetry."
)
add_para(
    "The fuel-sensitive wholesale layer therefore carries a much larger oil signal than headline WPI. This is expected because the dependent variable is closer to the fuel channel: the Fuel and Power group covers mineral oils, electricity, and coal, all of which are mechanically tied to the rupee oil price either directly or through cross-fuel substitution. The reported coefficient should be read with one caveat. The model fails the HAC RESET functional-form test, which suggests that the linear specification does not fully capture the curvature of the relationship, especially during episodes when administered prices and market-linked prices coexisted within the sample. The exact magnitude of CPT+ should therefore be reported with a functional-form caveat, although the sign and the order of magnitude are stable across specifications, lag windows, and sample trims."
)

section_heading("5.3 Retail Petrol Mechanism")
add_para(
    "The PPAC retail petrol mechanism specification is estimated on the Delhi retail petrol price series from August 2004 to December 2024, a sample of N = 245 months covering 20.42 years. The cumulative pass-through estimates are CPT+ = 0.346 with p < 0.001 and CPT− = 0.191 with p = 0.0002. The asymmetry test gives p = 0.0999, just outside the 5 percent threshold and inside the 10 percent threshold. The diagnostic battery in the channel-diagnostics table is accepted for main-text reporting under the mandatory model gate."
)
add_para(
    "The retail petrol layer therefore shows the largest direct pass-through in the chain. A one percent positive rupee-oil shock is associated with about a 0.346 percent cumulative response in Delhi retail petrol over the model's lag window, which is consistent with a market-linked pricing regime in which oil marketing companies revise pump prices frequently. The asymmetry is only marginal; therefore, the dissertation discusses it as suggestive rockets-and-feathers behaviour, in which positive shocks are passed through faster or more fully than negative shocks, but does not claim a strong 5 percent result. The retail petrol layer is the layer where asymmetry, if it exists at all in the chain, is most plausibly located, and its location at this point in the chain rather than at the headline aggregates is itself an empirical regularity worth noting."
)

section_heading("5.4 CPI Fuel and Light Bridge")
add_para(
    "The CPI Fuel and Light bridge specification is estimated from May 2011 to December 2024, a sample of N = 164 months covering 13.67 years. The shorter sample is dictated by the harmonised post-2011 CPI series. The cumulative pass-through estimates are CPT+ = 0.178 with p = 0.0021 and CPT− = 0.106 with p = 0.174. The asymmetry test gives p = 0.455. The positive-shock cumulative coefficient is strongly significant; the negative-shock coefficient is not."
)
add_para(
    "The CPI Fuel and Light layer therefore confirms that retail fuel movements enter the fuel-sensitive consumer price layer at a magnitude smaller than the retail petrol layer but larger than the headline CPI endpoint. Because the harmonised series begins in 2011, this evidence is treated as a bridge between PPAC retail petrol and headline CPI rather than as a headline mandate in its own right. The PPAC-to-fuel bridge specification supports this interpretation: retail petrol movements are associated with subsequent CPI Fuel and Light movements in the bridge equation and explain a non-trivial share of their variation, although the bridge Granger test for retail petrol to CPI Fuel and Light does not reject the null at conventional levels (p = 0.113), so the relationship should be read as an estimated bridge response rather than as a strict predictive precedence."
)

section_heading("5.5 Headline CPI Endpoint")
add_para(
    "The headline CPI specification is estimated from August 2004 to December 2024, a sample of N = 245 months covering 20.42 years, with an adjusted R² of 0.449. The cumulative pass-through estimates are CPT+ = 0.021 with p = 0.122 and CPT− = 0.001 with p = 0.938. The asymmetry test gives p = 0.241 under HAC inference and p = 0.500 in the restricted-residual circular block bootstrap. None of the cumulative effects are statistically distinguishable from zero at conventional levels."
)
add_para(
    "Headline CPI is therefore the endpoint where the oil signal becomes weak. The positive coefficient has the expected sign and is of a small but non-zero magnitude, which is consistent with the dilution mechanism predicted by the limited direct fuel weight in the consumer basket and the dominance of food and non-fuel services in household consumption. The dissertation does not claim a strong headline CPI effect. The result is reported as suggestive of limited positive pass-through; the formal reading is that the cumulative pass-through is not statistically distinguishable from zero in the post-2004 sample. This is the most policy-relevant of the layered findings, because headline CPI is the index that anchors the inflation-targeting framework in India."
)

section_heading("5.6 Integrated Attenuation Result")
add_para(
    "Bringing the layers together produces the central synthesis of this dissertation. Ordering the layers by the magnitude of CPT+, the empirical map is as follows: PPAC retail petrol at 0.346, WPI Fuel and Power at 0.287, the CPI Fuel and Light bridge at 0.178, headline WPI at 0.030, and headline CPI at 0.021 (not significant). The ordering is monotonic in the institutional distance of each layer from the rupee oil price, and the drop between the fuel-sensitive layers and the headline aggregates is more than an order of magnitude."
)

add_table(
    headers=["Layer", "N", "CPT+ (p)", "CPT− (p)", "Asym. p"],
    rows=[
        ["PPAC retail petrol", "245", "0.346 (<0.001)", "0.191 (0.0002)", "0.0999"],
        ["WPI Fuel and Power", "371", "0.287 (<0.001)", "0.268 (<0.001)", "0.783"],
        ["CPI Fuel and Light (bridge)", "164", "0.178 (0.0021)", "0.106 (0.174)", "0.455"],
        ["Headline WPI", "515", "0.030 (0.024)", "0.037 (0.001)", "0.673"],
        ["Headline CPI", "245", "0.021 (0.122)", "0.001 (0.938)", "0.241"],
    ],
    caption="Table 5.1: Layer-specific cumulative responses across the four-layer chain",
    col_widths=[1.95, 0.55, 1.20, 1.20, 0.90],
    font_size=9,
)
add_note(
    "Cumulative coefficients are layer-specific responses from the asymmetric ADL specification in log differences with Newey-West HAC inference; they should not be read as one identical structural elasticity, since the shock variable in the PPAC retail petrol equation is Brent, the shock in the headline WPI, WPI Fuel and Power, and headline CPI equations is the rupee oil price, and the explanatory variable in the CPI Fuel and Light bridge equation is the PPAC retail petrol price. The asymmetry p-value is from a Wald test of CPT+ = CPT−. Active samples: 1983-05 to 2026-03 (headline WPI), 1995-05 to 2026-03 (Fuel and Power), 2004-08 to 2024-12 (PPAC and headline CPI), 2011-05 to 2024-12 (CPI Fuel and Light bridge)."
)

add_para(
    "Two readings of Table 5.1 should be kept separate. The cumulative coefficients in the table are layer-specific responses, each estimated from its own asymmetric ADL specification with its own dependent variable, its own shock variable, and its own sample. They are not five comparable estimates of the same identical shock passing through five layers in sequence: the PPAC retail petrol equation uses Brent as the shock; the headline WPI, WPI Fuel and Power, and headline CPI equations use the rupee oil price; the CPI Fuel and Light bridge equation uses the PPAC retail petrol price as its shock variable. The table is therefore best read as a descriptive attenuation map across naturally ordered points in the price chain, not as a structural decomposition of one elasticity. With that qualification, the empirical pattern is unambiguous."
)
add_para(
    "The empirical story is therefore not that oil shocks disappear inside the Indian price system. They are strong in the fuel channel, where retail petrol and WPI Fuel and Power respond at a magnitude close to a third of the shock; they are visible in the fuel-sensitive consumer layer through the CPI Fuel and Light bridge; and they are weak in the headline aggregates, where the headline WPI carries a small but significant signal and the headline CPI carries only a weak and statistically uncertain one. This is the layered attenuation result and the central contribution of the dissertation."
)

add_figure(
    os.path.join(ROOT, "models", "cpi", "outputs", "figures", "fig_13_dilution_chain.png"),
    "Figure 5.2: Dilution chain showing cumulative pass-through across retail petrol, WPI Fuel and Power, CPI Fuel and Light, headline WPI, and headline CPI.",
)

section_heading("5.7 Reading the Attenuation Quantitatively")
add_para(
    "Table 5.1 also lends itself to a simple quantitative reading of attenuation. Taking the PPAC retail petrol layer as the reference, WPI Fuel and Power is about 83 percent of the retail petrol coefficient, the CPI Fuel and Light bridge about 51 percent, headline WPI about 9 percent, and headline CPI about 6 percent. These ratios are not structural attenuation parameters and they are sensitive to the choice of reference layer. They are useful only as a way of communicating the order-of-magnitude difference between the fuel-sensitive layers and the headline aggregates. The drop is not a smooth gradient; it is concentrated at the transition from the fuel-sensitive layers to the headline aggregates, which is exactly the point at which the basket-weight dilution and the tax-and-margin absorption are expected to operate."
)

section_heading("5.8 Pre/Post-2010 Wholesale Split")
add_para(
    "The pre/post-2010 wholesale split splits the long WPI samples at the petrol deregulation boundary of June 2010. For headline WPI, the pre-2010 cumulative pass-through is CPT+ = 0.012 with p = 0.381, while the post-2010 cumulative pass-through is CPT+ = 0.074 with p = 0.004. For WPI Fuel and Power, the pre-2010 cumulative pass-through is CPT+ = 0.092 with p = 0.168, while the post-2010 cumulative pass-through is CPT+ = 0.524 with p < 0.001."
)
add_para(
    "The post-2010 estimates are materially larger and statistically stronger than the pre-2010 estimates in both layers. This is consistent with the institutional move toward more market-linked fuel pricing, under which oil marketing companies revise retail prices much more frequently and pass on more of a given shock within the model's lag window. The dissertation does not claim this as a clean causal estimate of deregulation. Other changes occurred in the post-2010 period as well, including the adoption of the new CPI series in 2011, the move to flexible inflation targeting in 2016, the introduction of the Goods and Services Tax in 2017, and a sequence of episodes affecting fuel taxes and excise rates. The split should therefore be read as institutional evidence consistent with a stronger pass-through regime, not as a deregulation experiment."
)

add_figure(
    os.path.join(ROOT, "models", "wpi", "outputs", "figures", "fig_05_subsample_comparison.png"),
    "Figure 5.3: Pre/post-2010 cumulative pass-through for headline WPI and WPI Fuel and Power.",
)
page_break()

# ============================================================
# CHAPTER 6: ROBUSTNESS
# ============================================================
chapter_heading("Chapter 6", "Robustness, Diagnostics, and Limitations")

section_heading("6.1 Robustness Battery")
add_para(
    "The robustness battery for this dissertation is designed to test whether the layered attenuation result depends on a particular shock construction, on a particular sample, or on the asymptotic inference. The first robustness check decomposes the rupee oil price into its Brent and exchange-rate components and re-estimates the headline WPI specification. The decomposition gives CPT+ = 0.031 and CPT− = 0.037 with an asymmetry p-value of 0.704, which is essentially indistinguishable from the rupee-oil specification and confirms that the headline WPI conclusion does not depend on the way the shock variable is built."
)
add_para(
    "The second robustness check uses the restricted-residual circular block bootstrap with 4,999 replications to assess short-run asymmetry. The bootstrap p-values are 0.746 for headline WPI, 0.820 for WPI Fuel and Power, and 0.500 for headline CPI. None of these support a rejection of the null of symmetric short-run pass-through. The bootstrap and the HAC asymptotic tests therefore agree: short-run asymmetry is not the central finding of the dissertation, and where the retail petrol layer hints at it the evidence is only marginal."
)
add_para(
    "The third robustness check uses Granger-causality tests in the predictive sense. The tests support directional precedence from the rupee oil price to headline WPI and to WPI Fuel and Power. This is consistent with the layered design but is not a structural causality claim. The fourth robustness check uses Bai-Perron structural break tests to check that the layered relationships are not dominated by a single regime change. Where breaks are detected, the relevant institutional split — most importantly, the pre/post-2010 wholesale split — is reported separately."
)
add_para(
    "The fifth robustness check addresses the COVID-19 window and outlier sensitivity. Excluding the COVID window from the headline CPI specification and winsorising the dependent log differences at the one-percent and ninety-nine-percent tails do not overturn the main CPI conclusion. The positive cumulative pass-through remains small and not statistically significant at conventional levels. The results are therefore not driven by extreme observations."
)
add_para(
    "Lag-sensitivity and rolling-window checks add a final layer of reassurance. Re-estimating the headline WPI and headline CPI specifications under alternative lag windows (oil lags from zero to four and from zero to eight, own lags of six and eighteen) does not change the qualitative ordering of Table 5.1, and rolling-window estimates of the headline CPI cumulative pass-through hover around the central estimate without crossing into a significant range at conventional levels."
)

section_heading("6.2 Diagnostics Across Layers")
add_para(
    "The diagnostic battery for each layer reports the Breusch-Godfrey serial correlation test, the ARCH-LM test for conditional heteroscedasticity, the Jarque-Bera test for residual normality, the Ramsey RESET test for functional-form misspecification under the HAC covariance, and a CUSUM stability check. The headline WPI and headline CPI specifications pass these diagnostics at conventional levels except for mild residual autocorrelation at short lags, which is exactly the case for which the Newey-West HAC covariance estimator is designed. The retail petrol specification passes the channel-diagnostics gate and is accepted for main-text reporting. The WPI Fuel and Power specification fails the HAC RESET test, as already noted, and the magnitude of CPT+ for that layer is therefore reported with a functional-form caveat. The CUSUM plots show no evidence of a single dominant break in any of the layered specifications, which is consistent with the institutionally motivated pre/post-2010 split rather than with an unexplained regime change inside either subsample. These diagnostics support reading the layered ordering as an empirical regularity rather than as the artefact of a single brittle specification."
)

section_heading("6.3 Limitations")
add_para(
    "The limitations of the design should be stated plainly. The models are reduced-form projections; they are not structural causal estimates of how monetary policy or fiscal policy transmits to the price system. The pre/post-2010 split is suggestive evidence consistent with deregulation; it is not a clean policy experiment because other reforms and shocks occurred in the same period. The CPI Fuel and Light bridge sample, beginning in 2011, is shorter than ideal, which limits the power of the negative-shock test in that layer. The WPI Fuel and Power model fails the HAC RESET functional-form test, which means that the exact magnitude of the cumulative pass-through in that layer should be reported with a functional-form caveat. The headline CPI results should be written, throughout, as weak or suggestive rather than as decisive."
)
page_break()

# ============================================================
# CONCLUSION
# ============================================================
chapter_heading("", "Conclusion")

add_para(
    "The dissertation set out to ask where oil-price pass-through weakens inside the Indian price system. The answer is that pass-through in India is layered, not flat. The shock is strong at the points of the chain that are mechanically closest to the rupee oil price, and it is increasingly absorbed at each subsequent layer until it reaches the household-facing aggregate."
)
add_para(
    "The empirical map can be summarised in five sentences. The shock is clear in retail fuel and in fuel-sensitive price indices, where the cumulative pass-through coefficients reach 0.346 in PPAC retail petrol and 0.287 in WPI Fuel and Power. The shock is visible in the fuel-sensitive consumer layer, where the CPI Fuel and Light bridge reports a cumulative pass-through of 0.178 for positive shocks. The shock is statistically visible but small in headline WPI, where the cumulative pass-through is about 0.030. The shock weakens sharply before reaching headline CPI, where the cumulative pass-through is about 0.021 and not statistically distinguishable from zero. Across all layers, short-run asymmetry is not the main finding; where it is most plausibly located, in the retail petrol layer, the evidence is only marginal at the 10 percent level."
)
add_para(
    "The pre/post-2010 wholesale split adds an institutional observation. Pass-through to both headline WPI and WPI Fuel and Power is materially larger in the post-2010 sample than in the pre-2010 sample, consistent with the move toward more market-linked fuel pricing. The split is not a clean causal estimate of deregulation, because the post-2010 period also covers the new CPI series, the move to flexible inflation targeting, the Goods and Services Tax, and a sequence of fuel-tax episodes."
)
add_para(
    "The policy interpretation that follows from these results is similarly restrained. WPI is useful for tracking upstream cost pressure and is the index where oil shocks remain most clearly visible at the headline level, even after dilution. CPI is the index that is anchored to household inflation and that anchors the monetary policy framework, and it is also the index where the oil signal is weakest at the headline level. Neither index should be treated as a substitute for the other in the analysis of oil shocks. A monetary policy framework that uses CPI as its anchor is not insulated from oil shocks, but it sees the shock through a heavily diluted layer; a fiscal or producer-side analysis that uses WPI sees the shock at a magnitude that is small at the headline level but that is large in the fuel-sensitive sub-indices that drive intermediate input costs."
)
add_para(
    "Two extensions are realistic. The first is a more disaggregated CPI decomposition that moves below the headline aggregate to the transport, housing, and miscellaneous services components, in order to trace where the small headline CPI signal is concentrated. The second is a time-varying pass-through model that allows the cumulative coefficients to evolve smoothly with the pricing regime rather than as a single break at June 2010. Both extensions remain inside the same architectural framing used here and would extend rather than replace the layered map presented in this dissertation."
)
add_para(
    "The main lesson is that the question is not whether WPI or CPI is the correct index for oil shocks. The better question is where the oil shock survives inside the price system and where it is absorbed."
)
page_break()

# ============================================================
# REFERENCES
# ============================================================
chapter_heading("", "References")

refs = [
    "Bai, J., & Perron, P. (2003). Computation and analysis of multiple structural change models. Journal of Applied Econometrics, 18(1), 1–22. https://doi.org/10.1002/jae.659",
    "Bhanumurthy, N. R., Das, S., & Bose, S. (2012). Oil price shock, pass-through policy and its impact on India (NIPFP Working Paper No. 2012-99). National Institute of Public Finance and Policy.",
    "Kwiatkowski, D., Phillips, P. C. B., Schmidt, P., & Shin, Y. (1992). Testing the null hypothesis of stationarity against the alternative of a unit root. Journal of Econometrics, 54(1–3), 159–178. https://doi.org/10.1016/0304-4076(92)90104-Y",
    "Mandal, K., Bhattacharyya, I., & Bhoi, B. B. (2012). Is the oil price pass-through in India any different? Journal of Policy Modeling, 34(6), 832–848. https://doi.org/10.1016/j.jpolmod.2012.06.001",
    "Ministry of Statistics and Programme Implementation. (2015). Consumer Price Index: Changes in the revised series. Government of India.",
    "Newey, W. K., & West, K. D. (1987). A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. Econometrica, 55(3), 703–708. https://doi.org/10.2307/1913610",
    "Office of the Economic Adviser. (2017). Manual on Wholesale Price Index: Base 2011-12 = 100. Department for Promotion of Industry and Internal Trade, Ministry of Commerce and Industry, Government of India.",
    "Pal, D., & Mitra, S. K. (2016). Asymmetric oil product pricing in India: Evidence from a multiple threshold nonlinear ARDL model. Economic Modelling, 59, 314–328. https://doi.org/10.1016/j.econmod.2016.08.003",
    "Petroleum Planning and Analysis Cell. (2024). Ready reckoner: India's oil and gas. Ministry of Petroleum and Natural Gas, Government of India.",
    "Pradeep, S. (2022). Impact of diesel price reforms on asymmetricity of oil price pass-through to inflation: Indian perspective. The Journal of Economic Asymmetries, 26, e00249. https://doi.org/10.1016/j.jeca.2022.e00249",
    "World Bank. (2026). Commodity price data: The Pink Sheet. World Bank Commodity Markets.",
]
for r in refs:
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Inches(-0.4)
    p.paragraph_format.left_indent = Inches(0.4)
    p.paragraph_format.space_after = Pt(6)
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run = p.add_run(r)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)

doc.save(OUT)
print(f"Saved: {OUT}")
