# DESIGNOSFORGE v1.6.0 Release Notes

DESIGNOSFORGE v1.6.0 upgrades the system from prompt governance into training-aware design orchestration.

## Highlights

- Adds `AestheticMemoryIndex` for corpus audit, memory-index generation, and case recommendation.
- Upgrades PromptPacket to v1.6 with project-context lock, case-memory selection, and failure-memory sections.
- Adds project-context coverage across all current caption batches.
- Separates commercial projects, academic discipline competitions, Culture China research, and public cultural communication.
- Generates `lora_training_sandbox/aesthetic_corpus/aesthetic_memory_index.json` for batch-level memory selection.
- Adds CLI commands:
  - `python -m app.cli lora audit-corpus`
  - `python -m app.cli lora build-memory-index`
  - `python -m app.cli lora recommend --domain exhibition-board --context academic-discipline-competition`

## Migration Notes

Prompt builders and downstream workflows should expect PromptPacket v1.6 sections `01_TASK_BRIEF` through `18_REVISION_PROTOCOL`.

After adding new case images or captions, run:

```bash
PYTHONPATH=. python -m app.cli lora audit-corpus
PYTHONPATH=. python -m app.cli lora build-memory-index
```

Do not use public reference images for weight training until rights are cleared.

## Validation

- `python -m app.cli capabilities`
- `python -m app.cli lora audit-corpus`
- `python -m app.cli lora recommend --domain exhibition-board --context academic-discipline-competition`
- `python -m app.cli run "做一个品牌 VI 方案" --prompt-packet`
- `pytest -q`
- `tools/validate_source_skill.py`
