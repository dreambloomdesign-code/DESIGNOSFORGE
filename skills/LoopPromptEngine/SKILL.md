# LoopPromptEngine

Independent LoopPromptPack companion prompt system.

Use for self-refine iteration, failed-result recovery, branch search, visual-result repair, and seamless video-loop prompts.

Rules:

- do not replace PromptPacketV2
- change one axis per iteration
- preserve hard constraints
- keep visible text exact
- stop on pass, repeated failure, user acceptance, or max iterations
