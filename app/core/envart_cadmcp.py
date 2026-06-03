from dataclasses import asdict, dataclass
import json


CAD_CHANNELS = (
    {
        "id": "dxf_deterministic",
        "tools": ("cad_health", "dxf_inspect", "dxf_audit"),
        "best_for": "DXF layer/entity inspection, audit, semantic layer counting, and deterministic exchange geometry.",
    },
    {
        "id": "dwg_core_console",
        "tools": ("cad_health", "scr_write", "accoreconsole_run"),
        "best_for": "DWG batch conversion, non-interactive script execution, plotting, DXFOUT, and repeatable file processing.",
    },
    {
        "id": "autocad_com_live",
        "tools": ("cad_health", "autocad_state", "autocad_open", "autocad_send_command", "autocad_lisp"),
        "best_for": "Running AutoCAD document state, visible UI control, layer reads, command dispatch, and live QA.",
    },
    {
        "id": "tianzheng_architecture",
        "tools": ("cad_health", "tianzheng_launch"),
        "best_for": "Chinese architecture workflows with Tianzheng walls, doors, windows, columns, axes, rooms, stairs, and annotations.",
    },
)


ENVART_CAD_LOCKS = (
    "drawing_units",
    "scale_ratio",
    "north_arrow",
    "site_boundary",
    "structural_axes",
    "outer_envelope",
    "wall_topology",
    "column_positions",
    "door_window_openings",
    "stair_core",
    "circulation_paths",
    "room_or_zone_names",
    "dimension_text",
    "title_block",
    "layer_semantics",
)


ENVART_CAD_OUTPUTS = (
    "cad_source_audit",
    "semantic_layer_report",
    "plan_fidelity_prompt",
    "analysis_diagram_prompt_pack",
    "competition_board_prompt_pack",
    "construction_drawing_qa",
    "dxf_or_dwg_processing_plan",
)


@dataclass(frozen=True)
class EnvArtCADPlan:
    task_type: str
    source_channel: str
    preferred_tools: tuple
    geometry_locks: tuple
    output_modes: tuple
    qa_gates: tuple
    notes: tuple

    def to_dict(self):
        return asdict(self)

    def to_json(self):
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)


class EnvArtCADMCPBridge:
    """Map environmental-art requests onto CADMCP control channels and QA locks."""

    def plan(self, task_text):
        lowered = str(task_text or "").lower()
        channel = self._select_channel(lowered)
        outputs = self._select_outputs(lowered)
        notes = self._notes_for(lowered, channel)
        return EnvArtCADPlan(
            task_type="envart_cadmcp_fusion",
            source_channel=channel["id"],
            preferred_tools=channel["tools"],
            geometry_locks=ENVART_CAD_LOCKS,
            output_modes=outputs,
            qa_gates=(
                "run cad_health before any CAD file operation",
                "inspect/audit DXF after generated or converted CAD output",
                "preserve wall, opening, column, axis, boundary, dimension, and title-block truth before aesthetic styling",
                "use semantic CAD layers instead of copying source layer 0 habits",
                "never let image-generation style override CAD topology",
                "keep analysis arrows, colors, hatches, and labels on top of locked base geometry",
            ),
            notes=notes,
        )

    def _select_channel(self, lowered):
        if any(token in lowered for token in ("天正", "tianzheng", "建筑构件", "墙体", "门窗", "轴网")):
            return CAD_CHANNELS[3]
        if any(token in lowered for token in ("dwg", "批处理", "转换", "core console", "accoreconsole")):
            return CAD_CHANNELS[1]
        if any(token in lowered for token in ("autocad", "实时", "当前图纸", "打开图纸", "com")):
            return CAD_CHANNELS[2]
        return CAD_CHANNELS[0]

    def _select_outputs(self, lowered):
        outputs = ["cad_source_audit", "semantic_layer_report"]
        if any(token in lowered for token in ("展板", "竞赛", "分析图", "diagram", "board")):
            outputs.extend(["analysis_diagram_prompt_pack", "competition_board_prompt_pack"])
        if any(token in lowered for token in ("施工图", "节点", "详图", "尺寸", "标注", "jgjt", "jgj")):
            outputs.append("construction_drawing_qa")
        if any(token in lowered for token in ("生图", "图生图", "image2", "提示词", "prompt")):
            outputs.append("plan_fidelity_prompt")
        if any(token in lowered for token in ("dwg", "dxf", "转换", "批处理")):
            outputs.append("dxf_or_dwg_processing_plan")
        return tuple(dict.fromkeys(outputs))

    def _notes_for(self, lowered, channel):
        notes = [
            f"Use {channel['id']} because: {channel['best_for']}",
            "Treat CAD geometry as source truth and board aesthetics as an overlay layer.",
        ]
        if "image2" in lowered or "图生图" in lowered:
            notes.append("For image2 prompts, lock aspect ratio, orientation, wall topology, openings, columns, axes, and source line hierarchy before style transfer.")
        if "展板" in lowered:
            notes.append("For boards, separate source plan, analysis overlays, spatial generation, axon/section, render, and text explanation into a clear reading order.")
        return tuple(notes)
