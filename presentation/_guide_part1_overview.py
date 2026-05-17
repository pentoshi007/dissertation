"""Part 1: one-page overview of the whole research."""


def build(h):
    add_para = h['add_para']
    add_para_math = h['add_para_math']
    h1 = h['h1']; h2 = h['h2']; h3 = h['h3']
    bullets = h['bullets']
    page_break = h['page_break']
    add_callout = h['add_callout']

    h1("Part 1. The big picture in one page")

    h2("1.1 What is the research about, in one line")
    add_para(
        "We study how changes in the global price of crude oil reach different "
        "layers of prices in India, and we show that the effect is large near "
        "fuel prices but becomes much weaker by the time it hits the headline "
        "consumer price index."
    )

    h2("1.2 Why does it matter")
    bullets([
        "India imports most of its crude oil, and crude is priced in US dollars. "
        "So every oil shock is also partly a rupee-dollar shock.",
        "Headline CPI is the number the Reserve Bank of India targets for "
        "inflation. If headline CPI moves only a little with oil, people may "
        "think oil no longer matters for Indian inflation. We show that is the "
        "wrong reading. Oil still matters. It matters most in fuel-related "
        "prices and becomes diluted by the time you reach the broad basket.",
        "For a policy reader this is useful. It says that headline CPI alone "
        "hides fuel-side pressure. You have to look at WPI Fuel and Power, "
        "retail petrol, and CPI Fuel and Light to see it.",
    ])

    h2("1.3 The five price layers we look at")
    bullets([
        "Headline WPI: the broad wholesale price index.",
        "WPI Fuel and Power: the fuel-specific part of WPI.",
        "PPAC Delhi retail petrol: the price you actually pay at the pump.",
        "CPI Fuel and Light: the fuel-related part of the consumer basket.",
        "Headline CPI: the broad consumer price index.",
    ])

    h2("1.4 The one-line punchline of the results")
    add_para_math(
        "Positive cumulative pass-through CPT^{+} (a fancy name for ‘how much "
        "of a one per cent oil rise shows up in the dependent price over the "
        "model's lag window’) is about 0.52 for the preferred WPI Fuel and "
        "Power model, 0.35 for retail petrol, 0.18 for CPI Fuel and Light, "
        "0.03 for headline WPI, and only 0.02 for headline CPI — and headline "
        "CPI is not even statistically significant. The numbers fall as we "
        "move from fuel to the broad consumer index. That fall is what we "
        "call layered attenuation."
    )

    h2("1.5 One sentence on each technical ingredient")
    bullets([
        "Model: short-run asymmetric ADL in monthly log differences. ADL = "
        "autoregressive distributed lag. Asymmetric = positive and negative "
        "shocks enter separately. Short-run = we do not chase long-run "
        "relationships; the question is monthly response.",
        "Estimation: OLS, exactly the standard least squares you met in your "
        "first econometrics class, but with Newey-West HAC standard errors to "
        "fix the fact that monthly price data are auto-correlated and "
        "heteroscedastic.",
        "Inference: tests on whether the cumulative pass-through is zero, "
        "and whether positive and negative responses are equal (the symmetry "
        "test). Plus a restricted-residual circular block bootstrap with "
        "4,999 replications as a robustness check.",
        "Diagnostics gate: a model only carries a main claim if it passes "
        "Breusch-Godfrey (no leftover serial correlation), HAC-RESET "
        "(functional form not obviously wrong), and recursive CUSUM "
        "(coefficients stable over time).",
    ])

    h2("1.6 Research question in one sentence")
    add_para(
        "How do global oil-price shocks transmit across India's wholesale, "
        "retail fuel, fuel-sensitive consumer, and headline consumer price "
        "layers, and where does this pass-through weaken?"
    )

    h2("1.7 Contribution in one sentence")
    add_para(
        "We treat oil pass-through as a layered transmission problem across "
        "different price indices rather than as a single number linking crude "
        "to headline CPI, and we keep each layer's sample, shock variable, "
        "and diagnostics visible so nothing is hidden."
    )

    add_callout(
        "Remember",
        "The dissertation does not claim oil causes Indian inflation. It claims "
        "oil shocks pass through strongly at fuel layers and weakly at the "
        "headline CPI layer, and the difference is statistically rejected by a "
        "Wald test."
    )

    page_break()
