# Review report template

## Contents
- Report structure
- Questions each reader asks
- Filled example (fictional bakery, bank review)

## Report structure

1. **Verdict line:** "Verdict for a [reader]: [Ready / Nearly ready / Needs work / Not ready] · score [n]/100 · [b] blocking, [m] major, [n] minor findings."
2. **In one paragraph:** what the plan does well and the one thing that most affects the reader's decision.
3. **Top three fixes,** ranked by impact on the reader's decision; each with what to change and how long it takes.
4. **Scorecard:** dimension · score 1–5 · weight · one-line evidence (quote with page or slide).
5. **Findings:** severity · module or section · finding · why the reader cares · suggested fix.
6. **Numbers check:** each rechecked figure: plan says · recomputed · status (matches, mismatch, cannot check), plus C01–C14 results if a state file exists.
7. **Questions the reader will ask,** each with what to prepare.
8. **Strengths:** three to five specific strengths with evidence.
9. **Next steps:** offer to fix the top items one by one, rebuild the numbers, or rehearse the reader's questions.

## Questions each reader asks

- **Incubator:** Who have you spoken to, and what changed because of it? What is your riskiest assumption and how will you test it? Are both founders full-time? What do you need from us?
- **Bank:** How will you repay if sales are 25% lower? What is your own contribution? What collateral or guarantees can you offer? Do you have all licences? How long do customers take to pay?
- **Investor:** How big can this get, and why now? What traction proves demand? What are your unit economics today? Why is this team the one to win? How long will the money last, and which milestones will it reach?
- **Grant:** Who benefits, and how will you measure it? Why is this cost per beneficiary reasonable? How does the project continue after the grant? Which costs are eligible?
- **Partner:** What volumes, when? What do we gain? How reliable are you?

## Filled example (fictional bakery, bank review)

**Verdict for a bank: Needs work · score 57/100 · 1 blocking, 3 major, 2 minor findings.**

Sweet Crumb Bakery (fictional), Amman, asks for a 30000 JOD loan for an oven and fit-out. The plan describes the product and the founders' baking experience well, but the cash flow does not show how the loan is repaid: cash falls below zero in months 4–7 even after the loan.

**Top three fixes**
1. Rebuild the cash flow with the oven purchase in month 1 and supplier payment terms; size the loan from the cash low point plus a buffer (half a day with the coach or the financials skill).
2. Add a downside case (sales 25% lower) with the loan instalment and debt service coverage.
3. Replace the market size taken from a national bakery figure with a bottom-up count of the cafés and shops in the delivery area.

**Scorecard**

| Dimension | Score | Weight | Evidence |
|---|---|---|---|
| problem_customer | 3 | 6 | p.3: "cafés in Abdoun and Sweifieh complain about late deliveries" (8 interviews) |
| value_proposition | 3 | 6 | p.4: "fresh before 7 a.m. every day" |
| market | 2 | 6 | p.5: national bakery market, no source |
| competition | 3 | 6 | p.6: three competitors with prices, undated |
| business_model | 4 | 12 | p.7: unit cost 0.35 JOD, price 0.80 JOD (rechecked: 56.3% margin) |
| go_to_market | 3 | 8 | p.8: direct visits; no conversion rates |
| operations_team | 4 | 14 | p.9: 12 years' baking; supplier backup named |
| validation | 3 | 8 | p.10: 5 cafés trial orders, unpaid |
| financials | 2 | 26 | p.12: cash below zero in months 4–7 after the loan |
| risks_execution | 2 | 8 | p.14: two generic risks |

(`score_plan.py` result: 57; rated weight 100.)

**Findings**

| Severity | Section | Finding | Why the bank cares | Fix |
|---|---|---|---|---|
| Blocking | financials.cash_flow | Cash below zero in months 4–7 after the loan | Repayment is not covered | Re-size the loan from the low point plus buffer |
| Major | financials.scenarios | No downside case | Banks test repayment in a bad case | Add sales −25% with instalment and DSCR |
| Major | market.size | National figure, no source | Doubt spreads to other numbers | Bottom-up count in the delivery area |
| Major | validation.evidence | Trial orders were free | No proof cafés will pay the price | Convert 3 trial cafés to paid weekly orders |
| Minor | risks.register | Risks without mitigation | Shows limited planning | Add likelihood, impact, triggers, owners |
| Minor | summary.executive | Loan amount differs (30000 vs 28000 on p.15) | Inconsistency | Use one number |

**Numbers check:** margin per loaf 0.80 − 0.35 = 0.45 JOD (56.3%): matches · break-even with 2700 JOD monthly fixed costs: 6000 loaves a month (bizcalc break-even): the plan says 5000: mismatch · loan 30000 JOD at 9% over 48 months: about 747 JOD a month (bizcalc loan): the plan omits the instalment from the cash flow: mismatch.

**Strengths:** experienced founder with 12 years in commercial baking · clear unit cost build-up · backup flour supplier named · five cafés already trialling.
