# Personal Context Portfolio

Every AI agent, tool, and system you use needs to know who you are. Right now, you re-explain yourself from scratch every time — your role, your projects, your preferences, your constraints. It's the most repetitive, highest-friction part of working with AI, and it gets exponentially worse as the number of agents in your life grows from one to ten to fifty.

The personal context portfolio fixes this. It's a structured set of markdown files that together represent you as a context package — something any agent, any tool, any AI system can ingest and immediately understand who it's working with.

It's not a resume. It's not a profile. It's an operating manual for any AI that works for you.

## What's In It

Ten files, each covering a different dimension of who you are and how you work:

| File | What It Captures |
|------|-----------------|
| `identity.md` | Who you are in one page — the file an agent reads if it can only read one |
| `role-and-responsibilities.md` | What your weeks actually look like, not what your job description says |
| `current-projects.md` | Active workstreams, status, priority, what done looks like |
| `team-and-relationships.md` | Key people, how you interact, what they need from you |
| `tools-and-systems.md` | Your stack, your setup, what connects to what |
| `communication-style.md` | How you write, how you want things written for you |
| `goals-and-priorities.md` | What you're optimizing for and what you're deliberately ignoring |
| `preferences-and-constraints.md` | Hard rules, strong opinions, things any agent should respect |
| `domain-knowledge.md` | What you know that a general-purpose AI doesn't |
| `decision-log.md` | How you make decisions, with real examples |

These ten are a complete, usable portfolio on their own. Four **optional modules** — `unknowns.md`, `voice-anti-examples.md`, `operational-boundaries.md`, `current-state.md` — add more precision once you want it; see [`LOAD-PROTOCOL.md`](LOAD-PROTOCOL.md) for what they cover and when to load them.

## Design Principles

**Markdown-first.** Every AI system on earth can read markdown. It's the universal interchange format for context. Not JSON, not PDFs, not databases. Markdown files that are human-readable AND machine-readable.

**Modular, not monolithic.** Not one giant "about me" file. Separate files for separate domains. An agent prepping your meetings doesn't need your full life story — it needs your calendar context, team roster, and meeting preferences. Modularity lets agents grab what's relevant.

**Living, not static.** This isn't a thing you write once. It's a thing you maintain — or better, that your agents help you maintain. Your projects file updates as projects change. Your priorities file shifts quarterly. The portfolio evolves with you.

**Portable across everything.** Works with Claude, works with ChatGPT, works with OpenClaw agents, works with whatever comes next. No vendor lock-in. It's just files.

**Redact before you share.** Decide your redaction tier — full names, initials, or roles-only — before you fill out `team-and-relationships.md`, and before you fork this into anything that isn't strictly private. See "Redaction Tiers" in [`templates/team-and-relationships.md`](templates/team-and-relationships.md).

**Maintained, not archived.** A portfolio you write once and never touch is worse than not having one — a stale file gets acted on with confidence instead of prompting a question. See [`MAINTENANCE.md`](MAINTENANCE.md) for update cadence and what to do when the conversation and a file disagree.

## Build Yours

Fork this repo and use the templates in `/templates`. Each template includes the interview questions your AI build partner should ask you, plus the output structure for the finished file. Hand any template to Claude or ChatGPT and say "let's do this one."

*A hosted interviewer that automates this whole process may return down the line. For now, this repo is the whole thing — DIY, no signup, no waiting.*

## After You Build It

The portfolio is raw material. What makes it powerful is wiring it into the systems you actually use. The `/wiring` directory has guides for exposing your portfolio as an MCP resource, and for using it in Cursor, Claude Code, Claude Projects, a Custom GPT, OpenClaw agents, plain system prompts, or a custom API layer. That's the real work — and it's on you. See [`GETTING-STARTED.md`](GETTING-STARTED.md) for the full list.

## Repo Structure

```
personal-context-portfolio/
├── README.md                    ← you are here
├── GETTING-STARTED.md           ← step-by-step guide
├── LICENSE                      ← MIT
├── CHANGELOG.md                 ← notable changes, by version
├── MAINTENANCE.md               ← update cadence + conflict rules
├── CONVENTIONS.md               ← voice + formatting decisions that apply kit-wide
├── LOAD-PROTOCOL.md             ← minimum load + task-based context for agents
├── templates/                   ← empty templates with interview protocols: the core ten (see
│                                   "What's In It" above) plus four optional modules
│                                   (unknowns.md, voice-anti-examples.md, operational-boundaries.md,
│                                   current-state.md) and _frontmatter.md, the updated/stability/
│                                   scope convention
├── tools/
│   └── validate.py              ← frontmatter + local-link validator
├── examples/                    ← filled-out examples for three personas
│   ├── knowledge-worker/          (canonical frontmatter example)
│   ├── executive/
│   └── entrepreneur/
├── wiring/                      ← guides for connecting your portfolio to AI tools
│   ├── mcp-resource.md            (worked filesystem MCP config)
│   ├── cursor.md
│   ├── claude-code.md
│   ├── claude-projects.md
│   ├── chatgpt-custom-gpt.md
│   ├── openclaw-agents.md
│   ├── system-prompt-patterns.md
│   └── api-layer.md
└── interview-protocol/
    └── agent-system-prompt.md   ← the full interviewer system prompt (core ten + optional add-on pass)
```

## License

MIT. See [`LICENSE`](LICENSE). Fork it, customize it, use it however you want.
