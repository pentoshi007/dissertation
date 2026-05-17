# PPT Blueprint for External Evaluation

Important: for creating the actual PPT with Claude, use `claude_ppt_blueprint.md`. That file is rewritten as a direct Claude-ready prompt with the ADL equation, objective, research question, data sources, model layers, key results, and only the important tests in the main slides.

Title: From wholesale prices to consumer inflation: layered pass-through of global oil shocks in India, 1983-2026

Recommended length: 12 main slides + 3 backup slides  
Recommended speaking time: 8 to 12 minutes  
Style: medium text, simple English, one main message per slide

## How to use this blueprint

- Keep the slides understandable even if you speak less.
- Use short sentences on the slide.
- Put the most important numbers directly on the slide.
- Do not try to explain every econometric detail unless asked.
- If an evaluator asks something difficult, answer from the safe answer lines in `preparation.md`.
- Do not mention NARDL, bounds testing, or error correction. This project is short-run ADL only.

## Overall presentation story

The whole presentation should say one clear thing:

> Oil shocks show clearly in fuel-related price layers, but the effect becomes much weaker when we reach headline CPI. This is attenuation, not absence.

The safe one-line answer to remember:

> My research finds strong pass-through in retail petrol and WPI Fuel and Power, medium pass-through in CPI Fuel and Light, modest pass-through in headline WPI, and weak, statistically insignificant pass-through in headline CPI.

---

# Slide 1: Title slide

## Slide title

From wholesale prices to consumer inflation: layered pass-through of global oil shocks in India, 1983-2026

## Put on the slide

- Name: Aniket Pandey
- Programme/Department: MS Economics
- University name
- External evaluation presentation
- Supervisor name, if required by university format

## Visual suggestion

- Simple background image or icon path:
  - Crude oil barrel -> petrol pump -> consumer basket
- Do not add too many logos or graphics.

## What to discuss

- Greet the evaluators.
- Say the topic in one simple sentence.

## Easy speaking lines

> Good morning respected evaluators. My dissertation studies how global oil-price shocks pass through different price layers in India. I focus on WPI, retail petrol, CPI Fuel and Light, and headline CPI.

## If you feel nervous

Only say:

> My topic is oil-price pass-through to inflation in India. I look at where the effect is strong and where it becomes weak.

---

# Slide 2: Motivation and problem

## Slide title

Why study oil-price pass-through in India?

## Put on the slide

- India imports a large part of its crude oil requirement.
- Crude oil is priced internationally, mainly in dollars.
- So domestic pressure depends on:
  - global Brent crude price
  - INR/USD exchange rate
- But headline CPI does not move one-for-one with oil prices.
- The puzzle is: where does the oil shock become weak?

## Suggested mini diagram

`Brent crude + INR/USD -> domestic fuel costs -> WPI/CPI inflation`

## What to discuss

- India is exposed to oil shocks.
- But broad inflation indices have many components.
- Food, services, taxes, margins, subsidies, and index weights can dilute the oil signal.

## Easy speaking lines

> India is exposed to global oil prices because crude oil is imported and priced in dollars. But headline CPI is a broad index. It includes food, services, housing, and many other items. So the oil effect may become diluted before reaching headline CPI.

## Possible evaluator question

**Question:** Why not study only headline CPI?  
**Safe answer:** Because headline CPI is the final consumer inflation index, but oil first affects fuel-related layers. If we only look at headline CPI, we may miss the stronger pass-through in retail petrol and fuel-sensitive prices.

---

# Slide 3: Research question and contribution

## Slide title

Research question

## Put on the slide

Research question:

> How do global oil-price shocks transmit across India's wholesale, retail fuel, fuel-sensitive consumer, and headline consumer price layers, and where does this pass-through weaken?

Contribution:

- Treats oil pass-through as a layered transmission problem.
- Does not estimate only one oil-to-CPI relationship.
- Compares five price layers:
  - Headline WPI
  - WPI Fuel and Power
  - PPAC retail petrol
  - CPI Fuel and Light
  - Headline CPI

## What to discuss

- This is not a single mechanical chain.
- It is a map across related price layers.
- The main contribution is showing attenuation across layers.

## Easy speaking lines

> The contribution of my dissertation is that I do not treat oil pass-through as only one relationship between oil and CPI. I study it layer by layer. This helps show where the effect is strong and where it becomes weak.

## Critical warning for you

Do not say:

> WPI causes CPI in my model.

Say instead:

> WPI and CPI are related layers, but each equation is estimated separately.

---

# Slide 4: Layered transmission map

