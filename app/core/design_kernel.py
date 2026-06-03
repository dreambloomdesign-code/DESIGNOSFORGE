import json
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path

from app.lora_training.aesthetic_memory import AestheticMemoryIndex

from .aesthetic_quality import AestheticQualityGate
from .design_math import (
    ConstraintPenaltyModel,
    MultiObjectiveRanker,
    ScoreNormalizer,
    TextVectorizer,
    cosine,
    jaccard,
    weighted_sum,
)
from .envart_cadmcp import EnvArtCADMCPBridge
from .task_router import ROUTES, TaskRouterAgent


VERSION = "2.0.0"
FAILURE_MEMORY_PATH = Path("lora_training_sandbox/aesthetic_corpus/failure_memory.jsonl")


PROJECT_CONTEXT_KEYWORDS = {
    "commercial-project": ("商业", "品牌", "包装", "产品", "零售", "客户", "client", "retail", "campaign"),
    "academic-discipline-competition": ("高校", "学科竞赛", "竞赛", "课程", "研究", "展板", "competition"),
    "cultural-china-research": ("文化中国", "文化旅游", "非遗", "地域文化", "heritage"),
    "public-cultural-communication": ("公共文化", "城市", "博物馆", "文化中心", "标识", "civic", "museum"),
    "spatial-cad-production": ("cad", "dwg", "dxf", "autocad", "天正", "施工图", "墙体", "门窗", "轴网"),
    "portrait-session": ("人像", "修图", "精修", "摄影", "汉服", "照片", "纪实", "课堂", "活动", "portrait", "retouch"),
    "product-photo-production": ("产品摄影", "产品修图", "棚拍", "电商图", "product photo"),
    "experimental-design": ("实验", "探索", "先锋", "生成实验", "speculative"),
}


DOMAIN_KEYWORDS = {
    "vi-brand": ("品牌", "vi", "logo", "标志", "视觉识别", "城市标识"),
    "poster": ("海报", "主视觉", "活动视觉", "poster"),
    "typography": ("字体", "字形", "排版", "typography"),
    "exhibition-board": ("展板", "竞赛板", "汇报板", "board"),
    "environmental-art": ("环艺", "空间", "景观", "室内", "展陈", "cad", "dwg", "dxf"),
    "infovis": ("信息可视化", "图谱", "流程图", "地图", "数据"),
    "ui": ("ui", "界面", "app", "dashboard", "figma"),
    "web": ("网页", "网站", "web", "landing"),
    "packaging": ("包装", "盒", "瓶", "袋", "label"),
    "photography": ("摄影", "修图", "人像", "产品摄影", "照片", "纪实", "课堂纪实", "拯救", "photo", "retouch"),
    "short-video-aigc": ("短剧", "视频", "分镜", "镜头", "video"),
}


STYLE_AXIS_KEYWORDS = {
    "minimal-premium": ("极简", "高级", "留白", "克制", "premium"),
    "editorial-grid": ("网格", "编辑", "版心", "秩序", "grid"),
    "swiss-modern": ("瑞士", "现代主义", "几何", "sans"),
    "commercial-product": ("商业", "转化", "货架", "产品"),
    "soft-luxury": ("柔和", "奢感", "温润", "soft"),
    "tech-futurism": ("科技", "未来", "数字", "futurism"),
    "cultural-contemporary": ("文化", "当代", "地域", "东方"),
    "environmental-competition": ("环艺竞赛", "空间生成", "分析图", "展板"),
    "infographic-technical": ("技术图解", "流程", "说明图", "标注"),
    "natural-portrait-retouch": ("自然人像", "皮肤", "身份", "精修", "人物", "面貌", "不改脸"),
    "studio-product-lighting": ("棚拍", "布光", "反光", "产品摄影"),
    "composition-optimization": ("构图", "裁切", "透视", "主次", "拯救", "照片"),
    "hanfu-cultural-portrait": ("汉服", "古风", "国风", "簪花"),
    "cad-topology-fidelity": ("cad", "dwg", "dxf", "图层", "墙体", "门窗", "轴网"),
    "construction-drawing-logic": ("施工图", "节点", "尺寸", "标注", "材料"),
    "city-identity-dynamic-system": ("城市标识", "动态标志", "母子标", "网格推导", "城市品牌"),
}


@dataclass(frozen=True)
class DesignIntent:
    raw_text: str
    domains: tuple[str, ...]
    project_contexts: tuple[str, ...]
    style_axes: tuple[str, ...]
    delivery_modes: tuple[str, ...]
    hard_requirements: tuple[str, ...]
    risks: tuple[str, ...]


