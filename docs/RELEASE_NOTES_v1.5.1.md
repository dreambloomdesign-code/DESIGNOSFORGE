# DESIGNOSFORGE v1.5.1 Release Notes

## Highlights

DESIGNOSFORGE v1.5.1 reserves the LoRA aesthetic training space needed for future case-image and reference-image learning.

- Adds a design-domain taxonomy for UI, poster, exhibition board, VI/brand, environmental art, packaging, typography, infovis, web, and short-video AIGC.
- Adds style axes such as minimal premium, editorial grid, Swiss modern, commercial product, soft luxury, tech futurism, cultural contemporary, environmental competition, experimental typography, and technical infovis.
- Adds `python -m app.cli lora init-aesthetic-space` to generate corpus folders, domain manifests, and taxonomy snapshots.
- Keeps real images out of git by default while tracking manifests, captions, quality reviews, and `.gitkeep` placeholders.
- Adds documentation for rights status, rejected examples, comparison sets, and quality labels.

## Why It Matters

Future LoRA tuning should not mix every image into one unstructured dataset. DESIGNOSFORGE now separates design domains and style axes so aesthetic preferences can be optimized intentionally.

The reserved corpus supports:

- real successful case images
- reference images
- rejected images for failure contrast
- before/after comparison sets
- captions and prompt annotations
- quality reviews for visual cleanliness, text accuracy, layout order, and reference fidelity

## Validation

- `python -m app.cli lora init-aesthetic-space`
- `python tools/validate_source_skill.py`
- `pytest -q`
- text health audit with `mojibake_count: 0`
