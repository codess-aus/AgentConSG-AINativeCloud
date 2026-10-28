---
title: Human judgment
hero: assets/3-Judgement.png
hero_alt: "Judgment gives AI its direction. Direction: choose worthwhile problems. Context: bring what the system cannot see. Judgment: know when plausible is not good enough. Accountability: own consequential decisions. Speed is not correctness; fluency is not understanding."
---

# 03 · Judgment gives AI its direction

People contribute **direction, context, judgment, and accountability**. Human oversight is more than approving a polished response at the end.

## Put attention where it changes the outcome

The service owner defines acceptable risk. A domain expert identifies missing assumptions. A reviewer challenges the implementation and evidence. An operator owns escalation after release. These responsibilities may belong to the same person in a small team, but they must not disappear behind "the agent decided."

For triage, a plausible recommendation to restart a service may make an outage worse if a migration is running. The model may not have that context. The first release therefore cannot perform restarts, even when a plan claims to have approval.

```python
from examples.cloud_triage import Plan, authorise

proposal = Plan(
    service="checkout",
    action="restart_service",
    reason="A generated suggestion is not authority.",
)

try:
    authorise(proposal, allowed_services={"checkout"})
except PermissionError as error:
    print(f"Human review required; action blocked: {error}")
else:
    raise AssertionError("A restart must never be permitted in this workshop")
```

This is a blocked action, not an approval implementation. A real approval workflow must authenticate the approver, bind approval to an exact action and target, expire it, and record its use. A model-generated `approved=True` field would prove none of those things.

## Review decisions, not just syntax

Ask what evidence supports the recommendation, which assumptions are still unverified, what happens if the recommendation is wrong, and who can intervene. Tests help you assess a change; they do not choose the organisation's risk tolerance.

!!! example "Try with GitHub Copilot"
    Ask: "Review this proposal as an on-call engineer. List missing evidence, identify any irreversible effects, and suggest a read-only alternative. Do not grant permissions or implement the restart."

## Checkpoint

Write an escalation note with the affected service, known evidence, uncertainty, and responsible owner. Another person should be able to decide what to do without having to reconstruct your Copilot conversation.
