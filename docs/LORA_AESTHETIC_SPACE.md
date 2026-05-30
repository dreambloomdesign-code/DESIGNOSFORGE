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
```

Actual image files are ignored by git by default. Keep only `.gitkeep`, manifests, captions, taxonomy snapshots, and quality reviews in the repository.

## Design Domain Classes

Use these as the first-level classification for real case images and reference images:

- `ui`: app, dashboard, web product, mobile screen, components, design systems
- `poster`: key visual, campaign poster, event poster, typography poster, poster series
- `exhibition-board`: competition board, presentation board, analysis board, multi-panel board
- `vi-brand`: logo, VI, brand identity, brand board, brand applications
- `environmental-art`: interior, landscape, exhibition, spatial design, environmental analysis
- `packaging`: box, label, bottle, bag, commerce touchpoint, product package
- `typography`: expressive type, lettering, title systems, typographic rhythm
- `infovis`: diagram, map, flowchart, timeline, data narrative
- `web`: landing page, editorial web, product site, docs, responsive web
- `short-video-aigc`: storyboard, shot board, scene style, character continuity

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
- `experimental-typography`: expressive letterform, exact text, controlled distortion
- `infographic-technical`: label accuracy, diagram clarity, thin-line discipline

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

Failure labels:

- `fragmented_visual`
- `dirty_texture_noise`
- `layout_disorder`
- `text_error`
- `mojibake`
- `generic_style`
- `overdecorated`

## Training Strategy

Start with curation before training:

1. Add 20-50 high-quality examples per design domain.
2. Add rejected examples for common failures such as fragmented visuals, dirty texture, and garbled text.
3. Write captions that describe visible design structure, not vague praise.
4. Compare domain-specific style axes before mixing domains.
5. Train small adapters by domain first, then evaluate cross-domain transfer.
6. Keep adapter manifests out of public release unless weights and rights are cleared.
