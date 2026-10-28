---
title: Build with intent
hero: assets/10-people.png
hero_alt: "AI expands capability. People provide direction and accountability. When you add AI, have you designed how people guide, evaluate, and take responsibility for it? Thank you. Singapore river and bridges at dusk."
---

# 10 · Build with intent

**AI expands capability. People provide direction and accountability.**

The point is not to place AI everywhere. It is to give AI a clear role, useful context, bounded capabilities, and a way to be evaluated and improved.

## Make the release decision explicit

Your first triage release should remain read-only, scoped to approved services, observable, and easy to disable. A named owner reviews the acceptance criteria and evidence. Document unresolved limitations rather than letting a successful demo stand in for a production decision.

```python
# This is a release checklist summary, not an automated approval system.
evidence = {
    "scope_reviewed": True,
    "tests_passed": True,
    "evaluation_reviewed": True,
    "read_only_identity_verified": False,
    "rollback_rehearsed": False,
    "owner_signed_off": False,
}

ready = all(evidence.values())
print("Ready for owner decision" if ready else "Not ready for release")
assert not ready
```

The values are illustrative. In production, collect evidence from trusted CI checks, evaluation reports, infrastructure policy, and authenticated reviewers. Do not let a model fill a checklist with `True` values and call that approval.

## Close the feedback loop

Observe latency, tool failures, denied actions, escalations, and usefulness after release. Tie traces to prompt, policy, and model versions without retaining unnecessary sensitive payloads. Feed reviewed incidents back into your test and evaluation sets.

Release model or prompt changes through the same review process as code. Use a staged rollout where appropriate, define stop conditions, and test the rollback path. A system that cannot be safely stopped is not made safe by a good average score.

!!! example "Try with GitHub Copilot"
    Ask: "Draft a release review for the workshop triage assistant. Separate evidence we have from assumptions we have not tested. Include an owner, operational metrics, stop conditions, and a rollback plan. Do not claim the fixture suite proves model quality."

## Take this back to your team

Choose one workflow, write its intent and boundaries, make the result inspectable, and measure whether it helps. Expand authority only when the evidence and operational controls justify it.

**When you add AI, have you designed how people guide, evaluate, and take responsibility for it?**

Continue to [resources](resources.md) for official documentation and learning paths.
