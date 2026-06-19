# DESIGNOSFORGE v2.1.0 Release Notes

DESIGNOSFORGE v2.1.0 introduces system-level Loop Engineering for long-running, tool-connected, validated agent workflows.

## Highlights

- Adds `LoopEngineeringBlueprintBuilder`.
- Adds `LoopEngineeringOS` to the capability and skill registry.
- Adds `kernel loop-engineering` CLI output.
- Extends `DesignKernelPlan` with a `loop_engineering` side channel.
- Keeps `PromptPacketV2` and `LoopPromptPack` independent and backward compatible.
- Defines six durable loop layers: scheduler, worktree isolation, skill context, external connectors, validation gate, and persistent memory.
- Strengthens GitHub/release planning around compile, source validation, CLI smoke checks, tests, PR notes, and rollback.

## Validation

```powershell
$env:PYTHONPATH='.'
$env:PYTHONUTF8='1'
py -m compileall app tests tools
py -m app.cli capabilities
py -m app.cli kernel loop-engineering "Loop Engineering 调度 issue CI，worktree 并行隔离，validator 验收，写入长期记忆"
py -m app.cli kernel loop-prompt "create a design prompt with three loop iterations and self critique"
py -m pytest -q
py tools\validate_source_skill.py
```

## Compatibility

`LoopEngineeringBlueprint` is additive. It does not replace `PromptPacketV2` or `LoopPromptPack`.
