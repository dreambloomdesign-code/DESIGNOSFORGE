# LoopPromptPack Companion Protocol

LoopPromptPack is an independent prompt-engineering scheme for DESIGNOSFORGE v2.1. It does not replace PromptPacketV2.

Use it when a task needs prompt iteration, failed-result recovery, branch exploration, visual-result repair, or seamless video-loop prompts.

LoopPromptPack is not the same as Loop Engineering:

- `LoopPromptPack` controls repeated prompt attempts.
- `LoopEngineeringBlueprint` controls the system runtime around a loop: scheduler, worktree isolation, skills, connectors, validation, and memory.

## Activation

LoopPromptPack activates when the brief contains signals such as:

- loop, iteration, self critique, self-check, continue optimizing
- 循环, 闭环, 迭代, 多轮, 自我检查, 继续优化
- failed, not successful, does not count, redo
- 失败, 不成功, 不算数, 当做没发生, 好丑, 跑偏, 重来
- edit image, retouch, repair, preserve, do not change
- 改图, 修图, 拯救, 保留, 不要改变, 参考图
- seamless, loop video, first and last frame, closed camera path
- 无缝循环, 循环视频, 首尾一致, 镜头循环

## Loop Types

```text
self_refine_loop
  Draft -> critique -> revise -> rescore.

design_critic_loop
  Aesthetic critique over dominant anchor, layout order, density, color, typography, and anti-fragmentation.

failure_memory_loop
  Converts rejected outputs into explicit failure modes and safer next prompts.

branch_search_loop
  Generates several prompt directions, scores them, and recombines the strongest parts.

visual_result_loop
  Diagnoses a source/result image and writes a targeted edit or regeneration prompt.

seamless_video_loop
  Controls first/last frame matching, periodic motion, closed camera path, and temporal artifact suppression.
```

## Output Contract

Every LoopPromptPack returns:

```json
{
  "schema_version": "2.1.0-loop.1",
  "packet_type": "LoopPromptPack",
  "relationship_to_prompt_packet_v2": {
    "mode": "independent_companion_pack",
    "does_not_replace_prompt_packet_v2": true
  },
  "activation": {},
  "loop_contract": {},
  "context_snapshot": {},
  "stage_prompts": {},
  "quality_gate": {},
  "export_policy": {}
}
```

## Iteration Rules

- Preserve the stable original brief.
- Change one axis per iteration.
- Output state, critique, revision delta, revised prompt, score, and stop-or-continue decision.
- Keep visible text exact.
- Stop on score pass, no meaningful revision delta, repeated failure, user acceptance, or max iterations.
- Default max iterations: `3`.

## CLI

```powershell
py -m app.cli kernel loop-prompt "create a design prompt with three loop iterations and self critique"
py -m app.cli kernel loop-prompt "generate a seamless loop video prompt; first and last frame must match"
py -m app.cli kernel loop-engineering "Loop Engineering 调度 issue CI，worktree 并行隔离，validator 验收，写入长期记忆"
```

Use `kernel loop-prompt` for prompt iteration. Use `kernel loop-engineering` when the loop must become a running system.
