import json
import re
from dataclasses import dataclass


MOJIBAKE_MARKERS = ("\ufffd", "\u951d", "\u9286", "\u9422", "\u7edb", "\u6d63", "\u00e5", "\u00e6", "\u00e7")
CLUTTER_MARKERS = ("细碎", "脏乱", "凌乱", "杂乱", "信息爆炸", "元素很多", "复杂背景", "碎片", "堆满")
GENERIC_STYLE_MARKERS = ("高级", "好看", "大气", "丰富", "酷", "有质感", "震撼")
LAYOUT_TERMS = ("网格", "层级", "留白", "主次", "对齐", "版心", "节奏", "负空间", "grid", "hierarchy", "negative space")
TEXT_TERMS = ("准确", "可读", "拼写", "不乱码", "标题", "字距", "行距", "legible", "spelled exactly")


@dataclass(frozen=True)
class QualityReport:
    aesthetic_cohesion: int
    layout_order: int
    text_precision: int
    encoding_health: int
    prompt_specificity: int
    redundancy_control: int
    risks: tuple
    guardrails: tuple

    def to_dict(self):
        return {
            "scores": {
                "aesthetic_cohesion": self.aesthetic_cohesion,
                "layout_order": self.layout_order,
                "text_precision": self.text_precision,
                "encoding_health": self.encoding_health,
                "prompt_specificity": self.prompt_specificity,
                "redundancy_control": self.redundancy_control,
            },
            "risks": list(self.risks),
            "guardrails": list(self.guardrails),
        }


class AestheticQualityGate:
    def evaluate(self, text):
        normalized = " ".join(str(text or "").split())
        lowered = normalized.lower()
        risks = []
        guardrails = []

        clutter_hits = self._hits(normalized, CLUTTER_MARKERS)
        if clutter_hits:
            risks.append(f"visual_clutter:{','.join(clutter_hits)}")
            guardrails.append("Collapse small decorative fragments into 1-2 large visual anchors; keep backgrounds quiet and inspectable.")
        else:
            guardrails.append("Use one dominant focal anchor, two secondary supports, and controlled negative space.")

        if not self._hits(normalized, LAYOUT_TERMS):
            risks.append("layout_order_missing")
            guardrails.append("Define grid, alignment, focal hierarchy, module spacing, and density ceiling before rendering.")

        if not self._hits(normalized, TEXT_TERMS):
            risks.append("text_precision_missing")
            guardrails.append("State exact visible text, spelling, hierarchy, max line count, and no-garbled-text rule.")

        mojibake_hits = self._hits(normalized, MOJIBAKE_MARKERS)
        if mojibake_hits:
            risks.append(f"encoding_risk:{','.join(mojibake_hits)}")
            guardrails.append("Repair mojibake before prompt or delivery; validate UTF-8 text paths and rendered copy.")

        generic_hits = self._hits(normalized, GENERIC_STYLE_MARKERS)
        if len(generic_hits) >= 2:
            risks.append(f"generic_style_language:{','.join(generic_hits)}")
            guardrails.append("Replace generic praise words with concrete palette, material, light, composition, and typography constraints.")

        repeated = self._repeated_terms(lowered)
        if repeated:
            risks.append(f"redundancy_risk:{','.join(repeated[:5])}")
            guardrails.append("Deduplicate repeated mechanisms; keep one owner for routing, one for QA, and one for delivery.")

        return QualityReport(
            aesthetic_cohesion=self._score(92, 14 * len(clutter_hits) + 6 * len(generic_hits)),
            layout_order=88 if self._hits(normalized, LAYOUT_TERMS) else 58,
            text_precision=90 if self._hits(normalized, TEXT_TERMS) else 60,
            encoding_health=100 if not mojibake_hits else 35,
            prompt_specificity=self._specificity_score(normalized, generic_hits),
            redundancy_control=90 if not repeated else max(45, 90 - 8 * len(repeated)),
            risks=tuple(risks),
            guardrails=tuple(dict.fromkeys(guardrails)),
        )

    def audit_json(self, text):
        return json.dumps(self.evaluate(text).to_dict(), ensure_ascii=False, indent=2)

    def guardrail_text(self, text):
        report = self.evaluate(text)
        return "\n".join(f"- {item}" for item in report.guardrails)

    def _hits(self, text, markers):
        return [marker for marker in markers if marker.lower() in text.lower()]

    def _score(self, base, penalty):
        return max(0, min(100, base - penalty))

    def _specificity_score(self, text, generic_hits):
        concrete_count = sum(1 for term in LAYOUT_TERMS + TEXT_TERMS if term.lower() in text.lower())
        length_bonus = min(18, len(text) // 80)
        return self._score(64 + length_bonus + concrete_count * 4, len(generic_hits) * 5)

    def _repeated_terms(self, lowered):
        tokens = re.findall(r"[a-zA-Z]{4,}|[\u4e00-\u9fff]{2,}", lowered)
        ignored = {"designosforge", "promptpacket", "output", "style"}
        counts = {}
        for token in tokens:
            if token in ignored:
                continue
            counts[token] = counts.get(token, 0) + 1
        return [token for token, count in counts.items() if count >= 4]
