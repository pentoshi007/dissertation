# Claude-ready PPT Blueprint

Copy everything inside this file and give it to Claude to recreate or improve the PowerPoint.

This blueprint is designed for an external university evaluation. The presentation should look academic, clear, and confident, but the language must stay simple enough for the presenter to speak from the slides.

---

# Master prompt for Claude

Create a PowerPoint presentation for my MS Economics dissertation external evaluation.

The deck should have:

- 1 title slide
- 11 numbered content slides
- 1 thank-you slide
- Total: 13 slides
- Maximum presentation time: 15 minutes
- No speaker notes on the first title slide

## Dissertation title

From wholesale prices to consumer inflation: layered pass-through of global oil shocks in India, 1983-2026

## Presenter context

The presenter is introverted and not fully comfortable with spoken English or advanced econometrics. Therefore:

- Slides should not be too empty.
- Slides should not be text-heavy.
- Use medium text so evaluators can understand the research even if the presenter speaks briefly.
- Add short speaker notes for content slides in simple English.
- Use clean academic design, not flashy corporate design.
- Avoid very long sentences.
- Use simple words where possible.
- Put important equations and results on slides, but explain them in plain language.

## Design style

Use this style:

- Academic, modern, clean.
- Background: white or very light grey.
- Main colour: dark navy.
- Accent colours:
  - dark red or burnt orange for strong pass-through
  - amber for medium pass-through
  - grey-blue for weak pass-through
- Use flow diagrams for the layered chain.
- Use tables for data sources and main results.
- Use large readable fonts.
- Use icons only if they are simple: oil barrel, petrol pump, rupee, shopping basket, chart.

## Very important content rules

Do not add NARDL, bounds tests, cointegration, or error-correction language. This dissertation is short-run ADL only.

Do not claim structural causality.

Use this careful wording:

> The layered map is an attenuation map across related price layers. It is not one single mechanical causal chain.

Use this main conclusion:

> Oil shocks pass through strongly to fuel-related layers, but the effect becomes weak and statistically insignificant at headline CPI. This is attenuation, not absence.

## Main technical content to include

Keep these technical items in the main presentation:

1. Objective and research question.
2. Data sources and purpose of each variable.
3. Layered transmission map.
4. Short-run asymmetric ADL equation.
5. Meaning of positive and negative oil shocks.
6. Meaning of CPT+ and CPT-.
7. Newey-West HAC inference in one simple line.
8. Main results table.
9. Formal attenuation Wald test.
10. Discussion and policy relevance.
11. Final conclusion.

Keep only these tests in the main slides:

- p-values for CPT+ and CPT-
- asymmetry p-value, meaning CPT+ = CPT-
- key diagnostic/model gate as a short statement only
- attenuation Wald test: F = 14.3499, p = 0.0002

Move these to backup or omit from main slides:

- Bootstrap symmetry details
- AIC/BIC/HQIC details
- Granger causality details
- Bai-Perron structural break tests
- Breusch-Pagan details
- Full residual diagnostics
- Coefficient-by-coefficient regression tables

---

# Slide-by-slide structure

Create the title slide, 11 content slides, and a thank-you slide. If backup slides are added, keep them after the thank-you slide or as hidden slides.

---

# Slide 1: Title

## Slide title

From wholesale prices to consumer inflation

## Subtitle

Layered pass-through of global oil shocks in India, 1983-2026

## Slide content

- Aniket Pandey
- B.Tech + MS Economics
- School Of Engineering, JNU
- Supervisor: Prof. Shakti Kumar

## Visual

Use a simple horizontal visual:

`Brent crude -> Retail petrol -> Wholesale prices -> Consumer basket`

## Speaker notes

Do not add speaker notes on this slide.

---

# Slide 2: Background and motivation

## Slide title

Why oil-price pass-through matters for India

## Slide content

- India imports most of its crude oil.
- Crude oil is priced internationally, mainly in US dollars.
- Domestic oil pressure depends on:
  - Brent crude price
  - INR/USD exchange rate
- Oil can affect:
  - retail petrol prices
  - wholesale fuel prices
  - transport and input costs
  - consumer inflation
- But headline CPI does not move one-for-one with oil.

## Visual

Create a simple diagram:

`Brent crude + INR/USD -> domestic oil-cost pressure -> Indian price system`

## Speaker notes

India is exposed to oil shocks because it imports crude oil and crude is priced in dollars. But headline CPI is a broad index. It includes food, housing, services, and many non-fuel items. So the oil effect may become diluted before reaching headline CPI.

---

# Slide 3: Research gap, objective, and research question

## Slide title

