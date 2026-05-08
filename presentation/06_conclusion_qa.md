# PRESENTATION GUIDE -- PART 6: ROBUSTNESS, LIMITATIONS, CONCLUSION AND LIKELY QUESTIONS

---

## Robustness Checks (Things You Did to Double-Check)

### Check 1: Brent + Exchange Rate Decomposition (WPI)
Instead of using the combined rupee oil price, you decomposed it into Brent and exchange rate separately:

- Result: $CPT^{+} = 0.0309$ ($p = 0.0234$) -- almost identical to the rupee-shock result (0.0301)
- **Conclusion:** "The result doesn't depend on combining Brent and the exchange rate into one variable."

### Check 2: Bootstrap Symmetry Tests (4,999 replications)
Resampled the data 4,999 times to check if asymmetry findings are robust:

- Headline WPI: symmetry NOT rejected (bootstrap $p = 0.7461$)
- WPI Fuel and Power: symmetry NOT rejected (bootstrap $p = 0.8196$)
- Headline CPI: symmetry NOT rejected (bootstrap $p = 0.4997$)
- **Conclusion:** "Asymmetry is not a robust finding -- confirmed by bootstrap."

### Check 3: Pre/Post-2010 Wholesale Split
Compared pass-through before and after petrol deregulation (June 2010):

| Layer | Pre-2010 $CPT^{+}$ | Post-2010 $CPT^{+}$ |
|---|---|---|
| Headline WPI | 0.0117 ($p=0.38$, insignificant) | **0.0741** ($p=0.004$, significant) |
| WPI Fuel and Power | 0.0922 ($p=0.17$, insignificant) | **0.5241** ($p<0.001$, very strong) |

- **Conclusion:** "Pass-through is much stronger after deregulation, especially for WPI Fuel and Power which jumped from 0.09 to 0.52. But this is not a clean causal estimate -- other things changed too."

### Check 4: Post-2014 Diesel Deregulation

- The interaction $\theta_{h}$ is positive but NOT statistically significant at 6+ months
- Conclusion: "Diesel deregulation didn't produce a separately identifiable effect beyond petrol deregulation."

### Check 5: High Oil-Volatility Months

- No significant difference between normal and high-volatility periods at 6 months
- **Conclusion:** "Pass-through doesn't systematically differ during extreme oil movements."

---

## Limitations (Be Honest About These)

1. **Reduced-form, not structural causal:** "These are statistical associations, not proof that oil CAUSES inflation changes. Other factors could be at play."

2. **Different sample periods:** "Each layer has different data availability. The common-sample exercise mitigates this, but it's still a limitation."

3. **CPI Fuel and Light has a short sample:** Only starts in 2011, so it's treated as bridge evidence, not a primary result.

4. **WPI Fuel and Power has a RESET caveat:** The functional form test fails, so the result is reported as mechanism evidence with a caveat.

5. **PPAC uses Delhi prices only:** This is one city, used as a proxy for national retail fuel prices.

6. **Pre/post-2010 is suggestive, not causal:** Other reforms happened around the same time (CPI rebasing, inflation targeting, GST, changes in fuel taxes, and large global shocks).

7. **No long-run analysis:** This is deliberately short-run. No NARDL, no error-correction, no long-run elasticities. The focus is monthly transmission.

---

## Conclusion (What You Found)

State it clearly in these seven points:

1. **Oil-price pass-through in India is LAYERED** -- it varies across different price indices.

2. **Retail petrol and WPI Fuel and Power show STRONG pass-through** ($CPT^{+}$ of 0.35 and 0.29 respectively).

3. **CPI Fuel and Light provides bridge evidence** -- retail fuel pressure enters the consumer fuel layer with attenuation ($CPT^{+} = 0.18$).

4. **Headline WPI shows modest but statistically significant pass-through** ($CPT^{+} = 0.03$).

5. **Headline CPI shows WEAK and statistically INSIGNIFICANT pass-through** ($CPT^{+} = 0.02$, $p = 0.12$).

6. **Asymmetry is NOT the main finding** -- only retail petrol shows marginal evidence at the 10% level.

7. **Post-2010 deregulation is associated with stronger wholesale pass-through**, but it's institutional context, not clean causal evidence.

### The One-Line Takeaway:

> **"Oil shocks do not vanish in India, but they lose force as they move from fuel prices to headline consumer inflation."**

### Policy Implication:

- If you only watch headline CPI, you'll MISS near-fuel price pressure
- Monitoring retail petrol, WPI Fuel and Power, and CPI Fuel and Light gives a better early warning of oil-price transmission
- The rupee oil price ($\text{Brent} \times \text{exchange rate}$) matters more than Brent alone -- exchange rate movements amplify or dampen pass-through

---

## LIKELY PROFESSOR QUESTIONS AND ANSWERS

### Q1: "What is your main contribution?"
> "Most studies estimate a single equation linking oil to CPI or WPI. I treat pass-through as a layered problem -- tracking the shock through five price layers. This shows WHERE the signal weakens, not just WHETHER it exists."

### Q2: "Why ADL and not VAR or NARDL?"
> "ADL in log differences is simpler and more transparent for a short-run pass-through question. VAR would require choosing a system of variables and identifying structural shocks. NARDL would test for long-run equilibrium relationships, which is not my question -- I'm interested in monthly transmission, not long-run adjustment. ADL gives clean, interpretable short-run coefficients with proper HAC inference."

