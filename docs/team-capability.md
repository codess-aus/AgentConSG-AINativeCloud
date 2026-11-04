---
title: Repeatable team practice
hero: assets/9-repeatable.png
hero_alt: "Make good decisions easy to repeat. Shared patterns lead to team learning and continuous improvement. Reuse specifications, context guidelines, evaluation approaches, approved tools, and clear review expectations. The strongest capability is the ability to adapt. A group collaborating in a Singapore mural street."
---

# 09 · Make good decisions easy to repeat

**Shared patterns → team learning → continuous improvement.**

An individual's prompt history is not a team capability. Capture reusable intent, context, tests, and review standards in version control so that another engineer can reproduce and improve the work.

## Create a small paved road

Use repository instructions for Python conventions and safety expectations. Use issues for task-specific acceptance criteria and pull requests for review evidence. Reusable prompt files can describe common workflows, but they should not duplicate rapidly changing policy or claim to enforce permissions.

This repository includes `.github/copilot-instructions.md`. It directs Copilot toward the sample's actual contracts, standard-library tests, and explicit failure behaviour. Contributors can review those instructions like any other change.

## Measure the whole delivery loop

Time to first draft is only one part of delivery. Track review effort, rework, escaped defects, operational outcomes, and the proportion of tasks that reach a useful accepted result. Compare similar work and discuss confounding factors rather than attributing every improvement to AI.

```python
from statistics import median

# Illustrative minutes from issue readiness to a reviewed, accepted change.
baseline = [90, 120, 110, 100, 130]
assisted = [80, 95, 140, 85, 100]

print(f"Baseline median: {median(baseline)} minutes")
print(f"Assisted median: {median(assisted)} minutes")
assert len(baseline) == len(assisted)
```

These synthetic values teach measurement, not a claim about Copilot productivity. A faster median can coexist with more defects or longer tail latency; look at the distribution and quality outcomes together.

## Assume failure and rehearse recovery

<figure class="workshop-slide" markdown="1">

![Assume failure and design recovery: independent runtime hooks, least-privilege workflow permissions, bounded retries, rollback notes, and escalation with what failed, what was tried, evidence, and a proposed next step.](assets/9A-assumefailure.png){ loading=lazy decoding=async }

<figcaption>Recovery is a shared operating practice, not an instruction to keep retrying until a check turns green.</figcaption>
</figure>

Agree on a bounded iteration policy before handing work to an agent. The slide suggests one revision after an ordinary check failure, followed by human escalation if the next attempt also fails. This is a starting point for a team policy, not behaviour implemented by the workshop's `ToolBudget`. Permission denials, suspected data exposure, and unexpected mutation should stop immediately rather than consume an automatic retry.

A useful escalation names what failed, what was attempted, the affected commit and workflow run, relevant redacted evidence, and the next decision needed. Do not loosen a test, expand permissions, or remove a required check to make the failure disappear. A fresh run should be tied to a reasoned correction, not just hope that nondeterminism produces a better answer.

Runtime hooks can add pre-tool checks independently of a model's reasoning, but their configuration format and guarantees depend on the host. The slide's hook JSON is conceptual, not an installable configuration for this repository. A command-name check alone is not a complete mutation boundary: aliases, alternative tools, and indirect operations can bypass simplistic matching. Keep trusted tool policy and resource permissions as the underlying controls.

Likewise, GitHub Actions token permissions are separate from an agent runtime's permissions. Grant write access only to jobs that need it; a validation job should not inherit pull-request write access merely because a different job posts a comment. Test that denied operations fail explicitly without exposing secrets.

Make recovery repeatable with a short exercise: simulate an unavailable telemetry source, capture the failure and escalation, and have a teammate resume using only the recorded evidence. Before any future write-capable integration, identify who can disable it, revoke its credentials, and recover from a partial action. Add the reviewed failure case to the shared test or evaluation set so the next team benefits from the incident.

!!! example "Try with GitHub Copilot"
    Ask: "Review the repository instructions against the actual code and tests. Suggest one reusable instruction that prevents a concrete recurring mistake, and one task-specific instruction that belongs in an issue instead. Do not introduce new tooling."

## Checkpoint

Have a teammate reproduce the example and explain its boundaries using only the repository. Record one improvement to the shared workflow, its owner, and the evidence you will use to judge whether it helps.
