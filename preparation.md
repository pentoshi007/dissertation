# Simple Presentation Guide for External Evaluation

This is a single, beginner-friendly guide. Every concept is explained in plain English with an everyday example. Read it slowly. You do not need to memorise it. You only need to understand it well enough to talk about your own work.

The one sentence that protects you in any tough moment:

> My study uses short-run asymmetric ADL models to estimate how oil shocks pass through different price layers in India. The main result is attenuation: strong effects in fuel-related layers and weak, statistically insignificant effects in headline CPI.

If you forget everything else, remember this:

> Oil shocks are strong in fuel-related prices like petrol and WPI Fuel and Power, but become weak by the time they reach the broad headline CPI that the average household sees.

---

# 1. What your dissertation is about (in simple words)

## 1.1 The topic in one sentence

> I study how global oil-price shocks pass through India's price system, from wholesale and retail fuel prices to headline consumer inflation.

**Everyday example:** Imagine a stone dropped in a pond. The splash near the stone is huge, but by the time the ripples reach the edge of the pond, they are tiny. The stone is the global oil shock. The big splash is wholesale fuel price. The tiny ripple at the edge is headline CPI.

## 1.2 The main research question

> How do global oil-price shocks transmit across India's wholesale, retail fuel, fuel-sensitive consumer, and headline consumer price layers, and where does this pass-through weaken?

**In plain words:** When global oil prices change, which Indian prices feel it strongly, which feel it weakly, and where does the effect basically die out?

## 1.3 The main result

> Oil-price pass-through is strong in WPI Fuel and Power and retail petrol, smaller in CPI Fuel and Light, modest in headline WPI, and weak and statistically insignificant in headline CPI.

**Plain words:** Oil shocks hit fuel prices hard. By the time we look at the overall consumer inflation that families talk about, the effect almost disappears in our data.

## 1.4 The main contribution

> The dissertation treats oil pass-through as a layered transmission problem instead of only estimating one oil-to-CPI relationship.

**Plain words:** Many studies jump straight from oil to CPI. I look at the steps in between, like climbing down a staircase, so we can see exactly which step absorbs the shock.

## 1.5 Things you must NOT say (and what to say instead)

Do not say:

- "Oil has no effect on CPI."
- "WPI causes CPI in my model."
- "Deregulation caused the post-2010 increase with full certainty."
- "Granger causality proves true causality."
- "My model is a long-run cointegration model."
- "This is a NARDL or error-correction model."

Say instead:

- "Headline CPI pass-through is weak and statistically insignificant."
- "The layered map is an attenuation map, not one mechanical causal chain."
- "The pre/post-2010 split is institutional evidence, not a clean causal experiment."
- "Granger tests show predictive precedence, not structural causality."
- "The model studies short-run monthly pass-through using ADL in log differences."

---

# 2. Basic economics concepts, explained simply

## 2.1 Inflation

**What it means:** The rate at which prices rise over time.

**Example:** Last year a packet of biscuits cost Rs 20. This year it costs Rs 22. That is 10% inflation for that biscuit.

**Simple answer to give:**

> Inflation is the percentage increase in prices over time. CPI is closer to household prices, while WPI is closer to wholesale or producer-side prices.

## 2.2 CPI (Consumer Price Index)

**What it means:** A basket of things a typical household buys (food, rent, clothes, fuel, transport, etc). The government tracks how the price of this basket changes.

**Example:** Think of one big "shopping bag" filled with rice, dal, vegetables, petrol, school fees, etc. CPI tracks the total cost of that bag every month.

**Key point:** Food and services are large parts of this bag, so fuel is only one slice. That is why oil shocks can look small in headline CPI.

**Simple answer:**

> CPI is a broad consumer price index. Since it contains many non-fuel items, the oil shock may become weak at the headline CPI level.

## 2.3 WPI (Wholesale Price Index)

**What it means:** Prices at the wholesale level, before goods reach the final consumer.

**Example:** The price a petrol pump pays for fuel from the oil company is closer to WPI. The price you pay at the pump, with taxes, is closer to CPI.

**Simple answer:**

> WPI is more upstream than CPI. WPI Fuel and Power is close to the fuel channel, so it shows stronger oil pass-through.

## 2.4 Brent crude oil

**What it means:** A global benchmark price for crude oil. Most international oil trade is quoted near this price.

**Example:** When you see "oil is at $80 a barrel" on the news, that is usually Brent.

**Simple answer:**

