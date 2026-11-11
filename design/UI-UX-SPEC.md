# Business Plan Coach — UI/UX Specification

Version 2 turns the plan into one path: 14 steps in 5 sittings, one question at a time. It works for any business and any reader, in English or Arabic, on a phone or a laptop. The screens are drawn in the mockups in [screenshots/](screenshots/), using a fictional snack maker, Nour Bites. This is a design concept: nothing here is built yet.

## 1. What changed from version 1

Version 1 copied the layout of one incubator's form. Version 2 keeps nothing of that form in the main flow.

|  | Version 1 | Version 2 |
| --- | --- | --- |
| Structure | 10 areas taken from one incubator form | One path of 14 steps, the same for every business |
| Order | Fixed by the form | Set by the reader: bank, investor, incubator, grant, internal or partner |
| Home screen | Dashboard with 5 hubs and 3 levels | One screen: the next step and the path |
| Question screen | A form field with a character limit | One question, one answer box, coach feedback under it |
| Numbers | Three tabs of tables | Three numbers first, then one chart |
| Online forms | The whole app was built around one portal | Any form is one export option at the end |
| Sample content | One real company's plan | A fictional business, safe to show anyone |
| Look | Grey and blue, table-heavy | White ground, one green, one amber, larger type |

## 2. The path

The whole plan is one numbered path. The founder always sees which step they are on, which sitting it belongs to and how long that sitting takes.

Other readers get the same 14 steps in another order, cut into sittings by the same rule; section 9 lists all six. The executive summary is always last, because it is written from the saved answers.

## 3. Design principles

Six rules decide every screen. When two ideas compete, the one higher in the table wins.

| Principle | On screen this means |
| --- | --- |
| One thing at a time | One question per screen and one main button per screen |
| Always show where I am | Step 8 of 14, the sitting, and minutes left are visible; the path is one tap away |
| Teach in the moment | "Why it matters" sits above every question; lessons and examples open next to the answer, and examples only after a first try |
| Honest numbers | Every number carries a label: Verified, Estimate, Planned or To confirm. The app calculates; it never guesses a figure |
| Never lose work | Each accepted answer saves itself; "Skip for now" parks a question; the founder can stop at any point |
| Same on a phone, same in Arabic | One column at 390 px; full right-to-left layout with native Arabic copy |

**Tone.** Warm, short and specific. The coach names one strength, then asks one question. It never says "great answer" and never blames the founder for an error.

## 4. Screens

Five screens cover the whole product. Three of them are tabs in the top bar: My plan, Numbers, and Check and export.

Welcome appears once. A step opens from the path and closes back to it; when a question needs a calculation, the step links straight to Numbers.

| Screen | The founder's question | Main button | Also on screen |
| --- | --- | --- | --- |
| Welcome | What do I need to start? | Show me my path | The business in two sentences; reader; stage; coaching level; language |
| My plan | Where am I and what is next? | Continue | The path by sitting; plan health; what the founder gets at the end |
| Step | What do I write here? | Check my answer | Why it matters; prompts; label; lesson and example beside the answer |
| Numbers | Will the money work? | Change an input | Lowest cash, break-even, money needed; cash chart; downside case |
| Check and export | Is it ready, and how do I send it? | Download the plan | Readiness for the chosen reader; the 14 checks; six outputs |

Each screen is drawn in [screenshots/](screenshots/), with the step screen also shown on a phone in English and in Arabic.

## 5. The coaching step

The step screen repeats one loop: ask, answer, check, save. A weak answer gets one follow-up at a time and at most two; after that the gap is saved as "To confirm" and the founder moves on.

**Parts of the screen, top to bottom**

1. **Where we are.** "Business model and pricing, question 2 of 4", with one dot per question.
2. **Why it matters.** One or two lines on what the reader decides from this answer.
3. **The question.** One sentence that asks for one thing.
4. **Think about.** Two or three short prompts.
5. **Answer.** A text box. When the answer is a choice, three to five chips plus "Something else" and "Not sure yet".
6. **Label.** Where a number comes from: Verified, Estimate, Planned or To confirm.
7. **Buttons.** Check my answer, Help me think, Show an example, Skip for now. After the first check, the filled button moves to the follow-up question and this one becomes "Check again".
8. **Coach feedback.** One strength, the checklist line, a quick calculation when a number is involved, and one follow-up question.
9. **Tighter version.** The founder's own facts with the padding cut. The founder picks Keep it, Edit or Keep mine.

**Lesson and example.** A lesson card opens the first time a concept appears, for founders who chose "New to this", and never twice. An example card shows one weak and one strong answer from a different sector, and only after the founder's first try.

**Help me think** works down a ladder and stops as soon as the founder can answer.