Objective and research question

## Slide content

Research gap:

- Many discussions focus directly on oil price and headline inflation.
- This can hide where the oil effect is strong and where it becomes weak.

Objective:

- To estimate short-run oil-price pass-through across multiple Indian price layers.
- To identify whether the shock attenuates before reaching headline CPI.

Research question:

> How do global oil-price shocks transmit across India's wholesale, retail fuel, fuel-sensitive consumer, and headline consumer price layers, and where does this pass-through weaken?

## Speaker notes

The main objective is to study oil pass-through layer by layer. Instead of only asking whether oil affects headline CPI, I ask where the effect is strong and where it becomes weak.

---

# Slide 4: Conceptual framework: layered pass-through

## Slide title

Conceptual framework: a layered price map

## Slide content

Consumer-side chain:

`Brent crude -> PPAC retail petrol -> CPI Fuel and Light -> Headline CPI`

Wholesale-side map:

`Rupee oil price -> WPI Fuel and Power -> Headline WPI`

Important interpretation:

- Each layer is estimated separately.
- The map shows attenuation across related price layers.
- It is not a single mechanical WPI-to-CPI causal chain.

## Visual

Create a two-row flow diagram.

Row 1: Brent crude -> Retail petrol -> CPI Fuel and Light -> Headline CPI  
Row 2: Rupee oil price -> WPI Fuel and Power -> Headline WPI

Add colour intensity from strong to weak:

- Strong fuel layers: dark red/orange
- Medium bridge layer: amber
- Weak headline layer: grey-blue

## Speaker notes

This slide shows the logic of the dissertation. The consumer-side chain follows Brent to retail petrol, CPI Fuel and Light, and headline CPI. The wholesale-side map follows rupee oil price to WPI Fuel and Power and headline WPI. These are related layers, but each model is estimated separately.

---

# Slide 5: Data sources and purpose

## Slide title

Data sources and variable purpose

## Slide content

Use this table:

| Series                   | Source                                                     | Transformation         | Purpose in study                               |
| ------------------------ | ---------------------------------------------------------- | ---------------------- | ---------------------------------------------- |
| Brent crude price        | World Bank Pink Sheet, cross-checked with FRED POILBREUSDM | Monthly log difference | Global oil shock                               |
| INR/USD exchange rate    | FRED EXINUS                                                | Monthly log difference | Exchange-rate component of domestic oil cost   |
| Rupee oil price          | Brent × INR/USD                                            | Monthly log difference | Main oil shock for WPI and headline CPI models |
| Headline WPI             | Office of the Economic Adviser, chained to 2011-12 base    | Monthly log difference | Wholesale headline layer                       |
| WPI Fuel and Power       | Office of the Economic Adviser, chained to 2011-12 base    | Monthly log difference | Wholesale fuel-sensitive layer                 |
| PPAC Delhi retail petrol | PPAC ready reckoner                                        | Monthly log difference | Direct domestic retail fuel layer              |
| CPI Fuel and Light       | MoSPI harmonised series                                    | Monthly log difference | Fuel-sensitive consumer bridge                 |
| Headline CPI             | MoSPI / FRED CPI source                                    | Monthly log difference | Consumer endpoint                              |
| IIP                      | MoSPI                                                      | Monthly log difference | Activity control                               |

## Small note on slide

Monthly log differences are used as approximate monthly percentage changes.

## Speaker notes

The study uses monthly data. The variables are converted into log differences, which can be read approximately as monthly percentage changes. The rupee oil price combines Brent and the exchange rate, so it captures domestic oil-cost pressure.

---

# Slide 6: Model layers and samples

## Slide title

Five estimated layers

## Slide content

Use this table:

| Layer              | Dependent variable       | Shock variable    | Sample                                     | Role                               |
| ------------------ | ------------------------ | ----------------- | ------------------------------------------ | ---------------------------------- |
| Headline WPI       | WPI inflation            | Rupee oil shock   | 1983-05 to 2026-03                         | Main wholesale result              |
| WPI Fuel and Power | Fuel and Power inflation | Rupee oil shock   | 2010-04 to 2026-03, excluding Apr-Sep 2020 | Preferred wholesale fuel mechanism |
| PPAC retail petrol | Delhi petrol inflation   | Brent shock       | 2004-08 to 2024-12                         | Direct retail fuel mechanism       |
| CPI Fuel and Light | Fuel and Light inflation | PPAC petrol shock | 2011-05 to 2024-12                         | Consumer fuel bridge               |
| Headline CPI       | CPI inflation            | Rupee oil shock   | 2004-08 to 2024-12                         | Consumer endpoint                  |

