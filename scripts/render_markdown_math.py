from __future__ import annotations

import argparse
import json
import os
import webbrowser
from pathlib import Path


HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>
    :root {{
      color-scheme: light dark;
      --bg: #f7f7f4;
      --fg: #1c1c1a;
      --muted: #686864;
      --code-bg: #ecece7;
      --border: #d9d9d0;
      --link: #1f5faa;
    }}
    @media (prefers-color-scheme: dark) {{
      :root {{
        --bg: #161714;
        --fg: #f1f1ec;
        --muted: #b8b8ad;
        --code-bg: #252720;
        --border: #3a3c32;
        --link: #8bbcff;
      }}
    }}
    body {{
      margin: 0;
      background: var(--bg);
      color: var(--fg);
      font: 16px/1.62 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}
    main {{
      max-width: 980px;
      margin: 0 auto;
      padding: 32px 22px 72px;
    }}
    header {{
      color: var(--muted);
      border-bottom: 1px solid var(--border);
      margin-bottom: 28px;
      padding-bottom: 12px;
      font-size: 14px;
    }}
    h1, h2, h3, h4 {{
      line-height: 1.25;
      margin-top: 1.6em;
    }}
    a {{ color: var(--link); }}
    pre {{
      background: var(--code-bg);
      border: 1px solid var(--border);
      border-radius: 6px;
      overflow: auto;
      padding: 14px;
    }}
    code {{
      background: var(--code-bg);
      border-radius: 4px;
      padding: 0.12em 0.28em;
      font-family: Consolas, "SFMono-Regular", Menlo, monospace;
      font-size: 0.92em;
    }}
    pre code {{
      background: transparent;
      padding: 0;
    }}
    blockquote {{
      border-left: 4px solid var(--border);
      color: var(--muted);
      margin-left: 0;
      padding-left: 16px;
    }}
    table {{
      border-collapse: collapse;
      width: 100%;
    }}
    th, td {{
      border: 1px solid var(--border);
      padding: 6px 10px;
    }}
    .MathJax {{
      overflow-x: auto;
      overflow-y: hidden;
      max-width: 100%;
    }}
    .math-display {{
      margin: 1em 0;
      overflow-x: auto;
      overflow-y: hidden;
    }}
  </style>
  <script>
    window.MathJax = {{
      tex: {{
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
        processEscapes: true,
        tags: 'ams'
      }},
      options: {{
        skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
      }}
    }};
  </script>
  <script defer src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
</head>
<body>
  <main>
    <header>{source}</header>
    <article id="content">Loading Markdown preview...</article>
  </main>
  <script id="md-source" type="application/json">{markdown_json}</script>
  <script>
    function escapeHtml(text) {{
      return text
        .replaceAll('&', '&amp;')
        .replaceAll('<', '&lt;')
        .replaceAll('>', '&gt;')
        .replaceAll('"', '&quot;');
    }}

    function protectDisplayMath(markdown) {{
      const blocks = [];
      const protectedMarkdown = markdown.replace(/(^|\\n)\\s*\\$\\$\\s*\\n([\\s\\S]*?)\\n\\s*\\$\\$\\s*(?=\\n|$)/g, (match, prefix, body) => {{
        const token = `@@MATH_BLOCK_${{blocks.length}}@@`;
        blocks.push(`<div class="math-display">\\\\[${{escapeHtml(body.trim())}}\\\\]</div>`);
        return `${{prefix}}${{token}}`;
      }});
      return {{ protectedMarkdown, blocks }};
    }}

    window.addEventListener('load', async () => {{
      const source = JSON.parse(document.getElementById('md-source').textContent);
      const target = document.getElementById('content');
      const protectedMath = protectDisplayMath(source);
      let html = marked.parse(protectedMath.protectedMarkdown, {{ gfm: true, breaks: false }});
      protectedMath.blocks.forEach((block, index) => {{
        html = html.replace(`<p>@@MATH_BLOCK_${{index}}@@</p>`, block);
        html = html.replace(`@@MATH_BLOCK_${{index}}@@`, block);
      }});
      target.innerHTML = html;
      if (window.MathJax && MathJax.typesetPromise) {{
        await MathJax.typesetPromise([target]);
      }}
    }});
  </script>
</body>
</html>
"""


def iter_markdown_inputs(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_dir():
            files.extend(sorted(path.rglob("*.md")))
        elif path.suffix.lower() == ".md":
            files.append(path)
    return files


def output_path_for(markdown_path: Path, out_dir: Path | None, adjacent: bool) -> Path:
    if adjacent:
        return markdown_path.with_suffix(".html")
    assert out_dir is not None
    rel = markdown_path.resolve().relative_to(Path.cwd().resolve())
    return (out_dir / rel).with_suffix(".html")


def render_file(markdown_path: Path, output_path: Path) -> None:
    markdown = markdown_path.read_text(encoding="utf-8")
    source = markdown_path.as_posix()
    html = HTML_TEMPLATE.format(
        title=markdown_path.name,
        source=source,
        markdown_json=json.dumps(markdown).replace("</", "<\\/"),
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8", newline="\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Render Markdown files to local HTML previews with MathJax math."
    )
    parser.add_argument("paths", nargs="+", help="Markdown files or directories.")
    parser.add_argument(
        "--out-dir",
        default="previews",
        help="Directory for generated previews when --adjacent is not used.",
    )
    parser.add_argument(
        "--adjacent",
        action="store_true",
        help="Write .html files next to each .md file instead of under --out-dir.",
    )
    parser.add_argument("--open", action="store_true", help="Open the first generated HTML file.")
    args = parser.parse_args(argv)

    paths = [Path(item) for item in args.paths]
    markdown_files = iter_markdown_inputs(paths)
    if not markdown_files:
        raise SystemExit("No Markdown files found.")

    out_dir = None if args.adjacent else Path(args.out_dir)
    outputs: list[Path] = []
    for markdown_path in markdown_files:
        output_path = output_path_for(markdown_path, out_dir, args.adjacent)
        render_file(markdown_path, output_path)
        outputs.append(output_path)
        print(f"{markdown_path} -> {output_path}")

    if args.open and outputs:
        webbrowser.open(outputs[0].resolve().as_uri())

    return 0


if __name__ == "__main__":
    os.chdir(Path(__file__).resolve().parents[1])
    raise SystemExit(main())
