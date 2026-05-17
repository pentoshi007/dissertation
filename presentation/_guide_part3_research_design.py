"""Part 3: research question, objectives, scope, contribution."""


def build(h):
    add_para = h['add_para']
    add_para_math = h['add_para_math']
    h1 = h['h1']; h2 = h['h2']; h3 = h['h3']
    bullets = h['bullets']
    page_break = h['page_break']
    add_callout = h['add_callout']

    h1("Part 3. Research question, objectives, and contribution")

    h2("3.1 Main research question")
    add_para(
        "How do global oil-price shocks transmit across India's wholesale, "
        "retail fuel, fuel-sensitive consumer, and headline consumer price "
        "layers, and where does this pass-through weaken?"
    )
    add_para(
        "Note what the question does not say. It does not ask ‘do oil prices "
        "cause Indian inflation’. It does not ask ‘what is the one true "
        "elasticity between Brent and headline CPI’. It asks how the shock "
        "moves across layers, and where it fades. This framing is the point "
        "of the whole paper."
    )

    h2("3.2 Sub-questions you might be asked in the viva")
    bullets([
        "Does an oil shock visible in wholesale prices also show up in "
        "headline consumer inflation?",
        "Do positive and negative oil shocks have the same size of effect? "
        "This is the asymmetry question.",
        "Did fuel deregulation after 2010 change the size of pass-through? "
        "This is the pre/post-2010 question.",
        "Is headline CPI insulated from oil? If so, why? And if not, how "
        "much of the shock reaches it?",
    ])

    h2("3.3 Research objectives")
    bullets([
        "Build a consistent monthly dataset of oil, exchange rate, WPI, "
        "retail petrol, and CPI layers.",
        "Estimate short-run asymmetric ADL models for each layer using OLS "
        "with Newey-West HAC standard errors.",
        "Summarise each layer's response with cumulative pass-through for "
        "positive shocks (CPT+) and negative shocks (CPT-).",
        "Test whether CPT+ differs from zero, whether CPT- differs from zero, "
        "and whether the two are equal (the symmetry test).",
        "Run diagnostics and robustness checks so the main claims are "
        "defensible.",
        "Present the results as an attenuation map with a formal Wald test "
        "on the consumer-side chain.",
    ])

    h2("3.4 Scope and limits")
    bullets([
        "Monthly frequency only. We do not use daily or quarterly data.",
        "Short-run pass-through only. We do not estimate long-run "
        "equilibrium relationships, so there is no NARDL bounds test, no "
        "error correction model, and no cointegration claim.",
        "India as a whole. Retail petrol prices are taken from Delhi and "
        "treated as a retail-channel proxy, not a national retail measure.",
        "Reduced-form models. We estimate projections, not structural "
        "causal effects.",
    ])

    h2("3.5 Contribution")
    add_para(
        "The main contribution is the layered framing. Instead of one "
        "regression of headline CPI on oil, we fit five reduced-form "
        "equations, one per layer, and put the cumulative pass-through "
        "numbers side by side. This makes the attenuation pattern visible "
        "and testable with a formal Wald test on the common-sample "
        "consumer-side chain."
    )
    add_para(
        "A second smaller contribution is methodological hygiene. We use a "
        "strict diagnostic gate (Breusch-Godfrey, HAC-RESET, recursive "
        "CUSUM) and we report models that fail the gate as context rather "
        "than as claim-bearing estimates. For example, the full-sample "
        "pooled WPI Fuel and Power model fails HAC-RESET, so we report it "
        "as context and move the wholesale fuel claim to the preferred "
        "post-2010 excluding-COVID model which clears the gate cleanly."
    )

    h2("3.6 What we deliberately did not do")
    bullets([
        "No long-run cointegration analysis. Our claim is about monthly "
        "transmission, so long-run tools would be overkill and potentially "
        "misleading.",
        "No structural VAR decomposition. We report predictive precedence "
        "from Granger tests but we do not claim a structural shock "
        "identification.",
        "No disaggregated CPI sub-component regressions beyond Fuel and "
        "Light. That is explicitly listed as a future extension.",
    ])

    add_callout(
        "One-line contribution",
        "Oil pass-through in India is best read as a layered attenuation map, "
        "not as a single elasticity, and we provide the numbers and the formal "
        "test that support that reading."
    )

    page_break()