@dataclass(frozen=True)
class StateNode:
    id: str
    title: str
    owner: str
    inputs: tuple[str, ...] = ()
    outputs: tuple[str, ...] = ()
    gates: tuple[str, ...] = ()


@dataclass(frozen=True)
class CandidateDirection:
    id: str
    thesis: str
    composition: str
    memory_role: str
    risk_to_watch: str


@dataclass(frozen=True)
class CriticResult:
    critic: str
    score: int
    findings: tuple[str, ...]
    weight: float = 1.0


@dataclass(frozen=True)
class DesignKernelPlan:
    schema_version: str
    intent: dict
    route: dict
    aesthetic_genome: dict
    state_graph: list[dict]
    memory: dict
    candidates: list[dict]
    critics: list[dict]
    constraints: dict
    tool_plan: dict
    failure_memory: dict
    math_trace: dict
    prompt_packet_v2: dict

    def to_dict(self):
        return asdict(self)

    def to_json(self):
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)


class SemanticIntentParser:
    def __init__(self):
        self.vectorizer = TextVectorizer()

    def parse(self, text):
        raw = str(text or "")
        lowered = raw.lower()
        domains = self._score_vocab(lowered, DOMAIN_KEYWORDS)
        contexts = self._score_vocab(lowered, PROJECT_CONTEXT_KEYWORDS)
        axes = self._score_vocab(lowered, STYLE_AXIS_KEYWORDS)
        delivery = self._delivery_modes(lowered)
        hard = []
        risks = []
        if any(token in lowered for token in ("不要改变", "不改脸", "身份", "人物本来", "面貌", "identity")):
            hard.append("identity_lock")
            risks.append("identity_drift")
        if any(token in lowered for token in ("cad", "dwg", "dxf", "施工图", "墙体", "门窗", "轴网", "图层")):
            hard.append("source_geometry_lock")
            risks.append("cad_topology_drift")
        if any(token in lowered for token in ("乱码", "文字", "标题", "copy", "text", "排版")):
            hard.append("text_accuracy_lock")
            risks.append("text_error_or_mojibake")
        if any(token in lowered for token in ("细碎", "脏乱", "杂乱", "元素很多", "堆砌")):
            risks.append("fragmented_visual")
        if any(token in lowered for token in ("城市标识", "城市logo", "城市 logo", "马鞍山", "steel city")):
            risks.append("generic_symbol_stack")
        return DesignIntent(
            raw_text=raw,
            domains=tuple(domains or ("general-design",)),
            project_contexts=tuple(contexts or ("experimental-design",)),
            style_axes=tuple(axes or ("editorial-grid",)),
            delivery_modes=tuple(delivery),
            hard_requirements=tuple(dict.fromkeys(hard)),
            risks=tuple(dict.fromkeys(risks)),
        )

    def _score_vocab(self, lowered, vocab):
        query = self.vectorizer.tokens(lowered)
        scored = []
        for label, keywords in vocab.items():
            direct = sum(1.0 for keyword in keywords if keyword.lower() in lowered)
            keyword_vector = self.vectorizer.tokens(" ".join(keywords))
            vector_score = cosine(query, keyword_vector)
            score = direct + vector_score
            if score > 0.01:
                scored.append((score, label, direct, vector_score))
        scored.sort(key=lambda item: (-item[0], item[1]))
        return [label for _, label, _, _ in scored[:3]]

    def _delivery_modes(self, lowered):
        modes = []
        if any(token in lowered for token in ("prompt", "提示词", "生图", "图生图", "生成")):
            modes.append("prompt_packet")
        if any(token in lowered for token in ("照片", "修图", "拯救", "精修", "retouch", "photo edit")):
            modes.append("image_edit")
        if any(token in lowered for token in ("展板", "board", "a1", "a3")):
            modes.append("board")
        if any(token in lowered for token in ("cad", "dwg", "dxf", "施工图")):
            modes.append("cad_audit")
        if any(token in lowered for token in ("github", "开源", "发布", "版本", "tag")):
            modes.append("git_release")
        if not modes:
            modes.append("strategy")
        return tuple(dict.fromkeys(modes))


