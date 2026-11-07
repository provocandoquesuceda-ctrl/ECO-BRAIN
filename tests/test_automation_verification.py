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
