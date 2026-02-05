# 🧠 Reasoning Agents - Starter Kit

**Track**: Battle #2 - Reasoning Agents with Microsoft Foundry  

Welcome to the Reasoning Agents track! In this challenge, you'll build a multi-agent system with **Microsoft Foundry** that leverages advanced reasoning capabilities to solve complex problems. This starter kit provides you with the foundational knowledge, tools, and resources to get started on your journey.

---

## Prerequisites

Before starting this challenge, ensure you have the following:

### Required Skills
- **Basic Python programming** — variables, functions, classes, and working with APIs
- **Command line familiarity** — navigating directories, running scripts
- **Basic understanding of AI concepts** — what LLMs are, prompts, and responses

### Required Accounts (Free Tiers Available)
| Account | Purpose | Sign Up |
|---------|---------|---------|
| **GitHub** | Version control and submission | [github.com](https://github.com) |
| **Microsoft Azure** | Access to Microsoft Foundry | [azure.microsoft.com/free](https://aka.ms/azure-free-account) |
| **Discord** | Community support | [aka.ms/agentsleague/discord](https://aka.ms/agentsleague/discord) |

### Required Tools
- **Python 3.10+** — [python.org/downloads](https://python.org/downloads)
- **Visual Studio Code** — [code.visualstudio.com](https://code.visualstudio.com)
- **Git** — [git-scm.com](https://git-scm.com)

### Azure Subscription Notes
> [!IMPORTANT]
> Microsoft Foundry requires an Azure subscription. A **free trial** provides $200 credit for 30 days. Some features may incur costs after the trial. Check the [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator/) to estimate costs.

> [!WARNING]
> **Free Tier Limitations:** The Azure free subscription has significant constraints that may prevent full implementation of this challenge:
> - **Model access:** Some advanced models (e.g., GPT-5, Claude) may not be available or have very limited quotas
> - **Rate limits:** Strict API call limits (e.g., requests per minute, tokens per day)
> - **Region restrictions:** Free tier resources may only be available in limited regions
> - **Feature restrictions:** Some Microsoft Foundry features (agent orchestration, evaluations) may require pay-as-you-go
> - **Credit exhaustion:** $200 credit can be consumed quickly with heavy AI model usage
>
> **Recommendation:** For full functionality, consider a **pay-as-you-go** subscription or request access to [Azure for Students](https://azure.microsoft.com/free/students/) ($100 credit, no credit card required) or the [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups).

### ⏱️ Time Commitment
- **Setup**: ~1-2 hours
- **Learning basics**: ~4-6 hours
- **Building solution**: ~10-20 hours (varies by complexity)

---

## 🛠️ Environment Setup Guidance

Tips on setting up your development environment:

### Step 1: Clone the Repository
```bash
git clone https://github.com/YOUR-USERNAME/agentsleague.git
cd agentsleague/starter-kits/2-reasoning-agents
```

### Step 2: Create a Python Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```


### Step 3: Set Up Azure Credentials

1. Go to [Microsoft Foundry Portal](https://ai.azure.com)
2. Create or select your **AI Project**
3. In your project, go to **Project settings** (gear icon) → **Project properties**
4. Copy the **Project connection string**
5. Create a `.env` file in this directory:

```env
# Option 1: Use Project Connection String (Recommended)
# Find this in AI Foundry portal: Project settings → Project properties
AZURE_AI_PROJECT_CONNECTION_STRING=your-connection-string-here

# Option 2: Use Individual Settings
# AZURE_SUBSCRIPTION_ID=your-subscription-id
# AZURE_RESOURCE_GROUP=your-resource-group
# AZURE_AI_PROJECT_NAME=your-project-name

# Model Deployment Name (from your project's Deployments)
AZURE_AI_MODEL_DEPLOYMENT=gpt-4o
```

> [!TIP]
> **Finding your connection string:**
> 1. Open [ai.azure.com](https://ai.azure.com)
> 2. Select your project
> 3. Click the gear icon (Project settings) → Project properties
> 4. Copy the "Project connection string"

> [!WARNING]
> Never commit your `.env` file to GitHub! It's already in `.gitignore`.


---

## Project Ideas

In this track, we encourage you to create a multi-agent solution, using one of the following development approaches.

### Development Approaches

1. **Local development:** Build and test your custom agentic solution locally with the OSS [**Microsoft Agent Framework**](https://github.com/microsoft/agent-framework) in Visual Studio Code.
1. **Cloud-based development:** Use [**Microsoft Foundry**](https://azure.microsoft.com/products/ai-foundry/) to orchestrate your reasoning agents in the Cloud. You can choose either a low-code/no-code approach - leveraging the [Foundry UI](https://ai.azure.com) to configure your agents and workflows - or a code-first approach - using the **Foundry Agent Service** within the [Foundry SDK](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/develop/sdk-overview) to build your agentic AI solution programmatically.

Whatever approach you choose, you are encouraged to:

- Leverage Microsoft Foundry-hosted, GitHub-hosted or locally-hosted AI models.
- Use visualizations and monitoring tools to track agent performance and interactions.
- Integrate with various data sources/APIs/MCP tools to enhance agent capabilities.
- Implement evaluation and deployment strategies for your multi-agent system.
- Leverage AI-assisted development tools to accelerate your build process (e.g. [GitHub Copilot](https://github.com/features/copilot)).

### Real-world Scenario

The goal of this track challenge is to build a multi-agent system that can effectively assist students in their preparation for Microsoft certification exams. The system should be capable of understanding the exam syllabus, generating study plans, providing practice questions, and offering feedback on performance.

Below is a suggested architecture for your multi-agent solution. Feel free to adapt and expand upon this architecture based on your creativity and technical skills.

![Reasoning Agents Architecture](./reasoning-agents-architecture.png)

In the above architecture:

1. The student inputs to the system the topics they wish to learn. This input is processed, so that the main information are extracted in a pre-defined structure and sent to a subworkflow of 3 sequential agents:
    - A *learning path curator* agent – suggesting a list of learning paths on Microsoft Learn relevant to the topics provided.
    - A *study plan generator* agent - converting the curated path into a tangible study plan and generating a timeline with milestones, suggested time allocations, and daily/weekly study sessions.
    - An *engagement* agent – setting up automated reminders to send to the student email to help them stay up to date with the study plan.
1. Once the subworkflow is executed, the system waits for a human input that confirms the student is ready to start an assessment.
1. Once the student confirms, the *assessment* agent generates an assessment to evaluate the student readiness.
1. If the student passes the test, then another agent suggests the relevant Microsoft certification to take and plans the exam. Otherwise, the system loops back into the preparation subworkflow.

> [!TIP]
> Some of the functionalities described in the architecture above can be implemented by integrating with the [Microsoft Learn MCP server](https://github.com/microsoftdocs/mcp). Learn more about it in the [Microsoft Learn MCP documentation](https://learn.microsoft.com/training/support/mcp).

---

## 🚀 Quick Start

Get started quickly by exploring the following resources that provide step-by-step guidance for building custom agents.

### Build your first agent with Microsoft Foundry UI

Learn how to set up your Microsoft Foundry project and prototype your first agent with a low-code approach using the Microsoft Foundry UI.

🔗Microsoft Foundry quick starter: [https://learn.microsoft.com/training/modules/ai-agent-fundamentals/](https://learn.microsoft.com/training/modules/ai-agent-fundamentals/)

### Build your first agent with Microsoft Foundry Python SDK

Learn how to build your first custom agent and equip it with knowledge and tools using the Microsoft Foundry Agent Service with this hands-on tutorial.

🔗Build a Pizza Ordering Agent with Microsoft Foundry and MCP: [https://jolly-field-035345f1e.2.azurestaticapps.net/](https://jolly-field-035345f1e.2.azurestaticapps.net/)

### Build a multi-agent workflow with Microsoft Foundry

Learn how to orchestrate multiple agents into a declarative (low-code) or hosted (code-first) workflow using Microsoft Foundry.

🔗Build a workflow in Microsoft Foundry: [https://learn.microsoft.com/azure/ai-foundry/agents/concepts/workflow?view=foundry](https://learn.microsoft.com/azure/ai-foundry/agents/concepts/workflow?view=foundry)

### Build and orchestrate agents locally with Microsoft Agent Framework

Follow these step-by-step tutorials to build custom agents and orchestrate them through multi-agent workflows using the open-source Microsoft Agent Framework.

🔗Microsoft Agent Framework tutorials (C# and Python): [https://learn.microsoft.com/agent-framework/tutorials/overview](https://learn.microsoft.com/agent-framework/tutorials/overview)

---

## 🧠 Reasoning Patterns & Best Practices

When designing your reasoning agents and multi-agent workflows, consider applying well-established reasoning patterns and agentic best practices to improve robustness, transparency, and outcomes.

### Common reasoning patterns to explore include:

1. **Planner–Executor:** Separate agents responsible for planning (breaking down the problem) and execution (carrying out tasks step by step).
1. **Critic / Verifier:** Introduce an agent that reviews outputs, checks assumptions, and validates reasoning before final responses are returned.
1. **Self-reflection & Iteration:** Allow agents to reflect on intermediate results and refine their approach when confidence is low or errors are detected.
1. **Role-based specialization:** Assign clear responsibilities to each agent to reduce overlap and improve reasoning quality.

### Best practices for building with Microsoft Foundry:

1. Use **telemetry**, logs, and visual workflows in Foundry to understand how agents reason and collaborate.
    - Explore Foundry built-in monitoring tools to track agent interactions and performance: [Foundry Control Plane](https://learn.microsoft.com/azure/ai-foundry/control-plane/overview?view=foundry)
1. Apply **evaluation** strategies (e.g., test cases, scoring rubrics, or human-in-the-loop reviews) to continuously improve agent behavior.
    - [Evaluate generative AI models and applications by using Microsoft Foundry built-in features](https://learn.microsoft.com/azure/ai-foundry/how-to/evaluate-generative-ai-app?view=foundry&preserve-view=true)
    - [Evaluate your AI agents with the Microsoft Foundry SDK](https://learn.microsoft.com/azure/ai-foundry/how-to/develop/cloud-evaluation?view=foundry&tabs=python)
1. Build with **Responsible AI** principles in mind, at both application and data layers.
    - [Responsible AI in Microsoft Foundry](https://learn.microsoft.com/azure/ai-foundry/responsible-use-of-ai-overview?view=foundry)

---

## 📋 Requirements & Evaluation

### ✅ Submission Requirements

To be considered valid, your solution must:

- Implement a **multi-agent system** aligned with the **challenge scenario** (student preparation for Microsoft certification exams).
- Use **Microsoft Foundry** (UI or SDK) and/or the **Microsoft Agent Framework** for agent development and orchestration.
- Demonstrate **reasoning** and multi-step decision-making across agents.
- Integrate with **external tools**, APIs, and/or MCP (Model Context Protocol) servers to meaningfully extend agent capabilities (e.g., learning content retrieval, assessment generation, scheduling, notifications, data access, or evaluations).
- Be **demoable** (live or recorded) and clearly explain the agent interactions.
- Include **clear documentation** in the repository describing: agent roles and responsibilities, reasoning flow and orchestration logic, tools/API/MCP integrations.

> [!NOTE]
> Your solution must align with the challenge scenario, *but you are not required to follow the suggested architecture exactly.*
You are free to design a different agent composition, workflow structure, or reasoning strategy—as long as the system addresses the problem effectively.

Optional — but *highly valued*:

- Use of **evaluations**, **telemetry**, or **monitoring**
- Advanced **reasoning patterns** (planner–executor, critics, reflection loops)
- **Responsible AI** considerations (guardrails, validation, fallbacks)

### 🏆 Evaluation Criteria

Submissions will be scored using the following weighted criteria:

| Criterion | Impact |
|-----------|--------|
| **Accuracy & Relevance** | **25%** — Solution meets challenge requirements, aligns with the scenario, and produces correct, relevant outputs |
| **Reasoning & Multi-step Thinking** | **25%** — Clear problem decomposition, structured reasoning, and effective agent collaboration |
| **Creativity & Originality** | **15%** — Novel ideas, unique agent roles, or unexpected but effective execution |
| **User Experience & Presentation** | **15%** — Polished, clear, and demoable experience with understandable workflows |
| **Reliability & Safety** | **20%** — Robust agent patterns, safe tool/API/MCP usage, and avoidance of common pitfalls |

---

## Glossary

New to AI agents? Here's a quick reference for common terms:

| Term | Definition |
|------|------------|
| **Agent** | An AI system that can perceive its environment, make decisions, and take actions to achieve goals |
| **Multi-agent system** | Multiple AI agents working together, each with specialized roles, to solve complex problems |
| **Orchestration** | Coordinating multiple agents to work together in a defined workflow or sequence |
| **LLM (Large Language Model)** | AI models trained on vast text data that can understand and generate human-like text (e.g., GPT-4, Claude) |
| **Prompt** | The input/instruction you give to an AI model to get a specific response |
| **MCP (Model Context Protocol)** | A standard protocol for connecting AI models to external tools, data sources, and services |
| **Reasoning** | The AI's ability to break down problems, think step-by-step, and arrive at logical conclusions |
| **Tool calling** | An agent's ability to use external tools (APIs, databases, web search) to accomplish tasks |
| **Workflow** | A defined sequence of steps or agent interactions to complete a task |
| **Telemetry** | Data collected about agent performance, interactions, and behavior for monitoring and debugging |
| **Guardrails** | Safety mechanisms that prevent agents from producing harmful or incorrect outputs |
| **Human-in-the-loop** | A pattern where human approval is required at certain points in an agent workflow |
| **Evaluation** | Testing and measuring agent performance using metrics, test cases, or human review |
| **Foundry** | Microsoft's cloud platform for building, deploying, and managing AI applications and agents |

---

## 🔧 Troubleshooting

### Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'azure'` | Run `pip install -r requirements.txt` in your activated virtual environment |
| `AuthenticationError` | Verify your API key in `.env` is correct and hasn't expired |
| `Connection refused` errors | Check your Azure endpoint URL and internet connection |
| `RateLimitError` | You've exceeded API limits - wait a few minutes or check your Azure quotas |
| Python command not found | Ensure Python is installed and added to your PATH |
| Virtual environment not activating | On Windows, you may need to run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` first |

### Getting Help
1. Search existing [GitHub Issues](../../issues) for solutions
2. Ask in the Discord [#agentsleague channel](https://aka.ms/agentsleague/discord)
3. Open a new issue using our [Technical Question template](../../issues/new?template=technical-question.md)

---

## Resources

Explore the following additional resources to deepen your knowledge and accelerate your development:

- **Microsoft Foundry Documentation**: [https://learn.microsoft.com/azure/ai-foundry/](https://learn.microsoft.com/azure/ai-foundry/)
- **Microsoft Foundry Agent Service Overview**: [https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview?view=foundry&preserve-view=true](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview?view=foundry&preserve-view=true)
- **Microsoft Agent Framework Documentation**: [https://learn.microsoft.com/agent-framework/](https://learn.microsoft.com/agent-framework/)
- **Microsoft Agent Framework GitHub Repository**: [https://github.com/microsoft/agent-framework](https://github.com/microsoft/agent-framework)
- **AI Agents for Beginners Course**:[aka.ms/ai-agents-beginners](https://aka.ms/ai-agents-beginners)
- **AI assisted development with GitHub Copilot**: [https://github.com/github/awesome-copilot](https://github.com/github/awesome-copilot)

---

Questions? Join [Discord](https://aka.ms/agentsleague/discord) #agentsleague channel
