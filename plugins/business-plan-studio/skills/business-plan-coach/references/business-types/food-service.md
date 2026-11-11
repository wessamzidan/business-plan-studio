# Business type: Restaurants, cafés, cloud kitchens and catering

Covers restaurants, cafés, bakeries with seating, cloud (delivery-only) kitchens, food trucks and catering companies.

## How money is made
Covers (guests) or orders × average ticket, minus food cost, packaging, delivery-app commissions and labour. Thin margins mean small leaks (waste, commissions, staffing at quiet hours) decide profit.

## Key drivers and metrics
| Metric | Formula | Why it matters | Sections |
|---|---|---|---|
| Covers or orders a day | seats × turns, or orders by channel | Volume driver | financials.forecast |
| Average ticket | revenue ÷ covers or orders | Price and upselling | model.pricing |
| Food cost % | ingredient cost ÷ food revenue | Menu engineering | model.unit_economics |
| Labour % | payroll ÷ revenue | Largest controllable cost | financials.costs |
| Prime cost | food cost + labour | Common health check | financials.costs |
| Channel mix | dine-in vs own delivery vs apps | Apps charge commissions | gtm.channels |
| Waste | food thrown away ÷ food bought | Hidden loss | operations.activities |

## Sharpest questions
- `model.unit_economics`: What is the food cost of your three best-selling dishes, recipe by recipe?
- `gtm.channels`: What share of orders will come through delivery apps, and what commission do they take?
- `financials.forecast`: How many covers or orders on a weekday and on a weekend, by month?
- `operations.location_equipment`: What does the kitchen fit-out cost, and how many orders can it make an hour?
- `financials.costs`: How many staff per shift, and what is labour as a share of sales?
- `operations.legal`: Which health, municipal and fire licences do you need, and how long do they take?
- `operations.suppliers`: Who supplies key ingredients, and how often do prices change?
- `customer.priority_segment`: Office lunch, families, students or late-night delivery: who first?
- `risks.register`: What if ingredient prices rise 20%?
- `validation.evidence`: Have you sold your food anywhere yet (pop-ups, home orders, catering)?

## Options to offer
- Formats: dine-in · takeaway · own delivery · delivery apps · catering and events · packaged products to shops.
- Pricing: menu engineering (stars, puzzles, plough-horses), combos, minimum order for delivery.
- Channels: apps, maps listings, social media, office partnerships, events.

## Model template
Driver tree: orders per day × days × average ticket per channel; food cost %; app commission on app orders; packaging per order. Use one `units` stream per channel (dine-in, apps, catering) with seasonality; commissions as `variable_pct`.
```json
{"name": "Bowl Street (fictional)", "currency": "EGP", "start": "2027-01", "months": 12,
 "opening_cash": 400000,
 "streams": [
  {"name": "App orders", "type": "units", "volume": {"start": 1890, "growth_pct": 2}, "price": 220, "cost_pct": 35.6, "variable_pct": 25, "collection_days": 15},
  {"name": "Direct orders", "type": "units", "volume": {"start": 810, "growth_pct": 3}, "price": 220, "cost_pct": 35.6}],
 "fixed_costs": [{"name": "Kitchen rent", "monthly": 30000}, {"name": "Utilities and gas", "monthly": 18000}],
 "team": [{"role": "Cooks", "count": 4, "monthly_salary": 9000}, {"role": "Kitchen manager", "count": 1, "monthly_salary": 15000}],
 "capex": [{"name": "Kitchen equipment", "amount": 600000, "month": "2027-01", "life_months": 60}]}
```

## Capacity and operations
Orders per hour at peak, not per day, limit sales: ask for station capacity at lunch and dinner peaks. Delivery radius and preparation time affect app rankings.

## Convincing evidence
Level 2: tastings with target customers · Level 3: catering pre-orders, office lunch agreements · Level 4: pop-up or home-kitchen sales with receipts · Level 5: repeat orders and app ratings over months.

## Red flags reviewers spot
- Food cost from a guess, not recipe costing.
- App commissions or packaging left out.
- Full tables every day from month one.
- No licences budgeted or timed.
- Labour planned for average days, not peaks.

## Typical risks and mitigations
Ingredient price swings → menu review every quarter, supplier contracts · app dependence → own ordering channel, loyalty · staff turnover → training, shift planning · licence delays → start the process before signing the lease.

## Fictional mini-example
Bowl Street (fictional), a Cairo cloud kitchen: 90 orders a day for 30 days = 2700 orders at 220 EGP = 594000 EGP a month. Food at 32% costs 190080 EGP, packaging at 8 EGP an order 21600 EGP, and the 25% app commission on the 70% of orders through apps 103950 EGP: the commission alone is larger than rent and gas together.

## Hybrids
Food-service + manufacturing (packaged products for shops: separate batch costs and wholesale prices) · food-service + appointment-experience (cooking classes, events).
