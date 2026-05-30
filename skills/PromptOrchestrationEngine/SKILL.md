---
name: PromptOrchestrationEngine
description: PromptPacket orchestration for model-specific design prompts, reference locks, QA gates, and negative constraints.
---

# PromptOrchestrationEngine

Use inside DESIGNOSFORGE when the task matches this capability.

Core rules:
- Explicitly preserve DESIGNOSFORGE activation.
- Keep the three-step inference process.
- Do not generate final images before user confirmation.
- Feed constraints into PromptOrchestrationEngine and QAAgent.
- Keep outputs executable, traceable, and delivery-ready.
