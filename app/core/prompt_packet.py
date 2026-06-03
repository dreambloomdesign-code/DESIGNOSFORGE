import json

from .design_kernel import DesignKernel


PROMPT_PACKET_SECTIONS = (
    "schema_version",
    "packet_type",
    "task_brief",
    "intent",
    "route",
    "aesthetic_genome",
    "memory_selection",
    "candidate_directions",
    "critic_scores",
    "hard_constraints",
    "soft_goals",
    "failure_memory",
    "math_trace",
    "tool_plan",
    "revision_protocol",
    "generation_policy",
)


class PromptPacketBuilder:
    """Backward-compatible builder that now emits PromptPacketV2."""

    def build(self, project_name, task, style="", case_memory=""):
        brief = task
        if project_name:
            brief = f"{project_name}: {task}"
        if style:
            brief = f"{brief}\nStyle: {style}"
        if case_memory:
            brief = f"{brief}\nCaseMemoryOverride: {case_memory}"
        packet = DesignKernel().plan(brief).to_dict()["prompt_packet_v2"]
        return json.dumps(packet, ensure_ascii=False, indent=2)
