---
title: "Dissertation Study Guide"
subtitle: "Oil-Price Pass-Through in India: A Beginner's Companion to the Methodology, Tests, Numbers, and Defence"
author: "Aniket Pandey · Centre for Economic Studies and Planning, JNU"
date: "April 2026"
geometry: margin=1in
fontsize: 11pt
linestretch: 1.15
toc: true
toc-depth: 2
numbersections: false
colorlinks: true
linkcolor: NavyBlue
urlcolor: NavyBlue
toccolor: black
header-includes:
  - \usepackage{amsmath,amssymb,booktabs,longtable,array,pdflscape,ragged2e}
  - \usepackage{microtype}
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}\fancyhf{}\fancyhead[L]{Pass-Through Study Guide}\fancyhead[R]{\thepage}\renewcommand{\headrulewidth}{0pt}
  - \newenvironment{keybox}{\par\medskip\noindent\hrule\smallskip\itshape}{\par\smallskip\hrule\medskip}
  - \newcommand{\diff}{\Delta}
  - \setlength{\emergencystretch}{3em}
  - \setlength{\tabcolsep}{4pt}
  - \renewcommand{\arraystretch}{1.12}
---

\clearpage

# Chapter 0 — How to read this guide

This final version combines the fuller explanatory guide with the exact coefficient tables from the R output, rebuilt with safer table layouts. This document exists because you did not write your dissertation from scratch. The text, the R pipeline, and the econometric design were largely AI-generated, and you are now expected to defend it in front of a viva committee that may include your supervisor (Prof. Shakti Kumar) and an external examiner. The goal of this guide is to make sure that, by the time you walk into that room, every equation, every test, every number, and every claim in the dissertation is something you can explain, justify, and — where necessary — concede the limits of.

**The guide is built bottom-up.** Chapter 2 starts from "what is a time series" and assumes nothing. By the time you reach Chapters 4 and 5 (ADL and NARDL), you should be reading them as the natural next step rather than as new vocabulary. Chapters 6–8 walk through the actual numbers your code produced. Chapter 9 is brutally honest about what the dissertation cannot do — read this *before* the viva, not after. Chapter 10 is a question bank with answers in your own voice; rehearse those out loud.

**How to use it in the run-up to the viva.**

1. Read it once cover-to-cover. Slow on Chapters 2 and 6 (concepts and tests); fast on Chapter 7 (results) the first pass.
2. On the second pass, re-read Chapter 7 with the dissertation open beside it, and locate every number from the text inside the tables in `models/cpi/outputs/tables/` and `models/wpi/outputs/tables/`. If you can find a number you cannot recompute by eye from one of those CSVs, that is a number you do not yet own.
3. On the third pass, treat Chapter 10 as flashcards. Cover the answer; speak yours; uncover; compare.
4. Read Appendix A (annotated R) at least once so that when an examiner says "show me where in the code you do X", you can name the script.

**Conventions used.**
\(\diff y_t = \ln y_t - \ln y_{t-1}\) is the month-on-month log difference (multiplied by 100 in the code so coefficients read in percent). \(\text{CPT}^+ = \sum_{j=0}^{q} \beta_j^+\) is the cumulative pass-through from positive shocks; \(\text{CPT}^-\) is its negative-shock twin. "HAC" means Newey–West heteroskedasticity-and-autocorrelation-consistent standard errors. "RR-CBB" means restricted-residual circular block bootstrap.

**One disclaimer.** Where the code does something the dissertation text glosses over, or where I think an examiner is likely to push, this guide flags it explicitly with a "Watch out" box. Read those carefully — they are the places you can be ambushed. Do not memorise around them; if asked, concede the limit honestly and pivot to what the result *does* support. That posture is more defensible than overclaiming.

\clearpage

# Chapter 1 — The research question in plain English

## 1.1 The puzzle

India imports roughly 87 percent of its crude oil. When global oil prices move, that change has to enter the Indian economy somewhere. The strange thing is that it shows up loudly in some prices and very quietly in others. If you watch the pump price of petrol in Delhi, an oil shock is obvious within weeks. If you watch the headline Consumer Price Index — the one the Reserve Bank of India targets at 4 percent — you can barely see the shock at all. Both pictures are true at the same time. Your dissertation is an attempt to figure out *where in the price system the shock weakens*, and by how much, at each link of the chain.

## 1.2 The chain

The dissertation thinks of pass-through as a layered process, not a single elasticity. The chain is:

\begin{center}
Brent crude (USD) \(\times\) INR/USD \(\to\) \textbf{Rupee oil price} \(\to\) Retail petrol (PPAC, Delhi) \(\to\) WPI Fuel \& Power \(\to\) CPI Fuel \& Light \(\to\) Headline WPI / Headline CPI
\end{center}

Each arrow is a place where the shock can be amplified, attenuated, or delayed. Refiners' margins, oil marketing companies' price-revision rules, central and state excise on fuel, the basket weights of WPI versus CPI, and substitution by households — every one of these mediates one of the arrows. The "research question" is *which arrow is doing most of the absorbing*, and whether the institutional move from administered to market-linked petrol pricing in June 2010 changed the answer.

## 1.3 Why "asymmetric" pass-through?

A pass-through is *symmetric* if a +5 percent oil shock and a –5 percent oil shock move the dependent price by the same magnitude (in opposite directions). It is *asymmetric* — sometimes called "rockets and feathers" — if positive shocks are passed on faster or more fully than negative ones. The folklore: when crude rises, pump prices rise like a rocket; when crude falls, pump prices come down like a feather. Oil marketing companies and retail petrol distributors are the most-frequently-suspected culprits for this kind of behaviour, since they have pricing power within the regulatory window.

The dissertation tests this by splitting the rupee-oil log difference into a positive and a negative component:

$$\diff x_t^{+} = \max(\diff x_t, 0), \qquad \diff x_t^{-} = \min(\diff x_t, 0).$$

By construction \(\diff x_t = \diff x_t^{+} + \diff x_t^{-}\). You then estimate separate cumulative responses \(\text{CPT}^+\) and \(\text{CPT}^-\) and ask, with a Wald test, whether they are equal. Failing to reject that equality means the data do not support an asymmetry story.

**Concrete example.** Suppose Brent rises 10 percent for three months and then falls 10 percent for three months. A symmetric model says the cumulative effect on petrol prices over the six months is roughly zero. A "rockets-and-feathers" model says petrol moved up 7 percent on the rises and only came down 4 percent on the falls, leaving a residual price level 3 percent higher than where it started — pure margin captured by the seller. Whether that gap is real, in your data, is what the asymmetry test asks.

## 1.4 What "attenuation along the chain" means

"Attenuation" means the shock loses amplitude as it travels. Imagine clapping in a long tunnel: the sound that reaches the far end is the same sound, but quieter. In the price chain, a 1 percent rise in the rupee oil price might produce roughly a 0.35 percent cumulative rise in retail petrol over a few months, a 0.29 percent rise in WPI Fuel & Power, a 0.18 percent rise in the CPI Fuel & Light bridge, but only a 0.03 percent rise in headline WPI and a statistically insignificant 0.02 percent rise in headline CPI. The shock has not disappeared — most of it is sitting in the fuel-sensitive layers — but the household-facing aggregate that monetary policy targets sees only a faint echo. That ordering is the central empirical claim of the dissertation. The order-of-magnitude drop happens at the transition from the fuel-sensitive layers to the headline aggregates, which is exactly where basket weights, taxes, and substitution dilute the signal.

\begin{keybox}
\textbf{One-sentence summary.} The dissertation maps an oil shock through five points of the Indian price system and shows that the shock is strong upstream (retail fuel and fuel sub-indices), small but visible in headline WPI, and statistically indistinguishable from zero in headline CPI; short-run asymmetry is at most marginal, only at the retail-petrol layer.
\end{keybox}

## 1.5 Why this matters for India and for the RBI

Since 2016, the Monetary Policy Committee anchors policy on headline CPI inflation with a 4 percent target band. If oil shocks barely move headline CPI, two things follow. First, the inflation-targeting framework looks unresponsive to oil shocks even when upstream prices are moving violently — which makes communication awkward. Second, you cannot conclude that the economy is "insulated" from oil; the shock is hiding in WPI Fuel & Power and in retail fuel, which feed into producer costs, transport, fertilizer, and eventually — with long lags and through indirect channels — into the very CPI components that are dominated by food and services. The policy interpretation in the dissertation is restrained: WPI is where oil shocks remain visible at the headline level; CPI is where they are diluted. Neither index substitutes for the other.

The pre/post-2010 split adds a second policy-relevant observation. Petrol was deregulated in June 2010 and diesel in October 2014. After deregulation, oil marketing companies revise pump prices much more frequently, so the empirical pass-through that any econometric model can detect mechanically goes up. The dissertation reports this for the wholesale layers: pre-2010 headline-WPI \(\text{CPT}^+\) is 0.012 (not significant), post-2010 it jumps to 0.074 (\(p = 0.004\)); pre-2010 Fuel-and-Power \(\text{CPT}^+\) is 0.092 (not significant), post-2010 it leaps to 0.524 (\(p < 0.001\)). The honest reading is that this is *consistent with* deregulation rather than a clean causal estimate of it — too many other things changed in the same window (new CPI series in 2011, flexible inflation targeting in 2016, GST in 2017, repeated excise adjustments).

\clearpage

# Chapter 2 — Time-series concepts, built from zero

You cannot defend an ADL or an NARDL without these concepts. Each section below gives a one-line intuition, a fuller explanation, and the specific reason your dissertation needs the concept.

## 2.1 Time series, lag operator, white noise

A **time series** is a sequence of observations on the same variable taken at regular intervals — here, monthly. We write \(y_t\) for the value at month \(t\) and \(y_{t-1}\) for the previous month. The **lag operator** \(L\) is just shorthand: \(L y_t = y_{t-1}\), \(L^2 y_t = y_{t-2}\). It is convenient because models like \((1 - 0.4 L) y_t = \varepsilon_t\) are easier to read than spelling out lagged terms.

**White noise** is a sequence \(\varepsilon_t\) with three properties: mean zero, constant variance, and zero autocorrelation at every nonzero lag. It is the "no information left" benchmark — if your residuals look like white noise, the model has captured the systematic part of the data.

*Why your dissertation needs this.* The whole inferential apparatus in the ADL — t-tests, cumulative-pass-through tests, Wald tests — assumes the residual process is well-behaved (close to stationary, with bounded autocorrelation). The Newey–West HAC correction and the Breusch–Godfrey serial-correlation test exist precisely because in finite samples the residual is *almost* white noise but not quite.

## 2.2 Autocorrelation

Autocorrelation is the correlation of a series with its own past. If today's inflation is highly correlated with last month's inflation, the series is autocorrelated at lag 1. In economic time series, autocorrelation is the rule, not the exception — momentum, sticky prices, and seasonal patterns all create it.

The **autocorrelation function (ACF)** plots correlation at lag 1, 2, 3, …. A persistent series like a level CPI has an ACF that decays only slowly; a log-difference of CPI typically has small ACF values at all but the first few lags.

*Why this matters.* Two reasons. First, residual autocorrelation breaks OLS standard errors (they become too small) — that is the whole reason for HAC standard errors below. Second, the very fact that the dependent variable is autocorrelated is why you put own lags on the right-hand side of an ADL.

## 2.3 Stationarity and non-stationarity

A series is **(weakly) stationary** if its mean, variance, and autocovariance structure do not depend on the calendar date. Practically: if you slid the series along the time axis, you could not tell where the original window was.

A series is **non-stationary** if any of those moments drift over time. The level of the WPI is non-stationary — its mean is rising decade after decade. The log-difference of the WPI is far closer to stationary — month-on-month inflation has roughly the same average and the same volatility across the sample.

**Analogy.** Stationary series are people on an exercise treadmill: they shuffle around but stay in roughly the same place. Non-stationary series are people walking down a corridor: they meander, but they also drift in one direction.

## 2.4 Unit roots and the integration order I(0), I(1), I(2)

A **unit root** is the most common kind of non-stationarity. Consider an AR(1) process \(y_t = \rho y_{t-1} + \varepsilon_t\). If \(|\rho| < 1\), shocks die out and the series is stationary. If \(\rho = 1\), every shock persists forever and the series is a *random walk* — it has a unit root.

**Drunkard's-walk analogy.** A drunkard takes a random step of size \(\varepsilon_t\) every period. After \(T\) steps, his expected position is wherever he started, but his variance grows linearly with \(T\) — he can wander arbitrarily far, and where he ends up is permanently shifted by every push he received along the way. That is what a unit-root process does to shocks.

We classify series by their **order of integration**:

- **I(0)** — already stationary in levels. Example: a stationary AR(1) with \(|\rho| < 0.99\).
- **I(1)** — non-stationary in levels but becomes stationary after taking first differences. Most macroeconomic price levels (CPI, WPI, exchange rates, oil prices in levels) are I(1).
- **I(2)** — needs differencing twice to become stationary. Rare, sometimes seen in nominal aggregates during very high inflation.

Your unit-root tables (`table_03_unit_root_battery.csv` for CPI, `table_13_unit_root_battery.csv` for WPI) report ADF, PP and KPSS tests in levels and in first differences. The verdict in both: log-CPI, log-WPI, log-Brent, log-EXR, log-rupee-oil are all I(1) in levels and I(0) in first differences. IIP comes out borderline (ADF rejects in levels but KPSS does not, which is a textbook ambiguous case — see §2.5).

*Why this matters.* If two non-stationary series are regressed on each other in levels without sharing a unit root, you get **spurious regression** (next section). The ADL specification in the dissertation operates on first differences, so the integration concern is sidestepped — but you still report the unit-root battery so the reader can see that differencing is justified.

## 2.5 Why three different unit-root tests?

Each of ADF, PP, and KPSS has different power and different size in different situations, and they have *opposite* nulls.

| Test | Null \(H_0\) | Alternative \(H_1\) | Reject \(H_0\) means |
|---|---|---|---|
| Augmented Dickey–Fuller (ADF) | unit root | stationary | series is stationary |
| Phillips–Perron (PP) | unit root | stationary | series is stationary |
| KPSS (Kwiatkowski et al.) | stationary | unit root | series has a unit root |

KPSS is the *complementary* test. The clean classifications are:

- ADF rejects + KPSS fails to reject \(\Rightarrow\) **I(0)** with confidence.
- ADF fails to reject + KPSS rejects \(\Rightarrow\) **I(1)** with confidence.
- ADF rejects + KPSS rejects, or both fail \(\Rightarrow\) ambiguous; consider the economics.

In your tables, the level-form battery for log-CPI, log-WPI etc. shows ADF failing to reject and KPSS rejecting — clean I(1). The first-difference battery shows ADF rejecting and KPSS failing to reject — clean I(0). That is exactly what you need.

## 2.6 Spurious regression

If \(y_t\) and \(x_t\) are independent random walks (so the truth is no relationship), running OLS of \(y_t\) on \(x_t\) in levels produces, on average, a *significant* coefficient and a high \(R^2\). The standard errors are wrong because the residuals are non-stationary. Granger and Newbold (1974) demonstrated this empirically; Phillips (1986) gave the theory.

*The lesson the dissertation lives by.* You cannot just regress log-CPI on log-oil and report the slope. You must either (a) work in differences (which is what the main ADL specifications do), or (b) work in levels but inside a cointegrated framework with an error-correction term (which is what the supplementary NARDL appendix does, with the bounds test verifying that a long-run relationship exists).

## 2.7 Cointegration and long-run relationships

Two I(1) series \(y_t\) and \(x_t\) are **cointegrated** if some linear combination \(y_t - \beta x_t\) is I(0) — that is, even though each series wanders on its own, they wander *together*. Economically, cointegration is what "long-run equilibrium" looks like in the data.

**Rubber-band analogy.** Tie one end of a rubber band to a dog and the other to a person walking down a long road. Both wander; the dog dashes after squirrels, the person stops to look at shop windows. But the rubber band keeps them within a bounded distance. The deviation from the long-run leash length is stationary even though the locations are not.

**Error-correction.** If \(y\) and \(x\) are cointegrated, the model that captures both short-run dynamics and the pull toward the long-run can be written
$$\diff y_t = \alpha + \gamma\,(y_{t-1} - \beta x_{t-1}) + \text{(short-run lags)} + \varepsilon_t,$$
where the term in brackets is the deviation from long-run equilibrium. The coefficient \(\gamma\) is the **speed of adjustment**, and it must be negative and significant for the model to make sense — it says "if \(y\) is above its long-run value, pull it back down next month."

In the WPI NARDL appendix table (`table_07_nardl_summary.csv`), the ECT coefficients are −0.019 (Brent), −0.019 (Brent\|EXR), −0.017 (rupee-oil) and −0.081 (Fuel & Power on rupee-oil). All negative, all significant — formally consistent with cointegration. But note: the dissertation reads these as *descriptive* speed-of-adjustment numbers, not as structural disequilibrium parameters, and that caveat is correct.

## 2.8 Short-run vs long-run dynamics

