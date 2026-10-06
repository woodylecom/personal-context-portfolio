#!/usr/bin/env python3
"""
Personal Context Portfolio Kit — Meta Muse exporter.

Builds the two markdown files Meta Muse reportedly reads as persistent
context, from a FILLED-OUT portfolio (not the blank templates in this kit):

  Memory.md  — facts about you (who you are, what you're working on, your
               tools, goals, domain knowledge, what's deliberately unknown).
  Soul.md    — how the assistant should behave with you (communication
               style, hard rules, voice anti-examples, operational
               boundaries, household redaction rules).

See wiring/meta-muse.md for where these go in the Muse app and how the
file split was chosen.

What the export does, per source file:
  0. Matches files by name, with or without a numeric sort prefix
     (identity.md, 01-identity.md and 06a-voice-anti-examples.md all work).
     Files it doesn't recognize are listed as not exported.
  1. Skips files that are still blank templates (they contain an
     "Interview Protocol" section) — those are questions, not context.
  2. Strips the YAML frontmatter, but keeps its information as a visible
     "As of <updated> (<stability>)" line, because a pasted file loses its
     frontmatter and Muse would otherwise have no staleness signal.
  3. Demotes headings one level so each file becomes a section of the
     combined output.
  4. Warns when a time-sensitive file is stale (current-state.md older than
     10 days; any other "evolving" file older than 30 days), per
     MAINTENANCE.md.
  5. Runs heuristic redaction checks (minors details, medical details,
     contact and government identifiers) per templates/personal-use.md.
     These are a safety net, not a guarantee — read the output before
     pasting it anywhere. Findings print file:line and the rule, never the
     matched text.
  6. Reports each output's size against a soft character budget. Meta does
     not publish a limit; the defaults are conservative guesses — see
     wiring/meta-muse.md.
  7. Leaves out anything between <!-- export:omit --> and
     <!-- /export:omit --> (each marker on its own line), so a passage can
     stay in your portfolio for local tools without going to Muse. An
     unclosed or stray marker is an error and nothing is written.
  8. Drops unfilled template placeholders (*[fill in: ...]*) and turns
     links to other portfolio files or local paths into plain text, since
     neither means anything once pasted into Muse.
  9. Warns about dates written inside the text ("as of 2026-04-22", or a
     date cell in a table) that are much older than the export. A file's
     `updated` stamp can be refreshed for a one-line edit while older facts
     sit underneath it; this catches the facts the stamp would hide.

Usage:
    python tools/export_muse.py PORTFOLIO_DIR [--out DIR] [--as-of YYYY-MM-DD]
        [--include team-and-relationships decision-log]
        [--memory-budget N] [--soul-budget N] [--strict]

    PORTFOLIO_DIR  folder holding your filled-out portfolio files
    --out          where to write Memory.md and Soul.md (default: ./muse-export)
    --include      opt-in extras (team-and-relationships, decision-log) —
                   off by default because they carry the most third-party
                   detail; add them only after choosing a redaction tier
    --strict       treat warnings (stale, redaction, over budget) as failures

Exit code: 0 on success, 1 on any error (or any warning with --strict).
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date, datetime
from pathlib import Path

# Source file -> output, in the order sections appear. Order follows
# LOAD-PROTOCOL.md: minimum-load files first.
MEMORY_FILES = [
    "identity",
    "role-and-responsibilities",
    "current-state",
    "current-projects",
    "goals-and-priorities",
    "tools-and-systems",
    "domain-knowledge",
    "unknowns",
]
SOUL_FILES = [
    "preferences-and-constraints",
    "operational-boundaries",
    "communication-style",
    "voice-anti-examples",
    "personal-use",
]
# Opt-in only (see --include). Both land in Memory.md.
OPTIONAL_MEMORY_FILES = ["team-and-relationships", "decision-log"]

REQUIRED_FILES = {"identity", "preferences-and-constraints"}  # LOAD-PROTOCOL minimum load

DEFAULT_MEMORY_BUDGET = 8000
DEFAULT_SOUL_BUDGET = 4000

CURRENT_STATE_MAX_AGE_DAYS = 10  # templates/current-state.md staleness rule
EVOLVING_MAX_AGE_DAYS = 30
INTEXT_DATE_MAX_AGE_DAYS = 60

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
FIELD_RE = re.compile(r"^(\w+):\s*(.+?)\s*$", re.MULTILINE)
PREFIX_RE = re.compile(r"^\d+[a-z]?[-_]")
HEADING_RE = re.compile(r"^(#{1,5})(\s)", re.MULTILINE)
TEMPLATE_MARKER_RE = re.compile(r"^#+\s*Interview Protocol\b", re.MULTILINE | re.IGNORECASE)
OMIT_OPEN_RE = re.compile(r"^\s*<!--\s*export:omit\s*-->\s*$")
OMIT_CLOSE_RE = re.compile(r"^\s*<!--\s*/export:omit\s*-->\s*$")
OMIT_ANY_RE = re.compile(r"<!--\s*/?export:omit\s*-->")
PLACEHOLDER_RE = re.compile(r"\s*\*\[fill in:[^\]]*\]\*")
BARE_BULLET_RE = re.compile(r"^\s*(?:[-*]|\d+\.)\s*$")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
BLANK_RUN_RE = re.compile(r"\n{3,}")
# "as of 2026-04-22", "As of: 2026-04-22", or a table row ending in a date cell.
INTEXT_DATE_RE = re.compile(r"(?:\bas of:?\s*|\|\s*)(\d{4}-\d{2}-\d{2})(?=\s*(?:\||\)|,|\.|;|\s|$))", re.IGNORECASE)

# Heuristic redaction checks: (rule name, pattern). Kept deliberately
# narrow so warnings stay readable; they flag lines for a human to check.
REDACTION_RULES = [
    ("possible SSN", re.compile(r"\b\d{3}-\d{2}-\d{4}\b")),
    ("email address", re.compile(r"\b[\w.+-]+@[\w-]+\.[\w.-]+\b")),
    ("phone number", re.compile(r"(?<!\d)(?:\+?1[\s.-]?)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}(?!\d)")),
    ("date of birth", re.compile(r"\b(?:born|DOB|birthday)\b[^.\n]{0,20}\d", re.IGNORECASE)),
    ("exact child age", re.compile(r"\b(?:\d{1,2}[- ]year[- ]old|ages?\s+\d{1,2}\b|\(\d{1,2}\))", re.IGNORECASE)),
    ("school or program name", re.compile(
        r"\b[A-Z][\w'-]+\s+(?:Elementary|Middle School|High School|Academy|Daycare|Preschool|Montessori)\b")),
    ("medical detail", re.compile(
        r"\b(?:\d+\s?mg\b|ADHD|autis\w*|IEP\b|504 plan|diagnos(?:is|ed with)|prescription|medication|therap(?:y|ist))", re.IGNORECASE)),
    ("custody detail", re.compile(r"\bcustody\b", re.IGNORECASE)),
]

MEMORY_PREAMBLE = """\
# Memory

