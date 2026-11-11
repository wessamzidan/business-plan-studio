# Business type: Social enterprises, NGOs with earned income and cooperatives

Covers social enterprises, non-profits that sell goods or services, cooperatives, community businesses and impact-led companies applying for grants or impact investment.

## How money is made
A blend: sales of products or services, grants (often restricted to activities), donations and sometimes impact investment. The plan must show both financial sustainability and measurable impact, and separate restricted from unrestricted money.

## Key drivers and metrics
| Metric | Formula | Why it matters | Sections |
|---|---|---|---|
| Earned income share | sales ÷ total income | Independence from grants | model.revenue_streams |
| Cost per beneficiary | programme costs ÷ beneficiaries served | Efficiency donors compare | strategy.impact |
| Outcome indicators | e.g. jobs found, income gained, tonnes recycled | The impact itself | strategy.impact |
| Grant pipeline | applications × success chance × amount | Timing of funding | financials.funding |
| Restricted funds | grants tied to specific uses | Cannot pay other costs | financials.cash_flow |
| Unit economics of the product | price − direct cost | Earned income must not lose money | model.unit_economics |

## Sharpest questions
- `customer.segments`: Who benefits, and who pays? Are they the same people?
- `strategy.impact`: What change do you create, for whom, and how do you measure it (theory of change)?
- `model.revenue_streams`: What share of income comes from sales, grants and donations this year and in three years?
- `model.unit_economics`: Does each product or service cover its direct costs before grants?
- `financials.funding`: Which grants are secured, applied for or planned, with amounts and dates?
- `financials.cash_flow`: Which money is restricted to specific activities?
- `operations.legal`: Which legal form (company, association, cooperative), and what does it allow (profit distribution, donations, tax status)?
- `team.founders`: Who manages finance and reporting to donors?
- `validation.evidence`: What results have you already measured, with baselines?
- `risks.register`: What happens if the main grant is not renewed?

## Options to offer
- Revenue blends: product sales · service contracts with institutions · training fees · grants · donations · cross-subsidy (paying customers fund free places).
- Impact measures: people trained or employed · income change · health or education outcomes · resources saved · emissions avoided.

## Model template
Driver tree: earned income from `units` or `hours` streams; grants as dated `financing` entries of type grant (cash in, not revenue); programme costs as fixed costs or team lines; separate the cost of the social programme so cost per beneficiary can be computed.
```json
{"name": "Stitch Together Cooperative (fictional)", "currency": "UGX", "start": "2027-01", "months": 12,
 "opening_cash": 8000000,
 "streams": [{"name": "School uniforms", "type": "units", "volume": {"start": 300, "growth_pct": 4},
   "price": 45000, "unit_cost": 26000, "seasonality": [2.5, 1.5, 0.5, 0.5, 1.5, 0.5, 0.5, 1.5, 1.5, 0.5, 0.5, 0.5], "collection_days": 30}],
 "fixed_costs": [{"name": "Workshop rent", "monthly": 1200000}, {"name": "Trainee programme materials", "monthly": 1000000}],
 "team": [{"role": "Coordinator and trainers", "count": 3, "monthly_salary": 900000}],
 "financing": [{"type": "grant", "amount": 24000000, "month": "2027-02"}]}
```

## Capacity and operations
Capacity is trainers, workspace and the time beneficiaries can give. Production by trainees may be slower and less even: plan quality checks.

## Convincing evidence
Level 2: needs assessments, community consultations · Level 3: grant agreements, institutional letters of intent · Level 4: paid sales and measured outcomes · Level 5: outcomes tracked over time with baselines.

## Red flags reviewers spot
- Impact stated as activities ("we held 20 workshops") rather than outcomes.
- Grants shown as secured when only applied for.
- Earned income that loses money on every unit.
- Restricted grants used for general costs.
- No plan for when the main grant ends.

## Typical risks and mitigations
Grant dependence → grow earned income, diversify donors · mission drift → impact targets in the plan and the board's oversight · reporting burden → simple monitoring system from day one.

## Fictional mini-example
Stitch Together Cooperative (fictional), Kampala: training costs about 900000 UGX per trainee, so 40 trainees a year cost 36000000 UGX. Uniform sales cover part of it; the plan shows the gap the grant fills and how the share of earned income grows each year.

## Hybrids
Social enterprise + manufacturing or food-service (production by beneficiaries) · social enterprise + services (training contracts with institutions).
