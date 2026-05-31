import json
from pathlib import Path


DEFAULT_TAXONOMY_PATH = Path("config/lora_training/aesthetic_taxonomy.json")


class LoRAAestheticSpace:
    def __init__(self, root="lora_training_sandbox/aesthetic_corpus", taxonomy_path=DEFAULT_TAXONOMY_PATH):
        self.root = Path(root)
        self.taxonomy_path = Path(taxonomy_path)

    def load_taxonomy(self):
        return json.loads(self.taxonomy_path.read_text(encoding="utf-8"))

    def init_space(self):
        taxonomy = self.load_taxonomy()
        self.root.mkdir(parents=True, exist_ok=True)

        summary = {
            "root": str(self.root),
            "taxonomy_version": taxonomy["version"],
            "domain_count": len(taxonomy["design_domains"]),
            "style_axis_count": len(taxonomy["style_axes"]),
            "project_context_count": len(taxonomy.get("project_contexts", [])),
            "domains": [],
        }

        (self.root / "taxonomy_snapshot.json").write_text(
            json.dumps(taxonomy, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        for domain in taxonomy["design_domains"]:
            domain_root = self.root / "domains" / domain["id"]
            for group in taxonomy["image_groups"] + taxonomy["metadata_groups"]:
                folder = domain_root / group
                folder.mkdir(parents=True, exist_ok=True)
                (folder / ".gitkeep").touch()

            manifest = {
                "domain": domain,
                "allowed_style_axis_ids": [item["id"] for item in taxonomy["style_axes"]],
                "project_contexts": taxonomy.get("project_contexts", []),
                "allowed_quality_labels": taxonomy["quality_labels"],
                "caption_schema": taxonomy["caption_schema"],
                "notes": "Store images outside git by default; track captions, manifests, and quality reviews.",
            }
            (domain_root / "domain_manifest.json").write_text(
                json.dumps(manifest, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            summary["domains"].append(domain["id"])

        (self.root / "SPACE_MANIFEST.json").write_text(
            json.dumps(summary, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        return json.dumps(summary, ensure_ascii=False, indent=2)
