PROMPT_PACKET_SECTIONS = (
    "01_TASK_BRIEF", "02_DESIGN_INTENT", "03_REFERENCE_LOCK", "04_STYLE_DNA",
    "05_COMPOSITION", "06_COLOR_TYPOGRAPHY", "07_MATERIAL_LIGHTING",
    "08_MODEL_RENDER_RULES", "09_NEGATIVE_PROMPT", "10_QA_CHECKLIST", "11_OUTPUT_SPEC",
)

class PromptPacketBuilder:
    def build(self, project_name, task, style=""):
        values = {
            "01_TASK_BRIEF": f"ProjectName: {project_name}\nTask: {task}",
            "02_DESIGN_INTENT": "Clarify communicative goal, audience, and visual promise.",
            "03_REFERENCE_LOCK": "Use ReferenceModeOS when references are provided; lock subject, geometry, proportion, edge contour, material, and lighting.",
            "04_STYLE_DNA": style or "Define style DNA from the task context; avoid generic templates.",
            "05_COMPOSITION": "Describe focal hierarchy, layout rhythm, spatial relationship, and negative space.",
            "06_COLOR_TYPOGRAPHY": "Define color palette, typography direction, contrast, and legibility rules.",
            "07_MATERIAL_LIGHTING": "Define material texture, lighting logic, render clarity, and atmosphere.",
            "08_MODEL_RENDER_RULES": "Generate only after user confirmation; keep outputs clean, usable, and aligned with constraints.",
            "09_NEGATIVE_PROMPT": "no generic stock poster, no distorted geometry, no fake official logo, no unresolved placeholders, no illegible text",
            "10_QA_CHECKLIST": "accuracy, legibility, visual impact, novelty, reference fidelity, delivery readiness",
            "11_OUTPUT_SPEC": "Return a complete, directly copyable PromptPacket; do not split or package the prompt.",
        }
        body = ["PromptPacket"]
        for section in PROMPT_PACKET_SECTIONS:
            body.append(f"\n[{section}]\n{values[section]}")
        return "\n".join(body)
