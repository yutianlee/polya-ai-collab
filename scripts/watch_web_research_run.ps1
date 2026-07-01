param(
    [string] $RunId = "polya-main",
    [int] $StartRound = 1,
    [int] $Rounds = 3,
    [int] $PollSeconds = 30,
    [switch] $NoNormalize,
    [switch] $NoAutoPublish
)

$ErrorActionPreference = "Stop"

$Python = "C:\Users\yutia\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
if (-not (Test-Path -LiteralPath $Python)) {
    $Python = "python"
}

function Get-RoundName([int] $Round) {
    return "round_{0:D3}" -f $Round
}

function Get-PromptPath([string] $PromptBase, [string] $Name, [int] $Round) {
    $Suffixed = "$PromptBase\$($Name)_$Round.md"
    if (Test-Path -LiteralPath $Suffixed) {
        return $Suffixed
    }
    return "$PromptBase\$Name.md"
}

function Test-RealResponse([string] $Path) {
    if (-not (Test-Path -LiteralPath $Path)) {
        return $false
    }
    $Text = Get-Content -LiteralPath $Path -Raw
    if ([string]::IsNullOrWhiteSpace($Text)) {
        return $false
    }
    $Marker = "# Paste the web response below this line, then rerun the orchestrator."
    $Trimmed = $Text.Trim()
    if ($Trimmed -eq $Marker) {
        return $false
    }
    if ($Trimmed.StartsWith($Marker) -and $Trimmed.Substring($Marker.Length).Trim().Length -eq 0) {
        return $false
    }
    if ($Trimmed.StartsWith("# Pending API Response")) {
        return $false
    }
    return $true
}

