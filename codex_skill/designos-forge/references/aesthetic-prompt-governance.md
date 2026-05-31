# Aesthetic And Prompt Governance

## v1.6 Quality Thesis

The design must be context-aware before it is spectacular. Prevent dirty, fragmented, overfilled visuals by locking project context, selecting relevant memory cases, forcing a clear focal anchor, controlled density, exact text, and explicit negative constraints before generation.

## Root Causes To Catch

- Fragmented visuals: too many small decorative pieces, random icons, scattered labels, background debris, and no dominant focal anchor.
- Dirty visuals: muddy texture noise, overmixed palettes, low-contrast type, uncontrolled grain, and fake aging effects.
- Weak prompts: generic words such as "高级", "大气", "好看", or "丰富" without concrete composition, material, light, typography, and output rules.
- Text failures: long in-image copy, pseudo-text, misspelling, warped letters, mixed language without hierarchy, and mojibake.
- Layout disorder: no grid, no margin system, no reading path, too many modules, no density ceiling, and overlapping text.
- Redundant mechanisms: multiple agents owning the same decision, repeated QA sections, repeated negative prompts, and unclear handoff owner.
- Context mixing: commercial conversion logic applied to academic competition boards, or research-board density applied to premium packaging/product visuals.

## Hard Gates

Before image generation or final delivery, require:

- One dominant visual anchor and no more than two secondary supports.
- One explicit project context and 1-3 relevant memory cases, or a statement that no suitable memory case exists.
- Explicit grid, margin, alignment, reading path, and negative space.
- Density ceiling: name what stays empty, quiet, or visually subordinate.
- Exact visible text: spelling, language, hierarchy, max lines, and no pseudo-text.
- UTF-8/no-mojibake check when Chinese or mixed-language text is present.
- Anti-fragmentation negative prompt: no scattered tiny decorations, no dirty texture noise, no random icons, no warped type, no fake logos, no unresolved placeholders.
- One owner each for context routing, case-memory selection, QA, and delivery; remove duplicated mechanisms.

## PromptPacket v1.6 Sections

Use all sections in order:

```text
01_TASK_BRIEF
02_DESIGN_INTENT
03_AUDIENCE_CONTEXT
04_PROJECT_CONTEXT_LOCK
05_CASE_MEMORY_SELECTION
06_REFERENCE_LOCK
07_AESTHETIC_THESIS
08_COMPOSITION_HIERARCHY
09_LAYOUT_GRID_DENSITY
10_STYLE_DNA_MATERIAL
11_COLOR_LIGHT_TYPOGRAPHY
12_TEXT_ACCURACY
13_MODEL_RENDER_RULES
14_ANTI_FRAGMENTATION_NEGATIVE_PROMPT
15_FAILURE_MEMORY
16_QA_GATES
17_DELIVERY_SPEC
18_REVISION_PROTOCOL
```

## Rewrite Pattern

Replace vague visual language with controlled structure:

- Weak: "高级大气，元素丰富，有冲击力。"
- Strong: "One oversized matte-black ceramic bottle as the only focal anchor, centered on a 12-column editorial grid; two small secondary proof marks; 60% quiet warm-gray negative space; exact title text only; no scattered decorations or noisy texture."

For typography prompts, require exact text first. For boards, require modules and hierarchy. For UI, require tokens, grid, states, and content-fit QA.
