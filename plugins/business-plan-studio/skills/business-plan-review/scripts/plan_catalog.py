"""Shared catalogue of plan modules, sections, audiences and labels.

Imported by plan_state.py, check_plan.py and render_plan.py (keep this file in the
same folder as those scripts). Standard library only.
"""

SCHEMA_VERSION = 2

LABELS = ["Verified", "Estimate", "Planned", "To confirm"]
LABELS_AR = {"Verified": "مؤكَّد", "Estimate": "تقدير", "Planned": "مخطَّط", "To confirm": "بحاجة إلى تأكيد"}

STATUSES = ["todo", "doing", "draft", "done", "skipped", "later"]
STATUS_TEXT = {
    "todo": "not started", "doing": "in progress", "draft": "draft", "done": "done",
    "skipped": "skipped", "later": "come back later",
}

# id, English name, Arabic name, minutes for a guided pass, sections [(id, EN title, AR title)]
MODULES = [
    ("profile", "Business snapshot", "لمحة عن المشروع", 5, [
        ("profile.name", "Business name", "اسم المشروع"),
        ("profile.one_liner", "One-line description", "وصف المشروع في سطر"),
        ("profile.business_type", "Business type", "نوع النشاط"),
        ("profile.stage", "Stage", "مرحلة المشروع"),
        ("profile.location", "Location and currency", "الموقع والعملة"),
        ("profile.audience", "Plan reader", "قارئ الخطة"),
        ("profile.goal", "Goal of the plan", "هدف الخطة"),
        ("profile.deadline", "Deadline", "الموعد النهائي"),
        ("profile.assets", "What exists already", "ما هو متوفر حاليًا"),
    ]),
    ("customer", "Customer and problem", "العميل والمشكلة", 15, [
        ("customer.segments", "Customer segments", "شرائح العملاء"),
        ("customer.priority_segment", "Priority segment", "الشريحة ذات الأولوية"),
        ("customer.persona", "Ideal customer profile", "ملف العميل المثالي"),
        ("customer.problem", "Problem or need", "المشكلة أو الحاجة"),
        ("customer.alternatives", "Current alternatives", "البدائل الحالية"),
    ]),
    ("offer", "Offer and value proposition", "العرض والقيمة المقدمة", 10, [
        ("offer.description", "Product or service", "المنتج أو الخدمة"),
        ("offer.benefits", "Benefits", "الفوائد"),
        ("offer.value_proposition", "Value proposition", "القيمة المقدمة"),
        ("offer.why_now", "Why now", "لماذا الآن"),
    ]),
    ("market", "Market", "السوق", 15, [
        ("market.size", "Market size", "حجم السوق"),
        ("market.trends", "Trends", "الاتجاهات"),
        ("market.regulation", "Rules and licences", "القواعد والتراخيص"),
    ]),
    ("competition", "Competition and positioning", "المنافسة والتموضع", 15, [
        ("competition.competitors", "Competitors", "المنافسون"),
        ("competition.comparison", "Comparison", "المقارنة"),
        ("competition.positioning", "Positioning", "التموضع"),
        ("competition.advantage", "Competitive advantage", "الميزة التنافسية"),
        ("competition.swot", "SWOT", "التحليل الرباعي (SWOT)"),
    ]),
    ("model", "Business model and pricing", "نموذج العمل والتسعير", 15, [
        ("model.revenue_streams", "Revenue streams", "مصادر الإيرادات"),
        ("model.pricing", "Pricing", "التسعير"),
        ("model.unit_economics", "Unit economics", "اقتصاديات الوحدة"),
        ("model.payment_terms", "Payment terms", "شروط الدفع"),
    ]),
    ("gtm", "Go-to-market and sales", "الوصول إلى السوق والمبيعات", 15, [
        ("gtm.channels", "Channels", "قنوات الوصول"),
        ("gtm.marketing", "Marketing plan", "خطة التسويق"),
        ("gtm.sales_process", "Sales process", "عملية البيع"),
        ("gtm.partnerships", "Partnerships", "الشراكات"),
        ("gtm.targets", "Sales targets", "أهداف المبيعات"),
    ]),
    ("operations", "Operations and resources", "العمليات والموارد", 10, [
        ("operations.activities", "Key activities", "الأنشطة الرئيسية"),
        ("operations.resources", "Key resources", "الموارد الرئيسية"),
        ("operations.suppliers", "Suppliers", "الموردون"),
        ("operations.location_equipment", "Location and equipment", "الموقع والمعدات"),
        ("operations.legal", "Legal and compliance", "الشؤون القانونية والامتثال"),
    ]),
    ("team", "Team", "الفريق", 10, [
        ("team.founders", "Founders", "المؤسسون"),
        ("team.gaps", "Skill gaps", "الفجوات في المهارات"),
        ("team.hiring_plan", "Hiring plan", "خطة التوظيف"),
        ("team.advisors", "Advisors and mentors", "المستشارون والمرشدون"),
    ]),
    ("validation", "Validation and traction", "التحقق والمؤشرات المبكرة", 10, [
        ("validation.evidence", "Evidence so far", "الأدلة حتى الآن"),
        ("validation.experiments", "Experiments", "التجارب"),
        ("validation.metrics", "Traction metrics", "مؤشرات الزخم"),
        ("validation.learnings", "Learnings", "الدروس المستفادة"),
    ]),
    ("financials", "Financial plan", "الخطة المالية", 30, [
        ("financials.assumptions", "Key assumptions", "الافتراضات الرئيسية"),
        ("financials.forecast", "Sales forecast", "توقعات المبيعات"),
        ("financials.costs", "Costs", "التكاليف"),
        ("financials.cash_flow", "Cash flow", "التدفق النقدي"),
        ("financials.break_even", "Break-even", "نقطة التعادل"),
        ("financials.scenarios", "Scenarios", "السيناريوهات"),
        ("financials.funding", "Funding need and use of funds", "الاحتياج التمويلي واستخدام الأموال"),
    ]),
    ("risks", "Risks", "المخاطر", 10, [
        ("risks.register", "Risk register", "سجل المخاطر"),
    ]),
    ("strategy", "Strategy, milestones and impact", "الاستراتيجية والمحطات والأثر", 10, [
        ("strategy.vision_mission", "Vision, mission and values", "الرؤية والرسالة والقيم"),
        ("strategy.milestones", "Milestones", "المحطات الرئيسية"),
        ("strategy.action_plan", "Action plan", "خطة العمل التنفيذية"),
        ("strategy.kpis", "KPIs", "مؤشرات الأداء الرئيسية"),
        ("strategy.impact", "Impact", "الأثر"),
    ]),
    ("summary", "Executive summary", "الملخص التنفيذي", 10, [
        ("summary.executive", "Executive summary", "الملخص التنفيذي"),
        ("summary.one_pager", "One-page summary", "ملخص من صفحة واحدة"),
    ]),
]

