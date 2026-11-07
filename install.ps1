# Thai Token Optimizer - Local Setup Script
# Copies SKILL.md from the cloned repository folder to local skill directories.

param(
    [ValidateSet("menu", "skill", "always-on", "disable", "uninstall", "status")]
    [string]$Mode = "menu"
)

$SourceSkill = Join-Path $PSScriptRoot "SKILL.md"
$SkillDirs = @(
    "$HOME\.gemini\config\skills\thai-token-optimizer",
    "$HOME\.agents\skills\thai-token-optimizer",
    "$HOME\.claude\skills\thai-token-optimizer"
)

$GlobalRuleFile = "$HOME\.gemini\config\GEMINI.md"
$SectionHeader = "# Thai Token Optimizer Guidelines"

$RuleText = @"

# Thai Token Optimizer Guidelines
When the user communicates in Thai:
1. Conduct internal reasoning, planning, and subagent notes in natural English.
2. Reply in direct, natural Thai using bullet points or numbered steps without repeating the question.
3. Keep technical terms, code comments, logs, and commit messages in concise English (use Thai only for UI text).
4. Keep mock data compact (3-4 items) and use targeted edits instead of repeating full unchanged files.
"@

function Copy-LocalSkill {
    foreach ($Dir in $SkillDirs) {
        if (-not (Test-Path $Dir)) {
            New-Item -ItemType Directory -Force -Path $Dir | Out-Null
        }
        Copy-Item -Force -Path $SourceSkill -Destination (Join-Path $Dir "SKILL.md")
    }
    Write-Host "  [OK] Copied SKILL.md to local skill folders." -ForegroundColor Green
}

function Remove-GlobalSection {
    if (Test-Path $GlobalRuleFile) {
        $Lines = Get-Content -Path $GlobalRuleFile -Encoding UTF8
        $Filtered = @()
        $Skip = $false
        foreach ($Line in $Lines) {
            if ($Line -match "^# Thai Token Optimizer" -or $Line -match "THAI_TOKEN_OPTIMIZER_START") {
                $Skip = $true
            }
            if (-not $Skip) {
                $Filtered += $Line
            }
            if ($Line -match "THAI_TOKEN_OPTIMIZER_END") {
                $Skip = $false
            }
        }
        Set-Content -Path $GlobalRuleFile -Value $Filtered -Encoding UTF8
        Write-Host "  [OK] Disabled global rule in $GlobalRuleFile" -ForegroundColor Yellow
    }
}

function Add-GlobalSection {
    Remove-GlobalSection
    Add-Content -Path $GlobalRuleFile -Value $RuleText -Encoding UTF8
    Write-Host "  [OK] Added global rule to $GlobalRuleFile" -ForegroundColor Green
}

function Show-CurrentStatus {
    $Installed = Test-Path "$HOME\.gemini\config\skills\thai-token-optimizer\SKILL.md"
    $GlobalOn = $false
    if (Test-Path $GlobalRuleFile) {
        $Text = Get-Content -Raw -Path $GlobalRuleFile -Encoding UTF8
        if ($Text -match "Thai Token Optimizer") { $GlobalOn = $true }
    }
    Write-Host "`n--- Thai Token Optimizer Status ---" -ForegroundColor Cyan
    Write-Host "  Skill (@thai-token-optimizer) : $(if ($Installed) { 'INSTALLED' } else { 'NOT INSTALLED' })"
    Write-Host "  Global Rule (GEMINI.md)       : $(if ($GlobalOn) { 'ON' } else { 'OFF' })`n"
}

if ($Mode -eq "menu") {
    Show-CurrentStatus
    Write-Host "1 = Install Skill Only (@thai-token-optimizer)"
    Write-Host "2 = Install Skill + Enable Global Rule (Always-On)"
    Write-Host "3 = Disable Global Rule (Keep Skill)"
    Write-Host "4 = Uninstall All"
    $Choice = Read-Host "Select (1-4)"
    switch ($Choice) {
        "1" { $Mode = "skill" }
        "2" { $Mode = "always-on" }
        "3" { $Mode = "disable" }
        "4" { $Mode = "uninstall" }
        default { $Mode = "status" }
    }
}

switch ($Mode) {
    "skill"     { Copy-LocalSkill; Remove-GlobalSection; Show-CurrentStatus }
    "always-on" { Copy-LocalSkill; Add-GlobalSection; Show-CurrentStatus }
    "disable"   { Remove-GlobalSection; Show-CurrentStatus }
    "uninstall" {
        Remove-GlobalSection
        foreach ($Dir in $SkillDirs) {
            if (Test-Path $Dir) { Remove-Item -Recurse -Force -Path $Dir }
        }
        Show-CurrentStatus
    }
    "status"    { Show-CurrentStatus }
}
