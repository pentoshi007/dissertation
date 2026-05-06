"""Chapter content for aniket-dissertation.docx. Strict blueprint adherence."""
import os


def build(doc, add_para, chapter_heading, section_heading, page_break,
          add_figure, add_table, add_note, add_equation, add_para_math,
          mr, msub, msup, mfenced, mnary_sum, ROOT):

    ctx = dict(doc=doc, add_para=add_para, chapter_heading=chapter_heading,
               section_heading=section_heading, page_break=page_break,
               add_figure=add_figure, add_table=add_table, add_note=add_note,
               add_equation=add_equation, add_para_math=add_para_math,
               mr=mr, msub=msub, msup=msup, mfenced=mfenced,
               mnary_sum=mnary_sum, ROOT=ROOT)

    write_abstract(ctx)
    write_chapter1(ctx)
    write_chapter2(ctx)
    write_chapter3(ctx)
    write_chapter4(ctx)
    write_chapter5(ctx)
    write_chapter6(ctx)
    write_conclusion(ctx)
    write_references(ctx)


# ============================================================
# ABSTRACT
# ============================================================
def write_abstract(c):
    c['chapter_heading']("", "Abstract")
    c['add_para'](
        "This dissertation studies how global oil-price shocks pass through India's domestic price system. "
        "India imports most of its crude oil, and crude is priced in dollars, so movements in Brent and the "
        "INR/USD exchange rate form the external cost shock. Rather than estimating one "
        "oil-to-headline-CPI elasticity, the dissertation follows the shock across layers: headline "
        "WPI, WPI Fuel and Power, PPAC Delhi retail petrol, CPI Fuel and Light, and headline CPI. The models "
        "use monthly data and short-run asymmetric ADL specifications in log differences. Inference relies on "
        "Newey-West HAC standard errors, cumulative pass-through tests, bootstrap symmetry checks, and "
        "diagnostic checks. The results show layered attenuation. Retail petrol responds strongly "
        "to Brent shocks, while WPI Fuel and Power responds strongly to rupee oil shocks. CPI Fuel and Light "
        "records a smaller but statistically significant bridge response. Headline WPI pass-through is "
        "statistically significant but modest. Headline CPI pass-through is positive, weak, and not "
        "statistically significant at conventional levels. A common-sample attenuation test rejects equality "
        "between retail-petrol and headline-CPI positive pass-through. The evidence does not say that oil "
        "shocks are irrelevant for Indian inflation. It says their measurable effect is strongest "
        "near fuel prices and much weaker in the broad consumer index. Short-run asymmetry is secondary: it is "
        "marginal in retail petrol and unsupported in headline WPI, WPI Fuel and Power, and headline CPI."
    )
    c['page_break']()


# ============================================================
# CHAPTER 1
# ============================================================
def write_chapter1(c):
    c['chapter_heading']("Chapter 1", "Introduction")

    c['section_heading']("1.1 The puzzle in Indian inflation")
    c['add_para'](
        "India imports most of its crude oil. Because crude is invoiced in US dollars, the domestic cost shock "
        "from oil depends on both the Brent price and the rupee-dollar exchange rate. A rise in Brent and a "
        "depreciation of the rupee can amplify each other. A strong rupee can blunt a Brent rise. The rupee oil "
        "price therefore matters more for domestic inflation than Brent alone."
    )
    c['add_para'](
        "The puzzle starts from a simple observation. The same oil shock that visibly changes retail petrol "
        "prices at the pump can leave only a small mark on headline consumer inflation, the index that anchors "
        "monetary policy. This is not a contradiction. It is a sign that the shock weakens somewhere inside the "
        "price system. A rupee oil shock can reach prices directly through retail fuel and the fuel-sensitive "
        "sub-indices of WPI and CPI. It can also reach prices indirectly through transport, packaging, and "
        "industrial input costs. At the same time, taxes, margins, basket weights, and index construction "
        "absorb part of the shock at every stage. Treating oil pass-through as a single elasticity between Brent "
        "and headline CPI hides where this absorption happens."
    )
    c['add_para'](
        "WPI and CPI are also different by design. WPI is closer to producer-side and wholesale costs, with a "
        "non-trivial weight on fuel and power, mineral oils, and oil-intensive manufactured products. CPI is "
        "the household-facing index targeted by the inflation-targeting framework, and its basket is dominated "
        "by food, services, housing, and other non-fuel categories. Strong pass-through into wholesale fuel "
        "prices and weak pass-through into headline CPI can therefore coexist as a structural feature rather "
        "than as a model artefact."
    )

    c['section_heading']("1.2 Research question and contribution")
    c['add_para'](
        "The research question asks where the transmission weakens. How do global oil-price shocks transmit across "
        "India's wholesale, retail fuel, fuel-sensitive consumer, and headline consumer price layers, and where "
        "does this pass-through weaken? The framing is not limited to whether oil affects CPI or whether "
        "pass-through is asymmetric. Those questions remain important, but the primary framing is transmission "
        "and attenuation across layers."
    )
    c['add_para'](
        "The dissertation treats oil pass-through as a layered transmission problem rather than as a single "
        "elasticity between crude oil and headline inflation. The estimates use short-run asymmetric "
        "autoregressive distributed lag (ADL) models in log differences with Newey-West HAC inference. Positive "
        "and negative oil components are entered separately, and cumulative pass-through is summarised over the "
        "lag window. A Wald test asks whether the positive and negative cumulative effects are equal. Symmetry "
        "is also assessed using a restricted-residual circular block bootstrap with 4,999 replications. Granger "
        "causality tests and Bai-Perron break tests are used as supporting checks, not as structural causal "
        "evidence."
    )

    c['section_heading']("1.3 Preview of empirical results")
    c['add_para'](
        "Chapter 5 reports the full estimates. The main result can be previewed briefly here because it defines "
        "the contribution of the dissertation. Oil shocks are strongest at direct fuel-price layers, remain "
        "visible in fuel-sensitive wholesale and consumer components, and become much weaker in the broad "
        "headline indices. Positive cumulative pass-through is large for PPAC retail petrol (0.3459) and WPI "
        "Fuel and Power (0.2866), smaller for CPI Fuel and Light (0.1777), modest but statistically "
        "significant for headline WPI (0.0301), and weak and not statistically significant for headline CPI "
        "(0.0213). A common-sample attenuation test rejects equality between retail-petrol and headline-CPI "
        "positive pass-through, with F = 14.3499 and p = 0.0002."
    )
    c['add_para'](
        "The detailed p-values, diagnostics, and robustness checks are deferred to the results chapter. The "
        "important point for the introduction is the ordering. These estimates should not be read as one "
        "structural chain estimate. Each comes from the ADL equation suited to that layer. The common pattern "
        "is that oil shocks are strong in retail petrol and fuel-sensitive wholesale prices, smaller in CPI "
        "Fuel and Light, modest but statistically significant in headline WPI, and weak and not statistically "
        "significant in headline CPI. Short-run asymmetry is not the main finding. The retail petrol layer is "
        "the only layer where asymmetry is suggestive, and even there it is marginal at the 10 percent level."
    )

    c['section_heading']("1.4 Why the question matters")
    c['add_para'](
        "The layered framing speaks to two practical concerns. The first is how to interpret headline CPI as "
        "the monetary-policy anchor in an economy with large external cost shocks. If upstream prices respond "
        "but headline CPI responds weakly, CPI-based policy is not necessarily ignoring oil. It is observing "
        "the shock after basket weights, taxes, margins, and index construction have absorbed part of it. The "
        "second concern is fuel pricing policy. The pre/post-2010 wholesale split provides indirect evidence "
        "consistent with stronger pass-through under more market-linked pricing."
    )

    c['section_heading']("1.5 Roadmap")
    c['add_para'](
        "Chapter 2 places the empirical design inside India's oil pricing institutions and the existing "
        "literature. Chapter 3 describes the data, the chained WPI series, and the variable transformations. "
        "Chapter 4 sets out the asymmetric ADL specification and the inference strategy. Chapter 5 presents the "
        "layered results, the integrated attenuation result, and the pre/post-2010 wholesale split. Chapter 6 "
        "reports robustness checks, diagnostics, and limitations. The conclusion answers the research question "
        "directly."
    )
    c['page_break']()


