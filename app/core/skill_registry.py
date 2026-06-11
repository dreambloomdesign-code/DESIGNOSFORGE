from .models import SkillDefinition


SKILLS = (
    SkillDefinition(
        "DesignKernel",
        "kernel",
        "v2.0 design intelligence kernel: semantic vectors, state graph, probabilistic routing, aesthetic genome, memory retrieval, candidate ranking, constraint penalty, critic aggregation, failure memory, and PromptPacketV2.",
        ("DesignKernel", "2.0", "math kernel", "state graph", "failure memory", "PromptPacketV2", "数学内核"),
    ),
    SkillDefinition(
        "DesignMathEngine",
        "algorithm",
        "Mathematical design layer: mixed-language n-grams, cosine/jaccard similarity, softmax routing, entropy, confidence margin, Pareto front, TOPSIS ranking, and constraint penalty.",
        ("math", "algorithm", "vector", "softmax", "TOPSIS", "Pareto", "constraint penalty", "数学", "算法"),
    ),
    SkillDefinition("ReferenceModeOS", "reference", "Reference-image modes, DNA extraction, subject lock, edge and geometry constraints.", ("参考图", "reference", "lock")),
    SkillDefinition("PromptOrchestrationEngine", "prompt", "PromptPacket orchestration for model-specific design prompts, reference locks, QA gates, and negative constraints.", ("prompt", "提示词", "PromptPacket")),
    SkillDefinition(
        "LoopPromptEngine",
        "prompt_loop",
        "Independent LoopPromptPack module for self-refine iteration, failed-result recovery, branch search, visual-result repair, and seamless video-loop prompts. It is a companion pack for PromptPacketV2, not a replacement.",
        ("loop", "循环", "迭代", "自我检查", "失败修复", "无缝循环", "LoopPromptPack"),
    ),
    SkillDefinition("EnvArtBoardOS", "environment", "Environmental art boards, spatial analysis diagrams, CAD/DWG/DXF geometry locks, layers, scale, and circulation logic.", ("环艺", "展板", "空间", "CAD", "DWG", "DXF")),
    SkillDefinition("EnvArtCADMCPBridge", "environment_cad", "CADMCP bridge for environmental-art drawing channels: cad_health, DXF audit, DWG Core Console, AutoCAD COM, Tianzheng, semantic layers, and construction drawing QA.", ("cadmcp", "CADMCP", "DWG", "DXF", "AutoCAD", "天正", "施工图", "图层", "墙体", "门窗")),
    SkillDefinition("brandVIos", "brand", "Brand VI, logo, city identity, dynamic marks, color, type, visual systems, and brand deliverables.", ("品牌", "VI", "logo", "标识", "城市标识")),
    SkillDefinition("InfoVisOS", "infovis", "Information visualization, cultural diagrams, technical flows, maps, and data narratives.", ("信息可视化", "图谱", "流程图", "地图", "infovis")),
    SkillDefinition("PPTOS", "presentation", "PowerPoint, deck, report visuals, and page narrative.", ("PPT", "deck", "汇报")),
    SkillDefinition("WebDesignOS", "web", "Web, UI, Figma pages, interactions, and design specifications.", ("网页", "web", "UI", "Figma")),
    SkillDefinition("UIDesignSpecOS", "ui_spec", "UI design specifications, DESIGN.md, token-first systems, and QA rubrics.", ("design.md", "规范", "token")),
    SkillDefinition("LayeredBoardComposer", "delivery", "Layered PSD, PNG, PDF, ZIP, manifest, and module assembly.", ("分层", "PSD", "交付包", "zip")),
    SkillDefinition("DeliveryFeedbackLayer", "feedback", "Delivery manifests, QA reports, feedback interpretation, patch writing, reward scoring, and training-loop updates.", ("反馈", "训练", "交付")),
    SkillDefinition("TypographyDesignOS", "typography", "Typography posters, dynamic type, glyph rhythm, and layout experiments.", ("字体海报", "字体", "typography")),
    SkillDefinition("PosterDesignOS", "poster", "Poster key visuals, poster series, campaign visuals, and visual-impact optimization.", ("海报", "主视觉", "poster")),
    SkillDefinition("ShortDramaAIGC_OS", "video", "Short-drama AIGC, video storyboards, camera language, and generative video prompts.", ("短剧", "视频", "分镜", "Seedance")),
    SkillDefinition("GeneralDesignOS", "general", "General design task coordination and fallback strategy.", ("设计", "方案")),
    SkillDefinition("PhotographyOS", "photography", "Photography and retouching module: portrait preservation, product photography, composition optimization, Hanfu shoots, lighting plans, and post-production QA.", ("photography", "photo", "retouch", "portrait", "product photo", "hanfu", "摄影", "修图", "人像", "产品摄影", "精修", "汉服", "构图")),
    SkillDefinition("LoRAStyleTrainingLibrary", "lora", "Standalone style dataset sandbox, LoRA training plans, and adapter manifests.", ("LoRA", "训练库", "风格训练")),
)


class SkillRegistry:
    def __init__(self, skills=SKILLS):
        self._skills = {skill.name: skill for skill in skills}

    def list(self):
        return list(self._skills.values())

    def get(self, name):
        return self._skills[name]

    def has(self, name):
        return name in self._skills
