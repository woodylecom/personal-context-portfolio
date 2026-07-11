# Maintenance

Your portfolio is only useful if it's accurate. A stale file that confidently tells an agent the wrong thing is worse than no file at all — a missing file makes an agent ask a question; a wrong one makes it act on bad information without asking.

## Update Cadence

| File | Suggested cadence | Why |
|------|-------------------|-----|
| `current-projects.md` (and any `current-state`-style optional module) | Weekly, or whenever a project starts/ends/changes status | The fastest-moving file in the kit. Stale project status is the single most common way agents give confidently wrong help. |
| `team-and-relationships.md` | As relationships change — new hire, role change, reporting change | Not calendar-driven. Update when the org chart or dynamic actually changes, not on a schedule. |
| `goals-and-priorities.md` | Quarterly, or whatever cadence your org resets priorities | Goals shift slower than projects, but they do shift. |
| `tools-and-systems.md` | When your stack changes | Low churn for most people — update opportunistically. |
| `domain-knowledge.md` | Rare | Durable, structural knowledge. Update when your domain itself changes, not on a schedule. |
| `identity.md` / `role-and-responsibilities.md` | Rare | Structural files. Re-check after a role change, promotion, or major shift in what you do — not on a calendar. |
| `communication-style.md` / `preferences-and-constraints.md` | Rare, but worth a re-read after strong feedback (e.g., "your AI drafts still sound off") | Small drift accumulates; a periodic sanity check catches it. |
| `decision-log.md` | Append-only, whenever you make a decision worth remembering | Add entries — don't rewrite old ones. The log's value is the history. |

**Rule of thumb:** if a file is time-sensitive (active projects, current state), staleness is disqualifying — treat it as untrustworthy past its expected cadence. If a file is structural (identity, domain knowledge), staleness is more forgiving, but still check it after any real change.

## Stale Is Worse Than None

A missing file prompts a question. A stale file gets acted on. If you can't keep a file current, do one of these instead of leaving it silently wrong:

- Delete it and let the agent ask, or
- Add a note at the top flagging what's no longer trustworthy (e.g., "Team roster below is from Q1 and hasn't been reconfirmed").

If a file uses frontmatter (see [`templates/_frontmatter.md`](templates/_frontmatter.md) for the convention — it's opt-in per file, not mandatory kit-wide), the `updated:` date gives you and any agent reading the file a fast staleness check — treat a time-sensitive file with suspicion once it's more than ~10 days past due for its cadence.

## Conflict Rule

Sometimes the portfolio and the live conversation disagree — you tell an agent something that contradicts what a file says.

**The conversation wins.** What you're saying right now is more current than any file. But the contradiction shouldn't disappear silently:

1. Trust what the user says in the current conversation over what a file claims.
2. Flag the file — note that `[filename]` looks out of date on `[topic]` and should be updated.
3. Don't silently rewrite the file mid-conversation. Flag it, then let the user decide when and how to update it. That keeps the portfolio's edit history intentional instead of quietly rewritten by a side comment.

This is the same thing you'd want from a human assistant: believe you over their notes, but say something if the notes are wrong instead of just working around it forever.
