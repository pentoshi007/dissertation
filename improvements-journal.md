# Improvements for `build_journal_paper.py`

This checklist records the journal-paper corrections needed after the model fixes in `fixes-applied.md`.

## Applied changes

- Replace the old WPI Fuel and Power claim with the preferred specification:
  - Sample: April 2010 to March 2026, excluding April to September 2020.
  - N = 186.
  - CPT+ = 0.5205, p < 0.001.
  - CPT- = 0.4195, p < 0.001.
  - Asymmetry p = 0.1642.
  - Diagnostic gate passes.

- Retain the full-sample pooled WPI Fuel and Power model only as transparency context:
  - It gives CPT+ = 0.2866 and CPT- = 0.2677 over 371 observations.
  - It fails HAC-RESET and should not be described as the preferred result.

- Remove internal output-table codes from the reader-facing prose.
  - The old line naming "WPI tables 04b and 06b, CPI table 06, PPAC table 22b, and bridge table 27b" was replaced.
  - The revised version says that full lag coefficients are retained in the replication material, while the article reports cumulative pass-through and compact diagnostics.

- Make the journal framing beginner-safe and reviewer-safe:
  - State that retail petrol is the strongest direct fuel response in the consumer-side chain, not across every model.
  - State that the preferred WPI Fuel and Power value is numerically largest, but uses a different sample and shock variable.
  - Do not present the layered map as one mechanical Brent-to-WPI-to-CPI causal chain.
  - Keep the formal attenuation claim tied to the consumer-chain Wald test.

- Update the main results table:
  - WPI Fuel and Power now shows the preferred post-2010 excluding-COVID estimate.
  - The table note explains that the preferred WPI row excludes April to September 2020.

- Update diagnostics:
  - Preferred WPI Fuel and Power passes BG, HAC-RESET, and Rec-CUSUM.
  - The pooled WPI Fuel and Power model is marked as context only.
  - CPI M2 and M3 remain excluded from main claims.

- Use a reader-facing WPI figure:
  - The journal draft now uses the pre/post-2010 wholesale pass-through figure to support the regime-mixing discussion.
  - The preferred excluding-COVID estimate remains in the table, where the exact diagnostic status is clear.

- Keep the publication version cautious:
  - Do not call any target "active UGC-CARE approved" without separate current verification.
  - For actual double-blind journal submission, remove author-identifying and supervisor-identifying material from the anonymous manuscript and keep it only on the title page or acknowledgement file required by the journal.

## Files changed

- `build_journal_paper.py`
