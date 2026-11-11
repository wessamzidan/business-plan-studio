# Business type: Clinics, salons, gyms, training centres, tours and events

Covers medical and therapy clinics, beauty salons and spas, gyms and studios, tutoring and training centres, tour operators, event organisers and any business that sells time slots, seats or places.

## How money is made
Capacity (slots, seats, places) × occupancy × average spend, often with packages or memberships paid in advance. Staff productivity, no-shows, licences and the mix of one-off and recurring customers decide profit.

## Key drivers and metrics
| Metric | Formula | Why it matters | Sections |
|---|---|---|---|
| Capacity | staff or rooms × slots per day × days | Ceiling on revenue | operations.resources |
| Occupancy | booked slots ÷ capacity | Main volume lever | financials.forecast |
| Average spend | revenue ÷ visits (services plus products) | Price and upsell | model.pricing |
| No-show rate | missed bookings ÷ bookings | Lost revenue | operations.activities |
| Members and churn | active members, monthly cancellations | Predictable income | model.unit_economics |
| Revenue per staff hour | revenue ÷ staff hours | Productivity | financials.costs |
| Seasonality | monthly pattern (school year, tourist season, Ramadan, summer) | Cash planning | financials.forecast |

## Sharpest questions
- `operations.resources`: How many rooms, chairs, coaches or guides, and how many slots each per day?
- `financials.forecast`: What occupancy do you expect in month 1, 6 and 12, and why?
- `model.pricing`: What do single visits, packages and memberships cost, and which do most customers buy?
- `model.unit_economics`: What is the cost per visit (staff commission, consumables, rent per hour)?
- `operations.activities`: How do you cut no-shows: deposits, reminders, waitlists?
- `operations.legal`: Which professional licences, health permits or tourism licences are needed, and who holds them?
- `team.hiring_plan`: Are staff salaried, on commission or freelancers?
- `gtm.channels`: Maps listings, referrals, corporate deals, schools, travel platforms?
- `financials.cash_flow`: When does cash come in for packages and tours sold in advance, and when is it spent?
- `risks.register`: What if a key practitioner or guide leaves and clients follow them?

## Options to offer
- Revenue: per visit · packages of 5–10 sessions · monthly membership · corporate contracts · retail products · group classes · tours and event tickets.
- Channels: maps and booking apps · referrals · corporate wellness · partnerships with hotels, schools, insurers.

## Model template
Driver tree: visits = capacity × occupancy; revenue = visits × average spend; members as a recurring stream. Use a `rental`-style or `units` stream for visits (occupancy ramp with `rental` works well for slots) and a `subscription` stream for memberships; add seasonality.
```json
{"name": "Harakeh Physio (fictional)", "currency": "JOD", "start": "2027-01", "months": 12,
 "opening_cash": 30000,
 "streams": [{"name": "Therapy sessions", "type": "rental", "units_available": 672,
   "occupancy_pct": {"start": 45, "growth_pts": 3, "max": 80}, "price": 25, "unit_cost": 2},
  {"name": "Rehab memberships", "type": "subscription", "customers_start": 0, "new": {"start": 6}, "churn_pct": 10, "price": 60, "unit_cost": 5}],
 "fixed_costs": [{"name": "Clinic rent", "monthly": 2200}, {"name": "Booking system and supplies", "monthly": 400}],
 "team": [{"role": "Physiotherapists", "count": 4, "monthly_salary": 1100}, {"role": "Reception", "count": 1, "monthly_salary": 450}],
 "employer_oncost_pct": 14.25,
 "capex": [{"name": "Equipment", "amount": 25000, "month": "2027-01", "life_months": 60}]}
```

## Capacity and operations
Capacity is staff hours and rooms in the busiest hours, not the whole day: ask for occupancy by time band. Plan for staff leave and no-shows.

## Convincing evidence
Level 2: waiting lists or enquiries · Level 3: pre-sold packages, corporate letters of intent · Level 4: paid visits and bookings · Level 5: package renewals and member retention.

## Red flags reviewers spot
- Full occupancy assumed from month one.
- Staff productivity higher than the hours they can work.
- No-shows and cancellations ignored.
- Pre-paid packages treated as earned revenue when the service is delivered later.
- Licences held by one person with no backup.

## Typical risks and mitigations
Practitioner leaves → client relationships with the business, contracts · seasonal dips → corporate deals, off-season offers · licence or safety incident → compliance calendar, insurance · competition on price → specialised services and outcomes data.

## Fictional mini-example
Harakeh Physio (fictional), Amman: 4 therapists × 7 sessions a day × 24 days = 672 slots a month. At 70% occupancy that is about 470 sessions at 25 JOD = 11750 JOD a month before memberships.

## Hybrids
Appointment + retail-store (product sales) · appointment + saas-subscription (online programmes) · appointment + social-enterprise (subsidised places funded by grants).
