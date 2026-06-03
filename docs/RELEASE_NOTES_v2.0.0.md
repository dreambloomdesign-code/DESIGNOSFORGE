# DESIGNOSFORGE v2.0.0 Release Notes

DESIGNOSFORGE v2.0.0 is a leap from prompt governance to a mathematical design intelligence kernel.

## Highlights

- Adds `DesignKernel` as the default orchestration core.
- Adds `DesignMathEngine` with mixed Chinese/Latin vectorization, cosine/jaccard similarity, softmax probability, entropy, confidence margin, Pareto front, TOPSIS, weighted utility, and constraint penalty.
- Adds `PromptPacketV2` with route math, memory math, candidate optimization, critic aggregation, failure memory, and tool planning.
- Improves city identity routing with modular public-cultural identity logic and anti-landmark-stacking failure memory.
- Improves photography routing with identity preservation, body/anatomy, expression, clothing, light direction, and natural retouching constraints.
- Improves EnvArt CADMCP routing with source-fidelity constraints and CAD geometry locks.
- Adds `kernel math-audit` for explainable route and candidate decisions.

## Validation

Expected validation commands:

```powershell
py -m compileall app tools
py -m app.cli capabilities
py -m app.cli kernel math-audit "为安徽省钢城马鞍山市设计城市标识系统logo，要求现代、公共文化传播、不要堆砌地标"
py -m app.cli kernel prompt-packet "拯救课堂纪实照片，不要改变人物本来的面貌形象"
py tools\validate_source_skill.py
```

## Compatibility

v2.0.0 keeps existing LoRA, photography, EnvArt CADMCP, GitOps, and GitHub workflows while adding a richer PromptPacketV2 and `math_trace` contract. Consumers that only expect PromptPacket v1.6 should update to PromptPacketV2.