function Invoke-Orchestrator([int] $Round) {
    & $Python -m math_collab.orchestrator `
        --config config/agents.web-polya.json `
        --problem problems/polya_conjecture.md `
        --run-id $RunId `
        --start-round $Round `
        --rounds 1 `
        --timeout 1800 `
        --skip-missing-api
}

function Invoke-GraphValidation() {
    & $Python -m math_collab.validate_state_patch --graph state/proof_obligations.yml
}

function Invoke-JudgePatchValidation([string] $JudgePath) {
    & $Python -m math_collab.validate_round $JudgePath
}

function Invoke-StageDPublish([int] $Round) {
    if ($NoAutoPublish) {
        Write-Host "Stage D auto-publish disabled."
        return
    }

    $RoundName = Get-RoundName $Round
    $RoundPath = "rounds\$RunId\$RoundName"
    Write-Host ""
    Write-Host "Publishing Stage D update to GitHub for $RunId / $RoundName..."

    & git add -u -- .
    $Paths = @("state", "manifests", "human", $RoundPath)
    $Existing = @($Paths | Where-Object { Test-Path -LiteralPath $_ })
    if ($Existing.Count -gt 0) {
        & git add -- @Existing
    }

    & git diff --cached --quiet
    if ($LASTEXITCODE -eq 0) {
        Write-Host "No staged Stage D changes to commit."
    } else {
        & git commit -m "Complete $RunId $RoundName"
    }

    & git push
}

function Normalize-IfPresent([string[]] $Paths) {
    if ($NoNormalize) {
        return
    }
    $Existing = @($Paths | Where-Object { Test-Path -LiteralPath $_ })
    if ($Existing.Count -gt 0) {
        & $Python -m math_collab.normalize_markdown @Existing | Write-Host
    }
}

function Show-NeededFiles([int] $Round) {
    $RoundName = Get-RoundName $Round
    $Base = "handoff\$RunId\$RoundName"
    $ArchiveBase = "rounds\$RunId\$RoundName"
    $PromptBase = "rounds\$RunId\$RoundName\prompts"

    $WebResponseFiles = @(
        "$Base\responses\A1.md",
        "$Base\responses\A2.md",
        "$Base\responses\A3.md"
    )
    $ApiResponseFiles = @(
        "$ArchiveBase\responses\A4-$($Round.ToString('000')).md"
    )
    $WebReviewFiles = @(
        "$Base\reviews\A1.md",
        "$Base\reviews\A2.md",
        "$Base\reviews\A3.md"
    )
    $ApiReviewFiles = @(
        "$ArchiveBase\reviews\A4.md"
    )
    $JudgeFile = "$Base\judge\judge-$($Round.ToString('000')).md"

    if (($WebResponseFiles | Where-Object { -not (Test-RealResponse $_) }).Count -gt 0) {
        Write-Host ""
        Write-Host "Round $RoundName is waiting for reasoning responses."
        Write-Host "Paste these prompts into the fixed A1/A2/A3 web conversations:"
        Write-Host "  $(Get-PromptPath $PromptBase 'A1_reasoning' $Round)"
        Write-Host "  $(Get-PromptPath $PromptBase 'A2_reasoning' $Round)"
        Write-Host "  $(Get-PromptPath $PromptBase 'A3_reasoning' $Round)"
        Write-Host "Then use Copy response and save Markdown to:"
        $WebResponseFiles | ForEach-Object { Write-Host "  $_" }
        return "responses"
    }

    Normalize-IfPresent $WebResponseFiles
    Invoke-Orchestrator $Round

    if (($ApiResponseFiles | Where-Object { -not (Test-RealResponse $_) }).Count -gt 0) {
        Write-Host ""
        Write-Host "Round $RoundName is waiting for A4 DeepSeek API reasoning."
        Write-Host "Set DEEPSEEK_API_KEY, then rerun or let the watcher poll:"
        $ApiResponseFiles | ForEach-Object { Write-Host "  $_" }
        return "api-responses"
    }

    if (($WebReviewFiles | Where-Object { -not (Test-RealResponse $_) }).Count -gt 0) {
        Write-Host ""
        Write-Host "Round $RoundName is waiting for cross reviews."
        Write-Host "Paste these review prompts:"
        Write-Host "  $(Get-PromptPath $PromptBase 'A1_review' $Round)"
        Write-Host "  $(Get-PromptPath $PromptBase 'A2_review' $Round)"
        Write-Host "  $(Get-PromptPath $PromptBase 'A3_review' $Round)"
        Write-Host "Then use Copy response and save Markdown to:"
        $WebReviewFiles | ForEach-Object { Write-Host "  $_" }
        return "reviews"
    }

    Normalize-IfPresent $WebReviewFiles
    Invoke-Orchestrator $Round

    if (($ApiReviewFiles | Where-Object { -not (Test-RealResponse $_) }).Count -gt 0) {
        Write-Host ""
        Write-Host "Round $RoundName is waiting for A4 DeepSeek API review."
        Write-Host "Set DEEPSEEK_API_KEY, then rerun or let the watcher poll:"
        $ApiReviewFiles | ForEach-Object { Write-Host "  $_" }
        return "api-reviews"
    }

    if (-not (Test-RealResponse $JudgeFile)) {
        Write-Host ""
        Write-Host "Round $RoundName is waiting for judge synthesis."
        Write-Host "Paste this judge prompt into ChatGPT Extended Pro:"
        Write-Host "  $(Get-PromptPath $PromptBase 'judge' $Round)"
        Write-Host "Then use Copy response and save Markdown to:"
        Write-Host "  $JudgeFile"
        return "judge"
    }

    Normalize-IfPresent @($JudgeFile)
    Invoke-JudgePatchValidation $JudgeFile
    Invoke-Orchestrator $Round
    Invoke-GraphValidation
    Invoke-StageDPublish $Round
    Write-Host ""
    Write-Host "Round $RoundName is complete."
    return "complete"
}

Write-Host "Watching run '$RunId' from round $StartRound for $Rounds round(s)."
Write-Host "Press Ctrl+C to stop."
Invoke-GraphValidation

$EndRound = $StartRound + $Rounds - 1
for ($Round = $StartRound; $Round -le $EndRound; $Round++) {
    Invoke-Orchestrator $Round
    while ($true) {
        $Status = Show-NeededFiles $Round
        if ($Status -eq "complete") {
            break
        }
        Start-Sleep -Seconds $PollSeconds
    }
}

Write-Host ""
Write-Host "All requested rounds are complete."
