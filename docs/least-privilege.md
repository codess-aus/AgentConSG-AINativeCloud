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

!!! example "Try with GitHub Copilot"
    Ask: "Map the trust boundaries of this triage design. Explain where identity and service scope come from, what must never enter a prompt, and why text claiming approval cannot authorise an action. Do not add a write tool."

## Checkpoint

Show that an unauthorised service and an unrecognised action are both denied. Name the identity that would call a real telemetry API and the precise read permissions it would need.
