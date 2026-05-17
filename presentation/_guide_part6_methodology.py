"""Part 6: Methodology. ADL, OLS, Greek letters, ADL(p,q) selection."""


def build(h):
    add_para = h['add_para']
    add_para_math = h['add_para_math']
    h1 = h['h1']; h2 = h['h2']; h3 = h['h3']
    bullets = h['bullets']
    page_break = h['page_break']
    add_callout = h['add_callout']
    add_equation = h['add_equation']
    add_code_block = h['add_code_block']
    add_table = h['add_table']
    mr = h['mr']; msub = h['msub']; msup = h['msup']; msubsup = h['msubsup']
    mfenced = h['mfenced']; mnary_sum = h['mnary_sum']

    h1("Part 6. Methodology: the ADL model in plain language")

    h2("6.1 What is an ADL model")
    add_para(
        "ADL stands for Autoregressive Distributed Lag. Let us unpack that:"
    )
    bullets([
        "‘Autoregressive’ means the dependent variable depends on its own "
        "past values. If last month's inflation in WPI Fuel and Power was "
        "high, this month's is also likely to be a bit higher on average. "
        "So we put lags of the dependent variable on the right-hand side.",
        "‘Distributed lag’ means the explanatory variable enters not only "
        "at time t, but also at t−1, t−2, and so on. We let the effect of "
        "an oil shock spread out over several months, because in reality "
        "refiners, taxes, and supply chains take time to pass costs on.",
        "‘Short-run asymmetric’ means (a) we are interested in the monthly "
        "dynamics, not the long-run level relationship, and (b) positive "
        "and negative shocks are entered as separate variables.",
    ])

    h2("6.2 The full ADL equation with every term explained")
    eq_body = (
        msub(mr('Δy'), mr('t')) + mr(' = α + ') +
        mnary_sum(mr('i=1'), mr('p'),
                  msub(mr('φ'), mr('i')) + msub(mr('Δy'), mr('t−i'))) +
        mr(' + ') +
        mnary_sum(mr('j=0'), mr('q'),
                  msubsup(mr('β'), mr('j'), mr('+')) +
                  msubsup(mr('Δx'), mr('t−j'), mr('+'))) +
        mr(' + ') +
        mnary_sum(mr('j=0'), mr('q'),
                  msubsup(mr('β'), mr('j'), mr('−')) +
                  msubsup(mr('Δx'), mr('t−j'), mr('−'))) +
        mr(" + γ'") + msub(mr('Z'), mr('t')) + mr(' + ') +
        msub(mr('μ'), mr('m')) + mr(' + ') + msub(mr('ε'), mr('t'))
    )
    add_equation(eq_body, label="(6.1)")

    h2("6.3 Every symbol, one by one")
    add_table(
        headers=["Symbol", "Name", "What it means in plain language"],
        rows=[
            ["Δy_t", "Delta y sub t",
             "The percentage monthly change in the dependent price index at "
             "month t. E.g. this month's inflation in headline CPI."],
            ["α", "Alpha",
             "The intercept, or baseline monthly inflation when all "
             "right-hand-side variables are zero. It sets the ‘average level’ "
             "of the equation."],
            ["φ_i", "Phi sub i",
             "The coefficient on the i-th lag of the dependent variable. "
             "Measures how persistent inflation is in that index."],
            ["p", "p",
             "The number of own-lags used. For WPI models we use p = 12 to "
             "capture the annual cycle; for CPI and retail petrol we use "
             "p = 3, chosen by AIC over p = 1 to 4."],
            ["β^{+}_j", "beta plus sub j",
             "The coefficient on the j-th lag of the positive oil shock. Its "
             "sign tells us how a positive oil shock j months ago affects "
             "today's inflation."],
            ["β^{−}_j", "beta minus sub j",
             "The coefficient on the j-th lag of the negative oil shock."],
            ["q", "q",
             "The number of shock lags. For WPI we use q = 6 (wholesale "
             "channels are slower). For retail petrol and CPI we use q = 3 "
             "(fuel pricing and consumer baskets respond faster)."],
            ["Z_t", "Z sub t",
             "A vector of extra controls. For the retail petrol equation it "
             "contains IIP growth and the petrol/diesel deregulation "
             "dummies. For headline CPI it contains the same, plus a COVID "
             "dummy."],
            ["γ", "Gamma",
             "The vector of coefficients on those controls. The prime (γ') "
             "just means ‘multiply γ against the vector Z_t row by row’."],
            ["μ_m", "Mu sub m",
             "The month-of-year dummy. Eleven dummies for eleven months, "
             "with one month as the reference. Soaks up residual "
             "seasonality that survives log-differencing."],
            ["ε_t", "Epsilon sub t",
             "The error term. Everything the model did not explain. It is "
             "allowed to be heteroscedastic and autocorrelated; that is why "
             "we fix the standard errors later."],
        ],
        caption="Table 6.1. Every Greek letter and symbol in the ADL equation, "
                "translated.",
        col_widths=[0.9, 1.3, 4.2],
        font_size=10,
        note="Σ is the sum symbol. The subscript below Σ is where the index "
             "starts; the superscript above Σ is where it ends."
    )

    h2("6.4 How the coefficients α, β, γ, φ, μ are derived: OLS in plain terms")
    add_para(
        "All the coefficients in the ADL equation are estimated by ordinary "
        "least squares, OLS, exactly the same OLS you met in first-year "
        "econometrics. Nothing exotic."
    )
    add_para_math(
        "OLS picks the numbers α̂, β̂^{+}_{j}, β̂^{−}_{j}, γ̂, φ̂_{i}, μ̂_{m} "
        "that make the sum of squared residuals Σ ε̂^{2}_{t} as small as "
        "possible. A residual ε̂_{t} is the gap between the actual Δy_{t} "
        "we observe and the value our equation would predict for that month. "
        "OLS says: choose the coefficients so these gaps, squared and "
        "summed over all months in the sample, are minimised."
    )
    add_callout(
        "Why squares, not absolute values",
        "Squaring punishes big misses more than small ones and makes the "
        "math tractable. Under classical assumptions it is also the "
        "best-linear-unbiased estimator by the Gauss-Markov theorem."
    )

    h2("6.5 A tiny worked example of OLS")
    add_para(
        "Imagine a toy regression: Δy_{t} = α + β ΔBrent_{t} + ε_{t} with "
        "just three observations:"
    )
    add_table(
        headers=["Month", "ΔBrent", "Δy"],
        rows=[["t=1", "1.0", "0.4"], ["t=2", "2.0", "0.9"], ["t=3", "3.0", "1.3"]],
        caption="Table 6.2. Toy data for the OLS worked example.",
        col_widths=[1.0, 1.2, 1.2],
        font_size=10,
    )
    add_para(
        "If we choose α = 0 and β = 0.45, the predicted Δy values are "
        "0.45, 0.90, 1.35. The residuals are (0.4−0.45)=−0.05, "
        "(0.9−0.90)=0.0, (1.3−1.35)=−0.05. The sum of squared residuals "
        "is 0.005. OLS tries every possible pair (α, β) and picks the pair "
        "with the smallest sum of squared residuals. In practice the "
        "statistical package solves a simple matrix equation to find this "
        "minimum in one step."
    )
    add_para(
        "The same logic scales up to our ADL equation with many lags and "
        "many controls. Instead of two coefficients the software estimates "
        "thirty or more, but the principle is identical: the chosen "
        "coefficients are the ones that minimise the total squared "
        "prediction error."
    )

    add_code_block(
        "# Pseudo-code for OLS fit used inside the R scripts\n"
        "y  <- dln_cpi                              # dependent variable\n"
        "X  <- cbind(1,                             # intercept\n"
        "            dln_cpi_lag1, dln_cpi_lag2, dln_cpi_lag3,\n"
        "            dln_oil_inr_pos, dln_oil_inr_pos_lag1,\n"
        "            dln_oil_inr_pos_lag2, dln_oil_inr_pos_lag3,\n"
        "            dln_oil_inr_neg, dln_oil_inr_neg_lag1,\n"
        "            dln_oil_inr_neg_lag2, dln_oil_inr_neg_lag3,\n"
        "            dln_iip, D_petrol, D_diesel, D_covid,\n"
        "            month_dummies)\n"
        "\n"
        "beta_hat <- solve(t(X) %*% X) %*% (t(X) %*% y)    # OLS closed-form\n"
        "residuals <- y - X %*% beta_hat\n"
    )

    h2("6.6 How many lags to use: the (p, q) in ADL(p, q)")
    add_para(
        "ADL(p, q) is shorthand for ‘p lags of the dependent variable and q "
        "lags of the shock variable’. The choices we use come from the "
        "lag-selection tables inside the model pipelines, not from guesswork."
    )
    bullets([
        "For the headline WPI and WPI Fuel and Power equations we use "
        "ADL(12, 6). Twelve own-lags capture the annual cycle in wholesale "
        "inflation even after month dummies. Six shock-lags let the oil "
        "effect stretch half a year, which matches how wholesale passes "
        "from refineries through the supply chain.",
        "For the CPI Fuel and Light bridge and the headline CPI equations we "
        "use ADL(3, 3). Three own-lags because AIC over p in {1, 2, 3, 4} "
        "prefers three. Three shock-lags because the retail fuel and "
        "consumer-basket transmission is fast and deeper lags add noise.",
        "For the PPAC retail petrol equation we also use ADL(3, 3). "
        "Retail petrol adjusts quickly under post-2010 rules, so longer "
        "lags are not needed.",
    ])
    add_para(
        "AIC stands for Akaike Information Criterion. It rewards models that "
        "fit the data well and penalises models with too many parameters. "
        "Lower AIC is better. BIC (Bayesian Information Criterion) is the "
        "same idea with a stronger penalty for extra parameters. HQIC "
        "(Hannan-Quinn Information Criterion) is similar. We pick the lag "
        "order that minimises AIC among candidate orders, and confirm with "
        "BIC and HQIC when possible."
    )

    h2("6.7 Why we include month dummies")
    add_para(
        "Some months are systematically more inflationary than others, for "
        "reasons unrelated to oil: the monsoon hits food prices, festival "
        "seasons shift consumption patterns, tax-revision calendars align "
        "with fiscal years. Taking monthly log differences removes part of "
        "this seasonality but not all. Adding eleven monthly dummies for "
        "February through December (with January as the omitted reference "
        "month) absorbs the rest."
    )

    h2("6.8 Why we include policy dummies and a COVID dummy")
    bullets([
        "D_petrol captures the intercept shift after June 2010 petrol "
        "deregulation. Without it, the ADL equation would average pre- and "
        "post-2010 behaviour together and could bias the shock coefficients.",
        "D_diesel does the same for October 2014 diesel deregulation.",
        "D_covid flags the unusual April-September 2020 period. During "
        "COVID, oil prices collapsed and Indian retail prices did not move "
        "the way the usual pricing rules would suggest, because demand was "
        "extraordinary. Leaving those months in without a flag can distort "
        "the estimates.",
    ])
    add_callout(
        "Two ways we handle COVID",
        "For most models we include a D_covid dummy. For the preferred WPI "
        "Fuel and Power model we go further and drop April-September 2020 "
        "entirely from the sample, because the functional-form diagnostic "
        "test otherwise fails due to these outliers."
    )

    h2("6.9 One equation, five estimations")
    add_table(
        headers=["Layer", "Δy (dependent)", "Δx (shock)", "ADL(p,q)", "Main controls in Z"],
        rows=[
            ["Headline WPI", "WPI inflation", "Rupee oil shock", "ADL(12,6)",
             "Month fixed effects"],
            ["WPI Fuel and Power (preferred)", "WPI Fuel and Power inflation",
             "Rupee oil shock", "ADL(12,6)",
             "Exchange-rate controls, month dummies, post-2010 sample, "
             "excludes Apr-Sep 2020"],
            ["PPAC retail petrol", "Delhi retail petrol inflation", "Brent shock",
             "ADL(3,3)", "IIP growth, D_petrol, D_diesel, D_covid, month dummies"],
            ["CPI Fuel and Light (bridge)", "CPI Fuel and Light inflation",
             "PPAC petrol shock", "ADL(3,3)", "Month dummies"],
            ["Headline CPI (M1)", "Headline CPI inflation", "Rupee oil shock",
             "ADL(3,3)", "IIP growth, D_petrol, D_diesel, D_covid, month dummies"],
        ],
        caption="Table 6.3. The five estimated equations, their shock and "
                "dependent variables, lag order, and controls.",
        col_widths=[1.6, 1.4, 1.1, 0.9, 2.0],
        font_size=9,
        note="Every row is a separate OLS regression. The paper does not "
             "combine them into one simultaneous system."
    )

    page_break()
