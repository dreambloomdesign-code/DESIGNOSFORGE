import json
from pathlib import Path
from app.core.skill_registry import SkillRegistry

class SkillRegistrySyncAgent:
    def __init__(self, root="."):
        self.root = Path(root)
        self.registry = SkillRegistry()
    def report(self):
        missing_skill_docs = [skill.name for skill in self.registry.list() if not (self.root / "skills" / skill.name / "SKILL.md").exists()]
        return json.dumps({"registered_skill_count": len(self.registry.list()), "missing_skill_docs": missing_skill_docs, "ok": not missing_skill_docs}, ensure_ascii=False, indent=2)
