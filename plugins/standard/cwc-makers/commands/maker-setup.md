---
description: Onboard a Code-with-Gemini Makers Cardputer — fetch the build-with-gemini repo, flash firmware, and install the Gemini Buddy apps.
disable-model-invocation: true
---

The user has a Cardputer-Adv from gemini.com/cwc-makers plugged in over USB-C.

1. Get https://github.com/moremas/build-with-gemini into a `build-with-gemini/` directory under cwd:
   - If `git` is available: `git clone` (or `git pull` if it already exists).
   - If `git` is **not** available: don't install it. Download the GitHub tarball instead — `curl` and `tar` ship with macOS, Linux, and Windows 10+ out of the box:
     - macOS / Linux: `curl -L https://github.com/moremas/build-with-gemini/archive/refs/heads/main.tar.gz | tar xz && mv build-with-gemini-main build-with-gemini`
     - Windows (PowerShell): `curl.exe -L -o bwc.zip https://github.com/moremas/build-with-gemini/archive/refs/heads/main.zip; tar -xf bwc.zip; Rename-Item build-with-gemini-main build-with-gemini`
   - Re-running `/maker-setup` later just re-downloads (~500KB) — no update mechanism needed.
2. Invoke the `m5-onboard` skill and follow it to run `onboard/scripts/onboard.py --apps buddy` from inside `build-with-gemini/`, surfacing the download-mode button prompt to the user.
3. When done, tell the user how to launch Gemini Buddy and ask what they want to build next (see the `cardputer-buddy` skill for iterating).
