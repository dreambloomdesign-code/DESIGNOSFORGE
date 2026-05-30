# DesignOS Forge Runtime

## Local Path

```text
C:\Users\taojian\Documents\超级设计智能体\DesignOS_Forge_Algorithmic_Edition
```

## Install

```powershell
.\scripts\install_designos_forge.ps1
```

The install script creates `.venv`, installs the Python package in editable mode with dev tools, and builds the local TypeScript MCP skeletons when `npm` is available.

## CLI

Wake command:

```powershell
.\scripts\designos.ps1 run "调用DesignForge"
```

In chat mode, type:

```text
调用DesignForge
```

The wake command returns self-introduction and usage instructions only.

Interactive mode:

```powershell
.\scripts\designos.ps1
```

This is the default design-progress mode. It saves a local session, returns phase, maturity, locked decisions, options, risks, and next questions. It does not create delivery files until the user says "交付", "出包", "导出", or `deliver`.

Single request:

```powershell
.\scripts\designos.ps1 run "生成一个高级品牌VI方案，输出PDF PNG ZIP" -o pdf,png,zip
```

With attachments:

```powershell
.\scripts\designos.ps1 run "基于平面图生成环艺竞赛展板，比例准确，输出PSD PNG ZIP" -a "C:\path\plan.pdf" -o psd,png,zip
```

Raw JSON:

```powershell
.\scripts\designos.ps1 run "做一套信息可视化海报" -o png,pdf,zip --json
```

Image-model intent:

```powershell
.\scripts\designos.ps1 run "生成品牌主视觉并输出PNG" -o png --image-model --max-images 2
```

`--image-model` records that image generation is required. Real rendering still depends on available image-generation tools or MCP/API credentials.

## API

Start:

```powershell
.\scripts\start_designos_forge.ps1
```

Use another port when `8000` is occupied:

```powershell
.\scripts\start_designos_forge.ps1 -Port 8010
```

Docs:

```text
http://127.0.0.1:8000/docs
```

POST body for staged `/design-sessions/turn`:

```json
{
  "message": "为一个高端茶饮品牌建立竞赛级 VI 方案，风格高级、克制、非模板。",
  "output_requirements": ["pdf", "png", "zip"]
}
```

Continue with the returned `session_id`:

```json
{
  "session_id": "session id",
  "message": "选 B，但包装要更年轻，字体不要太传统。"
}
```

Deliver after confirmation:

```json
{
  "session_id": "session id",
  "message": "方向确认，出包。",
  "deliver": true,
  "output_requirements": ["pdf", "png", "zip"]
}
```

POST body for one-shot `/projects/intake`:

```json
{
  "user_request": "生成一个高级品牌VI方案，输出PDF PNG ZIP",
  "attachments": [],
  "output_requirements": ["pdf", "png", "zip"],
  "generate_delivery": true,
  "use_image_model": false,
  "max_image_count": 1
}
```

## Artifact Locations

Each run writes a folder under:

```text
data\deliveries\<delivery_id>
```

Important files:

- `delivery_plan.json`: requested formats and profile.
- `workflow_result.json`: full structured workflow.
- `prompt_pack.json`: downstream prompt and QA contract.
- `qa_report.md`: gate results and issues.
- `summary.md`: human-readable summary.
- `preview_01.png`: local placeholder preview.
- `manifest.json`: final artifact index.
- `delivery_package.zip`: archive for handoff.

## MCP Notes

Local skeletons:

- `mcp\image2-server`
- `mcp\photoshop-bridge-server`

Build them with `.\scripts\install_designos_forge.ps1`. Add their absolute paths to Codex MCP config only after they build. Keep them `required = false` until real credentials/bridges are confirmed, so Codex remains usable without external services.
