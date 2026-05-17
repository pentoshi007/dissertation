"""Part 8: Diagnostics. Every test in beginner language, built to memorise
on the first read. Includes the WPI Fuel and Power RESET fix in detail.
"""


def build(h):
    add_para = h['add_para']
    add_para_math = h['add_para_math']
    h1 = h['h1']; h2 = h['h2']; h3 = h['h3']
    bullets = h['bullets']
    page_break = h['page_break']
    add_callout = h['add_callout']
    add_table = h['add_table']
    add_code_block = h['add_code_block']

    h1("Part 8. Every test, in plain language")

    add_para(
        "This part covers every statistical test used anywhere in the paper. "
        "For each test you will see four things: what problem it checks, "
        "what its null hypothesis H0 says in plain words, a one-sentence "
        "rule for reading the p-value, and a quick memory hook. Read the "
        "memory hook aloud once and you will remember the test on the first "
        "try."
    )

    # -----------------------------------------------------------------------
    h2("8.1 The memory rule that works for every test")
    add_para_math(
        "Every test gives one number, the p-value. There is only one rule "
        "you need: if p < 0.05, we reject H_{0}. If p ≥ 0.05, we fail to "
        "reject H_{0}. ‘Reject’ means ‘the data disagree with H_{0}’. ‘Fail "
        "to reject’ means ‘the data are fine with H_{0}’. Whether rejecting "
        "is good news or bad news depends on what the test is checking. "
        "That is where students go wrong, so each test below tells you "
        "which direction you want."
    )
    add_callout(
        "Rule of thumb",
        "Small p (below 0.05) = reject H0. Large p (0.05 or more) = fail "
        "to reject H0. Whether that is good or bad depends on what H0 says."
    )

    # =======================================================================
    # STATIONARITY / UNIT ROOT TESTS
    # =======================================================================
    h2("8.2 Unit root tests: is the series stationary?")
    add_para(
        "A ‘stationary’ series has a stable mean and variance over time. A "
        "‘unit root’ series drifts indefinitely and needs to be differenced "
        "to calm it down. If we run a regression on two unit-root series in "
        "levels, we get a spurious ‘significant’ result just because both "
        "are trending. So we test for unit roots before fitting the model."
    )

    h3("ADF test (Augmented Dickey-Fuller)")
    bullets([
        "What it checks: does the series have a unit root?",
        "H0 (null): the series has a unit root (non-stationary).",
        "Rule: small p = reject H0 = series is stationary (good for us).",
        "Memory hook: ADF says ‘You are non-stationary until proven "
        "stationary.’ A low p breaks the default verdict.",
    ])

    h3("PP test (Phillips-Perron)")
    bullets([
        "What it checks: same question as ADF, but it handles "
        "autocorrelation in a non-parametric way.",
        "H0: the series has a unit root.",
        "Rule: small p = reject = stationary.",
        "Memory hook: PP is ADF's cousin with a different cleaning routine.",
    ])

    h3("KPSS test (Kwiatkowski-Phillips-Schmidt-Shin, 1992)")
    bullets([
        "What it checks: the OPPOSITE of ADF. Starts from stationarity.",
        "H0: the series is stationary.",
        "Rule: small p = reject = NOT stationary (has a unit root).",
        "Memory hook: KPSS is the ‘flip’. If KPSS says p < 0.05, that is "
        "BAD news for stationarity. Read it backward compared with ADF.",
    ])

    add_callout(
        "Why we use all three",
        "ADF/PP and KPSS have opposite nulls. If ADF rejects (p small) AND "
        "KPSS fails to reject (p large), both say the same thing: the "
        "series is stationary. If they disagree, we read it as ambiguous "
        "and look at more evidence."
    )

    h3("Zivot-Andrews test")
    bullets([
        "What it checks: is there a unit root when the data might have ONE "
        "structural break at an unknown date?",
        "H0: unit root, possibly with a break.",
        "Rule: small p = reject = stationary with a break.",
        "Memory hook: ZA is ADF ‘with a crack line’. It allows one sudden "
        "jump without being fooled by it.",
    ])

    add_para(
        "In our paper: all the price series in levels have unit roots. "
        "After taking log differences they become stationary by ADF, PP, "
        "and KPSS, with a small KPSS caveat for headline WPI inflation. "
        "That caveat is handled by the Bai-Perron break test, not by "
        "differencing again."
    )

    # =======================================================================
    # STRUCTURAL BREAK TESTS
    # =======================================================================
    h2("8.3 Structural break tests: did the relationship shift in time?")

    h3("Bai-Perron (2003) test")
    bullets([
        "What it checks: are there one or more unknown break points where "
        "the relationship shifts?",
        "H0: no break, parameters are constant.",
        "Rule: small p = reject = at least one break exists.",
        "Memory hook: Bai-Perron is a ‘break detective’. It scans the whole "
        "sample and says ‘a shift happened around month X’.",
    ])

    add_para(
        "In our paper: where Bai-Perron detects breaks in headline WPI "
        "inflation, we handle them with the institutional pre/post-2010 "
        "split rather than adding dummies for every mathematical break. "
        "This keeps the analysis anchored to fuel-pricing policy."
    )

    # =======================================================================
    # RESIDUAL DIAGNOSTICS (the model gate)
    # =======================================================================
    h2("8.4 Residual diagnostics: is the fitted model well-behaved?")
    add_para(
        "After fitting the ADL, the residuals ε̂_t should look like "
        "clean noise. These tests check whether they do. Anything unusual "
        "in the residuals means the model is missing something."
    )

    h3("Breusch-Godfrey test (BG), the leftover-pattern test")
    bullets([
        "What it checks: do the residuals still have autocorrelation? In "
        "other words, is last month's error predicting this month's error?",
        "H0: no serial correlation in residuals.",
        "Rule: LARGE p is what we want. Large p = fail to reject = residuals "
        "are clean. Small p = bad, residuals still have pattern.",
        "Memory hook: BG scans the residuals for leftover patterns. Pass "
        "it like a quality-control inspection at the end of a factory line.",
    ])
    add_para(
        "We run BG at 12 lags because the data are monthly and annual "
        "seasonality could sneak in. Our claim-bearing models all pass BG "
        "(p > 0.05)."
    )

    h3("Breusch-Pagan test (BP), the variance-stability test")
    bullets([
        "What it checks: is the residual variance constant, or does it "
        "grow and shrink with the size of the right-hand-side variables?",
        "H0: constant variance (homoskedasticity).",
        "Rule: large p = residuals have stable variance = happy.",
        "Memory hook: BP listens to whether the noise is ‘loud "
        "sometimes, quiet sometimes’. If yes, the standard errors need "
        "fixing. We use HAC errors either way, so BP is a health check, "
        "not a gate.",
    ])

    h3("Jarque-Bera test (JB), the normality test")
    bullets([
        "What it checks: do the residuals follow a bell-shaped (normal) "
        "distribution?",
        "H0: residuals are normally distributed.",
        "Rule: large p = residuals look normal.",
        "Memory hook: JB is a ‘bell-shape score’. Failing it does not kill "
        "OLS (we still get consistent estimates), but very large fails "
        "flag outliers worth investigating.",
    ])

    h3("Ramsey RESET test (HAC-RESET), the missing-shape test")
    bullets([
        "What it checks: did we use the wrong functional form? For "
        "example, is there a nonlinear effect the linear ADL missed?",
        "How it works, intuitively: RESET takes our fitted ŷ, squares and "
        "cubes it, and sticks ŷ^{2} and ŷ^{3} into the regression as "
        "extra variables. If those extra terms are jointly significant, "
        "then our original straight-line model was missing curvature.",
        "H0: the functional form is correct.",
        "Rule: large p = ‘straight line is fine, no missing curvature’. "
        "Small p = ‘the model is missing nonlinearity’ = bad.",
        "Memory hook: RESET adds two ‘bendy’ regressors to the equation. "
        "If they matter, the original shape was wrong.",
    ])
    add_para(
        "We run RESET under the HAC covariance so it stays valid with "
        "autocorrelated, heteroskedastic residuals. That is what ‘HAC-"
        "RESET’ means."
    )

    h3("Recursive CUSUM test, the stability test")
    bullets([
        "What it checks: do the coefficients stay roughly constant as we "
        "add data one month at a time, or do they drift?",
        "How it works, intuitively: fit the model on the first few months. "
        "Predict the next month. Record the forecast error. Do it again "
        "with one more month of data. Plot the cumulative sum of these "
        "errors.",
        "H0: coefficients are stable over time.",
        "Rule: a large p (and a CUSUM line that stays inside its 5 per "
        "cent confidence band) = stable coefficients. A small p = "
        "instability somewhere.",
        "Memory hook: CUSUM is a ‘running tab’ of forecast errors. If the "
        "tab ever runs too far from zero, the model's coefficients are "
        "shifting under our feet.",
    ])

    h3("OLS CUSUM test")
    bullets([
        "Same idea as recursive CUSUM but built from the residuals of a "
        "single full-sample OLS fit rather than a growing-window fit.",
        "Useful as a cross-check. We report recursive CUSUM as the main "
        "gate test because it is more sensitive to drift.",
    ])

    # =======================================================================
    # The mandatory model gate
    # =======================================================================
    h2("8.5 The mandatory model gate, in one mental picture")
    add_para(
        "Before a model can carry a main claim in our paper it must pass "
        "three doors in a row. Think of it as passport control."
    )
    bullets([
        "Door 1: BG12 (Breusch-Godfrey at 12 lags). ‘Are the residuals "
        "free of leftover patterns?’",
        "Door 2: HAC-RESET. ‘Is the functional form right?’",
        "Door 3: Recursive CUSUM. ‘Are the coefficients stable over time?’",
    ])
    add_para(
        "Any model that fails even one door is downgraded to ‘context’ or "
        "dropped from the main text. No exceptions. This rule is set "
        "BEFORE looking at the coefficients, so we cannot cherry-pick."
    )

    add_table(
        headers=["Specification", "BG12", "HAC-RESET", "Rec-CUSUM", "Result"],
        rows=[
            ["Headline WPI (1983-2026)", "Pass", "Pass", "Pass",
             "Main WPI claim"],
            ["WPI Fuel and Power, pooled full sample", "Pass", "FAIL",
             "Pass", "Context only"],
            ["WPI Fuel and Power, post-2010, excluding Apr-Sep 2020",
             "Pass", "Pass", "Pass", "Preferred wholesale fuel claim"],
            ["Headline CPI M1 (2004-2024)", "Pass", "Pass", "Pass",
             "Main CPI endpoint"],
            ["PPAC retail petrol (2004-2024)", "Pass", "Pass", "Pass",
             "Mechanism accepted"],
            ["CPI M2, M3 alternatives", "Varies", "FAIL", "Varies",
             "Not claim-bearing"],
        ],
        caption="Table 8.1. Gate result for every specification in the paper.",
        col_widths=[2.6, 0.6, 0.9, 0.9, 1.5],
        font_size=9,
    )

    # =======================================================================
    # The WPI Fuel and Power RESET fix — very important
    # =======================================================================
    h2("8.6 How we made WPI Fuel and Power pass HAC-RESET")
    add_para(
        "This is the most-asked methodology question the teacher can drop "
        "on you. Read it slowly once and you will answer it in one breath."
    )

    h3("What failed, and why")
    add_para(
        "The first version of the WPI Fuel and Power model used the full "
        "sample from May 1995 to March 2026. On that sample, the model "
        "failed the HAC-RESET test. ‘Fail HAC-RESET’ means: adding "
        "ŷ-squared and ŷ-cubed into the equation made a jointly "
        "significant improvement, so the straight-line ADL was missing "
        "something nonlinear."
    )
    add_para(
        "Two economic reasons were likely causes:"
    )
    bullets([
        "Regime mixing. The full sample lumps the pre-2010 administered "
        "pricing period together with the post-2010 market-linked period. "
        "Before 2010 the government set retail prices for long stretches, "
        "so oil shocks sometimes did not transmit at all. After 2010 oil "
        "marketing companies revised prices frequently, so transmission is "
        "much faster. Forcing one set of ADL coefficients to fit both "
        "behaviours creates a kink RESET can detect.",
        "COVID outliers. April through September 2020 saw unprecedented "
        "moves. Brent went negative in May 2020 on the WTI benchmark and "
        "very low on Brent; Indian demand collapsed; pricing rules were "
        "effectively suspended. Leaving those months in the sample forces "
        "the model to accommodate extreme points that the rest of the "
        "sample does not look like, which again shows up as functional-"
        "form misspecification.",
    ])

    h3("What we changed")
    bullets([
        "Change 1: shorten the sample to April 2010 onward so the pre-2010 "
        "administered regime no longer contaminates the estimates.",
        "Change 2: drop the six months from April 2020 to September 2020, "
        "which removes the most extreme COVID outliers while keeping the "
        "rest of the post-2010 sample intact.",
        "Change 3: keep the exchange-rate controls and the month fixed "
        "effects unchanged. Lag orders stay ADL(12, 6), so we are not "
        "tinkering with the lag structure to force a pass.",
    ])
    add_code_block(
        "# Pseudocode for the specification change\n"
        "sample_full    <- dates from 1995-05 to 2026-03        # failed RESET\n"
        "sample_preferred <- dates from 2010-04 to 2026-03\n"
        "               minus months in { 2020-04 .. 2020-09 }  # COVID dropped\n"
        "\n"
        "fit the same ADL(12, 6) on sample_preferred:\n"
        "    dln_wpi_fp_t = α + Σ φ_i dln_wpi_fp_{t-i}\n"
        "                      + Σ β+_j dln_oil_inr_pos_{t-j}\n"
        "                      + Σ β-_j dln_oil_inr_neg_{t-j}\n"
        "                      + exchange-rate controls\n"
        "                      + month fixed effects\n"
        "                      + ε_t\n"
    )

    h3("What happened after the change")
    add_table(
        headers=["Check", "Full sample (failed)", "Preferred sample (passes)"],
        rows=[
            ["Observations N", "371", "186"],
            ["CPT+ estimate", "0.2866 (p<0.001)", "0.5205 (p<0.001)"],
            ["CPT− estimate", "0.2677 (p<0.001)", "0.4195 (p<0.001)"],
            ["Asymmetry p-value", "0.7832", "0.1642"],
            ["BG12 (serial correlation)", "Pass", "Pass (p = 0.0746)"],
            ["HAC-RESET (functional form)", "FAIL", "Pass (p = 0.5443)"],
            ["Recursive CUSUM (stability)", "Pass", "Pass (p = 0.6999)"],
        ],
        caption="Table 8.2. Before and after the WPI Fuel and Power fix.",
        col_widths=[2.2, 2.2, 2.2],
        font_size=10,
        note="The preferred model has a smaller N but cleaner diagnostics. "
             "The pooled full-sample model is kept in the paper only as "
             "context so the reader can see why the change was needed."
    )

    add_callout(
        "One-sentence answer to the teacher",
        "‘We restricted the WPI Fuel and Power sample to April 2010 onward "
        "and dropped April to September 2020 because regime mixing and "
        "COVID outliers were creating a functional-form misspecification. "
        "After the restriction, HAC-RESET has p = 0.5443, BG has p = "
        "0.0746, and recursive CUSUM has p = 0.6999, so the model now "
        "passes the mandatory gate cleanly.’"
    )

    # =======================================================================
    # Coefficient-level tests (Wald, symmetry)
    # =======================================================================
    h2("8.7 Coefficient-level tests: are the numbers we care about real?")

    h3("Wald test on CPT+ and CPT−")
    bullets([
        "What it checks: is the cumulative pass-through statistically "
        "different from zero? And is CPT+ equal to CPT−?",
        "H0 for significance: CPT+ = 0 (or CPT− = 0).",
        "H0 for symmetry: CPT+ = CPT−.",
        "Rule: small p for significance = real effect. Small p for "
        "symmetry = positive and negative shocks pass through differently.",
        "Memory hook: a Wald test is like a ruler that measures how many "
        "standard errors away from the null our estimate is. Far away = "
        "small p.",
    ])

    h3("Attenuation Wald test (the headline test of the paper)")
    bullets([
        "What it checks: is Stage 1 pass-through (Brent to retail petrol) "
        "equal to Stage 3 pass-through (rupee oil to headline CPI)?",
        "H0: Stage 1 CPT+ = Stage 3 CPT+.",
        "Result: F = 14.3499, p = 0.0002. Reject.",
        "Meaning: the fall in pass-through from retail petrol to headline "
        "CPI is too big to be random. Attenuation is statistically real.",
    ])

    # =======================================================================
    # Bootstrap and Granger
    # =======================================================================
    h2("8.8 Bootstrap symmetry test, in plain language")
    bullets([
        "What it checks: the same H0 as the Wald symmetry test (CPT+ = "
        "CPT−), but without relying on large-sample theory for the "
        "p-value.",
        "How it works: resample the residuals (in blocks, circularly) "
        "4,999 times under the imposed null, re-compute the statistic "
        "each time, and count how often a fake statistic is as extreme as "
        "the real one. That fraction IS the bootstrap p-value.",
        "Why we do it: monthly samples are not infinite, so asymptotic "
        "p-values can be a little off. The bootstrap gives a second "
        "opinion that does not depend on the asymptotic distribution.",
        "Memory hook: bootstrap = ‘shuffle the data under the null, see "
        "how lucky we would need to be to get our real estimate’.",
    ])

    h2("8.9 Granger causality test, in plain language")
    bullets([
        "What it checks: if we already know past values of Y, does adding "
        "past values of X help us forecast Y better?",
        "H0: past values of X do not help forecast Y (X does not "
        "Granger-cause Y).",
        "Rule: small p = X does help = X Granger-causes Y.",
        "Careful: Granger causality is about prediction, NOT real "
        "causation. Two variables can Granger-cause each other and still "
        "be driven by a third cause.",
        "Memory hook: Granger tests ‘does knowing X's past make forecasts "
        "of Y sharper?’.",
    ])

    # =======================================================================
    # Other robustness tests
    # =======================================================================
    h2("8.10 Other robustness tests you should know by name")

    h3("Lag-sensitivity check")
    bullets([
        "What we do: re-estimate the model with shock lag q set to 4, 5, "
        "6, 7, 8 one by one.",
        "Why: to make sure the main results are not a single accident of "
        "choosing q = 6.",
        "In our paper: the ranking in the main table does not change when "
        "q varies in that range.",
    ])

    h3("Winsorising at 1 and 99 per cent")
    bullets([
        "What we do: cap extreme values in the dependent variable at the "
        "first and ninety-ninth percentiles. A point above the 99th "
        "percentile is pulled down to the 99th percentile value; below the "
        "1st is pulled up.",
        "Why: extreme shocks like COVID can distort one or two coefficients "
        "out of proportion. Capping reduces their leverage without "
        "dropping observations.",
        "In our paper: winsorised estimates give the same qualitative "
        "headline CPI conclusion.",
    ])

    h3("COVID-exclusion check")
    bullets([
        "What we do: re-estimate with the COVID months removed from the "
        "sample.",
        "Why: separate test of whether COVID is driving the main "
        "estimates.",
        "In our paper: excluding COVID does not overturn the weak "
        "headline CPI result.",
    ])

    h3("Rolling-window estimation")
    bullets([
        "What we do: fit the model on a moving window (for example, 120 "
        "months at a time) and slide the window forward month by month.",
        "Why: to see whether the coefficient moves smoothly or breaks "
        "sharply over time.",
        "In our paper: the headline CPI cumulative pass-through hovers "
        "near the central estimate without crossing into significance at "
        "conventional levels.",
    ])

    h3("Brent plus exchange-rate decomposition")
    bullets([
        "What we do: instead of using the rupee oil shock as one "
        "variable, use Brent and the exchange-rate change as two "
        "separate right-hand-side variables.",
        "Why: to check that the main conclusion does not hinge on how the "
        "shock is bundled.",
        "In our paper: decomposed estimates for headline WPI are very "
        "close to the rupee-shock estimates. Conclusion does not depend "
        "on bundling.",
    ])

    # =======================================================================
    # One-page memory card
    # =======================================================================
    h2("8.11 One-page memory card: every test in one table")
    add_table(
        headers=["Test", "H0 (null)", "Small p means"],
        rows=[
            ["ADF", "Unit root", "Stationary (good)"],
            ["PP", "Unit root", "Stationary (good)"],
            ["KPSS", "Stationary", "Unit root (bad for levels)"],
            ["Zivot-Andrews", "Unit root (with break allowed)",
             "Stationary with a break"],
            ["Bai-Perron", "No structural break", "Break detected"],
            ["Breusch-Godfrey (BG)", "No residual autocorrelation",
             "Leftover pattern in residuals (bad)"],
            ["Breusch-Pagan (BP)", "Homoskedastic residuals",
             "Residual variance unstable"],
            ["Jarque-Bera (JB)", "Residuals are normal", "Non-normal residuals"],
            ["HAC-RESET", "Functional form is correct",
             "Missing nonlinearity (bad)"],
            ["Recursive CUSUM", "Coefficients are stable",
             "Parameter drift (bad)"],
            ["Wald (significance)", "Coefficient = 0", "Coefficient is real"],
            ["Wald (symmetry)", "CPT+ = CPT−", "Asymmetric pass-through"],
            ["Wald (attenuation)", "Stage 1 CPT+ = Stage 3 CPT+",
             "Attenuation is real"],
            ["Granger", "X does not help forecast Y",
             "X Granger-causes Y"],
            ["Bootstrap symmetry", "CPT+ = CPT−",
             "Asymmetric pass-through (robust check)"],
        ],
        caption="Table 8.3. Every test in the paper, its null, and how to "
                "read a small p-value.",
        col_widths=[2.0, 2.3, 2.5],
        font_size=9.5,
    )

    add_callout(
        "Five-second revision before the viva",
        "ADF/PP reject = stationary, KPSS reject = bad. BG/RESET/CUSUM "
        "reject = bad. Wald reject = real effect. Granger reject = "
        "predictive link. For WPI Fuel and Power we shortened to post-2010 "
        "and dropped Apr-Sep 2020 so HAC-RESET passes."
    )

    page_break()
