# DESIGNOSFORGE v1.6.1 Source for Codex

DESIGNOSFORGE is an open-source Codex agent/skill system for turning AI design from prompt guessing into a governed design workflow.

It focuses on the problems that make AI visuals feel unusable: fragmented compositions, dirty textures, weak prompts, garbled text, broken layout order, and unreviewable delivery.

At its core are PromptPacket v1.6, aesthetic quality gates, training-aware case memory, project-context routing, corpus audit tools, EnvArt CADMCP routing, anti-fragmentation controls, text/encoding health checks, layout-order rules, and GitHub-ready release workflows.

The current development branch also adds a photography specialty module for portrait retouching, product photography generation and post-production, composition optimization, and Hanfu cultural portrait planning. See `docs/PHOTOGRAPHY_AESTHETIC_SPACE.md`.

v1.6.1 adds an environmental-art CADMCP fusion layer for CAD/DWG/DXF inspection, AutoCAD Core Console workflows, Tianzheng-aware routing, semantic CAD layers, construction drawing QA, and plan-fidelity image2 or board prompt generation. See `docs/ENVART_CADMCP_UPGRADE.md`.

## Open Source

DESIGNOSFORGE is released under the MIT License as an open-source Codex agent/skill system.

Use it to study, adapt, and extend:

- Codex skill packaging
- design-agent orchestration
- visual prompt governance
- aesthetic quality gates
- LoRA aesthetic corpus planning
- photography and retouching aesthetic-memory planning
- environmental-art CAD/DWG/DXF source-fidelity workflows
- training-aware aesthetic memory indexing
- project-context routing for commercial, academic competition, and public cultural work
- GitHub-ready release workflows

See `docs/CODEX_INSTALL.md` for local Codex skill installation.

## Why It Matters

Most AI design workflows fail after generation starts. DESIGNOSFORGE moves quality control before generation:

- one dominant focal anchor instead of scattered fragments
- grid, density, and negative-space rules instead of visual noise
- exact visible text instead of pseudo-text and mojibake
- structured PromptPacket output instead of loose prompt paragraphs
- project-context locks instead of mixing commercial and academic competition logic
- memory-case recommendations instead of relying on vague style recall
- reviewable GitHub workflows instead of one-off local experiments

For launch copy, social posts, and community announcements, see `docs/PROMOTION_COPY.md`.

## Quick Check

```bash
PYTHONPATH=. python -m app.cli capabilities
PYTHONPATH=. python -m app.cli run "做一个品牌 VI 方案" --prompt-packet
PYTHONPATH=. python -m app.cli gitops sync-registry
PYTHONPATH=. python -m app.cli github status
PYTHONPATH=. python -m app.cli github release-plan --version v1.6.1
PYTHONPATH=. python -m app.cli quality audit "高级 大气 细碎 脏乱 生成一张海报"
PYTHONPATH=. python -m app.cli envart-cad plan "用 CADMCP 审核环艺 DWG 平面并生成展板分析图提示词"
PYTHONPATH=. python -m app.cli lora init-aesthetic-space
PYTHONPATH=. python -m app.cli lora audit-corpus
PYTHONPATH=. python -m app.cli lora build-memory-index
PYTHONPATH=. python -m app.cli lora recommend --domain exhibition-board --context academic-discipline-competition
PYTHONPATH=. python -m app.cli lora recommend --domain environmental-art --context spatial-cad-production
PYTHONPATH=. pytest -q
```

## GitHub

This source package includes a GitHub Actions workflow, PR body, release notes, and a source skill validator.
After binding a target remote, push `release/1.6.1` and tag `v1.6.1`, then open a draft PR using `docs/PR_BODY_v1.6.1.md`.

## Codex Placement

Use `codex_skill/designos-forge/SKILL.md` as the Codex skill entry. The included Codex entry has been upgraded to `designos-forge` v1.6.1 with aesthetic quality gates, training-aware case memory, project-context routing, EnvArt CADMCP fusion, prompt precision, text/encoding health, environment-aware routing, and Git/GitHub release planning.
