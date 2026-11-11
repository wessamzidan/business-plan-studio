# Outputs: templates for the finished plan

## Contents
- Before any output
- Full plan document
- One-page summary
- Business Model Canvas and Lean Canvas
- Pitch deck outline
- Forms, portals and paste packs
- Registers: assumptions, open questions, actions
- Delivery formats

## Before any output

1. Run `scripts/check_plan.py`; resolve blocking results or state them openly in the plan.
2. Make sure every number in the text matches the saved numbers.
3. Draft with `scripts/render_plan.py`; then polish wording with the founder. Never add facts while polishing.
4. Keep claim labels in the founder's working copy. For the reader's copy, ask the founder: keep labels as brackets, move them to an assumptions appendix, or remove them while keeping the appendix. Never remove the uncertainty itself: "To confirm" items stay listed as open points.

## Full plan document

Draft: `render_plan.py --plan --audience <id> [--lang ar] --out plan.md`. Structure (the script orders modules by reader):
1. Cover: name, one-liner, contact, date, version.
2. Executive summary (one page).
3. Modules in the reader's order (see `references/audiences.md`), each with its section headings.
4. Financial tables: yearly summary in the text; monthly tables in an appendix.
5. Appendices: assumptions register, sources list with links and dates, open questions, supporting documents list.

Write in the reader's register: banks formal and precise, investors concise and confident, grants in the programme's own headings, incubators candid about what is still unknown.

## One-page summary

`render_plan.py --one-pager`. Order: what we do · the problem · who we serve · market (SOM) · how we make money · traction · competition and advantage · team · financial headline · what we need. About 350–450 words; same numbers as the plan.

## Business Model Canvas and Lean Canvas

`render_plan.py --canvas bmc` or `--canvas lean`. Each block is filled from its sections:

| Business Model Canvas block | Sections |
|---|---|
| Key partners | gtm.partnerships, operations.suppliers |
| Key activities | operations.activities |
| Key resources | operations.resources, team.founders |
| Value proposition | offer.value_proposition |
| Customer relationships | gtm.sales_process |
| Channels | gtm.channels |
| Customer segments | customer.priority_segment, customer.segments |
| Cost structure | financials.costs |
| Revenue streams | model.revenue_streams, model.pricing |

| Lean Canvas block | Sections |
|---|---|
| Problem | customer.problem, customer.alternatives |
| Customer segments | customer.priority_segment |
| Unique value proposition | offer.value_proposition |
| Solution | offer.description |
| Channels | gtm.channels |
| Revenue streams | model.revenue_streams, model.pricing |
| Cost structure | financials.costs |
| Key metrics | validation.metrics, strategy.kpis |
| Unfair advantage | competition.advantage |

Shorten each block to 2–4 bullet fragments for a one-page visual. If the environment can make slides or designs, offer a visual canvas.

## Pitch deck outline

`render_plan.py --deck-outline` gives 12 slides: title · problem · solution and value proposition · why now · market size · customer and go-to-market · business model · traction · competition · team · financials · the ask and use of funds. One message per slide, written as a headline sentence ("Clinics lose 1 in 5 appointments"), with at most 3 supporting points or one chart. If a slides tool or skill is available, offer to build the deck from this outline.

## Forms, portals and paste packs

Many readers use an online form or portal with fixed fields and limits. Build a form map once, then generate a paste pack:

```json
{"form": "Example accelerator application",
 "number_format": "digits only",
 "fields": [
   {"id": "q1", "page": "1", "label": "Describe your customer", "limit_chars": 600,
    "number_format": null, "calculated_by_portal": false, "maps_to": ["customer.priority_segment", "customer.persona"]},
   {"id": "q7", "page": "3", "label": "Year-1 revenue", "limit_chars": 20,
    "number_format": "digits only", "calculated_by_portal": false, "maps_to": ["financials.forecast"]}
 ]}
```

`render_plan.py --paste-pack form.json` prints one block per field with its character count and an "OVER LIMIT" flag; fields the portal calculates are skipped. Then rewrite each over-limit block to fit and show the founder before they paste. Keep each field in the language it is in now, use the form's number format (some portals reject thousands separators), and never press submit, send or publish for the founder.

## Registers: assumptions, open questions, actions

`render_plan.py --registers` prints three tables:
- Assumptions: id · assumption · value · label · how to validate · owner · due · status.
- Open questions: id · question · section · for whom (accountant, lawyer, supplier, founder) · status.
- Actions: what · owner · due.
Put them in the appendix, and give the founder the open questions as a to-do list.

## Delivery formats

- A document: use the environment's document tools when available (a Docs connector, a docx or PDF skill); otherwise deliver Markdown, which converts cleanly.
- The financial model: `fin_model.py model.json --xlsx model.xlsx` for a spreadsheet, plus the JSON input as the assumptions record.
- Forms: the paste pack.
- Always offer `plan_state.json` so the founder can continue later or in a new conversation.
