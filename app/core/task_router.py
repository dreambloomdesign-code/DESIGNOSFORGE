from .models import RouteResult


ROUTES = (
    ("brand_vi", "brandVIos", ("品牌", "vi", "logo", "标志", "城市标识", "色卡", "视觉识别")),
    ("typography_poster", "TypographyDesignOS", ("字体海报", "字体设计", "字形", "排版", "typography")),
    ("poster", "PosterDesignOS", ("海报", "主视觉", "活动视觉", "poster")),
    ("web_design", "WebDesignOS", ("网页", "网站", "web", "ui", "figma", "界面")),
    ("ppt", "PPTOS", ("ppt", "deck", "路演", "汇报", "演示")),
    ("info_vis", "InfoVisOS", ("信息可视化", "图谱", "流程图", "数据", "地图")),
    ("envart_cadmcp", "EnvArtCADMCPBridge", ("cadmcp", "dwg", "dxf", "autocad", "天正", "施工图", "图层", "墙体", "门窗", "轴网", "cad审图")),
    ("envart_board", "EnvArtBoardOS", ("环艺", "展板", "空间", "cad", "景观", "平面图", "立面图", "剖面图", "分析图")),
    ("short_video", "ShortDramaAIGC_OS", ("短剧", "视频", "分镜", "seedance", "即梦", "tapnow")),
    ("layered_psd", "LayeredBoardComposer", ("分层", "psd", "zip", "交付包", "manifest")),
    ("photography", "PhotographyOS", ("摄影", "修图", "人像", "产品摄影", "精修", "汉服", "构图", "拯救", "照片", "photo", "retouch", "portrait", "product photo", "hanfu")),
    ("lora_training", "LoRAStyleTrainingLibrary", ("lora", "风格训练", "训练库", "adapter", "训练集")),
    ("gitops", "GeneralDesignOS", ("git", "github", "版本", "分支", "提交", "回滚", "开源")),
)


class TaskRouterAgent:
    def route(self, text):
        lowered = str(text or "").lower()
        for task_type, skill_name, keywords in ROUTES:
            if any(keyword.lower() in lowered for keyword in keywords):
                return RouteResult(task_type, skill_name, 0.88, f"matched keywords for {task_type}")
        return RouteResult("general_design", "GeneralDesignOS", 0.55, "fallback general design route")