## Slide title

Layered price transmission map

## Put on the slide

Consumer-side chain:

`Brent crude -> PPAC retail petrol -> CPI Fuel and Light -> Headline CPI`

Wholesale-side map:

`Rupee oil price -> WPI Fuel and Power -> Headline WPI`

Important note:

- Each layer is estimated as a separate ADL model.
- The map shows attenuation across related layers.
- It is not one single structural equation.

## Suggested visual

Create a two-row flow chart:

Row 1: Brent -> Retail petrol -> CPI Fuel and Light -> Headline CPI  
Row 2: Rupee oil -> WPI Fuel and Power -> Headline WPI

Use colours:

- Dark red for strong pass-through
- Orange for medium pass-through
- Light yellow/grey for weak pass-through

## What to discuss

- Explain that the consumer chain is the cleanest story.
- Explain that WPI gives the upstream/wholesale side.

## Easy speaking lines

> I divide the price system into layers. The consumer chain goes from Brent to retail petrol, then to CPI Fuel and Light, and then to headline CPI. The wholesale map uses rupee oil price, WPI Fuel and Power, and headline WPI. I estimate separate models for these layers.

---

# Slide 5: Data and variables

## Slide title

Data and variables

## Put on the slide

| Layer              | Dependent variable       | Shock variable    | Role                     |
| ------------------ | ------------------------ | ----------------- | ------------------------ |
| Headline WPI       | WPI inflation            | Rupee oil shock   | Main WPI result          |
| WPI Fuel and Power | Fuel and Power inflation | Rupee oil shock   | Wholesale fuel layer     |
| PPAC retail petrol | Delhi petrol inflation   | Brent shock       | Direct retail fuel layer |
| CPI Fuel and Light | Fuel and Light inflation | PPAC petrol shock | Consumer fuel bridge     |
| Headline CPI       | CPI inflation            | Rupee oil shock   | Consumer endpoint        |

Other information:

- Frequency: monthly data
- Main transformation: log differences
- Log differences are used as monthly inflation or percentage change.

## What to discuss

- Keep this slide practical.
- Tell evaluators what is dependent variable and what is shock variable.
- Mention different samples only if asked, or put small footnote.

## Easy speaking lines

> I use monthly data. Most variables are converted into log differences, which means monthly percentage changes. The dependent variable changes by layer. For example, in the headline CPI model, CPI inflation is the dependent variable and the rupee oil shock is the explanatory shock.

## Optional footnote

Samples differ because all series are not available for the same full period.

---

# Slide 6: Methodology in simple language

## Slide title

Methodology: short-run asymmetric ADL model

## Put on the slide

ADL means Autoregressive Distributed Lag:

- Autoregressive: inflation depends on its own past values.
- Distributed lag: oil shocks can affect prices over several months.
- Asymmetric: positive and negative oil shocks enter separately.
- Short-run: the model studies monthly changes, not long-run cointegration.

Basic idea:

`Current inflation = past inflation + current and past oil shocks + controls + error`

## Small equation to put on slide

`Δy_t = past Δy + positive Δx shocks + negative Δx shocks + controls + error`

## What to discuss

- Do not spend too much time on equation.
- Explain what ADL does in plain language.
- Say OLS estimates the coefficients.

## Easy speaking lines

> I use a short-run asymmetric ADL model. This means current inflation is explained by its own past values and by current and past oil shocks. Positive and negative shocks are kept separate, so I can check whether prices respond differently to oil increases and decreases.

## Possible evaluator question

**Question:** Why ADL?  
**Safe answer:** Because oil-price effects may not appear fully in the same month. ADL allows the effect to spread across several monthly lags.

---

# Slide 7: Inference and key terms

## Slide title

How the results are tested

## Put on the slide

Main reported terms:

- `CPT+`: cumulative pass-through from positive oil shocks
- `CPT-`: cumulative pass-through from negative oil shocks
- `p-value`: shows whether the estimate is statistically distinguishable from zero
- `Asymmetry p`: tests whether `CPT+ = CPT-`
- Newey-West HAC standard errors: used because time-series errors may have autocorrelation and changing variance

Interpretation rule:

- If p < 0.05: statistically significant at 5 percent
- If p > 0.05: not statistically significant at conventional levels

## What to discuss

- This slide helps evaluators understand the table later.
- Keep it simple.

## Easy speaking lines

> I report cumulative pass-through because the effect of oil can be spread across months. CPT plus is the sum of positive-shock effects. CPT minus is the sum of negative-shock effects. I use Newey-West HAC standard errors because this is monthly time-series data.

