# Thai Token Optimizer v2.0 - Universal One-Line Installer (Windows PowerShell)
# Usage: irm https://raw.githubusercontent.com/Atc1501/thai-token-optimizer/main/install.ps1 | iex

$ErrorActionPreference = "Stop"
$SkillUrl = "https://raw.githubusercontent.com/Atc1501/thai-token-optimizer/main/SKILL.md"

$TargetDirs = @(
    "$HOME\.gemini\config\skills\thai-token-optimizer",
    "$HOME\.agents\skills\thai-token-optimizer",
    "$HOME\.claude\skills\thai-token-optimizer"
)

Write-Host "Installing Thai Token Optimizer v2.0..." -ForegroundColor Cyan

foreach ($Dir in $TargetDirs) {
    if (-not (Test-Path $Dir)) {
        New-Item -ItemType Directory -Force -Path $Dir | Out-Null
    }
    $TargetFile = Join-Path $Dir "SKILL.md"
    Invoke-RestMethod -Uri $SkillUrl -OutFile $TargetFile
    Write-Host "  [OK] Installed -> $TargetFile" -ForegroundColor Green
}

Write-Host "`nDone! Thai Token Optimizer v2.0 is now active across Antigravity, Gemini CLI, Codex, and Claude Code." -ForegroundColor Yellow
