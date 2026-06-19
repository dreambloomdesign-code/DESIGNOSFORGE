# GitHub Management

## Version Direction

Use semantic versioning with explicit release lanes:

- `v1.4.x`: operational upgrades that preserve the v1.4 inference protocol and public behavior.
- `v1.5.x`: aesthetic quality gates, text/encoding health, layout order, and redundancy governance.
- `v1.6.x`: training-aware memory, project-context routing, photography, EnvArt CADMCP, and PromptPacket v1.6.
- `v2.0.0`: mathematical DesignKernel, PromptPacketV2, route probability, memory similarity, candidate optimization, critic aggregation, and `math_trace`.
- `v2.1.x`: Loop Engineering, LoopEngineeringOS, durable loop runtime, GitHub/CI/worktree workflow planning, validation split, and persistent memory.

## Branch, Tag, and Release Rules

- Use `main` for stable releases.
- Use `release/<version>` for release candidates, such as `release/2.1.0`.
- Use `feat/<short-scope>` for new capabilities.
- Use `fix/<short-scope>` for defects.
- Use annotated release tags when possible: `v2.1.0`.
- Keep each release PR focused on one capability layer: skill metadata, runtime code, CLI management, tests, or packaging.

## GitHub Workflow

1. Check local state: `python -m app.cli github status`.
2. Update skill metadata, references, source package version, tests, README notes, release notes, and PR body.
3. Run validation: skill quick_validate, source CLI smoke checks, compileall, source validator, and pytest.
4. Commit with `feat: add loop engineering runtime`.
5. Push the branch and open a draft PR or push directly to `main` when explicitly requested.
6. Tag `v2.1.0` after tests pass and the release scope is accepted.
7. Attach validation evidence and rollback notes.

Use the GitHub plugin for repository, issue, PR, comment, label, release, and connector-backed write operations. Use local `git` and `gh` only for branch discovery, commits, pushes, current branch PR lookup, GitHub Actions logs, and gaps not covered by the connector.

## Source CLI

From the source package root:

```powershell
$env:PYTHONPATH='.'
$env:PYTHONUTF8='1'
py -3 -m app.cli github status
py -3 -m app.cli github release-plan --version v2.1.0
py -3 -m app.cli github pr-template --version v2.1.0
py -3 -m app.cli kernel loop-engineering "Loop Engineering 调度 issue CI，worktree 并行隔离，validator 验收，写入长期记忆"
```

Do not create remotes, push, or publish releases without an explicit repository target confirmation.
