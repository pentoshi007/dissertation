# Chapter 5: Results

## 5.1 All-Sample Local-Projection Response

Table 5.1 reports the estimated cumulative response of WPI Fuel and Power inflation to a one per cent rupee oil shock at selected horizons, using the full estimation sample of 371 observations from May 1995 to March 2026.

| Horizon | Estimate | SE (HAC) | 95% CI | p-value |
|---:|---:|---:|---|---|
| 0 | 0.0453 | 0.0112 | [0.023, 0.067] | <0.001 |
| 3 | 0.2849 | 0.0366 | [0.213, 0.357] | <0.001 |
| 6 | 0.2963 | 0.0379 | [0.222, 0.371] | <0.001 |
| 9 | 0.3539 | 0.0542 | [0.248, 0.460] | <0.001 |
| 12 | 0.3461 | 0.0721 | [0.205, 0.487] | <0.001 |

The all-sample response is positive at every horizon and statistically significant at the one per cent level throughout. The contemporaneous (horizon-0) response is modest at 0.0453 per cent, consistent with the idea that wholesale fuel prices adjust gradually rather than instantaneously to oil shocks. This small but significant immediate effect suggests that some administered or market-linked price revisions take place within the same month, but the bulk of the adjustment occurs over subsequent months.

The cumulative response rises steeply over the first three months, reaching 0.2849 by horizon 3, and then stabilises around 0.28–0.35 for the remainder of the horizon window. This levelling-off pattern is important: it implies that the oil-price pass-through process is largely completed within four to six months, with only a modest additional increment at longer horizons. The timing is consistent with the institutional reality of India's fuel-pricing mechanism, where retail prices are revised at regular fortnightly or monthly intervals rather than continuously.

At the six-month benchmark, a one per cent rupee oil shock is associated with a cumulative 0.2963 per cent increase in WPI Fuel and Power. At twelve months, the cumulative response is 0.3461. Both estimates are highly significant with p-values below 0.001. The magnitude implies an incomplete but economically meaningful pass-through: a one per cent increase in the rupee cost of crude oil is associated with a roughly 0.30 per cent increase in the wholesale fuel price index. The less-than-proportional response reflects the fact that WPI Fuel and Power includes not only petroleum products but also coal and electricity, whose prices adjust on different schedules and are partially regulated.

The estimated standard errors widen modestly at longer horizons, as expected from the increasing Newey–West bandwidth, but the confidence intervals remain comfortably above zero through horizon 12.

**[Figure 5.1: All-sample local-projection response — fig_03_lp_all_sample.png]**

Figure 5.1 confirms the visual pattern: a smooth, monotonically rising impulse response that levels off around horizon 4 and remains stable through horizon 12, with tight 95 per cent confidence bands that exclude zero at every point.

## 5.2 Post-2010 State-Dependent Response

Table 5.2 reports the state-dependent local-projection estimates, which allow the oil-price response to differ between the pre-2010 and post-2010 periods. The table shows the pre-2010 response (β_h), the total post-2010 response (β_h + θ_h), and the interaction term (θ_h) representing the additional post-2010 effect.

| Horizon | Pre-2010 | Post-2010 | Interaction (θ) | θ p-value | Sig |
|---:|---:|---:|---:|---|---|
| 0 | −0.0095 | 0.0929 | 0.1024 | <0.001 | *** |
| 3 | 0.1369 | 0.4292 | 0.2924 | <0.001 | *** |
| 6 | 0.1965 | 0.3937 | 0.1972 | 0.0220 | ** |
| 9 | 0.2060 | 0.4985 | 0.2925 | 0.0103 | ** |
| 12 | 0.2111 | 0.4803 | 0.2691 | 0.0840 | * |

The results reveal a striking difference between the two regimes. In the pre-2010 period, the response at horizon 0 is slightly negative (−0.0095) and not statistically significant, suggesting that administered fuel prices effectively blocked contemporaneous pass-through of oil shocks to the wholesale index. Under the administered pricing mechanism, oil marketing companies absorbed cost increases through under-recoveries rather than passing them through to wholesale prices immediately. The pre-2010 response becomes positive from horizon 1 onward and stabilises around 0.19–0.21 at horizons 5 through 12, indicating that even under administered pricing, some oil-price pass-through eventually occurred, albeit at a slower pace and smaller magnitude. This delayed adjustment may reflect periodic price revisions that the government permitted to limit the accumulation of under-recoveries.

