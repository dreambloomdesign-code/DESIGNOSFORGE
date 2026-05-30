import json
from pathlib import Path
from app.lora_training.aesthetic_space import LoRAAestheticSpace
from app.lora_training.service import LoRAStyleTrainingLibrary
from app.management.git_ops_manager import GitOpsManager
from app.management.github_manager import GitHubManager

def test_lora_library_init(tmp_path: Path):
    service = LoRAStyleTrainingLibrary(tmp_path / "lora_training_sandbox")
    payload = service.init_library("Ink Brand", "<ink_brand>")
    assert "Ink Brand" in payload
    assert "library_id" in payload

def test_lora_aesthetic_space_init(tmp_path: Path):
    root = tmp_path / "aesthetic_corpus"
    taxonomy = Path("config/lora_training/aesthetic_taxonomy.json")
    payload = json.loads(LoRAAestheticSpace(root, taxonomy).init_space())
    assert payload["domain_count"] >= 10
    assert "ui" in payload["domains"]
    assert "poster" in payload["domains"]
    assert "vi-brand" in payload["domains"]
    assert (root / "domains" / "ui" / "reference_images" / ".gitkeep").exists()
    manifest = json.loads((root / "domains" / "ui" / "domain_manifest.json").read_text(encoding="utf-8"))
    assert "minimal-premium" in manifest["allowed_style_axis_ids"]
    assert "fragmented_visual" in manifest["allowed_quality_labels"]

def test_gitops_status_runs_in_repo():
    assert isinstance(GitOpsManager(".").status(), str)

def test_github_status_handles_non_repo(tmp_path: Path):
    payload = json.loads(GitHubManager(tmp_path).status())
    assert payload["is_git_repo"] is False
    assert "Initialize git" in payload["recommended_next_action"]

def test_github_release_plan_mentions_version():
    plan = GitHubManager(".").release_plan("v9.9.9")
    assert "v9.9.9" in plan
    assert "draft PR" in plan

def test_github_default_release_plan_targets_v1_5_1():
    assert "v1.5.1" in GitHubManager(".").release_plan()
