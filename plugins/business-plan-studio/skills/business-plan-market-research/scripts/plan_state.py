#!/usr/bin/env python3
"""plan_state.py - the plan's memory: one JSON state file the coach reads and updates.

Usage: python3 plan_state.py [--file plan_state.json] <command> ...

  init      [--name N] [--one-liner T] [--type ID] [--stage S] [--country C] [--currency CUR]
            [--language CODE] [--audience ID] [--level new|some|expert] [--mode guided|quick|focus|review]
            [--goal T] [--deadline YYYY-MM-DD] [--force]
  setting   KEY VALUE                  language (any code: en, ar, es...), level, mode, audience, currency,
                                       business_type, stage, country
  set       SECTION --text T [--label L] [--source S] [--status S]
  status    SECTION STATUS             todo | doing | draft | done | skipped | later
  label     SECTION LABEL              Verified | Estimate | Planned | "To confirm"
  num       KEY VALUE [--unit U] [--label L] [--source S] [--section SECTION]
  import-numbers FILE [--source S] [--label L]     e.g. the --state-export file of fin_model.py
  import-sections FILE [--status S]    save many sections at once from a JSON file:
                                       {"customer.problem": {"text": "...", "label": "Estimate", "status": "draft"}, ...}
                                       (a plain string works as the text; default status draft)
  list      NAME VALUE [VALUE ...]     named lists, e.g. competitors, segments
  action    WHAT --owner O --due YYYY-MM-DD        adds to lists.actions
  assume    TEXT [--value V] [--label L] [--validate HOW] [--owner O] [--due D] [--section S]
  question  TEXT [--section S] [--for WHO]
  resolve   ID [--answer TEXT]          closes an assumption (A1...) or a question (Q1...)
  lesson    NAME                        records a lesson as taught, so it is not repeated in later sessions
  show      [SECTION]                   one section, or a compact overview
  map       [--lang en|ar]              progress map in the reader's order (Markdown)
  next                                  the next section to work on
  migrate   OLD_FILE                    convert a version 1 file into this format
  validate                              check the file against the schema

Section ids, statuses and labels come from plan_catalog.py. Every change is timestamped;
section texts keep their previous versions in "history". Standard library only.
"""
import argparse
import datetime as dt
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import plan_catalog as cat  # noqa: E402

LEVEL_CHOICES = ["new", "some", "expert"]
MODE_CHOICES = ["guided", "quick", "focus", "review"]
WEIGHT = {"done": 1.0, "draft": 0.6, "doing": 0.3, "todo": 0.0, "skipped": 0.0, "later": 0.0}


def now():
    return dt.datetime.now().isoformat(timespec="seconds")


def die(msg, code=2):
    print(f"Error: {msg}", file=sys.stderr)
    sys.exit(code)


def load(path, must=True):
    if not os.path.exists(path):
        if must:
            die(f"no state file at {path}. Run: plan_state.py --file {path} init ...")
        return None
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except json.JSONDecodeError as e:
        die(f"{path} is not valid JSON ({e})")


def save(path, st, event=None):
    st["updated"] = now()
    if event:
        st.setdefault("log", []).append({"at": st["updated"], "event": event})
        st["log"] = st["log"][-200:]
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(st, fh, ensure_ascii=False, indent=2)
    os.replace(tmp, path)


def new_state():
    t = now()
    return {"schema_version": cat.SCHEMA_VERSION, "created": t, "updated": t,
            "settings": {"language": "en", "level": "some", "mode": "guided", "audience": "incubator",
                         "currency": "", "business_type": "", "stage": "", "country": ""},
            "sections": {}, "numbers": {}, "lists": {}, "assumptions": [], "questions": [], "log": []}


def need_section(sid):
    if not cat.valid_section(sid):
        close = [s for s in cat.section_index() if s.split(".")[0] == sid.split(".")[0]]
        die(f"unknown section '{sid}'." + (f" Sections in this module: {', '.join(close)}" if close else
                                           " Run 'map' to see the section ids."))


def need_label(lbl):
    if lbl is None:
        return None
    for L in cat.LABELS:
        if lbl.lower() == L.lower():
            return L
    die(f"label must be one of: {', '.join(cat.LABELS)}")


