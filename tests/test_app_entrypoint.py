import ast
import subprocess
import sys
from pathlib import Path

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


def test_cli_executes_the_governed_cycle():
    root = Path(__file__).resolve().parents[1]
    completed = subprocess.run(
        [sys.executable, str(root / "app.py")],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    result = ast.literal_eval(completed.stdout)

    assert result["status"] == "cycle_verified"
    assert result["execution_mode"] == "human_governed"
    assert result["trace_events"] == 9