AUDIENCES = {
    "incubator": ["profile", "customer", "offer", "validation", "market", "competition", "model",
                  "gtm", "operations", "team", "financials", "risks", "strategy", "summary"],
    "bank": ["profile", "offer", "customer", "operations", "team", "market", "competition", "model",
             "gtm", "validation", "financials", "risks", "strategy", "summary"],
    "investor": ["profile", "customer", "offer", "market", "validation", "competition", "model",
                 "gtm", "team", "operations", "financials", "strategy", "risks", "summary"],
    "grant": ["profile", "customer", "offer", "strategy", "validation", "operations", "team",
              "financials", "risks", "market", "competition", "model", "gtm", "summary"],
    "internal": ["profile", "offer", "customer", "gtm", "operations", "team", "model", "financials",
                 "strategy", "risks", "market", "competition", "validation", "summary"],
    "partner": ["profile", "offer", "customer", "market", "model", "gtm", "operations", "team",
                "strategy", "risks", "financials", "competition", "validation", "summary"],
}
AUDIENCE_NAMES = {
    "incubator": "Incubator or accelerator", "bank": "Bank or lender", "investor": "Investor",
    "grant": "Grant or donor programme", "internal": "Internal plan (founders and team)",
    "partner": "Partner, distributor or landlord",
}

AUDIENCE_NAMES_AR = {
    "incubator": "حاضنة أو مسرّعة أعمال", "bank": "بنك أو جهة إقراض", "investor": "مستثمر",
    "grant": "برنامج منح أو جهة مانحة", "internal": "خطة داخلية للمؤسسين والفريق",
    "partner": "شريك أو موزّع أو مؤجِّر",
}

BUSINESS_TYPES = {
    "services": "Services (agency, consultancy, professional or B2B services)",
    "saas-subscription": "Software or subscription",
    "ecommerce-d2c": "E-commerce or direct-to-consumer brand",
    "retail-store": "Physical retail shop",
    "food-service": "Restaurant, café, cloud kitchen or catering",
    "manufacturing": "Manufacturing or food processing",
    "trade-distribution": "Import, export, wholesale or distribution",
    "marketplace-platform": "Marketplace or platform",
    "appointment-experience": "Clinic, salon, gym, training centre, tours or events",
    "social-enterprise": "Social enterprise, NGO or cooperative",
}

STAGES = ["idea", "building", "selling", "growing"]


def module_ids():
    return [m[0] for m in MODULES]


def section_index():
    """Return {section_id: (module_id, en_title, ar_title)}."""
    out = {}
    for mid, _en, _ar, _mins, sections in MODULES:
        for sid, en, ar in sections:
            out[sid] = (mid, en, ar)
    return out


def module_by_id():
    return {m[0]: m for m in MODULES}


def valid_section(sid):
    return sid in section_index()