def write_chapter3(c):
    c['chapter_heading']("Chapter 3", "Data and variables")

    c['section_heading']("3.1 Data sources")
    c['add_para'](
        "The empirical work uses monthly series drawn from official Indian statistical agencies and standard "
        "international macro databases. The wholesale price evidence is built from the Office of the Economic "
        "Adviser (OEA) WPI series, with the headline aggregate and the Fuel and Power group chained across "
        "successive base years to a common 2011-12 base. The retail fuel evidence is taken from the Petroleum "
        "Planning and Analysis Cell (PPAC) ready reckoner, which publishes monthly retail prices of petrol and "
        "diesel for the major Indian metropolitan markets. The international Brent crude price is obtained "
        "from the World Bank Pink Sheet and is cross-checked against the FRED POILBREUSDM series. The INR/USD "
        "exchange rate is obtained from FRED (series EXINUS). The all-India CPI is taken from the Ministry of "
        "Statistics and Programme Implementation (MoSPI), and the harmonised CPI Fuel and Light component is "
        "taken from the same source for the post-2011 period. The Index of Industrial Production is used as the "
        "activity control."
    )
    c['add_para'](
        "All series are merged at monthly frequency on common dates. Active samples are reported in Table 3.1 "
        "after inner joins on dates. The wholesale series carry a non-trivial chaining step that is documented "
        "separately in Section 3.3. The CPI Fuel and Light component is treated as bridge evidence rather than "
        "as a main mandate because the harmonised post-2011 series limits its sample to 164 months."
    )
    c['page_break']()

    c['add_table'](
        headers=["Series", "Source", "Transformation", "Active sample"],
        rows=[
            ["Brent crude (USD/bbl)", "World Bank Pink Sheet", "Monthly log difference", "Matched to layer"],
            ["INR/USD exchange rate", "FRED EXINUS", "Monthly log difference", "Matched to layer"],
            ["Rupee oil price", "Brent multiplied by INR/USD", "Monthly log difference", "Matched to layer"],
            ["Headline WPI", "OEA, chained to 2011-12 = 100", "Monthly log difference", "1983-05 to 2026-03"],
            ["WPI Fuel and Power", "OEA, chained to 2011-12 = 100", "Monthly log difference", "1995-05 to 2026-03"],
            ["PPAC Delhi retail petrol", "PPAC ready reckoner", "Monthly log difference", "2004-08 to 2024-12"],
            ["CPI Fuel and Light", "MoSPI harmonised series", "Monthly log difference", "2011-05 to 2024-12"],
            ["Headline CPI (all-India)", "MoSPI / FRED CPI source", "Monthly log difference", "2004-08 to 2024-12"],
            ["IIP (activity control)", "MoSPI", "Monthly log difference", "Matched to layer"],
        ],
        caption="Table 3.1: Series, sources, transformations, and sample spans",
        col_widths=[1.55, 1.95, 1.10, 1.20],
        font_size=9,
    )
    c['add_note'](
        "Wholesale series are chained to 2011-12 = 100 using official linking factors. Active samples are "
        "reported after inner joins on common monthly dates. CPI Fuel and Light is treated as bridge evidence "
        "because the harmonised series begins in 2011."
    )

    c['section_heading']("3.2 Variable construction")
    c['add_para_math'](
        "The rupee oil price is constructed by multiplying Brent in dollars per barrel by the monthly average "
        "INR/USD exchange rate. In symbols, oil_{INR} = Brent_{USD} * INR_{per USD}. This is the main shock variable "
        "for the headline WPI, WPI Fuel and Power, and headline CPI specifications. The PPAC retail petrol "
        "specification uses Brent as the shock variable because retail petrol movements are tightly linked to "
        "the dollar-denominated benchmark, especially after petrol pricing became more market-linked in 2010. "
        "The CPI Fuel and Light bridge "
        "specification uses the PPAC retail petrol price as the shock variable because it studies how retail "
        "fuel movements enter the fuel-sensitive consumer layer."
    )
    mr, msub, mfenced = c['mr'], c['msub'], c['mfenced']
    eq_3_1 = (mr('Δ') + msub(mr('x'), mr('t')) + mr(' = 100 × [ ln') +
              mfenced(msub(mr('x'), mr('t'))) + mr(' − ln') +
              mfenced(msub(mr('x'), mr('t−1'))) + mr(' ]'))
    c['add_equation'](eq_3_1, label="(3.1)")

    c['add_para_math'](
        "Equation (3.1) defines the monthly log difference of any series x_t scaled by 100. With this scaling, "
        "all main coefficients are approximately percentage responses. If CPT+ is 0.030, a one percent positive "
        "oil shock is associated with about a 0.030 percent cumulative change in the dependent price index over "
        "the lag window."
    )
    c['add_para'](
        "The asymmetric specification splits the rupee oil log difference into positive and negative parts. "
        "Equation (3.2) defines the two components."
    )
    msup = c['msup']
    delta_x = mr('Δ') + msub(mr('x'), mr('t'))
    delta_x_p = msup(mr('Δ') + msub(mr('x'), mr('t')), mr('+'))
    delta_x_m = msup(mr('Δ') + msub(mr('x'), mr('t')), mr('−'))
    eq_3_2 = (delta_x_p + mr(' = max') + mfenced(delta_x + mr(', 0')) + mr(',     ') +
              delta_x_m + mr(' = min') + mfenced(delta_x + mr(', 0')))
    c['add_equation'](eq_3_2, label="(3.2)")
    c['add_para_math'](
        "By construction, the positive component is non-negative and the negative component is non-positive. "
        "Together they sum back to the original log difference. CPT+ is the sum of the lag coefficients on the "
        "positive component, and CPT- is the sum of the lag coefficients on the negative component. CPT- "
        "should not be read as if it were a separate positive shock, because the underlying regressor is "
        "non-positive by construction."
    )

    c['section_heading']("3.3 Chained WPI series")
    c['add_para'](
        "The Office of the Economic Adviser publishes WPI under successive base years, with the most recent "
        "base set at 2011-12 = 100. Earlier vintages used 1981-82, 1993-94, and 2004-05. To assemble a "
        "continuous monthly headline WPI series and a continuous Fuel and Power group from May 1983 to March "
        "2026, the published vintages are linked using their official chain factors, and the splices are "
        "verified at the overlap dates so that they do not introduce visible level breaks. The chained series is "
        "rebased to 2011-12 = 100 so that all wholesale comparisons share one base."
    )
    c['add_para'](
        "Two practical points follow. First, the chained WPI series is the most extensive and methodologically "
        "consistent series available, and its long sample is what makes the pre/post-2010 split feasible. "
        "Second, where component definitions changed across base years, the dissertation prefers the longest "
        "internally consistent stretch over a shorter, perfectly homogeneous stretch."
    )

    c['add_figure'](
        os.path.join(c['ROOT'], "models", "wpi", "outputs", "figures", "fig_01_wpi_chained_series.png"),
        "Figure 3.1: Chained headline WPI and Fuel and Power series, rebased to 2011-12 = 100.",
    )

    c['section_heading']("3.4 The rupee oil shock")
    c['add_para'](
        "The rupee oil shock combines a Brent component and an exchange-rate component. The shock has visible "
        "negative tails during the 2008 commodity correction, the 2014-15 oil price collapse, and the early-2020 "
        "demand shock. It has visible positive tails during the 2007-08 commodity peak, the 2011-12 Brent "
        "surge, and the 2022 episode. These tails motivate the asymmetric specification used in the ADL models. "
        "Co-movement between the rupee oil log difference and WPI Fuel and Power log differences is visible to "
        "the eye across the long sample, while co-movement with headline CPI log differences is much weaker. "
        "This visual pattern is consistent with the layered attenuation result reported in Chapter 5."
    )
    c['add_figure'](
        os.path.join(c['ROOT'], "models", "wpi", "outputs", "figures", "fig_03_oil_decomposition.png"),
        "Figure 3.2: Decomposition of the rupee oil price into Brent and INR/USD contributions.",
    )

    c['section_heading']("3.5 Stationarity")
    c['add_para'](
        "Because the main specifications operate on log differences rather than on levels, the integration "
        "order of the underlying series is less binding than it would be for a levels regression. The unit "
        "root battery is reported for completeness in the model outputs. The augmented Dickey-Fuller, "
        "Phillips-Perron, and KPSS tests of Kwiatkowski et al. (1992) are reported for each series in levels "
        "and in first differences. The combined evidence supports treating the rupee oil price, headline WPI, "
        "WPI Fuel and Power, PPAC retail petrol, and headline CPI as integrated of order one in levels and "
        "stationary in first differences. This supports the differenced ADL specification used in the next "
        "chapter."
    )
    c['page_break']()


