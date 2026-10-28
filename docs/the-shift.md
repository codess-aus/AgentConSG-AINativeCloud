---
title: From assisted to native
hero: assets/2-theShift.png
hero_alt: "From AI-assisted to AI-native: AI as assistant provides isolated help; AI in the workflow participates across the lifecycle; AI as part of the system is designed with clear boundaries. A colourful Singapore mural street."
---

# 02 · From AI-assisted to AI-native

**AI as assistant → AI in the workflow → AI as part of the system.**

These are different integration points, not a maturity ladder that every application must climb. You can improve delivery with Copilot without adding any AI to your production application.

## Separate development-time and runtime AI

At development time, Copilot can explain a module, draft tests, or implement an issue in a reviewable branch. At runtime, an agent can select a tool based on changing evidence. Runtime decisions need their own authentication, validation, budgets, and observability; your editor's review workflow does not provide those controls for your application.

In the workshop, Copilot is the development-time assistant. The Python fixture stands in for a runtime planner so that the action boundary is independently testable.

```python
from examples.cloud_triage import Incident, propose

healthy = propose(Incident(service="checkout", error_rate=0.01))
degraded = propose(Incident(service="checkout", error_rate=0.12))
unknown = propose(Incident(service="checkout", error_rate=None))

assert healthy.action == "summarise"
assert degraded.action == "read_metrics"
assert unknown.action == "escalate"
```

The last result matters: missing context should produce an explicit escalation, not a confident diagnosis. The workflow can still be useful when it cannot complete the original task.

## Choose the smallest useful workflow

Begin with a single bounded task such as drafting a triage summary. Avoid a multi-agent design unless you can explain what independent role each agent plays and how you evaluate their coordination. More tool calls create more latency, cost, and failure opportunities.

!!! example "Try with GitHub Copilot"
    Ask: "Using the triage example, compare a deterministic rule, a single model call, and a tool-using agent. Explain which requirement would justify each option. Do not implement a model integration."

## Checkpoint

Draw two separate boundaries: Copilot's contribution to your development process, and the runtime system's authority. Identify one operation that should stay deterministic, even if a model proposes it.
