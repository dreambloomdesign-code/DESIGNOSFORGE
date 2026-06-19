import json

from app.core.aesthetic_quality import AestheticQualityGate
from app.core.capabilities import capability_report
from app.core.design_kernel import DesignKernel
from app.core.loop_prompt import LoopEngineeringBlueprintBuilder, LoopPromptPackBuilder
from app.core.prompt_packet import PROMPT_PACKET_SECTIONS, PromptPacketBuilder
from app.core.skill_registry import SkillRegistry
from app.core.task_router import TaskRouterAgent
from app.management.skill_registry_sync import SkillRegistrySyncAgent


def test_capabilities_include_core_agents():
    report = capability_report()
    assert "DESIGNOSFORGE v2.1.0" in report
    assert "PromptPacketV2Builder" in report
    assert "LoopPromptEngine" in report
    assert "LoopEngineeringOS" in report
    assert "Capability Call Table" in report
    assert "durable_agent_loop" in report
    assert "AestheticMemoryIndex" in report
    assert "GitOpsManager" in report
    assert "GitHubManager" in report


def test_skill_registry_has_expected_skills():
    registry = SkillRegistry()
    assert registry.has("brandVIos")
    assert registry.has("LoopPromptEngine")
    assert registry.has("LoopEngineeringOS")
    assert registry.has("PhotographyOS")


def test_task_router_routes_design_domains():
    router = TaskRouterAgent()
    assert router.route("make a brand logo VI system").skill_name == "brandVIos"
    assert router.route("create a typography poster").skill_name == "TypographyDesignOS"


def test_prompt_packet_v2_keeps_original_contract():
    packet_text = PromptPacketBuilder().build("test", "make a logo")
    packet = json.loads(packet_text)
    for section in PROMPT_PACKET_SECTIONS:
        assert section in packet
    assert packet["packet_type"] == "PromptPacketV2"
    assert "LoopPromptPack" not in packet


def test_loop_prompt_pack_is_independent_companion():
    pack = LoopPromptPackBuilder().build("create a design prompt with three loop iterations and self critique")
    assert pack["packet_type"] == "LoopPromptPack"
    assert pack["relationship_to_prompt_packet_v2"]["mode"] == "independent_companion_pack"
    assert pack["relationship_to_prompt_packet_v2"]["does_not_replace_prompt_packet_v2"] is True
    assert pack["activation"]["active"] is True
    assert pack["loop_contract"]["loop_type"] == "self_refine_loop"


def test_loop_engineering_blueprint_answers_six_questions():
    blueprint = LoopEngineeringBlueprintBuilder().build(
        "系统性革新升级 Loop Engineering：每天扫 CI，多个 Agent 用 worktree 并行，失败后写入记忆并由 verifier 验收"
    )
    assert blueprint["packet_type"] == "LoopEngineeringBlueprint"
    assert blueprint["activation"]["active"] is True
    assert len(blueprint["six_question_contract"]) == 6
    runtime = blueprint["runtime_blueprint"]
    for key in (
        "scheduler",
        "parallel_isolation",
        "skill_context",
        "external_connectors",
        "validation_gate",
        "persistent_memory",
    ):
        assert key in runtime
    assert runtime["parallel_isolation"]["isolation_mode"] == "git_worktree_per_agent"
    assert runtime["validation_gate"]["executor_validator_split"] is True


def test_kernel_exposes_loop_prompt_side_channel_for_video_loop():
    plan = DesignKernel().plan("generate a seamless loop video prompt; first and last frame must match").to_dict()
    pack = plan["loop_prompt_pack"]
    assert pack["packet_type"] == "LoopPromptPack"
    assert pack["activation"]["loop_type"] == "seamless_video_loop"
    assert "LoopPromptPack" in plan["tool_plan"]["tools"]
    assert "ShortDramaAIGC_OS" in plan["tool_plan"]["tools"]
    assert plan["prompt_packet_v2"]["packet_type"] == "PromptPacketV2"


def test_kernel_exposes_loop_engineering_side_channel():
    plan = DesignKernel().plan("Loop Engineering 调度 issue CI，worktree 并行隔离，validator 验收，写入长期记忆").to_dict()
    blueprint = plan["loop_engineering"]
    assert blueprint["packet_type"] == "LoopEngineeringBlueprint"
    assert blueprint["activation"]["active"] is True
    assert "LoopEngineeringBlueprint" in plan["tool_plan"]["tools"]
    assert plan["prompt_packet_v2"]["packet_type"] == "PromptPacketV2"


def test_aesthetic_quality_gate_detects_clutter_and_mojibake():
    report = AestheticQualityGate().evaluate("premium but cluttered messy tiny elements " + chr(0x9422))
    assert report.encoding_health < 100
    assert any("layout_order_missing" in risk for risk in report.risks)
    assert any("text_precision_missing" in risk for risk in report.risks)
    assert any("encoding_risk" in risk for risk in report.risks)


def test_skill_registry_sync_ok():
    assert '"ok": true' in SkillRegistrySyncAgent(".").report()
