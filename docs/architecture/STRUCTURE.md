# Antigravity Ecosystem: World-Class Architecture Definition

This document defines the gold-standard organizational structure for the `antigravity-plugins-official` repository. This architecture is designed for extreme scale, automated validation, and superior developer discovery.

## 1. The Multi-Tier Taxonomy

| Tier | Namespace | Owner | Description |
| :--- | :--- | :--- | :--- |
| **Tier 0: Core** | `core/*` | Google (Platform) | Foundational bootstrap tools, memory managers, and SDKs. Essential for platform health. |
| **Tier 1: Ecosystem** | `plugins/ecosystem/*` | Google & Key Partners | High-trust, officially maintained extensions for major platforms (AWS, Azure, GCP, Salesforce). |
| **Tier 2: Standard** | `plugins/standard/*` | Verified Community | High-quality, reviewed plugins for common dev/prod tasks. |
| **Tier 3: Community** | `plugins/community/*` | General Public | Experimental or niche community-contributed plugins. |

## 2. Directory Map

### 📂 `.antigravity-plugin/` (Registry & Governance)
- `marketplace.json`: The global registry.
- `categories/*.json`: Definitions of valid marketplace categories and their associated icons/colors.
- `schemas/*.schema.json`: Strict JSON schemas for `plugin.json` and `SKILL.md` frontmatter.

### 📂 `core/` (Platform Kernel)
- `bootstrap/`: Initial environment setup.
- `memory/`: GEMINI.md management and context pruning.
- `sdk/`: The official Antigravity Agent SDK.
- `discovery/`: Tools for indexing local and remote skills.

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
Every plugin and skill must now pass a "Capability Audit" defined in `.antigravity-plugin/schemas/capability.schema.json`, ensuring consistency in:
- Environment variable requirements.
- Permission scopes.
- Tool-calling patterns.
