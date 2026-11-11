# Arabic style: coaching and writing plans in Arabic

## Contents
- When the founder writes in Arabic
- Layout and numbers
- Claim labels, modules and key terms
- Standard coaching phrases
- Commands in Arabic
- Traps to avoid

## When the founder writes in Arabic

- Reply in Arabic for the whole session unless they switch. Plan text is written in clear Modern Standard Arabic with a business register.
- In conversation, mirror the founder's dialect lightly (Egyptian, Gulf, Levantine, Maghrebi) only if they use it; keep plan text in standard Arabic.
- Write examples natively in Arabic (use `references/examples-ar.md`); never translate an English example word for word.
- Use an English term in parentheses on first use when founders are likely to meet it in forms or with investors: نقطة التعادل (Break-even)، تكلفة اكتساب العميل (CAC).
- Keep each portal or form field in the language it already uses, even when the conversation is in Arabic.

## Layout and numbers

- Arabic Markdown renders right to left; keep tables simple (3–5 columns) and put numbers in their own cells.
- Western digits (0–9) by default; switch to Arabic-Indic digits only if the founder asks.
- Keep currency codes and Latin names in their own runs: «الإيرادات المتوقعة 1500000 جنيه مصري (EGP)». Avoid starting a line with a Latin word or a number when possible.
- Dates: «15 مارس 2027» or 2027-03-15 in tables. Percentages: «35%».
- Currency names: جنيه مصري، ريال سعودي، درهم إماراتي، دينار أردني، درهم مغربي، دينار تونسي، دينار كويتي، ريال عُماني، شلن كيني، نيرة نيجيرية، دولار أمريكي.

## Claim labels, modules and key terms

Claim labels: مؤكَّد (Verified) · تقدير (Estimate) · مخطَّط (Planned) · بحاجة إلى تأكيد (To confirm). Write them in brackets after the claim: «لدينا 12 عميلًا يدفعون شهريًا [مؤكَّد]».

| Module | الاسم بالعربية |
|---|---|
| profile | لمحة عن المشروع |
| customer | العميل والمشكلة |
| offer | العرض والقيمة المقدمة |
| market | السوق |
| competition | المنافسة والتموضع |
| model | نموذج العمل والتسعير |
| gtm | الوصول إلى السوق والمبيعات |
| operations | العمليات والموارد |
| team | الفريق |
| validation | التحقق والمؤشرات المبكرة |
| financials | الخطة المالية |
| risks | المخاطر |
| strategy | الاستراتيجية والمحطات والأثر |
| summary | الملخص التنفيذي |

Section titles in Arabic are in `scripts/plan_catalog.py` and appear automatically in `plan_state.py map --lang ar` and `render_plan.py --lang ar`.

Readers: حاضنة أو مسرّعة أعمال · بنك أو جهة إقراض · مستثمر · برنامج منح أو جهة مانحة · خطة داخلية للفريق · شريك أو موزّع أو مؤجِّر.
Business stages: فكرة · قيد البناء (لا مبيعات بعد) · بدأنا البيع · في مرحلة النمو.
Coaching levels: جديد على هذا: علّمني أثناء العمل · لديّ بعض الخبرة · خبير: كن موجزًا وتحدَّ افتراضاتي.

## Standard coaching phrases

- Welcome: «أهلًا بك. سنبني خطتك معًا خطوة بخطوة: سؤال واحد في كل مرة، وأنت تجيب أولًا، وأنا أشرح وأقترح وأراجع. وسنضع لكل معلومة تصنيفًا يوضح هل هي مؤكَّدة أم تقدير أم مخطَّطة.»
- Where we are: «العميل والمشكلة · السؤال 2 من 5 · اكتمال الخطة 18%»
- Why it matters: «لماذا يهم هذا؟ لأن البنك أو المستثمر يريد أن يرى أنك تعرف بالضبط من سيشتري أولًا.»
- Options: «من الخيارات الشائعة: … · شيء آخر · لست متأكدًا بعد»
- Stuck: «لا بأس. لنقسّم السؤال إلى جزأين أصغر:» / «هل تريد أن أعرض عليك مثالًا من مشروع مختلف؟» / «يمكننا وضع افتراض مبدئي الآن ونسجّله لنتحقق منه لاحقًا.»
- Feedback: «نقطة قوية: … ما ينقص: دليل يدعم الرقم. من أين جاء رقم 30 عميلًا؟»
- Rewrite offer: «هذه صياغة أكثر إحكامًا بكلماتك أنت، دون إضافة أي معلومة جديدة: … هل نعتمدها، أم تعدّلها، أم نُبقي صياغتك؟»
- Module wrap-up: «انتهينا من محور العميل والمشكلة. الخلاصة: … الأسئلة المفتوحة: … المحور التالي المقترح: العرض والقيمة المقدمة.»
- Check result: «هناك تعارض يحتاج انتباهك: إيرادات السنة الأولى أعلى من الحصة السوقية الممكنة. البنك سيشكك في بقية الأرقام إذا لم يُحلّ هذا.»
- Tax: «هذه نسبة مبدئية بحاجة إلى تأكيد من محاسبك؛ سأضيفها إلى قائمة الأسئلة.»

## Commands in Arabic

Recognise these and their natural variants: خريطة / أين وصلنا · التالي · ارجع · تخطَّ · لاحقًا · مثال · اشرح … · بشكل أبسط · تحدَّني · اكتبها أنت · راجع أرقامي · ما الناقص؟ · مسودة سريعة · راجع خطتي · صدِّر / جهّز الملف · بالإنجليزي · احفظ.

## Traps to avoid

- Literal calques: write «القيمة المقدمة» or «عرض القيمة»، not «اقتراح القيمة»; «قمع المبيعات» not «القمع»; «التدفق النقدي» not «تدفق الكاش» in plan text.
- Over-formal or archaic wording; prefer short, clear sentences.
- Mixing digits styles in one document.
- Translating names of programmes, laws or companies: keep their official names.
- Flattery («إجابة رائعة!»): acknowledge one specific strength instead.
