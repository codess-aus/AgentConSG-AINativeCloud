# Workshop contribution guidance

This repository hosts Building the AI Native Cloud for AgentCon Singapore 2026.
Use Python for programming examples and keep the offline exercise standard-library-only.
Explain intent, constraints, and acceptance criteria before broad changes.

The triage example is a deterministic teaching harness, not an LLM integration.
Preserve read-only capabilities, trusted service scope, explicit errors, and tool budgets.
Never add secrets, arbitrary shell execution, cloud mutation, or model-controlled approval.
Instructions and prompts guide behaviour; Python policy and service permissions enforce it.

Keep changes reviewable and add tests for normal, boundary, missing, and denied inputs.
Run `python -m unittest discover -s tests -v`, `python -m mkdocs build --strict`,
and `python scripts/check_site.py` before proposing a change.
Keep slides in assets, page text in docs, and all slide concepts available as accessible text.
Use descriptive links, meaningful hero alt text, and keyboard-accessible navigation.
