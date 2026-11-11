#!/usr/bin/env python3
"""fin_model.py - driver-based monthly financial model for a business plan.

Usage
  python3 fin_model.py model.json [--format md|json|csv] [--out FILE]
                                  [--xlsx FILE] [--state-export FILE]
  python3 fin_model.py --example        print a complete example input

The input format is documented in references/model-input-format.md (financials skill)
and in the --example output. Standard library only; --xlsx needs openpyxl.

What it produces: monthly profit and loss and cash flow, yearly blocks, cash low point,
break-even month, funding need, scenarios and sensitivity. All numbers are planning
estimates: label them in the plan and keep the input file as the assumptions record.
"""
import argparse
import copy
import csv
import io
import json
import math
import re
import sys

EXAMPLE = {
    "name": "Qamar Crisps (fictional)",
    "currency": "EGP",
    "start": "2027-01",
    "months": 24,
    "opening_cash": 150000,
    "streams": [
        {"name": "Cafe wholesale", "type": "units", "volume": {"start": 1200, "growth_pct": 5, "max": 6000},
         "price": 18, "unit_cost": 7, "collection_days": 30, "price_growth_pct_yearly": 10},
        {"name": "Online shop", "type": "units", "volume": {"start": 300, "growth_pct": 8, "max": 3000},
         "price": 35, "unit_cost": 9, "variable_pct": 12}
    ],
    "fixed_costs": [
        {"name": "Kitchen rent", "monthly": 15000, "growth_pct_yearly": 10, "category": "premises"},
        {"name": "Online ads", "monthly": 8000, "category": "marketing"}
    ],
    "team": [{"role": "Baker", "count": 2, "monthly_salary": 9000, "raise_pct_yearly": 10}],
    "employer_oncost_pct": 18.75,
    "capex": [{"name": "Oven", "amount": 120000, "month": "2027-01", "life_months": 60}],
    "financing": [{"type": "loan", "amount": 100000, "month": "2027-01", "rate_pct": 18,
                   "term_months": 24, "grace_months": 3}],
    "payment_days": 30,
    "scenarios": {"downside": {"volume_pct": -30, "growth_pct_points": -2, "cost_pct": 10}},
    "sensitivity": ["price", "volume", "unit_cost"]
}

STREAM_TYPES = {"units", "subscription", "retainer", "hours", "gmv", "rental", "schedule"}
SENS_DRIVERS = {"price": "price_pct", "volume": "volume_pct", "unit_cost": "unit_cost_pct",
                "fixed_costs": "fixed_pct", "growth": "growth_scale_pct"}
SENS_STEPS = [-20, -10, 10, 20]


class ModelError(Exception):
    pass


# ---------------------------------------------------------------- helpers
def parse_month(s, field):
    try:
        y, m = str(s).split("-")
        y, m = int(y), int(m)
        if not 1 <= m <= 12:
            raise ValueError
        return y * 12 + (m - 1)
    except Exception:
        raise ModelError(f"{field}: '{s}' is not a month in YYYY-MM form")


def month_str(idx):
    return f"{idx // 12:04d}-{idx % 12 + 1:02d}"


def day_shift(days):
    """Days to whole months: 0-14 same month, 15-44 one month, 45-74 two months..."""
    d = float(days or 0)
    m = math.floor((abs(d) + 15) / 30)
    return int(m if d >= 0 else -m)


def num(d, key, field, default=None, minimum=None):
    v = d.get(key, default)
    if v is None:
        raise ModelError(f"{field}.{key} is required")
    if not isinstance(v, (int, float)) or isinstance(v, bool):
        raise ModelError(f"{field}.{key} must be a number (got {v!r})")
    if minimum is not None and v < minimum:
        raise ModelError(f"{field}.{key} must be at least {minimum} (got {v})")
    return float(v)


