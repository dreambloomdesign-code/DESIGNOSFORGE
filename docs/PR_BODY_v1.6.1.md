# Release DESIGNOSFORGE v1.6.1

## Summary

This release upgrades environmental-art workflows with CADMCP fusion, making CAD/DWG/DXF source fidelity a first-class design constraint before prompt generation, board composition, or visual polish.

## Changes

- Add `EnvArtCADMCPBridge`.
- Add `envart-cad plan` CLI command.
- Register CAD-aware EnvArt agents and skills.
- Extend PromptPacket v1.6 with CAD geometry locks.
- Extend LoRA taxonomy with `spatial-cad-production`, `cad-topology-fidelity`, and `construction-drawing-logic`.
- Add EnvArt CADMCP foundation captions, manifest, and quality review.
- Update Codex skill metadata and docs.

## QA

- [ ] `PYTHONPATH=. python -m app.cli capabilities`
- [ ] `PYTHONPATH=. python -m app.cli envart-cad plan "用 CADMCP 审核环艺 DWG 平面并生成展板分析图提示词"`
- [ ] `PYTHONPATH=. python -m app.cli lora audit-corpus`
- [ ] `PYTHONPATH=. python -m app.cli lora build-memory-index`
- [ ] `PYTHONPATH=. python -m app.cli lora recommend --domain environmental-art --context spatial-cad-production`
- [ ] `PYTHONPATH=. python tools/validate_source_skill.py`
