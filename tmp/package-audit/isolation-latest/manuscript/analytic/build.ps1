[CmdletBinding()]
param(
    [string]$Compiler = ''
)

$ErrorActionPreference = 'Stop'

if (-not $Compiler) {
    if (Get-Command tectonic -ErrorAction SilentlyContinue) {
        $Compiler = 'tectonic'
    }
    elseif (Get-Command latexmk -ErrorAction SilentlyContinue) {
        $Compiler = 'latexmk'
    }
    else {
        throw 'No supported LaTeX compiler found (tectonic or latexmk).'
    }
}

function Invoke-LatexBuild {
    param(
        [Parameter(Mandatory)]
        [string]$Source,
        [Parameter(Mandatory)]
        [string]$OutputDirectory
    )

    $compilerName = [System.IO.Path]::GetFileNameWithoutExtension($Compiler)
    if ($compilerName -eq 'tectonic') {
        & $Compiler --outdir $OutputDirectory $Source
    }
    elseif ($compilerName -eq 'latexmk') {
        & $Compiler -pdf -interaction=nonstopmode -halt-on-error "-outdir=$OutputDirectory" $Source
    }
    else {
        throw "Unsupported LaTeX compiler '$Compiler'. Use tectonic or latexmk."
    }

    if ($LASTEXITCODE -ne 0) {
        throw "LaTeX compilation failed for $Source."
    }
}

$parts = @(
    'ratio-sharp-global-closure'
)

$analyticDirectory = $PSScriptRoot
$manuscriptDirectory = Split-Path -Parent $analyticDirectory
$compiledDirectory = Join-Path $analyticDirectory 'compiled'

New-Item -ItemType Directory -Force -Path $compiledDirectory | Out-Null

Push-Location $analyticDirectory
try {
    foreach ($part in $parts) {
        Invoke-LatexBuild -Source "$part.tex" -OutputDirectory $compiledDirectory
    }
}
finally {
    Pop-Location
}

Push-Location $manuscriptDirectory
try {
    Invoke-LatexBuild -Source 'spherical-shell-polya-analytic-supplement.tex' -OutputDirectory $manuscriptDirectory
    Invoke-LatexBuild -Source 'spherical-shell-polya-proof.tex' -OutputDirectory $manuscriptDirectory
}
finally {
    Pop-Location
}

Write-Host "Built the ratio-sharp support module, analytic supplement, and main paper with $Compiler."
