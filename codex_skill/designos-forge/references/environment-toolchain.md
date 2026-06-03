# Environment Toolchain

## Current Local Context

- Workspace: `D:\DESIGNOSFORGE`
- Installed skill: `C:\Users\taojian\.codex\skills\designos-forge`
- Source package: `D:\DESIGNOSFORGE\DESIGNOSFORGE_v1.4_source_for_codex`

Prefer the bundled runtime for document, slide, spreadsheet, PDF, image, and browser automation work:

```text
C:\Users\taojian\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe
C:\Users\taojian\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe
```

On this Windows environment, `python.exe` may resolve to the Windows Store shim. Use `py -3` or the bundled runtime, and set `PYTHONUTF8=1` before validating Chinese skill files.

## Audit Command

From the installed skill folder:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\audit-environment.ps1
```

The script returns JSON with detected skill folders, source package locations, Python launchers, bundled runtimes, and validation hints.

## Toolchain Map

- Brand VI and formal VI boards: use `brand-vi-board-system` when competition-grade boards, manuals, brand strategy, or formal VI output is requested.
- Mathematical design routing: use `DesignKernel` and `DesignMathEngine` before visual generation when routing, memory, constraints, candidates, or critic decisions matter.
- Environmental art, spatial boards, exhibition boards, maps, and CAD-based visual analysis: use `envart-analysis-board-agent`, `cad-drawing-control`, and `cad-project-drawing-methodology` as a fused workflow. For CAD/DWG/DXF tasks, run CADMCP readiness first, then preserve source geometry, semantic layers, wall/opening topology, dimensions, title block, and drawing units before board styling or image2 prompt generation.
- UI/web/product design: use `ui-design-spec`; use Browser for localhost verification and Figma for design files, components, diagrams, libraries, or FigJam.
- Image prompts and visual prompt engineering: use `image-prompt-crafter`, `gpt-image-2-style-library`, `prompt-engineering`, or `zh-prompt-library`.
- Real bitmap generation or editing: use image generation/editing only after DESIGNOSFORGE's confirmation gate passes.
- PPT/decks, documents, and spreadsheets: use Presentations, Documents, or Spreadsheets capabilities and render/verify outputs before delivery.
- GitHub, GitOps, registry sync, and source publishing: use GitHub skills, `references/github-management.md`, the v2.0 `github` CLI, or the `gitops` CLI only when code/source state is part of the request.
- Supabase-backed apps: use Supabase capabilities for schema, auth, storage, vectors, and SSR integration tasks.

## Runtime Validation

Validate the installed skill:

```powershell
$env:PYTHONUTF8='1'
py -3 'C:\Users\taojian\.codex\skills\.system\skill-creator\scripts\quick_validate.py' 'C:\Users\taojian\.codex\skills\designos-forge'
```

Validate the source package:

```powershell
$env:PYTHONPATH='.'
$env:PYTHONUTF8='1'
py -3 -m app.cli capabilities
py -3 -m app.cli kernel math-audit '为安徽省钢城马鞍山市设计城市标识系统logo，要求现代、公共文化传播、不要堆砌地标'
py -3 -m app.cli github status
py -3 -m app.cli quality audit '高级 大气 细碎 脏乱 生成一张海报'
```

The source package's editable install needs explicit setuptools discovery that includes `app*` and excludes resource folders.
