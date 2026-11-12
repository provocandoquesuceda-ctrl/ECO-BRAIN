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
    assert final_recheck["automation_run_id"] == evidence["automation_run_id"]
    assert final_recheck["recorded_status"] == "completed"
    assert final_recheck["completed_at"] == "2026-11-12T13:15:24.989055Z"
