# PromptBook Comprehensive Guide

This guide covers everything you need to know about using and accessing PromptBook's library of prompts, skills, and plugins.

---

## 📝 Prompt Templates
Promptbook provides a structured library of expert templates. You can access them in two primary ways:

### 1. Web Explorer (Easiest)
Browse, search, and hydrate prompts directly in your browser at **[ronmkr.github.io/PromptBook/](https://ronmkr.github.io/PromptBook/)**. This is the fastest way to use Promptbook without local installation.

### 2. CLI Integration
If the Promptbook extension is active, access prompts via the `/prompts:` namespace:
```bash
/prompts:code-review @file.ts
```

---

## 🛠 Skills (Behavioral Intelligence)
Skills are behavioral models that define how an AI agent should output information or interact with code.

### How to Use Skills
Skills are located in the `skills/` directory. Each skill is defined by a `SKILL.md` file.
*   **Contextual Activation**: When using an agent that supports the Universal Agent spec, skills are automatically loaded based on the task.
*   **Manual Reference**: You can point your AI to a specific `SKILL.md` to adopt that behavior.

### Key Categories
*   **Foundational**: Basic file handling (PDF, Word, Excel).
*   **Technical**: Language-specific patterns (Rust, Go, Python).
*   **Meta**: Tools for creating and optimizing other skills.

---

## 🔌 Plugins (Tooling & Agents)
Plugins extend the agent's capabilities with new tools and specialized sub-agents.

### Installation
Install plugins from the marketplace using the CLI:
```bash
/plugin install {plugin-name}@antigravity-plugins-official
```

### Understanding Tiers
*   **Core (Tier 0)**: Essential platform components.
*   **Ecosystem (Tier 1)**: High-trust extensions (GitHub, Firebase, Asana).
*   **Standard (Tier 2)**: General productivity and development tools.

---

## 🚀 Getting Started
1.  **Clone**: `git clone https://github.com/ronmkr/PromptBook.git`
2.  **Browse**: Use the [Full Catalog](../CATALOG.md) to discover components.
3.  **Use**: Choose the access method (Web or CLI) that fits your workflow.
