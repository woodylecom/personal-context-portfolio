# Wiring: Use Your Portfolio in Meta Muse

## What This Does

Meta Muse (the assistant in the Meta AI app) keeps persistent context about you in markdown files rather than in a custom-instructions box. Your portfolio is already markdown, so the job is mostly sorting: which files describe *you*, and which describe *how the assistant should work with you*. [`tools/export_muse.py`](../tools/export_muse.py) does that sorting automatically and produces two files ready to paste in.

## How Muse Holds Context — and How Sure We Are

Last checked 2026-10-04. Muse changes quickly; re-check these in your own app before relying on them.

| Claim | Source | Confidence |
|---|---|---|
| Muse remembers what you share in chats, patterns from your use, Connector context, and a "file-based memory system"; you can set name, time zone, interests, preferences, tone and communication style. | [Meta Help Center](https://www.meta.com/help/artificial-intelligence/995796179982326/) | High — official, though only read via search excerpt |
| Settings → Data Controls → **Import memory** brings in history from another AI assistant. | Meta Help Center (same page) | High — official |
| There's no custom-instructions box. Facts about you live in an editable **`Memory.md`** (Assistant → Identity → Memory); behavior rules live in an editable **`Soul.md`**. | Third-party guides: [agent-tune](https://agent-tune.com/guides/muse-personality), [aiagentslibrary](https://www.aiagentslibrary.com/blog/how-to-use-meta-muse/) | Medium — not confirmed by Meta; verify the menu path |
| No published length limit for `Soul.md`; example rule bodies run ~1,200–2,900 characters. | agent-tune (third-party) | Low-medium — the exporter's size budgets are guesses built on this |

If your app turns out not to have editable `Memory.md`/`Soul.md` files, the same two exported files still work: paste `Soul.md` into whatever personality or instructions setting you do have, and either paste `Memory.md` into memory or share it in a chat and ask Muse to remember it.

## Which Files Go Where

| Muse file | Portfolio files (in this order) | Why |
|---|---|---|
| `Memory.md` — facts about you | `identity`, `role-and-responsibilities`, `current-state`, `current-projects`, `goals-and-priorities`, `tools-and-systems`, `domain-knowledge`, `unknowns` | Descriptive context. `unknowns` stops Muse from filling gaps with guesses. |
| `Soul.md` — how to work with you | `preferences-and-constraints`, `operational-boundaries`, `communication-style`, `voice-anti-examples`, `personal-use` | Rules and voice — things that should shape every reply. |
| Opt-in (`--include`) → `Memory.md` | `team-and-relationships`, `decision-log` | Most third-party detail in the kit. Choose a redaction tier first (see [`team-and-relationships.md`](../templates/team-and-relationships.md)); roles-only is the safe default for anything stored with a third party. |

Only `identity.md` and `preferences-and-constraints.md` are required — the [minimum load](../LOAD-PROTOCOL.md). Anything else missing is skipped.

## Step by Step

1. **Fill out your portfolio somewhere private.** Not in a public fork of this kit — see [`templates/personal-use.md`](../templates/personal-use.md) on why a `.gitignore` entry isn't a redaction strategy.
2. **Run the exporter** from the kit folder:
   ```
   python tools/export_muse.py path/to/my-portfolio --out path/to/private/muse-export
   ```
   Add `--include team-and-relationships decision-log` if you want those in, and `--strict` if you want any warning to stop the run.
3. **Read the warnings.** The exporter flags:
   - blank templates it skipped,
   - stale files (`current-state.md` older than 10 days; other `evolving` files older than 30 — see [`MAINTENANCE.md`](../MAINTENANCE.md)),
   - lines that look like minors, medical, contact or government-ID details (heuristic — it prints file and line, never the text),
   - dates written inside the text that are more than 60 days old,
   - outputs over the soft size budget (`--memory-budget`, `--soul-budget`; defaults 8,000 and 4,000 characters).
   Fix the *source* file, then re-run. Don't hand-edit the output — the next export will overwrite it.
4. **Read both output files yourself** before they leave your machine. The redaction check is a safety net, not a guarantee.
5. **Paste into Muse.** Open Assistant → Identity → Memory and replace the contents of `Memory.md`; do the same for `Soul.md`. Keep a copy of whatever Muse had there first.
6. **Test it.** Ask Muse to do something it would get wrong without context — draft an email in your voice, plan your week around your hard constraints. Compare against a fresh, context-free chat.

## Keeping Things Out of the Export

Some passages belong in your portfolio but not with a third party — candid notes about a manager, staffing detail, local file paths. Wrap them so local tools still see them but the export leaves them out:

```
<!-- export:omit -->
Anything here stays in the portfolio and never reaches Memory.md or Soul.md.
<!-- /export:omit -->
```

Each marker goes on its own line. An unclosed block or a marker in the middle of a line is an error, and the exporter writes nothing until it's fixed. Unfilled template placeholders (`*[fill in: ...]*`) are dropped automatically, and links to other portfolio files become plain text.

Omitting is not updating: wrapping a stale section hides it, but the facts around it still need to be current.

## Keeping It Accurate

- **The portfolio is the source of truth; Muse is a copy.** Muse also writes its own memories from conversations and Connectors. When it learns something new about you, update the portfolio file and re-export rather than letting the two drift.
- **Re-export on the portfolio's cadence** — weekly if you rely on `current-state.md` / `current-projects.md`, otherwise after any real change.
- **Only bump `updated` after reviewing the whole file.** A one-line edit that refreshes the stamp makes every older fact in that file look current. The exporter also warns about dates written inside the text ("as of 2026-04-22", or a date cell in a table) that are more than 60 days old, whatever the stamp says.
- **Dates survive the paste.** Frontmatter doesn't, so the exporter turns each file's `updated`/`stability` into a visible "As of …" line, and `Soul.md` tells Muse that the conversation beats a stale file — and to say so, rather than silently work around it (the [conflict rule](../MAINTENANCE.md)).

## Tips

- Whatever goes into Muse is stored by Meta. Apply the strictest redaction tier you'd be comfortable with in a shared document, and never include anything on the minors never-include list.
- If you're over budget, trim the source files rather than raising the budget. Agents do better with a dense page than a sprawling five.
- The `Soul.md` output is in your voice ("I", "my") with a short preamble telling Muse those lines describe the person it's talking to — no third-person conversion needed (see [`CONVENTIONS.md`](../CONVENTIONS.md)).