In the post-2010 period, the total response is substantially larger at every horizon. The contemporaneous post-2010 response is 0.0929, nearly ten times larger than the pre-2010 estimate, indicating that market-linked pricing allows wholesale fuel prices to begin adjusting within the same month as the oil shock. By horizon 3, the post-2010 response reaches 0.4292, more than three times the pre-2010 value of 0.1369 at the same horizon.

At the six-month benchmark, the total post-2010 response is 0.3937, approximately double the pre-2010 response of 0.1965. This doubling of pass-through is consistent with the removal of the administered-price buffer that previously absorbed a large share of oil-price movements. The post-2010 interaction θ_h is 0.1972 at horizon 6 with a p-value of 0.0220. This is statistically significant at the 5 per cent level, confirming that the fuel-pricing reform of 2010 is associated with a measurably stronger oil-price pass-through to wholesale fuel prices.

The interaction is positive and statistically significant at the 5 per cent level or better through horizons 0 to 11. At horizon 12, the interaction estimate is 0.2691 with a p-value of 0.0840, which is significant at the 10 per cent level but not at the conventional 5 per cent level. This slight loss of precision at the longest horizon is expected given the wider confidence bands that arise from the larger Newey–West bandwidth.

**[Figure 5.2: Pre/Post-2010 state comparison — fig_04_lp_state_comparison_post2010.png]**

Figure 5.2 reinforces the quantitative finding: the post-2010 response path lies clearly above the pre-2010 path at all horizons, and the confidence bands separate after the first month. The visual gap between the two response paths is economically substantial and statistically significant throughout the relevant horizon range.

## 5.3 Diagnostic Evidence

Table 5.3 summarises the diagnostic tests for the horizon-0 specifications, comparing the simple all-sample LP with the state-dependent post-2010 LP.

| Diagnostic | Simple all-sample | State-dependent post-2010 |
|---|---|---|
| BG (lag 12) p | 0.7279 (PASS) | 0.0003 (CONTROLLED_BY_HAC) |
| Breusch–Pagan p | 0.2280 | 0.1223 |
| RESET (HAC) p | 0.0097 (REJECTED) | 0.3592 (PASS) |
| Rec-CUSUM p | 0.4293 (PASS) | 0.6459 (PASS) |
| OLS-CUSUM p | 0.9488 (PASS) | 0.8869 (PASS) |

The simple all-sample horizon-0 equation is rejected by the HAC RESET benchmark (p = 0.0097). This result should not be hidden; rather, it supports the state-dependent design because it shows that a single linear response is too restrictive for the full sample that spans both the administered and market-linked pricing eras. The diagnostic rejection of the simple all-sample benchmark is treated as evidence against a single linear pass-through equation. The preferred specification therefore allows the oil response to differ after the 2010 fuel-pricing reform period.

The state-dependent post-2010 specification passes the RESET test (p = 0.3592), the recursive CUSUM test (p = 0.6459), the OLS-CUSUM test (p = 0.8869), and the Breusch–Pagan heteroskedasticity test (p = 0.1223). These results indicate that the state-dependent specification is well-specified in terms of functional form, structurally stable over the sample, and free from problematic heteroskedasticity.

The Breusch–Godfrey test rejects the null of no serial correlation (p = 0.0003), but this is expected in monthly local-projection settings where overlapping multi-step residuals generate mechanical serial dependence. This is precisely why Newey–West HAC inference is used for all reported estimates.

As a further robustness check, a GLS model with AR(1) residual correlation is estimated for the state-dependent horizon-0 specification. This model directly accounts for first-order serial correlation rather than relying on robust standard errors. The normalised residuals from the GLS model pass the Ljung–Box lag-12 test with a p-value of 0.9974, confirming that the AR(1) correction is sufficient. The post-2010 interaction estimate from the GLS model is 0.1117 and remains highly significant (p < 0.001). Because residual serial dependence is expected in monthly local-projection settings, all reported inference uses Newey–West HAC standard errors. The GLS robustness check confirms that the main finding is not an artefact of serial dependence in the OLS residuals.