A coefficient on \(\diff x_t\) (today's shock) is a short-run impact. The **cumulative pass-through** \(\text{CPT}^+ = \sum_{j=0}^q \beta_j^+\) sums the responses across the model's lag window — that is your dissertation's main object of interest, the medium-run cumulative response. The **long-run multiplier** in a levels ARDL/NARDL is the steady-state response: it is computed as \(-\beta_x / \beta_y\) where \(\beta_y\) is the level coefficient on lagged dependent and \(\beta_x\) is the level coefficient on the regressor. The ARDL appendix reports long-run coefficients in `table_08_nardl_long_run.csv`.

## 2.9 Heteroskedasticity, serial correlation, and HAC

**Heteroskedasticity** means residual variance changes with \(t\) (or with the regressors). **Serial correlation** means residuals are correlated across time. OLS coefficient estimates remain unbiased under both, but the *standard errors* are wrong, which means t-statistics and p-values are unreliable.

The **Newey–West HAC** estimator adjusts the variance of the OLS coefficient vector to be robust to both heteroskedasticity and to autocorrelation up to a chosen bandwidth. Concretely, it inflates the OLS variance estimate by a weighted sum of cross-products of lagged residuals; the weights come from the Bartlett (triangular) kernel and decay smoothly to zero at the bandwidth. Your code uses `sandwich::NeweyWest(..., prewhite = FALSE)` with a project-specific bandwidth \( \lfloor 0.75 n^{1/3} \rfloor \) from `nw_lag(n)`.

*Why your dissertation needs it.* Macroeconomic monthly residuals are almost always autocorrelated (especially through seasonality) and often heteroskedastic (volatility clustering during crises). Without HAC, your \(\text{CPT}^+\) p-values would be artificially small, and you would over-reject the null of zero pass-through.

\begin{keybox}
\textbf{Quick checklist of when HAC is the right move.} The model is OLS in differences (so the regressors are stationary), the residuals show short-lag serial correlation (Breusch–Godfrey rejects), and the sample is moderately long ($T \ge 100$). All three apply to your specifications.
\end{keybox}

\clearpage

# Chapter 3 — The variables and the data

## 3.1 Where each series comes from

| Variable | What it measures | Source | Frequency | Active sample |
|---|---|---|---|---|
| Brent crude (USD/bbl) | International benchmark crude price | World Bank Pink Sheet via FRED, series `POILBREUSDM` | Monthly | 1983-05 → 2026-03 |
| INR/USD exchange rate | Monthly average rupee per dollar | FRED `EXINUS` | Monthly | 1983-05 → 2026-03 |
| Rupee oil price | Brent \(\times\) INR/USD | constructed | Monthly | 1983-05 → 2026-03 |
| Headline WPI | All-commodities wholesale price index, chained to 2011-12 = 100 | Office of the Economic Adviser (OEA), MoCI; chained from 1981-82, 1993-94, 2004-05 vintages | Monthly | 1983-05 → 2026-03 |
| WPI Fuel & Power | Fuel and power group of WPI, chained to 2011-12 = 100 | OEA; chained from 1993-94 and 2004-05 vintages | Monthly | 1995-05 → 2026-03 |
| PPAC retail petrol (Delhi) | Pump price of petrol in Delhi | Petroleum Planning and Analysis Cell ready reckoner | Monthly | 2004-08 → 2024-12 |
| Headline CPI | All-India general consumer price index | MoSPI; cross-checked against FRED `INDCPIALLMINMEI` | Monthly | 2004-08 → 2024-12 |
| CPI Fuel & Light (bridge) | Fuel and light component of CPI, harmonised post-2011 | MoSPI | Monthly | 2011-05 → 2024-12 |
| IIP (activity control) | Index of Industrial Production, chained | MoSPI; chain-link constructed in `chain_link_iip.py` | Monthly | matched to layer |

## 3.2 Transformations

Every model variable is in **month-on-month log differences** (multiplied by 100 in the R code, so coefficients read in percentage points):

$$\diff y_t = 100 \cdot \big(\ln y_t - \ln y_{t-1}\big).$$

Why log differences and not level changes? Three reasons. (1) Logs put proportional changes on a common scale, so a 5% rise in a Rs.100 series and a 5% rise in a Rs.10,000 series produce the same \(\diff\). (2) Differencing kills the unit root in I(1) series and avoids spurious-regression problems. (3) The resulting series is approximately a percentage change, which is how inflation is reported and how the cumulative-pass-through coefficient is interpreted.

The asymmetric components are then constructed as
$$\diff x_t^{+} = \max(\diff x_t, 0), \qquad \diff x_t^{-} = \min(\diff x_t, 0).$$

Note the sign convention: \(\diff x_t^{-}\) is the *negative* part with its sign preserved (it is \(\le 0\)), so \(\beta^{-}\) is the coefficient on a negative number; a positive \(\beta^{-}\) means negative oil shocks pull the dependent series down. This convention is what `pmin(dln_oil, 0)` produces in the code — be ready to explain it.

## 3.3 The WPI splice — the most technical part of the data

OEA publishes the WPI under successive base years. To build a continuous monthly headline series from May 1983 to March 2026 you need to chain four vintages: 1981-82, 1993-94, 2004-05, and 2011-12. The official linking factors used in your code (`models/wpi/R/00_config.R`) are:

| Step | Linking factor (headline) | Linking factor (Fuel & Power) |
|---|---|---|
| 1981-82 \(\to\) 1993-94 | 2.478 | n/a (Fuel \& Power chain begins 1993-94) |
| 1993-94 \(\to\) 2004-05 | 1.873 | 2.802 |
| 2004-05 \(\to\) 2011-12 | 1.561 | 1.690 |

The mechanics: a 1981-82-base index value is converted to the 2011-12 base by *dividing* through the product of all the relevant chain factors. So in `02_build_data.R` you see, for the 1981-82 segment:

```
chained_2011 = raw_value / prod(CHAIN_FACTORS$headline)
```

which is `raw / (2.478 × 1.873 × 1.561)`, about `raw / 7.245`. For 1993-94 base, it divides by `1.873 × 1.561`, about `2.924`. For 2004-05 base, by `1.561`. For 2011-12 base, no division.

The splice is then *checked* by inspecting the joined values at the boundary months in `table_03_splice_checks.csv`. The dissertation acknowledges that the OEA component definitions for "Fuel & Power" changed across vintages, so the chain at the *component* level is less perfect than the chain at the *headline* level — this is a known limit and is one place an examiner could push.

\begin{keybox}
\textbf{Watch out — splice fragility at the component level.} Headline WPI has been reweighted across base years and the chain factors are official; the resulting series is fine for the long-horizon ADL. The Fuel \& Power group, by contrast, had basket coverage changes across the 1993-94 and 2004-05 vintages (the inclusion of mineral oils and the treatment of electricity differed). The dissertation's statement is that the longest internally consistent stretch is preferred over a shorter, perfectly homogeneous stretch; you may have to defend that trade-off explicitly. The honest answer: any pre-2010 Fuel \& Power splice at component-level granularity carries definitional noise, and that is precisely why the post-2010 sub-sample (which uses only the 2011-12 base) is treated as the cleaner subsample for that layer.
\end{keybox}

## 3.4 Variable map: dissertation symbol \(\leftrightarrow\) R object

| Dissertation symbol / phrase | R object / column | Where built |
|---|---|---|
| \(y_t\) (headline WPI) | `dln_dep` in `headline_model_data` | `02_build_data.R` |
| \(y_t\) (Fuel & Power) | `dln_dep` in `fuel_model_data` | `02_build_data.R` |
| \(y_t\) (headline CPI) | `dlnCPI` in `df` | `models/cpi/R/03_variable_builder.R` |
| \(y_t\) (CPI Fuel & Light bridge) | `dlnFuel` in `df_fuel` | `09_mechanism_chain.R` |
| \(y_t\) (PPAC retail petrol) | `dlnPetrol` in `df_petrol` | `09_mechanism_chain.R` |
| \(\diff x_t\) rupee oil | `dlnOil` (CPI) / `dln_oil` (WPI) | both `03_variable_builder.R` and `02_build_data.R` |
| \(\diff x_t^{+}\) | `dlnOil_pos` / `dln_oil_pos` | same |
| \(\diff x_t^{-}\) | `dlnOil_neg` / `dln_oil_neg` | same |
| Brent log-difference | `dlnBrent` / `dln_brent` | same |
| EXR log-difference | `dln_exr` | same |
| activity control | `dlnIIP` | `03_variable_builder.R` |
| month-of-year FE | `mo_Jan, ..., mo_Nov` (CPI) or `month` (WPI) | `06_models.R` / `03_models.R` |
| petrol-deregulation dummy | `D_petrol` (= 1 from 2010-06) | `03_variable_builder.R` |
| diesel-deregulation dummy | `D_diesel` / `d_reform` (= 1 from 2014-10) | `03_variable_builder.R` / `02_build_data.R` |
| COVID dummy | CPI: `D_covid` (= 1 only in 2020-04); WPI: `d_covid` (= 1 over 2020-04 to 2020-09) | `03_variable_builder.R` / `02_build_data.R` |

## 3.5 Lag structure used in each layer

This is the table you should be able to recite verbatim.

| Layer | Dependent | Shock variable | Own lags \(p\) | Shock lags \(q\) |
|---|---|---|---|---|
| Headline WPI | dln(WPI) | dln(rupee oil) split | 12 | 0–6 |
| WPI Fuel & Power | dln(Fuel & Power) | dln(rupee oil) split | 12 | 0–6 |
| PPAC retail petrol | dln(petrol Delhi) | dln(Brent USD) split | 3 (AIC-selected) | 0–3 |
| CPI Fuel & Light bridge | dln(Fuel & Light) | dln(PPAC petrol) split | 3 | 0–3 |
| Headline CPI | dln(CPI) | dln(rupee oil) split | 3 (AIC-selected) | 0–3 |

\begin{keybox}
\textbf{Watch out — text vs code on lag length.} Section 3.5 of the dissertation (Table 3.2) lists the CPI/petrol layers as \(p = 6\), \(q = 0\)–4. The R code (\texttt{06\_models.R}) selects \(p\) by AIC over \(p \in \{1,2,3,4\}\) on a common sample, and the AIC minimum is at \(p = 3\) (table\_05b\_lag\_selection.csv: AIC values 440.58, 440.13, 438.79, 440.67 for \(p=1..4\); BIC and HQC pick \(p=1\)). The oil-lag depth used is \(q = 3\) (lags 0,1,2,3), set by theory rather than tuned. So the actual specification is ADL(3,3), not ADL(6,4). If asked: "I report headline CPI with \(p = 3\) selected by AIC and \(q = 3\) chosen by theory, consistent with the Indian pass-through literature; I confirmed in the lag-sensitivity check that varying \(q\) between 0 and 8 does not overturn the qualitative result." Concede the typo in the table if pressed.
\end{keybox}

## 3.6 Two descriptive features worth knowing

First, the rupee-oil log-difference has visibly fat negative tails — 2008, 2014–15, 2020 — and fat positive tails — 2007–08, 2011–12, 2022. That is what motivates the asymmetric specification at all; if the distribution were symmetric and Gaussian, you would not bother splitting.

Second, the eyeball co-movement between dln(rupee oil) and dln(WPI Fuel & Power) is strong across the entire sample, and the eyeball co-movement between dln(rupee oil) and dln(headline CPI) is weak. The naked-eye pattern is consistent with the layered attenuation result. An examiner who asks "did you look at the data before estimating?" should be answered with this point and Figure 3.1 / 3.2.

\clearpage

# Chapter 4 — The ADL model, fully explained

## 4.1 What an ADL is

An **autoregressive distributed-lag** model is a regression of a dependent variable on its own lags *and* on current and lagged values of one or more regressors. The general ADL\((p, q)\) is

$$y_t = \alpha + \sum_{i=1}^{p} \varphi_i\, y_{t-i} + \sum_{j=0}^{q} \beta_j\, x_{t-j} + \varepsilon_t.$$

"Autoregressive" because of the own lags \(y_{t-i}\); "distributed lag" because of the lagged regressor terms \(x_{t-j}\). It nests a static OLS regression (\(p = q = 0\)), a pure AR (drop \(x\)), and a pure distributed lag (drop the AR part). Properly specified, it is the workhorse short-run dynamics model in macro-time-series.

## 4.2 The asymmetric ADL used in the dissertation

You are not estimating a textbook ADL — you are estimating an **asymmetric** ADL, where the regressor is split into positive and negative components. The full specification (equation 4.3 in the dissertation) is:

$$\diff y_t = \alpha + \sum_{i=1}^{p} \varphi_i\, \diff y_{t-i} + \sum_{j=0}^{q} \beta_j^{+}\, \diff x_{t-j}^{+} + \sum_{j=0}^{q} \beta_j^{-}\, \diff x_{t-j}^{-} + Z_t' \gamma + \mu_m + \varepsilon_t,$$

where:

- \(\diff y_t\) is the log-difference of the dependent price index (CPI, WPI, Fuel & Power, retail petrol, or CPI Fuel & Light);
- \(\diff x_t\) is the log-difference of the shock variable (rupee oil for headline WPI / Fuel & Power / headline CPI; Brent for retail petrol; PPAC petrol for CPI Fuel & Light);
- \(\diff x_t^{+} = \max(\diff x_t, 0)\) and \(\diff x_t^{-} = \min(\diff x_t, 0)\);
- \(p\) is the **own-lag order** (12 for the long WPI specs, 3 elsewhere);
- \(q\) is the **distributed-lag order** on the oil components (6 for the long WPI specs, 3 elsewhere);
- \(Z_t\) is a vector of controls — typically \(\diff\)IIP and the contemporaneous and lag-1 EXR log-difference for the WPI specs;
- \(\mu_m\) are calendar-month fixed effects (Jan, Feb, …, Nov; December is the omitted baseline);
- \(\varepsilon_t\) is the residual.

For the long-horizon WPI specs there are also two policy-event dummies — `d_reform` (= 1 from October 2014 onward, the diesel-deregulation date) and `d_covid` (= 1 over April–September 2020) — included only in the Fuel & Power specification. For the CPI specs there are three: `D_petrol` (post-June-2010), `D_diesel` (post-October-2014), and `D_covid`.

## 4.3 What each parameter means in plain English

\(\alpha\) is a constant — a baseline drift in the dependent log-difference, conditional on the controls.

\(\varphi_i\) (own lag coefficients) capture **inflation persistence**: if last month's inflation was high, this month's tends to be too. The sum \(\sum \varphi_i\) is the persistence parameter; if it is well below 1 the differenced series mean-reverts at the inflation level (which is what we want).

\(\beta_j^{+}\) is the **j-period-ahead response of the dependent log-difference to a one-percent positive shock to the rupee oil price**. \(\beta_0^{+}\) is the contemporaneous response; \(\beta_1^{+}\) is the response one month later; and so on. \(\beta_j^{-}\) is the analogous response to negative shocks (remember the sign convention: \(\diff x^{-}\) is non-positive, so a positive \(\beta^{-}\) means oil falls drag the dependent series down).

\(\gamma\) coefficients on the controls are nuisance parameters; they are not the object of interest, they are there to keep \(\beta\) consistent.

\(\mu_m\) absorb seasonality — the systematic January-vs-July difference in inflation, which would otherwise contaminate the oil coefficients.

## 4.4 The cumulative pass-through (the headline number)

The single most important quantity in the whole dissertation is

$$\text{CPT}^{+} = \sum_{j=0}^{q} \beta_j^{+}, \qquad \text{CPT}^{-} = \sum_{j=0}^{q} \beta_j^{-}.$$

It answers: "if the rupee oil price rises 1%, what is the cumulative percentage response of the dependent series over the lag window of the model?" \(\text{CPT}^{+} = 0.030\) means a 1% positive oil shock is associated with a 0.03% cumulative rise in headline WPI over the \(q = 6\) lag window. \(\text{CPT}^{+} = 0.346\) for retail petrol means a 1% positive Brent shock is associated with a 0.346% cumulative rise in pump prices.

The CPT is *not* a long-run multiplier. It is a finite-horizon cumulative response in a differenced model — closer to "the impulse response summed over \(q+1\) months" than to "the steady-state elasticity". An examiner familiar with NARDL may try to lure you into calling it the long-run multiplier; do not. The long-run multiplier lives in the levels NARDL appendix and is computed differently (see Chapter 5).

## 4.5 The asymmetry test (the second-most-important number)

The dissertation tests \(H_0: \text{CPT}^{+} = \text{CPT}^{-}\) by a Wald restriction. The test statistic, under the HAC covariance \(\hat V\), is the standard

$$F = \frac{(R \hat\beta - r)' [R \hat V R']^{-1} (R \hat\beta - r)}{q_R}$$

with \(R\) selecting the difference \(\sum \beta_j^{+} - \sum \beta_j^{-}\) and \(r = 0\). A small \(p\)-value rejects the null and is evidence of asymmetry. In the dissertation, only the retail-petrol layer comes near significance (\(p = 0.0999\)) — and even that is marginal at 10%.

You also report a **restricted-residual circular block bootstrap** with \(B = 4{,}999\) replications. The procedure is:

1. Estimate the model under the null \(\text{CPT}^{+} = \text{CPT}^{-}\) (i.e. impose symmetry) and recover residuals.
2. Resample the residuals in *circular blocks* (so within-block autocorrelation is preserved and the wrap-around handles the end of the series).
3. Generate a bootstrap dependent series, re-estimate the unrestricted model, and recompute the Wald \(F\).
4. The bootstrap p-value is the share of the 4,999 bootstrapped \(F\)-statistics that exceed the observed one.

The bootstrap p-values you report — 0.746 (headline WPI), 0.820 (Fuel & Power), 0.500 (headline CPI) — are larger (more conservative) than the asymptotic HAC p-values, and they confirm that there is no short-run asymmetry to defend.

## 4.6 Lag selection: AIC, BIC, HQC

When you have to choose \(p\) (own-lag order), you fit competing models on a *common sample* (so the comparison is fair) and pick the one that minimises an information criterion. The three you report are:

$$\text{AIC} = -2\ln\hat L + 2k, \quad \text{BIC} = -2\ln\hat L + k\ln n, \quad \text{HQC} = -2\ln\hat L + 2k\ln\ln n.$$

\(\hat L\) is the maximised log-likelihood, \(k\) is the number of parameters, \(n\) is the sample size. AIC is the most permissive (penalises parameters lightly, picks longer lags); BIC is the most parsimonious for moderate \(n\); HQC sits in between asymptotically. The code in `06_models.R` reports all three and uses AIC by default.

Concretely for the headline-CPI specification (`table_05b_lag_selection.csv`):

| \(p\) | AIC | BIC | HQC |
|---|---|---|---|
| 1 | 440.58 | 531.51\* | 477.21\* |
| 2 | 440.13 | 534.56 | 478.16 |
| **3** | **438.79\*** | 536.71 | 478.23 |
| 4 | 440.67 | 542.09 | 481.51 |

AIC selects \(p = 3\); BIC and HQC select \(p = 1\). The dissertation goes with AIC. An examiner could ask, "why not BIC?". Defensible answer: AIC has lower sample-size-induced bias toward under-specification when residuals exhibit short-lag autocorrelation, which the BG12 test confirms is present in the symmetric M0; under-specifying \(p\) leaves residual autocorrelation that contaminates inference even with HAC.

For the long-horizon WPI ADLs the code does not run an information-criterion search at all — it hard-codes \(p = 12\) to absorb annual seasonality on top of the calendar-month fixed effects. The defence is that twelve own lags is a standard choice on monthly data when you suspect leftover seasonal structure even after FE; the lag-sensitivity robustness check confirms results are stable when \(q\) is varied.

## 4.7 OLS estimation: why is OLS okay here?

OLS is consistent and (under classical assumptions) BLUE. In your specification the regressors include *lagged dependent variables*, which means OLS is not unbiased in finite samples — it is *consistent* as \(T \to \infty\). For \(T \in \{164, 245, 371, 515\}\), the lagged-dependent-variable bias is small and shrinks with the sample. The conditions you actually need are:

1. The differenced regressors are stationary (your unit-root battery confirms this for the first-differenced series).
2. Errors are not contemporaneously correlated with the regressors. Because oil is heavily exogenous from India's perspective (India is a price taker on global crude), the rupee-oil shock is plausibly uncorrelated with month-\(t\) Indian-CPI residual.
3. Errors have finite variance (yes, despite fat tails).

Standard errors require correction (HAC) but the point estimates from OLS are fine. The alternative — GLS or maximum likelihood with an ARMA error structure — would gain efficiency at the cost of imposing more structure on \(\varepsilon_t\); your design opts for the more robust HAC route.

## 4.8 Worked example — reading the headline-WPI ADL output

