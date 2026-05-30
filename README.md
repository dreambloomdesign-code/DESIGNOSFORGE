# DESIGNOSFORGE v1.5 Source for Codex

DESIGNOSFORGE is a design-agent source package for Codex. It integrates default design-agent activation, three-step inference, image-generation gatekeeping, PromptPacket v1.5 generation, aesthetic quality gates, text/encoding health checks, skill registry management, LoRA sidecar planning, GitOps sidecar management, and GitHub release/PR planning.

## Open Source

DESIGNOSFORGE is released under the MIT License as an open-source Codex agent/skill system.

Use it to study, adapt, and extend:

- Codex skill packaging
- design-agent orchestration
- visual prompt governance
- aesthetic quality gates
- GitHub-ready release workflows

See `docs/CODEX_INSTALL.md` for local Codex skill installation.

## Quick Check

```bash
PYTHONPATH=. python -m app.cli capabilities
PYTHONPATH=. python -m app.cli run "做一个品牌 VI 方案" --prompt-packet
PYTHONPATH=. python -m app.cli gitops sync-registry
PYTHONPATH=. python -m app.cli github status
PYTHONPATH=. python -m app.cli github release-plan --version v1.5.0
PYTHONPATH=. python -m app.cli quality audit "高级 大气 细碎 脏乱 生成一张海报"
PYTHONPATH=. pytest -q
```

## GitHub

This source package includes a GitHub Actions workflow, PR body, release notes, and a source skill validator.
After binding a target remote, push `release/1.5.0` and tag `v1.5.0`, then open a draft PR using `docs/PR_BODY_v1.5.0.md`.

## Codex Placement

Use `codex_skill/designos-forge/SKILL.md` as the Codex skill entry. The included Codex entry has been upgraded to `designos-forge` v1.5.0 with aesthetic quality gates, prompt precision, text/encoding health, environment-aware routing, and Git/GitHub release planning.
