import json

from app.core.aesthetic_quality import AestheticQualityGate
from app.core.capabilities import capability_report
from app.core.design_kernel import DesignKernel
from app.core.loop_prompt import LoopPromptPackBuilder
from app.core.prompt_packet import PROMPT_PACKET_SECTIONS, PromptPacketBuilder
from app.core.skill_registry import SkillRegistry
from app.core.task_router import TaskRouterAgent
from app.management.skill_registry_sync import SkillRegistrySyncAgent


def test_capabilities_include_core_agents():
    report = capability_report()
    assert "DESIGNOSFORGE v2.0.0" in report
    assert "PromptPacketV2Builder" in report
    assert "LoopPromptEngine" in report
    assert "AestheticMemoryIndex" in report
    assert "GitOpsManager" in report
    assert "GitHubManager" in report


def test_skill_registry_has_expected_skills():
    registry = SkillRegistry()
    assert registry.has("brandVIos")
    assert registry.has("LoopPromptEngine")
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


def test_kernel_exposes_loop_prompt_side_channel_for_video_loop():
    plan = DesignKernel().plan("generate a seamless loop video prompt; first and last frame must match").to_dict()
    pack = plan["loop_prompt_pack"]
    assert pack["packet_type"] == "LoopPromptPack"
    assert pack["activation"]["loop_type"] == "seamless_video_loop"
    assert "LoopPromptPack" in plan["tool_plan"]["tools"]
    assert "ShortDramaAIGC_OS" in plan["tool_plan"]["tools"]
    assert plan["prompt_packet_v2"]["packet_type"] == "PromptPacketV2"


def test_aesthetic_quality_gate_detects_clutter_and_mojibake():
    report = AestheticQualityGate().evaluate("premium but cluttered messy tiny elements " + chr(0x9422))
    assert report.encoding_health < 100
    assert any("visual_clutter" in risk for risk in report.risks)
    assert any("encoding_risk" in risk for risk in report.risks)


def test_skill_registry_sync_ok():
    assert '"ok": true' in SkillRegistrySyncAgent(".").report()