def section(st, sid):
    return st["sections"].setdefault(sid, {"status": "todo", "text": "", "label": None, "sources": [],
                                           "updated": None, "history": []})


def cmd_init(a, path):
    if os.path.exists(path) and not a.force:
        die(f"{path} already exists. Use --force to start again (the old file will be kept as {path}.bak)")
    if os.path.exists(path):
        os.replace(path, path + ".bak")
    st = new_state()
    s = st["settings"]
    if a.type and a.type not in cat.BUSINESS_TYPES:
        die(f"--type must be one of: {', '.join(cat.BUSINESS_TYPES)}")
    if a.audience and a.audience not in cat.AUDIENCES:
        die(f"--audience must be one of: {', '.join(cat.AUDIENCES)}")
    if a.stage and a.stage not in cat.STAGES:
        die(f"--stage must be one of: {', '.join(cat.STAGES)}")
    for k, v in (("language", a.language), ("level", a.level), ("mode", a.mode), ("audience", a.audience),
                 ("currency", a.currency), ("business_type", a.type), ("stage", a.stage), ("country", a.country)):
        if v:
            s[k] = v
    fill = {"profile.name": a.name, "profile.one_liner": a.one_liner,
            "profile.business_type": cat.BUSINESS_TYPES.get(a.type, "") if a.type else None,
            "profile.stage": a.stage, "profile.location": ", ".join(x for x in (a.country, a.currency) if x) or None,
            "profile.audience": cat.AUDIENCE_NAMES.get(a.audience) if a.audience else None,
            "profile.goal": a.goal, "profile.deadline": a.deadline}
    for sid, txt in fill.items():
        if txt:
            sec = section(st, sid)
            sec.update({"text": txt, "status": "done", "updated": now()})
    save(path, st, "init")
    print(f"Created {path} ({sum(1 for v in fill.values() if v)} profile fields filled)")


def cmd_setting(a, path):
    st = load(path)
    key, val = a.key, a.value
    allowed = {"level": LEVEL_CHOICES, "mode": MODE_CHOICES,
               "audience": list(cat.AUDIENCES), "business_type": list(cat.BUSINESS_TYPES), "stage": cat.STAGES}
    if key not in ("language", "level", "mode", "audience", "currency", "business_type", "stage", "country"):
        die("setting must be one of language, level, mode, audience, currency, business_type, stage, country")
    if key in allowed and val not in allowed[key]:
        die(f"{key} must be one of: {', '.join(allowed[key])}")
    st["settings"][key] = val
    save(path, st, f"setting {key}={val}")
    print(f"{key} = {val}")


def cmd_set(a, path):
    need_section(a.section)
    st = load(path)
    sec = section(st, a.section)
    if sec["text"]:
        sec["history"].append({"text": sec["text"], "label": sec["label"], "at": sec["updated"]})
        sec["history"] = sec["history"][-10:]
    sec["text"] = a.text
    if a.label:
        sec["label"] = need_label(a.label)
    if a.source:
        sec["sources"].append(a.source)
    if a.status:
        if a.status not in cat.STATUSES:
            die(f"status must be one of: {', '.join(cat.STATUSES)}")
        sec["status"] = a.status
    elif sec["status"] in ("todo", "doing", "later", "skipped"):
        sec["status"] = "draft"
    sec["updated"] = now()
    save(path, st, f"set {a.section}")
    print(f"Saved {a.section} ({len(a.text)} characters, status {sec['status']}, label {sec['label'] or 'none'})")


def cmd_status(a, path):
    need_section(a.section)
    if a.status not in cat.STATUSES:
        die(f"status must be one of: {', '.join(cat.STATUSES)}")
    st = load(path)
    section(st, a.section)["status"] = a.status
    save(path, st, f"status {a.section}={a.status}")
    print(f"{a.section}: {cat.STATUS_TEXT[a.status]}")


def cmd_label(a, path):
    need_section(a.section)
    st = load(path)
    section(st, a.section)["label"] = need_label(a.label)
    save(path, st, f"label {a.section}")
    print(f"{a.section}: {section(st, a.section)['label']}")


