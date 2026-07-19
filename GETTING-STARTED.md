# Getting Started

Fork this repo and work through the templates with your own AI build partner (Claude, ChatGPT, or whatever you use). That's it — there's one path, and it's DIY.

*A hosted interviewer that automates this whole process (sign in, answer questions, download a finished portfolio) may return down the line. For now, this repo is the whole thing.*

---

## Building Your Portfolio

1. Fork or clone this repo.
2. Open any template file from `/templates`.
3. Copy the entire file and paste it to your AI build partner.
4. Say "let's do this one."
5. Your build partner will read the interview protocol embedded in the template and start asking you questions.
6. When it has enough, it'll draft the file. Read the draft and tell it what's wrong.
7. Save the final version. Move to the next template.

**Recommended order:** Start with `identity.md` and `role-and-responsibilities.md`. Everything else builds on those two. After that, the order matters less — go with whatever feels most relevant to your work right now.

**Suggested full sequence:**

1. `identity.md`
2. `role-and-responsibilities.md`
3. `current-projects.md`
4. `team-and-relationships.md`
5. `tools-and-systems.md`
6. `communication-style.md`
7. `goals-and-priorities.md`
8. `preferences-and-constraints.md`
9. `domain-knowledge.md`
10. `decision-log.md`

---

## After You Build It

Your portfolio is a set of markdown files. That's the point — they're portable. But they don't do anything until you wire them into the tools you actually use.

The `/wiring` directory has guides for:

- Exposing your portfolio as an MCP resource ([`mcp-resource.md`](wiring/mcp-resource.md), with a worked filesystem config)
- Using it in [Cursor](wiring/cursor.md) — rules or an `AGENTS.md` pointer pattern
- Using it in [Claude Code](wiring/claude-code.md) — `CLAUDE.md` + selective reads
- Using it in [Claude Projects](wiring/claude-projects.md)
- Using it in a [ChatGPT Custom GPT](wiring/chatgpt-custom-gpt.md) — including the character-limited Custom Instructions case
- Connecting it to [OpenClaw agents](wiring/openclaw-agents.md)
- Copy-paste [system prompt patterns](wiring/system-prompt-patterns.md) for anything else
- Building an [API layer](wiring/api-layer.md), if you need it (most people don't)

This is the part that turns your portfolio from "a nice set of documents" into actual infrastructure. Start with whatever tool you use most.

---

## Tips

- **Redact before you share.** Before you fill out `team-and-relationships.md` — or fork this anywhere that isn't strictly private — decide your redaction tier (full names, initials, or roles-only). See "Redaction Tiers" in [`templates/team-and-relationships.md`](templates/team-and-relationships.md). If your portfolio describes a minor, the tiers aren't enough — see [`templates/personal-use.md`](templates/personal-use.md) for what never goes in at all.
- **Be specific, not aspirational.** The portfolio should describe how you actually work, not how you wish you worked. Your agents need ground truth.
- **Don't skip the reaction pass.** When your build partner drafts a file, read it and find what's wrong. The corrections are where the real signal is. A rubber-stamped draft is a mediocre file.
- **Short is better than long.** A good context file is one page, not five. Agents perform better with dense, high-signal context than with sprawling documents.
- **Update regularly.** Projects change, priorities shift, you learn new tools. A portfolio that's six months stale is worse than no portfolio — it gives your agents confident but wrong context.
