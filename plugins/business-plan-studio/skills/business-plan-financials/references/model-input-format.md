# fin_model.py input format

The model reads one JSON file. Every amount is in the plan's currency, net of VAT or sales tax. Months are written `YYYY-MM`.

## Contents
- Top-level fields
- Revenue streams (7 types)
- Costs, team and capital spending
- Financing
- Timing of cash (collection, payment, stock)
- Tax placeholder
- Scenarios and sensitivity
- Output
- Complete example

## Top-level fields

| Field | Required | Meaning |
|---|---|---|
| `name` | no | Plan or company name, shown in the output |
| `currency` | yes | Currency code shown in every header, e.g. `EGP`, `SAR`, `USD` |
| `start` | yes | First month of the model, e.g. `2027-01` |
| `months` | no | Number of months, 12 to 60 (default 24) |
| `opening_cash` | no | Cash in the bank at the start (default 0) |
| `min_cash_buffer` | no | Cash the founder never wants to go below. Default: 3 × average monthly payroll plus fixed costs over the first 6 months |
| `streams` | yes | List of revenue streams (below) |
| `fixed_costs`, `team`, `employer_oncost_pct`, `capex`, `financing`, `payment_days`, `inventory_days`, `tax`, `scenarios`, `sensitivity` | no | See below |

## Revenue streams

Every stream has `name`, `type`, optional `start` (month it begins; default the model start) and optional `end`. Growth fields use a ramp object:

`{"start": 1200, "growth_pct": 5, "max": 6000}` means 1200 in the first month, +5% each month, never above 6000. Use `"growth_pts": 2` instead of `growth_pct` for percentages that rise by points (occupancy, utilisation). Add `"schedule": [..]` (one value per month) to override a ramp entirely.

Optional on every stream: `seasonality` (12 multipliers for January to December, default all 1), `price_growth_pct_yearly` (price rises every 12 months from the stream start), `variable_pct` (fees, commissions, delivery as % of revenue), `collection_days` (see Timing), and cost of sales as either `unit_cost` (per unit of the driver) or `cost_pct` (% of revenue).

| `type` | Driver fields | Revenue each month | Cost of sales |
|---|---|---|---|
| `units` | `volume` (ramp), `price`; optional `capacity` (most units deliverable in a month: the model warns when the plan exceeds it and exports it for check C02) | volume × price | volume × `unit_cost`, or revenue × `cost_pct` |
| `subscription` | `customers_start`, `new` (ramp of new customers per month), `churn_pct`, `price` (per customer per month) | active customers × price; active = previous × (1 − churn) + new | active × `unit_cost` |
| `retainer` | same fields as `subscription` (clients and monthly fee) | same | same |
| `hours` | `capacity_hours` (team hours available per month), `utilisation_pct` (ramp, %), `rate` (price per hour) | capacity × utilisation × rate | billed hours × `unit_cost` (direct cost per hour) |
| `gmv` | `gmv` (ramp of gross merchandise value), `take_rate_pct` | GMV × take rate | revenue × `cost_pct` |
| `rental` | `units_available`, `occupancy_pct` (ramp, %), `price` (per unit per month) | units × occupancy × price | occupied units × `unit_cost` |
| `schedule` | `amounts` (`{"2027-03": 50000, ...}`) | the amount in that month | revenue × `cost_pct` |

Subscription and retainer streams may use `cac` with a marketing budget instead of a ramp: give `"new": {"from_budget": 15000, "cac": 125}` and new customers = budget ÷ CAC (the budget is also added to fixed costs as marketing). In a scenario, a volume change keeps the budget and moves the CAC, so a −30% downside means the same spend wins 30% fewer customers.

## Costs, team and capital spending

- `fixed_costs`: `[{"name": "Rent", "monthly": 15000, "start": "2027-01", "end": null, "growth_pct_yearly": 10, "category": "premises"}]`. Categories are free text (marketing, premises, software, admin...).
- `team`: `[{"role": "Baker", "count": 2, "monthly_salary": 9000, "start": "2027-01", "end": null, "raise_pct_yearly": 10}]`. Founders who take pay go here too.
- `employer_oncost_pct`: employer social insurance and other payroll on-costs as % of salary (country specific; label To confirm until an accountant confirms).
- `capex`: `[{"name": "Oven", "amount": 120000, "month": "2027-01", "life_months": 60}]`. Cash leaves in that month; the profit and loss shows straight-line depreciation over `life_months`.

## Financing

`financing`: list of
- `{"type": "equity", "amount": 300000, "month": "2027-01"}`
- `{"type": "grant", "amount": 50000, "month": "2027-04"}` (grants are shown as cash in, not as revenue; ask an accountant how to book them)
- `{"type": "loan", "amount": 200000, "month": "2027-02", "rate_pct": 18, "term_months": 24, "grace_months": 3}`: interest-only during grace, then equal monthly instalments for the rest of the term. Interest goes to the profit and loss; principal only to cash.

