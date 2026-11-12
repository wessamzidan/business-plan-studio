# Install Business Plan Studio

Business Plan Studio is four skills in the open Agent Skills format: a folder with a `SKILL.md` file, some reference files and a few Python scripts. Every route below installs the same four skills.

| You use | Do this |
| --- | --- |
| Claude.ai (web, desktop, mobile) | Upload four ZIP files. [Steps](#claudeai) |
| Claude Cowork | Open one `.plugin` file. [Steps](#claude-cowork) |
| Claude Code | Add the plugin, or run `install.py`. [Steps](#claude-code) |
| Codex, OpenCode, Antigravity, Hermes | Run `install.py`. [Steps](#codex-opencode-antigravity-and-hermes) |
| Any other agent | Name its skills folder, or point it at `SKILL.md`. [Steps](#any-other-agent) |

## Before you start

- **Python 3** runs the calculators (tested with Python 3.11 to 3.13). Claude.ai and Cowork bring their own. On your own computer, check with `python3 --version`.
- **Web search** is optional. With it, the market research skill finds and cites sources. Without it, the skill guides your own research.
- **Excel export** is optional and needs `openpyxl` (`pip install openpyxl`).

## Get the files

Download the repository from GitHub (the green **Code** button, then **Download ZIP**) and unzip it, or run:

```
git clone https://github.com/wessamzidan/business-plan-studio
```

## The easiest way: ask your agent

If your agent can run commands on your computer (Claude Code, Codex, OpenCode, Antigravity, Hermes and similar), paste this:

> Install Business Plan Studio from https://github.com/wessamzidan/business-plan-studio. Read AGENTS.md in that repository and follow it. Tell me what you will copy and where before you do it.

If you already have the folder on your computer, open it in your agent and paste this instead:

> Install the skills in this folder for yourself. Read INSTALL.md, then run install.py with the right --agent name. Tell me what you will copy and where before you do it.

## Claude.ai

1. In Settings, turn on code execution and file creation.
2. Open Customize, then Skills.
3. If you already have a skill called `business-plan-coach`, delete it first. The new one has the same name.
4. Upload the four ZIP files from the `claude-ai-uploads` folder, starting with `business-plan-coach.zip`, and switch each one on.
5. Start a new chat and type: "Help me write a business plan for my bakery. I'm new to this."

Custom skills depend on your Claude plan. See Anthropic's help centre if the Skills page is missing.

## Claude Cowork

Drop `business-plan-studio.plugin` into a Cowork chat and accept the plugin. Then type the same first line as above.

## Claude Code

As a plugin, straight from GitHub:

```
/plugin marketplace add wessamzidan/business-plan-studio
/plugin install business-plan-studio@alrawaabit-business-plan-studio
```

Or from the folder on your computer:

```
python3 install.py --agent claude-code
```

## Codex, OpenCode, Antigravity and Hermes

Open a terminal in the Business Plan Studio folder and run one line. On Windows, type `python` or `py` instead of `python3`.

| Agent | Command | Copies the skills to |
| --- | --- | --- |
| OpenAI Codex | `python3 install.py --agent codex` | `~/.agents/skills` |
| OpenCode | `python3 install.py --agent opencode` | `~/.config/opencode/skills` |
| Google Antigravity | `python3 install.py --agent antigravity` | `~/.gemini/config/skills` |
| Hermes Agent | `python3 install.py --agent hermes` | `~/.hermes/skills` |

`~` means your home folder. The script copies four folders, uses no internet, and changes nothing else. To see what it would do first, add `--dry-run`. To see every agent it knows, run `python3 install.py --list`.

**For one project only.** Add `--project` and the project folder:

```
python3 install.py --agent codex --project /path/to/my-project
```

This copies the skills into the project's own skills folder (`.agents/skills` for Codex and Antigravity, `.opencode/skills` for OpenCode, `.hermes/skills` for Hermes, `.claude/skills` for Claude Code). Hermes loads project skills only after you run `hermes skills trust`.

**Then start.** Open your agent and type: "Help me write a business plan for my bakery. I'm new to this." If the agent does not pick the skill up, say: "Use the business-plan-coach skill." In Codex you can also type `$` and choose the skill, or run `/skills`.

Notes:

- Older Antigravity IDE versions read `~/.gemini/antigravity/skills`. If the skills do not load, run `python3 install.py --dest ~/.gemini/antigravity/skills`.
- `python3 install.py --agent agents` installs into the shared `~/.agents/skills` folder, which Codex and OpenCode both read.

## Any other agent

- **It has a skills folder.** Run `python3 install.py --dest PATH-TO-THAT-FOLDER`.
- **It has no skills feature but can read files and run Python.** Open the Business Plan Studio folder in it and say: "Read plugins/business-plan-studio/skills/business-plan-coach/SKILL.md and follow it."
- **Copy by hand.** Copy the four folders inside `plugins/business-plan-studio/skills/` into your agent's skills folder. Each must keep its name.

Tools that install skills from a GitHub link, such as `npx skills add wessamzidan/business-plan-studio` or `hermes skills install`, may also work. They have not been tested with this repository; `install.py` is the supported route.

## Check that it worked

Ask your agent: "Which Business Plan Studio skills do you have?" It should name four: `business-plan-coach`, `business-plan-financials`, `business-plan-market-research` and `business-plan-review`. Then ask: "Use bizcalc to work out the break-even for fixed costs of 30,000 a month, a price of 50 and a unit cost of 20." The answer is 1,000 units a month, and the agent should get it by running the script, not by mental arithmetic.

## Update or remove

- **Update:** get the new files, then run the same install command again. It replaces the four folders.
- **Remove:** `python3 install.py --agent NAME --uninstall`. It removes only folders that are Business Plan Studio skills.
- **Claude.ai:** delete or replace the skills under Customize, then Skills.

Your plan lives in `plan_state.json`, in your own working folder. Updating or removing the skills does not touch it.

## What has been tested

The skills were built and tested with Claude. For Codex, OpenCode, Antigravity and Hermes, the folder locations come from each agent's own documentation (checked in November 2026) and the installer is tested, but the skills have not yet been run inside those agents. Three things may differ there: the skills ask for an options card when one is available and fall back to a short numbered list; document export uses whatever document tools the agent has, or Markdown; and market research needs a web search tool. If something does not work in your agent, please report it.
