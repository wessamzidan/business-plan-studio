# Module 3: Market (`market`)

This module must show the market is big enough for the plan's goals, how it is changing, and which rules apply. Every outside figure needs a source and a date; an unsourced market size is worse than none.

## Order and depth

Investors read this early; banks and incubators want a sensible size and the rules; internal plans keep it short. Quick draft: write the method and mark figures To confirm.

## Sections

### market.size — Market size
- **Ask:** How many potential customers are there in the area you can serve, and how much does each spend a year on this need?
- **Why it matters:** readers check the market can support your revenue goals, and that you understand which part of it you can actually reach.
- **Help them think:** count customers, not just currency · narrow from everyone (TAM) to those you can serve (SAM) to what you can win in 2–3 years (SOM) · build SOM bottom-up from your sales capacity.
- **Method (minimum):** top-down (a sourced starting population × sourced filters × yearly spend) and bottom-up (customers you can reach × conversion × yearly value, capped by capacity). Run `scripts/market_size.py` with every input's source. Use the lower SOM.
- **Done when:** TAM, SAM and SOM, each with method, currency, year, source and label; year-1 revenue in the forecast is at most the SOM (check C03), usually well below.
- **Common mistakes:** "if we get 1% of a huge market" · global figures for a local business · counting the same spend twice · no year or currency.
- **Teach:** TAM, SAM and SOM · Top-down and bottom-up sizing · Citing sources
- **Labels:** sourced figures Verified (with link and date); filters and conversion usually Estimate.
- **Feeds and checks:** C03 with `forecast.revenue_y1`; save `plan_state.py num market.som VALUE --label Estimate`.
- **Length:** a 3-row table plus 2–4 lines of method.

### market.trends — Trends
- **Ask:** What is changing in this market that helps or hurts you over the next three years?
- **Why it matters:** shows the founder looks ahead; trends support "why now" and growth assumptions.
- **Help them think:** demand (habits, population, spending) · supply (new entrants, costs) · technology · rules · prices.
- **Done when:** 2–4 trends, each with a source or "To confirm", and what it means for this business.
- **Common mistakes:** generic world trends · trends that do not touch the plan's numbers.
- **Teach:** Market trends and timing · Citing sources
- **Length:** 3–4 bullets.

### market.regulation — Rules and licences
- **Ask:** Which licences, permits or rules apply to this business, and where are you with each?
- **Why it matters:** an unlicensed activity can stop the business; banks and grant readers check compliance.
- **Help them think:** business registration and tax registration · sector licences (food, health, education, finance, transport) · product standards and labelling · import or export rules · data protection · employment rules.
- **Done when:** a list with status (have / applied / to apply / to check), cost and time where known; legal questions flagged for a lawyer or accountant.
- **Common mistakes:** "no licences needed" without checking · stating a rule from memory.
- **Teach:** Licences and compliance · Tax questions for an accountant
- **Labels:** rules need a dated official source; otherwise To confirm.
- **Feeds and checks:** operations.legal, risks.register, financials.costs (licence fees).
- **Length:** a short table.

## Module summary

Show the TAM, SAM, SOM table with sources and labels, the trends that matter, the licence checklist and the research tasks still open.

## Hand-offs

Full sizing, competitor scans and rules research: business-plan-market-research when installed. Without it: search only if web search is available, open each page before citing it, and record title, publisher, link and date.
