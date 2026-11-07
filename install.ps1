<#
.SYNOPSIS
    Thai Token Optimizer v2.1 - Dual-Mode Installer & Mode Switcher
.DESCRIPTION
    Supports two activation modes:
    1. Skill Mode (On-Demand): Call via @thai-token-optimizer when needed.
    2. Always-On Global Rule : Automatically active in every chat from Turn 0.
    3. Disable Always-On     : Revert from Always-On back to Skill-Only mode safely.
    4. Uninstall All         : Remove both Always-On rule and Skill files.
.PARAMETER Mode
    Optional: 'menu', 'skill', 'always-on', 'disable', 'uninstall', or 'status'
#>
param(
    [ValidateSet("menu", "skill", "always-on", "disable", "uninstall", "status")]
    [string]$Mode = "menu"
)

$ErrorActionPreference = "Stop"
$Utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$SkillUrl = "https://raw.githubusercontent.com/Atc1501/thai-token-optimizer/main/SKILL.md"
$LocalSkillPath = if ($PSScriptRoot) { Join-Path $PSScriptRoot "SKILL.md" } else { "" }

$SkillDirs = @(
    "$HOME\.gemini\config\skills\thai-token-optimizer",
    "$HOME\.agents\skills\thai-token-optimizer",
    "$HOME\.claude\skills\thai-token-optimizer"
)

$GlobalRuleFiles = @(
    "$HOME\.gemini\config\GEMINI.md",
    "$HOME\.claude\CLAUDE.md",
    "$HOME\.agents\AGENTS.md"
)

$StartMarker = "<!-- THAI_TOKEN_OPTIMIZER_START -->"
$EndMarker   = "<!-- THAI_TOKEN_OPTIMIZER_END -->"

$RuleBlock = @"
$StartMarker
# Thai Token Optimizer v2.1 (Always-On Golden Ratio)

When the user communicates in Thai:
1. **Backend Reasoning**: Conduct all internal thinking (`<thinking>`), planning, and technical analysis in natural English (saves ~70% reasoning tokens while keeping 100% intelligence).
2. **Direct Thai Output**: Reply in natural, direct Thai. Omit ceremonial greetings and never echo the user's question back. Use bullet points or numbered steps.
3. **Technical Terms**: Keep coding, architecture, and system terms in standard English (`Config`, `Database`, `API`, `Function`).
4. **Code & Git Hygiene**: Write all inline code comments, docstrings, logs, and Git commit messages in concise English (use Thai only for user-facing UI strings).
5. **Subagents & Memory**: Communicate with subagents and store internal scratchpads/memory in concise English; summarize to the user in Thai.
$EndMarker
"@

function Install-SkillFiles {
    foreach ($Dir in $SkillDirs) {
        if (-not (Test-Path $Dir)) {
            New-Item -ItemType Directory -Force -Path $Dir | Out-Null
        }
        $TargetFile = Join-Path $Dir "SKILL.md"
        if ($LocalSkillPath -and (Test-Path $LocalSkillPath)) {
            Copy-Item -Force $LocalSkillPath $TargetFile
        } else {
            Invoke-RestMethod -Uri $SkillUrl -OutFile $TargetFile
        }
    }
    Write-Host "  [OK] Installed On-Demand Skill (@thai-token-optimizer)" -ForegroundColor Green
}

function Remove-AlwaysOnRule {
    foreach ($File in $GlobalRuleFiles) {
        if (Test-Path $File) {
            $Content = [System.IO.File]::ReadAllText($File, $Utf8NoBom)
            if ($Content -and $Content.Contains($StartMarker)) {
                $Pattern = "(?s)\r?\n?$([regex]::Escape($StartMarker)).*?$([regex]::Escape($EndMarker))\r?\n?"
                $Cleaned = [regex]::Replace($Content, $Pattern, "").TrimEnd()
                if ($Cleaned.Length -gt 0) {
                    [System.IO.File]::WriteAllText($File, ($Cleaned + "`r`n"), $Utf8NoBom)
                } else {
                    [System.IO.File]::WriteAllText($File, "", $Utf8NoBom)
                }
                Write-Host "  [OK] Removed Always-On Rule from -> $File" -ForegroundColor Yellow
            }
        }
    }
}

