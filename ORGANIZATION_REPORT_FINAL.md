# Universal Agent Ecosystem - Organization & Portability Report

The repository has been fully refactored into a **Provider-Agnostic, Multi-Tier Platform**. All intelligence—including skills, prompts, and tools—is now system-neutral, ensuring seamless migration to any LLM or Agentic Orchestrator (Claude, Gemini, OpenAI, etc.).

## 🌍 The Universal Taxonomy

### Tier 0: Core Platform (`/core`)
*Foundational systems for any agentic environment.*
- **`core/bootstrap/`**: Recommends automation instruction sets for new codebases.
- **`core/memory/`**: Advanced instruction-state management and learning extraction.
- **`core/agent-sdk/`**: Unified kits for building extensible agents.
- **`core/plugin-dev-toolkit/`**: Expert skills for creating new capabilities.
- **`skills/meta/behavior-instruction-factory/`**: The logic for packaging and validating behavioral instructions.

### Tier 1: Ecosystem Extensions (`/plugins/ecosystem`)
*Integrations for major infrastructure, using standardized tool patterns.*
- **`cloud/`**: AWS, Azure, GCP, Vercel, Netlify.
- **`database/`**: MongoDB, CockroachDB, Pinecone, Redis.
- **`dev-tools/`**: Universal LSPs, GitHub, GitLab, Playwright, Terraform.
- **`security/`**: Auth0, JFrog, Vulnerability Scanning.
- **`productivity/`**: Asana, Linear.

### Tier 2: Standard Extensions (`/plugins/standard`)
*Verified community-grade tools and bridge connectors.*
- **`development/`**: `feature-dev`, `playground`, `loop-verification`.
- **`productivity/`**: `code-review`, `instruction-simplifier`, `math-verifiers`.
- **`bridge/`**: Messaging connectors (Discord, Telegram, iMessage).

### Tier 3: Behavioral Intelligence (`/skills`)
*Functional models for specific outputs, stripped of provider branding.*
- **`foundational/`**: Document operations (DOCX, PDF, XLSX).
- **`technical/`**: `mcp-builder`, `webapp-testing`, `frontend-design`.
- **`enterprise/`**: `internal-comms`, `brand-standards`.
- **`creative-lab/`**: `generative-canvas-art`, `ui-theme-generator`.

### Tier 4: Prompt Library (`/prompts`)
- Root-level library of **35+ categories**, using the `{{args}}` and `{{code}}` universal hydration syntax.

---

## 🏗️ Portability Wins

1.  **Neutral Terminology**: Replaced all instances of "Claude/Gemini" with **"The Agent"**, and "Antigravity/Claude Code" with **"The Platform"**.
2.  **Abstracted Technicals**:
    *   `GOOGLE_API_KEY` → `AGENT_API_KEY`.
    *   `gemini-3.1-pro` → `universal-model-pro`.
    *   `slash commands` → `system commands`.
3.  **Migration-Ready**: Created **`docs/guides/PORTABILITY.md`** as the master guide for mapping these generic assets to specific providers.
4.  **Decoupled Manifest**: The root registry now uses a version-agnostic schema, allowing it to be used as a template for any marketplace.

This repository is now a high-fidelity **Knowledge & Tooling Engine** that is immune to provider-specific locking.
