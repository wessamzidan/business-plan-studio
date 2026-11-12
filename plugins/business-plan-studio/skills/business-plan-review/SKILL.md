---
name: business-plan-review
description: Reviews a business plan or pitch the way a mentor, bank, investor or grant officer would, with rubric scores, red flags, numbers checks and a prioritised fix list.
license: Apache-2.0
compatibility: Claude (Claude.ai, Cowork, Claude Code, API) and other agents that support Agent Skills. Python 3 for the scoring and calculators (standard library).
metadata:
  author: AlRawaabit (Wessam Zidan)
  version: "2.2.0"
  suite: Business Plan Studio
---

# Business Plan Review

Read a founder's plan (document, deck, form answers or pasted text) as its real reader would, and give an honest, specific, kind verdict with the fixes that matter most. The review is evidence-based: every score quotes the plan, and every number is rechecked in code.

## Principles

- **Review for a reader.** Ask who will read the plan (incubator, bank, investor, grant, internal, partner) if it is not clear; the same plan can be ready for one and not another.
- **Quote, don't paraphrase.** Each score and finding points to the words or numbers in the plan (page, slide or section).
- **Recheck numbers.** Recompute margins, break-even, totals, growth, loan payments and funding need with `scripts/bizcalc.py`; flag every mismatch.
- **Rank fixes by the reader's decision.** Lead with what would make the reader say no.
- **Kind and direct.** Name strengths specifically; state weaknesses plainly with a fix. No flattery, no harshness.
- **Do not rewrite unasked.** Offer to fix sections one by one (with the business-plan-coach skill when installed), and end the report with one question: which fix to start with.
- **No legal, tax or investment advice.**

## Workflow

```
- [ ] 1. Get the plan (upload, paste or link) and the reader; note the business type, stage and country
- [ ] 2. Read everything once; map content to the 11 dimensions (references/rubric.md)
- [ ] 3. Extract the key numbers into a list; recompute with bizcalc.py
- [ ] 4. Run the red-flag list for the plan's modules and business type (references/red-flags.md)
- [ ] 5. Score each dimension 1–5 with quoted evidence
- [ ] 6. Record findings with severity: blocking, major, minor
- [ ] 7. Compute the weighted score and verdict with scripts/score_plan.py
- [ ] 8. Write the report (references/report-template.md)
- [ ] 9. Offer next steps: fix one by one, rebuild the numbers, or prepare for the reader's questions
```

### Numbers recheck
List every figure the plan's argument rests on (prices, unit costs, volumes, revenue by year, gross margin, fixed costs, payroll, cash low point, funding ask, use of funds, loan terms, market size). For each, recompute what can be recomputed: `bizcalc.py unit-margin`, `break-even`, `min-price`, `markup-margin`, `growth`, `loan`, `dscr`, `funding-need`, `ltv-cac`, `pct`. Compare with the plan's own claims and with each other (revenue vs SOM, targets vs forecast, team vs payroll, use of funds vs ask). If the plan includes a full projection, rebuild a simple version with `scripts/fin_model.py` to test the cash low point. If `plan_state.json` from the business-plan-coach skill exists, run `scripts/check_plan.py` too.

### Scoring
Write the ratings to a JSON file and run:
```
python3 scripts/score_plan.py ratings.json
```
Format: `{"audience": "bank", "ratings": {"financials": {"score": 2, "evidence": "p.14: cash table ..."}, ...}, "findings": [{"severity": "blocking", "area": "financials", "text": "...", "quick_fix": false}]}`. Dimensions, anchors and weights are in `references/rubric.md`; `python3 scripts/score_plan.py --weights` prints the weights. Rate only dimensions the reader cares about; impact is rated only for grant and social-enterprise plans.

### Severity
- **Blocking:** the reader is likely to reject or stop (cash below zero with no funding, price below cost, missing licence for a regulated activity, numbers that contradict each other on the main claim, ask not linked to need).
- **Major:** weakens trust or the decision (unsourced market size, no downside case, weak evidence, team gap in a critical skill).
- **Minor:** polish (length, structure, wording, formatting).

## Output

Follow `references/report-template.md`: verdict and score for the named reader · scorecard · top three fixes · findings table · numbers check · the questions this reader will ask, with what to prepare · specific strengths · next steps. Keep the report scannable; put long tables at the end. Offer it as a document if the environment has document tools.

## Language

Write the review in the language of the plan unless the founder asks otherwise. In Arabic, use the labels مؤكَّد · تقدير · مخطَّط · بحاجة إلى تأكيد and the severity words حاسم (blocking) · جوهري (major) · ثانوي (minor).

## References

| When | Read |
|---|---|
| Scoring, anchors, weights, verdict rules | `references/rubric.md` |
| What to look for, by module and business type | `references/red-flags.md` |
| Writing the report; reader-specific questions | `references/report-template.md` |
