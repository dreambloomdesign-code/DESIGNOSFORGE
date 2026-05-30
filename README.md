# DESIGNOSFORGE v1.5 Source for Codex

DESIGNOSFORGE is an open-source Codex agent/skill system for turning AI design from prompt guessing into a governed design workflow.

It focuses on the problems that make AI visuals feel unusable: fragmented compositions, dirty textures, weak prompts, garbled text, broken layout order, and unreviewable delivery.

At its core are PromptPacket v1.5, aesthetic quality gates, anti-fragmentation controls, text/encoding health checks, layout-order rules, and GitHub-ready release workflows.

## Open Source

DESIGNOSFORGE is released under the MIT License as an open-source Codex agent/skill system.

Use it to study, adapt, and extend:

- Codex skill packaging
- design-agent orchestration
- visual prompt governance
- aesthetic quality gates
- GitHub-ready release workflows

See `docs/CODEX_INSTALL.md` for local Codex skill installation.

## Why It Matters

Most AI design workflows fail after generation starts. DESIGNOSFORGE moves quality control before generation:

- one dominant focal anchor instead of scattered fragments
- grid, density, and negative-space rules instead of visual noise
- exact visible text instead of pseudo-text and mojibake
- structured PromptPacket output instead of loose prompt paragraphs
- reviewable GitHub workflows instead of one-off local experiments

For launch copy, social posts, and community announcements, see `docs/PROMOTION_COPY.md`.

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
