# LoopPromptPack Companion Protocol

LoopPromptPack is an independent prompt-engineering scheme for DESIGNOSFORGE v2.0. It does not replace PromptPacketV2. It runs beside it when a task needs iteration, failed-result recovery, branch exploration, visual-result repair, or seamless video-loop prompts.

## Why It Exists

PromptPacketV2 is the main design contract: route, memory, candidates, constraints, critics, tool plan, and generation policy.

LoopPromptPack is a loop controller: it defines how to run repeated prompt attempts safely, how to critique each iteration, how to stop, and how to write failure knowledge back into memory.

## Activation

LoopPromptPack activates when the brief contains signals such as:

- loop, seamless, video loop, first and last frame, closed camera path
- 循环, 闭环, 迭代, 多轮, 自我检查, 继续优化
- 失败, 不成功, 不算数, 好丑, 跑偏, 重来
- 改图, 修图, 拯救, 保留, 不要改变
- 多方案, 分支, 候选, 方案比较

When no loop signal exists, the pack remains available but inactive.

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
  "schema_version": "2.0.0-loop.1",
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

## State Model

Each iteration must preserve:

- `iteration`
- stable original brief
- current draft prompt
- critique findings
- revision delta
- quality score
- stop or continue decision

The loop must change one axis at a time. This prevents prompt drift and avoids turning critique into an uncontrolled rewrite.

## Stop Conditions

A loop should stop when:

- the score reaches the target threshold
- no material revision delta remains
- the same failure repeats
- the user accepts the direction
- the maximum iteration count is reached

Default maximum iterations: `3`.

## CLI

```powershell
py -m app.cli kernel loop-prompt "create a design prompt with three loop iterations and self critique"
py -m app.cli kernel loop-prompt "generate a seamless loop video prompt; first and last frame must match"
py -m app.cli kernel prompt-packet "make a logo"
```

The third command still returns PromptPacketV2. It does not become a LoopPromptPack.
