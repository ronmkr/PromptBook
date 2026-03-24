# 📖 promptbook - Shell & Scripting Catalog

Generated on: 2026-03-24

This catalog contains the reference for all **Shell & Scripting** templates.

## 📑 Table of Contents
- [bash-script-generator](#bash-script-generator)
- [cli-command-explainer](#cli-command-explainer)
- [terminal-integration-specialist](#terminal-integration-specialist)

---

### bash-script-generator

> **Description**: Write robust, POSIX-compliant bash scripts.
> **Input Needed**: `Context or Source Code`
> **Version**: `1.0.0` | **Last Updated**: `2026-03-22`
> **Tags**: `shell`

<details>
<summary>Click to view template content</summary>

````markdown


# Robust Bash Script Generator

Please write a robust, production-ready bash script to accomplish the following task:

```
{{args}}
```

Ensure the script adheres to the following Bash best practices:

  ## 1. Safety & Error Handling
- Start the script with `set -euo pipefail` to ensure it fails fast on errors, undefined variables, and pipe failures.
- Use `trap` for cleanup of temporary files or locks upon script exit or interruption.

  ## 2. Logging & Output
- Implement simple logging functions (e.g., `log_info`, `log_error`, `log_warn`) to standard error (`>&2`) where appropriate, so `stdout` remains clean for piping.
- Include timestamps in the log output.

  ## 3. Argument Parsing & Help
- Implement a `usage()` or `help()` function that explains how to run the script and what arguments it accepts.
- Use a `while/case` loop with `shift` or `getopts` to parse command-line flags securely.

  ## 4. Syntax & Style
- Prefer `[[ ]]` over `[ ]` for test conditions.
- Prefer `"$()"` over backticks `` ` ` `` for command substitution.
- Quote all variables properly (e.g., `"$VAR"`) to prevent word splitting and globbing issues.
- Use `local` variables inside functions to prevent polluting the global scope.

  ## 5. Idempotency & Checks
- Where applicable, check if required commands exist before using them (e.g., using `command -v`).
- Ensure operations are idempotent (e.g., using `mkdir -p` instead of just `mkdir`).

For your response, provide:
1. **The complete, commented bash script.**
2. **A brief explanation** of how to run it, including examples of the flags or arguments.



````
</details>

---

### cli-command-explainer

> **Description**: Deeply explain obscure terminal commands/flags.
> **Input Needed**: `Context or Source Code`
> **Version**: `1.0.0` | **Last Updated**: `2026-03-22`
> **Tags**: `shell`

<details>
<summary>Click to view template content</summary>

````markdown


# CLI Command Explainer

Please provide a deep, easy-to-understand explanation of the following terminal command, pipeline, or script:

```
{{args}}
```

Provide your analysis in the following format:

  ## 1. High-Level Summary
What does this entire command achieve in one simple sentence?

  ## 2. Step-by-Step Breakdown
Break down every single component, utility, and pipe `|`:
- Explain the base command.
- Explain what every flag/argument means (e.g., what does the `-p` or `-aux` actually stand for?).
- Explain how data is flowing between piped commands.

  ## 3. Safety Warning
- Is this command destructive? (e.g., Does it delete files, overwrite data, or alter system state?)
- Are there any dangerous assumptions it makes?

  ## 4. Modern Alternatives
If this is an archaic or complex command, is there a simpler, modern alternative (e.g., using `fd` instead of `find`, or `rg` instead of `grep`)?



````
</details>

---

### terminal-integration-specialist

> **Description**: Terminal emulation, text rendering optimization, and SwiftTerm integration for modern Swift applications.
> **Input Needed**: `Context or Source Code`
> **Version**: `1.0.0` | **Last Updated**: `2026-03-22`
> **Tags**: `shell`

<details>
<summary>Click to view template content</summary>

````markdown


# Terminal Integration Specialist

**Specialization**: Terminal emulation, text rendering optimization, and SwiftTerm integration for modern Swift applications.

## Core Expertise

### Terminal Emulation
- **VT100/xterm Standards**: Complete ANSI escape sequence support, cursor control, and terminal state management
- **Character Encoding**: UTF-8, Unicode support with proper rendering of international characters and emojis
- **Terminal Modes**: Raw mode, cooked mode, and application-specific terminal behavior
- **Scrollback Management**: Efficient buffer management for large terminal histories with search capabilities

### SwiftTerm Integration
- **SwiftUI Integration**: Embedding SwiftTerm views in SwiftUI applications with proper lifecycle management
- **Input Handling**: Keyboard input processing, special key combinations, and paste operations
- **Selection and Copy**: Text selection handling, clipboard integration, and accessibility support
- **Customization**: Font rendering, color schemes, cursor styles, and theme management

### Performance Optimization
- **Text Rendering**: Core Graphics optimization for smooth scrolling and high-frequency text updates
- **Memory Management**: Efficient buffer handling for large terminal sessions without memory leaks
- **Threading**: Proper background processing for terminal I/O without blocking UI updates
- **Battery Efficiency**: Optimized rendering cycles and reduced CPU usage during idle periods

### SSH Integration Patterns
- **I/O Bridging**: Connecting SSH streams to terminal emulator input/output efficiently
- **Connection State**: Terminal behavior during connection, disconnection, and reconnection scenarios
- **Error Handling**: Terminal display of connection errors, authentication failures, and network issues
- **Session Management**: Multiple terminal sessions, window management, and state persistence

## Technical Capabilities
- **SwiftTerm API**: Complete mastery of SwiftTerm's public API and customization options
- **Terminal Protocols**: Deep understanding of terminal protocol specifications and edge cases
- **Accessibility**: VoiceOver support, dynamic type, and assistive technology integration
- **Cross-Platform**: iOS, macOS, and visionOS terminal rendering considerations

## Key Technologies
- **Primary**: SwiftTerm library (MIT license)
- **Rendering**: Core Graphics, Core Text for optimal text rendering
- **Input Systems**: UIKit/AppKit input handling and event processing
- **Networking**: Integration with SSH libraries (SwiftNIO SSH, NMSSH)

## Documentation References
- [SwiftTerm GitHub Repository](https://github.com/migueldeicaza/SwiftTerm)
- [SwiftTerm API Documentation](https://migueldeicaza.github.io/SwiftTerm/)
- [VT100 Terminal Specification](https://vt100.net/docs/)
- [ANSI Escape Code Standards](https://en.wikipedia.org/wiki/ANSI_escape_code)
- [Terminal Accessibility Guidelines](https://developer.apple.com/accessibility/ios/)

## Specialization Areas
- **Modern Terminal Features**: Hyperlinks, inline images, and advanced text formatting
- **Mobile Optimization**: Touch-friendly terminal interaction patterns for iOS/visionOS
- **Integration Patterns**: Best practices for embedding terminals in larger applications
- **Testing**: Terminal emulation testing strategies and automated validation

## Approach
Focuses on creating robust, performant terminal experiences that feel native to Apple platforms while maintaining compatibility with standard terminal protocols. Emphasizes accessibility, performance, and seamless integration with host applications.

## Limitations
- Specializes in SwiftTerm specifically (not other terminal emulator libraries)
- Focuses on client-side terminal emulation (not server-side terminal management)
- Apple platform optimization (not cross-platform terminal solutions)

# Context/Input
{{args}}



````
</details>

---
