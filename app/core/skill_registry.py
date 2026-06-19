from .models import SkillDefinition


SKILLS = (
    SkillDefinition(
        "DesignKernel",
        "kernel",
        "v2.1 design intelligence kernel: semantic vectors, state graph, probabilistic routing, aesthetic genome, memory retrieval, candidate ranking, constraint penalty, critic aggregation, failure memory, PromptPacketV2, LoopPromptPack, and LoopEngineeringBlueprint.",
        ("DesignKernel", "2.1", "math kernel", "state graph", "failure memory", "PromptPacketV2", "LoopEngineeringBlueprint", "\u6570\u5b66\u5185\u6838"),
    ),
    SkillDefinition(
        "DesignMathEngine",
        "algorithm",
        "Mathematical design layer: mixed-language n-grams, cosine/jaccard similarity, softmax routing, entropy, confidence margin, Pareto front, TOPSIS ranking, and constraint penalty.",
        ("math", "algorithm", "vector", "softmax", "TOPSIS", "Pareto", "constraint penalty", "\u6570\u5b66", "\u7b97\u6cd5"),
    ),
    SkillDefinition(
        "LoopEngineeringOS",
        "loop_engineering",
        "System-level Loop Engineering runtime blueprint: scheduler, worktree isolation, skill context, external connectors, executor/verifier split, persistent memory, handoff, stop conditions, and GitHub/CI/PR workflow alignment.",
        (
            "Loop Engineering",
            "agent loop",
            "scheduler",
            "event trigger",
            "worktree",
            "parallel",
            "validator",
            "verifier",
            "persistent memory",
            "GitHub",
            "CI",
            "issue",
            "PR",
            "\u8c03\u5ea6",
            "\u5b9a\u65f6",
            "\u4e8b\u4ef6\u89e6\u53d1",
            "\u5e76\u884c",
            "\u9a8c\u6536",
            "\u8bb0\u5fc6",
        ),
    ),
    SkillDefinition(
        "LoopPromptEngine",
        "prompt_loop",
        "Independent LoopPromptPack module for self-refine iteration, failed-result recovery, branch search, visual-result repair, and seamless video-loop prompts. It is a companion pack for PromptPacketV2, not a replacement.",
        ("loop", "iteration", "self critique", "failed-result recovery", "seamless loop", "LoopPromptPack", "\u5faa\u73af", "\u8fed\u4ee3", "\u81ea\u6211\u68c0\u67e5", "\u5931\u8d25\u4fee\u590d", "\u65e0\u7f1d\u5faa\u73af"),
    ),
    SkillDefinition("ReferenceModeOS", "reference", "Reference-image modes, DNA extraction, subject lock, edge and geometry constraints.", ("\u53c2\u8003\u56fe", "reference", "lock")),
    SkillDefinition("PromptOrchestrationEngine", "prompt", "PromptPacket orchestration for model-specific design prompts, reference locks, QA gates, and negative constraints.", ("prompt", "\u63d0\u793a\u8bcd", "PromptPacket")),
    SkillDefinition("EnvArtBoardOS", "environment", "Environmental art boards, spatial analysis diagrams, CAD/DWG/DXF geometry locks, layers, scale, and circulation logic.", ("\u73af\u827a", "\u5c55\u677f", "\u7a7a\u95f4", "CAD", "DWG", "DXF")),
    SkillDefinition("EnvArtCADMCPBridge", "environment_cad", "CADMCP bridge for environmental-art drawing channels: cad_health, DXF audit, DWG Core Console, AutoCAD COM, Tianzheng, semantic layers, and construction drawing QA.", ("cadmcp", "CADMCP", "DWG", "DXF", "AutoCAD", "\u5929\u6b63", "\u65bd\u5de5\u56fe", "\u56fe\u5c42", "\u5899\u4f53", "\u95e8\u7a97")),
    SkillDefinition("brandVIos", "brand", "Brand VI, logo, city identity, dynamic marks, color, type, visual systems, and brand deliverables.", ("\u54c1\u724c", "VI", "logo", "\u6807\u8bc6", "\u57ce\u5e02\u6807\u8bc6")),
    SkillDefinition("InfoVisOS", "infovis", "Information visualization, cultural diagrams, technical flows, maps, and data narratives.", ("\u4fe1\u606f\u53ef\u89c6\u5316", "\u56fe\u89e3", "\u6d41\u7a0b\u56fe", "\u5730\u56fe", "infovis")),
    SkillDefinition("PPTOS", "presentation", "PowerPoint, deck, report visuals, and page narrative.", ("PPT", "deck", "\u6c47\u62a5")),
    SkillDefinition("WebDesignOS", "web", "Web, UI, Figma pages, interactions, and design specifications.", ("\u7f51\u9875", "web", "UI", "Figma")),
    SkillDefinition("UIDesignSpecOS", "ui_spec", "UI design specifications, DESIGN.md, token-first systems, and QA rubrics.", ("design.md", "\u89c4\u8303", "token")),
    SkillDefinition("LayeredBoardComposer", "delivery", "Layered PSD, PNG, PDF, ZIP, manifest, and module assembly.", ("\u5206\u5c42", "PSD", "\u4ea4\u4ed8\u5305", "zip")),
    SkillDefinition("DeliveryFeedbackLayer", "feedback", "Delivery manifests, QA reports, feedback interpretation, patch writing, reward scoring, and training-loop updates.", ("\u53cd\u9988", "\u8bad\u7ec3", "\u4ea4\u4ed8")),
    SkillDefinition("TypographyDesignOS", "typography", "Typography posters, dynamic type, glyph rhythm, and layout experiments.", ("\u5b57\u4f53\u6d77\u62a5", "\u5b57\u4f53", "typography")),
    SkillDefinition("PosterDesignOS", "poster", "Poster key visuals, poster series, campaign visuals, and visual-impact optimization.", ("\u6d77\u62a5", "\u4e3b\u89c6\u89c9", "poster")),
    SkillDefinition("ShortDramaAIGC_OS", "video", "Short-drama AIGC, video storyboards, camera language, and generative video prompts.", ("\u77ed\u5267", "\u89c6\u9891", "\u5206\u955c", "Seedance")),
    SkillDefinition("GeneralDesignOS", "general", "General design task coordination and fallback strategy.", ("\u8bbe\u8ba1", "\u65b9\u6848")),
    SkillDefinition("PhotographyOS", "photography", "Photography and retouching module: portrait preservation, product photography, composition optimization, Hanfu shoots, lighting plans, and post-production QA.", ("photography", "photo", "retouch", "portrait", "product photo", "hanfu", "\u6444\u5f71", "\u4fee\u56fe", "\u4eba\u50cf", "\u4ea7\u54c1\u6444\u5f71", "\u7cbe\u4fee", "\u6c49\u670d", "\u6784\u56fe")),
    SkillDefinition("LoRAStyleTrainingLibrary", "lora", "Standalone style dataset sandbox, LoRA training plans, and adapter manifests.", ("LoRA", "\u8bad\u7ec3\u5e93", "\u98ce\u683c\u8bad\u7ec3")),
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
