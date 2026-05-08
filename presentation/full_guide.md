# PRESENTATION GUIDE — PART 1: THE BIG PICTURE & YOUR GOAL

---

## What Is This Dissertation About? (The One-Line Answer)

**"I studied how global oil price shocks travel through India's price system — from crude oil all the way to consumer inflation — and found that the shock gets weaker at each step."**

That's it. That's the core story. Now let's break it down.

---

## Why Does This Matter?

India imports about 85% of its crude oil. This oil is priced in US Dollars (USD). So when:

- **Brent crude oil price goes up** -> India pays more for oil
- **Indian Rupee (INR) weakens against the Dollar** -> India pays even MORE for the same oil
- **Both happen together** -> Double trouble for Indian prices

The big question everyone cares about: **"When oil prices rise globally, does it make everything expensive for Indian consumers?"**

Your answer: **"Not exactly. Oil shocks are STRONG in fuel prices but become WEAK by the time they reach headline consumer inflation."**

---

## Your Research Question

> **"How do global oil-price shocks transmit across India's wholesale, retail fuel, fuel-sensitive consumer, and headline consumer price layers, and WHERE does this pass-through WEAKEN?"**

---

## The Key Innovation: "Layered" Approach

Most previous researchers asked: "Does oil price affect CPI (Consumer Price Index)?" — just ONE equation.

**Your approach is different.** You follow the oil shock through FIVE layers of the Indian price system:

```
Layer 1: PPAC Retail Petrol (the petrol pump price)
      |   shock gets weaker
Layer 2: WPI Fuel & Power (wholesale fuel index)
      |   shock gets weaker
Layer 3: CPI Fuel & Light (consumer fuel component)
      |   shock gets weaker
Layer 4: Headline WPI (overall wholesale prices)
      |   shock gets weaker
Layer 5: Headline CPI (overall consumer prices — what RBI targets)
```

**Think of it like dropping a stone in a pond:**
- The splash is BIGGEST where the stone hits (petrol prices)
- The ripples get SMALLER as they spread outward (to headline CPI)

This weakening pattern is called **"LAYERED ATTENUATION"** — the central finding of your work.

---

## Two Pieces of Work

You have TWO documents:

### 1. The Dissertation (longer, ~7,000 words)
- Title: "From wholesale prices to consumer inflation: layered pass-through of global oil shocks in India, 1983–2026"
- Covers ALL five layers using **ADL models** (Autoregressive Distributed Lag)
- Also has a focused WPI Fuel & Power analysis using **Local Projections** (Jordà method)

### 2. The Journal Paper (shorter, ~5,000 words)
- Title: "Layered Oil-Price Pass-Through in India: Evidence from Wholesale, Retail Fuel, and Consumer Prices"
- Same five layers, same ADL method
- Written for the Indian Economic Journal style

**Both tell the same story — layered attenuation of oil shocks in India.**

---

## Key Terminology You Must Know

| Term | Full Form / Meaning |
|------|-------------------|
| **WPI** | Wholesale Price Index — measures prices at the wholesale/producer level |
| **CPI** | Consumer Price Index — measures prices consumers actually pay |
| **Brent** | Brent crude oil — the international benchmark oil price (in USD) |
| **INR/USD** | Indian Rupee per US Dollar exchange rate |
| **PPAC** | Petroleum Planning and Analysis Cell — a government body that tracks fuel prices |
| **OEA** | Office of the Economic Adviser — publishes WPI data |
| **MoSPI** | Ministry of Statistics and Programme Implementation — publishes CPI data |
| **FRED** | Federal Reserve Economic Data — a US database (used for exchange rate data) |
| **ADL** | Autoregressive Distributed Lag — a statistical model that includes past values |
| **HAC** | Heteroskedasticity and Autocorrelation Consistent — a method for reliable standard errors |
| **CPT** | Cumulative Pass-Through — how much of the oil shock reaches a price layer |
| **ADF** | Augmented Dickey-Fuller — a test for whether data has a unit root |
| **KPSS** | Kwiatkowski-Phillips-Schmidt-Shin — another stationarity test |
| **IIP** | Index of Industrial Production — a measure of industrial activity |
| **RBI** | Reserve Bank of India |
| **JEL** | Journal of Economic Literature (classification codes for economics papers) |
# PRESENTATION GUIDE — PART 2: DATA — WHAT, WHERE, WHY

---

## What Data Are You Using?

You use **monthly data** from official Indian and international sources. Here's everything:

### Data Source Table (Know This Cold!)

