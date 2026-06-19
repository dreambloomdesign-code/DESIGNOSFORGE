# LoopPromptPack Reference

LoopPromptPack is an independent companion prompt scheme for DESIGNOSFORGE. It does not replace PromptPacketV2.

Use it when the user asks for:

- loop, iteration, self critique, self-check, continue optimizing
- 循环, 闭环, 迭代, 多轮, 自我检查, 继续优化
- failed-result recovery: 失败, 不成功, 不算数, 当做没发生, 好丑, 跑偏, 重来
- branch exploration: 多方案, 分支, 候选, 方案比较
- visual result repair: 改图, 修图, 拯救, 保留, 不要改变
- seamless video loops: 无缝循环, 首尾一致, loop video, seamless, closed camera path

## Relationship To Loop Engineering

LoopPromptPack controls repeated prompt attempts. LoopEngineeringBlueprint controls the system runtime around a loop.

Use:

- `kernel loop-prompt` for prompt iteration.
- `kernel loop-engineering` for scheduler, worktree isolation, connectors, validation, and persistent memory.

## Required Fields

```text
schema_version
packet_type = LoopPromptPack
relationship_to_prompt_packet_v2
activation
loop_contract
context_snapshot
stage_prompts
quality_gate
export_policy
```

## Loop Types

- `self_refine_loop`: draft, critique, revise, rescore.
- `design_critic_loop`: fix aesthetics, layout order, density, typography, text precision, and anti-fragmentation.
- `failure_memory_loop`: turn rejected output into failure mode, root cause, locks, next prompt boundary, and must-not-repeat controls.
- `branch_search_loop`: produce several candidate prompt branches, score them, and recombine the strongest parts.
- `visual_result_loop`: diagnose a source/result image and write a targeted edit or regeneration prompt.
- `seamless_video_loop`: define first frame, last frame, loop duration, periodic motion, closed camera path, and temporal negative controls.

## Iteration Rules

- Preserve the stable original brief.
- Change one axis per iteration.
- Output state, critique, revision delta, revised prompt, score, and stop-or-continue decision.
- Stop on score pass, no meaningful revision delta, repeated failure, user acceptance, or max iterations.
- Default max iterations: `3`.

## CLI

```powershell
py -m app.cli kernel loop-prompt "create a design prompt with three loop iterations and self critique"
py -m app.cli kernel loop-prompt "generate a seamless loop video prompt; first and last frame must match"
```
