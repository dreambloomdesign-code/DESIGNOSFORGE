# Photography Specialty Aesthetic Space

DESIGNOSFORGE now includes a `photography` domain for portrait retouching, product photography, composition optimization, and Hanfu cultural portrait workflows.

## Scope

- portrait scene retouching
- natural portrait refinement
- product photography generation and post-production
- product edge, label, reflection and material correction
- crop, perspective and composition optimization
- Hanfu and cultural portrait shooting

## Source Policy

Online tutorials are stored as source links, summaries and transfer lessons only. Do not scrape tutorial images, copy full article text, or treat official examples as training assets.

Raw images belong in ignored local folders:

```text
lora_training_sandbox/aesthetic_corpus/domains/photography/reference_images
lora_training_sandbox/aesthetic_corpus/domains/photography/case_images
lora_training_sandbox/aesthetic_corpus/domains/photography/rejected_images
lora_training_sandbox/aesthetic_corpus/domains/photography/comparison_sets
```

Repository-safe files:

```text
lora_training_sandbox/aesthetic_corpus/domains/photography/captions
lora_training_sandbox/aesthetic_corpus/domains/photography/manifests
lora_training_sandbox/aesthetic_corpus/domains/photography/quality_reviews
```

## Subdomain Rules

### Portrait Retouching

Keep skin texture, facial identity, hair detail and original light direction. Remove temporary blemishes and distractions locally. Avoid plastic skin, over-bright eyes, face reshaping by default, and edits that leak into hair, fabric or background.

### Product Photography

Prioritize clean background, product edge contour, material accuracy, label readability, consistent lighting and credible shadow/reflection. Do not hallucinate label text or warp product geometry.

### Composition Optimization

Use crop, straightening, perspective correction, leading lines and negative space to strengthen hierarchy. Do not stretch bodies or products, amputate hands/sleeves/product corners, or fill crop edges with scene-inconsistent content.

### Hanfu Cultural Portrait

Treat costume, hair, makeup, prop, scene, pose and light as one cultural styling system. Favor coherent architecture, garden, lakeside, window light, soft backlight, classical gestures and garment silhouette. Avoid random costume decoration or historically incoherent props unless deliberately contemporary.

## First Training Batch

`photography-foundation-web-sources-2026` is a metadata-only tutorial reference batch. It covers:

- Adobe composition, product photography, portrait photography and retouching references
- Shopify product photography setup references
- Nikon, Canon and Sony portrait capture references
- Chinese Hanfu shooting references
- portrait-retouching research references for texture and region consistency

Use it to route prompts and quality gates. It is not an image dataset.