> Brent is a global crude oil price benchmark. Since oil is priced in dollars, India faces the combined effect of Brent and the rupee-dollar exchange rate.

## 2.5 Exchange rate and rupee oil price

**What it means:** Oil is bought in US dollars. India pays in rupees. So the cost of oil in India depends on both the dollar price of oil AND the rupee-dollar rate.

**Example:** Brent is $80. If 1 dollar = Rs 80, then a barrel costs Rs 6400. If the rupee weakens to Rs 90 per dollar, the same barrel now costs Rs 7200, even though the dollar price did not change.

**Simple answer:**

> Rupee oil price captures the domestic cost pressure from global oil because it combines Brent price and the exchange rate.

---

# 3. Econometrics concepts, explained simply

## 3.1 Time-series data

**What it means:** Data collected over time, in order. For example, monthly inflation from 1983 to 2026.

**Example:** A patient's temperature recorded every hour is a time series. Today's temperature is related to last hour's.

**Simple answer:**

> Time-series data are ordered over time. Because one month can be related to previous months, we need methods that handle lags and autocorrelation.

## 3.2 Log transformation

**What it means:** Taking the natural log of a price. When we take the difference of two logs, we get something close to a percentage change.

**Example:** If CPI goes from 100 to 105, log(105) - log(100) ≈ 0.0488, which is close to 4.88% (the actual percentage change). So log differences behave like growth rates.

**Simple answer:**

> I use log differences because they approximate monthly percentage changes. This makes the variables comparable as inflation or growth rates.

## 3.3 Stationarity

**What it means:** A series whose average and variance do not drift over time.

**Example:** The price level of petrol keeps going up over decades, so it is not stationary. But monthly _changes_ in petrol prices wobble around a roughly stable average, so they are closer to stationary.

**Simple answer:**

> Price levels often trend over time, so the dissertation uses log differences. This focuses on monthly changes and reduces the risk of spurious relationships.

## 3.4 OLS regression

**What it means:** A standard method that draws the best straight-line relationship between variables by minimising squared errors.

**Example:** If we plot ice-cream sales against temperature, OLS draws the line that best fits the dots.

**Simple answer:**

> OLS chooses the coefficient values that minimise the squared difference between actual and predicted inflation.

## 3.5 ADL model (Autoregressive Distributed Lag)

**What it means:**

- Autoregressive: today's inflation depends on its own past values.
- Distributed lag: today's inflation also depends on current AND past values of the shock (oil).

**Example:** If oil jumps today, the effect on Indian inflation may show up partly this month, partly next month, partly two months later. ADL lets all those months matter.

**Simple answer:**

> ADL is useful because oil shocks may affect prices over several months, not only in the same month.

## 3.6 Lag length

**What it means:** How many past months we include. AIC, BIC, HQIC are formulas that help us pick a good number.

**Example:** If we use 3 lags, we say oil from this month, last month, two months ago, and three months ago can all affect today's inflation.

**Simple answer:**

> Lags are included because price adjustment takes time. Information criteria such as AIC help choose a reasonable lag length without adding too many unnecessary variables.

## 3.7 Asymmetric pass-through ("rockets and feathers")

**What it means:** Prices may shoot up like rockets when oil rises, but drift down like feathers when oil falls.

**Example:** When crude jumps, petrol pumps revise prices in days. When crude falls, the cut at the pump can be slower and smaller.

**Simple answer:**

> Asymmetry means prices may respond differently to oil price increases and decreases. In my study, strong asymmetry is not supported except marginally in retail petrol.

## 3.8 Cumulative pass-through (CPT)

**What it means:** Add up the effect across all the lag months to get the total response.

**Example:** Suppose a 10% oil shock raises WPI Fuel and Power by 3% this month, 1.5% next month, and 0.7% the month after. CPT is 3 + 1.5 + 0.7 = 5.2% total. As a fraction of the 10% oil shock, that is 0.52, similar to your number.

- CPT+ = total response to positive oil shocks.
- CPT- = total response to negative oil shocks.

**Simple answer:**

> CPT is the total estimated response across the lag window. It is useful because oil-price effects can be spread across several months.

## 3.9 p-value

**What it means:** A number between 0 and 1 that tells us how surprised we should be if the true effect were really zero.

**Example:** p = 0.001 means: if oil really had no effect, seeing a result this strong would happen only 1 in 1000 times by chance. That is strong evidence of a real effect. p = 0.40 means we cannot rule out that the result is just noise.

