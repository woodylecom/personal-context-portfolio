# Personal Use

## What This File Is For

Two things. First, a mapping: the core ten templates speak in workplace language — roles, teams, projects, stakeholders — but every one of them has a personal-life reading, and this file shows you the translation so you can build a portfolio for your household, your family, or your life outside work without inventing new structure. Second, hard redaction rules for minors: if anyone described in your portfolio is a child, there are things that should never be written into a context file at all — not "redact before sharing," never written. The interview at the bottom produces a short filled-out file recording your mapping decisions and your household's standing redaction rules, so any agent working on family-related content loads the rules along with the context.

This is one of five **optional modules** in this kit (see [`unknowns.md`](unknowns.md), [`voice-anti-examples.md`](voice-anti-examples.md), [`operational-boundaries.md`](operational-boundaries.md), [`current-state.md`](current-state.md)). The core ten files are a complete portfolio on their own — this adds more precision once you want it.

---

## The Personal-Use Mapping

The templates weren't written twice — once for work, once for home — because the structure is the same; only the nouns change. Read each core file this way:

| Core file | Workplace reading | Personal/family reading |
|---|---|---|
| `identity.md` | Who you are professionally | Who you are, period — life stage, household shape, what a normal week looks like |
| `role-and-responsibilities.md` | What your job actually involves | Your roles at home: parent, caregiver, the one who handles the money, the one who cooks |
| `current-projects.md` | Active workstreams | The renovation, the move, the school-year logistics, the trip you're planning |
| `team-and-relationships.md` | Colleagues and stakeholders | Household members, extended family, close friends — the most redaction-sensitive file; see below |
| `tools-and-systems.md` | Your work stack | Family calendar, budgeting app, shared drives, smart-home setup |
| `communication-style.md` | How you write at work | Mostly unchanged — add family registers if they differ (texts to your partner vs. emails to a teacher) |
| `goals-and-priorities.md` | What you're optimizing for at work | Savings targets, health, time with people, what you're deliberately not doing this year |
| `preferences-and-constraints.md` | Work rules and preferences | Dietary rules, budget ceilings, bedtimes, "never schedule over family dinner" |
| `domain-knowledge.md` | Professional expertise | What you know that matters at home: caregiving specifics, the house's quirks, traditions |
| `decision-log.md` | How you make work decisions | Big household calls and how you actually made them |

The interview protocols inside the core templates are work-flavored; translate the questions the same way ("who are the 5-8 people you interact with most" becomes "who's in your household and close orbit"). Don't force all ten — a personal portfolio often starts with `identity.md`, `preferences-and-constraints.md`, and `team-and-relationships.md` and grows from there. The other optional modules map too: `current-state.md` works as a weekly family snapshot, and `operational-boundaries.md` matters *more* at home — "never contact my kid's school on my behalf" is exactly the kind of rule it exists to hold.

---

## Minors: What Never Goes In

The redaction tiers in [`team-and-relationships.md`](team-and-relationships.md) (full names / initials / roles-only) are a choice adults make about their own exposure. A child can't make that choice, and you can't make it for them retroactively — so minors get a stricter rule set that applies at **every** tier, including in a portfolio you believe is private.

Calibrate against the worst case, because this kit is built for it: portfolios live in version-controlled repos, get forked, get pasted into chat tools, get wired into MCP servers and system prompts, get synced across machines. One push to the wrong remote, one repo flipped from private to public, and everything ever committed — including things you deleted later, which live on in history — is exposed. Write every file as if that has already happened. A `.gitignore` entry is a plan to be careful; it is not a redaction strategy.

### Never write these about a child — at any tier, in any file

- **Full legal name** — or a nickname plus surname that identifies them just as well
- **Date of birth**, or exact age combined with any other identifier
- **School, daycare, camp, team, or program names** — including class names, jersey numbers, and schedules tied to a named place
- **Exact age + location combinations** — "my 9-year-old in Springfield" identifies a child nearly as well as a name
- **Medical, psychological, or developmental details** — diagnoses, medications, therapy, IEP/504 status
- **Custody, adoption, or legal-case specifics** — arrangements, case details, characterizations of the other parent
- **Likeness and account identifiers** — social media handles, links to tagged photos, physical descriptions precise enough to pick them out
- **Government or financial identifiers** — SSN, insurance IDs, passport numbers (these don't belong in *anyone's* portfolio)

### Generalize instead

The working pattern: **relationship label + broad age band**, plus logistics in functional terms. Give each child one stable label and use it in every file, so agents can track "who" without ever holding an identity.

