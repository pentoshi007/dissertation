# Fixes Applied to Dissertation Models

> Last updated: 9 May 2026

This document lists all model and figure fixes applied since the initial pipeline was established. Use this as a checklist when updating the dissertation chapters and the journal publishing paper.

---

## Fix 1: WPI Fuel & Power RESET Failure Resolved

**Problem**: The pooled Fuel & Power WPI ADL model failed the HAC-RESET functional-form test (p < 0.001), casting doubt on the specification of the dissertation's strongest upstream mechanism block.

**Root cause**: Two sources of misspecification in the pooled model:
1. **Regime mixing** — pre-2010 (administered pricing) and post-2010 (market-linked pricing) pass-through coefficients differ by approximately 5×. A single linear model cannot capture both regimes.
2. **COVID outliers** — April–September 2020 saw extreme oil shocks under de facto re-administered pricing, creating severe nonlinearity that a level-shift dummy alone cannot absorb.

**What was added** (in `models/wpi/R/03_models.R`):

### (a) Regime-dependent model (full sample with interactions)
- Added oil-shock × post-2010 interaction terms to the pooled equation.
- Wald test confirms the regime difference is statistically significant (F = 8.06, p < 0.001).
- Result: Pre-2010 CPT+ = 0.100, Post-2010 CPT+ = 0.458.
- Diagnostic status: HAC-RESET still fails (p = 0.004) — useful for documenting regime heterogeneity but not as the preferred specification.
- **Role in paper**: Report as evidence of structural break in pass-through; not the claim-bearing estimate.

### (b) Post-2010 excluding COVID model (preferred specification)
- Estimates on the deregulated-era sample only (April 2010 onward), with COVID months (April–September 2020) excluded.
- Economic justification: COVID reimposed administered pricing, so those months do not reflect the market-linked mechanism the model aims to estimate.
- **Result**:
  - N = 186 | Adj. R² = 0.678
  - CPT+ = 0.521 (p < 0.001)
  - CPT− = 0.420 (p < 0.001)
  - Asymmetry Wald p = 0.164
- **Diagnostics — all PASS**:
  - BG(12) p = 0.075
  - HAC-RESET p = 0.544 ✅ (was 0.001 in pooled)
  - Rec-CUSUM p = 0.700
  - OLS-CUSUM p = 0.877
- **Role in paper**: Preferred sector mechanism result for WPI Fuel & Power.

### Updated model hierarchy (WPI pipeline)

| Model | Role | HAC-RESET | Verdict |
|-------|------|-----------|---------|
| Headline WPI (INR oil) | Main WPI result | PASS (0.353) | Use as main result |
| Headline WPI (Brent+EXR) | Robustness/decomposition | PASS (0.338) | Use as robustness |
| Fuel & Power (pooled) | Original sector model | FAIL (0.001) | Superseded; report with caveat |
| Fuel & Power (regime) | Regime-dependent | FAIL (0.004) | Report for regime evidence only |
| **Fuel & Power (post-2010 excl. COVID)** | **Preferred sector mechanism** | **PASS (0.544)** | **Use as preferred result** |

### What to update in the dissertation

1. **Results chapter (WPI section)**: Present the post-2010 excl. COVID model as the preferred Fuel & Power specification. The pooled model remains as historical context showing the full-sample result, with an explicit caveat about functional-form misspecification.
2. **Methodology chapter**: Add a paragraph explaining the subsample strategy — regime mixing and COVID distortion as sources of nonlinearity, and why excluding these is economically defensible rather than ad hoc.
3. **Robustness section**: Report the regime-dependent model (with interaction terms) as supplementary evidence that pre/post-2010 pass-through differs significantly (Wald F = 8.06, p < 0.001).
4. **Discussion/Conclusion**: Note that the preferred Fuel & Power model shows strong, symmetric pass-through (CPT+ ≈ 0.52, CPT− ≈ 0.42) in the deregulated era, consistent with market-linked pricing transmitting oil shocks more directly.

