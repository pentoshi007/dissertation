# Model Diagnostic Notes

## What changed after the first run

The first implementation used six monthly dynamic controls. That version produced strong results, but it still left a serial-correlation concern in the state-dependent horizon-0 equation. The updated model now uses twelve monthly dynamic controls. This keeps the estimation sample above 30 years while reducing avoidable omitted-dynamics criticism.

Current main estimation sample:

- May 1995 to March 2026.
- 30.92 years after lag construction.

## Main diagnostic position

Do not write that every possible diagnostic test in every benchmark model passes. That is too broad and can be challenged. The safe statement is:

> The main state-dependent local-projection specification passes the functional-form and recursive-stability diagnostics. Serial correlation is handled by Newey-West HAC inference in the local projections, and a GLS AR(1) residual robustness check passes the Ljung-Box lag-12 test.

This is stronger and more defensible than trying to hide or force a diagnostic result.

## Current gate status

From `new-model/outputs/tables/table_11_publication_triage.csv`:

- Raw data present: PASS.
- Main sample above 30 years: PASS.
- One common monthly timeline: PASS.
- All-sample six-month response positive and significant: PASS.
- All-sample twelve-month response positive: PASS.
- Post-2010 state-dependence check: PASS.
- Horizon-0 state-dependent functional-form diagnostic: PASS.
- Serial-correlation robustness check: PASS.
- Asymmetry kept secondary: PASS.
- Post-2014 robustness: reported, but not used as a gate or headline claim.

## How to discuss the benchmark issue

The simple all-sample horizon-0 benchmark is rejected by the HAC RESET check. This should not be hidden. It supports the state-dependent design because it shows that a single linear response is too restrictive.

Safe wording:

> The diagnostic rejection of the simple all-sample benchmark is treated as evidence against a single linear pass-through equation. The preferred specification therefore allows the oil response to differ after the 2010 fuel-pricing reform period.

Avoid:

> All specifications pass all tests.

That sentence is not true and would invite criticism.

## How to discuss serial correlation

The state-dependent OLS local-projection residuals still show serial dependence under the Breusch-Godfrey diagnostic. This is common in time-series local projections and is why Newey-West HAC inference is used. The added GLS AR(1) robustness check directly models serial correlation and gives:

- Ljung-Box lag-12 p-value = 0.9974.
- Post-2010 interaction estimate remains positive and significant.

Safe wording:

> Because residual serial dependence is expected in monthly local-projection settings, all reported inference uses Newey-West HAC standard errors. As a robustness check, a GLS model with AR(1) residual correlation leaves the post-2010 interaction positive and significant, and its normalized residuals pass the Ljung-Box lag-12 check.

## How to discuss post-2014

The post-2014 interaction is positive but not statistically significant at the six-month horizon. It should not be sold as proof of diesel deregulation.

Safe wording:

> The post-2014 estimates are consistent in sign but weaker in precision, so the paper treats them as contextual robustness rather than as the main reform result.

Avoid:

> Diesel deregulation caused stronger pass-through.
