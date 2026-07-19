[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [string]$OutputDirectory
)

$ErrorActionPreference = 'Stop'
$manuscriptDirectory = $PSScriptRoot
$analyticDirectory = Join-Path $manuscriptDirectory 'analytic'
$utf8NoBom = [System.Text.UTF8Encoding]::new($false)

function Expand-SingleInput {
    param(
        [Parameter(Mandatory)][string]$RootSource,
        [Parameter(Mandatory)][string]$InputToken,
        [Parameter(Mandatory)][string]$FragmentSource,
        [Parameter(Mandatory)][string]$Destination
    )

    $root = [System.IO.File]::ReadAllText($RootSource)
    $fragment = [System.IO.File]::ReadAllText($FragmentSource).TrimEnd()
    $matches = [regex]::Matches($root, [regex]::Escape($InputToken)).Count
    if ($matches -ne 1) {
        throw "Expected one occurrence of '$InputToken' in $RootSource; found $matches."
    }

    $expanded = $root.Replace(
        $InputToken,
        "% BEGIN mechanically inlined support source`r`n$fragment`r`n% END mechanically inlined support source"
    )
    if ($expanded -match '\\(?:input|include|includepdf)\s*\{') {
        throw "Flattened source still has a local include command: $Destination"
    }
    [System.IO.File]::WriteAllText($Destination, $expanded, $utf8NoBom)
}

New-Item -ItemType Directory -Force -Path $OutputDirectory | Out-Null
$resolvedOutput = (Resolve-Path -LiteralPath $OutputDirectory).Path

Expand-SingleInput `
    -RootSource (Join-Path $manuscriptDirectory 'spherical-shell-polya-proof.tex') `
    -InputToken '\input{analytic/ratio-sharp-global-closure-summary.tex}' `
    -FragmentSource (Join-Path $analyticDirectory 'ratio-sharp-global-closure-summary.tex') `
    -Destination (Join-Path $resolvedOutput 'main.tex')

Expand-SingleInput `
    -RootSource (Join-Path $manuscriptDirectory 'spherical-shell-polya-analytic-supplement.tex') `
    -InputToken '\input{analytic/ratio-sharp-global-closure-body.tex}' `
    -FragmentSource (Join-Path $analyticDirectory 'ratio-sharp-global-closure-body.tex') `
    -Destination (Join-Path $resolvedOutput 'supplement.tex')

Write-Host "Generated flattened submission sources in $resolvedOutput"
