#!/usr/bin/env python3
"""market_size.py - TAM, SAM and SOM with a traceable chain of sources.

Usage: python3 market_size.py sizing.json [--json]
       python3 market_size.py --example

Input (every figure carries its source; a missing source is reported as To confirm):
{
  "currency": "EGP", "year": 2026, "unit_name": "cafes",
  "top_down": {
    "start": {"label": "Cafes in Greater Cairo", "value": 12000, "source": "..."},
    "tam_filters": [{"label": "serve baked snacks", "pct": 70, "source": "..."}],
    "sam_filters": [{"label": "independent, within our delivery zone", "pct": 40, "source": "..."}],
    "annual_value_per_customer": {"value": 36000, "source": "..."},
    "som_share_pct": {"value": 3, "source": "founder estimate from sales capacity"}
  },
  "bottom_up": {
    "reachable_customers": {"value": 900, "source": "..."},
    "conversion_pct": {"value": 8, "source": "pilot: 4 of 50 cafes visited bought"},
    "annual_value_per_customer": {"value": 36000, "source": "..."},
    "capacity_cap": {"value": 2000000, "source": "max yearly output at current kitchen"}
  },
  "year1_forecast_revenue": 1500000
}
TAM = start x tam filters x annual value. SAM = TAM x sam filters.
SOM (top-down) = SAM x som share. SOM (bottom-up) = reachable x conversion x annual value,
capped by capacity. The script reports both, the gap between them, and check C03.
"""
import argparse
import json
import sys

EXAMPLE = json.loads(__doc__.split("Input (every figure carries its source; a missing source is reported as To confirm):\n")[1]
                     .split("\nTAM =")[0])


def fig(d, field):
    if not isinstance(d, dict) or "value" not in d:
        raise ValueError(f"{field} needs a 'value'")
    v = float(d["value"])
    if v < 0:
        raise ValueError(f"{field} cannot be negative")
    return v, d.get("source") or "", d.get("label") or field


def run(sp):
    cur = sp.get("currency", "")
    steps, missing = [], []

    def note(label, value, source, how):
        steps.append({"step": label, "value": value, "how": how, "source": source or "To confirm"})
        if not source:
            missing.append(label)

    out = {"currency": cur, "year": sp.get("year"), "steps": steps}
    td = sp.get("top_down")
    if td:
        v, src, lab = fig(td["start"], "top_down.start")
        note(lab, v, src, "starting count")
        n = v
        for f in td.get("tam_filters", []):
            pct = float(f["pct"])
            n *= pct / 100
            note(f.get("label", "TAM filter"), n, f.get("source"), f"x {pct:g}%")
        av, asrc, _ = fig(td["annual_value_per_customer"], "annual_value_per_customer")
        tam = n * av
        note("TAM", tam, asrc, f"{n:,.0f} x {av:,.0f} {cur} a year")
        m = n
        for f in td.get("sam_filters", []):
            pct = float(f["pct"])
            m *= pct / 100
            note(f.get("label", "SAM filter"), m, f.get("source"), f"x {pct:g}%")
        sam = m * av
        note("SAM", sam, asrc, f"{m:,.0f} x {av:,.0f}")
        out.update({"tam": tam, "sam": sam, "sam_customers": m})
        if td.get("som_share_pct"):
            sv, ssrc, _ = fig(td["som_share_pct"], "som_share_pct")
            out["som_top_down"] = sam * sv / 100
            note("SOM (top-down)", out["som_top_down"], ssrc, f"SAM x {sv:g}%")
    bu = sp.get("bottom_up")
    if bu:
        rv, rsrc, _ = fig(bu["reachable_customers"], "reachable_customers")
        cv, csrc, _ = fig(bu["conversion_pct"], "conversion_pct")
        av, asrc, _ = fig(bu["annual_value_per_customer"], "annual_value_per_customer")
        note("Reachable customers", rv, rsrc, "count")
        note("Conversion", rv * cv / 100, csrc, f"x {cv:g}%")
        raw = rv * cv / 100 * av
        note("SOM (bottom-up, before capacity)", raw, asrc, f"customers x {av:,.0f} {cur}")
        som_bu = raw
        if bu.get("capacity_cap"):
            cap, capsrc, _ = fig(bu["capacity_cap"], "capacity_cap")
            if raw > cap:
                som_bu = cap
                note("Capacity cap applied", cap, capsrc, "the business cannot deliver more than this")
        out["som_bottom_up"] = som_bu
    soms = [out[k] for k in ("som_top_down", "som_bottom_up") if k in out]
    if soms:
        out["som"] = min(soms)
        if len(soms) == 2 and min(soms) > 0:
            out["som_gap_ratio"] = max(soms) / min(soms)
    y1 = sp.get("year1_forecast_revenue")
    if y1 is not None and "som" in out:
        y1 = float(y1)
        if y1 > out["som"]:
            out["c03"] = ("blocking", f"year-1 forecast {y1:,.0f} is above the SOM {out['som']:,.0f}")
        elif y1 > out["som"] * 0.5:
            out["c03"] = ("advisory", f"year-1 forecast is {y1 / out['som']:.0%} of the SOM (above 50% is aggressive)")
        else:
            out["c03"] = ("pass", f"year-1 forecast is {y1 / out['som']:.0%} of the SOM")
    out["missing_sources"] = missing
    return out


def to_md(o):
    c = o["currency"]
    L = [f"# Market size ({c}, {o.get('year') or 'year not stated'})", ""]
    for k, name in (("tam", "TAM"), ("sam", "SAM"), ("som_top_down", "SOM, top-down"), ("som_bottom_up", "SOM, bottom-up")):
        if k in o:
            L.append(f"- {name}: {o[k]:,.0f} {c} a year")
    if "som" in o:
        L.append(f"- SOM used in the plan (the lower of the two): {o['som']:,.0f} {c} a year")
    if o.get("som_gap_ratio", 1) > 2:
        L.append(f"- The two SOM methods differ by {o['som_gap_ratio']:.1f} times: explain the gap or revisit the inputs")
    L += ["", "| Step | Value | How | Source |", "|---|---|---|---|"]
    for s in o["steps"]:
        L.append(f"| {s['step']} | {s['value']:,.0f} | {s['how']} | {s['source']} |")
    if "c03" in o:
        L.append(f"\nCheck C03: {o['c03'][0]}: {o['c03'][1]}")
    if o["missing_sources"]:
        L.append(f"\nNo source yet (label To confirm): {', '.join(o['missing_sources'])}")
    return "\n".join(L)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("input", nargs="?")
    p.add_argument("--json", action="store_true")
    p.add_argument("--example", action="store_true")
    a = p.parse_args(argv)
    if a.example:
        print(json.dumps(EXAMPLE, indent=2))
        return
    if not a.input:
        p.print_help()
        sys.exit(2)
    try:
        with open(a.input, encoding="utf-8") as fh:
            sp = json.load(fh)
        o = run(sp)
    except (OSError, ValueError, KeyError, TypeError) as e:
        print(f"Input error: {e}", file=sys.stderr)
        sys.exit(2)
    print(json.dumps(o, indent=2, default=lambda x: round(x, 2)) if a.json else to_md(o))


if __name__ == "__main__":
    try:  # stay quiet when the output is piped into head or similar
        import signal
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except (ImportError, AttributeError, ValueError):
        pass
    main()