class HybridRouter:
    def __init__(self):
        self.keyword_router = TaskRouterAgent()
        self.vectorizer = TextVectorizer()

    def route(self, intent):
        keyword_route = self.keyword_router.route(intent.raw_text)
        scores = defaultdict(float)
        reasons = defaultdict(list)
        lowered = intent.raw_text.lower()
        query = self.vectorizer.tokens(lowered)

        for task_type, skill_name, keywords in ROUTES:
            direct_hits = [keyword for keyword in keywords if keyword.lower() in lowered]
            route_vector = self.vectorizer.tokens(" ".join(keywords))
            lexical = cosine(query, route_vector)
            score = len(direct_hits) * 4.0 + lexical * 2.0
            if score:
                scores[skill_name] += score
                reasons[skill_name].append({"source": task_type, "direct_hits": direct_hits, "lexical": round(lexical, 4)})

        domain_bonus = {
            "environmental-art": ("EnvArtBoardOS", 3.0),
            "photography": ("PhotographyOS", 3.5),
            "vi-brand": ("brandVIos", 3.0),
            "exhibition-board": ("LayeredBoardComposer", 2.5),
            "infovis": ("InfoVisOS", 2.5),
            "ui": ("UIDesignSpecOS", 2.5),
            "web": ("WebDesignOS", 2.5),
            "packaging": ("brandVIos", 1.5),
        }
        for domain in intent.domains:
            if domain in domain_bonus:
                skill, bonus = domain_bonus[domain]
                scores[skill] += bonus
                reasons[skill].append({"source": "domain_prior", "domain": domain, "bonus": bonus})

        if "spatial-cad-production" in intent.project_contexts:
            scores["EnvArtCADMCPBridge"] += 14.0
            reasons["EnvArtCADMCPBridge"].append({"source": "context_prior", "context": "spatial-cad-production", "bonus": 14.0})
        if "portrait-session" in intent.project_contexts or "product-photo-production" in intent.project_contexts:
            scores["PhotographyOS"] += 4.0
            reasons["PhotographyOS"].append({"source": "context_prior", "context": intent.project_contexts[0], "bonus": 4.0})
        if "public-cultural-communication" in intent.project_contexts:
            scores["brandVIos"] += 2.5
            reasons["brandVIos"].append({"source": "context_prior", "context": "public-cultural-communication", "bonus": 2.5})

        if not scores:
            scores[keyword_route.skill_name] += 1.0
            reasons[keyword_route.skill_name].append({"source": "keyword_router_fallback"})

        math_profile = self._math_profile(scores)

        if "spatial-cad-production" in intent.project_contexts:
            return self._route_payload("envart_cadmcp", "EnvArtCADMCPBridge", 0.98, keyword_route, scores, reasons, math_profile, "spatial-cad-production")
        if "photography" in intent.domains:
            return self._route_payload("photography", "PhotographyOS", 0.96, keyword_route, scores, reasons, math_profile, "photography")

        skill = math_profile["winner"]
        confidence = math_profile["confidence"]
        task_type = keyword_route.task_type if skill == keyword_route.skill_name else "design_kernel_routed"
        return self._route_payload(task_type, skill, confidence, keyword_route, scores, reasons, math_profile, "")

    def _math_profile(self, scores):
        labels = list(scores)
        values = [scores[label] for label in labels]
        probabilities = ScoreNormalizer.softmax(values, temperature=2.0)
        ranked = sorted(zip(labels, values, probabilities), key=lambda item: item[2], reverse=True)
        entropy = ScoreNormalizer.entropy(probabilities)
        best = ranked[0][2]
        second = ranked[1][2] if len(ranked) > 1 else 0.0
        confidence = ScoreNormalizer.confidence(best, second, entropy)
        return {
            "winner": ranked[0][0],
            "softmax_temperature": 2.0,
            "entropy": round(entropy, 4),
            "probability_margin": round(best - second, 4),
            "confidence": round(confidence, 4),
            "ranked_probabilities": [
                {"skill": label, "raw_score": round(score, 4), "probability": round(probability, 4)}
                for label, score, probability in ranked
            ],
        }

    def _route_payload(self, task_type, skill_name, confidence, keyword_route, scores, reasons, math_profile, forced=""):
        return {
            "task_type": task_type,
            "skill_name": skill_name,
            "confidence": round(float(confidence), 4),
            "reason": {
                "forced_context_or_domain": forced,
                "keyword_route": asdict(keyword_route),
                "hybrid_scores": {key: round(value, 4) for key, value in scores.items()},
                "score_reasons": {key: value for key, value in reasons.items()},
            },
            "math": math_profile,
        }