## Speaker notes

Each row is a separate model. The dependent variable and shock variable change according to the layer. This is why I describe the results as a layered map, not one single equation for the whole price system.

---

# Slide 7: Methodology: short-run asymmetric ADL model

## Slide title

Methodology: short-run asymmetric ADL model

## Slide content

Show this equation clearly:

`Δy_t = α + Σ φ_i Δy_{t-i} + Σ β_j^+ Δx^+_{t-j} + Σ β_j^- Δx^-_{t-j} + γ'Z_t + μ_m + ε_t`

Plain-English explanation:

- `Δy_t`: current monthly inflation in the selected price layer
- `Δy_{t-i}`: past inflation in the same layer
- `Δx^+`: positive oil shock
- `Δx^-`: negative oil shock
- `Z_t`: controls such as IIP and policy/COVID dummies where relevant
- `μ_m`: month effects for seasonality
- `ε_t`: unexplained part of inflation

Why ADL?

- Price adjustment takes time.
- Oil shocks can affect prices over several months.
- Positive and negative shocks may behave differently.

## Speaker notes

The model is an ADL model, which means current inflation depends on its own past values and current and past oil shocks. I use an asymmetric form because positive and negative oil shocks are entered separately. This allows me to test whether price increases and decreases are passed through differently.

---

# Slide 8: Key quantities and inference

## Slide title

What the model estimates

## Slide content

Cumulative pass-through:

`CPT+ = Σ β_j^+`

`CPT- = Σ β_j^-`

Meaning:

- `CPT+`: total response to positive oil shocks over the lag window
- `CPT-`: total response to negative oil shocks over the lag window
- Asymmetry test: checks whether `CPT+ = CPT-`

Important inference choices:

- OLS estimates the ADL equations.
- Newey-West HAC standard errors are used for p-values.
- HAC is used because monthly time-series errors may have autocorrelation and changing variance.

## Speaker notes

The main numbers in the results are CPT plus and CPT minus. They sum the lagged effects because oil-price pass-through may happen over several months. I use Newey-West HAC standard errors to make the p-values more reliable for monthly time-series data.

---

# Slide 9: Main results across layers

## Slide title

Main result: pass-through weakens across layers

## Slide content

Use this table:

| Layer              |   N |   CPT+ | p-value |   CPT- | p-value | Asym. p | Interpretation                      |
| ------------------ | --: | -----: | ------: | -----: | ------: | ------: | ----------------------------------- |
| WPI Fuel and Power | 186 | 0.5205 |  <0.001 | 0.4195 |  <0.001 |  0.1642 | Strong wholesale fuel pass-through  |
| PPAC retail petrol | 245 | 0.3459 |  <0.001 | 0.1912 |  0.0002 |  0.0999 | Strong direct fuel pass-through     |
| CPI Fuel and Light | 164 | 0.1777 |  0.0021 | 0.1058 |  0.1741 |  0.4554 | Significant bridge evidence         |
| Headline WPI       | 515 | 0.0301 |  0.0240 | 0.0374 |  0.0012 |  0.6727 | Modest but significant              |
| Headline CPI       | 245 | 0.0213 |  0.1220 | 0.0006 |  0.9375 |  0.2408 | Weak, not statistically significant |

Key message box:

> Strong near fuel prices, weak at headline CPI.

## Design instruction

Highlight the CPT+ column and the interpretation column. Use colour strength to show strong, medium, and weak pass-through.

## Speaker notes

This is the main results table. The largest pass-through is in WPI Fuel and Power and retail petrol. CPI Fuel and Light is smaller but still significant. Headline WPI is modest. Headline CPI is positive, but not statistically significant. So the main finding is attenuation.

---

# Slide 10: Wholesale results

## Slide title

Wholesale results: WPI and WPI Fuel and Power

## Slide content

Headline WPI:

- CPT+ = 0.0301, p = 0.0240
- CPT- = 0.0374, p = 0.0012
- Result: modest but statistically significant

WPI Fuel and Power, preferred model:

- CPT+ = 0.5205, p < 0.001
- CPT- = 0.4195, p < 0.001
- Result: strong wholesale fuel pass-through
- Preferred sample: post-2010, excluding COVID months

Interpretation:

> The oil signal is much stronger in the fuel-sensitive wholesale layer than in broad headline WPI.

## Figure

Use this project figure if available:

`models/wpi/outputs/figures/fig_04_cumulative_passthrough.png`

If the figure is too crowded, create a simple two-bar comparison instead.

## Speaker notes