def parse_value(v):
    try:
        f = float(str(v).replace(",", ""))
        return int(f) if f.is_integer() else f
    except ValueError:
        return v


def cmd_num(a, path):
    st = load(path)
    if a.section:
        need_section(a.section)
    st["numbers"][a.key] = {"value": parse_value(a.value), "unit": a.unit, "label": need_label(a.label),
                            "source": a.source, "section": a.section, "updated": now()}
    save(path, st, f"num {a.key}")
    print(f"{a.key} = {a.value}{(' ' + a.unit) if a.unit else ''} ({need_label(a.label) or 'no label yet'})")


def cmd_import(a, path):
    st = load(path)
    data = load(a.input_file)
    if not isinstance(data, dict):
        die("the import file must be a JSON object of key: value")
    for k, v in data.items():
        st["numbers"][k] = {"value": v, "unit": None, "label": need_label(a.label) or "Estimate",
                            "source": a.source, "section": None, "updated": now()}
    save(path, st, f"import {len(data)} numbers from {a.source}")
    print(f"Imported {len(data)} numbers from {a.input_file}")


def cmd_import_sections(a, path):
    st = load(path)
    data = load(a.input_file)
    if not isinstance(data, dict):
        die("the file must be a JSON object of section id: text or {text, label, status}")
    default = a.status or "draft"
    if default not in cat.STATUSES:
        die(f"status must be one of: {', '.join(cat.STATUSES)}")
    bad = [k for k in data if not cat.valid_section(k)]
    if bad:
        die(f"unknown section id(s): {', '.join(bad)}. Nothing was saved. Run 'map' or see plan_catalog.py for the ids.")
    for sid, v in data.items():
        if isinstance(v, str):
            v = {"text": v}
        text = (v.get("text") or "").strip()
        if not text:
            continue
        status = v.get("status") or default
        if status not in cat.STATUSES:
            die(f"{sid}: status must be one of: {', '.join(cat.STATUSES)}")
        sec = section(st, sid)
        if sec["text"]:
            sec["history"].append({"text": sec["text"], "label": sec["label"], "at": sec["updated"]})
            sec["history"] = sec["history"][-10:]
        sec.update({"text": text, "status": status, "updated": now()})
        if v.get("label"):
            sec["label"] = need_label(v["label"])
        if v.get("source"):
            sec["sources"].append(v["source"])
    save(path, st, f"import {len(data)} sections")
    print(f"Saved {len(data)} sections from {a.input_file}")


def cmd_list(a, path):
    st = load(path)
    st["lists"][a.name] = a.values
    save(path, st, f"list {a.name}")
    print(f"{a.name}: {', '.join(a.values)}")


def cmd_action(a, path):
    st = load(path)
    st["lists"].setdefault("actions", []).append({"what": a.what, "owner": a.owner, "due": a.due})
    save(path, st, "action")
    print(f"Action added: {a.what} ({a.owner or 'no owner'}, {a.due or 'no date'})")


def cmd_assume(a, path):
    st = load(path)
    if a.section:
        need_section(a.section)
    aid = f"A{len(st['assumptions']) + 1}"
    st["assumptions"].append({"id": aid, "text": a.text, "value": a.value, "label": need_label(a.label) or "Estimate",
                              "validate": a.validate, "owner": a.owner, "due": a.due, "section": a.section,
                              "status": "open", "created": now()})
    save(path, st, f"assume {aid}")
    print(f"{aid} recorded: {a.text}")


def cmd_question(a, path):
    st = load(path)
    if a.section:
        need_section(a.section)
    qid = f"Q{len(st['questions']) + 1}"
    st["questions"].append({"id": qid, "text": a.text, "section": a.section, "for": a.for_,
                            "status": "open", "answer": None, "created": now()})
    save(path, st, f"question {qid}")
    print(f"{qid} recorded: {a.text}")


def cmd_resolve(a, path):
    st = load(path)
    pool = st["assumptions"] if a.id.upper().startswith("A") else st["questions"]
    for item in pool:
        if item["id"].upper() == a.id.upper():
            item["status"] = "closed"
            if a.answer:
                item["answer"] = a.answer
            save(path, st, f"resolve {a.id}")
            print(f"{a.id} closed")
            return
    die(f"no assumption or question with id {a.id}")


