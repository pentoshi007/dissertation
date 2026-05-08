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