The wholesale results show that oil clearly affects fuel-sensitive wholesale prices. WPI Fuel and Power has a large and significant response. Headline WPI also responds, but the size is much smaller because the headline index is broader.

---

# Slide 11: Retail petrol and CPI Fuel and Light

## Slide title

Consumer fuel layers: retail petrol and CPI Fuel and Light

## Slide content

PPAC retail petrol:

- Shock variable: Brent crude
- CPT+ = 0.3459, p < 0.001
- CPT- = 0.1912, p = 0.0002
- Asymmetry p = 0.0999
- Interpretation: strong direct fuel pass-through; asymmetry only marginal

CPI Fuel and Light:

- Shock variable: PPAC retail petrol
- CPT+ = 0.1777, p = 0.0021
- CPT- = 0.1058, p = 0.1741
- Interpretation: significant bridge from retail fuel to consumer fuel category

## Visual

Create a simple two-step diagram:

`Brent -> Retail petrol -> CPI Fuel and Light`

Add small labels:

- Strong direct response at retail petrol
- Smaller but significant bridge response in CPI Fuel and Light

## Speaker notes

Retail petrol responds strongly to Brent shocks. CPI Fuel and Light also responds to retail petrol, but the size is smaller. This supports the idea that the oil shock enters consumer prices through fuel-related components, but becomes weaker as it moves forward.

---

# Slide 12: Headline CPI result

## Slide title

Headline CPI: the oil signal becomes weak

## Slide content

Headline CPI model:

- Sample: 2004-08 to 2024-12
- N = 245
- CPT+ = 0.0213, p = 0.1220
- CPT- = 0.0006, p = 0.9375
- Asymmetry p = 0.2408
- Model gate: passes

Interpretation:

- Positive CPT+ has the expected sign.
- But it is not statistically significant at conventional levels.
- This supports attenuation.
- It does not mean oil is irrelevant.

Key sentence:

> Headline CPI is where pass-through becomes weak and statistically quiet.

## Speaker notes

The headline CPI result is important because CPI is the final consumer inflation layer. The positive coefficient has the expected sign, but the p-value is above 0.05. So I do not claim strong CPI pass-through. I say the oil effect becomes weak at the headline CPI level.

---

# Slide 13: Formal attenuation result

## Slide title

Formal evidence of attenuation

## Slide content

Common-sample consumer chain:

| Stage   | Relationship                      |   CPT+ | p-value |
| ------- | --------------------------------- | -----: | ------: |
| Stage 1 | Brent -> PPAC retail petrol       | 0.4007 |  0.0001 |
| Stage 2 | PPAC petrol -> CPI Fuel and Light | 0.1777 |  0.0021 |
| Stage 3 | Rupee oil -> Headline CPI         | 0.0064 |  0.6355 |

Attenuation Wald test:

- Null hypothesis: Stage 1 CPT+ = Stage 3 CPT+
- F = 14.3499
- p = 0.0002
- Verdict: reject equality

Conclusion:

> The attenuation pattern is statistically supported.

## Figure

Use this project figure:

`models/cpi/outputs/figures/fig_13_dilution_chain.png`

If using both table and figure makes the slide crowded, use the figure as the main visual and place the Wald test result in a callout box.

## Speaker notes

To formally test attenuation, I compare the first and final stages of the consumer chain. The Wald test rejects equality between retail petrol pass-through and headline CPI pass-through. This supports the main attenuation result.

---

# Slide 14: Discussion and policy relevance

## Slide title

Discussion and policy relevance

## Slide content

Main result to explain:

> Pass-through falls sharply: retail petrol 0.4007 -> CPI Fuel 0.1777 -> headline CPI 0.0064.

What the results mean:

- Oil is clearly visible in fuel prices.
- The CPI Fuel and Light response is smaller, but still significant.
- Headline CPI dilutes the oil signal across a broad basket.
- The main result is attenuation across layers.

Policy focus:

- Do not rely only on headline CPI.
- Track retail fuel, WPI Fuel and Power, and CPI Fuel and Light.
- Watch transport and input costs for second-round pressure.
- Fuel taxes and pricing choices can change pass-through.

Final policy message:

> Oil pressure can build in fuel layers before it appears in headline CPI.

## Speaker notes

After the attenuation test, I will explain what the result means.

The numbers fall sharply across the consumer chain. Retail petrol responds strongly. CPI Fuel and Light responds less, but still significantly. Headline CPI is almost zero in the common-sample chain.

This makes sense because headline CPI is a broad basket. Fuel is only one part of it. So the oil signal becomes weaker when it is mixed with food, services, housing, and other items.

