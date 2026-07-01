# DeepSeek API Setup

This Pólya workflow has one API agent:

- `A4`: Deepseek V4-Pro

The web agents `A1`, `A2`, and `A3` run manually through ChatGPT, Claude, and Gemini.

## Configure Key

Create a local `.env` file from the template:

```powershell
Copy-Item .env.example .env
notepad .env
```

Fill in:

```text
DEEPSEEK_API_KEY=sk-...
DEEPSEEK_MODEL=deepseek-v4-pro
```

`.env` is ignored by Git. The orchestrator loads it automatically and does not overwrite already-set environment variables.

You can also set the key only for the current PowerShell session:

```powershell
$env:DEEPSEEK_API_KEY="sk-..."
$env:DEEPSEEK_MODEL="deepseek-v4-pro"
```

## Current API Settings

The active settings live in `config/agents.web-polya.json`.

```json
{
  "endpoint": "https://api.deepseek.com/chat/completions",
  "default_model": "deepseek-v4-pro",
  "temperature": 0.1,
  "extra_payload": {
    "thinking": {"type": "enabled"},
    "reasoning_effort": "max",
    "max_tokens": 32768
  }
}
```

## Smoke Test A4

After adding the key:

```powershell
python -m math_collab.api_smoke --config config/agents.web-polya.json --agents A4
```

Generate or advance the mixed run:

```powershell
python -m math_collab.orchestrator --config config/agents.web-polya.json --problem problems/polya_conjecture.md --run-id polya-main --start-round 1 --rounds 1 --skip-missing-api
```

What happens:

1. A1/A2/A3 web prompts are written under `rounds/polya-main/round_001/prompts/`.
2. A4 is called automatically if `DEEPSEEK_API_KEY` is configured.
3. If the key is missing, a pending file is written and the round barrier waits.
4. After saving A1/A2/A3 web responses into `handoff/polya-main/round_001/responses/`, rerun the same command to advance to reviews.
