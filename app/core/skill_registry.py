from .models import SkillDefinition

SKILLS = (
    SkillDefinition("ReferenceModeOS", "reference", "参考图 Mode 0-4 锁定、DNA、几何/主体/边缘约束", ("参考图", "复刻", "锁定")),
    SkillDefinition("PromptOrchestrationEngine", "prompt", "模型/技能/参考图约束的一体化 Prompt 编排和 QA", ("prompt", "提示词", "PromptPacket")),
    SkillDefinition("EnvArtBoardOS", "environment", "环艺展板、空间分析图、CAD/DWG/DXF 几何锁定、比例、图层语义与动线表达", ("环艺", "展板", "空间", "CAD", "DWG", "DXF")),
    SkillDefinition("EnvArtCADMCPBridge", "environment_cad", "融合 CADMCP 的环艺图纸通道：cad_health、DXF 审计、DWG Core Console、AutoCAD COM、天正建筑/结构与施工图 QA", ("cadmcp", "CADMCP", "DWG", "DXF", "AutoCAD", "天正", "施工图", "图层", "墙体", "门窗")),
    SkillDefinition("brandVIos", "brand", "品牌 VI、Logo、色彩、字体、视觉系统和品牌交付", ("品牌", "VI", "logo", "标志")),
    SkillDefinition("InfoVisOS", "infovis", "信息可视化、文化图谱、技术流程图与数据叙事", ("信息可视化", "图谱", "流程图")),
    SkillDefinition("PPTOS", "presentation", "PPT、路演 Deck、汇报视觉和页面叙事", ("PPT", "deck", "汇报")),
    SkillDefinition("WebDesignOS", "web", "Web/UI/Figma 页面、交互与设计规范", ("网页", "web", "UI", "Figma")),
    SkillDefinition("UIDesignSpecOS", "ui_spec", "UI 设计规范、DESIGN.md、Token First 与 QA Rubric", ("design.md", "规范", "token")),
    SkillDefinition("LayeredBoardComposer", "delivery", "分层 PSD、PNG、PDF、ZIP、Manifest 与模块裁切", ("分层", "PSD", "交付包", "zip")),
    SkillDefinition("AlgorithmicDesignEngine", "algorithm", "版式搜索、多目标评分、风格聚类和候选优化", ("算法", "评分", "候选")),
    SkillDefinition("DeliveryFeedbackLayer", "feedback", "交付、反馈解释、Patch、训练闭环和策略晋升", ("反馈", "训练", "交付")),
    SkillDefinition("TypographyDesignOS", "typography", "字体海报、动态字体、字形节奏和排版实验", ("字体海报", "字体", "typography")),
    SkillDefinition("PosterDesignOS", "poster", "海报主视觉、系列海报、活动视觉和视觉冲击力优化", ("海报", "主视觉", "poster")),
    SkillDefinition("ShortDramaAIGC_OS", "video", "短剧 AIGC、视频分镜、Seedance/即梦/TapNow 提示词", ("短剧", "视频", "分镜", "Seedance")),
    SkillDefinition("GeneralDesignOS", "general", "通用设计任务协调和兜底策略", ("设计", "方案")),
    SkillDefinition("PhotographyOS", "photography", "Photography and retouching module for portraits, product photography, composition optimization, Hanfu shoots, lighting schemes, and post-production QA.", ("photography", "photo", "retouch", "portrait", "product photo", "hanfu", "摄影", "修图", "人像", "产品摄影", "精修", "汉服", "构图")),
    SkillDefinition("LoRAStyleTrainingLibrary", "lora", "独立沙箱内的风格数据集、LoRA 训练计划和 adapter manifest", ("LoRA", "训练库", "风格训练")),
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
