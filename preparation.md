# Preparation Guide for External Evaluation

This file is for your personal preparation before presenting the dissertation.

You do not need to become an econometrics expert. Your goal is to understand the main ideas well enough to answer simple and medium-level questions confidently.

Main safety sentence:

> My study uses short-run asymmetric ADL models to estimate how oil shocks pass through different price layers in India. The main result is attenuation: strong effects in fuel-related layers and weak, statistically insignificant effects in headline CPI.

---

# 1. What you must know first

## 1.1 Your research topic in one sentence

Study this answer:

> I study how global oil-price shocks pass through India's price system, from wholesale and retail fuel prices to headline consumer inflation.

## 1.2 Your main research question

> How do global oil-price shocks transmit across India's wholesale, retail fuel, fuel-sensitive consumer, and headline consumer price layers, and where does this pass-through weaken?

## 1.3 Your main result

> Oil-price pass-through is strong in WPI Fuel and Power and retail petrol, smaller in CPI Fuel and Light, modest in headline WPI, and weak and statistically insignificant in headline CPI.

## 1.4 Your main contribution

> The dissertation treats oil pass-through as a layered transmission problem instead of only estimating one oil-to-CPI relationship.

## 1.5 What you should not claim

Do not say:

- Oil has no effect on CPI.
- WPI causes CPI in my model.
- Deregulation caused the post-2010 increase with full certainty.
- Granger causality proves true causality.
- My model is a long-run cointegration model.
- This is a NARDL or error-correction model.

Say instead:

- Headline CPI pass-through is weak and statistically insignificant.
- The layered map is an attenuation map, not one mechanical causal chain.
- The pre/post-2010 split is institutional evidence, not a clean causal experiment.
- Granger tests show predictive precedence, not structural causality.
- The model studies short-run monthly pass-through using ADL in log differences.

---

# 2. Core concepts to learn

Search these topics on YouTube or Google. Learn them in this order.

## Level 1: Basic economics concepts

### 1. Inflation

Search terms:

- `what is inflation economics simple explanation`
- `CPI and WPI difference India`
- `headline inflation vs core inflation`

What to understand:

- Inflation means the rate at which prices increase.
- CPI measures consumer prices.
- WPI measures wholesale prices.
- Headline inflation includes all items.

Simple answer:

> Inflation is the percentage increase in prices over time. CPI is closer to household prices, while WPI is closer to wholesale or producer-side prices.

### 2. Consumer Price Index, CPI

Search terms:

- `CPI India explained`
- `CPI basket India food weight fuel weight`
- `how CPI is calculated India`

What to understand:

- CPI is the main consumer inflation measure.
- It is used in India's inflation-targeting framework.
- It has many items, not only fuel.
- Food has a large weight, so oil effects can be diluted.

Simple answer:

> CPI is a broad consumer price index. Since it contains many non-fuel items, the oil shock may become weak at the headline CPI level.

### 3. Wholesale Price Index, WPI

Search terms:

- `WPI India explained`
- `difference between WPI and CPI India`
- `WPI Fuel and Power index India`

What to understand:

- WPI measures wholesale-level price changes.
- It is closer to producer costs than CPI.
- WPI Fuel and Power is a fuel-sensitive component.

Simple answer:

> WPI is more upstream than CPI. WPI Fuel and Power is close to the fuel channel, so it shows stronger oil pass-through.

### 4. Brent crude oil

Search terms:

- `Brent crude oil price explained`
- `why India uses Brent crude price`
- `global crude oil benchmark Brent explained`

What to understand:

- Brent is an international crude oil benchmark.
- Oil is priced in dollars.
- For India, domestic oil pressure also depends on exchange rate.

Simple answer:

> Brent is a global crude oil price benchmark. Since oil is priced in dollars, India faces the combined effect of Brent and the rupee-dollar exchange rate.

### 5. Exchange rate and rupee oil price

Search terms:

- `exchange rate pass through inflation simple explanation`
- `rupee depreciation oil import price India`
- `oil price in rupees formula Brent exchange rate`

What to understand:

- If Brent rises, import cost rises.
- If rupee depreciates, dollar oil becomes more expensive in rupees.
- Rupee oil price combines Brent and INR/USD.

Simple answer:

> Rupee oil price captures the domestic cost pressure from global oil because it combines Brent price and the exchange rate.

---

# 3. Econometrics concepts to learn

