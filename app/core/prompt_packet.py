import json

from .aesthetic_quality import AestheticQualityGate


PROMPT_PACKET_SECTIONS = (
    "01_TASK_BRIEF", "02_DESIGN_INTENT", "03_AUDIENCE_CONTEXT", "04_REFERENCE_LOCK",
    "05_AESTHETIC_THESIS", "06_COMPOSITION_HIERARCHY", "07_LAYOUT_GRID_DENSITY",
    "08_STYLE_DNA_MATERIAL", "09_COLOR_LIGHT_TYPOGRAPHY", "10_TEXT_ACCURACY",
    "11_MODEL_RENDER_RULES", "12_ANTI_FRAGMENTATION_NEGATIVE_PROMPT", "13_QA_GATES",
    "14_DELIVERY_SPEC", "15_REVISION_PROTOCOL",
)

class PromptPacketBuilder:
    def build(self, project_name, task, style=""):
        quality = AestheticQualityGate().evaluate(f"{task} {style}")
        scores = quality.to_dict()["scores"]
        guardrails = "\n".join(f"- {item}" for item in quality.guardrails)
        values = {
            "01_TASK_BRIEF": f"ProjectName: {project_name}\nTask: {task}",
            "02_DESIGN_INTENT": "Clarify the communicative goal, audience decision, visual promise, and success metric.",
            "03_AUDIENCE_CONTEXT": "Name the viewer, usage scenario, platform, aspect ratio, viewing distance, and delivery format.",
            "04_REFERENCE_LOCK": "When references exist, lock subject, geometry, proportion, edge contour, material, lighting, and text placement before changing style.",
            "05_AESTHETIC_THESIS": style or "State one precise aesthetic thesis: one dominant mood, one visual metaphor, one material/lighting logic, no generic style labels.",
            "06_COMPOSITION_HIERARCHY": "Define one primary focal anchor, two secondary supports, reading path, scale contrast, and negative space.",
            "07_LAYOUT_GRID_DENSITY": "Define grid, margins, module rhythm, alignment, density ceiling, and what must stay visually quiet.",
            "08_STYLE_DNA_MATERIAL": "Specify shape language, edge quality, texture, material behavior, realism/stylization level, and allowable variation.",
            "09_COLOR_LIGHT_TYPOGRAPHY": "Define palette roles, contrast, light direction, shadow softness, type family mood, weight, size hierarchy, and spacing.",
            "10_TEXT_ACCURACY": "List exact visible text; keep copy short, readable, correctly spelled, not garbled, and never replaced with pseudo-text.",
            "11_MODEL_RENDER_RULES": "Generate only after user confirmation; keep outputs inspectable, clean, and aligned with locked constraints.",
            "12_ANTI_FRAGMENTATION_NEGATIVE_PROMPT": "Avoid: scattered tiny decorations, dirty texture noise, overfilled background, random icons, warped type, fake logos, unresolved placeholders, illegible text, mojibake, low-contrast clutter.",
            "13_QA_GATES": f"Scores: {json.dumps(scores, ensure_ascii=False)}\nGuardrails:\n{guardrails}",
            "14_DELIVERY_SPEC": "Return the required artifact format, ratio, file/package expectations, preview needs, and downstream handoff notes.",
            "15_REVISION_PROTOCOL": "Revise by changing one axis at a time: composition, palette, typography, material, text, or density; preserve locked decisions.",
        }
        body = ["PromptPacket v1.5"]
        for section in PROMPT_PACKET_SECTIONS:
            body.append(f"\n[{section}]\n{values[section]}")
        return "\n".join(body)
