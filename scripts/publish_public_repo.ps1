param(
    [Parameter(Mandatory = $true)]
    [string] $RemoteUrl
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath ".git")) {
    git init -b main
}

git add README.md protocol.md problems state manifests rounds config math_collab docs sources human .github scripts .gitignore
git commit -m "Initialize multi-AI math research workflow"
git remote add origin $RemoteUrl
git push -u origin main
