from .models import SkillDefinition


SKILLS = (
    SkillDefinition(
        "DesignKernel",
        "kernel",
        "v2.0 设计智能内核：语义向量、状态图、概率路由、审美基因、记忆检索、多目标候选排序、约束惩罚、评审聚合、失败记忆与 PromptPacketV2。",
        ("DesignKernel", "2.0", "数学内核", "状态图", "失败记忆", "PromptPacketV2"),
    ),
    SkillDefinition(
        "DesignMathEngine",
        "algorithm",
        "设计数学层：中文 n-gram 向量化、cosine/jaccard 相似度、softmax 路由、熵与置信边际、Pareto 前沿、TOPSIS 排序、约束惩罚模型。",
        ("数学", "算法", "向量", "softmax", "TOPSIS", "Pareto", "约束惩罚"),
    ),
    SkillDefinition("ReferenceModeOS", "reference", "参考图 Mode 0-4 锁定、DNA 提取、主体/边缘/几何约束。", ("参考图", "复刻", "锁定")),
    SkillDefinition("PromptOrchestrationEngine", "prompt", "模型、技能、参考图约束的一体化 Prompt 编排和 QA。", ("prompt", "提示词", "PromptPacket")),
    SkillDefinition("EnvArtBoardOS", "environment", "环艺展板、空间分析图、CAD/DWG/DXF 几何锁定、比例、图层语义与动线表达。", ("环艺", "展板", "空间", "CAD", "DWG", "DXF")),
    SkillDefinition("EnvArtCADMCPBridge", "environment_cad", "融合 CADMCP 的环艺图纸通道：cad_health、DXF 审计、DWG Core Console、AutoCAD COM、天正建筑/结构与施工图 QA。", ("cadmcp", "CADMCP", "DWG", "DXF", "AutoCAD", "天正", "施工图", "图层", "墙体", "门窗")),
    SkillDefinition("brandVIos", "brand", "品牌 VI、Logo、城市标识、动态标识、色彩、字体、视觉系统和品牌交付。", ("品牌", "VI", "logo", "标志", "城市标识")),
    SkillDefinition("InfoVisOS", "infovis", "信息可视化、文化图谱、技术流程图、地图和数据叙事。", ("信息可视化", "图谱", "流程图", "地图")),
    SkillDefinition("PPTOS", "presentation", "PPT、路演 Deck、汇报视觉和页面叙事。", ("PPT", "deck", "汇报")),
    SkillDefinition("WebDesignOS", "web", "Web/UI/Figma 页面、交互与设计规范。", ("网页", "web", "UI", "Figma")),
    SkillDefinition("UIDesignSpecOS", "ui_spec", "UI 设计规范、DESIGN.md、Token First 与 QA Rubric。", ("design.md", "规范", "token")),
    SkillDefinition("LayeredBoardComposer", "delivery", "分层 PSD、PNG、PDF、ZIP、Manifest 与模块装配。", ("分层", "PSD", "交付包", "zip")),
    SkillDefinition("DeliveryFeedbackLayer", "feedback", "交付、反馈解释、Patch、训练闭环和策略晋升。", ("反馈", "训练", "交付")),
    SkillDefinition("TypographyDesignOS", "typography", "字体海报、动态字体、字形节奏和排版实验。", ("字体海报", "字体", "typography")),
    SkillDefinition("PosterDesignOS", "poster", "海报主视觉、系列海报、活动视觉和视觉冲击力优化。", ("海报", "主视觉", "poster")),
    SkillDefinition("ShortDramaAIGC_OS", "video", "短剧 AIGC、视频分镜、镜头语言和生成式视频提示词。", ("短剧", "视频", "分镜", "Seedance")),
    SkillDefinition("GeneralDesignOS", "general", "通用设计任务协调和兜底策略。", ("设计", "方案")),
    SkillDefinition("PhotographyOS", "photography", "摄影与修图模块：人像保真、产品摄影、构图优化、汉服拍摄、布光方案和后期 QA。", ("photography", "photo", "retouch", "portrait", "product photo", "hanfu", "摄影", "修图", "人像", "产品摄影", "精修", "汉服", "构图")),
    SkillDefinition("LoRAStyleTrainingLibrary", "lora", "独立沙箱内的风格数据集、LoRA 训练计划和 adapter manifest。", ("LoRA", "训练库", "风格训练")),
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
