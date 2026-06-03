# DESIGNOSFORGE v2.0.0 Source for Codex

DESIGNOSFORGE is an open-source Codex agent and skill system for turning AI design from prompt guessing into a governed, inspectable design workflow.

v2.0.0 moves the project from prompt governance into a mathematical design kernel. It now models design decisions as vectors, probabilities, constraints, ranked candidate directions, critic scores, and failure-memory retrieval.

## What Changed In v2.0

- `DesignKernel`: a new end-to-end orchestration core for intent parsing, routing, memory, constraints, candidates, critics, tool planning, and PromptPacketV2.
- `DesignMathEngine`: Chinese/Latin vectorization, cosine and jaccard similarity, softmax route probability, entropy, confidence margin, Pareto front, TOPSIS, weighted utility, and residual-risk penalty.
- `PromptPacketV2`: a richer design contract with route math, memory math, constraint math, candidate optimization, critic aggregation, and failure memory.
- Stronger city identity behavior: routes public-cultural logo tasks toward modular identity systems and actively penalizes generic landmark stacking.
- Stronger photography behavior: locks face identity, body anatomy, expression, clothing, light direction, skin texture, and documentary scene truth.
- Stronger EnvArt behavior: CADMCP remains the source-fidelity route for CAD/DWG/DXF, construction drawings, layer semantics, wall/opening topology, and plan-to-board workflows.

## Why It Matters

Most AI design workflows fail after generation starts. DESIGNOSFORGE moves quality control before generation:

- one dominant focal anchor instead of scattered fragments
- grid, density, and negative-space rules instead of visual noise
- exact visible text instead of pseudo-text and mojibake
- structured PromptPacketV2 output instead of loose prompt paragraphs
- project-context locks instead of mixing commercial and academic competition logic
- memory-case recommendations instead of vague style recall
- mathematical route and candidate audits instead of black-box taste claims
- GitHub-ready release workflows instead of one-off local experiments

## Open Source

DESIGNOSFORGE is released under the MIT License as an open-source Codex agent/skill system.

Use it to study, adapt, and extend:

- Codex skill packaging
- design-agent orchestration
- visual prompt governance
- mathematical design routing
- aesthetic quality gates
- LoRA aesthetic corpus planning
- photography and retouching aesthetic-memory planning
- environmental-art CAD/DWG/DXF source-fidelity workflows
- training-aware aesthetic memory indexing
- project-context routing for commercial, academic competition, and public cultural work
- GitHub-ready release workflows

See `docs/CODEX_INSTALL.md` for local Codex skill installation.

## Quick Check

```bash
PYTHONPATH=. python -m app.cli capabilities
PYTHONPATH=. python -m app.cli kernel plan "为安徽省钢城马鞍山市设计城市标识系统logo，要求现代、公共文化传播、不要堆砌地标"
PYTHONPATH=. python -m app.cli kernel math-audit "拯救课堂纪实照片，不要改变人物本来的面貌形象"
PYTHONPATH=. python -m app.cli kernel prompt-packet "用CADMCP审核环艺DWG平面并生成展板分析图提示词"
PYTHONPATH=. python -m app.cli lora audit-corpus
PYTHONPATH=. python -m app.cli lora build-memory-index
PYTHONPATH=. python -m app.cli envart-cad plan "用CADMCP审核环艺DWG平面并生成展板分析图提示词"
PYTHONPATH=. python -m app.cli github release-plan --version v2.0.0
PYTHONPATH=. pytest -q
```

## GitHub

This source package includes a GitHub Actions workflow, PR body, release notes, and a source skill validator.
After binding a target remote, push the main branch and tag `v2.0.0`, then open a draft PR using `docs/PR_BODY_v2.0.0.md`.

## Codex Placement

Use `codex_skill/designos-forge/SKILL.md` as the Codex skill entry. The included Codex entry has been upgraded to `designos-forge` v2.0.0 with a mathematical DesignKernel, PromptPacketV2, aesthetic memory, failure memory, photography, EnvArt CADMCP fusion, prompt precision, text/encoding health, environment-aware routing, and Git/GitHub release planning.
