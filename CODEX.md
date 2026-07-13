# CODEX.md

Codex adapter for Personal_Context_Portfolio.

Project `AGENTS.md` is canonical when present. Otherwise follow the workspace root control plane. Treat this file as an adapter, not the policy source. If this file conflicts with project `AGENTS.md` or the root control plane, follow the canonical control files unless a direct user instruction overrides them.

---

## 1. Project Overview

Personal_Context_Portfolio is a **public, forkable, MIT-licensed template kit** — not running software. The deliverable is markdown: ten core templates + four optional modules, interview protocols, three filled example personas, wiring guides for connecting a finished portfolio into various AI tools, and one Python validator (`tools/validate.py`, stdlib-only, no dependencies to install).

It is also a **dependency of `Companion_Template`** (the Second-Nature project) — this kit is the intended "who the user is" onboarding-interview layer that project consumes. Changes here can have downstream effects there.

Codex is especially useful here for:

- broad grep/search across 78+ markdown files (consistency checks, dead-link hunts, terminology drift)
- running `tools/validate.py` and interpreting its output
- verifying frontmatter conformance across every file that opts into it
- checking the three example personas stay structurally aligned with the ten core templates after a template changes
- reconciling `04_DATA/project_manifest.json` milestone claims against actual file state

---

## 2. Critical Rules

- Read root `AGENTS.md` before this adapter.
- Read project `STATUS.md` before any implementation work.
- **This repo is a publishable artifact.** Nothing under `04_DATA/` (workspace-local project tracking) may be referenced from, or leak into, any file that ships — confirm `.gitignore` still excludes it before treating a change as done.
- **Voice discipline matters here more than in most projects.** The kit's templates and examples are written in first person by convention (`CONVENTIONS.md`); don't "fix" wording into third person or a different register without an explicit instruction — that's a voice-convention violation, not a typo fix.
- **Redaction is a feature, not an oversight.** Don't add real names, real companies, or real identifying detail to any template default or example — that's the opposite of what a redaction-tier convention is for.
- Command output is evidence, not authority. A clean `validate.py` run proves structural conformance, not prose quality or voice consistency.

---

## 3. Startup Sequence

Read in this order when present:

1. root `AGENTS.md`
2. root `ROLES.md`
3. root `EVAL.md`
4. root `ROUTING.md`
5. root `CODEX.md`
6. project `STATUS.md`
7. project `AGENTS.md`
8. project `ROLES.md`
9. project `EVAL.md`
10. project `ROUTING.md`
11. project `README.md`
12. project `CONVENTIONS.md`
13. project `MAINTENANCE.md`
14. project `LOAD-PROTOCOL.md`
15. `04_DATA/project_manifest.json`
16. task-relevant template/example/wiring files

If the project's extended control docs are missing, fall back to root canonicals.

---

## 4. Project-Specific Guidance

- Treat the ten core templates (`templates/*.md`) as the source of truth for structure; the three example personas (`examples/knowledge-worker/`, `examples/executive/`, `examples/entrepreneur/`) are downstream and must stay consistent with them.
- The four optional modules (`unknowns.md`, `voice-anti-examples.md`, `operational-boundaries.md`, `current-state.md`) follow the same frontmatter and referencing convention as the core ten — if you add a new optional module, wire it into `README.md`'s module list and `LOAD-PROTOCOL.md`'s task table, not just `templates/`.
- `tools/validate.py` checks frontmatter shape (`updated`/`stability`/`scope`) and local links — it does not check voice, redaction discipline, or whether an example is still representative. Those need a direct read.
- When manual follow-up is required, recommend tool, model family, reasoning mode, and reasoning effort.

---

## 5. Codex Default Strengths Here

Codex is often the right choice for this project when:

