[CmdletBinding()]
param(
    [string]$Compiler = ''
)

$ErrorActionPreference = 'Stop'

$analyticDirectory = $PSScriptRoot
$manuscriptDirectory = Split-Path -Parent $analyticDirectory
$repositoryRoot = Split-Path -Parent $manuscriptDirectory
$releasePdfDirectory = Join-Path $repositoryRoot 'output/pdf'
$compiledDirectory = Join-Path $analyticDirectory 'compiled'
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss-fff'
$stagingDirectory = Join-Path $repositoryRoot "tmp/release-build-$stamp"

if (-not $Compiler) {
    $latexmk = Get-Command latexmk -ErrorAction SilentlyContinue
    $tectonic = Get-Command tectonic -ErrorAction SilentlyContinue
    if ($latexmk) {
        $Compiler = $latexmk.Source
    }
    elseif ($tectonic) {
        $Compiler = $tectonic.Source
    }
    else {
        throw 'No supported LaTeX compiler found (latexmk preferred; tectonic fallback).'
    }
}

function Assert-CleanSourceBytes {
    param([Parameter(Mandatory)][string]$Path)

    foreach ($byte in [System.IO.File]::ReadAllBytes($Path)) {
        if (($byte -lt 32) -and ($byte -notin 9, 10, 13)) {
            throw "Forbidden control byte in $Path."
        }
    }
}

function Invoke-LatexBuild {
    param(
        [Parameter(Mandatory)][string]$WorkingDirectory,
        [Parameter(Mandatory)][string]$Source,
        [Parameter(Mandatory)][string]$OutputDirectory
    )

    $compilerName = [System.IO.Path]::GetFileNameWithoutExtension($Compiler).ToLowerInvariant()
    Push-Location $WorkingDirectory
    try {
        if ($compilerName -eq 'latexmk') {
            & $Compiler -norc -pdf -interaction=nonstopmode -halt-on-error "-outdir=$OutputDirectory" $Source
        }
        elseif ($compilerName -eq 'tectonic') {
            & $Compiler --keep-logs --outdir $OutputDirectory $Source
        }
        else {
            throw "Unsupported LaTeX compiler '$Compiler'. Use latexmk or tectonic."
        }

        if ($LASTEXITCODE -ne 0) {
            throw "LaTeX compilation failed for $Source."
        }
    }
    finally {
        Pop-Location
    }
}

$liveSources = @(
    (Join-Path $manuscriptDirectory 'spherical-shell-polya-proof.tex'),
    (Join-Path $manuscriptDirectory 'spherical-shell-polya-analytic-supplement.tex'),
    (Join-Path $analyticDirectory 'ratio-sharp-global-closure.tex'),
    (Join-Path $analyticDirectory 'ratio-sharp-global-closure-body.tex'),
    (Join-Path $analyticDirectory 'ratio-sharp-global-closure-summary.tex')
)

foreach ($source in $liveSources) {
    Assert-CleanSourceBytes -Path $source
}

$generatedPdfInclude = Select-String -Path $liveSources -Pattern '\includepdf' -SimpleMatch
if ($generatedPdfInclude) {
    throw 'A live source includes a generated PDF; the release must build from TeX sources only.'
}

New-Item -ItemType Directory -Force -Path $stagingDirectory | Out-Null

Invoke-LatexBuild -WorkingDirectory $analyticDirectory `
    -Source 'ratio-sharp-global-closure.tex' -OutputDirectory $stagingDirectory
Invoke-LatexBuild -WorkingDirectory $manuscriptDirectory `
    -Source 'spherical-shell-polya-analytic-supplement.tex' -OutputDirectory $stagingDirectory
Invoke-LatexBuild -WorkingDirectory $manuscriptDirectory `
    -Source 'spherical-shell-polya-proof.tex' -OutputDirectory $stagingDirectory

$fatalLogPattern = @(
    'LaTeX Error',
    'Fatal error',
    'Emergency stop',
    'undefined references',
    'Citation.*undefined',
    'multiply defined',
    'Rerun to get cross-references right'
) -join '|'
$logFailures = Get-ChildItem -LiteralPath $stagingDirectory -Filter '*.log' |
    Select-String -Pattern $fatalLogPattern
if ($logFailures) {
    $messages = $logFailures | ForEach-Object { "$($_.Path):$($_.LineNumber): $($_.Line)" }
    throw "Release log gate failed:`n$($messages -join "`n")"
}

New-Item -ItemType Directory -Force -Path $compiledDirectory | Out-Null
New-Item -ItemType Directory -Force -Path $releasePdfDirectory | Out-Null

$ratioPdf = Join-Path $stagingDirectory 'ratio-sharp-global-closure.pdf'
$supplementPdf = Join-Path $stagingDirectory 'spherical-shell-polya-analytic-supplement.pdf'
$mainPdf = Join-Path $stagingDirectory 'spherical-shell-polya-proof.pdf'

Copy-Item -LiteralPath $ratioPdf -Destination (Join-Path $compiledDirectory 'ratio-sharp-global-closure.pdf') -Force
Copy-Item -LiteralPath $supplementPdf -Destination (Join-Path $manuscriptDirectory 'spherical-shell-polya-analytic-supplement.pdf') -Force
Copy-Item -LiteralPath $mainPdf -Destination (Join-Path $manuscriptDirectory 'spherical-shell-polya-proof.pdf') -Force
Copy-Item -LiteralPath $supplementPdf -Destination (Join-Path $releasePdfDirectory 'spherical-shell-polya-analytic-supplement.pdf') -Force
Copy-Item -LiteralPath $mainPdf -Destination (Join-Path $releasePdfDirectory 'spherical-shell-polya-proof-analytic.pdf') -Force

$mainCanonical = Get-FileHash (Join-Path $manuscriptDirectory 'spherical-shell-polya-proof.pdf') -Algorithm SHA256
$mainRelease = Get-FileHash (Join-Path $releasePdfDirectory 'spherical-shell-polya-proof-analytic.pdf') -Algorithm SHA256
$suppCanonical = Get-FileHash (Join-Path $manuscriptDirectory 'spherical-shell-polya-analytic-supplement.pdf') -Algorithm SHA256
$suppRelease = Get-FileHash (Join-Path $releasePdfDirectory 'spherical-shell-polya-analytic-supplement.pdf') -Algorithm SHA256
if (($mainCanonical.Hash -ne $mainRelease.Hash) -or ($suppCanonical.Hash -ne $suppRelease.Hash)) {
    throw 'Canonical and release PDF copies differ after publication.'
}

Write-Host "Built and published the ratio module, analytic supplement, and main paper with $Compiler."
Write-Host "Staging directory: $stagingDirectory"
