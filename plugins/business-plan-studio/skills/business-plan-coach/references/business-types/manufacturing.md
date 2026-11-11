# Business type: Manufacturing and food processing

Covers small manufacturers, food and beverage processing, cosmetics and household products, furniture and crafts at scale, packaging and contract manufacturing.

## How money is made
Units produced and sold, usually through distributors, retailers or business buyers, at a wholesale price. Profit depends on unit cost build-up, batch efficiency, capacity use, distributor margins and the cash tied up in materials and stock.

## Key drivers and metrics
| Metric | Formula | Why it matters | Sections |
|---|---|---|---|
| Unit cost | materials + packaging + direct labour + energy per unit | Floor for every price | model.unit_economics |
| Capacity | units per shift × shifts × days | Caps revenue; check C02 | operations.location_equipment |
| Utilisation | units made ÷ capacity | Fixed cost per unit falls as it rises | financials.forecast |
| Price ladder | factory → distributor → retailer → shelf price | Shows if the shelf price is competitive | model.pricing |
| Minimum order quantities | smallest batch of each input | Cash tied in materials | operations.suppliers |
| Inventory days | days of materials and finished stock held | Working capital | model.payment_terms |
| Yield and waste | good units ÷ units started | Hidden cost | operations.activities |

## Sharpest questions
- `model.unit_economics`: Build the cost of one unit: materials, packaging, labour, energy, waste. Which input is most volatile?
- `model.pricing`: What does the shelf price become after distributor and retailer margins, and how does it compare with competing products?
- `operations.location_equipment`: How many units can your line make per shift, really, and what limits it?
- `operations.suppliers`: What are the minimum orders and lead times for packaging and key materials?
- `operations.legal`: Which certifications are needed to sell to retailers or export (food safety, standards, halal, labelling)?
- `gtm.channels`: Distributor, wholesale, direct to shops, private label or export: which first, and on what terms?
- `model.payment_terms`: When do retailers and distributors pay, and when do you pay suppliers?
- `financials.funding`: Which equipment do you need, and could you lease or contract-manufacture first?
- `risks.register`: What happens if your main material price rises 25%?
- `validation.evidence`: Which buyers have tasted, tested or ordered samples?

## Options to offer
- Routes to market: distributors · direct to retailers · private label for other brands · business buyers (hotels, cafés) · export later.
- Production: own line · contract manufacturer first · co-packing · phased equipment.

## Model template
Driver tree: units sold = min(demand, capacity); revenue = units × wholesale price by channel; cost of goods = unit cost × units; stock bought ahead (`inventory_days`); equipment as capex. Use `units` streams per channel and capex lines.
```json
{"name": "Tamu Juice (fictional)", "currency": "KES", "start": "2027-01", "months": 24,
 "opening_cash": 2500000, "inventory_days": 30, "payment_days": 30,
 "streams": [{"name": "Distributor sales", "type": "units", "volume": {"start": 18200, "growth_pct": 3, "max": 31200},
   "capacity": 31200, "price": 110, "unit_cost": 75, "collection_days": 45}],
 "fixed_costs": [{"name": "Factory rent and power", "monthly": 220000}, {"name": "Quality and certification", "monthly": 30000}],
 "team": [{"role": "Production staff", "count": 6, "monthly_salary": 30000}],
 "employer_oncost_pct": 8,
 "capex": [{"name": "Bottling line", "amount": 3500000, "month": "2027-01", "life_months": 84}],
 "financing": [{"type": "loan", "amount": 2000000, "month": "2027-01", "rate_pct": 16, "term_months": 36, "grace_months": 6}]}
```

## Capacity and operations
Capacity is the slowest step (filling, cooking, drying, packing). Ask for real output per shift on good and bad days, maintenance downtime and changeover time between products.

## Convincing evidence
Level 2: tastings and buyer feedback · Level 3: purchase orders or letters of intent from distributors · Level 4: first batches sold with invoices · Level 5: repeat orders and shelf sell-through data.

## Red flags reviewers spot
- Unit cost without packaging, waste or labour.
- Equipment capacity used as sales forecast.
- Distributor margins forgotten, so the shelf price is too high.
- Certifications needed for the main channel not yet planned or budgeted.
- Materials and stock financed with no working-capital line.

## Typical risks and mitigations
Input price spikes → contracts, alternative recipes · machine breakdown → maintenance plan, spare parts · retailer delistings → several channels · quality incident → testing, traceability, insurance.

## Fictional mini-example
Tamu Juice (fictional), Nairobi: one bottle costs 75 KES (fruit 38, bottle and label 22, labour 10, energy 5) and sells to distributors at 110 KES, leaving 35 KES. The line can fill 1200 bottles a day; selling 700 a day uses 58% of capacity, so fixed costs per bottle fall as sales grow.

## Hybrids
Manufacturing + trade-distribution (exporting own products: add export costs and longer payment terms) · manufacturing + ecommerce-d2c (selling online too: separate margins per channel).
