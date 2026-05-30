import json
from pathlib import Path
from app.lora_training.service import LoRAStyleTrainingLibrary
from app.management.git_ops_manager import GitOpsManager
from app.management.github_manager import GitHubManager

def test_lora_library_init(tmp_path: Path):
    service = LoRAStyleTrainingLibrary(tmp_path / "lora_training_sandbox")
    payload = service.init_library("Ink Brand", "<ink_brand>")
    assert "Ink Brand" in payload
    assert "library_id" in payload

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
