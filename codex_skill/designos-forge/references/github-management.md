# GitHub Management

## Version Direction

Use semantic versioning with explicit release lanes:

- `v1.4.x`: operational upgrades that preserve the v1.4 inference protocol and public behavior.
- `v1.5.x`: aesthetic quality gates, text/encoding health, layout order, and redundancy governance.
- `v1.6.x`: training-aware memory, project-context routing, photography, EnvArt CADMCP, and PromptPacket v1.6.
- `v2.0.0`: mathematical DesignKernel, PromptPacketV2, route probability, memory similarity, candidate optimization, critic aggregation, and `math_trace`.

## Branch, Tag, and Release Rules

- Use `main` for stable releases.
- Use `release/<version>` for release candidates, such as `release/2.0.0`.
- Use `feat/<short-scope>` for new capabilities.
- Use `fix/<short-scope>` for defects.
- Use annotated release tags when possible: `v2.0.0`.
- Keep each release PR focused on one capability layer: skill metadata, runtime code, CLI management, tests, or packaging.

## GitHub Workflow

1. Check local state: `python -m app.cli github status`.
2. Update skill metadata, references, source package version, tests, and README notes.
3. Run validation: skill quick_validate, CLI smoke checks, compileall, source validator, and pytest when available.
4. Commit with `feat: upgrade designosforge to v2 design kernel`.
5. Push the branch and open a draft PR or push directly to `main` when explicitly requested.
6. Tag `v2.0.0`.
7. Attach validation evidence and rollback notes.

Use the GitHub plugin for repository, issue, PR, comment, label, release, and connector-backed write operations. Use local `git` and `gh` only for branch discovery, commits, pushes, current branch PR lookup, GitHub Actions logs, and gaps not covered by the connector.

## Source CLI

From the source package root:

```powershell
$env:PYTHONPATH='.'
$env:PYTHONUTF8='1'
py -3 -m app.cli github status
py -3 -m app.cli github release-plan --version v2.0.0
py -3 -m app.cli github pr-template --version v2.0.0
py -3 -m app.cli kernel math-audit "为安徽省钢城马鞍山市设计城市标识系统logo，要求现代、公共文化传播、不要堆砌地标"
```

Do not create remotes, push, or publish releases without an explicit repository target confirmation.