class DesignStateGraph:
    def build(self, intent, route):
        nodes = [
            StateNode("brief", "Requirement Boundary", "SemanticIntentParser", outputs=("intent", "risk_flags")),
            StateNode("memory", "Aesthetic Memory Retrieval", "DesignMemoryVectorIndex", inputs=("intent",), outputs=("case_memory", "failure_memory")),
            StateNode("constraints", "Constraint Solving", "ConstraintSolver", inputs=("intent", "source_assets"), outputs=("hard_constraints", "soft_goals", "penalty_vector")),
            StateNode("candidates", "Candidate Direction Search", "MultiCandidateGenerator", inputs=("intent", "case_memory", "constraints"), outputs=("ranked_candidate_directions",)),
            StateNode("critique", "Critic Ensemble", "CriticEnsemble", inputs=("candidate_directions", "constraints"), outputs=("critic_scores", "weighted_aggregate")),
            StateNode("tool_plan", "Tool Execution Plan", "ToolExecutionPlanner", inputs=("route", "constraints"), outputs=("tool_sequence",)),
            StateNode("delivery", "Delivery Contract", "DesignKernel", inputs=("approved_candidate", "tool_sequence"), outputs=("PromptPacketV2", "QAReport")),
            StateNode("learning", "Failure And Success Memory", "FailureMemoryBank", inputs=("user_feedback", "QAReport"), outputs=("memory_update",)),
        ]
        if route.get("skill_name") == "EnvArtCADMCPBridge":
            nodes.insert(2, StateNode("cadmcp", "CAD Source-Fidelity Pass", "EnvArtCADMCPBridge", inputs=("source_assets",), outputs=("cad_channel", "geometry_locks"), gates=("cad_health", "dxf_audit_when_available")))
        if "photography" in intent.domains:
            nodes.insert(2, StateNode("photo_truth", "Photo Identity And Light Lock", "PhotoTruthOS", inputs=("source_image",), outputs=("identity_lock", "retouch_chain"), gates=("do_not_change_identity",)))
        return [asdict(node) for node in nodes]


class AestheticGenomeExtractor:
    def extract(self, intent):
        domain = intent.domains[0]
        axes = set(intent.style_axes)
        return {
            "dominant_domain": domain,
            "composition_gene": self._composition_gene(domain, axes),
            "density_gene": "high-evidence-density" if "academic-discipline-competition" in intent.project_contexts else "controlled-medium-density",
            "color_gene": self._color_gene(axes),
            "typography_gene": "editable-exact-text / sans-hierarchy / no-pseudo-copy",
            "material_light_gene": self._material_gene(domain),
            "culture_translation_gene": "abstract structure before literal ornament" if "cultural-contemporary" in axes else "context-specific",
            "cleanliness_gene": "single anchor, quiet background, anti-fragmentation ceiling",
            "mathematical_gene": "vector similarity + multi-objective ranking + constraint penalty + critic aggregation",
        }

    def _composition_gene(self, domain, axes):
        if domain == "environmental-art":
            return "source plan as anchor + overlay analysis + axon/section support"
        if domain == "photography":
            return "subject identity anchor + light direction + background separation"
        if domain == "vi-brand":
            return "mark lockup + modular application system"
        if "city-identity-dynamic-system" in axes:
            return "grid-derived city mark + dynamic sublogo family + application proof"
        if "editorial-grid" in axes:
            return "strict editorial grid with modular hierarchy"
        return "one focal anchor with two supporting modules"

    def _color_gene(self, axes):
        if "cad-topology-fidelity" in axes:
            return "neutral CAD base + limited analysis accent colors"
        if "soft-luxury" in axes:
            return "warm restrained neutrals + soft contrast"
        if "tech-futurism" in axes:
            return "dark-light precision + luminous accent"
        if "city-identity-dynamic-system" in axes:
            return "civic base palette + semantic accent family"
        return "role-based palette: base, accent, hierarchy, warning"

    def _material_gene(self, domain):
        if domain == "packaging":
            return "credible substrate, edge, shadow, reflection"
        if domain == "photography":
            return "natural skin/product material, consistent light direction"
        if domain == "environmental-art":
            return "source drawing linework, material tags, spatial light logic"
        return "material named only when it has a visual role"


