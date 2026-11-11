# Lessons: micro-lessons the coach teaches as it goes

## Contents
- How to teach
- Basics
- Customer and offer
- Market
- Competition
- Model and pricing
- Go-to-market
- Operations and team
- Validation
- Financials
- Risks and strategy
- Summary

## How to teach

- Teach when a concept first appears for a "new" founder, when anyone asks ("explain X", "what does that mean?"), or after a weak answer that shows a gap. Never repeat a lesson already given in the session.
- Say it in 3 to 5 lines: plain words, why it matters, and the example, rewritten for the founder's own business when you can. Add the formula only when numbers are involved, and run the named `scripts/bizcalc.py` command instead of doing the arithmetic yourself.
- Ask the check question only in "new" mode, and only if it helps; never quiz an experienced founder.
- All example businesses below are fictional. Each lesson heading also gives the usual Arabic term.

## Basics

### What a business plan is for · الغرض من خطة العمل
**Plain words:** a plan is a decision document: it shows a specific reader why your business will work and what you need from them. **Why it matters:** a bank decides on a loan, an investor on a stake, an incubator on a place; each reads for different things. **Example:** the same bakery writes a 25-page plan with 36 months of cash flow for a bank, and 12 slides for an investor. **Watch out:** writing for "everyone". **Check:** who reads your plan first, and what do you want them to do?

