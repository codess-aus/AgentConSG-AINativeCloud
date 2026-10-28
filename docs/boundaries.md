---
title: Tools and boundaries
hero: assets/5-boundaries.png
hero_alt: "Design the boundaries, not just the tools. Model plus context plus tools plus control flow plus human oversight. What is the smallest useful set of capabilities, and what boundaries keep their use appropriate? A blue-hour bridge at Clarke Quay."
---

# 05 · Design the boundaries, not just the tools

An agent combines **model, context, tools, control flow, and human oversight**. Connecting a tool does not establish a safe workflow.

## Enforce the contract outside the model

MCP can expose tools and data through a standard protocol. It does not decide which operations your application should authorise, how to isolate tenants, or when to stop. Apply those controls in trusted code and at the underlying service.

The sample has an action allowlist, service allowlist, validated input types, and a maximum number of tool calls. The dispatcher checks policy before accessing the fixture. The model cannot expand its own permissions.

```python
from examples.cloud_triage import Incident, ToolBudget, execute, propose

budget = ToolBudget(max_calls=1)
plan = propose(Incident(service="checkout", error_rate=0.12))
result = execute(plan, allowed_services={"checkout"}, budget=budget)

assert result["status"] == "ok"
assert budget.used == 1

try:
    execute(plan, allowed_services={"checkout"}, budget=budget)
except RuntimeError as error:
    print(f"Stopped at the tool boundary: {error}")
else:
    raise AssertionError("The second tool call must be blocked")
```

Counting calls prevents unbounded iteration, but it is not a wall-clock timeout or a cost cap. For remote tools, also apply connection and response deadlines, bounded output sizes, cancellation, and a retry policy. Keep retries inside the same overall budget.

## Minimise authority

Expose a narrow `read_metrics` capability instead of arbitrary shell execution. Resolve service identifiers against the authenticated caller's scope. Never pass model-generated strings into a shell or accept an unrestricted URL as a telemetry endpoint.

!!! example "Try with GitHub Copilot"
    Ask: "Trace every route into execute. Check that authorisation and budget enforcement happen before tool access. Draft tests for an unknown action, a different service, an exhausted budget, and instruction-like text in a reason."

## Checkpoint

Demonstrate that changing `Plan.reason` cannot permit a forbidden action. Document which layer owns credentials, policy, cancellation, and audit records before connecting a real cloud tool.