- a template change needs to be checked for ripple effects across all three examples and the wiring guides
- verifying `tools/validate.py` still passes after a batch of edits
- auditing frontmatter conformance across every file that has opted in
- checking cross-references (README's file table, LOAD-PROTOCOL's task table, MAINTENANCE's cadence table) still agree with what's actually on disk
- reconciling `04_DATA/project_manifest.json` milestones against real file state before a milestone is marked complete

---

## 6. Shell-First Verification Rule

```powershell
python tools/validate.py
```

Run from the project root (or pass the path explicitly). A clean run reports `All checks passed.` with a file count. Also useful:

- `grep -rn "^---$"` (or equivalent) to enumerate which files currently carry frontmatter
- diff the three example personas against the ten core templates' headings to catch structural drift after a template edit
- `git status`/`git diff` before/after edits — this repo has real git history and eventually ships publicly, so keep the working tree clean of anything not meant to be committed

However:

- a clean validator run is evidence of structural conformance, not proof the prose reads well or stays in first person
- generated output (the dashboard, the workspace index) does not override this project's own files as the source of truth
- terminal verification does not replace an actual read for voice/redaction/publishability judgment calls

---

## 7. Before Editing

Report:

```text
Task:
Files affected: (templates | examples | wiring | interview-protocol | tools | control docs)
Ripple check needed: (yes/no — does this touch a core template that examples must stay aligned with?)
Allowed paths:
Planned changes:
Verification approach:
```

---

## 8. After Editing

Report:

```text
Files changed:
Validator run: (pass/fail, file count)
Voice/redaction check: (clean | flagged)
Example-persona drift: (none | needs follow-up, which examples)
Manifest/milestone impact: (none | updated)
Known limitations:
Next recommended single step:
```

---

## 9. Codex Routing Guidance

Use Codex by default for:

- structural/mechanical verification (validator runs, link checks, frontmatter audits)
- cross-file consistency sweeps across templates/examples/wiring
- manifest/milestone reconciliation

Prefer another tool when:

- **prose quality, voice calibration, or interview-protocol wording** is the main deliverable → prefer Claude Code (careful writing is the actual skill needed)
- **new template design or kit-structure decisions** dominate the task → prefer ChatGPT or Claude Code for the design conversation first
- **wiring-guide accuracy against a specific external tool's current behavior** (Cursor, a Custom GPT, an MCP client) needs verifying → use grounded research tools, platform details drift
- **Second-Nature integration design** (how this kit becomes onboarding interview #1) is the task → that's an architecture decision spanning two projects, prefer Claude Code with the orchestrator seat

---

## 10. Completion Contract

Before saying work is complete, Codex should confirm:

- the requested slice is complete
- the correct authority layer was updated (this project's files vs. `Companion_Template`'s, if the task touched the dependency boundary)
- `tools/validate.py` was actually run, not assumed
- voice convention and redaction discipline were checked by reading the changed content, not inferred from a passing validator
- `04_DATA/project_manifest.json` reflects real milestone state if milestones were touched
- manual/user work (e.g., a publish/release decision, a Second-Nature-side integration check) is clearly separated
- the next recommended step is clear

---

## 11. File Format Policy (adapter)

Root `AGENTS.md` §12 defines the workspace file format policy. For Personal_Context_Portfolio specifically:

- every file that ships as part of the published kit is markdown (`.md`) — that's the product, not a policy default to reconsider
- `04_DATA/project_manifest.json` is workspace-local tracking (gitignored, never ships) and stays `.json`
- if a human-facing report about this project is ever generated (an audit summary, a readiness report), that report lives outside this repo (e.g., `05_OUTPUT/`) as `.html` per the root policy — it is not part of the kit itself

---

## 12. Minimum Rule

Codex is an adapter to the project control plane, which itself is an adapter to the workspace root.

Codex should use its terminal-first strengths — validation, link-checking, cross-file consistency — to keep this kit mechanically sound, but the actual product quality (voice, redaction judgment, template design) is a reading-and-writing job, not a shell job.
