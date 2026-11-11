#!/usr/bin/env python3
"""Known-answer tests for the Business Plan Studio scripts.

Run from the repository root:  python3 tests/test_scripts.py
Every expected value below was worked out independently of the code under test.
"""
import argparse
import copy
import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
SKILLS = os.path.join(HERE, "..", "plugins", "business-plan-studio", "skills")
CANDIDATES = [os.path.join(HERE, "..", "shared", "scripts")] + [
    os.path.join(SKILLS, s, "scripts") for s in ("business-plan-coach", "business-plan-financials",
                                                 "business-plan-market-research", "business-plan-review")]
DIRS = [os.path.abspath(p) for p in CANDIDATES if os.path.isdir(p)]
for d in reversed(DIRS):
    sys.path.insert(0, d)


def script_path(name):
    """Each skill ships only the scripts it uses, so look in every skill."""
    return next(os.path.join(d, name) for d in DIRS if os.path.exists(os.path.join(d, name)))


import bizcalc  # noqa: E402
import check_plan  # noqa: E402
import fin_model  # noqa: E402
import market_size  # noqa: E402
import plan_catalog as cat  # noqa: E402
import score_plan  # noqa: E402


def ns(**kw):
    base = dict(fixed=None, hours=None, task_hours=None, direct=None, price=None, margin_pct=None, unit_cost=None,
                variable_pct=None, cost=None, markup_pct=None, days=None, arpu=None, gross_margin_pct=None,
                churn_pct=None, cac=None, monthly_margin=None, amount=None, rate=None, months=None, grace=None,
                low_point=None, buffer=None, start=None, end=None, capacity=None, demand=None, part=None,
                whole=None, inclusive=False, cash_available=None, debt_service=None)
    base.update(kw)
    return argparse.Namespace(**base)


def wj(path, data):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh)


