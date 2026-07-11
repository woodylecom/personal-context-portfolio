# Conventions

Small formatting and voice decisions that apply across the whole kit. Kept short on purpose — anything needing more than a paragraph belongs in its own doc.

## Voice: First-Person by Default

Every template and example in this kit is written in the **first person** ("I lead a team of...", "My manager needs..."). That's the default because most people building their own portfolio — for a Claude Project, ChatGPT custom instructions, or an MCP resource they read themselves — are describing themselves, and first person is the fastest, most natural path from template to filled-out file.

**Third person is an optional variant**, useful mainly for one case: injecting the portfolio into a system prompt where the model needs to talk *about* the user in the third person before addressing them directly. In that setup, files read like "Jason leads a team of..." and the system prompt instructs the model to treat the named person and "the user" as the same person, replying in second person. See `wiring/system-prompt-patterns.md` for the injection pattern that motivates this.

If you switch to third person, do it consistently across every file in the portfolio — don't mix voices within one set. Pick one at the start; converting later means touching every file you've already written.

## Related Conventions

- **Redaction tiers** (how much identifying detail to include for people you mention) — see the "Redaction Tiers" section in `templates/team-and-relationships.md`.
- **Update cadence and conflict handling** — see `MAINTENANCE.md`.
