# LoRA Aesthetic Space

Use this reference when DESIGNOSFORGE needs future LoRA training space for real case images and reference images.

## Command

From the source root:

```powershell
$env:PYTHONPATH='.'
$env:PYTHONUTF8='1'
py -3 -m app.cli lora init-aesthetic-space
py -3 -m app.cli lora audit-corpus
py -3 -m app.cli lora build-memory-index
py -3 -m app.cli lora recommend --domain exhibition-board --context academic-discipline-competition
```

## Dataset Root

```text
lora_training_sandbox/aesthetic_corpus
```

Images are ignored by git. Track only taxonomy, captions, manifests, quality reviews, and `.gitkeep` placeholders.
DESIGNOSFORGE v1.6 also tracks `aesthetic_memory_index.json`, which summarizes captions into case-memory batches for routing and PromptPacket v1.6 case selection.

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

## Aesthetic Memory Index

Run `lora build-memory-index` after adding or updating captions. The index is used to:

- audit missing `project_context_ids`
- summarize batch-level style DNA and risks
- recommend cases by domain, project context, and style axis
- prevent commercial, academic, public-culture, and Culture China samples from being mixed accidentally

Recommended queries:

```powershell
py -3 -m app.cli lora recommend --domain vi-brand --context commercial-project
py -3 -m app.cli lora recommend --domain exhibition-board --context academic-discipline-competition
py -3 -m app.cli lora recommend --domain infovis --context cultural-china-research
```

## Curation Rules

Separate `reference_images`, `case_images`, `rejected_images`, and `comparison_sets`.

Every image needs metadata: source type, domain, style axes, quality labels, positive notes, failure notes, text accuracy, layout notes, and rights status.

Do not train on unknown-rights images or private client assets unless rights are cleared.
