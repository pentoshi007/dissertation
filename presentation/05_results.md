# PRESENTATION GUIDE -- PART 5: RESULTS (THE NUMBERS THAT MATTER)

---

## The Big Results Table -- MEMORISE THIS

This is the single most important table in your entire work:

| Layer | Sample Period | N | $CPT^{+}$ | p-value | $CPT^{-}$ | p-value | Asym. p | Verdict |
|---|---|---|---|---|---|---|---|---|
| **PPAC Retail Petrol** | 2004-08 to 2024-12 | 245 | **0.3459** | **<0.001** | 0.1912 | 0.0002 | 0.0999 | Strong; marginal asymmetry |
| **WPI Fuel and Power** | 1995-05 to 2026-03 | 371 | **0.2866** | **<0.001** | 0.2677 | <0.001 | 0.7832 | Strong; RESET caveat |
| **CPI Fuel and Light** | 2011-05 to 2024-12 | 164 | **0.1777** | **0.0021** | 0.1058 | 0.1741 | 0.4554 | Moderate bridge evidence |
| **Headline WPI** | 1983-05 to 2026-03 | 515 | **0.0301** | **0.0240** | 0.0374 | 0.0012 | 0.6727 | Modest but significant |
| **Headline CPI** | 2004-08 to 2024-12 | 245 | **0.0213** | **0.1220** | 0.0006 | 0.9375 | 0.2408 | **Weak; NOT significant** |

### How to Read This Table -- Row by Row

**Row 1 -- PPAC Retail Petrol (Strongest Layer):**

- $CPT^{+} = 0.3459$ means: "When Brent oil goes up 1%, Delhi petrol price goes up about 0.35% over the lag window"
- $p < 0.001$ means: this is HIGHLY statistically significant (99.9% confidence)
- Asymmetry $p = 0.0999$: MARGINAL -- there's weak evidence that price increases pass through more than decreases (the "rockets and feathers" idea), but only at the 10% level, not the standard 5%

**Row 2 -- WPI Fuel and Power (Second Strongest):**

- $CPT^{+} = 0.2866$: "A 1% rupee oil shock -> about 0.29% increase in wholesale fuel prices"
- Very significant ($p < 0.001$)
- BUT has a RESET caveat (functional form test fails)
- Asymmetry $p = 0.7832$: NO asymmetry (ups and downs have similar effects)

**Row 3 -- CPI Fuel and Light (The Bridge):**

- $CPT^{+} = 0.1777$: "A 1% increase in PPAC petrol -> about 0.18% increase in consumer fuel prices"
- Significant at $p = 0.0021$
- This is **bridge evidence** -- it shows fuel shocks entering the consumer price basket
- Shorter sample (only from 2011), so treated as supporting, not primary

**Row 4 -- Headline WPI (Broad Wholesale):**

- $CPT^{+} = 0.0301$: SMALL -- "A 1% oil shock -> only 0.03% change in overall WPI"
- Still statistically significant ($p = 0.024$)
- Makes sense: WPI includes many non-fuel items that dilute the oil signal

**Row 5 -- Headline CPI (The Consumer Endpoint):**

- $CPT^{+} = 0.0213$: TINY and **NOT statistically significant** ($p = 0.1220 > 0.05$)
- This is the key finding: by the time oil shocks reach headline CPI, they're too weak to detect statistically
- The CPI basket has food (~45%), housing, health, education, clothing -- fuel is a SMALL weight

---

## The Attenuation Pattern -- Your Central Finding

**The ranking of $CPT^{+}$ tells the whole story:**

```
PPAC Retail Petrol:   0.3459  ||||||||||||||||||||||||||||||||||||  <-- STRONGEST
WPI Fuel and Power:   0.2866  ||||||||||||||||||||||||||||||       <-- Strong (with caveat)
CPI Fuel and Light:   0.1777  ||||||||||||||||||                   <-- Moderate (bridge)
Headline WPI:         0.0301  |||                                  <-- Small but significant
Headline CPI:         0.0213  ||                                   <-- Weak, NOT significant
```

**The shock loses about 94% of its force from retail petrol to headline CPI!**

### Formal Attenuation Test (Wald Test)

You formally test: "Is the retail petrol pass-through EQUAL to the headline CPI pass-through?"

$$H_{0}: CPT^{+}_{\text{retail petrol}} = CPT^{+}_{\text{headline CPI}}$$

