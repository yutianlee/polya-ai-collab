param(
    [Parameter(Mandatory = $true)]
    [string] $PromptPath,

    [int] $DelaySeconds = 5,

    [switch] $Submit
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $PromptPath)) {
    throw "Prompt file not found: $PromptPath"
}

$Text = Get-Content -LiteralPath $PromptPath -Raw
Set-Clipboard -Value $Text

Add-Type -AssemblyName System.Windows.Forms

Write-Host ""
Write-Host "Copied prompt to clipboard:"
Write-Host "  $PromptPath"
Write-Host ""
Write-Host "Click inside the target web AI input box now."
Write-Host "Pasting in $DelaySeconds second(s)..."

for ($i = $DelaySeconds; $i -gt 0; $i--) {
    Write-Host "$i..."
    Start-Sleep -Seconds 1
}

[System.Windows.Forms.SendKeys]::SendWait("^v")
Start-Sleep -Milliseconds 800

if ($Submit) {
    [System.Windows.Forms.SendKeys]::SendWait("{ENTER}")
    Write-Host "Pasted and submitted."
} else {
    Write-Host "Pasted. Review it, then press Enter/click Send manually."
}
