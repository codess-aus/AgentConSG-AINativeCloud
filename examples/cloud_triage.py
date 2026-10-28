"""A deterministic, read-only harness to explore agent boundaries without credentials."""

from dataclasses import dataclass
import json
import math
from types import MappingProxyType


ALLOWED_ACTIONS = frozenset({"read_metrics", "summarise", "escalate"})
METRICS = MappingProxyType({"checkout": 0.12})


@dataclass(frozen=True)
class Incident:
    service: str
    error_rate: float | None

    def __post_init__(self):
        if not isinstance(self.service, str) or not self.service.strip():
            raise ValueError("service must be a non-empty string")
        if self.error_rate is not None:
            if (
                isinstance(self.error_rate, bool)
                or not isinstance(self.error_rate, (int, float))
                or not math.isfinite(self.error_rate)
                or not 0 <= self.error_rate <= 1
            ):
                raise ValueError("error_rate must be finite and between 0 and 1")


@dataclass(frozen=True)
class Plan:
    service: str
    action: str
    reason: str

    def __post_init__(self):
        for field in ("service", "action", "reason"):
            value = getattr(self, field)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{field} must be a non-empty string")


@dataclass
class ToolBudget:
    max_calls: int
    used: int = 0

    def __post_init__(self):
        for field in ("max_calls", "used"):
            value = getattr(self, field)
            if type(value) is not int or value < 0:
                raise ValueError(f"{field} must be a non-negative integer")
        if self.used > self.max_calls:
            raise ValueError("used cannot exceed max_calls")

    def consume(self) -> None:
        if self.used >= self.max_calls:
            raise RuntimeError("tool-call budget exhausted")
        self.used += 1


def propose(incident: Incident) -> Plan:
    """Stand in for a model so policy tests are repeatable and offline."""
    if incident.error_rate is None:
        return Plan(incident.service, "escalate", "Telemetry is missing; ask the owner.")
    if incident.error_rate >= 0.05:
        return Plan(incident.service, "read_metrics", "Error rate meets the 5% threshold.")
    return Plan(incident.service, "summarise", "Error rate is below the 5% threshold.")


def authorise(plan: Plan, *, allowed_services: set[str]) -> None:
    if plan.service not in allowed_services:
        raise PermissionError(f"service is outside the caller's scope: {plan.service}")
    if plan.action not in ALLOWED_ACTIONS:
        raise PermissionError(f"action is not permitted: {plan.action}")


def execute(
    plan: Plan,
    *,
    allowed_services: set[str],
    budget: ToolBudget,
) -> dict[str, str | float]:
    """Validate authority before dispatch; only metric access consumes a tool call."""
    authorise(plan, allowed_services=allowed_services)
    if plan.action == "escalate":
        return {"status": "needs_human", "service": plan.service, "reason": plan.reason}
    if plan.action == "summarise":
        return {"status": "summary", "service": plan.service, "reason": plan.reason}

    budget.consume()
    if plan.service not in METRICS:
        raise LookupError(f"no metric fixture available for service: {plan.service}")
    return {
        "status": "ok",
        "service": plan.service,
        "error_rate": METRICS[plan.service],
    }


def main() -> None:
    incident = Incident(service="checkout", error_rate=0.12)
    result = execute(
        propose(incident),
        allowed_services={"checkout"},
        budget=ToolBudget(max_calls=1),
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
