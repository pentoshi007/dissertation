"""Part 11: Conclusion and the big takeaways."""


def build(h):
    add_para = h['add_para']
    h1 = h['h1']; h2 = h['h2']; h3 = h['h3']
    bullets = h['bullets']
    page_break = h['page_break']
    add_callout = h['add_callout']

    h1("Part 11. Conclusion and the policy takeaways")

    h2("11.1 Direct answer to the research question")
    add_para(
        "Oil-price shocks transmit to India's prices in a layered way. They "
        "are strong in retail petrol (CPT+ = 0.3459) and in the preferred "
        "WPI Fuel and Power model (CPT+ = 0.5205). They are still visible "
        "in CPI Fuel and Light (CPT+ = 0.1777). They are modest but "
        "statistically significant in headline WPI (CPT+ = 0.0301). And "
        "they are weak and not statistically significant in headline CPI "
        "(CPT+ = 0.0213). The formal Wald test rejects equality between "
        "the retail petrol and headline CPI positive pass-through "
        "(F = 14.3499, p = 0.0002). So the pass-through weakens "
        "specifically between the fuel layers and the broad consumer "
        "index."
    )

    h2("11.2 Policy takeaways, carefully stated")
    bullets([
        "A monetary-policy framework that relies only on headline CPI may "
        "miss oil-side pressure, because oil's footprint at that layer is "
        "statistically small.",
        "Monitoring a small set of fuel-sensitive layers (retail petrol, "
        "WPI Fuel and Power, CPI Fuel and Light) gives more short-run "
        "information about oil pass-through than the headline alone.",
        "The larger post-2010 wholesale pass-through is consistent with "
        "a more market-linked fuel pricing regime. It is not a clean "
        "causal estimate of deregulation, so the wording should stay "
        "cautious.",
        "Asymmetric pricing (rockets and feathers) is marginal at retail "
        "petrol, and not supported at the headline layers.",
    ])

    h2("11.3 What we do not claim")
    bullets([
        "We do not claim oil is irrelevant for Indian inflation.",
        "We do not claim deregulation caused bigger pass-through.",
        "We do not claim asymmetric pass-through is the headline finding.",
        "We do not claim a single structural chain from Brent to "
        "headline CPI.",
        "We do not claim headline CPI pass-through is zero. It is weak "
        "and not significant in our sample.",
    ])

    h2("11.4 Natural extensions for future work")
    bullets([
        "Decompose headline CPI into transport, housing, and "
        "miscellaneous services and trace where the small headline "
        "signal sits.",
        "Fit a time-varying-parameter ADL so the coefficients can drift "
        "smoothly with the pricing regime rather than breaking at a "
        "single date.",
        "A structural VAR with identified oil-supply and exchange-rate "
        "shocks, to convert the reduced-form map into a causal "
        "decomposition.",
        "A cross-country comparison of attenuation maps across oil-"
        "importing emerging economies.",
    ])

    h2("11.5 Closing line, the one the teacher will remember")
    add_para(
        "Oil shocks do not vanish in India, but they lose force as they "
        "move from fuel prices to broad consumer inflation."
    )

    add_callout(
        "If you only remember one thing",
        "This study turns oil pass-through into a layered attenuation map. "
        "The numbers fall cleanly from retail petrol and WPI Fuel and "
        "Power down to headline CPI, and the formal Wald test says that "
        "fall is statistically real."
    )

    page_break()
