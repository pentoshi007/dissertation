# From wholesale prices to consumer inflation: layered pass-through of global oil shocks in India, 1983-2026

Subtitle: Evidence from short-run asymmetric ADL models

This blueprint is the writing plan for the dissertation from the abstract onward. It is not meant to be copied mechanically. Use it as the final guide for structure, word count, results, table placement, figure placement, citations, and tone.

The dissertation should read like careful work by an MS Economics student. Keep the language plain. Do not decorate the findings. Do not overclaim. Do not use em dashes. Use short sentences when the point is simple. Use longer sentences only when the economics needs it.

The final dissertation should be around 7,000 words in total. A good target is 6,500 to 6,900 words for the main text, including the abstract and conclusion. If references are counted by the department, keep the main text closer to 6,500 words so the final file stays near 7,000 words. If references are not counted, the main text can be closer to 6,800 words.

The study is ADL-only. Do not include a NARDL method, bounds-test evidence, error-correction discussion, or a long-run appendix. The central contribution is the layered pattern of oil-price pass-through in India: strong transmission in retail petrol and fuel-sensitive wholesale prices, moderate transmission in CPI Fuel and Light, modest but significant transmission in headline WPI, and weak transmission in headline CPI.

## Final word budget

Use this word budget while drafting. It keeps the dissertation close to 7,000 words without making the results chapter too thin.

| Part                                  | Target words | Purpose                                                                          |
| ------------------------------------- | -----------: | -------------------------------------------------------------------------------- |
| Abstract                              |          200 | State the question, method, and main result.                                     |
| Chapter 1: Introduction               |          800 | Motivate the puzzle and state the contribution.                                  |
| Chapter 2: Background and literature  |          850 | Explain India's fuel-price setting and place the study in the literature.        |
| Chapter 3: Data and variables         |          850 | Describe sources, transformations, samples, and the constructed rupee oil shock. |
| Chapter 4: Methodology                |          850 | Explain the short-run asymmetric ADL model and inference.                        |
| Chapter 5: Results                    |        1,800 | Present the layered findings and the attenuation result.                         |
| Chapter 6: Robustness and limitations |          700 | Report checks and caveats without overloading the paper.                         |
| Conclusion                            |          550 | Answer the research question directly.                                           |
| References and captions               |   400 to 600 | Keep references relevant and APA formatted.                                      |

Do not treat the word count as equal space for every chapter. Chapter 5 deserves the most space because this is where the dissertation earns its argument.

## Title and research question

Use this title:

> From wholesale prices to consumer inflation: layered pass-through of global oil shocks in India, 1983-2026

Use this subtitle:

> Evidence from short-run asymmetric ADL models

Use this research question:

> How do global oil-price shocks transmit across India's wholesale, retail fuel, fuel-sensitive consumer, and headline consumer price layers, and where does this pass-through weaken?

This title is better than a CPI-only title because the evidence goes beyond headline CPI. The stronger story is that oil shocks appear clearly in fuel-related layers, then become much weaker in headline consumer inflation.

## Core logic of the layered chain

The layered chain is correct, but it must be written carefully. Do not present it as one mechanical equation in which the same shock moves step by step from Brent to WPI to CPI. The study uses separate reduced-form equations for related layers of the price system.

Use two linked ideas.

First, the CPI mechanism chain is:

`Brent crude price -> PPAC retail petrol -> CPI Fuel and Light -> headline CPI`

This chain is the cleanest consumer-price transmission story. Brent is the global shock. PPAC petrol is the direct domestic retail fuel layer. CPI Fuel and Light is the fuel-sensitive consumer layer. Headline CPI is the broad consumer endpoint.

Second, the wholesale map is:

`rupee oil price -> WPI Fuel and Power -> headline WPI`

This is not a claim that WPI causes CPI. It shows how the same external oil pressure appears more strongly in wholesale fuel-sensitive prices than in the broader wholesale index.

The full dissertation combines these two views. The WPI evidence shows upstream and wholesale pass-through. The CPI evidence shows how much of the fuel shock survives into consumer prices. Together, they support a layered attenuation interpretation.

Correct claim:

> Oil shocks are strong in retail fuel and fuel-sensitive wholesale prices, smaller in CPI Fuel and Light, modest in headline WPI, and weak in headline CPI.

Incorrect claim:

