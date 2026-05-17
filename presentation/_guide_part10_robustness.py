"""Part 10: Robustness and limitations."""


def build(h):
    add_para = h['add_para']
    add_para_math = h['add_para_math']
    h1 = h['h1']; h2 = h['h2']; h3 = h['h3']
    bullets = h['bullets']
    page_break = h['page_break']
    add_callout = h['add_callout']
    add_table = h['add_table']

    h1("Part 10. Robustness checks and limitations")

    h2("10.1 Six robustness checks, what each one shows")
    bullets([
        "Brent plus exchange-rate decomposition: we split rupee oil into "
        "its two drivers and re-estimate headline WPI. CPT^{+} = 0.0309 "
        "(p = 0.0234), CPT^{−} = 0.0375 (p < 0.001), asymmetry p = 0.7039. "
        "Nearly identical to the rupee-shock result. Conclusion: the "
        "headline WPI result does not depend on how we bundle the two "
        "components.",
        "Bootstrap symmetry: 4,999 restricted-residual circular block "
        "replications. Symmetry is not rejected for headline WPI "
        "(p = 0.7461), the full-sample WPI Fuel and Power context model "
        "(p = 0.8196), and headline CPI (p = 0.4997). Asymmetry is not "
        "the headline finding.",
        "Granger predictive tests: direction from oil to wholesale is "
        "supported; reverse direction is not. Matches the layered reading.",
        "Bai-Perron break tests: where breaks show up in the WPI "
        "inflation series, the institutional pre/post-2010 split is the "
        "policy-relevant way of handling them.",
        "COVID window and winsorising: excluding COVID from the headline "
        "CPI specification, and winsorising at the 1st and 99th "
        "percentiles, leaves the main CPI conclusion unchanged.",
        "Lag-sensitivity: varying the shock lag q between 4 and 8 in the "
        "wholesale models does not change the ranking in Table 9.1.",
    ])

    h2("10.2 Table of diagnostic pass/fail status at a glance")
    add_table(
        headers=["Spec", "BG12", "HAC-RESET", "Rec-CUSUM", "Bootstrap sym. p"],
        rows=[
            ["Headline WPI", "Pass", "Pass", "Pass", "0.7461"],
            ["WPI F&P preferred (post-2010, excl. COVID)", "Pass", "Pass",
             "Pass", "Asym. HAC p = 0.1642"],
            ["WPI F&P pooled context", "Pass", "Fail", "Pass", "0.8196"],
            ["Headline CPI M1", "Pass", "Pass", "Pass", "0.4997"],
            ["PPAC retail petrol", "Pass", "Pass", "Pass",
             "HAC asym. p = 0.0999"],
        ],
        caption="Table 10.1. Diagnostic and symmetry status for every "
                "claim-bearing or context specification.",
        col_widths=[2.5, 0.7, 1.0, 1.0, 1.3],
        font_size=9,
        note="BG12 and HAC-RESET are described in Part 8. The bootstrap "
             "symmetry p-value is reported where computed; otherwise the "
             "HAC-based asymmetry p-value is shown for completeness."
    )

    h2("10.3 Limitations, stated plainly")
    bullets([
        "Reduced-form models, not structural causal estimates. We project; "
        "we do not identify a structural shock.",
        "Different layers have different sample windows, because the "
        "official publishers made each series available at different "
        "dates. The common-sample CPI chain is the check that handles "
        "this concern.",
        "CPI Fuel and Light starts only in 2011, so it is bridge "
        "evidence, not a 20-year headline claim.",
        "PPAC retail petrol uses Delhi prices as a retail-fuel proxy. "
        "Other cities have similar dynamics, but we only run the "
        "estimate on Delhi.",
        "The full-sample pooled WPI Fuel and Power model fails the "
        "functional-form test. We report it as context and move the "
        "wholesale fuel claim to the post-2010 excluding-COVID model.",
        "The pre/post-2010 wholesale split is institutional evidence, "
        "NOT a clean causal estimate of deregulation.",
        "Headline CPI pass-through should be described as weak and not "
        "statistically significant, NOT as ‘zero’.",
        "The layered map is not a single mechanical shock moving through "
        "five equations. It is five related reduced-form equations whose "
        "coefficients share a common interpretation.",
    ])

    add_callout(
        "What to say if a reviewer presses on causality",
        "‘Our estimates are reduced-form short-run projections. The Granger "
        "tests show predictive precedence from oil to wholesale and to "
        "retail fuel, but we do not make structural causal claims. For "
        "structural identification, a shock-based SVAR or a natural "
        "experiment would be needed; that is a logical future extension.’"
    )

    page_break()
