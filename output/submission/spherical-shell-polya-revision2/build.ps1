[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$root = $PSScriptRoot
$build = Join-Path $root 'build'
$latexmk = Get-Command latexmk -ErrorAction Stop

foreach ($name in @('main.tex', 'supplement.tex')) {
    $path = Join-Path $root $name
    foreach ($byte in [System.IO.File]::ReadAllBytes($path)) {
        if (($byte -lt 32) -and ($byte -notin 9, 10, 13)) {
            throw "Forbidden control byte in $name."
        }
    }
    if (Select-String -LiteralPath $path -Pattern '\input','\include','\includepdf' -SimpleMatch) {
        throw "Flattened release source $name contains a local include command."
    }
}

New-Item -ItemType Directory -Force -Path $build | Out-Null
Push-Location $root
try {
    foreach ($name in @('main.tex', 'supplement.tex')) {
        & $latexmk.Source -norc -pdf -interaction=nonstopmode -halt-on-error "-outdir=$build" $name
        if ($LASTEXITCODE -ne 0) {
            throw "LaTeX compilation failed for $name."
        }
    }
}
finally {
    Pop-Location
}

$fatalLogPattern = @(
    'LaTeX Error',
    'Fatal error',
    'Emergency stop',
    'undefined references',
    'Citation.*undefined',
    'multiply defined',
    'Rerun to get cross-references right'
) -join '|'
$failures = Get-ChildItem -LiteralPath $build -Filter '*.log' |
    Select-String -Pattern $fatalLogPattern
if ($failures) {
    $messages = $failures | ForEach-Object { "$($_.Path):$($_.LineNumber): $($_.Line)" }
    throw "Final log gate failed:`n$($messages -join "`n")"
}

Copy-Item -LiteralPath (Join-Path $build 'main.pdf') -Destination (Join-Path $root 'main.pdf') -Force
Copy-Item -LiteralPath (Join-Path $build 'supplement.pdf') -Destination (Join-Path $root 'supplement.pdf') -Force
Write-Host 'Built main.pdf and supplement.pdf from flattened sources.'
