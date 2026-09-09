"""Evidence-first verification for automation-triggered ECO-CEL runs."""

from datetime import datetime, timezone


REQUIRED_FIELDS = {
    "automation_name",
    "observed_commit",
    "observed_status",
    "eco_cel_status",
    "trace_id",
    "execution_evidence",
}


def build_verification_record(
    automation_name: str,
    observed_commit: str,
    observed_status: str,
    eco_cel_status: str,
    trace_id: str,
    execution_evidence: str,
) -> dict:
    """Build a minimal, serializable record for a real automation observation."""
    record = {
        "automation_name": automation_name,
        "observed_commit": observed_commit,
        "observed_status": observed_status,
        "eco_cel_status": eco_cel_status,
        "trace_id": trace_id,
        "execution_evidence": execution_evidence,
        "recorded_at": datetime.now(timezone.utc).isoformat(),
    }
    validate_verification_record(record)
    return record


def validate_verification_record(record: dict) -> None:
    """Reject incomplete evidence; do not infer execution from code presence."""
    missing = REQUIRED_FIELDS - record.keys()
    if missing:
        raise ValueError(f"Missing verification evidence fields: {sorted(missing)}")

    for field in REQUIRED_FIELDS:
        value = record[field]
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"Verification field must be a non-empty string: {field}")

    if record["eco_cel_status"] != "cycle_verified":
        raise ValueError("eco_cel_status must be cycle_verified")