class DesignMemoryVectorIndex:
    def __init__(self):
        self.memory = AestheticMemoryIndex()
        self.vectorizer = TextVectorizer()

    def recommend(self, intent):
        domain = "" if intent.domains[0] == "general-design" else intent.domains[0]
        context = intent.project_contexts[0] if intent.project_contexts else ""
        style_axis = intent.style_axes[0] if intent.style_axes else ""
        base = self.memory.recommend(domain=domain, context=context, style_axis=style_axis, limit=5)
        query_tokens = self.vectorizer.tokens(intent.raw_text)
        results = base.get("results", [])
        for index, item in enumerate(results):
            sample_text = " ".join([
                item.get("case_id", ""),
                item.get("batch_id", ""),
                item.get("title", ""),
                item.get("domain", ""),
                item.get("project_context", ""),
                item.get("style_axis", ""),
                item.get("sample_caption", ""),
                " ".join(item.get("sample_positive_notes", [])),
                " ".join(item.get("sample_negative_notes", [])),
            ])
            sample_tokens = self.vectorizer.tokens(sample_text)
            lexical_similarity = cosine(query_tokens, sample_tokens)
            set_similarity = jaccard(query_tokens, sample_tokens)
            taxonomy_similarity = self._taxonomy_overlap(intent, item)
            taxonomy_prior = max(0.15, 1.0 - index * 0.12)
            memory_score = 0.42 * lexical_similarity + 0.12 * set_similarity + 0.31 * taxonomy_similarity + 0.15 * taxonomy_prior
            item["lexical_similarity"] = round(lexical_similarity, 4)
            item["jaccard_similarity"] = round(set_similarity, 4)
            item["taxonomy_similarity"] = round(taxonomy_similarity, 4)
            item["taxonomy_prior"] = round(taxonomy_prior, 4)
            item["memory_score"] = round(memory_score, 4)
        results.sort(key=lambda item: item.get("memory_score", 0.0), reverse=True)
        base["results"] = results
        base["ranking_mode"] = "taxonomy_filter + CJK_char_ngram_vector + cosine/jaccard/fused_score"
        base["math_trace"] = {
            "vectorizer": "mixed Latin word + Chinese char/bigram/trigram Counter",
            "query_feature_count": len(query_tokens),
            "score_formula": "0.42*cosine + 0.12*jaccard + 0.31*taxonomy_similarity + 0.15*taxonomy_prior",
            "top_scores": [
                {"case_id": item.get("case_id") or item.get("batch_id"), "memory_score": item.get("memory_score")}
                for item in results[:5]
            ],
        }
        return base

    def _taxonomy_overlap(self, intent, item):
        intent_labels = set(intent.domains) | set(intent.project_contexts) | set(intent.style_axes)
        item_labels = set()
        for key in ("primary_domain_ids", "secondary_domain_ids", "project_context_ids", "style_axis_ids"):
            item_labels.update(item.get(key, []))
        batch_id = str(item.get("batch_id", "")).lower()
        if "city-identity" in batch_id:
            item_labels.update(("vi-brand", "public-cultural-communication", "city-identity-dynamic-system"))
        if "photography" in batch_id:
            item_labels.update(("photography", "portrait-session", "product-photo-production", "composition-optimization", "natural-portrait-retouch"))
        if "envart" in batch_id or "cadmcp" in batch_id:
            item_labels.update(("environmental-art", "spatial-cad-production", "cad-topology-fidelity", "environmental-competition"))
        if "cultural-china" in batch_id:
            item_labels.update(("cultural-china-research", "public-cultural-communication", "exhibition-board", "infographic-technical"))
        if not intent_labels:
            return 0.0
        return len(intent_labels & item_labels) / len(intent_labels)


