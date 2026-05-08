# Chapter 6: Robustness and Limitations

## 6.1 Post-2014 Diesel Deregulation

India completed diesel price deregulation in October 2014. To test whether this second reform further strengthened oil-price pass-through, the state-dependent local projection is re-estimated with a post-2014 indicator replacing the post-2010 indicator. Table 6.1 reports the results at selected horizons.

| Horizon | Pre-2014 | Post-2014 | Interaction (θ) | θ p-value |
|---:|---:|---:|---:|---|
| 0 | −0.0027 | 0.0937 | 0.0964 | <0.001 |
| 6 | 0.2509 | 0.3497 | 0.0988 | 0.2809 |
| 12 | 0.2981 | 0.4048 | 0.1067 | 0.4672 |

The post-2014 interaction is positive at the six-month horizon (0.0988) but not statistically significant at conventional levels (p = 0.2809). At shorter horizons, the interaction is significant, reflecting the rapid adjustment of recently deregulated diesel prices. However, at the medium-run benchmarks of six and twelve months, the effect becomes imprecise, possibly because the post-2014 sub-sample is shorter and includes the COVID period, which introduces substantial noise.

The post-2014 estimates are consistent in sign but weaker in precision, so this dissertation treats them as contextual robustness rather than as the main reform result. The evidence does not support the claim that diesel deregulation caused a separately identifiable strengthening of pass-through beyond the effect already captured by the post-2010 petrol deregulation indicator.

**[Figure 6.1: Pre/Post-2014 comparison — fig_05_lp_state_comparison_post2014.png]**

## 6.2 High Oil-Volatility Months

To test whether pass-through is larger during periods of extreme oil-price movements, the sample is split using a high-volatility indicator defined as months in which the absolute rupee oil shock exceeds the 75th percentile of the sample distribution. Table 6.2 reports the results.

| Horizon | Normal vol. | High vol. | Interaction | θ p-value |
|---:|---:|---:|---:|---|
| 0 | 0.0190 | 0.0523 | 0.0333 | 0.1332 |
| 6 | 0.2762 | 0.3083 | 0.0321 | 0.7541 |
| 12 | 0.4966 | 0.3230 | −0.1736 | 0.2783 |

The high-volatility interaction is small and statistically insignificant at the six-month benchmark (0.0321, p = 0.7541). At longer horizons, the interaction turns slightly negative, suggesting that extreme oil-price movements may initially produce faster adjustment but do not result in a permanently larger cumulative response. This pattern is consistent with a fuel-pricing mechanism that eventually adjusts fully regardless of the size of the initial shock.

**[Figure 6.2: Normal vs high volatility — fig_06_lp_high_volatility.png]**

## 6.3 Asymmetry Between Positive and Negative Shocks

A specification separating positive and negative rupee oil shocks is estimated to test whether upward oil-price pass-through exceeds downward pass-through—the so-called rockets-and-feathers hypothesis. At the six-month horizon, the Wald test for equal responses gives F = 0.61 (p = 0.4357), failing to reject the null of symmetric pass-through. At the twelve-month horizon, the test rejects at the 5 per cent level (p = 0.0465), with the positive-shock response (0.6425) substantially exceeding the negative-shock response (0.1162). However, this single marginal rejection at the longest horizon, where confidence bands are widest, does not constitute strong evidence of systematic asymmetry. The asymmetry exercise is therefore reported as a secondary robustness table rather than as a main finding.

## 6.4 Limitations

Several limitations should be acknowledged. First, the local-projection estimates capture reduced-form associations and should not be interpreted as structural causal effects. The rupee oil price is not randomly assigned, and the estimated coefficients may reflect both direct cost-push effects and correlated macroeconomic conditions. Second, the chaining of WPI series across base years introduces a degree of measurement error, particularly around the splicing points. While the linking factors are official OEA ratios, the underlying commodity baskets differ across base years. Third, the post-2010 indicator is a binary variable that does not capture the gradual pace of actual reform implementation. Fourth, the COVID dummy may not fully capture pandemic effects on both oil markets and domestic fuel demand. Fifth, the analysis focuses on the wholesale fuel layer and does not trace pass-through to consumer prices or broader macroeconomic outcomes.

Despite these limitations, the main state-dependent local-projection specification passes the key diagnostic benchmarks—functional form, stability, and serial-correlation robustness—providing confidence that the estimated post-2010 effect is not driven by obvious specification errors.
