# Aesthetic And Prompt Governance

## v2.0 Quality Thesis

The design must be mathematically inspected before it becomes visually spectacular. Prevent dirty, fragmented, overfilled visuals by locking project context, selecting relevant memory cases, scoring candidate directions, measuring residual risk, and exposing route/candidate decisions through `math_trace`.

## Root Causes To Catch

- Fragmented visuals: too many small decorative pieces, random icons, scattered labels, background debris, and no dominant focal anchor.
- Dirty visuals: muddy texture noise, overmixed palettes, low-contrast type, uncontrolled grain, and fake aging effects.
- Weak prompts: generic words such as "高级", "大气", "好看", or "丰富" without concrete composition, material, light, typography, and output rules.
- Text failures: long in-image copy, pseudo-text, misspelling, warped letters, mixed language without hierarchy, and mojibake.
- Layout disorder: no grid, no margin system, no reading path, too many modules, no density ceiling, and overlapping text.
- Redundant mechanisms: multiple agents owning the same decision, repeated QA sections, repeated negative prompts, and unclear handoff owner.
- Context mixing: commercial conversion logic applied to academic competition boards, or research-board density applied to premium packaging/product visuals.

## Mathematical Gates

Before image generation or final delivery, require:

- `route.math`: softmax route probability, entropy, probability margin, and confidence.
- `memory.math_trace`: cosine, jaccard, taxonomy similarity, taxonomy prior, and top case scores.
- `constraints.penalty_vector`: risk load, mitigation strength, residual risk, and constraint satisfaction.
- `candidate_optimization`: Pareto/TOPSIS/weighted-utility ranking.
- `critic_aggregation`: weighted critic score.
- `failure_memory`: relevant failed modes and similarity score.

## Hard Gates

Before image generation or final delivery, require:

- One dominant visual anchor and no more than two secondary supports.
- One explicit project context and 1-3 relevant memory cases, or a statement that no suitable memory case exists.
- Explicit grid, margin, alignment, reading path, and negative space.
- Density ceiling: name what stays empty, quiet, or visually subordinate.
- Exact visible text: spelling, language, hierarchy, max lines, and no pseudo-text.
- UTF-8/no-mojibake check when Chinese or mixed-language text is present.
- Anti-fragmentation negative prompt: no scattered tiny decorations, no dirty texture noise, no random icons, no warped type, no fake logos, no unresolved placeholders.
- One owner each for context routing, case-memory selection, QA, and delivery; remove duplicated mechanisms.

## PromptPacketV2 Contract

PromptPacketV2 must include:

```text
schema_version
packet_type
task_brief
intent
route
aesthetic_genome
memory_selection
candidate_directions
critic_scores
hard_constraints
soft_goals
failure_memory
math_trace
tool_plan
revision_protocol
generation_policy
```

## LoopPromptPack Companion Contract

LoopPromptPack is a separate prompt scheme. It does not replace PromptPacketV2 and must not remove any PromptPacketV2 section.

Use LoopPromptPack only when the task needs iterative prompting, failed-result recovery, branch search, visual-result repair, or seamless video-loop prompting. It should be exported as an independent JSON object or attached beside PromptPacketV2 as a companion pack.

LoopPromptPack must include:

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

Required loop types:

- `self_refine_loop`: draft, critique, revise, rescore.
- `design_critic_loop`: repair aesthetics, layout order, density, typography, and text accuracy.
- `failure_memory_loop`: transform rejected outputs into explicit failure modes and safer next prompts.
- `branch_search_loop`: explore candidate prompt branches, score them, and recombine the strongest parts.
- `visual_result_loop`: diagnose an image/result and write a targeted edit or regeneration prompt.
- `seamless_video_loop`: enforce first/last frame consistency, periodic motion, and temporal artifact controls.

The loop must change one axis at a time and stop when the quality target passes, no meaningful revision remains, the same failure repeats, the user accepts the result, or the maximum iteration count is reached.

## Rewrite Pattern

Replace vague visual language with controlled structure:

- Weak: "高级大气，元素丰富，有冲击力。"
- Strong: "One oversized matte-black ceramic bottle as the only focal anchor, centered on a 12-column editorial grid; two small secondary proof marks; 60% quiet warm-gray negative space; exact title text only; no scattered decorations or noisy texture."

For typography prompts, require exact text first. For boards, require modules and hierarchy. For UI, require tokens, grid, states, and content-fit QA. For city identity, require grid derivation, scalable lockups, dynamic submarks, and no random landmark stacking.
