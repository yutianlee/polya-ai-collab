from __future__ import annotations

import argparse
from pathlib import Path

from .proof_obligations import (
    DEFAULT_GRAPH_PATH,
    apply_state_patch,
    extract_state_patch,
    load_graph,
    parse_structured_text,
    patch_result_summary,
    validate_graph,
    validate_patch_against_graph,
    write_graph,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate or apply proof-obligation state patches.")
    parser.add_argument("--graph", default=str(DEFAULT_GRAPH_PATH))
    parser.add_argument("--patch", help="Path to a judge output or raw state patch.")
    parser.add_argument("--apply", action="store_true", help="Apply the patch if validation passes.")
    parser.add_argument("--round-index", type=int)
    parser.add_argument("--judge-ref")
    args = parser.parse_args(argv)

    root = Path.cwd()
    graph_path = root / args.graph
    graph = load_graph(graph_path)
    issues = validate_graph(graph, root=root)
    if issues:
        print("Graph validation failed:")
        for issue in issues:
            print(f"- {issue}")
        return 1

    if not args.patch:
        print(f"Graph OK: {graph_path}")
        return 0

    patch_path = root / args.patch
    patch_source = patch_path.read_text(encoding="utf-8")
    patch_text = extract_state_patch(patch_source) or patch_source
    patch = parse_structured_text(patch_text, source=str(patch_path))
    patch_issues = validate_patch_against_graph(graph, patch)
    if patch_issues:
        print("Patch validation failed:")
        for issue in patch_issues:
            print(f"- {issue}")
        return 1

    if args.apply:
        graph, result = apply_state_patch(
            graph,
            patch,
            round_index=args.round_index,
            judge_ref=args.judge_ref,
        )
        issues = validate_graph(graph, root=root)
        if issues:
            print("Patched graph validation failed:")
            for issue in issues:
                print(f"- {issue}")
            return 1
        write_graph(graph_path, graph)
        print(f"Patch applied: {patch_result_summary(result)}")
    else:
        print("Patch OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
