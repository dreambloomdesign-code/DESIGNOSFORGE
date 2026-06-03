# Release DESIGNOSFORGE v2.0.0

## Summary

This PR upgrades DESIGNOSFORGE from v1.6.1 to v2.0.0 with a mathematical DesignKernel and PromptPacketV2.

## Changes

- Add `app/core/design_math.py`.
- Replace DesignKernel internals with semantic vector parsing, softmax routing, memory similarity, constraint penalty, candidate optimization, critic aggregation, and failure-memory retrieval.
- Add `kernel math-audit` CLI action.
- Update Codex skill entry, agent manifest, README, install docs, release notes, and source validator.
- Expand capability and skill registry reporting for the v2.0 math layer.

## Validation

- `py -m compileall app tools`
- `py -m app.cli capabilities`
- `py -m app.cli kernel math-audit "..."`
- `py -m app.cli kernel prompt-packet "..."`
- `py tools\validate_source_skill.py`

## Notes

Prompt consumers should migrate from PromptPacket v1.6 to PromptPacketV2 and use `math_trace` for explainable design decisions.
