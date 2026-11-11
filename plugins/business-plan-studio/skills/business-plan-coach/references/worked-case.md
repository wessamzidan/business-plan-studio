# Worked case: Nour Bites (fictional), from first answer to bank-ready plan

A complete fictional example that shows how a plan improves through coaching. Use it when a founder asks "what does a good plan look like?", or quote one section as an example. All names and numbers are invented; the financial figures were produced with `scripts/fin_model.py` and the calculators, so they agree with each other.

## Contents
- The business and the reader
- How the coaching went (four moments)
- Key sections as finally written
- The financial plan: version 1 versus final
- Checks and how they were resolved
- What this case teaches

## The business and the reader

Nour Bites (fictional) bakes healthy packed snacks (date bars, oat bites) in Cairo and sells them to independent cafés and through an online shop. Business type: manufacturing with an ecommerce-d2c line (hybrid). Stage: building, with a pilot. Reader: a bank, for an equipment and working-capital loan. Currency: EGP. Founders: two, full-time.

## How the coaching went (four moments)

1. **Customer.** The founder first wrote "our customers are health-conscious people". The coach asked who pays first and how they buy. After two follow-ups the priority segment became "independent cafés in Maadi, Zamalek and New Cairo with 20–60 seats that already sell packaged snacks", backed by 12 café owners who signed letters of intent to stock the bars for three months [Verified: signed letters].
2. **Pricing.** The founder planned to match a competitor at 20 EGP a pack. The coach ran `bizcalc.py unit-margin` (unit cost 9 EGP) and a shelf check: cafés resell at about 35 EGP, so a 22 EGP wholesale price leaves the café a fair margin and gives Nour Bites 13 EGP per pack (59.1%). The price moved to 22 EGP [Planned], with the cost build-up labelled Estimate.
3. **Numbers check.** Version 1 of the model (below) showed cash falling to −424775 EGP while the founder planned to ask for 300000 EGP: checks C06 and C07 were blocking. The coach showed three levers; the founder chose to start with two bakers, delay the packaging machine to September, ask for a larger loan and add family equity.
4. **Downside.** A bank asks "what if sales are slower?". The downside case (20% less volume, slower growth, 5% higher costs) runs out of cash in 2028. The founder wrote triggers and responses into the risk register instead of hiding it.

## Key sections as finally written

**offer.value_proposition:** "For independent cafés in Cairo whose customers ask for healthier snacks, Nour Bites supplies packed date bars and oat bites delivered twice a week, with no added sugar and a 45-day shelf life, unlike imported bars that cost cafés twice as much. 12 cafés signed letters of intent after a two-week tasting [Verified]."

**market.size (method summary):** "Cafés we can reach with one van: about 400 in three districts [To confirm: maps count, March 2027]. 15% conversion from our pilot visits gives 60 cafés, each buying about 330 packs a month (the average in our two-week tasting, about 13 a day): 60 × 330 × 22 × 12 = 5227200 EGP a year (SOM, cafés only) [Estimate]. The 12 signed cafés alone account for about 4000 packs a month."

**model.unit_economics:** "Café pack: price 22, unit cost 9, contribution 13 EGP (59.1%). Online bundle: price 45, unit cost 14, delivery and payment fees 15% (6.75), contribution 24.25 EGP (53.9%) [Estimate: recipe costing and courier quote]."

**financials.break_even:** "Monthly fixed costs including founder pay and employer charges are about 79156 EGP at launch, so we break even at about 6089 café packs a month (234 a day over 26 days) [Estimate]. The model reaches EBITDA break-even in July 2027."

**risks.register (top line):** "Café orders 20% below plan for two months (likelihood 2, impact 3) → trigger: delay the third baker and halve online marketing; draw no new debt."

## The financial plan: version 1 versus final

| | Version 1 (first draft) | Final plan |
|---|---|---|
| Café packs, first month | 3000 (a guess) | 4000 (12 signed cafés × about 330 packs) |
| Bakers at launch | 3 | 2, third from May 2027 |
| Founder pay, year 1 | 10000 each | 7000 each, rising in year 2 |
| Packaging machine | June 2027 | September 2027 |
| Money in | loan 300000 | loan 450000 + family equity 170000 |
| Cash low point | −424775 (January 2028) | 155119 (November 2027) |
| Months below zero | 19 | 0 |
| Funding need (buffer 150000) | 574775 | 0 |

Final plan results (base case, EGP):

| Period | Revenue | Gross margin | EBITDA | Net profit | Cash at end |
|---|---|---|---|---|---|
| Year 1 (2027) | 1826143 | 60.9% | 40190 | −110410 | 157204 |
| Year 2 (2028) | 3525443 | 65.2% | 960766 | 795835 | 796346 |

Loan: 450000 EGP at 22% over 36 months with 6 months' grace: interest-only 8250 a month, then 19635 a month; total interest 188548 EGP (`bizcalc.py loan`). Year-2 debt service coverage: EBITDA 960766 ÷ debt service 235619 = 4.1. Downside case: year-1 revenue 1378159 EGP; cash low point −181779 in May 2028; the triggers above keep cash positive, and the founders will open a 200000 EGP overdraft line before launch [Planned].

## Checks and how they were resolved

| Check | Version 1 | Final | What changed |
|---|---|---|---|
| C01 price vs cost | pass | pass | — |
| C03 SOM vs year-1 revenue | — | pass: café revenue in year 1 (1484555) is 28% of the café SOM (5227200) | SOM rebuilt bottom-up from reachable cafés and tasting volumes |
| C06 cash floor | blocking | pass | phasing, smaller team at launch, more funding |
| C07 ask vs need | blocking | pass | the 620000 asked covers the 510879 the model needs before any financing (cash low point plus the 150000 buffer) |
| C08 use of funds | — | pass | oven and mixer 250000, packaging machine 120000, working capital and buffer 250000 = 620000 = loan + equity |
| C12 labels | advisory | pass | every number labelled |

## What this case teaches

1. A specific, evidenced customer (signed letters) changes the numbers, not just the words.
2. Price is set from cost and the reseller's margin, then checked against the shelf.
3. The funding ask comes from the cash low point plus a buffer, never from a round number.
4. Profit and cash are different: break-even in July, but the cash low point is in November because of the machine purchase and 30-day café payments.
5. A downside case with triggers builds a bank's trust more than an optimistic single case.
