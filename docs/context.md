---
title: Context and specifications
hero: assets/4-context.png
hero_alt: "Right context beats more context. Intent: goal and success criteria. Relevant context: right information, time, and form. Constraints: visible assumptions and explicit scope. Together these produce better AI work. Blue and purple lanterns above a Singapore street."
---

# 04 · Right context beats more context

**Intent + relevant context + constraints → better AI work.**

A larger prompt is not automatically a better specification. Prefer current, authoritative information that explains the task and its limits. Remove secrets and unrelated customer data before providing context to any AI tool.

## Give Copilot a reviewable target

Start with the issue's goal, the relevant Python module, existing tests, and operational constraints. Ask Copilot to identify assumptions before changing code. Use repository instructions in `.github/copilot-instructions.md` for stable conventions; keep task-specific acceptance criteria in the issue or specification.

A useful specification for this example states that an unknown service is rejected, missing telemetry is escalated, rates must be finite values from zero to one, and tool calls are capped. Define how you will verify each statement.

```python
from examples.cloud_triage import Incident, propose

# Missing telemetry is a first-class state, not a zero error rate.
incident = Incident(service="checkout", error_rate=None)
plan = propose(incident)
assert plan.action == "escalate"
assert "missing" in plan.reason.lower()
```

Preserving the difference between **missing** and **healthy** avoids a common data-contract bug. A default of zero would make an unavailable monitoring source look like a healthy service.

## Treat retrieved material as data

Runbooks, issue comments, and tool results can contain instructions written by untrusted parties. Preserve provenance and freshness, but do not let retrieved text override the system's tool policy. Context selection and permission enforcement solve different problems.

!!! example "Try with GitHub Copilot"
    Attach `examples/cloud_triage.py` and `tests/test_cloud_triage.py`. Ask: "Propose a specification for stale telemetry. Define the timestamp contract, maximum age, timezone handling, and safe failure. Ask about ambiguous requirements before implementing."

## Checkpoint

Produce a small acceptance table covering normal input, missing input, invalid input, and out-of-scope targets. Each row should have an expected outcome and an automated test. Decide the stale-data policy with a human before coding it.