From `table_04b_headline_main_coefficients.csv` (selected rows, NW-HAC standard errors):

| Variable | Estimate | NW SE | t | p |
|---|---|---|---|---|
| (Intercept) | 0.3285 | 0.1109 | 2.96 | 0.003 |
| dln\_dep\_L1 | 0.3896 | 0.0465 | 8.38 | 0.000 |
| dln\_dep\_L2 | −0.0598 | 0.0512 | −1.17 | 0.243 |
| dln\_oil\_pos\_L0 | 0.00505 | 0.00527 | 0.96 | 0.339 |
| dln\_oil\_pos\_L1 | 0.01878 | 0.00624 | 3.01 | 0.003 |
| dln\_oil\_pos\_L5 | 0.01713 | 0.00522 | 3.28 | 0.001 |
| dln\_oil\_neg\_L0 | 0.01133 | 0.00618 | 1.83 | 0.067 |
| dln\_oil\_neg\_L1 | 0.01907 | 0.00463 | 4.12 | 0.000 |

How to read this in the viva:

- The intercept of 0.328 is in *percentage points per month*; the average headline WPI inflation in the conditioning sample is around 0.5%/month. The intercept is the residual baseline after the calendar-month FE absorb seasonality.
- The persistence coefficient \(\varphi_1 = 0.39\) (highly significant) says that 39% of last month's WPI inflation carries into this month — exactly the level of inertia textbook macro models assume.
- The contemporaneous oil response \(\beta_0^{+} = 0.005\) is *not* significant. Most of the pass-through happens with lag.
- The lag-1 coefficient on positive oil is 0.019 (\(p = 0.003\)) — significant. There is also a lag-5 spike of 0.017. Sum across \(j = 0, ..., 6\): the cumulative \(\text{CPT}^{+} = 0.030\) reported in the summary table.

The HAC-Wald test on \(\sum_{j=0}^6 \beta_j^{+} = 0\) yields \(p = 0.024\) — the cumulative response is significantly different from zero. The HAC-Wald test on \(\sum \beta_j^{+} = \sum \beta_j^{-}\) yields \(F = 0.179\), \(p = 0.673\) — no asymmetry. The bootstrap analogue is \(p = 0.746\), even more conservative.

That is exactly how you should narrate the result if asked to walk through the headline-WPI table at the board.

\clearpage

# Chapter 5 — NARDL, fully explained

## 5.1 Why NARDL is in the appendix and not the main text

NARDL — **Nonlinear ARDL** — is the levels-version of the asymmetric model. Where your main ADL works on differences and reports cumulative *short-run* responses, NARDL works on the levels of the log price indices and reports a *long-run* relationship plus an error-correction speed of adjustment. The two are complementary, not redundant.

Three reasons NARDL is supplementary in your dissertation:

1. NARDL in levels assumes a particular integration structure for the regressors — specifically, that they are I(0) or I(1) but not I(2). That is the **bounds-test** assumption of Pesaran, Shin & Smith (2001). The unit-root battery in your data confirms it, but the assumption is binding. The differenced ADL does not need it.
2. NARDL inference requires the lag selection in levels to be correct — choose too few lags and the residual is autocorrelated, choose too many and you lose power. The `nardl()` package picks lags by AIC up to a maximum of 4, which is reasonable but is one more degree of freedom for an examiner to question.
3. The cumulative-pass-through reading from the differenced ADL maps directly to "how many percentage points of an oil shock end up in the price index over a few months". The long-run NARDL multiplier maps to "what is the steady-state percentage response after the system has fully adjusted, which can take many years given an ECT of −0.019". The first is what policy practitioners ask about; the second is a theoretical object.

So the NARDL battery is reported as long-run *evidence* alongside the ADL, but the headline numbers in the dissertation come from the ADL.

## 5.2 The NARDL specification

The Shin–Yu–Greenwood-Nimmo (2014) NARDL in levels for one regressor is

$$\Delta y_t = \alpha + \rho\, y_{t-1} + \theta^{+}\, x_{t-1}^{+(\text{cum})} + \theta^{-}\, x_{t-1}^{-(\text{cum})} + \sum_{i=1}^{p-1} \pi_i\, \Delta y_{t-i} + \sum_{j=0}^{q} (\phi_j^{+}\, \Delta x_{t-j}^{+} + \phi_j^{-}\, \Delta x_{t-j}^{-}) + \varepsilon_t,$$

where \(x_t^{+(\text{cum})} = \sum_{s=1}^t \max(\Delta x_s, 0)\) and \(x_t^{-(\text{cum})} = \sum_{s=1}^t \min(\Delta x_s, 0)\) are the cumulative positive and negative components of the regressor, starting from the beginning of the sample. The structure is:

- \(\rho\) and the level coefficients \(\theta^{\pm}\) carry the **long-run** information.
- \(\pi_i\) and \(\phi_j^{\pm}\) carry the **short-run** dynamics.
- The **error-correction term** is \(\rho\,(y_{t-1} - \beta^{+} x_{t-1}^{+(\text{cum})} - \beta^{-} x_{t-1}^{-(\text{cum})})\) where \(\beta^{\pm} = -\theta^{\pm} / \rho\). The sign of \(\rho\) (the ECT) must be negative and significant for the model to make sense.
- The **long-run asymmetry** test is \(H_0: \beta^{+} = \beta^{-}\), implemented as a Wald test on the level coefficients.
- The **short-run asymmetry** test is \(H_0: \sum_j \phi_j^{+} = \sum_j \phi_j^{-}\), the differenced analogue.

## 5.3 The Pesaran–Shin–Smith bounds test

You cannot just regress \(y\) on lagged \(y\) and on the cumulative \(x^{\pm}\) terms — if the level series are not cointegrated, the levels coefficients are spurious. The bounds test tells you whether they are cointegrated.

The procedure:

1. Run the NARDL above and compute the joint **F-statistic** on the null \(H_0: \rho = \theta^{+} = \theta^{-} = 0\). A large F means the level terms jointly add information beyond the differenced terms — i.e., there is a long-run relationship.
2. Compare F to two critical values: an **I(0) lower bound** (assumes all regressors are I(0)) and an **I(1) upper bound** (assumes all regressors are I(1)). Pesaran, Shin & Smith (2001) tabulate these.
3. **Decision rule.**
   - F **above the I(1) upper bound** \(\Rightarrow\) reject \(H_0\): there is a long-run relationship. *Inconclusive about the integration order, but the relationship exists.*
   - F **below the I(0) lower bound** \(\Rightarrow\) fail to reject: no long-run relationship.
   - F **between** the two bounds \(\Rightarrow\) inconclusive; the answer depends on the integration structure of the regressors.
4. A complementary **t-bound test** is sometimes reported on \(\rho\) alone. Same logic: if \(t_\rho\) is more negative than the I(1) lower bound, reject the null of no long-run.

Your `table_07_nardl_summary.csv` reports the bounds F-statistics and, separately, the ECT coefficients and their p-values:

| Specification | Sample | N | Bounds F | ECT | ECT p | SR Wald p | LR Wald p |
|---|---|---|---|---|---|---|---|
| WPI ~ Brent | 1997-04 → 2025-03 | 333 | 27.66 | −0.0189 | 0.005 | 0.618 | 0.001 |
| WPI ~ Brent \| EXR | 1997-04 → 2025-03 | 333 | 21.40 | −0.0185 | 0.006 | 0.522 | <0.001 |
| WPI ~ Rupee oil | 1997-04 → 2025-03 | 331 | 21.43 | −0.0170 | 0.011 | 0.760 | 0.023 |
| Fuel & Power ~ Rupee oil | 1997-04 → 2025-03 | 331 | 34.15 | −0.0811 | <0.001 | 0.233 | <0.001 |

**Reading.** The PSS upper-bound critical value at the 1% level for one regressor (case III, unrestricted intercept, no trend) is around 7.84; for two regressors it is around 6.36. All four F-statistics in your table are *vastly* above the 1% upper bound — a long-run relationship is not in question. The ECT coefficients are all negative and significant — formally consistent with cointegration. The long-run Wald symmetry test rejects in three of the four specifications, while the short-run Wald symmetry test does not reject in any. So the levels evidence picks up an asymmetry the differenced ADL does not — but, as the dissertation notes, the conservative read is the differenced ADL one, because it does not depend on the level-series integration assumptions.

\begin{keybox}
\textbf{Watch out — the ECT magnitude.} An ECT of \(-0.019\) means the system corrects only about 1.9\% of any disequilibrium per month. That implies a half-life of roughly \(\ln(0.5) / \ln(1 - 0.019) \approx 36\) months. Three years to absorb half of an oil shock through this channel is slow; the dissertation correctly flags that the ECT is best read as a descriptive number rather than a structural disequilibrium parameter, because at this speed alternative specifications (different lag length, different sample) will move the ECT a lot.
\end{keybox}

## 5.4 There is also a separate ARDL-bounds table on the CPI side

`table_04b_bounds_test.csv` reports:

| Test | k | Case | Obs | F | HAC p |
|---|---|---|---|---|---|
| Pesaran-Shin-Smith ARDL bounds F | 2 | III | 245 | **3.6268** | 0.0138 |

This is the bounds test for the headline-CPI levels relationship. F = 3.63 is *below* the standard PSS upper-bound at 5% for two regressors (around 4.85 at the 5% level for case III). The conclusion is that the headline-CPI levels do not exhibit a clean long-run cointegrating relationship with cumulative oil — which is itself a defensible finding (it is consistent with the dilution result) and which is one further reason the ADL in differences is the more defensible workhorse for that layer.

## 5.5 Worked NARDL example: WPI Fuel & Power on rupee oil

From `table_07_nardl_summary.csv`, row 4: `Fuel & Power ~ Rupee oil` over April 1997 to March 2025, N = 331.

- **Bounds F = 34.15.** Far above the 1% upper bound. Reject the null of no long-run relationship.
- **ECT coefficient = −0.0811** (\(p < 0.001\)). Negative and significant; the model corrects roughly 8% of disequilibrium per month, half-life around 8.2 months.
- **Short-run Wald asymmetry p = 0.233.** Fail to reject short-run symmetry — consistent with the ADL finding for the same series (\(p = 0.783\) under HAC, 0.820 in the bootstrap).
- **Long-run Wald asymmetry p < 0.001.** Reject long-run symmetry. The level effect of cumulative positive oil shocks differs from cumulative negative oil shocks.

How to narrate this in the viva: "The NARDL bounds F is 34.15, above the 1% upper PSS bound, so I conclude there is a stable long-run relationship between the level of the Fuel and Power index and the cumulative positive and negative components of the rupee oil price. The error-correction term is −0.081 with a p-value below 0.001, consistent with cointegration and indicating about an eight-month half-life of disequilibrium adjustment. Short-run asymmetry is not detected, but the levels Wald test rejects long-run symmetry. I read this as supplementary evidence: the main short-run conclusion of symmetric pass-through in the Fuel and Power layer survives in the differenced ADL, but the levels NARDL detects a longer-horizon asymmetry that the differenced specification is not designed to capture."

\clearpage

# Chapter 6 — Every test in the dissertation, decoded

For each test below: what it tests, the null, the alternative, the test statistic, the decision rule, and what passing or failing means *for your dissertation*.

## 6.1 Augmented Dickey–Fuller (ADF)

**What it tests.** Whether a series has a unit root.
**Null \(H_0\).** Series has a unit root (non-stationary).
**Alternative \(H_1\).** Series is stationary (around a constant or trend).
**Statistic.** The t-statistic on \(\rho\) in \(\Delta y_t = \alpha + \rho y_{t-1} + \sum_{i=1}^k \delta_i \Delta y_{t-i} + \varepsilon_t\). Critical values are non-standard (Dickey–Fuller distribution).
**Decision rule.** Reject \(H_0\) if the ADF t-statistic is more negative than the critical value (e.g., −2.88 at the 5% level for a constant-only model).
**Means in your dissertation.** In levels, ADF fails to reject for log-CPI (t = −0.68), log-WPI (t = −1.00), log-EXR (t = −1.88) — all I(1). In first differences, ADF rejects strongly (t around −10 to −15) — all I(0). This justifies the differenced ADL.

## 6.2 Phillips–Perron (PP)

**What it tests.** Same null and alternative as ADF.
**Statistic.** A non-parametric correction to the unit-root test that handles serial correlation and heteroskedasticity in the error process without adding lagged differences.
**Decision rule.** Same as ADF; same critical values.
**Means in your dissertation.** Confirms ADF: levels are I(1), differences are I(0). PP and ADF agreeing is a clean robustness check, since the two correct for residual structure differently.

## 6.3 KPSS (Kwiatkowski–Phillips–Schmidt–Shin)

**What it tests.** Whether a series is stationary — but with the *opposite* null to ADF/PP.
**Null \(H_0\).** Series is stationary (around level or trend).
**Alternative \(H_1\).** Series has a unit root.
**Statistic.** A scaled cumulative sum of partial-sum residuals; large values indicate non-stationarity.
**Decision rule.** Reject \(H_0\) if KPSS exceeds critical value (0.463 at 5% for level-stationarity null).
**Means in your dissertation.** In levels, KPSS rejects for log-CPI (KPSS = 0.94), log-WPI (1.59), log-EXR (1.36) — confirming I(1). In differences, KPSS fails to reject (values 0.04–0.09) — confirming I(0). The convergence of ADF/PP/KPSS is what gives the unit-root conclusion confidence.

## 6.4 Pesaran–Shin–Smith bounds test

**What it tests.** Whether a long-run levels relationship exists between the dependent variable and the regressors in an ARDL/NARDL.
**Null \(H_0\).** No long-run relationship (\(\rho = \theta^{+} = \theta^{-} = 0\)).
**Statistic.** Joint F-statistic on the level coefficients.
**Decision rule.** Compare F to two bounds. Above the I(1) upper bound \(\Rightarrow\) reject. Below the I(0) lower bound \(\Rightarrow\) fail to reject. Between \(\Rightarrow\) inconclusive.
**Means in your dissertation.** The four NARDL specs all have F values 21–34, far above the 1% I(1) upper bound — clean evidence of a long-run relationship. The CPI-side bounds test (F = 3.63) is in the inconclusive-to-failing range, consistent with the dilution story.

## 6.5 Breusch–Godfrey serial-correlation LM test (BG)

**What it tests.** Whether residuals are autocorrelated up to order \(h\).
**Null \(H_0\).** No serial correlation up to lag \(h\).
**Statistic.** \(n R^2\) from auxiliary regression of residuals on regressors and \(h\) lagged residuals; distributed \(\chi^2(h)\) under \(H_0\).
**Decision rule.** Reject if p-value < 0.05.
**Means in your dissertation.** Reported at \(h = 12\) months. M0 (symmetric ADL) for headline CPI **fails** (p = 0.017) — there is leftover autocorrelation. M1 (asymmetric ADL, the recommended headline) **passes** (p = 0.073). All three WPI ADL specs **pass** (p between 0.25 and 0.84). The fact that M1 passes BG is one reason the dissertation prefers it over M0.

## 6.6 Breusch–Pagan / White heteroskedasticity tests

**What it tests.** Whether residual variance depends on regressors.
**Null \(H_0\).** Homoskedasticity (constant variance).
**Statistic.** Breusch–Pagan: \(n R^2\) from regression of squared residuals on regressors. White: includes squares and cross-products.
**Decision rule.** Reject if p-value < 0.05.
**Means in your dissertation.** All CPI specifications fail Breusch–Pagan at 5%. This is *expected* in macro time series — volatility clusters around crises (2008, COVID). The Newey–West HAC correction handles both heteroskedasticity and serial correlation, so a BP rejection is not a model-killer; it is the *reason* HAC standard errors are reported. An examiner who says "your model fails BP" should be answered: "yes, that is why I use Newey–West HAC throughout, which is heteroskedasticity-robust by construction."

## 6.7 ARCH-LM test

**What it tests.** Whether squared residuals are autocorrelated — i.e., whether there is conditional heteroskedasticity (volatility clustering).
**Null.** No ARCH up to lag \(h\).
**Statistic.** \(n R^2\) from regression of squared residuals on \(h\) lagged squared residuals.
**Means in your dissertation.** Reported at h = 4 and h = 12. CPI specs all pass at conventional levels (p > 0.3 in all cases). No major ARCH effects; HAC handles what little is there.

## 6.8 Jarque–Bera normality test (JB)

**What it tests.** Whether residuals are Gaussian.
**Null.** Skewness = 0 and excess kurtosis = 0 (normal).
**Statistic.** \(\frac{n}{6}(S^2 + \tfrac{1}{4}(K-3)^2)\), distributed \(\chi^2(2)\).
**Means in your dissertation.** All specifications **fail** JB (p close to 0). Kurtosis values around 5–6, mild positive skew. Macro residuals are almost never Gaussian because of fat tails from crisis episodes. This is *not* fatal for OLS — the Gauss–Markov theorem does not require normality, and HAC inference is asymptotic. The bootstrap p-values are reported precisely because they do not require normality.

## 6.9 Ramsey RESET test

**What it tests.** Whether the model has functional-form misspecification — i.e., whether powers of fitted values would significantly improve the regression.
**Null.** Linear specification is correct; \(\hat y_t^2, \hat y_t^3\) add nothing.
**Statistic.** F-test on additional fitted-value powers in the auxiliary regression.
**Means in your dissertation.** All CPI ADL specifications and the headline WPI ADL **pass** RESET under HAC. The **WPI Fuel & Power** ADL **fails** RESET (HAC p = 0.0008). This is the most important diagnostic failure in the whole pipeline. The dissertation acknowledges it: the linear specification does not capture all the curvature in the relationship, especially during episodes when administered and market-linked pricing coexisted. **The size of the Fuel-and-Power CPT coefficient should be quoted with this caveat.** An examiner who pushes here should be answered: "I report the CPT-pos = 0.287 with a functional-form caveat; the sign and order of magnitude are stable across robustness checks (sample trims, alternative lag windows, Brent vs rupee-oil shock), so I treat this as a robust qualitative finding even though the exact magnitude is sensitive to specification."

## 6.10 CUSUM / CUSUM-of-squares stability tests

**What it tests.** Whether the regression coefficients are stable over time.
**Null.** Coefficients are constant across the sample.
**Statistic.** Recursive (REC-CUSUM) or OLS-residual (OLS-CUSUM) cumulative sums plotted against critical bands; rejecting means the cumulative sum exits the band.
**Means in your dissertation.** Most specifications **pass**. M2 and M3 (Brent+EXR and interaction CPI specs) fail recursive CUSUM at 5%, which is one reason M1 is preferred as the headline. The WPI specs pass.

## 6.11 Wald test for asymmetry

**What it tests.** Whether the cumulative pass-through to positive and negative oil shocks are equal.
**Null.** \(\sum_{j=0}^q \beta_j^{+} = \sum_{j=0}^q \beta_j^{-}\).
**Statistic.** F or \(\chi^2\) statistic on the linear restriction, computed under HAC.
**Means in your dissertation.** All ADL specifications fail to reject at 5%. Retail petrol is marginal at 10% (p = 0.0999). The bootstrap analogues are even more conservative. The honest reading: short-run asymmetry is not the central finding.

