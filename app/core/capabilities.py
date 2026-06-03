from .skill_registry import SkillRegistry
from app import __version__

AGENTS = (
    "InputParserAgent", "TaskRouterAgent", "ReferenceModeOS", "ConstraintGraphAgent",
    "SkillProductComposer", "CreativeSearchAgent", "AestheticEvaluatorAgent",
    "PromptOrchestrationEngine", "ModelGateway", "QAAgent", "FeedbackInterpreter",
    "PatchApplier", "RewardModel", "TrajectoryLogger", "AgentTrainingEngine",
    "DeliveryAgent", "LoRAStyleTrainingLibrary", "LoRAAestheticSpace",
    "DesignInferenceProtocol", "GitOpsManager", "GitHubManager", "AestheticQualityGate", "PromptPrecisionCompiler",
    "TextEncodingGuard", "RedundancyReducer", "AestheticMemoryIndex", "ProjectContextRouter",
    "PhotographyOS", "PhotoRetouchingQualityGate",
    "EnvArtCADMCPBridge", "CADGeometryLockAgent", "CADLayerSemanticAuditor", "ConstructionDrawingQAGate",
)

def capability_report():
    registry = SkillRegistry()
    lines = [f"DESIGNOSFORGE v{__version__}", f"Agent Count: {len(AGENTS)}", f"Registered Skills: {len(registry.list())}", "", "Agents:"]
    lines.extend(f"- {agent}" for agent in AGENTS)
    lines.append("")
    lines.append("Skills:")
    lines.extend(f"- {skill.name}: {skill.description}" for skill in registry.list())
    return "\n".join(lines)
