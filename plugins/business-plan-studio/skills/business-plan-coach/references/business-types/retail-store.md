# Business type: Physical retail shop

Covers shops, kiosks, pharmacies, bookshops, grocery and convenience stores, showrooms and franchise units.

## How money is made
Visitors walk in, a share buy (conversion), each spends a basket amount, and the margin on goods pays rent, staff and stock. Location, stock management and rent decide the outcome.

## Key drivers and metrics
| Metric | Formula | Why it matters | Sections |
|---|---|---|---|
| Footfall | visitors per day | Driven by location | market.size, operations.location_equipment |
| Conversion | transactions ÷ visitors | Store quality and range | gtm.sales_process |
| Basket size | revenue ÷ transactions | Range, pricing, upselling | model.pricing |
| Gross margin | (sales − cost of goods) ÷ sales | Pays everything else | model.unit_economics |
| Rent ratio | rent ÷ sales | High ratios sink shops | financials.costs |
| Stock turns | cost of goods sold a year ÷ average stock | Cash tied in shelves | model.payment_terms |
| Shrinkage | stock lost to theft, damage, expiry ÷ sales | Hidden margin loss | financials.costs |

## Sharpest questions
- `operations.location_equipment`: How many people pass the shop each day, and how did you count them?
- `gtm.sales_process`: What share of visitors buy, and what do they spend?
- `model.pricing`: What is your margin by product category?
- `financials.costs`: What is the rent, and what share of expected sales is it?
- `operations.suppliers`: Which suppliers give credit, and on what terms?
- `model.payment_terms`: How long does stock sit before it sells?
- `competition.competitors`: Which shops within walking distance sell the same items, at what prices?
- `financials.forecast`: Which months are strongest (seasons, holidays, school year)?
- `operations.legal`: Which licences, signage and municipal permits are needed?
- `risks.register`: What happens if a big competitor opens nearby?

## Options to offer
- Revenue: product sales · services in store (repairs, printing) · online orders with pickup · loyalty programmes.
- Channels: location and window · local social media · maps listings · delivery apps · community events.

## Model template
Driver tree: transactions = footfall × conversion; revenue = transactions × basket; cost of goods from margin; seasonality for holidays. Use a `units` stream with monthly transactions as volume and the basket as price; `cost_pct` = 100 − gross margin %.
```json
{"name": "Qalam Stationery (fictional)", "currency": "MAD", "start": "2027-01", "months": 12,
 "opening_cash": 150000, "inventory_days": 45, "payment_days": 30,
 "streams": [{"name": "Shop sales", "type": "units", "volume": {"start": 2002, "growth_pct": 1},
   "price": 45, "cost_pct": 62,
   "seasonality": [0.9, 0.9, 1, 1, 1, 0.8, 0.7, 0.8, 1.6, 1.2, 1, 1.1]}],
 "fixed_costs": [{"name": "Rent", "monthly": 12000}, {"name": "Utilities and systems", "monthly": 3000}],
 "team": [{"role": "Sales staff", "count": 2, "monthly_salary": 3500}],
 "capex": [{"name": "Shop fit-out", "amount": 80000, "month": "2027-01", "life_months": 60}]}
```

## Capacity and operations
Capacity is staff hours at the till and shelf space; peaks (back to school, holidays) need temporary staff and earlier stock.

## Convincing evidence
Level 2: footfall counts at different times and days · Level 3: supplier quotes and a signed lease offer · Level 4: sales from a pop-up or an existing shop · Level 5: repeat customers and loyalty data.

## Red flags reviewers spot
- Footfall from guesses, not counts.
- Rent above roughly 10–15% of expected sales (rule of thumb; check local norms).
- No seasonality.
- Stock financed by cash with no supplier credit.
- Gross margin taken from supplier price lists with no shrinkage.

## Typical risks and mitigations
Low footfall → test with a pop-up first, choose location on counts · stock that does not sell → small first orders, weekly sales review · theft and damage → controls and insurance · rent increases → longer lease with fixed steps.

## Fictional mini-example
Qalam Stationery (fictional), Casablanca: 220 visitors a day, 35% buy, 45 MAD basket: 77 sales a day, 3465 MAD a day, about 90090 MAD over 26 days. At a 38% gross margin that leaves about 34234 MAD a month; rent of 12000 MAD is 13.3% of sales, high enough to watch.

## Hybrids
Retail + e-commerce (click and collect) · retail + food-service (café corner: separate margins and staff).
