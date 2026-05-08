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