> Oil prices pass mechanically from Brent to WPI to CPI through one single chain.

Avoid that second claim. It is too strong and not what the models estimate.

## Abstract

Target: 180 to 220 words. One paragraph.

Start with the empirical problem. Do not begin with a general sentence about the global economy. Mention India, imported crude oil, dollar pricing, WPI, retail fuel, CPI Fuel and Light, and headline CPI.

Suggested abstract:

> This dissertation studies how global oil-price shocks pass through India's domestic price system. India imports most of its crude oil, so Brent price movements and the INR/USD exchange rate together create an external cost shock for domestic prices. Instead of estimating only the relationship between oil and headline CPI, the dissertation follows the shock across several layers: headline WPI, WPI Fuel and Power, PPAC retail petrol, CPI Fuel and Light, and headline CPI. The empirical strategy uses monthly data and short-run asymmetric ADL models in log differences. Inference is based on Newey-West HAC standard errors, cumulative pass-through tests, bootstrap symmetry checks, and diagnostic triage. The results show a clear attenuation pattern. Retail petrol responds strongly to Brent shocks, and WPI Fuel and Power responds strongly to rupee oil shocks. CPI Fuel and Light shows a smaller but significant bridge response. Headline WPI shows statistically significant but modest pass-through, while headline CPI shows only weak positive pass-through that is not statistically significant at conventional levels. Short-run asymmetry is not the main finding. It is only marginal in the retail petrol model and is not supported in the headline WPI, WPI Fuel and Power, or headline CPI models.

## Chapter 1: introduction

Target: about 800 words.

The introduction should make the reader understand the puzzle quickly. India is highly exposed to oil imports, but headline CPI does not move one-for-one with global oil prices. The reason is not that oil is irrelevant. The reason is that price transmission is filtered through exchange rates, fuel pricing, taxes, margins, basket weights, and index construction.

Open with India, not with a broad history of oil shocks. A good first paragraph would say that imported crude is priced in dollars, so the domestic pressure from oil depends on both Brent prices and the exchange rate. Then explain why WPI and CPI may show different responses. WPI is closer to producer costs. CPI is the household-facing index and the inflation-targeting index, but it has a much broader basket.

The introduction should state the contribution in plain language:

> The dissertation treats oil pass-through as a layered transmission problem rather than a single elasticity between crude oil and headline inflation.

State the verified results early, but do not overload the first page with too many numbers. Use one compact paragraph:

- Headline WPI: CPT+ = 0.0301, p = 0.0240; CPT- = 0.0374, p = 0.0012; asymmetry p = 0.6727.
- WPI Fuel and Power: CPT+ = 0.2866, p < 0.001; CPT- = 0.2677, p < 0.001; asymmetry p = 0.7832.
- PPAC Delhi retail petrol: CPT+ = 0.3459, p < 0.001; CPT- = 0.1912, p = 0.0002; asymmetry p = 0.0999.
- CPI Fuel and Light bridge: CPT+ = 0.1777, p = 0.0021; CPT- = 0.1058, p = 0.1741; asymmetry p = 0.4554.
- Headline CPI: CPT+ = 0.0213, p = 0.1220; CPT- = 0.0006, p = 0.9375; asymmetry p = 0.2408.
- Attenuation test: equality of retail-petrol and headline-CPI positive pass-through is rejected, F = 14.3499, p = 0.0002.

End the introduction with a short roadmap. Keep it simple. Do not write a long paragraph that previews every subsection.

Suggested table or figure placement:

- No table is necessary in Chapter 1.
- If the introduction feels abstract, include one small conceptual figure showing the layered chain. If used, place it after the research question. Label it Figure 1.1.

## Chapter 2: background and literature

Target: about 850 words.

This chapter should explain why the layered approach makes sense for India.

### 2.1 India's oil-price setting

Explain three facts.

First, India imports most of its crude oil. Brent price movements therefore matter for domestic costs. Second, the rupee price of oil matters more for domestic inflation than Brent alone because crude is priced in dollars. Third, fuel pricing policy affects how quickly international prices reach consumers.

Discuss petrol deregulation in June 2010 and diesel deregulation in October 2014. Use careful wording. The pre/post-2010 split is useful institutional evidence, but it is not a clean experiment. Other changes also happened after 2010, including CPI rebasing, inflation targeting, GST, changes in fuel taxes, and large global shocks.

