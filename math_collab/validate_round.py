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
    parser = argparse.ArgumentParser(description="Validate the State Patch embedded in a judge output.")
    parser.add_argument("judge_output")
    parser.add_argument("--graph", default=str(DEFAULT_GRAPH_PATH))
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--round-index", type=int)
    args = parser.parse_args(argv)

    root = Path.cwd()
    judge_path = root / args.judge_output
    graph_path = root / args.graph
    judge_text = judge_path.read_text(encoding="utf-8")
    patch_text = extract_state_patch(judge_text)
    if not patch_text:
        print(f"No State Patch section found in {judge_path}")
        return 1

    graph = load_graph(graph_path)
    graph_issues = validate_graph(graph, root=root)
    if graph_issues:
        print("Graph validation failed:")
        for issue in graph_issues:
            print(f"- {issue}")
        return 1

    patch = parse_structured_text(patch_text, source=str(judge_path))
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
            judge_ref=str(judge_path.relative_to(root)),
        )
        graph_issues = validate_graph(graph, root=root)
        if graph_issues:
            print("Patched graph validation failed:")
            for issue in graph_issues:
                print(f"- {issue}")
            return 1
        write_graph(graph_path, graph)
        print(f"Patch applied: {patch_result_summary(result)}")
    else:
        print("Round State Patch OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
