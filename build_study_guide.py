#!/usr/bin/env python3
"""Build a beginner-friendly dissertation study guide from archived outputs."""

from __future__ import annotations

import csv
import re
import textwrap
from pathlib import Path


ROOT = Path(__file__).resolve().parent
ARCHIVE = Path("/private/tmp/fresh-dissertation-head")
OUT_MD = ROOT / "dissertation_study_guide.md"


def read_csv(rel: str) -> list[dict[str, str]]:
    with (ARCHIVE / rel).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def fmt(x: str | float | int, digits: int = 4) -> str:
    if x is None:
        return ""
    s = str(x)
    if s.lower() in {"nan", "na", ""}:
        return ""
    try:
        v = float(s)
    except ValueError:
        return s
    if abs(v) < 0.00005 and v != 0:
        return "<0.0001"
    return f"{v:.{digits}f}".rstrip("0").rstrip(".")


def esc_latex(s: str) -> str:
    s = "" if s is None else str(s)
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in s)


def markdown_table(rows: list[dict[str, str]], cols: list[str]) -> str:
    out = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for row in rows:
        out.append("| " + " | ".join(str(row.get(c, "")).replace("\n", " ") for c in cols) + " |")
    return "\n".join(out)


def coefficient_meaning(var: str, model: str) -> str:
    if var == "(Intercept)":
        return "Baseline monthly inflation when included controls are zero and the omitted month is the reference month."
    if re.match(r"dln_dep_L\d+", var):
        return "Lag of the dependent WPI inflation rate; captures persistence in that WPI layer."
    if re.match(r"dlnCPI_L\d+", var):
        return "Lag of headline CPI inflation; captures inflation persistence."
    if re.match(r"dlnFuel_L\d+", var):
        return "Lag of CPI Fuel and Light inflation; captures persistence in the fuel-light component."
    if re.match(r"dlnPetrol_L\d+", var):
        return "Lag of retail petrol inflation; captures inertia in pump-price adjustment."
    if "oil_pos" in var or "Oil_pos" in var:
        return "Effect of a positive rupee-oil change at this lag. The cumulative positive pass-through sums all such lags."
    if "oil_neg" in var or "Oil_neg" in var:
        return "Effect of a negative rupee-oil change at this lag. Since negative shocks are entered as negative numbers, a positive coefficient means prices fall when oil falls."
    if "Brent_pos" in var or "brent_pos" in var:
        return "Effect of a positive Brent change at this lag. Used for the retail-petrol and decomposition specifications."
    if "Brent_neg" in var or "brent_neg" in var:
        return "Effect of a negative Brent change at this lag. Positive coefficient means retail prices decline with Brent declines."
    if "Petrol_pos" in var:
        return "Effect of a positive retail-petrol change on CPI Fuel and Light at this lag."
    if "Petrol_neg" in var:
        return "Effect of a negative retail-petrol change on CPI Fuel and Light at this lag."
    if var in {"dln_exr", "dlnEXR"}:
        return "Contemporaneous exchange-rate change; a rupee depreciation raises the rupee cost of imports."
    if var in {"dln_exr_L1", "dlnEXR_L1"}:
        return "One-month lag of exchange-rate change."
    if var == "dlnIIP":
        return "Monthly IIP growth; proxy for domestic activity/demand conditions."
    if var in {"D_petrol", "d_reform"}:
        return "Policy-regime dummy; it shifts the intercept after the relevant deregulation/reform date."
    if var == "D_diesel":
        return "Diesel deregulation dummy from October 2014; captures a level shift in monthly inflation."
    if var in {"D_covid", "d_covid"}:
        return "COVID shock dummy. CPI uses April 2020; WPI uses April-September 2020."
    if var.startswith("month") or var.startswith("mo_"):
        return "Monthly seasonal dummy, measured relative to the omitted reference month."
    return "Control or generated regressor used by the model."


def coefficient_longtable(rel: str, caption: str, model: str) -> str:
    rows = read_csv(rel)
    lines = [
        r"\begingroup",
        r"\scriptsize",
        r"\setlength{\LTleft}{0pt}",
        r"\setlength{\LTright}{0pt}",
        r"\begin{longtable}{p{0.23\textwidth}rrrrp{0.37\textwidth}}",
        rf"\caption{{{esc_latex(caption)}}}\\",
        r"\toprule",
        r"Variable & Estimate & NW SE & t & p & Meaning \\",
        r"\midrule",
        r"\endfirsthead",
        r"\toprule",
        r"Variable & Estimate & NW SE & t & p & Meaning \\",
        r"\midrule",
        r"\endhead",
    ]
    for r in rows:
        lines.append(
            f"{esc_latex(r['Variable'])} & {fmt(r['Estimate'], 4)} & {fmt(r['NW_SE'], 4)} & "
            f"{fmt(r['t_value'], 3)} & {fmt(r['p_value'], 4)} & "
            f"{esc_latex(coefficient_meaning(r['Variable'], model))} \\\\"
        )
    lines += [r"\bottomrule", r"\end{longtable}", r"\endgroup"]
    return "\n".join(lines)


def code_block(path: str, start: int, end: int, title: str) -> str:
    lines = (ARCHIVE / path).read_text(encoding="utf-8").splitlines()
    snippet = "\n".join(lines[start - 1 : end])
    snippet = snippet.replace("─", "-").replace("═", "=")
    return f"\n**{title}**\n\n```r\n{snippet}\n```\n"


def csv_summary_row(rel: str) -> str:
    rows = read_csv(rel)
    return markdown_table(rows, list(rows[0].keys()))


