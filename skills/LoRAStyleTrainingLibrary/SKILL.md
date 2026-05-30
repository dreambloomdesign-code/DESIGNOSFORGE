---
name: LoRAStyleTrainingLibrary
description: Isolated LoRA style training library for DESIGNOSFORGE, including dataset ingestion, captions, style tokens, train configs, and adapter manifests.
---

# LoRAStyleTrainingLibrary

Use inside DESIGNOSFORGE when the task matches this capability.

Core rules:
- Explicitly preserve DESIGNOSFORGE activation.
- Keep the three-step inference process.
- Do not generate final images before user confirmation.
- Feed constraints into PromptOrchestrationEngine and QAAgent.
- Keep outputs executable, traceable, and delivery-ready.
