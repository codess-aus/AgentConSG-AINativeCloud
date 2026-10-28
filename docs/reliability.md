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

!!! example "Try with GitHub Copilot"
    Ask: "Extend the evaluation plan without changing the policy. Add missing-context, threshold-boundary, invalid-data, and denied-action cases. Distinguish deterministic tests from repeated model evaluations and propose an explicit release gate."

## Checkpoint

Run `python -m unittest discover -s tests -v`. Identify one behaviour that these tests cannot establish, such as a live model's hallucination rate. Define how you would measure it before release and monitor it afterward.
