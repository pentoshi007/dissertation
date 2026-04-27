## Abstract

Write the final paper from the abstract onward. Do not add a title page, declaration, certificate, acknowledgements, table of contents, list of figures, or list of tables. Those items will be added separately. The paper should read like a serious university dissertation chapter or compact dissertation-style paper, not like a generic AI-generated report. Keep the full paper under 8,000 words, excluding only front-matter items that are not part of this file.

The abstract should be 180-250 words. It should state the research problem, data, empirical method, main findings, and conclusion in one tight paragraph. Do not use decorative language. Do not open with a broad statement such as "Oil is the lifeblood of the economy." Start with the empirical problem: India imports most of the crude oil it consumes, but oil-price shocks do not pass evenly through the domestic price system.

The abstract should make four points:

1. The study examines oil-price pass-through in India as a layered transmission process rather than as a single CPI or WPI coefficient.
2. The data come from the `wpi`, `improved-v2`, and `data` folders only. The WPI evidence covers a long historical sample, while the CPI and PPAC retail fuel evidence covers the shorter but policy-relevant post-2004 period.
3. The main method is a short-run asymmetric ADL model in log differences, with Newey-West HAC inference and bootstrap symmetry checks where available. NARDL should be mentioned only as supplementary long-run evidence, not as the main identification strategy.
4. The core result is attenuation: pass-through is strongest at the retail fuel and WPI Fuel and Power layers, visible but small in headline WPI, and weak or statistically indistinguishable from zero in headline CPI.

Suggested abstract wording:

> This study examines how global oil-price shocks move through India's domestic price system. Instead of treating oil pass-through as a single relationship between crude oil and headline inflation, the paper traces the shock across wholesale prices, retail petrol prices, fuel-sensitive indices, and headline consumer inflation. Monthly data are drawn from official WPI series, PPAC retail fuel prices, Brent crude prices, INR/USD exchange rates, CPI series, and the processed datasets in `wpi`, `improved-v2`, and `data`. The main estimates use short-run asymmetric ADL models in log differences with Newey-West HAC inference, cumulative pass-through tests, and bootstrap symmetry checks. The evidence shows a clear ordering. Retail petrol and WPI Fuel and Power respond strongly to oil shocks; headline WPI responds significantly but with a much smaller coefficient; headline CPI shows only weak positive pass-through and no reliable evidence of short-run asymmetry. The pre/post-2010 WPI split suggests stronger pass-through after the move toward more market-linked fuel pricing, but this should be interpreted as institutional evidence rather than a clean causal estimate of deregulation. The paper concludes that Indian oil shocks are not absent from domestic prices. They are absorbed unevenly, with much of the shock diluted before it reaches headline consumer inflation.

## Chapter 1: Introduction

The introduction should be about 900-1,100 words. It should tell the reader why the question matters, what is missing in existing studies, what this paper does differently, and what the main answer is. Keep the opening grounded in India. Do not start with a global history of oil shocks unless it directly supports the Indian research question.

Use this research question:

> How do global oil-price shocks transmit across India's wholesale, retail fuel, fuel-sensitive consumer, and headline consumer price layers, and where does the pass-through weaken?

Do not frame the paper as "Does oil affect CPI?" or "Is oil pass-through asymmetric?" Those are secondary questions. The main framing is transmission and attenuation across layers.

The introduction should follow this order:

1. India is structurally exposed to oil shocks because crude oil is largely imported and priced in dollars. The rupee oil price combines the global Brent price and the INR/USD exchange rate.
2. The policy puzzle is that oil shocks are visible in upstream and fuel-related prices, but the headline CPI response is small. This is not a contradiction; it means the shock weakens somewhere inside the price system.
3. Existing Indian studies often examine one layer at a time: WPI, CPI, or retail fuel. This paper links those layers in one empirical design.
4. The paper uses two model families, but only one is the main workhorse. The body should rely on short-run ADL models in differences. NARDL belongs in a short appendix or supplementary section.
5. State the main results early: WPI headline CPT+ about 0.030, WPI Fuel and Power CPT+ about 0.287, PPAC retail petrol CPT+ about 0.346, CPI Fuel and Light bridge CPT+ about 0.178, and headline CPI CPT+ about 0.021 with p = 0.122.
6. State the contribution modestly. The contribution is not a new estimator or a claim of being the first Indian oil paper. The contribution is the integrated map of where the oil shock survives and where it fades.

