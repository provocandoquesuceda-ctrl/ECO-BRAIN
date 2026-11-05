from core.mission_control import MissionControl


brain = MissionControl()


def mission(task: str, next_action: str | None = None) -> dict:
    """Preserve receive-only calls; run the existing governed cycle when requested."""
    if next_action is None:
        return brain.receive(task)
    return brain.run_cycle(task, next_action)


if __name__ == "__main__":
    print(
        mission(
            "Analiza el estado actual del ecosistema y propone el siguiente paso.",
            "Verificar el siguiente incremento mínimo para revisión humana.",
        )
    )