## 3.1 Time-series data

Search terms:

- `time series data econometrics simple explanation`
- `monthly time series analysis basics`
- `autocorrelation in time series simple explanation`

What to understand:

- Time-series data are observations over time.
- Monthly data often have persistence and seasonality.
- Errors may be correlated across months.

Simple answer:

> Time-series data are ordered over time. Because one month can be related to previous months, we need methods that handle lags and autocorrelation.

## 3.2 Log transformation

Search terms:

- `why use logs in economics regression`
- `log difference percentage change explanation`
- `natural log in econometrics simple explanation`

What to understand:

- Logs help interpret changes as approximate percentages.
- Log differences are close to growth rates or inflation rates.

Simple answer:

> I use log differences because they approximate monthly percentage changes. This makes the variables comparable as inflation or growth rates.

## 3.3 Stationarity

Search terms:

- `stationarity time series simple explanation`
- `why stationarity is important in time series regression`
- `unit root simple explanation econometrics`

What to understand:

- A stationary series has stable statistical behaviour over time.
- Many price levels are non-stationary.
- Log differences are usually more stable than levels.

Simple answer:

> Price levels often trend over time, so the dissertation uses log differences. This focuses on monthly changes and reduces the risk of spurious relationships.

## 3.4 OLS regression

Search terms:

- `OLS regression simple explanation`
- `ordinary least squares explained intuitively`
- `linear regression coefficients p values explained`

What to understand:

- OLS estimates coefficients by minimising squared prediction errors.
- Coefficients show average association, controlling for other variables.

Simple answer:

> OLS chooses the coefficient values that minimise the squared difference between actual and predicted inflation.

## 3.5 ADL model

Search terms:

- `autoregressive distributed lag model simple explanation`
- `ADL model econometrics lags explanation`
- `distributed lag model oil price pass through`

What to understand:

ADL means:

- Autoregressive: dependent variable uses its own lags.
- Distributed lag: explanatory shock uses current and lagged values.

Simple answer:

> ADL is useful because oil shocks may affect prices over several months, not only in the same month.

## 3.6 Lag length

Search terms:

- `lag length selection AIC BIC simple explanation`
- `AIC BIC HQIC time series model selection`
- `why use lags in time series regression`

What to understand:

- A lag means a previous month's value.
- Lag length decides how many past months enter the model.
- AIC/BIC/HQIC help choose lag length.

Simple answer:

> Lags are included because price adjustment takes time. Information criteria such as AIC help choose a reasonable lag length without adding too many unnecessary variables.

## 3.7 Asymmetric pass-through

Search terms:

- `asymmetric price transmission rockets and feathers`
- `oil price pass through asymmetry explanation`
- `positive and negative shocks econometrics`

What to understand:

- Prices may rise quickly when oil rises but fall slowly when oil falls.
- This is sometimes called rockets and feathers.
- Your study tests this, but asymmetry is not the main finding.

Simple answer:

> Asymmetry means prices may respond differently to oil price increases and decreases. In my study, strong asymmetry is not supported except marginally in retail petrol.

## 3.8 Cumulative pass-through, CPT

Search terms:

- `cumulative pass through coefficient distributed lag`
- `sum of lag coefficients interpretation`
- `oil price pass through cumulative effect`

What to understand:

- Oil effects are spread over lags.
- CPT sums those lag coefficients.
- CPT+ is for positive shocks.
- CPT- is for negative shocks.

Simple answer:

> CPT is the total estimated response across the lag window. It is useful because oil-price effects can be spread across several months.

## 3.9 p-value

Search terms:

- `p value simple explanation statistics`
- `statistical significance p value 0.05 explained`
- `how to interpret p values regression`

What to understand:

- p-value helps judge statistical evidence.
- p < 0.05 is commonly treated as significant.
- p > 0.05 means the estimate is not statistically distinguishable from zero at conventional levels.

Simple answer:

> A p-value tells us how strong the statistical evidence is. If the p-value is high, I do not treat the coefficient as statistically significant.

## 3.10 Newey-West HAC standard errors

Search terms:

- `Newey West standard errors simple explanation`
- `HAC standard errors autocorrelation heteroskedasticity`
- `why use Newey West in time series regression`

What to understand:

- Time-series residuals can have autocorrelation.
- Variance can change over time.
- HAC corrects standard errors for these issues.

Simple answer:

> Newey-West HAC standard errors make inference more reliable when residuals have autocorrelation or heteroscedasticity, which is common in monthly time-series data.

## 3.11 Diagnostics

Search terms:

- `regression diagnostics time series simple explanation`
- `Breusch Godfrey test explained`
- `Ramsey RESET test explained`
- `CUSUM stability test explained`
- `Breusch Pagan test explained`

What to understand:

Main diagnostic tests in the dissertation:

- Breusch-Godfrey: serial correlation check
- Breusch-Pagan: heteroscedasticity check
- HAC-RESET: functional-form check
- CUSUM: stability check

Simple answer:

> Diagnostics check whether the model is reliable enough for interpretation. If an alternative model fails important diagnostics, I do not use it for the main claim.

## 3.12 Bootstrap

Search terms:

- `bootstrap statistics simple explanation`
- `bootstrap p value regression explanation`
- `block bootstrap time series simple explanation`

What to understand:

- Bootstrap repeats the test many times using resampled data or residuals.
- Block bootstrap preserves time-series dependence better than random resampling.
- In your study, bootstrap checks symmetry robustness.

Simple answer:

> Bootstrap is a robustness check. It helps confirm whether the symmetry result depends too much on asymptotic assumptions.

## 3.13 Wald test

Search terms:

- `Wald test regression simple explanation`
- `linear restriction test econometrics`
- `test equality of coefficients regression`

What to understand:

- Wald test checks restrictions on coefficients.
- Your key use: test whether Stage 1 CPT+ equals Stage 3 CPT+.

Simple answer:

> A Wald test checks whether two estimated effects are statistically equal. In my study, it rejects equality between retail petrol pass-through and headline CPI pass-through.

## 3.14 Granger causality

Search terms:

- `Granger causality simple explanation`
- `Granger causality does not mean true causality`
- `predictive causality time series explained`

What to understand:

- Granger causality means past values of X help predict Y.
- It does not prove true structural causality.

Simple answer:

> I treat Granger tests as predictive precedence checks, not proof of structural causality.

## 3.15 Structural breaks

Search terms:

- `structural break time series simple explanation`
- `Bai Perron test explained simple`
- `oil price structural break econometrics`

What to understand:

- A structural break means the relationship changes over time.
- India's fuel pricing changed around 2010 and 2014.
- COVID was also an abnormal period.

Simple answer:

> A structural break means the model relationship may change across periods. This is why the dissertation treats the post-2010 fuel-pricing period carefully.

---

# 4. India-specific topics to learn

## 4.1 India's oil imports

Search terms:

- `India crude oil import dependence`
- `India oil imports and inflation`
- `oil price shock India economy`

What to understand:

- India imports most of its crude oil.
- Oil shocks can affect fuel prices, transport costs, production costs, and inflation.

Simple answer:

> India is exposed to global oil shocks because it imports a large share of its crude oil requirement.

## 4.2 Fuel pricing in India

Search terms:

- `petrol price deregulation India 2010`
- `diesel price deregulation India 2014`
- `fuel price deregulation India explained`
- `oil marketing companies petrol diesel pricing India`

What to understand:

- Petrol deregulation around June 2010.
- Diesel deregulation around October 2014.
- Market-linked pricing changed pass-through behaviour.

Simple answer:

> After deregulation, retail fuel prices became more linked to international prices, although taxes and policy decisions still matter.

## 4.3 Taxes on fuel

Search terms:

- `fuel taxes India excise VAT petrol diesel`
- `petrol price components India tax dealer commission`
- `why petrol price does not fall with crude India`

What to understand:

- Petrol/diesel prices include crude cost, refining/marketing margins, excise duty, VAT, and dealer commission.
- Taxes can weaken or delay pass-through.

Simple answer:

> Retail fuel prices do not move only with crude oil because taxes and margins are also important.

## 4.4 Inflation targeting in India

Search terms:

- `India flexible inflation targeting 2016 explained`
- `RBI inflation target CPI 4 percent`
- `monetary policy framework India CPI inflation`

What to understand:

- Since 2016, India has formal flexible inflation targeting.
- CPI is the main target variable.

Simple answer:

> CPI matters for policy because India uses CPI-based flexible inflation targeting.

---

# 5. Your exact model results to memorise

You do not need to memorise every decimal. But know the direction and approximate size.

## 5.1 Main result ranking

Memorise this order:

1. WPI Fuel and Power: about 0.52, strong and significant.
2. PPAC retail petrol: about 0.35, strong and significant.
3. CPI Fuel and Light: about 0.18, significant bridge evidence.
4. Headline WPI: about 0.03, modest but significant.
5. Headline CPI: about 0.02, weak and not significant.

Simple sentence:

> The fuel-related layers have much larger coefficients than headline indices.

## 5.2 Main results table

| Layer | CPT+ | p-value | Interpretation |
| --- | ---: | ---: | --- |
| WPI Fuel and Power | 0.5205 | <0.001 | Strong wholesale fuel pass-through |
| PPAC retail petrol | 0.3459 | <0.001 | Strong direct retail fuel pass-through |
| CPI Fuel and Light | 0.1777 | 0.0021 | Significant bridge evidence |
| Headline WPI | 0.0301 | 0.0240 | Modest but significant |
| Headline CPI | 0.0213 | 0.1220 | Weak, not statistically significant |

## 5.3 Attenuation test

Memorise:

- Stage 1: Brent -> PPAC petrol, CPT+ = 0.4007
- Stage 3: oil -> headline CPI, CPT+ = 0.0064
- Wald test: F = 14.3499, p = 0.0002
- Verdict: attenuation supported

Simple sentence:

> The formal Wald test rejects equality between retail petrol and headline CPI pass-through, so attenuation is statistically supported.

## 5.4 Asymmetry result

Memorise:

- Asymmetry is not the main finding.
- Retail petrol has marginal asymmetry, p = 0.0999.
- Main WPI, WPI Fuel and Power, and headline CPI do not reject symmetry.

Simple sentence:

> The study tests asymmetry, but the main finding is attenuation, not asymmetric pass-through.

---

# 6. Likely questions and safe answers

## Question 1: What is your dissertation about?

Safe answer:

> My dissertation studies how global oil-price shocks pass through India's price system. I compare wholesale, retail fuel, fuel-sensitive CPI, and headline CPI layers. The main finding is that pass-through is strong in fuel-related layers but weak in headline CPI.

## Question 2: Why did you choose this topic?

Safe answer:

> India imports a large amount of crude oil, so global oil shocks are important for inflation. But headline CPI does not always move strongly with oil. I wanted to understand where the oil effect becomes weaker.

## Question 3: What is pass-through?

Safe answer:

> Pass-through means how much of a change in oil prices is transmitted to domestic prices. For example, if oil rises, pass-through measures how much domestic fuel prices or inflation respond.

## Question 4: What does attenuation mean?

Safe answer:

> Attenuation means the effect becomes smaller as it moves across layers. In my study, oil shocks are strong in fuel layers but become much weaker in headline CPI.

## Question 5: What method did you use?

Safe answer:

> I used short-run asymmetric ADL models in log differences. The model includes past inflation and current and lagged oil shocks. Positive and negative oil shocks are estimated separately.

## Question 6: Why ADL and not another model?

Safe answer:

> ADL is suitable because oil-price effects may be distributed over several months. My research question is about short-run monthly pass-through, so ADL in log differences is appropriate.

## Question 7: Why not use NARDL or cointegration?

Safe answer:

> My dissertation focuses on short-run pass-through in monthly changes, not long-run equilibrium relationships. So I keep the design as ADL in log differences and do not make long-run cointegration claims.

## Question 8: What is the dependent variable?

Safe answer:

> It changes by layer. For headline CPI, the dependent variable is headline CPI inflation. For WPI models, it is WPI inflation or WPI Fuel and Power inflation. For retail petrol, it is petrol price inflation.

## Question 9: What is the shock variable?

Safe answer:

> For headline WPI, WPI Fuel and Power, and headline CPI, I use the rupee oil price shock. For retail petrol, I use Brent. For CPI Fuel and Light, I use PPAC retail petrol as the shock.

## Question 10: Why use rupee oil price?

Safe answer:

> Because India's domestic oil-cost pressure depends on both the international oil price and the exchange rate. Rupee oil price captures both Brent and INR/USD movements.

## Question 11: What is CPT+?

Safe answer:

> CPT+ is cumulative pass-through from positive oil shocks. It is the sum of the positive shock coefficients across the lag window.

## Question 12: What is CPT-?

Safe answer:

> CPT- is cumulative pass-through from negative oil shocks. It is the sum of the negative shock coefficients across the lag window.

## Question 13: What does p-value mean in your table?

