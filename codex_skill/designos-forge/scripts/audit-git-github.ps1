param(
    [string]$Repo = "D:\DESIGNOSFORGE\DESIGNOSFORGE_v1.4_source_for_codex"
)

$ErrorActionPreference = "Stop"

function Run-Command {
    param([string[]]$Command, [string]$WorkingDirectory)
    $psi = [System.Diagnostics.ProcessStartInfo]::new()
    $psi.FileName = $Command[0]
    if ($Command.Count -gt 1) {
        $psi.Arguments = (($Command[1..($Command.Count - 1)] | ForEach-Object {
            if ($_ -match '\s') { '"' + ($_ -replace '"', '\"') + '"' } else { $_ }
        }) -join " ")
    }
    $psi.WorkingDirectory = $WorkingDirectory
    $psi.RedirectStandardOutput = $true
    $psi.RedirectStandardError = $true
    $psi.UseShellExecute = $false
    $process = [System.Diagnostics.Process]::Start($psi)
    $stdout = $process.StandardOutput.ReadToEnd()
    $stderr = $process.StandardError.ReadToEnd()
    $process.WaitForExit()
    $output = (($stdout + $stderr) | Out-String).Trim()
    [ordered]@{
        command = ($Command -join " ")
        exit_code = $process.ExitCode
        output = $output
    }
}

$git = Get-Command git -ErrorAction SilentlyContinue
$gh = Get-Command gh -ErrorAction SilentlyContinue
$exists = Test-Path -LiteralPath $Repo

$status = [ordered]@{
    repo = $Repo
    repo_exists = $exists
    git_available = $null -ne $git
    gh_available = $null -ne $gh
    git_status = $null
    git_branch = $null
    git_remotes = $null
    recommendation = ""
}

if (-not $exists) {
    $status.recommendation = "Create or extract the source package before GitHub management."
} elseif (-not $git) {
    $status.recommendation = "Install Git before repository management."
} else {
    $inside = Run-Command @("git", "rev-parse", "--is-inside-work-tree") $Repo
    if ($inside.exit_code -ne 0) {
        $status.git_status = $inside.output
        $status.recommendation = "Initialize git, create an initial commit, add GitHub remote, then push a release branch."
    } else {
        $status.git_status = (Run-Command @("git", "status", "--short") $Repo).output
        $status.git_branch = (Run-Command @("git", "branch", "--show-current") $Repo).output
        $status.git_remotes = (Run-Command @("git", "remote", "-v") $Repo).output
        $status.recommendation = "Use release branch, validation, PR, tag, and GitHub Release workflow."
    }
}

$status | ConvertTo-Json -Depth 5