## 6.12 Granger-causality test

**What it tests.** Whether past values of one variable help predict another, beyond what the dependent variable's own past predicts.
**Null.** Past values of \(x\) do not improve forecasts of \(y\) given \(y\)'s own past.
**Statistic.** F-test on the joint significance of lags of \(x\) in a regression of \(y\) on its own lags and lags of \(x\).
**Means in your dissertation.** Reported in `table_10b_granger_causality.csv` and `table_16_granger_causality.csv`:

| Direction | F | p | Verdict |
|---|---|---|---|
| dlnOil → dlnCPI | 2.29 | 0.079 | Reject H0 at 10% |
| dlnCPI → dlnOil (reverse) | 0.62 | 0.603 | Fail to reject |
| dlnBrent → dlnPetrol | 10.71 | 0.000 | Strong reject |
| dlnPetrol → dlnFuel | 2.03 | 0.113 | Fail to reject |

The directional reading: oil Granger-causes CPI (weakly) but not vice versa, oil Granger-causes petrol (strongly), and petrol does *not* Granger-cause CPI Fuel & Light at conventional levels. The dissertation is careful: Granger causality is *predictive precedence*, not structural causality, and is reported only as supporting evidence.

## 6.13 Bai–Perron multiple-break test

**What it tests.** Whether there are one or more *unknown-date* structural breaks in the relationship.
**Null.** No break in coefficients.
**Statistic.** F-statistic for \(L\) breaks vs. \(\ell + 1\) breaks; sequential procedure to date breaks.
**Means in your dissertation.** Reported in `table_04c_bai_perron.csv` (CPI side) and `table_15_bai_perron.csv` (WPI). Where breaks are detected, the institutional pre/post-2010 split is reported as the relevant subsample exercise. Bai–Perron functions here as a sanity check, not as a primary identification.

## 6.14 Zivot–Andrews test

**What it tests.** Whether a series has a unit root, allowing for one *endogenously dated* structural break.
**Null.** Unit root with possible break in mean/trend at some endogenous date.
**Means in your dissertation.** Reported in `table_04_zivot_andrews.csv` and `table_14_zivot_andrews.csv`. Break dates cluster around well-known regime episodes (2008, 2014, 2020). Same role as Bai–Perron — sanity check, not headline result.

## 6.15 Restricted-residual circular block bootstrap

**What it tests.** The same null as the asymptotic Wald test for asymmetry, but without relying on the asymptotic distribution.
**Procedure.** Impose the null; resample residuals in blocks (preserving short-run autocorrelation); bootstrap the test statistic; compute the p-value as the share of bootstrap statistics exceeding the observed.
**Means in your dissertation.** Reported in `table_14_bootstrap_wald.csv` and `table_17_bootstrap_wald.csv`. The bootstrap p-values (0.50, 0.75, 0.82) are larger than the asymptotic ones, which is the conservative reading and confirms the no-asymmetry conclusion.

\clearpage

# Chapter 7 — Walking through the results, layer by layer

This chapter is the one to memorise. Each section gives the estimated equation with real numbers, a coefficient-by-coefficient reading, the cumulative pass-through, the diagnostics, and the place of that layer in the attenuation story.

## 7.1 Headline WPI

**Sample.** May 1983 to March 2026, \(N = 515\) months. Adj \(R^2 = 0.421\).

**Specification.** ADL(12, 6) on log-differenced WPI with rupee-oil split into positive and negative, calendar-month FE, no policy dummies (the long sample makes a deregulation dummy meaningless against pre-1990 levels-administered pricing).

**Selected coefficients** (HAC standard errors):

- Intercept: 0.329 (p = 0.003).
- Persistence: \(\varphi_1 = 0.390\) (p = 0); \(\varphi_2\) through \(\varphi_{12}\) mostly small, only \(\varphi_7 = 0.076\) significant at 10%.
- Positive-oil distributed lags: \(\beta_1^{+} = 0.0188\) (p = 0.003), \(\beta_5^{+} = 0.0171\) (p = 0.001), others insignificant. Sum \(\text{CPT}^{+} = 0.030\).
- Negative-oil distributed lags: \(\beta_0^{-} = 0.0113\) (p = 0.067), \(\beta_1^{-} = 0.0191\) (p = 0). Sum \(\text{CPT}^{-} = 0.037\).

**Headline results.**

| | Estimate | p (HAC) | Bootstrap p |
|---|---|---|---|
| \(\text{CPT}^{+}\) | 0.030 | 0.024 | — |
| \(\text{CPT}^{-}\) | 0.037 | 0.001 | — |
| Asymmetry | F = 0.18 | 0.673 | 0.746 |

**Diagnostics.** BG12 p = 0.838 (pass), BP p = 0.170 (pass), RESET p = 0.353 (pass), CUSUM passes. Clean.

**Economic story.** A 1% positive rupee-oil shock is associated with about a 0.030% cumulative response in headline WPI over the next six months — statistically distinguishable from zero, but quantitatively small. The order of magnitude is consistent with the basket weights: fuel-related sub-indices are a substantial share of WPI, but oil shocks pass through them only partially before the headline aggregate is computed. There is no support for asymmetry here.

## 7.2 WPI Fuel & Power

**Sample.** May 1995 to March 2026, \(N = 371\). Adj \(R^2 = 0.463\).

**Specification.** Same ADL(12, 6) structure, with EXR and lagged EXR added as controls, and `d_reform` and `d_covid` dummies.

**Selected coefficients** (from `table_06b_fuel_power_coefficients.csv`):

- Intercept: 0.357 (p = 0.285).
- \(\varphi_1 = 0.213\) (p = 0); \(\varphi_2 = -0.132\) (p = 0.002); \(\varphi_{12} = 0.072\) (p = 0.074).
- Positive-oil: \(\beta_1^{+} = 0.129\) (p = 0), \(\beta_3^{+} = 0.067\) (p = 0.002), \(\beta_4^{+} = 0.040\) (p = 0.070). Sum \(\text{CPT}^{+} = 0.287\).
- Negative-oil: \(\beta_0^{-} = 0.069\) (p = 0), \(\beta_1^{-} = 0.120\) (p = 0). Sum \(\text{CPT}^{-} = 0.268\).

**Headline results.**

| | Estimate | p (HAC) | Bootstrap p |
|---|---|---|---|
| \(\text{CPT}^{+}\) | 0.287 | <0.001 | — |
| \(\text{CPT}^{-}\) | 0.268 | <0.001 | — |
| Asymmetry | F = 0.076 | 0.783 | 0.820 |

**Diagnostics.** BG12 p = 0.250 (pass), BP p = 0.599 (pass), CUSUM passes, **RESET p = 0.0008 (FAIL)**. The functional-form caveat is real and must be acknowledged.

**Economic story.** A 1% positive rupee-oil shock is associated with about a 0.287% cumulative response in WPI Fuel & Power over six months — roughly an order of magnitude larger than the headline-WPI response. The Fuel & Power group covers mineral oils, electricity, and coal; cross-fuel substitution and direct cost-passthrough explain the magnitude. The RESET failure means the linear specification misses some curvature — consistent with the regime change from administered to market-linked petrol/diesel pricing during the sample. The dissertation's claim is that the *order of magnitude* is robust, not the exact decimal.

## 7.3 PPAC retail petrol

**Sample.** August 2004 to December 2024, \(N = 245\).

**Specification.** ADL(3, 3) on dln(Delhi retail petrol), shock variable Brent (USD), with EXR controls, IIP, deregulation and COVID dummies, calendar-month FE.

**Selected coefficients** (from `table_22b_ppac_retail_fuel_coefficients.csv`):

- \(\varphi_1 = 0.043\) (insignificant), \(\varphi_2 = -0.206\) (p = 0.002).
- Positive-Brent: \(\beta_0^{+} = 0.108\) (p = 0.049), \(\beta_1^{+} = 0.171\) (p = 0.000), \(\beta_3^{+} = 0.109\) (p = 0.032). Sum \(\text{CPT}^{+} = 0.346\).
- Negative-Brent: \(\beta_1^{-} = 0.099\) (p = 0.015). Sum \(\text{CPT}^{-} = 0.191\).

**Headline results.**

| | Estimate | p (HAC) |
|---|---|---|
| \(\text{CPT}^{+}\) | 0.346 | <0.001 |
| \(\text{CPT}^{-}\) | 0.191 | 0.0002 |
| Asymmetry | — | **0.0999** |

**Diagnostics.** Channel-diagnostics gate accepted.

**Economic story.** This is the layer with the largest direct pass-through and the only layer where asymmetry is even marginally suggestive. \(\text{CPT}^{+}\) almost twice \(\text{CPT}^{-}\) (0.346 vs 0.191). The asymmetry p-value of 0.0999 is just outside the 5% threshold and inside the 10% threshold, which is the textbook "rockets-and-feathers" location: oil marketing companies pass on positive shocks more fully or faster than negative ones. The dissertation's restraint is correct — it discusses this as suggestive rather than as a confirmed asymmetry.

## 7.4 CPI Fuel & Light bridge

**Sample.** May 2011 to December 2024, \(N = 164\).

**Specification.** ADL(3, 3) on dln(CPI Fuel & Light), shock variable PPAC retail petrol (split positive/negative), with IIP, dummies, calendar FE.

**Selected coefficients** (from `table_16b_fuel_light_coefficients.csv`):

- \(\varphi_1 = 0.271\) (p = 0.001).
- Positive-petrol: \(\beta_0^{+} = 0.025\) (p = 0.116), \(\beta_1^{+} = 0.019\), \(\beta_3^{+} = 0.015\). Sum \(\text{CPT}^{+} = 0.178\) (p = 0.002 from summary).
- Negative-petrol: \(\beta_0^{-} = -0.022\) (p = 0.019), \(\beta_1^{-} = 0.026\). Sum \(\text{CPT}^{-} = 0.106\) (p = 0.174).

**Headline results.**

| | Estimate | p (HAC) |
|---|---|---|
| \(\text{CPT}^{+}\) | 0.178 | 0.0021 |
| \(\text{CPT}^{-}\) | 0.106 | 0.174 |
| Asymmetry | — | 0.455 |

**Economic story.** The bridge layer confirms that retail petrol movements enter the fuel-sensitive consumer index, at a cumulative magnitude roughly half the retail-petrol coefficient. The negative-shock coefficient is not statistically distinguishable from zero, partly because the post-2011 sample is short (164 months) and the negative-shock count is correspondingly small. The bridge Granger test (petrol → fuel) does not reject at conventional levels (p = 0.113), so the relationship is read as an estimated bridge response rather than as strict predictive precedence.

\begin{keybox}
\textbf{Watch out — the harmonised post-2011 series is short.} The 164-month CPI Fuel \& Light sample is the binding constraint on every conclusion that involves CPI sub-indices, including the negative-shock significance test in this layer. The honest answer when asked: "the harmonised series begins in 2011 because the new MoSPI CPI base is 2012 = 100; I cannot extend backward without splicing across a base-year change that I have not validated for sub-indices, so I treat the layer as a bridge with the noted power limitation."
\end{keybox}

## 7.5 Headline CPI

**Sample.** August 2004 to December 2024, \(N = 245\). Adj \(R^2 = 0.449\).

**Specification.** ADL(3, 3) on dln(CPI). Recommended headline is **M1**: rupee-oil split, AR(3) selected by AIC, oil lags 0–3 set by theory, with IIP, three policy dummies (D\_petrol, D\_diesel, D\_covid), calendar FE.

**Selected coefficients** from M1 (the recommended model):

- Persistence \(\varphi_1\) at the AIC-selected lag, \(\varphi_2\), \(\varphi_3\) — see `table_06_M1_asym_inr.csv`.
- The cumulative \(\text{CPT}^{+}\) over the four lags (0, 1, 2, 3) is 0.0213.
- The cumulative \(\text{CPT}^{-}\) is 0.000598.

**Headline results.**

| | Estimate | p (HAC) | Bootstrap p |
|---|---|---|---|
| \(\text{CPT}^{+}\) | 0.021 | 0.122 | — |
| \(\text{CPT}^{-}\) | 0.001 | 0.938 | — |
| Asymmetry | F = 1.38 | 0.241 | 0.500 |

**Diagnostics.** BG12 p = 0.073 (pass), BP p = 0.013 (fail — but HAC handles this), RESET p = 0.183 (pass), CUSUM passes.

**Economic story.** This is the endpoint where the oil signal becomes weak. The positive cumulative coefficient has the right sign and order of magnitude, but is not statistically distinguishable from zero at conventional levels. The negative coefficient is essentially zero. The dissertation does *not* claim a strong headline-CPI effect, and the formal reading is that headline CPI does not show statistically reliable short-run pass-through from oil over the post-2004 sample.

This is the most policy-relevant negative finding in the dissertation: the index that the inflation-targeting framework is anchored on is precisely the index where the oil signal is most diluted.

## 7.6 The integrated attenuation map

| Layer | N | \(\text{CPT}^{+}\) | p | Ratio to PPAC petrol |
|---|---|---|---|---|
| PPAC retail petrol | 245 | 0.346 | <0.001 | 100% |
| WPI Fuel & Power | 371 | 0.287 | <0.001 | 83% |
| CPI Fuel & Light bridge | 164 | 0.178 | 0.002 | 51% |
| Headline WPI | 515 | 0.030 | 0.024 | 9% |
| Headline CPI | 245 | 0.021 | 0.122 | 6% |

The drop is not gradual; it is concentrated at the transition from the fuel-sensitive layers to the headline aggregates. The attenuation Wald test (`table_23c_attenuation_wald.csv`) formalises this: the joint test "all positive and negative CPT equal across stages" rejects with \(F = 20.5\) (p close to 0); pairwise, retail-petrol \(\text{CPT}^{+}\) versus headline-CPI \(\text{CPT}^{+}\) gap of 0.272 rejects with \(F = 14.35\) (p = 0.0002).

## 7.7 Pre/post-2010 wholesale split

From `table_12_subsample_prepost2010.csv`:

| Model | Subsample | N | \(\text{CPT}^{+}\) | p | \(\text{CPT}^{-}\) | p | Asymmetry p |
|---|---|---|---|---|---|---|---|
| Headline WPI | Pre-2010 | 323 | 0.012 | 0.381 | 0.025 | 0.043 | 0.484 |
| Headline WPI | Post-2010 | 192 | 0.074 | 0.004 | 0.081 | 0.000 | 0.788 |
| Fuel & Power | Pre-2010 | 179 | 0.092 | 0.168 | 0.238 | 0.000 | 0.142 |
| Fuel & Power | Post-2010 | 192 | 0.524 | 0.000 | 0.438 | 0.000 | 0.227 |

**Reading.** Post-2010 pass-through is 6× larger for headline WPI and roughly 6× larger for Fuel & Power. The interpretation in the dissertation is restrained: this is institutional evidence consistent with the move toward more market-linked retail fuel pricing, not a clean causal estimate of deregulation. Other things changed in 2010–2017: the new CPI base in 2011, flexible inflation targeting in 2016, GST in 2017, repeated excise rate adjustments. The honest claim is "consistent with deregulation"; the overclaim would be "caused by deregulation".

\clearpage

## 7.8 Full coefficient tables from the code outputs


The sections above give the coefficients you are most likely to discuss at the board. The landscape tables below preserve the full code output, including controls and seasonal dummies. Use them for line-by-line viva drill: sign, magnitude, HAC t-statistic, p-value, and economic meaning.