1. Split the question into two or three smaller ones.
2. Offer options to choose from.
3. Show one example pair.
4. Offer a working assumption, labelled Estimate or To confirm.
5. Park the question and move on.

## 6. Numbers screen

The founder sees three numbers before any table: the lowest cash point, the break-even month and the money needed. Everything else on the screen explains those three.

1. **Three numbers.** Lowest cash and its month, against the safety buffer. Break-even month. Money needed, against the amount asked for.
2. **One chart.** Cash at the end of each month, with the buffer drawn as a line and the lowest point marked.
3. **The downside case.** What happens if sales are lower, in one sentence, with the response the founder planned.
4. **What moves cash most.** Three plain rows from the sensitivity run, such as "price 10% lower".
5. **Year table.** Revenue, gross margin, EBITDA, net profit and cash at year end.
6. **Inputs.** Every figure the founder gave, each with its label and an Edit button.

A problem is shown as a sentence, never as a code.

| Check result | What the founder sees | Where |
| --- | --- | --- |
| Blocking, such as cash below zero | What disagrees, why the reader cares, and two ways to fix it | Top of Numbers, and on My plan |
| Advisory, such as a number without a label | One short line with a "Fix" link | Plan health on My plan |
| Pass | Nothing, unless the founder opens "Show all 14 checks" | Check and export |

All arithmetic comes from the skill's calculators, so the screen and the exported plan always agree. Price and margin points are shown as illustrations; the price stays the founder's decision. The app never fills a gap with a "typical" figure; it asks for the founder's own.

## 7. Look and feel

The look is calm and bright: a near-white ground, one green for action and progress, one amber for attention. Colour always comes with a word or an icon, never alone.

**Colours**

| Name | Value | Used for | Contrast |
| --- | --- | --- | --- |
| Ground | #F6F8F7 | Page background |  |
| Surface | #FFFFFF | Cards and inputs |  |
| Ink | #12211C | Text | 15.6:1 on ground |
| Muted | #51605A | Secondary text | 6.2:1 on ground |
| Line | #DCE3DF | Card borders |  |
| Control border | #8A9690 | Input borders | 3.1:1 on white |
| Green | #0B6B4F | Main buttons, done, progress | 6.5:1 with white text |
| Green tint | #E2F1EB | Current step, selected choice |  |
| Amber | #F5B83D, tint #FFF3D6, text #7A4B00 | In progress, things to look at | 6.7:1 text on tint |
| Red | #A8321F on #FCE9E4 | Blocking problems only | 5.7:1 |
| Blue | #1D5FA8 on #E6EFF9 | Estimate label | 5.6:1 |
| Violet | #5B3FA6 on #EDE8F8 | Planned label | 6.5:1 |

**Type.** Readex Pro for both English and Arabic, so the two languages share one voice. Sizes: 32 for a screen title, 28 for a question (20 on a phone), 24 for section titles, 18 for card titles, 16 for body, 14 for helper text. Weights 400, 500 and 600. Line height 1.5 in English and 1.7 in Arabic.

**Shape and space.** Spacing steps of 8, 12, 16, 24, 32 and 48 px. Cards have a 16 px radius and a 1 px line, with no shadow. Buttons have a 12 px radius and are at least 44 px tall. Choice chips are fully rounded.

**Claim labels.** Each label is an icon, a word and a colour: Verified (tick, green), Estimate (wave, blue), Planned (calendar, violet), To confirm (question mark, amber).

**Components**

| Component | Where | Note |
| --- | --- | --- |
| Top bar | Every screen | Three tabs: My plan, Numbers, Check and export |
| Continue card | My plan | The only filled green button on the screen |
| Sitting card and step row | My plan | Status shown as icon and word: Done, In progress, To do |
| Question card | Step | Why it matters, question, prompts, answer, label |
| Choice chip | Welcome, Step | Single or multiple choice; selected state uses green tint and a tick |
| Coach feedback card | Step | Strength, checklist, quick calculation, one follow-up |
| Lesson card and example card | Step | Beside the answer on a laptop, under it on a phone |
| Number tile | Numbers | One number, its unit, one line of meaning |
| Cash chart | Numbers | One line, one buffer line, two marked points |
| Check row | Check and export | Plain sentence, with Pass or Look at this |
| Output card | Check and export | Name, format, Download |

**Copy rules.** A button says what happens next: "Check my answer", never "Submit". Numbers are grouped by the user's locale. No emoji.

## 8. Arabic, phone and accessibility

Arabic and the phone layout are designed first-class, not adapted afterwards. The two phone mockups show the coaching step in English and in Arabic.

