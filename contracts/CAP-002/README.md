# CAP-002 Consumer Contract v1

Status: PILOT / isolated; not released.

## Purpose
Define a stable, machine-validated boundary for a consumer that requests an ECO-BRAIN Mission Control cycle. The contract does not grant authority to execute external or irreversible actions.

## Request
A JSON object conforming to `request.schema.json`:
- `contract_version`: `1.0`
- `capability`: `CAP-002`
- `task`: task description
- `proposed_action`: proposed next action only

## Response
A JSON object conforming to `response.schema.json`. The adapter must invoke the real `core.mission_control.MissionControl.run_cycle(task, proposed_action)` implementation and preserve its `mission_id`, `trace_id`, `status`, `execution_mode`, `next_action`, and `trace_events` values. Contract metadata may be added by the adapter.

## Safety and authority
- Execution mode must remain `human_governed`.
- The cycle is proposal-only; no external services or irreversible actions.
- The consumer must fail closed if schema validation fails.
- A passing contract test proves the tested commit pair works together; it does not certify legal correctness or production readiness.

## Reproducibility
The consumer CI must check out this repository at an immutable commit SHA, not a moving branch. Record the consumer commit, producer commit, CI run ID, test result, and artifacts before promoting the pilot.
