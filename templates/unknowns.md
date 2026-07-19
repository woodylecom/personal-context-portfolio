# Unknowns & Open Questions

## What This File Is For

A single place to collect what's missing, uncertain, or "TBD" across your portfolio. The goal is to keep gaps visible so they get closed over time — not lost inside longer files. This file also tells agents what NOT to assume: anything you've deliberately left out belongs here too, so an agent doesn't try to "helpfully" fill the gap with a guess.

This is one of five **optional modules** in this kit (see [`voice-anti-examples.md`](voice-anti-examples.md), [`operational-boundaries.md`](operational-boundaries.md), [`current-state.md`](current-state.md), [`personal-use.md`](personal-use.md)). The core ten files are a complete portfolio on their own — these add more precision once you want it.

---

## Interview Protocol

*Hand this entire file to your AI build partner and say "let's do this one." Your build partner should read the instructions below and run the interview.*

**Instructions for the build partner:** This file works differently from the others — you're not drafting a description, you're compiling a list. Review what's already been built (the other completed files) and ask the user to name gaps directly. Keep going until they run out; don't pad the list to make it look more thorough.

**Questions to ask:**

1. Looking back at the files we've built so far, is there anything that felt like a guess rather than a real answer? Anything you weren't sure about while we were drafting it?
2. Is there anything you're deliberately choosing NOT to include in this portfolio — not because you forgot, but on purpose? (Privacy, doesn't change often enough to matter, not relevant to how agents work with you, etc.)
3. Are there decisions still in flight where you don't know the answer yet, but an agent should know that you don't know?
4. Is there anything about how you work that you genuinely haven't figured out yourself yet?

**When you have enough:** Once the user runs out of gaps. This file can be short — "None currently" under Open Unknowns is a valid, good answer after the initial pass.

**After drafting:** This file isn't "done" the way the others are — treat it as a living register. When a gap gets filled later (a decision gets made, a project's status becomes clear), move the answer into the relevant file and delete the entry here rather than leaving it stale.

---

## Output Structure

```markdown
---
updated: YYYY-MM-DD
stability: evolving
scope: open-questions
---

# Unknowns & Open Questions

## Open Unknowns

[Things that are genuinely uncertain or TBD right now. One line each, with enough context that an agent knows what NOT to assume. Delete entries once resolved — move the answer into the relevant file instead.]

## Intentionally Excluded

[Things you've deliberately left out of the portfolio — not gaps, choices. Note briefly why, so a future agent (or future you) doesn't try to "fix" the omission.]

## How to Use This File

- When an agent is given the full portfolio, it reads this file to know what NOT to assume.
- When you're reviewing the portfolio periodically, this is the "open loops" list.
- Entries here aren't blockers — the portfolio is usable as-is. This file just keeps the gaps honest.
```
