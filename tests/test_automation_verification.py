import json
from pathlib import Path

import pytest

from core.automation_verification import (
    build_verification_record,
    validate_verification_record,
)


def test_builds_minimal_automation_evidence_record():
    record = build_verification_record(
        automation_name="ECO-BRAIN Daily Sprint",
        observed_commit="abc123",
        observed_status="main_observed",
        eco_cel_status="cycle_verified",
        trace_id="TRC-test",
        execution_evidence="workflow_run:123",
    )

    assert record["automation_name"] == "ECO-BRAIN Daily Sprint"
    assert record["eco_cel_status"] == "cycle_verified"
    assert record["trace_id"] == "TRC-test"
    assert record["recorded_at"]


def test_rejects_records_without_execution_evidence():
    with pytest.raises(ValueError, match="execution_evidence"):
        validate_verification_record(
            {
                "automation_name": "ECO-BRAIN Daily Sprint",
                "observed_commit": "abc123",
                "observed_status": "main_observed",
                "eco_cel_status": "NOT_REVALIDATED_IN_THIS_AUDIT",
                "trace_id": "TRC-test",
                "execution_evidence": "",
            }
        )


def test_preserves_explicit_non_verified_eco_cel_status():
    record = build_verification_record(
        automation_name="ECO-BRAIN Daily Verification",
        observed_commit="abc123",
        observed_status="completed",
        eco_cel_status="NOT_REVALIDATED_IN_THIS_AUDIT",
        trace_id="TRC-test",
        execution_evidence="automation_run:run-123",
    )

    assert record["eco_cel_status"] == "NOT_REVALIDATED_IN_THIS_AUDIT"


def test_rejects_blank_eco_cel_status():
    with pytest.raises(ValueError, match="eco_cel_status"):
        validate_verification_record(
            {
                "automation_name": "ECO-BRAIN Daily Verification",
                "observed_commit": "abc123",
                "observed_status": "completed",
                "eco_cel_status": " ",
                "trace_id": "TRC-test",
                "execution_evidence": "automation_run:run-123",
            }
        )


def test_rejects_unknown_eco_cel_status():
    with pytest.raises(ValueError, match="eco_cel_status must be one of"):
        validate_verification_record(
            {
                "automation_name": "ECO-BRAIN Daily Verification",
                "observed_commit": "abc123",
                "observed_status": "completed",
                "eco_cel_status": "designed",
                "trace_id": "TRC-test",
                "execution_evidence": "automation_run:run-123",
            }
        )


def test_daily_verification_evidence_passes_existing_verifier():
    evidence_path = (
        Path(__file__).resolve().parents[1]
        / "evidence/automation-runs/2026-11-07-eco-brain-daily-verification.json"
    )
    evidence = json.loads(evidence_path.read_text(encoding="utf-8"))

    validate_verification_record(evidence["verification_record"])

    assert evidence["verification_record"]["trace_id"] == evidence["trace_id"]
    assert (
        evidence["verification_record"]["eco_cel_status"]
        == "NOT_REVALIDATED_IN_THIS_AUDIT"
    )


def test_daily_verification_20261108_evidence_passes_existing_verifier():
    evidence_path = (
        Path(__file__).resolve().parents[1]
        / "evidence/automation-runs/2026-11-08-eco-brain-daily-verification.json"
    )
    evidence = json.loads(evidence_path.read_text(encoding="utf-8"))

    validate_verification_record(evidence["verification_record"])

    assert evidence["verification_record"]["trace_id"] == evidence["trace_id"]
    assert (
        evidence["verification_record"]["eco_cel_status"]
        == "NOT_REVALIDATED_IN_THIS_AUDIT"
    )
    assert evidence["verification_record"]["observed_status"] == "in_progress"



def test_daily_verification_20261110_evidence_preserves_capture_and_terminal_recheck():
    evidence_path = (
        Path(__file__).resolve().parents[1]
        / "evidence/automation-runs/2026-11-10-eco-brain-daily-verification.json"
    )
    evidence = json.loads(evidence_path.read_text(encoding="utf-8"))

    validate_verification_record(evidence["verification_record"])

    assert evidence["automation_run_status_at_capture"] == "in_progress"
    assert evidence["completed_at"] is None
    assert evidence["verification_record"]["observed_status"] == "in_progress"

    final_recheck = evidence["final_platform_recheck"]
    assert final_recheck["automation_run_id"] == evidence["automation_run_id"]
    assert final_recheck["recorded_status"] == "completed"
    assert final_recheck["completed_at"] == "2026-11-10T13:13:23.073530Z"

