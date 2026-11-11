# Business Plan Studio

[![Tests](https://github.com/wessamzidan/business-plan-studio/actions/workflows/tests.yml/badge.svg)](https://github.com/wessamzidan/business-plan-studio/actions/workflows/tests.yml) ![License: Apache 2.0](https://img.shields.io/badge/license-Apache%202.0-0B6B4F) ![Version 2.1.0](https://img.shields.io/badge/version-2.1.0-0B6B4F)

**An interactive business plan mentor for Claude: four Agent Skills that coach founders of any business, in English or Arabic, from first idea to a plan a bank, investor, incubator or grant programme will trust.**

Created by **AlRawaabit (Wessam Zidan)**. Licensed under Apache 2.0. Version 2.1.0.

## What it does

Business Plan Studio turns Claude into a patient, sharp business mentor. Instead of filling a template for you, it builds the plan *with* you:

- **One question at a time.** You answer first; Claude explains why each part matters, checks your answer, and offers a tighter version in your own words.
- **Teaches as you go.** 62 micro-lessons (break-even, unit economics, TAM/SAM/SOM, cash flow, CAC and LTV...) at your level: "new to this", "some experience" or "experienced, challenge me".
- **Examples when you need them.** Weak and strong answers for every section, from fictional businesses in many sectors and countries, plus native Arabic examples and a complete worked case.
- **Any business.** Tailored questions, drivers, red flags and model templates for 10 business types: services, software and subscriptions, e-commerce, retail shops, food service, manufacturing, trade and distribution, marketplaces, clinics/salons/gyms/training/tours, and social enterprises.
- **Any reader.** Module order, emphasis and length adapt to incubators, banks, investors, grant programmes, partners or an internal plan.
- **Numbers you can defend.** Tested calculators do all arithmetic: a monthly financial model with cash flow, break-even, scenarios, sensitivity and funding need (with optional Excel export), plus 14 consistency checks (price vs cost, capacity, market size vs forecast, cash floor, funding ask, use of funds...).
- **Honest by design.** Every claim is labelled Verified, Estimate, Planned or To confirm. Nothing is invented; market facts are researched with sources and dates, and tax or legal points become questions for your accountant or lawyer.
- **Remembers your progress.** A small `plan_state.json` file keeps your answers, numbers, assumptions and open questions, so you can stop and continue later, even in a new chat.
- **Ready-to-use outputs.** Full plan for your reader, one-page summary, Business Model Canvas or Lean Canvas, pitch deck outline, a paste pack for online application forms, and registers of assumptions, open questions and actions.

## The four skills

| Skill | Use it for |
|---|---|
| `business-plan-coach` | The guided journey: intake, plan map, coaching, teaching, examples, checks and outputs. Start here. |
| `business-plan-financials` | Building or fixing the numbers: pricing, unit economics, break-even, monthly cash flow, scenarios, funding need, loans and equity. |
| `business-plan-market-research` | Market sizing (TAM, SAM, SOM), competitors, customer interviews and local rules, with cited sources. |
| `business-plan-review` | A mentor, bank, investor or grant officer's review of an existing plan: scores, red flags, number checks and a ranked fix list. |

Each skill works on its own; together they share the same plan file.

## Install

Code execution must be enabled for the calculators. Each skill is a folder containing `SKILL.md`; the `claude-ai-uploads` folder has one ready-made ZIP per skill.

**Claude.ai (web, desktop, mobile)**
1. Turn on code execution and file creation in Settings.
2. Open Customize, then Skills (claude.ai/customize/skills), and choose to upload a skill.
3. Upload each ZIP from `claude-ai-uploads/` (start with `business-plan-coach.zip`) and switch the skills on.
Availability of custom skills depends on your plan; see Anthropic's help centre.

**Claude Cowork (desktop app)**
Open `business-plan-studio.plugin` in a Cowork chat and accept the plugin, or upload the skill ZIPs as above.

**Claude Code**
- As a plugin from GitHub: run `/plugin marketplace add wessamzidan/business-plan-studio`, then `/plugin install business-plan-studio@alrawaabit-business-plan-studio`.
- Or copy the four folders from `plugins/business-plan-studio/skills/` into `~/.claude/skills/` (personal) or `.claude/skills/` (one project).

**Claude API**
Upload each skill folder with the Skills API (`/v1/skills`) and attach the skill ids to your requests with the code execution tool. API containers have no internet access, so market research falls back to the founder's own sources.

## Try it

- "Help me write a business plan for my bakery in Alexandria. I'm new to this."
- "أريد أن أكتب خطة عمل لمشروع مطبخ سحابي في الرياض لتقديمها إلى بنك."
- "Quick draft of a plan for my cleaning company; I have 15 minutes."
- "Build a 24-month cash flow for my SaaS and tell me how much funding I need."
- "How big is the market for school uniforms in Nairobi? Show your sources."
- "Review my plan as a bank would." (attach the plan)

Useful things to say during a session: *map* · *next* · *skip* · *later* · *example* · *explain break-even* · *simpler* · *challenge me* · *draft it for me* · *check my numbers* · *what's missing* · *export*.

<!-- concept:start -->
## Design concept

The skills work in chat today. This repository also holds a design for a guided app on top of them: one path of 14 steps in 5 sittings, one question at a time, in English and Arabic, on a phone or a laptop. It is a design only; nothing in it is built yet. See [`design/`](design/) for the specification and every screen.

![The coaching step: why it matters, one question, an answer box and coach feedback](design/screenshots/step.png)
<!-- concept:end -->

## Privacy

Your plan stays in your conversation and in the `plan_state.json` file you download. The skills do not send data anywhere. They never ask for passwords, and they never press submit or send buttons on portals for you.

## Important

Business Plan Studio supports planning; it is not financial, tax, legal or investment advice. Tax and payroll rates are dated starting points to confirm with a qualified accountant. All example companies are fictional.

## Contributing

Issues and pull requests are welcome, especially new business types, country starting points, Arabic examples and calculator tests. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Credits and licence

Created by AlRawaabit (Wessam Zidan), https://alrawaabit.com. Licensed under the Apache License, Version 2.0 (see `LICENSE`). If you share or adapt it, keep the `LICENSE` and `NOTICE` files.
