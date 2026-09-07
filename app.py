from core.mission_control import MissionControl


brain = MissionControl()


def mission(task: str) -> dict:
    """Entry point for the first ECO-BRAIN Mission Control proof."""
    return brain.receive(task)


if __name__ == "__main__":
    print(mission("Analiza el estado actual del ecosistema y propone el siguiente paso."))
