# AgentConSG Building the AI-Native Cloud

### 1. Building the AI-Native Cloud | 0:00–2:00
**On slide:** Title and one-line premise: *AI-native is a way of engineering, not a feature.*

**Script:**  
Good morning, and thank you for having me here in Singapore.

When we talk about AI in the cloud, it’s tempting to focus on the visible part: the model, the prompt, or the feature someone can try in a product demo. But the harder question is what it takes to build software around AI that people can rely on.

That means thinking beyond a clever response. We have to consider the information the system uses, how it chooses its actions, how we evaluate its behaviour, and what happens when it is uncertain or wrong.

I want to talk about that shift: from adding AI to an application, to building software and engineering practices that are AI-native. And I want to emphasize one principle throughout: AI can extend what a team can do, but human judgment is what gives that capability direction and accountability.

---

### 2. From AI-assisted to AI-native | 2:00–4:30
**On slide:** A simple progression: *AI as assistant → AI in the workflow → AI as part of the system.*

**Script:**  
Many of us have already experienced AI-assisted development. We ask for an explanation, generate a test, or get help completing a function. These are valuable, but they are often isolated interactions. The developer still holds the full task and uses AI for a small part of it.

AI-native development asks us to think more broadly. Where does AI participate in the lifecycle? What context does it need? Which tools can it use? How do we check its work? And how does the system behave when the model gives an incomplete or unexpected result?

This is not a claim that every application needs an agent, or that every task should be handed to a model. It is an invitation to design deliberately. Sometimes the right choice is conventional code. Sometimes AI adds useful flexibility. The engineering work is knowing which is appropriate, then designing the boundaries around it.

---

### 3. The human contribution | 4:30–7:00
**On slide:** Human strengths around an AI system: *direction, context, judgment, accountability.*

**Script:**  
The phrase “human in the loop” can sound like a final approval button. But people add value much earlier and in more ways than that.

Humans decide what problem is worth solving. We know which constraints matter, which trade-offs are acceptable, and when an answer that sounds plausible is not good enough. We can bring context that is missing from the system, recognize when the situation has changed, and take responsibility for consequential decisions.

AI can help us explore options, summarize information, generate candidate solutions, and reduce repetitive work. But speed is not the same as correctness, and fluency is not the same as understanding.

So the goal is not to keep a person checking every token. It is to put human attention where it has the most leverage: setting intent, shaping context, reviewing important decisions, and improving the system based on what happens in practice.

---

### 4. Context and specifications | 7:00–9:30
**On slide:** *Intent + relevant context + constraints → better AI work.*

**Script:**  
A model can only work with the context it receives. More context is not automatically better. The useful question is whether it has the right information, at the right time, in a form it can use.

That is the idea behind context engineering. It means treating context as an intentional part of the system: what information is available, where it comes from, how it is selected, and what should remain out of scope.

Specifications matter for the same reason. A clear spec gives people and AI a shared target. It can describe the goal, constraints, expected behaviour, and how we will know whether the result is acceptable.

This does not mean trying to predict every detail in advance. It means making important assumptions visible, so they can be questioned and revised. Good context and good specifications do not remove human judgment. They make it more effective by giving both the people and the AI a clearer basis for decisions.

---

### 5. Tools, agents, and boundaries | 9:30–12:00
**On slide:** *Model + context + tools + control flow + human oversight.*

**Script:**  
As AI systems become more capable, they may use tools to retrieve information or take actions. Protocols such as MCP can help connect models with external tools and data sources. But connecting a tool is not the same as designing a safe workflow.

We still need to decide what the system is allowed to access, what it can change, and when it must stop and ask for help. We need clear inputs and outputs, meaningful permissions, and a way to understand what happened.

This is where the surrounding harness matters: the control flow, state, limits, and checks that shape how the model works. A capable model inside a poorly designed harness can still produce a fragile system. A bounded workflow with clear responsibilities can make a system more understandable and easier to improve.

The design question is not simply, “What tools can the AI use?” It is, “What is the smallest useful set of capabilities, and what boundaries keep their use appropriate?”

---

### 6. AI-native development in the daily loop | 12:00–14:30
**On slide:** *Specify → build → test → review → learn.*

**Script:**  
These ideas apply to the way we build software, not only to the AI features inside it. Tools such as GitHub Copilot can help across the development loop: exploring unfamiliar code, drafting implementation options, creating tests, or investigating a defect.

But the developer’s role does not disappear. It becomes more explicit. We need to provide useful context, break work into reviewable steps, check generated changes against the specification, and decide whether the result is maintainable.

A good workflow makes the work inspectable. It preserves familiar engineering safeguards such as version control, tests, code review, and continuous integration. It also makes room for AI to contribute where it is useful.

The goal is not to accept more generated code. It is to improve the quality and flow of engineering work. That requires us to measure the outcome, not just how quickly the first draft appeared.

---

### 7. Reliability and evaluation | 14:30–17:30
**On slide:** *Expect variation. Measure behaviour. Design for failure.*

**Script:**  
Traditional software often gives us predictable behaviour for a given input. AI systems can be probabilistic. The same request may produce different outputs, and an answer can be convincing without being correct.

That changes how we think about reliability. We need to evaluate behaviour across representative cases, including difficult and ambiguous ones. We should test not only whether the system succeeds, but also whether it fails safely: when context is missing, a tool is unavailable, or the model is uncertain.

