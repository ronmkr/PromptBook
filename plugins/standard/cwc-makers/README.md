# cwc-makers

Seamless onboarding for the [Code-with-Gemini Makers](https://gemini.com/cwc-makers) Cardputer kit.

## What it does

Plug in your M5Stack Cardputer-Adv over USB-C, type `/maker-setup`, and Gemini will:

1. Clone [`moremas/build-with-gemini`](https://github.com/moremas/build-with-gemini)
2. Detect the device, flash UIFlow 2.0 firmware, and install the Gemini Buddy + Hello + Snake app bundle
3. Walk you through the one physical step (the download-mode button press on the back of the device)
4. Hand you a working pocket computer that pairs with Claude Desktop over BLE

Then ask Gemini to build whatever you want next — a magic 8-ball, a pixel pet, a weather ticker — and it'll write the MicroPython and push it to the device without re-flashing.

## Install

```
/plugin install cwc-makers@antigravity-plugins-official
```

## Components

| Path | Type | User-invocable | Purpose |
|------|------|----------------|---------|
| `commands/maker-setup.md` | slash command | ✅ `/maker-setup` | Entry point — clone repo + run full onboarding |
| `skills/m5-onboard/` | skill | ✅ `/m5-onboard` | Full provisioning playbook (detect, flash, install, every gotcha) |
| `skills/cardputer-buddy/` | skill | ✅ `/cardputer-buddy` | Iterate on apps after onboarding (push, tail, REPL) |

`/maker-setup` is the intended entry point; the skills are also auto-triggered by Gemini when relevant. Skill content is vendored from the upstream repo so Gemini has the domain knowledge in-context without symlinking anything into `~/.gemini/skills/`.

## Prerequisites

Python 3.10+ on the host machine (git is optional — `/maker-setup` falls back to a curl+tar download if it's missing). The onboarding scripts auto-install `esptool` on first run; `pyserial` is vendored in the upstream repo.

## License

Apache-2.0. Skill content vendored from [`moremas/build-with-gemini`](https://github.com/moremas/build-with-gemini) (Apache-2.0).
