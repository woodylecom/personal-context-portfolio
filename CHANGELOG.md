# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added

- `LICENSE` (MIT) to back up the license claim already in `README.md`.
- `.gitignore` covering common OS, editor, and tooling artifacts.
- This changelog.
- Four optional-module templates backported and generalized from the live reference portfolio this kit's author uses day to day: `templates/unknowns.md`, `templates/voice-anti-examples.md`, `templates/operational-boundaries.md`, `templates/current-state.md`. Each ships its own interview protocol and output structure, same as the core ten.
- `templates/_frontmatter.md` — the `updated` / `stability` / `scope` convention, opt-in per file, used by the four optional modules and demonstrated across the `knowledge-worker` example set.
- `LOAD-PROTOCOL.md` — minimum load (identity + preferences-and-constraints + optional `operational-boundaries` + optional `unknowns`) plus task-based additional loads, mirroring the pattern this repo's own author uses in their workspace `AGENTS.md`.
- `tools/validate.py` — recursively checks any `.md` file with a frontmatter block for well-formed `updated`/`stability`/`scope`, and checks local `.md` links resolve. Frontmatter-less files are not an error; frontmatter is opt-in kit-wide.
- `MAINTENANCE.md` — update cadence by file type, the "stale is worse than none" rule, and the conflict rule (the current conversation wins over a file; flag the file, don't silently rewrite it).
- `CONVENTIONS.md` — short kit-wide voice note (first-person default; third-person as an optional variant for system-prompt injection) plus pointers to the redaction-tier and maintenance conventions.
- Redaction tiers (full names / initials / roles-only) documented in `templates/team-and-relationships.md`, with guidance on which tier fits a private, shared, or public fork.
- `wiring/cursor.md`, `wiring/claude-code.md`, `wiring/chatgpt-custom-gpt.md` — first-class wiring guides alongside the existing MCP/Claude Projects/OpenClaw/system-prompt/API-layer guides.
- A worked filesystem MCP server config example (Claude Desktop / Claude Code JSON) added to `wiring/mcp-resource.md`.
- Optional-module example stubs (`unknowns.md`, `voice-anti-examples.md`, `operational-boundaries.md`, `current-state.md`) added to all three personas under `examples/` (`knowledge-worker`, `executive`, `entrepreneur`), each short, first-person, and in that persona's established voice.
- A one-line redaction-tier note added to each persona's `team-and-relationships.md` example ("full names OK — private example pack; drop to initials/roles-only before using this as a template for a shared or public fork").
- `templates/personal-use.md` — a fifth optional module: maps the work-flavored core ten to personal/family use (per-file translation table), and sets hard minors-redaction rules — a never-include list (legal names, birth dates, school/team names, age+location combinations, medical/psychological details, custody specifics, likeness/account identifiers), generalize-instead patterns with before/after examples (relationship label + broad age band), household-level phrasing for safety-critical facts, and an assume-a-public-commit calibration ("a `.gitignore` entry is not a redaction strategy"). Ships its own interview protocol and output structure like the other modules; the produced file records household labels and standing rules agents must honor.
- Frontmatter (`updated`/`stability`/`scope`) stamped across the full `examples/knowledge-worker/` set (all ten core files plus the four new optional modules) as the canonical worked example of the convention — and, in a follow-up pass, across the `executive` and `entrepreneur` core files as well, so all three personas now demonstrate the convention end to end.

### Fixed

- `wiring/cursor.md` referenced "this workspace's own root `AGENTS.md`" — a leftover from the private workspace this kit was backported from. Now points at this kit's own [`LOAD-PROTOCOL.md`](LOAD-PROTOCOL.md) instead.
- Example-pack timeline coherence: quarter-based targets that contradicted the July 2026 `updated` dates on the same persona's files ("end of Q2" launch targets in `knowledge-worker`, "before Q3" hiring targets in `executive`, an "end of Q2" course launch in `entrepreneur`) replaced with explicit month/season targets so dates and content agree.
- The interviewer system prompt promised a "5-8 questions" interview per file while every per-file guide specifies 3-6; aligned to 3-6.
- `examples/entrepreneur/voice-anti-examples.md` used the same ✅ example in both "Openers" and "Tone by Audience → To clients"; the opener now has its own distinct line.

### Changed

- Removed the "Path 1: Use the Web App" option from `README.md` and `GETTING-STARTED.md`. No hosted interviewer exists yet, and the placeholder `[Link to app]` / `[app URL]` links were vaporware. DIY (fork the repo, work through `/templates`) is now the only documented path, with a one-line note that a hosted interviewer may return later.
- `README.md` repo structure tree now matches what's actually on disk — no more provisional `*` markers. Includes `MAINTENANCE.md`, `CONVENTIONS.md`, `LOAD-PROTOCOL.md`, the four optional templates, `tools/validate.py`, and the full `wiring/` guide list.
- `README.md` "Design Principles" gained two new principles (redact-before-share, maintained-not-archived) merged in from the privacy/maintenance work, and "What's In It" now points to the four optional modules.
- `README.md` and `GETTING-STARTED.md` wiring lists now name Cursor, Claude Code, and ChatGPT Custom GPT explicitly instead of only MCP / Claude Projects / OpenClaw.
- `GETTING-STARTED.md` tips gained a "redact before you share" tip pointing at the team-and-relationships redaction tiers.
- `MAINTENANCE.md`'s reference to `templates/_frontmatter.md` is no longer hedged with "if present" — the file exists as of this pass.
- `interview-protocol/agent-system-prompt.md` documents the core ten as the "exactly ten files" default and the four optional modules as a separate, skippable add-on pass — kept as-is through this merge; still useful for anyone using an AI build partner to fill out the kit even without the (dropped) hosted web app.
- Optional-module count is now five kit-wide: `README.md` (module list, repo tree, redact-before-share principle), `GETTING-STARTED.md` (redaction tip), `LOAD-PROTOCOL.md` (new task-table row for personal/family content; ten-plus-five is fifteen), `templates/_frontmatter.md`, the four existing modules' cross-references ("one of five"), and `interview-protocol/agent-system-prompt.md` (add-on pass now offers `personal-use.md` as Optional File 5 — and runs it *first* when a portfolio covers family life, since its redaction rules bind the other interviews).

### Decisions (Lead defaults, this pass)

- `LICENSE` copyright holder stays "Jason Woody" — this is a public template kit the author is publishing, not a place to genericize the copyright line.
- `MAINTENANCE.md`, `CONVENTIONS.md`, and `LOAD-PROTOCOL.md` stay at repo root rather than moving under `templates/` or a `docs/` folder — they're kit-wide conventions, not per-file templates.
- Frontmatter remains opt-in on produced files; the meta templates themselves (the files under `templates/`) don't need frontmatter stamped on them — they're instructions, not context to load.
- Kept `interview-protocol/agent-system-prompt.md` even though the hosted web app (Path 1) was dropped — it's still directly useful handed to a DIY build partner (Claude, ChatGPT, etc.), which is exactly the only path this kit documents now.

Further Unreleased entries land as future passes complete.
