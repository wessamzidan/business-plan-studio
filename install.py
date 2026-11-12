#!/usr/bin/env python3
"""Install the Business Plan Studio skills into an AI agent's skills folder.

    python3 install.py --list                      show the agents and folders this script knows
    python3 install.py --agent codex               install for one agent, for your user account
    python3 install.py --agent opencode --project PATH    install inside one project only
    python3 install.py --dest PATH                 install into any skills folder you name
    python3 install.py --agent codex --dry-run     show what would happen, change nothing
    python3 install.py --agent codex --uninstall   remove the four skills again

What it does: copies four folders (one per skill) into the skills folder of the agent you name.
It uses only the Python standard library, makes no network calls, and changes nothing outside
that skills folder. Claude.ai and Claude Cowork do not use this script: see INSTALL.md.
"""
import argparse
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "plugins", "business-plan-studio", "skills")
SKILLS = ["business-plan-coach", "business-plan-financials", "business-plan-market-research",
          "business-plan-review"]
MARKER = "suite: Business Plan Studio"  # in every SKILL.md of this package
START_LINE = "Help me write a business plan for my bakery. I'm new to this."

# Folder locations come from each agent's own documentation (checked November 2026).
AGENTS = {
    "claude-code": {
        "label": "Claude Code",
        "user": "~/.claude/skills", "project": ".claude/skills", "home": "~/.claude",
        "notes": ["Restart Claude Code if the skills do not appear.",
                  "To call a skill by name, type /business-plan-coach."],
    },
    "codex": {
        "label": "OpenAI Codex",
        "user": "~/.agents/skills", "project": ".agents/skills", "home": "~/.codex",
        "notes": ["Codex detects new skills by itself. Restart it if they do not appear.",
                  "To call a skill by name, type $ and pick business-plan-coach, or run /skills."],
    },
    "opencode": {
        "label": "OpenCode",
        "user": "~/.config/opencode/skills", "project": ".opencode/skills", "home": "~/.config/opencode",
        "notes": ["Restart OpenCode if the skills do not appear."],
    },
    "antigravity": {
        "label": "Google Antigravity",
        "user": "~/.gemini/config/skills", "project": ".agents/skills", "home": "~/.gemini",
        "notes": ["Restart Antigravity if the skills do not appear.",
                  "Older Antigravity IDE versions read ~/.gemini/antigravity/skills instead. "
                  "If the skills do not load, run this script again with --dest and that folder."],
    },
    "hermes": {
        "label": "Hermes Agent",
        "user": "~/.hermes/skills", "project": ".hermes/skills", "home": "~/.hermes",
        "notes": ["Restart Hermes if the skills do not appear."],
        "project_notes": ["Hermes loads project skills only after you run: hermes skills trust"],
    },
    "agents": {
        "label": "Shared .agents folder",
        "user": "~/.agents/skills", "project": ".agents/skills", "home": "~/.agents",
        "notes": ["Codex and OpenCode read this folder. Other agents that follow the Agent Skills "
                  "format may read it too; check your agent's documentation."],
    },
}


def expand(path):
    return os.path.abspath(os.path.expanduser(path))


def skill_version(folder):
    """The version written in a skill's SKILL.md, or None."""
    try:
        with open(os.path.join(folder, "SKILL.md"), encoding="utf-8") as fh:
            head = fh.read(2000)
    except OSError:
        return None
    m = re.search(r'^\s*version:\s*"?([0-9][0-9A-Za-z.\-]*)"?\s*$', head, re.M)
    return m.group(1) if m else None


def is_ours(folder):
    """True when the folder holds a skill from this package."""
    try:
        with open(os.path.join(folder, "SKILL.md"), encoding="utf-8") as fh:
            return MARKER in fh.read(2000)
    except OSError:
        return False


