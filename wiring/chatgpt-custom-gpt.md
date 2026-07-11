# Wiring: Use Your Portfolio in ChatGPT / a Custom GPT

## What This Does

ChatGPT gives you two different places to add context, with two very different size budgets:

1. **Custom Instructions** — always-active, applies to every new chat, but character-limited (a few thousand characters, split across two fields).
2. **Custom GPT knowledge files** — uploaded documents attached to a specific Custom GPT, with much more room (closer to Claude Projects — see [`claude-projects.md`](claude-projects.md)).

Which one you use changes how much of the portfolio you can realistically include.

## Option 1: Custom Instructions (Character-Limited)

You cannot fit ten portfolio files into Custom Instructions. Don't try — you'll get truncated, and truncation happens silently mid-file, which is worse than deliberately picking a subset.

**Recommended subset: `identity.md` + `communication-style.md`.** These two cover the highest-value context in the smallest space — who the person is, and how they want things written. That combination alone fixes the two most common failure modes of generic AI output: wrong assumptions about the person, and a tone/voice mismatch.

Paste a condensed version of both files into the "What would you like ChatGPT to know about you?" field, and add instruction language to the "How would you like ChatGPT to respond?" field:

```
[condensed identity.md — trim to the highest-signal 3-5 lines]
[condensed communication-style.md — trim to the highest-signal 3-5 lines]
```

```
Match the communication style described above in every response. Don't reference this context
explicitly unless I ask — just use it.
```

If you have room left after those two, `preferences-and-constraints.md` is the next highest-value addition (hard rules an agent should never violate).

## Option 2: Custom GPT Knowledge Files (More Room)

If you're building a Custom GPT rather than just setting Custom Instructions, you get file uploads with a much larger budget — similar to the Claude Projects approach.

1. Create a Custom GPT (or edit an existing one).
2. Upload portfolio files to its Knowledge section — same file-selection logic as [`claude-projects.md`](claude-projects.md): match the files to the GPT's purpose rather than uploading all ten by default.
3. Add instructions in the GPT's configuration telling it how to use the uploaded files (e.g. "You have access to my personal context portfolio in your knowledge files. Use it to inform responses; don't narrate what you're reading unless asked.").

This is the better option if you want more than the two-file Custom Instructions subset, or if you're building a GPT for a specific recurring task (a meeting-prep GPT, a writing-assistant GPT) rather than a general assistant.

## Tips

- Custom Instructions apply to *every* chat in your account. A general-purpose subset (identity + communication style) is the right default there — save task-specific combinations (team context, project context) for a Custom GPT built for that task.
- Trim aggressively. A condensed 3-5 line version of `identity.md` that fits the character budget beats a truncated dump of the full file.
- When your portfolio changes, Custom Instructions won't update themselves — you pasted static text. Re-paste after material changes, the same way you'd refresh a Claude Projects upload.
- If you outgrow the character limit and find yourself fighting to trim further, that's the signal to move to a Custom GPT with knowledge files instead of squeezing more into Custom Instructions.
