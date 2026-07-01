param(
    [string] $RunId = "polya-main",
    [int] $StartRound = 1,
    [int] $Rounds = 1,
    [int] $DelaySeconds = 6,
    [switch] $SubmitPrompts,
    [switch] $SkipPaste,
    [switch] $NoOpenBrowser,
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

function Save-ClipboardResponse([string] $OutputPath) {
    powershell -NoProfile -ExecutionPolicy Bypass -File scripts\save_clipboard_response.ps1 -OutputPath $OutputPath
}

function Paste-Prompt([string] $PromptPath, [string] $Label) {
    if ($SkipPaste) {
        $Text = Get-Content -LiteralPath $PromptPath -Raw
        Set-Clipboard -Value $Text
        Write-Host ""
        Write-Host "Copied $Label prompt to clipboard:"
        Write-Host "  $PromptPath"
        Write-Host "Paste it into the web UI, send it, then copy the model response."
        return
    }

    Write-Host ""
    Write-Host "Ready to paste $Label prompt."
    Write-Host "Focus the target web input before the countdown ends."
    $Args = @(
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-File", "scripts\paste_web_prompt.ps1",
        "-PromptPath", $PromptPath,
        "-DelaySeconds", $DelaySeconds
    )
    if ($SubmitPrompts) {
        $Args += "-Submit"
    }
    powershell @Args
}

function Capture-WebResponse([string] $PromptPath, [string] $OutputPath, [string] $Label) {
    if (Test-RealResponse $OutputPath) {
        Write-Host "$Label already saved: $OutputPath"
        return
    }

    Paste-Prompt $PromptPath $Label
    Write-Host ""
    Write-Host "Wait for $Label to finish, click the web UI's Copy response button, then press Enter here."
    [void](Read-Host "Press Enter after Copy response")
    Save-ClipboardResponse $OutputPath
}

function Wait-ForApiFile([string] $Path, [string] $Label, [int] $Round) {
    while (-not (Test-RealResponse $Path)) {
        Write-Host ""
        Write-Host "$Label is not complete yet:"
        Write-Host "  $Path"
        Write-Host "If this is a pending API response, set DEEPSEEK_API_KEY and press Enter to rerun the orchestrator."
        [void](Read-Host "Press Enter to retry")
        Invoke-Orchestrator $Round
    }
}

function Process-Round([int] $Round) {
    $RoundName = Get-RoundName $Round
    $HandoffBase = "handoff\$RunId\$RoundName"
    $ArchiveBase = "rounds\$RunId\$RoundName"
    $PromptBase = "$ArchiveBase\prompts"

    Write-Host ""
    Write-Host "=== $RunId / $RoundName ==="
    Invoke-Orchestrator $Round

    $A1ReasoningPrompt = Get-PromptPath $PromptBase "A1_reasoning" $Round
    $A2ReasoningPrompt = Get-PromptPath $PromptBase "A2_reasoning" $Round
    $A3ReasoningPrompt = Get-PromptPath $PromptBase "A3_reasoning" $Round
    $A1ReasoningOut = "$HandoffBase\responses\A1.md"
    $A2ReasoningOut = "$HandoffBase\responses\A2.md"
    $A3ReasoningOut = "$HandoffBase\responses\A3.md"
    Capture-WebResponse $A1ReasoningPrompt $A1ReasoningOut "A1 reasoning"
    Capture-WebResponse $A2ReasoningPrompt $A2ReasoningOut "A2 reasoning"
    Capture-WebResponse $A3ReasoningPrompt $A3ReasoningOut "A3 reasoning"

    Invoke-Orchestrator $Round
    Wait-ForApiFile "$ArchiveBase\responses\A4-$($Round.ToString('000')).md" "A4 reasoning" $Round
    Invoke-Orchestrator $Round

    $A1ReviewPrompt = Get-PromptPath $PromptBase "A1_review" $Round
    $A2ReviewPrompt = Get-PromptPath $PromptBase "A2_review" $Round
    $A3ReviewPrompt = Get-PromptPath $PromptBase "A3_review" $Round
    $A1ReviewOut = "$HandoffBase\reviews\A1.md"
    $A2ReviewOut = "$HandoffBase\reviews\A2.md"
    $A3ReviewOut = "$HandoffBase\reviews\A3.md"
    Capture-WebResponse $A1ReviewPrompt $A1ReviewOut "A1 review"
    Capture-WebResponse $A2ReviewPrompt $A2ReviewOut "A2 review"
    Capture-WebResponse $A3ReviewPrompt $A3ReviewOut "A3 review"

    Invoke-Orchestrator $Round
    Wait-ForApiFile "$ArchiveBase\reviews\A4.md" "A4 review" $Round
    Invoke-Orchestrator $Round

    $JudgePrompt = Get-PromptPath $PromptBase "judge" $Round
    $JudgeOut = "$HandoffBase\judge\judge-$($Round.ToString('000')).md"
    Capture-WebResponse $JudgePrompt $JudgeOut "A1 judge"

    Write-Host ""
    Write-Host "Validating saved judge State Patch before Stage D..."
    & $Python -m math_collab.validate_round $JudgeOut

    Invoke-Orchestrator $Round
    Invoke-GraphValidation
    Invoke-StageDPublish $Round

    Write-Host ""
    Write-Host "Completed $RoundName. Reading packet and proof-obligation graph are updated."
}

if (-not $NoOpenBrowser) {
    Start-Process "https://chatgpt.com/"
    Start-Process "https://claude.ai/"
    Start-Process "https://gemini.google.com/"
}

Invoke-GraphValidation

$EndRound = $StartRound + $Rounds - 1
for ($Round = $StartRound; $Round -le $EndRound; $Round++) {
    Process-Round $Round
}

Write-Host ""
Write-Host "All requested obligation workflow rounds are complete."
