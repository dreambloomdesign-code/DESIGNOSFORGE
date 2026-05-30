# Aesthetic And Prompt Governance

## v1.5 Quality Thesis

The design must be inspectable before it is spectacular. Prevent dirty, fragmented, overfilled visuals by forcing a clear focal anchor, controlled density, exact text, and explicit negative constraints before generation.

## Root Causes To Catch

- Fragmented visuals: too many small decorative pieces, random icons, scattered labels, background debris, and no dominant focal anchor.
- Dirty visuals: muddy texture noise, overmixed palettes, low-contrast type, uncontrolled grain, and fake aging effects.
- Weak prompts: generic words such as "高级", "大气", "好看", or "丰富" without concrete composition, material, light, typography, and output rules.
- Text failures: long in-image copy, pseudo-text, misspelling, warped letters, mixed language without hierarchy, and mojibake.
- Layout disorder: no grid, no margin system, no reading path, too many modules, no density ceiling, and overlapping text.
- Redundant mechanisms: multiple agents owning the same decision, repeated QA sections, repeated negative prompts, and unclear handoff owner.

## Hard Gates

Before image generation or final delivery, require:

- One dominant visual anchor and no more than two secondary supports.
- Explicit grid, margin, alignment, reading path, and negative space.
- Density ceiling: name what stays empty, quiet, or visually subordinate.
- Exact visible text: spelling, language, hierarchy, max lines, and no pseudo-text.
- UTF-8/no-mojibake check when Chinese or mixed-language text is present.
- Anti-fragmentation negative prompt: no scattered tiny decorations, no dirty texture noise, no random icons, no warped type, no fake logos, no unresolved placeholders.
- One owner each for routing, QA, and delivery; remove duplicated mechanisms.

## PromptPacket v1.5 Sections

Use all sections in order:

```text
01_TASK_BRIEF
02_DESIGN_INTENT
03_AUDIENCE_CONTEXT
04_REFERENCE_LOCK
05_AESTHETIC_THESIS
06_COMPOSITION_HIERARCHY
07_LAYOUT_GRID_DENSITY
08_STYLE_DNA_MATERIAL
09_COLOR_LIGHT_TYPOGRAPHY
10_TEXT_ACCURACY
11_MODEL_RENDER_RULES
12_ANTI_FRAGMENTATION_NEGATIVE_PROMPT
13_QA_GATES
14_DELIVERY_SPEC
15_REVISION_PROTOCOL
```

## Rewrite Pattern

Replace vague visual language with controlled structure:

- Weak: "高级大气，元素丰富，有冲击力。"
- Strong: "One oversized matte-black ceramic bottle as the only focal anchor, centered on a 12-column editorial grid; two small secondary proof marks; 60% quiet warm-gray negative space; exact title text only; no scattered decorations or noisy texture."

For typography prompts, require exact text first. For boards, require modules and hierarchy. For UI, require tokens, grid, states, and content-fit QA.
