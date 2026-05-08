# PRESENTATION GUIDE -- PART 3: METHODOLOGY (THE MODELS)

---

## What Model Are You Using? -- The ADL Model

**ADL = Autoregressive Distributed Lag model**

Break that name down:

- **Auto-regressive** = the model includes past values of the dependent variable (Y depends on its own past)
- **Distributed Lag** = the effect of the shock variable (oil) is spread over several months, not just instant

### The Main Equation (This Is The Heart of Your Work)

$$\Delta y_{t} = \alpha + \sum_{i=1}^{p} \varphi_{i}\,\Delta y_{t-i} + \sum_{j=0}^{q} \beta_{j}^{+}\,\Delta x_{t-j}^{+} + \sum_{j=0}^{q} \beta_{j}^{-}\,\Delta x_{t-j}^{-} + \gamma^{\prime} Z_{t} + \mu_{m} + \varepsilon_{t}$$

**Don't panic!** Let's decode every single piece:

| Symbol | What It Is | Plain English |
|---|---|---|
| $\Delta y_{t}$ | Monthly inflation in the price index | "How much did the price index change this month?" |
| $\alpha$ (alpha) | Constant / intercept | A fixed baseline number |
| $\varphi_{i}$ (phi) | Coefficients on lagged own inflation | "How much does LAST month's inflation affect THIS month's?" |
| $\Delta y_{t-i}$ | Past values of inflation (lags 1,2,3...) | "What was inflation 1, 2, 3 months ago?" |
| $\beta_{j}^{+}$ (beta-plus) | Coefficients on POSITIVE oil shocks | "When oil goes UP, how much does the price index respond?" |
| $\Delta x_{t-j}^{+}$ | Positive oil shock at lag j | "By how much did oil price INCREASE, j months ago?" |
| $\beta_{j}^{-}$ (beta-minus) | Coefficients on NEGATIVE oil shocks | "When oil goes DOWN, how much does the price index respond?" |
| $\Delta x_{t-j}^{-}$ | Negative oil shock at lag j | "By how much did oil price DECREASE, j months ago?" |
| $\gamma^{\prime} Z_{t}$ (gamma-prime Z) | Control variables | Other factors like IIP growth, exchange rate changes, dummy variables |
| $\mu_{m}$ (mu-m) | Month fixed effects | Captures seasonal patterns (e.g., prices may behave differently in Jan vs Jul) |
| $\varepsilon_{t}$ (epsilon) | Error term / residual | Everything else the model doesn't capture -- random noise |
| $\Sigma$ (Sigma) | Summation sign | "Add up all the terms from i=1 to p" or "j=0 to q" |

### How Are These Coefficient Values Determined?

All the Greek-letter values ($\alpha, \varphi, \beta^{+}, \beta^{-}, \gamma, \mu$) are **estimated by OLS (Ordinary Least Squares)**. Here is how it works in simple terms:

1. **You feed the computer your data:** monthly inflation values ($\Delta y_{t}$) and oil shock values ($\Delta x_{t}^{+}, \Delta x_{t}^{-}$) for hundreds of months
2. **OLS finds the "best fit" line** through the data -- it picks the coefficient values that minimise the total squared errors ($\sum \varepsilon_{t}^{2}$)
3. **Think of it like drawing the best straight line** through a scatter plot -- the line that is closest to all the data points on average
4. The computer solves this mathematically in one step -- you don't guess the values

**What each estimated value tells you:**

| Coefficient | How It's Determined | What Its Value Means |
|---|---|---|
| $\alpha$ (intercept) | OLS best fit | The baseline inflation when all shocks are zero |
| $\varphi_{i}$ (AR coefficients) | OLS best fit | How much past inflation predicts current inflation |
| $\beta_{j}^{+}$ (positive oil) | OLS best fit | How much a 1% oil price INCREASE at lag j moves inflation |
| $\beta_{j}^{-}$ (negative oil) | OLS best fit | How much a 1% oil price DECREASE at lag j moves inflation |
| $\gamma$ (controls) | OLS best fit | Effect of IIP growth, exchange rate, etc. |
| $\mu_{m}$ (month effects) | OLS best fit | Seasonal adjustment for each calendar month |
| $\varepsilon_{t}$ (error) | What's left over | The residual -- difference between actual and predicted inflation |

