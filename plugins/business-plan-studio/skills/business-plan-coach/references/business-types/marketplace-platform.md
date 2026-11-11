# Business type: Marketplaces and platforms

Covers two-sided marketplaces (services, goods, rentals, freelancers, B2B sourcing), booking platforms and any business earning a take rate on transactions between others.

## How money is made
A percentage (take rate) of the value of transactions between buyers and sellers (GMV), sometimes plus listing fees, subscriptions or ads. The platform must attract both sides at the same time and keep transactions on the platform.

## Key drivers and metrics
| Metric | Formula | Why it matters | Sections |
|---|---|---|---|
| GMV | value of all transactions | Volume driver | financials.forecast |
| Take rate | platform revenue ÷ GMV | Pricing power | model.pricing |
| Liquidity | share of listings or requests that result in a transaction | Proof the marketplace works | validation.metrics |
| Supply and demand CAC | cost to add one active seller and one active buyer | Growth cost on both sides | gtm.channels |
| Repeat rate | buyers transacting again | Keeps CAC low | validation.metrics |
| Leakage | transactions moving off the platform | Silent revenue loss | risks.register |
| Contribution per transaction | take − payment, support, insurance and refund costs | Real margin | model.unit_economics |

## Sharpest questions
- `customer.segments`: Who are the two sides, and which side is harder to get?
- `gtm.channels`: Which side will you build first, in which city or niche, and how?
- `validation.metrics`: Of the requests or listings so far, what share turned into paid transactions?
- `model.pricing`: What take rate, charged to whom, and why will they accept it?
- `model.unit_economics`: After payment fees, support, refunds and insurance, what does one transaction leave?
- `risks.register`: Why will users keep transacting on the platform instead of going direct?
- `operations.activities`: How do you vet suppliers and handle disputes?
- `financials.forecast`: How do active buyers, active sellers and transactions per user grow each month?
- `operations.legal`: Who is liable when something goes wrong; which licences apply to payments?
- `customer.alternatives`: What do buyers and sellers use today (classifieds, WhatsApp groups, agents)?

## Options to offer
- Revenue: commission on transactions · subscription for sellers · featured listings and ads · payment or financing fees · managed services.
- Launch: one niche and one city first · seed supply manually · guarantee quality on early transactions · referral rewards.

## Model template
Driver tree: GMV = active buyers × transactions per buyer × average value; revenue = GMV × take rate; costs = payment and support per transaction plus acquisition on both sides. Use a `gmv` stream with `cost_pct` for transaction costs (as % of platform revenue) and fixed marketing budgets for each side.
```json
{"name": "FixKaro (fictional)", "currency": "INR", "start": "2027-01", "months": 24,
 "opening_cash": 25000000,
 "streams": [{"name": "Home services commissions", "type": "gmv", "gmv": {"start": 3000000, "growth_pct": 12, "max": 30000000},
   "take_rate_pct": 15, "cost_pct": 13.3}],
 "fixed_costs": [{"name": "Supply acquisition", "monthly": 600000, "category": "marketing"},
                 {"name": "Demand acquisition", "monthly": 1200000, "category": "marketing"},
                 {"name": "Tech and tools", "monthly": 400000}],
 "team": [{"role": "Engineering", "count": 4, "monthly_salary": 150000},
          {"role": "Operations and support", "count": 6, "monthly_salary": 40000}]}
```

## Capacity and operations
Capacity is supply quality and support: how many verified providers in each area, response times, dispute handling per 1000 transactions.

## Convincing evidence
Level 2: interviews on both sides · Level 3: suppliers signed up and buyers on a waitlist · Level 4: paid transactions with a take rate charged · Level 5: repeat transactions and rising liquidity in the first city.

## Red flags reviewers spot
- Growth assumed on both sides at once with one marketing budget.
- Take rate higher than sellers' margins can carry.
- Leakage ignored.
- GMV reported as revenue.
- National launch before one city works.

## Typical risks and mitigations
Chicken-and-egg → start narrow, seed supply · leakage → value-added services (payments, insurance, reviews) · quality incidents → vetting and guarantees · a funded competitor → own a niche deeply.

## Fictional mini-example
FixKaro (fictional), Mumbai: 12000000 INR of monthly bookings at a 15% take rate is 1800000 INR of revenue; payment costs of 2% of bookings (240000 INR) leave 1560000 INR before support and acquisition on both sides.

## Hybrids
Marketplace + SaaS (seller software subscriptions: add a `subscription` stream) · marketplace + trade-distribution (holding stock: add `units` streams and inventory days).