## Timing of cash

Days are turned into whole months: 0–14 days = same month, 15–44 = one month later, 45–74 = two months later, and so on.
- `collection_days` (per stream): customers pay this long after the sale.
- `payment_days` (top level): the business pays suppliers for cost of sales this long after the sale.
- `inventory_days` (top level): stock is bought this long before it is sold. Cost of sales cash moves by (payment_days − inventory_days); a negative result means paying before selling.
Cash that would fall after the last month is left out of the cash flow and reported as receivables or payables at the end. A payment that would fall before the first month is placed in the first month.

## Tax placeholder

`tax`: `{"basis": "profit", "rate_pct": 22.5}` charges tax on positive profit before tax for each 12-month block, in the block's last month. `{"basis": "turnover", "rate_pct": 1}` charges the rate on each month's revenue. `{"basis": "none"}` is the default. This is a planning placeholder only: label it To confirm and ask an accountant.

## Scenarios and sensitivity

`scenarios`: named changes applied to the base inputs, for example
`{"downside": {"volume_pct": -30, "growth_pct_points": -3, "price_pct": -5, "cost_pct": 10, "churn_pct_points": 2, "collection_days_add": 30}, "upside": {"volume_pct": 20}}`.
`volume_pct` scales every starting volume (units, new customers, GMV, utilisation, occupancy, schedule amounts); `price_pct` scales prices, hourly rates, take rates and schedule amounts; `cost_pct` scales unit costs and fixed costs together, while `unit_cost_pct` and `fixed_pct` scale one of them; `growth_pct_points` adds points to every `growth_pct`; `churn_pct_points` adds points to churn; `collection_days_add` delays customer payments.

`sensitivity`: list of drivers from `price`, `volume`, `unit_cost`, `fixed_costs`, `growth`. Each is tested at −20%, −10%, +10% and +20% and reported as year-1 net profit and cash low point.

## Output

`python3 scripts/fin_model.py model.json` prints a Markdown summary; `python3 scripts/fin_model.py --example` prints the complete example below. Options:
- `--format json|csv|md` (default md); `--out FILE`
- `--xlsx FILE` writes a workbook (Inputs, Monthly, Summary, Scenarios, Sensitivity) when `openpyxl` is installed; otherwise it says so and continues
- `--state-export FILE` writes the numbers the coach's `check_plan.py` needs: `forecast.revenue_y1` (and `_y2`...), `forecast.revenue.<YYYY-MM>`, `cash.low_point`, `cash.low_point_month`, `cash.buffer`, `funding.need` (after the financing in the model), `funding.need_without_financing` and `funding.in_model` (so the coach can compare the ask with the need before any financing), `model.break_even_month`, `model.gross_margin_pct_y1`, `model.headcount_peak`, `payroll.monthly_avg_y1`, `offer.<stream>.price` / `offer.<stream>.unit_cost` per stream, and `capacity.<stream>` / `demand.<stream>` for `units` streams with a `capacity` and for `hours` streams (as `<stream>_hours`). Stream names become keys in lower case with underscores. Load them with `plan_state.py import-numbers FILE`.

Summary fields: revenue, gross margin %, EBITDA and net profit per 12-month block; first month from which EBITDA stays at or above zero; cash low point and its month; months below zero; funding need = max(0, buffer − cash low point), both after the financing in the model and without it; ending cash; receivables and payables left at the end.

## Complete example

```json
{
  "name": "Qamar Crisps (fictional)",
  "currency": "EGP",
  "start": "2027-01",
  "months": 24,
  "opening_cash": 150000,
  "streams": [
    {"name": "Cafe wholesale", "type": "units", "volume": {"start": 1200, "growth_pct": 5, "max": 6000},
     "price": 18, "unit_cost": 7, "collection_days": 30, "price_growth_pct_yearly": 10},
    {"name": "Online shop", "type": "units", "volume": {"start": 300, "growth_pct": 8, "max": 3000},
     "price": 35, "unit_cost": 9, "variable_pct": 12}
  ],
  "fixed_costs": [
    {"name": "Kitchen rent", "monthly": 15000, "growth_pct_yearly": 10, "category": "premises"},
    {"name": "Online ads", "monthly": 8000, "category": "marketing"}
  ],
  "team": [{"role": "Baker", "count": 2, "monthly_salary": 9000, "raise_pct_yearly": 10}],
  "employer_oncost_pct": 18.75,
  "capex": [{"name": "Oven", "amount": 120000, "month": "2027-01", "life_months": 60}],
  "financing": [{"type": "loan", "amount": 100000, "month": "2027-01", "rate_pct": 18, "term_months": 24, "grace_months": 3}],
  "payment_days": 30,
  "scenarios": {"downside": {"volume_pct": -30, "growth_pct_points": -2, "cost_pct": 10}},
  "sensitivity": ["price", "volume", "unit_cost"]
}
```
