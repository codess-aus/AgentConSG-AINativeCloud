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

## Separate plan, act, and verify

<figure class="workshop-slide" markdown="1">

![Separate planning, execution, and validation: record intent in an issue or pull request, implement through branch commits, and verify with checks, scans, artifacts, and review outcomes.](assets/6A-review.png){ loading=lazy decoding=async }

<figcaption>Review intent before accepting impact, then compare the implementation and evidence with the accepted plan.</figcaption>
</figure>

When planning, execution, and validation are mixed into a single conversation, reviewers may see only the final diff. Preserve the plan as an issue comment, pull request description, or versioned document before consequential implementation begins. It should identify expected files, behavioural changes, non-goals, and checks, not just a list of editing steps.

Execution then produces the concrete branch commits. If new information invalidates the plan, update it visibly and seek the appropriate decision before expanding scope. Validation compares that revision with the original acceptance criteria, including negative cases. A test written by the same agent can share the implementation's misunderstanding, so a reviewer should inspect whether it proves the requirement rather than simply mirrors the code.

In the trace-identifier exercise, planning settles where the identifier comes from and what counts as valid. Execution changes the result contract and consumers. Validation demonstrates the agreed cases and unchanged denial behaviour. Keeping those stages distinct makes a missing contract decision visible before it becomes a compatibility bug.

## Make every action leave reviewable evidence

<figure class="workshop-slide" markdown="1">

![Minimum evidence set: a visible plan, bounded pull request and commit history, required-check run links, durable logs and reports, and review outcomes and approvals. Trace artifacts to a workflow run and commit.](assets/6B-visibleartifacts.png){ loading=lazy decoding=async }

<figcaption>A durable evidence trail lets someone review and investigate the work without access to the original chat.</figcaption>
</figure>

Add an **Evidence** section to the pull request that links the accepted plan, tested commit, required check runs, relevant reports, and review decisions. Record what each check establishes and what remains untested. A summary such as "all tests passed" is weaker than an identifiable run with the actual command, outcome, and revision.

Tie each artifact to a workflow run and commit so evidence from an earlier revision cannot silently justify a later change. New commits may require checks and approvals to be refreshed according to repository rules. Configure suitable retention and access controls: a report that expires before an incident investigation, or exposes sensitive payloads, is not a useful audit strategy.

Durable evidence does not mean retaining every prompt or raw tool response. Prefer redacted outcomes, identifiers, and decision records. Failed and cancelled runs also matter because they explain why an iteration stopped or why someone chose a different approach. The [reliability chapter](reliability.md#make-workflow-handoffs-event-aware) extends this evidence trail across automated handoffs.

!!! example "Try with GitHub Copilot"
    Ask: "Plan a change to include a non-empty trace identifier in the execution result. Identify the acceptance tests and affected consumers first. Implement only that change, then explain the diff against the criteria."

## Checkpoint

Prepare a pull request description linking the issue, the intended behaviour, test evidence, residual risk, and rollback plan. A reviewer should not need access to your private chat to understand the change.
