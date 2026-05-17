"""Part 7: Inference. HAC, p-values, Wald, bootstrap, Granger."""


def build(h):
    add_para = h['add_para']
    add_para_math = h['add_para_math']
    h1 = h['h1']; h2 = h['h2']; h3 = h['h3']
    bullets = h['bullets']
    page_break = h['page_break']
    add_callout = h['add_callout']
    add_equation = h['add_equation']
    add_code_block = h['add_code_block']
    mr = h['mr']; msub = h['msub']; msup = h['msup']; mfenced = h['mfenced']

    h1("Part 7. Inference: p-values, HAC, Wald, bootstrap, Granger")

    h2("7.1 What is a p-value in one line")
    add_para(
        "A p-value is the probability of seeing a coefficient at least as "
        "extreme as the one we estimated, if the true coefficient were zero. "
        "A small p (conventionally below 0.05) tells us the estimate is "
        "unlikely to be a random accident, so we say the coefficient is "
        "‘statistically significant’ at that level."
    )
    add_callout(
        "Simple translation",
        "Coefficient = 0.30 and p = 0.002 means: ‘The data say the effect is "
        "about 0.30, and there is only a 0.2 per cent chance we would see "
        "something this extreme if the real effect were zero. So we believe "
        "the effect is real.’"
    )

    h2("7.2 The standard error and why monthly data need HAC")
    add_para(
        "Every coefficient has a standard error, which measures how noisy "
        "that coefficient estimate is. The p-value is the coefficient "
        "divided by its standard error, compared to a reference "
        "distribution. If the standard error is wrong, the p-value is "
        "wrong."
    )
    add_para(
        "Classical OLS standard errors assume residuals are independent and "
        "have the same variance (‘no heteroskedasticity, no autocorrelation’). "
        "Monthly inflation data break both assumptions. Errors are often "
        "correlated across months, and their variance changes with regimes "
        "like COVID. So we use Newey-West HAC standard errors instead."
    )
    bullets([
        "HAC = Heteroskedasticity and Autocorrelation Consistent.",
        "Named after Newey and West (1987), who derived them.",
        "They adjust the covariance matrix of the coefficients so the p-values "
        "remain valid even when residuals are heteroskedastic and "
        "autocorrelated.",
        "The adjustment uses a kernel (we use the Bartlett kernel) and a "
        "bandwidth; we use a data-dependent bandwidth with floor(0.75 × "
        "N^{1/3}) as the rule for the main wholesale models.",
    ])

    h2("7.3 The three hypotheses we test on cumulative pass-through")
    add_para_math(
        "For every layer we report three tests. First, H_{0}: CPT^{+} = 0. "
        "Does the positive-shock response sum to zero, or is there a real "
        "positive response? Second, H_{0}: CPT^{−} = 0. Same question for "
        "negative shocks. Third, H_{0}: CPT^{+} = CPT^{−}. This is the "
        "symmetry test. Can we treat positive and negative shocks as "
        "equivalent in size?"
    )
    add_para(
        "All three tests are linear restrictions on combinations of the β "
        "coefficients. They are standard Wald tests. A Wald test checks "
        "whether the coefficients estimated from the data are far from the "
        "values in the null hypothesis, in a way that is weighted by the "
        "HAC covariance matrix."
    )

    h2("7.4 How a Wald test works, intuitively")
    add_para(
        "Imagine we estimated CPT^{+} = 0.35 with a standard error of "
        "0.08. The null hypothesis CPT^{+} = 0 says the true CPT^{+} is "
        "zero. Our estimate is 0.35 / 0.08 ≈ 4.4 standard errors away from "
        "zero. A test statistic that big gives a very small p-value, so we "
        "reject the null and conclude CPT^{+} is not zero."
    )
    add_para(
        "Similarly, the symmetry test looks at (CPT^{+} − CPT^{−}) and its "
        "standard error under the HAC covariance. If the difference is "
        "small relative to its standard error, we do not reject symmetry."
    )

    h2("7.5 The bootstrap symmetry check")
    add_para(
        "The Wald test relies on large-sample theory. In finite samples the "
        "p-value can be slightly off. A bootstrap re-computes the p-value "
        "without relying on asymptotic theory. We use a restricted-residual "
        "circular block bootstrap with 4,999 replications."
    )
    bullets([
        "‘Restricted-residual’ means we enforce the null (CPT^{+} = "
        "CPT^{−}) when we resample, so that the distribution we build is "
        "the one under the null.",
        "‘Circular block’ means we resample residuals in blocks to preserve "
        "the within-block autocorrelation that monthly data exhibit. The "
        "‘circular’ part wraps around the end of the sample so every point "
        "has the same chance of being included.",
        "We do this 4,999 times, each time computing a fake test statistic. "
        "The bootstrap p-value is the fraction of fake statistics at least "
        "as extreme as the one we saw in the real data.",
    ])
    add_callout(
        "Why 4,999",
        "Odd numbers avoid ambiguity when computing the fraction. 4,999 is "
        "a conventional, stable choice; the results change very little if "
        "you use 9,999 instead."
    )

    h2("7.6 Granger causality: predictive precedence, not real causality")
    add_para(
        "A Granger test asks: if we already know current and past values of "
        "x and y, does adding past values of oil improve our forecast of y? "
        "If yes, oil ‘Granger-causes’ y. That is a predictive statement, not "
        "a structural causal claim. Oil can Granger-cause CPI without being "
        "the sole cause of CPI movements."
    )
    add_para(
        "We report these tests alongside the ADL results to check whether "
        "the direction of predictive information is consistent with our "
        "layered reading. For example, rupee oil Granger-causes headline "
        "WPI and WPI Fuel and Power, while the reverse directions do not "
        "hold. This matches the idea that oil leads wholesale, not the "
        "other way around."
    )
    add_callout(
        "What to say in the viva",
        "If asked ‘does oil cause inflation’, answer: ‘We test predictive "
        "precedence, not structural causality. Oil Granger-causes wholesale "
        "inflation in our sample, but we do not claim it is the only cause.’"
    )

    h2("7.7 Reading the main numbers in our paper")
    add_para_math(
        "When we report CPT^{+} = 0.3459 (p < 0.001) for retail petrol, we "
        "mean: our point estimate of the cumulative response to a positive "
        "one per cent Brent shock, summed over three shock lags, is about "
        "0.35 per cent, and under the HAC standard errors the probability "
        "of seeing something that big under the null CPT^{+} = 0 is below "
        "0.001. That is very strong evidence that the positive cumulative "
        "pass-through is real."
    )
    add_para_math(
        "Asymmetry p = 0.0999 for retail petrol means: the HAC-based Wald "
        "test for H_{0}: CPT^{+} = CPT^{−} gives a p-value of about 0.10. "
        "This is borderline. We say it rejects symmetry only at the 10 per "
        "cent level and describe it as suggestive, not decisive."
    )

    page_break()
