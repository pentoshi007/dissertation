# Chapter 3: Data and Variables

## 3.1 Data Sources and Sample Coverage

The empirical analysis draws on three primary data sources, each available at monthly frequency. Table 3.1 summarises the series, their coverage, and the number of observations.

| Series | Start | End | N | Span (years) |
|---|---|---|---:|---:|
| WPI Fuel & Power chained | 1994-04 | 2026-03 | 384 | 32.00 |
| Brent USD | 1960-01 | 2026-03 | 795 | 66.25 |
| INR/USD exchange rate | 1973-01 | 2026-03 | 639 | 53.25 |
| Matched model data | 1994-04 | 2026-03 | 384 | 32.00 |

The WPI Fuel and Power data are sourced from the Office of the Economic Adviser (OEA), Ministry of Commerce and Industry. The OEA publishes monthly WPI figures for all major commodity groups, including the Fuel, Power, Light, and Lubricants sub-group, which is the wholesale-level measure most directly linked to petroleum product costs. The Brent crude oil price in US dollars per barrel is taken from the World Bank Pink Sheet, which reports monthly average commodity prices compiled from major international exchanges. The INR/USD exchange rate is sourced from the Federal Reserve Bank of St Louis (FRED) EXINUS series, which provides a monthly average of the bilateral exchange rate.

## 3.2 Chaining the WPI Fuel and Power Index

The OEA publishes the WPI under successive base years: 1993–94, 2004–05, and 2011–12. Each base-year revision changes the index weights and reference level, so the raw series from different base years are not directly comparable. To construct a continuous monthly series, the study chains the three base-year segments onto the most recent 2011–12 base using official linking factors.

The linking procedure divides older-base observations by the cumulative chain factor to express them on the 2011–12 scale. The 1993–94 base series covering April 1994 to December 2004 is divided by the product of the 1993–94-to-2004–05 factor (2.802) and the 2004–05-to-2011–12 factor (1.690), yielding a combined divisor of 4.735. The 2004–05 base series covering January 2005 to March 2012 is divided by the 2004–05-to-2011–12 factor (1.690). Observations from April 2012 onward, already on the 2011–12 base, require no adjustment. Figure 3.1 plots the resulting chained WPI Fuel and Power index from April 1994 to March 2026.

**[Figure 3.1: Chained WPI Fuel and Power Index — fig_01_wpi_fuel_chained.png]**

The chained series shows the broad pattern expected from India's fuel-price history: a gradual increase through the late 1990s and early 2000s under administered pricing, a sharp rise during the 2007–08 oil boom, a collapse during the 2008–09 global financial crisis, a recovery and plateau during the 2010–14 period of partial deregulation, a decline during the 2014–16 oil price downturn, and a volatile recovery culminating in the post-COVID surge of 2021–22.

## 3.3 Constructing the Rupee Oil Price

The key independent variable in this study is the rupee-denominated oil price, defined as:

> oil_INR_t = Brent_USD_t × INR_per_USD_t

This formulation captures the cost of crude oil as faced by Indian refiners and, by extension, the wholesale fuel market. A rise in the dollar price of Brent, a depreciation of the rupee, or both simultaneously will increase the rupee oil price and create a cost-push impulse for WPI Fuel and Power.

The analysis uses monthly log differences of all variables, multiplied by 100 to express changes in percentage terms. Figure 3.2 plots the monthly rupee oil shock series, which displays high volatility with monthly changes ranging from approximately −47 to +40 per cent. Notable episodes include the 1998 Asian crisis, the 2008 global financial crisis, the 2014–15 oil price collapse, and the extreme movements in April 2020 during the initial COVID-19 lockdowns.

**[Figure 3.2: Monthly rupee oil shocks — fig_02_rupee_oil_shock.png]**

## 3.4 Additional Variables and Controls

The model includes the following additional variables: the change in the log INR/USD exchange rate, capturing exchange-rate movements not already embedded in the rupee oil price; a post-2010 indicator (d_post2010) equal to one from July 2010 onward, marking petrol price deregulation; a post-2014 indicator (d_post2014) equal to one from November 2014 onward, marking diesel deregulation; a COVID dummy equal to one from April 2020 to September 2020; and eleven monthly dummies to absorb systematic seasonal variation in fuel prices.

## 3.5 Descriptive Statistics

Table 3.2 reports summary statistics for the main variables in levels and log differences.

| Variable | N | Mean | SD | Min | Median | Max |
|---|---:|---:|---:|---:|---:|---:|
| WPI Fuel & Power | 384 | 81.54 | 39.04 | 22.87 | 81.20 | 167.10 |
| Brent USD | 384 | 58.06 | 31.86 | 9.80 | 58.43 | 133.87 |
| INR/USD | 384 | 55.32 | 16.03 | 31.37 | 48.36 | 92.82 |
| Rupee oil (INR) | 384 | 3432.55 | 2239.54 | 417.39 | 3208.35 | 9624.23 |
| Δln WPI Fuel (%) | 383 | 0.50 | 2.33 | −11.18 | 0.29 | 9.06 |
| Δln Rupee oil (%) | 383 | 0.79 | 9.25 | −47.01 | 1.78 | 39.97 |

The mean monthly rupee oil change is 0.79 per cent, reflecting a secular upward drift in both dollar oil prices and the INR/USD rate over the sample. The standard deviation of 9.25 per cent confirms the high volatility of this series. The WPI Fuel and Power index ranges from 22.87 (in the mid-1990s on the 2011–12 base) to 167.10 (in 2022), illustrating the wide variation available for estimation.

## 3.6 Unit Root Tests

Table 3.3 reports Augmented Dickey–Fuller (ADF) unit root tests for the log-level and first-difference forms of each variable.

| Variable | Form | ADF stat | 5% CV | Stationary? |
|---|---|---:|---:|---|
| ln(WPI Fuel & Power) | Level | −2.07 | −3.42 | NO |
| ln(Rupee Brent oil) | Level | −3.02 | −3.42 | NO |
| ln(INR/USD) | Level | −2.18 | −3.42 | NO |
| Δln(WPI Fuel & Power) | First Diff | −12.05 | −2.87 | YES |
| Δln(Rupee Brent oil) | First Diff | −12.94 | −2.87 | YES |
| Δln(INR/USD) | First Diff | −12.87 | −2.87 | YES |

All log-level series fail to reject the null of a unit root at the 5 per cent level, while all first-differenced series reject it decisively. This confirms that the variables are integrated of order one, I(1), and that monthly log differences are the appropriate transformation for estimation. The local-projection specification uses these first differences as both the dependent variable (in cumulative form) and the explanatory variables.

## 3.7 Estimation Sample

After constructing twelve monthly lags for dynamic controls, the main estimation sample runs from May 1995 to March 2026, comprising 371 observations and spanning 30.92 years. This exceeds the 30-year threshold commonly regarded as a minimum for reliable time-series inference at monthly frequency.