### What to update in the journal paper

- The preferred specification for the WPI Fuel & Power layer is now the post-2010 excl. COVID model.
- State that the full-sample pooled model is retained for transparency but superseded for inference.
- Use language like: "The preferred specification restricts the sample to the post-deregulation period (April 2010 onward) and excludes COVID months when de facto administered pricing was reimposed. This model passes all diagnostic tests including the HAC-robust RESET test (p = 0.544)."

---

## Fix 2: CPT− Label Correction in All Figures

**Problem**: Bar charts and axis labels across both pipelines displayed `|CPT−|` (absolute value notation) for the negative cumulative pass-through coefficient. This is incorrect — CPT− is a defined econometric quantity (the sum of negative oil-shock lag coefficients), not an absolute value.

**What was changed**:

| File | Figures affected |
|------|-----------------|
| `models/wpi/R/05_figures.R` | Fig 4 (CPT bars), Fig 5 (subsample comparison), Fig 9 (asymmetry gap) |
| `models/cpi/R/11_figures.R` | Fig 4 (CPT bars), Fig 10 (asymmetry gap), Fig 13 (dilution chain), Fig 13b (common-sample dilution) |
| `models/cpi/R/09_mechanism_chain.R` | Console interpretation text |

**Before**: Legend shows `|CPT−|`, axis label shows `CPT+ − |CPT−|`
**After**: Legend shows `CPT−`, axis label shows `CPT+ − CPT−`

All 26 figures (12 WPI + 14 CPI) were regenerated. No model results changed — this was a display-only fix.

### What to update in the dissertation

- Replace any reference to `|CPT−|` with `CPT−` in the text.
- If the dissertation refers to "the absolute value of the negative pass-through coefficient", simplify to "the negative cumulative pass-through coefficient (CPT−)".

### What to update in the journal paper

- Same label correction in any tables or figure captions that use `|CPT−|`.

---

## Current Diagnostic Status — Complete Summary

### WPI Pipeline (all models)

| Model | N | BG(12) | HAC-RESET | Rec-CUSUM | OLS-CUSUM | Status |
|-------|---|--------|-----------|-----------|-----------|--------|
| Headline WPI (INR oil) | 515 | ✅ 0.838 | ✅ 0.353 | ✅ 0.395 | ✅ 0.057 | Main result |
| Headline WPI (Brent+EXR) | 515 | ✅ 0.451 | ✅ 0.338 | ✅ 0.310 | ✅ 0.086 | Robustness |
| Fuel & Power (pooled) | 371 | ✅ 0.250 | ❌ 0.001 | ✅ 0.863 | ✅ 0.977 | Superseded |
| Fuel & Power (regime) | 371 | ✅ 0.449 | ❌ 0.004 | ✅ 0.637 | ✅ 0.994 | Regime evidence |
| Fuel & Power (post-2010 excl. COVID) | 186 | ✅ 0.075 | ✅ 0.544 | ✅ 0.700 | ✅ 0.877 | **Preferred** |

### CPI Pipeline (all models)

| Model | N | BG(12) | HAC-RESET | Rec-CUSUM | OLS-CUSUM | Status |
|-------|---|--------|-----------|-----------|-----------|--------|
| M0: Symmetric ADL | 247 | ❌ 0.017 | ✅ 0.420 | ✅ 0.064 | ✅ 0.589 | Baseline only |
| M1: Asym INR (headline) | 245 | ✅ 0.073 | ✅ 0.183 | ✅ 0.091 | ✅ 0.388 | **Headline** |
| M2: Brent+EXR | 245 | ✅ 0.156 | ❌ 0.013 | ❌ 0.034 | ✅ 0.406 | Robustness only |
| M3: Interaction | 245 | ✅ 0.132 | ❌ <0.001 | ❌ 0.043 | ✅ 0.583 | Appendix only |

### CPI Mechanism Chain