Allowed contribution sentence:

> The paper contributes by treating oil-price pass-through in India as a layered transmission problem, showing that oil shocks are strong in retail fuel and fuel-sensitive prices but much weaker in headline consumer inflation.

Do not write:

- "This paper proves oil shocks do not affect CPI."
- "This paper establishes the first complete theory of oil pass-through in India."
- "The results confirm asymmetric pass-through."
- "Deregulation caused the entire post-2010 increase."

## Chapter 2: Institutional Background and Literature

This chapter should be 1,100-1,300 words. It should combine institutional context and literature review. Do not split it into a long generic literature survey. The literature should be used only to position the paper's design.

Use three subsections.

### 2.1 India's Oil Pricing and Inflation Context

Explain the chain in simple terms:

`Brent crude price -> INR/USD exchange rate -> rupee oil price -> domestic retail fuel prices -> fuel-sensitive WPI/CPI components -> headline WPI/CPI`.

The important institutional points are:

- India imports most of its crude oil requirement, so global oil prices enter the domestic economy as an external cost shock.
- Oil is priced internationally in US dollars, which makes the exchange rate part of the domestic shock.
- Retail fuel pricing in India has moved from administered pricing toward more market-linked pricing, with petrol deregulation in June 2010 and diesel deregulation in October 2014.
- WPI and CPI answer different empirical questions. WPI is closer to upstream and producer-side price pressure. CPI is closer to household-facing inflation and the monetary-policy target.
- CPI dilution is expected because the direct fuel weight in the CPI basket is limited, while food and non-fuel services dominate household consumption weights.

Use the RBI/MoSPI CPI weight evidence only as support. Do not overbuild the paper around basket weights unless the final draft has exact official weights and a properly formatted citation.

### 2.2 What Existing Studies Already Show

Keep the literature focused. Use only enough references to support the paper's framing:

- Mandal, Bhattacharyya, and Bhoi (2012) show that oil-price pass-through in India became more relevant under more frequent domestic price adjustment.
- Bhanumurthy, Das, and Bose (2012) discuss oil shocks, pass-through policy, inflation, fiscal costs, and macroeconomic trade-offs in India.
- Pal and Mitra (2016) provide evidence of asymmetric oil-product pricing in India.
- Pradeep (2022) studies diesel price reform and asymmetric oil pass-through to disaggregated wholesale prices, retail diesel prices, and aggregate consumer prices.
- Pesaran, Shin, and Smith (2001) justify the bounds-testing framework used for the appendix NARDL models.
- Shin, Yu, and Greenwood-Nimmo (2014) justify the nonlinear ARDL decomposition.
- Newey and West (1987) justify HAC standard errors in the ADL models.

If the writer adds more references, each one must do real work. Do not add references merely to make the bibliography look longer.

### 2.3 Gap and Hypotheses

The gap is architectural. Existing studies often answer one of these questions separately:

- Does oil affect WPI?
- Does oil affect CPI?
- Do fuel prices adjust asymmetrically?
- Did deregulation alter pass-through?

This paper asks a different question: where does the shock weaken as it moves through the price system?

Use these hypotheses:

- H1: Oil shocks pass through significantly to headline WPI, but the magnitude is small.
- H2: Pass-through is stronger in retail fuel and fuel-sensitive price layers than in headline indices.
- H3: Headline CPI shows attenuation relative to upstream and fuel-sensitive layers.
- H4: Post-2010 wholesale pass-through is larger than pre-2010 pass-through, consistent with more market-linked fuel pricing.
- H5: Short-run asymmetry is not the central finding. It appears most clearly, and only marginally, at the retail petrol layer.

## Chapter 3: Data and Variables

This chapter should be 900-1,100 words. Use only `data`, `wpi`, and `improved-v2`. Do not use the older `improved` or `older` folders unless the user explicitly asks for a historical comparison.

### 3.1 Source Priority

Treat these as the source of truth:

