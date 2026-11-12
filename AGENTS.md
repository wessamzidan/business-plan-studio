# Instructions for AI agents

This file is for an AI agent that a person has pointed at this repository. People should read [README.md](README.md) and [INSTALL.md](INSTALL.md).

## What this repository is

Business Plan Studio is four Agent Skills (folders with a `SKILL.md`, reference files and Python scripts) that turn an agent into a business plan mentor. The agent coaches a founder through a plan one question at a time, teaches as it goes, does all arithmetic with tested scripts, and labels every claim Verified, Estimate, Planned or To confirm. It works in English and Arabic.

| Skill | Use it when the person wants |
| --- | --- |
| `business-plan-coach` | to write or continue a business plan. Start here. |
| `business-plan-financials` | pricing, break-even, a monthly cash flow, a funding need. |
| `business-plan-market-research` | market size, competitors, customer research, local rules, with sources. |
| `business-plan-review` | an existing plan scored the way a bank, investor, incubator or grant officer would. |

The skills are in `plugins/business-plan-studio/skills/`.

## If a person asked you to install it

1. **Get the files** if you do not have them: `git clone https://github.com/wessamzidan/business-plan-studio`. Work inside that folder.
2. **Find your name.** Run `python3 install.py --list`. It prints the agents it knows (`claude-code`, `codex`, `opencode`, `antigravity`, `hermes`, `agents`) and the folder each one reads.
3. **Say what you will do before you do it.** Run `python3 install.py --agent YOUR-NAME --dry-run` and tell the person which four folders will be copied and where. Wait for their yes.
4. **Install.** Run `python3 install.py --agent YOUR-NAME`. For one project only, add `--project PATH`. If you are not in the list, use `--dest PATH-TO-YOUR-SKILLS-FOLDER`.
5. **Report back.** Tell the person where the skills are, whether the calculator check printed OK, whether they need to restart you, and the first thing to type: "Help me write a business plan for my bakery. I'm new to this."

What the installer does: it copies four folders, uses only the Python standard library, makes no network calls, and changes nothing outside the target skills folder. It replaces an older copy of these four skills and refuses to overwrite a folder of the same name that belongs to something else. On Windows the command may be `python` or `py`.

Do only this. Do not install other packages, change the person's settings, or run anything else from the repository as part of installing. Excel export needs `openpyxl`; mention it and let the person decide.

If you are Claude.ai or Claude Cowork, you cannot use the installer. Tell the person to follow the Claude.ai or Cowork steps in [INSTALL.md](INSTALL.md).

## If a person asked you to use it without installing

Read `plugins/business-plan-studio/skills/business-plan-coach/SKILL.md` and follow it. Paths in that file are relative to its own folder. Keep the person's `plan_state.json` in their working folder, not inside this repository.

## What to tell the person about using it

1. Say what the business is and where, in a sentence or two. The coach asks who will read the plan and how much teaching they want.
2. Answer one question at a time. The coach checks each answer and offers a tighter version in the person's own words.
3. Useful words at any time: *map*, *next*, *skip*, *later*, *example*, *explain break-even*, *simpler*, *challenge me*, *check my numbers*, *what's missing*, *export*.
4. A full plan takes about three hours over several sittings; a quick draft takes about fifteen minutes.
5. At the end of a sitting the coach hands over `plan_state.json`. A new chat has no memory, so the person gives that file back next time to continue.

## If you are changing this repository

- Run `python3 tests/test_scripts.py` before and after. A change to a calculator needs a new known-answer test.
- Examples must be fictional. Never add real company figures or personal data.
- Do not edit `claude-ai-uploads/*.zip` or `business-plan-studio.plugin` by hand. The maintainer rebuilds them at each release.
- See [CONTRIBUTING.md](CONTRIBUTING.md).
