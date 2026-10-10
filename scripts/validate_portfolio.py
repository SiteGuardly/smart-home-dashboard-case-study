from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ("README.md", "SECURITY.md", "CHANGELOG.md")
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def local_target(raw: str) -> str | None:
    target = raw.strip().split(" ", 1)[0].strip("<>")
    if not target or target.startswith(("http://", "https://", "mailto:", "#", "data:")):
        return None
    return target.split("#", 1)[0]


def main() -> int:
    problems: list[str] = []
    for required in REQUIRED:
        if not (ROOT / required).is_file():
            problems.append(f"Missing required file: {required}")

    for markdown in ROOT.rglob("*.md"):
        if ".git" in markdown.parts:
            continue
        for match in LINK.finditer(markdown.read_text(encoding="utf-8")):
            target = local_target(match.group(1))
            if target is None:
                continue
            resolved = (markdown.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                problems.append(f"Reference escapes repository: {markdown.relative_to(ROOT)} -> {target}")
                continue
            if not resolved.exists():
                problems.append(f"Missing reference: {markdown.relative_to(ROOT)} -> {target}")

    if problems:
        print("\n".join(problems))
        return 1
    print("Portfolio references are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

