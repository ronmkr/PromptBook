# Using promptbook with Aider

Aider uses a CONTEXT -> COMMAND -> EDIT loop. You can use Promptbook templates as surgical instructions for Aider.

## 🌐 Web Explorer (Fastest)
The easiest way to use Promptbook with Aider is via the [Web Explorer](https://ronmkr.github.io/PromptBook/):
1. Open the [Explorer](https://ronmkr.github.io/PromptBook/).
2. Select a prompt (e.g., `refactor-agent`).
3. Paste your code into the arguments field.
4. Click **Copy** and paste the hydrated prompt into Aider's chat.

## 💻 Terminal Usage (Power Users)
1. Find a prompt using `pop search`.
2. Use `pop use <name> --no-copy` to see the prompt.
3. Paste the instructions into Aider's chat.

---

## Using Promptbook as Skills
PromptBook templates work as reusable skills for Aider. Here's how to use them:

### Quick Skill Injection
```bash
# Hydrate a template and copy to clipboard
pop use code-reviewer-agent --args @file.py | pbcopy

# Use with language context for surgical extraction
pop use security-scan --language python --args @main.py | pbcopy
```

### Using with Aider's --prompt Flag
```bash
# Export a template and use with aider
pop use code-reviewer-agent --no-copy > /tmp/code-review.md
aider --prompt /tmp/code-review.md main.py
```

### Available Categories
| Category | Use Case |
|----------|----------|
| `engineering/` | Code review, refactoring, debugging |
| `security/` | Security audits, threat modeling |
| `testing/` | TDD, E2E, test generation |
| `architecture/` | System design, ADRs |
| `<language>-specialist/` | Language-specific patterns |