def write_chapter4(c):
    c['chapter_heading']("Chapter 4", "Methodology")

    c['section_heading']("4.1 Model specification")
    c['add_para'](
        "The empirical strategy is a short-run asymmetric autoregressive distributed lag (ADL) model in log "
        "differences. The dependent variable is monthly inflation in the relevant price index. The shock "
        "variable changes by layer. The asymmetry is introduced by splitting the shock variable into positive "
        "and negative components, as defined in Chapter 3. Both components are then entered with their own lag "
        "structure on the right-hand side."
    )
    c['add_para'](
        "Equation (4.1) sets out the general form of the model used at every layer."
    )
    mr, msub, msup, mfenced, mnary_sum = c['mr'], c['msub'], c['msup'], c['mfenced'], c['mnary_sum']
    sum_phi = mnary_sum(mr('i=1'), mr('p'),
                        msub(mr('φ'), mr('i')) + mr(' Δ') + msub(mr('y'), mr('t−i')))
    sum_beta_p = mnary_sum(mr('j=0'), mr('q'),
                           msup(msub(mr('β'), mr('j')), mr('+')) + mr(' ') +
                           msup(msub(mr('Δx'), mr('t−j')), mr('+')))
    sum_beta_m = mnary_sum(mr('j=0'), mr('q'),
                           msup(msub(mr('β'), mr('j')), mr('−')) + mr(' ') +
                           msup(msub(mr('Δx'), mr('t−j')), mr('−')))
    eq_4_1 = (mr('Δ') + msub(mr('y'), mr('t')) + mr(' = α + ') + sum_phi +
              mr(' + ') + sum_beta_p + mr(' + ') + sum_beta_m + mr(' + ') +
              msup(msub(mr('Z'), mr('t')), mr('′')) + mr(' γ + ') +
              msub(mr('μ'), mr('m')) + mr(' + ') + msub(mr('ε'), mr('t')))
    c['add_equation'](eq_4_1, label="(4.1)")

    c['add_para_math'](
        "In equation (4.1), Δy_t is the dependent log difference, the φ_i are own-lag coefficients with "
        "own-lag order p, the β_j^+ and β_j^{−} coefficients are the asymmetric distributed-lag coefficients on the positive "
        "and negative shock components with distributed-lag order q, Z_t is a vector of controls, μ_m are "
        "calendar-month fixed effects, and ε_t is the residual. For the long WPI specifications the model "
        "uses twelve own lags and oil lags from zero to six. The same lag structure is retained for the WPI "
        "Fuel and Power specification. For the PPAC retail petrol, CPI Fuel and Light bridge, and headline "
        "CPI specifications, the lag structure follows the channel-mechanism model-gate specifications and "
        "is not re-tuned ex post."
    )

    c['add_table'](
        headers=["Layer", "Dependent variable", "Shock variable", "Role"],
        rows=[
            ["Headline WPI", "Headline WPI inflation", "Rupee oil shock", "Main WPI result"],
            ["WPI Fuel and Power", "WPI Fuel and Power inflation", "Rupee oil shock", "Wholesale fuel mechanism"],
            ["PPAC retail petrol", "Delhi retail petrol inflation", "Brent shock", "Retail fuel mechanism"],
            ["CPI Fuel and Light", "CPI Fuel and Light inflation", "PPAC petrol shock", "Consumer fuel bridge"],
            ["Headline CPI", "Headline CPI inflation", "Rupee oil shock", "Consumer endpoint"],
        ],
        caption="Table 4.1: Model roles by layer",
        col_widths=[1.85, 2.05, 1.30, 1.60],
        font_size=9,
    )
    c['add_note'](
        "Each row is a separate asymmetric ADL specification. The shock variable differs by layer: the rupee "
        "oil price for the headline WPI, WPI Fuel and Power, and headline CPI specifications; Brent for the "
        "retail petrol mechanism; and PPAC retail petrol for the CPI Fuel and Light bridge. The layered map is "
        "therefore an attenuation map across naturally ordered points in the price chain rather than a "
        "structural decomposition of one identical shock."
    )

    c['section_heading']("4.2 Inference")
    c['add_para'](
        "Inference uses Newey and West (1987) heteroscedasticity-and-autocorrelation-consistent standard "
        "errors with a Bartlett kernel and a data-dependent bandwidth. Three formal tests are reported for "
        "each layer. The first asks whether CPT+ differs from zero. The second asks whether CPT- differs from "
        "zero. The third asks whether CPT+ equals CPT-, which is the symmetry test."
    )
    sum_p = mnary_sum(mr('j=0'), mr('q'), msup(msub(mr('β'), mr('j')), mr('+')))
    sum_m = mnary_sum(mr('j=0'), mr('q'), msup(msub(mr('β'), mr('j')), mr('−')))
    eq_4_2 = (msup(mr('CPT'), mr('+')) + mr(' = ') + sum_p + mr(',     ') +
              msup(mr('CPT'), mr('−')) + mr(' = ') + sum_m)
    c['add_equation'](eq_4_2, label="(4.2)")
    c['add_para'](
        "Equation (4.2) defines the cumulative pass-through coefficients used throughout the dissertation. "
        "CPT+ is the sum of the lag coefficients on the positive component. CPT- is the sum of the lag "
        "coefficients on the negative component. The symmetry test in equation (4.3) is the joint linear "
        "restriction tested under HAC inference."
    )
    eq_4_3 = (msub(mr('H'), mr('0')) + mr(': ') +
              msup(mr('CPT'), mr('+')) + mr(' = ') + msup(mr('CPT'), mr('−')))
    c['add_equation'](eq_4_3, label="(4.3)")

    c['add_para'](
        "Symmetry is also assessed using a restricted-residual circular block bootstrap with 4,999 "
        "replications. The bootstrap is restricted-residual to preserve the imposed null structure under "
        "resampling, and the circular block retains the within-block autocorrelation of the residual process. "
        "The bootstrap p-values are reported alongside the asymptotic Wald p-values. They are a robustness "
        "check on the asymptotic test, not a separate model. Where the asymptotic and bootstrap p-values "
        "disagree by a non-trivial margin, the bootstrap is treated as the more conservative reading."
    )

    c['section_heading']("4.3 Lag selection")
    c['add_para'](
        "Lag selection follows the model-gate and lag-selection tables produced for each layer. The own-lag "
        "order is set to twelve in the long WPI specifications to capture annual seasonality even after month "
        "fixed effects are imposed. The distributed-lag order on the oil components is set to six for the "
        "wholesale specifications. The retail petrol, CPI Fuel and Light, and headline CPI specifications "
        "inherit a shorter own-lag order and a distributed-lag order of about three to four, consistent with "
        "the shorter samples and faster pass-through dynamics in the retail and consumer layers. AIC, BIC, and "
        "HQIC support these choices, and lag-sensitivity checks reported in Chapter 6 confirm that the main "
        "results are stable when the distributed-lag order is varied between four and eight in the wholesale "
        "specifications."
    )

    c['section_heading']("4.4 Diagnostics and model roles")
    c['add_para'](
        "The diagnostic battery for each layer reports the Breusch-Godfrey serial correlation test, the "
        "Breusch-Pagan test for heteroscedasticity, the Ramsey RESET test for functional-form misspecification "
        "under the HAC covariance, and recursive and OLS CUSUM stability checks. Model roles are stated "
        "before estimation, not after. Headline WPI is accepted as the main WPI result. The WPI Brent plus "
        "exchange-rate decomposition is a robustness check rather than a competing model. WPI Fuel and Power "
        "is a strong mechanism result, but it is reported with a functional-form caveat because HAC-RESET "
        "fails. Headline CPI M1 is accepted as the main CPI endpoint. PPAC retail petrol is accepted as the "
        "mandatory first-stage mechanism model. CPI Fuel and Light is supporting bridge evidence because the "
        "harmonised sample begins in 2011 and is shorter than the 20-year mandatory sample. The CPI M2 and M3 "
        "specifications are not claim-bearing models because diagnostics reject them for main-text use."
    )
    c['add_para'](
        "Two supporting checks are used in the results chapter. Granger causality tests are reported for "
        "oil to WPI and oil to Fuel and Power, and for Brent to PPAC retail petrol. They support a predictive "
        "directional reading of the chain. They do not establish structural causality. Bai and Perron (2003) "
        "structural break tests are used to check whether the empirical samples are dominated by a single "
        "regime change. Where breaks are detected, the institutional pre/post-2010 split addresses them in the "
        "most policy-relevant way."
    )
    c['page_break']()


