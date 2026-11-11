#!/usr/bin/env python3
"""check_plan.py - run the plan's consistency checks (C01-C14) on the state file.

Usage: python3 check_plan.py [--file plan_state.json] [--json] [--only C03,C06]

Each check reads numbers, lists and sections from the state file. When the numbers a
check needs are missing it reports "n/a" with the keys to add. Results: pass,
advisory (worth a look), blocking (a reader will reject or question the plan).

Number keys the checks use (set with plan_state.py num KEY VALUE, or import the
--state-export file of fin_model.py):
  offer.<name>.price, offer.<name>.unit_cost, offer.<name>.min_price          C01
  capacity.<name>, demand.<name>   (same unit and period, e.g. loaves per day)  C02
  market.som, forecast.revenue_y1                                              C03
  target.<YYYY-MM>, forecast.revenue.<YYYY-MM>                                C04
  team.headcount, model.headcount_peak                                         C05
  cash.low_point, cash.buffer                                                  C06
  funding.ask, funding.need_without_financing (or funding.need)              C07
  use_of_funds.<item> (one per item), funding.ask                              C08
  unit.ltv, unit.cac, unit.payback_months                                      C09
  assumption.growth_pct_monthly, forecast.revenue_y1, forecast.revenue_y2      C10
  model.gross_margin_pct_y1, stated.gross_margin_pct                           C11
Lists: competitors (C14), segments (C14), actions (C13, via plan_state.py action).
Thresholds marked "rule of thumb" are conventions to discuss with the founder, not laws.
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import plan_catalog as cat  # noqa: E402

GROWTH_RULE_PCT = 15      # rule of thumb: >15% a month for a year is rare outside very early bases
SOM_SHARE_ADVISORY = 0.5  # year-1 revenue above half of SOM is aggressive
TARGET_TOLERANCE = 0.10   # targets within 10% of the forecast count as consistent
USE_OF_FUNDS_TOL = 0.01   # 1% rounding tolerance
MARGIN_GAP_PTS = 5        # stated vs modelled gross margin
LTV_CAC_MIN, PAYBACK_MAX = 3, 12


def val(nums, key):
    v = nums.get(key)
    if v is None:
        return None
    v = v.get("value") if isinstance(v, dict) else v
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def r(cid, status, detail, fix=""):
    return {"check": cid, "status": status, "detail": detail, "fix": fix}


def checks(st):
    nums = st.get("numbers", {})
    lists = st.get("lists", {})
    secs = st.get("sections", {})
    out = []

    # C01 price vs cost
    offers = sorted({k.split(".")[1] for k in nums if k.startswith("offer.") and k.count(".") >= 2})
    found = False
    for o in offers:
        p = val(nums, f"offer.{o}.price")
        uc, mp = val(nums, f"offer.{o}.unit_cost"), val(nums, f"offer.{o}.min_price")
        if p is None or (uc is None and mp is None):
            continue
        found = True
        floor = max(x for x in (uc, mp) if x is not None)
        what = "minimum price" if mp is not None and floor == mp else "unit cost"
        if p < floor:
            out.append(r("C01", "blocking", f"{o}: price {p:g} is below its {what} {floor:g}",
                         "Raise the price, cut the cost, or explain why this item is sold at a loss"))
        elif p < floor * 1.1:
            out.append(r("C01", "advisory", f"{o}: price {p:g} is within 10% of its {what} {floor:g}",
                         "Thin margin: check every cost is included"))
        else:
            out.append(r("C01", "pass", f"{o}: price {p:g} covers its {what} {floor:g}"))
    if not found:
        out.append(r("C01", "n/a", "no offer with both a price and a cost", "add offer.<name>.price and offer.<name>.unit_cost or .min_price"))

    # C02 capacity vs demand
    caps = {k[len("capacity."):]: val(nums, k) for k in nums if k.startswith("capacity.")}
    done = False
    for name, cap in caps.items():
        dem = val(nums, f"demand.{name}")
        if cap is None or dem is None:
            continue
        done = True
        use = dem / cap * 100 if cap else float("inf")
        if use > 100:
            out.append(r("C02", "blocking", f"{name}: demand {dem:g} is above capacity {cap:g} ({use:.0f}%)",
                         "Add capacity (hire, shift, equipment), slow the forecast, or raise prices"))
        elif use > 85:
            out.append(r("C02", "advisory", f"{name}: demand uses {use:.0f}% of capacity", "Little room for sick days, peaks or rework"))
        else:
            out.append(r("C02", "pass", f"{name}: demand uses {use:.0f}% of capacity"))
    if not done:
        out.append(r("C02", "n/a", "no matching capacity.<name> and demand.<name>", "add both in the same unit and period"))

    # C03 SOM vs year-1 revenue
    som, y1 = val(nums, "market.som"), val(nums, "forecast.revenue_y1")
    if som is None or y1 is None:
        out.append(r("C03", "n/a", "needs market.som and forecast.revenue_y1"))
    elif y1 > som:
        out.append(r("C03", "blocking", f"year-1 revenue {y1:,.0f} is above the SOM {som:,.0f}",
                     "Recheck the SOM method or lower the forecast"))
    elif y1 > som * SOM_SHARE_ADVISORY:
        out.append(r("C03", "advisory", f"year-1 revenue is {y1 / som:.0%} of the SOM (rule of thumb: above 50% is aggressive)",
                     "Explain how you win that share so fast"))
    else:
        out.append(r("C03", "pass", f"year-1 revenue is {y1 / som:.0%} of the SOM"))

    # C04 targets vs forecast
    tg = {k[len("target."):]: val(nums, k) for k in nums if k.startswith("target.")}
    hits = 0
    for m, t in sorted(tg.items()):
        f = val(nums, f"forecast.revenue.{m}")
        if f is None or t is None:
            continue
        hits += 1
        gap = (t - f) / f if f else float("inf")
        if abs(gap) > TARGET_TOLERANCE:
            out.append(r("C04", "advisory", f"{m}: target {t:,.0f} vs forecast {f:,.0f} ({gap:+.0%})",
                         "Align the sales target with the forecast, or explain the difference"))
        else:
            out.append(r("C04", "pass", f"{m}: target matches the forecast ({gap:+.0%})"))
    if not hits:
        out.append(r("C04", "n/a", "needs target.<YYYY-MM> with a matching forecast.revenue.<YYYY-MM>"))

    # C05 team vs payroll
    th, mh = val(nums, "team.headcount"), val(nums, "model.headcount_peak")
    if th is None or mh is None:
        out.append(r("C05", "n/a", "needs team.headcount and model.headcount_peak"))
    elif abs(th - mh) > 0.01:
        out.append(r("C05", "advisory", f"team section plans {th:g} people; the model pays {mh:g}",
                     "Every person in the team plan needs a cost, and every cost a person"))
    else:
        out.append(r("C05", "pass", f"team plan and payroll both show {th:g} people"))

    # C06 cash never below zero
    low, buf = val(nums, "cash.low_point"), val(nums, "cash.buffer")
    if low is None:
        out.append(r("C06", "n/a", "needs cash.low_point (run fin_model.py --state-export)"))
    elif low < 0:
        month = (nums.get("cash.low_point_month") or {}).get("value", "")
        out.append(r("C06", "blocking", f"cash falls to {low:,.0f} {('in ' + str(month)) if month else ''}".strip(),
                     "Show how the gap is funded (equity, loan, grant, slower spending, faster collection)"))
    elif buf is not None and low < buf:
        out.append(r("C06", "advisory", f"cash low point {low:,.0f} is under the buffer {buf:,.0f}", "Plan a buffer for surprises"))
    else:
        out.append(r("C06", "pass", f"cash stays at or above {low:,.0f}"))

    # C07 funding ask vs need
    ask = val(nums, "funding.ask")
    need = val(nums, "funding.need_without_financing")
    if need is None:
        need = val(nums, "funding.need")
    if ask is None or need is None:
        out.append(r("C07", "n/a", "needs funding.ask and funding.need"))
    elif ask < need:
        out.append(r("C07", "blocking", f"ask {ask:,.0f} is below the funding need {need:,.0f}",
                     "Raise the ask, add another source, or change the plan so the need falls"))
    elif need == 0 and ask > 0:
        out.append(r("C07", "advisory", f"the model needs no funding but the plan asks for {ask:,.0f}", "Say what the money speeds up"))
    elif ask > need * 1.5:
        out.append(r("C07", "advisory", f"ask {ask:,.0f} is more than 1.5 times the need {need:,.0f}", "Justify the extra or lower the ask"))
    else:
        out.append(r("C07", "pass", f"ask {ask:,.0f} covers the need {need:,.0f}"))

    # C08 use of funds adds up
    uses = {k: val(nums, k) for k in nums if k.startswith("use_of_funds.")}
    if not uses or ask is None:
        out.append(r("C08", "n/a", "needs use_of_funds.<item> lines and funding.ask"))
    else:
        tot = sum(v for v in uses.values() if v is not None)
        if abs(tot - ask) > max(1.0, ask * USE_OF_FUNDS_TOL):
            out.append(r("C08", "blocking", f"use of funds adds to {tot:,.0f} but the ask is {ask:,.0f}",
                         "Make the lines add up to the ask exactly"))
        else:
            out.append(r("C08", "pass", f"use of funds adds up to the ask ({tot:,.0f})"))

    # C09 LTV/CAC and payback
    ltv, cac, pb = val(nums, "unit.ltv"), val(nums, "unit.cac"), val(nums, "unit.payback_months")
    if ltv is None or cac is None:
        out.append(r("C09", "n/a", "needs unit.ltv and unit.cac (repeat-purchase and subscription models)"))
    else:
        ratio = ltv / cac if cac else float("inf")
        st_ = "blocking" if ratio < 1 else ("advisory" if ratio < LTV_CAC_MIN else "pass")
        out.append(r("C09", st_, f"LTV/CAC is {ratio:.1f}" + (" (rule of thumb: 3 or more)" if st_ != "pass" else ""),
                     "Lower acquisition cost, raise margin or retention" if st_ != "pass" else ""))
        if pb is not None and pb > PAYBACK_MAX:
            out.append(r("C09", "advisory", f"CAC payback {pb:g} months (rule of thumb: within 12)", "Shorten payback or show the cash to carry it"))

    # C10 growth sanity
    g = val(nums, "assumption.growth_pct_monthly")
    y2 = val(nums, "forecast.revenue_y2")
    flags = []
    if g is not None and g > GROWTH_RULE_PCT:
        flags.append(f"monthly growth assumption {g:g}% (rule of thumb: above {GROWTH_RULE_PCT}% for a year is rare)")
    if y1 and y2 and y2 / y1 > 4:
        flags.append(f"year 2 revenue is {y2 / y1:.1f} times year 1")
    if g is None and not (y1 and y2):
        out.append(r("C10", "n/a", "needs assumption.growth_pct_monthly or forecast.revenue_y1 and _y2"))
    elif flags:
        out.append(r("C10", "advisory", "; ".join(flags), "Tie growth to a driver you control (sales capacity, budget, channels)"))
    else:
        out.append(r("C10", "pass", "growth assumptions look moderate"))

    # C11 margin sanity
    gm, sgm = val(nums, "model.gross_margin_pct_y1"), val(nums, "stated.gross_margin_pct")
    if gm is None:
        out.append(r("C11", "n/a", "needs model.gross_margin_pct_y1"))
    elif gm < 0:
        out.append(r("C11", "blocking", f"gross margin is negative ({gm:g}%)", "Every sale loses money before overheads"))
    elif sgm is not None and abs(gm - sgm) > MARGIN_GAP_PTS:
        out.append(r("C11", "advisory", f"plan text says {sgm:g}% gross margin; the model gives {gm:g}%", "Use one number"))
    else:
        out.append(r("C11", "pass", f"gross margin {gm:g}%"))

    # C12 unlabelled numbers
    unl = [k for k, v in nums.items() if isinstance(v, dict) and not v.get("label")]
    unl_secs = [sid for sid, v in secs.items() if v.get("text") and re.search(r"\d", v["text"])
                and not v.get("label") and not sid.startswith("profile.")]
    if unl or unl_secs:
        out.append(r("C12", "advisory", f"{len(unl)} number(s) and {len(unl_secs)} section(s) with figures have no claim label"
                     + (f": {', '.join((unl + unl_secs)[:6])}" if unl or unl_secs else ""),
                     "Add Verified, Estimate, Planned or To confirm"))
    else:
        out.append(r("C12", "pass", "every number carries a claim label"))

    # C13 actions with owner and date
    acts = lists.get("actions") or []
    if not acts:
        ap = secs.get("strategy.action_plan", {})
        if ap.get("status") in ("done", "draft"):
            out.append(r("C13", "advisory", "action plan has text but no structured actions",
                         "Add each action with plan_state.py action WHAT --owner --due"))
        else:
            out.append(r("C13", "n/a", "no actions recorded yet"))
    else:
        bad = [x["what"] for x in acts if not x.get("owner") or not x.get("due")]
        if bad:
            out.append(r("C13", "advisory", f"{len(bad)} action(s) without an owner or date: {', '.join(bad[:4])}", "Give each an owner and a date"))
        else:
            out.append(r("C13", "pass", f"{len(acts)} actions, each with an owner and a date"))

    # C14 names consistent
    comp = lists.get("competitors") or []
    ctext = (secs.get("competition.comparison", {}).get("text") or "").lower()
    if comp and ctext:
        miss = [c for c in comp if c.lower() not in ctext]
        out.append(r("C14", "advisory" if miss else "pass",
                     f"competitors missing from the comparison: {', '.join(miss)}" if miss else "competitor names match the comparison",
                     "Use the same names everywhere" if miss else ""))
    segs = lists.get("segments") or []
    ptext = (secs.get("customer.priority_segment", {}).get("text") or "").lower()
    if segs and ptext:
        ok = any(s.lower() in ptext for s in segs)
        out.append(r("C14", "pass" if ok else "advisory",
                     "priority segment is one of the listed segments" if ok else "priority segment does not match any listed segment",
                     "" if ok else "Name the priority segment exactly as in the segment list"))
    if not ((comp and ctext) or (segs and ptext)):
        out.append(r("C14", "n/a", "needs lists competitors or segments plus the matching section text"))
    return out


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--file", default="plan_state.json")
    p.add_argument("--json", action="store_true")
    p.add_argument("--only")
    a = p.parse_args(argv)
    if not os.path.exists(a.file):
        print(f"Error: no state file at {a.file}", file=sys.stderr)
        sys.exit(2)
    with open(a.file, encoding="utf-8") as fh:
        st = json.load(fh)
    res = checks(st)
    if a.only:
        keep = {x.strip().upper() for x in a.only.split(",")}
        res = [x for x in res if x["check"] in keep]
    order = {"blocking": 0, "advisory": 1, "pass": 2, "n/a": 3}
    res.sort(key=lambda x: (order[x["status"]], x["check"]))
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return
    counts = {k: sum(1 for x in res if x["status"] == k) for k in order}
    print(f"Checks: {counts['blocking']} blocking, {counts['advisory']} advisory, {counts['pass']} pass, {counts['n/a']} not enough data\n")
    print("| Check | Result | What we found | Suggested fix |\n|---|---|---|---|")
    for x in res:
        print(f"| {x['check']} | {x['status']} | {x['detail']} | {x['fix']} |")


if __name__ == "__main__":
    try:  # stay quiet when the output is piped into head or similar
        import signal
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except (ImportError, AttributeError, ValueError):
        pass
    main()
