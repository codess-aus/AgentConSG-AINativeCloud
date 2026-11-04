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

## Capability needs structure

<figure class="workshop-slide" markdown="1">

![Capability is not reliability: without architecture, agents can act before intent is agreed, obscure the diff, and skip validation. Branching, editing, and opening pull requests need structure.](assets/3A-Structure.png){ loading=lazy decoding=async }

<figcaption>Power needs structure: making a change is not the same as demonstrating that it is safe.</figcaption>
</figure>

An agent that can create a branch, modify files, open a pull request, and iterate on feedback has useful delivery capabilities. None of those operations establishes that it understood the problem. Without agreed intent, it can optimise for the wrong outcome; without a bounded diff, it can make review harder; without validation, it can produce a convincing explanation unsupported by evidence.

Put human judgment at three distinct decision points. Before implementation, agree on the problem, permitted scope, and success criteria. During review, compare the actual change with that agreement and challenge surprising files or assumptions. Before release, decide whether the evidence is sufficient for the consequences of being wrong. These decisions need not all belong to one person.

For example, a request to improve triage escalation should not become permission to rewrite service authorisation. If an agent discovers that a broader change seems necessary, it should explain the dependency and pause for a scope decision. A reviewer should be able to reject that expansion without having to discard the useful, bounded part of the proposal.

**A useful review question:** can someone explain why this change exists, what it is allowed to affect, and how its result was checked without trusting the agent's own summary? If not, improve the task and evidence before adding more autonomy. The [next chapter](context.md#map-the-work-before-choosing-the-agent) turns that structure into an explicit lifecycle map.

!!! example "Try with GitHub Copilot"
    Ask: "Review this proposal as an on-call engineer. List missing evidence, identify any irreversible effects, and suggest a read-only alternative. Do not grant permissions or implement the restart."

## Checkpoint

Write an escalation note with the affected service, known evidence, uncertainty, and responsible owner. Another person should be able to decide what to do without having to reconstruct your Copilot conversation.
