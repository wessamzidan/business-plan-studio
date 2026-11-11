# Market sizing: TAM, SAM and SOM

## Contents
- Definitions to give founders
- Top-down method
- Bottom-up method
- Triangulation and the forecast check
- Using market_size.py
- Worked examples (fictional)
- Common mistakes
- How to present it

## Definitions to give founders

- **TAM (total addressable market):** yearly spending on this need by everyone who has it, in the plan's area of interest.
- **SAM (serviceable available market):** the part of TAM the business can serve with its offer, channels and geography.
- **SOM (serviceable obtainable market):** the part of SAM the business can realistically win in the next two to three years, limited by sales capacity, competition and money.
Always state currency, year and whether values include tax.

## Top-down method

Start from a sourced count (population, households, firms, outlets, imports) and narrow it with sourced filters (share with the need, share in the target area, share in the right size band), then multiply by yearly spending per customer (sourced, or from the founder's pilot). Every filter needs a source or is labelled Estimate with its reasoning.

## Bottom-up method

Count the customers the business can actually reach (by district, list, channel or sales capacity), apply a conversion rate (from pilots or tests where possible), multiply by yearly value per customer, and cap the result by what the business can deliver (capacity). This is usually the SOM that readers believe.

## Triangulation and the forecast check

- Run both methods. If the two SOMs differ by more than about two times, explain why or revisit the inputs.
- Use the lower SOM in the plan unless the founder can justify the higher one.
- Check C03: year-1 revenue must not exceed SOM, and above about half of SOM is aggressive and needs an explanation (signed customers, existing contracts).

## Using market_size.py

Input (`python3 scripts/market_size.py --example` prints a full one):
```json
{"currency": "MAD", "year": 2027,
 "top_down": {
   "start": {"label": "Households in Rabat", "value": 600000, "source": "census table, 2024"},
   "tam_filters": [{"label": "pay for laundry", "pct": 20, "source": "our survey, 120 households, Feb 2027"}],
   "sam_filters": [{"label": "inside the delivery zone", "pct": 25, "source": "district map count"}],
   "annual_value_per_customer": {"value": 1800, "source": "survey: average spend"},
   "som_share_pct": {"value": 2, "source": "founder estimate from van capacity"}},
 "bottom_up": {
   "reachable_customers": {"value": 6000, "source": "two vans, three districts"},
   "conversion_pct": {"value": 5, "source": "pilot: 64 deposits from 1280 leaflets"},
   "annual_value_per_customer": {"value": 1800, "source": "survey"},
   "capacity_cap": {"value": 900000, "source": "max loads per van per year × price"}},
 "year1_forecast_revenue": 410000}
```
Output: TAM, SAM, both SOMs, the chosen SOM, a step-by-step trace with sources, and the C03 result. Inputs with no source are listed as To confirm.

## Worked examples (fictional)

**Laundry service, Rabat (MAD):** 600000 households × 20% paying for laundry = 120000 × 1800 MAD = 216 million MAD (TAM); 25% in the delivery zone = 30000 households, 54 million MAD (SAM); bottom-up 6000 reachable × 5% = 300 households × 1800 = 540000 MAD (SOM). Year-1 forecast 410000 MAD is 76% of SOM: aggressive, explained by 64 pre-paid deposits.

**Export consultancy, Amman (JOD):** count buyers, not export value: 900 small and mid-size exporters registered with the chamber × 30% in food and cosmetics needing certification support = 270 firms × 6000 JOD a year = 1.62 million JOD (SAM). Two consultants can serve 25 clients a year: 150000 JOD (SOM, capacity-capped).

## Common mistakes

- "If we get 1% of a huge market": no method, no capacity link.
- Global or national figures for a local business.
- Using total industry revenue (including competitors' costs, exports or other products) as spending on the need.
- Double counting the same spend across segments.
- Mixing currencies or years without stating the rate and date.
- Figures from AI summaries, unnamed reports or search snippets.

## How to present it

| | Value (currency, year) | Method | Source | Label |
|---|---|---|---|---|
| TAM | | | | |
| SAM | | | | |
| SOM | | | | |

Then three to five lines on the method, the gap between top-down and bottom-up, and the link to the year-1 forecast.