def remove(path):
    if os.path.islink(path):
        os.unlink(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.unlink(path)


def show_list():
    print("Agents this script knows. 'found' means the agent's own folder exists on this computer.\n")
    print("  %-12s %-22s %-28s %s" % ("name", "agent", "for your user account", "inside one project"))
    for key, a in AGENTS.items():
        found = "found" if os.path.isdir(expand(a["home"])) else ""
        print("  %-12s %-22s %-28s %-18s %s" % (key, a["label"], a["user"], a["project"], found))
    print("\nInstall with:  python3 install.py --agent NAME")
    print("Any other agent:  python3 install.py --dest PATH-TO-ITS-SKILLS-FOLDER")
    print("Claude.ai and Claude Cowork: see INSTALL.md (upload the ZIPs or open the .plugin file).")


def check_calculators(target):
    script = os.path.join(target, "business-plan-coach", "scripts", "bizcalc.py")
    try:
        r = subprocess.run([sys.executable, script, "-h"], capture_output=True, timeout=60)
        ok = r.returncode == 0
    except (OSError, subprocess.SubprocessError):
        ok = False
    version = "%d.%d.%d" % sys.version_info[:3]
    if ok:
        print("Calculators: OK (Python %s)" % version)
    else:
        print("Calculators: could NOT run with Python %s. The skills need Python 3 to do the arithmetic." % version)
    return ok


def main():
    p = argparse.ArgumentParser(description="Install the Business Plan Studio skills for an AI agent.",
                                epilog="Run with --list to see the agents and folders.")
    p.add_argument("--agent", choices=sorted(AGENTS), help="the agent to install for")
    p.add_argument("--project", metavar="PATH", help="install inside this project folder instead of your user account")
    p.add_argument("--dest", metavar="PATH", help="install into this skills folder (for an agent not in the list)")
    p.add_argument("--list", action="store_true", help="show the agents and folders, then stop")
    p.add_argument("--dry-run", action="store_true", help="show what would happen without changing anything")
    p.add_argument("--uninstall", action="store_true", help="remove the four skills from the folder")
    p.add_argument("--force", action="store_true",
                   help="replace a folder of the same name even when it is not a Business Plan Studio skill")
    args = p.parse_args()

    if args.list or not (args.agent or args.dest):
        show_list()
        if not args.list:
            print("\nNothing was installed: name an agent with --agent, or a folder with --dest.")
        return 0
    if args.dest and args.project:
        p.error("use --dest or --project, not both")
    if args.project and not args.agent:
        p.error("--project needs --agent, so the script knows which folder name to use")
    if args.project and not os.path.isdir(expand(args.project)):
        p.error("the project folder does not exist: %s" % expand(args.project))

    agent = AGENTS.get(args.agent)
    if args.dest:
        target = expand(args.dest)
    elif args.project:
        target = os.path.join(expand(args.project), *agent["project"].split("/"))
    else:
        target = expand(agent["user"])
    doing = "Would" if args.dry_run else "Did"

    if args.uninstall:
        removed = 0
        for name in SKILLS:
            dst = os.path.join(target, name)
            if not os.path.lexists(dst):
                print("  %-32s not there" % name)
            elif not is_ours(dst) and not args.force:
                print("  %-32s left alone (not a Business Plan Studio skill)" % name)
            else:
                if not args.dry_run:
                    remove(dst)
                removed += 1
                print("  %-32s %s" % (name, "would be removed" if args.dry_run else "removed"))
        print("%s remove %d skill folder(s) from: %s" % (doing, removed, target))
        return 0

    missing = [n for n in SKILLS if not os.path.isfile(os.path.join(SOURCE, n, "SKILL.md"))]
    if missing:
        print("Cannot find the skills next to this script (looked in %s)." % SOURCE)
        print("Run install.py from the unzipped or cloned Business Plan Studio folder.")
        return 1

    # Refuse before touching anything if a same-named folder belongs to something else.
    foreign = [n for n in SKILLS
               if os.path.lexists(os.path.join(target, n)) and not is_ours(os.path.join(target, n))]
    if foreign and not args.force:
        print("These folders already exist in %s and are not Business Plan Studio skills:" % target)
        for n in foreign:
            print("  " + n)
        print("Nothing was changed. Move them away, or run again with --force to replace them.")
        return 1

    version = skill_version(os.path.join(SOURCE, SKILLS[0])) or "?"
    print("Business Plan Studio %s -> %s" % (version, target))
    ignore = shutil.ignore_patterns("evals", "__pycache__", "*.pyc", ".DS_Store")
    for name in SKILLS:
        src, dst = os.path.join(SOURCE, name), os.path.join(target, name)
        if os.path.lexists(dst):
            old = skill_version(dst)
            state = "replaces %s" % (old or "an existing copy")
            if not args.dry_run:
                remove(dst)
        else:
            state = "new"
        if not args.dry_run:
            os.makedirs(target, exist_ok=True)
            shutil.copytree(src, dst, ignore=ignore)
        print("  %-32s %s" % (name, state))

    if args.dry_run:
        print("Dry run: nothing was changed.")
        return 0

    ok = all(os.path.isfile(os.path.join(target, n, "SKILL.md")) for n in SKILLS)
    if not ok:
        print("Something went wrong: a SKILL.md is missing after the copy.")
        return 1
    check_calculators(target)

    print("\nNext:")
    notes = list(agent["notes"]) if agent else ["Restart your agent if the skills do not appear."]
    if agent and args.project:
        notes += agent.get("project_notes", [])
    notes.append('Start with: "%s"' % START_LINE)
    notes.append('If the agent does not pick the skill up, say: "Use the business-plan-coach skill."')
    for i, n in enumerate(notes, 1):
        print("  %d. %s" % (i, n))
    return 0


if __name__ == "__main__":
    sys.exit(main())
