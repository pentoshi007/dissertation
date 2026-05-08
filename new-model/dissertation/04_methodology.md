# Chapter 4: Methodology

## 4.1 Local Projections

This study estimates impulse responses using the local-projection (LP) method introduced by Jordà (2005). Unlike a vector autoregressive (VAR) system, which estimates a single set of dynamic equations and iterates them forward to obtain impulse responses at successive horizons, the LP approach runs a separate regression for each horizon h = 0, 1, 2, …, H. The dependent variable at each horizon is the cumulative change in the outcome variable from the period before the shock to h periods after it.

The advantage of this approach is twofold. First, each horizon's regression is estimated independently, so any misspecification at one horizon does not propagate to others. Second, the LP framework accommodates state-dependent responses by simply interacting the shock variable with a state indicator, without requiring the researcher to estimate and invert a nonlinear VAR.

The baseline all-sample specification is:

> 100 × [ln(WPI Fuel_{t+h}) − ln(WPI Fuel_{t−1})] = α_h + β_h Δln(oil_INR_t) + lag controls + month FE + ε_{t+h}

where the left-hand side measures the cumulative percentage change in the chained WPI Fuel and Power index from month t−1 to month t+h. The coefficient β_h captures the cumulative response of WPI Fuel and Power inflation to a one per cent rupee oil shock at horizon h.

## 4.2 Lag Controls

The specification includes twelve monthly lags of three variables as dynamic controls: lagged WPI Fuel and Power inflation, lagged rupee oil shocks, and lagged exchange-rate changes. The inclusion of a full year of lagged controls serves two purposes. First, it absorbs serial dependence in the dependent variable and the regressors, reducing the risk of omitted-dynamics bias. Second, it ensures that the estimated contemporaneous response β_h reflects the marginal effect of the current-period shock, conditional on the recent history of fuel inflation, oil prices, and exchange rates.

The choice of twelve lags follows from the monthly frequency of the data: a full year of dynamic controls captures any annual cyclical pattern that might otherwise confound the estimated oil-shock response. Using twelve rather than six lags reduces the estimation sample by an additional six months, but the main sample remains above 30 years (30.92 years from May 1995 to March 2026), which is well above the threshold for reliable monthly time-series inference.

Additional controls include eleven month fixed effects to capture systematic seasonal patterns in fuel pricing, such as those associated with budget cycles or seasonal demand; a COVID dummy for April–September 2020 to absorb the extreme supply-chain disruption and demand collapse during the initial pandemic period; and a post-2010 level shift in the all-sample specification to absorb any structural change in the average rate of WPI fuel inflation after deregulation. This level control ensures that the oil-shock coefficient captures the marginal response to shocks rather than the difference in mean inflation between the two periods.

## 4.3 State-Dependent Specification

To test whether fuel-pricing reform altered the oil-price pass-through, the study estimates a state-dependent version of the local projection:

> … + β_h Δln(oil_INR_t) + θ_h Δln(oil_INR_t) × Post2010_t + …

Here, β_h captures the pre-2010 response and θ_h captures the additional response in the post-2010 period. The total post-2010 response is β_h + θ_h. The post-2010 indicator equals one from July 2010 onward, corresponding to the month following the government's announcement of petrol price deregulation. The same state-dependent structure is applied with a post-2014 indicator (from November 2014, corresponding to diesel deregulation) as a robustness exercise. A high-volatility indicator, defined as months in which the absolute rupee oil shock exceeds the 75th percentile of the sample distribution, is also used to test whether pass-through differs during periods of large price movements.

## 4.4 Inference: Newey–West HAC Standard Errors

Local projections with multi-step-ahead dependent variables generate overlapping residuals that are serially correlated by construction. At horizon h, the dependent variable is the cumulative change from t−1 to t+h, so the residuals from adjacent observations share h overlapping months. Standard OLS standard errors, which assume independent residuals, are therefore inappropriate and would produce misleadingly narrow confidence intervals.

This study uses Newey–West heteroskedasticity and autocorrelation consistent (HAC) standard errors for all reported estimates. The Newey–West estimator allows for both heteroskedasticity and autocorrelation of unknown form in the residuals, producing valid inference even when the true error covariance structure is not known.

The bandwidth for the Newey–West kernel is set to max(4, h + 1) for each horizon h, following the recommendation that the bandwidth should be at least as large as the forecast horizon to account for the mechanical overlap in residuals. All reported confidence intervals are 95 per cent intervals constructed as the point estimate ± 1.96 × HAC standard error.

## 4.5 Diagnostics

The study reports a battery of diagnostic tests for the horizon-0 equations, which are the most important for detecting specification problems:

- Breusch–Godfrey test (order 12) for residual serial correlation. If the BG test rejects, this does not invalidate the LP estimates because HAC standard errors are designed to handle serial correlation, but it motivates the GLS robustness check described below.
- RESET test with HAC variance for functional-form misspecification, checking whether powers of the fitted values improve the model. A rejection suggests that a linear specification is too restrictive.
- Recursive CUSUM and OLS-CUSUM tests for parameter stability, checking whether estimated coefficients remain stable over the sample period.
- GLS with AR(1) residual correlation as a serial-correlation robustness check. This model directly accounts for first-order serial correlation in the residuals and is assessed using the Ljung–Box test on normalised residuals at lag 12.

## 4.6 Horizon Range

Impulse responses are estimated for horizons h = 0 through 12, corresponding to the contemporaneous month through twelve months after the shock. This range captures the short- to medium-run pass-through of oil shocks to wholesale fuel prices. The six-month horizon is used as the primary reporting benchmark, with the twelve-month horizon serving as the medium-run estimate.