Correct wording:

> The post-2010 wholesale estimates are consistent with stronger pass-through under more market-linked fuel pricing. They should not be read as a clean causal estimate of deregulation.

### 2.2 Why WPI and CPI can differ

Make this distinction clear. WPI is closer to producer and wholesale cost pressure. CPI measures household prices and includes food, services, housing, education, health, and other non-fuel items. A fuel shock can be visible in WPI Fuel and Power and still look small in headline CPI because the CPI basket is broader.

This is the main economic reason why the results are not contradictory. Strong pass-through in retail petrol and WPI Fuel and Power can coexist with weak headline CPI pass-through.

### 2.3 Literature

Keep the literature focused. Do not list every oil-price paper. Use papers that help explain the economics or justify the method.

Use Mandal et al. (2012) for Indian oil-price pass-through and domestic fuel adjustments. Use Bhanumurthy et al. (2012) for oil shocks, inflation, and policy trade-offs in India. Use Pradeep (2022) for reform-related pass-through and asymmetry in disaggregated Indian prices. Use Newey and West (1987) for HAC inference. Use Bai and Perron (2003) for structural breaks. Use Kwiatkowski et al. (1992) for stationarity testing.

Suggested table or figure placement:

- Do not use a table unless the chapter becomes too dense.
- If a literature table is required by the supervisor, keep it short: author, data, method, finding, how this dissertation differs. Put it at the end of Chapter 2 as Table 2.1.

## Chapter 3: data and variables

Target: about 850 words.

Use only the active folders:

- `models/data`
- `models/wpi`
- `models/cpi`

Do not use old root-level folders or stale outputs.

### 3.1 Data sources

Describe each source in prose, then use Table 3.1. The data sources are official WPI series from the Office of the Economic Adviser, Brent prices from the World Bank Pink Sheet, INR/USD exchange rates, PPAC Delhi retail petrol prices, MoSPI CPI series, and IIP/activity controls.

Place Table 3.1 immediately after the source discussion.

Table 3.1 should include:

| Series                   | Source                        | Transformation         | Active sample      |
| ------------------------ | ----------------------------- | ---------------------- | ------------------ |
| Brent crude price        | World Bank Pink Sheet         | Monthly log difference | Matched to layer   |
| INR/USD exchange rate    | FRED or source used in data   | Monthly log difference | Matched to layer   |
| Rupee oil price          | Brent multiplied by INR/USD   | Monthly log difference | Matched to layer   |
| Headline WPI             | OEA, chained to 2011-12 = 100 | Monthly log difference | 1983-05 to 2026-03 |
| WPI Fuel and Power       | OEA, chained to 2011-12 = 100 | Monthly log difference | 1995-05 to 2026-03 |
| PPAC Delhi retail petrol | PPAC                          | Monthly log difference | 2004-08 to 2024-12 |
| CPI Fuel and Light       | MoSPI                         | Monthly log difference | 2011-05 to 2024-12 |
| Headline CPI             | MoSPI or processed CPI source | Monthly log difference | 2004-08 to 2024-12 |

### 3.2 Variable construction

Explain the rupee oil price clearly:

`oil_INR = Brent_USD * INR_per_USD`

Then define log differences:

`Delta x_t = 100 * [ln(x_t) - ln(x_{t-1})]`

All main coefficients are approximately percentage responses. If CPT+ is 0.030, a 1 percent positive oil shock is associated with about a 0.03 percent cumulative change in the dependent price index over the lag window.

Explain the positive and negative shock split:

`Delta x_t+ = max(Delta x_t, 0)`

`Delta x_t- = min(Delta x_t, 0)`

Be careful with CPT-. It is the sum of coefficients on the negative-shock regressor. The negative-shock variable is non-positive by construction. Do not describe CPT- as if it were a separate positive oil shock.

Suggested figure placement:

- Place Figure 3.1 after the WPI chaining paragraph: `models/wpi/outputs/figures/fig_01_wpi_chained_series.png`.
- Place Figure 3.2 after the rupee oil construction paragraph: `models/wpi/outputs/figures/fig_03_oil_decomposition.png`.

## Chapter 4: methodology

Target: about 850 words.

This chapter should be clear and not too technical. The reader should understand what the ADL model does and why it fits the question.

