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
                "eco_cel_status": "cycle_verified",
                "trace_id": "TRC-test",
                "execution_evidence": "",
            }
        )


def test_rejects_unverified_cycle_status():
    with pytest.raises(ValueError, match="cycle_verified"):
        validate_verification_record(
            {
                "automation_name": "ECO-BRAIN Daily Sprint",
                "observed_commit": "abc123",
                "observed_status": "main_observed",
                "eco_cel_status": "designed",
                "trace_id": "TRC-test",
                "execution_evidence": "workflow_run:123",
            }
        )