**Common rule:** p < 0.05 is treated as statistically significant.

**Simple answer:**

> A p-value tells us how strong the statistical evidence is. If the p-value is high, I do not treat the coefficient as statistically significant.

## 3.10 Newey-West HAC standard errors

**What it means:** A correction we apply to standard errors when monthly residuals are correlated across time or have changing variance. It makes p-values trustworthy.

**Example:** Like adjusting your weighing scale for a slight tilt. The number was always there, but now it is more reliable.

**Simple answer:**

> Newey-West HAC standard errors make inference more reliable when residuals have autocorrelation or heteroscedasticity, which is common in monthly time-series data.

## 3.11 Diagnostics

**What it means:** Routine health checks for a regression model.

- Breusch-Godfrey: are residuals correlated across months?
- Breusch-Pagan: does the variance of residuals change over time?
- HAC-RESET: is the functional form (the shape of the relationship) okay?
- CUSUM: is the relationship stable, or does it break across periods?

**Example:** Like blood tests before declaring a patient healthy. If a model fails important tests, we do not trust its main story.

**Simple answer:**

> Diagnostics check whether the model is reliable enough for interpretation. If an alternative model fails important diagnostics, I do not use it for the main claim.

## 3.12 Bootstrap

**What it means:** A robustness check that resamples the data many times to see if the conclusion holds.

**Example:** Like asking the same question to 1000 randomly drawn groups instead of just one and checking that the answer stays similar.

**Block bootstrap:** Resamples in blocks of consecutive months, to preserve time-series structure.

**Simple answer:**

> Bootstrap is a robustness check. It helps confirm whether the symmetry result depends too much on asymptotic assumptions.

## 3.13 Wald test

**What it means:** A test that checks whether two coefficients (or combinations of them) are statistically equal.

**Example:** In your work, the Wald test checks: "Is retail petrol's pass-through equal to headline CPI's pass-through?" The answer is no, with F = 14.35 and p = 0.0002, which strongly supports attenuation.

**Simple answer:**

> A Wald test checks whether two estimated effects are statistically equal. In my study, it rejects equality between retail petrol pass-through and headline CPI pass-through.

## 3.14 Granger causality

**What it means:** If past values of X help predict Y better than Y's own past alone, we say X "Granger-causes" Y. This is about prediction, not real-world cause.

**Example:** Dark clouds Granger-cause rain in the sense that clouds appear first and help predict rain. But clouds do not physically cause rain in the deep sense, they are a sign of it.

**Simple answer:**

> I treat Granger tests as predictive precedence checks, not proof of structural causality.

## 3.15 Structural breaks

**What it means:** Points in time when the relationship in the data changes, so a single equation may not fit the whole sample.

**Example:** India deregulated petrol pricing in June 2010 and diesel in October 2014. Before deregulation, retail fuel prices were administered. After it, they tracked international prices more closely. The relationship "changed shape" around those dates.

**Simple answer:**

> A structural break means the model relationship may change across periods. This is why the dissertation treats the post-2010 fuel-pricing period carefully.

---

# 4. India-specific topics, explained simply

## 4.1 India's oil imports

**Fact:** India imports roughly 80%+ of its crude oil.

**Why it matters:** If global oil rises, India pays more in dollars and feels cost pressure across fuel, transport, fertiliser, plastics, and many other goods.

**Simple answer:**

> India is exposed to global oil shocks because it imports a large share of its crude oil requirement.

## 4.2 Fuel pricing in India

**Key dates to remember:**

- June 2010: petrol prices deregulated.
- October 2014: diesel prices deregulated.

**What changed:** Before deregulation, the government fixed retail fuel prices. After deregulation, oil marketing companies adjusted prices closer to international moves (with taxes still applied).

**Simple answer:**

> After deregulation, retail fuel prices became more linked to international prices, although taxes and policy decisions still matter.

## 4.3 Taxes on fuel

**What you pay at the pump =** crude oil cost + refining + marketing margin + excise duty (central tax) + VAT (state tax) + dealer commission.

**Example:** If crude rises by Rs 5, the pump price may rise by less than Rs 5 if margins absorb part of it, or by more if taxes are ad-valorem. When crude falls, taxes can hold the pump price up.

**Simple answer:**

> Retail fuel prices do not move only with crude oil because taxes and margins are also important.

## 4.4 Inflation targeting in India

**Fact:** Since 2016, RBI follows flexible inflation targeting with a CPI target of 4% (with a 2-6% band).

