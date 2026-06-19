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
为安徽省钢城马鞍山市设计城市标识系统 logo，要求现代、公共文化传播、不要堆砌地标。
```

DESIGNOSFORGE v2.1.0 uses a mathematical DesignKernel, PromptPacketV2, independent LoopPromptPack, LoopEngineeringOS, aesthetic quality gates, training-aware case memory, failure memory, project-context routing, EnvArt CADMCP source-fidelity routing, photography identity locks, image-generation confirmation gates, text/encoding health checks, and GitHub/GitOps release planning.

## Loop Engineering Smoke Test

Use this when you need to verify durable loop routing:

```powershell
py -m app.cli kernel loop-engineering "Loop Engineering 调度 issue CI，worktree 并行隔离，validator 验收，写入长期记忆"
```

## Math Audit

Use this when you want to see why the system chose a route or candidate direction:

```powershell
py -m app.cli kernel math-audit "拯救课堂纪实照片，不要改变人物本来的面貌形象"
```
