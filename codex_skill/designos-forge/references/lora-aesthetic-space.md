# LoRA Aesthetic Space

Use this reference when DESIGNOSFORGE needs future LoRA training space for real case images and reference images.

## Command

From the source root:

```powershell
$env:PYTHONPATH='.'
$env:PYTHONUTF8='1'
py -3 -m app.cli lora init-aesthetic-space
```

## Dataset Root

```text
lora_training_sandbox/aesthetic_corpus
```

Images are ignored by git. Track only taxonomy, captions, manifests, quality reviews, and `.gitkeep` placeholders.

## Domain Classes

- `ui`: app, dashboard, mobile screen, component, design system
- `poster`: poster, key visual, typography poster, campaign visual
- `exhibition-board`: competition board, presentation board, analysis board
- `vi-brand`: logo, VI, brand identity, brand board
- `environmental-art`: interior, landscape, exhibition, spatial board
- `packaging`: product packaging, label, bottle, box, bag
- `typography`: lettering, type hierarchy, expressive title system
- `infovis`: diagram, map, flowchart, data narrative
- `web`: landing page, product site, editorial web, docs
- `short-video-aigc`: storyboard, shot board, scene/character continuity

## Style Axes

- `minimal-premium`
- `editorial-grid`
- `swiss-modern`
- `commercial-product`
- `soft-luxury`
- `tech-futurism`
- `cultural-contemporary`
- `environmental-competition`
- `experimental-typography`
- `infographic-technical`

## Project Contexts

Use project context tags to separate business deliverables from competition and research works:

- `commercial-project`: market-facing brand, packaging, product, service, or client-delivery work
- `academic-discipline-competition`: university discipline competition work with research framing, methodology, evidence chains, and board logic
- `cultural-china-research`: Culture China, Chinese cultural tourism, heritage communication, illustrated infovis, and interaction research
- `public-cultural-communication`: museum, tourism, education, city communication, and civic cultural design

For `academic-discipline-competition`, describe research logic, information hierarchy, visual analysis, and application validation. Avoid treating dense boards as commercial ads.

## Curation Rules

Separate `reference_images`, `case_images`, `rejected_images`, and `comparison_sets`.

Every image needs metadata: source type, domain, style axes, quality labels, positive notes, failure notes, text accuracy, layout notes, and rights status.

Do not train on unknown-rights images or private client assets unless rights are cleared.
