# Rubric: 11 dimensions, anchors, weights and verdicts

## Contents
- Dimensions and anchors
- Weights by reader
- Verdict rules
- Scoring tips

## Dimensions and anchors

Score each dimension 1–5. Quote the plan for every score. Anchors describe what the plan shows, not how good the business idea sounds.

### problem_customer — Problem and customer
1. "Everyone" as customer; problem asserted with no evidence.
2. Segments named but broad; problem described from the founder's view.
3. One priority segment; problem plausible with some interviews or data.
4. Specific segment and persona; problem quantified (frequency, cost) with interviews or data.
5. As 4, plus customers already paying for workarounds or for this offer; evidence level 4–5.

### value_proposition — Offer and value proposition
1. Features only; no clear customer outcome.
2. Benefits claimed with superlatives; no link to alternatives.
3. Clear offer and benefits; difference from alternatives stated.
4. One-sentence value proposition with customer, result, alternative and proof.
5. As 4, with measured results from real customers and a credible "why now".

### market — Market
1. Market size missing or "1% of a huge market".
2. Big figures without sources or with the wrong geography.
3. TAM/SAM/SOM with some sources; method unclear.
4. Sourced top-down and bottom-up; SOM tied to capacity; dates and currency stated.
5. As 4, plus trends and rules researched with sources; forecast well inside SOM or explained.

### competition — Competition and positioning
1. "No competitors."
2. Competitors listed without comparison.
3. Comparison on some criteria; positioning stated.
4. Honest comparison on customer criteria with sources and dated prices; clear positioning.
5. As 4, plus a durable advantage with proof that grows over time.

### business_model — Business model and pricing
1. Revenue model unclear or price below cost.
2. Prices stated without cost basis.
3. Prices cover unit cost; main revenue stream clear.
4. Prices justified by cost floor, alternatives and value; unit economics complete (all variable costs); payment terms stated.
5. As 4, plus proven unit economics from real sales (and LTV/CAC with measured churn for repeat models).

### go_to_market — Go-to-market and sales
1. "Social media" and "word of mouth" with no plan.
2. Channel list with no costs or funnel.
3. Focused channels with estimated costs; targets stated.
4. Funnel with conversion rates, CAC by channel, targets matching the forecast and capacity.
5. As 4, with tested channels and measured CAC or conversion.

### operations_team — Operations and team
1. Unclear who delivers what; no team detail.
2. Activities and team listed; gaps ignored.
3. Key activities, resources and suppliers clear; team roles defined; obvious gaps named.
4. Capacity checked against demand; supplier risks covered; team with relevant results and a costed hiring plan.
5. As 4, with a track record of delivery and full-time commitment of key people.

### validation — Validation and traction
1. No customer contact.
2. Opinions and surveys only (levels 0–2).
3. Interviews with the right segment and some commitments (level 3).
4. Paid sales or paid pilots (level 4) with metrics.
5. Repeat purchases or retention over months (level 5) with trends.

### financials — Financial plan
1. Missing, or numbers that contradict each other.
2. Totals without assumptions; profit only, no cash flow.
3. Driver-based forecast with costs and cash flow; some assumptions stated.
4. Monthly cash flow with the low point, break-even, funding need and use of funds that add up; assumptions labelled; downside case.
5. As 4, with figures grounded in actual results and sensitivity on key drivers; repayment capacity or runway clearly shown.

### risks_execution — Risks and execution
1. Risks absent or generic.
2. Risks listed with no mitigation.
3. Main risks with mitigations; milestones stated.
4. Risk register with likelihood, impact, triggers and owners; dated action plan with owners.
5. As 4, with the downside case linked to triggers and responses, and KPIs to monitor.

### impact — Impact (grant and social-enterprise plans only)
1. Impact claimed with no measures.
2. Activities counted as impact.
3. Outcomes named with indicators.
4. Theory of change with indicators, baselines, targets and measurement method.
5. As 4, with outcomes already measured and a plan to sustain them after the grant.

## Weights by reader

Each row sums to 100. `python3 scripts/score_plan.py --weights` prints the same table.

| Dimension | incubator | bank | investor | grant | internal | partner |
|---|---|---|---|---|---|---|
| problem_customer | 12 | 6 | 12 | 10 | 8 | 8 |
| value_proposition | 10 | 6 | 10 | 8 | 8 | 12 |
| market | 8 | 6 | 12 | 4 | 6 | 8 |
| competition | 8 | 6 | 8 | 4 | 8 | 8 |
| business_model | 10 | 12 | 12 | 8 | 12 | 12 |
| go_to_market | 10 | 8 | 10 | 6 | 14 | 14 |
| operations_team | 10 | 14 | 12 | 12 | 14 | 14 |
| validation | 14 | 8 | 10 | 8 | 8 | 8 |
| financials | 10 | 26 | 8 | 12 | 14 | 10 |
| risks_execution | 8 | 8 | 6 | 8 | 8 | 6 |
| impact | 0 | 0 | 0 | 20 | 0 | 0 |

## Verdict rules

Weighted score (0–100) = sum over rated dimensions of score ÷ 5 × weight, rescaled to 100 if some weighted dimensions are not rated.
- **Ready:** 80 or more and no blocking finding.
- **Nearly ready:** 65–79 with no blocking finding, or 80+ with exactly one blocking finding that is a quick fix.
- **Needs work:** 45–64, or any other blocking finding.
- **Not ready:** below 45.

## Scoring tips

- Score what is on the page. A strong business with a weak plan scores low; say so kindly.
- One dimension at a time, with a quote; avoid letting one weakness lower every score.
- When in doubt between two scores, choose the lower and say what would raise it.
- A blocking finding overrides a high score: the verdict rules already handle this.
