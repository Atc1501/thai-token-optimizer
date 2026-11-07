# Automated Test Suite for install.ps1 (5 Core Safety Scenarios)
$ErrorActionPreference = "Stop"
$Utf8 = New-Object System.Text.UTF8Encoding($false)

$RepoRoot = Split-Path -Parent $PSScriptRoot
$Installer = Join-Path $RepoRoot "install.ps1"
$TestSandbox = Join-Path $PSScriptRoot "sandbox_config"

function Reset-Sandbox {
    if (Test-Path $TestSandbox) {
        Remove-Item -Path $TestSandbox -Recurse -Force
    }
    New-Item -ItemType Directory -Path $TestSandbox | Out-Null
}

function Assert-True {
    param([bool]$Condition, [string]$Message)
    if (-not $Condition) {
        throw "TEST FAILED: $Message"
    }
    Write-Host "  [PASS] $Message" -ForegroundColor Green
}

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host " RUNNING INSTALLER SAFETY TEST SUITE (5 SCENARIOS)" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan

# ------------------------------------------------------------------
# TEST 1: Fresh Installation
# ------------------------------------------------------------------
Write-Host "`n[Test 1] Fresh Installation" -ForegroundColor Yellow
Reset-Sandbox
& $Installer -Mode "always-on" -BaseConfigDir $TestSandbox | Out-Null

$GeminiFile = Join-Path $TestSandbox "GEMINI.md"
$SkillFile  = Join-Path $TestSandbox "skills\thai-token-optimizer\SKILL.md"
Assert-True (Test-Path $SkillFile) "SKILL.md created on fresh install"
Assert-True (Test-Path $GeminiFile) "GEMINI.md created on fresh install"
$Content1 = [System.IO.File]::ReadAllText($GeminiFile, $Utf8)
Assert-True ($Content1.Contains("<!-- THAI_TOKEN_OPTIMIZER_START -->") -and $Content1.Contains("<!-- THAI_TOKEN_OPTIMIZER_END -->")) "GEMINI.md contains START and END markers"

# ------------------------------------------------------------------
# TEST 2: Idempotent Re-install (No Duplicate Rules + Backup Created)
# ------------------------------------------------------------------
Write-Host "`n[Test 2] Idempotent Re-installation & Backup Creation" -ForegroundColor Yellow
& $Installer -Mode "always-on" -BaseConfigDir $TestSandbox | Out-Null
$Content2 = [System.IO.File]::ReadAllText($GeminiFile, $Utf8)
$StartCount = ([regex]::Matches($Content2, "<!-- THAI_TOKEN_OPTIMIZER_START -->")).Count
Assert-True ($StartCount -eq 1) "Re-running always-on produces exactly 1 rule block (count = $StartCount)"
Assert-True (Test-Path "$GeminiFile.bak") "GEMINI.md.bak backup created before modification"
Assert-True (Test-Path "$SkillFile.bak") "SKILL.md.bak backup created before overwrite"

# ------------------------------------------------------------------
# TEST 3: Uninstall Preserves Surrounding User Content (Top & Bottom)
# ------------------------------------------------------------------
Write-Host "`n[Test 3] Uninstall Preserves User Rules Above & Below Block" -ForegroundColor Yellow
Reset-Sandbox
$InitialUserDoc = @"
# User Rule Top
Always keep top rule intact.

<!-- THAI_TOKEN_OPTIMIZER_START -->
# Thai Token Optimizer Guidelines
Old content inside markers
<!-- THAI_TOKEN_OPTIMIZER_END -->

# User Rule Bottom
Always keep bottom rule intact.
"@
[System.IO.File]::WriteAllText($GeminiFile, $InitialUserDoc, $Utf8)
& $Installer -Mode "always-on" -BaseConfigDir $TestSandbox | Out-Null
& $Installer -Mode "uninstall" -BaseConfigDir $TestSandbox | Out-Null

$AfterUninstall = [System.IO.File]::ReadAllText($GeminiFile, $Utf8)
Assert-True ($AfterUninstall.Contains("# User Rule Top") -and $AfterUninstall.Contains("Always keep top rule intact.")) "Top user rule preserved after uninstall"
Assert-True ($AfterUninstall.Contains("# User Rule Bottom") -and $AfterUninstall.Contains("Always keep bottom rule intact.")) "Bottom user rule preserved after uninstall"
Assert-True (-not $AfterUninstall.Contains("THAI_TOKEN_OPTIMIZER")) "Thai Token Optimizer block cleanly removed"
Assert-True (-not (Test-Path $SkillFile)) "Manifest-tracked SKILL.md removed on uninstall"

# ------------------------------------------------------------------
# TEST 4: Missing or Duplicate Marker Must Refuse Modification
# ------------------------------------------------------------------
Write-Host "`n[Test 4] Corrupted / Incomplete Marker Rejection" -ForegroundColor Yellow
Reset-Sandbox
$CorruptedDoc = @"
# Important User Rule
Do not lose this line.
<!-- THAI_TOKEN_OPTIMIZER_START -->
# Thai Token Optimizer Guidelines
Missing end marker here!
"@
[System.IO.File]::WriteAllText($GeminiFile, $CorruptedDoc, $Utf8)

$ThrewError = $false
try {
    & $Installer -Mode "disable" -BaseConfigDir $TestSandbox | Out-Null
} catch {
    $ThrewError = $true
}
$AfterCorrupted = [System.IO.File]::ReadAllText($GeminiFile, $Utf8)
Assert-True $ThrewError "Installer rejected file with missing END marker"
Assert-True ($AfterCorrupted -eq $CorruptedDoc) "Corrupted GEMINI.md was left 100% untouched"

# ------------------------------------------------------------------
# TEST 5: Legacy Markerless Migration (Exact Match vs Ambiguous)
# ------------------------------------------------------------------
Write-Host "`n[Test 5] Legacy Version Migration (Markerless -> Marker-Wrapped)" -ForegroundColor Yellow
Reset-Sandbox
$LegacyDoc = @"
# Brain + Worker Rule
Keep this header.

# Thai Token Optimizer Guidelines
When the user communicates in Thai:
1. Conduct internal reasoning, planning, and subagent notes in natural English.
2. Reply in direct, natural Thai using bullet points or numbered steps without repeating the question.
3. Keep technical terms, code comments, logs, and commit messages in concise English (use Thai only for UI text).
4. Keep mock data compact (3-4 items) and use targeted edits instead of repeating full unchanged files.

# Bottom Custom Rule
Keep this footer too.
"@
[System.IO.File]::WriteAllText($GeminiFile, $LegacyDoc, $Utf8)
& $Installer -Mode "always-on" -BaseConfigDir $TestSandbox | Out-Null

$MigratedDoc = [System.IO.File]::ReadAllText($GeminiFile, $Utf8)
Assert-True ($MigratedDoc.Contains("# Brain + Worker Rule")) "Legacy migration preserved top rule"
Assert-True ($MigratedDoc.Contains("# Bottom Custom Rule")) "Legacy migration preserved bottom rule"
Assert-True ($MigratedDoc.Contains("<!-- THAI_TOKEN_OPTIMIZER_START -->") -and $MigratedDoc.Contains("<!-- THAI_TOKEN_OPTIMIZER_END -->")) "Legacy block upgraded to START/END markers"

# Clean up test sandbox
Reset-Sandbox
Remove-Item -Path $TestSandbox -Force

Write-Host "`n============================================================" -ForegroundColor Green
Write-Host " ALL 5 TEST SCENARIOS PASSED SUCCESSFULLY!" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green
