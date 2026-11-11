# Business type: Import, export, wholesale and distribution

Covers exporters and importers, trading companies, wholesalers, distributors, sourcing agents and commission-based trade intermediaries.

## How money is made
Buying goods and selling them on with a margin, or earning a commission for connecting buyers and sellers. Margins are thin, so landed cost, exchange rates, payment terms and the working-capital cycle decide survival.

## Key drivers and metrics
| Metric | Formula | Why it matters | Sections |
|---|---|---|---|
| Landed cost | purchase + packing + transport + insurance + duties + fees | Real cost per unit | model.unit_economics |
| Gross margin per shipment | sales value − landed cost | The whole profit pool | model.pricing |
| Shipments per year | containers, pallets or orders | Volume driver | financials.forecast |
| Cash cycle | days stock is held + days customers take − days suppliers give | Working capital need | model.payment_terms |
| FX exposure | sales or costs in foreign currency | Margin can vanish with rate moves | risks.register |
| Buyer concentration | largest buyer ÷ sales | Risk | risks.register |

## Sharpest questions
- `model.unit_economics`: Build the cost per unit up to the point of sale named in your terms (for example FOB or CIF): what is included?
- `model.payment_terms`: When do you pay suppliers, and when do buyers pay (advance, letter of credit, 30–90 days)?
- `customer.priority_segment`: Which country and buyer type first, and why that market?
- `validation.evidence`: Which buyers have received samples, sent purchase orders or paid?
- `operations.suppliers`: How do you secure consistent quality and volume from suppliers?
- `operations.legal`: Which export or import registrations, certificates, standards and labels are needed for the target market?
- `risks.register`: How do you check a new buyer before sending samples, documents or goods on credit?
- `financials.funding`: How much cash is tied up per shipment, and for how many days?
- `market.size`: What do trade statistics show about imports of this product into the target market (cite the source)?
- `gtm.channels`: Trade fairs, export councils, B2B platforms, agents or direct outreach?

## Options to offer
- Revenue: margin on goods · commission or agency fee · services (sourcing, inspection, logistics).
- Payment security: advance payment · letter of credit · documentary collection · credit insurance (ask a bank).
- Channels: trade fairs, trade missions, export promotion bodies, B2B platforms, distributors abroad.

## Model template
Driver tree: shipments per month × volume per shipment × price; landed cost per unit as unit cost; long collection days; stock bought ahead; exchange rate stated as an assumption. Use a `units` stream per market and timing fields.
```json
{"name": "Zitouna Export (fictional)", "currency": "TND", "start": "2027-01", "months": 24,
 "opening_cash": 400000, "payment_days": 0, "inventory_days": 15,
 "streams": [{"name": "Bottled olive oil (FOB)", "type": "units", "volume": {"schedule": [0, 18000, 0, 18000, 0, 18000, 0, 18000, 18000, 0, 18000, 18000]},
   "price": 21, "unit_cost": 17.5, "collection_days": 60}],
 "fixed_costs": [{"name": "Office, fairs and samples", "monthly": 9000}],
 "team": [{"role": "Export manager", "count": 1, "monthly_salary": 4500}],
 "financing": [{"type": "loan", "amount": 300000, "month": "2027-01", "rate_pct": 10, "term_months": 12, "grace_months": 0}]}
```

## Capacity and operations
Capacity is working capital, supplier volume and documentation speed, not warehouse space. Ask how many shipments the team can handle at once.

## Convincing evidence
Level 2: buyer meetings at fairs · Level 3: sample requests from verified buyers, signed pro-forma invoices · Level 4: shipments paid · Level 5: repeat orders from the same buyers.

## Red flags reviewers spot
- Landed cost missing insurance, port fees, certificates or bank charges.
- Selling on credit to new foreign buyers with no verification or security.
- Exchange rate not stated, or one rate used for all years.
- Margins of a few percent with large fixed costs.
- Market size from global production instead of the target market's imports.

## Typical risks and mitigations
Buyer default or fraud → verify buyers (registration, references, trade records) before samples or credit; advance payment or letters of credit · FX moves → price in a stable currency, hedge with the bank · quality rejection → inspections and certificates · shipping delays → buffer time, clear contracts.

## Fictional mini-example
Zitouna Export (fictional), Tunis: olive oil costs 17.5 TND a litre ready for shipment (oil 13.5, bottling 3.2, transport and port 0.8) and sells FOB at 21 TND: 3.5 TND a litre, 16.7%. One 18000-litre container earns 63000 TND but ties up 315000 TND until the buyer pays 60 days after shipping.

## Hybrids
Trade + services (sourcing agent with fees) · trade + manufacturing (own brand produced by a contract packer).