**You do NOT set these values yourself.** The data determines them. Then you check: "Are these values statistically significant (different from zero)?" using p-values from Newey-West HAC standard errors.

**The individual $\beta$ values are small numbers** (e.g., 0.01 to 0.10 at each lag). What you report as the main result is their SUM, which is $CPT^{+}$ or $CPT^{-}$ (cumulative pass-through). For example, if $\beta_{0}^{+} = 0.10$, $\beta_{1}^{+} = 0.12$, $\beta_{2}^{+} = 0.08$, $\beta_{3}^{+} = 0.05$, then $CPT^{+} = 0.10 + 0.12 + 0.08 + 0.05 = 0.35$.

**Key model fit statistic -- Adjusted $R^{2}$:**

| Model | Adjusted $R^{2}$ | Meaning |
|---|---|---|
| Headline WPI | 0.4207 | The model explains 42% of monthly WPI inflation variation |
| WPI Fuel and Power | 0.4630 | 46% of WPI Fuel variation explained |
| Headline CPI (M1) | 0.4492 | 45% of monthly CPI inflation variation explained |

An $R^{2}$ of 0.42--0.46 is **good for monthly macro data**. It means the model captures nearly half of all monthly variation. The remaining 50--55% is driven by food prices, supply shocks, policy changes, and other factors not in the model.

---

### What Does ADL(p,q) Mean? -- Model Specifications

**ADL(p,q)** is shorthand notation where:

- **p** = number of own lags (how many past months of inflation you include)
- **q** = number of oil shock lags (how many past months of oil shocks you include)

**Example: ADL(3,3) means:**

- Include inflation from 3 months ago ($\Delta y_{t-1}, \Delta y_{t-2}, \Delta y_{t-3}$) -- that's the "3" for p
- Include oil shocks from this month AND 3 months back ($\Delta x_{t}, \Delta x_{t-1}, \Delta x_{t-2}, \Delta x_{t-3}$) -- that's the "3" for q
- Note: oil shock lags go from 0 to q, so ADL(3,3) actually has 4 oil shock terms (lags 0,1,2,3)

**Example: ADL(12,6) means:**

- Include 12 months of own inflation lags (a full year of history)
- Include oil shocks from lag 0 to lag 6 (current month plus 6 months back = 7 oil shock terms)

### How Are The Lag Numbers (p and q) Chosen?

You use a statistical criterion called **AIC (Akaike Information Criterion)**:

1. **Try different lag combinations:** ADL(1,3), ADL(2,3), ADL(3,3), ADL(4,3), etc.
2. **For each, compute the AIC** -- a score that balances model fit against complexity
3. **Pick the combination with the LOWEST AIC** -- that's the best trade-off between fitting the data well and not over-fitting with too many lags

**In simple terms:** AIC asks "Does adding one more lag actually help predict inflation better, or does it just add noise?" The lag count that gives the best prediction wins.

**For your models specifically:**

- **CPI pipeline:** AIC tested p = 1 to 4, and **p = 3 won** (best AIC). Oil lags fixed at q = 3.
- **WPI pipeline:** Uses p = 12 (a full year) because the WPI series is much longer (500+ months) and monthly seasonality in wholesale prices can extend up to 12 months. Oil lags q = 6 to capture a half-year response window.

### Full Model Specifications (What Each Model Looks Like)

| Model | Specification | Controls Included |
|---|---|---|
| **Headline WPI** | ADL(12,6) | Month fixed effects |
| **WPI Fuel and Power** | ADL(12,6) | Exchange-rate change, post-2010 dummy, post-2014 dummy, COVID dummy, month fixed effects |
| **PPAC Retail Petrol** | ADL(3,3) | IIP growth, petrol deregulation dummy, diesel deregulation dummy, COVID dummy, month fixed effects |
| **CPI Fuel and Light** | ADL(3,3) | No extra controls (short sample) |
| **Headline CPI (M1)** | ADL(3,3) | IIP growth, petrol deregulation dummy, diesel deregulation dummy, COVID dummy, month fixed effects |

