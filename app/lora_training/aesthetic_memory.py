import json
from collections import Counter, defaultdict
from pathlib import Path


class AestheticMemoryIndex:
    def __init__(self, root="lora_training_sandbox/aesthetic_corpus"):
        self.root = Path(root)

    def caption_items(self):
        for path in sorted((self.root / "domains").glob("*/captions/*.jsonl")):
            if path.name == ".gitkeep":
                continue
            for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                if not line.strip():
                    continue
                item = json.loads(line)
                item["_caption_file"] = path.as_posix()
                item["_line"] = line_no
                yield item

    def audit(self):
        items = list(self.caption_items())
        domains = Counter()
        contexts = Counter()
        style_axes = Counter()
        rights = Counter()
        batches = defaultdict(int)
        missing_project_context = []
        missing_quality_review_batches = []

        for item in items:
            domains[item.get("domain_id", "")] += 1
            contexts.update(item.get("project_context_ids", []))
            style_axes.update(item.get("style_axis_ids", []))
            rights[item.get("rights_status", "")] += 1
            batches[item.get("batch_id", "")] += 1
            if not item.get("project_context_ids"):
                missing_project_context.append({
                    "batch_id": item.get("batch_id"),
                    "image_id": item.get("image_id"),
                    "caption_file": item.get("_caption_file"),
                    "line": item.get("_line"),
                })

        for batch_id in batches:
            if not list((self.root / "domains").glob(f"*/quality_reviews/{batch_id}.quality_review.json")):
                missing_quality_review_batches.append(batch_id)

        return {
            "schema_version": "1.6.0",
            "caption_item_count": len(items),
            "batch_count": len(batches),
            "domain_distribution": dict(sorted(domains.items())),
            "project_context_distribution": dict(sorted(contexts.items())),
            "style_axis_distribution": dict(sorted(style_axes.items())),
            "rights_distribution": dict(sorted(rights.items())),
            "project_context_coverage": {
                "with_context": len(items) - len(missing_project_context),
                "missing_context": len(missing_project_context),
            },
            "missing_project_context": missing_project_context,
            "missing_quality_review_batches": sorted(set(missing_quality_review_batches)),
        }

    def build_index(self):
        items = list(self.caption_items())
        batches = {}
        for item in items:
            batch_id = item.get("batch_id", "")
            batch = batches.setdefault(batch_id, {
                "batch_id": batch_id,
                "primary_domain_ids": set(),
                "secondary_domain_ids": set(),
                "style_axis_ids": set(),
                "project_context_ids": set(),
                "visual_genre_tags": set(),
                "rights_statuses": set(),
                "image_count": 0,
                "sample_caption": "",
                "sample_positive_notes": [],
                "sample_negative_notes": [],
            })
            batch["image_count"] += 1
            batch["primary_domain_ids"].add(item.get("domain_id", ""))
            batch["secondary_domain_ids"].update(item.get("secondary_domain_ids", []))
            batch["style_axis_ids"].update(item.get("style_axis_ids", []))
            batch["project_context_ids"].update(item.get("project_context_ids", []))
            batch["visual_genre_tags"].update(item.get("visual_genre_tags", []))
            batch["rights_statuses"].add(item.get("rights_status", ""))
            if not batch["sample_caption"]:
                batch["sample_caption"] = item.get("caption", "")
                batch["sample_positive_notes"] = item.get("positive_aesthetic_notes", [])[:3]
                batch["sample_negative_notes"] = item.get("negative_failure_notes", [])[:3]

        normalized = []
        for batch in batches.values():
            normalized.append({
                key: sorted(value) if isinstance(value, set) else value
                for key, value in batch.items()
            })

        payload = {
            "schema_version": "1.6.0",
            "purpose": "Aesthetic memory index for training-aware DESIGNOSFORGE routing and PromptPacket v1.6 case selection.",
            "root": self.root.as_posix(),
            "audit": self.audit(),
            "batches": sorted(normalized, key=lambda item: item["batch_id"]),
        }
        output = self.root / "aesthetic_memory_index.json"
        output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return payload

    def recommend(self, domain="", context="", style_axis="", limit=5):
        domain = domain.strip()
        context = context.strip()
        style_axis = style_axis.strip()
        index_path = self.root / "aesthetic_memory_index.json"
        if index_path.exists():
            batches = json.loads(index_path.read_text(encoding="utf-8")).get("batches", [])
        else:
            batches = self.build_index().get("batches", [])

        ranked = []
        for batch in batches:
            score = 0
            reasons = []
            if domain and (domain in batch.get("primary_domain_ids", []) or domain in batch.get("secondary_domain_ids", [])):
                score += 4
                reasons.append(f"domain:{domain}")
            if context and context in batch.get("project_context_ids", []):
                score += 5
                reasons.append(f"context:{context}")
            if style_axis and style_axis in batch.get("style_axis_ids", []):
                score += 3
                reasons.append(f"style_axis:{style_axis}")
            if not (domain or context or style_axis):
                score = batch.get("image_count", 0)
                reasons.append("general_memory")
            if score > 0:
                ranked.append({
                    "batch_id": batch.get("batch_id"),
                    "score": score,
                    "match_reasons": reasons,
                    "primary_domain_ids": batch.get("primary_domain_ids", []),
                    "secondary_domain_ids": batch.get("secondary_domain_ids", []),
                    "project_context_ids": batch.get("project_context_ids", []),
                    "style_axis_ids": batch.get("style_axis_ids", []),
                    "sample_caption": batch.get("sample_caption", ""),
                    "sample_positive_notes": batch.get("sample_positive_notes", []),
                    "sample_negative_notes": batch.get("sample_negative_notes", []),
                })

        ranked.sort(key=lambda item: (-item["score"], item["batch_id"]))
        return {
            "schema_version": "1.6.0",
            "query": {
                "domain": domain,
                "context": context,
                "style_axis": style_axis,
                "limit": limit,
            },
            "results": ranked[:limit],
        }
