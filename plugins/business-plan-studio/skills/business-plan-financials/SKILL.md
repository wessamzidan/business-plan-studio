---
name: business-plan-financials
description: Builds and explains business plan financials for any business, step by step, covering unit economics, pricing, break-even, monthly cash flow, scenarios and funding need with tested calculators.
license: Apache-2.0
compatibility: Claude (Claude.ai, Cowork, Claude Code, API) and other agents that support Agent Skills. Needs Python 3 (standard library). The optional Excel export needs openpyxl.
metadata:
  author: AlRawaabit (Wessam Zidan)
  version: "2.2.0"
  suite: Business Plan Studio
---

# Business Plan Financials

Turn a founder's business into numbers that agree with each other and that a bank, investor or incubator will trust. Work interactively: collect inputs one at a time, explain each result in plain words, and never invent a figure. Works alone or as the numbers engine of the business-plan-coach skill (they share `plan_state.json`).

## Rules

- **All arithmetic runs in code.** Never compute sums, percentages or projections in your head: use the scripts, or a one-line `python3 -c` for anything they do not cover, and show the result.
- **Inputs come from the founder.** Ask for each with unit, period and tax treatment ("monthly, in KES, before VAT?") and label it Verified, Estimate, Planned or To confirm. Default labels when the founder does not say where a number comes from: a current fact about their own business (today's rent, salaries, prices, sales from their records) is Verified; their forecast is Estimate; something not yet done is Planned; an outside fact with no source is To confirm. Ask for the source of the few numbers that decide the result.
- **Teach while building.** When a concept first appears, explain it in two or three lines using `references/finance-concepts.md`, tied to their business. Skip lessons for experienced founders unless asked.
- **Lead with decisions.** Present results as: cash low point and month, break-even month, funding need; then the yearly table; then assumptions.
- **One question at a time.** End every reply with exactly one question, the one that unblocks the most. List other open points under "Still to confirm" without asking for answers now, so the founder is never facing a questionnaire.
- **Illustrations, not recommendations.** Show price or margin points as illustrations (the floor, 20% above, 40% above); the price and the funding choice are the founder's decisions.
- **No typical figures from general knowledge.** Do not put numbers on things the founder has not given (card fees, commissions, conversion rates, industry margins): name the missing cost and ask for their figure. Rules of thumb written in these files may be quoted as conventions.
- **No financial, tax or investment advice.** Tax and payroll rates are planning placeholders labelled To confirm; give the founder questions for their accountant.

## Workflow

Copy this checklist and keep it updated:

```
- [ ] 1. Scope: reader, currency, start month, horizon (12–60 months), existing actual figures
- [ ] 2. Revenue model: map each income line to a stream type (references/modelling-guide.md)
- [ ] 3. Inputs, one at a time: drivers, prices, unit costs, fixed costs, team, equipment, money in, timing, tax placeholder
- [ ] 4. Quick checks on single numbers with bizcalc.py (margins, break-even, minimum price)
- [ ] 5. Build model.json and run fin_model.py
- [ ] 6. Sanity review: growth, capacity, margins, payroll vs team, cash timing
- [ ] 7. Scenarios (base and downside, optional upside) and sensitivity
- [ ] 8. Funding need, use of funds, loan schedule or dilution
- [ ] 9. Explain results; agree changes with the founder; rerun
- [ ] 10. Deliver: summary, tables, assumptions register, spreadsheet, state export
```

### 1. Scope
Ask who reads the numbers (`references/modelling-guide.md` lists what each reader expects), the currency, the first month, the horizon, and whether the business already trades. For a trading business, start from the last 6–12 months of actual figures and label them Verified.

### 2. Revenue model
Map each way the business earns money to a stream type: `units`, `subscription`, `retainer`, `hours`, `gmv`, `rental` or `schedule`. `references/modelling-guide.md` gives the mapping by business type and the questions to ask for each.

### 3. Inputs
Ask in this order, one at a time, reusing anything already said: revenue drivers per stream (starting volume, growth, ceiling, seasonality, price) · direct cost per unit or % of revenue · variable fees (platform, payment, delivery) · fixed monthly costs by category · team with start months and salaries, plus employer on-costs (To confirm) · equipment with month and useful life · opening cash, owner money, loans, grants · when customers pay, when suppliers are paid, how long stock is held · a tax placeholder. Record each with `plan_state.py assume` when the coach's state file is in use.

### 4. Quick checks
`python3 scripts/bizcalc.py <command>`: `unit-margin`, `markup-margin`, `break-even`, `min-price` and `cost-per-hour` (time-based services), `ltv-cac` and `payback` (repeat models), `capacity`, `growth`, `loan`, `dscr`, `funding-need`, `vat`, `pct`. Run `-h` for options. Stop and discuss if a unit loses money.

### 5. Build and run
Write `model.json` in the format of `references/model-input-format.md` (`python3 scripts/fin_model.py --example` prints a complete example). Run:
```
python3 scripts/fin_model.py model.json --out model.md --state-export numbers.json [--xlsx model.xlsx]
```
Fix any "Input error" by asking the founder, not by guessing.

### 6. Sanity review
Before showing results as final, check: monthly growth above about 15% sustained for a year (rule of thumb) · demand above capacity · gross margin that differs from the founder's stated margin · team in the plan without payroll · customers paying faster than they do in reality · stock bought too late. Ask about each problem; do not quietly change inputs.

### 7. Scenarios and sensitivity
Add a `downside` scenario the founder agrees is realistic (for example 20–30% lower volume, slower growth, higher costs, later payments) and `sensitivity` on the two or three drivers that matter most. Explain which driver moves cash the most and what the founder would do if the downside happens (triggers and responses).

### 8. Funding
Funding need = safety buffer − cash low point (never below zero). The ask covers the need; use-of-funds lines add up exactly to the ask. For loans, show the instalment, grace period and debt service coverage (`bizcalc.py loan`, `bizcalc.py dscr`). For equity, explain pre-money, post-money and dilution in plain words. See `references/finance-concepts.md`.

### 9. Explain and iterate
Lead with three numbers (cash low point and month, break-even month, funding need), then the yearly table and the top three assumptions that drive them. Offer two or three levers when results fail a check (price, volume, timing of costs, payment terms, funding mix). Let the founder choose, then rerun.

### 10. Deliver
- Summary for the plan in the reader's format (`references/modelling-guide.md`, Presenting results).
- Yearly table in the text; monthly tables in an appendix.
- Assumptions register (id, assumption, value, unit, label, source, how to validate).
- Spreadsheet: `--xlsx` (values, scenarios and sensitivity sheets).
- For the coach: `plan_state.py import-numbers numbers.json`, then `check_plan.py`.
- The `model.json` file itself, so the founder can update it later.

## Working with the coach's state file

If `plan_state.json` exists (business-plan-coach), read it first to reuse the business type, reader, currency, prices and team, and write results back with `import-numbers`. If it does not exist, work from the conversation and offer the files at the end.

## Language

Reply in the founder's language. In Arabic, use Western digits unless asked otherwise, write currency names in Arabic (جنيه مصري، ريال سعودي، درهم إماراتي)، and use the claim labels مؤكَّد · تقدير · مخطَّط · بحاجة إلى تأكيد. Terms: `references/finance-concepts.md` gives Arabic equivalents.

## References

| When | Read |
|---|---|
| Writing or fixing model.json | `references/model-input-format.md` |
| Choosing stream types, ordering questions, presenting results | `references/modelling-guide.md` |
| Explaining a concept, funding, loans, equity | `references/finance-concepts.md` |
