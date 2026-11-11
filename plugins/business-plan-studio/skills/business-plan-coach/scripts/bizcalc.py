#!/usr/bin/env python3
"""bizcalc.py - small business-plan calculators. Run instead of doing arithmetic by hand.

Usage: python3 bizcalc.py <command> [options] [--json]

Commands
  cost-per-hour  --fixed F --hours H                 fixed monthly cost / productive hours
  min-price      --fixed F --hours H --task-hours T [--direct D] [--price P] [--margin-pct M]
                 minimum price of a time-based job = task hours x cost per hour + direct cost
  unit-margin    --price P --unit-cost C [--variable-pct V]   contribution per unit and %
  markup-margin  --cost C (--price P | --markup-pct M | --margin-pct M)
  break-even     --fixed F --price P --unit-cost C [--variable-pct V] [--days D]
  ltv-cac        --arpu A --gross-margin-pct G --churn-pct CH --cac CAC   (monthly basis)
  payback        --cac CAC --monthly-margin M
  loan           --amount A --rate R --months N [--grace G]   (R = annual interest %)
  funding-need   --low-point L --buffer B
  growth         --start S (--end E --months N | --rate R --months N)   monthly compound growth
  capacity       --capacity C --demand D
  pct            --part P --whole W
  vat            --amount A --rate R [--inclusive]
  dscr           --cash-available C --debt-service D

All amounts are in the plan's currency. Percentages are written as numbers (18.75 means 18.75%).
Rounding: money to 2 decimals; cost per hour is rounded to 2 decimals before it is used,
as most forms and spreadsheets do. Exit code 2 means the inputs were invalid.
"""
import argparse
import json
import math
import sys


def fail(msg):
    print(f"Input error: {msg}", file=sys.stderr)
    sys.exit(2)


def need_pos(name, v, allow_zero=False):
    if v is None:
        fail(f"--{name} is required")
    if v < 0 or (v == 0 and not allow_zero):
        fail(f"--{name} must be {'zero or more' if allow_zero else 'more than zero'} (got {v})")
    return v


def money(x):
    return round(x + 0.0, 2)


def cost_per_hour(a):
    need_pos("fixed", a.fixed, True)
    need_pos("hours", a.hours)
    return {"cost_per_hour": money(a.fixed / a.hours),
            "explain": f"{a.fixed:g} / {a.hours:g} hours = {money(a.fixed / a.hours)} per hour"}


def min_price(a):
    need_pos("fixed", a.fixed, True)
    need_pos("hours", a.hours)
    need_pos("task-hours", a.task_hours)
    direct = a.direct or 0.0
    need_pos("direct", direct, True)
    cph = money(a.fixed / a.hours)
    mp = a.task_hours * cph + direct
    out = {"cost_per_hour": cph, "minimum_price": round(mp),
           "explain": f"{a.task_hours:g} h x {cph} + {direct:g} direct = {money(mp)} (rounded {round(mp)})"}
    if a.margin_pct is not None:
        if not 0 <= a.margin_pct < 100:
            fail("--margin-pct must be between 0 and 99.99")
        out["price_for_margin"] = round(mp / (1 - a.margin_pct / 100))
        out["margin_pct_target"] = a.margin_pct
    if a.price is not None:
        out["price"] = a.price
        out["above_minimum"] = round(a.price - mp)
        out["status"] = "OK" if a.price >= mp else "BELOW MINIMUM PRICE"
    return out


def unit_margin(a):
    need_pos("price", a.price)
    need_pos("unit-cost", a.unit_cost, True)
    var = (a.variable_pct or 0) / 100 * a.price
    contrib = a.price - a.unit_cost - var
    return {"contribution_per_unit": money(contrib),
            "contribution_margin_pct": money(contrib / a.price * 100),
            "gross_margin_pct": money((a.price - a.unit_cost) / a.price * 100),
            "status": "OK" if contrib > 0 else "LOSS ON EVERY UNIT",
            "explain": f"{a.price:g} - {a.unit_cost:g} - {money(var)} variable = {money(contrib)}"}