## If asked about HAC

> HAC is a correction for standard errors. It makes inference more reliable when residuals have autocorrelation or heteroscedasticity.

---

# Slide 8: Main results table

## Slide title

Main results: pass-through by layer

## Put on the slide

| Layer              | Sample             |   N |   CPT+ |      p |   CPT- |      p | Asym. p | Verdict                     |
| ------------------ | ------------------ | --: | -----: | -----: | -----: | -----: | ------: | --------------------------- |
| WPI Fuel and Power | 2010-04 to 2026-03 | 186 | 0.5205 | <0.001 | 0.4195 | <0.001 |  0.1642 | Strong wholesale fuel layer |
| PPAC retail petrol | 2004-08 to 2024-12 | 245 | 0.3459 | <0.001 | 0.1912 | 0.0002 |  0.0999 | Strong direct fuel layer    |
| CPI Fuel and Light | 2011-05 to 2024-12 | 164 | 0.1777 | 0.0021 | 0.1058 | 0.1741 |  0.4554 | Bridge evidence             |
| Headline WPI       | 1983-05 to 2026-03 | 515 | 0.0301 | 0.0240 | 0.0374 | 0.0012 |  0.6727 | Modest but significant      |
| Headline CPI       | 2004-08 to 2024-12 | 245 | 0.0213 | 0.1220 | 0.0006 | 0.9375 |  0.2408 | Weak, not significant       |

## Design instruction

- Use small font but keep table readable.
- Highlight `WPI Fuel and Power`, `PPAC retail petrol`, and `Headline CPI` rows.
- Add a short takeaway box below the table.

Takeaway box:

> Fuel-related layers show strong pass-through. Headline CPI shows weak and statistically insignificant pass-through.

## What to discuss

- Do not read every number.
- Explain the ranking.
- State that asymmetry is not the main finding.

## Easy speaking lines

> This table gives the main result. Pass-through is strongest in WPI Fuel and Power and retail petrol. It is smaller in CPI Fuel and Light. It becomes very small in headline WPI and headline CPI. The headline CPI coefficient is positive, but it is not statistically significant.

---

# Slide 9: Wholesale results

## Slide title

Wholesale layer: WPI results

## Put on the slide

Headline WPI:

- Sample: 1983-05 to 2026-03
- CPT+ = 0.0301, p = 0.0240
- CPT- = 0.0374, p = 0.0012
- Interpretation: modest but statistically significant

WPI Fuel and Power, preferred model:

- Sample: 2010-04 to 2026-03, excluding COVID months
- CPT+ = 0.5205, p < 0.001
- CPT- = 0.4195, p < 0.001
- Interpretation: strong wholesale fuel pass-through

## Figure/table to put

Use one of these:

- `models/wpi/outputs/figures/fig_04_cumulative_passthrough.png`
- Or a clean two-row table if the figure is too crowded.

## What to discuss

- WPI Fuel and Power is much closer to fuel items.
- Headline WPI is broad, so the oil signal is diluted.
- Preferred Fuel and Power model excludes COVID months because COVID distorted usual pricing behaviour.

## Easy speaking lines

> The wholesale results show that oil clearly affects fuel-sensitive wholesale prices. WPI Fuel and Power has a large and significant response. Headline WPI also responds, but the size is much smaller because headline WPI is a broader index.

## Safe line if asked about COVID exclusion

> COVID months were unusual because oil prices and administered pricing behaviour were abnormal. Excluding April to September 2020 improves the model diagnostics and gives the preferred wholesale fuel estimate.

---

# Slide 10: Retail petrol and CPI Fuel and Light

## Slide title

Consumer fuel layers: petrol and CPI Fuel and Light

## Put on the slide

PPAC retail petrol:

- Shock: Brent crude price
- CPT+ = 0.3459, p < 0.001
- CPT- = 0.1912, p = 0.0002
- Asymmetry p = 0.0999
- Interpretation: strong direct fuel pass-through, asymmetry only marginal

CPI Fuel and Light:

- Shock: PPAC retail petrol
- CPT+ = 0.1777, p = 0.0021
- CPT- = 0.1058, p = 0.1741
- Interpretation: bridge evidence from retail fuel to consumer fuel category

## What to discuss

- Retail petrol is the direct fuel layer.
- CPI Fuel and Light is the consumer fuel bridge.
- CPI Fuel and Light sample is shorter, so call it supporting bridge evidence.

## Easy speaking lines

