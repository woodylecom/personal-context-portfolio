#!/usr/bin/env python3
"""
Personal Context Portfolio Kit — validator.

This kit is different from a single filled-out portfolio: it ships template
files (interview protocols, not context to load), example personas, and
wiring guides, spread across several directories. Frontmatter is opt-in per
file here, not mandatory kit-wide — see templates/_frontmatter.md for the
convention. So this validator:

  1. Recursively scans every .md file in the kit.
  2. If a file HAS a YAML frontmatter block, checks it's well-formed:
       - updated    (YYYY-MM-DD)
       - stability  (one of: stable, evolving, draft)
       - scope      (any non-empty string)
     Files WITHOUT frontmatter are not an error — frontmatter is opt-in.
  3. Checks every markdown link of the form [text](path.md) or
     [text](path.md#anchor) pointing to a local .md file resolves to an
     existing file somewhere in the kit.

Note on "stability": this kit normalizes to {stable, evolving, draft}. The
live reference portfolio this kit was backported from also uses a "living"
value for weekly-cadence files (see its current-state file). This kit folds
that into "evolving" instead of adding a fourth value. If you fork this and
want a distinct "living" tier for weekly-cadence files, add it to
VALID_STABILITY below and document the distinction in
templates/_frontmatter.md.

Usage:
    python tools/validate.py           # run from anywhere inside the kit
    python validate.py                 # run from inside tools/

Exit code: 0 on pass, 1 on any failure. Errors are printed to stdout.
"""

from __future__ import annotations

import re
import sys
from datetime import datetime
from pathlib import Path

REQUIRED_FIELDS = {"updated", "stability", "scope"}
VALID_STABILITY = {"stable", "evolving", "draft"}

# Directories to skip entirely (not part of the kit's content).
EXCLUDE_DIRS = {".git", "node_modules", "__pycache__"}

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
FIELD_RE = re.compile(r"^(\w+):\s*(.+?)\s*$", re.MULTILINE)
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def find_kit_root() -> Path:
    """Locate the kit root by walking up until we find README.md + GETTING-STARTED.md."""
    here = Path(__file__).resolve().parent
    for candidate in (here, here.parent):
        if (candidate / "README.md").exists() and (candidate / "GETTING-STARTED.md").exists():
            return candidate
    raise SystemExit("ERROR: could not locate kit root from " + str(here))


def iter_md_files(root: Path):
    for path in sorted(root.rglob("*.md")):
        rel_parts = path.relative_to(root).parts
        if any(part in EXCLUDE_DIRS for part in rel_parts):
            continue
        yield path


def parse_frontmatter(text: str) -> dict[str, str] | None:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    return dict(FIELD_RE.findall(match.group(1)))


def check_frontmatter(rel: str, text: str) -> list[str]:
    """Validate frontmatter IF present. Absence is not an error in this kit."""
    errors: list[str] = []
    fm = parse_frontmatter(text)
    if fm is None:
        return errors

    missing = REQUIRED_FIELDS - fm.keys()
    if missing:
        errors.append(f"{rel}: missing frontmatter fields: {sorted(missing)}")

    updated = fm.get("updated", "")
    if updated:
        try:
            datetime.strptime(updated, "%Y-%m-%d")
        except ValueError:
            errors.append(f"{rel}: 'updated' is not YYYY-MM-DD (got {updated!r})")

    stability = fm.get("stability", "").lower()
    if stability and stability not in VALID_STABILITY:
        errors.append(
            f"{rel}: 'stability' must be one of {sorted(VALID_STABILITY)} (got {stability!r})"
        )

    scope = fm.get("scope", "").strip()
    if "scope" in fm and not scope:
        errors.append(f"{rel}: 'scope' is empty")

    return errors


def check_links(md_file: Path, rel: str, text: str, root: Path) -> list[str]:
    errors: list[str] = []
    for _text, target in LINK_RE.findall(text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        path_part = target.split("#", 1)[0]
        if not path_part or not path_part.endswith(".md"):
            continue
        resolved = (md_file.parent / path_part).resolve()
        try:
            resolved.relative_to(root.resolve())
        except ValueError:
            # Link points outside the kit root - not this validator's concern.
            continue
        if not resolved.exists():
            errors.append(f"{rel}: broken link -> {target}")
    return errors


def main() -> int:
    root = find_kit_root()
    md_files = list(iter_md_files(root))
    if not md_files:
        print(f"ERROR: no .md files found in {root}")
        return 1

    all_errors: list[str] = []
    for md in md_files:
        rel = md.relative_to(root).as_posix()
        text = md.read_text(encoding="utf-8")
        all_errors.extend(check_frontmatter(rel, text))
        all_errors.extend(check_links(md, rel, text, root))

    print(f"Validated {len(md_files)} files in {root}")
    if all_errors:
        print(f"\n{len(all_errors)} issue(s) found:\n")
        for err in all_errors:
            print(f"  - {err}")
        return 1
    print("All checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