def write_chapter5(c):
    c['chapter_heading']("Chapter 5", "Results")

    c['section_heading']("5.1 Headline WPI")
    c['add_para'](
        "The headline WPI specification is estimated on the chained WPI series from May 1983 to March 2026. "
        "The sample contains N = 515 monthly observations and spans 42.92 years. The model achieves an "
        "adjusted R-squared of 0.421. The cumulative pass-through estimates are CPT+ = 0.0301 with p = 0.0240 "
        "and CPT- = 0.0374 with p = 0.0012. Both cumulative effects are statistically distinguishable from "
        "zero at conventional levels. The asymmetry test gives p = 0.6727 under HAC inference and a bootstrap "
        "p of 0.7461. The Breusch-Godfrey, HAC-RESET, and recursive CUSUM diagnostics pass."
    )
    c['add_para'](
        "Headline WPI shows statistically significant but modest pass-through from rupee oil shocks. Positive "
        "and negative cumulative effects are close to each other, so the model does not support short-run "
        "asymmetry in headline WPI. A one percent positive rupee oil shock is associated with about a 0.030 "
        "percent cumulative response in headline WPI over the lag window. This is statistically visible but "
        "quantitatively small given that fuel and power, mineral oils, and oil-intensive manufactured products "
        "together account for a non-trivial share of the WPI basket."
    )

    c['section_heading']("5.2 WPI Fuel and Power")
    c['add_para'](
        "The WPI Fuel and Power specification is estimated from May 1995 to March 2026. The sample contains "
        "N = 371 monthly observations and spans 30.92 years. The model achieves an adjusted R-squared of "
        "0.463. The cumulative pass-through estimates are CPT+ = 0.2866 with p < 0.001 and CPT- = 0.2677 with "
        "p < 0.001. Both cumulative effects are large and highly significant. The asymmetry test gives "
        "p = 0.7832 under HAC inference and a bootstrap p of 0.8196. The Breusch-Godfrey and recursive CUSUM "
        "diagnostics pass; the HAC-RESET test fails."
    )
    c['add_para'](
        "WPI Fuel and Power carries a much stronger oil signal than headline WPI. This fits the economics "
        "because the dependent variable is closer to the fuel channel. The Fuel and Power group covers mineral "
        "oils, electricity, and coal, which are more exposed to energy-cost movements than the headline "
        "basket. The reported coefficient size is large. The exact magnitude of "
        "CPT+ should be reported with a functional-form caveat because the linear specification does not fully "
        "capture the curvature of the relationship, especially during episodes when administered prices and "
        "market-linked prices coexisted in the sample. The sign and the order of magnitude are stable across "
        "specifications, lag windows, and sample trims."
    )

    c['add_table'](
        headers=["Layer", "Sample", "N", "CPT+ (p)", "CPT- (p)", "Asym. p"],
        rows=[
            ["Headline WPI", "1983-05 to 2026-03", "515", "0.0301 (0.0240)", "0.0374 (0.0012)", "0.6727"],
            ["WPI Fuel and Power", "1995-05 to 2026-03", "371", "0.2866 (<0.001)", "0.2677 (<0.001)", "0.7832"],
        ],
        caption="Table 5.1: Headline WPI and WPI Fuel and Power cumulative pass-through",
        col_widths=[1.55, 1.55, 0.45, 1.20, 1.20, 0.85],
        font_size=9,
    )
    c['add_note'](
        "Cumulative pass-through coefficients from asymmetric ADL models in log differences with Newey-West "
        "HAC inference. CPT+ is the sum of the lag coefficients on the positive rupee oil component, CPT- is "
        "the sum of the lag coefficients on the negative component, and the asymmetry p-value is from a Wald "
        "test of CPT+ = CPT-."
    )

    c['add_figure'](
        os.path.join(c['ROOT'], "models", "wpi", "outputs", "figures", "fig_04_cumulative_passthrough.png"),
        "Figure 5.1: Wholesale cumulative pass-through for headline WPI, the Brent plus exchange-rate check, and WPI Fuel and Power.",
    )

    c['section_heading']("5.3 PPAC retail petrol")
    c['add_para'](
        "The PPAC retail petrol mechanism is estimated from August 2004 to December 2024. The sample contains "
        "N = 245 monthly observations and spans 20.42 years. The cumulative pass-through estimates are "
        "CPT+ = 0.3459 with p < 0.001 and CPT- = 0.1912 with p = 0.0002. The asymmetry test gives p = 0.0999. "
        "The mandatory model gate passes for this specification, so it is reported in the main text as the "
        "first-stage mechanism model."
    )
    c['add_para'](
        "Retail petrol is the strongest direct fuel layer in the chain. A one percent positive Brent "
        "shock is associated with about a 0.346 percent cumulative response in Delhi retail petrol over the "
        "model's lag window. The asymmetry result is only marginal at the 10 percent level, so the dissertation "
        "describes it as suggestive evidence of asymmetric retail-price adjustment rather than as a decisive "
        "5 percent result. The retail petrol layer is the layer where asymmetry, if it exists at all in the chain, is "
        "most plausibly located. Its location at this point in the chain rather than at the headline aggregates "
        "is itself an empirical regularity worth noting."
    )

    c['section_heading']("5.4 CPI Fuel and Light bridge")
    c['add_para'](
        "The CPI Fuel and Light bridge specification is estimated from May 2011 to December 2024. The sample "
        "contains N = 164 monthly observations and spans 13.67 years. The shorter sample is dictated by the "
        "harmonised post-2011 CPI series. The cumulative pass-through estimates are CPT+ = 0.1777 with "
        "p = 0.0021 and CPT- = 0.1058 with p = 0.1741. The asymmetry test gives p = 0.4554. The "
        "positive-shock cumulative coefficient is strongly significant; the negative-shock coefficient is not."
    )
    c['add_para'](
        "CPI Fuel and Light shows that retail fuel movements enter a fuel-sensitive consumer layer at a "
        "magnitude smaller than the retail petrol layer but larger than the headline CPI endpoint. Because the "
        "harmonised series begins in 2011, this evidence is treated as a bridge between PPAC retail petrol and "
        "headline CPI rather than as a headline mandate in its own right. The bridge Granger test for retail "
        "petrol to CPI Fuel and Light does not reject the null at conventional levels (p = 0.113), so the "
        "relationship is read as an estimated bridge response rather than as strict predictive precedence."
    )

    c['add_table'](
        headers=["Layer", "Sample", "N", "CPT+ (p)", "CPT- (p)", "Asym. p"],
        rows=[
            ["PPAC retail petrol", "2004-08 to 2024-12", "245", "0.3459 (<0.001)", "0.1912 (0.0002)", "0.0999"],
            ["CPI Fuel and Light bridge", "2011-05 to 2024-12", "164", "0.1777 (0.0021)", "0.1058 (0.1741)", "0.4554"],
        ],
        caption="Table 5.2: PPAC retail petrol and CPI Fuel and Light bridge cumulative pass-through",
        col_widths=[1.85, 1.55, 0.45, 1.20, 1.20, 0.85],
        font_size=9,
    )
    c['add_note'](
        "PPAC retail petrol is estimated with Brent as the shock variable. The CPI Fuel and Light bridge is "
        "estimated with PPAC retail petrol as the shock variable. Inference uses Newey-West HAC standard "
        "errors. The PPAC retail petrol model passes the mandatory model gate; the CPI Fuel and Light "
        "specification is reported as supporting bridge evidence because the harmonised sample begins in 2011."
    )

    c['section_heading']("5.5 Headline CPI")
    c['add_para'](
        "The headline CPI specification is estimated from August 2004 to December 2024. The sample contains "
        "N = 245 monthly observations and spans 20.42 years. The model achieves an adjusted R-squared of "
        "0.4492. The cumulative pass-through estimates are CPT+ = 0.0213 with p = 0.1220 and CPT- = 0.0006 "
        "with p = 0.9375. The asymmetry test gives p = 0.2408 under HAC inference and a bootstrap p of "
        "0.4997. The mandatory model gate passes, so the specification is the main CPI endpoint."
    )
    c['add_para'](
        "Headline CPI is the layer where the oil signal becomes weak. The positive coefficient has the "
        "expected sign, but it is not statistically significant at conventional levels. This supports the "
        "attenuation argument. It does not mean oil is irrelevant for consumers. It means that most of the "
        "shock is absorbed before it reaches the household-facing aggregate. The dissertation does not claim "
        "a strong headline CPI effect. The result is reported as suggestive of limited positive pass-through, "
        "with the formal reading that the cumulative pass-through is not statistically distinguishable from "
        "zero in the post-2004 sample."
    )

    c['add_table'](
        headers=["Layer", "Sample", "N", "Adj. R²", "CPT+ (p)", "CPT- (p)", "Asym. p"],
        rows=[["Headline CPI (M1)", "2004-08 to 2024-12", "245", "0.4492",
               "0.0213 (0.1220)", "0.0006 (0.9375)", "0.2408"]],
        caption="Table 5.3: Headline CPI cumulative pass-through (main endpoint)",
        col_widths=[1.45, 1.55, 0.45, 0.65, 1.10, 1.10, 0.55],
        font_size=9,
    )
    c['add_note'](
        "M1 is the asymmetric ADL specification with rupee oil as the shock variable. Diagnostics: "
        "Breusch-Godfrey passes; HAC-RESET passes; recursive CUSUM passes. The bootstrap symmetry p-value is "
        "0.4997 from 4,999 restricted-residual circular block replications."
    )

    c['section_heading']("5.6 Integrated attenuation result")
    c['add_para'](
        "Bringing the layers together produces the central synthesis of the dissertation. Ordering the layers "
        "by the magnitude of CPT+, the empirical map is the following: PPAC retail petrol at 0.3459, WPI Fuel "
        "and Power at 0.2866, the CPI Fuel and Light bridge at 0.1777, headline WPI at 0.0301, and headline CPI "
        "at 0.0213 (not statistically significant). The ordering broadly follows each layer's closeness to "
        "direct fuel exposure, and the drop between the fuel-sensitive layers and the headline aggregates is "
        "roughly an order of magnitude."
    )
    c['add_para'](
        "A useful supporting view is the common-sample CPI chain, in which all three stages are estimated on "
        "the overlapping sample. Stage 1 (Brent to PPAC petrol) gives CPT+ = 0.4007 with p = 0.0001. Stage 2 "
        "(PPAC petrol to CPI Fuel and Light) gives CPT+ = 0.1777 with p = 0.0021. Stage 3 (oil to headline "
        "CPI) gives CPT+ = 0.0064 with p = 0.6355. A formal Wald test of equality between Stage 1 and Stage 3 "
        "is rejected, with F = 14.3499 and p = 0.0002. The verdict is that attenuation is "
        "present along the common-sample chain."
    )

    c['add_table'](
        headers=["Layer", "N", "CPT+ (p)", "CPT- (p)", "Asym. p"],
        rows=[
            ["PPAC retail petrol", "245", "0.3459 (<0.001)", "0.1912 (0.0002)", "0.0999"],
            ["WPI Fuel and Power", "371", "0.2866 (<0.001)", "0.2677 (<0.001)", "0.7832"],
            ["CPI Fuel and Light bridge", "164", "0.1777 (0.0021)", "0.1058 (0.1741)", "0.4554"],
            ["Headline WPI", "515", "0.0301 (0.0240)", "0.0374 (0.0012)", "0.6727"],
            ["Headline CPI", "245", "0.0213 (0.1220)", "0.0006 (0.9375)", "0.2408"],
            ["Common sample, Stage 1 (Brent to PPAC petrol)", "165", "0.4007 (0.0001)", "0.2263 (0.0007)", "0.1123"],
            ["Common sample, Stage 2 (PPAC to CPI F&L)", "164", "0.1777 (0.0021)", "0.1058 (0.1741)", "0.4554"],
            ["Common sample, Stage 3 (oil to headline CPI)", "168", "0.0064 (0.6355)", "−0.0001 (0.9923)", "0.7340"],
            ["Attenuation Wald: H0 Stage 1 CPT+ = Stage 3 CPT+", "n/a", "F = 14.3499", "p = 0.0002", "Reject"],
        ],
        caption="Table 5.4: Integrated attenuation across the layered chain",
        col_widths=[2.45, 0.55, 1.20, 1.10, 0.50],
        font_size=9,
    )
    c['add_note'](
        "The first five rows are layer-specific cumulative pass-through coefficients, each estimated from its "
        "own asymmetric ADL specification. Common-sample stages restrict each model to the common CPI-chain "
        "window; observation counts differ after lag construction. "
        "The attenuation Wald row tests equality of CPT+ at Stage 1 and Stage 3 under HAC inference. Inference "
        "uses Newey-West HAC standard errors throughout."
    )

    c['add_figure'](
        os.path.join(c['ROOT'], "models", "cpi", "outputs", "figures", "fig_13_dilution_chain.png"),
        "Figure 5.2: CPI attenuation chain from Brent to PPAC petrol, CPI Fuel and Light, and headline CPI.",
    )
    c['add_figure'](
        os.path.join(c['ROOT'], "models", "cpi", "outputs", "figures", "fig_13b_dilution_common_sample.png"),
        "Figure 5.3: Common-sample CPI chain from Brent to headline CPI.",
    )

    c['add_para'](
        "The layered pattern is clear. Oil-price shocks are strong in retail fuel and fuel-sensitive "
        "wholesale prices. They are still visible in CPI Fuel and Light. They are much smaller in the broad "
        "headline indices, especially headline CPI. This is attenuation, not absence. The cumulative "
        "coefficients in Table 5.4 are layer-specific responses, each estimated from its own ADL "
        "specification with its own dependent variable, its own shock variable, and its own sample. They are "
        "not five identical estimates of the same shock passing through five layers in sequence. The PPAC "
        "retail petrol equation uses Brent as the shock; the headline WPI, WPI Fuel and Power, and headline "
        "CPI equations use the rupee oil price; the CPI Fuel and Light bridge uses the PPAC retail petrol "
        "price. The table is therefore best read as an attenuation map across naturally ordered points in the "
        "price chain rather than as a structural decomposition of one elasticity. With that qualification, the "
        "evidence supports the attenuation interpretation."
    )

    c['section_heading']("5.7 Pre/post-2010 wholesale split")
    c['add_para'](
        "The pre/post-2010 split uses an April 2010 cutoff around the petrol deregulation episode. For "
        "headline WPI, the pre-2010 cumulative pass-through is CPT+ = 0.0117 with p = 0.3812, while "
        "the post-2010 cumulative pass-through is CPT+ = 0.0741 with p = 0.0043. For WPI Fuel and Power, the "
        "pre-2010 cumulative pass-through is CPT+ = 0.0922 with p = 0.1679, while the post-2010 cumulative "
        "pass-through is CPT+ = 0.5241 with p < 0.001. The post-2010 estimates are materially larger and "
        "statistically stronger than the pre-2010 estimates in both layers."
    )
    c['add_para'](
        "The post-2010 wholesale estimates are consistent with stronger pass-through under more market-linked "
        "fuel pricing, in which oil marketing companies revise retail prices much more frequently and pass on "
        "more of a given shock within the model's lag window. The split is not a clean causal estimate of "
        "deregulation. Other changes occurred in the post-2010 period as well, including the new CPI series in "
        "2011, the move to flexible inflation targeting in 2016, the Goods and Services Tax in 2017, and a "
        "sequence of fuel-tax episodes."
    )
    c['add_figure'](
        os.path.join(c['ROOT'], "models", "wpi", "outputs", "figures", "fig_05_subsample_comparison.png"),
        "Figure 5.4: Pre/post-2010 cumulative pass-through for headline WPI and WPI Fuel and Power.",
    )
    c['page_break']()


