from app import mission


def test_app_entrypoint_runs_existing_human_governed_cycle():
    result = mission(
        "Analiza el estado actual del ecosistema.",
        "Verificar el siguiente incremento mínimo.",
    )

    assert result["mission_id"].startswith("MIS-")
    assert result["trace_id"].startswith("TRC-")
    assert result["status"] == "cycle_verified"
    assert result["execution_mode"] == "human_governed"
    assert result["trace_events"] == 9


def test_receive_only_call_remains_backward_compatible():
    result = mission("Recibir una tarea sin ejecutar el ciclo.")

    assert result["mission_id"].startswith("MIS-")
    assert result["trace_id"].startswith("TRC-")
    assert result["status"] == "received"
    assert result["next_stage"] == "context"
