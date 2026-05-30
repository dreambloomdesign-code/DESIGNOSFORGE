from app.core.aesthetic_quality import AestheticQualityGate
from app.core.capabilities import capability_report
from app.core.orchestrator import MasterOrchestrator
from app.core.prompt_packet import PROMPT_PACKET_SECTIONS, PromptPacketBuilder
from app.core.skill_registry import SkillRegistry
from app.core.task_router import TaskRouterAgent
from app.management.skill_registry_sync import SkillRegistrySyncAgent

def test_capabilities_include_core_agents():
    report = capability_report()
    assert "DESIGNOSFORGE v1.5.0" in report
    assert "AestheticQualityGate" in report
    assert "GitOpsManager" in report
    assert "GitHubManager" in report
    assert "LoRAStyleTrainingLibrary" in report

def test_skill_registry_has_expected_skills():
    registry = SkillRegistry()
    assert len(registry.list()) == 16
    assert registry.has("brandVIos")

def test_task_router_routes_design_domains():
    router = TaskRouterAgent()
    assert router.route("做一个品牌 VI").skill_name == "brandVIos"
    assert router.route("生成字体海报").skill_name == "TypographyDesignOS"

def test_image_generation_gate_blocks_without_confirmation():
    output = MasterOrchestrator().run("做一张海报并开始生图")
    assert "正在调用 DESIGNOSFORGE" in output
    assert "已拦截" in output

def test_prompt_packet_contains_required_sections():
    packet = PromptPacketBuilder().build("test", "logo")
    for section in PROMPT_PACKET_SECTIONS:
        assert section in packet
    assert "PromptPacket v1.5" in packet
    assert "ANTI_FRAGMENTATION" in packet
    assert "TEXT_ACCURACY" in packet

def test_aesthetic_quality_gate_detects_clutter_and_mojibake():
    report = AestheticQualityGate().evaluate("高级 大气 细碎 脏乱 " + chr(0x9422) + " 生成一张信息很多的海报")
    assert report.encoding_health < 100
    assert any("visual_clutter" in risk for risk in report.risks)
    assert any("encoding_risk" in risk for risk in report.risks)

def test_skill_registry_sync_ok():
    assert '"ok": true' in SkillRegistrySyncAgent(".").report()