Evaluation needs to continue after release. Models, prompts, data, and user expectations can change. A set of checks that was useful last month may no longer cover the cases that matter today.

This is an engineering discipline, not a final polish step. Define what quality means. Collect evidence. Use feedback to improve the system. And make sure the people operating it can see enough to investigate and respond when its behaviour is unexpected.

---

### 8. Security, privacy, and governance | 17:30–20:00
**On slide:** *Least privilege. Protect data. Keep decisions accountable.*

**Script:**  
When we connect AI to data and tools, we also create new questions about privacy, security, and governance. What information is sent to a model? What can be retained? Who is allowed to access a capability? How do we prevent a workflow from acting outside its intended scope?

These are not questions to leave until deployment. They affect architecture and context design from the beginning. Use only the data and permissions the task needs. Make sensitive boundaries explicit. Keep consequential actions reviewable, and establish a clear path for escalation.

Governance is most useful when it helps teams make good decisions consistently, rather than adding paperwork after the design is finished. The right controls depend on the risk of the use case. A low-impact suggestion and a high-impact action should not have identical approval requirements.

Human oversight is meaningful when people have the information, authority, and time to intervene.

---

### 9. From individual practice to team capability | 20:00–22:30
**On slide:** *Shared patterns → team learning → continuous improvement.*

**Script:**  
AI-native engineering is not only an individual developer learning a new tool. Teams need shared ways to describe work, provide context, review changes, evaluate behaviour, and respond to failures.

That means building practices people can reuse. It might include specification templates, context guidelines, evaluation approaches, approved tool integrations, or clear review expectations. The purpose is not to standardize every decision. It is to make good decisions easier to repeat and risky assumptions easier to notice.

Teams also need to learn from use. Where is AI saving time? Where does it create extra review work? Which tasks benefit from it, and which are better handled another way? Those answers will vary by team and change as the tools change.

The strongest capability is not dependence on a particular model or product. It is the ability to adapt engineering practice as the technology evolves.

---

### 10. Closing: build with intent | 22:30–25:00
**On slide:** *AI expands capability. People provide direction and accountability.*

**Script:**  
Let me bring this back to the title: building the AI-native cloud.

It is not about putting AI everywhere. It is about building cloud systems and engineering workflows in which AI has a clear role, useful context, bounded capabilities, and ways to be evaluated and improved.

And it is about recognizing what people contribute. We bring intent, domain knowledge, judgment, and accountability. AI can help us move faster and explore more possibilities, but people decide what matters, what is acceptable, and what should happen next.

If you take one question away from this talk, make it this: when you add AI to a system or workflow, have you designed not only what the AI can do, but also how people guide, evaluate, and take responsibility for it?

That is how we move beyond AI-assisted experiments and build systems that are genuinely useful, trustworthy, and ready to evolve. Thank you.

## Image prompts

Use these as **background artwork**, with slide text added separately. Keeping text out of the generated images avoids misspellings and gives you room to adjust the layout.

**Shared visual direction for all slides:**  
*Wide 16:9 watercolor illustration for a polished technology conference presentation. Singapore-inspired urban scene, hand-painted paper texture, layered transparent washes, delicate ink linework, warm tropical light, restrained contemporary palette of jade, teal, coral, saffron, indigo, and cream. Atmospheric and sophisticated, with generous uncluttered negative space for slide text. No text, lettering, logos, UI, or watermark. Avoid photorealism and overly busy detail.*

1. **Opening:** Peranakan shophouses in Singapore, ornate pastel façades, five-foot way, tropical greenery, morning light. View down the street with open sky and pale wash on the left for title placement.
2. **AI-assisted to AI-native:** Haji Lane-inspired murals and narrow street, layered painted walls suggesting many ideas converging into one path, human-scale scene, open pale area on the right.
3. **Human contribution:** Bugis street mural-inspired wall art with a person thoughtfully observing and sketching ideas, expressive colours but no readable lettering, balanced composition with open space for key points.
4. **Context and specifications:** Chinatown lanterns above a quiet street, lanterns at different depths suggesting selected and organized context, warm light against teal shadows, clear negative space on the left.
5. **Tools and boundaries:** Clarke Quay at blue hour, historic riverside buildings, bridges connecting separate points, subtle reflections suggesting connected systems, uncluttered upper-right area for text.
6. **Daily engineering loop:** Watercolor view of Singapore shophouses and a five-foot way, a gently curving walkway with small visual cues of making, checking, and revising, no literal icons or words, open sky for slide text.
7. **Reliability and evaluation:** Clarke Quay bridge in changing weather, soft rain fading into clear light, stable bridge structure and layered river reflections, visual metaphor for resilience, pale space for text.
8. **Security and governance:** Chinatown lanterns glowing behind a patterned screen, light contained within clear boundaries, elegant architectural details, restrained palette and open space for text.
9. **Team capability:** Haji Lane-inspired mural street with a small group exchanging ideas, collaborative but not posed, painterly colour flowing through the scene, open central area for a short phrase.
10. **Closing:** Wide Singapore river scene with Clarke Quay lights and bridges at dusk, reflections leading toward a luminous horizon, calm hopeful mood, large uncluttered sky for the closing message.

**Practical slide note:** Keep the artwork soft behind the content, use one main idea per slide, and place text over a consistent translucent cream panel if the image’s contrast varies.