- `wpi/outputs/tables/table_01_data_spans.csv`
- `wpi/outputs/tables/table_02_chain_factors.csv`
- `wpi/outputs/tables/table_03_splice_checks.csv`
- `wpi/outputs/tables/table_04_headline_main_model.csv`
- `wpi/outputs/tables/table_06_fuel_power_model.csv`
- `improved-v2/outputs/tables/table_24_publication_decision.csv`
- `improved-v2/outputs/tables/table_22_ppac_retail_fuel.csv`
- `improved-v2/outputs/tables/table_23_dilution_hypothesis.csv`
- `improved-v2/outputs/tables/table_27_ppac_to_fuel_bridge.csv`
- `improved-v2/outputs/tables/table_28_mandatory_model_gate.csv`

Use raw data only to describe sources:

- `data/raw/wpi/`
- `data/raw/ppac_rsp_pre2017.xls`
- `data/raw/ppac_rsp_post2017.xlsx`
- `data/raw/POILBREUSDM.csv`
- `data/raw/EXINUS.csv`
- `data/raw/INDCPIALLMINMEI.csv`
- `data/processed/`

### 3.2 Main Variables

Define variables clearly:

- Brent crude oil price in USD per barrel.
- INR/USD exchange rate.
- Rupee oil price, constructed as Brent multiplied by INR/USD.
- Headline WPI chained to 2011-12 = 100.
- WPI Fuel and Power chained to 2011-12 = 100.
- PPAC Delhi retail petrol price.
- Headline CPI.
- CPI Fuel and Light, used only as a bridge series because the harmonised sample begins in 2011.
- IIP or activity control where already used in the `improved-v2` models.

All main model variables should be used in month-on-month log differences. Write this as:

`Delta ln(Y_t) = ln(Y_t) - ln(Y_{t-1})`

If the final paper uses percentages, be consistent. Do not mix decimal log changes and percent log changes without saying so.

### 3.3 Data Table

Include one main data table in Chapter 3. Use the content from `paper/tbl_data.tex` or rebuild it from the CSV outputs. The table should have four columns:

1. Series
2. Source
3. Transformation
4. Active sample

Keep the table narrow enough for A4 portrait. Use 9-10 pt font if needed. Do not let long source names overflow. Wrap text inside cells.

Suggested table placement:

`Table 3.1: Series, sources, transformations, and sample spans`

Use this note under the table:

> Notes: Wholesale series are chained to a common 2011-12 = 100 base using official linking factors. Active samples are reported after inner joins on common dates. CPI Fuel and Light is treated as supporting bridge evidence because the harmonised series begins in 2011.

## Chapter 4: Empirical Methodology

This chapter should be 1,000-1,200 words. Keep it technical but readable. Do not bury the reader in equations.

### 4.1 Main ADL Specification

The main model is a short-run asymmetric ADL in log differences. Use positive and negative oil-change components:

`Delta x_t^+ = max(Delta x_t, 0)`

`Delta x_t^- = min(Delta x_t, 0)`

The general model is:

`Delta y_t = alpha + own lags of Delta y_t + lags of Delta x_t^+ + lags of Delta x_t^- + controls + month fixed effects + error`

For WPI, use twelve own lags and oil lags 0-6. For CPI and PPAC mechanism models, follow the lag structure already used in `improved-v2`; do not invent new lag lengths unless rerunning the models.

Define cumulative pass-through:

`CPT+ = sum of coefficients on positive oil-change lags`

`CPT- = sum of coefficients on negative oil-change lags`

Explain interpretation plainly:

> A CPT+ of 0.030 means that a 1 percent positive rupee-oil shock is associated with about a 0.03 percent cumulative increase in the dependent price index over the model's lag window, holding the model's controls fixed.

### 4.2 Inference

Use Newey-West HAC standard errors for coefficient and cumulative restriction tests. State that the paper tests:

- whether CPT+ differs from zero,
- whether CPT- differs from zero,
- whether CPT+ equals CPT-.

Use bootstrap symmetry tests where the outputs report them:

- Headline WPI bootstrap p = 0.746
- WPI Fuel and Power bootstrap p = 0.820
- Headline CPI bootstrap p = 0.500

Do not claim asymmetry when the p-value does not support it.

