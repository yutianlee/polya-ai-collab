from __future__ import annotations

import argparse
import os
from pathlib import Path

from .orchestrator import call_openai_compatible, load_config, load_env_file


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Smoke test configured API agents.")
    parser.add_argument("--config", default="config/agents.web-polya.json")
    parser.add_argument("--agents", default="A4", help="Comma-separated agent ids.")
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument(
        "--prompt",
        default=(
            "In two or three sentences, confirm that you can participate in "
            "research on Pólya's conjecture for spherical shells and name one concrete "
            "next verification task."
        ),
    )
    args = parser.parse_args(argv)

    root = Path.cwd()
    load_env_file(root / ".env")
    agents, _, _ = load_config(root / args.config)
    wanted = {item.strip() for item in args.agents.split(",") if item.strip()}
    selected = [agent for agent in agents if agent.id in wanted]
    if not selected:
        raise SystemExit(f"No matching agents in config: {sorted(wanted)}")

    failed = False
    for agent in selected:
        if agent.provider != "openai_compatible":
            print(f"{agent.id}: skipped provider={agent.provider}")
            continue
        api_key_env = agent.raw.get("api_key_env", "")
        if not os.environ.get(api_key_env):
            print(f"{agent.id}: missing {api_key_env}")
            failed = True
            continue
        print(f"{agent.id}: calling {agent.raw.get('default_model')} at {agent.raw.get('endpoint')}")
        try:
            output = call_openai_compatible(agent, args.prompt, args.timeout)
        except Exception as exc:  # noqa: BLE001 - CLI should report provider errors verbatim.
            print(f"{agent.id}: failed: {exc}")
            failed = True
            continue
        print(f"{agent.id}: ok, {len(output)} chars")
        preview = output.strip().splitlines()[:8]
        for line in preview:
            print(f"  {line[:160]}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
