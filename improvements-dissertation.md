# Improvements for `build_aniket_dissertation.py`

This checklist records the corrections needed after the model fixes in `fixes-applied.md`. The dissertation text is generated through `build_aniket_dissertation.py`, with the chapter prose stored in `_diss_chapters.py`.

## Applied changes

- Use the preferred WPI Fuel and Power model as the claim-bearing wholesale fuel result:
  - Sample: April 2010 to March 2026, excluding April to September 2020.
  - N = 186, adjusted R-squared = 0.678.
  - CPT+ = 0.5205, p < 0.001.
  - CPT- = 0.4195, p < 0.001.
  - Asymmetry p = 0.1642.
  - Mandatory diagnostics pass: BG p = 0.0746, HAC-RESET p = 0.5443, Rec-CUSUM p = 0.6999.

- Keep the old full-sample pooled WPI Fuel and Power model only as context:
  - CPT+ = 0.2866 and CPT- = 0.2677 remain useful for transparency.
  - It fails HAC-RESET, so it should not carry the main inference.
  - The failure is framed as regime mixing plus COVID pricing distortion, not as evidence against oil transmission.

- Add the economic reason for the post-2010 excluding-COVID sample:
  - Pre-2010 and post-2010 pass-through differ strongly.
  - April to September 2020 reflects unusual administered-pricing conditions during COVID.
  - Excluding those months is an economic specification choice, not a cosmetic result selection.

- Update the dissertation result ordering:
  - Preferred WPI Fuel and Power: 0.5205.
  - PPAC retail petrol: 0.3459.
  - CPI Fuel and Light bridge: 0.1777.
  - Headline WPI: 0.0301.
  - Headline CPI: 0.0213, not statistically significant.

- Keep the attenuation claim restrained:
  - The WPI and PPAC rows use different shock variables and samples.
  - The integrated table is an attenuation map, not a single mechanical causal chain.
  - The cleanest formal attenuation test remains the consumer-chain Stage 1 versus Stage 3 Wald test.

- Correct diagnostics and bootstrap wording:
  - Bootstrap p = 0.8196 belongs to the pooled WPI Fuel and Power context model.
  - The preferred WPI Fuel and Power model is reported with HAC asymmetry p = 0.1642.

- Keep CPI statements reviewer-safe:
  - Headline CPI pass-through is positive but statistically insignificant, not zero.
  - CPI Fuel and Light is bridge evidence because the sample starts in 2011.
  - The PPAC-to-Fuel Granger result does not reject at 5 percent, so it should be stated as supportive bridge evidence, not causal proof.

- Use CPT- consistently as the negative cumulative pass-through coefficient.
  - Do not write `|CPT-|`.
  - Do not call it the absolute value of negative pass-through.

## Files changed

- `build_aniket_dissertation.py`
- `_diss_chapters.py`