### Claim labels and evidence · تصنيف الادعاءات والأدلة
**Plain words:** every statement gets one label: Verified (you have proof), Estimate (your best number, with how you got it), Planned (not done yet), To confirm (needs a source or someone's answer). **Why it matters:** readers trust a plan that shows what is known and what is hoped. **Example:** "We have 12 paying clients [Verified]; we expect 30 by June [Estimate: 3 new a month from referrals, as in the last 4 months]." **Watch out:** writing plans as facts. **Check:** which label fits "the market is growing fast"?

## Customer and offer

### Customer segment · شريحة العملاء
**Plain words:** a group of customers with the same need, who buy the same way. **Why it matters:** each segment needs its own message, channel and often price. **Example:** a fictional Nairobi laundry splits customers into busy households, hostels for students and small hotels: three very different buyers. **Watch out:** age and gender with no need attached. **Check:** what need do the people in your first segment share?

### Ideal customer and persona · العميل المثالي والشخصية النموذجية
**Plain words:** a short portrait of one typical buyer in your priority segment, based on real people you have met. **Why it matters:** it makes marketing, sales and product choices concrete. **Example:** "Owner of a 30-seat café in Zamalek, orders supplies on WhatsApp every Thursday, hates running out of pastries on weekends." **Watch out:** inventing hobbies and quotes. **Check:** where could you meet ten people like this next week?

### Jobs to be done · المهمة التي يريد العميل إنجازها
**Plain words:** customers "hire" a product to get a job done in their life or work. **Why it matters:** it shows what you really compete with. **Example:** a parent buying tutoring is hiring "my child passes the exam and I stop worrying", which a cheaper app or a cousin can also do. **Watch out:** describing your product instead of the job. **Check:** what is your customer trying to get done when they reach for you?

### Problem evidence · الدليل على وجود المشكلة
**Plain words:** proof that the problem is real, frequent and costly: what customers did and spent, not what they said they might do. **Why it matters:** a painful, proven problem is what makes people pay. **Example:** "9 of 12 restaurant owners we interviewed threw away stock last month; average loss about 4000 MAD [Verified: interview notes]." **Watch out:** "people would love an app for this". **Check:** what did your customers last do about this problem, and what did it cost them?

### Value proposition · القيمة المقدمة
**Plain words:** one or two sentences saying for whom, what result, and why you rather than the alternative. **Why it matters:** it is the sentence readers repeat. **How:** "For [customer] who [problem], we provide [result], unlike [alternative], because [proof]." **Example:** "For clinics in Riyadh losing 1 in 5 appointments to no-shows, we fill gaps with reminders and a waitlist, unlike manual calls, cutting no-shows by half in our 3 pilots [Verified]." **Watch out:** "best quality at the best price". **Check:** what proof sits behind your "because"?

### Benefit versus feature · الفائدة مقابل الميزة
**Plain words:** a feature is what the product has; a benefit is what the customer gains. **Why it matters:** customers pay for gains. **Example:** "GPS tracking" is a feature; "you know exactly when the delivery arrives, so the kitchen is ready" is the benefit. **Watch out:** feature lists. **Check:** for your main feature, answer "so what?" until a customer would say the answer aloud.

### Why now · لماذا الآن
**Plain words:** the recent change that makes this the right moment. **Why it matters:** investors ask why nobody did it before and why it will work now. **Example:** "Since the new e-invoicing rule, every small shop must issue digital invoices: our simple tool arrives as they search for one [source and date]." **Watch out:** "the digital age". **Check:** what changed in the last two or three years that helps you?

## Market

### TAM, SAM and SOM · السوق الكلي والمتاح والممكن الوصول إليه
**Plain words:** TAM is all the yearly spending on this need; SAM is the part you can serve with your offer and location; SOM is the part you can realistically win in the next few years. **Why it matters:** readers check that the market is big enough and that your revenue goals fit inside your SOM. **Work it out:** `scripts/market_size.py` with a source for every input. **Example:** a fictional Rabat laundry: 600000 households × 20% paying for laundry × 1800 MAD a year = 216 million MAD (TAM); 25% within the delivery zone = 54 million (SAM); 6000 reachable households × 5% conversion × 1800 = 540000 MAD (SOM). **Watch out:** "1% of a huge market". **Check:** which number should your year-1 revenue be compared with?

### Top-down and bottom-up sizing · التقدير من أعلى إلى أسفل ومن أسفل إلى أعلى
**Plain words:** top-down starts from a big published number and narrows it; bottom-up counts customers you can reach and what they spend with you. **Why it matters:** doing both and explaining the gap is what convinces readers. **Example:** top-down says 3.6 million a year, bottom-up 2 million: the plan uses 2 million and explains that capacity limits it. **Watch out:** only top-down. **Check:** how many customers can your team actually serve in a year?

### Market trends and timing · اتجاهات السوق والتوقيت
**Plain words:** changes in demand, supply, technology, prices or rules that affect your market. **Why it matters:** trends support your growth assumptions or warn of risks. **Example:** "Delivery-app orders in our city grew strongly last year [source]; we plan 40% of sales through apps." **Watch out:** world trends with no link to your numbers. **Check:** which trend changes one of your numbers?

### Citing sources · توثيق المصادر
**Plain words:** every outside fact gets title, publisher, link and the date of the data. **Why it matters:** readers check one number; if it fails, they doubt all of them. **Example:** "Households in Rabat: 600000 (national statistics office, census table X, 2024, accessed March 2027)." **Watch out:** search snippets, unnamed "reports". **Check:** could a reader find your number in under a minute?

## Competition

### Direct, indirect and substitute competitors · المنافسون المباشرون وغير المباشرين والبدائل
**Plain words:** direct competitors sell the same thing to the same customer; indirect ones solve the same need differently; substitutes include doing it yourself or doing nothing. **Why it matters:** "no competitors" tells readers you have not looked. **Example:** for a meal-prep service: other meal-prep firms (direct), restaurants and delivery apps (indirect), home cooking (substitute). **Check:** what did your last customer use before you?

### Positioning statement · بيان التموضع
**Plain words:** where you stand against alternatives on what customers care about most. **Example:** "The fastest same-day repair service in Jeddah for small offices, at mid-market prices." **Watch out:** positioning on something customers ignore. **Check:** which two things decide your customers' choice?

### Competitive advantage and moat · الميزة التنافسية والحصن الدفاعي
**Plain words:** what keeps customers choosing you after others copy you: lower cost, exclusive access, know-how, network effects, brand, switching costs. **Why it matters:** investors fund advantages that grow over time. **Example:** a fictional olive-oil exporter holds exclusive supply from 40 certified farms and lab records buyers ask for. **Watch out:** "passion" and "quality". **Check:** what would a competitor need a year to copy?

### SWOT analysis · التحليل الرباعي (SWOT)
**Plain words:** strengths and weaknesses are inside the business; opportunities and threats come from outside. **Why it matters:** it shows self-awareness; weaknesses and threats must link to risks and actions. **Example:** weakness "one supplier for packaging" → risk register → action "qualify a second supplier by May". **Watch out:** generic items. **Check:** which weakness will you fix first?

## Model and pricing

### Revenue models · نماذج الإيرادات
**Plain words:** the ways customers pay: per unit, per hour or project, subscription, retainer, commission or take rate, rental, licence, advertising, grants. **Why it matters:** the model decides your forecast drivers and how cash arrives. **Example:** a design studio moves from one-off projects to monthly retainers to make revenue predictable. **Check:** which single stream brings most of your year-1 income?

### Pricing strategies · استراتيجيات التسعير
**Plain words:** cost-plus (cost plus a margin), competitor-based, value-based (a share of the value created), tiered, penetration (low to enter) and premium. **Why it matters:** price sets margin, positioning and how many customers you need. **Example:** a clinic-software firm charges 300 SAR a month because each clinic loses about 3000 SAR a month to no-shows [Estimate]. **Watch out:** pricing below cost "for now" with no date to raise it. **Check:** what is your floor price, and what is the customer's alternative cost?

### Gross margin and markup · هامش الربح الإجمالي ونسبة الزيادة
**Plain words:** markup is profit divided by cost; margin is profit divided by price. **Work it out:** `bizcalc.py markup-margin --cost C --price P`. **Example:** cost 100, price 150: markup 50%, margin 33.3%. **Watch out:** mixing them when setting prices. **Check:** if you need a 40% margin on a 60-unit cost, what is the price?

### Contribution margin · هامش المساهمة
**Plain words:** what one sale leaves after its direct costs, to pay fixed costs and profit. **Work it out:** `bizcalc.py unit-margin --price P --unit-cost C --variable-pct V`. **Example:** a Nairobi juice bar sells at 120 KES, ingredients and cup 70, card fees 3%: contribution 46.40 KES (38.7%). **Watch out:** forgetting fees, delivery, packaging or returns. **Check:** which variable cost do you most often forget?

### Unit economics · اقتصاديات الوحدة
**Plain words:** the money one unit, order or customer makes or loses. **Why it matters:** if each unit loses money, growth makes it worse. **Example:** a cloud kitchen order at 250 EGP: food 90, packaging 10, app commission 25% (62.50) leaves 87.50 EGP (35%) before rent and salaries. **Check:** after all costs of one order, what is left?

### Break-even point · نقطة التعادل
**Plain words:** the sales level where income covers all costs: no profit, no loss. **Work it out:** fixed costs ÷ contribution per unit: `bizcalc.py break-even --fixed F --price P --unit-cost C --days D`. **Example:** fixed costs 60000 EGP a month, price 18, unit cost 7: 5455 units a month, about 210 a day over 26 trading days. **Watch out:** forgetting founder pay in fixed costs. **Check:** how far is your current monthly volume from break-even?

### Cost per hour and minimum price · تكلفة الساعة والحد الأدنى للسعر
**Plain words:** for services, every productive hour must carry its share of fixed costs; the minimum price of a job covers its hours plus direct costs. **Work it out:** `bizcalc.py min-price --fixed F --hours H --task-hours T --direct D`. **Example:** an agency with 48000 AED fixed costs and 400 productive hours a month costs 120 AED an hour; a 30-hour project with 1500 direct costs must sell for at least 5100 AED. **Watch out:** counting all paid hours as productive. **Check:** how many hours a month does your team really bill?

### Payment terms and working capital · شروط الدفع ورأس المال العامل
**Plain words:** working capital is the cash tied up between paying suppliers and getting paid by customers. **Example:** a distributor holds stock 30 days and gives customers 60 days, but pays suppliers in 30: each sale ties up cash for 60 days. **Why it matters:** fast-growing businesses run out of cash even when profitable. **Check:** how many days pass between paying for a sale's costs and receiving its money?

## Go-to-market

### Sales channels · قنوات البيع
**Plain words:** the routes customers use to find and buy from you: direct sales, shop, website, marketplace, distributor, partner, app. **Why it matters:** each channel has a cost and a fit with your persona. **Example:** a skincare brand starts with Instagram and one pharmacy chain, not ten channels. **Check:** where does your persona already buy similar things?

### Marketing funnel and conversion rate · قمع التسويق ومعدل التحويل
**Plain words:** the steps from stranger to customer, and the share that moves from each step to the next. **Work it out:** `bizcalc.py pct --part P --whole W` for each step. **Example:** 2000 visitors, 4% start a trial (80), 25% of trials buy: 20 customers. **Watch out:** conversion rates borrowed from other countries or industries. **Check:** which step loses the most people?

### Customer acquisition cost (CAC) · تكلفة اكتساب العميل
**Plain words:** what you spend on marketing and sales to win one new customer. **Work it out:** total acquisition spend ÷ new customers. **Example:** 9000 SAR ads + 3000 SAR sales time ÷ 40 new clients = 300 SAR each. **Watch out:** counting only ad spend. **Check:** what did your last ten customers cost to win?

### Customer lifetime value (LTV) · القيمة الدائمة للعميل
**Plain words:** the gross margin a customer brings over the whole time they stay. **Work it out:** monthly revenue per customer × gross margin ÷ monthly churn: `bizcalc.py ltv-cac`. **Example:** 49 USD a month, 80% margin, 4% churn: 39.20 a month for about 25 months = 980 USD. **Watch out:** using revenue instead of margin. **Check:** what share of customers leave each month?

### LTV to CAC ratio and payback · نسبة القيمة الدائمة إلى تكلفة الاكتساب وفترة الاسترداد
**Plain words:** how many times a customer pays back the cost of winning them, and how many months that takes. **Example:** LTV 980 ÷ CAC 245 = 4.0; payback 245 ÷ 39.20 = 6.3 months. Many investors look for about 3 or more and payback within a year: conventions, not laws. **Check:** what happens to the ratio if churn doubles?

### Sales process and pipeline · عملية البيع ومسار الصفقات
**Plain words:** the stages a deal passes through (lead, meeting, proposal, decision) and how many deals sit at each. **Why it matters:** B2B revenue depends on the pipeline months ahead. **Example:** a training company needs 30 meetings to send 10 proposals and win 3 contracts a month. **Check:** how long does your typical deal take from first contact to payment?

### Sales targets · أهداف المبيعات
**Plain words:** the units, customers and revenue you commit to by given dates. **Why it matters:** targets must match the funnel, capacity and forecast, or readers see wishful thinking. **Example:** 20 new subscribers a month from 80 trials at 25% conversion. **Check:** which funnel numbers produce your month-6 target?

## Operations and team

### Key activities and resources · الأنشطة والموارد الرئيسية
**Plain words:** what you must do very well and what you need to do it: people, equipment, premises, technology, licences, money. **Example:** a food truck's key activities are cooking, location choice and permits; key resources the truck, the cook and the permit. **Check:** which resource, if lost tomorrow, would stop the business?

### Capacity and utilisation · الطاقة الإنتاجية ونسبة الاستخدام
**Plain words:** capacity is the most you can deliver in a period; utilisation is the share used. **Work it out:** `bizcalc.py capacity --capacity C --demand D`. **Example:** a salon with 3 stylists × 8 hours × 26 days = 624 hours; 470 booked = 75%. Above about 85%, small problems cause delays. **Check:** what limits your capacity first: people, equipment or space?

### Suppliers and minimum order quantity · الموردون والحد الأدنى للطلب
**Plain words:** the minimum order quantity is the smallest batch a supplier will sell. **Why it matters:** large minimums tie up cash and space. **Example:** a cosmetics brand must buy 5000 bottles at once, about four months of sales. **Check:** what is your most critical input, and who is your backup?

### Licences and compliance · التراخيص والامتثال
**Plain words:** the registrations, permits and rules the business must meet to operate legally. **Why it matters:** missing one can close the business; banks check this. **Example:** a home bakery needs business registration, a food-safety certificate and labelling rules before selling to shops. **Watch out:** rules from memory; check official sources and ask a professional. **Check:** which licence takes longest to get?

### Team gaps and hiring plan · فجوات الفريق وخطة التوظيف
**Plain words:** the skills the plan needs but the team lacks, and when and how you will fill them. **Example:** two technical founders plan a part-time sales lead from month 3 and an accountant on contract. **Watch out:** hiring plans with no salary in the forecast. **Check:** which missing skill would hurt most in the next six months?

## Validation

### Evidence ladder · سُلَّم الأدلة
**Plain words:** evidence gets stronger from 0 to 5: assumption, desk research, interviews, commitments (deposits, letters of intent), first paid sales, repeat purchases. **Why it matters:** readers trust levels 3–5 far more than 0–2. **Example:** 40 people liked a post (level 0–1); 12 paid a deposit (level 3). **Check:** what is the highest level you have reached so far?

### Customer interviews · مقابلات العملاء
**Plain words:** short conversations about what customers did in the past, not opinions about your idea. **How:** ask about the last time the problem happened, what they tried, what it cost; do not pitch; listen. **Example:** "Tell me about the last time your delivery was late. What did you do?" beats "Would you use our app?". **Check:** how many people outside friends and family have you interviewed?

### Minimum viable product and experiments · المنتج الأدنى القابل للتطبيق والتجارب
**Plain words:** the smallest, cheapest test that tells you whether a key assumption is true. **Example:** before buying a 200000 EGP machine, a founder sells hand-made batches to 10 cafés for four weeks. **Watch out:** tests with no pass or fail line. **Check:** what result would make you change your plan?

### Traction metrics · مؤشرات الزخم
**Plain words:** the few numbers that show real progress: paying customers, revenue, repeat rate, recurring revenue, utilisation. **Example:** "Monthly recurring revenue up from 2000 to 6500 USD in five months [Verified: billing records]." **Watch out:** downloads and followers as proof of demand. **Check:** which number would you show a reader first?

### Pilots and letters of intent · المشاريع التجريبية وخطابات النوايا
**Plain words:** a pilot is a limited real use by a customer, ideally paid; a letter of intent states a customer's intention to buy on stated terms. **Why it matters:** both move evidence to level 3–4. **Example:** a paid three-month pilot with two hotels at half price, converting to a full contract if waste falls by 20%. **Check:** what would your first customer sign today?

## Financials

### Assumptions register · سجل الافتراضات
**Plain words:** a table of every assumption behind the numbers, its value, label, source and how you will check it. **Why it matters:** it lets readers challenge inputs, not just results. **Example:** "A3: café clients reorder weekly · Estimate · 6 weeks of order data from 4 cafés · confirm with 8 more weeks by April." **Check:** which assumption, if wrong, hurts the plan most?

### Revenue forecast drivers · محركات توقعات الإيرادات
**Plain words:** build revenue from the things that cause it (customers, visits, conversion, price, capacity) month by month, not from a target total. **Example:** subscriptions: start 100, add 20 a month, lose 5% a month: month 1 = 115, month 2 = 129.25 subscribers. **Watch out:** reaching full capacity in month one. **Check:** what limits your sales growth: leads, staff or production?

### Fixed and variable costs · التكاليف الثابتة والمتغيرة
**Plain words:** fixed costs stay the same whatever you sell (rent, salaries, software); variable costs rise with each sale (ingredients, packaging, commissions). **Example:** a print shop's rent is fixed; paper and ink are variable. **Watch out:** forgetting founder pay, accounting, insurance and maintenance. **Check:** which costs rise when you sell one more unit?

### Payroll on-costs · تكاليف التوظيف الإضافية
**Plain words:** the employer costs on top of salary: social insurance, other levies and benefits. **Example:** if the employer share is 20%, a salary of 8000 costs 9600 a month. **Watch out:** rates from memory: use the country profile, label them To confirm and ask an accountant. **Check:** which people in your plan will be insured, and from when?

### Profit versus cash · الربح مقابل النقد
**Plain words:** profit is income minus costs on paper; cash is money in the bank. A sale on 60-day terms is profit now and cash later. **Why it matters:** businesses close for lack of cash, not lack of profit. **Example:** a wholesaler books 100000 of sales in March but collects in May while paying salaries in March and April. **Check:** in which month is your cash lowest?

### Cash flow and cash low point · التدفق النقدي وأدنى رصيد نقدي
**Plain words:** month-by-month money in and out; the low point is the lowest balance you reach. **Work it out:** `scripts/fin_model.py`. **Why it matters:** the low point sets how much funding you need. **Watch out:** ignoring loan repayments, tax and equipment purchases. **Check:** what is your cash low point, and when?

### Runway and burn rate · مدة الصمود ومعدل الحرق
**Plain words:** burn rate is how much cash you lose a month; runway is how many months the cash lasts. **Example:** 450000 EGP in the bank and a 75000 monthly burn gives 6 months of runway. **Check:** when must you raise money or reach break-even?

### Scenarios and sensitivity · السيناريوهات وتحليل الحساسية
**Plain words:** scenarios change several assumptions together (base, downside, upside); sensitivity changes one at a time to see which matters most. **Example:** with sales 30% slower, cash falls below zero in month 7: the plan adds a credit line. **Check:** which single input moves your cash the most?

### Funding need and use of funds · الاحتياج التمويلي واستخدام الأموال
**Plain words:** the money needed so cash never falls below a safety buffer, and exactly what it pays for. **Work it out:** `bizcalc.py funding-need --low-point L --buffer B`. **Example:** low point −80000, buffer 60000: need 140000; the use-of-funds lines add up to exactly 140000. **Watch out:** round asks with no link to the cash flow. **Check:** which milestones will this money reach?

### Loans and debt service · القروض وخدمة الدين
**Plain words:** debt service is the interest and principal you repay each period; lenders compare it with the cash you generate (DSCR). **Work it out:** `bizcalc.py loan --amount A --rate R --months N --grace G`; `bizcalc.py dscr`. **Example:** 100000 at 18% over 24 months with 3 months' grace: 1500 a month interest-only, then 5586.55 a month. DSCR 9000 ÷ 6000 = 1.5. **Check:** can your monthly cash cover the instalment in the downside case?

### Equity and dilution · حقوق الملكية والتخفيف
**Plain words:** selling a share of the company for investment; dilution is the drop in the founders' percentage. **Example:** 500000 invested at a 2000000 pre-money valuation gives a 2500000 post-money value: the investor owns 20%. **Watch out:** valuation is a negotiation, not a formula. **Check:** how much of the company are you willing to sell for this round?

### Capital spending and depreciation · الإنفاق الرأسمالي والإهلاك
**Plain words:** buying long-lasting assets; the cost is spread over their useful life in the profit and loss, while the cash leaves at purchase. **Example:** a 120000 oven used for 60 months costs 2000 a month in depreciation, but 120000 of cash in month one. **Check:** which purchases could you lease instead?

### Tax questions for an accountant · أسئلة الضرائب للمحاسب
**Plain words:** taxes and registrations differ by country and change often, so the plan lists questions rather than conclusions. **Example:** "Must we register for VAT in year one? Which small-business regime applies? Do our prices include tax?" **Watch out:** stating rates from memory. **Check:** who is your accountant, and when will you ask them?

## Risks and strategy

### Risk register · سجل المخاطر
**Plain words:** a table of what could go wrong, how likely and how bad (1–3 each), what you do now to reduce it, and what you will do if it happens. **Example:** "Largest client (35% of sales) leaves · likelihood 2, impact 3 · sign 3 new mid-size clients by Q3 · trigger: notice received, cut ad spend and offer a 3-month contract." **Check:** which risk would you lose sleep over?

### Mission, vision and values · الرسالة والرؤية والقيم
**Plain words:** vision is where you are going, mission is what you do every day to get there, values are the rules for decisions. **Example:** vision: "the trusted repair partner for 500 offices in Jeddah by 2030"; value: "we never leave a client without a working printer overnight". **Watch out:** slogans anyone could write. **Check:** which value would cost you money to keep?

### Milestones and action plan · المحطات الرئيسية وخطة العمل
**Plain words:** milestones are dated results that prove progress; the action plan lists who does what by when. **Example:** "First 10 paying cafés by 30 April · owner: Sara". **Watch out:** actions with no owner. **Check:** what must happen in the next 30 days?

### Key performance indicators (KPIs) · مؤشرات الأداء الرئيسية
**Plain words:** the few numbers you check every month to know you are on track. **Example:** monthly revenue, gross margin %, new customers, repeat rate, cash at month end. **Watch out:** tracking twenty numbers. **Check:** which number would make you change course if it fell?

### Impact and the SDGs · الأثر وأهداف التنمية المستدامة
**Plain words:** the social or environmental change the business causes, measured over time; the UN Sustainable Development Goals give a shared language. **Example:** a recycling cooperative tracks tonnes recycled and income earned by members, linked to one or two specific SDG targets. **Watch out:** listing many goals with no measurement. **Check:** which indicator will you measure every quarter?

## Summary

### Executive summary · الملخص التنفيذي
**Plain words:** one page that tells the whole story and ends with the ask; many readers read nothing else. **How:** write it last, from saved sections, with the key numbers. **Watch out:** a page about passion with no numbers. **Check:** could a stranger repeat your business in two sentences after reading it?

### Elevator pitch · العرض المختصر
**Plain words:** a 20–30 second spoken version: who you help, the problem, your solution, proof and the ask. **Example:** "We help small clinics in Riyadh halve no-shows with reminders and a waitlist. Three clinics already pay us 300 riyals a month. We're raising 400000 to reach 100 clinics." **Check:** can you say yours without notes?
