# Loop Engineering Reference

Loop Engineering is the system-runtime layer for durable agent workflows. It is separate from LoopPromptPack.

Use LoopEngineeringOS when the user asks for:

- Loop Engineering
- long-running agent loops
- scheduler, cron, daily checks, event triggers
- GitHub issue, PR, CI, test failure, or release-monitor loops
- multiple agents, parallel work, worktree isolation
- validator, verifier, review, acceptance gate
- persistent memory, loop state, project-following workflows

## Six Questions

Every LoopEngineeringBlueprint must answer:

1. Who wakes the loop?
   - manual, scheduled, event, validation failure, or goal-until-done trigger.
2. How do parallel agents avoid collisions?
   - worktree/sandbox per executor, path ownership, merge gate, conflict check.
3. How does the agent know project habits?
   - required skills, project rules, no-touch paths, naming conventions, known traps.
4. What external systems can it touch?
   - local files, Git, GitHub, issues, PRs, CI, browser QA, CAD MCP, image tools, database, notifications.
5. Who validates the result?
   - executor/verifier split, deterministic tests first, critic/reviewer checks, human review threshold.
6. How does it remember yesterday?
   - state file, PR body, issue, failure memory, delivery manifest, next wake condition.

## Runtime Requirements

- Scheduler is explicit.
- Parallel editing uses worktree isolation when paths may overlap.
- Skills and project context are loaded before execution.
- External side effects are logged.
- The executor does not serve as the only validator.
- Stop conditions and human handoff rules are explicit.
- Persistent memory is written after each iteration.

## CLI

```powershell
py -m app.cli kernel loop-engineering "Loop Engineering 调度 issue CI，worktree 并行隔离，validator 验收，写入长期记忆"
```

## Output Contract

```text
packet_type = LoopEngineeringBlueprint
runtime_blueprint.scheduler
runtime_blueprint.parallel_isolation
runtime_blueprint.skill_context
runtime_blueprint.external_connectors
runtime_blueprint.validation_gate
runtime_blueprint.persistent_memory
agent_topology
state_schema
handoff_contract
failure_controls
prompt_scaffold
```
