# EVAL.md

Project-specific completion and acceptance gate for Personal_Context_Portfolio.

This file inherits the generic completion checks defined in the workspace root `EVAL.md`. Apply those workspace-level checks first (scope, authority, boundaries, drift, state sync, verification, adapters, human handoff, final output). The sections below add project-specific quality criteria for this project's actual deliverable: a **public, forkable, MIT-licensed template kit** — markdown templates, interview protocols, example personas, wiring guides, and a validator — not running software.

---

## 1. Quick-Reference Checklist

- [ ] **Workspace gate** — root `EVAL.md` checklist applied first
- [ ] **Validator green** — `python tools/validate.py` run against the repo, all checks pass or failures explained
- [ ] **Frontmatter convention** — any file carrying frontmatter matches `templates/_frontmatter.md` (`updated`/`stability`/`scope`, valid values)
- [ ] **Voice convention** — first-person by default per `CONVENTIONS.md`; no mixed voice within one file/example set
- [ ] **Redaction discipline** — `team-and-relationships.md` and its examples respect the stated redaction tier; no real third-party PII leaked into template defaults
- [ ] **Portability** — no vendor lock-in, no format creep away from plain markdown
- [ ] **04_DATA stays out** — workspace-tracking dir (`04_DATA/`) never referenced from published files, confirmed still gitignored
- [ ] **Examples stay representative** — if a template changed, the three filled examples (`knowledge-worker`, `executive`, `entrepreneur`) still reflect its current structure
- [ ] **Local links resolve** — no dead relative links between README/templates/wiring/examples
- [ ] **Publishable-quality bar** — a stranger could clone the repo and successfully build their own portfolio using only `GETTING-STARTED.md` + `README.md`
- [ ] **Milestone accuracy** — `04_DATA/project_manifest.json` milestones reflect real completion, not aspirational
- [ ] **Second-Nature dependency** — if this kit is the intended onboarding-interview layer for `Companion_Template`, changes here that would break that integration are flagged

---

## 2. Quality Rubric

| Category | Target |
| --- | --- |
| Portability | Plain markdown only; works unmodified in Claude, ChatGPT, MCP, or a raw system prompt |
| Modularity | Each of the ten core files + five optional modules stays independently loadable — no file assumes another was already read |
| Voice consistency | First person by default (per `CONVENTIONS.md`); any third-person fork is consistent within itself, not mixed |
| Redaction safety | Team/relationship content defaults to a stated redaction tier; nothing in a shipped template implies real names are required |
| Staleness signaling | Frontmatter-bearing files carry a truthful `updated` date and correct `stability` tier — never `stable` on something that's actually `draft` |
| Publishability | `GETTING-STARTED.md` alone is sufficient for a first-time user with no other context |
| Validator coverage | `tools/validate.py` actually catches the things this rubric cares about (frontmatter shape, local links) — extend it rather than working around it if it can't |

---

## 3. Verification — How to Actually Check This

```powershell
python "01_PROJECTS/Personal_Context_Portfolio/tools/validate.py"
```

Run from anywhere; it takes the repo path as an argument or defaults to its own parent. A clean run reports `All checks passed.` with the file count. Treat a validator failure as blocking — fix the file, don't route around the check.

For voice/redaction/frontmatter-semantics issues the validator can't catch mechanically (does this example actually read as first person throughout, does this redaction example actually look safe to publish), spot-check by reading the changed file directly — the validator checks *shape*, not *content quality*.

---

## 4. Milestone Acceptance

Pull current milestone state from `04_DATA/project_manifest.json` rather than duplicating it here (state sync — don't let two files disagree). At minimum, before marking a milestone complete:

- **M2 (Personal-use mapping + minors redaction guidance)** — new/updated files pass the validator; minors-redaction guidance is concrete enough that a parent building a kid's portfolio knows exactly what to omit or generalize, not just "be careful."
- **M3 (Everyday example persona)** — the new example is structurally consistent with the existing three (`knowledge-worker`, `executive`, `entrepreneur`) and actually demonstrates the personal-use additions from M2/M4, not just a fourth professional persona.
- **M4 (Personal-life optional modules)** — new modules follow the existing optional-module pattern (frontmatter per `_frontmatter.md`, referenced from `LOAD-PROTOCOL.md`, referenced from `README.md`'s module list) rather than being bolted on inconsistently.
- **M5 (Second-Nature integration)** — verify against `Companion_Template`'s actual onboarding flow, not just this repo in isolation; a claim of "wired in" requires checking the consuming side, not just this project's own files.

---

## 5. Pass / Return Standard

A slice should pass only if:

- the relevant workspace `EVAL.md` checks pass first
- `tools/validate.py` passes clean (or a failure is explained and tracked, not silently ignored)
- the change doesn't introduce mixed voice, broken redaction discipline, or vendor lock-in
- `04_DATA/project_manifest.json` and, if material, the workspace index reflect the new state
- for milestone work, the relevant Section 4 criteria are met

Return for revision if any of these are materially false, or if a change to the core ten templates isn't reflected in the three example personas.
