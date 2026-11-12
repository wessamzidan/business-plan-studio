# Contributing

Thank you for helping Business Plan Studio work better for founders everywhere.

## What helps most

- **New business types or sector examples.** A fictional business, a weak answer and a strong answer for the same question.
- **Country starting points.** Tax, social insurance, registration and licensing figures, each with a source and a date.
- **Arabic.** Native-quality examples, corrections to existing wording, and Arabic terms for lessons. Other languages are welcome too.
- **Bug reports from real sessions.** What you asked, what Claude did, and what you expected.
- **Tests for the calculators.** Known-answer tests, with the expected value worked out independently of the code.

## Ground rules

1. **Examples are fictional.** Never submit a real company's figures, a client's plan, or anyone's personal data.
2. **Keep the claim labels** (Verified, Estimate, Planned, To confirm) and the rule that Claude never invents a fact.
3. **Dated facts need a source and a date.** Present them as starting points to confirm with an accountant or lawyer, never as advice.
4. **One question per coaching reply.** Keep each `SKILL.md` short and put detail in its `references/` folder.
5. **Run the tests** before you open a pull request: `python3 tests/test_scripts.py`. A change to a calculator needs a new test.
6. **Leave the packaged files alone.** The ZIPs in `claude-ai-uploads/` and `business-plan-studio.plugin` are rebuilt by the maintainer at each release.

## How to propose a change

Open an issue first for anything large. For a small fix, fork the repository, make the change on a branch, and open a pull request that says what you changed and why.

By contributing, you agree that your work is licensed under the Apache License 2.0, like the rest of the project. Please keep the `LICENSE` and `NOTICE` files in any copy you share.
