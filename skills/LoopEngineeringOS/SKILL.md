# LoopEngineeringOS

System-runtime layer for durable agent loops.

Use when a workflow needs scheduler, event triggers, GitHub/CI/issue/PR integration, multi-agent worktree isolation, executor/verifier split, persistent memory, and complete project-following behavior.

Every loop must answer:

- who wakes the loop
- how parallel agents avoid collisions
- how the agent knows project habits
- what external systems it can touch
- who validates the result
- how it remembers yesterday

CLI:

```powershell
py -m app.cli kernel loop-engineering "Loop Engineering 调度 issue CI，worktree 并行隔离，validator 验收，写入长期记忆"
```
