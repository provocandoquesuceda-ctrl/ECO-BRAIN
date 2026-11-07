import pytest

from core.mission_control import MissionControl


EXPECTED_EVENTS = [
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


def test_eco_cel_cycle_is_traceable_and_human_governed():
    brain = MissionControl()

    result = brain.run_cycle(
        "Analiza el estado actual de ECO-BRAIN.",
        "Verificar el siguiente incremento mínimo.",
    )

    assert result["mission_id"].startswith("MIS-")
    assert result["trace_id"].startswith("TRC-")
    assert result["status"] == "cycle_verified"
    assert result["execution_mode"] == "human_governed"
    assert result["trace_events"] == 9
    assert [trace.event for trace in brain.traces] == EXPECTED_EVENTS
    assert brain.traces[-1].event == "STATE_UPDATED"


def test_incomplete_trace_cannot_be_reported_as_verified():
    class MissingProposalMissionControl(MissionControl):
        def _trace(self, mission_id: str, event: str, data: dict) -> None:
            if event == "PROPOSED":
                return
            super()._trace(mission_id, event, data)

    brain = MissingProposalMissionControl()

    with pytest.raises(RuntimeError, match="Mission trace verification failed"):
        brain.run_cycle("Analiza una misión incompleta.", "No declarar éxito.")

    events = [trace.event for trace in brain.traces]
    assert "PROPOSED" not in events
    assert "VERIFIED" not in events
