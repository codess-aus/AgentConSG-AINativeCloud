---
title: Inspectable engineering
hero: assets/6-inspectable.png
hero_alt: "Keep the work inspectable. Specify, build, test, review, learn. Version control, tests, review, and CI still apply. Measure the outcome, not how fast the first draft appeared. Watercolour Singapore shophouses."
---

# 06 · Keep the work inspectable

**Specify → build → test → review → learn.** Copilot can accelerate a draft; it does not remove the need for evidence.

## Keep changes small enough to understand

Start an issue with intent and acceptance criteria. Ask Copilot to inspect the relevant code and propose a plan. Implement one bounded change on a branch, run the focused tests, then inspect the diff yourself. Request an independent human review for consequential changes.

If you delegate an issue to a Copilot coding agent, give it the same scope and test expectations. Its pull request is a proposed change, not a release approval. Keep required checks and branch rules in force.

## Make the evidence reproducible

The sample exposes a deterministic fixture so a reviewer can reproduce the result locally. This is deliberately separate from evaluating a live model.

```python
import json

from examples.cloud_triage import Incident, ToolBudget, execute, propose

plan = propose(Incident(service="checkout", error_rate=0.12))
result = execute(
    plan,
    allowed_services={"checkout"},
    budget=ToolBudget(max_calls=1),
)

# Record the chosen action and outcome, not raw incident payloads or secrets.
evidence = {"service": plan.service, "action": plan.action, "status": result["status"]}
print(json.dumps(evidence, sort_keys=True))
assert evidence["status"] == "ok"
```

For a real system, add a trace identifier, policy version, prompt/model version, latency, and redacted tool outcomes. Use your organisation's retention and access controls. More logging is not always better if it captures sensitive inputs.

!!! example "Try with GitHub Copilot"
    Ask: "Plan a change to include a non-empty trace identifier in the execution result. Identify the acceptance tests and affected consumers first. Implement only that change, then explain the diff against the criteria."

## Checkpoint

Prepare a pull request description linking the issue, the intended behaviour, test evidence, residual risk, and rollback plan. A reviewer should not need access to your private chat to understand the change.