def cmd_lesson(a, path):
    st = load(path)
    taught = st["lists"].setdefault("lessons_taught", [])
    if a.name not in taught:
        taught.append(a.name)
    save(path, st, f"lesson {a.name}")
    print(f"Lessons taught so far: {', '.join(taught)}")


def progress(st):
    order = cat.AUDIENCES.get(st["settings"].get("audience") or "incubator", cat.module_ids())
    mods = cat.module_by_id()
    rows = []
    for mid in order:
        _id, en, ar, mins, secs = mods[mid]
        stats = [st["sections"].get(sid, {}).get("status", "todo") for sid, _e, _a in secs]
        score = sum(WEIGHT[s] for s in stats) / len(stats)
        rows.append({"module": mid, "en": en, "ar": ar, "minutes": mins, "sections": len(secs),
                     "done": stats.count("done"), "draft": stats.count("draft"),
                     "later": stats.count("later") + stats.count("skipped"), "pct": round(score * 100)})
    return rows


def bar(pct, width=10):
    full = round(pct / 100 * width)
    return "#" * full + "." * (width - full)


def cmd_map(a, path):
    st = load(path)
    lang = a.lang or st["settings"].get("language", "en")
    if lang != "ar":
        lang = "en"  # the map has English and Arabic wording; other languages: translate it in the reply
    rows = progress(st)
    total = round(sum(r["pct"] * r["sections"] for r in rows) / sum(r["sections"] for r in rows))
    name = st["sections"].get("profile.name", {}).get("text") or "Business plan"
    if lang == "ar":
        aud_ar = cat.AUDIENCE_NAMES_AR.get(st["settings"].get("audience"), "")
        print(f"**{name}**: اكتمال الخطة {total}%" + (f" (القارئ: {aud_ar})" if aud_ar else "") + "\n")
        print("| # | المحور | التقدم | الحالة |\n|---|---|---|---|")
    else:
        aud = cat.AUDIENCE_NAMES.get(st["settings"].get("audience"), "")
        print(f"**{name}**: plan {total}% complete" + (f" (for: {aud})" if aud else "") + "\n")
        print("| # | Module | Progress | Status |\n|---|---|---|---|")
    for i, r in enumerate(rows, 1):
        if r["pct"] == 100:
            status = "مكتمل" if lang == "ar" else "done"
        elif r["pct"] == 0 and not r["later"]:
            status = (f"لم يبدأ (~{r['minutes']} دقيقة)" if lang == "ar" else f"not started (~{r['minutes']} min)")
        else:
            parts = []
            if r["done"]:
                parts.append(f"{r['done']}/{r['sections']} " + ("مكتمل" if lang == "ar" else "done"))
            if r["draft"]:
                parts.append(f"{r['draft']} " + ("مسودة" if lang == "ar" else "draft"))
            if r["later"]:
                parts.append(f"{r['later']} " + ("مؤجل" if lang == "ar" else "later"))
            status = ", ".join(parts) or ("قيد العمل" if lang == "ar" else "in progress")
        name_col = r["ar"] if lang == "ar" else r["en"]
        print(f"| {i} | {name_col} | `{bar(r['pct'])}` {r['pct']}% | {status} |")
    open_a = sum(1 for x in st["assumptions"] if x["status"] == "open")
    open_q = sum(1 for x in st["questions"] if x["status"] == "open")
    if open_a or open_q:
        print(("\nافتراضات مفتوحة: " if lang == "ar" else "\nOpen assumptions: ") + str(open_a) +
              (" · أسئلة مفتوحة: " if lang == "ar" else " · open questions: ") + str(open_q))


def next_section(st):
    order = cat.AUDIENCES.get(st["settings"].get("audience") or "incubator", cat.module_ids())
    mods = cat.module_by_id()
    for pref in (("doing",), ("todo",), ("draft",), ("later",)):
        for mid in order:
            for sid, _e, _a in mods[mid][4]:
                if st["sections"].get(sid, {}).get("status", "todo") in pref:
                    return sid
    return None


