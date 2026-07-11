# Wiring: Use Your Portfolio in Claude Code

## What This Does

Claude Code reads `CLAUDE.md` automatically at the start of a session — both a project-level `CLAUDE.md` in your repo and a user-level one at `~/.claude/CLAUDE.md`. By pointing `CLAUDE.md` at your portfolio, every Claude Code session starts with a path to your context, and you can tell Claude Code exactly which files to read and when.

This is a different mechanism from [Claude Projects](claude-projects.md): Projects attach static file uploads to a web/app conversation, while `CLAUDE.md` gives a coding agent a live pointer to files on disk that it can re-read any time they change.

## How It Works

1. Open (or create) `CLAUDE.md` — project-level if the context only matters for this repo, user-level (`~/.claude/CLAUDE.md`) if it should apply everywhere you use Claude Code.
2. Add a section that names where your portfolio lives and defines a minimum load plus task-based extras — this mirrors the [`LOAD-PROTOCOL.md`](../LOAD-PROTOCOL.md) pattern:

```markdown
## User Context

User profile, preferences, and working context live at `/path/to/context-portfolio`.
Treat as canonical; read it directly rather than duplicating content here.

### Minimum load (any task needing user context)
- `identity.md`
- `preferences-and-constraints.md`

### Task-based additional loads
- **Drafting content on the user's behalf:** + `communication-style.md`
- **Project-relevant work:** + `current-projects.md`
- **Work involving specific people:** + `team-and-relationships.md`
- **Decision support:** + `goals-and-priorities.md`, `decision-log.md`
```

3. Claude Code reads `CLAUDE.md` at session start, so it knows the pointer exists — but for a large portfolio, tell it explicitly to do the selective read at the top of a task ("read `identity.md` and `current-projects.md` before we start") rather than assuming it pulled every file unprompted.

## Selective Reads vs. Full Loads

Don't tell Claude Code to read all ten files on every session start — that's the same "don't paste everything" problem as system prompts, just with a live filesystem instead of a static paste. Instead:

- Keep the `CLAUDE.md` section as a **menu**, not a mandate: it documents what's available and when to reach for it.
- At the start of a specific task, ask for the selective read explicitly: "Before we do this, read `identity.md` and `preferences-and-constraints.md` from my context portfolio."
- For recurring workflows, add a project-specific slash command (`.claude/commands/`) that bakes in the right selective read for that workflow, so you're not re-typing the file list every time.

## Which Files for Which Work

- **Any task at all:** `identity.md`, `preferences-and-constraints.md` — cheap, high-value, catches hard constraints.
- **Implementation/planning work:** + `current-projects.md`, `role-and-responsibilities.md`.
- **Anything drafted in the user's voice** (commit messages, docs, comments meant to sound like the user): + `communication-style.md`.
- **Work involving specific people or teams:** + `team-and-relationships.md`.

## Tips

- If you're already using the filesystem MCP approach (see [`mcp-resource.md`](mcp-resource.md)), `CLAUDE.md` and MCP aren't competing — `CLAUDE.md` documents the pointer and the load pattern; MCP is one way Claude Code (or Claude Desktop) can actually fetch the files. You can use `CLAUDE.md`'s selective-read instructions with plain file reads too, no MCP required.
- Keep the portfolio's `updated` frontmatter current. A `CLAUDE.md` pointer to a stale file is worse than no pointer — Claude Code will read it and trust it.
- If a project's `CLAUDE.md` is already long, keep the user-context section short and link out to [`LOAD-PROTOCOL.md`](../LOAD-PROTOCOL.md) for the full minimum-load rationale rather than duplicating it inline.
