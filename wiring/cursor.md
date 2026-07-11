# Wiring: Use Your Portfolio in Cursor

## What This Does

Cursor reads project-level rule and instruction files automatically at the start of every session. By pointing those files at your portfolio, every chat and agent task in that project starts with Cursor already knowing your role, your projects, and how you like things done — without you re-pasting anything.

## How It Works

Cursor supports a few overlapping mechanisms. Use the one that matches how you already work.

**Option 1: A project rule that points at the portfolio**

Add a rule file (`.cursor/rules/context-portfolio.mdc` or your project's rules location) that tells Cursor where the portfolio lives and when to read from it:

```
When starting work that depends on who the user is (drafting content, planning, prioritizing,
or anything referencing "my role" / "my team" / "my preferences"), read the relevant files from
/path/to/context-portfolio before responding:
- identity.md and preferences-and-constraints.md for almost everything
- current-projects.md for planning or status work
- communication-style.md for anything you draft on the user's behalf
- team-and-relationships.md for anything involving specific people
```

Mark the rule "Always" if you want it live in every chat, or scope it to specific file globs/paths if you only want it active in certain kinds of work.

**Option 2: An `AGENTS.md` pointer pattern**

If your project already uses (or could use) an `AGENTS.md` control file, add a short section pointing at the portfolio and defining a minimum load — the same minimum-load pattern defined in [`LOAD-PROTOCOL.md`](../LOAD-PROTOCOL.md). For example:

```
## User Context

User profile, communication style, and working context live at `/path/to/context-portfolio`.
Minimum load for any task needing user context: `identity.md`, `preferences-and-constraints.md`.
Task-based extras: `current-projects.md` for project work, `team-and-relationships.md` for anything
involving specific people, `communication-style.md` for anything drafted on the user's behalf.
```

This scales better than a single rule file once you have several projects, because every project's `AGENTS.md` can point at the same shared portfolio without duplicating its content.

**Option 3: Ad hoc `@`-mention**

For a one-off task, just `@`-mention the specific portfolio file in your chat message (e.g. `@identity.md what would I think about this?`). No setup required — good for trying the portfolio out before committing to a standing rule.

## Which Files for Which Work

Same logic as the other wiring guides — don't load everything into every rule.

- **General coding/implementation work:** `identity.md`, `preferences-and-constraints.md` — mostly to catch hard constraints (tools you won't use, formats you don't want).
- **Planning or status work:** + `current-projects.md`, `goals-and-priorities.md`.
- **Anything you draft on the user's behalf** (docs, commit messages, PR descriptions in the user's voice): + `communication-style.md`.
- **Anything involving specific people:** + `team-and-relationships.md`.

## Tips

- If you manage several projects in Cursor, prefer the `AGENTS.md` pointer pattern (Option 2) over duplicating the same rule in every project — one source of truth, referenced everywhere.
- Keep the rule's instructions about *when* to read the portfolio, not just *where* it is. "Read `identity.md` before responding" is more useful than just listing a file path.
- If a rule is marked "Always," keep the file list short — it loads on every request, so bloating it slows things down and dilutes the context that matters.
- Update the portfolio files themselves, not the rule. The rule should point at the files, not duplicate their content, so updates propagate without touching Cursor config.
