# DESIGNOSFORGE v1.6 Source Manifest

This source package upgrades DESIGNOSFORGE into a training-aware design agent.

## Added In v1.6

- `app/lora_training/aesthetic_memory.py`: corpus audit, memory-index generation, and case recommendation.
- PromptPacket v1.6: 18 sections with project-context lock, case-memory selection, and failure-memory.
- `lora_training_sandbox/aesthetic_corpus/aesthetic_memory_index.json`: batch-level aesthetic memory generated from captions.
- Project-context coverage across current LoRA captions and manifests.
- CLI commands:
  - `lora audit-corpus`
  - `lora build-memory-index`
  - `lora recommend`

## Added In v1.6.1

- `app/core/envart_cadmcp.py`: EnvArt CADMCP channel planning and geometry-lock contract.
- CLI command:
  - `envart-cad plan`
- `docs/ENVART_CADMCP_UPGRADE.md`: environmental-art CADMCP fusion workflow.
- `lora_training_sandbox/aesthetic_corpus/domains/environmental-art/captions/envart-cadmcp-foundation-2026.caption.jsonl`: CADMCP workflow memory.
- `spatial-cad-production` project context.
- `cad-topology-fidelity` and `construction-drawing-logic` style axes.
- CAD source-fidelity quality labels.

## Validation Targets

- `python -m app.cli capabilities` reports `DESIGNOSFORGE v1.6.1`.
- `python -m app.cli envart-cad plan "用 CADMCP 审核环艺 DWG 平面并生成展板分析图提示词"` returns an EnvArt CADMCP plan.
- `python -m app.cli lora audit-corpus` reports zero missing project contexts.
- `python -m app.cli lora recommend --domain environmental-art --context spatial-cad-production` returns EnvArt CADMCP foundation memory.
- `python -m app.cli lora recommend --domain exhibition-board --context academic-discipline-competition` returns academic competition cases.
- `pytest -q` passes.
- `tools/validate_source_skill.py` passes.
