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
    "DesignKernel", "DesignMathEngine", "TextVectorizer", "ScoreNormalizer", "MultiObjectiveRanker",
    "ConstraintPenaltyModel", "DesignStateGraph", "HybridRouter", "AestheticGenomeExtractor",
    "DesignMemoryVectorIndex", "FailureMemoryBank", "MultiCandidateGenerator",
    "CriticEnsemble", "ConstraintSolver", "ToolExecutionPlanner", "PromptPacketV2Builder",
    "LoopPromptEngine", "LoopPromptPackBuilder", "LoopEngineeringBlueprintBuilder", "LoopEngineeringOS",
)

CALL_TABLE = (
    ("general_design_strategy", "DesignKernel", "PromptPacketV2", "route math, critic aggregation, constraints"),
    ("iterative_prompt_refinement", "LoopPromptEngine", "LoopPromptPack", "one-axis iteration, stop conditions, failure memory"),
    ("durable_agent_loop", "LoopEngineeringOS", "LoopEngineeringBlueprint", "scheduler, worktree isolation, verifier split, persistent memory"),
    ("brand_vi_city_identity", "brandVIos", "PromptPacketV2", "grid derivation, dynamic system, no random landmark stacking"),
    ("academic_infovis_board", "InfoVisOS/LayeredBoardComposer", "PromptPacketV2", "thesis hierarchy, evidence modules, text accuracy"),
    ("envart_cad_production", "EnvArtCADMCPBridge", "CAD-aware plan", "CAD health, DXF audit, geometry locks"),
    ("photography_retouching", "PhotographyOS", "edit or shoot plan", "identity preservation, light direction, artifact check"),
    ("github_release_work", "GitHubManager/GitOpsManager", "release plan or PR body", "compileall, tests, source validator, CI/PR checks"),
)

def capability_report():
    registry = SkillRegistry()
    lines = [f"DESIGNOSFORGE v{__version__}", f"Agent Count: {len(AGENTS)}", f"Registered Skills: {len(registry.list())}", "", "Agents:"]
    lines.extend(f"- {agent}" for agent in AGENTS)
    lines.append("")
    lines.append("Skills:")
    lines.extend(f"- {skill.name}: {skill.description}" for skill in registry.list())
    lines.append("")
    lines.append("Capability Call Table:")
    lines.extend(f"- {intent}: route={route}; output={output}; validation={validation}" for intent, route, output, validation in CALL_TABLE)
    return "\n".join(lines)
