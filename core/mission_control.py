from core.models import Mission, Trace


class MissionControl:
    """Minimal orchestration loop for ECO-BRAIN v0.1."""

    def __init__(self) -> None:
        self.traces: list[Trace] = []

    def receive(self, task: str) -> dict:
        mission = Mission(task=task)
        self._trace(mission.mission_id, "MISSION_RECEIVED", {"task": task})

        result = {
            "mission_id": mission.mission_id,
            "task": task,
            "status": "received",
            "next_stage": "context",
        }
        self._trace(mission.mission_id, "MISSION_INITIALIZED", result)
        result["trace_id"] = self.traces[-1].trace_id
        return result

    def _trace(self, mission_id: str, event: str, data: dict) -> None:
        self.traces.append(Trace(mission_id=mission_id, event=event, data=data))
