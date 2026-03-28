# Using promptbook with Windsurf

Windsurf (by Codeium) supports highly contextual agentic flows that can be enhanced with Promptbook templates.

## 🌐 Web Explorer (Recommended)
The fastest way to use Promptbook with Windsurf is via the [Web Explorer](https://ronmkr.github.io/PromptBook/):
1. Open the [Explorer](https://ronmkr.github.io/PromptBook/).
2. Select a template (e.g., `refactor-agent`).
3. Paste your code into the arguments field.
4. Click **Copy** and paste the hydrated prompt into Windsurf's flow.

## 💻 Terminal Explorer (Power Users)
Keep the `pop` TUI open in a separate terminal to quickly find and inject prompts:
```bash
make tui
```

---

## Using Promptbook as Skills
PromptBook templates work as reusable skills for Windsurf.

### Setup Skills Directory
1. Create a directory: `mkdir -p .windsurf/skills`
2. Export templates: `pop use tdd-workflow --no-copy > .windsurf/skills/tdd-workflow.md`
3. Reference them in Windsurf config or via chat.

### Available Categories
| Category | Use Case |
|----------|----------|
| `engineering/` | Code review, refactoring, debugging |
| `security/` | Security audits, threat modeling |
| `testing/` | TDD, E2E, test generation |
| `architecture/` | System design, ADRs |
