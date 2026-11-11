# Business type: Services

Covers agencies, consultancies, professional services (accounting, legal support, engineering, design), freelancers, B2B service firms, IT services and maintenance contracts.

## How money is made
People's time, sold by the hour, by project, as monthly retainers or for a success fee. Revenue is capped by billable hours, so the plan lives or dies on utilisation, pricing per hour and repeat clients.

## Key drivers and metrics
| Metric | Formula | Why it matters | Sections |
|---|---|---|---|
| Productive hours | team members × billable hours each per month | Sets capacity and cost per hour | operations.resources |
| Utilisation | hours billed ÷ productive hours | Below ~60% the firm is idle; above ~85% quality and staff suffer (rules of thumb) | financials.forecast |
| Cost per hour | fixed monthly cost ÷ productive hours (`bizcalc.py cost-per-hour`) | Floor for every price | model.pricing |
| Minimum price | task hours × cost per hour + direct costs (`bizcalc.py min-price`) | Check C01 for every offer | model.pricing |
| Retainer share | retainer revenue ÷ total revenue | Predictability for banks and investors | model.revenue_streams |
| Client concentration | largest client ÷ total revenue | Risk if one client leaves | risks.register |

## Sharpest questions
- `model.pricing`: How many hours does each offer really take, including meetings, revisions and admin?
- `model.pricing`: What does one productive hour cost you? (run cost-per-hour with founder pay included)
- `model.revenue_streams`: Which share of revenue is recurring (retainers, maintenance) versus one-off?
- `customer.priority_segment`: Which client type pays fastest and comes back?
- `gtm.channels`: Where did your last five clients come from?
- `gtm.sales_process`: How many proposals do you send to win one client, and how long does it take?
- `operations.resources`: Who does the work, and what happens if they leave?
- `team.hiring_plan`: At what utilisation will you hire the next person?
- `financials.forecast`: How many retainer clients and projects per month, and how many hours each?
- `model.payment_terms`: Do clients pay upfront, monthly or 30–60 days after invoice?
- `risks.register`: What share of revenue comes from your largest client?
- `competition.advantage`: What do you know or have that a freelancer cannot copy?

## Options to offer
- Pricing models: hourly · fixed project fee · monthly retainer · value or success fee · packages (audit, implementation, support).
- Channels: referrals and case studies · LinkedIn and email outreach · partnerships with complementary firms · events and associations · marketplaces.
- Cost structure: salaries are most of the cost; tools and software; marketing; office or co-working.

## Model template
Driver tree: revenue = retainer clients × monthly fee + projects × project fee (+ hourly work); capacity = team hours; check hours needed ≤ hours available every month. Use `retainer` streams for retainers, `units` for projects, `hours` for pure hourly work.
```json
{"name": "Falcon Lane Studio (fictional)", "currency": "AED", "start": "2027-01", "months": 12,
 "streams": [
  {"name": "Retainers", "type": "retainer", "customers_start": 6, "new": {"start": 1}, "churn_pct": 4, "price": 9000, "unit_cost": 1000},
  {"name": "Projects", "type": "units", "volume": {"start": 2, "growth_pct": 3}, "price": 15000, "unit_cost": 1500}],
 "fixed_costs": [{"name": "Office and tools", "monthly": 9000}],
 "team": [{"role": "Designers and strategists", "count": 4, "monthly_salary": 12000}],
 "employer_oncost_pct": 10}
```

## Capacity and operations
Count productive hours honestly: about 60–75% of paid hours are billable in most small firms (rule of thumb: ask the founder for timesheets). Hours per retainer must be agreed and tracked; scope creep silently lowers the hourly rate.

## Convincing evidence
Level 3: signed proposals or letters of intent · Level 4: paid projects with invoices · Level 5: retainers renewed for 6+ months, referrals from clients.

## Red flags reviewers spot
- Prices set by competitors with no cost-per-hour check (C01).
- Revenue growth with no new hires while utilisation already exceeds 85% (C02).
- One client above 30–40% of revenue with no plan.
- Founders' time not costed, so the business looks profitable only because founders work for free.
- "Partnerships" with no signed agreement or referral history.

## Typical risks and mitigations
Key client loss → retainers with notice periods, more mid-size clients · scope creep → written scope and change requests · late payment → deposits, monthly billing in advance · key person leaves → documented processes, second person on every account.

## Fictional mini-example
Falcon Lane Studio (fictional), Dubai: 4 people with 520 productive hours a month and fixed costs (salaries, office, tools) of 62400 AED, so one hour costs 120 AED. A 40-hour monthly retainer with 1000 AED of direct costs has a minimum price of 5800 AED; the studio charges 9000 AED. Six retainers use 240 hours (46% utilisation), leaving room for projects before the next hire.

## Hybrids
Services + saas-subscription (agency with a software product: model both, watch that services cash funds the product) · services + trade-distribution (export agents earning fees and commissions: add `schedule` or `units` streams for commissions).