### 4.3 NARDL as Supplementary Evidence

The NARDL material should not drive the paper. Put it in an appendix or short robustness subsection. The paper may say:

> The NARDL results provide long-run supplementary evidence, but the main conclusions are based on differenced ADL specifications because they are easier to interpret, less dependent on the level-series integration assumptions, and directly aligned with month-on-month inflation dynamics.

Use `wpi/outputs/tables/table_07_nardl_summary.csv` and `paper/tbl_nardl.tex` only if including the appendix.

## Chapter 5: Results

This chapter is the core of the paper and should be about 1,900-2,300 words. It should not become a dump of every CSV. The reader should finish Chapter 5 understanding the layered attenuation result.

### 5.1 Long-Horizon Headline WPI Results

Use:

- `wpi/outputs/tables/table_04_headline_main_model.csv`
- `wpi/outputs/tables/table_05_headline_brent_exr_model.csv`
- `wpi/outputs/tables/table_09_diagnostics.csv`
- `wpi/outputs/tables/table_17_bootstrap_wald.csv`

Main result:

- Sample: 1983-05 to 2026-03
- N = 515
- Span: 42.92 years
- Adjusted R2 = 0.421
- CPT+ = 0.030, p = 0.024
- CPT- = 0.037, p = 0.001
- Asymmetry p = 0.673
- Bootstrap symmetry p = 0.746

Interpretation:

> Headline WPI responds significantly to rupee oil shocks, but the effect is small. The positive and negative cumulative effects are similar, so the headline WPI model does not support short-run asymmetry.

Do not say "oil strongly drives WPI headline inflation." Say "statistically visible but modest."

### 5.2 Fuel and Power WPI

Use:

- `wpi/outputs/tables/table_06_fuel_power_model.csv`
- `wpi/outputs/tables/table_09_diagnostics.csv`
- `wpi/outputs/tables/table_17_bootstrap_wald.csv`

Main result:

- Sample: 1995-05 to 2026-03
- N = 371
- Span: 30.92 years
- Adjusted R2 = 0.463
- CPT+ = 0.287, p < 0.001
- CPT- = 0.268, p < 0.001
- Asymmetry p = 0.783
- Bootstrap symmetry p = 0.820

Interpretation:

> The fuel-sensitive wholesale layer carries a much larger oil signal than headline WPI. This is expected because the dependent variable is closer to the fuel channel. However, the model fails the HAC RESET test, so the exact coefficient should be reported with a functional-form caveat.

### 5.3 Retail Petrol Mechanism

Use:

- `improved-v2/outputs/tables/table_22_ppac_retail_fuel.csv`
- `improved-v2/outputs/tables/table_26_channel_diagnostics.csv`
- `improved-v2/outputs/tables/table_28_mandatory_model_gate.csv`

Main result:

- Sample: 2004-08 to 2024-12
- N = 245
- Span: 20.42 years
- CPT+ = 0.346, p < 0.001
- CPT- = 0.191, p = 0.0002
- Asymmetry p = 0.0999
- Diagnostics accepted for main text

Interpretation:

> The retail petrol layer shows the largest direct pass-through. The asymmetry is only marginal at the 10 percent level, so it can be discussed as suggestive rockets-and-feathers behaviour, not as a strong 5 percent result.

### 5.4 CPI Fuel and Light Bridge

Use:

- `improved-v2/outputs/tables/table_27_ppac_to_fuel_bridge.csv`
- `improved-v2/outputs/tables/table_23_dilution_hypothesis.csv`
- `improved-v2/outputs/tables/table_23b_dilution_common_sample.csv`

Main result:

- Sample: 2011-05 to 2024-12
- N = 164
- Span: 13.67 years
- CPT+ = 0.178, p = 0.0021
- CPT- = 0.106, p = 0.174
- Asymmetry p = 0.455

Interpretation:

> CPI Fuel and Light confirms that retail fuel movements enter fuel-sensitive consumer prices. Because the sample starts in 2011, this is bridge evidence, not a headline mandate.

### 5.5 Headline CPI Endpoint

Use:

- `improved-v2/outputs/tables/table_10_model_comparison.csv`
- `improved-v2/outputs/tables/table_14_bootstrap_wald.csv`
- `improved-v2/outputs/tables/table_24_publication_decision.csv`
- `paper/tbl_cpi.tex`

Main result:

- Sample: 2004-08 to 2024-12
- N = 245
- Span: 20.42 years
- Adjusted R2 = 0.449
- CPT+ = 0.021, p = 0.122
- CPT- = 0.001, p = 0.938
- Asymmetry p = 0.241
- Bootstrap symmetry p = 0.500

Interpretation:

> Headline CPI is the endpoint where the oil signal becomes weak. The positive coefficient has the expected sign but is not statistically significant at 5 percent. The paper may say the result is suggestive of limited positive pass-through, but it must not claim a strong headline CPI effect.

### 5.6 Integrated Attenuation Result

This should be the main synthesis. Use:

- `improved-v2/outputs/tables/table_23_dilution_hypothesis.csv`
- `improved-v2/outputs/tables/table_23c_attenuation_wald.csv`
- `paper/tbl_summary.tex`

Report the ranking:

- PPAC retail petrol CPT+ = 0.346
- WPI Fuel and Power CPT+ = 0.287
- CPI Fuel and Light bridge CPT+ = 0.178
- Headline WPI CPT+ = 0.030
- Headline CPI CPT+ = 0.021, not significant

Interpretation:

> The empirical story is not that oil shocks disappear. They are strong in the fuel channel and then diluted in the headline aggregates. This is the central result of the paper.

### 5.7 Pre/Post-2010 Wholesale Split

Use:

- `wpi/outputs/tables/table_12_subsample_prepost2010.csv`

Report:

- Headline WPI pre-2010 CPT+ = 0.012, p = 0.381
- Headline WPI post-2010 CPT+ = 0.074, p = 0.004
- Fuel and Power pre-2010 CPT+ = 0.092, p = 0.168
- Fuel and Power post-2010 CPT+ = 0.524, p < 0.001

Interpretation:

> The post-2010 estimates are materially larger and consistent with the institutional move toward more market-linked fuel pricing. This is not a full causal identification of deregulation because other changes also occurred in this period.

## Chapter 6: Robustness, Diagnostics, and Limitations

This chapter should be 800-1,000 words. It should show that the author understands the model's weak points.

Include these robustness points:

- Brent plus exchange-rate decomposition gives a similar headline WPI conclusion: CPT+ = 0.031, CPT- = 0.037, asymmetry p = 0.704.
- Bootstrap symmetry tests do not support short-run asymmetry in headline WPI, Fuel and Power WPI, or headline CPI.
- Granger tests support predictive precedence from oil to WPI and Fuel and Power, but Granger evidence is not structural causality.
- COVID-window exclusion and winsorisation do not overturn the main CPI conclusions.
- The NARDL appendix detects long-run asymmetry in some specifications, but this should be treated as supplementary because it depends on level-series assumptions and lag selection.

Limitations to state clearly:

- The models are reduced-form projections, not structural causal estimates.
- The post-2010 split is suggestive, not a clean policy experiment.
- CPI Fuel and Light is shorter than ideal.
- WPI Fuel and Power has a functional-form diagnostic caveat.
- Headline CPI results should be written as weak or suggestive, not decisive.

## Conclusion

The conclusion should be 700-900 words. It should not introduce new tables, new models, or new references. It should return to the research question and answer it directly.

The conclusion should make these points in order:

1. Oil pass-through in India is layered.
2. The shock is clear in retail fuel and fuel-sensitive price indices.
3. It is visible but small in headline WPI.
4. It weakens sharply before reaching headline CPI.
5. Short-run asymmetry is not the main finding.
6. The post-2010 evidence is consistent with stronger pass-through under more market-linked fuel pricing, but it is not a clean causal estimate.
7. Policy interpretation: WPI is useful for upstream cost pressure, CPI is necessary for household inflation, and neither should be treated as a substitute for the other.

Good closing sentence:

> The main lesson is that the question is not whether WPI or CPI is the correct index for oil shocks. The better question is where the oil shock survives inside the price system and where it is absorbed.

Avoid a dramatic ending. Do not write "future research should explore endless possibilities." If adding future work, keep it to two realistic extensions: more disaggregated CPI components and time-varying pass-through models.