def cmd_next(a, path):
    st = load(path)
    sid = next_section(st)
    if not sid:
        print("All sections are done. Suggested next step: run check_plan.py, then render the outputs.")
        return
    mid, en, ar = cat.section_index()[sid]
    print(f"{sid} ({en} / {ar}) in module {mid}; status {st['sections'].get(sid, {}).get('status', 'todo')}")


def cmd_show(a, path):
    st = load(path)
    if a.section:
        need_section(a.section)
        print(json.dumps(st["sections"].get(a.section, {"status": "todo"}), ensure_ascii=False, indent=2))
        return
    s = st["settings"]
    print(f"Settings: {json.dumps(s, ensure_ascii=False)}")
    filled = {k: v for k, v in st["sections"].items() if v.get("text")}
    print(f"Sections with text: {len(filled)} of {len(cat.section_index())}")
    for sid, v in filled.items():
        t = v["text"].replace("\n", " ")
        print(f"- {sid} [{v['status']}, {v.get('label') or 'no label'}]: {t[:90]}{'...' if len(t) > 90 else ''}")
    taught = st["lists"].get("lessons_taught") or []
    if taught:
        print(f"Lessons already taught: {', '.join(taught)}")
    print(f"Numbers: {len(st['numbers'])} · Lists: {', '.join(st['lists']) or 'none'} · "
          f"Open assumptions: {sum(1 for x in st['assumptions'] if x['status'] == 'open')} · "
          f"Open questions: {sum(1 for x in st['questions'] if x['status'] == 'open')}")


def cmd_migrate(a, path):
    old = load(a.old_file)
    if old.get("schema_version") == cat.SCHEMA_VERSION:
        die("that file is already version 2")
    if os.path.exists(path):
        die(f"{path} exists; choose another --file for the migrated plan")
    st = new_state()
    intake = old.get("intake", {})
    st["settings"].update({k: intake.get(k, "") for k in ("currency", "country")})
    st["settings"]["language"] = intake.get("language") or "en"
    if intake.get("company"):
        section(st, "profile.name").update({"text": intake["company"], "status": "done", "updated": now()})
    portal_map = {"1.1": "customer.segments", "1.3": "customer.priority_segment", "1.4": "customer.persona",
                  "1.5": "customer.problem", "1.6": "offer.value_proposition", "2.3": "operations.resources",
                  "2.4": "operations.activities", "4.2": "competition.competitors", "4.4": "competition.swot",
                  "4.6": "competition.advantage", "5.1": "customer.persona", "5.2": "gtm.channels",
                  "5.5": "gtm.targets", "6.1": "financials.costs", "6.4": "model.pricing", "6.7": "market.size",
                  "7.1": "financials.forecast", "7.5": "financials.cash_flow", "8.4": "strategy.action_plan"}
    moved = 0
    for old_id, v in (old.get("sections") or {}).items():
        new_id = portal_map.get(old_id)
        if not new_id:
            st.setdefault("unmapped_v1", {})[old_id] = v
            continue
        sec = section(st, new_id)
        texts = [f"{k}: {f['value']}" for k, f in (v.get("fields") or {}).items() if f.get("value")]
        if texts:
            sec["text"] = "\n".join(texts)
        sec["status"] = {"complete": "done", "draft": "draft", "needs review": "draft", "skipped": "skipped"}.get(
            v.get("status"), "todo")
        for q in v.get("open_questions") or []:
            st["questions"].append({"id": f"Q{len(st['questions']) + 1}", "text": q, "section": new_id,
                                    "for": None, "status": "open", "answer": None, "created": now()})
        moved += 1
    save(path, st, f"migrated from {a.old_file}")
    print(f"Migrated {moved} sections into {path}; {len(st.get('unmapped_v1', {}))} kept under 'unmapped_v1'")