| Data Series | Source (Full Name) | What It Measures | Time Period |
|---|---|---|---|
| **Brent crude oil price** | World Bank Pink Sheet (monthly commodity prices) | International oil price in USD per barrel | Matched to each layer |
| **INR/USD exchange rate** | FRED EXINUS series (Federal Reserve Bank of St. Louis) | How many rupees per 1 US dollar | Matched to each layer |
| **Headline WPI** | OEA (Office of the Economic Adviser), Ministry of Commerce, chained to 2011-12 base | Overall wholesale price level in India | 1983-05 to 2026-03 |
| **WPI Fuel and Power** | OEA, chained to 2011-12 base | Wholesale prices of fuel, power, light, lubricants | 1995-05 to 2026-03 |
| **PPAC Delhi retail petrol** | PPAC (Petroleum Planning and Analysis Cell), Ministry of Petroleum | Retail petrol price at Delhi pumps | 2004-08 to 2024-12 |
| **CPI Fuel and Light** | MoSPI (Ministry of Statistics and Programme Implementation) | Consumer fuel component of CPI basket | 2011-05 to 2024-12 |
| **Headline CPI** | OECD/FRED series INDCPIALLMINMEI | Overall consumer price level (all items) | 2004-08 to 2024-12 |
| **IIP growth** | MoSPI | Industrial activity control variable | Matched to CPI models |

### Why Different Time Periods?

Each data series starts at a different date because official agencies began publishing them at different times. That's why:

- WPI goes back to 1983 (longest series)
- CPI Fuel and Light only starts in 2011 (shortest)
- This is NOT a problem -- you acknowledge it and handle it properly

---

## How Do You Transform the Data?

### Step 1: Construct the Rupee Oil Price

This is your **key independent variable** (the "shock" variable). The formula is simple:

> **Rupee Oil Price = Brent Price (in USD) x Exchange Rate (INR per USD)**

**In symbols:**

$$\text{oil}_{t}^{INR} = \text{Brent}_{t}^{USD} \times \frac{INR_{t}}{USD_{t}}$$

**What this means in plain English:**

- If Brent oil costs \$80 per barrel, and the exchange rate is Rs.83 per dollar
- Then the rupee oil price = 80 x 83 = Rs.6,640 per barrel
- If either Brent goes UP or the rupee WEAKENS, this number goes UP
- That's the actual cost pressure Indian refiners face

### Step 2: Take Monthly Log Differences (x100)

You don't use raw price levels. You convert everything to **percentage changes**:

$$\Delta x_{t} = 100 \times \Big[\ln(x_{t}) - \ln(x_{t-1})\Big]$$

**What this means in plain English:**

- $\Delta$ (Delta) = "change in"
- $x_{t}$ = value of variable x in month t (this month)
- $x_{t-1}$ = value of variable x in month t-1 (last month)
- $\ln$ = natural logarithm (a mathematical function)
- Multiplying by 100 converts to approximate **percentage change**

**Example:** If WPI was 120 last month and 121.2 this month:

- $\Delta x_{t} = 100 \times [\ln(121.2) - \ln(120)] = 100 \times 0.01 = \textbf{1.0\%}$
- So WPI inflation that month was about 1%

**Why log differences?**

- Raw price levels have "unit roots" (they wander upward without returning)
- You can't do reliable statistics on wandering data
- Log differences make the data **stationary** (stable, mean-reverting)
- Your ADF tests CONFIRM this -- levels are non-stationary, differences ARE stationary

### Step 3: Split into Positive and Negative Shocks

You separate oil price changes into "good news" and "bad news":

$$\Delta x_{t}^{+} = \max(\Delta x_{t},\; 0) \quad\text{-- keeps only POSITIVE changes (oil price went UP)}$$

$$\Delta x_{t}^{-} = \min(\Delta x_{t},\; 0) \quad\text{-- keeps only NEGATIVE changes (oil price went DOWN)}$$

**Why split?** To test **asymmetry** -- does a price INCREASE have the same effect as a price DECREASE? (Spoiler: mostly yes, except maybe for retail petrol)

---

## Unit Root Tests (Why You Can Trust the Data)

Before running models, you test: "Is this data suitable for regression?"

| Variable | Level Form | First Difference |
|---|---|---|
| $\ln(\text{WPI Fuel})$ | NOT stationary (ADF = -2.07) | PASS: Stationary (ADF = -12.05) |
| $\ln(\text{Rupee Oil})$ | NOT stationary (ADF = -3.02) | PASS: Stationary (ADF = -12.94) |
| $\ln(\text{INR/USD})$ | NOT stationary (ADF = -2.18) | PASS: Stationary (ADF = -12.87) |

**What this means:** All variables are I(1) -- "integrated of order 1" -- meaning they need to be differenced once to become usable. Your monthly log differences are the correct transformation.

**If professor asks: "What is a unit root?"**

> "A unit root means the data wanders over time without returning to a fixed average. Like a drunk person walking -- they don't come back to where they started. You can't do reliable regression on such data. Taking first differences removes this problem."

---

## Quick Stats to Remember

| Variable | Mean Monthly Change | Standard Deviation | Range |
|---|---|---|---|
| Rupee oil shock | +0.79% per month | 9.25% | -47% to +40% |
| WPI Fuel and Power | +0.50% per month | 2.33% | -11% to +9% |

**Key point:** Oil shocks are VERY volatile (SD of 9.25%!) compared to WPI Fuel changes (SD of 2.33%). This already hints at incomplete pass-through.
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
# PRESENTATION GUIDE -- PART 4: DIAGNOSTIC TESTS AND WHAT THEY MEAN

---

## What Tests Are You Running and Why?

Before trusting any model's results, you run **diagnostic tests** to check: "Is this model reliable?"