## Figures to Include

Use figures from `wpi` and `improved-v2` only. Place each figure close to the paragraph where it is interpreted. If the AI cannot embed the original plot, it must insert a clear placeholder in the text, for example:

`[PLACEHOLDER: Insert wpi/outputs/figures/fig_01_wpi_chained_series.png here. Caption: Chained headline WPI and Fuel and Power series, rebased to 2011-12 = 100.]`

Main-body figures:

1. `wpi/outputs/figures/fig_01_wpi_chained_series.png`  
   Use in Chapter 3 after the data table. It shows the chained WPI construction and splice points.

2. `wpi/outputs/figures/fig_03_oil_decomposition.png`  
   Use in Chapter 3 or Chapter 4. It shows Brent and INR/USD contributions to rupee oil prices.

3. `wpi/outputs/figures/fig_04_cumulative_passthrough.png`  
   Use in Chapter 5.1. It shows the cumulative WPI pass-through profile.

4. `wpi/outputs/figures/fig_05_subsample_comparison.png`  
   Use in Chapter 5.7. It shows pre/post-2010 differences.

5. `improved-v2/outputs/figures/fig_13_dilution_chain.png`  
   Use in Chapter 5.6. This is the most important synthesis figure.

6. `improved-v2/outputs/figures/fig_10_asymmetry_gap.png`  
   Use only if space permits. It supports the claim that asymmetry is not the strongest pattern across layers.

Appendix-only or optional figures:

- `wpi/outputs/figures/fig_11_bootstrap_distribution.png`
- `wpi/outputs/figures/fig_06_cusum_stability.png`
- `wpi/outputs/figures/fig_07_residual_diagnostics.png`
- `improved-v2/outputs/figures/fig_12_bootstrap_distribution.png`
- `improved-v2/outputs/figures/fig_13b_dilution_common_sample.png`

Do not include too many diagnostic figures in the main paper. They interrupt the argument.

## Tables to Include

Use no more than six main tables. If the final paper becomes too long, reduce to four.

Main tables:

1. Data and variable definitions: use `paper/tbl_data.tex` or rebuild from source CSVs.
2. Headline WPI ADL results: use `paper/tbl_wpi.tex`.
3. Mechanism layer results: combine PPAC petrol and WPI Fuel and Power using `paper/tbl_mech.tex`.
4. Headline CPI endpoint: use `paper/tbl_cpi.tex`.
5. Integrated attenuation summary: use `paper/tbl_summary.tex`.
6. Pre/post-2010 split: use `wpi/outputs/tables/table_12_subsample_prepost2010.csv`, either as its own table or merged into the attenuation summary.

Appendix table:

- NARDL bounds battery: use `paper/tbl_nardl.tex`.

Table formatting rules:

- Use clear captions above tables.
- Use notes below tables.
- Use 9-10 pt table font if needed.
- Use wrapped columns for long text.
- Do not use screenshots of tables.
- Use `booktabs` style if writing LaTeX.
- In Word, use fixed column widths and repeat header rows if a table splits across pages.
- If a table does not fit portrait A4, either shorten labels or move it to appendix. Do not let text overlap.

Figure formatting rules:

- Use the original PNG files, not low-resolution screenshots.
- Keep figures within page margins.
- Captions should be concise and interpretive.
- Do not repeat the full regression result in the caption.
- Check that axis labels, legends, and captions do not overlap after export to PDF.
- If the plot is too dense, place it in appendix rather than resizing it until unreadable.

## Writing Rules

The writing should sound like a careful student who understands the work. It should not sound like a promotional abstract, a policy brochure, or generic AI prose.

Use:

- "suggests"
- "is consistent with"
- "provides evidence of"
- "statistically visible but small"
- "reported with a caveat"
- "not statistically distinguishable from zero"

Avoid:

- "proves"
- "confirms beyond doubt"
- "crucial"
- "pivotal"
- "delves into"
- "underscores"
- "showcases"
- "complex tapestry"
- "not only... but also"
- "in today's ever-changing economy"

