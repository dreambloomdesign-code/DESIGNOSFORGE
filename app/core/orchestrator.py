import json

from .aesthetic_quality import AestheticQualityGate
from .design_inference_protocol import DesignInferenceProtocol
from .design_kernel import DesignKernel
from .models import DesignSessionState
from .prompt_packet import PromptPacketBuilder
from .task_router import TaskRouterAgent


class MasterOrchestrator:
    def __init__(self):
        self.router = TaskRouterAgent()
        self.protocol = DesignInferenceProtocol()
        self.prompt_packet = PromptPacketBuilder()
        self.quality = AestheticQualityGate()
        self.kernel = DesignKernel()

    def run(self, prompt, confirm_image_generation=False, emit_prompt_packet=False):
        kernel_plan = self.kernel.plan(prompt).to_dict()
        route = kernel_plan["route"]
        state = DesignSessionState(
            prompt=prompt,
            task_type=route["task_type"],
            skill_name=route["skill_name"],
            image_generation_confirmed=confirm_image_generation,
        )
        if confirm_image_generation:
            state.prompt = f"确认生图 {state.prompt}"
        step = self.protocol.next_step(state)
        quality = self.quality.evaluate(prompt)
        route_math = kernel_plan["math_trace"]["route_probability"]
        candidate = kernel_plan["candidates"][0] if kernel_plan["candidates"] else {}
        lines = [
            "正在调用 DESIGNOSFORGE。",
            "",
            f"Kernel: DesignKernel v{kernel_plan['schema_version']}",
            f"TaskRoute: {route['task_type']} -> {route['skill_name']} ({route['confidence']})",
            f"RouteMath: winner={route_math.get('winner')}, entropy={route_math.get('entropy')}, margin={route_math.get('probability_margin')}",
            f"TopCandidate: {candidate.get('id', 'none')} score={candidate.get('final_score', 'n/a')}",
            f"InferenceStep: Step {step.step} - {step.title}",
            step.content,
        ]
        if quality.risks:
            lines.append(f"QualityGate: {', '.join(quality.risks)}")
        active_failures = kernel_plan["failure_memory"]["active_failure_modes"]
        if active_failures:
            lines.append(f"FailureMemory: {', '.join(active_failures)}")
        if step.image_generation_blocked:
            lines.append("ImageGate: 已拦截。用户未确认前不生图、不出最终图。")
        if step.recommend_image_generation:
            lines.append("Recommendation: 三步推演完成后，应主动询问是否确认进入生图、出图或交付阶段。")
        if emit_prompt_packet:
            lines.extend(["", json.dumps(kernel_plan["prompt_packet_v2"], ensure_ascii=False, indent=2)])
        return "\n".join(lines)
