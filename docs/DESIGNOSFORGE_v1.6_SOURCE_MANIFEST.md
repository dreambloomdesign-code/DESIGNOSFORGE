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

## Validation Targets

- `python -m app.cli capabilities` reports `DESIGNOSFORGE v1.6.0`.
- `python -m app.cli lora audit-corpus` reports zero missing project contexts.
- `python -m app.cli lora recommend --domain exhibition-board --context academic-discipline-competition` returns academic competition cases.
- `pytest -q` passes.
- `tools/validate_source_skill.py` passes.