> Retail petrol responds strongly to Brent shocks. CPI Fuel and Light also responds to retail petrol, but the size is smaller. This supports the idea that the oil shock moves from direct fuel prices into the fuel-sensitive part of the consumer basket.

## Safe line about asymmetry

> The retail petrol asymmetry result is only marginal at the 10 percent level, so I treat it as suggestive, not a strong conclusion.

---

# Slide 11: Headline CPI and attenuation

## Slide title

Headline CPI: where the oil signal becomes weak

## Put on the slide

Headline CPI result:

- Sample: 2004-08 to 2024-12
- N = 245
- CPT+ = 0.0213, p = 0.1220
- CPT- = 0.0006, p = 0.9375
- Asymmetry p = 0.2408

Interpretation:

- Positive sign is expected.
- But it is not statistically significant.
- This supports attenuation.
- It does not mean oil is irrelevant.

## Figure to put

Use:

`models/cpi/outputs/figures/fig_13_dilution_chain.png`

Caption:

> Cumulative positive pass-through across the consumer-price chain

## What to discuss

- This is the most important result for your conclusion.
- Say “weak and statistically insignificant”, not “zero”.

## Easy speaking lines

> Headline CPI is the final consumer inflation layer. Here the oil coefficient is positive but not statistically significant. So my conclusion is not that oil has no effect. My conclusion is that the effect becomes weak at the headline CPI level.

---

# Slide 12: Formal attenuation test

## Slide title

Formal test of attenuation

## Put on the slide

Common-sample consumer chain:

| Stage   | Relationship                      |   CPT+ | p-value |
| ------- | --------------------------------- | -----: | ------: |
| Stage 1 | Brent -> PPAC retail petrol       | 0.4007 |  0.0001 |
| Stage 2 | PPAC petrol -> CPI Fuel and Light | 0.1777 |  0.0021 |
| Stage 3 | Rupee oil -> Headline CPI         | 0.0064 |  0.6355 |

Wald test:

- H0: Stage 1 CPT+ = Stage 3 CPT+
- F = 14.3499
- p = 0.0002
- Verdict: reject equality

Conclusion:

> Attenuation is statistically supported.

## Figure to put

Use:

`models/cpi/outputs/figures/fig_13b_dilution_common_sample.png`

If the slide gets crowded, use either the table or the figure, not both.

## What to discuss

- Explain that the test formally compares the first and final consumer-chain stages.
- Since p = 0.0002, the difference is statistically supported.

## Easy speaking lines

> To make the attenuation argument formal, I compare the first and final stages of the consumer chain. The Wald test rejects equality between retail petrol pass-through and headline CPI pass-through. This supports the attenuation result statistically.

---

# Slide 13: Robustness and diagnostics

## Slide title

Robustness and diagnostic checks

## Put on the slide

Main checks:

- Headline WPI diagnostics pass.
- Preferred WPI Fuel and Power model passes after using post-2010 sample and excluding COVID months.
- Headline CPI M1 passes the mandatory model gate.
- PPAC retail petrol model passes the mandatory mechanism gate.
- Bootstrap symmetry checks do not make asymmetry the main finding.
- CPI M2 and M3 are not used for main claims because diagnostics reject them.
- Granger tests are used only as predictive precedence checks, not structural causality.

## What to discuss

- This slide reassures evaluators that you did not pick numbers randomly.
- Do not explain every diagnostic unless asked.

## Easy speaking lines

> I also checked the models using diagnostics. The main WPI, headline CPI, and PPAC retail petrol models pass their important gates. Some alternative CPI models fail diagnostics, so I do not use them for main claims. This is why the final results are based on the accepted model hierarchy.

## Safe line about Granger causality

> Granger causality only means predictive precedence. It does not prove deep structural causality.

---

# Slide 14: Limitations

## Slide title

Limitations

## Put on the slide

- The models are reduced-form projections, not structural causal estimates.
- Different layers have different sample periods.
- CPI Fuel and Light has a shorter sample, so it is bridge evidence.
- PPAC retail petrol uses Delhi petrol prices as a retail fuel proxy.
- The pre/post-2010 split is institutional evidence, not a clean deregulation experiment.
- The layered map is not a single mechanical WPI-to-CPI causal chain.

## What to discuss

- Say limitations confidently.
- Limitations make the study more honest, not weaker.

## Easy speaking lines

> My study has some limitations. The models are reduced-form, so I do not claim structural causality. Also, the layers have different sample lengths. CPI Fuel and Light is treated as bridge evidence because its sample starts later. These limitations are kept in mind while interpreting the results.

