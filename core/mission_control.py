from core.models import Mission, Trace


class MissionControl:
    """Minimal orchestration loop for ECO-BRAIN v0.1 and ECO-CEL proofing."""

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

    def run_cycle(self, task: str, next_action: str) -> dict:
        """Execute a deterministic ECO-CEL control cycle without external side effects.

        The default execution posture is proposal-only. This proves continuity and
        traceability while keeping strategic, sensitive, and irreversible actions
        outside automatic authority.
        """
        received = self.receive(task)
        mission_id = received["mission_id"]

        self._trace(mission_id, "OBSERVED", {"task": task})
        self._trace(mission_id, "ANALYZED", {"finding": "cycle_ready"})
        self._trace(mission_id, "PRIORITIZED", {"next_action": next_action})
        self._trace(mission_id, "PREPARED", {"action": next_action})
        self._trace(
            mission_id,
            "PROPOSED",
            {"action": next_action, "execution_mode": "human_governed"},
        )
        self._trace(mission_id, "VERIFIED", {"criterion": "trace_complete"})
        self._trace(
            mission_id,
            "STATE_UPDATED",
            {"next_action": next_action, "status": "ready_for_next_cycle"},
        )

        return {
            "mission_id": mission_id,
            "task": task,
            "status": "cycle_verified",
            "next_action": next_action,
            "execution_mode": "human_governed",
            "trace_id": self.traces[-1].trace_id,
            "trace_events": len(
                [trace for trace in self.traces if trace.mission_id == mission_id]
            ),
        }

    def _trace(self, mission_id: str, event: str, data: dict) -> None:
        self.traces.append(Trace(mission_id=mission_id, event=event, data=data))
