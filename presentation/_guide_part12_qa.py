"""Part 12: Viva question bank with short model answers."""


def build(h):
    add_para = h['add_para']
    add_para_math = h['add_para_math']
    h1 = h['h1']; h2 = h['h2']; h3 = h['h3']
    bullets = h['bullets']
    page_break = h['page_break']
    add_callout = h['add_callout']
    doc = h['doc']
    emit_runs = h['emit_runs']
    from docx.shared import Pt, Inches

    def qa(q, a):
        qp = doc.add_paragraph()
        qp.paragraph_format.first_line_indent = Inches(0)
        qp.paragraph_format.space_before = Pt(6)
        qp.paragraph_format.space_after = Pt(2)
        emit_runs(qp, "Q. " + q, font_size=11.5, bold=True)
        ap = doc.add_paragraph()
        ap.paragraph_format.first_line_indent = Inches(0)
        ap.paragraph_format.left_indent = Inches(0.2)
        ap.paragraph_format.space_after = Pt(6)
        emit_runs(ap, "A. " + a, font_size=11.5)

    h1("Part 12. Viva question bank with short model answers")

    h2("12.1 Setting-the-scene questions")

    qa(
        "What is your main research question?",
        "How global oil-price shocks transmit across India's wholesale, "
        "retail fuel, fuel-sensitive consumer, and headline consumer "
        "price layers, and where that pass-through weakens."
    )
    qa(
        "What is your main finding in one line?",
        "Oil-price shocks pass through strongly at fuel-related layers "
        "and weakly at the headline CPI layer, and the difference is "
        "statistically significant."
    )
    qa(
        "What is the contribution of the study?",
        "Treating oil pass-through as a layered transmission problem "
        "across five price indices, rather than as a single elasticity "
        "between Brent and headline CPI, and backing that framing with a "
        "formal Wald test on the common-sample consumer-price chain."
    )
    qa(
        "What is novel compared with earlier India studies?",
        "Earlier work usually picks one index or one equation. We put "
        "five related equations into one attenuation map, keep each "
        "layer's sample and shock variable visible, and show that the "
        "fall in pass-through from retail petrol to headline CPI is "
        "statistically real."
    )
    qa(
        "Why does this matter for policy?",
        "The Reserve Bank of India targets headline CPI for inflation. "
        "If headline CPI is weakly tied to oil, a policy reader looking "
        "only at headline might miss upstream fuel-side pressure. So "
        "they should also watch fuel-sensitive layers."
    )

    h2("12.2 Data questions")

    qa(
        "Where does your Brent crude data come from?",
        "The World Bank Commodity Price Data, commonly called the Pink "
        "Sheet. Monthly frequency. Cross-checked against FRED POILBREUSDM."
    )
    qa(
        "Where does the INR/USD exchange rate come from?",
        "FRED series EXINUS for the CPI pipeline, and EXINUS_latest for "
        "the WPI pipeline. FRED is Federal Reserve Economic Data at the "
        "Federal Reserve Bank of St. Louis."
    )
    qa(
        "Who publishes the WPI?",
        "The Office of the Economic Adviser (OEA), inside the Department "
        "for Promotion of Industry and Internal Trade (DPIIT), Ministry "
        "of Commerce and Industry."
    )
    qa(
        "Who publishes the CPI?",
        "The Ministry of Statistics and Programme Implementation, MoSPI."
    )
    qa(
        "Why PPAC retail petrol for Delhi and not national?",
        "PPAC (Petroleum Planning and Analysis Cell, Ministry of "
        "Petroleum and Natural Gas) publishes consistent monthly Delhi "
        "prices back to 2004. It is used as a retail-fuel channel proxy. "
        "Other metros give similar qualitative patterns."
    )
    qa(
        "What is the rupee oil price? Why construct it?",
        "It is Brent in dollars multiplied by the INR/USD rate. We use "
        "it because Indian refiners and the broader economy pay for oil "
        "in rupees. A Brent rise with a rupee appreciation at the same "
        "time creates a different domestic cost pressure than a Brent "
        "rise alone."
    )
    qa(
        "Why do your samples differ across layers?",
        "Each official series becomes available at different dates. "
        "Headline WPI goes back to 1983-05, WPI Fuel and Power to "
        "1995-05, retail petrol to 2004-08, and CPI Fuel and Light only "
        "to 2011-05. We use the longest consistent window for each layer."
    )
    qa(
        "How do you handle the fact that samples differ?",
        "We run a common-sample consumer-chain check where all three "
        "stages are estimated on overlapping months, with small observation "
        "differences from lag construction. The qualitative ranking holds. "
        "The Wald test for "
        "attenuation uses this common-sample set-up."
    )

    h2("12.3 Variable questions")

    qa(
        "Why log differences and not levels?",
        "Price levels have unit roots and trend together. Regressing "
        "them on each other produces spurious results. Log differences "
        "are stationary and also read naturally as percentage changes."
    )
    qa(
        "Why multiply the log difference by 100?",
        "So that each coefficient reads as a percentage response per "
        "one per cent shock. Without the 100 the economics is the same, "
        "just in decimals."
    )
    qa(
        "What is the positive/negative shock split?",
        "For every shock we build a non-negative ‘twin’ that equals "
        "max(Δx, 0) and a non-positive ‘twin’ that equals min(Δx, 0). "
        "They sum to the original shock. This lets us test whether "
        "positive and negative shocks pass through at the same size."
    )
    qa(
        "What is CPT+ and CPT−?",
        "CPT+ is the sum of coefficients on the positive-shock lags, "
        "adding up the total cumulative response to a one per cent "
        "positive shock over the ADL lag window. CPT− is the same sum "
        "for negative shocks."
    )

    h2("12.4 Methodology questions")

    qa(
        "Why ADL?",
        "ADL models allow the dependent inflation to depend on its own "
        "recent past (autoregressive) and on current and recent shocks "
        "(distributed lag). That matches how price data behave. We use "
        "the asymmetric version to test rockets and feathers."
    )
    qa(
        "Why not NARDL or an error-correction model?",
        "Our question is about monthly transmission, not about long-run "
        "equilibrium relationships. NARDL bounds and error-correction "
        "tools would be overkill and would invite long-run claims we do "
        "not need."
    )
    qa(
        "What does ADL(3,3) mean? How did you choose 3 and 3?",
        "Three lags of the dependent variable, three lags of the shock. "
        "The dependent-lag order is picked by AIC over p = 1 to 4 for "
        "the CPI and retail petrol pipelines. The shock-lag order "
        "balances fast retail and consumer dynamics against the "
        "informational content of older lags."
    )
    qa(
        "Why ADL(12,6) for WPI?",
        "Twelve own-lags capture the annual cycle in wholesale inflation "
        "even after month dummies. Six shock-lags let the oil response "
        "stretch half a year, which matches the way wholesale prices "
        "move after input costs change."
    )
    qa(
        "How are the coefficients estimated? Is it OLS or something fancier?",
        "Plain OLS. We estimate every ADL equation by minimising the "
        "sum of squared residuals. The only non-standard step is the "
        "standard errors, which are Newey-West HAC to fix autocorrelation "
        "and heteroskedasticity."
    )
    qa(
        "What do α, β, γ, φ, μ, ε mean in your equation?",
        "α is the intercept. φ_i are coefficients on own-lags of the "
        "dependent variable. β^+_j and β^-_j are coefficients on "
        "positive and negative shock lags. γ is the vector of "
        "coefficients on controls. μ_m are month-of-year dummies. ε_t "
        "is the residual, everything the model did not explain."
    )
    qa(
        "Are there specific numerical values of these coefficients?",
        "Yes; the full coefficient tables are in the model output "
        "folders. In the main text we report the cumulative "
        "pass-through CPT+ and CPT− because those are the quantities "
        "policy readers care about."
    )

    h2("12.5 Inference questions")

    qa(
        "What are Newey-West HAC standard errors?",
        "Standard errors that remain valid when residuals are "
        "heteroskedastic (different variance over time) and "
        "autocorrelated (residuals correlated with their own recent "
        "past). Without HAC, p-values would be too small and we would "
        "over-reject the null."
    )
    qa(
        "Why 4,999 bootstrap replications?",
        "Odd numbers avoid ties when computing percentile p-values. "
        "4,999 is enough for stable estimates. Using 9,999 would move "
        "the p-values by a small amount at most."
    )
    qa(
        "What does a Wald test do?",
        "It tests linear restrictions on coefficients. Our CPT+ = 0 "
        "and CPT+ = CPT− tests are Wald tests. Under HAC inference, a "
        "large Wald statistic gives a small p-value and rejects the "
        "null."
    )
    qa(
        "How do Granger tests fit into the paper?",
        "They are predictive-precedence tests, not causality tests. "
        "They show that past oil movements improve forecasts of "
        "wholesale and retail fuel inflation. We report them as "
        "supporting evidence, not as structural causal identification."
    )

    h2("12.6 Diagnostic questions")

    qa(
        "What is the mandatory model gate?",
        "Three tests every claim-bearing model must pass: "
        "Breusch-Godfrey at 12 lags for serial correlation, HAC-RESET "
        "for functional form, and recursive CUSUM for parameter "
        "stability."
    )
    qa(
        "Why did the full-sample WPI Fuel and Power model fail?",
        "It fails HAC-RESET, meaning the functional form is "
        "misspecified. The most likely reason is regime mixing: it "
        "combines the pre-2010 administered period with the post-2010 "
        "market-linked period and the COVID outliers. Restricting to "
        "post-2010 and dropping April-September 2020 fixes this."
    )
    qa(
        "What do ADF, PP, KPSS do?",
        "They test for unit roots. ADF and PP have H_0: unit root. "
        "KPSS reverses it with H_0: stationarity. Using all three "
        "together gives a robust verdict. All our differenced series "
        "pass as stationary."
    )
    qa(
        "What about the KPSS caveat on WPI inflation?",
        "KPSS rejects stationarity for WPI inflation in a couple of "
        "subsamples. We read this alongside the Bai-Perron break test "
        "results and treat it as a break-related caveat handled by the "
        "institutional pre/post-2010 split, not a reason to re-difference."
    )

    h2("12.7 Results questions")

    qa(
        "Why is CPT+ so much larger in WPI Fuel and Power than in headline WPI?",
        "WPI Fuel and Power is close to the fuel channel. Its basket "
        "contains petrol, diesel, LPG, coal-adjacent items, and "
        "electricity. Headline WPI averages this with manufactured "
        "goods and food, so the oil signal is diluted."
    )
    qa(
        "Why is headline CPI pass-through weak?",
        "The CPI basket is dominated by food, services, housing, "
        "health, and education. Fuel and Light is just one group. So "
        "even a big shock in fuel prices becomes a small number by the "
        "time you sum to headline CPI."
    )
    qa(
        "Does headline CPI pass-through equal zero?",
        "No. It is weak and statistically insignificant at conventional "
        "levels in our sample. We never describe it as zero. We "
        "describe it as weak and not significant."
    )
    qa(
        "What does the Wald F = 14.35 mean in words?",
        "It is the test statistic for the null that Stage 1 CPT+ "
        "equals Stage 3 CPT+ in the common-sample consumer-price "
        "chain. With p = 0.0002, we reject the null. The attenuation "
        "from retail petrol to headline CPI is statistically real."
    )
    qa(
        "Why is asymmetry not the headline finding?",
        "Because HAC and bootstrap symmetry tests fail to reject "
        "symmetry in headline WPI, WPI Fuel and Power, CPI Fuel and "
        "Light, and headline CPI. Retail petrol is the only layer with "
        "even marginal evidence, at p = 0.0999."
    )
    qa(
        "Why did you prefer the post-2010 Fuel and Power model?",
        "It is the only Fuel and Power specification that passes the "
        "mandatory diagnostic gate cleanly. The full-sample pooled "
        "model fails HAC-RESET because it mixes regimes."
    )

    h2("12.8 Broader and trickier questions")

    qa(
        "Is your work causal?",
        "No. It is reduced-form projection. Granger tests show "
        "predictive precedence from oil to wholesale and retail fuel, "
        "but we do not claim structural identification."
    )
    qa(
        "Could the pre/post-2010 split be confounded?",
        "Yes. The post-2010 window also contains the new CPI series in "
        "2011, flexible inflation targeting in 2016, GST in 2017, and "
        "several fuel-tax episodes. We call the split institutional "
        "evidence, not causal."
    )
    qa(
        "Why Delhi for retail petrol?",
        "PPAC has the longest consistent monthly Delhi series. Other "
        "metros behave similarly. We use Delhi as a retail-fuel channel "
        "proxy."
    )
    qa(
        "Could endogeneity be a problem? Does India affect global Brent?",
        "India is a large buyer but not a price-setter for Brent. "
        "Brent is driven by OPEC+ decisions, US shale, global demand, "
        "and geopolitics, all exogenous from India's perspective. The "
        "reverse-direction Granger tests also fail to reject the null "
        "that wholesale Indian prices do not predict Brent. So "
        "endogeneity concerns are small."
    )
    qa(
        "What if oil's effect operates through expectations rather than cost?",
        "That is possible and is one of the reasons headline CPI is "
        "not the layer where oil transmission is most visible. "
        "Expectations feed into the whole basket. Our layered evidence "
        "is consistent with direct cost transmission being stronger at "
        "fuel layers; expectation channels would be a structural-shock "
        "extension."
    )
    qa(
        "Would a structural VAR improve the paper?",
        "It would allow identified oil-supply, demand, and exchange-"
        "rate shocks, and shock-specific impulse responses. That is a "
        "legitimate extension. We chose ADL because the question is "
        "short-run pass-through by layer, and ADL keeps the "
        "interpretation clean."
    )
    qa(
        "How would your results change if CPI were defined differently?",
        "We use the standard MoSPI headline CPI and its Fuel and Light "
        "component. Alternative definitions (core CPI, rural-only, "
        "urban-only) would move the headline number by small amounts. "
        "The attenuation pattern is robust because it depends on basket "
        "breadth, not on the exact CPI variant."
    )

    add_callout(
        "Exam tip",
        "When in doubt, bring the answer back to layered attenuation. "
        "Whether the teacher asks about method, data, or a specific "
        "number, the story is: oil is strong in fuel layers, weak in "
        "headline CPI, and the Wald test formally confirms the fall."
    )

    page_break()
