# Current State

## What This File Is For

A living weekly snapshot — what's actually happening right now, as opposed to the slower-moving files ([`current-projects.md`](current-projects.md), [`goals-and-priorities.md`](goals-and-priorities.md)). This is the file most likely to go stale, and a stale snapshot actively misleads rather than just under-informing. If you're not going to update it on a real cadence, don't build it — a missing file is more honest than a six-month-old one.

This is one of five **optional modules** in this kit (see [`unknowns.md`](unknowns.md), [`voice-anti-examples.md`](voice-anti-examples.md), [`operational-boundaries.md`](operational-boundaries.md), [`personal-use.md`](personal-use.md)). The core ten files are a complete portfolio on their own — this adds more precision once you want it.

---

## Interview Protocol

*Hand this entire file to your AI build partner and say "let's do this one."*

**Instructions for the build partner:** Unlike the other files, this one is meant to be regenerated regularly, not drafted once. Run this as a quick weekly check-in rather than a long interview — the goal is 5 minutes, not 30.

**Questions to ask:**

1. What are the 1-3 things you're most focused on this week?
2. What went well in the last week or two — any wins worth noting?
3. What's been friction — blocking, annoying, or not working?
4. Are there any decisions you're actively weighing right now (distinct from ones you've already made — those go in `decision-log.md`)?
5. Are there any numbers worth tracking week over week for your work?
6. Anything coming up — deadlines, unusual meetings, expected handoffs?

**When you have enough:** After a quick pass through all six — this should take minutes, not a full interview session.

**After drafting:** Set a real cadence (weekly is the default) and a real reminder. This file is only useful if `updated` stays current — see the staleness rule in the Output Structure below.

---

## Output Structure

```markdown
---
updated: YYYY-MM-DD
stability: evolving
scope: current-state
cadence: weekly
---

> Stale snapshots actively mislead. If `updated` is more than 10 days old, treat this file with suspicion and lean on the slower-moving files instead.

# Current State

## This Week's Focus

[1-3 top priorities for the current week.]

## Recent Wins
*(last 1-2 weeks)*

[What worked, what shipped, what closed.]

## Recent Friction
*(last 1-2 weeks)*

[What's blocking, what's annoying, what didn't work.]

## Active Decisions in Flight
*(currently weighing — distinct from `decision-log.md`, which captures decisions already made)*

[Open decisions you're actively working through right now.]

## Numbers Worth Tracking

| Metric | Value | As of |
|---|---|---|
| [metric] | [value] | [date] |

[Update on your cadence. Anything that drifts week over week belongs here.]

## Coming Up

[Deadlines, special meetings, expected handoffs — anything non-routine.]
```

**A note on `stability`:** this kit normalizes weekly-cadence files to `evolving` rather than adding a separate `living` tier. If you want that distinction in your own fork, add it to `VALID_STABILITY` in [`tools/validate.py`](../tools/validate.py) and document it in [`templates/_frontmatter.md`](_frontmatter.md).