Facts about me, exported from my personal context portfolio on {as_of}.
Each section says when it was last confirmed. Treat anything marked
"draft", or flagged as stale, as a starting point to check with me — not
as settled fact.
"""

SOUL_PREAMBLE = """\
# Soul

How to work with me, exported from my personal context portfolio on
{as_of}. The sections below describe me, the person you're talking to —
whether a section says "I" or uses my name.

## Standing Rules for Using This Context

- Follow the hard rules and boundaries below in every reply, without exception.
- Use this context quietly. Don't recite it back to me unless I ask.
- If what I tell you in a conversation contradicts these files, the
  conversation wins — but tell me which section looks out of date instead
  of silently working around it, so I can fix the source.
- If something you need isn't covered, ask me rather than guess.
"""


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    return dict(FIELD_RE.findall(match.group(1))), text[match.end():]


def demote_headings(body: str) -> str:
    return HEADING_RE.sub(lambda m: "#" + m.group(1) + m.group(2), body)


def age_in_days(updated: str, as_of: date) -> int | None:
    try:
        return (as_of - datetime.strptime(updated, "%Y-%m-%d").date()).days
    except ValueError:
        return None


def blank_omitted(label: str, body: str, line_offset: int, errors: list[str]) -> str:
    """Blank every line inside an export:omit block, markers included.

    Lines are blanked rather than deleted so redaction findings, which run
    after this, still report the line number of the source file.
    """
    lines, inside, opened_at = body.split("\n"), False, 0
    for i, line in enumerate(lines):
        lineno = line_offset + 1 + i
        if OMIT_OPEN_RE.match(line):
            if inside:
                errors.append(f"{label}:{lineno}: export:omit opened again before line {opened_at}'s block closed")
            inside, opened_at = True, lineno
            lines[i] = ""
        elif OMIT_CLOSE_RE.match(line):
            if not inside:
                errors.append(f"{label}:{lineno}: /export:omit with no open block")
            inside = False
            lines[i] = ""
        elif OMIT_ANY_RE.search(line):
            errors.append(f"{label}:{lineno}: export:omit marker must be on a line of its own")
        elif inside:
            lines[i] = ""
    if inside:
        errors.append(f"{label}:{opened_at}: export:omit block never closed")
    return "\n".join(lines)


def localize(body: str) -> str:
    """Drop placeholders, unlink local references, collapse leftover blank runs."""
    def unlink(m: re.Match) -> str:
        target = m.group(2)
        return m.group(0) if target.startswith(("http://", "https://", "mailto:")) else m.group(1)

    out = []
    for line in body.split("\n"):
        had_placeholder = "*[fill in:" in line
        line = LINK_RE.sub(unlink, PLACEHOLDER_RE.sub("", line))
        if had_placeholder and (not line.strip() or BARE_BULLET_RE.match(line)):
            continue
        out.append(line.rstrip())
    return BLANK_RUN_RE.sub("\n\n", "\n".join(out))


def stale_intext_dates(label: str, body: str, line_offset: int, as_of: date) -> list[str]:
    """Flag in-text dates far older than the export, one warning per line."""
    findings = []
    for lineno, line in enumerate(body.splitlines(), start=line_offset + 1):
        ages = [age for d in INTEXT_DATE_RE.findall(line)
                if (age := age_in_days(d, as_of)) is not None and age > INTEXT_DATE_MAX_AGE_DAYS]
        if ages:
            findings.append(f"{label}:{lineno}: in-text date is {max(ages)} days old — reconfirm the fact, "
                            "whatever the file's 'updated' stamp says")
    return findings


def redaction_findings(name: str, body: str, line_offset: int) -> list[str]:
    findings = []
    for lineno, line in enumerate(body.splitlines(), start=line_offset + 1):
        for rule, pattern in REDACTION_RULES:
            if pattern.search(line):
                findings.append(f"{name}:{lineno}: {rule} — check against templates/personal-use.md")
    return findings


def build_section(name: str, path: Path, as_of: date, warnings: list[str],
                  errors: list[str]) -> str | None:
    label = path.name
    text = path.read_text(encoding="utf-8")
    if TEMPLATE_MARKER_RE.search(text):
        warnings.append(f"{label}: still a blank template (has an Interview Protocol section) — skipped")
        return None

    fm, body = parse_frontmatter(text)
    line_offset = text[: len(text) - len(body)].count("\n")
    updated = fm.get("updated", "").strip()
    stability = fm.get("stability", "").strip().lower()

    if updated:
        age = age_in_days(updated, as_of)
        if age is None:
            warnings.append(f"{label}: 'updated' is not YYYY-MM-DD ({updated!r})")
        elif name == "current-state" and age > CURRENT_STATE_MAX_AGE_DAYS:
            warnings.append(f"{label}: {age} days old (limit {CURRENT_STATE_MAX_AGE_DAYS}) — refresh before exporting")
        elif stability in ("evolving", "living") and age > EVOLVING_MAX_AGE_DAYS:
            warnings.append(f"{label}: {stability} file is {age} days old — reconfirm it")
    elif name in ("current-state", "current-projects"):
        warnings.append(f"{label}: no 'updated' date — Muse can't tell how current it is")

    body = blank_omitted(label, body, line_offset, errors)
    warnings.extend(redaction_findings(label, body, line_offset))
    warnings.extend(stale_intext_dates(label, body, line_offset, as_of))

    body = demote_headings(localize(body).strip())
    if updated:
        stamp = f"_As of {updated}" + (f" ({stability})" if stability else "") + "_"
        if stability == "draft":
            stamp += " — _first pass, not yet confirmed; check with me before relying on it_"
        # Put the stamp right under the section's own heading when it has one.
        first, _, rest = body.partition("\n")
        body = f"{first}\n\n{stamp}\n{rest}" if first.startswith("##") else f"{stamp}\n\n{body}"
    return body


def index_portfolio(portfolio: Path) -> dict[str, Path]:
    """Map canonical names (identity, ...) to files, ignoring numeric sort prefixes."""
    index: dict[str, Path] = {}
    for path in sorted(portfolio.glob("*.md")):
        index.setdefault(PREFIX_RE.sub("", path.stem).lower(), path)
    return index


def build_output(preamble: str, names: list[str], files: dict[str, Path], as_of: date,
                 warnings: list[str], errors: list[str]) -> tuple[str, list[str]]:
    sections, used = [], []
    for name in names:
        path = files.get(name)
        if path is None:
            continue
        section = build_section(name, path, as_of, warnings, errors)
        if section:
            sections.append(section)
            used.append(name)
    return preamble.format(as_of=as_of.isoformat()) + "\n" + "\n\n".join(sections) + "\n", used


def main() -> int:
    parser = argparse.ArgumentParser(description="Export a filled-out portfolio to Meta Muse's Memory.md + Soul.md.")
    parser.add_argument("portfolio", type=Path, help="folder holding your filled-out portfolio files")
    parser.add_argument("--out", type=Path, default=Path("muse-export"), help="output folder (default: ./muse-export)")
    parser.add_argument("--as-of", default=date.today().isoformat(), help="export date, YYYY-MM-DD (default: today)")
    parser.add_argument("--include", nargs="*", default=[], choices=OPTIONAL_MEMORY_FILES,
                        help="opt-in extras for Memory.md")
    parser.add_argument("--memory-budget", type=int, default=DEFAULT_MEMORY_BUDGET)
    parser.add_argument("--soul-budget", type=int, default=DEFAULT_SOUL_BUDGET)
    parser.add_argument("--strict", action="store_true", help="fail on any warning")
    args = parser.parse_args()

    try:
        as_of = datetime.strptime(args.as_of, "%Y-%m-%d").date()
    except ValueError:
        print(f"ERROR: --as-of must be YYYY-MM-DD (got {args.as_of!r})")
        return 1

    portfolio = args.portfolio.resolve()
    if not portfolio.is_dir():
        print(f"ERROR: portfolio folder not found: {portfolio}")
        return 1

    errors: list[str] = []
    warnings: list[str] = []

    files = index_portfolio(portfolio)
    missing = sorted(n for n in REQUIRED_FILES if n not in files)
    if missing:
        errors.append(f"missing minimum-load file(s): {', '.join(m + '.md' for m in missing)} (see LOAD-PROTOCOL.md)")

    memory_names = MEMORY_FILES + [n for n in OPTIONAL_MEMORY_FILES if n in args.include]
    memory, memory_used = build_output(MEMORY_PREAMBLE, memory_names, files, as_of, warnings, errors)
    soul, soul_used = build_output(SOUL_PREAMBLE, SOUL_FILES, files, as_of, warnings, errors)

    for req in sorted(REQUIRED_FILES):
        if req not in memory_used + soul_used and req not in missing:
            errors.append(f"{req}.md could not be exported (still a template?) — it's required")

    for label, text, budget in (("Memory.md", memory, args.memory_budget), ("Soul.md", soul, args.soul_budget)):
        if len(text) > budget:
            warnings.append(f"{label}: {len(text)} chars, over the {budget}-char soft budget — trim the source files")

    kit_root = Path(__file__).resolve().parent.parent
    out = args.out.resolve()
    is_public_kit = (kit_root / "GETTING-STARTED.md").exists() and (kit_root / "templates").is_dir()
    if is_public_kit and out.is_relative_to(kit_root) and not out.is_relative_to(kit_root / "04_DATA"):
        warnings.append(f"output folder is inside the public kit ({out}) — don't commit it; use a private folder")

    print(f"Portfolio: {portfolio}")
    print(f"Memory.md sections: {', '.join(memory_used) or '(none)'}")
    print(f"Soul.md sections:   {', '.join(soul_used) or '(none)'}")
    skipped = sorted(p.name for n, p in files.items() if n not in memory_used + soul_used)
    if skipped:
        print(f"Not exported:       {', '.join(skipped)}")

    if errors:
        print(f"\n{len(errors)} error(s):")
        for err in errors:
            print(f"  - {err}")
        print("\nNothing written.")
        return 1

    out.mkdir(parents=True, exist_ok=True)
    (out / "Memory.md").write_text(memory, encoding="utf-8")
    (out / "Soul.md").write_text(soul, encoding="utf-8")
    print(f"\nWrote {out / 'Memory.md'} ({len(memory)} chars, budget {args.memory_budget})")
    print(f"Wrote {out / 'Soul.md'} ({len(soul)} chars, budget {args.soul_budget})")

    if warnings:
        print(f"\n{len(warnings)} warning(s):")
        for warning in warnings:
            print(f"  - {warning}")
        if args.strict:
            print("\n--strict: failing on warnings.")
            return 1
    else:
        print("\nNo warnings.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
