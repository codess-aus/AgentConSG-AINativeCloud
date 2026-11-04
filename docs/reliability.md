---
title: Reliability and evaluation
hero: assets/7-reliability.png
hero_alt: "Reliability is measured, not assumed. Expect variation: same input, different outputs. Measure behaviour across representative and hard cases. Design for failure when context or tools are missing. Evaluation continues after release. A Singapore river bridge in changing light."
---

# 07 · Reliability is measured, not assumed

**Expect variation. Measure behaviour. Design for failure.**

Unit tests validate deterministic code. Evaluations assess whether an AI system behaves acceptably across a defined distribution of cases. You need both. Passing a small fixture suite does not establish production reliability.

## Define a release gate before running the evaluation

Include healthy services, degraded services, missing context, invalid rates, unauthorised targets, malicious tool text, and unavailable dependencies. Separate safety invariants, such as no write capability, from quality metrics such as useful recommendations.

```python
from examples.cloud_triage import Incident, propose

cases = [
    (Incident("checkout", 0.01), "summarise"),
    (Incident("checkout", 0.05), "read_metrics"),
    (Incident("checkout", 0.12), "read_metrics"),
    (Incident("checkout", None), "escalate"),
]

passed = sum(propose(incident).action == expected for incident, expected in cases)
score = passed / len(cases)
print(f"Fixture pass rate: {passed}/{len(cases)} ({score:.0%})")
assert score == 1.0, "Every deterministic workshop fixture must pass"
```

The exact 5% boundary is included because a test only below and above the threshold can miss an off-by-one comparison. These four fixtures check the teaching policy, not a live model.

## Evaluate a real model separately

Use a versioned, sanitised dataset with expected outcomes or a human-reviewed rubric. Repeat representative inputs to observe variation; record model, prompt, context, policy, latency, and cost. Keep a holdout set so tuning does not merely memorise your evaluation examples.

Measure unsafe-action attempts, unsupported claims, appropriate escalations, and useful triage outcomes. Report denominators and case categories, not a single attractive percentage. A blocked unsafe proposal is a harness success but still a model behaviour worth investigating.

## Design autonomy around consequence

<figure class="workshop-slide" markdown="1">

![Risk-based autonomy: infrastructure and workflow changes need stricter rules and expert reviews; application and dependency changes need pull requests and checks; low-risk documentation may qualify for automerge only after configured requirements pass.](assets/7A-Risk.png){ loading=lazy decoding=async }

<figcaption>Risk determines the gate. An agent that can bypass required checks defeats the surrounding reliability design.</figcaption>
</figure>

Use the slide's categories as a starting point, not a universal classification. Infrastructure and workflow edits can alter the controls that protect every later change. Application and dependency changes can affect runtime behaviour or supply-chain exposure. Documentation and formatting often have less impact, but an operational runbook or executable documentation example can still be consequential.

For each task, consider blast radius, reversibility, data exposure, and the strength of available checks. A low-risk task might qualify for automerge only when repository policy allows it and every configured requirement passes. Higher-risk work needs relevant owners and stronger evidence; passing a familiar unit suite does not justify increasing an agent's authority.

Test the control path as well as the proposed feature. Can the agent merge its own change without the intended approval? Can it edit the workflow that declares success, or bypass a ruleset? These are architecture and repository-policy questions, not qualities that a better prompt can guarantee. The [least-privilege chapter](least-privilege.md#use-pull-requests-as-control-points) explains how review requirements become actual gates.

## Make workflow handoffs event-aware

<figure class="workshop-slide" markdown="1">

![Reliable workflows use structured step and job outputs, GitHub event contexts, safe triggers, and job-level conditions so pull-request-only work runs only for a pull request event.](assets/7B-ReliableWorkflows.png){ loading=lazy decoding=async }

<figcaption>Plans and signals should be structured outputs with explicit event assumptions, not text that downstream jobs guess how to interpret.</figcaption>
</figure>

A workflow triggered by a pull request, schedule, or manual dispatch does not always have the same context. A PR comment job, for example, needs an actual PR number. Gate PR-only work with an event-aware job condition such as `github.event_name == 'pull_request'`; provide a separate intentional path for manual validation instead of assuming missing PR fields exist.

Pass machine-readable values through step outputs and declared job outputs. Have consumers depend on the producing job, validate required values, and distinguish success from skipped, failed, or cancelled work. A missing output is not an approval signal. Keep user-controlled issue titles, branch names, and model-generated text out of executable shell expressions.

Treat trigger choice as a trust decision. Do not use a privileged event to execute untrusted pull request code with secrets or a write token merely to make a handoff easier. Reusable or chained workflows also need a clear account of whose code is running and which permissions it receives.

The slide's JavaScript workflow is an illustration of event gating, not a workflow to install in this Python workshop. Its action version and commands are not dependency recommendations. Check current supported action versions in the [GitHub Actions documentation](https://docs.github.com/en/actions) when authoring a real workflow.

!!! example "Try with GitHub Copilot"
    Ask: "Extend the evaluation plan without changing the policy. Add missing-context, threshold-boundary, invalid-data, and denied-action cases. Distinguish deterministic tests from repeated model evaluations and propose an explicit release gate."

## Checkpoint

Review the four fixture cases above. Identify one behaviour that deterministic tests like these cannot establish, such as a live model's hallucination rate. Define how you would measure it before release and monitor it afterward.
