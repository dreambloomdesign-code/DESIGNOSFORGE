# LoRA Aesthetic Training Space

## Purpose

DESIGNOSFORGE reserves a LoRA aesthetic corpus space for future tuning from real case images and reference images.

This space is not meant to store model weights in git. It is meant to preserve the classification system, captions, manifests, quality reviews, and dataset structure that will guide later LoRA training.

## Dataset Root

```text
lora_training_sandbox/aesthetic_corpus
```

Initialize:

```bash
PYTHONPATH=. python -m app.cli lora init-aesthetic-space
PYTHONPATH=. python -m app.cli lora audit-corpus
PYTHONPATH=. python -m app.cli lora build-memory-index
```

Actual image files are ignored by git by default. Keep only `.gitkeep`, manifests, captions, taxonomy snapshots, quality reviews, and the generated `aesthetic_memory_index.json` in the repository.

## Design Domain Classes

Use these as the first-level classification for real case images and reference images:

- `ui`: app, dashboard, web product, mobile screen, components, design systems
- `poster`: key visual, campaign poster, event poster, typography poster, poster series
- `exhibition-board`: competition board, presentation board, analysis board, multi-panel board
- `vi-brand`: logo, VI, brand identity, brand board, brand applications
- `environmental-art`: interior, landscape, exhibition, spatial design, environmental analysis, CAD/DWG/DXF source-fidelity workflows
- `packaging`: box, label, bottle, bag, commerce touchpoint, product package
- `typography`: expressive type, lettering, title systems, typographic rhythm
- `infovis`: diagram, map, flowchart, timeline, data narrative
- `web`: landing page, editorial web, product site, docs, responsive web
- `short-video-aigc`: storyboard, shot board, scene style, character continuity
- `photography`: portrait photography, portrait retouching, product photography, composition optimization, Hanfu portrait shooting, and photo post-production references

## Style Axis Classes

Use these as multi-label aesthetic axes:

- `minimal-premium`: quiet surface, restrained palette, clear focal anchor, high whitespace
- `editorial-grid`: strong grid, reading path, modular hierarchy, print-like order
- `swiss-modern`: geometric alignment, sans typography, strict spacing, neutral contrast
- `commercial-product`: inspectable product, clean lighting, controlled reflections
- `soft-luxury`: soft light, warm neutrals, delicate material, low-noise atmosphere
- `tech-futurism`: precise geometry, luminous accents, no random sci-fi clutter
- `cultural-contemporary`: cultural symbol translation without ornament overload
- `environmental-competition`: plan fidelity, spatial hierarchy, board-level readability
- `cad-topology-fidelity`: locked units, scale, north, axes, wall topology, openings, columns, dimensions, title block, and semantic layers before styling
- `construction-drawing-logic`: editable text, semantic lineweights, hosted door/window openings, construction dimensions, elevations, material notes, and detail indexes
- `experimental-typography`: expressive letterform, exact text, controlled distortion
- `infographic-technical`: label accuracy, diagram clarity, thin-line discipline
- `natural-portrait-retouch`: preserved skin texture, believable facial anatomy, natural color, and local non-destructive retouching
- `studio-product-lighting`: clean product edge contour, controlled reflections, accurate material, and inspectable studio lighting
- `composition-optimization`: balanced crop, perspective correction, subject breathing room, leading lines, and clear focal hierarchy
- `hanfu-cultural-portrait`: coherent costume, hair, makeup, prop, architecture or landscape scene, and respectful cultural styling

## Project Context Classes

Use project context as a second layer after domain and style axis. This prevents commercial cases and university competition cases from being mixed into one aesthetic prompt.

- `commercial-project`: market-facing brand, packaging, product, service, or client-delivery work
- `academic-discipline-competition`: university discipline competition boards with research framing, methodology, evidence chains, and proposal logic
- `cultural-china-research`: Culture China, regional culture, cultural tourism, heritage communication, illustrated infovis, and interaction research works
- `public-cultural-communication`: museum, tourism, education, city communication, and civic cultural design
- `portrait-session`: personal, editorial, fashion, Hanfu, and cultural portrait sessions with natural anatomy, stable pose, coherent scene, and subject dignity
- `product-photo-production`: product photography generation, post-production, e-commerce hero shots, still life, and material/lighting correction references
- `spatial-cad-production`: environmental art, architecture, interior, exhibition, landscape, CAD/DWG/DXF, semantic-layer, construction drawing, and source-fidelity workflows

## Photography Specialty Module

The `photography` domain is a v1.7-ready specialty space for:

