# Dissertation Blueprint

## Working title

State-dependent oil-price pass-through to India's wholesale fuel inflation, 1994-2026

Subtitle: Evidence from monthly local projections

## Core argument

The dissertation should argue that rupee-denominated Brent shocks transmit strongly to India's WPI Fuel and Power index, and that the response is larger after the 2010 fuel-pricing reform period. The claim is deliberately narrower than the older WPI/CPI layered paper. This study does not need headline CPI to be strong. It focuses on the fuel-sensitive wholesale layer where the data span is long and the economics is direct.

Correct claim:

> Rupee oil shocks have a positive and statistically significant cumulative association with WPI Fuel and Power inflation, and the response is stronger in the post-2010 fuel-pricing reform period.

Avoid this claim:

> Oil shocks mechanically determine all Indian inflation.

## Formatting rules for the dissertation docx builder

Use the same basic Word style as the current dissertation builder:

- Paper: A4.
- Font: Times New Roman throughout.
- Body text: 12 pt, justified, 1.5 line spacing.
- Margins: top 1 inch, bottom 1 inch, left 3.54 cm, right 1 inch.
- Heading 1: 20 pt, bold, centred.
- Heading 2: 14 pt, bold, left aligned.
- Heading 3: 12 pt, bold.
- Captions: 10 pt, Times New Roman, italic for figure captions.
- References: APA 7 author-year style.
- Tone: plain MS Economics prose. Use cautious language. Do not overclaim causality.

## Word budget

Target 6,500 to 7,000 words for the main dissertation.

| Part | Target words | Purpose |
| --- | ---: | --- |
| Abstract | 200 | State question, data, method, and main result. |
| Chapter 1: Introduction | 850 | Motivate India's oil exposure and the wholesale fuel layer. |
| Chapter 2: Background and literature | 950 | Cover fuel pricing, WPI vs CPI, and oil-shock literature. |
| Chapter 3: Data and variables | 900 | Explain WPI chaining, Brent, exchange rate, and rupee oil shock. |
| Chapter 4: Methodology | 950 | Explain local projections, state dependence, HAC inference, and diagnostics. |
| Chapter 5: Results | 1,800 | Present all-sample LP, post-2010 state dependence, and robustness. |
| Chapter 6: Robustness and limitations | 750 | Discuss post-2014, high-volatility, asymmetry, and limits. |
| Conclusion | 550 | Answer the research question and state policy relevance carefully. |

## Chapter plan

### Abstract

Use one paragraph. Mention India, rupee oil prices, WPI Fuel and Power, 1994-2026 monthly data, local projections, Newey-West HAC inference, and the post-2010 state-dependent result.

Suggested result wording:

> The all-sample six-month cumulative response is 0.2963 and statistically significant at the 1 per cent level. The post-2010 interaction adds 0.1972 at the six-month horizon, with p = 0.0220.

### Chapter 1: Introduction

Open with India's exposure to dollar-priced imported crude oil. Explain why WPI Fuel and Power is the right fallback layer: it is closer to fuel costs, has a long official monthly sample, and avoids the short CPI component history. State the research question and contribution.

Place no heavy table in Chapter 1. If needed, use Figure 1.1 as a simple conceptual chain:

```text
Brent USD + INR/USD -> rupee oil shock -> WPI Fuel and Power inflation
```

### Chapter 2: Background and literature

Cover:

- India's administered and market-linked fuel-pricing background.
- Petrol deregulation around 2010 and diesel deregulation around 2014.
- Why WPI Fuel and Power should respond more directly than headline CPI.
- Kilian (2009): oil shocks are not all alike.
- Jorda (2005): local projections estimate impulse responses without relying on a full VAR.
- Mandal et al. (2012), Bhanumurthy et al. (2012), Sarmah and Bal (2021), and Deheri and Ramachandran (2023): India oil-shock evidence.

Keep the literature review focused. Do not list papers that are not used in the argument.

### Chapter 3: Data and variables

Use Table 3.1 from `new-model/outputs/tables/table_01_data_spans.csv`.

Explain:

- OEA WPI Fuel and Power chaining.
- World Bank Pink Sheet Brent series.
- INR/USD exchange rate.
- Rupee oil price: `oil_INR = Brent_USD * INR_per_USD`.
- Monthly log differences.
- Main estimation sample: May 1995 to March 2026 after twelve monthly dynamic controls.

Place:

- Figure 3.1: `new-model/outputs/figures/fig_01_wpi_fuel_chained.png`.
- Figure 3.2: `new-model/outputs/figures/fig_02_rupee_oil_shock.png`.
- Table 3.2: `new-model/outputs/tables/table_03_descriptive_stats.csv`.
- Table 3.3: `new-model/outputs/tables/table_04_unit_root_battery.csv`.

### Chapter 4: Methodology

Explain local projections in plain language: estimate a separate regression for each horizon instead of forcing one dynamic system to generate all responses.

Main equation:

```text
100 * [ln(WPI_Fuel_{t+h}) - ln(WPI_Fuel_{t-1})]
  = alpha_h + beta_h * Delta oil_INR_t
  + lag controls + month fixed effects + error_{t+h}
```

State-dependent equation:

```text
... + beta_h * Delta oil_INR_t
    + theta_h * Delta oil_INR_t * Post2010_t
```

Inference:

- Newey-West HAC standard errors for all horizons.
- Six lags of WPI fuel inflation, rupee oil shocks, and exchange-rate changes.
- COVID dummy for April 2020 to September 2020.
- Month fixed effects.

### Chapter 5: Results

Main result order:

1. All-sample LP response from `table_05_lp_all_sample.csv` and `fig_03_lp_all_sample.png`.
2. Post-2010 state-dependent response from `table_06_lp_post2010.csv` and `fig_04_lp_state_comparison_post2010.png`.
3. Diagnostic motivation from `table_10_diagnostics.csv`.

Use exact result language:

> The all-sample response is positive at every horizon. At six months, a 1 per cent rupee oil shock is associated with a 0.2963 per cent cumulative response in WPI Fuel and Power. At twelve months, the estimate is 0.3461.

For state dependence:

> The post-2010 interaction is positive and significant through most horizons. At six months, the additional post-2010 response is 0.1972, with p = 0.0220.

### Chapter 6: Robustness and limitations

Use:

- `table_07_lp_post2014.csv` and `fig_05_lp_state_comparison_post2014.png`.
- `table_08_lp_high_volatility.csv` and `fig_06_lp_high_volatility.png`.
- `table_09_asymmetry_secondary.csv`.
- `table_11_publication_triage.csv` and `table_12_model_gate.csv`.

Wording for post-2014:

> The post-2014 interaction is positive at the six-month horizon but not statistically significant at conventional levels. It is therefore reported as robustness without being used as a headline claim.

Wording for diagnostics:

> The simple all-sample horizon-0 equation is rejected by the HAC RESET benchmark. The post-2010 state-dependent specification passes the functional-form and stability checks. Serial correlation is handled through HAC inference, with a GLS AR(1) residual robustness check reported separately.

### Conclusion

Answer directly:

> Rupee oil shocks transmit clearly to India's wholesale fuel inflation. The evidence is strongest in the WPI Fuel and Power layer and is stronger after the 2010 fuel-pricing reform period.

End with a cautious policy implication: fuel-price reforms make wholesale fuel prices more responsive to global oil and exchange-rate shocks, so inflation management should track the rupee oil price, not Brent alone.
