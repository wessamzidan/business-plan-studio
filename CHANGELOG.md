# Changelog

## 2.2.0 (November 2026)

Install anywhere: the same four skills now install in other agents that read the Agent Skills format.

- **Added:** `install.py`, which copies the skills into the skills folder of Claude Code, Codex, OpenCode, Antigravity or Hermes, or into any folder you name. It can preview (`--dry-run`) and remove (`--uninstall`), and it never overwrites a folder that belongs to something else.
- **Added:** `INSTALL.md`, with the steps for every agent, and instructions for AI agents, so a person can hand the files to their agent and let it install the skills.
- **Added:** a "How a session works" walk-through in the README, and three installer tests (24 tests in all).
- **Changed:** each skill's compatibility note now names other agents. The coaching content and the calculators are the same as in 2.1.0.
- **Note:** the skills were built and tested with Claude. For other agents, the folder locations follow each agent's documentation and the installer is tested, but the skills have not yet been run inside those agents.

## 2.1.0 (November 2026)

Second review pass: a line-by-line audit, a new automated test suite and more test conversations.

- **Fixed:** bank plans skipped the validation module and investor plans skipped the operations module in the plan map.
- **Fixed:** the capacity check (C02) never received the capacity and demand figures the financial model exports; stream names with dots or brackets broke the price check (C01).
- **Fixed:** in downside scenarios, a marketing budget now buys fewer customers instead of shrinking; rental seasonality is applied consistently; scripts no longer print an error when their output is piped.
- **Fixed:** the worked case's market size now agrees with its sales forecast; two business-type files used a section id that does not exist.
- **Added:** 24 more native Arabic example pairs, so every plan section has one; Arabic headings for the canvas, one-pager and deck outline.
- **Added:** an "ending a sitting" routine (recap, next step, hand over the plan file) and a record of lessons already taught, so they are not repeated in later sessions.
- **Added:** optional `capacity` on unit-sales streams in the financial model, with a warning when the plan exceeds it.
- **Added:** `tests/test_scripts.py` (21 known-answer tests) and 10 evaluation cases in the standard `evals/` layout.
- **Updated:** country starting points re-checked in November 2026 (UAE Small Business Relief now runs to tax periods ending by 31 December 2029; Egypt's 2027 social-insurance wage range added; Saudi figures added).
- **Changed:** each skill now ships only the scripts it uses.

## 2.0.0 (November 2026)

Rebuilt from version 1 (a single skill made for one incubator portal) after a full review.

- **Any business, any reader:** a universal 14-module plan structure with 63 sections; profiles for 10 business types; guidance for 6 readers (incubator, bank, investor, grant, internal, partner). Portal-specific rules moved into optional form maps.
- **Interactive coaching:** a fixed coaching-turn format, three coaching levels, options when the answer is a choice, a "stuck" ladder, natural-language commands in English and Arabic, guided, quick-draft, focus and review modes.
- **Teaching layer:** 62 micro-lessons with Arabic terms, a bilingual glossary, English and native Arabic example libraries, and a complete fictional worked case.
- **Four skills instead of one:** business-plan-coach, business-plan-financials, business-plan-market-research, business-plan-review.
- **Calculators:** new monthly financial model (7 revenue stream types, payroll on-costs, capital spending and depreciation, loans with grace periods, equity and grants, payment and stock timing, tax placeholder, scenarios, sensitivity, Excel export); 14 command calculators; market sizing with a source trail; a readiness scorer with reader-specific weights.
- **Plan memory:** state file version 2 with claim labels, numbers, lists, assumptions, open questions, actions, history and migration from version 1.
- **Checks:** 14 automatic consistency checks (C01–C14) instead of prose rules.
- **Best practices:** short third-person descriptions (under 200 characters), license and metadata fields, contents lists in long references, one consistent set of claim labels, no time-sensitive facts outside dated country profiles.
- **Privacy:** all examples are fictional companies.

## 1.0.0 (November 2026)

First version: one skill coaching a single company through one incubator's online portal.