Safe answer:

> The p-value shows whether the estimated effect is statistically distinguishable from zero. If the p-value is below 0.05, I treat it as statistically significant at the 5 percent level.

## Question 14: What is your strongest result?

Safe answer:

> The strongest result is the layered attenuation pattern. Fuel-related layers show strong pass-through, but headline CPI pass-through is weak and statistically insignificant. The formal Wald test supports this attenuation.

## Question 15: Why is headline CPI weak?

Safe answer:

> Headline CPI is a broad consumer basket. It includes many non-fuel items, especially food and services. Fuel shocks can be absorbed through taxes, margins, and basket weights, so the direct oil signal becomes diluted.

## Question 16: Does your result mean oil prices do not matter for consumers?

Safe answer:

> No. I do not say oil is irrelevant. I say the effect is strong in fuel-related layers but becomes weak and statistically insignificant in headline CPI.

## Question 17: What is asymmetry in your study?

Safe answer:

> Asymmetry means positive and negative oil shocks may have different effects. For example, prices may rise faster when oil rises than they fall when oil declines.

## Question 18: Did you find asymmetry?

Safe answer:

> Not strongly. Retail petrol gives marginal evidence at the 10 percent level, but the main WPI, WPI Fuel and Power, and headline CPI models do not reject symmetry. So asymmetry is not the central result.

## Question 19: Why did you exclude COVID months in WPI Fuel and Power?

Safe answer:

> April to September 2020 was an abnormal period with extreme oil-price movements and unusual pricing behaviour. Excluding those months improves diagnostics and gives a cleaner preferred estimate for the post-2010 market-linked period.

## Question 20: What are diagnostics?

Safe answer:

> Diagnostics check whether the model is reliable enough for interpretation. I use checks for serial correlation, functional form, heteroscedasticity, and stability.

## Question 21: What if a model fails diagnostics?

Safe answer:

> Then I do not use it for the main claim. For example, CPI M2 and M3 are not claim-bearing because diagnostics reject them.

## Question 22: What is Granger causality?

Safe answer:

> Granger causality means past values of one variable help predict another variable. It does not prove true structural causality, so I call it predictive precedence.

## Question 23: Is your study causal?

Safe answer:

> It is not a structural causal model. It is a reduced-form time-series study of pass-through patterns and predictive relationships.

## Question 24: What is reduced-form?

Safe answer:

> Reduced-form means I estimate the observed relationship between variables without fully modelling every structural mechanism behind price-setting.

## Question 25: Why do samples differ across models?

Safe answer:

> Data availability differs across WPI, CPI, PPAC petrol, and CPI Fuel and Light. I use the reliable available sample for each layer.

## Question 26: What is the policy implication?

Safe answer:

> Oil shocks matter most for fuel-sensitive layers, but their effect on headline CPI is diluted. Policymakers should monitor fuel-specific channels, not only the headline CPI response.

## Question 27: What is the main limitation?

Safe answer:

> The main limitation is that the models are reduced-form and different layers have different samples. So I interpret the results as a layered attenuation map, not a single structural causal chain.

## Question 28: What would you improve in future research?

Safe answer:

> Future work could use a structural model, state-level fuel price data, separate tax components, and more detailed CPI subcomponents to study the mechanism more deeply.

## Question 29: Why use monthly data?

Safe answer:

> Monthly data are suitable because fuel prices and inflation adjust over short periods. They also provide enough observations to estimate lagged pass-through.

## Question 30: What is your conclusion in one sentence?

Safe answer:

> Oil-price pass-through in India is layered: strong in fuel-related prices, but weak and statistically insignificant in headline CPI.

---

# 7. If you do not know the answer

Use these answers instead of guessing.

## If the question is outside your project

> I have not estimated that directly in this dissertation, so I should not overclaim. Based on my results, I can only say that the pass-through is stronger in fuel-related layers and weaker in headline CPI.

## If the question is too technical

> My understanding is limited to the model used in this dissertation. In this project, the point of that method is to handle lagged monthly pass-through and to test cumulative effects.

## If they ask for another model

> That would be a useful extension. My dissertation deliberately keeps the design short-run ADL only, because the research question is about monthly pass-through and attenuation across layers.

## If they challenge your English or explanation

> Sorry, let me say it more simply. The oil shock is strong near fuel prices, but it becomes weak when we reach broad headline CPI.

## If they ask a question you did not understand