def write_chapter6(c):
    c['chapter_heading']("Chapter 6", "Robustness and limitations")

    c['section_heading']("6.1 Robustness checks")
    c['add_para'](
        "The robustness checks are designed to test whether the layered attenuation result depends on a "
        "particular shock construction, on a particular sample, or on the asymptotic inference. The first "
        "check decomposes the rupee oil price into its Brent and exchange-rate components and re-estimates the "
        "headline WPI specification. The decomposition gives CPT+ = 0.0309 with p = 0.0234 and CPT- = 0.0375 "
        "with p < 0.001, with asymmetry p = 0.7039. This is very close to the rupee oil specification and "
        "suggests that the headline WPI conclusion does not depend on how the shock variable is built."
    )
    c['add_para'](
        "The second check uses the restricted-residual circular block bootstrap with 4,999 replications to "
        "assess short-run asymmetry. The bootstrap p-values are 0.7461 for headline WPI, 0.8196 for WPI Fuel "
        "and Power, and 0.4997 for headline CPI. None of these support a rejection of the null of symmetric "
        "short-run pass-through. The bootstrap and the asymptotic Wald tests therefore agree. Short-run "
        "asymmetry is not the central finding of the dissertation, and where the retail petrol layer hints at "
        "it the evidence is only marginal."
    )
    c['add_para'](
        "The third check uses Granger causality tests in the predictive sense. The tests support directional "
        "precedence from the rupee oil price to headline WPI (F = 7.43, p < 0.001) and to WPI Fuel and Power "
        "(F = 15.22, p < 0.001), and from Brent to PPAC retail petrol (F = 10.71, p < 0.001). The reverse "
        "directions do not reject the null. This is consistent with the layered design, but it is not a "
        "structural causality claim. The fourth check uses Bai and Perron (2003) structural break tests to "
        "check whether the layered relationships are dominated by a single regime change. Where breaks are "
        "detected for headline WPI inflation, the institutional pre/post-2010 wholesale split provides a "
        "policy-relevant comparison."
    )
    c['add_para'](
        "The fifth check addresses the COVID-19 window and outlier sensitivity. Excluding the COVID window "
        "from the headline CPI specification, and winsorising the dependent log differences at the one and "
        "ninety-nine percent tails, do not overturn the main CPI conclusion. The positive cumulative "
        "pass-through remains small and not statistically significant at conventional levels. Lag-sensitivity "
        "checks at oil lags from zero to four and from zero to eight do not change the qualitative ordering of "
        "Table 5.4. Rolling-window estimates of the headline CPI cumulative pass-through hover around the "
        "central estimate without crossing into a significant range at conventional levels."
    )

    c['add_table'](
        headers=["Layer", "BG12", "RESET-HAC", "Rec-CUSUM", "Bootstrap symmetry p"],
        rows=[
            ["Headline WPI", "PASS", "PASS", "PASS", "0.7461"],
            ["WPI Fuel and Power", "PASS", "FAIL", "PASS", "0.8196"],
            ["Headline CPI (M1)", "PASS", "PASS", "PASS", "0.4997"],
        ],
        caption="Table 6.1: Diagnostics and bootstrap symmetry summary",
        col_widths=[1.85, 0.80, 1.10, 1.10, 1.45],
        font_size=9,
    )
    c['add_note'](
        "BG12 is the Breusch-Godfrey serial correlation test at lag 12. RESET-HAC is the Ramsey functional "
        "form test under the HAC covariance. Rec-CUSUM is the recursive CUSUM stability check. Bootstrap "
        "symmetry p-values are from 4,999 restricted-residual circular block replications."
    )

    c['section_heading']("6.2 Limitations")
    c['add_para'](
        "The limitations of the design should be stated plainly. The models are reduced-form projections, not "
        "structural causal estimates. The pre/post-2010 split is institutional evidence consistent with "
        "stronger pass-through under more market-linked pricing, but it is not a clean policy experiment. The "
        "CPI Fuel and Light bridge sample begins in 2011 and is shorter than the headline CPI and headline "
        "WPI samples, which limits the power of the negative-shock test in that layer. The WPI Fuel and Power "
        "model fails the HAC-RESET functional-form test, so the exact magnitude of CPT+ in that layer should "
        "be reported with a functional-form caveat. The CPI M2 and M3 specifications are not claim-bearing "
        "models in the main text because their diagnostics reject them. Headline CPI pass-through should be "
        "described as weak and statistically insignificant, not as zero. The layered table is an attenuation "
        "map across naturally ordered points in the price chain. It is not a structural decomposition of one "
        "identical shock across all equations."
    )
    c['page_break']()