def rj(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def run(script, *args, cwd=None):
    return subprocess.run([sys.executable, script_path(script), *args], capture_output=True, text=True, cwd=cwd)


class Bizcalc(unittest.TestCase):
    def test_cost_per_hour_and_min_price(self):
        self.assertEqual(bizcalc.cost_per_hour(ns(fixed=48000, hours=400))["cost_per_hour"], 120.0)
        r = bizcalc.min_price(ns(fixed=48000, hours=400, task_hours=30, direct=1500, price=5000))
        self.assertEqual(r["minimum_price"], 5100)
        self.assertEqual(r["status"], "BELOW MINIMUM PRICE")
        r = bizcalc.min_price(ns(fixed=48000, hours=400, task_hours=30, direct=1500, margin_pct=25))
        self.assertEqual(r["price_for_margin"], 6800)  # 5100 / 0.75

    def test_unit_margin_and_markup(self):
        r = bizcalc.unit_margin(ns(price=120, unit_cost=70, variable_pct=3))
        self.assertEqual(r["contribution_per_unit"], 46.4)
        self.assertEqual(r["contribution_margin_pct"], 38.67)
        self.assertEqual(bizcalc.unit_margin(ns(price=10, unit_cost=12))["status"], "LOSS ON EVERY UNIT")
        r = bizcalc.markup_margin(ns(cost=100, markup_pct=50))
        self.assertEqual((r["price"], r["margin_pct"]), (150.0, 33.33))
        self.assertEqual(bizcalc.markup_margin(ns(cost=60, margin_pct=40))["price"], 100.0)

    def test_break_even(self):
        r = bizcalc.break_even(ns(fixed=60000, price=18, unit_cost=7, days=26))
        self.assertEqual(r["break_even_units_rounded_up"], 5455)
        self.assertEqual(r["break_even_units_per_day"], 209.79)
        self.assertEqual(bizcalc.break_even(ns(fixed=2700, price=0.8, unit_cost=0.35))["break_even_units_rounded_up"], 6000)
        with self.assertRaises(SystemExit):
            bizcalc.break_even(ns(fixed=100, price=5, unit_cost=6))

    def test_ltv_cac_loan_funding(self):
        r = bizcalc.ltv_cac(ns(arpu=49, gross_margin_pct=80, churn_pct=4, cac=245))
        self.assertEqual((r["ltv"], r["ltv_to_cac"], r["cac_payback_months"]), (980, 4.0, 6.25))
        r = bizcalc.loan(ns(amount=100000, rate=18, months=24, grace=3))
        self.assertEqual(r["grace_payment_interest_only"], 1500.0)
        self.assertEqual(r["instalment_after_grace"], 5586.55)
        self.assertEqual(r["schedule_extract"][-1]["balance"], 0.0)
        r = bizcalc.loan(ns(amount=12000, rate=0, months=12))
        self.assertEqual((r["instalment_after_grace"], r["total_interest"]), (1000.0, 0.0))
        self.assertEqual(bizcalc.funding_need(ns(low_point=-80000, buffer=60000))["funding_need"], 140000)
        self.assertEqual(bizcalc.funding_need(ns(low_point=90000, buffer=60000))["funding_need"], 0)

    def test_growth_capacity_vat_dscr(self):
        self.assertEqual(bizcalc.growth(ns(start=1, end=2, months=12))["monthly_growth_pct"], 5.95)
        self.assertEqual(bizcalc.growth(ns(start=100, rate=10, months=2))["end_value"], 121.0)
        self.assertEqual(bizcalc.capacity(ns(capacity=624, demand=470))["utilisation_pct"], 75.32)
        self.assertEqual(bizcalc.capacity(ns(capacity=480, demand=560))["status"], "OVER CAPACITY")
        self.assertEqual(bizcalc.vat(ns(amount=114, rate=14, inclusive=True))["net"], 100.0)
        self.assertEqual(bizcalc.vat(ns(amount=100, rate=15))["gross"], 115.0)
        self.assertEqual(bizcalc.dscr(ns(cash_available=9000, debt_service=6000))["dscr"], 1.5)

    def test_cli_and_errors(self):
        r = run("bizcalc.py", "pct", "--part", "20", "--whole", "80", "--json")
        self.assertEqual(json.loads(r.stdout)["pct"], 25.0)
        r = run("bizcalc.py", "cost-per-hour", "--fixed", "100", "--hours", "0")
        self.assertEqual(r.returncode, 2)
        self.assertIn("Input error", r.stderr)


BASE = {"currency": "EGP", "start": "2027-01", "months": 12, "opening_cash": 1000,
        "streams": [{"name": "Packs", "type": "units", "volume": 100, "price": 10, "unit_cost": 4}],
        "fixed_costs": [{"name": "Rent", "monthly": 200}]}


class FinModel(unittest.TestCase):
    def test_flat_units_model(self):
        r = fin_model.run_model(BASE)
        m = r["monthly"][0]
        self.assertEqual((m["revenue"], m["cost_of_sales"], m["ebitda"]), (1000, 400, 400))
        self.assertEqual(r["monthly"][-1]["cash_end"], 1000 + 12 * 400)
        self.assertEqual(r["years"][0]["gross_margin_pct"], 60.0)
        self.assertEqual(r["summary"]["break_even_month"], "2027-01")
        self.assertEqual(r["summary"]["cash_low_point"], 1400)

    def test_ramp_cap_seasonality_price_growth(self):
        s = copy.deepcopy(BASE)
        s["months"] = 24
        s["streams"][0].update({"volume": {"start": 100, "growth_pct": 10, "max": 121}, "price_growth_pct_yearly": 10,
                                "seasonality": [2] + [1] * 11})
        r = fin_model.run_model(s)
        rev = [round(m["revenue"], 2) for m in r["monthly"]]
        self.assertEqual(rev[0], 2000.0)      # 100 x 2 (January) x 10
        self.assertEqual(rev[1], 1100.0)      # 110 x 10
        self.assertEqual(rev[2], 1210.0)      # capped at 121
        self.assertEqual(rev[12], 2662.0)     # 121 x 2 x 11 (price +10% in year 2)

    def test_subscription_and_budget_cac(self):
        s = {"currency": "USD", "start": "2027-01", "months": 12,
             "streams": [{"name": "Plan", "type": "subscription", "customers_start": 100, "new": {"start": 20},
                          "churn_pct": 5, "price": 10}]}
        d = fin_model.run_model(s)["streams"][0]["driver"]
        self.assertAlmostEqual(d[0], 115.0)
        self.assertAlmostEqual(d[1], 129.25)
        s["streams"][0]["new"] = {"from_budget": 1000, "cac": 100}
        r = fin_model.run_model(s)
        self.assertAlmostEqual(r["streams"][0]["driver"][0], 105.0)   # 95 + 10 new
        self.assertEqual(r["monthly"][0]["fixed_costs"], 1000)        # the budget is a cost
        down = fin_model.run_model(fin_model.apply_mods(s, {"volume_pct": -50}))
        self.assertAlmostEqual(down["streams"][0]["driver"][0], 100.0)  # same budget buys 5, not 10
        self.assertEqual(down["monthly"][0]["fixed_costs"], 1000)

    def test_hours_gmv_rental_schedule(self):
        s = {"currency": "USD", "start": "2027-01", "months": 12, "streams": [
            {"name": "Consulting", "type": "hours", "capacity_hours": 160, "utilisation_pct": {"start": 50, "growth_pts": 10, "max": 90}, "rate": 40},
            {"name": "Market", "type": "gmv", "gmv": 10000, "take_rate_pct": 10, "cost_pct": 20},
            {"name": "Desks", "type": "rental", "units_available": 10, "occupancy_pct": {"start": 40, "growth_pts": 20, "max": 100}, "price": 100},
            {"name": "Grant work", "type": "schedule", "amounts": {"2027-03": 5000}}]}
        r = fin_model.run_model(s)
        by = {x["name"]: x for x in r["streams"]}
        self.assertEqual(by["Consulting"]["revenue"][0], 3200)     # 160 x 50% x 40
        self.assertEqual(by["Consulting"]["revenue"][5], 5760)     # capped at 90%
        self.assertEqual((by["Market"]["revenue"][0], by["Market"]["cogs"][0]), (1000, 200))
        self.assertEqual([by["Desks"]["revenue"][k] for k in (0, 3, 4)], [400, 1000, 1000])
        self.assertEqual((by["Grant work"]["revenue"][1], by["Grant work"]["revenue"][2]), (0, 5000))

    def test_cash_timing(self):
        s = copy.deepcopy(BASE)
        s["fixed_costs"] = []
        s["streams"][0]["collection_days"] = 30
        s["payment_days"] = 60
        r = fin_model.run_model(s)
        self.assertEqual(r["monthly"][0]["cash_in_sales"], 0)
        self.assertEqual(r["monthly"][1]["cash_in_sales"], 1000)
        self.assertEqual(r["monthly"][1]["cash_out_cost_of_sales"], 0)
        self.assertEqual(r["monthly"][2]["cash_out_cost_of_sales"], 400)
        self.assertEqual(r["summary"]["receivables_at_end"], 1000)
        self.assertEqual(r["summary"]["payables_at_end"], 800)
        s["payment_days"] = 0
        s["inventory_days"] = 30            # stock bought a month before it is sold
        r = fin_model.run_model(s)
        self.assertEqual(r["monthly"][0]["cash_out_cost_of_sales"], 800)   # months 1 and 2 both land in month 1
        self.assertEqual(r["summary"]["payables_at_end"], 0)

    def test_team_capex_loan_tax(self):
        s = copy.deepcopy(BASE)
        s["team"] = [{"role": "Baker", "count": 2, "monthly_salary": 100, "start": "2027-03"}]
        s["employer_oncost_pct"] = 20
        s["capex"] = [{"name": "Oven", "amount": 1200, "month": "2027-01", "life_months": 12}]
        s["financing"] = [{"type": "loan", "amount": 100000, "month": "2027-01", "rate_pct": 18, "term_months": 24, "grace_months": 3},
                          {"type": "equity", "amount": 500, "month": "2027-02"}, {"type": "grant", "amount": 300, "month": "2027-02"}]
        s["tax"] = {"basis": "turnover", "rate_pct": 1}
        r = fin_model.run_model(s)
        m = r["monthly"]
        self.assertEqual((m[1]["payroll"], m[2]["payroll"]), (0, 240))
        self.assertEqual((m[0]["capex"], m[0]["depreciation"]), (1200, 100))
        self.assertEqual((m[0]["loan_in"], m[0]["interest"]), (100000, 0))
        self.assertEqual(m[1]["interest"], 1500)
        self.assertEqual(m[3]["loan_principal"], 0)                       # third grace month
        self.assertAlmostEqual(m[4]["interest"] + m[4]["loan_principal"], 5586.55, places=2)
        self.assertEqual((m[1]["equity_in"], m[1]["grants_in"]), (500, 300))
        self.assertEqual(m[0]["tax"], 10)
        s["tax"] = {"basis": "profit", "rate_pct": 10}
        s["financing"] = []
        r = fin_model.run_model(s)
        pbt = sum(x["ebitda"] - x["depreciation"] - x["interest"] for x in r["monthly"])
        self.assertAlmostEqual(r["monthly"][11]["tax"], pbt * 0.1)
        self.assertEqual(sum(x["tax"] for x in r["monthly"][:11]), 0)

    def test_funding_need_scenarios_sensitivity_export(self):
        s = copy.deepcopy(BASE)
        s["opening_cash"] = 0
        s["min_cash_buffer"] = 1000
        s["fixed_costs"] = [{"name": "Rent", "monthly": 900}]
        s["streams"][0]["capacity"] = 90
        s["financing"] = [{"type": "equity", "amount": 5000, "month": "2027-01"}]
        s["scenarios"] = {"downside": {"volume_pct": -50, "cost_pct": 10}}
        s["sensitivity"] = ["price"]
        r = fin_model.run_all(s)
        # base: 600 gross - 900 rent = -300 a month; with 5000 equity the low point is 1400 in month 12
        self.assertEqual(r["summary"]["cash_low_point"], 1400)
        self.assertEqual(r["summary"]["funding_need"], 0)
        self.assertEqual(r["summary"]["funding_need_without_financing"], 4600)   # buffer 1000 - (-3600)
        self.assertEqual(r["summary"]["break_even_month"], None)
        self.assertTrue(any("capacity" in w for w in r["warnings"]))
        # downside: 50 x (10 - 4.4) = 280 gross; rent 990
        self.assertAlmostEqual(r["scenarios"]["downside"]["years"][0]["ebitda"], 12 * (280 - 990))
        self.assertEqual(len(r["sensitivity"]), 4)
        self.assertAlmostEqual(r["sensitivity"][0]["year1_net_profit"], 12 * (100 * (8 - 4) - 900))
        ex = fin_model.state_export(r)
        self.assertEqual(ex["forecast.revenue_y1"], 12000)
        self.assertEqual(ex["offer.packs.price"], 10)
        self.assertEqual((ex["capacity.packs"], ex["demand.packs"]), (90, 100))
        self.assertEqual(ex["funding.need_without_financing"], 4600)

    def test_example_and_bad_input(self):
        self.assertTrue(fin_model.run_all(fin_model.EXAMPLE)["monthly"])
        for bad in ({"currency": "EGP", "start": "2027-13", "streams": [{}]},
                    {"start": "2027-01", "streams": [{"type": "units"}]},
                    {"currency": "EGP", "start": "2027-01", "streams": []},
                    {"currency": "EGP", "start": "2027-01", "streams": [{"type": "magic"}]}):
            with self.assertRaises(fin_model.ModelError):
                fin_model.run_model(bad)
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "m.json")
            wj(p, fin_model.EXAMPLE)
            r = run("fin_model.py", p, "--state-export", os.path.join(d, "n.json"), "--out", os.path.join(d, "m.md"))
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertIn("forecast.revenue_y1", rj(os.path.join(d, "n.json")))


