# Thai Token Optimizer - Safe Local Installer
# Features:
# - Strict START/END marker validation (aborts on malformed/duplicate markers)
# - Automatic .bak backup before modifying GEMINI.md or existing SKILL.md
# - Atomic write via temporary file (.tmp) with verification before replacement
# - Exact-match legacy migration for older markerless installations
# - Uninstall removes only verified skill-owned files

param(
    [ValidateSet("menu", "skill", "always-on", "disable", "uninstall", "status")]
    [string]$Mode = "menu",

    [string]$BaseConfigDir = "$HOME\.gemini\config"
)

$ErrorActionPreference = "Stop"
$Utf8Encoding = New-Object System.Text.UTF8Encoding($false)

$SourceSkill = Join-Path $PSScriptRoot "SKILL.md"
$SkillDir = Join-Path $BaseConfigDir "skills\thai-token-optimizer"
$SkillFile = Join-Path $SkillDir "SKILL.md"
$SkillBackup = Join-Path $SkillDir "SKILL.md.bak"
$ManifestFile = Join-Path $SkillDir ".installed_manifest"
$GlobalRuleFile = Join-Path $BaseConfigDir "GEMINI.md"
$GlobalBackupFile = Join-Path $BaseConfigDir "GEMINI.md.bak"

$StartMarker = "<!-- THAI_TOKEN_OPTIMIZER_START -->"
$EndMarker   = "<!-- THAI_TOKEN_OPTIMIZER_END -->"

$ManagedBlock = @(
    $StartMarker,
    "# Thai Token Optimizer Guidelines",
    "When the user communicates in Thai:",
    "1. Conduct internal reasoning, planning, and subagent notes in natural English.",
    "2. Reply in direct, natural Thai using bullet points or numbered steps without repeating the question.",
    "3. Keep technical terms, code comments, logs, and commit messages in concise English (use Thai only for UI text).",
    "4. Keep mock data compact (3-4 items) and use targeted edits instead of repeating full unchanged files.",
    $EndMarker
) -join "`r`n"

$ExactLegacyBlock = @(
    "# Thai Token Optimizer Guidelines",
    "When the user communicates in Thai:",
    "1. Conduct internal reasoning, planning, and subagent notes in natural English.",
    "2. Reply in direct, natural Thai using bullet points or numbered steps without repeating the question.",
    "3. Keep technical terms, code comments, logs, and commit messages in concise English (use Thai only for UI text).",
    "4. Keep mock data compact (3-4 items) and use targeted edits instead of repeating full unchanged files."
)

function Write-FileAtomically {
    param(
        [Parameter(Mandatory = $true)][string]$FilePath,
        [Parameter(Mandatory = $true)][AllowEmptyString()][string]$NewContent,
        [Parameter(Mandatory = $true)][string]$BackupPath
    )

    $ParentDir = Split-Path -Parent $FilePath
    if (-not (Test-Path $ParentDir)) {
        New-Item -ItemType Directory -Path $ParentDir | Out-Null
    }

    # 1. Backup existing file before any write
    if (Test-Path $FilePath) {
        Copy-Item -Path $FilePath -Destination $BackupPath -Force
    }

    # 2. Write to temporary file first
    $TempFile = "$FilePath.tmp"
    [System.IO.File]::WriteAllText($TempFile, $NewContent, $Utf8Encoding)

    # 3. Verify temporary file was written and matches expected content
    if (-not (Test-Path $TempFile)) {
        throw "Safety check failed: Temporary file '$TempFile' was not created."
    }
    $VerifyContent = [System.IO.File]::ReadAllText($TempFile, $Utf8Encoding)
    if ($VerifyContent -ne $NewContent) {
        Remove-Item -Path $TempFile -ErrorAction SilentlyContinue
        throw "Safety check failed: Temporary file content verification mismatch."
    }

    # 4. Replace target file with verified temporary file
    Move-Item -Path $TempFile -Destination $FilePath -Force
}

function Copy-LocalSkill {
    if (-not (Test-Path $SourceSkill)) {
        throw "Source file not found: $SourceSkill"
    }
    if (-not (Test-Path $SkillDir)) {
        New-Item -ItemType Directory -Path $SkillDir | Out-Null
    }

    # Backup existing SKILL.md if present
    if (Test-Path $SkillFile) {
        Copy-Item -Path $SkillFile -Destination $SkillBackup -Force
        Write-Host "  [Backup] Backed up existing SKILL.md -> $SkillBackup" -ForegroundColor DarkGray
    }

    Copy-Item -Path $SourceSkill -Destination $SkillFile -Force
    [System.IO.File]::WriteAllText($ManifestFile, "SKILL.md`r`n", $Utf8Encoding)
    Write-Host "  [OK] Installed SKILL.md -> $SkillFile" -ForegroundColor Green
}

