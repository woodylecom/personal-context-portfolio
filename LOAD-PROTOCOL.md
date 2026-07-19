# Load Protocol

How an agent should decide which files to read before starting a task — so you're not dumping the whole portfolio into every context window, and an agent isn't working from too little.

## Minimum Load
*(any task needing basic context about you)*

- `identity.md` — who you are
- `preferences-and-constraints.md` — hard rules and strong preferences
- `operational-boundaries.md` — what agents must never do without approval *(optional module — see [`templates/operational-boundaries.md`](templates/operational-boundaries.md))*
- `unknowns.md` — what's genuinely uncertain or deliberately excluded *(optional module — see [`templates/unknowns.md`](templates/unknowns.md))*

If you haven't built the optional modules yet, minimum load is just `identity.md` + `preferences-and-constraints.md`.

## Task-Based Additional Loads

| Task type | Add |
|---|---|
| Content on your behalf (emails, drafts, messages) | `communication-style.md`, `voice-anti-examples.md` *(optional module)* |
| Project-relevant work | `current-projects.md` |
| Drafting for or about other people | `team-and-relationships.md` |
| Decision support | `goals-and-priorities.md`, `decision-log.md` |
| Domain-specific work | `domain-knowledge.md` |
| Anything time-sensitive | `current-state.md` *(optional module — check `updated`, distrust if more than 10 days stale)* |
| Personal / family content (anything mentioning household members or minors) | `personal-use.md` *(optional module — household labels + hard redaction rules for minors)* |
| Out-of-scope / gap check | `unknowns.md` *(optional module)* |

## Why This Exists

The core ten files plus five optional modules is fifteen files. Most tasks need three or four of them, not all fifteen. This protocol exists so you — or an agent deciding this on your behalf — can load the minimum that's actually useful, instead of defaulting to "load everything" or "load whatever's top of mind."

See [`templates/_frontmatter.md`](templates/_frontmatter.md) for how `stability` and `updated` should factor into how much an agent trusts what it loads.

## Updating This File

If you add your own custom files beyond the fifteen in this kit, add a row here rather than letting agents guess which of your files are relevant to which task.
