from core.mission_control import MissionControl


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
    assert brain.traces[-1].event == "STATE_UPDATED"
