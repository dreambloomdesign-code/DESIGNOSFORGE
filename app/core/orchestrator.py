from .design_inference_protocol import DesignInferenceProtocol
from .models import DesignSessionState
from .prompt_packet import PromptPacketBuilder
from .task_router import TaskRouterAgent

class MasterOrchestrator:
    def __init__(self):
        self.router = TaskRouterAgent()
        self.protocol = DesignInferenceProtocol()
        self.prompt_packet = PromptPacketBuilder()

    def run(self, prompt, confirm_image_generation=False, emit_prompt_packet=False):
        route = self.router.route(prompt)
        state = DesignSessionState(prompt=prompt, task_type=route.task_type, skill_name=route.skill_name, image_generation_confirmed=confirm_image_generation)
        if confirm_image_generation:
            state.prompt = f"确认生图 {state.prompt}"
        step = self.protocol.next_step(state)
        lines = ["正在调用 DESIGNOSFORGE。", "", f"TaskRoute: {route.task_type} -> {route.skill_name}", f"InferenceStep: Step {step.step}｜{step.title}", step.content]
        if step.image_generation_blocked:
            lines.append("ImageGate: 已拦截。用户未确认前不生图、不出最终图。")
        if step.recommend_image_generation:
            lines.append("Recommendation: 三步推演完成后，应主动询问是否确认进入生图/出图阶段。")
        if emit_prompt_packet:
            lines.extend(["", self.prompt_packet.build("DESIGNOSFORGE_TASK", prompt)])
        return "\n".join(lines)
