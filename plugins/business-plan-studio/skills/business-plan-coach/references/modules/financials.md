# Module 10: Financial plan (`financials`)

This module must turn the plan's words into numbers that agree with each other: assumptions, sales forecast, costs, cash flow, break-even, scenarios and the funding need. Every figure is calculated by a script and every input carries a claim label.

## Contents
- Order and depth
- How to collect inputs
- Sections: financials.assumptions · financials.forecast · financials.costs · financials.cash_flow · financials.break_even · financials.scenarios · financials.funding
- Module summary
- Hand-offs

## Order and depth

After the model, go-to-market, operations and team modules, because their answers become the inputs. Bank plans need 24–36 months and a repayment view; investor plans 36 months and unit economics; incubators 12–24 months; grant plans a budget by activity. Quick draft: a 12-month model with labelled estimates.

## How to collect inputs

Ask one input at a time, always with unit, period and tax treatment ("monthly, in KES, before VAT?"). Reuse answers already given. Order:
1. Revenue drivers per stream (volume or customers, price, growth, start month, seasonality).
2. Direct costs per unit or as % of revenue; variable fees (platform, payment, delivery).
3. Fixed monthly costs by category.
4. Team: roles, counts, salaries, start months; employer on-costs from the country profile (To confirm).
5. Equipment and other capital spending, with month and useful life.
6. Money in: opening cash, owner equity, loans, grants.
7. Timing: customer payment days, supplier payment days, stock days.
8. Tax placeholder (basis and rate, To confirm with an accountant).
Write the inputs to `model.json` in the fin_model format (`python3 scripts/fin_model.py --example` shows it), run `python3 scripts/fin_model.py model.json --state-export numbers.json`, then `plan_state.py import-numbers numbers.json` and `check_plan.py`.

## Sections

### financials.assumptions — Key assumptions
- **Ask:** Let's list the assumptions behind your numbers: which are facts, which are estimates, and how will you check them?
- **Done when:** an assumptions register (id, assumption, value, unit, label, source, how to validate, by when) covering every input that moves results by more than about 10%.
- **Teach:** Assumptions register · Claim labels and evidence
- **Length:** a table (appendix for long plans).

### financials.forecast — Sales forecast
- **Ask:** Starting from your first month, how many units or customers will you sell each month, at what price?
- **Method:** build from drivers (capacity, funnel, channels), not from a target revenue. Compare with gtm.targets (C04), capacity (C02) and SOM (C03). Flag growth above about 15% a month sustained for a year (C10, rule of thumb).
- **Done when:** a monthly forecast per stream for the period the reader needs, with yearly totals and the drivers stated.
- **Common mistakes:** top-down "1% of the market" forecasts · instant full capacity · flat prices for three years with rising costs.
- **Teach:** Revenue forecast drivers
- **Length:** yearly table in the text; monthly table in an appendix.

### financials.costs — Costs
- **Ask:** What are your monthly fixed costs, your direct costs per unit and your planned salaries?
- **Done when:** fixed costs by category, direct costs per unit, payroll with on-costs, and one-off start-up costs; every person in the team plan has a cost (C05).
- **Common mistakes:** forgetting founder pay, marketing, insurance, accounting, software, maintenance, bank and payment fees.
- **Teach:** Fixed and variable costs · Payroll on-costs
- **Length:** a cost table.

### financials.cash_flow — Cash flow
- **Ask:** (Show the model's cash line) Does this match how money really moves in your business, including late payers and stock bought in advance?
- **Done when:** month-end cash for every month; low point and month stated; no month below zero without funding shown (C06).
- **Teach:** Profit versus cash · Cash flow and cash low point · Runway and burn rate
- **Length:** summary lines plus a monthly table in the appendix.

### financials.break_even — Break-even
- **Ask:** At what monthly sales do you cover all costs, and in which month do you expect to get there?
- **Method:** `bizcalc.py break-even --fixed F --price P --unit-cost C` for units; the model's break-even month for timing.
- **Done when:** break-even units or revenue per month, and the month reached in the base case.
- **Teach:** Break-even point · Contribution margin
- **Length:** 2–3 lines.

### financials.scenarios — Scenarios
- **Ask:** If sales come 30% slower and costs 10% higher, what happens to cash?
- **Method:** add `scenarios` (base, downside, optional upside) and `sensitivity` to the model; report the cash low point and funding need for each.
- **Done when:** a downside case with stated assumptions and its cash low point; the plan says what the founder would do if it happens.
- **Teach:** Scenarios and sensitivity
- **Length:** a 2–3 row table plus 2 lines.

### financials.funding — Funding need and use of funds
- **Ask:** How much money do you need, from whom, and for what exactly?
- **Method:** funding need = safety buffer minus the cash low point (`bizcalc.py funding-need`); the ask covers the need (C07); use-of-funds lines add up to the ask exactly (C08; save `funding.ask` and `use_of_funds.<item>`). Loans: `bizcalc.py loan` for instalments and `bizcalc.py dscr` for coverage.
- **Done when:** amount, type of money (equity, loan, grant, own funds), timing, use-of-funds table, and what milestones the money reaches.
- **Common mistakes:** asking for a round number with no link to the cash low point · use of funds that does not add up · no buffer.
- **Teach:** Funding need and use of funds · Loans and debt service · Equity and dilution
- **Labels:** the ask is Planned; quotes behind use of funds Verified where available.
- **Length:** a use-of-funds table plus 2–4 lines.

## Module summary

Lead with the decision numbers: cash low point and month, break-even month, funding need. Then yearly revenue, gross margin, EBITDA and net profit; scenario results; checks C01–C14 that touch numbers; the assumptions to validate first.

## Hand-offs

business-plan-financials (when installed) runs this module in depth, including the spreadsheet (`fin_model.py --xlsx`). Without it, use `scripts/fin_model.py` from this skill.
