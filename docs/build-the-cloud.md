---
title: Build the AI-native cloud
hero: assets/1-BuildTheCloud.png
hero_alt: "Building the AI-Native Cloud, Michelle Sandford, Azure Developer Engagement Lead, Microsoft ANZ. AI-native is a way of engineering, not a feature. Watercolour Singapore shophouses with purple and blue light trails."
---

# 01 · Build the AI-native cloud

**AI-native is a way of engineering, not a feature.**

Putting a model behind an endpoint does not make a cloud service dependable. The engineering problem includes context selection, tool permissions, state, evaluation, deployment, and incident response. Design those parts together rather than treating safeguards as a post-demo task.

## Start with an operational problem

Our scenario is incident triage: an operator wants to understand a degraded cloud service. The assistant may inspect a small, sanitised service snapshot and suggest a next step. It must not restart workloads, alter infrastructure, or invent missing telemetry.

The example deliberately separates **a proposal** from **permission to act**. It uses deterministic Python so you can test the harness without an API key. A production model would propose the same structured plan, which must be validated before dispatch.

```python
from examples.cloud_triage import Incident, propose

incident = Incident(service="checkout", error_rate=0.12)
plan = propose(incident)
assert plan.action == "read_metrics"
print(plan)
```

`0.12` means 12% of requests are failing. The initial policy uses 5% as a teaching threshold, not a universal production SLO. A real team derives thresholds from its service objectives and traffic profile.

## Place AI in the Agentic SDLC

Use Copilot to explore the existing service and draft acceptance criteria before implementation. Keep the issue, reviewed specification, code change, tests, and operational evidence linked. The release decision belongs to the service owner.

!!! example "Try with GitHub Copilot"
    Open `examples/cloud_triage.py`. Ask: "Explain the incident-triage flow without changing files. Identify the trust boundary between a proposal and tool execution. Draft acceptance criteria for a read-only first release, including missing telemetry and an unknown service."

## Checkpoint

You should have a scope statement, a named release owner, and at least three observable acceptance criteria. One must say **no infrastructure mutation**. If the task is fully specified by stable rules, consider whether ordinary code is sufficient before introducing a model.