> Sorry, could you please repeat the question slowly? I want to answer it correctly.

## If they ask why not include something

> That is a good point. I kept the dissertation focused on the main research question and avoided adding models that were outside the short-run ADL design.

---

# 8. Speaking practice script

Practise this 2-minute version first.

> My dissertation studies how global oil-price shocks pass through India's price system. India imports a large share of crude oil, and crude is priced internationally, so oil shocks can create domestic price pressure. But headline CPI does not always move strongly with oil prices. This is the puzzle of my research.
>
> I study this as a layered transmission problem. The main layers are WPI, WPI Fuel and Power, PPAC retail petrol, CPI Fuel and Light, and headline CPI. I use monthly data and short-run asymmetric ADL models in log differences. The model allows oil shocks to affect prices over several months and separates positive and negative shocks.
>
> The main result is attenuation. Pass-through is strong in WPI Fuel and Power and retail petrol. It is smaller in CPI Fuel and Light. It is modest in headline WPI, and weak and statistically insignificant in headline CPI. A formal Wald test also supports attenuation across the consumer-price chain.
>
> So my conclusion is not that oil prices are irrelevant. Instead, oil matters strongly near fuel-related prices, but the effect becomes diluted before reaching headline CPI.

Practise this 30-second version for confidence.

> My dissertation studies oil-price pass-through in India. I use short-run ADL models across WPI, retail petrol, CPI Fuel and Light, and headline CPI. The main finding is layered attenuation. Oil shocks pass strongly into fuel-related layers, but the effect becomes weak and statistically insignificant in headline CPI.

---

# 9. Words you should pronounce simply

Use these simpler pronunciations while practising.

- Econometrics: ee-ko-no-me-tricks
- Autoregressive: auto-regressive
- Distributed lag: distributed lag
- Asymmetric: a-sym-me-tric
- Cumulative: queue-mu-la-tive
- Pass-through: pass through
- Attenuation: a-ten-you-ay-shun
- Heteroscedasticity: he-te-ro-ske-das-ti-city
- Autocorrelation: auto-correlation
- Diagnostics: die-ag-nos-tics
- Cointegration: co-integration
- Newey-West: new-ee west
- Wald test: wald test
- Granger causality: grain-jer causality

If a word feels difficult, replace it:

- Instead of `attenuation`, say `the effect becomes weaker`.
- Instead of `heteroscedasticity`, say `changing error variance`.
- Instead of `autocorrelation`, say `errors are related across months`.
- Instead of `statistically insignificant`, say `not strong enough statistically`.

---

# 10. Final revision checklist before presentation

## Content checklist

- Can I state the research question in one sentence?
- Can I explain why oil matters for India?
- Can I explain WPI versus CPI?
- Can I explain ADL in simple words?
- Can I explain CPT+ and CPT-?
- Can I explain the main results table?
- Can I explain why headline CPI is weak?
- Can I explain attenuation?
- Can I state the limitations honestly?

## Slide checklist

- Does each slide have one clear message?
- Are the tables readable?
- Are the most important numbers highlighted?
- Is the conclusion slide simple?
- Are backup slides ready for ADL, CPI weakness, and difficult questions?

## Speaking checklist

- Practise the opening 3 times.
- Practise the main result 5 times.
- Practise the conclusion 3 times.
- Do not memorise long paragraphs.
- Speak slowly.
- Pause after important numbers.
- If nervous, read the slide and explain only one point.

---

# 11. Minimum topics to learn if time is short

If you have only one day, study only these:

1. CPI vs WPI difference
2. Brent crude and rupee oil price
3. Pass-through and attenuation
4. ADL model basics
5. Log differences
6. p-values and statistical significance
7. Newey-West HAC standard errors
8. CPT+ and CPT-
9. Diagnostics and why failed models are not used
10. Granger causality does not mean true causality

If you have three days, add:

1. AIC/BIC lag selection
2. Asymmetric price transmission
3. Wald test
4. Bootstrap
5. Structural breaks
6. Fuel pricing deregulation in India
7. Fuel taxes and retail petrol pricing
8. Inflation targeting in India

---

# 12. Final confidence note

You do not have to answer like a professor. You only need to answer like someone who understands their own project.

If you remember nothing else, remember this:

> Oil shocks are strong in fuel-related layers, but weak in headline CPI. My dissertation shows this using short-run ADL models and calls it layered attenuation.
