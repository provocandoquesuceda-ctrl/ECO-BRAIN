from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


@dataclass
class Mission:
    task: str
    mission_id: str = field(default_factory=lambda: f"MIS-{uuid4().hex[:12]}")
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )


@dataclass
class Trace:
    mission_id: str
    event: str
    data: dict = field(default_factory=dict)
    trace_id: str = field(default_factory=lambda: f"TRC-{uuid4().hex[:12]}")
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
