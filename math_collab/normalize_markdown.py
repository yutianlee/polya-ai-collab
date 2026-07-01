from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path


WEB_RESPONSE_MARKER = "# Paste the web response below this line, then rerun the orchestrator."
MOJIBAKE_MARKERS = "\u9225\u8305\u9518"

MATH_HINTS = [
    "\\",
    "_",
    "^",
    "{",
    "}",
    "sum",
    "int",
    "prod",
    "frac",
    "sqrt",
    "pi",
    "epsilon",
    "alpha",
    "beta",
    "gamma",
    "delta",
    "theta",
    "lambda",
    "sigma",
    "omega",
    "infty",
    "leq",
    "geq",
    "sim",
    "ll",
    "gg",
    "cdot",
    "times",
    "mathbb",
    "operatorname",
    "O_",
    "N(",
    "E(",
    "P(",
    "R^",
    "X^",
]


def looks_like_math(text: str) -> bool:
    stripped = text.strip()
    if len(stripped) < 3 or len(stripped) > 500:
        return False
    if stripped.startswith(("http://", "https://")):
        return False
    lower = stripped.lower()
    return any(hint.lower() in lower for hint in MATH_HINTS)


def normalize_bare_display_math(markdown: str) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip() == "[":
            block: list[str] = []
            j = i + 1
            while j < len(lines) and lines[j].strip() != "]":
                block.append(lines[j])
                j += 1
            if j < len(lines) and looks_like_math("\n".join(block)):
                out.append("$$")
                out.extend(block)
                out.append("$$")
                i = j + 1
                continue
        out.append(line)
        i += 1
    return "\n".join(out) + ("\n" if markdown.endswith("\n") else "")


def normalize_latex_display_delimiters(markdown: str) -> str:
    display_open = re.compile(r"(?<!\\)\\\[")
    display_close = re.compile(r"(?<!\\)\\\]")
    lines = markdown.splitlines()
    out: list[str] = []
    in_display = False
    for line in lines:
        stripped = line.strip()
        if stripped == r"\[" and not in_display:
            out.append("$$")
            in_display = True
            continue
        if stripped == r"\]" and in_display:
            out.append("$$")
            in_display = False
            continue
        open_match = None if "`" in line else display_open.search(line)
        close_match = None if "`" in line else display_close.search(line)
        if open_match and not in_display:
            before = line[: open_match.start()]
            after = line[open_match.end() :]
            if before.strip():
                out.append(before.rstrip())
            out.append("$$")
            if after.strip():
                out.append(after.strip())
            in_display = True
            continue
        if close_match and in_display:
            before = line[: close_match.start()]
            after = line[close_match.end() :]
            if before.strip():
                out.append(before.rstrip())
            out.append("$$")
            if after.strip():
                out.append(after.strip())
            in_display = False
            continue
        out.append(line)
    return "\n".join(out) + ("\n" if markdown.endswith("\n") else "")


def strip_outer_markdown_fence(markdown: str) -> str:
    stripped = markdown.strip()
    if not stripped.startswith("```"):
        return markdown
    lines = stripped.splitlines()
    first = lines[0].strip().lower() if lines else ""
    if len(lines) >= 2 and first in {"```markdown", "```md", "```"} and lines[-1].strip() == "```":
        return "\n".join(lines[1:-1]).strip() + "\n"
    return markdown


def strip_web_response_marker(markdown: str) -> str:
    text = markdown.strip()
    if text == WEB_RESPONSE_MARKER:
        return ""
    if text.startswith(WEB_RESPONSE_MARKER):
        return text[len(WEB_RESPONSE_MARKER) :].strip() + "\n"
    return markdown.replace(WEB_RESPONSE_MARKER, "").strip() + "\n"


def ascii_fold_latin(text: str) -> str:
    decomposed = unicodedata.normalize("NFKD", text)
    return "".join(char for char in decomposed if not unicodedata.combining(char))