### 4.1 Model specification

Use the short-run asymmetric ADL model in log differences:

`Delta y_t = alpha + own lags of Delta y_t + lags of Delta x_t+ + lags of Delta x_t- + controls + month fixed effects + error_t`

Explain the model in words before showing the equation. Say that the dependent variable is monthly inflation in the relevant price index, and the shock variable changes by layer.

Use Table 4.1 after the model equation.

Table 4.1 should include:

| Layer              | Dependent variable            | Shock variable    | Role                     |
| ------------------ | ----------------------------- | ----------------- | ------------------------ |
| Headline WPI       | Headline WPI inflation        | Rupee oil shock   | Main WPI result          |
| WPI Fuel and Power | WPI Fuel and Power inflation  | Rupee oil shock   | Wholesale fuel mechanism |
| PPAC retail petrol | Delhi retail petrol inflation | Brent shock       | Retail fuel mechanism    |
| CPI Fuel and Light | CPI Fuel and Light inflation  | PPAC petrol shock | Consumer fuel bridge     |
| Headline CPI       | Headline CPI inflation        | Rupee oil shock   | Consumer endpoint        |

This table is important because it prevents a logical mistake. It shows that the layers are related, but not all estimated with the same dependent variable or shock variable.

### 4.2 Inference

Define cumulative pass-through:

`CPT+ = sum of positive-shock lag coefficients`

`CPT- = sum of negative-shock lag coefficients`

Report three tests:

- H0: CPT+ = 0.
- H0: CPT- = 0.
- H0: CPT+ = CPT-.

Use Newey-West HAC standard errors for the main inference. Use bootstrap symmetry checks as a robustness check. Do not make the bootstrap sound like a separate model.

### 4.3 Diagnostics and model roles

State the model roles clearly.

- Headline WPI is accepted as the main WPI result.
- WPI Brent plus exchange rate is a decomposition robustness check.
- WPI Fuel and Power is a strong mechanism result, but report it with a functional-form caveat because HAC-RESET fails.
- Headline CPI M1 is accepted as the main CPI endpoint.
- PPAC retail petrol is accepted as the mandatory first-stage mechanism model.
- CPI Fuel and Light is supporting bridge evidence because the sample is shorter than 20 years.
- CPI M2 and M3 are not claim-bearing models because diagnostics reject them for main-text use.

## Chapter 5: results

Target: about 1,800 words.

This chapter should carry the dissertation. Organise it by layers, not by file names.

### 5.1 Headline WPI

Report the result first, then interpret it.

Verified result:

- Sample: 1983-05 to 2026-03.
- N = 515.
- Span = 42.92 years.
- Adjusted R2 = 0.421.
- CPT+ = 0.0301, p = 0.0240.
- CPT- = 0.0374, p = 0.0012.
- Asymmetry p = 0.6727.
- Bootstrap symmetry p = 0.7461.
- Diagnostics: BG, HAC-RESET, and Rec-CUSUM pass.

Interpretation:

> Headline WPI shows statistically significant but modest pass-through from rupee oil shocks. Positive and negative cumulative effects are close, so the model does not support short-run asymmetry in headline WPI.

Place Table 5.1 here if combining headline WPI and WPI Fuel and Power results in one table.

### 5.2 WPI Fuel and Power

Verified result:

- Sample: 1995-05 to 2026-03.
- N = 371.
- Span = 30.92 years.
- Adjusted R2 = 0.463.
- CPT+ = 0.2866, p < 0.001.
- CPT- = 0.2677, p < 0.001.
- Asymmetry p = 0.7832.
- Bootstrap symmetry p = 0.8196.
- Diagnostics: BG and Rec-CUSUM pass; HAC-RESET fails.

Interpretation:

> WPI Fuel and Power carries a much stronger oil signal than headline WPI. This fits the economics because the dependent variable is closer to the fuel channel. The size is large, but report the exact magnitude with a functional-form caveat.

Place Figure 5.1 after sections 5.1 and 5.2: `models/wpi/outputs/figures/fig_04_cumulative_passthrough.png`.

### 5.3 Retail petrol

Verified result:

- Sample: 2004-08 to 2024-12.
- N = 245.
- Span = 20.42 years.
- CPT+ = 0.3459, p < 0.001.
- CPT- = 0.1912, p = 0.0002.
- Asymmetry p = 0.0999.
- Mandatory gate: PASS.