def write_conclusion(c):
    c['chapter_heading']("", "Conclusion")
    c['add_para'](
        "The dissertation set out to ask where oil-price pass-through weakens inside the Indian price system. "
        "The answer is that pass-through is layered, not flat. The shock is strongest at the points of the "
        "price system closest to direct fuel-price exposure, and it becomes weaker as the analysis moves "
        "toward broader household-facing aggregates."
    )
    c['add_para'](
        "The empirical map can be read in five steps. Retail petrol and WPI Fuel and Power show strong "
        "pass-through, with cumulative coefficients of 0.3459 and 0.2866 for positive shocks. CPI Fuel and "
        "Light provides bridge evidence that fuel movements enter a fuel-sensitive consumer layer at a "
        "cumulative coefficient of 0.1777 for positive shocks. Headline WPI shows statistically significant "
        "but modest pass-through at 0.0301. Headline CPI shows weak and statistically insignificant "
        "pass-through at 0.0213. Across all layers, short-run asymmetry is not the main finding. Where it is "
        "most plausibly located, in the retail petrol layer, the evidence is only marginal at the 10 percent "
        "level."
    )
    c['add_para'](
        "The pre/post-2010 wholesale split adds an institutional observation. Pass-through to both headline "
        "WPI and WPI Fuel and Power is materially larger in the post-2010 sample than in the pre-2010 sample. "
        "This is consistent with the move toward more market-linked fuel pricing, under which oil marketing "
        "companies revise retail prices much more frequently. The split is not a clean causal estimate of "
        "deregulation, because the post-2010 period also covers the new CPI series, the move to flexible "
        "inflation targeting, the Goods and Services Tax, and a sequence of fuel-tax episodes."
    )
    c['add_para'](
        "The policy interpretation is restrained. WPI is useful for tracking upstream cost pressure and is "
        "the index where oil shocks remain most clearly visible at the headline level, even after dilution. "
        "CPI is the household-facing index and the inflation-targeting anchor, and it is the index where the "
        "oil signal is weakest at the headline level. Neither index should be treated as a substitute for the "
        "other when the question is about oil shocks. A monetary policy framework that uses CPI as its anchor "
        "is not insulated from oil shocks, but it sees the shock through a heavily diluted layer. A fiscal or "
        "producer-side analysis that uses WPI sees the shock at a magnitude that is small at the headline "
        "level but large in the fuel-sensitive sub-indices that drive intermediate input costs."
    )
    c['add_para'](
        "Two extensions are realistic. The first is a more disaggregated CPI decomposition that moves below "
        "the headline aggregate to the transport, housing, and miscellaneous services components, in order to "
        "trace where the small headline CPI signal is concentrated. The second is a time-varying pass-through "
        "model that allows the cumulative coefficients to evolve smoothly with the pricing regime rather than "
        "as a single break at June 2010. Both extensions remain inside the same architectural framing used "
        "here. They would extend rather than replace the layered map presented in this dissertation."
    )
    c['add_para'](
        "The main lesson is simple: oil shocks do not vanish in India, but they lose force as they move from "
        "fuel prices to headline consumer inflation."
    )
    c['page_break']()


