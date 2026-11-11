# Module 7: Operations and resources (`operations`)

This module must show the business can deliver what it sells, at the planned volume and cost: the activities, resources, suppliers, premises and legal set-up. Banks read it to judge whether the cash flow is achievable.

## Order and depth

Banks: early (after offer and customer). Investors: shorter, focused on scale. Quick draft: activities and resources.

## Sections

### operations.activities — Key activities
- **Ask:** What are the few activities you must do very well every week to deliver your offer?
- **Help them think:** making or sourcing · selling · delivering or serving · quality control · customer support · admin.
- **Done when:** 4–6 activities, who does each, and which ones are outsourced.
- **Common mistakes:** listing every task · forgetting sales and collection as activities.
- **Teach:** Key activities and resources
- **Length:** a short list.

### operations.resources — Key resources
- **Ask:** Which resources do you need: people, equipment, premises, technology, licences, money? Which do you have now?
- **Done when:** resources split into "have" and "need", with cost and timing for each need (feeds financials.costs and capex).
- **Teach:** Key activities and resources · Capital spending and depreciation
- **Labels:** owned assets Verified; purchases Planned with quotes if possible.
- **Length:** a have/need table.

### operations.suppliers — Suppliers
- **Ask:** Who supplies your main inputs, on what terms, and what happens if one fails?
- **Help them think:** top 3 inputs by cost · price and minimum order quantity · lead time · payment terms · a backup supplier.
- **Done when:** main suppliers (or supplier types), terms, minimum orders and a backup for each critical input.
- **Common mistakes:** one supplier for a critical input with no backup · ignoring minimum orders that tie up cash.
- **Teach:** Suppliers and minimum order quantity · Payment terms and working capital
- **Feeds and checks:** model.payment_terms (`payment_days`, `inventory_days`), risks.register.
- **Length:** a short table.

### operations.location_equipment — Location and equipment
- **Ask:** Where will you operate, and what equipment do you need, at what cost?
- **Method:** list each item with cost, purchase month and useful life for the model's capex lines; check capacity with `bizcalc.py capacity --capacity C --demand D` and save `capacity.<name>` and `demand.<name>` for C02.
- **Done when:** location with monthly rent and lease terms, equipment list with costs (quotes where possible), capacity per day or month.
- **Common mistakes:** capacity based on the machine's label, not real shifts and staff · no maintenance costs.
- **Teach:** Capacity and utilisation · Capital spending and depreciation
- **Length:** a short table.

### operations.legal — Legal and compliance
- **Ask:** What legal form will the business take, and which registrations, licences, insurance and contracts are needed?
- **Help them think:** company form and ownership · tax registration · sector licences · insurance · customer and supplier contracts · data protection · intellectual property.
- **Done when:** a checklist with status and owner; questions for a lawyer or accountant listed, not answered as advice.
- **Teach:** Licences and compliance · Tax questions for an accountant
- **Feeds and checks:** market.regulation, risks.register.
- **Length:** a checklist.

## Module summary

Show what is delivered, by whom and with what; capacity against demand (C02); supplier risks; legal status and open legal questions.
