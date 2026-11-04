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

## Turn the principles into one sprint of change

<figure class="workshop-slide" markdown="1">

![Six changes to take back to a repository: scope agents to implementation and validation, add task contracts, plan first for sensitive work, require pull request gates and owners, use event-aware jobs, and add runtime controls, evidence, and least privilege.](assets/10A-summary.png){ loading=lazy decoding=async }

<figcaption>Start with one bounded workflow and make its controls demonstrable before expanding autonomy.</figcaption>
</figure>

These six changes turn the workshop into a practical adoption plan. They are recommendations to apply and verify in your own repository, not claims that this sample has configured production rules, agent hooks, or deployment approvals.

| Change | First concrete step | Evidence that it works |
|---|---|---|
| Scope agent participation | Choose an implementation-and-validation task with no production authority. | A lifecycle map names allowed operations, handoffs, and a responsible owner. |
| Add a task contract | Record inputs, outputs, boundaries, success criteria, and stop conditions in the issue. | A teammate can judge completion without reading the original chat. |
| Plan first for sensitive work | Require an accepted plan before workflow, infrastructure, authentication, or production changes. | The approved scope is identifiable, and a scope change triggers a new decision. |
| Make PR gates real | Add a template and appropriate owners, then configure required checks and reviews. | A controlled test shows the executing identity cannot bypass the required decision. |
| Make jobs event-aware | Separate PR-specific work from manual, scheduled, or push-triggered paths. | Each supported trigger runs the intended jobs without assuming absent context. |
| Operate with evidence and least privilege | Link runs and reports, scope credentials, and add supported runtime controls and bounded recovery. | Denied access, failure escalation, and the disable or rollback path have been exercised. |

Start with the task contract and lifecycle map, then assign an owner to each control the chosen workflow needs. Do not enable broader capabilities while the corresponding boundary is still only a proposed instruction. Use the [boundaries](boundaries.md#write-a-task-contract), [review evidence](engineering-loop.md#make-every-action-leave-reviewable-evidence), and [recovery](team-capability.md#assume-failure-and-rehearse-recovery) sections as working references.

At the end of the sprint, review useful accepted outcomes alongside review effort, failures, and escalations. Keep the workflow narrow if evidence is weak. Expanding autonomy should be a deliberate, reversible decision supported by observed behaviour, not a reward for an impressive demonstration.

Continue to [resources](resources.md) for official documentation and learning paths.
