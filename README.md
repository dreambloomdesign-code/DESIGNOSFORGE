# DESIGNOSFORGE v1.4 Source for Codex

DESIGNOSFORGE is a design-agent source package for Codex. It integrates default design-agent activation, three-step inference, image-generation gatekeeping, PromptPacket generation, skill registry management, LoRA sidecar planning, GitOps sidecar management, and GitHub release/PR planning.

## Quick Check

```bash
PYTHONPATH=. python -m app.cli capabilities
PYTHONPATH=. python -m app.cli run "做一个品牌 VI 方案" --prompt-packet
PYTHONPATH=. python -m app.cli gitops sync-registry
PYTHONPATH=. python -m app.cli github status
PYTHONPATH=. python -m app.cli github release-plan --version v1.4.2
PYTHONPATH=. pytest -q
```

## Codex Placement

Use `codex_skill/designos-forge/SKILL.md` as the Codex skill entry. The included Codex entry has been upgraded to `designos-forge` v1.4.2 with environment-aware Git/GitHub routing while preserving the v1.4 source package runtime.