def ramp_value(r, i, field, pct_cap=None):
    """Value of a ramp object (or plain number) i months after the stream starts."""
    if isinstance(r, (int, float)) and not isinstance(r, bool):
        v = float(r)
    elif isinstance(r, dict):
        if "schedule" in r:
            sch = r["schedule"]
            if not isinstance(sch, list) or not sch:
                raise ModelError(f"{field}.schedule must be a non-empty list")
            v = float(sch[min(i, len(sch) - 1)])
        else:
            start = num(r, "start", field, minimum=0)
            if "growth_pts" in r:
                v = start + float(r["growth_pts"]) * i
            else:
                v = start * (1 + float(r.get("growth_pct", 0)) / 100) ** i
            if r.get("max") is not None:
                v = min(v, float(r["max"]))
    else:
        raise ModelError(f"{field} must be a number or a ramp object")
    v = max(v, 0.0)
    if pct_cap is not None:
        v = min(v, pct_cap)
    return v


# ---------------------------------------------------------------- scenario modifiers
def apply_mods(spec, mods):
    s = copy.deepcopy(spec)
    vol = 1 + mods.get("volume_pct", 0) / 100
    price = 1 + mods.get("price_pct", 0) / 100
    ucost = (1 + mods.get("cost_pct", 0) / 100) * (1 + mods.get("unit_cost_pct", 0) / 100)
    fixed = (1 + mods.get("cost_pct", 0) / 100) * (1 + mods.get("fixed_pct", 0) / 100)
    gpts = mods.get("growth_pct_points", 0)
    gscale = 1 + mods.get("growth_scale_pct", 0) / 100
    churn_pts = mods.get("churn_pct_points", 0)
    coll_add = mods.get("collection_days_add", 0)

    def scale_ramp(r, factor):
        if isinstance(r, (int, float)) and not isinstance(r, bool):
            return r * factor
        if isinstance(r, dict):
            r = dict(r)
            if "schedule" in r:
                r["schedule"] = [x * factor for x in r["schedule"]]
            else:
                r["start"] = r.get("start", 0) * factor
                if "growth_pct" in r:
                    r["growth_pct"] = r["growth_pct"] * gscale + gpts
                if "growth_pts" in r:
                    r["growth_pts"] = r["growth_pts"] * gscale
                if r.get("max") is not None and factor > 1:
                    r["max"] = r["max"] * factor
        return r

    for st in s.get("streams", []):
        t = st.get("type")
        if t == "units":
            st["volume"] = scale_ramp(st.get("volume", 0), vol)
        elif t in ("subscription", "retainer"):
            new = st.get("new", 0)
            if isinstance(new, dict) and "from_budget" in new:
                new = dict(new)
                if vol > 0:
                    new["cac"] = new["cac"] / vol  # same budget, fewer (or more) customers
                else:
                    new["from_budget"] = 0
            else:
                new = scale_ramp(new, vol)
            st["new"] = new
            st["churn_pct"] = max(0.0, st.get("churn_pct", 0) + churn_pts)
        elif t == "hours":
            st["utilisation_pct"] = scale_ramp(st.get("utilisation_pct", 0), vol)
        elif t == "gmv":
            st["gmv"] = scale_ramp(st.get("gmv", 0), vol)
            st["take_rate_pct"] = st.get("take_rate_pct", 0) * price
        elif t == "rental":
            st["occupancy_pct"] = scale_ramp(st.get("occupancy_pct", 0), vol)
        elif t == "schedule":
            st["amounts"] = {k: v * vol * price for k, v in st.get("amounts", {}).items()}
        for k in ("price", "rate"):
            if k in st:
                st[k] = st[k] * price
        if "unit_cost" in st:
            st["unit_cost"] = st["unit_cost"] * ucost
        if "cost_pct" in st:
            st["cost_pct"] = st["cost_pct"] * ucost
        if coll_add:
            st["collection_days"] = st.get("collection_days", 0) + coll_add
    for fc in s.get("fixed_costs", []):
        fc["monthly"] = fc.get("monthly", 0) * fixed
    return s