class MultiCandidateGenerator:
    OBJECTIVE_WEIGHTS = {
        "domain_fit": 0.24,
        "constraint_fit": 0.24,
        "memory_fit": 0.17,
        "clarity": 0.17,
        "risk_control": 0.12,
        "novelty": 0.06,
    }

    def __init__(self):
        self.ranker = MultiObjectiveRanker()

    def generate(self, intent, memory, constraints, route):
        domain = intent.domains[0]
        if domain == "environmental-art":
            candidates = (
                CandidateDirection("source_fidelity", "CAD source truth as visual authority", "locked plan base with sparse analysis overlays", "borrow geometry-lock and QA methods", "topology drift"),
                CandidateDirection("evidence_board", "Spatial reasoning becomes an evidence chain", "site -> problem -> strategy -> plan -> axon -> material", "borrow competition board hierarchy", "overdense tiny diagrams"),
                CandidateDirection("technical_editorial", "Technical clarity with editorial restraint", "large drawing anchor plus narrow annotation rail", "borrow thin-line infovis discipline", "decorative hatches"),
            )
        elif domain == "photography":
            candidates = (
                CandidateDirection("photo_truth", "Preserve identity and scene truth", "subject anchor, natural light, gentle cleanup", "borrow retouch QA", "face drift or plastic skin"),
                CandidateDirection("editorial_documentary", "Documentary image with public-account polish", "clean crop, hierarchy, background suppression", "borrow composition memory", "fake studio look"),
                CandidateDirection("product_light", "Controlled material and edge readability", "product anchor, credible contact shadow, label plane", "borrow studio lighting memory", "fake labels"),
            )
        elif domain == "vi-brand":
            candidates = (
                CandidateDirection("grid_city_mark", "City identity starts from a repeatable geometric grammar", "primary mark + grid proof + dynamic submarks + civic applications", "borrow city identity logo systems", "generic landmark stacking"),
                CandidateDirection("letter_place_system", "Letterform and place features fuse into a modular civic sign", "lettermark core, semantic color family, bilingual lockups", "borrow dynamic logo systems", "weak local specificity"),
                CandidateDirection("industrial_culture_abstraction", "Industrial heritage becomes abstract rhythm, not literal steel icons", "compressed geometry, strong negative space, restrained applications", "borrow public-cultural identity memory", "too heavy or corporate"),
            )
        else:
            candidates = (
                CandidateDirection("clean_system", "System clarity over decoration", "one anchor, two supports, strict grid", "borrow closest memory case", "generic style language"),
                CandidateDirection("cultural_modern", "Cultural meaning translated into structure", "symbol abstraction with quiet negative space", "borrow cultural-contemporary cases", "literal ornament stacking"),
                CandidateDirection("high_impact", "Strong public-facing recognition", "large mark/title anchor and restrained applications", "borrow brand/poster memory", "visual clutter"),
            )

        ranked_input = []
        for index, candidate in enumerate(candidates):
            item = asdict(candidate)
            item["metrics"] = self._metrics(index, item, intent, memory, constraints, route)
            ranked_input.append(item)
        return self.ranker.rank(ranked_input, self.OBJECTIVE_WEIGHTS)

    def _metrics(self, index, candidate, intent, memory, constraints, route):
        residual_risk = constraints.get("penalty_vector", {}).get("residual_risk", 0.35)
        memory_scores = [item.get("memory_score", 0.0) for item in memory.get("results", [])[:3]]
        memory_fit = sum(memory_scores) / len(memory_scores) if memory_scores else 0.35
        domain_fit = 0.9 if intent.domains[0] != "general-design" else 0.55
        if candidate["id"] in ("photo_truth", "source_fidelity", "grid_city_mark"):
            domain_fit += 0.06
        constraint_fit = constraints.get("penalty_vector", {}).get("constraint_satisfaction", 0.7)
        clarity = 0.74 + 0.05 * int("anchor" in candidate["composition"]) + 0.04 * int("grid" in candidate["composition"])
        route_match = 0.04 if route.get("skill_name") in ("EnvArtCADMCPBridge", "PhotographyOS", "brandVIos") else 0.0
        risk_control = max(0.0, min(1.0, 1.0 - residual_risk + route_match - 0.03 * index))
        novelty = max(0.35, 0.72 - 0.08 * index + 0.05 * int("abstract" in candidate["thesis"].lower()))
        return {
            "domain_fit": round(min(1.0, domain_fit), 4),
            "constraint_fit": round(constraint_fit, 4),
            "memory_fit": round(min(1.0, memory_fit), 4),
            "clarity": round(min(1.0, clarity), 4),
            "risk_control": round(risk_control, 4),
            "novelty": round(novelty, 4),
        }


class CriticEnsemble:
    WEIGHTS = {
        "AestheticCritic": 0.24,
        "DomainCritic": 0.20,
        "ConstraintCritic": 0.22,
        "CandidateCritic": 0.18,
        "MemoryCritic": 0.10,
        "TextCritic": 0.03,
        "IdentityCritic": 0.03,
    }

    def evaluate(self, intent, candidates, constraints, memory):
        text = intent.raw_text
        quality = AestheticQualityGate().evaluate(text).to_dict()
        base_score = int(sum(quality["scores"].values()) / len(quality["scores"]))
        critics = [
            CriticResult("AestheticCritic", base_score, tuple(quality.get("guardrails", [])[:3]), self.WEIGHTS["AestheticCritic"]),
            CriticResult("DomainCritic", self._domain_score(intent), tuple(self._domain_findings(intent)), self.WEIGHTS["DomainCritic"]),
            CriticResult("ConstraintCritic", self._constraint_score(constraints), tuple(constraints.get("risk_controls", [])[:3]), self.WEIGHTS["ConstraintCritic"]),
            CriticResult("CandidateCritic", self._candidate_score(candidates), tuple(candidate["risk_to_watch"] for candidate in candidates[:3]), self.WEIGHTS["CandidateCritic"]),
            CriticResult("MemoryCritic", self._memory_score(memory), tuple(self._memory_findings(memory)), self.WEIGHTS["MemoryCritic"]),
        ]
        if "text_accuracy_lock" in intent.hard_requirements:
            critics.append(CriticResult("TextCritic", 88, ("exact visible text required", "UTF-8 and no pseudo-copy gate active"), self.WEIGHTS["TextCritic"]))
        if "identity_lock" in intent.hard_requirements:
            critics.append(CriticResult("IdentityCritic", 92, ("preserve face, body, expression, clothing, and pose",), self.WEIGHTS["IdentityCritic"]))
        metrics = {critic.critic: critic.score / 100 for critic in critics}
        weights = {critic.critic: critic.weight for critic in critics}
        aggregate = int(round(weighted_sum(metrics, weights) * 100))
        critics.append(CriticResult("KernelAggregateCritic", aggregate, ("weighted_sum(score_i, critic_weight_i)", "critic scores are normalized to 0..1 before aggregation"), 1.0))
        return [asdict(critic) for critic in critics]

    def _domain_score(self, intent):
        return 94 if intent.domains[0] != "general-design" else 70

    def _domain_findings(self, intent):
        return [f"primary_domain={intent.domains[0]}", f"primary_context={intent.project_contexts[0]}"]

    def _constraint_score(self, constraints):
        satisfaction = constraints.get("penalty_vector", {}).get("constraint_satisfaction", 0.76)
        return int(round(55 + satisfaction * 40))

    def _candidate_score(self, candidates):
        return int(round(70 + min(0.25, candidates[0].get("final_score", 0.0)) * 100)) if candidates else 70

    def _memory_score(self, memory):
        top = memory.get("results", [{}])[0].get("memory_score", 0.0) if memory.get("results") else 0.0
        return int(round(60 + min(0.4, top) * 90))

    def _memory_findings(self, memory):
        results = memory.get("results", [])
        if not results:
            return ("no memory case matched; use conservative generic design gates",)
        top_case = results[0].get("case_id") or results[0].get("batch_id")
        return (f"top_case={top_case}", f"top_memory_score={results[0].get('memory_score')}")


