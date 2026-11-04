---
title: Resources
hero: assets/0-AgentConSG.png
hero_alt: "AgentCon Singapore, part of the AgentCon World Tour by the Global AI Community. AI Agents Developer Conference. agentcon.city/singapore."
---

# Resources

Keep learning after **Building the AI Native Cloud** at AgentCon Singapore 2026. Start with the learning paths supplied for this session, then use the reference documentation when implementing your own workflow.

## Workshop code samples

- [Code samples](https://github.com/codess-aus/AgentConSG-AINativeCloud/tree/main/examples): the standard-library Python triage example used in every chapter. Save both files into a folder named `examples` and run `python -m examples.cloud_triage`.

## Session learning paths

- [Awesome Copilot Learning Hub](https://awesome-copilot.github.com/learning-hub/): community-curated guidance and practical patterns.
- [GitHub Copilot Fundamentals](https://learn.microsoft.com/en-us/training/paths/copilot/): build a foundation for responsible, effective Copilot use.
- [GitHub Agentic Developer Learning Path](https://learn.microsoft.com/en-us/training/paths/gh-developing-agentic-systems-1): explore agentic development practices.

## GitHub Copilot and the Agentic SDLC

- [GitHub Copilot documentation](https://docs.github.com/en/copilot): editor setup, features, plans, and administration.
- [Repository custom instructions](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot): provide shared, version-controlled development guidance.
- [Copilot coding agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent): understand delegated issue-to-pull-request workflows.
- [Responsible use of GitHub Copilot](https://docs.github.com/en/copilot/responsible-use): understand limitations and human review responsibilities.
- [GitHub Actions documentation](https://docs.github.com/en/actions): automate tests, builds, and release gates.

## Tools, evaluation, and secure systems

- [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro): understand the protocol, then design your own permission boundaries.
- [Python unittest](https://docs.python.org/3/library/unittest.html): run and extend the workshop's deterministic test suite.
- [OWASP Top 10 for LLM applications](https://genai.owasp.org/llm-top-10/): explore prompt injection, excessive agency, and related risks.
- [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/): connect AI workflows with reliability, security, and operational excellence.

The workshop example is deliberately offline and read-only. Before using a real model or cloud API, add authenticated identity, scoped credentials, schema validation at the model boundary, deadlines, redacted observability, and a representative evaluation dataset.