For policy, the important point is monitoring. Headline CPI alone may miss pressure building in fuel-sensitive layers. Retail fuel, WPI Fuel and Power, and CPI Fuel and Light should be watched together.

The model does not prove one exact policy action. It shows that policy should separate direct fuel shocks from wider second-round inflation.

---

# Slide 15: Conclusion

## Slide title

Conclusion: oil pass-through is layered and attenuated

## Slide content

Main conclusion:

> Oil-price shocks matter in India, but their effect weakens across the price system.

Findings by layer:

- Strong: WPI Fuel and Power and PPAC retail petrol.
- Bridge: CPI Fuel and Light is smaller but significant.
- Modest: headline WPI is small but statistically significant.
- Weak: headline CPI is not statistically significant.

Takeaways:

- Attenuation pattern is visible at every step of the consumer chain.
- Stage 1 vs Stage 3 ratio is about 63× smaller, and equality is rejected.
- Asymmetry is not the central result; only retail petrol is marginal.
- Fuel-only and headline-CPI views give different policy reads.

Final sentence:

> Attenuation, not absence, of oil-price transmission.

## Speaker notes

To conclude, the central finding is layered attenuation.

Oil shocks matter in India, but the effect is not equally strong everywhere. It is strong in WPI Fuel and Power and retail petrol. It is smaller in CPI Fuel and Light. It is modest in headline WPI. It is weak and not statistically significant in headline CPI.

The formal attenuation test also supports this result.

So my final conclusion is simple: oil-price transmission is present, but it becomes diluted before reaching headline CPI.

Thank you. I am happy to take your questions.

---

# Backup slide 1: ADL equation explained simply

Use this only if evaluators ask about the equation.

## Slide title

Backup: ADL model in simple words

## Slide content

ADL means Autoregressive Distributed Lag.

- Autoregressive: current inflation depends on past inflation.
- Distributed lag: oil shocks can affect prices over several months.
- Asymmetric: positive and negative oil shocks are entered separately.
- Short-run: the model studies monthly changes, not long-run equilibrium.

Simple model idea:

`Current inflation = past inflation + oil shocks over several months + controls + error`

## Speaker notes

The ADL model is useful because price adjustment is not always immediate. Oil shocks can take several months to show in domestic prices.

---

# Backup slide 2: Important tests explained simply

Use this only if asked about tests.

## Slide title

Backup: key tests in plain language

## Slide content

- p-value for CPT+: checks whether positive-shock pass-through is statistically different from zero.
- p-value for CPT-: checks whether negative-shock pass-through is statistically different from zero.
- Asymmetry p-value: checks whether positive and negative pass-through are different.
- BG test: checks serial correlation.
- HAC-RESET: checks functional-form problems.
- Recursive CUSUM: checks stability.
- Wald attenuation test: checks whether retail petrol pass-through and headline CPI pass-through are equal.

## Speaker notes

The tests are used to decide whether the estimates are reliable and whether the attenuation result is statistically supported.

---

# Backup slide 3: Safe answers for difficult questions

Use this only if asked difficult questions.

## Slide title

Backup: safe interpretation boundaries

## Slide content

If asked about causality:

> The models are reduced-form. I do not claim structural causality.

If asked about asymmetry:

> Asymmetry is tested, but it is not the main finding. Only retail petrol gives marginal evidence.

If asked why headline CPI is weak:

> Headline CPI is broad and includes many non-fuel items, so the oil signal is diluted.

If asked why samples differ:

> Data availability differs across WPI, CPI, PPAC petrol, and CPI Fuel and Light.

If asked the main result:

> Strong in fuel layers, weak in headline CPI. That is the attenuation result.

## Speaker notes

These answers help keep the interpretation careful and avoid overclaiming.

---

# Required figures from project

Use these exact figure paths if the PPT creation environment can access project files:

1. `models/cpi/outputs/figures/fig_13_dilution_chain.png`
   - Use on Slide 13.
   - Best figure for the main attenuation result.

2. `models/wpi/outputs/figures/fig_04_cumulative_passthrough.png`
   - Use on Slide 10 if readable.
   - If not readable, recreate a clean bar chart from the table values.

Optional figure:

3. `models/cpi/outputs/figures/fig_13b_dilution_common_sample.png`
   - Use only if there is space or if creating an appendix.

---

# Final instruction for Claude

Generate a polished PowerPoint using this blueprint. Keep the deck at 1 title slide, 11 numbered content slides, and 1 thank-you slide. Do not add speaker notes to the first title slide. Use simple academic English. Make the deck understandable even if the presenter speaks briefly. Do not add unsupported methods, causes, or results. Keep the technical content accurate but do not overload the main slides with secondary tests.
