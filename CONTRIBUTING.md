# Contributing

Thanks for improving DESIGNOSFORGE.

## Scope

This repository is for Codex-oriented open-source agent and skill workflows:

- Codex skill entry and references under `codex_skill/designos-forge`
- Source agents under `app`
- Routed design skill descriptions under `skills`
- Validation, packaging, and GitHub release workflows

## Development

```bash
python -m pip install -e ".[dev]"
PYTHONPATH=. python -m app.cli capabilities
PYTHONPATH=. python -m app.cli quality audit "高级 大气 细碎 脏乱 生成一张海报"
pytest -q
```

On Windows, prefer `py -3` and set `PYTHONUTF8=1` when validating Chinese or mixed-language files.

## Pull Requests

Before opening a PR:

- Keep changes focused on one capability layer.
- Run tests and source skill validation.
- Include validation evidence in the PR body.
- Do not include private conversation logs, API keys, model weights, generated private assets, or personal context.

## Design Quality

For visual-generation workflows, preserve the v1.5 gates:

- one dominant focal anchor
- explicit grid and density ceiling
- exact visible text and spelling rules
- UTF-8/no-mojibake checks
- anti-fragmentation negative prompt
- one owner each for routing, QA, and delivery
