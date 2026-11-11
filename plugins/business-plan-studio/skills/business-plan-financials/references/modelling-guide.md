# Modelling guide: from the founder's words to a model

## Contents
- What each reader expects
- Mapping businesses to stream types
- Turning answers into inputs
- Questions per stream type
- Sanity review
- Scenario design
- Presenting results
- Common modelling mistakes

## What each reader expects

| Reader | Horizon and detail | Numbers they check first |
|---|---|---|
| Incubator | 12–24 months monthly | price vs cost, cash floor, realistic first-year sales |
| Bank | 24–36 months monthly, downside case | cash never below zero, debt service coverage, owner contribution, collateral |
| Investor | 36 months, yearly plus monthly first year | growth drivers, unit economics (LTV/CAC, payback), burn and runway, use of funds |
| Grant | budget by activity and period | eligible costs, co-funding, cost per beneficiary, sustainability after the grant |
| Internal | 12 months monthly | targets, budgets by owner, cash buffer |

## Mapping businesses to stream types

| Business | Stream type | Driver |
|---|---|---|
| Products, orders, meals, bottles, tickets | `units` | volume ramp × price |
| Software, memberships, boxes, maintenance plans | `subscription` | new customers, churn, monthly price |
| Agency or consultancy retainers | `retainer` | new clients, churn, monthly fee |
| Hourly or day-rate services | `hours` | capacity hours × utilisation × rate |
| Marketplaces and platforms | `gmv` | transaction value × take rate |
| Rooms, desks, slots, vehicles, equipment hire | `rental` | units available × occupancy × price |
| Contracts with known dates, grants paid as income, one-off projects | `schedule` | amount per month |

Hybrids get one stream per line of income. Grants and donations are usually better as `financing` entries of type grant (cash in), unless an accountant says to treat them as income.

## Turning answers into inputs

| The founder says | Input |
|---|---|
| "About 40 cakes a day, six days a week" | `units` volume 40 × 26 = 1040 a month |
| "We hope to double sales by the end of the year" | ask what drives it; as a ramp: growth of about 6% a month reaches roughly double in 12 months (`bizcalc.py growth --start 1 --end 2 --months 12` gives 5.95%) |
| "Busy in summer, dead in Ramadan" | `seasonality`, 12 multipliers averaging about 1 |
| "Cafés pay us monthly" | `collection_days`: 30 |
| "We buy flour for two months at a time" | `inventory_days`: 60 |
| "Ingredients are about a third of the price" | `cost_pct`: 33 (or `unit_cost` if known per unit) |
| "Apps take 25%" | `variable_pct`: 25 on the app stream |
| "We'll hire a second designer when we have 10 clients" | a `team` line starting in the month the forecast reaches 10 clients |
| "A loan of 500000 over 3 years at 20%, first 6 months free of principal" | `financing` loan, `term_months` 36, `grace_months` 6, `rate_pct` 20 |

## Questions per stream type

- **units:** How many do you sell today (or in the pilot)? What limits more sales: demand, production or delivery? Price per unit before tax? Direct cost per unit? Seasonality?
- **subscription and retainer:** How many paying customers now? New customers a month and from which channel? What share cancel each month? Monthly price and plan mix? Cost to serve one customer?
- **hours:** Productive hours per person per month? Share of hours billed today? Rate per hour? Direct cost per billed hour?
- **gmv:** Transactions a month and average value? Take rate and who pays it? Payment and support costs per transaction?
- **rental:** Units available? Occupancy now and the path to target? Price per unit per period? Cost per occupied unit?
- **schedule:** Dates and amounts of signed or expected contracts; probability (label To confirm if not signed).

## Sanity review

| Check | What to look for | Ask the founder |
|---|---|---|
| Growth | sustained growth above about 15% a month, or a curve with no cap | Which channel, budget or capacity produces this growth? |
| Capacity | volume above what people or equipment can deliver | What do you add, and when, to deliver this? |
| Margins | gross margin far from the founder's experience | Which cost is missing? |
| Payroll | team plan and model payroll differ | Who is missing from the model, or from the plan? |
| Cash timing | everyone pays on day one; stock bought on the day of sale | How long do customers really take to pay? |
| Founder pay | founders work for free in every year | When do you start paying yourselves, and how much? |
| Tax | none at all | Add a placeholder and a question for the accountant |

## Scenario design

- **Base:** the founder's honest expectation, built from drivers.
- **Downside:** what a careful lender would assume: lower volume (20–30%), slower growth, higher costs, slower payments. Ask the founder what would really go wrong.
- **Upside (optional, investors):** what happens if the main channel performs better; never the headline.
For each scenario, report the cash low point, funding need and break-even month, and agree triggers and responses ("if orders are 20% below plan for two months, we delay the second hire").

## Presenting results

Lead with the decision numbers in one short paragraph:

> In the base case cash is lowest at 155119 EGP in November 2027, EBITDA turns positive from July 2027, and with the 450000 EGP loan and 170000 EGP of owners' money the plan needs no further funding. In the downside case cash falls to −181779 EGP in May 2028, so we will open an overdraft line before launch.

Then: yearly table (revenue, gross margin, EBITDA, net profit, cash at end) · the three assumptions that move results most (from sensitivity) · scenario table · monthly tables in an appendix · assumptions register. Banks: add the loan schedule and debt service coverage. Investors: add unit economics and runway after the round. Grants: present the budget by activity.

## Common modelling mistakes

- Starting from a revenue target instead of drivers.
- Leaving out founder pay, employer charges, payment fees, delivery, returns, maintenance, insurance, accounting or software.
- Treating loans and equity as income, or loan principal as an expense.
- Treating the purchase of equipment as a monthly expense instead of capital spending.
- Ignoring the gap between profit and cash (payment terms, stock).
- Showing only one scenario.
- Mixing prices with and without VAT.
- Rounding in every cell instead of at the end.
