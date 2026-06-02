# Universal Agent Interface (UAI) - Portability Guidelines

This repository has been refactored to follow the **Universal Agent Interface (UAI)** standard. All instructions, logic, and metadata are intentionally system-neutral to ensure portability across any LLM or Agentic Orchestrator.

## ⚖️ Terminology Mapping

When migrating to a new system, use this mapping to translate generic terms to provider-specific ones:

| Universal Term | Claude Equivalent | Gemini Equivalent | ChatGPT Equivalent |
| :--- | :--- | :--- | :--- |
| **The Agent** | Claude | Gemini | ChatGPT / GPT-4 |
| **The Platform** | Claude Code | Antigravity | OpenAI Canvas / GPTs |
| **Agent Artifacts** | Artifacts | Artifacts | Code Interpreter Blocks |
| **System Commands** | Slash Commands | Slash Commands | Custom Instructions |
| **Platform Metadata** | `.claude-plugin` | `.antigravity-plugin` | `manifest.json` |

## 🏗️ Design Principles for Portability

1.  **Functional Over Nominal**: Describe *what* the agent should do, not *who* the agent is. Use "The Agent should evaluate..." instead of "Gemini should evaluate...".
2.  **Environment-Based Triggers**: Avoid hardcoding platform-specific UI elements. Refer to "Input Context" instead of "Chat Box".
3.  **Standardized Schemas**: Use standard JSON/TOML for configuration rather than provider-proprietary formats where possible.
4.  **Agnostic SDKs**: Prefer REST APIs and generic HTTP wrappers over platform-specific library SDKs in core logic.

## 🚀 How to Migrate
1.  **Rename Registry**: Change the root `.antigravity-plugin/` directory to match your target system's manifest folder.
2.  **Environment Variables**: The ecosystem uses `PLATFORM_API_KEY`. Map your specific provider key (e.g., `OPENAI_API_KEY`) to this variable.
3.  **Capabilities Audit**: Review `docs/architecture/CAPABILITIES.md` to see which generic features (e.g., "Filesystem Access") your target system supports.
