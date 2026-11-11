# Business type: E-commerce and direct-to-consumer brands

Covers online stores, brands selling through their own site, Instagram, TikTok or WhatsApp shops, marketplace sellers (Amazon, Noon, Jumia and similar) and subscription boxes sold per order.

## How money is made
Orders. Each order brings an average order value (AOV); after product, packaging, delivery, payment fees, returns and discounts, what is left must pay for winning the customer (CAC) and fixed costs. Repeat purchases decide profitability.

## Key drivers and metrics
| Metric | Formula | Why it matters | Sections |
|---|---|---|---|
| Traffic and conversion | orders = visitors × conversion rate | Main volume driver | gtm.sales_process |
| AOV | revenue ÷ orders | Spreads delivery and CAC | model.pricing |
| Contribution per order | AOV − product − packaging − delivery − fees − returns (`bizcalc.py unit-margin`) | The real margin | model.unit_economics |
| CAC by channel | spend on a channel ÷ new customers from it | Which channels to scale | gtm.channels |
| Repeat rate | customers ordering again within 6 months ÷ all customers | Turns a loss on first order into profit | validation.metrics |
| Return rate | returned orders ÷ orders | Fashion and electronics risk | model.unit_economics |
| Stock cover | stock value ÷ monthly cost of goods sold | Cash tied in inventory | model.payment_terms |

## Sharpest questions
- `model.unit_economics`: After product, packaging, delivery, payment fees and returns, what is left from one order?
- `model.pricing`: What is your average order value, and how do you raise it (bundles, free-delivery threshold)?
- `gtm.channels`: What does one new customer cost on each channel, measured, not guessed?
- `validation.metrics`: What share of first-time buyers order again within 3 and 6 months?
- `operations.suppliers`: What is the minimum order quantity and lead time for your top product?
- `model.payment_terms`: Cash on delivery, cards or wallets? How many cash-on-delivery orders are refused?
- `operations.location_equipment`: Who stores, packs and ships: you, a warehouse partner or the marketplace?
- `financials.forecast`: What monthly ad budget drives the forecast, at what CAC?
- `competition.competitors`: Which brands and marketplaces sell the same product, at what price?
- `risks.register`: What happens if ad costs rise 30%?

## Options to offer
- Channels: social ads · creators and influencers · marketplaces · WhatsApp and community selling · search · retail partners later.
- Pricing: single products · bundles · subscriptions for refills · free delivery above a threshold.
- Fulfilment: in-house · third-party warehouse · marketplace fulfilment · dropshipping (low margin).

## Model template
Driver tree: orders = new customers + repeat orders; new customers = ad budget ÷ CAC; revenue = orders × AOV; variable costs = delivery, fees and returns as % of revenue. Use a `units` stream for orders (AOV as price, product and packaging as unit cost, fees as `variable_pct`) and a fixed marketing budget, or model repeat buyers with a `subscription` stream.
```json
{"name": "Shea & Co (fictional)", "currency": "NGN", "start": "2027-01", "months": 12,
 "opening_cash": 3000000, "inventory_days": 60,
 "streams": [{"name": "Online orders", "type": "units", "volume": {"start": 250, "growth_pct": 8, "max": 1500},
   "price": 18000, "unit_cost": 6500, "variable_pct": 15.4}],
 "fixed_costs": [{"name": "Ads", "monthly": 1500000, "category": "marketing"},
                 {"name": "Storage and tools", "monthly": 250000}],
 "team": [{"role": "Operations and customer care", "count": 2, "monthly_salary": 250000}]}
```

## Capacity and operations
Packing speed, storage space and delivery partners cap volume. Stock must be ordered weeks or months before sales: set `inventory_days` and check the cash low point.

## Convincing evidence
Level 3: pre-orders or a waitlist with deposits · Level 4: first orders from paid ads at a measured CAC · Level 5: repeat rate and reviews over several months.

## Red flags reviewers spot
- Contribution per order calculated without delivery, returns or payment fees.
- CAC assumed from industry articles; no test spend.
- All growth from ads with no repeat purchases.
- Stock bought for 12 months upfront, draining cash.
- Cash-on-delivery refusals ignored.

## Typical risks and mitigations
Ad costs rise → build email, WhatsApp and community channels · stock-outs or overstock → smaller, more frequent orders · copycats on marketplaces → brand, reviews, bundles · delivery failures → two courier partners.

## Fictional mini-example
Shea & Co (fictional), Lagos: an 18000 NGN average order leaves 8730 NGN (48.5%) after product 6000, delivery 2500, payment fees 270 and packaging 500. With a 6000 NGN CAC, a first order earns 2730 NGN towards fixed costs; repeat orders, with no CAC, carry the profit.

## Hybrids
E-commerce + retail-store (online plus a shop: two `units` streams with different margins) · E-commerce + manufacturing (own production: add capex and batch costs).
