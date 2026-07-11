# Operational Boundaries

## What This File Is For

Hard rules for how agents should act when working with you, on your behalf, or on your content. Pairs with [`voice-anti-examples.md`](voice-anti-examples.md) — that file covers *how* to write; this one covers *what not to do operationally*. This is the file that prevents an agent from sending something it shouldn't, fabricating something it doesn't know, or quietly dropping a rule three turns into a conversation.

Keep domain-specific verification rules (clinical, legal, financial, technical — whatever your field requires) generic here and specific in your own notes or a persona pack. This template ships with a placeholder for that section rather than someone else's field-specific rules — don't copy clinical or legal boilerplate from an example that isn't your field.

This is one of four **optional modules** in this kit (see [`unknowns.md`](unknowns.md), [`voice-anti-examples.md`](voice-anti-examples.md), [`current-state.md`](current-state.md)). The core ten files are a complete portfolio on their own — this adds more precision once you want it.

---

## Interview Protocol

*Hand this entire file to your AI build partner and say "let's do this one."*

**Instructions for the build partner:** This file is rules, not preferences — the difference from `preferences-and-constraints.md` is that violating one of these isn't just annoying, it's a real problem (a bad send, a fabricated fact, a broken confidence). Push for the failure mode, not the abstract principle: "what's the worst thing an agent could do here?"

**Questions to ask:**

1. Are there actions an agent should never take on your behalf without your explicit approval first — sending a message, accepting a meeting, posting something, anything external-facing?
2. Does your field have rules about fabrication or verification — things an AI should never guess at and should cite a real source for instead?
3. When an agent isn't sure about something, how do you want it to signal that — should it distinguish between "I know this," "I'm inferring this," and "I'd need to check"?
4. What's the worst version of an agent "losing the thread" across a long conversation — forgetting a correction, drifting back to a default behavior you already told it to stop? Give a real example if you have one.
5. If a request would violate one of these rules, or two rules ever conflicted, what should the agent do — proceed, ask, or refuse?

**When you have enough:** After 4-5 questions covering at least the external-actions and uncertainty categories. The domain-specific section can stay a placeholder if your field doesn't have hard verification rules — don't force content into it.

**After drafting:** Present the draft and ask if there's a rule they've had to repeat to an AI more than once. Repeated corrections are exactly what belongs here.

---

## Output Structure

```markdown
---
updated: YYYY-MM-DD
stability: stable
scope: hard-rules
---

# Operational Boundaries

## External Actions on My Behalf

[Rules for anything an agent sends, posts, schedules, or otherwise commits externally without you reviewing it first. Be specific about what needs approval and how — per-message, per-batch, verbal-ok-counts, etc.]

## Domain-Specific Verification

[Optional. If your field has hard rules about fabrication, citation, or verification — legal, clinical, financial, technical, or otherwise — put them here. Leave this section out entirely if it doesn't apply.]

## Sources and Uncertainty

[How agents should signal what they know vs. infer vs. need to check. Note any situations where guessing is worse than saying "I don't know."]

## Continuity Across Turns

[What happens when you correct an agent's behavior mid-conversation — is it a one-turn fix or a standing rule? How should an agent recover if it's lost track of earlier instructions?]

## Edge Cases

[What an agent should do when a request would violate one of these rules, when two rules conflict, or when a rule seems wrong for the current situation. Default: surface the conflict, don't silently decide.]
```
