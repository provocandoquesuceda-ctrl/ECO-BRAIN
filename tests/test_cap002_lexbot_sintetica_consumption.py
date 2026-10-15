"""Controlled consumer test for CAP-002 (ECO-BRAIN Mission Control).

This test exercises the existing host API without calling external services or
performing irreversible actions. It is an isolated proof branch for LEXBOT
Sintética reuse evaluation; it does not integrate or release either product.
"""

from core.mission_control import MissionControl


def test_cap002_controlled_consumption_is_traceable_and_proposal_only():
    control = MissionControl()
    task = "LEXBOT Sintética: evaluar un escenario jurídico estrictamente ficticio"
    proposed_action = "Preparar un escenario sintético para revisión humana; no ejecutar acciones externas"

    result = control.run_cycle(task, proposed_action)

    assert result["status"] == "cycle_verified"
    assert result["task"] == task
    assert result["next_action"] == proposed_action
    assert result["execution_mode"] == "human_governed"
    assert result["mission_id"].startswith("MIS-")
    assert result["trace_id"].startswith("TRC-")
    assert result["trace_events"] == 9

    events = [event.event for event in control.traces if event.mission_id == result["mission_id"]]
    assert events == [
        "MISSION_RECEIVED",
        "MISSION_INITIALIZED",
        "OBSERVED",
        "ANALYZED",
        "PRIORITIZED",
        "PREPARED",
        "PROPOSED",
        "VERIFIED",
        "STATE_UPDATED",
    ]
