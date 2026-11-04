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

## Draw the boundary before work starts

<figure class="workshop-slide" markdown="1">

![Draw the boundary: restrict editable directories, treat workflow and infrastructure changes as higher risk, and prefer pull requests over direct default-branch changes. A dependency remediation agent detects, branches, updates, and proposes.](assets/5A-exampleboundaries.png){ loading=lazy decoding=async }

<figcaption>Agents propose; humans and policy accept. Scope the change early to reduce its blast radius.</figcaption>
</figure>

A dependency remediation task illustrates why a useful tool still needs a narrow job. The agent can inspect an alert, create a branch, update the affected dependency and lockfile, and propose a pull request with verification evidence. That task does not also authorise changes to deployment credentials, branch rules, or the workflow that judges its own work.

Directory boundaries make the intended scope reviewable, but a directory name is not an enforcement mechanism. Combine change inspection and ownership review with runtime and repository controls. If the fix genuinely requires a workflow or infrastructure change, stop and request a separate scope decision from the responsible owner rather than slipping it into an application patch.

## Write a task contract

<figure class="workshop-slide" markdown="1">

![A task contract defines inputs, outputs, and success criteria: issue context and scope, a plan and pull request with evidence, passing checks, an intent-matching diff, and a rollback or escalation path.](assets/5B-taskcontracts.png){ loading=lazy decoding=async }

<figcaption>A task contract makes completion inspectable. Passing CI is necessary, but it does not prove that the change meets its intent.</figcaption>
</figure>

For a proposed trace-identifier improvement to this repository's triage example, the contract could be:

| Contract element | Concrete agreement |
|---|---|
| Inputs | The issue, `examples/cloud_triage.py`, existing tests, and consumers of execution results. No credentials or raw customer incidents. |
| Scope | The result contract and focused tests. Preserve read-only actions, trusted service scope, and call limits; exclude deployment and workflow changes. |
| Outputs | A plan, a bounded pull request, and evidence linked to the tested revision. |
| Success | Results contain the agreed identifier; existing consumers remain compatible; missing, invalid, and denied cases preserve their specified behaviour. |
| Stop or escalate | Pause if the identifier's source or format is ambiguous, or if implementation requires a broader permission or schema change. |

This is a proposal for a future exercise, not a feature already implemented in the sample. Settle the identifier contract before asking an agent to code it. A useful contract is precise enough that a reviewer can reject a technically passing change that solves a different problem.

## Govern tools, MCP, and secrets separately

<figure class="workshop-slide" markdown="1">

![Govern tools, MCP, and secrets: allowlist capabilities and delegation, specify transport and authentication, expose a narrow tool namespace, and inject scoped secrets only at runtime into components that need them.](assets/5C-tools.png){ loading=lazy decoding=async }

<figcaption>Every integration widens the potential blast radius. An agent runtime has its own credential boundary.</figcaption>
</figure>

Maintain an inventory of allowed tools, their targets, who owns them, and whether delegation can expose additional capabilities. Hiding an agent from a menu is not authorisation. A subagent should not become a route around the parent task's boundaries; its tools and credentials need their own enforceable scope.

For an MCP integration, review the server's transport, authentication, exposed tool subset, and output handling. A local process and a remote endpoint have different deployment and credential concerns, even if they expose similarly named tools. Avoid wildcard access when the task needs only one read operation, and continue treating returned text as untrusted data.

Inject secrets at runtime through the supported secret boundary, only into the component that needs them. Never embed credentials in instructions, prompts, or committed configuration. Do not assume the coding agent inherits GitHub Actions secrets, or that a workflow's permissions configure the agent's MCP connection. Verify each runtime independently and document how to revoke access.

!!! example "Try with GitHub Copilot"
    Ask: "Trace every route into execute. Check that authorisation and budget enforcement happen before tool access. Draft tests for an unknown action, a different service, an exhausted budget, and instruction-like text in a reason."

## Checkpoint

Demonstrate that changing `Plan.reason` cannot permit a forbidden action. Document which layer owns credentials, policy, cancellation, and audit records before connecting a real cloud tool.