$$F = 14.3499, \quad p = 0.0002 \quad \Longrightarrow \quad \textbf{REJECT equality}$$

**Translation:** "The difference between retail petrol pass-through (0.35) and headline CPI pass-through (0.02) is NOT due to chance. Attenuation is statistically confirmed."

---

## Common-Sample Check

Since each layer has different time periods, you also do a **common-sample exercise** (same time window):

| Stage | Link | $CPT^{+}$ | p-value |
|---|---|---|---|
| Stage 1 | Brent -> PPAC Petrol | 0.4007 | 0.0001 |
| Stage 2 | PPAC Petrol -> CPI Fuel and Light | 0.1777 | 0.0021 |
| Stage 3 | Rupee Oil -> Headline CPI | 0.0064 | 0.6355 |

**The attenuation pattern SURVIVES even on the same sample.** Stage 1 is strong, Stage 3 is essentially zero.

---

## WPI Fuel and Power -- Local Projection Results (New-Model Dissertation)

This gives a different view -- how the effect BUILDS over time:

| Horizon (months) | Cumulative Response ($\beta_{h}$) | p-value |
|---|---|---|
| 0 (same month) | 0.0453 | <0.001 |
| 3 months | 0.2849 | <0.001 |
| 6 months | 0.2963 | <0.001 |
| 9 months | 0.3539 | <0.001 |
| 12 months | 0.3461 | <0.001 |

**Key insight:** Most of the pass-through happens within 3--4 months, then levels off. This matches India's fuel pricing mechanism (prices revised fortnightly/monthly, not continuously).

### Pre-2010 vs Post-2010 (Reform Effect)

The state-dependent specification adds an **interaction term** $\theta_{h}$ to test whether pass-through changed after deregulation:

$$\beta_{h}\,\Delta\ln(\text{oil}_{t}^{INR}) + \theta_{h}\,\Delta\ln(\text{oil}_{t}^{INR}) \times d_{\text{post2010}}$$

- $\beta_{h}$ = pre-2010 response
- $\beta_{h} + \theta_{h}$ = total post-2010 response
- If $\theta_{h}$ is significant, deregulation made pass-through stronger

| Horizon | Pre-2010 | Post-2010 | Interaction ($\theta_{h}$) | $\theta$ p-value |
|---|---|---|---|---|
| 0 | -0.0095 (blocked!) | 0.0929 | 0.1024 | <0.001 |
| 3 | 0.1369 | 0.4292 | 0.2924 | <0.001 |
| 6 | 0.1965 | **0.3937** | 0.1972 | 0.0220 |
| 12 | 0.2111 | 0.4803 | 0.2691 | 0.0840 |

**Before 2010 (administered pricing):**

- At horizon 0: response is NEGATIVE (-0.01) -- prices were BLOCKED from adjusting
- Oil marketing companies absorbed the cost through "under-recoveries" (losses)
- Eventually some pass-through occurs: approximately 0.20 by 6 months

**After 2010 (market-linked pricing):**

- At horizon 0: 0.093 -- prices adjust within the SAME month
- By 6 months: 0.39 -- roughly DOUBLE the pre-2010 response
- Deregulation removed the administered-price buffer

**This is strong evidence that fuel pricing reform changed the pass-through.**

---

## On Asymmetry -- The "Rockets and Feathers" Question

**Question:** "Do prices go UP faster when oil rises (rockets) than they come DOWN when oil falls (feathers)?"

**Your answer:** Mostly NO.

| Layer | Asymmetry p-value | Conclusion |
|---|---|---|
| PPAC Retail Petrol | 0.0999 | Marginal at 10% -- suggestive but NOT decisive |
| WPI Fuel and Power | 0.7832 | No asymmetry |
| CPI Fuel and Light | 0.4554 | No asymmetry |
| Headline WPI | 0.6727 | No asymmetry |
| Headline CPI | 0.2408 | No asymmetry |

**Bottom line:** Asymmetry is NOT your main finding. The main finding is ATTENUATION across layers.

**If professor asks about rockets and feathers:**

> "I tested for asymmetry in every layer using Wald tests and bootstrap resampling. Only retail petrol shows marginal evidence at the 10% level. All other layers show symmetric pass-through. So the story here is not about asymmetry -- it's about how the oil signal gets weaker as we move from fuel to broader prices."
