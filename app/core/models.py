from dataclasses import dataclass, field
from typing import Any

@dataclass(frozen=True)
class SkillDefinition:
    name: str
    domain: str
    description: str
    triggers: tuple[str, ...] = ()

@dataclass(frozen=True)
class RouteResult:
    task_type: str
    skill_name: str
    confidence: float
    reason: str

@dataclass
class DesignSessionState:
    prompt: str
    task_type: str = "general_design"
    skill_name: str = "GeneralDesignOS"
    design_inference_step: int = 0
    image_generation_requested: bool = False
    image_generation_confirmed: bool = False
    image_generation_blocked: bool = False
    image_generation_recommended: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)
