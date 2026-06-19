# Loop Engineering

Loop Engineering upgrades a loop from repeated prompting into a running system. In DESIGNOSFORGE v2.1.0, `LoopPromptPack` remains the prompt-iteration layer, while `LoopEngineeringBlueprint` defines the runtime around it.

## The Six Questions

Every serious loop must answer six questions before it runs:

1. Who wakes the loop?
   - manual trigger
   - scheduled trigger
   - event trigger
   - validation-failure trigger
   - goal-until-done trigger

2. How do parallel agents avoid collisions?
   - use one worktree or sandbox per executor when edits can overlap
   - declare file ownership before editing
   - merge through review rather than direct overwrite
   - run conflict gates before accepting output

3. How does the agent know project habits?
   - load the right skills
   - read project rules and no-touch paths
   - keep naming conventions and known pitfalls outside the chat
   - treat skills as long-term memory, not one-off prompt text

4. What external systems can it touch?
   - local files
   - Git and GitHub
   - issues, PRs, CI, tests
   - browser QA, CAD MCP, image tools, or databases when relevant
   - all side effects must be logged

5. Who validates the result?
   - split executor and verifier roles
   - run deterministic checks first
   - use critic or reviewer agents for subjective quality
   - ask for human review when correctness cannot be proven

6. How does it remember yesterday?
   - write a loop state file
   - record decisions, failures, confirmed facts, and next wake conditions
   - update failure memory for rejected directions
   - keep durable state in the repository or issue system

Principle: the model may forget, but the repository must not.

## Runtime Blueprint

`LoopEngineeringBlueprint` always contains:

```json
{
  "schema_version": "2.1.0-loop-engineering.1",
  "packet_type": "LoopEngineeringBlueprint",
  "relationship_to_loop_prompt_pack": {},
  "activation": {},
  "six_question_contract": [],
  "runtime_blueprint": {
    "scheduler": {},
    "parallel_isolation": {},
    "skill_context": {},
    "external_connectors": {},
    "validation_gate": {},
    "persistent_memory": {}
  },
  "agent_topology": {},
  "state_schema": {},
  "handoff_contract": {},
  "failure_controls": [],
  "prompt_scaffold": {},
  "export_policy": {}
}
```

## Runtime Roles

- `scheduler`: wakes the loop and decides whether work continues.
- `executor`: performs route-specific work.
- `verifier`: runs tests, audits, critic checks, and acceptance gates.
- `memory_writer`: persists state, failures, and handoff notes.
- `merge_or_handoff`: merges accepted work or asks for human review.

## Practical Call Table

| Trigger | Runtime mode | Required layer |
| --- | --- | --- |
| `issue`, `CI`, `PR`, `GitHub` | event-connected dev loop | Git/GitHub connector, tests, verifier |
| `worktree`, `parallel`, `多个 Agent` | parallel loop | worktree isolation and ownership gate |
| `每天`, `定时`, `30 minutes` | scheduled monitor loop | scheduler and memory file |
| `validator`, `verifier`, `验收` | validation loop | executor/verifier split |
| `长期记忆`, `persistent memory` | durable loop | state file and failure memory |

## CLI

```powershell
py -m app.cli kernel loop-engineering "Loop Engineering 调度 issue CI，worktree 并行隔离，validator 验收，写入长期记忆"
```

Use `kernel loop-prompt` when you only need a prompt iteration pack. Use `kernel loop-engineering` when the loop must operate as a system.