**If professor asks: "Why not use more lags?"**

> "Adding more lags uses up degrees of freedom (you lose data points at the start of the sample). With a short sample like CPI (245 observations), using 12 lags would consume too many observations. AIC selects p = 3 as the optimal balance. For WPI, which has 515 observations, 12 lags are affordable and capture the full annual cycle of wholesale price dynamics."

---

### What Are "Lags"?

A **lag** means "a past value." If today is May 2026:

- Lag 1 = April 2026 (one month ago)
- Lag 3 = February 2026 (three months ago)
- Lag 12 = May 2025 (twelve months ago)

**Why include lags?** Because oil price changes DON'T affect Indian prices instantly. It takes time for crude oil to reach the refinery, then the petrol pump, then wholesale prices, then consumer prices. Lags capture this delay.

### Which Shock Variable for Which Layer?

This is IMPORTANT -- each layer uses a DIFFERENT shock:

| Layer (Dependent Variable) | Shock Variable | Why |
|---|---|---|
| **Headline WPI** inflation | Rupee oil shock | WPI tracks producer costs, which depend on rupee-denominated oil |
| **WPI Fuel and Power** inflation | Rupee oil shock | Wholesale fuel prices directly face rupee oil costs |
| **PPAC Retail Petrol** change | Brent USD shock | Retail fuel pricing is based on international product prices |
| **CPI Fuel and Light** inflation | PPAC petrol shock | Consumer fuel prices follow retail pump prices |
| **Headline CPI** inflation | Rupee oil shock | Overall consumer inflation depends on rupee-denominated costs |

---

## Control Variables (the $Z_{t}$ vector)

| Control | What It Is | Why Include It |
|---|---|---|
| **Exchange rate change** | Monthly change in INR/USD | Captures currency effects beyond what's in rupee oil |
| **IIP growth** | Index of Industrial Production growth | Controls for demand-side economic activity |
| **Post-2010 dummy** | = 1 from July 2010 onward | Marks petrol price deregulation |
| **Post-2014 dummy** | = 1 from November 2014 onward | Marks diesel price deregulation |
| **COVID dummy** | = 1 for April--September 2020 | Absorbs extreme pandemic disruption |
| **Month dummies** | 11 monthly indicators | Captures seasonal patterns |

### What Is a Dummy Variable?

A dummy variable is simply a variable that equals **1** when a condition is true, and **0** otherwise. It acts like an on/off switch in the model:

| Dummy Variable | Equals 1 When... | Equals 0 When... | Purpose |
|---|---|---|---|
| **Post-2010 ($d\_{\text{post2010}}$)** | From July 2010 onward | Before July 2010 | Captures the effect of **petrol price deregulation** -- the government stopped controlling petrol prices |
| **Post-2014 ($d\_{\text{post2014}}$)** | From November 2014 onward | Before November 2014 | Captures **diesel price deregulation** -- diesel prices also became market-linked |
| **COVID ($d\_{\text{covid}}$)** | April 2020 to September 2020 | All other months | Absorbs the **extreme disruption** during the pandemic -- oil prices crashed, supply chains broke, demand collapsed |
| **Month dummies ($\mu_{m}$)** | One for each calendar month (Jan through Nov; December is the reference) | Other months | Captures **seasonal patterns** -- e.g., fuel demand may differ in summer vs winter |

**Why use dummies?** Without them, these special events would contaminate your oil-shock estimates. For example, during COVID, oil prices crashed for reasons unrelated to normal pass-through. The COVID dummy "absorbs" that abnormality so your $\beta$ coefficients reflect normal oil-price transmission, not pandemic chaos.

