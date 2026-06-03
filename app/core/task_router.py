from .models import RouteResult

ROUTES = (
    ("brand_vi", "brandVIos", ("品牌", "vi", "logo", "标志", "色卡")),
    ("typography_poster", "TypographyDesignOS", ("字体海报", "字体设计", "字形")),
    ("poster", "PosterDesignOS", ("海报", "主视觉", "活动视觉", "poster")),
    ("web_design", "WebDesignOS", ("网页", "web", "ui", "figma", "界面")),
    ("ppt", "PPTOS", ("ppt", "deck", "路演", "汇报")),
    ("info_vis", "InfoVisOS", ("信息可视化", "图谱", "流程图", "数据")),
    ("envart_cadmcp", "EnvArtCADMCPBridge", ("cadmcp", "dwg", "dxf", "autocad", "天正", "施工图", "图层", "墙体", "门窗", "轴网", "cad审图")),
    ("envart_board", "EnvArtBoardOS", ("环艺", "展板", "空间", "cad", "景观", "平面图", "立面图", "剖面图", "分析图")),
    ("short_video", "ShortDramaAIGC_OS", ("短剧", "视频", "分镜", "seedance", "即梦", "tapnow")),
    ("layered_psd", "LayeredBoardComposer", ("分层", "psd", "zip", "交付包", "manifest")),
    ("photography", "PhotographyOS", ("摄影", "修图", "人像", "产品摄影", "精修", "汉服", "构图", "photo", "retouch", "portrait", "product photo", "hanfu")),
    ("lora_training", "LoRAStyleTrainingLibrary", ("lora", "风格训练", "训练库", "adapter")),
    ("gitops", "GeneralDesignOS", ("git", "版本", "分支", "提交", "回滚")),
)

class TaskRouterAgent:
    def route(self, text):
        lowered = text.lower()
        for task_type, skill_name, keywords in ROUTES:
            if any(keyword.lower() in lowered for keyword in keywords):
                return RouteResult(task_type, skill_name, 0.88, f"matched keywords for {task_type}")
        return RouteResult("general_design", "GeneralDesignOS", 0.55, "fallback general design route")