def markup_margin(a):
    need_pos("cost", a.cost)
    if a.price is not None:
        p = need_pos("price", a.price)
    elif a.markup_pct is not None:
        p = a.cost * (1 + a.markup_pct / 100)
    elif a.margin_pct is not None:
        if not 0 <= a.margin_pct < 100:
            fail("--margin-pct must be between 0 and 99.99")
        p = a.cost / (1 - a.margin_pct / 100)
    else:
        fail("give --price, --markup-pct or --margin-pct")
    return {"cost": a.cost, "price": money(p),
            "markup_pct": money((p - a.cost) / a.cost * 100),
            "margin_pct": money((p - a.cost) / p * 100),
            "note": "Markup is profit / cost; margin is profit / price. A 50% markup is a 33.33% margin."}


def break_even(a):
    need_pos("fixed", a.fixed, True)
    need_pos("price", a.price)
    need_pos("unit-cost", a.unit_cost, True)
    contrib = a.price - a.unit_cost - (a.variable_pct or 0) / 100 * a.price
    if contrib <= 0:
        fail("price must be higher than unit cost plus variable costs, otherwise there is no break-even")
    units = a.fixed / contrib
    out = {"contribution_per_unit": money(contrib),
           "break_even_units_per_month": money(units),
           "break_even_units_rounded_up": math.ceil(units - 1e-9),
           "break_even_revenue_per_month": round(units * a.price)}
    if a.days:
        out["break_even_units_per_day"] = money(units / a.days)
    return out


def ltv_cac(a):
    need_pos("arpu", a.arpu)
    need_pos("cac", a.cac)
    if not 0 < a.churn_pct <= 100:
        fail("--churn-pct must be above 0 and at most 100 (monthly churn)")
    if not 0 < a.gross_margin_pct <= 100:
        fail("--gross-margin-pct must be above 0 and at most 100")
    margin = a.arpu * a.gross_margin_pct / 100
    life = 100 / a.churn_pct
    ltv = margin * life
    return {"monthly_margin_per_customer": money(margin), "average_lifetime_months": money(life),
            "ltv": round(ltv), "ltv_to_cac": money(ltv / a.cac),
            "cac_payback_months": money(a.cac / margin),
            "rule_of_thumb": "Many investors look for LTV/CAC of 3 or more and payback within 12 months; "
                             "treat these as conventions to discuss, not laws."}


def payback(a):
    need_pos("cac", a.cac)
    need_pos("monthly-margin", a.monthly_margin)
    return {"payback_months": money(a.cac / a.monthly_margin)}


def loan(a):
    need_pos("amount", a.amount)
    need_pos("rate", a.rate, True)
    need_pos("months", a.months)
    g = int(a.grace or 0)
    n = int(a.months) - g
    if n <= 0:
        fail("--months must be longer than --grace")
    r = a.rate / 100 / 12
    pay = a.amount / n if r == 0 else a.amount * r / (1 - (1 + r) ** (-n))
    bal, rows, total_int = a.amount, [], 0.0
    for m in range(1, int(a.months) + 1):
        interest = bal * r
        principal = 0.0 if m <= g else pay - interest
        bal -= principal
        total_int += interest
        if m <= 3 or m == g + 1 or m > int(a.months) - 2:
            rows.append({"month": m, "payment": money(interest + principal), "interest": money(interest),
                         "principal": money(principal), "balance": money(max(bal, 0))})
    return {"grace_payment_interest_only": money(a.amount * r) if g else None,
            "instalment_after_grace": money(pay), "total_interest": money(total_int),
            "total_repaid": money(a.amount + total_int), "schedule_extract": rows}


