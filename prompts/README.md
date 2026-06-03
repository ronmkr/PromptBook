# Unified Prompt Template Library

This directory contains a standardized, versioned library of expert prompt templates for any agentic system. These templates are organized by domain and are designed to be provider-agnostic.

## 📂 Structure
The library is organized into 35+ categories including:
- **`engineering/`**: Development standards, code review, and refactoring.
- **`security/`**: Threat modeling, vulnerability scanning, and policy design.
- **`ai-agents/`**: Autonomous loop logic, multi-agent orchestration, and observer patterns.
- **`language-specific/`**: Python, Rust, Go, TypeScript, etc.

## 🚀 Usage
Templates use a universal hydration syntax:
- `{{args}}`: Primary user input.
- `{{code}}`: Code snippet for analysis.
- `{{file}}`: Full file content.

## ⚖️ Portability
Every template has been refactored to use neutral terminology ("The Agent", "The Platform") to ensure it works across Claude, Gemini, OpenAI, or any custom orchestrator.

## 📖 Catalog
For a full list of all available templates and their descriptions, see the **[📝 Prompt Templates Catalog](../docs/PROMPTS_CATALOG.md)**.

---
*Integrated from the PromptBook expert library.*