def write_references(c):
    c['chapter_heading']("", "References")
    refs = [
        "Bai, J., & Perron, P. (2003). Computation and analysis of multiple structural change models. "
        "Journal of Applied Econometrics, 18(1), 1-22. https://doi.org/10.1002/jae.659",

        "Bhanumurthy, N. R., Das, S., & Bose, S. (2012). Oil price shock, pass-through policy and its impact "
        "on India (NIPFP Working Paper No. 2012-99). National Institute of Public Finance and Policy.",

        "Kwiatkowski, D., Phillips, P. C. B., Schmidt, P., & Shin, Y. (1992). Testing the null hypothesis of "
        "stationarity against the alternative of a unit root. Journal of Econometrics, 54(1-3), 159-178. "
        "https://doi.org/10.1016/0304-4076(92)90104-Y",

        "Mandal, K., Bhattacharyya, I., & Bhoi, B. B. (2012). Is the oil price pass-through in India any "
        "different? Journal of Policy Modeling, 34(6), 832-848. "
        "https://doi.org/10.1016/j.jpolmod.2012.06.001",

        "Ministry of Statistics and Programme Implementation. (2015). Consumer Price Index: Changes in the "
        "revised series. Government of India.",

        "Newey, W. K., & West, K. D. (1987). A simple, positive semi-definite, heteroskedasticity and "
        "autocorrelation consistent covariance matrix. Econometrica, 55(3), 703-708. "
        "https://doi.org/10.2307/1913610",

        "Office of the Economic Adviser. (2017). Manual on Wholesale Price Index: Base 2011-12 = 100. "
        "Department for Promotion of Industry and Internal Trade, Ministry of Commerce and Industry, "
        "Government of India.",

        "Petroleum Planning and Analysis Cell. (2024). Ready reckoner: India's oil and gas. Ministry of "
        "Petroleum and Natural Gas, Government of India.",

        "Pradeep, S. (2022). Impact of diesel price reforms on asymmetricity of oil price pass-through to "
        "inflation: Indian perspective. The Journal of Economic Asymmetries, 26, e00249. "
        "https://doi.org/10.1016/j.jeca.2022.e00249",

        "World Bank. (2026). Commodity price data: The Pink Sheet. World Bank Commodity Markets.",
    ]
    from docx.shared import Inches, Pt
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    for r in refs:
        p = c['doc'].add_paragraph()
        p.paragraph_format.first_line_indent = Inches(-0.4)
        p.paragraph_format.left_indent = Inches(0.4)
        p.paragraph_format.space_after = Pt(6)
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        run = p.add_run(r)
        run.font.name = 'Times New Roman'
        run.font.size = Pt(12)


