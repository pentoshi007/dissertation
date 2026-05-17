"""Part 9: Results, layer by layer. Every number from the paper explained."""

import os


def build(h):
    add_para = h['add_para']
    add_para_math = h['add_para_math']
    h1 = h['h1']; h2 = h['h2']; h3 = h['h3']
    bullets = h['bullets']
    page_break = h['page_break']
    add_callout = h['add_callout']
    add_table = h['add_table']
    add_figure = h['add_figure']
    ROOT = h['ROOT']

    h1("Part 9. Results: what the numbers say, layer by layer")

    h2("9.1 One table with every main number")
    add_table(
        headers=["Layer", "Sample", "N", "CPT+", "p", "CPT−", "p",
                 "Asym. p", "Verdict"],
        rows=[
            ["PPAC retail petrol", "2004-08 to 2024-12", "245",
             "0.3459", "<0.001", "0.1912", "0.0002", "0.0999",
             "Strong direct fuel; marginal asymmetry"],
            ["WPI Fuel and Power (preferred)", "2010-04 to 2026-03", "186",
             "0.5205", "<0.001", "0.4195", "<0.001", "0.1642",
             "Preferred wholesale fuel; diagnostics pass"],
            ["CPI Fuel and Light (bridge)", "2011-05 to 2024-12", "164",
             "0.1777", "0.0021", "0.1058", "0.1741", "0.4554",
             "Bridge evidence; shorter sample"],
            ["Headline WPI", "1983-05 to 2026-03", "515",
             "0.0301", "0.0240", "0.0374", "0.0012", "0.6727",
             "Modest but significant"],
            ["Headline CPI (M1)", "2004-08 to 2024-12", "245",
             "0.0213", "0.1220", "0.0006", "0.9375", "0.2408",
             "Weak, not significant"],
        ],
        caption="Table 9.1. Cumulative pass-through across all five layers.",
        col_widths=[1.7, 1.2, 0.35, 0.5, 0.5, 0.5, 0.5, 0.55, 1.6],
        font_size=8.5,
        note="CPT+ sums the β^+ coefficients across the ADL shock lags. CPT− "
             "sums the β^− coefficients. p-values use Newey-West HAC "
             "inference. WPI models use rupee oil shocks, retail petrol uses "
             "Brent, and CPI Fuel and Light uses PPAC petrol as the shock."
    )

    h2("9.2 Headline WPI")
    add_para(
        "The headline WPI model runs from May 1983 to March 2026, with "
        "N = 515 monthly observations. The adjusted R² is 0.421, which "
        "means the model explains about 42 per cent of the monthly "
        "variation in headline WPI inflation."
    )
    add_para_math(
        "CPT^{+} = 0.0301 with p = 0.0240 says a one per cent positive "
        "rupee oil shock is associated with a cumulative 0.03 per cent "
        "response in headline WPI. That is small in magnitude but "
        "statistically distinguishable from zero at the 5 per cent level. "
        "CPT^{−} = 0.0374 with p = 0.0012 is the negative-shock sum, also "
        "statistically significant. The asymmetry test gives p = 0.6727 "
        "(HAC) and p = 0.7461 (bootstrap). We cannot reject that positive "
        "and negative responses are equal, so the WPI layer does not "
        "support asymmetric pass-through."
    )
    add_callout(
        "In words",
        "A big rise in the rupee oil price does move headline WPI, but not "
        "by much. Headline WPI is too broad for oil to dominate it."
    )

    h2("9.3 WPI Fuel and Power (preferred specification)")
    add_para(
        "This is our preferred wholesale fuel result. The sample is "
        "April 2010 to March 2026, excluding April-September 2020 (COVID). "
        "N = 186. Adjusted R² is about 0.68. The diagnostics pass the gate: "
        "BG p = 0.0746, HAC-RESET p = 0.5443, recursive CUSUM p = 0.6999."
    )
    add_para_math(
        "CPT^{+} = 0.5205 with p < 0.001. A one per cent positive rupee "
        "oil shock is associated with roughly a 0.52 per cent cumulative "
        "response in WPI Fuel and Power inflation. CPT^{−} = 0.4195 with "
        "p < 0.001. Asymmetry p = 0.1642, so we do not reject symmetry."
    )
    add_para(
        "Why is this layer so much bigger than headline WPI? Because this "
        "index is close to the fuel channel. It contains petrol, diesel, "
        "LPG, electricity, and coal-adjacent items, all of which track "
        "oil costs closely. The headline WPI basket mixes this with "
        "manufactured goods and food, diluting the fuel signal."
    )

    h2("9.4 Why we reject the older full-sample pooled Fuel and Power model")
    add_para(
        "We also fit a full-sample pooled WPI Fuel and Power model over "
        "1995-05 to 2026-03 with N = 371. It gives CPT^{+} = 0.2866 and "
        "CPT^{−} = 0.2677. Both are statistically significant. But HAC-"
        "RESET fails, so the functional form is misspecified. We report "
        "that estimate as ‘context only’ because the full sample mixes the "
        "administered-pricing regime, the market-linked regime, and COVID "
        "outliers. The preferred post-2010 excluding-COVID specification "
        "clears the diagnostic gate cleanly and is what we use for the "
        "wholesale fuel claim."
    )

    h2("9.5 PPAC retail petrol")
    add_para(
        "The retail petrol model runs from August 2004 to December 2024, "
        "with N = 245. The adjusted R² is 0.236. The shock is Brent "
        "directly, because retail petrol pricing under the post-2010 "
        "rules is anchored to international product prices."
    )
    add_para_math(
        "CPT^{+} = 0.3459 with p < 0.001. A one per cent positive Brent "
        "shock is associated with a cumulative 0.35 per cent response in "
        "Delhi retail petrol over the three-month shock window. "
        "CPT^{−} = 0.1912 with p = 0.0002. Asymmetry p = 0.0999."
    )
    add_callout(
        "Asymmetry reading",
        "The asymmetry p-value just below 0.10 is the one place in the "
        "paper where asymmetry is suggestive. It is the well-known "
        "‘rockets and feathers’ pattern: retail petrol rises faster than "
        "it falls. But we are careful to say ‘marginal at the 10 per cent "
        "level’, not ‘significant asymmetry’."
    )

    h2("9.6 CPI Fuel and Light bridge")
    add_para(
        "This equation uses PPAC petrol as the shock and CPI Fuel and "
        "Light as the dependent. The sample is May 2011 to December 2024, "
        "N = 164. The shorter sample is why we call it bridge evidence."
    )
    add_para_math(
        "CPT^{+} = 0.1777 with p = 0.0021. A one per cent positive retail "
        "petrol shock is associated with a cumulative 0.18 per cent "
        "response in CPI Fuel and Light. CPT^{−} = 0.1058 with p = 0.1741 "
        "is not significant. Asymmetry p = 0.4554."
    )
    add_para(
        "The bridge shows that retail fuel movements do enter the "
        "fuel-sensitive part of the consumer basket, at a size smaller "
        "than retail petrol but larger than headline CPI. That is exactly "
        "the shape attenuation would produce."
    )

    h2("9.7 Headline CPI endpoint")
    add_para(
        "The headline CPI model uses rupee oil as the shock. Sample "
        "2004-08 to 2024-12, N = 245, adjusted R² = 0.4492. Diagnostics "
        "pass the mandatory gate."
    )
    add_para_math(
        "CPT^{+} = 0.0213 with p = 0.1220. The positive-shock cumulative "
        "response has the expected sign but is NOT statistically "
        "significant at conventional levels. CPT^{−} = 0.0006, p = "
        "0.9375, is essentially zero. Asymmetry p = 0.2408 does not reject "
        "symmetry. Bootstrap symmetry p = 0.4997."
    )
    add_callout(
        "Key takeaway",
        "This is the crucial number. Headline CPI is where oil becomes "
        "statistically quiet. We describe it as weak and not significant, "
        "NEVER as ‘zero’ or ‘no effect’."
    )

    h2("9.8 The integrated attenuation Wald test")
    add_para(
        "To make the attenuation story formal we estimate the "
        "consumer-side chain on a common sample window and then test "
        "whether the first-stage pass-through equals the third-stage "
        "pass-through."
    )
    add_table(
        headers=["Stage", "What it measures", "CPT+", "p"],
        rows=[
            ["Stage 1", "Brent → PPAC retail petrol", "0.4007", "0.0001"],
            ["Stage 2", "PPAC petrol → CPI Fuel and Light", "0.1777", "0.0021"],
            ["Stage 3", "Rupee oil → Headline CPI", "0.0064", "0.6355"],
        ],
        caption="Table 9.2. Consumer-side chain, common-sample estimates.",
        col_widths=[0.8, 2.9, 1.0, 0.8],
        font_size=9.5,
    )
    add_para_math(
        "Formal Wald test: H_{0}: CPT^{+}_{Stage 1} = CPT^{+}_{Stage 3}. "
        "F = 14.3499, p = 0.0002. We reject equality. Attenuation across "
        "the consumer-price chain is statistically supported."
    )

    # Figure: the attenuation chain
    add_figure(
        os.path.join(ROOT, "models/cpi/outputs/figures/fig_13_dilution_chain.png"),
        "Figure 9.1. Cumulative positive pass-through across the consumer-"
        "price chain, showing attenuation from retail petrol to headline CPI."
    )

    h2("9.9 Pre/post-2010 wholesale split (institutional context)")
    add_table(
        headers=["Model", "Pre-2010 CPT+ (p)", "Post-2010 CPT+ (p)"],
        rows=[
            ["Headline WPI", "0.0117 (p = 0.3812)", "0.0741 (p = 0.0043)"],
            ["WPI Fuel and Power", "0.0922 (p = 0.1679)", "0.5241 (p < 0.001)"],
        ],
        caption="Table 9.3. Pre/post-2010 wholesale pass-through split.",
        col_widths=[2.0, 2.0, 2.0],
        font_size=10,
        note="The split is institutional evidence consistent with stronger "
             "pass-through under market-linked fuel pricing. It is NOT a "
             "clean causal estimate of deregulation."
    )
    add_para(
        "Both rows show the post-2010 estimates are materially larger and "
        "statistically stronger. Under more market-linked pricing, a given "
        "oil shock passes through to wholesale more of the time and "
        "faster. Other things changed over the same period too: new CPI "
        "series 2011, flexible inflation targeting 2016, GST 2017, and "
        "several fuel-tax episodes. So we do not call this a clean "
        "deregulation experiment."
    )

    h2("9.10 Predictive precedence (Granger tests)")
    bullets([
        "Rupee oil → headline WPI: F = 7.43, p < 0.001. Supported.",
        "Rupee oil → WPI Fuel and Power: F = 15.22, p < 0.001. Supported.",
        "Brent → PPAC petrol: F = 10.71, p < 0.001. Supported.",
        "Rupee oil → headline CPI: F = 2.29, p = 0.0794. Only at the 10 "
        "per cent level. Weak.",
        "PPAC petrol → CPI Fuel and Light: p = 0.113. Not supported.",
    ])
    add_para(
        "This lines up with the main estimates: the oil signal is easy to "
        "pick up near fuel prices and harder to detect in the broad CPI."
    )

    h2("9.11 The one-line summary of the results chapter")
    add_callout(
        "Remember this",
        "Strong in retail petrol and WPI Fuel and Power. Medium in CPI Fuel "
        "and Light. Modest in headline WPI. Weak and not significant in "
        "headline CPI. Wald test formally rejects that retail petrol and "
        "headline CPI positive pass-throughs are equal."
    )

    page_break()
