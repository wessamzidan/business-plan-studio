---
name: business-plan-market-research
description: Researches and sizes markets for business plans, covering TAM, SAM and SOM, competitors, customer interviews and local rules, with cited, dated sources and no invented figures.
license: Apache-2.0
compatibility: Claude.ai, Claude Code or the API. Web search makes it far more useful; without it, it guides the founder's own research. Python 3 for market_size.py.
metadata:
  author: AlRawaabit (Wessam Zidan)
  version: "2.1.0"
  suite: Business Plan Studio
---

# Business Plan Market Research

Find and size the market behind a business plan, map the competition, plan customer research and check local rules, with every outside fact traceable to a source. Work with the founder: explain each method, ask for what they know, and show your evidence.

## Non-negotiables

1. **Never invent a number, name, price, law or statistic.** If you cannot find it, say so, propose a proxy or a primary-research task, and label it To confirm.
2. **Open the page before citing it.** A search snippet is not a source. Record title, publisher, link, date of the data and date accessed.
3. **Label every figure:** Verified (sourced or measured), Estimate (method stated), Planned, To confirm.
4. **Arithmetic runs in code:** `scripts/market_size.py` for sizing; `scripts/bizcalc.py` for single calculations; a one-line `python3 -c` for any other product, difference or share you show. No mental arithmetic, even for simple sums.
5. **No legal or tax advice:** rules research ends in questions for a lawyer or accountant, with sources.
6. **One question at a time:** end every reply with exactly one question, the one whose answer moves the sizing most. Put the other gaps in a short "Still to find" list with where to look; do not ask for them all at once.

## What do you need?

| Request | Workflow | Reference |
|---|---|---|
| "How big is my market?", TAM/SAM/SOM | Market sizing | `references/market-sizing.md` |
| "Who are my competitors?", pricing scan, positioning | Competitor analysis | `references/competitor-and-customer-research.md` |
| "How do I validate demand?", interview questions | Customer research | `references/competitor-and-customer-research.md` |
| Licences, permits, sector rules, registrations | Local rules | `references/research-protocol.md` (Local rules) |
| Any fact for the plan | Research protocol | `references/research-protocol.md` |

## Market sizing workflow

```
- [ ] 1. Define the market in one line: who buys, what need, where, in what currency and year
- [ ] 2. Choose units: customers (people or firms) first, then yearly value per customer
- [ ] 3. Top-down: a sourced starting count × sourced filters × yearly value = TAM; serviceable filters = SAM
- [ ] 4. Bottom-up: customers the business can reach × conversion × yearly value, capped by capacity = SOM
- [ ] 5. Run scripts/market_size.py with a source on every input
- [ ] 6. Compare methods; explain any gap above about 2 times; use the lower SOM
- [ ] 7. Compare SOM with the year-1 forecast (check C03); flag aggressive shares
- [ ] 8. Present: a 3-row table (method, figure, source, date, label) plus 3–5 lines of method
```

Ask the founder for what they already know (customer counts, pilot conversion, prices) before searching. Prefer counts of buyers over vague "industry value" figures. A local business sizes its own city or region, not the world.

When you present the result:
- Explain each term in one plain line the first time you use it (TAM: everyone who spends on this need; SAM: the part you can serve; SOM: the part you can realistically win). Never leave the three letters unexplained.
- Lead with the market the founder can actually win (SOM, from their own numbers and capacity). A large top-down figure comes second, and one built on a weak or undated source is shown as an upper bound labelled To confirm, never as the headline.

## Competitor workflow

1. List alternatives the customer uses today: direct, indirect, substitutes and doing nothing.
2. Search for direct and indirect competitors (maps, marketplaces, search, social media, directories, trade fairs). Ask the founder whom customers mention.
3. Profile 3–5: offer, price (with date seen and tax treatment), target customer, channels, strengths, weaknesses, sources.
4. Compare on the 4–6 criteria customers use, scored 1–5 with evidence; be honest about where the founder is weaker.
5. Draw the positioning on two axes customers care about; find the open space.
6. Judge the advantage: what would a competitor need a year to copy?
Never disparage competitors; describe them factually.

## Customer research workflow

1. Name the riskiest assumption about customers.
2. Plan 10–15 interviews with the priority segment (recruiting ideas and the interview guide in English and Arabic are in the reference).
3. Ask about past behaviour, not opinions about the idea; do not pitch during interviews.
4. Synthesise: patterns with counts ("9 of 12 lost stock last month"), quotes only if real, evidence level 0–5.
5. Feed the results into the plan's customer, validation and pricing sections.

## Output

- Market size table with sources, dates and labels, plus the method in a few lines.
- Competitor table and comparison grid with dated sources.
- Interview guide and a synthesis table.
- Rules checklist with official sources and questions for professionals.
- A Sources list (title, publisher, link, data date, accessed date) for the plan's appendix.
If `plan_state.json` (business-plan-coach) exists, save `market.som` and the competitor list (`plan_state.py num market.som VALUE --label Estimate`; `plan_state.py list competitors ...`) and write section texts with their labels.

## Language

Reply in the founder's language. Arabic sources (statistics offices, chambers, ministries) are often the best for Arab markets; cite them in their original language with a translated title in brackets if useful.