function Get-ValidatedContentWithoutSection {
    param([string]$RawContent)

    if ([string]::IsNullOrEmpty($RawContent)) {
        return ""
    }

    $StartMatches = [regex]::Matches($RawContent, [regex]::Escape($StartMarker))
    $EndMatches   = [regex]::Matches($RawContent, [regex]::Escape($EndMarker))

    # Strict Marker Validation: Reject incomplete or duplicate markers
    if ($StartMatches.Count -ne $EndMatches.Count) {
        throw "Marker integrity error in '$GlobalRuleFile': Found $($StartMatches.Count) START marker(s) and $($EndMatches.Count) END marker(s). Aborting to protect user data."
    }
    if ($StartMatches.Count -gt 1) {
        throw "Marker integrity error in '$GlobalRuleFile': Found duplicate ($($StartMatches.Count)) START/END marker blocks. Aborting to protect user data."
    }

    # Case A: Standard Marker-bounded removal
    if ($StartMatches.Count -eq 1) {
        $StartIndex = $StartMatches[0].Index
        $EndIndex   = $EndMatches[0].Index + $EndMatches[0].Length
        if ($EndIndex -le $StartIndex) {
            throw "Marker integrity error in '$GlobalRuleFile': END marker appears before START marker. Aborting to protect user data."
        }

        $Before = $RawContent.Substring(0, $StartIndex)
        $After  = $RawContent.Substring($EndIndex)

        # Clean up surrounding newline join without altering user content
        $BeforeTrimmed = $Before.TrimEnd("`r", "`n")
        $AfterTrimmed  = $After.TrimStart("`r", "`n")

        if ($BeforeTrimmed.Length -gt 0 -and $AfterTrimmed.Length -gt 0) {
            return $BeforeTrimmed + "`r`n`r`n" + $AfterTrimmed
        } elseif ($BeforeTrimmed.Length -gt 0) {
            return $BeforeTrimmed + "`r`n"
        } elseif ($AfterTrimmed.Length -gt 0) {
            return $AfterTrimmed
        } else {
            return ""
        }
    }

    # Case B: Legacy Migration (No markers present, check if legacy heading exists)
    if ($RawContent -match "(?m)^# Thai Token Optimizer") {
        $Normalized = $RawContent -replace "`r`n", "`n"
        $LegacyNormalized = ($ExactLegacyBlock -join "`n")

        if ($Normalized.Contains($LegacyNormalized)) {
            $Migrated = $Normalized.Replace($LegacyNormalized, "").Trim()
            if ($Migrated.Length -gt 0) {
                return ($Migrated -replace "`n", "`r`n") + "`r`n"
            } else {
                return ""
            }
        } else {
            throw "Legacy migration error in '$GlobalRuleFile': Found '# Thai Token Optimizer' heading without markers, but its content does not match the known legacy signature. Please add START/END markers manually."
        }
    }

    return $RawContent
}

function Remove-GlobalSection {
    if (-not (Test-Path $GlobalRuleFile)) {
        return
    }
    $RawContent = [System.IO.File]::ReadAllText($GlobalRuleFile, $Utf8Encoding)
    $CleanedContent = Get-ValidatedContentWithoutSection -RawContent $RawContent

    if ($CleanedContent -ne $RawContent) {
        Write-FileAtomically -FilePath $GlobalRuleFile -NewContent $CleanedContent -BackupPath $GlobalBackupFile
        Write-Host "  [Backup] Backed up GEMINI.md -> $GlobalBackupFile" -ForegroundColor DarkGray
        Write-Host "  [OK] Removed Thai Token Optimizer section from $GlobalRuleFile" -ForegroundColor Yellow
    }
}

function Add-GlobalSection {
    $ExistingContent = ""
    if (Test-Path $GlobalRuleFile) {
        $RawContent = [System.IO.File]::ReadAllText($GlobalRuleFile, $Utf8Encoding)
        $ExistingContent = Get-ValidatedContentWithoutSection -RawContent $RawContent
    }

    $TrimmedExisting = $ExistingContent.TrimEnd("`r", "`n")
    if ($TrimmedExisting.Length -gt 0) {
        $NewContent = $TrimmedExisting + "`r`n`r`n" + $ManagedBlock + "`r`n"
    } else {
        $NewContent = $ManagedBlock + "`r`n"
    }

    Write-FileAtomically -FilePath $GlobalRuleFile -NewContent $NewContent -BackupPath $GlobalBackupFile
    if (Test-Path $GlobalBackupFile) {
        Write-Host "  [Backup] Backed up GEMINI.md -> $GlobalBackupFile" -ForegroundColor DarkGray
    }
    Write-Host "  [OK] Enabled Always-On Global Rule in $GlobalRuleFile" -ForegroundColor Green
}

function Uninstall-SkillFiles {
    # Only delete files verified by manifest
    if (Test-Path $ManifestFile) {
        if (Test-Path $SkillFile) {
            Remove-Item -Path $SkillFile
            Write-Host "  [OK] Removed installed $SkillFile" -ForegroundColor Yellow
        }
        Remove-Item -Path $ManifestFile
    } elseif (Test-Path $SkillFile) {
        Write-Warning "Skipped deleting '$SkillFile' because installation manifest was not found."
    }
}

function Show-CurrentStatus {
    $Installed = Test-Path $SkillFile
    $GlobalOn = $false
    if (Test-Path $GlobalRuleFile) {
        $Raw = [System.IO.File]::ReadAllText($GlobalRuleFile, $Utf8Encoding)
        if ($Raw.Contains($StartMarker) -and $Raw.Contains($EndMarker)) {
            $GlobalOn = $true
        }
    }
    Write-Host "`n--- Thai Token Optimizer Status ---" -ForegroundColor Cyan
    Write-Host "  Skill (@thai-token-optimizer) : $(if ($Installed) { 'INSTALLED' } else { 'NOT INSTALLED' })"
    Write-Host "  Global Rule (GEMINI.md)       : $(if ($GlobalOn) { 'ON' } else { 'OFF' })`n"
}

if ($Mode -eq "menu") {
    Show-CurrentStatus
    Write-Host "1 = Install Skill Only (@thai-token-optimizer) [Recommended / Safest]"
    Write-Host "2 = Install Skill + Enable Global Rule (Always-On in GEMINI.md)"
    Write-Host "3 = Disable Global Rule (Keep Skill)"
    Write-Host "4 = Uninstall Skill & Global Rule"
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
    "uninstall" { Remove-GlobalSection; Uninstall-SkillFiles; Show-CurrentStatus }
    "status"    { Show-CurrentStatus }
}
