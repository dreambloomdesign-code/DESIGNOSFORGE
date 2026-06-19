# Release DESIGNOSFORGE v2.1.0

## Summary

- Add Loop Engineering as a system-runtime layer for long-running agent loops.
- Add `LoopEngineeringBlueprintBuilder` and `LoopEngineeringOS`.
- Add `kernel loop-engineering` CLI export.
- Document the six-question loop contract: scheduler, isolation, skill context, connectors, validation, and memory.
- Keep `PromptPacketV2` and `LoopPromptPack` independent and backward compatible.
- Strengthen GitHub/CI/worktree workflow planning and release validation.

## Validation

- [ ] `py -m compileall app tests tools`
- [ ] `py -m app.cli capabilities`
- [ ] `py -m app.cli kernel loop-engineering "Loop Engineering 调度 issue CI，worktree 并行隔离，validator 验收，写入长期记忆"`
- [ ] `py -m app.cli kernel loop-prompt "create a design prompt with three loop iterations and self critique"`
- [ ] `py -m pytest -q`
- [ ] `py tools\validate_source_skill.py`
- [ ] Skill quick_validate passed

## Compatibility

This is additive. Existing PromptPacketV2, LoopPromptPack, LoRA memory, EnvArt CADMCP, photography workflows, and GitHub management remain intact.

## Rollback

Revert the release commit or restore the previous tag.