Interpretation:

> Retail petrol is the strongest direct fuel layer. The asymmetry result is only marginal at the 10 percent level, so describe it as suggestive rather than decisive.

### 5.4 CPI Fuel and Light bridge

Verified result:

- Sample: 2011-05 to 2024-12.
- N = 164.
- Span = 13.67 years.
- CPT+ = 0.1777, p = 0.0021.
- CPT- = 0.1058, p = 0.1741.
- Asymmetry p = 0.4554.

Interpretation:

> CPI Fuel and Light shows that retail fuel movements enter a fuel-sensitive consumer layer. Because the sample starts in 2011, use it as bridge evidence rather than as a mandatory headline model.

Place Table 5.2 after sections 5.3 and 5.4. It should combine PPAC retail petrol and CPI Fuel and Light bridge results.

### 5.5 Headline CPI

Verified result:

- Sample: 2004-08 to 2024-12.
- N = 245.
- Span = 20.42 years.
- Adjusted R2 = 0.4492.
- CPT+ = 0.0213, p = 0.1220.
- CPT- = 0.0006, p = 0.9375.
- Asymmetry p = 0.2408.
- Bootstrap symmetry p = 0.4997.
- Mandatory gate: PASS.

Interpretation:

> Headline CPI is where the oil signal becomes weak. The positive coefficient has the expected sign, but it is not statistically significant at conventional levels. This supports the attenuation argument. It does not mean oil is irrelevant for consumers.

Place Table 5.3 here. It can be a short table with the headline CPI cumulative result, diagnostics status, and bootstrap result.

### 5.6 Integrated attenuation result

This is the most important section of the dissertation. It should not read like a list of numbers. Explain what the ordering means.

Main ranking by CPT+:

- PPAC retail petrol: 0.3459.
- WPI Fuel and Power: 0.2866.
- CPI Fuel and Light: 0.1777.
- Headline WPI: 0.0301.
- Headline CPI: 0.0213, not statistically significant.

Common-sample CPI chain:

- Stage 1, Brent to PPAC petrol: CPT+ = 0.4007, p = 0.0001.
- Stage 2, PPAC petrol to CPI Fuel and Light: CPT+ = 0.1777, p = 0.0021.
- Stage 3, oil to headline CPI: CPT+ = 0.0064, p = 0.6355.

Formal attenuation test:

- H0: CPT+ Stage 1 = CPT+ Stage 3.
- F = 14.3499, p = 0.0002.
- Verdict: reject equality. Attenuation is present.

Place Table 5.4 immediately before the interpretation paragraph. This should be the integrated attenuation table.

Place Figure 5.2 immediately after Table 5.4: `models/cpi/outputs/figures/fig_13_dilution_chain.png`.

If space permits, place Figure 5.3 after the common-sample paragraph: `models/cpi/outputs/figures/fig_13b_dilution_common_sample.png`.

Write the interpretation like this:

> The layered pattern is clear. Oil-price shocks are strong in retail fuel and fuel-sensitive wholesale prices. They are still visible in CPI Fuel and Light. They are much smaller in the broad headline indices, especially headline CPI. This is attenuation, not absence.

### 5.7 Pre/post-2010 wholesale split

Verified result:

- Headline WPI pre-2010 CPT+ = 0.0117, p = 0.3812.
- Headline WPI post-2010 CPT+ = 0.0741, p = 0.0043.
- WPI Fuel and Power pre-2010 CPT+ = 0.0922, p = 0.1679.
- WPI Fuel and Power post-2010 CPT+ = 0.5241, p < 0.001.

Interpretation:

> The post-2010 wholesale estimates are larger, especially for Fuel and Power. This is consistent with more market-linked pricing, but it is not a clean causal estimate of deregulation.

Place Table 5.5 here only if space permits. If the paper is too long, move the table to an appendix and keep one paragraph in the main text.

Place Figure 5.4 only if space permits: `models/wpi/outputs/figures/fig_05_subsample_comparison.png`.

## Chapter 6: robustness and limitations

Target: about 700 words.

Keep this chapter tight. It should reassure the reader, not repeat the whole results chapter.

Report these checks:

- WPI Brent plus exchange-rate decomposition gives a similar headline WPI result: CPT+ = 0.0309, p = 0.0234; CPT- = 0.0375, p < 0.001; asymmetry p = 0.7039.
- WPI bootstrap symmetry tests do not reject symmetry for headline WPI or WPI Fuel and Power.
- CPI bootstrap symmetry does not reject symmetry for headline CPI M1.
- CPI M2 and M3 are not claim-bearing models because diagnostics reject them for main-text use.
- Granger tests support predictive precedence from oil to WPI and from Brent to retail petrol, but they are not structural causality tests.
- CPI robustness checks do not overturn the weak headline CPI conclusion.

Use one compact diagnostics table if needed. Place it near the beginning of Chapter 6 as Table 6.1. Do not include every coefficient table in the main text.

Limitations to state plainly:

- The models are reduced-form projections, not structural causal estimates.
- The pre/post-2010 split is institutional evidence, not a clean policy experiment.
- CPI Fuel and Light has a shorter sample than headline CPI and WPI.
- WPI Fuel and Power has a functional-form caveat.
- Headline CPI pass-through should be described as weak and statistically insignificant, not zero.
- The layered table is an attenuation map, not a structural decomposition of one identical shock across all equations.

## Conclusion

Target: about 550 words.

Answer the research question directly. Do not add new results.

Conclusion structure:

1. Oil-price pass-through in India is layered.
2. Retail petrol and WPI Fuel and Power show strong pass-through.
3. CPI Fuel and Light provides bridge evidence that fuel movements enter a consumer fuel layer.
4. Headline WPI shows statistically significant but modest pass-through.
5. Headline CPI shows weak and statistically insignificant pass-through.
6. Short-run asymmetry is not the main result.
7. The post-2010 wholesale split is consistent with stronger pass-through under more market-linked pricing, but it is not clean causal evidence.
8. The policy lesson is that WPI, retail fuel prices, and CPI reveal different parts of the same inflation process.

Good closing sentence:

> The main lesson is simple: oil shocks do not vanish in India, but they lose force as they move from fuel prices to headline consumer inflation.

## Main tables and figures

Use tables and figures inside the chapter where they are discussed. Do not place all tables at the end. Do not include more tables than the argument needs.

Recommended main tables:

| Label     | Placement                       | Content                                          | Source output                                                                                 |
| --------- | ------------------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| Table 3.1 | Chapter 3, after data sources   | Variables, sources, transformations, samples     | Data description and model outputs                                                            |
| Table 4.1 | Chapter 4, after model equation | Model roles by layer                             | Author's summary                                                                              |
| Table 5.1 | Chapter 5.1 to 5.2              | Headline WPI and WPI Fuel and Power results      | `models/wpi/outputs/tables/table_04_headline_main_model.csv`, `table_06_fuel_power_model.csv` |
| Table 5.2 | Chapter 5.3 to 5.4              | PPAC retail petrol and CPI Fuel and Light bridge | `models/cpi/outputs/tables/table_22_ppac_retail_fuel.csv`, `table_27_ppac_to_fuel_bridge.csv` |
| Table 5.3 | Chapter 5.5                     | Headline CPI endpoint result                     | `models/cpi/outputs/tables/table_06_M1_asym_inr.csv`                                          |
| Table 5.4 | Chapter 5.6                     | Integrated attenuation table                     | `models/cpi/outputs/tables/table_23_dilution_hypothesis.csv`, WPI result tables               |
| Table 5.5 | Chapter 5.7, if space permits   | Pre/post-2010 wholesale split                    | `models/wpi/outputs/tables/table_12_subsample_prepost2010.csv`                                |
| Table 6.1 | Chapter 6, if space permits     | Diagnostics and robustness summary               | WPI and CPI diagnostics tables                                                                |

Recommended figures:

