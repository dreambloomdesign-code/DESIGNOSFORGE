import json
from dataclasses import asdict, dataclass
from pathlib import Path
from uuid import uuid4

@dataclass(frozen=True)
class LoRALibrary:
    library_id: str
    name: str
    style_token: str
    sandbox: str

class LoRAStyleTrainingLibrary:
    def __init__(self, sandbox="lora_training_sandbox"):
        self.sandbox = Path(sandbox)
        self.libraries_dir = self.sandbox / "libraries"
        self.libraries_dir.mkdir(parents=True, exist_ok=True)
    def status(self):
        libraries = sorted(p.name for p in self.libraries_dir.glob("*") if p.is_dir())
        return json.dumps({"sandbox": str(self.sandbox), "library_count": len(libraries), "libraries": libraries}, ensure_ascii=False, indent=2)
    def init_library(self, name, style_token):
        library_id = f"lora_{uuid4().hex[:10]}"
        root = self.libraries_dir / library_id
        for child in ("dataset/assets", "jobs", "outputs", "logs", "manifests"):
            (root / child).mkdir(parents=True, exist_ok=True)
        library = LoRALibrary(library_id, name, style_token, str(root))
        (root / "library_manifest.json").write_text(json.dumps(asdict(library), ensure_ascii=False, indent=2), encoding="utf-8")
        return json.dumps(asdict(library), ensure_ascii=False, indent=2)