| Stage | CPT+ | p-value | CPT− | Asym p | N |
|-------|------|---------|------|--------|---|
| S1: Brent → PPAC Petrol | 0.346 | <0.001 | 0.191 | 0.100 | 245 |
| S2: PPAC → Fuel & Light CPI | 0.178 | 0.002 | 0.106 | 0.456 | 164 |
| S3: Oil → Headline CPI (M1) | 0.021 | 0.122 | 0.001 | 0.241 | 245 |

### Attenuation Wald Test

| Hypothesis | F | p | Verdict |
|-----------|---|---|---------|
| CPT+ Stage 1 = CPT+ Stage 3 | 14.35 | <0.001 | Attenuation confirmed |
| CPT− Stage 1 = CPT− Stage 3 | 4.34 | 0.038 | Reject equality |
| Joint | 20.48 | <0.001 | Stages differ |

---

## Known Remaining Issues (Not Fixed — By Design)

These are documented limitations, not model bugs. They should be discussed transparently in the paper rather than "fixed" through specification changes.

### 1. Headline CPI (M1) CPT+ is statistically insignificant (p = 0.122)

- This is the expected finding, not an error. Oil pass-through to India's food-heavy CPI (46% food weight) is genuinely small.
- The attenuation Wald test (F = 14.35, p < 0.001) formally confirms that pass-through attenuates from retail fuel to headline CPI.
- **Recommended framing**: "Oil shocks reach headline CPI but at a diluted, statistically insignificant level, consistent with the dilution hypothesis."

### 2. CPI Fuel & Light bridge — short sample and Granger failure

- The harmonised CPI Fuel & Light series begins only in 2011 (N = 164).
- Granger causality from dlnPetrol → dlnFuel fails to reject at 5% (p = 0.113).
- However, the ADL model's CPT+ is significant (p = 0.002).
- **Recommended framing**: "Supportive bridge evidence rather than a fully claim-bearing causal stage."

### 3. Shock variable differs across layers

- Stage 1 uses Brent USD, Stage 3 uses INR oil. The common-sample attenuation test partially addresses this.
- **Recommended framing**: Acknowledge as a limitation of the layered approach; note that the common-sample Wald test uses a standardised framework.

### 4. M2 and M3 diagnostic failures (CPI)

- M2 (Brent+EXR) fails both HAC-RESET and Rec-CUSUM; M3 (Interaction) also fails both.
- These models are already correctly assigned as robustness-only (M2) and appendix-only (M3).
- No fix needed — the publication triage already handles this.

---

## Output Files Reference

### WPI pipeline outputs (key tables)

| File | Contents |
|------|----------|
| `table_06_fuel_power_model.csv` | Pooled Fuel & Power model (original, RESET-FAIL) |
| `table_07_fuel_power_regime_model.csv` | Regime-dependent model (with interactions) |
| `table_07b_fuel_power_regime_coefficients.csv` | Regime model full coefficient table |
| `table_08_fuel_power_post2010_model.csv` | **Preferred** post-2010 excl. COVID model |
| `table_08b_fuel_power_post2010_coefficients.csv` | Preferred model full coefficient table |
| `table_09_diagnostics.csv` | All model diagnostics |
| `table_10_publication_decision.csv` | Publication verdict for each model |
| `table_11_model_gate.csv` | Pass/fail gate summary |

### CPI pipeline outputs (key tables)

| File | Contents |
|------|----------|
| `table_09_diagnostics_all.csv` | All model diagnostics (M0–M3) |
| `table_23_dilution_hypothesis.csv` | Three-stage dilution chain |
| `table_23b_dilution_common_sample.csv` | Common-sample dilution comparison |
| `table_23c_attenuation_wald.csv` | Formal attenuation Wald test |
| `table_24_publication_decision.csv` | Full publication triage |
| `table_26_channel_diagnostics.csv` | Mechanism channel diagnostics |
| `table_28_mandatory_model_gate.csv` | Mandatory model gate (M1 + PPAC) |
