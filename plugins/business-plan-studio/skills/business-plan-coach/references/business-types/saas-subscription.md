# Business type: Software and subscriptions

Covers SaaS, mobile apps with paid plans, subscription boxes, memberships sold online and any business paid monthly or yearly for continuing access.

## How money is made
Customers pay every month or year while they stay. Value builds as customers accumulate, so the plan depends on how fast new customers arrive, how many leave (churn), how much each pays, and what it costs to win them.

## Key drivers and metrics
| Metric | Formula | Why it matters | Sections |
|---|---|---|---|
| MRR | active customers × monthly price | Core revenue measure | validation.metrics |
| Churn | customers lost in a month ÷ customers at the start | Small changes compound over years | model.unit_economics |
| CAC | sales and marketing spend ÷ new customers | Cost of growth | gtm.channels |
| LTV | monthly revenue × gross margin ÷ churn (`bizcalc.py ltv-cac`) | Value of a customer | model.unit_economics |
| LTV/CAC and payback | LTV ÷ CAC; CAC ÷ monthly margin | Investors' first check (C09) | model.unit_economics |
| Activation | share of sign-ups reaching the first value moment | Leaky products churn early | validation.metrics |
| Net revenue retention | revenue from last year's customers this year ÷ last year | Expansion vs churn | financials.forecast |

## Sharpest questions
- `validation.evidence`: How many customers pay today, and how many were free pilots?
- `model.pricing`: What is each plan's price, and which plan do most customers choose?
- `model.unit_economics`: What did it cost to win your last 20 customers, all costs included?
- `validation.metrics`: What share of customers who paid three months ago still pay?
- `gtm.channels`: Which channel brought your best-retained customers?
- `offer.value_proposition`: What does the customer lose if they cancel?
- `operations.resources`: What does it cost to serve one customer (hosting, support, payment fees)?
- `financials.forecast`: How many new customers a month, from which spend, at what CAC?
- `team.hiring_plan`: When do you add sales and support, and what triggers it?
- `customer.alternatives`: What do customers use today: spreadsheets, a local competitor, a global tool?
- `financials.funding`: How many months of runway does the ask give, and what MRR will you reach?

## Options to offer
- Pricing: monthly or yearly (discount for yearly) · tiers by usage or seats · setup fee · freemium with paid upgrade · per-location pricing for multi-branch clients.
- Channels: content and search · free trial · partners and resellers · direct sales for bigger clients · marketplaces and app stores.

## Model template
Driver tree: active customers = previous × (1 − churn) + new; revenue = active × price; new customers from a marketing budget ÷ CAC or a ramp. Use a `subscription` stream; add a `units` stream for setup fees.
```json
{"name": "Mawid Pro (fictional)", "currency": "SAR", "start": "2027-01", "months": 24,
 "opening_cash": 400000,
 "streams": [
  {"name": "Clinic plan", "type": "subscription", "customers_start": 12,
   "new": {"from_budget": 12000, "cac": 1200}, "churn_pct": 3, "price": 300, "unit_cost": 45},
  {"name": "Setup fee", "type": "units", "volume": 10, "price": 500, "unit_cost": 100}],
 "fixed_costs": [{"name": "Hosting and tools", "monthly": 4000}],
 "team": [{"role": "Developers", "count": 2, "monthly_salary": 14000},
          {"role": "Sales and support", "count": 1, "monthly_salary": 9000}],
 "employer_oncost_pct": 12,
 "scenarios": {"downside": {"churn_pct_points": 3, "volume_pct": -30}}}
```

## Capacity and operations
Capacity is rarely servers; it is onboarding and support hours per new customer. Ask how many new customers one support person can onboard a month.

## Convincing evidence
Level 3: paid pilots or pre-paid yearly plans · Level 4: paying customers beyond friends · Level 5: cohort retention over 6+ months, expansion revenue.

## Red flags reviewers spot
- Free pilots counted as customers; no data on conversion to paid.
- Churn assumed at 1% a month with no history.
- CAC from ads only, leaving out sales salaries (C09).
- Hockey-stick growth with flat marketing spend (C10).
- Prices in another currency with no exchange-rate assumption.

## Typical risks and mitigations
High churn → onboarding and success checks in the first 60 days · long sales cycles → smaller entry plan · a global competitor enters → local features, language, payment methods, support · cash burn → milestones tied to MRR.

## Fictional mini-example
Mawid Pro (fictional), Riyadh: clinic booking at 300 SAR a month with 85% gross margin, 3% monthly churn and a 1200 SAR CAC. LTV = 300 × 0.85 ÷ 0.03 = 8500 SAR; LTV/CAC 7.1; payback 4.7 months. The plan still shows the cash dip while new customers repay their acquisition cost.

## Hybrids
SaaS + services (setup and training fees: add `units` or `hours` streams) · SaaS + marketplace (take rate on bookings: add a `gmv` stream).
