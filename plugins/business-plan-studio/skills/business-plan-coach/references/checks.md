# Checks C01–C14: what they test and the number keys they read

`scripts/check_plan.py` reads `plan_state.json`. Save numbers with `plan_state.py num KEY VALUE --label L` or import them from `fin_model.py --state-export`. A check with missing keys reports "n/a"; that is fine early on. Results: **blocking** (a reader is likely to reject or stop), **advisory** (worth a look; explain or fix), **pass**, **n/a**.

| Check | Tests | Keys it reads | Blocking when | Advisory when |
|---|---|---|---|---|
| C01 | Price vs cost | `offer.<name>.price`, `offer.<name>.unit_cost`, `offer.<name>.min_price` | price below unit cost or minimum price | price within 10% of the floor |
| C02 | Capacity vs demand | `capacity.<name>`, `demand.<name>` (same unit and period; fin_model exports both for `hours` streams and for `units` streams that state a `capacity`) | demand above capacity | above 85% of capacity |
| C03 | SOM vs year-1 revenue | `market.som`, `forecast.revenue_y1` | revenue above SOM | revenue above 50% of SOM |
| C04 | Targets vs forecast | `target.<YYYY-MM>`, `forecast.revenue.<YYYY-MM>` | (never) | more than 10% apart |
| C05 | Team vs payroll | `team.headcount`, `model.headcount_peak` | (never) | different |
| C06 | Cash floor | `cash.low_point`, `cash.buffer` | low point below zero | below the buffer |
| C07 | Funding ask vs need | `funding.ask`, `funding.need_without_financing` (from fin_model; falls back to `funding.need`) | ask below need | no need but an ask; ask above 1.5 × need |
| C08 | Use of funds | `use_of_funds.<item>`, `funding.ask` | lines do not add up to the ask (1% tolerance) | — |
| C09 | LTV/CAC and payback | `unit.ltv`, `unit.cac`, `unit.payback_months` | LTV below CAC | ratio below 3; payback above 12 months |
| C10 | Growth sanity | `assumption.growth_pct_monthly`, `forecast.revenue_y1`, `forecast.revenue_y2` | (never) | above 15% a month; year 2 above 4 × year 1 |
| C11 | Margin sanity | `model.gross_margin_pct_y1`, `stated.gross_margin_pct` | negative gross margin | stated and modelled differ by more than 5 points |
| C12 | Claim labels | all numbers; sections containing digits | (never) | any unlabelled |
| C13 | Actions | `lists.actions` (via `plan_state.py action`) | (never) | missing owner or date; action plan text with no structured actions |
| C14 | Names | `lists.competitors`, `lists.segments`, competition.comparison and customer.priority_segment texts | (never) | names not matching |

Thresholds marked as advisory are rules of thumb that many readers use; they start a conversation, they do not prove the plan wrong. Explain them that way to the founder.

## Presenting results to the founder

Lead with blocking items, one line each: what disagrees, why the reader cares, two ways to fix it. Then advisories in one short list. Do not show passes unless asked. After a fix, rerun only the affected check (`--only C03`).

## Example

> Two checks need attention. Your year-1 revenue (1.5 million) is above the market you can realistically win (SOM 1.2 million). A bank will doubt every other number if this one does not hold. Either revisit the SOM method (your bottom-up count used only one district) or lower the forecast. Want to look at the SOM first?