def normalize_smart_punctuation(text: str) -> str:
    replacements = {
        "\ufeff": "",
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2010": "-",
        "\u2011": "-",
        "\u2013": "--",
        "\u2014": "--",
        "\u2026": "...",
        "\u2212": "-",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return ascii_fold_latin(text)


def repair_common_mojibake(markdown: str) -> str:
    # Common when UTF-8 text copied from web AI output is decoded through CP936/GBK.
    def recover(match: re.Match[str]) -> str:
        raw = match.group(0)
        if not any(marker in raw for marker in MOJIBAKE_MARKERS):
            return raw
        try:
            recovered = raw.encode("gbk").decode("utf-8")
        except UnicodeError:
            return raw
        return recovered

    markdown = re.sub(
        r"[\u4e00-\u9fff\u9200-\u92ff]*[\u9225\u8305\u9518][\u4e00-\u9fff\u9200-\u92ff]*",
        recover,
        markdown,
    )
    markdown = markdown.replace("\u9225?", '"')
    markdown = normalize_smart_punctuation(markdown)
    markdown = re.sub(r'(\*\*Reject: "[^"\n]+")\*$', r"\1**", markdown, flags=re.MULTILINE)
    markdown = markdown.replace('"diagnostic', '" diagnostic')
    return markdown

def normalize_copied_display_operators(markdown: str) -> str:
    lines = markdown.splitlines()
    out: list[str] = []
    in_display_math = False
    previous_u3_floor = False
    previous_u1_floor_difference = False
    previous_math_line = ""
    previous_restored_hash_equation = False

    def is_u3_floor(line: str) -> bool:
        return bool(re.search(r"\\left\\lfloor\\frac\{u\+3\}\{4\}\\right\\rfloor", line))

    def is_u1_floor(line: str) -> bool:
        return bool(re.search(r"\\left\\lfloor\\frac\{u\+1\}\{4\}\\right\\rfloor", line))

    def continues_restored_hash_equation(line: str) -> bool:
        return bool(
            re.fullmatch(r"2i\\chi_4\([hn]\)[.,]?", line)
            or re.fullmatch(r"-6x\^\{-6\},?", line)
        )

    def append_math_line(line: str, restored_hash_equation: bool = False) -> None:
        nonlocal previous_math_line, previous_restored_hash_equation
        nonlocal previous_u3_floor, previous_u1_floor_difference
        out.append(line)
        stripped_line = line.strip()
        previous_math_line = stripped_line
        previous_restored_hash_equation = restored_hash_equation
        previous_u1_floor_difference = stripped_line.startswith("-") and is_u1_floor(stripped_line)
        previous_u3_floor = not previous_u1_floor_difference and is_u3_floor(stripped_line)

    for line in lines:
        stripped = line.strip()
        if stripped == "$$":
            in_display_math = not in_display_math
            out.append(stripped)
            previous_u3_floor = False
            previous_u1_floor_difference = False
            previous_math_line = ""
            previous_restored_hash_equation = False
            continue
        if in_display_math and not stripped:
            continue
        if in_display_math and re.fullmatch(r"={2,}", stripped):
            append_math_line("=")
            continue
        if in_display_math and re.fullmatch(r"[-\u2212]{2,}", stripped):
            append_math_line("-")
            continue
        if in_display_math:
            copied_hash = re.fullmatch(r"#+\s+(.+)", stripped)
            if copied_hash:
                body = copied_hash.group(1)
                if is_u3_floor(body):
                    append_math_line(body)
                elif is_u1_floor(body):
                    append_math_line(f"- {body}")
                elif previous_math_line == "=":
                    append_math_line(body, restored_hash_equation=True)
                else:
                    append_math_line(f"= {body}", restored_hash_equation=True)
                continue
            if previous_math_line == "=" and stripped.startswith("= "):
                append_math_line(stripped[2:].strip(), restored_hash_equation=True)
                continue
            if previous_restored_hash_equation and continues_restored_hash_equation(stripped):
                append_math_line(f"= {stripped}")
                continue
            if previous_u3_floor and is_u1_floor(stripped) and not stripped.startswith(("-", "=")):
                append_math_line(f"- {stripped}")
                continue
            if previous_u1_floor_difference and stripped.startswith(r"\frac12+"):
                append_math_line("=")
                append_math_line(stripped)
                continue
        if in_display_math:
            append_math_line(line.rstrip())
        else:
            out.append(line.rstrip())
            previous_math_line = ""
            previous_restored_hash_equation = False
            previous_u3_floor = False
            previous_u1_floor_difference = False
    return "\n".join(out) + ("\n" if markdown.endswith("\n") else "")


def strip_chatgpt_content_references(markdown: str) -> str:
    return re.sub(r"\s*:contentReference\[[^\]]+\]\{[^}]+\}", "", markdown)


def normalize_final_newline(markdown: str) -> str:
    return markdown.rstrip() + "\n"


def normalize_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    normalized = strip_web_response_marker(original)
    normalized = strip_outer_markdown_fence(normalized)
    normalized = repair_common_mojibake(normalized)
    normalized = normalize_bare_display_math(normalized)
    normalized = normalize_latex_display_delimiters(normalized)
    normalized = normalize_copied_display_operators(normalized)
    normalized = strip_chatgpt_content_references(normalized)
    normalized = normalize_final_newline(normalized)
    if normalized != original:
        path.write_text(normalized, encoding="utf-8", newline="\n")
        return True
    return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Normalize copied web AI Markdown responses.")
    parser.add_argument("paths", nargs="+", help="Markdown files to normalize.")
    args = parser.parse_args(argv)

    changed = []
    for item in args.paths:
        path = Path(item)
        if normalize_file(path):
            changed.append(str(path))

    if changed:
        print("Normalized:")
        for path in changed:
            print(f"- {path}")
    else:
        print("No normalization needed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
