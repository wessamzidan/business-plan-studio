# Module 6: Go-to-market and sales (`gtm`)

This module must show exactly how customers will hear about the business, buy and come back, at what cost, and how that turns into the sales targets in the forecast. Readers distrust targets with no funnel behind them.

## Contents
- Order and depth
- Sections: gtm.channels · gtm.marketing · gtm.sales_process · gtm.partnerships · gtm.targets
- Module summary
- Hand-offs

## Order and depth

After pricing. Investors and incubators read it closely; banks check targets against the forecast. Quick draft: channels and targets.

## Sections

### gtm.channels — Channels
- **Ask:** Through which two or three channels will you reach and sell to your priority customers first?
- **Why it matters:** focus on a few channels you can afford and measure beats a list of ten.
- **Options when stuck (by type):** services: referrals, LinkedIn, partnerships, events · saas-subscription: content and search, product-led trials, partner resellers · ecommerce-d2c: social ads, influencers, marketplaces · retail-store and food-service: location and footfall, delivery apps, local social media · manufacturing and trade-distribution: distributors, trade fairs, direct sales to buyers · marketplace-platform: one side first (usually supply), then demand · appointment-experience: maps listings, referrals, packages · social-enterprise: community partners, institutions.
- **Done when:** 2–3 channels, each with why it fits the persona, cost per month or per customer (CAC estimate) and how it is measured.
- **Common mistakes:** "social media" with no plan · channels the persona does not use · no cost.
- **Teach:** Sales channels · Customer acquisition cost (CAC)
- **Labels:** CAC from tests Verified; otherwise Estimate with method.
- **Length:** a short table.

### gtm.marketing — Marketing plan
- **Ask:** What will you do in the first 90 days to get attention and leads, and what will it cost?
- **Help them think:** message (from the value proposition) · content or offers · monthly budget · who does it · what you will measure.
- **Done when:** 3–6 concrete activities with monthly budget and owner; the budget appears in financials.costs.
- **Common mistakes:** a big brand campaign before product proof · no budget line in the forecast.
- **Teach:** Marketing funnel and conversion rate
- **Length:** a 90-day table.

### gtm.sales_process — Sales process
- **Ask:** Walk me through how a stranger becomes a paying customer: each step, how long it takes and how many drop out.
- **Why it matters:** the funnel turns marketing spend into a believable number of customers.
- **Help them think:** stages (aware, interested, trial or quote, purchase, repeat) · conversion between stages · sales cycle length · who sells.
- **Method:** funnel math: leads × conversion % = customers; compute with `bizcalc.py pct` and save the rates as assumptions.
- **Done when:** stages with conversion rates (labelled), cycle length, and who is responsible.
- **Common mistakes:** conversion rates from articles about other countries or industries · ignoring repeat purchase.
- **Teach:** Sales process and pipeline · Marketing funnel and conversion rate
- **Length:** a funnel table plus 2 lines.

### gtm.partnerships — Partnerships
- **Ask:** Which partners could bring you customers or lower your costs, and what do they get in return?
- **Options:** distributors, resellers, complementary businesses, associations and chambers, platforms, suppliers offering credit, public support programmes.
- **Done when:** 2–4 partners, with the mutual benefit and status (talking, agreed, signed).
- **Common mistakes:** naming famous partners with no contact · no benefit for the partner.
- **Labels:** signed agreements Verified; talks Planned.
- **Length:** a short table.

### gtm.targets — Sales targets
- **Ask:** What are your sales targets for months 3, 6 and 12 (customers, units and revenue)?
- **Why it matters:** targets are what you will be judged on; they must match the forecast and the funnel.
- **Method:** derive targets from the funnel (leads × conversion) and capacity; compare with the forecast month by month. Save `target.<YYYY-MM>` values for C04.
- **Done when:** targets for at least three dates, in units and revenue, matching the forecast within about 10% (C04) and within capacity (C02).
- **Common mistakes:** round-number targets with no funnel · targets that differ from the financial forecast.
- **Teach:** Sales targets
- **Length:** a 3-row table.

## Module summary

Show channels with CAC, the 90-day marketing plan, the funnel, partners and targets, plus C02 and C04 results.

## Hand-offs

Channel cost assumptions feed business-plan-financials (marketing budget and CAC in subscription streams).