| Instead of | Write | What the agent still gets |
|---|---|---|
| "Maya Chen, born 2017-04-02, 3rd grader at Oakwood Elementary" | "my eldest (grade-schooler)" | Birth order and life stage — enough for gifts, tone, and logistics |
| "Pickup at Oakwood is 3:10, Mrs. Alvarez's class" | "school pickup mid-afternoon on weekdays — hard stop" | The scheduling constraint, which is all it ever needed |
| "Leo (6) has ADHD, takes 10mg guanfacine at 7am" | "my youngest needs a structured morning routine — keep mornings simple" — or nothing at all | The functional need. The chart stays with the doctor. |
| "I have the kids Wed-Sun per the custody agreement" | "the kids are with me the back half of each week" | The calendar reality, minus the legal file |
| "Maya's soccer at Riverside Park, #12, Saturdays 9am" | "one kid has a Saturday-morning activity in season" | The recurring block to schedule around |

Age bands that work: baby, toddler, preschooler, grade-schooler, middle-schooler, teen. They're precise enough for any agent task and too vague to identify anyone.

Medical and psychological details deserve the strictest line: they usually stay out entirely, even generalized — a portfolio is not a medical record, and almost no agent task needs one. When safety genuinely requires it (a severe allergy an agent planning meals must know about), state it at the household level, not attached to a child: "severe nut allergy in the household — check every food suggestion."

### Two tests before a detail goes in

1. **Could a stranger use it?** If a detail — alone or combined with others already in the portfolio — could let a stranger identify the child, find where they'll be, or learn something about their body or mind, it stays out. Watch the combinations: an age band, a city, a rare hobby, and a dietary restriction each look safe alone and identify a specific kid together.
2. **Does it change what an agent does?** An agent planning your week needs "pickup mid-afternoon," not the school's name. An agent drafting a birthday reminder needs "my eldest's birthday is in early April," not a date of birth. If the specific fact doesn't change the agent's output, the general one wins by default.

Only a detail that passes both belongs in a file — and for minors, when in doubt, out.

### Building a portfolio *for* a child

Same rules, tightened: if the portfolio's subject is the minor (a homework-helper context file, for instance), keep it thin, local-only, and first-name-or-label only — and never put it in a repo you'd ever fork public. A kid's portfolio is the one file set in this kit that should not follow the "fork it and version it" default.

---

## Interview Protocol

*Hand this entire file to your AI build partner and say "let's do this one."*

**Instructions for the build partner:** Run this file FIRST if the portfolio covers personal or family life — before drafting any other file — because it sets rules the other interviews must obey. Two hard rules for you: (1) never write anything from the never-include list into *any* file, even if the user volunteers it — generalize it on the spot and say that's what you did; (2) once a child has a label, use it everywhere and never ask for the real name.

**Questions to ask:**

1. Will any part of this portfolio ever leave this machine — a repo, a shared drive, a chat tool, an MCP resource? (Assume yes unless the user is certain. The minors rules apply either way; this decides the adults' tier.)
2. Who's in your household and close orbit, and who among them is under 18?
3. For each adult: which redaction tier — full names, initials, or roles-only? (See the tiers in `team-and-relationships.md`.)
4. For each minor: pick a stable label — relationship + age band, like "my eldest (teen)." This is their name in every file from now on.
5. Is there anything about a child an agent genuinely needs to do its job — a safety-critical allergy, a hard schedule constraint? Capture it in functional, household-level terms.
6. Which core files are you repurposing for personal use, and what does each one cover in your life?

**When you have enough:** Once every minor has a label, every adult has a tier, and the mapping is decided. This is a short interview — the value is in the rules, not the length.

**After drafting:** If any other files were drafted before this one, re-scan them for real names, birthdates, school names, and the rest of the never-include list, and fix what you find now — not in a later "cleanup pass" that never comes.

---

## Output Structure

```markdown
---
updated: YYYY-MM-DD
stability: stable
scope: personal-use-rules
---

# Personal Use

## How This Portfolio Maps

[Which core files you've repurposed and what each covers in your personal life. One line each.]

## Household Labels

[One stable label per person. Adults: name, initials, or role per your chosen redaction tier. Minors: relationship + age band only — "my eldest (grade-schooler)." These are the only identifiers any file or agent output uses.]

## Standing Rules for Minors

[The never-include list as you've adopted it, plus anything stricter your household adds. Agents treat this as hard policy, not preference.]

## Agent Rules

[What an agent must do when content touches family: use the labels above everywhere, including new drafts; never ask for or record anything on the never-include list; flag anything external-facing that mentions a minor for review before it goes anywhere.]
```