# ---------------------------------------------------------------- core
def run_model(spec):
    if not isinstance(spec, dict):
        raise ModelError("the input must be a JSON object")
    cur = spec.get("currency")
    if not cur:
        raise ModelError("currency is required (for example EGP, SAR, USD)")
    start = parse_month(spec.get("start"), "start")
    n = int(spec.get("months", 24))
    if not 12 <= n <= 60:
        raise ModelError("months must be between 12 and 60")
    months = [start + k for k in range(n)]
    streams = spec.get("streams") or []
    if not streams:
        raise ModelError("add at least one revenue stream in 'streams'")
    Z = lambda: [0.0] * n  # noqa: E731

    rev, cogs, var, extra_mkt = Z(), Z(), Z(), Z()
    cash_in_sales, cash_out_cogs = Z(), Z()
    receivables_end = payables_end = 0.0
    stream_rows = []
    over_capacity = {}
    pay_shift = day_shift(spec.get("payment_days", 0)) - day_shift(spec.get("inventory_days", 0))

    for si, st in enumerate(streams):
        f = f"streams[{si}]"
        t = st.get("type")
        if t not in STREAM_TYPES:
            raise ModelError(f"{f}.type must be one of {sorted(STREAM_TYPES)} (got {t!r})")
        name = st.get("name") or f"Stream {si + 1}"
        s0 = parse_month(st["start"], f + ".start") if st.get("start") else start
        s1 = parse_month(st["end"], f + ".end") if st.get("end") else None
        season = st.get("seasonality") or [1] * 12
        if len(season) != 12:
            raise ModelError(f"{f}.seasonality needs 12 values (January to December)")
        pg = float(st.get("price_growth_pct_yearly", 0)) / 100
        vpct = float(st.get("variable_pct", 0)) / 100
        shift = day_shift(st.get("collection_days", 0))
        srev, scogs, sdrv = Z(), Z(), Z()
        active_prev = float(st.get("customers_start", 0))
        for k, mi in enumerate(months):
            if mi < s0 or (s1 is not None and mi > s1):
                continue
            i = mi - s0
            sea = float(season[mi % 12])
            pf = (1 + pg) ** (i // 12)
            if t == "units":
                vol = ramp_value(st.get("volume", 0), i, f + ".volume") * sea
                if st.get("capacity") is not None and vol > float(st["capacity"]) + 1e-9:
                    over_capacity.setdefault(name, []).append(month_str(mi))
                price = num(st, "price", f) * pf
                r = vol * price
                c = vol * float(st.get("unit_cost", 0)) if "unit_cost" in st else r * float(st.get("cost_pct", 0)) / 100
                drv = vol
            elif t in ("subscription", "retainer"):
                new = st.get("new", 0)
                if isinstance(new, dict) and "from_budget" in new:
                    budget = num(new, "from_budget", f + ".new", minimum=0)
                    cac = num(new, "cac", f + ".new", minimum=0.01)
                    n_new = budget / cac * sea
                    extra_mkt[k] += budget
                else:
                    n_new = ramp_value(new, i, f + ".new") * sea
                churn = float(st.get("churn_pct", 0)) / 100
                if not 0 <= churn <= 1:
                    raise ModelError(f"{f}.churn_pct must be between 0 and 100")
                active = active_prev * (1 - churn) + n_new
                active_prev = active
                price = num(st, "price", f) * pf
                r = active * price
                c = active * float(st.get("unit_cost", 0)) if "unit_cost" in st else r * float(st.get("cost_pct", 0)) / 100
                drv = active
            elif t == "hours":
                caph = num(st, "capacity_hours", f, minimum=0)
                util = ramp_value(st.get("utilisation_pct", 0), i, f + ".utilisation_pct", pct_cap=100)
                billed = caph * util / 100 * sea
                rate = num(st, "rate", f) * pf
                r = billed * rate
                c = billed * float(st.get("unit_cost", 0)) if "unit_cost" in st else r * float(st.get("cost_pct", 0)) / 100
                drv = billed
            elif t == "gmv":
                g = ramp_value(st.get("gmv", 0), i, f + ".gmv") * sea
                r = g * num(st, "take_rate_pct", f, minimum=0) / 100
                c = r * float(st.get("cost_pct", 0)) / 100
                drv = g
            elif t == "rental":
                units = num(st, "units_available", f, minimum=0)
                occ = ramp_value(st.get("occupancy_pct", 0), i, f + ".occupancy_pct", pct_cap=100)
                occupied = min(units, units * occ / 100 * sea)
                price = num(st, "price", f) * pf
                r = occupied * price
                c = occupied * float(st.get("unit_cost", 0)) if "unit_cost" in st else r * float(st.get("cost_pct", 0)) / 100
                drv = occupied
            else:  # schedule
                amounts = st.get("amounts") or {}
                r = float(amounts.get(month_str(mi), 0))
                c = r * float(st.get("cost_pct", 0)) / 100
                drv = r
            srev[k], scogs[k], sdrv[k] = r, c, drv
            rev[k] += r
            cogs[k] += c
            var[k] += r * vpct
            kk = k + shift
            if kk < 0:
                kk = 0
            if kk < n:
                cash_in_sales[kk] += r
            else:
                receivables_end += r
            kp = k + pay_shift
            if kp < 0:
                kp = 0
            if kp < n:
                cash_out_cogs[kp] += c
            else:
                payables_end += c
        stream_rows.append({"name": name, "type": t, "revenue": srev, "cogs": scogs, "driver": sdrv,
                            "price": st.get("price", st.get("rate")), "unit_cost": st.get("unit_cost"),
                            "capacity_hours": st.get("capacity_hours"), "capacity": st.get("capacity")})

    fixed = Z()
    for fi, fc in enumerate(spec.get("fixed_costs") or []):
        f = f"fixed_costs[{fi}]"
        amt = num(fc, "monthly", f, minimum=0)
        c0 = parse_month(fc["start"], f + ".start") if fc.get("start") else start
        c1 = parse_month(fc["end"], f + ".end") if fc.get("end") else None
        g = float(fc.get("growth_pct_yearly", 0)) / 100
        for k, mi in enumerate(months):
            if mi >= c0 and (c1 is None or mi <= c1):
                fixed[k] += amt * (1 + g) ** ((mi - c0) // 12)
    for k in range(n):
        fixed[k] += extra_mkt[k]

    salaries, heads = Z(), Z()
    for ti, tm in enumerate(spec.get("team") or []):
        f = f"team[{ti}]"
        sal = num(tm, "monthly_salary", f, minimum=0)
        cnt = num(tm, "count", f, default=1, minimum=0)
        c0 = parse_month(tm["start"], f + ".start") if tm.get("start") else start
        c1 = parse_month(tm["end"], f + ".end") if tm.get("end") else None
        g = float(tm.get("raise_pct_yearly", 0)) / 100
        for k, mi in enumerate(months):
            if mi >= c0 and (c1 is None or mi <= c1):
                salaries[k] += cnt * sal * (1 + g) ** ((mi - c0) // 12)
                heads[k] += cnt
    oncost = float(spec.get("employer_oncost_pct", 0)) / 100
    payroll = [x * (1 + oncost) for x in salaries]

    capex_cash, dep = Z(), Z()
    for ci, cx in enumerate(spec.get("capex") or []):
        f = f"capex[{ci}]"
        amt = num(cx, "amount", f, minimum=0)
        m0 = parse_month(cx.get("month") or month_str(start), f + ".month")
        life = int(num(cx, "life_months", f, default=60, minimum=1))
        for k, mi in enumerate(months):
            if mi == m0:
                capex_cash[k] += amt
            if m0 <= mi < m0 + life:
                dep[k] += amt / life

    equity, grants, loan_in, interest, principal = Z(), Z(), Z(), Z(), Z()
    for fi, fn in enumerate(spec.get("financing") or []):
        f = f"financing[{fi}]"
        typ = fn.get("type")
        amt = num(fn, "amount", f, minimum=0)
        m0 = parse_month(fn.get("month") or month_str(start), f + ".month")
        if typ in ("equity", "grant"):
            for k, mi in enumerate(months):
                if mi == m0:
                    (equity if typ == "equity" else grants)[k] += amt
        elif typ == "loan":
            rate = num(fn, "rate_pct", f, minimum=0) / 100 / 12
            term = int(num(fn, "term_months", f, minimum=1))
            grace = int(fn.get("grace_months", 0))
            if grace >= term:
                raise ModelError(f"{f}: grace_months must be shorter than term_months")
            nrep = term - grace
            pay = amt / nrep if rate == 0 else amt * rate / (1 - (1 + rate) ** (-nrep))
            bal = amt
            for k, mi in enumerate(months):
                j = mi - m0  # 0 = month received
                if j == 0:
                    loan_in[k] += amt
                if 1 <= j <= term:
                    it = bal * rate
                    pr = 0.0 if j <= grace else min(pay - it, bal)
                    bal -= pr
                    interest[k] += it
                    principal[k] += pr
        else:
            raise ModelError(f"{f}.type must be equity, grant or loan")

    gross = [rev[k] - cogs[k] for k in range(n)]
    ebitda = [gross[k] - var[k] - fixed[k] - payroll[k] for k in range(n)]
    ebit = [ebitda[k] - dep[k] for k in range(n)]
    pbt = [ebit[k] - interest[k] for k in range(n)]
    tax = Z()
    tx = spec.get("tax") or {"basis": "none"}
    basis = tx.get("basis", "none")
    trate = float(tx.get("rate_pct", 0)) / 100
    if basis == "turnover":
        tax = [rev[k] * trate for k in range(n)]
    elif basis == "profit":
        for b in range(0, n, 12):
            blk = range(b, min(b + 12, n))
            t_amt = max(0.0, sum(pbt[k] for k in blk)) * trate
            tax[max(blk)] += t_amt
    elif basis != "none":
        raise ModelError("tax.basis must be profit, turnover or none")
    net = [pbt[k] - tax[k] for k in range(n)]

    opening = float(spec.get("opening_cash", 0))
    cash_open, cash_close, flow = Z(), Z(), Z()
    bal = opening
    for k in range(n):
        cash_open[k] = bal
        flow[k] = (cash_in_sales[k] - cash_out_cogs[k] - var[k] - fixed[k] - payroll[k] - capex_cash[k]
                   + loan_in[k] + equity[k] + grants[k] - interest[k] - principal[k] - tax[k])
        bal += flow[k]
        cash_close[k] = bal

    buf = spec.get("min_cash_buffer")
    if buf is None:
        first = range(min(6, n))
        buf = 3 * sum(payroll[k] + fixed[k] for k in first) / len(first)
    buf = float(buf)
    low = min(cash_close)
    low_k = cash_close.index(low)
    be = None
    for k in range(n):
        if all(e >= 0 for e in ebitda[k:]):
            be = k
            break
    blocks = []
    for b in range(0, n, 12):
        blk = list(range(b, min(b + 12, n)))
        R = sum(rev[k] for k in blk)
        G = sum(gross[k] for k in blk)
        blocks.append({"block": f"Year {b // 12 + 1}", "months": f"{month_str(months[blk[0]])} to {month_str(months[blk[-1]])}",
                       "revenue": R, "gross_profit": G, "gross_margin_pct": (G / R * 100) if R else 0.0,
                       "ebitda": sum(ebitda[k] for k in blk), "net_profit": sum(net[k] for k in blk),
                       "cash_end": cash_close[blk[-1]]})
    monthly = []
    for k in range(n):
        monthly.append({"month": month_str(months[k]), "revenue": rev[k], "cost_of_sales": cogs[k],
                        "gross_profit": gross[k], "variable_costs": var[k], "fixed_costs": fixed[k],
                        "payroll": payroll[k], "ebitda": ebitda[k], "depreciation": dep[k],
                        "interest": interest[k], "tax": tax[k], "net_profit": net[k],
                        "cash_in_sales": cash_in_sales[k], "cash_out_cost_of_sales": cash_out_cogs[k],
                        "capex": capex_cash[k], "loan_in": loan_in[k], "equity_in": equity[k],
                        "grants_in": grants[k], "loan_principal": principal[k], "net_cash_flow": flow[k],
                        "cash_end": cash_close[k], "headcount": heads[k]})
    warnings = []
    neg = [month_str(months[k]) for k in range(n) if cash_close[k] < 0]
    if neg:
        warnings.append(f"Cash is below zero in {len(neg)} month(s): {', '.join(neg[:6])}{'...' if len(neg) > 6 else ''}")
    elif low < buf:
        warnings.append(f"Cash falls below the safety buffer of {buf:,.0f} (low point {low:,.0f} in {month_str(months[low_k])})")
    for st in streams:
        for key in ("volume", "new", "gmv"):
            r = st.get(key)
            if isinstance(r, dict) and r.get("growth_pct", 0) > 15 and r.get("max") is None:
                warnings.append(f"{st.get('name')}: {r['growth_pct']}% monthly growth with no cap; add 'max' or justify it")
    if be is None:
        warnings.append("EBITDA does not stay at or above zero within the model period")
    for nm, ms in over_capacity.items():
        warnings.append(f"{nm}: planned volume is above the stated capacity in {len(ms)} month(s), first in {ms[0]}")
    return {
        "name": spec.get("name", ""), "currency": cur, "start": month_str(start), "months": n,
        "summary": {
            "cash_low_point": low, "cash_low_month": month_str(months[low_k]),
            "months_below_zero": len(neg), "min_cash_buffer": buf,
            "funding_need": max(0.0, buf - low), "ending_cash": cash_close[-1],
            "break_even_month": month_str(months[be]) if be is not None else None,
            "receivables_at_end": receivables_end, "payables_at_end": payables_end,
            "peak_headcount": max(heads) if heads else 0,
        },
        "years": blocks, "monthly": monthly, "streams": stream_rows, "warnings": warnings,
    }


def run_all(spec):
    base = run_model(spec)
    fin = spec.get("financing") or []
    base["summary"]["financing_in_model"] = sum(float(f.get("amount", 0)) for f in fin)
    if fin:
        nofin = dict(spec)
        nofin["financing"] = []
        nf = run_model(nofin)["summary"]
        base["summary"]["funding_need_without_financing"] = nf["funding_need"]
    else:
        base["summary"]["funding_need_without_financing"] = base["summary"]["funding_need"]
    scen = {}
    for nm, mods in (spec.get("scenarios") or {}).items():
        r = run_model(apply_mods(spec, mods))
        scen[nm] = {"mods": mods, "summary": r["summary"], "years": r["years"]}
    sens = []
    for drv in spec.get("sensitivity") or []:
        key = SENS_DRIVERS.get(drv)
        if not key:
            raise ModelError(f"sensitivity driver '{drv}' must be one of {sorted(SENS_DRIVERS)}")
        for step in SENS_STEPS:
            r = run_model(apply_mods(spec, {key: step}))
            sens.append({"driver": drv, "change_pct": step, "year1_net_profit": r["years"][0]["net_profit"],
                         "cash_low_point": r["summary"]["cash_low_point"]})
    base["scenarios"] = scen
    base["sensitivity"] = sens
    return base


# ---------------------------------------------------------------- output
def f0(x):
    return f"{x:,.0f}"


def to_markdown(res):
    c, s = res["currency"], res["summary"]
    L = [f"# Financial model: {res['name'] or 'plan'} ({c})", ""]
    L.append(f"- Cash low point: {f0(s['cash_low_point'])} {c} in {s['cash_low_month']}"
             f" ({s['months_below_zero']} month(s) below zero)")
    L.append(f"- Break-even (EBITDA stays at or above zero from): {s['break_even_month'] or 'not reached in this period'}")
    L.append(f"- Funding need to keep a buffer of {f0(s['min_cash_buffer'])} {c}: {f0(s['funding_need'])} {c}"
             + (f" after the {f0(s['financing_in_model'])} {c} of financing in the model"
                f" (without it: {f0(s['funding_need_without_financing'])} {c})" if s.get('financing_in_model') else ""))
    L.append(f"- Ending cash: {f0(s['ending_cash'])} {c}; peak headcount {s['peak_headcount']:g}")
    if s["receivables_at_end"] or s["payables_at_end"]:
        L.append(f"- Left at the end: receivables {f0(s['receivables_at_end'])}, payables {f0(s['payables_at_end'])}")
    L += ["", f"| Period | Revenue ({c}) | Gross margin | EBITDA ({c}) | Net profit ({c}) | Cash at end ({c}) |",
          "|---|---|---|---|---|---|"]
    for b in res["years"]:
        L.append(f"| {b['block']} ({b['months']}) | {f0(b['revenue'])} | {b['gross_margin_pct']:.1f}% | "
                 f"{f0(b['ebitda'])} | {f0(b['net_profit'])} | {f0(b['cash_end'])} |")
    L += ["", f"| Month | Revenue | Gross profit | Payroll | Fixed | EBITDA | Net profit | Cash end |",
          "|---|---|---|---|---|---|---|---|"]
    for m in res["monthly"]:
        L.append(f"| {m['month']} | {f0(m['revenue'])} | {f0(m['gross_profit'])} | {f0(m['payroll'])} | "
                 f"{f0(m['fixed_costs'] + m['variable_costs'])} | {f0(m['ebitda'])} | {f0(m['net_profit'])} | {f0(m['cash_end'])} |")
    if res.get("scenarios"):
        L += ["", f"| Scenario | Year 1 revenue | Year 1 net profit | Cash low point | Funding need |", "|---|---|---|---|---|"]
        L.append(f"| base | {f0(res['years'][0]['revenue'])} | {f0(res['years'][0]['net_profit'])} | "
                 f"{f0(s['cash_low_point'])} ({s['cash_low_month']}) | {f0(s['funding_need'])} |")
        for nm, sc in res["scenarios"].items():
            ss = sc["summary"]
            L.append(f"| {nm} | {f0(sc['years'][0]['revenue'])} | {f0(sc['years'][0]['net_profit'])} | "
                     f"{f0(ss['cash_low_point'])} ({ss['cash_low_month']}) | {f0(ss['funding_need'])} |")
    if res.get("sensitivity"):
        L += ["", "| Driver change | Year 1 net profit | Cash low point |", "|---|---|---|"]
        for r in res["sensitivity"]:
            L.append(f"| {r['driver']} {r['change_pct']:+d}% | {f0(r['year1_net_profit'])} | {f0(r['cash_low_point'])} |")
    if res["warnings"]:
        L += ["", "Warnings:"] + [f"- {w}" for w in res["warnings"]]
    L += ["", "Planning estimates only: label them in the plan and keep this input file as the assumptions record."]
    return "\n".join(L)


def to_csv(res):
    buf = io.StringIO()
    rows = res["monthly"]
    w = csv.DictWriter(buf, fieldnames=list(rows[0].keys()))
    w.writeheader()
    for r in rows:
        w.writerow({k: (round(v, 2) if isinstance(v, float) else v) for k, v in r.items()})
    return buf.getvalue()


def state_export(res):
    s, y = res["summary"], res["years"]
    out = {
        "forecast.revenue_y1": round(y[0]["revenue"]),
        "cash.low_point": round(s["cash_low_point"]), "cash.low_point_month": s["cash_low_month"],
        "cash.buffer": round(s["min_cash_buffer"]), "funding.need": round(s["funding_need"]),
        "funding.need_without_financing": round(s.get("funding_need_without_financing", s["funding_need"])),
        "funding.in_model": round(s.get("financing_in_model", 0)),
        "model.break_even_month": s["break_even_month"], "model.gross_margin_pct_y1": round(y[0]["gross_margin_pct"], 1),
        "model.headcount_peak": s["peak_headcount"], "model.months_below_zero": s["months_below_zero"],
        "payroll.monthly_avg_y1": round(sum(m["payroll"] for m in res["monthly"][:12]) / min(12, len(res["monthly"]))),
    }
    for i, b in enumerate(y[1:], start=2):
        out[f"forecast.revenue_y{i}"] = round(b["revenue"])
    for m in res["monthly"]:
        out[f"forecast.revenue.{m['month']}"] = round(m["revenue"])
    for st in res["streams"]:
        key = re.sub(r"[^a-z0-9]+", "_", st["name"].lower()).strip("_") or "stream"
        if st["price"] is not None:
            out[f"offer.{key}.price"] = st["price"]
        if st["unit_cost"] is not None:
            out[f"offer.{key}.unit_cost"] = st["unit_cost"]
        if st["type"] == "hours" and st["capacity_hours"]:
            out[f"capacity.{key}_hours"] = st["capacity_hours"]
            out[f"demand.{key}_hours"] = round(max(st["driver"]), 1)
        if st["type"] == "units" and st.get("capacity") is not None:
            out[f"capacity.{key}"] = st["capacity"]
            out[f"demand.{key}"] = round(max(st["driver"]), 1)
    return out


def write_xlsx(res, path):
    try:
        from openpyxl import Workbook
        from openpyxl.styles import Font
    except ImportError:
        print("Note: openpyxl is not installed, so no Excel file was written (pip install openpyxl).", file=sys.stderr)
        return False
    wb = Workbook()
    ws = wb.active
    ws.title = "Summary"
    s = res["summary"]
    ws.append([f"Financial model: {res['name']}", res["currency"]])
    ws["A1"].font = Font(bold=True)
    for k, v in s.items():
        ws.append([k.replace("_", " "), round(v) if isinstance(v, float) else v])
    ws.append([])
    ws.append(["Period", "Months", "Revenue", "Gross margin %", "EBITDA", "Net profit", "Cash at end"])
    for b in res["years"]:
        ws.append([b["block"], b["months"], round(b["revenue"]), round(b["gross_margin_pct"], 1),
                   round(b["ebitda"]), round(b["net_profit"]), round(b["cash_end"])])
    wm = wb.create_sheet("Monthly")
    keys = list(res["monthly"][0].keys())
    wm.append([k.replace("_", " ") for k in keys])
    for m in res["monthly"]:
        wm.append([round(m[k], 2) if isinstance(m[k], float) else m[k] for k in keys])
    for cell in wm[1]:
        cell.font = Font(bold=True)
    if res.get("scenarios"):
        wsn = wb.create_sheet("Scenarios")
        wsn.append(["Scenario", "Changes", "Year 1 revenue", "Year 1 net profit", "Cash low point", "Low month", "Funding need"])
        for nm, sc in res["scenarios"].items():
            ss = sc["summary"]
            wsn.append([nm, json.dumps(sc["mods"]), round(sc["years"][0]["revenue"]), round(sc["years"][0]["net_profit"]),
                        round(ss["cash_low_point"]), ss["cash_low_month"], round(ss["funding_need"])])
    if res.get("sensitivity"):
        wse = wb.create_sheet("Sensitivity")
        wse.append(["Driver", "Change %", "Year 1 net profit", "Cash low point"])
        for r in res["sensitivity"]:
            wse.append([r["driver"], r["change_pct"], round(r["year1_net_profit"]), round(r["cash_low_point"])])
    wn = wb.create_sheet("Notes")
    wn.append(["These are planning estimates calculated by fin_model.py. Edit the JSON input and run again to update."])
    for w in res["warnings"]:
        wn.append([w])
    wb.save(path)
    return True


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("input", nargs="?")
    p.add_argument("--format", choices=["md", "json", "csv"], default="md")
    p.add_argument("--out")
    p.add_argument("--xlsx")
    p.add_argument("--state-export")
    p.add_argument("--example", action="store_true")
    a = p.parse_args(argv)
    if a.example:
        print(json.dumps(EXAMPLE, indent=2, ensure_ascii=False))
        return
    if not a.input:
        p.print_help()
        sys.exit(2)
    try:
        with open(a.input, encoding="utf-8") as fh:
            spec = json.load(fh)
        res = run_all(spec)
    except FileNotFoundError:
        print(f"Input error: file not found: {a.input}", file=sys.stderr)
        sys.exit(2)
    except json.JSONDecodeError as e:
        print(f"Input error: {a.input} is not valid JSON ({e})", file=sys.stderr)
        sys.exit(2)
    except ModelError as e:
        print(f"Input error: {e}", file=sys.stderr)
        sys.exit(2)
    if a.format == "json":
        text = json.dumps(res, indent=2, ensure_ascii=False, default=lambda x: round(x, 2))
    elif a.format == "csv":
        text = to_csv(res)
    else:
        text = to_markdown(res)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"Wrote {a.out}")
    else:
        print(text)
    if a.xlsx and write_xlsx(res, a.xlsx):
        print(f"Wrote {a.xlsx}")
    if a.state_export:
        with open(a.state_export, "w", encoding="utf-8") as fh:
            json.dump(state_export(res), fh, indent=2, ensure_ascii=False)
        print(f"Wrote {a.state_export}")


if __name__ == "__main__":
    try:  # stay quiet when the output is piped into head or similar
        import signal
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except (ImportError, AttributeError, ValueError):
        pass
    main()
