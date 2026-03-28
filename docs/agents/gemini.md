# Using promptbook with Gemini CLI

Promptbook is natively integrated with Gemini CLI as an extension.

## 🌐 Web Explorer (Recommended)
The easiest way to discover and preview prompts is via the [Web Explorer](https://ronmkr.github.io/PromptBook/):
1. Open the [Explorer](https://ronmkr.github.io/PromptBook/).
2. Select a prompt.
3. Paste your context/code into the arguments field.
4. Copy the hydrated prompt and paste it into your Gemini session.

## 🔌 CLI Integration
If you have the Promptbook repository, you can link it directly:
```bash
gemini extension install /path/to/promptbook
```

Once installed, use the `/prompts:` prefix:
```bash
/prompts:code-review-security {{file}}
```

## 💻 Explorer & Search
Power users can use the TUI or CLI search:
```bash
# Launch TUI
make tui

# Search via CLI
pop search "react testing"
```

---

## Using Promptbook as Skills
PromptBook templates work as reusable skills for Gemini CLI.

### Quick Skill Injection
```bash
# Hydrate and copy
pop use code-reviewer-agent --args @file.py | pbcopy
```

### Export as Standalone Skill
```bash
# Export for Gemini skill activation
pop use project-guidelines --no-copy > ~/.gemini/skills/my-project/SKILL.md
```
