#!/usr/bin/env python3
"""score_plan.py - turn a reviewer's ratings into a weighted readiness score and verdict.

Usage: python3 score_plan.py ratings.json [--json]
       python3 score_plan.py --weights            print the weights table

Input:
{"audience": "bank",
 "ratings": {"problem_customer": {"score": 3, "evidence": "quote or page"}, ...},
 "findings": [{"severity": "blocking|major|minor", "area": "financials", "text": "...", "quick_fix": false}]}

Scores are 1-5 per dimension (see references/rubric.md). The weighted score is
sum(score / 5 x weight) over rated dimensions, rescaled to 100 when some are not rated.
Verdicts: Ready (80+ and no blocking finding) · Nearly ready (65-79 with no blocking finding,
or 80+ with exactly one blocking finding marked quick_fix) · Needs work (45-64, or any
other blocking finding) · Not ready (below 45).
"""
import argparse
import json
import sys

DIMENSIONS = ["problem_customer", "value_proposition", "market", "competition", "business_model",
              "go_to_market", "operations_team", "validation", "financials", "risks_execution", "impact"]

WEIGHTS = {  # each row sums to 100
    "incubator": [12, 10, 8, 8, 10, 10, 10, 14, 10, 8, 0],
    "bank":      [6, 6, 6, 6, 12, 8, 14, 8, 26, 8, 0],
    "investor":  [12, 10, 12, 8, 12, 10, 12, 10, 8, 6, 0],
    "grant":     [10, 8, 4, 4, 8, 6, 12, 8, 12, 8, 20],
    "internal":  [8, 8, 6, 8, 12, 14, 14, 8, 14, 8, 0],
    "partner":   [8, 12, 8, 8, 12, 14, 14, 8, 10, 6, 0],
}
for k, v in WEIGHTS.items():
    assert sum(v) == 100, k


def verdict(score, findings):
    blocking = [f for f in findings if f.get("severity") == "blocking"]
    quick = len(blocking) == 1 and blocking[0].get("quick_fix")
    if score >= 80 and not blocking:
        return "Ready"
    if (65 <= score < 80 and not blocking) or (score >= 80 and quick):
        return "Nearly ready"
    if score < 45:
        return "Not ready"
    return "Needs work"


def run(data):
    aud = data.get("audience", "incubator")
    if aud not in WEIGHTS:
        raise ValueError(f"audience must be one of {', '.join(WEIGHTS)}")
    w = dict(zip(DIMENSIONS, WEIGHTS[aud]))
    ratings = data.get("ratings", {})
    rows, got, possible = [], 0.0, 0.0
    for d in DIMENSIONS:
        if w[d] == 0 and d not in ratings:
            continue
        r = ratings.get(d)
        if r is None:
            rows.append({"dimension": d, "score": None, "weight": w[d], "evidence": "not rated"})
            continue
        s = r.get("score") if isinstance(r, dict) else r
        if not isinstance(s, (int, float)) or not 1 <= s <= 5:
            raise ValueError(f"{d}: score must be 1 to 5")
        got += s / 5 * w[d]
        possible += w[d]
        rows.append({"dimension": d, "score": s, "weight": w[d],
                     "evidence": (r.get("evidence") if isinstance(r, dict) else "") or ""})
    if possible == 0:
        raise ValueError("no dimension was rated")
    score = round(got / possible * 100)
    findings = data.get("findings", [])
    return {"audience": aud, "score": score, "verdict": verdict(score, findings), "rows": rows,
            "rated_weight": possible,
            "findings": {k: sum(1 for f in findings if f.get("severity") == k) for k in ("blocking", "major", "minor")}}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("input", nargs="?")
    p.add_argument("--json", action="store_true")
    p.add_argument("--weights", action="store_true")
    a = p.parse_args(argv)
    if a.weights:
        print("| Dimension | " + " | ".join(WEIGHTS) + " |\n|---|" + "---|" * len(WEIGHTS))
        for i, d in enumerate(DIMENSIONS):
            print(f"| {d} | " + " | ".join(str(WEIGHTS[k][i]) for k in WEIGHTS) + " |")
        return
    if not a.input:
        p.print_help()
        sys.exit(2)
    try:
        with open(a.input, encoding="utf-8") as fh:
            res = run(json.load(fh))
    except (OSError, ValueError, json.JSONDecodeError) as e:
        print(f"Input error: {e}", file=sys.stderr)
        sys.exit(2)
    if a.json:
        print(json.dumps(res, indent=2, ensure_ascii=False))
        return
    print(f"**Verdict: {res['verdict']}** · score {res['score']}/100 for a {res['audience']} reader"
          f" · findings: {res['findings']['blocking']} blocking, {res['findings']['major']} major, {res['findings']['minor']} minor")
    if res["rated_weight"] < 100:
        print(f"(Scored on {res['rated_weight']:g}% of the weight; unrated dimensions are left out.)")
    print("\n| Dimension | Score (1-5) | Weight | Evidence |\n|---|---|---|---|")
    for r in res["rows"]:
        print(f"| {r['dimension']} | {r['score'] if r['score'] is not None else '-'} | {r['weight']} | {r['evidence']} |")


if __name__ == "__main__":
    try:  # stay quiet when the output is piped into head or similar
        import signal
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except (ImportError, AttributeError, ValueError):
        pass
    main()