**Note:** There is NO war dummy in this study. The study period includes global events like the Russia-Ukraine conflict (2022), but this is captured through the oil price movements themselves -- Brent spiked due to the war, and that spike enters the model through $\Delta x_{t}^{+}$.

---

## Cumulative Pass-Through (CPT) -- Your Key Metric

This is the MOST IMPORTANT number in your entire dissertation.

$$CPT^{+} = \beta_{0}^{+} + \beta_{1}^{+} + \beta_{2}^{+} + \cdots + \beta_{q}^{+} = \sum_{j=0}^{q} \beta_{j}^{+}$$

$$CPT^{-} = \beta_{0}^{-} + \beta_{1}^{-} + \beta_{2}^{-} + \cdots + \beta_{q}^{-} = \sum_{j=0}^{q} \beta_{j}^{-}$$

**What $CPT^{+}$ means in plain English:**

- "If oil price goes up by 1%, how much does the price index go up IN TOTAL over the next few months?"
- If $CPT^{+} = 0.35$, it means: "A 1% oil price increase leads to about 0.35% total increase in that price index"
- The closer to 1.0, the more "complete" the pass-through
- The closer to 0, the more the shock is "absorbed" or "diluted"

**Three hypothesis tests you run on CPT:**

| Test | Null Hypothesis | What It Checks |
|---|---|---|
| **Test 1** | $H_{0}: CPT^{+} = 0$ | "Do positive oil shocks have ANY effect?" |
| **Test 2** | $H_{0}: CPT^{-} = 0$ | "Do negative oil shocks have ANY effect?" |
| **Test 3** | $H_{0}: CPT^{+} = CPT^{-}$ | "Is the effect SYMMETRIC?" (same for ups and downs?) |

---

## Inference Method: Newey-West HAC Standard Errors

**Standard errors** tell you how precise your estimates are. Smaller SE = more precise.

**Problem:** Monthly economic data has two issues:

1. **Heteroskedasticity** -- the "noise" in data isn't constant (some months are noisier)
2. **Autocorrelation** -- this month's noise is correlated with last month's noise

**Regular standard errors assume neither problem exists.** If you use them anyway, your confidence intervals will be WRONG (too narrow), and you'll falsely claim significance.

**Solution: Newey-West HAC standard errors** (Newey and West, 1987)

- **H**eteroskedasticity **A**nd auto**C**orrelation consistent
- These standard errors are VALID even when both problems exist
- They're wider (more honest) than regular standard errors
- **Bandwidth** = how many lags of autocorrelation to account for. Formula: $\lfloor 0.75 \times N^{1/3} \rfloor$

**If professor asks: "Why not just use OLS standard errors?"**

> "Because monthly price data is almost certainly heteroskedastic and autocorrelated. Using OLS standard errors would give misleadingly narrow confidence intervals and inflate the t-statistics, leading to false rejections of the null hypothesis. Newey-West HAC errors correct for both problems."

---

## The Local Projection Method (Jorda, 2005) -- For the New-Model Dissertation

Your WPI Fuel and Power dissertation also uses **Local Projections (LP)**:

$$100 \times \Big[\ln(\text{WPI Fuel}_{t+h}) - \ln(\text{WPI Fuel}_{t-1})\Big] = \alpha_{h} + \beta_{h}\,\Delta\ln(\text{oil}_{t}^{INR}) + \text{lag controls} + \text{month FE} + \varepsilon_{t+h}$$

**Key difference from ADL:**

- ADL: one regression, coefficients on multiple lags
- LP: **separate regression for each horizon** h = 0, 1, 2, ..., 12

**What is "horizon h"?**

- h = 0: "What happens THIS month?" (contemporaneous)
- h = 3: "What happens over the next 3 months?"
- h = 6: "What happens over 6 months?" (your primary benchmark)
- h = 12: "What happens over 12 months?" (medium-run)

$\beta_{h}$ = the cumulative response at horizon h. This traces out an **impulse response function** -- a curve showing how the effect builds over time.

**Why LP?** Each horizon is estimated independently, so errors at one horizon don't contaminate others. It's more robust to misspecification.
