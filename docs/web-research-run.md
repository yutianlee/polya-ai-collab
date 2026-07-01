# Pólya Web Research Run Procedure

Use this procedure for mixed runs where A1/A2/A3 are manual web agents and A4 is called automatically through the DeepSeek API.

Agents:

- A1: GPT Pro Extended.
- A2: Claude Opus 4.8 Max.
- A3: Gemini Pro Deep Think.
- A4: Deepseek V4-Pro through the API.

Use one persistent web conversation for A1, one for A2, and one for A3 for the whole run. The public repo remains authoritative; specifically, `state/proof_obligations.yml` is the mathematical state and `manifests/reading_packet.md` is the compact generated packet.

For A4 API setup, see `docs/api-setup.md`.

## Guided Runner

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\auto_obligation_run.ps1 -RunId polya-main -StartRound 1 -Rounds 1
```

Useful switches:

```text
-SubmitPrompts   # press Enter after pasting prompts
-SkipPaste       # copy prompts to clipboard only
-NoOpenBrowser   # do not open ChatGPT/Claude/Gemini tabs
-NoAutoPublish   # apply Stage D locally without commit/push
```

The helper:

- validates the graph;
- generates prompts;
- opens ChatGPT, Claude, and Gemini unless `-NoOpenBrowser` is set;
- pastes each A1/A2/A3 prompt through the clipboard helper unless `-SkipPaste` is set;
- waits while the user copies web responses;
- saves and normalizes Markdown;
- waits for A4 API output;
- validates the judge patch;
- regenerates state and the reading packet;
- commits and pushes after Stage D unless `-NoAutoPublish` is set.

## Manual Watcher

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\watch_web_research_run.ps1 -RunId polya-main -StartRound 1 -Rounds 1 -PollSeconds 30
```

The watcher tells you which files are missing and where to save copied responses.

## Important Paths

Reasoning responses:

```text
handoff/<run-id>/round_XXX/responses/A1.md
handoff/<run-id>/round_XXX/responses/A2.md
handoff/<run-id>/round_XXX/responses/A3.md
rounds/<run-id>/round_XXX/responses/A4-XXX.md
```

Reviews:

```text
handoff/<run-id>/round_XXX/reviews/A1.md
handoff/<run-id>/round_XXX/reviews/A2.md
handoff/<run-id>/round_XXX/reviews/A3.md
rounds/<run-id>/round_XXX/reviews/A4.md
```

Judge:

```text
handoff/<run-id>/round_XXX/judge/judge-XXX.md
```

## Direct Orchestrator Command

```powershell
python -m math_collab.orchestrator --config config/agents.web-polya.json --problem problems/polya_conjecture.md --run-id polya-main --start-round 1 --rounds 1 --skip-missing-api
```

Re-run the same command after saving web responses or setting the API key.
