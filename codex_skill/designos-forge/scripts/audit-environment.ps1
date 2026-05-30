param(
    [string]$SkillRoot = (Join-Path $env:USERPROFILE ".codex\skills"),
    [string]$Workspace = "D:\DESIGNOSFORGE"
)

$ErrorActionPreference = "Stop"

function Test-PathInfo {
    param([string]$Path)
    [ordered]@{
        path = $Path
        exists = Test-Path -LiteralPath $Path
    }
}

$skillDirs = @()
if (Test-Path -LiteralPath $SkillRoot) {
    $skillDirs = Get-ChildItem -LiteralPath $SkillRoot -Directory -Force |
        Where-Object { $_.Name -ne ".system" } |
        Sort-Object Name |
        ForEach-Object { $_.Name }
}

$pythonCommands = @()
foreach ($cmd in @("py", "python")) {
    $found = Get-Command $cmd -ErrorAction SilentlyContinue
    if ($found) {
        $pythonCommands += [ordered]@{ name = $cmd; source = $found.Source }
    }
}

$bundledPython = "C:\Users\taojian\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
$bundledNode = "C:\Users\taojian\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe"

[ordered]@{
    timestamp = (Get-Date).ToString("o")
    skill_root = $SkillRoot
    workspace = $Workspace
    installed_skills = $skillDirs
    designos_skill = Test-PathInfo (Join-Path $SkillRoot "designos-forge")
    source_zip = Test-PathInfo "C:\Users\taojian\Downloads\DESIGNOSFORGE_v1.4_source_for_codex.zip"
    fixed_source = Test-PathInfo (Join-Path $Workspace "DESIGNOSFORGE_v1.4_source_for_codex")
    fixed_source_zip = Test-PathInfo (Join-Path $Workspace "DESIGNOSFORGE_v1.4_source_for_codex_fixed.zip")
    python_commands = $pythonCommands
    bundled_python = Test-PathInfo $bundledPython
    bundled_node = Test-PathInfo $bundledNode
    validation_hint = "Set PYTHONUTF8=1 before validating Chinese skill files on Windows."
} | ConvertTo-Json -Depth 6
