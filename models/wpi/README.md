# WPI Oil Pass-Through Pipeline

A literature-aligned pipeline that estimates oil-price pass-through into India's Wholesale Price Index (WPI) using official OEA monthly WPI files, World Bank Pink Sheet Brent prices, and the FRED INR/USD series. The active estimation strategy is a short-run asymmetric ADL framework in log differences.

## Running

```bash
Rscript wpi/run_all.R
```

All raw inputs are already under `data/raw/wpi/`. All outputs go to `wpi/outputs/`.

## Data sources

- Office of Economic Adviser monthly WPI files and linking factors:
  - `https://eaindustry.nic.in/download_data_1112.asp`
  - `https://eaindustry.nic.in/download_data_0405.asp`
  - `https://eaindustry.nic.in/download_data_9394.asp`
  - `https://eaindustry.nic.in/download_data_8182.asp`
  - `https://eaindustry.nic.in/linking_factor1112.asp`
  - `https://eaindustry.nic.in/linking_factor0405.asp`
  - `https://eaindustry.nic.in/linking_factor9394.asp`
- World Bank Pink Sheet monthly Brent prices:
  - `https://thedocs.worldbank.org/en/doc/74e8be41ceb20fa0da750cda2f6b9e4e-0050012026/related/CMO-Historical-Data-Monthly.xlsx`
- FRED INR/USD exchange rate:
  - `https://fred.stlouisfed.org/graph/fredgraph.csv?id=EXINUS`

## Chain construction

- Headline WPI: OEA releases chained across four base-year series (1981-82, 1993-94, 2004-05, 2011-12) using official linking factors to a common `2011-12 = 100` basis, running April 1982 – March 2026 (528 observations).
- Fuel & Power WPI: chained across 1993-94, 2004-05, and 2011-12 bases to `2011-12 = 100`, running April 1994 – March 2026 (384 observations).
- After inner-joining with Brent and INR/USD, the ADL estimation samples cover roughly 43 years (headline) and 31 years (fuel).

## Models

### Main short-run ADL (claim-bearing)

- `M1 — Headline INR-oil`: Δln(WPI)\_t regressed on 12 own lags, positive and negative parts of Δln(oil_INR) at lags 0–6, month fixed effects. Newey–West HAC standard errors.
- `M2 — Headline Brent + EXR`: same structure but with positive and negative Δln(Brent) and separate Δln(EXR) terms as a decomposition check.
- `M3 — Fuel & Power`: fuel inflation on asymmetric INR-oil, Δln(EXR) controls, a post-October-2014 diesel-deregulation dummy, an April–September 2020 COVID dummy, and month fixed effects.

Each spec reports cumulative pass-through (CPT+ = Σ positive-shock coefficients, CPT- = Σ negative-shock coefficients), the Wald tests for CPT+ = 0, CPT- = 0, and symmetry CPT+ = CPT-.

### Diagnostics on the short-run ADL models

Breusch–Godfrey(12), Breusch–Pagan, HAC-RESET(2,3), Rec-CUSUM, OLS-CUSUM.

### Robustness: pre- vs post-2010 subsample

Same ADL specifications re-estimated on subsamples split at 2010-04 (onset of Indian petrol deregulation and precursor to the 2013–14 diesel deregulation).

## Literature

- Pradeep (2022), _Journal of Economic Asymmetries_: diesel-reform-driven asymmetric pass-through to disaggregated wholesale and consumer prices.
- Sadath and Acharya (2021), _IJESM_: SVAR on India showing asymmetric macro effects of oil shocks on WPI.

## Interpreting the current outputs

Full sample (1983–2026) headline ADL: CPT+ ≈ 0.030 (p = 0.024), CPT- ≈ 0.037 (p = 0.001), symmetry not rejected (p = 0.67). Subsample split suggests a larger post-2010 pass-through pattern: pre-2010 pass-through is weak and insignificant on the positive side, while post-2010 pass-through is larger (CPT+ ≈ 0.074, CPT- ≈ 0.081, both significant). Fuel-and-power post-2010 pass-through is much larger (CPT+ ≈ 0.52, CPT- ≈ 0.44). This is consistent with the economic expectation that fuel-price reforms and more market-linked pricing strengthen the transmission of global oil shocks into fuel-sensitive wholesale prices, while headline pass-through remains attenuated.

## Outputs

Tables in `wpi/outputs/tables/` cover data spans, chain factors, splice checks, ADL summaries and coefficients for each specification, diagnostics, publication-triage verdicts, bootstrap symmetry checks, Granger causality, unit-root checks, structural-break evidence, and the pre/post-2010 subsample comparison. Figures in `wpi/outputs/figures/` show the chained WPI series, oil decomposition, cumulative pass-through, diagnostics, and subsample comparison.
