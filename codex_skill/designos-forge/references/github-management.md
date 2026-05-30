# GitHub Management

## Version Direction

Use semantic versioning with explicit release lanes:

- `v1.4.x`: operational upgrades that preserve the v1.4 inference protocol and public behavior.
- `v1.5.0`: new design workflow capabilities that affect routing, generated contracts, or delivery formats.
- `v2.0.0`: breaking changes to PromptPacket structure, CLI command shape, artifact contracts, or user-facing orchestration rules.

Recommended near-term path:

1. `v1.4.2`: add GitHub management, release planning, PR templates, and local repository status checks.
2. `v1.5.0`: add aesthetic quality gates, PromptPacket v1.5, text/encoding health, layout order, and redundancy governance.
3. `v1.5.1`: add CI workflow templates and automated skill/source validation.
4. `v1.6.0`: add plugin-aware release publishing, changelog generation, issue templates, and multi-skill compatibility matrix.

## Branch, Tag, and Release Rules

- Use `main` for stable releases.
- Use `release/<version>` for release candidates, such as `release/1.4.2`.
- Use `feat/<short-scope>` for new capabilities.
- Use `fix/<short-scope>` for defects.
- Use annotated release tags when possible: `v1.4.2`, `v1.4.3`, `v1.5.0`.
- Keep each release PR focused on one capability layer: skill metadata, runtime code, CLI management, tests, or packaging.

## GitHub Workflow

1. Check local state: `python -m app.cli github status`.
2. Create a release branch: `git switch -c release/1.4.2`.
3. Update skill metadata, references, source package version, tests, and README notes.
4. Run validation: skill quick_validate, CLI smoke checks, and pytest.
5. Commit with `release: designosforge v1.4.2`.
6. Push the branch and open a draft PR.
7. Attach validation evidence and rollback notes.
8. After review and CI, merge to `main`, tag, push tag, and publish GitHub Release notes.

Use the GitHub plugin for repository, issue, PR, comment, label, release, and connector-backed write operations. Use local `git` and `gh` only for branch discovery, commits, pushes, current branch PR lookup, GitHub Actions logs, and gaps not covered by the connector.

## Source CLI

From the source package root:

```powershell
$env:PYTHONPATH='.'
$env:PYTHONUTF8='1'
py -3 -m app.cli github status
py -3 -m app.cli github release-plan --version v1.5.0
py -3 -m app.cli github pr-template --version v1.5.0
```

If the folder is not yet a Git repository, initialize and publish only after the user confirms the target GitHub owner/repo:

```powershell
git init
git add .
git commit -m "release: designosforge v1.5.0"
git remote add origin https://github.com/<owner>/<repo>.git
git push -u origin main
```

Do not create remotes, push, or publish releases without explicit repository target confirmation.