### Test 1: Breusch-Godfrey (BG) Test -- Serial Correlation

**What it checks:** "Are the residuals (errors) correlated with each other?"

**Why it matters:** If errors from month 1 predict errors from month 2, the model is missing some pattern in the data.

**How to read it:**

- High p-value (> 0.05) -> PASS -> No serial correlation detected -> Good!
- Low p-value (< 0.05) -> FAIL -> Serial correlation present -> BUT you use Newey-West HAC errors, which handle this, so it's not fatal

### Test 2: RESET Test (with HAC) -- Functional Form

**What it checks:** "Is a LINEAR model the right shape, or should there be curves/nonlinearities?"

**Full name:** Ramsey Regression Equation Specification Error Test

**How to read it:**

- High p-value (> 0.05) -> PASS -> Linear model is adequate
- Low p-value (< 0.05) -> FAIL -> The model might be too simple

**Important:** WPI Fuel and Power FAILS this test -> that's why it gets a "functional form caveat"

### Test 3: Recursive CUSUM -- Parameter Stability

**What it checks:** "Do the model's coefficients stay stable over time, or do they shift?"

**Full name:** Cumulative Sum of Recursive Residuals

**How to read it:**

- p-value > 0.05 -> PASS -> Parameters are stable over the sample
- p-value < 0.05 -> FAIL -> Something changed structurally mid-sample

### Test 4: Bootstrap Symmetry Test

**What it checks:** "Is the $CPT^{+} = CPT^{-}$ result real, or could it be a fluke?"

**How it works:**

1. Take the data, resample it randomly 4,999 times (with replacement)
2. For each resample, estimate the model and compute the Wald statistic for $CPT^{+} = CPT^{-}$
3. See where your ACTUAL Wald statistic falls in the distribution of 4,999 bootstrap statistics
4. If your actual statistic is extreme -> asymmetry is real; if not -> symmetry holds

### Test 5: ADF and Phillips-Perron -- Unit Root Tests

**What they check:** "Does this data wander or is it stable?"

- Wandering data (unit root) -> can't run regressions on levels
- Stable data (stationary) -> safe to use

### Test 6: KPSS Test -- Stationarity Test

**What it checks:** The OPPOSITE of ADF -- here the null hypothesis is that data IS stationary.

- If KPSS rejects -> data is NOT stationary (needs differencing)
- Useful as a cross-check alongside ADF

### Test 7: Bai-Perron Test -- Structural Breaks

**What it checks:** "Are there specific dates where the relationship fundamentally changed?"

- Relevant because fuel pricing policy changed in 2010 and 2014

---

## The "Model Gate" -- How You Decide Which Models to Trust

You use a strict **diagnostic triage** system:

| Gate Status | Criteria | What It Means |
|---|---|---|
| **PASS (Claim-bearing)** | Passes BG + RESET + CUSUM | Full confidence -- use for main conclusions |
| **CAVEAT (Mechanism evidence)** | Passes 2 of 3 | Report the result BUT note the failing test |
| **REJECT (Excluded)** | Fails 2 or more tests | Do NOT use for main claims |

### Which models pass the gate?

| Model | BG Test | RESET Test | CUSUM Test | Gate Status |
|---|---|---|---|---|
| Headline WPI | PASS | PASS | PASS | **MAIN RESULT** |
| WPI Fuel and Power | PASS | FAIL | PASS | **Mechanism with caveat** |
| PPAC Retail Petrol | PASS | PASS | PASS | **MAIN RESULT** |
| Headline CPI (M1) | PASS | PASS | PASS | **MAIN RESULT** |
| CPI Fuel and Light bridge | PASS | PASS | PASS | **Bridge evidence** (short sample) |
| CPI M2, M3 (alternatives) | Various failures | -- | -- | **EXCLUDED** |

**If professor asks: "Why did you exclude M2 and M3?"**

> "M2 and M3 are alternative CPI specifications that fail the diagnostic gate. Their residuals show problems with serial correlation or functional form. Including them would make claims based on unreliable models. I follow a strict diagnostic triage: only models that pass the mandatory checks carry the main conclusions."

---

## The Granger Causality / Predictive Precedence Tests

**What it checks:** "Do past oil price changes PREDICT future price index changes?"

**Important caveat:** This is NOT proof of causation! It only shows "predictive precedence."

### Key Results:

| Direction | F-statistic | p-value | Verdict |
|---|---|---|---|
| Rupee oil -> Headline WPI | 7.43 | < 0.001 | Oil predicts WPI |
| Rupee oil -> WPI Fuel and Power | 15.22 | < 0.001 | Oil strongly predicts WPI Fuel |
| Brent -> PPAC Petrol | 10.71 | < 0.001 | Brent strongly predicts petrol |
| Rupee oil -> Headline CPI | 2.29 | 0.0794 | Marginal (10% level only) |
| PPAC Petrol -> CPI Fuel and Light | -- | 0.1126 | Not clearly significant |
| WPI -> Oil (reverse) | -- | -- | Not supported |

**Pattern:** Oil predicts fuel prices strongly, but the signal fades at broader price levels. This matches your main attenuation finding!
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
