# DesignOS Forge v1.4 Source Notes

## Source Package

```text
C:\Users\taojian\Downloads\DESIGNOSFORGE_v1.4_source_for_codex.zip
```

The source consolidates default DESIGNOSFORGE activation, three-step design inference, image-generation confirmation gating, PromptPacket generation, task routing, sixteen routed design skills, LoRA style-training sidecar planning, GitOps sidecar management, and a Codex skill entry.

## Quick Checks

After extracting the package and entering its root:

```powershell
$env:PYTHONPATH='.'
python -m app.cli capabilities
python -m app.cli run "做一个品牌 VI 方案" --prompt-packet
python -m app.cli gitops sync-registry
pytest -q
```

`python -m app.cli run "做一张海报并开始生图"` should state `正在调用 DESIGNOSFORGE` and block image generation until explicit confirmation. Use `--confirm-image-generation` only when the user has confirmed.

## CLI Surface

```powershell
python -m app.cli capabilities
python -m app.cli run "USER REQUEST" [--confirm-image-generation] [--prompt-packet]
python -m app.cli lora status
python -m app.cli lora init --name "Style Library" --style-token "<token>"
python -m app.cli gitops status --repo .
python -m app.cli gitops diff --repo .
python -m app.cli gitops sync-registry --repo .
```

## PromptPacket Sections

Use all sections in order:

```text
01_TASK_BRIEF
02_DESIGN_INTENT
03_REFERENCE_LOCK
04_STYLE_DNA
05_COMPOSITION
06_COLOR_TYPOGRAPHY
07_MATERIAL_LIGHTING
08_MODEL_RENDER_RULES
09_NEGATIVE_PROMPT
10_QA_CHECKLIST
11_OUTPUT_SPEC
```

## Registered v1.4 Skills

`ReferenceModeOS`, `PromptOrchestrationEngine`, `EnvArtBoardOS`, `brandVIos`, `InfoVisOS`, `PPTOS`, `WebDesignOS`, `UIDesignSpecOS`, `LayeredBoardComposer`, `AlgorithmicDesignEngine`, `DeliveryFeedbackLayer`, `TypographyDesignOS`, `PosterDesignOS`, `ShortDramaAIGC_OS`, `GeneralDesignOS`, and `LoRAStyleTrainingLibrary`.
