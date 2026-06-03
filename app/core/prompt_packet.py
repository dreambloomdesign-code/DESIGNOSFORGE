import json

from .aesthetic_quality import AestheticQualityGate
from app.lora_training.aesthetic_memory import AestheticMemoryIndex


PROMPT_PACKET_SECTIONS = (
    "01_TASK_BRIEF", "02_DESIGN_INTENT", "03_AUDIENCE_CONTEXT",
    "04_PROJECT_CONTEXT_LOCK", "05_CASE_MEMORY_SELECTION", "06_REFERENCE_LOCK",
    "07_AESTHETIC_THESIS", "08_COMPOSITION_HIERARCHY", "09_LAYOUT_GRID_DENSITY",
    "10_STYLE_DNA_MATERIAL", "11_COLOR_LIGHT_TYPOGRAPHY", "12_TEXT_ACCURACY",
    "13_MODEL_RENDER_RULES", "14_ANTI_FRAGMENTATION_NEGATIVE_PROMPT", "15_FAILURE_MEMORY",
    "16_QA_GATES", "17_DELIVERY_SPEC", "18_REVISION_PROTOCOL",
)

class PromptPacketBuilder:
    def build(self, project_name, task, style="", case_memory=""):
        quality = AestheticQualityGate().evaluate(f"{task} {style}")
        scores = quality.to_dict()["scores"]
        guardrails = "\n".join(f"- {item}" for item in quality.guardrails)
        inferred_domain, inferred_context = self._infer_memory_query(task)
        case_memory_text = case_memory or self._case_memory_text(inferred_domain, inferred_context)
        values = {
            "01_TASK_BRIEF": f"ProjectName: {project_name}\nTask: {task}",
            "02_DESIGN_INTENT": "Clarify the communicative goal, audience decision, visual promise, and success metric.",
            "03_AUDIENCE_CONTEXT": "Name the viewer, usage scenario, platform, aspect ratio, viewing distance, and delivery format.",
            "04_PROJECT_CONTEXT_LOCK": "Select one project context before style: commercial-project, academic-discipline-competition, cultural-china-research, public-cultural-communication, or another explicit context. Do not mix commercial conversion logic with academic research boards unless requested.",
            "05_CASE_MEMORY_SELECTION": case_memory_text,
            "06_REFERENCE_LOCK": "When references exist, lock subject, geometry, proportion, edge contour, material, lighting, and text placement before changing style.",
            "07_AESTHETIC_THESIS": style or "State one precise aesthetic thesis: one dominant mood, one visual metaphor, one material/lighting logic, no generic style labels.",
            "08_COMPOSITION_HIERARCHY": "Define one primary focal anchor, two secondary supports, reading path, scale contrast, and negative space.",
            "09_LAYOUT_GRID_DENSITY": "Define grid, margins, module rhythm, alignment, density ceiling, and what must stay visually quiet.",
            "10_STYLE_DNA_MATERIAL": "Specify shape language, edge quality, texture, material behavior, realism/stylization level, and allowable variation.",
            "11_COLOR_LIGHT_TYPOGRAPHY": "Define palette roles, contrast, light direction, shadow softness, type family mood, weight, size hierarchy, and spacing.",
            "12_TEXT_ACCURACY": "List exact visible text; keep copy short, readable, correctly spelled, not garbled, and never replaced with pseudo-text.",
            "13_MODEL_RENDER_RULES": "Generate only after user confirmation; keep outputs inspectable, clean, and aligned with locked constraints.",
            "14_ANTI_FRAGMENTATION_NEGATIVE_PROMPT": "Avoid: scattered tiny decorations, dirty texture noise, overfilled background, random icons, warped type, fake logos, unresolved placeholders, illegible text, mojibake, low-contrast clutter.",
            "15_FAILURE_MEMORY": "Record rejected attempts as failure modes, not positive references. State what must not repeat: wrong context, generic symbol stacking, unreadable type, dirty texture, or layout disorder.",
            "16_QA_GATES": f"Scores: {json.dumps(scores, ensure_ascii=False)}\nGuardrails:\n{guardrails}",
            "17_DELIVERY_SPEC": "Return the required artifact format, ratio, file/package expectations, preview needs, and downstream handoff notes.",
            "18_REVISION_PROTOCOL": "Revise by changing one axis at a time: composition, palette, typography, material, text, memory case, or density; preserve locked decisions.",
        }
        body = ["PromptPacket v1.6"]
        for section in PROMPT_PACKET_SECTIONS:
            body.append(f"\n[{section}]\n{values[section]}")
        return "\n".join(body)

    def _infer_memory_query(self, task):
        lowered = task.lower()
        if any(token in lowered for token in ("产品摄影", "产品修图", "棚拍", "电商图", "product photo", "product photography")):
            return "photography", "product-photo-production"
        if any(token in lowered for token in ("摄影", "修图", "人像", "精修", "汉服", "portrait", "retouch", "photo edit", "hanfu")):
            return "photography", "portrait-session"
        if any(token in lowered for token in ("高校", "学科竞赛", "文化中国", "文化旅游", "competition board")):
            return "exhibition-board", "academic-discipline-competition"
        if any(token in lowered for token in ("公共文化", "文化中心", "博物馆", "civic")):
            return "vi-brand", "public-cultural-communication"
        if any(token in lowered for token in ("包装", "产品", "商业", "retail", "package")):
            return "vi-brand", "commercial-project"
        if any(token in lowered for token in ("品牌", "vi", "logo", "标志")):
            return "vi-brand", "commercial-project"
        if any(token in lowered for token in ("展板", "环艺", "空间")):
            return "exhibition-board", "academic-discipline-competition"
        return "", ""

    def _case_memory_text(self, domain, context):
        try:
            recommendation = AestheticMemoryIndex().recommend(domain=domain, context=context, limit=3)
        except (FileNotFoundError, json.JSONDecodeError):
            recommendation = {"results": []}
        results = recommendation.get("results", [])
        if not results:
            return "No matching aesthetic-memory case is available. Use taxonomy-level project context and state exclusions explicitly."
        lines = [
            f"MemoryQuery: domain={domain or 'any'}, context={context or 'any'}",
            "Use these cases as references for structure, not as direct copies:",
        ]
        for result in results:
            positives = "; ".join(result.get("sample_positive_notes", [])[:2])
            negatives = "; ".join(result.get("sample_negative_notes", [])[:2])
            lines.append(f"- {result['batch_id']} | borrow: {positives or 'case structure'} | exclude: {negatives or 'exact protected text/assets'}")
        return "\n".join(lines)
