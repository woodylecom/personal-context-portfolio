# Frontmatter Convention

## What This File Is For

Not an interview template — a shared convention for any file in your portfolio. Frontmatter lets an agent look at a file and know two things without reading it in full: how recently it was checked, and how much to trust it. This matters more as your portfolio grows past the core ten files.

This convention is used by the four optional modules ([`unknowns.md`](unknowns.md), [`voice-anti-examples.md`](voice-anti-examples.md), [`operational-boundaries.md`](operational-boundaries.md), [`current-state.md`](current-state.md)) — see each one's "Output Structure" section for a worked example.

---

## The Convention

Any context file that carries frontmatter starts with a three-line YAML block:

```markdown
---
updated: YYYY-MM-DD
stability: stable | evolving | draft
scope: short-slug-describing-the-file
---
```

- **`updated`** — the date this file was last reviewed and confirmed accurate, not just last edited.
- **`stability`**:
  - `stable` — settled facts that rarely change (identity, most of preferences-and-constraints, voice anti-examples).
  - `evolving` — true today, expected to shift on a regular cadence (current-projects, goals-and-priorities, current-state, unknowns).
  - `draft` — a first pass that hasn't been reacted to and corrected yet. Agents should re-verify before relying on it.
- **`scope`** — a short slug (a few words, kebab-case) describing what the file covers. Helps an agent that only gets one file dropped into context understand its role at a glance.

## Where to Use It

Frontmatter is opt-in per file, not mandatory across the whole portfolio — a one-page identity file you wrote once and rarely touch doesn't need it. It earns its keep on:

- Anything with a real update cadence (`current-projects.md`, `current-state.md`, `goals-and-priorities.md`).
- Anything you want an agent to actively distrust once stale (`current-state.md` especially — see its staleness rule).
- The four optional modules in this kit, which use it by convention. Adopt it on the core ten files too if you want the same protection everywhere.

## How Agents Should Use It

- Trust `stable` files at face value.
- Re-verify `evolving` and `draft` files against the current conversation before acting on them — if the user says something that contradicts the file, the conversation wins; flag the file as stale rather than silently overriding it.
- If `updated` is old relative to the file's own cadence (see `current-state.md`'s 10-day rule as the reference point), say so before relying on the content.

## If You Fork This

[`tools/validate.py`](../tools/validate.py) checks any file that has frontmatter for a well-formed `updated`/`stability`/`scope` block — it does not require frontmatter on files that don't use it. If you want to make frontmatter mandatory across your own fork (for example, on every persona example file in a shared team repo), that's a validator change, not a content change — see the comments in `validate.py` for where to extend it.