| Area | Rule |
| --- | --- |
| Direction | Arabic sets right-to-left on the whole page. The path, progress dots and back arrows mirror. The cash chart does not mirror: time still runs left to right |
| Arabic copy | Written natively, not translated word for word. Step names and labels come from the skill's own Arabic terms |
| Labels in Arabic | مؤكَّد · تقدير · مخطَّط · بحاجة إلى تأكيد |
| Digits and money | Western digits (0 to 9) in both languages; currency names written in Arabic in Arabic text |
| Mixed text | A number or Latin name inside an Arabic sentence is isolated, so it does not reorder the sentence |
| Phone | One column below 720 px. The three tabs move to a bar at the bottom. Lesson and example open under the question. Sitting cards stack. Wide tables scroll inside their own box |
| Touch | Every control is at least 44 px tall |
| Contrast | Text is at least 4.5:1 against its background; the values are listed in section 7 |
| Keyboard | Every control is reachable with Tab and shows a 2 px green focus ring. Ctrl or Cmd with Enter runs "Check my answer" |
| Screen reader | Progress is read as "Step 8 of 14". Coach feedback is announced when it arrives, without moving focus |
| Motion | Transitions last 200 ms or less and are removed when the device asks for reduced motion |

## 9. Build notes

Every screen is a view of one file, `plan_state.json`, and every action calls a script that already ships in Business Plan Studio 2.1.0. The app adds no business logic of its own.

| Screen | Calls | Reads and writes |
| --- | --- | --- |
| Welcome | `plan_state.py init` | Creates the plan file: name, one-line description, business type, stage, country, currency, reader, coaching level, language |
| My plan | `plan_state.py map` and `next`, `check_plan.py` | Status of each step, the next question, check results |
| Step | The step's module file, then `plan_state.py set`, `num`, `label`, `lesson`, `question`, `assume` | Section text, label, status, numbers, lessons already taught, parked questions |
| Numbers | `fin_model.py`, `bizcalc.py`, `plan_state.py import-numbers`, `check_plan.py` | Model inputs, monthly results, scenarios, sensitivity |
| Check and export | `score_plan.py`, `check_plan.py`, `render_plan.py`, `fin_model.py --xlsx` | Readiness, the 14 checks, plan document, one-pager, canvas, deck outline, form answers, spreadsheet |

**Sittings.** A sitting is a display grouping only. Steps follow the reader's order from the skill; a new sitting starts when the next step would take the sitting past 45 minutes. With the skill's time estimates this gives 5 sittings and 180 minutes for every reader.

| Reader | Sitting 1 | Sitting 2 | Sitting 3 | Sitting 4 | Sitting 5 |
| --- | --- | --- | --- | --- | --- |
| Incubator | Snapshot, Customer, Offer, Validation | Market, Competition, Model | Go-to-market, Operations, Team | Financials, Risks | Strategy, Summary |
| Bank | Snapshot, Offer, Customer, Operations | Team, Market, Competition | Model, Go-to-market, Validation | Financials, Risks | Strategy, Summary |
| Investor | Snapshot, Customer, Offer, Market | Validation, Competition, Model | Go-to-market, Team, Operations | Financials, Strategy | Risks, Summary |
| Grant | Snapshot, Customer, Offer, Strategy | Validation, Operations, Team | Financials, Risks | Market, Competition, Model | Go-to-market, Summary |
| Internal | Snapshot, Offer, Customer, Go-to-market | Operations, Team, Model | Financials, Strategy | Risks, Market, Competition | Validation, Summary |
| Partner | Snapshot, Offer, Customer, Market | Model, Go-to-market, Operations | Team, Strategy, Risks | Financials, Competition | Validation, Summary |

**Acceptance checks.** The build is done when all of these hold.

- [ ] A first-time founder reaches the first question from Welcome with one text answer and four taps
- [ ] Every screen has exactly one filled green button
- [ ] Every coach reply ends with exactly one question
- [ ] Every number on screen shows one of the four labels
- [ ] Closing the browser in the middle of a step loses no accepted answer
- [ ] Every screen works at 390 px wide with no sideways scrolling
- [ ] The Arabic layout is fully mirrored and the copy passes a native-speaker read
- [ ] Numbers on the Numbers screen equal the calculator output for the same inputs
- [ ] Text contrast is at least 4.5:1 and every control is reachable by keyboard

## 10. Open questions

Five decisions are still open; each changes what gets built.

- [ ] Brand: keep this neutral look, or let each organisation add its own colours?
- [ ] Platform: a standalone web app, or these screens as pages that open inside Claude next to the skill?
- [ ] Accounts: do founders sign in, or is carrying the plan file enough for a first release?
- [ ] Sittings: is 45 minutes the right ceiling, or should the founder choose a sitting length on Welcome?
- [ ] Readiness: show the score out of 100, or only the verdict (Ready, Nearly ready, Needs work, Not ready)?
