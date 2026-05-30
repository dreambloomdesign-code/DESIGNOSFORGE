param(
    [string]$Path = "D:\DESIGNOSFORGE\DESIGNOSFORGE_v1.4_source_for_codex"
)

$ErrorActionPreference = "Stop"
$markers = @(0xFFFD, 0x951D, 0x9286, 0x9422, 0x7EDB, 0x6D63, 0x00E5, 0x00E6, 0x00E7) |
    ForEach-Object { [string][char]$_ }
$extensions = @(".md", ".py", ".json", ".toml", ".yaml", ".yml", ".ps1")
$issues = @()
$mojibakeCount = 0
$longLineCount = 0

if (-not (Test-Path -LiteralPath $Path)) {
    throw "Path does not exist: $Path"
}

$files = Get-ChildItem -LiteralPath $Path -Recurse -File |
    Where-Object { $extensions -contains $_.Extension.ToLowerInvariant() -and $_.FullName -notmatch "\\.git\\" }

foreach ($file in $files) {
    $content = Get-Content -LiteralPath $file.FullName -Raw -Encoding UTF8
    foreach ($marker in $markers) {
        if ($content.Contains($marker)) {
            $issues += [ordered]@{ file = $file.FullName; type = "mojibake_marker"; marker = $marker }
            $mojibakeCount += 1
        }
    }
    $lineNumber = 0
    foreach ($line in ($content -split "`r?`n")) {
        $lineNumber += 1
        if ($line.Length -gt 220) {
            $issues += [ordered]@{ file = $file.FullName; type = "long_line"; line = $lineNumber; length = $line.Length }
            $longLineCount += 1
        }
    }
}

[ordered]@{
    path = $Path
    scanned_files = $files.Count
    issue_count = $issues.Count
    mojibake_count = $mojibakeCount
    long_line_count = $longLineCount
    issues = $issues
    ok = $mojibakeCount -eq 0
} | ConvertTo-Json -Depth 6