**Why it matters:** CPI is the headline number for policy, which is exactly the layer where your study finds weak pass-through.

**Simple answer:**

> CPI matters for policy because India uses CPI-based flexible inflation targeting.

---

# 5. Your exact results to remember

You do not have to memorise decimals. Know the _direction_ and _rough size_.

## 5.1 The ranking (memorise this order)

1. **WPI Fuel and Power:** about 0.52, strong and significant.
2. **PPAC retail petrol:** about 0.35, strong and significant.
3. **CPI Fuel and Light:** about 0.18, significant bridge evidence.
4. **Headline WPI:** about 0.03, modest but significant.
5. **Headline CPI:** about 0.02, weak and not significant.

One-line story:

> The fuel-related layers have much larger coefficients than headline indices.

## 5.2 Main results table

| Layer              |   CPT+ | p-value | What it means                          |
| ------------------ | -----: | ------: | -------------------------------------- |
| WPI Fuel and Power | 0.5205 |  <0.001 | Strong wholesale fuel pass-through     |
| PPAC retail petrol | 0.3459 |  <0.001 | Strong direct retail fuel pass-through |
| CPI Fuel and Light | 0.1777 |  0.0021 | Significant bridge evidence            |
| Headline WPI       | 0.0301 |  0.0240 | Modest but significant                 |
| Headline CPI       | 0.0213 |  0.1220 | Weak, not statistically significant    |

**How to read 0.5205:** A 1% positive shock in rupee oil is associated with about a 0.52% cumulative increase in WPI Fuel and Power across the lag window.

## 5.3 The attenuation Wald test

- Stage 1: Brent -> PPAC petrol, CPT+ = 0.4007
- Stage 3: oil -> headline CPI, CPT+ = 0.0064
- Wald test: F = 14.3499, p = 0.0002
- Verdict: attenuation supported

**What F = 14.3499 means in plain words:**

The F-statistic is a single number that measures how far apart two estimates are, scaled by how noisy they are. Think of it as a "distance score." A small F (close to 1) means the two estimates could easily be equal. A big F means they are far apart relative to the noise.

In your case, the test is asking: "Is the retail petrol pass-through (0.4007) really equal to the headline CPI pass-through (0.0064)?"

- Under the null hypothesis "they are equal," F would normally hover near 1.
- You got F = 14.35, which is much bigger than 1.
- That tells us the gap between 0.40 and 0.006 is far too large to be just statistical noise.

**What p = 0.0002 means in plain words:**

If the two pass-throughs were truly equal, the chance of seeing a gap this large (or larger) just by random luck would be only 0.0002, that is 2 in 10,000.

That is extremely small, much smaller than the usual 0.05 cut-off. So we confidently reject "they are equal" and conclude that retail petrol pass-through is genuinely much larger than headline CPI pass-through. This is exactly what "attenuation" means: the effect shrinks as it moves through the layers.

**One-line answer you can say aloud:**

> The Wald test gives F equal to 14.35 with a p-value of 0.0002. That means the chance of seeing such a big gap between retail petrol and headline CPI pass-through by accident is only about 2 in 10,000, so attenuation is statistically supported.

Plain words:

> The formal Wald test rejects equality between retail petrol and headline CPI pass-through, so attenuation is statistically supported.

## 5.4 Asymmetry

- Asymmetry is NOT the main story.
- Retail petrol shows marginal asymmetry, p = 0.0999.
- Headline WPI, WPI Fuel and Power, and headline CPI do not reject symmetry.

Plain words:

> The study tests asymmetry, but the main finding is attenuation, not asymmetric pass-through.

---

# 6. Likely questions with safe, simple answers

## Q1. What is your dissertation about?

> My dissertation studies how global oil-price shocks pass through India's price system. I compare wholesale, retail fuel, fuel-sensitive CPI, and headline CPI layers. The main finding is that pass-through is strong in fuel-related layers but weak in headline CPI.

## Q2. Why did you choose this topic?

> India imports a large amount of crude oil, so global oil shocks are important for inflation. But headline CPI does not always move strongly with oil. I wanted to understand where the oil effect becomes weaker.

## Q3. What is pass-through?

> Pass-through means how much of a change in oil prices is transmitted to domestic prices. For example, if oil rises by 10%, pass-through measures how much domestic fuel prices or inflation respond.

## Q4. What does attenuation mean?

> Attenuation means the effect becomes smaller as it moves across layers. In my study, oil shocks are strong in fuel layers but become much weaker in headline CPI.

