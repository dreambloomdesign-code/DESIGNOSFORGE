# Release DESIGNOSFORGE v1.6.0

## Summary

- Add training-aware aesthetic memory through `AestheticMemoryIndex`.
- Upgrade PromptPacket to v1.6 with project-context lock, case-memory selection, and failure-memory sections.
- Normalize current LoRA captions and manifests with `project_context_ids`.
- Add corpus audit, memory-index generation, and case recommendation CLI commands.

## Validation

- [ ] `python -m app.cli capabilities`
- [ ] `python -m app.cli lora audit-corpus`
- [ ] `python -m app.cli lora build-memory-index`
- [ ] `python -m app.cli lora recommend --domain exhibition-board --context academic-discipline-competition`
- [ ] `python -m app.cli run "做一个品牌 VI 方案" --prompt-packet`
- [ ] `pytest -q`
- [ ] `python tools/validate_source_skill.py`
- [ ] GitHub Actions passed

## Migration

- Prompt consumers should use PromptPacket v1.6 sections `01_TASK_BRIEF` through `18_REVISION_PROTOCOL`.
- Case curation should include `project_context_ids` before the memory index is rebuilt.

## Rollback

- Revert the release commit or restore the previous `v1.5.1` tag.