class StateAndChecks(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.f = os.path.join(self.dir.name, "plan_state.json")

    def tearDown(self):
        self.dir.cleanup()

    def ps(self, *args):
        return run("plan_state.py", "--file", self.f, *args)

    def checks(self):
        r = run("check_plan.py", "--file", self.f, "--json")
        return {(c["check"], c["status"]) for c in json.loads(r.stdout)}

    def test_lifecycle(self):
        self.assertEqual(self.ps("init", "--name", "Test Co", "--type", "services", "--audience", "bank",
                                 "--currency", "EGP", "--language", "es").returncode, 0)
        self.assertNotEqual(self.ps("init", "--name", "Again").returncode, 0)          # no silent overwrite
        self.assertEqual(self.ps("set", "customer.segments", "--text", "Cafes; offices", "--label", "estimate").returncode, 0)
        self.assertNotEqual(self.ps("set", "customer.nope", "--text", "x").returncode, 0)
        self.assertNotEqual(self.ps("label", "customer.segments", "Maybe").returncode, 0)
        self.ps("set", "customer.segments", "--text", "Cafes; offices; hotels", "--status", "done")
        self.ps("assume", "Cafes reorder weekly", "--validate", "8 weeks of orders")
        self.ps("question", "VAT threshold?", "--for", "accountant")
        self.ps("lesson", "Break-even point")
        self.ps("resolve", "Q1", "--answer", "Not yet required")
        st = rj(self.f)
        sec = st["sections"]["customer.segments"]
        self.assertEqual((sec["label"], sec["status"], len(sec["history"])), ("Estimate", "done", 1))
        self.assertEqual(st["questions"][0]["status"], "closed")
        self.assertEqual(st["lists"]["lessons_taught"], ["Break-even point"])
        self.assertEqual(st["settings"]["language"], "es")
        self.assertIn("Bank or lender", self.ps("map").stdout)
        self.assertIn("State file is valid", self.ps("validate").stdout)
        for flag in ("--plan", "--one-pager", "--deck-outline", "--registers"):
            self.assertEqual(run("render_plan.py", "--file", self.f, flag).returncode, 0)
        self.assertIn("Cafes; offices; hotels", run("render_plan.py", "--file", self.f, "--plan").stdout)

    def test_import_sections(self):
        self.ps("init", "--name", "T")
        good = os.path.join(self.dir.name, "draft.json")
        wj(good, {"customer.problem": {"text": "Cafes run out of bread", "label": "Estimate"},
                  "offer.description": "Fresh loaves delivered daily", "market.size": {"text": ""}})
        self.assertEqual(self.ps("import-sections", good).returncode, 0)
        st = rj(self.f)
        self.assertEqual(st["sections"]["customer.problem"]["status"], "draft")
        self.assertEqual(st["sections"]["customer.problem"]["label"], "Estimate")
        self.assertEqual(st["sections"]["offer.description"]["text"], "Fresh loaves delivered daily")
        self.assertNotIn("market.size", st["sections"])            # empty text is skipped
        bad = os.path.join(self.dir.name, "bad.json")
        wj(bad, {"customer.problem": "new text", "customer.nope": "x"})
        self.assertNotEqual(self.ps("import-sections", bad).returncode, 0)
        self.assertEqual(rj(self.f)["sections"]["customer.problem"]["text"], "Cafes run out of bread")  # nothing saved

    def test_every_section_and_audience_is_consistent(self):
        ids = set(cat.section_index())
        self.assertEqual(len(ids), 63)
        for order in cat.AUDIENCES.values():
            self.assertEqual(sorted(order), sorted(cat.module_ids()))
        self.assertEqual(set(cat.AUDIENCES), set(cat.AUDIENCE_NAMES), set(cat.AUDIENCE_NAMES_AR))
        self.assertEqual(sum(m[3] for m in cat.MODULES), 180)   # minutes: "about 3 hours"

    def test_checks(self):
        self.ps("init", "--name", "T")
        nums = {"offer.a.price": 12000, "offer.a.min_price": 14000, "capacity.hours": 480, "demand.hours": 560,
                "market.som": 900000, "forecast.revenue_y1": 1152000, "cash.low_point": -192000, "cash.buffer": 0,
                "funding.ask": 100000, "funding.need": 192000, "use_of_funds.x": 60000, "use_of_funds.y": 30000,
                "unit.ltv": 500, "unit.cac": 600, "assumption.growth_pct_monthly": 20,
                "model.gross_margin_pct_y1": -5, "team.headcount": 4, "model.headcount_peak": 3,
                "target.2027-06": 100, "forecast.revenue.2027-06": 50}
        for k, v in nums.items():
            self.ps("num", k, str(v), "--label", "Estimate")
        self.ps("action", "Call the bank")
        got = self.checks()
        for c in ("C01", "C02", "C03", "C06", "C07", "C08", "C09", "C11"):
            self.assertIn((c, "blocking"), got, c)
        for c in ("C04", "C05", "C10", "C13"):
            self.assertIn((c, "advisory"), got, c)
        self.assertIn(("C12", "pass"), got)
        fixes = {"offer.a.price": 16000, "demand.hours": 400, "forecast.revenue_y1": 300000, "cash.low_point": 50000,
                 "funding.need": 90000, "funding.ask": 90000, "unit.ltv": 2400, "assumption.growth_pct_monthly": 5,
                 "model.gross_margin_pct_y1": 40, "model.headcount_peak": 4, "target.2027-06": 52}
        for k, v in fixes.items():
            self.ps("num", k, str(v), "--label", "Estimate")
        got = self.checks()
        for c in ("C01", "C02", "C03", "C04", "C05", "C06", "C07", "C08", "C09", "C10", "C11"):
            self.assertIn((c, "pass"), got, c)

    def test_paste_pack(self):
        self.ps("init", "--name", "T")
        self.ps("set", "financials.forecast", "--text", "Year 1 revenue 1,826,143 EGP")
        form = os.path.join(self.dir.name, "form.json")
        wj(form, {"form": "Demo", "number_format": "digits only", "fields": [
            {"id": "a", "label": "Revenue", "limit_chars": 10, "maps_to": ["financials.forecast"]},
            {"id": "b", "label": "Total", "calculated_by_portal": True, "maps_to": []}]})
        out = run("render_plan.py", "--file", self.f, "--paste-pack", form).stdout
        self.assertIn("1826143", out)
        self.assertIn("OVER LIMIT", out)
        self.assertNotIn("## Total", out)


class MarketAndScore(unittest.TestCase):
    def test_market_size(self):
        sp = {"currency": "MAD", "year": 2027,
              "top_down": {"start": {"label": "Households", "value": 600000, "source": "census"},
                           "tam_filters": [{"label": "pay for laundry", "pct": 20, "source": "survey"}],
                           "sam_filters": [{"label": "in zone", "pct": 25}],
                           "annual_value_per_customer": {"value": 1800, "source": "survey"}},
              "bottom_up": {"reachable_customers": {"value": 6000, "source": "vans"},
                            "conversion_pct": {"value": 5, "source": "pilot"},
                            "annual_value_per_customer": {"value": 1800, "source": "survey"}},
              "year1_forecast_revenue": 410000}
        o = market_size.run(sp)
        self.assertEqual((o["tam"], o["sam"], o["som"]), (216000000, 54000000, 540000))
        self.assertEqual(o["c03"][0], "advisory")
        self.assertEqual(o["missing_sources"], ["in zone"])
        sp["bottom_up"]["capacity_cap"] = {"value": 300000, "source": "capacity"}
        self.assertEqual(market_size.run(sp)["c03"][0], "blocking")

    def test_score_and_verdicts(self):
        for row in score_plan.WEIGHTS.values():
            self.assertEqual(sum(row), 100)
        full = {d: 5 for d in score_plan.DIMENSIONS[:-1]}
        self.assertEqual(score_plan.run({"audience": "bank", "ratings": full})["verdict"], "Ready")
        r = score_plan.run({"audience": "bank", "ratings": full, "findings": [{"severity": "blocking"}]})
        self.assertEqual((r["score"], r["verdict"]), (100, "Needs work"))
        r = score_plan.run({"audience": "bank", "ratings": full, "findings": [{"severity": "blocking", "quick_fix": True}]})
        self.assertEqual(r["verdict"], "Nearly ready")
        bank = dict(zip(score_plan.DIMENSIONS, [3, 3, 2, 3, 4, 3, 4, 3, 2, 2]))
        self.assertEqual(score_plan.run({"audience": "bank", "ratings": bank})["score"], 57)
        self.assertEqual(score_plan.run({"audience": "investor", "ratings": {"market": 1}})["verdict"], "Not ready")
        with self.assertRaises(ValueError):
            score_plan.run({"audience": "bank", "ratings": {"market": 9}})


if __name__ == "__main__":
    unittest.main(verbosity=1)