\begin{landscape}
\begingroup
\scriptsize
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.12}
\setlength{\LTleft}{0pt}
\setlength{\LTright}{0pt}
\begin{longtable}{>{\RaggedRight\arraybackslash}p{0.18\linewidth}>{\RaggedLeft\arraybackslash}p{0.075\linewidth}>{\RaggedLeft\arraybackslash}p{0.075\linewidth}>{\RaggedLeft\arraybackslash}p{0.06\linewidth}>{\RaggedLeft\arraybackslash}p{0.07\linewidth}>{\RaggedRight\arraybackslash}p{0.43\linewidth}}
\caption{Full coefficient table: Headline WPI ADL}\\
\toprule
Variable & Estimate & NW SE & t & p & Plain-English meaning \\
\midrule
\endfirsthead
\toprule
Variable & Estimate & NW SE & t & p & Plain-English meaning \\
\midrule
\endhead
\texttt{(Intercept)} & 0.3285 & 0.1109 & 2.963 & 0.0032 & Baseline monthly inflation after controls and omitted-month seasonal effects. \\
\texttt{dln\_\allowbreak{}dep\_\allowbreak{}L1} & 0.3896 & 0.0465 & 8.383 & 0 & Lag of the dependent WPI inflation rate; captures persistence in that WPI layer. \\
\texttt{dln\_\allowbreak{}dep\_\allowbreak{}L2} & -0.0598 & 0.0512 & -1.168 & 0.2432 & Lag of the dependent WPI inflation rate; captures persistence in that WPI layer. \\
\texttt{dln\_\allowbreak{}dep\_\allowbreak{}L3} & 0.0646 & 0.0512 & 1.262 & 0.2076 & Lag of the dependent WPI inflation rate; captures persistence in that WPI layer. \\
\texttt{dln\_\allowbreak{}dep\_\allowbreak{}L4} & -0.0634 & 0.046 & -1.378 & 0.1688 & Lag of the dependent WPI inflation rate; captures persistence in that WPI layer. \\
\texttt{dln\_\allowbreak{}dep\_\allowbreak{}L5} & 0.0592 & 0.0502 & 1.18 & 0.2388 & Lag of the dependent WPI inflation rate; captures persistence in that WPI layer. \\
\texttt{dln\_\allowbreak{}dep\_\allowbreak{}L6} & 0.0471 & 0.043 & 1.097 & 0.2733 & Lag of the dependent WPI inflation rate; captures persistence in that WPI layer. \\
\texttt{dln\_\allowbreak{}dep\_\allowbreak{}L7} & 0.0762 & 0.045 & 1.695 & 0.0907 & Lag of the dependent WPI inflation rate; captures persistence in that WPI layer. \\
\texttt{dln\_\allowbreak{}dep\_\allowbreak{}L8} & -0.0327 & 0.0506 & -0.646 & 0.5185 & Lag of the dependent WPI inflation rate; captures persistence in that WPI layer. \\
\texttt{dln\_\allowbreak{}dep\_\allowbreak{}L9} & 0.0214 & 0.0429 & 0.499 & 0.6179 & Lag of the dependent WPI inflation rate; captures persistence in that WPI layer. \\
\texttt{dln\_\allowbreak{}dep\_\allowbreak{}L10} & 0.0439 & 0.0382 & 1.15 & 0.2506 & Lag of the dependent WPI inflation rate; captures persistence in that WPI layer. \\
\texttt{dln\_\allowbreak{}dep\_\allowbreak{}L11} & -0.024 & 0.0442 & -0.543 & 0.5872 & Lag of the dependent WPI inflation rate; captures persistence in that WPI layer. \\
\texttt{dln\_\allowbreak{}dep\_\allowbreak{}L12} & 0.0221 & 0.047 & 0.47 & 0.6383 & Lag of the dependent WPI inflation rate; captures persistence in that WPI layer. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}pos\_\allowbreak{}L0} & 0.005 & 0.0053 & 0.957 & 0.3392 & Positive rupee-oil shock at this lag. CPT+ sums all positive-shock lag coefficients. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}pos\_\allowbreak{}L1} & 0.0188 & 0.0062 & 3.01 & 0.0028 & Positive rupee-oil shock at this lag. CPT+ sums all positive-shock lag coefficients. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}pos\_\allowbreak{}L2} & -0.0062 & 0.0054 & -1.144 & 0.2532 & Positive rupee-oil shock at this lag. CPT+ sums all positive-shock lag coefficients. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}pos\_\allowbreak{}L3} & 0.0027 & 0.005 & 0.551 & 0.5821 & Positive rupee-oil shock at this lag. CPT+ sums all positive-shock lag coefficients. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}pos\_\allowbreak{}L4} & 0.0006 & 0.0055 & 0.101 & 0.9195 & Positive rupee-oil shock at this lag. CPT+ sums all positive-shock lag coefficients. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}pos\_\allowbreak{}L5} & 0.0171 & 0.0052 & 3.279 & 0.0011 & Positive rupee-oil shock at this lag. CPT+ sums all positive-shock lag coefficients. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}pos\_\allowbreak{}L6} & -0.008 & 0.0055 & -1.442 & 0.1499 & Positive rupee-oil shock at this lag. CPT+ sums all positive-shock lag coefficients. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}neg\_\allowbreak{}L0} & 0.0113 & 0.0062 & 1.833 & 0.0674 & Negative rupee-oil shock at this lag. The shock variable is negative, so a positive coefficient means prices fall when oil falls. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}neg\_\allowbreak{}L1} & 0.0191 & 0.0046 & 4.119 & 0 & Negative rupee-oil shock at this lag. The shock variable is negative, so a positive coefficient means prices fall when oil falls. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}neg\_\allowbreak{}L2} & $<0.0001$ & 0.0046 & 0.008 & 0.994 & Negative rupee-oil shock at this lag. The shock variable is negative, so a positive coefficient means prices fall when oil falls. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}neg\_\allowbreak{}L3} & 0.0073 & 0.0061 & 1.192 & 0.2338 & Negative rupee-oil shock at this lag. The shock variable is negative, so a positive coefficient means prices fall when oil falls. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}neg\_\allowbreak{}L4} & -0.002 & 0.0043 & -0.466 & 0.6417 & Negative rupee-oil shock at this lag. The shock variable is negative, so a positive coefficient means prices fall when oil falls. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}neg\_\allowbreak{}L5} & -0.0096 & 0.0045 & -2.12 & 0.0345 & Negative rupee-oil shock at this lag. The shock variable is negative, so a positive coefficient means prices fall when oil falls. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}neg\_\allowbreak{}L6} & 0.0113 & 0.0066 & 1.731 & 0.084 & Negative rupee-oil shock at this lag. The shock variable is negative, so a positive coefficient means prices fall when oil falls. \\
\texttt{month02} & -0.3991 & 0.1177 & -3.391 & 0.0008 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{month03} & 0.1077 & 0.1107 & 0.973 & 0.3309 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{month04} & 0.3712 & 0.1377 & 2.696 & 0.0073 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{month05} & -0.2337 & 0.1212 & -1.928 & 0.0545 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{month06} & 0.2266 & 0.1355 & 1.673 & 0.095 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{month07} & 0.1752 & 0.1415 & 1.238 & 0.2163 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{month08} & -0.1945 & 0.1304 & -1.492 & 0.1364 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{month09} & -0.3373 & 0.1319 & -2.558 & 0.0108 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{month10} & -0.0481 & 0.1174 & -0.41 & 0.6821 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{month11} & -0.4179 & 0.119 & -3.512 & 0.0005 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{month12} & -0.6101 & 0.1218 & -5.011 & 0 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\bottomrule
\end{longtable}
\endgroup
\end{landscape}

\begin{landscape}
\begingroup
\scriptsize
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.12}
\setlength{\LTleft}{0pt}
\setlength{\LTright}{0pt}
\begin{longtable}{>{\RaggedRight\arraybackslash}p{0.18\linewidth}>{\RaggedLeft\arraybackslash}p{0.075\linewidth}>{\RaggedLeft\arraybackslash}p{0.075\linewidth}>{\RaggedLeft\arraybackslash}p{0.06\linewidth}>{\RaggedLeft\arraybackslash}p{0.07\linewidth}>{\RaggedRight\arraybackslash}p{0.43\linewidth}}
\caption{Full coefficient table: WPI Fuel and Power ADL}\\
\toprule
Variable & Estimate & NW SE & t & p & Plain-English meaning \\
\midrule
\endfirsthead
\toprule
Variable & Estimate & NW SE & t & p & Plain-English meaning \\
\midrule
\endhead
\texttt{(Intercept)} & 0.3573 & 0.3337 & 1.071 & 0.285 & Baseline monthly inflation after controls and omitted-month seasonal effects. \\
\texttt{dln\_\allowbreak{}dep\_\allowbreak{}L1} & 0.2132 & 0.0577 & 3.693 & 0.0003 & Lag of the dependent WPI inflation rate; captures persistence in that WPI layer. \\
\texttt{dln\_\allowbreak{}dep\_\allowbreak{}L2} & -0.132 & 0.0423 & -3.119 & 0.002 & Lag of the dependent WPI inflation rate; captures persistence in that WPI layer. \\
\texttt{dln\_\allowbreak{}dep\_\allowbreak{}L3} & -0.0735 & 0.0536 & -1.372 & 0.1709 & Lag of the dependent WPI inflation rate; captures persistence in that WPI layer. \\
\texttt{dln\_\allowbreak{}dep\_\allowbreak{}L4} & -0.0261 & 0.0382 & -0.683 & 0.495 & Lag of the dependent WPI inflation rate; captures persistence in that WPI layer. \\
\texttt{dln\_\allowbreak{}dep\_\allowbreak{}L5} & 0.0082 & 0.0585 & 0.14 & 0.8884 & Lag of the dependent WPI inflation rate; captures persistence in that WPI layer. \\
\texttt{dln\_\allowbreak{}dep\_\allowbreak{}L6} & 0.0794 & 0.0621 & 1.279 & 0.2019 & Lag of the dependent WPI inflation rate; captures persistence in that WPI layer. \\
\texttt{dln\_\allowbreak{}dep\_\allowbreak{}L7} & 0.0396 & 0.0363 & 1.092 & 0.2758 & Lag of the dependent WPI inflation rate; captures persistence in that WPI layer. \\
\texttt{dln\_\allowbreak{}dep\_\allowbreak{}L8} & -0.0079 & 0.0404 & -0.196 & 0.8449 & Lag of the dependent WPI inflation rate; captures persistence in that WPI layer. \\
\texttt{dln\_\allowbreak{}dep\_\allowbreak{}L9} & 0.0377 & 0.0615 & 0.613 & 0.5403 & Lag of the dependent WPI inflation rate; captures persistence in that WPI layer. \\
\texttt{dln\_\allowbreak{}dep\_\allowbreak{}L10} & 0.0394 & 0.0496 & 0.795 & 0.4274 & Lag of the dependent WPI inflation rate; captures persistence in that WPI layer. \\
\texttt{dln\_\allowbreak{}dep\_\allowbreak{}L11} & -0.0222 & 0.0375 & -0.592 & 0.5542 & Lag of the dependent WPI inflation rate; captures persistence in that WPI layer. \\
\texttt{dln\_\allowbreak{}dep\_\allowbreak{}L12} & 0.0724 & 0.0404 & 1.792 & 0.074 & Lag of the dependent WPI inflation rate; captures persistence in that WPI layer. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}pos\_\allowbreak{}L0} & 0.0137 & 0.0216 & 0.632 & 0.5277 & Positive rupee-oil shock at this lag. CPT+ sums all positive-shock lag coefficients. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}pos\_\allowbreak{}L1} & 0.1294 & 0.0258 & 5.016 & 0 & Positive rupee-oil shock at this lag. CPT+ sums all positive-shock lag coefficients. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}pos\_\allowbreak{}L2} & 0.0129 & 0.0247 & 0.523 & 0.601 & Positive rupee-oil shock at this lag. CPT+ sums all positive-shock lag coefficients. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}pos\_\allowbreak{}L3} & 0.0672 & 0.0213 & 3.15 & 0.0018 & Positive rupee-oil shock at this lag. CPT+ sums all positive-shock lag coefficients. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}pos\_\allowbreak{}L4} & 0.0404 & 0.0222 & 1.819 & 0.0699 & Positive rupee-oil shock at this lag. CPT+ sums all positive-shock lag coefficients. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}pos\_\allowbreak{}L5} & 0.0242 & 0.0263 & 0.92 & 0.3584 & Positive rupee-oil shock at this lag. CPT+ sums all positive-shock lag coefficients. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}pos\_\allowbreak{}L6} & -0.0012 & 0.0206 & -0.057 & 0.9543 & Positive rupee-oil shock at this lag. CPT+ sums all positive-shock lag coefficients. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}neg\_\allowbreak{}L0} & 0.0685 & 0.0174 & 3.939 & 0.0001 & Negative rupee-oil shock at this lag. The shock variable is negative, so a positive coefficient means prices fall when oil falls. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}neg\_\allowbreak{}L1} & 0.1201 & 0.0211 & 5.692 & 0 & Negative rupee-oil shock at this lag. The shock variable is negative, so a positive coefficient means prices fall when oil falls. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}neg\_\allowbreak{}L2} & 0.0041 & 0.0248 & 0.165 & 0.8692 & Negative rupee-oil shock at this lag. The shock variable is negative, so a positive coefficient means prices fall when oil falls. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}neg\_\allowbreak{}L3} & 0.0145 & 0.0243 & 0.597 & 0.5512 & Negative rupee-oil shock at this lag. The shock variable is negative, so a positive coefficient means prices fall when oil falls. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}neg\_\allowbreak{}L4} & 0.0278 & 0.0202 & 1.376 & 0.1698 & Negative rupee-oil shock at this lag. The shock variable is negative, so a positive coefficient means prices fall when oil falls. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}neg\_\allowbreak{}L5} & -0.0141 & 0.0171 & -0.824 & 0.4105 & Negative rupee-oil shock at this lag. The shock variable is negative, so a positive coefficient means prices fall when oil falls. \\
\texttt{dln\_\allowbreak{}oil\_\allowbreak{}neg\_\allowbreak{}L6} & 0.0467 & 0.0207 & 2.261 & 0.0244 & Negative rupee-oil shock at this lag. The shock variable is negative, so a positive coefficient means prices fall when oil falls. \\
\texttt{dln\_\allowbreak{}exr} & 0.1082 & 0.051 & 2.12 & 0.0347 & Contemporaneous exchange-rate change; depreciation raises rupee import cost. \\
\texttt{dln\_\allowbreak{}exr\_\allowbreak{}L1} & 0.0091 & 0.0591 & 0.154 & 0.878 & One-month lag of exchange-rate change. \\
\texttt{d\_\allowbreak{}reform} & -0.0237 & 0.1902 & -0.125 & 0.9008 & Fuel-pricing reform or deregulation dummy. \\
\texttt{d\_\allowbreak{}covid} & -0.7501 & 0.7141 & -1.05 & 0.2943 & COVID disruption dummy. \\
\texttt{month02} & -0.3536 & 0.3722 & -0.95 & 0.3428 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{month03} & 0.1748 & 0.4338 & 0.403 & 0.6873 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{month04} & -0.7418 & 0.4989 & -1.487 & 0.138 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{month05} & -0.6272 & 0.4645 & -1.35 & 0.1778 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{month06} & -0.1319 & 0.4079 & -0.323 & 0.7466 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{month07} & $<0.0001$ & 0.4686 & 0 & 1 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{month08} & -1.0879 & 0.376 & -2.894 & 0.0041 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{month09} & 0.2766 & 0.3654 & 0.757 & 0.4496 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{month10} & 0.0448 & 0.3826 & 0.117 & 0.9069 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{month11} & -0.0136 & 0.3725 & -0.036 & 0.9709 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{month12} & -0.3785 & 0.3733 & -1.014 & 0.3113 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\bottomrule
\end{longtable}
\endgroup
\end{landscape}

\begin{landscape}
\begingroup
\scriptsize
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.12}
\setlength{\LTleft}{0pt}
\setlength{\LTright}{0pt}
\begin{longtable}{>{\RaggedRight\arraybackslash}p{0.18\linewidth}>{\RaggedLeft\arraybackslash}p{0.075\linewidth}>{\RaggedLeft\arraybackslash}p{0.075\linewidth}>{\RaggedLeft\arraybackslash}p{0.06\linewidth}>{\RaggedLeft\arraybackslash}p{0.07\linewidth}>{\RaggedRight\arraybackslash}p{0.43\linewidth}}
\caption{Full coefficient table: PPAC Delhi retail petrol ADL}\\
\toprule
Variable & Estimate & NW SE & t & p & Plain-English meaning \\
\midrule
\endfirsthead
\toprule
Variable & Estimate & NW SE & t & p & Plain-English meaning \\
\midrule
\endhead
\texttt{(Intercept)} & -1.6317 & 0.7192 & -2.269 & 0.0243 & Baseline monthly inflation after controls and omitted-month seasonal effects. \\
\texttt{dlnPetrol\_\allowbreak{}L1} & 0.0427 & 0.0545 & 0.784 & 0.4341 & Lag of retail petrol inflation; captures pump-price inertia. \\
\texttt{dlnPetrol\_\allowbreak{}L2} & -0.2065 & 0.0663 & -3.116 & 0.0021 & Lag of retail petrol inflation; captures pump-price inertia. \\
\texttt{dlnPetrol\_\allowbreak{}L3} & -0.0075 & 0.0697 & -0.107 & 0.9146 & Lag of retail petrol inflation; captures pump-price inertia. \\
\texttt{dlnBrent\_\allowbreak{}pos\_\allowbreak{}L0} & 0.1077 & 0.0544 & 1.978 & 0.0492 & Positive Brent shock at this lag. \\
\texttt{dlnBrent\_\allowbreak{}pos\_\allowbreak{}L1} & 0.1715 & 0.0462 & 3.713 & 0.0003 & Positive Brent shock at this lag. \\
\texttt{dlnBrent\_\allowbreak{}pos\_\allowbreak{}L2} & -0.0422 & 0.0469 & -0.898 & 0.37 & Positive Brent shock at this lag. \\
\texttt{dlnBrent\_\allowbreak{}pos\_\allowbreak{}L3} & 0.1089 & 0.0504 & 2.162 & 0.0317 & Positive Brent shock at this lag. \\
\texttt{dlnBrent\_\allowbreak{}neg\_\allowbreak{}L0} & 0.0118 & 0.0377 & 0.315 & 0.7534 & Negative Brent shock at this lag. Positive coefficient means the dependent price falls when Brent falls. \\
\texttt{dlnBrent\_\allowbreak{}neg\_\allowbreak{}L1} & 0.0995 & 0.0405 & 2.454 & 0.0149 & Negative Brent shock at this lag. Positive coefficient means the dependent price falls when Brent falls. \\
\texttt{dlnBrent\_\allowbreak{}neg\_\allowbreak{}L2} & 0.0468 & 0.0402 & 1.165 & 0.2455 & Negative Brent shock at this lag. Positive coefficient means the dependent price falls when Brent falls. \\
\texttt{dlnBrent\_\allowbreak{}neg\_\allowbreak{}L3} & 0.0331 & 0.0306 & 1.084 & 0.2796 & Negative Brent shock at this lag. Positive coefficient means the dependent price falls when Brent falls. \\
\texttt{dlnIIP} & 0.0657 & 0.0422 & 1.557 & 0.1209 & IIP growth; proxy for domestic activity or demand pressure. \\
\texttt{D\_\allowbreak{}petrol} & 0.7727 & 0.4876 & 1.585 & 0.1145 & Fuel-pricing reform or deregulation dummy. \\
\texttt{D\_\allowbreak{}diesel} & -0.6199 & 0.4395 & -1.411 & 0.1598 & Diesel deregulation dummy from October 2014. \\
\texttt{D\_\allowbreak{}covid} & 9.6753 & 3.0424 & 3.18 & 0.0017 & COVID disruption dummy. \\
\texttt{mo\_\allowbreak{}Jan} & 0.727 & 0.735 & 0.989 & 0.3237 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Feb} & 1.3707 & 1.0425 & 1.315 & 0.1899 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Mar} & 0.1725 & 0.6799 & 0.254 & 0.7999 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Apr} & 1.3551 & 1.3843 & 0.979 & 0.3287 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}May} & 0.7566 & 0.8501 & 0.89 & 0.3744 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Jun} & 2.5898 & 1.185 & 2.185 & 0.0299 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Jul} & 1.8955 & 0.9709 & 1.952 & 0.0522 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Aug} & 1.2348 & 1.1267 & 1.096 & 0.2743 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Sep} & 2.283 & 0.8236 & 2.772 & 0.0061 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Oct} & 1.1573 & 0.7989 & 1.449 & 0.1489 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Nov} & 0.8294 & 0.8774 & 0.945 & 0.3456 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\bottomrule
\end{longtable}
\endgroup
\end{landscape}

