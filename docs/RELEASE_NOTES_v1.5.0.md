# DESIGNOSFORGE v1.5.0 Release Notes

## Highlights

DESIGNOSFORGE v1.5.0 is a quality jump focused on visual discipline and prompt reliability.

- Open source: released as an MIT-licensed Codex agent/skill system.
- Cleaner images: anti-fragmentation rules prevent scattered tiny elements, dirty texture noise, random icons, and overfilled backgrounds.
- Stronger prompts: PromptPacket v1.5 adds aesthetic thesis, composition hierarchy, grid/density, exact text rules, QA gates, and revision protocol.
- Better text: exact visible text, spelling locks, no pseudo-text, and no mojibake are now first-class gates.
- Better layout: grid, margin, reading path, density ceiling, and no-overlap concerns are explicit.
- Better release process: GitHub validation workflow, PR body, release notes, and source skill validator are included.

## Developer Notes

- New module: `app.core.aesthetic_quality`
- New CLI: `python -m app.cli quality audit "<text>"`
- New CLI: `python -m app.cli quality guardrails "<text>"`
- New workflow: `.github/workflows/validate.yml`
- New validator: `tools/validate_source_skill.py`
- New install guide: `docs/CODEX_INSTALL.md`

## Upgrade Guidance

Use `release/1.5.0` as the PR branch. After GitHub remote binding, push the branch and tag:

```bash
git push -u origin release/1.5.0
git push origin v1.5.0
```

Open a draft PR with `docs/PR_BODY_v1.5.0.md`, then publish release notes from `docs/RELEASE_NOTES_v1.5.0.md`.
