# Team and Relationships

## What This File Is For

The key people in your work life and how you interact with each of them. Agents use this to prep for meetings, draft communications, and understand the human context around your work. An agent prepping your 1:1 needs to know who the person across the table is, what they care about, and what you need from each other.

---

## Redaction Tiers

This file usually holds the most sensitive content in the whole portfolio — real names, reporting structures, personal dynamics. Before you fill it out, decide how exposed it's going to be, because that changes how much identifying detail belongs in it.

| Tier | What it looks like | Use when |
|------|--------------------|----------|
| **Full names** | "Priya Patel, VP of Product" | A private fork or local-only file — a portfolio that never leaves your machine or your own AI accounts. |
| **Initials** | "P.P., VP of Product" | Shared with a small trusted group, or injected into tools where the model provider doesn't need real identities to be useful. |
| **Roles-only** | "VP of Product (my manager)" | Committed to a shared or public repo, used in a demo, or injected into any system prompt / MCP resource that could be logged, screenshotted, or seen by someone outside your org. |

Default to **roles-only** if you're unsure — you can always add real names back into a private local copy later. Roles-only loses almost nothing an agent needs: the dynamics ("what they need from me," "what I need from them," "context for agents") are the useful part of this file, and none of it depends on a real name.

If you mix tiers within one file (e.g., initials for peers, full names for people who already know you're doing this), say so at the top of the file so future-you — and any agent reading it — knows why.

---

## Interview Protocol

*Hand this entire file to your AI build partner and say "let's do this one." Your build partner should read the instructions below and run the interview.*

**Instructions for the build partner:** You're helping the user create their team and relationships file. Before you start, confirm which redaction tier applies (see above) — it decides whether you're writing full names, initials, or roles-only. Then get the list of key people, and go through each one. Use what you already know from previous files — if they mentioned collaborators during the projects or role interviews, reference them rather than re-asking.

**Questions to ask:**

0. Is this file going somewhere private/local, or somewhere it might be shared (a repo, a demo, a shared drive)? That decides the redaction tier — full names, initials, or roles-only.
1. Who are the 5-8 people you interact with most in your work? Give me names and roles.
2. [For each person:] What's your working relationship with [name]? How do you typically interact — meetings, Slack, email?
3. What does [name] need from you, and what do you need from them?
4. Is there anything an AI working on your behalf should know about working with or preparing for interactions with [name]? Style preferences, things to be careful about, context that matters?

**When you have enough:** After you've covered each person the user named.

**After drafting:** Present the draft. Ask the user to check whether the dynamics feel right — the "what they need from you" and "what you need from them" sections are where the real value is, and they're easy to get subtly wrong.

---

## Output Structure

```markdown
# Team and Relationships

[Repeat this block for each key person.]

## [Name]

**Role:** [Their title or role.]
**Relationship:** [Manager / Direct Report / Peer / Client / Collaborator / Stakeholder / etc.]
**How We Interact:** [Regular 1:1s, async Slack, project-based, ad hoc, etc. Include cadence if regular.]
**What They Need From Me:** [What they depend on you for.]
**What I Need From Them:** [What you depend on them for.]
**Context for Agents:** [Anything an AI should know when preparing for or communicating with this person — their communication style, preferences, sensitivities, working patterns.]
```

**Redaction note:** if you're using the initials or roles-only tier, swap the `## [Name]` heading accordingly — e.g. `## P.P.` (initials) or `## VP of Product (my manager)` (roles-only). Everything else in the block stays the same; the value is in the dynamics, not the name.
