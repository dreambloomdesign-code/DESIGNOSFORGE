# Release DESIGNOSFORGE v1.5.0

## Summary

- Add v1.5 aesthetic quality gates for visual cleanliness, layout order, text precision, encoding health, prompt specificity, and redundancy control.
- Expand PromptPacket from v1.4's compact contract to a 15-section v1.5 production prompt structure.
- Add quality CLI actions, text-health audit script, and stronger poster/typography/UI subskill gates.
- Preserve GitHub management, image-generation confirmation gates, and environment-aware routing.
- Publish the project as an MIT-licensed open-source Codex agent/skill system.

## Validation

- [x] Installed skill validates
- [x] Source skill validates
- [x] `pytest -q` passes
- [x] `app.cli capabilities` reports `DESIGNOSFORGE v1.5.0`
- [x] `quality audit` detects clutter and mojibake risks
- [x] Text-health audit reports `mojibake_count: 0`
- [x] MIT License, contributing guide, security policy, and Codex install guide included

## Risk Notes

- Long-line warnings remain as layout/documentation hygiene warnings, not release blockers.
- No GitHub remote is configured in the local checkout yet.

## Rollback

- Revert commit `8702f3b` or restore tag `v1.4.2` baseline from `main`.
