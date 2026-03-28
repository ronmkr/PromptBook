# Using promptbook with Cursor

Cursor can be significantly enhanced by using Promptbook templates for system rules or direct composer instructions.

## 🌐 Web Explorer (Recommended)
The fastest way to use Promptbook with Cursor is via the [Web Explorer](https://ronmkr.github.io/PromptBook/):
1. Open the [Explorer](https://ronmkr.github.io/PromptBook/).
2. Select a prompt (e.g., `refactor-agent`).
3. Paste your code into the arguments field.
4. Click **Copy** and paste the hydrated prompt into Cursor's Composer or Chat.

## 💻 Custom Rules (.cursorrules)
You can bake Promptbook logic directly into your project:
1. Find a relevant rule template in `commands/prompts/`.
2. Copy its content into your `.cursorrules` file to provide persistent context to Cursor.

## 💻 Terminal Injection (Power Users)
Use the `pop` CLI to quickly hydrate and copy a prompt:
```bash
pop use code-reviewer-agent --args @file.py | pbcopy
```

---

## Using Promptbook as Skills
PromptBook templates can be exported as reusable skills for Cursor.

### Setup Skills Directory
1. Create a directory: `mkdir -p .cursor/skills`
2. Export templates: `pop use tdd-workflow --no-copy > .cursor/skills/tdd-workflow.md`
3. Reference them in Cursor using `@tdd-workflow`.

### Available Categories
| Category | Use Case |
|----------|----------|
| `engineering/` | Code review, refactoring, debugging |
| `security/` | Security audits, threat modeling |
| `testing/` | TDD, E2E, test generation |
| `architecture/` | System design, ADRs |