Do not use forced three-part lists in every paragraph. Vary sentence length. Use direct sentences when the result is simple. It is acceptable to write "This is a small number" or "The result should be treated carefully" where that is the honest interpretation.

Academic integrity rule: write original, source-grounded prose. Do not fabricate citations, p-values, coefficients, sample dates, or robustness checks. Do not try to evade detection systems. The right way to make the paper human is to make it specific, restrained, and defensible.

## Word Budget

Keep the final paper below 8,000 words.

Suggested allocation:

- Abstract: 180-250
- Introduction: 900-1,100
- Institutional background and literature: 1,100-1,300
- Data and variables: 900-1,100
- Methodology: 1,000-1,200
- Results: 1,900-2,300
- Robustness and limitations: 800-1,000
- Conclusion: 700-900
- References: only sufficient and relevant sources

## Word and Dissertation Formatting

Follow the university formatting requirements when converting this blueprint into the final document:

- A4 page size.
- Mirror margins: 1 inch top, bottom, and outside; 3.54 cm inside.
- Portrait orientation.
- Times New Roman, 12 pt body text.
- 1.5 line spacing.
- Justified body text.
- Chapter titles in Heading 1.
- Main sections in Heading 2.
- Subsections in Heading 3.
- Subheadings bold.
- Start each chapter on a new page using a page break.
- Use Word captions for figures and tables so the user can generate lists later.
- Do not manually type the table of contents, list of figures, or list of tables in this file.

## References

Bai, J., & Perron, P. (2003). Computation and analysis of multiple structural change models. *Journal of Applied Econometrics, 18*(1), 1-22. https://doi.org/10.1002/jae.659

Bhanumurthy, N. R., Das, S., & Bose, S. (2012). *Oil price shock, pass-through policy and its impact on India* (NIPFP Working Paper No. 2012-99). National Institute of Public Finance and Policy.

Kwiatkowski, D., Phillips, P. C. B., Schmidt, P., & Shin, Y. (1992). Testing the null hypothesis of stationarity against the alternative of a unit root. *Journal of Econometrics, 54*(1-3), 159-178. https://doi.org/10.1016/0304-4076(92)90104-Y

Mandal, K., Bhattacharyya, I., & Bhoi, B. B. (2012). Is the oil price pass-through in India any different? *Journal of Policy Modeling, 34*(6), 832-848. https://doi.org/10.1016/j.jpolmod.2012.06.001

Ministry of Statistics and Programme Implementation. (2015). *Consumer Price Index: Changes in the revised series*. Government of India.

Newey, W. K., & West, K. D. (1987). A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. *Econometrica, 55*(3), 703-708. https://doi.org/10.2307/1913610

Office of the Economic Adviser. (2017). *Manual on Wholesale Price Index: Base 2011-12 = 100*. Department for Promotion of Industry and Internal Trade, Ministry of Commerce and Industry, Government of India.

Pal, D., & Mitra, S. K. (2016). Asymmetric oil product pricing in India: Evidence from a multiple threshold nonlinear ARDL model. *Economic Modelling, 59*, 314-328. https://doi.org/10.1016/j.econmod.2016.08.003

Pesaran, M. H., Shin, Y., & Smith, R. J. (2001). Bounds testing approaches to the analysis of level relationships. *Journal of Applied Econometrics, 16*(3), 289-326. https://doi.org/10.1002/jae.616

Petroleum Planning and Analysis Cell. (2024). *Ready reckoner: India's oil and gas*. Ministry of Petroleum and Natural Gas, Government of India.

Pradeep, S. (2022). Impact of diesel price reforms on asymmetricity of oil price pass-through to inflation: Indian perspective. *The Journal of Economic Asymmetries, 26*, e00249. https://doi.org/10.1016/j.jeca.2022.e00249

Shin, Y., Yu, B., & Greenwood-Nimmo, M. (2014). Modelling asymmetric cointegration and dynamic multipliers in a nonlinear ARDL framework. In R. C. Sickles & W. C. Horrace (Eds.), *Festschrift in honor of Peter Schmidt: Econometric methods and applications* (pp. 281-314). Springer. https://doi.org/10.1007/978-1-4899-8008-3_9

World Bank. (2026). *Commodity price data: The Pink Sheet*. World Bank Commodity Markets.
