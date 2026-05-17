"""Part 4: data sources with full names, meanings, and roles."""


def build(h):
    add_para = h['add_para']
    add_para_math = h['add_para_math']
    h1 = h['h1']; h2 = h['h2']; h3 = h['h3']
    bullets = h['bullets']
    page_break = h['page_break']
    add_callout = h['add_callout']
    add_table = h['add_table']

    h1("Part 4. Data: what is it, where does it come from, and why")

    h2("4.1 All series at monthly frequency")
    add_para(
        "Every series we use is monthly. Different series start in different "
        "years because the underlying publications began at different dates. "
        "This is why the sample windows are not the same across layers."
    )

    h2("4.2 Crude oil price: Brent, from the World Bank Pink Sheet")
    add_para(
        "‘Brent crude’ is a benchmark crude oil produced in the North Sea. "
        "‘Brent price’ is the price of a barrel of Brent crude in US dollars. "
        "World traders use Brent as a standard, so it is the global oil price "
        "most economists use for applied work on India."
    )
    add_para(
        "We take the monthly Brent price from the World Bank Commodity Price "
        "Data, the publication commonly called the Pink Sheet. It is a "
        "monthly bulletin published by the World Bank with prices of major "
        "energy, metals, and agricultural commodities. The WPI model also "
        "cross-checks against FRED series POILBREUSDM. FRED stands for "
        "Federal Reserve Economic Data, maintained by the Federal Reserve "
        "Bank of St. Louis."
    )

    h2("4.3 Exchange rate: INR per USD, from FRED")
    add_para(
        "INR per USD is how many rupees you pay for one dollar. It goes up "
        "when the rupee depreciates. We take the monthly average INR/USD rate "
        "from the FRED series EXINUS (the CPI pipeline uses EXINUS; the WPI "
        "pipeline uses the updated EXINUS_latest file). FRED pulls this from "
        "the Federal Reserve's H.10 statistical release."
    )

    h2("4.4 Rupee oil price: constructed, not downloaded")
    add_para_math(
        "The rupee oil price, oil^{INR}_{t}, is built as Brent in dollars "
        "multiplied by the INR/USD rate: oil^{INR}_{t} = Brent^{USD}_{t} × "
        "INR_{t}/USD_{t}. This is the main shock variable for the WPI and "
        "headline CPI equations."
    )

    h2("4.5 Wholesale Price Index (WPI): from the Office of the Economic Adviser")
    add_para(
        "The Office of the Economic Adviser (OEA) inside the Department for "
        "Promotion of Industry and Internal Trade (DPIIT), Ministry of "
        "Commerce and Industry, Government of India, publishes the WPI every "
        "month. We use two WPI series: headline WPI (the whole index) and "
        "WPI Fuel and Power (the sub-index that tracks fuel, power, and "
        "mineral oil items in the wholesale basket)."
    )
    add_para(
        "The OEA has published WPI under several base years, 1981-82, "
        "1993-94, 2004-05, and now 2011-12 = 100. To get a continuous "
        "monthly series from May 1983 to March 2026, we chain the older "
        "vintages using the OEA's official chain factors and rebase "
        "everything to 2011-12 = 100. The pipeline verifies splices at the "
        "overlap dates so that we do not introduce visible level breaks."
    )

    h2("4.6 PPAC Delhi retail petrol: from the Petroleum Planning and Analysis Cell")
    add_para(
        "PPAC, the Petroleum Planning and Analysis Cell, is a unit under "
        "the Ministry of Petroleum and Natural Gas. It publishes a ready "
        "reckoner with monthly retail prices of petrol and diesel in major "
        "Indian cities. We use the Delhi retail petrol price from August "
        "2004 to December 2024 as our direct retail-fuel layer. We choose "
        "Delhi because it has one of the longest, most consistent monthly "
        "series."
    )

    h2("4.7 Consumer Price Index (CPI): from MoSPI")
    add_para(
        "MoSPI, the Ministry of Statistics and Programme Implementation, "
        "publishes the all-India CPI every month. We use two CPI series: "
        "headline CPI (the whole index) and CPI Fuel and Light (the sub-group "
        "that collects household energy items like LPG, kerosene, and "
        "electricity-related charges)."
    )
    add_para(
        "In practice, headline CPI is loaded from a processed file inside "
        "the CPI pipeline (the FRED OECD series INDCPIALLMINMEI is the "
        "headline source; MoSPI is the authority). CPI Fuel and Light is the "
        "processed MoSPI all-India component series used starting in May "
        "2011, when the current harmonised series is continuously available."
    )

    h2("4.8 Index of Industrial Production (IIP): MoSPI")
    add_para(
        "IIP is a monthly index of manufacturing and industrial output "
        "published by MoSPI. We use its monthly growth rate as a control for "
        "domestic activity or demand in the retail-petrol and headline CPI "
        "equations. The idea is that some inflation movement is caused by "
        "demand conditions, not by oil, and we do not want the oil "
        "coefficient to pick up that other story."
    )

    h2("4.9 Summary table of series and their roles")
    add_table(
        headers=["Series", "Source (full name)", "Transformation",
                 "Active sample", "Role in the paper"],
        rows=[
            ["Brent crude price", "World Bank Commodity Price Data (Pink Sheet)",
             "Monthly log difference", "Matched to layer", "Global oil shock"],
            ["INR/USD exchange rate",
             "Federal Reserve Economic Data (FRED EXINUS / EXINUS_latest)",
             "Monthly log difference", "Matched to layer", "Exchange-rate component"],
            ["Rupee oil price", "Brent multiplied by INR/USD",
             "Monthly log difference", "Matched to layer", "Domestic oil shock"],
            ["Headline WPI", "Office of the Economic Adviser (DPIIT, MoCI), 2011-12 = 100",
             "Monthly log difference", "1983-05 to 2026-03", "Wholesale endpoint"],
            ["WPI Fuel and Power",
             "Office of the Economic Adviser (DPIIT, MoCI), 2011-12 = 100",
             "Monthly log difference", "1995-05 to 2026-03", "Wholesale fuel layer"],
            ["PPAC Delhi retail petrol",
             "Petroleum Planning and Analysis Cell (MoPNG) ready reckoner",
             "Monthly log difference", "2004-08 to 2024-12", "Retail fuel layer"],
            ["CPI Fuel and Light",
             "Ministry of Statistics and Programme Implementation (MoSPI)",
             "Monthly log difference", "2011-05 to 2024-12", "Consumer fuel bridge"],
            ["Headline CPI",
             "MoSPI, via processed CPI source (OECD INDCPIALLMINMEI / FRED)",
             "Monthly log difference", "2004-08 to 2024-12", "Consumer endpoint"],
            ["Index of Industrial Production",
             "MoSPI", "Monthly log difference", "Matched to layer", "Activity control"],
        ],
        caption="Table 4.1. Every series used in the paper, with its full "
                "source name, transformation, active sample, and role.",
        col_widths=[1.3, 1.7, 1.1, 1.1, 1.1],
        font_size=9,
        note="Samples differ across layers because the official series became "
             "available in different years. We deliberately did not force a "
             "common sample; instead we run a common-sample CPI-chain check "
             "separately (see Part 9)."
    )

    h2("4.10 Why samples are different, and why that is fine")
    bullets([
        "Headline WPI has the longest window (1983 onward) because the OEA "
        "series goes back that far. We use it fully, since more data gives "
        "better inference.",
        "WPI Fuel and Power starts in 1995 because that is when the OEA "
        "component series is continuously available in a chainable form.",
        "PPAC retail petrol starts in August 2004 because that is the "
        "earliest consistent monthly series from PPAC.",
        "Headline CPI uses the same post-2004 window so the retail petrol "
        "and headline CPI are on the same 20-year consumer-side window.",
        "CPI Fuel and Light starts in May 2011 because that is when the "
        "current harmonised MoSPI series begins. We treat it as bridge "
        "evidence for this reason, not as the main headline model.",
    ])

    add_callout(
        "Viva tip",
        "If a teacher asks why the sample windows differ, answer: ‘Each "
        "series is used from the earliest date its official publisher makes "
        "it available. Headline WPI goes back to 1983. CPI Fuel and Light "
        "starts in 2011, which is why we treat it as bridge evidence and not "
        "as our main consumer-side claim.’"
    )

    page_break()
