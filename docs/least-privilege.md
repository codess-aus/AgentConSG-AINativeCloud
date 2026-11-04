---
title: Least privilege
hero: assets/8-leastprivilege.png
hero_alt: "Least privilege, by design. Protect data and keep decisions accountable. Low-impact suggestions need lighter review; high-impact actions need explicit approval. Oversight needs information, authority, and time to intervene. Lanterns behind a patterned architectural screen."
---

# 08 · Least privilege, by design

**Least privilege. Protect data. Keep decisions accountable.**

A read-only assistant and an infrastructure operator should not share credentials. Scope access by identity, environment, tenant, service, and operation, then enforce that scope at the resource as well as in your harness.

## Reject out-of-scope targets

The caller supplies the trusted service scope. A model's choice of service cannot expand it.

```python
from examples.cloud_triage import Plan, ToolBudget, execute

budget = ToolBudget(max_calls=1)
plan = Plan(service="payments", action="read_metrics", reason="Inspect the service.")

try:
    execute(plan, allowed_services={"checkout"}, budget=budget)
except PermissionError as error:
    print(f"Access denied explicitly: {error}")
else:
    raise AssertionError("Cross-service access must be denied")

assert budget.used == 0
```

Denied work does not reach the tool. A production application should still count denied attempts for abuse detection using a separate request-rate limit, and emit a redacted audit event.

## Protect context and credentials

Use managed identity or short-lived credentials where available. Retrieve secrets from an approved secret store, never from committed examples or prompts. Minimise telemetry before providing it to a model, and verify your organisation's Copilot and model-provider data policies.

Treat issue comments, runbooks, repository content, and MCP results as potentially untrusted inputs. Instructions embedded in those sources must not modify trusted authorisation decisions. Tool descriptions alone do not prevent prompt injection.

## Make oversight meaningful

For higher-impact capabilities, require an authenticated approval tied to the action, target, parameters, and expiry. Display the evidence and blast radius to the reviewer. Protect deployment environments and maintain a revocation and rollback path. The workshop deliberately offers no write capability.

## Enforce the plan-to-action handoff

<figure class="workshop-slide" markdown="1">

![Enforce rather than only instruct: use read-only planning tools, an explicit approval handoff, tool gating, and a plan artifact that can be reviewed before changes begin.](assets/8A-enforce.png){ loading=lazy decoding=async }

<figcaption>Instructions guide behaviour. Tool allowlists, resource permissions, and gates enforce the boundary.</figcaption>
</figure>

"Do not edit files yet" is useful guidance, but it does not remove a write tool. For a planning-only role, expose read-only capabilities and no mutation credentials. After an authorised person accepts a plan, make the transition to implementation an explicit handoff with the accepted scope and permitted targets.

Approval should identify the exact action or plan revision and its limits. If the target, parameters, or scope changes, require a new decision rather than reusing a broad statement of consent. The executing runtime must still enforce permissions independently of the plan text. A field claiming approval cannot create authority.

Some interfaces offer a plan mode or pause before execution. Verify the guarantees of the specific runtime rather than assuming the label means tools are disabled. The same applies to orchestrators and subagents: a read-only planner must not gain write access indirectly through delegation. These are design patterns for a future integration; the offline sample continues to deny every write action.

## Use pull requests as control points

<figure class="workshop-slide" markdown="1">

![Pull requests as control points: create a branch and proposed plan, obtain review, run required checks, and merge only after approvals and checks pass. Route sensitive paths to appropriate code owners.](assets/8B-gates.png){ loading=lazy decoding=async }

<figcaption>A pull request becomes an enforcement point only when repository rules make its checks and reviews mandatory.</figcaption>
</figure>

A pull request template can ask for intent, scope, evidence, and rollback information. It cannot itself prevent a merge. Configure branch protection or rulesets to require the relevant checks and approvals, restrict bypass privileges, and prevent an agent from writing directly to the protected branch. Use protected environments for deployment decisions that should remain separate from merging code.

CODEOWNERS routes review to people responsible for sensitive paths, but required code-owner approval must also be enabled in the applicable repository rules. The slide's team names are illustrative, not real teams. When writing a real file, remember that the **last matching pattern wins**: place a broad fallback before more-specific workflow, infrastructure, or security paths. Copying the slide's final `*` fallback literally would override those earlier assignments.

Plan review and merge review answer different questions. The first accepts an approach before impact; the second checks what actually changed and whether current evidence supports it. Configure review freshness for new commits according to risk, and prevent the executing identity from approving its own work. An agent may assemble evidence, but it should not be able to remove the gate that judges it.

!!! example "Try with GitHub Copilot"
    Ask: "Map the trust boundaries of this triage design. Explain where identity and service scope come from, what must never enter a prompt, and why text claiming approval cannot authorise an action. Do not add a write tool."

## Checkpoint

Show that an unauthorised service and an unrecognised action are both denied. Name the identity that would call a real telemetry API and the precise read permissions it would need.
