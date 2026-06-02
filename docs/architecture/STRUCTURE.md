# Antigravity Ecosystem: World-Class Architecture Definition

This document defines the gold-standard organizational structure for the `antigravity-plugins-official` repository. This architecture is designed for extreme scale, automated validation, and superior developer discovery.

## 1. The Multi-Tier Taxonomy

| Tier | Namespace | Owner | Description |
| :--- | :--- | :--- | :--- |
| **Tier 0: Core** | `core/*` | Google (Platform) | Foundational bootstrap tools, memory managers, and SDKs. |
| **Tier 1: Ecosystem** | `plugins/ecosystem/*` | Google & Partners | High-trust extensions for major platforms (AWS, GCP, etc.). |
| **Tier 2: Standard** | `plugins/standard/*` | Verified Community | High-quality plugins for common dev/prod tasks. |
| **Tier 3: Skills** | `skills/*` | Universal Agent | Behavioral intelligence models for specific outputs. |
| **Tier 4: Prompts** | `prompts/*` | PromptBook | Standardized library of expert prompt templates. |

## 2. Directory Map

### 📂 `.antigravity-plugin/` (Registry & Governance)
- `marketplace.json`: The global registry.
- `categories/*.json`: Definitions of valid marketplace categories and their associated icons/colors.
- `schemas/*.schema.json`: Strict JSON schemas for `plugin.json` and `SKILL.md` frontmatter.

### 📂 `core/` (Platform Kernel)
- `bootstrap/`: Initial environment setup.
- `memory/`: GEMINI.md management and context pruning.
- `agent-sdk/`: The official Antigravity Agent SDK.
- `plugin-dev-toolkit/`: Expert skills for creating new capabilities.

### 📂 `plugins/ecosystem/` (The "Golden" Extension Set)
- `cloud/`: AWS, Azure, Google Cloud, Vercel, Netlify.
- `database/`: MongoDB, CockroachDB, Pinecone, Redis, PlanetScale.
- `dev-tools/`: LSPs, Debuggers, Buildkite, CircleCI.
- `security/`: Auth0, Snyk, 42Crunch, Aikido.

### 📂 `skills/` (Behavioral Intelligence)
- `foundational/`: Base agent behaviors (doc writing, PDF parsing).
- `enterprise/`: Company-specific workflows (Internal Comms, Brand Guidelines).
- `creative-lab/`: Experimental interactive skills (Algorithmic Art).

### 📂 `scripts/` (Automated Lifecycle)
- `validation/`: CI/CD scripts to verify broken paths, schema compliance, and dead links.
- `discovery/`: Scrapers to find new skill candidates in the wild.
- `maintenance/`: Automated dependency bumps for MCP servers.

## 3. Metadata Standardization
Every plugin and skill must now pass a validation audit based on the schemas in `.antigravity-plugin/schemas/`, ensuring consistency in:
- Environment variable requirements.
- Permission scopes.
- Tool-calling patterns.
