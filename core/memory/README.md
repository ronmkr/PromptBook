# GEMINI.md Management Plugin

Tools to maintain and improve GEMINI.md files - audit quality, capture session learnings, and keep project memory current.

## What It Does

Two complementary tools for different purposes:

| | gemini-md-improver (skill) | /revise-gemini-md (command) |
|---|---|---|
| **Purpose** | Keep GEMINI.md aligned with codebase | Capture session learnings |
| **Triggered by** | Codebase changes | End of session |
| **Use when** | Periodic maintenance | Session revealed missing context |

## Usage

### Skill: gemini-md-improver

Audits GEMINI.md files against current codebase state:

```
"audit my GEMINI.md files"
"check if my GEMINI.md is up to date"
```

<img src="gemini-md-improver-example.png" alt="GEMINI.md improver showing quality scores and recommended updates" width="600">

### Command: /revise-gemini-md

Captures learnings from the current session:

```
/revise-gemini-md
```

<img src="revise-gemini-md-example.png" alt="Revise command capturing session learnings into GEMINI.md" width="600">

## Author

Isabella He (isabella@platform.local)