## If evaluator challenges causality

> Yes, that is a fair point. My study estimates pass-through associations and predictive relationships. It does not claim a structural causal model.

---

# Slide 15: Conclusion

## Slide title

Conclusion

## Put on the slide

Main answer:

> Oil-price pass-through in India is layered and attenuated.

Key findings:

- Strong in WPI Fuel and Power and PPAC retail petrol.
- Visible but smaller in CPI Fuel and Light.
- Modest but significant in headline WPI.
- Weak and statistically insignificant in headline CPI.
- Formal Wald test supports attenuation.
- Asymmetry is not the central result.

Final implication:

> Oil shocks matter for fuel-related prices, but broad headline inflation absorbs and dilutes much of the shock.

## What to discuss

- End calmly.
- Do not add new results.
- Thank the evaluators.

## Easy speaking lines

> To conclude, my dissertation finds that oil shocks matter, but their effect is not uniform across the price system. The effect is strong in fuel-related layers and becomes weak in headline CPI. So the main result is layered attenuation.

Final line:

> Thank you. I am happy to take your questions.

---

# Backup slide A: What is ADL?

Use only if asked.

## Put on the slide

ADL = Autoregressive Distributed Lag

- Current inflation depends on past inflation.
- Oil shocks can affect inflation over more than one month.
- Positive and negative shocks are entered separately.
- Estimated using OLS.

Simple answer:

> ADL is useful here because price transmission takes time.

---

# Backup slide B: Why headline CPI response is weak

Use only if asked.

## Put on the slide

Reasons headline CPI pass-through can be weak:

- CPI basket is broad and food-heavy.
- Fuel has limited direct weight in headline CPI.
- Taxes and margins can absorb part of oil shocks.
- Government pricing and excise decisions can smooth retail prices.
- Monetary and demand conditions also affect inflation.

Simple answer:

> Oil affects fuel prices strongly, but headline CPI includes many non-fuel items, so the total CPI response becomes diluted.

---

# Backup slide C: Safe answers for difficult questions

Use only if asked or keep printed for yourself.

## Put on the slide

If asked about causality:

> My models are reduced-form. I do not claim structural causality.

If asked about asymmetry:

> Asymmetry is not the main finding. Only retail petrol gives marginal evidence at the 10 percent level.

If asked why samples differ:

> Data availability differs across WPI, CPI, PPAC petrol, and CPI Fuel and Light. So each model uses the reliable available sample for that layer.

If asked why not long-run model:

> The dissertation focuses on short-run monthly pass-through. Therefore I use log-difference ADL models, not long-run cointegration models.

If asked the main result:

> Strong in fuel layers, weak in headline CPI. That is the attenuation result.

---

# Suggested slide design

## Colour palette

- Dark navy for titles
- White or very light grey background
- Red/orange for strong pass-through
- Yellow for medium pass-through
- Grey/blue for weak pass-through

## Fonts

- Title: 30 to 36 pt
- Main bullets: 20 to 24 pt
- Tables: 12 to 16 pt, but readable
- Speaker notes: not on slide, keep in presenter notes

## Layout rules

- Use 4 to 6 bullets per slide.
- Use one table or one figure per slide.
- Do not put large paragraphs.
- Put the easy speaking line in presenter notes.
- Highlight only the most important numbers.

## Recommended figures from project

Use these figures if you make the actual PPT:

1. `models/cpi/outputs/figures/fig_13_dilution_chain.png`
   - Best figure for the main result.
2. `models/cpi/outputs/figures/fig_13b_dilution_common_sample.png`
   - Best figure for the formal common-sample attenuation story.
3. `models/wpi/outputs/figures/fig_04_cumulative_passthrough.png`
   - Useful for wholesale pass-through.
4. `models/wpi/outputs/figures/fig_05_subsample_comparison.png`
   - Use only if evaluator is interested in pre/post-2010 split.

## Recommended final slide count

If you want 10 slides, remove:

- Slide 7: Inference and key terms
- Slide 12: Formal attenuation test
- Slide 13: Robustness and diagnostics
- Put one sentence from each into other slides.

If you want 12 slides, use:

- Slides 1 to 12 only.

If you want 15 slides, use:

- Slides 1 to 15.

## Most important slides for your confidence

Memorise these four slides best:

- Slide 3: Research question
- Slide 8: Main results table
- Slide 11: Headline CPI and attenuation
- Slide 15: Conclusion

If you forget something, return to this sentence:

> The effect is strong in fuel layers and weak in headline CPI, so the main finding is attenuation.