\begin{landscape}
\begingroup
\scriptsize
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.12}
\setlength{\LTleft}{0pt}
\setlength{\LTright}{0pt}
\begin{longtable}{>{\RaggedRight\arraybackslash}p{0.18\linewidth}>{\RaggedLeft\arraybackslash}p{0.075\linewidth}>{\RaggedLeft\arraybackslash}p{0.075\linewidth}>{\RaggedLeft\arraybackslash}p{0.06\linewidth}>{\RaggedLeft\arraybackslash}p{0.07\linewidth}>{\RaggedRight\arraybackslash}p{0.43\linewidth}}
\caption{Full coefficient table: direct rupee-oil to CPI Fuel and Light}\\
\toprule
Variable & Estimate & NW SE & t & p & Plain-English meaning \\
\midrule
\endfirsthead
\toprule
Variable & Estimate & NW SE & t & p & Plain-English meaning \\
\midrule
\endhead
\texttt{(Intercept)} & 0.4043 & 0.2331 & 1.735 & 0.085 & Baseline monthly inflation after controls and omitted-month seasonal effects. \\
\texttt{dlnFuel\_\allowbreak{}L1} & 0.2714 & 0.08 & 3.393 & 0.0009 & Lag of CPI Fuel and Light inflation; captures persistence. \\
\texttt{dlnFuel\_\allowbreak{}L2} & -0.0233 & 0.0838 & -0.278 & 0.7817 & Lag of CPI Fuel and Light inflation; captures persistence. \\
\texttt{dlnFuel\_\allowbreak{}L3} & 0.0541 & 0.0485 & 1.116 & 0.2663 & Lag of CPI Fuel and Light inflation; captures persistence. \\
\texttt{dlnOil\_\allowbreak{}pos\_\allowbreak{}L0} & 0.0249 & 0.0158 & 1.584 & 0.1156 & Positive rupee-oil shock at this lag. CPT+ sums all positive-shock lag coefficients. \\
\texttt{dlnOil\_\allowbreak{}pos\_\allowbreak{}L1} & 0.0185 & 0.0193 & 0.963 & 0.3375 & Positive rupee-oil shock at this lag. CPT+ sums all positive-shock lag coefficients. \\
\texttt{dlnOil\_\allowbreak{}pos\_\allowbreak{}L2} & 0.0026 & 0.0123 & 0.208 & 0.8354 & Positive rupee-oil shock at this lag. CPT+ sums all positive-shock lag coefficients. \\
\texttt{dlnOil\_\allowbreak{}pos\_\allowbreak{}L3} & 0.0148 & 0.0166 & 0.892 & 0.3741 & Positive rupee-oil shock at this lag. CPT+ sums all positive-shock lag coefficients. \\
\texttt{dlnOil\_\allowbreak{}neg\_\allowbreak{}L0} & -0.0225 & 0.0095 & -2.366 & 0.0194 & Negative rupee-oil shock at this lag. The shock variable is negative, so a positive coefficient means prices fall when oil falls. \\
\texttt{dlnOil\_\allowbreak{}neg\_\allowbreak{}L1} & 0.0262 & 0.022 & 1.192 & 0.2355 & Negative rupee-oil shock at this lag. The shock variable is negative, so a positive coefficient means prices fall when oil falls. \\
\texttt{dlnOil\_\allowbreak{}neg\_\allowbreak{}L2} & 0.0023 & 0.0142 & 0.164 & 0.8703 & Negative rupee-oil shock at this lag. The shock variable is negative, so a positive coefficient means prices fall when oil falls. \\
\texttt{dlnOil\_\allowbreak{}neg\_\allowbreak{}L3} & 0.0048 & 0.0109 & 0.438 & 0.6621 & Negative rupee-oil shock at this lag. The shock variable is negative, so a positive coefficient means prices fall when oil falls. \\
\texttt{dlnIIP} & -0.0083 & 0.0173 & -0.481 & 0.6315 & IIP growth; proxy for domestic activity or demand pressure. \\
\texttt{D\_\allowbreak{}diesel} & -0.2316 & 0.1135 & -2.041 & 0.0432 & Diesel deregulation dummy from October 2014. \\
\texttt{D\_\allowbreak{}covid} & -3.4605 & 1.5919 & -2.174 & 0.0314 & COVID disruption dummy. \\
\texttt{mo\_\allowbreak{}Jan} & -0.2061 & 0.2492 & -0.827 & 0.4096 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Feb} & 0.0414 & 0.369 & 0.112 & 0.9107 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Mar} & -0.3493 & 0.3365 & -1.038 & 0.3011 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Apr} & -0.1892 & 0.5278 & -0.358 & 0.7206 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}May} & 0.0359 & 0.2774 & 0.13 & 0.8972 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Jun} & -0.2051 & 0.2899 & -0.707 & 0.4805 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Jul} & 0.3071 & 0.3634 & 0.845 & 0.3996 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Aug} & -0.3846 & 0.2816 & -1.365 & 0.1743 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Sep} & -0.2424 & 0.4157 & -0.583 & 0.5608 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Oct} & 0.1353 & 0.2772 & 0.488 & 0.6262 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Nov} & 0.1408 & 0.2877 & 0.489 & 0.6253 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\bottomrule
\end{longtable}
\endgroup
\end{landscape}

\begin{landscape}
\begingroup
\scriptsize
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.12}
\setlength{\LTleft}{0pt}
\setlength{\LTright}{0pt}
\begin{longtable}{>{\RaggedRight\arraybackslash}p{0.18\linewidth}>{\RaggedLeft\arraybackslash}p{0.075\linewidth}>{\RaggedLeft\arraybackslash}p{0.075\linewidth}>{\RaggedLeft\arraybackslash}p{0.06\linewidth}>{\RaggedLeft\arraybackslash}p{0.07\linewidth}>{\RaggedRight\arraybackslash}p{0.43\linewidth}}
\caption{Full coefficient table: PPAC petrol to CPI Fuel and Light bridge}\\
\toprule
Variable & Estimate & NW SE & t & p & Plain-English meaning \\
\midrule
\endfirsthead
\toprule
Variable & Estimate & NW SE & t & p & Plain-English meaning \\
\midrule
\endhead
\texttt{(Intercept)} & 0.1872 & 0.0856 & 2.187 & 0.0303 & Baseline monthly inflation after controls and omitted-month seasonal effects. \\
\texttt{dlnFuel\_\allowbreak{}L1} & 0.2741 & 0.07 & 3.914 & 0.0001 & Lag of CPI Fuel and Light inflation; captures persistence. \\
\texttt{dlnFuel\_\allowbreak{}L2} & -0.0403 & 0.0848 & -0.475 & 0.6354 & Lag of CPI Fuel and Light inflation; captures persistence. \\
\texttt{dlnFuel\_\allowbreak{}L3} & 0.056 & 0.0531 & 1.056 & 0.2929 & Lag of CPI Fuel and Light inflation; captures persistence. \\
\texttt{dlnPetrol\_\allowbreak{}pos\_\allowbreak{}L0} & 0.0705 & 0.0316 & 2.232 & 0.0271 & Positive retail-petrol shock at this lag in the CPI Fuel and Light bridge. \\
\texttt{dlnPetrol\_\allowbreak{}pos\_\allowbreak{}L1} & -0.0134 & 0.0154 & -0.874 & 0.3833 & Positive retail-petrol shock at this lag in the CPI Fuel and Light bridge. \\
\texttt{dlnPetrol\_\allowbreak{}pos\_\allowbreak{}L2} & 0.0279 & 0.0214 & 1.305 & 0.1938 & Positive retail-petrol shock at this lag in the CPI Fuel and Light bridge. \\
\texttt{dlnPetrol\_\allowbreak{}pos\_\allowbreak{}L3} & 0.0927 & 0.0284 & 3.266 & 0.0013 & Positive retail-petrol shock at this lag in the CPI Fuel and Light bridge. \\
\texttt{dlnPetrol\_\allowbreak{}neg\_\allowbreak{}L0} & 0.0293 & 0.0322 & 0.911 & 0.3637 & Negative retail-petrol shock at this lag in the CPI Fuel and Light bridge. \\
\texttt{dlnPetrol\_\allowbreak{}neg\_\allowbreak{}L1} & 0.0764 & 0.0436 & 1.753 & 0.0816 & Negative retail-petrol shock at this lag in the CPI Fuel and Light bridge. \\
\texttt{dlnPetrol\_\allowbreak{}neg\_\allowbreak{}L2} & 0.0507 & 0.0427 & 1.188 & 0.2365 & Negative retail-petrol shock at this lag in the CPI Fuel and Light bridge. \\
\texttt{dlnPetrol\_\allowbreak{}neg\_\allowbreak{}L3} & -0.0506 & 0.0198 & -2.561 & 0.0114 & Negative retail-petrol shock at this lag in the CPI Fuel and Light bridge. \\
\bottomrule
\end{longtable}
\endgroup
\end{landscape}

\begin{landscape}
\begingroup
\scriptsize
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.12}
\setlength{\LTleft}{0pt}
\setlength{\LTright}{0pt}
\begin{longtable}{>{\RaggedRight\arraybackslash}p{0.18\linewidth}>{\RaggedLeft\arraybackslash}p{0.075\linewidth}>{\RaggedLeft\arraybackslash}p{0.075\linewidth}>{\RaggedLeft\arraybackslash}p{0.06\linewidth}>{\RaggedLeft\arraybackslash}p{0.07\linewidth}>{\RaggedRight\arraybackslash}p{0.43\linewidth}}
\caption{Full coefficient table: headline CPI M1 asymmetric rupee-oil ADL}\\
\toprule
Variable & Estimate & NW SE & t & p & Plain-English meaning \\
\midrule
\endfirsthead
\toprule
Variable & Estimate & NW SE & t & p & Plain-English meaning \\
\midrule
\endhead
\texttt{(Intercept)} & -0.1223 & 0.2022 & -0.605 & 0.5458 & Baseline monthly inflation after controls and omitted-month seasonal effects. \\
\texttt{dlnCPI\_\allowbreak{}L1} & 0.1652 & 0.0575 & 2.875 & 0.0044 & Lag of headline CPI inflation; captures persistence. \\
\texttt{dlnCPI\_\allowbreak{}L2} & -0.0785 & 0.0688 & -1.142 & 0.2547 & Lag of headline CPI inflation; captures persistence. \\
\texttt{dlnCPI\_\allowbreak{}L3} & -0.1159 & 0.0677 & -1.712 & 0.0884 & Lag of headline CPI inflation; captures persistence. \\
\texttt{dlnOil\_\allowbreak{}pos\_\allowbreak{}L0} & -0.004 & 0.0073 & -0.554 & 0.5802 & Positive rupee-oil shock at this lag. CPT+ sums all positive-shock lag coefficients. \\
\texttt{dlnOil\_\allowbreak{}pos\_\allowbreak{}L1} & 0.0054 & 0.0114 & 0.476 & 0.6349 & Positive rupee-oil shock at this lag. CPT+ sums all positive-shock lag coefficients. \\
\texttt{dlnOil\_\allowbreak{}pos\_\allowbreak{}L2} & 0.0143 & 0.0086 & 1.657 & 0.0989 & Positive rupee-oil shock at this lag. CPT+ sums all positive-shock lag coefficients. \\
\texttt{dlnOil\_\allowbreak{}pos\_\allowbreak{}L3} & 0.0056 & 0.0073 & 0.773 & 0.4406 & Positive rupee-oil shock at this lag. CPT+ sums all positive-shock lag coefficients. \\
\texttt{dlnOil\_\allowbreak{}neg\_\allowbreak{}L0} & 0.0099 & 0.0068 & 1.441 & 0.151 & Negative rupee-oil shock at this lag. The shock variable is negative, so a positive coefficient means prices fall when oil falls. \\
\texttt{dlnOil\_\allowbreak{}neg\_\allowbreak{}L1} & -0.0077 & 0.0084 & -0.914 & 0.3615 & Negative rupee-oil shock at this lag. The shock variable is negative, so a positive coefficient means prices fall when oil falls. \\
\texttt{dlnOil\_\allowbreak{}neg\_\allowbreak{}L2} & -0.0066 & 0.0083 & -0.785 & 0.4334 & Negative rupee-oil shock at this lag. The shock variable is negative, so a positive coefficient means prices fall when oil falls. \\
\texttt{dlnOil\_\allowbreak{}neg\_\allowbreak{}L3} & 0.005 & 0.0061 & 0.818 & 0.4144 & Negative rupee-oil shock at this lag. The shock variable is negative, so a positive coefficient means prices fall when oil falls. \\
\texttt{dlnIIP} & -0.0076 & 0.0052 & -1.452 & 0.1479 & IIP growth; proxy for domestic activity or demand pressure. \\
\texttt{D\_\allowbreak{}petrol} & 0.1163 & 0.1135 & 1.024 & 0.3068 & Fuel-pricing reform or deregulation dummy. \\
\texttt{D\_\allowbreak{}diesel} & -0.3385 & 0.0915 & -3.7 & 0.0003 & Diesel deregulation dummy from October 2014. \\
\texttt{D\_\allowbreak{}covid} & -0.3446 & 0.5182 & -0.665 & 0.5068 & COVID disruption dummy. \\
\texttt{mo\_\allowbreak{}Jan} & 0.6925 & 0.1826 & 3.791 & 0.0002 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Feb} & 0.019 & 0.2732 & 0.07 & 0.9447 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Mar} & 0.5205 & 0.2113 & 2.463 & 0.0145 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Apr} & 0.8528 & 0.2049 & 4.163 & 0 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}May} & 0.6435 & 0.188 & 3.423 & 0.0007 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Jun} & 1.0107 & 0.1748 & 5.781 & 0 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Jul} & 1.8476 & 0.2503 & 7.38 & 0 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Aug} & 0.3612 & 0.2031 & 1.778 & 0.0768 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Sep} & 0.6771 & 0.1902 & 3.56 & 0.0005 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Oct} & 1.2127 & 0.1932 & 6.277 & 0 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\texttt{mo\_\allowbreak{}Nov} & 0.4575 & 0.1753 & 2.61 & 0.0097 & Calendar-month seasonal dummy relative to the omitted reference month. \\
\bottomrule
\end{longtable}
\endgroup
\end{landscape}
\clearpage
# Chapter 8 — Robustness battery and the pre/post-2010 split

The robustness battery in `models/cpi/R/10_robustness.R` and the pre/post-2010 split in `models/wpi/R/03_models.R` are both there to ask the same question: **does the layered attenuation result depend on a particular choice — of shock construction, of sample, of inference, of lag length, of outlier handling?** The answer the dissertation defends is: no, the qualitative ordering survives every check.

## 8.1 The pre/post-2010 split — institutional logic

Petrol was administered until June 2010 — the central government set retail prices for long stretches and absorbed shocks via under-recoveries to oil marketing companies and via subsidy adjustments. After June 2010, oil marketing companies revised pump prices much more frequently. Diesel followed in October 2014. The expectation is that any econometric pass-through model, which detects the pass-through that *actually happens at observed retail prices*, should record larger coefficients in the post-2010 sample — not because the underlying economic transmission changed, but because the retail-price-revision mechanism stopped suppressing it.

What you find:

| Model | Pre-2010 \(\text{CPT}^{+}\) | Post-2010 \(\text{CPT}^{+}\) | Multiple |
|---|---|---|---|
| Headline WPI | 0.012 (n.s.) | 0.074*** | 6× |
| WPI Fuel & Power | 0.092 (n.s.) | 0.524*** | 5.7× |

A factor of 6 is large. The two readings:

1. **Strong reading.** Post-2010 retail price revisions transmit oil shocks roughly six times more strongly than pre-2010 administered pricing did. The deregulation of fuel pricing has materially increased the empirical pass-through visible in upstream price indices.
2. **Restrained reading.** The post-2010 sample also covers the 2011 CPI rebase, the 2016 inflation-targeting framework, the 2017 GST, the 2020 COVID episode, and a sequence of fuel-tax interventions. Any of these could in principle shift the coefficient, and a single break at 2010 cannot identify which one.

The dissertation takes the restrained reading and presents the split as institutional evidence rather than as a clean policy experiment. That is the right defensive posture for the viva.

## 8.2 The Brent + EXR decomposition

Robustness check: replace the rupee-oil shock with separate Brent and EXR shocks, to verify that the headline result is not an artefact of how the shock is constructed.

For headline WPI: \(\text{CPT}^{+} = 0.031\), \(\text{CPT}^{-} = 0.037\), asymmetry p = 0.704. **Essentially identical to the rupee-oil specification.** The conclusion does not depend on collapsing Brent and EXR into a single rupee-oil variable.

## 8.3 Restricted-residual circular block bootstrap

Inference robustness — replace the asymptotic Wald p-values with bootstrapped ones. The bootstrap p-values are larger (more conservative) than the asymptotic ones in every case:

| Model | Asymptotic p | Bootstrap p |
|---|---|---|
| Headline WPI ADL | 0.673 | 0.746 |
| Fuel & Power ADL | 0.783 | 0.820 |
| Headline CPI M1 | 0.241 | 0.500 |
| Headline CPI M2 (Brent+EXR) | 0.144 | 0.568 |

**No specification approaches asymmetry significance under the bootstrap.** That is a strong robustness result.

## 8.4 COVID-window exclusion and winsorisation

Excluding the COVID window (April 2020 – September 2020) from the headline-CPI specification and winsorising the dependent log-difference at the 1% and 99% tails do not overturn the main CPI conclusion. The positive cumulative pass-through stays small and not statistically significant. Reported in `table_18_covid_sensitivity.csv` and `table_19_winsorized.csv`. **Result is not driven by extreme observations.**

## 8.5 Lag-sensitivity

Re-estimate headline WPI and headline CPI under alternative lag windows: oil lags from 0–4 and 0–8, own lags of 6 and 18. Reported in `table_20_lag_sensitivity.csv`. The qualitative ordering of Table 5.1 does not change. CPI cumulative pass-through varies between roughly 0.015 and 0.030 across lag choices but never becomes significant at 5%; WPI Fuel & Power CPT remains in the 0.25–0.32 range.

## 8.6 Rolling-window estimates

`rolling_window_data.csv` reports rolling estimates of the headline-CPI cumulative pass-through over moving windows. The estimate hovers around the central 0.021 value without crossing into significance — no period in the post-2004 sample shows a significant headline-CPI pass-through.

## 8.7 Subsamples on the CPI side

`table_17_subsample.csv` reports the post-2011 subsample, the pre-October-2014 subsample, and the post-October-2014 subsample. \(\text{CPT}^{+}\) is 0.017, 0.017, 0.010 respectively, none significant. The headline-CPI dilution result is stable.

## 8.8 Outlier-sensitive bridge specifications

The CPI Fuel & Light bridge is sensitive to the harmonised sample length (164 months) and to the diesel-deregulation dummy. The bridge ADL \(\text{CPT}^{+}\) changes only modestly when alternative specifications are tried (`table_27_ppac_to_fuel_bridge.csv`), but the negative-shock significance is the brittle one — driven mostly by sample size.

## 8.9 NARDL bounds and long-run asymmetry

The supplementary NARDL battery (Chapter 5 of this guide) gives a long-run asymmetry signal that the differenced ADL does not. The dissertation reads this as supplementary evidence rather than as primary identification because (a) NARDL depends on level-series integration, (b) NARDL lag selection is itself a choice, (c) the differenced ADL is the index-targeted-inflation-relevant horizon. This is the right hierarchy.

## 8.10 What the robustness battery does *not* address

Three things that no amount of in-sample robustness can settle:

1. **Endogeneity through the exchange rate.** EXR responds to oil shocks (terms-of-trade, sentiment) and to domestic inflation. The "rupee oil" shock is therefore not strictly exogenous. The Brent+EXR decomposition partially addresses this but does not eliminate it.
2. **Time-varying coefficients.** The pre/post-2010 split is a single break; the underlying transmission could be smoothly changing. A time-varying-parameter model would be a natural extension and is acknowledged as such in the conclusion.
3. **Indirect channels.** The dissertation captures direct pass-through through the price-index aggregates. Indirect channels (oil → transport → food prices, oil → fertiliser → agricultural prices) are absorbed into the headline-CPI residuals rather than modelled explicitly.