**Everyday example to add if needed:** Like a sound becoming quieter as it passes through walls.

## Q5. What method did you use?

> I used short-run asymmetric ADL models in log differences. The model includes past inflation and current and lagged oil shocks. Positive and negative oil shocks are estimated separately.

## Q6. Why ADL and not another model?

> ADL is suitable because oil-price effects may be distributed over several months. My research question is about short-run monthly pass-through, so ADL in log differences is appropriate.

## Q7. Why not NARDL or cointegration?

> My dissertation focuses on short-run pass-through in monthly changes, not long-run equilibrium relationships. So I keep the design as ADL in log differences and do not make long-run cointegration claims.

## Q8. What is the dependent variable?

> It changes by layer. For headline CPI, the dependent variable is headline CPI inflation. For WPI models, it is WPI inflation or WPI Fuel and Power inflation. For retail petrol, it is petrol price inflation.

## Q9. What is the shock variable?

> For headline WPI, WPI Fuel and Power, and headline CPI, I use the rupee oil price shock. For retail petrol, I use Brent. For CPI Fuel and Light, I use PPAC retail petrol as the shock.

## Q10. Why use rupee oil price instead of just Brent?

> Because India's domestic oil-cost pressure depends on both the international oil price and the exchange rate. Rupee oil price captures both Brent and INR/USD movements.

## Q11. What is CPT+?

> CPT+ is cumulative pass-through from positive oil shocks. It is the sum of the positive shock coefficients across the lag window.

## Q12. What is CPT-?

> CPT- is cumulative pass-through from negative oil shocks. It is the sum of the negative shock coefficients across the lag window.

## Q13. What does the p-value mean in your table?

> The p-value shows whether the estimated effect is statistically distinguishable from zero. If the p-value is below 0.05, I treat it as statistically significant at the 5 percent level.

## Q14. What is your strongest result?

> The layered attenuation pattern. Fuel-related layers show strong pass-through, but headline CPI pass-through is weak and statistically insignificant. The formal Wald test supports this attenuation.

## Q15. Why is headline CPI weak?

> Headline CPI is a broad consumer basket. It includes many non-fuel items, especially food and services. Fuel shocks can be absorbed through taxes, margins, and basket weights, so the direct oil signal becomes diluted.

## Q16. Does this mean oil prices do not matter for consumers?

> No. I do not say oil is irrelevant. I say the effect is strong in fuel-related layers but becomes weak and statistically insignificant in headline CPI.

## Q17. What is asymmetry in your study?

> Asymmetry means positive and negative oil shocks may have different effects. For example, prices may rise faster when oil rises than they fall when oil declines.

## Q18. Did you find asymmetry?

> Not strongly. Retail petrol gives marginal evidence at the 10 percent level, but the main WPI, WPI Fuel and Power, and headline CPI models do not reject symmetry. So asymmetry is not the central result.

## Q19. Why did you exclude COVID months for WPI Fuel and Power?

> April to September 2020 was an abnormal period with extreme oil-price movements and unusual pricing behaviour. Excluding those months improves diagnostics and gives a cleaner preferred estimate for the post-2010 market-linked period.

## Q20. What are diagnostics?

> Diagnostics check whether the model is reliable enough for interpretation. I use checks for serial correlation, functional form, heteroscedasticity, and stability.

## Q21. What if a model fails diagnostics?

> Then I do not use it for the main claim. For example, CPI M2 and M3 are not claim-bearing because diagnostics reject them.

## Q22. What is Granger causality?

> Granger causality means past values of one variable help predict another variable. It does not prove true structural causality, so I call it predictive precedence.

## Q23. Is your study causal?

> It is not a structural causal model. It is a reduced-form time-series study of pass-through patterns and predictive relationships.

## Q24. What is reduced-form?

> Reduced-form means I estimate the observed relationship between variables without fully modelling every structural mechanism behind price-setting.

**Plain words:** I describe _what_ happens between variables, not the deep _why_ of each firm's decision.

## Q25. Why do samples differ across models?

> Data availability differs across WPI, CPI, PPAC petrol, and CPI Fuel and Light. I use the reliable available sample for each layer.

## Q26. What is the policy implication?

> Oil shocks matter most for fuel-sensitive layers, but their effect on headline CPI is diluted. Policymakers should monitor fuel-specific channels, not only the headline CPI response.

## Q27. What is the main limitation?