def test_daily_verification_20261112_evidence_preserves_capture_and_terminal_recheck():
    evidence_path = (
        Path(__file__).resolve().parents[1]
        / "evidence/automation-runs/2026-11-12-eco-brain-daily-verification.json"
    )
    evidence = json.loads(evidence_path.read_text(encoding="utf-8"))

    validate_verification_record(evidence["verification_record"])

    assert evidence["automation_run_status_at_capture"] == "in_progress"
    assert evidence["completed_at"] is None
    assert evidence["verification_record"]["observed_status"] == "in_progress"

    final_recheck = evidence["final_platform_recheck"]
    assert evidence["automation_run_id"] == "aa3d5d5a-2fe8-8330-a04e-339ea33930ca"
    assert final_recheck["automation_run_id"] == evidence["automation_run_id"]
    assert final_recheck["recorded_status"] == "completed"
    assert final_recheck["completed_at"] == "2026-11-12T13:15:24.989055Z"

def test_daily_verification_20261113_evidence_preserves_capture_and_terminal_recheck():
    evidence_path = (
        Path(__file__).resolve().parents[1]
        / "evidence/automation-runs/2026-11-13-eco-brain-daily-verification.json"
    )
    evidence = json.loads(evidence_path.read_text(encoding="utf-8"))

    validate_verification_record(evidence["verification_record"])

    assert evidence["automation_run_status_at_capture"] == "in_progress"
    assert evidence["completed_at"] is None
    assert evidence["verification_record"]["observed_status"] == "in_progress"

    final_recheck = evidence["final_platform_recheck"]
    assert evidence["automation_run_id"] == "575c52c1-700c-8322-9a9e-b5ffc5938226"
    assert final_recheck["automation_run_id"] == evidence["automation_run_id"]
    assert final_recheck["recorded_status"] == "completed"
    assert final_recheck["completed_at"] == "2026-11-13T13:20:02.364350Z"

def test_daily_verification_20261114_evidence_preserves_capture_and_terminal_recheck():
    evidence_path = (
        Path(__file__).resolve().parents[1]
        / "evidence/automation-runs/2026-11-14-eco-brain-daily-verification.json"
    )
    evidence = json.loads(evidence_path.read_text(encoding="utf-8"))

    validate_verification_record(evidence["verification_record"])

    assert evidence["automation_run_status_at_capture"] == "in_progress"
    assert evidence["completed_at"] is None
    assert evidence["verification_record"]["observed_status"] == "in_progress"

    final_recheck = evidence["final_platform_recheck"]
    assert evidence["automation_run_id"] == "aedeb923-4478-8328-baec-3fdb2fd11b68"
    assert final_recheck["automation_run_id"] == evidence["automation_run_id"]
    assert final_recheck["recorded_status"] == "completed"
    assert final_recheck["completed_at"] == "2026-11-14T13:45:46.633921Z"


def test_daily_verification_20261115_evidence_preserves_capture_and_terminal_recheck():
    evidence_path = (
        Path(__file__).resolve().parents[1]
        / "evidence/automation-runs/2026-11-15-eco-brain-daily-verification.json"
    )
    evidence = json.loads(evidence_path.read_text(encoding="utf-8"))

    validate_verification_record(evidence["verification_record"])

    assert evidence["automation_run_status_at_capture"] == "in_progress"
    assert evidence["completed_at"] is None
    final_recheck = evidence["final_platform_recheck"]
    assert final_recheck["automation_run_id"] == evidence["automation_run_id"]
    assert evidence["automation_run_id"] == "93b0fa5a-c2c4-832e-bd36-bd44c82e0384"
    assert final_recheck["recorded_status"] == "completed"
    assert final_recheck["completed_at"] == "2026-11-15T13:42:41.086810Z"


def test_daily_verification_20261117_audit_record_captures_target_run_after_initial_snapshot():
    evidence_path = (
        Path(__file__).resolve().parents[1]
        / "evidence/automation-runs/2026-11-17-eco-brain-daily-verification.json"
    )
    evidence = json.loads(evidence_path.read_text(encoding="utf-8"))

    validate_verification_record(evidence["verification_record"])

    assert evidence["verification_record"]["observed_status"] == "in_progress"
    assert evidence["automation_id"] == "6a9eb5753ed08191819558c94fab138a"
    assert evidence["automation_run_id"] == "078ac166-af94-8326-87f4-c4520c64bf47"
    assert evidence["automation_run_status_at_capture"] == "in_progress"
    assert evidence["scheduled_for"] == "2026-11-17T13:00:37Z"
    assert evidence["started_at"] == "2026-11-17T13:14:58.843348Z"
    assert evidence["timestamp"] == evidence["started_at"]
    assert evidence["completed_at"] is None
    assert evidence["trace_id"] == "TRC-ECO-BRAIN-DV-20261117T131458Z"
    assert evidence["verification_record"]["observed_status"] == "in_progress"
    assert (
        evidence["execution"]["current_daily_verification_run"]["automation_run_id"]
        == evidence["automation_run_id"]
    )
    assert (
        evidence["execution"]["initial_daily_sprint_observation"]["target_platform_observation"]
        ["new_run_visible_for_2026_11_17"]
        is False
    )
    assert evidence["eco_cel_status"] == "NOT_REVALIDATED_IN_THIS_AUDIT"



