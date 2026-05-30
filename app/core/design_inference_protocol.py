from dataclasses import dataclass
from .models import DesignSessionState

IMAGE_REQUEST_KEYWORDS = ("生图", "生成图片", "出图", "生成图", "开始生成", "generate image", "render")
IMAGE_CONFIRM_KEYWORDS = ("确认生图", "确认出图", "可以生图", "可以出图", "确认生成", "approve image")

@dataclass(frozen=True)
class StepwiseResult:
    step: int
    title: str
    content: str
    recommend_image_generation: bool
    image_generation_allowed: bool
    image_generation_blocked: bool

class DesignInferenceProtocol:
    steps = {1: "需求边界推演", 2: "设计策略推演", 3: "生成准备推演"}

    def detect_image_request(self, text: str) -> bool:
        lowered = text.lower()
        return any(keyword.lower() in lowered for keyword in IMAGE_REQUEST_KEYWORDS)

    def detect_image_confirmation(self, text: str) -> bool:
        lowered = text.lower()
        return any(keyword.lower() in lowered for keyword in IMAGE_CONFIRM_KEYWORDS)

    def next_step(self, state: DesignSessionState) -> StepwiseResult:
        state.design_inference_step = min(state.design_inference_step + 1, 3)
        state.image_generation_requested = self.detect_image_request(state.prompt)
        state.image_generation_confirmed = state.image_generation_confirmed or self.detect_image_confirmation(state.prompt)
        if state.image_generation_requested and not state.image_generation_confirmed:
            state.image_generation_blocked = True
        state.image_generation_recommended = state.design_inference_step >= 3
        allowed = state.image_generation_requested and state.image_generation_confirmed
        return StepwiseResult(
            step=state.design_inference_step,
            title=self.steps[state.design_inference_step],
            content=self._content_for_step(state),
            recommend_image_generation=state.image_generation_recommended,
            image_generation_allowed=allowed,
            image_generation_blocked=state.image_generation_blocked and not allowed,
        )

    def _content_for_step(self, state: DesignSessionState) -> str:
        if state.design_inference_step == 1:
            return "锁定任务类型、受众、平台规格、交付形式、参考限制、是否涉及图片生成或最终视觉输出。"
        if state.design_inference_step == 2:
            return "拆解风格 DNA、构图系统、色彩字体、材质光影、参考图锁定、负向约束与可变创意空间。"
        return "整理可执行方案、PromptPacket 或交付清单；三步完成后主动推荐是否进入生图、出图或交付阶段，并等待用户确认。"
