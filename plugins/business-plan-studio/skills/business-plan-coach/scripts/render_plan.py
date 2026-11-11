#!/usr/bin/env python3
"""render_plan.py - draft the plan's outputs from the state file.

Usage: python3 render_plan.py [--file plan_state.json] OUTPUT [--audience ID] [--lang en|ar]
                              [--include-empty] [--out FILE]
OUTPUT is one of:
  --plan                 the full plan in the reader's order (default)
  --one-pager            a one-page summary
  --canvas bmc|lean      Business Model Canvas or Lean Canvas as a Markdown table
  --deck-outline         a 12-slide pitch outline with the content each slide draws on
  --paste-pack FORM.json one block per form field, with character counts against the limit
  --registers            assumptions, open questions and actions

The output is a draft for Claude to polish with the founder: it copies saved section texts
and claim labels; it never invents content. Missing sections appear as [To do] lines when
--include-empty is used. Standard library only.
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import plan_catalog as cat  # noqa: E402

BMC = [("Key partners", ["gtm.partnerships", "operations.suppliers"]),
       ("Key activities", ["operations.activities"]),
       ("Key resources", ["operations.resources", "team.founders"]),
       ("Value proposition", ["offer.value_proposition"]),
       ("Customer relationships", ["gtm.sales_process"]),
       ("Channels", ["gtm.channels"]),
       ("Customer segments", ["customer.priority_segment", "customer.segments"]),
       ("Cost structure", ["financials.costs"]),
       ("Revenue streams", ["model.revenue_streams", "model.pricing"])]
LEAN = [("Problem", ["customer.problem", "customer.alternatives"]),
        ("Customer segments", ["customer.priority_segment"]),
        ("Unique value proposition", ["offer.value_proposition"]),
        ("Solution", ["offer.description"]),
        ("Channels", ["gtm.channels"]),
        ("Revenue streams", ["model.revenue_streams", "model.pricing"]),
        ("Cost structure", ["financials.costs"]),
        ("Key metrics", ["validation.metrics", "strategy.kpis"]),
        ("Unfair advantage", ["competition.advantage"])]
DECK = [("Title and one-liner", ["profile.name", "profile.one_liner"]),
        ("Problem", ["customer.problem"]),
        ("Solution and value proposition", ["offer.description", "offer.value_proposition"]),
        ("Why now", ["offer.why_now", "market.trends"]),
        ("Market size", ["market.size"]),
        ("Customer and go-to-market", ["customer.priority_segment", "gtm.channels"]),
        ("Business model", ["model.revenue_streams", "model.pricing", "model.unit_economics"]),
        ("Traction and validation", ["validation.evidence", "validation.metrics"]),
        ("Competition", ["competition.comparison", "competition.advantage"]),
        ("Team", ["team.founders", "team.hiring_plan"]),
        ("Financials", ["financials.forecast", "financials.cash_flow", "financials.break_even"]),
        ("The ask and use of funds", ["financials.funding", "strategy.milestones"])]
ONE_PAGER = [("What we do", ["profile.one_liner", "offer.value_proposition"]),
             ("The problem", ["customer.problem"]),
             ("Who we serve", ["customer.priority_segment"]),
             ("Market", ["market.size"]),
             ("How we make money", ["model.revenue_streams", "model.pricing"]),
             ("Traction", ["validation.evidence", "validation.metrics"]),
             ("Competition and advantage", ["competition.advantage"]),
             ("Team", ["team.founders"]),
             ("Financial headline", ["financials.forecast", "financials.break_even"]),
             ("What we need", ["financials.funding"])]


AR = {
    "Key partners": "الشركاء الرئيسيون", "Key activities": "الأنشطة الرئيسية", "Key resources": "الموارد الرئيسية",
    "Value proposition": "القيمة المقدمة", "Customer relationships": "العلاقة مع العملاء", "Channels": "القنوات",
    "Customer segments": "شرائح العملاء", "Cost structure": "هيكل التكاليف", "Revenue streams": "مصادر الإيرادات",
    "Problem": "المشكلة", "Unique value proposition": "القيمة الفريدة المقدمة", "Solution": "الحل",
    "Key metrics": "المؤشرات الرئيسية", "Unfair advantage": "الميزة التي يصعب نسخها",
    "Title and one-liner": "العنوان ووصف المشروع في سطر", "Solution and value proposition": "الحل والقيمة المقدمة",
    "Why now": "لماذا الآن", "Market size": "حجم السوق", "Customer and go-to-market": "العميل وطريقة الوصول إلى السوق",
    "Business model": "نموذج العمل", "Traction and validation": "المؤشرات المبكرة والتحقق",
    "Competition": "المنافسة", "Team": "الفريق", "Financials": "الأرقام المالية",
    "The ask and use of funds": "التمويل المطلوب واستخدامه", "What we do": "ماذا نقدّم", "The problem": "المشكلة",
    "Who we serve": "من نخدم", "Market": "السوق", "How we make money": "كيف نحقق الإيرادات",
    "Traction": "المؤشرات المبكرة", "Competition and advantage": "المنافسة والميزة التنافسية",
    "Financial headline": "أبرز الأرقام المالية", "What we need": "ما نحتاجه",
    "Business Model Canvas": "نموذج العمل التجاري", "Lean Canvas": "النموذج المرن (Lean Canvas)",
    "Pitch deck outline": "مخطط العرض التقديمي", "Slide": "الشريحة", "Draws on": "المصدر",
    "one-page summary": "ملخص من صفحة واحدة",
}


def tr(text, lang):
    return AR.get(text, text) if lang == "ar" else text


def load(path):
    if not os.path.exists(path):
        sys.exit(f"Error: no state file at {path}")
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def label_tag(lbl, lang):
    if not lbl:
        return ""
    return f" [{cat.LABELS_AR[lbl]}]" if lang == "ar" else f" [{lbl}]"


def text_of(st, sids, lang, limit=None, with_label=True):
    parts = []
    for sid in sids:
        s = st["sections"].get(sid) or {}
        if s.get("text"):
            t = s["text"].strip()
            if limit and len(t) > limit:
                t = t[:limit].rsplit(" ", 1)[0] + "..."
            parts.append(t + (label_tag(s.get("label"), lang) if with_label else ""))
    return "\n\n".join(parts)


def todo(lang):
    return "[للإنجاز]" if lang == "ar" else "[To do]"


def plan(st, audience, lang, include_empty):
    idx = cat.module_by_id()
    name = (st["sections"].get("profile.name") or {}).get("text") or ("خطة العمل" if lang == "ar" else "Business plan")
    L = [f"# {name}", ""]
    aud = (cat.AUDIENCE_NAMES_AR if lang == "ar" else cat.AUDIENCE_NAMES).get(audience, audience)
    L.append(f"_{'مسودة خطة عمل موجهة إلى' if lang == 'ar' else 'Draft business plan for'}: {aud}_\n")
    order = cat.AUDIENCES.get(audience, cat.module_ids())
    order = ["summary"] + [m for m in order if m not in ("summary", "profile")]
    n = 0
    for mid in order:
        _id, en, ar, _mins, secs = idx[mid]
        body = []
        for sid, sen, sar in secs:
            s = st["sections"].get(sid) or {}
            if s.get("text"):
                body.append(f"### {sar if lang == 'ar' else sen}\n\n{s['text'].strip()}{label_tag(s.get('label'), lang)}\n")
            elif include_empty:
                body.append(f"### {sar if lang == 'ar' else sen}\n\n{todo(lang)}\n")
        if body:
            n += 1
            L.append(f"## {n}. {ar if lang == 'ar' else en}\n")
            L.extend(body)
    return "\n".join(L)


def table(st, rows, lang, title):
    L = [f"# {tr(title, lang)}", "", "| " + ("الخانة" if lang == "ar" else "Block") + " | " + ("المحتوى" if lang == "ar" else "Content") + " |", "|---|---|"]
    for blk, sids in rows:
        t = text_of(st, sids, lang, limit=300).replace("\n", " ").replace("|", "/") or todo(lang)
        L.append(f"| {tr(blk, lang)} | {t} |")
    return "\n".join(L)


def deck(st, lang):
    L = [f"# {tr('Pitch deck outline', lang)}", ""]
    for i, (title, sids) in enumerate(DECK, 1):
        t = text_of(st, sids, lang, limit=400) or todo(lang)
        L.append(f"## {tr('Slide', lang)} {i}: {tr(title, lang)}\n\n{tr('Draws on', lang)}: {', '.join(sids)}\n\n{t}\n")
    return "\n".join(L)


def one_pager(st, lang):
    name = (st["sections"].get("profile.name") or {}).get("text") or "Business"
    L = [f"# {name}: {tr('one-page summary', lang)}", ""]
    for title, sids in ONE_PAGER:
        t = text_of(st, sids, lang, limit=350) or todo(lang)
        L.append(f"**{tr(title, lang)}.** {t}\n")
    return "\n".join(L)


def digits_only(text):
    return re.sub(r"(?<=\d)[,٬  ](?=\d{3}\b)", "", text)


def paste_pack(st, form_path, lang):
    with open(form_path, encoding="utf-8") as fh:
        form = json.load(fh)
    L = [f"# Paste pack: {form.get('form', 'form')}", ""]
    over = 0
    for f in form.get("fields", []):
        if f.get("calculated_by_portal"):
            continue
        t = text_of(st, f.get("maps_to", []), lang, with_label=False)
        if (f.get("number_format") or form.get("number_format", "")).startswith("digits"):
            t = digits_only(t)
        lim = f.get("limit_chars")
        n = len(t)
        flag = ""
        if lim and n > lim:
            flag = f" OVER LIMIT by {n - lim}"
            over += 1
        L.append(f"## {f.get('page', '')} {f.get('label', f.get('id'))}".strip())
        L.append(f"Characters: {n}" + (f" / {lim}" if lim else "") + flag)
        L.append("```text\n" + (t or "[nothing saved for this field yet]") + "\n```\n")
    L.insert(1, f"{over} field(s) over their limit. Labels are left out of pasted text; keep them in the plan.\n")
    return "\n".join(L)


def registers(st):
    L = ["# Assumptions, open questions and actions", "", "## Assumptions register", "",
         "| Id | Assumption | Value | Label | How to validate | Owner | Due | Status |", "|---|---|---|---|---|---|---|---|"]
    for a in st.get("assumptions", []):
        L.append(f"| {a['id']} | {a['text']} | {a.get('value') or ''} | {a.get('label') or ''} | {a.get('validate') or ''} | "
                 f"{a.get('owner') or ''} | {a.get('due') or ''} | {a['status']} |")
    L += ["", "## Open questions", "", "| Id | Question | Section | For | Status |", "|---|---|---|---|---|"]
    for q in st.get("questions", []):
        L.append(f"| {q['id']} | {q['text']} | {q.get('section') or ''} | {q.get('for') or ''} | {q['status']} |")
    L += ["", "## Actions", "", "| Action | Owner | Due |", "|---|---|---|"]
    for x in st.get("lists", {}).get("actions", []):
        L.append(f"| {x['what']} | {x.get('owner') or ''} | {x.get('due') or ''} |")
    return "\n".join(L)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--file", default="plan_state.json")
    g = p.add_mutually_exclusive_group()
    g.add_argument("--plan", action="store_true")
    g.add_argument("--one-pager", action="store_true")
    g.add_argument("--canvas", choices=["bmc", "lean"])
    g.add_argument("--deck-outline", action="store_true")
    g.add_argument("--paste-pack")
    g.add_argument("--registers", action="store_true")
    p.add_argument("--audience", choices=list(cat.AUDIENCES))
    p.add_argument("--lang", choices=["en", "ar"])
    p.add_argument("--include-empty", action="store_true")
    p.add_argument("--out")
    a = p.parse_args(argv)
    st = load(a.file)
    lang = a.lang or st.get("settings", {}).get("language", "en")
    if lang != "ar":
        lang = "en"  # headings in English or Arabic; translate other languages when polishing
    aud = a.audience or st.get("settings", {}).get("audience") or "incubator"
    if a.one_pager:
        text = one_pager(st, lang)
    elif a.canvas:
        text = table(st, BMC if a.canvas == "bmc" else LEAN, lang,
                     "Business Model Canvas" if a.canvas == "bmc" else "Lean Canvas")
    elif a.deck_outline:
        text = deck(st, lang)
    elif a.paste_pack:
        text = paste_pack(st, a.paste_pack, lang)
    elif a.registers:
        text = registers(st)
    else:
        text = plan(st, aud, lang, a.include_empty)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as fh:
            fh.write(text + "\n")
        print(f"Wrote {a.out}")
    else:
        print(text)


if __name__ == "__main__":
    try:  # stay quiet when the output is piped into head or similar
        import signal
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except (ImportError, AttributeError, ValueError):
        pass
    main()
