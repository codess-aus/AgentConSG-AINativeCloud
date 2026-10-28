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

!!! example "Try with GitHub Copilot"
    Ask: "Review the repository instructions against the actual code and tests. Suggest one reusable instruction that prevents a concrete recurring mistake, and one task-specific instruction that belongs in an issue instead. Do not introduce new tooling."

## Checkpoint

Have a teammate reproduce the example and explain its boundaries using only the repository. Record one improvement to the shared workflow, its owner, and the evidence you will use to judge whether it helps.