class ConstraintSolver:
    def __init__(self):
        self.penalty_model = ConstraintPenaltyModel()

    def solve(self, intent):
        hard = list(intent.hard_requirements)
        soft = ["one dominant visual anchor", "explicit grid", "controlled density", "exact text policy"]
        risk_controls = list(intent.risks)
        cad_plan = None
        if "source_geometry_lock" in hard or "spatial-cad-production" in intent.project_contexts:
            cad_plan = EnvArtCADMCPBridge().plan(intent.raw_text).to_dict()
            hard.extend(cad_plan["geometry_locks"])
            risk_controls.extend(["run cad_health", "audit converted DXF", "keep analysis overlays separate from base geometry"])
        if "identity_lock" in hard or "photography" in intent.domains:
            hard.extend(["face_identity", "body_anatomy", "expression", "clothing", "light_direction"])
            risk_controls.extend(["no face replacement", "no plastic skin", "local corrections before global grading"])
        if "vi-brand" in intent.domains:
            hard.extend(["single mark grammar", "grid derivation", "dynamic submark system", "application proof"])
            risk_controls.extend(["no random landmark stacking", "local symbol must be abstracted into repeatable geometry"])
        constraints = {
            "hard_constraints": tuple(dict.fromkeys(hard)),
            "soft_goals": tuple(dict.fromkeys(soft)),
            "risk_controls": tuple(dict.fromkeys(risk_controls)),
            "cad_plan": cad_plan,
        }
        constraints["penalty_vector"] = self.penalty_model.penalty_vector(intent, constraints)
        constraints["mathematical_model"] = "residual_risk = max(0, risk_load + complexity - mitigation_strength) / 2.25"
        return constraints


class ToolExecutionPlanner:
    def plan(self, intent, route, constraints):
        steps = ["parse_intent", "retrieve_memory", "solve_constraints", "rank_candidates", "run_critic_ensemble"]
        tools = []
        if constraints.get("cad_plan"):
            tools.extend(constraints["cad_plan"].get("preferred_tools", []))
        if "prompt_packet" in intent.delivery_modes:
            tools.append("PromptPacketV2")
        if "git_release" in intent.delivery_modes:
            tools.extend(["GitOpsManager", "GitHubManager"])
        if route["skill_name"] == "PhotographyOS":
            tools.extend(["identity_lock", "local_retouch_chain", "composition_crop_plan"])
        return {
            "route_skill": route["skill_name"],
            "steps": tuple(dict.fromkeys(steps)),
            "tools": tuple(dict.fromkeys(tools)),
            "requires_user_confirmation": "image_generation" if "prompt_packet" in intent.delivery_modes else "",
        }


class FailureMemoryBank:
    def __init__(self, path=FAILURE_MEMORY_PATH):
        self.path = Path(path)
        self.vectorizer = TextVectorizer()

    def summarize(self, intent):
        items = self._load()
        query = self.vectorizer.tokens(intent.raw_text)
        relevant = []
        for item in items[-120:]:
            item_text = " ".join([item.get("task", ""), item.get("domain", ""), item.get("failure_mode", ""), item.get("note", "")])
            similarity = cosine(query, self.vectorizer.tokens(item_text))
            domain_bonus = 0.25 if item.get("domain") in intent.domains else 0.0
            relevance_score = similarity + domain_bonus
            if relevance_score > 0.08:
                clone = dict(item)
                clone["relevance_score"] = round(relevance_score, 4)
                relevant.append(clone)
        relevant.sort(key=lambda item: item["relevance_score"], reverse=True)
        return {
            "path": self.path.as_posix(),
            "total_items": len(items),
            "relevant_items": relevant[:5],
            "active_failure_modes": tuple(dict.fromkeys(intent.risks)),
            "math_trace": {
                "matching": "cosine(query_ngram_vector, failure_ngram_vector) + domain_bonus",
                "query_feature_count": len(query),
            },
        }

    def record(self, task, domain, failure_mode, note):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        item = {
            "schema_version": VERSION,
            "task": task,
            "domain": domain,
            "failure_mode": failure_mode,
            "note": note,
        }
        with self.path.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(json.dumps(item, ensure_ascii=False) + "\n")
        return item

    def _load(self):
        if not self.path.exists():
            return []
        items = []
        for line in self.path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                items.append(json.loads(line))
        return items


