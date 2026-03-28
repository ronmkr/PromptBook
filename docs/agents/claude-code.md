# Using promptbook with Claude Code

Claude Code can be easily enhanced using Promptbook templates for specialized tasks like security audits, TDD, or architectural reviews.

## 🌐 Web Explorer (Recommended)
The fastest way to use Promptbook with Claude Code is via the [Web Explorer](https://ronmkr.github.io/PromptBook/):
1. Visit the [Explorer](https://ronmkr.github.io/PromptBook/).
2. Select a template (e.g., `security-scan`).
3. Paste your code into the arguments field.
4. Click **Copy** and paste the result into your Claude Code session.

## 💻 Terminal Workflow (Power Users)
Pipe code directly into a template and copy the result:
```bash
pop use code-reviewer-agent --args "$(cat main.py)" | pbcopy
```

---

## Using Promptbook as Skills
PromptBook templates work as reusable skills for Claude Code.

### Export as Claude Code Skill
```bash
# Export a template as a compatible skill
pop use project-guidelines --no-copy > ~/.claude/skills/project-guidelines.md
```

### Available Categories
| Category | Use Case |
|----------|----------|
| `engineering/` | Code review, refactoring, debugging |
| `security/` | Security audits, threat modeling |
| `testing/` | TDD, E2E, test generation |
| `architecture/` | System design, ADRs |
| `ai-agents/` | Agentic workflows, MCP, eval |

### Recommended Prompts for Claude Code
- `code-reviewer-agent` — Comprehensive code review
- `security-scan` — Security vulnerability detection
- `refactor-agent` — Safe refactoring suggestions
- `tdd-workflow` — Test-driven development
- `mcp-master` — MCP server design
