from core.models import Mission, Trace


class MissionControl:
    """Minimal orchestration loop for ECO-BRAIN v0.1 and ECO-CEL proofing."""

    CYCLE_EVENTS = (
        "MISSION_RECEIVED",
        "MISSION_INITIALIZED",
        "OBSERVED",
        "ANALYZED",
        "PRIORITIZED",
        "PREPARED",
        "PROPOSED",
        "VERIFIED",
        "STATE_UPDATED",
    )

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
        """Execute a deterministic cycle and verify its trace before success.

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

        expected_prefix = self.CYCLE_EVENTS[:7]
        self._verify_mission_events(mission_id, expected_prefix)

        self._trace(
            mission_id,
            "VERIFIED",
            {"criterion": "expected_trace_prefix_complete"},
        )
        self._trace(
            mission_id,
            "STATE_UPDATED",
            {"next_action": next_action, "status": "ready_for_next_cycle"},
        )

        self._verify_mission_events(mission_id, self.CYCLE_EVENTS)
        mission_traces = [
            trace for trace in self.traces if trace.mission_id == mission_id
        ]

        return {
            "mission_id": mission_id,
            "task": task,
            "status": "cycle_verified",
            "next_action": next_action,
            "execution_mode": "human_governed",
            "trace_id": mission_traces[-1].trace_id,
            "trace_events": len(mission_traces),
        }

    def _verify_mission_events(
        self, mission_id: str, expected_events: tuple[str, ...]
    ) -> None:
        """Raise instead of reporting success when the mission trace is incomplete."""
        actual_events = tuple(
            trace.event for trace in self.traces if trace.mission_id == mission_id
        )
        if actual_events != expected_events:
            raise RuntimeError(
                "Mission trace verification failed: "
                f"expected {expected_events}, received {actual_events}"
            )

    def _trace(self, mission_id: str, event: str, data: dict) -> None:
        self.traces.append(Trace(mission_id=mission_id, event=event, data=data))
