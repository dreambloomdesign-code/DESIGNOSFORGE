# DESIGNOSFORGE v1.6 System Evaluation

## Starting Point

DESIGNOSFORGE v1.5.1 had strong prompt governance, aesthetic quality gates, text health checks, and a reserved LoRA corpus. After several curated case batches, the corpus began to contain useful design judgment, but runtime inference did not yet use that judgment formally.

## Main Gap

The system could store training cases, but it did not yet ask:

- Which project context is this?
- Which memory cases should influence the prompt?
- Which cases must be excluded?
- Are commercial, academic, and public-culture references being mixed by accident?
- Which rejected attempts should become failure-memory rather than positive training data?

## v1.6 System Solution

- Add `AestheticMemoryIndex` to audit and summarize the corpus.
- Add `project_context_ids` across current captions and manifests.
- Add batch-level case recommendation by domain, context, and style axis.
- Upgrade PromptPacket to v1.6 with context lock, case-memory selection, and failure-memory.
- Keep image rights conservative: public reference metadata is tracked, original images remain ignored by git.

## Current Corpus Status

- Caption items: 38
- Batches: 5
- Missing project contexts: 0
- Rights status: all current records are `public_reference_only`
- Main domains: `vi-brand`, `exhibition-board`
- Active contexts: `commercial-project`, `academic-discipline-competition`, `cultural-china-research`, `public-cultural-communication`

## Next Risks

- UI, typography, poster, web, and short-video domains still need more curated batches.
- Public reference images are not training-ready until rights are cleared.
- Memory recommendation is metadata-based; future work can add vector similarity after the corpus grows.
