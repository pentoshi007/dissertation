"""Part 2: background, institutional setting, and intuition."""


def build(h):
    add_para = h['add_para']
    add_para_math = h['add_para_math']
    h1 = h['h1']; h2 = h['h2']; h3 = h['h3']
    bullets = h['bullets']
    page_break = h['page_break']
    add_callout = h['add_callout']
    add_table = h['add_table']

    h1("Part 2. Background: India, oil, WPI, and CPI")

    h2("2.1 India and imported crude oil")
    add_para(
        "India produces only a small share of the crude oil it consumes. Most "
        "of the crude used in Indian refineries is imported. The import bill "
        "is paid in US dollars because crude oil trades worldwide in dollars "
        "per barrel. That is why the rupee-dollar exchange rate is part of "
        "the story and not just a background variable."
    )
    add_para_math(
        "When we talk about an ‘oil shock’ for India, we mean the movement in "
        "the rupee price of oil, oil^{INR}_{t} = Brent^{USD}_{t} × INR_{t}/USD_{t}. "
        "If Brent rises or the rupee depreciates, this rupee oil price rises, "
        "and refiners and distributors face higher costs in rupees."
    )

    h2("2.2 Why the dollar and the exchange rate matter")
    bullets([
        "A 10 per cent rise in Brent does not always lead to a 10 per cent "
        "rise in the rupee oil price. If the rupee appreciates at the same "
        "time, the rupee oil price rises by less than 10 per cent.",
        "A depreciation of the rupee, even without any Brent move, pushes up "
        "the rupee oil price.",
        "Studying the rupee oil price captures both channels at once. That "
        "is why our main WPI and headline CPI equations use the rupee oil "
        "shock as the explanatory variable.",
    ])

    h2("2.3 The difference between WPI and CPI")
    add_para(
        "Wholesale Price Index, WPI, measures prices at the wholesale or "
        "producer level. It is published by the Office of the Economic "
        "Adviser, which sits inside the Department for Promotion of Industry "
        "and Internal Trade, Ministry of Commerce and Industry. WPI has a "
        "fairly large share of mineral oils, fuel and power, and "
        "oil-intensive manufactured goods, which is why it is sensitive to "
        "oil shocks."
    )
    add_para(
        "Consumer Price Index, CPI, measures prices at the household level. "
        "It is published by the Ministry of Statistics and Programme "
        "Implementation. The CPI basket is dominated by food, housing, "
        "services (like health and education), transport, and clothing. "
        "Fuel and Light is only one of several groups inside the CPI, so a "
        "pure fuel shock gets averaged down when you sum to the headline CPI."
    )

    add_table(
        headers=["Feature", "WPI", "CPI"],
        rows=[
            ["Level of the economy measured", "Wholesale / producer", "Retail / household"],
            ["Publisher", "Office of the Economic Adviser, DPIIT, MoCI",
             "Ministry of Statistics and Programme Implementation (MoSPI)"],
            ["Base year used here", "2011-12 = 100 (chained)",
             "Processed series; official base periodically revised"],
            ["Fuel and oil-intensive weight", "High", "Low (Fuel and Light is a sub-group)"],
            ["Policy role", "Useful for producer-side cost pressure",
             "Main inflation target of the Reserve Bank of India"],
        ],
        caption="Table 2.1. WPI and CPI at a glance.",
        col_widths=[1.8, 2.3, 2.3],
        note="Both indices are published monthly. The study chains successive "
             "WPI base years so a long monthly series is available from 1983 onward."
    )

    h2("2.4 How fuel is priced in India, in short")
    add_para(
        "Before 2010, retail petrol prices in India were administered. The "
        "government held them fixed for long stretches, and oil marketing "
        "companies (Indian Oil, Bharat Petroleum, Hindustan Petroleum) "
        "absorbed the difference through under-recoveries and fiscal "
        "support. So when Brent moved, retail petrol sometimes did not move "
        "at all for months."
    )
    add_para(
        "In June 2010 petrol pricing was deregulated. The oil marketing "
        "companies were allowed to revise petrol prices more freely in line "
        "with international product prices. Diesel was deregulated in "
        "October 2014. The move to daily price revisions began in 2017. "
        "Under these rules, a Brent move now reaches retail petrol quickly, "
        "so the econometric pass-through we can measure from the data is "
        "bigger in the post-2010 sample than in the pre-2010 sample."
    )
    add_callout(
        "Careful wording",
        "We do not claim that deregulation caused the bigger post-2010 "
        "pass-through. Other things also changed: new CPI series in 2011, "
        "flexible inflation targeting in 2016, GST in 2017, tax-rate moves, "
        "and so on. The pre/post-2010 split is institutional evidence, not a "
        "clean experiment."
    )

    h2("2.5 Why a layered reading beats a single elasticity")
    add_para(
        "Most earlier India papers pick one price index, usually headline "
        "WPI or headline CPI, and report a single number for how much oil "
        "passes through. That is fine, but it misses where the shock weakens. "
        "If you only look at headline CPI, you may get a small coefficient "
        "and think oil is unimportant. But retail petrol may be moving by a "
        "lot in the same data. Our layered design keeps all those layers in "
        "one frame so the reader can see the attenuation pattern."
    )

    h2("2.6 The literature that anchors this work")
    bullets([
        "Mandal, Bhattacharyya and Bhoi (2012) studied oil price pass-through "
        "in India and found partial, asymmetric, and policy-sensitive "
        "transmission, especially through administered fuel prices.",
        "Bhanumurthy, Das and Bose (2012) analysed oil shock pass-through and "
        "its policy implications in India in an NIPFP working paper.",
        "Pradeep (2022) looked at diesel price reforms and asymmetric oil "
        "pass-through in India, using disaggregated data.",
        "Newey and West (1987) gave us the HAC standard errors we use for "
        "inference. The formula they introduced corrects standard errors for "
        "autocorrelation and heteroskedasticity.",
        "Bai and Perron (2003) gave the structural-break test we use as a "
        "background check for regime shifts.",
        "Kwiatkowski, Phillips, Schmidt and Shin (1992) gave the KPSS "
        "stationarity test we use alongside ADF and Phillips-Perron.",
    ])

    page_break()