These are honest limits and belong in Chapter 9.

\clearpage

# Chapter 9 — Limitations, honestly

The dissertation acknowledges several limitations explicitly. There are also a handful that the text glosses over but that the code makes visible. This chapter lists both, in the order an examiner is most likely to bring them up.

## 9.1 Limitations the dissertation already states

1. **Reduced-form, not structural.** The ADL and NARDL are reduced-form projections. They estimate the empirical pass-through that actually occurred at observed prices, conditional on whatever institutional, fiscal, and monetary regime prevailed. They do not identify *why* a given pass-through coefficient is what it is.
2. **Pre/post-2010 is institutional evidence, not a deregulation experiment.** The post-2010 period also covers the new CPI series, flexible inflation targeting, GST, and recurring excise adjustments.
3. **CPI Fuel & Light bridge sample is short** (164 months from May 2011). This limits the power of the negative-shock test in that layer.
4. **WPI Fuel & Power fails the HAC RESET test** (p = 0.0008). The exact magnitude of \(\text{CPT}^{+} = 0.287\) for that layer is reported with a functional-form caveat. The sign and order-of-magnitude are stable across robustness checks; the decimal is not.
5. **Headline CPI results are weak/suggestive.** The dissertation never claims a significant headline-CPI pass-through; the formal reading is "not statistically distinguishable from zero in the post-2004 sample."

## 9.2 Limitations the code makes visible but the text understates

1. **Lag-length disagreement between text and code (Table 3.2 vs `06_models.R`).** The text lists CPI/petrol layers as \(p = 6\), \(q = 0\)–4. The code uses AIC-selected \(p = 3\) and theory-set \(q = 3\). Defensive answer: "I report results with \(p\) selected by AIC and \(q\) chosen by theory, consistent with the Indian pass-through literature; the lag-sensitivity check confirms results are stable when \(q\) is varied between 0 and 8."
2. **Component-level WPI splice across base years is less clean than the headline splice.** OEA component definitions for "Fuel & Power" changed across 1993-94 and 2004-05 vintages — coverage of mineral oils and electricity differed. The pre-2010 Fuel-and-Power coefficient carries definitional noise. This is partly why the post-2010 subsample reads cleaner.
3. **Symmetric M0 baseline fails Breusch-Godfrey serial-correlation test** (p = 0.017 at 12 lags). The asymmetric M1 passes (p = 0.073). The text does not flag that the *symmetric* baseline you compare M1 against is itself misspecified by the residual-autocorrelation diagnostic. If asked, concede the point and use it to argue that the asymmetric specification — which corrects the BG failure — is the more defensible workhorse even though its asymmetry test is null.
4. **Endogeneity via the exchange rate.** The rupee-oil shock variable \(\text{Brent}_t \times \text{EXR}_t\) treats EXR as exogenous. EXR responds to oil prices through the terms-of-trade and to inflation through monetary policy. The Brent+EXR decomposition reduces but does not eliminate this concern. No instrumental variable strategy is attempted.
5. **No unit-root test on the bridge series \(\diff\)Petrol → \(\diff\)Fuel & Light.** The chain goes through the retail-petrol layer twice — once as the dependent variable in the petrol model, once as the regressor in the bridge model. The unit-root tests treat them as separate; a more conservative design would test them jointly.
6. **The headline-CPI Granger result (oil → CPI) is significant only at 10%** (\(p = 0.079\)). The text treats this as supporting the directional reading of the chain, which is fine, but a strict reader might say the predictive precedence at the headline-CPI endpoint is itself weak.
7. **The bridge Granger test (petrol → fuel & light) does not reject** (\(p = 0.113\)). The dissertation acknowledges this but still uses the bridge equation. The defensive answer is that Granger non-rejection is consistent with a contemporaneous channel that the lag-based predictive test cannot detect; the bridge equation reports an estimated *contemporaneous-plus-lag* response, which is a different object from Granger predictive precedence.
8. **The "attenuation" claim conflates different shock variables across stages.** The PPAC retail-petrol equation uses Brent as the shock; the WPI and headline-CPI equations use rupee oil; the CPI Fuel & Light bridge uses retail petrol. The Table 5.1 "ratios" (83%, 51%, 9%, 6%) are comparing apples and oranges. The dissertation acknowledges this in the notes to Table 5.1, and the attenuation Wald test in `table_23c_attenuation_wald.csv` is run on a common-sample subset — but in conversation it is easy to overclaim. Be careful to use the phrase "descriptive attenuation map" rather than "structural decomposition of one elasticity".
9. **NARDL ECT magnitudes are descriptively slow** (−0.019 implies a ~3-year half-life). The dissertation correctly flags this; the same flag should be raised in Chapter 5 of the dissertation rather than tucked into Appendix A.
10. **The local folder snapshot is not fully runnable as-is.** The current visible `models/cpi/run_all.R` and `models/wpi/run_all.R` files are thin orchestrators, while many Git-tracked data files, R modules, and output tables are absent from the working tree. This guide was prepared by reading the dissertation and the Git `HEAD` versions of those pipeline files and outputs. If asked to rerun the analysis, restore the tracked pipeline files first.

## 9.3 Where the examiner is most likely to push

In rough order of probability:

1. **"Why ADL and not VECM?"** Defended in Chapter 10 below — short-run inflation dynamics, not long-run cointegrating system; differenced specifications are easier to interpret and do not require the levels integration assumptions.
2. **"Defend your lag length."** AIC at \(p = 3\); \(q = 3\) by theory; lag-sensitivity check varies \(q\) over \([0, 8]\) without overturning the result.
3. **"The exchange rate is endogenous."** Brent+EXR decomposition reduces concern; instrumenting EXR is beyond the dissertation's scope and is a natural extension.
4. **"Post-2010 = deregulation"** is overclaimed.** No, dissertation says "consistent with deregulation"; multiple co-confounding regime changes acknowledged.
5. **"Your Fuel & Power model fails RESET."** Yes; CPT magnitude reported with functional-form caveat; sign and order-of-magnitude robust to alternative specifications, lag windows, sample trims.
6. **"Headline CPI insignificance is a Type-II error from a short sample."** Possible, but lag-sensitivity, COVID exclusion, winsorisation, and rolling windows all show stable null result; Type-II concern is not specific to the central estimate.
7. **"Why monthly and not quarterly?"** Monthly data follows the inflation-targeting cadence and the PPAC reporting frequency; quarterly aggregation would lose retail-pricing information.
8. **"Your ECT in NARDL is suspiciously slow."** Acknowledged; ECT read as descriptive, not structural; differenced ADL is the workhorse.
9. **"You did not test for cointegration on the CPI side."** The bounds test is reported (`table_04b_bounds_test.csv`) and the F = 3.63 result is in the inconclusive-to-failing range — itself consistent with the dilution finding.
10. **"You're chaining the WPI series across base-year changes that altered basket coverage."** True for Fuel & Power components; defended by preferring the longest internally consistent stretch and by reporting splice-check tables.

\clearpage

# Chapter 10 — Anticipated viva questions, with full answers

Each answer is in the first person, the voice you would use at the board. Rehearse them out loud. They are full enough to defend against follow-up; not so verbose that they sound rehearsed.

## Q1. What is your research question, in one sentence?

I ask where, in the chain from international Brent crude to headline Indian inflation, the oil shock weakens — and by how much at each link. The framing is layered transmission and attenuation, not a single elasticity.

## Q2. Why is this an interesting question?

Two reasons. First, India imports roughly 87% of its crude, so oil shocks enter the price system as an external cost shock; if the inflation-targeting framework anchors on headline CPI but oil shocks are diluted before they reach headline CPI, then the policy index sees a heavily filtered version of an important shock. Second, the deregulation of retail fuel pricing in 2010 (petrol) and 2014 (diesel) means the empirical pass-through visible to a model is partly a function of the pricing regime, not just refining and tax structure. Locating where the shock survives versus where it is absorbed is policy-useful.

## Q3. What is a unit root, and why do I care?

A unit root means a series follows a process where shocks are permanent — every push moves the series to a new level forever. Most price levels in the data — log-CPI, log-WPI, log-Brent, log-EXR — are I(1): they have a unit root in levels and are stationary in first differences. I care because regressing two I(1) series on each other in levels gives spurious results: high \(R^2\) and significant slopes even when the truth is no relationship. My main specification therefore works in log-differences, which removes the unit root and makes OLS inference valid.

## Q4. Why ADL and not VAR or VECM?

A VAR treats every series as endogenous and reports impulse responses to orthogonalised shocks. That is the right tool when there are bidirectional dynamics and identification is the central question. My identifying assumption is asymmetric: India is a price-taker on global Brent, so Brent and the rupee oil price can plausibly be treated as exogenous to Indian inflation in a single-equation projection. Given that asymmetry, a VAR is overkill — it spends degrees of freedom modelling the reverse channels (CPI → Brent) that I can defensibly assume away. VECM would be the right tool if my central object were the long-run cointegrating relationship; mine is short-run inflation dynamics, where the differenced ADL is more directly interpretable and does not depend on the level-series integration assumptions. I do report a supplementary NARDL battery in the appendix to provide long-run evidence.

## Q5. Defend your lag length.