def cmd_validate(a, path):
    st = load(path)
    errs = []
    if st.get("schema_version") != cat.SCHEMA_VERSION:
        errs.append(f"schema_version is {st.get('schema_version')}, expected {cat.SCHEMA_VERSION} (use migrate)")
    for k in ("settings", "sections", "numbers", "lists", "assumptions", "questions"):
        if k not in st:
            errs.append(f"missing '{k}'")
    for sid, v in st.get("sections", {}).items():
        if not cat.valid_section(sid):
            errs.append(f"unknown section id {sid}")
        if v.get("status") not in cat.STATUSES:
            errs.append(f"{sid}: bad status {v.get('status')}")
        if v.get("label") not in cat.LABELS + [None]:
            errs.append(f"{sid}: bad label {v.get('label')}")
    for k, v in st.get("numbers", {}).items():
        if v.get("label") not in cat.LABELS + [None]:
            errs.append(f"number {k}: bad label {v.get('label')}")
    if errs:
        print("Problems found:\n- " + "\n- ".join(errs))
        sys.exit(1)
    print("State file is valid.")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--file", default="plan_state.json")
    sub = p.add_subparsers(dest="cmd")
    s = sub.add_parser("init")
    for o in ("name", "one-liner", "type", "stage", "country", "currency", "audience", "goal", "deadline"):
        s.add_argument(f"--{o}")
    s.add_argument("--language", help="language code of the conversation, e.g. en, ar, es, fr")
    s.add_argument("--level", choices=LEVEL_CHOICES)
    s.add_argument("--mode", choices=MODE_CHOICES)
    s.add_argument("--force", action="store_true")
    s = sub.add_parser("setting"); s.add_argument("key"); s.add_argument("value")
    s = sub.add_parser("set"); s.add_argument("section"); s.add_argument("--text", required=True)
    s.add_argument("--label"); s.add_argument("--source"); s.add_argument("--status")
    s = sub.add_parser("status"); s.add_argument("section"); s.add_argument("status")
    s = sub.add_parser("label"); s.add_argument("section"); s.add_argument("label")
    s = sub.add_parser("num"); s.add_argument("key"); s.add_argument("value")
    s.add_argument("--unit"); s.add_argument("--label"); s.add_argument("--source"); s.add_argument("--section")
    s = sub.add_parser("import-numbers"); s.add_argument("input_file"); s.add_argument("--source", default="fin_model.py")
    s.add_argument("--label")
    s = sub.add_parser("import-sections"); s.add_argument("input_file"); s.add_argument("--status")
    s = sub.add_parser("list"); s.add_argument("name"); s.add_argument("values", nargs="+")
    s = sub.add_parser("action"); s.add_argument("what"); s.add_argument("--owner"); s.add_argument("--due")
    s = sub.add_parser("assume"); s.add_argument("text"); s.add_argument("--value"); s.add_argument("--label")
    s.add_argument("--validate"); s.add_argument("--owner"); s.add_argument("--due"); s.add_argument("--section")
    s = sub.add_parser("question"); s.add_argument("text"); s.add_argument("--section")
    s.add_argument("--for", dest="for_")
    s = sub.add_parser("resolve"); s.add_argument("id"); s.add_argument("--answer")
    s = sub.add_parser("lesson"); s.add_argument("name")
    s = sub.add_parser("show"); s.add_argument("section", nargs="?")
    s = sub.add_parser("map"); s.add_argument("--lang", choices=["en", "ar"])
    sub.add_parser("next")
    s = sub.add_parser("migrate"); s.add_argument("old_file")
    sub.add_parser("validate")
    a = p.parse_args(argv)
    if not a.cmd:
        p.print_help()
        sys.exit(2)
    fn = {"init": cmd_init, "setting": cmd_setting, "set": cmd_set, "status": cmd_status, "label": cmd_label,
          "num": cmd_num, "import-numbers": cmd_import, "import-sections": cmd_import_sections, "list": cmd_list, "action": cmd_action,
          "assume": cmd_assume, "question": cmd_question, "resolve": cmd_resolve, "lesson": cmd_lesson,
          "show": cmd_show,
          "map": cmd_map, "next": cmd_next, "migrate": cmd_migrate, "validate": cmd_validate}[a.cmd]
    fn(a, a.file)


if __name__ == "__main__":
    try:  # stay quiet when the output is piped into head or similar
        import signal
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except (ImportError, AttributeError, ValueError):
        pass
    main()
