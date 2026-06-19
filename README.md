# DESIGNOSFORGE v2.1.0 Source for Codex

DESIGNOSFORGE is an open-source Codex agent and skill system for turning AI design from prompt guessing into a governed, inspectable design workflow.

v2.1.0 adds **Loop Engineering**: a system-runtime layer for scheduled, event-driven, multi-agent, tool-connected loops that can keep project context, validate results, and write durable memory.

## What Changed In v2.1

- `DesignKernel`: keeps the v2 mathematical orchestration core for intent parsing, routing, memory, constraints, candidates, critics, tool planning, and PromptPacketV2.
- `LoopPromptPack`: remains the independent prompt-iteration companion pack for self-refine, failed-result recovery, branch search, visual-result repair, and seamless video loops.
- `LoopEngineeringBlueprint`: new runtime blueprint for scheduler, worktree isolation, skill context, external connectors, validation gates, and persistent memory.
- `LoopEngineeringOS`: new registry/capability route for long-running agent loops, GitHub/CI/PR workflows, and complete project-following workflows.
- GitHub release planning now defaults to `v2.1.0` and includes compile, source validator, CLI smoke, and pytest gates.
- Skill packaging now exposes Loop Engineering as a separate layer rather than replacing PromptPacketV2 or LoopPromptPack.

## Why It Matters

Most AI design workflows fail because the agent loses the project thread. DESIGNOSFORGE v2.1 makes the workflow answer six engineering questions before it runs:

- Who wakes the loop?
- How do parallel agents avoid collisions?
- How does the agent know project habits?
- What external systems can it touch?
- Who validates the result?
- How does it remember yesterday?

Principle: the model may forget, but the repository must not.

## Capability Call Table

| User intent | Primary route | Output | Validation |
| --- | --- | --- | --- |
| General design strategy | `DesignKernel` | `PromptPacketV2` | route math, critic aggregation, constraints |
| Iterative prompt refinement | `LoopPromptEngine` | `LoopPromptPack` | one-axis iteration, stop conditions, failure memory |
| Durable agent loops | `LoopEngineeringOS` | `LoopEngineeringBlueprint` | scheduler, worktree isolation, verifier split, memory |
| Brand, VI, city identity | `brandVIos` | mark system direction and prompt packet | grid derivation, dynamic system, no random landmarks |
| Academic infovis boards | `InfoVisOS` / `LayeredBoardComposer` | board strategy and modules | thesis hierarchy, evidence modules, text accuracy |
| EnvArt/CAD production | `EnvArtCADMCPBridge` | CAD-aware plan or prompt packet | CAD health, DXF audit, geometry locks |
| Photography/retouching | `PhotographyOS` | edit or shoot plan | identity preservation, light direction, artifact check |
| GitHub/release work | `GitHubManager` / GitHub plugin | release plan or PR body | compileall, tests, source validator, CI/PR checks |

## Quick Check

```powershell
$env:PYTHONPATH='.'
$env:PYTHONUTF8='1'
py -m app.cli capabilities
py -m app.cli kernel loop-engineering "Loop Engineering 调度 issue CI，worktree 并行隔离，validator 验收，写入长期记忆"
py -m app.cli kernel loop-prompt "create a design prompt with three loop iterations and self critique"
py -m app.cli github release-plan --version v2.1.0
py -m compileall app tests tools
py -m pytest -q
py tools\validate_source_skill.py
```

## Open Source

DESIGNOSFORGE is released under the MIT License as an open-source Codex agent/skill system.

Use it to study, adapt, and extend:

- Codex skill packaging
- design-agent orchestration
- visual prompt governance
- mathematical design routing
- Loop Engineering runtime design
- aesthetic quality gates
- LoRA aesthetic corpus planning
- photography and retouching workflows
- environmental-art CAD/DWG/DXF source-fidelity workflows
- GitHub-ready release workflows

See `docs/CODEX_INSTALL.md` for local Codex skill installation.

## GitHub

This source package includes GitHub workflow docs, PR bodies, release notes, and a source skill validator.

For v2.1 release work, use `docs/PR_BODY_v2.1.0.md` and `docs/RELEASE_NOTES_v2.1.0.md`. Do not publish releases or notify external systems without explicit user intent.

## Codex Placement

Use `codex_skill/designos-forge/SKILL.md` as the Codex skill entry. The included skill has been upgraded to `designos-forge` v2.1.0 with DesignKernel, PromptPacketV2, LoopPromptPack, LoopEngineeringOS, aesthetic memory, failure memory, photography, EnvArt CADMCP fusion, prompt precision, text/encoding health, project-context routing, GitOps, and GitHub release planning.