### Q3: "Why different shock variables for different layers?"
> "Because each layer faces a different relevant price. Wholesale prices depend on the rupee cost of crude ($\text{Brent} \times \text{INR/USD}$). Retail petrol prices are set based on international product prices in USD. Consumer fuel prices follow domestic pump prices. Matching the shock to each layer keeps the regressions interpretable."

### Q4: "Why is headline CPI not significant?"
> "The CPI basket is very broad. Food alone is about 45% of CPI. Housing, health, education, services, clothing -- these don't directly respond to monthly oil movements. Even a strong fuel shock gets diluted when fuel is only a small weight in the total basket. This isn't a failure -- it's the central finding: attenuation."

### Q5: "What is Newey-West and why do you need it?"
> "Newey-West is a way to calculate standard errors that remain valid even when residuals are heteroskedastic (varying variance) and autocorrelated (correlated over time). Monthly economic data almost always has both problems. Without Newey-West, my confidence intervals would be too narrow and I'd falsely reject null hypotheses."

### Q6: "What does $p < 0.05$ mean?"
> "If the p-value is less than 0.05, there's less than a 5% probability that I would observe an effect this large if there were truly no relationship. So I reject the null hypothesis of no effect. It's the standard threshold in economics for statistical significance."

### Q7: "What is CPT and how do you interpret it?"
> "$CPT$ stands for Cumulative Pass-Through. It's the sum of all the coefficients on oil shock lags: $CPT^{+} = \sum_{j} \beta_{j}^{+}$. If $CPT^{+} = 0.35$, it means a 1% positive oil shock is associated with a total 0.35% increase in that price index over the lag window. The closer to 1.0, the more complete the pass-through."

### Q8: "Why does WPI Fuel and Power have a caveat?"
> "The RESET test for functional form fails, which means a purely linear specification might not capture all the dynamics. The result is still economically meaningful and the other diagnostics pass, so I report it as mechanism evidence with an explicit functional-form caveat rather than as a fully validated main claim."

### Q9: "Is there any asymmetry (rockets and feathers)?"
> "I tested for asymmetry in every layer using Wald tests ($H_{0}: CPT^{+} = CPT^{-}$) and bootstrap resampling. Only retail petrol shows marginal evidence at the 10% level. All other layers show symmetric pass-through. So the story here is not about asymmetry -- it's about how the oil signal gets weaker as we move from fuel to broader prices."

### Q10: "What about the reform effect?"
> "After petrol deregulation in 2010, WPI Fuel and Power pass-through roughly quintupled -- from 0.09 (insignificant) to 0.52 (highly significant). Headline WPI also strengthened. This is consistent with removing the administered-price buffer. But I'm careful to say this is institutional evidence, not a clean causal experiment, because other policy and macro changes happened around the same time."

### Q11: "What is a unit root and why does it matter?"
> "A unit root means the data has a stochastic trend -- it wanders without returning to a mean. Regressing one unit-root variable on another can produce spurious (fake) significant results. I use ADF tests to confirm all my variables have unit roots in levels but become stationary after first differencing. That's why I use monthly log differences."

### Q12: "Could you have used a structural model?"
> "A structural model would require identifying assumptions about the causal transmission mechanism -- which I don't have strong enough theoretical grounds for. My reduced-form approach is more honest: it tells you the statistical associations without claiming specific causal pathways. The layered design provides suggestive evidence of the transmission channel without requiring structural identification."

### Q13: "What's the difference between WPI and CPI?"
> "WPI (Wholesale Price Index) measures prices at the wholesale/producer level -- closer to input costs. CPI (Consumer Price Index) measures prices consumers actually pay -- it includes services, housing, health, education, which WPI doesn't. WPI is influenced more by commodity costs; CPI reflects the broader economy. That's why oil shocks appear differently in each."

### Q14: "Why did you use dummy variables?"
> "Dummy variables control for known structural events that would otherwise distort the oil-shock estimates. The post-2010 dummy ($d_{\text{post2010}} = 1$ from July 2010) absorbs the level shift from petrol deregulation. The post-2014 dummy does the same for diesel. The COVID dummy ($d_{\text{covid}} = 1$ for April--September 2020) absorbs the extreme pandemic disruption when oil prices crashed for non-economic reasons. Month dummies ($\mu_{m}$) capture seasonal patterns. Without these controls, the $\beta$ coefficients would mix up oil-price effects with reform effects and pandemic noise."

---

## TIMELINE FOR 20-25 MINUTE PRESENTATION

| Minutes | What to Cover |
|---|---|
| 0--3 | Introduction: India imports oil, prices in USD, the puzzle (oil up but CPI doesn't move much) |
| 3--5 | Research question and the layered approach innovation |
| 5--8 | Data: sources (with full forms), rupee oil price construction, log differences |
| 8--12 | Methodology: ADL model explained simply, CPT definition, Newey-West, diagnostic tests |
| 12--16 | Results: Go layer by layer (petrol -> WPI Fuel -> CPI Fuel -> WPI headline -> CPI headline) |
| 16--19 | The attenuation finding: ranking, Wald test, common-sample check |
| 19--21 | Robustness: deregulation effect, bootstrap, decomposition |
| 21--23 | Limitations and conclusion |
| 23--25 | The one-line takeaway + policy implications |
