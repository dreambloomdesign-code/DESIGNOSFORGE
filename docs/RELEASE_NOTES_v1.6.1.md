# DESIGNOSFORGE v1.6.1 Release Notes

DESIGNOSFORGE v1.6.1 focuses on environmental-art intelligence and CADMCP fusion.

## Added

- `EnvArtCADMCPBridge` runtime module for CADMCP channel planning.
- `envart-cad plan` CLI command.
- New agents in capability reporting: `EnvArtCADMCPBridge`, `CADGeometryLockAgent`, `CADLayerSemanticAuditor`, and `ConstructionDrawingQAGate`.
- `spatial-cad-production` project context.
- `cad-topology-fidelity` and `construction-drawing-logic` style axes.
- CAD-specific quality labels for source fidelity, semantic layers, wall topology, openings, dimensions, title blocks, construction annotations, and topology drift.
- `envart-cadmcp-foundation-2026` aesthetic-memory batch.

## Improved

- PromptPacket v1.6 now injects CAD geometry locks for CAD/DWG/DXF, AutoCAD, Tianzheng, construction drawing, plan, section, and elevation tasks.
- EnvArt routing now prioritizes CADMCP tasks before generic board routing.
- Quality gates now detect CAD source terms and CAD topology risk terms.

## Validation

- `python -m app.cli capabilities`
- `python -m app.cli envart-cad plan "..."`
- `python -m app.cli lora audit-corpus`
- `python -m app.cli lora build-memory-index`
- `python -m app.cli lora recommend --domain environmental-art --context spatial-cad-production`
- `python tools/validate_source_skill.py`
