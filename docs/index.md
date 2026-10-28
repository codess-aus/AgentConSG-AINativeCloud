---
title: Workshop home
hero: assets/0-AgentConSG.png
hero_alt: "AgentCon Singapore, part of the AgentCon World Tour by the Global AI Community. AI Agents Developer Conference. agentcon.city/singapore."
---

# Building the AI Native Cloud

<p class="workshop-eyebrow">AgentCon Singapore 2026 · Michelle Sandford</p>

<p class="workshop-lead">AI-native is a way of engineering, not a feature. Build cloud systems where AI has useful context, bounded capabilities, and evidence behind every consequential decision.</p>

[Start the workshop](build-the-cloud.md){ .md-button .md-button--primary }
[Explore the chapters](#choose-your-chapter){ .md-button }

## Welcome

This technical companion turns the ten ideas from **Building the AI Native Cloud** into hands-on engineering practice. Follow the talk in order or jump straight to a chapter. Each slide is available full size; the text below it explains the same ideas without requiring you to read the image.

The running example is a **read-only cloud incident-triage assistant**. GitHub Copilot helps you specify, implement, test, and review it. The Python harness, not a model's confidence, decides which operations are permitted. No cloud account, paid API, credentials, or live model is needed for the exercises.

## Get ready

Use Python **3.15** for the workshop and a current VS Code installation with GitHub Copilot access for the prompting exercises. The standard-library example also works with Python 3.12 or later. Copilot features and availability depend on your plan, editor, and organisation policies.

Clone this repository using its **Code** menu and open the folder in VS Code. In the integrated terminal, run `python -m examples.cloud_triage`, then `python -m unittest discover -s tests -v`. On Windows, use `py` if `python` is not available. The [resources page](resources.md) links to the source repository and setup documentation.

!!! tip "Choose your pace"
    Follow the ten chapters alongside the 25-minute talk, or allow 60 to 90 minutes to complete the exercises. Each chapter includes a Copilot prompt and an observable checkpoint. You can read all the content without a Copilot subscription.

## The Agentic SDLC

**Specify → plan → implement → verify → review → release → observe → learn.**

AI can contribute at every stage, but people own the intent, boundaries, and release decision. Treat repository instructions as guidance, tests as evidence, and permissions as enforcement. A prompt alone is never a security boundary.

## Choose your chapter

<div class="workshop-grid">
  <a class="workshop-card" href="#welcome">
    <img src="assets/0-AgentConSG.png" alt="" width="916" height="516" loading="lazy">
    <strong>00 · Welcome to AgentCon Singapore</strong>
    <span>Workshop setup, learning outcomes, and the Agentic SDLC.</span>
  </a>
  <a class="workshop-card" href="build-the-cloud/">
    <img src="assets/1-BuildTheCloud.png" alt="" width="916" height="516" loading="lazy">
    <strong>01 · Build the AI-native cloud</strong>
    <span>Start with engineering intent, not a model integration.</span>
  </a>
  <a class="workshop-card" href="the-shift/">
    <img src="assets/2-theShift.png" alt="" width="916" height="516" loading="lazy">
    <strong>02 · From AI-assisted to AI-native</strong>
    <span>Distinguish an assistant, a workflow, and a production system.</span>
  </a>
  <a class="workshop-card" href="human-judgment/">
    <img src="assets/3-Judgement.png" alt="" width="916" height="516" loading="lazy">
    <strong>03 · Human judgment</strong>
    <span>Make direction, context, judgment, and accountability explicit.</span>
  </a>
  <a class="workshop-card" href="context/">
    <img src="assets/4-context.png" alt="" width="916" height="516" loading="lazy">
    <strong>04 · Context and specifications</strong>
    <span>Give Copilot the right context and measurable acceptance criteria.</span>
  </a>
  <a class="workshop-card" href="boundaries/">
    <img src="assets/5-boundaries.png" alt="" width="916" height="516" loading="lazy">
    <strong>05 · Tools, agents, and boundaries</strong>
    <span>Constrain capabilities in the harness, not just in the prompt.</span>
  </a>
  <a class="workshop-card" href="engineering-loop/">
    <img src="assets/6-inspectable.png" alt="" width="916" height="516" loading="lazy">
    <strong>06 · Inspectable engineering</strong>
    <span>Keep specifications, patches, tests, and review connected.</span>
  </a>
  <a class="workshop-card" href="reliability/">
    <img src="assets/7-reliability.png" alt="" width="916" height="516" loading="lazy">
    <strong>07 · Reliability and evaluation</strong>
    <span>Measure representative behaviour and safe failure.</span>
  </a>
  <a class="workshop-card" href="least-privilege/">
    <img src="assets/8-leastprivilege.png" alt="" width="916" height="516" loading="lazy">
    <strong>08 · Least privilege by design</strong>
    <span>Protect data and require meaningful approval for higher risk.</span>
  </a>
  <a class="workshop-card" href="team-capability/">
    <img src="assets/9-repeatable.png" alt="" width="916" height="516" loading="lazy">
    <strong>09 · Repeatable team practice</strong>
    <span>Turn individual experiments into shared engineering capability.</span>
  </a>
  <a class="workshop-card" href="build-with-intent/">
    <img src="assets/10-people.png" alt="" width="916" height="516" loading="lazy">
    <strong>10 · Build with intent</strong>
    <span>Make an evidence-based release decision and own what follows.</span>
  </a>
  <a class="workshop-card" href="resources/">
    <strong>Continue learning · Resources</strong>
    <span>Official Copilot documentation, learning paths, and workshop references.</span>
  </a>
</div>