def funding_need(a):
    need_pos("buffer", a.buffer, True)
    need = max(0.0, a.buffer - a.low_point)
    return {"funding_need": round(need),
            "explain": f"buffer {a.buffer:g} - lowest cash {a.low_point:g} = {round(need)} (never below 0)"}


def growth(a):
    need_pos("start", a.start)
    need_pos("months", a.months)
    if a.end is not None:
        need_pos("end", a.end)
        rate = ((a.end / a.start) ** (1 / a.months) - 1) * 100
        return {"monthly_growth_pct": money(rate), "yearly_equivalent_pct": money(((1 + rate / 100) ** 12 - 1) * 100)}
    if a.rate is None:
        fail("give --end or --rate")
    end = a.start * (1 + a.rate / 100) ** a.months
    return {"end_value": money(end), "multiple": money(end / a.start)}


def capacity(a):
    need_pos("capacity", a.capacity)
    need_pos("demand", a.demand, True)
    use = a.demand / a.capacity * 100
    return {"utilisation_pct": money(use), "spare": money(a.capacity - a.demand),
            "status": "OVER CAPACITY" if use > 100 else ("TIGHT (above 85%)" if use > 85 else "OK")}


def pct(a):
    need_pos("whole", a.whole)
    return {"pct": money(a.part / a.whole * 100)}


def vat(a):
    need_pos("amount", a.amount, True)
    need_pos("rate", a.rate, True)
    if a.inclusive:
        net = a.amount / (1 + a.rate / 100)
        return {"net": money(net), "tax": money(a.amount - net), "gross": money(a.amount)}
    return {"net": money(a.amount), "tax": money(a.amount * a.rate / 100), "gross": money(a.amount * (1 + a.rate / 100))}


def dscr(a):
    need_pos("debt-service", a.debt_service)
    ratio = a.cash_available / a.debt_service
    return {"dscr": money(ratio),
            "note": "Lenders often look for 1.2 to 1.5 or more; ask the lender for its own threshold."}


COMMANDS = {
    "cost-per-hour": (cost_per_hour, ["fixed", "hours"]),
    "min-price": (min_price, ["fixed", "hours", "task-hours", "direct", "price", "margin-pct"]),
    "unit-margin": (unit_margin, ["price", "unit-cost", "variable-pct"]),
    "markup-margin": (markup_margin, ["cost", "price", "markup-pct", "margin-pct"]),
    "break-even": (break_even, ["fixed", "price", "unit-cost", "variable-pct", "days"]),
    "ltv-cac": (ltv_cac, ["arpu", "gross-margin-pct", "churn-pct", "cac"]),
    "payback": (payback, ["cac", "monthly-margin"]),
    "loan": (loan, ["amount", "rate", "months", "grace"]),
    "funding-need": (funding_need, ["low-point", "buffer"]),
    "growth": (growth, ["start", "end", "months", "rate"]),
    "capacity": (capacity, ["capacity", "demand"]),
    "pct": (pct, ["part", "whole"]),
    "vat": (vat, ["amount", "rate"]),
    "dscr": (dscr, ["cash-available", "debt-service"]),
}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd")
    for name, (_fn, opts) in COMMANDS.items():
        sp = sub.add_parser(name)
        for o in opts:
            sp.add_argument(f"--{o}", type=float)
        if name == "vat":
            sp.add_argument("--inclusive", action="store_true")
        sp.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    if not a.cmd:
        p.print_help()
        sys.exit(2)
    out = COMMANDS[a.cmd][0](a)
    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=2))
    else:
        for k, v in out.items():
            if v is None:
                continue
            if isinstance(v, list):
                print(f"{k}:")
                for row in v:
                    print("  " + ", ".join(f"{rk}={rv}" for rk, rv in row.items()))
            else:
                print(f"{k}: {v}")


if __name__ == "__main__":
    try:  # stay quiet when the output is piped into head or similar
        import signal
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except (ImportError, AttributeError, ValueError):
        pass
    main()