For the long WPI specifications I fix \(p = 12\) own lags to absorb annual seasonality on top of the calendar-month fixed effects, and \(q = 0\)–6 oil lags. For headline CPI I select \(p\) by AIC over \(\{1,2,3,4\}\) on a common sample with \(L_4\) — AIC picks \(p = 3\); BIC picks \(p = 1\) and HQC also picks \(p = 1\). I go with AIC because under-specifying \(p\) leaves residual autocorrelation that the symmetric M0 baseline reveals (BG12 p = 0.017 for the AR(1) symmetric model, which then passes BG once the asymmetric specification at AIC's lag is used). I set \(q = 3\) for headline CPI by theory, consistent with the Indian pass-through literature, and confirm in the lag-sensitivity check that varying \(q\) from 0 to 8 does not overturn the qualitative result.

## Q6. Why log differences?

Three reasons. Logs put proportional changes on a common scale across series of different magnitudes; differencing removes the unit root in I(1) series and avoids spurious-regression problems; and the resulting series approximates a percentage change, which is the unit in which inflation is reported and the unit in which my cumulative pass-through coefficient has a clean interpretation.

## Q7. What is the cumulative pass-through and how is it estimated?

It is the sum of distributed-lag coefficients on the positive (or negative) component of the oil shock, summed across the model's lag window: \(\text{CPT}^{+} = \sum_{j=0}^{q} \beta_j^{+}\). I estimate it as a linear restriction on the coefficient vector of the asymmetric ADL and report a HAC-adjusted Wald test of \(H_0: \text{CPT}^{+} = 0\) and \(H_0: \text{CPT}^{+} = \text{CPT}^{-}\). The interpretation is that a 1% positive oil shock is associated with a \(\text{CPT}^{+}\)-percent cumulative response of the dependent log-differenced price index over \(q+1\) months, holding the controls fixed.

## Q8. Walk me through your headline-WPI result.

Sample is May 1983 to March 2026, 515 monthly observations, adjusted \(R^2 = 0.421\). The model is ADL(12, 6) on log-differenced WPI with rupee-oil split into positive and negative components, calendar-month fixed effects, and HAC inference. \(\text{CPT}^{+} = 0.030\) with HAC p = 0.024; \(\text{CPT}^{-} = 0.037\) with p = 0.001. Both cumulative responses are statistically distinguishable from zero. The HAC asymmetry test gives \(F = 0.18\), p = 0.673; the restricted-residual circular-block bootstrap p is 0.746. So a 1% positive oil shock is associated with about a 0.030% cumulative response in headline WPI over six months — small but significant — with no support for asymmetry. Diagnostics are clean: BG12 p = 0.84, BP p = 0.17, RESET p = 0.35, CUSUM passes.

## Q9. Why is the headline-CPI coefficient so much smaller than retail petrol?

Two structural reasons. The basket weight of fuel in the CPI is small; food and non-fuel services dominate household consumption. And the absorption mechanisms — taxes that adjust counter-cyclically, oil marketing margins, and inventory cycles — soak up most of the shock at the upstream layers before it reaches the headline aggregate. The drop is not gradual; it is concentrated at the transition from the fuel-sensitive layers (Fuel & Power, CPI Fuel & Light) to the headline aggregates (WPI, CPI), which is exactly where basket-weight dilution and tax-and-margin absorption are expected to operate.

## Q10. Why do you call the headline-CPI coefficient "weak" rather than "zero"?

The point estimate is positive (0.021) and of roughly the order of magnitude one would expect given the small fuel weight in the CPI basket; it is just not statistically distinguishable from zero in this sample. Calling it "zero" would be overclaiming the negative; calling it "weak/suggestive" is more honest. The lag-sensitivity, COVID exclusion, winsorisation, and rolling-window robustness checks all give similarly small, similarly insignificant estimates, so the honest summary is that I cannot reject the null of no short-run pass-through to headline CPI.

## Q11. Is there asymmetry in the chain?

Not in a way I can defend at the 5% level. The HAC and bootstrap Wald tests on \(\text{CPT}^{+} = \text{CPT}^{-}\) fail to reject in every layer. The retail-petrol layer comes closest, with HAC p = 0.0999 — just outside 5%, just inside 10%. That is the textbook "rockets-and-feathers" location, where oil marketing companies pass on positive shocks more fully than negative ones. I report it as suggestive rather than as a confirmed asymmetry.

## Q12. The Fuel & Power model fails RESET. Doesn't that invalidate the result?

It cautions me against quoting the exact magnitude. The HAC-RESET p-value of 0.0008 indicates the linear specification misses some functional-form curvature, plausibly because the sample spans both administered and market-linked petrol pricing regimes and the relationship is not perfectly linear across them. The sign and order of magnitude of \(\text{CPT}^{+} = 0.287\) are stable across robustness checks — alternative shock variables (Brent vs rupee oil), alternative lag windows, sample trims — so I treat the qualitative finding as robust and the exact decimal as caveatted.

## Q13. The bounds test on the CPI side comes out at F = 3.63. Doesn't that mean the long-run relationship is weak?

Yes — and I think that is informative rather than worrying. The CPI-side bounds F is in the inconclusive-to-failing range relative to the standard PSS critical values for two regressors. That is consistent with my main differenced finding: short-run pass-through to headline CPI is weak, and the levels relationship is correspondingly imprecise. The wholesale-side NARDL specifications, by contrast, have bounds F values of 21–34 — far above the 1% upper bound — and the wholesale-side ADL coefficients are correspondingly significant. The two pieces agree.

## Q14. The pre/post-2010 split shows a 6× jump. Is that deregulation?

It is *consistent* with deregulation, not a clean causal estimate of deregulation. Petrol was deregulated in June 2010 and diesel in October 2014; under market-linked pricing, oil marketing companies revise pump prices much more frequently, mechanically increasing the pass-through visible to a model. But the post-2010 sample also covers the new CPI series in 2011, the move to flexible inflation targeting in 2016, GST in 2017, and a sequence of fuel-tax episodes. Any of these could shift the coefficient. A clean causal estimate would need a continuous time-varying-parameter specification or, ideally, a difference-in-differences design on a non-deregulated comparison good, neither of which is available in this dataset.

## Q15. Why don't you use VECM, given that you find cointegration in the NARDL appendix?

A VECM is a multi-equation system that imposes a long-run cointegrating relationship and models the joint short-run adjustment of all variables back to it. I view the system as essentially recursive — Brent is exogenous to India, EXR responds to global factors and to Indian inflation, and the price layers respond to the rupee oil shock. The VECM machinery would force me to model reverse channels I do not believe in. The NARDL bounds test gives me the long-run information I want without the VECM overhead, and the differenced ADL gives me the short-run inflation dynamics that policy-relevant pass-through requires.

## Q16. What does "Newey–West HAC" do, and why do you need it?

Newey–West constructs a covariance matrix for the OLS coefficient vector that is robust to both heteroskedasticity (residual variance varying with regressors) and to autocorrelation in the residuals up to a chosen bandwidth. The OLS coefficient estimates are unbiased; only the standard errors need correcting. The Breusch–Godfrey test confirms residual autocorrelation at short lags in my specifications, and the Breusch–Pagan test confirms heteroskedasticity. Without HAC, my t-statistics would be too large and I would over-reject the null of zero pass-through. The bandwidth is set data-dependently, the kernel is the Bartlett kernel, and prewhitening is off — all standard choices for monthly macro data.

## Q17. What is the bootstrap doing that the HAC isn't?

The HAC test relies on the asymptotic distribution of the Wald statistic, which is approximate in finite samples and which can mis-size the test if residuals are very fat-tailed. The restricted-residual circular block bootstrap re-estimates the test statistic under the null on resampled residuals, preserving short-run autocorrelation through the block structure, and reads off the p-value as the empirical share of bootstrap statistics exceeding the observed one. It is a finite-sample sanity check on the asymptotic test. In every specification, the bootstrap p-value is larger (more conservative) than the asymptotic one, and they tell the same qualitative story.

## Q18. Why monthly data?

Three reasons. Monetary policy operates on a roughly monthly cadence (CPI is released monthly; the MPC reviews quarterly but tracks monthly). PPAC publishes retail fuel prices monthly. And quarterly aggregation would lose the within-quarter dynamics of retail-pricing revisions, which are part of the transmission mechanism I want to characterise. Weekly data would be ideal for retail petrol but is not consistently available for CPI, so monthly is the only frequency at which the entire chain is observed.

## Q19. How did you handle the WPI splice across base-year revisions?

The OEA publishes WPI under successive base years: 1981-82, 1993-94, 2004-05, and 2011-12. I use the official linking factors from the OEA — for headline WPI, 2.478 (1981-82 → 1993-94), 1.873 (1993-94 → 2004-05), and 1.561 (2004-05 → 2011-12), with 1.690 and 2.802 the analogues for Fuel & Power. The chain is implemented as repeated division through the relevant factor product, so a 1981-82-base value is converted to the 2011-12 base by dividing through the full product. I report a splice-check table at boundary months in `table_03_splice_checks.csv` to verify no visible level breaks. The headline chain is clean. The Fuel-and-Power chain is acknowledged to be less clean at the component level because OEA basket coverage for that group changed slightly across revisions; I prefer the longest internally consistent stretch over a shorter, perfectly homogeneous one.

## Q20. How do you handle endogeneity of the exchange rate?

The rupee-oil shock is constructed as Brent × EXR, and both Brent and EXR could be argued to be endogenous to inflation through reverse channels. Brent is plausibly exogenous from India's perspective — India is a price-taker on global crude. EXR is more ambiguous: it responds to terms-of-trade shocks (which include oil) and to Indian inflation through monetary policy. To assess robustness, I report a Brent + EXR decomposition in which Brent's positive and negative components and EXR's contemporaneous and lagged log-differences enter the headline-WPI specification separately. The cumulative-pass-through coefficient barely changes (\(\text{CPT}^{+}\) goes from 0.030 to 0.031). I do not attempt an instrumental-variable strategy for EXR, and I acknowledge it as a limitation.

## Q21. What controls are in the model and why?

For the headline CPI specification: the activity control is dlnIIP (industrial production), to absorb domestic demand pressure; calendar-month dummies January–November (December omitted as baseline) for seasonality not absorbed by differencing; and three policy-event dummies — D\_petrol from June 2010 (petrol deregulation), D\_diesel from October 2014 (diesel deregulation), D\_covid for April–September 2020. For the WPI specifications, similar controls plus contemporaneous and lag-1 dlnEXR when the shock variable is rupee-oil — to disentangle the exchange-rate component. The controls are not the object of interest; they exist to keep the cumulative pass-through coefficient on oil consistent.

## Q22. Why do you report multiple CPI specifications (M0, M1, M2, M3)?

M0 is a symmetric ADL baseline — the simplest specification, useful as a reference. It fails BG12 (p = 0.017), which means the symmetric model leaves residual autocorrelation; this is precisely the gap the asymmetric specification fills. M1 is the recommended headline — asymmetric ADL with rupee-oil. M2 is the Brent+EXR decomposition robustness check. M3 is an interaction specification with a deregulation dummy. The multiplicity is for robustness; M1 is the model the headline numbers come from.

## Q23. The negative-shock coefficient at the CPI Fuel & Light bridge is insignificant. Why?

Mostly sample size. The bridge sample is 164 months because the harmonised post-2011 CPI Fuel & Light series begins in May 2011. The number of large negative-petrol-shock observations in that window is correspondingly small, so the negative-shock test has limited power. The positive-shock coefficient is 0.178 (p = 0.002) — adequately powered — and that is the bridge result I emphasise.

## Q24. Why is your headline-WPI \(\text{CPT}^{+}\) (0.030) so much smaller than the Fuel & Power \(\text{CPT}^{+}\) (0.287)?

Basket weights and aggregation. The Fuel & Power group covers mineral oils, electricity, and coal — directly oil-linked categories with a tight pass-through. Headline WPI includes manufactured products and primary articles whose oil content is mediated through input cost structure, with much smaller direct fuel weight. The order-of-magnitude gap is exactly what one would expect from the WPI basket structure; my contribution is to quantify it in a single empirical frame.

## Q25. What would change your conclusion?

Three things. First, a longer harmonised CPI sub-index sample, especially for transport, housing and miscellaneous services, would let me test whether the small headline-CPI signal is concentrated in particular components rather than truly absent. Second, a time-varying-parameter or rolling-window specification that lets the cumulative coefficients evolve smoothly with the pricing regime — instead of a single 2010 break — could reveal a non-zero headline-CPI pass-through in particular periods. Third, an instrumental-variable strategy for EXR (using global commodity baskets or U.S. monetary policy shocks as instruments) would let me cleanly separate the exchange-rate from the oil-price contribution to the rupee-oil shock and could revise the headline-CPI estimate in either direction. I view all three as natural extensions; none is feasible inside the data and the scope of this dissertation.

## Q26. Bonus — what is the single most important caveat in this dissertation?

That the layered attenuation map in Table 5.1 is descriptive, not structural. The five cumulative-pass-through coefficients across the chain use *different* shock variables — Brent for retail petrol, rupee-oil for the WPI and headline-CPI specifications, retail petrol for the CPI Fuel & Light bridge — so the ratios in Table 5.1 should not be read as a structural decomposition of one elasticity. They are an attenuation map across naturally ordered points in the price chain, and that is the correct interpretive framing. I want to be careful never to call them an "elasticity decomposition".

\clearpage

# Appendix A — Annotated R code

The following are the most important code chunks. Each is paired with line-by-line commentary in plain English.

## A.1 The WPI splice (`models/wpi/R/02_build_data.R`)

```r
chained_headline <- bind_rows(
  headline_8182 %>%
    filter(date < as.Date("1994-04-01")) %>%
    transmute(date, raw_value, segment = "1981-82 base -> 2011-12",
              chained_2011 = raw_value / prod(CHAIN_FACTORS$headline)),
  headline_9394 %>%
    filter(date >= as.Date("1994-04-01"), date < as.Date("2005-01-01")) %>%
    transmute(date, raw_value, segment = "1993-94 base -> 2011-12",
              chained_2011 = raw_value / (CHAIN_FACTORS$headline["base_9394_to_0405"] *
                                          CHAIN_FACTORS$headline["base_0405_to_1112"])),
  headline_0405 %>%
    filter(date >= as.Date("2005-01-01"), date < as.Date("2012-04-01")) %>%
    transmute(date, raw_value, segment = "2004-05 base -> 2011-12",
              chained_2011 = raw_value / CHAIN_FACTORS$headline["base_0405_to_1112"]),
  headline_1112 %>%
    filter(date >= as.Date("2012-04-01")) %>%
    transmute(date, raw_value, segment = "2011-12 base", chained_2011 = raw_value)
) %>% arrange(date)
```

Line-by-line:

1. `bind_rows(...)` — stack four sub-segments vertically.
2. The first segment uses the 1981-82 base for all months before April 1994. To convert to the 2011-12 base, divide by the *product* of all three chain factors: \(2.478 \times 1.873 \times 1.561 \approx 7.245\). So a published value of 100 on the 1981-82 base becomes \(100 / 7.245 \approx 13.8\) on the 2011-12 base.
3. The second segment uses the 1993-94 base for April 1994 through December 2004. Divide by \(1.873 \times 1.561 \approx 2.924\).
4. The third uses the 2004-05 base for January 2005 through March 2012. Divide by \(1.561\).
5. The fourth uses the 2011-12 base directly from April 2012 onward; no division.
6. `arrange(date)` ensures the resulting series is in calendar order.

The Fuel & Power chain is the same logic with two factors instead of three, beginning in 1994 because the 1981-82 vintage Fuel & Power group is not directly comparable.

## A.2 Building log-differences and asymmetric components

```r
mutate(
  oil_inr = brent_usd * exr,
  ln_dep   = log(dep),
  ln_oil   = log(oil_inr),
  dln_dep  = c(NA, 100 * diff(ln_dep)),
  dln_oil  = c(NA, 100 * diff(ln_oil)),
  dln_oil_pos = pmax(dln_oil, 0),
  dln_oil_neg = pmin(dln_oil, 0),
  d_reform = as.integer(date >= as.Date("2014-10-01")),
  d_covid  = as.integer(date >= as.Date("2020-04-01") &
                        date <= as.Date("2020-09-01"))
)
```

1. `oil_inr = brent_usd * exr` — construct the rupee oil price as Brent (USD/bbl) times INR/USD, in rupees per barrel.
2. `ln_*` — natural logarithms.
3. `dln_*` — month-on-month log differences, multiplied by 100 so the units are percentage points; the leading `NA` is because the first observation has no prior month to difference against.
4. `dln_oil_pos = pmax(dln_oil, 0)` — the positive part. If oil moved up by 5% this month, this is 5; if oil moved down, this is 0.
5. `dln_oil_neg = pmin(dln_oil, 0)` — the negative part with sign preserved. If oil moved down by 3%, this is −3; if oil moved up, this is 0.
6. The two policy dummies are 0/1 indicators on the relevant date windows.

By construction, `dln_oil = dln_oil_pos + dln_oil_neg`, which is what allows the symmetric ADL to be nested inside the asymmetric one (set \(\beta^{+} = \beta^{-}\) and you recover the symmetric model).

## A.3 Lag construction

```r
for (k in 1:MAIN_AR_LAGS) df[[paste0("dln_dep_L", k)]] <- dplyr::lag(df$dln_dep, k)
for (k in 0:MAIN_OIL_LAGS) {
  df[[paste0("dln_oil_pos_L", k)]] <- dplyr::lag(df$dln_oil_pos, k)
  df[[paste0("dln_oil_neg_L", k)]] <- dplyr::lag(df$dln_oil_neg, k)
}
```

Three loops that create the lagged columns used as right-hand-side variables. `MAIN_AR_LAGS = 12` for the WPI specifications; `MAIN_OIL_LAGS = 6`. So you end up with `dln_dep_L1, ..., dln_dep_L12` and `dln_oil_pos_L0, ..., dln_oil_pos_L6` (and the negative analogues). `dplyr::lag(x, k)` shifts the column down by \(k\), inserting `NA` at the top.

## A.4 Fitting the ADL and computing HAC

```r
m_headline_main <- lm(f_headline_main, data = df_headline_main)
nw_headline_main <- NeweyWest(m_headline_main,
                              lag = nw_lag(nrow(df_headline_main)),
                              prewhite = FALSE)
```

1. `lm(f, data)` fits the model by ordinary least squares.
2. `NeweyWest()` from the `sandwich` package returns a heteroskedasticity-and-autocorrelation-consistent variance-covariance matrix for the coefficient vector.
3. `lag = nw_lag(n)` is the project-specific Newey–West bandwidth. In both the CPI and WPI helpers, the code defines it as \(\lfloor 0.75 n^{1/3} \rfloor\).
4. `prewhite = FALSE` means no AR(1) prewhitening of the residuals before computing the long-run variance — the standard, simpler default.

## A.5 Cumulative pass-through and asymmetry test

```r
cpt_headline_main <- compute_cpt(
  m_headline_main,
  paste0("dln_oil_pos_L", 0:MAIN_OIL_LAGS),
  paste0("dln_oil_neg_L", 0:MAIN_OIL_LAGS),
  nw_headline_main,
  "Headline main: "
)
```

`compute_cpt()` is a wrapper in `01_helpers.R` that:

1. Sums the coefficients on the positive-oil lags to form \(\text{CPT}^{+}\).
2. Sums the coefficients on the negative-oil lags to form \(\text{CPT}^{-}\).
3. Tests \(H_0: \text{CPT}^{+} = 0\) and \(H_0: \text{CPT}^{-} = 0\) using `car::linearHypothesis()` with the HAC covariance, returning F-statistics and p-values.
4. Tests \(H_0: \text{CPT}^{+} = \text{CPT}^{-}\) (the asymmetry test) using the same machinery on the difference of sums.
5. Returns a named list of the four objects used downstream.

## A.6 NARDL fit

```r
nardl_headline_inr <- nardl(
  ln_wpi ~ ln_oil_inr,
  data = nardl_headline_data,
  ic = "aic",
  maxlag = NARDL_MAX_LAG,
  graph = FALSE,
  case = 3
)
```

From the `nardl` R package:

1. Fits the Shin–Yu–Greenwood-Nimmo NARDL on the levels of log-WPI and log-rupee-oil.
2. `ic = "aic"` — choose lag length by AIC.
3. `maxlag = 4` — search up to 4 lags.
4. `case = 3` — the PSS bounds-test "Case III" with unrestricted intercept and no trend.
5. `graph = FALSE` suppresses plotting.

The returned object carries the bounds F, the long-run coefficients, the ECT, and the SR/LR Wald asymmetry tests, which are unpacked by `collect_nardl_summary()` and saved to `table_07_nardl_summary.csv` and `table_08_nardl_long_run.csv`.

## A.7 Restricted-residual circular block bootstrap

The bootstrap loop in `08_bootstrap.R` (CPI side) does, in essence:

```r
# 1. Estimate model under H0 (impose CPT+ = CPT-)
m_null <- lm(f_null, data = df)
e_hat <- residuals(m_null)

# 2. Fit unrestricted model and compute observed Wald F
m_un <- lm(f_un, data = df)
F_obs <- linearHypothesis(m_un, "sum_pos = sum_neg",
                          vcov. = vcovHAC(m_un))$F[2]

# 3. Block-bootstrap loop
F_boot <- numeric(B)
for (b in 1:B) {
  # circular block resample of residuals
  e_star <- circular_block_resample(e_hat, block_len)
  # generate bootstrap dependent
  y_star <- fitted(m_null) + e_star
  m_un_star <- lm(update(f_un, y_star ~ .), data = df)
  F_boot[b] <- linearHypothesis(m_un_star, "sum_pos = sum_neg",
                                vcov. = vcovHAC(m_un_star))$F[2]
}

# 4. Bootstrap p-value
p_boot <- mean(F_boot >= F_obs)
```

Why each step matters:

1. *Restricted residuals* — using residuals from the model that imposes the null preserves the null structure on the resampled data, which is what makes the bootstrap correctly sized.
2. *Circular block* — block size preserves short-run autocorrelation; circular wrap-around uses every observation as a block start, avoiding end-of-sample bias.
3. *Refitting under HAC* — each bootstrap replicate is itself HAC-corrected, so the bootstrap is layered on top of HAC, not a substitute for it.
4. *p-value* — the share of bootstrap F-statistics that exceed the observed one.

## A.8 The diagnostics block

```r
bg <- bgtest(m, order = 12)              # Breusch-Godfrey, 12 lags
bp <- bptest(m)                          # Breusch-Pagan
reset <- resettest(m, type = "fitted")   # Ramsey RESET
arch4 <- ArchTest(residuals(m), lags = 4)
arch12 <- ArchTest(residuals(m), lags = 12)
jb <- jarque.bera.test(residuals(m))
cusum_rec <- efp(formula = ..., type = "Rec-CUSUM")
cusum_ols <- efp(formula = ..., type = "OLS-CUSUM")
```

Each line is a one-call test from a standard R package (`lmtest`, `tseries`, `strucchange`). They populate the diagnostics tables row by row.

\clearpage

# Appendix B — Glossary

**ADF (Augmented Dickey–Fuller).** Unit-root test; null is "series has a unit root", reject means stationary.

**ADL (Autoregressive Distributed-Lag).** Single-equation regression with own lags and current/lagged regressors. Workhorse short-run dynamics model.

**Asymmetric ADL.** ADL where the regressor is split into positive and negative components, allowing rockets-and-feathers-style behaviour.

**Attenuation.** The progressive weakening of a shock as it moves through the price chain.

**Bai–Perron test.** Endogenously dated multiple structural break test.

**Bandwidth (HAC).** The number of lagged residual cross-products used in the Newey–West variance estimator. Set data-dependently.

**Bartlett kernel.** The triangular weighting function used in Newey–West to taper the lag covariances to zero at the bandwidth.

**Bounds test (PSS).** Pesaran–Shin–Smith joint F-test in an ARDL/NARDL on the level coefficients; tests for a long-run relationship without requiring all regressors to be I(1).

**Breusch–Godfrey LM test.** Test for residual serial correlation up to lag \(h\). Null: no serial correlation.

**Breusch–Pagan test.** Test for heteroskedasticity in OLS residuals.

**Calendar-month fixed effects.** Eleven dummy variables (one per month, December omitted) absorbing the systematic seasonality in the dependent series.

**Circular block bootstrap.** A block bootstrap variant where blocks are drawn with wrap-around at the sample end, so every observation has equal probability of being a block start.

**Cointegration.** Property that two or more I(1) series share a common stochastic trend, so a linear combination is I(0).

**CPT (Cumulative Pass-Through).** \(\sum_{j=0}^q \beta_j^{\pm}\); the cumulative response of the dependent log-difference to a one-unit log-difference shock summed over the model's lag window.

**CUSUM / CUSUM-of-squares.** Recursive stability test on the regression coefficient vector; rejects if cumulative sum of recursive residuals exits a critical band.

**ECT (Error-Correction Term).** Coefficient \(\rho\) on the lagged level of the dependent variable in an ARDL/NARDL ECM representation; must be negative and significant.

**Fixed effects.** Indicator variables that absorb categorical heterogeneity (here, calendar months).

**Granger causality.** Predictive precedence: \(x\) Granger-causes \(y\) if past \(x\) helps forecast \(y\) beyond \(y\)'s own past.

**HAC (Heteroskedasticity-and-Autocorrelation-Consistent).** Family of variance estimators robust to both heteroskedasticity and autocorrelation. Newey–West is the standard.

**HQC (Hannan–Quinn information criterion).** Lag-selection criterion intermediate between AIC and BIC.

**I(0), I(1), I(2).** Order of integration; how many times you must difference to get a stationary series.

**Information criterion.** Penalised log-likelihood used to compare models; AIC, BIC, HQC are the three reported here.

**Jarque–Bera test.** Test for residual normality based on skewness and kurtosis.

**KPSS test.** Stationarity test with null "stationary"; complementary to ADF/PP.

**Lag operator \(L\).** Convention: \(Ly_t = y_{t-1}\), \(L^2 y_t = y_{t-2}\), etc.

**Long-run multiplier.** Steady-state response in a levels ARDL/NARDL: \(-\theta / \rho\) where \(\theta\) is the level coefficient on the regressor and \(\rho\) is the level coefficient on the lagged dependent.

**M0, M1, M2, M3.** Naming convention for CPI side: M0 = symmetric ADL baseline, M1 = recommended asymmetric headline (rupee oil), M2 = Brent+EXR decomposition robustness, M3 = deregulation interaction.

**NARDL (Nonlinear ARDL).** Asymmetric levels ARDL of Shin–Yu–Greenwood-Nimmo (2014); reports long-run relationship and ECT.

**Newey–West.** Specific HAC estimator with Bartlett kernel and data-dependent bandwidth (Newey–West 1987, 1994).

**OLS (Ordinary Least Squares).** Standard linear regression estimator; consistent and efficient under classical assumptions.

**Phillips–Perron (PP).** Unit-root test, same null as ADF, with a non-parametric correction for residual structure.

**PPAC.** Petroleum Planning and Analysis Cell; publishes monthly retail fuel prices.

**Prewhitening.** Pre-fitting of an AR model to residuals before computing HAC; can improve small-sample performance but adds tuning. Off in your code.

**Ramsey RESET test.** Tests whether powers of fitted values would significantly improve the regression; rejects under functional-form misspecification.

**Restricted-residual bootstrap.** Bootstrap that resamples residuals from the model fit *under the null*, so the resampled data inherit the null's restriction structure.

**Rockets-and-feathers.** Folk term for asymmetric pass-through where positive shocks are passed on faster than negative ones.

**RR-CBB.** Restricted-residual circular block bootstrap (Section 4.5).

**Spurious regression.** Misleading "significant" relationship between two independent unit-root processes regressed in levels.

**Stationarity.** Property that mean, variance, and autocovariance do not depend on calendar date.

**Unit root.** Non-stationarity of the AR(1) form \(y_t = y_{t-1} + \varepsilon_t\); shocks are permanent.

**Wald test.** Test of one or more linear restrictions on the coefficient vector. Used here for CPT-equals-zero and CPT-symmetry restrictions.

**Winsorisation.** Capping the dependent variable at the 1st and 99th percentiles to limit influence of outliers.

**WPI.** Wholesale Price Index, published by Office of the Economic Adviser, MoCI; here chained to 2011-12 = 100.

**Zivot–Andrews test.** Unit-root test allowing for one endogenously dated structural break.

\clearpage