- portrait scene retouching and background cleanup
- natural portrait retouching, skin texture preservation, face/hair/clothing refinement
- product photography generation, product cutout, reflection/highlight control, white-background and hero-scene polish
- composition optimization, crop, straightening, perspective correction, and focal hierarchy
- Hanfu and cultural portrait shooting, including costume/scene/makeup/prop coherence

Photography tutorial pages, shooting plans, and retouching recipes may be stored as `tutorial_reference`, `shooting_recipe`, or `retouching_recipe` caption rows. These rows teach workflow logic and quality gates only. They are not raw image training samples.

Do not store scraped tutorial images or full article text in the public repository. Keep links, summaries, source date, rights notes, and transferable design/photography lessons.

## EnvArt CADMCP Specialty Module

The `environmental-art` domain now includes a CAD-aware project context: `spatial-cad-production`.

Use it for:

- CAD/DWG/DXF source inspection and audit
- AutoCAD Core Console conversion or batch scripts
- Tianzheng-aware architecture component workflows
- semantic layer classification
- construction drawing QA
- plan, section, elevation, and model screenshot fidelity locks
- image2 prompts and competition boards that must preserve source geometry

CAD workflow rows may be stored as `cad_reference`, `cad_workflow_recipe`, or `drawing_qa_recipe` caption rows. These rows teach source-fidelity, geometry-lock, semantic-layer, and QA logic. They are not raw CAD training samples.

For CAD or plan-based references:

- preserve units, scale, north arrow, site boundary, axes, walls, columns, openings, dimensions, title block, and semantic layers
- keep ordinary annotations as editable text, not vector glyph outlines
- keep wall lines split at openings; do not cover unbroken walls with door/window symbols
- add analysis overlays above locked base geometry instead of redrawing the base
- never invent roads, POI, room names, dimensions, north arrows, or site facts

When a case is `academic-discipline-competition`, prefer captions that describe research structure, section hierarchy, evidence display, information visualization, and application proof. Do not let it inherit commercial conversion language unless the case is explicitly commercial.

## Aesthetic Memory Index

DESIGNOSFORGE v1.6 uses `aesthetic_memory_index.json` as the bridge between curated training cases and runtime prompt decisions.

The index supports:

- corpus audits for missing `project_context_ids` and missing quality reviews
- batch-level summaries of domains, style axes, contexts, rights status, positive notes, and failure notes
- recommendation queries such as `--domain exhibition-board --context academic-discipline-competition`
- explicit separation between commercial work, university competition work, Culture China research, and public cultural communication

## Directory Contract

Each domain contains:

```text
reference_images/   external references, inspiration, visual direction images
case_images/        successful real cases or approved generated cases
rejected_images/    failed cases for negative learning and QA contrast
comparison_sets/    before/after or reference/result pairs
captions/           caption files and prompt annotations
manifests/          dataset manifests, provenance, and rights status
quality_reviews/    aesthetic QA notes and scoring
domain_manifest.json
```

## Caption And Rights Rules

Every image should have metadata before it is used for training:

- source type: reference, case, rejected, or comparison
- design domain
- style axis labels
- quality labels
- positive aesthetic notes
- negative failure notes
- text accuracy notes
- layout notes
- rights status

Do not train on images marked `unknown_do_not_train`.

For photography references:

- preserve human anatomy and skin texture; avoid plastic skin and face warping
- preserve light direction and shadow logic across subject, background, and product
- separate local retouching from global color grading
- keep product edges, labels, material texture, and reflections credible
- for Hanfu, check costume, hair, makeup, prop, posture, architecture/landscape scene, and cultural atmosphere as one system

## Quality Labels

Positive labels:

- `clean_composition`
- `strong_focal_anchor`
- `good_negative_space`
- `layout_ordered`
- `text_accurate`
- `material_credible`
- `color_controlled`
- `reference_fidelity`
- `cad_source_fidelity`
- `semantic_layers`
- `wall_topology_locked`
- `opening_accuracy`
- `dimension_editable`
- `title_block_preserved`
- `construction_annotation_complete`

Failure labels:

- `fragmented_visual`
- `dirty_texture_noise`
- `layout_disorder`
- `text_error`
- `mojibake`
- `generic_style`
- `overdecorated`
- `cad_topology_drift`
- `wall_crosses_opening`
- `source_layer_zero_copied`
- `fake_site_geometry`

## Training Strategy

Start with curation before training:

1. Add 20-50 high-quality examples per design domain.
2. Add rejected examples for common failures such as fragmented visuals, dirty texture, and garbled text.
3. Write captions that describe visible design structure, not vague praise.
4. Compare domain-specific style axes before mixing domains.
5. Train small adapters by domain first, then evaluate cross-domain transfer.
6. Keep adapter manifests out of public release unless weights and rights are cleared.
