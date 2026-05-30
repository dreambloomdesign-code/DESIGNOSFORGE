# Codex Skill Install

Install the DESIGNOSFORGE skill by copying the bundled skill folder into your Codex skills directory.

## Windows

```powershell
$src = "codex_skill\designos-forge"
$dst = "$env:USERPROFILE\.codex\skills\designos-forge"
New-Item -ItemType Directory -Force -Path $dst | Out-Null
Copy-Item -Recurse -Force "$src\*" $dst
```

Validate:

```powershell
$env:PYTHONUTF8='1'
py -3 "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "$env:USERPROFILE\.codex\skills\designos-forge"
```

## Usage

In Codex, say:

```text
调用DesignForge
```

or ask for a design workflow such as:

```text
做一个高端品牌 VI 方案，避免画面细碎脏乱，文字必须准确。
```

DESIGNOSFORGE v1.5 uses aesthetic quality gates, PromptPacket v1.5, image-generation confirmation gates, text/encoding health checks, and GitHub/GitOps release planning.
