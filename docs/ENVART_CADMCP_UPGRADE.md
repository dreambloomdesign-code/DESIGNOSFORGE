# EnvArt CADMCP Upgrade

DESIGNOSFORGE v1.6.1 upgrades `EnvArtBoardOS` into a CAD-aware environmental-art workflow.

The goal is simple: CAD truth first, visual expression second.

## Capability Model

`EnvArtCADMCPBridge` routes environmental-art work through CADMCP channels before board styling, image2 prompts, or delivery.

Supported channels:

- `dxf_deterministic`: `cad_health`, `dxf_inspect`, `dxf_audit`
- `dwg_core_console`: `cad_health`, `scr_write`, `accoreconsole_run`
- `autocad_com_live`: `cad_health`, `autocad_state`, `autocad_open`, `autocad_send_command`, `autocad_lisp`
- `tianzheng_architecture`: `cad_health`, `tianzheng_launch`

## Geometry Locks

Before environmental-art styling, lock:

- units, scale, north arrow, site boundary, structural axes
- outer envelope, walls, columns, openings, stairs and cores
- circulation paths, room or zone names, dimensions, title block
- semantic layers and editable text

## Output Modes

- CAD source audit
- semantic layer report
- plan-fidelity prompt
- analysis diagram prompt pack
- competition board prompt pack
- construction drawing QA
- DWG/DXF processing plan

## Quality Gates

Do not change CAD topology to improve aesthetics.

Avoid:

- wall additions, deletions, drift, or deformation
- door/window symbols pasted over unbroken walls
- copied source layer `0` habits
- fake dimensions, north arrows, roads, POI, or room names
- construction notes used as decorative texture
- renders replacing missing plan logic

## CLI

```bash
PYTHONPATH=. python -m app.cli envart-cad plan "用 CADMCP 审核环艺 DWG 平面并生成展板分析图提示词"
PYTHONPATH=. python -m app.cli lora recommend --domain environmental-art --context spatial-cad-production
```

## LoRA Memory

The batch `envart-cadmcp-foundation-2026` reserves workflow memory for:

- CADMCP channel selection
- source-fidelity and topology locks
- semantic layer classification
- construction drawing QA
- plan-locked image2 prompts
- board evidence-chain composition