def test_daily_verification_20261119_evidence_preserves_capture_and_terminal_recheck():
    evidence_path = (
        Path(__file__).resolve().parents[1]
        / "evidence/automation-runs/2026-11-19-eco-brain-daily-verification.json"
    )
    evidence = json.loads(evidence_path.read_text(encoding="utf-8"))

    validate_verification_record(evidence["verification_record"])

    assert evidence["automation_id"] == "6a9eb5753ed08191819558c94fab138a"
    assert evidence["automation_run_id"] == "87a02c07-2770-8332-931d-7efd70ca39f2"
    assert evidence["automation_run_status_at_capture"] == "in_progress"
    assert evidence["scheduled_for"] == "2026-11-19T13:00:37Z"
    assert evidence["started_at"] == "2026-11-19T13:20:16.018367Z"
    assert evidence["completed_at"] is None
    assert evidence["timestamp"] == evidence["started_at"]
    assert evidence["verification_record"]["observed_status"] == "in_progress"

    final_recheck = evidence["final_platform_recheck"]
    assert final_recheck["automation_run_id"] == evidence["automation_run_id"]
    assert final_recheck["recorded_status"] == "completed"
    assert final_recheck["completed_at"] == "2026-11-19T13:24:20.304205Z"
    assert final_recheck["historical_capture_preserved"] is True



def test_daily_verification_20261121_evidence_preserves_capture_and_terminal_recheck():
    evidence_path = (
        Path(__file__).resolve().parents[1]
        / "evidence/automation-runs/2026-11-21-eco-brain-daily-verification.json"
    )
    evidence = json.loads(evidence_path.read_text(encoding="utf-8"))

    validate_verification_record(evidence["verification_record"])

    assert evidence["automation_id"] == "6a9eb5753ed08191819558c94fab138a"
    assert evidence["automation_run_id"] == "1d350f25-07e0-832b-8ca5-50cd3125e63a"
    assert evidence["automation_run_status_at_initial_capture"] == "in_progress"
    assert evidence["scheduled_for"] == "2026-11-21T13:00:37Z"
    assert evidence["started_at"] == "2026-11-21T13:26:37.427570Z"
    assert evidence["timestamp"] == evidence["started_at"]
    assert evidence["completed_at"] is None
    assert evidence["trace_id"] == "TRC-ECO-BRAIN-DV-20261121T132637Z"
    assert evidence["verification_record"]["trace_id"] == evidence["trace_id"]
    assert evidence["verification_record"]["eco_cel_status"] == (
        "NOT_REVALIDATED_IN_THIS_AUDIT"
    )

    final_recheck = evidence["final_platform_recheck"]
    assert final_recheck["automation_run_id"] == evidence["automation_run_id"]
    assert final_recheck["recorded_status"] == "completed"
    assert final_recheck["completed_at"] == "2026-11-21T13:32:15.340377Z"
    assert "original capture remains unchanged" in final_recheck["note"].lower()

def test_daily_verification_20261122_evidence_preserves_capture_and_terminal_recheck():
    evidence_path = (
        Path(__file__).resolve().parents[1]
        / "evidence/automation-runs/2026-11-22-eco-brain-daily-verification.json"
    )
    evidence = json.loads(evidence_path.read_text(encoding="utf-8"))

    validate_verification_record(evidence["verification_record"])

    assert evidence["automation_id"] == "6a9eb5753ed08191819558c94fab138a"
    assert evidence["automation_run_id"] == "1252383f-bd24-8331-8cbf-ed6143230f73"
    assert evidence["automation_run_status_at_initial_capture"] == "in_progress"
    assert evidence["scheduled_for"] == "2026-11-22T13:00:37Z"
    assert evidence["started_at"] == "2026-11-22T13:26:20.173309Z"
    assert evidence["timestamp"] == evidence["started_at"]
    assert evidence["completed_at"] is None
    assert evidence["trace_id"] == "TRC-ECO-BRAIN-DV-20261122T132620Z"
    assert evidence["verification_record"]["observed_status"] == "in_progress"

    final_recheck = evidence["final_platform_recheck"]
    assert final_recheck["automation_run_id"] == evidence["automation_run_id"]
    assert final_recheck["latest_result_run_id"] == evidence["automation_run_id"]
    assert final_recheck["recorded_status"] == "completed"
    assert final_recheck["completed_at"] == "2026-11-22T13:32:16.866621Z"
    assert final_recheck["historical_capture_preserved"] is True
