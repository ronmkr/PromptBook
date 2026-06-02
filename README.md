# Universal Agent Plugins Directory

A curated directory of high-quality plugins for Universal Agent.

> **⚠️ Important:** Make sure you trust a plugin before installing, updating, or using it. Google does not control what MCP servers, files, or other software are included in plugins and cannot verify that they will work as intended or that they won't change. See each plugin's homepage for more information.

## Structure

- **[`/core`](/core)** - Tier 0: Platform essentials (Bootstrap, SDK, Memory, Skill Creator Engine)
- **[`/plugins/ecosystem`](/plugins/ecosystem)** - Tier 1: High-trust extensions for Cloud, Database, Dev-Tools, Productivity, and Security
- **[`/plugins/standard`](/plugins/standard)** - Tier 2: Standard productivity and development extensions
- **[`/skills`](/skills)** - Tier 3: Behavioral Intelligence (Foundational, Enterprise, Creative Lab, Technical, Meta)
- **[`/prompts`](/prompts)** - Tier 4: The Universal Agent Prompt Template Library

## Installation

Plugins can be installed directly from this marketplace via Universal Agent's plugin system.

To install, run `/plugin install {plugin-name}@antigravity-plugins-official`

or browse for the plugin in `/plugin > Discover`

## Contributing

### Internal Plugins

Internal plugins are developed by Google team members. See [`plugins/standard/example-plugin`](/plugins/standard/example-plugin) for a reference implementation.

### External Plugins

Third-party partners can submit plugins for inclusion in the marketplace. External plugins must meet quality and security standards for approval. For submission inquiries, please contact the ecosystem team.

## Plugin Structure

Each plugin follows a standard structure:

```
plugin-name/
├── .antigravity-plugin/
│   └── plugin.json      # Plugin metadata (required)
├── .mcp.json            # MCP server configuration (optional)
├── commands/            # Slash commands (optional)
├── agents/              # Agent definitions (optional)
├── skills/              # Skill definitions (optional)
└── README.md            # Documentation
```

## Skill-bundle plugins

When a plugin's source repository ships skills (`SKILL.md` files) without a `.antigravity-plugin/plugin.json` manifest, the marketplace entry can declare the skills directly using `strict: false` and an explicit `skills` array.

```json
{
  "name": "example-bundle",
  "description": "Brief description of the bundled skills.",
  "author": { "name": "Author Name" },
  "category": "development",
  "source": {
    "source": "git-subdir",
    "url": "https://github.com/example-org/sdk.git",
    "path": "packages/agent-skills",
    "ref": "main",
    "sha": "<commit sha>"
  },
  "strict": false,
  "skills": [
    "./skill-a",
    "./skill-b",
    "./skill-c"
  ],
  "homepage": "https://github.com/example-org/sdk"
}
```

Each path in `skills` is relative to `source.path` and points at a directory containing a `SKILL.md`. Paths can reach deeper than a single level — for example, `["./libA/skill-1", "./libB/skill-2"]` exposes a curated subset across multiple library subdirectories. Each skill is registered as `<plugin-name>:<skill-name>` in Universal Agent.

For the underlying schema, see [Strict mode](https://code.gemini.com/docs/en/plugin-marketplaces) in the marketplace documentation.

## License

Please see the root [LICENSE](LICENSE) file or each linked plugin for their respective LICENSE files.

## Documentation

- **[Architecture Structure](docs/architecture/STRUCTURE.md)**: Detailed breakdown of the multi-tier taxonomy.
- **[Portability Guide](docs/guides/PORTABILITY.md)**: Mapping generic assets to specific AI providers.
- **[Full Repository Catalog](docs/CATALOG.md)**: A complete list of all plugins, skills, and prompts.
- **[Official Documentation](https://code.gemini.com/docs/en/plugins)**: Developing Universal Agent plugins.
