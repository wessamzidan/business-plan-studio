# Finance concepts: plain explanations, formulas and commands

All example companies are fictional. Run the named command instead of calculating by hand. Not financial, tax or investment advice; rules differ by country.

## Contents
- Margins and unit economics
- Break-even and minimum price
- Customers: CAC, LTV, payback
- Profit, cash and working capital
- Funding need and use of funds
- Loans and debt service
- Equity and dilution
- Grants and other money
- Arabic terms

## Margins and unit economics

- **Gross margin** = (price − cost of the item) ÷ price. **Markup** = (price − cost) ÷ cost. A 50% markup is a 33.3% margin. `bizcalc.py markup-margin --cost C --price P`.
- **Contribution per unit** = price − unit cost − variable costs (fees, delivery, commission). It pays for fixed costs and profit. `bizcalc.py unit-margin --price P --unit-cost C --variable-pct V`.
- **By business type:** products and food: per item or order · subscriptions: per customer per month · services: per hour or project · marketplaces: take minus cost per transaction · rentals: per occupied unit.
- Example: a juice bar (fictional) sells at 120 KES, ingredients and cup cost 70, card fees 3%: contribution 46.40 KES, 38.7%.

## Break-even and minimum price

- **Break-even units** = fixed costs ÷ contribution per unit. `bizcalc.py break-even --fixed F --price P --unit-cost C [--variable-pct V] [--days D]`.
- **Break-even month** = the first month from which EBITDA stays at or above zero (fin_model.py reports it).
- **Cost per hour** (services) = fixed monthly cost ÷ productive hours. **Minimum price** = task hours × cost per hour + direct costs. `bizcalc.py min-price --fixed F --hours H --task-hours T --direct D [--price P] [--margin-pct M]`.
- Example: fixed costs 48000 AED, 400 productive hours: 120 AED an hour; a 30-hour job with 1500 AED of direct costs has a minimum price of 5100 AED.

## Customers: CAC, LTV, payback

- **CAC** = all acquisition spend (ads, sales salaries, commissions, events) ÷ new customers in the same period.
- **LTV** = monthly revenue per customer × gross margin ÷ monthly churn. **LTV/CAC** and **payback** (CAC ÷ monthly margin per customer): `bizcalc.py ltv-cac --arpu A --gross-margin-pct G --churn-pct C --cac K`.
- Conventions many investors use: LTV/CAC of about 3 or more, payback within about 12 months. They are conversation starters, not rules.
- Example: 49 USD a month, 80% margin, 4% churn: margin 39.20 a month, about 25 months of life, LTV 980 USD; with CAC 245 the ratio is 4.0 and payback 6.3 months.

## Profit, cash and working capital

- **Profit** counts sales when made and costs when incurred; **cash** counts money when it moves. Equipment is cash out at purchase but a monthly depreciation cost in profit. Loan principal is cash out but not a cost; interest is both.
- **Working capital cycle** = days stock is held + days customers take to pay − days suppliers give. Positive days mean growth consumes cash.
- **Cash low point** = the lowest month-end balance; it sets the funding need. **Burn rate** = monthly cash lost; **runway** = cash ÷ burn.

## Funding need and use of funds

- **Funding need** = safety buffer − cash low point, never below zero. `bizcalc.py funding-need --low-point L --buffer B`. fin_model.py uses a default buffer of three months of payroll plus fixed costs unless the founder sets `min_cash_buffer`.
- **Use of funds** lists every amount (equipment, fit-out, stock, marketing, working capital, buffer) and adds up exactly to the ask.
- The ask also shows the milestones the money reaches ("90 clinics and break-even by month 20").

## Loans and debt service

- **Instalment** for a loan repaid in equal monthly payments: `bizcalc.py loan --amount A --rate R --months N [--grace G]` (interest-only during grace).
- **Debt service coverage ratio (DSCR)** = cash available for debt service (often EBITDA, or operating cash flow) ÷ interest and principal due in the same period. `bizcalc.py dscr --cash-available C --debt-service D`. Lenders often look for about 1.2–1.5 or more; ask the lender for its own threshold.
- Banks also look at the owner's own contribution, collateral or guarantees, and repayment in the downside case.
- Example: 100000 at 18% over 24 months with 3 months' grace: 1500 a month interest-only, then 5586.55 a month; total interest 21817.54.

## Equity and dilution

- **Pre-money valuation** = agreed value before the investment; **post-money** = pre-money + investment; **investor share** = investment ÷ post-money.
- Example: 500000 at a 2000000 pre-money valuation: post-money 2500000; the investor owns 20%, founders' shares are diluted by the same 20%.
- Valuation is a negotiation shaped by traction, market, team and comparable deals, not a formula. Show the cap table before and after.
- Other instruments (convertible notes, SAFEs, revenue-based finance) have their own terms: explain the idea, and suggest legal review.

## Grants and other money

- Grants are not repaid but come with conditions: eligible costs, reporting, sometimes co-funding. In the model, add them as `financing` of type grant (cash in) unless an accountant advises otherwise.
- Supplier credit and customer deposits are free working capital: model them through `payment_days` and negative `collection_days`.
- Ethics: never inflate projections to win funding; label assumptions and show the downside.

## Arabic terms

هامش الربح الإجمالي (gross margin) · نسبة الزيادة على التكلفة (markup) · هامش المساهمة (contribution margin) · نقطة التعادل (break-even) · تكلفة الساعة (cost per hour) · الحد الأدنى للسعر (minimum price) · تكلفة اكتساب العميل (CAC) · القيمة الدائمة للعميل (LTV) · فترة الاسترداد (payback) · التدفق النقدي (cash flow) · أدنى رصيد نقدي (cash low point) · معدل الحرق (burn rate) · مدة الصمود (runway) · رأس المال العامل (working capital) · الاحتياج التمويلي (funding need) · استخدام الأموال (use of funds) · القسط (instalment) · فترة السماح (grace period) · نسبة تغطية خدمة الدين (DSCR) · التقييم قبل الاستثمار وبعده (pre-money, post-money) · التخفيف (dilution) · الإهلاك (depreciation) · السيناريو المتحفظ (downside case) · تحليل الحساسية (sensitivity).
