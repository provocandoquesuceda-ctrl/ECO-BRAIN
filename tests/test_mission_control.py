from core.mission_control import MissionControl


def test_receive_creates_mission_and_trace():
    brain = MissionControl()
    result = brain.receive("test task")

    assert result["mission_id"].startswith("MIS-")
    assert result["trace_id"].startswith("TRC-")
    assert result["status"] == "received"
    assert len(brain.traces) == 2
