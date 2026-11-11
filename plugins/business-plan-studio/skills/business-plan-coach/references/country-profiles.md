# Country profiles: currency, tax and payroll starting points

## Contents
- How to use
- Profile template (any country)
- Egypt
- United Arab Emirates
- Saudi Arabia
- Other countries

## How to use

- Tax, payroll and licence rules change. Treat every rate here as a dated starting point: label it **To confirm**, say "check with your accountant", and add the question to the open-questions list (`plan_state.py question "..." --for accountant`).
- The figures below were last checked in November 2026 against the pages named in each table. Before relying on one, check the official source if web search is available, and record the page and date. Look every figure up again if today is more than about six months after that check.
- Never give tax or legal advice; give the founder the questions to ask.
- For any country not listed, build the profile on the fly with the template below, using official sources (tax authority, social insurance authority, labour ministry, investment or company registry).

## Profile template (any country)

| Item | What to find | Where the plan uses it |
|---|---|---|
| Currency and code | e.g. EGP, SAR, AED, MAD, KES, NGN | every amount and table header |
| VAT or sales tax | standard rate, registration threshold, whether prices are quoted with tax | model.pricing (prices before or after tax), financials (exclude VAT from revenue) |
| Small-business tax regimes | turnover-based or simplified regimes and their thresholds | `tax` placeholder in the model |
| Corporate income tax or zakat | rate and thresholds | `tax` placeholder in the model |
| Employer payroll costs | social insurance shares, wage floors and ceilings, other levies | `employer_oncost_pct` in the model; team.hiring_plan |
| Minimum wage | current amount for the sector | team.hiring_plan (every salary above it) |
| Company forms and registration | common legal forms, registry, typical time and cost | operations.legal |
| Sector licences | permits for food, health, education, finance, transport, tourism and other regulated activities | market.regulation, operations.legal |
| Import and export basics | registrations, certificates, duties | trade-distribution plans |
| Public support | SME agencies, export councils, investment authorities, grant programmes (as questions to explore) | gtm.partnerships, financials.funding |

## Egypt

| Item | Starting point (checked November 2026) | Where it was checked | Question for the accountant |
|---|---|---|---|
| Currency | Egyptian pound (EGP) | — | Is any income in USD or other currencies? Which rate and date do we use? |
| VAT | Standard rate 14%. A registration threshold of EGP 500000 of annual turnover is commonly cited; not confirmed in this check | PwC Worldwide Tax Summaries, Egypt (reviewed August 2026); Egyptian Tax Authority | Must we register now? Do our prices include VAT? |
| Simplified tax for small businesses | Law 6 of 2025: turnover-based rates for small businesses, roughly 0.4% to 1.5% of turnover by bracket | Published summaries of Law 6 of 2025; Egyptian Tax Authority | Are we eligible, and which bracket applies? |
| Social insurance | Employer 18.75% and employee 11% of the insurable wage | PwC Worldwide Tax Summaries, Egypt, "Other taxes" | Which employees and founders are insured, from which month? |
| Insurable wage range | EGP 2700 to 16700 a month from 1 January 2026; the published table shows EGP 3200 to 19300 for 2027 | PwC Worldwide Tax Summaries, Egypt, "Other taxes" | Which wage do we insure each person on, and what changes in January? |
| Minimum wage (private sector) | EGP 7000 a month, in force since 1 March 2025; no increase announced as of this check | Payroll provider guides updated November 2026; National Wages Council decisions | Are all planned salaries above it? |

## United Arab Emirates

Rules differ between the mainland and free zones.

| Item | Starting point (checked November 2026) | Where it was checked | Question for the accountant |
|---|---|---|---|
| Currency | UAE dirham (AED) | — | — |
| VAT | Standard rate 5%; mandatory registration above a turnover threshold (not re-checked here) | Federal Tax Authority, tax.gov.ae | Must we register, and are our prices quoted with VAT? |
| Corporate tax | 9% on taxable income above AED 375000 (not re-checked here). Small Business Relief for businesses with revenue up to AED 3 million was extended in 2026 to tax periods ending on or before 31 December 2029 (Ministerial Decision No. 131 of 2026) | Business press reports of the Ministry of Finance decision (August 2026); Federal Tax Authority | Do we qualify for Small Business Relief or for free-zone treatment, and must we still register and file? |
| Payroll costs | Pension contributions apply to UAE and GCC nationals; visas, medical insurance and end-of-service gratuity apply to expatriate staff (not re-checked here) | General Pension and Social Security Authority; Ministry of Human Resources and Emiratisation | What does each hire cost in total, including visa, insurance and gratuity? |
| Company set-up | A mainland licence or a free-zone licence, each with different rules on where you may trade | Economic department of the emirate; the free-zone authority | Which licence fits our customers and activities? |

## Saudi Arabia

| Item | Starting point (checked November 2026) | Where it was checked | Question for the accountant |
|---|---|---|---|
| Currency | Saudi riyal (SAR) | — | — |
| VAT | Standard rate 15%; mandatory registration above SAR 375000 of annual taxable supplies | Employer tax guide updated May 2026; Zakat, Tax and Customs Authority (ZATCA), zatca.gov.sa | Must we register, and are prices quoted with VAT? |
| Zakat and income tax | Zakat applies to Saudi and GCC ownership; income tax applies to foreign ownership shares (not re-checked here) | ZATCA | How is our ownership taxed? |
| Social insurance (GOSI) | Saudi employees: employer about 12.25% and employee about 10.25% of basic salary plus housing, with yearly step-ups announced to 2028. Non-Saudi employees: employer 2% (occupational hazards) | Employer tax guide updated May 2026; General Organization for Social Insurance, gosi.gov.sa | What is the employer cost for each planned hire this year and next? |
| Saudization | Nitaqat quotas may require Saudi hires by sector and size (not re-checked here) | Ministry of Human Resources and Social Development | How many Saudi employees must we have, and when? |

## Other countries

Fill the profile template from official sources, cite each line with its page and date, and label every rate To confirm until an accountant confirms. Useful starting points: the national tax authority, the social insurance or social security agency, the labour ministry, the company registry or investment authority, chambers of commerce and the national SME agency. Large accounting firms publish free country tax summaries that help find the right official page.
