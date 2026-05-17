"""Part 5: variables. Log differences, shock splits, scaling, construction."""


def build(h):
    add_para = h['add_para']
    add_para_math = h['add_para_math']
    h1 = h['h1']; h2 = h['h2']; h3 = h['h3']
    bullets = h['bullets']
    page_break = h['page_break']
    add_callout = h['add_callout']
    add_equation = h['add_equation']
    add_code_block = h['add_code_block']
    mr = h['mr']; msub = h['msub']; msup = h['msup']; mfenced = h['mfenced']

    h1("Part 5. Variables: log differences, shocks, and the rupee oil price")

    h2("5.1 Why we use log differences and not raw levels")
    add_para(
        "Prices grow roughly exponentially over time. If we regress the level "
        "of CPI on the level of Brent, we get a misleading ‘t-statistic’ "
        "because both variables trend together, even when no real "
        "relationship exists. This is the classic spurious regression "
        "problem from Granger and Newbold (1974). To avoid it, we difference "
        "the logs."
    )
    add_para(
        "Logarithms turn a proportional change into a level change. If a "
        "price goes up by one per cent, the log goes up by about 0.01. "
        "Taking the difference of the log is therefore a clean way to "
        "measure monthly growth in per cent terms."
    )

    h2("5.2 The log-difference formula")
    eq_5_1 = (mr('Δ') + msub(mr('x'), mr('t')) + mr(' = 100 × ') +
              mfenced(mr('ln') + mfenced(msub(mr('x'), mr('t'))) + mr(' − ln') +
                      mfenced(msub(mr('x'), mr('t−1')))))
    add_equation(eq_5_1, label="(5.1)")
    add_para_math(
        "Here x_{t} is the value of a series in month t and x_{t−1} is its "
        "value the previous month. The factor of 100 turns the number into "
        "a percentage. So Δx_{t} is the percentage growth of x from month "
        "t−1 to month t."
    )
    add_callout(
        "Intuition",
        "If Brent goes from 100 dollars in one month to 101 dollars the next, "
        "then Δ(Brent)_{t} is approximately 100 × (ln 101 − ln 100) ≈ "
        "0.995, very close to 1. We read this as about a one per cent rise."
    )

    h2("5.3 Splitting shocks into positive and negative parts")
    add_para_math(
        "For every shock variable we build two ‘twins’: one that is zero "
        "whenever the shock is negative, and one that is zero whenever the "
        "shock is positive. Formally, Δx^{+}_{t} = max(Δx_{t}, 0) and "
        "Δx^{−}_{t} = min(Δx_{t}, 0). The first is non-negative. The "
        "second is non-positive. Added together they reconstruct the "
        "original shock."
    )
    add_para_math(
        "Why do this split? Because an oil-price rise and an oil-price fall "
        "may pass through at different speeds. Retailers often raise fuel "
        "prices quickly and cut them slowly, a pattern the pass-through "
        "literature calls ‘rockets and feathers’. The split lets the data "
        "test whether CPT^{+} and CPT^{−} are equal without forcing them "
        "to be."
    )

    h2("5.4 Cumulative pass-through, CPT+ and CPT−")
    add_para_math(
        "In the ADL model we put several lags of Δx^{+}_{t} and several "
        "lags of Δx^{−}_{t} on the right-hand side. Each lag has its own "
        "coefficient β^{+}_{0}, β^{+}_{1}, … and β^{−}_{0}, β^{−}_{1}, …. "
        "The cumulative pass-through for positive shocks is simply the sum "
        "of those β^{+} coefficients over the lag window. CPT^{+} = "
        "Σ_{j=0}^{q} β^{+}_{j}. Likewise CPT^{−} = Σ_{j=0}^{q} β^{−}_{j}."
    )
    add_para_math(
        "CPT^{+} = 0.3 means: a one per cent positive oil shock this month "
        "is associated with, in total across this month and the following q "
        "months, about a 0.3 per cent change in the dependent price index. "
        "CPT^{−} is the twin number for negative shocks."
    )
    add_callout(
        "Careful",
        "Since Δx^{−} is non-positive by construction, CPT^{−} times a "
        "negative shock value produces a negative price response on average. "
        "Do not read CPT^{−} as if it were a separate positive shock."
    )

    h2("5.5 Why we multiply the log difference by 100")
    add_para(
        "The factor of 100 is cosmetic. It simply turns log differences into "
        "percentages so that every coefficient reads as ‘percentage response "
        "per one per cent shock’. Without the 100, the coefficients would be "
        "the same story told in decimals (0.003 instead of 0.30)."
    )

    h2("5.6 Rupee oil price step by step")
    add_para("We construct the rupee oil price in two steps:")
    add_code_block(
        "# Step 1: align dates and pick monthly series\n"
        "brent_usd       <- load_world_bank_pink_sheet()\n"
        "inr_per_usd     <- load_fred_EXINUS()\n"
        "\n"
        "# Step 2: multiply them at each date to get rupee oil\n"
        "oil_inr[t]      <- brent_usd[t] * inr_per_usd[t]\n"
        "\n"
        "# Step 3: make it a monthly change\n"
        "dln_oil_inr[t]  <- 100 * ( log(oil_inr[t]) - log(oil_inr[t-1]) )\n"
        "\n"
        "# Step 4: split into positive and negative shock\n"
        "dln_oil_inr_pos[t] <- max(dln_oil_inr[t], 0)\n"
        "dln_oil_inr_neg[t] <- min(dln_oil_inr[t], 0)\n"
    )
    add_para(
        "The same step-by-step logic applies to Brent alone (for the retail "
        "petrol equation) and to PPAC petrol (for the CPI Fuel and Light "
        "bridge equation). The only difference is which input series plays "
        "the role of ‘x’."
    )

    h2("5.7 Controls you will see in the equations")
    bullets([
        "ΔIIP_{t}: the monthly growth of the Index of Industrial Production. "
        "A demand-side control for the retail petrol and headline CPI equations.",
        "D_petrol: a dummy variable that is 0 before June 2010 and 1 after "
        "that, to allow the intercept to shift after petrol deregulation.",
        "D_diesel: a dummy variable that is 0 before October 2014 and 1 after, "
        "to mark diesel deregulation.",
        "D_covid: a dummy that flags the unusual months during COVID "
        "(April-September 2020 in the WPI models; April 2020 in the CPI models).",
        "μ_{m}: eleven monthly seasonal dummies (one month is the reference), "
        "to soak up residual seasonality after month-on-month differencing.",
    ])

    h2("5.8 Why the shock variable differs across layers")
    add_para(
        "We use the rupee oil price as the shock for WPI, WPI Fuel and "
        "Power, and headline CPI, because Indian producers and the economy "
        "as a whole care about the rupee cost of imported crude, which "
        "bundles Brent and the exchange rate."
    )
    add_para(
        "For retail petrol we use Brent alone, because retail petrol prices "
        "are pegged (under market-linked pricing) to international product "
        "prices that are very close to the dollar benchmark. Tax and pricing "
        "rules absorb much of the exchange-rate component separately."
    )
    add_para(
        "For CPI Fuel and Light we use PPAC retail petrol as the shock, "
        "because the question here is specifically how retail fuel movements "
        "enter the fuel-sensitive consumer basket. Using oil directly would "
        "mix the Brent-to-petrol stage and the petrol-to-CPI-Fuel-and-Light "
        "stage."
    )

    page_break()
