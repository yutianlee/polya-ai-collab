param(
    [string] $RunId = "polya-main",
    [int] $StartRound = 1,
    [int] $Rounds = 1,
    [int] $PollSeconds = 30,
    [switch] $NoAutoPublish
)

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Resolve-Path (Join-Path $ScriptDir "..")
Set-Location $RepoRoot

& powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\watch_web_research_run.ps1 `
    -RunId $RunId `
    -StartRound $StartRound `
    -Rounds $Rounds `
    -PollSeconds $PollSeconds `
    -NoNormalize `
    -NoAutoPublish:$NoAutoPublish
