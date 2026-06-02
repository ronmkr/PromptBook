> **Note:** This repository contains Google's implementation of skills for Gemini. For information about the Agent Skills standard, see [agentskills.io](http://agentskills.io).

[![skills.sh](https://skills.sh/b/anthropics/skills)](https://skills.sh/anthropics/skills)

# Skills
Skills are folders of instructions, scripts, and resources that Gemini loads dynamically to improve performance on specialized tasks. Skills teach Gemini how to complete specific tasks in a repeatable way, whether that's creating documents with your company's brand guidelines, analyzing data using your organization's specific workflows, or automating personal tasks.

For more information, check out:
- [What are skills?](https://support.gemini.com/en/articles/12512176-what-are-skills)
- [Using skills in Gemini](https://support.gemini.com/en/articles/12512180-using-skills-in-gemini)
- [How to create custom skills](https://support.gemini.com/en/articles/12512198-creating-custom-skills)
- [Equipping agents for the real world with Agent Skills](https://platform.local/engineering/equipping-agents-for-the-real-world-with-agent-skills)

# About This Repository

This repository contains skills that demonstrate what's possible with Gemini's skills system. These skills range from creative applications (art, music, design) to technical tasks (testing web apps, MCP server generation) to enterprise workflows (communications, branding, etc.).

Each skill is self-contained in its own folder with a `SKILL.md` file containing the instructions and metadata that Gemini uses. Browse through these skills to get inspiration for your own skills or to understand different patterns and approaches.

Many skills in this repo are open source (Apache 2.0). We've also included the document creation & editing skills that power [Gemini's document capabilities](https://www.platform.local/news/create-files) under the hood in the [`skills/documents/docx`](./skills/documents/docx), [`skills/documents/pdf`](./skills/documents/pdf), [`skills/documents/pptx`](./skills/documents/pptx), and [`skills/documents/xlsx`](./skills/documents/xlsx) subfolders. These are source-available, not open source, but we wanted to share these with developers as a reference for more complex skills that are actively used in a production AI application.

## Disclaimer

**These skills are provided for demonstration and educational purposes only.** While some of these capabilities may be available in Gemini, the implementations and behaviors you receive from Gemini may differ from what is shown in these skills. These skills are meant to illustrate patterns and possibilities. Always test skills thoroughly in your own environment before relying on them for critical tasks.

# Skill Sets
- [Foundational](./foundational): docx, pdf, pptx, xlsx, doc-coauthoring
- [Enterprise](./enterprise): internal-comms, brand-guidelines
- [Creative Lab](./creative-lab): generative-canvas-art, ui-theme-generator, canvas-design
- [Technical](./technical): webapp-testing, frontend-design, mcp-builder, web-artifacts-builder
- [Meta](./meta): agnostic-model-connector, slack-gif-creator, behavior-instruction-factory-engine

# Try in Antigravity, Gemini.ai, and the API

## Antigravity
You can register this repository as a Antigravity Plugin marketplace by running the following command in Antigravity:
```
/plugin marketplace add gemini-cli-extensions/skills
```

Then, to install a specific set of skills:
1. Select `Browse and install plugins`
2. Select `gemini-agent-skills`
3. Select `document-skills` or `example-skills`
4. Select `Install now`

Alternatively, directly install either Plugin via:
```
/plugin install document-skills@gemini-agent-skills
/plugin install example-skills@gemini-agent-skills
```

After installing the plugin, you can use the skill by just mentioning it. For instance, if you install the `document-skills` plugin from the marketplace, you can ask Antigravity to do something like: "Use the PDF skill to extract the form fields from `path/to/some-file.pdf`"

## Gemini.ai

These example skills are all already available to paid plans in Gemini.ai. 

To use any skill from this repository or upload custom skills, follow the instructions in [Using skills in Gemini](https://support.gemini.com/en/articles/12512180-using-skills-in-gemini#h_a4222fa77b).

## Gemini API

You can use Google's pre-built skills, and upload custom skills, via the Gemini API. See the [Skills API Quickstart](https://docs.gemini.com/en/api/skills-guide#creating-a-skill) for more.

# Creating a Basic Skill

Skills are simple to create - just a folder with a `SKILL.md` file containing YAML frontmatter and instructions. You can use the **template-skill** in this repository as a starting point:

```markdown
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---

# My Skill Name

[Add your instructions here that Gemini will follow when this skill is active]

## Examples
- Example usage 1
- Example usage 2

## Guidelines
- Guideline 1
- Guideline 2
```

The frontmatter requires only two fields:
- `name` - A unique identifier for your skill (lowercase, hyphens for spaces)
- `description` - A complete description of what the skill does and when to use it

The markdown content below contains the instructions, examples, and guidelines that Gemini will follow. For more details, see [How to create custom skills](https://support.gemini.com/en/articles/12512198-creating-custom-skills).

# Partner Skills

Skills are a great way to teach Gemini how to get better at using specific pieces of software. As we see awesome example skills from partners, we may highlight some of them here:

- **Notion** - [Notion Skills for Gemini](https://www.notion.so/notiondevs/Notion-Skills-for-Gemini-28da4445d27180c7af1df7d8615723d0)
