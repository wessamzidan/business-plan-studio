# Module 5: Business model and pricing (`model`)

This module must show how money comes in, at what price, with what margin per sale, and on what payment terms. It is where many plans quietly lose money on every unit; check it with the scripts, not by eye.

## Contents
- Order and depth
- Sections: model.revenue_streams · model.pricing · model.unit_economics · model.payment_terms
- Module summary
- Hand-offs

## Order and depth

Before the financial plan, after customer and offer. Banks and investors read this closely. Quick draft: revenue streams and pricing with labels.

## Sections

### model.revenue_streams — Revenue streams
- **Ask:** In which ways will customers pay you? List each revenue stream and roughly what share of income it will bring in year one.
- **Why it matters:** the revenue model decides the forecast drivers, cash timing and risk.
- **Options when stuck (by type):** services: hourly, project, retainer, success fee · saas-subscription: monthly or yearly plans, tiers, setup fees · ecommerce-d2c and retail-store: product sales, bundles, delivery fees · food-service: dine-in, delivery, catering, events · manufacturing: wholesale, private label, export · trade-distribution: margin on goods, commission · marketplace-platform: take rate, listing fees, ads · appointment-experience: per visit, packages, memberships · social-enterprise: sales plus grants and donations.
- **Done when:** 1–4 streams, each with its unit of sale and expected share; the main stream is clear.
- **Common mistakes:** too many streams for a new business · ad revenue with no audience.
- **Teach:** Revenue models
- **Feeds and checks:** financials.forecast (each stream becomes a model stream).
- **Length:** a short table.

### model.pricing — Pricing
- **Ask:** What price will you charge for each offer, and how did you set it?
- **Why it matters:** price must cover cost, fit what customers pay for alternatives and match the positioning.
- **Help them think:** cost-plus floor (what it costs you plus margin) · competitor and alternative prices · value to the customer · price per unit, per month or per project · with or without VAT or sales tax.
- **Method:** compute the floor first. Products: `bizcalc.py unit-margin --price P --unit-cost C`. Time-based services: `bizcalc.py min-price --fixed F --hours H --task-hours T --direct D --price P`. Mark-up and margin: `bizcalc.py markup-margin`.
- **Done when:** each offer has a price, a stated basis (cost, competitor scan with date, value), tax treatment, and passes C01 (price above unit cost or minimum price). Save `offer.<name>.price` and `offer.<name>.unit_cost` or `.min_price`.
- **Common mistakes:** pricing below cost to win customers with no plan to raise prices · copying a competitor's price without knowing their costs · mixing prices with and without tax.
- **Teach:** Pricing strategies · Gross margin and markup · Cost per hour and minimum price
- **Labels:** prices already charged Verified; planned prices Planned; competitor prices Verified with date.
- **Length:** a price table plus 2–3 lines on the basis.

### model.unit_economics — Unit economics
- **Ask:** For one sale (or one customer), how much do you keep after the direct costs of that sale?
- **Why it matters:** if each sale loses money, more sales make it worse; readers check this before growth plans.
- **Method by type:** contribution per unit or order (`bizcalc.py unit-margin`, include delivery, packaging, payment and platform fees as `--variable-pct`) · subscription and repeat models: CAC, LTV, LTV/CAC and payback (`bizcalc.py ltv-cac`) · services: margin per project at the planned rate · marketplaces: take rate minus cost per transaction.
- **Done when:** contribution per unit and margin %, plus LTV/CAC and payback for repeat models (C09), with each input labelled. Save `unit.ltv`, `unit.cac`, `unit.payback_months` where relevant.
- **Common mistakes:** leaving out payment fees, delivery, returns or discounts · using revenue instead of margin in LTV · CAC with only ad spend.
- **Teach:** Unit economics · Contribution margin · Customer acquisition cost (CAC) · Customer lifetime value (LTV) · LTV to CAC ratio and payback
- **Length:** 3–6 lines or a small table.

### model.payment_terms — Payment terms
- **Ask:** When do customers pay you, and when do you pay suppliers?
- **Why it matters:** profit on paper can still run out of cash if customers pay late or stock is bought early.
- **Options:** cash on order · deposit plus balance · 30, 60 or 90 days · monthly in advance · marketplace payouts on a schedule · letters of credit (trade).
- **Done when:** customer terms and supplier terms are stated per main stream; they feed `collection_days`, `payment_days` and `inventory_days` in the model.
- **Common mistakes:** assuming everyone pays on day one · forgetting stock bought months before sales.
- **Teach:** Payment terms and working capital
- **Length:** 2–4 lines.

## Module summary

Show the revenue streams, the price table with floors and C01 results, unit economics with labels, and payment terms. Name the main driver of the forecast.

## Hand-offs

Full model and pricing scenarios: business-plan-financials when installed; otherwise build a simple model with `scripts/fin_model.py`.