| Label      | Placement                         | Figure path                                                     | Purpose                                                 |
| ---------- | --------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------- |
| Figure 3.1 | Chapter 3, WPI construction       | `models/wpi/outputs/figures/fig_01_wpi_chained_series.png`      | Show chained WPI series.                                |
| Figure 3.2 | Chapter 3, oil shock construction | `models/wpi/outputs/figures/fig_03_oil_decomposition.png`       | Show Brent and exchange-rate contribution to rupee oil. |
| Figure 5.1 | Chapter 5, after WPI results      | `models/wpi/outputs/figures/fig_04_cumulative_passthrough.png`  | Show WPI cumulative pass-through.                       |
| Figure 5.2 | Chapter 5, attenuation section    | `models/cpi/outputs/figures/fig_13_dilution_chain.png`          | Main synthesis figure.                                  |
| Figure 5.3 | Chapter 5, if space permits       | `models/cpi/outputs/figures/fig_13b_dilution_common_sample.png` | Common-sample attenuation check.                        |
| Figure 5.4 | Chapter 5, if space permits       | `models/wpi/outputs/figures/fig_05_subsample_comparison.png`    | Pre/post-2010 wholesale comparison.                     |

Every table should have a short note. The note should define CPT+, CPT-, sample period, and whether p-values use Newey-West HAC inference. Every figure should have a caption that says what the reader should notice.

## Writing style rules

Write like a careful economics student, not like a press release.

Use:

- "the results suggest"
- "the estimates are consistent with"
- "statistically significant but modest"
- "weak and not statistically significant"
- "reported with a caveat"
- "reduced-form evidence"

Avoid:

- "proves"
- "clearly demonstrates" unless the test directly supports it
- inflated importance language
- vague claims about significance
- slogan-like contrasts
- decorative verbs when a simple verb works better
- em dashes

Use simple transitions. For example:

- "The next layer is retail petrol."
- "The CPI result is weaker."
- "This is where the attenuation claim comes from."
- "The evidence is suggestive, not causal."

Do not hide uncertainty. The dissertation is stronger when the caveats are honest.

## APA citation rules

Use APA 7 style consistently.

In-text examples:

- Narrative citation with two authors: Newey and West (1987) propose HAC standard errors.
- Parenthetical citation with two authors: (Newey & West, 1987).
- Three or more authors: Mandal et al. (2012) examine oil-price pass-through in India.
- Parenthetical citation with three or more authors: (Mandal et al., 2012).
- Government source in narrative form: The Office of the Economic Adviser (2017) explains the WPI base revision.
- Government source in parenthetical form: (Office of the Economic Adviser, 2017).

Reference list rules:

- Arrange references alphabetically by first author or institutional author.
- Use sentence case for article and report titles.
- Use title case for journal names.
- Italicise journal names and volume numbers.
- Include issue number in parentheses when available.
- Include page range and DOI when available.
- Do not cite a paper in the reference list unless it appears in the text.

## References

Bai, J., & Perron, P. (2003). Computation and analysis of multiple structural change models. _Journal of Applied Econometrics, 18_(1), 1-22. https://doi.org/10.1002/jae.659

Bhanumurthy, N. R., Das, S., & Bose, S. (2012). _Oil price shock, pass-through policy and its impact on India_ (NIPFP Working Paper No. 2012-99). National Institute of Public Finance and Policy.

Kwiatkowski, D., Phillips, P. C. B., Schmidt, P., & Shin, Y. (1992). Testing the null hypothesis of stationarity against the alternative of a unit root. _Journal of Econometrics, 54_(1-3), 159-178. https://doi.org/10.1016/0304-4076(92)90104-Y

Mandal, K., Bhattacharyya, I., & Bhoi, B. B. (2012). Is the oil price pass-through in India any different? _Journal of Policy Modeling, 34_(6), 832-848. https://doi.org/10.1016/j.jpolmod.2012.06.001

Ministry of Statistics and Programme Implementation. (2015). _Consumer Price Index: Changes in the revised series_. Government of India.

Newey, W. K., & West, K. D. (1987). A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. _Econometrica, 55_(3), 703-708. https://doi.org/10.2307/1913610

Office of the Economic Adviser. (2017). _Manual on Wholesale Price Index: Base 2011-12 = 100_. Department for Promotion of Industry and Internal Trade, Ministry of Commerce and Industry, Government of India.

Petroleum Planning and Analysis Cell. (2024). _Ready reckoner: India's oil and gas_. Ministry of Petroleum and Natural Gas, Government of India.

Pradeep, S. (2022). Impact of diesel price reforms on asymmetricity of oil price pass-through to inflation: Indian perspective. _The Journal of Economic Asymmetries, 26_, e00249. https://doi.org/10.1016/j.jeca.2022.e00249

World Bank. (2026). _Commodity price data: The Pink Sheet_. World Bank Commodity Markets.
