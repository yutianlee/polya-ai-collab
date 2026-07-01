from __future__ import annotations

import argparse
import re
from datetime import datetime
from pathlib import Path


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")[:60] or "note"


def append_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    path.write_text(existing.rstrip() + "\n\n" + text.strip() + "\n", encoding="utf-8", newline="\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Add human intervention notes to the research workflow.")
    parser.add_argument(
        "--kind",
        choices=["idea", "reference", "goal", "constraint", "correction", "question"],
        required=True,
    )
    parser.add_argument("--title", required=True)
    parser.add_argument("--text", required=True)
    parser.add_argument(
        "--activate",
        action="store_true",
        help="Also append this note to human/current_directives.md so it strongly affects the next round.",
    )
    args = parser.parse_args(argv)

    root = Path.cwd()
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{timestamp}_{args.kind}_{slugify(args.title)}.md"
    note = f"""# {args.title}

Kind: {args.kind}
Timestamp: {datetime.now().isoformat(timespec="seconds")}

{args.text}
"""
    note_path = root / "human" / "inbox" / filename
    note_path.parent.mkdir(parents=True, exist_ok=True)
    note_path.write_text(note, encoding="utf-8", newline="\n")

    if args.kind == "idea":
        append_text(root / "human" / "ideas.md", note)
    elif args.kind == "reference":
        append_text(root / "human" / "references.md", note)
    elif args.kind == "goal":
        append_text(root / "human" / "goals.md", note)

    if args.activate:
        append_text(root / "human" / "current_directives.md", note)

    print(f"Added human note: {note_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