def main() -> None:
    wpi_main = read_csv("wpi/outputs/tables/table_04_headline_main_model.csv")[0]
    wpi_fuel = read_csv("wpi/outputs/tables/table_06_fuel_power_model.csv")[0]
    cpi_m1 = read_csv("improved-v2/outputs/tables/table_10_model_comparison.csv")[1]
    ppac = read_csv("improved-v2/outputs/tables/table_22_ppac_retail_fuel.csv")[0]
    fuel_direct = read_csv("improved-v2/outputs/tables/table_16_fuel_light.csv")[0]
    bridge = read_csv("improved-v2/outputs/tables/table_27_ppac_to_fuel_bridge.csv")[0]

    text = f"""---
title: "Dissertation Study Guide"
subtitle: "From Crude Oil to Consumer Inflation: Transmission and Attenuation Across India's Price System"
author: "Prepared from dissertation.docx and the R pipeline outputs"
date: "29 April 2026"
documentclass: report
geometry: margin=0.8in
fontsize: 10pt
toc: true
toc-depth: 2
numbersections: true
colorlinks: true
linkcolor: blue
urlcolor: blue
header-includes:
  - \\usepackage{{booktabs}}
  - \\usepackage{{longtable}}
  - \\usepackage{{array}}
  - \\usepackage{{amsmath}}
  - \\usepackage{{amssymb}}
  - \\usepackage{{microtype}}
  - \\usepackage{{fancyhdr}}
  - \\pagestyle{{fancy}}
  - \\fancyhf{{}}
  - \\fancyhead[L]{{Dissertation Study Guide}}
  - \\fancyhead[R]{{\\thepage}}
  - \\setlength{{\\parskip}}{{0.55em}}
  - \\setlength{{\\parindent}}{{0pt}}
---

\\setcounter{{chapter}}{{-1}}

# How To Read This Guide

This guide is for viva preparation, not for adding more decorative theory to the dissertation. Read it in three passes.

First, read Chapters 1-3 to understand the story: an international oil shock enters India as a rupee oil shock, moves strongly into retail petrol and fuel-sensitive wholesale prices, and then becomes much weaker by the time it reaches headline CPI. This is the dissertation's core idea: transmission with attenuation.

Second, read Chapters 4-6 with a pencil. These chapters explain the time-series machinery from zero: why log differences are used, why lags are needed, what ADL and NARDL do, and what each diagnostic test is asking. Do not memorise equations mechanically. Learn the words around each equation.

Third, use Chapters 7-10 as viva rehearsal. Chapter 7 is the model-by-model result walk-through. Chapter 9 tells you where the dissertation is weak. Chapter 10 gives full viva answers in a defensible student voice.

The most important discipline in the viva is precision. Do not say "oil significantly affects headline CPI" without qualification. The code says headline CPI pass-through is positive but not significant at 5 percent. A stronger and safer sentence is: "Oil shocks clearly pass through to retail petrol, WPI Fuel and Power, and headline WPI, but the estimated headline CPI response is small and statistically weak."

# The Research Question In Plain English

The dissertation asks one main question:

> When global oil prices move, how much of that shock survives as it travels through India's price system, and where does it get diluted?

The price chain is best understood as layers rather than as one single pipe:

1. Brent crude in US dollars is the world oil price.
2. Brent multiplied by INR/USD gives the rupee oil price, the cost shock India actually faces.
3. Retail petrol prices respond because fuel marketing and pump prices are close to crude costs, though taxes and administered pricing intervene.
4. WPI Fuel and Power responds because it is a fuel-heavy wholesale index.
5. CPI Fuel and Light responds, but its available harmonised series is shorter.
6. Headline CPI responds weakly because fuel has a limited direct weight and many other items dominate the consumer basket.

Why this matters: RBI targets headline CPI, but oil shocks enter the economy upstream. If the shock is strong upstream but diluted before headline CPI, monetary policy should not read a weak headline CPI coefficient as "oil does not matter." It means oil matters through particular layers and relative prices, while the headline index absorbs only a small part of it.

**Asymmetric pass-through in everyday language.** Suppose Brent rises by 10 percent and petrol rises quickly, but when Brent falls by 10 percent petrol falls slowly or less fully. That is asymmetry. The dissertation tests this by splitting oil changes into positive and negative parts.

**Attenuation in everyday language.** Imagine a loud sound passing through several walls. Near the source it is loud; after several walls it is faint. Oil shocks are loud in retail petrol and WPI Fuel and Power, but faint in headline CPI.

# Time-Series Concepts From Zero

## Stationarity, Unit Roots, and Integration

**Intuition.** A stationary series returns to a stable range; a non-stationary series wanders.

**Explanation.** A stationary time series has a roughly stable mean, variance, and autocorrelation structure. A non-stationary series, especially one with a unit root, can drift for long periods. The classic analogy is a drunkard's walk: each step is random, but the location does not naturally return to a fixed centre.

**Formal idea.** A simple unit-root process is

\\[
y_t = y_{{t-1}} + u_t.
\\]

If a series is stationary in levels, it is called \\(I(0)\\). If its first difference is stationary, it is called \\(I(1)\\). If it must be differenced twice, it is \\(I(2)\\).

**Why the dissertation needs it.** Regressing non-stationary levels on each other can create fake relationships. The main ADL models avoid this by using monthly log differences. The NARDL appendix can use levels only because it checks for cointegration.

## White Noise, Autocorrelation, and the Lag Operator

**Intuition.** White noise is pure surprise. Autocorrelation means today's value remembers yesterday's value.

White noise has mean zero, constant variance, and no serial correlation:

\\[
E(u_t)=0, \\quad Var(u_t)=\\sigma^2, \\quad Cov(u_t,u_{{t-k}})=0.
\\]

The lag operator writes yesterday's value compactly: \\(L y_t = y_{{t-1}}\\). Then \\(L^2 y_t = y_{{t-2}}\\).

**Why needed.** Inflation data usually have memory. ADL models include lags of the dependent variable and lags of oil shocks so the model does not pretend all adjustment happens instantly.

## Spurious Regression

**Intuition.** Two unrelated wandering series can look related simply because both trend.

If \\(y_t\\) and \\(x_t\\) are unrelated but both non-stationary, OLS may produce a high \\(R^2\\) and significant t-statistics. That is spurious regression.

**Why needed.** The dissertation therefore estimates the main claim-bearing models in \\(\\Delta \\ln\\) form. The NARDL appendix is used only after bounds testing.

## Cointegration and Long-Run Relationships

**Intuition.** Two variables may wander, but not drift apart forever.

If \\(y_t\\) and \\(x_t\\) are each \\(I(1)\\), but \\(y_t - \\beta x_t\\) is stationary, the two are cointegrated.

**Why needed.** NARDL asks whether there is a long-run relation between price levels and oil-price levels, even if the levels themselves are non-stationary.

## Short Run Versus Long Run

The short run is the month-by-month response: what happens this month, next month, and over the selected lag window. The long run is the total equilibrium relation after temporary dynamics have worked through.

The ADL models in the dissertation are mainly short-run models. Their central reported statistic is cumulative pass-through:

\\[
CPT^+ = \\sum_{{j=0}}^q \\beta_j^+, \\qquad
CPT^- = \\sum_{{j=0}}^q \\beta_j^-.
\\]

## Error Correction

**Intuition.** Error correction is a rubber band. If prices move away from their long-run relation, the error-correction term pulls them back.

A generic ECM is

\\[
\\Delta y_t = \\lambda (y_{{t-1}} - \\theta x_{{t-1}}) + \\text{{short-run terms}} + u_t.
\\]

For a valid correction mechanism, \\(\\lambda\\) should be negative. If \\(\\lambda=-0.08\\), about 8 percent of the disequilibrium is corrected each month.

## Heteroskedasticity, Serial Correlation, and Newey-West HAC

Heteroskedasticity means the error variance is not constant. Serial correlation means errors are correlated over time. Both are common in monthly macro data.

OLS coefficients can still be useful under weaker conditions, but ordinary standard errors become unreliable. Newey-West HAC standard errors adjust inference for heteroskedasticity and autocorrelation. The dissertation uses:

\\[
\\text{{NW lag}} = \\left\\lfloor 0.75 n^{{1/3}} \\right\\rfloor.
\\]

# Variables And Data

## Main Sources

\\begin{{longtable}}{{p{{0.25\\textwidth}}p{{0.35\\textwidth}}p{{0.25\\textwidth}}}}
\\toprule
Variable & What it measures & Source used in code/text \\\\
\\midrule
Brent crude & International benchmark crude oil price in USD per barrel & World Bank Pink Sheet, cached through FRED series POILBREUSDM \\\\
INR/USD & Rupees per US dollar & FRED EXINUS \\\\
Rupee oil price & Brent multiplied by INR/USD & Constructed in code \\\\
Headline WPI & Wholesale price index, chained to 2011-12 base & Office of Economic Adviser, Ministry of Commerce and Industry \\\\
WPI Fuel and Power & Fuel-heavy wholesale sub-index, chained to 2011-12 base & Office of Economic Adviser \\\\
Retail petrol & Delhi retail selling price of petrol & PPAC monthly/ready reckoner files \\\\
Headline CPI & All-India CPI index & Code uses FRED/OECD INDCPIALLMINMEI; dissertation text mentions MoSPI cross-check \\\\
CPI Fuel and Light & Consumer fuel-light component & Cached MoSPI harmonised series \\\\
IIP & Activity control & RBI DBIE chain-linked IIP file \\\\
\\bottomrule
\\end{{longtable}}

## Transformations

**Logs.** Logs turn multiplicative growth into additive changes and make coefficients close to elasticities.

**Monthly log differences.** The code uses \\(100\\times\\Delta\\ln\\), so a value of 1 means roughly 1 percent monthly growth:

\\[
\\Delta \\ln y_t \\times 100 = 100(\\ln y_t - \\ln y_{{t-1}}).
\\]

When both the dependent variable and oil shock are multiplied by 100, the pass-through coefficient is still interpretable as percent-on-percent. For example, a CPT of 0.03 means a 10 percent oil increase is associated with about 0.3 percentage point cumulative monthly inflation in the dependent price index over the lag window.

**Positive and negative decomposition.**

\\[
\\Delta oil_t^+ = \\max(\\Delta oil_t,0), \\qquad
\\Delta oil_t^- = \\min(\\Delta oil_t,0).
\\]

The negative component is stored as a negative number. Therefore a positive coefficient on \\(\\Delta oil^-\\) means that when oil falls, the dependent price also falls.

**WPI chain linking.** The WPI code does not estimate an overlap ratio from the data. It divides old-base WPI values by official linking-factor chains to express them on a 2011-12 base.

{csv_summary_row("wpi/outputs/tables/table_02_chain_factors.csv")}

## Variable-to-Code Map

\\begin{{longtable}}{{p{{0.24\\textwidth}}p{{0.28\\textwidth}}p{{0.38\\textwidth}}}}
\\toprule
Dissertation variable & R object/column & Notes \\\\
\\midrule
Headline WPI inflation & \\texttt{{dln\\_dep}} in WPI headline data & Dependent variable in headline WPI ADL \\\\
WPI Fuel and Power inflation & \\texttt{{dln\\_dep}} in WPI fuel data & Same generic name, different dataset \\\\
Headline CPI inflation & \\texttt{{dlnCPI}} & CPI endpoint \\\\
CPI Fuel and Light inflation & \\texttt{{dlnFuel}} & Supporting short sample model \\\\
Retail petrol inflation & \\texttt{{dlnPetrol}} & Delhi PPAC petrol price \\\\
Rupee oil-price change & \\texttt{{dlnOil}} / \\texttt{{dln\\_oil}} & Brent times exchange rate, then log-differenced \\\\
Positive rupee-oil shocks & \\texttt{{dlnOil\\_pos\\_L0}} etc.; WPI uses \\texttt{{dln\\_oil\\_pos\\_L0}} etc. & L0 is current month \\\\
Negative rupee-oil shocks & \\texttt{{dlnOil\\_neg\\_L0}} etc.; WPI uses \\texttt{{dln\\_oil\\_neg\\_L0}} etc. & Stored as negative values \\\\
Brent decomposition & \\texttt{{dlnBrent\\_pos\\_Lk}}, \\texttt{{dlnBrent\\_neg\\_Lk}} & Used in retail petrol and robustness models \\\\
Exchange-rate controls & \\texttt{{dlnEXR}}, \\texttt{{dlnEXR\\_L1}}; WPI uses \\texttt{{dln\\_exr}}, \\texttt{{dln\\_exr\\_L1}} & Included in decomposition/fuel WPI models \\\\
Activity control & \\texttt{{dlnIIP}} & CPI/retail/fuel-light models \\\\
Petrol deregulation dummy & \\texttt{{D\\_petrol}} & From June 2010 \\\\
Diesel deregulation dummy & \\texttt{{D\\_diesel}} or WPI \\texttt{{d\\_reform}} & From October 2014 \\\\
COVID dummy & \\texttt{{D\\_covid}} or \\texttt{{d\\_covid}} & CPI: April 2020 only; WPI: April-September 2020 \\\\
Monthly dummies & \\texttt{{month}} factor or \\texttt{{mo\\_Jan}} through \\texttt{{mo\\_Nov}} & Seasonal controls \\\\
\\bottomrule
\\end{{longtable}}

# The ADL Model, Fully Explained

## General ADL(p, q)

An autoregressive distributed lag model says today's value of \\(y\\) depends on its own past and on current and lagged values of \\(x\\):

\\[
y_t = \\alpha + \\sum_{{i=1}}^p \\phi_i y_{{t-i}} + \\sum_{{j=0}}^q \\beta_j x_{{t-j}} + u_t.
\\]

Here \\(p\\) is the number of dependent-variable lags and \\(q\\) is the number of oil-shock lags.

## Asymmetric ADL Used Here

The main short-run model is:

\\[
\\Delta p_t =
\\alpha + \\sum_{{i=1}}^p \\phi_i \\Delta p_{{t-i}}
+ \\sum_{{j=0}}^q \\beta_j^+ \\Delta oil_{{t-j}}^+
+ \\sum_{{j=0}}^q \\beta_j^- \\Delta oil_{{t-j}}^-
+ \\gamma' Z_t + u_t.
\\]

\\(\\Delta p_t\\) is the inflation rate of the price index being studied. \\(Z_t\\) contains controls such as activity, policy dummies, exchange-rate terms, COVID dummies, and seasonal dummies depending on the model.

## Specific Lag Choices

WPI models use fixed lags: AR(12), oil lags 0-6, and month fixed effects. This is a modelling choice, not an AIC-selected lag length.

CPI headline models select the own-lag order \\(p\\) by AIC over 1-4. AIC picks \\(p=3\\), while BIC and HQC pick \\(p=1\\). The oil lag length \\(q=3\\) is theory-driven, not AIC-selected. This distinction matters in a viva.

{csv_summary_row("improved-v2/outputs/tables/table_05b_lag_selection.csv")}

## Long-Run Multiplier In An ADL

If the model is in levels, the long-run multiplier is:

\\[
LRM = \\frac{{\\sum_{{j=0}}^q \\beta_j}}{{1-\\sum_{{i=1}}^p \\phi_i}}.
\\]

But the dissertation's main models are in log differences. They report cumulative short-run pass-through over the lag window:

\\[
CPT = \\sum_{{j=0}}^q \\beta_j.
\\]

Do not call the main ADL CPT a permanent long-run elasticity. It is a cumulative short-run response over the selected lag window.

## Inference

A t-statistic tests one coefficient:

\\[
t = \\frac{{\\hat\\beta}}{{SE(\\hat\\beta)}}.
\\]

A Wald/F test tests a restriction involving one or more coefficients. For example, \\(H_0:CPT^+=0\\) tests whether the sum of all positive oil-shock coefficients is zero.

A p-value is the probability of seeing a test statistic at least this extreme if the null hypothesis were true. The decision rule used here is conventional: reject at 5 percent if \\(p<0.05\\); call it marginal at 10 percent if \\(0.05\\le p<0.10\\).

**Worked example.** In the WPI headline model, \\(CPT^+=0.0301\\) with p=0.024. That rejects \\(H_0:CPT^+=0\\) at 5 percent. Interpretation: a 10 percent positive rupee-oil shock is associated with about 0.301 percentage point cumulative increase in WPI monthly inflation over the lag window.

# NARDL, Fully Explained

NARDL is used as supplementary evidence because the main dissertation claim is short-run layered transmission, not a new long-run cointegration result.

The positive and negative partial sums in NARDL are:

\\[
x_t^+ = \\sum_{{s=1}}^t \\max(\\Delta x_s,0), \\qquad
x_t^- = \\sum_{{s=1}}^t \\min(\\Delta x_s,0).
\\]

A simplified NARDL error-correction form is:

\\[
\\Delta y_t =
\\alpha + \\rho y_{{t-1}} + \\theta^+ x_{{t-1}}^+
+ \\theta^- x_{{t-1}}^-
+ \\sum_i \\phi_i \\Delta y_{{t-i}}
+ \\sum_j \\left(\\pi_j^+ \\Delta x_{{t-j}}^+ + \\pi_j^- \\Delta x_{{t-j}}^-\\right)
+ u_t.
\\]

**Short-run asymmetry** tests whether the short-run positive and negative coefficients differ:

\\[
H_0: \\sum_j \\pi_j^+ = \\sum_j \\pi_j^-.
\\]

**Long-run asymmetry** tests whether long-run positive and negative multipliers differ:

\\[
H_0: -\\theta^+/\\rho = -\\theta^-/\\rho.
\\]

**Bounds testing.** The Pesaran-Shin-Smith bounds test checks whether the lagged level terms jointly matter. If the F-statistic is above the \\(I(1)\\) upper bound, reject no cointegration. If it is below the \\(I(0)\\) lower bound, fail to reject. If it is between the bounds, the result is inconclusive.

WPI NARDL summary:

{csv_summary_row("wpi/outputs/tables/table_07_nardl_summary.csv")}

Important caveat: the CPI improved-v2 pipeline removed earlier CPI NARDL specifications because the prior error-correction framing was not reliable. The dissertation's NARDL appendix should therefore be defended as WPI supplementary evidence, not as the main CPI claim.

# Every Test Decoded

\\begin{{longtable}}{{p{{0.18\\textwidth}}p{{0.25\\textwidth}}p{{0.25\\textwidth}}p{{0.22\\textwidth}}}}
\\toprule
Test & What it tests & Null and alternative & How to read it here \\\\
\\midrule
ADF & Unit root using an augmented Dickey-Fuller regression & H0: unit root. H1: stationary. & More negative than critical value means reject unit root. \\\\
Phillips-Perron & Unit root robust to serial correlation/heteroskedasticity & H0: unit root. H1: stationary. & Used as a second unit-root check. \\\\
KPSS & Stationarity from the opposite direction & H0: stationary. H1: unit root/non-stationary. & Large statistic rejects stationarity. KPSS over-rejects in some long/break-prone samples. \\\\
Zivot-Andrews & Unit root allowing one endogenous structural break & H0: unit root with break. H1: trend-stationary with break. & Used to identify possible break dates, not as a central claim. \\\\
Bai-Perron & Multiple structural breaks in mean/regression relationship & H0 varies by break count; algorithm chooses breaks by BIC. & Supports the idea of regime shifts, especially around WPI inflation. \\\\
Pesaran-Shin-Smith bounds & Long-run levels relationship in ARDL/ECM & H0: no levels relation. H1: cointegration. & Use I(0)/I(1) bounds, not only the HAC p-value. \\\\
Breusch-Godfrey LM & Serial correlation in residuals & H0: no serial correlation up to selected order. & Passing supports dynamic adequacy. \\\\
Breusch-Pagan & Heteroskedasticity & H0: constant variance. & Failure does not kill the model; HAC standard errors are used. \\\\
White/ARCH-LM & Conditional heteroskedasticity & H0: no ARCH effects. & Report-only in code; HAC handles inference risk. \\\\
Jarque-Bera & Normal residuals & H0: normal residuals. & Often fails in macro data; less damaging with large samples and HAC inference. \\\\
Ramsey RESET & Functional-form misspecification & H0: no omitted nonlinear fitted-value terms. & A failure is more serious because it suggests specification risk. \\\\
CUSUM/CUSUMSQ & Parameter stability & H0: stable parameters. & Passing supports stability. Code uses Rec-CUSUM and OLS-CUSUM. \\\\
Wald asymmetry & Equality of cumulative positive and negative pass-through & H0: CPT+ = CPT-. & Failure to reject means no reliable asymmetry. \\\\
Granger causality & Predictive direction & H0: lagged X does not predict Y beyond lagged Y. & Supports transmission ordering, but is not structural causality. \\\\
\\bottomrule
\\end{{longtable}}

Unit-root results to remember:

{csv_summary_row("wpi/outputs/tables/table_13_unit_root_battery.csv")}

{csv_summary_row("improved-v2/outputs/tables/table_03_unit_root_battery.csv")}

# Walking Through The Results Layer By Layer

## WPI Headline

Estimated model: WPI headline monthly inflation on 12 own lags, positive and negative rupee-oil shocks at lags 0-6, and month fixed effects.

Summary: sample {wpi_main['Sample_start']} to {wpi_main['Sample_end']}, N={wpi_main['N']}, adjusted R-squared {wpi_main['Adj_R2']}. CPT+={wpi_main['CPT_pos']} (p={wpi_main['CPTpos_p']}), CPT-={wpi_main['CPT_neg']} (p={wpi_main['CPTneg_p']}), asymmetry p={wpi_main['Asym_p']}.

Economic reading: headline WPI responds significantly to oil shocks, but the size is small. This is the first clear attenuation result: wholesale headline prices move, but much less than fuel-heavy prices.

{coefficient_longtable("wpi/outputs/tables/table_04b_headline_main_coefficients.csv", "Headline WPI ADL coefficients", "wpi_headline")}

## WPI Fuel And Power

Estimated model: WPI Fuel and Power inflation on 12 own lags, rupee-oil positive/negative shocks at lags 0-6, exchange-rate controls, diesel-reform and COVID dummies, and month fixed effects.

Summary: sample {wpi_fuel['Sample_start']} to {wpi_fuel['Sample_end']}, N={wpi_fuel['N']}, adjusted R-squared {wpi_fuel['Adj_R2']}. CPT+={wpi_fuel['CPT_pos']} (p={wpi_fuel['CPTpos_p']}), CPT-={wpi_fuel['CPT_neg']} (p={wpi_fuel['CPTneg_p']}), asymmetry p={wpi_fuel['Asym_p']}.

Economic reading: WPI Fuel and Power is much more sensitive to oil than headline WPI. The model passes BG and CUSUM diagnostics but fails HAC-RESET, so report it with a functional-form caveat.

{coefficient_longtable("wpi/outputs/tables/table_06b_fuel_power_coefficients.csv", "WPI Fuel and Power ADL coefficients", "wpi_fuel")}

## Retail Petrol

Estimated model: Delhi retail petrol inflation on own lags, positive and negative Brent shocks at lags 0-3, IIP, policy dummies, COVID dummy, and month dummies.

Summary: sample {ppac['Sample_start']} to {ppac['Sample_end']}, N={ppac['N']}, adjusted R-squared {ppac['Adj_R2']}. CPT+={ppac['CPT_pos']} (p={ppac['CPTpos_p']}), CPT-={ppac['CPT_neg']} (p={ppac['CPTneg_p']}), asymmetry p={ppac['Asym_p']}.

Economic reading: retail petrol is the strongest direct mechanism in the CPI-side pipeline. Positive Brent shocks pass through strongly. Asymmetry is only marginal at 10 percent, so do not overclaim it.

{coefficient_longtable("improved-v2/outputs/tables/table_22b_ppac_retail_fuel_coefficients.csv", "PPAC Delhi retail petrol coefficients", "ppac")}

## CPI Fuel And Light

There are two related estimates, and you must keep them separate.

Direct oil-to-Fuel-and-Light model: CPT+={fuel_direct['CPT_pos']} (p={fuel_direct['CPTpos_p']}), CPT-={fuel_direct['CPT_neg']} (p={fuel_direct['CPTneg_p']}), sample {fuel_direct['Sample_start']} to {fuel_direct['Sample_end']}, N={fuel_direct['N']}. This is supporting evidence only because the series is shorter than 20 years.

Bridge model from PPAC petrol to CPI Fuel and Light: CPT+={bridge['CPT_pos']} (p={bridge['CPTpos_p']}), CPT-={bridge['CPT_neg']} (p={bridge['CPTneg_p']}), N={bridge['N']}. This is the 0.178 number used in the attenuation story. It is not the same as direct rupee-oil pass-through.

{coefficient_longtable("improved-v2/outputs/tables/table_16b_fuel_light_coefficients.csv", "Direct oil to CPI Fuel and Light coefficients", "fuel_light")}

{coefficient_longtable("improved-v2/outputs/tables/table_27b_ppac_to_fuel_bridge_coefficients.csv", "PPAC petrol to CPI Fuel and Light bridge coefficients", "bridge")}

## Headline CPI

Estimated model: headline CPI inflation on AIC-selected own lags p=3, positive and negative rupee-oil shocks at lags 0-3, IIP, petrol/diesel deregulation dummies, COVID dummy, and month dummies.

Summary: N={cpi_m1['N']}, adjusted R-squared {cpi_m1['Adj_R2']}. CPT+={cpi_m1['CPT_pos']} (p={cpi_m1['CPTpos_p']}), CPT-={cpi_m1['CPT_neg']}, asymmetry p={cpi_m1['Asym_p']}.

Economic reading: the headline CPI response is positive but weak. The correct viva sentence is: "I find strong upstream and fuel-layer transmission, but headline CPI pass-through is small and not statistically significant at conventional 5 percent levels."

{coefficient_longtable("improved-v2/outputs/tables/table_06_M1_asym_inr.csv", "Headline CPI M1 coefficients", "cpi")}

## Integrated Attenuation

{csv_summary_row("improved-v2/outputs/tables/table_23_dilution_hypothesis.csv")}

Common-sample check:

{csv_summary_row("improved-v2/outputs/tables/table_23b_dilution_common_sample.csv")}

Formal attenuation test:

{csv_summary_row("improved-v2/outputs/tables/table_23c_attenuation_wald.csv")}

The common-sample result is the strongest defence of the attenuation claim because it avoids comparing a 20-year petrol/headline sample with a shorter Fuel and Light sample.

# Robustness And Pre/Post-2010 Split

## Why The Split Matters

Petrol prices were deregulated in June 2010 and diesel prices in October 2014. Under administered pricing, retail prices could be held back by subsidies, under-recoveries, or tax changes. After deregulation, prices adjust more frequently, so measured pass-through should rise.

The WPI split uses April 2010 as the practical breakpoint in the code, close to the June 2010 petrol deregulation event.

{csv_summary_row("wpi/outputs/tables/table_12_subsample_prepost2010.csv")}

Interpretation: WPI pass-through is much larger after 2010, especially for Fuel and Power. This is consistent with market-linked pricing, but it is not a clean causal estimate because many other things changed across decades.

## CPI Robustness

{csv_summary_row("improved-v2/outputs/tables/table_21_robustness_summary.csv")}

The CPI robustness checks mostly support the cautious conclusion: headline CPI pass-through is small, not robustly asymmetric, and weaker than the fuel-layer estimates.

# Limitations, Honestly

1. The current working tree is incomplete. The visible `models/cpi/run_all.R` and `models/wpi/run_all.R` are orchestrators, but the actual modules and output tables are deleted from the filesystem and only available from Git history. If asked, say the analysis was generated from a fuller pipeline and that the present directory snapshot is not directly runnable without restoring those tracked files.

2. The dissertation sometimes speaks as if the whole chain is one sequential causal system. The code actually estimates several related models: WPI headline, WPI Fuel and Power, retail petrol, CPI Fuel and Light, and headline CPI. These support a layered interpretation, but they are not one jointly estimated structural chain.

3. The 0.178 CPI Fuel and Light number is a PPAC-petrol-to-Fuel-and-Light bridge estimate, not the direct rupee-oil-to-Fuel-and-Light estimate. The direct estimate is 0.0608.

4. Headline CPI pass-through is weak. Do not claim strong CPI pass-through. The central result is attenuation, not a large endpoint effect.

5. Asymmetry is not robust. Retail petrol gives marginal evidence at 10 percent, but most Wald and bootstrap tests fail to reject symmetry.

6. WPI Fuel and Power has a RESET failure, which means possible functional-form misspecification. Report it with a caveat.

7. Some unit-root evidence is mixed. KPSS flags stationarity problems in places where ADF/PP suggest first differences are stationary. The guide's defensible line is that differencing plus HAC inference is conservative, and NARDL is supplementary.

8. The pre/post split is institutional evidence, not causal identification. It does not isolate deregulation from all other policy and macroeconomic changes.

9. CPI Fuel and Light is short, from 2011 onward. It is useful mechanism evidence, not a full 20-year mandatory model.

10. Newey-West fixes standard errors, not bad model design. If the model omits important variables, HAC cannot rescue the interpretation.

# Anticipated Viva Questions With Full Answers

1. **What is your dissertation about?**  
It studies how international oil-price shocks transmit through India's price system. The key point is not just whether oil affects inflation, but where the shock weakens. I find strong pass-through to retail petrol and WPI Fuel and Power, smaller but significant pass-through to headline WPI, and weak pass-through to headline CPI.

2. **Why use rupee oil price rather than Brent alone?**  
India pays for crude in dollars but consumers and domestic firms face rupee costs. A Brent increase and rupee depreciation reinforce each other, so Brent multiplied by INR/USD is the relevant domestic cost shock.

3. **What does asymmetric pass-through mean?**  
It means prices may respond differently to oil-price increases and decreases. For example, petrol may rise quickly when Brent rises but fall slowly when Brent falls.

4. **Did you find strong asymmetry?**  
No. The safest answer is that asymmetry is weak. Retail petrol shows marginal evidence at 10 percent, but most ADL Wald and bootstrap tests do not reject symmetry.

5. **Then why use asymmetric models?**  
Because the literature and the institutional setting make asymmetry plausible. Splitting positive and negative shocks lets the data test that possibility rather than imposing symmetry.

6. **What is attenuation?**  
Attenuation means the shock becomes smaller as it moves through layers. A large oil shock reaches retail petrol and fuel-heavy indices strongly, but only a small fraction reaches headline CPI.

7. **What is a unit root?**  
A unit root means shocks have persistent effects and the series does not naturally return to a fixed mean. In a random walk, today's level equals yesterday's level plus a shock.

8. **Why not regress CPI levels directly on oil levels?**  
Because non-stationary levels can create spurious regressions. The main models use log differences. Levels are used only in the supplementary bounds/NARDL framework.

9. **What is ADL?**  
ADL stands for autoregressive distributed lag. The dependent variable depends on its own lags and on current and lagged oil shocks.

10. **Why are lags included?**  
Price adjustment takes time. Retail fuel, wholesale prices, and CPI components do not all adjust in the same month as the oil shock.

11. **How did you choose lag lengths?**  
For CPI, the own lag order was selected by AIC over p=1 to 4, and AIC picked p=3. The oil lag q=3 is theory-driven. For WPI, the code uses AR(12) and oil lags 0-6 as fixed monthly dynamic choices.

12. **Why did BIC pick a shorter lag than AIC?**  
BIC penalises complexity more strongly. AIC is more willing to keep extra lags. I report this and treat the q=3 specification as theory-consistent rather than purely data-selected.

13. **What is cumulative pass-through?**  
It is the sum of the oil-shock coefficients over the lag window. It answers: over the included months, how much does the dependent inflation rate respond to an oil-price change?

14. **Interpret WPI headline CPT+ = 0.030.**  
A 10 percent positive rupee-oil shock is associated with about a 0.3 percentage point cumulative increase in WPI inflation over the lag window.

15. **Interpret CPI headline CPT+ = 0.021 with p=0.122.**  
The sign is positive, but it is not statistically significant at 5 or 10 percent. I would not claim strong headline CPI pass-through.

16. **Why use Newey-West standard errors?**  
Monthly macro residuals often have heteroskedasticity and serial correlation. Newey-West adjusts the standard errors so t-tests and Wald tests are less misleading.

17. **Does Newey-West change the coefficients?**  
No. It changes the estimated standard errors and therefore inference, not the OLS point estimates.

18. **What does the Breusch-Godfrey test do?**  
It tests whether residuals are serially correlated up to a chosen lag order. Passing it supports the adequacy of the lag structure.

19. **What does RESET test do?**  
It checks whether nonlinear functions of the fitted values add explanatory power. A failure suggests functional-form misspecification or omitted nonlinearities.

20. **Your WPI Fuel and Power RESET fails. Is that fatal?**  
It is a caveat, not a reason to discard the whole result. The pass-through magnitude is large and plausible, but I should describe the model as mechanism evidence with functional-form risk.

21. **What is the bounds test?**  
It tests whether lagged level terms jointly matter in an ARDL error-correction form. If the F-statistic exceeds the upper bound, there is evidence of a long-run relation.

22. **What is the error-correction coefficient?**  
It is the speed at which deviations from the long-run relation are corrected. It should be negative for a valid correction mechanism.

23. **Why not use VAR or VECM?**  
A VAR/VECM would model all variables jointly, but it needs a different identification strategy and more parameters. My dissertation's aim is a layered pass-through map, so single-equation ADL models are more transparent and easier to defend.

24. **Does Granger causality prove economic causality?**  
No. It shows predictive ordering: past oil changes help predict prices beyond their own lags. It supports the transmission story but does not prove structural causality.

25. **What would change your conclusion?**  
If headline CPI pass-through became large and significant across lag choices, or if the formal attenuation tests failed on common samples, the attenuation conclusion would weaken.

26. **What is the strongest result?**  
The strongest result is not asymmetry. It is attenuation: strong pass-through in retail petrol and fuel-sensitive layers, much weaker pass-through in headline CPI.

27. **What is the weakest part of the dissertation?**  
The layered chain is not estimated as one structural system, and some supporting series are short. I would be transparent about that.

28. **How should you answer if asked whether the AI-generated code is reliable?**  
I would say I verified the logic by reading the pipeline: data are transformed into log differences, oil shocks are split into positive and negative components, OLS is used with HAC inference, and diagnostics are reported. I would also acknowledge that the current folder snapshot needs the Git-tracked modules restored to rerun end to end.

29. **What is your one-sentence conclusion?**  
Oil shocks are not absent from Indian inflation; they are strong upstream but diluted before they reach headline CPI.

30. **What should policy take from this?**  
Headline CPI may understate upstream oil stress. RBI should monitor fuel-sensitive and wholesale layers alongside headline CPI, while recognising that monetary policy cannot directly control global oil prices.

\\appendix

# Annotated R Code

The current filesystem only contains thin `models/*/run_all.R` orchestrators. The annotated chunks below come from the Git-tracked pipeline modules exported from `HEAD`.

{code_block("wpi/R/02_build_data.R", 47, 92, "WPI chain linking")}

Plain-English annotation: the code takes each historical WPI base-year segment, keeps the dates belonging to that segment, and divides old-base index values by the official linking-factor chain needed to express the values on a 2011-12 base. It then binds the segments into one continuous monthly series.

{code_block("improved-v2/R/03_variable_builder.R", 9, 36, "CPI-side variable construction")}

Plain-English annotation: the code constructs rupee oil price, logs the main variables, creates monthly log differences multiplied by 100, and then splits oil changes into positive and negative components.

{code_block("wpi/R/03_models.R", 5, 43, "WPI ADL formula construction")}

Plain-English annotation: the WPI code builds three formulas: headline rupee-oil ADL, headline Brent-plus-exchange-rate ADL, and Fuel and Power ADL. The headline model has 12 own lags and 7 oil lags. The fuel model also includes exchange-rate, reform, COVID, and seasonal controls.

{code_block("improved-v2/R/06_models.R", 82, 117, "Headline CPI M1 model")}

Plain-English annotation: this is the recommended CPI headline model. It uses the AIC-selected own lags, positive and negative rupee-oil shocks from lag 0 to lag 3, IIP, petrol/diesel deregulation dummies, COVID dummy, and monthly seasonal dummies.

{code_block("wpi/R/01_helpers.R", 79, 99, "Cumulative pass-through and asymmetry tests")}

Plain-English annotation: `compute_cpt` sums the positive-shock coefficients, sums the negative-shock coefficients, tests each sum against zero, and then tests whether the two sums are equal.

{code_block("improved-v2/R/05b_cointegration.R", 1, 33, "Bounds-test logic")}

Plain-English annotation: this file estimates a conditional ECM for headline CPI and tests whether the lagged level terms are jointly zero. The decision is made using Pesaran-Shin-Smith bounds.

{code_block("improved-v2/R/09b_attenuation_test.R", 1, 18, "Common-sample attenuation problem")}

Plain-English annotation: this module fixes a real weakness: the main dilution table compares stages with different sample windows. It re-estimates stages on the common Fuel and Light sample and runs a stacked Wald test.

# Glossary

ADF: Augmented Dickey-Fuller test for a unit root.

ADL: Autoregressive distributed lag model; a regression with lags of the dependent variable and lags of explanatory variables.

ARCH: Autoregressive conditional heteroskedasticity; changing volatility over time.

Asymmetry: Different responses to positive and negative shocks.

Attenuation: Weakening of pass-through as a shock moves through layers.

Bai-Perron: A method for detecting multiple structural breaks.

Bounds test: Pesaran-Shin-Smith test for a long-run levels relationship in ARDL models.

CPI: Consumer Price Index, household-facing inflation measure.

CPT: Cumulative pass-through, the sum of oil-shock coefficients over the lag window.

CUSUM: A stability test based on cumulative residual behaviour.

ECT: Error-correction term; measures adjustment back toward a long-run relation.

Granger causality: Predictive causality based on lagged values, not proof of structural causality.

HAC: Heteroskedasticity-and-autocorrelation-consistent standard errors.

I(0): Stationary in levels.

I(1): Stationary after first differencing.

IIP: Index of Industrial Production, used as an activity control.

KPSS: Unit-root-related test with stationarity as the null.

Log difference: Approximate percentage change, \\(\\Delta\\ln y_t\\).

NARDL: Nonlinear ARDL; ARDL model with positive and negative partial sums.

Newey-West: HAC covariance estimator used for robust inference.

OLS: Ordinary least squares.

PP test: Phillips-Perron unit-root test.

PPAC: Petroleum Planning and Analysis Cell.

RESET: Ramsey specification test for functional-form problems.

Splicing: Connecting series with different base years into one comparable series.

Stationarity: Stable mean/variance/autocorrelation over time.

Unit root: A form of non-stationarity where shocks have persistent effects.

Wald test: Test of one or more linear restrictions on coefficients.

WPI: Wholesale Price Index, upstream/producer-side price measure.
"""
    OUT_MD.write_text(text, encoding="utf-8")
    print(f"Wrote {OUT_MD}")


if __name__ == "__main__":
    main()