# ============================================================
# CHAPTER 2
# ============================================================
def write_chapter2(c):
    c['chapter_heading']("Chapter 2", "Background and literature")

    c['section_heading']("2.1 India's oil-price setting")
    c['add_para'](
        "Three institutional facts shape the empirical design. First, India imports most of its crude oil, so "
        "Brent price movements directly influence domestic refining costs. Second, the rupee price of oil "
        "matters more for domestic inflation than Brent alone, because crude is invoiced in dollars. The "
        "exchange rate is therefore part of the shock rather than an external control. Third, fuel pricing "
        "policy affects how quickly international prices reach consumers. Petrol pricing was deregulated in "
        "June 2010, and diesel pricing was deregulated in October 2014. Under administered pricing, the "
        "government set retail prices for long stretches and absorbed part of the shock through "
        "under-recoveries to oil marketing companies and through subsidy adjustments. Under market-linked "
        "pricing, oil marketing companies revise retail prices much more frequently, which raises the "
        "empirical pass-through that an econometric model can detect."
    )
    c['add_para'](
        "The dissertation reports a pre/post-2010 split for the wholesale models to capture this institutional "
        "shift. The split is informative, but it is not a clean experiment. Other changes also happened after "
        "2010, including CPI rebasing in 2011, the move to flexible inflation targeting in 2016, the Goods and "
        "Services Tax in 2017, several rounds of fuel-tax adjustments, and the global commodity and pandemic "
        "episodes that followed. The post-2010 wholesale estimates are consistent with stronger pass-through "
        "under more market-linked fuel pricing. They should not be read as a clean causal estimate of "
        "deregulation."
    )

    c['section_heading']("2.2 Why WPI and CPI can differ")
    c['add_para'](
        "WPI and CPI answer different empirical questions. WPI is closer to producer and wholesale cost "
        "pressure. The Fuel and Power group within WPI covers mineral oils, electricity, and coal, so it is "
        "more exposed to energy-cost movements than the broad headline basket. CPI is the household-facing "
        "index. It includes food, services, housing, education, health, and other "
        "non-fuel items, and has been the inflation-targeting anchor since 2016. The direct weight of fuel in "
        "CPI is limited, while the weight of food and services is large."
    )
    c['add_para'](
        "This is the main economic reason why a fuel shock can be visible in WPI Fuel and Power and in retail "
        "petrol while staying small in headline CPI. Strong pass-through in fuel-sensitive layers and weak "
        "pass-through at the headline CPI level are not contradictory. They are consistent with the way the two "
        "indices are constructed and with the dilution that happens through tax and margin absorption between "
        "the wholesale layer and the consumer basket."
    )

    c['section_heading']("2.3 Literature")
    c['add_para'](
        "The literature most directly relevant to this dissertation can be summarised in a few studies. "
        "Mandal et al. (2012) examine oil-price pass-through in India and document how domestic adjustment "
        "depends on the pricing regime. Their evidence anticipates the institutional point that empirical "
        "pass-through is partly a function of how often retail prices are revised. Bhanumurthy et al. (2012) "
        "embed oil shocks in a broader macroeconomic frame and consider the trade-off between pass-through "
        "policy, inflation, and fiscal cost. Their work provides useful context for why the political economy "
        "of pass-through is complicated even when the engineering of pass-through is straightforward."
    )
    c['add_para'](
        "Pradeep (2022) studies the impact of diesel price reform on the asymmetricity of oil-price "
        "pass-through to disaggregated wholesale prices, retail diesel, and aggregate consumer prices. That "
        "study is the closest in spirit to the layered design used here, although the present dissertation "
        "extends the layered map to include retail petrol, the WPI Fuel and Power group, the CPI Fuel and Light "
        "bridge, and headline CPI inside a single empirical frame. On the methodological side, Newey and West "
        "(1987) provide the HAC covariance estimator used for inference in the ADL models. Bai and Perron "
        "(2003) provide the multiple-break test used in the structural-break diagnostics. Kwiatkowski et al. "
        "(1992) provide the stationarity test used in the unit root battery."
    )
    c['add_para'](
        "The asymmetric split between positive and negative oil changes follows the applied pass-through "
        "literature. In this dissertation the asymmetric ADL specification is used as a transparent way of "
        "asking whether the cumulative response to positive and negative shocks differs in the short run. The "
        "study does not estimate long-run relationships; the focus is on short-run dynamics in log differences."
    )

    c['section_heading']("2.4 Gap and hypotheses")
    c['add_para'](
        "Existing Indian studies often answer one of these questions in isolation: does oil affect WPI, does "
        "oil affect CPI, do retail fuel prices adjust asymmetrically, and did deregulation alter pass-through. "
        "Each of these is a useful question, but together they leave the reader without a single map of where "
        "the shock survives and where it fades. This dissertation asks a different question. Where does the "
        "shock weaken as it moves through the price system?"
    )
    c['add_para'](
        "The empirical hypotheses follow from this framing. H1: oil shocks pass through significantly to "
        "headline WPI, but the magnitude is small. H2: pass-through is stronger in retail fuel and "
        "fuel-sensitive layers than in the headline aggregates. H3: headline CPI shows attenuation relative to "
        "upstream and fuel-sensitive layers. H4: post-2010 wholesale pass-through is larger than pre-2010 "
        "pass-through, consistent with more market-linked fuel pricing. H5: if short-run asymmetry appears, it "
        "is expected to be more visible at the retail fuel layer than in the broad headline aggregates."
    )
    c['page_break']()
