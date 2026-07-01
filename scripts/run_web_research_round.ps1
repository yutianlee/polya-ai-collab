param(
    [string] $RunId = "polya-main",
    [int] $Round = 1
)

$ErrorActionPreference = "Stop"

$Python = "C:\Users\yutia\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
if (-not (Test-Path -LiteralPath $Python)) {
    $Python = "python"
}

& $Python -m math_collab.orchestrator `
    --config config/agents.web-polya.json `
    --problem problems/polya_conjecture.md `
    --run-id $RunId `
    --start-round $Round `
    --rounds 1 `
    --timeout 1800 `
    --skip-missing-api

Write-Host ""
Write-Host "Next:"
Write-Host "1. Open prompt files under rounds/$RunId/round_$($Round.ToString('000'))/prompts."
Write-Host "   Prompt filenames include the round suffix, e.g. *_$Round.md."
Write-Host "2. Paste A1 prompts into ChatGPT Extended Pro, A2 prompts into Claude Opus 4.8 Max, and A3 prompts into Gemini Pro Deep Think."
Write-Host "3. A4 DeepSeek runs automatically when DEEPSEEK_API_KEY is set."
Write-Host "4. Use Copy response and save Markdown under handoff/$RunId/round_$($Round.ToString('000'))."
Write-Host "5. Ensure the judge response preserves the ## State Patch block."
Write-Host "6. Rerun this script for the same round until judge completes and the patch validates, then increment -Round."
