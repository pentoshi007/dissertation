"""Part 13: Glossary and cheat sheet."""


def build(h):
    add_para = h['add_para']
    add_para_math = h['add_para_math']
    h1 = h['h1']; h2 = h['h2']; h3 = h['h3']
    bullets = h['bullets']
    page_break = h['page_break']
    add_callout = h['add_callout']
    add_table = h['add_table']

    h1("Part 13. Glossary and cheat sheet")

    h2("13.1 Glossary of acronyms and terms")
    add_table(
        headers=["Term", "Full form / meaning"],
        rows=[
            ["ADL", "Autoregressive Distributed Lag model"],
            ["ADF", "Augmented Dickey-Fuller unit-root test"],
            ["AIC", "Akaike Information Criterion"],
            ["Attenuation", "A reduction in the size of a shock's effect "
                            "as it moves through a chain"],
            ["Bai-Perron", "Structural-break test for multiple unknown breaks"],
            ["BG", "Breusch-Godfrey serial correlation test"],
            ["BIC", "Bayesian Information Criterion"],
            ["Brent", "North Sea crude benchmark used as the global oil "
                      "price reference"],
            ["CPI", "Consumer Price Index (MoSPI)"],
            ["CPI Fuel and Light", "CPI sub-group covering household energy"],
            ["CPT+", "Cumulative positive pass-through"],
            ["CPT−", "Cumulative negative pass-through"],
            ["CUSUM", "Cumulative sum parameter-stability test"],
            ["DPIIT", "Department for Promotion of Industry and Internal "
                      "Trade, Ministry of Commerce and Industry"],
            ["EXINUS", "FRED INR/USD exchange rate series"],
            ["FRED", "Federal Reserve Economic Data, St. Louis Fed"],
            ["GST", "Goods and Services Tax (India, from July 2017)"],
            ["HAC", "Heteroskedasticity and Autocorrelation Consistent "
                    "standard errors (Newey-West)"],
            ["HQIC", "Hannan-Quinn Information Criterion"],
            ["IIP", "Index of Industrial Production (MoSPI)"],
            ["INR", "Indian Rupee"],
            ["KPSS", "Kwiatkowski-Phillips-Schmidt-Shin stationarity test"],
            ["MoCI", "Ministry of Commerce and Industry"],
            ["MoPNG", "Ministry of Petroleum and Natural Gas"],
            ["MoSPI", "Ministry of Statistics and Programme Implementation"],
            ["NIPFP", "National Institute of Public Finance and Policy"],
            ["OEA", "Office of the Economic Adviser, DPIIT, MoCI"],
            ["OLS", "Ordinary Least Squares"],
            ["Pink Sheet", "World Bank's monthly commodity price data bulletin"],
            ["PP", "Phillips-Perron unit-root test"],
            ["PPAC", "Petroleum Planning and Analysis Cell, MoPNG"],
            ["RESET", "Ramsey Regression Equation Specification Error Test"],
            ["USD", "United States Dollar"],
            ["Wald test", "Test of linear restrictions on coefficients"],
            ["WPI", "Wholesale Price Index (Office of the Economic Adviser)"],
            ["WPI Fuel and Power", "WPI sub-group covering fuel, power, and "
                                   "mineral oils"],
            ["Zivot-Andrews", "Unit-root test allowing one structural break"],
        ],
        caption="Table 13.1. Acronyms and terms used throughout the paper "
                "and this guide.",
        col_widths=[1.8, 4.6],
        font_size=10,
    )

    h2("13.2 One-page cheat sheet you can glance at during the presentation")
    bullets([
        "Question: where does oil pass-through weaken across Indian "
        "price layers?",
        "Answer: it weakens between fuel layers and the broad headline "
        "consumer index.",
        "Main result numbers: CPT+ = 0.5205 preferred WPI F&P (p<0.001); "
        "0.3459 retail petrol (p<0.001); 0.1777 CPI F&L bridge "
        "(p=0.0021); 0.0301 headline WPI (p=0.024); 0.0213 headline CPI "
        "(p=0.122, not significant).",
        "Formal attenuation test: F = 14.3499, p = 0.0002. Reject "
        "equality between retail petrol and headline CPI CPT+.",
        "Asymmetry: only marginal at retail petrol (p=0.0999). Not the "
        "headline finding.",
        "Method: short-run asymmetric ADL in monthly log differences, "
        "OLS with Newey-West HAC standard errors, bootstrap symmetry "
        "check with 4,999 replications.",
        "Lag orders: ADL(12,6) for WPI models, ADL(3,3) for CPI and "
        "retail petrol models.",
        "Diagnostic gate: Breusch-Godfrey, HAC-RESET, recursive CUSUM. "
        "All claim-bearing models pass.",
        "Data sources (full form): OEA WPI, MoSPI CPI, PPAC Delhi "
        "petrol, World Bank Pink Sheet Brent, FRED EXINUS for "
        "INR/USD.",
        "Core message: oil still matters in India, but most of it is "
        "absorbed before it reaches headline CPI.",
    ])

    add_callout(
        "Closing line to rehearse",
        "‘Oil shocks do not vanish in India, but they lose force as they "
        "move from fuel prices to broad consumer inflation.’"
    )