function Enable-AlwaysOnRule {
    Remove-AlwaysOnRule | Out-Null
    foreach ($File in $GlobalRuleFiles) {
        $Parent = Split-Path -Parent $File
        if (-not (Test-Path $Parent)) {
            New-Item -ItemType Directory -Force -Path $Parent | Out-Null
        }
        if (Test-Path $File) {
            $Existing = [System.IO.File]::ReadAllText($File, $Utf8NoBom)
            if ($Existing -and $Existing.Trim().Length -gt 0) {
                $NewContent = $Existing.TrimEnd() + "`r`n`r`n" + $RuleBlock + "`r`n"
            } else {
                $NewContent = $RuleBlock + "`r`n"
            }
        } else {
            $NewContent = $RuleBlock + "`r`n"
        }
        [System.IO.File]::WriteAllText($File, $NewContent, $Utf8NoBom)
        Write-Host "  [OK] Enabled Always-On Global Rule -> $File" -ForegroundColor Green
    }
}

function Show-Status {
    $SkillInstalled = Test-Path "$HOME\.gemini\config\skills\thai-token-optimizer\SKILL.md"
    $AlwaysOnActive = $false
    if (Test-Path "$HOME\.gemini\config\GEMINI.md") {
        $Raw = [System.IO.File]::ReadAllText("$HOME\.gemini\config\GEMINI.md", $Utf8NoBom)
        if ($Raw -and $Raw.Contains($StartMarker)) { $AlwaysOnActive = $true }
    }
    Write-Host "`n============================================================" -ForegroundColor Cyan
    Write-Host " THAI TOKEN OPTIMIZER v2.1 - CURRENT STATUS" -ForegroundColor Cyan
    Write-Host "============================================================" -ForegroundColor Cyan
    Write-Host ("  * Mode 1: On-Demand Skill (@thai-token-optimizer) : " + ($(if ($SkillInstalled) { "INSTALLED" } else { "NOT INSTALLED" })))
    Write-Host ("  * Mode 2: Always-On Global Rule (Auto every chat) : " + ($(if ($AlwaysOnActive) { "ACTIVE (ON)" } else { "INACTIVE (OFF)" })))
    Write-Host "============================================================`n" -ForegroundColor Cyan
}

if ($Mode -eq "menu") {
    Show-Status
    Write-Host "Select Activation Mode:" -ForegroundColor White
    Write-Host "  [1] Mode 1: On-Demand Skill Only (Invoke manually via @thai-token-optimizer)" -ForegroundColor Cyan
    Write-Host "  [2] Mode 2: Always-On Global Rule (Auto-active in every chat from Turn 0)" -ForegroundColor Green
    Write-Host "  [3] Disable Always-On (Revert to Mode 1: On-Demand Skill Only)" -ForegroundColor Yellow
    Write-Host "  [4] Uninstall All (Remove both Always-On Rule and Skill files)" -ForegroundColor Red
    Write-Host "  [5] Check Status Only" -ForegroundColor Gray
    $Choice = Read-Host "`nEnter number (1-5)"
    switch ($Choice) {
        "1" { $Mode = "skill" }
        "2" { $Mode = "always-on" }
        "3" { $Mode = "disable" }
        "4" { $Mode = "uninstall" }
        default { $Mode = "status" }
    }
}

switch ($Mode) {
    "skill" {
        Write-Host "`n[Switching to Mode 1: On-Demand Skill Only]..." -ForegroundColor Cyan
        Install-SkillFiles
        Remove-AlwaysOnRule
        Show-Status
    }
    "always-on" {
        Write-Host "`n[Switching to Mode 2: Always-On Global Rule + Skill]..." -ForegroundColor Green
        Install-SkillFiles
        Enable-AlwaysOnRule
        Show-Status
    }
    "disable" {
        Write-Host "`n[Disabling Always-On Global Rule (Keeping @thai-token-optimizer Skill)]..." -ForegroundColor Yellow
        Remove-AlwaysOnRule
        Show-Status
    }
    "uninstall" {
        Write-Host "`n[Uninstalling Thai Token Optimizer Completely]..." -ForegroundColor Red
        Remove-AlwaysOnRule
        foreach ($Dir in $SkillDirs) {
            if (Test-Path $Dir) { Remove-Item -Recurse -Force $Dir }
        }
        Show-Status
    }
    "status" {
        Show-Status
    }
}
