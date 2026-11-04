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

## Map the work before choosing the agent

<figure class="workshop-slide" markdown="1">

![Six design moves for safe agents: map to the software development lifecycle, define the task, separate planning from action, gate with pull requests, build reliable workflows, and operate safely.](assets/4A-map.png){ loading=lazy decoding=async }

<figcaption>Context includes the delivery process: define where the agent participates and where decisions remain controlled.</figcaption>
</figure>

The six moves connect a good specification to an operable system. Map the task to a lifecycle stage, define its inputs and success criteria, separate the proposed plan from execution, use pull requests as review gates, make workflow handoffs explicit, and design operational limits. They are connected controls, not six extra paragraphs to paste into every prompt.

For the triage workshop, a small change such as adding trace identifiers belongs primarily to implementation and validation. Its context should include the execution result contract, affected consumers, and tests. Production deployment credentials would add authority without helping the task. This is why context selection should follow the work's purpose rather than expose everything the platform can reach.

## Give each lifecycle stage an evidence home

<figure class="workshop-slide" markdown="1">

![Agents mapped to planning, implementation, validation, and deployment. Evidence belongs in issues and plans, branches and commits, workflow checks and artifacts, and deployment environments and approvals respectively.](assets/4B-MapBoundaries.png){ loading=lazy decoding=async }

<figcaption>Map responsibilities and durable evidence across the software development lifecycle, rather than treating an agent as an unrestricted developer.</figcaption>
</figure>

| Stage | Bounded contribution | Evidence and decision |
|---|---|---|
| Planning | Identify assumptions, draft scope, and propose acceptance criteria. | An issue or versioned plan records intent; a responsible person accepts the approach. |
| Implementation | Make the agreed change on a branch. | Commits and a pull request expose exactly what changed; reviewers challenge scope drift. |
| Validation | Run agreed checks and report failures. | Workflow runs, test reports, and evaluation results support a decision about the exact revision. |
| Deployment | Prepare release information without assuming production authority. | Protected environments and authenticated approvals govern release where configured. |

A handoff should carry the task identifier, accepted scope, revision, unresolved assumptions, and links to evidence. If validation finds that the specification is ambiguous, return to planning rather than letting an implementation agent silently redefine success.

This mapping also identifies controls that prose cannot enforce. Saying "validation only" does not make an agent read-only; its runtime permissions must match that role. The [boundaries chapter](boundaries.md#draw-the-boundary-before-work-starts) develops the corresponding task contract, and [least privilege](least-privilege.md#enforce-the-plan-to-action-handoff) explains enforcement.

!!! example "Try with GitHub Copilot"
    Attach `examples/cloud_triage.py` and `tests/test_cloud_triage.py`. Ask: "Propose a specification for stale telemetry. Define the timestamp contract, maximum age, timezone handling, and safe failure. Ask about ambiguous requirements before implementing."

## Checkpoint

Produce a small acceptance table covering normal input, missing input, invalid input, and out-of-scope targets. Each row should have an expected outcome and an automated test. Decide the stale-data policy with a human before coding it.