class PromptPacketV2Builder:
    def build(self, intent, route, genome, memory, candidates, critics, constraints, tool_plan, failure_memory, math_trace):
        return {
            "schema_version": VERSION,
            "packet_type": "PromptPacketV2",
            "task_brief": intent.raw_text,
            "intent": asdict(intent),
            "route": route,
            "aesthetic_genome": genome,
            "memory_selection": memory.get("results", []),
            "candidate_directions": candidates,
            "critic_scores": critics,
            "hard_constraints": constraints.get("hard_constraints", ()),
            "soft_goals": constraints.get("soft_goals", ()),
            "failure_memory": failure_memory,
            "math_trace": math_trace,
            "tool_plan": tool_plan,
            "revision_protocol": "Revise one axis at a time: intent, memory, candidate, layout, color, typography, source lock, text, or delivery.",
            "generation_policy": "Do not generate or edit final visuals until the user confirms image generation.",
        }


class DesignKernel:
    def __init__(self):
        self.intent_parser = SemanticIntentParser()
        self.router = HybridRouter()
        self.graph = DesignStateGraph()
        self.genome = AestheticGenomeExtractor()
        self.memory = DesignMemoryVectorIndex()
        self.constraints = ConstraintSolver()
        self.candidates = MultiCandidateGenerator()
        self.critics = CriticEnsemble()
        self.tool_plan = ToolExecutionPlanner()
        self.failures = FailureMemoryBank()
        self.packet = PromptPacketV2Builder()

    def plan(self, text):
        intent = self.intent_parser.parse(text)
        route = self.router.route(intent)
        genome = self.genome.extract(intent)
        memory = self.memory.recommend(intent)
        constraints = self.constraints.solve(intent)
        candidates = self.candidates.generate(intent, memory, constraints, route)
        critics = self.critics.evaluate(intent, candidates, constraints, memory)
        tool_plan = self.tool_plan.plan(intent, route, constraints)
        failure_memory = self.failures.summarize(intent)
        state_graph = self.graph.build(intent, route)
        math_trace = self._math_trace(route, memory, constraints, candidates, critics, failure_memory)
        prompt_packet = self.packet.build(intent, route, genome, memory, candidates, critics, constraints, tool_plan, failure_memory, math_trace)
        return DesignKernelPlan(
            schema_version=VERSION,
            intent=asdict(intent),
            route=route,
            aesthetic_genome=genome,
            state_graph=state_graph,
            memory=memory,
            candidates=candidates,
            critics=critics,
            constraints=constraints,
            tool_plan=tool_plan,
            failure_memory=failure_memory,
            math_trace=math_trace,
            prompt_packet_v2=prompt_packet,
        )

    def _math_trace(self, route, memory, constraints, candidates, critics, failure_memory):
        aggregate = next((critic for critic in critics if critic["critic"] == "KernelAggregateCritic"), {})
        return {
            "kernel_version": VERSION,
            "state_model": "directed acyclic design-state graph",
            "text_vector_space": "Counter features with Latin words, Chinese chars, Chinese bigrams, and Chinese trigrams",
            "route_probability": route.get("math", {}),
            "memory_similarity": memory.get("math_trace", {}),
            "constraint_penalty": constraints.get("penalty_vector", {}),
            "candidate_optimization": {
                "method": "Pareto front + TOPSIS + normalized weighted utility",
                "objective_weights": MultiCandidateGenerator.OBJECTIVE_WEIGHTS,
                "ranked_scores": [
                    {
                        "id": candidate["id"],
                        "rank": candidate["rank"],
                        "final_score": candidate["final_score"],
                        "pareto_front": candidate["pareto_front"],
                    }
                    for candidate in candidates
                ],
            },
            "critic_aggregation": {
                "method": "weighted_sum(score_i, critic_weight_i)",
                "aggregate_score": aggregate.get("score"),
            },
            "failure_memory_similarity": failure_memory.get("math_trace", {}),
        }