> The main limitation is that the models are reduced-form and different layers have different samples. So I interpret the results as a layered attenuation map, not a single structural causal chain.

## Q28. What would you improve in future research?

> Future work could use a structural model, state-level fuel price data, separate tax components, and more detailed CPI subcomponents to study the mechanism more deeply.

## Q29. Why monthly data?

> Monthly data are suitable because fuel prices and inflation adjust over short periods. They also provide enough observations to estimate lagged pass-through.

## Q30. Your conclusion in one sentence?

> Oil-price pass-through in India is layered: strong in fuel-related prices, but weak and statistically insignificant in headline CPI.

---

# 7. What to say if you do not know the answer

It is okay to not know. Be calm and honest. Use one of these:

**If the question is outside your project:**

> I have not estimated that directly in this dissertation, so I should not overclaim. Based on my results, I can only say that the pass-through is stronger in fuel-related layers and weaker in headline CPI.

**If the question is too technical:**

> My understanding is limited to the model used in this dissertation. In this project, the point of that method is to handle lagged monthly pass-through and to test cumulative effects.

**If they suggest another model:**

> That would be a useful extension. My dissertation deliberately keeps the design short-run ADL only, because the research question is about monthly pass-through and attenuation across layers.

**If they challenge your wording:**

> Sorry, let me say it more simply. The oil shock is strong near fuel prices, but it becomes weak when we reach broad headline CPI.

**If you did not hear or understand the question:**

> Sorry, could you please repeat the question slowly? I want to answer it correctly.

**If they ask why you did not include something:**

> That is a good point. I kept the dissertation focused on the main research question and avoided adding models that were outside the short-run ADL design.

---

# 8. Speaking practice scripts

## The 2-minute version

> My dissertation studies how global oil-price shocks pass through India's price system. India imports a large share of crude oil, and crude is priced internationally, so oil shocks can create domestic price pressure. But headline CPI does not always move strongly with oil prices. This is the puzzle of my research.
>
> I study this as a layered transmission problem. The main layers are WPI, WPI Fuel and Power, PPAC retail petrol, CPI Fuel and Light, and headline CPI. I use monthly data and short-run asymmetric ADL models in log differences. The model allows oil shocks to affect prices over several months and separates positive and negative shocks.
>
> The main result is attenuation. Pass-through is strong in WPI Fuel and Power and retail petrol. It is smaller in CPI Fuel and Light. It is modest in headline WPI, and weak and statistically insignificant in headline CPI. A formal Wald test also supports attenuation across the consumer-price chain.
>
> So my conclusion is not that oil prices are irrelevant. Instead, oil matters strongly near fuel-related prices, but the effect becomes diluted before reaching headline CPI.

## The 30-second version

> My dissertation studies oil-price pass-through in India. I use short-run ADL models across WPI, retail petrol, CPI Fuel and Light, and headline CPI. The main finding is layered attenuation. Oil shocks pass strongly into fuel-related layers, but the effect becomes weak and statistically insignificant in headline CPI.

---

# 9. Pronunciation help

Use these simpler ways to say difficult words.

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

If a word feels difficult, just replace it with plain English:

- Instead of "attenuation," say "the effect becomes weaker."
- Instead of "heteroscedasticity," say "changing error variance."
- Instead of "autocorrelation," say "errors are related across months."
- Instead of "statistically insignificant," say "not strong enough statistically."

---

# 10. Final checklist before you walk in

## Content

- I can state the research question in one sentence.
- I can explain why oil matters for India.
- I can explain WPI versus CPI in everyday words.
- I can explain ADL as "lagged effects spread over months."
- I can explain CPT+ and CPT- as "total effect across lags."
- I can read the main results table aloud.
- I can explain why headline CPI is weak.
- I can explain attenuation with a simple example.
- I can state the limitations honestly.

## Slides

- Each slide has one clear message.
- Tables are readable from the back of the room.
- Most important numbers are highlighted.
- Conclusion slide is simple and short.
- Backup slides exist for ADL, CPI weakness, and tough questions.

## Speaking

- Practise the opening 3 times.
- Practise the main result 5 times.
- Practise the conclusion 3 times.
- Do not memorise long paragraphs. Memorise ideas, not sentences.
- Speak slowly. Pause after important numbers.
- If nervous, just read the slide and explain one point.

---

# 11. If you only have limited time

**If you have one day, study only these:**

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

**If you have three days, also add:**

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

You did the work. Trust it. Speak slowly. Smile. You will be fine.
